# WCAG Compliance Pack

## Purpose

The Web Content Accessibility Guidelines (WCAG), published by the W3C Web Accessibility Initiative (WAI), define how to make web content accessible to people with disabilities including visual, auditory, motor, cognitive, and speech impairments. WCAG 2.2 Level AA is the default target for most regulated industries and is referenced by Section 508, the ADA, and the European Accessibility Act (EAA 2025). Conformance is measured at three levels: A (minimum), AA (standard), and AAA (enhanced). This pack identifies design-to-code obligations but does not provide legal advice — consult accessibility counsel for compliance determinations.

## Design-to-Code Checks

1. **Perceivable — Text alternatives (1.1.1)**: Verify every non-text content element (images, icons, charts, video thumbnails) has a text alternative. Flag decorative images that lack `alt=""` and informative images that lack descriptive alt text. Complex images (charts, infographics) require long descriptions, not just short alt text.

2. **Perceivable — Adaptable content (1.3.1–1.3.5)**: Confirm that information, structure, and relationships are conveyed programmatically — headings follow a logical hierarchy (h1→h2→h3 without skipping levels), form inputs have associated labels, tables have headers and captions. Flag layouts where visual relationships are not available in the DOM.

3. **Perceivable — Distinguishable content (1.4.1–1.4.13)**: Verify color contrast ratios: 4.5:1 for normal text, 3:1 for large text (18px+ bold or 24px+ regular), and 3:1 for UI components and graphical objects. Flag color-only indicators (red/green status without an icon or text). Verify that content is readable at 200% zoom without horizontal scrolling at 1280px width (1.4.10 Reflow). For WCAG 2.2, check focus appearance (2.4.13) — focus indicators must have 3:1 contrast and be at least 2px thick.

4. **Operable — Keyboard accessibility (2.1.1–2.1.4)**: Confirm every interactive element is reachable and operable via keyboard — Tab, Shift+Tab, Enter, Space, Arrow keys. Flag drag-and-drop operations that lack keyboard alternatives, custom widgets without ARIA keyboard patterns, and keyboard traps where focus cannot escape a component.

5. **Operable — Navigable (2.4.1–2.4.13)**: Verify "Skip to main content" links, descriptive page titles, meaningful link text (no "click here"), visible focus indicators on every interactive element, and multiple ways to locate pages (search, sitemap, navigation). For single-page apps, confirm client-side focus management: focus moves to new content after navigation.

6. **Understandable — Readable and predictable (3.1.1–3.2.6)**: Confirm the page language is declared with the `lang` attribute and changes are marked inline. Verify that navigation and UI components are consistent across pages. Flag unexpected context changes — form submission, new window opening, or focus movement must be triggered by user action, not automatic.

7. **Understandable — Input assistance (3.3.1–3.3.9)**: Verify that all form errors are identified, described in text, and associated with the relevant field. Error suggestions must be provided where known. Confirm that forms requiring legal, financial, or data-deletion commitment are reversible, checked, or confirmed before final submission.

8. **Robust — Compatible (4.1.1–4.1.3)**: Verify valid, complete HTML with unique IDs and proper nesting. Confirm ARIA roles, states, and properties are used correctly — no orphan ARIA attributes, no `aria-hidden="true"` on focusable elements. For custom interactive components, verify they expose correct name, role, and value to assistive technology.

## Implementation Questions

Before finalizing design-to-code output, an agent should ask:
- Is the target WCAG conformance level A, AA, or AAA, and for which version (2.1 or 2.2)?
- Has the design been tested with screen readers (NVDA, VoiceOver, JAWS) and keyboard-only navigation?
- Are there custom interactive components (dropdowns, modals, tabs, date pickers, drag-and-drop) that need ARIA authoring?
- Does the client-side routing solution manage focus and announce page changes to assistive technology?
- Is there an automated accessibility testing step in CI (axe-core, Lighthouse, Pa11y) and manual testing cadence?

## Related Packs\n\n- **Government/FedRAMP**: Section 508 legally requires WCAG 2.0 AA for all US federal government-facing interfaces.\n- **GDPR**: Accessible consent mechanisms and privacy notices are required — inaccessible consent is not valid consent under GDPR.\n- **SOC 2**: Processing Integrity (PI-series) controls are undermined if users with disabilities cannot access or operate the system.\n\n## Final Review Rule

If this pack is relevant to the product domain, XD_SECURITY_ARCHITECT and XD_PRINCIPAL_ENGINEER must review the architecture before final output.

**Disclaimer**: This compliance pack identifies design and engineering obligations. It does not constitute a WCAG conformance claim, legal compliance determination, or accessibility certification. Conformance claims require evaluation by qualified accessibility professionals per W3C WCAG-EM methodology.