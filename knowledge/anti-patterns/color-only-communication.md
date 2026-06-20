# Color Only Communication

## Risk
Meaning conveyed only through color fails accessibility and weakens comprehension.

## Detection Pattern
Scan XD artboards for status indicators, error states, or data visualizations that use only color (red/green, blue/orange) without icons, text labels, or pattern fills. Flag any component where removing color would make its meaning ambiguous. Common in charts with single-hue legends, form validation that shows only red borders, and toggle states rendered as color changes alone.

## Correction Strategy
- Preserve the user goal.
- Remove or reduce the anti-pattern.
- Add accessible labels, structure, feedback, or alternative controls.
- Verify with keyboard, screen reader, responsive, and state tests where relevant.

## Override Level
Strongly Recommend by default. Require or Block when accessibility, security, payment, healthcare, admin, or destructive workflows are involved.
