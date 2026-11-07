# Layout

How to place, group, size, and space elements: the spacing scale, screen structure, sizing and flow, the
website hero, responsive behavior, and rhythm. Read this file before you build any screen or section, and
return to it whenever a layout looks crowded, loose, or unplanned. Text sizes and line length live in
references/rules/typography.md; color, contrast, and shadows live in references/rules/color.md. Numbers are CSS pixels (points on
iOS, dp on Android).

## Alignment and grouping

### LAY-1 · Hold each section to one alignment axis
Choose left-aligned or centered for the whole section and give every block in it the same treatment. A
centered title over a left-aligned paragraph and a left-aligned button pulls one section in two directions.
- **Why:** a single axis gives the eye one place to start each line; mixed axes look accidental.
- **Check:** one vertical line per section touches the start of every block, or runs through the middle of each.

### LAY-2 · Show relationships with proximity
Keep the space inside a group at about half, or less, of the space between groups. A label sits 4–8 from
its input, the input sits 16 from the next field, and the whole form sits 24–32 from the next section.
- **Why:** distance is the first grouping cue people read, before borders or color.
- **Check:** squint at the render; groups still separate with every line and box mentally removed.

### LAY-3 · Align everything to an implicit grid
Place blocks on shared column edges even when no grid is drawn. Inside a container, every child starts at
the same inset. No element floats at an offset that nothing else on the screen shares.
- **Why:** shared edges make a layout read as one deliberate system instead of loose parts.
- **Check:** every left edge on the screen lines up with at least one other edge.

## Spacing

### LAY-4 · Use one 4-point spacing scale
Take every margin, padding, and gap from this scale. Never type a value that falls between two steps.

| px | Tailwind | Typical use |
|---|---|---|
| 4 | `1` | icon to its text, label to its hint |
| 8 | `2` | label to field, tight button group |
| 12 | `3` | button group, list item internals |
| 16 | `4` | stacked fields, item grid gap, mobile page padding |
| 24 | `6` | panel padding, gap between app sections |
| 32 | `8` | gap between app sections, desktop page padding |
| 48 | `12` | major blocks inside a marketing section |
| 64 | `16` | marketing section padding on mobile |
| 96 | `24` | marketing section padding on desktop |
| 128 | `32` | generous marketing section padding |

Three bounded exceptions: 10 (`2.5`) inside controls so a button or nav item lands on its target height; 20
(`5`) for mobile page padding; steps of 32 above 128, such as 160 (`40`), for marketing section padding.
Gaps between siblings never use 10 or 20.
- **Why:** a closed scale keeps spacing consistent across screens and blocks one-off values.
- **Check:** every spacing value in the code appears in the table or in the exception list.

### LAY-5 · Start product UI from the spacing reference
Desktop defaults for product screens at medium density. Adjust inside a range, never outside it; compact
and airy screens shift these values as LAY-7 shows.

| Situation | Value |
|---|---|
| Gap between the sections of one screen | 24–32 |
| Gap in a grid of cards or tiles | 16–24 |
| Gap between fields stacked vertically | 16 |
| Gap between fields side by side | 16 |
| Gap between buttons in a group | 8–12 |
| Inner padding of a panel or card | 24 |
| Button padding, vertical × horizontal | about 10 × 16 |
| Input padding, vertical × horizontal | about 8 × 16 |
| Input height (buttons beside inputs match it) | 36–44 |
| Horizontal page padding | 16–20 on mobile, 24–32 on desktop |
| Sidebar width | 240–280 |
| Sidebar nav item padding, vertical × horizontal | about 10–12 × 12–16, items touching with no gap |

- **Why:** tested defaults remove guesswork and keep screens consistent with each other.
- **Check:** measure five gaps on the screen; each one falls inside the range of its row.

### LAY-6 · Pad marketing sections generously
On marketing pages, give each section 96–160 of vertical padding on desktop and 64–96 on mobile. Sections of
equal weight share one value; a section set apart on purpose may take more.
- **Why:** a marketing page is read one idea at a time, and the space between ideas paces the scroll.
- **Check:** section padding is at least 96 at 1440 wide and at least 64 at 375 wide.

### LAY-7 · Choose one density mode per screen
Pick the mode from the content and apply it to the whole screen.

| Mode | Use for | Item gap | Panel padding | Control height | Table row |
|---|---|---|---|---|---|
| Compact | data-heavy tools, tables, consoles | 8–12 | 16 | 32–36 | 36–40 |
| Medium (default) | most product screens | 16–24 | 24 | 36–40 | 44–52 |
| Airy | low-complexity flows, onboarding, short settings | 24–32 | 32–48 | 44 | 52+ |

Compact controls are for pointer input only; touch screens keep targets at 44 or more (see
references/guides/mobile-app.md).
- **Why:** one density gives a screen one rhythm; mixed density looks like two products joined together.
- **Check:** every gap and padding on the screen comes from a single row of this table.

## Structure

### LAY-8 · Give each screen one dominant axis
Decide whether the screen reads mainly top to bottom (feed, form, article) or side to side (list beside
detail, navigation beside a canvas), and arrange everything else to follow that direction.
- **Why:** one main direction tells people where to look next.
- **Check:** you can describe the reading path of the screen in one sentence.

### LAY-9 · Use two structural zones before adding a third
Start with two regions, such as navigation and content, or list and detail. Add a third region, like an
inspector or a context panel, only when the task needs it visible all the time.
- **Why:** every extra zone splits attention and narrows the space left for the main work.
- **Check:** removing the third zone would break a task, not just tidy the screen.

### LAY-10 · Avoid nested scroll containers
Let the page, or one main region, scroll. Never put a scrolling panel inside another scrolling panel. Sticky
headers and a fixed sidebar are fine.
- **Why:** nested scrolling traps wheel and touch gestures and hides content in unexpected places.
- **Check:** at any point on the screen, one scroll gesture moves exactly one region.

### LAY-11 · Separate with whitespace before drawing lines
Reach first for a larger gap, then for a tonal shift between surfaces, and only then for a 1 px divider. A
divider needs a job: splitting rows in a dense list, marking the edge of a sticky header, or dividing a
toolbar.
- **Why:** each line adds visual noise, while space separates without adding any.
- **Check:** removing any remaining divider would make the grouping harder to read.

### LAY-12 · Pick a skeleton that fits the task
Common screen skeletons:

| Skeleton | Dimensions | Fits |
|---|---|---|
| Sidebar + main | sidebar 240–280, main fluid | many top-level destinations, persistent navigation |
| Top bar + content | bar 56–64 tall, content below | few destinations, content-first tools and sites |
| Main + side column | main fluid, side fixed at 320–360 | detail with inspector, document with comments |
| Item grid | columns derived from a minimum item width | browsing collections: files, products, media |

Do not reach for a sidebar or a dashboard by habit; use one only when navigation depth or the workflow
calls for it.
- **Why:** a skeleton chosen from habit forces the content into the wrong shape.
- **Check:** you can name the task need that justifies every zone in the skeleton.

### LAY-13 · Cap the page content width
Hold page content inside a centered container with a maximum width of 1200–1440, and let backgrounds run
full width. Paragraph length inside it is set by TYPE-10 in references/rules/typography.md, not by this cap.
`max-width: 1280px; margin-inline: auto;` (Tailwind `max-w-7xl mx-auto`)
- **Why:** unbounded content on wide monitors pushes related items too far apart.
- **Check:** at 1920 wide, content stops at the cap and only the outer margins grow.

## Sizing and flow

### LAY-14 · Let content size its containers
Build with flex or grid and `gap`, and let width and height come from the content and the parent. Fix a
size only where the design demands it: icons, avatars, media aspect ratios, sidebar width. Never estimate
the box size of a text element by hand.
- **Why:** hard-coded sizes repeat what layout already computes and break when content changes.
- **Check:** lengthen a label by 50%; its container grows and nothing nearby breaks.

### LAY-15 · Treat clipping and overflow as bugs
Every container grows to fit what it holds. Long strings wrap, or truncate with an ellipsis and expose the
full text on hover or focus. Nothing spills past its parent or slides under a sibling. Give flex children
that hold text `min-width: 0` so truncation works.
- **Why:** clipped content is lost information, and overflow reads as a broken product.
- **Check:** at 375, 768, and 1440, no content extends beyond its parent's box.

### LAY-16 · Space siblings with gap
Set the space between siblings with the parent's `gap`. Do not insert empty spacer elements, and do not put
margins on every child.
**Do:** `display: flex; flex-direction: column; gap: 16px;` (Tailwind `flex flex-col gap-4`)
**Avoid:** an empty `<div class="h-4">` between items, or `margin-top` repeated on each child.
In SwiftUI, the same idea is `VStack(spacing: 16)` instead of fixed-height spacer views.
- **Why:** one gap value on the parent keeps spacing consistent and editable in one place.
- **Check:** no element exists only to create space.

### LAY-17 · Apply horizontal page padding once
Put the page's left and right padding on one content wrapper. Sections inside inherit it instead of adding
their own. A section with a full-bleed background places the background outside the wrapper and its content
inside.
- **Why:** per-section padding drifts, and section edges stop lining up.
- **Check:** the content of every section starts at the same x position.

### LAY-18 · Use absolute positioning only for overlays
Allowed: overlays (menus, popovers, dialogs, toasts), badges pinned to a corner, and intentional overlaps in
display compositions. Never place chart labels, table cells, or list items by coordinates; leave their
alignment to the layout engine or the charting library (see references/guides/dashboard-and-tables.md).
- **Why:** absolutely placed content ignores its neighbors and breaks when the data or the width changes.
- **Check:** resize the viewport; no positioned element drifts away from what it labels.

### LAY-19 · Keep overlaps and crops readable
Display elements may overlap one another or run off an edge, but text never loses part of a word, and the
order of reading stays obvious. Body copy, controls, and data are never overlapped or cropped.
- **Why:** a cut word or an unclear order turns a style choice into a reading error.
- **Check:** every word in an overlap reads whole, and two people read the blocks in the same order.

## Website hero

These rules cover the opening of a website and nothing else. App working surfaces and later page sections
follow the rest of this file.

### LAY-20 · Compose the hero as one continuous stage
Build the opening as a single scene where a commanding image and the main statement work together. Avoid
the split where copy fills one column and a boxed photo or product card fills the other.
- **Why:** a split opening reads as two weak halves instead of one strong first impression.
- **Check:** the image and the headline share one ground, with no box edge between them.

### LAY-21 · Choose one of three hero compositions
- **Wide photograph** that leaves a calm region in the picture for the type.
- **Oversized cut-out object** set against a flat color or a gradient.
- **Illustrated scene** with the statement built into it.

The headline can cross over the image or occupy a planned strip of space above it. Either way, the image
remains the largest and most commanding element.
- **Why:** each of these keeps image and statement inside one composition.
- **Check:** the image covers more area than any other element in the hero.

### LAY-22 · Make room for type without a visible box
Clear space for the headline through the way the shot is framed, empty areas in the picture, the lighting,
or a gradual tonal fade with no edge. Never place a visible dark rectangle or panel behind the copy.
Contrast must still pass (see references/rules/color.md).
- **Why:** a box behind the text announces that the image was never composed for it.
- **Check:** no shape with a visible edge sits between the headline and the image.

### LAY-23 · Keep hero navigation quiet and the action obvious
Navigation holds the logo, a few links, and one call to action. The primary action is the clearest
interactive element in the hero; everything else that can be clicked stays visually lighter.
- **Why:** the opening has one job, and competing controls dilute it.
- **Check:** a first-time viewer can point to the primary action within two seconds.

### LAY-24 · Recompose the hero for narrow screens
On phones, re-crop the image around its subject and rearrange the type and image for a tall, narrow format.
Do not scale the desktop composition down.
- **Why:** a shrunken desktop hero turns both the subject and the headline into thumbnails.
- **Check:** at 375 wide, the subject fills the crop and the headline sits in clear space.

## Responsive

### LAY-25 · Preserve the hierarchy at every breakpoint
The element that dominates on desktop still dominates on a phone, and the primary action stays in view.
Rearrange regions as width changes; do not demote or hide the main one.
- **Why:** if the order of importance changes with width, the screen means different things on each device.
- **Check:** at each breakpoint, the same element is the first thing you notice.

### LAY-26 · Adapt the structure to each device class

| Class | Width | Structure |
|---|---|---|
| Mobile | up to 767 | a single main column; side panels turn into sheets or stack below the main content |
| Tablet | 768–1279 | transitional; keep the main column, move side panels into drawers or below |
| Desktop | 1280 and up | several zones and higher density are fine |

On mobile, nothing scrolls sideways except content that needs it, such as a wide data table.
- **Why:** each class has different space and input, so the structure has to change, not just scale.
- **Check:** at 375 wide, there is no horizontal scroll outside data tables.

### LAY-27 · Test at 375, 768, and 1280 or 1440
Render and look at each width before calling a layout done, then drag through the widths in between.
- **Why:** layouts tend to break between the sizes they were designed for.
- **Check:** renders at 375, 768, and 1440 (or 1280) show no overlap, clipping, or horizontal scrollbar.

## Rhythm

### LAY-28 · Alternate rich and quiet regions
Follow a dense or image-heavy region with a calmer one. Two dense regions in a row blur together; two
sparse ones in a row feel unfinished.
- **Why:** changes in density pace reading and mark where one idea ends and the next begins.
- **Check:** label each section rich or quiet; no two neighboring sections are both rich.

### LAY-29 · Do not stretch thin content with whitespace
Whitespace paces content; it does not fill a page with little to say. If a section holds one sentence, make
the section smaller, merge it into a neighbor, or cut it, rather than padding it to fill the viewport.
- **Why:** inflated space around thin content reads as empty, not calm.
- **Check:** no section is mostly blank because its padding was raised to fill the screen.
