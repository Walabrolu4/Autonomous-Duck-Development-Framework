# Sprint 006_2: GitHub Deployment — Blueprint

## Proposed Implementation

### 1. Astro Configuration Update
- **Target:** `website/astro.config.mjs`
- **Action:** Add `site` and `base` properties to the Astro config to ensure all statically generated assets and relative links resolve to the repository subpath.
```js
  site: 'https://Walabrolu4.github.io',
  base: '/Autonomous-Duck-Development-Framework',
```

### 2. URL Pathing Fixes
- **Target:** `website/src/layouts/Layout.astro` and `website/src/layouts/DocsLayout.astro`
- **Action:** Prepend `import.meta.env.BASE_URL` or the hardcoded base path to the absolute `/docs/` and `/downloads/` navigation links to ensure they resolve correctly on the GitHub Pages domain.

### 3. GitHub Actions Workflow
- **Target:** `.github/workflows/deploy.yml` (New File)
- **Action:** Create the official Astro GitHub Pages deployment workflow.
- **Details:** 
  - Trigger on push to `main`.
  - Use `ubuntu-latest`.
  - Set working directory to `./website` for the `npm ci` and `npm run build` steps.
  - Upload the `./website/dist` directory as the pages artifact.
  - Deploy using the `actions/deploy-pages@v4` action.
