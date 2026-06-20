# Modular Monolith

## Use When
Use for enterprise systems needing strong module boundaries without distributed-system cost.

## Avoid When
Avoid when independent deployability is already required and operational maturity exists.

## XD-to-Code Application
- Group XD screens by functional cohesion into modules; screens that change together for the same business reason stay together.
- Define module boundaries from XD screen groupings: a module owns its screens, data, and domain logic, exposing only a public API.
- Use XD navigation patterns to validate module coupling: if navigating from Screen A to Screen B requires tight coupling, they may belong in the same module.
- Enforce compile-time module isolation: no module imports another module's internal XD-derived components directly.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
