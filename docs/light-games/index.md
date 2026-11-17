# ADDF Light Games — Documentation Wiki

**Edition:** ADDF Light Games · **Branch:** `ADDF_light_games` · **Status:** Stage 7 candidate, awaiting human review  
**Document authority:** [Framework specifications](../../spec/FRAMEWORK_SPEC.md), [Project File Contracts](../../spec/PROJECT_FILE_CONTRACTS.md), [Sprint Contracts](../../spec/SPRINT_FILE_CONTRACTS.md)

This is the **canonical Markdown wiki** for the game-development-focused Light edition of the Autonomous Duck Deployment Framework. It contains thorough reference material while the actual user experience begins with six project files and one consequential question at a time.

**Start quickly:** [Root Quick Start](../../QUICK_START.md) · [Your First Session](guides/first-session.md) · [Install Starter Kit](guides/install.md)

**Compare editions:** [Original ADDF vs. ADDF Light Games](foundations/comparison.md) — full side-by-side table of philosophy, lifecycles, files, permission gates, onboarding, and recommended use cases.

**One complete document:** [Generated MANUAL.md](../../MANUAL.md) — all chapters below, built from these wiki pages; do not edit it manually.

## Wiki navigation

### Foundations

- [Overview](foundations/overview.md)
- [Philosophy](foundations/philosophy.md)
- [Original ADDF vs. ADDF Light Games](foundations/comparison.md)
- [Core Concepts](foundations/core-concepts.md)
- [Glossary](foundations/glossary.md)

### Getting started

- [Install](guides/install.md)
- [First Session](guides/first-session.md)
- [From Zero](guides/from-zero.md)
- [From Idea](guides/from-idea.md)
- [Existing Project](guides/existing-project.md)
- [Quick Reference](guides/quick-reference.md)

### Five-stage lifecycle

- [Index](lifecycle/index.md)
- [Research](lifecycle/research.md)
- [Design](lifecycle/design.md)
- [Implement](lifecycle/implement.md)
- [Refine](lifecycle/refine.md)
- [Acceptance](lifecycle/acceptance.md)

### Sprint workflow

- [Overview](sprints/overview.md)
- [Backlog](sprints/backlog.md)
- [Planning](sprints/planning.md)
- [Approvals](sprints/approvals.md)
- [Review](sprints/review.md)

### Guided learning

- [Guided Discovery](learning/guided-discovery.md)
- [Checkpoints](learning/checkpoints.md)
- [Decisions](learning/decisions.md)

### Agents and integrations

- [Operating Contract](agents/operating-contract.md)
- [Permissions](agents/permissions.md)
- [Handoff](agents/handoff.md)
- [Claude Code](agents/claude-code.md)
- [Codex](agents/codex.md)
- [Openclaw](agents/openclaw.md)

### Quality and safety

- [Testing](quality/testing.md)
- [Playtesting](quality/playtesting.md)
- [Validation](quality/validation.md)
- [Failure Recovery](quality/failure-recovery.md)
- [Security](quality/security.md)

### Reference

- [File Reference](reference/file-reference.md)
- [Prompt Catalog](reference/prompt-catalog.md)
- [Troubleshooting](reference/troubleshooting.md)
- [Faq](reference/faq.md)

## How to use this wiki

Begin with the [Quick Start](../../QUICK_START.md) or the [first-session guide](guides/first-session.md). You do **not** need to read every chapter before starting a game. During actual work, use the [Quick Reference](guides/quick-reference.md) and read only the relevant stage's page.

If you are a framework maintainer or educator, the full wiki covers the human design/learning process, approval safeguards, file contracts, optional agent integrations, testing, security, and recovery. The generated manual combines the pages without creating a competing source of truth.

## What is normative versus explanatory?

- **Normative framework rules:** Approved `spec/` files. This wiki explains and illustrates them; it does not silently change their permissions.
- **Project state:** A user's own `SECURITY.md`, `AGENTS.md`, `GAME.md`, `STATE.md`, `DECISIONS.md` and sprint records.
- **Canonical documentation prose:** `docs/light-games/**/*.md`, ordered by `manifest.txt`.
- **Derived artifact:** Root `MANUAL.md` produced by `scripts/build_light_manual.py`; CI detects drift.
- **Not yet finished:** Stage 8 branding/logo, Stage 9 website distribution, Stage 10 release packaging. The Stage 5 live Claude Code/Codex/OpenClaw runs remain openly unverified.

## Boundaries

Original full ADDF documentation under `docs/` and `main` has not been replaced. The Light wiki is isolated under `docs/light-games/` to prevent conflicts, and its release must never auto-merge into or deploy over the original ADDF site.

This wiki is distributed as Markdown under the repository's existing license; see the repository's [LICENSE](../../LICENSE) for exact terms. Links to vendor documentation are informational and may change with host versions.
