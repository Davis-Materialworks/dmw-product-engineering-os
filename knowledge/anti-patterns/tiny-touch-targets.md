# Tiny Touch Targets

## Risk
Touch targets below platform/WCAG expectations increase motor difficulty and error rates.

## Detection Pattern
Measure interactive elements on XD artboards designed for mobile viewports: flag any tappable area smaller than 44x44 CSS pixels (WCAG 2.5.5 minimum). Check densely packed controls like inline date pickers, table row actions, map pins, and icon-only toolbars. Verify spacing between adjacent touch targets — elements closer than 8px apart risk mis-taps even if individually large enough.

## Correction Strategy
- Preserve the user goal.
- Remove or reduce the anti-pattern.
- Add accessible labels, structure, feedback, or alternative controls.
- Verify with keyboard, screen reader, responsive, and state tests where relevant.

## Override Level
Strongly Recommend by default. Require or Block when accessibility, security, payment, healthcare, admin, or destructive workflows are involved.
