#!/usr/bin/env python3
"""Calcola i posti per gli arredi (3 a terra, quadri sulle pareti) misurando la geometria di ogni interno isometrico.
Uso: python3 tools/arredi/slot_auto.py img/dimore/reggia/stanze/ > slot.json
Dal profilo alto e basso della sagoma (pixel non neri) ricava le due pareti e il rombo del pavimento con rette
interpolate, poi mette i posti in coordinate relative (frazioni lungo le pareti e il pavimento): così vanno bene
per stanze alte, basse, strette o larghe. La scala degli oggetti segue l'altezza delle pareti."""
import json, os, sys
import numpy as np
from PIL import Image

H_RIF = 300          # altezza di parete delle stanze del castello, su cui sono tarate le scale di base
def retta(xs, ys):
    """Retta robusta: due passate, la seconda senza i punti lontani (lampadari, archi che sporgono)."""
    m, q = np.polyfit(xs, ys, 1)
    r = np.abs(ys - (m * xs + q)); ok = r < max(6, np.percentile(r, 70))
    return np.polyfit(xs[ok], ys[ok], 1)

def misura(f):
    a = np.array(Image.open(f).convert("RGB")).astype(int); M = a.sum(2) > 45
    cols = np.where(M.sum(0) > 8)[0]; x0, x1 = cols.min(), cols.max(); W = x1 - x0
    top = np.array([np.argmax(M[:, x]) for x in range(x0, x1 + 1)], float)
    bot = np.array([M.shape[0] - 1 - np.argmax(M[::-1, x]) for x in range(x0, x1 + 1)], float)
    xs = np.arange(x0, x1 + 1, dtype=float)
    sx = lambda p, q: (xs >= x0 + p * W) & (xs <= x0 + q * W)
    tl, tr = retta(xs[sx(.05, .35)], top[sx(.05, .35)]), retta(xs[sx(.65, .95)], top[sx(.65, .95)])
    bl, br = retta(xs[sx(.05, .35)], bot[sx(.05, .35)]), retta(xs[sx(.65, .95)], bot[sx(.65, .95)])
    cx = (tr[1] - tl[1]) / (tl[0] - tr[0]); cx = min(max(cx, x0 + .2 * W), x1 - .2 * W)
    yt = lambda x: np.polyval(tl, x) if x <= cx else np.polyval(tr, x)
    fx = (br[1] - bl[1]) / (bl[0] - br[0]); fx = min(max(fx, x0 + .2 * W), x1 - .2 * W)
    yb = lambda x: np.polyval(bl, x) if x <= fx else np.polyval(br, x)
    spess = 0.03 * (yb(fx) - yt(cx))                  # spessore della lastra sotto il pavimento
    # Nel rombo del pavimento angolo dietro + angolo davanti = angolo sinistro + angolo destro:
    # (yt(cx)+hw) + (yb(fx)-spess) = (yt(x0)+hw) + (yt(x1)+hw)  ->  hw = yt(cx) + yb(fx) - spess - yt(x0) - yt(x1)
    hw = yt(cx) + yb(fx) - spess - yt(x0) - yt(x1)
    hw = float(min(max(hw, 60), 0.8 * (yb(fx) - yt(cx))))
    FL = np.array([x0, yt(x0) + hw]); FR = np.array([x1, yt(x1) + hw]); FBk = np.array([cx, yt(cx) + hw])
    pav = lambda u, v: FBk + u * (FL - FBk) + v * (FR - FBk)
    parete = lambda lato, s, h: (lambda x: [x, yt(x) + h * hw])(x0 + s * (cx - x0) if lato == "l" else cx + s * (x1 - cx))
    return dict(x0=x0, x1=x1, cx=cx, hw=hw, pav=pav, parete=parete, W=W)

def posti(nome, g):
    sc = round(min(1.15, max(.45, g["hw"] / H_RIF)), 3)
    t = [g["pav"](.8, .25), g["pav"](.25, .8), g["pav"](.85, .85)]
    t = [[round(float(p[0])), round(float(p[1])), round(.65 * sc, 3)] for p in t]
    if nome == "corridoio":
        pp = [("l", .3, .4, .75), ("l", .7, .4, .75), ("r", .35, .4, .75), ("r", .72, .4, .75), ("l", .5, .15, .5)]
    elif nome in ("balcone", "terrazzo", "giardino"):
        pp = [("r", .5, .4, 1)]
    else:
        pp = [("l", .45, .4, 1), ("r", .55, .4, 1)]
    p = [[round(float(x)), round(float(y)), lato, round(.55 * sc * k, 3)] for lato, s, h, k in pp for x, y in [g["parete"](lato, s, h)]]
    c = g["pav"](.55, .55); span = .16 * g["W"]
    piano = {"x0": round(float(c[0] - span)), "x1": round(float(c[0] + span)), "y": round(float(c[1])), "s": round(2.6 * min(1.1, max(.6, g["hw"] / H_RIF)), 2)}
    return {"t": t, "p": p, "piano": piano}

if __name__ == "__main__":
    d = sys.argv[1]; out = {}
    for f in sorted(os.listdir(d)):
        if f.endswith(".webp"): out[f[:-5]] = posti(f[:-5], misura(os.path.join(d, f)))
    print(json.dumps(out, separators=(",", ":")))
