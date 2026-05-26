# Initial Setup

Run these commands to scaffold the project, then populate files in the correct order before opening any AI session.

## Table of contents

1. [Create the project](#create-the-project)
2. [Populate files in order](#populate-files-in-order)
3. [First session](#first-session)

---

## Create the project

Run this block from the root of your new project directory:

```bash
mkdir -p src docs research planning/sprints/sprint_001
touch AGENTS.md DOMAIN.md STATE.md DECISIONS.md COMMANDS.md \
      STYLE_GUIDE.md SECURITY.md QUESTIONS.md RISKS.md \
      GIT_STRATEGY.md PROMPT_CHANGELOG.md
touch planning/backlog.md
touch planning/sprints/sprint_001/requirements.md \
      planning/sprints/sprint_001/blueprint.md \
      planning/sprints/sprint_001/acceptance.md \
      planning/sprints/sprint_001/dry_run.md \
      planning/sprints/sprint_001/implementation_log.md \
      planning/sprints/sprint_001/human_review.md \
      planning/sprints/sprint_001/retrospective.md
```

This creates the [standard ADDF project structure](repository-structure.md). All files are empty — you populate them next, in a specific order.

![First-session onboarding flow](_PDF/images/10_First-session onboarding flow.png)

---

## Populate files in order

Fill the core files in this sequence. Each file depends on the one before it:

1. `SECURITY.md` — define safe-to-load and never-load rules before writing anything else
2. `AGENTS.md` — mode rules, permissions, Permission Level scale
3. `DOMAIN.md` — business logic, entities, workflows, in-scope and out-of-scope boundaries
4. `STATE.md` — current goal, active scale, current mode, blockers, next intended step
5. `COMMANDS.md` — run, test, build, deploy, and rollback commands
6. `DECISIONS.md` — starter entries for any architecture decisions already made
7. `QUESTIONS.md` — open unknowns that need resolution before or during design
8. `RISKS.md` — known risks with initial mitigation notes

You do not need all eight files fully complete before opening a session. A filled `SECURITY.md` and a stub `AGENTS.md` and `DOMAIN.md` are enough to run the project initialization prompt with Design Mode and let the model help fill the rest.

See [File Reference](file-reference.md) for the full template for each file.

**Rule:** Fill `SECURITY.md` before loading files into an AI session.

---

## First session

A new project begins with this mode sequence:

```
Research Mode     — if meaningful unknowns exist
Design Mode       — to generate project memory from research and intent
Design Mode       — to generate the first Sprint Pack
Develop Mode      — to produce a dry run
Develop Mode      — to implement after dry run approval
Design Mode       — to review output and update state
```

Open your LLM. Load `AGENTS.md` first, then the files appropriate to the current mode. Declare the mode at the top of the session. Use the prompts in the [Prompt Catalog](prompt-catalog.md).

For a step-by-step walkthrough of the first 20 minutes, see [Getting Started](getting-started.md). This page covers the technical scaffold only.

**Rule:** Declare the mode before the model acts.

---

[← Repository Structure](repository-structure.md) · [← Wiki Home](index.md) · ADDF v3.5
