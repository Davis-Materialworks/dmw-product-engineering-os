# Modal Inside Modal

## Risk
Nested modal flows create focus traps, unclear escape behavior, and high cognitive load.

## Detection Pattern
Trace XD interaction flows where a modal dialog triggers a second overlay on top of it — look for stacked dimmed backgrounds, nested close buttons, or confirmation dialogs that launch from within an already-open modal. Flag any flow where the user must dismiss two or more overlays in reverse order to return to the main screen. Check whether focus management is defined for each nesting level.

## Correction Strategy
- Preserve the user goal.
- Remove or reduce the anti-pattern.
- Add accessible labels, structure, feedback, or alternative controls.
- Verify with keyboard, screen reader, responsive, and state tests where relevant.

## Override Level
Strongly Recommend by default. Require or Block when accessibility, security, payment, healthcare, admin, or destructive workflows are involved.
