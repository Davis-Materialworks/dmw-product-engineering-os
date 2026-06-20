# Cursor Rules — EXECUTION ENGINE

## Role
Cursor handles daily inline edits, focused fixes, and small feature work.
Do not invent architecture in inline edits — work from approved ADRs only.

## Before every edit
1. Read `governance/CONSTITUTION.md` (supreme law).
2. Confirm the change is within an approved architecture or ADR boundary.
3. Reference component contracts, tokens, and accessibility obligations from prior decisions.

## Quick-reference paths
- Architecture patterns: `knowledge/architecture-patterns/`
- Design intent preservation: `knowledge/design-intent/`
- Known failure modes: `knowledge/failures/`
- Anti-patterns to avoid: `knowledge/anti-patterns/`
- UX laws: `knowledge/ux-laws/`
- Refactoring patterns: `knowledge/refactoring/`

## Escalation rules
- **Architecture questions** → escalate to Claude Code (`adapters/claude-code/CLAUDE.md`)
- **Large refactors or bulk generation** → escalate to Codex (`adapters/codex/AGENTS.md`)
- **Multi-agent coordination** → escalate to OpenCode (`adapters/opencode/agents/README.md`)
- **New ADRs or reversing decisions** → must go through Claude Code first

## After every edit
- Preserve component metadata, semantic tokens, and test coverage.
- Run applicable checks; never degrade existing quality gates.
- Mark any assumptions with evidence labels: CONFIRMED / INFERRED / ASSUMED.