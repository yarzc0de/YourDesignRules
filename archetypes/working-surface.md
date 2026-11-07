# Working Surface
> Product-led marketing and apps in which a real, working native workflow is the argument: one surface, framed by navigation and an inspector.

## When to pick
- Design tools, editors, IDEs, project and issue trackers, analytics, no-code builders, mapping and CAD tools.
- B2B products where watching the workflow convinces more than any description of it.
- Admin products with a central object (a document, a board, a canvas, a query) that the user manipulates.
- Skip it when the product has no distinctive interface, or the brief offers no real content to show in it.

## Composition
- Organize every product view in three parts: navigation (left rail or top bar), the working surface in the
  center as the dominant region, and an inspector of 280–340 px for the selected object.
- Show one believable moment of the workflow: an object selected, the inspector showing its properties, a
  toolbar state that matches the selection.
- Build the surface from real elements (CORE-10) and fill it with supplied data or plainly labeled sample
  data (CORE-9).
- On websites, reuse that one surface through crops: later sections zoom into the inspector, the toolbar, or
  a single object, each with a caption that says what is shown.
- Website hero: the headline and primary action sit in a band at the top, and one product frame spanning
  most of the content width rises from below it on the same ground, cropped by the fold; never copy on one
  side and a small framed app on the other.
- Keep the marketing around the frame quiet so the interface carries the color and the detail.

## Typography
| Role | Family | Weights |
|---|---|---|
| Display (marketing only) | Space Grotesk | 500, 700 |
| Body, product UI | Manrope | 400, 500, 600 |
| Code, values, coordinates | IBM Plex Mono | 400, 500 |

- Marketing display 48–80 px in Space Grotesk 700, line height 1.05, −2% tracking; section headings 32–40
  px at 500.
- Inside the product, use Manrope alone: panel titles 14–16 px at 600, UI labels 12–13 px at 500, body
  14 px. Space Grotesk stays outside the frame.
- Inspector values, coordinates, and code in IBM Plex Mono 12–13 px.
- Neither Space Grotesk nor Manrope has italics; show emphasis with weight.
- Load from Google Fonts: Space Grotesk (500, 700), Manrope (400–600), IBM Plex Mono (400, 500).

## Color roles
Light palette for both the marketing page and the product inside the frame.

| Role | Token | Example |
|---|---|---|
| Ground (marketing) | `--background` | `#FFFFFF` |
| Band surface (marketing sections) | `--surface` | `#F3F5F8` |
| Product chrome (nav, inspector) | `--chrome` | `#F7F8FA` |
| Canvas | `--canvas` | `#EDF0F3` |
| Text primary / secondary / muted | `--foreground`, `--secondary-foreground`, `--muted-foreground` | `#101418` / `#4A525C` / `#626C77` |
| Accent (selection, primary action) | `--primary` | `#2B59E8` with `#FFFFFF` text |
| Selection fill | `--selection` | accent at 10–12% over the canvas |
| Boundary / strong (inputs) | `--border`, `--border-strong` | `#DFE3E8` / `#7F8893` |
| Status | `--success`, `--warning`, `--error`, `--info` | `#16753F`, `#985700`, `#C8283A`, `#0A6AA8` |

- If the real product is dark, use its own palette inside the frame and choose the marketing ground to suit it.
- This palette is a starting point; brand or user colors replace it (CORE-13).

## Shape and elevation
- Radius follows the element: canvas and tables 0, controls 6 px, panels and popovers 8–12 px, the marketing
  product frame 16–24 px.
- On websites, the product frame gets one large soft shadow plus a 1 px hairline, within the limits in
  rules/color.md. Panels inside the product stay flat.
- Menus and popovers inside the product take the small soft shadow.
- Selection: a 1.5–2 px accent outline, handles where the object can be resized, and the inspector showing the
  selected object's name.

## Imagery
- The interface is the imagery. Photos of people are optional and secondary, for example one shot of a team
  at work near the closing section.
- Code samples come from the user's real docs or API. Without them, leave the code block out rather than write
  code that only looks plausible.
- Icons: one library at 16 px in toolbars, with a tooltip or label on anything that is not universal.
- Charts inside the frame use supplied series only.

## Avoid
- A screenshot floating on a gradient, or a tilted 3D perspective mockup.
- Several small, disconnected mock panels scattered around the page.
- Invented revenue charts, user counts, partner logos, or integrations.
- Pictures of UI where live elements belong.
- Glowing or neon frames around the product.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites
- Apps: the surface gets most of the viewport, side panels collapse, and an empty canvas offers one clear first
  action.
- Apps: toolbars 40–48 px tall; keyboard shortcuts shown in menus and tooltips.
- Websites: one frame in the hero, crops of the same frame in later sections, and the primary call to action
  repeated at the end.
- Websites: keep sample content consistent across crops; the same project, names, and values appear every time.
