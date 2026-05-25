[Home](../index.md) → [File Reference](index.md) → SECURITY.md

# SECURITY.md

## Purpose

SECURITY.md is the highest-priority file in the project. It is filled in before any other file. Every file created after SECURITY.md may be uploaded to an AI session — so the boundary must be set first. SECURITY.md defines, for this specific project, which files are safe to share with an AI and which must never leave the machine.

---

## The Absolute Rule

> **The following must NEVER appear in any file uploaded to an LLM session:**
> - API keys or tokens of any kind
> - Database connection strings or passwords
> - Contents of `.env` or `.env.*` files
> - Real user PII: names, emails, phone numbers, addresses, ID numbers
> - OAuth secrets or private keys
> - Internal IP addresses or private domain names
> - Payment information of any kind

There are no exceptions. Violating this rule exposes sensitive information to external AI services — with no way to retrieve it.

---

## Template

```markdown
# SECURITY.md Data Security Protocol

## The Absolute Rule
The following must NEVER appear in any file uploaded to an LLM session:
- API keys or tokens of any kind
- Database connection strings or passwords
- Contents of .env or .env.* files
- Real user PII: names, emails, phone numbers, addresses, ID numbers

## Redaction Protocol for Mode 4 Discovery
Before uploading any operational data file:
1. Replace all email addresses with user_NNN@example.com
2. Replace all API keys with [API_KEY_REDACTED]
3. Save the redacted version as [filename]_redacted.[ext]

## Safe to Upload for This Project
[List the specific file types and folders safe to share for this project]

## Never Upload for This Project
[List specific file types and folders that must never be shared for this project]
```

---

## Redaction Protocol

When working in [Mode 4: Data Ingestion](../modes/data-ingestion.md), you may need to load raw data files (spreadsheets, CSVs, API responses) into an AI session. Before any such file leaves your machine:

1. Replace all email addresses with `user_NNN@example.com`
2. Replace all API keys and tokens with `[API_KEY_REDACTED]`
3. Save the result as `[filename]_redacted.[ext]` — never overwrite the original

The `.gitignore` file must include `.env`, `.env.*`, `*.key`, `*.pem`, and `secrets/` directories before the first commit.

## See Also

- [Mode 4: Data Ingestion](../modes/data-ingestion.md)
- [Getting Started — Step 2](../getting-started.md#step-2--fill-in-securitymd-first)
- [Setup — Security Protocol](../setup.md#security-and-secrets-protocol)
