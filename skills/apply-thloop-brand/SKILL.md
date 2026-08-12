---
name: apply-thloop-brand
description: Apply the complete ThLoop Continuous Core identity to websites, apps, dashboards, presentations, social assets, print, apparel, event environments, mockups, and frontend code. Use when creating, redesigning, reviewing, or auditing any ThLoop-branded visual deliverable; when the user mentions ThLoop, Continuous Core, Twin Chamber, Chicane Cut, the ThLoop palette, or asks to make a project look like the ThLoop brand. Do not use for unrelated brands or backend-only work with no visual output.
---

# Apply ThLoop Brand

Apply ThLoop as a production design system, not as a dark theme. Preserve the hierarchy: **Continuous Core wordmark** is primary, **Twin Chamber** is the only compact mark, and **Chicane Cut** is a graphic device—never a third logo.

## Required workflow

1. Inspect the requested artifact, target medium, audience, functional hierarchy, and existing brand assets.
2. Read [references/brand-foundations.md](references/brand-foundations.md) before making visual decisions.
3. Select only the references needed for the medium:
   - Web apps, dashboards, landing pages, or code: read [references/digital-ui.md](references/digital-ui.md).
   - Copy, UI labels, presentations, or campaigns: read [references/voice-content.md](references/voice-content.md).
   - Print, apparel, events, mockups, or physical applications: read [references/applications.md](references/applications.md).
   - Final review or audit: read [references/accessibility-and-qa.md](references/accessibility-and-qa.md).
   - Image-generation prompts: read [references/prompt-recipes.md](references/prompt-recipes.md).
4. Reuse canonical files from `assets/logos/` and `assets/marks/`; do not redraw, trace from reference PNGs, regenerate, or crop the wordmark/compact mark from mockups.
5. Implement with semantic tokens from `assets/tokens/`; do not scatter raw color values across components.
6. Validate contrast, responsiveness, states, asset integrity, and brand hierarchy before delivery.
7. Run `scripts/brand_audit.py <target>` on code projects and fix every error. Run `scripts/check_contrast.py` when adding a new foreground/background pairing.

## Identity hierarchy

### Continuous Core wordmark

Use the full wordmark for heroes, navigation, documents, equipment badges, boot screens, credentials, signage, and any surface wide enough to preserve legibility. Use the light asset on Loop Black and the dark asset on Technical Paper.

### Twin Chamber compact mark

Use only for favicons, app icons, avatars, garment patches, seals, folio markers, compact loading states, and spaces where the full wordmark cannot remain legible. Preserve its two chambers, lower return stroke, and gold chicane notch.

### Chicane Cut visual device

Use as a crop, divider, frame, edge intervention, transition, mask, motion path, or pattern fragment. NUNCA present it as a standalone logo, app icon, avatar, or replacement for Twin Chamber.

## Non-negotiable rules

- ALWAYS preserve the exact geometry and aspect ratio of canonical SVG assets.
- ALWAYS keep Chicane Gold rare: normally 1–3% of the composition; never exceed 5% without explicit approval.
- ALWAYS make function the source of visual hierarchy.
- ALWAYS use real domain copy and realistic states; never use lorem ipsum.
- ALWAYS implement initial, loading, success, error, empty, disabled, hover, active, and focus states when relevant.
- ALWAYS provide visible keyboard focus and WCAG AA contrast.
- NEVER use gradients, neon, glow, glassmorphism, purple/cyan technology clichés, decorative circuit boards, infinity symbols, generic code brackets, or gaming/esports styling.
- NEVER wrap every block in a card. Prefer typography, spacing, alignment, surface shifts, and hairline dividers.
- NEVER enlarge the gold notch into a stripe, fill, or dominant panel.
- NEVER alter the spelling or capitalization of `ThLoop`.
- NEVER place the wordmark inside another badge or enclosing shape.
- NEVER recreate logos with fonts, image generation, or improvised paths when canonical assets are available.

## Asset selection

Use [references/asset-catalog.md](references/asset-catalog.md) to choose the correct source file. Prefer SVG for interfaces, print, and scalable deliverables. Use PNG only when the target cannot accept SVG. Copy assets into the output project instead of linking to this skill directory.

## Frontend implementation

1. Copy `assets/tokens/thloop.css` or adapt `assets/tokens/thloop.tokens.json` to the existing token architecture.
2. Copy only needed brand assets; preserve descriptive filenames.
3. Reuse templates from `assets/templates/react/` when the stack is React/Next.js.
4. Build mobile-first at 375px, then verify 768px and 1440px.
5. Keep Server Components by default in Next.js; isolate interactive Client Components.
6. Animate only `transform` and `opacity`; respect `prefers-reduced-motion`.
7. Use Twin Chamber for icons only when it communicates brand identity—not as a decorative icon beside every title.

## Output contract

Deliver the finished artifact, not only recommendations. State which canonical assets and tokens were used. If the canonical logo cannot be embedded in a target format, explain the limitation and provide the closest lossless alternative. Do not claim exact brand compliance if any logo was regenerated rather than reused.
