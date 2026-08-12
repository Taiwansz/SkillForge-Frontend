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
| `assets/icons/app-icon.svg` | Base square app icon |
| `assets/png/*.png` | Raster fallbacks and common export sizes |
| `assets/reference/thloop-brand-system.png` | Approved visual direction board; reference only |
| `assets/reference/mockups/equipment-kit.png` | Equipment and delivery-kit application reference |
| `assets/reference/mockups/apparel.png` | Apparel and embroidery application reference |
| `assets/reference/mockups/digital-system.png` | Product UI and digital application reference |
| `assets/reference/mockups/hackathon-space.png` | Environmental and hackathon-space reference |

## Tokens and templates

| Path | Use |
|---|---|
| `assets/tokens/thloop.css` | CSS custom properties and base theme |
| `assets/tokens/thloop.tokens.json` | Platform-neutral design tokens |
| `assets/tokens/tailwind-preset.ts` | Tailwind theme extension |
| `assets/templates/react/ThLoopLogo.tsx` | Responsive full/compact React component |
| `assets/templates/react/ThLoopShell.css` | Branded shell primitives |

## Rules

- Copy only needed assets into the destination project.
- Prefer SVG unless raster is required.
- Do not edit canonical SVG paths inside a product project. Create a documented new derivative only when production constraints demand it.
- Use the reference PNG to understand composition, not as the source for extracting or tracing the logo.
