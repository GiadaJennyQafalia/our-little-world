import sys, numpy as np
from PIL import Image
from scipy import ndimage
A=(sys.argv[1] if len(sys.argv) > 1 else "sorgenti") + "/"  # cartella con i fogli generati (jpg su fondo verde)
FOGLI={"reliquie":"674f5cb3-image.jpg","casa":"2c699af6-image.jpg","medievali":"92e10582-image.jpg","arazzi2":"a4f353b1-image.jpg","arazzi1":"54d7159a-image.jpg","strumenti":"67e500ec-image.jpg"}
def maschera(path):
    im=np.array(Image.open(path).convert("RGB")).astype(int)
    h,w,_=im.shape
    bordo=np.concatenate([im[0],im[-1],im[:,0],im[:,-1]]); bg=np.median(bordo,axis=0)
    d=np.sqrt(((im-bg)**2).sum(-1))
    simile=(d<70)|((im[...,1]>im[...,0]+60)&(im[...,1]>im[...,2]+60)&(d<120))
    # tutto ciò che è verde chroma, anche nei buchi (manici, gambe, corde); i verdi spenti dei dipinti restano
    croma=(d<80)|((im[...,1]>im[...,0]+70)&(im[...,1]>im[...,2]+70)&(im[...,1]>170))
    return im,~croma,bg
for k,f in FOGLI.items():
    im,fg,bg=maschera(A+f)
    fg2=ndimage.binary_opening(fg,iterations=2)
    lab,n=ndimage.label(ndimage.binary_dilation(fg2,iterations=8))
    objs=[(s,(lab[s]==i+1)) for i,s in enumerate(ndimage.find_objects(lab))]
    big=[(s[1].start,s[0].start,s[1].stop-s[1].start,s[0].stop-s[0].start) for s,m in objs if (s[0].stop-s[0].start)*(s[1].stop-s[1].start)>6000]
    big.sort(key=lambda b:(round((b[1]+b[3]/2)/250),b[0]))
    print(k,im.shape[:2],bg.astype(int),len(big),big)
