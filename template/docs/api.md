# docs/api.md API Reference

Update after any sprint that adds, changes, or removes an API endpoint or external integration. Add a DECISIONS.md entry for breaking changes.

---

## Endpoint: [METHOD] /[path]

**Purpose:** [What this endpoint does]
**Auth required:** Yes / No

### Request

```
Headers:
  Content-Type: application/json
  Authorization: Bearer [token]  (if required)

Body:
{
  "field": "type — description"
}
```

### Response

```
200 OK
{
  "field": "type — description"
}

4xx / 5xx errors:
{
  "error": "description"
}
```

### Notes
[Edge cases, rate limits, or important behavior]

---

[Repeat block for each endpoint]
