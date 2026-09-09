# Motion

## Motion idea

TokLang motion visualizes compression: a broad stream converges, pauses at the yellow spine, and exits shorter. It should feel quick and deliberate, never bouncy or cartoonish.

## Timing

- Micro interaction: 120–180 ms.
- Component transition: 200–320 ms.
- Explanatory compression sequence: 600–900 ms.
- Ambient loop: 6–12 seconds with long rests.

## Easing

- Enter: `cubic-bezier(.22, 1, .36, 1)`.
- Exit: `cubic-bezier(.4, 0, 1, 1)`.
- Compression: accelerate toward the yellow spine, pause 60–100 ms, then resolve smoothly.

## Approved behaviors

- token lines converge into the yellow spine;
- mapped symbols replace source phrases in place;
- savings counter changes only after the transformation completes;
- the compact mark can draw on as one continuous curve;
- patterns can drift 4–12 px over long intervals.

## Avoid

- elastic bounce;
- constant floating;
- rapid neon pulses;
- spinning logos;
- scroll hijacking;
- motion that hides source/output comparison.

## Reduced motion

When `prefers-reduced-motion: reduce` is active, replace transformations with a 100 ms opacity change or an immediate state change. Keep all information available.
