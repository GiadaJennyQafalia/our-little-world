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
  const COPRE_CAPELLI = new Set(["hood", "barbuta", "bascinet", "greathelm", "armet", "close", "sugarloaf", "nasal", "norman", "spangen", "pointed", "kettle", "morion", "legion_h", "viking", "horned"]);
  const pezzo = (slot, id) => id && CAT.slot[slot] && CAT.slot[slot].find(v => v.id === id);
  const colDi = x => (x && typeof x === "object" ? x.col : null);
  const idDi = x => (x && typeof x === "object" ? x.id : x);
  const fa = (slot, pg) => pezzo(slot, idDi(pg[slot]));
  const compatibile = (voce, corpo) => !!(voce && voce.corpi[corpo] && voce.corpi[corpo].walk);
  /* Elenco dei livelli da disegnare, ordinati dal fondo alla cima: { f, z, mats } */
  function livelli(pg, solo) {
    const corpo = pg.corpo === "male" ? "male" : "female", L = [];
    const aggiungi = (voce, mats, col, slot) => {
      if (!compatibile(voce, corpo)) return;
      const va = voce.varianti ? (voce.varianti.includes(col) ? col : voce.varianti[0]) : null;
      for (const l of voce.corpi[corpo].walk) L.push({ f: va ? l.f.replace("{v}", va) : l.f, z: l.z, mats: va ? [] : mats, slot });
    };
    const pelle = pg.pelle || "light", occhi = pg.occhi || "blue";
    const capCol = colDi(pg.capelli) || "blonde";
    if (!solo) {
      aggiungi(CAT.fissi.corpo, [["body", pelle]]);
      aggiungi(corpo === "male" ? CAT.fissi.testa_m : CAT.fissi.testa_f, [["body", pelle], ["eye", occhi]]);
      aggiungi(CAT.fissi["sopracciglia_" + (pg.sopr === "thick" ? "thick" : "thin")], [["hair", capCol]]);
      const fc = pg.faccia && CAT.facce && CAT.facce[pg.faccia];
      if (fc && pg.faccia !== "neutral") aggiungi(fc, [["body", pelle], ["eye", occhi]]);
    }
    const mat = (voce, col) => !voce || !voce.materiale ? [] : [[voce.materiale, col || (voce.materiale === "body" ? pelle : voce.materiale === "hair" ? capCol : null)]].filter(m => m[1]);
    /* Cappucci ed elmi chiusi coprono tutta la testa: i capelli sotto non si disegnano, altrimenti spuntano dai bordi. */
    const cap = fa("cappello", pg), coperta = cap && COPRE_CAPELLI.has(cap.id);
    for (const slot of Object.keys(CAT.slot)) {
      const v = fa(slot, pg); if (!v || (coperta && slot === "capelli")) continue;
      aggiungi(v, mat(v, colDi(pg[slot])), colDi(pg[slot]), slot);
    }
    return L.map((l, i) => ({ ...l, i })).sort((a, b) => a.z - b.z || a.i - b.i);
  }

  /* Disegna un fotogramma 64×64: riga 0 = su, 1 = sinistra, 2 = giù, 3 = destra; colonna 0 = posa ferma, 1–8 = passi. */
  async function fotogramma(pg, riga, col, solo) {
    await carica();
    const L = livelli(pg, solo), fogli = await Promise.all(L.map(l => colorata(l.f, l.mats).catch(() => null)));
    const c = document.createElement("canvas"); c.width = F; c.height = F; const x = c.getContext("2d"); x.imageSmoothingEnabled = false;
    /* Con un cappello i capelli si tagliano sopra la tesa: in ogni colonna resta solo quello che pende sotto il cappello,
       così una pettinatura voluminosa non spunta sopra o ai lati della punta. */
    const hi = L.map((l, i) => l.slot === "cappello" && fogli[i] ? i : -1).filter(i => i >= 0);
    let fondo = null;
    if (hi.length && L.some(l => l.slot === "capelli")) {
      const hc = document.createElement("canvas"); hc.width = hc.height = F; const hx = hc.getContext("2d");
      hi.forEach(i => hx.drawImage(fogli[i], col * F, riga * F, F, F, 0, 0, F, F));
      const d = hx.getImageData(0, 0, F, F).data; fondo = new Array(F).fill(-1);
      for (let xx = 0; xx < F; xx++) for (let y = 0; y < F; y++) if (d[(y * F + xx) * 4 + 3] > 20) fondo[xx] = y;
      const ok = fondo.filter(v => v >= 0); if (!ok.length) fondo = null; else { const m = Math.min(...ok); fondo = fondo.map(v => v >= 0 ? v : m); }
    }
    fogli.forEach((s, i) => {
      if (!s) return;
      if (fondo && L[i].slot === "capelli") {
        const t = document.createElement("canvas"); t.width = t.height = F; const tx = t.getContext("2d");
        tx.drawImage(s, col * F, riga * F, F, F, 0, 0, F, F);
        for (let xx = 0; xx < F; xx++) if (fondo[xx] > 0) tx.clearRect(xx, 0, 1, fondo[xx] + 1);
        x.drawImage(t, 0, 0);
      } else x.drawImage(s, col * F, riga * F, F, F, 0, 0, F, F);
    });
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
    let attivo = true, k = 0;
    const rid = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    const cols = passi && !rid ? [1, 2, 3, 4, 5, 6, 7, 8] : [0];
    const batte = !rid && !OCCHI_CHIUSI.has(pg.faccia || "neutral"), chiusa = { ...pg, faccia: "closed" };
    (async () => {
      const fotogrammi = await Promise.all(cols.map(c => fotogramma(pg, riga, c)));
      const chiusi = batte ? await Promise.all(cols.map(c => fotogramma(chiusa, riga, c))) : null;
      canvas.width = F * scala; canvas.height = F * scala; const x = canvas.getContext("2d"); x.imageSmoothingEnabled = false;
      /* ogni tanto (circa ogni 4–5 secondi) sbatte le palpebre per un fotogramma */
      const giro = () => { if (!attivo || !canvas.isConnected) return; x.clearRect(0, 0, canvas.width, canvas.height); const i = k % fotogrammi.length; x.drawImage(chiusi && k % 37 === 36 ? chiusi[i] : fotogrammi[i], 0, 0, canvas.width, canvas.height); k++; setTimeout(giro, 1000 / fps); };
      giro();
    })();
    return () => { attivo = false; };
  }
  /* Un solo pezzo (per l'armadio): disegnato da solo, senza il corpo. */
  async function pezzoSolo(canvas, corpo, slot, sel, lato = 96) {
    const fr = await fotogramma({ corpo, pelle: "light", [slot]: sel }, 2, 0, true);
    const d = fr.getContext("2d").getImageData(0, 0, F, F).data; let x0 = F, y0 = F, x1 = -1, y1 = -1;
    for (let y = 0; y < F; y++) for (let x = 0; x < F; x++) if (d[(y * F + x) * 4 + 3] > 20) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
    canvas.width = lato; canvas.height = lato; const c = canvas.getContext("2d"); c.imageSmoothingEnabled = false; c.clearRect(0, 0, lato, lato);
    if (x1 < 0) return;
    const w = x1 - x0 + 1, h = y1 - y0 + 1, k = Math.max(1, Math.min(6, Math.floor((lato - 8) / Math.max(w, h))));
    c.drawImage(fr, x0, y0, w, h, Math.round((lato - w * k) / 2), Math.round((lato - h * k) / 2), w * k, h * k);
  }
  /* Immagine per HUD e profilo: restituisce un data URL del busto. */
  async function ritratto(pg, scala = 3) { const c = document.createElement("canvas"); await disegna(c, pg, { ritratto: true, scala }); return c.toDataURL("image/png"); }

  /* ---------- Scelte offerte dal creatore ---------- */
  const elenco = (slot, corpo) => carica().then(() => CAT.slot[slot].filter(v => compatibile(v, corpo)));
  const palette = mat => Object.keys(CAT.palette[mat].rampe);
  const hexDi = (mat, nome) => rgb2hex(rampa(mat, nome)[Math.floor(rampa(mat, nome).length * 0.66)]);

  /* ---------- Animali ----------
     Fogli 512×160 di celle 32×32: 4 colori da 4 colonne; righe 0 = destra, 1 = su, 2 = giù, 3 = sinistra. Colonne 0–2 = passi, 3 = sdraiato.
     I primi 4 colori sono disegnati nel foglio; gli altri ("extra") nascono dal primo cambiando le tinte una per una (cambio di palette:
     i fogli usano pochissimi colori, quindi il risultato resta pulito). Gli occhi sono pixel noti, ricolorati a richiesta.
     Il pezzo finale (4 colonne di un solo colore, con gli occhi scelti) si costruisce una volta e resta in memoria. */
  const E = (nome, hex, ...t) => ({ nome, hex, t });
  const BASE_FELINO = ["#efe9e7", "#b7b3b2", "#827c7c", "#d6b39d", "#bc8b6d"];
  const NASO_ROSSO = ["#ba6c4c", "#b14e45"], NASO_ROSA = ["#d6b39d", "#bc8b6d"];
  const felino = (nome, hex, c, naso) => E(nome, hex, c[0], c[1], c[2], naso[0], naso[1]);
  const ANIMALI = {
    gatto: { nome: "Gatto", file: "assets/pets/gatto.png", colori: ["bianco", "dorato", "rosso", "nero"], occhi: true,
      hexNativi: { bianco: "#f2f0ee", dorato: "#e0b24a", rosso: "#b5532f", nero: "#2b2b33" }, base: BASE_FELINO, extra: [
        felino("grigio", "#8e8c93", ["#a9a8ae", "#85838b", "#5c5a63"], NASO_ROSA), felino("arancio", "#d9802f", ["#e9913d", "#cc7326", "#9b4f18"], NASO_ROSSO),
        felino("cioccolato", "#5a382a", ["#6e4636", "#563526", "#3d2319"], NASO_ROSSO), felino("viola", "#7d5aa6", ["#9470bb", "#7552a0", "#553a7a"], NASO_ROSSO),
        felino("rosa", "#e48fb4", ["#f2adc9", "#d686a8", "#ab5f84"], NASO_ROSA), felino("azzurro", "#6fa4d0", ["#94c8ec", "#6fa4d0", "#4c7ca8"], NASO_ROSA)] },
    cane: { nome: "Cane", file: "assets/pets/cane.png", colori: ["bianco", "marrone", "dorato", "nero"], occhi: true,
      hexNativi: { bianco: "#f2f0ee", marrone: "#8a5430", dorato: "#e0b24a", nero: "#2b2b33" }, base: BASE_FELINO, extra: [
        felino("grigio", "#8e8c93", ["#a9a8ae", "#85838b", "#5c5a63"], NASO_ROSA), felino("arancio", "#d9802f", ["#e9913d", "#cc7326", "#9b4f18"], NASO_ROSSO),
        felino("crema", "#e6d4a8", ["#f1e1be", "#d8c096", "#b69a70"], NASO_ROSA), felino("viola", "#7d5aa6", ["#9470bb", "#7552a0", "#553a7a"], NASO_ROSSO),
        felino("rosa", "#e48fb4", ["#f2adc9", "#d686a8", "#ab5f84"], NASO_ROSA), felino("azzurro", "#6fa4d0", ["#94c8ec", "#6fa4d0", "#4c7ca8"], NASO_ROSA)] },
    scimmia: { nome: "Scimmia", file: "assets/pets/scimmia.png", colori: ["marrone", "dorato", "grigio", "nero"], occhi: true,
      hexNativi: { marrone: "#7a4a2a", dorato: "#c98b3a", grigio: "#8a8580", nero: "#40383e" },
      base: ["#7a4a2a", "#341c10", "#e2b48a", "#b98463", "#54301a"], extra: [
        E("bianco", "#ece6e0", "#ece6e0", "#8f8a86", "#f7d9c4", "#dbb9a2", "#bdb7b2"), E("arancio", "#cd6a2c", "#cd6a2c", "#5a2410", "#f1c48e", "#d19c6a", "#98431b"),
        E("crema", "#e8d6ac", "#e8d6ac", "#8a7554", "#f8eed6", "#dac6a0", "#c0aa80"), E("viola", "#7f5aa6", "#7f5aa6", "#2f1d48", "#e2c4da", "#ba93b2", "#55397a"),
        E("rosa", "#e592b4", "#e592b4", "#7a3a58", "#f9dbe3", "#daabbc", "#b3637f"), E("azzurro", "#6498c8", "#6498c8", "#1f3b5c", "#e6dccb", "#c2b4a0", "#426f9f")] },
    /* Volanti: colonne 0–2 = battito d'ali, 3 = posato a terra. Volano accanto alla spalla dell'eroe; quando si ferma il corvo si posa a terra, il pipistrello si appende a testa in giù. */
    corvo: { nome: "Corvo", file: "assets/pets/corvo.png", colori: ["nero", "blu", "grigio", "bianco"], vola: true, occhi: false,
      hexNativi: { nero: "#3a313a", blu: "#343b4c", grigio: "#767276", bianco: "#d4d3d4" },
      base: ["#302732", "#4b444c", "#3a313a", "#1d131e", "#cbba7b"], extra: [
        E("viola", "#5e467a", "#3a2850", "#5e467a", "#4a3562", "#241636", "#b090e0"), E("rosso", "#7e444c", "#4f2228", "#7e444c", "#62313a", "#2f1015", "#e08080"),
        E("verde", "#466e52", "#24402c", "#466e52", "#33523c", "#14261b", "#90d090"), E("rosa", "#8a6475", "#5a3a4a", "#8a6475", "#6e4a5a", "#3a2230", "#e8b0c8")] },
    pipistrello: { nome: "Pipistrello", file: "assets/pets/pipistrello.png", colori: ["viola", "nero", "marrone", "argento"], vola: true, appeso: true, occhi: true,
      hexNativi: { viola: "#6b4c8f", nero: "#2b2b33", marrone: "#8a5430", argento: "#cfcbd6" },
      base: ["#1d181e", "#432f53", "#5c436f", "#7784a2", "#5f5f7b", "#b572b1"], extra: [
        E("blu", "#3d6490", "#14202e", "#2c4a6a", "#3d6490", "#7fa6c8", "#5c82a8", "#9fc0e0"), E("rosso", "#7a3342", "#200f12", "#5c2230", "#7a3342", "#b8707c", "#9a5560", "#e09aa8"),
        E("verde", "#3d7a52", "#10201a", "#2c5a3e", "#3d7a52", "#80b08c", "#5c9068", "#a8d4b0"), E("arancio", "#9a6430", "#251912", "#7a4a22", "#9a6430", "#d0a070", "#b07f4a", "#e8c090")] }
  };
  for (const A of Object.values(ANIMALI)) { A.hex = { ...A.hexNativi }; for (const e of A.extra) { A.colori.push(e.nome); A.hex[e.nome] = e.hex; } A.nNativi = 4; }
  /* Colori degli occhi: due tonalità (chiara e scura); gli animali con un solo pixel per occhio usano la chiara. "" = come disegnati. */
  const OCCHI = { verde: ["#499231", "#006b46"], azzurro: ["#7cc4f4", "#2f78c0"], ambra: ["#f0b440", "#a8700c"], viola: ["#c08af0", "#7a42b8"], rosso: ["#f06060", "#a81c1c"] };
  /* Pixel degli occhi: "riga_colonna" → [[x, y, tonalità]]; la sagoma è uguale in tutti i colori, quindi vale per ognuno. */
  const OCCHI_PX = {"gatto":{"0_0":[[24,14,0],[24,15,1]],"0_1":[[24,13,0],[24,14,1]],"0_2":[[24,14,0],[24,15,1]],"2_0":[[14,18,0],[18,18,0],[14,19,1],[18,19,1]],"2_1":[[14,19,0],[18,19,0],[14,20,1],[18,20,1]],"2_2":[[14,18,0],[18,18,0],[14,19,1],[18,19,1]],"3_0":[[7,14,0],[7,15,1]],"3_1":[[7,13,0],[7,14,1]],"3_2":[[7,14,0],[7,15,1]],"4_0":[[14,19,0],[18,19,0],[14,20,1],[18,20,1]],"4_1":[[14,20,0],[18,20,0],[14,21,1],[18,21,1]]},"cane":{"0_0":[[24,14,0],[24,15,1]],"0_1":[[24,13,0],[24,14,1]],"0_2":[[24,14,0],[24,15,1]],"1_3":[[8,9,0],[8,10,1],[12,9,0],[12,10,1]],"2_0":[[14,18,0],[14,19,1],[18,18,0],[18,19,1]],"2_1":[[14,19,0],[14,20,1],[18,19,0],[18,20,1]],"2_2":[[14,19,0],[14,20,1],[18,19,0],[18,20,1]],"3_0":[[7,14,0],[7,15,1]],"3_1":[[7,13,0],[7,14,1]],"3_2":[[7,14,0],[7,15,1]],"4_0":[[14,19,0],[14,20,1],[18,19,0],[18,20,1]],"4_1":[[14,20,0],[14,21,1],[18,20,0],[18,21,1]]},"scimmia":{"0_0":[[21,13,0]],"0_1":[[21,13,0]],"0_2":[[21,13,0]],"0_3":[[18,13,0]],"2_0":[[14,12,0],[17,12,0]],"2_1":[[14,12,0],[17,12,0]],"2_2":[[14,12,0],[17,12,0]],"3_0":[[10,13,0]],"3_1":[[10,13,0]],"3_2":[[10,13,0]],"3_3":[[13,13,0]]},"pipistrello":{"0_0":[[23,17,0]],"0_1":[[23,15,0]],"0_2":[[23,14,0]],"0_3":[[13,21,0],[17,21,0]],"1_3":[[13,21,0],[17,21,0]],"2_0":[[14,14,0],[18,14,0]],"2_1":[[14,15,0],[18,15,0]],"2_2":[[14,17,0],[18,17,0]],"2_3":[[13,21,0],[17,21,0]],"3_0":[[8,17,0]],"3_1":[[8,15,0]],"3_2":[[8,14,0]],"3_3":[[13,21,0],[17,21,0]]}};
  const rgbDi = h => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
  const fogli = new Map();
  const foglio = f => { if (!fogli.has(f)) fogli.set(f, new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => no(new Error("manca " + f)); i.src = f; })); return fogli.get(f); };
  /* Il foglio con tutti i colori: i 4 disegnati e, di seguito, i blocchi extra ottenuti cambiando le tinte del primo. */
  const estesi = new Map();
  const foglioEsteso = specie => {
    if (!estesi.has(specie)) estesi.set(specie, foglio(ANIMALI[specie].file).then(img => {
      const A = ANIMALI[specie], c = document.createElement("canvas"); c.width = 512 + A.extra.length * 128; c.height = 256;
      const x = c.getContext("2d", { willReadFrequently: true }); x.imageSmoothingEnabled = false; x.drawImage(img, 0, 0);
      A.extra.forEach((e, k) => {
        const blocco = x.getImageData(0, 0, 128, 256), d = blocco.data, m = new Map();
        A.base.forEach((b, i) => { const [r, g, bl] = rgbDi(b), [r2, g2, b2] = rgbDi(e.t[i]); m.set((r << 16) | (g << 8) | bl, [r2, g2, b2]); });
        for (let p = 0; p < d.length; p += 4) { if (!d[p + 3]) continue; const n = m.get((d[p] << 16) | (d[p + 1] << 8) | d[p + 2]); if (n) { d[p] = n[0]; d[p + 1] = n[1]; d[p + 2] = n[2]; } }
        x.putImageData(blocco, 512 + k * 128, 0);
      });
      return c;
    }));
    return estesi.get(specie);
  };
  /* Il pezzo di un animale: 4 colonne (passi e sdraiato) di un solo colore, con gli occhi scelti. Promessa di { img, c0 } (c0 = prima colonna). */
  /* ---------- Accessori degli animali ----------
     Disegnati in codice sopra ogni fotogramma, agganciati alla testa (punto-occhi) di ogni posa. Un accessorio sta in uno "slot":
     collo (collare, fiocco), testa (cappello). Per aggiungerne altri (ali, mantelline: slot "schiena") basta una voce in ACCESSORI,
     una funzione in DISEGNA_ACC e, se serve, l'ancora nello stesso GEO. pet.acc = { collo: {id, col}, testa: {id, col} }. */
  const COLORI_ACC = { rosso: ["#c23b3b", "#7e1f1f", "#ee7a7a"], blu: ["#3b6fc2", "#22427a", "#7aa6ee"], verde: ["#3f9a52", "#245c30", "#82d494"], viola: ["#8a4fc2", "#53307c", "#be8af0"], oro: ["#e0b24a", "#9a6f1a", "#f6dc8a"], rosa: ["#e86aa6", "#a03468", "#f6a6cc"], nero: ["#34343e", "#17171d", "#6a6a78"] };
  const SLOT_ACC = { testa: "Testa", viso: "Viso", collo: "Collo" };
  const ACCESSORI = {
    collare: { slot: "collo", nome: "Collare", col: "rosso" }, fiocco: { slot: "collo", nome: "Fiocco", col: "blu" }, sciarpa: { slot: "collo", nome: "Sciarpa", col: "rosso" },
    campanellino: { slot: "collo", nome: "Campanellino", col: "verde" }, medaglione: { slot: "collo", nome: "Medaglione", col: "viola" },
    strega: { slot: "testa", nome: "Cappello da strega", col: "viola" }, corona: { slot: "testa", nome: "Corona", col: "oro" }, occhiali: { slot: "viso", nome: "Occhiali", col: "nero" }
  };
  const ORDINE_ACC = ["schiena", "collo", "viso", "testa"];
  /* Punto-occhi di ogni posa (riga 0 = verso destra, 2 = di fronte; la 3 è la 0 specchiata, la 1 è la 2 vista da dietro). s = di lato, f = di fronte; g = pipistrello appeso. */
  const ANCORE = {
    gatto: { s: [[24, 14.5], [24, 13.5], [24, 14.5], [25, 13.5]], f: [[16, 18.5], [16, 19.5], [16, 18.5]] },
    cane: { s: [[24, 14.5], [24, 13.5], [24, 14.5], [25, 14.5]], f: [[16, 18.5], [16, 19.5], [16, 19.5]] },
    scimmia: { s: [[21, 13], [21, 13], [21, 13], [21, 13]], f: [[15.5, 12], [15.5, 12], [15.5, 12]] },
    corvo: { s: [[23, 15], [22, 15], [22, 13], [23, 13]], f: [[16, 14], [16, 13], [16, 13]] },
    pipistrello: { s: [[23, 17], [23, 15], [23, 14]], f: [[16, 14], [16, 15], [16, 17]], g: [16, 21] }
  };
  /* Quanto distano cappello (t = base della tesa) e collo (c) dal punto-occhi. Di lato: c = [dx, da y, a y]; di fronte/dietro: c = [dy, mezza larghezza]. */
  const GEO = {
    gatto: { cap: "g", s: { t: [-1, -3], c: [-5, 1, 5] }, f: { t: [0, -8], c: [4, 5] }, b: { t: [0, -10], c: [-3, 5] } },
    cane: { cap: "g", s: { t: [-1, -3], c: [-5, 1, 5] }, f: { t: [0, -8], c: [4, 5] }, b: { t: [0, -10], c: [-3, 5] } },
    scimmia: { cap: "g", dc: -2, s: { t: [-1, -2], c: [-4, 2, 7] }, f: { t: [0, -3], c: [4, 4] }, b: { t: [0, -3], c: [4, 4] } },
    corvo: { cap: "p", s: { t: [-1, -2], c: [-4, 1, 5] }, f: { t: [0, -3], c: [1, 2] }, b: { t: [0, -3], c: [1, 2] } },
    pipistrello: { cap: "p", s: { t: [-1, -3], c: [-4, -1, 4] }, f: { t: [0, -5], c: [3, 3] }, b: { t: [0, -5], c: [3, 3] }, g: { t: [0, 4], c: [3, 3] } }
  };
  const CAPPELLO = {
    g: ["......cc...", ".....ccc...", ".....cccc..", "....ccccc..", "...ccccccc.", "...bbbbbbb.", "ddddddddddd", ".ddddddddd."],
    p: ["...cc..", "..ccc..", ".bbbbb.", "ddddddd", ".ddddd."]
  };
  const FIOCCO = ["cc.cc", "ccdcc", "cc.cc"];
  const CORONA = {
    g: ["c...c...c", "cc.ccc.cc", "ccccgcccc", "ddddddddd"],
    p: ["c..c..c", "ccccccc", "cccgccc", "ddddddd"]
  };
  /* Fascia attorno al collo che segue la sagoma (colora solo pixel dell'animale). colori = righe/colonne dello spessore; ritorna lo spessore. */
  function banda(x, op, g, colori, ext) {
    const sp = colori.length;
    if (g.dir === "s") {
      const x0 = Math.round(g.ax + g.sign * g.geo.c[0]);
      for (let y = Math.round(g.ay + g.geo.c[1]); y <= Math.round(g.ay + g.geo.c[2]); y++) for (let k = 0; k < sp; k++) { const px = x0 - g.sign * k; if (op(px, y)) { x.fillStyle = colori[k]; x.fillRect(g.ox + px, g.oy + y, 1, 1); } }
      if (ext) { const ym = Math.round(g.ay + g.geo.c[2]); if (op(x0, ym + 1)) { x.fillStyle = ext; x.fillRect(g.ox + x0, g.oy + ym + 1, 1, 1); } }
    } else {
      const y0 = Math.round(g.ay + g.geo.c[0]), hw = g.geo.c[1];
      for (let k = 0; k < sp; k++) for (let px = Math.round(g.ax - hw); px <= Math.round(g.ax + hw); px++) if (op(px, y0 + k)) { x.fillStyle = colori[k]; x.fillRect(g.ox + px, g.oy + y0 + k, 1, 1); }
      if (ext && g.dir === "f" && op(Math.round(g.ax), y0 + 2)) { x.fillStyle = "#f6dc8a"; x.fillRect(g.ox + Math.round(g.ax), g.oy + y0 + 2, 1, 1); }
    }
    return sp;
  }
  /* Punto appena sotto la fascia, dove pendono campanellino e medaglione. */
  function puntoGiu(g, spess) {
    if (g.dir === "s") return [Math.round(g.ax + g.sign * g.geo.c[0]) + (g.sign > 0 ? 1 : -2), Math.round(g.ay + g.geo.c[2]) + 1];
    return [Math.round(g.ax) - 1, Math.round(g.ay + g.geo.c[0]) + spess];
  }
  const DISEGNA_ACC = {
    collare(x, op, g, c) { banda(x, op, g, [c[0], c[1]], c[2]); },
    sciarpa(x, op, g, c) {
      const sp = banda(x, op, g, [c[0], c[1], c[0]], null);
      let tx, ty;
      if (g.dir === "s") { tx = Math.round(g.ax + g.sign * g.geo.c[0]) - g.sign * (sp + 1); ty = Math.round(g.ay + g.geo.c[2]); } else { tx = Math.round(g.ax) + 2; ty = Math.round(g.ay + g.geo.c[0]) + sp; }
      for (let j = 0; j < 4; j++) for (let i = 0; i < 2; i++) { x.fillStyle = j % 2 ? c[1] : c[0]; x.fillRect(g.ox + tx + i, g.oy + ty + j, 1, 1); }
    },
    campanellino(x, op, g, c) {
      banda(x, op, g, [c[0], c[1]], null);
      const [bx, by] = puntoGiu(g, 2);
      x.fillStyle = "#f6dc8a"; x.fillRect(g.ox + bx, g.oy + by, 2, 1); x.fillStyle = "#e0b24a"; x.fillRect(g.ox + bx, g.oy + by + 1, 2, 1); x.fillStyle = "#9a6f1a"; x.fillRect(g.ox + bx + (g.sign > 0 ? 1 : 0), g.oy + by + 1, 1, 1);
    },
    medaglione(x, op, g, c) {
      if (g.dir === "b") return;
      banda(x, op, g, ["#e0b24a"], null);
      const [bx, by] = puntoGiu(g, 1);
      x.fillStyle = "#9a6f1a"; x.fillRect(g.ox + bx - 1, g.oy + by - 1, 4, 4); x.fillStyle = c[0]; x.fillRect(g.ox + bx, g.oy + by, 2, 2); x.fillStyle = c[2]; x.fillRect(g.ox + bx, g.oy + by, 1, 1);
    },
    corona(x, op, g, c) {
      const sp = CORONA[g.cap], w = sp[0].length, h = sp.length, bx = Math.round(g.ax + g.sign * g.geo.t[0]), by = Math.round(g.ay + g.geo.t[1]) + 1 + (g.dc || 0), gemma = c === COLORI_ACC.rosso ? COLORI_ACC.blu[0] : COLORI_ACC.rosso[0];
      sp.forEach((riga, j) => { for (let i = 0; i < w; i++) { const ch = riga[i]; if (ch === ".") continue; x.fillStyle = ch === "c" ? c[0] : ch === "g" ? gemma : c[1]; const yy = g.giu ? by + (h - 1 - j) : by - (h - 1 - j); x.fillRect(g.ox + bx - (w >> 1) + i, g.oy + yy, 1, 1); } });
    },
    occhiali(x, op, g, c) {
      if (g.dir === "b" || !g.occhi || !g.occhi.length) return;
      const gruppi = g.dir === "s" ? [g.occhi] : [g.occhi.filter(p => p[0] < g.ax), g.occhi.filter(p => p[0] >= g.ax)].filter(a => a.length);
      const colM = c === COLORI_ACC.nero ? "#7a7a8c" : c[0], px = (a, b) => { x.fillStyle = colM; x.fillRect(g.ox + a, g.oy + b, 1, 1); };
      const anelli = gruppi.map(a => ({ x0: Math.min(...a.map(p => p[0])) - 1, x1: Math.max(...a.map(p => p[0])) + 1, y0: Math.min(...a.map(p => p[1])) - 1, y1: Math.max(...a.map(p => p[1])) + 1 }));
      for (const r of anelli) for (let i = r.x0; i <= r.x1; i++) for (let j = r.y0; j <= r.y1; j++) if (i === r.x0 || i === r.x1 || j === r.y0 || j === r.y1) px(i, j);
      if (anelli.length === 2) { const y = Math.round((anelli[0].y0 + anelli[0].y1) / 2); for (let i = anelli[0].x1 + 1; i < anelli[1].x0; i++) px(i, y); }
      if (g.dir === "s") { const r = anelli[0]; for (let k = 1; k <= 3; k++) px(g.sign > 0 ? r.x0 - k : r.x1 + k, r.y0 + 1); }
    },
    fiocco(x, op, g, c) {
      if (g.dir === "b") return;
      const [m, sc] = c, cx = g.dir === "s" ? Math.round(g.ax + g.sign * g.geo.c[0]) + g.sign : Math.round(g.ax), cy = g.dir === "s" ? Math.round(g.ay + g.geo.c[2]) - 1 : Math.round(g.ay + g.geo.c[0]) + 1;
      FIOCCO.forEach((riga, j) => { for (let i = 0; i < 5; i++) { const ch = riga[i]; if (ch === ".") continue; x.fillStyle = ch === "c" ? m : sc; x.fillRect(g.ox + cx - 2 + i, g.oy + cy - 1 + j, 1, 1); } });
    },
    strega(x, op, g, c) {
      const sp = CAPPELLO[g.cap], w = sp[0].length, h = sp.length, bx = Math.round(g.ax + g.sign * g.geo.t[0]), by = Math.round(g.ay + g.geo.t[1]);
      const fascia = c === COLORI_ACC.oro ? COLORI_ACC.rosso[0] : COLORI_ACC.oro[0];
      sp.forEach((riga, j) => { for (let i = 0; i < w; i++) { const ch = riga[i]; if (ch === ".") continue; x.fillStyle = ch === "c" ? c[0] : ch === "b" ? fascia : c[1]; const yy = g.giu ? by + (h - 1 - j) : by - (h - 1 - j); x.fillRect(g.ox + bx - (w >> 1) + i, g.oy + yy, 1, 1); } });
    }
  };
  /* Pixel degli occhi di una posa (per gli occhiali); il corvo non ne ha, li ricavo dalla testa. */
  function occhiCella(specie, r, c, dir, pt) {
    const e = OCCHI_PX[specie] && OCCHI_PX[specie][r + "_" + c];
    if (e) return e.map(p => [p[0], p[1]]);
    if (specie === "corvo") return dir === "s" ? [[Math.round(pt[0] + (r === 3 ? 1 : -1)), Math.round(pt[1]) - 1]] : [[Math.round(pt[0]) - 2, Math.round(pt[1])], [Math.round(pt[0]) + 2, Math.round(pt[1])]];
    return null;
  }
  function applicaAccessori(x, pet) {
    const im = x.getImageData(0, 0, 128, 256).data, geo = GEO[pet.specie], anc = ANCORE[pet.specie];
    if (!geo || !anc) return;
    for (const slot of ORDINE_ACC) {
      const a = pet.acc && pet.acc[slot], def = a && ACCESSORI[a.id]; if (!def || def.slot !== slot) continue;
      const col = COLORI_ACC[a.col] || COLORI_ACC.rosso;
      for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) {
        const lato = r === 0 || r === 3, sign = r === 3 ? -1 : 1;
        let dir = lato ? "s" : r === 1 ? "b" : "f", pt, giu = false, gm = geo[dir];
        if (pet.specie === "pipistrello" && c === 3 && lato) { dir = "f"; pt = anc.g; giu = true; gm = geo.g; }
        else { pt = (lato ? anc.s : anc.f)[c]; if (!pt) continue; if (lato && r === 3) pt = [31 - pt[0], pt[1]]; }
        const op = (px, py) => px >= 0 && px < 32 && py >= 0 && py < 32 && im[(((r * 32) + py) * 128 + c * 32 + px) * 4 + 3] > 0;
        DISEGNA_ACC[a.id](x, op, { occhi: occhiCella(pet.specie, r, c, dir, pt), ox: c * 32, oy: r * 32, ax: pt[0], ay: pt[1], sign: dir === "s" ? sign : 1, dir, geo: gm, cap: geo.cap, dc: geo.dc, giu }, col);
      }
    }
  }
  const blocchiPet = new Map();
  function sheetPet(pet) {
    const A = ANIMALI[pet.specie], col = Math.max(0, Math.min(A.colori.length - 1, pet.col | 0)), occ = A.occhi && OCCHI[pet.occhi] ? pet.occhi : "", accs = pet.acc ? JSON.stringify(pet.acc) : "", chiave = pet.specie + "|" + col + "|" + occ + "|" + accs;
    if (!blocchiPet.has(chiave)) blocchiPet.set(chiave, foglioEsteso(pet.specie).then(sheet => {
      const c = document.createElement("canvas"); c.width = 128; c.height = 256;
      const x = c.getContext("2d", { willReadFrequently: true }); x.imageSmoothingEnabled = false;
      const sx = col < 4 ? col * 128 : 512 + (col - 4) * 128; x.drawImage(sheet, sx, 0, 128, 256, 0, 0, 128, 256);
      if (occ) {
        const im = x.getImageData(0, 0, 128, 256), d = im.data, t = OCCHI[occ], px = OCCHI_PX[pet.specie] || {};
        for (const k in px) { const [r, cc] = k.split("_").map(Number); for (const [ex, ey, ton] of px[k]) { const o = ((r * 32 + ey) * 128 + cc * 32 + ex) * 4; if (!d[o + 3]) continue; const [R, G, B] = rgbDi(t[Math.min(ton, t.length - 1)]); d[o] = R; d[o + 1] = G; d[o + 2] = B; } }
        x.putImageData(im, 0, 0);
      }
      if (accs) applicaAccessori(x, pet);
      return c;
    }));
    return blocchiPet.get(chiave).then(img => ({ img, c0: 0 }));
  }
  function animaPet(canvas, pet, { riga = 0, scala = 3, fps = 5, fermo = false } = {}) {
    let attivo = true; const A = ANIMALI[pet && pet.specie]; if (!A) return () => {};
    const rid = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    sheetPet(pet).then(({ img, c0 }) => {
      canvas.width = 32 * scala; canvas.height = 32 * scala; const x = canvas.getContext("2d"); x.imageSmoothingEnabled = false; let k = 0; const seq = [0, 1, 2, 1];
      const giro = () => {
        if (!attivo || !canvas.isConnected) return;
        x.clearRect(0, 0, canvas.width, canvas.height);
        const col = fermo || rid ? 1 : seq[k++ % 4];
        x.drawImage(img, (c0 + col) * 32, riga * 32, 32, 32, 0, 0, canvas.width, canvas.height);
        if (!(fermo || rid)) setTimeout(giro, 1000 / fps);
      };
      giro();
    }).catch(e => console.warn("animale", e));
    return () => { attivo = false; };
  }


  /* ---------- Espressioni ----------
     pg.faccia = id di catalogo.facce (strato sopra la testa). Le emozioni a tempo (es. felice dopo una missione) valgono per tutte le viste. */
  const EMO = {}, OCCHI_CHIUSI = new Set(["happy", "happy2", "closed"]);
  let alFinireEmo = null;
  function emozione(id, faccia, ms = 6000) {
    EMO[id] = { faccia, fino: Date.now() + ms };
    setTimeout(() => { if (EMO[id] && EMO[id].fino <= Date.now()) { delete EMO[id]; if (alFinireEmo) alFinireEmo(id); } }, ms + 60);
  }
  const emoAttiva = id => (EMO[id] && EMO[id].fino > Date.now() ? EMO[id].faccia : null);
  const facce = () => (CAT && CAT.facce) || {};

  /* ---------- Abitanti: gli eroi (e i loro animali) che passeggiano nel pavimento delle stanze ----------
     host = contenitore posizionato sopra l'immagine; w/h = dimensioni dell'immagine in pixel;
     abitanti = [{ id, pg, pet, x0, x1, y, scala, stanza, faccia, spavento }]
     faccia = espressione di base (preferita, o l'umore della stanza); spavento = sguardo che scatta tra stupore e occhiate ai lati.
     Le coordinate sono in pixel dell'immagine (x = centro dei piedi, y = linea dei piedi) e vengono trasformate in percentuali.
     Se due eroi sono nella stessa stanza, ogni tanto si avvicinano e chiacchierano, si sorridono o litigano. */
  const FC = new Map(), FSYNC = new Map(), STATO = {}, DIALOGO = {};
  let giroAbitanti = 0;
  async function fotoC(pg, riga, col) {
    const k = JSON.stringify(pg) + "|" + riga + "|" + col;
    if (!FC.has(k)) FC.set(k, fotogramma(pg, riga, col).then(f => { FSYNC.set(k, f); return f; }));
    return FC.get(k);
  }
  let prossimoTipo = null; /* solo per le prove: forza il prossimo dialogo */
  const TIPI_DIALOGO = [["chiacchiera", 0.45], ["sorriso", 0.3], ["litigio", 0.25]];
  const FUMETTO = { chiacchiera: "…", sorriso: "♥", litigio: "#!" };
  function abita(host, w, h, abitanti) {
    cancelAnimationFrame(giroAbitanti);
    const rid = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    const pc = (v, t) => (v / t * 100).toFixed(3) + "%";
    const PIEDI = 60, PIEDI_PET = 29, VEL = 38, FPS = 9;
    const lista = abitanti.filter(a => a && a.pg).map(a => {
      const ch = a.id + "@" + (a.vista || ""), st = STATO[ch] || (STATO[ch] = {});
      const nuovaStanza = st.stanza !== a.stanza;
      if (nuovaStanza || st.x == null || st.x < a.x0 || st.x > a.x1) { st.x = a.x0 + Math.random() * (a.x1 - a.x0); st.stanza = a.stanza; st.meta = null; st.fermoFino = performance.now() + 800; st.px = null; st.inDialogo = false; st.guarda = null; }
      const cv = document.createElement("canvas"); cv.width = F; cv.height = F; cv.className = "abit-eroe" + (nuovaStanza ? " nuovo" : ""); cv.setAttribute("aria-hidden", "true");
      cv.style.width = pc(F * a.scala, w); host.appendChild(cv);
      const fum = document.createElement("span"); fum.className = "abit-fumetto"; fum.hidden = true; fum.setAttribute("aria-hidden", "true"); host.appendChild(fum);
      let pcv = null, A = null, imgPet = null;
      if (a.pet && ANIMALI[a.pet.specie]) {
        A = ANIMALI[a.pet.specie]; pcv = document.createElement("canvas"); pcv.width = 32; pcv.height = 32; pcv.className = "abit-pet" + (nuovaStanza ? " nuovo" : ""); pcv.setAttribute("aria-hidden", "true");
        pcv.style.width = pc(32 * a.scala, w); host.appendChild(pcv);
        sheetPet(a.pet).then(r => { imgPet = r.img; }).catch(() => {});
      }
      if (st.px == null) st.px = st.x;
      const base = a.faccia || a.pg.faccia || "neutral", fr = {}, chiesti = new Set();
      const pgF = fc => ({ ...a.pg, faccia: fc });
      for (const r of [1, 2, 3]) for (let c = 0; c <= 8; c++) { const f = FSYNC.get(JSON.stringify(pgF(base)) + "|" + r + "|" + c); if (f) fr[base + "|" + r + "_" + c] = f; }
      const dai = (fc, r, c) => { const k = fc + "|" + r + "_" + c; if (chiesti.has(k)) return; chiesti.add(k); fotoC(pgF(fc), r, c).then(f => { fr[k] = f; }).catch(() => {}); };
      return { a, st, cv, fum, pcv, A, get imgPet() { return imgPet; }, base, fr, dai, ultimoF: null };
    });
    /* Carica i fotogrammi: prima la posa ferma, poi i passi, poi gli occhi chiusi per il battito delle palpebre. */
    for (const o of lista) {
      o.dai(o.base, 2, 0);
      if (!rid) { for (const r of [1, 3, 2]) for (let c = 1; c <= 8; c++) o.dai(o.base, r, c); for (const r of [2, 1, 3]) o.dai("closed", r, 0); }
      if (o.a.spavento) for (const fc of ["shock", "look_l", "look_r"]) o.dai(fc, 2, 0);
    }
    /* Coppie nella stessa stanza (esattamente due eroi). */
    const perStanza = {};
    for (const o of lista) (perStanza[o.a.stanza] = perStanza[o.a.stanza] || []).push(o);
    const coppie = Object.values(perStanza).filter(g => g.length === 2).map(g => {
      const k = g.map(o => o.a.id).sort().join("+") + "@" + g[0].a.stanza + "@" + (g[0].a.vista || "");
      const d = DIALOGO[k] || (DIALOGO[k] = { fase: "attesa", prossima: performance.now() + 5000 + Math.random() * 9000 });
      for (const o of g) for (const fc of ["happy", "happy2", "anger", "angry2"]) for (const r of [1, 3]) o.dai(fc, r, 0);
      return { g, d };
    });
    const dialoga = t => {
      for (const { g, d } of coppie) {
        const [s, x] = g[0].st.x <= g[1].st.x ? g : [g[1], g[0]];
        if (d.fase === "attesa") {
          if (rid || t < d.prossima || s.st.meta != null || x.st.meta != null) continue;
          let r = Math.random(); d.tipo = prossimoTipo || TIPI_DIALOGO.find(([, p]) => (r -= p) < 0)[0]; prossimoTipo = null;
          s.st.inDialogo = x.st.inDialogo = true;
          /* si fermano a un passo l'uno dall'altro, senza sovrapporsi */
          const mezzo = (s.a.x1 + x.a.x0) / 2, gap = 18 * Math.max(s.a.scala, x.a.scala);
          s.st.meta = Math.max(s.a.x0, Math.min(s.a.x1, mezzo - gap)); x.st.meta = Math.max(x.a.x0, Math.min(x.a.x1, mezzo + gap)); d.fase = "avvicina"; d.limite = t + 9000;
        } else if (d.fase === "avvicina") {
          if ((s.st.meta == null && x.st.meta == null) || t > d.limite) { s.st.meta = x.st.meta = null; s.st.guarda = 3; x.st.guarda = 1; d.fase = "parla"; d.inizio = t; d.fino = t + 5500; }
        } else if (d.fase === "parla" && t > d.fino) {
          for (const o of g) { o.st.inDialogo = false; o.st.guarda = null; o.st.fermoFino = t + 1200 + Math.random() * 1500; o.fum.hidden = true; }
          d.fase = "attesa"; d.prossima = t + 18000 + Math.random() * 25000;
        }
      }
    };
    const facciaDialogo = (o, t) => {
      const c = coppie.find(c => c.g.includes(o)); if (!c || c.d.fase !== "parla") return null;
      const turno = Math.floor((t - c.d.inizio) / 1100) % 2, parla = c.g.indexOf(o) === turno;
      return { tipo: c.d.tipo, parla, faccia: c.d.tipo === "sorriso" ? "happy2" : c.d.tipo === "litigio" ? (parla ? "angry2" : "anger") : (parla ? "neutral" : "happy") };
    };
    let t0 = performance.now();
    const passo = t => {
      if (!host.isConnected) return;
      const dt = Math.min(0.1, (t - t0) / 1000); t0 = t;
      dialoga(t);
      for (const o of lista) {
        const { a, st } = o;
        if (!rid) {
          if (st.meta != null) {
            const d = st.meta - st.x, mv = Math.min(Math.abs(d), VEL * dt);
            st.x += Math.sign(d) * mv; st.dir = d > 0 ? 3 : 1;
            if (Math.abs(st.meta - st.x) < 0.5) { st.meta = null; st.fermoFino = t + 1500 + Math.random() * 3500; st.dir = 2; }
          } else if (!st.inDialogo && t >= (st.fermoFino || 0) && a.x1 - a.x0 > 30) {
            let m = a.x0 + Math.random() * (a.x1 - a.x0); if (Math.abs(m - st.x) < 25) m = st.x < (a.x0 + a.x1) / 2 ? a.x1 : a.x0; st.meta = m;
          }
        }
        const moto = st.meta != null, riga = moto ? st.dir : (st.guarda || 2), col = moto ? 1 + Math.floor(t / (1000 / FPS)) % 8 : 0;
        /* Espressione: emozione a tempo > dialogo > spavento > espressione di base; da fermo ogni tanto sbatte le palpebre. */
        let faccia = o.base;
        if (a.spavento) faccia = ["shock", "shock", "look_l", "shock", "look_r"][Math.floor(t / 650) % 5];
        const dl = facciaDialogo(o, t); if (dl) faccia = dl.faccia;
        const ev = emoAttiva(a.id); if (ev) faccia = ev;
        if (!moto && !rid && !OCCHI_CHIUSI.has(faccia)) {
          if (t > (st.batti || 0)) { st.battiFine = t + 150; st.batti = t + 2500 + Math.random() * 4000; }
          if (t < st.battiFine) faccia = "closed";
        }
        let f = o.fr[faccia + "|" + riga + "_" + col];
        if (!f) { o.dai(faccia, riga, col); f = o.fr[o.base + "|" + riga + "_" + col] || o.fr[o.base + "|2_0"]; }
        if (f && o.ultimoF !== f) { const x = o.cv.getContext("2d"); x.clearRect(0, 0, F, F); x.drawImage(f, 0, 0); o.ultimoF = f; }
        const yE = a.y;
        o.cv.style.left = pc(st.x - F * a.scala / 2, w); o.cv.style.top = pc(yE - PIEDI * a.scala, h); o.cv.style.zIndex = Math.round(yE);
        /* Fumetto sopra la testa di chi parla (o di entrambi, se si sorridono). */
        const mostra = dl && (dl.parla || dl.tipo === "sorriso");
        if (mostra) {
          if (o.fum.hidden || o.fum.dataset.t !== dl.tipo) { o.fum.hidden = false; o.fum.dataset.t = dl.tipo; o.fum.textContent = FUMETTO[dl.tipo]; }
          o.fum.style.left = pc(st.x, w); o.fum.style.top = pc(yE - 50 * a.scala, h); o.fum.style.zIndex = Math.round(yE) + 5;
        } else if (!o.fum.hidden) o.fum.hidden = true;
        if (o.pcv) {
          const verso = moto ? (st.dir === 3 ? 1 : -1) : (st.pverso || 1), meta = st.x - verso * 34 * a.scala / 2;
          st.px += (meta - st.px) * Math.min(1, dt * 2.4);
          const inMoto = Math.abs(meta - st.px) > 2 && !rid, r = st.px < meta - 2 ? 0 : st.px > meta + 2 ? 3 : (verso > 0 ? 0 : 3);
          if (moto) st.pverso = verso;
          if (o.imgPet) {
            const vola = o.A && o.A.vola && (st.vol || 0) > 0.15, c0 = 0, cc = inMoto || vola ? [0, 1, 2, 1][Math.floor(t / (vola ? 110 : 160)) % 4] : 3, kp = r + "_" + cc;
            if (o.ultimoP !== kp) { const x = o.pcv.getContext("2d"); x.imageSmoothingEnabled = false; x.clearRect(0, 0, 32, 32); x.drawImage(o.imgPet, (c0 + cc) * 32, r * 32, 32, 32, 0, 0, 32, 32); o.ultimoP = kp; }
          }
          /* Gli animali che volano salgono all'altezza della spalla quando l'eroe cammina e scendono a terra quando si ferma. */
          let su = 0;
          if (o.A && o.A.vola) {
            const meta = inMoto || moto ? 1 : 0; st.vol = (st.vol || 0) + (meta - (st.vol || 0)) * Math.min(1, dt * 3);
            su = st.vol * (30 + Math.sin(t / 260) * 2.5) * a.scala;
            if (o.A.appeso) su += (1 - st.vol) * 38 * a.scala; /* a riposo il pipistrello resta in alto, appeso a testa in giù */
          }
          o.pcv.style.left = pc(st.px - 16 * a.scala, w); o.pcv.style.top = pc(yE + 4 - PIEDI_PET * a.scala - su, h); o.pcv.style.zIndex = Math.round(yE) + (su > 1 ? 3 : 1);
        }
      }
      giroAbitanti = requestAnimationFrame(passo);
    };
    giroAbitanti = requestAnimationFrame(passo);
  }

  window.OLW_SPRITE = { abita, emozione, emoAttiva, facce, set alFinireEmo(fn) { alFinireEmo = fn; }, provaDialogo(tipo) { prossimoTipo = tipo; for (const d of Object.values(DIALOGO)) if (d.fase === "attesa") d.prossima = 0; }, pezzoSolo, ANIMALI, OCCHI_PET: OCCHI, COLORI_ACC, SLOT_ACC, ACCESSORI, sheetPet, animaPet, carica, disegna, anima, ritratto, fotogramma, elenco, palette, hexDi, catalogo: () => CAT, compatibile };
})();
