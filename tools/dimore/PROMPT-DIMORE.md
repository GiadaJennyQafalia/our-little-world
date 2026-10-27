# Prompt delle dimore

## Come funziona il sistema delle stanze

Le stanze sono **standard**: ogni dimora ha la sua versione di ogni tipo. La vista d'insieme non è più un'immagine fissa: l'app la compone dalla **vostra pianta**, mettendo ogni stanza al suo posto dentro la cornice della dimora. Cambiando dimora la casa resta la stessa.

Per ogni dimora servono:
1. **Sezione** (1 immagine): da qui ricavo la cornice (tetto, mura, base) e le 8 stanze di base viste di fronte.
2. **Stanze in più viste di fronte** (1 immagine): open space, studio, lavanderia, terrazzo, giardino, cantina.
3. **Interni** (14 immagini): le 8 stanze di base e le 6 in più, in prospettiva isometrica.

Finché un'immagine manca, l'app usa quella più simile (es. lo studio usa il soggiorno), quindi si può generare un po' alla volta.

**Come generarle**
- Sezione: allega `castello.png` (modello della disposizione) e l'esterno della dimora come stile.
- Stanze in più viste di fronte: allega `castello.png` come stile.
- Interni: allega la stanza del castello con lo stesso nome (`bagno.png`, `camera.png`…); per le 6 stanze in più allega `soggiorno.png`.
- Salva con i nomi indicati e mandami una dimora alla volta.

Le stanze sono di notte, in ordine e senza personaggi: lo sporco e gli eroi li aggiunge l'app.

---

## La Rocca di Pietranotte (il castello di adesso)

Ha già la sezione e le 8 stanze di base: mancano solo le stanze in più.

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a dark stone medieval castle, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of dark grey stone walls with battlements, round towers, torches and candle light. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a dark stone medieval castle, in the style of dark grey stone walls with battlements, round towers, torches and candle light, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a dark stone medieval castle, in the style of dark grey stone walls with battlements, round towers, torches and candle light, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a dark stone medieval castle, in the style of dark grey stone walls with battlements, round towers, torches and candle light, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a dark stone medieval castle, in the style of dark grey stone walls with battlements, round towers, torches and candle light, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a dark stone medieval castle, in the style of dark grey stone walls with battlements, round towers, torches and candle light, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a dark stone medieval castle, in the style of dark grey stone walls with battlements, round towers, torches and candle light, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## Il Palazzo d'Argentaluna

Disponibile da subito.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of a white marble fairy-tale palace at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a white marble fairy-tale palace, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a white marble fairy-tale palace, in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a white marble fairy-tale palace, in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a white marble fairy-tale palace, in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a white marble fairy-tale palace, in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a white marble fairy-tale palace, in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a white marble fairy-tale palace, in the style of gleaming white marble walls with gold trims, slender towers with deep blue pointed roofs, tall gothic windows with warm golden light, blue and gold heraldic banners, a pale stone courtyard, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of a white marble bathroom with a gilded clawfoot tub, a marble washbasin with gold taps, a tall gilded mirror, blue velvet curtains, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a royal bedroom with a canopy bed with blue silk curtains, a white and gold wardrobe, a vanity table with a mirror, a thick blue rug, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a tidy palace storage room with white cabinets with gold handles, shelves of folded linens and glass jars, a silver bucket and a broom, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a long palace gallery corridor with a white marble floor, a narrow blue and gold carpet runner, gilded wall sconces, a small console table with a flower vase, inside a white marble fairy-tale palace, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a bright palace kitchen with a white tiled stove with copper pots, marble counters, a cabinet with fine porcelain, a small round table set with silverware, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a grand entrance hall with a double door with gold details, a white marble floor with a round blue rug, a gilded coat stand, a bench with cushions, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of an elegant throne-room style living room with a white marble fireplace, a blue velvet sofa, gilded armchairs, a harp in the corner, tall windows, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of a white marble balcony with a carved balustrade, potted white roses and small lemon trees, a wrought iron bench, a starry night sky with a crescent moon, inside a white marble fairy-tale palace, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## La Tana di Colleverde

Si sblocca al livello 4.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of a cozy burrow dug inside a grassy hill at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a cozy burrow dug inside a grassy hill, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a cozy burrow dug inside a grassy hill, in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a cozy burrow dug inside a grassy hill, in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a cozy burrow dug inside a grassy hill, in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a cozy burrow dug inside a grassy hill, in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a cozy burrow dug inside a grassy hill, in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a cozy burrow dug inside a grassy hill, in the style of round earthen walls covered in grass, round wooden doors and round windows, warm lanterns hanging on chains, wildflowers and stepping stones, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of a cozy burrow bathroom with round earthen walls, a wooden barrel bathtub, a clay washbasin on a wooden stand, a round mirror, dried herbs hanging, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a burrow bedroom with a low wooden bed with a patchwork quilt, a round window, a small wooden dresser, a braided rug, a lantern on a nightstand, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a burrow pantry with curved wooden shelves full of jars of jam, cheese wheels, sacks of flour, strings of onions and garlic, a broom and a basket, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a curved burrow tunnel corridor with wooden beams, a round wooden door at the end, a long woven rug, little lanterns on the walls, inside a cozy burrow dug inside a grassy hill, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a burrow kitchen with a stone hearth and a hanging cauldron, a big wooden table with mismatched chairs, shelves with clay pots, a basket of vegetables, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a burrow entrance with a big round green wooden door, a coat rack with cloaks and walking sticks, a doormat, a bench with boots, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of a burrow living room with a round fireplace, two squashy armchairs, a pipe stand, bookshelves carved into the earth, a round rug, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of a small grassy terrace on the hill with a low wooden fence, flower pots, a little bench, fireflies, a starry night sky with a crescent moon, inside a cozy burrow dug inside a grassy hill, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## La Torre dell'Ametista

Si sblocca al livello 6.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of a tall wizard tower of dark stone with purple crystals at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a tall wizard tower of dark stone with purple crystals, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a tall wizard tower of dark stone with purple crystals, in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a tall wizard tower of dark stone with purple crystals, in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a tall wizard tower of dark stone with purple crystals, in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a tall wizard tower of dark stone with purple crystals, in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a tall wizard tower of dark stone with purple crystals, in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a tall wizard tower of dark stone with purple crystals, in the style of dark grey stone, a spiral staircase climbing outside, narrow arched windows with warm light, floating glowing purple crystals, small lanterns with violet flames, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of a wizard tower bathroom with curved stone walls, a copper tub with purple steam, a washbasin carved from a crystal geode, glowing amethyst stones, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a wizard bedroom with a bed with a starry purple blanket, a desk with an open spellbook and candles, a telescope by the arched window, stacks of books, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a wizard storage room with shelves of potion bottles, jars with strange ingredients, scrolls in cubbyholes, a flying broom leaning on the wall, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a narrow curved tower corridor with stone steps, glowing rune symbols on the walls, a long purple rug, floating candles, inside a tall wizard tower of dark stone with purple crystals, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a wizard kitchen with a bubbling cauldron on a stove, shelves of herbs and potion bottles, a wooden table with a mortar and pestle, hanging dried plants, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a tower entrance with a heavy arched wooden door with iron runes, a coat rack with a wizard hat and cloak, a magic circle drawn on the floor, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of a wizard study used as a living room with a fireplace with purple flames, a velvet armchair, a globe, bookshelves up to the ceiling, a crystal ball on a stand, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of a round stone balcony at the top of the tower with a crenellated parapet, a telescope, floating purple crystals, a starry night sky with a crescent moon, inside a tall wizard tower of dark stone with purple crystals, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## Il Rifugio di Vettagelo

Si sblocca al livello 8.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of a mountain refuge made of logs and stone on a snowy peak at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a mountain refuge made of logs and stone on a snowy peak, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a mountain refuge made of logs and stone on a snowy peak, in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a mountain refuge made of logs and stone on a snowy peak, in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a mountain refuge made of logs and stone on a snowy peak, in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a mountain refuge made of logs and stone on a snowy peak, in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a mountain refuge made of logs and stone on a snowy peak, in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a mountain refuge made of logs and stone on a snowy peak, in the style of thick log walls on a stone base, a steep snowy roof, icicles, warm glowing windows, pine trees covered in snow, snowy mountain peaks, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of a mountain lodge bathroom with log walls, a wooden tub, an enamel washbasin, thick wool towels, a small window with snow outside, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a mountain lodge bedroom with a log bed with fur blankets and a red check quilt, a wooden chest, antlers on the wall, a small snowy window, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a mountain lodge storage room with stacked firewood, skis and snowshoes, wool blankets on shelves, lanterns, a broom and a bucket, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a narrow log corridor with wooden plank floor, a long red woven rug, coat hooks with scarves, small lanterns, a wooden door at the end, inside a mountain refuge made of logs and stone on a snowy peak, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a mountain kitchen with a cast-iron wood stove, a pot of soup, a heavy wooden table with benches, hanging cured meats and herbs, cheese on a board, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a mountain lodge entrance with a heavy wooden door, a bench with snow boots, coats and scarves on hooks, a snowy doormat, a lantern, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of a mountain lodge living room with a big stone fireplace, a sofa with fur throws, a rocking chair, a bear skin rug, mugs of hot chocolate, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of a wooden balcony with a log railing covered in snow, potted pines, a bench with a blanket, snowy mountain peaks and a starry night sky with a crescent moon, inside a mountain refuge made of logs and stone on a snowy peak, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## Il Nido del Grande Faggio

Si sblocca al livello 10.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of an elven house built in the branches of a giant ancient tree at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of an elven house built in the branches of a giant ancient tree, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside an elven house built in the branches of a giant ancient tree, in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside an elven house built in the branches of a giant ancient tree, in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside an elven house built in the branches of a giant ancient tree, in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside an elven house built in the branches of a giant ancient tree, in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside an elven house built in the branches of a giant ancient tree, in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside an elven house built in the branches of a giant ancient tree, in the style of a huge tree trunk with rooms between the branches, rope bridges, round wooden windows, glowing lanterns and fireflies, leaves in autumn colors, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of an elven treehouse bathroom with curved bark walls, a tub carved in a tree stump, a washbasin made of a big shell, hanging vines, glowing mushrooms, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of an elven treehouse bedroom with a bed woven from branches with a leaf blanket, a round window with leaves outside, hanging lanterns, a carved wooden chest, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a treehouse storage room with woven baskets of nuts and berries, clay jars, coiled ropes, a bow and quiver, a broom made of twigs, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a narrow treehouse passage along a thick branch with a wooden plank floor, a woven leaf rug, rope railings, small lanterns, inside an elven house built in the branches of a giant ancient tree, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a treehouse kitchen with a small clay oven, a table carved from a stump, baskets of fruit and mushrooms, hanging herbs, wooden bowls, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a treehouse entrance with a round wooden door set in the trunk, a ladder, cloaks on branch hooks, a moss doormat, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of an elven treehouse living room with a small stone hearth, cushions on a woven rug, a harp, shelves in the hollow of the trunk, glowing fireflies, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of a wooden platform on a big branch with a rope railing, hanging lanterns, potted ferns, leaves all around, a starry night sky with a crescent moon, inside an elven house built in the branches of a giant ancient tree, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## Il Faro di Scogliasecca

Si sblocca al livello 12.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of a lighthouse on a rocky island in the sea at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a lighthouse on a rocky island in the sea, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a lighthouse on a rocky island in the sea, in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a lighthouse on a rocky island in the sea, in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a lighthouse on a rocky island in the sea, in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a lighthouse on a rocky island in the sea, in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a lighthouse on a rocky island in the sea, in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a lighthouse on a rocky island in the sea, in the style of a tall white and red striped lighthouse tower with a bright lamp on top, a stone keeper's cottage at its base, rocks, crashing waves and seagulls, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of a lighthouse keeper bathroom with white painted planks, a tin tub, a porthole mirror, blue and white towels, seashells on a shelf, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a lighthouse bedroom with a wooden bed with a navy blanket, a round porthole window with the sea, a ship in a bottle, a sea chest, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a lighthouse storage room with coiled ropes, oil cans for the lamp, fishing nets, lanterns, life rings, a broom and a bucket, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a narrow curved lighthouse corridor with a spiral stair going up, white painted stone walls, a striped rug, brass lamps, inside a lighthouse on a rocky island in the sea, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a lighthouse kitchen with a small iron stove, a pot of fish soup, a wooden table, blue and white plates on a rack, a fishing net on the wall, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a lighthouse entrance with a heavy blue wooden door, oilskin coats and boots, an anchor by the wall, a striped doormat, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of a lighthouse keeper living room with a small fireplace, an armchair with a blanket, maps and a ship's wheel on the wall, a telescope, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of the round gallery around the lighthouse lamp with an iron railing, the big lamp glowing behind, the sea and a starry night sky with a crescent moon, inside a lighthouse on a rocky island in the sea, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## L'Abbazia di Muschioscuro

Si sblocca al livello 14.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of an old stone abbey hidden in a mossy forest at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of an old stone abbey hidden in a mossy forest, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside an old stone abbey hidden in a mossy forest, in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside an old stone abbey hidden in a mossy forest, in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside an old stone abbey hidden in a mossy forest, in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside an old stone abbey hidden in a mossy forest, in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside an old stone abbey hidden in a mossy forest, in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside an old stone abbey hidden in a mossy forest, in the style of grey stone walls covered in moss and ivy, a bell tower, pointed arches, stained glass windows glowing warmly, tall dark trees around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of an abbey bathroom with stone walls and moss, a stone basin fed by a little fountain, a wooden tub, candles in niches, a small stained glass window, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a monk's cell bedroom with a simple wooden bed with a wool blanket, a desk with a candle and an illuminated manuscript, a stone arched window, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of an abbey cellar with wine barrels, jars of honey, bundles of herbs, candles in boxes, a broom and a bucket, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a cloister corridor with stone arches, a long rug, candles on iron stands, a wooden door at the end, inside an old stone abbey hidden in a mossy forest, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of an abbey kitchen with a big stone hearth, a long wooden table, loaves of bread, a bubbling pot, hanging herbs and copper pans, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of an abbey entrance with a huge arched oak door with iron studs, a stone holy water font, a bench, a hanging bell rope, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of an abbey library used as a living room with tall bookshelves, a reading lectern, a fireplace, wooden armchairs, a big stained glass window, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of a stone loggia with arches overlooking the cloister garden with a fountain, potted herbs, ivy, a starry night sky with a crescent moon, inside an old stone abbey hidden in a mossy forest, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

---

## Il Galeone delle Nuvole

Si sblocca al livello 16.

### Sezione

Allega: `castello.png` + l'esterno della dimora. Salva come `sezione.png`.

```
16-bit pixel art cutaway cross-section of a flying wooden galleon sailing above the clouds at night, portrait format 768x1376 pixels, in exactly the same layout as the attached castle cutaway: the same 8 rooms in the same positions and sizes (top row: bathroom on the left, bedroom on the right; middle row: storage room on the left, a narrow vertical corridor in the center, kitchen on the right; bottom row: entrance hall on the left, living room on the right; a narrow balcony strip along the right side), the same thick dark outlines between rooms, the same camera, the same pixel scale. Restyle the outer walls, roofs, towers and surroundings as a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around. Each room furnished in the same style, clean and tidy, warm candle light. Starry night sky with a crescent moon. No characters, no text, no letters.
```

### Stanze in più viste di fronte

Allega: `castello.png`. Salva come `tessere_extra.png`.

```
16-bit pixel art sprite sheet of 6 separate front-view cutaway rooms of a flying wooden galleon sailing above the clouds, in exactly the same style, pixel scale and front cutaway view as the rooms inside the attached castle cutaway (back wall, floor, furniture seen from the front, thick dark outline around each room). Arranged in a 3x2 grid with wide gaps of flat pure chroma green (#00FF00) between them. Walls and furniture in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around. Top row, left to right: open space kitchen and living room, study, laundry room. Bottom row, left to right: terrace, garden, cellar. The terrace and the garden are open to a starry night sky. Clean and tidy, warm light. No characters, no text, no letters.
```

### Cucina-soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `cucina_soggiorno.png`.

```
16-bit pixel art isometric interior of a large open space room with a kitchen corner on the left (stove, counter, shelves) and a living area on the right (fireplace, sofa, rug), a dining table in the middle, inside a flying wooden galleon sailing above the clouds, in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Studio (interno)

Allega: `soggiorno.png` del castello. Salva come `studio.png`.

```
16-bit pixel art isometric interior of a study with a writing desk with candles and papers, tall bookshelves, a reading armchair, a globe, inside a flying wooden galleon sailing above the clouds, in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Lavanderia (interno)

Allega: `soggiorno.png` del castello. Salva come `lavanderia.png`.

```
16-bit pixel art isometric interior of a laundry room with a washtub and washboard, a drying rack with linens, baskets of clothes, an iron on a small board, inside a flying wooden galleon sailing above the clouds, in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Terrazzo (interno)

Allega: `soggiorno.png` del castello. Salva come `terrazzo.png`.

```
16-bit pixel art isometric interior of a wide open terrace with a stone or wooden floor, a balustrade along the front, potted plants and small trees, a table with two chairs, a starry night sky with a crescent moon, inside a flying wooden galleon sailing above the clouds, in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Giardino (interno)

Allega: `soggiorno.png` del castello. Salva come `giardino.png`.

```
16-bit pixel art isometric interior of a small enclosed garden with grass, flower beds, a little fountain, a bench, a vegetable patch, lanterns, a starry night sky with a crescent moon, inside a flying wooden galleon sailing above the clouds, in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cantina o garage (interno)

Allega: `soggiorno.png` del castello. Salva come `cantina.png`.

```
16-bit pixel art isometric interior of a cellar with barrels and crates, shelves of jars and bottles, tools on the wall, a workbench, a lantern, inside a flying wooden galleon sailing above the clouds, in the style of a big wooden ship hull with portholes, billowing sails, a balloon and brass propellers, ropes and rigging, fluffy clouds around, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Bagno (interno)

Allega: `bagno.png` del castello. Salva come `bagno.png`.

```
16-bit pixel art isometric interior of a ship cabin bathroom with curved wooden walls, a brass tub, a porthole with clouds outside, a washbasin on a brass stand, rope details, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Camera (interno)

Allega: `camera.png` del castello. Salva come `camera.png`.

```
16-bit pixel art isometric interior of a captain's cabin bedroom with a wooden bunk bed with a red blanket, a big porthole with clouds, a sea chest, a hanging lantern, maps on the wall, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Sgabuzzino (interno)

Allega: `sgabuzzino.png` del castello. Salva come `sgabuzzino.png`.

```
16-bit pixel art isometric interior of a ship hold storage room with barrels and crates, coiled ropes, spare sails, lanterns, a broom and a mop bucket, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Corridoio (interno)

Allega: `corridoio.png` del castello. Salva come `corridoio.png`.

```
16-bit pixel art isometric interior of a narrow ship corridor below deck with curved wooden walls, a plank floor, a narrow rug, hanging lanterns, a hatch ladder, inside a flying wooden galleon sailing above the clouds, 720x706 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Cucina (interno)

Allega: `cucina.png` del castello. Salva come `cucina.png`.

```
16-bit pixel art isometric interior of a ship galley kitchen with a small iron stove, pots hanging from hooks, barrels of supplies, a fixed wooden table, a porthole, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Ingresso (interno)

Allega: `ingresso.png` del castello. Salva come `ingresso.png`.

```
16-bit pixel art isometric interior of a ship entrance with a wooden hatch door, coats and a captain's hat on hooks, a ship's bell, a coiled rope, a doormat, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Soggiorno (interno)

Allega: `soggiorno.png` del castello. Salva come `soggiorno.png`.

```
16-bit pixel art isometric interior of a captain's lounge with a big ship's wheel, a leather armchair, a globe and brass instruments, a map table, a wide window with clouds, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```

### Balcone (interno)

Allega: `balcone.png` del castello. Salva come `balcone.png`.

```
16-bit pixel art isometric interior of the open deck of the flying ship with a wooden railing, ropes and sails, a brass telescope, clouds below and a starry night sky with a crescent moon, inside a flying wooden galleon sailing above the clouds, 720x676 pixels, in exactly the same framing, camera angle, wall height and pixel scale as the attached room image: the same two back walls (left and right), the same open door on the right wall, the same floor shape, with free floor space in the middle and in the front. Clean and tidy, warm light, dark fantasy cozy mood. No characters, no text, no letters.
```
