# Duplicate Elimination

## Rule
Eliminate duplication when repeated tokens, variants, validation rules, data formatting, or interaction behavior create drift risk.

## Detection Pattern
- Repeated code or visual structures drift across screens.
- Design intent is hidden behind layout-only names.
- Tests are difficult because state or domain logic is trapped in UI.
- Performance cost grows with data size, media size, or route complexity.

## Correction Strategy
- Preserve visible behavior and design intent.
- Extract the smallest useful abstraction.
- Add or recommend tests around changed behavior.
- Re-run accessibility and performance checks when the refactor changes interaction or rendering.
