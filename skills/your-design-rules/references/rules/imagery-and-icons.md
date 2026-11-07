# Imagery and icons

How to decide what kind of visual a spot needs, then how to source it well: icons, stock photos, generated
images, vector artwork, and edits to existing images. Read it before you add any visual to a screen, and again
before you write an image prompt or a stock query. Contrast and treatment for text over images live in
`references/rules/color.md`.

## Choosing a source

### IMG-1 · Pick every visual's source from this tree
Walk the branches in order and stop at the first one that fits.
1. **Interface glyph** such as a chevron, arrow, check, close, or navigation symbol: take it from an icon
   library (Lucide, Heroicons, Phosphor, Material Symbols, or SF Symbols). Follow IMG-3.
2. **Real-world subject** such as a person, place, product, texture, avatar, or hero backdrop: use a stock
   photo. Generate an image only when the scene is specific and imagined and stock cannot supply it.
3. **Decoration or data** such as pills, badges, glows, blobs, dividers, background gradients, abstract
   patterns, and charts: draw it with CSS, native shapes, gradients, and layout; it needs no image file.
4. **Custom artwork** (a logo, mascot, diagram, or bespoke illustration) that icons, shapes, and photos
   cannot assemble: request an SVG from a vector generator or use a designer's file, and only when the
   artwork is the point. That means the user requested it, the brand has no mark and needs one, or a custom
   illustration carries a section.
5. **Existing project artwork:** use what is there. Look for it before acting on branches 2–4.

- **Why:** the lightest source that does the job keeps the design editable, consistent, and fast to change.
- **Check:** for each visual, name the branch it came from; none came from a heavier branch than needed.

### IMG-2 · Resolve common needs with this lookup

| Need | Use | Never |
|---|---|---|
| Close, menu, chevron, search | An icon from the product's one library | Hand-drawn paths, emoji, a second icon set |
| Status pill or badge | Text in a styled container using tokens | An image of a badge |
| Glow, blob, or soft background | A CSS radial gradient or a blurred shape | A generated raster |
| Divider or abstract pattern | A border, a CSS gradient, a repeated shape | An image file |
| Chart or graph | A chart library or SVG built from the data | A generated image or hand-placed dots |
| Diagram | Editable shapes, text, and connectors | A raster of a diagram |
| Product interface | Real UI built as elements (see `references/rules/core.md`) | A screenshot or generated picture of UI |
| Team member or customer | A supplied photo, or a labeled placeholder | A generated face presented as a real person |
| Place, object, or texture | A supplied or stock photo | A guessed URL (IMG-12) |
| Specific imagined scene | A generated image prompted per IMG-9 | A loosely related stock photo |
| Logo the brand already has | The project's existing file | Redrawing or regenerating it |
| Logo the brand lacks | A vector generator or a designer asset | A mark hand-built from primitives |

- **Why:** most visual mistakes come from reaching for a heavier source than the need requires.
- **Check:** no visual in the build matches an entry in the Never column.

## Icons

### IMG-3 · Use one icon library at consistent sizes
Choose one library per product and stay with it. Size icons at 16, 20, or 24 px and keep one stroke weight.

| Size | Typical use |
|---|---|
| 16 px | Inline with 13–14 px text, dense tables, input adornments |
| 20 px | Buttons, menus, sidebar navigation with 14–16 px labels |
| 24 px | Toolbars, tab bars, standalone icon buttons |

Use the outline style by default; the filled variant may mark the selected state. Color icons with text
tokens, and give any icon that carries meaning 3:1 contrast (see `references/rules/color.md`).
- **Why:** mixed libraries, sizes, and strokes make an interface look patched together.
- **Check:** every icon comes from the same library, measures 16, 20, or 24 px, and shares one stroke weight.

### IMG-4 · Keep text labels on navigation and actions
Icons support labels; they do not replace the ones a user needs. Only universally understood glyphs (search,
close, menu) may stand alone. Every icon-only button has an accessible name, such as `aria-label="Close"`.
- **Why:** most icons are ambiguous without a word, and people hesitate over controls they cannot name.
- **Check:** every icon shown without visible text is search, close, or menu, and has an accessible name.

### IMG-5 · Never hand-draw artwork from raw SVG paths
Do not assemble logos, mascots, or illustrations from hand-written paths, circles, and polygons. Use a
vector generator or a designer asset per IMG-1 branch 4, or leave the artwork out; most designs need none.
Simple decorative shapes from branch 3, such as a ring or a blob, are fine.
- **Why:** hand-assembled drawings look amateur and undercut an otherwise careful design.
- **Check:** no SVG in the build depicts a figure, object, or mark unless a generator, a designer, or the
  project supplied it.

## Generated art

### IMG-6 · Budget generated art: one asset, many placements
Build and review the layout without artwork first. Then generate only the images the design needs, turn each
into a reusable component, and place instances of it. Do not generate a variant per section or per card.
- **Why:** adding one image later is cheap; removing a dozen mismatched ones is not.
- **Check:** each generated asset has a stated purpose, and none exists only to fill a card.

### IMG-7 · Art-direct each image before you source it
Write these notes for every image, stock or generated:
1. **Role:** the job it does in the section's story.
2. **Subject:** what is literally in the frame.
3. **Viewpoint:** camera height, angle, and distance.
4. **Light:** direction, quality, and time of day.
5. **Materials:** the surfaces and textures that must read.
6. **Crop:** aspect ratio and where the subject sits.
7. **Quiet regions:** where type will go.

- **Why:** an image picked without direction rarely fits the layout or the message.
- **Check:** each image has all seven notes, and the chosen asset matches them.

### IMG-8 · Tell the generator everything; it cannot see the page
An image generation tool knows only its prompt. Spell out the subject, composition, and style (line, flat
fill, or photographic), then the palette, light, viewpoint, crop, and the location of the calm region reserved
for text. Put one subject in each prompt and ask for one image, not a set of variants. Exclude text, lettering, logos, and watermarks;
real words belong in the layout.
- **Why:** a vague prompt returns a generic picture that fights the palette and the composition.
- **Check:** the prompt fills every field of the IMG-9 template.

### IMG-9 · Write image prompts from this template

```text
Subject:    <one literal subject and what it is doing>
Role:       <the job this image does in the section>
Viewpoint:  <camera height, angle, distance, lens feel>
Light:      <source direction, quality, time of day>
Materials:  <surfaces and textures that must read clearly>
Palette:    <colors tied to the design tokens; what stays neutral>
Crop:       <aspect ratio, subject position, safe area for other crops>
Quiet area: <where the type sits and how calm that region must be>
Style:      <photographic, flat fill, or line; finish; exclusions>
```

Worked example, a hero for a neighborhood tool library's membership page:

```text
Subject:    a member lifting a cordless drill off a pegboard wall of hand tools
Role:       hero background showing the outcome: borrowing a tool instead of buying one
Viewpoint:  eye level, three-quarter angle, medium distance, 35 mm feel
Light:      soft daylight from a high window on the right, gentle falloff to the left
Materials:  perforated hardboard, worn steel, rubber grips, a denim work apron
Palette:    cool grays and slate blue; the drill body is teal to echo --primary
Crop:       16:9, member in the right third; a 4:5 crop around the member must also work on mobile
Quiet area: the left 40% is plain wall in soft shade, behind the headline
Style:      documentary photograph, natural color, shallow depth of field; no text, logos, or watermark
```
- **Why:** a fixed template keeps every prompt complete and every image consistent with the system.
- **Check:** all nine fields hold concrete words, not filler adjectives like "modern" or "clean".

### IMG-10 · Wait for generated assets before judging them
Generation often completes after the request returns, and a failure can be silent. Confirm the file exists,
loads, and has the expected dimensions before you screenshot, review, or build around it.
- **Why:** reviewing a section with a missing image hides layout problems and reports false success.
- **Check:** every generated image in the render is the real asset, not a broken link or an empty frame.

## Stock and sourcing

### IMG-11 · Query stock with one to three concrete nouns
Search for what the camera would see, not for the idea or the page slot.

| Do | Avoid |
|---|---|
| `tide pool` | `nature wellness concept` |
| `bike mechanic` | `hero image for fintech app` |
| `harbor fog` | `teamwork success` |
| `pottery wheel` | `happy diverse people using app` |

Run several narrow queries rather than one broad one, then choose against the notes from IMG-7.
- **Why:** stock libraries index what is visible, so abstract words return the most generic results.
- **Check:** every query is one to three nouns that name visible things.

### IMG-12 · Never guess or invent image URLs
An image URL must come from a tool result or from the user; never assemble a plausible one from memory or a
pattern. Without a real source, use a labeled placeholder: a neutral block at the final aspect ratio captioned
like "Photo: harbor at dawn". Report missing or placeholder images to the user in your reply, never inside the
product UI.
- **Why:** a guessed URL breaks in production or shows someone else's picture.
- **Check:** every image URL in the build traces to a tool result, a user message, or the project's files.

## Editing existing images

### IMG-13 · Remove a background only when the subject leaves its frame
Cut the subject out when it must sit directly on the design's own ground, overlap two sections, or break out
of its container. Otherwise keep the photo whole.
- **Why:** a cut-out loses its context and light, so it needs a compositional reason.
- **Check:** each cut-out sits on a design ground, crosses a section edge, or extends past its frame, with no
  halo of the old background.

### IMG-14 · Replace backgrounds to fix a setting or unify a set
Swap the background when the subject works but its surroundings do not, or when several stock photos need one
shared setting. Describe only the new setting in the prompt: the surface, the light, and colors drawn from the
palette. Do not describe the subject again.
- **Why:** restating the subject invites the generator to alter it.
- **Check:** subjects are unchanged, and every replaced background shares one light direction and palette.

### IMG-15 · Vectorize only flat, high-contrast art
Trace to vector only artwork that already has flat fills and hard edges, such as a scanned mark or a two-color
sketch. Never vectorize photographs, and never generate a raster only to trace it; request vector output from a
vector generator instead.
- **Why:** tracing tonal images yields blotchy, heavy files that look worse than the source.
- **Check:** every traced asset started as flat art with a handful of solid colors.

## Placement and cropping

### IMG-16 · Never stretch or distort an image
Fill frames with a cover fit and a deliberate focal point. On narrow screens, recompose the crop instead of
shrinking the desktop one.

```css
.media { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; object-position: 70% 40%; }
@media (max-width: 600px) { .media { aspect-ratio: 4 / 5; object-position: 75% 50%; } }
```
SwiftUI: `.scaledToFill()` with `.clipped()`. Flutter: `BoxFit.cover` with an `alignment`.
- **Why:** squashed people and products are noticed instantly and read as broken.
- **Check:** at 375, 768, and 1440 px every image keeps its native proportions and its subject in frame.

### IMG-17 · Reuse one strong scene through different crops
When a page needs several images, crop one strong scene at different scales (a wide view, a detail, a
texture) before adding unrelated thumbnails.
- **Why:** one scene seen several ways feels intentional; unrelated thumbnails feel like filler.
- **Check:** the images on a page share a subject, setting, or light, and none fills a slot by itself.

### IMG-18 · Show the outcome, not a floating screenshot
On landing pages, picture people in the improved state the product creates. Avoid a lone product screenshot
hovering on a gradient. The exception is a product-led direction where the real interface is the argument,
built as real elements. Hero composition lives in `references/rules/layout.md` and `references/guides/landing-page.md`.
- **Why:** visitors respond to the result they want, not to a picture of a tool.
- **Check:** the hero image answers "what does life look like after this product?"

### IMG-19 · Tie every illustration to the content
Illustrations, doodles, and spot art depict something the section actually says. Delete any that only fill
space.
- **Why:** filler art dilutes the message and signals a template.
- **Check:** for each illustration, you can point to the sentence or data point it refers to.

## Treatments

### IMG-20 · Apply image treatments only for a stated purpose
Duotone, halftone, dithering, noir, film grading, selective color, and shader effects are optional. Use one
when it does a job, such as unifying mismatched photos or marking archival material. Never apply a treatment
over working text or UI, and never use one to rescue an image that lacked art direction (IMG-7). Recheck text
contrast afterward (see `references/rules/color.md`).
- **Why:** a treatment without a purpose is decoration, and over UI it hurts legibility.
- **Check:** each treated image has a one-phrase reason, and no control or text layer carries the effect.

## Alt text

### IMG-21 · Write alt text that states the image's role
Say what the image contributes in this context, in one short sentence, without opening with "image of".
Decorative images get an empty alt (`alt=""`) or the platform setting that hides them from assistive
technology.

**Do:** `alt="Member taking a drill from the tool library wall"`

**Avoid:** `alt="hero image"`, `alt="photo123.jpg"`, or descriptive alt text on a background blob.

- **Why:** screen reader users need the image's meaning, and decorative noise slows them down.
- **Check:** every content image has a specific alt, and every decorative image has an empty one.

### IMG-22 · Explore several candidates for the key visual, then keep one
The budget in IMG-6 applies to supporting images. For the one key visual that carries the page (a website
hero, a campaign image, an app's empty-state illustration), write three or four prompts that differ in
composition, viewpoint, or style, generate all of them, compare them at the size they will be shown, and keep
the single strongest. Judge on: a clear subject, a mood that matches the plan, room for the headline, and a
palette the interface can borrow from. Delete the rest; never ship two near-identical versions.
- **Why:** the first generation is rarely the best one, and the key visual is where extra attempts pay off.
- **Check:** you can name the candidates you rejected and why the kept one won.

