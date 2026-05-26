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

- [ ] H1 title matches `Docs_List.md` exactly.
- [ ] One-sentence lede under the title (Space Grotesk lede style in web; plain text in MD).
- [ ] Table of contents if the page has more than 3 sections.
- [ ] Every framework term uses canonical capitalization: `Research Mode`, `Design Mode`, `Develop Mode`, `Sprint Pack`, `Dry Run`, `Permission Level`, `Project Brain`, `Local File Sovereignty`.
- [ ] All file names wrapped in backticks: `` `STATE.md` ``, not `STATE.md`.
- [ ] No banned words: *just, simply, easy, basically, amazing, powerful, seamless, unleash, supercharge, let's, magical, AI-powered, best practice, unlock*.
- [ ] Em dashes — not hyphens — for asides.
- [ ] At most one *Quack!* per page (footer only, and only if the page warrants it).
- [ ] No emoji anywhere.
- [ ] Each section ends with a **Rule:** callout quoting the relevant rule from the source.
- [ ] Internal links use relative paths (e.g., `../modes/index.md` from inside `docs/lifecycle/`).
- [ ] Page footer includes: navigation back to `../index.md` or `./index.md`, and the framework version (`ADDF v3.5`).
- [ ] Images referenced using relative paths from `docs/`: `_PDF/images/<filename>` or `../_PDF/images/<filename>` from sub-folders.

---

## Slice A — Foundation (Priority: First)

*Create the scaffolding and navigation layer. All other slices depend on these.*

### A1 — Wiki Home
- [ ] Create `docs/index.md`
- [ ] H1: `ADDF Wiki`
- [ ] One-sentence lede: `The Autonomous Duck Deployment Framework — a file-first methodology for coordinating LLM-assisted research, design, development, review, handoff, and long-term project evolution.`
- [ ] Brief "What this wiki covers" paragraph (3–4 sentences)
- [ ] Navigation table with all 25 pages: columns = Page, Section, What's there
- [ ] Note about the `_PDF/` subfolder (source documents live there; wiki pages live here)
- [ ] Note mapping README links to actual wiki paths (e.g. `docs/sprint-workflow.md` → `docs/sprint-loop.md`)
- [ ] Footer: `ADDF v3.5 · [→ README](../README.md)`
- [ ] Source: `README.md` documentation table; v3.5 §1, §3

### A2 — Getting Started
- [ ] Create `docs/getting-started.md`
- [ ] H1: `Getting Started`
- [ ] Lede: one sentence answering "what do I do in the first 20 minutes?"
- [ ] TOC
- [ ] Section: "What you need" — requirements checklist (any capable LLM, a text editor, a repo)
- [ ] Section: "Step 1 — Copy the starter kit" — folder structure visual + bash commands from §17.1
- [ ] Section: "Step 2 — Fill `SECURITY.md` first" — why this file comes before everything else
- [ ] Section: "Step 3 — Populate the core files in order" — the 8-file sequence from §17.2
- [ ] Section: "Step 4 — Your first session" — the mode sequence from §17.3
- [ ] Section: "What comes next" — links to lifecycle, sprint loop, prompt catalog
- [ ] **Rule:** `Fill SECURITY.md before loading files into an AI session.`
- [ ] Image: `_PDF/images/10_First-session onboarding flow.png`
- [ ] Source: v3.5 §17, §23.1

### A3 — Core Concepts
- [ ] Create `docs/core-concepts.md`
- [ ] H1: `Core Concepts`
- [ ] Lede: one sentence on the four separations
- [ ] TOC
- [ ] Section: "The four separations" — block-quote the four questions from §3, explain each
- [ ] Section: "The six core principles" — each principle (§4.1–4.6) as its own H3 with the rule callout
- [ ] Section: "Why it works" — brief closing on how the separations prevent the three failure modes from §2
- [ ] Links: work scale, lifecycle, modes, project brain
- [ ] Source: v3.5 §2, §3, §4

---

## Slice B — The Lifecycle

*The 8-step lifecycle page. One page, all steps.*

### B1 — Lifecycle Overview
- [ ] Create `docs/lifecycle/` folder
- [ ] Create `docs/lifecycle/index.md`
- [ ] H1: `The 8-Step ADDF Lifecycle`
- [ ] Lede: one sentence on scalability of the lifecycle
- [ ] TOC
- [ ] Intro paragraph: "The lifecycle is scalable. Apply the full path to a new project. Apply a slice to a bounded feature."
- [ ] **Step 1 — Research** (H2 anchor: `#research`)
  - [ ] Primary mode, purpose, inputs, outputs, exit criteria, rule
- [ ] **Step 2 — Design & Feasibility** (H2 anchor: `#design-feasibility`)
  - [ ] Primary mode, purpose, outputs, exit criteria, rule
- [ ] **Step 3 — Validation Gate** (H2 anchor: `#validation-gate`)
  - [ ] Primary mode, the seven gate questions, outputs, exit criteria, rule
- [ ] **Step 4 — Architecture** (H2 anchor: `#architecture`)
  - [ ] Primary mode, purpose, outputs, exit criteria, rule
- [ ] **Step 5 — Sprint Planning** (H2 anchor: `#sprint-planning`)
  - [ ] Primary mode, purpose, outputs, exit criteria, rule
- [ ] **Step 6 — Build & Test** (H2 anchor: `#build-test`)
  - [ ] Primary mode, dry run step, implementation step, outputs, exit criteria, rule
- [ ] **Step 7 — Review & Reflection** (H2 anchor: `#review-reflection`)
  - [ ] Primary mode, purpose, outputs, exit criteria, rule
- [ ] **Step 8 — Deploy, Maintain, or Resume** (H2 anchor: `#deploy-maintain-resume`)
  - [ ] Primary mode, the seven next-state options, outputs, exit criteria, rule
- [ ] Mode-to-lifecycle mapping table (from §8.4)
- [ ] Scale examples section (new project, new feature, sprint, patch — from §8.5)
- [ ] Images: `_PDF/images/5_8-Step Lifecycle.png`, `_PDF/images/4_Scale  Lifecycle  Mode interlock.png`
- [ ] Source: v3.5 §7, §8

---

## Slice C — Operating Modes

*Four pages: overview + one per mode.*

### C1 — Modes Overview
- [ ] Create `docs/modes/` folder
- [ ] Create `docs/modes/index.md`
- [ ] H1: `Operating Modes`
- [ ] Lede: "Every AI session runs in one explicit mode — the mode answers what the model is allowed to do."
- [ ] TOC
- [ ] Section: mode overview paragraph (one sentence per mode)
- [ ] Mode boundaries table (§5.4): Mode | Primary Action | Writes | Must Not Write
- [ ] Section: "Declaring a mode" — how to declare at session start
- [ ] Links to each mode page + permission levels
- [ ] Image: `_PDF/images/2_Three Operating Modes.png`
- [ ] Source: v3.5 §5

### C2 — Research Mode
- [ ] Create `docs/modes/research-mode.md`
- [ ] H1: `Research Mode`
- [ ] Lede: one sentence
- [ ] TOC
- [ ] Section: "When to use Research Mode" — the use cases list from §5.1
- [ ] Section: "What Research Mode may produce" — output file list
- [ ] Section: "What Research Mode must not do" — the five prohibitions
- [ ] Section: "The Research Mode prompt" — prompt text from §19.1 in a fenced code block
- [ ] **Rule:** `Research Mode gathers evidence. It does not decide or build.`
- [ ] Link to Design Mode (natural next step)
- [ ] Source: v3.5 §5.1, §7.1, §19.1

### C3 — Design Mode
- [ ] Create `docs/modes/design-mode.md`
- [ ] H1: `Design Mode`
- [ ] Lede: one sentence
- [ ] TOC
- [ ] **Note callout at top:** "Design Mode was called *Architect Mode* in earlier versions of the framework. The two terms refer to the same role."
- [ ] Section: "What Design Mode covers" — the 14-item list from §5.2
- [ ] Section: "What Design Mode may create or update" — the full file list
- [ ] Section: "What Design Mode must not do" — the five prohibitions
- [ ] Section: "Design Mode prompts" — project init prompt (§19.2), sprint pack prompt (§19.3), dry run review prompt (§19.5), resumption prompt (§19.7) — each in a fenced code block with a H3 label
- [ ] **Rule:** `Design Mode writes Markdown project memory. It does not write implementation.`
- [ ] Source: v3.5 §5.2, §19.2, §19.3, §19.5, §19.7

### C4 — Develop Mode
- [ ] Create `docs/modes/develop-mode.md`
- [ ] H1: `Develop Mode`
- [ ] Lede: one sentence
- [ ] TOC
- [ ] **Note callout at top:** "Develop Mode was called *Builder Mode* in earlier versions of the framework."
- [ ] Section: "What Develop Mode may create or modify" — implementation file list
- [ ] Section: "What Develop Mode must do" — the 10 requirements
- [ ] Section: "What Develop Mode must not do" — the 8 prohibitions
- [ ] Section: "The dry run requirement" — explanation + image reference
- [ ] Section: "Develop Mode prompts" — dry run prompt (§19.4), authorization prompt (§19.6) — each in a fenced code block
- [ ] **Rule:** `Develop Mode changes implementation files only after dry run approval.`
- [ ] Link to permission levels page
- [ ] Image: `_PDF/images/8_Dry Run Approval Gate.png`
- [ ] Source: v3.5 §5.3, §19.4, §19.6

---

## Slice D — Work Scale & Sprint Loop

### D1 — Work Scale Model
- [ ] Create `docs/work-scale.md`
- [ ] H1: `Work Scale Model`
- [ ] Lede: "Scale determines how much process is appropriate — a patch and a new project must not follow the same workflow."
- [ ] TOC
- [ ] Section per scale (Project, Release, Feature, Sprint, Patch) — each with definition + examples
- [ ] Scale-to-process mapping table (§6.6)
- [ ] **Rule:** `Do not run a project process for a patch. Do not run a patch process for a project.`
- [ ] Image: `_PDF/images/3_Work Scale Model.png`
- [ ] Source: v3.5 §6

### D2 — Sprint Loop
- [ ] Create `docs/sprint-loop.md`
- [ ] H1: `Sprint Loop`
- [ ] Lede: one sentence on what the sprint loop controls
- [ ] TOC
- [ ] Overview: numbered list of all 11 steps
- [ ] Section per step (§12.2–12.12) — each as H3 with what happens and who acts
- [ ] Permission level authorization example (the exact text from §12.8)
- [ ] **Rule:** `A sprint ends when state is updated, not when code compiles.`
- [ ] Image: `_PDF/images/7_Sprint Loop.png`
- [ ] Source: v3.5 §12

---

## Slice E — Project Brain & File Reference

### E1 — Project Brain
- [ ] Create `docs/project-brain.md`
- [ ] H1: `The Project Brain`
- [ ] Lede: "The Project Brain is the file-backed memory layer — it must be current, explicit, scoped, reviewable, searchable, versioned, and safe to load into an LLM session."
- [ ] TOC
- [ ] Section: "Core files" — file list with one-line responsibility for each (from §9.4 table)
- [ ] Section: "Sprint files" — file list with one-line responsibility each
- [ ] Section: "Release and feature files" — file list
- [ ] Section: "Properties of good project memory" — the 7 properties from §9.4
- [ ] File responsibilities table (§9.4) — full table
- [ ] **Rule:** `If a model needs to know it later, write it to the project brain.`
- [ ] Image: `_PDF/images/6_Project Brain file map.png`
- [ ] Source: v3.5 §9

### E2 — File Reference
- [ ] Create `docs/file-reference.md`
- [ ] H1: `File Reference`
- [ ] Lede: "Template and purpose for every project brain file."
- [ ] TOC
- [ ] Section per file template:
  - [ ] `AGENTS.md` — purpose + full template from §18.1
  - [ ] `STATE.md` — purpose + full template from §18.2
  - [ ] `DOMAIN.md` — purpose + full template from §18.3
  - [ ] `DECISIONS.md` — purpose + full template from §18.4
  - [ ] Sprint Pack (`requirements.md`, `blueprint.md`, `acceptance.md`) — purpose + all three templates from §18.5
- [ ] **Rule:** `Templates are starting points, not decoration. Remove sections that do not apply.`
- [ ] Source: v3.5 §18

---

## Slice F — Prompt Catalog

### F1 — Prompt Catalog
- [ ] Create `docs/prompt-catalog.md`
- [ ] H1: `Prompt Catalog`
- [ ] Lede: "Copy-paste prompts for every framework mode and workflow — research, planning, implementation, review, and resumption."
- [ ] TOC
- [ ] Intro: "Store prompts under `prompts/research/`, `prompts/design/`, `prompts/develop/`"
- [ ] Section: "Research Mode Prompt" (§19.1) — purpose, files to load, prompt in fenced code block
- [ ] Section: "Design Mode — Project Initialization" (§19.2) — purpose, files to load, prompt
- [ ] Section: "Design Mode — Sprint Pack Generation" (§19.3) — purpose, files to load, prompt
- [ ] Section: "Develop Mode — Dry Run" (§19.4) — purpose, files to load, prompt
- [ ] Section: "Design Mode — Dry Run Review" (§19.5) — purpose, files to load, prompt
- [ ] Section: "Develop Mode — Authorization" (§19.6) — purpose, files to load, prompt
- [ ] Section: "Resumption Prompt" (§19.7) — purpose, files to load, prompt
- [ ] **Rule:** `Prompts are executable protocol. Keep them terse.`
- [ ] Source: v3.5 §19

---

## Slice G — Handoff, Repository, Setup

### G1 — Handoff Protocol
- [ ] Create `docs/handoff-protocol.md`
- [ ] H1: `Handoff, Resumption & Model Switching`
- [ ] Lede: "ADDF treats model handoff as a normal operating condition — a new model resumes from files, not from memory."
- [ ] TOC
- [ ] Section: "Session checkpoint protocol" — the file update list from §14.1
- [ ] Section: "Handoff summary template" — full template from §14.2 in a fenced MD code block
- [ ] Section: "Incoming model protocol" — the file load list + wait-for-authorization rule from §14.3
- [ ] Section: "The resumption prompt" — link to prompt catalog and include the prompt text for convenience
- [ ] **Rule:** `The next model resumes from files, not from memory.`
- [ ] Image: `_PDF/images/9_Handoff and Resumption.png`
- [ ] Source: v3.5 §14, §19.7

### G2 — Repository Structure
- [ ] Create `docs/repository-structure.md`
- [ ] H1: `Repository Structure`
- [ ] Lede: one sentence
- [ ] TOC
- [ ] Section: "Standard ADDF project" — full folder tree from §16.1 in fenced code block
- [ ] Section: "Minimum viable ADDF" — folder tree from §16.2 + explanation of what each file does
- [ ] Section: "Public ADDF repository" — folder tree from §16.3
- [ ] **Rule:** `The folder structure should make the operating model visible.`
- [ ] Image: `_PDF/images/12_Repository structure.png`, `_PDF/images/11_Starter kit structure.png`
- [ ] Source: v3.5 §16

### G3 — Initial Setup
- [ ] Create `docs/initial-setup.md`
- [ ] H1: `Initial Setup`
- [ ] Lede: one sentence
- [ ] TOC
- [ ] Section: "Create the project" — bash commands from §17.1 in fenced bash code block
- [ ] Section: "Populate files in order" — the 8-file sequence (numbered list)
- [ ] Section: "First session" — the mode sequence from §17.3
- [ ] Note: link to getting-started.md for the 20-minute walkthrough; this page covers the technical scaffold only
- [ ] **Rule:** `Fill SECURITY.md before loading files into an AI session.`
- [ ] Image: `_PDF/images/10_First-session onboarding flow.png`
- [ ] Source: v3.5 §17

---

## Slice H — Permission Levels & Cycles

### H1 — Permission Levels
- [ ] Create `docs/permission-levels.md`
- [ ] H1: `Develop Mode Permission Levels`
- [ ] Lede: "Permission levels apply only to Develop Mode — they control how far the model may reach beyond the approved sprint scope."
- [ ] TOC
- [ ] Section: the permission levels table (§13) — Level | Name | Meaning
- [ ] Section: "How levels are used" — most work starts at 0, proceeds to 1; levels 2–4 require stronger justification
- [ ] Section: "How to authorize a level" — the authorization message pattern from §12.8
- [ ] Section: "Escalation rules" — the model cannot self-authorize; escalation requires explicit human instruction
- [ ] **Rule:** `Permission level controls Develop Mode freedom.`
- [ ] Source: v3.5 §13

### H2 — Release Cycles
- [ ] Create `docs/release-cycles.md`
- [ ] H1: `Release Cycles`
- [ ] Lede: "A release groups features into a bounded delivery target — a completed release becomes the baseline for the next."
- [ ] TOC
- [ ] Section: "Release plan" — what a release plan defines (§10.1)
- [ ] Section: "Release folder structure" — folder tree from §10.2
- [ ] Section: "Starting a new version" — load list + Design Mode output from §10.3
- [ ] Section: "Release completion criteria" — the 8-item checklist from §10.4
- [ ] **Rule:** `A new release updates the project brain. It does not restart the project from zero.`
- [ ] Source: v3.5 §10

### H3 — Feature Cycles
- [ ] Create `docs/feature-cycles.md`
- [ ] H1: `Feature Cycles`
- [ ] Lede: "A feature cycle adds a capability to an existing project without restarting the full lifecycle."
- [ ] TOC
- [ ] Section: "Feature flow" — the 8-step flow from §11.1 (numbered list)
- [ ] Section: "Feature folder structure" — folder tree from §11.2
- [ ] Section: "Feature brief template" — full template from §11.3 in a fenced MD code block
- [ ] **Rule:** `A feature cycle extends the project. It does not erase existing state.`
- [ ] Source: v3.5 §11

---

## Slice I — Domain Adaptations & Examples

### I1 — Domain Adaptations
- [ ] Create `docs/domain-adaptations.md`
- [ ] H1: `Domain Adaptations`
- [ ] Lede: "ADDF is domain-agnostic — the structure stays stable and the domain files adapt."
- [ ] TOC
- [ ] Section per domain (§20.1–20.5):
  - [ ] Web Applications — typical entities, typical commands
  - [ ] Game Development — typical entities, note on `DOMAIN.md` as technical game design doc
  - [ ] Desktop Applications — typical entities
  - [ ] Data / Automation — typical entities
  - [ ] Documentation / Framework Projects — typical entities
- [ ] **Rule:** `Keep the structure stable. Adapt the domain files.`
- [ ] Source: v3.5 §20

### I2 — Examples
- [ ] Create `docs/examples.md`
- [ ] H1: `Examples`
- [ ] Lede: "Two worked examples showing ADDF in practice — the Mini Task Tracker and the ADDF public repository."
- [ ] TOC
- [ ] Section: "Mini Task Tracker" (§21)
  - [ ] Work scale breakdown
  - [ ] Lifecycle use summary (each mode and what it did)
  - [ ] Example `DOMAIN.md` from §21.3 in a fenced MD code block
  - [ ] **Rule:** `Small examples stay small. The point is to expose the process, not showcase an app.`
- [ ] Section: "ADDF Public Repository" (§22)
  - [ ] Project scope list
  - [ ] Release plan summary (v0.1–v0.4)
  - [ ] Sprint 001 goal + in-scope / out-of-scope
  - [ ] **Rule:** `The public repository must dogfood the framework.`
- [ ] Image: `_PDF/images/15_Mini Task Tracker scale example.png`, `_PDF/images/14_Public roadmap.png`
- [ ] Source: v3.5 §21, §22

---

## Slice J — Operational Reference

### J1 — Operational Checklists
- [ ] Create `docs/checklists.md`
- [ ] H1: `Operational Checklists`
- [ ] Lede: "Four gate checklists — each is an execution gate, not a suggestion."
- [ ] TOC
- [ ] Section: "Before first AI session" — checklist from §23.1 (markdown checkboxes)
- [ ] Section: "Before Develop Mode" — checklist from §23.2
- [ ] Section: "Before authorizing development" — checklist from §23.3
- [ ] Section: "Before commit" — checklist from §23.4
- [ ] **Rule:** `A checklist is an execution gate, not a suggestion.`
- [ ] Source: v3.5 §23

### J2 — Failure Handling & Troubleshooting
- [ ] Create `docs/troubleshooting.md`
- [ ] H1: `Failure Handling & Troubleshooting`
- [ ] Lede: "Failure recovery begins by writing state — not by asking the model to try again."
- [ ] TOC
- [ ] Section: "Develop Mode touched unapproved files" (§24.1) — 5-step action list
- [ ] Section: "The model invented business logic" (§24.2) — 6-step action list
- [ ] Section: "Project state is confused" (§24.3) — Design Mode consistency audit: load list + ask
- [ ] Section: "Model runs out of context" (§24.4) — Session Checkpoint Protocol: 3-file update + resumption prompt
- [ ] **Rule:** `Failure recovery begins by writing state, not by asking for another fix.`
- [ ] Source: v3.5 §24

---

## Slice K — Reference Pages

### K1 — Agile Comparison
- [ ] Create `docs/agile-comparison.md`
- [ ] H1: `ADDF and Agile`
- [ ] Lede: "ADDF borrows useful language from Agile. It is not Scrum."
- [ ] TOC
- [ ] Section: "What ADDF uses from Agile" — bullet list (backlog, sprint, acceptance criteria, review, retrospective, release, iteration)
- [ ] Section: "What ADDF does not require" — bullet list (Scrum Master, Product Owner, daily standups, story points, velocity tracking, ceremony cadence, two-week sprint)
- [ ] Section: "Sprint definition in ADDF" — a sprint is a bounded AI implementation packet, defined by artifacts not duration
- [ ] Term mapping table: Agile/Scrum term | ADDF equivalent (from §15.2)
- [ ] **Rule:** `Use Agile language where it clarifies. Do not import Scrum ceremony.`
- [ ] Source: v3.5 §15

### K2 — Glossary
- [ ] Create `docs/glossary.md`
- [ ] H1: `Glossary`
- [ ] Lede: "Canonical definitions for all ADDF framework terms."
- [ ] Alphabetical definition list — each term as H3, definition as paragraph, with link to the relevant wiki page
- [ ] Terms to include (from v3.5 §25 + STYLE_GUIDE §20):
  - [ ] ADDF
  - [ ] Context Engineering
  - [ ] Design Mode (with Architect Mode alias note)
  - [ ] Develop Mode (with Builder Mode alias note)
  - [ ] Dry Run
  - [ ] Feature
  - [ ] Handoff Summary
  - [ ] Local File Sovereignty
  - [ ] Patch
  - [ ] Permission Level
  - [ ] Project Brain
  - [ ] Release
  - [ ] Research Mode
  - [ ] Sprint
  - [ ] Sprint Pack
  - [ ] Validation Gate
  - [ ] Work Scale
- [ ] *Quack!* footer (earned here — final page of the wiki)
- [ ] Source: v3.5 §25, STYLE_GUIDE §11, §20

---

## Completion Checklist

When all slices are done, verify the following before declaring the wiki complete:

- [ ] Every page in `Docs_List.md` exists as a file.
- [ ] Every internal link in every page resolves to an existing file.
- [ ] `docs/index.md` navigation table covers all 25 pages.
- [ ] README links that use different filenames are bridged in `docs/index.md`.
- [ ] `docs/DOCS_Notes.md` has notes from every slice.
- [ ] No banned words appear in any page (spot-check 5 random pages).
- [ ] Every page has a **Rule:** callout with a rule from the source.
- [ ] `docs/glossary.md` is the only page with a *Quack!* footer.

---

*ADDF · `docs/Docs_Todo.md` · generated 2026-05-25*
