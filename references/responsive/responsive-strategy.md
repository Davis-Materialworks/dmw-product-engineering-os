# Responsive Design Strategy

Infer responsive behavior from XD artboard families and content requirements. Never assume a single artboard width represents the full experience.

## Strategy Decision

Determine the design's intent before choosing a responsive approach:

| Signal | Strategy |
|--------|----------|
| XD artboards sorted desktop-first, mobile is sparse | Desktop-first with progressive degradation |
| XD artboards sorted mobile-first, content-first | Mobile-first with progressive enhancement |
| Artboards share layout patterns across widths | Fluid with container queries — fewer explicit breakpoints |
| Artboards differ substantially per width | Explicit breakpoints with layout-switching components |
| Single artboard only | Infer responsive model from content type and industry |

When uncertain, default to mobile-first. It forces content prioritization and catches over-design early.

## Breakpoint System

Do not generate arbitrary breakpoints. Derive them from artboard widths, content breakage points, and device landscape:

```
Base: Tailwind defaults unless artboards dictate otherwise
  sm: 640px   (derived from XD mobile artboard max)
  md: 768px   (derived from XD tablet artboard)
  lg: 1024px  (derived from XD desktop artboard)
  xl: 1280px  (derived from XD wide artboard)
  2xl: 1536px (max content width for dense layouts)
```

If only one artboard exists, propose these breakpoints and document the assumption. Map XD responsive resize and constraints to CSS behavior — preserve spatial relationships but accommodate real content and dynamic data.

## Container Queries vs. Media Queries

| Use media queries when | Use container queries when |
|------------------------|---------------------------|
| Page-level layout (header, sidebar, footer) | Component-level adaptation |
| Global navigation changes | Card grids that reflow independently |
| Font-size scaling across the document | A component reused in narrow and wide containers |
| Feature toggling (show/hide major sections) | Dashboard widgets, modals, data tables |

Prefer container queries for reusable components. Media queries remain correct for page-shell layout.

## Responsive Typography

Use `clamp()` for fluid type scales. Derive min/max from XD character styles at smallest and largest artboards:

```css
/* Fluid type scale derived from XD character styles */
--text-body: clamp(0.875rem, 0.8rem + 0.25vw, 1rem);       /* 14px → 16px */
--text-h1:   clamp(1.5rem, 1.2rem + 1vw, 2.5rem);           /* 24px → 40px */
--text-h2:   clamp(1.25rem, 1.05rem + 0.75vw, 2rem);        /* 20px → 32px */
--text-h3:   clamp(1.125rem, 1rem + 0.5vw, 1.5rem);         /* 18px → 24px */
```

Line-height should increase at smaller viewports (1.4 for mobile, 1.5 for body). Heading line-height stays tight (1.1–1.2) regardless of viewport.

## Responsive Images

Every image must declare responsive behavior:

- **Hero/banner images**: `srcset` with 3-4 breakpoint densities, `sizes` attribute for layout-aware selection
- **Content images**: `loading="lazy"` below the fold, explicit width/height to prevent CLS
- **Icons and illustrations**: SVG with `viewBox`, avoid raster for scalable assets
- **Product/thumbnail grids**: `srcset` with `sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"`

Never serve desktop-resolution images to mobile viewports. Generate responsive image pipelines from XD export sizes.

## Responsive Component Patterns

Map common XD layout patterns to responsive implementations:

| XD Pattern | Mobile (< 768px) | Tablet (768–1023px) | Desktop (1024px+) |
|------------|------------------|---------------------|-------------------|
| Multi-column card grid | Single column, full-width cards | 2-column grid | 3–4 column grid |
| Data table | Card stack with labels | Horizontal scroll or 2-column | Full table with all columns |
| Sidebar + content | Drawer or push-below | Collapsible sidebar | Persistent sidebar |
| Horizontal nav | Hamburger menu | Condensed tabs | Full horizontal nav |
| Hero + feature grid | Stacked, hero reduced | 2-column features | Full layout |
| Form | Single column, full-width inputs | 2-column for short fields | Multi-column where logical |
| Dashboard widgets | Stacked, priority-ordered | 2-column masonry | Full grid |

Every component must declare its responsive behavior. "It works on mobile" is not a responsive strategy — describe how it adapts.

## XD Artboard-to-Responsive Mapping

1. **Identify artboard families**: Group artboards by shared content (same screen at multiple widths). If ungrouped, infer families from naming conventions and content overlap.
2. **Extract layout intent**: Note grid columns, spacing ratios, and content priority at each width.
3. **Identify breakage points**: Where does the XD layout stop working at intermediate widths? These are your breakpoints.
4. **Map constraints to CSS**: XD responsive resize (fixed, responsive width/height, constraints) translates to CSS layout properties.
5. **Fill the gaps**: XD artboards are snapshots. Generate the intermediate states and edge cases (350px phone, 1200px laptop, 2000px monitor).

## Responsive Testing Checklist

Before shipping, verify at these minimum viewport widths:

- 320px (small phone)
- 375px (iPhone)
- 414px (large phone)
- 768px (tablet portrait)
- 1024px (tablet landscape / small laptop)
- 1280px (standard desktop)
- 1440px (large desktop)
- 1920px (wide monitor)

At each width, check:
- [ ] No horizontal scroll at any width
- [ ] Text remains readable (no truncation, overflow, or microscopic type)
- [ ] Touch targets >= 44x44px at mobile widths
- [ ] Images scale correctly without distortion
- [ ] Navigation is reachable and operable
- [ ] Forms are usable with on-screen keyboard visible
- [ ] No content is hidden without an accessible way to reach it
- [ ] Modals, dropdowns, and overlays remain usable
- [ ] `prefers-reduced-motion` is respected at all widths

## Performance by Viewport

Mobile is not just a smaller desktop. Enforce:

- **Below 768px**: No autoplaying video, defer non-critical scripts, minimize font loading
- **Below 1024px**: Conditionally load heavy components (data tables, charts) if off-screen
- **All widths**: Lazy-load below-the-fold content, use `content-visibility: auto` for long scroll containers