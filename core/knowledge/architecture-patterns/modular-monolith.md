# Modular Monolith

## Use When
Use for enterprise systems needing strong module boundaries without distributed-system cost.

## Avoid When
Avoid when independent deployability is already required and operational maturity exists.

## XD-to-Code Application
- Map XD screens to product domains before creating folders.
- Keep generic UI primitives separate from domain components.
- Preserve design intent and data ownership boundaries.
- Define testing seams at module, use-case, or adapter boundaries.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
