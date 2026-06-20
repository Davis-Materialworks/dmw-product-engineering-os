# Unlabeled Inference

## Root Cause
The agent blends confirmed XD facts with guesses, making fidelity and review impossible.

## Detection Pattern
Architecture, tokens, or components are asserted without CONFIRMED, INFERRED, ASSUMED, or UNKNOWN status.

## Correction Strategy
Attach confidence status to every major design, product, data, and implementation claim.

## Prevention Rule
Final output must include an evidence ledger for all high-impact claims.
