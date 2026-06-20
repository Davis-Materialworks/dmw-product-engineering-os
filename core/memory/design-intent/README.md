# Design Intent Memory

Preserve intent, not just visuals. Before implementing or refactoring a screen, read matching intent records and keep business goals, user goals, and action hierarchy intact unless the user changes strategy.

## Record Fields

- screen
- business_goal
- user_goal
- primary_action
- secondary_action
- evidence
- preservation_rules

## Rule

If visual fidelity conflicts with intent, escalate the conflict and propose an intent-preserving design alternative.
