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
    "icons/favicon.svg": [(32, "png/favicon-32.png")],
    "icons/app-icon.svg": [
        (180, "png/apple-touch-icon-180.png"),
        (512, "png/app-icon-512.png"),
        (1024, "png/app-icon-1024.png"),
    ],
}


def export_with_inkscape(inkscape: str, source: pathlib.Path, output: pathlib.Path, width: int) -> None:
    command = [
        inkscape,
        str(source),
        "--export-background-opacity=0",
        f"--export-width={width}",
        f"--export-filename={output}",
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise SystemExit(f"Failed to export {source.name}: {detail}")


def build_icon_svg(
    mark_svg: pathlib.Path,
    output_svg: pathlib.Path,
    size: int,
    radius: int,
    title: str,
    *,
    opaque_square: bool = False,
) -> None:
    text = mark_svg.read_text(encoding="utf-8")
    view_box = text.split('viewBox="', 1)[1].split('"', 1)[0].split()
    mark_w, mark_h = float(view_box[2]), float(view_box[3])
    group = text.split("<g ", 1)[1].rsplit("</g>", 1)[0]
    group = "<g " + group + "</g>"
    target_w = size * 0.78
    scale = target_w / mark_w
    x = (size - mark_w * scale) / 2
    y = (size - mark_h * scale) / 2
    output_svg.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" role="img" aria-labelledby="title">\n'''
        f'''  <title id="title">{title}</title>\n'''
        f'''  <rect width="{size}" height="{size}"{'' if opaque_square else f' rx="{radius}"'} fill="#0A0A0A"/>\n'''
        f'''  <rect x="{size * 0.028:.2f}" y="{size * 0.028:.2f}" width="{size * 0.944:.2f}" height="{size * 0.944:.2f}" rx="{radius * 0.89:.2f}" fill="none" stroke="#2A2A2A" stroke-width="{max(2, size * 0.008):.2f}"/>\n'''
        f'''  <g transform="translate({x:.3f} {y:.3f}) scale({scale:.6f})">{group}</g>\n'''
        f'''</svg>\n''',
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1] / "assets")
    args = parser.parse_args()
    assets = args.assets.resolve()
    inkscape = shutil.which("inkscape")
    imagemagick = shutil.which("magick") or shutil.which("convert")
    if inkscape is None and imagemagick is None:
        raise SystemExit("Inkscape or ImageMagick is required.")

    if inkscape:
        build_icon_svg(
            assets / "marks/twin-chamber-light.svg",
            assets / "icons/favicon.svg",
            512,
            96,
            "ThLoop favicon",
        )
        build_icon_svg(
            assets / "marks/twin-chamber-light.svg",
            assets / "icons/app-icon.svg",
            1024,
            220,
            "ThLoop app icon",
            opaque_square=True,
        )

    for source_name, variants in EXPORTS.items():
        source = assets / source_name
        if not source.is_file():
            raise SystemExit(f"Missing source SVG: {source}")
        for width, output_name in variants:
            output = assets / output_name
            output.parent.mkdir(parents=True, exist_ok=True)
            if inkscape:
                export_with_inkscape(inkscape, source, output, width)
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
