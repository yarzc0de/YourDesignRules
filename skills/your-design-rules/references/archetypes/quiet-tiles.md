# Quiet Tiles
> Friendly, detailed information sorted into soft tiles on a strict grid, with each tile's size and density set by what it holds.

## When to pick
- Consumer productivity, personal finance, health and habit tracking, smart home, trip planning, learning apps.
- Overview screens where items differ in weight: one key figure, a schedule, a few short lists.
- Feature sections where each item has real content of its own (a number, a crop of the product, a short
  list) rather than a one-line benefit.
- Skip it when the content is one long read or one dense table; tiles would only chop it up.

## Composition
- Place tiles on one column grid (12 on desktop, 4 on phones) with a single gap value of 16 or 24 px. Tiles
  span 1–4 columns and 1–2 rows according to their content.
- Make one tile clearly larger than the rest: the selected item, today's plan, the current balance. It is the
  dominant region of the view (CORE-2).
- Give timelines, schedules, and step sequences wide tiles that span the full row, so they read left to right.
- Keep minor items together: five settings or three short facts form one tile with rows, not five tiles.
- Let density differ between tiles: a compact table tile can sit next to a tile that holds one large number.
- Website hero: not a tile grid. One oversized cut-out object or photograph rests on a single soft-tinted
  ground with the headline set into its open space, and the tiles begin after it.
- In product UI, keep the tile system for home and overview screens; detail screens switch to full-width lists
  and forms.

## Typography
| Role | Family | Weights |
|---|---|---|
| Display, key values, tile titles | Bricolage Grotesque | 600, 700, 800 |
| Body, UI, labels | DM Sans | 400, 500, 600 |
| Times, amounts, counters | IBM Plex Mono | 400, 500 |

- Marketing display 48–80 px at 700–800 with −2% tracking; let the optical size axis follow the font size.
- Key tile value 40–64 px in Bricolage Grotesque 700; tile titles 16–18 px at 600. Keep Bricolage at 16 px
  and above.
- Body 15–16 px DM Sans; labels 12–13 px DM Sans 500 in sentence case.
- IBM Plex Mono for times, amounts, and counters, so changing digits keep their width.
- Load from Google Fonts: Bricolage Grotesque (optical size axis, 600–800), DM Sans (400–600), IBM Plex Mono
  (400, 500).

## Color roles
Light palette on a cool gray ground, so white tiles separate without borders.

| Role | Token | Example |
|---|---|---|
| Ground | `--background` | `#F3F5F9` |
| Tile surface | `--surface` | `#FFFFFF` |
| Key tile tint | `--surface-key` | `#E9EEFC` |
| Category tint (one, optional) | `--surface-alt` | `#E7F5EE` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#14161C` / `#474D5A` / `#5E6573` |
| Accent (actions, selection) | `--primary` | `#4C3FD1` with `#FFFFFF` text |
| Boundary / strong (inputs) | `--border`, `--border-strong` | `#DCE1EA` / `#7F8796` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#177245`, `#A0560A`, `#C42B3B`, `#1C6AB0` |

- Tints mark the key tile or a category. They never mean "selected" on their own; selection adds the accent
  outline and a label or check.
- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Tiles 20 px (anywhere in 16–24, one value per product); elements inside tiles 12 px; buttons, inputs,
  chips, and segmented controls fully rounded.
- Flat by default: tiles separate from the ground by tone, and borders are rare. A tile that can be dragged
  or opened may take the small soft shadow on hover, per rules/color.md.
- Selected tile: key tint, a 2 px accent outline, and a visible label or check.
- Tile padding 20–24 px; 8–12 px between a tile's title and its content.

## Imagery
- Warm everyday photography of the people and places the product serves, cropped to fit tiles; reuse one
  scene through several crops instead of collecting unrelated thumbnails.
- Small charts inside tiles (progress bar, ring, sparkline, week strip) built from real elements and real data.
- Icons from one library (Phosphor suits the soft shapes) at 20–24 px, set directly on the tile without a
  colored circle behind each one.
- Illustrations only when they describe what the tile contains.

## Avoid
- A bento of equal tiles where several hold filler such as "Fast" or "Secure".
- Tiles for one-line facts.
- Gradient fills, glassy tiles, or heavy shadows.
- Two or more different tile radii on one screen.
- A hero arranged as a bento.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps: on phones the grid collapses to one column with the key tile first; small stat tiles may pair two per
  row.
- Apps: tapping a tile opens a full screen or a sheet, not a bigger tile in place.
- Websites: use the tile grid once per page, for the section where items truly differ in size and content;
  other sections are plain type and imagery.
