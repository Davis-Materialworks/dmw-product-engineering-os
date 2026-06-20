# Agent Routing Matrix

| Task | Preferred Agent | Role |
| --- | --- | --- |
| architecture review | claude-code | ARCHITECTURE ENGINE |
| design critique | claude-code | ARCHITECTURE ENGINE |
| principal engineer review | claude-code | ARCHITECTURE ENGINE |
| security architecture review | claude-code | ARCHITECTURE ENGINE |
| product strategy review | claude-code | ARCHITECTURE ENGINE |
| council verdict preparation | claude-code | ARCHITECTURE ENGINE |
| large refactor | codex | IMPLEMENTATION ENGINE |
| benchmark automation | codex | IMPLEMENTATION ENGINE |
| repository-wide code generation | codex | IMPLEMENTATION ENGINE |
| inline implementation | cursor | EXECUTION ENGINE |
| focused refactoring | cursor | EXECUTION ENGINE |
| daily development workflow | cursor | EXECUTION ENGINE |
| workflow automation | opencode | ORCHESTRATION ENGINE |
| multi-agent sequencing | opencode | ORCHESTRATION ENGINE |
| report/evolution orchestration | opencode | ORCHESTRATION ENGINE |

## Rule
When the requested task matches multiple rows, route architecture and risk decisions to Claude Code first, implementation to Codex or Cursor second, and orchestration to OpenCode when coordination is the main problem.
