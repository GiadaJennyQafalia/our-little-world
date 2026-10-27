#!/usr/bin/env python3
"""Aggiunge armi e scudi nuovi al catalogo esistente (assets/lpc/catalogo.json) senza ricostruire il resto.
Uso: python3 tools/build_armi.py <clone del generatore LPC> assets/lpc
Il clone (parziale) si prepara come per build_lpc.py; i file servono già scaricati in <clone>/spritesheets.

Note sui formati:
- alcune armi (archi, katana, scimitarra, tridente, lancia lunga) esistono solo con celle 128×128 ("walk_128"):
  il personaggio sta nel quadrato centrale 64×64 (offset 32,32), quindi ritaglio quello e tengo le prime 9 colonne.
- lo scudo a goccia è fatto di 4 strati: legno, vernice, stemma, bordo. La vernice si ricolora con il colore scelto,
  lo stemma è "cotto" in oro così resta visibile sopra la vernice."""
import json, os, sys
from PIL import Image

GEN, OUT = sys.argv[1], sys.argv[2]
SS = os.path.join(GEN, "spritesheets")
CAT_F = os.path.join(OUT, "catalogo.json")
cat = json.load(open(CAT_F, encoding="utf-8"))
METALLI = ["brass", "bronze", "copper", "iron", "silver", "steel", "gold", "ceramic"]
LEGNI = ["light", "medium", "dark", "red"]

def salva(img, rel):
    dst = os.path.join(OUT, rel); os.makedirs(os.path.dirname(dst), exist_ok=True); img.save(dst, optimize=True)

def copia(rel_src, rel_dst=None, grande=False):
    """Copia un foglio di camminata; se grande (celle 128) lo riporta a celle 64."""
    im = Image.open(os.path.join(SS, rel_src)).convert("RGBA")
    if grande:
        out = Image.new("RGBA", (9 * 64, 4 * 64))
        for r in range(4):
            for c in range(9):
                out.alpha_composite(im.crop((c * 128 + 32, r * 128 + 32, c * 128 + 96, r * 128 + 96)), (c * 64, r * 64))
        im = out
    assert im.size == (576, 256), (rel_src, im.size)
    salva(im, rel_dst or rel_src)

def varianti_presenti(cartelle, vs):
    return [v for v in vs if all(os.path.exists(os.path.join(SS, c.format(v=v))) for c in cartelle)]

def voce(idp, nome, strati, varianti=None, materiale=None, prezzo=None, grande=False):
    """strati = [(percorso con {v} opzionale, z)] uguali per i due corpi, oppure dict corpo -> strati."""
    per_corpo = strati if isinstance(strati, dict) else {"male": strati, "female": strati}
    for corpo, ls in per_corpo.items():
        for f, z in ls:
            if "{v}" in f:
                for v in varianti: copia(f.format(v=v), None, grande)
            else: copia(f, None, grande)
    v = {"id": idp, "nome": nome, "materiale": materiale,
         "corpi": {c: {"walk": [{"f": f, "z": z} for f, z in ls]} for c, ls in per_corpo.items()}}
    if varianti: v["varianti"] = varianti
    if prezzo: v["prezzo"] = prezzo
    return v

nuove_armi = []
# --- Tiro
for idp, cart, nome, prezzo in (("bow", "normal", "Arco", 60), ("recurve", "recurve", "Arco ricurvo", 120), ("greatbow", "great", "Arco lungo", 120)):
    base = f"weapon/ranged/bow/{cart}/walk/"
    vs = varianti_presenti([base + "background/{v}.png", base + "foreground/{v}.png"], LEGNI + METALLI)
    nuove_armi.append(voce(idp, nome, [(base + "background/{v}.png", -1), (base + "foreground/{v}.png", 141)], vs, prezzo=prezzo, grande=True))
nuove_armi.append(voce("crossbow", "Balestra", [("weapon/ranged/crossbow/background/walk/crossbow.png", -1), ("weapon/ranged/crossbow/foreground/walk/crossbow.png", 140)], prezzo=120))
nuove_armi.append(voce("slingshot", "Fionda", [("weapon/ranged/slingshot/background/walk/slingshot.png", 9), ("weapon/ranged/slingshot/foreground/walk/slingshot.png", 140)], prezzo=60))
# --- Lame
nuove_armi.append(voce("katana", "Katana", [("weapon/sword/katana/walk/behind/katana.png", 9), ("weapon/sword/katana/walk/katana.png", 140)], prezzo=200, grande=True))
nuove_armi.append(voce("saber", "Sciabola", [("weapon/sword/saber/universal_behind/walk/saber.png", 9), ("weapon/sword/saber/walk/saber.png", 140)], prezzo=60))
nuove_armi.append(voce("scimitar", "Scimitarra", [("weapon/sword/scimitar/walk/behind/scimitar.png", 9), ("weapon/sword/scimitar/walk/scimitar.png", 140)], prezzo=120, grande=True))
nuove_armi.append(voce("glowsword", "Spada luminosa", [("weapon/sword/glowsword/universal_behind/walk/{v}.png", 9), ("weapon/sword/glowsword/walk/{v}.png", 140)], ["blue", "red"], prezzo=200))
# --- Pesanti e aste
nuove_armi.append(voce("waraxe", "Ascia da guerra", [("weapon/blunt/waraxe/behind/walk/waraxe.png", 9), ("weapon/blunt/waraxe/walk/waraxe.png", 140)], prezzo=120))
nuove_armi.append(voce("flail", "Flagello", [("weapon/blunt/flail/behind/walk/flail.png", 9), ("weapon/blunt/flail/walk/flail.png", 140)], prezzo=60))
nuove_armi.append(voce("halberd", "Alabarda", [("weapon/polearm/halberd/behind/walk/halberd.png", 8), ("weapon/polearm/halberd/walk/halberd.png", 140)], prezzo=120))
# Tridente e lancia lunga esistono solo a celle 128 e sporgono molto fuori dal quadrato 64: ritagliati si spezzano, quindi restano fuori.

# --- Scudi
nuovi_scudi = []
rv = [v for v in ("brown", "black", "green", "yellow") if os.path.exists(os.path.join(SS, f"shield/round/walk/{v}.png"))]
nuovi_scudi.append(voce("round", "Scudo tondo", [("shield/round/walk/{v}.png", 110)], rv, prezzo=60))
kite_vs = sorted(f[:-4] for f in os.listdir(os.path.join(SS, "shield/kite/male/walk")) if os.path.exists(os.path.join(SS, "shield/kite/female/walk", f)))
nuovi_scudi.append(voce("kite", "Scudo a mandorla", {"male": [("shield/kite/male/walk/{v}.png", 110)], "female": [("shield/kite/female/walk/{v}.png", 110)]}, kite_vs, prezzo=120))
nuovi_scudi.append(voce("spartan", "Scudo spartano", [("shield/spartan/bg/walk/spartan.png", 2), ("shield/spartan/fg/walk/spartan.png", 110)], prezzo=60))

# Scudo a goccia: lo stemma in oro (rampa "yellow" della stoffa) sopra la vernice ricolorabile
P = cat["palette"]["cloth"]; h2 = lambda h: tuple(int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
mappa = dict(zip(map(h2, P["rampe"][P["base"]]), map(h2, P["rampe"]["yellow"])))
def oro(rel):
    im = Image.open(os.path.join(SS, rel)).convert("RGBA"); px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a and (r, g, b) in mappa: px[x, y] = (*mappa[(r, g, b)], a)
    salva(im, rel.replace("/walk.png", "/walk_oro.png"))
H = "shield/heater/revised/"
for parte in ("wood", "paint", "trim"):
    for lato in ("bg", "fg"): copia(f"{H}{parte}/{lato}/walk.png")
STEMMI = [("", "Scudo a goccia"), ("cross", "Scudo con croce"), ("saltire", "Scudo con croce di sant'Andrea"),
          ("quarterly", "Scudo inquartato"), ("chevron", "Scudo con scaglione"), ("bend", "Scudo con banda"), ("paly", "Scudo palato")]
for st, nome in STEMMI:
    strati = [(H + "wood/bg/walk.png", 2), (H + "paint/bg/walk.png", 3), (H + "trim/bg/walk.png", 6),
              (H + "wood/fg/walk.png", 110), (H + "paint/fg/walk.png", 111), (H + "trim/fg/walk.png", 115)]
    if st:
        for lato in ("bg", "fg"): oro(f"{H}pattern/{st}/{lato}/walk.png")
        strati += [(f"{H}pattern/{st}/bg/walk_oro.png", 4), (f"{H}pattern/{st}/fg/walk_oro.png", 112)]
    nuovi_scudi.append({"id": "heater" + ("_" + st if st else ""), "nome": nome, "materiale": "cloth", "prezzo": 120,
                        "corpi": {c: {"walk": [{"f": f, "z": z} for f, z in strati]} for c in ("male", "female")}})

def aggiungi(slot, voci):
    gia = {v["id"] for v in cat["slot"][slot]}
    cat["slot"][slot] = [v for v in cat["slot"][slot] if v["id"] not in {x["id"] for x in voci}] + voci
    return [v["id"] for v in voci if v["id"] not in gia]
print("armi nuove:", aggiungi("arma", nuove_armi))
print("scudi nuovi:", aggiungi("scudo", nuovi_scudi))

# Crediti dalle definizioni del generatore
DEF = ["weapons/ranged/bow/weapon_ranged_bow_normal", "weapons/ranged/bow/weapon_ranged_bow_recurve", "weapons/ranged/bow/weapon_ranged_bow_great",
       "weapons/ranged/weapon_ranged_crossbow", "weapons/ranged/weapon_ranged_slingshot", "weapons/sword/weapon_sword_katana", "weapons/sword/weapon_sword_saber",
       "weapons/sword/weapon_sword_scimitar", "weapons/sword/weapon_sword_glowsword", "weapons/blunt/weapon_blunt_waraxe", "weapons/blunt/weapon_blunt_flail",
       "weapons/polearm/weapon_polearm_halberd",
       "weapons/shields/shield_round", "weapons/shields/shield_kite", "weapons/shields/shield_spartan", "weapons/shields/heater/shield_heater_revised_wood",
       "weapons/shields/heater/shield_heater_revised_paint", "weapons/shields/heater/shield_heater_revised_trim"] + \
      [f"weapons/shields/heater/revised_pattern/shield_heater_revised_pattern_{s}" for s, _ in STEMMI if s]
noti = {(c["file"], tuple(c["autori"])) for c in cat["crediti"]}
nuovi_cr = []
for d in DEF:
    for c in json.load(open(os.path.join(GEN, "sheet_definitions", d + ".json"), encoding="utf-8")).get("credits", []):
        k = (c.get("file"), tuple(c.get("authors", [])))
        if k in noti: continue
        noti.add(k); nuovi_cr.append({"file": k[0], "autori": list(k[1]), "licenze": c.get("licenses", []), "url": c.get("urls", []), "note": c.get("notes", "")})
cat["crediti"] += nuovi_cr
json.dump(cat, open(CAT_F, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
md = os.path.join(os.path.dirname(os.path.dirname(OUT.rstrip("/"))), "CREDITI.md")
righe = open(md, encoding="utf-8").read().rstrip("\n").split("\n")
pos = max(i for i, r in enumerate(righe) if r.startswith("| `")) + 1
righe[pos:pos] = ["| `%s` | %s | %s | %s |" % (c["file"], ", ".join(c["autori"]), ", ".join(c["licenze"]), " ".join("<%s>" % u for u in c["url"])) for c in nuovi_cr]
open(md, "w", encoding="utf-8").write("\n".join(righe) + "\n")
print("crediti aggiunti:", len(nuovi_cr))
