#!/usr/bin/env python3
"""Export canonical ThLoop SVG assets to PNG using ImageMagick."""

from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess


EXPORTS = {
    "logos/thloop-continuous-core-light.svg": [(1080, "png/thloop-wordmark-light-1080.png")],
    "logos/thloop-continuous-core-dark.svg": [(1080, "png/thloop-wordmark-dark-1080.png")],
    "marks/twin-chamber-light.svg": [(512, "png/twin-chamber-light-512.png")],
    "marks/twin-chamber-dark.svg": [(512, "png/twin-chamber-dark-512.png")],
    "icons/favicon.svg": [(32, "png/favicon-32.png"), (180, "png/apple-touch-icon-180.png")],
    "icons/app-icon.svg": [(512, "png/app-icon-512.png"), (1024, "png/app-icon-1024.png")],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1] / "assets")
    args = parser.parse_args()
    assets = args.assets.resolve()
    inkscape = shutil.which("inkscape")
    imagemagick = shutil.which("magick") or shutil.which("convert")
    if inkscape is None and imagemagick is None:
        raise SystemExit("Inkscape or ImageMagick is required.")

    for source_name, variants in EXPORTS.items():
        source = assets / source_name
        if not source.is_file():
            raise SystemExit(f"Missing source SVG: {source}")
        for width, output_name in variants:
            output = assets / output_name
            output.parent.mkdir(parents=True, exist_ok=True)
            if inkscape:
                command = [
                    inkscape,
                    str(source),
                    "--export-background-opacity=0",
                    f"--export-width={width}",
                    f"--export-filename={output}",
                ]
            else:
                command = [imagemagick, "-background", "none", str(source), "-resize", f"{width}x", str(output)]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode:
                detail = (result.stderr or result.stdout).strip()
                raise SystemExit(f"Failed to export {source.name}: {detail}")
            print(f"exported {output.relative_to(assets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
