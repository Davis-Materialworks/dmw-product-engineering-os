# Dashboard SaaS — Design Specification

## Product Context
B2B SaaS analytics dashboard for mid-market operations teams. Users monitor real-time KPIs, drill into metric trends, export filtered reports, and receive proactive alerts.

## User Goals
- Glance at business-critical KPIs on load (revenue, churn, active users, NPS)
- Filter by date range, team, segment, and geography
- Drill from summary cards to detailed trend charts
- Export reports as CSV/PDF with applied filters
- Acknowledge and triage system alerts in a notification drawer

## Color Palette
| Token | Hex | Usage |
|---|---|---|
| `surface.canvas` | `#F8FAFC` | Page background |
| `surface.sidebar` | `#1E293B` | Persistent left nav |
| `surface.card` | `#FFFFFF` | KPI cards, panels |
| `text.primary` | `#0F172A` | Headings, body copy |
| `text.secondary` | `#64748B` | Labels, metadata |
| `action.primary.bg` | `#2563EB` | Primary buttons, selected filters |
| `action.primary.hover` | `#1D4ED8` | Hover state |
| `feedback.success` | `#16A34A` | Positive trend, healthy status |
| `feedback.warning` | `#F59E0B` | Warning badges, thresholds |
| `feedback.danger` | `#DC2626` | Alert badges, negative trends |
| `focus.ring` | `#3B82F6` | Focus indicator (3px offset) |

## Typography Scale
| Token | Size / Line | Weight | Usage |
|---|---|---|---|
| `display.metric` | 32px / 1.1 | 700 | KPI values in MetricCard |
| `heading.section` | 18px / 1.3 | 600 | Section titles above charts/tables |
| `heading.page` | 24px / 1.3 | 700 | Page title in top bar |
| `body.default` | 14px / 1.5 | 400 | Table cells, descriptions |
| `label.table` | 12px / 1.4 | 500 | Column headers, filter labels |
| `caption.meta` | 11px / 1.4 | 400 | Timestamps, secondary metadata |
| Font family: Inter (headings + body), JetBrains Mono (metric values) |

## Component Inventory
- **AppShell** — Persistent sidebar (dark bg) + top command bar + scrollable content area
- **MetricCard** — KPI value, label, trend indicator (arrow + percentage), sparkline thumbnail
- **DataTable** — Sortable columns, row hover, status badges, bulk-select, pagination (20 rows default)
- **FilterPanel** — Horizontal filter bar below top nav; date picker, segment dropdown, saved filter presets
- **ExportAction** — Dropdown button (CSV / PDF), triggers download with current filters
- **NotificationDrawer** — Slide-in panel from right; unread count badge, per-item dismiss, "mark all read"
- **SkeletonLoader** — Shimmer placeholders for MetricCards and table rows during data fetch

## Layout Structure
```
┌──────────────────────────────────────────┐
│ SIDEBAR (240px)  │  TOP COMMAND BAR      │
│ - Nav items      │───────────────────────│
│ - User avatar    │  FILTER BAR           │
│ - Collapse btn   │───────────────────────│
│                  │  KPI CARD GRID (4col) │
│                  │───────────────────────│
│                  │  2-COL CONTENT        │
│                  │  [Chart] [Table]      │
└──────────────────────────────────────────┘
```

## Responsive Behavior
- **1440px+**: Sidebar visible, 4-column KPI grid, 2-column chart+table
- **1024–1439px**: Sidebar collapsible (hamburger toggle), 3-column KPI grid, stacked chart+table
- **768–1023px**: Sidebar hidden by default (overlay on toggle), 2-column KPI grid
- **<768px**: Single column, KPI cards stack vertically, table becomes horizontal-scroll card list

## State Descriptions
- **Loading**: Skeleton shimmer on MetricCards and table rows; filter bar disabled
- **Empty**: Illustrated empty state with guidance text ("No data for selected filters")
- **Error**: Toast notification (top-right), inline error banner with retry button, partial data shown if available
- **Data-loaded**: Cards animate in (fade-up stagger), table populates, filters become interactive

## Accessibility Requirements
- WCAG 2.2 AA compliance throughout
- Sidebar: `<nav>` landmark with `aria-label="Main navigation"` and visible skip link
- MetricCards: trend indicators include both color AND directional icon/text (not color-only)
- DataTable: `<caption>`, `<thead>` scoped headers, `aria-sort` on sortable columns, sort announcements via live region
- NotificationDrawer: `<dialog>` semantics, focus trap, Escape closes, focus returns to trigger button
- All interactive elements: visible focus ring (3px, 2px offset), minimum 44×44px touch targets
- Charts: text summaries + data-table fallback for screen readers