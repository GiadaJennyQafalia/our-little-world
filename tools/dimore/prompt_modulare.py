#!/usr/bin/env python3
"""Scrive PROMPT-MODULARE.md: i prompt per le stanze modulari di ogni dimora.
Una stanza modulare (solo nella vista della dimora) è fatta di due parti:
  - uno SFONDO (muro + fregio + pavimento) che l'app costruisce dai CAMPIONI DI MATERIALE, così si ripete
    senza giunture e la stanza può essere larga quanto serve;
  - i MOBILI come pezzi singoli su fondo verde, che l'app appoggia sul pavimento in base alla larghezza.
Per ogni dimora: 3 fogli di materiali (pavimenti visti dall'alto, muri, fregi) e 6 fogli di mobili."""

DIMORE = [
 ("castello", "La Rocca di Pietranotte", 1, "dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle"),
 ("reggia", "Il Palazzo d'Argentaluna", 1, "gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace"),
 ("hobbit", "La Tana di Colleverde", 4, "curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill"),
 ("torre", "La Torre dell'Ametista", 6, "dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower"),
 ("rifugio", "Il Rifugio di Vettagelo", 8, "thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge"),
 ("albero", "Il Nido del Grande Faggio", 10, "living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse"),
 ("faro", "Il Faro di Scogliasecca", 12, "white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse"),
 ("abbazia", "L'Abbazia di Muschioscuro", 14, "old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey"),
 ("nave", "Il Galeone delle Nuvole", 16, "curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds"),
]

# Materiali: l'app costruisce da sola lo sfondo di ogni stanza (muro + fregio + pavimento) partendo da questi campioni.
# Il pavimento si genera visto DALL'ALTO (così non può avere prospettiva) e l'app lo schiaccia in verticale.
PAVIMENTI = ["light wooden planks", "dark wooden planks", "old worn wooden planks", "large stone slabs", "small square stone tiles",
             "black and white checkered tiles", "wooden parquet with a geometric pattern", "packed earth with small stones", "short grass"]
MURI = ["stone bricks", "smooth plaster", "plaster in a darker shade", "rough irregular stones", "carved wooden panelling",
        "square ceramic tiles", "vertical wooden boards", "large cut stone blocks", "a starry night sky with no moon (for outdoor rooms)"]
FREGI = ["a wooden wainscot with vertical boards and a top rail", "a simple wooden baseboard", "a thin decorative painted band",
         "a band of small decorated ceramic tiles", "a stone balustrade", "a low trimmed hedge"]
# Mobili: (pezzo, "p" se va appeso alla parete). 6 pezzi per stanza, nell'ordine in cui li ritaglio.
MOBILI = {
 "soggiorno": ["a sofa", "an armchair", "a fireplace", "a tall bookcase", "a low coffee table", "a tall window (wall piece)"],
 "camera": ["a double bed", "a wardrobe", "a nightstand with a candle", "a dresser", "a rug (seen from slightly above)", "a window with curtains (wall piece)"],
 "cucina": ["a stove with a pot", "a counter with a sink", "a tall cupboard", "a small table with two chairs", "a shelf with jars (wall piece)", "hanging pots and pans (wall piece)"],
 "bagno": ["a clawfoot bathtub", "a washbasin on a stand", "a toilet", "a towel rack with towels", "a mirror (wall piece)", "a small window (wall piece)"],
 "ingresso": ["a big double front door (wall piece, reaching the floor)", "a coat stand with cloaks", "a bench", "an umbrella and boot stand", "a doormat (seen from slightly above)", "a wall lamp (wall piece)"],
 "corridoio": ["a small console table with a vase", "a suit of armour or a statue", "a tall plant in a pot", "a long carpet runner (seen from slightly above)", "a wall lamp (wall piece)", "a hanging banner (wall piece)"],
 "ripostiglio": ["shelves full of folded linens and boxes", "a broom and a bucket", "a stack of crates", "a barrel", "a mop and cleaning things", "hanging tools on hooks (wall piece)"],
 "studio": ["a desk with books and a quill", "a desk chair", "a tall bookcase", "a globe on a stand", "a reading armchair", "a map (wall piece)"],
 "lavanderia": ["washing tubs", "a drying rack with clothes", "a laundry basket", "a big cauldron of hot water", "an ironing board", "a shelf with folded linen (wall piece)"],
 "cantina": ["a stack of wine barrels", "a wine rack with bottles", "a workbench with tools", "sacks of flour", "a pile of firewood", "a hanging lantern (wall piece)"],
 "balcone": ["a potted plant", "a small potted tree", "a small round table with two chairs", "a bench", "a lantern on a post", "a flower box (to put on the balustrade)"],
 "giardino": ["a small fountain", "a flower bed", "a garden bench", "a small tree", "a vegetable patch", "a lantern on a post"],
}
FOGLI_MOBILI = [("soggiorno", "camera"), ("cucina", "bagno"), ("ingresso", "corridoio"), ("ripostiglio", "studio"), ("lavanderia", "cantina"), ("balcone", "giardino")]
NOMI = {"soggiorno": "soggiorno", "camera": "camera", "cucina": "cucina", "bagno": "bagno", "ingresso": "ingresso", "corridoio": "corridoio",
        "ripostiglio": "sgabuzzino", "studio": "studio", "lavanderia": "lavanderia", "cantina": "cantina", "balcone": "balcone e terrazzo", "giardino": "giardino"}

GRIGLIA = "arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). "
ORDINE = "Order left to right, top to bottom: "

def p_pavimenti(stile):
    return ("16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, " + GRIGLIA +
            "Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, "
            "no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. "
            "Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. "
            "Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of " + stile + ". "
            + ORDINE + "; ".join(f"{i + 1}) {m}" for i, m in enumerate(PAVIMENTI)) + ". No text, no letters, no green inside the swatches.")

def p_muri(stile):
    return ("16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, " + GRIGLIA +
            "Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. "
            "Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. "
            "Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of " + stile + ". "
            + ORDINE + "; ".join(f"{i + 1}) {m}" for i, m in enumerate(MURI)) + ". No text, no letters, no green inside the swatches.")

def p_fregi(stile):
    return ("16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image "
            "and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, "
            "and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. "
            "Even flat lighting, no vignette, no darker ends. Materials in the style of " + stile + ". "
            "From top to bottom: " + "; ".join(f"{i + 1}) {m}" for i, m in enumerate(FREGI)) + ". No text, no letters, no green inside the strips.")

def p_mobili(stile, a, b):
    lista = lambda t: ", ".join(f"{i + 1}) {m}" for i, m in enumerate(MOBILI[t]))
    return ("16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). "
            "Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. "
            "Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. "
            "Furniture in the style of " + stile + ". "
            f"Top row, left to right ({a.upper()}): {lista(a)}. "
            f"Bottom row, left to right ({b.upper()}): {lista(b)}. "
            "Clean and tidy. No characters, no text, no letters, no green inside the pieces.")

out = ["# Prompt delle stanze modulari", "",
 "## Come funziona", "",
 "Nella vista della dimora ogni stanza è fatta di **due parti**, come nei giochi tipo Fallout Shelter:",
 "1. **Lo sfondo** (muro, fregio e pavimento): lo costruisco io da codice partendo dai **campioni di materiale**, quindi si ripete senza giunture e la stanza può essere larga quanto serve.",
 "2. **I mobili**: pezzi singoli su fondo verde, che l'app appoggia sul pavimento.", "",
 "Le stanze che si aprono toccandole restano come sono: questi prompt servono solo per la vista della dimora.", "",
 "**Per ogni dimora servono 9 immagini:** 3 fogli di materiali (pavimenti, muri, fregi) e 6 fogli di mobili (2 stanze per foglio, 6 pezzi per stanza).",
 "I pavimenti si generano visti **dall'alto**, così non possono avere prospettiva: sono io a schiacciarli per farli sembrare a terra.", "",
 "**Cosa allegare**",
 "- **Pavimenti**: allega la sezione della dimora (per la Rocca `castello.png`, per il Palazzo `sezione.png`), così colori e stile restano quelli.",
 "- **Muri e fregi**: allega il foglio pavimenti della stessa dimora.",
 "- **Mobili**: allega il foglio muri della stessa dimora (stessa luce e stessa scala).", "",
 "**Consigli**",
 "- Genera i fogli di una dimora **nella stessa chat** del generatore, uno dopo l'altro: lo stile resta coerente.",
 "- Se un campione ha una giuntura ai bordi non importa: la sistemo io.",
 "- Se in un foglio un pezzo viene male o ne manca uno, va bene lo stesso: dimmelo e lo salto.",
 "- **Rocca:** i muri dei due fogli di sfondi già fatti vanno bene e li riuso. Servono solo *Pavimenti* e *Mobili foglio 1 e 2*.", "", "---", ""]
for k, nome, lv, stile in DIMORE:
    out += [f"## {nome}", "", "Disponibile da subito." if lv <= 1 else f"Si sblocca al livello {lv}.", ""]
    out += ["### Materiali · Pavimenti (visti dall'alto)", "", "```", p_pavimenti(stile), "```", ""]
    out += ["### Materiali · Muri", "", "```", p_muri(stile), "```", ""]
    out += ["### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)", "", "```", p_fregi(stile), "```", ""]
    for i, (a, b) in enumerate(FOGLI_MOBILI):
        out += [f"### Mobili · Foglio {i + 1}: {NOMI[a]} (sopra) e {NOMI[b]} (sotto)", "", "```", p_mobili(stile, a, b), "```", ""]
    out += ["---", ""]
open("PROMPT-MODULARE.md", "w", encoding="utf-8").write("\n".join(out))
print(sum(1 for x in out if x == "```") // 2, "prompt")
