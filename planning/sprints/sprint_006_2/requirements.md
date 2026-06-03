# Sprint 006_2: GitHub Deployment — Requirements

## Goal
Automate the static generation and deployment of the ADDF website to GitHub Pages via GitHub Actions, establishing a hands-free continuous deployment pipeline.

## In Scope
- Configuring the Astro static site generator to respect the GitHub Pages repository subpath (`/Autonomous-Duck-Development-Framework`).
- Updating absolute navigation URLs across layouts to use the Astro Base URL or absolute repository subpath.
- Creating a GitHub Actions workflow (`deploy.yml`) to automatically build and deploy the `website/` directory to GitHub Pages on every push to `main`.

## Out of Scope
- Acquiring or configuring a custom domain.
- Setting up staging environments or preview branches.
- Deploying the CLI init tool or web onboarding app.
- Modifying any website content or styles (beyond URL pathing fixes).

## Assumptions
- The repository is hosted at `https://github.com/Walabrolu4/Autonomous-Duck-Development-Framework`.
- The live GitHub Pages URL will be `https://Walabrolu4.github.io/Autonomous-Duck-Development-Framework/`.
- The user has sufficient repository permissions to enable GitHub Actions as the source for GitHub Pages.
