# Hick's Law

## Principle
Decision time increases logarithmically with the number and complexity of choices presented. The more options a user must evaluate, the longer they take to decide — and beyond a threshold, they may abandon the decision entirely.

## How to Detect Violations in XD Artboards
- **Count interactive elements**: If a single screen or modal presents more than 7±2 primary action targets, Hick's Law is likely violated. Count buttons, links, tabs, and menu items that compete for attention at the same hierarchy level.
- **Measure navigation depth**: If the XD prototype's main navigation has more than 5 top-level items, users will scan slower and recall less.
- **Check filter/sort overload**: Artboards with dropdowns or filter bars containing more than 5 options without progressive disclosure (e.g., "Show more filters") violate Hick's Law.
- **Audit CTA multiplicity**: Landing pages or hero sections with more than 2 primary CTAs dilute decision speed. If the XD shows three buttons side by side at equal weight, flag it.

## Concrete XD-to-Code Examples
1. **Navigation menu with 10 top-level items**: The XD artboard shows a horizontal nav bar with "Dashboard, Projects, Reports, Analytics, Settings, Billing, Team, Security, Support, Help." Reduce to 5 core items, move the rest under a "More" dropdown or progressive disclosure menu. Code consequence: smaller bundle, faster render, and users find their target 40% faster.
2. **Pricing page with 7 tiers**: The XD artboard shows 7 pricing cards with overlapping features. Reduce to 3 tiers (Starter, Pro, Enterprise) and use a feature comparison table behind a toggle. Code consequence: fewer components to maintain, less cognitive load on the user, and higher conversion.
3. **Dashboard with 12 competing widgets**: The XD artboard places 12 data cards at equal visual weight. Apply progressive disclosure: show 4 core KPIs, group secondary metrics under expandable sections, and move deep analytics to a dedicated reports page. Code consequence: faster initial render, simpler state management.

## When to Invoke Hick's Law in a Design Critique
- During component review when a screen has more than 5 top-level actions
- During navigation architecture review — before coding the nav component
- When a stakeholder requests "add another option" without removing anything
- On mobile artboards where screen real estate is especially constrained

## Common False Positives
- **Filter-rich interfaces for power users**: A data table with 15 filter options serves expert users who need precision. The complexity is deliberate, not accidental. Validate by checking whether the target persona is a daily power user.
- **Hierarchically organized menus**: A mega-menu with 30 items is fine if they are grouped into 4 clearly labeled categories. The number of *categories* matters for Hick's Law, not the total item count.
- **Wizards and multi-step flows**: Breaking a complex form into 6 steps does not violate Hick's Law — each step presents few choices. The total step count is irrelevant; choices-per-step is the metric.