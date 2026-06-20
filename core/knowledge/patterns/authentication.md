# Authentication Pattern

## Recognition Signals
- login
- signup
- forgot password
- MFA
- session timeout
- SSO

## Expected Components
- AuthLayout
- LoginForm
- PasswordField
- MfaChallenge
- SessionTimeoutDialog

## Component Metadata Schema Example
```json
{
  "component": "AuthLayout",
  "industry": "Pattern-dependent",
  "accessibility": [
    "labels",
    "error association",
    "password visibility label",
    "focus first invalid field"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "invalid credentials",
    "locked account",
    "MFA required",
    "password reset"
  ]
}
```

## Accessibility Obligations
- labels
- error association
- password visibility label
- focus first invalid field

## Testing Obligations
- invalid credentials
- locked account
- MFA required
- password reset

## Critic Guidance
Challenge flows that hide errors, overemphasize social login, or omit recovery paths.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
