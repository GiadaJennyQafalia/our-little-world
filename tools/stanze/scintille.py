#!/usr/bin/env python3
"""Toglie dalle immagini delle stanze (img/stanze: la Rocca) le scintille dorate dipinte nell'illustrazione
e ne scrive le posizioni: l'app le ridisegna come scintille animate solo quando la stanza non ha nessuna faccenda scaduta.
Le scintille sono piccole croci gialle isolate (7-11 px); candele, fuoco e dorature non vengono toccati: sono blob piu' grandi,
o vicini ad altri blob gialli.
Uso (dalla radice del repo): python3 tools/stanze/scintille.py [--prova]    (--prova: non scrive, salva solo un controllo visivo)
Stampa il dizionario delle posizioni (percentuali) da incollare in SCINTILLE di js/app.js."""
import glob, json, os, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
import cv2

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CARTELLE = ["img/stanze"]            # le stanze del Palazzo non hanno scintille dipinte (marmo chiaro): restano come sono
PROVA = "--prova" in sys.argv


def trova(a):
    """Candidati: piccole macchie dorate e luminose (top-hat), quasi quadrate, su sfondo scuro e senza calore intorno.
    Le fiamme hanno un alone caldo e un corpo sotto, le dorature stanno su oggetti chiari: non passano. Falsi positivi residui: ESCLUDI."""
    r, g, b, al = (a[..., i].astype(np.int32) for i in range(4))
    luce = (r * 3 + g * 2) // 5
    th = luce - ndi.grey_opening(luce, footprint=np.ones((13, 13)))              # solo cio' che e' piu' piccolo di 13 px e piu' chiaro di dintorni
    oro = (al > 200) & (th > 60) & (r - b > 45) & (r >= g - 10)
    oro = ndi.binary_closing(oro, structure=np.ones((3, 3)))
    lab, n = ndi.label(oro, structure=np.ones((3, 3)))
    caldo = (r - b > 60) & (r > 120)
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    out = []
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start; area = int((lab[sl] == i).sum())
        if not (5 <= w <= 18 and 5 <= h <= 18 and 12 <= area <= 130 and max(w, h) / min(w, h) <= 1.4 and .2 <= area / (w * h) <= .75): continue
        cx, cy = sl[1].start + w // 2, sl[0].start + h // 2
        y0, y1, x0, x1 = max(0, cy - 16), cy + 17, max(0, cx - 16), cx + 17
        d = np.hypot(xx[y0:y1, x0:x1] - cx, yy[y0:y1, x0:x1] - cy); ring = (d >= 9) & (d <= 15)
        if luce[y0:y1, x0:x1][ring].mean() > 85 or caldo[y0:y1, x0:x1][ring].sum() > 6: continue
        c = luce[max(0, cy - 3):cy + 4, max(0, cx - 3):cx + 4]               # le scintille grandi hanno un cuore quasi bianco e ampio; le piccole restano (sono polvere dorata)
        if c.max() < 225 or int((c > 150).sum()) < 12: continue
        out.append((cx, cy))
    return out


# Correzioni a mano (pixel dell'immagine 720 di larghezza): falsi positivi da togliere e scintille mancate da aggiungere.
ESCLUDI, AGGIUNGI = {}, {}


risultato = {}
for cart in CARTELLE:
    for f in sorted(glob.glob(os.path.join(RADICE, cart, "*.webp"))):
        im = Image.open(f).convert("RGBA"); a = np.array(im).astype(int)
        nome = os.path.relpath(f, RADICE); pts = [p for p in trova(a) if not any(abs(p[0] - e[0]) < 6 and abs(p[1] - e[1]) < 6 for e in ESCLUDI.get(nome, []))] + [tuple(p) for p in AGGIUNGI.get(nome, [])]
        risultato[nome] = [[round(x / im.width * 100, 1), round(y / im.height * 100, 1)] for x, y in pts]
        if PROVA:
            d = ImageDraw.Draw(im)
            for x, y in pts: d.ellipse((x - 9, y - 9, x + 9, y + 9), outline=(0, 255, 0, 255), width=2); d.text((x + 11, y - 5), f"{x},{y}", fill=(255, 255, 255, 255))
            os.makedirs("/tmp/scintille_prova", exist_ok=True); im.convert("RGB").save("/tmp/scintille_prova/" + nome.replace("/", "_").replace(".webp", ".png"))
            continue
        if not pts: continue
        mask = np.zeros(a.shape[:2], np.uint8)
        for x, y in pts: cv2.circle(mask, (int(round(x)), int(round(y))), 8, 255, -1)
        mask = cv2.bitwise_and(mask, ((a[..., 3] > 0).astype(np.uint8) * 255))
        rgb = cv2.inpaint(np.ascontiguousarray(a[..., :3].astype(np.uint8)), mask, 6, cv2.INPAINT_TELEA)
        new = np.dstack([rgb, a[..., 3].astype(np.uint8)])
        Image.fromarray(new, "RGBA").save(f, lossless=True, method=6)
print(json.dumps(risultato, separators=(",", ":")))
