# Motion

Rules for animation and transitions: hover and press feedback, menus, dialogs, sheets, page changes, scroll
reveals, loading, and data updates. Read this before adding any transition, and whenever a guide asks for
interaction states. Motion should explain what changed and where things went. If an animation explains
nothing, it is decoration, and CORE-7 applies.

## Purpose

### MOTION-1 · Give every animation a job
Animate only to do one of four things: confirm an action (feedback), show where something came from or went
(orientation), keep the user's place across a change (continuity), or point out something that changed
while they weren't looking (attention). Everything else stays still.
- **Why:** motion without a job slows the user down and makes the interface feel busy.
- **Check:** for each animation you can name which of the four jobs it does.

### MOTION-2 · Keep one signature moment per page at most
A marketing page may have one expressive motion moment: a headline that resolves as it scrolls in, a product
walkthrough, a crossfade between two states of the hero image. Everything around it uses the quiet defaults
below. Product UI gets no signature moment; its motion is feedback and continuity only.
- **Why:** several competing effects cancel each other out and read as a template.
- **Check:** you can point to the single expressive animation, and the rest of the page uses the defaults.

### MOTION-3 · Design the still frame first
Every screen must look finished with all motion switched off. Animation is applied on top of a correct
static layout; it never carries information that the static state lacks.
- **Why:** reduced-motion users, screenshots, slow devices, and failed scripts all see the still frame.
- **Check:** with animations disabled, nothing is missing, hidden, overlapping, or half-transparent.

## Timing

### MOTION-4 · Pick durations from this table

| What moves | Duration | Examples |
|---|---|---|
| Instant feedback | 100–150 ms | button press, checkbox tick, toggle thumb |
| Hover and color changes | 150–200 ms | background tint, underline, icon color |
| Small surfaces | 150–250 ms | tooltip, dropdown, popover, toast in |
| Medium surfaces | 250–350 ms | dialog, bottom sheet, side drawer, accordion |
| Large changes | 350–500 ms | route change, shared-element expand, hero image swap |
| Scroll reveals | 500–700 ms | a section rising into view on a marketing page |

Nothing that blocks the user should take longer than 500 ms. On phones, use the low end of each range.
- **Why:** under ~100 ms a change feels instant; past ~500 ms the user starts waiting for the interface.
- **Check:** every duration in the code falls inside its row.

### MOTION-5 · Make exits faster than entrances
Leaving takes about two thirds of the time entering took: a dialog that opens in 300 ms closes in about
200 ms. Dismissed things should get out of the way.
- **Why:** the user has already decided to move on; a slow exit holds them back.
- **Check:** each exit duration is shorter than its matching entrance.

### MOTION-6 · Respond within 100 ms
The first visible response to a click, tap, or key press (a pressed state, a spinner, an optimistic update)
starts within 100 ms, even when the work behind it takes longer.
- **Why:** a delay before any response makes people click again.
- **Check:** pressing any control changes something on screen immediately.

## Easing

### MOTION-7 · Never use linear or the browser default for movement
`linear` is only for things that move at constant speed: progress bars, spinners, marquees, video scrubbing.
The CSS default `ease` and the generic `ease-in-out` keyword are not chosen curves. Define and use easing
tokens instead:

```css
:root {
  --ease-out:    cubic-bezier(0.22, 1, 0.36, 1);   /* things arriving: decelerate into place */
  --ease-in:     cubic-bezier(0.55, 0, 1, 0.45);   /* things leaving: accelerate away */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);   /* things moving from one spot to another */
  --dur-fast: 150ms;
  --dur-base: 250ms;
  --dur-slow: 400ms;
}
.menu { transition: opacity var(--dur-base) var(--ease-out), transform var(--dur-base) var(--ease-out); }
```
- **Why:** real objects speed up and slow down; constant speed looks mechanical.
- **Check:** no transition or animation uses `linear` (except continuous progress) or omits a timing function.

### MOTION-8 · Match the curve to the direction
Entering elements decelerate (`--ease-out`), leaving elements accelerate (`--ease-in`), and elements that
stay on screen while moving use `--ease-in-out`. For gesture-driven motion (drag to dismiss, swipe between
pages) use a spring so the motion continues from the finger's velocity.
- **Why:** the curve tells the eye whether something is arriving, leaving, or relocating.
- **Check:** every enter uses an ease-out curve and every exit an ease-in curve.

### MOTION-9 · Keep bounce out of interface chrome
No visible overshoot on buttons, menus, dialogs, tables, or navigation. A slight overshoot is acceptable
only for playful directions (see archetypes/toybox.md) and only on decorative or celebratory elements.
- **Why:** bouncing controls feel unstable and slow down repeated use.
- **Check:** no UI control scales or moves past its final position before settling.

## What to animate

### MOTION-10 · Animate transform and opacity only
Move with `transform: translate`, grow with `transform: scale`, fade with `opacity`. Do not animate `top`,
`left`, `width`, `height`, `margin`, or `padding`; they force layout on every frame. To expand height, use
`grid-template-rows: 0fr → 1fr` or measure and animate a transform (FLIP). Animate a shadow by fading the
opacity of a pseudo-element that carries it, not by changing `box-shadow`.
- **Why:** transform and opacity run on the compositor and stay smooth on slow phones.
- **Check:** the transition property lists contain only `transform`, `opacity`, colors, or `grid-template-rows`.

### MOTION-11 · Travel short distances
Entering elements move 8–24 px, never across the screen. Scale-in starts at 0.95–0.98, never at 0. Popovers
and menus grow from their trigger (`transform-origin` on the side nearest the trigger); sheets and drawers
slide in from the edge they are attached to. The 0.95 floor applies to surfaces and containers; drawn lines
are exempt: a 1 px rule may grow with `scaleX(0 → 1)` and an SVG stroke may draw in with
`stroke-dashoffset`, as long as the line is finished in 300–600 ms.
- **Why:** small, anchored movement shows where something came from without making the eye chase it.
- **Check:** no surface travels more than 24 px or scales from below 0.95, except full-screen sheets that
  slide from their edge and drawn lines.

### MOTION-12 · Stagger lists briefly, then stop
When several items appear together (menu links, search results, a card row on first load), offset each by
30–50 ms, apply the stagger to the first 6–8 items only, and keep the whole sequence under 400 ms.
- **Why:** a short stagger shows reading order; a long one makes the last item feel late.
- **Check:** the last staggered item finishes within 400 ms of the first one starting.

## Interaction states

### MOTION-13 · Give every interactive element the full state set
Default, hover, pressed, focus-visible, disabled, and, where data loads, loading. Hover changes color or
background in 150–200 ms. Pressed answers in about 100 ms with `scale(0.97–0.98)` or a 1 px downward shift.
Focus-visible shows a ring at once with no transition delay. Disabled has no hover response at all.

```css
.btn { transition: background-color 180ms var(--ease-out), transform 100ms var(--ease-out); }
.btn:hover { background-color: var(--primary-hover); }
.btn:active { transform: scale(0.98); }
.btn:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; transition: none; }
.btn:disabled { opacity: 0.5; pointer-events: none; }
```
- **Why:** states are how the interface proves it heard the user.
- **Check:** each control visibly changes on hover, press, and keyboard focus.

### MOTION-14 · Morph toggles between their two states
An icon that switches meaning (menu ↔ close, play ↔ pause, expand ↔ collapse) rotates or morphs into its
other state over 200–250 ms instead of swapping instantly. Chevrons rotate 180° rather than being replaced.
- **Why:** the morph shows that both states belong to one control.
- **Check:** toggling the control shows a short transition between the two icons.

### MOTION-15 · Open the mobile menu as a full panel
On phones, the navigation menu opens as a full-height panel or sheet, not a small dropdown. It slides or fades
in over 250–300 ms, its links stagger in per MOTION-12, the page behind stops scrolling, and Escape or the
close button returns focus to the menu button.
- **Why:** a full panel gives touch targets room and makes the menu feel like a place, not a popup.
- **Check:** open the menu at 375 px; it fills the screen, the background is locked, and focus returns on close.

## Continuity

### MOTION-16 · Keep the user's place across a change
When a list item opens into a detail view, a thumbnail becomes a full image, or a card expands, animate the
element from its old position and size to its new one (FLIP, the View Transitions API, or a shared-element
transition in the platform). Route changes without a shared element use a quick crossfade (150–250 ms), not a
slide or zoom.
- **Why:** continuity tells the user that the new view is the same thing, seen closer.
- **Check:** opening and closing a detail view never makes the user search for where they were.

### MOTION-17 · Animate data changes without hiding the data
When values update, fade or tint the changed value briefly (about 1 s) so the eye finds it. Do not count up
numbers on dashboards or tables, and do not re-animate charts every time a filter changes; transition
the bars or lines from old values to new ones in 250–400 ms instead.
- **Why:** count-up effects delay reading and make the number look unreliable.
- **Check:** every number is readable at its final value the instant it appears.

## Loading

### MOTION-18 · Match the loading indicator to the wait

| Expected wait | Show |
|---|---|
| Under 300 ms | Nothing; just render the result |
| 300 ms – 2 s | Inline spinner or progress on the control that started it |
| Over 2 s, layout known | Skeleton shaped like the real content, gentle pulse of 1.5–2 s |
| Over 10 s or measurable | Determinate progress with a label, and a way to cancel |

Never flash a spinner for a fast result: delay it about 300 ms, then keep it visible at least 500 ms once shown.
- **Why:** an indicator that blinks on and off is worse than none.
- **Check:** each async action falls in one row of the table and uses that indicator.

## Scroll

### MOTION-19 · Prefer one orchestrated moment to a reveal on every section
A fade-and-rise on every section is the generic default and reads as generated. Spend motion on the page's
one signature moment (MOTION-2) instead. If you still use scroll reveals on a marketing page, apply them to at
most two or three elements that benefit from arriving (a diagram, a key number, a product view): fade in
while rising 16–32 px over 500–700 ms on `--ease-out`, once, never replayed on scroll back. Trigger with `IntersectionObserver` (threshold about 0.15),
never an unthrottled scroll listener. Do not reveal content in product UI, tables, or dashboards, and never
delay the hero headline or the primary CTA.
- **Why:** one well-timed reveal is noticed; ten identical ones are noise, and in a tool they delay work.
- **Check:** the first screen is fully visible on load, no more than three elements use scroll reveals, and
  none animates a second time.

### MOTION-20 · Never hide content behind JavaScript
Start revealed elements visible in the HTML and hide them only after a script adds a class (for example
`.js .reveal { opacity: 0 }`). If the script fails or is blocked, everything must still show.
- **Why:** content stuck at `opacity: 0` is the most common way motion breaks a page.
- **Check:** with JavaScript disabled, every section is visible.

### MOTION-21 · Don't hijack scrolling
No scroll-jacking, scroll snapping on long text pages, or parallax on text. Parallax, if used at all, is
limited to one background image moving at 0.8–0.9× scroll speed.
- **Why:** taking control of scroll breaks trackpads, keyboard paging, and screen readers.
- **Check:** the page scrolls at native speed with mouse wheel, trackpad, keyboard, and touch.

## Accessibility

### MOTION-22 · Respect reduced motion
Under `prefers-reduced-motion: reduce`, replace movement with an opacity change or an instant swap; turn off
parallax, autoplay, staggering, and scroll reveals; keep essential feedback such as focus rings and pressed
colors. In SwiftUI read `accessibilityReduceMotion`; in Flutter read `MediaQuery.disableAnimations`.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
- **Why:** motion can cause nausea and dizziness for people with vestibular disorders.
- **Check:** with reduced motion turned on in the OS, nothing slides, scales, or parallaxes.

### MOTION-23 · Let users stop anything that runs on its own
Anything that moves, loops, or autoplays for more than 5 seconds (carousels, background video, marquees,
animated illustrations) needs a visible pause control. Never flash anything more than three times per second.
- **Why:** these are WCAG 2.2.2 and 2.3.1 requirements, and endless motion pulls attention from reading.
- **Check:** every autoplaying element has a pause button, and nothing strobes.

## Performance

### MOTION-24 · Keep it at 60 fps on a mid-range phone
Use `will-change` only on elements about to animate and remove it afterwards. Avoid animating `filter: blur`,
`backdrop-filter`, and large `box-shadow` values on big areas. Throttle any scroll or pointer work with
`requestAnimationFrame`. Test on a throttled CPU (4× slowdown in browser dev tools).
- **Why:** dropped frames make even well-designed motion feel broken.
- **Check:** a performance recording of the main interactions shows no long frames over 16 ms.

## Platform notes

| Platform | Defaults to reach for |
|---|---|
| CSS / Tailwind | the tokens in MOTION-7; Tailwind `ease-[cubic-bezier(0.22,1,0.36,1)] duration-300` |
| React | CSS transitions first; Motion (Framer Motion) for layout and shared-element transitions |
| SwiftUI | `.spring(response: 0.35, dampingFraction: 0.9)` for UI, `.easeOut(duration: 0.25)` for fades |
| Flutter | `Curves.easeOutCubic` for enter, `Curves.easeInCubic` for exit, `AnimatedSwitcher` for swaps |
| Figma prototypes | Smart Animate with a custom bezier matching `--ease-out`, durations from MOTION-4 |

## Motion and archetypes

Each archetype has a motion character (see the Motion section of each file in archetypes/). The timing,
easing, and accessibility rules above apply under every archetype; the archetype only shifts the tone, for
example crisper and shorter for technical directions, slower crossfades for photographic ones.
