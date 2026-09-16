#!/usr/bin/env python3
"""Audit source files for common THP / ThPay brand violations."""

from pathlib import Path
import re
import sys

BAD_PATTERNS = {
    'neon/glow styling': r'\b(neon|glow|drop-shadow\([^)]*(?:cyan|purple|#0ff|#f0f))',
    'glassmorphism': r'backdrop-filter\s*:\s*blur|backdrop-blur',
    'generic dark default': r'(?:body|:root)[^{]*\{[^}]*background(?:-color)?\s*:\s*#(?:000000|0a0a0a|111111)\b',
    'unapproved purple/cyan cliché': r'#(?:7c3aed|8b5cf6|06b6d4|22d3ee)\b',
}

APPROVED_HEX = {
    '#101a44','#2f66f3','#ffc83d','#8fe1cf','#f7a7b8','#ff7d72',
    '#fff9f1','#f6f2ec','#e5ded5','#64708a','#ffffff','#188a64',
    '#9a6500','#c83d4d','#1746c9','#0c1436','#151f4a','#1c2858',
    '#bcc6db','#34416e','#73b7ff',
}

TEXT_EXT = {'.css','.scss','.html','.tsx','.ts','.jsx','.js','.vue','.svelte'}

def audit(root: Path):
    errors = []
    for path in root.rglob('*') if root.is_dir() else [root]:
        if not path.is_file() or path.suffix.lower() not in TEXT_EXT:
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        low = text.lower()
        for label, pattern in BAD_PATTERNS.items():
            if re.search(pattern, low, re.S):
                errors.append(f'{path}: {label}')
        if 'thpay' in low and ('linear-gradient(' in low or 'radial-gradient(' in low):
            errors.append(f'{path}: gradient detected in ThPay-branded surface; verify it is necessary and restrained')
        for color in re.findall(r'#[0-9a-fA-F]{6}\b', text):
            if color.lower() not in APPROVED_HEX:
                # informational only: semantic/data colors may be legitimate
                print(f'WARN {path}: unregistered color {color}')
    return errors

if __name__ == '__main__':
    target = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    problems = audit(target)
    for problem in problems:
        print('ERROR', problem)
    print(f'Brand audit: {len(problems)} error(s)')
    raise SystemExit(1 if problems else 0)
