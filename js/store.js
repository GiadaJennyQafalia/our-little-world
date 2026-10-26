/* Our little world · livello dati
   Imita la piccola API "collection / doc / onSnapshot" usata dall'app, sopra una tabella Supabase `docs`.
   Ogni collezione viene caricata una volta, tenuta in memoria e aggiornata in tempo reale. */
(function () {
  "use strict";
  const ALFA = "abcdefghijklmnopqrstuvwxyz0123456789";
  const nuovoId = () => { let s = ""; for (const x of crypto.getRandomValues(new Uint8Array(20))) s += ALFA[x % 36]; return s; };
  const copia = d => (d == null ? d : JSON.parse(JSON.stringify(d)));
  const OPS = {
    "==": (a, b) => a === b, "!=": (a, b) => a !== b,
    "<": (a, b) => a < b, "<=": (a, b) => a <= b, ">": (a, b) => a > b, ">=": (a, b) => a >= b
  };

  function creaStore(sb) {
    const cache = {};          // collezione -> Map(id -> dati)
    const caricamenti = {};    // collezione -> Promise
    const ascoltatori = new Set();

    const avvisa = coll => { for (const a of ascoltatori) if (a.coll === coll) { try { a.run(); } catch (e) { console.error(e); } } };

    async function carica(coll) {
      const m = new Map(), passo = 1000;
      for (let da = 0; ; da += passo) {
        const { data, error } = await sb.from("docs").select("id,data").eq("coll", coll).range(da, da + passo - 1);
        if (error) throw error;
        data.forEach(r => m.set(r.id, r.data));
        if (data.length < passo) break;
      }
      cache[coll] = m;
      avvisa(coll);
      return m;
    }
    function assicura(coll) {
      if (!caricamenti[coll]) caricamenti[coll] = carica(coll).catch(e => { delete caricamenti[coll]; throw e; });
      return caricamenti[coll];
    }
    function locale(coll, id, dati) {
      if (!cache[coll]) return;
      if (dati === null) cache[coll].delete(id); else cache[coll].set(id, dati);
      avvisa(coll);
    }

    let canale = null;
    function collegaTempoReale() {
      if (canale) sb.removeChannel(canale);
      canale = sb.channel("olw-docs")
        .on("postgres_changes", { event: "*", schema: "public", table: "docs" }, p => {
          if (p.eventType === "DELETE") {
            const o = p.old || {};
            if (o.coll) locale(o.coll, o.id, null);
            else for (const c in cache) if (cache[c].has(o.id)) locale(c, o.id, null);
          } else if (p.new && p.new.coll) locale(p.new.coll, p.new.id, p.new.data);
        })
        .subscribe();
    }
    collegaTempoReale();

    /* Al ritorno in primo piano ricarica tutto: il telefono può aver perso aggiornamenti mentre dormiva. */
    async function ricarica() {
      collegaTempoReale();
      await Promise.all(Object.keys(cache).map(c => carica(c).catch(e => console.error(c, e))));
    }

    const istantanea = (id, d) => ({ id, exists: d != null, data: () => copia(d) });

    function Doc(coll, id) {
      return {
        id, path: coll + "/" + id,
        async get() { await assicura(coll); return istantanea(id, cache[coll].get(id)); },
        async set(dati) {
          const { error } = await sb.from("docs").upsert({ coll, id, data: dati, updated_at: new Date().toISOString() });
          if (error) throw error;
          locale(coll, id, copia(dati));
        },
        async update(patch) {
          const { data, error } = await sb.rpc("doc_merge", { p_coll: coll, p_id: id, p_patch: patch });
          if (error) throw error;
          locale(coll, id, data);
        },
        async delete() {
          const { error } = await sb.from("docs").delete().eq("coll", coll).eq("id", id);
          if (error) throw error;
          locale(coll, id, null);
        },
        onSnapshot(cb, err) {
          const a = { coll, run: () => { if (cache[coll]) cb(istantanea(id, cache[coll].get(id))); } };
          ascoltatori.add(a);
          if (cache[coll]) a.run(); else assicura(coll).catch(e => err && err(e));
          return () => ascoltatori.delete(a);
        }
      };
    }

    function Query(coll, filtri = [], ordine = null, limite = null) {
      const risultati = () => {
        let arr = [...(cache[coll] || new Map()).entries()].filter(([, d]) => filtri.every(([f, op, v]) => OPS[op](d[f], v)));
        if (ordine) {
          const [f, dir] = ordine, s = dir === "desc" ? -1 : 1;
          arr.sort((a, b) => (a[1][f] > b[1][f] ? 1 : a[1][f] < b[1][f] ? -1 : 0) * s);
        }
        if (limite) arr = arr.slice(0, limite);
        return { docs: arr.map(([id, d]) => istantanea(id, d)), size: arr.length };
      };
      return {
        where: (f, op, v) => Query(coll, [...filtri, [f, op, v]], ordine, limite),
        orderBy: (f, dir = "asc") => Query(coll, filtri, [f, dir], limite),
        limit: n => Query(coll, filtri, ordine, n),
        doc: id => Doc(coll, id || nuovoId()),
        async add(dati) { const d = Doc(coll, nuovoId()); await d.set(dati); return d; },
        async get() { await assicura(coll); return risultati(); },
        onSnapshot(cb, err) {
          const a = { coll, run: () => { if (cache[coll]) cb(risultati()); } };
          ascoltatori.add(a);
          if (cache[coll]) a.run(); else assicura(coll).catch(e => err && err(e));
          return () => ascoltatori.delete(a);
        }
      };
    }

    return {
      collection: name => Query(name),
      doc: path => { const i = path.lastIndexOf("/"); return Doc(path.slice(0, i), path.slice(i + 1)); },
      ricarica
    };
  }

  window.OLWStore = { creaStore };
})();
