# Digital UI

## Product principles

1. Show cause and effect: input, mapping, output, savings.
2. Keep primary actions obvious even when the page is expressive.
3. Use animation to explain transformation, not to decorate every interaction.
4. Keep developer-facing evidence close to claims.

## Layout

- Content max width: 1200–1280 px.
- Reading width: 640–760 px.
- Base spacing unit: 4 px; common gaps: 8, 12, 16, 24, 32, 48, 72, 96.
- Hero sections can be asymmetric: copy left, live compression demo right.
- Keep content on a strict grid while ribbons and patterns can break it.

## Components

### Navigation

Use the extended logo or compact mark. Keep navigation calm and reserve yellow for the primary action or active state, not both simultaneously.

### Buttons

- Primary light: Deep Wine fill, Paper White label.
- Primary dark: Safety Yellow fill, Night Wine label.
- Secondary: transparent with a 1 px wine/silver border.
- Focus: 3 px Safety Yellow ring plus 2 px canvas gap.
- Radius: 10–14 px, never a default full pill for large buttons.

### Cards

Use a quiet surface, a fine border, and one curved detail at most. Metric cards may enlarge a single savings number in yellow.

### Code and token panels

- Use monospace only inside code, mappings, IDs, and metrics.
- Original text uses a calm surface; compressed output uses a subtle wine tint.
- Highlight only changed or mapped tokens.
- Never fake savings. Label demonstrations as `exemplo` when values are not computed.

### Forms

Labels remain visible above fields. Validation text must be specific. Yellow is focus, not error. Error states use the functional danger color plus text.

## Light theme

Use Brushed Silver as the broad canvas and Paper White for elevated reading surfaces. Deep Wine provides the strongest anchors. Avoid placing light gray copy directly on silver.

## Dark theme

Use Night Wine for the page and Raised Wine for elevated surfaces. Primary text is Mist. Keep patterns between 4–12% opacity. Yellow focus and CTA states must have Night Wine text.

## Responsive behavior

- Replace full signatures with the compact mark below 640 px when header width is constrained.
- Stack before/after demos vertically.
- Crop decorative curves intentionally; do not shrink them into tiny clutter.
- Preserve 20 px minimum page gutters on mobile.

## Accessibility

- Body copy targets WCAG AA contrast.
- Controls have a visible non-color state change.
- Respect `prefers-reduced-motion`.
- Preserve headings and landmarks when implementing expressive layouts.
- Do not encode original/compressed states only through wine and yellow; use labels or icons too.

Use `assets/templates/react/` or `assets/templates/toklang-starter.html` as implementation starters.
