# Core rules

These rules apply to every interface you build: product screens, marketing pages, mobile apps, dashboards,
slides. Read this file first, then the guide for the task (`references/guides/`) and the rule files it points to. When a
guide or archetype seems to disagree with a core rule, the core rule wins unless the user explicitly asked
for the exception.

## Purpose and focus

### CORE-1 · Give every view one job and one primary action
Before placing anything, write down the single question this view answers and the one action it exists to
enable. If you find two equally important jobs, split them into two views, tabs, or steps.
- **Why:** a view that tries to do everything gives the user no starting point.
- **Check:** you can state the view's job in one sentence and point at its primary action.

### CORE-2 · Make one region dominant
Each view has one area that is clearly the most important: the headline and image, the editor canvas, the
chart, the list being worked on. Everything else is visibly secondary. Avoid layouts where three or four
regions carry the same weight.
- **Why:** the eye needs a place to land; equal weight reads as noise.
- **Check:** squint at the render. One region still stands out.

### CORE-3 · Let hierarchy come from type, position, and contrast
Signal importance with size, weight, placement, and contrast. Make the key statement, the selected item, or
the working value impossible to miss. Supporting text is quieter but still comfortably readable. Adding a box
around something is the last resort for emphasis, not the first.
- **Why:** boxes multiply quickly and flatten hierarchy instead of creating it.
- **Check:** remove every border and background in your head. The order of importance is still obvious.

## Reduction

### CORE-4 · Run a reduction pass before you call it done
Explore freely while building, then edit. Delete or merge: messages that repeat, emphasis that competes,
containers nested for no reason, labels that restate what is already visible, decoration without a role. For
each remaining element ask: "If this vanished, what would the user lose?" If the answer is "nothing",
remove it, merge it, or make it quieter. Re-inspect and repeat until the next cut would hurt.
- **Why:** first drafts collect clutter; the edit is where design quality comes from.
- **Check:** you can name the job of every element on the screen.

### CORE-5 · Reduce noise, not substance
Reduction does not mean sparse. Hold on to the detail people use, the controls they need, type with
character, and the photos or illustration that make the product recognizable. Group related information before hiding any of it, and never
hide context the user needs to make a decision. A rich screen is fine when each part earns its place.
- **Why:** over-minimal screens push work onto the user and look unfinished.
- **Check:** nothing the user needs for the primary task sits behind an extra click.

### CORE-6 · Do not wrap every element in a card
Use a container only when it does real work: it bounds an object the user can select, drag, or open; it lifts
an overlay above the page; or it separates a distinct data record. For everything else, separate with
whitespace, alignment, a single hairline, or a change of surface tone.
- **Why:** card-inside-card-inside-section is the most recognizable sign of generated UI.
- **Check:** for each container, say what breaks if it becomes plain content on the page. "Nothing" means
  remove it.

**Avoid:** a features section where each of six one-line benefits sits in its own bordered, shadowed,
rounded card.
**Do:** a two-column list with a bold lead-in per item, aligned to one grid line.

### CORE-7 · Use effects sparingly and on purpose
Gradients, drop shadows, large corner radii, glows, blur, and glass are opt-in. Use them when the user asks,
when the brand or chosen archetype calls for them, or when they explain something (depth of an overlay, a
light source). One deliberate effect beats four default ones. Shadow and gradient limits live in
`references/rules/color.md`.
- **Why:** stacked effects date a design instantly and hide weak structure.
- **Check:** each effect on the page has a reason you can say out loud.

### CORE-8 · Make one bold decision and commit to it
Clean is the floor, not the goal. Every page needs one thing a visitor would remember and describe to someone
else, pushed far enough to be unmistakable, with everything around it kept quiet. Pick one lever:
- **Scale:** display type 6–10× the body size, or one number set as large as the screen allows.
- **Color:** a whole section or the entire ground in one confident, saturated color.
- **Image:** a single art-directed photograph or illustration, full-bleed, cropped with intent.
- **Product:** the real interface shown huge, in a meaningful state, built from live elements.
- **Structure:** an asymmetric grid, a type-only section, a diagram, or an interactive moment.

Product UIs spend their boldness on the working surface (a hero chart, a canvas, a map), never on
decoration, and still reuse their patterns (see `references/guides/web-app.md`).
- **Why:** a page that only avoids mistakes looks like every other careful page; distinctiveness is what
  makes it feel authored.
- **Check:** describe the page in one sentence without naming its content. If the sentence would fit any
  product ("clean layout, white background, blue button"), the bold decision is missing.

## Honest content

### CORE-9 · Use real content and invent nothing
Treat the facts the user supplied as the complete dataset. Do not make up metrics, chart series, customer
logos, testimonials, awards, partner names, or "completed" system states. When a sample is unavoidable,
make it obviously illustrative (round numbers, "Sample data" label, generic names) and tell the user.
- **Why:** invented proof misleads real visitors and gets shipped by accident.
- **Check:** every number and claim on screen traces back to the brief or is labeled as a sample.

### CORE-10 · Build UI from real elements, not pictures of UI
Text, buttons, inputs, tables, charts, and diagrams are built as live, editable elements. Never place a
generated image or screenshot where an interface should be, and never bake labels or data into an image.
- **Why:** pictures of UI can't be edited, translated, read by screen readers, or kept in sync.
- **Check:** you can select and edit every piece of text on the screen.

### CORE-11 · Keep confirmation before irreversible actions
Destructive or committing actions (delete, pay, send, publish) need a confirmation step or an undo. Show the
resulting state after the action.
- **Why:** a design that skips confirmation teaches the implementation to skip it too.
- **Check:** every destructive action has a confirm or undo path in the design.

## Identity and choices

### CORE-12 · Treat a style as an identity, not a template
An archetype (see `references/archetypes/`) or brand guide decides type, color, imagery, shape, and material. It does
not decide how many sections you build, what ratio a split uses, or how many cards appear. Compose for this
company, this content, and this task.
- **Why:** copying a template's skeleton produces the same page for every product.
- **Check:** the section list came from the content, not from the archetype file.

### CORE-13 · Honor explicit user choices
Fonts, colors, radius, and shadow settings the user specified, or that appear in supplied brand guidelines,
are hard constraints. Suggested palettes in archetypes are starting points you may replace.
- **Why:** the user's stated preferences outrank your taste.
- **Check:** every user-specified value appears unchanged in the output.

## Process

### CORE-14 · Show something early, then iterate
Get a first rough but visible version on screen quickly, then refine it. Don't plan every detail in your head
before rendering anything.
- **Why:** users want to see progress, and the render reveals problems planning misses.
- **Check:** the first render happens before you polish any single section.

### CORE-15 · Verify each section right after you build it
Render and look at every section as soon as it is done, at its intended size, using
`references/rules/review-checklist.md`. Don't wait until the whole page is finished.
- **Why:** errors compound; a broken header found late means rework everywhere.
- **Check:** each section was rendered and checked before the next one started.

### CORE-16 · Fix in place instead of regenerating
After a review, correct the existing elements. Don't delete a screen and rebuild it from scratch to fix a
spacing or color problem.
- **Why:** regenerating discards work that was right and introduces new errors.
- **Check:** fixes touch only the elements that were wrong.

### CORE-17 · Reuse before you create
Reuse existing components, tokens, and content in the project. When UI repeats (buttons, rows, cards, nav
items), build it once as a component and reuse it. Never overwrite existing tokens or variables without
being asked.
- **Why:** reuse keeps the system consistent and makes later edits propagate.
- **Check:** no component is duplicated with small, accidental differences.

### CORE-18 · Do exactly what was asked on edit requests
When the user asks for a specific change (move, remove, reorder, rename, copy, recolor), make that change and
nothing else. Suggest further improvements in your reply instead of applying them.
- **Why:** unrequested edits break trust and are hard to review.
- **Check:** the diff contains only the requested change.

### CORE-19 · Deliver information when asked to research or compare
When the request is to investigate options, weigh vendors, or prepare a plan, the output is that
information laid out clearly (a table, a brief, a comparison), not a marketing website about the topic.
- **Why:** a styled landing page about competitors answers nothing.
- **Check:** the deliverable can be read and acted on without scrolling through decoration.

### CORE-20 · Report limitations outside the product
If a font failed to load, an image could not be generated, or data was missing, tell the user in your reply.
Never write notes like "image unavailable" or "placeholder font" into the interface itself.
- **Why:** process notes inside the UI get shipped.
- **Check:** the rendered UI contains only product content.

## Generated-UI tells

These patterns show up in almost every machine-made page. They look tidy, say little, and make products
indistinguishable. Treat each one as a default to avoid, not a building block.

### CORE-21 · Don't fill space with rows of equal boxes
The pattern: three or four same-size boxes in a row, each holding a bold label and a one-line gray caption,
usually split by borders or vertical hairlines. Typical forms: an audience strip under the hero ("Nurses /
Pilots / Factory crews"), a feature trio, a "01 / 02 / 03" steps row, a quartet of KPI tiles. It gives every
item the same weight and adds a band of near-empty boxes between the parts that matter.
Instead:
- Say it in the copy: "for nurses, pilots, and factory crews" in the headline or subhead.
- Show it: let the imagery depict the audience or the outcome.
- Rank it: give one item the lead (bigger, with an image or a real detail) and make the rest subordinate.
- Write it: a plain sentence or a short list with bold lead-ins, aligned to the text column.

Keep an equal row only when the items are truly parallel and each carries enough content to compare side by
side: pricing tiers, plan comparisons, a product spec table.
- **Why:** equal boxes with one-line captions are the most recognizable filler in generated pages.
- **Check:** no row of three or more equal boxes whose content is a label plus one line or less.

**Avoid:** a band under the hero with three bordered cells: "Nurses — Three 12s, a day off, then a flip to
nights" / "Pilots — Early reports, late finishes" / "Factory crews — Days, swings, and nights".
**Do:** "Built for nurses, pilots, and anyone whose schedule flips between days and nights." in the hero
subhead, with a photo of a nurse heading home at dawn.

### CORE-22 · Question the rest of the generated-page kit
Each of these needs a reason specific to this product, or it goes:
- an icon in a tinted rounded square above every feature title;
- a small uppercase eyebrow label above every section heading;
- a pill badge ("New", "Now in beta") above the hero headline when nothing is new;
- a row of checkmarks with "No credit card / Cancel anytime" under every button;
- a grid of identical cards repeated in two or more sections;
- a gradient blob or glow behind the hero for no stated light source;
- a stat strip of big numbers that the brief never supplied;
- one word in the headline picked out in italic, bold, or a different color;
- tracked-out all-caps labels on small text everywhere;
- metadata strung together with middle dots ("A · B · C") as the default way to show facts;
- a monospace face for small labels and numbers when the product has nothing to do with code or data;
- an arrow glyph appended to every link and button label;
- numbered markers (01 / 02 / 03) on content that is not a sequence.
- **Why:** each item alone is harmless; together they are the template every generator ships.
- **Check:** for each kit item present, you can name what it does for this product. Otherwise remove it.

## Distinctiveness

### CORE-23 · Take the look from the subject's world
Before choosing a palette or a font, list what the product's world actually looks like: its materials,
tools, places, documents, signage, and vocabulary. A night-shift sleep product lives in dim rooms and early
light; a freight tool lives in manifests, containers, and route maps; a kids' coding app lives in toy
blocks and bright plastic. Draw at least two choices (color, type, image, structure, or the opening moment)
from that list, and open the page with the most characteristic thing in that world.
- **Why:** choices borrowed from the subject cannot be mistaken for another product's page.
- **Check:** you can name the real-world source behind at least two visual choices.

### CORE-24 · Write a design plan, then test it for sameness
Before writing code, put down a compact plan:
- **Palette:** 4–6 named hex values with their roles.
- **Type:** families, roles, and the size of the largest and smallest text.
- **Layout:** one sentence per main section plus a rough ASCII wireframe of the first screen.
- **Bold decision:** the one lever from CORE-8 and where it lives.

Then run the sameness test: imagine a similar brief for a competitor. Would you produce nearly the same plan?
For each part where the answer is yes, change it to something this brief specifically justifies, and say what
you changed. Only then build.
- **Why:** generated designs converge because the first idea is always the average idea.
- **Check:** the plan names at least one change made after the sameness test.

### CORE-25 · Avoid the house styles generators fall into
These looks show up regardless of the subject. Use one only when the brief asks for it or the subject
genuinely calls for it, and say why:
- cream or warm off-white ground, high-contrast serif headline, terracotta or clay accent;
- near-black ground with a single acid-green, electric-blue, or vermilion accent;
- newspaper layout with hairline rules, zero radius, and dense columns;
- the SaaS card kit: everything in identical rounded cards with one radius, one soft gray shadow, and
  decorative gradient washes;
- dark navy page with a purple-to-blue gradient and glowing product screenshots.
- **Why:** a look that appears for every subject tells the visitor nobody made a choice.
- **Check:** if your plan matches one of these, the plan states the brief-specific reason.

## Where to go next

| Task | Read next |
|---|---|
| Any layout or spacing decision | `references/rules/layout.md` |
| Fonts, sizes, line length | `references/rules/typography.md` |
| Palette, contrast, shadows | `references/rules/color.md` |
| Transitions, hover and press states, loading, scroll effects | `references/rules/motion.md` |
| Icons, photos, illustrations, image prompts | `references/rules/imagery-and-icons.md` |
| Checking your work | `references/rules/review-checklist.md` |
| Product UI | `references/guides/web-app.md` |
| Marketing page | `references/guides/landing-page.md` |
| Phone app | `references/guides/mobile-app.md` |
| Dashboards and data tables | `references/guides/dashboard-and-tables.md` |
| Presentations | `references/guides/slides.md` |
| No brand direction given | `references/archetypes/README.md` |
