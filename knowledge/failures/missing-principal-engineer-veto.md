# Missing Principal Engineer Veto

## Root Cause
Architecture is accepted without a senior engineering review of scalability, security, maintainability, testability, and performance.

## Detection Pattern
Implementation plan has no explicit architecture veto/pass decision.

## Correction Strategy
Run XD_PRINCIPAL_ENGINEER before finalizing architecture and reject plans that fail the world-class gate.

## Prevention Rule
No implementation plan can proceed with Architecture, Maintainability, Security, or Testability below threshold.
