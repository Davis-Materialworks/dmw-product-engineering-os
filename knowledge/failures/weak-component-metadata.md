# Weak Component Metadata

## Root Cause
The system extracts generic component names without industry, accessibility, performance, or testing obligations.

## Detection Pattern
Inventory contains only names like Button, Input, Card, or Table.

## Correction Strategy
Emit component metadata objects with industry, accessibility, performance, testing, states, and ownership.

## Prevention Rule
Every nontrivial component inventory item must use the component metadata schema.
