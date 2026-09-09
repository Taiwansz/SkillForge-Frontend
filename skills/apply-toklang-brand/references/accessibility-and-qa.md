# Accessibility and QA

## Contrast

- Body text targets WCAG 2.2 AA: 4.5:1.
- Large text and meaningful graphical objects target at least 3:1.
- Safety Yellow with Paper White is not a valid text pairing.
- Use Night Wine or Deep Wine text on Safety Yellow.
- Muted Silver is secondary text on dark surfaces, not tiny metadata below 14 px.

Run:

```bash
python scripts/check_contrast.py
```

## Logo QA

- correct signature for available space;
- clear space preserved;
- no distortion;
- no accidental recoloring;
- yellow spine remains visible;
- compact mark used at tiny sizes.

## UI QA

- keyboard focus visible;
- touch targets at least 44 by 44 CSS pixels when practical;
- semantic headings and landmarks;
- error states include text;
- loading and empty states are explicit;
- responsive layouts checked at 320, 768, 1024, and 1440 px;
- reduced motion checked;
- light and dark themes checked independently.

## Content QA

- brand spelled `TokLang`;
- token claims identify whether values are measured or illustrative;
- no false equivalence between character reduction and token reduction;
- technical diagrams remain readable without color alone;
- terminology matches the API and thesis.

## Asset QA

Run:

```bash
python scripts/validate_assets.py
python scripts/brand_audit.py path/to/project
```

The validator checks required files, SVG view boxes, raster dimensions, and manifest entries. The audit scans source files for common palette, naming, and logo mistakes.
