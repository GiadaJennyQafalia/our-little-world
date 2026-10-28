#!/usr/bin/env python3
"""Scrive PROMPT-MODULARE.md: i prompt per le stanze modulari di ogni dimora.
Una stanza modulare è fatta di due parti:
  - uno SFONDO vuoto (solo muro e pavimento) che si ripete in orizzontale senza giunture, così la stanza può
    essere larga quanto serve;
  - i MOBILI come pezzi singoli su fondo verde, che l'app appoggia sul pavimento in base alla larghezza.
Per ogni dimora: 3 fogli di sfondi (4 per foglio) e 6 fogli di mobili (2 stanze per foglio)."""

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

# Sfondi: cosa c'è su muro e pavimento (niente mobili). Gli esterni hanno cielo stellato SENZA luna (si ripete).
SFONDI = {
 "soggiorno": "LIVING ROOM: wall with a wooden wainscot on the lower part, wooden plank floor",
 "camera": "BEDROOM: soft plain wall with a thin decorative band, warm wooden floor",
 "cucina": "KITCHEN: wall with a band of ceramic tiles at counter height, stone tile floor",
 "bagno": "BATHROOM: wall covered with ceramic tiles on the lower half, checkered tile floor",
 "ingresso": "ENTRANCE HALL: wall with a stone or wooden wainscot, large floor tiles",
 "corridoio": "CORRIDOR: plain wall with a simple baseboard, long stone floor",
 "ripostiglio": "STORAGE ROOM: rough plain wall, worn wooden floor",
 "studio": "STUDY: wall with wooden panelling, wooden parquet floor",
 "lavanderia": "LAUNDRY ROOM: plain wall with a tiled band, stone floor",
 "cantina": "CELLAR: rough stone wall, packed earth and stone floor",
 "balcone": "BALCONY: a starry night sky (no moon) behind a balustrade that runs along the whole back edge, stone floor",
 "giardino": "GARDEN: a starry night sky (no moon) behind a low hedge that runs along the whole back edge, grass with a stone path",
}
FOGLI_SFONDI = [("soggiorno", "camera", "cucina", "bagno"), ("ingresso", "corridoio", "ripostiglio", "studio"), ("lavanderia", "cantina", "balcone", "giardino")]

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

def p_sfondi(stile, tipi):
    pos = ["Top left", "Top right", "Bottom left", "Bottom right"]
    return ("16-bit pixel art sheet of 4 EMPTY room backgrounds for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower), "
            "arranged in a 2x2 grid of square panels separated by wide gaps of flat pure chroma green (#00FF00). "
            "Every panel shows ONLY the back wall and the floor of a room seen straight from the front: the back wall fills the top two thirds, "
            "the floor fills the bottom third and is seen slightly from above, and the line where the wall meets the floor is at exactly the same height in all four panels. "
            "NO side walls, NO corners, NO ceiling, NO doors, NO windows, NO furniture, NO objects, NO lamps, NO characters: just the empty wall and floor surfaces with their materials, trims and baseboards. "
            "Each panel must TILE SEAMLESSLY HORIZONTALLY: its left edge continues exactly into its right edge, with no border, no frame, no vignette and no darker edges. "
            "Even soft ambient light, no bright spots. Materials in the style of " + stile + ". "
            + " ".join(f"{pos[i]}: {SFONDI[t]}." for i, t in enumerate(tipi))
            + " No text, no letters, no green inside the panels.")

def p_mobili(stile, a, b):
    lista = lambda t: ", ".join(f"{i + 1}) {m}" for i, m in enumerate(MOBILI[t]))
    return ("16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). "
            "Same front view, light and pixel scale as the attached room backgrounds: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. "
            "Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. "
            "Furniture in the style of " + stile + ". "
            f"Top row, left to right ({a.upper()}): {lista(a)}. "
            f"Bottom row, left to right ({b.upper()}): {lista(b)}. "
            "Clean and tidy. No characters, no text, no letters, no green inside the pieces.")

out = ["# Prompt delle stanze modulari", "",
 "## Come funziona", "",
 "Ogni stanza è fatta di **due parti**, come nei giochi tipo Fallout Shelter:",
 "1. **Lo sfondo**: solo muro e pavimento, vuoto, che si ripete in orizzontale. L'app lo allunga quanto serve, quindi una stanza può essere larga quanto vuoi.",
 "2. **I mobili**: pezzi singoli su fondo verde. L'app li appoggia sul pavimento e li distribuisce in base alla larghezza della stanza.", "",
 "**Per ogni dimora servono 9 immagini:** 3 fogli di sfondi (4 stanze per foglio) e 6 fogli di mobili (2 stanze per foglio, 6 pezzi per stanza).",
 "Cucina-soggiorno, terrazzo e \"altro\" non hanno immagini proprie: usano sfondi e mobili delle altre stanze.", "",
 "**Cosa allegare**",
 "- **Sfondi, foglio 1**: allega la sezione della dimora (per la Rocca `castello.png`, per il Palazzo `sezione.png`; per le altre dimore il foglio 1 di sfondi della Rocca, così il generatore capisce l'inquadratura).",
 "- **Sfondi, fogli 2 e 3**: allega il foglio 1 di sfondi della stessa dimora.",
 "- **Mobili**: allega il foglio 1 di sfondi della stessa dimora (stessa inquadratura e stessa scala).", "",
 "**Consigli**",
 "- Genera i fogli di una dimora **nella stessa chat** del generatore, uno dopo l'altro: lo stile resta coerente.",
 "- Se in uno sfondo si vede una giuntura ai bordi non importa: la sistemo io (rendo i bordi continui o uso lo specchio).",
 "- Se in un foglio di mobili un pezzo viene male o ne manca uno, va bene lo stesso: dimmelo e lo salto.",
 "- **Prima prova:** per la Rocca fai solo *Sfondi foglio 1* e *Mobili foglio 1 e 2* e mandameli. Se il risultato ci piace, facciamo il resto.", "", "---", ""]
for k, nome, lv, stile in DIMORE:
    out += [f"## {nome}", "", "Disponibile da subito." if lv <= 1 else f"Si sblocca al livello {lv}.", ""]
    for i, f in enumerate(FOGLI_SFONDI):
        out += [f"### Sfondi · Foglio {i + 1}: " + ", ".join(NOMI[t] for t in f), "", "```", p_sfondi(stile, f), "```", ""]
    for i, (a, b) in enumerate(FOGLI_MOBILI):
        out += [f"### Mobili · Foglio {i + 1}: {NOMI[a]} (sopra) e {NOMI[b]} (sotto)", "", "```", p_mobili(stile, a, b), "```", ""]
    out += ["---", ""]
open("PROMPT-MODULARE.md", "w", encoding="utf-8").write("\n".join(out))
print(sum(1 for x in out if x == "```") // 2, "prompt")
