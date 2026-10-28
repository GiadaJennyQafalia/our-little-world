#!/usr/bin/env python3
"""Compone le stanze modulari di una dimora e le scrive come tessere dell'app: img/dimore/<dimora>/tessere/<tipo>.webp.
Uso (dalla radice del repo): python3 tools/dimore/modulare/esporta.py castello reggia
Ogni stanza è larga W pixel del disegno (vedi LARGHEZZE) e alta 96, composta a Q volte (Q=6: 576 px di altezza).
Scrive anche, per ogni dimora, la tabella delle misure da incollare in SKIN[...].tessere.dim di js/app.js."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import componi
from PIL import Image

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
LARGHEZZE = {"bagno": 108, "camera": 108, "ripostiglio": 88, "corridoio": 56, "cucina": 88, "ingresso": 88, "soggiorno": 120,
             "balcone": 60, "cucina_soggiorno": 176, "studio": 120, "lavanderia": 128, "cantina": 128, "giardino": 124, "terrazzo": 124}

for dim in sys.argv[1:] or ["castello", "reggia"]:
    componi.usa(dim)
    out = os.path.join(RADICE, "img", "dimore", dim, "tessere"); misure = {}
    for tipo, W in LARGHEZZE.items():
        im, _ = componi.stanza(tipo, W)
        im = im.convert("RGB")
        im.save(os.path.join(out, tipo + ".webp"), quality=95, method=6)
        misure[tipo] = [im.width, im.height]
    print(dim, json.dumps(misure, sort_keys=True, separators=(",", ":")))
