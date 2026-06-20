# Cursor Adapter — EXECUTION ENGINE

Role: Handles daily development, inline editing, focused refactoring, and developer workflows after architecture decisions are made.

## Cursor-Specific Rules

### `inline-editing-conventions`
Cursor's inline diff model works best with small, single-purpose edits that touch one concern at a time.
- Each edit should address exactly one architectural concern (one anti-pattern fix, one refactoring, one component extraction).
- Run validation after each inline edit batch — never accumulate unreviewed changes.
- Prefer Cursor's inline suggestion UI for applying `knowledge/patterns/` guidance to existing code.

### `escalation-rules`
Cursor handles daily implementation. Escalate to other engines when:
- A change affects architecture boundaries → escalate to Claude Code (`adapters/claude-code/CLAUDE.md`)
- A change requires multi-file orchestration → escalate to OpenCode (`adapters/opencode/workflows/orchestration-engine.md`)
- A change needs benchmark validation → escalate to Codex (`adapters/codex/AGENTS.md`)
- A change touches `governance/CONSTITUTION.md` or `SKILL.md` → block until architecture review completes

### `quick-reference-paths`
Paths for common Cursor workflows:
- Architecture patterns: `knowledge/architecture-patterns/`
- Anti-pattern detection: `knowledge/anti-patterns/`
- Refactoring recipes: `knowledge/refactoring/`
- Design tokens and components: `references/design-system/`
- UX law references: `knowledge/ux-laws/`
- Compliance requirements: `compliance/`
- Validation scripts: `scripts/`

Consult these paths before writing or refactoring any component. Cursor's role is precise execution, not architectural invention.