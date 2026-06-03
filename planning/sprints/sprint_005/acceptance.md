# Sprint 005: Website MVP — Acceptance Criteria

## 1. Technical Acceptance
- [ ] `npm run build` completes successfully inside the `website/` directory, producing static HTML files.
- [ ] No server-side runtime, database, or backend API is required to serve the built site.
- [ ] Astro is configured strictly for static output.

## 2. Content & Routing Acceptance
- [ ] The Homepage (`/`) loads and displays the hero section, features, and core methodology concepts as specified in the site map.
- [ ] The Start Here page (`/start-here`) loads and clearly lists the first-session steps.
- [ ] The Downloads page (`/downloads`) loads and provides links for the starter kit and prompt catalog.
- [ ] Global navigation correctly links between these three pages. Links to `/docs/*` are either omitted or visually marked as "Coming Soon".

## 3. Design & Quality Acceptance
- [ ] The site strictly implements the `STYLE_GUIDE.md` color palette (`--paper`, `--ink`, `--yolk`). No unauthorized colors, gradients, or shadows are used.
- [ ] Typography strictly follows the three-family rule (`Instrument Serif`, `Space Grotesk`, `JetBrains Mono`) with correct tracking and line-heights.
- [ ] UI components use the correct 4px border radius and 1px borders.
- [ ] The website copy adheres to the declarative, concrete voice defined in the style guide.
- [ ] The massive *Quack!* is present in the site footer.
- [ ] The interim PNG logo is visible in the site header.
