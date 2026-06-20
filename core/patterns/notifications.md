# Notifications Pattern

## Recognition Signals
- bell
- inbox
- toast
- alert
- unread
- preferences

## Expected Components
- NotificationBell
- NotificationList
- Toast
- PreferenceCenter

## Component Metadata Schema Example
```json
{
  "component": "NotificationBell",
  "industry": "Pattern-dependent",
  "accessibility": [
    "unread count label",
    "live region restraint",
    "dismiss buttons",
    "focus management"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "new notification",
    "mark read",
    "dismiss",
    "preference toggle"
  ]
}
```

## Accessibility Obligations
- unread count label
- live region restraint
- dismiss buttons
- focus management

## Testing Obligations
- new notification
- mark read
- dismiss
- preference toggle

## Critic Guidance
Challenge noisy notifications and alerts that interrupt critical workflows.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
