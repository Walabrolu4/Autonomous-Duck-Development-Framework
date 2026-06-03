# Sprint 006: Documentation Pages — Acceptance Criteria

## 1. Technical Acceptance
- [ ] `npm run build` completes successfully without errors or broken internal links.
- [ ] The generated pages remain purely static, requiring no client-side JavaScript frameworks.
- [ ] All new documentation pages are accessible via URLs starting with `/docs/`.

## 2. Content & Routing Acceptance
- [ ] The global header navigation in `Layout.astro` correctly links to `/docs/framework` and `/docs/lifecycle`.
- [ ] All 8 required documentation pages exist and load correctly.
- [ ] The `DocsLayout.astro` sidebar contains links to all 8 documentation pages.
- [ ] Clicking any link in the docs sidebar navigates to the correct page without breaking the layout.

## 3. Design & Quality Acceptance
- [ ] The documentation pages adhere to the canonical 60/25/10/5 color ratio established in `STYLE_GUIDE.md`.
- [ ] Content is formatted for readability (proper margins, line-heights, and responsive behavior for mobile screens).
- [ ] The voice remains declarative and concrete, matching the internal framework documentation.
- [ ] Code blocks are styled with a dark background (`--ink`) and `JetBrains Mono` font.
