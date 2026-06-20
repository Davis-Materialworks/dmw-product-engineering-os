# AGENTS.md

This repository contains Adobe XD Enterprise OS: an agent-agnostic core platform with host-specific adapters.

When editing this repo:

- Preserve Adobe XD-first positioning.
- Keep durable intelligence in `core/`.
- Keep adapters thin; they translate core rules for Codex, Claude Code, Cursor, and OpenCode.
- Do not create separate OS forks such as "Adobe XD Enterprise OS for Codex" or "Adobe XD Enterprise OS for Claude Code".
- Keep `SKILL.md` as the Codex orchestration entrypoint and update it when routing rules change.
- Update `compatibility/` when agent capabilities, limits, preferred workflows, or forbidden workflows change.
- Update `adapters/` only for host-specific prompts, commands, rules, or workflows.
- Put detailed cross-agent guidance in `core/` or existing knowledge modules.
- Do not convert the system into a Figma migration workflow.
- Prefer practical, testable, production-oriented guidance over vague inspirational language.
- Run `python3 scripts/validate_skill_repo.py` before finalizing changes.
