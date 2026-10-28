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


# Riempimenti: decorazioni che si aggiungono da sole negli spazi vuoti, per non lasciare le stanze spoglie.
# pavimento: (pezzo, riga dei piedi) · tappeti stesi a terra · parete: (pezzo, riga della cima).
RIEMPI_PAV = {
 "soggiorno": ["balcone_1", "camera_3", "corridoio_3"], "camera": ["balcone_1", "corridoio_3", "soggiorno_5"],
 "cucina": ["ripostiglio_5", "ripostiglio_4", "balcone_1"], "bagno": ["balcone_1", "ripostiglio_5"],
 "ingresso": ["corridoio_3", "ripostiglio_5", "balcone_1"], "corridoio": ["balcone_1", "ripostiglio_5", "corridoio_3"],
 "ripostiglio": ["cantina_2", "ripostiglio_5", "ripostiglio_4"], "studio": ["corridoio_3", "soggiorno_5", "balcone_1"],
 "lavanderia": ["ripostiglio_5", "balcone_1", "ripostiglio_4"], "cantina": ["ripostiglio_4", "ripostiglio_5", "cantina_2"],
 "balcone": ["balcone_1", "giardino_6"], "giardino": ["giardino_6", "balcone_1", "giardino_1"],
}
RIEMPI_TAPPETI = {"soggiorno": "camera_5", "camera": "camera_5", "ingresso": "ingresso_5", "corridoio": "corridoio_4", "studio": "camera_5", "bagno": "ingresso_5", "cucina": "ingresso_5"}
RIEMPI_PARETE = {  # solo le stanze al coperto; all'aperto c'è il cielo. (pezzo, riga della cima)
 "soggiorno": [("soggiorno_6", 12), ("ingresso_6", 26), ("corridoio_6", 6), ("studio_6", 10), ("corridoio_5", 28), ("bagno_5", 10)],
 "camera": [("camera_6", 10), ("ingresso_6", 26), ("studio_6", 10), ("bagno_5", 10), ("corridoio_5", 28), ("corridoio_6", 6)],
 "cucina": [("cucina_6", 26), ("ingresso_6", 24), ("bagno_6", 14), ("bagno_6", 12), ("ripostiglio_8", 20), ("corridoio_5", 28)],
 "bagno": [("bagno_6", 12), ("bagno_5", 10), ("ingresso_6", 24), ("corridoio_5", 28), ("soggiorno_6", 12)],
 "ingresso": [("corridoio_6", 6), ("ingresso_6", 26), ("studio_6", 10), ("corridoio_5", 28), ("soggiorno_6", 12)],
 "corridoio": [("ingresso_6", 24), ("corridoio_6", 6), ("corridoio_5", 26), ("studio_6", 10), ("bagno_5", 10)],
 "ripostiglio": [("ripostiglio_8", 20), ("ingresso_6", 24), ("lavanderia_7", 26), ("cantina_6", 18), ("bagno_6", 12)],
 "studio": [("studio_6", 10), ("soggiorno_6", 12), ("corridoio_5", 28), ("ingresso_6", 26), ("corridoio_6", 6)],
 "lavanderia": [("lavanderia_7", 26), ("ingresso_6", 24), ("bagno_6", 12), ("ripostiglio_8", 20), ("corridoio_5", 28)],
 "cantina": [("cantina_6", 18), ("ingresso_6", 24), ("ripostiglio_8", 20), ("bagno_6", 12), ("corridoio_6", 6)],
}
LUCI = {"soggiorno_3", "cucina_1", "lavanderia_4", "ingresso_6", "corridoio_5", "camera_3", "soggiorno_5", "cantina_6", "studio_5"}


def luce(img, cx, cy, r=26, a=46, col=(255, 168, 70)):
    """Alone caldo (si somma) attorno a fuochi e candele."""
    y, x = np.mgrid[0:img.height, 0:img.width]
    k = np.clip(1 - np.hypot(x - cx, (y - cy) * 1.25) / r, 0, 1) ** 2 * a
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
    r = STANZE[nome]
    img = sfondo(W, r["m_alto"], r.get("m_basso"), r.get("fascia"), r["pav"], r.get("pav_g"), bordo=r.get("bordo"))
    lay = disponi(W, r["pav_mobili"]); pos = {k: (cx, b) for k, cx, b, _ in lay if k != "R"}
    posti = {"t": [(round(cx), b) for k, cx, b, _ in lay if k == "R"], "p": [(round(cx), CIMA_DIPINTO) for k, cx, b, _ in lay if k == "R"]}
    piani, parete, ombre = [], [], []          # ingombri a terra, sul muro
    for k, cx, b, w in lay:
        piani.append((cx - w / 2, cx + w / 2))
        if k == "R": parete.append((cx - DIPINTO[0] / 2, cx + DIPINTO[0] / 2)); continue
        p = pezzo(k)
        if b - p.height < 56: parete.append((cx - p.width / 2, cx + p.width / 2))
    appesi = []
    for p, sopra, cima in r.get("appesi", []):
        if sopra in pos: appesi.append((p, pos[sopra][0], cima))
    # profilo dei mobili: altezza della cima di ciò che sta a terra, colonna per colonna (il muro libero sta sopra)
    cima_mobili = np.full(W, MURO - BATT - 1.0)
    for k, cx, b, w in lay:
        if k == "R": continue
        top = b - pezzo(k).height
        cima_mobili[max(0, int(cx - w / 2)):min(W, int(cx + w / 2) + 1)] = np.minimum(cima_mobili[max(0, int(cx - w / 2)):min(W, int(cx + w / 2) + 1)], top)
    blocca = np.zeros(W, bool)                  # colonne con un pezzo appeso o un posto dipinto
    def segna(cx, w, pad=2): blocca[max(0, int(cx - w / 2 - pad)):min(W, int(cx + w / 2 + pad) + 1)] = True
    for k, cx, b, w in lay:
        if k == "R": segna(cx, DIPINTO[0], 3)
    for p, cx, cima in appesi: segna(cx, pezzo(p).width, 3)
    # 1. tappeti stesi a terra: sotto al centro (e a un quarto se la stanza è larga)
    tap = RIEMPI_TAPPETI.get(nome)
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
    extra = riempi_pav([(p, 84 + k % 3 * 2) for k, p in enumerate(RIEMPI_PAV[nome] * 2)])
    for p, cx, b in extra: piani.append((cx - pezzo(p).width / 2, cx + pezzo(p).width / 2))
    # 3. candele, finestre, arazzi sul muro libero: ognuno va nel punto più largo dove ci sta in altezza
    deco = []
    if nome in RIEMPI_PARETE:
        pool = RIEMPI_PARETE[nome]
        usati = {}
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
    for k, cx, cima in [(p, cx, cm) for p, cx, cm in appesi] + deco:
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
