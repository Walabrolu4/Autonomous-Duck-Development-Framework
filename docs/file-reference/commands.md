[Home](../index.md) → [File Reference](index.md) → COMMANDS.md

# COMMANDS.md

## Purpose

COMMANDS.md is the single source of truth for every command the Builder needs to run, test, build, deploy, and roll back the project. The Builder reads COMMANDS.md during the implementation phase and pastes the raw terminal output into `implementation_log.md`. If a command is not in COMMANDS.md, the Builder cannot run it — and cannot verify the work.

---

## Template

```markdown
# COMMANDS.md Project Commands

## Environments
| Environment | Base URL          | Database    | Notes            |
|-------------|-------------------|-------------|------------------|
| dev         | localhost:[port]  | [local DB]  | Safe to reset    |
| staging     | [staging URL]     | [staging DB]| QA only          |
| production  | [prod URL]        | [prod DB]   | Requires approval|

## Development [dev only]
[command to start dev server]

## Testing [dev and staging]
[command to run all tests]

## Build
[command to build for production]

## Lint / Type Check
[lint command]

## Rollback
[rollback command — must be documented before deployment]
```

---

## When to Fill It In

Fill in COMMANDS.md before writing any code. The Builder uses these commands during verification — they are what makes "the tests pass" a concrete statement rather than an impression. If COMMANDS.md is empty when the Builder runs verification, the sprint cannot be confirmed as complete.

---

> **Rollback Rule:** The rollback command must be documented in COMMANDS.md *before* deployment, not after something breaks. If you need to revert in seconds, you cannot afford to spend time figuring out the rollback command under pressure.

## See Also

- [Mode 3: Refactor / Migration](../modes/refactor-migration.md)
- [Step 7: Deployment](../lifecycle/07-deployment.md)
