# Sprint 004 — Dry Run

**Sprint:** Sprint 004 - Website Information Architecture
**Permission Level:** 0 (Dry Run Only)

## 1. Files to create
- `website/README.md`
- `docs/site-map.md`
- `docs/page-blueprints.md`

## 2. Files to modify
- `planning/sprints/sprint_004/implementation_log.md` (to be created/updated during implementation to log these changes, standard Develop Mode artifact)
- `planning/sprints/sprint_004/handoff_summary.md` (to be created at the end of the sprint, standard Develop Mode artifact)

## 3. Files to move or delete
- None.

## 4. Commands to run
- None. Explicitly forbidden in this sprint to run framework initialization commands (e.g., `create-astro`, `npm init`).

## 5. Dependencies requested
- None.

## 6. Risks
- **Scope Creep:** There is a risk of accidentally writing HTML/CSS/JS or framework config code into `website/` instead of keeping it strictly to information architecture documentation as mandated by the sprint blueprint.
- **Tech Stack Assumptions:** Page blueprints might assume capabilities of Astro that conflict with static constraints, though Astro is well-suited for static sites. We must stick to Markdown and structural planning.

## 7. Ambiguities
- The exact mapping of existing Markdown documentation files (e.g., `DOMAIN.md`, `START_HERE.md`) to the website's `/docs/*` URL paths. We will need to map these explicitly in `docs/site-map.md`.
- No ambiguities requiring immediate addition to `QUESTIONS.md` before implementation.
