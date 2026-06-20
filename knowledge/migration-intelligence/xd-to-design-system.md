# XD-TO-DESIGN-SYSTEM Migration Playbook

## Purpose
Map XD components, styles, assets, and states into governed tokens, component specs, documentation, contribution rules, and migration guidance.

## Common Pitfalls
- **Token flattening**: XD color swatches, character styles, and component states get extracted as flat lists, losing the semantic relationships (e.g., "Primary action" vs. "Destructive action" vs. "Disabled"). Every token must carry a usage rule, not just a value.
- **Design-code drift**: Exporting tokens once and never again means the design system package diverges from XD within weeks. Automate token extraction or enforce a sync schedule.
- **Over-specification**: Copying every XD property into a design token creates an unmaintainable token tree. Cards don't need `card-padding-top` — they need `spacing-md` with a component-level spec.
- **Missing state documentation**: XD components may only show default state. The design system must document loading, empty, error, disabled, focused, pressed, and expanded states for every interactive component.
- **Version coupling**: Tying the design system version to the XD file version creates a false dependency. Design system versions should be independent, with a compatibility matrix.
- **Asset format fragmentation**: XD exports to PNG/SVG, but design systems need multiple formats: SVG for web, PDF for iOS, XML vector drawable for Android, and a raster fallback for each density.

## Token Translation Rules
| XD Source | Design Token | Notes |
|-----------|-------------|-------|
| Color Swatch | `--color-{semantic}-{variant}` | Layer semantics: `primary`, `secondary`, `danger`, `success`, `warning`, `info` with variants `-hover`, `-active`, `-disabled`, `-bg` |
| Character Style | `--font-{role}-{property}` | `--font-heading-1-size`, `--font-heading-1-weight`, `--font-body-size`, `--font-caption-size` |
| Spacing grid | `--spacing-{scale}` | XD 8px grid → `--spacing-2` (8px), `--spacing-4` (16px), `--spacing-6` (24px), `--spacing-8` (32px) |
| Border Radius | `--radius-{size}` | `--radius-sm` (4px), `--radius-md` (8px), `--radius-lg` (12px), `--radius-pill` (999px) |
| Shadow | `--shadow-{elevation}` | `--shadow-low`, `--shadow-medium`, `--shadow-high`; document blur, offset, color for each |
| Breakpoint | `--breakpoint-{size}` | `--breakpoint-sm` (640px), `--breakpoint-md` (768px), `--breakpoint-lg` (1024px), `--breakpoint-xl` (1280px) |
| Duration (animation) | `--duration-{speed}` | `--duration-fast` (150ms), `--duration-normal` (300ms), `--duration-slow` (500ms) |
| Easing | `--ease-{type}` | `--ease-in`, `--ease-out`, `--ease-in-out`; export cubic-bezier values |

## Component Mapping Guidelines
- **XD Component (Master)** → Component specification with name, description, variants, states, anatomy diagram, and usage do's/don'ts
- **XD Component States** → State matrix: [default, hover, active, focus, disabled, loading, empty, error] × [responsive breakpoints]
- **XD Character Style** → Typography token group with font family, size, weight, line height, letter spacing, and text transform
- **XD Color Swatch group** → Semantic color token group with base, hover, active, disabled, and contrast-ratio-checked variants
- **XD Asset export** → Multi-format asset pipeline: SVG (web), PDF (iOS), XML vector (Android), PNG@1x/2x/3x (fallback)
- **XD Repeat Grid with components** → Component list specification with item, empty state, loading skeleton, and error state

## Migration Checklist
1. [ ] Inventory all XD colors, character styles, and reusable components; deduplicate near-identical values
2. [ ] Define semantic naming: map all raw XD values to purpose-based tokens (e.g., `#FF0000` → `--color-danger-500`)
3. [ ] Audit every component for missing states: add loading, empty, error, disabled, focused, pressed for each
4. [ ] Generate platform-specific token files: CSS custom properties, Tailwind config, SwiftUI Color extensions, Flutter ThemeData
5. [ ] Create component specification template: name, anatomy, variants, states, accessibility, usage, code examples
6. [ ] Define contribution workflow: who owns tokens? how are changes proposed and reviewed? when does a token graduate from experimental to stable?
7. [ ] Set up automated token extraction (XD plugin → JSON → token transformer → platform files)
8. [ ] Document versioning policy: MAJOR for breaking token renames, MINOR for new components/tokens, PATCH for fixes
9. [ ] Build a Storybook or equivalent component gallery with live rendering of every component in every state
10. [ ] Define sunset/deprecation policy: how are old tokens removed without breaking consumers?

## Verification Checklist
- [ ] All semantic tokens pass WCAG AA contrast ratio (4.5:1 for text, 3:1 for large text and UI components)
- [ ] Token JSON exports are valid and parseable by all target platform transformers
- [ ] Component specs include accessibility annotations (ARIA roles for web, accessibilityLabel for mobile)
- [ ] Storybook/Gallery renders every component variant (not just default state)
- [ ] Version compatibility matrix exists and is up to date
- [ ] Contribution guide is published and reviewed by both design and engineering leads