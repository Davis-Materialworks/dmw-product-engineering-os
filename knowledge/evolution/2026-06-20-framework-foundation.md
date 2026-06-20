# 2026-06-20 Framework Foundation

## Decisions Made

### Evidence Label System
Every XD extraction must label each finding with CONFIRMED, INFERRED, ASSUMED, or UNKNOWN. The label determines downstream treatment: CONFIRMED values are binding, INFERRED values are strong defaults that can be challenged, ASSUMED values trigger a review prompt, and UNKNOWN values block implementation until resolved. This was adapted from intelligence analysis frameworks where source confidence drives action.

### World-Class Gate Thresholds
Set minimum scores: Accessibility ≥ 95, Maintainability/Architecture/Security/Design Quality/Testability/Documentation ≥ 90, Performance ≥ 85. These thresholds are intentionally aggressive — a "90" in the gate scoring system does not mean "B+," it means "no known issues." Anything below 90 has a documented gap. This prevents the common pattern where teams set thresholds at 80 and then rationalize every score up to 80.

### Principal Engineer Veto
The principal engineer review lens can block any output that does not meet architecture, scalability, testability, or maintainability standards. This is not a recommendation — it is a gate with veto power. The rationale: in a traditional team, the principal engineer would stop bad architecture before it ships. An automated system needs the same authority encoded as a rule.

### Component Metadata Requirements
Every component extracted from XD must carry: name, purpose, industry usage context, accessibility requirements, performance requirements, testing requirements, and state inventory (default, hover, active, focus, disabled, loading, empty, error). Without this, the component is a visual artifact, not a production component. This was learned from observing countless "pixel-perfect" components that broke in every non-default state.

## What We Learned From the Refactoring
1. **Scaffolding is not documentation**: The initial 11-line migration playbooks were placeholders. A migration playbook that does not include common pitfalls, token translation rules, and verification checklists is not useful — it is overhead. Either write a real playbook or link to external references.
2. **UX laws need context to be actionable**: "Cite when users are overwhelmed" is not actionable. A UX law entry must answer: how do I detect this in an XD artboard? What does a real violation look like? When should I invoke this in a critique? Without these, the law is trivia, not a tool.
3. **Design intent needs preservation rules**: Extracting business goals and user goals from XD artboards is valuable, but storing them without rules for how to preserve them when the design changes is incomplete. Every intent record needs preservation rules that define what must not change.
4. **Evolution entries must describe actual decisions**: The initial entries listed "lessons learned" as vague statements. Real evolution entries should describe: what decision was made, why, what tradeoffs were considered, and what was observed afterward. Without this, the evolution log is a changelog, not institutional memory.

## Missing Rules Discovered
- Require evidence labels on every extracted design value
- World-class gate enforcement before any output is considered final
- Component metadata: states, accessibility, performance, testing requirements
- Critic review: no output ships without design critique
- Principal engineer veto: architecture decisions can be blocked
- Migration playbooks must include pitfalls, token maps, and verification checklists

## New Patterns Discovered
The initial pattern library was seeded with 10 categories (authentication, onboarding, checkout, settings, search, dashboard, reporting, billing, notifications, admin). Each will need patterns for: component structure, state management approach, accessibility requirements, common mistakes, and testing strategy.

## Benchmark Changes Required
Replace placeholder design inputs with real XD projects, recreated interfaces, industry-specific challenge sets, and design-system-focused projects. Add candidate-output fixtures once real XD-to-code runs produce verifiable results.

## Failure Library Updates
Seed failures for: frontmatter discovery failures, unlabeled inference in design extraction, weak component metadata (missing states), missing design critique pass, missing principal engineer veto, weak score gate enforcement (scores claimed without evidence), and no self-improvement loop feedback.

## Prevention Rules Added
1. Consult knowledge libraries before final output — every module in `knowledge/` is mandatory reading for relevant tasks
2. Run score gates before shipping — output must pass the World-Class Gate or be explicitly flagged as below threshold
3. Record evolution entries after every significant project — lessons decay if not captured immediately