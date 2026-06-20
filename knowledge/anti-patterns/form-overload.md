# Form Overload

## Risk
Long forms without grouping, defaults, progress, validation, or save/resume create abandonment.

## Detection Pattern
Inspect XD artboards for forms with 10+ visible fields on a single screen without section dividers, step indicators, or progressive disclosure. Count fields against the viewport height — if scrolling is required before the user knows how many steps remain, flag it. Check whether required vs. optional fields are visually differentiated and whether smart defaults pre-fill any inputs.

## Correction Strategy
- Preserve the user goal.
- Remove or reduce the anti-pattern.
- Add accessible labels, structure, feedback, or alternative controls.
- Verify with keyboard, screen reader, responsive, and state tests where relevant.

## Override Level
Strongly Recommend by default. Require or Block when accessibility, security, payment, healthcare, admin, or destructive workflows are involved.
