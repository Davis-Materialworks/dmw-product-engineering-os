# 2026-06-20 Responsive Strategy

## Decisions Made

### Breakpoint Taxonomy
Adopted a 5-breakpoint system based on device class, not pixel widths alone: `base` (<640px, phones), `sm` (640-768px, large phones and small tablets), `md` (768-1024px, tablets and small laptops), `lg` (1024-1280px, desktops), `xl` (>1280px, large displays). Breakpoint names are purpose-agnostic — they describe screen width, not device intent. This prevents the anti-pattern of naming breakpoints `tablet` and then discovering the tablet breakpoint also applies to split-screen desktop windows.

### Mobile-First vs. Desktop-First Default
Chose mobile-first as the default authoring strategy. All components render the mobile (`base`) layout by default and add complexity at wider breakpoints via `min-width` media queries (or framework equivalents: `sm:`, `md:`, `lg:`, `xl:`). Rationale: mobile-first forces designers and engineers to prioritize content hierarchy. If it doesn't fit on a phone, maybe it shouldn't exist. Desktop-first leads to "just hide it on mobile" which accumulates dead markup and degraded mobile performance.

### XD Artboard Width Detection
XD artboards must be labeled by width or the system will issue a warning. Standard widths map naturally: 375-414px → `base`, 768px → `md`, 1024px → `lg`, 1440px → `xl`. An artboard at 390px is a `base` layout with an inferred iPhone 14/15 target. An artboard at 834px is ambiguous (iPad portrait or small laptop) — these receive an INFERRED label and a review prompt.

### Multi-Artboard Responsive Strategy
When XD provides multiple artboards for the same screen at different widths, the system must:
1. Identify which artboard is the mobile layout (smallest width)
2. Map layout differences between breakpoints as explicit responsive rules: "At `md`, the sidebar becomes visible. At `lg`, the data table gains 3 additional columns."
3. Flag artboards with identical layouts at multiple sizes as wasted design effort — the design is responsive by scaling, not by adaptive layout
4. Flag artboards with completely different layouts at different sizes as potential user confusion — the same screen should not look like two different products

## Implementation Patterns Discovered

### Container Queries for Component-Level Responsiveness
Standard media queries respond to viewport width, but components embedded in different containers (sidebar, main content, modal) need their own breakpoints. When an XD artboard shows a component at different widths within the same viewport (e.g., a card in a 3-column grid vs. a card in a 2-column sidebar), use container queries. Code pattern: `@container (min-width: 400px)` for the card component, not `@media (min-width: 768px)`.

### The "First Meaningful Paint at Base" Rule
Every screen must render a complete, usable layout at the `base` breakpoint. Progressive enhancement at wider breakpoints is acceptable; graceful degradation from desktop is not. This means: no component that is essential to task completion should be hidden at mobile widths. If the XD shows a desktop chart that becomes a summary stat on mobile, the summary stat must communicate the same decision — not just "less data."

### Responsive Typography Strategy
XD artboard text sizes should not be taken literally at every breakpoint. A 56px headline on a 1440px artboard should scale down to 32-36px on a 375px screen using a modular scale — not fluid scaling (which produces unreadable text at extremes) and not fixed pixels (which wastes screen space). Pattern: define `--font-heading-1` as `clamp(2rem, 1rem + 3vw, 3.5rem)` with explicit min/max bounds.

## What We Learned
1. **Responsive design is a migration intelligence dimension**: Every migration playbook needed a "responsive strategy" section. The XD-to-NextJS playbook documents Tailwind breakpoints; the XD-to-Flutter playbook documents `LayoutBuilder` and `MediaQuery`; the XD-to-SwiftUI playbook documents `sizeClass` and `ViewThatFits`.
2. **XD artboard ordering matters**: The order of artboards in the XD file implies priority. The first artboard is the primary design — responsive variants are secondary. But the responsive module must reverse this: mobile is primary, desktop is enhanced.
3. **Testing responsive layouts requires tooling, not just resizing**: Visual regression tools (Percy, Chromatic) must capture every breakpoint as a separate snapshot. Manual "resize the browser window" testing misses edge cases and is not reproducible.

## Prevention Rules Added
1. All components must render correctly at `base` before any wider-breakpoint work begins
2. XD artboards must carry width labels or the migration system issues a warning
3. Container queries are preferred over media queries for reusable components
4. Every migration playbook must include a responsive strategy section specific to the target framework