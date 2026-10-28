#!/usr/bin/env python3
"""Per ogni tessera frontale crea una striscia "neutra" da ripetere ai lati quando la cella della pianta è più larga
della tessera: così la stanza si allunga (muro, zoccolo, pavimento) invece di lasciare buchi neri.
Uso: python3 tools/dimore/riempi.py img/dimore/castello/tessere/
Scrive <dir>/riempi/<tipo>.webp. Ogni riga della striscia è il colore mediano di quella riga della tessera, preso
solo dalle colonne "tranquille" (poco dettaglio): restano le fasce di muro e pavimento, spariscono i mobili, che
ripetuti farebbero file di camini o armadi. Un leggero rumore di righe vicine evita l'effetto tinta piatta."""
import os, sys
import numpy as np
from PIL import Image

d = sys.argv[1]; out = os.path.join(d, "riempi"); os.makedirs(out, exist_ok=True)
for f in sorted(os.listdir(d)):
    if not f.endswith(".webp"): continue
    a = np.asarray(Image.open(os.path.join(d, f)).convert("RGB")).astype(float); h, w, _ = a.shape
    g = a.sum(2); grad = np.zeros_like(g); grad[1:] += np.abs(np.diff(g, axis=0)); grad[:, 1:] += np.abs(np.diff(g, axis=1))
    m = round(w * .04); cols = np.arange(m, w - m)
    calme = cols[np.argsort(grad[:, cols].mean(0))[: max(4, len(cols) // 3)]]      # il terzo di colonne più tranquille
    prof = np.median(a[:, calme], axis=1)                                          # h × 3
    ws = 16; s = np.repeat(prof[:, None, :], ws, axis=1)
    rng = np.random.default_rng(1); tex = a[:, calme][:, rng.integers(0, len(calme), ws)] - prof[:, None, :]
    s = np.clip(s + .35 * np.clip(tex, -40, 40), 0, 255)
    Image.fromarray(s.astype(np.uint8)).save(os.path.join(out, f), quality=92)
    print(f, w, h)
