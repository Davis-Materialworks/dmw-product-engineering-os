# Hexagonal Architecture

## Use When
Use when integrations, APIs, services, and adapters need to change independently around a stable domain core.

## Avoid When
Avoid when there are no meaningful external ports or adapters.

## XD-to-Code Application
- Define input ports from XD user actions: each button, form, or gesture maps to a use-case interface in the application core.
- Define output ports from XD data displays: each list, chart, or detail view implies a data-fetching port the UI adapter calls.
- XD screens that trigger external integrations (payment, file upload, search) reveal adapter boundaries around third-party services.
- Test the domain core in isolation by swapping XD-derived UI adapters with test doubles at port boundaries.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
