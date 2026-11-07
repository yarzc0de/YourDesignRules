---
name: your-design-rules
description: Design rulebook for building interfaces that look designed, not generated. Use it whenever you create or restyle any UI — a landing page, marketing site, web app screen, admin panel, dashboard, data table, form, mobile app screen, or slide deck — in HTML/CSS, React/Tailwind, Vue, SwiftUI, Flutter, or a design tool. Also use it when the user asks to make a UI "look better", "more professional", "less generic", or "less like AI made it", when choosing fonts, colors, spacing, icons, or images for a UI, and when the user has no brand and needs a visual direction.
---

# Your Design Rules

A set of short, testable rules for layout, typography, color, imagery, and review, plus task guides and 16
visual archetypes. The rules exist because AI-built UI fails in predictable ways: everything wrapped in
cards, equal-weight sections, default gradients and shadows, beige backgrounds, invented metrics, text that
clips, and no one checking the render. Following the workflow below avoids those failures.

All paths below are relative to this skill's folder.

## Workflow

1. **Read the core.** Always read `references/rules/core.md` first. It is short and every other file builds
   on it.
2. **Pick the task guide.** Read the one that matches the job:

   | Building | Read |
   |---|---|
   | Product UI, admin, editor, settings, CRUD | `references/guides/web-app.md` |
   | Marketing site, landing page, product page | `references/guides/landing-page.md` |
   | Phone or tablet app screens | `references/guides/mobile-app.md` |
   | Dashboards, metrics, charts, data tables | `references/guides/dashboard-and-tables.md` |
   | Presentations | `references/guides/slides.md` |

3. **Settle the visual direction.**
   - If the user gave a brand, style guide, existing design system, or explicit fonts/colors, use those and
     skip archetypes. User choices always win (CORE-13).
   - If not, read `references/archetypes/README.md`, pick one archetype that fits the product and audience,
     tell the user which one and why in one sentence, then read that archetype's file.
4. **Write a design plan before any code** (CORE-23, CORE-24): what the subject's world looks like, a 4–6
   color palette with roles, type families and sizes, a sentence per section plus an ASCII sketch of the
   first screen, and the one bold decision (CORE-8). Run the sameness test and change anything a competitor's
   page would share. Show the plan to the user in a few lines, then build.
5. **Read the rule files you need** as decisions come up:
   - spacing, grids, hero composition, responsive behavior → `references/rules/layout.md`
   - fonts, sizes, line length, numerals → `references/rules/typography.md`
   - palette roles, contrast, banned backgrounds, shadows, dark mode → `references/rules/color.md`
   - icons vs. photos vs. generated images vs. SVG, image prompts → `references/rules/imagery-and-icons.md`
   - transitions, hover/press/focus states, loading, scroll effects → `references/rules/motion.md`
6. **Build section by section.** After each section, render it and run `references/rules/review-checklist.md`
   on the actual render (screenshot, browser, simulator). Fix problems in place before moving on (CORE-15,
   CORE-16).
7. **Finish with the whole-screen checks** in the checklist: breakpoints 375/768/1440, rhythm, reduction pass,
   keyboard and focus. Tell the user about anything you could not verify or had to assume.

## The rules that matter most

If you remember nothing else:

- One job, one primary action, one dominant region per view.
- Don't put every element in a card. A container needs a job.
- No rows of equal boxes with a label and a one-line caption (audience strips, feature trios, 01/02/03
  steps). Say it in the copy, show it in an image, or rank the items (CORE-21).
- Effects (gradients, shadows, big radii, glow, glass) only on purpose. Shadows soft and diffuse, never hard.
- No beige, cream, ivory, tan, or warm off-white backgrounds.
- Accent color is for actions and selection, not decoration.
- Use real content. Never invent metrics, logos, testimonials, or image URLs.
- Build UI as real elements, never as images of UI. Never hand-draw logos from SVG paths.
- Motion only with a job: 150–350 ms, ease-out curves, transform and opacity only, reduced motion respected.
- Clean is the floor, not the goal: one bold decision per page, taken from the subject's world (CORE-8,
  CORE-23), and none of the house styles generators default to (CORE-25).
- Check the render after every section, and fix in place.

## When the user only wants a small change

If the request is a specific edit (move this, recolor that, remove a section), make exactly that change
(CORE-18). Mention other issues you noticed in your reply instead of fixing them unasked.
