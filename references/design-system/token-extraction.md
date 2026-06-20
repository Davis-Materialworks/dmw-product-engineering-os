# Token Extraction Engine

Create a durable token system from XD assets and observed values.

## Token levels

1. Primitive: raw values.
2. Semantic: purpose-based aliases.
3. Component: component-specific aliases.
4. State: hover, pressed, disabled, focus, error.
5. Mode: light, dark, high-contrast, brand themes.

## Scales

Infer scales for:

- color
- typography
- spacing
- radius
- elevation
- opacity
- z-index
- motion duration/easing
- border width

## Quality rules

- Do not create a token for every one-off value.
- Cluster near-duplicates and recommend cleanup.
- Preserve brand-critical values.
- Use semantic tokens in components.
- Emit JSON-friendly names and Tailwind-compatible names when relevant.

## Example

```json
{
  "color": {
    "primitive": { "blue-600": "#2563EB" },
    "semantic": { "action-primary-bg": "{color.primitive.blue-600}" }
  }
}
```
