"""Prepara le immagini di una dimora per l'app.
- Interni: ritaglia la stanza dallo sfondo (scuro o verde), la porta alla stessa inquadratura delle stanze del castello
  (720x676, 720x706 il corridoio, stanza adattata al riquadro e appoggiata in basso al centro) su fondo nero;
  le porte aperte che mostrano il verde diventano buie.
- Fogli su fondo verde: separa le stanze (isometriche o viste di fronte) e le restituisce in ordine di lettura.
Uso come modulo: from prepara import interno, pezzi_foglio."""
import numpy as np
from PIL import Image
from scipy import ndimage

BUIO = (11, 9, 16)

def _verde(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (g > 150) & (g > r + 60) & (g > b + 60)

def _maschera_stanza(a, soglia=36):
    """Vero dove c'è la stanza: tolgo lo sfondo che tocca i bordi (colore dell'angolo) e tutto il verde chroma."""
    a = a.astype(int)
    bg = np.median(np.concatenate([a[:4, :4].reshape(-1, 3), a[:4, -4:].reshape(-1, 3), a[-4:, :4].reshape(-1, 3), a[-4:, -4:].reshape(-1, 3)]), axis=0)
    simile = (np.abs(a - bg).sum(-1) < soglia) | _verde(a)
    lab, _ = ndimage.label(simile)
    bordo = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fuori = np.isin(lab, list(bordo))
    m = ~fuori
    # la parte più grande, senza briciole
    lab2, n = ndimage.label(ndimage.binary_opening(m, iterations=2))
    if n > 1:
        sz = ndimage.sum(np.ones_like(lab2), lab2, range(1, n + 1)); m = lab2 == (1 + int(np.argmax(sz)))
    return ndimage.binary_fill_holes(m)

def interno(img, corridoio=False, margine=8, soglia=36):
    """img: PIL RGB(A) di una sola stanza. Restituisce un'immagine RGB 720x676 (o 720x706) come quelle del castello."""
    W, H = 720, (706 if corridoio else 676)
    a = np.array(img.convert("RGB"))
    m = _maschera_stanza(a, soglia)
    v = _verde(a.astype(int)) & m          # verde dentro la stanza (porte aperte)
    a = a.copy(); a[v] = BUIO
    ys, xs = np.where(m); x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    rgba = np.dstack([a, np.where(m, 255, 0).astype(np.uint8)])[y0:y1, x0:x1]
    st = Image.fromarray(rgba, "RGBA")
    k = min((W - 2 * margine) / st.width, (H - 2 * margine) / st.height)
    st = st.resize((round(st.width * k), round(st.height * k)), Image.LANCZOS)
    out = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    out.alpha_composite(st, ((W - st.width) // 2, H - margine - st.height))
    return out.convert("RGB")

def pezzi_foglio(img, min_area=40000, unisci=8):
    """Separa le stanze di un foglio su fondo verde. Restituisce [(x0,y0,x1,y1, PIL RGBA)] in ordine di lettura."""
    a = np.array(img.convert("RGB")).astype(int)
    fg = ~_verde(a)
    fg = ndimage.binary_opening(fg, iterations=2)
    # le stanze che si toccano sono separate da sottili linee verdi: le allargo erodendo, poi etichetto
    sep = ndimage.binary_erosion(fg, iterations=4) if unisci <= 0 else ndimage.binary_dilation(fg, iterations=unisci)
    lab, n = ndimage.label(sep)
    if unisci <= 0: lab = np.where(fg, ndimage.grey_dilation(lab, size=(11, 11)), 0)
    out = []
    for i, s in enumerate(ndimage.find_objects(lab)):
        h, w = s[0].stop - s[0].start, s[1].stop - s[1].start
        if h * w < min_area: continue
        m = (lab[s] == i + 1) & fg[s]
        rgb = np.array(img.convert("RGB"))[s].copy()
        rgba = np.dstack([rgb, np.where(m, 255, 0).astype(np.uint8)])
        out.append((s[1].start, s[0].start, s[1].stop, s[0].stop, Image.fromarray(rgba, "RGBA")))
    cy = lambda p: (p[1] + p[3]) / 2
    out.sort(key=cy); righe = []
    for p in out:
        if righe and abs(cy(p) - cy(righe[-1][-1])) < (p[3] - p[1]) * 0.5: righe[-1].append(p)
        else: righe.append([p])
    return [p for r in righe for p in sorted(r, key=lambda p: p[0])]
