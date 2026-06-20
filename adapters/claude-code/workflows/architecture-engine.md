# Architecture Engine Workflow (Claude Code)

## Phase 1: Context loading
1. Read `governance/CONSTITUTION.md`.
2. Load only relevant knowledge: `knowledge/architecture-patterns/`, `knowledge/failures/`, `knowledge/decisions/`, `knowledge/design-intent/`.
3. Scan `knowledge/adrs/` for related prior decisions — do not reverse without cause.

## Phase 2: Multi-lens review
Run each as an independent review section:
1. **Design Critic**: UX hierarchy, accessibility, cognitive load, error recovery.
2. **Principal Engineer**: Scalability, maintainability, testability, repo fit.
3. **Security Architect**: OWASP top 10, auth, secrets, API exposure, data classification.
4. **Product Strategist**: Feature purpose, metric impact, simpler alternatives, bloat risk.
5. **Cost Analyst**: Implementation cost, maintenance burden, tech-debt estimate, complexity score.

## Phase 3: Tradeoff synthesis
1. Produce a tradeoff matrix: what you gain vs. what you give up.
2. Every decision must name its rejected alternatives and why.
3. Prefer reversible decisions over "optimal" irreversible ones.

## Phase 4: Decision recording
1. Write ADR to `knowledge/adrs/` using the ADR template.
2. Update `knowledge/decisions/` if prior product decisions are affected.
3. Record assumptions in evidence labels: CONFIRMED / INFERRED / ASSUMED / UNKNOWN.

## Phase 5: Handoff
1. Package approved architecture + ADRs as an implementation plan.
2. Hand off to Codex (`adapters/codex/AGENTS.md`) or Cursor (`adapters/cursor/rules/README.md`).
3. Run `python3 scripts/validate_skill_repo.py` before declaring done.
4. Feed lessons into `knowledge/evolution/`.