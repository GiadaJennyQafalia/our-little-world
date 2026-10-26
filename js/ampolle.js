/* Our little world · ampolle dello sgabuzzino
   Cinque forme disegnate a pixel (14 colonne) e riempite a livello: pieno, metà, quasi finito, finito.
   '#' vetro · 'g' interno (si riempie dal basso) · 'c' tappo di sughero · 'h' erogatore dello spray */
(function () {
  "use strict";
  const FORME = {
    tonda: { nome: "Ampolla", m: [
      "....cccccc....", "....cccccc....", ".....#gg#.....", ".....#gg#.....", "....#gggg#....", "...#gggggg#...", "..#gggggggg#..", ".#gggggggggg#.", ".#gggggggggg#.",
      "#gggggggggggg#", "#gggggggggggg#", "#gggggggggggg#", "#gggggggggggg#", ".#gggggggggg#.", ".#gggggggggg#.", "..#gggggggg#..", "...#gggggg#...", "....######...."] },
    fiala: { nome: "Fiala", m: [
      "....cccccc....", "....cccccc....", "...########...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...",
      "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...#gggggg#...", "...########..."] },
    beuta: { nome: "Beuta", m: [
      ".....cccc.....", ".....cccc.....", ".....#gg#.....", ".....#gg#.....", ".....#gg#.....", "....#gggg#....", "....#gggg#....", "...#gggggg#...", "...#gggggg#...", "..#gggggggg#..",
      "..#gggggggg#..", ".#gggggggggg#.", ".#gggggggggg#.", "#gggggggggggg#", "#gggggggggggg#", "#gggggggggggg#", "##############"] },
    spray: { nome: "Spray", m: [
      "...hhhhhh.....", "..hhhhhhhhhh..", "..hhhhhh......", ".....#hh#.....", "...########...", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..",
      "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..##########.."] },
    flacone: { nome: "Flacone", m: [
      "....cccccc....", "....cccccc....", "....#gggg#....", "...#gggggg#...", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..",
      "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..#gggggggg#..", "..##########.."] }
  };
  const PALETTE = [["verde", "#4fb36b"], ["azzurro", "#4fa3e0"], ["blu", "#3d5bd9"], ["viola", "#9b5de5"], ["rosa", "#f06fa8"], ["rosso", "#e5484d"], ["arancio", "#f4923c"], ["giallo", "#f2cc45"], ["bianco", "#e8e4f0"], ["nero", "#3a3148"]];
  const FRAZIONE = { "pieno": 1, "metà": 0.5, "quasi finito": 0.2, "finito": 0 };
  const COLS = 14, RIGHE = 18;

  const hex2rgb = h => { h = String(h || "#4fa3e0").replace("#", ""); if (h.length === 3) h = h.replace(/./g, "$&$&"); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) || 0); };
  const mix = (a, b, t) => "rgb(" + a.map((v, i) => Math.round(v + (b[i] - v) * t)).join(",") + ")";
  const hash = s => { let h = 7; for (const c of String(s || "")) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; };
  const nomiForme = Object.keys(FORME);
  /* Forma e colore di un prodotto: quelli scelti, oppure uno stabile ricavato dal nome. */
  const predefinito = p => { const h = hash(p && p.tipo); return { forma: p && FORME[p.forma] ? p.forma : nomiForme[h % nomiForme.length], colore: p && p.colore ? p.colore : PALETTE[(h >>> 3) % PALETTE.length][1] }; };

  function disegna(canvas, forma, colore, livello, scala) {
    const F = FORME[forma] || FORME.tonda, m = F.m, k = scala || 4;
    canvas.width = COLS * k; canvas.height = RIGHE * k;
    const x = canvas.getContext("2d"); x.imageSmoothingEnabled = false; x.clearRect(0, 0, canvas.width, canvas.height);
    const rgb = hex2rgb(colore), chiaro = mix(rgb, [255, 255, 255], .45), scuro = mix(rgb, [0, 0, 0], .35), liquido = mix(rgb, rgb, 0);
    const righeG = m.map((r, i) => r.includes("g") ? i : -1).filter(i => i >= 0), R = righeG.length;
    const fr = FRAZIONE[livello] == null ? 1 : FRAZIONE[livello], n = fr === 0 ? 0 : Math.max(1, Math.round(R * fr));
    const pieneDa = R - n, off = RIGHE - m.length;
    const px = (cx, ry, col) => { x.fillStyle = col; x.fillRect(cx * k, (ry + off) * k, k, k); };
    m.forEach((riga, ry) => {
      const prima = riga.indexOf("g"), ultima = riga.lastIndexOf("g"), pos = righeG.indexOf(ry);
      for (let cx = 0; cx < COLS; cx++) {
        const c = riga[cx];
        if (c === "#") px(cx, ry, "#b9b1d0");
        else if (c === "c") px(cx, ry, m[ry + 1] && m[ry + 1][cx] === "c" ? "#a97a46" : "#7a5230");
        else if (c === "h") px(cx, ry, cx % 2 ? "#8b8497" : "#a39cb0");
        else if (c === "g") {
          const pieno = pos >= pieneDa && n > 0;
          if (!pieno) px(cx, ry, "rgba(190,205,235,.14)");
          else px(cx, ry, pos === pieneDa ? chiaro : cx === prima ? chiaro : cx === ultima ? scuro : liquido);
        }
      }
    });
  }
  window.OLW_AMPOLLE = { FORME, PALETTE, FRAZIONE, disegna, predefinito, COLS, RIGHE };
})();
