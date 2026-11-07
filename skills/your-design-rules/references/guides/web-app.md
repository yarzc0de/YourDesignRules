# Web app guide

This guide covers functional product interfaces that people work in: consoles, editors, admin tools, queues,
settings, maps, and dashboards. It is not for marketing pages; use `guides/landing-page.md` for those. Read
it after `rules/core.md` and before you choose a layout. Spacing, type, and color values come from
`rules/layout.md`, `rules/typography.md`, and `rules/color.md`; sizes are px (pt on iOS, dp on Android).
Data-heavy screens also need `guides/dashboard-and-tables.md`.

## Infer the product first

### WEB-1 · Infer the product before choosing a layout
Answer these from the request, in order, before placing a single element:
1. Name the product type and the user's main job in one sentence (CORE-1).
2. Pick the dominant region: the thing the user looks at while doing that job (CORE-2).
3. Name the primary action for the screen, then for each section.
4. Choose one density mode: compact, medium, or airy (WEB-5).
5. Decide disclosure: what is always visible, what appears on selection, what lives in settings.
6. Only then pick a skeleton (WEB-4).

| Product type | Dominant region | Primary action | Density | Disclosure |
|---|---|---|---|---|
| Admin or settings | The form or list being edited | Save changes | Medium | Advanced options in collapsed groups |
| Queue or inbox | The list plus the selected item | Resolve or approve, then next | Compact | History on demand in a side column |
| Editor (doc, design, code) | The document or canvas | Edit in place; publish is secondary | Medium, quiet chrome | Tools appear for the current selection |
| Console or infra tool | Resource list or log stream | Create or deploy a resource | Compact | Configuration in a detail view |
| Map or spatial tool | The map | Search for or select a place | Minimal chrome | Details in a panel after selection |
| Monitoring dashboard | The metric or chart that answers the question | Investigate or filter by time | Compact to medium | Drill down from the chart |
| Checkout or setup wizard | The current step | Continue | Airy | One step at a time, summary aside |
| Catalog or library | The item grid or list | Open or add an item | Medium | Filters collapsed until needed |

- **Why:** the layout should follow from the job, not from the last app you built.
- **Check:** you can state the type, region, action, density, and disclosure before the first render.

### WEB-2 · Do not default to a sidebar, dashboard, or canvas
A sidebar earns its place with five or more destinations users switch between. A dashboard needs a
monitoring question; a canvas needs free-form spatial work. A settings page, a single-purpose tool, or a
three-step flow needs none of them.
- **Why:** borrowed scaffolding adds navigation and panels with nothing to hold.
- **Check:** every structural region on the screen maps to an answer from WEB-1.

## Structure

### WEB-3 · Organize working surfaces around the workflow
An editor, queue, map, console, or dashboard has to function as that tool, not as a page describing it. Arrange
four parts around the task: navigation (where am I), the working surface (what I act on), controls (what I
can do now), and selected context (details of the current object). Put controls next to what they affect.
- **Why:** people judge a product by whether the task flows, not by how a screenshot looks.
- **Check:** you can trace the main task end to end without leaving the surface or hunting for a control.

### WEB-4 · Pick a skeleton that fits the content

| Skeleton | Use when | Avoid when |
|---|---|---|
| Sidebar (240–280 wide) + main | Five or more top-level destinations; long sessions with frequent switching | Two to four destinations; single-task tools |
| Top bar (56–64 tall) + content | Few destinations; the content needs full width (editor, map, document) | Deep, multi-level navigation |
| Fluid main + fixed side column (320–360) | List and detail; an inspector for the selected object | The side column would collect unrelated widgets |
| Item grid | Browsing visual objects where a thumbnail aids recognition (files, templates, products) | Text records compared by attributes; use a table or list |
| Single focused column (max 480–640) | Forms, wizards, settings, checkout | The task needs a reference panel beside it |

- **Why:** each skeleton implies a way of working; the wrong one makes users fight the structure.
- **Check:** you can say why this skeleton fits, in terms of the job named in WEB-1.

### WEB-5 · Keep one density mode per screen
Choose by how much the user scans versus reads. Don't mix a compact table with airy cards on one screen.

| Mode | Use for | Row height | Gaps between items |
|---|---|---|---|
| Compact | Queues, consoles, data-heavy tools | 36–40 | 8–12 |
| Medium (default) | Most product screens | 44–52 | 16–24 |
| Airy | Onboarding, checkout, low-complexity flows | 56–64 | 24–32 |

- **Why:** mixed density makes one part look cramped and the other look empty.
- **Check:** every row height and gap on the screen comes from one row of this table.

### WEB-6 · Give each screen one main axis and few zones
- Work flows either left to right (list, then detail) or top to bottom (header, then content), not both.
- Start with two zones. Add a third only when the selected context must stay visible beside the work.
- One scroll container per zone; never a scrolling panel inside another scrolling panel.
- Separate zones with whitespace or a tonal shift first; add a divider line only where zones touch.
- **Why:** every extra zone and scroll area is something to manage instead of the task.
- **Check:** scrolling anywhere on the screen moves exactly one region.

## Clarity

### WEB-7 · Make the interface explain itself
Label controls with what they do ("Export CSV", not "Go"). Navigation and actions carry text; icon-only
buttons are acceptable for universal glyphs (search, close, menu, more) and still get a tooltip and an
accessible name. Show system state wherever it applies: saved or unsaved, syncing, offline, filtered.
- **Why:** a user who has to guess what a control does will avoid it.
- **Check:** a first-time user can say what each control does without hovering.

### WEB-8 · Disclose detail progressively
Show what the primary task needs by default. Put advanced or rare controls where they become relevant: on
selection, in an expandable group, in a detail view. A complex product is acceptable; a confusing one is
not. Group before you hide, and never hide what a decision depends on (CORE-5).
- **Why:** showing everything at once buries the one control the user came for.
- **Check:** the default view covers the primary task, and every hidden control is one obvious step away.

### WEB-9 · Let users recognize instead of recall
Surface the actions for the current object right next to it. Keep control positions fixed across screens:
page actions top right, row actions at the row's end, filters above the list they narrow. Highlight the
current location in the navigation and keep the way back obvious.
- **Why:** people remember where things are far better than what they are called.
- **Check:** on any screen, the current location is visible in both the navigation and the page title.

### WEB-10 · Solve similar problems the same way
Every list filters the same way, every record opens the same way, every destructive action confirms the
same way. Reuse components rather than inventing a variant per screen (CORE-17). Titles keep one size and
position on every screen.
- **Why:** consistency lets a user learn the product once.
- **Check:** two screens that host the same kind of task use the same components in the same places.

### WEB-11 · Give every record a clear identity
Any view of a single object (a customer, an order, a deployment) opens with its name or ID as the largest
text, a labeled status badge, key metadata (owner, dates, amounts), and the actions available on it.
- **Why:** users need to know what they are looking at before they change it.
- **Check:** the header block alone tells you which record this is, its state, and what you can do.

## Actions

### WEB-12 · Rank actions with a fixed button hierarchy
One primary action per screen or per independent section; everything else is visibly quieter. Rare actions
go into an overflow ("More") menu. Buttons use about 10×16 padding, match input height (36–44), and sit
8–12 apart in a group. Every level has hover, focus, active, and disabled styles (CHK-9, CHK-15).

| Level | Use for | Treatment | How many |
|---|---|---|---|
| Primary | The main action of the screen or section | Solid accent fill, highest contrast | One |
| Secondary | Useful alternatives to the primary | Neutral or tinted fill | A few |
| Outline | Cancel, back, low-commitment steps | Border only, no fill | As needed |
| Ghost | Inline, toolbar, row, and navigation actions | Text or icon only; background on hover | As needed |
| Destructive | Delete, remove, revoke | Error color; solid fill only inside the confirm step | Kept apart from the primary |

- **Why:** when two buttons look primary, the user has to read both to decide.
- **Check:** squint at the screen; exactly one button per section reads as the main one (CHK-5).

### WEB-13 · Place actions where users expect them

| Context | Convention |
|---|---|
| Card, modal, or form footer | Actions aligned right; the primary at the far right |
| Destructive confirmation | Cancel on the left, the destructive button to its right |
| Toolbar | Primary action at the start (left); secondary and view controls at the end (right) |
| Page header | Title on the left; page-level actions on the right of the same row |
| Table row | Row actions in the last column or an overflow menu |
| Narrow screens | Actions stacked full width, primary first |

- **Why:** placement is how users find actions without reading labels.
- **Check:** every modal and form in the product puts its actions in the same spot.

### WEB-14 · Keep destructive actions distinct and confirmed
Never style a destructive action as the primary of an ordinary form; separate it by space or position (a
"Danger zone" group, or the far left of a footer). The confirm dialog names the object and the consequence
("Delete project Atlas? Its files will be removed for everyone."), and its button repeats the verb ("Delete
project"), never "OK". Prefer undo when the action can be reversed (CORE-11).
- **Why:** a destructive action that looks like any other gets clicked by habit.
- **Check:** every destructive action has a confirmation that names the object, or an undo.

## System status and feedback

### WEB-15 · Design all five states for every data surface
Any surface that loads, lists, or saves data needs every state below, designed on purpose. Never fail silently.

| State | Must show | Avoid |
|---|---|---|
| Loading | Past ~300 ms of waiting, a skeleton shaped like the final layout; a count or percentage past ~10 s; surrounding chrome stays usable | A full-screen spinner for one panel; layout jumps when content lands |
| Empty | What will appear here, why it is empty, and one action that fills it; a separate "no results" variant with a way to clear filters | A blank area; a large illustration with no action |
| Error | What went wrong in plain words, what to do next (retry, edit, get help), and the user's input preserved | A raw error code alone; a cleared form; color as the only signal |
| Success | A confirmation naming the object ("Invoice 0042 sent"), the resulting state, and undo where possible; toasts last 4–6 s | Silent completion; a modal the user must dismiss after routine work |
| Permission | What is restricted, why, and who can grant access or how to request it | Hiding the feature without a word; controls that fail only when clicked |

- **Why:** the in-between states are where users lose trust, time, and data.
- **Check:** for each data surface you can render all five states (CHK-9).

### WEB-16 · Respond to every action right away
- Acknowledge input within about 100 ms: a pressed state, a spinner inside the button, an optimistic update.
- Validate a field when it loses focus or on submit, not on every keystroke; clear the error once fixed.
- Offer undo for reversible changes; reserve confirmation for irreversible ones (WEB-14).
- Disable a button only while its own request runs; a button that stays disabled says why.
- **Why:** an action with no visible response looks broken and gets repeated.
- **Check:** trigger each action in the render; something visible changes immediately.

## Forms

### WEB-17 · Build forms as one clear column
- Put each label above its field (4–8 gap) and helper text below it in muted type. A placeholder is never
  the label.
- Show errors inline under the field they belong to, with an icon and text, never color alone.
- Stack fields 16 apart; separate field groups by 24–32 with a group heading.
- Use one column, max 480–640 wide. Only two short, related fields may share a row (first and last name,
  city and postal code).
- Make inputs 36–44 tall with about 8×16 padding; let field width hint at the expected length.
- Mark whichever case is rarer: if most fields are required, label the optional ones.
- End with the submit button as the form's primary action, labeled with its result ("Create account").
- **Why:** a form read straight down one line of sight gets filled faster, with fewer mistakes.
- **Check:** every field has a visible, associated label, and every error names the field and the fix.

**Avoid:** "Invalid input" in red under a field. **Do:** "Enter a date after March 1, 2026" with an icon.

## Shape and decoration

### WEB-18 · Choose one radius vocabulary
Pick one system and apply it everywhere; user-specified radii override both examples (CORE-13). When one
rounded shape sits inside another, set the inner radius to the outer radius minus the padding between them,
with a floor of 0.

| Element | Soft system | Tight system |
|---|---|---|
| Tables, data grids, full-bleed regions | 0 | 0 |
| Panels, cards, modals | 12 | 6 |
| Menus, popovers, tooltips | 8 | 6 |
| Buttons, inputs, badges | Full (pill) | 6 |

- **Why:** mixed radii make components look as if they came from different products.
- **Check:** list every radius in the build; each one matches a row of the chosen system.

### WEB-19 · Remove anything that does not serve the task
Each element supports navigation, understanding, a decision, or an action; anything else goes (CORE-4).
Product screens rarely need hero images, decorative gradients, filler illustrations, or welcome banners.
Containers stay only when they do a job (CORE-6).
- **Why:** decoration on a working surface competes with the work.
- **Check:** for each decorative element you can name which of those four jobs it does.

## Growth and adaptation

### WEB-20 · Design for ten times the data
Test every surface with realistic extremes: zero, one, and 10,000 items; names over 60 characters; seven-digit
numbers. Long lists paginate or virtualize; long text truncates with a tooltip or wraps on purpose; the
navigation has room for new sections. New features extend existing patterns instead of adding new layouts.
- **Why:** layouts built around the sample data break on the customer's data.
- **Check:** the render holds with the longest realistic string and the largest realistic count (CHK-2).

### WEB-21 · Keep the hierarchy at every width
At 1280–1440 use the full skeleton. At 768 move the sidebar behind a menu button and turn the side column
into a drawer. At 375 use one column: side panels turn into sheets or stack under the main content, and wide
tables follow `guides/dashboard-and-tables.md`. The dominant region and the primary action always come first.
- **Why:** a hierarchy that works only at desktop width fails everyone else.
- **Check:** at 375, 768, and 1440 the primary action is visible without searching (CHK-12).

## Before you hand off

Run `rules/review-checklist.md` after each section and on the whole screen; for product UI, stress these:

| Check | What to confirm on a product screen |
|---|---|
| CHK-2 | Long names, large counts, and empty values do not break the layout |
| CHK-5 | One primary action per section, ranked per WEB-12 |
| CHK-9 | All five states from WEB-15 exist for each data surface |
| CHK-15 | Every control is reachable by keyboard and shows a visible focus ring |
