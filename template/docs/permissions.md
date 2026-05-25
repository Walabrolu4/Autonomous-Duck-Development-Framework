# docs/permissions.md Permission Model

Documents who can do what within the application. Update when auth or role logic changes — add a DECISIONS.md entry first.

---

## Roles

| Role       | Description                          |
|------------|--------------------------------------|
| [Role 1]   | [What this role can do]              |
| [Role 2]   | [What this role can do]              |

## Permission Matrix

| Action                  | [Role 1] | [Role 2] | Unauthenticated |
|-------------------------|----------|----------|-----------------|
| [e.g. View dashboard]   | Yes      | Yes      | No              |
| [e.g. Edit settings]    | Yes      | No       | No              |

## Notes
[Any special cases, inheritance rules, or conditions]
