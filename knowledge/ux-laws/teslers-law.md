# Tesler's Law (Law of Conservation of Complexity)

## Principle
Every system has an irreducible minimum of complexity. This complexity cannot be eliminated — it can only be shifted. The design question is: who bears the complexity — the user or the system (and by extension, the engineers)? Good design absorbs complexity so the user does not have to.

## How to Detect Violations in XD Artboards
- **Count user decisions required to complete a task**: If the XD flow requires the user to make 8+ explicit choices to complete a core task (e.g., checkout, signup, creating a project), complexity has likely been pushed to the user.
- **Audit default values**: Empty form fields, unselected dropdowns, and unchecked toggles that could have sensible defaults represent complexity shifted onto the user. Every field without a default should have a justification.
- **Check for manual configuration where automation exists**: If the XD artboard asks the user to enter their country AND their currency AND their timezone, the system is pushing complexity that could be inferred from country alone (or from the browser/device).
- **Look for explanation text alongside UI**: If an XD artboard needs paragraphs of helper text to explain a feature, the feature itself is too complex and the explanation is a band-aid. The complexity should be designed out, not documented around.

## Concrete XD-to-Code Examples
1. **Checkout with 5 separate address forms**: The XD flow shows separate forms for shipping address, billing address, contact info, payment method, and delivery preferences. Reduce complexity: "Same as shipping" toggle for billing address, auto-detect card type from number, remember address from account. Code consequence: `useMemo` for derived fields, `localStorage` for remembered preferences, card type regex detection.
2. **Dashboard requiring manual date range selection every visit**: The XD artboard defaults to an empty date picker. Pre-fill "Last 30 days" and save the user's last selection. The user bears the complexity of remembering what range they chose last time. Code consequence: persist `dateRange` to `localStorage` or URL params; default to `last30Days` on first visit.
3. **Filter system with 12 independent dropdowns**: The XD shows a filter bar with 12 dropdowns that must all be set manually. Intelligent defaults: infer "My Projects" if the user has a team, pre-select "Active" status, hide filters with zero matching results. Code consequence: `useMemo` to compute which filters have non-zero result counts, conditional rendering of irrelevant filters.

## When to Invoke Tesler's Law in a Design Critique
- When a feature spec includes a user flow with many sequential decisions — ask "which of these can we decide for the user?"
- During form design review — challenge every empty field
- When someone proposes "let the user configure it" as a solution — Tesler's Law says that's pushing complexity to the user
- On settings pages — every setting is complexity the user must manage; fewer settings is better

## Common False Positives
- **Legal/compliance requirements**: A GDPR consent form with required checkboxes pushes complexity to the user, but the law mandates it. The irreducible complexity here is external. Focus on making the mandatory steps as simple as possible.
- **Creative tools**: A photo editor with 50 filters exposes complexity deliberately — users of creative tools want control, not simplification. The complexity is the product. Tesler's Law applies to productivity and transactional interfaces, not creative expression tools.
- **Expert configuration**: A CI/CD pipeline configuration interface is inherently complex because the domain is complex. Simplifying the interface to hide complexity would prevent experts from doing their jobs. In this case, the user willingly accepts complexity in exchange for power — this is a valid design tradeoff, not a violation.