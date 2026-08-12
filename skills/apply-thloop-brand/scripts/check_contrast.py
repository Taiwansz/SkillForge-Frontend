#!/usr/bin/env python3
"""Calculate WCAG contrast for two colors without third-party dependencies."""

from __future__ import annotations

import argparse
import re


HEX_RE = re.compile(r"^#?([0-9a-fA-F]{6})$")


def parse_hex(value: str) -> tuple[int, int, int]:
    match = HEX_RE.fullmatch(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(f"Invalid 6-digit hex color: {value}")
    raw = match.group(1)
    return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4))


def luminance(rgb: tuple[int, int, int]) -> float:
    channels = []
    for component in rgb:
        channel = component / 255
        channels.append(channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(foreground: tuple[int, int, int], background: tuple[int, int, int]) -> float:
    light, dark = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foreground", type=parse_hex)
    parser.add_argument("background", type=parse_hex)
    parser.add_argument("--minimum", type=float, default=4.5)
    args = parser.parse_args()

    ratio = contrast(args.foreground, args.background)
    verdict = "PASS" if ratio >= args.minimum else "FAIL"
    print(f"Contrast: {ratio:.2f}:1 — {verdict} (minimum {args.minimum:.1f}:1)")
    return 0 if ratio >= args.minimum else 1


if __name__ == "__main__":
    raise SystemExit(main())
