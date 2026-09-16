#!/usr/bin/env python3
"""Build deterministic THP / ThPay reference-board PNG from canonical SVG."""

from pathlib import Path
try:
    import cairosvg
except ImportError:
    raise SystemExit('Install cairosvg: pip install cairosvg')

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'assets/visual/brand-reference.svg'
out = ROOT / 'assets/png/thpay-brand-reference-1440.png'
out.parent.mkdir(exist_ok=True)
cairosvg.svg2png(url=str(source), write_to=str(out), output_width=1440)
print(out)
