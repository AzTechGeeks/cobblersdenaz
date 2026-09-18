# Cobbler's Den — website redesign

Mobile-first redesign of [cobblersdenaz.com](https://cobblersdenaz.com) for Cobbler's Den Shoe & Luggage Repair, Paradise Valley, Phoenix. Built by AZ Tech Geeks.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The site. One self-contained file — every photo, badge and logo is embedded, so it can be dropped on any static host as-is. |
| `pitch/` | The one-page AZ Tech Geeks pitch deck for this redesign (`pitch/index.html` plus its two image assets). |
| `src/template.html` | The editable source of the site. Image slots are `{{TOKENS}}`. Edit copy and layout here, not in `index.html`. |
| `src/images/photos/` | Photography, already cropped and compressed. `story.jpg` is a frame from the shop's own commercial. |
| `src/images/client/` | Client-owned assets carried over from the old site: the three "Best of Scottsdale" award badges and four retail brand logos. |
| `src/build.py` | Inlines the images into the template and writes `index.html`. |

## Rebuilding after an edit

```
python src/build.py
```

Requires Python 3 only (standard library). Commit both `src/template.html` and the regenerated `index.html`.

## Deploying

Copy `index.html` to the web root of the host for cobblersdenaz.com. Nothing else is required — no CMS, no build step on the server, no external requests except Google Fonts (Barlow / Barlow Condensed).

## Content notes

- Hours: Mon–Fri 8:30–5, Sat 9–3, Sun closed. The "Open now" indicator runs on `America/Phoenix` (no DST).
- Phone 602-953-1266 · 12871 N. Tatum Blvd, Phoenix, AZ 85032, across from Paradise Valley Mall.
- There is deliberately no contact form — every "free estimate" button is a `tel:` link to the shop.
- Stock photography is from Unsplash (license permits commercial use without attribution). Replace with the shop's own photos when available; the hero and the six category tiles are the first candidates.
