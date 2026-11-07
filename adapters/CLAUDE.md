<!-- your-design-rules:start -->
<!-- Paste this block into your project's CLAUDE.md if you use Claude Code without the plugin. Copy rules/, guides/, and archetypes/ from the YourDesignRules repo into a design-rules/ folder at your project root, or change the paths below. -->
## Design rules

When you create or restyle any UI (web page, app screen, dashboard, table, form, mobile screen, slides),
follow the design rulebook in `design-rules/`:

1. Read `design-rules/rules/core.md` first.
2. Read the guide for the task: `design-rules/guides/web-app.md`, `landing-page.md`, `mobile-app.md`,
   `dashboard-and-tables.md`, or `slides.md`.
3. No brand or style given? Pick one archetype from `design-rules/archetypes/README.md`, say which and why,
   and read its file. User-specified fonts and colors always win.
4. Consult `design-rules/rules/layout.md`, `typography.md`, `color.md`, and `imagery-and-icons.md` as
   decisions come up.
5. Build section by section. After each section, render it and run `design-rules/rules/review-checklist.md`
   on the actual render. Fix in place.

Non-negotiables: one primary action and one dominant region per view; no card-wrapping without a job;
effects only on purpose, shadows soft; no beige/cream/ivory/tan backgrounds; accent only for actions;
no invented data, logos, testimonials, or image URLs; UI built from real elements; check every render.
<!-- your-design-rules:end -->
