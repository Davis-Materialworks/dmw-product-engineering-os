# Dashboard Design Intent

screen: Dashboard
business_goal: Increase retention by making account health immediately visible and actionable
user_goal: Monitor account health, identify anomalies, and decide the next action within 10 seconds
primary_action: View insights (scan KPIs for deviations from normal)
secondary_action: Export report (for sharing or deeper offline analysis)

## Evidence
Dashboard screens in SaaS products combine account health indicators, summary metrics, alert banners, quick-action buttons, and reporting affordances. Retention improves when users can glance at the dashboard and answer three questions in under 5 seconds: "Is everything okay?", "What changed?", and "What should I do next?" Dashboards that are passive metrics walls — presenting data without interpretation — increase time-to-decision and decrease return frequency.

## UX Principles Specific to Dashboards
1. **Glanceability over precision**: The first view should communicate status through visual encoding (color, size, position), not numbers. A red indicator means "attention needed" faster than a number that requires comparison to a baseline.
2. **Anomaly-first ordering**: Place anomalies and changes above stable metrics. A metric that hasn't changed in 30 days does not need to be in the top-left position — put the metric that changed 40% since yesterday there.
3. **Progressive disclosure of detail**: Show KPIs, then trends on hover/expand, then raw data on click. Three levels of depth, never all at once. This maps to: summary cards → expandable charts → full report/data table.
4. **Contextual comparisons**: Every metric needs a comparison baseline (yesterday, last week, same period last year, target). A number without context is trivia, not intelligence.
5. **Action coupling**: Every significant metric must imply an action. "Revenue down 15%" without a "View affected transactions" link is incomplete — the user has to navigate to find the root cause.

## Common XD Dashboard Patterns and Their Business Goals
| XD Pattern | Business Goal | Implementation Notes |
|-----------|--------------|---------------------|
| KPI row with sparklines | Answer "is everything okay?" in <3 seconds | Use `recharts` sparklines; color-code positive/negative trends; add tooltip for precision |
| Alert/notification banner | Surface critical issues immediately | Position above the KPI row; auto-dismiss resolved alerts; link to resolution flow |
| Data table with filter bar | Enable deep investigation by power users | Paginate or virtualize; persist filter state in URL; add export button adjacent |
| Chart widgets (line, bar, donut) | Show trends the KPIs don't capture | 3-6 months of history by default; toggle to 12M/All Time; add annotation markers for events |
| Quick-action buttons | Shortcut common next-steps from dashboard | "Create New," "View All," "Download Report" — limit to 3-4; align with user's most common post-dashboard action |
| Activity feed | Show what happened recently in chronological order | Limit to 10 items; group by time ("Today," "Yesterday," "This Week"); link each item to full detail |

## Preservation Rules
- Keep account health visible above secondary reporting tools — the KPI row or equivalent must be in the first viewport (above the fold)
- Preserve a clear primary path to insights — the user's most common "what does this mean?" path must be one click/tap from the dashboard
- Keep export available but secondary unless user research or benchmark data elevates reporting to primary
- Do not turn the dashboard into a passive metrics wall; every major metric should imply an interpretation or next step. If a metric appears on the dashboard and clicking it leads nowhere, remove it or add a drill-down.
- Maintain visual hierarchy: anomaly alerts → key metrics → trends → detail links → secondary tools. Never let a secondary tool (export, settings, theme toggle) dominate the primary action zone.
- When adding a new dashboard widget, remove one. Dashboard widget count should trend toward essentialism, not accumulation.