# Docs_Prompt.md

> Copy-paste this entire prompt into any capable LLM to continue building the ADDF wiki.
> The prompt is self-contained — the LLM needs only this text and access to the repo folder.

---

## HOW TO USE THIS PROMPT

1. Open the folder: `E:\_Projects\Others\Autonomous Duck Deployment Framework\Autonomous Duck deployment Framework\` (or the repo root wherever it lives on your machine).
2. Copy everything below the horizontal rule into a new LLM session.
3. Grant the LLM file-read and file-write access to the repo folder.
4. The LLM will read `docs/DOCS_Notes.md` first, then check `docs/Docs_Todo.md` to find the next uncompleted slice, and proceed.

---

---

## PROMPT (copy from here)

You are working on the **Autonomous Duck Deployment Framework (ADDF)** documentation wiki.

Your job is to **build the next uncompleted todo slice** from `docs/Docs_Todo.md` and write the corresponding Markdown files into the `docs/` folder.

---

### STEP 1 — Read these files before doing anything else

Read all four of these files in full:

1. `docs/DOCS_Notes.md` — critical observations, decisions, and open questions. This is your briefing. Do not skip it.
2. `docs/Docs_Todo.md` — the full todo list. Find the next slice where NOT all items are marked `[x]`. That is your target slice.
3. `docs/Docs_List.md` — the page inventory. Use it to check correct file paths, titles, and link relationships.
4. `docs/_PDF/style Guide/STYLE_GUIDE.md` — the style authority. Every page you write must comply with it.

---

### STEP 2 — Identify the next slice

In `docs/Docs_Todo.md`, slices are labelled **Slice A**, **Slice B**, …, **Slice K**.

A slice is complete when every `- [ ]` in it has been changed to `- [x]`.

Find the first incomplete slice. That is the only slice you work on in this session.

If the current session runs long or you approach context limits before finishing the slice, checkpoint correctly (see Step 5).

---

### STEP 3 — Read the source documents

The primary source is:

- `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_5.md`

For engineering-depth details, also read:

- `docs/_PDF/Autonomous_Duck_Deployment_Framework_v3_5_senior_engineering.md`

Each todo item in `Docs_Todo.md` lists the relevant source section (e.g., "Source: v3.5 §7, §8"). Read those sections before writing.

---

### STEP 4 — Write the pages

For each page in your target slice:

1. Create the file at the path listed in `Docs_Todo.md` (relative to repo root). Create any sub-folders needed.
2. Write the page content following the todo item checklist exactly.
3. Apply the global rules from the top of `Docs_Todo.md` to every page:
   - Canonical capitalization for framework terms.
   - File names in backticks.
   - No banned words (just, simply, easy, basically, amazing, powerful, seamless, unleash, supercharge, let's, magical, AI-powered, best practice, unlock).
   - Em dashes — not hyphens — for asides.
   - **Rule:** callout in each section.
   - No emoji.
   - At most one *Quack!* per page (footer only, and only on the glossary page per convention).
   - Internal links as relative paths.
   - Page footer with link back to wiki root and `ADDF v3.5` version tag.
4. When a todo item is complete, mark it `[x]` in `docs/Docs_Todo.md`.

---

### STEP 5 — After completing a slice (or before stopping)

1. Mark all completed items `[x]` in `docs/Docs_Todo.md`.
2. Append a note to `docs/DOCS_Notes.md` under "Notes Added During Build":

```
### Slice [LETTER] — [Date]
Completed: [list of files created]
Issues: [any discrepancies found, decisions made, things to flag for next LLM]
```

3. If you found any new information, conflicts, or questions while writing — add them to `DOCS_Notes.md` under the relevant section before the build notes.

---

### WRITING STYLE QUICK REFERENCE

From `STYLE_GUIDE.md` (full guide in `docs/_PDF/style Guide/STYLE_GUIDE.md`):

**Voice:** Declarative over suggestive. Concrete over abstract. Write like a senior engineer explaining a process to a peer.

**Structure per page:**
1. H1 title
2. One-sentence lede
3. TOC (if more than 3 sections)
4. The why (2–4 sentences)
5. Sections — each with: opener → how → rule → example
6. **Rule:** callout quoting the non-negotiable
7. Footer: link back to index + version

**Terminology (always capitalized):**
- Research Mode, Design Mode, Develop Mode
- Sprint Pack, Dry Run, Permission Level
- Project Brain, Local File Sovereignty, Context Engineering
- Validation Gate

**File names:** always in backticks — `` `STATE.md` ``, `` `dry_run.md` ``, `` `AGENTS.md` ``

**Design Mode note:** Older versions of ADDF called Design Mode "Architect Mode" and Develop Mode "Builder Mode". When writing mode pages, include a callout noting the alias.

**Images:** Reference existing images via relative path from the `docs/` folder:
- `_PDF/images/5_8-Step Lifecycle.png`
- `_PDF/images/2_Three Operating Modes.png`
- `_PDF/images/7_Sprint Loop.png`
- `_PDF/images/8_Dry Run Approval Gate.png`
- `_PDF/images/9_Handoff and Resumption.png`
- (and others — full list in `DOCS_Notes.md` section 5)

---

### FOLDER STRUCTURE REFERENCE

The wiki lives in `docs/`. Do not touch `docs/_PDF/` (source documents only).

```
docs/
├── index.md                    ← Wiki root
├── getting-started.md
├── core-concepts.md
├── work-scale.md
├── sprint-loop.md
├── project-brain.md
├── file-reference.md
├── prompt-catalog.md
├── handoff-protocol.md
├── repository-structure.md
├── initial-setup.md
├── permission-levels.md
├── release-cycles.md
├── feature-cycles.md
├── domain-adaptations.md
├── examples.md
├── checklists.md
├── troubleshooting.md
├── agile-comparison.md
├── glossary.md
├── lifecycle/
│   └── index.md
├── modes/
│   ├── index.md
│   ├── research-mode.md
│   ├── design-mode.md
│   └── develop-mode.md
├── Docs_List.md                ← Page inventory (planning artifact)
├── Docs_Todo.md                ← Todo list (planning artifact — mark items [x] as you go)
├── Docs_Prompt.md              ← This file
├── DOCS_Notes.md               ← Living notes — read first, update after each slice
└── _PDF/                       ← Source documents — DO NOT MODIFY
```

---

### IMPORTANT RULES

- Do not modify any file in `docs/_PDF/`.
- Do not modify `docs/Docs_List.md` or `docs/Docs_Prompt.md` unless you find an error that must be corrected (add a note to `DOCS_Notes.md` if you do).
- Do not rename any file from the path listed in `Docs_Todo.md`.
- If you find a conflict between `DOCS_Notes.md` and `Docs_Todo.md`, follow `DOCS_Notes.md` (it is more recent) and record the conflict.
- Complete the entire target slice before stopping if possible. If context runs short, complete the current page, checkpoint, and leave clear notes for the next session.

---

*Begin by reading `docs/DOCS_Notes.md`. Then find the next incomplete slice in `docs/Docs_Todo.md`. Then build.*

---

## END OF PROMPT
