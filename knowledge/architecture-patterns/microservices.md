# Microservices

## Use When
Use only when bounded contexts need independent deployment, scaling, ownership, and data lifecycle.

## Avoid When
Avoid for early products, small teams, or systems without observability and platform maturity.

## XD-to-Code Application
- Map each XD screen group to a candidate bounded context and identify cross-screen data flows as service boundaries.
- Define API contracts from XD interaction patterns: what data each screen loads independently vs. what it fetches on-demand.
- Treat XD navigation flows as inter-service call graphs; screens that share no data dependencies may belong to separate services.
- Design client-side composition from XD layouts: identify where the UI aggregates data from multiple services on a single screen.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
