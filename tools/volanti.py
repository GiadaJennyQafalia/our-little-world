"""Fogli di corvo e pipistrello nel formato degli animali dell'app.
512x256, celle 32x32: 4 colori x 4 colonne; righe 0 destra, 1 su, 2 giù, 3 sinistra.
Colonne 0-2 = volo (ali giù, a metà, su), colonna 3 = a riposo (corvo posato a terra, pipistrello appeso a testa in giù).
Sorgenti: [LPC] Birds (bluecarrot16) e [LPC] Monsters, pipistrello di bagzie."""
from PIL import Image
import colorsys

def tinta(img, h, s_mul, l_mul, l_add=0.0):
    out = img.copy(); px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if not a: continue
            hh, ll, ss = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
            hh2 = hh if h is None else h
            ll2 = min(1, ll * l_mul + l_add); ss2 = min(1, ss * s_mul)
            rr, gg, bb = colorsys.hls_to_rgb(hh2, ll2, ss2)
            px[x, y] = (round(rr * 255), round(gg * 255), round(bb * 255), a)
    return out

def tinta_parti(img, f_corpo, protetti):
    """Ricolora solo i pixel non 'protetti' (becco, occhi): protetti(r,g,b) -> True per lasciarli."""
    t = f_corpo(img); src = img.load(); dst = t.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = src[x, y]
            if a and protetti(r, g, b): dst[x, y] = (r, g, b, a)
    return t

def foglio(celle, varianti, nome):
    out = Image.new("RGBA", (512, 256))
    for ci, f in enumerate(varianti):
        for riga in range(4):
            for col in range(4):
                out.alpha_composite(f(celle[riga][col]), ((ci * 4 + col) * 32, riga * 32))
    out.save(f"assets/pets/{nome}.png")

# ---- Corvo: 3x8 celle 32; righe 0-3 volo (sinistra, su, giù, destra), 4-7 a terra (stesso ordine)
B = Image.open("tools/sorgenti/lpc_bird_2_black.png").convert("RGBA")
cb = lambda r, c: B.crop((c * 32, r * 32, c * 32 + 32, r * 32 + 32))
ord_app = {0: 3, 1: 1, 2: 2, 3: 0}  # riga app -> riga sorgente
corvo = [[cb(ord_app[r], 0), cb(ord_app[r], 1), cb(ord_app[r], 2), cb(4 + ord_app[r], 0)] for r in range(4)]
becco = lambda r, g, b: r > 150 and g > 110 and b < 120 and r > b + 60
foglio(corvo, [
    lambda i: i,
    lambda i: tinta_parti(i, lambda j: tinta(j, 0.62, 2.2, 1.05, 0.03), becco),   # blu notte
    lambda i: tinta_parti(i, lambda j: tinta(j, None, 0.2, 1.6, 0.12), becco),    # grigio
    lambda i: tinta_parti(i, lambda j: tinta(j, None, 0.1, 1.0, 0.62), becco),    # bianco
], "corvo")

# ---- Pipistrello: 7x4 celle 64; righe 0 su, 1 sinistra, 2 giù, 3 destra; col 0 a terra, 1-4 volo
P = Image.open("tools/sorgenti/lpc_bat.png").convert("RGBA")
def cp(r, c, terra=False):
    x0, y0 = c * 64 + 16, r * 64 + (21 if terra else 12)
    return P.crop((x0, y0, x0 + 32, y0 + 32))
ord_bat = {0: 3, 1: 0, 2: 2, 3: 1}
import importlib.util, os
_sp = importlib.util.spec_from_file_location("appeso", os.path.join(os.path.dirname(__file__), "pipistrello_appeso.py")); _m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
appeso = _m.posa()  # colonna 3: a riposo, appeso a testa in giù (disegnato da codice)
pip = [[cp(ord_bat[r], 1), cp(ord_bat[r], 2), cp(ord_bat[r], 3), appeso] for r in range(4)]
occhi = lambda r, g, b: r > 150 and g < 90 and b < 90
foglio(pip, [
    lambda i: i,                                                                   # viola
    lambda i: tinta_parti(i, lambda j: tinta(j, None, 0.25, 0.72), occhi),          # nero
    lambda i: tinta_parti(i, lambda j: tinta(j, 0.07, 1.4, 1.0, 0.02), occhi),      # marrone
    lambda i: tinta_parti(i, lambda j: tinta(j, None, 0.15, 1.2, 0.42), occhi),     # argento
], "pipistrello")
