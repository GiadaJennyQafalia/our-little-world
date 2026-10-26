/* Our little world · esportazione dati
   csv(): righe -> testo CSV (separatore ";" e BOM, così Excel italiano lo apre senza sorprese).
   zip(): impacchetta più file in un unico .zip (senza compressione, basta e avanza per del testo).
   scarica(): fa scaricare il file al browser. */
(function () {
  "use strict";
  const cella = v => {
    if (v == null) return "";
    if (typeof v === "boolean") return v ? "sì" : "no";
    const s = String(v);
    return /[";\n\r]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  };
  const csv = (colonne, righe) => "﻿" + [colonne.join(";"), ...righe.map(r => colonne.map(c => cella(r[c])).join(";"))].join("\r\n") + "\r\n";

  let TAB = null;
  const crc32 = byte => {
    if (!TAB) { TAB = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; TAB[n] = c >>> 0; } }
    let c = 0xFFFFFFFF; for (let i = 0; i < byte.length; i++) c = TAB[(c ^ byte[i]) & 255] ^ (c >>> 8);
    return (c ^ 0xFFFFFFFF) >>> 0;
  };
  function zip(files) {
    const enc = new TextEncoder(), parti = [], centrale = [];
    let pos = 0;
    const d = new Date(), ora = (d.getHours() << 11) | (d.getMinutes() << 5) | (d.getSeconds() >> 1), data = ((d.getFullYear() - 1980) << 9) | ((d.getMonth() + 1) << 5) | d.getDate();
    for (const [nome, testo] of Object.entries(files)) {
      const n = enc.encode(nome), b = enc.encode(testo), crc = crc32(b);
      const loc = new DataView(new ArrayBuffer(30));
      loc.setUint32(0, 0x04034b50, true); loc.setUint16(4, 20, true); loc.setUint16(6, 0x0800, true); loc.setUint16(8, 0, true);
      loc.setUint16(10, ora, true); loc.setUint16(12, data, true); loc.setUint32(14, crc, true);
      loc.setUint32(18, b.length, true); loc.setUint32(22, b.length, true); loc.setUint16(26, n.length, true); loc.setUint16(28, 0, true);
      parti.push(new Uint8Array(loc.buffer), n, b);
      const c = new DataView(new ArrayBuffer(46));
      c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint16(8, 0x0800, true); c.setUint16(10, 0, true);
      c.setUint16(12, ora, true); c.setUint16(14, data, true); c.setUint32(16, crc, true);
      c.setUint32(20, b.length, true); c.setUint32(24, b.length, true); c.setUint16(28, n.length, true);
      c.setUint32(42, pos, true);
      centrale.push(new Uint8Array(c.buffer), n);
      pos += 30 + n.length + b.length;
    }
    const lenC = centrale.reduce((s, x) => s + x.length, 0);
    const fine = new DataView(new ArrayBuffer(22));
    fine.setUint32(0, 0x06054b50, true); fine.setUint16(8, Object.keys(files).length, true); fine.setUint16(10, Object.keys(files).length, true);
    fine.setUint32(12, lenC, true); fine.setUint32(16, pos, true);
    return new Blob([...parti, ...centrale, new Uint8Array(fine.buffer)], { type: "application/zip" });
  }

  function scarica(nome, blob) {
    const url = URL.createObjectURL(blob), a = document.createElement("a");
    a.href = url; a.download = nome; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 10000);
  }

  window.OLW_CSV = { csv, zip, scarica };
})();
