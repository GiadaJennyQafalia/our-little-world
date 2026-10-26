# Our little world

A cozy dark‑fantasy game that turns household chores into quests for two players.
Installable as a PWA on Android, with real‑time sync between phones.

> Personal project by Giada Jenny Qafalia. Built for daily use at home and as a portfolio piece.

## What it does

- **Quests instead of a cleaning schedule.** Every chore has a duration, effort and an "annoyance" rating; points, category (quick, annoying, long) and due date are derived from them.
- **Daily mission.** Each day the app picks one quest (overdue first, then the ones due soon) worth a +20% bonus. It can be rerolled once.
- **The house reacts.** Each room is *Splendente → In ordine → Trascurata → Abbandonata* depending on how many points are overdue; cobwebs and dust appear on the dwelling.
- **Heroes, XP and coins.** Two separate currencies: XP drives levels and unlocks, coins are spent on personal rewards.
- **Challenge mode.** Two‑week or one‑month duels; the loser gives the winner a gift from an agreed list.
- **Supply closet.** Cleaning products with stock levels; running‑out items go straight to the shopping list.

## Tech stack

| Layer | Choice | Why |
|---|---|---|
| Front end | Vanilla HTML/CSS/JS, no build step | Opens instantly on a phone, easy to host anywhere |
| Data | Supabase (Postgres + Realtime) | One `docs` table with JSONB documents; row‑level security limits access to household members |
| Auth | Supabase email + password | One account per player, so each phone remembers its hero |
| Offline shell | Service worker + Web App Manifest | Installable, app shell cached; data always fresh |
| Graphics | Hand‑made pixel art (inline SVG, 9‑slice frames) | No external assets or licences needed |

`js/store.js` exposes a tiny Firestore‑style API (`collection().where().onSnapshot()`, `doc().update()`) on top of Supabase, so the game logic stays independent of the backend.

## Run your own

1. Create a free Supabase project.
2. In the SQL editor run `supabase/1_setup.sql` (add your players' emails to `membri`).
3. Put your Project URL and publishable/anon key in `config.js`, or leave it empty and paste them on first launch.
4. Serve the folder over HTTPS (GitHub Pages works) and open it in Chrome → *Install app*.

## Project structure

```
index.html            app shell
css/style.css         pixel frames + theme
js/store.js           Supabase data layer with live updates
js/app.js             game rules and screens
sw.js                 service worker
supabase/             database setup and data import
```
