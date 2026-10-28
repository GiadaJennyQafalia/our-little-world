#!/usr/bin/env python3
"""Compone le stanze modulari della vista dimora: muro + zoccolatura/battiscopa + pavimento (dai campioni di
materiale) e i mobili ritagliati sopra. Le misure delle ricette sono in 'pixel del disegno' (stanza alta 96); l'immagine
esce Q volte più grande (Q=6 di solito) usando i pezzi ritagliati ad alta risoluzione (cartella pezzi_x6, estrai.py con Q=6).
POSTI=1 lascia liberi un posto a terra per le reliquie e uno a parete per i dipinti (servono solo se la stanza si apre).

Uso: python3 componi.py castello|reggia   -> <dimora>/prova.png (ogni stanza stretta e larga)
     import componi; componi.usa("reggia"); componi.stanza(nome, W)  -> (immagine, posti)

Le cartelle castello/ e reggia/ contengono: pezzi_x6/ (mobili), materiali/ (muri e pavimenti, materiali.py), fregi/ (fregi.py)."""
import os, random, sys
import numpy as np
from PIL import Image, ImageDraw

DIR = os.path.dirname(os.path.abspath(__file__))
H, MURO, BATT = 96, 68, 3          # altezza stanza, riga dove finisce il muro, spessore battiscopa (pixel del disegno)
Q = int(os.environ.get("Q", 6))     # pixel dell'immagine per pixel del disegno
POSTI = os.environ.get("POSTI", "0") == "1"
RELIQUIA = (18, 20)                 # posto a terra (larghezza, altezza) per una reliquia
DIPINTO = (18, 20)                  # posto a parete per un dipinto o un arazzo
CIMA_DIPINTO = 20                   # riga della cima dei dipinti
BASE, CFG = None, None              # dimora in uso (vedi usa())
S = lambda v: int(round(v * Q))     # misura del disegno -> pixel dell'immagine


class Pz:
    """Un pezzo ritagliato: .im è l'immagine, .width/.height sono in pixel del disegno."""
    def __init__(s, im): s.im = im; s.width = im.width / Q; s.height = im.height / Q


def carica(nome):
    if nome.startswith("pezzi/") and Q > 1: nome = "pezzi_x%d/" % Q + nome[6:]
    return Image.open(os.path.join(BASE, nome)).convert("RGBA")


def senza_giunture(t, asse_x=True, asse_y=False, f=0.18):
    """Rende il campione ripetibile: i bordi opposti sfumano l'uno nell'altro."""
    a = np.array(t).astype(float)
    if asse_x:
        w = a.shape[1]; o = max(2, int(w * f)); core = a[:, :w - o].copy()
        for i in range(o):
            k = (i + 1) / (o + 1); core[:, i] = a[:, i] * k + a[:, w - o + i] * (1 - k)
        a = core
    if asse_y:
        h = a.shape[0]; o = max(2, int(h * f)); core = a[:h - o].copy()
        for i in range(o):
            k = (i + 1) / (o + 1); core[i] = a[i] * k + a[h - o + i] * (1 - k)
        a = core
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def grade(t, sat=0.55, mult=(0.80, 0.72, 0.92), luce=0.85):
    """Porta un campione verso la palette della Rocca: meno saturo, più viola, più scuro."""
    a = np.array(t).astype(float); rgb = a[..., :3]
    grigio = rgb.mean(2, keepdims=True); rgb = grigio + (rgb - grigio) * sat
    a[..., :3] = rgb * np.array(mult) * luce
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def ripeti(t, w, h):
    out = Image.new("RGBA", (w, h))
    for y in range(0, h, t.height):
        for x in range(0, w, t.width):
            out.paste(t, (x, y))
    return out


def muro(n, alto):
    t = carica(f"materiali/muri_{n}.png"); s = S(alto) / t.height
    t = t.resize((max(8, round(t.width * s)), S(alto)), Image.LANCZOS)
    return senza_giunture(t, True, True)


def pavimento(n, w=96, h=30, **g):
    t = carica(f"materiali/pavimenti_{n}.png").resize((S(w), S(h)), Image.LANCZOS)   # schiacciato in verticale: sembra a terra
    t = senza_giunture(t, True, False)
    return grade(t, **g) if CFG["gradare"] else t


def fregio(n, h, W):
    """Striscia di bordo n (foglio fregi) alta h pixel del disegno, ripetuta per tutta la larghezza W."""
    t = carica(f"fregi/fregio_{n}.png"); s = S(h) / t.height
    t = t.resize((max(8, round(t.width * s)), S(h)), Image.LANCZOS)
    a = np.array(t); a[..., 3] = np.where(a[..., 3] > 110, 255, 0)
    return ripeti(senza_giunture(Image.fromarray(a, "RGBA"), True, False, 0.1), S(W), S(h))


def balaustra(img):
    d = ImageDraw.Draw(img); top = MURO - 20
    pietra, luce, buio = (92, 84, 104), (122, 112, 134), (52, 46, 62)
    d.rectangle((0, MURO - 4, img.width, MURO - 1), fill=pietra); d.line((0, MURO - 4, img.width, MURO - 4), fill=luce)
    for x in range(2, img.width, 6):
        d.rectangle((x, top + 3, x + 2, MURO - 5), fill=pietra); d.line((x + 2, top + 3, x + 2, MURO - 5), fill=buio)
        d.point((x, top + 8), fill=luce); d.point((x + 1, top + 12), fill=buio)
    d.rectangle((0, top, img.width, top + 3), fill=pietra); d.line((0, top, img.width, top), fill=luce); d.line((0, top + 3, img.width, top + 3), fill=buio)


def siepe(img):
    rnd = random.Random(7); d = ImageDraw.Draw(img); top = MURO - 18
    for x in range(img.width):
        t = top + int(2 * np.sin(x / 3.1) + rnd.random() * 2)
        for y in range(t, MURO):
            v = rnd.random()
            col = (34, 58, 40) if v < .55 else (46, 76, 50) if v < .85 else (24, 40, 30)
            if y == t: col = (64, 96, 62)
            d.point((x, y), fill=col)


def sul_disegno(img, W, f):
    """Disegna con f a risoluzione 1 (pixel del disegno) e porta il risultato a Q volte, sopra img."""
    capa = Image.new("RGBA", (W, H)); f(capa)
    img.alpha_composite(capa.resize((S(W), S(H)), Image.NEAREST))


def sfondo(W, r):
    """Muro, zoccolatura, fascia, pavimento e bordo di una stanza larga W, secondo la ricetta r."""
    img = Image.new("RGBA", (S(W), S(H))); d = ImageDraw.Draw(img)
    img.paste(ripeti(muro(*r["m_alto"]), S(W), S(MURO)), (0, 0))
    mb = r.get("m_basso")
    if isinstance(mb, tuple) and mb and mb[0] == "f":              # zoccolatura da striscia: ("f", n, altezza)
        _, n, alt = mb; img.alpha_composite(fregio(n, alt, W), (0, S(MURO - alt)))
    elif mb:                                                        # zoccolatura da campione di muro
        n, h_t, alt = mb
        img.paste(ripeti(muro(n, h_t), S(W), S(alt)), (0, S(MURO - alt)))
        d.rectangle((0, S(MURO - alt - 2), S(W), S(MURO - alt) - 1), fill=(70, 46, 40)); d.rectangle((0, S(MURO - alt - 2), S(W), S(MURO - alt - 2) + Q - 1), fill=(96, 66, 54))
    fa = r.get("fascia")
    if fa and fa[0] == "f":                                         # fascia da striscia: ("f", n, altezza, riga)
        _, n, alt, y = fa; img.alpha_composite(fregio(n, alt, W), (0, S(y)))
    elif fa:                                                        # fascia disegnata: (riga, colore)
        y, col = fa
        d.rectangle((0, S(y), S(W), S(y + 3) - 1), fill=col); d.rectangle((0, S(y), S(W), S(y) + Q - 1), fill=tuple(min(255, c + 25) for c in col))
        for x in range(1, W, 6): d.rectangle((S(x), S(y + 2), S(x + 1) - 1, S(y + 3) - 1), fill=tuple(max(0, c - 30) for c in col))
    img.paste(ripeti(pavimento(*r["pav"], **(r.get("pav_g") or {})), S(W), S(H - MURO)), (0, S(MURO)))
    bordo, batt = r.get("bordo"), r.get("batt", (52, 36, 34))
    d = ImageDraw.Draw(img)
    if bordo == "balaustra": sul_disegno(img, W, balaustra)
    elif bordo == "siepe": sul_disegno(img, W, siepe)
    elif isinstance(bordo, tuple):                                  # bordo da striscia: ("f", n, altezza), appoggiato al pavimento
        _, n, alt = bordo; img.alpha_composite(fregio(n, alt, W), (0, S(MURO - alt)))
    elif isinstance(batt, tuple) and batt and batt[0] == "f":       # battiscopa da striscia: ("f", n, altezza)
        _, n, alt = batt; img.alpha_composite(fregio(n, alt, W), (0, S(MURO - alt)))
    elif batt:
        d.rectangle((0, S(MURO - BATT), S(W), S(MURO) - 1), fill=batt); d.rectangle((0, S(MURO - BATT), S(W), S(MURO - BATT) + Q - 1), fill=tuple(c + 24 for c in batt))
    # luce: ombra dal soffitto (non all'aperto), ombra del muro sul pavimento, bordi della sezione
    a = np.array(img).astype(float); y = (np.arange(S(H))[:, None] + .5) / Q; ombra = np.ones((S(H), 1)); lm = CFG["luce_min"]
    m = S(MURO)
    if not bordo: ombra[:m] *= (lm + (1 - lm) * np.clip(y[:m] / (MURO * 0.55), 0, 1))
    ombra[m:] *= (0.62 + 0.38 * np.clip((y[m:] - MURO) / 6, 0, 1))
    x = (np.arange(S(W))[None, :] + .5) / Q; lati = 0.6 + 0.4 * np.clip(np.minimum(x, W - x) / 7, 0, 1)
    a[..., :3] *= (ombra * lati)[..., None]
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def pezzo(nome):
    if isinstance(nome, tuple):                  # gruppo: pezzi affiancati (sedia-tavolo-sedia, scopa e secchio…)
        ps = [carica(f"pezzi/{n}.png") for n in nome]
        g = Image.new("RGBA", (sum(p.width for p in ps) + (len(ps) - 1) * Q, max(p.height for p in ps))); x = 0
        for p in ps: g.alpha_composite(p, (x, g.height - p.height)); x += p.width + Q
        return Pz(g)
    return Pz(carica(f"pezzi/{nome}.png"))


def appoggia(img, p, cx, base, ombra=True):
    x, y = int(S(cx) - p.im.width / 2), int(S(base) - p.im.height)
    if ombra:
        om = Image.new("RGBA", img.size); ImageDraw.Draw(om).ellipse((x + 2 * Q, S(base) - 2 * Q, x + p.im.width - 2 * Q, S(base) + 2 * Q), fill=(10, 6, 16, 110))
        img.alpha_composite(om)
    img.alpha_composite(p.im, (x, y))


def appendi(img, p, cx, cima):
    img.alpha_composite(p.im, (int(S(cx) - p.im.width / 2), S(cima)))


def tappeto(img, p, cx, base, schiaccia=3):
    q = p.im.resize((p.im.width, max(3, p.im.height // schiaccia)), Image.LANCZOS)
    img.alpha_composite(q, (int(S(cx) - q.width / 2), S(base) - q.height))


# ----------------------------------------------------------------------------------------------------------------
# Ricette. pav_mobili: (pezzo o gruppo, riga dei piedi, priorità) da sinistra a destra; nelle stanze strette si
# tolgono prima i mobili con priorità più bassa. "R" è il posto libero per una reliquia (con un dipinto sopra).
# appesi: (pezzo, sopra quale mobile, riga della cima). tappeti / davanti: (pezzo, sotto/davanti a quale mobile, riga).
# ----------------------------------------------------------------------------------------------------------------
STANZE_CASTELLO = {
 "soggiorno": dict(m_alto=(1, 40), m_basso=(7, 36, 22), pav=(2,),
     pav_mobili=[("soggiorno_4", 83, 2), ("soggiorno_3", 81, 5), "R", ("soggiorno_1", 86, 4), ("soggiorno_2", 86, 1)],
     appesi=[("soggiorno_6", "soggiorno_1", 18)], tappeti=[("camera_5", "soggiorno_1", 93)], davanti=[("soggiorno_5", "soggiorno_1", 92)]),
 "camera": dict(m_alto=(2, 56), fascia=(30, (78, 62, 84)), pav=(1,),
     pav_mobili=[("camera_2", 82, 3), ("camera_3", 84, 2), ("camera_1", 87, 5), "R", ("camera_4", 83, 1)],
     appesi=[("camera_6", "camera_1", 10)], tappeti=[("camera_5", "camera_1", 93)]),
 "cucina": dict(m_alto=(8, 44), pav=(5,),
     pav_mobili=[("cucina_1", 82, 5), ("cucina_2", 82, 4), "R", ("cucina_3", 81, 2), ("cucina_4", 88, 3)],
     appesi=[("cucina_7", "cucina_2", 16), ("cucina_6", "cucina_1", 24)]),
 "bagno": dict(m_alto=(2, 56), m_basso=(6, 30, 28), pav=(6,), pav_g=dict(sat=.3, mult=(.58, .53, .68), luce=.72),
     pav_mobili=[("bagno_1", 88, 5), ("bagno_2", 84, 4), "R", ("bagno_4", 76, 1), ("bagno_3", 84, 4.2)],
     appesi=[("bagno_6", "bagno_1", 12), ("bagno_5", "bagno_2", 12)]),
 "ingresso": dict(m_alto=(8, 44), m_basso=(4, 30, 18), pav=(4,),
     pav_mobili=[("ingresso_1", 72, 5), ("ingresso_2", 84, 3), "R", ("ingresso_3", 84, 2), ("ingresso_4", 84, 1)],
     appesi=[("ingresso_6", "ingresso_3", 30)], davanti=[("ingresso_5", "ingresso_1", 80)]),
 "corridoio": dict(m_alto=(3, 48), m_basso=(7, 36, 22), pav=(2,),
     pav_mobili=[("corridoio_1", 84, 3), "R", ("corridoio_2", 86, 5), ("corridoio_3", 85, 2)],
     appesi=[("corridoio_6", "corridoio_2", 6), ("corridoio_5", "corridoio_1", 22)]),
 "ripostiglio": dict(m_alto=(4, 40), pav=(3,),
     pav_mobili=[("ripostiglio_1", 82, 5), (("ripostiglio_2", "ripostiglio_3"), 84, 4), "R", ("ripostiglio_4", 84, 2), ("ripostiglio_5", 84, 1), (("ripostiglio_6", "ripostiglio_7"), 84, 3)],
     appesi=[("ripostiglio_8", "ripostiglio_4", 20)]),
 "studio": dict(m_alto=(1, 40), m_basso=(5, 34, 24), pav=(7,),
     pav_mobili=[("studio_3", 82, 4), (("studio_1", "studio_2"), 84, 5), "R", ("studio_4", 84, 2), ("studio_5", 85, 3)],
     appesi=[("studio_6", ("studio_1", "studio_2"), 12)]),
 "lavanderia": dict(m_alto=(2, 56), m_basso=(6, 30, 20), pav=(5,),
     pav_mobili=[(("lavanderia_1", "lavanderia_2"), 85, 5), ("lavanderia_5", 84, 4), "R", ("lavanderia_3", 84, 3), ("lavanderia_4", 85, 2), ("lavanderia_6", 84, 1)],
     appesi=[("lavanderia_7", "lavanderia_4", 26)]),
 "cantina": dict(m_alto=(4, 40), pav=(8,), pav_g=dict(sat=.5, mult=(.78, .7, .86), luce=.75),
     pav_mobili=[("cantina_1", 85, 5), ("cantina_2", 82, 4), "R", ("cantina_3", 84, 3), ("cantina_4", 85, 2), ("cantina_5", 85, 1)],
     appesi=[("cantina_6", "cantina_3", 20)]),
 "balcone": dict(m_alto=(9, 60), pav=(4,), bordo="balaustra",
     pav_mobili=[("balcone_1", 84, 3), (("balcone_3", "balcone_4", "balcone_5"), 86, 5), "R", ("balcone_6", 85, 2), ("balcone_7", 84, 4), ("balcone_2", 84, 1)],
     appesi=[("balcone_8", ("balcone_3", "balcone_4", "balcone_5"), 39)]),
 "giardino": dict(m_alto=(9, 60), pav=(9,), pav_g=dict(sat=.6, mult=(.72, .82, .78), luce=.7), bordo="siepe",
     pav_mobili=[("giardino_4", 82, 4), ("giardino_2", 86, 3), "R", ("giardino_1", 86, 5), ("giardino_3", 85, 2), ("giardino_6", 84, 1)],
     davanti=[("giardino_5", "giardino_2", 94)]),
}

# Palazzo d'Argentaluna: marmo chiaro, blu e oro. I fogli di cucina e bagno non ci sono ancora.
STANZE_REGGIA = {
 "soggiorno": dict(m_alto=(2, 44), fascia=("f", 3, 8, 30), batt=("f", 2, 6), pav=(1,),
     pav_mobili=[("soggiorno_4", 83, 2), ("soggiorno_3", 81, 5), "R", ("soggiorno_1", 86, 4), ("soggiorno_2", 86, 1)],
     appesi=[("soggiorno_6", "soggiorno_1", 8)], tappeti=[("camera_5", "soggiorno_1", 93)], davanti=[("soggiorno_5", "soggiorno_1", 92)]),
 "camera": dict(m_alto=(8, 60), fascia=("f", 4, 12, 28), batt=("f", 2, 6), pav=(7,),
     pav_mobili=[("camera_2", 82, 3), ("camera_3", 84, 2), ("camera_1", 87, 5), "R", ("camera_4", 83, 1)],
     appesi=[("camera_6", "camera_1", 8)], tappeti=[("camera_5", "camera_1", 93)]),
 "cucina": dict(m_alto=(2, 56), m_basso=("f", 1, 18), batt=("f", 2, 6), pav=(5,),
     pav_mobili=[("cucina_1", 82, 5), ("cucina_2", 82, 4), "R", ("cucina_3", 81, 2), (("cucina_4", "cucina_5", "cucina_7"), 88, 3)],
     appesi=[("cucina_8", "cucina_1", 16), ("cucina_6", "cucina_2", 24)]),
 "bagno": dict(m_alto=(2, 56), m_basso=(6, 30, 22), batt=("f", 2, 6), pav=(6,),
     pav_mobili=[("bagno_1", 88, 5), ("bagno_2", 84, 4), "R", ("bagno_3", 84, 4.2)],
     appesi=[("bagno_5", "bagno_2", 12), ("bagno_6", "bagno_1", 12), ("bagno_4", "bagno_3", 20)]),
 "ingresso": dict(m_alto=(8, 44), m_basso=("f", 1, 18), batt=("f", 2, 6), pav=(6,),
     pav_mobili=[("ingresso_1", 72, 5), ("ingresso_2", 84, 3), "R", ("ingresso_3", 84, 2), ("ingresso_4", 84, 1)],
     appesi=[("ingresso_6", "ingresso_3", 30)], davanti=[("ingresso_5", "ingresso_1", 80)]),
 "corridoio": dict(m_alto=(5, 48), batt=("f", 2, 6), pav=(2,),
     pav_mobili=[("corridoio_1", 84, 3), "R", ("corridoio_2", 86, 5), ("corridoio_3", 85, 2)],
     appesi=[("corridoio_6", "corridoio_2", 4), ("corridoio_5", "corridoio_1", 22)]),
 "ripostiglio": dict(m_alto=(1, 40), batt=("f", 2, 6), pav=(3,),
     pav_mobili=[("ripostiglio_1", 82, 5), (("ripostiglio_2", "ripostiglio_3"), 84, 4), "R", ("ripostiglio_4", 84, 2), ("ripostiglio_5", 84, 1), ("ripostiglio_6", 84, 3)],
     appesi=[("ripostiglio_7", "ripostiglio_4", 20)]),
 "studio": dict(m_alto=(5, 48), batt=("f", 2, 6), pav=(2,),
     pav_mobili=[("studio_3", 82, 4), (("studio_1", "studio_2"), 84, 5), "R", ("studio_4", 84, 2), ("studio_5", 85, 3)],
     appesi=[("studio_6", ("studio_1", "studio_2"), 12)]),
 "lavanderia": dict(m_alto=(2, 56), m_basso=(6, 30, 22), batt=("f", 2, 6), pav=(5,),
     pav_mobili=[("lavanderia_1", 85, 5), ("lavanderia_4", 84, 4), "R", ("lavanderia_2", 84, 3), ("lavanderia_3", 85, 2), ("lavanderia_5", 84, 1)],
     appesi=[("lavanderia_6", "lavanderia_1", 24)]),
 "cantina": dict(m_alto=(4, 40), batt=("f", 2, 6), pav=(8,),
     pav_mobili=[("cantina_1", 85, 5), ("cantina_2", 82, 4), "R", ("cantina_3", 84, 3), ("cantina_4", 85, 2), ("cantina_5", 85, 1)],
     appesi=[("cantina_6", "cantina_3", 20)]),
 "balcone": dict(m_alto=(9, 60), pav=(4,), bordo=("f", 5, 20),
     pav_mobili=[("balcone_1", 84, 3), (("balcone_3", "balcone_4", "balcone_5"), 86, 5), "R", ("balcone_6", 85, 2), ("balcone_7", 84, 4), ("balcone_2", 84, 1)],
     appesi=[("balcone_8", ("balcone_3", "balcone_4", "balcone_5"), 39)]),
 "giardino": dict(m_alto=(9, 60), pav=(9,), bordo=("f", 6, 18),
     pav_mobili=[("giardino_4", 82, 4), ("giardino_2", 86, 3), "R", ("giardino_1", 86, 5), ("giardino_3", 85, 2), ("giardino_6", 84, 1)],
     davanti=[("giardino_5", "giardino_2", 94)]),
}

# Riempimenti: decorazioni che si aggiungono da sole negli spazi vuoti, per non lasciare le stanze spoglie.
# pavimento: pezzi a terra · tappeti: steso a terra · parete: (pezzo, riga della cima) · luci: pezzi che fanno alone caldo.
RIEMPI_CASTELLO = dict(
 pav={"soggiorno": ["balcone_1", "dec_b_1", "camera_3", "dec_b_6"], "camera": ["balcone_1", "dec_b_6", "corridoio_3", "dec_b_2"],
      "cucina": ["ripostiglio_5", "dec_b_3", "ripostiglio_4", "balcone_1"], "bagno": ["balcone_1", "dec_b_6", "ripostiglio_5"],
      "ingresso": ["dec_b_1", "corridoio_3", "dec_b_2", "ripostiglio_5"], "corridoio": ["dec_b_2", "balcone_1", "dec_b_1", "ripostiglio_5"],
      "ripostiglio": ["cantina_2", "dec_b_3", "ripostiglio_5", "ripostiglio_4"], "studio": ["dec_b_1", "corridoio_3", "soggiorno_5", "dec_b_2"],
      "lavanderia": ["ripostiglio_5", "dec_b_3", "balcone_1", "dec_b_6"], "cantina": ["ripostiglio_4", "dec_b_4", "ripostiglio_5", "cantina_2"],
      "balcone": ["balcone_1", "giardino_6", "dec_b_4"], "giardino": ["giardino_6", "balcone_1", "giardino_1"]},
 tap={"soggiorno": "dec_b_5", "camera": "dec_b_5", "ingresso": "ingresso_5", "corridoio": "corridoio_4", "studio": "dec_b_5", "bagno": "ingresso_5", "cucina": "ingresso_5"},
 parete={
  "soggiorno": [("soggiorno_6", 12), ("dec_a_2", 14), ("ingresso_6", 26), ("dec_a_1", 12), ("corridoio_6", 6), ("dec_a_6", 26), ("studio_6", 10), ("dec_a_4", 0)],
  "camera": [("camera_6", 10), ("dec_a_2", 14), ("ingresso_6", 26), ("dec_a_3", 6), ("studio_6", 10), ("dec_a_4", 0), ("corridoio_5", 28)],
  "cucina": [("cucina_6", 26), ("ingresso_6", 24), ("bagno_6", 14), ("dec_a_6", 24), ("ripostiglio_8", 20), ("dec_a_4", 0)],
  "bagno": [("bagno_6", 12), ("bagno_5", 10), ("ingresso_6", 24), ("dec_a_3", 6), ("dec_a_4", 0)],
  "ingresso": [("dec_a_1", 10), ("corridoio_6", 6), ("ingresso_6", 26), ("dec_a_2", 14), ("studio_6", 10), ("dec_a_4", 0), ("soggiorno_6", 12)],
  "corridoio": [("dec_a_1", 12), ("ingresso_6", 24), ("corridoio_6", 6), ("dec_a_2", 14), ("dec_a_3", 6), ("studio_6", 10), ("dec_a_4", 0)],
  "ripostiglio": [("ripostiglio_8", 20), ("ingresso_6", 24), ("dec_a_6", 26), ("lavanderia_7", 26), ("cantina_6", 18), ("dec_a_4", 0)],
  "studio": [("studio_6", 10), ("dec_a_2", 12), ("soggiorno_6", 12), ("dec_a_1", 12), ("dec_a_6", 26), ("ingresso_6", 26), ("dec_a_4", 0)],
  "lavanderia": [("lavanderia_7", 26), ("ingresso_6", 24), ("bagno_6", 12), ("ripostiglio_8", 20), ("dec_a_4", 0)],
  "cantina": [("cantina_6", 18), ("ingresso_6", 24), ("dec_a_1", 12), ("ripostiglio_8", 20), ("dec_a_4", 0), ("dec_a_6", 26)]},
 luci={"soggiorno_3", "cucina_1", "lavanderia_4", "ingresso_6", "corridoio_5", "camera_3", "soggiorno_5", "cantina_6", "studio_5", "dec_b_2", "dec_b_4", "dec_a_4", "dec_a_6"},
)
RIEMPI_REGGIA = dict(
 pav={"soggiorno": ["balcone_1", "corridoio_3"], "camera": ["balcone_1", "corridoio_3"], "ingresso": ["corridoio_3", "balcone_1"],
      "cucina": ["balcone_1", "corridoio_3"], "bagno": ["balcone_1", "corridoio_3"],
      "corridoio": ["balcone_1", "corridoio_3"], "ripostiglio": ["ripostiglio_5", "ripostiglio_4"], "studio": ["corridoio_3", "balcone_1"],
      "lavanderia": ["ripostiglio_5", "balcone_1"], "cantina": ["ripostiglio_5", "ripostiglio_4"], "balcone": ["balcone_1", "giardino_6"],
      "giardino": ["giardino_6", "balcone_1"]},
 tap={"soggiorno": "camera_5", "camera": "camera_5", "ingresso": "ingresso_5", "studio": "camera_5"},
 parete={
  "soggiorno": [("soggiorno_6", 8), ("ingresso_6", 26), ("corridoio_6", 4), ("studio_6", 8), ("corridoio_5", 28)],
  "cucina": [("cucina_6", 24), ("ingresso_6", 24), ("corridoio_6", 4), ("corridoio_5", 28)],
  "bagno": [("bagno_6", 12), ("bagno_5", 12), ("ingresso_6", 24), ("corridoio_6", 4)],
  "camera": [("camera_6", 8), ("ingresso_6", 26), ("studio_6", 8), ("corridoio_5", 28), ("corridoio_6", 4)],
  "ingresso": [("corridoio_6", 4), ("ingresso_6", 26), ("studio_6", 8), ("corridoio_5", 28), ("soggiorno_6", 8)],
  "corridoio": [("ingresso_6", 24), ("corridoio_6", 4), ("corridoio_5", 26), ("studio_6", 8)],
  "ripostiglio": [("ripostiglio_7", 20), ("ingresso_6", 24), ("lavanderia_6", 26), ("cantina_6", 18)],
  "studio": [("studio_6", 8), ("soggiorno_6", 8), ("corridoio_5", 28), ("ingresso_6", 26), ("corridoio_6", 4)],
  "lavanderia": [("lavanderia_6", 26), ("ingresso_6", 24), ("ripostiglio_7", 20), ("corridoio_5", 28)],
  "cantina": [("cantina_6", 18), ("ingresso_6", 24), ("ripostiglio_7", 20), ("corridoio_6", 4)]},
 luci={"soggiorno_3", "lavanderia_4", "ingresso_6", "corridoio_5", "camera_3", "cantina_6", "studio_1", "balcone_7", "giardino_6"},
)
# Stanze in più (tessere della dimora): il terrazzo è un balcone più largo; la zona giorno unisce cucina e soggiorno.
STANZE_CASTELLO["terrazzo"] = STANZE_CASTELLO["balcone"]
RIEMPI_CASTELLO["pav"]["terrazzo"] = RIEMPI_CASTELLO["pav"]["balcone"]
STANZE_CASTELLO["cucina_soggiorno"] = dict(m_alto=(1, 40), m_basso=(7, 36, 22), pav=(2,),
     pav_mobili=[("cucina_1", 82, 5), ("cucina_2", 82, 4), ("cucina_3", 81, 2), "R", ("soggiorno_3", 81, 5), ("soggiorno_1", 86, 4), ("soggiorno_2", 86, 1), ("cucina_4", 88, 3)],
     appesi=[("cucina_7", "cucina_2", 16), ("cucina_6", "cucina_1", 24), ("soggiorno_6", "soggiorno_1", 18)], tappeti=[("camera_5", "soggiorno_1", 93)], davanti=[("soggiorno_5", "soggiorno_1", 92)])
RIEMPI_CASTELLO["pav"]["cucina_soggiorno"] = ["dec_b_1", "camera_3", "dec_b_6", "balcone_1"]
RIEMPI_CASTELLO["parete"]["cucina_soggiorno"] = [("dec_a_2", 14), ("ingresso_6", 26), ("dec_a_1", 12), ("corridoio_6", 6), ("dec_a_6", 26), ("studio_6", 10), ("dec_a_4", 0)]
STANZE_REGGIA["terrazzo"] = STANZE_REGGIA["balcone"]
RIEMPI_REGGIA["pav"]["terrazzo"] = RIEMPI_REGGIA["pav"]["balcone"]
STANZE_REGGIA["cucina_soggiorno"] = dict(m_alto=(2, 44), fascia=("f", 3, 8, 30), batt=("f", 2, 6), pav=(1,),
     pav_mobili=[("cucina_1", 82, 5), ("cucina_2", 82, 4), ("cucina_3", 81, 2), "R", ("soggiorno_3", 81, 5), ("soggiorno_1", 86, 4), ("soggiorno_2", 86, 1), (("cucina_4", "cucina_5", "cucina_7"), 88, 3)],
     appesi=[("cucina_8", "cucina_1", 16), ("cucina_6", "cucina_2", 24), ("soggiorno_6", "soggiorno_1", 8)], tappeti=[("camera_5", "soggiorno_1", 93)], davanti=[("soggiorno_5", "soggiorno_1", 92)])
RIEMPI_REGGIA["pav"]["cucina_soggiorno"] = ["balcone_1", "corridoio_3"]
RIEMPI_REGGIA["parete"]["cucina_soggiorno"] = [("ingresso_6", 26), ("corridoio_6", 4), ("studio_6", 8), ("corridoio_5", 28)]
RIEMPI_REGGIA["tap"]["cucina_soggiorno"] = "camera_5"

DIMORE = {
 "castello": dict(stanze=STANZE_CASTELLO, rie=RIEMPI_CASTELLO, gradare=True, luce_min=0.68),
 "reggia": dict(stanze=STANZE_REGGIA, rie=RIEMPI_REGGIA, gradare=False, luce_min=0.85),
}


def usa(dimora):
    """Sceglie la dimora su cui lavorare (cartella con pezzi/, materiali/, fregi/)."""
    global BASE, CFG
    BASE = os.path.join(DIR, dimora); CFG = DIMORE[dimora]
    return CFG["stanze"]


usa("castello")


def disponi(W, voci, bordo=3, minimo=1):
    """Sceglie cosa entra e lo distribuisce con spazi uguali. Con POSTI il posto reliquia non viene mai tolto, e nelle
    stanze larghe se ne aggiunge un secondo. Restituisce [(chiave, centro x, base, larghezza)]."""
    def largh(v): return RELIQUIA[0] if v[0] == "R" else pezzo(v[0]).width
    if not POSTI: voci = [v for v in voci if v != "R"]
    voci = [("R", 88, 9) if v == "R" else v for v in voci]
    if POSTI and W >= 160:                         # stanza larga: secondo posto per una reliquia
        voci.insert(len(voci) - 1, ("R", 88, 1.5))
    while voci:
        larg = sum(largh(v) for v in voci)
        if larg + minimo * (len(voci) - 1) <= W - 2 * bordo: break
        voci.remove(min(voci, key=lambda v: v[2]))
    larg = sum(largh(v) for v in voci)
    gap = (W - 2 * bordo - larg) / max(1, len(voci) - 1) if len(voci) > 1 else 0
    x = bordo if len(voci) > 1 else (W - larg) / 2
    out = []
    for v in voci:
        w = largh(v); out.append((v[0], x + w / 2, v[1], w)); x += w + gap
    return out


def luce(img, cx, cy, r=26, a=46, col=(255, 168, 70)):
    """Alone caldo (si somma) attorno a fuochi e candele; misure in pixel del disegno."""
    y, x = np.mgrid[0:img.height, 0:img.width]
    k = np.clip(1 - np.hypot(x - S(cx), (y - S(cy)) * 1.25) / S(r), 0, 1) ** 2 * a
    arr = np.array(img).astype(float)
    for c in range(3): arr[..., c] += k * col[c] / 255
    img.paste(Image.fromarray(arr.clip(0, 255).astype(np.uint8), "RGBA"))


def buchi(occupati, W, bordo=4, pad=2):
    """Intervalli liberi tra gli ingombri [(x0, x1)]."""
    occ = sorted((max(bordo, a - pad), min(W - bordo, b + pad)) for a, b in occupati); out, x = [], bordo
    for a, b in occ:
        if a > x: out.append((x, a))
        x = max(x, b)
    if W - bordo > x: out.append((x, W - bordo))
    return out


def stanza(nome, W):
    """(immagine, posti). posti = {"t": [(cx, base)], "p": [(cx, cima)]} in pixel del disegno."""
    r = CFG["stanze"][nome]; rie = CFG["rie"]; LUCI = rie["luci"]
    img = sfondo(W, r)
    lay = disponi(W, r["pav_mobili"]); pos = {k: (cx, b) for k, cx, b, _ in lay if k != "R"}
    posti = {"t": [(round(cx), b) for k, cx, b, _ in lay if k == "R"], "p": [(round(cx), CIMA_DIPINTO) for k, cx, b, _ in lay if k == "R"]}
    piani = [(cx - w / 2, cx + w / 2) for k, cx, b, w in lay]
    appesi = [(p, pos[sopra][0], cima) for p, sopra, cima in r.get("appesi", []) if sopra in pos]
    # profilo dei mobili: altezza della cima di ciò che sta a terra, colonna per colonna (il muro libero sta sopra)
    cima_mobili = np.full(W, MURO - BATT - 1.0)
    for k, cx, b, w in lay:
        if k == "R": continue
        sl = slice(max(0, int(cx - w / 2)), min(W, int(cx + w / 2) + 1))
        cima_mobili[sl] = np.minimum(cima_mobili[sl], b - pezzo(k).height)
    blocca = np.zeros(W, bool)                  # colonne con un pezzo appeso o un posto dipinto
    def segna(cx, w, pad=2): blocca[max(0, int(cx - w / 2 - pad)):min(W, int(cx + w / 2 + pad) + 1)] = True
    for k, cx, b, w in lay:
        if k == "R": segna(cx, DIPINTO[0], 3)
    for p, cx, cima in appesi: segna(cx, pezzo(p).width, 3)
    # 1. tappeti stesi a terra: sotto al centro (e a un quarto se la stanza è larga)
    tap = rie["tap"].get(nome)
    if tap and not r.get("bordo"):
        for fx in ((.5,) if W < 150 else (.28, .72)): tappeto(img, pezzo(tap), fx * W, 93)
    # 2. mobiletti, piante, botti nei buchi del pavimento
    def riempi_pav(pool):
        out, i = [], 0
        for a_, b_ in buchi(piani, W):
            scelti, usato = [], 0
            for _ in range(len(pool) * 3):
                n_, bs = pool[i % len(pool)]; i += 1; w_ = pezzo(n_).width
                if usato + w_ + 6 <= b_ - a_ and (not scelti or scelti[-1][0] != n_): scelti.append((n_, bs, w_)); usato += w_ + 2
            if not scelti: continue
            avanzo = (b_ - a_ - usato) / (len(scelti) + 1); x = a_ + avanzo
            for n_, bs, w_ in scelti: out.append((n_, x + w_ / 2, bs)); x += w_ + 2 + avanzo
        return out
    extra = riempi_pav([(p, 84 + k % 3 * 2) for k, p in enumerate(rie["pav"][nome] * 2)])
    for p, cx, b in extra:
        piani.append((cx - pezzo(p).width / 2, cx + pezzo(p).width / 2))
        top = b - pezzo(p).height; sl = slice(max(0, int(cx - pezzo(p).width / 2)), min(W, int(cx + pezzo(p).width / 2) + 1))
        cima_mobili[sl] = np.minimum(cima_mobili[sl], top)
    # 3. candele, finestre, arazzi sul muro libero: ognuno va nel punto più largo dove ci sta in altezza
    deco, usati = [], {}
    if nome in rie["parete"]:
        pool = rie["parete"][nome]
        for n in range(14):
            n_, cima = pool[n % len(pool)]; q = pezzo(n_); best = None
            if usati.get(n_, 0) >= 1 + (W >= 150): continue          # al massimo uno (due nelle stanze larghe) per tipo
            libero = (~blocca) & (cima_mobili >= cima + q.height + 3)
            x = 0
            while x < W:
                if not libero[x]: x += 1; continue
                y = x
                while y < W and libero[y]: y += 1
                if y - x >= q.width + 2 and (best is None or y - x > best[1] - best[0]): best = (x, y)
                x = y
            if not best: continue
            cx = (best[0] + best[1]) / 2; deco.append((n_, cx, cima)); usati[n_] = usati.get(n_, 0) + 1; segna(cx, q.width, 3)
    # luci prima dei mobili, così l'alone sta dietro
    for k, cx, b, _ in lay:
        if k in LUCI: luce(img, cx, b - pezzo(k).height * 0.55)
    for k, cx, cima in appesi + deco:
        if k in LUCI: luce(img, cx, cima + pezzo(k).height * 0.35, r=20, a=40)
    for k, cx, b in extra:
        if k in LUCI: luce(img, cx, b - pezzo(k).height * 0.7, r=18, a=36)
    for p, sotto, base in r.get("tappeti", []):
        if sotto in pos: tappeto(img, pezzo(p), pos[sotto][0], base)
    for p, cx, cima in appesi + deco: appendi(img, pezzo(p), cx, cima)
    for p, cx, b in sorted(extra, key=lambda e: e[2]): appoggia(img, pezzo(p), cx, b)
    for k, cx, b, _ in lay:
        if k != "R": appoggia(img, pezzo(k), cx, b)
    for p, sopra, base in r.get("davanti", []):
        if sopra in pos: appoggia(img, pezzo(p), pos[sopra][0], base, ombra=False)
    return img, posti


def segna_posti(img, posti):
    """Solo per le prove con POSTI=1: riquadri tratteggiati dorati dove andranno reliquie e dipinti."""
    d = ImageDraw.Draw(img); oro = (214, 176, 92, 255)
    def tratteggio(x0, y0, x1, y1):
        for x in range(S(x0), S(x1) + 1, 2 * Q): d.rectangle((x, S(y0), x + Q - 1, S(y0) + Q - 1), fill=oro); d.rectangle((x, S(y1), x + Q - 1, S(y1) + Q - 1), fill=oro)
        for y in range(S(y0), S(y1) + 1, 2 * Q): d.rectangle((S(x0), y, S(x0) + Q - 1, y + Q - 1), fill=oro); d.rectangle((S(x1), y, S(x1) + Q - 1, y + Q - 1), fill=oro)
    for cx, b in posti["t"]: tratteggio(cx - RELIQUIA[0] // 2, b - RELIQUIA[1], cx + RELIQUIA[0] // 2, b)
    for cx, c in posti["p"]: tratteggio(cx - DIPINTO[0] // 2, c, cx + DIPINTO[0] // 2, c + DIPINTO[1])


if __name__ == "__main__":
    dim = sys.argv[1] if len(sys.argv) > 1 else "castello"
    ric = usa(dim)
    G, coppie = 6, []
    for nome in ric:
        ims = []
        for w in (110, 190):
            im, posti = stanza(nome, w)
            if POSTI: segna_posti(im, posti)
            ims.append(im.resize((w * 3, H * 3), Image.LANCZOS))
        coppie.append(ims)
    if len(coppie) % 2: coppie.append([Image.new("RGBA", (1, H * 3))])
    righe = [coppie[i] + coppie[i + 1] for i in range(0, len(coppie), 2)]
    Wt = max(sum(i.width for i in r) + G * (len(r) + 1) for r in righe); Ht = len(righe) * (H * 3 + G) + G
    tav = Image.new("RGBA", (Wt, Ht), (24, 18, 30, 255)); y = G
    for r in righe:
        x = G
        for im in r: tav.alpha_composite(im, (x, y)); x += im.width + G
        y += H * 3 + G
    tav.save(os.path.join(BASE, "prova.png"))
    print(dim, "ok", len(ric), "stanze")
