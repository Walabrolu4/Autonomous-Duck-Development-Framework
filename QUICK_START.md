# ADDF Light Games — Quick Start

**Start with an idea, a question, or an existing game.** The AI facilitates research, design, implementation, refinement, and human acceptance. You make the consequential decisions; the agent maintains project files and follows approvals.

> This is the **game-development edition** on `ADDF_light_games`. The original ADDF framework remains on `main`. This Quick Start is part of the **Stage 3 starter-kit candidate**, not a production-tested release.

## What you need

- A Markdown-capable project folder and an AI assistant. A coding agent (e.g., Claude Code or Codex) is useful for later implementation, but **not required for discovery and design**.
- A game idea is **optional**. No engine, programming language, database, cloud account, Notion workspace, or OpenClaw installation is required to begin.
- Permission to create a few Markdown files in **your own game project**, not inside the ADDF framework repository.

## 1. Choose a starting point

- **No idea:** “I want to make a small game, but I don't have a concept. Guide me with a few interesting, buildable options.”
- **An idea:** “I want to make a top-down game where you steer a boat through a storm. Help me find a small first playable version.”
- **Existing project:** “I already have a game. First audit the repo read-only, identify what works and what is missing, then propose one next sprint. Do not overwrite my files.”

You can use your own words; these are examples, not exact commands.

## 2. Install the smallest project brain

**For a brand-new game folder**, copy the **six files** inside [`starter-kit/minimal/`](starter-kit/minimal/) into the *root of your game project*, preserving the `planning/` subfolder:

```text
my-game/
├── AGENTS.md
├── SECURITY.md
├── GAME.md
├── STATE.md
├── DECISIONS.md
└── planning/
    └── BACKLOG.md
```

Do **not** copy the framework repository's root `AGENTS.md`; that belongs to the original full ADDF edition. Do **not** copy `starter-kit/blank/`; that is the inherited full-ADDF starter kit.

For an **existing game**, do not automatically copy or overwrite any files. Follow the [existing-project adoption guide](starter-kit/EXISTING_PROJECTS.md): read-only inventory, conflict report, human-approved migration.

**No `sprint-001` directory yet.** It appears only after you select a testable milestone.

## 3. Start a conversation

Point the AI at **your game project folder** if its tools permit file access. Otherwise, provide the six Markdown files in the chat and have it draft changes for you to review and save. Use this first-session message:

> Use ADDF Light Games. First read SECURITY.md, AGENTS.md and STATE.md, then GAME.md, DECISIONS.md and planning/BACKLOG.md as needed. We are in discovery; **do not edit game code**. Help me choose one small playable outcome using one meaningful question at a time. Identify facts, assumptions and unknowns; explain key tradeoffs without overwhelming me. Maintain these project files if you have authorized file access; otherwise show me the edits. Do not claim I approved decisions I have not made. Stop before implementation and show me the sprint plan and exact proposed file/command changes.

Then add your idea—or simply say you have none.

**First session without file tools:** the AI can still facilitate discussion and produce proposed Markdown; you copy approved text into your own project. File-backed continuity matters more than an orchestration product.

## 4. Research and choose a first slice

The AI should:
1. Summarize your concept and constraints (or suggest 2–3 small game concepts if none).
2. Ask only the next meaningful decision question; “I'm not sure” is valid.
3. Explain relevant alternatives and why a choice matters.
4. Propose **one** observable milestone; for example, “Move an avatar in a 2D arena and avoid one clearly visible obstacle.”
5. Record the chosen direction in `GAME.md` and, for significant choices, `DECISIONS.md`.
6. Select a backlog item or research spike. Create the next sprint's three files only after selecting that milestone.

### The sprint pack

After the first milestone is selected, copy the three **distribution templates** from [`starter-kit/sprint-template/`](starter-kit/sprint-template/) to `planning/sprints/sprint-001/` in **your game project**:

```text
planning/sprints/sprint-001/
├── SPRINT.md  # outcome, research, tradeoffs, acceptance tests, Gate D
├── PLAN.md    # dry run: files, commands, dependencies, risks, Gate I
└── REVIEW.md  # evidence, playtest, refinements, Gate A
```

The agent fills the actual fields. Do not claim that a template's placeholder is a human choice, a passed test, or a real approval.

## 5. Review the two checkpoints before code

**Gate D — Design:** You approve the key direction and testable sprint outcome after seeing the tradeoffs. This is **not** permission to edit game code.

**Gate I — Implementation:** Before any game-code/asset/config changes, review `PLAN.md`: exact file operations, commands, dependencies, network and other side effects, risks, rollback, and acceptance checks. Explicitly authorize the displayed revision and scope, or request changes.

An example scoped answer:

> “I approve Sprint 001's design and authorize PLAN.md revision r1 for the listed files and commands only. No publishing, purchases or additional dependencies.”

Only use that wording when you have **actually read and agree with the plan**. Approval can be narrower, split across two messages, or withheld. The AI must **stop** while authorization is missing.

## 6. Implement, playtest and accept (or refine)

Once Gate I is valid, the coding agent implements **only the approved scope**, records actual commands and test results, and prepares `REVIEW.md`. You then run or inspect the game and report whether the promised behavior works and how it feels.

**Gate A — Human acceptance:** Accept, accept with stated conditions, request refinement, reject, or pause. Passing automated tests does **not** equal human acceptance. Any fix that needs new files/dependencies/risk must go through a revised plan and Gate I again. The final status and next action go into `STATE.md`.

The repeating loop is:

```text
Research → Design / Ideation → Implement → Refine → Acceptance
              Gate D             Gate I               Gate A
```

## How to resume next time

Start a new session with:

> “Resume this ADDF Light Games project. Read SECURITY.md, AGENTS.md, STATE.md, then the active sprint's SPRINT.md, PLAN.md and REVIEW.md and relevant decisions. Tell me the last **verified** stage/status, what is authorized, what evidence is missing, and one safe next action. Do not resume coding if an approval cannot be verified.”

AI memory is optional; the repository files are the source of truth. Secrets never belong in chat or the project brain.

## Want examples or more detail?

- [How to install and use the Light starter kit](starter-kit/LIGHT_GAMES.md)
- [Existing-project adoption without overwrites](starter-kit/EXISTING_PROJECTS.md)
- [Stage 3 manual review checklist](starter-kit/STAGE_03_REVIEW.md)
- [Framework Specification](spec/FRAMEWORK_SPEC.md)
- [Project File Contracts](spec/PROJECT_FILE_CONTRACTS.md)
- [Sprint File Contracts](spec/SPRINT_FILE_CONTRACTS.md)
- [Approval Policy](spec/APPROVAL_POLICY.md)

The full wiki, combined manual, provider-specific prompts and live game pilots are **later stages**, not yet validated by this Quick Start.
