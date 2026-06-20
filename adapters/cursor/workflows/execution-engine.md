# Execution Engine Workflow (Cursor)

Cursor handles daily inline edits and focused fixes. This workflow keeps scope tight.

## Step 1: Validate context
1. Read `governance/CONSTITUTION.md`.
2. Confirm the edit is within an approved architecture or ADR.
3. Load only needed knowledge modules: `knowledge/failures/`, `knowledge/anti-patterns/`, `knowledge/design-intent/`.

## Step 2: Make the edit
1. Make the smallest change that solves the problem.
2. Preserve: component names, semantic tokens, accessibility roles, test coverage.
3. If the fix requires new patterns, check `knowledge/patterns/` first.
4. Do not invent architecture — escalate if the edit crosses ADR boundaries.

## Step 3: Validate
1. Run available lint, type-check, and tests.
2. Confirm no degradation of existing quality scores.

## Step 4: Escalate if needed
- **Architecture question?** → Claude Code (`adapters/claude-code/workflows/architecture-engine.md`)
- **Large refactor?** → Codex (`adapters/codex/workflows/implementation-engine.md`)
- **Multi-agent?** → OpenCode (`adapters/opencode/workflows/orchestration-engine.md`)
- **New ADR needed?** → Must route through Claude Code first.

## Step 5: Record
1. Document what changed and why in the commit message.
2. If the edit revealed a failure pattern, propose entry for `knowledge/failures/`.
3. Mark any assumptions with evidence labels.