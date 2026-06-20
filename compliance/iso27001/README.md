# ISO 27001 Compliance Pack

## Purpose

ISO/IEC 27001 is the international standard for Information Security Management Systems (ISMS). It requires organizations to systematically examine security risks, design and implement a coherent set of controls (drawn from Annex A, now aligned with ISO 27002:2022), and adopt an ongoing management process. Unlike point-in-time audits, ISO 27001 mandates continuous improvement through the Plan-Do-Check-Act cycle. This pack identifies design-to-code obligations but does not provide legal advice or certification — engage an accredited certification body.

## Design-to-Code Checks

1. **Asset inventory and classification**: Verify that the system identifies information assets (databases, file storage, APIs, logs) and their classification level (Public, Internal, Confidential, Restricted). Flag any design that treats all data uniformly — a marketing landing page and a customer PII database must not share the same security posture.

2. **Risk assessment integration**: Confirm that design decisions reference the organization's risk assessment. Flag any feature that introduces a risk scenario not covered by existing risk treatment plans as `ISO27001_RISK_REGISTER_GAP`. Risk acceptance decisions must be documented, not implicit.

3. **Access control (Annex A.5)**: Verify role-based access control, segregation of duties, and least-privilege enforcement. Administrative interfaces must require MFA. Flag shared accounts, hard-coded credentials, or access provisioning that bypasses formal approval workflows. Privileged access must be reviewed periodically.

4. **Cryptography (Annex A.8.24)**: Confirm a documented cryptographic policy is applied — encryption at rest (AES-256), encryption in transit (TLS 1.2+), key management lifecycle, and certificate management. Flag any system that generates, stores, or distributes cryptographic keys without a key management policy.

5. **Incident management (Annex A.5.24–A.5.27)**: Verify that the system supports the incident response lifecycle — detection, containment, eradication, recovery, and post-incident review. Logging must capture sufficient evidence for forensic analysis. Flag any security-sensitive component that lacks alerting or that logs sensitive data making logs themselves a risk.

6. **Supplier security (Annex A.5.19–A.5.22)**: When the architecture includes third-party services, verify that supplier security requirements are defined and monitored. Flag any integration without a documented supplier security assessment or where supplier data access exceeds the principle of least privilege.

7. **Physical and environmental security (Annex A.7)**: Though primarily operational, flag designs where client-side applications store sensitive data in localStorage/sessionStorage accessible on shared or unattended devices — this creates a physical security exposure vector.

8. **Continuous improvement evidence**: Verify that monitoring, measurement, analysis, and evaluation are designed into the system. Admin dashboards should surface ISMS metrics (incident counts, access review status, patch compliance). Flag operational interfaces that provide no measurement capability as `ISO27001_PDCA_GAP`.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- What is the information classification scheme and does the architecture reflect tiered security controls per classification level?
- Has a risk assessment been completed for this system, and are residual risks within the organization's risk appetite?
- Does the system produce evidence required for ISMS audits — access reviews, change management records, incident logs?
- Are all third-party suppliers assessed for security posture, and are their responsibilities documented?
- Is there a documented Statement of Applicability (SoA) mapping which Annex A controls apply?

## Related Packs\n\n- **SOC 2**: Both require information security management — ISO 27001 is a management system standard, while SOC 2 is an attestation standard; controls largely overlap.\n- **Government/FedRAMP**: FedRAMP's NIST SP 800-53 controls map closely to ISO 27001 Annex A, and both require continuous monitoring.\n- **GDPR**: ISO 27001 provides the security management framework that GDPR's "appropriate technical and organizational measures" require.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute an ISO 27001 certification, ISMS audit opinion, or legal advice. Certification is issued exclusively by accredited certification bodies. Engage your ISMS manager and certification body.