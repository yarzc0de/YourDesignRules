# Slides guide

Rules for presentation decks: pitches, keynotes, board updates, internal reviews, lectures. Read it after
`references/rules/core.md` whenever the output is a slide, in any format (HTML slides, a slide app, a 16:9 frame). All
sizes are px on a 1920 × 1080 canvas; scale them proportionally for other 16:9 sizes. The second half is a
layout library with its own IDs (prefix `S-`) so a plan can name the layout each slide uses. Check each slide
with `references/rules/review-checklist.md` (CHK-1 to CHK-11) at full size, then the whole deck.

## Priorities

### SLIDE-1 · Rank clarity, readability, hierarchy, then simplicity
When goals conflict, resolve them in this order: a clear message, text readable at a distance, a visible
order of importance, and only then minimalism. Every slide must work on a projector in a bright room, in a
shared video-call window, and on a phone.
- **Why:** slides are seen once, briefly, and often on poor screens.
- **Check:** at 50% size (960 × 540) the title and body still read, and the point lands within five seconds.

### SLIDE-2 · Adapt the brand for the room
Keep the brand's fonts, colors, and imagery, but set type larger and spacing looser than the brand uses on
web or print. If a brand color fails contrast as text, keep it for shapes, fields, and display type that
passes. When brand and readability conflict, readability wins.
- **Why:** brand systems are tuned for 16 px at arm's length, not for a wall twenty feet away.
- **Check:** every text and background pair meets the contrast in SLIDE-7.

### SLIDE-3 · Put one idea on each slide
A slide makes one point and supports the speaker; it is not a document. If the content will not fit at the
sizes in SLIDE-5, split it across two slides or cut it. Never shrink type to make room.
- **Why:** two ideas on one slide halve the attention each one gets.
- **Check:** you can state the slide's point in one sentence, and its title says it.

### SLIDE-4 · Reuse a few layouts instead of inventing new ones
Choose a small set of layouts from the library below and repeat them. Titles sit at the same position and
size on every content slide; margins, grid, and footer never move. Save novelty for the opening, the closing,
and the one or two slides that need extra emphasis.
- **Why:** a steady structure lets the audience read content instead of relearning the layout.
- **Check:** flip quickly through the deck; titles do not jump.

## Type

### SLIDE-5 · Meet the type minimums
Use at most two families. Build hierarchy with size and weight; reserve all caps for short labels.

| Role | Size | Minimum | Line height |
|---|---|---|---|
| Cover and statement titles | 80–144 | 72 | 1.0–1.1 |
| Slide title | 48–64 | 40 | 1.1–1.2 |
| Body and list items | 28–32 | 24 | 1.3–1.4 |
| Key numbers | 120–360 | twice the slide title | 0.95–1.05 |
| Labels and captions | 22–24 | 20 | 1.2–1.3 |
| Sources and footers (non-essential only) | 18–20 | 18 | 1.2 |

Keep body lines under about 60 characters. Font rules in `references/rules/typography.md` still apply.
- **Why:** text below these sizes disappears on projectors and shared screens.
- **Check:** no text on any slide is smaller than its role's minimum.

## Canvas and color

### SLIDE-6 · Lay out every slide on one 1920 × 1080 grid
Use a 16:9 canvas and keep all content at least 100 from every edge. Default margins are 120 left and right
and 100 top and bottom, leaving a 1680 × 880 content area (x 120–1800, y 100–980) split into 12 columns of
about 103 with 40 gutters. On content slides the title zone runs from y 100 to 240 and content starts at
y 280 or below. Only full-bleed images and background fields cross the margins.
- **Why:** one fixed grid gives every slide the same skeleton and keeps text clear of projector cropping.
- **Check:** draw the margin box; no text or icon crosses it.

### SLIDE-7 · Use 2–3 core colors and keep body text neutral
Pick 2–3 core colors plus neutrals. Body text is a neutral with high contrast: aim for 7:1 and never go below
4.5:1 (`references/rules/color.md`). Spend the accent only on emphasis: the highlighted number, the key bar, the one
phrase that matters. Use a colorblind-safe chart palette and pair every color meaning with a label.
- **Why:** projectors wash out contrast, and an accent used everywhere marks nothing.
- **Check:** each slide has one accent focus, and body text meets 4.5:1 on the real background.

## Visuals and data

### SLIDE-8 · Make every visual carry meaning
Use images, icons, and diagrams only when they explain or prove something. Prefer specific visuals (the
product, a real place, a diagram of the mechanism) over generic stock. Keep icons from one set at one size,
48–96 on slides, with one stroke weight. Source and prompt imagery per `references/rules/imagery-and-icons.md`.
- **Why:** decorative imagery takes attention from the point without adding to it.
- **Check:** for each visual, you can say what the audience learns from it.

### SLIDE-9 · Show data as a chart with one highlighted insight
Turn numbers into a chart whenever their shape matters, and choose the type with DATA-4. The title states
the insight, the one series or bar that proves it carries the accent, and everything else stays neutral.
Label values directly at 20 or larger (24 preferred) and drop the legend when labels fit. Plot only supplied
data (CORE-9).
- **Why:** an audience reads a highlighted chart in seconds and a table of figures barely at all.
- **Check:** the title states the finding, and the highlighted mark shows it.

## Density and context

### SLIDE-10 · Write phrases, not paragraphs
Body text is short phrases: about 30 words per slide outside the title, 50 at most. The title is a sentence
that states the takeaway ("Onboarding changes cut support tickets by a third"), not a topic label
("Support"). Detail, sources, and caveats go into speaker notes or an appendix.
- **Why:** people cannot read a paragraph and listen to the speaker at the same time.
- **Check:** reading only the slide titles in order tells the whole story.

### SLIDE-11 · Match the deck to its context
| Context | Density | Visual approach |
|---|---|---|
| Corporate or board | medium; structured sections and a clear agenda | charts and simple tables, restrained color |
| Startup pitch | low; one claim per slide | bold statements, large numbers, the product in use |
| Marketing or sales | low to medium; titles framed as customer benefits | customer outcomes and real product shots |
| Internal review or working session | medium to high; more detail allowed | charts, lists, tables; little imagery |
| Keynote or talk | very low; a few words per slide | full-bleed images, statements, single numbers |

The densest context still honors SLIDE-5.
- **Why:** the same content needs different amounts of text when read alone versus spoken over.
- **Check:** the deck's typical slide matches the density of the row you picked.

## Opening, closing, and text-only slides

### SLIDE-12 · Open and close with a statement, not information
The cover and the closing slide set the tone: one strong visual and a few weighty words. Do not open on an
agenda, and do not close on a slide that only says "Thank you" or "Questions?". End on the one thing the
audience should remember or do, with contact details as a secondary line.
- **Why:** the first and last slides are the ones people remember.
- **Check:** the closing slide makes its point even if the speaker says nothing.

### SLIDE-13 · Let type carry text-only slides
When a slide has no image, the type is the visual: 80–144 in size, placed asymmetrically on the grid, with
an unexpected alignment or one word in the accent. Unusual is welcome; unreadable is not, so keep whole
words, a clear reading order, and the contrast minimum.
- **Why:** a small centered sentence on an empty slide looks unfinished.
- **Check:** the text block spans at least half the content width and reads in one pass.

## Layout library

The library uses the grid from SLIDE-6: content area 1680 × 880, 12 columns of about 103 with 40 gutters.
Common spans are 4 columns ≈ 533, 6 ≈ 820, 8 ≈ 1107, and 10 ≈ 1393. All sizes are px on 1920 × 1080.

### SLIDE-14 · Name a library layout for every slide
Plan the deck as a list of slides that each cite one layout ID ("4: S-NUMBERS"). Change the content, not the
skeleton. If no layout fits, the slide most likely holds two ideas (SLIDE-3); a new layout must still use the
SLIDE-6 grid and the SLIDE-5 sizes.
- **Why:** named layouts keep the deck consistent and make review concrete.
- **Check:** every slide in the plan maps to exactly one S- ID.

#### Frame: open, divide, close

**S-COVER · Cover**
- Grid: title block in columns 1–8 in the lower third, ending near y 840; presenter line on the bottom
  margin; logo at the top-left margin, 40–56 tall; behind it a full-bleed image or a solid brand field.
- Sizes: title 96–144 on 1–2 lines; subtitle 32–40; presenter, date, and event 24.
- Rules: no more than 12 words above the presenter line. An image keeps a quiet area under the title (CHK-3).

**S-SECTION · Section divider**
- Grid: section label and title in columns 1–8, at the same spot on every divider; an optional oversized
  numeral in columns 9–12 acts as the visual.
- Sizes: label 28–40; title 80–120; numeral 240–400.
- Rules: dividers share layout and colors, changing only number and words; a ground change marks the break.

**S-CLOSE · Closing**
- Grid: the final statement in the cover position (columns 1–8, lower third), or centered when it is 1–2
  lines; the next-step or contact line sits 48–64 below.
- Sizes: statement 80–128; next step or contact 28–36.
- Rules: state the takeaway or the requested action; "Thank you" is at most a secondary line. Reuse the
  cover's visual language so the deck feels closed.

#### Statements

**S-STATEMENT · Single statement**
- Grid: one text block spanning 8–10 columns, starting at column 1 or column 3 for asymmetry; vertically
  centered or top-aligned between y 200 and 320.
- Sizes: 72–120, line height 1.05–1.15, 15 words or fewer.
- Rules: one sentence and no supporting body text. Emphasize 1–3 words at most, with weight or the accent.

**S-QUOTE · Quote**
- Grid: quote text in columns 2–10; attribution 32–48 below, aligned to the quote's left edge; an optional
  oversized quotation mark (200–320, accent tint) hangs in column 1.
- Sizes: quote 56–80, 30 words or fewer; name 28–32 at weight 600; role and company 24.
- Rules: only real, attributable quotes (CORE-9). Shorten the quote rather than shrinking it.

#### Image and idea

**S-SPLIT-L · Concept, image on the left**
- Grid: image bleeds off the left edge at x 0–960 (or 0–1120 for a wider split), full height; text sits on
  the right, 80–120 from the image edge and 120 from the right edge, vertically centered.
- Sizes: title 56–72; body 28–32 as up to 3 lines or 3 short items; label 20–24.
- Rules: the image shows the concept literally, cropped so the subject faces the text; no frame or shadow.

**S-SPLIT-R · Concept, image on the right**
- Grid: mirror of S-SPLIT-L; text from the left margin to 80–120 before the image, image at x 960–1920.
- Sizes: title 56–72; body 28–32 as up to 3 lines or 3 short items; label 20–24.
- Rules: alternate L and R on consecutive concept slides, keeping text sizes and vertical position identical.

**S-BLEED · Full-bleed image with overlay title**
- Grid: image covers all 1920 × 1080; title in the photo's quiet area, aligned to the margin box, usually
  lower left within columns 1–7.
- Sizes: title 72–120, 10 words or fewer; caption or credit 20–24.
- Rules: when the crop has no quiet area, add a soft localized gradient behind the text only, never a full
  dark overlay or a visible box (`references/rules/color.md`). Measure contrast on the composite.

#### Structure

**S-PILLARS · Three pillars**
- Grid: title zone, then three 4-column blocks (about 533 wide each), tops on one line at y ≥ 320.
- Sizes: icon or number 64–96; pillar heading 36–44; body 24–28, 12 words or fewer per pillar.
- Rules: exactly three items with parallel phrasing; four or more become S-LIST or two slides. Separate the
  blocks with space or thin rules, not three boxes (CORE-6).

**S-VERSUS · Comparison or before and after**
- Grid: two 6-column halves (about 820 each), split by the gutter plus a 1–2 px rule or a tonal shift on one
  side; headings on one baseline, then 3–4 paired rows aligned across the split.
- Sizes: side headings 40–56; row items 28–32; optional row labels 22–24.
- Rules: compare the same attributes in the same order on both sides. The "before" or alternative side stays
  neutral; the "after" or recommended side carries the accent.

**S-STEPS · Process steps**
- Grid: 3–5 steps in one row that shares the 1680 width equally, joined by a line or arrows, numbers on one
  baseline. Switch to a vertical stack in columns 1–8 when labels run past four words.
- Sizes: step number 48–72; step label 32–40; detail 24–28, 12 words or fewer.
- Rules: five steps at most; split longer processes with a progress marker. One reading direction only.

**S-MATRIX · 2×2 matrix**
- Grid: a square plot area 600–700 per side below the title zone, in columns 1–7 or centered; axis labels at
  both ends of each axis; an optional takeaway in columns 9–12.
- Sizes: axis labels 24–28; quadrant names 32–40; plotted item labels 22–24; takeaway 28–32.
- Rules: label each axis with what increases ("Cost: low to high"). Highlight the quadrant that matters and
  keep the other three neutral.

**S-LIST · Short list**
- Grid: title zone, then the list in columns 1–8, or two lists in 6-column halves; 24–40 between items.
- Sizes: item lead-in 32–40 at weight 600; optional detail 24–28 on the same or the next line.
- Rules: 3–5 items, one level only, no nested bullets. Each item fits on 1–2 lines.

#### Numbers and data

**S-NUMBER · Single big number**
- Grid: the number spans 40–70% of the content width, from the left margin or centered; the context line
  shares its left edge or baseline; the source sits on the bottom margin.
- Sizes: number 200–360, tabular, weight 600–800; unit 40–60% of the number; context 32–40; source 18–20.
- Rules: supplied data only (CORE-9), plus one line on what it means: period, comparison, or consequence.

**S-NUMBERS · Two or three numbers**
- Grid: two numbers in 6-column halves or three in 4-column thirds, on one baseline, labels in one row below.
- Sizes: numbers 120–200 in tabular figures; label 28–32; context 22–24.
- Rules: same format and precision across the set, with the accent on one number at most. Four or more
  numbers become S-CHART or an appendix table.

**S-CHART · Chart with insight**
- Grid: chart in columns 1–8 (about 1107 wide, 560–680 tall) with the insight text in columns 9–12; or a
  full-width chart under a title that states the insight.
- Sizes: title 48–60; insight text 28–32; axis and data labels 20–24; highlighted value 32–48; source 18–20.
- Rules: one highlighted series, the rest neutral, direct labels instead of a legend. Build it as a real
  chart, never an image (CORE-10).

## Which layout for which job

| Job | Layout | When it does not fit |
|---|---|---|
| Open the talk | S-COVER | S-BLEED with the title as the cover |
| Mark the start of a new part | S-SECTION | an S-STATEMENT naming the part |
| Make one claim land | S-STATEMENT | S-BLEED when a picture adds proof |
| Let a customer or expert speak | S-QUOTE | skip it if no real quote exists |
| Explain an idea with a picture | S-SPLIT-L or S-SPLIT-R | S-BLEED when the image is the idea |
| Set a scene or a mood | S-BLEED | S-SPLIT-L |
| Present three parallel ideas | S-PILLARS | S-LIST for four or five |
| Contrast two options or two states | S-VERSUS | S-SPLIT-L followed by S-SPLIT-R |
| Make one number memorable | S-NUMBER | S-STATEMENT built around the number |
| Show two or three headline numbers | S-NUMBERS | S-CHART for four or more |
| Show a trend or comparison in data | S-CHART | appendix table for exact values |
| Explain a sequence | S-STEPS | split across slides beyond five steps |
| Place options on two criteria | S-MATRIX | S-VERSUS when only one criterion matters |
| Agenda, recap, or requirements | S-LIST | S-PILLARS for exactly three |
| End the talk | S-CLOSE | S-STATEMENT with a contact line |

## When the brief is unclear

### SLIDE-15 · Ask ≤ 3 questions or state ≤ 5 assumptions
If the audience, purpose, length, brand, or data is unclear, either ask at most three focused questions
before building, or list at most five assumptions at the top of your reply and proceed. Ask first about
what changes the deck most: audience and context (SLIDE-11), the one message to remember, and which data
or brand assets exist.
- **Why:** a short check costs less than rebuilding a deck aimed at the wrong room.
- **Check:** your reply holds no more than three questions or five stated assumptions.
