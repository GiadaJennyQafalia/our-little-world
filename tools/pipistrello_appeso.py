"""Posa del pipistrello appeso a testa in giù (32x32), disegnata da codice con i colori dello sprite di bagzie.
Ali chiuse attorno al corpo, artigli in alto, testa in basso con le orecchie che puntano giù."""
from PIL import Image
PAL = {"o": (29, 24, 30), "d": (67, 47, 83), "m": (92, 67, 111), "p": (181, 114, 177), "b": (95, 95, 123),
       "l": (119, 132, 162), "e": (174, 0, 0), "f": (255, 249, 214)}
DIS = [
    "....o.....o....",
    "....o.....o....",
    "...odo...odo...",
    "..odmdoooddmo..",
    ".odmmmdmdmmmdo.",
    "odmpmmmdmmmpmdo",
    "odmpmmmdmmmpmdo",
    "odmmpmmdmmpmmdo",
    "odmmpmmdmmpmmdo",
    ".odmpmmdmmpmdo.",
    ".odmmpmdmpmmdo.",
    "..odmpmdmpmdo..",
    "..odmmpdpmmdo..",
    "...oddmdmddo...",
    "....oobbboo....",
    "...obbbbbbbo...",
    "...obfbbbfbo...",
    "..oblllllllbo..",
    "..oblelllelbo..",
    "...oblllllbo...",
    "..obo.....obo..",
    "..oo.......oo..",
]
def posa():
    im = Image.new("RGBA", (32, 32))
    w = max(len(r) for r in DIS); x0 = (32 - w) // 2; y0 = 3
    for y, r in enumerate(DIS):
        for x, ch in enumerate(r):
            if ch != ".": im.putpixel((x0 + x, y0 + y), (*PAL[ch], 255))
    return im
if __name__ == "__main__":
    posa().resize((256, 256), Image.NEAREST).save("pipistrello_appeso.png")
