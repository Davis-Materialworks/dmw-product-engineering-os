# Admin Pattern

## Recognition Signals
- users
- roles
- permissions
- audit log
- bulk action
- SSO
- SCIM

## Expected Components
- AdminShell
- UserTable
- RoleEditor
- PermissionMatrix
- AuditLog

## Component Metadata Schema Example
```json
{
  "component": "AdminShell",
  "industry": "Pattern-dependent",
  "accessibility": [
    "grid semantics",
    "bulk selection labels",
    "confirmation dialogs",
    "table captions"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "permission denied",
    "bulk action",
    "audit event",
    "role change conflict"
  ]
}
```

## Accessibility Obligations
- grid semantics
- bulk selection labels
- confirmation dialogs
- table captions

## Testing Obligations
- permission denied
- bulk action
- audit event
- role change conflict

## Critic Guidance
Challenge admin designs without least privilege, audit trails, or recovery paths.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
