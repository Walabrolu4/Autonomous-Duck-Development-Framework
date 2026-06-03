# Sprint 006: Documentation Pages — Requirements

## 1. Goal
Build the core documentation pages for the ADDF website (v0.2 scope). This entails converting the framework's canonical Markdown documentation into styled Astro pages that adhere to the visual identity established in Sprint 005.

## 2. Context
Per `planning/backlog.md`, Sprint 006 builds the core documentation pages: Framework, Scale Model, Lifecycle, Modes, Project Brain, Starter Kit, Prompt Catalog, and Examples. Sprint 005 established the site's layout, CSS variables, and index page. The navigation links in `Layout.astro` that were commented out or missing must now be activated to link to these new docs.

## 3. Scope
**In scope:**
- Astro page generation for the 8 core documentation topics under `website/src/pages/docs/`.
- Implementation of a sidebar or secondary navigation system for the docs section.
- Reactivating the `Framework` and `Lifecycle` header navigation links in `Layout.astro`.
- Formatting content directly from the existing `DOMAIN.md`, `STYLE_GUIDE.md`, and `docs/` Markdown files into Astro pages.

**Out of scope:**
- Modifying the underlying framework logic or definitions.
- The web onboarding app (`/onboarding`), which belongs to v0.4.
- Adding interactive components (e.g., React/Vue islands). The site remains purely static.
- Rebuilding the homepage or downloads page.

## 4. References
- `planning/backlog.md`
- `docs/site-map.md`
- `docs/page-blueprints.md`
- `website/src/layouts/Layout.astro`
- `STYLE_GUIDE.md`
