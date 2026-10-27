/* Our little world · service worker
   Tiene in cache la "scocca" dell'app così si apre subito; i dati arrivano sempre freschi da Supabase. */
const VERSIONE = "olw-v3.35.0";
const SCOCCA = ["./", "index.html", "css/style.css", "js/store.js", "js/sprite.js", "js/csv.js", "js/ampolle.js", "js/app.js", "config.js", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "img/castello.webp", "img/porta.png", "img/porta-sporco1.png", "img/porta-sporco2.png", "img/porta-sporco3.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSIONE).then(c => c.addAll(SCOCCA)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSIONE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET") return;
  if (url.hostname.endsWith("supabase.co") || url.hostname.endsWith("supabase.in")) return; // dati: sempre dalla rete
  const mia = url.origin === self.location.origin;
  if (mia) {
    // Prima la rete (così gli aggiornamenti arrivano subito), poi la cache se sei offline.
    e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(VERSIONE).then(x => x.put(e.request, c)); return r; })
      .catch(() => caches.match(e.request).then(r => r || caches.match("index.html"))));
  } else if (/fonts\.(googleapis|gstatic)\.com|cdn\.jsdelivr\.net/.test(url.hostname)) {
    // Font e libreria: dalla cache se ci sono, altrimenti scaricali e conservali.
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(res => { const c = res.clone(); caches.open(VERSIONE).then(x => x.put(e.request, c)); return res; })));
  }
});
