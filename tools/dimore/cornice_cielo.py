#!/usr/bin/env python3
"""Uniforma il cielo del contorno di una dimora: nelle fasce laterali e nella base il cielo (che nelle immagini originali
è un gradiente diverso da quello del tetto, e a ogni ripetizione della fascia fa uno scalino) diventa un colore unico,
quello delle ultime righe del tetto. Le torri e le decorazioni non cambiano.
Uso (dalla radice): python3 tools/dimore/cornice_cielo.py reggia 17 27 64"""
import sys, numpy as np
from PIL import Image
dim = sys.argv[1]; SKY = np.array(list(map(int, sys.argv[2:5])))
orig = f"tools/dimore/modulare/{dim}/cornice/"; out = f"img/dimore/{dim}/"

def piatta(a, lato, soglia=40):
    """Cambia in SKY i pixel simili al cielo di quella riga (preso dal bordo esterno della fascia)."""
    a = a.astype(int); rif = a[:, 2:3] if lato == "sx" else a[:, -3:-2]
    m = np.abs(a - rif).sum(2) < soglia
    a[m] = SKY; return a.astype(np.uint8)

for nome, lato in (("muro", "sx"), ("muro_dx", "dx")):
    a = np.array(Image.open(orig + nome + ".webp").convert("RGB"))
    Image.fromarray(piatta(a, lato)).save(out + nome + ".webp", lossless=True)
B = np.array(Image.open(orig + "base.webp").convert("RGB")).astype(int)
rif = B[0, 3]; top = B[:40]; m = np.abs(top - rif).sum(2) < 36; top[m] = SKY; B[:40] = top
Image.fromarray(B.astype(np.uint8)).save(out + "base.webp", lossless=True)
print("fatto", dim)
