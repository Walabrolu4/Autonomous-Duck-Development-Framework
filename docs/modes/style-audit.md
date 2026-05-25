[Home](../index.md) → [Operating Modes](index.md) → Mode 5: Style Audit

# Mode 5: Style Audit

## Use For

Enforcing `STYLE_GUIDE.md` conventions across new or modified files. Catching naming inconsistencies, formatting deviations, and code standard violations before they accumulate.

---

## Workflow / Rule

1. Load `AGENTS.md`, `DOMAIN.md`, and `STYLE_GUIDE.md` into the Builder session
2. Specify which files to audit (typically the files modified or created in the most recent sprint)
3. Builder checks each file against the rules in `STYLE_GUIDE.md`
4. Builder reports violations and either fixes them (with approval) or lists them for human resolution
5. Update `implementation_log.md` with the audit results

A Style Audit does not require a full sprint pack — it is a targeted check against a defined standard. The Builder operates at Level 1 or Level 2 for audit sessions.

---

## When It's Mandatory

A Style Audit is recommended after any sprint that creates more than three new files. It is **mandatory before any production deployment**.

Style drift is subtle — each sprint may introduce one or two inconsistencies that seem minor in isolation. Over many sprints, they compound into a codebase with inconsistent naming, mixed formatting, and undocumented patterns that make future Architect blueprints less accurate.

## See Also

- [STYLE_GUIDE.md](../file-reference/style-guide.md)
- [Step 7: Deployment & Maintenance](../lifecycle/07-deployment.md)
