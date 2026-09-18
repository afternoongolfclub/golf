# Golf Sim Tracker

A simple, self-contained web app for logging and tracking golf shot numbers from a
golf simulator or launch monitor (TrackMan, Uneekor, Foresight/GCQuad, SkyTrak,
Garmin, Rapsodo, and others).

## Features

- **Log shots** with the metrics that matter: club, shot number, club speed,
  ball speed, launch angle, spin rate, carry, and total distance. The shot
  number auto-increments so you can just keep hitting.
- **Scan from a photo** — take or upload a picture of your launch monitor screen
  and on-device OCR reads the numbers straight into the form for you to confirm
  before saving. (Needs internet the first time you scan, to load the OCR
  engine; after that the numbers still get filled locally.)
- **Keeps the photo** with each shot, stored on your device (in the browser's
  IndexedDB, downscaled to save space). Tap the 📷 in the shots table to view
  it, and **Save to phone** to drop it into your Photos/Files.
- **Smash factor** is calculated automatically (ball speed ÷ club speed).
- **Session stats** — shot count, average carry, average ball speed, average
  smash factor, and longest carry — update live.
- **Insights** — a one-tap analysis of all your shots: plain-language takeaways
  (longest club, most consistent, biggest yardage gap, driver efficiency), an
  average-carry-by-club chart with dispersion, and a per-club breakdown table
  (carry, consistency, total, ball/club speed, smash, launch, spin).
- **Filter** the shot table by club.
- **Import from CSV or Excel** — load an existing spreadsheet of shots. Columns
  are matched by header name (e.g. `Club`, `Shot #`, `Ball Speed`, `Spin Rate`,
  `Carry`, `Total`), so it works with the app's own exports and with files from
  most sim/launch-monitor software. `.csv` is read directly; `.xlsx` loads a
  reader on first use (needs internet once — otherwise Save As CSV in Excel).
- **Export to CSV** for analysis in a spreadsheet.
- **Persistent** — everything is saved to your browser's local storage, so your
  data is still there when you come back.
- **Hosel charts** (`hosel.html`) — loft and lie adjustment settings for adjustable
  drivers, fairways, mini drivers and hybrids. Pick a club, pick the loft stamped
  on your head, and the chart shows the playing loft, lie, face angle and (where
  the maker publishes it) the spin change at every hosel setting. Tap a setting to
  see it in full, and a "smallest move for…" table tells you where to go from
  where you are. Reached from the **Hosel charts →** link in the header.

No build step, no dependencies, no server.

## Usage

Open `index.html` in any modern web browser.

That's it. Log a shot with the form on the left; your shots and stats appear on
the right.

To log from a photo, tap **Take / choose photo**, point at (or select) a picture
of your launch monitor screen, and the readable numbers are filled in for you. Always
give them a quick check before hitting **Add Shot** — OCR is best-effort and can
misread on blurry or angled shots.

### Hosel charts

Open `hosel.html` (or tap **Hosel charts →** in the header). Search or filter by
brand, pick your club, then set the loft stamped on your head and your current
hosel setting. Clubs covered out of the box:

| Club | System | Settings |
| --- | --- | --- |
| Titleist GT2 driver | SureFit | 16 (A1–D4) |
| Titleist 910F fairway | SureFit Tour | 16 (A1–D4) |
| Titleist 910 D2/D3 driver | SureFit Tour | 16 (A1–D4) |
| TaylorMade BRNR Mini Driver Copper | 4° loft sleeve | 12 clicks |
| TaylorMade M1 Rescue | 3° loft sleeve | 12 clicks |
| Any TaylorMade driver/fairway, M1 onward | 4° loft sleeve | 12 clicks |

Because the hosel — not the head — decides the chart, each entry lists the other
models it covers: the Titleist charts also serve GT, TSR, TSi, TS, 917, 915 and
913, and the TaylorMade sleeve charts cover M1 through Qi10 and later. Every
chart is transcribed from the maker's own tuning manual where one is published,
and the sources are linked in the app.

Adding a club is a one-entry edit to the `MODELS` array near the top of the
script in `hosel.html`; adding a brand means adding one entry to `SYSTEMS` too.

The charts install to a phone home screen on their own, separately from the
tracker: open `hosel.html` and use **Add to Home Screen**. It gets its own icon
(a loft sleeve with the selected setting) and opens straight to the charts,
because `hosel.webmanifest` sets `hosel.html` as the start URL.

## Deploying

The site is static — every file is served as-is from the repository root, so any
static host works.

**Netlify.** `netlify.toml` is checked in with the publish directory, cache
headers and a `/hosel` shortcut, so there is nothing to configure:

- *From the Netlify UI:* **Add new site → Import an existing project → GitHub →
  afternoongolfclub/golf**. Leave the build command empty; `netlify.toml`
  supplies the rest. Every push to the production branch redeploys.
- *From a terminal:* `npx netlify-cli login` then
  `npx netlify-cli deploy --prod --dir .`

**GitHub Pages** is already wired up through `.github/workflows`, and the two
can run side by side.

## Data & privacy

All data stays in your browser (via `localStorage`). Nothing is uploaded
anywhere. Use **Export CSV** to back up or move your data, and **Clear All** to
wipe it.
