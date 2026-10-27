"""Da una sezione 768x1376 (stessa disposizione del castello) ricava cornice e tessere frontali di una dimora.
Uso: python3 tools/dimore/tagli_sezione.py <sezione.png> img/dimore/<id>/"""
import os, sys
from PIL import Image
POSTI = {"bagno": (112, 283, 376, 530), "camera": (392, 283, 656, 530), "ripostiglio": (112, 550, 312, 798), "corridoio": (328, 550, 440, 898),
         "cucina": (456, 550, 656, 898), "ingresso": (112, 918, 312, 1198), "soggiorno": (328, 918, 656, 1198), "balcone": (678, 400, 756, 1062)}
src, out = sys.argv[1], sys.argv[2].rstrip("/") + "/"
C = Image.open(src).convert("RGBA").resize((768, 1376), Image.LANCZOS)
os.makedirs(out + "tessere", exist_ok=True)
for t, b in POSTI.items(): C.crop(b).save(out + "tessere/" + t + ".webp", quality=92)
C.crop((0, 0, 768, 283)).save(out + "tetto.webp", quality=92)
C.crop((0, 1198, 768, 1376)).save(out + "base.webp", quality=92)
C.crop((0, 560, 112, 900)).save(out + "muro.webp", quality=92)
print("ok", out)
