#!/usr/bin/env python3
"""Export canonical THP / ThPay SVG assets to PNG using CairoSVG."""

from pathlib import Path
import sys

try:
    import cairosvg
except ImportError:
    raise SystemExit('Install cairosvg: pip install cairosvg')

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
OUT = ASSETS / 'png'
OUT.mkdir(exist_ok=True)

JOBS = [
    ('icons/app-icon.svg', 'app-icon-1024.png', 1024),
    ('icons/app-icon.svg', 'app-icon-512.png', 512),
    ('icons/favicon.svg', 'favicon-32.png', 32),
    ('marks/thp-modular.svg', 'thp-modular-512.png', 512),
    ('logos/thpay-primary-dark.svg', 'thpay-primary-dark-1080.png', 1080),
    ('logos/thpay-primary-light.svg', 'thpay-primary-light-1080.png', 1080),
    ('visual/brand-reference.svg', 'thpay-brand-reference-1440.png', 1440),
]

for source, output, width in JOBS:
    cairosvg.svg2png(url=str(ASSETS / source), write_to=str(OUT / output), output_width=width)
    print('wrote', OUT / output)
