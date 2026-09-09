#!/usr/bin/env python3
"""Scan source files for common TokLang brand-system mistakes."""

import re
import sys
from pathlib import Path

TEXT_EXTENSIONS = {".html", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".md", ".json", ".yaml", ".yml"}
RULES = [
    (re.compile(r"\bTok(?:e|en)\s*Lang(?:uage)?\b", re.I), "Use the exact spelling TokLang."),
    (re.compile(r"#(?:00ff00|22c55e|3b82f6|8b5cf6)\b", re.I), "Generic green/blue/purple detected; verify it is functional, not brand color."),
    (re.compile(r"(?:logo|wordmark).*(?:rotate|skew|drop-shadow)", re.I), "Do not rotate, skew, or shadow the logo."),
    (re.compile(r"color\s*:\s*#(?:fff|ffffff).*background(?:-color)?\s*:\s*#ffd324", re.I | re.S), "White on Safety Yellow lacks contrast."),
]


def main() -> int:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    files = [target] if target.is_file() else [p for p in target.rglob("*") if p.suffix.lower() in TEXT_EXTENSIONS]
    findings = []
    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern, message in RULES:
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                findings.append(f"{path}:{line}: {message}")
    if findings:
        print("\n".join(findings))
        return 1
    print("No common TokLang brand violations found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
