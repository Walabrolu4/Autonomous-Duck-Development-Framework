# ADDF Light — Repository Information Architecture

**Status:** Stage 2 proposed specification · human review required  
**Edition:** ADDF Light (game-development-first, methodology portable)  
**Applies to:** This framework repository's Light branch **and** repositories generated from the starter kit  
**Authority:** [Framework Specification](FRAMEWORK_SPEC.md), [Approval Policy](APPROVAL_POLICY.md), [Workflow States](WORKFLOW_STATES.md)  
**Companion contracts:** [Project Files](PROJECT_FILE_CONTRACTS.md) · [Sprint Files](SPRINT_FILE_CONTRACTS.md) · [Validation and Migration](VALIDATION_AND_MIGRATION.md)

## 1. Two kinds of repository — do not confuse them

**A. Framework distribution repository** — the `feature/addf-light` branch of Autonomous Duck Development Framework. It **documents and distributes** ADDF Light. Its `spec/`, `docs/`, `starter-kit/`, `prompts/`, `examples/`, `assets/`, and `website/` directories are framework-authoring materials.

**B. User's project repository** — a *different*, new or existing game repository. After copying the starter kit, its root `AGENTS.md`, `GAME.md`, `STATE.md`, and other project files describe **that particular game**, not the ADDF Light framework.

The same filename can exist in both places but must not be treated as the same document. For example, the current framework repository's pre-existing full-ADDF `AGENTS.md` is **not** automatically a valid ADDF Light game-project template.

## 2. Repository migration policy: staged, non-destructive

The Light branch was created from the full ADDF `main` branch. Therefore it currently contains the original full framework files, site, starter kits, and documentation. **Their presence does not imply they are Light implementation files.**

During Stage 2:
- Add authoritative design specifications **only** under `spec/`.
- Leave the original root files, `docs/`, `starter-kit/`, `prompts/`, website, assets, and deployment workflow unchanged.
- Do not rename, delete, or overwrite the full-ADDF material yet.
- Do not deploy the Light branch to the production GitHub Pages site.

During later stages:
- Build Light-specific starter-kit and prompt content in isolated paths, with a review checkpoint.
- Only after the working Light kit is validated, decide which legacy paths to replace, archive, or remove **on the Light branch**.
- Preserve full ADDF independently on `main`, with no implicit merge from Light to main.
- Plan any deletion or website-switch explicitly; publishing/merging requires separate authorization.

**Naming policy:** The working branch is `feature/addf-light`; the branded edition is **ADDF Light** (not “light-mode,” and not a light-colored theme). Paths use `kebab-case` for docs and `UPPER_SNAKE.md` for project-brain documents, as indicated below.

## 3. Planned framework-distribution structure

The following is the **target structure**, not a claim that all paths already exist. A stage owns each group, and no group is created merely to make the tree appear complete.

```text
ADDF framework repo — feature/addf-light/
├── README.md                      # Stage 7/9: edition homepage, routes to Quick Start
├── QUICK_START.md                 # Stage 3: shortest executable first-session guide
├── MANUAL.md                      # Stage 7: generated complete single-document manual
├── CHANGELOG.md                   # Stage 10: release history
├── VERSION.md                     # Stage 10: version and compatibility policy
├── LICENSE                        # Retain original until reviewed; obey upstream notices
│
├── spec/                          # Stage 1–2: framework contracts / normative source
│   ├── FRAMEWORK_SPEC.md
│   ├── WORKFLOW_STATES.md
│   ├── APPROVAL_POLICY.md
│   ├── DECISION_PROTOCOL.md
│   ├── REPOSITORY_ARCHITECTURE.md
│   ├── PROJECT_FILE_CONTRACTS.md
│   ├── SPRINT_FILE_CONTRACTS.md
│   ├── VALIDATION_AND_MIGRATION.md
│   └── STAGE_02_REVIEW.md
│
├── docs/                          # Stage 7: source Markdown wiki
│   ├── index.md                   # navigable table of contents
│   ├── foundations/
│   ├── guides/
│   ├── lifecycle/
│   ├── sprints/
│   ├── learning/
│   ├── agents/
│   ├── quality/
│   └── reference/
│
├── starter-kit/                   # Stage 3/5: distributable PROJECT templates
│   ├── README.md                  # how to copy/use the kit
│   ├── minimal/                   # nine canonical project files; empty state is valid
│   ├── extended/                  # optional, additive modules
│   └── examples/                  # filled artifacts for learning
│
├── prompts/                       # Stage 4: agent-neutral task prompts
│   ├── START.md
│   ├── DISCOVER.md
│   ├── RESEARCH.md
│   ├── DESIGN.md
│   ├── PLAN.md
│   ├── IMPLEMENT.md
│   ├── REFINE.md
│   ├── ACCEPT.md
│   └── RESUME.md
│
├── integrations/                  # Stage 4: optional provider adapters
│   ├── claude-code/
│   ├── codex/
│   └── openclaw/
├── examples/                      # Stage 5: end-to-end trials and evidence
│   ├── from-zero/
│   ├── completed-game/
│   └── existing-project/
├── assets/brand/                  # Stage 8: ADDF Light mark and lockups
├── scripts/                       # Stage 6–7: validators and manual generator
└── website/                       # Stage 9: Astro site and distribution
```

**Avoid parallel source directories:** If a website page is rendered from wiki Markdown, its source lives in `docs/`, not in a second handwritten copy within `website/`. The long-form manual is generated from an ordered index; no independent editing of generated `MANUAL.md`.

## 4. Planned project repository: minimum copy-to-root kit

These are the **nine logical Markdown files** installed into the *user's game project*. No other files are mandatory to enter Research and Design. The agent creates sprint files only when a sprint is chosen.

```text
your-game/
├── AGENTS.md                 # rules; reads safety restrictions before acting
├── GAME.md                   # human-owned intent and validated assumptions
├── STATE.md                  # current stage, status, sprint and next step
├── DECISIONS.md              # significant human decisions and reversals
├── SECURITY.md               # excluded files, side-effect and tool limits
├── planning/
│   ├── BACKLOG.md             # future slices, ideas, ordering, dependencies
│   └── sprints/
│       └── sprint-001/
│           ├── SPRINT.md      # research + design + acceptance specification
│           ├── PLAN.md        # dry-run and implementation authorization
│           └── REVIEW.md      # testing, feedback, refinement and human verdict
└── [game source, engine configuration and assets as appropriate]
```

A **brand-new** project may initially have only the five root documents and `planning/BACKLOG.md`, with no sprint directory. A directory is a model, not a requirement to generate blank files. The agent creates `sprint-001/` when a first testable milestone is selected. For a game project that already has `AGENTS.md` or other named files, **no overwrite is allowed** without an explicit reviewed migration.

## 5. Ordering and dependency graph

```text
SECURITY.md → AGENTS.md → GAME.md
                            │
                            ├→ DECISIONS.md
                            ├→ planning/BACKLOG.md
                            └→ STATE.md
                                  │
                                  ▼
                         sprint-NNN/SPRINT.md
                                  │  (Gate D)
                                  ▼
                         sprint-NNN/PLAN.md
                                  │  (Gate I)
                                  ▼
                         approved source changes / test results
                                  │
                                  ▼
                         sprint-NNN/REVIEW.md
                                  │  (Gate A)
                                  ▼
                               STATE.md
                                  │
                                  └→ next prioritized backlog item
```

This is a dependency **reading/recording** order, not a demand that the user fill every file manually. The agent starts the discovery conversation using a safe scaffold and writes the documents progressively.

## 6. Authority hierarchy and conflict resolution

Within a game project:

1. **Security and external constraints:** `SECURITY.md`, applicable law/organizational policy, and direct user restrictions.
2. **Agent behavior:** `AGENTS.md`, so long as it does not weaken higher-priority restrictions.
3. **Human intent and decisions:** current explicit user input, `GAME.md`, and actual evidenced decisions in `DECISIONS.md`.
4. **Authorized work:** active `SPRINT.md` + exact authorized revision of `PLAN.md`.
5. **Evidence and current status:** `REVIEW.md` + `STATE.md`, cross-checked against actual code, git diff and test output.
6. **Backlog and derived summaries:** `BACKLOG.md`, future plans, generated explanations.

**Do not blindly choose “chat always wins” or “file always wins.”** A current user request may legitimately supersede older files, but the agent must record a material change and invalidate any stale implementation approval before acting. An unverified “approved” string in a generated file is not evidence.

When the documents disagree, stop at the safer permission state, report the conflict, and request resolution. No automated “repair” may forge an approval or erase past human verdicts.

## 7. What is canonical versus generated?

| Category | Canonical source | Derived artifact | Owner |
| --- | --- | --- | --- |
| Framework rules | `spec/*.md` | wiki summaries, FAQs, checklists | framework authors / reviewers |
| Public documentation | `docs/**/*.md` | `MANUAL.md`, generated site content | docs maintainers |
| Agent-neutral prompts | `prompts/*.md` | model-specific adapters | prompt maintainers |
| Starter project contract | `starter-kit/minimal/**/*.md` | downloadable ZIP | framework maintainers |
| Example evidence | `examples/**` | screenshots/demo videos | pilot testers |
| Project/game truth | project brain + actual code/tests | summaries and agent context | project user + authorized agents |
| Implementation authorization | specific `PLAN.md` revision + human consent evidence | status summary in `STATE.md` | human owner |
| Acceptance | human verdict + observations in `REVIEW.md` | completion badge/changelog | human owner |

One conceptual rule has two life cycles: framework-spec amendments are reviewed as framework development; a game-project's `AGENTS.md` follows the installed version and needs an explicit migration to new rules. Do not silently update user projects when the framework changes.

## 8. Git and release boundaries

- **Framework repo:** `main` is original ADDF; `feature/addf-light` is the experimental Light edition. No automatic merge into original `main`.
- **Project repo:** ordinary source-controlled game commits; agent implementation occurs on an approved feature branch/worktree when practical. Sprint IDs are not Git branch names.
- **Publishing:** browser previews, releases, downloadable starter ZIPs, and documentation deployments require explicit target and access review. A successful build does not imply publication approval.
- **History:** `DECISIONS.md` is append/supersede rather than overwrite; `REVIEW.md` keeps separate review rounds. The agent does not rewrite acceptance history.
- **Downloads:** package only actual starter-kit files and licenses; exclude source secrets, test credentials, caches, build outputs and temporary research.
- **Website:** the inherited `.github/workflows/deploy.yml` builds/deploys `main` only. Stage 9 must design preview isolation rather than changing that workflow by accident.
- **License:** retain attribution and verify that distributable Light material and new assets are licensed consistently; do not assume a license covers a new logo automatically.

## 9. Optional modules: complexity is additive

| Optional module | Why add it | When to activate |
| --- | --- | --- |
| `docs/architecture.md` | architectural decisions and interfaces | multiple subsystems or agents |
| `docs/validation.md` | test matrix and device coverage | larger gameplay systems |
| `docs/assets.md` | provenance, file format, asset pipeline | generated/third-party assets grow |
| `planning/releases/` | release scope, notes, shipping gates | multiple shipping milestones |
| `planning/features/` | break a feature across sprints | larger features |
| `research/` | in-depth sourced investigations | a short sprint research section is insufficient |
| `planning/RISKS.md` | accumulated cross-sprint risks | several material risks accumulate |
| `COMMANDS.md` | canonical run/test/export commands | build steps become complex |
| `docs/permissions.md` | permissions matrix beyond default gates | teams, remote agents, regulated work |
| Full ADDF | formal tiers, richer governance and delivery audits | migrations, sensitive systems, multi-team work |

An optional module should be introduced by **need**, with its purpose and link from the existing project brain. Its absence is not a validation failure.

## 10. Local and cloud interoperability

ADDF Light is a **methodology**, not a hosting stack. Local Claude Code, Codex, a browser chat, or optional OpenClaw can load and update the same project files subject to tool permissions. Canva and Notion are useful for brainstorming and knowledge management but do **not** become authoritative substitutes for the file-backed decisions and authorized sprint contracts unless an explicit sync mechanism and review policy are defined.

A zero-configuration manual path remains required: user copies templates and pastes the next prompt; if autonomous tools are not installed, the framework can still guide decisions, produce a plan, and prepare a review checklist.

## 11. Documentation acceptance rules

Stage 7 must ensure:
- Every wiki page has a specific purpose, when-to-use criterion, exact procedure, example, failure mode and related links.
- The Quick Start begins at zero context and does **not** force the full manual.
- `MANUAL.md` is generated from wiki source in documented order and carries a generation notice.
- All links resolve within the Light branch or intentionally point to the parent ADDF edition.
- Light/Original comparison remains discoverable from the README, wiki and manual.
- Versioned kit ZIP and examples match the contracts—not an obsolete design.

## 12. Stage 2 boundary and manual review

This file is **specification only**. It does not instantiate `starter-kit/minimal`, change existing root ADDF files, add website pages, or modify deployment.

- [ ] Can you tell framework-repository files from user-project files?
- [ ] Does the nine-file minimal contract match the intended first-run experience?
- [ ] Are existing user projects protected from implicit overwrite?
- [ ] Is one source of truth defined for docs/manual/kit?
- [ ] Are future stage owners clearly separated?
- [ ] Are edition/main branch and deployment boundaries explicit?

Human approval of Stage 2 is required before any starter-kit file is created.