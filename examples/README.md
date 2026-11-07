# Examples

Four tasks, each built twice from the same prompt and the same facts by the same model:

- **before**: a plain request ("make it look good and modern"), built in one pass with no rules loaded.
- **after**: the same request with the `your-design-rules` skill active. The agent followed the skill's
  workflow: read the core rules and the task guide, picked an archetype, built section by section, and ran
  `rules/review-checklist.md` on screenshots after each section.

The checklist loop is part of the skill, so the "after" runs took longer. That difference is the point: the
rules make the agent look at its own render and fix what it sees.

## One skill, three identities

Asked for three different subjects, the skill picks three different archetypes and builds three pages that do
not look like each other. That is the job of the archetype layer: smooth motion is shared craft, but the
identity comes from the subject.

| Page | Archetype | Ground | Type |
|---|---|---|---|
| [Sunshift](saas-landing/after.html) — on-call SaaS ([fold](saas-landing/after-fold.jpg)) | Working Surface | White, daylit | Space Grotesk · Manrope |
| [Marl](ceramics-landing/after.html) — ceramics studio ([fold](ceramics-landing/after-fold.jpg)) | Gallery Wall | White, warm | Cormorant Infant · Karla |
| [This repo's site](../docs/index.html) — [live](https://yarzc0de.github.io/YourDesignRules/) ([fold](project-site/fold.jpg)) | Monochrome Stage | Black, cinematic | Plus Jakarta Sans |

All three pass the same checks — smooth scroll, no frame over 25 ms at 2× density and 4× CPU, no rows of equal
boxes. Only the identity differs, because the subject does.

## SaaS landing page: Sunshift

On-call scheduling and incident handoff for engineering teams across time zones. The brief listed the
features, integrations, pricing, and hosting; it had no customers, logos, testimonials, or usage numbers. Both
runs could generate images.

| | Before | After |
|---|---|---|
| First screen | [before-fold.jpg](saas-landing/before-fold.jpg) | [after-fold.jpg](saas-landing/after-fold.jpg) |
| Full page | [before-1440.jpg](saas-landing/before-1440.jpg) | [after-1440.jpg](saas-landing/after-1440.jpg) (still frame) |
| Phone | [before-390.jpg](saas-landing/before-390.jpg) | [after-390.jpg](saas-landing/after-390.jpg) |
| Scroll | | [after-scroll-filmstrip.jpg](saas-landing/after-scroll-filmstrip.jpg) |
| HTML | [before.html](saas-landing/before.html) | [after.html](saas-landing/after.html) |

| Before | After | Rules |
|---|---|---|
| Cream ground, serif headline, orange accent, one word in orange italic | White daylit ground, one burnt-orange accent held back for actions and the live "now" state, cool-gray section bands | CORE-25, COLOR-8 |
| Pill badge above the headline, logo strip of integrations | Neither; integrations are named as text and shown inside the real product crops | CORE-22, IMG-5 |
| Text column beside a small boxed schedule widget | The product's own follow-the-sun rotation board shown large as the hero: a 24-hour day/night band with each engineer in their time zone and a live UTC "now" line | LAY-20, LAND-18, WEB-22 |
| Three zigzag feature rows and a row of three equal cards | One live rotation surface; the handoff, incident, and escalation shown as real product crops, with no equal feature cards | CORE-8, CORE-21 |
| Every section fades in the same way (and stays invisible in a full-page capture) | Load sequence, then a scroll story: the sun sweeps a full UTC day and the on-call baton passes Jonas → Dana → Mei; each later section plays its entrance once | MOTION-19, MOTION-25, MOTION-28 |

Archetype chosen: **Working Surface** — the product's own follow-the-sun rotation board is the hero, on a
light ground with a single burnt-orange accent reserved for actions and the live state.

## SaaS app screen: Sunshift "Now"

The screen an engineering manager sees after login: who is on call, what is burning, and whether the next
handoff is ready. The brief listed six engineers in six time zones, today's rotation, two open incidents, two
deploys, the last handoff, weekly page counts, and integrations. Both runs could generate portraits.

| | Before | After |
|---|---|---|
| First screen | [before-fold.jpg](saas-app/before-fold.jpg) | [after-fold.jpg](saas-app/after-fold.jpg) |
| Full page | [before-1440.jpg](saas-app/before-1440.jpg) | [after-1440.jpg](saas-app/after-1440.jpg) |
| Phone | [before-390.jpg](saas-app/before-390.jpg) | [after-390.jpg](saas-app/after-390.jpg) |
| HTML | [before.html](saas-app/before.html) | [after.html](saas-app/after.html) |

| Before | After | Rules |
|---|---|---|
| Warm cream ground; the sidebar stops partway down the page | White app with a full-height sidebar | COLOR-8, CHK-1 |
| Three cards on top, four equal cards below, uppercase eyebrows on each | One dark working-surface panel leads; the rest is plain sections | CORE-21, CORE-22, WEB-22 |
| A Gantt chart of colored shift bars | Each engineer's local daylight drawn as a band; shifts cascade like a relay; one gold "now" line crosses rotation, incidents, and deploys | WEB-22, WEB-26, CORE-23 |
| Static states | Live now-line, selected incident with its detail open, drafted handoff note | WEB-23 |
| Hard cuts between states | Tabs crossfade with view transitions, the indicator slides, the handoff drawer slides from its edge, popovers grow from their trigger | MOTION-26, MOTION-27 |

Archetype chosen: **Working Surface**, sharing its palette and type with the Sunshift landing page.

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

## Landing page: Marl (ceramics studio)

A one-person studio throwing small-batch stoneware. The brief had only product facts (one-of-a-kind pieces,
lead-free glazes, a monthly drop, $28–$120, made to order, 30-day returns) and, as the reference and three
mood words the skill asks for when there is no brand, "a quiet printed gallery catalogue" and "warm, handmade,
editorial".

| | Desktop | Phone |
|---|---|---|
| After | [after-1440.jpg](ceramics-landing/after-1440.jpg) | [after-390.jpg](ceramics-landing/after-390.jpg) |
| HTML | [after.html](ceramics-landing/after.html) | |

Archetype chosen: **Gallery Wall** — the reference is the archetype almost verbatim. One art-directed,
warm-lit full-bleed photograph of the making carries the hero, and the page reads as a catalogue of numbered
plates with evidence captions. The accent is a single deep iron-oxide glaze tone, kept off any cream ground to
dodge the generator house style (CORE-25); the collection is an asymmetric hang, not a four-up card grid
(CORE-21). This run and Sunshift started from the same rules and the same model; only the subject changed.

## The project's own site: Monochrome Stage

This repository's landing page — [live](https://yarzc0de.github.io/YourDesignRules/), source at
[docs/index.html](../docs/index.html) — was built with the skill. It is the Monochrome Stage case: black and
white, one monumental fine-art key visual, large soft geometric type, and a scroll that glides from scene to
scene ([fold](project-site/fold.jpg), [full page](project-site/full-1440.jpg)).

Archetype chosen: **Monochrome Stage**. The bold decision is a single black-and-white fine-art image carrying
the hero, with the headline set in its empty sky; the page then moves through a word-by-word manifesto, a
before/after wipe over the two SaaS examples, and a horizontal rules track. One Lenis loop, transform and
opacity only, no frame over 25 ms at 2× density.

## Reproduce

Give an agent the prompt and facts above twice: once plain, once with the skill installed. Render both at
1440 and 390 px wide and compare them against `rules/review-checklist.md`.
