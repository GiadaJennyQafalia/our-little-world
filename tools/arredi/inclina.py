# Porta i quadri all'inclinazione delle pareti isometriche (2:1): sale verso destra con pendenza 0.5 (parete sinistra).
import json, numpy as np
from PIL import Image
D="/home/claude/our-little-world/assets/arredi/"
cat=json.load(open(D+"arredi.json"))
for c in cat:
    if c["posto"]!="parete": continue
    im=Image.open(D+c["id"]+".png"); a=np.array(im); A=a[...,3]>0; h,w=A.shape
    xs=np.arange(int(w*.25),int(w*.75)); tops=np.array([np.argmax(A[:,x]) if A[:,x].any() else np.nan for x in xs],float)
    ok=~np.isnan(tops); s=np.polyfit(xs[ok],tops[ok],1)[0]   # pendenza attuale (negativa = sale a destra)
    k=-0.5-s
    sh=np.round(k*np.arange(w)).astype(int); off=-sh.min(); H=h+sh.max()-sh.min()
    out=np.zeros((H,w,4),np.uint8)
    for x in range(w): out[sh[x]+off:sh[x]+off+h,x]=a[:,x]
    img=Image.fromarray(out); img=img.crop(img.getbbox()); img.save(D+c["id"]+".png",optimize=True)
    c["w"],c["h"]=img.size; c["pend"]=round(float(s),3)
json.dump(cat,open(D+"arredi.json","w"),ensure_ascii=False,indent=0)
print([ (c["id"],c.get("pend")) for c in cat if c["posto"]=="parete"][:6])
