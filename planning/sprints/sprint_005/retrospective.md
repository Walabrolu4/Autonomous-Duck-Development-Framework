# Sprint 005: Website MVP — Retrospective

## 1. What Was Planned
Sprint 005 aimed to build the first public version (v0.2) of the ADDF website using Astro for static site generation. The goal was to establish the brand's visual identity based on `STYLE_GUIDE.md`, create the first-session onboarding flow (`/start-here`), and serve downloadable resources (`/downloads`).

## 2. What Was Built
- Initialized an Astro project configured strictly for static site generation.
- Created `website/src/styles/global.css` translating the canonical 60/25/10/5 color palette, typography (Instrument Serif, Space Grotesk, JetBrains Mono), and UI patterns.
- Built the global layout (`Layout.astro`) complete with the massive *Quack!* footer.
- Authored `index.astro`, `start-here.astro`, and `downloads.astro`.
- Successfully validated the static output via `npm run build`.

## 3. Variances from the Blueprint
- **Assets:** The logo asset referenced in the `dry_run.md` (`assets/logo/duck-logo.png`) was found to be missing because the folder did not exist. The source path was successfully updated to `docs/_PDF/images/duck-logo.png` before implementation. Furthermore, the downloadable `.zip` assets were discovered missing post-implementation and subsequently generated and placed in `website/public/assets`.
- **Consistency Audit Fixes:** A post-implementation audit discovered placeholder links (`href="#"`), missing GitHub repository URLs, and a terminology inconsistency (using internal Architect/Builder roles instead of public Design/Develop modes). These were corrected via minor patches before the sprint closed.
- **CLI Commands:** The hero section's teaser `$ addf init` was updated to `$ cp -r starter-kit/blank/* .` to accurately reflect the v0.1 manual setup process since the CLI is out of scope until v0.3.

## 4. Lessons Learned
- **Astro Alignment:** Authoring Astro manually without `create-astro` went smoothly, but verifying build scripts in `package.json` was an extra step that could be missed. 
- **Placeholders vs. Acceptance Criteria:** The human `acceptance.md` explicitly warned against unstyled placeholders, which was initially missed during implementation. A consistency audit successfully caught and resolved the issue. 
- **Voice Guidelines vs. Internal Definitions:** `STYLE_GUIDE.md` examples using internal role names (Architect/Builder) conflicted with `DECISIONS.md` public mode terminology. Future sprints must prioritize `DECISIONS.md` override rules.
