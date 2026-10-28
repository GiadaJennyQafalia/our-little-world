#!/usr/bin/env python3
"""Compone le stanze modulari della vista dimora: muro + zoccolatura/battiscopa + pavimento (dai campioni di
materiale) e i mobili ritagliati sopra. Ogni stanza lascia liberi dei POSTI per gli arredi comprati in Bottega:
un posto a terra per le reliquie e, sopra di esso, un posto a parete per dipinti e arazzi (due e due se la stanza
è larga). Tutto è disegnato in 'pixel del disegno' e poi ingrandito senza sfumare, come la pixel art.

Uso: python3 componi.py            -> prove/prova.png (ogni stanza stretta e larga, posti segnati in oro)
     from componi import stanza     -> stanza(nome, W) restituisce (immagine, posti)"""
import os, random
import numpy as np
from PIL import Image, ImageDraw

DIR = os.path.dirname(os.path.abspath(__file__))
H, MURO, BATT = 96, 68, 3          # altezza stanza, riga dove finisce il muro, spessore battiscopa (pixel del disegno)
SCALA = 3                           # ingrandimento delle prove
RELIQUIA = (18, 20)                 # posto a terra (larghezza, altezza) per una reliquia
DIPINTO = (18, 20)                  # posto a parete per un dipinto o un arazzo
CIMA_DIPINTO = 20                   # riga della cima dei dipinti


def carica(nome):
    return Image.open(os.path.join(DIR, nome)).convert("RGBA")


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
    t = carica(f"materiali/muri_{n}.png").resize((alto, alto), Image.BOX)
    return senza_giunture(t, True, True)


def pavimento(n, w=96, h=30, **g):
    t = carica(f"materiali/pavimenti_{n}.png").resize((w, h), Image.BOX)   # schiacciato in verticale: sembra a terra
    return grade(senza_giunture(t, True, False), **g)


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


def sfondo(W, m_alto, m_basso=None, fascia=None, pav=None, pav_g=None, batt=(52, 36, 34), bordo=None):
    img = Image.new("RGBA", (W, H))
    img.paste(ripeti(muro(*m_alto), W, MURO), (0, 0))
    d = ImageDraw.Draw(img)
    if m_basso:                                  # zoccolatura (boiserie, piastrelle) sulla parte bassa del muro
        n, h_t, alt = m_basso
        img.paste(ripeti(muro(n, h_t), W, alt), (0, MURO - alt))
        d.rectangle((0, MURO - alt - 2, W, MURO - alt - 1), fill=(70, 46, 40)); d.line((0, MURO - alt - 2, W, MURO - alt - 2), fill=(96, 66, 54))
    if fascia:                                   # fascia decorata a metà muro
        y, col = fascia
        d.rectangle((0, y, W, y + 3), fill=col); d.line((0, y, W, y), fill=tuple(min(255, c + 25) for c in col))
        for x in range(1, W, 6): d.point((x, y + 2), fill=tuple(max(0, c - 30) for c in col))
    img.paste(ripeti(pavimento(*pav, **(pav_g or {})), W, H - MURO), (0, MURO))
    if bordo == "balaustra": balaustra(img)
    elif bordo == "siepe": siepe(img)
    elif batt:
        d = ImageDraw.Draw(img)
        d.rectangle((0, MURO - BATT, W, MURO - 1), fill=batt); d.line((0, MURO - BATT, W, MURO - BATT), fill=tuple(c + 24 for c in batt))
    # luce: ombra dal soffitto (non all'aperto), ombra del muro sul pavimento, bordi della sezione
    a = np.array(img).astype(float); y = np.arange(H)[:, None]; ombra = np.ones((H, 1))
    if not bordo: ombra[:MURO] *= (0.68 + 0.32 * np.clip(y[:MURO] / (MURO * 0.55), 0, 1))
    ombra[MURO:] *= (0.62 + 0.38 * np.clip((y[MURO:] - MURO) / 6, 0, 1))
    x = np.arange(W)[None, :]; lati = 0.6 + 0.4 * np.clip(np.minimum(x, W - 1 - x) / 7, 0, 1)
    a[..., :3] *= (ombra * lati)[..., None]
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def pezzo(nome):
    if isinstance(nome, tuple):                  # gruppo: pezzi affiancati (sedia-tavolo-sedia, scopa e secchio…)
        ps = [carica(f"pezzi/{n}.png") for n in nome]
        g = Image.new("RGBA", (sum(p.width for p in ps) + len(ps) - 1, max(p.height for p in ps))); x = 0
        for p in ps: g.alpha_composite(p, (x, g.height - p.height)); x += p.width + 1
        return g
    return carica(f"pezzi/{nome}.png")


def appoggia(img, p, cx, base, ombra=True):
    x, y = int(cx - p.width / 2), int(base - p.height)
    if ombra:
        om = Image.new("RGBA", img.size); ImageDraw.Draw(om).ellipse((x + 2, base - 2, x + p.width - 2, base + 2), fill=(10, 6, 16, 110))
        img.alpha_composite(om)
    img.alpha_composite(p, (x, y))


def appendi(img, p, cx, cima):
    img.alpha_composite(p, (int(cx - p.width / 2), int(cima)))


def tappeto(img, p, cx, base, schiaccia=3):
    q = p.resize((p.width, max(3, p.height // schiaccia)), Image.NEAREST)
    img.alpha_composite(q, (int(cx - q.width / 2), int(base - q.height)))


# Ricette. pav_mobili: (pezzo o gruppo, riga dei piedi, priorità) da sinistra a destra; nelle stanze strette si
# tolgono prima i mobili con priorità più bassa. "R" è il posto libero per una reliquia (con un dipinto sopra).
# appesi: (pezzo, sopra quale mobile, riga della cima). tappeti / davanti: (pezzo, sotto/davanti a quale mobile, riga).
STANZE = {
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


def disponi(W, voci, bordo=5, minimo=3):
    """Sceglie cosa entra e lo distribuisce con spazi uguali. Il posto reliquia ha priorità massima: non viene mai tolto,
    e nelle stanze larghe se ne aggiunge un secondo. Restituisce [(chiave, centro x, base, larghezza)]."""
    def largh(v): return RELIQUIA[0] if v[0] == "R" else pezzo(v[0]).width
    voci = [("R", 88, 9) if v == "R" else v for v in voci]
    if W >= 160:                                   # stanza larga: secondo posto per una reliquia
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


def stanza(nome, W):
    """(immagine, posti). posti = {"t": [(cx, base)], "p": [(cx, cima)]} in pixel del disegno."""
    r = STANZE[nome]
    img = sfondo(W, r["m_alto"], r.get("m_basso"), r.get("fascia"), r["pav"], r.get("pav_g"), bordo=r.get("bordo"))
    lay = disponi(W, r["pav_mobili"]); pos = {k: (cx, b) for k, cx, b, _ in lay if k != "R"}
    posti = {"t": [(round(cx), b) for k, cx, b, _ in lay if k == "R"], "p": [(round(cx), CIMA_DIPINTO) for k, cx, b, _ in lay if k == "R"]}
    for p, sotto, base in r.get("tappeti", []):
        if sotto in pos: tappeto(img, pezzo(p), pos[sotto][0], base)
    for p, sopra, cima in r.get("appesi", []):
        if sopra in pos: appendi(img, pezzo(p), pos[sopra][0], cima)
    for k, cx, b, _ in lay:
        if k != "R": appoggia(img, pezzo(k), cx, b)
    for p, sopra, base in r.get("davanti", []):
        if sopra in pos: appoggia(img, pezzo(p), pos[sopra][0], base, ombra=False)
    return img, posti


def segna_posti(img, posti):
    """Solo per le prove: riquadri tratteggiati dorati dove andranno reliquie e dipinti."""
    d = ImageDraw.Draw(img); oro = (214, 176, 92, 255)
    def tratteggio(x0, y0, x1, y1):
        for x in range(x0, x1 + 1, 2): d.point((x, y0), fill=oro); d.point((x, y1), fill=oro)
        for y in range(y0, y1 + 1, 2): d.point((x0, y), fill=oro); d.point((x1, y), fill=oro)
    for cx, b in posti["t"]: tratteggio(cx - RELIQUIA[0] // 2, b - RELIQUIA[1], cx + RELIQUIA[0] // 2, b)
    for cx, c in posti["p"]: tratteggio(cx - DIPINTO[0] // 2, c, cx + DIPINTO[0] // 2, c + DIPINTO[1])


if __name__ == "__main__":
    os.makedirs(os.path.join(DIR, "prove"), exist_ok=True)
    G, coppie = 6, []
    for nome in STANZE:
        ims = []
        for w in (110, 190):
            im, posti = stanza(nome, w); segna_posti(im, posti); ims.append(im)
        coppie.append(ims)
    righe = [coppie[i] + coppie[i + 1] for i in range(0, len(coppie), 2)]
    Wt = max(sum(i.width for i in r) + G * (len(r) + 1) for r in righe); Ht = len(righe) * (H + G) + G
    tav = Image.new("RGBA", (Wt, Ht), (24, 18, 30, 255)); y = G
    for r in righe:
        x = G
        for im in r: tav.alpha_composite(im, (x, y)); x += im.width + G
        y += H + G
    tav.resize((Wt * SCALA, Ht * SCALA), Image.NEAREST).save(os.path.join(DIR, "prove", "prova.png"))
    print("ok")
