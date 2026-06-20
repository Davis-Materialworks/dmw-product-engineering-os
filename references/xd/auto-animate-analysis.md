# XD Auto-Animate and Prototype Motion

Translate prototype intent into production motion with restraint.

## Motion intent taxonomy

- continuity: preserve object identity across screens
- feedback: confirm interaction
- orientation: show where the user is in a flow
- hierarchy: reveal priority
- causality: show action-result relationship
- delight: add polish without blocking task completion

## XD to implementation mapping

- position change -> transform translate
- size change -> scale or layout transition
- opacity change -> fade
- rotation -> transform rotate
- overlay reveal -> dialog/sheet/popover transition
- drag -> gesture-driven motion
- timed transition -> onboarding/demo/auto-advance only when user control remains clear

## Libraries

Web: Framer Motion, Motion One, CSS transitions.
React Native: Reanimated.
Flutter: AnimationController, AnimatedContainer, Hero.
SwiftUI: matchedGeometryEffect, withAnimation.

## Accessibility

Always support reduced motion. Avoid motion that conveys critical information without text/structure. Avoid dizziness-inducing parallax or large unexpected movement.
