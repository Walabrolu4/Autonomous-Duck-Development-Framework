# Stage 03 — Starter Kit and Quick Start Review

**Status:** Stage 3 implemented; **awaiting manual human verification and approval**  
**Branch:** `ADDF_light_games`  
**Source contracts:** `spec/PROJECT_FILE_CONTRACTS.md`, `spec/SPRINT_FILE_CONTRACTS.md`  
**Scope:** Onboarding guides and uninstantiated Markdown templates; no game implementation, provider integration, live pilot, ZIP, website deployment, or modification of the original full ADDF root files.

## 1. Files delivered

### Entry points

- [../QUICK_START.md](../QUICK_START.md): First-session guide; no-idea, idea and existing-game starts; gates and resumption.
- [LIGHT_GAMES.md](LIGHT_GAMES.md): Exactly what belongs in the user project, when to copy sprint files, canonical template ownership.
- [EXISTING_PROJECTS.md](EXISTING_PROJECTS.md): Read-only inventory, proposed mapping and human-approved non-destructive adoption.

### Six initial project files

- [minimal/AGENTS.md](minimal/AGENTS.md)
- [minimal/SECURITY.md](minimal/SECURITY.md)
- [minimal/GAME.md](minimal/GAME.md)
- [minimal/STATE.md](minimal/STATE.md)
- [minimal/DECISIONS.md](minimal/DECISIONS.md)
- [minimal/planning/BACKLOG.md](minimal/planning/BACKLOG.md)

The initial project has **no active sprint** and starts in `research` / `discovering` with `authorized: no`. No file inside `minimal/` implies that a user already made design choices, permitted coding, played a game or approved work.

### Three distribution-only sprint templates

- [sprint-template/SPRINT.md](sprint-template/SPRINT.md)
- [sprint-template/PLAN.md](sprint-template/PLAN.md)
- [sprint-template/REVIEW.md](sprint-template/REVIEW.md)

These are **not installed** in the initial six-file project. They are copied into `planning/sprints/sprint-001/` *only when* the first bounded milestone is selected, then populated with project-specific facts before the appropriate approval gates.

## 2. What the framework does *not* claim yet

- The templates are **Markdown specifications**, not executable automation.
- The pilot first sprint has **not** been built or playtested. That belongs to Stage 5.
- No provider-specific Claude Code/Codex/OpenClaw adapters have been created. Those belong to Stage 4.
- No reliable automatic validator has been installed. That belongs to Stage 6.
- The original `starter-kit/blank/` and inherited `starter-kit/README.md` still belong to full ADDF; no accidental migration of those files is intended.
- The framework's original GitHub Pages deployment on `main` remains outside this stage.

## 3. Manual verification checklist

### A. GitHub branch and files

- [ ] I am viewing the `ADDF_light_games` branch, not `main`.
- [ ] The root `QUICK_START.md` exists.
- [ ] The `starter-kit/` folder has `LIGHT_GAMES.md` and `EXISTING_PROJECTS.md`.
- [ ] `starter-kit/minimal/` has the **six** expected Markdown files, including `planning/BACKLOG.md`.
- [ ] `starter-kit/sprint-template/` has **exactly three** named sprint Markdown files.
- [ ] `spec/` still contains the nine approved Stage 1 and Stage 2 specifications.
- [ ] The original full-ADDF `starter-kit/blank/` and existing root files remain intact.

### B. Content and onboarding

- [ ] Quick Start explains no-idea, existing-idea, and existing-project routes.
- [ ] It does **not** demand an engine or paid service to begin discovering a game.
- [ ] It tells the user to copy **only the minimal six** to a new game folder.
- [ ] It clearly warns not to overwrite an existing repo's `AGENTS.md` or other documentation.
- [ ] It introduces `SPRINT.md`, `PLAN.md`, `REVIEW.md` only after a milestone is chosen.
- [ ] The agent, not the novice user, is intended to draft and maintain the Markdown records.
- [ ] The agent can guide research/design in a read-only or manual chat without writing game code.
- [ ] The resumption prompt uses verified project files and avoids assuming earlier authorization.

### C. Safety and permissions

- [ ] The initial `STATE.md` has `active_sprint: none`, `sprint_status: discovering`, `authorized: no`.
- [ ] `SECURITY.md` excludes secrets and unapproved network/external side effects.
- [ ] `AGENTS.md` distinguishes Research, Design, Develop write boundaries.
- [ ] `SPRINT.md` defines a real Gate D design choice and acceptance criteria **before code**.
- [ ] `PLAN.md` defaults Gate I to `pending` and forbids out-of-scope file/command changes.
- [ ] `REVIEW.md` defaults Gate A to `pending`; agent tests do **not** equal human playtesting.
- [ ] Stale plans, new dependencies, public deployment, and destructive commands cause a stop/re-approval.
- [ ] Rejected/failed playtest rounds must remain in the history.

### D. Structural conformance

- [ ] File names and required headings agree with Stage 2 contracts.
- [ ] Required metadata keys are present with valid placeholders or `pending`.
- [ ] Decisions/backlog are empty until there are real items; examples cannot be mistaken for actual choices.
- [ ] Sprint templates' IDs and revisions are intentionally examples and not active project status.
- [ ] Relative links from guides point to real files on this branch.
- [ ] `main` has not changed and no Light website was published.

## 4. Five small dry-run scenarios (instructions for a human review)

**These are manual paper tests**, not claims that AI agents or engines have been run end to end.

| Scenario | Correct outcome |
| --- | --- |
| User starts with no idea | Agent asks one question/offers a few tiny concepts; files stay `discovering`, no sprint/code |
| User chooses a player action | Agent updates `GAME.md` and real `D-###` choice only if selected; drafts one milestone |
| User says “I like the idea” | May complete Gate D if specific and recorded; **never** auto-authorizes implementation |
| New package needed during code work | Agent stops; updates plan revision and asks for new Gate I before installing |
| Game builds but human has not played | Automated result recorded in `REVIEW.md`; Gate A `pending`, no `accepted` |

## 5. Boundary and outstanding work

The files in this stage are a **candidate**. Before later implementation:
- Stage 4 must create robust agent-neutral prompts and provider integrations conforming to these templates.
- Stage 5 must test all three entry routes and one genuinely playable sprint in an isolated example.
- Stage 6 must implement deterministic structural validation and error reporting.
- Stage 7 must add the complete wiki and generated manual; Stage 8 creates branding; Stages 9–10 cover packaging, website and release.

If you find a contract mismatch, fix the template or explicitly revise Stage 2 **before proceeding**. Do not declare a staged manual check to be a live pilot.

## 6. User sign-off

**Stage 03 has been implemented and is paused here, not yet human-approved.**

After checking the files, an explicit response can be:

> “I have reviewed Stage 3, and approve the Quick Start and starter-kit templates. Proceed to Stage 4: agent prompts and optional integrations. Stop again for my review.”

If anything feels too heavyweight, missing or unsafe, request a targeted revision instead. No Stage 4 work is authorized without your instruction.
