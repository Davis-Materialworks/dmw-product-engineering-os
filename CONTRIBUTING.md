# Contributing

Thank you for considering a contribution to DMW Product Engineering OS.

This project is intended to improve design-to-production quality through practical product engineering guidance, benchmarks, governance, review systems, and agent-compatible workflows.

## Contribution Priorities

High-value contributions include:

- Stronger benchmark scenarios
- Better accessibility checks
- Better architecture review rules
- Better governance and decision records
- Improved design-source abstraction
- Agent adapter improvements
- Public documentation improvements
- Security, privacy, and compliance hardening
- Real-world lessons added to `knowledge/evolution/`

## Before You Start

Read:

- [README.md](README.md)
- [DISCLAIMER.md](DISCLAIMER.md)
- [TRADEMARK.md](TRADEMARK.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [governance/CONSTITUTION.md](governance/CONSTITUTION.md)

## Development Workflow

1. Create a focused branch.
2. Keep changes scoped to one purpose.
3. Preserve the agent-agnostic core plus thin adapter architecture.
4. Put durable rules in `core/`, `knowledge/`, `governance/`, or other shared modules.
5. Put host-specific instructions only in `adapters/`.
6. Avoid adding speculative modules without evidence from benchmarks, failures, project experience, or user needs.
7. Run validation before opening a pull request:

```bash
python3 scripts/validate_skill_repo.py
python3 scripts/score_benchmarks.py
```

## Documentation Standards

Documentation should be:

- Clear
- Actionable
- Evidence-oriented
- Enterprise-ready
- Free of marketing hype
- Consistent with the Constitution

Do not create placeholder content. If a topic is not ready for a real document, open an issue describing the gap instead.

## Pull Request Expectations

Pull requests should include:

- Summary of what changed
- Why it changed
- Validation performed
- Any known risks or tradeoffs
- Related issue, benchmark, failure, decision, or ADR when applicable

## Legal And Trademark Notes

Do not imply Adobe affiliation, endorsement, sponsorship, certification, or approval. Do not add Adobe logos or proprietary Adobe assets. Follow [TRADEMARK.md](TRADEMARK.md).
