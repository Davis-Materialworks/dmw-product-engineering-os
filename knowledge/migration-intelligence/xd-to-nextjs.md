# XD-TO-NEXTJS Migration Playbook

## Purpose
Map XD artboards to App Router routes, layouts, server/client boundaries, typed components, Tailwind tokens, visual regression, and accessibility checks.

## Common Pitfalls
- **Server/Client boundary confusion**: XD artboards showing dynamic behavior (hover, focus, real-time updates) get migrated into Server Components, losing interactivity. Always audit interaction states before choosing `"use client"`.
- **Layout cascade mismatch**: XD artboard groups become nested Layout components, but Next.js Layouts do not remount on navigation — state preservation assumptions from XD prototypes silently fail.
- **Token drift during Tailwind migration**: XD fill colors map to hex values, but Tailwind's `bg-red-500` is shade 500 of red, not a precise hex match. Unmatched colors silently degrade brand consistency.
- **Image optimization assumptions**: XD artboards export at 2x/3x resolution, but `next/image` requires explicit `width`/`height` or `fill` — omitted dimensions cause Cumulative Layout Shift (CLS).
- **Font loading flash**: Custom fonts specified in XD cause FOUT/FOIT unless declared in `next/font` with proper `display` strategy and subset configuration.

## Token Translation Rules
| XD Source | Tailwind Token | Notes |
|-----------|---------------|-------|
| Fill color (hex) | `bg-{color}-{shade}` | Match to nearest Tailwind shade; if >2% ΔE from brand, use `tailwind.config.ts` custom color |
| Text color (hex) | `text-{color}-{shade}` | Same shade-matching rule; dark mode variants need explicit `dark:` prefix |
| Drop shadow (XD) | `shadow-{size}` | XD blur → Tailwind shadow-sm/md/lg/xl; XD spread → ring-width |
| Border radius (px) | `rounded-{size}` | Map ≤4px→`sm`, 6px→`md`, 8px→`lg`, 12px→`xl`, 16px→`2xl`, full→`full` |
| Spacing (px) | `p-{n}`, `m-{n}`, `gap-{n}` | Divide by 4 (Tailwind's base unit); 16px → `p-4` |
| Font size (pt/px) | `text-{size}` | `xs`(12), `sm`(14), `base`(16), `lg`(18), `xl`(20), `2xl`(24), etc. |
| Line height | `leading-{n}` | Relative: 1.0→`none`, 1.25→`tight`, 1.5→`normal`, 1.75→`relaxed`, 2.0→`loose` |
| Opacity | `opacity-{n}` | XD 0-100% → Tailwind 0-100 (0, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 100) |

## Component Mapping Guidelines
- **XD Repeat Grid** → Server Component with `Array.map()` if static; Client Component with virtualized list if >50 items
- **XD Component (Master)** → TypeScript interface + reusable component with `Props` type; master→instance overrides become prop defaults + spread
- **XD Artboard Group** → Layout component (`layout.tsx`) if shared across routes; wrapper component if page-specific
- **XD Hover State** → CSS `hover:` variants in Tailwind for simple transitions; `useState`/`onMouseEnter` for complex interactive state
- **XD Auto-Animate** → Framer Motion `AnimatePresence` for enter/exit; CSS transitions for simple property changes
- **XD Overlay/Modal** → Parallel route (`@modal`) or `dialog` element with `useEffect` for body scroll lock

## Migration Checklist
1. [ ] Audit every XD artboard for interaction states (hover, focus, active, disabled, loading, empty, error)
2. [ ] Classify each component as Server (no interactivity) or Client (`"use client"`)
3. [ ] Extract XD colors and match to Tailwind shades; document custom colors required
4. [ ] Map XD typography styles to Tailwind `fontFamily` config and `text-{size}` classes
5. [ ] Export XD assets at 2x resolution; place in `public/` or import into component files
6. [ ] Define route structure from XD artboard navigation: `/dashboard`, `/dashboard/settings`, etc.
7. [ ] Build shared Layout components from XD artboard groups used across screens
8. [ ] Implement responsive variants for each XD artboard width (mobile/tablet/desktop)
9. [ ] Add `loading.tsx` skeletons for routes with data-fetching artboards
10. [ ] Add `error.tsx` boundaries for routes that display error states in XD
11. [ ] Configure `next/font` for every custom font in XD with `subsets` and `display: 'swap'`

## Verification Checklist
- [ ] `npm run build` passes with zero errors
- [ ] Lighthouse Accessibility score ≥ 95 (test every route)
- [ ] Percy/Chromatic visual diff approved for all breakpoints (mobile, tablet, desktop)
- [ ] `next/image` warnings resolved — no missing width/height on any `<Image>`
- [ ] Keyboard navigation path matches XD interaction flow
- [ ] Screen reader announces dynamic content changes (route changes, form errors, loading states)
- [ ] Dark mode variants render correctly if XD specifies them
- [ ] `npm run lint` passes (ESLint + prettier)