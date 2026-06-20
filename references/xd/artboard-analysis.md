# XD Artboard Analysis

Analyze artboards as product states, not static pictures.

## Artboard classification

Classify each artboard into one or more roles:

- entry point
- onboarding
- authentication
- dashboard
- list/index
- detail view
- creation/editing flow
- checkout/payment
- settings
- empty state
- loading state
- error state
- success/completion
- permission or consent
- admin/control panel
- notification/alert

## Flow reconstruction

Infer flow from naming, order, prototype wires, repeated layout, CTA labels, and visual progression. Build a flow graph:

- nodes: artboards/screens/states
- edges: user actions, automatic transitions, failure paths
- guards: auth, permissions, validation, payment, subscription status
- outcomes: success, abandonment, retry, escalation

## Expert heuristics

- A repeated header/sidebar indicates persistent app shell.
- Similar artboards with changed content often indicate component states rather than separate pages.
- Modal-like artboards should become dialog/sheet components, not routes, unless they have shareable state.
- Blank screens are usually missing empty/loading/error states; flag them.
- Marketing pages need content hierarchy and conversion flow analysis.
- Enterprise dashboards require data density, filtering, permissions, export, and audit behavior.

## Output contract

For each analyzed artboard produce:

- role
- route/component recommendation
- primary user goal
- primary action
- secondary actions
- data dependencies
- states required
- accessibility risks
- responsive risks
- implementation notes
