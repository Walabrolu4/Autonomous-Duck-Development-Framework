# docs/validation.md Validation Rules

Documents input validation rules for all user-facing and API inputs. Update when new fields or forms are introduced.

---

## Entity: [EntityName]

| Field        | Rule                                  | Error message                        |
|--------------|---------------------------------------|--------------------------------------|
| [field]      | Required, non-empty string            | "[Field] cannot be empty."           |
| [field]      | Integer between 1 and 100             | "[Field] must be between 1 and 100." |

## Global Rules
- [e.g. All date fields must be ISO 8601 format]
- [e.g. All text fields are trimmed of leading/trailing whitespace before validation]
