# GDPR Compliance Pack

## Purpose
For EU personal data, minimize collection, expose consent and preference controls, support access/deletion/export workflows, document retention, and avoid dark patterns. Do not claim legal compliance; flag product and engineering obligations.

## Design-to-Code Checks
- Identify sensitive data shown in XD artboards.
- Mark CONFIRMED, INFERRED, ASSUMED, and UNKNOWN compliance-relevant claims.
- Require least-privilege UI behavior for protected actions.
- Require accessible consent, error, recovery, export, deletion, or audit surfaces where relevant.
- Escalate legal or regulatory uncertainty instead of claiming compliance.

## Final Review Rule
If this pack is relevant to the product domain, XD_SECURITY_REVIEWER and XD_PRINCIPAL_ENGINEER must review the architecture before final output.
