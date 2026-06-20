# Onboarding Pattern

## Recognition Signals
- welcome
- tour
- setup
- profile
- import
- connect account

## Expected Components
- OnboardingStepper
- SetupChecklist
- ProgressIndicator
- SkipLink

## Component Metadata Schema Example
```json
{
  "component": "OnboardingStepper",
  "industry": "Pattern-dependent",
  "accessibility": [
    "progress text",
    "skip path",
    "keyboard paging",
    "reduced motion"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "skip",
    "resume",
    "back",
    "incomplete required step"
  ]
}
```

## Accessibility Obligations
- progress text
- skip path
- keyboard paging
- reduced motion

## Testing Obligations
- skip
- resume
- back
- incomplete required step

## Critic Guidance
Challenge onboarding that blocks value, has unclear completion, or uses motion as instruction.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
