# Settings Pattern

## Recognition Signals
- preferences
- profile
- account
- security
- notifications
- billing settings

## Expected Components
- SettingsLayout
- SettingsSection
- PreferenceToggle
- DangerZone

## Component Metadata Schema Example
```json
{
  "component": "SettingsLayout",
  "industry": "Pattern-dependent",
  "accessibility": [
    "section headings",
    "toggle labels",
    "confirmation dialogs",
    "status feedback"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "save success",
    "validation",
    "permission denied",
    "destructive cancel"
  ]
}
```

## Accessibility Obligations
- section headings
- toggle labels
- confirmation dialogs
- status feedback

## Testing Obligations
- save success
- validation
- permission denied
- destructive cancel

## Critic Guidance
Challenge settings that bury critical controls or mix destructive actions with routine edits.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
