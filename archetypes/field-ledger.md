# Field Ledger
> A light technical sheet where outlined regions share their edges, monospace notes label the details, and one large readout of a real value anchors each view.

## When to pick
- Infrastructure consoles, developer tools, CLI companions, API references, data pipelines, and hardware or
  network configuration.
- Audiences that scan for exact values and trust precision more than personality.
- Products whose most convincing asset is a real measurement: uptime, throughput, latency, capacity, cost.
- Skip it when the product is emotional or consumer-facing, or when no real number deserves to be enlarged.

## Composition
- Build each view as a sheet of outlined regions that share borders, like the cells of a spec form. Neighbors
  meet on a single 1 px line; never leave a gap between two outlined regions or stack two borders.
- Set key/value pairs across the full row: the mono key pinned to the left edge of its region, the value on
  the right edge. Two related groups (source and target, plan and actual) can face each other across one row
  so the comparison reads in a single pass.
- Give each view one large readout of a value that exists in the data (CORE-9). It is the dominant region
  (CORE-2); everything else on the sheet is smaller and quieter.
- Use mono annotations for units, IDs, timestamps, coordinates, and region labels. Each one must carry
  information; a serial number that refers to nothing is decoration.
- Keep a 12-column grid with regions spanning whole columns, 16–24 px padding inside regions, and compact
  density for data views.
- Website hero: one continuous stage built from a wide, evenly lit photograph of the real hardware or site,
  with the headline and the readout set in a ruled band directly above it or in its quiet area, never as a
  copy column beside a framed picture.
- In product UI the sheet becomes the layout: the sidebar is a ruled column, the inspector is a stack of
  key/value rows, and tables share their outer edge with the regions around them.

## Typography
| Role | Family | Weights |
|---|---|---|
| Readout, headings, UI, body | Titillium Web | 300, 400, 600, 700 |
| Labels, values, code | IBM Plex Mono | 400, 500 |

- Readout: Titillium Web 300 at 72–120 px, line height 1.0, tracking −2%. If the value updates live, set it
  in IBM Plex Mono 400 instead so the digits keep their width.
- Headings 20–32 px at 600; UI and body text 14–16 px at 400. Titillium Web ships no 500, so step from 400
  straight to 600 instead of requesting a weight the family does not have.
- Region labels: IBM Plex Mono 11–12 px, uppercase, +6% tracking, muted color. Values in tables and key/value
  rows: Plex Mono 13–14 px, right-aligned when numeric.
- Load from Google Fonts: Titillium Web (300, 400, 600, 700) and IBM Plex Mono (400, 500).

## Color roles
Light palette. Chroma appears only when a state is real; the interface itself is ink on white.

| Role | Token | Example |
|---|---|---|
| Ground | `--background` | `#FFFFFF` |
| Surface (header strips, recessed fields, selected row) | `--surface` | `#F3F5F7` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#0E141B` / `#3E4955` / `#5C6874` |
| Accent (primary action, selection rule) | `--primary` | `#0E141B` with `#FFFFFF` text |
| Signal (the one live condition) | `--signal` | `#C2410C` |
| Boundary (region lines) / strong (inputs) | `--border`, `--border-strong` | `#C5CDD5` / `#7D8995` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#1D7346`, `#8A5A00`, `#C2410C`, `#2B5797` |

- The signal color marks the single condition that needs attention now (an incident, a failing check, a
  quota breach) and doubles as the error color. Other statuses stay small and always carry a text label.
- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Radius 0 on regions, tables, panels, and the sheet; 2 px on buttons and inputs; 4 px is the ceiling (tags).
- No shadows. Menus and dialogs separate with the strong boundary color and the surface tone; dialogs also
  get a scrim.
- Selected state: surface tone plus a 2 px ink rule on the leading edge, never a lift.
- A 2 px ink rule above a section title adds weight where a region needs it.

## Imagery
- Most views need none. Diagrams (topology, pipelines, rack layouts) are built from real elements with mono
  labels (CORE-10).
- Photograph only the real thing: hardware, cabling, the physical site. Even light, plain backgrounds, a mono
  caption below the image.
- Icons: one outline library (Lucide or Phosphor) at 16 px with a 1.5 px stroke, matching the region lines.
- Charts: thin ink strokes on hairline axes; the signal color only for the series or point past a threshold.

## Avoid
- Film grain, scanlines, CRT curvature, glow, or green-on-black "hacker" styling.
- Rounded floating cards with shadows; they break the shared-edge sheet.
- A second or third saturated color used for emphasis or decoration.
- Decorative crosshairs, fake serial numbers, and barcodes that encode nothing.
- Uppercase mono for sentences; mono labels stay a few words long.
- An enlarged readout of an invented or rounded-for-effect number.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps: compact density, 36–40 px table rows, the inspector as key/value rows. The readout leads overview
  screens only; on detail screens the record's name leads instead.
- Apps: the signal color appears while the state is true and clears as soon as it resolves.
- Websites: the same sheet with more air (24–32 px region padding, section spacing per rules/layout.md), and a
  spec table or measured result as proof instead of quote cards.
- Websites: one primary action in solid ink; secondary links in mono with an underline.
