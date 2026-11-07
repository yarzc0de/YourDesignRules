# Wide Horizon
> Large photographs of a real place and tall condensed capitals put the visitor inside one scene that returns at different scales down the page.

## When to pick

- Travel, tourism boards, parks, outdoor gear, hotels sold by their setting, real estate, and architecture.
- The client has, or can license, strong photography of a specific location, route, or building.
- The mood is open air and scale: distance, weather, light, the height of a room or a ridge.
- Skip it when there is no credible scene to show. A skyline that could be any city undermines the whole direction.

## Composition

- Choose one anchor scene and bring it back: full bleed at the top, a tight detail crop next to the booking form,
  a narrow strip above the footer. One place seen several ways reads as a story; ten unrelated photos read as a
  catalog.
- Website hero: the photograph fills the stage edge to edge and the condensed headline sits inside a calm region
  of that same frame (sky, water, a plain wall), so picture and statement form one continuous stage. This
  applies to the site opening only; see rules/layout.md.
- Pick the crop before writing the headline. If the calm region is too busy, recrop or choose another frame
  rather than darkening the photo.
- Alternate scene sections with plain sections of short reading text so the page has room to breathe.
- Floating panels (search, dates, filters) may sit over a photo. Anchor them to an edge or the lower third, keep
  them compact, and never place them over the subject.
- Oversized faint words behind content are texture only. Anything a reader needs appears as real text at full
  contrast.
- In product UI, the scene shrinks to a header band or one detail image per record (a listing, a trail, a
  property). Lists, forms, and maps stay on the plain ground.

## Typography

| Role | Family | Weights |
|---|---|---|
| Display, section heads, short labels | Oswald | 500, 600, 700 |
| Body, UI, forms, captions | Hanken Grotesk | 400, 500, 600 |

- Display in capitals at 80–144 px on desktop and 48–64 px on phones; line height 0.95–1.0; tracking 0 to +1%,
  because condensed capitals crowd quickly when tightened.
- Two to four words per headline line. The narrow face lets a long place name fit without shrinking it.
- Body stays sentence case in Hanken Grotesk: 17–18 px on websites, 15–16 px in apps.
- Eyebrows and small labels: Oswald 500, capitals, 13–14 px, +6% tracking. Prices, dates, and distances use
  Hanken Grotesk with tabular figures.
- Load from Google Fonts: Oswald, Hanken Grotesk.

## Color roles

Dark example, tuned for dusk and night photography. Treat it as a starting point and replace it when the brand
or the photographs point elsewhere (CORE-13).

| Role | Example | Use |
|---|---|---|
| Ground | `#0F1417` | Page background between scenes |
| Surface | `#182024` | Panels, forms, menus |
| Surface raised | `#222C31` | Floating panels, popovers |
| Text primary | `#E9EEF1` | Headlines, body |
| Text secondary | `#AEB9BF` | Supporting copy |
| Text muted | `#84919A` | Captions, credits, metadata |
| Text inverse | `#1A0E06` | Text on the accent |
| Accent | `#F08A4B` | Primary action, selected filter or date |
| Boundary | `#2E3A40` | Hairlines; input outlines use `#5E6B73` |
| Status | success `#5BC48D`, warning `#E9C55A`, error `#F2706A`, info `#6CB4E6` | Always with a label or icon |

- The photographs supply most of the color. Take the accent from a hue already in the anchor scene (low sun, a
  painted door, a jacket) so the action and the image agree.
- A light variant uses a white ground, dark slate text, and the accent darkened until white text on it reaches
  4.5:1.

## Shape and elevation

- Radius 0 on photographs and full-bleed sections, 6 px on panels and inputs. Buttons and filter chips are either
  full pills or 6 px; choose one for the whole product.
- Panels floating over photographs get one large soft shadow, for example `0 12px 40px rgba(0,0,0,0.18)`.
  Content in the normal flow stays flat. Limits are in rules/color.md.
- Floating panels use the opaque surface color, not glass, so form text never competes with the scene.
- Where text sits on the photo, add a soft gradient from the nearest edge that fades out past the text block.
  The rest of the frame stays untouched.

## Motion
- The hero photo may drift very slightly (scale 1.0 → 1.04 over 10–15 s, once) or crossfade between crops of the same scene; never a looping slideshow without pause.
- Condensed headlines fade up 16 px once; no letter animation.
- Parallax only on one background image at 0.85× speed, if at all (MOTION-21).
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery

- Literal scenes: a named place, a time of day, real weather. If the brand sells a location, show that location.
- Stock searches use concrete nouns: "fjord ferry", "desert trailhead", "loft staircase".
- One anchor scene in several crops beats many thumbnails. Cut-out details (a tent, a chair) may sit on the
  plain ground.
- People appear small in the frame to give scale, not posed toward the camera.
- Recrop for portrait screens around the subject instead of scaling the landscape frame down.
- Icons: one thin outline set at 20–24 px. Maps and routes are real map components, not pictures of maps.

## Avoid

- Generic drone shots, skylines of nowhere, or mixed seasons and locations with no narrative reason.
- A uniform dark overlay across a whole photo, or heavy shadows behind text.
- Condensed capitals for paragraphs, form labels, or instructions.
- A hero split into a headline column beside a boxed photo.
- Background words that carry information such as dates, prices, or names.
- A carousel of unrelated photos standing in for the story.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/imagery-and-icons.md,
  rules/color.md, and rules/review-checklist.md.

## In apps vs. on websites

- Websites: the scene leads. Full-bleed sections, display type at full scale, and scene sections alternating with
  plain reading sections.
- Apps (booking, listings, trip planning): one header image per record or detail view. Oswald for screen titles
  and section labels only; everything else in Hanken Grotesk on the plain ground.
- Search, booking, and checkout controls stay opaque, upright, and in the normal flow.
- On phones, show at most one photograph per screen and keep the primary action below it, within thumb reach.
