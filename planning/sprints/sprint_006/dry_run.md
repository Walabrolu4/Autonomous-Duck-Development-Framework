# Sprint 006: Documentation Pages — Dry Run

**Mode:** Develop Mode (Permission Level 0)  
**Date:** 2026-06-03

## 1. Files to create
- `website/src/layouts/DocsLayout.astro`
- `website/src/pages/docs/framework.astro`
- `website/src/pages/docs/scale-model.astro`
- `website/src/pages/docs/lifecycle.astro`
- `website/src/pages/docs/modes.astro`
- `website/src/pages/docs/project-brain.astro`
- `website/src/pages/docs/starter-kit.astro`
- `website/src/pages/docs/prompt-catalog.astro`
- `website/src/pages/docs/examples.astro`

## 2. Files to modify
- `website/src/layouts/Layout.astro` (To activate `Framework` and `Lifecycle` header links)

## 3. Files to move or delete
- No files to move or delete. 

## 4. Commands to run
- `New-Item -ItemType Directory -Force -Path "website\public\images"` (to hold the documentation images)
- `Copy-Item -Path "docs\_PDF\images\*" -Destination "website\public\images\" -Recurse` (to make the assets available to the Astro build)
- `npm run build` (inside `website/` to verify static generation)

## 5. Dependencies requested
- None. Astro is already installed and configured from Sprint 005.

## 6. Risks
- **Asset pathing:** The images currently reside in `docs/_PDF/images/`. Astro requires static assets to be in `website/public/` or imported directly. Copying them to `website/public/images/` is necessary to ensure they resolve properly when deployed.
- **Markdown Conversion:** Converting complex markdown (like tables in `DOMAIN.md` or `STYLE_GUIDE.md`) to Astro components could lead to CSS styling bleed if not scoped properly.

## 7. Ambiguities
- **Image handling:** Should the images remain purely in `docs/_PDF/images/` and be imported relatively, or copied to `website/public/images/` as proposed in section 4? The public directory is the standard Astro pattern for static assets.
- **Styling constraints:** `STYLE_GUIDE.md` does not explicitly define typography for markdown tables or blockquotes. We will fallback to JetBrains Mono for tables and Space Grotesk for blockquotes if encountered.
