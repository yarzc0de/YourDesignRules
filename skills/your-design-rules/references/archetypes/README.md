# Archetypes

An archetype is a ready-made visual identity: a font pairing, color roles, shape, elevation, and an approach to
imagery. Use one when the user has given no brand or style direction. Read this file to choose, then open the
chosen archetype and the guide for the task (`references/guides/`). The universal rules in references/rules/core.md and
references/rules/color.md apply under every archetype.

## Index

| Archetype | Identity | Best for | Ground | Fonts |
|---|---|---|---|---|
| [Field Ledger](field-ledger.md) | A light technical sheet where outlined regions share their edges, monospace notes label the details, and one large readout of a real value anchors each view. | Infrastructure, developer tools, data utilities | Light | Titillium Web, IBM Plex Mono |
| [Night Console](night-console.md) | A dark product platform where the real working surface comes forward on an atmospheric ground and everything around it stays quiet. | Developer platforms, products used in a dark UI | Dark | Chakra Petch, Instrument Sans, Fragment Mono |
| [Calm Utility](calm-utility.md) | A neutral, restrained baseline for back-office tools and day-to-day web apps, where clarity comes first and a single accent shows what to do. | Admin tools, B2B SaaS, everyday web apps | Light | Manrope, Karla, Fragment Mono |
| [Civic Grid](civic-grid.md) | Expressive Swiss modernism for public information: oversized grotesque type steps across visible alignments inside deep margins, in plain language. | Public sector, education, information services | Light | Schibsted Grotesk, Public Sans, Martian Mono |
| [Quiet Tiles](quiet-tiles.md) | Friendly, detailed information sorted into soft tiles on a strict grid, with each tile's size and density set by what it holds. | Consumer productivity, wellness, personal planning | Light | Bricolage Grotesque, DM Sans, IBM Plex Mono |
| [Working Surface](working-surface.md) | Product-led marketing and apps in which a real, working native workflow is the argument: one surface, framed by navigation and an inspector. | Product-led SaaS marketing and apps | Light | Space Grotesk, Manrope, IBM Plex Mono |
| [Studio Sketchbook](studio-sketchbook.md) | Loose hand-drawn illustration and figures at human scale gather around a real task, so the product feels warm while its ground stays white or cool. | Consumer productivity, wellness, learning | Light | Fraunces, Karla |
| [Gallery Wall](gallery-wall.md) | Serif statements and photographs mounted like plates on white or cool mats, arranged with the stillness of a gallery. | Fashion, hospitality, galleries, portfolios | Light | Cormorant Infant, Karla |
| [Wide Horizon](wide-horizon.md) | Large photographs of a real place and tall condensed capitals put the visitor inside one scene that returns at different scales down the page. | Travel, outdoor, real estate, architecture | Either | Oswald, Hanken Grotesk |
| [Atelier Serif](atelier-serif.md) | A monumental high-contrast serif, true small caps, and hairline rules on pure white or deep black give craft and luxury work a measured, exact voice. | Fashion, luxury, craft, fine hospitality | Either | Bodoni Moda, Bodoni Moda SC, Archivo |
| [Frosted Depth](frosted-depth.md) | Translucent layers float in front of a solid reading plane, so the interface gains optical depth without giving up legibility. | AI assistants, creative and media tools, spatial products | Either | Red Hat Display, Instrument Sans |
| [Signal Color](signal-color.md) | Solid fields of saturated color and loud heavy type, where moving into a new field tells the reader the subject has changed. | Campaigns, launches, events, consumer brands | Light base with saturated fields | Archivo Black, DM Sans |
| [Specimen Notes](specimen-notes.md) | A subject presented like a specimen and surrounded by its evidence: callouts, rulers, measurements, and mono labels that explain what you are looking at. | Science, health, research, collections | Light | Space Grotesk, Newsreader, IBM Plex Mono |
| [Ambient Glow](ambient-glow.md) | Dense, heavy grotesque type on a deep field, with colored light falling in from the edges and every reading area kept solid. | AI products, creative tools, music, crypto | Dark | Darker Grotesque |
| [Broadsheet](broadsheet.md) | A front page rebuilt for screens: a masthead rule, heavy serif headlines, and a multi-column grid in which a story's importance sets its width. | Publications, newsrooms, education, public information | Light (or one deliberate color) | Petrona, Alata |
| [Monochrome Stage](monochrome-stage.md) | Black and white, cinematic, and very smooth: one monumental fine-art image, large soft geometric type, and a scroll that glides from scene to scene. | Launch pages for developer tools, AI, open source, premium software | Dark | Plus Jakarta Sans, Geist Mono |
| [Toybox](toybox.md) | Saturated color, inflated shapes, and sticker-like pieces arranged with intent around one clear statement and a calm path people can actually use. | Playful consumer brands, games, family products, events | Light (with saturated fields) | Unbounded, Outfit |

## Archetypes are a starting point

An archetype gives you a coherent kit. It does not make the page distinctive on its own: you still draw at
least two choices from the subject's world (CORE-23), write a plan and run the sameness test (CORE-24), and
make one bold decision (CORE-8). Push the archetype toward the subject: change the accent, the imagery, and
the opening moment so that two products using the same archetype still look like two different companies.
Broadsheet, Night Console, Ambient Glow, and Monochrome Stage sit close to house styles that are easy to
overuse (CORE-25); pick them only when the subject really calls for them — news, a developer platform, a
product used in the dark, or a story a black-and-white fine-art image genuinely carries — not because the user
said "smooth" or "premium". Smoothness is in the motion rules and belongs to every archetype.

## How to pick an archetype when there is no brand

1. Look for direction first. If the user supplied a brand, a style guide, reference designs, or named fonts and
   colors, follow that and skip archetypes. Check the project for existing tokens too (CORE-17). If they gave
   nothing, ask for one reference and three mood words before choosing (CORE-26); their answer outranks the
   product-type table below.
2. Read the request for three things: the kind of product, who uses it, and the mood its wording suggests.
3. Choose exactly one archetype and tell the user which one and why in a single line, for example "Using
   Broadsheet: a newsroom with many stories of mixed importance." Do not blend two archetypes.
4. Use the table below when the product type is clear. Where two candidates are listed, the last column says
   when the second one fits better.

   | Product type | Candidates | Prefer the second when |
   |---|---|---|
   | Developer tools, infrastructure | Field Ledger, Night Console | the product lives in a dark UI and its working surface is the pitch |
   | Admin tools, B2B SaaS | Calm Utility, Working Surface | the page sells the product by showing its real workflow |
   | Public sector, education, information | Civic Grid, Broadsheet | there are many stories or updates of uneven weight |
   | Consumer productivity, wellness | Quiet Tiles, Studio Sketchbook | the tone is personal and illustration suits the brand |
   | Travel, the outdoors, real estate | Wide Horizon | — |
   | Fashion, luxury goods, hospitality | Atelier Serif, Gallery Wall | photography of rooms or work should lead rather than type |
   | Science, health, research | Specimen Notes | — |
   | AI, creative tools, crypto | Ambient Glow, Frosted Depth | there is a central object and the platform already uses translucency |
   | Launch pages for dev tools, AI, open source, premium software | Working Surface, Monochrome Stage | a dramatic black-and-white fine-art image carries the story better than the real product view |
   | Consumer brands, campaigns, events | Signal Color, Toybox | the audience is families or the voice is playful |

   If nothing matches, use Calm Utility for product UI. For a marketing page, pick by the user's mood words and
   say so. "Smooth" is never an archetype: it comes from the motion rules (references/rules/motion.md) and every archetype
   can be smooth, so never read it as a reason to go dark or monochrome. "Premium" and "cinematic" are moods
   that several archetypes meet — match them to the subject: Atelier Serif or Gallery Wall for editorial calm,
   Wide Horizon for a place, Frosted Depth for soft depth, Monochrome Stage only when a black-and-white fine-art
   image truly leads. Do not funnel every premium page into one dark look.
5. Apply identity only. The archetype decides type, color, shape, elevation, and imagery. The number of sections,
   split ratios, density, and components still come from the content and the task guide (CORE-12).
6. Let user choices win. Any font, color, radius, or shadow setting the user names replaces the archetype's
   value, and every example palette is a starting point you may change (CORE-13).
7. Load the archetype's fonts from Google Fonts, request only the weights its typography table lists, and
   confirm in the render that they actually loaded.

## The file format

Every archetype file uses the same headings in the same order, so you can jump straight to the part you need.

- `# <Name>` followed by a one-sentence identity as a quote.
- `## When to pick`: product types, audiences, and the conditions under which the direction fails.
- `## Composition`: how space, alignment, and the website hero are handled, and how the direction adapts to
  product UI.
- `## Typography`: a role, family, and weights table, scale notes, and the Google Fonts families to load.
- `## Color roles`: ground, surfaces, text, accent, boundary, and status, with one example palette.
- `## Shape and elevation`: radius values in px and the shadow policy.
- `## Motion`: the direction's motion character; timing and accessibility come from references/rules/motion.md.
- `## Imagery`: subjects, sources, treatments, and icons.
- `## Avoid`: the mistakes that break this particular direction, ending with a one-line link to the universal
  rules.
- `## In apps vs. on websites`: how the identity changes between a working product and a marketing page.
