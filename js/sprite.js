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
     Fogli 512×160 di celle 32×32: 4 colori da 4 colonne; righe 0 = destra, 1 = su, 2 = giù, 3 = sinistra. Colonne 0–2 = passi, 3 = sdraiato. */
  const ANIMALI = {
    gatto: { nome: "Gatto", file: "assets/pets/gatto.png", colori: ["bianco", "dorato", "rosso", "nero"] },
    cane: { nome: "Cane", file: "assets/pets/cane.png", colori: ["bianco", "marrone", "dorato", "nero"] },
    scimmia: { nome: "Scimmia", file: "assets/pets/scimmia.png", colori: ["marrone", "dorato", "grigio", "nero"] },
    /* Volanti: colonne 0–2 = battito d'ali, 3 = posato a terra. Volano accanto alla spalla dell'eroe; quando si ferma il corvo si posa a terra, il pipistrello si appende a testa in giù. */
    corvo: { nome: "Corvo", file: "assets/pets/corvo.png", colori: ["nero", "blu", "grigio", "bianco"], vola: true },
    pipistrello: { nome: "Pipistrello", file: "assets/pets/pipistrello.png", colori: ["viola", "nero", "marrone", "argento"], vola: true, appeso: true }
  };
  const fogli = new Map();
  const foglio = f => { if (!fogli.has(f)) fogli.set(f, new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => no(new Error("manca " + f)); i.src = f; })); return fogli.get(f); };
  function animaPet(canvas, pet, { riga = 0, scala = 3, fps = 5, fermo = false } = {}) {
    let attivo = true; const A = ANIMALI[pet && pet.specie]; if (!A) return () => {};
    const rid = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches, c0 = Math.max(0, Math.min(3, pet.col | 0)) * 4;
    foglio(A.file).then(img => {
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
        foglio(A.file).then(i => { imgPet = i; }).catch(() => {});
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
            const vola = o.A && o.A.vola && (st.vol || 0) > 0.15, c0 = Math.max(0, Math.min(3, (a.pet.col | 0))) * 4, cc = inMoto || vola ? [0, 1, 2, 1][Math.floor(t / (vola ? 110 : 160)) % 4] : 3, kp = r + "_" + cc;
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

  window.OLW_SPRITE = { abita, emozione, emoAttiva, facce, set alFinireEmo(fn) { alFinireEmo = fn; }, provaDialogo(tipo) { prossimoTipo = tipo; for (const d of Object.values(DIALOGO)) if (d.fase === "attesa") d.prossima = 0; }, pezzoSolo, ANIMALI, animaPet, carica, disegna, anima, ritratto, fotogramma, elenco, palette, hexDi, catalogo: () => CAT, compatibile };
})();
