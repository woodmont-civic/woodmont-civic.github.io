"""Build the WCA vinyl sign files: real-size proofs, per-color cut files with outlined text, previews, and a measurement manifest.

Run from a temp venv, not the repo:
  uv venv /tmp/signs --python 3.12
  uv pip install --python /tmp/signs/bin/python fonttools uharfbuzz skia-pathops resvg-py numpy pillow opencv-python-headless
  /tmp/signs/bin/python source/build_signs.py <dir holding Playfair.ttf and Outfit.ttf>

Fonts: Playfair Display and Outfit variable TTFs from github.com/google/fonts (SIL OFL). Not stored in the repo.
Layout coordinates below are inches. Files are written at 100 units per inch.
"""
import io, json, re, sys
from pathlib import Path

import cv2, numpy as np, pathops, uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image
import resvg_py

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(sys.argv[1])
U = 100  # file units per inch

# Screen colors for proofs and previews. materials.md maps these to stocked vinyl.
GREEN, GOLD, GREY = "#1b4d1f", "#c98a14", "#8b8374"
NAMES = {GREEN: "green", GOLD: "gold"}
NOTE = "UNTESTED on a real cutter. All text is outlined. Check size on import against manifest.json."

_fonts = {}


def font(family, wght):
    key = (family, wght)
    if key not in _fonts:
        tt = TTFont(FONTS / f"{family}.ttf")
        tt = instancer.instantiateVariableFont(tt, {"wght": wght})
        buf = io.BytesIO(); tt.save(buf)
        data = buf.getvalue()
        _fonts[key] = (TTFont(io.BytesIO(data)), hb.Font(hb.Face(data)))
    return _fonts[key]


class Piece:
    """One cuttable item, kept as its own group so it can be moved on the vinyl."""

    def __init__(self, id, color, d, source):
        self.id, self.color, self.d, self.source = id, color, d, source
        bp = BoundsPen(None)
        parse_path(d, bp)
        x0, y0, x1, y1 = bp.bounds
        self.x0, self.y0, self.x1, self.y1 = x0 / U, y0 / U, x1 / U, y1 / U
        self.w, self.h = self.x1 - self.x0, self.y1 - self.y0


def text(id, s, x, baseline, size, color, family="Outfit", wght=700, anchor="start"):
    """Shape with HarfBuzz for real kerning, then merge the whole line into one set of closed outlines."""
    tt, hf = font(family, wght)
    buf = hb.Buffer(); buf.add_str(s); buf.guess_segment_properties()
    hb.shape(hf, buf, {"kern": True, "liga": False})
    upem = tt["head"].unitsPerEm
    k = size / upem * U
    adv = sum(p.x_advance for p in buf.glyph_positions)
    ox = x * U - (adv * k / 2 if anchor == "middle" else 0)
    gs, order = tt.getGlyphSet(), tt.getGlyphOrder()
    merged = pathops.Path()
    pen_x = 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        tp = TransformPen(merged.getPen(glyphSet=gs), (k, 0, 0, -k, ox + (pen_x + pos.x_offset) * k, baseline * U))
        gs[order[info.codepoint]].draw(tp)
        pen_x += pos.x_advance
    merged.simplify(fix_winding=True)  # variable fonts overlap their strokes; a cutter would slice along those lines
    sp = SVGPathPen(None, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    merged.draw(sp)
    return Piece(id, color, sp.getCommands(), f"{family} {wght}")


# Image areas are left empty in the cut files. Images will come from community submissions.
PLACEHOLDER_LABEL = ("Image to come", "(community submission)")


PF = dict(family="Playfair", wght=700)
SIGNS = {
    "yard-sign-24x18": dict(
        title="WCA yard sign", w=24, h=18, rx=0.15, stock="4 mm corrugated plastic, flutes vertical",
        holes=[], hole_r=0,  # the strip joins with wire pushed into the top flutes
        image=(1.3, 1.75, 9.0, 14.5),
        pieces=[
                text("name-1", "Woodmont", 11.2, 4.25, 2.15, GREEN, **PF),
                text("name-2", "Civic", 11.2, 6.75, 2.15, GREEN, **PF),
                text("name-3", "Association", 11.2, 9.25, 2.15, GREEN, **PF),
                text("join", "Join for $20 a year", 11.2, 12.5, 1.25, GOLD, wght=700),
                text("url", "woodmontbonair.com", 11.2, 15.0, 1.15, GREEN, wght=600)]),
    "meeting-strip-24x6": dict(
        title="Meeting tonight swap-out strip", w=24, h=6, rx=0.15, stock="4 mm corrugated plastic, flutes vertical",
        holes=[], hole_r=0,  # the strip joins with wire pushed into the bottom flutes
        image=None,
        pieces=[text("meeting-tonight", "Meeting tonight", 12, 3.0, 2.8, GREEN, wght=700, anchor="middle"),
                text("welcome", "All neighbors welcome", 12, 5.0, 1.15, GREEN, wght=600, anchor="middle")]),
    "door-magnet-24x12": dict(
        title="WCA car door magnet", w=24, h=12, rx=0.75, stock="30 mil white magnetic sheet",
        holes=[], hole_r=0,
        image=(0.75, 1.9, 9.6, 8.2),
        pieces=[
                text("name-1", "Woodmont", 11.0, 5.0, 1.6, GREEN, **PF),
                text("name-2", "Civic Association", 11.0, 7.0, 1.42, GREEN, **PF),
                text("url", "woodmontbonair.com", 11.0, 9.1, 1.15, GREEN, wght=700)]),
    "table-banner-72x24": dict(
        title="WCA event table banner", w=72, h=24, rx=0.2, stock="13 oz white vinyl banner, hemmed, grommets",
        holes=[(1.6, 1.6), (36, 1.6), (70.4, 1.6), (1.6, 22.4), (36, 22.4), (70.4, 22.4)], hole_r=0.3,
        image=(3.6, 3.25, 10.8, 17.5),
        pieces=[
                text("name-1", "Woodmont Civic", 16.4, 11.2, 6.6, GREEN, **PF),
                text("name-2", "Association", 16.4, 17.2, 5.0, GREEN, **PF),
                text("join-1", "Come say hello", 47, 15.0, 1.9, GOLD, wght=700),
                text("join-2", "Join for $20 a year", 47, 17.6, 1.9, GOLD, wght=700),
                text("line", "Neighbors working together", 47, 21.4, 1.6, GREEN, wght=600),
                text("url", "woodmontbonair.com", 16.4, 21.4, 2.5, GREEN, wght=600)]),
}


def header(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}in" height="{h}in" viewBox="0 0 {w * U} {h * U}">'
            f"<title>{title}</title><desc>{NOTE}</desc>")


def groups(pieces):
    return "".join(f'<g id="{p.id}"><path fill="{p.color}" fill-rule="evenodd" d="{p.d}"/></g>' for p in pieces)


def render(svg, width):
    # resvg-py rejects inch sizes, so drop only the size attributes for rendering; the viewBox is unchanged.
    svg = re.sub(r' width="\d+in" height="\d+in"', "", svg, count=1)
    png = bytes(resvg_py.svg_to_bytes(svg_string=svg, width=width, background="#ffffff"))
    return Image.open(io.BytesIO(png)).convert("RGB")


def measure(svg, w, h, dpi=100):
    """Measure the written file itself: rendered ink area, plus the thinnest strokes and smallest islands."""
    arr = np.array(render(svg, w * dpi).convert("L"))
    mask = (arr < 200).astype(np.uint8)
    d = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
    ridge = (d > 0) & (d >= cv2.dilate(d, np.ones((3, 3), np.uint8)) - 1e-3)
    n, _, st, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
    areas = st[1:, cv2.CC_STAT_AREA] / dpi**2
    return dict(ink_sqin=round(float(mask.sum()) / dpi**2, 1),
                thin_stroke_p5_in=round(float(np.percentile(d[ridge] * 2, 5)) / dpi, 3),
                islands=int(n - 1), islands_under_quarter_sqin=int((areas < 0.25).sum()))


manifest = {"note": NOTE, "units": "inches; files are 100 units per inch", "signs": {}}
for name, s in SIGNS.items():
    w, h = s["w"], s["h"]
    entry = {"title": s["title"], "w_in": w, "h_in": h, "stock": s["stock"], "colors": {}}
    # Check nothing leaves the sign or runs into a hole or grommet.
    for p in s["pieces"]:
        assert p.x0 > 0.4 and p.y0 > 0.4 and p.x1 < w - 0.4 and p.y1 < h - 0.4, (name, p.id, p.x0, p.y0, p.x1, p.y1)
        for hx, hy in s["holes"]:
            gap = max(p.x0 - hx, hx - p.x1, p.y0 - hy, hy - p.y1)
            assert gap > s["hole_r"] + 0.2, (name, p.id, "hole", hx, hy, gap)
        if s["image"]:
            ix, iy, iw, ih = s["image"]
            gap = max(p.x0 - (ix + iw), ix - p.x1, p.y0 - (iy + ih), iy - p.y1)
            assert gap > 0.5, (name, p.id, "image area", gap)
    entry["image_area_in"] = dict(zip(("x", "y", "w", "h"), s["image"])) if s["image"] else None
    for c in dict.fromkeys(p.color for p in s["pieces"]):
        ps = [p for p in s["pieces"] if p.color == c]
        svg = header(w, h, f'{s["title"]}, {NAMES[c]} vinyl') + groups(ps) + "</svg>"
        for banned in ("<text", "<use", "font-family", "<style", "transform="):
            assert banned not in svg, banned
        path = ROOT / "cut-files" / f"{name}--{NAMES[c]}.svg"
        path.write_text(svg)
        render(svg, min(w * 50, 2400)).save(ROOT / "previews" / f"{name}--{NAMES[c]}.png")
        entry["colors"][NAMES[c]] = {
            "file": f"cut-files/{path.name}",
            **measure(svg, w, h),
            "bbox_in": [round(min(p.x0 for p in ps), 2), round(min(p.y0 for p in ps), 2),
                        round(max(p.x1 for p in ps), 2), round(max(p.y1 for p in ps), 2)],
            "pieces": [dict(id=p.id, w=round(p.w, 2), h=round(p.h, 2), source=p.source) for p in ps]}
    board = f'<rect id="board-not-cut" x="1" y="1" width="{w * U - 2}" height="{h * U - 2}" rx="{s["rx"] * U}" fill="#fdfdfb" stroke="#8b8374" stroke-width="2"/>'
    holes = "".join(f'<circle cx="{x * U}" cy="{y * U}" r="{s["hole_r"] * U}" fill="#d8d3c8" stroke="#8b8374" stroke-width="2"/>' for x, y in s["holes"])
    ph = ""
    if s["image"]:
        ix, iy, iw, ih = s["image"]
        cx, cy = ix + iw / 2, iy + ih / 2
        size = min(iw / 9, 0.9)
        labels = [text("label-1", PLACEHOLDER_LABEL[0], cx, cy - size * 0.2, size, GREY, wght=600, anchor="middle"),
                  text("label-2", PLACEHOLDER_LABEL[1], cx, cy + size * 1.2, size * 0.8, GREY, wght=500, anchor="middle"),
                  text("label-3", f"{iw:g} × {ih:g} in", cx, cy + size * 2.5, size * 0.7, GREY, wght=500, anchor="middle")]
        ph = (f'<g id="image-placeholder-not-cut"><rect x="{ix * U}" y="{iy * U}" width="{iw * U}" height="{ih * U}" rx="{0.2 * U}" '
              f'fill="#f1eee7" stroke="{GREY}" stroke-width="4" stroke-dasharray="24 16"/>{groups(labels)}</g>')
    proof = header(w, h, s["title"]) + f'<g id="hardware-not-cut">{board}{holes}</g>' + ph + groups(s["pieces"]) + "</svg>"
    (ROOT / "signs" / f"{name}.svg").write_text(proof)
    render(proof, 1600).save(ROOT / "previews" / f"{name}.png")
    manifest["signs"][name] = entry
    for c, v in entry["colors"].items():
        print(name, c, {k: v[k] for k in ("ink_sqin", "thin_stroke_p5_in", "islands", "islands_under_quarter_sqin", "bbox_in")})
        for p in v["pieces"]:
            print("   ", p)
(ROOT / "manifest.json").write_text(json.dumps(manifest, indent=1))
