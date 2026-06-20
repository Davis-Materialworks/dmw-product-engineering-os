# Codex Adapter — IMPLEMENTATION ENGINE

## Before any task
1. Read target repo's `AGENTS.md` first, then this file, then `SKILL.md`.
2. Read `governance/CONSTITUTION.md` and `compatibility/routing-matrix.md`.
3. Confirm architecture is approved. If not, request Claude Code review first.
4. Confirm XD_SECURITY_ARCHITECT has approved the architecture plan before writing implementation code.

## Knowledge modules to load
- Implementation patterns: `knowledge/architecture-patterns/`, `knowledge/patterns/`
- Refactoring: `knowledge/refactoring/`
- Migration: `knowledge/migration-intelligence/`
- Avoiding known failures: `knowledge/failures/`, `knowledge/anti-patterns/`
- Design intent preservation: `knowledge/design-intent/`

## Implementation rules
1. Prefer small, reviewable diffs — never one massive commit.
2. Follow target repo conventions over OS defaults.
3. Run the most relevant checks after every edit.
4. After implementation: `python3 scripts/validate_skill_repo.py`
5. Run benchmarks when applicable: `python3 scripts/score_benchmarks.py`

## Receiving architecture from Claude Code
- Claude Code produces ADRs and implementation plans.
- Translate architecture decisions into concrete code changes.
- Preserve approved component metadata, tokens, and accessibility contracts.
- If the architecture plan is ambiguous, request clarification — do not guess.

## Before completion
- Run all available repo checks (lint, test, type-check).
- Explain what changed, why, and what remains uncertain.
- Feed lessons learned into `knowledge/evolution/`.