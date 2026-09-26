# Hosel Charts

Loft and lie adjustment charts for adjustable drivers, fairways, mini drivers and
hybrids, as a single self-contained web page. Pick your club, pick the loft
stamped on the head, and every hosel setting shows the playing loft, the lie, the
face angle and — where the maker publishes it — the spin change.

No build step, no dependencies, no server, nothing uploaded anywhere.

## Features

- **Club picker** with search and brand filtering.
- **Three chart views** — a 4×4 grid for Titleist SureFit, a clickable 12-click
  dial for TaylorMade sleeves, tappable cards for PING and Callaway, and a full
  table for any of them.
- **Loft & lie finder** wherever the settings form a complete grid: pick the loft
  you want across the top and the lie down the side, and the cell is the setting
  to dial in.
- **Playing numbers, not just deltas** — set the loft stamped on your head and
  the chart shows what you are actually playing at every setting.
- **"Smallest move for…"** — from your current setting, the nearest setting for
  more loft, less loft, more upright or flatter, in clicks where clicks apply.
- **Remembers** your club, loft and setting between visits, on your device.

## Clubs covered

| Club | System | Settings |
| --- | --- | --- |
| Titleist GT2 driver | SureFit | 16 (A1–D4) |
| Titleist 910F fairway | SureFit Tour | 16 (A1–D4) |
| Titleist 910 D2/D3 driver | SureFit Tour | 16 (A1–D4) |
| TaylorMade BRNR Mini Driver Copper | 4° loft sleeve | 12 clicks |
| TaylorMade M1 Rescue | 3° loft sleeve | 12 clicks |
| Any TaylorMade driver/fairway, M1 onward | 4° loft sleeve | 12 clicks |
| PING G430 Max driver | Trajectory Tuning 2.0 | 8 |
| Any PING G410/G425/G430 driver or fairway | Trajectory Tuning 2.0 | 8 |
| Callaway Paradym / Ai Smoke driver | OptiFit | 8 (4 loft × 2 lie) |
| Any Callaway OptiFit driver or fairway | OptiFit | 8 (4 loft × 2 lie) |

Because the hosel — not the head — decides the chart, each entry lists the other
models it covers: the Titleist charts also serve GT, TSR, TSi, TS, 917, 915 and
913; the TaylorMade sleeve charts cover M1 through Qi10 and later; the PING chart
covers every G410, G425 and G430; and the Callaway chart covers every OptiFit
driver and fairway from the Rogue on.

Every chart is transcribed from the maker's own tuning manual, settings chart or
fitting instructions, and the sources are linked in the app. Where a maker
publishes lie as a word rather than a number — PING's *Flat*, Callaway's *Draw* —
the app says so and marks the degrees as an estimate (`≈`) instead of inventing
precision.

## Usage

Open `index.html` in any modern browser, or visit the deployed site. On a phone,
use **Add to Home Screen** — the manifest and icons are set up so it launches
like an app.

Adding a club is a one-entry edit to the `MODELS` array near the top of the
script in `index.html`; adding a brand means adding one entry to `SYSTEMS` too.

## Deploying

The site is static — every file is served as-is from the repository root.

**GitHub Pages** is wired up in `.github/workflows/deploy-pages.yml`: every push
to `main` publishes the repository root.

**Netlify.** `netlify.toml` is checked in with the publish directory, cache
headers and redirects, so there is nothing to configure — import the repository
and leave the build command empty.

## Related

The shot tracker that this page started out inside now lives in its own app:
[afternoongolfclub/golfsimtracker](https://github.com/afternoongolfclub/golfsimtracker).
