# Claude Code Adapter — ARCHITECTURE ENGINE

## Before any task
1. Read `governance/CONSTITUTION.md` — supreme law of this OS.
2. Read `compatibility/routing-matrix.md` — confirm this is architecture work.
3. Load only relevant knowledge modules for the task:
   - Architecture decisions: `knowledge/architecture-patterns/`, `knowledge/adrs/`
   - Risk & failure: `knowledge/failures/`, `knowledge/anti-patterns/`
   - Design intent: `knowledge/design-intent/`, `knowledge/decisions/`
   - Evolution context: `knowledge/evolution/`, `knowledge/success-patterns/`

## Core workflow
1. Run Design Critic → Principal Engineer → Security Architect → Product Strategist → Cost Analyst reviews.
2. Synthesize into tradeoff matrix — name what you're giving up.
3. Produce ADR-ready decisions; write to `knowledge/adrs/` or `knowledge/decisions/`.
4. When architecture is approved, hand off implementation plan to Codex (`adapters/codex/AGENTS.md`).
5. For daily edits, route to Cursor (`adapters/cursor/rules/README.md`).

## Validation
Run before finalizing: `python3 scripts/validate_skill_repo.py`

## Review lenses (apply as independent sections)
- **Design Critic**: challenge UX, hierarchy, accessibility, cognitive load.
- **Principal Engineer**: veto unscalable/unmaintainable architecture.
- **Security Architect**: review OWASP risks, secrets, session management.
- **Product Strategist**: challenge feature purpose, metric impact, bloat.
- **Cost Analyst**: estimate implementation + maintenance + operational cost.

## Agent contracts
Challenge product decisions via `agents/XD_RED_TEAM.md`.
Final verdicts via `agents/XD_JUDGE.md`.

## Rules
- Decisions must become durable records, not conversation memory.
- Do not fork core rules — translate only the workflow for Claude Code.
- Prefer reversibility: choose decisions easy to change over "optimal" ones.
- Every abstraction must justify its complexity.