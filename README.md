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

No build step, no dependencies, no server.

## Also in this repo

- **[Wrong Park Patrol](disney-spotter/)** (`disney-spotter/`) — a lighthearted
  scavenger-hunt game for Disney World: score points for spotting fellow guests
  wearing rival-park attire (Harry Potter, Mario, Pokémon, Minions, and more).

## Usage

Open `index.html` in any modern web browser.

That's it. Log a shot with the form on the left; your shots and stats appear on
the right.

To log from a photo, tap **Take / choose photo**, point at (or select) a picture
of your launch monitor screen, and the readable numbers are filled in for you. Always
give them a quick check before hitting **Add Shot** — OCR is best-effort and can
misread on blurry or angled shots.

## Data & privacy

All data stays in your browser (via `localStorage`). Nothing is uploaded
anywhere. Use **Export CSV** to back up or move your data, and **Clear All** to
wipe it.
