# Governance

Governance in DMW Product Engineering OS exists to keep recommendations evidence-based, accessible, secure, maintainable, and aligned with user and business outcomes.

## Governing Documents

- [governance/CONSTITUTION.md](governance/CONSTITUTION.md): supreme rules for the system.
- [DISCLAIMER.md](DISCLAIMER.md): public independence and third-party relationship notice.
- [TRADEMARK.md](TRADEMARK.md): trademark and naming policy.
- [SECURITY.md](SECURITY.md): vulnerability and security guidance.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md): community expectations.
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution workflow.

## Decision Framework

Major decisions should be recorded using:

- ADRs in `knowledge/adrs/` or `core/memory/adrs/`
- Decision memory in `knowledge/decisions/` or `core/memory/decisions/`
- Design intent memory in `knowledge/design-intent/` or `core/memory/design-intent/`
- Risk register entries when a decision has operational, security, compliance, accessibility, or maintainability risk

## Review Lifecycle

Nontrivial work should pass through:

1. Constitution check
2. Evidence labeling
3. Pattern and anti-pattern lookup
4. Accessibility review
5. Architecture review
6. Security review
7. Product strategy review
8. Cost and complexity review
9. Red Team challenge
10. Judge verdict
11. Evolution note when the work reveals a reusable lesson

## Approval Workflow

Recommendations should use one of four override levels:

- Recommend: useful improvement, not blocking.
- Strongly Recommend: high-value improvement, should be addressed unless there is a clear tradeoff.
- Require: must be addressed before production use.
- Block: unacceptable risk; reject or revise before continuing.

## Public Repository Governance

Because this repository is public:

- Avoid implying Adobe or third-party endorsement.
- Avoid committing proprietary design assets, customer data, secrets, or private project details.
- Keep examples generic unless there is explicit permission to publish them.
- Prefer evidence-based guidance over broad claims.
- Keep the platform design-source agnostic even when Adobe XD is the first supported source.
