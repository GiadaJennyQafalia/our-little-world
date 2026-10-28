#!/usr/bin/env python3
"""Ritaglia i pezzi dai fogli di mobili su fondo verde e li riporta alla scala dei pixel del disegno.
Uso: python3 estrai.py foglio.jpg nome_sopra nome_sotto
Scrive pezzi/<stanza>_<n>.png (n da 1, da sinistra a destra) e un foglio di controllo controllo_<foglio>.png.
Le scritte del generatore (nomi, misure) vengono scartate perché sono basse e larghe."""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage

DIR = os.getcwd()   # lanciato dentro la cartella della dimora (castello/ o reggia/)
PX = 250 * int(os.environ.get("Q", 1))  # con Q=6 i pezzi escono 6 volte più grandi (cartella pezzi_x6);  larghezza del foglio in pixel del disegno: un divano viene ~40 px, come nelle misure scritte dal generatore


def verde(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (g > 120) & (g > r + 45) & (g > b + 45)


def pezzi(path):
    im = Image.open(path).convert("RGB")
    a = np.array(im).astype(int)
    H, W = a.shape[:2]
    pieno = ~verde(a)
    pieno = ndimage.binary_opening(pieno, iterations=2)
    lab, n = ndimage.label(ndimage.binary_dilation(pieno, iterations=4))
    out = []
    for i, sl in enumerate(ndimage.find_objects(lab)):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
        if h < 0.07 * H:          # scritte e briciole
            continue
        m = (lab[sl] == i + 1) & pieno[sl]
        out.append((sl, m))
    # due file: sopra e sotto la metà
    righe = [[], []]
    for sl, m in out:
        righe[0 if (sl[0].start + sl[0].stop) / 2 < H / 2 else 1].append((sl, m))
    return im, a, [sorted(r, key=lambda p: p[0][1].start) for r in righe]


def a_pixel(im, a, sl, m, k):
    rgb = a[sl].astype(np.uint8)
    # toglie il riflesso verde sui bordi
    g = rgb[..., 1].astype(int); lim = np.maximum(rgb[..., 0], rgb[..., 2]).astype(int)
    rgb[..., 1] = np.where(g > lim + 10, lim + 10, g).clip(0, 255).astype(np.uint8)
    al = (m * 255).astype(np.uint8)
    w, h = max(1, round(m.shape[1] / k)), max(1, round(m.shape[0] / k))
    pre = Image.fromarray(np.dstack([rgb, al]), "RGBA")
    rid = pre.resize((w, h), Image.BOX)
    r = np.array(rid)
    r[..., 3] = np.where(r[..., 3] > 110, 255, 0)
    return Image.fromarray(r, "RGBA")


if __name__ == "__main__":
    path, nomi = sys.argv[1], sys.argv[2:4]
    im, a, righe = pezzi(path)
    k = im.width / PX
    CART = "pezzi" if PX == 250 else "pezzi_x%d" % (PX // 250)
    os.makedirs(os.path.join(DIR, CART), exist_ok=True)
    ctrl = []
    for nome, riga in zip(nomi, righe):
        for j, (sl, m) in enumerate(riga):
            p = a_pixel(im, a, sl, m, k)
            p.save(os.path.join(DIR, CART, f"{nome}_{j + 1}.png"))
            ctrl.append((f"{nome}_{j + 1}", p))
        print(nome, len(riga), "pezzi")
    # foglio di controllo ingrandito 3x su fondo scuro
    Wc = sum(p.width * 3 + 12 for _, p in ctrl); Hc = max(p.height for _, p in ctrl) * 3 + 12
    c = Image.new("RGB", (Wc, Hc), (40, 34, 48)); x = 6
    for _, p in ctrl:
        q = p.resize((p.width * 3, p.height * 3), Image.NEAREST); c.paste(q, (x, Hc - q.height - 6), q); x += q.width + 12
    c.save(os.path.join(DIR, "controllo_" + "_".join(nomi) + ("" if PX == 250 else "_x%d" % (PX // 250)) + ".png")) if PX == 250 else None
