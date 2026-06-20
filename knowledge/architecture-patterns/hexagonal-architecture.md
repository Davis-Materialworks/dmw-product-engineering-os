# Hexagonal Architecture

## Use When
Use when integrations, APIs, services, and adapters need to change independently around a stable domain core.

## Avoid When
Avoid when there are no meaningful external ports or adapters.

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
