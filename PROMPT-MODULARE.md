# Prompt delle stanze modulari

## Come funziona

Nella vista della dimora ogni stanza è fatta di **due parti**, come nei giochi tipo Fallout Shelter:
1. **Lo sfondo** (muro, fregio e pavimento): lo costruisco io da codice partendo dai **campioni di materiale**, quindi si ripete senza giunture e la stanza può essere larga quanto serve.
2. **I mobili**: pezzi singoli su fondo verde, che l'app appoggia sul pavimento.

Le stanze che si aprono toccandole restano come sono: questi prompt servono solo per la vista della dimora.

**Per ogni dimora servono 9 immagini:** 3 fogli di materiali (pavimenti, muri, fregi) e 6 fogli di mobili (2 stanze per foglio, 6 pezzi per stanza).
I pavimenti si generano visti **dall'alto**, così non possono avere prospettiva: sono io a schiacciarli per farli sembrare a terra.

**Cosa allegare**
- **Pavimenti**: allega la sezione della dimora (per la Rocca `castello.png`, per il Palazzo `sezione.png`), così colori e stile restano quelli.
- **Muri e fregi**: allega il foglio pavimenti della stessa dimora.
- **Mobili**: allega il foglio muri della stessa dimora (stessa luce e stessa scala).

**Consigli**
- Genera i fogli di una dimora **nella stessa chat** del generatore, uno dopo l'altro: lo stile resta coerente.
- Se un campione ha una giuntura ai bordi non importa: la sistemo io.
- Se in un foglio un pezzo viene male o ne manca uno, va bene lo stesso: dimmelo e lo salto.
- **Rocca:** i muri dei due fogli di sfondi già fatti vanno bene e li riuso. Servono solo *Pavimenti* e *Mobili foglio 1 e 2*.

---

## La Rocca di Pietranotte

Disponibile da subito.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## Il Palazzo d'Argentaluna

Disponibile da subito.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of gleaming white marble with gold trims, blue velvet and blue and gold heraldic details, polished light wood, a bright fairy-tale palace. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## La Tana di Colleverde

Si sblocca al livello 4.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved earthen walls with wooden beams, warm honey-colored wood, green and ochre fabrics, round shapes, a cozy burrow inside a grassy hill. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## La Torre dell'Ametista

Si sblocca al livello 6.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of dark grey stone with glowing purple amethyst crystals, violet fabrics, brass and old wood, a wizard tower. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## Il Rifugio di Vettagelo

Si sblocca al livello 8.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of thick wooden logs on a stone base, red check wool fabrics, furs, warm firelight, a snowy mountain refuge. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## Il Nido del Grande Faggio

Si sblocca al livello 10.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of living tree bark and pale carved wood, leaves in autumn colors, woven fabrics, glowing fireflies, an elven treehouse. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## Il Faro di Scogliasecca

Si sblocca al livello 12.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of white painted planks and stone, navy blue and red details, brass and rope, a seaside lighthouse. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## L'Abbazia di Muschioscuro

Si sblocca al livello 14.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of old grey stone with moss and ivy, dark oak, iron candle stands, stained glass colors, a forest abbey. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---

## Il Galeone delle Nuvole

Si sblocca al livello 16.

### Materiali · Pavimenti (visti dall'alto)

```
16-bit pixel art texture sheet of 9 FLOOR materials for a cozy dark fantasy game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture seen EXACTLY FROM DIRECTLY ABOVE (top-down, orthographic): completely flat, no perspective, no vanishing point, no horizon, every plank and tile line perfectly horizontal or vertical. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no shadows, no vignette, no darker edges, no objects, no furniture, no rugs. Materials in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Order left to right, top to bottom: 1) light wooden planks; 2) dark wooden planks; 3) old worn wooden planks; 4) large stone slabs; 5) small square stone tiles; 6) black and white checkered tiles; 7) wooden parquet with a geometric pattern; 8) packed earth with small stones; 9) short grass. No text, no letters, no green inside the swatches.
```

### Materiali · Muri

```
16-bit pixel art texture sheet of 9 WALL materials for a side-view cutaway dollhouse game, arranged in a 3x3 grid of square swatches separated by wide gaps of flat pure chroma green (#00FF00). Every swatch is a seamless tileable texture of a flat wall seen straight from the front, with no perspective, no corners, no floor, no ceiling. Each swatch tiles seamlessly in both directions: its left edge continues into its right edge and its top edge into its bottom edge. Even flat lighting, no vignette, no darker edges, no doors, no windows, no lamps, no objects. Materials in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Order left to right, top to bottom: 1) stone bricks; 2) smooth plaster; 3) plaster in a darker shade; 4) rough irregular stones; 5) carved wooden panelling; 6) square ceramic tiles; 7) vertical wooden boards; 8) large cut stone blocks; 9) a starry night sky with no moon (for outdoor rooms). No text, no letters, no green inside the swatches.
```

### Materiali · Fregi (battiscopa, boiserie, fasce, balaustra, siepe)

```
16-bit pixel art sheet of 6 horizontal TRIM STRIPS for a side-view cutaway dollhouse game, stacked one above the other across the whole width of the image and separated by wide gaps of flat pure chroma green (#00FF00). Every strip is seen straight from the front, flat, with no perspective, and tiles seamlessly horizontally: its left end continues exactly into its right end. Each strip is drawn as it would sit along the bottom of a wall. Even flat lighting, no vignette, no darker ends. Materials in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. From top to bottom: 1) a wooden wainscot with vertical boards and a top rail; 2) a simple wooden baseboard; 3) a thin decorative painted band; 4) a band of small decorated ceramic tiles; 5) a stone balustrade; 6) a low trimmed hedge. No text, no letters, no green inside the strips.
```

### Mobili · Foglio 1: soggiorno (sopra) e camera (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Top row, left to right (SOGGIORNO): 1) a sofa, 2) an armchair, 3) a fireplace, 4) a tall bookcase, 5) a low coffee table, 6) a tall window (wall piece). Bottom row, left to right (CAMERA): 1) a double bed, 2) a wardrobe, 3) a nightstand with a candle, 4) a dresser, 5) a rug (seen from slightly above), 6) a window with curtains (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 2: cucina (sopra) e bagno (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Top row, left to right (CUCINA): 1) a stove with a pot, 2) a counter with a sink, 3) a tall cupboard, 4) a small table with two chairs, 5) a shelf with jars (wall piece), 6) hanging pots and pans (wall piece). Bottom row, left to right (BAGNO): 1) a clawfoot bathtub, 2) a washbasin on a stand, 3) a toilet, 4) a towel rack with towels, 5) a mirror (wall piece), 6) a small window (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 3: ingresso (sopra) e corridoio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Top row, left to right (INGRESSO): 1) a big double front door (wall piece, reaching the floor), 2) a coat stand with cloaks, 3) a bench, 4) an umbrella and boot stand, 5) a doormat (seen from slightly above), 6) a wall lamp (wall piece). Bottom row, left to right (CORRIDOIO): 1) a small console table with a vase, 2) a suit of armour or a statue, 3) a tall plant in a pot, 4) a long carpet runner (seen from slightly above), 5) a wall lamp (wall piece), 6) a hanging banner (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 4: sgabuzzino (sopra) e studio (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Top row, left to right (RIPOSTIGLIO): 1) shelves full of folded linens and boxes, 2) a broom and a bucket, 3) a stack of crates, 4) a barrel, 5) a mop and cleaning things, 6) hanging tools on hooks (wall piece). Bottom row, left to right (STUDIO): 1) a desk with books and a quill, 2) a desk chair, 3) a tall bookcase, 4) a globe on a stand, 5) a reading armchair, 6) a map (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 5: lavanderia (sopra) e cantina (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Top row, left to right (LAVANDERIA): 1) washing tubs, 2) a drying rack with clothes, 3) a laundry basket, 4) a big cauldron of hot water, 5) an ironing board, 6) a shelf with folded linen (wall piece). Bottom row, left to right (CANTINA): 1) a stack of wine barrels, 2) a wine rack with bottles, 3) a workbench with tools, 4) sacks of flour, 5) a pile of firewood, 6) a hanging lantern (wall piece). Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

### Mobili · Foglio 6: balcone e terrazzo (sopra) e giardino (sotto)

```
16-bit pixel art sprite sheet of separate furniture pieces on a flat pure chroma green (#00FF00) background, for a side-view cutaway dollhouse game (like Fallout Shelter or Tiny Tower). Same front view, light and pixel scale as the attached material sheets: every piece seen straight from the front and slightly from above; floor pieces stand on their own feet, wall pieces are drawn flat as if hanging on a wall. Each piece is complete and separate, with wide green gaps around it; no piece touches another, no shadows on the green, no floor and no wall behind the pieces. Furniture in the style of curved ship planks of warm wood, brass fittings, ropes and canvas, red and navy fabrics, a flying galleon above the clouds. Top row, left to right (BALCONE): 1) a potted plant, 2) a small potted tree, 3) a small round table with two chairs, 4) a bench, 5) a lantern on a post, 6) a flower box (to put on the balustrade). Bottom row, left to right (GIARDINO): 1) a small fountain, 2) a flower bed, 3) a garden bench, 4) a small tree, 5) a vegetable patch, 6) a lantern on a post. Clean and tidy. No characters, no text, no letters, no green inside the pieces.
```

---
