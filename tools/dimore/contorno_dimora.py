#!/usr/bin/env python3
"""Ricompone il contorno di una dimora a partire dall'immagine del generatore (tools/dimore/modulare/<dimora>/cornice/contorno_gen.jpg):
un unico rettangolo per tutte le stanze, con le torri accanto (mai dentro) e il portone d'ingresso in basso.
L'immagine ha il cielo e l'apertura in verde #00FF00. L'apertura del generatore è più stretta di quella che serve alle stanze,
quindi la si allarga ripetendo un tratto della cornice in alto (merli o balaustra) e un tratto liscio di muro in basso, ai due lati del portone.
Uscite in img/dimore/<dimora>/: tetto.webp, base.webp (con l'apertura trasparente), muro.webp e muro_dx.webp (fasce che si ripetono in verticale).
Stampa i numeri da mettere in SKIN.<dimora>.cornice di js/app.js.
Uso (dalla radice del repo): python3 tools/dimore/contorno_dimora.py castello|reggia"""
import json, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

RADICE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT_W = 1536                              # larghezza finale delle immagini

# Misure sull'immagine del generatore (pixel dell'originale).
#  sx/dx: blocco sinistro/destro (cielo + torre + lato del rettangolo, fino al bordo dell'apertura) · centro: l'apertura
#  y_tetto: cima dell'immagine · y_foro: riga dove inizia l'apertura · y_fascia: dove iniziano le fasce delle torri (sotto eventuali finestre)
#  y_base: dove inizia la base · y_fondo: fondo dell'apertura · y_fine: fine dello zoccolo
#  ins: larghezza aggiunta all'apertura · xc: punto dove si ripete il tratto della cornice in alto
#  ins_base: [(posizione, inizio tessera, fine tessera, larghezza)]: tratti lisci di muro ripetuti ai lati del portone
#  bande: la base si compone in due fasce di righe (apertura / muro con finestre): nella fascia dell'apertura si allarga il vuoto,
#         in quella del muro le finestre si ripetono lungo tutta la riga (le tessere possono passare sopra il bordo dell'apertura)
CONF = {
 "castello": dict(sky=(54, 33, 49), sx=(37, 352), dx=(1088, 1401), foro_punto=(719, 1140), y_tetto=376, y_foro=728, y_fascia=728, y_base=1466, y_fondo=1551, y_fine=2089,
                  ins=513, xc=505, ins_base=[(436, 404, 462, 257), (1003, 972, 1026, 256)]),
 "reggia": dict(sky=(17, 27, 64), sx=(14, 335), dx=(1103, 1424), foro_punto=(719, 1130), y_tetto=180, y_foro=700, y_fascia=800, y_base=1450, y_fondo=1564, y_fine=2222,
                ins=622, xc=440, ins_base=[(417, 262, 417, 310), (1177, 1021, 1177, 312)], bande=True, y_liscio=1612, col_liscia=500),
}

dim = sys.argv[1] if len(sys.argv) > 1 else "castello"
C = CONF[dim]; SKY = C["sky"]
GEN = os.path.join(RADICE, f"tools/dimore/modulare/{dim}/cornice/contorno_gen.jpg")
OUT = os.path.join(RADICE, f"img/dimore/{dim}/")
(X_SX0, X_SX1), (X_DX0, X_DX1) = C["sx"], C["dx"]; CENTRO = (X_SX1, X_DX0); INS = C["ins"]

a = np.array(Image.open(GEN).convert("RGB")).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
verde = (g > 120) & (g > r + 45) & (g > b + 45)
lab, n = ndi.label(verde)
aperta = verde & (lab == lab[C["foro_punto"][1], C["foro_punto"][0]])          # l'apertura è il verde che contiene il suo punto centrale
cielo = verde & ~aperta                                                         # il resto (cielo, terreno, fessure tra torre e cornice) prende il colore del cielo
# il verde sfumato sul bordo della pietra: si toglie dal cielo (1 px) e si scurisce quello che resta
bordo = ndi.binary_dilation(verde, iterations=1)
vicino = ndi.binary_dilation(verde, iterations=4) & ~bordo
a2 = a.copy()
mix = (a2[..., 0] + a2[..., 2]) // 2
a2[..., 1] = np.where(vicino, np.minimum(a2[..., 1], mix), a2[..., 1])
a2[ndi.binary_dilation(cielo, iterations=1)] = SKY
foro = ndi.binary_dilation(aperta, iterations=1)
alpha = np.where(foro, 0, 255).astype(np.uint8)
a2[foro] = (0, 0, 0)
rgba = np.dstack([a2.clip(0, 255).astype(np.uint8), alpha])


def colonne(tipo):
    """Indici delle colonne dell'originale, nell'ordine in cui compongono la larghezza finale."""
    sx = list(range(X_SX0, CENTRO[0])); dx = list(range(CENTRO[1], X_DX1))
    if tipo == "tetto":      # la parte che si ripete (merli, balaustra) si copia una volta in più
        xc = C["xc"]
        mezzo = list(range(CENTRO[0], xc)) + list(range(xc, xc + INS)) + list(range(xc, CENTRO[1]))
    else:                    # base: tratti lisci di muro ai lati del portone, mai sopra fiaccole, stendardi o portone
        mezzo, x = [], CENTRO[0]
        for pos, ta, tb, lung in sorted(C["ins_base"]):
            mezzo += list(range(x, pos)) + [ta + i % (tb - ta) for i in range(lung)]; x = pos
        mezzo += list(range(x, CENTRO[1]))
    return np.array(sx + mezzo + dx)


def base_bande():
    """Base in due fasce: sopra il fondo dell'apertura si allarga il vuoto, sotto il muro continua con le finestre ripetute."""
    ya, yf, ye = C["y_base"], C["y_fondo"] + 2, C["y_fine"] + 14
    alto = rgba[ya:yf][:, list(range(X_SX0, CENTRO[1])) + [CENTRO[0] + 40] * INS + list(range(CENTRO[1], X_DX1))].copy()
    cols, x, ins = [], X_SX0, []
    for pos, ta, tb, lung in sorted(C["ins_base"]):
        cols += list(range(x, pos)); ins += [False] * (pos - x)
        cols += [ta + i % (tb - ta) for i in range(lung)]; ins += [True] * lung; x = pos
    cols += list(range(x, X_DX1)); ins += [False] * (X_DX1 - x)
    basso = rgba[yf:ye][:, cols].copy()
    # nelle prime righe (dove finisce la cornice dell'apertura) si usa lo stesso schema della fascia alta, con una colonna liscia al posto del vuoto
    n = C["y_liscio"] - yf
    liscia = list(range(X_SX0, CENTRO[0])) + [C["col_liscia"]] * (CENTRO[1] - CENTRO[0] + INS) + list(range(CENTRO[1], X_DX1))
    basso[:n] = rgba[yf:yf + n][:, liscia]
    assert alto.shape[1] == basso.shape[1], (alto.shape, basso.shape)
    return np.concatenate([alto, basso], 0)


def tessera_v(blocco, y0, y1):
    """Fascia che si ripete in verticale senza giunture: parte da y0 (dove finisce il tetto); si cerca la lunghezza L per cui le righe
    dopo la fine sono le più simili a quelle dell'inizio, così il taglio cade tra due righe compatibili."""
    best = None
    for L in range(240, y1 - y0 - 10):
        d = 0
        for k in range(-6, 6):
            d += np.abs(blocco[y0 + k].astype(int) - blocco[y0 + L + k].astype(int)).mean()
        if best is None or d < best[0]: best = (d, L)
    return best[1]


Y0, Y1, YB, YF, YE = C["y_tetto"], C["y_fascia"], C["y_base"], C["y_fondo"], C["y_fine"]
pezzi = {}
for nome, (ya, yb) in (("tetto", (Y0, Y1)), ("base", (YB, C["y_fine"] + 14))):
    parte = base_bande() if (nome == "base" and C.get("bande")) else rgba[ya:yb][:, colonne(nome)].copy()
    if nome == "base": parte[C["y_fine"] - ya:] = (*SKY, 255)       # qualche riga di cielo sotto lo zoccolo
    pezzi[nome] = parte
Wg = pezzi["tetto"].shape[1]; f = OUT_W / Wg
dimpx = {}
for nome in ("tetto", "base"):
    im = Image.fromarray(pezzi[nome]).resize((OUT_W, round(pezzi[nome].shape[0] * f)), Image.LANCZOS)
    im.save(OUT + nome + ".webp", lossless=True, method=6); dimpx[nome] = im.size

strisce = {}
for nome, (x0, x1) in (("muro", (X_SX0, X_SX1)), ("muro_dx", (X_DX0, X_DX1))):
    blocco = rgba[:, x0:x1, :3]
    L = tessera_v(blocco, Y1, YB)
    t = blocco[Y1:Y1 + L]
    tre = np.concatenate([t, t, t], 0)                                   # per ridimensionare senza bordi alla giuntura
    w = round((x1 - x0) * f)
    ri = np.array(Image.fromarray(tre).resize((w, round(tre.shape[0] * f)), Image.LANCZOS))
    h3 = ri.shape[0] // 3
    Image.fromarray(ri[h3:2 * h3]).save(OUT + nome + ".webp", lossless=True, method=6)
    strisce[nome] = (w, h3, L)

css = 768 / OUT_W
ov = round((YF - YB) * f); ov_t = round((Y1 - C["y_foro"]) * f)           # quanto la base sale sopra il fondo dell'apertura / il tetto scende sotto la cima
res = dict(tetto=[768, round(dimpx["tetto"][1] * css, 1), round(ov_t * css, 1)], base=[768, round(dimpx["base"][1] * css, 1), round(ov * css, 1)],
           muro=[round(strisce["muro"][0] * css, 1), round(strisce["muro"][1] * css, 1)], dx=[round(strisce["muro_dx"][0] * css, 1), round(strisce["muro_dx"][1] * css, 1)])
res["area"] = [res["muro"][0], round(768 - res["dx"][0], 1)]
print(dim, json.dumps(res), "tile", {k: v[2] for k, v in strisce.items()}, "px tetto", dimpx["tetto"], "base", dimpx["base"])
