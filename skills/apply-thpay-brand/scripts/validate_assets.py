#!/usr/bin/env python3
"""Validate canonical THP / ThPay assets and invariants."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
REQUIRED = [
    'logos/thpay-primary-dark.svg',
    'logos/thpay-primary-light.svg',
    'logos/thpay-primary-mono.svg',
    'marks/thp-modular.svg',
    'marks/connector-t-dark.svg',
    'marks/connector-t-light.svg',
    'icons/app-icon.svg',
    'icons/favicon.svg',
    'visual/connection-blocks.svg',
    'visual/connection-pattern.svg',
    'tokens/thpay.css',
    'tokens/thpay.tokens.json',
]
APPROVED = ['#101A44','#2F66F3','#FFC83D','#8FE1CF','#F7A7B8','#FF7D72','#FFF9F1','#F6F2EC','#E5DED5','#64708A','#FFFFFF','#73B7FF']

errors = []
for rel in REQUIRED:
    p = ASSETS / rel
    if not p.exists(): errors.append(f'missing {rel}')

for rel in [r for r in REQUIRED if r.endswith('.svg')]:
    p = ASSETS / rel
    if not p.exists(): continue
    text = p.read_text(encoding='utf-8')
    if 'viewBox=' not in text: errors.append(f'{rel}: missing viewBox')
    if '<svg' not in text: errors.append(f'{rel}: invalid SVG')

manifest = json.loads((ASSETS / 'asset-manifest.json').read_text(encoding='utf-8'))
for value in manifest['palette'].values():
    if value not in APPROVED: errors.append(f'unapproved manifest color {value}')

for error in errors: print('ERROR', error)
print(f'Asset validation: {len(errors)} error(s)')
raise SystemExit(1 if errors else 0)
