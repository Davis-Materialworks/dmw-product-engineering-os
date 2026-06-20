# Pixel Copy Without Design Critique

## Root Cause
The agent treats XD as a visual trace instead of a product specification that can contain UX defects.

## Detection Pattern
Output reproduces layout but has no UX, accessibility, conversion, or enterprise-readiness critique.

## Correction Strategy
Run XD_DESIGN_CRITIC before implementation and require challenged assumptions in the plan.

## Prevention Rule
Never implement a nontrivial XD design until critique findings are accepted, remediated, or explicitly deferred.
