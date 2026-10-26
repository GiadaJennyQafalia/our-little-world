# Our little world · come metterla online (circa 20 minuti)

Servono due account gratuiti: **Supabase** (dove vivono i dati) e **GitHub Pages** (dove vive l'app).

## 1. Supabase, il registro della casa

1. Vai su supabase.com → *Start your project* → entra con GitHub.
2. *New project*: nome `our-little-world`, regione **Central EU (Frankfurt)**, scegli una password del database e salvala.
3. Quando il progetto è pronto, apri **SQL Editor** → *New query*.
4. Incolla tutto il file `supabase/1_setup.sql`. Prima di premere *Run*, nella riga con `email.di.francesco@esempio.it` togli i due trattini iniziali e scrivi l'email vera di Francesco. Premi **Run**.
5. Nuova query: incolla `supabase/2_import_dati.sql` e premi **Run**. Così ritrovi le 44 faccende, Jenny, Franz e il detersivo nello sgabuzzino.
6. **Authentication → URL Configuration**: in *Site URL* scrivi `https://giadajennyqafalia.github.io/our-little-world/`.
7. (Facoltativo) **Authentication → Sign In / Providers → Email**: se togli *Confirm email* non serve cliccare la mail di conferma quando create gli account.
8. **Project Settings → API Keys**: copia il **Project URL** e la **Publishable key** (o *anon public* se vedi quella). Sono pubbliche per natura: senza login e senza la tua email nella tabella membri non aprono niente.

## 2. GitHub, la casa dell'app

1. Su GitHub crea un repository **pubblico** chiamato `our-little-world`, vuoto.
2. Dimmelo in chat: carico io i file. Se preferisci farlo tu, dal computer: *Add file → Upload files* e trascina il contenuto della cartella (non la cartella stessa).
3. Nel repository: **Settings → Pages → Build and deployment**: *Deploy from a branch*, branch `main`, cartella `/ (root)`, *Save*.
4. Dopo un paio di minuti l'app è su `https://giadajennyqafalia.github.io/our-little-world/`.

## 3. Sul telefono

1. Apri il link in **Chrome**.
2. La prima volta l'app chiede URL e chiave di Supabase (se non li ho già messi io in `config.js`): incollali.
3. *Prima volta? Crea l'account* con la tua email, poi *Entra*.
4. Scegli **Jenny**: da ora il telefono si ricorda di te.
5. Menu **⋮ → Installa app** (o *Aggiungi a schermata Home*). Ora ha la sua icona e si apre come un gioco, senza barra del browser.

Francesco fa lo stesso dal suo telefono con la sua email e sceglie **Franz**.

## Da sapere

- Un progetto Supabase gratuito va in pausa dopo una settimana senza nessun accesso: usandola ogni giorno non succede. Se capita, si riattiva dal pannello di Supabase.
- L'app vecchia su claude.ai resta com'è: da oggi i punti si segnano solo qui.
