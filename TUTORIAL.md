# Quick Start Tutorial

Take a SaaS dashboard design from "looks good" to production-ready review in under 15 minutes.

## Prerequisites

- Python 3.10+
- An agent environment (Codex, Claude Code, Cursor, or OpenCode)
- This repo installed (see [INSTALL.md](INSTALL.md))

## 5-Minute Walkthrough: Audit an XD Dashboard

You have a SaaS admin dashboard artboard exported from XD. You want a design-quality check,
component inventory, and an architecture recommendation — not a code dump.

### 1. Describe a dashboard to the skill

Give your agent a prompt like this:

```
Load DMW Product Engineering OS. I have an Adobe XD SaaS admin dashboard
export with these artboards:

1. "Dashboard - Overview"  — key metrics: revenue chart, user growth KPI,
   recent activity feed, quick-action buttons.
2. "Dashboard - Users"     — searchable, filterable user table with bulk
   actions (activate, deactivate, delete) and export-to-CSV.
3. "Dashboard - Settings"  — user profile form, notification preferences,
   billing summary card, danger-zone account-deletion flow.

Target stack: Next.js, TypeScript, Tailwind CSS, shadcn/ui.
Run in Audit mode. Focus on accessibility gaps, component reuse,
and architecture fit. Give me a world-class gate score.
```

### 2. See the Design Critic in action

The agent first applies evidence labels across the agent roster:

```
Mandatory first pass — product category + user goals inferred:
  INFERRED: Internal operations dashboard (SaaS admin), primary user is
            a team lead managing 10-200 accounts.
  Missing: empty-state artboard, bulk-delete confirmation artboard,
           forgot-password flow, dark-mode variants.

XD_DESIGN_CRITIC:
  FAIL — DataTable lacks caption, scope attributes, and sort-announce live
         region. CONFIRMED: 5-column table, header row uses <th> but no
         scope="col". Keyboard order: tab skips filter → export button.
  FAIL — Quick-action buttons use color-only state (green="active",
         gray="disabled"). WCAG 2.2 requires non-color indicator.
  PASS WITH WARNINGS — Revenue chart tooltip values appear only on hover.
         No keyboard or touch equivalent for data points.

XD_ACCESSIBILITY_LEAD:
  FAIL (3 items) → cannot reach WCAG 2.2 AA without remediation.
  Blocking: DataTable missing semantic structure (caption, scope, sort
  announcement). Quick-actions have color-only affordance. Tooltip data
  is mouse-only.

XD_PRINCIPAL_ENGINEER:
  REVIEW — Architecture fits Next.js App Router with parallel routes for
  dashboard panels. Component extraction below threshold: 3 of 6 reuseable
  components detected (DataTable, FilterPanel, MetricCard). Missing:
  UserAvatar, StatusBadge, QuickActionGroup. Recommend extracting before
  implementation to avoid duplication across 3 artboard screens.

World-Class Gate scores:
  Design Quality:  85 (FAIL — contrast + table semantics)
  Accessibility:   78 (FAIL — 3 blocking issues)
  Architecture:    88 (PASS WITH WARNINGS — component extraction gap)
  Maintainability: 90 (PASS)
  Performance:     87 (PASS WITH WARNINGS — DataTable not paginated)
  Security:        90 (PASS)
  Testability:     91 (PASS)
  Documentation:   90 (PASS)

XD_COUNCIL verdict: REVISE. Accessibility < 95 blocks release.
Remediation plan attached.
```

### 3. Extract components and tokens

Switch to Extraction mode to inventory what you have:

```
Extract components and design tokens from the XD artboards. Emit
CONFIRMED/INFERRED labels for every item. Output as structured metadata.
```

The agent produces component metadata and a token hierarchy:

```json
{
  "components": [
    {
      "name": "FilterPanel",
      "evidence": "CONFIRMED — repeated on 'Users' and 'Overview' artboards with same layout",
      "industry": "Enterprise SaaS",
      "accessibility": ["labeled inputs", "aria-controls on filter triggers"],
      "states": ["collapsed", "expanded", "applied", "clear-pending"]
    },
    {
      "name": "BillingSummaryCard",
      "evidence": "CONFIRMED — artboard 'Settings', unique layout, single instance",
      "industry": "SaaS",
      "accessibility": ["semantic headings", "monetary values in <data>"],
      "states": ["active-plan", "trial-expiring", "past-due"]
    }
  ],
  "tokens": {
    "primitive": {
      "color.blue.700": "#1d4ed8",
      "space.4": "16px",
      "radius.md": "8px"
    },
    "semantic": {
      "color.surface.card": "#ffffff",
      "color.text.primary": "#0f172a",
      "color.text.muted": "#64748b",
      "color.action.destructive": "#dc2626",
      "color.feedback.success": "#16a34a"
    }
  }
}
```

### 4. Get an architecture recommendation

```
Given 3 artboard groups (Overview, Users, Settings), recommend an
architecture pattern. Justify the fit and state what was rejected.
```

The agent selects and justifies:

```
Architecture recommendation:
  Pattern: Feature-Sliced Design
  Grouping: features/dashboard-overview, features/user-management,
            features/settings
  Shared layer: shared/ui (DataTable, FilterPanel, MetricCard,
                StatusBadge, QuickActionGroup), shared/lib (exportCSV,
                formatCurrency)

  Why: 3 independent product domains with limited cross-feature coupling.
       Each feature owns its data-fetching, form logic, and routing.
       Shared primitives extracted from design tokens reduce duplication.

  Rejected alternatives:
    - Clean Architecture: added abstraction overhead without domain
      complexity to justify it (no business-logic layer needed).
    - Monolith pages/: would duplicate DataTable logic across 2 of 3
      artboard screens.
    - Micro-frontends: premature — single team, single deploy, no
      independent-ownership requirement.

  Output stack: Next.js App Router, React Server Components, TypeScript
                strict, Tailwind CSS (semantic tokens), shadcn/ui (base
                components), Zod (runtime validation).
```

## Next Steps

You now have a design critique, component inventory, tokens, and an architecture plan — all
without writing a line of implementation code.

- **Run a benchmark**: `python3 scripts/score_benchmarks.py` to see how the OS scores reference
  dashboards, ecommerce flows, healthcare screens, and more.
- **Read the failure library**: `knowledge/failures/` — each file captures a real failure
  pattern (pixel-copy-without-critique, unlabeled-inference, etc.) the OS is designed to prevent.
- **Study the agent roster**: `knowledge/agents/AGENT_ROSTER.md` — learn when to involve
  XD_DESIGN_CRITIC vs XD_EXECUTIVE_REVIEWER vs XD_SIMPLICITY_ADVOCATE.
- **Trigger benchmark intelligence**: `python3 scripts/benchmark_intelligence.py` to feed
  your project's lessons back into `knowledge/evolution/`.

## Taking It Further

- **Add your real XD files** to `benchmarks/01-dashboard-saas/design/` and re-run scoring.
- **Create a custom compliance pack** under `compliance/` if your domain has regulatory
  requirements beyond what ship (GDPR, HIPAA, SOC2, PCI-DSS, WCAG, ISO27001, PIPA, Gov).
- **Contribute a success pattern** to `knowledge/success-patterns/` after shipping a
  project that went from design critique → extraction → architecture → implementation.
- **Set up CI benchmark gates** using `.github/workflows/` so every PR must pass the
  world-class gate against reference designs.