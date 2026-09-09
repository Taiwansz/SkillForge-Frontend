# Asset catalog

## Signatures and marks

| File | Purpose |
|---|---|
| `assets/png/toklang-stacked-industrial.png` | exact approved stacked raster master |
| `assets/png/toklang-extended-industrial.png` | exact approved extended raster master |
| `assets/png/toklang-flow-industrial.png` | approved compact-mark raster |
| `assets/logos/toklang-stacked-light.svg` | scalable stacked signature for light fields |
| `assets/logos/toklang-stacked-dark.svg` | scalable stacked signature for dark fields |
| `assets/logos/toklang-extended-light.svg` | scalable extended signature for light fields |
| `assets/logos/toklang-extended-dark.svg` | scalable extended signature for dark fields |
| `assets/marks/toklang-flow-light.svg` | compact mark on light fields |
| `assets/marks/toklang-flow-dark.svg` | compact mark on dark fields |
| `assets/icons/favicon.svg` | favicon-scale mark |
| `assets/icons/app-icon.svg` | square product/app tile |
| `assets/icon.svg` | skill catalog icon |

## Complete PNG library

`assets/png/` contains 60 ready-to-use PNG files: 3 approved raster masters plus 57 deterministic exports. The generated collection is indexed by `assets/png/png-manifest.json`, including pixel dimensions, byte size, color mode, and SHA-256 digest.

| Folder | Contents |
|---|---|
| `assets/png/logos/` | stacked and extended logos, light/dark, standard and 2× |
| `assets/png/marks/` | compact flow mark, light/dark, 256–1024 px |
| `assets/png/icons/` | favicon 16/32/64, touch icon 180, app icons 512/1024 |
| `assets/png/patterns/` | every pattern family at standard and 2× widths |
| `assets/png/illustrations/` | Data Fall and Hero Compression at standard and 2× |
| `assets/png/micro/` | every microasset in two or three practical sizes |
| `assets/png/reference/` | lossless PNG copies of all reference boards |

Regenerate the collection after changing an SVG master:

```bash
python scripts/export_pngs.py
```

## Decorative assets

| File | Recommended role |
|---|---|
| `assets/visual/corner-ribbon.svg` | corners and section transitions |
| `assets/visual/compression-stream.svg` | feature explanation |
| `assets/visual/token-blooms.svg` | ambient token clusters |
| `assets/visual/contour-field.svg` | quiet semantic field |
| `assets/visual/modular-pattern.svg` | repeatable pattern |
| `assets/visual/data-fall.svg` | metrics and data sections |
| `assets/visual/hero-compression.svg` | hero illustration |

## Microassets

| File | Recommended role |
|---|---|
| `assets/micro/divider-compression.svg` | section divider |
| `assets/micro/bullet-token.svg` | branded bullet or node |
| `assets/micro/cursor-flow.svg` | tutorial cursor |
| `assets/micro/badge-savings.svg` | savings callout |
| `assets/micro/underline-flow.svg` | headline emphasis |
| `assets/micro/progress-compression.svg` | progress visualization |
| `assets/micro/corner-focus.svg` | focus frame |
| `assets/micro/token-chip.svg` | compact syntax example |

## Tokens and starters

| File | Purpose |
|---|---|
| `assets/tokens/toklang.css` | CSS custom properties and base utilities |
| `assets/tokens/toklang.tokens.json` | platform-neutral design tokens |
| `assets/tokens/tailwind-preset.ts` | Tailwind theme extension |
| `assets/templates/react/TokLangBrand.tsx` | React asset components |
| `assets/templates/react/TokLangShell.css` | branded shell and demo styles |
| `assets/templates/toklang-starter.html` | no-build landing-page starter |
| `scripts/export_pngs.py` | regenerate all PNG derivatives and their manifest |

## References

| File | Shows |
|---|---|
| `assets/reference/industrial-pop-applications.jpg` | final palette and applications |
| `assets/reference/decorative-system.jpg` | complete pattern system |
| `assets/reference/landing-light.jpg` | approved light direction |
| `assets/reference/landing-dark.jpg` | approved dark direction |

## Source-of-truth rule

Use the exact approved PNG masters when visual fidelity to the selected concept is the priority. Use the supplied SVG construction for scalable digital UI. Do not extract logos again from reference boards.
