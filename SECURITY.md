# Security Policy

DMW Product Engineering OS is a documentation, benchmark, governance, and agent-workflow repository. It may influence generated application architecture and implementation, so security issues in rules, prompts, workflows, examples, or automation should be treated seriously.

## Supported Versions

The `main` branch is the active supported version unless a separate release branch is published.

## Reporting A Vulnerability

If you find a security issue, please do not publish exploit details in a public issue.

Report security concerns through Davis Materialworks' official contact channels or by opening a minimal public issue that requests a private maintainer contact path without disclosing sensitive details.

Include:

- A clear description of the issue
- Affected files, workflows, prompts, scripts, or benchmark data
- Potential impact
- Reproduction steps when safe to share
- Suggested mitigation if known

## Security Scope

In scope:

- Unsafe generated-code guidance
- Insecure architecture recommendations
- Prompt-injection-prone workflows
- Secrets-handling mistakes
- Dangerous automation scripts
- Compliance or privacy guidance that could materially mislead users
- Security review agents that miss critical checks

Out of scope:

- Vulnerabilities in unrelated third-party products
- Issues caused by using proprietary design assets without permission
- Requests for official Adobe support or Adobe product security handling

## Security Principles

- Security and privacy are product requirements.
- Authentication, authorization, session handling, auditability, secrets handling, and API exposure must be reviewed explicitly.
- Unknown security requirements should be labeled `UNKNOWN`, not assumed safe.
- High-risk generated systems should be reviewed by `XD_SECURITY_ARCHITECT`, `XD_PRINCIPAL_ENGINEER`, `XD_RED_TEAM`, and `XD_JUDGE`.
