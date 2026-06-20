# Decision Memory

Future agents must read relevant decision records before proposing changes. Decisions explain why the OS chose a product, UX, architecture, design-system, or implementation direction.

## Required Fields

- id
- title
- context
- decision
- alternatives
- tradeoffs
- accepted_risks
- future_reconsideration

## Rule

Do not reverse a prior decision silently. Preserve it, explicitly supersede it with a new decision record, or ask the user when evidence is insufficient.
