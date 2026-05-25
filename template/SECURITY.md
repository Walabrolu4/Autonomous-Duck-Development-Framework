# SECURITY.md Data Security Protocol

## The Absolute Rule

The following must NEVER appear in any file uploaded to an LLM session:

- API keys or tokens of any kind
- Database connection strings or passwords
- Contents of .env or .env.* files
- Real user PII: names, emails, phone numbers, addresses, ID numbers

## Redaction Protocol for Mode 4 Discovery

Before uploading any operational data file:

1. Replace all email addresses with `user_NNN@example.com`
2. Replace all API keys with `[API_KEY_REDACTED]`
3. Save the redacted version as `[filename]_redacted.[ext]`

## Safe to Upload for This Project

[List the specific file types and folders safe to share for this project]

- All framework Markdown files (AGENTS.md, STATE.md, DOMAIN.md, etc.)
- Source code files that contain no secrets
- Sprint planning files

## Never Upload for This Project

[List specific file types and folders that must never be shared for this project]

- .env and .env.* files
- secrets/ directory
- *.key and *.pem files
