#!/usr/bin/env python3
"""Generate PWA icons for the Beach Beer Tracker (no external deps)."""
import zlib, struct, math

def write_png(path, pix, w, h):
    raw = bytearray()
    stride = w * 4
    for y in range(h):
        raw.append(0)
        raw.extend(pix[y * stride:(y + 1) * stride])
    comp = zlib.compress(bytes(raw), 9)
    def chunk(typ, data):
        return (struct.pack(">I", len(data)) + typ + data +
                struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff))
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)))
        f.write(chunk(b"IDAT", comp))
        f.write(chunk(b"IEND", b""))

def lerp(a, b, t):
    return a + (b - a) * t

def mix(c1, c2, t):
    return tuple(lerp(c1[i], c2[i], t) for i in range(3))

def sample(u, v):
    """Return (r,g,b) for normalized coords u,v in [0,1]. Full-bleed (maskable-safe)."""
    # --- background: sky (top) into sand (bottom) ---
    horizon = 0.62
    if v < horizon:
        t = v / horizon
        col = mix((86, 184, 224), (185, 228, 240), t)   # deep sky -> hazy sky
    else:
        t = (v - horizon) / (1 - horizon)
        col = mix((244, 228, 193), (233, 210, 160), t)  # light sand -> deeper sand

    # --- sun, upper-left, with soft glow ---
    dx, dy = u - 0.27, v - 0.24
    d = math.hypot(dx, dy)
    glow = max(0.0, 1 - d / 0.30)
    col = mix(col, (255, 235, 130), glow * 0.55)
    if d < 0.135:
        col = mix(col, (255, 205, 60), min(1.0, (0.135 - d) / 0.03))

    # --- distant sea line just above horizon ---
    if horizon - 0.05 < v < horizon:
        col = mix(col, (40, 140, 180), 0.35)

    # ===== beer mug =====
    L, R, T, B = 0.355, 0.605, 0.30, 0.80   # outer glass bounds
    rad = 0.045
    def in_round_rect(x, y, l, r, t, b, cr):
        if x < l or x > r or y < t or y > b:
            return False
        cx = min(max(x, l + cr), r - cr)
        cy = min(max(y, t + cr), b - cr)
        return math.hypot(x - cx, y - cy) <= cr
    def round_rect_dist_ok(x, y, l, r, t, b, cr):
        return in_round_rect(x, y, l, r, t, b, cr)

    # handle (C-shape) on the right, drawn first so glass overlaps it
    hcx, hcy = R + 0.055, (T + B) / 2 + 0.02
    hd = math.hypot(u - hcx, v - hcy)
    if 0.085 < hd < 0.135 and u > R - 0.01:
        col = (250, 250, 248)
        return col

    if in_round_rect(u, v, L, R, T, B, rad):
        wall = 0.022
        il, ir, it, ib = L + wall, R - wall, T + wall, B - wall
        if in_round_rect(u, v, il, ir, it, ib, rad * 0.6):
            foam_line = it + 0.13
            if v < foam_line:
                # frothy foam: base white plus bumpy bottom edge
                bump = 0.012 * math.sin((u - il) / (ir - il) * math.pi * 5)
                if v < foam_line - 0.02 + bump:
                    col = (255, 252, 246)
                else:
                    col = (255, 252, 246)
            else:
                # amber beer with a subtle vertical gradient + bubbles
                bt = (v - foam_line) / (ib - foam_line)
                col = mix((247, 178, 24), (236, 150, 10), bt)
                for bx, by, br in ((0.43, 0.55, 0.012), (0.50, 0.66, 0.010),
                                   (0.46, 0.72, 0.008), (0.53, 0.50, 0.009)):
                    if math.hypot(u - bx, v - by) < br:
                        col = (255, 226, 150)
        else:
            # glass rim / wall highlight
            col = (255, 255, 255)
        return col

    return col

def render(size, ss=4):
    big = size * ss
    out = bytearray(size * size * 4)
    # accumulate supersampled
    inv = 1.0 / big
    # precompute per-target-pixel by averaging ss*ss samples
    for py in range(size):
        for px in range(size):
            r = g = b = 0.0
            for sy in range(ss):
                v = ((py * ss) + sy + 0.5) * inv
                for sx in range(ss):
                    u = ((px * ss) + sx + 0.5) * inv
                    c = sample(u, v)
                    r += c[0]; g += c[1]; b += c[2]
            n = ss * ss
            i = (py * size + px) * 4
            out[i] = int(r / n + 0.5)
            out[i+1] = int(g / n + 0.5)
            out[i+2] = int(b / n + 0.5)
            out[i+3] = 255
    return out

for sz, name in ((512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png")):
    write_png(name, render(sz), sz, sz)
    print("wrote", name)
print("done")
