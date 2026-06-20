# Microservices

## Use When
Use only when bounded contexts need independent deployment, scaling, ownership, and data lifecycle.

## Avoid When
Avoid for early products, small teams, or systems without observability and platform maturity.

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
