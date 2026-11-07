# Calm Utility
> A neutral, restrained baseline for back-office tools and day-to-day web apps, where clarity comes first and a single accent shows what to do.

## When to pick
- Admin panels, internal tools, settings, billing, CRM, scheduling, and other forms-heavy products.
- Any web app with no brand direction where the task is routine and the user wants to finish quickly.
- The fallback when nothing else in this folder clearly fits the request.
- Skip it when the brief asks for a strong mood or a memorable campaign; this direction is deliberately quiet.

## Composition
- Separate regions with tone and hairlines, not containers: the sidebar or a panel header sits on the surface
  tone, the work area on the ground, and a 1 px line marks where they meet.
- Pick the skeleton from the task (rules/layout.md): sidebar plus main for products with many areas, a top
  bar for few destinations, a fixed 320–360 px side column for record details.
- Repeat one page header pattern everywhere: the title at the same size on every screen, an optional one-line
  description, the primary action on the right.
- Run forms in one column up to about 640 px wide, grouped into titled sections split by a hairline rather
  than a card per section.
- Tables use hairline row dividers and 44–48 px rows by default, 36–40 px in compact views.
- Let the distinctive moment come from content: a clear summary figure, a well-written empty state, an
  activity timeline. Do not invent decoration to fill that role (CORE-8).
- Website hero: give the stage to one calm, wide photograph of the work the product supports, or to the
  product view built from real elements, with the headline in its quiet area or in a band right above it,
  never in a separate column beside it.

## Typography
| Role | Family | Weights |
|---|---|---|
| Headings | Manrope | 600, 700 |
| Body, UI, labels | Karla | 400, 500, 700 |
| IDs, amounts, timestamps | Fragment Mono | 400 |

- Page title 24–28 px Manrope 700, section title 18–20 px at 600, line height 1.2. Manrope has no italics, so
  never style a heading italic.
- Body 16 px on web pages, 14–15 px in app UI. Labels in Karla 500 at 13–14 px, sentence case; skip
  uppercase eyebrows unless the product already uses them.
- Use Fragment Mono for values in columns (IDs, amounts, dates) so digits line up; numbers inside sentences
  stay in Karla.
- Load from Google Fonts: Manrope (600, 700), Karla (400, 500, 700), Fragment Mono (400).

## Color roles
Light palette. Neutral ground plus one vivid accent.

| Role | Token | Example |
|---|---|---|
| Ground | `--background` | `#FFFFFF` |
| Surface (sidebar, panel headers, table header) | `--surface` | `#F5F7FA` |
| Selected (row, nav item) | `--accent-subtle` | `#EAF0FD` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#111827` / `#4B5563` / `#646B78` |
| Accent (actions, focus, links) | `--primary` | `#2F5FD0` with `#FFFFFF` text |
| Boundary (hairlines) / strong (inputs) | `--border`, `--border-strong` | `#E2E6EC` / `#838D9C` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#15803D`, `#B45309`, `#C0262D`, `#0369A1` |

- Give each status a pale tint for banners and badges, and keep its text in the full-strength color.
- For dark mode, build a separate palette as rules/color.md describes instead of inverting this one.
- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Panels, dialogs, and cards that bound a real object: 10–12 px. Buttons and inputs: 8 px or fully rounded,
  one choice for the whole product. Badges: fully rounded. Tables: square inside their container.
- Mostly flat. Menus and popovers get the small shadow from rules/color.md plus a hairline; panels get none.
- Dialogs sit over a scrim so they need no heavier shadow.
- Focus: a 2 px accent ring with a 2 px offset on every interactive control.

## Imagery
- Icons carry most of the visual load: one library (Lucide or Heroicons) at 16 px in dense UI and 20 px in
  navigation, 1.5 px stroke, always beside a text label except for search, close, and menu.
- Empty states: one icon, one sentence that says what will appear here, one action. No illustration sets.
- Avatars: real photos the user supplies, otherwise initials on a neutral tint.
- Marketing photos: real people at real work in natural light, never posed handshakes.

## Avoid
- An accent-colored sidebar or a gradient page header.
- A row of eight equal KPI cards.
- Every settings group wrapped in its own shadowed card.
- A second accent hue added for variety.
- Icon-only navigation.
- Pill buttons and 8 px buttons on the same screen.
- Placeholder text standing in for field labels.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps: medium density by default, compact for tables and logs; one primary button per screen or section;
  destructive actions in their own color and position.
- Apps: keep every pattern (header, table, form, empty state) identical across screens; consistency is the
  point of this direction.
- Websites: the same calm voice at a larger scale, with display headlines at 40–56 px in Manrope 700 and
  sections separated by whitespace and the surface tone.
- Websites: the accent appears only on calls to action and links.
