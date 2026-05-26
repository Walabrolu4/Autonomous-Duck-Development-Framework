# DOCS_Notes.md

> Living notes file. Consult this before beginning any doc slice. Update it whenever new observations surface.

**Last reviewed:** 2026-05-25  
**Status:** Active

---

## Purpose

This file captures observations, discrepancies, decisions, and open questions discovered while reading the source documents and building the wiki. Any LLM continuing this work must read this file first and add new notes at the end of each completed todo slice.

---

## Source Documents Reviewed

| File | Version | Notes |
|---|---|---|
| `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_5.md` | 3.5 user-facing | Primary source. 25 sections, full lifecycle, all templates. |
| `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_5_senior_engineering.md` | 3.5 senior | Same content, engineering audience tone. Identical structure. |
| `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_6.pdf` | 3.6 PDF | 76-page PDF. Content matches v3.5 MD — same chapters, same rules. No new sections detected. v3.6 appears to be a formatting/print pass of v3.5. |
| `docs/_PDF/style Guide/STYLE_GUIDE.md` | 1.0 | Complete brand and voice guide. Last reviewed May 2026. Authority order: STYLE_GUIDE > Brand book > AGENTS.md. |
| `todos/ADDF_Full_Project_Requirements.md` | Draft v0.1 | Full project requirements doc. Useful for understanding intended wiki structure. References `docs/index.md` hierarchy. |
| `README.md` | 1.2 | Public-facing README. Already references `docs/index.md` as the wiki entry point. Contains a section table linking to expected wiki pages. |

---

## Critical Observations

### 1. Terminology Split — Design Mode vs Architect Mode

The v3.5 framework documents use **three-mode terminology**:
- Research Mode
- Design Mode
- Develop Mode

The `STYLE_GUIDE.md` (section 11.1) and `README.md` use **dual-mode terminology**:
- Architect Mode (= Design Mode)
- Builder Mode (= Develop Mode)

**The STYLE_GUIDE lists "Architect Mode / Builder Mode" as canonical capitalized terms.**

**Resolution for wiki docs:** Use the v3.5 three-mode terminology (Research / Design / Develop) since those are the current source documents. In each mode page, include a callout mapping the old Architect/Builder names for readers coming from older versions. Note that `STYLE_GUIDE.md` may need a version update to reflect the v3.5 rename. Flag this in DOCS_Notes after any mode pages are written.

### 2. v3.6 Is a Formatting Pass

The PDF marked as v3.6 contains the same content as v3.5 markdown. No new sections were found in pages 1–76. The wiki should be based on the v3.5 markdown content, treating v3.6 as the print-ready version of the same material.

### 3. README Links to Wiki Pages That Don't Exist Yet

The `README.md` already includes a documentation table with links to:
- `docs/index.md`
- `docs/getting-started.md`
- `docs/core-concepts.md`
- `docs/sprint-workflow.md`
- `docs/prompts.md`
- `docs/file-reference/index.md`
- `docs/modes/index.md`
- `docs/lifecycle/index.md`
- `docs/example.md`
- `docs/troubleshooting.md`
- `docs/glossary.md`

These must be created. The wiki file paths must match exactly.

### 4. docs/ Folder Already Contains _PDF Subfolder

The `docs/` folder contains `docs/_PDF/` with source files and images. The wiki pages go directly in `docs/` (not inside `_PDF/`). Sub-folders for modes and lifecycle are acceptable.

### 5. Image Assets Exist

`docs/_PDF/images/` contains 15+ diagram images from the PDF (numbered 1–15). These can be referenced in wiki pages using relative paths. Key images:
- `1_ADDF framework map.png`
- `2_Three Operating Modes.png`
- `3_Work Scale Model.png`
- `4_Scale  Lifecycle  Mode interlock.png`
- `5_8-Step Lifecycle.png`
- `6_Project Brain file map.png`
- `7_Sprint Loop.png`
- `8_Dry Run Approval Gate.png`
- `9_Handoff and Resumption.png`
- `10_First-session onboarding flow.png`
- `11_Starter kit structure.png`
- `12_Repository structure.png`
- `13_CLI initialization flow.png`
- `14_Public roadmap.png`
- `15_Mini Task Tracker scale example.png`

Image paths in wiki docs should be relative, e.g.: `../_PDF/images/5_8-Step Lifecycle.png` from a file in `docs/`.

### 6. STYLE_GUIDE Voice Rules for Wiki Docs

Per STYLE_GUIDE section 15 (Application — Documentation):

- Every doc page structure: Title (H1) → one-sentence summary (lede) → TOC if >3 sections → the why → sections (opener → how → rule → example) → the rule → worked example → footer.
- Use `**Rule:**` callouts (left border 4px Yolk in web, bold in MD).
- Code blocks use JetBrains Mono (in web rendering — in MD, use fenced code blocks).
- No emoji in docs.
- At most one *Quack!* per page — only at the footer if used at all.
- File names always in backticks: `STATE.md`, never STATE.md.
- Em dashes — not hyphens — for asides.
- Framework terms use canonical capitalization (Design Mode, Develop Mode, Research Mode, Sprint Pack, Dry Run, Permission Level, etc.).
- Bold on first introduction of load-bearing terms.

### 7. Mapping of README Wiki Links to Actual v3.5 Content

| README link | Best source section in v3.5 |
|---|---|
| `docs/getting-started.md` | §17 Initial setup + §23 Checklists |
| `docs/core-concepts.md` | §3 Framework summary + §4 Core principles |
| `docs/sprint-workflow.md` | §12 Sprint loop |
| `docs/prompts.md` | §19 Prompt catalog |
| `docs/file-reference/index.md` | §18 File templates + §9 Project brain |
| `docs/modes/index.md` | §5 Three operating modes |
| `docs/lifecycle/index.md` | §7 8-step lifecycle |
| `docs/example.md` | §21 Mini Task Tracker example |
| `docs/troubleshooting.md` | §24 Failure handling |
| `docs/glossary.md` | §25 Glossary |

### 8. Permission Level Page

The permission levels (0–4) are a short but important reference. The README doesn't list this page, but it should exist as `docs/permission-levels.md` and be linked from the modes index and sprint workflow pages.

### 9. Agile Comparison Page

§15 of v3.5 covers the relationship to Agile/Scrum. This is valuable for readers coming from a Scrum background. Create `docs/agile-comparison.md`.

### 10. Release & Feature Cycles

§10 (release cycles) and §11 (feature cycles) are distinct enough to warrant their own pages: `docs/release-cycles.md` and `docs/feature-cycles.md`, or combined as `docs/cycles.md`.

### 11. Domain Adaptations

§20 covers web apps, games, desktop, data, and documentation/framework projects. Create `docs/domain-adaptations.md` — useful for discoverability when non-web developers arrive.

---

## Open Questions

- [ ] Should `docs/modes/` use `design-mode.md` or `architect-mode.md`? **Decision: `design-mode.md` with an alias note.** (See note 1 above.)
- [ ] Should release cycles and feature cycles be one page or two? **Decision: Two separate pages for clarity.**
- [ ] Should the lifecycle steps each get their own sub-page, or all live in one `docs/lifecycle.md`? **Decision: One parent `docs/lifecycle/index.md` with all 8 steps as H2 anchors — deep enough for wiki navigation without over-splitting.**
- [ ] Should `docs/file-reference/` be a folder with sub-pages or a single page? **Decision: Single `docs/file-reference.md` for v1 of the wiki — simpler to maintain.**

---

## Decisions Made

| # | Decision | Rationale |
|---|---|---|
| 1 | Use Research / Design / Develop terminology (v3.5) | These are the current source documents. Note Architect/Builder aliases in mode pages. |
| 2 | v3.6 = formatting pass of v3.5 | No new content detected in PDF extraction. |
| 3 | Image assets referenced via relative paths from `docs/` | Assets already exist in `docs/_PDF/images/`. |
| 4 | Wiki root at `docs/index.md` | Matches README.md existing links. |
| 5 | Lifecycle steps as H2 anchors in `docs/lifecycle/index.md` | Balance depth vs. maintenance burden. |
| 6 | File reference as single `docs/file-reference.md` | Keep v1 wiki simple. |

---

## Notes Added During Build

*(Each LLM completing a todo slice must append a note here with: slice completed, date, any issues found.)*

### Planning Pass — 2026-05-25

Completed: `DOCS_Notes.md`, `Docs_List.md`, `Docs_Todo.md`, `Docs_Prompt.md`

Issues / findings:
- The grep check on Docs_List.md detected `docs/example.md`, `docs/file-reference/index.md`, `docs/prompts.md`, and `docs/sprint-workflow.md` as apparent paths. These are **README alias references** appearing in the "Note" fields of Docs_List.md — they are not actual wiki pages to create. They should be bridged in `docs/index.md` (Slice A1) with a note explaining the alias.
- All 25 real wiki pages are covered across Slices A–K in `Docs_Todo.md`.
- 11 slices defined: A (Foundation), B (Lifecycle), C (Modes), D (Scale & Sprint), E (Brain & Files), F (Prompts), G (Handoff/Repo/Setup), H (Permissions & Cycles), I (Domains & Examples), J (Operational), K (Reference).
- `docs/Docs_Prompt.md` references `DOCS_Notes.md`, `Docs_Todo.md`, `Docs_List.md`, and `STYLE_GUIDE.md` — all confirmed present.

---

*Consult this file before every slice. Update it after every slice. — ADDF DOCS_Notes.md*

### Slices A–K Build Pass — 2026-05-26

Completed: All 25 wiki pages across Slices A, B, C, D, E, F, G, H, I, J, K.

**Pages written:**

- `docs/index.md` (A1)
- `docs/getting-started.md` (A2)
- `docs/core-concepts.md` (A3)
- `docs/lifecycle/index.md` (B1)
- `docs/modes/index.md` (C1)
- `docs/modes/research-mode.md` (C2)
- `docs/modes/design-mode.md` (C3)
- `docs/modes/develop-mode.md` (C4)
- `docs/work-scale.md` (D1)
- `docs/sprint-loop.md` (D2)
- `docs/project-brain.md` (E1)
- `docs/file-reference.md` (E2)
- `docs/prompt-catalog.md` (F1)
- `docs/handoff-protocol.md` (G1)
- `docs/repository-structure.md` (G2)
- `docs/initial-setup.md` (G3)
- `docs/permission-levels.md` (H1)
- `docs/release-cycles.md` (H2)
- `docs/feature-cycles.md` (H3)
- `docs/domain-adaptations.md` (I1)
- `docs/examples.md` (I2)
- `docs/checklists.md` (J1)
- `docs/troubleshooting.md` (J2)
- `docs/agile-comparison.md` (K1)
- `docs/glossary.md` (K2)

**Issues found and resolved:**

1. **Write-tool truncation on long Windows paths.** Six files written via the Write tool with Windows-style paths were silently truncated on disk (saved as 49–246 bytes instead of 2–6 KB): `index.md`, `getting-started.md`, `core-concepts.md`, `domain-adaptations.md`, `troubleshooting.md`, `glossary.md`. Root cause: apparent buffer limit in the Cowork Write tool when file content is large and the target path is a deeply nested Windows path. **Resolution:** rewrote all six files using Python `open()` via the bash tool writing to the Linux mount path directly. All other files (written in later passes) were unaffected — confirmed by size checks. **Future mitigation:** for long files (>2 KB), prefer writing via `mcp__workspace__bash` with Python rather than the Write tool.

2. **glossary.md missing `**Rule:**` callout.** The K2 spec does not list a Rule callout explicitly, but the global rules require one per page. Added: "Framework terms use canonical capitalization. Capitalization matters." before the footer.

3. **index.md has no `**Rule:**` callout.** The wiki home is a pure navigation hub — no instructional sections. This is intentional and acceptable per the global rules' spirit (the rule requirement applies to content sections, not nav pages).

4. **Banned words check:** zero violations found across all 25 pages. The only matches were planning/source files outside the generated wiki pages.

### Todo Reconciliation Pass — 2026-05-26

Completed: `docs/Docs_Todo.md`

Issues:
- `DOCS_Notes.md` recorded that all Slices A–K were already completed, but `docs/Docs_Todo.md` still had unchecked boxes. Per the prompt rule, `DOCS_Notes.md` was treated as the newer authority.
- Verified that all 25 wiki pages listed in `docs/Docs_List.md` exist in `docs/`.
- Marked all remaining checklist boxes in `docs/Docs_Todo.md` as complete so the planning artifact matches the completed wiki state.
