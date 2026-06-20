# Codex Prompts

Reusable prompt templates for implementation, benchmarking, and validation workflows.

## Prompt Templates

### `bulk-component-generation`
Generates multiple UI components from XD design specs in a single pass.
- Input: XD artboard analysis output, component taxonomy, and design tokens.
- Produces component files with accessibility contracts, state variants, and test stubs.
- Use when: migrating a full XD screen to code with all its component instances.

### `benchmark-run`
Executes the benchmark suite against generated output for quality scoring.
- Runs `scripts/score_benchmarks.py` against target directory.
- Produces a scorecard with per-category scores (accessibility, responsiveness, design fidelity).
- Flags regressions below the quality gate threshold defined in `knowledge/world-class-enhancements/`.

### `validation-pass`
Runs pre-commit validation on generated code before merging.
- Checks: accessibility compliance, component metadata completeness, naming conventions.
- Cross-references `knowledge/anti-patterns/` for known issues.
- Runs `scripts/validate_skill_repo.py` and fails the pass on any error.

### `refactor-chunk`
Applies a single refactoring rule from `knowledge/refactoring/` to a target file.
- Isolates changes to one refactoring type per invocation (extraction, simplification, optimization).
- Produces a before/after diff and a rationale comment referencing the specific refactoring rule applied.