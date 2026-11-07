# Gallery Wall
> Serif statements and photographs mounted like plates on white or cool mats, arranged with the stillness of a gallery.

## When to pick
- Photographers, architects, interior designers, galleries and museums, hotels and restaurants with strong
  photography, fashion lookbooks, portfolios, premium property listings.
- Content where real photographs exist and deserve space.
- Brands whose tone is calm, considered, and unhurried.
- Skip it when there are no strong photos, or when the product is a dense working tool.

## Composition
- Give each view one dominant photograph, mounted on the mat with deep space around it (64–128 px gutters),
  instead of tucking it into a grid.
- Hang secondary photos as smaller plates along a shared line, a common top edge or a common center line,
  with one aspect ratio per row.
- Place captions outside the image as evidence: title, place, year, credit, material, or price, taken from
  supplied facts. A fine rule may separate caption from plate.
- Set one serif statement per wall, large and with room, offset from the photo's center line so the pair
  reads as asymmetric.
- Mark hanging lines and section starts with fine 1 px rules in the boundary color instead of boxes.
- Website hero: one photograph fills the stage edge to edge, or sits on a wide mat, with the serif statement
  in its quiet area or in a band of mat directly above; never a text column next to a framed picture.
- In product UI (bookings, collections, a CMS), plates become a regular grid of one ratio, and detail views
  pair a large plate with a caption block and a quiet list of facts.

## Typography
| Role | Family | Weights |
|---|---|---|
| Statements, page and object titles | Cormorant Infant | 300, 400, 500; italic 400 |
| Body, UI, captions | Karla | 400, 500 |

- Statements 48–96 px in Cormorant Infant 400, or 300 above 72 px; line height 1.05–1.15, tracking −1%.
- Its small x-height makes it weak at small sizes: keep Cormorant Infant at 24 px and above, with object
  titles at 24–32 px.
- Body 16–17 px Karla 400. Captions 13 px Karla, the object title in 500 and the rest in 400. Plate numbers
  11–12 px uppercase with +8% tracking.
- Load from Google Fonts: Cormorant Infant (300–500, italic 400) and Karla (400, 500).

## Color roles
Light palette. Color comes from the photographs; the interface keeps to neutral mats and one deep slate.

| Role | Token | Example |
|---|---|---|
| Mat (ground) | `--background` | `#FFFFFF` |
| Cool mat (alternate rooms, lightbox) | `--surface` | `#EEF1F4` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#141619` / `#4A4F56` / `#62686F` |
| Accent (primary action, links) | `--primary` | `#1F3A4D` with `#FFFFFF` text |
| Rule / input boundary | `--border`, `--border-strong` | `#D5D9DE` / `#80868E` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#2A7148`, `#8F5A00`, `#A7282F`, `#2C5D8A` |

- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Photographs and plates: radius 0. Buttons and inputs: 2–4 px.
- No shadows under photographs and no frame effects; a plate is a flat image on a flat mat.
- Lightbox controls, menus, and booking dialogs may use the medium soft elevation from rules/color.md and
  nothing stronger.

## Imagery
- Real photographs from the client: the work, the rooms, the objects. Keep light consistent across a set, and
  grade color only when it serves the whole set.
- Crop with care and keep subjects whole; recompose crops for phones rather than shrinking them.
- Stock photography never stands in for the client's own work.
- Icons are rare and thin: one outline library at 16–20 px with a 1.25–1.5 px stroke.
- The lightbox opens on the cool mat, not a black overlay, unless the photographs themselves are dark.

## Avoid
- Drop shadows under photos, faux frames, instant-print borders, and rotated plates.
- Captions laid over images, and any text on photos outside the hero's quiet area.
- Tight gutters that crowd plates into a contact sheet.
- Autoplaying carousels.
- Cormorant Infant in buttons, form labels, or body text.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps: one plate ratio across lists; the serif only for page and object titles; every control, filter, and
  data value in Karla.
- Apps: details open in a side panel that keeps the plate in view.
- Websites: one plate per scroll stop on long pages and an unhurried pace. Gutters tighten from 64–128 px on
  desktop to 24–32 px on phones, and captions stay below their plates.
