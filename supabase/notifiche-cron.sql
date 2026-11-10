-- Our little world · programma che richiama la funzione "notifiche" ogni 5 minuti.
-- Prima di eseguirlo, sostituisci SEGRETO_QUI con lo stesso valore messo nel secret CRON_SECRET della funzione.
create extension if not exists pg_cron;
create extension if not exists pg_net;

select cron.unschedule('olw-notifiche') where exists (select 1 from cron.job where jobname = 'olw-notifiche');

select cron.schedule(
  'olw-notifiche',
  '*/5 * * * *',
  $$ select net.http_post(
       url     := 'https://rquvzcetknujcrebghyk.supabase.co/functions/v1/notifiche',
       headers := '{"Content-Type":"application/json","x-cron-secret":"SEGRETO_QUI"}'::jsonb,
       body    := '{}'::jsonb
     ) $$
);
