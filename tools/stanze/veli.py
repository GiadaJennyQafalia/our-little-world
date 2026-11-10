#!/usr/bin/env python3
"""Disegna i 'veli' dello sporco delle stanze, in pixel art: mucchi di polvere (3 misure), ragnatela d'angolo (nell'angolo dove si incontrano
le due pareti, in prospettiva isometrica), ragnatela piatta (per le miniature) e ragnetto. Scrive img/veli/*.png.
Con --posizioni calcola, per ogni illustrazione di stanza, dove mettere i mucchi (lungo i bordi del pavimento) e l'angolo della ragnatela,
e stampa il dizionario da incollare in VELI di js/app.js.
Uso (dalla radice del repo): python3 tools/stanze/veli.py [--posizioni]"""
import glob, json, math, os, random, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(RADICE, "img/veli")
os.makedirs(OUT, exist_ok=True)


def mucchio(w, h, seme):
    """Un mucchietto di polvere grigio-lilla: profilo irregolare, luce in alto, ombra in basso, qualche granello attorno."""
    r = random.Random(seme)
    im = Image.new("RGBA", (w + 4, h + 3), (0, 0, 0, 0)); px = im.load()
    chiaro, medio, scuro, ombra = (150, 142, 160, 255), (118, 110, 130, 255), (86, 79, 100, 255), (20, 14, 30, 80)
    for x in range(w):
        t = (2 * x / (w - 1) - 1)
        alt = max(1, round(h * (1 - abs(t) ** 2.5) ** 0.7 + r.choice((-1, 0, 0, 1)) * (0 if h < 6 else 1)))
        alt = min(alt, h)
        for k in range(alt):
            y = h - 1 - k + 1
            px[x + 2, y] = chiaro if (k == alt - 1 and alt > 2) or (k >= alt - 2 and t < 0.15 and alt > 4) else (scuro if k == 0 and alt > 2 else medio)
        px[x + 2, h + 1] = ombra if px[x + 2, h + 1][3] == 0 else px[x + 2, h + 1]
    for _ in range(max(2, w // 4)):                                       # granelli sparsi
        gx, gy = r.randrange(0, w + 4), r.randrange(max(0, h - 3), h + 2)
        if px[gx, gy][3] == 0: px[gx, gy] = r.choice((medio, scuro, (118, 110, 130, 170)))
    return im


def linea(d, a, b, col):
    d.line([a, b], fill=col, width=1)


def ragnatela_angolo():
    """Ragnatela nell'angolo in alto tra due pareti viste in isometrica: il vertice sta in alto al centro, i due lati scendono con pendenza 1/2,
    lo spigolo verticale scende al centro. Pochi fili radiali, spirali che cedono, tratti mancanti e le due parti non uguali."""
    W, H = 60, 40; im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    r = random.Random(21); ap = (30, 1)
    col = lambda a: (236, 232, 244, a)
    for lato, scala, raggi in ((-1, 1.0, 4), (1, 0.78, 4)):
        e1 = (ap[0] + lato * 28 * scala, ap[1] + 14 * scala); e2 = (ap[0] + lato * 2, ap[1] + 31 * scala)
        punti = []
        for k in range(raggi + 1):
            t = k / raggi; p = (e1[0] + (e2[0] - e1[0]) * t, e1[1] + (e2[1] - e1[1]) * t); cedi = 0.2 * math.sin(math.pi * t) + r.uniform(-0.04, 0.04)
            punti.append((p[0] + (ap[0] - p[0]) * cedi, p[1] + (ap[1] - p[1]) * cedi))
        for i, p in enumerate(punti):
            if i == raggi: continue                                         # lo spigolo e' uno solo (lo disegna il lato sinistro)
            linea(d, ap, (round(p[0]), round(p[1])), col(190))
        for ring in (0.38, 0.68, 1.0):
            for k in range(raggi):
                if r.random() < 0.22: continue
                a = [ap[0] + (punti[k][0] - ap[0]) * ring + r.uniform(-.6, .6), ap[1] + (punti[k][1] - ap[1]) * ring + r.uniform(-.6, .6)]
                b = [ap[0] + (punti[k + 1][0] - ap[0]) * ring + r.uniform(-.6, .6), ap[1] + (punti[k + 1][1] - ap[1]) * ring + r.uniform(-.6, .6)]
                mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
                m = (mx + (ap[0] - mx) * 0.14, my + (ap[1] - my) * 0.14 + 0.8)
                linea(d, (round(a[0]), round(a[1])), (round(m[0]), round(m[1])), col(140)); linea(d, (round(m[0]), round(m[1])), (round(b[0]), round(b[1])), col(140))
    return im


def ragnatela_lato():
    """Ragnatela piatta d'angolo (per le miniature della dimora): vertice in alto a sinistra."""
    W, H = 26, 22; im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); r = random.Random(3)
    col = lambda a: (232, 228, 240, a)
    pts = []
    for k in range(6):
        ang = math.radians(8 + k * 15.5); pts.append((math.cos(ang), math.sin(ang)))
    for ring in (0.3, 0.55, 0.8, 1.0):
        for k in range(5):
            if r.random() < 0.15 and ring < 1: continue
            a = (pts[k][0] * 24 * ring, pts[k][1] * 20 * ring); b = (pts[k + 1][0] * 24 * ring, pts[k + 1][1] * 20 * ring)
            m = ((a[0] + b[0]) / 2 * 0.9, (a[1] + b[1]) / 2 * 0.9)
            linea(d, (round(a[0]), round(a[1])), (round(m[0]), round(m[1])), col(150)); linea(d, (round(m[0]), round(m[1])), (round(b[0]), round(b[1])), col(150))
    for p in pts: linea(d, (0, 0), (round(p[0] * 24), round(p[1] * 20)), col(210))
    return im


def ragno():
    """Ragnetto di 9x7 pixel: corpo scuro, due puntini di luce, otto zampe piegate."""
    W, H = 11, 8; im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); px = im.load()
    corpo, luce, zampa = (40, 30, 54, 255), (235, 90, 110, 255), (132, 120, 150, 255)
    for x, y in ((4, 3), (5, 3), (6, 3), (4, 4), (5, 4), (6, 4), (5, 2), (5, 5)): px[x, y] = corpo
    px[4, 2] = corpo; px[6, 2] = corpo
    px[4, 3] = luce; px[6, 3] = luce
    for lato in (-1, 1):
        cx = 5
        for (dx, dy), seq in (((1, 0), [(3, 0), (2, 1)]), ((1, 1), [(3, 2), (1, 2)]), ((1, 3), [(3, 4), (1, 5)]), ((1, 4), [(3, 5), (2, 7)])):
            pass
        for y0, tratto in ((2, [(2, 1), (3, 0)]), (3, [(3, 2), (4, 2)]), (4, [(3, 4), (4, 5)]), (5, [(3, 6), (4, 7)])):
            x, y = cx + lato * 2, y0
            for (ddx, yy) in tratto:
                xx = cx + lato * ddx
                if 0 <= xx < W and 0 <= yy < H: px[xx, yy] = zampa
    return im


def sprite():
    for nome, (w, h) in {"mucchio_s": (11, 5), "mucchio_m": (16, 7), "mucchio_l": (22, 9)}.items():
        mucchio(w, h, nome).save(f"{OUT}/{nome}.png")
    ragnatela_angolo().save(f"{OUT}/ragnatela_angolo.png"); ragnatela_lato().save(f"{OUT}/ragnatela_lato.png"); ragno().save(f"{OUT}/ragno.png")


def forma(f):
    """Maschera dell'illustrazione: l'alpha se c'e', altrimenti tutto cio' che non e' lo sfondo nero collegato al bordo."""
    a = np.array(Image.open(f).convert("RGBA")).astype(int)
    if a[..., 3].min() < 200: return a[..., 3] > 40
    scuro = a[..., :3].max(2) < 14
    lab, _ = ndi.label(scuro)
    bordo = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    return ~np.isin(lab, list(bordo))


def posizioni():
    out = {}
    for f in sorted(glob.glob(os.path.join(RADICE, "img/stanze/*.webp")) + glob.glob(os.path.join(RADICE, "img/dimore/reggia/stanze/*.webp"))):
        m = forma(f); H, W = m.shape
        nome = os.path.relpath(f, RADICE); r = random.Random(nome)
        ys = lambda x: (H - 1 - int(np.argmax(m[::-1, x]))) if m[:, x].any() else None
        riga = np.where(m.any(1))[0][0]; xs = np.where(m[riga])[0]; ax = int(xs.mean())       # il punto piu' alto della sagoma = spigolo tra le due pareti
        scarto = 16 if "reggia" in nome else 64
        pts = []
        for fx, mis in ((0.24, "m"), (0.74, "l"), (0.49, "s"), (0.12, "s"), (0.62, "m"), (0.86, "m"), (0.36, "l")):
            x = int(W * (fx + r.uniform(-0.04, 0.04))); y = ys(x)
            if y is None: continue
            off = r.randint(42, 120)
            pts.append([round(x / W * 100, 1), round((y - off) / H * 100, 1), mis])
        out[nome] = {"angolo": [round(ax / W * 100, 1), round((riga + scarto) / H * 100, 1)], "mucchi": pts}
    return out


if __name__ == "__main__":
    sprite()
    if "--posizioni" in sys.argv: print(json.dumps(posizioni(), separators=(",", ":")))
