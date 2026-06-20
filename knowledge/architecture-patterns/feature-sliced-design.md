# Feature-Sliced Design

## Use When
Use when frontend work spans multiple product domains and needs predictable boundaries between app, pages, widgets, features, entities, and shared primitives.

## Avoid When
Avoid when the app is tiny or the team lacks conventions to enforce layer boundaries.

## XD-to-Code Application
- Map each XD artboard or screen variant to a feature folder under `features/`, with shared primitives in `shared/`.
- Identify entities from XD data models that span multiple screens and place them in `entities/` layer.
- Detect widget candidates from XD component instances reused across artboards; place them in `widgets/`.
- Pages layer maps to top-level XD flows; each page orchestrates features and widgets without owning business logic.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
