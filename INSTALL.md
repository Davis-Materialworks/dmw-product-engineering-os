# Installation

DMW Product Engineering OS is a folder-based agent skill bundle — a directory of markdown files that agents load as structured intelligence. Installation means cloning the repo and registering it with your agent environment.

## Quick Install (Agent Skills Ecosystem)

The preferred method is through the cross-agent skills ecosystem (Codex, Claude Code, Cursor, OpenCode):

```bash
skills add Davis-Materialworks/dmw-product-engineering-os
```

To update when new releases are published:

```bash
skills update dmw-product-engineering-os
```

## Manual Installation

If your agent environment uses a different skills manager, follow the steps below.

### Prerequisites

- Python 3.10+
- Git
- At least one of: Codex, Claude Code, Cursor, or OpenCode

### Step 1: Clone

```bash
git clone https://github.com/Davis-Materialworks/dmw-product-engineering-os.git ~/.dmw-os
```

Any location works. `~/.dmw-os` is the convention used below.

## Step 2: Register with Your Agent

### Codex (primary host)

Codex reads skills from folder bundles. Point Codex to the repo root so it loads `SKILL.md` as an available skill:

```json
// In your Codex config (codex.json or project-level manifest):
{
  "skills": ["~/.dmw-os"]
}
```

For project-specific agent guidance, copy or symlink `adapters/codex/AGENTS.md` to your application repo root as `AGENTS.md`.

### Claude Code

Register the repo as a Claude Code custom skill:

```bash
# Option A: install as a project-level skill
mkdir -p .claude/skills
ln -s ~/.dmw-os .claude/skills/dmw-os

# Option B: install as a user-level skill
mkdir -p ~/.claude/skills
ln -s ~/.dmw-os ~/.claude/skills/dmw-os
```

For project-level Claude guidance, copy `adapters/claude-code/CLAUDE.md` to your repo root.

### Cursor

Copy Cursor rules into your project:

```bash
cp adapters/cursor/.cursor/rules/* .cursor/rules/
```

Or copy the entire adapter into your project for full workflows:

```bash
cp -r adapters/cursor/* .
```

### OpenCode

Register the repo as an OpenCode skill by adding it to your `opencode.json` skills array or symlink it into the skills directory:

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.dmw-os ~/.config/opencode/skills/dmw-os
```

Copy `adapters/opencode/agents/*` to your OpenCode agents directory to enable multi-agent orchestration.

## Step 3: Verify

```bash
python3 scripts/validate_skill_repo.py
```

A clean exit means the repo is structurally valid and ready for use.

## Verification: What Success Looks Like

After loading the skill, your agent should recognize DMW Product Engineering OS capabilities. Test with:

> **"Audit this XD dashboard design for accessibility issues."**

The agent should respond with terms like "evidence labeling," "world-class gate," "CONFIRMED/INFERRED," and reference knowledge modules. If it responds generically — for example, "Your design looks fine. Here are some accessibility tips" — the skill path may not be registered correctly. Verify your adapter path matches the instructions above.

## Step 4: Project Integration

Put a short `AGENTS.md` in each application repo telling the agent when to invoke DMW Product Engineering OS. Example:

```markdown
# AGENTS.md

When working with design assets, Adobe XD files, design specs, or
design-to-production tasks, load DMW Product Engineering OS from
~/.dmw-os and follow its routing rules.
```

---

Before public or client-facing use, read `DISCLAIMER.md`, `TRADEMARK.md`, and `governance/CONSTITUTION.md`.