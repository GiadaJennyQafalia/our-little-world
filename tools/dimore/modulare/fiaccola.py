#!/usr/bin/env python3
"""Disegna la fiaccola a muro della Rocca (castello/pezzi_x6/fiaccola.png): manico di legno in un anello di ferro, coppa, fiamma.
Si disegna a mezzo pixel del disegno (grana di Q/2 pixel) così ha la stessa finezza dei mobili ritagliati. Uso: python3 fiaccola.py"""
import os
from PIL import Image

Q = 6; G = Q // 2
PAL = {"o": (206, 78, 22), "m": (250, 148, 38), "c": (255, 226, 122), "k": (40, 28, 30), "I": (40, 34, 48), "i": (104, 94, 116),
       "W": (116, 72, 42), "w": (160, 108, 62), "d": (76, 46, 30)}
RIGHE = [
 ".....oo.....", ".....om.....", "....omm.o...", "....ommmo...", "...ommmmo...", "...ommccmo..", "..ommcccmo..", "..ommcccmo..",
 "..ommccmmo..", "...ommmmo...", "...oommoo...", "....oooo....",
 "..iiiiiiii..", "..IIIIIIII..", "...IIIIII...", ".....IIi....",
 "....wWWd....", "....wWWd....", "...IIIIII...", "....wWWd....", "....wWWd....", "....wWWd....", "....wWWd....",
 "..IIIIIIII..", "..IiIIIIiI..", "..IIIIIIII..",
]
im = Image.new("RGBA", (12 * G, len(RIGHE) * G), (0, 0, 0, 0))
for y, riga in enumerate(RIGHE):
    for x, c in enumerate(riga):
        if c != ".": im.paste(PAL[c] + (255,), (x * G, y * G, (x + 1) * G, (y + 1) * G))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "castello", "pezzi_x6", "fiaccola.png")
im.save(out); print(out, im.size)
