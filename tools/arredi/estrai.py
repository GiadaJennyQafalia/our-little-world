import json, os, numpy as np, colorsys
from PIL import Image
from scipy import ndimage
exec(open("trova.py").read().split("for k,f in FOGLI.items():")[0])
OUT="/home/claude/our-little-world/assets/arredi/"; os.makedirs(OUT,exist_ok=True)
N={
"reliquie":[("anfora","Anfora greca"),("busto","Busto di marmo"),("astrolabio","Astrolabio d'ottone"),("clessidra","Clessidra antica"),("mappamondo","Mappamondo"),("leggio","Libro degli incantesimi"),("gatto_egizio","Gatto egizio"),("specchio_magico","Specchio su piede"),("mappa_tesoro","Mappa del tesoro"),("lanterna","Lanterna appesa")],
"casa":[("macchina_cucire","Macchina da cucire"),("scopa_secchio","Scopa e secchio"),("cesto_cucito","Cesto da cucito"),("torta","Torta sotto la campana"),("ciotola_mattarello","Ciotola e mattarello"),("profumi","Profumi e alambicco"),("cavalletto","Cavalletto da pittura"),("zaino","Zaino da escursione"),("felce","Felce in vaso"),("filatoio","Filatoio"),("baule","Baule col telo")],
"medievali":[("d_regina","La regina in trono"),("d_cavaliere","Il cavaliere col vessillo"),("d_citta","La città murata"),("d_dama_falco","La dama col falco"),("d_mietitura","La mietitura"),("d_musici","I musici"),("d_drago","Il cavaliere e il drago"),("d_giardino","Il giardino della fontana"),("d_angelo","L'angelo col giglio"),("d_banchetto","Il banchetto")],
"arazzi2":[("a_drago_torre","Arazzo del drago sulla torre"),("d_cervi","Cervi al chiaro di luna"),("d_caccia","La caccia al cervo"),("d_tempesta","Nave nella tempesta"),("d_neve","Villaggio sotto la neve"),("d_gatto_re","Il gatto con la corona"),("d_strega","La casetta della strega"),("d_stelle","Il cielo delle costellazioni"),("spade_scudo","Spade e scudo"),("vetrata","Vetrata della rosa")],
"arazzi1":[("a_unicorno","Arazzo dell'unicorno"),("a_castello","Arazzo del castello stellato"),("stendardo","Stendardo del leone"),("d_dama","Ritratto di dama"),("d_ritratto_cav","Ritratto di cavaliere"),("d_montagne","Montagne al tramonto"),("d_natura_morta","Natura morta con candela"),("specchio_oro","Specchio dorato"),("d_mappa","Mappa del mondo"),("trittico","Trittico dorato")],
"strumenti":[("pianoforte","Pianoforte a coda"),("clavicembalo","Clavicembalo"),("arpa","Arpa d'oro"),("violoncello","Violoncello"),("liuto","Liuto"),("ghironda","Ghironda"),("grammofono","Grammofono"),("organo","Organo a canne"),("tamburo","Tamburo"),("violino","Violino nella custodia")]}
CAT={"reliquie":"reliquia","casa":"casa","medievali":"dipinto","arazzi2":"dipinto","arazzi1":"dipinto","strumenti":"strumento"}
PREZZO={"reliquia":200,"casa":100,"dipinto":150,"strumento":150}
SPECIALI={"pianoforte":250,"clavicembalo":250,"organo":250,"arpa":250,"trittico":200,"vetrata":200,"d_angelo":200}
ARAZZI={"a_drago_torre","a_unicorno","a_castello","stendardo"}
SCALA=0.36
cat=[]
for k,f in FOGLI.items():
    im,fg,bg=maschera(A+f); H,W=fg.shape
    fg=ndimage.binary_opening(fg,iterations=2)
    lab,n=ndimage.label(ndimage.binary_dilation(fg,iterations=8))
    boxes=[]
    for i,s in enumerate(ndimage.find_objects(lab)):
        if (s[0].stop-s[0].start)*(s[1].stop-s[1].start)<=6000: continue
        boxes.append((s,i+1))
    cy=lambda b:(b[0][0].start+b[0][0].stop)/2
    boxes.sort(key=cy); righe=[[boxes[0]]]
    for b in boxes[1:]:
        if cy(b)-cy(righe[-1][-1])>220: righe.append([b])
        else: righe[-1].append(b)
    ordine=[b for r in righe for b in sorted(r,key=lambda b:b[0][1].start)]
    assert len(ordine)==len(N[k]),(k,len(ordine))
    for (s,li),(idd,nome) in zip(ordine,N[k]):
        m=(lab[s]==li)&fg[s]
        rgb=im[s].astype(float).copy()
        # bordo: niente riflesso verde
        vicino=ndimage.binary_dilation(~m,iterations=3)&m
        g=rgb[...,1]; cap=np.maximum(rgb[...,0],rgb[...,2])+8
        rgb[...,1]=np.where(vicino,np.minimum(g,cap),g)
        if idd in ("clessidra","torta"):  # vetro verde: ambra / vetro chiaro
            gg=(rgb[...,1]>rgb[...,0]+25)&(rgb[...,1]>rgb[...,2]+25)&m
            r,gc,bc=rgb[...,0],rgb[...,1],rgb[...,2]
            L=(r*.3+gc*.59+bc*.11)
            if idd=="clessidra": new=np.stack([L*1.15+30,L*0.85+10,L*0.35],-1)
            else: new=np.stack([L*0.95+20,L*1.0+22,L*1.08+30],-1)
            rgb[gg]=new[gg]
        a=np.where(m,255,0)
        img=Image.fromarray(np.dstack([np.clip(rgb,0,255),a]).astype(np.uint8),"RGBA")
        bb=img.getbbox(); img=img.crop(bb)
        w,h=img.size; img=img.resize((max(1,round(w*SCALA)),max(1,round(h*SCALA))),Image.LANCZOS)
        al=np.array(img); al[...,3]=np.where(al[...,3]>110,255,0); img=Image.fromarray(al)
        img.save(OUT+idd+".png",optimize=True)
        c=CAT[k]; posto="parete" if c=="dipinto" else "terra"
        tipo="arazzo" if idd in ARAZZI else c
        cat.append({"id":idd,"nome":nome,"tipo":tipo,"posto":posto,"prezzo":SPECIALI.get(idd,PREZZO[c]),"w":img.size[0],"h":img.size[1]})
json.dump(cat,open(OUT+"arredi.json","w"),ensure_ascii=False,indent=0)
print(len(cat))
# contact sheet
ims=[(c,Image.open(OUT+c["id"]+".png")) for c in cat]
cols=11; cw=200; ch=210
sheet=Image.new("RGBA",(cols*cw,((len(ims)+cols-1)//cols)*ch),(46,36,58,255))
for i,(c,m) in enumerate(ims):
    x,y=(i%cols)*cw,(i//cols)*ch
    sheet.alpha_composite(m,(x+(cw-m.width)//2,y+ch-m.height-6))
sheet.save("/tmp/claude-0/-home-claude/204f82a5-5bfa-5d11-a784-4d48705ba746/scratchpad/arredi_tutti.png"); print(sheet.size)
