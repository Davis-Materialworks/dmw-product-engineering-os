# HIPAA Compliance Pack

## Purpose

The Health Insurance Portability and Accountability Act (HIPAA) applies to covered entities (healthcare providers, health plans, healthcare clearinghouses) and their business associates who handle Protected Health Information (PHI). It mandates administrative, physical, and technical safeguards to ensure the confidentiality, integrity, and availability of electronic PHI (ePHI). This pack identifies design-to-code obligations but does not provide legal advice — consult qualified counsel and your organization's Privacy Officer for compliance determinations.

## Design-to-Code Checks

1. **PHI identification**: Mark every artboard or component that displays, collects, transmits, or stores Protected Health Information. PHI includes not just medical data but also demographic identifiers that could identify an individual. Tag as `HIPAA_PHI_SURFACE`.

2. **Minimum necessary access**: Verify that role-based views enforce least-privilege — a billing clerk sees billing fields but not clinical notes, a lab technician sees lab results but not psychiatric evaluations. Flag any artboard where all roles see all PHI fields as `HIPAA_MINIMUM_NECESSARY_GAP`.

3. **Encryption at rest and in transit**: Confirm that data flows specify TLS 1.2+ for PHI in transit and AES-256 or equivalent for PHI at rest. Flag any artboard annotation, flow diagram, or architecture note that references unencrypted PHI storage or transmission without corresponding encryption controls.

4. **Access logging and audit trails**: Verify that every PHI access, modification, creation, and deletion is logged with user identity, timestamp, action, and affected record. Admin interfaces must expose these audit logs. Flag any PHI interaction without a corresponding audit trail design.

5. **Business Associate Agreements (BAAs)**: When integrations with third-party services (analytics, cloud storage, messaging, AI/ML APIs) process PHI, flag as `HIPAA_BAA_REQUIRED` — a BAA must be executed before PHI flows through that service.

6. **Automatic logoff and session management**: Confirm session timeout behavior for PHI-facing interfaces — recommend 15 minutes of inactivity for clinical contexts, with a warning at 13 minutes. PHI must not remain visible on an unattended screen.

7. **PHI redaction and de-identification**: When PHI appears in screenshots, test data, or non-production environments, verify de-identification mechanisms are in place. Flag artboard mockups that use real-looking patient data as `HIPAA_PHI_IN_MOCK`. The Safe Harbor method requires removal of 18 identifiers.

8. **Breach notification readiness**: Verify that audit and access logs are structured to support breach assessment — within 60 days of discovery, covered entities must determine whether a breach requires notification. Flag any data flow that lacks the logging granularity to reconstruct a breach timeline.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- Has the organization's Privacy Officer or Security Officer reviewed the PHI data flows shown in these artboards?
- Are all third-party services processing PHI covered by a signed BAA?
- Does the authentication system support role-based access at the field level, not just the page level?
- Are PHI audit logs designed to be immutable and stored separately from the application database?
- Is there a documented breach notification procedure, and does the audit trail architecture support it?

## Related Packs\n\n- **SOC 2**: Shared security controls around access management, audit logging, encryption, and incident response.\n- **GDPR**: Patient data rights overlap — right to access, erasure, and data portability apply under both frameworks.\n- **PCI-DSS**: Payment card data in healthcare billing contexts triggers overlapping encryption and access control requirements.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute legal advice, a HIPAA compliance certification, or a guarantee of regulatory compliance. Consult qualified healthcare counsel and your organization's Privacy/Security Officer.