#!/usr/bin/env python3
"""Rende continuo il contorno della vista a piani: le due fasce laterali (muro.webp, muro_dx.webp) vengono allargate
fino a coincidere con la larghezza delle torri del tetto e della base, e si ripetono senza giunture verticali.
Uso (dalla radice): python3 tools/dimore/cornice_continua.py castello 32 17 79 95
   = dimora, bordo sinistro della torre nella fascia, dove deve arrivare, bordo destro della torre nella fascia destra, dove deve arrivare."""
import sys, numpy as np
from PIL import Image
dim, sx0, sx1, dx0, dx1 = sys.argv[1], *map(int, sys.argv[2:6])
orig = f"tools/dimore/modulare/{dim}/cornice/"; out = f"img/dimore/{dim}/"

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
        cielo = np.repeat(a[:, 2:max(3, da - 2)].mean(1, keepdims=True), a_, 1)
        t = np.array(Image.fromarray(a[:, da:]).resize((w - a_, h), Image.LANCZOS))
        return np.concatenate([cielo.astype(np.uint8), t], 1)
    t = np.array(Image.fromarray(a[:, :da]).resize((a_, h), Image.LANCZOS))   # torre [0,da) -> [0,a_); cielo il resto
    cielo = np.repeat(a[:, da + 2:w - 2].mean(1, keepdims=True), w - a_, 1)
    return np.concatenate([t, cielo.astype(np.uint8)], 1)

L = np.array(Image.open(orig + "muro.webp").convert("RGB")); R = np.array(Image.open(orig + "muro_dx.webp").convert("RGB"))
L2 = vert(adatta(L, sx0, sx1, "sx")); R2 = vert(adatta(R, dx0, dx1, "dx"))
Image.fromarray(L2).save(out + "muro.webp", lossless=True); Image.fromarray(R2).save(out + "muro_dx.webp", lossless=True)
print("muro", L2.shape, "muro_dx", R2.shape)
