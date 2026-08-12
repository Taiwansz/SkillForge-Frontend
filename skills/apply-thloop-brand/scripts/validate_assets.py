#!/usr/bin/env python3
"""Validate canonical ThLoop SVG/PNG assets and brand invariants."""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

from PIL import Image


ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
REQUIRED = [
    "logos/thloop-continuous-core-light.svg",
    "logos/thloop-continuous-core-dark.svg",
    "logos/thloop-continuous-core-mono.svg",
    "marks/twin-chamber-light.svg",
    "marks/twin-chamber-dark.svg",
    "marks/twin-chamber-mono.svg",
    "visual/chicane-cut-light.svg",
    "visual/chicane-cut-dark.svg",
    "visual/chicane-divider.svg",
    "visual/chicane-pattern.svg",
    "icons/favicon.svg",
    "icons/app-icon.svg",
    "tokens/thloop.css",
    "tokens/thloop.tokens.json",
]
FORBIDDEN_SVG = re.compile(r"<\s*(?:linearGradient|radialGradient|filter)\b", re.I)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    for relative in REQUIRED:
        if not (ASSETS / relative).is_file():
            fail(f"missing required asset: {relative}")

    manifest: dict[str, dict[str, object]] = {}
    for path in sorted(ASSETS.rglob("*")):
        if not path.is_file() or path.name == "asset-manifest.json":
            continue
        relative = path.relative_to(ASSETS).as_posix()
        if relative == "icon.svg":
            continue
        raw = path.read_bytes()
        entry: dict[str, object] = {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
        if path.suffix.lower() == ".svg":
            text = raw.decode("utf-8")
            if FORBIDDEN_SVG.search(text):
                fail(f"forbidden gradient/filter in {relative}")
            try:
                root = ET.fromstring(text)
            except ET.ParseError as exc:
                fail(f"invalid SVG {relative}: {exc}")
            view_box = root.attrib.get("viewBox")
            if not view_box:
                fail(f"missing viewBox in {relative}")
            if not any(element.tag.endswith("title") for element in root.iter()):
                fail(f"missing title in {relative}")
            entry["viewBox"] = view_box
        elif path.suffix.lower() == ".png":
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                entry["dimensions"] = list(image.size)
                entry["mode"] = image.mode
        manifest[relative] = entry

    (ASSETS / "asset-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Validated {len(manifest)} assets; manifest updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
