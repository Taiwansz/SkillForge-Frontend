---
name: apply-thpay-brand
description: Apply the complete THP / ThPay visual identity to payroll products, employee portals, dashboards, websites, presentations, social assets, mockups, and frontend code. Use when creating, redesigning, reviewing, or auditing anything branded THP or ThPay; when the user asks for the friendly human-centered payroll identity, the modular THP mark, the People Move Tomorrow system, or the ThPay palette. Do not use for unrelated brands or backend-only work with no visual output.
---

# Apply THP / ThPay Brand

Apply THP as a **friendly payroll product system**, not as generic fintech styling. The brand must balance operational credibility with human warmth. The product can handle complex payroll, compliance, benefits, eSocial, audit, employee self-service and service desk without making the interface feel intimidating.

## Required workflow

1. Inspect the requested artifact, medium, audience, user role, information density and existing assets.
2. Read `references/brand-foundations.md` before making visual decisions.
3. Read only the references needed for the task:
   - Web apps, dashboards, portals or frontend code: `references/digital-ui.md`.
   - Payroll, HR, benefits, employee and compliance flows: `references/payroll-domain.md`.
   - Copy, labels, campaigns and presentations: `references/voice-content.md`.
   - Physical or campaign applications: `references/applications.md`.
   - Image generation: `references/prompt-recipes.md`.
   - Final review: `references/accessibility-and-qa.md`.
4. Reuse canonical assets from `assets/logos/`, `assets/marks/` and `assets/visual/`. Do not redraw them from screenshots or regenerate them with an image model.
5. Implement colors and spacing through semantic tokens from `assets/tokens/`.
6. Make the default product experience light, calm, responsive and readable. Dark navy is an anchor color, not the default canvas for every screen.
7. Validate contrast, states, responsiveness, asset integrity and brand hierarchy before delivery.
8. When working on code, run `scripts/brand_audit.py <target>` and `scripts/check_contrast.py` before calling the result brand-compliant.

## Identity hierarchy

### Primary lockup

Use the modular THP symbol plus the `ThPay` wordmark for navigation, heroes, documents, login screens, presentations and broad brand signatures. Use the dark-text asset on ivory/light surfaces and the light-text asset on navy/dark surfaces.

### Modular THP symbol

The symbol is built from rounded connected modules. It represents technology, humanity, people and processes working together. Preserve its geometry, overlap order and color relationships. It may be used alone in square brand spaces when the product context already identifies ThPay.

### Connector T compact mark

The compact `T` module is reserved for app icons, favicons, tiny avatars and constrained square spaces. It is not a decorative icon to repeat beside every heading.

### Connection Blocks graphic language

Rounded blocks, bridges, arches and partial overlaps are the brand's visual grammar. They can become patterns, section crops, illustration frames, background fields and motion transitions. They must never compete with content.

## Non-negotiable rules

- ALWAYS prioritize people and task clarity over visual spectacle.
- ALWAYS use warm ivory or white-adjacent surfaces for dense operational work.
- ALWAYS preserve the exact proportions of canonical logo SVGs.
- ALWAYS pair status color with text or icon meaning.
- ALWAYS use realistic Brazilian payroll/HR copy; never lorem ipsum.
- ALWAYS provide loading, success, error, empty, disabled, hover, active and focus states when relevant.
- ALWAYS support keyboard focus and WCAG AA contrast for functional UI.
- NEVER make the product dark-by-default unless the user explicitly requests a dark theme.
- NEVER use generic bank/fintech symbols such as currency signs, wallets, credit cards, shields or stock-market arrows as brand identifiers.
- NEVER use neon, cyberpunk, glassmorphism, excessive gradients, glowing borders or purple/blue AI clichés.
- NEVER make every module a floating card. Use section grouping, whitespace, dividers and surface shifts first.
- NEVER turn the pastel palette into a childish toy aesthetic. Keep typography, spacing and data presentation professional.
- NEVER alter the spelling `ThPay` or replace the canonical lockup with improvised text artwork.

## Friendly product behavior

Friendly does not mean low-information. It means the system explains itself, reveals complexity progressively and makes consequences clear. Prefer plain-language labels, contextual summaries, sensible defaults, visible next steps and confirmation before high-impact payroll actions.

For DP/RH screens, keep professional density with readable tables and strong hierarchy. For the employee portal, increase spacing, simplify terminology and prioritize personal actions: holerite, benefits, requests, documents and support.

## Frontend implementation

1. Copy `assets/tokens/thpay.css` or map `assets/tokens/thpay.tokens.json` to the project token layer.
2. Copy only the brand assets required by the project; preserve filenames.
3. Use `assets/templates/react/` for React/Next.js implementations.
4. Design mobile-first at 375px, then verify 768px, 1024px and 1440px.
5. Keep touch targets at least 44×44px.
6. Prefer `transform` and `opacity` for motion and honor `prefers-reduced-motion`.
7. Use semantic data colors independently from brand colors when meaning requires it.

## Output contract

Deliver the finished artifact, not only recommendations. State which canonical assets and tokens were used. If a target format cannot embed the vector logo, export from the canonical SVG rather than recreating the mark. Do not claim exact brand compliance if the official asset was regenerated or manually approximated.
