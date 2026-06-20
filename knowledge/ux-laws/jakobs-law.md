# Jakob's Law

## Principle
Users spend most of their time on other websites and apps. They bring expectations from those experiences to yours. When your product behaves like everything else they use, they can transfer existing knowledge — reducing learning time and cognitive load. Violating these expectations requires a clear, defensible benefit that outweighs the friction.

## How to Detect Violations in XD Artboards
- **Check navigation position**: If the primary navigation is not at the top (desktop) or bottom (mobile), users will spend extra seconds locating it. The XD prototype should match the platform convention unless there is a documented user research justification.
- **Audit link/button differentiation**: If XD text layers that function as links are not underlined or colored distinctly from body text, users will not know they are interactive. Check every artboard for unlabeled, unstyled interactive elements.
- **Verify icon semantics**: If the XD uses a gear icon for "profile" or a magnifying glass for "zoom" (not search), users will misclick. Every icon must match its industry-standard meaning.
- **Check form patterns**: If the submit button is above the form fields (violating top-to-bottom reading order) or the password field lacks a show/hide toggle, users will stumble.
- **Audit scroll behavior**: If the XD prototype simulates horizontal scroll for content that convention says should scroll vertically (or vice versa), users will miss content.

## Concrete XD-to-Code Examples
1. **Center-aligned nav on a SaaS dashboard**: The XD artboard places the main navigation in a center-positioned floating panel. Every major SaaS product (GitHub, Linear, Stripe, Vercel) uses left sidebar or top nav. Users arrive expecting left/top navigation — the center panel delays task completion by 3-5 seconds while they visually search. Code consequence: restructure as left sidebar with collapsible sections.
2. **Underlined non-link text**: The XD design underlines section titles for visual hierarchy. Users interpret underlines as links (web convention since 1995). Use bold weight, color, or size for hierarchy instead. Code consequence: replace `text-decoration: underline` with `font-weight: 600` on heading elements.
3. **Custom scrollbar with non-standard behavior**: The XD prototype shows a styled scrollbar that does not match the OS scrollbar position or behavior. Users lose the ability to click the scrollbar track to jump or use muscle memory for scrollbar position. Code consequence: remove custom scrollbar CSS; use native scrollbar or, if branding requires it, maintain standard behavior (clickable track, draggable thumb, visible on hover).

## When to Invoke Jakob's Law in a Design Critique
- When a designer proposes a novel navigation pattern — ask: "What user research justifies breaking the convention?"
- During competitive audit — if competitors all use pattern X and the design uses pattern Y, flag it
- Before building custom UI components that have well-known native equivalents (date pickers, selects, toasts)
- On onboarding artboards — new users rely most heavily on convention

## Common False Positives
- **Innovation with measured benefit**: If usability testing shows that a novel pattern improves task completion by 30%+ and the learning curve is <2 uses, the violation is justified. Jakob's Law does not ban innovation — it demands evidence.
- **Platform-specific conventions**: What violates Jakob's Law on iOS may be standard on Android. A "Back" button in the top-left is expected on iOS but wrong on Android (where the system back gesture handles it). Always check platform, not just the web.
- **Domain-specific tools**: A DAW (digital audio workstation) or video editor has conventions that look alien to web users but are standard for that domain's user base. Jakob's Law applies to the user's *actual* prior experience, not generic web conventions.