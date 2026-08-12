# ThLoop digital UI system

## Contents

1. Token integration
2. Page architecture
3. Components
4. Dashboards and data
5. Motion
6. Responsive behavior
7. Metadata and assets

## Token integration

Import `assets/tokens/thloop.css` globally or map `assets/tokens/thloop.tokens.json` into the project’s existing token layer. Use semantic tokens such as `--tl-bg`, `--tl-surface`, and `--tl-text`; do not bind components directly to palette names.

## Page architecture

### Landing and presentation pages

- Use a full-width hero with one clear statement and one primary action.
- Place the wordmark in navigation or hero signature, not both at oversized scale.
- Use Chicane Cut as an edge transition between at most two major sections.
- Vary section rhythm: full-width editorial statement, split technical evidence, compact proof list, then action.
- Avoid the default sequence of hero plus three equal cards plus testimonials plus CTA.

### Applications and dashboards

- Use a stable shell: compact navigation, main work surface, optional contextual inspector.
- Keep the content background Loop Black and raised operational surfaces Chassis.
- Use lines, spacing, and labels to group data before adding cards.
- Keep one hero metric or status; render secondary metrics smaller and quieter.
- Reserve gold for the active selection, one key metric, or an explicit action—not all three simultaneously.

## Components

### Buttons

- Primary: Technical Paper background, Loop Black text, 4–8px radius.
- Secondary: transparent/Chassis surface, Technical Paper text, 1px Smoked Mirror border.
- Critical brand action: a small Chicane notch may interrupt one edge; do not turn the entire button gold.
- Minimum target: 44×44px.

### Inputs

- Use visible labels above fields.
- Use Chassis surface, Smoked Mirror border, Technical Paper value, and a high-contrast focus ring.
- Place validation text directly below the field and pair color with text/icon semantics.

### Navigation

- Use compact uppercase monospaced metadata sparingly.
- Indicate current state with a gold rule/notch plus contrast change.
- Do not place icons inside pastel squares.

### Data tables

- Use tabular numerals, sticky headers when useful, row hover, keyboard focus, and clear sorting state.
- Prefer 40–48px row heights for operational density.
- Provide horizontal scrolling or stacked mobile representation, never clipped columns.

### Cards and surfaces

- Add a surface only when it communicates grouping, elevation, interaction, or state.
- Do not nest cards. Use section labels and 1px dividers.
- Avoid large drop shadows; use `#2A2A2A` against `#0A0A0A` for depth.

## Dashboards and data

Structure information in three levels:

1. health/status and one primary KPI;
2. trend or comparison evidence;
3. operational detail, filters, logs, and tables.

Use neutral chart series by default. Use gold for one selected series or reference line. Add status colors only for semantic states and always include textual labels.

## Motion

- Microinteractions: 150–200ms ease-out.
- Panels: 240–320ms cubic-bezier(0.16, 1, 0.3, 1).
- Brand reveal: animate the Chicane Cut as two paths approaching the gold registration gap; do not draw an infinity loop.
- Animate `transform` and `opacity` only when possible.
- Honor `prefers-reduced-motion`.

## Responsive behavior

- Design at 375px first.
- Verify at 768px and 1440px.
- Preserve the full wordmark above its minimum legible width; swap to Twin Chamber below it.
- Never squeeze the wordmark. Replace it responsively.
- Keep all touch controls at least 44×44px.
- Ensure Chicane crops do not create accidental horizontal overflow.

## Metadata and assets

- Use Twin Chamber for favicon and app icon.
- Use the full wordmark for Open Graph images and branded boot screens.
- Add descriptive alt text for informative brand imagery; mark purely decorative Chicane elements with empty alt text or `aria-hidden="true"`.

