#!/usr/bin/env python3
"""Check WCAG contrast for TokLang's documented foreground/background pairs."""

PAIRS = {
    "wine on silver": ("#4A1824", "#D9DADC"),
    "night on yellow": ("#130B10", "#FFD324"),
    "mist on night": ("#ECEDEF", "#130B10"),
    "mist on surface": ("#ECEDEF", "#211219"),
    "muted on night": ("#AEB2B8", "#130B10"),
    "dark text on paper": ("#24171C", "#F7F7F4"),
}


def luminance(value: str) -> float:
    rgb = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    channels = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return .2126 * channels[0] + .7152 * channels[1] + .0722 * channels[2]


def contrast(foreground: str, background: str) -> float:
    a, b = luminance(foreground), luminance(background)
    return (max(a, b) + .05) / (min(a, b) + .05)


if __name__ == "__main__":
    failed = False
    for name, pair in PAIRS.items():
        ratio = contrast(*pair)
        status = "PASS" if ratio >= 4.5 else "LARGE TEXT ONLY" if ratio >= 3 else "FAIL"
        print(f"{status:15} {ratio:5.2f}:1  {name}")
        failed |= ratio < 3
    raise SystemExit(1 if failed else 0)
