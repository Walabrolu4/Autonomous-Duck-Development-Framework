[Home](index.md)

# Setup and Scaffolding

## Recommended Tooling

Use simple tools at the start. Add terminal and CLI layers only when they actually improve your workflow.

- **Obsidian** — primary interface for managing Markdown files, Architect Packs, STATE.md, prompts, and the project brain. Linked notes and search make it easy to navigate between files.
- **VSCode** — primary interface for the Builder layer; AI coding extensions (Cursor, Cline, Copilot) execute from here.
- **WSL on Windows** — Bash environment for scripts, git commands, and local servers.
- **Git** — every sprint ends with a clean commit on its branch before context reset.
- **Claude CLI** — Architect sessions via terminal.
- **Gemini CLI** — discovery and data ingestion sessions.
- **GPT CLI** — validation and style enforcement sessions.

You do not need all of these on day one. Start with a text editor and any LLM chat interface. Add terminal tools and CLIs when you feel the friction they solve.

---

## Initializing the Directory

Run this from your terminal to create the full project skeleton:

```bash
# Create primary project directory
mkdir -p /path/to/[PROJECT_NAME]
cd /path/to/[PROJECT_NAME]

# Initialize git and create branch structure
git init
git checkout -b main
git checkout -b dev

# Build structural scaffolding
mkdir -p src docs planning/meetings planning/sprints/sprint_001 _templates

# Generate root tracking files
touch AGENTS.md README.md STATE.md DECISIONS.md DOMAIN.md RISKS.md \
      QUESTIONS.md FILE_INVENTORY.md COMMANDS.md STYLE_GUIDE.md \
      SECURITY.md GIT_STRATEGY.md PROMPT_CHANGELOG.md

# Generate documentation files
touch docs/architecture.md docs/data_model.md docs/api.md \
      docs/permissions.md docs/validation.md

# Generate sprint templates
touch planning/backlog.md
touch planning/sprints/sprint_001/requirements.md \
      planning/sprints/sprint_001/blueprint.md \
      planning/sprints/sprint_001/blueprint_feedback.md \
      planning/sprints/sprint_001/acceptance.md \
      planning/sprints/sprint_001/dry_run.md \
      planning/sprints/sprint_001/implementation_log.md \
      planning/sprints/sprint_001/human_review.md \
      planning/sprints/sprint_001/retrospective.md \
      planning/sprints/sprint_001/rollback_log.md

# Create .gitignore
echo -e ".env\n.env.*\n*.key\n*.pem\nsecrets/" > .gitignore
```

**What this creates:** The root tracking files are the project brain. The `docs/` folder holds architecture and API documentation. The `planning/` folder holds the backlog and sprint folders. `src/` is where the Builder writes code. `_templates/` holds starter files for new sprints.

---

## Full Directory Structure

```
Project-Root/
├── AGENTS.md              # AI persona rules and permission levels
├── STATE.md               # Living roadmap: current sprint, status, blockers
├── DOMAIN.md              # Business logic, entities, and workflows
├── DECISIONS.md           # Immutable ADR ledger of design choices
├── FILE_INVENTORY.md      # Source asset manifest and data shapes
├── COMMANDS.md            # Run, build, test, deploy, and rollback commands
├── STYLE_GUIDE.md         # Naming conventions, UI rules, code standards
├── SECURITY.md            # Safe-to-share and never-share file lists
├── GIT_STRATEGY.md        # Branching model and commit rules
├── PROMPT_CHANGELOG.md    # Version history of all framework prompts
├── RISKS.md               # Known risks and mitigation strategies
├── QUESTIONS.md           # Unresolved questions blocking design
├── README.md              # Project overview
├── .gitignore             # Excludes secrets and env files
├── docs/
│   └── architecture.md, data_model.md, api.md, permissions.md, validation.md
├── planning/
│   ├── backlog.md         # Future ideas outside current scope
│   └── sprints/
│       └── sprint_001/
│           ├── requirements.md, blueprint.md, acceptance.md
│           ├── blueprint_feedback.md
│           ├── dry_run.md
│           ├── implementation_log.md
│           ├── human_review.md
│           ├── rollback_log.md
│           └── retrospective.md
├── _templates/            # Starter templates for new sprints
└── src/                   # Execution codebase
```

---

## Populating Files in Order

Fill files in this order. The order matters — each file builds on the previous.

1. **SECURITY.md** — Fill in safe-to-share and never-share lists before anything else. Every file you create after this may be uploaded to an AI session. Know the boundary first.
2. **AGENTS.md** — Paste the permission rules and persona instructions. This file is loaded in every session and is the highest-priority instruction set.
3. **DOMAIN.md** — Write business definitions. Every entity, workflow, and rule not defined here is a gap the AI may fill with an invention.
4. **COMMANDS.md** — Document every command needed to run, test, build, deploy, and roll back before writing code.
5. **GIT_STRATEGY.md** — Fill in the branching model for this project.
6. **STATE.md** — Initialize using the strict short format. Set status to Discovery Phase.
7. **DECISIONS.md** — Create an empty ledger with the ADR header ready.
8. **QUESTIONS.md and RISKS.md** — Create empty ledgers with headers. Add any known risks or questions immediately.

---

## Context Loading Protocol {#context-loading-protocol}

Load only the files the current session needs. Loading everything wastes tokens and introduces noise.

| Session Type | Load These Files | Do Not Load |
|---|---|---|
| **Architect Planning** | AGENTS.md, STATE.md, DOMAIN.md, DECISIONS.md, QUESTIONS.md, RISKS.md | Full source code, old sprint folders |
| **Builder Implementation** | AGENTS.md, STATE.md, sprint requirements + blueprint + acceptance, COMMANDS.md, and only source files the sprint touches | DECISIONS.md, old sprints, unrelated files |
| **Audit Verification** | acceptance.md, dry_run.md, implementation_log.md, test output | Source files, DOMAIN.md |
| **Data Ingestion (Mode 4)** | AGENTS.md, FILE_INVENTORY.md, raw source documents (redacted) | Sprint files, source code |
| **Style Check** | AGENTS.md, DOMAIN.md, STYLE_GUIDE.md, files being validated | Sprint files |

---

## Security and Secrets Protocol {#security-and-secrets-protocol}

> **Highest-priority rule:** API keys, database connection strings, OAuth secrets, private keys, `.env` contents, real user PII, internal IPs/private domains, and payment information must **never** appear in files uploaded to an LLM session.

- **Redaction rule for Mode 4:** Replace sensitive values with `[REDACTED]` or synthetic placeholders before the file leaves your machine.
- **Safe-to-share list:** Framework Markdown files are safe to upload only if written according to the protocol and free of secrets.
- **`.gitignore` must include** `.env`, `.env.*`, `*.key`, `*.pem`, and `secrets/` directories before the first commit.
- **SECURITY.md** is the project-specific record of what is safe and not safe for this project. Update it when new credential types are introduced.

For the full SECURITY.md template and redaction protocol, see [SECURITY.md](file-reference/security.md).

---

## Git Branching Protocol {#git-branching-protocol}

| Branch | Purpose | Who Commits |
|--------|---------|-------------|
| `main` | Production-ready code only | Human operator, after Architect approval |
| `dev` | Integration branch — all sprint branches merge here first | Human operator, after `human_review.md` passes |
| `sprint/NNN-short-description` | One branch per sprint | Builder agent |
| `refactor/short-description` | Mode 3 refactor or migration work | Builder agent |

Four rules that apply on every project:

1. The Builder always works on a named `sprint/NNN` branch — stated explicitly at the start of every Builder session.
2. Mode 1 Quick Patch is the only mode that may work directly on `dev`, given its scope constraint of under 10 lines with no new business logic.
3. Mode 3 Refactor/Migration requires a dedicated `refactor/description` branch with an explicit merge plan in `blueprint.md`.
4. `dev` merges into `main` only after Architect approval.

## See Also

- [SECURITY.md](file-reference/security.md)
- [Getting Started](getting-started.md)
- [File Reference](file-reference/index.md)
