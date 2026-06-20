# PDPA Compliance Pack

## Purpose

Personal Data Protection Acts (PDPA) exist across multiple jurisdictions — Singapore's PDPA (2012, amended 2020), Thailand's PDPA (2019), Malaysia's PDPA (2010), and others — each establishing data protection obligations around consent, purpose limitation, notification, access and correction, accuracy, protection, retention limitation, transfer limitation, and breach notification. While specifics differ, the core principles are convergent. This pack surfaces common PDPA obligations across jurisdictions but does not provide legal advice — consult qualified counsel in the relevant jurisdiction.

## Design-to-Code Checks

1. **Consent model verification**: Verify that consent mechanisms are jurisdiction-appropriate. Singapore allows deemed consent in certain circumstances; Thailand requires explicit consent for sensitive data. Flag any artboard where consent is bundled, pre-ticked, or presented as a condition of service when not strictly necessary as `PDPA_CONSENT_GAP`.

2. **Purpose limitation**: Confirm that data collection screens state the purpose at or before the point of collection. If a form collects an email "for account creation" but the data flow routes it to a marketing platform, flag as `PDPA_PURPOSE_MISMATCH`. Data cannot be used for purposes beyond what was disclosed without fresh consent.

3. **Notification obligation**: Verify that data collection interfaces inform individuals of: what data is collected, the purpose, who it may be disclosed to, and whether it will be transferred abroad. Flag artboards lacking visible privacy notices or collection statements as `PDPA_NOTIFICATION_GAP`.

4. **Access and correction mechanisms**: Confirm that authenticated users can access their personal data held by the system and request corrections. Flag any profile page that displays data but provides no edit, correction, or download mechanism as `PDPA_ACCESS_GAP`. Some jurisdictions (Singapore) permit fees for access requests; others (Thailand) require free access.

5. **Cross-border transfer controls**: When data flows show personal data leaving the jurisdiction, verify that the destination country provides a comparable standard of protection OR that legally required safeguards are in place (contractual clauses, binding corporate rules, consent). Flag unqualified cross-border data flows as `PDPA_TRANSFER_GAP`.

6. **Data breach notification readiness**: Confirm that the system captures sufficient logging to identify, contain, and assess a data breach. Most PDPA regimes require breach notification within 72 hours (Singapore: as soon as practicable; Thailand: 72 hours; Malaysia: as soon as practicable with 14-day detailed report). Flag systems that cannot reconstruct a breach timeline.

7. **Retention limitation**: Verify that data retention periods are defined and enforced. Designs that store personal data indefinitely without a documented retention justification or that lack deletion/archival mechanisms should be flagged as `PDPA_RETENTION_GAP`. Retention must not exceed what is necessary for the stated purpose.

8. **Protection obligation**: Confirm that reasonable security measures protect personal data from unauthorized access, collection, use, disclosure, copying, modification, disposal, or similar risks. This includes encryption, access controls, and regular security testing. Flag any component that stores or transmits personal data without corresponding security controls.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- Which specific PDPA jurisdiction applies (Singapore, Thailand, Malaysia, Philippines, etc.) and has counsel confirmed the interpretation?
- Does the design include a Data Protection Officer (DPO) contact mechanism where required?
- Are cross-border data transfers documented with the legal basis for each transfer?
- Has a Data Protection Impact Assessment (DPIA) been conducted for high-risk processing activities?
- Is the breach notification workflow documented and can the system produce the required evidence within the notification window?

## Related Packs\n\n- **GDPR**: Convergent core principles — consent, purpose limitation, access/correction, breach notification, and cross-border transfer controls are shared across both frameworks.\n- **SOC 2**: Privacy (P-series) criteria and confidentiality controls map to PDPA's protection obligation and retention limitation requirements.\n- **ISO 27001**: Provides the security management framework for meeting PDPA's "reasonable security measures" protection obligation.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations across multiple PDPA jurisdictions. It does not constitute legal advice, a compliance determination, or a guarantee of regulatory compliance in any specific jurisdiction. Consult qualified data protection counsel in the relevant jurisdiction.