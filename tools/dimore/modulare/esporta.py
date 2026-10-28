#!/usr/bin/env python3
"""Compone le stanze modulari di una dimora e le scrive come tessere dell'app: img/dimore/<dimora>/tessere/<tipo>.webp.
Uso (dalla radice del repo): python3 tools/dimore/modulare/esporta.py castello reggia
Ogni stanza è larga W pixel del disegno (vedi LARGHEZZE) e alta 96; l'app la scala a seconda della casa.
Scrive anche, per ogni dimora, la tabella delle misure da incollare in SKIN[...].tessere.dim di js/app.js."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import componi
from PIL import Image

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SCALA = 3
LARGHEZZE = {"bagno": 100, "camera": 100, "ripostiglio": 84, "corridoio": 56, "cucina": 84, "ingresso": 80, "soggiorno": 112,
             "balcone": 52, "cucina_soggiorno": 168, "studio": 112, "lavanderia": 124, "cantina": 124, "giardino": 124, "terrazzo": 124}

for dim in sys.argv[1:] or ["castello", "reggia"]:
    componi.usa(dim)
    out = os.path.join(RADICE, "img", "dimore", dim, "tessere"); misure = {}
    for tipo, W in LARGHEZZE.items():
        im, _ = componi.stanza(tipo, W)
        im = im.resize((W * SCALA, componi.H * SCALA), Image.NEAREST).convert("RGB")
        im.save(os.path.join(out, tipo + ".webp"), lossless=True, quality=100, method=6)
        misure[tipo] = [im.width, im.height]
    print(dim, json.dumps(misure, sort_keys=True, separators=(",", ":")))
