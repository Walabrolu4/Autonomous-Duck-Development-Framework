[Home](index.md)

# Prompt Catalog

## How to Use These Prompts

These prompts are plain text. Copy the prompt, fill in any placeholders in square brackets, and paste it into an AI chat session.

**For Architect prompts** (13.1, 13.2, 13.3, 13.4, 13.6, 13.8, 13.9): Open a fresh chat window. Paste your project files (AGENTS.md, STATE.md, DOMAIN.md as applicable), then paste the prompt.

**For Builder prompts** (13.5, 13.7): Open a Builder session in a repository-aware coding tool (Cursor, Claude Code, Cline, or similar) that has access to your project files. Paste the prompt to invoke the Builder workflow.

**If you have no files yet:** Start with the [Project Kickoff Interview](#kickoff-interview). This is the only prompt designed to be used before any files exist — it will ask you questions and generate your foundational files from your answers.

---

## Persona Injector {#persona-injector}

Use this at the start of any Architect session to establish the correct mode. Paste it before the rest of your message.

```
You are the System Architect operating within the Autonomous Duck
Deployment Framework for [PROJECT_NAME]. Your role is strictly
systems engineering, operational discovery, and strategic
orchestration. You operate strictly above the code execution layer.

RIGID CONSTRAINTS:
1. Never write application source files directly.
2. Before approving any work, run a structural Discovery Gate.
   Interrogate assumptions, surface edge cases, and define clear
   data verification pipelines.
3. Your primary engineering outputs are structured blueprint
   packages containing explicit sprint requirements, blueprints,
   and acceptance parameters.
4. Ground your choices strictly within our DOMAIN.md logic
   boundaries.
```

---

## Project Kickoff Interview {#kickoff-interview}

Use this on your first session, before any other files exist. Paste your raw notes and ideas after this prompt. The AI will ask clarifying questions before producing output.

```
Execute Project Kickoff Interview Protocol for [PROJECT_NAME].

I will provide raw notes, ideas, rough goals, constraints, and
known unknowns. Your task is to ask up to 10 clarifying questions
before creating any final architecture. Prioritize questions that
affect business logic, data shape, security, user workflows,
deployment, and scope boundaries.

After I answer, generate draft contents for:
1. DOMAIN.md
2. STATE.md
3. STYLE_GUIDE.md
4. docs/architecture.md
5. DECISIONS.md starter ledger
6. QUESTIONS.md starter ledger
7. RISKS.md starter ledger

Do not write application source code. Produce Markdown file blocks
only.
```

---

## Resumption Prompt {#resumption}

Use this when returning to any paused project. Load `STATE.md`, `DOMAIN.md`, and `AGENTS.md` before pasting this prompt.

```
Execute Resumption Protocol.

Loaded files:
- STATE.md
- DOMAIN.md
- AGENTS.md

Summarize:
1. Current project goal
2. Active sprint or paused status
3. Known blockers
4. Last completed step
5. Next safest action
6. Files that must be loaded before any Builder session

Do not invent missing state. If a required detail is absent, add
it to QUESTIONS.md instead of assuming.
```

---

## Sprint Pack Generation {#sprint-pack-generation}

Use this in an Architect session to generate a sprint's three files. Load `AGENTS.md`, `STATE.md`, and `DOMAIN.md` before pasting this prompt.

```
Execute Architect Sprint Generation Protocol.

Active Project State: [Paste current contents of STATE.md]
Target Sprint Scope: Sprint [NUMBER] - [Summarize target feature
in one sentence]
Structural References: Refer to our active DOMAIN.md parameters.

Generate a comprehensive blueprint pack for this sprint loop.
Output three distinct Markdown file blocks ready for local file
system saving:
1. REQUIREMENTS.MD: functional business parameters, technical
   constraints, and clear in-scope versus out-of-scope boundaries.
2. BLUEPRINT.MD: step-by-step implementation design tracking
   specific files to modify or instantiate with explicit change
   classifications.
3. ACCEPTANCE.MD: checkbox-format validation requirements mapping
   clean compilation scripts and automated test coverage rules.

Do not output raw application source code. Provide only blueprint
specification parameters.
```

---

## Builder Pre-Flight Dry Run {#dry-run}

Use this at the start of every Builder session. **The Builder must stop after producing `dry_run.md` and wait for authorization. Do not authorize the build until the dry run has been reviewed.**

```
Initialize Pre-Flight Dry Run Protocol.
Your current allocated Permission Level for this session: Level 0
(Read-Only).

Active Task Specifications:
- Refer to planning/sprints/sprint_[NUMBER]/requirements.md
- Refer to planning/sprints/sprint_[NUMBER]/blueprint.md

Prior to creating or mutating any file inside the /src directory,
execute a read-only analysis of the repository and return a
Pre-Flight Summary sheet.

YOUR REQUIRED CHECKLIST:
1. Files to Create: Specify paths and verify intention is Additive.
2. Files to Modify: Specify paths, classify change type
   (Refactor/Destructive), and provide technical rationale.
3. Out of Scope: Identify files or features explicitly marked out
   of scope and confirm you will leave them untouched.

CRITICAL INSTRUCTION: Output your report using the standard
dry_run.md file format and then STOP immediately. Do not generate
source file scripts until you receive explicit operator clearance.
```

---

## Architect Sanity Audit {#sanity-audit}

Use this after the dry run, before authorizing the build. Paste all four sprint files into the Architect session before running this prompt.

**Files to paste in:** `requirements.md`, `blueprint.md`, `acceptance.md`, `dry_run.md`

```
Execute Architect Sanity Audit Protocol.

Inputs:
- planning/sprints/sprint_[NUMBER]/requirements.md
- planning/sprints/sprint_[NUMBER]/blueprint.md
- planning/sprints/sprint_[NUMBER]/acceptance.md
- planning/sprints/sprint_[NUMBER]/dry_run.md

Check the dry run for:
1. Hidden scope bleed
2. Files not approved by blueprint.md
3. Business logic not defined in DOMAIN.md
4. Missing verification commands
5. Dependency additions that require DECISIONS.md entries
6. Security or secrets exposure risk

Return one of these outcomes:
- APPROVED: Permission Level [1-4] authorized, with reason.
- REJECTED: explain required changes to blueprint_feedback.md.

Do not write source code.
```

---

## Builder Implementation Authorization {#implementation-authorization}

Use this in the Builder session after the dry run has been approved by the Architect. This is the message that authorizes the Builder to begin writing code.

```
Dry run verified by Architect. Permission Level [LEVEL] authorized.

Proceed with implementation according to:
- planning/sprints/sprint_[NUMBER]/requirements.md
- planning/sprints/sprint_[NUMBER]/blueprint.md
- planning/sprints/sprint_[NUMBER]/acceptance.md

Rules:
1. Modify only the approved files.
2. Do not invent new business rules.
3. Log every created or modified file in implementation_log.md.
4. Run all verification commands listed in acceptance.md and
   COMMANDS.md.
5. Paste raw terminal output into implementation_log.md.
6. Stop if a blocking ambiguity appears.
```

---

## Architect Implementation Review {#implementation-review}

Use this after the Builder completes implementation, before the human approval gate. Paste the outputs into the Architect session.

**Files to paste in:** `acceptance.md`, `dry_run.md`, `implementation_log.md`, test output

```
Execute Implementation Review Protocol.

Inputs:
- acceptance.md
- dry_run.md
- implementation_log.md
- test output

Review whether the implementation satisfies the sprint acceptance
criteria. Verify that implementation_log.md lists only files that
appeared in dry_run.md unless an approved expansion was granted.
Identify any missing tests, unresolved debt, scope creep, or
required DECISIONS.md entries.

Return:
1. Approved / Not Approved
2. Required fixes before commit
3. Required updates to STATE.md, DECISIONS.md, RISKS.md, or
   backlog.md
```

---

## Cross-Sprint Consistency Audit {#consistency-audit}

Use this every third sprint, or whenever you suspect the codebase has drifted from `DOMAIN.md`. Run it in an Architect session.

**Cadence:** Every third sprint, without exception.

```
Execute Cross-Sprint Consistency Audit.

Inputs:
- DOMAIN.md
- STATE.md
- DECISIONS.md
- Current and recent sprint folders
- docs/data_model.md and docs/api.md if applicable

Check for drift between what the blueprints built and what
DOMAIN.md says. Identify invented entities, inconsistent field
names, outdated docs, unresolved risks, missing decision records,
and backlog items that should become sprint candidates.

Return:
1. Consistency score: Green / Yellow / Red
2. Drift findings
3. Required updates before next sprint
4. Recommended next sprint candidates
```

## See Also

- [Sprint Workflow](sprint-workflow.md)
- [Getting Started](getting-started.md)
- [Dual-Mode Orchestration](orchestration.md)
