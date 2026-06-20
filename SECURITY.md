# Security Policy

DMW Product Engineering OS is a documentation, benchmark, governance, and agent-workflow repository. It may influence generated application architecture and implementation, so security issues in rules, prompts, workflows, examples, or automation should be treated seriously.

## Supported Versions

The `main` branch is the active supported version unless a separate release branch is published.

## Reporting A Vulnerability

If you find a security issue, please do not publish exploit details in a public issue.

Report vulnerabilities privately to **security@davismaterialworks.com**. We will acknowledge within 5 business days. Please do not open public issues for security vulnerabilities.

Include:

- A clear description of the issue
- Affected files, workflows, prompts, scripts, or benchmark data
- Potential impact
- Reproduction steps when safe to share
- Suggested mitigation if known

### Safe Harbor

We will not pursue legal action against researchers who follow this disclosure policy for good-faith reports. We consider security research conducted in accordance with this policy to be:

- Authorized under applicable anti-hacking laws
- Exempt from restrictions in our Terms of Service that would otherwise prohibit such activity
- Conducted in good faith when you give us reasonable time to address the issue before public disclosure

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
