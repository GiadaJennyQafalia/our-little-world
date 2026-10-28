#!/usr/bin/env python3
"""Rende continuo il contorno della vista a piani: le due fasce laterali (muro.webp, muro_dx.webp) vengono allargate
fino a coincidere con la larghezza delle torri del tetto e della base, e si ripetono senza giunture verticali.
Uso (dalla radice): python3 tools/dimore/cornice_continua.py castello 32 24 79 87
   = dimora, bordo sinistro della torre nella fascia, dove deve arrivare (in basso), bordo destro della torre nella fascia destra, dove deve arrivare.
Poi aggiunge sotto la base uno zoccolo di pietra con un po' di terreno, così le torri non finiscono tagliate.
In alto la torre resta com'è (la larghezza del tetto): l'app la fa allargare piano piano con un clip-path (cornice.taper)."""
import sys, numpy as np
from PIL import Image
dim, sx0, sx1, dx0, dx1 = sys.argv[1], *map(int, sys.argv[2:6])
orig = f"tools/dimore/modulare/{dim}/cornice/"; out = f"img/dimore/{dim}/"

SKY = np.array([54, 33, 49])      # il cielo del tetto: lo stesso colore ai lati e intorno alla base

def vert(a, f=0.16):
    """Ripetizione senza giunture in verticale: le ultime righe sfumano nelle prime."""
    h = a.shape[0]; o = max(3, int(h * f)); core = a[:h - o].astype(float).copy()
    for i in range(o):
        k = (i + 1) / (o + 1); core[i] = a[i] * k + a[h - o + i] * (1 - k)
    return core.clip(0, 255).astype(np.uint8)

def adatta(a, da, a_, lato):
    """Allarga la parte di torre; il cielo ai margini si riempie con la sua colonna media."""
    h, w = a.shape[:2]
    if lato == "sx":            # cielo [0,da) -> [0,a_); torre [da,w) -> [a_,w)
        cielo = np.full((h, a_, 3), SKY)
        t = np.array(Image.fromarray(a[:, da:]).resize((w - a_, h), Image.LANCZOS))
        return np.concatenate([cielo.astype(np.uint8), t], 1)
    t = np.array(Image.fromarray(a[:, :da]).resize((a_, h), Image.LANCZOS))   # torre [0,da) -> [0,a_); cielo il resto
    cielo = np.full((h, w - a_, 3), SKY)
    return np.concatenate([t, cielo.astype(np.uint8)], 1)

L = np.array(Image.open(orig + "muro.webp").convert("RGB")); R = np.array(Image.open(orig + "muro_dx.webp").convert("RGB"))
L2 = vert(adatta(L, sx0, sx1, "sx")); R2 = vert(adatta(R, dx0, dx1, "dx"))
Image.fromarray(L2).save(out + "muro.webp", lossless=True); Image.fromarray(R2).save(out + "muro_dx.webp", lossless=True)
print("muro", L2.shape, "muro_dx", R2.shape)

# --- zoccolo sotto la base ---
B = np.array(Image.open(orig + "base.webp").convert("RGB")).astype(float); h, w = B.shape[:2]
ZOC, TER = 16, 22
vecchio = B[:, 2:8].reshape(-1, 3).mean(0)
B[np.abs(B - vecchio).sum(2) < 24] = SKY     # il cielo della base prende il colore del tetto
cielo_sx = cielo_dx = SKY.astype(float)
nuova = np.zeros((h + ZOC + TER, w, 3)); nuova[:h] = B
for y in range(h, h + ZOC + TER):
    nuova[y, :w // 2] = cielo_sx; nuova[y, w // 2:] = cielo_dx
x0, x1 = 14, w - 14                                   # lo zoccolo sporge un po' oltre le torri
pietra = B[h - 14:h - 2]                                # le ultime righe di mattoni, ripetute
for i in range(ZOC):
    riga = pietra[i % len(pietra)]
    for x in range(x0, x1):
        sx = min(max(x, 26), w - 27)                    # ai bordi si ripetono le colonne dentro la torre
        c = riga[sx] * 0.82
        if i < 2: c = riga[sx] * 1.12 + 14              # bordo chiaro in cima
        if i >= ZOC - 2: c = riga[sx] * 0.55            # ombra in fondo
        nuova[h + i, x] = c
for j in range(TER):                                    # ombra morbida sul terreno
    k = 0.72 + 0.28 * j / TER
    for x in range(x0 - 6, x1 + 6):
        nuova[h + ZOC + j, x] = (cielo_sx if x < w // 2 else cielo_dx) * k
Image.fromarray(nuova.clip(0, 255).astype(np.uint8)).save(out + "base.webp", lossless=True)
print("base", nuova.shape)
print("cielo sx", cielo_sx.round(), "dx", cielo_dx.round())
