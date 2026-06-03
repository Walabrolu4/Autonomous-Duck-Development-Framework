# Sprint 005: Website MVP — Requirements

## 1. Goal
Build the first public version of the ADDF website (v0.2). Deliver a static site that establishes the framework's visual identity, provides the first-session onboarding guide, and serves the downloadable starter kit and prompts.

## 2. Context
Per `planning/backlog.md`, Sprint 005 builds the core public website. Sprint 004 established the site map and page blueprints. Decision 003 mandates a static-first approach. Decision 009 requires a framework that supports future interactive islands (Astro). Decision 011 establishes the PNG logo as the interim visual asset.

## 3. Scope
**In scope:**
- Astro configuration for pure static site generation.
- Implementation of the global layout (header, footer, navigation).
- Implementation of the Homepage (`/`).
- Implementation of the Start Here page (`/start-here`).
- Implementation of the Downloads page (`/downloads`).
- Integration of the interim PNG logo.
- Strict adherence to `STYLE_GUIDE.md` for colors (Yolk, Ink, Paper), typography (Instrument Serif, Space Grotesk, JetBrains Mono), and voice (declarative, concrete).

**Out of scope:**
- Documentation pages (`/docs/*`). These belong to Sprint 006.
- The web onboarding app (`/onboarding`). This belongs to v0.4.
- Any backend logic, databases, or API integrations.
- Vector logo production.

## 4. References
- `STYLE_GUIDE.md`
- `docs/site-map.md`
- `docs/page-blueprints.md`
- `website/README.md`
- `DECISIONS.md` (Decisions 003, 009, 011)
