# ThLoop asset catalog

## Canonical assets

| Path | Use |
|---|---|
| `assets/logos/thloop-continuous-core-light.svg` | Full wordmark on dark surfaces |
| `assets/logos/thloop-continuous-core-dark.svg` | Full wordmark on light surfaces |
| `assets/logos/thloop-continuous-core-mono.svg` | Production/engraving; color controlled by CSS |
| `assets/marks/twin-chamber-light.svg` | Compact mark on dark surfaces |
| `assets/marks/twin-chamber-dark.svg` | Compact mark on light surfaces |
| `assets/marks/twin-chamber-mono.svg` | Small production use; color controlled by CSS |
| `assets/visual/chicane-cut-light.svg` | Large device on dark surface |
| `assets/visual/chicane-cut-dark.svg` | Large device on light surface |
| `assets/visual/chicane-divider.svg` | Section divider |
| `assets/visual/chicane-pattern.svg` | Repeating pattern source |
| `assets/icons/favicon.svg` | Browser favicon |
| `assets/icons/app-icon.svg` | Opaque square app/touch icon source; rounded keyline is internal artwork, not alpha |
| `assets/png/*.png` | Raster fallbacks and common export sizes |
| `assets/reference/thloop-brand-system.png` | Brand-system presentation generated from canonical assets |
| `assets/reference/thloop-applications.png` | Deterministic applications using embedded canonical assets |
| `assets/reference/mockups/equipment-kit.png` | Compatibility alias for the deterministic brand-system board |
| `assets/reference/mockups/apparel.png` | Compatibility alias for exact-master applications; no AI-interpreted lettering |
| `assets/reference/mockups/digital-system.png` | Compatibility alias for exact-master applications; no AI-interpreted lettering |
| `assets/reference/mockups/hackathon-space.png` | Compatibility alias for exact-master applications; no AI-interpreted lettering |

## Tokens and templates

| Path | Use |
|---|---|
| `assets/tokens/thloop.css` | CSS custom properties and base theme |
| `assets/tokens/thloop.tokens.json` | Platform-neutral design tokens |
| `assets/tokens/tailwind-preset.ts` | Tailwind theme extension |
| `assets/templates/react/ThLoopLogo.tsx` | Full/compact React component; parent layout chooses `compact` below 160px |
| `assets/templates/react/ThLoopShell.css` | Branded shell primitives |
| `scripts/build_brand_boards.py` | Rebuild deterministic reference/application boards from canonical assets |

## Rules

- Copy only needed assets into the destination project.
- Prefer SVG unless raster is required.
- Do not edit canonical SVG paths inside a product project. Create a documented new derivative only when production constraints demand it.
- Use only files in `assets/logos/` and `assets/marks/` as logo masters. Any logo visible inside a reference image or mockup is non-authoritative.
- Monochrome masters preserve the gold-notch geometry in `currentColor`; they change color count, never silhouette.
- Run `scripts/build_brand_boards.py` to refresh both canonical boards and all four compatibility aliases together.
