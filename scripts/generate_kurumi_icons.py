# -*- coding: utf-8 -*-
"""Generate high-resolution Victorian Gothic Kurumi Tokisaki (Zafkiel) UI icons."""

import math
import os
from PIL import Image, ImageDraw, ImageFilter

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static", "icons"))
SCALE = 4  # 4x supersampling for ultra crisp anti-aliasing

def create_canvas(size=(128, 128)):
    w, h = size[0] * SCALE, size[1] * SCALE
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    return im, draw, w, h

def save_scaled(im, filename, target_size=(128, 128)):
    out = im.resize(target_size, Image.Resampling.LANCZOS)
    path = os.path.join(OUTPUT_DIR, filename)
    out.save(path, "PNG")
    print(f"Generated {filename} -> {path} ({target_size})")

# ----------------------------------------------------------------------
# 1. Voice / Mic Icon (Zafkiel Astral Microphone & Clock Resonance)
# ----------------------------------------------------------------------
def generate_mic_icon(active=False):
    im, draw, W, H = create_canvas((128, 128))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255) if active else (212, 175, 55, 240)
    gold_dark = (197, 160, 89, 255) if active else (160, 128, 50, 220)
    crimson = (255, 30, 70, 255) if active else (196, 30, 58, 235)
    ruby = (255, 20, 60, 255) if active else (180, 15, 40, 240)

    # Vintage Gothic Studio Microphone Capsule
    cap_w = 22 * SCALE
    cap_h = 34 * SCALE
    top_y = cy - 24 * SCALE
    bot_y = top_y + cap_h

    # Acoustic Grille Outer Frame (Capsule shape)
    draw.rounded_rectangle([cx - cap_w/2, top_y, cx + cap_w/2, bot_y], radius=int(cap_w/2), fill=(26, 8, 14, 255), outline=gold, width=int(2.5*SCALE))
    
    # Horizontal grille bars across mic capsule
    for y_bar in range(int(top_y + 8*SCALE), int(bot_y - 4*SCALE), int(5*SCALE)):
        draw.line([cx - cap_w/2 + 3*SCALE, y_bar, cx + cap_w/2 - 3*SCALE, y_bar], fill=gold_dark, width=int(1.5*SCALE))

    # Center Ruby Clock Gem on mic
    draw.ellipse([cx - 7*SCALE, cy - 8*SCALE, cx + 7*SCALE, cy + 6*SCALE], fill=ruby, outline=gold, width=int(1.5*SCALE))
    draw.line([cx, cy - 1*SCALE, cx, cy - 5*SCALE], fill=gold, width=int(1.5*SCALE))
    draw.line([cx, cy - 1*SCALE, cx + 3*SCALE, cy + 2*SCALE], fill=gold, width=int(1.5*SCALE))

    # Mic stem and base
    stem_w = 6 * SCALE
    draw.rectangle([cx - stem_w/2, bot_y, cx + stem_w/2, bot_y + 16*SCALE], fill=gold)
    draw.ellipse([cx - 16*SCALE, bot_y + 14*SCALE, cx + 16*SCALE, bot_y + 24*SCALE], fill=(26, 8, 14, 255), outline=gold, width=int(2*SCALE))

    # Curved Gothic Acoustic Cradle (U-mount)
    draw.arc([cx - 24*SCALE, cy - 12*SCALE, cx + 24*SCALE, bot_y + 6*SCALE], 0, 180, fill=gold, width=int(2.5*SCALE))
    draw.ellipse([cx - 27*SCALE, cy - 15*SCALE, cx - 21*SCALE, cy - 9*SCALE], fill=ruby, outline=gold, width=int(1.5*SCALE))
    draw.ellipse([cx + 21*SCALE, cy - 15*SCALE, cx + 27*SCALE, cy - 9*SCALE], fill=ruby, outline=gold, width=int(1.5*SCALE))

    # Radiating Astral Soundwaves flanking
    for i, offset in enumerate([14, 26, 38]):
        alpha = int(240 - i * 50) if active else int(180 - i * 50)
        col = (255, 30, 70, alpha) if active else (212, 175, 55, alpha)
        w_arc = int(2*SCALE)
        # Left waves
        draw.arc([cx - (24+offset)*SCALE, cy - 20*SCALE, cx - (4+offset)*SCALE, cy + 16*SCALE], 120, 240, fill=col, width=w_arc)
        # Right waves
        draw.arc([cx + (4+offset)*SCALE, cy - 20*SCALE, cx + (24+offset)*SCALE, cy + 16*SCALE], 300, 60, fill=col, width=w_arc)

    return im

# ----------------------------------------------------------------------
# 2. Agent / Workshop Icon (Kurumi's Crossed Flintlock & Musket)
# ----------------------------------------------------------------------
def generate_agent_icon(active=False):
    im, draw, W, H = create_canvas((128, 128))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255) if active else (212, 175, 55, 240)
    steel = (245, 235, 220, 255) if active else (210, 195, 180, 230)
    wood = (140, 20, 40, 255) if active else (95, 14, 28, 240)
    ruby = (255, 30, 70, 255) if active else (196, 30, 58, 230)

    # GUN 1: Long Musket (slanted -45 deg: stock at bottom-left, muzzle at top-right)
    # Line from (-44, 44) to (44, -44)
    # Barrel: from (0, 0) to (44, -44)
    # Stock: from (-44, 44) to (0, 0)
    cos45, sin45 = math.cos(math.radians(45)), math.sin(math.radians(45))
    def musket_pt(along, perp):
        # along: along diagonal towards top-right (+X, -Y)
        # perp: perpendicular (+X, +Y)
        x = cx + (along * cos45 + perp * sin45) * SCALE
        y = cy + (-along * sin45 + perp * cos45) * SCALE
        return (x, y)

    # Musket barrel (slender steel)
    draw.polygon([musket_pt(0, -2.5), musket_pt(48, -2.5), musket_pt(48, 2.5), musket_pt(0, 2.5)], fill=steel)
    draw.polygon([musket_pt(42, -4), musket_pt(48, -4), musket_pt(48, 4), musket_pt(42, 4)], fill=gold) # Muzzle crown
    draw.polygon([musket_pt(20, -3.5), musket_pt(24, -3.5), musket_pt(24, 3.5), musket_pt(20, 3.5)], fill=gold) # Mid band
    # Musket stock (long, elegant rifle stock)
    draw.polygon([musket_pt(0, -3), musket_pt(-42, -3), musket_pt(-48, 8), musket_pt(-38, 12), musket_pt(0, 4)], fill=wood)
    draw.polygon([musket_pt(-42, -3), musket_pt(-48, 8), musket_pt(-52, 6), musket_pt(-46, -5)], fill=gold) # Brass buttplate

    # GUN 2: Flintlock Pistol (slanted +45 deg: muzzle at top-left, grip at bottom-right)
    def pistol_pt(along, perp):
        # along: along diagonal towards top-left (-X, -Y)
        # perp: perpendicular (-X, +Y)
        x = cx + (-along * cos45 - perp * sin45) * SCALE
        y = cy + (-along * sin45 + perp * cos45) * SCALE
        return (x, y)

    # Pistol barrel (shorter, ornate brass/steel)
    draw.polygon([pistol_pt(0, -3), pistol_pt(40, -3), pistol_pt(40, 3), pistol_pt(0, 3)], fill=steel)
    draw.polygon([pistol_pt(34, -4.5), pistol_pt(40, -4.5), pistol_pt(40, 4.5), pistol_pt(34, 4.5)], fill=gold) # Muzzle
    draw.polygon([pistol_pt(16, -4), pistol_pt(20, -4), pistol_pt(20, 4), pistol_pt(16, 4)], fill=gold)
    # Pistol curved grip
    draw.polygon([pistol_pt(0, -3), pistol_pt(-20, -3), pistol_pt(-36, 16), pistol_pt(-30, 22), pistol_pt(0, 4)], fill=wood)
    draw.ellipse([pistol_pt(-34, 18)[0]-5*SCALE, pistol_pt(-34, 18)[1]-5*SCALE, pistol_pt(-34, 18)[0]+5*SCALE, pistol_pt(-34, 18)[1]+5*SCALE], fill=gold) # Pommel

    # Central Interlocking Zafkiel Gear unifying the two guns
    gear_r = 15 * SCALE
    draw.ellipse([cx - gear_r, cy - gear_r, cx + gear_r, cy + gear_r], fill=(26, 8, 14, 255), outline=gold, width=int(2.5*SCALE))
    # 8 Gear teeth
    for deg in range(0, 360, 45):
        rad = math.radians(deg)
        tx = cx + (gear_r + 2*SCALE) * math.cos(rad)
        ty = cy + (gear_r + 2*SCALE) * math.sin(rad)
        draw.ellipse([tx - 2.5*SCALE, ty - 2.5*SCALE, tx + 2.5*SCALE, ty + 2.5*SCALE], fill=gold)
    # Ruby Core
    draw.ellipse([cx - 7*SCALE, cy - 7*SCALE, cx + 7*SCALE, cy + 7*SCALE], fill=ruby, outline=gold, width=int(1.5*SCALE))

    return im

# ----------------------------------------------------------------------
# 3. Community / Shadow Domain Icon (Zafkiel Astral Clockwork Vortex)
# ----------------------------------------------------------------------
def generate_community_icon(active=False):
    im, draw, W, H = create_canvas((128, 128))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255) if active else (212, 175, 55, 240)
    crimson = (255, 30, 70, 255) if active else (196, 30, 58, 230)
    dark_shadow = (25, 6, 14, 255) if active else (16, 4, 9, 240)
    ruby = (255, 20, 60, 255) if active else (180, 15, 40, 240)

    # Outer Roman Dial Ring
    dial_r = 48 * SCALE
    draw.ellipse([cx - dial_r, cy - dial_r, cx + dial_r, cy + dial_r], fill=dark_shadow, outline=gold, width=3*SCALE)
    
    # Inner border
    draw.ellipse([cx - (dial_r-6*SCALE), cy - (dial_r-6*SCALE), cx + (dial_r-6*SCALE), cy + (dial_r-6*SCALE)], outline=crimson, width=2*SCALE)

    # 12 Roman Tick Marks / Dots
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        r_inner = dial_r - 4*SCALE
        r_outer = dial_r - (8*SCALE if i % 3 == 0 else 6*SCALE)
        x1 = cx + r_inner * math.cos(angle)
        y1 = cy + r_inner * math.sin(angle)
        x2 = cx + r_outer * math.cos(angle)
        y2 = cy + r_outer * math.sin(angle)
        draw.line([x1, y1, x2, y2], fill=gold, width=int(2.5*SCALE if i % 3 == 0 else 1.5*SCALE))

    # Swirling Shadow Spirals / Astral Tendrils in center
    for i, rot in enumerate([0, 120, 240]):
        spiral_pts = []
        for step in range(18):
            a = math.radians(rot + step * 18)
            r = (8 + step * 1.8) * SCALE
            spiral_pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        for j in range(len(spiral_pts)-1):
            col = crimson if (i+j)%2 == 0 else gold
            draw.line([spiral_pts[j], spiral_pts[j+1]], fill=col, width=int(2.5*SCALE))

    # Clock Hands: Hour hand pointing to 7 (210 deg), Minute hand pointing to 12 (-90 deg)
    # Minute hand (long, ornate spear)
    draw.line([cx, cy, cx, cy - 32*SCALE], fill=gold, width=int(3*SCALE))
    draw.polygon([(cx, cy - 36*SCALE), (cx - 4*SCALE, cy - 28*SCALE), (cx + 4*SCALE, cy - 28*SCALE)], fill=gold)

    # Hour hand (pointing to 7 o'clock = 210 deg)
    h_rad = math.radians(120)  # 7 o'clock in cartesian is ~120 deg down-left
    hx = cx - 22*SCALE * math.sin(math.radians(30))
    hy = cy + 22*SCALE * math.cos(math.radians(30))
    draw.line([cx, cy, hx, hy], fill=gold, width=int(3.5*SCALE))
    draw.ellipse([hx - 3*SCALE, hy - 3*SCALE, hx + 3*SCALE, hy + 3*SCALE], fill=ruby)

    # Center jewel
    draw.ellipse([cx - 7*SCALE, cy - 7*SCALE, cx + 7*SCALE, cy + 7*SCALE], fill=ruby, outline=gold, width=2*SCALE)

    return im

# ----------------------------------------------------------------------
# 4. Settings Icon (Zafkiel Master Chrono Gear & Roman Dial XII)
# ----------------------------------------------------------------------
def generate_settings_icon(active=False):
    im, draw, W, H = create_canvas((128, 128))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255) if active else (212, 175, 55, 240)
    gold_dark = (197, 160, 89, 255) if active else (150, 120, 45, 220)
    crimson = (255, 30, 70, 255) if active else (196, 30, 58, 230)
    ruby = (255, 20, 60, 255) if active else (180, 15, 40, 240)

    # Main Cogwheel Rim
    outer_r = 46 * SCALE
    inner_r = 34 * SCALE
    
    # 8 Gear cogs around perimeter
    num_teeth = 8
    for i in range(num_teeth):
        ang = math.radians(i * (360 / num_teeth))
        # Cog shape
        w_tooth = 8 * SCALE
        h_tooth = 7 * SCALE
        tx = cx + outer_r * math.cos(ang)
        ty = cy + outer_r * math.sin(ang)
        draw.ellipse([tx - 6*SCALE, ty - 6*SCALE, tx + 6*SCALE, ty + 6*SCALE], fill=gold)

    # Outer Gear Ring
    draw.ellipse([cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r], fill=(20, 6, 12, 255), outline=gold, width=3*SCALE)
    draw.ellipse([cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r], outline=crimson, width=2*SCALE)

    # Exposed Inner Clockwork Spokes (3 diagonal ornate cross-bars)
    for deg in [30, 90, 150]:
        rad = math.radians(deg)
        x1 = cx + inner_r * math.cos(rad)
        y1 = cy + inner_r * math.sin(rad)
        x2 = cx - inner_r * math.cos(rad)
        y2 = cy - inner_r * math.sin(rad)
        draw.line([x1, y1, x2, y2], fill=gold, width=int(3*SCALE))

    # Roman numeral XII at the top of the gear
    xii_y = cy - 20 * SCALE
    # X
    draw.line([cx - 10*SCALE, xii_y - 5*SCALE, cx - 2*SCALE, xii_y + 5*SCALE], fill=gold, width=int(2*SCALE))
    draw.line([cx - 2*SCALE, xii_y - 5*SCALE, cx - 10*SCALE, xii_y + 5*SCALE], fill=gold, width=int(2*SCALE))
    # I
    draw.line([cx + 3*SCALE, xii_y - 5*SCALE, cx + 3*SCALE, xii_y + 5*SCALE], fill=gold, width=int(2*SCALE))
    # I
    draw.line([cx + 8*SCALE, xii_y - 5*SCALE, cx + 8*SCALE, xii_y + 5*SCALE], fill=gold, width=int(2*SCALE))

    # Center Chrono Boss & Ruby Core
    draw.ellipse([cx - 12*SCALE, cy - 12*SCALE, cx + 12*SCALE, cy + 12*SCALE], fill=(30, 8, 16, 255), outline=gold, width=int(2.5*SCALE))
    draw.ellipse([cx - 6*SCALE, cy - 6*SCALE, cx + 6*SCALE, cy + 6*SCALE], fill=ruby)

    return im

# ----------------------------------------------------------------------
# 5. Rest / Dismiss Icon (Kurumi's Gothic Velvet Rose & Thorn Ribbon)
# ----------------------------------------------------------------------
def generate_rest_icon(active=False):
    im, draw, W, H = create_canvas((128, 128))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255) if active else (212, 175, 55, 240)
    crimson = (255, 30, 70, 255) if active else (196, 30, 58, 240)
    crimson_dark = (160, 15, 35, 255) if active else (110, 10, 24, 240)
    ruby = (255, 20, 60, 255) if active else (180, 15, 40, 240)

    # Entwined Thorn Vine Circle
    vine_r = 44 * SCALE
    draw.arc([cx - vine_r, cy - vine_r, cx + vine_r, cy + vine_r], 30, 330, fill=gold, width=int(2.5*SCALE))
    # Thorns
    for deg in [60, 120, 180, 240, 300]:
        rad = math.radians(deg)
        tx = cx + vine_r * math.cos(rad)
        ty = cy + vine_r * math.sin(rad)
        # Thorn point outward
        ox = cx + (vine_r + 6*SCALE) * math.cos(rad + 0.1)
        oy = cy + (vine_r + 6*SCALE) * math.sin(rad + 0.1)
        draw.line([tx, ty, ox, oy], fill=gold, width=int(2.5*SCALE))

    # Gothic Velvet Rose Petals
    # Layer 1: Outer Petals (5 petals)
    for i in range(5):
        ang = math.radians(i * 72 - 90)
        px = cx + 20*SCALE * math.cos(ang)
        py = cy + 20*SCALE * math.sin(ang)
        draw.ellipse([px - 16*SCALE, py - 16*SCALE, px + 16*SCALE, py + 16*SCALE], fill=crimson_dark, outline=gold, width=int(1.5*SCALE))

    # Layer 2: Mid Petals (5 petals, rotated)
    for i in range(5):
        ang = math.radians(i * 72 - 54)
        px = cx + 12*SCALE * math.cos(ang)
        py = cy + 12*SCALE * math.sin(ang)
        draw.ellipse([px - 11*SCALE, py - 11*SCALE, px + 11*SCALE, py + 11*SCALE], fill=crimson, outline=gold, width=int(1.5*SCALE))

    # Layer 3: Rose Core Swirl
    draw.ellipse([cx - 8*SCALE, cy - 8*SCALE, cx + 8*SCALE, cy + 8*SCALE], fill=ruby, outline=gold, width=2*SCALE)
    draw.arc([cx - 5*SCALE, cy - 5*SCALE, cx + 5*SCALE, cy + 5*SCALE], 45, 270, fill=gold, width=int(2*SCALE))

    # Little sleep/stardust orbs flanking
    for ox, oy in [(-30, -32), (32, -28), (28, 30)]:
        draw.ellipse([cx + ox*SCALE - 3*SCALE, cy + oy*SCALE - 3*SCALE, cx + ox*SCALE + 3*SCALE, cy + oy*SCALE + 3*SCALE], fill=gold)

    return im

# ----------------------------------------------------------------------
# 6. Mic Trigger Badge (Play Trigger Triangle / Arrow)
# ----------------------------------------------------------------------
def generate_trigger_icon():
    im, draw, W, H = create_canvas((64, 64))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255)
    ruby = (230, 25, 60, 255)

    # Sleek equilateral triangle pointing right
    # Base at left, apex at right
    pts = [
        (cx + 14*SCALE, cy),
        (cx - 12*SCALE, cy - 15*SCALE),
        (cx - 8*SCALE, cy),
        (cx - 12*SCALE, cy + 15*SCALE)
    ]
    draw.polygon(pts, fill=ruby, outline=gold)
    draw.line([pts[0], pts[1]], fill=gold, width=int(2*SCALE))
    draw.line([pts[1], pts[2]], fill=gold, width=int(2*SCALE))
    draw.line([pts[2], pts[3]], fill=gold, width=int(2*SCALE))
    draw.line([pts[3], pts[0]], fill=gold, width=int(2*SCALE))
    
    return im

# ----------------------------------------------------------------------
# 7. Send Button (Zafkiel Astral Bullet / Chrono Arrow - REPLACING CAT PAW)
# ----------------------------------------------------------------------
def generate_send_icon():
    im, draw, W, H = create_canvas((52, 52))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255)
    gold_dark = (212, 175, 55, 255)
    ruby = (255, 25, 65, 255)
    ruby_dark = (160, 15, 35, 255)

    # Background circle: Ornate Crimson & Gold Pocket Watch Bezel
    r = 24 * SCALE
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(26, 8, 14, 255), outline=gold, width=int(2.5*SCALE))
    draw.ellipse([cx - (r-3*SCALE), cy - (r-3*SCALE), cx + (r-3*SCALE), cy + (r-3*SCALE)], outline=ruby, width=int(1.5*SCALE))

    # Zafkiel Astral Bullet / Arrow pointing Northeast (top-right, send angle 45 deg)
    # Apex at top-right
    tip = (cx + 11*SCALE, cy - 11*SCALE)
    # Wing Left
    wl = (cx - 11*SCALE, cy - 3*SCALE)
    # Wing Right
    wr = (cx + 3*SCALE, cy + 11*SCALE)
    # Tail Center indent
    tail = (cx - 3*SCALE, cy + 3*SCALE)

    # Bullet body
    draw.polygon([tip, wr, tail, wl], fill=ruby, outline=gold)
    
    # Golden spine line
    draw.line([tail, tip], fill=gold, width=int(2*SCALE))
    # Golden tip point
    draw.ellipse([tip[0]-2.5*SCALE, tip[1]-2.5*SCALE, tip[0]+2.5*SCALE, tip[1]+2.5*SCALE], fill=gold)

    return im

# ----------------------------------------------------------------------
# 8. Chat Header Icon (Zafkiel Pocket Watch Seal)
# ----------------------------------------------------------------------
def generate_chat_icon():
    im, draw, W, H = create_canvas((64, 64))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255)
    gold_dark = (212, 175, 55, 240)
    ruby = (255, 25, 65, 255)

    # Top crown / ring of pocket watch
    draw.ellipse([cx - 8*SCALE, cy - 30*SCALE, cx + 8*SCALE, cy - 18*SCALE], outline=gold, width=int(2*SCALE))
    draw.rectangle([cx - 4*SCALE, cy - 22*SCALE, cx + 4*SCALE, cy - 16*SCALE], fill=gold)

    # Watch casing
    r = 20 * SCALE
    draw.ellipse([cx - r, cy - r + 3*SCALE, cx + r, cy + r + 3*SCALE], fill=(22, 6, 12, 255), outline=gold, width=int(2.5*SCALE))
    draw.ellipse([cx - (r-3*SCALE), cy - (r-3*SCALE) + 3*SCALE, cx + (r-3*SCALE), cy + (r-3*SCALE) + 3*SCALE], outline=ruby, width=int(1.5*SCALE))

    # Center ruby & hands
    draw.ellipse([cx - 4*SCALE, cy - 4*SCALE + 3*SCALE, cx + 4*SCALE, cy + 4*SCALE + 3*SCALE], fill=ruby, outline=gold, width=int(1*SCALE))
    draw.line([cx, cy + 3*SCALE, cx, cy - 10*SCALE + 3*SCALE], fill=gold, width=int(2*SCALE))
    draw.line([cx, cy + 3*SCALE, cx + 7*SCALE, cy + 5*SCALE + 3*SCALE], fill=gold, width=int(2*SCALE))

    return im

# ----------------------------------------------------------------------
# 9. Window Minimize Orb (Replacing Cat Yarn Ball with Chrono Sphere)
# ----------------------------------------------------------------------
def generate_expand_icon(active=False):
    im, draw, W, H = create_canvas((128, 128))
    cx, cy = W / 2, H / 2
    
    gold = (255, 215, 0, 255) if active else (212, 175, 55, 240)
    crimson = (255, 30, 70, 255) if active else (196, 30, 58, 235)
    ruby = (255, 20, 60, 255) if active else (180, 15, 40, 240)

    # Outer Astral Chrono Sphere
    r = 48 * SCALE
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(22, 6, 14, 255), outline=gold, width=int(3.5*SCALE))
    
    # Intersecting golden orbital rings (Armillary Sphere / Astral Gear bands)
    draw.ellipse([cx - r, cy - 22*SCALE, cx + r, cy + 22*SCALE], outline=gold, width=int(2.5*SCALE))
    draw.ellipse([cx - 22*SCALE, cy - r, cx + 22*SCALE, cy + r], outline=gold, width=int(2.5*SCALE))
    draw.ellipse([cx - (r-8*SCALE), cy - (r-8*SCALE), cx + (r-8*SCALE), cy + (r-8*SCALE)], outline=crimson, width=int(2*SCALE))

    # Central Kurumi Zafkiel Ruby Core
    core_r = 16 * SCALE
    draw.ellipse([cx - core_r, cy - core_r, cx + core_r, cy + core_r], fill=ruby, outline=gold, width=int(2.5*SCALE))
    
    # 4 Cardinal Astral Prongs
    draw.line([cx, cy - core_r, cx, cy - (core_r + 14*SCALE)], fill=gold, width=int(2.5*SCALE))
    draw.line([cx, cy + core_r, cx, cy + (core_r + 14*SCALE)], fill=gold, width=int(2.5*SCALE))
    draw.line([cx - core_r, cy, cx - (core_r + 14*SCALE), cy], fill=gold, width=int(2.5*SCALE))
    draw.line([cx + core_r, cy, cx + (core_r + 14*SCALE), cy], fill=gold, width=int(2.5*SCALE))

    return im

def main():
    print("Beginning generation of Kurumi Zafkiel UI assets...")
    
    # 1. Mic
    save_scaled(generate_mic_icon(active=False), "mic_icon_off.png", (128, 128))
    save_scaled(generate_mic_icon(active=True), "mic_icon_on.png", (128, 128))
    
    # 2. Agent / Workshop (Crossed Guns)
    save_scaled(generate_agent_icon(active=False), "Agent_off.png", (128, 128))
    save_scaled(generate_agent_icon(active=True), "Agent_on.png", (128, 128))

    # 3. Community / Shadow Domain (Zafkiel Clock Swirl)
    save_scaled(generate_community_icon(active=False), "neko_community_off.png", (128, 128))
    save_scaled(generate_community_icon(active=True), "neko_community_on.png", (128, 128))

    # 4. Settings (Zafkiel Master Gear)
    save_scaled(generate_settings_icon(active=False), "set_off.png", (128, 128))
    save_scaled(generate_settings_icon(active=True), "set_on.png", (128, 128))

    # 5. Rest / Dismiss (Velvet Rose)
    save_scaled(generate_rest_icon(active=False), "rest_off.png", (128, 128))
    save_scaled(generate_rest_icon(active=True), "rest_on.png", (128, 128))

    # 6. Mic Trigger
    save_scaled(generate_trigger_icon(), "play_trigger_icon.png", (64, 64))

    # 7. Send Button (Replacing Cat Paw!)
    save_scaled(generate_send_icon(), "send_new_icon.png", (52, 52))
    save_scaled(generate_send_icon(), "send_icon.png", (52, 52))

    # 8. Chat Header Icon
    save_scaled(generate_chat_icon(), "chat_icon.png", (64, 64))

    # 9. Window Minimize Orb (Replacing Yarn Ball)
    save_scaled(generate_expand_icon(active=False), "expand_icon_off.png", (128, 128))
    save_scaled(generate_expand_icon(active=True), "expand_icon_on.png", (128, 128))
    save_scaled(generate_expand_icon(active=False), "expand_icon_off_ball.png", (128, 128))

    print("All Kurumi Zafkiel UI assets successfully synthesized!")

if __name__ == "__main__":
    main()
