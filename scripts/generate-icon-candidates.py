"""Quartz Orchid Theme - icon candidates.

Code-drawn candidates (no AI images), a light/dark contact sheet and an inline
strip. Re-runnable: every mark is redrawn from scratch.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

# palette (desaturated on purpose - the plain pink/lilac range is taken)
QUARTZ = (243, 240, 242, 255)      # #F3F0F2  quartz white
QUARTZ_D = (226, 221, 228, 255)     # #E2DDE4  shaded quartz
ORCHID = (185, 167, 204, 255)       # #B9A7CC  grey orchid
ORCHID_D = (140, 118, 163, 255)     # #8C76A3  deep orchid
GOLD = (214, 196, 158, 255)         # #D6C49E  pale gold
GOLD_D = (168, 144, 100, 255)       # #A89064  old gold
SLATE = (58, 52, 64, 255)           # #3A3440  ink slate
MIST = (176, 188, 200, 255)         # #B0BCC8  cool mist (secondary accent)

LIGHT_BG = (243, 241, 243, 255)
DARK_BG = (32, 29, 36, 255)
LIGHT_INK = (58, 50, 62, 255)
DARK_INK = (233, 226, 234, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def bez(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def poly(draw, pts, fill, outline=None, width=0):
    draw.polygon([scr(p) for p in pts], fill=fill,
                 outline=outline, width=wd(width) if width else 0)


def disc(draw, center, r, fill, outline=None, width=0):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S],
                 fill=fill, outline=outline, width=wd(width) if width else 0)


def ell(draw, box, fill, outline=None, width=0):
    draw.ellipse([box[0] * S, box[1] * S, box[2] * S, box[3] * S],
                 fill=fill, outline=outline, width=wd(width) if width else 0)


def leaf(draw, base, tip, width, bend, fill, outline=None, ow=0):
    bx, by = base
    tx, ty = tip
    dx, dy = tx - bx, ty - by
    length = math.hypot(dx, dy)
    nx, ny = -dy / length, dx / length
    mx, my = (bx + tx) / 2 + nx * bend, (by + ty) / 2 + ny * bend
    pts = bez(base, (mx + nx * width, my + ny * width), tip) + \
        bez(tip, (mx - nx * width, my - ny * width), base)[1:]
    poly(draw, pts, fill, outline, ow)


def rrect(draw, box, radius, fill, outline=None, width=0):
    draw.rounded_rectangle([box[0] * S, box[1] * S, box[2] * S, box[3] * S],
                           radius=radius * S, fill=fill, outline=outline,
                           width=wd(width) if width else 0)


def line(draw, pts, color, width, joint="curve"):
    draw.line([scr(p) for p in pts], fill=color, width=wd(width), joint=joint)


# ---------------------------------------------------------------- candidates

def cand_quartz_cluster():
    """01 - three quartz points leaning against each other."""
    img = canvas()
    d = ImageDraw.Draw(img)

    def crystal(cx, top, half, bottom, lean, body, edge):
        # tapered hexagonal column with a pointed termination
        poly(d, [(cx - half * 0.82 + lean, top + 110), (cx + half * 0.82 + lean, top + 78),
                 (cx + half, bottom), (cx - half, bottom)], body, SLATE, 18)
        poly(d, [(cx - half * 0.82 + lean, top + 110), (cx + half * 0.82 + lean, top + 78),
                 (cx + lean, top)], body, SLATE, 18)
        line(d, [(cx - half * 0.16 + lean, top + 150),
                 (cx - half * 0.16, bottom - 30)], edge, 13)

    crystal(336, 404, 92, 806, -30, QUARTZ, QUARTZ_D)
    crystal(524, 236, 108, 826, 0, QUARTZ, QUARTZ_D)
    crystal(700, 344, 86, 806, 30, QUARTZ, QUARTZ_D)

    # small shards at the base
    poly(d, [(214, 872), (270, 872), (238, 800)], QUARTZ_D, SLATE, 14)
    poly(d, [(788, 878), (846, 878), (818, 806)], GOLD, SLATE, 14)

    return finish(img)


def cand_orchid_stem():
    """02 - a sprig of orchids with two leaves."""
    img = canvas()
    d = ImageDraw.Draw(img)

    stem = bez((470, 900), (546, 640), (600, 330))
    line(d, stem, SLATE, 26)

    leaf(d, (516, 706), (286, 560), 92, -34, ORCHID, SLATE, 16)
    leaf(d, (556, 520), (800, 420), 84, 30, QUARTZ_D, SLATE, 16)

    def bloom(cx, cy, r, petal, center):
        size = int(r * 3 * S)
        for i in range(5):
            layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            ld = ImageDraw.Draw(layer)
            c = size / 2
            ld.ellipse([c - r * 0.30 * S, c - r * 1.16 * S,
                        c + r * 0.30 * S, c - r * 0.26 * S],
                       fill=petal, outline=SLATE, width=wd(13))
            layer = layer.rotate(-90 + i * 72, resample=Image.BICUBIC)
            img.alpha_composite(layer, (int(cx * S - c), int(cy * S - c)))
        disc(d, (cx, cy), r * 0.24, center, SLATE, 13)

    bloom(600, 288, 104, ORCHID, GOLD)
    bloom(462, 448, 82, QUARTZ_D, GOLD)
    bloom(592, 598, 72, ORCHID, GOLD_D)

    return finish(img)


def cand_prism():
    """03 - a prism splitting one beam into a soft spectrum."""
    img = canvas()
    d = ImageDraw.Draw(img)

    poly(d, [(104, 470), (390, 424), (390, 500), (104, 542)], GOLD, None, 0)

    poly(d, [(404, 640), (620, 236), (836, 640)], QUARTZ, SLATE, 24)
    line(d, [(470, 560), (620, 360)], QUARTZ_D, 18)

    poly(d, [(660, 480), (934, 344), (934, 396), (664, 520)], ORCHID, None, 0)
    poly(d, [(660, 500), (934, 408), (934, 456), (664, 538)], GOLD, None, 0)
    poly(d, [(664, 520), (934, 472), (934, 518), (668, 556)], MIST, None, 0)

    return finish(img)


def cand_geode_half():
    """04 - a geode cut open, crystals inside."""
    img = canvas()
    d = ImageDraw.Draw(img)

    ell(d, (150, 300, 874, 900), QUARTZ_D, SLATE, 26)
    ell(d, (250, 386, 774, 838), QUARTZ, SLATE, 20)

    def tooth(cx, base_y, h, w, fill):
        poly(d, [(cx - w, base_y), (cx + w, base_y), (cx, base_y - h)],
             fill, SLATE, 14)

    tooth(392, 748, 220, 62, ORCHID)
    tooth(512, 772, 320, 74, ORCHID_D)
    tooth(636, 748, 210, 58, GOLD)
    tooth(452, 790, 150, 44, GOLD_D)
    tooth(576, 792, 160, 46, QUARTZ_D)

    return finish(img)


def cand_chandelier():
    """05 - a crystal chandelier."""
    img = canvas()
    d = ImageDraw.Draw(img)

    line(d, [(512, 120), (512, 250)], SLATE, 18)
    disc(d, (512, 268), 34, GOLD, SLATE, 16)
    line(d, [(268, 350), (756, 350)], SLATE, 20)

    def drop(cx, cy, w, h, fill):
        poly(d, [(cx - w, cy), (cx + w, cy), (cx, cy + h)], fill, SLATE, 16)
        ell(d, (cx - w, cy - w * 0.9, cx + w, cy + w * 0.9),
            fill, SLATE, 16)

    drop(512, 430, 62, 300, QUARTZ)
    drop(300, 392, 40, 176, ORCHID)
    drop(724, 392, 40, 176, ORCHID)
    drop(404, 366, 30, 120, GOLD)
    drop(620, 366, 30, 120, GOLD)
    drop(512, 748, 48, 170, ORCHID_D)

    return finish(img)


def cand_pebble_arc():
    """06 - three pebbles in a quiet arc."""
    img = canvas()
    d = ImageDraw.Draw(img)

    def pebble(cx, cy, rx, ry, fill):
        ell(d, (cx - rx, cy - ry, cx + rx, cy + ry), fill, SLATE, 22)
        ell(d, (cx - rx * 0.42, cy - ry * 0.55,
                cx - rx * 0.02, cy - ry * 0.15), (255, 255, 255, 120))

    pebble(320, 690, 132, 96, QUARTZ_D)
    pebble(556, 560, 156, 112, ORCHID)
    pebble(742, 726, 112, 82, GOLD)

    arc = bez((200, 840), (520, 900), (836, 838))
    line(d, arc, SLATE, 20)

    return finish(img)


CANDIDATES = [
    ("01", "quartz-cluster", cand_quartz_cluster),
    ("02", "orchid-stem", cand_orchid_stem),
    ("03", "prism", cand_prism),
    ("04", "geode-half", cand_geode_half),
    ("05", "chandelier", cand_chandelier),
    ("06", "pebble-arc", cand_pebble_arc),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "QUARTZ ORCHID THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
