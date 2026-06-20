# XD Design Spec Analysis

Use Design Specs as the highest-fidelity XD handoff input when available.

## Extract

- artboard dimensions
- measurements
- colors
- character styles
- CSS snippets
- downloadable assets
- layout spacing
- component naming
- design tokens if named
- platform view assumptions

## Cautions

XD CSS snippets are hints, not final architecture. Do not paste them blindly. Normalize into tokens, semantic components, responsive layout, and accessible states.

## Token normalization

Map raw values to semantic use:

- raw color used for button background -> `color.action.primary.background`
- raw muted text -> `color.text.secondary`
- card background -> `color.surface.card`
- destructive red -> `color.feedback.danger`

## Missing data strategy

If Design Specs are absent, infer from screenshots and exports. Mark inferred values as provisional.
