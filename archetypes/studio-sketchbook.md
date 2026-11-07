# Studio Sketchbook
> Loose hand-drawn illustration and figures at human scale gather around a real task, so the product feels warm while its ground stays white or cool.

## When to pick
- Education and courses, onboarding flows, creative communities, small studios, nonprofits, family products,
  journaling, cooking, gardening.
- Consumer apps that want a human voice and friendliness without looking childish.
- Products where it is easy to picture a person doing the task.
- Skip it for dense data tools or for audiences who expect a formal tone.

## Composition
- Put an organized content surface at the center (a lesson, a form, a list, an editor) and arrange drawn
  figures around it: leaning on its edge, reaching into a corner, pointing at what they relate to. Figures
  never cover working text or controls.
- Scale figures to people, not to icons: a figure roughly as tall as the panel it stands beside.
- Every figure refers to the content next to it, such as a person holding the object the section explains,
  never a generic waving character.
- Short notes of two to five words may point at real elements with a drawn arrow. They label; they never
  instruct, and they never carry a value.
- Keep the content surface on a strict axis even where the drawings break the grid.
- Website hero: an illustrated scene holds the headline inside it, figures and type sharing one ground, so
  the statement reads as part of the drawing rather than a caption beside it.
- In product UI, illustrations move to onboarding, empty states, and completion moments; working screens
  stay plain.

## Typography
| Role | Family | Weights |
|---|---|---|
| Display, headings, notes | Fraunces | 400, 600, 700; italic 400 |
| Body, UI, labels, values | Karla | 400, 500, 700 |

- Display 48–88 px in Fraunces 600, with the SOFT axis raised to 50–100 for rounded terminals and the optical
  size axis following the font size. Headings 24–36 px at 600.
- Body 16–18 px Karla 400, line height 1.55; UI labels Karla 500 at 14 px.
- Notes: Fraunces italic at 18–22 px with the WONK axis on, in ink or the accent. This is the handwritten
  voice; add a script family only when the user supplies one (CORE-13).
- Instructions, values, labels, and buttons always stay in Karla.
- Load from Google Fonts: Fraunces (ital, opsz, wght, SOFT, and WONK axes) and Karla (400–700).

## Color roles
Light palette. Warmth comes from the coral accent, the drawn line, and the soft serif; the ground stays
white or cool.

| Role | Token | Example |
|---|---|---|
| Ground | `--background` | `#FFFFFF` |
| Surface (content panel, bands) | `--surface` | `#F1F5FA` |
| Alternate band | `--surface-alt` | `#EAF4EF` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#1E1B2E` / `#4A4659` / `#615D72` |
| Accent (actions, selection, notes) | `--primary` | `#C2412D` with `#FFFFFF` text |
| Boundary / strong (inputs) | `--border`, `--border-strong` | `#DADDE5` / `#8C8A9B` |
| Illustration inks (drawings only) | `--ink-*` | line `#1E1B2E`, coral `#E8664A`, sunflower `#F2B630`, sky `#7DB8E8` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#237A4B`, `#9C5B00`, `#A1124B`, `#2662A8` |

- Error is darker and cooler than the coral accent and always carries an icon and text, so the two never
  read as one signal. Illustration inks never color text.
- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Radius 12 px on buttons, inputs, and chips; 20–24 px on the content surface and large panels.
- The content surface may take one large soft shadow so it sits in front of the illustrated ground. Nothing
  else is lifted.
- Drawn figures have no frame or radius; they overlap the panel edge where the scene calls for it.

## Motion
- Illustrations may draw in once (stroke reveal, 400–600 ms; see MOTION-11) when they enter the viewport; they never loop.
- Controls use the default timings; the warmth stays in the art, not in wobbling buttons.
- Under reduced motion, illustrations appear complete.
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery
- One illustration style for the whole product: loose ink line with a visible hand wobble, flat fills from
  the illustration inks, plenty of white. Commission it or generate it once, make each figure a reusable
  component, and recombine the same cast for new scenes (rules/imagery-and-icons.md).
- Never assemble figures by hand from raw vector shapes.
- Photos are optional: hands, materials, and real workspaces in natural light. Keep photos and drawings in
  separate sections.
- Icons: one rounded outline library (Phosphor Regular works) at 20–24 px.

## Avoid
- Paper or kraft textures, coffee-ring overlays, and torn-edge dividers.
- Doodles that float as filler: stars, squiggles, arrows pointing at nothing.
- Lettering or script type for instructions, prices, dates, or form labels.
- A new drawing style in each section.
- Flat corporate figures with oversized limbs and no tie to the content.
- Illustrations placed over body text or controls.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps: one figure per empty state or onboarding step; forms, settings, and lists stay free of illustration.
- Apps: notes never appear inside forms or tables.
- Websites: an illustrated hero scene, then the same cast at smaller scale beside the sections it relates to.
- Websites: alternate drawn sections with plain ones so the drawings keep their effect.
