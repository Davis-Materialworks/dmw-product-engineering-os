# Generator: Next.js + React + Tailwind + shadcn/ui

## Generation order

1. Read existing project conventions.
2. Define or extend tokens.
3. Create/extend UI primitives.
4. Create feature components.
5. Create routes/layouts.
6. Add states and accessibility.
7. Add tests.
8. Run checks.

## Tailwind rules

- Prefer token classes and CSS variables.
- Avoid arbitrary values unless one-off and documented.
- Use responsive utilities deliberately.
- Keep class strings readable; use helper functions for variants.

## shadcn rules

Use shadcn/ui when it accelerates accessible primitives. Do not force it for bespoke visuals or highly custom domain components.
