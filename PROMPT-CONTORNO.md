# Prompt del contorno della dimora (rettangolo delle stanze, torri accanto, portone)

Il **contorno** è il guscio vuoto dentro cui l'app mette le stanze. Cosa cambia rispetto a quello di ora:
- le stanze stanno in **un rettangolo unico** con una cornice di pietra dritta su tutti e quattro i lati;
- le **torri stanno accanto** al rettangolo e non ci entrano mai;
- sotto il rettangolo c'è il **portone d'ingresso**.

**Cosa allegare:** la sezione della dimora (per la Rocca `castello.png`), così colori, luce e scala restano quelli.

**Cosa farò con l'immagine:**
- il **verde** (cielo, terra e apertura) diventa trasparente: il rettangolo verde mi dice da solo dove vanno le stanze, e il cielo lo rimetto io (luna, stelle e nuvole);
- le **torri** e i **lati della cornice** hanno un tratto uguale ripetuto, così posso allungarli quanto serve per qualunque numero di piani;
- tetto, base e portone restano come li disegna il generatore.

**Consigli**
- Se le misure non sono precise (rettangolo un po' più largo, torri un po' più grosse) non importa: le misuro io sull'immagine.
- Controlla solo che le torri **non tocchino il verde dell'apertura** e che la cornice sia **dritta e uguale** sui due lati.
- Se viene bene a metà (per esempio il portone è sbagliato), mandamela lo stesso e rigenero solo quel pezzo.

---

## La Rocca di Pietranotte

```
16-bit pixel art of the EMPTY FRONT SHELL of a castle, drawn as a perfectly flat FRONT ELEVATION (orthographic, straight from the front, NO perspective, NO three-quarter view, no cast shadows on the ground), for a side-view cutaway dollhouse game (like Fallout Shelter). Portrait image, 9:16. The whole background is flat pure chroma green (#00FF00): the sky, the ground around the castle AND the big rectangular opening in the middle are all the same flat green. LAYOUT, measured on the width and height of the image. 1) CENTRAL FRAME: one big perfectly straight RECTANGLE of thick stone wall that surrounds an empty rectangular opening. The opening is flat green, with razor-straight edges and square corners, starting at 15% of the width and ending at 85% of the width, and going from 21% to 82% of the height. Around the opening the stone frame is about 2% of the width thick on the left, right and top, with a thin lighter stone rim (coping) on its inner edge. The two vertical sides of the frame are plain, regular stone courses with no windows and no decorations, always the same from top to bottom (so that a slice can be repeated). On top of the frame there is a straight parapet with square battlements (merlons) that rises from 15% to 21% of the height. 2) TWO FREE-STANDING TOWERS, one on the far left and one on the far right of the image, each exactly 12.5% of the width wide, standing right next to the frame but NEVER overlapping it and NEVER entering the rectangle. Round dark purple-grey stone towers with a crenellated crown. Each tower is a straight round cylinder with the SAME width from top to bottom: no flare, no wider crown, no wider foot. Each tower rises from 11% to 97% of the height, with a crown at the top (its top is a little higher than the frame's parapet). The middle part of each tower is a repeating pattern, identical every 12% of the height: plain bricks and one narrow arrow slit window, so that a slice of it can be repeated. A simple stone plinth at the foot. 3) FRONT WALL BELOW THE OPENING, from 82% to 97% of the height, as wide as the frame, with the same stone and the same courses. In the exact center of it: a big arched double gate (PORTONE) made of dark oak planks with black wrought-iron bands and studs, under a pointed stone arch, about 22% of the width wide and 9% of the height tall, with a lit wall torch on each side of the arch. The gate reaches the bottom edge of the wall; there is a small flat stone step in front of it; on both sides of the gate a short plain stretch of wall with a small arrow slit. The wall and the towers end on one straight stone base line at 97% of the height, and under it is the flat green ground. Every straight edge is perfectly horizontal or vertical. Stone and materials in the style of dark purple-grey stone bricks, dark wooden beams and furniture, wrought iron details, warm candle light, a moody dark fantasy medieval castle. Same front view, light, colors and pixel scale as the attached castle section. No characters, no sky details (no moon, no stars, no clouds), no text, no letters, no green inside the stone.
```
