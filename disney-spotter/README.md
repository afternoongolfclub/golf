# 🏰 Wrong Park Patrol

A tongue-in-cheek scavenger-hunt scoring game for Disney World. You earn points
every time you spot a fellow guest wearing attire from a **rival** park or
franchise — Harry Potter robes, a Mario tee, a Pokémon backpack, Minions,
Jurassic Park, Sonic, and so on. The more "out of place" the fandom, the more
points it's worth.

> It only rewards **non-Disney** franchises. Star Wars, Marvel, Pixar, Avatar
> and Indiana Jones are all owned by Disney — so they don't count!

## How to play

1. Open the app and pick which park you're in.
2. (Optional) arm bonus multipliers — head-to-toe outfit, whole group, or
   spotted while stuck in a ride queue.
3. When you spot someone repping the wrong park, **tap that franchise**. You
   score its point value, boosted by any multipliers and your current combo.
4. Spot several people in quick succession to build a **combo** (+25% each
   step, resets after 90s of no spotting).
5. Climb the ranks, unlock badges, and share your score.

## Features

- **15 built-in bounties** across four rarity tiers (10 / 15 / 25 / 40 pts) plus
  the ability to **add your own custom franchises**.
- **Combos & multipliers** for extra points.
- **Ranks** from _Park Newbie_ up to _Legendary Eagle-Eye_, with a progress bar.
- **Session vs. all-time** scoring — start a "new day" to reset combos while
  keeping your lifetime total.
- **Badges/achievements** to chase.
- **Bounty breakdown** chart of your most-spotted franchises.
- **Share** your score via the native share sheet or clipboard.

## Tech

A single self-contained `index.html` — no build step, no dependencies, no
server. It's a small PWA (installable via "Add to Home Screen") and all data is
stored on your device in `localStorage`. Nothing is uploaded anywhere.

Open `index.html` in any modern browser, or visit the deployed path
`/disney-spotter/`.
