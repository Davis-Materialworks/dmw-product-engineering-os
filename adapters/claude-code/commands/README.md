# Claude Code Commands

Custom slash commands for architecture and design governance workflows.

## Available Commands

### `/design-review`
Runs the full design critic pipeline against a target file, artboard export, or generated UI.
- Loads `knowledge/anti-patterns/` and `knowledge/ux-laws/` for violation detection.
- Produces a ranked issue list with severity levels: BLOCKER, STRONG, SUGGESTION.
- Outputs to `results/` with timestamped report.

### `/architecture-review`
Validates architecture decisions against the pattern library and constitution.
- Cross-references `knowledge/architecture-patterns/` against the current codebase structure.
- Flags violations of dependency direction, boundary rules, and pattern misuse.
- Generates an ADR draft when a new architectural decision is detected.

### `/council-convene`
Launches a multi-agent council session using `knowledge/agents/` contracts.
- Sequentially invokes: XD_DESIGN_CRITIC → XD_PRINCIPAL_ENGINEER → XD_SECURITY_ARCHITECT → XD_PRODUCT_STRATEGIST.
- Synthesizes conflicting opinions into a weighted tradeoff matrix.
- Outputs a council verdict with dissenting opinions preserved.

### `/constitution-check`
Validates a proposed change against `governance/CONSTITUTION.md`.
- Returns PASS, CONDITIONAL, or VIOLATION with specific clause references.
- Requires explicit justification for any CONDITIONAL or VIOLATION result.
- Must pass before architecture review can approve a change.