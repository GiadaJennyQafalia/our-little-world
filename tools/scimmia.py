from PIL import Image
import numpy as np
C=32
PAL={
 "marrone":dict(f=(122,74,42),d=(84,48,26),s=(226,180,138),k=(185,132,99),o=(52,28,16)),
 "dorato": dict(f=(201,139,58),d=(146,94,34),s=(241,214,166),k=(205,165,118),o=(92,56,20)),
 "grigio": dict(f=(138,133,128),d=(98,93,90),s=(230,196,170),k=(190,152,128),o=(56,52,50)),
 "nero":   dict(f=(64,56,62),d=(40,34,38),s=(205,165,130),k=(160,120,92),o=(22,18,20)),
}
def grid(): return [["."]*C for _ in range(C)]
def put(g,x,y,c):
    if 0<=x<C and 0<=y<C: g[y][x]=c
def ell(g,cx,cy,rx,ry,c):
    for y in range(C):
        for x in range(C):
            if ((x-cx)/rx)**2+((y-cy)/ry)**2<=1.0: g[y][x]=c
def rect(g,x0,y0,x1,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): put(g,x,y,c)
def pts(g,ps,c):
    for x,y in ps: put(g,x,y,c)
def outline(g):
    out=[r[:] for r in g]
    for y in range(C):
        for x in range(C):
            if g[y][x]!="." : continue
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                xx,yy=x+dx,y+dy
                if 0<=xx<C and 0<=yy<C and g[yy][xx] not in ".o":
                    out[y][x]="o"; break
    return out

# ---- vista di lato, guarda a destra. leg: posizione zampe per il passo (0,1,2)
def lato(passo):
    g=grid()
    # coda arricciata dietro
    pts(g,[(8,17),(7,16),(6,15),(5,14),(5,13),(5,12),(6,11),(7,11),(8,12),(8,13),(7,13)],"f")
    # zampe (dietro e davanti), il passo sposta i piedi
    off=[(0,0),(1,-1),(-1,1)][passo]
    for bx,o in ((10,off[0]),(17,off[1])):
        rect(g,bx+o,20,bx+1+o,23,"d" if bx==10 else "f")
        rect(g,bx+o,24,bx+2+o,24,"k")
    # corpo
    ell(g,13.5,18.5,5.2,3.2,"f")
    rect(g,11,20,16,21,"f")
    pts(g,[(12,21),(13,21),(14,21),(15,21)],"s")
    # testa
    ell(g,19,13,3.6,3.6,"f")
    # orecchio
    pts(g,[(16,12),(16,13),(15,12),(15,13)],"s"); put(g,15,13,"k")
    # muso chiaro
    ell(g,20.4,14,2.2,2.3,"s")
    pts(g,[(21,16),(20,16)],"k")
    # fronte scura sopra gli occhi
    pts(g,[(19,11),(20,11),(21,11)],"d")
    put(g,21,13,"e"); put(g,22,15,"k")
    return g

def seduta():
    g=grid()
    pts(g,[(10,24),(9,24),(8,24),(7,23),(6,22),(6,21),(7,20),(8,20),(8,21)],"f")
    ell(g,14,20,4,4.2,"f")
    pts(g,[(15,21),(16,21),(15,22),(16,22),(16,20)],"s")
    rect(g,12,24,17,24,"k")
    rect(g,17,20,17,23,"d"); put(g,18,23,"k")
    ell(g,16,13,3.6,3.6,"f")
    pts(g,[(13,12),(13,13),(12,12),(12,13)],"s"); put(g,12,13,"k")
    ell(g,17.4,14,2.2,2.3,"s")
    pts(g,[(16,11),(17,11),(18,11)],"d")
    put(g,18,13,"e"); put(g,19,15,"k"); pts(g,[(18,16),(17,16)],"k")
    return g

def fronte(passo):
    g=grid()
    # coda di lato
    pts(g,[(19,21),(20,20),(21,19),(21,18),(20,17),(19,17)],"f")
    o=[(0,0),(-1,1),(1,-1)][passo]
    rect(g,13,21,14,23+min(0,o[0]),"f"); rect(g,17,21,18,23+min(0,o[1]),"f")
    rect(g,12,24+min(0,o[0]),14,24+min(0,o[0]),"k"); rect(g,17,24+min(0,o[1]),19,24+min(0,o[1]),"k")
    ell(g,15.5,18.5,3.8,3.6,"f")
    ell(g,15.5,19.2,2.0,2.2,"s")
    # braccia
    rect(g,11,17,11,21,"d"); rect(g,20,17,20,21,"d"); put(g,11,22,"k"); put(g,20,22,"k")
    # testa
    ell(g,15.5,12,4,3.7,"f")
    pts(g,[(11,11),(11,12),(10,11),(10,12),(20,11),(20,12),(21,11),(21,12)],"s")
    ell(g,15.5,13,2.8,2.4,"s")
    pts(g,[(14,10),(15,10),(16,10),(17,10)],"d")
    put(g,14,12,"e"); put(g,17,12,"e"); pts(g,[(15,14),(16,14)],"k"); pts(g,[(15,15),(16,15)],"k")
    return g

def retro(passo):
    g=grid()
    o=[(0,0),(-1,1),(1,-1)][passo]
    rect(g,13,21,14,23+min(0,o[0]),"d"); rect(g,17,21,18,23+min(0,o[1]),"d")
    rect(g,12,24+min(0,o[0]),14,24+min(0,o[0]),"k"); rect(g,17,24+min(0,o[1]),19,24+min(0,o[1]),"k")
    ell(g,15.5,18.5,3.8,3.6,"f")
    rect(g,11,17,11,21,"d"); rect(g,20,17,20,21,"d")
    ell(g,15.5,12,4,3.7,"f")
    pts(g,[(11,11),(11,12),(10,11),(10,12),(20,11),(20,12),(21,11),(21,12)],"s")
    pts(g,[(15,9),(16,9),(15,10)],"d")
    # coda alzata che si arriccia sopra la schiena
    pts(g,[(15,21),(15,22),(16,22),(17,22),(18,21),(19,20),(20,19),(21,18),(22,17),(22,16),(21,15),(20,15),(20,16)],"d")
    return g

def render(g,pal):
    g=outline(g)
    a=np.zeros((C,C,4),np.uint8)
    for y in range(C):
        for x in range(C):
            ch=g[y][x]
            if ch==".": continue
            col=pal["o"] if ch=="o" else (24,16,12) if ch=="e" else pal[ch]
            a[y,x]=(*col,255)
    return Image.fromarray(a,"RGBA")

def mirror(g): return [r[::-1] for r in g]

if __name__=="__main__":
    sheet=Image.new("RGBA",(512,256),(0,0,0,0))
    for ci,(nome,pal) in enumerate(PAL.items()):
        for p in range(3):
            # riga 0 destra, 1 su, 2 giù, 3 sinistra
            for riga,gg in ((0,lato(p)),(1,retro(p)),(2,fronte(p)),(3,mirror(lato(p)))):
                sheet.alpha_composite(render(gg,pal),((ci*4+p)*C,riga*C))
        sheet.alpha_composite(render(seduta(),pal),((ci*4+3)*C,0))
        sheet.alpha_composite(render(mirror(seduta()),pal),((ci*4+3)*C,3*C))
    sheet.save("assets/pets/scimmia.png")
    # anteprima ingrandita: colore marrone + i 4 colori di fianco
    prev=sheet.crop((0,0,128,128)).resize((512,512),Image.NEAREST)
    bg=Image.new("RGBA",(512+520,512),(58,48,68,255)); bg.alpha_composite(prev)
    row=Image.new("RGBA",(4*32,32)); 
    for ci in range(4): row.alpha_composite(sheet.crop(((ci*4)*C,0,(ci*4+1)*C,C)),(ci*32,0))
    bg.alpha_composite(row.resize((512,128),Image.NEAREST),(520,0))
    seat=Image.new("RGBA",(4*32,32))
    for ci in range(4): seat.alpha_composite(sheet.crop(((ci*4+3)*C,0,(ci*4+4)*C,C)),(ci*32,0))
    bg.alpha_composite(seat.resize((512,128),Image.NEAREST),(520,140))
    cat=Image.open("/home/claude/our-little-world/assets/pets/gatto.png").crop((0,0,32,32)).resize((128,128),Image.NEAREST)
    bg.alpha_composite(cat,(520,300)); bg.alpha_composite(sheet.crop((0,0,32,32)).resize((128,128),Image.NEAREST),(660,300))
    bg.save("scimmia_anteprima.png")
