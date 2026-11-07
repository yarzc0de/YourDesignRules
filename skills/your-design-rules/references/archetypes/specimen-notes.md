# Specimen Notes
> A subject presented like a specimen and surrounded by its evidence: callouts, rulers, measurements, and mono labels that explain what you are looking at.

## When to pick

- Science, health, research institutes, labs, biotech, field guides, museum collections, and hardware or
  materials products with measured properties.
- There are real facts to annotate: dimensions, composition, sources, study findings.
- The audience reads carefully and cares where a claim comes from.
- Skip it when there is no evidence to place around the subject. Empty callouts are just decoration.

## Composition

- The subject is large and central. Annotations sit to its sides, each joined by a leader line that ends exactly
  on the feature it describes.
- Give the evidence a reading order: number the callouts 1, 2, 3 and repeat those numbers in the text column.
- Reading text in Newsreader runs beside or below the plate at a comfortable measure; notes and sources sit in
  mono at the margin.
- Rulers, scale bars, and grids appear only when the measurement behind them was supplied (CORE-9).
- Website hero: the specimen, cut out or shot on a plain ground, fills the stage; the headline sits in the open
  space around it with two or three real callouts attached, so subject, statement, and evidence form one
  continuous stage. This applies to the site opening only; see rules/layout.md.
- In product UI, the specimen becomes a record's detail view: image or diagram in the main region, properties as
  a labeled list in a side column, sources at the bottom.

## Typography

| Role | Family | Weights |
|---|---|---|
| Headings, UI, buttons | Space Grotesk | 500, 600, 700 |
| Reading text, long captions | Newsreader | 400, 500, 400 italic |
| Labels, measurements, IDs, sources | IBM Plex Mono | 400, 500 |

- Headings at 32–64 px, line height 1.1, tracking −1%.
- Newsreader at 18–20 px on websites, line height 1.55, 60–70 characters per line. It has an optical-size axis;
  leave optical sizing on.
- Mono labels at 12–13 px. Keep value and unit together and make the unit quieter: "42" in primary text, "mm" in
  muted.
- Scientific names and titles of works in Newsreader's true italic.
- Load from Google Fonts: Space Grotesk, Newsreader, IBM Plex Mono.

## Color roles

Light example. It is a starting point (CORE-13).

| Role | Example | Use |
|---|---|---|
| Ground | `#FFFFFF` | Page background |
| Surface | `#F3F5F6` | Specimen plates, property panels |
| Text primary | `#15191C` | Headings, reading text, values |
| Text secondary | `#47515A` | Supporting copy, callout text |
| Text muted | `#66707A` | Units, sources, timestamps |
| Text inverse | `#FFFFFF` | Text on the accent |
| Accent | `#0A6F86` | Primary action, the callout currently selected |
| Annotation | `#15191C` leader lines and rulers | Minor ticks `#7A848D` (3.8:1) |
| Boundary | `#D7DCE0` hairlines | Input outlines `#7A848D` |
| Status | success `#1E7A4C`, warning `#9A6200`, error `#B42318`, info `#3557C9` | Always with a label or icon |

- Highlight one callout at a time with the accent, the one being read or hovered. The rest stay in ink.
- Color inside the specimen photo is the subject's own. Do not tint the photo to match the palette.

## Shape and elevation

- Radius none on plates, rulers, tables, and the specimen frame; 8 px on panels, inputs, and tooltips; full on
  callout markers and tags.
- Lines are 1 px. Leader lines are straight or have one elbow, never curves, and never cross each other.
- A cut-out specimen floating on the ground may cast one large soft shadow, for example
  `0 16px 48px rgba(21,25,28,0.10)`. Nothing else is lifted. Limits are in rules/color.md.

## Imagery

- Photograph the subject evenly lit on a plain ground, straight on or orthographic, so measurements make sense.
- Microscopy, x-ray, cross-sections, and field photos come from real, credited sources.
- Diagrams are built from shapes and live text. Custom anatomy or mechanism art comes from a vector asset, never
  from hand-placed primitives.
- Callouts, labels, and rulers are live elements placed over or around the image, never part of the image file
  (CORE-10).
- Icons: a thin outline set at 16–20 px, used sparingly.

## Avoid

- Decorative rulers, crosshairs, coordinates, or "Fig. 3" labels with nothing real behind them.
- Invented measurements, sample sizes, or study results.
- Labels baked into a photograph or a generated image.
- Leader lines that end near the feature instead of on it.
- Mono for paragraphs or long notes.
- More than six to eight callouts on one plate. Split the subject into views instead.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/imagery-and-icons.md,
  rules/color.md, and rules/review-checklist.md.

## In apps vs. on websites

- Websites: one specimen per section with a generous plate, and long-form reading in Newsreader.
- Apps (lab tools, collection databases, patient education): a detail view with the image and a property list.
  Mono for IDs, measurements, and timestamps; Space Grotesk for titles; Newsreader for notes and descriptions.
- Sample tables follow guides/dashboard-and-tables.md, with numbers right-aligned in mono.
- On phones, callouts become a numbered list under the image; tapping a number highlights its feature.
