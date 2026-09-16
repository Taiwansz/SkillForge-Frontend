# THP / ThPay digital UI system

## Token integration

Import `assets/tokens/thpay.css` globally or map `assets/tokens/thpay.tokens.json` into the existing design-token architecture. Bind components to semantic tokens such as `--thp-bg`, `--thp-surface`, `--thp-text`, `--thp-action` and `--thp-border`; avoid scattering palette hex values throughout code.

## Product principle

The interface must feel friendly to a payroll analyst who is not from IT and equally understandable to an employee using the self-service portal. Complexity belongs in the system, not in the user's head.

## Page architecture

### DP / RH workspace

Use a stable app shell:

- compact left navigation or top navigation;
- clear page title + competence/context selector;
- one summary region for status and key actions;
- working area for tables, payroll cycles, exceptions and detailed data;
- contextual drawer for employee/payslip inspection when useful.

Avoid huge dark canvases. Default to Warm Ivory/white working surfaces, Ink Navy text and a restrained dark anchor in the nav or key brand regions.

### Employee portal

Prioritize the employee's tasks:

1. next/available payslip;
2. benefits and allowed choices;
3. requests/tickets;
4. personal data/documents;
5. clear status and effective date of requested changes.

Use larger spacing and simpler language than the analyst view.

## Components

### Buttons

- Primary: Ink Navy or Cobalt fill with high-contrast text.
- Secondary: white/ivory surface with Line border and Ink Navy text.
- Soft action: pale Mint/Blush/Cobalt tint only when emphasis is low.
- Destructive: semantic red, never Coral merely because it is a brand color.
- Minimum target: 44×44px.

### Inputs

- Always show persistent labels.
- Use white/ivory fields, Line border and strong focus ring in Cobalt.
- Keep helper and validation messages close to the field.
- Currency, date and percentage fields must show formatting examples or masks.

### Cards and surfaces

Use cards for grouping, not decoration. Recommended radius 16–20px. Prefer one surface containing related data over multiple nested cards. Flat surface shifts and dividers come before shadows.

### Data tables

- 44–52px row height by default.
- Sticky headers for long payroll lists.
- Tabular numbers and right alignment for currency.
- Clear row hover, selected and keyboard focus states.
- Persist filters and sorting when navigating to a detail drawer.
- Never clip columns on mobile: switch to stacked records or explicit horizontal scroll with frozen identity column.

### Status

Use text + icon + color. Example labels: `Concluído`, `Em conferência`, `Aguardando documento`, `Rejeitado pelo eSocial`, `Programado`. Never communicate status only by hue.

## Dashboards

Structure information in four levels:

1. readiness / payroll health;
2. blockers and exceptions;
3. key totals and trends;
4. operational detail.

Avoid a wall of KPI cards. A payroll dashboard should help the analyst decide what needs attention next.

## Motion

- Microinteraction: 140–200ms ease-out.
- Drawer/panel: 220–300ms cubic-bezier(0.16, 1, 0.3, 1).
- Brand motion: connection blocks slide or hand off into one another; no infinite loop gimmicks.
- Animate transform/opacity where possible.
- Honor `prefers-reduced-motion`.

## Responsive behavior

Verify at 375, 768, 1024 and 1440px.

- Navigation collapses before content becomes cramped.
- Tables become stacked records or controlled horizontal scroll.
- Drawers become full-screen sheets on narrow mobile.
- Do not reduce body text below 14px; prefer 15–16px for employee-facing flows.
- Zoom at 50%, 100%, 125% and 200% must not cause overlap or clipped actions.
- No fixed heights for content-rich cards.

## Dark theme

Dark mode is optional, not the identity default. When requested, use Ink Navy as the base, a slightly lighter navy surface and preserve Cobalt/Mint/Blush accents. Never simply invert all colors. Payroll tables and long-form content must retain readable contrast and restrained saturation.
