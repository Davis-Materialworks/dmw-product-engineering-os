# Dashboard Pattern

## Recognition Signals
- KPI
- chart
- summary
- trend
- recent activity
- health

## Expected Components
- DashboardShell
- MetricCard
- ChartPanel
- ActivityFeed
- DataTable

## Component Metadata Schema Example
```json
{
  "component": "DashboardShell",
  "industry": "Pattern-dependent",
  "accessibility": [
    "chart summaries",
    "data alternatives",
    "not color-only",
    "landmarks"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "loading",
    "empty data",
    "filter changes",
    "chart summary"
  ]
}
```

## Accessibility Obligations
- chart summaries
- data alternatives
- not color-only
- landmarks

## Testing Obligations
- loading
- empty data
- filter changes
- chart summary

## Critic Guidance
Challenge vanity metrics, unclear hierarchy, and dashboards with no action path.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
