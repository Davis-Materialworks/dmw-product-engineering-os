# Missing Skill Description Frontmatter

## Root Cause
The skill used nonstandard metadata, so agent discovery can fail or become unreliable.

## Detection Pattern
SKILL.md frontmatter lacks a `description:` key that starts with `Use when`.

## Correction Strategy
Replace summary-only metadata with required `name` and `description` fields.

## Prevention Rule
Every skill edit must run validation that checks required frontmatter keys.
