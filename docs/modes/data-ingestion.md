[Home](../index.md) → [Operating Modes](index.md) → Mode 4: Data Ingestion / Discovery

# Mode 4: Data Ingestion / Discovery

## Use For

Parsing messy spreadsheets or PDFs, ingesting external APIs, mapping new data sources, or building ETL pipelines. Any task where raw, potentially sensitive data is being processed by an AI session.

---

## Security Gate

The security gate comes first — always. Before any data file is loaded into an AI session:

1. Replace all email addresses with `user_NNN@example.com`
2. Replace all API keys and tokens with `[API_KEY_REDACTED]`
3. Review the file against the `SECURITY.md` never-share list
4. Save the redacted version as `[filename]_redacted.[ext]` — never overwrite the original

Real user PII, database credentials, API keys, and OAuth secrets must never appear in any file uploaded to an LLM session. This rule has no exceptions.

---

## Workflow / Rule

1. Security gate: redact all sensitive data before loading anything
2. Load `AGENTS.md` and `FILE_INVENTORY.md` into the Architect session
3. Load the redacted source documents
4. Architect maps the data shapes, defines rejection criteria, and produces `DOMAIN.md` additions for any new entities
5. Any discovered schema additions require new `DECISIONS.md` entries
6. Builder writes transformation and ingestion code within the approved blueprint

## See Also

- [SECURITY.md](../file-reference/security.md)
- [AGENTS.md](../file-reference/agents.md)
- [Step 1: Research & Global Architecture](../lifecycle/01-research.md)
