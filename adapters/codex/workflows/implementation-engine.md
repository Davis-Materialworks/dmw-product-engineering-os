# Implementation Engine Workflow (Codex)

## Phase 1: Pre-flight
1. Read target repo's `AGENTS.md`, then `SKILL.md`, then this workflow.
2. Read `governance/CONSTITUTION.md` and `compatibility/routing-matrix.md`.
3. Confirm architecture is approved and ADRs exist. If not, escalate to Claude Code.

## Phase 2: Scoping
1. Load relevant knowledge: `knowledge/architecture-patterns/`, `knowledge/patterns/`, `knowledge/refactoring/`, `knowledge/failures/`.
2. Break work into small, reviewable diffs (≤5 files per diff when possible).
3. Identify tests that must be added and checks that must pass.

## Phase 3: Implementation
1. Implement one diff at a time.
2. After each diff: run lint, type-check, and relevant tests.
3. Preserve approved component metadata, semantic tokens, and accessibility contracts.
4. Never silently change architecture — escalate if the ADR doesn't cover the situation.

## Phase 4: Validation
1. Run `python3 scripts/validate_skill_repo.py`.
2. Run `python3 scripts/score_benchmarks.py` if scope affects benchmark areas.
3. Verify no regression in existing quality gates.

## Phase 5: Completion
1. Summarize: what changed, which files, which checks passed.
2. Call out assumptions and risks explicitly.
3. Feed failures and new patterns into `knowledge/evolution/`.
4. If the implementation revealed architectural gaps, flag for Claude Code review.