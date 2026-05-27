# SECURITY.md

## Files That Must Never Be Loaded Into AI Tools

- Any file containing API keys or credentials
- Any `.env` file
- Any file with personal contact information
- Any file with private infrastructure paths

## Repository Rules

- Do not commit secrets, tokens, or API keys.
- Do not commit `.env` files.
- When in doubt, do not load the file. Record the question in QUESTIONS.md.