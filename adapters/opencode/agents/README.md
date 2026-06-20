# OpenCode Agents — ORCHESTRATION ENGINE

## Role
OpenCode coordinates multi-agent workflows, sequences tasks across engines,
and automates benchmark/validation/evolution pipelines.

## Orchestration workflow
1. Read `compatibility/routing-matrix.md` to select the right engine.
2. Route architecture questions to Claude Code → `adapters/claude-code/CLAUDE.md`
3. Route implementation to Codex → `adapters/codex/AGENTS.md`
4. Route daily edits to Cursor → `adapters/cursor/rules/README.md`
5. After each phase, collect outputs and feed into the next engine.

## Sequencing multi-agent tasks
1. **Architecture phase**: Claude Code produces ADRs and tradeoff matrices.
2. **Red Team review**: Run `agents/XD_RED_TEAM.md` against architecture decisions.
3. **Implementation phase**: Codex translates approved architecture into code.
4. **Judge verdict**: Run `agents/XD_JUDGE.md` for evidence-based final pass/fail.

## Automation scripts
- Validate repo integrity: `python3 scripts/validate_skill_repo.py`
- Run benchmarks: `python3 scripts/score_benchmarks.py`
- Generate intelligence: `python3 scripts/benchmark_intelligence.py`
- Results stored in `results/`, reports in `reports/`.

## Evolution feedback loop
After every substantial project:
1. Extract lessons, failures, and new patterns.
2. Write entries into `knowledge/evolution/`.
3. Promote repeated failures to `knowledge/failures/`.
4. Update benchmark expectations if quality floor has shifted.