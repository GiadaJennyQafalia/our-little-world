# Notifiche push · configurazione su Supabase (una volta sola)

1. **Edge Functions → Deploy a new function → via Editor**: nome `notifiche`, incolla il contenuto di `supabase/functions/notifiche/index.ts`, Deploy.
2. Nella pagina della funzione, **Details**: disattiva **Verify JWT** (la funzione si protegge da sola con `CRON_SECRET`).
3. **Edge Functions → Secrets**: aggiungi `VAPID_PUBLIC`, `VAPID_PRIVATE`, `CRON_SECRET` (i valori te li dà Claude; la chiave privata non va mai nel repository).
4. **SQL Editor**: incolla `supabase/notifiche-cron.sql` (con il tuo `CRON_SECRET` al posto di `SEGRETO_QUI`) ed esegui.
5. Sul telefono: Impostazioni → Notifiche → accendi e Salva.

La funzione legge e scrive solo nella tabella `docs` (collezioni `push` e `pushlog`).
