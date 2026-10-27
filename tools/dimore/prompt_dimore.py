"""Scrive PROMPT-DIMORE.md: i prompt per la sezione e le 8 stanze di ogni dimora.
Ogni prompt va usato allegando come modello l'immagine corrispondente del castello (stessa disposizione e inquadratura)."""
CASTELLO = ("castello", "La Rocca di Pietranotte", 1, "a dark stone medieval castle", "dark grey stone walls with battlements, round towers, torches and candle light", {})
D = [
 ("reggia", "Il Palazzo d'Argentaluna", 1, "a white marble fairy-tale palace", "gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard",
  {"bagno": "a white marble bathroom with a gilded clawfoot tub, a marble washbasin with gold taps, a tall gilded mirror, blue velvet curtains",
   "camera": "a royal bedroom with a canopy bed with blue silk curtains, a white and gold wardrobe, a vanity table with a mirror, a thick blue rug",
   "sgabuzzino": "a tidy palace storage room with white cabinets with gold handles, shelves of folded linens and glass jars, a silver bucket and a broom",
   "corridoio": "a long palace gallery corridor with a white marble floor, a narrow blue and gold carpet runner, gilded wall sconces, a small console table with a flower vase",
   "cucina": "a bright palace kitchen with a white tiled stove with copper pots, marble counters, a cabinet with fine porcelain, a small round table set with silverware",
   "ingresso": "a grand entrance hall with a double door with gold details, a white marble floor with a round blue rug, a gilded coat stand, a bench with cushions",
   "soggiorno": "an elegant throne-room style living room with a white marble fireplace, a blue velvet sofa, gilded armchairs, a harp in the corner, tall windows",
   "balcone": "a white marble balcony with a carved balustrade, potted white roses and small lemon trees, a wrought iron bench, a starry night sky with a crescent moon"}),
 ("hobbit", "La Tana di Colleverde", 4, "a cozy burrow dug inside a grassy hill", "round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones",
  {"bagno": "a cozy burrow bathroom with round earthen walls, a wooden barrel bathtub, a clay washbasin on a wooden stand, a round mirror, dried herbs hanging",
   "camera": "a burrow bedroom with a low wooden bed with a patchwork quilt, a round window, a small wooden dresser, a braided rug, a lantern on a nightstand",
   "sgabuzzino": "a burrow pantry with curved wooden shelves full of jars of jam, cheese wheels, sacks of flour, strings of onions and garlic, a broom and a basket",
   "corridoio": "a curved burrow tunnel corridor with wooden beams, a round wooden door at the end, a long woven rug, little lanterns on the walls",
   "cucina": "a burrow kitchen with a stone hearth and a hanging cauldron, a big wooden table with mismatched chairs, shelves with clay pots, a basket of vegetables",
   "ingresso": "a burrow entrance with a big round green wooden door, a coat rack with cloaks and walking sticks, a doormat, a bench with boots",
   "soggiorno": "a burrow living room with a round fireplace, two squashy armchairs, a pipe stand, bookshelves carved into the earth, a round rug",
   "balcone": "a small grassy terrace on the hill with a low wooden fence, flower pots, a little bench, fireflies, a starry night sky with a crescent moon"}),
 ("torre", "La Torre dell'Ametista", 6, "a tall wizard tower of dark stone with purple crystals", "dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames",
  {"bagno": "a wizard tower bathroom with curved stone walls, a copper tub with purple steam, a washbasin carved from a crystal geode, glowing amethyst stones",
   "camera": "a wizard bedroom with a bed with a starry purple blanket, a desk with an open spellbook and candles, a telescope by the arched window, stacks of books",
   "sgabuzzino": "a wizard storage room with shelves of potion bottles, jars with strange ingredients, scrolls in cubbyholes, a flying broom leaning on the wall",
   "corridoio": "a narrow curved tower corridor with stone steps, glowing rune symbols on the walls, a long purple rug, floating candles",
   "cucina": "a wizard kitchen with a bubbling cauldron on a stove, shelves of herbs and potion bottles, a wooden table with a mortar and pestle, hanging dried plants",
   "ingresso": "a tower entrance with a heavy arched wooden door with iron runes, a coat rack with a wizard hat and cloak, a magic circle drawn on the floor",
   "soggiorno": "a wizard study used as a living room with a fireplace with purple flames, a velvet armchair, a globe, bookshelves up to the ceiling, a crystal ball on a stand",
   "balcone": "a round stone balcony at the top of the tower with a crenellated parapet, a telescope, floating purple crystals, a starry night sky with a crescent moon"}),
 ("rifugio", "Il Rifugio di Vettagelo", 8, "a mountain refuge made of logs and stone on a snowy peak", "thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks",
  {"bagno": "a mountain lodge bathroom with log walls, a wooden tub, an enamel washbasin, thick wool towels, a small window with snow outside",
   "camera": "a mountain lodge bedroom with a log bed with fur blankets and a red check quilt, a wooden chest, antlers on the wall, a small snowy window",
   "sgabuzzino": "a mountain lodge storage room with stacked firewood, skis and snowshoes, wool blankets on shelves, lanterns, a broom and a bucket",
   "corridoio": "a narrow log corridor with wooden plank floor, a long red woven rug, coat hooks with scarves, small lanterns, a wooden door at the end",
   "cucina": "a mountain kitchen with a cast-iron wood stove, a pot of soup, a heavy wooden table with benches, hanging cured meats and herbs, cheese on a board",
   "ingresso": "a mountain lodge entrance with a heavy wooden door, a bench with snow boots, coats and scarves on hooks, a snowy doormat, a lantern",
   "soggiorno": "a mountain lodge living room with a big stone fireplace, a sofa with fur throws, a rocking chair, a bear skin rug, mugs of hot chocolate",
   "balcone": "a wooden balcony with a log railing covered in snow, potted pines, a bench with a blanket, snowy mountain peaks and a starry night sky with a crescent moon"}),
 ("albero", "Il Nido del Grande Faggio", 10, "an elven house built in the branches of a giant ancient tree", "a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors",
  {"bagno": "an elven treehouse bathroom with curved bark walls, a tub carved in a tree stump, a washbasin made of a big shell, hanging vines, glowing mushrooms",
   "camera": "an elven treehouse bedroom with a bed woven from branches with a leaf blanket, a round window with leaves outside, hanging lanterns, a carved wooden chest",
   "sgabuzzino": "a treehouse storage room with woven baskets of nuts and berries, clay jars, coiled ropes, a bow and quiver, a broom made of twigs",
   "corridoio": "a narrow treehouse passage along a thick branch with a wooden plank floor, a woven leaf rug, rope railings, small lanterns",
   "cucina": "a treehouse kitchen with a small clay oven, a table carved from a stump, baskets of fruit and mushrooms, hanging herbs, wooden bowls",
   "ingresso": "a treehouse entrance with a round wooden door set in the trunk, a ladder, cloaks on branch hooks, a moss doormat",
   "soggiorno": "an elven treehouse living room with a small stone hearth, cushions on a woven rug, a harp, shelves in the hollow of the trunk, glowing fireflies",
   "balcone": "a wooden platform on a big branch with a rope railing, hanging lanterns, potted ferns, leaves all around, a starry night sky with a crescent moon"}),
 ("faro", "Il Faro di Scogliasecca", 12, "a lighthouse on a rocky island in the sea", "a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls",
  {"bagno": "a lighthouse keeper bathroom with white painted planks, a tin tub, a porthole mirror, blue and white towels, seashells on a shelf",
   "camera": "a lighthouse bedroom with a wooden bed with a navy blanket, a round porthole window with the sea, a ship in a bottle, a sea chest",
   "sgabuzzino": "a lighthouse storage room with coiled ropes, oil cans for the lamp, fishing nets, lanterns, life rings, a broom and a bucket",
   "corridoio": "a narrow curved lighthouse corridor with a spiral stair going up, white painted stone walls, a striped rug, brass lamps",
   "cucina": "a lighthouse kitchen with a small iron stove, a pot of fish soup, a wooden table, blue and white plates on a rack, a fishing net on the wall",
   "ingresso": "a lighthouse entrance with a heavy blue wooden door, oilskin coats and boots, an anchor by the wall, a striped doormat",
   "soggiorno": "a lighthouse keeper living room with a small fireplace, an armchair with a blanket, maps and a ship's wheel on the wall, a telescope",
   "balcone": "the round gallery around the lighthouse lamp with an iron railing, the big lamp glowing behind, the sea and a starry night sky with a crescent moon"}),
 ("abbazia", "L'Abbazia di Muschioscuro", 14, "an old stone abbey hidden in a mossy forest", "grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around",
  {"bagno": "an abbey bathroom with stone walls and moss, a stone basin fed by a little fountain, a wooden tub, candles in niches, a small stained glass window",
   "camera": "a monk's cell bedroom with a simple wooden bed with a wool blanket, a desk with a candle and an illuminated manuscript, a stone arched window",
   "sgabuzzino": "an abbey cellar with wine barrels, jars of honey, bundles of herbs, candles in boxes, a broom and a bucket",
   "corridoio": "a cloister corridor with stone arches, a long rug, candles on iron stands, a wooden door at the end",
   "cucina": "an abbey kitchen with a big stone hearth, a long wooden table, loaves of bread, a bubbling pot, hanging herbs and copper pans",
   "ingresso": "an abbey entrance with a huge arched oak door with iron studs, a stone holy water font, a bench, a hanging bell rope",
   "soggiorno": "an abbey library used as a living room with tall bookshelves, a reading lectern, a fireplace, wooden armchairs, a big stained glass window",
   "balcone": "a stone loggia with arches overlooking the cloister garden with a fountain, potted herbs, ivy, a starry night sky with a crescent moon"}),
 ("nave", "Il Galeone delle Nuvole", 16, "a flying wooden galleon sailing above the clouds", "a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around",
  {"bagno": "a ship cabin bathroom with curved wooden walls, a brass tub, a porthole with clouds outside, a washbasin on a brass stand, rope details",
   "camera": "a captain's cabin bedroom with a wooden bunk bed with a red blanket, a big porthole with clouds, a sea chest, a hanging lantern, maps on the wall",
   "sgabuzzino": "a ship hold storage room with barrels and crates, coiled ropes, spare sails, lanterns, a broom and a mop bucket",
   "corridoio": "a narrow ship corridor below deck with curved wooden walls, a plank floor, a narrow rug, hanging lanterns, a hatch ladder",
   "cucina": "a ship galley kitchen with a small iron stove, pots hanging from hooks, barrels of supplies, a fixed wooden table, a porthole",
   "ingresso": "a ship entrance with a wooden hatch door, coats and a captain's hat on hooks, a ship's bell, a coiled rope, a doormat",
   "soggiorno": "a captain's lounge with a big ship's wheel, a leather armchair, a globe and brass instruments, a map table, a wide window with clouds",
   "balcone": "the open deck of the flying ship with a wooden railing, ropes and sails, a brass telescope, clouds below and a starry night sky with a crescent moon"}),
]
# Le 6 stanze in più (open space, studio, lavanderia, terrazzo, giardino, cantina): stesso stile della dimora.
EXTRA = [
 ("cucina_soggiorno", "Cucina-soggiorno", "open space kitchen and living room", "a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle"),
 ("studio", "Studio", "study", "a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe"),
 ("lavanderia", "Lavanderia", "laundry room", "a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board"),
 ("terrazzo", "Terrazzo", "terrace", "a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon"),
 ("giardino", "Giardino", "garden", "a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon"),
 ("cantina", "Cantina o garage", "cellar", "a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern"),
]
STANZE = [("bagno", "bathroom", "bagno.webp"), ("camera", "bedroom", "camera.webp"), ("sgabuzzino", "storage room", "sgabuzzino.webp"), ("corridoio", "corridor", "corridoio.webp"),
          ("cucina", "kitchen", "cucina.webp"), ("ingresso", "entrance hall", "ingresso.webp"), ("soggiorno", "living room", "soggiorno.webp"), ("balcone", "balcony", "balcone.webp")]
NOMI_IT = {"bagno": "Bagno", "camera": "Camera", "sgabuzzino": "Sgabuzzino", "corridoio": "Corridoio", "cucina": "Cucina", "ingresso": "Ingresso", "soggiorno": "Soggiorno", "balcone": "Balcone"}
# Descrizioni delle 6 stanze in più, per dimora: stile comune + oggetti tipici
EXTRA_DESC = {
 "cucina_soggiorno": "ONE single open space room with a kitchen corner along the left wall (stove, counter, shelves) and a living area along the right wall (fireplace, sofa), a small dining table near the back",
 "studio": "a study with a writing desk with candles and papers, bookshelves along the back walls, a reading armchair",
 "lavanderia": "a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes",
 "cantina": "a cellar with barrels and crates against the back walls, shelves of jars and bottles, a small workbench",
 "terrazzo": "a wide open terrace with a balustrade along the front edges, potted plants, a small table with two chairs, open to a starry night sky with a crescent moon (show only the terrace, not the outside of the building)",
 "giardino": "a small enclosed garden open to a starry night sky, grass and stone paths, flower beds and a little fountain against the back walls, a bench",
}
SPAZIO = ("Keep the furniture close to the back walls and leave room for decorations added later: three EMPTY floor spots with nothing on them "
          "(one near the left wall, one near the right wall, one in the front center of the floor) and two BARE patches of wall at mid height "
          "(one on the left back wall, one on the right back wall) with no windows, banners, paintings, mirrors or lamps there.")
REGOLE = ("Every room drawn exactly like the attached room image: same 3/4 isometric angle seen from above (NOT a first-person or one-point perspective view), "
          "a diamond-shaped floor, two back walls (left and right), an open door on the right back wall, same wall height and pixel scale. "
          "Each room is ONE single complete room, separate from the others, with no extra rooms or sections around it.")
# Stile degli interni (senza tetti, torri e paesaggi, che valgono solo per la sezione)
INTERNI = {"reggia": "white marble walls with gold trims, tall gothic windows, blue velvet and blue and gold heraldic banners",
 "hobbit": "round earthen walls with wooden beams, round windows and doors, warm lanterns, patchwork fabrics",
 "torre": "curved dark grey stone walls, arched windows, glowing purple crystals, candles and violet lanterns",
 "rifugio": "thick log walls on a stone base, wooden beams, red check fabrics and fur throws, warm lanterns",
 "albero": "curved bark walls and branches, round wooden windows, leaves, hanging lanterns and glowing mushrooms",
 "faro": "white painted planks and stone, round portholes, blue and white fabrics, brass lamps and ropes",
 "abbazia": "grey stone walls with moss and ivy, pointed arches, small stained glass windows, candles in niches",
 "nave": "curved dark wooden ship walls, portholes with clouds outside, brass fittings, ropes and hanging lanterns"}
def foglio(chi, stile, stanze, n_col=2):
    pos = ["Top left", "Top right", "Bottom left", "Bottom right"] if len(stanze) == 4 else ["Left", "Right"]
    griglia = "a 2x2 grid" if len(stanze) == 4 else "a single row of 2"
    return (f"16-bit pixel art sprite sheet of {len(stanze)} separate ISOMETRIC room interiors of {chi}, arranged in {griglia} with wide gaps of flat pure chroma green (#00FF00) between them. "
            f"{REGOLE} Walls and furniture in the style of {stile}. {SPAZIO}\n" +
            " ".join(f"{p}: {d}." for p, d in zip(pos, stanze)) +
            "\nClean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters, no green inside the rooms.")
FOGLI = [
 ("Foglio 1", "bagno, camera, cucina, soggiorno", ["bagno", "camera", "cucina", "soggiorno"]),
 ("Foglio 2", "ingresso, corridoio, sgabuzzino, balcone", ["ingresso", "corridoio", "sgabuzzino", "balcone"]),
 ("Foglio 3", "cucina-soggiorno, studio, lavanderia, cantina", ["cucina_soggiorno", "studio", "lavanderia", "cantina"]),
 ("Foglio 4", "terrazzo, giardino", ["terrazzo", "giardino"]),
]
def desc(st, k):
    if k in EXTRA_DESC: return EXTRA_DESC[k]
    d = st[k]
    if k == "corridoio": d += " (a narrow room, still isometric)"
    return d
def fronte(chi, stile):
    return (f"16-bit pixel art sprite sheet of 6 separate FRONT-VIEW cutaway rooms of {chi}, in exactly the same flat front view, layout and pixel scale as the attached sheet "
            f"(dollhouse cross-section seen straight from the front: back wall, floor, two short side walls; NOT isometric, NOT seen from above). "
            f"3x2 grid with wide gaps of flat pure chroma green (#00FF00). Walls and furniture in the style of {stile}. "
            "Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace open to the starry night sky, small garden with a fountain open to the starry night sky, cellar with barrels. "
            "Clean and tidy, warm light. No characters, no text, no letters, no green inside the rooms.")
def sezione(chi, stile):
    return (f"16-bit pixel art cutaway cross-section of {chi} at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: "
            "the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; "
            "bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. "
            f"Restyle the outer walls, roofs, towers and surroundings as {stile}. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.")
P = lambda t: ["```", t, "```", ""]
out = ["# Prompt delle dimore", "",
 "## Come funziona", "",
 "Le stanze sono **standard**: ogni dimora ha la sua versione di ogni tipo, e la vista d'insieme si compone dalla vostra pianta.",
 "Ogni stanza lascia libero lo spazio per gli arredi: **3 punti a terra** (vicino alla parete sinistra, vicino alla parete destra, al centro davanti) e **2 tratti di parete spogli** (uno a sinistra e uno a destra) per quadri e arazzi.", "",
 "**Per ogni dimora servono 6 immagini:**",
 "1. **Sezione**: allega `castello.png` e, se lo hai, l'esterno della dimora.",
 "2. **Stanze in più viste di fronte**: allega il foglio verde del castello (`tessere_extra_castello.png`).",
 "3. **Interni, fogli 1–4**: 4 stanze per foglio su fondo verde (il 4° ne ha 2). Allega `soggiorno.png` del castello come riferimento dell'inquadratura.", "",
 "**Consigli**",
 "- Genera i fogli uno dopo l'altro **nella stessa chat** del generatore: lo stile resta coerente.",
 "- Se in un foglio una stanza viene male, rigenera solo quel foglio.",
 "- Mandami una dimora alla volta: ritaglio, allineo e collego io.",
 "- Finché manca un'immagine l'app usa quella più simile, quindi si può fare un po' alla volta.", "",
 "---", "", "## La Rocca di Pietranotte", "", "**Completa.** Sezione, 14 interni e stanze in più viste di fronte ci sono tutti.", ""]
for k, nome, lv, chi, stile, st in D:
    out += ["---", "", f"## {nome}", "", (f"Si sblocca al livello {lv}." if lv > 1 else "Disponibile da subito."), ""]
    if k == "reggia":
        out += ["**Completo** (sezione, 14 interni, 5 stanze in più viste di fronte). Manca solo la lavanderia vista di fronte: finché non c'è si usa lo sgabuzzino.", ""]
        continue
    out += ["### Sezione", "", "Allega: `castello.png` + l'esterno della dimora.", ""] + P(sezione(chi, stile))
    out += ["### Stanze in più viste di fronte", "", "Allega: `tessere_extra_castello.png`.", ""] + P(fronte(chi, INTERNI[k]))
    for titolo, elenco, ks in FOGLI:
        out += [f"### Interni · {titolo}: {elenco}", "", "Allega: `soggiorno.png` del castello.", ""] + P(foglio(chi, INTERNI[k], [desc(st, x) for x in ks]))
open("PROMPT-DIMORE.md", "w", encoding="utf-8").write("\n".join(out))
print(sum(1 for x in out if x == "```") // 2, "prompt")
