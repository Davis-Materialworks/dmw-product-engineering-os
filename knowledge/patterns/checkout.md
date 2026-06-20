# Checkout Pattern

## Recognition Signals
- cart
- shipping
- billing
- payment
- coupon
- order review

## Expected Components
- CartSummary
- CheckoutStep
- PaymentMethodForm
- OrderReview

## Component Metadata Schema Example
```json
{
  "component": "CartSummary",
  "industry": "Pattern-dependent",
  "accessibility": [
    "fieldsets",
    "error summaries",
    "step labels",
    "focus invalid field"
  ],
  "performance": [
    "avoid unnecessary re-rendering",
    "preserve responsive stability"
  ],
  "testing": [
    "coupon failure",
    "payment decline",
    "address validation",
    "order confirmation"
  ]
}
```

## Accessibility Obligations
- fieldsets
- error summaries
- step labels
- focus invalid field

## Testing Obligations
- coupon failure
- payment decline
- address validation
- order confirmation

## Critic Guidance
Challenge hidden fees, weak review steps, and payment flows without recovery.

## Prevention Rule
Recognize this pattern from XD labels, repeated structures, controls, and flow position before extracting components or architecture.
