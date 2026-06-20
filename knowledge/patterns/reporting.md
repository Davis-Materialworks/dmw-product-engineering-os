# Reporting Pattern

## Recognition Signals
- report
- export
- date range
- schedule
- CSV
- PDF

## Expected Components
- ReportBuilder
- DateRangePicker
- ExportMenu
- ScheduledReportDialog

## Component Metadata Schema Example
```json
{
  "component": "ReportBuilder",
  "industry": "Pattern-dependent",
  "accessibility": [
    "date labels",
    "export status",
    "table semantics",
    "progress feedback"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "date range",
    "export permission",
    "large report",
    "schedule failure"
  ]
}
```

## Accessibility Obligations
- date labels
- export status
- table semantics
- progress feedback

## Testing Obligations
- date range
- export permission
- large report
- schedule failure

## Critic Guidance
Challenge reports without provenance, permissions, or readable data density.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
