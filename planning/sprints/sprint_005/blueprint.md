# Sprint 005: Website MVP — Blueprint

## 1. Architecture & Stack
- **Framework:** Astro (Static Site Generation mode). Astro allows us to build a purely static site now while supporting interactive islands in v0.4 without a rewrite.
- **Styling:** Vanilla CSS. We will implement the design tokens defined in `STYLE_GUIDE.md`. No utility frameworks.
- **Hosting Target:** Static file host.

## 2. File Implementation Plan

### 2.1 Initialization
- **`website/package.json`**: Astro dependencies and build scripts (`dev`, `build`, `preview`).
- **`website/astro.config.mjs`**: Minimal Astro configuration for static generation.

### 2.2 Global Assets & Layout
- **`website/src/styles/global.css`**: 
  - CSS variables for the canonical palette (`--yolk: #F5C518`, `--ink: #14110D`, `--paper: #F6F1E4`, etc.).
  - Typography imports (`Instrument Serif`, `Space Grotesk`, `JetBrains Mono`) from Google Fonts.
  - Spacing scale (`--space-0` through `--space-16`).
  - Base resets, 1px `var(--rule)` borders, and 4px border radius.
- **`website/src/layouts/Layout.astro`**: 
  - Global HTML shell and SEO metadata.
  - Global header with sticky scroll, transparent-to-Paper background, and primary CTA.
  - Yolk footer containing the massive *Quack!* and mono metadata line.
- **`website/public/logo.png`**: The interim PNG logo.

### 2.3 Pages
- **`website/src/pages/index.astro`**: Homepage. 
  - **Hero:** Paper or Yolk background, Mono eyebrow, Instrument Serif headline ("The files are the project."), Space Grotesk lede, CTAs with `→`, and an Ink terminal block with a blinking cursor.
  - **Features:** 1px rule cards, Paper-warm fills for accents.
  - **Lifecycle:** Dark panel integration for the 8-step diagram.
- **`website/src/pages/start-here.astro`**: Onboarding guide. Declarative, concrete instructions.
- **`website/src/pages/downloads.astro`**: Hub for downloading the starter kit and prompt catalog.

## 3. Design Guidelines
- **Color:** Enforce the 60/25/10/5 ratio (Paper/Ink/Yolk/Pond). No pure black or pure white. No gradients.
- **Typography:** Instrument Serif for display (with negative tracking), Space Grotesk for body, JetBrains Mono for eyebrows and code.
- **UI Details:** No drop shadows (except a single soft shadow for the hero terminal block). Use 1px borders and sharp 4px radii.
- **Voice:** Write like a senior engineer. Declarative. Concrete. Use em dashes. No filler words ("just", "simply", "magical").
