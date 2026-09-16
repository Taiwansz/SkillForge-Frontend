# THP / ThPay accessibility and QA

## Brand integrity

- [ ] Primary logo comes from `assets/logos/`.
- [ ] Compact icon comes from `assets/marks/` or `assets/icons/`.
- [ ] No logo was recreated by typing or image generation.
- [ ] Bright colors support hierarchy rather than dominate the viewport.
- [ ] Product screens remain professional and friendly, not childish.
- [ ] Light interface is the default unless dark mode was explicitly requested.

## Accessibility

- [ ] Body and functional text meet WCAG AA contrast.
- [ ] Focus is visible for keyboard users.
- [ ] Touch/click targets are at least 44×44px.
- [ ] Status is not communicated by color alone.
- [ ] Form labels persist when fields contain values.
- [ ] Errors identify both the problem and a recovery path.
- [ ] Motion respects `prefers-reduced-motion`.
- [ ] Zoom at 200% remains usable without overlapping controls.
- [ ] Tables provide a mobile strategy rather than clipping content.

## Responsive QA

Check 375, 768, 1024 and 1440px. Also verify 50%, 100%, 125% and 200% browser zoom for dense dashboard screens.

Watch for:

- fixed heights that truncate translated or wrapped text;
- drawers wider than the viewport;
- sidebar overlap;
- hidden table actions;
- clipped currency values;
- charts with unreadable legends;
- pastel text on pastel surfaces.

## Content QA

- [ ] Copy matches the user's role.
- [ ] Brazilian formats are used when context is pt-BR.
- [ ] Effective date/competence is visible for benefit and payroll changes.
- [ ] Legal or tax values are not presented as timeless facts when they are only sample data.
- [ ] Empty states explain what the user can do next.
