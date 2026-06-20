# Doherty Threshold

## Principle
Productivity soars when a computer and its user interact at a pace (<400ms) that ensures neither has to wait on the other. When system response time drops below 400ms, the user's attention remains uninterrupted and they can maintain flow state. Above 400ms, attention breaks, context switches begin, and productivity degrades rapidly. At 1 second, the user notices the delay. At 10 seconds, they leave.

## How to Detect Violations in XD Artboards
- **Identify interactions that imply server round-trips**: Any XD tap/click that triggers a data fetch, search, filter, save, or navigation is a Doherty threshold risk. If the XD prototype shows an instant result but the real implementation requires network latency, the design is misleading.
- **Audit loading indicators**: If the XD artboard shows a spinner with no skeleton or progress state, the design expects the user to wait passively — a Doherty threshold violation that breaks flow. Skeleton screens, optimistic UI, and progress bars are defenses.
- **Check for synchronous blocking in the intended UX**: Does the XD show a modal that must be dismissed before the user can continue? Is there a "Processing..." overlay that blocks all interaction? These are architectural decisions visible in the prototype.
- **Look for search-as-you-type vs. search-on-submit**: If the XD artboard shows a search box but the intended behavior is a full page reload on submit (not instant filtering), the threshold is violated for every search. The user expects milliseconds, gets seconds.

## Concrete XD-to-Code Examples
1. **Dashboard with full-page reload on filter change**: The XD artboard shows a filter bar above a data table. The intended behavior is a page reload to fetch filtered data (2-3 seconds). Violation: every filter change breaks flow. Solution: client-side filter the visible dataset, then fetch in background with skeleton rows. Code consequence: `useOptimistic` for instant UI feedback, `React.Suspense` with skeleton fallback for background refresh.
2. **Save button with no feedback until server response**: The XD shows a "Save" button that leads to a "Saved!" confirmation screen. The 2-second gap between click and confirmation exceeds the threshold. Solution: instantly show "Saving..." on the button, then transition to checkmark on success. Code consequence: `useTransition` from React 19 or `useOptimistic` for immediate state update, rollback on error.
3. **Search results appearing after 3-second API call**: The XD prototype shows results appearing instantly after typing. Real implementation: debounced API call with 300-500ms network latency. Solution: show skeleton results immediately on keystroke, replace with real data when it arrives. Code consequence: `useDeferredValue` for input, `Suspense` with `SkeletonCard` list for results area.

## When to Invoke the Doherty Threshold in a Design Critique
- During architecture review — when the proposed data-fetching strategy introduces visible latency
- Before approving any UX that shows a raw spinner — spinners are a design admission that the threshold is violated
- When a stakeholder proposes a feature that requires chained API calls (fetch A, wait, fetch B, wait)
- During mobile design review — mobile networks increase latency, making the threshold harder to meet

## Common False Positives
- **Deliberately slow interactions**: A file upload progress bar at 5% per second is truthful and useful — the user understands why it is slow and can plan around it. The violation is not the slowness but the lack of feedback. Presence of a meaningful progress indicator transforms the wait from a break in flow to a background process.
- **Batch operations**: A "Generate monthly report" action that takes 10 seconds is acceptable if it is an infrequent, high-value operation. The Doherty Threshold applies to frequent, in-flow interactions — not occasional heavy operations. The test: does the user encounter this delay more than 3 times per session?
- **Offline-first systems**: An app that works fully offline and syncs in the background has zero perceived latency for user interactions. The sync happening in the background may take 30 seconds, but the user never waits. This is a Doherty Threshold *solution*, not a violation.