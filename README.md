# DMW Product Engineering OS

Enterprise Design-to-Production Intelligence Platform for Web Applications, Mobile Applications, Design Systems, and Product Engineering.

DMW Product Engineering OS is an independent open source project created and maintained by Davis Materialworks. It transforms design assets, product concepts, user experiences, and design systems into production-ready product engineering guidance, review systems, benchmarks, and implementation workflows.

## Independent Project Notice

DMW Product Engineering OS is an independent open-source initiative created by Davis Materialworks. The project is not affiliated with or endorsed by Adobe. Adobe XD support exists because Adobe Creative Cloud tools have been part of our day-to-day design and product development workflow for many years, and this framework was originally developed to improve those real-world processes.

This repository is not an Adobe product, plugin, exporter, certification program, or official workflow. It is not affiliated with, endorsed by, sponsored by, authorized by, or associated with Adobe Inc. Adobe XD is the initial supported design source because it reflects real Davis Materialworks workflows and existing design assets. See [DISCLAIMER.md](DISCLAIMER.md) and [TRADEMARK.md](TRADEMARK.md).

## Mission

DMW Product Engineering OS helps teams move from design intent to production-quality software with stronger review loops, clearer architecture decisions, accessibility enforcement, benchmark-driven quality gates, and organizational learning.

The goal is not shallow design-to-code generation. The goal is production-grade product engineering.

## Vision

The long-term objective is a design-source-agnostic product engineering intelligence platform that can evaluate, critique, plan, implement, test, and improve product systems across multiple design and product inputs.

Current primary design source:

- Adobe XD

Planned and compatible future sources:

- Figma
- Penpot
- Sketch
- Design Tokens
- Product Requirement Documents
- Design System Specifications
- User Flow Documentation

## What This Repository Is

- A design intelligence framework
- A product engineering platform
- A multi-agent review system
- A benchmark-driven quality framework
- A continuous learning platform
- A public, reusable foundation for product engineering workflows

## What This Repository Is Not

- An Adobe XD plugin
- A design exporter
- A code generator
- A prompt collection
- An official Adobe project
- A replacement for human product, design, engineering, security, legal, or accessibility review

## Core Principles

The project Constitution lives at [governance/CONSTITUTION.md](governance/CONSTITUTION.md). Its core principles are:

1. User Value Over Visual Fidelity
2. Accessibility Over Aesthetics
3. Maintainability Over Cleverness
4. Evidence Over Assumptions
5. Simplicity Over Complexity
6. Business Outcomes Over Feature Count
7. Design Intent Over Pixel Perfection
8. Security And Privacy Are Product Requirements
9. Learning Must Come From Evidence

## Architecture Overview

DMW Product Engineering OS is organized as a durable core plus thin adapters:

- `core/` contains agent-independent knowledge, agents, benchmarks, patterns, governance, reviews, compliance, memory, and evolution.
- `adapters/codex/` makes Codex the IMPLEMENTATION ENGINE for repository-wide changes, large refactors, bulk generation, and benchmark automation.
- `adapters/claude-code/` makes Claude Code the ARCHITECTURE ENGINE for deep reasoning, design critique, architecture review, tradeoffs, security architecture, product strategy, and council verdicts.
- `adapters/cursor/` makes Cursor the EXECUTION ENGINE for daily development, inline editing, focused refactoring, and developer workflows.
- `adapters/opencode/` makes OpenCode the ORCHESTRATION ENGINE for multi-agent sequencing, workflow execution, automation, reporting, and evolution loops.
- `compatibility/` documents context limits, strengths, weaknesses, preferred workflows, forbidden workflows, and routing rules.

Everything durable belongs in the core. Adapters translate the same core intelligence into each host environment.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full architecture overview.

## Repository Structure

```text
/
|-- README.md
|-- LICENSE
|-- DISCLAIMER.md
|-- TRADEMARK.md
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- ROADMAP.md
|-- ARCHITECTURE.md
|-- GOVERNANCE.md
|-- AGENTS.md
|-- SKILL.md
|-- adapters/
|-- agents/
|-- benchmarks/
|-- compliance/
|-- governance/
|-- knowledge/
|-- memory/
|-- patterns/
|-- reviews/
|-- workflows/
|-- reports/
`-- scripts/
```

## Supported Platforms

Primary implementation targets:

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

Secondary implementation targets:

- React Native
- Flutter
- SwiftUI

Enterprise product targets:

- SaaS Platforms
- Internal Tools
- AI Products
- Ecommerce
- Fintech
- Healthcare
- Government
- Enterprise Applications

## Supported Agents

The repository supports multiple agent environments without forking the operating system:

| Agent Environment | Role | Best Used For |
| --- | --- | --- |
| Codex | IMPLEMENTATION ENGINE | Repository-wide changes, large refactors, bulk generation, benchmark automation |
| Claude Code | ARCHITECTURE ENGINE | Deep reasoning, architecture, design reviews, tradeoffs, council review |
| Cursor | EXECUTION ENGINE | Daily development, inline editing, focused refactoring |
| OpenCode | ORCHESTRATION ENGINE | Workflow execution, automation, multi-agent sequencing |

Routing rules live in [compatibility/routing-matrix.md](compatibility/routing-matrix.md).

## Quality Standards

The World-Class Gate requires:

- Accessibility >= 95
- Architecture >= 90
- Maintainability >= 90
- Security >= 90
- Design Quality >= 90
- Testability >= 90
- Documentation >= 90
- Performance >= 85

The gate may produce one of four verdicts:

- PASS
- PASS WITH WARNINGS
- REVISE
- REJECT

## Getting Started

1. Read [DISCLAIMER.md](DISCLAIMER.md), [TRADEMARK.md](TRADEMARK.md), and [governance/CONSTITUTION.md](governance/CONSTITUTION.md).
2. Choose the adapter for your agent environment under `adapters/`.
3. Review [compatibility/routing-matrix.md](compatibility/routing-matrix.md) before assigning work to an agent.
4. Use `SKILL.md` as the Codex skill entrypoint when installing this repository as a Codex skill.
5. Run validation:

```bash
python3 scripts/validate_skill_repo.py
python3 scripts/score_benchmarks.py
```

## Contributing

Contributions should improve product engineering quality, public documentation, benchmarks, governance, accessibility, architecture, or agent compatibility. Start with [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

## Roadmap

The roadmap is maintained in [ROADMAP.md](ROADMAP.md). The near-term focus is public-repo maturity, design-source abstraction, benchmark expansion, governance hardening, and real-project learning loops.

## License

This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE).

The license grants rights to use the software, but does not grant rights to use Davis Materialworks names, logos, trademarks, or brand identity. See [TRADEMARK.md](TRADEMARK.md).
