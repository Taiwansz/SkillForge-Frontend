#!/usr/bin/env python3
"""Rebuild faithful path-only SVG logos from the approved TokLang raster masters."""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
MASTER = ASSETS / "png"

WINE = "#4A1824"
YELLOW = "#FFD324"
MIST = "#ECEDEF"
SILVER = "#D9DADC"

SOURCES = {
    "stacked": MASTER / "toklang-stacked-industrial.png",
    "extended": MASTER / "toklang-extended-industrial.png",
    "flow": MASTER / "toklang-flow-industrial.png",
}


def masks(path: Path) -> tuple[np.ndarray, np.ndarray]:
    rgba = np.asarray(Image.open(path).convert("RGBA"))
    rgb = rgba[..., :3].astype(np.int16)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    yellow = (r > 145) & (g > 95) & (b < 155) & ((r + g) > (2.15 * b))
    wine = (r < 175) & (r > (1.45 * g)) & (r > (1.18 * b)) & ~yellow
    # Close single-pixel extraction gaps without filling intentional counters.
    structure = np.ones((3, 3), dtype=bool)
    wine = ndimage.binary_closing(wine, structure)
    yellow = ndimage.binary_closing(yellow, structure)

    def remove_specks(mask: np.ndarray, minimum: int) -> np.ndarray:
        labels, count = ndimage.label(mask)
        sizes = np.bincount(labels.ravel())
        keep = sizes >= minimum
        keep[0] = False
        return keep[labels]

    return remove_specks(wine, 18), remove_specks(yellow, 28)


def vector_path(mask: np.ndarray, upscale: int = 4) -> str:
    enlarged = Image.fromarray((mask * 255).astype("uint8")).resize(
        (mask.shape[1] * upscale, mask.shape[0] * upscale), Image.Resampling.BICUBIC
    )
    field = ndimage.gaussian_filter(np.asarray(enlarged, dtype=float) / 255, sigma=2.0)
    figure, axis = plt.subplots(figsize=(1, 1), dpi=72)
    contours = axis.contour(field, levels=[0.5])
    segments = contours.allsegs[0]
    plt.close(figure)
    commands = []
    for segment in segments:
        if len(segment) < 4:
            continue
        points = segment / upscale
        commands.append(f"M{points[0,0]:.2f},{points[0,1]:.2f}")
        commands.extend(f"L{x:.2f},{y:.2f}" for x, y in points[1:])
        commands.append("Z")
    return "".join(commands)


def svg_document(title: str, width: int, height: int, wine_path: str, yellow_path: str, *, dark: bool) -> str:
    ink = MIST if dark else WINE
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
  <title id="title">{title}</title>
  <path d="{wine_path}" fill="{ink}" fill-rule="evenodd"/>
  <path d="{yellow_path}" fill="{YELLOW}" fill-rule="evenodd"/>
</svg>
'''


def icon_document(title: str, size: int, width: int, height: int, wine_path: str, yellow_path: str) -> str:
    scale = (size * .80) / width
    x = (size - width * scale) / 2
    y = (size - height * scale) / 2
    radius = round(size * .22)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" role="img" aria-labelledby="title">
  <title id="title">{title}</title>
  <rect width="{size}" height="{size}" rx="{radius}" fill="{SILVER}"/>
  <g transform="translate({x:.3f} {y:.3f}) scale({scale:.6f})">
    <path d="{wine_path}" fill="{WINE}" fill-rule="evenodd"/>
    <path d="{yellow_path}" fill="{YELLOW}" fill-rule="evenodd"/>
  </g>
</svg>
'''


def main() -> int:
    built = {}
    for name, source in SOURCES.items():
        image = Image.open(source)
        wine_mask, yellow_mask = masks(source)
        built[name] = (image.width, image.height, vector_path(wine_mask), vector_path(yellow_mask))

    for name, stem, title in [
        ("stacked", "logos/toklang-stacked", "TokLang stacked logo"),
        ("extended", "logos/toklang-extended", "TokLang extended logo"),
        ("flow", "marks/toklang-flow", "TokLang compact flow mark"),
    ]:
        width, height, wine_path, yellow_path = built[name]
        for theme in ("light", "dark"):
            output = ASSETS / f"{stem}-{theme}.svg"
            output.write_text(svg_document(title, width, height, wine_path, yellow_path, dark=theme == "dark"), encoding="utf-8")
            print(f"rebuilt {output.relative_to(ROOT)}")

    width, height, wine_path, yellow_path = built["flow"]
    for output_name, size, title in [
        ("icons/favicon.svg", 64, "TokLang favicon"),
        ("icons/app-icon.svg", 512, "TokLang app icon"),
        ("icon.svg", 64, "TokLang skill icon"),
    ]:
        output = ASSETS / output_name
        output.write_text(icon_document(title, size, width, height, wine_path, yellow_path), encoding="utf-8")
        print(f"rebuilt {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
