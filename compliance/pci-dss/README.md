# PCI-DSS Compliance Pack

## Purpose
For cardholder data, keep payment collection inside approved payment boundaries, avoid storing sensitive card data, redact logs, and make payment errors recoverable without exposing sensitive detail.

## Design-to-Code Checks
- Identify sensitive data shown in XD artboards.
- Mark CONFIRMED, INFERRED, ASSUMED, and UNKNOWN compliance-relevant claims.
- Require least-privilege UI behavior for protected actions.
- Require accessible consent, error, recovery, export, deletion, or audit surfaces where relevant.
- Escalate legal or regulatory uncertainty instead of claiming compliance.

## Final Review Rule
If this pack is relevant to the product domain, XD_SECURITY_REVIEWER and XD_PRINCIPAL_ENGINEER must review the architecture before final output.
