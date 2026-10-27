#!/usr/bin/env python3
"""Aggiunge al catalogo esistente i pezzi "a pagamento" della Bottega: armature, abiti speciali, acconciature rare, gioielli.
Uso: python3 tools/build_pezzi.py <clone del generatore LPC> assets/lpc
Ogni voce ha "gruppo" (il reparto della Bottega) e "prezzo"; anche negli slot gratuiti (busto, gambe, capelli, scarpe)
questi pezzi si comprano. La logica di lettura delle definizioni è la stessa di build_lpc.py."""
import json, os, shutil, subprocess, sys
from PIL import Image

GEN, OUT = sys.argv[1], sys.argv[2]
SS = os.path.join(GEN, "spritesheets")
CAT_F = os.path.join(OUT, "catalogo.json")
cat = json.load(open(CAT_F, encoding="utf-8"))
CORPI = ["male", "female"]

# slot -> [(id, definizione, nome, gruppo, prezzo)]
NUOVI = {
 "cappello": [
  ("armet", "headwear/helmets/helmets/hat_helmet_armet", "Elmo armet", "armatura", 150), ("close", "headwear/helmets/helmets/hat_helmet_close", "Elmo chiuso", "armatura", 150),
  ("horned", "headwear/helmets/helmets/hat_helmet_horned", "Elmo cornuto", "armatura", 150), ("viking", "headwear/helmets/helmets/hat_helmet_barbarian_viking", "Elmo vichingo", "armatura", 150),
  ("sugarloaf", "headwear/helmets/helmets/hat_helmet_sugarloaf", "Elmo a pan di zucchero", "armatura", 200), ("norman", "headwear/helmets/helmets/hat_helmet_norman", "Elmo normanno", "armatura", 120),
  ("morion", "headwear/helmets/helmets/hat_helmet_morion", "Morione", "armatura", 120), ("legion_h", "headwear/helmets/helmets/hat_helmet_legion", "Elmo legionario", "armatura", 120),
  ("pointed", "headwear/helmets/helmets/hat_helmet_pointed", "Elmo a punta", "armatura", 120), ("spangen", "headwear/helmets/helmets/hat_helmet_spangenhelm", "Spangenhelm", "armatura", 120)],
 "busto": [
  ("chainmail", "torso/torso_chainmail", "Cotta di maglia", "armatura", 150),
  ("apron", "torso/aprons/torso_aprons_apron_full", "Grembiule", "abito", 60), ("overalls", "torso/aprons/torso_aprons_overalls", "Salopette", "abito", 80),
  ("kimono", "torso/dresses/kimono/dress_kimono", "Kimono", "abito", 150), ("kimono_split", "torso/dresses/kimono/dress_kimono_split", "Kimono aperto", "abito", 150),
  ("blouse_long", "torso/shirts/torso_clothes_blouse_longsleeve", "Camicetta a maniche lunghe", "abito", 80), ("tunic_sara", "torso/shirts/torso_clothes_tunic_sara", "Tunica ricamata", "abito", 120),
  ("collared", "torso/jacket/torso_jacket_collared", "Cappotto col colletto", "abito", 150), ("vest_open", "torso/vest/torso_clothes_vest_open", "Gilet aperto", "abito", 60)],
 "braccia": [
  ("arms_armour", "arms/arms_armour", "Bracciali d'arme", "armatura", 120), ("bauldron", "arms/bauldron", "Spallaccio", "armatura", 120),
  ("shoulders_legion", "arms/shoulders/shoulders_legion", "Spallacci legionari", "armatura", 120)],
 "gambe": [
  ("legs_armour", "legs/legs_armour", "Gambali", "armatura", 150), ("legion_skirt", "legs/skirts/legs_skirts_legion", "Gonnellino legionario", "armatura", 80),
  ("belle", "legs/skirts/legs_skirt_belle", "Gonna da ballo", "abito", 150), ("overskirt", "legs/skirts/legs_skirt_overskirt", "Sopragonna", "abito", 80),
  ("widepants", "legs/pants/legs_widepants", "Pantaloni larghi", "abito", 60)],
 "scarpe": [
  ("feet_armour", "feet/feet_armour", "Schinieri", "armatura", 120), ("sandals", "feet/feet_sandals", "Sandali", "abito", 40),
  ("slippers", "feet/feet_slippers", "Pantofole", "abito", 40), ("ghillies", "feet/shoes/feet_shoes_ghillies", "Scarpe allacciate", "abito", 60)],
 "capelli": [
  ("afro", "hair/afro/hair_afro", "Afro", "acconciatura", 80), ("curly_long", "hair/curly/hair_curly_long", "Ricci lunghi", "acconciatura", 80),
  ("curls_xlong", "hair/curly/hair_curls_large_xlong", "Boccoli lunghissimi", "acconciatura", 120), ("dreads", "hair/afro/hair_dreadlocks_long", "Dreadlocks", "acconciatura", 100),
  ("pigtails", "hair/pigtails/hair_pigtails", "Codini", "acconciatura", 80), ("bunches", "hair/pigtails/hair_bunches", "Codini alti", "acconciatura", 80),
  ("liberty", "hair/spiky/hair_spiked_liberty", "Punte ribelli", "acconciatura", 100), ("longhawk", "hair/bald/hair_longhawk", "Cresta", "acconciatura", 100),
  ("relm_xlong", "hair/braids/hair_relm_xlong", "Lunghissimi con frangia", "acconciatura", 120), ("sara", "hair/xlong/hair_sara", "Onde da sirena", "acconciatura", 120),
  ("half_up", "hair/braids/hair_half_up", "Mezza coda", "acconciatura", 80), ("bangs_bun", "hair/braids/hair_bangs_bun", "Chignon con frangia", "acconciatura", 80),
  ("long_band", "hair/xlong/hair_long_band", "Lunghi con fascia", "acconciatura", 100)],
 "collo": [
  ("gem_pearl", "headwear/neck/charms/neck_gem_pearl", "Perla", "gioiello", 80), ("gem_emerald", "headwear/neck/charms/neck_gem_emerald", "Gemma a smeraldo", "gioiello", 100),
  ("gem_princess", "headwear/neck/charms/neck_gem_princess", "Gemma principessa", "gioiello", 100), ("chain", "headwear/neck/neck_necklace_chain", "Catenina", "gioiello", 60),
  ("beaded", "headwear/neck/neck_necklace_beaded_large", "Collana di perline", "gioiello", 60), ("amulet_spider", "headwear/neck/charms/neck_amulet_spider", "Amuleto del ragno", "gioiello", 100)],
 "accessorio": [
  ("earrings_pear", "headwear/accessories/earrings/facial_earrings_pear", "Orecchini a goccia", "gioiello", 80), ("earrings_princess", "headwear/accessories/earrings/facial_earrings_princess", "Orecchini principessa", "gioiello", 100),
  ("monocle", "headwear/accessories/monocle/facial_monocle_right", "Monocolo", "gioiello", 80)],
}

carica = lambda rel: json.load(open(os.path.join(GEN, "sheet_definitions", rel + ".json"), encoding="utf-8"))
def scegli_variante(vs):
    for c in ("white", "base_white"):
        if c in vs: return c
    return vs[0]
def file_pezzo(d, corpo, var):
    out = []
    for k, v in sorted(d.items()):
        if not (k.startswith("layer_") and isinstance(v, dict)) or v.get("custom_animation"): continue
        base = v.get(corpo)
        if not base: continue
        out.append((f"{base}walk/{var.replace(' ', '_')}.png" if var is not None else f"{base}walk.png", v.get("zPos", 0)))
    return out
tutti = set(subprocess.run(["git", "-C", GEN, "ls-tree", "-r", "--name-only", "HEAD", "spritesheets"], capture_output=True, text=True).stdout.split("\n"))
PAL = cat["palette"]
def base_rgb(m):
    return {tuple(int(c.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)) for c in PAL[m]["rampe"][PAL[m]["base"]]}
def scarica(files):
    dirs = sorted({os.path.dirname("spritesheets/" + f) for f in files})
    for i in range(0, len(dirs), 200): subprocess.run(["git", "-C", GEN, "sparse-checkout", "add"] + dirs[i:i + 200], check=True)

voci_nuove, crediti, serve = {}, {}, set()
for slot, elenco in NUOVI.items():
    for idp, rel, nome, gruppo, prezzo in elenco:
        d = carica(rel); vs = d.get("variants"); var = scegli_variante(vs) if vs else None
        rec = d.get("recolors"); mat = None
        if rec: mat = rec.get("material") or (rec.get("color_1") or {}).get("material")
        elif vs and var in ("white", "base_white"): mat = "cloth"
        if mat and mat not in PAL: mat = None
        v = {"id": idp, "nome": nome, "materiale": mat, "gruppo": gruppo, "prezzo": prezzo, "corpi": {}, "_vs": vs, "_var": var}
        for corpo in CORPI:
            if d.get("animations") and "walk" not in d["animations"]: continue
            lay = file_pezzo(d, corpo, var)
            if lay: v["corpi"][corpo] = {"walk": [{"f": f, "z": z} for f, z in lay]}
            for f, _ in lay: serve.add(f)
        for c in d.get("credits", []): crediti[(c.get("file"), tuple(c.get("authors", [])))] = c
        voci_nuove.setdefault(slot, []).append(v)
scarica([f for f in serve if "spritesheets/" + f in tutti])
esiste = lambda f: os.path.exists(os.path.join(SS, f))
def combacia(f, m):
    im = Image.open(os.path.join(SS, f)).convert("RGBA"); b = base_rgb(m); tot = ok = 0
    for px in im.getdata():
        if px[3] == 255: tot += 1; ok += tuple(px[:3]) in b
    return tot and ok / tot > .9
extra = set()
for vv in voci_nuove.values():
    for v in vv:
        if not v["_vs"]: continue
        campione = next((l["f"] for c in v["corpi"].values() for l in c["walk"] if esiste(l["f"])), None)
        if campione and v["materiale"] and combacia(campione, v["materiale"]): continue
        v["materiale"] = None; v["varianti"] = [x.replace(" ", "_") for x in v["_vs"] if not x.startswith("base_")]
        for c in v["corpi"].values():
            for l in c["walk"]:
                suf = "/" + v["_var"].replace(" ", "_") + ".png"
                if l["f"].endswith(suf):
                    pre = l["f"][:-len(suf) + 1]; l["f"] = pre + "{v}.png"
                    extra |= {pre + x + ".png" for x in v["varianti"] if "spritesheets/" + pre + x + ".png" in tutti}
scarica(extra)
usati = set(); aggiunte = {}
for slot, vv in voci_nuove.items():
    for v in vv:
        for corpo in list(v["corpi"]):
            ok = []
            for l in v["corpi"][corpo]["walk"]:
                if "{v}" in l["f"]:
                    fs = [l["f"].replace("{v}", x) for x in v.get("varianti", []) if esiste(l["f"].replace("{v}", x))]
                    if fs: ok.append(l); usati |= set(fs)
                elif esiste(l["f"]): ok.append(l); usati.add(l["f"])
            if ok: v["corpi"][corpo]["walk"] = ok
            else: del v["corpi"][corpo]
        if "varianti" in v:  # tieni solo le varianti presenti per tutti gli strati
            v["varianti"] = [x for x in v["varianti"] if all(esiste(l["f"].replace("{v}", x)) for c in v["corpi"].values() for l in c["walk"] if "{v}" in l["f"])]
        v.pop("_vs", None); v.pop("_var", None)
        if v["corpi"]: aggiunte.setdefault(slot, []).append(v)
        else: print("scartato", slot, v["id"])
for f in usati:
    dst = os.path.join(OUT, f); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy(os.path.join(SS, f), dst)
for slot, vv in aggiunte.items():
    ids = {v["id"] for v in vv}
    cat["slot"][slot] = [x for x in cat["slot"][slot] if x["id"] not in ids] + vv
noti = {(c["file"], tuple(c["autori"])) for c in cat["crediti"]}
nuovi_cr = [{"file": k[0], "autori": list(k[1]), "licenze": c.get("licenses", []), "url": c.get("urls", []), "note": c.get("notes", "")}
            for k, c in crediti.items() if k not in noti and any(k[0] and (u.startswith(k[0]) or k[0] in u) for u in usati)]
cat["crediti"] += nuovi_cr
json.dump(cat, open(CAT_F, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
md = os.path.join(os.path.dirname(os.path.dirname(OUT.rstrip("/"))), "CREDITI.md")
righe = open(md, encoding="utf-8").read().rstrip("\n").split("\n")
pos = max(i for i, r in enumerate(righe) if r.startswith("| `")) + 1
righe[pos:pos] = ["| `%s` | %s | %s | %s |" % (c["file"], ", ".join(c["autori"]), ", ".join(c["licenze"]), " ".join("<%s>" % u for u in c["url"])) for c in nuovi_cr]
open(md, "w", encoding="utf-8").write("\n".join(righe) + "\n")
for slot, vv in aggiunte.items(): print(slot, [(v["id"], len(v.get("varianti", [])) or v["materiale"]) for v in vv])
print("file:", len(usati), "crediti nuovi:", len(nuovi_cr))
