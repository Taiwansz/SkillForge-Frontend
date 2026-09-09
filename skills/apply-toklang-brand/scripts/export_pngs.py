#!/usr/bin/env python3
"""Export every TokLang vector asset and reference board to organized PNG files."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PNG = ASSETS / "png"

EXPORTS = {
    "logos/toklang-stacked-light.svg": [(720, "logos/toklang-stacked-light-720.png"), (1440, "logos/toklang-stacked-light-1440.png")],
    "logos/toklang-stacked-dark.svg": [(720, "logos/toklang-stacked-dark-720.png"), (1440, "logos/toklang-stacked-dark-1440.png")],
    "logos/toklang-extended-light.svg": [(1320, "logos/toklang-extended-light-1320.png"), (2640, "logos/toklang-extended-light-2640.png")],
    "logos/toklang-extended-dark.svg": [(1320, "logos/toklang-extended-dark-1320.png"), (2640, "logos/toklang-extended-dark-2640.png")],
    "marks/toklang-flow-light.svg": [(256, "marks/toklang-flow-light-256.png"), (512, "marks/toklang-flow-light-512.png"), (1024, "marks/toklang-flow-light-1024.png")],
    "marks/toklang-flow-dark.svg": [(256, "marks/toklang-flow-dark-256.png"), (512, "marks/toklang-flow-dark-512.png"), (1024, "marks/toklang-flow-dark-1024.png")],
    "icons/favicon.svg": [(16, "icons/favicon-16.png"), (32, "icons/favicon-32.png"), (64, "icons/favicon-64.png")],
    "icons/app-icon.svg": [(180, "icons/apple-touch-icon-180.png"), (512, "icons/app-icon-512.png"), (1024, "icons/app-icon-1024.png")],
    "visual/corner-ribbon.svg": [(800, "patterns/corner-ribbon-800.png"), (1600, "patterns/corner-ribbon-1600.png")],
    "visual/compression-stream.svg": [(1200, "patterns/compression-stream-1200.png"), (2400, "patterns/compression-stream-2400.png")],
    "visual/token-blooms.svg": [(800, "patterns/token-blooms-800.png"), (1600, "patterns/token-blooms-1600.png")],
    "visual/contour-field.svg": [(1200, "patterns/contour-field-1200.png"), (2400, "patterns/contour-field-2400.png")],
    "visual/modular-pattern.svg": [(640, "patterns/modular-pattern-640.png"), (1280, "patterns/modular-pattern-1280.png")],
    "visual/data-fall.svg": [(900, "illustrations/data-fall-900.png"), (1800, "illustrations/data-fall-1800.png")],
    "visual/hero-compression.svg": [(1280, "illustrations/hero-compression-1280.png"), (2560, "illustrations/hero-compression-2560.png")],
    "micro/divider-compression.svg": [(640, "micro/divider-compression-640.png"), (1280, "micro/divider-compression-1280.png")],
    "micro/bullet-token.svg": [(48, "micro/bullet-token-48.png"), (96, "micro/bullet-token-96.png"), (192, "micro/bullet-token-192.png")],
    "micro/cursor-flow.svg": [(64, "micro/cursor-flow-64.png"), (128, "micro/cursor-flow-128.png"), (256, "micro/cursor-flow-256.png")],
    "micro/badge-savings.svg": [(360, "micro/badge-savings-360.png"), (720, "micro/badge-savings-720.png")],
    "micro/underline-flow.svg": [(720, "micro/underline-flow-720.png"), (1440, "micro/underline-flow-1440.png")],
    "micro/progress-compression.svg": [(720, "micro/progress-compression-720.png"), (1440, "micro/progress-compression-1440.png")],
    "micro/corner-focus.svg": [(160, "micro/corner-focus-160.png"), (320, "micro/corner-focus-320.png"), (640, "micro/corner-focus-640.png")],
    "micro/token-chip.svg": [(360, "micro/token-chip-360.png"), (720, "micro/token-chip-720.png")],
}

REFERENCES = {
    "reference/decorative-system.jpg": "reference/decorative-system.png",
    "reference/industrial-pop-applications.jpg": "reference/industrial-pop-applications.png",
    "reference/landing-light.jpg": "reference/landing-light.png",
    "reference/landing-dark.jpg": "reference/landing-dark.png",
}


def export_svg(inkscape: str, source: Path, output: Path, width: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run([
        inkscape, str(source), "--export-background-opacity=0", f"--export-width={width}",
        f"--export-filename={output}"
    ], capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(f"Failed to export {source}: {(result.stderr or result.stdout).strip()}")


def describe(path: Path) -> dict:
    with Image.open(path) as image:
        dimensions = list(image.size)
        mode = image.mode
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "dimensions": dimensions,
        "mode": mode,
    }


def main() -> int:
    inkscape = shutil.which("inkscape")
    if not inkscape:
        raise SystemExit("Inkscape is required to export the TokLang PNG library.")
    exported = []
    for source_name, outputs in EXPORTS.items():
        source = ASSETS / source_name
        for width, output_name in outputs:
            output = PNG / output_name
            export_svg(inkscape, source, output, width)
            exported.append(describe(output))
            print(f"exported {output.relative_to(ROOT)}")
    for source_name, output_name in REFERENCES.items():
        source, output = ASSETS / source_name, PNG / output_name
        output.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as image:
            # Reference boards contain JPEG grain; indexed color keeps their PNG
            # counterparts practical for Git without changing their dimensions.
            image.convert("RGB").quantize(colors=128, method=Image.Quantize.MEDIANCUT).save(
                output, format="PNG", optimize=True
            )
        exported.append(describe(output))
        print(f"exported {output.relative_to(ROOT)}")
    manifest = PNG / "png-manifest.json"
    manifest.write_text(json.dumps({"brand": "TokLang", "count": len(exported), "assets": exported}, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {manifest.relative_to(ROOT)} with {len(exported)} PNGs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
