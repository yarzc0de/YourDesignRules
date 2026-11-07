# Ambient Glow
> Dense, heavy grotesque type on a deep field, with colored light falling in from the edges and every reading area kept solid.

## When to pick

- AI products, creative tools, music and audio, crypto, night events, launches that want atmosphere.
- The brand is comfortable on a dark ground with a small number of strong statements.
- There is a believable light idea to borrow: a stage, a window at dusk, a screen glowing in a dark room.
- Skip it for daytime work tools with dense data. A dark, lit field tires the eyes over long sessions.

## Composition

- Treat the light as part of a scene. Place it at one or two edges, as if from a source just out of frame, and let
  it fade smoothly before it reaches the content.
- Reading regions (text blocks, forms, tables, product UI) sit on opaque surfaces or on plain ground where no
  light falls.
- Large, tightly set headlines carry the page. Hierarchy comes from the weight range of one family.
- Website hero: the deep field and its edge light form the stage, the oversized headline sits in the calmest dark
  area, and any product image receives the light instead of floating in front of it, so it reads as one
  continuous stage. This applies to the site opening only; see rules/layout.md.
- Not every section is lit. Alternate lit and unlit sections, and move the light source at most once per section.
- In product UI, the light stays out of the working area. At most a faint edge light on sign-in or an empty state.

## Typography

| Role | Family | Weights |
|---|---|---|
| Display | Darker Grotesque | 800, 900 |
| Headings, labels, buttons | Darker Grotesque | 600, 700 |
| Body, UI text | Darker Grotesque | 400, 500 |

- Darker Grotesque sets small for its size. Use 18–20 px for body so it reads like 16 px in other faces; line
  height 1.45.
- Display at 88–160 px on desktop and 56–72 px on phones; line height 0.9–0.95; tracking −2%.
- Weight carries hierarchy: a 900 headline over 400 body. Use no more than three weights on one screen.
- Avoid weights below 400 under 24 px; thin strokes break up on a dark ground.
- For columns of numbers, right-align and confirm the digits render at equal widths before relying on them.
- Load from Google Fonts: Darker Grotesque.

## Color roles

Dark example. It is a starting point (CORE-13).

| Role | Example | Use |
|---|---|---|
| Ground | `#0A0B10` | The deep field |
| Surface | `#13151C` | Opaque reading panels |
| Surface raised | `#1B1E27` | Menus, dialogs, popovers |
| Text primary | `#E6E8EE` | Headlines, body |
| Text secondary | `#A6ABB8` | Supporting copy |
| Text muted | `#868C9C` | Captions, metadata |
| Text inverse | `#05211E` | Text on the accent |
| Accent | `#45E0CE` | Primary action, selection, focus ring |
| Light 1, Light 2 | `#E8532E` ember, `#B8264F` rose | Edge light only, never on UI |
| Boundary | `#2A2E3A` | Hairlines; input outlines use `#5A6070` |
| Status | success `#5FC977`, warning `#F2C14E`, error `#FF6470`, info `#6FA8FF` | Always with a label or icon |

- The warm light is atmosphere; the cool accent is the one thing people press. Keeping the two hues apart stops
  the action from being mistaken for decoration.
- Raised surfaces step lighter in tone. Edge light from the field never stands in for elevation.

## Shape and elevation

- Square sections and media; 4–6 px radius on buttons, inputs, and panels.
- No shadows on cards or panels. Elevation comes from the lighter opaque surface steps above.
- Light is a large radial gradient placed on the field, for example
  `radial-gradient(60% 50% at 100% 0%, rgb(232 83 46 / 0.35), transparent 70%)`, never a box-shadow around a
  component.
- Animated gradients or shaders move slowly, pause under reduced-motion settings, and fall back to a static
  gradient with the same light. Limits are in rules/color.md.

## Motion
- The edge light may shift slowly (20–40 s cycle) only if a pause control exists and reduced motion turns it off; reading areas never move.
- Content enters with plain fades of 300–400 ms; no glow pulses on buttons.
- Provide a static image fallback for any shader or animated gradient.
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery

- Photographs lit by colored light: night interiors, stages, studios. The light in the photo matches the edge
  colors.
- Product UI is built as real elements (CORE-10) and lit from the same side as the field.
- Abstract light comes from CSS gradients or a shader, not from an image file.
- Icons: one outline set at 20 px in the secondary text color; accent only on the selected item.

## Avoid

- Haze, grain, or glow over controls, text, charts, or tables.
- Light with no direction: centered blobs, random orbs, a glow behind every card.
- The default purple-to-blue gradient.
- A pure black ground with pure white text.
- Glow as the only signal for focus, hover, or selection.
- A shader or animation with no static fallback.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites

- Websites: full atmosphere in the hero and in one or two lit sections; reading sections stay on plain ground.
- Apps: dark, fully opaque UI. Edge light only on sign-in, onboarding, and empty states.
- Data views (tables, charts, logs) sit on the surface color with no light behind them at all.
- Motion: one ambient animation per page at most.
