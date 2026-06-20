# PCI-DSS Compliance Pack

## Purpose

The Payment Card Industry Data Security Standard (PCI-DSS) applies to any organization that stores, processes, or transmits cardholder data (CHD) or sensitive authentication data (SAD). It defines 12 core requirements across six control objectives: build and maintain secure networks, protect cardholder data, maintain a vulnerability management program, implement strong access control measures, regularly monitor and test networks, and maintain an information security policy. This pack identifies design-to-code obligations but does not provide legal advice or guarantee PCI compliance — engage a Qualified Security Assessor (QSA).

## Design-to-Code Checks

1. **Cardholder data boundaries**: Identify every artboard, component, or data flow that touches Primary Account Numbers (PANs), cardholder names, service codes, or expiration dates. Map the Cardholder Data Environment (CDE) boundary — flag any element outside the CDE that touches CHD as `PCI_CDE_BOUNDARY_VIOLATION`.

2. **Prohibited data storage**: Verify that sensitive authentication data (full track data, CVV/CVC, PIN, PIN block) is NEVER stored after authorization, even in logs, error messages, or debugging output. Flag any data model, log schema, or error-handling flow that captures SAD as `PCI_PROHIBITED_STORAGE`.

3. **Tokenization and truncation**: When PANs appear in non-payment contexts (customer profiles, receipts, order history), verify they are either truncated (first 6, last 4 digits maximum) or replaced with a service-provider-generated token. Flag unmasked PANs outside the payment flow as `PCI_TOKENIZATION_REQUIRED`.

4. **SAQ applicability**: Determine which SAQ (Self-Assessment Questionnaire) the architecture implies — SAQ A (fully outsourced, iframe/redirect), SAQ A-EP (partially outsourced, direct post), SAQ D (merchant handles card data). Flag SAQ D architectures early — they require the full 300+ controls vs. ~20 for SAQ A.

5. **Network segmentation**: Verify that the CDE is segmented from non-CDE systems via firewalls, VLANs, or separate VPCs. Flag architectures where the payment service shares a network segment with general-purpose application servers as `PCI_SEGMENTATION_GAP`.

6. **Key management**: Confirm that cryptographic keys used for cardholder data protection are managed in an HSM or key management service (AWS KMS, Azure Key Vault), with documented key rotation schedules. Flag hard-coded keys, keys in config files, or keys stored alongside encrypted data as `PCI_KEY_MANAGEMENT_GAP`.

7. **Access control**: Verify that access to cardholder data is on a need-to-know basis, with unique user IDs, MFA for all CDE access, and automatic session timeouts. Flag shared-account designs, lack of MFA in CDE paths, or any admin panel that accesses CHD without MFA.

8. **Logging and monitoring**: Confirm that all access to cardholder data is logged with user identity, timestamp, and action. Audit logs must be tamper-proof and retained for at least 12 months (last 3 months immediately available). Flag any CHD access path without corresponding audit trail design.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- Which SAQ type does this architecture fall under, and has a QSA reviewed that determination?
- Is the Cardholder Data Environment clearly bounded, with firewalls, separate accounts, and restricted access?
- Are third-party payment components (SDKs, iframes, redirects) validated and listed on the PCI SSC website?
- Does the system use a PCI-validated Point-to-Point Encryption (P2PE) solution or an approved tokenization service?
- Is there a documented incident response plan specific to cardholder data breaches?

## Related Packs\n\n- **SOC 2**: Shared controls around access management, change management audit trails, and vendor risk assessment.\n- **ISO 27001**: Overlapping requirements for cryptography, key management, access control, and logging/audit trails.\n- **HIPAA**: Healthcare payment card transactions must satisfy both PCI-DSS encryption requirements and HIPAA's PHI safeguards.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute a PCI-DSS compliance assessment, SAQ completion, Report on Compliance (ROC), or legal advice. Engage a Qualified Security Assessor (QSA) for official PCI-DSS validation.