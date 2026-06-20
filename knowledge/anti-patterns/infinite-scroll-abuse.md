# Infinite Scroll Abuse

## Risk
Infinite scroll is harmful when users need position, comparison, selection, export, or completion.

## Detection Pattern
Identify XD screens where content extends past the viewport without pagination controls, a visible item count, a search/filter mechanism, or a "back to top" affordance. Flag any infinite-scroll list that lacks a footer, making it impossible to reach footer links. Check whether the XD flow includes comparison, selection across pages, or export actions — all of which infinite scroll undermines.

## Correction Strategy
- Preserve the user goal.
- Remove or reduce the anti-pattern.
- Add accessible labels, structure, feedback, or alternative controls.
- Verify with keyboard, screen reader, responsive, and state tests where relevant.

## Override Level
Strongly Recommend by default. Require or Block when accessibility, security, payment, healthcare, admin, or destructive workflows are involved.
