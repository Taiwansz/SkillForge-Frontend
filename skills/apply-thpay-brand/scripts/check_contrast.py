#!/usr/bin/env python3
"""Check common THP foreground/background contrast pairs."""

PAIRS = [
    ('Ink Navy on Warm Ivory', '#101A44', '#FFF9F1'),
    ('Muted Ink on Warm Ivory', '#64708A', '#FFF9F1'),
    ('White on Cobalt', '#FFFFFF', '#2F66F3'),
    ('Ink Navy on Solar', '#101A44', '#FFC83D'),
    ('Ink Navy on Mint', '#101A44', '#8FE1CF'),
    ('Ink Navy on Blush', '#101A44', '#F7A7B8'),
]

def rgb(hex_color):
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))

def channel(c):
    return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4

def lum(hex_color):
    r, g, b = (channel(c) for c in rgb(hex_color))
    return .2126*r + .7152*g + .0722*b

def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + .05) / (y + .05)

if __name__ == '__main__':
    failed = False
    for name, fg, bg in PAIRS:
        value = ratio(fg, bg)
        verdict = 'AA body' if value >= 4.5 else ('AA large only' if value >= 3 else 'FAIL')
        print(f'{name}: {value:.2f}:1 — {verdict}')
        failed |= value < 3
    raise SystemExit(1 if failed else 0)
