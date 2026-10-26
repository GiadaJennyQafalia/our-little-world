#!/usr/bin/env python3
"""Costruisce assets/lpc + assets/lpc/catalogo.json dalla Universal LPC Spritesheet Character Generator.
Uso: python3 tools/build_lpc.py <cartella del clone del generatore> <cartella di destinazione assets/lpc>
Il clone si prepara con: git clone --depth 1 --filter=blob:none https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator gen
Copia solo la camminata (walk): il primo fotogramma è la posa ferma dei pezzi scelti qui sotto."""
import json, os, shutil, subprocess, sys
GEN, OUT = sys.argv[1], sys.argv[2]
ANIM = ["walk"]
CORPI = ["male", "female"]
# slot -> elenco di (id, file di definizione, etichetta italiana)
SCELTA = {
 "capelli": [
  ("long", "hair/long/hair_long", "Lunghi"), ("wavy", "hair/long/hair_wavy", "Mossi"), ("loose", "hair/long/hair_loose", "Sciolti"),
  ("long_messy", "hair/long/hair_long_messy", "Lunghi scompigliati"), ("xlong", "hair/xlong/hair_xlong", "Lunghissimi"),
  ("xlong_wavy", "hair/xlong/hair_xlong_wavy", "Lunghissimi mossi"), ("princess", "hair/xlong/hair_princess", "Principessa"),
  ("bob", "hair/bob/hair_bob", "Caschetto"), ("page", "hair/short/hair_page", "Paggetto"), ("pixie", "hair/short/hair_pixie", "Pixie"),
  ("messy", "hair/short/hair_messy", "Scompigliati"), ("bedhead", "hair/short/hair_bedhead", "Spettinati"), ("parted", "hair/short/hair_parted", "Scriminatura"),
  ("swoop", "hair/short/hair_swoop", "Ciuffo"), ("mop", "hair/short/hair_mop", "Mop"), ("curtains", "hair/short/hair_curtains", "A tendina"),
  ("unkempt", "hair/short/hair_unkempt", "Ribelli"), ("plain", "hair/short/hair_plain", "Semplici"),
  ("ponytail", "hair/braids/hair_ponytail", "Coda"), ("high_ponytail", "hair/braids/hair_high_ponytail", "Coda alta"),
  ("braid", "hair/braids/hair_braid", "Treccia"), ("long_tied", "hair/braids/hair_long_tied", "Raccolti lunghi"), ("topknot", "hair/braids/hair_topknot_short", "Chignon")],
 "orecchie": [("elven", "head/ears/head_ears_elven", "Elfiche"), ("elven_m", "head/ears/head_ears_medium", "Elfiche medie"),
  ("cat", "head/furry_ears/top/head_ears_cat_skin", "Da gatto"), ("wolf", "head/furry_ears/top/head_ears_wolf_skin", "Da lupo"),
  ("big", "head/ears/head_ears_big", "Grandi"), ("dragon", "head/ears/head_ears_dragon", "Da drago"), ("long", "head/ears/head_ears_long", "Lunghe")],
 "corna": [("curled", "head/appendages/head_horns_curled", "Corna ricurve"), ("back", "head/appendages/head_horns_backwards", "Corna all'indietro")],
 "busto": [
  ("longsleeve", "torso/shirts/longsleeve/torso_clothes_longsleeve", "Maniche lunghe"), ("longsleeve2", "torso/shirts/longsleeve/torso_clothes_longsleeve2", "Maniche lunghe 2"),
  ("scoop", "torso/shirts/longsleeve/torso_clothes_longsleeve_scoop", "Scollo ampio"), ("vneck", "torso/shirts/shortsleeve/torso_clothes_tshirt_vneck", "Maglia a V"),
  ("sleeveless", "torso/shirts/sleeveless/torso_clothes_sleeveless2", "Senza maniche"), ("tanktop", "torso/shirts/sleeveless/torso_clothes_sleeveless_tanktop", "Canotta"),
  ("tunic", "torso/shirts/torso_clothes_tunic", "Tunica"), ("corset", "torso/shirts/torso_clothes_corset", "Corsetto"), ("blouse", "torso/shirts/torso_clothes_blouse", "Camicetta"),
  ("robe", "torso/shirts/torso_clothes_robe", "Veste lunga"), ("vest", "torso/vest/torso_clothes_vest", "Gilet"), ("tabard", "torso/jacket/torso_jacket_tabard", "Tabarro"),
  ("trench", "torso/jacket/torso_jacket_trench", "Trench"), ("frock", "torso/jacket/torso_jacket_frock", "Redingote"),
  ("leather", "torso/armour/torso_armour_leather", "Armatura di cuoio"), ("legion", "torso/armour/torso_armour_legion", "Armatura legionaria"), ("plate", "torso/armour/torso_armour_plate", "Armatura a piastre"),
  ("bodice", "torso/dresses/dress_bodice", "Corpetto"), ("sash", "torso/dresses/dress_sash", "Abito con fusciacca"), ("dress_slit", "torso/dresses/dress_slit", "Abito con spacco")],
 "gambe": [("pants", "legs/pants/legs_pants", "Pantaloni"), ("pants2", "legs/pants/legs_pants2", "Pantaloni lunghi"), ("pantaloons", "legs/pants/legs_pantaloons", "Calzoni"),
  ("skirt", "legs/skirts/legs_skirts_plain", "Gonna"), ("skirt_slit", "legs/skirts/legs_skirts_slit", "Gonna con spacco")],
 "scarpe": [("boots", "feet/boots/feet_boots_basic", "Stivali"), ("boots_fold", "feet/boots/feet_boots_fold", "Stivali risvoltati"),
  ("shoes", "feet/shoes/feet_shoes_basic", "Scarpe"), ("shoes_sara", "feet/shoes/feet_shoes_sara", "Scarpette")],
 "mantello": [("solid", "torso/cape/cape_solid", "Mantello"), ("tattered", "torso/cape/cape_tattered", "Mantello logoro")],
 "cappello": [
  ("wizard", "headwear/hats/magic/hat_magic_wizard", "Cappello da mago"), ("celestial", "headwear/hats/magic/hat_magic_celestial", "Cappello celeste"),
  ("hood", "headwear/coverings/hoods/hat_hood_cloth", "Cappuccio"), ("leathercap", "headwear/hats/caps/hat_cap_leather", "Berretto di cuoio"),
  ("cavalier", "headwear/hats/caps/hat_cap_cavalier", "Cappello da cavaliere"), ("bandana", "headwear/coverings/bandana/hat_bandana", "Bandana"),
  ("headband", "headwear/coverings/headbands/hat_headband_thick", "Fascia"), ("crown", "headwear/hats/formal/hat_formal_crown", "Corona"), ("tiara", "headwear/hats/formal/hat_formal_tiara", "Diadema"),
  ("barbuta", "headwear/helmets/helmets/hat_helmet_barbuta", "Elmo barbuta"), ("bascinet", "headwear/helmets/helmets/hat_helmet_bascinet", "Elmo bacinetto"),
  ("kettle", "headwear/helmets/helmets/hat_helmet_kettle", "Elmo a bombetta"), ("nasal", "headwear/helmets/helmets/hat_helmet_nasal", "Elmo nasale"),
  ("greathelm", "headwear/helmets/helmets/hat_helmet_greathelm", "Grande elmo"),
  ("large", "headwear/hats/magic/hat_magic_large", "Cappello a tesa larga"), ("bowler", "headwear/hats/formal/hat_formal_bowler", "Bombetta"), ("tophat", "headwear/hats/formal/hat_formal_tophat", "Cilindro"),
  ("bonnie", "headwear/hats/caps/hat_cap_bonnie", "Berretto bonnie"), ("santa", "headwear/hats/holiday/hat_holiday_santa", "Cappello di Natale"), ("elfhat", "headwear/hats/holiday/hat_holiday_elf", "Cappello da elfo")],
 "accessorio": [("earrings_moon", "headwear/accessories/earrings/facial_earrings_moon", "Orecchini luna"), ("earrings_stud", "headwear/accessories/earrings/facial_earrings_stud", "Orecchini a perno"),
  ("earrings_emerald", "headwear/accessories/earrings/facial_earrings_emerald", "Orecchini smeraldo"), ("glasses", "headwear/accessories/glasses/facial_glasses", "Occhiali"),
  ("glasses_round", "headwear/accessories/glasses/facial_glasses_round", "Occhiali tondi"), ("sunglasses", "headwear/accessories/glasses/facial_glasses_sunglasses", "Occhiali da sole"),
  ("glasses_half", "headwear/accessories/glasses/facial_glasses_halfmoon", "Occhiali a mezzaluna"), ("glasses_nerd", "headwear/accessories/glasses/facial_glasses_nerd", "Occhiali nerd"),
  ("glasses_sec", "headwear/accessories/glasses/facial_glasses_secretary", "Occhiali da segretaria"), ("shades", "headwear/accessories/glasses/facial_glasses_shades", "Occhiali scuri"),
  ("eyepatch", "headwear/accessories/eyepatch/facial_eyepatch_ambi", "Benda sull'occhio"), ("mask", "headwear/accessories/facial_mask_plain", "Maschera")],
 "arma": [("wand", "weapons/magic/weapon_magic_wand", "Bacchetta"), ("gnarled", "weapons/magic/weapon_magic_gnarled", "Bastone nodoso"),
  ("crystal", "weapons/magic/weapon_magic_crystal", "Bastone di cristallo"), ("simple", "weapons/magic/weapon_magic_simple", "Bastone semplice"),
  ("bow", "weapons/ranged/bow/weapon_ranged_bow_normal", "Arco"), ("recurve", "weapons/ranged/bow/weapon_ranged_bow_recurve", "Arco ricurvo"), ("greatbow", "weapons/ranged/bow/weapon_ranged_bow_great", "Arco lungo"),
  ("dagger", "weapons/sword/weapon_sword_dagger", "Pugnale"), ("arming", "weapons/sword/weapon_sword_arming", "Spada"), ("longsword", "weapons/sword/weapon_sword_longsword", "Spadone"), ("rapier", "weapons/sword/weapon_sword_rapier", "Stocco"),
  ("katana", "weapons/sword/weapon_sword_katana", "Katana"), ("mace", "weapons/blunt/weapon_blunt_mace", "Mazza"), ("club", "weapons/blunt/weapon_blunt_club", "Clava"), ("spear", "weapons/polearm/weapon_polearm_spear", "Lancia"),
  ("scythe", "weapons/polearm/weapon_polearm_scythe", "Falce"), ("trident", "weapons/polearm/weapon_polearm_trident", "Tridente"), ("cane", "weapons/polearm/weapon_polearm_cane", "Bastone da passeggio"),
  ("watering", "tools/tool_watering_can", "Annaffiatoio"), ("hoe", "tools/tool_hoe", "Zappa"), ("shovel", "tools/tool_shovel", "Pala"), ("rod", "tools/tool_rod", "Canna da pesca"), ("pickaxe", "tools/tool_pickaxe", "Piccone"), ("hammer", "tools/tool_hammer", "Martello")],
 "collo": [("amulet_star", "headwear/neck/charms/neck_amulet_star", "Amuleto stella"), ("amulet_cross", "headwear/neck/charms/neck_amulet_cross", "Amuleto a croce"), ("amulet_dangle", "headwear/neck/charms/neck_amulet_dangle", "Amuleto pendente"),
  ("necklace", "headwear/neck/neck_necklace", "Collana"), ("bowtie", "headwear/neck/neck_bowtie", "Papillon"), ("cravat", "headwear/neck/neck_cravat", "Cravattino"), ("jabot", "headwear/neck/neck_jabot", "Jabot"), ("scarf", "headwear/neck/neck_scarf", "Sciarpa")],
 "vita": [("belt_leather", "torso/waist/belt_leather", "Cintura di cuoio"), ("belt_mage", "torso/waist/belt_mage", "Cintura da mago"), ("belt_double", "torso/waist/belt_double", "Doppia cintura"),
  ("sash", "torso/waist/belt_sash", "Fusciacca"), ("sash_n", "torso/waist/belt_sash_narrow", "Fusciacca stretta"), ("waistband", "torso/waist/belt_waistband", "Fascia in vita")],
 "braccia": [("gloves", "arms/arms_gloves", "Guanti"), ("bracers", "arms/wrists/arms_bracers", "Bracciali"), ("cuffs", "arms/wrists/wrists_cuffs", "Polsini"), ("pauldrons", "arms/shoulders/shoulders_pauldrons", "Spalline corazzate"), ("epaulets", "arms/shoulders/shoulders_epaulets", "Spalline")],
 "schiena": [("backpack", "torso/backpack/backpack", "Zaino"), ("basket", "torso/backpack/backpack_basket", "Cesto"), ("quiver", "torso/backpack/quiver", "Faretra"), ("squarepack", "torso/backpack/backpack_squarepack", "Sacca quadrata")],
 "scudo": [("crusader", "weapons/shields/engrailed/shield_crusader", "Scudo crociato"), ("plus", "weapons/shields/engrailed/shield_plus", "Scudo a croce")],
 "barba": [("beard", "hair/beards/beards_beard", "Barba"), ("beard_medium", "hair/beards/beards_medium", "Barba media"), ("beard_trimmed", "hair/beards/beards_trimmed", "Barba curata"), ("beard_winter", "hair/beards/beards_winter", "Barba lunga"),
  ("stubble", "hair/beards/beards_5oclock_shadow", "Barba di tre giorni"), ("mustache", "hair/mustaches/beards_mustache", "Baffi"), ("handlebar", "hair/mustaches/beards_handlebar", "Baffi a manubrio"), ("chevron", "hair/mustaches/beards_chevron", "Baffi a V"), ("walrus", "hair/mustaches/beards_walrus", "Baffoni")],
 "ali": [("bat", "body/wings/wings_bat", "Ali di pipistrello"), ("feathered", "body/wings/wings_feathered", "Ali piumate"), ("pixie", "body/wings/pixie/wings_pixie", "Ali di fata"), ("monarch", "body/wings/monarch/wings_monarch", "Ali di farfalla"), ("dragonfly", "body/wings/dragonfly/wings_dragonfly", "Ali di libellula")],
 "coda": [("cat", "body/tails/tail_cat", "Coda di gatto"), ("wolf", "body/tails/tail_wolf", "Coda di lupo"), ("fluffy", "body/tails/tail_wolf_fluffy", "Coda soffice")],
}
FISSI = [("corpo", "body/body"), ("testa_m", "head/heads/human/heads_human_male"), ("testa_f", "head/heads/human/heads_human_female"),
         ("sopracciglia_thin", "head/eyebrows/eyebrows_thin"), ("sopracciglia_thick", "head/eyebrows/eyebrows_thick")]

def carica(rel):
    return json.load(open(os.path.join(GEN, "sheet_definitions", rel + ".json"), encoding="utf-8"))

def scegli_variante(vs):
    """Per ricolorare serve la variante 'bianca' (la base del tessuto); altrimenti la prima disponibile."""
    for c in ("white", "base_white"):
        if c in vs: return c
    return vs[0]

def file_pezzo(d, corpo, anim, var):
    """Elenco (file relativo a spritesheets, zPos) per un pezzo, un corpo e un'animazione."""
    out = []
    for k, v in sorted(d.items()):
        if not (k.startswith("layer_") and isinstance(v, dict)): continue
        base = v.get(corpo)
        if not base: continue
        nome = anim
        if var is not None:
            out.append((f"{base}{nome}/{var.replace(' ', '_')}.png", v.get("zPos", 0)))
        else:
            out.append((f"{base}{nome}.png", v.get("zPos", 0)))
    return out

catalogo = {"anim": ANIM, "corpi": CORPI, "slot": {}, "fissi": {}, "crediti": []}
da_copiare = set(); avvisi = []; crediti = {}
def registra(idp, rel, etic, fisso=False):
    d = carica(rel)
    vs = d.get("variants")
    var = scegli_variante(vs) if vs else None
    rec = d.get("recolors")
    mat = None
    if rec:
        mat = rec.get("material") or (rec.get("color_1") or {}).get("material")
    elif vs and var in ("white", "base_white"): mat = "cloth"
    voce = {"id": idp, "nome": etic, "materiale": mat, "corpi": {}}
    if vs: voce["_vs"] = vs; voce["_var"] = var
    if rec and rec.get("color_2"): voce["materiale2"] = rec["color_2"].get("material")
    for corpo in CORPI:
        voce["corpi"][corpo] = {}
        for anim in ANIM:
            if d.get("animations") and anim not in d["animations"]: continue
            lay = file_pezzo(d, corpo, anim, var)
            ok = []
            for f, z in lay:
                ok.append({"f": f, "z": z}); da_copiare.add(f)
            if ok: voce["corpi"][corpo][anim] = ok
    for c in d.get("credits", []):
        crediti[(c.get("file"), tuple(c.get("authors", [])))] = c
    return voce

for slot, elenco in SCELTA.items():
    catalogo["slot"][slot] = [registra(i, r, e) for i, r, e in elenco]
for i, r in FISSI:
    catalogo["fissi"][i] = registra(i, r, i, True)
catalogo["crediti"] = [{"file": k[0], "autori": list(k[1]), "licenze": c.get("licenses", []), "url": c.get("urls", []), "note": c.get("notes", "")} for k, c in crediti.items()]
# scarica dal clone (parziale) i soli file che servono, poi tieni quelli che esistono davvero
tutti = set(subprocess.run(["git", "-C", GEN, "ls-tree", "-r", "--name-only", "HEAD", "spritesheets"], capture_output=True, text=True).stdout.split("\n"))
lista = sorted(f for f in da_copiare if "spritesheets/" + f in tutti)
print("richiesti", len(da_copiare), "presenti nel repo", len(lista))
for i in range(0, len(lista), 400):
    pezzo = ["spritesheets/" + f for f in lista[i:i + 400]]
    subprocess.run(["git", "-C", GEN, "checkout", "HEAD", "--"] + pezzo, check=True)
esistono = {f for f in lista if os.path.exists(os.path.join(GEN, "spritesheets", f))}
from PIL import Image
RAMPE_BASE = {}
def base_rgb(m):
    meta = {"body": "body", "hair": "hair", "cloth": "cloth", "eye": "eye", "metal": "metal"}[m]
    mt = json.load(open(os.path.join(GEN, "palette_definitions", meta, "meta_" + meta + ".json")))
    r = json.load(open(os.path.join(GEN, "palette_definitions", meta, meta + "_ulpc.json")))[mt["base"]]
    return {tuple(int(c.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) for c in r}
def combacia(f, m):
    """Il file usa davvero la rampa di base del materiale? Altrimenti i colori sono già fatti a mano (varianti)."""
    im = Image.open(os.path.join(GEN, "spritesheets", f)).convert("RGBA"); b = base_rgb(m); tot = ok = 0
    for px in im.getdata():
        if px[3] == 255: tot += 1; ok += tuple(px[:3]) in b
    return tot and ok / tot > .9
def tutte_le_voci():
    return list(catalogo["fissi"].values()) + [x for voci in catalogo["slot"].values() for x in voci]
extra_file = set()
for v in tutte_le_voci():
    if not v.get("_vs"): continue
    campione = next((l["f"] for c in v["corpi"].values() for a in c.values() for l in a if l["f"] in esistono), None)
    if campione and v["materiale"] and combacia(campione, v["materiale"]): continue
    # varianti già colorate: le offro come scelte con nome, senza ricolorare
    v["materiale"] = None; v["varianti"] = [x.replace(" ", "_") for x in v["_vs"] if not x.startswith("base_")]
    for c in v["corpi"].values():
        for a in c.values():
            for l in a:
                if l["f"].endswith("/" + v["_var"].replace(" ", "_") + ".png"):
                    pre = l["f"][:-len(v["_var"].replace(" ", "_")) - 4]
                    l["f"] = pre + "{v}.png"
                    for x in v["varianti"]:
                        if "spritesheets/" + pre + x + ".png" in tutti: extra_file.add(pre + x + ".png")
for i in range(0, len(extra_file), 400):
    subprocess.run(["git", "-C", GEN, "checkout", "HEAD", "--"] + ["spritesheets/" + f for f in sorted(extra_file)[i:i + 400]], check=True)
esistono |= {f for f in extra_file if os.path.exists(os.path.join(GEN, "spritesheets", f))}
def pota(voce):
    for corpo in list(voce["corpi"]):
        for anim in list(voce["corpi"][corpo]):
            ok = [l for l in voce["corpi"][corpo][anim] if l["f"] in esistono or ("{v}" in l["f"] and any(l["f"].replace("{v}", x) in esistono for x in voce.get("varianti", [])))]
            if ok: voce["corpi"][corpo][anim] = ok
            else: del voce["corpi"][corpo][anim]
        if not voce["corpi"][corpo]: del voce["corpi"][corpo]
    return voce
catalogo["slot"] = {k: [v for v in map(pota, voci) if v["corpi"]] for k, voci in catalogo["slot"].items()}
catalogo["fissi"] = {k: pota(v) for k, v in catalogo["fissi"].items()}
usati = set()
for v in tutte_le_voci():
    for c in v["corpi"].values():
        for a in c.values():
            for l in a:
                if "{v}" in l["f"]: usati |= {l["f"].replace("{v}", x) for x in v.get("varianti", []) if l["f"].replace("{v}", x) in esistono}
                else: usati.add(l["f"])
shutil.rmtree(OUT, ignore_errors=True)
for f in usati:
    dst = os.path.join(OUT, f); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy(os.path.join(GEN, "spritesheets", f), dst)
# palette: rampe di base e rampe scelte per ogni materiale
PAL = os.path.join(GEN, "palette_definitions")
mat = {}
for m, cart, nomi in (("body", "body", "body_ulpc"), ("hair", "hair", "hair_ulpc"), ("cloth", "cloth", "cloth_ulpc"), ("eye", "eye", "eye_ulpc"), ("metal", "metal", "metal_ulpc")):
    meta = json.load(open(os.path.join(PAL, cart, "meta_" + cart + ".json")))
    rampe = json.load(open(os.path.join(PAL, cart, nomi + ".json")))
    mat[m] = {"base": meta["base"], "rampe": rampe}
for v in tutte_le_voci():
    v.pop("_vs", None); v.pop("_var", None)
catalogo["palette"] = mat
catalogo["crediti"] = [c for c in catalogo["crediti"] if any(u.startswith(c["file"]) or c["file"] in u for u in usati)]
# animali: file scaricati a mano da OpenGameArt (assets/pets), non dal generatore
catalogo["crediti"].append({"file": "pets/gatto, pets/cane", "autori": ["bluecarrot16"], "licenze": ["CC-BY 3.0", "CC-BY-SA 3.0", "GPL 3.0", "GPL 2.0", "OGA-BY 3.0"], "url": ["https://opengameart.org/content/lpc-cats-and-dogs"], "note": "[LPC] Cats and Dogs"})
json.dump(catalogo, open(os.path.join(OUT, "catalogo.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
tot = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(OUT) for f in fs)
print("pezzi:", sum(len(v) for v in catalogo["slot"].values()) + len(catalogo["fissi"]), "file:", len(usati), "peso MB:", round(tot / 1e6, 1))
for k, v in catalogo["slot"].items(): print(k, [x["id"] for x in v])

# CREDITI.md alla radice del repo: la licenza LPC richiede di nominare gli autori
righe = ["# Crediti", "", "Gli sprite dei personaggi vengono dal **Universal LPC Spritesheet Character Generator** e dalla comunità **Liberated Pixel Cup** (LPC):",
         "https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator", "",
         "I pezzi sono distribuiti con licenze CC-BY-SA 3.0, CC-BY 3.0/4.0, OGA-BY 3.0, GPL 3.0 e CC0. L'uso richiede di nominare gli autori, qui sotto. Le immagini composte nell'app restano sotto le stesse licenze (con condivisione allo stesso modo).",
         "Il codice dell'app è un'altra cosa e non è coperto da queste licenze.", "", "| Pezzo | Autori | Licenze | Fonti |", "|---|---|---|---|"]
for c in sorted(catalogo["crediti"], key=lambda x: x["file"]):
    righe.append("| `%s` | %s | %s | %s |" % (c["file"], ", ".join(c["autori"]), ", ".join(c["licenze"]), " ".join("<%s>" % u for u in c["url"])))
open(os.path.join(os.path.dirname(os.path.dirname(OUT.rstrip("/"))), "CREDITI.md"), "w", encoding="utf-8").write("\n".join(righe) + "\n")
print("CREDITI.md scritto")
