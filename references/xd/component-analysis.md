# XD Component Analysis

XD components can contain main components, instances, overrides, states, and responsive resize behavior. Treat these as design-system signals.

## Detection

Identify components even when layer names are poor. Use visual repetition, shared structure, repeated text roles, common icon placement, repeated dimensions, repeated states, and recurring interaction patterns.

## Component debt signals

- Same button recreated many times with slightly different colors.
- Text styles copied manually instead of using character styles.
- Component instances with structural overrides that should be variants.
- Missing hover/focus/disabled/error/loading states.
- Icons embedded as raster images when vector/SVG would be appropriate.
- Components named by appearance instead of purpose.

## Variant model

For each component infer:

- name
- purpose
- variants
- sizes
- states
- slots
- props
- controlled/uncontrolled behavior
- accessibility contract
- test cases

## Naming rules

Use domain-semantic names when the component is product-specific. Use design-system names when generic.

Examples:

- Generic: `Button`, `Dialog`, `Tabs`, `DataTable`, `Toast`.
- Domain: `InvoiceStatusBadge`, `ClaimReviewPanel`, `PatientTimeline`, `LoanOfferCard`.

## State standard

Every interactive component should consider default, hover, focus-visible, active, disabled, loading, error, success, selected/current, read-only, and skeleton states.
