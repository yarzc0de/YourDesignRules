# Monochrome Stage
> Black and white, cinematic, and very smooth: one monumental fine-art image, large soft geometric type, and a scroll that glides from scene to scene.

## When to pick
- Launch pages for developer tools, AI products, open-source projects, and premium software where the story
  matters more than a feature grid.
- Products whose user asked for black and white, or for one dramatic full-bleed fine-art image to carry the
  page. "Smooth" is never a trigger — every archetype is smooth — and "premium" or "cinematic" point here only
  when the subject genuinely suits a dark black-and-white story.
- Portfolios and studios that want calm confidence rather than decoration.
- Skip it for dense product UI with many statuses (use Calm Utility) and for brands that live on one strong
  color (use Signal Color).

## Composition
- Open on one full-height stage: a black and white key visual edge to edge, the headline set in the image's
  dark sky or negative space, the install or sign-up action directly below it (LAY-20 to LAY-22 in
  references/rules/layout.md).
- Alternate full-bleed image scenes with plain black sections of type. Never put two image scenes next to each
  other.
- Give each section one idea and plenty of height. Pinned scroll scenes carry the story: a statement whose
  words light up, a before/after wipe, a horizontal track of short statements (MOTION-19 in references/rules/motion.md).
- Separate content with space, not lines or cards. The few framed elements (a product screenshot, an install
  panel) get large radii and a hairline ring, nothing else.
- Keep the layout left-aligned on a wide gutter (5vw, 20–72 px) with a 1320 px maximum width.
- In product UI the same identity becomes a black or near-black interface with white type and gray hierarchy;
  the imagery moves to empty states and onboarding.

## Typography
| Role | Family | Weights |
|---|---|---|
| Display and headings | Plus Jakarta Sans | 700, 800 |
| Body and UI | Plus Jakarta Sans | 400, 500, 600 |
| Commands and code only | Geist Mono | 400, 500 |

- Hero headline 7–8vw on desktop (roughly 96–135 px), line height 0.92–0.95, tracking −0.05em. Section
  headings 40–76 px at 700 with −0.045em.
- Body 17 px, line height 1.6, in 80% white. Small print 14–15 px in 55% white.
- Use mono only for things people copy and paste. No mono labels, no uppercase eyebrows.
- Load from Google Fonts: Plus Jakarta Sans (400, 500, 600, 700, 800) and Geist Mono (400, 500).

## Color roles
Monochrome. This palette is a starting point (CORE-13); keep it free of hue unless the user asks for one.

| Role | Token | Example |
|---|---|---|
| Ground | `--black` | `#000000` |
| Raised panel (screenshots, install panel) | `--surface` | `#0C0C0C`, or black at 55–60% over an image |
| Display text, icons, primary button | `--white` | `#FFFFFF` |
| Body text | `--text-2` | `#C9C9C9` |
| Secondary text | `--text-3` | `#8F8F8F` |
| Hairlines and rings | `--line` | `rgb(255 255 255 / 0.14)` |

- The primary action is a white pill with black text; secondary actions are white text links or translucent
  pills. There is no accent color.
- Over photographs, make room for text with a soft left or top gradient into black, never a box (COLOR-12 in
  references/rules/color.md). Body text stays off pure white (COLOR-18).

## Shape and elevation
- Pills (fully rounded) for buttons, command lines, and tabs. Framed media 18–20 px radius. Everything else is
  unframed.
- No drop shadows on ordinary elements. Framed screenshots may sit on one deep, very soft shadow
  (`0 30px 80px rgb(0 0 0 / 0.6)`) with a 1 px ring at 14% white.
- Translucent panels over images use a 10–16 px blur, kept small (MOTION-29).

## Motion
- Smooth scrolling through one loop (MOTION-28): inertia on the wheel, native touch, nothing hijacked.
- Load sequence (MOTION-25): the key visual fades in while settling from 1.06 to 1.0 scale over about 1.4 s; the
  headline lines rise from behind masks, 110 ms apart; then the lead text, the action, and the navigation.
- The hero image drifts at about 0.28× scroll speed and the hero copy fades as the stage leaves. No zoom on
  scroll.
- Two or three pinned scenes per page, such as words lighting up, a before/after wipe, or a horizontal track.
  Other sections simply arrive, with at most a soft 28 px rise.
- Tabs use a sliding white indicator; copy buttons morph into a check and show a small toast.

## Imagery
- Black and white fine-art photography or photoreal renders with a deep tonal range: velvety blacks, luminous
  whites, soft mist. Think long exposures, monumental simple forms (rings, monoliths, spheres), a tiny human
  figure for scale, and plenty of empty sky.
- Generate three or four candidates and keep the strongest (IMG-22). Prompt for "black and white fine-art
  photograph", the subject, the light, and where the empty space for the headline sits.
- Real product screenshots appear in color inside frames. They are the only color on the page, which makes
  them read as evidence.

## Avoid
- Adding a brand accent "for interest"; the restraint is the identity.
- Gray boxes, card grids, or hairline tables between scenes.
- Moving or zooming photographs continuously while the user scrolls.
- Mono labels, uppercase eyebrows, or dense small print.
- Effects on large layers during scroll (blend modes, filters, big blurs).
- Universal rules still apply: references/rules/core.md, references/rules/color.md, references/rules/motion.md.

## In apps vs. on websites
- Websites: everything above, with the key visual and the scroll story doing the persuading.
- Apps: a black interface with white type, gray hierarchy, one weight step for selection, and fluid state
  transitions (MOTION-27). Keep imagery to onboarding, empty states, and the sign-in screen.
