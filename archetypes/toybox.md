# Toybox
> Saturated color, inflated shapes, and sticker-like pieces arranged with intent around one clear statement and a calm path people can actually use.

## When to pick

- Family and kids' products, games, snacks and drinks, creative hobbies, community events, playful campaigns.
- The brand voice is cheerful or jokey and the audience is not in a hurry.
- There is a recurring object, character, or motif that the stickers can refer to.
- Skip it for finance, health, legal, and anything where trust depends on restraint.

## Composition

- Planned disorder: decorative pieces cluster around the statement and the interaction islands, tilted 2–6
  degrees and overlapping edges, while the reading path between them stays straight.
- Interaction islands are the nav, the primary action, forms, and pricing. They stay upright, aligned, and free of
  stickers.
- One headline per section. Each sticker refers to the content beside it: a stamp, a ticket, the product, the
  mascot.
- Website hero: a saturated stage field holds the oversized Unbounded headline, one inflated or cut-out object,
  and a few stickers composed around them as one continuous stage, with the primary action upright next to the
  headline. This applies to the site opening only; see rules/layout.md.
- Decoration budget: three to six pieces per section, all instances of a few reusable components (CORE-17).
- In product UI, play moves to empty states, rewards, onboarding, and icons. Lists, forms, and settings stay
  standard and calm.

## Typography

| Role | Family | Weights |
|---|---|---|
| Display, big numbers | Unbounded | 600, 700, 800 |
| Body, UI, buttons | Outfit | 400, 500, 600 |

- Display at 64–140 px on desktop and 40–56 px on phones; line height 0.95–1.05; tracking −2%.
- Unbounded is wide. Keep display lines to two to four words and break them by meaning.
- Outfit body at 17–18 px on websites and 16 px in apps. Buttons in Outfit 600 at 16 px.
- Shaped, outlined, or reflective display lettering needs the same words as live text nearby or as its accessible
  name.
- Load from Google Fonts: Unbounded, Outfit.

## Color roles

Light example with a saturated stage. It is a starting point (CORE-13).

| Role | Example | Use |
|---|---|---|
| Ground | `#FFFFFF` | Page background, reading sections |
| Stage field | `#FFD23F` | Hero and feature fields; text on it `#17142A` |
| Surface | `#F1F3F8` | Panels, inputs, pricing |
| Text primary | `#17142A` | Headlines, body |
| Text secondary | `#4A4760` | Supporting copy |
| Text muted | `#66637A` | Captions, metadata |
| Text inverse | `#FFFFFF` | Text on the accent |
| Accent | `#2F5BFF` | Primary action, selection; 3.6:1 against the stage |
| Sticker colors | tomato `#FF4F2E`, pink `#FF8AD0`, lime `#C4F03A`, sky `#47B8FF` | Decoration only; text on them `#17142A` |
| Boundary | `#D9DCE6` hairlines | Input outlines `#8A8F98`; sticker outlines `#17142A` |
| Status | success `#18794A`, warning `#9C5C00`, error `#C81E4A`, info `#0E6FA8` | Always with a label or icon |

- Each section draws on two or three of these colors, not all of them.
- Sticker colors never appear on buttons, links, or selection, so the accent stays the only thing that looks
  pressable.

## Shape and elevation

- Radius 0 for stickers cut as stamps or tickets, 12–24 px for panels and inflated shapes, full for buttons,
  chips, and tags.
- Lifted pieces get a medium soft shadow, for example `0 8px 24px rgba(23,20,42,0.12)`. Nothing else is lifted.
  Limits are in rules/color.md.
- The inflated look comes from generous radius and a gentle highlight gradient from one light direction (top
  left), not from heavy shadows.
- Stickers carry a 2 px ink outline or a white die-cut border, chosen once for the whole set.

## Imagery

- Cut-out product photos and people with real expressions; 3D renders of inflated objects with consistent light.
- Mascots and stickers come from a vector asset or generator, are made once as components, and are never drawn
  from raw primitives.
- Icons: one rounded set, filled or duotone, at 24 px.
- Decorative art never stands in for content; every piece points at something on the page.

## Avoid

- Decoration covering text, the primary action, or form fields.
- Tilted buttons, tilted inputs, tilted body text.
- Random confetti or scattered shapes with no reference to the content.
- Unbounded for paragraphs, form labels, or instructions.
- Every color on every element. Restraint per section keeps the play legible.
- Chrome or reflective lettering with no readable equivalent.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/imagery-and-icons.md,
  rules/color.md, and rules/review-checklist.md.

## In apps vs. on websites

- Websites: a stage field in the hero, stickers around statements, calm sections for pricing, forms, and the
  final action.
- Apps: a white ground and standard components; Unbounded only for screen titles and celebration moments;
  stickers in empty states, achievements, and onboarding.
- Games and kids' apps may push play further, but navigation, purchases, and settings keep the same calm
  treatment.
- On phones, cut the decoration to one or two pieces per screen and keep them away from the thumb zone.
