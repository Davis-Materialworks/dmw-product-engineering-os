# Peak-End Rule

## Principle
Users judge experiences not by the sum or average of all moments, but disproportionately by the most intense emotional moment (the peak) and the final moment (the end). A largely positive experience with a frustrating peak or disappointing ending will be remembered negatively; a mediocre experience with a delightful peak and satisfying ending may be remembered fondly.

## How to Detect Violations in XD Artboards
- **Audit the "end" of every flow**: What is the last screen the user sees after completing a core task (signing up, checking out, submitting a form)? If it is a generic "Success" message or, worse, a redirect with no acknowledgment, the ending is weak. Every flow-ending artboard is a high-leverage design surface.
- **Identify emotional peaks**: Map the emotional curve of the user journey. Where is the user most frustrated? Most delighted? If there are no deliberate positive peaks, the experience will be remembered as flat or negative regardless of baseline quality.
- **Check error recovery**: The most common negative peak is an error state. If the XD artboard shows a generic error message with no recovery path, this single screen may dominate the user's memory of the entire product.
- **Audit loading states**: Long waits (Doherty Threshold violations) create negative peaks. If the XD shows no loading skeleton, progress indicator, or entertaining interstitial, the wait becomes a memory-defining negative peak.

## Concrete XD-to-Code Examples
1. **E-commerce checkout ending on "Order #12345 confirmed"**: The XD flow ends with a plain confirmation page. Add a micro-celebration (confetti animation), a "What's next?" timeline showing delivery stages, and a one-tap "Add to calendar" for the delivery date. Code consequence: lightweight Lottie animation, semantic timeline component, calendar URL generation.
2. **Signup flow with a lengthy form and no reward**: The XD shows a 6-field signup form ending at the dashboard. The peak is the frustration of filling the form; the end is anti-climactic. Add a progressive onboarding wizard with completion celebration at step 3 (the peak) and a personalized welcome page at the end. Code consequence: multi-step form with `framer-motion` transitions, completion badge component.
3. **Error state with "Something went wrong"**: The XD artboard shows a generic error page with no recovery action. This will be the user's most intense memory. Add specific error diagnosis ("Your payment method was declined — try another card"), a one-click retry, and a human tone. Code consequence: typed error responses with actionable recovery buttons, error categorization by recoverability.

## When to Invoke the Peak-End Rule in a Design Critique
- During flow review — especially the last 2-3 screens of every critical user journey
- Before shipping any error state or empty state
- During onboarding redesign — the first-run experience creates the initial "peak"
- When prioritizing UX improvements — fixing a single peak pain point may improve user satisfaction more than fixing five minor annoyances

## Common False Positives
- **Utility tools with no emotional dimension**: A currency converter or calculator has no emotional peaks by design. Users judge these purely on efficiency and accuracy. Forcing delight onto a utility tool feels jarring. The Peak-End Rule applies to experiences with an emotional component — not pure tools.
- **Negative peaks that are outside the product's control**: A delivery delay creates a negative peak, but the e-commerce platform did not cause it. The Peak-End Rule should inform recovery communication, not be blamed for external events. Focus on what the product can control: apology, transparency, and compensation.
- **Over-celebrating trivial actions**: "You clicked a button! Confetti!" creates a positive peak that feels manipulative and cheapens real achievements. Reserve peaks for meaningful milestones: completing onboarding, first successful transaction, reaching a goal.