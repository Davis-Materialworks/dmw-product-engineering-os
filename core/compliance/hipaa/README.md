# HIPAA Compliance Pack

## Purpose
For protected health information, enforce minimum necessary display, role-based access, auditability, timeout behavior, redaction, and secure sharing flows. Do not claim HIPAA compliance; flag required legal/security review.

## Design-to-Code Checks
- Identify sensitive data shown in XD artboards.
- Mark CONFIRMED, INFERRED, ASSUMED, and UNKNOWN compliance-relevant claims.
- Require least-privilege UI behavior for protected actions.
- Require accessible consent, error, recovery, export, deletion, or audit surfaces where relevant.
- Escalate legal or regulatory uncertainty instead of claiming compliance.

## Final Review Rule
If this pack is relevant to the product domain, XD_SECURITY_REVIEWER and XD_PRINCIPAL_ENGINEER must review the architecture before final output.
