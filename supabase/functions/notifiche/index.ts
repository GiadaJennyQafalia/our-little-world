// Our little world · notifiche push
// Si avvia ogni 5 minuti (pg_cron → pg_net). Legge i dati della casa, guarda cosa va comunicato a ciascun telefono iscritto
// (collezione "push" nella tabella docs) e manda le notifiche: ognuno riceve solo le sue.
// Segreti richiesti (Edge Functions → Secrets): VAPID_PUBLIC, VAPID_PRIVATE, CRON_SECRET.
import { createClient } from "npm:@supabase/supabase-js@2";
import webpush from "npm:web-push@3.6.7";

const DAY = 86400000, HOUR = 3600000;
const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
webpush.setVapidDetails("https://giadajennyqafalia.github.io/our-little-world/", Deno.env.get("VAPID_PUBLIC")!, Deno.env.get("VAPID_PRIVATE")!);

type Doc = { id: string; data: any };
async function tutti(coll: string): Promise<Doc[]> {
  const out: Doc[] = [];
  for (let da = 0; ; da += 1000) {
    const { data, error } = await sb.from("docs").select("id,data").eq("coll", coll).range(da, da + 999);
    if (error) throw error;
    out.push(...data);
    if (data.length < 1000) break;
  }
  return out;
}
async function salva(coll: string, id: string, data: any) {
  const { error } = await sb.from("docs").upsert({ coll, id, data, updated_at: new Date().toISOString() });
  if (error) throw error;
}

/** Data e ora locali nel fuso del telefono. */
function locale(ts: number, tz: string) {
  const p: Record<string, string> = {};
  for (const x of new Intl.DateTimeFormat("en-CA", { timeZone: tz, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).formatToParts(new Date(ts))) p[x.type] = x.value;
  return { ymd: `${p.year}-${p.month}-${p.day}`, min: +p.hour * 60 + +p.minute };
}
const toMin = (hhmm: string, def: string) => { const [h, m] = (hhmm || def).split(":").map(Number); return h * 60 + (m || 0); };
const inFinestra = (min: number, ora: string, def: string) => { const o = toMin(ora, def); return min >= o && min < o + 180; };   // l'ora scelta + 3 ore di tolleranza
const inSilenzio = (min: number, s: any) => { if (!s || !s.on) return false; const da = toMin(s.da, "22:30"), a = toMin(s.a, "07:30"); return da <= a ? min >= da && min < a : min >= da || min < a; };

Deno.serve(async (req) => {
  if (req.headers.get("x-cron-secret") !== Deno.env.get("CRON_SECRET")) return new Response("no", { status: 401 });
  const now = Date.now();
  const subs = await tutti("push");
  if (!subs.length) return Response.json({ iscritti: 0 });

  const [giocatoriL, faccendeL, sfideL, cfgL, logL] = await Promise.all([tutti("giocatori"), tutti("faccende"), tutti("sfide"), tutti("config"), tutti("pushlog")]);
  const nome = (id: string) => (giocatoriL.find((g) => g.id === id)?.data?.nome) || "L'altra persona";
  const cfg = cfgL.find((c) => c.id === "casa")?.data || {};
  const log: Record<string, any> = logL.find((l) => l.id === "stato")?.data || {};
  const faccende = faccendeL.map((f) => ({ id: f.id, ...f.data }));

  // Completamenti: tutti (servono per le scadenze) solo se serve; i nuovi si cercano per data.
  let tuttiComp: any[] | null = null;
  const compTutti = async () => (tuttiComp ??= (await tutti("completamenti")).map((c) => c.data));
  const compNuovi = async (dopo: number) => {
    const { data, error } = await sb.from("docs").select("data").eq("coll", "completamenti").gt("data->>ts", String(dopo));
    if (error) throw error;
    return data.map((r: any) => r.data).filter((c: any) => !c.annullato && c.ts <= now).sort((a: any, b: any) => a.ts - b.ts);
  };

  let inviate = 0, tolte = 0;
  for (const s of subs) {
    const d = s.data, eroe: string = d.eroe, pr = d.prefs || {}, tz = d.tz || "Europe/Rome";
    if (!eroe || !d.sub || !pr.on) continue;
    const L = locale(now, tz), domani = locale(now + DAY, tz).ymd;
    const mio = (log[s.id] ||= { nuovo: true });
    const coda: { chiave: string; titolo: string; testo: string; tag: string }[] = [];
    const gia = (mio.visti ||= {});

    // --- Sfide (eventi con una chiave: si mandano una volta sola)
    const sf: typeof coda = [];
    for (const x of sfideL) {
      const f = x.data, id = x.id, mioEroe = Array.isArray(f.eroi) && f.eroi.includes(eroe);
      if (!mioEroe) continue;
      const altro = (f.eroi as string[]).find((e) => e !== eroe) || f.da;
      if (f.stato === "proposta" && f.da !== eroe && now - (f.creata || 0) < 3 * DAY) sf.push({ chiave: `sfP|${id}`, titolo: "Nuova sfida!", testo: `${nome(f.da)} ti sfida. Accetti?`, tag: "sfida-" + id });
      if (f.stato === "attiva" && f.da === eroe) sf.push({ chiave: `sfR|${id}|si`, titolo: "Sfida accettata", testo: `${nome(altro)} ha accettato la tua sfida. Che vinca il migliore!`, tag: "sfida-" + id });
      if (f.stato === "rifiutata" && f.da === eroe) sf.push({ chiave: `sfR|${id}|no`, titolo: "Sfida rifiutata", testo: `${nome(altro)} non ha accettato la sfida.`, tag: "sfida-" + id });
      if (f.stato === "attiva" && f.fine > now && f.fine - now <= DAY) sf.push({ chiave: `sfU|${id}`, titolo: "Ultimo giorno di sfida", testo: "Hai tempo fino a domani: ogni faccenda conta.", tag: "sfida-" + id });
      if ((f.stato === "attiva" && f.fine <= now) || f.stato === "conclusa") {
        const v = f.risultato?.vincitore;
        const testo = f.stato !== "conclusa" || !f.risultato ? "La sfida è finita: apri l'app per scoprire chi ha vinto e il premio."
          : !v ? "La sfida è finita in pareggio: apri l'app per il premio." : v === eroe ? "Hai vinto la sfida! Apri l'app per scoprire il tuo premio." : `${nome(v)} ha vinto la sfida: apri l'app, c'è un premio da consegnare.`;
        sf.push({ chiave: `sfE|${id}`, titolo: "La sfida è finita", testo, tag: "sfida-" + id });
      }
    }
    const tipoSf: Record<string, string> = { sfP: "proposta", sfR: "risposta", sfU: "ultimo", sfE: "esito" };
    for (const e of sf) {
      if (gia[e.chiave]) continue;
      if (mio.nuovo) { gia[e.chiave] = now; continue; }                       // primo giro di un telefono nuovo: non rimanda il passato
      if (pr.sfide?.[tipoSf[e.chiave.split("|")[0]]] !== false) coda.push(e); else gia[e.chiave] = now;
    }

    // --- Mosse dell'altra persona
    if (mio.nuovo) mio.mosse = now;
    else if (pr.mosse && !inSilenzio(L.min, pr.silenzio)) {
      const nuovi = (await compNuovi(mio.mosse || now)).filter((c: any) => !(c.giocatori || []).includes(eroe));
      if (nuovi.length) {
        const chi = nome(nuovi[nuovi.length - 1].giocatori?.[0]);
        const ultimo = nuovi[nuovi.length - 1];
        coda.push({ chiave: "mos|" + ultimo.ts, titolo: chi, testo: nuovi.length === 1 ? `ha completato: ${ultimo.nome}` : `ha completato ${nuovi.length} faccende, l'ultima: ${ultimo.nome}`, tag: "mosse" });
      }
    }

    // --- Missione del giorno
    if (pr.missione?.on && mio.mis !== L.ymd && inFinestra(L.min, pr.missione.ora, "09:00")) {
      const mg = cfg.missioneGiorno;
      if (mg && mg.giorno === L.ymd && mg.fatta) mio.mis = L.ymd;
      else {
        const f = mg && mg.giorno === L.ymd ? faccende.find((x) => x.id === mg.id) : null;
        coda.push({ chiave: "mis|" + L.ymd, titolo: "Missione del giorno", testo: f ? `${f.nome} (${f.stanza}). Ti va di compierla?` : "La missione di oggi ti aspetta: apri l'app per scoprirla.", tag: "missione" });
      }
    }

    // --- Faccende che scadono domani
    if (pr.scadenza?.on && mio.sca !== L.ymd && inFinestra(L.min, pr.scadenza.ora, "18:00")) {
      const comp = await compTutti(), ult: Record<string, number> = {};
      for (const c of comp) if (!c.annullato && (!ult[c.faccendaId] || c.ts > ult[c.faccendaId])) ult[c.faccendaId] = c.ts;
      const altroPren = (f: any) => f.prenDa && f.prenDa !== eroe && f.prenFino > now;
      const doma = faccende.filter((f) => f.attiva !== false && f.tipo === "ricorrente" && f.freq && !altroPren(f)).filter((f) => {
        const last = Math.max(f.base || 0, ult[f.id] || 0, f.ultima || 0), sc = last + f.freq * DAY + (f.rinvio || 0);
        return sc > now && locale(sc, tz).ymd === domani;
      });
      if (doma.length) {
        const n = doma.map((f) => f.nome);
        coda.push({ chiave: "sca|" + L.ymd, titolo: "In scadenza domani", testo: n.length <= 3 ? n.join(", ") : `${n.slice(0, 3).join(", ")} e altre ${n.length - 3}`, tag: "scadenza" });
      } else mio.sca = L.ymd;
    }

    // --- Invio (le ore di silenzio rimandano tutto alla mattina)
    if (!inSilenzio(L.min, pr.silenzio)) {
      for (const e of coda) {
        try {
          await webpush.sendNotification(d.sub, JSON.stringify({ title: e.titolo, body: e.testo, tag: e.tag }), { TTL: 6 * 3600, urgency: "normal" });
          inviate++;
          const k = e.chiave.split("|")[0];
          if (k === "mis") mio.mis = L.ymd; else if (k === "sca") mio.sca = L.ymd; else if (k === "mos") mio.mosse = Number(e.chiave.split("|")[1]); else gia[e.chiave] = now;
        } catch (er: any) {
          if (er?.statusCode === 404 || er?.statusCode === 410) { await sb.from("docs").delete().eq("coll", "push").eq("id", s.id); delete log[s.id]; tolte++; break; }
          console.error("invio", s.id, er?.statusCode || er);
        }
      }
    }
    if (log[s.id]) { delete mio.nuovo; for (const k of Object.keys(gia)) if (now - gia[k] > 30 * DAY) delete gia[k]; }
  }
  // telefoni spenti: ripulisce il registro
  for (const id of Object.keys(log)) if (!subs.find((s) => s.id === id)) delete log[id];
  await salva("pushlog", "stato", log);
  return Response.json({ iscritti: subs.length, inviate, tolte });
});
