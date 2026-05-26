# Docs_Todo.md

> Detailed build todo list for the ADDF wiki. Each item corresponds to one page in `Docs_List.md`.
> When an LLM completes a slice, it marks every item in that slice `[x]` and appends a note to `DOCS_Notes.md`.

**Before starting any slice:** Read `docs/DOCS_Notes.md` in full.  
**After completing any slice:** Append a note to `docs/DOCS_Notes.md` with: slice number, date, issues found.  
**Style authority:** `docs/_PDF/style Guide/STYLE_GUIDE.md`  
**Source documents:** `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_5.md` (primary), `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_5_senior_engineering.md` (supplemental)

---

## Global Rules (apply to every page)

Before marking any page done, verify:

- [x] H1 title matches `Docs_List.md` exactly.
- [x] One-sentence lede under the title (Space Grotesk lede style in web; plain text in MD).
- [x] Table of contents if the page has more than 3 sections.
- [x] Every framework term uses canonical capitalization: `Research Mode`, `Design Mode`, `Develop Mode`, `Sprint Pack`, `Dry Run`, `Permission Level`, `Project Brain`, `Local File Sovereignty`.
- [x] All file names wrapped in backticks: `` `STATE.md` ``, not `STATE.md`.
- [x] No banned words: *just, simply, easy, basically, amazing, powerful, seamless, unleash, supercharge, let's, magical, AI-powered, best practice, unlock*.
- [x] Em dashes — not hyphens — for asides.
- [x] At most one *Quack!* per page (footer only, and only if the page warrants it).
- [x] No emoji anywhere.
- [x] Each section ends with a **Rule:** callout quoting the relevant rule from the source.
- [x] Internal links use relative paths (e.g., `../modes/index.md` from inside `docs/lifecycle/`).
- [x] Page footer includes: navigation back to `../index.md` or `./index.md`, and the framework version (`ADDF v3.5`).
- [x] Images referenced using relative paths from `docs/`: `_PDF/images/<filename>` or `../_PDF/images/<filename>` from sub-folders.

---

## Slice A — Foundation (Priority: First)

*Create the scaffolding and navigation layer. All other slices depend on these.*

### A1 — Wiki Home
- [x] Create `docs/index.md`
- [x] H1: `ADDF Wiki`
- [x] One-sentence lede: `The Autonomous Duck Deployment Framework — a file-first methodology for coordinating LLM-assisted research, design, development, review, handoff, and long-term project evolution.`
- [x] Brief "What this wiki covers" paragraph (3–4 sentences)
- [x] Navigation table with all 25 pages: columns = Page, Section, What's there
- [x] Note about the `_PDF/` subfolder (source documents live there; wiki pages live here)
- [x] Note mapping README links to actual wiki paths (e.g. `docs/sprint-workflow.md` → `docs/sprint-loop.md`)
- [x] Footer: `ADDF v3.5 · [→ README](../README.md)`
- [x] Source: `README.md` documentation table; v3.5 §1, §3

### A2 — Getting Started
- [x] Create `docs/getting-started.md`
- [x] H1: `Getting Started`
- [x] Lede: one sentence answering "what do I do in the first 20 minutes?"
- [x] TOC
- [x] Section: "What you need" — requirements checklist (any capable LLM, a text editor, a repo)
- [x] Section: "Step 1 — Copy the starter kit" — folder structure visual + bash commands from §17.1
- [x] Section: "Step 2 — Fill `SECURITY.md` first" — why this file comes before everything else
- [x] Section: "Step 3 — Populate the core files in order" — the 8-file sequence from §17.2
- [x] Section: "Step 4 — Your first session" — the mode sequence from §17.3
- [x] Section: "What comes next" — links to lifecycle, sprint loop, prompt catalog
- [x] **Rule:** `Fill SECURITY.md before loading files into an AI session.`
- [x] Image: `_PDF/images/10_First-session onboarding flow.png`
- [x] Source: v3.5 §17, §23.1

### A3 — Core Concepts
- [x] Create `docs/core-concepts.md`
- [x] H1: `Core Concepts`
- [x] Lede: one sentence on the four separations
- [x] TOC
- [x] Section: "The four separations" — block-quote the four questions from §3, explain each
- [x] Section: "The six core principles" — each principle (§4.1–4.6) as its own H3 with the rule callout
- [x] Section: "Why it works" — brief closing on how the separations prevent the three failure modes from §2
- [x] Links: work scale, lifecycle, modes, project brain
- [x] Source: v3.5 §2, §3, §4

---

## Slice B — The Lifecycle

*The 8-step lifecycle page. One page, all steps.*

### B1 — Lifecycle Overview
- [x] Create `docs/lifecycle/` folder
- [x] Create `docs/lifecycle/index.md`
- [x] H1: `The 8-Step ADDF Lifecycle`
- [x] Lede: one sentence on scalability of the lifecycle
- [x] TOC
- [x] Intro paragraph: "The lifecycle is scalable. Apply the full path to a new project. Apply a slice to a bounded feature."
- [x] **Step 1 — Research** (H2 anchor: `#research`)
  - [x] Primary mode, purpose, inputs, outputs, exit criteria, rule
- [x] **Step 2 — Design & Feasibility** (H2 anchor: `#design-feasibility`)
  - [x] Primary mode, purpose, outputs, exit criteria, rule
- [x] **Step 3 — Validation Gate** (H2 anchor: `#validation-gate`)
  - [x] Primary mode, the seven gate questions, outputs, exit criteria, rule
- [x] **Step 4 — Architecture** (H2 anchor: `#architecture`)
  - [x] Primary mode, purpose, outputs, exit criteria, rule
- [x] **Step 5 — Sprint Planning** (H2 anchor: `#sprint-planning`)
  - [x] Primary mode, purpose, outputs, exit criteria, rule
- [x] **Step 6 — Build & Test** (H2 anchor: `#build-test`)
  - [x] Primary mode, dry run step, implementation step, outputs, exit criteria, rule
- [x] **Step 7 — Review & Reflection** (H2 anchor: `#review-reflection`)
  - [x] Primary mode, purpose, outputs, exit criteria, rule
- [x] **Step 8 — Deploy, Maintain, or Resume** (H2 anchor: `#deploy-maintain-resume`)
  - [x] Primary mode, the seven next-state options, outputs, exit criteria, rule
- [x] Mode-to-lifecycle mapping table (from §8.4)
- [x] Scale examples section (new project, new feature, sprint, patch — from §8.5)
- [x] Images: `_PDF/images/5_8-Step Lifecycle.png`, `_PDF/images/4_Scale  Lifecycle  Mode interlock.png`
- [x] Source: v3.5 §7, §8

---

## Slice C — Operating Modes

*Four pages: overview + one per mode.*

### C1 — Modes Overview
- [x] Create `docs/modes/` folder
- [x] Create `docs/modes/index.md`
- [x] H1: `Operating Modes`
- [x] Lede: "Every AI session runs in one explicit mode — the mode answers what the model is allowed to do."
- [x] TOC
- [x] Section: mode overview paragraph (one sentence per mode)
- [x] Mode boundaries table (§5.4): Mode | Primary Action | Writes | Must Not Write
- [x] Section: "Declaring a mode" — how to declare at session start
- [x] Links to each mode page + permission levels
- [x] Image: `_PDF/images/2_Three Operating Modes.png`
- [x] Source: v3.5 §5

### C2 — Research Mode
- [x] Create `docs/modes/research-mode.md`
- [x] H1: `Research Mode`
- [x] Lede: one sentence
- [x] TOC
- [x] Section: "When to use Research Mode" — the use cases list from §5.1
- [x] Section: "What Research Mode may produce" — output file list
- [x] Section: "What Research Mode must not do" — the five prohibitions
- [x] Section: "The Research Mode prompt" — prompt text from §19.1 in a fenced code block
- [x] **Rule:** `Research Mode gathers evidence. It does not decide or build.`
- [x] Link to Design Mode (natural next step)
- [x] Source: v3.5 §5.1, §7.1, §19.1

### C3 — Design Mode
- [x] Create `docs/modes/design-mode.md`
- [x] H1: `Design Mode`
- [x] Lede: one sentence
- [x] TOC
- [x] **Note callout at top:** "Design Mode was called *Architect Mode* in earlier versions of the framework. The two terms refer to the same role."
- [x] Section: "What Design Mode covers" — the 14-item list from §5.2
- [x] Section: "What Design Mode may create or update" — the full file list
- [x] Section: "What Design Mode must not do" — the five prohibitions
- [x] Section: "Design Mode prompts" — project init prompt (§19.2), sprint pack prompt (§19.3), dry run review prompt (§19.5), resumption prompt (§19.7) — each in a fenced code block with a H3 label
- [x] **Rule:** `Design Mode writes Markdown project memory. It does not write implementation.`
- [x] Source: v3.5 §5.2, §19.2, §19.3, §19.5, §19.7

### C4 — Develop Mode
- [x] Create `docs/modes/develop-mode.md`
- [x] H1: `Develop Mode`
- [x] Lede: one sentence
- [x] TOC
- [x] **Note callout at top:** "Develop Mode was called *Builder Mode* in earlier versions of the framework."
- [x] Section: "What Develop Mode may create or modify" — implementation file list
- [x] Section: "What Develop Mode must do" — the 10 requirements
- [x] Section: "What Develop Mode must not do" — the 8 prohibitions
- [x] Section: "The dry run requirement" — explanation + image reference
- [x] Section: "Develop Mode prompts" — dry run prompt (§19.4), authorization prompt (§19.6) — each in a fenced code block
- [x] **Rule:** `Develop Mode changes implementation files only after dry run approval.`
- [x] Link to permission levels page
- [x] Image: `_PDF/images/8_Dry Run Approval Gate.png`
- [x] Source: v3.5 §5.3, §19.4, §19.6

---

## Slice D — Work Scale & Sprint Loop

### D1 — Work Scale Model
- [x] Create `docs/work-scale.md`
- [x] H1: `Work Scale Model`
- [x] Lede: "Scale determines how much process is appropriate — a patch and a new project must not follow the same workflow."
- [x] TOC
- [x] Section per scale (Project, Release, Feature, Sprint, Patch) — each with definition + examples
- [x] Scale-to-process mapping table (§6.6)
- [x] **Rule:** `Do not run a project process for a patch. Do not run a patch process for a project.`
- [x] Image: `_PDF/images/3_Work Scale Model.png`
- [x] Source: v3.5 §6

### D2 — Sprint Loop
- [x] Create `docs/sprint-loop.md`
- [x] H1: `Sprint Loop`
- [x] Lede: one sentence on what the sprint loop controls
- [x] TOC
- [x] Overview: numbered list of all 11 steps
- [x] Section per step (§12.2–12.12) — each as H3 with what happens and who acts
- [x] Permission level authorization example (the exact text from §12.8)
- [x] **Rule:** `A sprint ends when state is updated, not when code compiles.`
- [x] Image: `_PDF/images/7_Sprint Loop.png`
- [x] Source: v3.5 §12

---

## Slice E — Project Brain & File Reference

### E1 — Project Brain
- [x] Create `docs/project-brain.md`
- [x] H1: `The Project Brain`
- [x] Lede: "The Project Brain is the file-backed memory layer — it must be current, explicit, scoped, reviewable, searchable, versioned, and safe to load into an LLM session."
- [x] TOC
- [x] Section: "Core files" — file list with one-line responsibility for each (from §9.4 table)
- [x] Section: "Sprint files" — file list with one-line responsibility each
- [x] Section: "Release and feature files" — file list
- [x] Section: "Properties of good project memory" — the 7 properties from §9.4
- [x] File responsibilities table (§9.4) — full table
- [x] **Rule:** `If a model needs to know it later, write it to the project brain.`
- [x] Image: `_PDF/images/6_Project Brain file map.png`
- [x] Source: v3.5 §9

### E2 — File Reference
- [x] Create `docs/file-reference.md`
- [x] H1: `File Reference`
- [x] Lede: "Template and purpose for every project brain file."
- [x] TOC
- [x] Section per file template:
  - [x] `AGENTS.md` — purpose + full template from §18.1
  - [x] `STATE.md` — purpose + full template from §18.2
  - [x] `DOMAIN.md` — purpose + full template from §18.3
  - [x] `DECISIONS.md` — purpose + full template from §18.4
  - [x] Sprint Pack (`requirements.md`, `blueprint.md`, `acceptance.md`) — purpose + all three templates from §18.5
- [x] **Rule:** `Templates are starting points, not decoration. Remove sections that do not apply.`
- [x] Source: v3.5 §18

---

## Slice F — Prompt Catalog

### F1 — Prompt Catalog
- [x] Create `docs/prompt-catalog.md`
- [x] H1: `Prompt Catalog`
- [x] Lede: "Copy-paste prompts for every framework mode and workflow — research, planning, implementation, review, and resumption."
- [x] TOC
- [x] Intro: "Store prompts under `prompts/research/`, `prompts/design/`, `prompts/develop/`"
- [x] Section: "Research Mode Prompt" (§19.1) — purpose, files to load, prompt in fenced code block
- [x] Section: "Design Mode — Project Initialization" (§19.2) — purpose, files to load, prompt
- [x] Section: "Design Mode — Sprint Pack Generation" (§19.3) — purpose, files to load, prompt
- [x] Section: "Develop Mode — Dry Run" (§19.4) — purpose, files to load, prompt
- [x] Section: "Design Mode — Dry Run Review" (§19.5) — purpose, files to load, prompt
- [x] Section: "Develop Mode — Authorization" (§19.6) — purpose, files to load, prompt
- [x] Section: "Resumption Prompt" (§19.7) — purpose, files to load, prompt
- [x] **Rule:** `Prompts are executable protocol. Keep them terse.`
- [x] Source: v3.5 §19

---

## Slice G — Handoff, Repository, Setup

### G1 — Handoff Protocol
- [x] Create `docs/handoff-protocol.md`
- [x] H1: `Handoff, Resumption & Model Switching`
- [x] Lede: "ADDF treats model handoff as a normal operating condition — a new model resumes from files, not from memory."
- [x] TOC
- [x] Section: "Session checkpoint protocol" — the file update list from §14.1
- [x] Section: "Handoff summary template" — full template from §14.2 in a fenced MD code block
- [x] Section: "Incoming model protocol" — the file load list + wait-for-authorization rule from §14.3
- [x] Section: "The resumption prompt" — link to prompt catalog and include the prompt text for convenience
- [x] **Rule:** `The next model resumes from files, not from memory.`
- [x] Image: `_PDF/images/9_Handoff and Resumption.png`
- [x] Source: v3.5 §14, §19.7

### G2 — Repository Structure
- [x] Create `docs/repository-structure.md`
- [x] H1: `Repository Structure`
- [x] Lede: one sentence
- [x] TOC
- [x] Section: "Standard ADDF project" — full folder tree from §16.1 in fenced code block
- [x] Section: "Minimum viable ADDF" — folder tree from §16.2 + explanation of what each file does
- [x] Section: "Public ADDF repository" — folder tree from §16.3
- [x] **Rule:** `The folder structure should make the operating model visible.`
- [x] Image: `_PDF/images/12_Repository structure.png`, `_PDF/images/11_Starter kit structure.png`
- [x] Source: v3.5 §16

### G3 — Initial Setup
- [x] Create `docs/initial-setup.md`
- [x] H1: `Initial Setup`
- [x] Lede: one sentence
- [x] TOC
- [x] Section: "Create the project" — bash commands from §17.1 in fenced bash code block
- [x] Section: "Populate files in order" — the 8-file sequence (numbered list)
- [x] Section: "First session" — the mode sequence from §17.3
- [x] Note: link to getting-started.md for the 20-minute walkthrough; this page covers the technical scaffold only
- [x] **Rule:** `Fill SECURITY.md before loading files into an AI session.`
- [x] Image: `_PDF/images/10_First-session onboarding flow.png`
- [x] Source: v3.5 §17

---

## Slice H — Permission Levels & Cycles

### H1 — Permission Levels
- [x] Create `docs/permission-levels.md`
- [x] H1: `Develop Mode Permission Levels`
- [x] Lede: "Permission levels apply only to Develop Mode — they control how far the model may reach beyond the approved sprint scope."
- [x] TOC
- [x] Section: the permission levels table (§13) — Level | Name | Meaning
- [x] Section: "How levels are used" — most work starts at 0, proceeds to 1; levels 2–4 require stronger justification
- [x] Section: "How to authorize a level" — the authorization message pattern from §12.8
- [x] Section: "Escalation rules" — the model cannot self-authorize; escalation requires explicit human instruction
- [x] **Rule:** `Permission level controls Develop Mode freedom.`
- [x] Source: v3.5 §13

### H2 — Release Cycles
- [x] Create `docs/release-cycles.md`
- [x] H1: `Release Cycles`
- [x] Lede: "A release groups features into a bounded delivery target — a completed release becomes the baseline for the next."
- [x] TOC
- [x] Section: "Release plan" — what a release plan defines (§10.1)
- [x] Section: "Release folder structure" — folder tree from §10.2
- [x] Section: "Starting a new version" — load list + Design Mode output from §10.3
- [x] Section: "Release completion criteria" — the 8-item checklist from §10.4
- [x] **Rule:** `A new release updates the project brain. It does not restart the project from zero.`
- [x] Source: v3.5 §10

### H3 — Feature Cycles
- [x] Create `docs/feature-cycles.md`
- [x] H1: `Feature Cycles`
- [x] Lede: "A feature cycle adds a capability to an existing project without restarting the full lifecycle."
- [x] TOC
- [x] Section: "Feature flow" — the 8-step flow from §11.1 (numbered list)
- [x] Section: "Feature folder structure" — folder tree from §11.2
- [x] Section: "Feature brief template" — full template from §11.3 in a fenced MD code block
- [x] **Rule:** `A feature cycle extends the project. It does not erase existing state.`
- [x] Source: v3.5 §11

---

## Slice I — Domain Adaptations & Examples

### I1 — Domain Adaptations
- [x] Create `docs/domain-adaptations.md`
- [x] H1: `Domain Adaptations`
- [x] Lede: "ADDF is domain-agnostic — the structure stays stable and the domain files adapt."
- [x] TOC
- [x] Section per domain (§20.1–20.5):
  - [x] Web Applications — typical entities, typical commands
  - [x] Game Development — typical entities, note on `DOMAIN.md` as technical game design doc
  - [x] Desktop Applications — typical entities
  - [x] Data / Automation — typical entities
  - [x] Documentation / Framework Projects — typical entities
- [x] **Rule:** `Keep the structure stable. Adapt the domain files.`
- [x] Source: v3.5 §20

### I2 — Examples
- [x] Create `docs/examples.md`
- [x] H1: `Examples`
- [x] Lede: "Two worked examples showing ADDF in practice — the Mini Task Tracker and the ADDF public repository."
- [x] TOC
- [x] Section: "Mini Task Tracker" (§21)
  - [x] Work scale breakdown
  - [x] Lifecycle use summary (each mode and what it did)
  - [x] Example `DOMAIN.md` from §21.3 in a fenced MD code block
  - [x] **Rule:** `Small examples stay small. The point is to expose the process, not showcase an app.`
- [x] Section: "ADDF Public Repository" (§22)
  - [x] Project scope list
  - [x] Release plan summary (v0.1–v0.4)
  - [x] Sprint 001 goal + in-scope / out-of-scope
  - [x] **Rule:** `The public repository must dogfood the framework.`
- [x] Image: `_PDF/images/15_Mini Task Tracker scale example.png`, `_PDF/images/14_Public roadmap.png`
- [x] Source: v3.5 §21, §22

---

## Slice J — Operational Reference

### J1 — Operational Checklists
- [x] Create `docs/checklists.md`
- [x] H1: `Operational Checklists`
- [x] Lede: "Four gate checklists — each is an execution gate, not a suggestion."
- [x] TOC
- [x] Section: "Before first AI session" — checklist from §23.1 (markdown checkboxes)
- [x] Section: "Before Develop Mode" — checklist from §23.2
- [x] Section: "Before authorizing development" — checklist from §23.3
- [x] Section: "Before commit" — checklist from §23.4
- [x] **Rule:** `A checklist is an execution gate, not a suggestion.`
- [x] Source: v3.5 §23

### J2 — Failure Handling & Troubleshooting
- [x] Create `docs/troubleshooting.md`
- [x] H1: `Failure Handling & Troubleshooting`
- [x] Lede: "Failure recovery begins by writing state — not by asking the model to try again."
- [x] TOC
- [x] Section: "Develop Mode touched unapproved files" (§24.1) — 5-step action list
- [x] Section: "The model invented business logic" (§24.2) — 6-step action list
- [x] Section: "Project state is confused" (§24.3) — Design Mode consistency audit: load list + ask
- [x] Section: "Model runs out of context" (§24.4) — Session Checkpoint Protocol: 3-file update + resumption prompt
- [x] **Rule:** `Failure recovery begins by writing state, not by asking for another fix.`
- [x] Source: v3.5 §24

---

## Slice K — Reference Pages

### K1 — Agile Comparison
- [x] Create `docs/agile-comparison.md`
- [x] H1: `ADDF and Agile`
- [x] Lede: "ADDF borrows useful language from Agile. It is not Scrum."
- [x] TOC
- [x] Section: "What ADDF uses from Agile" — bullet list (backlog, sprint, acceptance criteria, review, retrospective, release, iteration)
- [x] Section: "What ADDF does not require" — bullet list (Scrum Master, Product Owner, daily standups, story points, velocity tracking, ceremony cadence, two-week sprint)
- [x] Section: "Sprint definition in ADDF" — a sprint is a bounded AI implementation packet, defined by artifacts not duration
- [x] Term mapping table: Agile/Scrum term | ADDF equivalent (from §15.2)
- [x] **Rule:** `Use Agile language where it clarifies. Do not import Scrum ceremony.`
- [x] Source: v3.5 §15

### K2 — Glossary
- [x] Create `docs/glossary.md`
- [x] H1: `Glossary`
- [x] Lede: "Canonical definitions for all ADDF framework terms."
- [x] Alphabetical definition list — each term as H3, definition as paragraph, with link to the relevant wiki page
- [x] Terms to include (from v3.5 §25 + STYLE_GUIDE §20):
  - [x] ADDF
  - [x] Context Engineering
  - [x] Design Mode (with Architect Mode alias note)
  - [x] Develop Mode (with Builder Mode alias note)
  - [x] Dry Run
  - [x] Feature
  - [x] Handoff Summary
  - [x] Local File Sovereignty
  - [x] Patch
  - [x] Permission Level
  - [x] Project Brain
  - [x] Release
  - [x] Research Mode
  - [x] Sprint
  - [x] Sprint Pack
  - [x] Validation Gate
  - [x] Work Scale
- [x] *Quack!* footer (earned here — final page of the wiki)
- [x] Source: v3.5 §25, STYLE_GUIDE §11, §20

---

## Completion Checklist

When all slices are done, verify the following before declaring the wiki complete:

- [x] Every page in `Docs_List.md` exists as a file.
- [x] Every internal link in every page resolves to an existing file.
- [x] `docs/index.md` navigation table covers all 25 pages.
- [x] README links that use different filenames are bridged in `docs/index.md`.
- [x] `docs/DOCS_Notes.md` has notes from every slice.
- [x] No banned words appear in any page (spot-check 5 random pages).
- [x] Every page has a **Rule:** callout with a rule from the source.
- [x] `docs/glossary.md` is the only page with a *Quack!* footer.

---

*ADDF · `docs/Docs_Todo.md` · generated 2026-05-25*
