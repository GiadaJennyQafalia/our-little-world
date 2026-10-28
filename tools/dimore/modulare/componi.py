#!/usr/bin/env python3
"""Compone una stanza modulare della vista dimora: muro + battiscopa + pavimento (dai campioni) e mobili sopra.
Tutto è disegnato in 'pixel del disegno' e poi ingrandito senza sfumare, come la pixel art.
Uso: python3 componi.py  ->  prove/<stanza>_<larghezza>.png e prove/prova.png (tutte insieme)."""
import os
import numpy as np
from PIL import Image, ImageDraw

DIR = os.path.dirname(os.path.abspath(__file__))
H, MURO, BATT = 96, 68, 3          # altezza stanza, riga dove finisce il muro, spessore battiscopa (pixel del disegno)
SCALA = 3                           # ingrandimento finale


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
    rgb = rgb * np.array(mult) * luce
    a[..., :3] = rgb
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def ripeti(t, w, h, dx=0):
    out = Image.new("RGBA", (w, h))
    for y in range(0, h, t.height):
        for x in range(-dx, w, t.width):
            out.paste(t, (x, y))
    return out


def muro(n, alto):
    """Campione di muro n (1-9) ridotto ai pixel del disegno."""
    t = carica(f"materiali/muri_{n}.png")
    t = t.resize((alto, alto), Image.BOX)
    return senza_giunture(t, True, True)


def pavimento(n, w=96, h=30, **g):
    t = carica(f"materiali/pavimenti_{n}.png")
    t = t.resize((w, h), Image.BOX)       # schiacciato in verticale: sembra a terra
    return grade(senza_giunture(t, True, False), **g)


def sfondo(W, m_alto, m_basso=None, fascia=None, pav=None, pav_g=None, batt=(52, 36, 34)):
    img = Image.new("RGBA", (W, H))
    img.paste(ripeti(muro(*m_alto), W, MURO), (0, 0))
    if m_basso:                                  # zoccolatura (boiserie, piastrelle) sulla parte bassa del muro
        n, h_t, alt = m_basso
        img.paste(ripeti(muro(n, h_t), W, alt), (0, MURO - alt))
        d = ImageDraw.Draw(img); d.rectangle((0, MURO - alt - 2, W, MURO - alt - 1), fill=(70, 46, 40)); d.line((0, MURO - alt - 2, W, MURO - alt - 2), fill=(96, 66, 54))
    if fascia:                                   # fascia decorata a metà muro
        y, col = fascia; d = ImageDraw.Draw(img)
        d.rectangle((0, y, W, y + 3), fill=col); d.line((0, y, W, y), fill=tuple(min(255, c + 25) for c in col))
        for x in range(1, W, 6): d.point((x, y + 2), fill=tuple(max(0, c - 30) for c in col))
    p = pavimento(*pav, **(pav_g or {}))
    img.paste(ripeti(p, W, H - MURO), (0, MURO))
    d = ImageDraw.Draw(img)
    d.rectangle((0, MURO - BATT, W, MURO - 1), fill=batt); d.line((0, MURO - BATT, W, MURO - BATT), fill=tuple(c + 24 for c in batt))
    # luce: ombra dal soffitto, ombra del muro sul pavimento, bordi della sezione
    a = np.array(img).astype(float)
    y = np.arange(H)[:, None]
    ombra = np.ones((H, 1))
    ombra[:MURO] *= (0.68 + 0.32 * np.clip(y[:MURO] / (MURO * 0.55), 0, 1))
    ombra[MURO:] *= (0.62 + 0.38 * np.clip((y[MURO:] - MURO) / 6, 0, 1))
    x = np.arange(W)[None, :]
    lati = 0.6 + 0.4 * np.clip(np.minimum(x, W - 1 - x) / 7, 0, 1)
    a[..., :3] *= (ombra * lati)[..., None]
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA")


def pezzo(nome):
    return carica(f"pezzi/{nome}.png")


def appoggia(img, p, cx, base):
    """Mobile da pavimento: centrato su cx, con i piedi sulla riga base, e un'ombra sotto."""
    x, y = int(cx - p.width / 2), int(base - p.height)
    om = Image.new("RGBA", img.size); d = ImageDraw.Draw(om)
    d.ellipse((x + 2, base - 2, x + p.width - 2, base + 2), fill=(10, 6, 16, 110))
    img.alpha_composite(om); img.alpha_composite(p, (x, y))


def appendi(img, p, cx, cima):
    img.alpha_composite(p, (int(cx - p.width / 2), int(cima)))


def tappeto(img, p, cx, base):
    q = p.resize((p.width, max(3, p.height // 3)), Image.NEAREST)
    img.alpha_composite(q, (int(cx - q.width / 2), int(base - q.height)))


# Ricette: muro (campione, altezza), zoccolatura (campione, altezza, quanto sale), pavimento (campione) e mobili.
# pavimento: (pezzo, riga dei piedi, priorità) da sinistra a destra; se la stanza è stretta si tolgono prima quelli
# con priorità più bassa. appesi: (pezzo, sopra quale mobile, riga della cima). tappeti: (pezzo, sotto quale mobile).
STANZE = {
 "soggiorno": dict(m_alto=(1, 40), m_basso=(7, 36, 22), pav=(2,),
     pav_mobili=[("soggiorno_4", 83, 2), ("soggiorno_3", 81, 5), ("soggiorno_1", 86, 4), ("soggiorno_2", 86, 1)],
     appesi=[("soggiorno_6", "soggiorno_1", 18)], tappeti=[("camera_5", "soggiorno_1", 93)], davanti=[("soggiorno_5", "soggiorno_1", 92)]),
 "camera": dict(m_alto=(2, 56), fascia=(30, (78, 62, 84)), pav=(7,),
     pav_mobili=[("camera_2", 82, 3), ("camera_3", 84, 2), ("camera_1", 87, 5), ("camera_4", 83, 1)],
     appesi=[("camera_6", "camera_1", 10)], tappeti=[("camera_5", "camera_1", 93)]),
 "cucina": dict(m_alto=(8, 44), pav=(5,),
     pav_mobili=[("cucina_1", 82, 5), ("cucina_2", 82, 4), ("cucina_3", 81, 2), ("cucina_4", 88, 3)],
     appesi=[("cucina_7", "cucina_2", 16), ("cucina_6", "cucina_1", 24)]),
 "bagno": dict(m_alto=(2, 56), m_basso=(6, 30, 28), pav=(6,), pav_g=dict(sat=.3, mult=(.58, .53, .68), luce=.72),
     pav_mobili=[("bagno_1", 88, 5), ("bagno_2", 84, 4), ("bagno_4", 76, 1), ("bagno_3", 84, 3)],
     appesi=[("bagno_6", "bagno_1", 12), ("bagno_5", "bagno_2", 12)]),
}


def disponi(W, voci, bordo=5, minimo=3):
    """Sceglie quali mobili entrano e li distribuisce con spazi uguali. Restituisce {pezzo: centro x}."""
    voci = list(voci)
    while voci:
        larg = sum(pezzo(p).width for p, *_ in voci)
        if larg + minimo * (len(voci) - 1) <= W - 2 * bordo: break
        voci.remove(min(voci, key=lambda v: v[2]))
    larg = sum(pezzo(p).width for p, *_ in voci)
    gap = (W - 2 * bordo - larg) / max(1, len(voci) - 1) if len(voci) > 1 else 0
    x = bordo if len(voci) > 1 else (W - larg) / 2
    out = {}
    for p, base, _ in voci:
        w = pezzo(p).width; out[p] = (x + w / 2, base); x += w + gap
    return out


def stanza(nome, W):
    r = STANZE[nome]
    img = sfondo(W, r["m_alto"], r.get("m_basso"), r.get("fascia"), r["pav"], r.get("pav_g"))
    pos = disponi(W, r["pav_mobili"])
    for p, sotto, base in r.get("tappeti", []):
        if sotto in pos: tappeto(img, pezzo(p), pos[sotto][0], base)
    for p, sopra, cima in r.get("appesi", []):
        if sopra in pos: appendi(img, pezzo(p), pos[sopra][0], cima)
    for p, (cx, base) in pos.items(): appoggia(img, pezzo(p), cx, base)
    for p, sopra, base in r.get("davanti", []):
        if sopra in pos: appoggia(img, pezzo(p), pos[sopra][0], base)
    return img


if __name__ == "__main__":
    os.makedirs(os.path.join(DIR, "prove"), exist_ok=True)
    righe = []
    for nome, larghe in [("soggiorno", (110, 200)), ("camera", (100, 180)), ("cucina", (110, 190)), ("bagno", (90, 160))]:
        ims = [stanza(nome, w) for w in larghe]
        for w, im in zip(larghe, ims): im.save(os.path.join(DIR, "prove", f"{nome}_{w}.png"))
        righe.append(ims)
    G = 6
    Wt = max(sum(i.width for i in r) + G * (len(r) + 1) for r in righe); Ht = len(righe) * (H + G) + G
    tav = Image.new("RGBA", (Wt, Ht), (24, 18, 30, 255)); y = G
    for r in righe:
        x = G
        for im in r: tav.alpha_composite(im, (x, y)); x += im.width + G
        y += H + G
    tav.resize((Wt * SCALA, Ht * SCALA), Image.NEAREST).save(os.path.join(DIR, "prove", "prova.png"))
    print("ok")
