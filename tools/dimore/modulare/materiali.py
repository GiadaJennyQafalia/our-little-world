#!/usr/bin/env python3
"""Ritaglia i 9 campioni di un foglio di materiali (griglia 3x3 su fondo verde).
Uso: python3 materiali.py foglio.png muri|pavimenti  ->  materiali/<tipo>_<n>.png (n da 1, per righe)."""
import sys, os
import numpy as np
from PIL import Image

DIR = os.path.dirname(os.path.abspath(__file__))


def verde(a):
    r, g, b = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
    return (g > 120) & (g > r + 45) & (g > b + 45)


def tratti(pieno, minimo):
    """Tratti consecutivi in cui la proiezione è 'piena' (fuori dalle fasce verdi)."""
    out, s = [], None
    for i, v in enumerate(list(pieno) + [False]):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s >= minimo: out.append((s, i))
            s = None
    return out


if __name__ == "__main__":
    path, tipo = sys.argv[1], sys.argv[2]
    im = Image.open(path).convert("RGB"); a = np.array(im)
    g = verde(a)
    cols = tratti(g.mean(0) < 0.5, im.width // 8)
    rows = tratti(g.mean(1) < 0.5, im.height // 8)
    os.makedirs(os.path.join(DIR, "materiali"), exist_ok=True)
    n = 0
    for y0, y1 in rows:
        for x0, x1 in cols:
            n += 1
            m = 4  # margine: via i bordi sfumati nel verde
            im.crop((x0 + m, y0 + m, x1 - m, y1 - m)).save(os.path.join(DIR, "materiali", f"{tipo}_{n}.png"))
    print(tipo, n, "campioni", cols, rows)
