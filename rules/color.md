# Color

How to give colors jobs, decide where saturation goes, meet contrast thresholds, put text on images, draw
shadows, and build a dark palette. Read it before you choose a hue, define tokens, or style a surface, and
return to the contrast and shadow rules during review (`rules/review-checklist.md`).

## Roles and tokens

### COLOR-1 · Assign roles before you choose hues
Decide what each color does, then pick its value. Every interface needs these roles:

| Role | Job | Example tokens |
|---|---|---|
| Ground | The dominant background of the page or app | `--background` |
| Surface | Working planes (panels, popovers, inputs), set apart from the ground by lightness | `--surface`, `--surface-raised` |
| Text | Primary, secondary, muted, and inverse copy | `--foreground`, `--foreground-secondary`, `--muted-foreground`, `--inverse-foreground` |
| Accent | Actions, selection, focus | `--primary`, `--primary-foreground`, `--ring` |
| Boundary | Quiet borders, dividers, input outlines | `--border`, `--input` |
| Status | Success, warning, error, info; destructive actions | `--success`, `--warning`, `--error`, `--info`, `--destructive` |

Every fill that can hold text gets a `-foreground` partner for the text on top of it (`--success-foreground`,
`--destructive-foreground`). `--destructive` styles destructive buttons; `--error` styles error messages. They
may share a hue.
- **Why:** a hue picked without a job ends up decorating instead of communicating.
- **Check:** every color in the build maps to exactly one row of this table.

### COLOR-2 · Reference tokens in components, never raw values
Components read `var(--primary)` or the platform equivalent: Tailwind theme keys, SwiftUI asset colors, a
Flutter `ColorScheme`. Raw hex and rgb values live only where tokens are defined. Add new tokens next to
existing ones; never silently overwrite a project's tokens (see `rules/core.md`).
- **Why:** one token edit should restyle the whole product, dark theme included.
- **Check:** searching component code for hex and `rgb(` literals finds hits only in the token file.

### COLOR-3 · Limit the palette to two or three core colors
Work with two or three core hues plus a neutral ramp. Status hues are additional and stay functional. A
fourth brand hue needs a stated reason.
- **Why:** each extra hue weakens the accent and makes the screen look unplanned.
- **Check:** count the distinct non-neutral hues outside the status set; the total is 3 or fewer.

### COLOR-4 · Pair every color signal with a label or icon
Status, validation, and selection never depend on hue alone. An invalid field shows red, an icon, and a
message; a selected row shows a tint plus a check mark or a weight change.
- **Why:** color-blind readers, glare, and grayscale displays strip hue away, so the cue must survive without it.
- **Check:** view the screen in grayscale; every state is still identifiable.

## Where chroma lives

### COLOR-5 · Choose one chroma relationship and keep it
Decide where saturated color sits and how much area it covers. Pick one model:
- **Neutral ground, one vivid accent:** a white or cool gray field; color only on actions and selection.
- **Dark field, luminous details:** a deep ground; bright color limited to small points such as data, focus,
  and the primary action.
- **Saturated ground, contrasting type:** a bold color field with near-white or near-black type that clears
  COLOR-10.

Hold the chosen model on every screen of the product.
- **Why:** mixing models produces pages that look assembled from different products.
- **Check:** you can name the model in one phrase, and every screen fits it.

### COLOR-6 · Spend the accent on actions and selection only
The primary call to action is the most prominent colored element in view. Keep the accent off decorative
icons, headings, illustrations, and background shapes. Secondary actions use neutral or outline styling.
- **Why:** an accent that appears everywhere stops pointing at the next step.
- **Check:** blur the screenshot; the first colored shape you notice is the primary action or the selection.

### COLOR-7 · Keep status hues distinct from the accent
Success, warning, error, and info each get their own hue, and none matches the accent. If the brand accent is
red or green, shift the conflicting status hue or rely more on icons and text, so an error never looks like a
button. Pair each status with a label or icon per COLOR-4.
- **Why:** an accent that doubles as a status color makes every action look like an alert.
- **Check:** set a primary button beside each status badge; no pair can be mistaken for the other.

## Grounds and surfaces

### COLOR-8 · Never use beige, cream, ivory, tan, or sand grounds
These hues and every warm off-white are banned for page and app backgrounds and for container fills (cards,
panels, bands, sidebars, modals). Use these instead:

| Instead of | Use |
|---|---|
| Cream or ivory page ground | Pure white `#FFFFFF`, or a cool neutral such as `#F7F8FA` |
| Beige or sand panel fill | A cool gray surface such as `#F1F3F5`, or a lightness step of the ground |
| Tan section band | A dark ground such as `#111318`, or a deliberate saturated color field |
| Warm off-white for a crafted or luxury feel | A white ground, with warmth carried by type, light, texture, and photography |

Natural tones inside photographs are fine; the ban covers interface fills. When the user or supplied brand
guidelines require one of these grounds, follow them (see `rules/core.md`).
- **Why:** warm off-white grounds are the stock default of generated UI and look muddy beside real imagery.
- **Check:** (heuristic) on any near-white fill, red minus blue is 4 or less on a 0–255 scale, and no light or
  mid-tone fill has hue 25–60° with saturation 10–60%.

### COLOR-9 · Separate surfaces from the ground by lightness
Panels, popovers, and inputs sit one lightness step away from the ground instead of inside a heavy border or
shadow. In light themes, white surfaces on a `#F5F6F8` ground or `#F3F4F6` surfaces on white both work; for
dark themes, see COLOR-17. Add a `--border` hairline only where the step alone is too faint.
- **Why:** tonal steps group content without adding boxes or visual noise.
- **Check:** each surface differs visibly from the ground, and none relies on a shadow alone to stand apart.

## Contrast

### COLOR-10 · Meet WCAG AA contrast for text and controls

| Element | Minimum ratio |
|---|---|
| Body and UI text below large size | 4.5:1 |
| Large text: at least 24 px regular, or at least 18.66 px bold | 3:1 |
| Boundaries of UI components (inputs, toggles, focus rings) and meaningful icons | 3:1 against adjacent colors |

Secondary and muted text get no exemption: `--muted-foreground` must reach 4.5:1 on every surface it sits on.
Disabled controls are exempt from the ratio.
- **Why:** below these ratios text fails low-vision readers and washes out on bright screens and projectors.
- **Check:** run a contrast checker on every text and surface token pair, in both themes.

### COLOR-11 · Measure contrast on the rendered composite
Text over photographs, translucent glass, gradients, or video takes its contrast from whatever is behind it.
Sample the lightest and darkest background pixels under each text block and test both. Recheck after every
crop change and at every breakpoint.
- **Why:** a pair that passes on a flat swatch can fail over the bright patch of a photo.
- **Check:** the worst-case pixel under each line of text still meets COLOR-10.

## Text on images

### COLOR-12 · Set text on a quiet area or a local fade
Work through these in order:
1. Choose or crop the image so text lands on a calm, low-detail region: sky, wall, shade, soft focus.
2. If that region is still too busy, add a soft gradient behind the text alone, fading to fully transparent
   well before the far edge.

Do not use a visible dark box behind the copy, heavy text-shadow halos, or a uniform dark overlay across the
whole image. The overlay flattens the photo; the box and halo look like patches.

```css
/* Local fade behind left-aligned hero copy; the right side of the photo stays untouched */
.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgb(8 10 14 / 0.55) 0%, rgb(8 10 14 / 0) 55%);
}
```
- **Why:** the image stays vivid and the words stay legible; boxes and halos trade one for the other.
- **Check:** no hard edge shows around the text area, the far side keeps its original brightness, and COLOR-11
  passes.

## Shadows and depth

### COLOR-13 · Keep shadows faint, broad, and close
Prefer flat surfaces or a subtle lift. When a shadow is needed, keep it within these limits:
- Opacity about 4–12% black.
- Blur 16–48 px.
- Vertical offset 2–12 px, horizontal offset 0.
- Optional second tight layer for contact: 1 px offset, 1–3 px blur.

Forbidden: hard offset blocks, crisp cast edges, dark heavy rims, and shadows on text. Glass, tactile, and
collage styles follow the same limits.

```css
/* Do: broad and faint, with a tight contact layer */
.panel-raised {
  box-shadow:
    0 1px 2px rgb(0 0 0 / 0.06),
    0 8px 24px rgb(0 0 0 / 0.08);
}

/* Avoid: hard offset block, sharp dark cast with a heavy rim, shadowed text */
.panel-bad   { box-shadow: 6px 6px 0 #000; }
.popover-bad { box-shadow: 0 4px 4px rgb(0 0 0 / 0.45), inset 0 0 0 2px rgb(0 0 0 / 0.6); }
.title-bad   { text-shadow: 0 2px 3px rgb(0 0 0 / 0.6); }
```
- **Why:** harsh shadows add weight and noise without adding information.
- **Check:** every shadow layer is at or below 12% opacity, the main layer has 16–48 px blur and 2–12 px
  offset, and no text carries a shadow.

### COLOR-14 · Never signal state with depth alone
Selected, disabled, active, and error states each need a color change, an icon, or text in addition to any
shadow or lift. A card may rise on hover as feedback, but selection must stay visible after the pointer
leaves.
- **Why:** a soft shadow is too faint to read reliably and nearly vanishes in dark themes.
- **Check:** strip every shadow from the render; each state is still identifiable.

## Gradients

### COLOR-15 · Give every gradient a physical or brand reason
A gradient models a light source, describes volume, or carries a documented brand ramp. Without one of those
reasons, use a flat fill. Skip the default purple-to-blue sweep and rainbow meshes. Keep text away from busy
stops and verify it per COLOR-11.
- **Why:** an unmotivated gradient is decoration that reads as a template.
- **Check:** state each gradient's reason in one phrase; if you cannot, make it flat.

## Dark mode

### COLOR-16 · Design dark mode as a separate palette
Do not invert the light theme or swap only the ground. Redefine every role from COLOR-1 for the dark context,
then test both themes on the same screens.
- **Why:** inverted palettes produce glaring accents, muddy surfaces, and broken contrast.
- **Check:** the dark theme defines its own value for every role token.

### COLOR-17 · Raise dark surfaces by making them lighter
Each step up in depth gets a lighter surface instead of a larger shadow. Example ramp: ground `#0E1014`,
surface `#161920`, raised surface `#1E222A`, overlay `#262B34`. Floating layers may keep a shadow, but it
cannot be what separates them.
- **Why:** shadows barely register on a dark ground, while lightness steps do.
- **Check:** each depth level is visibly lighter than the level beneath it.

### COLOR-18 · Keep body text off pure white on a black ground
For most dark themes use a ground around `#0B0D10`–`#121212`. A deliberate monochrome direction (black and
white photography, archetypes/monochrome-stage.md) may use true `#000000` as the ground. Either way, pure
white is for display type, icons, and the primary button; set body text near 80–90% white (`#C9C9C9` to
`#E6E6E6`) and secondary text around 55% (`#8F8F8F`).
- **Why:** maximum contrast on long text causes glare and a smeared halo; on big headlines it gives punch.
- **Check:** paragraphs are not `#FFFFFF`, and secondary text still passes 4.5:1 on the ground.

### COLOR-19 · Desaturate accents slightly for dark themes
Lower the accent's saturation a little and raise its lightness so it does not vibrate against the dark
ground. Adjust status hues the same way, then recheck COLOR-10 for text on and around them.
- **Why:** fully saturated hues glow on dark grounds and pull the eye away from content.
- **Check:** the dark accent is a lighter, calmer version of the light one and still passes with
  `--primary-foreground`.

## Charts

### COLOR-20 · Chart with one highlight and a colorblind-safe palette
Draw most series in neutrals and give the single highlight color to the key series or data point. When several
categories need distinct hues, use a palette tested for color vision deficiency, and never separate series by
red versus green alone; add direct labels, markers, or patterns. Chart structure lives in
`guides/dashboard-and-tables.md`.
- **Why:** one highlight tells the reader where to look; a rainbow tells them nothing.
- **Check:** under a deuteranopia and protanopia simulation every series stays distinct, and one element holds
  the highlight.
