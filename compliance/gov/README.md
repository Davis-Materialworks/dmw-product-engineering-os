# Government / FedRAMP Compliance Pack

## Purpose

Federal Risk and Authorization Management Program (FedRAMP) standardizes security assessment and authorization for cloud services used by US federal agencies. It enforces NIST SP 800-53 controls across three impact levels (Low, Moderate, High) and requires continuous monitoring. Other government frameworks (StateRAMP, IRS 1075, CJIS, ITAR) impose additional controls. This pack identifies design-to-code obligations but does not authorize a system for government use — engage your Agency Authorizing Official (AO) and Third-Party Assessment Organization (3PAO).

## Design-to-Code Checks

1. **Authorization boundary**: Verify the system boundary diagram clearly delineates what is in-scope for the authorization package. Every component, interface, and data flow inside the boundary inherits all FedRAMP controls. Flag any external service or API consumed by the system that is not documented in the boundary as `FEDRAMP_BOUNDARY_GAP`.

2. **FIPS 140-2 / 140-3 cryptography**: Confirm that all cryptographic modules used in the design (TLS libraries, hashing functions, encryption at rest) are FIPS 140-2 validated or in-process. Flag any non-FIPS cryptographic usage (e.g., MD5 for any purpose, non-FIPS TLS cipher suites, unvalidated open-source crypto) as `FIPS_VALIDATION_REQUIRED`.

3. **Continuous monitoring**: Verify that the architecture includes ongoing assessment of security controls — vulnerability scanning (monthly at minimum), configuration monitoring, log review, and POA&M (Plan of Action and Milestones) tracking. Flag any system without designed-in monitoring as `FEDRAMP_MONITORING_GAP`.

4. **Identity and authentication**: Confirm PIV/CAC/smart-card-compatible authentication, MFA enforcement for all privileged and user access, and integration with agency identity providers (ICAM). Flag username/password-only authentication for privileged access as `FEDRAMP_AUTHENTICATION_GAP`.

5. **Separation of duties**: Verify that administrative roles are separated — no single user can both approve a change and deploy it, both create accounts and review audit logs, or both develop code and push to production. Flag designs that collapse these roles.

6. **E-authentication risk assessment**: For citizen-facing services, verify that the authentication level (anonymous, low, moderate, high per NIST SP 800-63) matches the sensitivity of the transaction. Tax filing requires higher assurance than viewing public park hours.

7. **Section 508 / accessibility**: Confirm WCAG 2.0 Level AA compliance as a non-negotiable floor for all government-facing interfaces. Flag any artboard that fails contrast, keyboard navigation, or screen-reader requirements.

8. **Data sovereignty and residency**: Verify where data is stored geographically — many government contracts require data to remain within CONUS (continental US). Flag any data flow that routes government data through non-US infrastructure, even for processing or caching.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- What is the target FedRAMP impact level (Low, Moderate, High), and has the FIPS 199 categorization been completed?
- Is there a System Security Plan (SSP) and has the authorization boundary been approved by the AO?
- Are all cryptographic modules FIPS 140-2 validated, with certificate numbers documented?
- Does the architecture support Continuous Monitoring (ConMon) deliverables — vulnerability scans, configuration baselines, POA&M updates?
- Is the system subject to additional overlays (IRS 1075, CJIS, ITAR, DoD IL4/5/6)?

## Related Packs\n\n- **ISO 27001**: Shared continuous monitoring, risk assessment, and access control requirements — FedRAMP maps to NIST SP 800-53 which overlaps with ISO 27001 Annex A controls.\n- **WCAG**: Section 508 mandates WCAG 2.0 AA — accessibility is a regulatory requirement, not optional, for government systems.\n- **SOC 2**: Shared vendor risk management and security monitoring controls relevant for cloud service providers pursuing both frameworks.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute a FedRAMP authorization, ATO, or legal advice. Authority to Operate is granted exclusively by the Agency Authorizing Official. Engage your 3PAO and AO.