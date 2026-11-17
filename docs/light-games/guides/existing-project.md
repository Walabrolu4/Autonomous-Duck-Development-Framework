# Adopt Light in an Existing Game Project

An existing repo has history, human-owned design choices, source files, build constraints and possibly an `AGENTS.md` that defines permissions. Light should **integrate** with that reality, not overwrite it.

## When to use

Use this for an ongoing Phaser, Unity, Godot, Unreal, web or custom-engine project; for a repo previously using original ADDF; or for a classroom project with established files.

## Phase 1 — Read-only audit

Before opening arbitrary files, identify likely secret paths and excluded data. Read relevant safe files and list:
- engine/language and **verified** project structure;
- existing design intent and gameplay systems;
- run/build/test commands, distinguishing actual execution from documentation;
- `AGENTS.md`, `CLAUDE.md` or other project instructions that might conflict;
- current branch/worktree, uncommitted work and important backups;
- active issues, risks and unknowns.

Do not run installers, apply a starter kit, change Git settings, rename files or edit game source during the audit.

## Phase 2 — Map without erasing

| Existing document | Possible Light destination | Treatment |
| --- | --- | --- |
| GDD, design brief, README | `GAME.md` | Summarize confirmed intent; preserve original |
| Existing agent instruction file | `AGENTS.md` | Review conflict; **never blindly overwrite** |
| Roadmap or issue list | `planning/BACKLOG.md` | Map candidates with history |
| Decisions and playtest notes | `DECISIONS.md` / `REVIEW.md` | Preserve actual sources and past verdicts |
| Existing security policy | `SECURITY.md` | Retain stricter exclusions |
| Prior full-ADDF sprint files | Light sprint triplet (optional migration) | Keep originals; map conceptual responsibilities |
| Source/config/assets | Remain as-is | No adoption-time changes by default |

The Stage 5 [existing-project fixture](../../../examples/existing-project/README.md) illustrates an `AGENTS.md` conflict, a read-only audit and a proposal to **merge** instructions instead of replacing them.

## Phase 3 — Proposed migration plan

Before a single adoption write, identify exact paths to create/modify/move/delete, what content would be copied or reinterpreted, impacts on existing rules, potential data loss, rollback and the branch/worktree where changes would occur.

The human explicitly reviews that migration scope. General interest in Light does not authorize replacement of existing project instructions or code. Migrating project-brain documents is distinct from the Gate I needed for subsequent game implementation.

## Phase 4 — Safe initial state

Once approved, create the minimal files where genuinely missing and record `project_origin: existing-project`. Start Light `STATE.md` in `research` / `discovering`, `authorized: no`, unless there is verifiable *current* Light sprint authorization. Existing code does not imply ongoing Gate I.

Choose a modest first task: a reproducible bug, a new playtest, a single mechanic or a research spike. Draft the sprint pack only after the human selects it.

## Verify the adoption

Compare the actual diff against the migration plan. Confirm old GDD, source, Git history and permissions remain accessible. If a file was overwritten accidentally, stop, preserve the diff and seek human instructions on restoring it. Do not force-reset uncommitted work.

## Common failures

**Blind copy:** Overwriting a rich `AGENTS.md` with the Light template. Use a reviewed merge.

**Fabricated test:** Assuming an existing project builds because a README contains a command. Mark not verified until run under proper permission.

**Silent mode migration:** Converting original ADDF approval levels into new Gate I without checking whether consent still applies. Keep old records, re-approve current scope.

## Related

[Install guide](install.md) · [Source-control safety](../quality/security.md) · [Original comparison](../foundations/comparison.md)
