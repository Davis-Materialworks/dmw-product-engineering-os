# Frontend Architecture

## Default stack

Next.js + React + TypeScript + Tailwind + shadcn/ui.

## Structure

Prefer feature-oriented architecture:

- `app/` routes and layouts
- `components/ui/` generic primitives
- `components/design-system/` styled foundation components
- `features/<domain>/` product-specific components, hooks, schemas, and tests
- `lib/` shared utilities
- `styles/` tokens and globals

## Rules

- Keep domain logic out of generic UI primitives.
- Keep server/data concerns separated from presentational components.
- Use typed props and discriminated unions for variants/states.
- Encapsulate complex interactions in hooks or state machines.
- Avoid global CSS leaks.
