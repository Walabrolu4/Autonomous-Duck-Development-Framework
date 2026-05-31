# Data Model - Mini Task Tracker

## Entities

Task is the only entity in v0.1.

## Fields

| Field | Type | Rules |
|---|---|---|
| `id` | string | UUID generated when the task is created. |
| `title` | string | Required, 1-200 characters. |
| `status` | enum | `open` or `complete`; defaults to `open`. |
| `created_at` | ISO 8601 string | Set when the task is created. |

## Relationships

None. The TaskList is a flat array of Task records.

## Constraints

Task title is required. Whitespace-only titles are rejected. Duplicate titles are allowed. Completed tasks can be reopened.
