# Clean Architecture

## Use When
Use when business rules must stay independent of frameworks, UI libraries, databases, or transport layers.

## Avoid When
Avoid when indirection would exceed the product's complexity.

## XD-to-Code Application
- Map XD artboards to use-case interactors that live in the application layer, not in UI components.
- Define domain entities from XD data models (user profiles, orders, dashboards) before binding them to any framework.
- Isolate XD-derived UI components into the outer adapter ring so domain logic never imports a view library.
- Create repository interfaces at domain boundaries that the XD screens imply (e.g., `OrderRepository`) without coupling to a specific database.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
