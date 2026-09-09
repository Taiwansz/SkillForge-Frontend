# Patterns and illustration

## Purpose

TokLang decoration should reinforce how the product works: many language units enter, mapping happens, and a smaller structured representation leaves. Patterns are system diagrams made expressive.

## Canonical families

### Corner Ribbon

File: `assets/visual/corner-ribbon.svg`

A broad cropped wine curve with a yellow gate. Use at page corners, section transitions, covers, and social templates. Maximum one dominant ribbon per viewport.

### Compression Stream

File: `assets/visual/compression-stream.svg`

Multiple rounded input streams converge into a narrow channel and exit as three compact tokens. Use beside product explanations, architecture sections, and token-saving claims.

### Token Blooms

File: `assets/visual/token-blooms.svg`

Four approved petal-based token symbols: Trident, Pinwheel, Butterfly, and Orbit. The combined sheet is `token-blooms.svg`; every bloom also has an individual SVG and PNG. Use for section headings, cards, and quieter backgrounds.

### Contour Field

File: `assets/visual/contour-field.svg`

Mirrored contour lines converge around a yellow compression gate. Use in large empty fields and section backgrounds. Do not treat it as a full-page wallpaper.

### Modular Pattern

File: `assets/visual/modular-pattern.svg`

Repeatable rounded modules and yellow gates derived from the approved pattern board. Use on packaging, swag, banners, or contained UI empty states.

### Data Fall

File: `assets/visual/data-fall.svg`

Vertical segmented streams with intermittent yellow mapped tokens. Use in page margins, metrics, and technical storytelling.

### Hero Compression

File: `assets/visual/hero-compression.svg`

The largest explanatory illustration. Use once per page, normally in the hero or core product section.

## Microassets

Each microasset has an editable SVG master in `assets/micro/` and ready-to-use PNG exports in `assets/png/micro/`.

| Asset | Purpose |
|---|---|
| `section-divider` / `divider-compression` | vertical yellow section marker and compatibility alias |
| `rule` | quiet wine horizontal rule |
| `pagination` | three-dot pagination motif |
| `bullet-token` | yellow list bullet or status node |
| `cursor-flow` | wine tutorial pointer |
| `badge-savings` | wine pill with yellow signal dash |
| `corner-bracket` | wine framing corner |
| `underline-flow` | yellow headline emphasis |
| `progress-compression` | shrinking wine progress segments |
| `corner-focus` | yellow focus corner |
| `token-chip` | compact syntax example |

Do not use these as substitutes for common interface icons such as search, close, menu, or accessibility controls.

## PNG availability

Every canonical logo, mark, icon, pattern, illustration, microasset, and reference board has a PNG counterpart. Use `assets/png/png-manifest.json` to select an exact size. Prefer the smallest export that is at least as large as its rendered CSS width on a 2× display.

## Density levels

- **Ambient:** 4–8% opacity, behind empty areas only.
- **Supporting:** 12–25% opacity, beside content.
- **Hero:** full brand colors with its own clear field.

## Cropping

Crop large curves at the top, bottom, or outside edge. Never crop the yellow compression point. The viewer must understand that a transformation occurs there.

## Combining patterns

Use one dominant family and optionally one ambient family in a composition. Do not combine three or more expressive motifs in one viewport.

## Illustration rules

- flat vector geometry;
- controlled soft shadows only on UI mockups;
- no 3D glass blobs, chrome letters, cute characters, gears, pipes, or factory imagery;
- no arbitrary squiggles disconnected from compression;
- maintain round joins and purposeful flow;
- leave copy-safe negative space.

## Reference

See `assets/reference/decorative-system.jpg` for the approved system board and `assets/reference/industrial-pop-applications.jpg` for real-world scale examples.
