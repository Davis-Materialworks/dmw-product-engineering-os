# Miller's Law

## Principle
The average person can hold approximately 7 (±2) items in working memory at once. Chunking information into meaningful groups helps users process, understand, and retain complex content by reducing the number of discrete items they must track.

## How to Detect Violations in XD Artboards
- **Count form fields in a single visual group**: If a form section presents more than 5-7 fields without visual grouping, users will lose context. Look for forms where field labels and inputs form one undifferentiated block.
- **Audit dashboard data points**: A single screen with more than 7 independent metrics forces users to constantly re-read to track values. Check whether metrics are grouped into meaningful categories (financial, performance, health) or left as a flat grid.
- **Check navigation depth alongside breadth**: An artboard with 9 top-level nav items AND deep submenus forces users to hold both the current location and the destination in memory. The product of breadth × relevant depth should not exceed working memory limits.
- **Evaluate comparison UI**: Side-by-side comparisons of products/plans with more than 5 features across more than 3 options exceed working memory. Users resort to paper notes or browser tabs to compare.

## Concrete XD-to-Code Examples
1. **Registration form with 14 fields in one block**: The XD artboard shows 14 input fields stacked without section headers. Chunk into 3 groups: "Account Details" (email, password, confirm), "Personal Info" (name, phone, country), and "Preferences" (notifications, theme). Use fieldset + legend or Card components to visually separate groups. Code consequence: `FormSection` components with distinct borders, collapsed state tracking per section.
2. **Dashboard with 20 unlabeled KPI cards**: The XD artboard shows a 4×5 grid of metric cards. Group into 4 categories (Revenue, Users, Performance, Health) with section headers. Reduce each category to top 3-4 metrics; bury the rest under "View all." Code consequence: `SectionList` or grouped card layout with expand/collapse per section.
3. **Phone number input as 10 separate fields**: The XD artboard shows 10 individual digit boxes for a phone number. Replace with a single input field with masking. The user's mental model is "my phone number," not "10 digits." Code consequence: single `TextInput` with `onChangeText` mask formatting, reduced from 10 controlled inputs to 1.

## When to Invoke Miller's Law in a Design Critique
- During form design review — before the form component is built
- When a stakeholder says "just add another field"
- During information architecture review of complex dashboards or admin panels
- On mobile designs where screen space forces dense layouts

## Common False Positives
- **Expert interfaces with learned chunking**: A Bloomberg terminal shows hundreds of data points, but expert users have built chunking strategies over years. Miller's Law applies to novice-to-intermediate users, not domain experts with trained working memory.
- **Search results and feeds**: A list of 20 search results with clear, scannable titles and metadata snippets does not violate Miller's Law. Users do not hold all 20 in memory — they scan sequentially, deciding on each item independently.
- **Tabular data with stable headers**: A data table with 12 columns and 500 rows is acceptable if column headers are frozen and users scan row-by-row. The headers act as external memory (recognition, not recall), which bypasses working memory limits.