# Feature-Sliced Design

## Use When
Use when frontend work spans multiple product domains and needs predictable boundaries between app, pages, widgets, features, entities, and shared primitives.

## Avoid When
Avoid when the app is tiny or the team lacks conventions to enforce layer boundaries.

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
