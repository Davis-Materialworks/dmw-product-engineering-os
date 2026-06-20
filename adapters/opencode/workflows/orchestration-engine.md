# Orchestration Engine Workflow (OpenCode)

OpenCode coordinates the full DMW OS pipeline across agents. This workflow sequences architecture → review → implementation → validation.

## Phase 1: Dispatch architecture
1. Read `compatibility/routing-matrix.md` to confirm routing.
2. Dispatch Claude Code via `adapters/claude-code/workflows/architecture-engine.md`.
3. Wait for ADRs, tradeoff matrices, and approved implementation plan.

## Phase 2: Red Team challenge
1. Run `agents/XD_RED_TEAM.md` against all architecture decisions.
2. Collect gaps, risks, and edge cases the architecture didn't address.
3. If Red Team finds blockers, return to Phase 1 with findings.

## Phase 3: Implementation
1. Dispatch Codex via `adapters/codex/workflows/implementation-engine.md`.
2. Feed approved ADRs and Red Team findings as implementation constraints.
3. Monitor for architectural escalations — route back to Claude Code if needed.

## Phase 4: Validation & scoring
1. Run `python3 scripts/validate_skill_repo.py`.
2. Run `python3 scripts/score_benchmarks.py` for benchmark tasks.
3. Run `python3 scripts/benchmark_intelligence.py` for trend analysis.

## Phase 5: Judge verdict
1. Run `agents/XD_JUDGE.md` for evidence-based final pass/fail.
2. Track scores against world-class gate thresholds (Design ≥90, A11y ≥95, etc.).

## Phase 6: Evolution
1. Extract lessons, failures, and new patterns.
2. Write to `knowledge/evolution/`.
3. Promote repeated failures to `knowledge/failures/`.
4. Store benchmark results in `results/YYYY-MM-DD/`, generate `reports/`.