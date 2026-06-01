# Page Blueprints

This document defines the content structure, sources, and required assets for each page defined in `site-map.md`.

## 1. Homepage (`/`)

**Purpose:** Introduce ADDF, explain its core value (local file sovereignty), and drive users to start.

- **Hero Section:**
  - Headline: "The files are the project."
  - Subheadline: File-first methodology for LLM-assisted software development.
  - Call to Action: "Start Here" button (links to `/start-here`).
  - Required Asset: Duck logo (`assets/logo/`).
- **Features Section:**
  - Highlights: Local File Sovereignty, Zero lock-in, 3-mode operating model.
  - Content Source: Derived from `DOMAIN.md` and `README.md`.
- **How It Works Section:**
  - Visual: 8-step lifecycle diagram.
  - Required Asset: Lifecycle diagram (`assets/lifecycle/`).
  - Content Source: Derived from `DOMAIN.md`.

## 2. Start Here (`/start-here`)

**Purpose:** Provide the onboarding flow for an operator's first session.

- **Introduction:** 
  - Summary of what is needed (LLM of choice, terminal, markdown editor).
- **Step-by-Step Guide:**
  - Step 1: Download the starter kit (links to `/downloads`).
  - Step 2: Initialize project brain.
  - Step 3: Run the first session.
- **Content Source:** Directly derived from `START_HERE.md`.

## 3. Downloads (`/downloads`)

**Purpose:** Central hub for all downloadable framework assets.

- **Starter Kit Section:**
  - Options: Blank Starter Kit, Example-Filled Starter Kit.
  - Format: ZIP downloads.
- **Prompt Catalog Section:**
  - Options: Full prompt catalog grouped by mode.
  - Format: ZIP download.
- **Content Source:** Driven by artifacts in `starter-kit/` and `prompts/`.

## 4. Documentation Pages (`/docs/*`)

**Purpose:** Detailed reference for ADDF concepts.

### 4.1 Framework (`/docs/framework`)
- **Sections:** Identity, target operators, what the project is/is not.
- **Content Source:** `DOMAIN.md`.

### 4.2 Scale Model (`/docs/scale-model`)
- **Sections:** Project → Release → Feature → Sprint → Patch definitions.
- **Content Source:** `DOMAIN.md`.

### 4.3 Lifecycle (`/docs/lifecycle`)
- **Sections:** 8-step lifecycle, sprint loop.
- **Required Asset:** Core framework diagrams (`assets/diagrams/`).
- **Content Source:** `DOMAIN.md`.

### 4.4 Modes (`/docs/modes`)
- **Sections:** Research, Design, and Develop Mode rules.
- **Content Source:** `AGENTS.md`.

### 4.5 Project Brain (`/docs/project-brain`)
- **Sections:** Core files list and purposes.
- **Content Source:** `DOMAIN.md`, `STATE.md`, `DECISIONS.md`.

### 4.6 Starter Kit & Prompt Catalog (`/docs/starter-kit`, `/docs/prompt-catalog`)
- **Sections:** Structure and usage instructions.
- **Content Source:** `START_HERE.md` and internal READMEs.

### 4.7 Examples (`/docs/examples`)
- **Sections:** Mini Task Tracker walkthrough.
- **Content Source:** `examples/mini-task-tracker/`.
