# AGENTS.md

This repository contains DMW Product Engineering OS: an independent, agent-agnostic product engineering platform with host-specific adapters.

When editing this repo:

- Preserve Davis Materialworks project identity.
- Keep Adobe XD positioned as the initial supported design source, not as an affiliation or the whole platform.
- Do not imply Adobe affiliation, sponsorship, certification, endorsement, partnership, or approval.
- Follow `DISCLAIMER.md` and `TRADEMARK.md` for public-facing wording.
- Keep the architecture design-source agnostic for future Figma, Penpot, Sketch, design-token, PRD, and design-system inputs.
- Keep durable intelligence in `core/`.
- Keep adapters thin; they translate core rules for Codex, Claude Code, Cursor, and OpenCode.
- Do not create separate OS forks such as "DMW Product Engineering OS for Codex" or "DMW Product Engineering OS for Claude Code".
- Keep `SKILL.md` as the Codex orchestration entrypoint and update it when routing rules change.
- Update `compatibility/` when agent capabilities, limits, preferred workflows, or forbidden workflows change.
- Update `adapters/` only for host-specific prompts, commands, rules, or workflows.
- Put detailed cross-agent guidance in `core/` or existing knowledge modules.
- Do not convert the system into a Figma migration workflow.
- Prefer practical, testable, production-oriented guidance over vague inspirational language.
- Run `python3 scripts/validate_skill_repo.py` before finalizing changes.
