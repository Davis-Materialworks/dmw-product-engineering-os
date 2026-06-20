# Benchmarks

This directory supports both reference benchmark definitions and the Benchmark Intelligence System.

> **Note on Schema A benchmarks (01–10):** The numbered bootstrap benchmark projects
> intentionally share the same `source_options` (input format, pipeline parameters, etc.)
> across all Schema A benchmarks. This is by design — Schema A uses a uniform ingestion
> pipeline, and per-benchmark variation lives in `benchmark.json` expected outputs, not in
> source configuration.

Phase 1 bootstrap projects use numbered directories:

- `01-dashboard-saas`
- `02-ecommerce`
- `03-fintech`
- `04-healthcare`
- `05-mobile-app`
- `06-admin-panel`
- `07-ai-chat`
- `08-design-system`
- `09-marketing-site`
- `10-b2b-workflow`

Each project contains:

- `design/`
- `screenshots/`
- `expected-output/`
- `review/`
- `scorecard/`
- `benchmark.json`

Run:

```bash
python3 scripts/benchmark_intelligence.py
```
