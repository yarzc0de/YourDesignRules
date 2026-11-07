# Examples

Two tasks, each built twice from the same prompt and the same facts by the same model:

- **before**: a plain request ("make it look good and modern"), built in one pass with no rules loaded.
- **after**: the same request with the `your-design-rules` skill active. The agent followed the skill's
  workflow: read the core rules and the task guide, picked an archetype, built section by section, and ran
  `rules/review-checklist.md` on screenshots after each section.

The checklist loop is part of the skill, so the "after" runs took longer. That difference is the point: the
rules make the agent look at its own render and fix what it sees.

## Landing page: Tidewell

A sleep-tracking ring for shift workers. The brief contained only product facts (sensors, shift-calendar
sleep plan, 6-day battery, titanium, 3.1 g, 50 m, $249, no subscription, ships in 3 weeks, 30-day returns,
sizes 6–13). It contained no testimonials, press logos, or user counts.

| | Before | After |
|---|---|---|
| Desktop | [before-1440.jpg](landing-page/before-1440.jpg) | [after-1440.jpg](landing-page/after-1440.jpg) |
| Phone | [before-390.jpg](landing-page/before-390.jpg) | [after-390.jpg](landing-page/after-390.jpg) |
| HTML | [before.html](landing-page/before.html) | [after.html](landing-page/after.html) |

What the rules changed:

| Before | After | Rules |
|---|---|---|
| Split hero: text column beside a ring drawn in CSS | One continuous stage: a photo of someone asleep at midday wearing the ring, headline in its quiet area | LAY-20, IMG-5 |
| Band of three boxes under the hero: "Nurses / Pilots / Factory crews" | Audience named in the subhead | CORE-21, LAND-17 |
| Two sections of three identical cards each | One timeline that shows a sample night shift turned into a sleep plan | CORE-8, CORE-22 |
| The same dark navy density in every section | Dark hero, light problem statement, gray timeline, white specs, dark pre-order | LAND-10, LAY-28 |
| No image of the outcome | The hero shows the outcome; the ring is annotated like a specimen | IMG-18 |

Archetype chosen: **Specimen Notes** (Space Grotesk, Newsreader, IBM Plex Mono). Both images in `after.html`
are AI-generated (the product is fictional, so stock photography could not show it) and are embedded in the
file. The timeline is labeled as an illustration with a sample schedule.

## Dashboard: Crumb & Co

The home screen of a bakery chain's back-office app, seen right after login, with a sidebar (Dashboard,
Orders, Inventory, Stores, Staff, Reports, Settings). Question to answer: "Which store needs attention right
now?" The brief contained today's figures for four stores, four low-stock items, eight recent orders, and
the oven status at one store.

| | Before | After |
|---|---|---|
| Desktop | [before-1440.jpg](dashboard/before-1440.jpg) | [after-1440.jpg](dashboard/after-1440.jpg) |
| Phone | [before-390.jpg](dashboard/before-390.jpg) | [after-390.jpg](dashboard/after-390.jpg), [menu open](dashboard/after-menu-375.jpg) |
| HTML | [before.html](dashboard/before.html) | [after.html](dashboard/after.html) |

What the rules changed:

| Before | After | Rules |
|---|---|---|
| Cream page background | White ground, cool gray sidebar | COLOR-8 |
| Sidebar stops at the first screen height, leaving an empty strip below | Sidebar runs the full height | CHK-1 |
| Four equal store cards, a boxed alert panel with an icon in a tinted square per item | One lead answer (Old Town, −14%, oven offline, low stock, refund) and a ranked bar chart for all four stores | CORE-6, CORE-21, CORE-22, DATA-2 |
| Cards around every table | Tables sit on the page, separated by whitespace and hairlines | CORE-6, LAY-11 |
| Three competing buttons in the alert | One primary action, "Open Old Town" | WEB-12 |
| Notification bell with an unread dot, though the brief has no notifications | Only supplied data | CORE-9 |

Archetype chosen: **Calm Utility** (Manrope, Karla, Fragment Mono). Below 1024 px the sidebar becomes a
sheet that slides in from the left (MOTION-15), and the tables turn into list rows (DATA-17). Loading, empty,
and error states can be previewed with `?state=loading`, `?state=empty`, or `?state=error`.

## Reproduce

Give an agent the prompt and facts above twice: once plain, once with the skill installed. Render both at
1440 and 390 px wide and compare them against `rules/review-checklist.md`.
