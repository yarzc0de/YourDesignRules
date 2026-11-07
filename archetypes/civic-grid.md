# Civic Grid
> Expressive Swiss modernism for public information: oversized grotesque type steps across visible alignments inside deep margins, in plain language.

## When to pick
- Government and municipal services, transit, public health, universities, libraries, NGOs, annual reports,
  open data portals, visitor information for museums.
- Architecture, planning, and design studios that want rigor without luxury cues.
- Content where clarity and trust matter more than warmth.
- Skip it for playful consumer brands or for products whose interface is the hero.

## Composition
- Lay a 12-column grid with deep outer margins (96–160 px on desktop, at least 20 px on phones). Readers see the
  grid through the alignments, not through drawn grid lines.
- Step type across columns: a headline starting on column 1, its standfirst on column 4, body text on
  column 7. Every block starts exactly on a column line.
- Keep one strong left axis per section, flush left and ragged right. Nothing is centered.
- Group tightly and separate generously: 8–12 px inside a group, 64–96 px between groups.
- Run a plain rail down the left 2–3 columns for section numbers, dates, labels, and in-page navigation. The
  rail is text on the ground, with no box or fill.
- Open sections with a full-width rule in the text color, 1–2 px; a heavier 4 px rule can open the page.
- Website hero: the oversized headline and one wide documentary photograph share the grid, the photo running
  from a column line to the bleed edge and the headline crossing its top edge or sitting in the band just
  above; no centered type and no framed image beside a text column.

## Typography
| Role | Family | Weights |
|---|---|---|
| Display, headings | Schibsted Grotesk | 700, 800, 900 |
| Body, UI | Public Sans | 400, 600 |
| Section numbers, data, captions | Martian Mono | 400, 500 |

- Display 72–160 px on desktop, 40–64 px on phones, line height 0.95–1.0, tracking −2% to −3%. Break lines at
  phrase boundaries.
- Body 17–18 px Public Sans, line height 1.5, 60–70 characters per line; a 5–6 column span holds that measure
  on desktop.
- Martian Mono at 11–13 px for section numbers, dates, table figures, and captions. It sets wide, so narrow its
  width axis to about 87.5 or keep the strings short.
- Load from Google Fonts: Schibsted Grotesk (700–900), Public Sans (400, 600), Martian Mono (400, 500).

## Color roles
Light palette. Chroma lives in one blue, used either for actions or as an occasional full-bleed field.

| Role | Token | Example |
|---|---|---|
| Ground | `--background` | `#FFFFFF` |
| Surface (table headers, rare insets) | `--surface` | `#F1F3F5` |
| Field (one saturated section) | `--field` | `#1F49C7` with `#FFFFFF` text, `#DCE4FA` secondary |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#0A0A0A` / `#3A3A3A` / `#5C5C5C` |
| Accent (links, primary action) | `--primary` | `#1F49C7` with `#FFFFFF` text |
| Rule / hairline / input boundary | `--rule`, `--border`, `--border-strong` | `#0A0A0A` / `#D0D4D9` / `#858B93` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#18794E`, `#A35200`, `#C5221F`, `#0B6E99` |

- Inside a field section, buttons invert to a white fill with blue text.
- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Right angles: radius 0 on images, sections, tables, and buttons. Up to 4 px only on inputs when the platform
  focus style expects it.
- No shadows. Menus and dialogs separate with a 2 px ink border; dialogs also get a scrim.
- Rules do the structural work that boxes do in other directions.

## Motion
- Movement follows the grid: elements slide along one axis (horizontal or vertical), never diagonally, 200–300 ms.
- Large type does not animate letter by letter; a section may fade in once on the website.
- Links underline with a left-to-right wipe of about 200 ms.
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery
- Documentary photography of real places, services, and people, in full color and unfiltered.
- Crop images to column spans so their edges land on grid lines.
- Captions sit outside the image, below it or in the rail, in Martian Mono or Public Sans at 13–14 px, stating
  what, where, and when.
- Pictograms from one library (Material Symbols suits public information) at 24 px, outline or filled, not
  both.
- Maps, timelines, and charts are built from real elements: bars in ink, one highlighted in the accent.

## Avoid
- A paper-tinted ground.
- Centered headlines, or a lone colored square standing in for the whole style. The direction lives in the
  grid, the scale contrast, and the alignment discipline.
- Rounded cards, drop shadows, and gradients.
- Drawn grid lines that no content aligns to.
- Captions or headlines laid over photographs.
- Stock photos of smiling teams in place of the real service.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps (service flows, portals, applications): one question per page in a single column on the grid, headings
  at 32–40 px, and the rail showing steps and progress.
- Apps: tables get a 2 px ink rule under the header and hairlines between rows; labels use plain words.
- Websites: full display scale, numbered sections in the rail, at most one saturated field section per page.
