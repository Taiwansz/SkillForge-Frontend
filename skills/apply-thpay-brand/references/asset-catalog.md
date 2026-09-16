# THP / ThPay asset catalog

## Canonical logos

- `assets/logos/thpay-primary-dark.svg` — primary lockup for light surfaces.
- `assets/logos/thpay-primary-light.svg` — primary lockup for Ink Navy/dark surfaces.
- `assets/logos/thpay-primary-mono.svg` — one-color production fallback.

## Marks and icons

- `assets/marks/thp-modular.svg` — full modular THP symbol.
- `assets/marks/connector-t-dark.svg` — compact mark for light backgrounds.
- `assets/marks/connector-t-light.svg` — compact mark for dark backgrounds.
- `assets/icons/app-icon.svg` — canonical square app icon.
- `assets/icons/favicon.svg` — simplified favicon.
- `assets/icon.svg` — skill package icon alias.

## Visual system

- `assets/visual/connection-blocks.svg` — modular block composition.
- `assets/visual/connection-pattern.svg` — repeatable low-density pattern.
- `assets/visual/brand-reference.svg` — deterministic vector reference board.

## Tokens

- `assets/tokens/thpay.css` — CSS custom properties and semantic themes.
- `assets/tokens/thpay.tokens.json` — machine-readable design tokens.
- `assets/tokens/tailwind-preset.ts` — Tailwind theme extension.

## Templates

- `assets/templates/react/ThPayLogo.tsx` — canonical React asset wrapper.
- `assets/templates/react/ThPayShell.css` — starter app-shell styling.
- `assets/templates/thpay-starter.html` — zero-dependency HTML starter.

## Generated raster assets

Run `scripts/export_pngs.py` to generate PNG fallbacks from the SVG masters. SVG remains the source of truth.

## Selection rule

Use the primary lockup whenever there is enough horizontal space. Use the full THP symbol for square-ish brand moments. Use Connector T only when the space is too small for the full symbol or when the platform specifically expects an app icon/favicon.
