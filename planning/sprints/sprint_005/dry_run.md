# Sprint 005: Website MVP — Dry Run

**Permission Level:** 0 (Analysis only)  
**Status:** Awaiting human authorization

## 1. Files to create
- `website/package.json`
- `website/astro.config.mjs`
- `website/src/styles/global.css`
- `website/src/layouts/Layout.astro`
- `website/src/pages/index.astro`
- `website/src/pages/start-here.astro`
- `website/src/pages/downloads.astro`
- `website/public/logo.png` (copied from `docs/_PDF/images/duck-logo.png`)

## 2. Files to modify
- None.

## 3. Files to move or delete
- None.

## 4. Commands to run
- `mkdir -p website/src/pages website/src/styles website/src/layouts website/public`
- `cd website && npm init -y`
- `cd website && npm install astro`
- `cp "docs/_PDF/images/duck-logo.png" "website/public/logo.png"`
- `cd website && npm run build` (for validation)

## 5. Dependencies requested
- `astro` (production/dev dependency for static site generation)

## 6. Risks
- Manually creating Astro files rather than using `create-astro` requires careful setup of `astro.config.mjs` to ensure the build succeeds.

## 7. Ambiguities
- Should we use `npm install astro` or just `npx astro`? We will install it locally to ensure reproducible builds.
