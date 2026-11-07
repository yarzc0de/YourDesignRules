# Landing page guide

This guide covers marketing pages whose job is to turn a visitor into a signup, a sale, or a booked call:
launch pages, campaign pages, single-product sites, and home pages that sell. It is not for product screens;
use `guides/web-app.md` for those. Read `rules/core.md` first. The hero composition is defined in
`rules/layout.md`, type sizes in `rules/typography.md`, contrast and accent use in `rules/color.md`, and image
choices in `rules/imagery-and-icons.md`. Sizes are px (pt on iOS, dp on Android).

## Goal and message

### LAND-1 · Choose one conversion goal before anything else
Decide the single action the page exists for: sign up, buy, book a demo, or join a waitlist. Every section
either moves the visitor toward that action or removes a reason not to take it. Cut sections, links, and
side offers that pull anywhere else.
- **Why:** a page that asks for three different actions tends to get none of them.
- **Check:** you can name the goal in a few words, and each section's job connects to it.

### LAND-2 · Write the words before choosing visuals
Draft the headline, subhead, section headings, proof, and CTA labels as plain text first, in narrative
order (LAND-9). Pick layout, imagery, and color only after that text makes the case on its own.
- **Why:** visuals chosen first end up decorating a message that does not exist yet.
- **Check:** the text-only draft, read top to bottom, persuades without any images.

### LAND-3 · Sell the change, not the tool
Describe the visitor after they adopt the product: what they stop worrying about, what they get back, who
they become. Features appear as the reason that change is believable, not as the headline.
- **Why:** visitors buy a better version of their own situation, not a list of parts.
- **Check:** the hero and section headings mention the visitor's result more often than product features.

### LAND-4 · Climb the headline ladder
Write the headline on the highest rung your real facts can support. Example for Rafterly, a fictional app
that turns spoken notes into home inspection reports:

| Rung (strongest first) | What it says | Example |
|---|---|---|
| Transformation | Who the visitor becomes | "Be the inspector who is home for dinner" |
| Outcome | The result they get | "Hand over the report before you leave the driveway" |
| Benefit | The measurable gain | "Finish reports in half the time" (only with a real, measured figure) |
| Feature | What the product does | "Voice-to-report transcription" |

Feature copy belongs in subheads and section detail. Draft two or three headlines on the top rung and keep
the clearest one.
- **Why:** the top rungs speak to the visitor's goal; the bottom rung makes them work out why it matters.
- **Check:** the hero headline sits on one of the top two rungs, and any number in it comes from the brief.

## The hero

### LAND-5 · Make the hero carry the whole pitch
The opening view answers three questions: what this is, why it matters to the visitor, and the next step.
Keep it to a single idea: one headline of about 12 words or fewer, one supporting sentence that fits on two lines, and
one primary CTA. All of it is visible without scrolling at 1280×720 and at 375×667.
- **Why:** many visitors decide from the first screen and never scroll.
- **Check:** show only the first screen to someone new; they can say what it is and what to click.

### LAND-6 · Compose the hero as one continuous stage
The dominant image and the main statement form a single composition. Pick one of three structures (full
rule in `rules/layout.md`):

| Option | Composition | Where the type goes |
|---|---|---|
| Wide photograph | A full-width scene, shot or cropped so one region stays calm | In that calm region: sky, wall, shade, soft focus |
| Oversized object | One cut-out product or object, large enough to dominate, on a plain or gradient field | On the open field beside or across the object |
| Illustrated scene | A drawn scene planned with the statement as one of its parts | Inside the scene, placed from the first sketch |

- Type can overlap the image or occupy a planned band above it; either way the image stays strongest.
- Make room for text with crop, negative space, lighting, or a soft continuous tonal fade. Never put a
  visible dark panel behind the copy.
- On narrow screens, recrop and recompose the scene; do not scale the desktop hero down.
- This applies to the page opening only, not to later sections or to app screens.
- **Why:** a split hero reads as two weak halves; one stage reads as one confident idea.
- **Check:** the image is the largest element, and no frame, card, or column edge cuts it off from the type.

**Avoid:** a text column on the left and a boxed photo or product card floating on the right.
**Do:** one photograph across the full width, with the headline set into its quiet sky.

### LAND-7 · Show the outcome in the imagery
Picture the visitor's future: people in the improved situation, the finished result, the place they get to.
Use real product UI only when the product itself is the argument, and then show it doing real work. A lone
screenshot floating on a gradient is the weakest choice. Keep text over images legible with crop and a
localized tonal gradient (`rules/color.md`); never stretch or distort an image (`rules/imagery-and-icons.md`).
- **Why:** visitors can picture themselves in a scene; they cannot picture themselves in a screenshot.
- **Check:** each major image shows a person, place, or result after adoption, or real UI doing a real task.

### LAND-8 · Make the primary CTA the most prominent element
The CTA button carries the accent at full strength, and the accent appears nowhere else as decoration. Label
it with a verb and an object ("Start free trial", "Book a demo"), never "Submit" or "Click here". A secondary
option, if any, is a quiet text link. Button text passes 4.5:1 and the button edge 3:1 against its ground.
- **Why:** the eye should reach the action without searching for it.
- **Check:** in a blurred screenshot of the hero, the CTA is the first colored shape you notice (CHK-5).

## Narrative and rhythm

### LAND-9 · Order sections as promise, proof, action
The page answers four questions in turn: what the product is, why it works, why to trust it, what to do
now. Treat the order below as a default; adapt it to the content and drop any section you cannot fill with
true material (CORE-12).

| Section | Job | What proves it |
|---|---|---|
| Hero | State the change and the next step | Outcome image, headline, CTA |
| Problem | Name the visitor's current situation in their words | A specific scene or task, not generic statistics |
| How it works | Show the path in three or four steps | Real product views or step visuals |
| Outcomes | Tie the key capabilities to results | Before and after, named results, real product detail |
| Proof | Give reasons to trust | Quotes with name and role, permitted logos, measured results |
| Objections | Remove the last reasons to wait | Pricing, terms, FAQ, guarantees, security notes |
| Final CTA | Ask again | The same label and destination as the hero CTA |
| Footer | Help visitors who need more | Contact, legal, a few key links |

- **Why:** visitors need to understand before they believe, and believe before they act.
- **Check:** read the section headings alone; they tell the promise, proof, action story in order.

### LAND-10 · Alternate density from section to section
Follow a text-heavy section with a visual one and a dense one with a calm one; never stack two sections of
the same density. Dark bands suit proof and single bold statements; light bands suit explanation and detail. Give sections 96–160 of vertical padding on desktop and 64–96 on mobile. Whitespace
paces the reading; it must not pad out a page that has little to say.
- **Why:** a uniform page gives the reader no sense of progress.
- **Check:** no two consecutive sections share density or layout shape (CHK-13, CORE-8).

### LAND-11 · Keep one axis per section and group tightly
Center a section or left-align it, never both. Keep items within a group close (8–16) and separate groups
and sections generously (48 and up). The heading, text, and CTA for one idea sit together.
- **Why:** proximity shows what belongs together faster than borders do.
- **Check:** every text block in a section starts on one shared line or centers on one axis (CHK-4).

### LAND-12 · Meet the type minimums
Sizes follow the scale in `rules/typography.md`:

| Role | Desktop | Mobile |
|---|---|---|
| Hero headline | 48–96 | 36–48 |
| Section heading | 30–48 | 24–32 |
| Body | 16–20 | 16–17 |
| Captions, legal, footer | 12–14 | 12–14 |

- Set body copy at 16 or larger. Short supporting text may drop to 14, never lower; 12–13 is for captions
  and legal lines only.
- Adjacent levels differ by a ratio of at least 1.2.
- Center no more than two or three lines; left-align anything longer.
- Keep body lines between 50 and 75 characters.
- Break headlines by hand at natural phrases; no single-word last lines.
- **Why:** a page that is tiring to read cannot persuade anyone.
- **Check:** measure rendered body size and line length on desktop and at 375 (CHK-6).

## Proof

### LAND-13 · Show only real, specific proof
Proof is concrete and traceable: a named result in the form "[customer] cut [task] from [before] to
[after]", a real quote with name, role, and company, a logo the user supplied. Never invent logos, quotes,
ratings, or user counts (CORE-9). With no real proof yet, leave the section out, or fill the slot with an
obvious bracketed sample such as "[Customer quote]". Name every such slot in your reply (CORE-20).
- **Why:** one specific result convinces more than a wall of vague praise, and fake proof is a liability.
- **Check:** every quote, logo, and number traces to the brief or is a visible placeholder (CHK-10).

## Navigation and footer

### LAND-14 · Keep the navigation restrained
Logo on the left, three to five text links, and one CTA button on the right with the same label as the hero
CTA. Keep the bar 64–80 tall. No mega-menus or dropdown trees on a landing page. On mobile, keep the logo
and the CTA visible and move the links into a menu.
- **Why:** every extra link is an exit from the conversion path.
- **Check:** the nav holds at most five links plus one button.

### LAND-15 · Repeat the primary CTA in the closing section
Close with a short section that restates the promise in one line and repeats the CTA with the same label and
destination. On long pages, one extra repeat right after the proof section is fine.
- **Why:** a visitor convinced at the bottom of the page should not have to scroll back up.
- **Check:** the last section before the footer contains the primary CTA.

### LAND-16 · Keep the footer quiet and organized
Use two to four labeled link groups (for example product, company, legal), contact details, copyright, and
social links if supplied. Set it at 12–14 in muted text that still passes 4.5:1. It is not a second sitemap
listing every page, and it makes no new pitch.
- **Why:** a loud footer competes with the final CTA directly above it.
- **Check:** the footer is visibly quieter than the final CTA section and has no more than four groups.

### LAND-17 · Put the audience in the pitch, not in a strip of boxes
Never follow the hero with a band of equal cells naming who the product is for, or with a trio of equal
"how it works" boxes. Name the audience in the headline or subhead, show them in the imagery, and explain the
mechanism with one visual (a timeline, a diagram, the real product view) instead of three captioned boxes.
See CORE-21 for the general rule and the narrow exceptions.
- **Why:** the strip pushes the proof further down and tells the visitor nothing the hero couldn't.
- **Check:** the section after the hero contains new information, not a boxed restatement of the audience
  or features.

## Before you hand off

Run `rules/review-checklist.md` after each section and on the whole page; for landing pages, stress these:

| Check | What to confirm on a landing page |
|---|---|
| CHK-3 | Headline and CTA pass contrast on the actual image or gradient behind them |
| CHK-5 | The primary CTA is the most prominent interactive element in every view |
| CHK-7 | Images arrived, are cropped for each breakpoint, and keep a quiet zone under text |
| CHK-10 | Every proof point is real or a visible placeholder listed in your reply |
| CHK-13 | Section density and shape alternate down the page |
