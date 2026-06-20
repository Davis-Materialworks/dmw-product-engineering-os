# GDPR Compliance Pack

## Purpose

The General Data Protection Regulation (GDPR) applies to any organization processing personal data of individuals in the European Economic Area (EEA), regardless of where the organization is based. It requires data protection by design and by default, lawful bases for processing, and grants individuals rights over their data including access, rectification, erasure, portability, and objection to automated decision-making. This pack identifies design-to-code obligations but does not provide legal advice — consult qualified counsel for regulatory determinations.

## Design-to-Code Checks

1. **Data minimization**: Confirm the UI only collects fields necessary for the stated purpose. Flag any artboard where optional fields are presented as required or where excessive personal data is gathered without clear justification. Mark as `GDPR_MINIMIZATION_GAP` when collection exceeds stated purpose.

2. **Consent surfaces**: Verify consent mechanisms are granular, affirmative, and withdrawable — no pre-ticked checkboxes, no bundled consent where one checkbox covers marketing + analytics + third-party sharing. Each processing purpose must have its own opt-in. Cookie consent must be as easy to withdraw as it was to give.

3. **Right to erasure (Art. 17)**: Confirm the UI exposes or references a mechanism for users to request deletion of their personal data. In administrative interfaces, verify that delete operations cascade to all copies, backups, and third-party recipients where technically feasible.

4. **Data portability (Art. 20)**: Verify user-facing interfaces provide an export mechanism producing structured, commonly-used, machine-readable formats (JSON, CSV). Flag designs that export only PDFs or images as `GDPR_PORTABILITY_GAP`.

5. **Data Protection Impact Assessment (DPIA) triggers**: When artboards include large-scale processing, profiling, biometric data, systematic monitoring, or special-category data (health, ethnicity, political views), flag as `GDPR_DPIA_REQUIRED` — a DPIA must be completed before implementation.

6. **Cross-border transfer indicators**: When data flows or architecture diagrams show personal data leaving the EEA (to US servers, third-party processors, or APIs), flag the transfer mechanism — require evidence of adequacy decision, Standard Contractual Clauses (SCCs), or Binding Corporate Rules (BCRs).

7. **Retention and transparency**: Confirm data-retention periods are documented and visible. Flag UI that archives data indefinitely without user-facing retention disclosures. Audit logs must distinguish between "soft delete" (user-facing removal) and "hard delete" (actual data erasure).

8. **Privacy by default**: Verify that privacy-protective settings are the default — profiles are not public by default, tracking is opt-in not opt-out, and the most privacy-preserving option is pre-selected. Flag dark patterns that nudge users toward data-sharing choices.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- What is the lawful basis for each data processing activity shown in these artboards?
- Is there a documented data flow showing where personal data enters, is stored, processed, and leaves the system?
- Does the design expose mechanisms for users to access, correct, delete, and export their data?
- Have third-party processors and sub-processors been identified for all integrations?
- Is there a data retention schedule, and does the UI reflect it in archive/delete workflows?

## Related Packs\n\n- **SOC 2**: Shared privacy controls — SOC 2 Privacy (P-series) criteria map to GDPR's data protection principles.\n- **HIPAA**: Overlapping patient data rights (access, erasure, portability) and data minimization requirements.\n- **PDPA**: Convergent consent, purpose limitation, and cross-border transfer principles across data protection regimes.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute legal advice, a legal compliance determination, or a guarantee of GDPR compliance. Consult qualified privacy counsel.