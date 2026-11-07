# Frosted Depth
> Translucent layers float in front of a solid reading plane, so the interface gains optical depth without giving up legibility.

## When to pick

- AI assistants, creative and media tools, spatial or 3D products, music apps, wallets that want to feel calm.
- There is a strong central object (a render, a device, a material) that can sit behind or below the glass.
- The target platform already uses translucency in its system chrome, so matching it feels native.
- Skip it for dense back-office tools where nearly every surface carries data.

## Composition

- Think in three planes: the field (ground plus object), the reading plane (opaque content surfaces), and glass.
  Only the third plane is translucent.
- Glass is for supporting surfaces: the nav bar, a floating toolbar, a popover, a player control. Reading text,
  forms, and tables sit on the opaque plane.
- Give the central object open space on every side, so the blur behind the glass shows a real shape shifting in
  color rather than gray noise.
- Website hero: one object with generous space around it fills the stage, the statement sits in the open field
  on the same ground, and a glass nav floats above both, forming one continuous stage. This applies to the site
  opening only; see rules/layout.md.
- Layer order is always obvious: glass sits above content, and glass never stacks on glass.
- In product UI, the working area is opaque. Glass is limited to the toolbar, a floating inspector, or the
  command palette.

## Typography

| Role | Family | Weights |
|---|---|---|
| Display, headings | Red Hat Display | 500, 600, 700 |
| Body, UI, labels | Instrument Sans | 400, 500, 600 |

- Display at 56–96 px on desktop and 40–52 px on phones; line height 1.0–1.1; tracking −2%.
- Body at 16 px, line height 1.5. UI labels at 13–14 px, weight 500.
- On glass, set any text under 16 px at weight 500 or heavier so its strokes hold up against a moving background.
- Load from Google Fonts: Red Hat Display, Instrument Sans.

## Color roles

Light, cool example. It is a starting point; swap it for brand colors when they exist (CORE-13). A dark
variant uses a ground near `#0D1220`, reading surfaces near `#151B2B`, glass of that surface color at about
70%, and the same accent.

| Role | Example | Use |
|---|---|---|
| Ground | `#E8EDF4` | The field behind everything |
| Reading surface | `#FFFFFF` | Opaque panels for text, forms, data |
| Glass | `#FFFFFF` at 62% with 24 px blur | Nav, floating controls; solid fallback `#F7F9FC` |
| Text primary | `#0E1726` | Headlines, body |
| Text secondary | `#3D4A5C` | Supporting copy |
| Text muted | `#5A6678` | Captions, metadata |
| Text inverse | `#FFFFFF` | Text on the accent |
| Accent | `#2F5BEA` | Primary action, selection |
| Boundary | `#C9D3E0` | Hairlines; input outlines use `#7D8899` |
| Status | success `#1A7A4C`, warning `#A86400`, error `#C93636`, info `#0E7C9A` | Always with a label or icon |

- The object behind the glass supplies the color. Keep the ground itself calm and nearly flat.
- Measure contrast on the composite: text on glass over the lightest and the darkest content that can scroll
  behind it. If either fails, raise the glass opacity or move the text to the opaque plane.

## Shape and elevation

- Radius 12 px on controls and small popovers, 16 px on panels, 24 px on large sheets. Nested corners use the
  outer radius minus the padding.
- Glass and floating panels get a medium soft shadow, for example `0 8px 24px rgba(14,23,38,0.08)`, plus a 1 px
  inner edge of white at about 70%. The opaque reading plane stays flat. Limits are in rules/color.md.
- Keep blur between 16 and 32 px. Beyond that the layer reads as fog.
- Ship the solid fallback for browsers without backdrop blur and for users who ask for reduced transparency.

```css
.glass { background: rgb(255 255 255 / 0.62); backdrop-filter: blur(24px); }
@supports not (backdrop-filter: blur(1px)) { .glass { background: #F7F9FC; } }
@media (prefers-reduced-transparency: reduce) { .glass { background: #F7F9FC; backdrop-filter: none; } }
```

## Motion
- Glass layers enter by fading and sharpening (opacity plus a small 8–12 px translate); never animate `backdrop-filter` values.
- Floating controls lift 2 px on hover; the reading plane never moves.
- Provide a solid-surface fallback with no blur under reduced transparency or reduced motion.
- Timing, easing, and reduced-motion rules: rules/motion.md.

## Imagery

- One central object with real form and light that still reads through blur: a 3D render, a device, glass,
  liquid, fabric, a plant.
- Keep one light direction across renders and photos. Soft highlights on the glass edge should agree with it.
- Cut the object out and place it on the ground, or photograph it against a matching background.
- Icons: one rounded outline set (Lucide or Phosphor) at 20 px in toolbars, filled variant for the selected item.
- Color behind glass comes from the object or the content, never from floating orbs or blurred blobs added as
  filler.

## Avoid

- Glass under primary reading text, tables, charts, or long forms.
- Glass stacked on glass, or more than two translucent layers on one screen.
- Rainbow mesh backgrounds and the default purple-to-blue gradient.
- Contrast checked only on a flat mockup instead of the real composite.
- White text on light glass.
- Blur above 32 px, or several shadows on one layer.
- Any glass surface without its solid fallback.
- Universal rules still apply: CORE-4 to CORE-8 in rules/core.md, plus rules/color.md and
  rules/review-checklist.md.

## In apps vs. on websites

- Websites: the hero object and a glass nav, then sections that alternate opaque reading bands with one more view
  of the object. Glass appears once or twice per page.
- Apps: the content area is opaque white. Glass is reserved for the top bar, a floating toolbar, and the command
  palette. Dense tables, editors, and charts always sit on an opaque backplate.
- Phones: a translucent tab bar and sheet chrome match the platform; the content inside a sheet stays opaque.
