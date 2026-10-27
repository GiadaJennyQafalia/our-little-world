"""Costruisce le immagini di Rocca di Pietranotte (stanze in più) e Palazzo d'Argentaluna dai file generati.
Uso: python3 tools/dimore/costruisci.py <cartella con i file originali>"""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from prepara import interno, pezzi_foglio, BUIO
A = sys.argv[1].rstrip("/") + "/"
R = os.path.join(os.path.dirname(__file__), "..", "..")
def salva(im, rel):
    p = os.path.join(R, rel); os.makedirs(os.path.dirname(p), exist_ok=True); im.save(p, quality=90); print(rel, im.size)
def tessera(pezzo):
    im = pezzo[4]; bb = im.getbbox(); im = im.crop(bb)
    fondo = Image.new("RGBA", im.size, BUIO + (255,)); fondo.alpha_composite(im); return fondo.convert("RGB")
def affianca(a, b):
    h = max(a.height, b.height); out = Image.new("RGB", (a.width + b.width, h), BUIO); out.paste(a, (0, h - a.height)); out.paste(b, (a.width, h - b.height)); return out
def carica(f): return Image.open(A + f).convert("RGB")

# ---- Rocca di Pietranotte: 5 interni in più e 6 tessere frontali
for f, t in (("2a98bf8e-image.jpg", "cantina"), ("bb7f0db4-image.jpg", "giardino"), ("8f779ce5-image.png", "cucina_soggiorno"), ("e2e29b77-image.jpg", "lavanderia"), ("58bd5461-image.jpg", "studio")):
    salva(interno(carica(f), soglia=10), f"img/stanze/{t}.webp")  # stanze scure: soglia bassa per non mangiare i muri
p = pezzi_foglio(carica("e0e3fa0e-image.jpg"), unisci=0)
for pz, t in zip(p, ["cucina_soggiorno", "studio", "lavanderia", "terrazzo", "giardino", "cantina"]): salva(tessera(pz), f"img/dimore/castello/tessere/{t}.webp")

# ---- Palazzo d'Argentaluna
D = "img/dimore/reggia/"
sez = carica("0abb7876-image.jpg").resize((768, 1376), Image.LANCZOS)
# il Palazzo ha le stanze un po' spostate rispetto al castello: riquadri misurati sulla sua sezione
POSTI = {"bagno": (102, 302, 322, 550), "camera": (332, 302, 622, 550), "ripostiglio": (100, 570, 292, 802), "corridoio": (303, 552, 405, 802),
         "cucina": (415, 570, 622, 802), "ingresso": (100, 822, 365, 1085), "soggiorno": (376, 822, 622, 1085), "balcone": (628, 690, 750, 1085)}
for t, b in POSTI.items(): salva(sez.crop(b), D + f"tessere/{t}.webp")
salva(sez.crop((0, 0, 768, 300)), D + "tetto.webp"); salva(sez.crop((0, 1085, 768, 1376)), D + "base.webp"); salva(sez.crop((0, 560, 100, 900)), D + "muro.webp")
salva(sez, D + "sezione.webp")
p = pezzi_foglio(carica("0f2ffd00-image.jpg"), unisci=0)
salva(affianca(tessera(p[0]), tessera(p[1])), D + "tessere/cucina_soggiorno.webp")
for pz, t in zip(p[2:], ["studio", "terrazzo", "giardino", "cantina"]): salva(tessera(pz), D + f"tessere/{t}.webp")
for f, t in (("998c968f-image.jpg", "bagno"), ("331abfed-image.jpg", "sgabuzzino"), ("5f3049a6-image.jpg", "cucina"), ("013def4f-image.jpg", "ingresso"),
             ("101ba23b-image.jpg", "soggiorno"), ("241c9faa-image.jpg", "balcone"), ("4783d3a9-image.jpg", "studio"), ("2011a290-image.jpg", "lavanderia"),
             ("eba1a29f-image.png", "cantina"), ("edb80060-image.jpg", "giardino")):
    salva(interno(carica(f)), D + f"stanze/{t}.webp")
cam = pezzi_foglio(carica("f2f96008-image.jpg"), unisci=0)[1]
salva(interno(cam[4]), D + "stanze/camera.webp")
tre = pezzi_foglio(carica("09f81c30-image.jpg"), unisci=0)
salva(interno(tre[0][4], corridoio=True), D + "stanze/corridoio.webp")
salva(interno(tre[1][4]), D + "stanze/cucina_soggiorno.webp")
salva(interno(tre[2][4]), D + "stanze/terrazzo.webp")
