#!/usr/bin/env python3
"""Ricompone il contorno della Rocca a partire dall'immagine del generatore (tools/dimore/modulare/castello/cornice/contorno_gen.jpg):
un unico rettangolo di pietra per tutte le stanze, con le torri accanto (mai dentro) e il portone d'ingresso in basso.
L'immagine ha il cielo e l'apertura in verde #00FF00. L'apertura del generatore è più stretta di quella che serve alle stanze,
quindi la si allarga ripetendo i merli (in alto) e un tratto liscio di muro (in basso, ai due lati del portone).
Uscite in img/dimore/castello/: tetto.webp, base.webp (con l'apertura trasparente), muro.webp e muro_dx.webp (fasce che si ripetono in verticale).
Stampa i numeri da mettere in SKIN.castello.cornice di js/app.js.
Uso (dalla radice del repo): python3 tools/dimore/contorno_rocca.py"""
import json, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GEN = os.path.join(RADICE, "tools/dimore/modulare/castello/cornice/contorno_gen.jpg")
OUT = os.path.join(RADICE, "img/dimore/castello/")
SKY = (54, 33, 49)                       # lo stesso cielo di prima (#362131)

# misure sull'immagine del generatore (pixel dell'originale)
X_SX0, X_SX1 = 37, 352                   # blocco sinistro: cielo + torre + lato del rettangolo, fino al bordo dell'apertura
X_DX0, X_DX1 = 1088, 1401                # blocco destro
CENTRO = (352, 1088)                     # l'apertura
Y_TETTO, Y_APERTURA, Y_BASE, Y_FINE = 376, 728, 1466, 2089
INS = 513                                # larghezza aggiunta all'apertura: 6 periodi di merli (85,5 px)
OUT_W = 1536                             # larghezza finale delle immagini

a = np.array(Image.open(GEN).convert("RGB")).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
verde = (g > 120) & (g > r + 45) & (g > b + 45)
lab, n = ndi.label(verde)
tot = np.bincount(lab.ravel())[1:]
cielo_l = 1 + int(np.argmax(tot)); aperta = verde & (lab != cielo_l)
cielo = verde & (lab == cielo_l)
# il verde sfumato sul bordo della pietra: si toglie dal cielo (1 px) e si scurisce quello che resta
bordo = ndi.binary_dilation(verde, iterations=1)
vicino = ndi.binary_dilation(verde, iterations=4) & ~bordo
a2 = a.copy()
mix = (a2[..., 0] + a2[..., 2]) // 2
a2[..., 1] = np.where(vicino, np.minimum(a2[..., 1], mix), a2[..., 1])
sk = ndi.binary_dilation(cielo, iterations=1)
a2[sk] = SKY
foro = ndi.binary_dilation(aperta, iterations=1)
alpha = np.where(foro, 0, 255).astype(np.uint8)
a2[foro] = (0, 0, 0)
rgba = np.dstack([a2.clip(0, 255).astype(np.uint8), alpha])


def colonne(tipo):
    """Indici delle colonne dell'originale, nell'ordine in cui compongono la larghezza finale."""
    sx = list(range(X_SX0, CENTRO[0])); dx = list(range(CENTRO[1], X_DX1))
    if tipo == "tetto":      # merli: la parte che si ripete va da un varco all'altro (6 periodi)
        xc = 505
        mezzo = list(range(CENTRO[0], xc)) + list(range(xc, xc + INS)) + list(range(xc, CENTRO[1]))
    else:                    # base: due tratti lisci di muro ai lati del portone, mai sopra la fiaccola o il portone
        per = 64; xs, xd = 436, 1003
        mezzo = list(range(CENTRO[0], xs)) + [404 + i % 58 for i in range(INS // 2 + 1)] + list(range(xs, xd)) + [972 + i % 54 for i in range(INS // 2)] + list(range(xd, CENTRO[1]))
    return np.array(sx + mezzo + dx)


def ridim(im, w, h=None):
    im = Image.fromarray(im)
    f = w / im.width
    return np.array(im.resize((w, max(1, round(im.height * f))), Image.LANCZOS))


def tessera_v(blocco, y0, y1):
    """Fascia che si ripete in verticale senza giunture: parte da y0 (dove finisce il tetto); si cerca la lunghezza L per cui le righe
    dopo la fine sono le più simili a quelle dell'inizio, così il taglio cade tra due righe di mattoni compatibili."""
    best = None
    for L in range(330, y1 - y0 - 10):
        d = 0
        for k in range(-6, 6):
            d += np.abs(blocco[y0 + k].astype(int) - blocco[y0 + L + k].astype(int)).mean()
        if best is None or d < best[0]: best = (d, L)
    return best[1]


out = {}
info = {}
for nome, tipo, (ya, yb) in (("tetto", "tetto", (Y_TETTO, Y_APERTURA)), ("base", "base", (Y_BASE, Y_FINE + 14))):
    cols = colonne(tipo)
    parte = rgba[ya:yb][:, cols]
    if nome == "base":
        parte = parte.copy()
        sotto = parte[Y_FINE - ya:]; sotto[...] = (*SKY, 255)       # qualche riga di cielo sotto lo zoccolo
    out[nome] = parte
Wg = out["tetto"].shape[1]
f = OUT_W / Wg
for nome in ("tetto", "base"):
    im = Image.fromarray(out[nome]); im = im.resize((OUT_W, round(im.height * f)), Image.LANCZOS)
    im.save(OUT + nome + ".webp", lossless=True, method=6); out[nome + "_px"] = im.size

strisce = {}
for nome, (x0, x1) in (("muro", (X_SX0, X_SX1)), ("muro_dx", (X_DX0, X_DX1))):
    blocco = rgba[:, x0:x1, :3]
    L = tessera_v(blocco, Y_APERTURA, Y_BASE)
    t = blocco[Y_APERTURA:Y_APERTURA + L]
    tre = np.concatenate([t, t, t], 0)                                   # per ridimensionare senza bordi alla giuntura
    w = round((x1 - x0) * f)
    ri = np.array(Image.fromarray(tre).resize((w, round(tre.shape[0] * f)), Image.LANCZOS))
    h3 = ri.shape[0] // 3
    Image.fromarray(ri[h3:2 * h3]).save(OUT + nome + ".webp", lossless=True, method=6)
    strisce[nome] = (w, h3, L)

css = 768 / OUT_W / 1.0          # px dell'immagine -> px dello schermo
tw, th = out["tetto_px"]; bw, bh = out["base_px"]
ov = round((Y_APERTURA + (1551 - Y_APERTURA) - Y_BASE) * f)       # parte della base che sale sopra il fondo dell'apertura (righe Y_BASE..1551)
ov = round((1551 - Y_BASE) * f)
res = dict(tetto=[768, round(th * css, 1)], base=[768, round(bh * css, 1), round(ov * css, 1)],
           muro=[round(strisce["muro"][0] * css, 1), round(strisce["muro"][1] * css, 1)],
           dx=[round(strisce["muro_dx"][0] * css, 1), round(strisce["muro_dx"][1] * css, 1)])
a0 = res["muro"][0]; a1 = round(768 - res["dx"][0], 1)
res["area"] = [a0, a1]
print(json.dumps(res), "tile", {k: v[2] for k, v in strisce.items()}, "px tetto", out["tetto_px"], "base", out["base_px"])
