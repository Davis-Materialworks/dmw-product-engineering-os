# Domain-Driven Design

## Use When
Use when domain language, business rules, workflows, and bounded contexts drive the product more than visual screens.

## Avoid When
Avoid superficial entity naming without real domain modeling.

## XD-to-Code Application
- Extract bounded contexts from XD user flows: screens serving the same business capability with shared language belong together.
- Derive aggregate roots from XD screens where a single entity owns transactional consistency (e.g., an Order screen owns line items).
- Define domain events from XD state transitions visible across screens (e.g., Order Placed, Payment Confirmed).
- Build a ubiquitous language glossary from labels, button text, and form field names found across XD artboards.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
