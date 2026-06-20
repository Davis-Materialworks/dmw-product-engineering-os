# Search Pattern

## Recognition Signals
- search box
- filters
- sort
- results
- no results
- facets

## Expected Components
- SearchInput
- FilterPanel
- ResultsList
- EmptyResults
- SortControl

## Component Metadata Schema Example
```json
{
  "component": "SearchInput",
  "industry": "Pattern-dependent",
  "accessibility": [
    "results count",
    "filter labels",
    "keyboard focus",
    "live updates restrained"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "empty query",
    "no results",
    "filters",
    "keyboard navigation"
  ]
}
```

## Accessibility Obligations
- results count
- filter labels
- keyboard focus
- live updates restrained

## Testing Obligations
- empty query
- no results
- filters
- keyboard navigation

## Critic Guidance
Challenge search designs without empty states, clear filters, or relevance explanation.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
