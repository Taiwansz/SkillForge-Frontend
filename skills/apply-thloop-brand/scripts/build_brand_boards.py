#!/usr/bin/env python3
"""Build deterministic ThLoop reference boards from canonical SVG assets."""

from __future__ import annotations

import argparse
import pathlib

from PIL import Image, ImageDraw, ImageFont


ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BLACK = "#0A0A0A"
PAPER = "#F0EDE6"
GOLD = "#C8B560"
CHASSIS = "#2A2A2A"
MIRROR = "#5C5C5C"


def font(size: int, bold: bool = False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    return ImageFont.truetype(path, size)


def load_rgba(path: pathlib.Path) -> Image.Image:
    return Image.open(path).convert("RGBA")


def fit(image: Image.Image, box: tuple[int, int, int, int], contain: float = 0.9) -> tuple[Image.Image, tuple[int, int]]:
    x0, y0, x1, y1 = box
    scale = min((x1 - x0) * contain / image.width, (y1 - y0) * contain / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    return resized, (x0 + (x1 - x0 - resized.width) // 2, y0 + (y1 - y0 - resized.height) // 2)


def paste_fit(canvas: Image.Image, asset: Image.Image, box, contain=0.9):
    resized, pos = fit(asset, box, contain)
    canvas.alpha_composite(resized, pos)


def label(draw: ImageDraw.ImageDraw, pos, text, size=18, color=PAPER, bold=False):
    draw.text(pos, text.upper(), font=font(size, bold), fill=color)


def line(draw, xy, fill=MIRROR, width=1):
    draw.line(xy, fill=fill, width=width)


def build_system(output: pathlib.Path):
    canvas = Image.new("RGBA", (1600, 1100), BLACK)
    d = ImageDraw.Draw(canvas)
    wm = load_rgba(ASSETS / "png/thloop-wordmark-light-1080.png")
    compact = load_rgba(ASSETS / "png/twin-chamber-light-512.png")

    label(d, (30, 24), "Identity core", 17)
    label(d, (1090, 24), "Compact mark — Twin Chamber", 17)
    line(d, (1065, 20, 1065, 330), PAPER)
    paste_fit(canvas, wm, (30, 52, 1045, 305), 0.92)
    paste_fit(canvas, compact, (1080, 55, 1570, 300), 0.77)

    line(d, (0, 330, 1600, 330), MIRROR)
    label(d, (30, 352), "Visual system", 17)
    boxes = [(30, 390, 540, 650), (570, 390, 820, 650), (850, 390, 1085, 650), (1115, 390, 1570, 650)]
    titles = ["Chicane handoff", "Section divider", "Frame device", "Pattern rhythm"]
    for box, title in zip(boxes, titles):
        d.rectangle(box, fill=PAPER)
        label(d, (box[0] + 14, box[1] + 12), title, 13, BLACK)
    # Handoff
    d.rounded_rectangle((60, 470, 255, 555), radius=42, fill=BLACK)
    d.rounded_rectangle((320, 470, 510, 555), radius=42, fill=BLACK)
    d.polygon([(260, 480), (282, 502), (306, 544), (284, 522)], fill=GOLD)
    # Divider
    d.rectangle((598, 492, 790, 500), fill=BLACK)
    d.polygon([(678, 484), (688, 484), (706, 510), (696, 510)], fill=GOLD)
    # Frame
    d.rounded_rectangle((875, 445, 1060, 625), radius=18, outline=BLACK, width=22)
    d.polygon([(1028, 570), (1044, 586), (1056, 620), (1040, 604)], fill=GOLD)
    # Pattern
    for row in range(4):
        for col in range(5):
            x = 1145 + col * 78 + (row % 2) * 35
            y = 452 + row * 48
            d.rounded_rectangle((x, y, x + 62, y + 24), radius=12, fill=BLACK)
            if (row + col) % 3 == 0:
                d.polygon([(x + 48, y + 18), (x + 56, y + 26), (x + 62, y + 38), (x + 54, y + 30)], fill=GOLD)

    line(d, (0, 680, 1600, 680), MIRROR)
    label(d, (30, 704), "Brand palette", 17)
    swatches = [(BLACK, "Loop Black", "#0A0A0A"), (PAPER, "Technical Paper", "#F0EDE6"), (GOLD, "Chicane", "#C8B560"), (CHASSIS, "Chassis", "#2A2A2A"), (MIRROR, "Smoked Mirror", "#5C5C5C")]
    for i, (color, name, value) in enumerate(swatches):
        x = 30 + i * 210
        d.rounded_rectangle((x, 750, x + 168, 870), radius=8, fill=color, outline=MIRROR, width=1)
        label(d, (x, 884), name, 12)
        label(d, (x, 904), value, 12, GOLD if color == GOLD else PAPER)

    line(d, (1080, 700, 1080, 960), MIRROR)
    label(d, (1110, 704), "Identity hierarchy", 17)
    label(d, (1110, 756), "01  Continuous Core", 16, GOLD, True)
    d.text((1110, 790), "Primary signature\nHeroes · navigation · signage", font=font(16), fill=PAPER, spacing=8)
    label(d, (1110, 858), "02  Twin Chamber", 16, GOLD, True)
    d.text((1110, 892), "Official compact mark\nIcons · patches · small spaces", font=font(16), fill=PAPER, spacing=8)

    line(d, (0, 980, 1600, 980), MIRROR)
    label(d, (30, 1008), "Canonical asset board · no regenerated lettering · no logo variation", 15, PAPER)
    canvas.convert("RGB").save(output, quality=95)


def build_applications(output: pathlib.Path):
    canvas = Image.new("RGBA", (1600, 1100), BLACK)
    d = ImageDraw.Draw(canvas)
    wm = load_rgba(ASSETS / "png/thloop-wordmark-light-1080.png")
    compact = load_rgba(ASSETS / "png/twin-chamber-light-512.png")
    label(d, (34, 26), "ThLoop applications · exact master lockup", 18)
    line(d, (34, 58, 1566, 58), MIRROR)

    # Boot screen
    d.rounded_rectangle((34, 90, 930, 610), radius=18, fill="#111111", outline=CHASSIS, width=3)
    d.rounded_rectangle((75, 130, 889, 565), radius=8, fill=BLACK, outline=MIRROR, width=1)
    paste_fit(canvas, wm, (130, 230, 835, 405), 0.88)
    label(d, (365, 460), "System ready", 17, MIRROR)
    label(d, (52, 105), "01 · Boot screen", 13, GOLD)

    # App icon and mobile card
    d.rounded_rectangle((970, 90, 1566, 610), radius=18, fill=CHASSIS)
    label(d, (992, 110), "02 · Compact system", 13, GOLD)
    d.rounded_rectangle((1075, 180, 1285, 390), radius=48, fill=BLACK, outline=MIRROR, width=2)
    paste_fit(canvas, compact, (1095, 225, 1265, 350), 0.92)
    label(d, (1320, 190), "Project core", 15)
    d.rounded_rectangle((1320, 228, 1518, 292), radius=6, fill=BLACK, outline=MIRROR)
    label(d, (1338, 245), "Operational", 13, PAPER)
    d.rounded_rectangle((1320, 312, 1518, 376), radius=6, fill=BLACK, outline=MIRROR)
    label(d, (1338, 329), "Integrity 96.8%", 13, GOLD)
    d.rounded_rectangle((1070, 435, 1518, 545), radius=8, fill=BLACK)
    label(d, (1090, 455), "Twin Chamber", 13, GOLD)
    d.text((1090, 485), "Only for compact spaces.\nNever replace the wordmark when width allows.", font=font(14), fill=PAPER, spacing=7)

    # Credential
    d.rounded_rectangle((34, 655, 530, 1050), radius=16, fill=CHASSIS)
    label(d, (52, 675), "03 · Event credential", 13, GOLD)
    d.rounded_rectangle((105, 730, 458, 1008), radius=8, fill="#111111", outline=MIRROR)
    paste_fit(canvas, wm, (135, 760, 428, 838), 0.9)
    line(d, (135, 855, 428, 855), GOLD, 2)
    label(d, (135, 885), "Hackathon", 15)
    label(d, (135, 930), "Judge · all areas", 14, MIRROR)

    # Equipment badge
    d.rounded_rectangle((565, 655, 1032, 1050), radius=16, fill="#151515")
    label(d, (585, 675), "04 · Equipment badge", 13, GOLD)
    d.rounded_rectangle((620, 770, 980, 940), radius=14, fill="#202020", outline=MIRROR, width=3)
    for x, y in [(645, 795), (955, 795), (645, 915), (955, 915)]: d.ellipse((x-7, y-7, x+7, y+7), fill=BLACK, outline=MIRROR)
    paste_fit(canvas, wm, (680, 820, 920, 890), 0.9)

    # Document cover
    d.rounded_rectangle((1068, 655, 1566, 1050), radius=16, fill=CHASSIS)
    label(d, (1088, 675), "05 · Technical document", 13, GOLD)
    d.rectangle((1150, 720, 1490, 1018), fill=PAPER)
    dark_wm = load_rgba(ASSETS / "png/thloop-wordmark-dark-1080.png")
    paste_fit(canvas, dark_wm, (1180, 748, 1460, 820), 0.88)
    label(d, (1180, 850), "Project specification", 13, BLACK, True)
    d.text((1180, 882), "CORE / ITERATION / RETURN\nDOCUMENT 001\nSTATUS: VERIFIED", font=font(13), fill=MIRROR, spacing=7)
    canvas.convert("RGB").save(output, quality=95)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--system", type=pathlib.Path, default=ASSETS / "reference/thloop-brand-system.png")
    parser.add_argument("--applications", type=pathlib.Path, default=ASSETS / "reference/thloop-applications.png")
    args = parser.parse_args()
    args.system.parent.mkdir(parents=True, exist_ok=True)
    args.applications.parent.mkdir(parents=True, exist_ok=True)
    build_system(args.system)
    build_applications(args.applications)
    print(f"built {args.system.relative_to(ROOT)}")
    print(f"built {args.applications.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
