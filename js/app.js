(() => {
"use strict";
const DAY = 864e5, HOUR = 36e5;
const WEB = "data:image/svg+xml," + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none" stroke="#a89cb3" stroke-width="1.1"><path d="M0 0L100 70M0 0L70 100M0 0L30 100M0 0L100 30"/><path d="M0 22Q18 18 22 0M0 44Q30 38 44 0M0 66Q45 56 66 0M0 88Q60 74 88 0"/></svg>');
document.documentElement.style.setProperty("--web", `url("${WEB}")`);

const DIMORE = { castello: "Il Castello", hobbit: "La Tana nella collina", caverna: "La Grotta di cristalli", reggia: "Il Palazzo", torre: "La Torre del mago", appartamento: "L'Appartamento in città" };
const CLASSI = { strega: "Strega", ranger: "Ranger", alchimista: "Alchimista", cavaliere: "Cavaliere", elfo: "Elfo", druido: "Druido" };
const DESC_CLASSE = { strega: "Incantesimi e bastone nodoso", ranger: "Cappuccio, arco e passo silenzioso", alchimista: "Pozioni, occhiali e curiosità", cavaliere: "Armatura lucida e onore", elfo: "Eleganza e orecchie a punta", druido: "Corna, foresta e radici" };
/* Il kit di ogni classe: i pezzi che l'eroe ha di serie. Gli altri pezzi "speciali" si comprano con le monete. */
const KIT = {
  strega: { capelli: { id: "wavy", col: "blonde" }, busto: { id: "robe", col: "black" }, gambe: { id: "skirt", col: "black" }, scarpe: { id: "boots", col: "brown" }, cappello: { id: "wizard", col: "black" }, mantello: { id: "solid", col: "#d6338f" }, arma: { id: "gnarled", col: "medium" } },
  ranger: { capelli: { id: "mop", col: "sandy" }, busto: { id: "leather" }, gambe: { id: "pants", col: "black" }, scarpe: { id: "boots", col: "leather" }, cappello: { id: "hood", col: "#5c4a7a" }, mantello: { id: "solid", col: "#5c4a7a" } },
  alchimista: { capelli: { id: "bedhead", col: "brown" }, busto: { id: "longsleeve2", col: "lavender" }, gambe: { id: "pants", col: "brown" }, scarpe: { id: "boots", col: "leather" }, accessorio: { id: "glasses", col: "black" }, arma: { id: "crystal", col: "purple" } },
  cavaliere: { capelli: { id: "parted", col: "light_brown" }, busto: { id: "plate" }, gambe: { id: "pants", col: "gray" }, scarpe: { id: "boots", col: "gray" }, cappello: { id: "barbuta", col: "steel" } },
  elfo: { capelli: { id: "long", col: "platinum" }, orecchie: { id: "elven" }, busto: { id: "longsleeve2", col: "forest" }, gambe: { id: "pants", col: "brown" }, scarpe: { id: "boots_fold", col: "leather" }, mantello: { id: "solid", col: "forest" } },
  druido: { capelli: { id: "braid", col: "ginger" }, corna: { id: "curled" }, busto: { id: "longsleeve", col: "forest" }, gambe: { id: "pants", col: "brown" }, scarpe: { id: "boots", col: "leather" }, cappello: { id: "hood", col: "forest" }, arma: { id: "gnarled", col: "medium" } }
};
const SOSTITUTI = { busto: ["longsleeve2", "longsleeve", "scoop", "vneck", "sleeveless"], gambe: ["pants", "pants2"], scarpe: ["boots", "shoes"] };
const PREZZO = { animale: 100, orecchie: 50, corna: 80, coda: 70, ali: 120, mantello: 70, cappello: 60, accessorio: 40, collo: 40, vita: 30, braccia: 40, schiena: 60, arma: 60, scudo: 60, barba: 30 };
const PELLI = ["light", "amber", "olive", "taupe", "bronze", "brown", "black"];
const STATI = ["Splendente", "In ordine", "Trascurata", "Abbandonata"];
/* ---------- Pianta della casa e skin delle dimore ----------
   La PIANTA dice quali sono le stanze vere di casa (nome, tipo, posizione nella mappa stilizzata) e vive in config/casa.pianta.
   La DIMORA (skin) è solo l'aspetto: un'immagine con dei "posti", uno per tipo di stanza. Ogni stanza della pianta va nel posto del suo tipo,
   quindi cambiando dimora la casa resta la stessa. Tutte le dimore condividono la disposizione dei posti del castello. */
const TIPI = { bagno: "Bagno", camera: "Camera", cucina: "Cucina", soggiorno: "Soggiorno", ingresso: "Ingresso", corridoio: "Corridoio", ripostiglio: "Ripostiglio", balcone: "Balcone", altro: "Altro (senza posto)" };
const POSTI = [ /* riquadri tappabili, in pixel dell'immagine 768×1376 */
  { tipo: "bagno", rect: [112, 283, 376, 530] },
  { tipo: "camera", rect: [392, 283, 656, 530] },
  { tipo: "ripostiglio", rect: [112, 550, 312, 798] },
  { tipo: "corridoio", rect: [328, 550, 440, 898], stretta: true },
  { tipo: "cucina", rect: [456, 550, 656, 898] },
  { tipo: "ingresso", rect: [112, 918, 312, 1198] },
  { tipo: "soggiorno", rect: [328, 918, 656, 1198] },
  { tipo: "balcone", rect: [678, 400, 756, 1062], stretta: true }
];
const SKIN = { castello: { img: "img/castello.webp", w: 768, h: 1376, stanze: "img/stanze/", file: { bagno: "bagno", camera: "camera", ripostiglio: "sgabuzzino", corridoio: "corridoio", cucina: "cucina", ingresso: "ingresso", soggiorno: "soggiorno", balcone: "balcone" } } };
const GRIGLIA = { w: 11, h: 11 };
const CORRIDOIO = { tipo: "corridoio", x: 4, y: 3, w: 2, h: 4 };
const PIANTA_BASE = {
  "Bagno": { tipo: "bagno", x: 0, y: 0, w: 5, h: 3 }, "Camera": { tipo: "camera", x: 5, y: 0, w: 5, h: 3 },
  "Sgabuzzino": { tipo: "ripostiglio", x: 0, y: 3, w: 4, h: 4 }, "Cucina": { tipo: "cucina", x: 6, y: 3, w: 4, h: 4 },
  "Ingresso": { tipo: "ingresso", x: 0, y: 7, w: 4, h: 4 }, "Salotto": { tipo: "soggiorno", x: 4, y: 7, w: 6, h: 4 },
  "Balcone": { tipo: "balcone", x: 10, y: 2, w: 1, h: 6 }
};
const COL_TIPO = { bagno: "#5f9fb0", camera: "#8a6bb5", cucina: "#c98a4b", soggiorno: "#6f9a5b", ingresso: "#b0985f", corridoio: "#7d7a8c", ripostiglio: "#8a7260", balcone: "#5f8f7a", altro: "#b05f5f" };
function tipoDa(n) {
  const t = String(n || "").toLowerCase();
  return /bagn|wc|toilet/.test(t) ? "bagno" : /camer|letto|stanza da letto/.test(t) ? "camera" : /cucin/.test(t) ? "cucina" : /sogg|salotto|living|sala/.test(t) ? "soggiorno"
    : /ingress|entrata/.test(t) ? "ingresso" : /sgab|ripost|cantin|lavander/.test(t) ? "ripostiglio" : /balcon|terraz|veranda/.test(t) ? "balcone" : /corridoi/.test(t) ? "corridoio" : "altro";
}
/* La pianta effettiva: i valori salvati, altrimenti quelli di base ricavati dal nome. "Tutta la casa" è sempre il corridoio. */
function pianta() {
  const salvata = (S.config && S.config.pianta) || {}, out = {};
  for (const r of stanze()) {
    const b = PIANTA_BASE[r], s = salvata[r];
    out[r] = { ...(b || { tipo: tipoDa(r), x: 0, y: 0, w: 3, h: 2 }), ...(s || {}) };
    if (!TIPI[out[r].tipo]) out[r].tipo = "altro";
  }
  out["Tutta la casa"] = { ...CORRIDOIO, ...((salvata["Tutta la casa"]) || {}), tipo: "corridoio" };
  return out;
}
const tipoStanza = r => (pianta()[r] || {}).tipo || "altro";
const nomeStanza = r => r === "Tutta la casa" ? "Corridoio" : r;
/* La stanza della pianta che occupa un posto: la prima, in ordine, che ha quel tipo. */
function stanzaDelPosto(tipo, pi) {
  if (tipo === "corridoio") return "Tutta la casa";
  return Object.keys(pi).find(r => r !== "Tutta la casa" && pi[r].tipo === tipo) || null;
}
const LIVELLI_PRODOTTO = ["pieno", "metà", "quasi finito", "finito"];
const XP_SOGLIE = [0, 200, 450, 750, 1100, 1500, 2000];
const SBLOCCHI = ["personaggio base", "vestiti", "cappelli e accessori", "segni particolari", "primo animale", "accessori per animali", "animali fantasy", "oggetti rari"];
const CAT = {
  rapida: { nome: "Rapida", plur: "Rapide", col: "var(--rapida)", desc: "fino a 44 min, sbatti 1–3" },
  sbatti: { nome: "Sbatti", plur: "Sbatti", col: "var(--sbatti)", desc: "sbatti 4–5" },
  lunga: { nome: "Lunga", plur: "Lunghe", col: "var(--lunga)", desc: "45 min o più" }
};
const categoria = f => f.minuti >= 45 ? "lunga" : f.sbatti >= 4 ? "sbatti" : "rapida";

/* ---------- Pixel art ---------- */
function pix(rows, pal, cls) {
  const h = rows.length, w = rows[0].length; let r = "";
  rows.forEach((row, y) => [...row].forEach((ch, x) => { if (ch !== ".") r += `<rect x="${x}" y="${y}" width="1.04" height="1.04" fill="${pal[ch]}"/>`; }));
  return `<svg class="px ${cls || ""}" viewBox="0 0 ${w} ${h}" aria-hidden="true">${r}</svg>`;
}
const ICON = {
  rapida: c => pix([".....aaa.", "....aaa..", "...aaa...", "..aaaaaa.", "....aab..", "...aab...", "..ab.....", ".a.......", "........."], { a: c, b: "#2b8f80" }),
  sbatti: c => pix(["..aaaaa..", ".aaaaaaa.", "aaaaaaaaa", "aabbabbaa", "aabbabbaa", "aaaaaaaaa", ".aaabaaa.", "..a.a.a..", "..aaaaa.."], { a: c, b: "#15111c" }),
  lunga: c => pix(["bbbbbbbbb", ".a.....a.", ".acc.cca.", "..accca..", "...aca...", "..a.c.a..", ".a..c..a.", ".accccca.", "bbbbbbbbb"], { a: c, b: "#c9a26a", c: "#e0a944" }),
  clock: c => pix([".aaaaa.", "a..b..a", "a..b..a", "a..bbba", "a.....a", "a.....a", ".aaaaa."], { a: c, b: c }),
  coin: () => pix([".aaaa.", "abbbba", "abaaba", "abaaba", "abbbba", ".aaaa."], { a: "#e0a944", b: "#f6d27a" }),
  star: () => pix(["....a....", "...aba...", "aaabbbaaa", ".abbbbba.", "..abbba..", ".abbabba.", ".aa...aa.", "a.......a", "........."], { a: "#b8862b", b: "#f6d27a" }),
  pin: c => pix(["..aaa..", ".abbba.", ".abbba.", "..aaa..", "...a...", "...a...", "...a..."], { a: c, b: "#ece2cc" })
};

let db = null, me = null, winStart = 0, archiviando = false, sb = null, utente = null;
const S = {
  config: null, faccende: [], comp: [], giocatori: {}, premi: [], riscatti: [], prodotti: [], spesa: [], sfidaPremi: [], sfide: {},
  loaded: { config: false, faccende: false, giocatori: false, comp: false },
  view: "casa", stanzaSel: null, fCat: "tutte", fStanza: "tutte", sgab: "scorte", onboardingShown: false
};
const BONUS_GIORNO = 0.2;
try { const v = localStorage.getItem("olw-view"); if (v) S.view = v; me = localStorage.getItem("olw-hero"); } catch (e) {}

const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = n => Math.round(n).toLocaleString("it-IT");
const puntiBase = (min, d, s) => Math.max(5, Math.round(min / 2 * (1 + 0.15 * (d - 1) + 0.15 * (s - 1))));
const nome = id => (S.giocatori[id] && S.giocatori[id].nome) || "Qualcuno";
const giorni = ms => Math.round(ms / DAY);
const dataBreve = ts => new Date(ts).toLocaleDateString("it-IT", { day: "numeric", month: "short" });
const oraBreve = ts => new Date(ts).toLocaleString("it-IT", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
const inizioGiorno = ts => { const d = new Date(ts); d.setHours(0, 0, 0, 0); return d.getTime(); };
const inizioMese = ts => { const d = new Date(ts); d.setHours(0, 0, 0, 0); d.setDate(1); return d.getTime(); };
const meseDopo = ts => { const d = new Date(ts); d.setMonth(d.getMonth() + 1); return d.getTime(); };
const chiaveMese = ts => { const d = new Date(ts); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0"); };
function salvaEroe(id) {
  me = id; try { localStorage.setItem("olw-hero", id); } catch (e) {}
  if (db && utente) db.doc("utenti/" + utente.id).set({ eroe: id, email: utente.email || "", ts: Date.now() }).catch(e => console.error(e));
}
const oggiKey = (ts = Date.now()) => { const d = new Date(ts); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); };

function toast(msg, azione) {
  document.querySelectorAll(".toast").forEach(t => t.remove());
  const t = document.createElement("div"); t.className = "toast fr-parch"; t.setAttribute("role", "status");
  const s = document.createElement("span"); s.textContent = msg; t.appendChild(s);
  if (azione) { const b = document.createElement("button"); b.textContent = azione.label; b.onclick = () => { t.remove(); azione.fn(); }; t.appendChild(b); }
  document.body.appendChild(t); setTimeout(() => t.remove(), azione ? 6000 : 2600);
}
/* Piccola festa a schermo: scintille pixel e un cartiglio. */
function festa(testo) {
  document.querySelectorAll(".festa").forEach(x => x.remove());
  const d = document.createElement("div"); d.className = "festa"; d.setAttribute("aria-hidden", "true");
  let html = `<div class="festa-banner">${esc(testo)}</div>`;
  for (let k = 0; k < 18; k++) {
    const ang = (k / 18) * Math.PI * 2, r = 90 + (k % 3) * 40;
    html += `<i style="--dx:${Math.round(Math.cos(ang) * r)}px;--dy:${Math.round(Math.sin(ang) * r)}px;--dl:${(k % 4) * 40}ms"></i>`;
  }
  d.innerHTML = html; document.body.appendChild(d);
  setTimeout(() => d.remove(), 1900);
}
let ultimoLivello = null, ultimoEroe = null;
function controllaLivello() {
  if (!me || !S.giocatori[me] || !S.loaded.comp) return;
  const lv = livelloDa(xpDi(me)).lv;
  if (ultimoEroe !== me) { ultimoEroe = me; ultimoLivello = lv; return; }
  if (ultimoLivello !== null && lv > ultimoLivello) festa(`Livello ${lv}! Sbloccato: ${livelloDa(xpDi(me)).sblocco}`);
  ultimoLivello = lv;
}

function errore(e) {
  console.error(e);
  const permesso = e && (e.code === "42501" || /row-level security|permission/i.test(e.message || ""));
  toast(permesso ? "Questo account non è tra i membri della casa: aggiungi la sua email nella tabella membri di Supabase." : "Salvataggio non riuscito. Controlla la connessione e riprova.");
}

/* ---------- Calcoli ---------- */
function ultimeComp() {
  const m = {};
  for (const c of S.comp) { if (c.annullato) continue; if (!m[c.faccendaId] || c.ts > m[c.faccendaId]) m[c.faccendaId] = c.ts; }
  return m;
}
function infoFaccenda(f, ult, now) {
  const base = puntiBase(f.minuti, f.diff, f.sbatti);
  const lastComp = Math.max(ult[f.id] || 0, f.ultima || 0);
  const last = Math.max(f.base || 0, lastComp);
  const riposo = lastComp && now - lastComp < 6 * HOUR ? 6 * HOUR - (now - lastComp) : 0;
  let urgente = false, ritardo = 0, scadenza = null, mult = 1, frac = null;
  if (f.tipo === "ricorrente" && f.freq) {
    scadenza = last + f.freq * DAY;
    ritardo = now - scadenza;
    urgente = ritardo >= 0;
    frac = Math.max(0, Math.min(1, (scadenza - now) / (f.freq * DAY)));
    if (urgente) mult = Math.min(1.5, 1 + 0.1 * Math.floor(ritardo / (7 * DAY)));
  }
  const prenotata = f.prenDa && f.prenFino > now ? f.prenDa : null;
  return { base, punti: Math.round(base * mult), mult, riposo, urgente, ritardo, scadenza, frac, prenotata, last, cat: categoria(f) };
}
/* ---------- Missione del giorno ---------- */
const hashStr = s => { let h = 7; for (const ch of s) h = (h * 31 + ch.charCodeAt(0)) >>> 0; return h; };
function scegliGiorno(now, escludi) {
  const ult = ultimeComp();
  const c = S.faccende.filter(f => f.attiva !== false && f.id !== escludi).map(f => ({ f, i: infoFaccenda(f, ult, now) }))
    .filter(x => !x.i.riposo && !(x.i.prenotata && x.i.prenotata !== me));
  if (!c.length) return null;
  const urg = c.filter(x => x.i.urgente).sort((a, b) => b.i.ritardo - a.i.ritardo);
  if (urg.length) return urg[0].f.id;
  const ric = c.filter(x => x.i.scadenza != null).sort((a, b) => a.i.scadenza - b.i.scadenza);
  if (ric.length && ric[0].i.scadenza - now < 3 * DAY) return ric[0].f.id;
  /* Nessuna urgenza: una a sorpresa, uguale per tutto il giorno, tra le prime in scadenza. */
  const pool = (ric.length ? ric.slice(0, 6) : c);
  return pool[hashStr(oggiKey(now) + (escludi || "")) % pool.length].f.id;
}
function missioneGiorno(now) {
  const mg = S.config && S.config.missioneGiorno;
  if (!mg || mg.giorno !== oggiKey(now)) return null;
  const f = S.faccende.find(x => x.id === mg.id);
  if (!f || (!mg.fatta && f.attiva === false)) return null;
  return { ...mg, f };
}
let scegliendo = false;
async function assicuraMissioneGiorno(now) {
  if (scegliendo || !db || !S.config || !S.loaded.faccende || !S.loaded.comp || !me) return;
  if (missioneGiorno(now)) return;
  const id = scegliGiorno(now);
  if (!id) return;
  scegliendo = true;
  try { await db.doc("config/casa").update({ missioneGiorno: { giorno: oggiKey(now), id, fatta: false, cambi: 0 } }); }
  catch (e) { console.error("missione del giorno", e); }
  scegliendo = false;
}
async function cambiaGiorno() {
  const now = Date.now(), mg = missioneGiorno(now);
  if (!mg || mg.fatta || (mg.cambi || 0) >= 1) return;
  const id = scegliGiorno(now, mg.id);
  if (!id) { toast("Non ci sono altre missioni disponibili oggi"); return; }
  try { await db.doc("config/casa").update({ missioneGiorno: { ...S.config.missioneGiorno, id, cambi: (mg.cambi || 0) + 1 } }); toast("Il destino ha scelto un'altra missione"); }
  catch (e) { errore(e); }
}

function stanze() {
  const set = new Set((S.config && S.config.stanze) || []);
  for (const f of S.faccende) if (f.attiva !== false && f.stanza && f.stanza !== "Tutta la casa") set.add(f.stanza);
  return [...set];
}
function statoStanze(now) {
  const ult = ultimeComp(), out = {};
  for (const r of stanze()) {
    let tot = 0, scad = 0, urg = 0;
    for (const f of S.faccende) {
      if (f.attiva === false || f.tipo !== "ricorrente") continue;
      if (f.stanza !== r && f.stanza !== "Tutta la casa") continue;
      const i = infoFaccenda(f, ult, now);
      tot += i.base; if (i.urgente) { scad += i.base; if (f.stanza === r) urg++; }
    }
    const pct = tot ? scad / tot : 0;
    out[r] = { pct, livello: pct <= 0.10 ? 0 : pct <= 0.25 ? 1 : pct <= 0.50 ? 2 : 3, urg };
  }
  return out;
}
function xpDi(id) {
  let x = 0;
  for (const c of S.comp) if (!c.annullato && c.ts >= winStart && (c.giocatori || []).includes(id)) x += c.punti || 0;
  const arch = (S.giocatori[id] && S.giocatori[id].archivio) || {};
  for (const [k, v] of Object.entries(arch)) { const [y, m] = k.split("-").map(Number); if (new Date(y, m - 1, 1).getTime() < winStart) x += v || 0; }
  return x;
}
function moneteDi(id) { let spese = 0; for (const r of S.riscatti) if (r.giocatore === id) spese += r.costo || 0; return xpDi(id) - spese; }
function livelloDa(xp) {
  let lv = 1, soglia = 0, prossima = XP_SOGLIE[1];
  for (let i = 1; ; i++) {
    const s = i < XP_SOGLIE.length ? XP_SOGLIE[i] : XP_SOGLIE.at(-1) + 600 * (i - XP_SOGLIE.length + 1);
    if (xp >= s) { lv = i + 1; soglia = s; } else { prossima = s; break; }
  }
  return { lv, soglia, prossima, sblocco: SBLOCCHI[Math.min(lv - 1, SBLOCCHI.length - 1)] };
}
function periodoSfida(now) {
  const cfg = S.config || {}, len = (cfg.sfidaGiorni || 14) * DAY, start0 = cfg.sfidaInizio || now;
  const k = Math.max(0, Math.floor((now - start0) / len));
  const inizio = start0 + k * len;
  return { len, inizio, fine: inizio + len, prec: k >= 1 ? inizio - len : null };
}
function punteggi(da, a) {
  const p = {}; for (const id of Object.keys(S.giocatori)) p[id] = 0;
  for (const c of S.comp) if (!c.annullato && c.ts >= da && c.ts < a) for (const g of c.giocatori || []) p[g] = (p[g] || 0) + (c.punti || 0);
  return p;
}
/* I mesi più vecchi della finestra di lettura diventano totali salvati sull'eroe, così XP e monete non calano mai. */
async function archivia() {
  if (archiviando || !db) return;
  const eroi = Object.keys(S.giocatori); if (!eroi.length) return;
  archiviando = true;
  try {
    const primo = Math.min(...eroi.map(id => S.giocatori[id].ts || Date.now()));
    for (let m = inizioMese(primo); m < winStart; m = meseDopo(m)) {
      const k = chiaveMese(m);
      const mancano = eroi.filter(id => !(S.giocatori[id].archivio && k in S.giocatori[id].archivio));
      if (!mancano.length) continue;
      const snap = await db.collection("completamenti").where("ts", ">=", m).where("ts", "<", meseDopo(m)).limit(1000).get();
      const somme = {}; for (const id of mancano) somme[id] = 0;
      snap.docs.forEach(d => { const c = d.data(); if (c.annullato) return; for (const g of c.giocatori || []) if (g in somme) somme[g] += c.punti || 0; });
      for (const id of mancano) await db.doc("giocatori/" + id).update({ archivio: { ...(S.giocatori[id].archivio || {}), [k]: somme[id] } });
    }
  } catch (e) { console.error("archivio", e); }
  archiviando = false;
}

/* ---------- Grafica ---------- */
function scena(tipo) {
  const st = 'fill="var(--stone)" stroke="var(--stone-hi)" stroke-width="1.5"';
  const win = 'fill="#e0a94455"';
  const ground = '<path d="M0 150 Q80 138 160 146 T320 140 V170 H0Z" fill="#241c2e"/>';
  const moon = '<circle cx="270" cy="34" r="14" fill="#ece2cc" opacity=".85"/><circle cx="276" cy="30" r="13" fill="#1d1630"/>';
  const shapes = {
    castello: `<rect x="70" y="72" width="180" height="78" ${st}/><rect x="44" y="40" width="48" height="110" ${st}/><rect x="228" y="40" width="48" height="110" ${st}/>
      <path d="M44 40v-10h10v10h8v-10h10v10h8v-10h12v10M228 40v-10h10v10h8v-10h10v10h8v-10h12v10M70 72v-9h12v9h12v-9h12v9h12v-9h12v9h12v-9h12v9h12v-9h12v9h12v-9h12v9h12v-9h12v9" ${st}/>
      <path d="M138 150v-34a22 22 0 0 1 44 0v34z" fill="#15111c" stroke="var(--stone-hi)"/><rect x="60" y="62" width="8" height="16" rx="4" ${win}/><rect x="252" y="62" width="8" height="16" rx="4" ${win}/><rect x="100" y="92" width="8" height="14" rx="4" ${win}/><rect x="212" y="92" width="8" height="14" rx="4" ${win}/>`,
    hobbit: `<path d="M20 150 Q160 20 300 150Z" fill="#2f3a2a" stroke="#45573d" stroke-width="1.5"/><circle cx="160" cy="118" r="28" fill="#3d2a1e" stroke="var(--candle)" stroke-width="2"/><circle cx="160" cy="118" r="2.5" fill="var(--candle)"/><circle cx="100" cy="118" r="11" ${win} stroke="#45573d"/><circle cx="220" cy="118" r="11" ${win} stroke="#45573d"/><rect x="214" y="58" width="10" height="26" fill="#45573d"/>`,
    caverna: `<path d="M10 150 L40 70 L90 40 L170 30 L240 46 L300 90 L312 150Z" ${st}/><path d="M110 150 Q110 80 160 78 Q210 80 210 150Z" fill="#15111c"/><circle cx="160" cy="132" r="7" fill="var(--candle)" opacity=".8"/><path d="M60 82l6 14 6-14M250 74l5 12 5-12" fill="var(--stone-hi)"/>`,
    reggia: `<rect x="40" y="88" width="240" height="62" ${st}/><path d="M110 88 Q160 20 210 88Z" ${st}/><rect x="156" y="34" width="8" height="18" fill="var(--candle)"/><path d="M40 88 L160 66 L280 88" fill="none" stroke="var(--stone-hi)" stroke-width="1.5"/>
      ${[60, 92, 124, 188, 220, 252].map(x => `<rect x="${x}" y="98" width="10" height="52" fill="var(--stone-hi)"/>`).join("")}<path d="M146 150v-28a14 14 0 0 1 28 0v28z" fill="#15111c"/>`,
    torre: `<path d="M120 150 L130 50 L190 50 L200 150Z" ${st}/><path d="M118 50 L160 6 L202 50Z" fill="#3b2a4f" stroke="var(--stone-hi)" stroke-width="1.5"/><rect x="154" y="70" width="12" height="20" rx="6" ${win}/><rect x="150" y="104" width="12" height="18" rx="6" ${win}/><path d="M150 150v-16a10 10 0 0 1 20 0v16z" fill="#15111c"/>`,
    appartamento: `<rect x="90" y="30" width="140" height="120" ${st}/><rect x="80" y="24" width="160" height="10" ${st}/>
      ${[52, 82, 112].map(y => [108, 148, 188].map(x => `<rect x="${x}" y="${y}" width="22" height="18" ${y === 82 && x === 148 ? 'fill="#e0a944aa"' : win}/>`).join("")).join("")}<rect x="148" y="132" width="24" height="18" fill="#15111c"/>`
  };
  return `<svg class="scene" viewBox="0 0 320 170" role="img" aria-label="${esc(DIMORE[tipo] || "La dimora")}">${moon}${shapes[tipo] || shapes.castello}${ground}</svg>`;
}
function sigillo(classe, cls) {
  const g = {
    cavaliere: '<path d="M34 14v30M26 38h16M34 44v8" stroke="var(--candle)" stroke-width="3" stroke-linecap="round"/>',
    strega: '<path d="M18 46h32L38 30 34 12 28 30z" fill="var(--arcane)"/><circle cx="34" cy="20" r="2" fill="var(--candle)"/>',
    ranger: '<path d="M24 14q22 20 0 40" fill="none" stroke="var(--moss)" stroke-width="3"/><path d="M24 14v40M20 34h26M46 34l-6-4M46 34l-6 4" stroke="var(--parchment)" stroke-width="2"/>',
    alchimista: '<path d="M29 14h10M31 14v12L20 48a3 3 0 0 0 3 4h22a3 3 0 0 0 3-4L37 26V14" fill="none" stroke="var(--parchment)" stroke-width="2.5"/><path d="M24 42h20l3 6a3 3 0 0 1-3 4H23a3 3 0 0 1-3-4z" fill="var(--moss)"/>'
  };
  return `<svg class="sigil ${cls || ""}" viewBox="0 0 68 68" aria-hidden="true"><circle cx="34" cy="34" r="32" fill="var(--vault-2)" stroke="var(--candle)" stroke-width="1.5"/><circle cx="34" cy="34" r="27" fill="none" stroke="var(--seam)"/>${g[classe] || g.cavaliere}</svg>`;
}
/* Ritratto del personaggio composto con i pezzi LPC; finché non è pronto (o per gli eroi senza personaggio) si vede il sigillo della classe. */
const AV = new Map(), AVattesa = new Set(); let avTimer = 0;
function avatar(g, cls) {
  if (!g || !g.pg || !window.OLW_SPRITE) return sigillo(g && g.classe, cls);
  const k = JSON.stringify(g.pg), u = AV.get(k);
  if (u) return `<img class="avatar ${cls || ""}" src="${u}" alt="" width="108" height="108">`;
  if (!AVattesa.has(k)) {
    AVattesa.add(k);
    window.OLW_SPRITE.ritratto(g.pg, 3).then(d => { AV.set(k, d); clearTimeout(avTimer); avTimer = setTimeout(() => { if (db) render(); }, 60); }).catch(e => console.warn("ritratto", e));
  }
  return sigillo(g.classe, cls);
}
const pips = (n, cls, label) => `<span class="pips ${cls}" title="${label} ${n} su 5" aria-label="${label} ${n} su 5">${[1, 2, 3, 4, 5].map(k => `<i class="${k <= n ? "on" : ""}"></i>`).join("")}</span>`;
function tempoRestante(i, f, now) {
  if (f.tipo !== "ricorrente" || !f.freq) {
    return `<div class="timer"><div class="gauge free"></div><div class="tlabel"><span>${f.tipo === "occasionale" ? "da fare una volta" : "quando serve"}</span><span>nessuna scadenza</span></div></div>`;
  }
  if (i.urgente) {
    const g = giorni(i.ritardo);
    return `<div class="timer"><div class="gauge late"><i></i></div><div class="tlabel"><b class="late">${g < 1 ? "Scaduta oggi" : `In ritardo di ${g} ${g === 1 ? "giorno" : "giorni"}`}</b><span>ogni ${f.freq} g</span></div></div>`;
  }
  const rest = i.scadenza - now, cls = i.frac > 0.5 ? "" : i.frac > 0.2 ? "mid" : "low";
  const gg = Math.floor(rest / DAY), hh = Math.ceil(rest / HOUR);
  const txt = rest < DAY ? `Scade tra ${hh} ${hh === 1 ? "ora" : "ore"}` : `${gg} ${gg === 1 ? "giorno rimasto" : "giorni rimasti"}`;
  return `<div class="timer"><div class="gauge ${cls}"><i style="width:${Math.max(3, i.frac * 100)}%"></i></div><div class="tlabel"><b>${txt}</b><span>entro ${dataBreve(i.scadenza)} · ogni ${f.freq} g</span></div></div>`;
}

/* ---------- Viste ---------- */
function render() {
  const now = Date.now();
  const tabVista = S.view === "stanza" ? "casa" : S.view;
  document.querySelectorAll("nav.tabs button").forEach(b => b.setAttribute("aria-current", b.dataset.view === tabVista ? "page" : "false"));
  $("#fab").hidden = !(db && me && S.view === "missioni");
  const hc = $("#heroChip"), cc = $("#coinChip");
  if (me && S.giocatori[me]) {
    const g = S.giocatori[me], xp = xpDi(me), L = livelloDa(xp);
    const pct = Math.min(100, (xp - L.soglia) / (L.prossima - L.soglia) * 100);
    hc.hidden = false;
    hc.innerHTML = `${avatar(g, "xs")}<span class="hud-txt"><span class="hud-name">${esc(g.nome)}</span><span class="hud-lv"><b class="lvl">Lv ${L.lv}</b><span class="xpbar" aria-hidden="true"><i style="width:${pct}%"></i></span></span></span>`;
    hc.setAttribute("aria-label", `Stai giocando come ${g.nome}, livello ${L.lv}. Cambia eroe`);
    cc.hidden = false; cc.innerHTML = `${ICON.coin()}<b class="num">${fmt(moneteDi(me))}</b>`;
    cc.setAttribute("aria-label", fmt(moneteDi(me)) + " monete");
  } else {
    hc.hidden = !(db && S.loaded.giocatori);
    hc.innerHTML = `<span class="hud-txt"><span class="hud-name">Chi gioca?</span></span>`;
    cc.hidden = true;
  }
  if (!db || !S.loaded.config || !S.loaded.faccende) return;
  controllaLivello();
  assicuraMissioneGiorno(now);
  const v = { casa: vCasa, stanza: vStanza, missioni: vMissioni, eroe: vEroe, premi: vPremi, sgabuzzino: vSgab }[S.view] || vCasa;
  $("#view").innerHTML = v(now);
  document.querySelectorAll("canvas.pet-cv").forEach(c => window.OLW_SPRITE.animaPet(c, { specie: c.dataset.specie, col: +c.dataset.col }, { riga: 0, scala: 2, fps: 4 }));
  if (S.loaded.giocatori && !(me && S.giocatori[me]) && !S.onboardingShown) {
    S.onboardingShown = true;
    if (Object.keys(S.giocatori).length) apriChi(); else apriProfilo(null, true);
  }
}

/* Polvere e ragnatele sono disegnate da codice sopra l'immagine, in base allo stato della stanza (0 = splendente … 3 = abbandonata). */
function velo(livello, maschera) {
  const web = [0, 0, 0.35, 0.85][livello], polvere = [0, 0.15, 0.55, 1][livello];
  const tw = livello === 0 ? [[22, 30], [64, 20], [78, 58], [36, 70]].map(([x, y], k) => `<i class="tw" style="left:${x}%;top:${y}%;animation-delay:${k * 0.7}s"></i>`).join("") : "";
  const m = maschera ? ` style="-webkit-mask:url(${maschera}) center/100% 100% no-repeat;mask:url(${maschera}) center/100% 100% no-repeat"` : "";
  return `<span class="veil v${livello}"${m} aria-hidden="true"><img class="cobweb l" src="${WEB}" alt="" style="opacity:${web}"><img class="cobweb r" src="${WEB}" alt="" style="opacity:${web}"><span class="dust" style="opacity:${polvere}"></span>${tw}</span>`;
}
/* "Tutta la casa" non è una stanza vera: nel castello è il corridoio e prende lo stato medio della casa. */
function statoUna(r, now, st) {
  if (st[r]) return st[r];
  if (r !== "Tutta la casa") return null;
  const k = Object.keys(st), media = k.length ? k.reduce((a, x) => a + st[x].pct, 0) / k.length : 0, ult = ultimeComp();
  const urg = S.faccende.filter(f => f.attiva !== false && f.tipo === "ricorrente" && f.stanza === "Tutta la casa" && infoFaccenda(f, ult, now).urgente).length;
  return { pct: media, livello: media <= 0.10 ? 0 : media <= 0.25 ? 1 : media <= 0.50 ? 2 : 3, urg };
}
function strisciaGiorno(now) {
  const mg = missioneGiorno(now);
  if (!mg) return "";
  const f = mg.f, i = infoFaccenda(f, ultimeComp(), now), c = CAT[i.cat];
  if (mg.fatta) return `<section class="daily-strip fr-parch done" aria-label="Missione del giorno">
    <button class="ds-main" data-act="vaiMissioni" data-r="tutte"><span class="ds-seal">${ICON.star()}</span><span class="ds-txt"><span class="ds-kicker">Missione del giorno</span><span class="ds-title">${esc(f.nome)}</span><span class="ds-meta">Compiuta${mg.fattaDa ? " da " + esc(mg.fattaDa.map(nome).join(" e ")) : ""}. Domani ne arriva una nuova.</span></span></button></section>`;
  const premio = Math.round(i.punti * (1 + BONUS_GIORNO));
  return `<section class="daily-strip fr-parch ${i.cat}" aria-label="Missione del giorno">
    <button class="ds-main" data-act="vaiMissioni" data-r="tutte"><span class="ds-seal">${ICON[i.cat](c.col)}</span><span class="ds-txt"><span class="ds-kicker">Missione del giorno</span><span class="ds-title">${esc(f.nome)}</span><span class="ds-meta">${esc(f.stanza)} · ${ICON.coin()}<b class="num">${premio}</b></span></span></button>
    <button class="btn prime sm" data-act="fatta" data-id="${f.id}">Compiuta!</button>
  </section>`;
}
function dimoraMappa(dim, st, now) {
  const sk = SKIN[dim], pi = pianta(), pc = (v, t) => (v / t * 100).toFixed(3) + "%";
  const tasti = POSTI.map(po => {
    const r = stanzaDelPosto(po.tipo, pi), x = r && statoUna(r, now, st); if (!x) return "";
    const [x0, y0, x1, y1] = po.rect, nome = nomeStanza(r);
    return `<button class="rm lv${x.livello}${po.stretta ? " stretta" : ""}" data-act="stanza" data-r="${esc(r)}" style="left:${pc(x0, sk.w)};top:${pc(y0, sk.h)};width:${pc(x1 - x0, sk.w)};height:${pc(y1 - y0, sk.h)}" title="${esc(nome)}" aria-label="${esc(nome)}: ${STATI[x.livello]}, ${x.urg ? x.urg + (x.urg === 1 ? " missione urgente" : " missioni urgenti") : "tutto in pari"}">${velo(x.livello)}${x.urg ? `<span class="rm-badge num" aria-hidden="true">${x.urg}</span>` : ""}</button>`;
  }).join("");
  return `<div class="castle"><img src="${sk.img}" width="${sk.w}" height="${sk.h}" alt="${esc(DIMORE[dim])} in sezione: tocca una stanza" decoding="async">${tasti}</div>`;
}
function gruppoMissioni(t, a, vuoto, now) {
  return `<section class="sec"><div class="sec-head"><h3>${t}</h3><span class="muted small num">${a.length}</span></div>${a.length ? `<div class="list">${a.map(x => cartaMissione(x, now)).join("")}</div>` : `<div class="empty fr-dash small">${vuoto}</div>`}</section>`;
}
function vStanza(now) {
  const r = S.stanzaSel, st = statoStanze(now), x = r && statoUna(r, now, st);
  if (!x) { S.view = "casa"; return vCasa(now); }
  const nome = nomeStanza(r), dimS = (S.config && S.config.dimora) || "castello", sk = SKIN[dimS], img = sk && sk.file[tipoStanza(r)], ult = ultimeComp();
  const tutte = S.faccende.filter(f => f.attiva !== false && f.stanza === r).map(f => ({ f, i: infoFaccenda(f, ult, now) }));
  const urg = tutte.filter(y => y.i.urgente && !y.i.riposo).sort((a, b) => b.i.ritardo - a.i.ritardo);
  const disp = tutte.filter(y => !y.i.urgente && !y.i.riposo).sort((a, b) => (a.i.scadenza ?? 1e15) - (b.i.scadenza ?? 1e15));
  const rip = tutte.filter(y => y.i.riposo).sort((a, b) => a.i.riposo - b.i.riposo);
  const pulita = Math.round((1 - x.pct) * 100), col = ["var(--candle)", "var(--moss)", "var(--arcane)", "var(--ember)"][x.livello];
  return `
  <button class="btn ghost sm back" data-act="indietro">← ${esc(DIMORE[dimS] || "La dimora")}</button>
  <section class="hero fr-stone st${x.livello} room-hero">
    <div class="room-scene">${img ? `<img src="${sk.stanze}${img}.webp" alt="${esc(nome)}" decoding="async">` : ""}${velo(x.livello, img ? sk.stanze + img + ".webp" : "")}</div>
    <div class="hero-cap">
      <div class="sec-head"><span class="state">${esc(nome)}</span><span class="pill p${x.livello}">${STATI[x.livello]}</span></div>
      <span class="bar big" aria-hidden="true"><i style="width:${Math.max(4, pulita)}%;background:${col}"></i></span>
      <span class="muted small"><span class="num">${pulita}%</span> pulita${r === "Tutta la casa" ? " (stato medio della casa)" : ""} · ${x.urg ? `<span class="num">${x.urg}</span> ${x.urg === 1 ? "missione urgente" : "missioni urgenti"}` : "nessuna missione urgente"}</span>
    </div>
  </section>
  ${r === "Tutta la casa" ? `<p class="muted small" style="margin:0">Le faccende di tutta la casa, come l'aspirapolvere, stanno nel corridoio.</p>` : ""}
  ${tutte.length ? "" : `<div class="empty fr-dash">Nessuna faccenda in questa stanza.</div>`}
  ${gruppoMissioni("Urgenti", urg, "Niente di scaduto qui.", now)}
  ${gruppoMissioni("Disponibili", disp, "Nessuna missione disponibile.", now)}
  ${rip.length ? gruppoMissioni("In riposo · fatte da poco", rip, "", now) : ""}
  <button class="btn ghost" data-act="vaiMissioni" data-r="${esc(r)}">Vedi tutte le missioni</button>`;
}

function vCasa(now) {
  const cfg = S.config || {};
  const st = statoStanze(now), rs = Object.keys(st);
  const media = rs.length ? rs.reduce((a, r) => a + st[r].pct, 0) / rs.length : 0;
  const liv = media <= 0.10 ? 0 : media <= 0.25 ? 1 : media <= 0.50 ? 2 : 3;
  const dim = cfg.dimora || "castello";
  const sparks = [[14, 30], [30, 18], [52, 26], [72, 14], [86, 36], [44, 8]].map(([x, y]) => `<i class="spark" style="left:${x}%;top:${y}%"></i>`).join("");
  const webOp = [0, 0, 0.35, 0.8][liv], dustOp = [0, 0.2, 0.6, 1][liv];
  const p = periodoSfida(now), sc = punteggi(p.inizio, now), ids = Object.keys(S.giocatori);
  const urgTot = rs.reduce((a, r) => a + st[r].urg, 0);
  return `
  ${strisciaGiorno(now)}
  <section class="hero fr-stone st${liv}">
    ${SKIN[dim] ? "" : `<div class="scene-wrap">${scena(dim)}<div class="glow"></div>
    <img class="cobweb l" src="${WEB}" alt="" style="opacity:${webOp}"><img class="cobweb r" src="${WEB}" alt="" style="opacity:${webOp}">
    <div class="dust" style="opacity:${dustOp}"></div>${sparks}</div>`}
    <div class="hero-cap">
      <div class="sec-head"><span class="state">${esc(cfg.nome || "Our little world")}</span><span class="pill p${liv}">${STATI[liv]}</span></div>
      <span class="muted small">${esc(DIMORE[dim] || "La dimora")} · <span class="num">${Math.round(media * 100)}%</span> delle faccende ricorrenti in ritardo · ${urgTot ? `<span class="num">${urgTot}</span> missioni urgenti` : "nessuna missione urgente"}</span>
    </div>
    ${SKIN[dim] ? dimoraMappa(dim, st, now) : ""}
  </section>
  <section class="sec">
    <div class="sec-head"><h3>Stanze</h3><button class="btn ghost sm" data-act="pianta">Pianta</button></div>
    ${rs.length ? `<div class="rooms">${rs.map(r => `
      <button class="room fr-stone st${st[r].livello}" data-act="stanza" data-r="${esc(r)}">
        <span class="rn">${esc(r)}</span>
        <span><span class="pill p${st[r].livello}">${STATI[st[r].livello]}</span></span>
        <span class="bar"><i style="width:${Math.max(4, 100 - st[r].pct * 100)}%;background:${["var(--candle)", "var(--moss)", "var(--arcane)", "var(--ember)"][st[r].livello]}"></i></span>
        <span class="muted small">${st[r].urg ? st[r].urg + " urgenti" : "tutto in pari"}</span>
      </button>`).join("")}</div>` : `<div class="empty fr-dash">Nessuna stanza ancora. Aggiungile dalle impostazioni della casa.</div>`}
  </section>
  ${ids.length ? `<section class="sec">
    <div class="sec-head"><h3>Sfida in corso</h3><span class="muted small">finisce il ${dataBreve(p.fine - 1)}</span></div>
    ${duello(sc, ids)}
  </section>` : ""}`;
}
function duello(sc, ids) {
  if (ids.length < 2) return `<div class="notice fr-stone small muted">La sfida parte quando c'è un secondo eroe. Dal telefono dell'altra persona, tocca "Chi gioca?" in alto e crea un nuovo eroe.</div>`;
  const [a, b] = ids;
  return `<div class="duel fr-stone"><div><div class="score num">${fmt(sc[a] || 0)}</div><div class="who">${esc(nome(a))}</div></div><div class="vs">contro</div><div><div class="score num">${fmt(sc[b] || 0)}</div><div class="who">${esc(nome(b))}</div></div></div>`;
}

function cartaGiorno(now) {
  const mg = missioneGiorno(now);
  if (!mg) return "";
  const f = mg.f, i = infoFaccenda(f, ultimeComp(), now), c = CAT[i.cat];
  const premio = Math.round(i.punti * (1 + BONUS_GIORNO));
  if (mg.fatta) return `<section class="daily fr-parch done" aria-label="Missione del giorno">
    <div class="daily-seal">${ICON.star()}</div>
    <div class="daily-body">
      <span class="daily-kicker">Missione del giorno</span>
      <span class="daily-title">${esc(f.nome)}</span>
      <span class="daily-note">Compiuta${mg.fattaDa ? " da " + esc(mg.fattaDa.map(nome).join(" e ")) : ""}. Domani all'alba arriva una nuova pergamena.</span>
    </div></section>`;
  const pren = i.prenotata, mia = pren && pren === me;
  return `<section class="daily fr-parch ${i.cat}" aria-label="Missione del giorno">
    <div class="daily-seal">${ICON[i.cat](c.col)}</div>
    <div class="daily-body">
      <span class="daily-kicker">Missione del giorno · bonus +${Math.round(BONUS_GIORNO * 100)}%</span>
      <span class="daily-title">${esc(f.nome)}</span>
      <span class="daily-meta">${esc(f.stanza)} · <span class="num">${f.minuti}</span> min · ${c.nome}${i.urgente ? ` · <span class="late">in ritardo</span>` : ""}</span>
      <div class="daily-reward"><span class="reward-old num">${i.punti}</span><span class="reward-new">${ICON.coin()}<b class="num">${premio}</b></span></div>
      <div class="daily-act">
        <button class="btn prime" data-act="fatta" data-id="${f.id}">Compiuta!</button>
        ${pren && !mia ? `<span class="small">Prenotata da ${esc(nome(pren))}</span>` : `<button class="btn ghost-dark" data-act="prenota" data-id="${f.id}">${mia ? "Togli prenotazione" : "La faccio io"}</button>`}
        ${(mg.cambi || 0) < 1 ? `<button class="linkbtn" data-act="cambiaGiorno">Cambia missione</button>` : ""}
      </div>
    </div>
  </section>`;
}

function cartaMissione({ f, i }, now) {
  const c = CAT[i.cat];
  const pren = i.prenotata;
  const mia = pren && pren === me;
  const mg = missioneGiorno(now), delGiorno = mg && !mg.fatta && mg.id === f.id;
  return `<article class="quest fr-stone ${i.cat}${i.riposo ? " rest" : ""}${i.urgente && !i.riposo ? " is-late" : ""}">
    <div class="emblem"><span class="tile">${ICON[i.cat](c.col)}</span><span class="cn">${c.nome}</span></div>
    <div class="qbody">
      <div class="qtop"><span class="qn">${esc(f.nome)}${delGiorno ? ' <span class="tagday">del giorno</span>' : ""}</span><span class="pts">${ICON.coin()}<b class="num">${i.punti}</b></span></div>
      <div class="qtags">
        <span class="t">${ICON.pin("var(--ash)")}${esc(f.stanza)}</span>
        <span class="t">${ICON.clock("var(--ash)")}<span class="num">${f.minuti}</span> min</span>
        <span class="t">fatica ${pips(f.diff, "d", "Difficoltà")}</span>
        <span class="t">sbatti ${pips(f.sbatti, "s", "Sbatti")}</span>
        ${i.mult > 1 ? `<span class="t bounty">taglia +${Math.round((i.mult - 1) * 100)}%</span>` : ""}
      </div>
      ${tempoRestante(i, f, now)}
      ${pren ? `<span class="reserved">${ICON.pin("var(--arcane)")}Prenotata da ${esc(mia ? "te" : nome(pren))} fino alle ${new Date(f.prenFino).toLocaleTimeString("it-IT", { hour: "2-digit", minute: "2-digit" })}</span>` : ""}
      <div class="qact">
        ${i.riposo ? `<span class="muted small" style="flex:1">Di nuovo disponibile tra <span class="num">${Math.ceil(i.riposo / HOUR)}</span> h</span>` : `
        <button class="btn sm arc" data-act="prenota" data-id="${f.id}" ${pren && !mia ? "disabled" : ""}>${mia ? "Togli prenotazione" : pren ? "Prenotata" : "La faccio io"}</button>
        <button class="btn sm prime" data-act="fatta" data-id="${f.id}">Fatta</button>`}
        <button class="dots" data-act="menu" data-id="${f.id}" aria-label="Altre azioni per ${esc(f.nome)}">⋯</button>
      </div>
    </div>
  </article>`;
}
function vMissioni(now) {
  const ult = ultimeComp();
  const tutte = S.faccende.filter(f => f.attiva !== false).map(f => ({ f, i: infoFaccenda(f, ult, now) }));
  let lst = tutte;
  if (S.fCat !== "tutte") lst = lst.filter(x => x.i.cat === S.fCat);
  if (S.fStanza !== "tutte") lst = lst.filter(x => x.f.stanza === S.fStanza);
  const urg = lst.filter(x => x.i.urgente && !x.i.riposo).sort((a, b) => b.i.ritardo - a.i.ritardo);
  const disp = lst.filter(x => !x.i.urgente && !x.i.riposo).sort((a, b) => (a.i.scadenza ?? 1e15) - (b.i.scadenza ?? 1e15));
  const rip = lst.filter(x => x.i.riposo).sort((a, b) => a.i.riposo - b.i.riposo);
  const gruppo = (t, a, vuoto) => `<section class="sec"><div class="sec-head"><h3>${t}</h3><span class="muted small num">${a.length}</span></div>${a.length ? `<div class="list">${a.map(x => cartaMissione(x, now)).join("")}</div>` : `<div class="empty fr-dash small">${vuoto}</div>`}</section>`;
  const catBtns = [["tutte", "Tutte", ""], ...Object.entries(CAT).map(([k, c]) => [k, c.plur, ICON[k](c.col)])];
  const rs = ["tutte", ...stanze(), "Tutta la casa"];
  return `
  ${cartaGiorno(now)}
  <div class="filters" role="group" aria-label="Filtra per categoria">${catBtns.map(([k, l, ic]) => `<button data-act="fcat" data-k="${k}" aria-pressed="${S.fCat === k}">${ic}${l}</button>`).join("")}</div>
  <div class="filters" role="group" aria-label="Filtra per stanza">${rs.map(r => `<button data-act="fstanza" data-r="${esc(r)}" aria-pressed="${S.fStanza === r}">${esc(r === "tutte" ? "Tutte le stanze" : r)}</button>`).join("")}</div>
  ${tutte.length ? "" : `<div class="empty fr-dash">Nessuna faccenda nel registro. Tocca + per crearne una.</div>`}
  ${gruppo("Urgenti", urg, "Niente di scaduto qui.")}
  ${gruppo("Disponibili", disp, "Nessuna missione disponibile con questi filtri.")}
  ${rip.length ? gruppo("In riposo · fatte da poco", rip, "") : ""}
  <button class="btn ghost" data-act="extra">Ho fatto una faccenda che non è in lista</button>`;
}

function vEroe(now) {
  if (!me || !S.giocatori[me]) return `<div class="notice fr-stone"><h2>Chi sta giocando?</h2><p class="muted small">Scegli il tuo eroe o creane uno nuovo.</p><button class="btn prime" data-act="chi">Scegli l'eroe</button></div>`;
  const eroe = S.giocatori[me];
  const xp = xpDi(me), L = livelloDa(xp);
  const pct = Math.min(100, (xp - L.soglia) / (L.prossima - L.soglia) * 100);
  const da30 = now - 30 * DAY, ids = Object.keys(S.giocatori);
  const perG = punteggi(da30, now + 1), perS = {};
  let minSett = 0;
  for (const c of S.comp) {
    if (c.annullato) continue;
    if (c.ts >= da30) perS[c.stanza || "Altro"] = (perS[c.stanza || "Altro"] || 0) + (c.punti || 0);
    if (c.ts >= now - 7 * DAY && (c.giocatori || []).includes(me)) minSett += c.minuti || 0;
  }
  const maxG = Math.max(1, ...Object.values(perG)), sArr = Object.entries(perS).sort((a, b) => b[1] - a[1]), maxS = Math.max(1, ...sArr.map(x => x[1]));
  const storia = S.comp.slice(0, 25);
  return `
  <section class="hero-card fr-stone">
    ${avatar(eroe)}
    ${eroe.pet && window.OLW_SPRITE && OLW_SPRITE.ANIMALI[eroe.pet.specie] ? `<canvas class="pet-cv" data-specie="${eroe.pet.specie}" data-col="${eroe.pet.col | 0}" aria-label="${esc(eroe.pet.nome || OLW_SPRITE.ANIMALI[eroe.pet.specie].nome)}"></canvas>` : ""}
    <div class="stack">
      <span class="hn">${esc(eroe.nome)}</span>
      <span class="muted small">${esc(CLASSI[eroe.classe] || "Avventuriero")} · livello ${L.lv}</span>
      <span class="bar"><i style="width:${pct}%"></i></span>
      <span class="muted small num">${fmt(xp)} / ${fmt(L.prossima)} XP · ${fmt(moneteDi(me))} monete</span>
    </div>
  </section>
  <div class="kv"><span class="muted">Sbloccato al livello ${L.lv}</span><span>${esc(L.sblocco)}</span></div>
  <div class="kv"><span class="muted">Minuti di pulizia negli ultimi 7 giorni</span><span class="num">${fmt(minSett)}</span></div>
  <div class="row-actions"><button class="btn sm" data-act="profilo">Modifica eroe</button><button class="btn sm ghost" data-act="chi">Cambia eroe</button></div>
  ${eroe.pg ? "" : `<div class="notice fr-stone small"><b>Crea il tuo personaggio.</b> Scegli classe, aspetto e colori: lo vedranno anche nella barra in alto.<br><button class="btn prime sm" data-act="profilo">Crea il personaggio</button></div>`}
  <p class="muted small" style="margin:0">Nel creatore trovi i pezzi speciali e gli animali da comprare con le monete.</p>
  <section class="sec"><h3>Punti negli ultimi 30 giorni</h3>
    <div class="bars fr-stone">${ids.map(id => `<div class="brow"><span>${esc(nome(id))}</span><span class="bar"><i style="width:${(perG[id] || 0) / maxG * 100}%"></i></span><span class="num">${fmt(perG[id] || 0)}</span></div>`).join("")}</div>
  </section>
  <section class="sec"><h3>Punti per stanza, ultimi 30 giorni</h3>
    <div class="bars fr-stone">${sArr.length ? sArr.map(([r, v]) => `<div class="brow"><span>${esc(r)}</span><span class="bar"><i style="width:${v / maxS * 100}%;background:var(--arcane)"></i></span><span class="num">${fmt(v)}</span></div>`).join("") : '<span class="muted small">Ancora nessuna missione completata.</span>'}</div>
  </section>
  <section class="sec"><h3>Cronologia</h3>
    <div class="panel fr-stone">${storia.length ? storia.map(c => {
      const puoi = !c.annullato && now - c.ts < DAY;
      return `<div class="hist${c.annullato ? " undone" : ""}"><span style="min-width:0"><b>${esc(c.nome)}</b><br><span class="muted small">${esc((c.giocatori || []).map(nome).join(" e "))} · ${oraBreve(c.ts)}${c.extra ? " · extra" : ""}</span></span>
        <span class="row-actions" style="flex:none;align-items:center"><span class="pts num">${c.punti}</span>${puoi ? `<button class="btn sm ghost" data-act="annulla" data-id="${c.id}">Annulla</button>` : ""}</span></div>`;
    }).join("") : '<p class="muted small">Le missioni completate compaiono qui. Un completamento si può annullare entro 24 ore.</p>'}</div>
  </section>`;
}

function vPremi(now) {
  if (!me || !S.giocatori[me]) return `<div class="notice fr-stone">Scegli il tuo eroe per usare i premi. <button class="btn prime sm" data-act="chi">Scegli l'eroe</button></div>`;
  const monete = moneteDi(me);
  const miei = S.premi.filter(p => p.giocatore === me).sort((a, b) => a.costo - b.costo);
  const daConsegnare = S.riscatti.filter(r => !r.consegnato).sort((a, b) => b.ts - a.ts);
  const p = periodoSfida(now), ids = Object.keys(S.giocatori), sc = punteggi(p.inizio, now);
  let prec = "";
  if (p.prec != null && ids.length >= 2) {
    const ps = punteggi(p.prec, p.inizio), [a, b] = ids;
    const vinc = ps[a] === ps[b] ? null : (ps[a] > ps[b] ? a : b);
    const scelta = S.sfide[String(p.prec)];
    prec = `<div class="notice fr-stone small"><b>Periodo concluso il ${dataBreve(p.inizio - 1)}:</b> ${vinc ? `vince ${esc(nome(vinc))} (${fmt(ps[vinc])} a ${fmt(ps[vinc === a ? b : a])}).` : `pareggio ${fmt(ps[a])} a ${fmt(ps[b])}: organizzate qualcosa di carino insieme.`}
      ${vinc ? (scelta ? `<br>Premio scelto: <b>${esc(scelta.nome)}</b>${scelta.consegnato ? " · consegnato" : ` · <button class="btn sm" data-act="sfidaConsegnato" data-id="${p.prec}">Segna consegnato</button>`}` : `<br>${esc(nome(vinc))} sceglie il premio: <button class="btn sm prime" data-act="sceglipremio" data-id="${p.prec}">Scegli il premio</button>`) : ""}</div>`;
  }
  return `
  <section class="sec">
    <div class="sec-head"><h3>I premi di ${esc(nome(me))}</h3><span class="chip gold num">${fmt(monete)} monete</span></div>
    ${miei.length ? `<div class="list">${miei.map(pr => `<div class="reward fr-stone"><span style="min-width:0"><span class="rn">${esc(pr.nome)}</span><br><span class="muted small num">${fmt(pr.costo)} monete${monete < pr.costo ? ` · ne mancano ${fmt(pr.costo - monete)}` : ""}</span></span>
      <span class="row-actions" style="flex:none"><button class="btn sm ${monete >= pr.costo ? "prime" : ""}" data-act="riscatta" data-id="${pr.id}" ${monete >= pr.costo ? "" : "disabled"}>Riscatta</button><button class="dots" data-act="delpremio" data-id="${pr.id}" aria-label="Elimina ${esc(pr.nome)}">⋯</button></span></div>`).join("")}</div>`
      : `<div class="empty fr-dash small">Nessun premio ancora. Un premio piccolo costa 150 monete, uno medio 450, uno grande 900 (circa un mese di faccende).</div>`}
    <button class="btn" data-act="nuovopremio">Nuovo premio</button>
  </section>
  ${daConsegnare.length ? `<section class="sec"><h3>Da consegnare</h3><div class="list">${daConsegnare.map(r => `<div class="reward fr-stone"><span style="min-width:0"><span class="rn">${esc(r.nome)}</span><br><span class="muted small">per ${esc(nome(r.giocatore))} · ${dataBreve(r.ts)}</span></span><button class="btn sm" data-act="consegnato" data-id="${r.id}">Consegnato</button></div>`).join("")}</div></section>` : ""}
  <section class="sec">
    <div class="sec-head"><h3>Sfida</h3><span class="muted small">${dataBreve(p.inizio)} – ${dataBreve(p.fine - 1)} · mancano ${Math.max(1, Math.ceil((p.fine - now) / DAY))} g</span></div>
    ${duello(sc, ids)}
    ${prec}
    <div class="sec-head"><h3>Premi della sfida</h3><button class="btn sm" data-act="nuovosfidapremio">Aggiungi</button></div>
    ${S.sfidaPremi.length ? `<div class="list">${S.sfidaPremi.map(x => `<div class="reward fr-stone"><span class="rn">${esc(x.nome)}</span><button class="dots" data-act="delsfidapremio" data-id="${x.id}" aria-label="Elimina ${esc(x.nome)}">⋯</button></div>`).join("")}</div>`
      : `<div class="empty fr-dash small">Concordate insieme i regali possibili: a fine periodo chi perde ne regala uno a chi vince.</div>`}
  </section>`;
}

function vSgab() {
  const tab = S.sgab;
  let body;
  if (tab === "scorte") {
    const ps = [...S.prodotti].sort((a, b) => LIVELLI_PRODOTTO.indexOf(b.livello) - LIVELLI_PRODOTTO.indexOf(a.livello) || String(a.tipo).localeCompare(b.tipo));
    body = `${ps.length ? `<div class="list">${ps.map(p => `<div class="jar fr-stone">
      <div class="jt"><b>${esc(p.tipo)}</b><span class="muted small">${esc(p.marca || "")}</span></div>
      <div class="field"><span class="lab">Confezione in uso</span><div class="levels" role="group" aria-label="Livello della confezione in uso">${LIVELLI_PRODOTTO.map(l => `<button data-act="livello" data-id="${p.id}" data-l="${l}" aria-pressed="${p.livello === l}">${l}</button>`).join("")}</div></div>
      <div class="sec-head"><span class="lab">Confezioni nuove, chiuse</span><span class="stepper"><button data-act="scorta" data-id="${p.id}" data-d="-1" aria-label="Una in meno">−</button><span class="num">${p.scorta || 0}</span><button data-act="scorta" data-id="${p.id}" data-d="1" aria-label="Una in più">+</button></span></div>
      <div class="row-actions"><button class="btn sm" data-act="finendo" data-id="${p.id}">Sta finendo</button><button class="btn sm ghost" data-act="delprodotto" data-id="${p.id}">Elimina</button></div>
    </div>`).join("")}</div>` : `<div class="empty fr-dash">Lo sgabuzzino è vuoto. Aggiungi i prodotti che hai in casa: tipo, marca e quante confezioni nuove ci sono.</div>`}
    <button class="btn" data-act="nuovoprodotto">Aggiungi prodotto</button>`;
  } else {
    const sp = [...S.spesa].sort((a, b) => (a.ts || 0) - (b.ts || 0));
    body = `${sp.length ? `<div class="list">${sp.map(x => `<label class="shop fr-stone"><input type="checkbox" id="spesa-${x.id}" data-act="comprato" data-id="${x.id}"><span class="sn">${esc(x.testo)}</span></label>`).join("")}</div>` : `<div class="empty fr-dash">La lista della spesa è vuota. Quando un prodotto sta finendo e non ci sono confezioni nuove, finisce qui da solo.</div>`}
    <button class="btn" data-act="nuovaspesa">Aggiungi alla lista</button>`;
  }
  return `<div class="seg fr-stone" role="group" aria-label="Sezione"><button data-act="sgab" data-t="scorte" aria-pressed="${tab === "scorte"}">Scorte</button><button data-act="sgab" data-t="spesa" aria-pressed="${tab === "spesa"}">Lista della spesa${S.spesa.length ? ` (${S.spesa.length})` : ""}</button></div>${body}`;
}

/* ---------- Pannelli ---------- */
function apriSheet(html, onMount) {
  chiudiSheet();
  const scrim = document.createElement("div");
  scrim.className = "scrim"; scrim.id = "scrim";
  scrim.innerHTML = `<div class="sheet fr-stone2" role="dialog" aria-modal="true">${html}</div>`;
  scrim.addEventListener("click", e => { if (e.target === scrim && !scrim.dataset.lock) chiudiSheet(); });
  document.body.appendChild(scrim);
  const sh = scrim.querySelector(".sheet");
  sh.querySelectorAll("[data-close]").forEach(b => b.addEventListener("click", chiudiSheet));
  if (onMount) onMount(sh, scrim);
}
function chiudiSheet() { const s = $("#scrim"); if (s) s.remove(); }
const radio = (name, opts, sel) => `<div class="radios">${opts.map(([v, l]) => `<label><input type="radio" name="${name}" value="${esc(v)}" ${String(v) === String(sel) ? "checked" : ""}><span>${esc(l)}</span></label>`).join("")}</div>`;
const val = (sh, n) => { const el = sh.querySelector(`[name="${n}"]:checked`) || sh.querySelector(`[name="${n}"]`); return el ? el.value : ""; };

function apriChi() {
  const ids = Object.keys(S.giocatori);
  apriSheet(`<h2>Chi sta giocando?</h2>
    <p class="muted small" style="margin:0">Ogni telefono ricorda il suo eroe. Puoi cambiarlo quando vuoi toccando il nome in alto.</p>
    <div class="list">${ids.map(id => { const g = S.giocatori[id]; return `<button class="pick fr-stone2" data-pick="${id}">${avatar(g, "sm")}<span class="stack"><b>${esc(g.nome)}</b><span class="muted small">${esc(CLASSI[g.classe] || "")} · livello ${livelloDa(xpDi(id)).lv}</span></span></button>`; }).join("")}</div>
    <div class="sheet-actions"><button class="btn" id="nuovoEroe">Nuovo eroe</button>${me && S.giocatori[me] ? '<button class="btn ghost" data-close>Chiudi</button>' : ""}</div>`, (sh, scrim) => {
    if (!(me && S.giocatori[me])) scrim.dataset.lock = "1";
    sh.querySelectorAll("[data-pick]").forEach(b => b.onclick = () => { salvaEroe(b.dataset.pick); chiudiSheet(); render(); toast("Giochi come " + nome(me)); });
    sh.querySelector("#nuovoEroe").onclick = () => apriProfilo(null, !(me && S.giocatori[me]));
  });
}

/* ---------- Creatore del personaggio ---------- */
const SP = () => window.OLW_SPRITE, LPC = () => SP().catalogo();
const pezzoDi = (slot, id) => LPC().slot[slot].find(x => x.id === id);
const pezzoOk = (slot, id, corpo) => { const v = pezzoDi(slot, id); return !!v && SP().compatibile(v, corpo); };
function convalida(pg) {
  /* Toglie o sostituisce i pezzi che non esistono per il corpo scelto. */
  const out = { ...pg };
  for (const slot of Object.keys(LPC().slot)) {
    const x = out[slot]; if (!x) continue;
    if (pezzoOk(slot, x.id, out.corpo)) continue;
    const s = (SOSTITUTI[slot] || []).find(i => pezzoOk(slot, i, out.corpo));
    out[slot] = s ? { id: s, col: x.col } : null;
  }
  return out;
}
function applicaKit(pg, classe, conCapelli) {
  const k = KIT[classe] || {}, out = { ...pg, classe };
  for (const slot of Object.keys(LPC().slot)) if (slot !== "capelli") out[slot] = k[slot] ? { ...k[slot] } : null;
  if (conCapelli || !out.capelli) out.capelli = { ...k.capelli };
  return convalida(out);
}
const pgIniziale = classe => applicaKit({ corpo: "female", pelle: "light", occhi: "brown", sopr: "thin" }, classe, true);
const hexColore = (mat, col) => { if (/^#/.test(col)) return col; try { return SP().hexDi(mat, col); } catch (e) { return "#8a8494"; } };
const MATERIALE_SLOT = { capelli: "hair", busto: "cloth", gambe: "cloth", scarpe: "cloth", mantello: "cloth", cappello: "cloth" };

function apriProfilo(id, obbligatorio) {
  const g = id ? S.giocatori[id] : {};
  const D = { nome: g.nome || "", sbloccati: [...(g.sbloccati || [])], pg: null, tab: "corpo", pet: g.pet ? { ...g.pet } : null };
  const aperto = SP().carica().then(() => {
    D.pg = g.pg ? convalida({ ...g.pg }) : pgIniziale(g.classe && CLASSI[g.classe] ? g.classe : "strega");
    if (!D.pg.classe) D.pg.classe = g.classe || "strega";
  });
  apriSheet(`<h2>${id ? "Il tuo eroe" : "Nuovo eroe"}</h2><p class="muted small" style="margin:0">Caricamento dei pezzi…</p>`, async (sh, scrim) => {
    if (obbligatorio) scrim.dataset.lock = "1";
    try { await aperto; } catch (e) { sh.innerHTML = `<h2>Eroe</h2><p class="err">Non riesco a caricare i pezzi del personaggio. Controlla la connessione e riprova.</p><div class="sheet-actions"><button class="btn ghost" data-close>Chiudi</button></div>`; console.error(e); return; }
    const monete = () => (id ? moneteDi(id) : 0);
    const possiede = (slot, i) => !PREZZO[slot] || ((KIT[D.pg.classe] || {})[slot] || {}).id === i || D.sbloccati.includes(slot + "/" + i);
    const TAB = [["corpo", "Corpo"], ["capelli", "Capelli"], ["vestiti", "Vestiti"], ["extra", "Extra"], ["oggetti", "Oggetti"], ["animali", "Animali"]];
    sh.innerHTML = `<h2>${id ? "Il tuo eroe" : "Nuovo eroe"}</h2>
      <div class="field"><label for="cNome">Nome</label><input type="text" id="cNome" maxlength="24" value="${esc(D.nome)}"></div>
      <div class="field"><span class="lab">Classe</span><div class="cr-classi" id="cClassi"></div></div>
      <div class="cr-prev fr-dash"><canvas id="cPrev" aria-label="Anteprima del personaggio"></canvas><canvas id="cPetPrev" aria-label="Anteprima dell'animale"></canvas><button class="btn sm ghost" id="cGira" type="button">Gira</button></div>
      <div class="radios cr-tabs">${TAB.map(([k, l]) => `<label><input type="radio" name="tab" value="${k}" ${k === D.tab ? "checked" : ""}><span>${l}</span></label>`).join("")}</div>
      <div id="cPan" class="cr-pan"></div>
      <p class="err" id="pErr" hidden></p>
      <div class="sheet-actions">${obbligatorio ? (Object.keys(S.giocatori).length ? '<button class="btn ghost" id="pBack">Indietro</button>' : "") : '<button class="btn ghost" data-close>Annulla</button>'}<button class="btn prime" id="pSalva">Salva</button></div>`;
    const back = sh.querySelector("#pBack"); if (back) back.onclick = apriChi;
    let riga = 2, stop = null, tm = 0;
    let stopPet = null;
    const anteprima = () => { clearTimeout(tm); tm = setTimeout(() => { if (stop) stop(); stop = SP().anima(sh.querySelector("#cPrev"), D.pg, { riga, scala: 4 }); if (stopPet) stopPet(); const pc = sh.querySelector("#cPetPrev"); pc.hidden = !D.pet; if (D.pet) stopPet = SP().animaPet(pc, D.pet, { riga: riga === 1 ? 3 : 0, scala: 3 }); }, 40); };
    const classi = () => { sh.querySelector("#cClassi").innerHTML = Object.entries(CLASSI).map(([k, n]) => `<button type="button" class="cr-card${k === D.pg.classe ? " on" : ""}" data-classe="${k}" aria-pressed="${k === D.pg.classe}"><img src="img/classi/${k}.webp" alt="" loading="lazy"><b>${n}</b><span>${DESC_CLASSE[k]}</span></button>`).join(""); };
    const sw = (slot, mat, lista, cur) => `<div class="sws">${lista.map(c => `<button type="button" class="sw${c === cur ? " on" : ""}" data-for="${slot}" data-col="${esc(c)}" style="background:${hexColore(mat, c)}" title="${esc(c.replace(/_/g, " "))}" aria-label="${esc(c.replace(/_/g, " "))}"></button>`).join("")}</div>`;
    const colori = (slot, extra) => {
      const x = D.pg[slot]; if (!x) return "";
      const v = pezzoDi(slot, x.id); if (!v) return "";
      if (v.varianti) return `<div class="sws">${v.varianti.map(c => `<button type="button" class="sw${c === x.col ? " on" : ""}" data-for="${slot}" data-col="${esc(c)}" style="background:${hexColore("cloth", c)}" title="${esc(c.replace(/_/g, " "))}" aria-label="${esc(c.replace(/_/g, " "))}"></button>`).join("")}</div>`;
      const m = v.materiale || MATERIALE_SLOT[slot]; if (!m || m === "eye") return "";
      const lista = Object.keys(LPC().palette[m].rampe);
      const libero = m === "metal" ? "" : `<label class="sw custom" title="Colore libero"><input type="color" data-for="${slot}" value="${/^#/.test(x.col || "") ? x.col : hexColore(m, x.col || LPC().palette[m].base)}"></label>`;
      return `<div class="sws">${lista.map(c => `<button type="button" class="sw${c === x.col ? " on" : ""}" data-for="${slot}" data-col="${esc(c)}" style="background:${hexColore(m, c)}" title="${esc(c.replace(/_/g, " "))}" aria-label="${esc(c.replace(/_/g, " "))}"></button>`).join("")}${libero}</div>`;
    };
    const blocco = (slot, titolo, { nessuno } = {}) => {
      const lista = LPC().slot[slot].filter(v => SP().compatibile(v, D.pg.corpo)), cur = D.pg[slot] && D.pg[slot].id;
      const chips = lista.map(v => { const ok = possiede(slot, v.id); return `<button type="button" class="opt${v.id === cur ? " on" : ""}${ok ? "" : " lock"}" data-slot="${slot}" data-id="${v.id}">${esc(v.nome)}${ok ? "" : ` <span class="prz">${ICON.coin()}<b class="num">${PREZZO[slot]}</b></span>`}</button>`; }).join("");
      return `<div class="field"><span class="lab">${titolo}</span><div class="opts">${nessuno ? `<button type="button" class="opt${cur ? "" : " on"}" data-slot="${slot}" data-id="">Nessuno</button>` : ""}${chips}</div>${colori(slot)}</div>`;
    };
    const HEX_PET = { bianco: "#f2f0ee", dorato: "#e0b24a", rosso: "#b5532f", nero: "#2b2b33", marrone: "#8a5430" };
    const pannelloAnimali = () => {
      const A = SP().ANIMALI, cur = D.pet && D.pet.specie;
      const chips = Object.entries(A).map(([k, a]) => { const ok = D.sbloccati.includes("pet/" + k); return `<button type="button" class="opt${k === cur ? " on" : ""}${ok ? "" : " lock"}" data-pet="${k}">${a.nome}${ok ? "" : ` <span class="prz">${ICON.coin()}<b class="num">${PREZZO.animale}</b></span>`}</button>`; }).join("");
      const cols = cur ? `<div class="field"><span class="lab">Colore del pelo</span><div class="sws">${A[cur].colori.map((c, i) => `<button type="button" class="sw${(D.pet.col | 0) === i ? " on" : ""}" data-petcol="${i}" style="background:${HEX_PET[c]}" title="${c}" aria-label="${c}"></button>`).join("")}</div></div><div class="field"><label for="cPetNome">Nome dell'animale</label><input type="text" id="cPetNome" maxlength="20" value="${esc(D.pet.nome || "")}"></div>` : "";
      return `<div class="field"><span class="lab">Compagno di avventure</span><div class="opts"><button type="button" class="opt${cur ? "" : " on"}" data-pet="">Nessuno</button>${chips}</div></div>${cols}<p class="muted small" style="margin:0">Ne hai ${fmt(monete())} monete. L'animale ti accompagna e compare nella tua scheda.</p>`;
    };
    const pannello = () => {
      const pg = D.pg, el = sh.querySelector("#cPan"); let h = "";
      if (D.tab === "corpo") h = `
        <div class="field"><span class="lab">Genere</span>${radio("corpo", [["female", "Femminile"], ["male", "Maschile"]], pg.corpo)}</div>
        <div class="field"><span class="lab">Carnagione</span>${sw("pelle", "body", PELLI, pg.pelle)}<div class="sws"><label class="sw custom" title="Colore libero"><input type="color" data-for="pelle" value="${/^#/.test(pg.pelle || "") ? pg.pelle : hexColore("body", pg.pelle || "light")}"></label></div></div>
        <div class="field"><span class="lab">Occhi</span>${sw("occhi", "eye", Object.keys(LPC().palette.eye.rampe), pg.occhi)}<div class="sws"><label class="sw custom" title="Colore libero"><input type="color" data-for="occhi" value="${/^#/.test(pg.occhi || "") ? pg.occhi : hexColore("eye", pg.occhi || "blue")}"></label></div></div>
        <div class="field"><span class="lab">Sopracciglia</span>${radio("sopr", [["thin", "Sottili"], ["thick", "Folte"]], pg.sopr || "thin")}</div>
        ${blocco("orecchie", "Orecchie", { nessuno: true })}${blocco("corna", "Corna", { nessuno: true })}${blocco("coda", "Coda", { nessuno: true })}${blocco("ali", "Ali", { nessuno: true })}`;
      else if (D.tab === "capelli") h = blocco("capelli", "Stile dei capelli") + blocco("barba", "Barba e baffi", { nessuno: true });
      else if (D.tab === "vestiti") h = blocco("busto", "Busto") + blocco("gambe", "Gambe") + blocco("scarpe", "Scarpe") + blocco("mantello", "Mantello", { nessuno: true }) + blocco("cappello", "Cappello", { nessuno: true });
      else if (D.tab === "extra") h = blocco("accessorio", "Occhiali e orecchini", { nessuno: true }) + blocco("collo", "Collo", { nessuno: true }) + blocco("vita", "Cintura e fusciacca", { nessuno: true }) + blocco("braccia", "Guanti, bracciali e spalline", { nessuno: true }) + blocco("schiena", "Sulla schiena", { nessuno: true });
      else if (D.tab === "animali") h = pannelloAnimali();
      else h = blocco("arma", "Bastone, arma o attrezzo", { nessuno: true }) + blocco("scudo", "Scudo", { nessuno: true }) + `<p class="muted small" style="margin:0">Gli oggetti con le monete si comprano toccandoli. Ne hai ${fmt(monete())}.</p>`;
      el.innerHTML = h;
    };
    const tutto = () => { classi(); pannello(); anteprima(); };
    const cambia = f => { f(D.pg); D.pg = convalida(D.pg); pannello(); anteprima(); };
    tutto();
    sh.addEventListener("change", e => {
      const t = e.target;
      if (t.name === "tab") { D.tab = t.value; pannello(); }
      else if (t.name === "corpo") cambia(p => { p.corpo = t.value; });
      else if (t.name === "sopr") cambia(p => { p.sopr = t.value; });
      else if (t.type === "color") cambia(p => { setCol(p, t.dataset.for, t.value); });
    });
    sh.addEventListener("input", e => { const t = e.target; if (t.type === "color") { setCol(D.pg, t.dataset.for, t.value); anteprima(); } });
    const setCol = (p, slot, c) => { if (slot === "pelle" || slot === "occhi") p[slot] = c; else if (p[slot]) p[slot] = { ...p[slot], col: c }; };
    const acquista = (chiave, nomePezzo, prezzo, poi) => {
      if (!id) { toast("Lo compri dopo aver creato l'eroe, con le monete guadagnate"); return; }
      if (monete() < prezzo) { toast(`Ti servono ${prezzo} monete: ne hai ${fmt(monete())}`); return; }
      conferma("Comprare questo pezzo?", `${esc(nomePezzo)} costa ${fmt(prezzo)} monete. Te ne restano ${fmt(monete() - prezzo)}.`, "Compra", async () => {
        try {
          await db.collection("riscatti").add({ nome: "Negozio: " + nomePezzo, costo: prezzo, giocatore: id, ts: Date.now(), consegnato: true, negozio: true });
          D.sbloccati.push(chiave); await db.doc("giocatori/" + id).update({ sbloccati: D.sbloccati });
          toast("Comprato: " + nomePezzo); poi();
        } catch (er) { errore(er); }
      });
    };
    sh.addEventListener("input", e => { if (e.target.id === "cPetNome" && D.pet) D.pet.nome = e.target.value; });
    sh.addEventListener("click", e => {
      const pb = e.target.closest("[data-pet]"), pc = e.target.closest("[data-petcol]");
      if (pb) {
        const k = pb.dataset.pet;
        if (!k) { D.pet = null; pannello(); anteprima(); return; }
        const metti = () => { D.pet = { specie: k, col: D.pet && D.pet.specie === k ? D.pet.col : 0, nome: (D.pet && D.pet.nome) || "" }; pannello(); anteprima(); };
        if (D.sbloccati.includes("pet/" + k)) metti(); else acquista("pet/" + k, SP().ANIMALI[k].nome, PREZZO.animale, metti);
        return;
      }
      if (pc) { D.pet = { ...D.pet, col: +pc.dataset.petcol }; pannello(); anteprima(); return; }
      const cl = e.target.closest("[data-classe]"), op = e.target.closest(".opt"), co = e.target.closest(".sw[data-col]");
      if (cl) { D.pg = applicaKit(D.pg, cl.dataset.classe, false); tutto(); return; }
      if (co) { cambia(p => setCol(p, co.dataset.for, co.dataset.col)); return; }
      if (e.target.closest("#cGira")) { riga = [2, 1, 0, 3][([2, 1, 0, 3].indexOf(riga) + 1) % 4]; anteprima(); return; }
      if (!op) return;
      const slot = op.dataset.slot, pid = op.dataset.id;
      if (!pid) { cambia(p => { p[slot] = null; }); return; }
      if (!possiede(slot, pid)) {
        const v = pezzoDi(slot, pid), c = PREZZO[slot];
        if (!id) { toast("Lo compri dopo aver creato l'eroe, con le monete guadagnate"); return; }
        if (monete() < c) { toast(`Ti servono ${c} monete: ne hai ${fmt(monete())}`); return; }
        conferma("Comprare questo pezzo?", `${esc(v.nome)} costa ${fmt(c)} monete. Te ne restano ${fmt(monete() - c)}.`, "Compra", async () => {
          try {
            await db.collection("riscatti").add({ nome: "Negozio: " + v.nome, costo: c, giocatore: id, ts: Date.now(), consegnato: true, negozio: true });
            D.sbloccati.push(slot + "/" + pid); await db.doc("giocatori/" + id).update({ sbloccati: D.sbloccati });
            toast("Comprato: " + v.nome); cambia(p => { p[slot] = { id: pid, col: (p[slot] && p[slot].col) || null }; });
          } catch (er) { errore(er); }
        });
        return;
      }
      const v = pezzoDi(slot, pid), prima = D.pg[slot];
      cambia(p => { p[slot] = { id: pid, col: prima && prima.col && (v.varianti ? v.varianti.includes(prima.col) : true) ? prima.col : (KIT[p.classe] && KIT[p.classe][slot] && KIT[p.classe][slot].id === pid ? KIT[p.classe][slot].col : null) }; });
    });
    sh.querySelector("#pSalva").onclick = async () => {
      const n = sh.querySelector("#cNome").value.trim();
      if (!n) { const e = sh.querySelector("#pErr"); e.textContent = "Scrivi un nome per l'eroe."; e.hidden = false; return; }
      try {
        const dati = { nome: n, classe: D.pg.classe, pg: D.pg, sbloccati: D.sbloccati, pet: D.pet || null };
        if (id) await db.doc("giocatori/" + id).update(dati);
        else { const ref = db.collection("giocatori").doc(); await ref.set({ ...dati, ts: Date.now(), archivio: {} }); salvaEroe(ref.id); }
        if (stop) stop(); if (stopPet) stopPet(); chiudiSheet(); render(); toast(id ? "Eroe aggiornato" : "Benvenuto, " + n);
      } catch (e) { errore(e); }
    };
    scrim.addEventListener("remove", () => stop && stop());
  });
}

function formFaccenda(f, modo) {
  const rs = [...stanze(), "Tutta la casa"];
  const oggi = new Date().toISOString().slice(0, 10);
  const tipo = f ? f.tipo : (modo === "extra" ? "occasionale" : "ricorrente");
  const titolo = modo === "extra" ? "Faccenda fuori lista" : f ? "Modifica faccenda" : "Nuova faccenda";
  const lastNow = f ? infoFaccenda(f, ultimeComp(), Date.now()).last : 0;
  apriSheet(`<h2>${titolo}</h2>
    ${modo === "extra" ? '<p class="muted small" style="margin:0">Se la faccenda è già nel registro, usa il suo pulsante Fatta: anche in anticipo, fa ripartire la scadenza.</p>' : ""}
    <div class="field"><label for="fNome">Nome</label><input type="text" id="fNome" name="nome" maxlength="60" value="${esc(f ? f.nome : "")}"></div>
    <div class="field"><label for="fStanza">Stanza</label><select id="fStanza" name="stanza">${rs.map(r => `<option ${f && f.stanza === r ? "selected" : ""}>${esc(r)}</option>`).join("")}</select></div>
    <div class="field"><label for="fMin">Durata in minuti</label><input type="number" id="fMin" name="minuti" min="1" max="1440" inputmode="numeric" value="${f ? f.minuti : 15}"></div>
    <div class="field"><span class="lab">Difficoltà</span>${radio("diff", [1, 2, 3, 4, 5].map(n => [n, n]), f ? f.diff : 2)}</div>
    <div class="field"><span class="lab">Sbatti</span>${radio("sbatti", [1, 2, 3, 4, 5].map(n => [n, n]), f ? f.sbatti : 3)}<span class="muted small">1 = nessun problema, 5 = farei qualsiasi altra cosa</span></div>
    ${modo === "extra" ? "" : `<div class="field"><span class="lab">Tipo</span>${radio("tipo", [["ricorrente", "Ricorrente"], ["occorrenza", "All'occorrenza"], ["occasionale", "Una volta"]], tipo)}</div>
    <div id="fRic" class="field" ${tipo === "ricorrente" ? "" : "hidden"}>
      <span class="lab">Ogni quanti giorni</span>${radio("freqQ", [[3, "3"], [7, "7"], [14, "14"], [30, "30"], [60, "60"], [90, "90"], [180, "180"], [365, "365"]], f && f.freq ? f.freq : 7)}
      <label for="fUlt" class="lab" style="margin-top:6px">Ultima volta fatta</label><input type="date" id="fUlt" name="ultima" value="${f && lastNow ? new Date(lastNow).toISOString().slice(0, 10) : oggi}" max="${oggi}">
    </div>`}
    <div class="preview"><span class="muted" id="fCat">Categoria</span><span class="pts num" id="fPts">0</span></div>
    <p class="err" id="fErr" hidden></p>
    <div class="sheet-actions">${f ? '<button class="btn ghost" id="fDel">Elimina</button>' : ""}<button class="btn ghost" data-close>Annulla</button><button class="btn prime" id="fSalva">${modo === "extra" ? "Segna come fatta" : "Salva"}</button></div>`, sh => {
    const upd = () => {
      const m = +sh.querySelector("#fMin").value || 0, s = +val(sh, "sbatti");
      sh.querySelector("#fPts").textContent = m > 0 ? puntiBase(m, +val(sh, "diff"), s) + " punti" : "–";
      sh.querySelector("#fCat").textContent = "Categoria: " + CAT[categoria({ minuti: m, sbatti: s })].nome;
      const ric = sh.querySelector("#fRic"); if (ric) ric.hidden = val(sh, "tipo") !== "ricorrente";
    };
    sh.addEventListener("input", upd); sh.addEventListener("change", upd); upd();
    const del = sh.querySelector("#fDel");
    if (del) del.onclick = () => {
      if (del.dataset.ok) { db.doc("faccende/" + f.id).update({ attiva: false }).then(() => { chiudiSheet(); toast("Faccenda eliminata"); }, errore); return; }
      del.dataset.ok = "1"; del.textContent = "Tocca di nuovo per eliminare"; del.classList.add("danger");
    };
    sh.querySelector("#fSalva").onclick = async () => {
      const nomeF = sh.querySelector("#fNome").value.trim(), minuti = Math.round(+sh.querySelector("#fMin").value);
      const err = sh.querySelector("#fErr");
      if (!nomeF) { err.textContent = "Scrivi il nome della faccenda."; err.hidden = false; return; }
      if (!(minuti > 0)) { err.textContent = "Indica quanti minuti ci vogliono, almeno 1."; err.hidden = false; return; }
      const dati = { nome: nomeF, stanza: sh.querySelector("#fStanza").value, minuti, diff: +val(sh, "diff"), sbatti: +val(sh, "sbatti") };
      try {
        if (modo === "extra") {
          const now = Date.now();
          const ref = await db.collection("faccende").add({ ...dati, tipo: "occasionale", freq: null, base: now, ultima: now, attiva: false });
          const punti = puntiBase(dati.minuti, dati.diff, dati.sbatti);
          const cref = await db.collection("completamenti").add({ faccendaId: ref.id, nome: dati.nome, stanza: dati.stanza, minuti: dati.minuti, giocatori: [me], punti, ts: now, annullato: false, extra: true, prevUltima: 0 });
          chiudiSheet(); toast(`+${punti} punti per la faccenda extra`, { label: "Annulla", fn: () => annulla(cref.id) }); return;
        }
        const t = val(sh, "tipo");
        dati.tipo = t; dati.freq = t === "ricorrente" ? +val(sh, "freqQ") : null;
        const u = sh.querySelector("#fUlt");
        if (t === "ricorrente" && u && u.value && u.value !== (lastNow ? new Date(lastNow).toISOString().slice(0, 10) : oggi)) { const d = Date.parse(u.value + "T12:00:00"); dati.base = d; dati.ultima = d; }
        if (f) await db.doc("faccende/" + f.id).update(dati);
        else await db.collection("faccende").add({ ...dati, base: dati.base || Date.now(), attiva: true });
        chiudiSheet(); toast(f ? "Faccenda aggiornata" : "Faccenda aggiunta");
      } catch (e) { errore(e); }
    };
  });
}

async function completa(f, chi) {
  const now = Date.now();
  const i = infoFaccenda(f, ultimeComp(), now);
  const mg = missioneGiorno(now), bonus = !!(mg && !mg.fatta && mg.id === f.id);
  const punti = bonus ? Math.round(i.punti * (1 + BONUS_GIORNO)) : i.punti;
  try {
    const ref = await db.collection("completamenti").add({ faccendaId: f.id, nome: f.nome, stanza: f.stanza, minuti: f.minuti, giocatori: chi, punti, ts: now, annullato: false, extra: false, prevUltima: f.ultima || 0, bonus });
    if (bonus) await db.doc("config/casa").update({ missioneGiorno: { ...S.config.missioneGiorno, fatta: true, fattaDa: chi } });
    const upd = { ultima: now };
    if (f.tipo === "occasionale") upd.attiva = false;
    if (f.prenDa) { upd.prenDa = null; upd.prenFino = 0; }
    await db.doc("faccende/" + f.id).update(upd);
    if (bonus) festa(`Missione del giorno compiuta! +${punti}`);
    toast(`+${punti} · ${f.nome}`, { label: "Annulla", fn: () => annulla(ref.id) });
  } catch (e) { errore(e); }
}
async function annulla(cid) {
  try {
    const cs = await db.doc("completamenti/" + cid).get(); if (!cs.exists) return;
    const c = cs.data(); if (c.annullato) return;
    await db.doc("completamenti/" + cid).update({ annullato: true });
    const f = S.faccende.find(x => x.id === c.faccendaId);
    if (f && !c.extra) {
      const upd = {};
      if (f.ultima === c.ts) upd.ultima = c.prevUltima || 0;
      if (f.tipo === "occasionale") upd.attiva = true;
      if (Object.keys(upd).length) await db.doc("faccende/" + f.id).update(upd);
    }
    const mg = S.config && S.config.missioneGiorno;
    if (c.bonus && mg && mg.id === c.faccendaId && mg.giorno === oggiKey(c.ts)) await db.doc("config/casa").update({ missioneGiorno: { ...mg, fatta: false, fattaDa: null } });
    toast("Completamento annullato");
  } catch (e) { errore(e); }
}

function apriInsieme(f) {
  const ids = Object.keys(S.giocatori);
  const i = infoFaccenda(f, ultimeComp(), Date.now());
  apriSheet(`<h2>Fatta insieme</h2>
    <div class="preview"><span class="muted">${esc(f.nome)}</span><span class="pts num">+${i.punti} a testa</span></div>
    <div class="field"><span class="lab">Chi l'ha fatta</span><div class="radios">${ids.map(id => `<label><input type="checkbox" name="chi" value="${id}" ${id === me ? "checked" : ""}><span>${esc(nome(id))}</span></label>`).join("")}</div></div>
    <p class="err" id="cErr" hidden></p>
    <div class="sheet-actions"><button class="btn ghost" data-close>Annulla</button><button class="btn prime" id="cOk">Missione compiuta</button></div>`, sh => {
    sh.querySelector("#cOk").onclick = async () => {
      const chi = [...sh.querySelectorAll('[name="chi"]:checked')].map(x => x.value);
      if (!chi.length) { const e = sh.querySelector("#cErr"); e.textContent = "Scegli almeno un eroe."; e.hidden = false; return; }
      chiudiSheet(); await completa(f, chi);
    };
  });
}

function apriMenu(f) {
  const ids = Object.keys(S.giocatori);
  apriSheet(`<h2>${esc(f.nome)}</h2>
    <div class="list">
      ${ids.length > 1 ? '<button class="btn" id="mIns">Fatta insieme a un altro eroe</button>' : ""}
      <button class="btn" id="mMod">Modifica faccenda</button>
      <button class="btn ghost" data-close>Chiudi</button>
    </div>`, sh => {
    const ins = sh.querySelector("#mIns"); if (ins) ins.onclick = () => apriInsieme(f);
    sh.querySelector("#mMod").onclick = () => formFaccenda(f);
  });
}

function apriImpostazioni() {
  const cfg = S.config || {};
  apriSheet(`<h2>La casa</h2>
    <div class="field"><label for="sNome">Nome della casa</label><input type="text" id="sNome" maxlength="40" value="${esc(cfg.nome || "Our little world")}"></div>
    <div class="field"><span class="lab">Dimora</span>${radio("dimora", Object.entries(DIMORE).filter(([k]) => SKIN[k]).map(([k, v]) => [k, v.replace(/^(Il|La|L') ?/, "")]), SKIN[cfg.dimora] ? cfg.dimora : "castello")}<span class="muted small">Le altre dimore arrivano presto: la pianta resta la stessa.</span></div>
    <div class="field"><span class="lab">Pianta della casa</span><button class="btn" id="sPianta">Apri la pianta</button><span class="muted small">Le tue stanze vere, disegnate in piccolo. Valgono per ogni dimora.</span></div>
    <div class="field"><span class="lab">Durata della sfida</span>${radio("sfida", [[14, "2 settimane"], [30, "1 mese"]], cfg.sfidaGiorni || 14)}<span class="muted small">La nuova durata vale dal periodo in corso: i punti già fatti restano.</span></div>
    <div class="field"><label for="sStanza">Aggiungi una stanza</label><div class="row-actions"><input type="text" id="sStanza" maxlength="30" style="flex:1;min-width:0;background:var(--ink);border:1px solid var(--seam);border-radius:10px;padding:10px 12px"><button class="btn" id="sAdd">Aggiungi</button></div><span class="muted small">${esc(stanze().join(", "))}</span></div>
    <div class="field"><span class="lab">Crediti</span><button class="btn ghost" id="sCrediti">Chi ha disegnato i personaggi</button></div>
    <div class="field"><span class="lab">Account</span><div class="row-actions" style="align-items:center"><span class="muted small" style="flex:1;min-width:0;overflow-wrap:anywhere">${esc(utente ? utente.email : "")}</span><button class="btn sm ghost" id="sEsci">Esci</button></div></div>
    <div class="sheet-actions"><button class="btn ghost" data-close>Chiudi</button><button class="btn prime" id="sSalva">Salva</button></div>`, sh => {
    sh.querySelector("#sPianta").onclick = () => apriPianta();
    sh.querySelector("#sCrediti").onclick = () => apriCrediti();
    sh.querySelector("#sEsci").onclick = async () => { try { localStorage.removeItem("olw-hero"); } catch (e) {} await sb.auth.signOut(); location.reload(); };
    sh.querySelector("#sAdd").onclick = async () => {
      const r = sh.querySelector("#sStanza").value.trim(); if (!r) return;
      try { await db.doc("config/casa").update({ stanze: [...new Set([...(cfg.stanze || []), r])] }); toast("Stanza aggiunta: " + r); sh.querySelector("#sStanza").value = ""; } catch (e) { errore(e); }
    };
    sh.querySelector("#sSalva").onclick = async () => {
      const g = +val(sh, "sfida");
      const dati = { nome: sh.querySelector("#sNome").value.trim() || "Our little world", dimora: val(sh, "dimora"), sfidaGiorni: g };
      if (g !== (cfg.sfidaGiorni || 14)) dati.sfidaInizio = periodoSfida(Date.now()).inizio;
      try { await db.doc("config/casa").update(dati); chiudiSheet(); toast("Casa aggiornata"); } catch (e) { errore(e); }
    };
  });
}

/* Editor della pianta: rettangoli su una griglia, un tipo per stanza. Il tipo decide in quale posto della dimora compare la stanza. */
function apriPianta() {
  const cfg = S.config || {}, W = GRIGLIA.w, H = GRIGLIA.h, base = pianta(), D = {};
  for (const r of Object.keys(base)) D[r] = { ...base[r] };
  let sel = null, drag = null;
  const nFacc = r => S.faccende.filter(f => f.attiva !== false && f.stanza === r).length;
  apriSheet(`<h2>Pianta della casa</h2>
    <p class="muted small" style="margin:0">Trascina una stanza per spostarla, il quadratino in basso a destra per cambiarne la misura. Non serve la scala giusta: basta che si capisca com'è fatta casa.</p>
    <div class="pianta-wrap fr-dash"><svg id="pSvg" viewBox="0 0 ${W} ${H}" role="img" aria-label="Pianta stilizzata della casa"></svg></div>
    <div id="pInfo" class="pianta-info"></div>
    <div class="field"><label for="pNuova">Aggiungi una stanza</label><div class="row-actions"><input type="text" id="pNuova" maxlength="30" style="flex:1;min-width:0;background:var(--night);border:1px solid var(--seam);border-radius:10px;padding:10px 12px"><button class="btn" id="pAdd">Aggiungi</button></div></div>
    <div id="pAvvisi" class="pianta-avvisi small"></div>
    <div class="sheet-actions"><button class="btn ghost" data-close>Annulla</button><button class="btn prime" id="pSalva">Salva la pianta</button></div>`, sh => {
    const svg = sh.querySelector("#pSvg"), info = sh.querySelector("#pInfo"), av = sh.querySelector("#pAvvisi");
    const ridisegna = () => {
      svg.innerHTML = `<defs><pattern id="pg" width="1" height="1" patternUnits="userSpaceOnUse"><path d="M1 0H0V1" fill="none" stroke="#ffffff" stroke-opacity=".07" stroke-width=".04"/></pattern></defs><rect width="${W}" height="${H}" fill="url(#pg)"/>` +
        Object.entries(D).map(([r, q]) => {
          const on = r === sel, nm = nomeStanza(r), max = Math.max(3, Math.floor(q.w * 2.4));
          return `<g data-r="${esc(r)}"><rect class="pr${on ? " on" : ""}${r === "Tutta la casa" ? " fix" : ""}" x="${q.x + .06}" y="${q.y + .06}" width="${q.w - .12}" height="${q.h - .12}" rx=".18" fill="${COL_TIPO[q.tipo] || COL_TIPO.altro}"/>` +
            `<text x="${q.x + q.w / 2}" y="${q.y + q.h / 2 + .18}" text-anchor="middle" class="pt">${esc(nm.length > max ? nm.slice(0, max - 1) + "…" : nm)}</text>` +
            (on ? `<rect class="ph" data-h="1" x="${q.x + q.w - .62}" y="${q.y + q.h - .62}" width=".5" height=".5" rx=".1"/>` : "") + `</g>`;
        }).join("");
      const q = sel && D[sel];
      info.innerHTML = q ? (sel === "Tutta la casa"
        ? `<b>Corridoio</b><span class="muted small">Qui stanno le faccende di "tutta la casa", come l'aspirapolvere. Puoi spostarlo e ridimensionarlo.</span>`
        : `<div class="field"><label for="pTipo"><b>${esc(sel)}</b> · che tipo di stanza è?</label><select id="pTipo">${Object.entries(TIPI).filter(([k]) => k !== "corridoio").map(([k, v]) => `<option value="${k}" ${k === q.tipo ? "selected" : ""}>${esc(v)}</option>`).join("")}</select></div>
           <button class="btn ghost sm" id="pDel" ${nFacc(sel) ? "disabled" : ""}>${nFacc(sel) ? `Ha ${nFacc(sel)} faccende: non si può togliere` : "Togli questa stanza"}</button>`)
        : `<span class="muted small">Tocca una stanza per scegliere il suo tipo.</span>`;
      const t = info.querySelector("#pTipo"); if (t) t.onchange = () => { D[sel].tipo = t.value; ridisegna(); };
      const d = info.querySelector("#pDel"); if (d) d.onclick = () => { delete D[sel]; sel = null; ridisegna(); };
      const per = {}; for (const [r, x] of Object.entries(D)) if (r !== "Tutta la casa") (per[x.tipo] = per[x.tipo] || []).push(r);
      const msg = [];
      for (const [k, v] of Object.entries(per)) if (k !== "altro" && v.length > 1) msg.push(`Hai più stanze di tipo ${TIPI[k].toLowerCase()} (${v.map(esc).join(", ")}): nella dimora compare solo ${esc(v[0])}.`);
      if (per.altro) msg.push(`${per.altro.map(esc).join(", ")}: senza tipo non hanno un posto nella dimora, ma restano tra le stanze e le missioni.`);
      const vuoti = POSTI.filter(po => po.tipo !== "corridoio" && !per[po.tipo]).map(po => TIPI[po.tipo].toLowerCase());
      if (vuoti.length) msg.push(`Nella dimora restano vuoti i posti: ${vuoti.join(", ")}.`);
      av.innerHTML = msg.map(m => `<p class="muted">${m}</p>`).join("");
    };
    const cella = e => { const b = svg.getBoundingClientRect(); return [(e.clientX - b.left) / b.width * W, (e.clientY - b.top) / b.height * H]; };
    svg.addEventListener("pointerdown", e => {
      const g = e.target.closest("g[data-r]"); if (!g) { sel = null; ridisegna(); return; }
      const r = g.dataset.r, q = D[r], [cx, cy] = cella(e), resize = !!e.target.closest("[data-h]");
      sel = r; drag = { r, resize, dx: cx - q.x, dy: cy - q.y, w0: q.w, h0: q.h, x0: cx, y0: cy };
      try { svg.setPointerCapture(e.pointerId); } catch (x) {}
      e.preventDefault(); ridisegna();
    });
    svg.addEventListener("pointermove", e => {
      if (!drag) return; const q = D[drag.r], [cx, cy] = cella(e);
      if (drag.resize) { q.w = Math.max(1, Math.min(W - q.x, Math.round(drag.w0 + cx - drag.x0))); q.h = Math.max(1, Math.min(H - q.y, Math.round(drag.h0 + cy - drag.y0))); }
      else { q.x = Math.max(0, Math.min(W - q.w, Math.round(cx - drag.dx))); q.y = Math.max(0, Math.min(H - q.h, Math.round(cy - drag.dy))); }
      ridisegna();
    });
    const fine = () => { drag = null; };
    svg.addEventListener("pointerup", fine); svg.addEventListener("pointercancel", fine);
    sh.querySelector("#pAdd").onclick = () => {
      const inp = sh.querySelector("#pNuova"), n = inp.value.trim(); if (!n) return;
      if (D[n] || n === "Tutta la casa") { toast("Esiste già una stanza con questo nome"); return; }
      const occ = (x, y) => Object.values(D).some(q => x < q.x + q.w && x + 3 > q.x && y < q.y + q.h && y + 2 > q.y);
      let px = 0, py = 0; outer: for (let y = 0; y <= H - 2; y++) for (let x = 0; x <= W - 3; x++) if (!occ(x, y)) { px = x; py = y; break outer; }
      D[n] = { tipo: tipoDa(n), x: px, y: py, w: 3, h: 2 }; sel = n; inp.value = ""; ridisegna();
    };
    sh.querySelector("#pSalva").onclick = async () => {
      try {
        const nomi = Object.keys(D).filter(r => r !== "Tutta la casa");
        await db.doc("config/casa").update({ pianta: D, stanze: nomi });
        chiudiSheet(); toast("Pianta salvata");
      } catch (e) { errore(e); }
    };
    ridisegna();
  });
}

function apriCrediti() {
  window.OLW_SPRITE.carica().then(() => {
    const cr = window.OLW_SPRITE.catalogo().crediti, autori = [...new Map(cr.flatMap(c => c.autori).map(a => [a.toLowerCase(), a])).values()].sort((a, b) => a.localeCompare(b)), lic = [...new Set(cr.flatMap(c => c.licenze))].sort();
    apriSheet(`<h2>Crediti</h2>
      <p class="muted small" style="margin:0">I personaggi sono composti con gli sprite del <b>Liberated Pixel Cup</b> e dell'<i>Universal LPC Spritesheet Character Generator</i>, opera di tanti artisti. Le immagini restano sotto le loro licenze: ${esc(lic.join(", "))}.</p>
      <div class="panel fr-stone small" style="line-height:1.6">${autori.map(esc).join(" · ")}</div>
      <p class="muted small" style="margin:0">Elenco completo con le fonti: <a href="https://github.com/GiadaJennyQafalia/our-little-world/blob/main/CREDITI.md" target="_blank" rel="noopener">CREDITI.md</a>. Le card delle classi sono illustrazioni generate con l'AI.</p>
      <div class="sheet-actions"><button class="btn ghost" data-close>Chiudi</button></div>`);
  }).catch(() => toast("Non riesco a caricare i crediti"));
}
function apriSemplice(titolo, campi, onSave, nota) {
  apriSheet(`<h2>${titolo}</h2>${nota ? `<p class="muted small" style="margin:0">${nota}</p>` : ""}
    ${campi.map(c => c.radio ? `<div class="field"><span class="lab">${c.label}</span>${radio(c.name, c.radio, c.value)}</div>` : `<div class="field"><label for="x-${c.name}">${c.label}</label><input type="${c.type || "text"}" id="x-${c.name}" name="${c.name}" ${c.type === "number" ? 'inputmode="numeric" min="0"' : 'maxlength="60"'} value="${esc(c.value ?? "")}"></div>`).join("")}
    <p class="err" id="xErr" hidden></p>
    <div class="sheet-actions"><button class="btn ghost" data-close>Annulla</button><button class="btn prime" id="xOk">Salva</button></div>`, sh => {
    sh.querySelector("#xOk").onclick = async () => {
      const v = {}; for (const c of campi) v[c.name] = val(sh, c.name).trim();
      const msg = onSave(v, sh);
      if (typeof msg === "string") { const e = sh.querySelector("#xErr"); e.textContent = msg; e.hidden = false; return; }
      try { await msg; chiudiSheet(); } catch (e) { errore(e); }
    };
  });
}
function conferma(titolo, testo, etichetta, azione) {
  apriSheet(`<h2>${titolo}</h2><p style="margin:0">${testo}</p><div class="sheet-actions"><button class="btn ghost" data-close>Annulla</button><button class="btn prime" id="kOk">${etichetta}</button></div>`, sh => {
    sh.querySelector("#kOk").onclick = async () => { try { await azione(); chiudiSheet(); } catch (e) { errore(e); } };
  });
}

/* ---------- Azioni ---------- */
const trova = (arr, id) => arr.find(x => x.id === id);
const libere = new Set(["pianta", "filtro", "fcat", "fstanza", "sgab", "stanza", "indietro", "vaiMissioni", "chi"]);
document.addEventListener("click", e => {
  const nav = e.target.closest("nav.tabs button");
  if (nav) { S.view = nav.dataset.view; try { localStorage.setItem("olw-view", S.view); } catch (x) {} window.scrollTo(0, 0); render(); return; }
  const b = e.target.closest("[data-act]"); if (!b || b.closest(".sheet")) return;
  if (!db) return;
  const id = b.dataset.id, act = b.dataset.act;
  if (act === "comprato") return;
  if (!(me && S.giocatori[me]) && !libere.has(act)) { apriChi(); return; }
  switch (act) {
    case "chi": apriChi(); break;
    case "pianta": apriPianta(); break;
    case "stanza": S.view = "stanza"; S.stanzaSel = b.dataset.r; render(); window.scrollTo(0, 0); break;
    case "indietro": S.view = "casa"; render(); window.scrollTo(0, 0); break;
    case "vaiMissioni": S.view = "missioni"; S.fStanza = b.dataset.r; S.fCat = "tutte"; render(); window.scrollTo(0, 0); break;
    case "fcat": S.fCat = b.dataset.k; render(); break;
    case "fstanza": S.fStanza = b.dataset.r; render(); break;
    case "cambiaGiorno": cambiaGiorno(); break;
    case "fatta": { const f = trova(S.faccende, id); if (f) { b.disabled = true; completa(f, [me]); } break; }
    case "prenota": {
      const f = trova(S.faccende, id); if (!f) break;
      const mia = f.prenDa === me && f.prenFino > Date.now();
      db.doc("faccende/" + f.id).update(mia ? { prenDa: null, prenFino: 0 } : { prenDa: me, prenFino: Date.now() + 3 * HOUR })
        .then(() => toast(mia ? "Prenotazione tolta" : "Prenotata per 3 ore"), errore);
      break;
    }
    case "menu": { const f = trova(S.faccende, id); if (f) apriMenu(f); break; }
    case "extra": formFaccenda(null, "extra"); break;
    case "profilo": apriProfilo(me, false); break;
    case "annulla": { const c = trova(S.comp, id); if (c) conferma("Annullare il completamento?", `${esc(c.nome)}: i ${c.punti} punti vengono tolti a ${esc((c.giocatori || []).map(nome).join(" e "))}.`, "Annulla completamento", () => annulla(id)); break; }
    case "nuovopremio": apriSemplice("Nuovo premio", [{ name: "nome", label: "Premio" }, { name: "costo", label: "Costo in monete", radio: [[150, "Piccolo · 150"], [450, "Medio · 450"], [900, "Grande · 900"]], value: 450 }], v => v.nome ? db.collection("premi").add({ nome: v.nome, costo: +v.costo, giocatore: me, ts: Date.now() }).then(() => toast("Premio aggiunto")) : "Scrivi il nome del premio.", "Un massaggio, una serata relax, un oggetto che desideri da tempo. Resta in lista anche dopo il riscatto."); break;
    case "delpremio": { const p = trova(S.premi, id); if (p) conferma("Eliminare il premio?", esc(p.nome), "Elimina", () => db.doc("premi/" + id).delete()); break; }
    case "riscatta": { const p = trova(S.premi, id); if (p) conferma("Riscattare il premio?", `${esc(p.nome)} costa ${fmt(p.costo)} monete. A ${esc(nome(me))} restano ${fmt(moneteDi(me) - p.costo)} monete.`, "Riscatta", () => db.collection("riscatti").add({ premioId: p.id, nome: p.nome, costo: p.costo, giocatore: me, ts: Date.now(), consegnato: false }).then(() => toast("Premio riscattato"))); break; }
    case "consegnato": db.doc("riscatti/" + id).update({ consegnato: true }).catch(errore); break;
    case "nuovosfidapremio": apriSemplice("Premio della sfida", [{ name: "nome", label: "Regalo" }], v => v.nome ? db.collection("sfidaPremi").add({ nome: v.nome, ts: Date.now() }) : "Scrivi il regalo."); break;
    case "delsfidapremio": { const p = trova(S.sfidaPremi, id); if (p) conferma("Togliere dalla lista?", esc(p.nome), "Togli", () => db.doc("sfidaPremi/" + id).delete()); break; }
    case "sceglipremio":
      if (!S.sfidaPremi.length) { toast("Aggiungi prima almeno un premio della sfida"); break; }
      apriSemplice("Scegli il premio", [{ name: "p", label: "Premio", radio: S.sfidaPremi.map(x => [x.id, x.nome]), value: S.sfidaPremi[0].id }], v => { const p = trova(S.sfidaPremi, v.p); return db.doc("sfide/" + id).set({ premioId: p.id, nome: p.nome, consegnato: false }); });
      break;
    case "sfidaConsegnato": db.doc("sfide/" + id).update({ consegnato: true }).catch(errore); break;
    case "sgab": S.sgab = b.dataset.t; render(); break;
    case "livello": db.doc("prodotti/" + id).update({ livello: b.dataset.l }).catch(errore); break;
    case "scorta": { const p = trova(S.prodotti, id); if (p) db.doc("prodotti/" + id).update({ scorta: Math.max(0, (p.scorta || 0) + +b.dataset.d) }).catch(errore); break; }
    case "finendo": {
      const p = trova(S.prodotti, id); if (!p) break;
      if ((p.scorta || 0) > 0) conferma(esc(p.tipo), `Hai ${p.scorta} ${p.scorta === 1 ? "confezione nuova" : "confezioni nuove"} nello sgabuzzino. Quando finisci quella in uso, aprine una con "Apri confezione".`, "Apri confezione ora", () => db.doc("prodotti/" + id).update({ scorta: p.scorta - 1, livello: "pieno" }).then(() => toast("Confezione nuova aperta")));
      else if (S.spesa.some(x => x.prodottoId === id)) toast("È già nella lista della spesa");
      else db.collection("spesa").add({ testo: p.tipo + (p.marca ? " · " + p.marca : ""), prodottoId: id, ts: Date.now() }).then(() => { db.doc("prodotti/" + id).update({ livello: "quasi finito" }); toast("Nessuna confezione nuova: aggiunto alla lista della spesa"); }, errore);
      break;
    }
    case "delprodotto": { const p = trova(S.prodotti, id); if (p) conferma("Eliminare il prodotto?", esc(p.tipo), "Elimina", () => db.doc("prodotti/" + id).delete()); break; }
    case "nuovoprodotto": apriSemplice("Nuovo prodotto", [{ name: "tipo", label: "Tipo (es. sgrassatore)" }, { name: "marca", label: "Marca" }, { name: "livello", label: "Confezione in uso", radio: LIVELLI_PRODOTTO.map(l => [l, l]), value: "pieno" }, { name: "scorta", label: "Confezioni nuove, chiuse", type: "number", value: 0 }], v => v.tipo ? db.collection("prodotti").add({ tipo: v.tipo, marca: v.marca, scorta: Math.max(0, Math.round(+v.scorta || 0)), livello: v.livello, ts: Date.now() }).then(() => toast("Prodotto aggiunto")) : "Scrivi il tipo di prodotto."); break;
    case "nuovaspesa": apriSemplice("Lista della spesa", [{ name: "testo", label: "Cosa comprare" }], v => v.testo ? db.collection("spesa").add({ testo: v.testo, prodottoId: null, ts: Date.now() }) : "Scrivi cosa comprare."); break;
  }
});
document.addEventListener("change", e => {
  const b = e.target.closest('[data-act="comprato"]'); if (!b || !b.checked) return;
  const x = trova(S.spesa, b.dataset.id); if (!x) return;
  const p = x.prodottoId ? trova(S.prodotti, x.prodottoId) : null;
  b.checked = false;
  const aprire = !p || p.livello === "finito" || p.livello === "quasi finito";
  apriSemplice("Comprato", [
    { name: "tipo", label: "Tipo", value: p ? p.tipo : x.testo }, { name: "marca", label: "Marca", value: p ? p.marca : "" },
    { name: "q", label: "Quante confezioni", type: "number", value: 1 },
    { name: "dest", label: "Cosa fai con quella nuova", radio: [["apri", "La apro subito"], ["scorta", "La metto in scorta"]], value: aprire ? "apri" : "scorta" }
  ], v => {
    const q = Math.max(1, Math.round(+v.q || 1));
    if (!v.tipo) return "Scrivi il tipo di prodotto.";
    const apri = v.dest === "apri";
    const dati = { tipo: v.tipo, marca: v.marca, scorta: (p ? p.scorta || 0 : 0) + (apri ? q - 1 : q) };
    if (apri) dati.livello = "pieno";
    const fatto = p ? db.doc("prodotti/" + p.id).update(dati) : db.collection("prodotti").add({ ...dati, livello: apri ? "pieno" : "finito", ts: Date.now() });
    return fatto.then(() => db.doc("spesa/" + x.id).delete()).then(() => toast(apri ? "Confezione nuova in uso" : "Messo in scorta nello sgabuzzino"));
  }, "Se la apri subito sostituisce quella finita; altrimenti resta chiusa nello sgabuzzino.");
});
$("#fab").onclick = () => db && me && formFaccenda(null);
$("#btnSettings").onclick = () => { if (db && me && S.giocatori[me]) apriImpostazioni(); else if (db) apriChi(); };
$("#heroChip").onclick = () => db && apriChi();
setInterval(() => { if (!$("#scrim")) render(); }, 60000);

/* ---------- Avvio ---------- */
function leggiCollegamento() {
  const c = window.OLW_CONFIG || {};
  if (c.supabaseUrl && c.supabaseKey) return { url: c.supabaseUrl, key: c.supabaseKey };
  try { const x = JSON.parse(localStorage.getItem("olw-sb") || "null"); if (x && x.url && x.key) return x; } catch (e) {}
  return null;
}
function schermata(html, onMount) {
  document.body.classList.add("pre");
  $("#view").innerHTML = `<section class="gate">${html}</section>`;
  if (onMount) onMount($("#view .gate"));
}
const stemma = `<div class="gate-crest">${pix([
  "......aa......", ".....abba.....", "....abbbba....", "...abbbbbba...", "..abbbbbbbba..", ".aaaaaaaaaaaa.",
  "..bccbbbbccb..", "..bccbbbbccb..", "..bbbbddbbbb..", "..bbbbddbbbb..", "..bbbbddbbbb..", ".eeeeeeeeeeee."
], { a: "#7a4a6a", b: "#4b3f5c", c: "#f2c062", d: "#2a1f33", e: "#3c5a3a" }, "crest")}</div>`;

function chiediCollegamento(msg) {
  schermata(`${stemma}<h2>Collega il regno</h2>
    <p class="muted small">Serve una volta sola per telefono: incolla i due valori che trovi in Supabase → Project Settings → API.</p>
    <div class="field"><label for="gUrl">Project URL</label><input type="text" id="gUrl" placeholder="https://xxxx.supabase.co" autocomplete="off" autocapitalize="off" spellcheck="false"></div>
    <div class="field"><label for="gKey">anon public key</label><input type="text" id="gKey" placeholder="eyJ..." autocomplete="off" autocapitalize="off" spellcheck="false"></div>
    <p class="err" id="gErr" ${msg ? "" : "hidden"}>${esc(msg || "")}</p>
    <button class="btn prime big" id="gOk">Collega</button>`, g => {
    g.querySelector("#gOk").onclick = () => {
      const url = g.querySelector("#gUrl").value.trim().replace(/\/+$/, ""), key = g.querySelector("#gKey").value.trim();
      if (!/^https:\/\/.+/.test(url) || key.length < 20) { const e = g.querySelector("#gErr"); e.textContent = "Controlla i due valori: l'URL inizia con https:// e la chiave è lunga."; e.hidden = false; return; }
      try { localStorage.setItem("olw-sb", JSON.stringify({ url, key })); } catch (e) {}
      location.reload();
    };
  });
}

function chiediAccesso() {
  schermata(`${stemma}<h2>Entra nella dimora</h2>
    <p class="muted small">Ognuno entra con il suo account: così l'app ricorda il tuo eroe su ogni telefono.</p>
    <div class="field"><label for="aMail">Email</label><input type="email" id="aMail" autocomplete="email" inputmode="email" autocapitalize="off"></div>
    <div class="field"><label for="aPass">Password</label><input type="password" id="aPass" autocomplete="current-password" minlength="6"></div>
    <p class="err" id="aErr" hidden></p>
    <p class="ok small" id="aOk" hidden></p>
    <button class="btn prime big" id="aIn">Entra</button>
    <button class="btn ghost" id="aNew">Prima volta? Crea l'account</button>
    <button class="linkbtn" id="aReset">Ho dimenticato la password</button>`, g => {
    const mail = () => g.querySelector("#aMail").value.trim(), pass = () => g.querySelector("#aPass").value;
    const err = t => { const e = g.querySelector("#aErr"); e.textContent = t; e.hidden = !t; g.querySelector("#aOk").hidden = true; };
    const ok = t => { const e = g.querySelector("#aOk"); e.textContent = t; e.hidden = false; g.querySelector("#aErr").hidden = true; };
    const traduci = e => /invalid login/i.test(e.message) ? "Email o password non corrette." : /not confirmed/i.test(e.message) ? "Conferma prima l'email: apri il link che ti è arrivato." : /already registered/i.test(e.message) ? "Questa email ha già un account: usa Entra." : /password/i.test(e.message) ? "La password deve avere almeno 6 caratteri." : "Qualcosa non ha funzionato: " + e.message;
    g.querySelector("#aIn").onclick = async () => {
      if (!mail() || !pass()) return err("Scrivi email e password.");
      const { error } = await sb.auth.signInWithPassword({ email: mail(), password: pass() });
      if (error) err(traduci(error)); else location.reload();
    };
    g.querySelector("#aNew").onclick = async () => {
      if (!mail() || pass().length < 6) return err("Scrivi l'email e una password di almeno 6 caratteri.");
      const { data, error } = await sb.auth.signUp({ email: mail(), password: pass(), options: { emailRedirectTo: location.origin + location.pathname } });
      if (error) return err(traduci(error));
      if (data.session) location.reload(); else ok("Account creato. Apri la mail di conferma, tocca il link e poi torna qui a premere Entra.");
    };
    g.querySelector("#aReset").onclick = async () => {
      if (!mail()) return err("Scrivi prima la tua email.");
      const { error } = await sb.auth.resetPasswordForEmail(mail(), { redirectTo: location.origin + location.pathname });
      if (error) err(traduci(error)); else ok("Ti ho mandato una mail per scegliere una nuova password.");
    };
  });
}

function chiediNuovaPassword() {
  schermata(`${stemma}<h2>Nuova password</h2>
    <div class="field"><label for="nPass">Password nuova</label><input type="password" id="nPass" autocomplete="new-password" minlength="6"></div>
    <p class="err" id="nErr" hidden></p><button class="btn prime big" id="nOk">Salva</button>`, g => {
    g.querySelector("#nOk").onclick = async () => {
      const p = g.querySelector("#nPass").value;
      if (p.length < 6) { const e = g.querySelector("#nErr"); e.textContent = "Almeno 6 caratteri."; e.hidden = false; return; }
      const { error } = await sb.auth.updateUser({ password: p });
      if (error) { const e = g.querySelector("#nErr"); e.textContent = error.message; e.hidden = false; } else location.replace(location.pathname);
    };
  });
}

async function avvio() {
  const col = leggiCollegamento();
  if (!col) return chiediCollegamento();
  if (!(window.supabase && window.supabase.createClient)) {
    schermata(`${stemma}<h2>Nessuna connessione</h2><p class="muted small">Non riesco a raggiungere il registro della casa. Controlla la connessione e riapri l'app.</p><button class="btn prime big" onclick="location.reload()">Riprova</button>`);
    return;
  }
  sb = window.supabase.createClient(col.url, col.key, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } });
  if (/type=recovery/.test(location.hash)) {
    sb.auth.onAuthStateChange(ev => { if (ev === "PASSWORD_RECOVERY") chiediNuovaPassword(); });
    return;
  }
  const { data: { session }, error } = await sb.auth.getSession();
  if (error && /fetch|network/i.test(error.message)) return chiediCollegamento("Non riesco a contattare Supabase: controlla URL e chiave.");
  if (!session) return chiediAccesso();
  utente = session.user;
  document.body.classList.remove("pre");
  $("#view").innerHTML = `<div class="notice fr-stone"><h2>Apertura della dimora…</h2><p class="muted small">Le candele si accendono.</p></div>`;

  db = window.OLWStore.creaStore(sb);
  winStart = inizioMese(Date.now() - 65 * DAY);

  if (!me) {
    try { const u = await db.doc("utenti/" + utente.id).get(); if (u.exists && u.data().eroe) { me = u.data().eroe; localStorage.setItem("olw-hero", me); } }
    catch (e) {
      console.error(e);
      if (e && (e.code === "42501" || /permission|security/i.test(e.message || ""))) {
        $("#view").innerHTML = `<div class="notice fr-stone"><h2>Porta chiusa</h2><p class="muted small">L'account ${esc(utente.email)} non è tra i membri della casa. Aggiungi la sua email nella tabella <b>membri</b> di Supabase e riapri l'app.</p><button class="btn" id="xEsci">Esci</button></div>`;
        $("#xEsci").onclick = async () => { await sb.auth.signOut(); location.reload(); };
        return;
      }
    }
  }

  const coll = (name, key, q) => (q || db.collection(name)).onSnapshot(s => { S[key] = s.docs.map(d => ({ id: d.id, ...d.data() })); if (key in S.loaded) S.loaded[key] = true; render(); }, err => { console.error(name, err); errore(err); });
  db.doc("config/casa").onSnapshot(s => {
    S.config = s.exists ? s.data() : null; S.loaded.config = true;
    if (!s.exists) db.doc("config/casa").set({ nome: "Our little world", dimora: "castello", sfidaGiorni: 14, sfidaInizio: Date.now(), stanze: ["Bagno", "Camera", "Cucina", "Salotto", "Ingresso"] }).catch(errore);
    render();
  }, err => { console.error(err); errore(err); });
  coll("faccende", "faccende");
  db.collection("completamenti").where("ts", ">=", winStart).orderBy("ts", "desc").limit(1000).onSnapshot(s => { S.comp = s.docs.map(d => ({ id: d.id, ...d.data() })); S.loaded.comp = true; render(); }, err => console.error("completamenti", err));
  let archDone = false;
  db.collection("giocatori").onSnapshot(s => {
    S.giocatori = {}; s.docs.forEach(d => S.giocatori[d.id] = d.data()); S.loaded.giocatori = true; render();
    if (!archDone) { archDone = true; archivia(); }
  }, err => console.error(err));
  coll("premi", "premi"); coll("riscatti", "riscatti"); coll("prodotti", "prodotti"); coll("spesa", "spesa"); coll("sfidaPremi", "sfidaPremi");
  db.collection("sfide").onSnapshot(s => { S.sfide = {}; s.docs.forEach(d => S.sfide[d.id] = d.data()); render(); });

  let nascostaDa = 0;
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) { nascostaDa = Date.now(); return; }
    if (nascostaDa && Date.now() - nascostaDa > 20000) db.ricarica().then(render);
  });
}
avvio().catch(e => console.error(e));
})();
