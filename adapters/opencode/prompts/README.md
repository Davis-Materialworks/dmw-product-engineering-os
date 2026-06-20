# OpenCode Prompts

Prompt templates for orchestrating multi-agent workflows, evolution feedback, and report generation.

## Prompt Templates

### `multi-agent-sequencing`
Coordinates multiple specialized agents through a sequential review pipeline.
- Input: design source files, target platform, and quality requirements.
- Executes: Design Critic → Principal Engineer → Security Architect → Product Strategist → Judge.
- Each agent receives the previous agent's output plus the original design context.
- Produces a consolidated report with action items prioritized by agent consensus weight.

### `evolution-feedback`
Extracts lessons learned from a completed project and writes them into the knowledge base.
- Scans: commit history, PR discussions, benchmark score deltas, and design review notes.
- Identifies: new patterns, repeated failures, unexpected successes, and process improvements.
- Writes entries into `knowledge/evolution/` with cross-references to relevant pattern or failure files.
- Flags anything that should be promoted to `knowledge/failures/` if it recurs.

### `report-generation`
Generates a structured project report suitable for stakeholder review.
- Sources: benchmark scorecards, agent review outputs, ADR registry, and evolution notes.
- Sections: executive summary, quality scores by category, architecture decisions, risk register.
- Outputs to `reports/` with machine-readable JSON and human-readable Markdown formats.
- Includes a "what we learned" section sourced from `knowledge/evolution/`.

### `compliance-audit`
Audits generated code against a selected compliance pack.
- Input: target compliance pack from `compliance/` (HIPAA, WCAG, SOC2, GDPR, PCI-DSS, etc.).
- Scans: generated components, API routes, data flows, and configuration.
- Produces: compliance gap report with severity ratings and remediation steps.