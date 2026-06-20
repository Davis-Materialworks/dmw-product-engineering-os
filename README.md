# Adobe XD Enterprise OS

An Adobe XD-native, agent-agnostic enterprise intelligence platform for turning XD artboards, Design Specs, screenshots, exported assets, and Creative Cloud workflows into production-grade product systems.

The OS is organized as a durable core plus thin adapters:

- `core/` contains agent-independent knowledge, agents, benchmarks, patterns, governance, reviews, compliance, memory, and evolution.
- `adapters/codex/` makes Codex the IMPLEMENTATION ENGINE for repository-wide changes, large refactors, bulk generation, and benchmark automation.
- `adapters/claude-code/` makes Claude Code the ARCHITECTURE ENGINE for deep reasoning, design critique, architecture review, tradeoffs, security architecture, product strategy, and council verdicts.
- `adapters/cursor/` makes Cursor the EXECUTION ENGINE for daily development, inline editing, focused refactoring, and developer workflows.
- `adapters/opencode/` makes OpenCode the ORCHESTRATION ENGINE for multi-agent sequencing, workflow execution, automation, reporting, and evolution loops.
- `compatibility/` documents context limits, strengths, weaknesses, preferred workflows, forbidden workflows, and routing rules.

Do not fork separate operating systems for Codex, Claude Code, Cursor, or OpenCode. Everything durable belongs in `core/`; adapters translate the same core intelligence into each host environment.

## Install

Copy this folder into the appropriate skill, agent, command, rule, or workflow location for your host tool, or keep it in a repo and point the adapter to it according to your environment.

Recommended project usage:

1. Keep this repository separate as a reusable Adobe XD intelligence platform.
2. In each application repo, add the adapter-specific entrypoint for the host tool you use.
3. For a specific task, provide XD Design Specs, screenshots, exported assets, or a short XD ingestion brief.
4. Use `compatibility/routing-matrix.md` to decide which engine should lead architecture, implementation, execution, or orchestration work.

## Recommended Codex AGENTS.md snippet

```md
# AGENTS.md

Use the Adobe XD Enterprise OS Core through the Codex adapter for any task involving Adobe XD designs, artboards, design specs, screenshots, prototypes, exported assets, design systems, or XD-to-code implementation.

Read `core/governance/CONSTITUTION.md` and `compatibility/routing-matrix.md` before nontrivial work.

Codex role: IMPLEMENTATION ENGINE.

Primary stack defaults: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui. Preserve repository conventions when they differ.

Do not suggest migrating to Figma unless explicitly asked. Treat Adobe XD as the design source of truth.
```

## Structure

- `SKILL.md` is the Codex skill entrypoint and orchestration layer.
- `core/` is the canonical agent-independent intelligence layer.
- `adapters/` contains host-specific entrypoints, prompts, commands, rules, and workflows.
- `compatibility/` contains capability docs and task routing.
- `references/` contains legacy and supporting expert modules.
- `templates/` contains reusable briefs, reports, and prompts.
- `checklists/` contains scoring and QA gates.
- `scripts/` contains optional validation, scoring, and benchmark automation helpers.

## Source-aware design decisions

Adobe XD supports Design Specs for developer handoff, including development view workflows, colors, character styles, tokens, measurements, and downloadable assets. XD components support states, instance overrides, and responsive resize behavior. XD prototypes can use auto-animate, drag, time, tap, hover, keyboard/gamepad, and voice-style triggers depending on context. This OS is built around those XD-native concepts rather than a Figma-first conversion path.
