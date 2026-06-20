# Changelog

All notable changes to DMW Product Engineering OS.

## [1.0.0] - 2026-06-20

### Added
- **Core orchestration**: `SKILL.md` as the primary Codex entrypoint with task routing, agent invocation, and gate enforcement rules.
- **Knowledge modules**: Design intelligence modules covering migration intelligence (5 target frameworks), UX laws (7 laws with XD-specific detection and critique patterns), design intent preservation, component intelligence, and pattern libraries.
- **Migration playbooks**: XD-to-NextJS, XD-to-React-Native, XD-to-Flutter, XD-to-SwiftUI, and XD-to-Design-System with token translation tables, component mapping guidelines, common pitfalls, and verification checklists.
- **UX law enforcement**: Hick's Law, Fitts's Law, Miller's Law, Jakob's Law, Tesler's Law, Peak-End Rule, and Doherty Threshold — each with XD artboard violation detection, concrete examples, and false positive guidance.
- **World-Class Gate**: Automated quality scoring across 8 dimensions with minimum thresholds and rejection conditions.
- **Agent roster**: 10 specialized review agents (design critic, principal engineer, security architect, product strategist, cost analyst, accessibility lead, council, future-proofing, simplicity advocate, executive reviewer) with multi-agent mental model.
- **Failure library framework**: Structured failure recording with root cause analysis, prevention rules, and rule creation triggers.
- **Benchmark suite**: 7 industry categories with expected abilities and standardized scoring.
- **Self-improvement loop**: Post-project review requirements and evolution repository with dated entries.
- **Compliance packs**: WCAG, GDPR, PDPA, HIPAA, PCI-DSS, SOC2, ISO27001 with key requirements.
- **Evolution tracking**: Framework foundation decisions (evidence labels, gate thresholds, principal engineer veto, component metadata) and responsive strategy (breakpoint taxonomy, mobile-first default, XD artboard width detection).
- **Design intent preservation**: Business goal, user goal, action hierarchy, and preservation rules for dashboard and extensible to other screen types.
- **Host adapters**: Thin translation layers for Codex, Claude Code, Cursor, and OpenCode.
- **Validation**: `scripts/validate_skill_repo.py` for structural integrity checks.

### Design Principles
- Adobe XD is the initial supported design source; architecture is design-source agnostic for future inputs (Figma, Penpot, Sketch, design tokens, PRDs, design systems).
- Durable intelligence lives in `core/`; adapters remain thin and host-specific.
- Every code output must pass the World-Class Gate before shipping.
- Evidence from XD is labeled CONFIRMED, INFERRED, ASSUMED, or UNKNOWN — labels determine downstream treatment.