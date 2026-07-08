# TrackMan Tracker

A simple, self-contained web app for logging and tracking golf shot numbers from a
[TrackMan](https://www.trackman.com/) (or any launch monitor).

## Features

- **Log shots** with the metrics that matter: club, club speed, ball speed,
  launch angle, spin rate, carry, and total distance.
- **Smash factor** is calculated automatically (ball speed ÷ club speed).
- **Session stats** — shot count, average carry, average ball speed, average
  smash factor, and longest carry — update live.
- **Filter** the shot table by club.
- **Export to CSV** for analysis in a spreadsheet.
- **Persistent** — everything is saved to your browser's local storage, so your
  data is still there when you come back.

No build step, no dependencies, no server.

## Usage

Open `index.html` in any modern web browser.

That's it. Log a shot with the form on the left; your shots and stats appear on
the right.

## Data & privacy

All data stays in your browser (via `localStorage`). Nothing is uploaded
anywhere. Use **Export CSV** to back up or move your data, and **Clear All** to
wipe it.
