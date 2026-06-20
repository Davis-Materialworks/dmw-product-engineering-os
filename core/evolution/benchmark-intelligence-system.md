# Benchmark Intelligence System

## Lessons Learned
The DMW Product Engineering OS needs benchmark projects, expected outputs, actual outputs, score history, regression detection, and reporting to measure improvement objectively.

## Missing Rules Added
- Store expected outputs before scoring actual outputs.
- Store results by date under `results/YYYY-MM-DD/`.
- Detect regressions and improvements over time.
- Generate reports and feed lessons into `knowledge/evolution/`.

## Benchmark Changes Required
Replace placeholder design inputs with real XD projects, recreated interfaces, UI challenges, industry-specific projects, and design-system-focused projects.

## Future Scale Target
Support 100+ projects and promote repeated failures into the failure library.
