#!/usr/bin/env python3
"""Ritaglia le strisce orizzontali (fregi: boiserie, battiscopa, fascia, piastrelle, balaustra, siepe) da un foglio
dove sono impilate su fondo verde. Uso (dentro castello/ o reggia/): python3 ../fregi.py fregi.jpg
Scrive fregi/fregio_<n>.png (n da 1, dall'alto in basso), con il verde reso trasparente."""
import sys, os
import numpy as np
from PIL import Image

DIR = os.getcwd()


def verde(a):
    r, g, b = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
    return (g > 120) & (g > r + 45) & (g > b + 45)


if __name__ == "__main__":
    im = Image.open(sys.argv[1]).convert("RGB"); a = np.array(im); g = verde(a)
    pieno = (~g).mean(1) > 0.2
    tratti, s = [], None
    for y, v in enumerate(list(pieno) + [False]):
        if v and s is None: s = y
        if not v and s is not None:
            if y - s >= 20: tratti.append((s, y))
            s = None
    os.makedirs(os.path.join(DIR, "fregi"), exist_ok=True)
    for n, (y0, y1) in enumerate(tratti, 1):
        rgba = np.dstack([a[y0:y1], np.where(g[y0:y1], 0, 255).astype(np.uint8)])
        Image.fromarray(rgba, "RGBA").save(os.path.join(DIR, "fregi", f"fregio_{n}.png"))
        print(n, y1 - y0, "px")
