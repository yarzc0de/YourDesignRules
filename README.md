# YourDesignRules

A design rulebook that AI coding agents load before they build UI. It works as a Claude Code plugin, a skill
for any agent that reads `SKILL.md`, and plain markdown you can point Codex, Cursor, Gemini CLI, or anything
else at.

AI-built interfaces fail in predictable ways: every element in its own card, sections of equal weight,
default gradients and heavy shadows, beige backgrounds, invented metrics and testimonials, text that clips at
narrow widths, and nobody looking at the render. These rules are written to stop those failures. Each one is
short, imperative, and testable, and comes with a one-line reason.

<!-- before/after -->
| Without the rules | With the rules |
|---|---|
| ![Landing page without the rules](examples/landing-page/before-1440.png) | ![Landing page with the rules](examples/landing-page/after-1440.png) |
| ![Dashboard without the rules](examples/dashboard/before-1440.png) | ![Dashboard with the rules](examples/dashboard/after-1440.png) |

Same prompt, same facts, same model. The left column is a plain request; the right column had the skill
active. See [`examples/`](examples/) for the HTML, phone-width renders, and the checklist results.

## What's inside

```
rules/                   universal rules, read on every UI task
  core.md                purpose, hierarchy, reduction, no card-wrapping, honest content, process
  layout.md              axes, spacing scale, density, skeletons, the hero stage, responsive behavior
  typography.md          families, scale, measure, line height, numerals, loading fonts
  color.md               color roles, contrast, banned backgrounds, shadows, dark mode, charts
  imagery-and-icons.md   icon vs. photo vs. generated image vs. SVG, image prompts, stock queries
  motion.md              durations, easing tokens, states, continuity, loading, reduced motion
  review-checklist.md    the check you run on the render after every section
guides/                  one per kind of job
  web-app.md  landing-page.md  mobile-app.md  dashboard-and-tables.md  slides.md
archetypes/              16 visual directions for when there is no brand
skills/your-design-rules the skill (SKILL.md + a synced copy of the files above)
adapters/                snippets for AGENTS.md, CLAUDE.md, GEMINI.md, and Cursor rules
examples/                before/after pages built from the same prompt
scripts/                 sync-skill.mjs, overlap-check.py
```

About 250 rules in total. Every rule has an ID (`CORE-6`, `LAY-20`, `COLOR-8`) so agents and humans can cite
them in reviews.

## Install

> The repository must be public for the remote install commands below to work.

### Claude Code

```
/plugin marketplace add yarzc0de/YourDesignRules
/plugin install your-design-rules@your-design-rules
```

The skill loads automatically when you ask for UI work. To try it from a local clone without installing:
`claude --plugin-dir /path/to/YourDesignRules`.

### Any agent that supports skills (Claude Code, Codex, Cursor, and others)

```
npx skills add yarzc0de/YourDesignRules
```

This uses the open [`skills`](https://github.com/vercel-labs/skills) installer and copies
`skills/your-design-rules/` into your agent's skills folder. The folder is self-contained.

### Codex

Install it as a Codex plugin (the manifest is in `.codex-plugin/`), or copy the files and paste
[`adapters/AGENTS.md`](adapters/AGENTS.md) into your project's `AGENTS.md`.

### Cursor

Install it as a Cursor plugin (the manifest is in `.cursor-plugin/`), or copy
[`adapters/cursor/your-design-rules.mdc`](adapters/cursor/your-design-rules.mdc) into `.cursor/rules/`.

### Gemini CLI and everything else

Copy `rules/`, `guides/`, and `archetypes/` into a `design-rules/` folder in your project, then paste the
matching snippet from [`adapters/`](adapters/) into the file your agent reads at startup (`GEMINI.md`,
`AGENTS.md`, `CLAUDE.md`).

```
git clone --depth 1 https://github.com/yarzc0de/YourDesignRules /tmp/ydr
mkdir -p design-rules && cp -r /tmp/ydr/{rules,guides,archetypes} design-rules/
cat /tmp/ydr/adapters/AGENTS.md >> AGENTS.md
```

## How an agent uses it

1. Read `rules/core.md`.
2. Read the guide for the job: web app, landing page, mobile app, dashboard, or slides.
3. If the user gave no brand, pick one archetype from `archetypes/README.md` and say which and why. User
   choices always override the archetype.
4. Open `layout.md`, `typography.md`, `color.md`, `imagery-and-icons.md`, and `motion.md` as decisions come up.
5. Build one section at a time. After each section, render it and run `rules/review-checklist.md` on the
   actual pixels. Fix in place, then move on.

## A few of the rules

| ID | Rule | Why |
|---|---|---|
| CORE-6 | Do not wrap every element in a card | Card-inside-card is the most recognizable sign of generated UI |
| CORE-21 | Don't fill space with rows of equal boxes | Label-plus-caption trios are the most common filler in generated pages |
| CORE-9 | Use real content and invent nothing | Invented proof misleads visitors and gets shipped by accident |
| LAY-20 | Compose the hero as one continuous stage | A text column beside a boxed photo reads as two weak halves |
| TYPE-7 | Set body text at 16 px, never below 14 | Small body text is the first thing readers give up on |
| COLOR-8 | Never use beige, cream, ivory, tan, or sand grounds | Warmth belongs in type, light, and photography, not a tinted canvas |
| COLOR-13 | Keep shadows faint, broad, and close | Harsh shadows add weight and noise without adding information |
| IMG-5 | Never hand-draw artwork from raw SVG paths | Hand-built logos and mascots look amateur every time |
| IMG-12 | Never guess or invent image URLs | Guessed URLs break or show the wrong picture |
| MOTION-10 | Animate transform and opacity only | They stay smooth on slow phones; layout properties stutter |
| MOTION-22 | Respect reduced motion | Motion can make people with vestibular disorders ill |
| CHK-* | Check the render after every section | Errors compound when they are found at the end |

## Archetypes

When the user has no brand, the agent picks one of 16 directions. Each sets fonts, color roles, shape,
elevation, imagery, and motion character. None of them set the page structure; that comes from the content.

| Archetype | Best for | Fonts |
|---|---|---|
| [Field Ledger](archetypes/field-ledger.md) | Infrastructure, developer tools | Titillium Web, IBM Plex Mono |
| [Night Console](archetypes/night-console.md) | Developer platforms, dark product UI | Chakra Petch, Instrument Sans, Fragment Mono |
| [Calm Utility](archetypes/calm-utility.md) | Admin tools, B2B SaaS | Manrope, Karla, Fragment Mono |
| [Civic Grid](archetypes/civic-grid.md) | Public sector, education | Schibsted Grotesk, Public Sans, Martian Mono |
| [Quiet Tiles](archetypes/quiet-tiles.md) | Consumer productivity, wellness | Bricolage Grotesque, DM Sans, IBM Plex Mono |
| [Working Surface](archetypes/working-surface.md) | Product-led SaaS | Space Grotesk, Manrope, IBM Plex Mono |
| [Studio Sketchbook](archetypes/studio-sketchbook.md) | Learning, wellness, friendly consumer apps | Fraunces, Karla |
| [Gallery Wall](archetypes/gallery-wall.md) | Fashion, hospitality, portfolios | Cormorant Infant, Karla |
| [Wide Horizon](archetypes/wide-horizon.md) | Travel, outdoor, real estate | Oswald, Hanken Grotesk |
| [Atelier Serif](archetypes/atelier-serif.md) | Luxury, craft | Bodoni Moda, Archivo |
| [Frosted Depth](archetypes/frosted-depth.md) | AI assistants, media tools | Red Hat Display, Instrument Sans |
| [Signal Color](archetypes/signal-color.md) | Campaigns, launches, events | Archivo Black, DM Sans |
| [Specimen Notes](archetypes/specimen-notes.md) | Science, health, research | Space Grotesk, Newsreader, IBM Plex Mono |
| [Ambient Glow](archetypes/ambient-glow.md) | AI products, music, creative tools | Darker Grotesque |
| [Broadsheet](archetypes/broadsheet.md) | Publications, newsrooms | Petrona, Alata |
| [Toybox](archetypes/toybox.md) | Playful consumer brands, games | Unbounded, Outfit |

All fonts are on Google Fonts.

## Contributing

- Edit the files in `rules/`, `guides/`, and `archetypes/`, never the copies in
  `skills/your-design-rules/references/`. Run `node scripts/sync-skill.mjs` afterwards; CI fails if the copies
  are stale.
- Keep the house style: an imperative title of ten words or fewer, a short body with real numbers, one
  **Why:** line, and a **Check:** line when the rule can be tested.
- If you rewrite material from another source, run `python3 scripts/overlap-check.py --source <dir>` to catch
  phrases of eight or more words that match it.

## Background

This project came out of studying how modern AI design tools structure the instructions they give their
agents. The motion rules were also informed by
[elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) (MIT). Everything here is written from scratch in our own words, is tool-agnostic, and applies equally to
HTML/CSS, React and Tailwind, SwiftUI, Flutter, and Figma.

## License

Two licenses, because the repository holds two kinds of things:

- **Rules content: [CC BY 4.0](LICENSE-CONTENT).** This covers `rules/`, `guides/`, `archetypes/`,
  `skills/`, `adapters/`, and the prose in this README. You can copy, adapt, and redistribute it, including
  commercially and inside your own prompts or products, as long as you credit "YourDesignRules" with a link.
  Creative Commons licenses are made for text; MIT is not.
- **Code: [MIT](LICENSE).** This covers `scripts/`, the plugin manifests, the CI configuration, and the HTML
  and CSS in `examples/`. MIT is the usual choice for small tooling and adds no friction to reuse.
