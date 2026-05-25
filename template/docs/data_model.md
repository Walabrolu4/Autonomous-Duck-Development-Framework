# docs/data_model.md Data Model

Update after any sprint that adds or changes database tables, collections, or storage schemas. Add a DECISIONS.md entry for any structural change.

---

## Entity: [EntityName]

**Storage:** [e.g. PostgreSQL table `users`, localStorage key `tasks`]

| Field        | Type     | Required | Description                        |
|--------------|----------|----------|------------------------------------|
| id           | string   | Yes      | Unique identifier                  |
| [field]      | [type]   | Yes/No   | [Description]                      |

**Indexes:** [List any indexes and why they exist]
**Relationships:** [Foreign keys or references to other entities]

---

## Entity: [EntityName]

[Repeat block for each entity]
