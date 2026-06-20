# Event-Driven Systems

## Use When
Use when workflows are asynchronous, audit-heavy, integration-heavy, or require decoupled reactions to domain events.

## Avoid When
Avoid when request-response flows are clearer, safer, and easier to operate.

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
