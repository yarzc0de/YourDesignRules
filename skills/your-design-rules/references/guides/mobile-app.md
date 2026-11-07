# Mobile app guide

Rules for phone apps and phone-sized mockups in any stack: SwiftUI, Jetpack Compose, Flutter, React Native,
or a mobile web app. Read it after `references/rules/core.md` whenever the target is a phone screen. General spacing,
type, and color rules live in `references/rules/layout.md`, `references/rules/typography.md`, and `references/rules/color.md`; this guide
covers what changes when the screen is small, held in one hand, and shared with system UI. Sizes are in pt
(iOS) or dp (Android), which map one to one onto CSS px in a mockup.

## Frame and system chrome

### MOB-1 · Keep app UI inside the safe area
No text, control, or content may sit under the status bar, the notch or Dynamic Island, the home indicator,
or the Android navigation bar. Backgrounds and full-bleed images may extend behind them; anything people
read or tap may not. In code, read the insets from the platform instead of hard-coding them.

| Region | Typical inset | Notes |
|---|---|---|
| iOS status bar, incl. notch or island | 47–62 pt | varies by device; 20 pt on home-button phones |
| iOS home indicator | 34 pt | bottom inset on Face ID phones |
| Android status bar | about 24–48 dp | taller on some devices with display cutouts |
| Android navigation | about 24 dp (gestures), 48 dp (three buttons) | depends on the user's setting |

Stack notes: SwiftUI respects the safe area by default; Flutter uses `SafeArea` or `MediaQuery.paddingOf`;
React Native uses `react-native-safe-area-context`; mobile web needs `viewport-fit=cover` plus
`env(safe-area-inset-*)`.
- **Why:** content under system UI is hard to read, and taps there trigger the OS instead of the app.
- **Check:** overlay the device insets on the render; no text or control crosses them.

### MOB-2 · Fix the mockup width, let the height grow
Start a static mockup at a real device size and treat only the width as fixed. A scrolling screen gets a
taller frame that shows all of its content; never crop content at the device height or squeeze it to fit.
If the first viewport matters, mark it with a guide line (for example at y = 844).

| Device class | Frame (pt or dp) |
|---|---|
| Small iPhone | 375 × 667 |
| Default iPhone | 390 × 844 or 393 × 852 |
| Large iPhone | 430 × 932 |
| Default Android | 360 × 800 or 412 × 915 |

- **Why:** a cropped mockup hides content the build must place anyway; a squeezed one misstates spacing.
- **Check:** the last section in the frame is complete and followed by the normal bottom padding.

### MOB-3 · Build system chrome first, then content
Place the frame parts in this order: status bar area, top bar or large title, tab bar or bottom action area,
then the content wrapper and its sections. The chrome decides how much room the content really has.
- **Why:** content built first ends up hidden behind bars that arrive later.
- **Check:** top bar and tab bar exist before the first content section is rendered.

## Content wrapper and spacing

### MOB-4 · Apply side padding once, on one content wrapper
Put all scrolling content in a single container with 16–20 horizontal padding; pick one value and keep it on
every screen. Sections inside carry no side padding of their own. Full-bleed elements (hero image, carousel)
opt out on purpose. Space siblings with the container's gap, not with spacer elements or per-child margins.
- **Why:** padding repeated per section drifts, and the shared left edge breaks.
- **Check:** every text block on the screen starts at the same x position.

### MOB-5 · Space the screen with one mobile scale
Take every value from the 4-pt scale in `references/rules/layout.md`:

| Relationship | Value |
|---|---|
| Screen side padding | 16–20 |
| Between screen sections | 24–32 |
| Between related items in a group | 12–16 |
| Section heading to its content | 8–12 |
| Vertical padding inside a list row | 12–16 |
| Icon to its label | 8 |
| Between buttons in a group | 8–12 |
| Bottom padding of the scroll content | same as the section gap |

When a bar floats over the content, add its height and bottom offset to that bottom padding (MOB-8).
- **Why:** a small screen exposes uneven spacing faster than a large one.
- **Check:** every gap on the screen maps to a row in this table.

## Tab bar

### MOB-6 · Use a tab bar for 3–5 top-level destinations
A tab bar switches between peer destinations; it is not a toolbar of actions. With two destinations use a
segmented control; with more than five, regroup or move the rest under the last tab. A central "Create" tab
is acceptable only when creating is the app's core loop. Order and labels never change between screens.
- **Why:** more than five tabs push targets and labels below usable sizes.
- **Check:** the bar has 3–5 items, and each one leads to a place, not a one-off action.

### MOB-7 · Size the floating tab bar from this table
Use these values for a custom floating bar. When the native tab bar suits the brand, use it instead (MOB-20).

| Part | Spec |
|---|---|
| Position | inset 16 from both sides, 12 above the bottom safe-area inset |
| Height | 56–64 |
| Corner radius | half the height, so the ends are fully round |
| Inner padding | about 6 |
| Fill | translucent surface at 70–85% opacity with background blur; solid surface where blur is unsupported |
| Shadow | soft and diffuse, per `references/rules/color.md` |
| Item | icon 22–24 above a label 10–11, sentence case |
| Selected item | filled icon and label in the accent tint, on a soft pill-shaped highlight |
| Inactive item | outline icon and label in the muted text color |

- **Why:** fixed dimensions keep the bar compact, thumb-sized, and identical on every screen.
- **Check:** the selected tab is obvious in grayscale, and labels pass 4.5:1 on the blurred composite (CHK-3).

### MOB-8 · Reserve layout space for the tab bar
Keep the bar in the layout flow as the last element of the screen stack, or use the platform's native tab
bar container. If it floats over scrolling content, give the content bottom padding of bar height plus bottom
offset plus one section gap so the last item can scroll clear. Never absolutely position the bar over content
without that reserved space. In a tall static mockup the bar sits at the end of the frame.
- **Why:** an unreserved bar permanently hides the last row and its actions.
- **Check:** scroll to the end; the last element sits fully above the bar.

## Screen rules

### MOB-9 · Orient the user within the first two elements
Give each screen one primary intent (CORE-1). The first one or two elements, usually the title plus the main
control or summary, say which screen this is and what it is for. Secondary information goes further down.
- **Why:** on a phone the first viewport is often all people read before they act.
- **Check:** hide everything below the first two elements; the screen's purpose is still clear.

### MOB-10 · Use one title size and style on every screen
Screens at the same level share title size, weight, and position: for example a 28–34 large title on
top-level screens and a 17–20 inline title on pushed screens. Take sizes from `references/rules/typography.md`.
- **Why:** a title that changes between tabs makes the app look assembled from parts.
- **Check:** overlay two tab screenshots; their titles occupy the same box.

### MOB-11 · Recompose for the phone instead of shrinking desktop
Design one dominant column. Side panels become sheets (MOB-19) or stacked sections, wide tables become list
rows (DATA-17), and hover-only controls become visible buttons or long-press menus. Never scale a desktop
layout down to phone width.
- **Why:** a shrunken desktop layout yields tiny type and targets nobody can hit.
- **Check:** at 375 wide nothing scrolls sideways except an intentional carousel or data table (CHK-12).

### MOB-12 · Keep navigation and relevant actions in view
Persistent navigation (tab bar or top bar) stays on screen across top-level flows. Secondary actions tied to
the current content stay one tap away (top-bar button, overflow menu, row swipe) rather than moving to a
settings screen. Hide navigation only during focused tasks such as checkout, capture, or full-screen media.
- **Why:** people lose their place when the way back or the next step disappears.
- **Check:** from any screen, a top-level destination is one tap or one back gesture away.

## Reach and touch

### MOB-13 · Put frequent actions within thumb reach
Design for one-handed use: primary and frequent actions in the lower half, titles and rare actions on top.

| Zone | Put here |
|---|---|
| Bottom third (easy) | primary button, tab bar, compose or create, frequent controls |
| Middle (comfortable) | content, list rows, inline controls |
| Top third (stretch) | title, back, search entry, rare actions such as edit, settings, filters |

A full-width bottom button is 48–56 tall, inset by the side padding, and sits above the home indicator.
Platform-standard top-bar commits ("Done", "Save") are fine for short forms inside sheets.
- **Why:** the top corners of a modern phone are out of reach for most thumbs.
- **Check:** each screen's primary action lies below its vertical midpoint, or follows the sheet exception.

### MOB-14 · Make touch targets at least 44 pt or 48 dp
Hit areas measure ≥ 44 × 44 pt on iOS and ≥ 48 × 48 dp on Android, with ≥ 8 between neighbors. An icon can
stay visually at 20–24 if padding brings its tappable area up to the minimum. List rows are at least 44 tall
on iOS and 48–56 on Android.
- **Why:** small or crowded targets cause mis-taps, and mis-taps trigger the wrong action.
- **Check:** outline every hit area; none is under the minimum or overlaps its neighbor.

### MOB-15 · Let text scale without breaking the layout
Body text is 15–17 (`references/rules/typography.md`) and grows with the user's text-size setting: Dynamic Type on iOS,
sp on Android, rem on mobile web. Containers that hold text never get a fixed height; rows wrap or grow
instead of truncating essential labels.
- **Why:** many people raise the system text size, and fixed boxes clip it.
- **Check:** at the largest accessibility text size nothing essential is clipped or overlapping (CHK-2).

## Selection, confirmation, feedback

### MOB-16 · Mark selection with more than color
Selected rows, chips, segments, and tabs change in two ways at once: color plus a shape, icon, or weight
change (checkmark, filled segment, filled icon). In multi-select mode the top bar shows the count
("3 selected") and a bottom bar holds the available actions.
- **Why:** color-only selection fails for colorblind users and in direct sunlight.
- **Check:** in grayscale, the selected item is still obvious.

### MOB-17 · Confirm before committing, or offer undo
Apply CORE-11. A destructive action opens a dialog or action sheet that names the object and the outcome,
with a verb label ("Delete 3 photos") and an easy cancel. Payments, sends, and bookings get a review step
that summarizes what will happen. Reversible actions (archive, mark as read) may run at once with an undo
snackbar or banner instead of a confirm.
- **Why:** accidental taps are common on a phone, and one tap must never cause loss.
- **Check:** every destructive or committing tap leads to a confirm or to an undo.

### MOB-18 · Show the next state after every action
Answer each tap within about 100 ms with a pressed state. For slower work, show progress inside the control
(spinner in the button, button disabled against double submits). When the work completes, show the result
where the user is looking: the updated row, a success screen for payments, or a short toast or snackbar.
Never finish silently. Haptics may reinforce the visual change but never replace it.
- **Why:** with no visible response people tap again, and duplicate actions follow.
- **Check:** for each action in the flow you can point at the frame that shows its result.

## Sheets

### MOB-19 · Put secondary tasks in bottom sheets
Use a sheet for tasks that support the current screen: filters, sharing, quick create, item details,
pickers. Keep the parent screen visible behind a dim scrim so the context stays.

| Part | Spec |
|---|---|
| Heights | medium about 50% of the screen; large up to just below the top safe area |
| Grabber | 32–36 × 4–5, centered, 8 from the top edge |
| Top corner radius | 16–28 |
| Header | title plus a close or "Done" control |
| Primary action | pinned to the bottom, above the home indicator |
| Content padding | the screen's 16–20 side padding |

Show one sheet at a time. Multi-step tasks and long forms get a full-screen modal or a pushed screen instead.
Keep scrolling inside the sheet distinct from the drag-to-dismiss gesture.
- **Why:** a sheet keeps people anchored to the screen that started the task.
- **Check:** no sheet opens on top of another sheet.

## Platform conventions

### MOB-20 · Use platform conventions unless the brand defines its own
Default to the host platform's patterns. Deviate only where the brand system defines its own (a custom
floating tab bar, for example), and then apply that deviation on every screen.

| Concern | iOS | Android (Material 3) |
|---|---|---|
| Top-level title | large title (34 pt) that collapses to an inline 17 pt title | top app bar 64 dp, title 22 sp; medium and large variants collapse |
| Back | chevron plus previous title at top left; swipe from the left edge | system back gesture or button; up arrow in the top app bar |
| Top-level navigation | tab bar, 49 pt plus the home indicator | navigation bar, 80 dp, 24 dp icons |
| Primary screen action | trailing top-bar button or bottom button | floating action button (56 dp) at bottom right, or bottom button |
| Confirmation | centered alert; action sheet for a set of choices | dialog with right-aligned text buttons, confirm last |
| Short feedback | inline change or banner; there is no system toast | snackbar at the bottom, optional undo action |
| Extra actions | pull-down menu from a "More" button; context menu on long press | three-dot overflow menu in the top app bar |
| Sheets | sheet with medium and large detents and a grabber | modal bottom sheet with a drag handle |
| Icons | SF Symbols | Material Symbols |
| Text scaling | Dynamic Type text styles | sp units |
| Minimum target | 44 × 44 pt | 48 × 48 dp |

- **Why:** platform patterns are already learned; a foreign one costs every user time.
- **Check:** each row is handled the native way or by one documented brand rule.

## Review

Run `references/rules/review-checklist.md` on every screen. Pay extra attention to CHK-2 at large text sizes, CHK-5 for
one primary action within thumb reach, CHK-9 for confirmations and feedback states, and CHK-12 at 375 and 430
widths.
