# Design System Package

## Use When
Use when the design system must be distributed as a versioned, consumable package across multiple projects or teams. Applies when design tokens, components, and documentation are shared via npm, Maven, CocoaPods, or similar registry.

## Avoid When
Avoid when the design system serves a single project with no cross-team reuse, or when the overhead of package versioning, publishing, and consumer updates exceeds the coordination benefit.

## XD-to-Code Application
- **Token extraction**: Extract design tokens from XD character styles, color swatches, and layout grids into a platform-agnostic token format (DTCG, Style Dictionary, or custom JSON). Map primitive tokens (raw values from XD) to semantic tokens (purpose-driven names) before publishing.
- **Component library structure**: Organize components by domain and atomicity — atoms (Button, Input, Icon), molecules (FormField, SearchBar), and organisms (DataTable, FilterPanel). Each component package exports typed props, accessibility contracts, and state variants.
- **Package publishing**: Version packages with semantic versioning and publish to a private or public registry. Each release must include changelogs, migration guides for breaking changes, and updated token definitions. Consuming projects import version-locked packages rather than copying source.
- **Drift prevention**: Periodically compare consuming project token and component usage against the published package. Flag drift where projects use raw values, override package styles, or fall behind the latest version.

## Review Questions
- Does this pattern reduce token duplication across projects?
- Can consumers adopt new versions without manual migration?
- Are component contracts typed, documented, and covered by visual regression tests?
- What simpler approach (shared config, copy-paste with linting) was considered and rejected?