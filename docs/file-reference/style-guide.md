[Home](../index.md) → [File Reference](index.md) → STYLE_GUIDE.md

# STYLE_GUIDE.md

## Purpose

STYLE_GUIDE.md defines the naming conventions, code standards, and architectural rules that apply to this project. The Builder reads it before generating any code to ensure consistency across sprints. Without it, each sprint may produce code that looks and behaves differently, making the codebase harder to maintain over time.

---

## Template

```markdown
# STYLE_GUIDE.md Project Conventions

## Code Style
Language: [e.g. TypeScript strict mode]
Formatter: [e.g. Prettier]
Linter: [e.g. ESLint]

## Naming Conventions
| Type        | Convention    | Example              |
|-------------|---------------|----------------------|
| Components  | PascalCase    | UserProfileCard      |
| Functions   | camelCase     | getUserById          |
| Constants   | SCREAMING_SNAKE | MAX_RETRY_COUNT    |

## What Requires Architect Approval Before Proceeding
- New database tables or schema changes
- New third-party dependencies
- Auth or permission changes
```

---

## What Requires Architect Approval

Three categories of change always require Architect approval before the Builder begins — regardless of how simple they appear:

- **New database tables or schema changes** — structural decisions with long-term implications
- **New third-party dependencies** — introduce security, licensing, and maintenance risk
- **Auth or permission changes** — high-risk changes that can affect all users

Any of these discovered during the dry run must be flagged in the [Sanity Audit](../prompts.md#sanity-audit) and recorded in [DECISIONS.md](decisions.md) before the build proceeds.

## See Also

- [Mode 5: Style Audit](../modes/style-audit.md)
