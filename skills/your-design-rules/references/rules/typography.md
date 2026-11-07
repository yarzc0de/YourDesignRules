# Typography

How to choose typefaces, build a type scale, and set text so it reads well on product screens and websites
alike. Read this file when you pick fonts, define text tokens, or style any text, from a hero headline to a
table cell. Spacing between text blocks lives in references/rules/layout.md; text contrast lives in references/rules/color.md.
Sizes are CSS pixels (points on iOS, sp on Android).

## Families and roles

### TYPE-1 · Use two families at most, plus an optional mono
Assign each family to roles and keep it there. One family for everything is a valid choice.

| Role | Covers | Family |
|---|---|---|
| Display and headings | page titles, section heads, hero statements | heading family, or the body family |
| Body | paragraphs, descriptions, help text | body family |
| Captions and labels | field labels, metadata, badges, eyebrows | body family |
| Data | table numbers, code, IDs, timestamps | mono, or body family with tabular figures |

- **Why:** each extra family adds load time and dilutes a consistent voice.
- **Check:** the stylesheet loads at most two proportional families and at most one monospaced family.

### TYPE-2 · Keep expressive faces to display and short notes
Script, swash, pixel, ultra-condensed, and decorative serif faces belong in headlines, short display lines,
and brief annotations. Never set instructions, form labels, values, or controls in them.
- **Why:** decorative letterforms slow reading exactly where accuracy matters most.
- **Check:** every button, label, input, and number on the screen uses the body or data family.

### TYPE-3 · Pair decorative text with a readable version
When a message appears only as stylized display art (a script signature, a pixel logotype, outlined or
distorted lettering), repeat it in plain text nearby or in the element's accessible name.
- **Why:** people and screen readers must get the meaning without decoding the artwork.
- **Check:** hide the decorative text; the screen still says everything it needs to.

### TYPE-4 · Load every weight and style you set
Load a font file for each weight you use, true italics, and true small caps (or a dedicated small-caps
family). Never let the browser fake bold or italic; turn synthesis off so gaps show up:
`font-synthesis: none;`
- **Why:** faked bold smears and faked italic is only slanted roman; both look cheap.
- **Check:** every `font-weight` and `font-style` in the code maps to a loaded font file.

### TYPE-5 · Confirm the fonts loaded in the render
Judge type on the rendered screen, not in the code. A system fallback means the font failed to load, and
every size, width, and line break you checked is wrong. In a browser, read the rendered-font entry in the
inspector for headings, body, and data.
- **Why:** a design reviewed in a fallback font has never really been reviewed.
- **Check:** the inspector names the intended family as the rendered font for each text role.

## Scale and size

### TYPE-6 · Build the scale with clear jumps
Take sizes from one scale, and step between neighboring hierarchy levels by a ratio of at least 1.2, up to
about 1.333. Where two sizes in use sit closer than that (14 and 16), separate them by weight or color as
well. Most screens need five or six sizes, not the whole table.

| Size | Typical role |
|---|---|
| 12 | captions, badges, legal text |
| 14 | secondary text, dense UI labels, table cells |
| 16 | body text (web default) |
| 18 | lead paragraph, large body |
| 20 | card titles, small section titles |
| 24 | section headings |
| 30 | page titles in apps |
| 36 | page titles on websites |
| 48 | marketing headlines |
| 60 | display |
| 72 | large display |
| 96 | hero display |

- **Why:** small steps look like mistakes; clear steps read as intentional levels.
- **Check:** each heading level on the screen is at least 1.2 times the size of the level below it.

### TYPE-7 · Set body text at 16 px, never below 14

| Context | Size |
|---|---|
| Body text on the web | 16 by default |
| Body copy in any context | 14 at the smallest |
| Body text in mobile apps | 15–17 (iOS body style is 17, Android 16) |
| Captions and fine print | 12 at the smallest |

Set sizes in `rem` on the web so browser text settings apply (`1rem` is 16 px by default).
- **Why:** smaller body text strains reading and shuts out people with low vision.
- **Check:** no paragraph renders below 14 px and no caption below 12 px.

### TYPE-8 · Add weight before adding sizes
Before creating a new size, try a heavier weight at an existing one. Common weights: 400 for body text,
500–600 for labels and emphasis, 600–800 for headings.
- **Why:** weight builds hierarchy without multiplying sizes.
- **Check:** each family on the screen uses no more than three weights.

### TYPE-9 · Use one title style on every screen
Screen titles in an app share one size, weight, and family across every screen. Define the style once as a
token and reuse it.
- **Why:** a title that changes size from screen to screen makes the hierarchy unreliable.
- **Check:** every screen title resolves to the same text token.

## Measure, alignment, and line height

### TYPE-10 · Keep body lines to 50–75 characters, 35–50 on phones
Limit the width of paragraphs, not of the page. On screens 400 px wide or less, 16 px body text gives about
35–50 characters per line; that is correct there, so don't shrink the type to reach 50.
`max-width: 65ch;` (Tailwind `max-w-prose`)
- **Why:** long lines lose the reader at each return, and very short lines chop sentences apart.
- **Check:** a typical body line holds 50–75 characters at 1440 wide and 35–50 at 375.

### TYPE-11 · Center no more than three lines
Center a headline, a short subtitle, or a caption that runs 2–3 lines at most. Left-align anything longer.
- **Why:** centered text has a ragged starting edge, so the eye has to hunt for each new line.
- **Check:** no centered block wraps to a fourth line at any breakpoint.

### TYPE-12 · Match line height to the role
Write line height as a unitless value so it scales with the font size.

| Role | Line height | Example (size / line height) |
|---|---|---|
| Body copy | 1.45–1.6 | 16 / 24 |
| UI labels, buttons, table cells | 1.2–1.4 | 14 / 18 |
| Headings | 1.1–1.25 | 24 / 30 |
| Large display (48 and up) | 0.95–1.1 | 72 / 72 |

- **Why:** body text needs air to track across lines, while big type set loosely falls apart.
- **Check:** no heading uses body line height, and no paragraph is set tighter than 1.45.

### TYPE-13 · Tighten display type, open caps, leave body alone
- Large display text: −1% to −3% (`letter-spacing: -0.01em` to `-0.03em`).
- Short all-caps labels: +4% to +8% (`0.04em` to `0.08em`).
- Body text: the font's default spacing, always.
- **Why:** large letters look loose at default spacing, and capitals crowd each other without extra room.
- **Check:** no paragraph or body-size text carries a letter-spacing value.

## Case and line breaks

### TYPE-14 · Keep all caps rare and short
Use capitals only for tags and labels of a few words that carry information (a status, a category, a unit),
never for a sentence or a paragraph. An eyebrow label above a heading needs its own reason, such as a section
number in a real sequence or a category the reader filters by; never put one above every heading by habit
(CORE-22). Apply capitals with `text-transform: uppercase` so the source text keeps normal case. Archetypes
that mention uppercase labels follow this limit too.
- **Why:** capitals erase word shapes, and tracked caps everywhere are a template tell.
- **Check:** no all-caps text runs past about four words, and fewer than half the section headings carry an
  eyebrow.

### TYPE-15 · Break headlines on purpose
Break display lines at phrase boundaries, and never leave one word alone on the last line. Use
`text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs, then review each breakpoint.
- **Why:** a stranded last word or a break inside a phrase makes the headline read wrong.
- **Check:** at 375, 768, and 1440, no headline ends on a single-word line.

## Numbers and data

### TYPE-16 · Keep labels, values, and units together
Place each value's label and unit close enough to read as one group (see LAY-2 in references/rules/layout.md). Never
show a bare number whose meaning the reader has to guess.
- **Why:** a number without its label and unit leaves the reader guessing.
- **Check:** every number on the screen has a label, and a unit where one applies, inside its group.

### TYPE-17 · Make the unit quieter than the number
Set units, currency symbols, and suffixes smaller, lighter, or in the secondary text color so the number
leads.
**Do:** "42" at 30 px semibold, "ms" beside it at 14 px in the secondary color.
**Avoid:** a unit at the same size and weight as its value, or larger.
- **Why:** people scan for the value; the unit is context.
- **Check:** in every metric, the unit is visibly subordinate to its number.

### TYPE-18 · Use tabular figures for aligned and changing numbers
Turn on tabular figures for table columns, prices, timers, counters, and any value that updates live.
Right-align numeric columns (see references/guides/dashboard-and-tables.md).
`font-variant-numeric: tabular-nums;` (Tailwind `tabular-nums`)
- **Why:** proportional digits vary in width, so columns misalign and live values jitter.
- **Check:** a column of numbers lines up digit by digit, and a running timer does not shake.

## Room to grow

### TYPE-19 · Leave room for headline copy
Marketing headlines follow a copy ladder (see references/guides/landing-page.md). Size the container to the copy, not
the copy to the container: allow two to three lines at display size, and never fix a box around one draft.
- **Why:** copy changes after layout, and a box sized for one draft clips or crowds the next.
- **Check:** a headline 30% longer still fits without clipping or a size change.

### TYPE-20 · Respect the user's text size setting
Let text follow the platform setting: `rem` on the web, Dynamic Type text styles on iOS, sp units on
Android. In SwiftUI, use text styles such as `.font(.body)` rather than `.font(.system(size: 16))`.
- **Why:** many people enlarge text, and fixed sizes override their choice.
- **Check:** at the largest standard text setting, every text element scales and stays readable.

### TYPE-21 · Let containers grow when text grows
Do not fix the height of buttons, rows, cards, or headers that contain text; set padding and a
`min-height` instead. Let labels wrap to a second line rather than clip (see LAY-15 in references/rules/layout.md).
- **Why:** fixed heights clip text as soon as it is enlarged or the copy gets longer.
- **Check:** at 200% text size, no text is clipped or overlapping.
