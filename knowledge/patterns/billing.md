# Billing Pattern

## Recognition Signals
- plan
- invoice
- payment method
- usage
- upgrade
- subscription

## Expected Components
- PlanCard
- InvoiceTable
- UsageMeter
- PaymentMethodPanel

## Component Metadata Schema Example
```json
{
  "component": "PlanCard",
  "industry": "Pattern-dependent",
  "accessibility": [
    "price labels",
    "renewal terms",
    "error association",
    "not color-only"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "upgrade",
    "payment failure",
    "invoice download",
    "usage limit"
  ]
}
```

## Accessibility Obligations
- price labels
- renewal terms
- error association
- not color-only

## Testing Obligations
- upgrade
- payment failure
- invoice download
- usage limit

## Critic Guidance
Challenge dark patterns, unclear renewal pricing, and cancellation friction.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
