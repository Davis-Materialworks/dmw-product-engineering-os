# Architecture

DMW Product Engineering OS is organized as a design-source-aware, agent-agnostic product engineering intelligence platform.

## Architectural Goals

- Keep durable intelligence independent of any one agent host.
- Keep design-source-specific assumptions out of the core platform where possible.
- Support Adobe XD as the first design-source implementation.
- Preserve room for future inputs such as Figma, Penpot, Sketch, design tokens, product requirements, and user-flow documentation.
- Make review, governance, accessibility, architecture, testing, and benchmark quality explicit.

## Core And Adapters

The repository uses a core plus adapters model:

- `core/` is the canonical cross-agent intelligence layer.
- `adapters/` contains host-specific entrypoints and workflows.
- `compatibility/` explains agent strengths, weaknesses, limits, and routing.

Adapters must not fork the operating system. They translate the same core into the local conventions of Codex, Claude Code, Cursor, and OpenCode.

## Core Domains

The core platform contains:

- `core/knowledge/`: reusable knowledge modules, failure libraries, success patterns, architecture patterns, prompts, and learning systems.
- `core/agents/`: core challenge and verdict agents.
- `core/benchmarks/`: benchmark definitions and expected outputs.
- `core/patterns/`: design and product pattern recognition.
- `core/governance/`: constitutional rules and governance constraints.
- `core/reviews/`: enterprise review workflows.
- `core/compliance/`: compliance-oriented review packs.
- `core/memory/`: ADRs, decision memory, and design intent memory.
- `core/evolution/`: lessons learned and benchmark evolution notes.

## Agent Roles

| Agent Environment | Platform Role | Responsibility |
| --- | --- | --- |
| Codex | IMPLEMENTATION ENGINE | Large edits, repository-wide implementation, refactors, validation scripts, benchmark automation |
| Claude Code | ARCHITECTURE ENGINE | Deep reasoning, design critique, architecture review, tradeoffs, council preparation |
| Cursor | EXECUTION ENGINE | Daily development, inline changes, focused refactoring, local developer workflows |
| OpenCode | ORCHESTRATION ENGINE | Workflow execution, multi-agent sequencing, automation, reports, evolution loops |

Task routing is defined in [compatibility/routing-matrix.md](compatibility/routing-matrix.md).

## Design Source Strategy

Adobe XD is the initial supported design source because it reflects the real-world workflows and assets used by Davis Materialworks. It should be treated as a source adapter and workflow implementation, not as the entire platform identity.

Future design sources should be added through source-specific modules that feed the same core review, benchmark, governance, and implementation workflows.

## Quality Flow

Typical flow:

1. Ingest design or product input.
2. Label evidence as `CONFIRMED`, `INFERRED`, `ASSUMED`, or `UNKNOWN`.
3. Extract design intent, components, tokens, flows, risks, and constraints.
4. Run design, accessibility, architecture, security, product, cost, and code-review agents.
5. Apply benchmark and world-class gates.
6. Produce implementation guidance or code through the correct adapter.
7. Store failures, successes, decisions, and lessons learned.

## Governance Flow

Major decisions should use:

- Constitution review
- ADRs
- Decision memory
- Risk register
- Human override level
- Judge verdict
- Evolution notes after completion

See [GOVERNANCE.md](GOVERNANCE.md).
