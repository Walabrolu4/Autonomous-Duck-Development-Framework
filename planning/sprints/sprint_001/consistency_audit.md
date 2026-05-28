# Consistency Audit — Project Brain Files

**Project:** Autonomous Duck Deployment Framework — Public Repository  
**Mode:** Design Mode  
**Scope:** 12 generated project brain files  
**References:** `todos/ADDF_Project_Requirements_v2_1.md`, `docs/modes/`, `docs/sprint-loop.md`, `docs/permission-levels.md`, `docs/project-brain.md`, `docs/handoff-protocol.md`, `docs/_PDF/style Guide/STYLE_GUIDE.md`  
**Date:** 2026-05-27  
**Auditor:** Design Mode session

---

## AGENTS.md

**Status: FAIL**

### Issues

**Issue A1 — Dry run content definition is incomplete.**

`AGENTS.md` Section 2, Step 3 defines the dry run as:

> "a complete list of every file the model intends to create, modify, or delete, with a brief reason for each change."

`docs/modes/develop-mode.md` (The dry run requirement) specifies that `dry_run.md` must list:

```
- files to create
- files to modify
- files to move or delete
- commands to run
- dependencies requested
- risks
- ambiguities
```

The generated definition omits: "move or delete" (files to move are not the same as files to delete), "commands to run," "dependencies requested," "risks," and "ambiguities." These omissions are significant — the dependency and risk fields exist precisely to trigger the Dependency Approval Gate (Sprint Loop Step 6) before authorization is given.

**Issue A2 — Develop Mode "Writes to" list is missing two files.**

`AGENTS.md` Section 1 (Develop Mode) and Section 6 (mode boundaries summary table) both state:

> **Writes to:** Implementation files approved in `blueprint.md`, `implementation_log.md`.

`docs/modes/develop-mode.md` (What Develop Mode may create or modify) explicitly lists three Markdown files Develop Mode may write:

```
dry_run.md
implementation_log.md
handoff_summary.md
```

`dry_run.md` and `handoff_summary.md` are both missing from the "Writes to" lists in Sections 1 and 6. This matters: `dry_run.md` is the first output of every Develop Mode session, and `handoff_summary.md` is required before any model handoff or context limit. Omitting them from the boundary definition creates a gap in the session contract.

**Issue A3 — Dependency Approval Gate is absent from the dry run sequence.**

`AGENTS.md` Section 2 condenses the post-dry-run review into one step:

> "5. The human (or Design Mode review) approves or rejects the dry run."

`docs/sprint-loop.md` defines a distinct Step 6 — Dependency Approval Gate — between the dry run review and authorization:

> "Any new dependency named in `dry_run.md` requires a `DECISIONS.md` entry before implementation proceeds."

This gate is not mentioned. An operator reading only `AGENTS.md` would not know that a new dependency discovered in the dry run cannot be authorized without first recording a decision. This is a meaningful omission in the session contract.

**Issue A4 — Research Mode "Must not write to" is over-broad.**

`AGENTS.md` Section 1 (Research Mode) states:

> **Must not write to:** `planning/sprints/`, `docs/` (substantive changes), implementation files.

`docs/modes/research-mode.md` states:

> "These files go in the `research/` folder or the relevant sprint or feature folder."

The blanket prohibition on writing to `planning/sprints/` prevents Research Mode from writing research notes into a sprint's subfolder — which the documentation explicitly permits. The intent is to prevent Research Mode from modifying sprint plan files (`requirements.md`, `blueprint.md`, `acceptance.md`), not to prohibit research notes in sprint folders.

### Recommendations

**A1:** Replace the dry run description in Section 2, Step 3 with:

> "Produce `dry_run.md` listing: files to create, files to modify, files to move or delete, commands to run, dependencies requested, risks, and ambiguities. Stop after producing this file."

**A2:** In both the Develop Mode "Writes to" entry in Section 1 and the mode boundaries table in Section 6, add `dry_run.md` and `handoff_summary.md`:

> **Writes to:** `dry_run.md`, `implementation_log.md`, `handoff_summary.md`, implementation files approved in `blueprint.md`.

**A3:** Expand step 5 of the dry run sequence to two steps:

> "5. The human (or Design Mode review) approves or rejects the dry run.  
> 5a. If `dry_run.md` lists any new dependency, a `DECISIONS.md` entry recording that dependency is required before authorization can be given."

**A4:** Change the Research Mode "Must not write to" restriction from:

> `planning/sprints/`

to:

> `planning/sprints/sprint_NNN/requirements.md`, `planning/sprints/sprint_NNN/blueprint.md`, `planning/sprints/sprint_NNN/acceptance.md` (sprint plan files — those belong to Design Mode)

---

## DOMAIN.md

**Status: FAIL**

### Issues

**Issue D1 — Incorrect prompt group count.**

`DOMAIN.md` Section 4, in-scope list, line 73:

> `prompts/ (all four groups)`

`todos/ADDF_Project_Requirements_v2_1.md` Section 11.2 defines five prompt groups:

```
Research Prompts
Design Prompts
Develop Prompts
Handoff / Resumption Prompts
Maintenance Prompts
```

This is confirmed by `PROMPT_CHANGELOG.md` which correctly lists all five groups. "All four groups" is factually incorrect and inconsistent with both the requirements and `PROMPT_CHANGELOG.md` within the same commit.

**Issue D2 — Out-of-scope table is missing four items from requirements section 4.**

The requirements document Section 4 (Non-goals) defines 14 explicit non-goals. Four are absent from the `DOMAIN.md` out-of-scope table:

| Missing item | Requirements section 4 entry |
|---|---|
| Complex SaaS dashboard | "A complex SaaS dashboard." |
| Fully automated agent runner | "A fully automated agent runner." |
| Deep IDE integration | "Deep IDE integration." |
| Specific LLM requirement | "Any requirement to use a specific LLM." |

Note: "Anything that requires a specific LLM" appears in Section 3 ("What this project is not") but is absent from the formal out-of-scope table in Section 4. Moving it there would make the table the complete authority.

### Recommendations

**D1:** Change "all four groups" to "all five groups" in the in-scope list. For precision, expand to:

> `prompts/` (five groups: Research, Design, Develop, Handoff/Resumption, Maintenance)

**D2:** Add the four missing rows to the out-of-scope table:

| Complex SaaS dashboard | Not planned |
| Fully automated agent runner | Not planned |
| Deep IDE integration | Not planned |
| Requirement to use a specific LLM | Not planned |

Move "Anything that requires a specific LLM" from Section 3 into the table as well, or add a cross-reference.

---

## DECISIONS.md

**Status: PASS**

### Notes

Decision 001 matches `todos/ADDF_Project_Requirements_v2_1.md` Section 20.3 exactly. Title, Status, Context, Decision, and Tradeoffs are reproduced faithfully.

The generated format extends the requirements template by adding `Date`, `Decided by`, and `Consequences` sections. These are additive — they do not contradict the template. `Consequences` provides useful context that `Tradeoffs` does not fully cover. No correction needed.

Decisions 002–007 correctly capture the Recommended Starting Decisions from Section 25 and the two pending questions (license, prompt distribution format), with appropriate cross-references to `QUESTIONS.md`.

---

## QUESTIONS.md

**Status: PASS**

All ten open questions from `todos/ADDF_Project_Requirements_v2_1.md` Section 24 are present and numbered Q001–Q010:

| Requirements Q | QUESTIONS.md entry |
|---|---|
| License | Q001 ✓ |
| CLI package name | Q002 ✓ |
| Static website only | Q003 ✓ |
| Release folders in starter kit | Q004 ✓ |
| `DECISIONS.md` in minimal ADDF | Q005 ✓ |
| Onboarding app in v0.1 | Q006 ✓ |
| Visual assets for v0.1 | Q007 ✓ |
| Planning history visibility | Q008 ✓ |
| CLI language | Q009 ✓ |
| Prompt distribution format | Q010 ✓ |

No questions are missing. Each entry is correctly marked Open with blocking information and a date. The `## Resolved questions` section is present and ready.

---

## RISKS.md

**Status: PASS**

All nine risks are project-specific. No generic placeholder risks are present. Each risk is traceable to a concrete ADDF concern:

- Risk 001 (Terminology drift) — directly tied to the Architect/Builder → Research/Design/Develop transition.
- Risk 002 (Documentation outpacing structure) — specific to the sprint sequencing dependency (starter kit before docs).
- Risk 003 (Scope creep) — specific to the v0.1/v0.2/v0.3 release boundary.
- Risk 004 (Secrets in public repository) — project-specific given the public repo context.
- Risk 005 (AI-generated content contradicting the framework) — specific to the meta-problem of using AI to document an AI methodology.
- Risk 006 (Example project calibration) — specific to Mini Task Tracker.
- Risk 007 (Brand inconsistency across surfaces) — specific to the multi-artifact release model.
- Risk 008 (Handoff protocol not tested) — specific to a core framework claim.
- Risk 009 (Version misalignment) — specific to the multi-artifact versioning strategy.

No risk contradicts framework guidance. Risk 004 is consistent with `SECURITY.md`. Risk 001 correctly references `STYLE_GUIDE.md` as the mitigation anchor. Risk 002 correctly references the sprint sequence from Section 22 of the requirements.

---

## STYLE_GUIDE.md

**Status: WARNING**

### Issues

**Issue S1 — Pre-existing full brand guide uses superseded terminology.**

The generated project brain `STYLE_GUIDE.md` correctly defines the three public modes (Research Mode, Design Mode, Develop Mode) and explicitly states "Do not use Architect Mode or Builder Mode as public ADDF modes."

However, the pre-existing full brand guide at `docs/_PDF/style Guide/STYLE_GUIDE.md` still lists in its vocabulary table (Section 11.1):

> | **Architect Mode** / **Builder Mode** | No | Always capitalized. |

And in Section 2.4:
> "We are not 'an AI assistant for developers.' The Architect and Builder are roles, not products."

This creates an intra-repository contradiction. An operator loading the full brand guide will find Architect Mode / Builder Mode as primary capitalized terms — directly contradicting both the generated `STYLE_GUIDE.md` and Decision 002.

This is a defect in a pre-existing file, not in the generated project brain file. The project brain `STYLE_GUIDE.md` is correct. The pre-existing file requires updating.

### Notes

The voice description matches both the requirements document (Section 16.2: "declarative, concrete, peer-level, precise, and occasionally wry") and the full brand guide (Section 10.1: "declarative, concrete, occasionally wry, never cute"). No conflict.

The `Quack!` usage rule is correctly present in Section 7 ("at most once per page, only at the end of a long-form document, at a success moment, or in an empty state"). The full brand guide additionally permits `Quack!` as the "stinger of a release-note title" — this specific usage is absent from the project brain quick reference but is covered by the "full reference" pointer at the bottom of the file.

### Recommendation

**S1:** Create a task (add to `planning/backlog.md`) to update `docs/_PDF/style Guide/STYLE_GUIDE.md` Section 11.1 vocabulary table before v0.1 public release. Replace `Architect Mode / Builder Mode` entries with `Research Mode`, `Design Mode`, and `Develop Mode`. Update the Section 2.4 framing to reflect the public mode terminology decision.

This is a v0.1 blocking item — the full brand guide is a public-facing artifact.

---

## GIT_STRATEGY.md

**Status: PASS**

Branch naming pattern (`sprint/NNN-short-description`) matches the full brand guide Section 17.3 exactly.

Commit message format (Conventional Commits, no emoji, no exclamation marks, no personal pronouns) matches the full brand guide Section 17.2 exactly.

PR structure (Context, What changed, Verification, Out of scope) matches the requirements document Section 19.4 PR requirements.

Release process is internally consistent with `VERSION.md` and `CHANGELOG.md`. The 10-step release sequence is complete and does not contradict any framework documentation.

---

## COMMANDS.md

**Status: PASS**

Commands are appropriately scoped to v0.1. Website and CLI commands are correctly marked as out-of-scope stubs with target version labels. No commands reference tools or frameworks that are not part of the current project scope.

The validation section (Section 8) correctly includes a `git grep` command for secret detection, consistent with `SECURITY.md` and Risk 004 in `RISKS.md`.

---

## PROMPT_CHANGELOG.md

**Status: PASS**

All five prompt groups are correctly listed (Research, Design, Develop, Handoff, Maintenance) — consistent with requirements Section 11.2. This makes `PROMPT_CHANGELOG.md` internally consistent with the requirements document and contradicts the error in `DOMAIN.md` ("all four groups"), confirming that error is isolated to `DOMAIN.md`.

The breaking-change convention is clearly defined and aligns with the importance of authorization gate semantics in Develop Mode prompts.

---

## START_HERE.md

**Status: PASS**

All 15 first-session steps from `todos/ADDF_Project_Requirements_v2_1.md` Sections 3.2 and 8.4 are present and in the correct sequence:

| Requirements step | START_HERE.md step |
|---|---|
| Copy or clone the starter kit | Step 1 ✓ |
| Fill `SECURITY.md` | Step 2 ✓ |
| Fill `AGENTS.md` | Step 3 ✓ |
| Draft `DOMAIN.md` | Step 4 ✓ |
| Initialize `STATE.md` | Step 5 ✓ |
| Run Research Mode if unknowns exist | Step 6 ✓ |
| Run Design Mode to create project memory | Step 7 ✓ |
| Run Design Mode to generate Sprint 001 | Step 8 ✓ |
| Run Develop Mode at Permission Level 0 | Step 9 ✓ |
| Review `dry_run.md` | Step 10 ✓ |
| Authorize Develop Mode | Step 11 ✓ |
| Verify output | Step 12 ✓ |
| Update state | Step 13 ✓ |
| Commit | Step 14 ✓ |
| Close or checkpoint the AI session | Step 15 ✓ |

### Note

Step 11 uses the abbreviated authorization message form from `docs/sprint-loop.md` Step 7. The extended form in `docs/modes/develop-mode.md` includes additional rules (log all changes, run verification, stop if ambiguity appears, produce handoff notes). The abbreviated form is appropriate for a first-session guide; the full prompt belongs in the prompt catalog. No correction needed.

---

## VERSION.md

**Status: PASS**

Version registry covers all required artifacts (framework manual, starter kit, prompt catalog, examples, diagrams, website, CLI, onboarding app). Release history starts correctly at v0.0.1.

Framework manual version history correctly identifies 3.5 as the current public version.

---

## CHANGELOG.md

**Status: WARNING**

### Issue

**Issue C1 — `SECURITY.md` is listed outside the project brain files group.**

In the v0.0.1 entry, `SECURITY.md` appears as a standalone bullet:

> "SECURITY.md — security and never-load rules."

It is listed separately from the project brain files block:

> "Project brain files: AGENTS.md, DOMAIN.md, DECISIONS.md, COMMANDS.md, QUESTIONS.md, RISKS.md, STYLE_GUIDE.md, GIT_STRATEGY.md, PROMPT_CHANGELOG.md."

`docs/project-brain.md` and requirements Section 6.1 both explicitly include `SECURITY.md` as a required project brain file. The separation in the changelog creates a false impression that it occupies a different category.

### Recommendation

**C1:** Move `SECURITY.md` into the project brain files list in the v0.0.1 CHANGELOG entry so the entry correctly represents it as a project brain file:

> "Project brain files: AGENTS.md, DOMAIN.md, STATE.md, DECISIONS.md, COMMANDS.md, STYLE_GUIDE.md, SECURITY.md, QUESTIONS.md, RISKS.md, GIT_STRATEGY.md, PROMPT_CHANGELOG.md."

---

## All files — global checks

### Terminology violations

**Forbidden mode names (Architect Mode, Builder Mode) appearing as primary modes:**

Scan result:

| File | Finding |
|---|---|
| `AGENTS.md` | "Do not refer to Architect Mode or Builder Mode as public ADDF modes." — correct usage (prohibition) ✓ |
| `DOMAIN.md` | "Do not refer to Architect Mode or Builder Mode as public ADDF modes." — correct usage (prohibition) ✓ |
| `DECISIONS.md` | Decision 002: "Architect Mode and Builder Mode are not exposed as primary public modes." — correct usage ✓ |
| `STYLE_GUIDE.md` | "Do not use Architect Mode or Builder Mode as public ADDF modes." — correct usage ✓ |
| `docs/_PDF/style Guide/STYLE_GUIDE.md` | **VIOLATION (pre-existing file):** Section 11.1 lists "Architect Mode / Builder Mode — Always capitalized." This file requires remediation before v0.1 public release. |

No generated project brain file uses Architect Mode or Builder Mode as a primary mode name. The violation exists in a pre-existing file.

**Non-framework terminology found in generated files:**

None found. All generated files use Research Mode, Design Mode, and Develop Mode consistently.

**"Users" instead of "operators":**

`AGENTS.md`, `DOMAIN.md`, `STYLE_GUIDE.md`, `RISKS.md`, `START_HERE.md` — all use "operator" or "operators" as the primary term. No "users" violations found.

**File names not wrapped in backticks:**

Spot-checked. All file names in prose are wrapped in backticks across all generated files. No violations found.

**Emoji:**

No emoji found in any generated file. `Quack!` appears correctly (once each, at the end of `START_HERE.md`; absent from other files where it would be inappropriate). No violations found.

### Missing required sections

| File | Required sections per spec | Status |
|---|---|---|
| `AGENTS.md` | Mode definitions, dry run rule, permission levels, safe-to-load list, session protocol | Present (with defects noted above) |
| `DOMAIN.md` | Project identity, scope, out-of-scope, entities, terminology, rules | Present (with defects noted above) |
| `DECISIONS.md` | Status, Context, Decision, Tradeoffs for Decision 001 | Present |
| `QUESTIONS.md` | All 10 section-24 questions, resolved section | Present |
| `RISKS.md` | Project-specific risks with mitigation | Present |
| `STYLE_GUIDE.md` | Voice, terminology, banned words, no-emoji rule, Quack! rule | Present |
| `GIT_STRATEGY.md` | Branching, commits, PRs, release process | Present |
| `COMMANDS.md` | Run, test, build, deploy, rollback | Present |
| `PROMPT_CHANGELOG.md` | Version history, format convention, breaking change definition | Present |
| `START_HERE.md` | All 15 first-session steps | Present |
| `VERSION.md` | Artifact version registry, release history, versioning scheme | Present |
| `CHANGELOG.md` | Format convention, unreleased section, v0.0.1 entry | Present |

---

## Audit summary

### Files that passed with no issues

- `DECISIONS.md`
- `QUESTIONS.md`
- `RISKS.md`
- `GIT_STRATEGY.md`
- `COMMANDS.md`
- `PROMPT_CHANGELOG.md`
- `START_HERE.md`
- `VERSION.md`

### Files that need correction

| File | Severity | Issues |
|---|---|---|
| `AGENTS.md` | **FAIL — correct before use** | A1: Dry run definition incomplete. A2: Develop Mode write list missing `dry_run.md` and `handoff_summary.md`. A3: Dependency Approval Gate absent. A4: Research Mode write restriction over-broad. |
| `DOMAIN.md` | **FAIL — correct before use** | D1: Prompt group count wrong ("four" should be "five"). D2: Four non-goals missing from out-of-scope table. |
| `STYLE_GUIDE.md` | **WARNING — action required on pre-existing file** | S1: Full brand guide at `docs/_PDF/style Guide/STYLE_GUIDE.md` uses superseded Architect/Builder terminology. Generated file is correct; pre-existing file needs update. |
| `CHANGELOG.md` | **WARNING — minor correction** | C1: `SECURITY.md` listed outside the project brain files group. |

### Terminology violations found

- No terminology violations in the 12 generated project brain files.
- One pre-existing violation: `docs/_PDF/style Guide/STYLE_GUIDE.md` Section 11.1 and Section 2.4 use Architect Mode / Builder Mode as primary canonical terms. This contradicts Decision 002 and must be resolved before v0.1 public release.

### Missing required content

- `AGENTS.md`: missing `dry_run.md` and `handoff_summary.md` from Develop Mode write boundary; missing full dry run content definition; missing Dependency Approval Gate.
- `DOMAIN.md`: missing four requirements Section 4 non-goals from out-of-scope table; incorrect prompt group count.
- No other required content is missing.

### Blocking items before first sprint authorization

The following must be corrected before a Design Mode session generates the Sprint 001 sprint pack:

1. `AGENTS.md` Issues A1, A2, A3 — the dry run rule definition and Develop Mode write boundary are used by every sprint.
2. `DOMAIN.md` Issue D1 — an incorrect fact in the project scope definition.
3. `DOMAIN.md` Issue D2 — incomplete non-goals list used for scope validation.

`AGENTS.md` Issue A4, `STYLE_GUIDE.md` Issue S1, and `CHANGELOG.md` Issue C1 are not blocking for sprint authorization but must be resolved before v0.1 public release.

---

*ADDF · `planning/sprints/sprint_001/consistency_audit.md` · Design Mode · 2026-05-27*
