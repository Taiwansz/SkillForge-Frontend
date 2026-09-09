---
name: apply-toklang-brand
description: Apply the official TokLang visual identity to websites, dashboards, documentation, presentations, social assets, product UI, and developer-facing materials. Use whenever creating, reviewing, or restyling anything for TokLang, including its stacked logo, extended wordmark, TK flow icon, Industrial Pop palette, compression patterns, token-saving diagrams, and dark or light interfaces.
---

# Apply TokLang Brand

Build TokLang materials from the approved identity system instead of improvising a generic developer-tool aesthetic.

## Brand idea

TokLang turns verbose natural-language intent into compact, reversible tokens. Its visual language expresses **compression with continuity**: dense inputs flow through a narrow yellow spine and leave as a smaller, structured stream.

Use these traits together:

- technical, compact, and confident;
- curvilinear rather than rigid or engineering-like;
- expressive without becoming childish;
- high-contrast Industrial Pop color;
- visible proof of token reduction.

## Required workflow

1. Identify the output: product UI, landing page, technical diagram, document, presentation, social asset, or icon.
2. Read [references/brand-foundations.md](references/brand-foundations.md).
3. Read [references/logo-usage.md](references/logo-usage.md) before placing any brand signature.
4. Read the reference matching the task:
   - UI or landing page: [references/digital-ui.md](references/digital-ui.md)
   - pattern or illustration: [references/patterns-and-illustration.md](references/patterns-and-illustration.md)
   - animation: [references/motion.md](references/motion.md)
   - writing or labels: [references/voice-content.md](references/voice-content.md)
   - applications or mockups: [references/applications.md](references/applications.md)
   - prompts for image tools: [references/prompt-recipes.md](references/prompt-recipes.md)
5. Reuse canonical files from `assets/`; do not redraw the icon or invent a new logo.
6. Use semantic tokens from `assets/tokens/toklang.css` or `toklang.tokens.json`.
7. Run the relevant checks in `scripts/` before delivery.

## Asset hierarchy

- Primary signature: `assets/png/toklang-stacked-industrial.png`
- Extended signature: `assets/png/toklang-extended-industrial.png`
- Compact mark: `assets/marks/toklang-flow-light.svg` or `toklang-flow-dark.svg`
- Favicon: `assets/icons/favicon.svg`
- Product icon: `assets/icons/app-icon.svg`
- Decorative system: `assets/visual/`
- Reference boards: `assets/reference/`

The approved PNG signatures are the exact visual masters selected during identity development. The supplied SVG signatures are deterministic UI-ready constructions. Preserve their proportions and never replace them with typed text.

## Non-negotiables

- Spell the product **TokLang** exactly.
- Keep safety yellow `#FFD324` as the compression signal, not a general background color.
- Use deep wine `#4A1824` instead of generic black for large brand fields.
- Prefer brushed silver `#D9DADC` to plain gray in light compositions.
- Preserve clear space equal to the yellow spine width around logos.
- Use the compact mark below 120 px; do not squeeze the full wordmark into tiny spaces.
- Do not use neon green, default SaaS blue, purple gradients, circuit-board clichés, robots, angle brackets, or generic code icons.
- Do not fill every surface with patterns. Decorative density must fall away near copy and controls.
- Token metrics must be real or clearly labeled as illustrative.

## Delivery checklist

- Brand signature is a supplied asset.
- Palette uses semantic tokens.
- Light and dark states preserve contrast.
- Layout includes breathing room around curved elements.
- At least one visual communicates compression, mapping, or reversible flow when conceptually relevant.
- Mobile, reduced-motion, and keyboard-focus states are covered for interactive work.
- Run `python scripts/validate_assets.py`.
- Run `python scripts/check_contrast.py` for new color combinations.
- Run `python scripts/brand_audit.py <target>` for web or document source files.

See [references/asset-catalog.md](references/asset-catalog.md) for the full inventory.
