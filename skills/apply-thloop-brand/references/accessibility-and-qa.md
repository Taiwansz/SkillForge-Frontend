# ThLoop accessibility and QA

## Preflight checklist

### Brand integrity

- [ ] Full wordmark comes from `assets/logos/`.
- [ ] Compact mark is Twin Chamber from `assets/marks/`.
- [ ] Chicane Cut is not presented as a logo.
- [ ] Wordmark aspect ratio is unchanged.
- [ ] Gold occupies no more than 5%, preferably 1–3%.
- [ ] No rejected mark, infinity symbol, circuit cliché, gradient, glow, or neon appears.

### Accessibility

- [ ] Normal text contrast is at least 4.5:1.
- [ ] Large text and non-text UI contrast is at least 3:1.
- [ ] Focus is visible and not encoded by gold alone.
- [ ] Interactive targets are at least 44×44px on touch screens.
- [ ] All controls are keyboard reachable.
- [ ] Icons have accessible names when functional.
- [ ] Decorative marks are hidden from assistive technology.
- [ ] Reduced-motion preferences are respected.
- [ ] Information is never communicated only by color.

### Responsive and states

- [ ] Verified at 375px, 768px, and 1440px.
- [ ] No horizontal overflow.
- [ ] Full wordmark swaps to Twin Chamber instead of compressing.
- [ ] Empty, loading, success, error, disabled, hover, active, and focus states exist when relevant.
- [ ] Long text, realistic data, and zero-data conditions were tested.

### Engineering

- [ ] Semantic tokens are used.
- [ ] Images include dimensions or aspect ratio to prevent layout shift.
- [ ] SVGs are embedded or optimized without path mutation.
- [ ] Motion uses transform/opacity where possible.
- [ ] No secrets, inline credentials, or unrelated third-party assets are bundled.

## Deterministic checks

Run:

```bash
python3 scripts/brand_audit.py <project-or-file>
python3 scripts/check_contrast.py '#F0EDE6' '#0A0A0A'
```

Treat audit errors as release blockers. Review warnings intentionally and document exceptions.

## Verified dark-theme pairs

| Use | Foreground | Background | Contrast |
|---|---:|---:|---:|
| Primary text | `#F0EDE6` | `#0A0A0A` | 16.93:1 |
| Muted text | `#9B9993` | `#2A2A2A` | 5.04:1 |
| Error text/icon | `#D88278` | `#2A2A2A` | 5.05:1 |
| Chicane accent, large/non-text only | `#C8B560` | `#0A0A0A` | 9.65:1 |

Re-run `check_contrast.py` for every new foreground/background pair. Do not assume a token that passes on Loop Black also passes on Chassis.
