# Sprint 006: Documentation Pages — Blueprint

## 1. Architecture & Stack
- **Framework:** Astro (Static Site Generation mode).
- **Styling:** Vanilla CSS, continuing the design tokens established in Sprint 005 (`--yolk`, `--ink`, `--paper`, etc.).
- **Layout Approach:** Documentation pages will utilize a new `DocsLayout.astro` that wraps the global `Layout.astro` and adds a left-hand sidebar navigation for the documentation sections.

## 2. File Implementation Plan

### 2.1 Layouts & Navigation
- **`website/src/layouts/Layout.astro`** [MODIFY]: Uncomment/add the `Framework` and `Lifecycle` links in the header navigation pointing to `/docs/framework` and `/docs/lifecycle`.
- **`website/src/layouts/DocsLayout.astro`** [NEW]: A sub-layout that accepts the global layout and provides a two-column grid (sidebar nav on the left, markdown content on the right).

### 2.2 Documentation Pages
- **`website/src/pages/docs/framework.astro`** [NEW]: The core philosophy and 3 principles. Integrates `1_ADDF framework map.png`.
- **`website/src/pages/docs/scale-model.astro`** [NEW]: The project/release/feature/sprint scale explanation. Integrates `3_Work Scale Model.png` and `4_Scale  Lifecycle  Mode interlock.png`.
- **`website/src/pages/docs/lifecycle.astro`** [NEW]: The 8-step lifecycle diagram and step-by-step breakdown. Integrates `5_8-Step Lifecycle.png` and `7_Sprint Loop.png`.
- **`website/src/pages/docs/modes.astro`** [NEW]: Detailed rules for Research, Design, and Develop modes. Integrates `2_Three Operating Modes.png` and `8_Dry Run Approval Gate.png`.
- **`website/src/pages/docs/project-brain.astro`** [NEW]: Documentation on `STATE.md`, `DOMAIN.md`, `DECISIONS.md`, etc. Integrates `6_Project Brain file map.png`.
- **`website/src/pages/docs/starter-kit.astro`** [NEW]: Guide on using the blank and example-filled kits. Integrates `11_Starter kit structure.png` and `12_Repository structure.png`.
- **`website/src/pages/docs/prompt-catalog.astro`** [NEW]: Overview of the prompts. Integrates `9_Handoff and Resumption.png`.
- **`website/src/pages/docs/examples.astro`** [NEW]: Overview of the example projects. Integrates `15_Mini Task Tracker scale example.png`.

## 3. Design Guidelines
- **Typography:** Continue using Instrument Serif for page titles (`h1`), Space Grotesk for body, and JetBrains Mono for code blocks and eyebrows.
- **Content Blocks:** Use the 1px Rule borders for callouts or warning boxes.
- **Sidebar:** The sidebar must clearly indicate the currently active page.
