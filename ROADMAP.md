# Roadmap

This roadmap describes the public evolution of DMW Product Engineering OS. It is intentionally practical: improvements should come from benchmark evidence, real projects, failures, success patterns, and contributor experience.

## Phase 1: Public Repository Maturity

- Publish clear disclaimer, trademark, contribution, conduct, security, architecture, governance, and roadmap documents.
- Standardize repository identity around DMW Product Engineering OS.
- Preserve Adobe XD as the initial supported design source while clarifying the design-source-agnostic architecture.
- Keep the Apache License 2.0 and clarify that trademark rights are not granted by the license.

## Phase 2: Core Platform Stabilization

- Continue separating agent-independent core knowledge from adapter-specific workflows.
- Reduce duplicated root/core knowledge where appropriate without breaking compatibility.
- Strengthen validation scripts so public documentation, adapters, benchmarks, and governance documents remain present.
- Expand ADR, decision, design-intent, risk, and evolution workflows.

## Phase 3: Benchmark Expansion

- Add more benchmark projects across SaaS, ecommerce, fintech, healthcare, AI products, enterprise systems, and mobile applications.
- Track benchmark score history over time.
- Detect regressions in design quality, accessibility, architecture, performance, maintainability, security, testability, and documentation.
- Convert repeated benchmark failures into prevention rules.

## Phase 4: Design-Source Abstraction

- Keep Adobe XD support as the first implementation.
- Add source adapters for additional design and product inputs when there is enough evidence and demand.
- Candidate sources include Figma, Penpot, Sketch, Design Tokens, Product Requirement Documents, Design System Specifications, and User Flow Documentation.
- Avoid hardcoding a single design tool into the core platform.

## Phase 5: Enterprise Governance And Learning

- Mature review lifecycle, approval workflow, risk register, ADR framework, and decision tracking.
- Improve institutional memory and portfolio intelligence.
- Add success-pattern tracking alongside failure tracking.
- Feed lessons learned from production projects into `knowledge/evolution/`.

## Phase 6: Ecosystem Readiness

- Improve adapter-specific workflows for Codex, Claude Code, Cursor, and OpenCode.
- Publish usage examples for different organization types and industries.
- Clarify extension points for new agents, design sources, benchmark packs, and compliance packs.
- Continue tightening public documentation and contributor experience.
