# Sprint 006_2: GitHub Deployment — Acceptance

## Acceptance Criteria

1. **Astro Configuration:**
   - `astro.config.mjs` contains the correct `site` and `base` URL for the repository.
   
2. **Path Resolution:**
   - The global header links (Framework, Downloads) and the sidebar documentation links utilize the Astro Base URL to prevent 404s in the production environment.
   
3. **Workflow Exists:**
   - `.github/workflows/deploy.yml` exists at the root of the repository.
   - The workflow explicitly targets the `website/` working directory for installation and building.
   - The workflow targets `website/dist` as the artifact path for deployment.

4. **Build Integrity:**
   - Running `npm run build` locally still succeeds without syntax errors or path resolution failures.
