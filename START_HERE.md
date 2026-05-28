# START_HERE.md

**The Autonomous Duck Deployment Framework — first session guide.**

You downloaded this. Here is what to do first.

---

## What you need

- A project directory. It can be an existing project or a new one.
- A capable LLM. Any of these work: Claude, Codex, ChatGPT, Gemini, or any model you can give a system prompt to.
- A text editor.
- Git (recommended but not required for your first session).

ADDF does not require a specific LLM. It does not require a CLI. It does not require any account or subscription beyond the model you are already using.

---

## The first session, step by step

### Step 1 — Copy the starter kit

Copy the contents of `starter-kit/blank/` into your project directory.

```
your-project/
├── AGENTS.md
├── DOMAIN.md
├── STATE.md
├── DECISIONS.md
├── COMMANDS.md
├── STYLE_GUIDE.md
├── SECURITY.md
├── QUESTIONS.md
├── RISKS.md
├── GIT_STRATEGY.md
├── PROMPT_CHANGELOG.md
└── planning/
    └── sprints/
        └── sprint_001/
```

If you only want the minimal setup, copy only:

```
AGENTS.md
DOMAIN.md
STATE.md
COMMANDS.md
SECURITY.md
planning/sprints/sprint_001/
```

### Step 2 — Fill `SECURITY.md`

Open `SECURITY.md`. Add the files in your project that must never be loaded into an LLM session. At minimum:

```
- Any .env file
- Any file containing API keys or credentials
- Any file with personal contact information
- Any file with private infrastructure paths
```

Add any additional files specific to your project. Do this before opening any AI session. It takes five minutes and protects you indefinitely.

### Step 3 — Fill `AGENTS.md`

Open `AGENTS.md`. The starter kit provides a complete template. Read it and confirm the mode definitions, the dry run approval rule, and the safe-to-load list match your project context.

For most projects, the starter kit version of `AGENTS.md` is correct as-is. The key things to verify:

- The safe-to-load list does not include anything from your `SECURITY.md`.
- The three modes (Research Mode, Design Mode, Develop Mode) match how you intend to work.

### Step 4 — Draft `DOMAIN.md`

Open `DOMAIN.md`. Replace the placeholder content with your project's:

- What the project is.
- What it is not.
- Scope for the first release.
- Key entities and terminology.
- Domain rules.

This does not need to be perfect. It needs to be honest. A sparse `DOMAIN.md` is better than a missing one.

### Step 5 — Initialize `STATE.md`

Open `STATE.md`. Set:

```
Current Goal: [What you are trying to achieve]
Active Release: v0.1
Active Sprint: Sprint 001
Current Status: Project brain initialized. Ready for first Design Mode session.
Next Step: Run Design Mode to generate Sprint 001 sprint pack.
```

### Step 6 — Run Research Mode if unknowns exist

If your project has significant unknowns — technology choices, architecture decisions, third-party integrations you haven't evaluated — open a Research Mode session before Design Mode.

Load into the session: `AGENTS.md`, `STATE.md`, `DOMAIN.md`, `QUESTIONS.md`.

Tell the model:

```
You are operating in Research Mode.
Goal: [Investigate the specific unknown].
```

Research Mode produces notes and updates `QUESTIONS.md`. It does not make decisions. You make the decisions based on what it finds.

If your unknowns are small or already resolved, skip this step and go to Step 7.

### Step 7 — Run Design Mode to create the project brain

Open a Design Mode session.

Load into the session: `AGENTS.md`, `STATE.md`, `DOMAIN.md`, and any relevant research notes.

Tell the model:

```
You are operating in Design Mode for [project name].
Goal: Complete the project brain files for the first sprint.
Create or refine: DOMAIN.md, DECISIONS.md, RISKS.md, QUESTIONS.md, STYLE_GUIDE.md, COMMANDS.md, GIT_STRATEGY.md.
```

Review every file the model produces. Update anything that is wrong or incomplete. The model generates a starting structure — you are responsible for accuracy.

### Step 8 — Run Design Mode to create Sprint 001

In the same or a new Design Mode session:

Load: `AGENTS.md`, `STATE.md`, `DOMAIN.md`, `DECISIONS.md`.

Tell the model:

```
You are operating in Design Mode for [project name].
Goal: Generate the Sprint 001 sprint pack.
Files to create:
- planning/sprints/sprint_001/requirements.md
- planning/sprints/sprint_001/blueprint.md
- planning/sprints/sprint_001/acceptance.md
```

Review the sprint pack. The requirements must reflect what you actually want to build. The blueprint must list every file to be created or modified. The acceptance criteria must be specific and testable.

Do not proceed to Develop Mode until the sprint pack is correct.

### Step 9 — Run Develop Mode at Permission Level 0

Open a Develop Mode session.

Load: `AGENTS.md`, `STATE.md`, `DOMAIN.md`, `planning/sprints/sprint_001/requirements.md`, `planning/sprints/sprint_001/blueprint.md`, `planning/sprints/sprint_001/acceptance.md`.

Tell the model:

```
You are operating in Develop Mode.
Permission Level: 0.
Produce dry_run.md. Do not implement anything yet.
```

The model produces `dry_run.md` — a complete list of every file it intends to create or modify, with a reason for each change. This is the only output of a Level 0 session. The model must not touch any implementation file.

### Step 10 — Review the dry run

Read `dry_run.md` carefully.

Ask yourself:
- Does this list match what the blueprint says?
- Are there any files listed that should not be touched?
- Are there any files missing that should be touched?
- Does anything look unexpected?

If the dry run is wrong, reject it. Send it to a Design Mode session for review. Update the blueprint if needed. Run Develop Mode at Level 0 again.

Do not authorize if you have doubts.

### Step 11 — Authorize development

When the dry run is correct, send the authorization to the Develop Mode session:

```
Dry run approved.
Permission Level 1 authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

The model implements the sprint. It modifies only the files listed in `blueprint.md` and `dry_run.md`.

### Step 12 — Verify output

Check the implementation against `acceptance.md`.

- Did the model create the files specified?
- Do the files contain the expected content?
- Are there any unintended changes to files outside the blueprint?

Run any tests or manual checks needed. If something is wrong, document it in `human_review.md` and decide whether to patch or revert.

### Step 13 — Update state

When the sprint is complete and verified:

1. Update `STATE.md`: set the next sprint, current status, and next step.
2. Fill `planning/sprints/sprint_001/implementation_log.md` with what was done.
3. Fill `planning/sprints/sprint_001/human_review.md` with your review notes.
4. Write a brief `planning/sprints/sprint_001/retrospective.md`.

### Step 14 — Commit

```
git add .
git commit -m "feat(sprint-001): complete sprint 001 deliverables"
```

### Step 15 — Close or checkpoint the AI session

End the Develop Mode session. You do not need to save the chat history — the files are the record.

If you are mid-sprint and need to stop, run the session checkpoint prompt first:

```
You are operating in Design Mode.
Goal: Write a session checkpoint for the current state of the project.
Create: planning/sprints/sprint_001/session_checkpoint.md
Include: what was completed, what is in progress, what the next step is, and what files to load to resume.
```

---

## Next sessions

Every subsequent session follows the same pattern:

1. Declare the mode.
2. Load `AGENTS.md` and `STATE.md`.
3. Load the files relevant to the task.
4. State the session goal.
5. Work inside the mode boundaries.
6. Update the project brain when the session ends.

The model has no memory between sessions. The files do.

---

## Where to go from here

- [Full manual](docs/full-manual.md) — complete framework reference.
- [Modes](docs/modes.md) — Research Mode, Design Mode, and Develop Mode in detail.
- [Lifecycle](docs/lifecycle.md) — the 8-step lifecycle explained.
- [Prompt catalog](docs/prompt-catalog.md) — copy-ready prompts for every mode.
- [Mini Task Tracker example](examples/mini-task-tracker/) — a complete small project.
- [Handoff protocol](docs/handoff-protocol.md) — how to hand work to a different model.

---

**Rule:** If a model needs to know it later, write it to the project brain.

*Quack!*

---

*ADDF · `START_HERE.md` · v0.1 · Framework v3.5*
