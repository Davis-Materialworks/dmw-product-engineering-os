# Domain-Driven Design

## Use When
Use when domain language, business rules, workflows, and bounded contexts drive the product more than visual screens.

## Avoid When
Avoid superficial entity naming without real domain modeling.

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
