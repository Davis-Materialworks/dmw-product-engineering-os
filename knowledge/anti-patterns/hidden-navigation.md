# Hidden Navigation

## Risk
Navigation hidden behind unclear icons or gestures reduces discoverability and confidence.

## Detection Pattern
Examine XD artboards for navigation triggered only by hamburger menus on desktop, unlabeled icon-only toolbars, swipe gestures without affordance indicators, or hover-revealed menus invisible to keyboard and touch users. Flag any primary navigation item that requires discovery — if the user can't see where to go within 3 seconds of landing, the navigation is hidden.

## Correction Strategy
- Preserve the user goal.
- Remove or reduce the anti-pattern.
- Add accessible labels, structure, feedback, or alternative controls.
- Verify with keyboard, screen reader, responsive, and state tests where relevant.

## Override Level
Strongly Recommend by default. Require or Block when accessibility, security, payment, healthcare, admin, or destructive workflows are involved.
