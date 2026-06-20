from pathlib import Path

root = Path(__file__).resolve().parents[1]

required_files = [
    root / 'SKILL.md',
    root / 'README.md',
    root / 'AGENTS.md',
    root / 'DISCLAIMER.md',
    root / 'TRADEMARK.md',
    root / 'CONTRIBUTING.md',
    root / 'CODE_OF_CONDUCT.md',
    root / 'SECURITY.md',
    root / 'ROADMAP.md',
    root / 'ARCHITECTURE.md',
    root / 'GOVERNANCE.md',
    root / 'scripts' / 'score_benchmarks.py',
    root / 'scripts' / 'benchmark_intelligence.py',
    root / 'governance' / 'CONSTITUTION.md',
    root / 'agents' / 'XD_RED_TEAM.md',
    root / 'agents' / 'XD_JUDGE.md',
    root / 'compatibility' / 'routing-matrix.md',
    root / 'adapters' / 'opencode' / 'workflows' / 'orchestration-engine.md',
    root / 'adapters' / 'cursor' / '.cursor' / 'README.md',
    root / 'adapters' / 'claude-code' / 'CLAUDE.md',
    root / 'adapters' / 'codex' / 'AGENTS.md',
    root / 'core' / 'README.md',
]
required_dirs = [
    root / 'references',
    root / 'benchmarks',
    root / 'knowledge' / 'failures',
    root / 'knowledge' / 'patterns',
    root / 'knowledge' / 'evolution',
    root / 'knowledge' / 'decisions',
    root / 'knowledge' / 'design-intent',
    root / 'knowledge' / 'architecture-patterns',
    root / 'knowledge' / 'agents',
    root / 'knowledge' / 'refactoring',
    root / 'knowledge' / 'prompts',
    root / 'knowledge' / 'ux-laws',
    root / 'knowledge' / 'anti-patterns',
    root / 'knowledge' / 'migration-intelligence',
    root / 'knowledge' / 'adrs',
    root / 'knowledge' / 'success-patterns',
    root / 'knowledge' / 'world-class-enhancements',
    root / 'compliance',
    root / 'results',
    root / 'reports',
    root / 'governance',
    root / 'agents',
    root / 'core',
    root / 'adapters',
    root / 'compatibility',
    root / 'memory',
    root / 'patterns',
    root / 'reviews',
    root / 'workflows',
]

missing = [str(p.relative_to(root)) for p in required_files if not p.exists()]
missing += [str(p.relative_to(root)) for p in required_dirs if not p.is_dir()]
if missing:
    raise SystemExit('Missing required paths: ' + ', '.join(missing))

skill_text = (root / 'SKILL.md').read_text(encoding='utf-8')
for phrase in [
    'description: Use when',
    'DMW Product Engineering OS',
    'not affiliated with, endorsed by, sponsored by, authorized by, or associated with Adobe Inc.',
    'design-source agnostic',
    'Do not ask the user to migrate away from their source of truth',
    'OpenAI Codex',
    'Progressive disclosure map',
    'CONFIRMED',
    'INFERRED',
    'ASSUMED',
    'UNKNOWN',
    'XD_DESIGN_CRITIC',
    'XD_PRINCIPAL_ENGINEER',
    'World-class gate',
    'Architecture pattern rule',
    'Elite intelligence rule',
    'scripts/benchmark_intelligence.py',
    'Benchmark intelligence rule',
    'Final foundation rule',
    'governance/CONSTITUTION.md',
    'compatibility/routing-matrix.md',
    'Platform architecture',
    'XD_EXECUTIVE_REVIEWER',
    'XD_SIMPLICITY_ADVOCATE',
    'XD_FUTURE_PROOFING_AGENT',
    'Decision and intent memory',
    'XD_COUNCIL',
    'XD_COST_ANALYST',
    'XD_PRODUCT_STRATEGIST',
    'XD_SECURITY_ARCHITECT',
]:
    if phrase not in skill_text:
        raise SystemExit(f'SKILL.md missing phrase: {phrase}')

readme_text = (root / 'README.md').read_text(encoding='utf-8')
for phrase in [
    'DMW Product Engineering OS',
    'not affiliated with, endorsed by, sponsored by, authorized by, or associated with Adobe Inc.',
    'DISCLAIMER.md',
    'TRADEMARK.md',
    'design-source-agnostic product engineering intelligence platform',
]:
    if phrase not in readme_text:
        raise SystemExit(f'README.md missing phrase: {phrase}')

disclaimer_text = (root / 'DISCLAIMER.md').read_text(encoding='utf-8')
for phrase in [
    'independent project created and maintained by Davis Materialworks',
    'The inclusion of Adobe XD support should not be interpreted as a partnership',
    'Future Design Sources',
]:
    if phrase not in disclaimer_text:
        raise SystemExit(f'DISCLAIMER.md missing phrase: {phrase}')

modules = list((root / 'references').rglob('*.md'))
if len(modules) < 15:
    raise SystemExit('Expected at least 15 reference modules')

benchmarks = [p for p in (root / 'benchmarks').glob('*/benchmark.json') if not p.parent.name[:2].isdigit()]
if len(benchmarks) < 7:
    raise SystemExit(f'Expected at least 7 reference benchmarks, found {len(benchmarks)}')

patterns = list((root / 'knowledge' / 'patterns').glob('*.md'))
if len(patterns) < 10:
    raise SystemExit(f'Expected at least 10 design patterns, found {len(patterns)}')

compliance = [p for p in (root / 'compliance').iterdir() if p.is_dir()]
if len(compliance) < 8:
    raise SystemExit(f'Expected at least 8 compliance packs, found {len(compliance)}')

print(f'OK: {len(modules)} reference modules, {len(benchmarks)} benchmarks, {len(patterns)} patterns, {len(compliance)} compliance packs found.')


architecture_patterns = list((root / 'knowledge' / 'architecture-patterns').glob('*.md'))
if len(architecture_patterns) < 7:
    raise SystemExit(f'Expected at least 7 architecture patterns, found {len(architecture_patterns)}')

agent_contracts = list((root / 'knowledge' / 'agents').glob('*.md'))
if len(agent_contracts) < 4:
    raise SystemExit(f'Expected at least 4 agent contracts, found {len(agent_contracts)}')


ux_laws = list((root / 'knowledge' / 'ux-laws').glob('*.md'))
if len(ux_laws) < 7:
    raise SystemExit(f'Expected at least 7 UX laws, found {len(ux_laws)}')

anti_patterns = list((root / 'knowledge' / 'anti-patterns').glob('*.md'))
if len(anti_patterns) < 6:
    raise SystemExit(f'Expected at least 6 anti-patterns, found {len(anti_patterns)}')

migration_playbooks = list((root / 'knowledge' / 'migration-intelligence').glob('*.md'))
if len(migration_playbooks) < 5:
    raise SystemExit(f'Expected at least 5 migration playbooks, found {len(migration_playbooks)}')


bootstrap_benchmarks = list((root / 'benchmarks').glob('[0-9][0-9]-*/benchmark.json'))
if len(bootstrap_benchmarks) < 10:
    raise SystemExit(f'Expected at least 10 bootstrap benchmark projects, found {len(bootstrap_benchmarks)}')
