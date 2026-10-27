#!/usr/bin/env python3
"""Aggiunge le espressioni del volto (head/faces del generatore LPC) al catalogo esistente.
Uso: python3 tools/build_facce.py <clone del generatore LPC> assets/lpc
Ogni espressione è uno strato sopra la testa (z 101) che usa la rampa della pelle e quella degli occhi,
quindi si ricolora come la testa. Finiscono in catalogo["facce"][id] = { nome, scegli, corpi: {male,female: {walk:[{f,z}]}} }."""
import json, os, shutil, sys

GEN, OUT = sys.argv[1], sys.argv[2]
SS = os.path.join(GEN, "spritesheets")
CAT_F = os.path.join(OUT, "catalogo.json")
cat = json.load(open(CAT_F, encoding="utf-8"))

# id, cartella, nome italiano, se si può scegliere come espressione preferita
FACCE = [
    ("neutral", "neutral", "Serenità", True), ("happy", "happy", "Sorriso", True), ("happy2", "happy2", "Gioia", True),
    ("blush", "blush", "Timidezza", True), ("shock", "shock", "Stupore", True), ("sad", "sad", "Malinconia", True),
    ("anger", "anger", "Broncio", True), ("eyeroll", "eyeroll", "Noia", True), ("shame", "shame", "Imbarazzo", False),
    ("angry2", "angry2", "Furia", False), ("sad2", "sad2", "Disperazione", False), ("tears", "tears", "Lacrime", False),
    ("closed", "closed", "Occhi chiusi", False), ("look_l", "look_l", "Sguardo a sinistra", False), ("look_r", "look_r", "Sguardo a destra", False),
]
facce = {}
for idf, cart, nome, scegli in FACCE:
    corpi = {}
    for corpo in ("male", "female"):
        for d in (corpo, "global"):
            rel = f"head/faces/{d}/{cart}/walk.png"
            if os.path.exists(os.path.join(SS, rel)):
                dst = os.path.join(OUT, rel); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy(os.path.join(SS, rel), dst)
                corpi[corpo] = {"walk": [{"f": rel, "z": 101}]}
                break
    if len(corpi) == 2: facce[idf] = {"nome": nome, "scegli": scegli, "corpi": corpi}
    else: print("manca", idf)
cat["facce"] = facce

d = json.load(open(os.path.join(GEN, "sheet_definitions/head/faces/face_happy.json"), encoding="utf-8"))
noti = {(c["file"], tuple(c["autori"])) for c in cat["crediti"]}; nuovi = []
for c in d.get("credits", []):
    k = (c.get("file"), tuple(c.get("authors", [])))
    if k not in noti: nuovi.append({"file": k[0], "autori": list(k[1]), "licenze": c.get("licenses", []), "url": c.get("urls", []), "note": c.get("notes", "")})
cat["crediti"] += nuovi
json.dump(cat, open(CAT_F, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
md = os.path.join(os.path.dirname(os.path.dirname(OUT.rstrip("/"))), "CREDITI.md")
righe = open(md, encoding="utf-8").read().rstrip("\n").split("\n")
pos = max(i for i, r in enumerate(righe) if r.startswith("| `")) + 1
righe[pos:pos] = ["| `%s` | %s | %s | %s |" % (c["file"], ", ".join(c["autori"]), ", ".join(c["licenze"]), " ".join("<%s>" % u for u in c["url"])) for c in nuovi]
open(md, "w", encoding="utf-8").write("\n".join(righe) + "\n")
print("facce:", list(facce), "crediti nuovi:", len(nuovi))
