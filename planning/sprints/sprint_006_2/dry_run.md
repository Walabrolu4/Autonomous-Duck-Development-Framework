# Sprint 006_2: GitHub Deployment — Dry Run

**Mode:** Develop Mode (Permission Level 0)  
**Date:** 2026-06-03

## 1. Files to create
- `.github/workflows/deploy.yml` (The GitHub Actions workflow for Astro deployment)

## 2. Files to modify
- `website/astro.config.mjs` (Add `site` and `base` config properties)
- `website/src/layouts/Layout.astro` (Prepend `import.meta.env.BASE_URL` to navigation and logo links)
- `website/src/layouts/DocsLayout.astro` (Prepend `import.meta.env.BASE_URL` to pagination links and sidebar nav)
- `website/src/pages/docs/*.astro` (Prepend `import.meta.env.BASE_URL` to `next` and `prev` props, and ensure `<img src>` tags use the base path)
- `website/src/pages/index.astro` (Ensure any absolute links/images use the base URL)
- `website/src/pages/downloads.astro` (Ensure asset download ZIP links use the base URL)

*Note: Since the entire site needs pathing updates to support GitHub Pages subpaths, every `.astro` file containing an absolute `/` link or `/images/` path must be updated. This slightly expands the original blueprint's scope from just `Layout.astro` and `DocsLayout.astro` to all content pages containing absolute URLs.*

## 3. Files to move or delete
- No files to move or delete.

## 4. Commands to run
- `New-Item -ItemType Directory -Force -Path ".github\workflows"` (to create the actions directory)
- `npm run build` (inside `website/` to verify static generation locally with the new configuration)

## 5. Dependencies requested
- None. The deployment relies entirely on built-in Astro configuration and standard GitHub Actions.

## 6. Risks
- **Asset pathing:** If the `import.meta.env.BASE_URL` is missed on an image tag, css link, or download zip, the asset will 404 in production despite the site loading. All absolute URLs (`/images/`, `/docs/`, `/assets/`, `/logo.png`) must be converted.
- **Local Dev Experience:** Adding a `base` config means the local dev server (`npm run dev`) will also start serving from `/Autonomous-Duck-Development-Framework/` instead of `/`. This is standard Astro behavior but requires the developer to navigate to the correct subpath locally.

## 7. Ambiguities
- **Username Casing:** The user's exact GitHub username capitalization is `Walabrolu4`. The site property will be set to `https://Walabrolu4.github.io` and the base to `/Autonomous-Duck-Development-Framework`, which is case-sensitive on GitHub Pages.
