#!/usr/bin/env python3
"""Audit source files for common violations of the ThLoop identity."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".jsx", ".mjs", ".scss", ".svg", ".ts", ".tsx", ".vue"
}
SKIP_DIRS = {".git", ".next", "build", "coverage", "dist", "node_modules", "vendor"}
CANONICAL_HEX = {"#0a0a0a", "#f0ede6", "#c8b560", "#2a2a2a", "#5c5c5c"}
FORBIDDEN_PATTERNS = {
    "gradient": re.compile(r"(?:linear|radial|conic)-gradient\s*\(", re.I),
    "SVG gradient": re.compile(r"<\s*(?:linearGradient|radialGradient)\b", re.I),
    "glow styling": re.compile(r"\b(?:text-shadow|filter)\s*:[^;]*(?:glow|blur)\b", re.I),
    "infinity symbol": re.compile(r"∞|\binfinity\b", re.I),
    "generic lorem ipsum": re.compile(r"\blorem\s+ipsum\b", re.I),
}
WORDMARK_FILES = {
    "thloop-continuous-core-light.svg",
    "thloop-continuous-core-dark.svg",
    "thloop-continuous-core-mono.svg",
}
COMPACT_FILES = {
    "twin-chamber-light.svg", "twin-chamber-dark.svg", "twin-chamber-mono.svg", "favicon.svg", "app-icon.svg"
}


def iter_files(target: pathlib.Path):
    if target.is_file():
        if target.suffix.lower() in TEXT_SUFFIXES:
            yield target
        return
    for path in target.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=pathlib.Path)
    parser.add_argument("--strict-colors", action="store_true", help="Warn about non-canonical literal hex colors.")
    args = parser.parse_args()
    target = args.target.resolve()
    if not target.exists():
        print(f"ERROR: target does not exist: {target}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    for path in iter_files(target):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(target) if target.is_dir() else path.name
        for label, pattern in FORBIDDEN_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{rel}:{line}: forbidden {label}")

        if args.strict_colors:
            for value in re.findall(r"#[0-9a-fA-F]{6}\b", text):
                lowered = value.lower()
                if lowered not in CANONICAL_HEX:
                    line = text.count("\n", 0, text.find(value)) + 1
                    warnings.append(f"{rel}:{line}: non-canonical literal color {value}")

        if re.search(r"\bTh\s*Loop\b", text, re.I) and path.suffix.lower() in {".html", ".jsx", ".tsx", ".vue"}:
            if not any(name in text for name in WORDMARK_FILES | COMPACT_FILES):
                warnings.append(f"{rel}: brand name appears without a canonical logo asset reference")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    print(f"Audit complete: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
