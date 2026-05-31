# Validation - Mini Task Tracker

## Input Validation Rules

- Task title must not be empty.
- Task title must not be only whitespace.
- Task title must not exceed 200 characters.

## Edge Cases

- Whitespace-only title: reject.
- Emoji in title: allow.
- Duplicate title: allow.
- Malformed localStorage data: reset to an empty TaskList and continue.

## Acceptance Tests

- Add a valid task and confirm it appears in the list.
- Attempt to add an empty task and confirm it is rejected.
- Reload the browser and confirm tasks persist.
- Complete a task and confirm its status changes.
- Reopen a completed task and confirm its status changes.
