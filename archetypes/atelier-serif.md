# Atelier Serif
> A monumental high-contrast serif, true small caps, and hairline rules on pure white or deep black give craft and luxury work a measured, exact voice.

## When to pick

- Fashion, jewelry, watchmaking, fragrance, fine hospitality, wine, architecture studios, made-to-order craft.
- The brand trades on precision and restraint, not on the amount of information it can show.
- At least one excellent photograph of the product, the room, or the making exists.
- Skip it for dense tools and long forms. The type needs space that data-heavy screens cannot give it.

## Composition

- One statement per view: a single headline, a short paragraph, and at most one action in each section.
- Website hero: one photograph of the object or the room fills the stage, and the serif statement sits in a calm
  part of that frame, large enough to hold its own while the image stays dominant and the subject stays
  uncovered. This applies to the site opening only; see rules/layout.md.
- Work on an exact baseline grid. Headlines, small-cap labels, and body text in neighboring columns land on
  shared baselines.
- Align optically, not only by box edges: hang opening quotation marks outside the text edge, and nudge large
  round letters and italics until their visible edge meets the margin.
- Use 1 px rules to divide and frame instead of boxes. Run each rule to a column edge, never stopping short.
- Prefer asymmetric placement to centered stacks: a headline offset by one column, a caption at the far margin.
- In product UI, keep the serif for page titles, product names, and key prices. Everything operational moves to
  Archivo on a quiet grid.

## Typography

| Role | Family | Weights |
|---|---|---|
| Display, headlines, pull quotes | Bodoni Moda | 400, 500, 400 italic |
| Small-cap labels, eyebrows, navigation | Bodoni Moda SC | 400, 500 |
| Body, UI, forms, captions | Archivo | 400, 500, 600 |

- Display at 72–160 px on desktop and 44–64 px on phones; line height 0.95–1.05; tracking −1% to −2%.
- Bodoni hairlines vanish at small sizes. Keep Bodoni Moda at 24 px and above; small-cap labels stay at
  14–16 px, weight 500.
- Bodoni Moda has an optical-size axis. Leave optical sizing on so large headlines get finer hairlines and smaller
  sizes get sturdier strokes.
- Small caps come from the Bodoni Moda SC family itself. Never imitate them by shrinking capitals. Track them +5%.
- Archivo body at 15–17 px, line height 1.5. Prices, sizes, and dimensions use tabular figures.
- Load from Google Fonts: Bodoni Moda, Bodoni Moda SC, Archivo.

## Color roles

Light example on pure white. It is a starting point (CORE-13). A deep dark version swaps ground and ink, using a
ground near `#0C0C0E` and text near `#ECECEE` rather than pure black and pure white.

| Role | Example | Use |
|---|---|---|
| Ground | `#FFFFFF` | Page background |
| Surface | `#F4F4F5` | Rare: inputs, a quiet band behind specifications |
| Text primary | `#111113` | Headlines, body |
| Text secondary | `#4A4A50` | Supporting copy |
| Text muted | `#6B6B72` | Captions, credits |
| Text inverse | `#FFFFFF` | Text on ink fills |
| Accent | `#111113` | Primary action as an ink fill; selection shown by underline |
| Boundary | `#111113` structural rules, `#DADADD` quiet dividers | Input outlines use `#8A8A90` |
| Status | success `#2F6B47`, warning `#8A5A00`, error `#A32020`, info `#2B4F7A` | Always with a label or icon |

- The interface stays ink and white. Color arrives through photographs and the product itself.
- When the brand owns a color, it takes the accent role and nothing else changes.

## Shape and elevation

- Radius 0 on images, buttons, inputs, and tags; 2 px at most where a control needs a softer edge.
- No shadows anywhere. Depth comes from photography and from the size contrast between display and body type.
- Rules are 1 px. A 2 px rule may open a major section, once per page.
- Primary button: an ink rectangle with Archivo 500 text. Secondary actions are text links underlined with a
  4 px offset. One filled button per view.

## Motion
- Measured and slow: 400–600 ms opacity fades; nothing slides more than 8 px.
- Hairline rules may draw across (scaleX 0 → 1, 500 ms) once when their section enters.
- No bounce, no stagger longer than three items.
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery

- Still life and interiors with deliberate light: raking side light on texture, deep shadow, one subject.
- For craft brands, show hands and tools at work and material up close: grain, stitching, enamel, brushed metal.
- Image treatments such as toned monochrome or film grain stay inside the photograph and never extend over text
  or UI.
- Large plates with wide margins; crops tight enough that the material is legible.
- Product photography shows the real product (CORE-9). Generated images only for an imagined scene stock cannot
  supply.
- Icons only where text cannot replace them (cart, close, menu): thin stroke, 20 px.

## Avoid

- Gold gradients, foil textures, script faces, or monograms assembled from primitives.
- The same centered stack of eyebrow, headline, paragraph, and button repeated section after section.
- Bodoni for body copy or anything under 24 px other than the small-cap labels.
- Imitation small caps, browser-slanted italics, or letter-spaced lowercase.
- Shadows, rounded cards, and pill buttons.
- Two statements competing in one view.
- Tinted paper backgrounds standing in for luxury. Warmth comes from light in the photographs.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/typography.md, rules/color.md,
  and rules/review-checklist.md.

## In apps vs. on websites

- Websites: full display scale, generous vertical space, photography carrying the mood, one action per section.
- Apps (client portals, booking, store accounts): Bodoni Moda for page titles and product names only; Archivo for
  everything people read closely or operate; structure from rules and spacing.
- Checkout and forms never use the display serif inside fields or buttons. Labels are Archivo 500.
- On phones, headlines drop to 40–56 px while small-cap labels stay at 14 px or larger.
