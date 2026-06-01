# Sprint 004 — Blueprint

**Sprint:** Sprint 004 - Website Information Architecture

## 1. Approved Changes

### 1.1 Create `website/README.md`
- **Purpose:** Document the purpose of the `website/` directory before code is added.
- **Content Requirements:** 
  - State that this directory will house the v0.2 static website and the future v0.4 web onboarding app.
  - Note the architectural decisions: use a static framework that supports future client-side interactivity (Decision 009) and static site first (Decision 003).
  - Explicitly declare that no source code is written in Sprint 004.

### 1.2 Create `docs/site-map.md`
- **Purpose:** Define the URL structure and navigation hierarchy.
- **Content Requirements:**
  - Define primary navigation (Header) and secondary navigation (Footer).
  - Define the path structure:
    - `/` (Homepage)
    - `/start-here` (First-session onboarding)
    - `/downloads` (Starter kit, examples, prompt catalog)
    - `/docs/*` (Framework, Scale Model, Lifecycle, Modes, Project Brain, Starter Kit, Prompt Catalog, Examples)
  - Include a future placeholder path for `/onboarding` (v0.4).

### 1.3 Create `docs/page-blueprints.md`
- **Purpose:** Provide a content specification for every page defined in the site map.
- **Content Requirements:**
  - Break down each page by its sections (e.g., Hero, Features, Call to Action).
  - Identify where the content comes from (e.g., derived from `README.md`, `DOMAIN.md`, `START_HERE.md`, or existing prompts).
  - List required assets (e.g., duck logo, lifecycle diagram) for each page.

## 2. Directory Structure Updates
- `website/` (New directory to be created, initially only containing `README.md`)

## 3. Constraints
- Do not write HTML, CSS, JavaScript, or any website framework code.
- Ensure the architecture aligns with Decisions 003 and 009.
