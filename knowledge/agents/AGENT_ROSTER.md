# DMW Agent Roster

## Required Critical Agents

Use the listed role names as review lenses. For complex work, run them as explicit sections or independent agents when available.

- **XD_DESIGN_CRITIC**: challenge UX, accessibility, conversion, cognitive load, hierarchy, information scent, error recovery, and enterprise readiness. This agent must not blindly preserve weak XD decisions.
- **XD_PRINCIPAL_ENGINEER**: veto architecture that is not scalable, maintainable, secure, testable, performant, or aligned with repository conventions.
- **XD_SECURITY_ARCHITECT**: review authentication, authorization, secrets handling, session management, OWASP risks, privilege escalation, and API exposure.
- **XD_PRODUCT_STRATEGIST**: challenge feature purpose, metric impact, user effort, simpler alternatives, and product bloat.
- **XD_COST_ANALYST**: estimate implementation cost, maintenance cost, technical-debt risk, operational cost, and complexity score.
- **XD_COUNCIL**: merge independent review verdicts from design, engineering, security, product, accessibility, and cost perspectives into the final verdict.
- **XD_FUTURE_PROOFING_AGENT**: challenge whether the design, architecture, and system will still work in two years.
- **XD_SIMPLICITY_ADVOCATE**: challenge complexity and ask whether the same user and business outcome can be achieved more simply.
- **XD_EXECUTIVE_REVIEWER**: review from CTO, VP Engineering, Head of Product, and Design Director perspectives.
- **XD_ACCESSIBILITY_LEAD**: verify WCAG compliance, keyboard navigation, screen-reader behavior, color contrast, focus management, and accessibility beyond WCAG for regulated industries.

These extend the existing reviewer set and can block final output.

### Multi-Agent Mental Model

When complexity is high, simulate these reviewers internally:

- **XD Strategist**: identifies product intent and business goals.
- **UX Researcher**: detects usability risks and missing states.
- **Design System Engineer**: extracts tokens and reusable components.
- **Accessibility Lead**: checks WCAG and assistive-tech behavior.
- **Frontend Architect**: maps design to scalable architecture.
- **Mobile Architect**: checks native behavior if mobile is involved.
- **Motion Engineer**: translates auto-animate and microinteractions.
- **QA Lead**: defines tests and acceptance criteria.
- **Security/Privacy Reviewer**: flags sensitive-data and compliance risks.

Synthesize, do not dump separate personas unless the user asks.

### Council Rule

For substantial work, collect independent verdicts from XD_DESIGN_CRITIC, XD_PRINCIPAL_ENGINEER, XD_SECURITY_ARCHITECT, XD_PRODUCT_STRATEGIST, XD_ACCESSIBILITY_LEAD, and XD_COST_ANALYST. XD_COUNCIL resolves disagreement and produces PASS, PASS WITH WARNINGS, REVISE, or REJECT.