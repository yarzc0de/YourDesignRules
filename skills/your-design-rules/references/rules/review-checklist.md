# Review checklist

Run this checklist after **every section** you build (hero, feature block, table, form, sidebar), then once
more on the whole screen. It is the verification loop required by CORE-15. Look at the actual render, at
its intended size, not at your code.

How to use it:
1. Render the section (browser screenshot, simulator, preview, or design tool view).
2. Walk the list top to bottom. Each item is pass/fail.
3. Fix failures in place (CORE-16), re-render, and re-check only the failed items.
4. Move on to the next section only when every item passes or the user accepted the exception.

## Per-section checks

### CHK-1 · Structure is intact
No collapsed containers (zero width or height), no elements stacked on top of each other by accident, no
layout that only works at one exact width.

### CHK-2 · Nothing is clipped or overflowing
All text is fully visible; no words cut by a container edge; no unintended horizontal scroll; containers
grow to fit their content. Long strings (names, emails, numbers) were tested with realistic lengths.

### CHK-3 · Contrast passes on the real pixels
Body text ≥ 4.5:1, large text and UI boundaries/icons ≥ 3:1, measured against what is actually behind
them: photo, gradient, glass. See `references/rules/color.md`.

### CHK-4 · Alignment and spacing are on the system
One alignment axis per section. Shared edges line up. Every gap and padding value comes from the spacing
scale in `references/rules/layout.md`. Related items are closer to each other than to unrelated ones.

### CHK-5 · There is one focal point and one obvious primary action
Squint: one element dominates. The primary action is findable in under two seconds and is the most prominent
interactive element. The accent color is not spread across decoration.

### CHK-6 · Type renders as intended
The intended fonts loaded (no system fallback), weights and italics are real, body size and line length are
within `references/rules/typography.md`, headlines break at deliberate points with no single-word last lines.

### CHK-7 · Images and icons are right
Images arrived (no empty frames or pending placeholders), are not stretched, have a sensible crop with a
quiet area under any text, and have alt text. Icons come from one library at consistent sizes. See
`references/rules/imagery-and-icons.md`.

### CHK-8 · Effects and containers are justified
No card wrapping without a job (CORE-6). No rows of equal label-plus-caption boxes (CORE-21) and no
unexplained generated-page kit items (CORE-22). Shadows are soft and diffuse, never hard or offset. No
beige, cream, ivory, or tan grounds. Each gradient or blur has a reason (CORE-7).

### CHK-9 · States exist where data or actions exist
Data surfaces show loading, empty, error, and success states (and permission states when relevant).
Destructive actions have confirmation or undo. Interactive elements have hover, focus, active, and disabled
styles.

### CHK-10 · Content is honest
No invented metrics, logos, testimonials, or completed states. Samples are clearly labeled (CORE-9).

### CHK-11 · What rendered is what you meant
Compare the render with your intent for the section. If you meant "a dominant chart with a quiet filter bar"
and the filter bar is louder than the chart, the section fails even if every other item passes.

## Whole-screen checks

### CHK-12 · Hierarchy survives every breakpoint
Check at 375, 768, and 1440 px wide (or the target devices). Mobile is recomposed, not shrunk: one column,
readable sizes, tap targets ≥ 44 px, no horizontal scroll except intentional data tables.

### CHK-13 · The page has rhythm, not repetition
Sections vary in density and shape (CORE-8). No three consecutive sections share the same layout.

### CHK-14 · Reduction pass is done
For every element ask what breaks if it disappears (CORE-4). Remove, merge, or quiet anything with no
answer, then re-render.

### CHK-15 · Keyboard and focus work
Every interactive element is reachable by keyboard in a logical order and shows a visible focus ring
(≥ 3:1 against its surroundings). Nothing important depends on hover alone.

### CHK-16 · Limitations are reported, not shown
Missing fonts, failed images, or assumed data are mentioned in your reply to the user, never inside the UI
(CORE-20).

### CHK-17 · Motion has a job and can be turned off
Every animation confirms, orients, keeps continuity, or flags a change (MOTION-1). Durations and easing come
from references/rules/motion.md, only transform and opacity animate, and with reduced motion enabled nothing slides or
scales. With JavaScript off, no content is stuck invisible. Capture a scroll filmstrip (a frame every
300–400 px) and confirm every frame is readable and the scroll story advances; in apps, click through state
changes and confirm none of them jumps (MOTION-27).

### CHK-18 · The page makes one bold decision
You can name the one memorable thing on the page (CORE-8) and the real-world source of at least two visual
choices (CORE-23). The page does not match a generator house style without a stated reason (CORE-25), and
none of the template chrome in CORE-22 appears without a job. On marketing pages, the first screen is
worth a screenshot on its own: a key visual or a product view strong enough that someone would share it
(LAND-18). In product UI, the working surface is the most crafted region on the screen (WEB-22 to
WEB-27).

## Copy-paste version

```
Section: ____________   Viewport: ______
[ ] CHK-1  structure intact
[ ] CHK-2  no clipping / overflow
[ ] CHK-3  contrast on real pixels
[ ] CHK-4  alignment + spacing scale
[ ] CHK-5  one focal point, obvious primary action
[ ] CHK-6  fonts loaded, sizes + measure ok
[ ] CHK-7  images arrived, cropped, alt text; icons consistent
[ ] CHK-8  no card-wrapping, soft shadows, no beige
[ ] CHK-9  states present
[ ] CHK-10 content honest
[ ] CHK-11 render matches intent
Whole screen:
[ ] CHK-12 375 / 768 / 1440
[ ] CHK-13 rhythm
[ ] CHK-14 reduction pass
[ ] CHK-15 keyboard + focus
[ ] CHK-16 limitations reported in reply
[ ] CHK-17 motion has a job, reduced motion works
[ ] CHK-18 one bold decision, drawn from the subject
```
