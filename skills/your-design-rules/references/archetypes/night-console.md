# Night Console
> A dark product platform where the real working surface comes forward on an atmospheric ground and everything around it stays quiet.

## When to pick
- Developer platforms, cloud and model consoles, security and observability tools, audio and video software.
- Products used in long sessions or low light, by people who already work in dark editors.
- Marketing for a technical product whose interface is the strongest proof it has.
- Skip it for public information, forms-heavy admin, or audiences who print and share their screens.

## Composition
- Rank planes by brightness: the working surface (editor, graph, log stream, query result) is the largest and
  lightest plane; navigation, toolbars, and status bars sit darker and lower in contrast.
- Keep the atmosphere in the ground: one broad, low-chroma pool of light behind the main surface, placed
  off-center and fading to the base ground well before the viewport edges.
- Keep the surroundings quiet: muted nav labels, outline icons, no decorative panels. The working surface
  holds the color and the contrast.
- Light falls behind content onto the ground. It never sits on type, icons, or borders.
- Product UI skeleton: sidebar 240–264 px, top bar 48–56 px, fluid main surface, and an inspector of 320–360
  px when a selection needs detail; a command palette for frequent users.
- Website hero: put the promise in a band at the top of the dark field and let the live product surface, built
  from real elements, rise beneath it across the width and past the fold, with the light pooling behind the
  frame; never a text column beside a boxed screenshot.
- Later sections reuse that same surface at tighter crops instead of introducing new mock panels.

## Typography
| Role | Family | Weights |
|---|---|---|
| Display, page and section titles | Chakra Petch | 500, 600 |
| UI, body | Instrument Sans | 400, 500, 600 |
| Code, logs, values | Fragment Mono | 400, italic 400 |

- Chakra Petch only at 24 px and up: marketing headlines 48–72 px with −1% tracking, app page titles 24–28 px.
  Short uppercase eyebrows at 12 px with +8% tracking are fine; buttons, labels, and paragraphs are not.
- Instrument Sans 14–15 px in app UI, 16–18 px for marketing body. Stay at 400 or heavier on this ground;
  thinner strokes break up at small sizes.
- Fragment Mono ships one weight. Emphasize inside code with color or a surface tint, never with bold, which
  the browser would fake.
- Load from Google Fonts: Chakra Petch (500, 600), Instrument Sans (400–600), Fragment Mono (400 and italic).

## Color roles
Dark palette. Each step up in elevation is a lighter surface.

| Role | Token | Example |
|---|---|---|
| Ground | `--background` | `#0B0E14` |
| Surface (panels, the working plane) | `--surface` | `#131823` |
| Surface raised (menus, inspector) | `--surface-raised` | `#1B2130` |
| Overlay (dialogs, command palette) | `--overlay` | `#232A3B` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#E6E9EF` / `#A9B1C0` / `#8C95A6` |
| Accent (actions, selection) | `--primary` | `#7AA2FF` with `#0B0E14` text |
| Boundary (hairlines) / strong (inputs) | `--border`, `--border-strong` | `#2A3243` / `#66718A` |
| Ground light | `--ground-light` | accent at 10–16% opacity in a radial falloff |
| Status | `--success`, `--warning`, `--error`, `--info` | `#5BD08A`, `#F2B84B`, `#FF7A7A`, `#8FC1E3` |

- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Radius 6 px on buttons, inputs, and chips; 8 px on panels and menus; 12 px on dialogs and the website
  product frame.
- Raise a surface by making it lighter first, then add a 1 px top hairline at about 6% white so its edge reads.
- A large, diffuse shadow is allowed on the website product frame and on floating dialogs, within the limits
  in references/rules/color.md. Items in a grid get none.
- Selected rows: raised surface, a 2 px accent bar on the leading edge, and an accent label or filled icon.

## Motion
- Quiet and fast in the workspace: 150–250 ms fades and short 8 px slides for panels and inspectors.
- Glow never pulses or breathes; status lights change color once and stay.
- Website: the product surface may assemble once on load (panels fading in with a 40 ms stagger), then everything holds still.
- Timing, easing, and reduced-motion rules: references/rules/motion.md.

## Imagery
- The product surface is the main image. Fill it with the user's real data or clearly marked sample data
  (CORE-9).
- Build the atmosphere with native gradients, not a photograph or a generated texture.
- If a photo is needed (a team, hardware, a server room), pick a low-key shot with one light source and crop
  it so its dark areas dissolve into the ground.
- Icons: one outline library at 16 or 20 px, 1.5 px stroke, muted by default; the filled variant or the accent
  marks the selected item.
- Charts: neutral gray series on the surface, one accent highlight.

## Avoid
- Glowing type, neon outlines, or text shadows.
- A wall of cards, each with its own glow or gradient border.
- Fake terminal output: invented commands, made-up logs, code that would not run. Use the user's real
  snippets or leave the block out.
- Matrix rain, scanlines, and lens flares.
- Chakra Petch in buttons, form labels, or paragraphs.
- Universal rules still apply: CORE-4 to CORE-8 in references/rules/core.md, plus references/rules/color.md (including its dark mode
  guidance) and references/rules/review-checklist.md.

## In apps vs. on websites
- Apps: turn the ground light down to almost nothing on working screens; keep it for sign-in, empty states,
  and onboarding.
- Apps: compact to medium density, collapsible side panels, and a working surface that takes most of the width.
- Websites: one pool of light near the top and at most one more near the closing call to action.
- Websites: pace sections by alternating the base ground with a slightly lighter surface band; copy code
  samples from the real docs.
