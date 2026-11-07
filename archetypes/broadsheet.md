# Broadsheet
> A front page rebuilt for screens: a masthead rule, heavy serif headlines, and a multi-column grid in which a story's importance sets its width.

## When to pick

- Publications, newsletters, journals, newsrooms of public agencies, universities, think tanks, annual reports,
  and long-form features.
- Any site that carries many stories of uneven importance and publishes often.
- Teams that need a structure able to absorb volume without redesign.
- Skip it for single-product marketing or a page with one message.

## Composition

- Masthead: the name, the date or issue, and a heavy rule beneath it, such as 4 px over 1 px.
- A 12-column grid on desktop. The lead story spans 6–8 columns, secondary stories 3–4, briefs 2–3. Rank shows
  through column span and headline size together.
- 1 px column rules separate stories instead of cards. Gutters are 24–32 px with the rule centered in them.
- Kickers (section labels) sit above headlines in Alata capitals; bylines and timestamps sit below in small Alata.
- Website hero: the lead story is the stage. One commanding photograph spans the lead columns and the headline
  sits large in a deliberate band directly above it, so picture and headline read as a single unit. This applies
  to the site opening only; see rules/layout.md.
- Article pages use one reading column of 60–70 characters, with pull quotes breaking the column and captions
  under images.
- In product UI (reader apps, editorial tools), the front page becomes a ranked list that keeps the same type
  system.

## Typography

| Role | Family | Weights |
|---|---|---|
| Headlines, body, pull quotes | Petrona | 400, 400 italic, 600, 800, 900 |
| Kickers, bylines, navigation, UI | Alata | 400 (only weight) |

- Lead headline at 56–96 px, weight 900, line height 1.0–1.05, tracking −1.5%. Secondary headlines at 28–36 px,
  weight 800. Briefs at 18–22 px, weight 600.
- Body in Petrona 400 at 18 px, line height 1.55, 55–65 characters per column.
- Alata labels at 12–14 px, capitals, +6% tracking. With a single weight, UI text is ranked by size and case.
- Standfirsts (the line under a headline) in Petrona 400 at 20–22 px in secondary text color.
- Load from Google Fonts: Petrona, Alata.

## Color roles

Light example on white. It is a starting point (CORE-13).

| Role | Example | Use |
|---|---|---|
| Ground | `#FFFFFF` | Page background |
| Surface | `#F4F5F7` | Briefing rails, newsletter sign-up, inputs |
| Text primary | `#121212` | Headlines, body |
| Text secondary | `#3F4247` | Standfirsts, captions |
| Text muted | `#61656B` | Bylines, timestamps, credits |
| Text inverse | `#FFFFFF` | Text on the accent |
| Accent | `#1A47B8` | Links, subscribe action, active section |
| Boundary | `#121212` masthead and section rules, `#C8CBD0` column rules | Input outlines `#8A8F96` |
| Status | success `#1D7A46`, warning `#9A5B00`, error `#B3261E`, info `#0F6E7E` | Always with a label or icon |

- "Live" and "Breaking" labels use the error red only when the story is actually live, always with the word.
- A special report may take one deliberate saturated ground, such as a full cobalt or deep green section. Never a
  yellowed newsprint tint.

## Shape and elevation

- Square geometry: radius 0 on images, buttons, inputs, and tags.
- No shadows. Rules and gutters do all the separating.
- Rule weights form a small system: 4 px masthead, 2 px section openers, 1 px column and story dividers.

## Motion
- Almost none: the front page loads complete; story previews on hover change only the headline underline, 150 ms.
- Live updates (a new story, a changed figure) get a brief highlight band that fades over 2 s.
- No scroll reveals; a newspaper is already in place when you look at it.
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery

- Reportage photography of real people, places, and events, always credited.
- Captions and credits sit outside the image, beneath it, in Petrona italic or small Alata.
- Image size follows story rank. The lead gets the largest picture; briefs often have none.
- Charts and maps are real elements in the publication's palette with one highlighted series.
- Icons stay minimal (search, menu, share) at 20 px.

## Avoid

- Beige or newsprint grounds, paper textures, distressed type.
- Stories as shadowed cards (CORE-6).
- Every story at the same size in a uniform grid.
- A blackletter masthead built from primitives. A real logo needs a designer asset.
- Captions laid over photographs.
- Alata for headlines or body copy.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/typography.md, rules/color.md,
  and rules/review-checklist.md.

## In apps vs. on websites

- Websites: a front page grid, section fronts with the same grid at smaller scale, and single-column article
  pages.
- Apps (readers, editorial tools): a story list ranked by headline size, a single-column article view, Alata for
  tabs and controls, plain settings screens.
- Editorial tools keep Petrona for story titles in lists so the editor sees stories as readers will.
- On phones, columns collapse to one. The lead keeps its photograph, rank stays visible through headline size, and
  the rules remain.
