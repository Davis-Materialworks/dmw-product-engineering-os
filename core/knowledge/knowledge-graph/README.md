# Knowledge Graph

Store relationships between screens, components, actions, data, states, risks, and tests. Use this for large-project reasoning instead of flat component lists.

## Relationship Format

```text
Dashboard
├─ DataTable
├─ FilterPanel
├─ ExportAction
└─ AnalyticsWidget
```

## Required Node Types
- screen
- component
- action
- data_source
- state
- user_goal
- business_goal
- accessibility_obligation
- test_case
- risk

## Rule
For multi-screen work, build a graph before architecture or implementation. Use the graph to detect missing states, orphan components, duplicate flows, and untested critical paths.
