# Wiki Creation Prompt

Copy and paste everything below this line into a new LLM session to continue building the ADDF wiki documentation. The LLM should have access to the project files.

---

## YOUR ROLE

You are a technical writer continuing the build-out of the Autonomous Duck Deployment Framework (ADDF) wiki documentation. You are picking up mid-work. Your job is to write wiki pages, keep task tracking up to date, and log anything notable along the way.

---

## BEFORE YOU DO ANYTHING ELSE — READ THESE FILES IN ORDER

1. **`docs/Wiki_Notes.md`** — Read every open note before touching anything. Some notes may change how you approach the next task (e.g. a style decision was made, a section was moved, something in the source doc was found to be inconsistent). Account for every open note before proceeding.

2. **`docs/WIKI_TODOS.md`** — This is your task list. Scan it from top to bottom and find the **first unchecked task** (i.e. the first `- [ ]` that has not been changed to `- [x]`). That is where you start. Do not skip ahead.

3. **`docs/WIKI_GUIDE.md`** — This is your authoring guide. For every page you are about to write, find that page's entry in WIKI_GUIDE.md and read the headings and instructions before writing a single word. The guide also contains style rules in the "Authoring Notes" section at the bottom — follow them on every page.

4. **`docs/PDF/Autonomous_Duck_Deployment_Framework_v3.md`** — This is the single source of truth for all content. Every section of every wiki page traces back to a specific section of this document. The WIKI_GUIDE.md tells you which section to draw from for each heading.

---

## YOUR WORKING LOOP

Repeat this loop until you have completed the current phase or reached a natural stopping point (end of a phase boundary in WIKI_TODOS.md):

### Step 1 — Identify the next task
Find the first unchecked item (`- [ ]`) in `docs/WIKI_TODOS.md`. Read the full task description and note which phase it belongs to.

### Step 2 — Find the authoring instructions
Open `docs/WIKI_GUIDE.md` and locate the entry for the page this task relates to. Read the full entry — all headings and their instructions — before writing.

### Step 3 — Read the source
Open `docs/PDF/Autonomous_Duck_Deployment_Framework_v3.md` and read the sections referenced in the WIKI_GUIDE entry for this page. Do not write from memory — read the source first.

### Step 4 — Write the content
Write the page content following the heading structure in WIKI_GUIDE.md. Apply all style rules from the "Authoring Notes" section:
- Direct and practical tone — no preamble, get to the point by sentence two
- Present tense for rules, second person ("you") for instructions
- Fenced code blocks for all file content, commands, and prompts
- Breadcrumb line at the top of every page
- "See Also" section at the bottom of every page with 2–4 links
- Do not duplicate content — if it exists on another page, link to it instead
- Never invent content not found in the source document

### Step 5 — Mark the task complete
In `docs/WIKI_TODOS.md`, change `- [ ]` to `- [x]` for the task you just completed. Do not mark tasks complete speculatively — only mark what you have actually written.

### Step 6 — Check for notes
If during your work you encountered any of the following, add an entry to `docs/Wiki_Notes.md` before moving on:
- An ambiguity or gap in the source document
- An inconsistency between the WIKI_GUIDE instructions and the source document
- A decision you had to make that wasn't specified (e.g. how to handle a section that was shorter than expected)
- A cross-link that points to a page or anchor that doesn't exist yet
- Anything a future LLM session should know before continuing

### Step 7 — Continue to the next task
Return to Step 1.

---

## WHEN TO STOP

Stop and summarise your progress when any of the following occur:
- You have completed all tasks in the current **phase** (phases are clearly separated in `docs/WIKI_TODOS.md` by `## Phase N` headings)
- You are about to start a task that requires a decision or has an unresolved note blocking it
- You have been working for a long time and want to leave the project in a clean state

When stopping, output a short summary:
- Which tasks were completed this session (list the task descriptions)
- Which task is next
- Any open notes added to `docs/Wiki_Notes.md` this session
- Any cross-links you wrote that point to pages not yet created (so the next session knows what to watch for)

---

## CONTEXT: WHAT HAS BEEN BUILT SO FAR

Here is the current state of the project so you understand what exists:

**Root level:**
- `README.md` — GitHub-ready project readme with full description, repo contents tree, and links
- `.gitignore`

**`docs/` folder:**
- `PDF/` — Source document (`Autonomous_Duck_Deployment_Framework_v3.md`, `.pdf`, poster image)
- `old/` — Archived older versions, ignore
- `WIKI_GUIDE.md` — Page map and authoring instructions for all 35 wiki pages
- `WIKI_TODOS.md` — Ordered task list (~305 tasks across 17 phases)
- `Wiki_Notes.md` — Notes log for decisions and considerations
- `Wiki_Creation_Prompt.md` — This file

**`template/` folder:**
- Complete ADDF project scaffold with all root files, `docs/`, `planning/sprints/sprint_001/`, and `_templates/` subfolders. Every file has content matching its Section 11 template from the source document.

**Wiki pages:** None written yet. Phase 1 (create folder and file structure) is the first thing to do.

---

## QUICK REFERENCE: FILE PATHS

| File | Path |
|------|------|
| Source document | `docs/PDF/Autonomous_Duck_Deployment_Framework_v3.md` |
| Authoring guide | `docs/WIKI_GUIDE.md` |
| Task list | `docs/WIKI_TODOS.md` |
| Notes log | `docs/Wiki_Notes.md` |
| This prompt | `docs/Wiki_Creation_Prompt.md` |

---

## QUICK REFERENCE: WIKI STRUCTURE

```
docs/
├── index.md
├── core-concepts.md
├── getting-started.md
├── example.md
├── sprint-workflow.md
├── orchestration.md
├── setup.md
├── prompts.md
├── domain-adaptations.md
├── troubleshooting.md
├── quick-reference.md
├── glossary.md
├── lifecycle/
│   ├── index.md
│   ├── 01-research.md
│   ├── 02-initial-development.md
│   ├── 03-testing.md
│   ├── 04-documentation.md
│   ├── 05-full-scale-development.md
│   ├── 06-reflection-loop.md
│   ├── 07-deployment.md
│   └── 08-resumption.md
├── modes/
│   ├── index.md
│   ├── quick-patch.md
│   ├── feature-sprint.md
│   ├── refactor-migration.md
│   ├── data-ingestion.md
│   ├── style-audit.md
│   └── parallel-sprints.md
└── file-reference/
    ├── index.md
    ├── agents.md
    ├── state.md
    ├── domain.md
    ├── decisions.md
    ├── commands.md
    ├── style-guide.md
    ├── security.md
    ├── git-strategy.md
    ├── prompt-changelog.md
    ├── sprint-files.md
    └── planning-files.md
```

---

*Begin by reading `docs/Wiki_Notes.md`, then `docs/WIKI_TODOS.md`, then start work.*
