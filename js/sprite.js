/* Our little world · personaggi
   Compone il personaggio sovrapponendo i pezzi LPC (Liberated Pixel Cup, vedi CREDITI.md) su un canvas e li ricolora
   sostituendo i colori della rampa di base con quelli scelti. Il personaggio è un piccolo oggetto salvato su Supabase:
   { classe, corpo: "male"|"female", pelle, occhi, sopr: "thin"|"thick", capelli: {id,col}, orecchie: id|null, corna: id|null,
     busto: {id,col}, gambe: {id,col}, scarpe: {id,col}, mantello: {id,col}|null, cappello: {id,col}|null, accessorio: {id,col}|null, arma: id|null }
   I colori sono nomi di palette ("blonde", "black"…) oppure esadecimali "#rrggbb". */
(function () {
  "use strict";
  const BASE = "assets/lpc/", F = 64;
  let CAT = null, pronto = null;
  const imgs = new Map(), ric = new Map();

  const carica = () => pronto || (pronto = fetch(BASE + "catalogo.json").then(r => r.json()).then(c => (CAT = c)));
  const immagine = f => {
    if (!imgs.has(f)) imgs.set(f, new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => no(new Error("manca " + f)); i.src = BASE + f; }));
    return imgs.get(f);
  };

  /* ---------- Colori ---------- */
  const hex2rgb = h => { h = h.replace("#", ""); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)); };
  const rgb2hex = c => "#" + c.map(v => Math.round(Math.max(0, Math.min(255, v))).toString(16).padStart(2, "0")).join("");
  function rgb2hsl([r, g, b]) {
    r /= 255; g /= 255; b /= 255; const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2; let h = 0, s = 0;
    if (mx !== mn) { const d = mx - mn; s = l > .5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; }
    return [h, s, l];
  }
  function hsl2rgb([h, s, l]) {
    if (!s) return [l * 255, l * 255, l * 255];
    const q = l < .5 ? l * (1 + s) : l + s - l * s, p = 2 * l - q, f = t => { t = (t + 1) % 1; return 255 * (t < 1 / 6 ? p + (q - p) * 6 * t : t < .5 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p); };
    return [f(h + 1 / 3), f(h), f(h - 1 / 3)];
  }
  /* Rampa (dal più scuro al più chiaro) per un materiale e un colore: una palette con nome oppure una generata da un colore libero. */
  function rampa(mat, col) {
    const P = CAT.palette[mat], n = P.rampe[P.base].length;
    if (col && P.rampe[col]) return P.rampe[col].map(hex2rgb);
    if (!/^#[0-9a-f]{6}$/i.test(col || "")) return P.rampe[P.base].map(hex2rgb);
    const [h, s, l] = rgb2hsl(hex2rgb(col)), out = [];
    for (let i = 0; i < n; i++) {
      const t = n === 1 ? .6 : i / (n - 1), L = Math.max(.05, Math.min(.96, l + (t - .6) * .85)), S = Math.min(1, s * (.75 + .5 * (1 - Math.abs(t - .5) * 2)));
      out.push(hsl2rgb([h, S, L]));
    }
    return out;
  }
  const chiave = (...a) => a.join("|");

  /* Ricolora un'immagine sostituendo ogni colore della rampa di base con quello corrispondente della rampa scelta. */
  async function colorata(f, mats) {
    const k = chiave(f, mats.map(m => m.join(":")).join(",")); if (ric.has(k)) return ric.get(k);
    const p = immagine(f).then(i => {
      const c = document.createElement("canvas"); c.width = i.width; c.height = i.height;
      const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(i, 0, 0);
      if (!mats.length) return c;
      const mappa = new Map();
      for (const [mat, col] of mats) { const b = rampa(mat, CAT.palette[mat].base), t = rampa(mat, col); b.forEach((rgb, j) => mappa.set((rgb[0] << 16) | (rgb[1] << 8) | rgb[2], t[j])); }
      const d = x.getImageData(0, 0, c.width, c.height), px = d.data;
      for (let j = 0; j < px.length; j += 4) { if (!px[j + 3]) continue; const t = mappa.get((px[j] << 16) | (px[j + 1] << 8) | px[j + 2]); if (t) { px[j] = t[0]; px[j + 1] = t[1]; px[j + 2] = t[2]; } }
      x.putImageData(d, 0, 0); return c;
    });
    ric.set(k, p); return p;
  }

  /* ---------- Pezzi ---------- */
  const pezzo = (slot, id) => id && CAT.slot[slot] && CAT.slot[slot].find(v => v.id === id);
  const colDi = x => (x && typeof x === "object" ? x.col : null);
  const idDi = x => (x && typeof x === "object" ? x.id : x);
  const fa = (slot, pg) => pezzo(slot, idDi(pg[slot]));
  const compatibile = (voce, corpo) => !!(voce && voce.corpi[corpo] && voce.corpi[corpo].walk);
  /* Elenco dei livelli da disegnare, ordinati dal fondo alla cima: { f, z, mats } */
  function livelli(pg) {
    const corpo = pg.corpo === "male" ? "male" : "female", L = [];
    const aggiungi = (voce, mats, col) => {
      if (!compatibile(voce, corpo)) return;
      const va = voce.varianti ? (voce.varianti.includes(col) ? col : voce.varianti[0]) : null;
      for (const l of voce.corpi[corpo].walk) L.push({ f: va ? l.f.replace("{v}", va) : l.f, z: l.z, mats: va ? [] : mats });
    };
    const pelle = pg.pelle || "light", occhi = pg.occhi || "blue";
    aggiungi(CAT.fissi.corpo, [["body", pelle]]);
    aggiungi(corpo === "male" ? CAT.fissi.testa_m : CAT.fissi.testa_f, [["body", pelle], ["eye", occhi]]);
    const capCol = colDi(pg.capelli) || "blonde";
    aggiungi(CAT.fissi["sopracciglia_" + (pg.sopr === "thick" ? "thick" : "thin")], [["hair", capCol]]);
    const mat = (voce, col) => !voce || !voce.materiale ? [] : [[voce.materiale, col || (voce.materiale === "body" ? pelle : voce.materiale === "hair" ? capCol : null)]].filter(m => m[1]);
    for (const slot of ["capelli", "orecchie", "corna", "busto", "gambe", "scarpe", "mantello", "cappello", "accessorio", "arma"]) {
      const v = fa(slot, pg); if (!v) continue;
      aggiungi(v, mat(v, colDi(pg[slot])), colDi(pg[slot]));
    }
    return L.map((l, i) => ({ ...l, i })).sort((a, b) => a.z - b.z || a.i - b.i);
  }

  /* Disegna un fotogramma 64×64: riga 0 = su, 1 = sinistra, 2 = giù, 3 = destra; colonna 0 = posa ferma, 1–8 = passi. */
  async function fotogramma(pg, riga, col) {
    await carica();
    const L = livelli(pg), fogli = await Promise.all(L.map(l => colorata(l.f, l.mats).catch(() => null)));
    const c = document.createElement("canvas"); c.width = F; c.height = F; const x = c.getContext("2d"); x.imageSmoothingEnabled = false;
    fogli.forEach(s => { if (s) x.drawImage(s, col * F, riga * F, F, F, 0, 0, F, F); });
    return c;
  }

  /* Disegna nel canvas dato: busto (ritratto) o figura intera, ingrandito senza sfocare. */
  async function disegna(canvas, pg, { riga = 2, col = 0, scala = 3, ritratto = false } = {}) {
    const fr = await fotogramma(pg, riga, col);
    const sx = ritratto ? 14 : 0, sy = ritratto ? 6 : 0, sw = ritratto ? 36 : F, sh = ritratto ? 36 : F;
    canvas.width = sw * scala; canvas.height = sh * scala;
    const x = canvas.getContext("2d"); x.imageSmoothingEnabled = false; x.clearRect(0, 0, canvas.width, canvas.height);
    x.drawImage(fr, sx, sy, sw, sh, 0, 0, canvas.width, canvas.height);
  }
  /* Fa camminare il personaggio sul posto (o ferma, se si preferisce il movimento ridotto). Restituisce una funzione che ferma l'animazione. */
  function anima(canvas, pg, { riga = 2, scala = 3, fps = 8, passi = true } = {}) {
    let attivo = true, k = 0, fotogrammi = null;
    const rid = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    (async () => {
      fotogrammi = await Promise.all((passi && !rid ? [1, 2, 3, 4, 5, 6, 7, 8] : [0]).map(c => fotogramma(pg, riga, c)));
      canvas.width = F * scala; canvas.height = F * scala; const x = canvas.getContext("2d"); x.imageSmoothingEnabled = false;
      const giro = () => { if (!attivo || !canvas.isConnected) return; x.clearRect(0, 0, canvas.width, canvas.height); x.drawImage(fotogrammi[k % fotogrammi.length], 0, 0, canvas.width, canvas.height); k++; setTimeout(giro, 1000 / fps); };
      giro();
    })();
    return () => { attivo = false; };
  }
  /* Immagine per HUD e profilo: restituisce un data URL del busto. */
  async function ritratto(pg, scala = 3) { const c = document.createElement("canvas"); await disegna(c, pg, { ritratto: true, scala }); return c.toDataURL("image/png"); }

  /* ---------- Scelte offerte dal creatore ---------- */
  const elenco = (slot, corpo) => carica().then(() => CAT.slot[slot].filter(v => compatibile(v, corpo)));
  const palette = mat => Object.keys(CAT.palette[mat].rampe);
  const hexDi = (mat, nome) => rgb2hex(rampa(mat, nome)[Math.floor(rampa(mat, nome).length * 0.66)]);

  window.OLW_SPRITE = { carica, disegna, anima, ritratto, fotogramma, elenco, palette, hexDi, catalogo: () => CAT, compatibile };
})();
