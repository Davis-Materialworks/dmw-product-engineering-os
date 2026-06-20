# Event-Driven Systems

## Use When
Use when workflows are asynchronous, audit-heavy, integration-heavy, or require decoupled reactions to domain events.

## Avoid When
Avoid when request-response flows are clearer, safer, and easier to operate.

## XD-to-Code Application
- Trace XD user interactions (clicks, form submissions, navigation) to domain events: each meaningful action emits an event.
- Identify async workflows from XD screens that show loading states, background processing, or real-time updates.
- Map XD notification patterns (toasts, banners, status indicators) to event subscribers that update UI independently.
- Design event schemas from XD data shapes flowing between screens, not from database tables.

## Review Questions
- Does this pattern reduce complexity for this project?
- Are boundaries clear to future developers?
- Does the pattern support accessibility, security, and testing requirements?
- What simpler architecture was considered and rejected?
