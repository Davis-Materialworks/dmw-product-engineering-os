# Healthcare Patient Portal — Design Specification

## Product Context
Patient-facing web portal for a regional healthcare network. Patients log in to view upcoming appointments, manage medications, review lab results with clinical interpretations, message their care team, and access visit summaries. High stakes for accuracy, privacy, and accessibility.

## User Goals
- See upcoming appointments with date, provider, location, and prep instructions
- Review medication list with dosage, schedule, refill status, and interaction warnings
- View lab results with reference ranges, trend indicators, and clinician annotations
- Send and receive secure messages with care team members
- Download visit summaries and share with external providers

## Color Palette
| Token | Hex | Usage |
|---|---|---|
| `surface.page` | `#F1F5F9` | Page background |
| `surface.card` | `#FFFFFF` | Cards, panels, message bubbles |
| `text.primary` | `#0F172A` | Headings, body, critical info |
| `text.secondary` | `#475569` | Labels, metadata, non-critical text |
| `action.primary.bg` | `#0284C7` | Primary buttons (Book, Send, Request) |
| `action.primary.hover` | `#0369A1` | Hover state |
| `feedback.critical` | `#DC2626` | Abnormal lab results, emergency banner |
| `feedback.warning` | `#D97706` | Borderline results, expiring prescriptions |
| `feedback.normal` | `#16A34A` | Normal results, confirmed appointments |
| `feedback.info` | `#2563EB` | Informational banners, non-urgent messages |
| `focus.ring` | `#0284C7` | Focus indicator |

## Typography Scale
| Token | Size / Line | Weight | Usage |
|---|---|---|---|
| `heading.page` | 26px / 1.2 | 700 | Portal section titles |
| `heading.section` | 18px / 1.3 | 600 | Card titles, appointment dates |
| `body.default` | 16px / 1.6 | 400 | Body copy, message text, visit notes |
| `label.field` | 13px / 1.4 | 600 | Form labels, table headers |
| `display.lab-value` | 20px / 1.2 | 600 | Lab result values |
| `caption.clinical` | 12px / 1.4 | 400 | Reference ranges, timestamps, units |
| Font family: system-ui stack (SF Pro Text on iOS/macOS, Segoe UI on Windows, Roboto on Android) |

## Component Inventory
- **PatientHeader** — Patient name, DOB, MRN, primary provider, allergies badge (critical warning if present)
- **AppointmentCard** — Date/time, provider name + photo, location with map link, visit type, prep instructions, "Add to calendar" action
- **MedicationList** — Grouped by active/discontinued; each row: drug name, dosage, frequency, refill status, interaction warning icon
- **LabResultsTable** — Test name, result value, reference range, trend arrow (since last result), clinical flag (Normal/Borderline/Abnormal), date collected
- **LabResultDetail** — Expanded panel: result history chart (sparkline), clinician note, "Download PDF" action, share button
- **MessageThread** — Secure inbox UI: conversation list (left panel), message thread (right panel), compose input with attachment support, unread badges
- **VisitSummaryCard** — Collapsible accordion: diagnosis codes, procedures, medications prescribed, follow-up instructions, provider signature
- **AlertBanner** — Dismissible site-wide banner for critical lab results, appointment reminders, or portal messages

## Layout Structure
```
┌──────────────────────────────────────────────┐
│  PORTAL HEADER (PatientHeader + AlertBanner) │
├─────────┬────────────────────────────────────┤
│ NAV     │  CONTENT AREA                      │
│ - Home  │  ┌───────────────────────────────┐ │
│ - Appts │  │ SECTION TITLE       [Action]  │ │
│ - Meds  │  ├───────────────────────────────┤ │
│ - Labs  │  │ AppointmentCard × N           │ │
│ - Msgs  │  │ MedicationList                │ │
│ - Visits│  │ LabResultsTable               │ │
│         │  │ MessageThread                 │ │
└─────────┴────────────────────────────────────┘
```

## Responsive Behavior
- **1024px+**: Persistent sidebar nav (200px), content area with card grid
- **768–1023px**: Collapsible nav (hamburger), single-column cards
- **<768px**: Bottom tab bar navigation, single-column, tables become stacked card layouts, MessageThread becomes single-panel (tap to toggle list/thread)

## State Descriptions
- **Loading**: Skeleton placeholders matching card shapes; nav disabled; header shows patient name immediately if cached
- **Empty appointments**: Illustrated state "No upcoming appointments" with "Schedule one" CTA button
- **Empty messages**: "No messages" with "Contact your care team" link
- **Critical lab result**: AlertBanner at top (red, non-dismissible), affected row highlighted in LabResultsTable, "Reviewed by Dr. [Name]" timestamp
- **Medication interaction**: Warning icon with tooltip; clicking opens interaction detail panel
- **Message send failure**: Inline error, message preserved in compose field, retry button
- **Session timeout**: Modal overlay "Your session will expire in 2 minutes. Extend session?" with countdown; auto-logout after expiry

## HIPAA / Security Requirements
- All PHI (name, DOB, MRN, lab results, messages) encrypted in transit (TLS 1.3) and at rest (AES-256)
- Session timeout: 15 minutes idle, 4 hours absolute max; re-authentication required for sensitive actions
- Audit logging: every record view, message read, and download action is logged with timestamp and user identity
- Role-based access: patient sees own records only; provider sees assigned patients; admin has full access with audit trail
- PHI never appears in URLs, query strings, or client-side analytics

## Accessibility Requirements
- WCAG 2.2 AA compliance mandatory; AAA for color contrast on clinical data
- Lab results: abnormal flags include both color (red) AND text label ("Abnormal — above reference range") — never color alone
- Data tables: `<caption>`, `<th scope="row|col">`, `aria-sort` for sortable columns
- All form fields: visible `<label>`, error messages linked via `aria-describedby`
- Keyboard: full portal navigable without mouse; skip-to-content link; visible focus ring on all interactive elements
- Screen reader: medication interactions announced via `aria-live="polite"`; critical alerts via `role="alert"`