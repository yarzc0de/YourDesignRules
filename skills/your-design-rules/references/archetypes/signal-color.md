# Signal Color
> Solid fields of saturated color and loud heavy type, where moving into a new field tells the reader the subject has changed.

## When to pick

- Campaigns, launches, festivals, conferences, sports, cultural programs, consumer brands that own a strong color.
- Short pages with a few distinct messages, each important enough to earn its own field.
- The brand can carry two to four saturated colors with confidence.
- Skip it for long reading, dense data, or products where color must signal status.

## Composition

- One field, one topic: the announcement, the lineup, the venue, the tickets. Switching fields means switching
  subjects, so content inside a field is never split into further bands.
- Use three to five fields per page at most. Two fields in a row never share a color.
- Website hero: the first field is the whole stage. An oversized Archivo Black headline and one cut-out figure or
  large photograph sit together on a single solid color, with the primary action in the same field, as one
  continuous stage. This applies to the site opening only; see references/rules/layout.md.
- Type is the main graphic. Headlines may run close to the edges, break with intent, and overlap an image as long
  as every word stays whole.
- Supporting text and forms inside a field share one alignment axis with generous padding and no inner cards.
- In product UI, full fields become identity moments only: onboarding, empty states, a confirmation or
  celebration screen. Working screens use the white base with one accent.

## Typography

| Role | Family | Weights |
|---|---|---|
| Display, big numbers, labels of 1–3 words | Archivo Black | 400 (single style, already black) |
| Body, UI, forms | DM Sans | 400, 500, 700 |

- Display at 72–180 px on desktop and 48–72 px on phones; line height 0.9–1.0; tracking −2% to −3%.
- Archivo Black is for headlines, dates and prices that are the point, and very short labels. Never paragraphs,
  long button labels, or form labels.
- DM Sans body at 17–18 px on websites, line height 1.5; 500 for links and labels, 700 for inline emphasis.
- When a headline is too long for the field, break it onto another line. Do not shrink it below the display range.
- Load from Google Fonts: Archivo Black, DM Sans.

## Color roles

Light example: a field set on a white base. It is a starting point (CORE-13). Each field lists the only text
color allowed on it.

| Role | Example | Text on it |
|---|---|---|
| Ground (base) | `#FFFFFF` | primary `#111111`, secondary `#444449`, muted `#666670` |
| Field: cobalt | `#1B3FE0` | `#FFFFFF` |
| Field: vermilion | `#FF4A1C` | `#111111` (white fails at 3.4:1) |
| Field: lemon | `#FFE14D` | `#111111` |
| Field: forest | `#0B5D3B` | `#FFFFFF` |
| Accent (primary action) | `#111111` fill on white, vermilion, lemon | `#FFFFFF` |
| Accent on dark fields | `#FFFFFF` fill on cobalt and forest | `#111111` |
| Boundary | `#111111` at 1–2 px on the base; the field's text color on a field | — |
| Status | success `#0A7A45`, warning `#B25E00`, error `#C8102E`, info `#1F5FA8` | on the base only, with a label or icon |

- Inside a field, secondary text uses the field's own text color at a smaller size or lighter weight. Gray text
  on a saturated field fails contrast and looks muddy.
- Forms, validation, and status messages sit on the white base, where status colors stay distinct from the
  fields.
- A field color never carries meaning on its own. A vermilion field is a topic, not an error.

## Shape and elevation

- Radius 4 px on inputs and tags, or full pills on buttons and chips. Pick one for the whole project.
- No shadows. Fields meet edge to edge on straight seams, and the change of color is the separation.
- A cut-out image may cross the seam between two fields to tie them together.
- Where a boundary is needed, draw it at 2 px in the field's text color.

## Motion
- Color fields change with a hard cut or a fast 150–200 ms wipe as the reader crosses into a new subject; no slow gradient morphs.
- Loud type does not shake, spin, or stretch; it may slide in 24 px once.
- Buttons respond with a firm pressed state (scale 0.97, 100 ms).
- Timing, easing, and reduced-motion rules: references/rules/motion.md.

## Imagery

- Cut-out photographs of people or objects placed directly on a field, scaled large and cropped by the edge.
- Duotone photos in the field color plus ink work when the treatment has a purpose. Keep it on the photo, never
  under text or controls.
- At most one image per field.
- Icons: one bold filled set at 24 px, in the field's text color.
- Lineups, speakers, sponsors, and dates are real names and real facts (CORE-9).

## Avoid

- A new color band for every paragraph or feature.
- More than five fields, or fields that differ only slightly in hue.
- Gray or muted text on a saturated field.
- Gradients between fields, or shadowed cards inside them (CORE-6).
- Archivo Black for body copy or instructions.
- Using a field color as a status signal.
- Universal rules still apply: CORE-4 to CORE-8 in references/rules/core.md, plus references/rules/color.md and
  references/rules/review-checklist.md.

## In apps vs. on websites

- Websites: full-width fields at full scale; scrolling moves from topic to topic; at most one action per field,
  with the primary action repeated in the final field.
- Apps: white base, ink text, one field color promoted to the accent. Archivo Black only for screen titles and
  hero numbers, at the same size on every screen.
- Tickets, passes, and confirmation screens may use a full field, since each is a single object with one message.
- On phones, fields stack and display sizes drop but stay heavy; long headlines break rather than shrink.
