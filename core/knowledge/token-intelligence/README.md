# Design Token Intelligence

Do more than extract tokens. Normalize, deduplicate, detect drift, and recommend consolidation.

## Required Analysis
- Normalize raw XD values into primitive, semantic, component, state, and mode tokens.
- Detect duplicates with identical values and different names.
- Detect near-duplicates that suggest design drift.
- Detect semantic conflicts, such as the same red used for danger and promotion.
- Recommend consolidation, aliases, deprecations, and migration steps.

## Output
token_inventory:
duplicates:
drift_clusters:
semantic_conflicts:
consolidation_plan:
migration_notes:
