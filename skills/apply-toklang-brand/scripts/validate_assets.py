#!/usr/bin/env python3
"""Validate the required TokLang brand bundle and its asset manifest."""

import json
import struct
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "agents/openai.yaml", "assets/icon.svg", "assets/asset-manifest.json",
    "assets/marks/toklang-flow-light.svg", "assets/marks/toklang-flow-dark.svg",
    "assets/logos/toklang-stacked-light.svg", "assets/logos/toklang-stacked-dark.svg",
    "assets/logos/toklang-extended-light.svg", "assets/logos/toklang-extended-dark.svg",
    "assets/png/toklang-stacked-industrial.png", "assets/png/toklang-extended-industrial.png",
    "assets/png/toklang-flow-industrial.png", "assets/tokens/toklang.css",
    "references/brand-foundations.md", "references/logo-usage.md",
    "references/patterns-and-illustration.md", "references/accessibility-and-qa.md",
]


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG signature")
    return struct.unpack(">II", header[16:24])


def main() -> int:
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing: {relative}")

    for path in (ROOT / "assets").rglob("*.svg"):
        try:
            root = ElementTree.parse(path).getroot()
            if not root.attrib.get("viewBox"):
                errors.append(f"SVG lacks viewBox: {path.relative_to(ROOT)}")
        except ElementTree.ParseError as exc:
            errors.append(f"invalid SVG {path.relative_to(ROOT)}: {exc}")

    for path in (ROOT / "assets/png").glob("*.png"):
        try:
            width, height = png_size(path)
            if min(width, height) < 128:
                errors.append(f"raster too small: {path.relative_to(ROOT)} ({width}x{height})")
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    manifest_path = ROOT / "assets/asset-manifest.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for item in manifest.get("assets", []):
            if not (ROOT / item["path"]).is_file():
                errors.append(f"manifest target missing: {item['path']}")

    if errors:
        print("TokLang brand validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("TokLang brand bundle is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
