# SOC 2 Compliance Pack

## Purpose

SOC 2 (System and Organization Controls 2) is an auditing standard developed by the AICPA for service organizations that store, process, or transmit customer data in the cloud. It evaluates controls across five Trust Services Criteria (TSC): Security, Availability, Processing Integrity, Confidentiality, and Privacy. Unlike prescriptive regulations, SOC 2 requires the organization to define its own control objectives and demonstrate they are met. This pack identifies design-to-code obligations but does not guarantee SOC 2 attestation — engage your auditor early.

## Design-to-Code Checks

1. **Security (Common Criteria / CC-series)**: Verify that every system boundary has authentication, authorization, and access control. Flag any artboard or flow diagram where unauthenticated users can reach sensitive functionality as `SOC2_SECURITY_BOUNDARY_GAP`. Logical and physical access controls must be designed into every component.

2. **Availability (A-series)**: Confirm the architecture includes monitoring, alerting, and recovery controls. Flag designs without health-check endpoints, circuit breakers for external dependencies, or degradation states as `SOC2_AVAILABILITY_GAP`. Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) should be referenced.

3. **Processing Integrity (PI-series)**: Verify that data processing flows include input validation, error handling, and idempotency where needed. Flag any workflow where processing errors could silently corrupt data as `SOC2_PROCESSING_INTEGRITY_GAP`. Batch processing must detect and surface partial failures.

4. **Confidentiality (C-series)**: Confirm that confidential data (not just PII — includes trade secrets, business data, client IP) is identified and protected. Flag artboards where confidential data is displayed to unauthorized roles or transmitted without encryption as `SOC2_CONFIDENTIALITY_GAP`. Data classification labels should be visible in the design.

5. **Privacy (P-series)**: Verify that the design addresses the organization's privacy notice commitments — if the privacy notice says "we do not share data with third parties," the data flow diagram must not route PII to third-party APIs. Flag discrepancies between privacy promises and actual data flows as `SOC2_PRIVACY_NOTICE_GAP`.

6. **Change management evidence**: Administrative interfaces must log who made what configuration change and when. Flag any admin panel without change audit trails as `SOC2_CHANGE_MANAGEMENT_GAP`. SOC 2 auditors will ask for evidence of authorized, tested, and approved changes.

7. **Vendor risk indicators**: When the architecture integrates with third-party services (auth providers, payment processors, cloud infrastructure, monitoring tools), flag each as `SOC2_VENDOR_RISK` — the vendor's own SOC 2 report (or equivalent) must be reviewed, and their subservice organization impact assessed.

8. **Incident response surfaces**: Verify that the UI and operational tooling include mechanisms for detecting, reporting, and responding to security incidents. Flag any security-sensitive interface that lacks a visible "report incident" or escalation path.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- Which Trust Services Criteria are in scope for this system's SOC 2 audit (Security only, or Security + Availability + Confidentiality, etc.)?
- Has the control environment been mapped to the five TSC categories, and do these artboards align with those control objectives?
- Are vendor SOC 2 reports collected and reviewed for every third-party integration?
- Does the change management workflow produce auditable evidence (approval records, test results, deployment logs)?
- Is there a documented incident response plan, and do the operational interfaces support it?

## Related Packs\n\n- **ISO 27001**: Shared security management controls, asset classification, access control, and continuous improvement requirements.\n- **GDPR**: Shared privacy and data confidentiality obligations, including data classification and vendor risk assessment.\n- **HIPAA**: Shared security controls for audit logging, access management, and incident response — relevant if SOC 2 scope includes healthcare data.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute a SOC 2 audit opinion, attestation, or legal advice. Engage your auditor early and consult qualified counsel for regulatory determinations.