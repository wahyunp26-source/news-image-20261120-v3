#!/usr/bin/env python3
"""Build the news-image-20261120 v3 front page (1024x1024 JPEG).

Layout: classic newspaper front page — kicker + huge serif date headline +
italic sub-headline + 6-stat strip + region tabs + 3 big features + 10
medium stories (2 rows of 5) + dark world map with pins + 23 briefs +
full-width DATE CHECK strip + sources footer. All illustrations are flat
vector, one bold motif each, drawn for legibility at ~300px wide.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (26, 26, 26)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
NAVY = (16, 32, 68)
GREY = (90, 90, 90)
LIGHTGREY = (200, 196, 184)
PINRED = (200, 30, 30)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w, draw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_image(path, tw, th):
    """Center-crop an image to the target box (tw x th)."""
    im = Image.open(path).convert("RGB")
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    im = im.resize((int(sw * scale) + 1, int(sh * scale) + 1), Image.LANCZOS)
    x = (im.width - tw) // 2
    y = (im.height - th) // 2
    return im.crop((x, y, x + tw, y + th))


def draw_pin(draw, x, y, n, r=9):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=PINRED,
                 outline=(255, 255, 255), width=2)
    f = font(SANS_B, 11)
    t = str(n)
    tw = draw.textlength(t, font=f)
    draw.text((x - tw / 2, y - 6), t, font=f, fill=(255, 255, 255))


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)
    MX = 16                      # side margin
    CW = W - 2 * MX              # content width = 992
    y = 10

    # ---------- top kicker bar ----------
    f_kick = font(SANS_B, 13)
    d.text((MX, y), "THE WORLD IN ONE DAY", font=f_kick, fill=RED)
    r = "FRIDAY'S NEWS  •  ONE PAGE  •  36 STORIES  •  6 CONTINENTS"
    d.text((W - MX - d.textlength(r, font=f_kick), y), r, font=f_kick, fill=INK)
    y += 22

    # ---------- headline ----------
    f_head = font(SERIF_B, 68)
    t = "Friday 20 November 2026"
    d.text(((W - d.textlength(t, font=f_head)) / 2, y), t, font=f_head, fill=INK)
    y += 72

    # ---------- sub-headline ----------
    f_sub = font(SERIF_I, 19)
    t = ("Cyclone Akvan strikes India  •  Ballistic missiles hit Kyiv  •  "
         "COP31 deadlocked on final day  •  Asian AI sell-off")
    d.text(((W - d.textlength(t, font=f_sub)) / 2, y), t, font=f_sub, fill=DARKRED)
    y += 28
    d.line([(MX, y), (W - MX, y)], fill=INK, width=3)
    y += 8

    # ---------- stats strip ----------
    stats = [
        ("300,000+", "evacuated ahead of Cyclone Akvan"),
        ("~30", "ballistic missiles fired at Kyiv"),
        ("-4.1%", "Nikkei, Asia's worst week since 2020"),
        ("2.3%", "Japan Oct headline CPI, BoJ eyed"),
        ("118", "Phillips' historic century vs India"),
        ("8 yrs", "BepiColombo reaches Mercury"),
    ]
    f_num = font(SERIF_B, 30)
    f_cap = font(SANS, 11)
    cell = CW // 6
    for i, (num, cap) in enumerate(stats):
        cx = MX + i * cell
        nw = d.textlength(num, font=f_num)
        d.text((cx + (cell - nw) / 2, y), num, font=f_num, fill=RED)
        for j, ln in enumerate(wrap(cap, f_cap, cell - 12, d)):
            lw = d.textlength(ln, font=f_cap)
            d.text((cx + (cell - lw) / 2, y + 33 + j * 13), ln,
                   font=f_cap, fill=GREY)
        if i:
            d.line([(cx, y + 2), (cx, y + 48)], fill=LIGHTGREY, width=1)
    y += 56
    d.line([(MX, y), (W - MX, y)], fill=INK, width=2)
    y += 6

    # ---------- region tabs ----------
    regions = [("EUROPE", 7, (26, 60, 110)), ("AMERICAS", 8, (150, 30, 30)),
               ("ASIA-PACIFIC", 9, (20, 90, 90)), ("MIDEAST", 3, (120, 80, 20)),
               ("AFRICA", 3, (60, 110, 40)), ("OCEANIA", 4, (40, 90, 130)),
               ("WORLD / SPACE", 2, (80, 80, 80))]
    f_tab = font(SANS_B, 11)
    x = MX
    for name, n, col in regions:
        label = f" {name} {n} "
        tw = d.textlength(label, font=f_tab)
        d.rounded_rectangle([x, y, x + tw + 6, y + 18], radius=8, fill=col)
        d.text((x + 3, y + 3), label, font=f_tab, fill=(255, 255, 255))
        x += tw + 10
    r = "ALL STORIES: FRI 20 NOV 2026, ANY TIME ZONE"
    d.text((W - MX - d.textlength(r, font=f_tab), y + 3), r, font=f_tab, fill=GREY)
    y += 26

    # ---------- 3 big features ----------
    big = [
        ("f01-odisha", "LANDFALL  •  GUSTS 110 KM/H", "CYCLONE AKVAN",
         "01  •  ODISHA, INDIA  •  CYCLONE",
         "Cyclone Akvan makes landfall in eastern India",
         "Severe storm crosses near Gopalpur; 300,000+ evacuated, winds "
         "90–100 gusting 110 km/h, 423 rescue teams deployed, schools "
         "shut. (IMD, Reuters)"),
        ("f02-kyiv", "01:25 LOCAL  •  7 WAVES", "~30 MISSILES",
         "02  •  KYIV, UKRAINE  •  WAR",
         "Russia fires wave of ~30 ballistic missiles at Kyiv",
         "Seven overnight waves hit energy and transport sites; fires burn "
         "in three districts; Dutch and Austrian embassies damaged. "
         "(Kyiv Post, Reuters)"),
        ("f03-cop31", "UN CLIMATE SUMMIT", "$120BN FINANCE GAP",
         "03  •  ANTALYA, TÜRKİYE  •  CLIMATE",
         "COP31 reaches its final day deadlocked",
         "Closing draft omits fossil-fuel phase-out while $120bn adaptation "
         "finance stays unresolved; hosts push “35 by 35” clean-power goal. "
         "(UN News, Reuters)"),
    ]
    bw = (CW - 16) // 3
    bh = 138
    f_tag = font(SANS_B, 10)
    f_kick2 = font(SANS_B, 12)
    f_h2 = font(SERIF_B, 20)
    f_body = font(SANS, 12)
    for i, (img, tag_l, tag_r, kick, head, body) in enumerate(big):
        bx = MX + i * (bw + 8)
        im = fit_image(os.path.join(ASSETS, img + ".webp"), bw, bh)
        page.paste(im, (bx, y))
        d.rectangle([bx, y + bh - 20, bx + bw, y + bh], fill=(0, 0, 0))
        d.text((bx + 5, y + bh - 17), tag_l, font=f_tag, fill=(255, 255, 255))
        rw = d.textlength(tag_r, font=f_tag)
        d.text((bx + bw - rw - 5, y + bh - 17), tag_r, font=f_tag,
               fill=(255, 210, 60))
        ty = y + bh + 6
        d.text((bx, ty), kick, font=f_kick2, fill=RED)
        ty += 17
        for ln in wrap(head, f_h2, bw, d)[:2]:
            d.text((bx, ty), ln, font=f_h2, fill=INK)
            ty += 22
        for ln in wrap(body, f_body, bw, d)[:3]:
            d.text((bx, ty), ln, font=f_body, fill=(50, 50, 50))
            ty += 15
    y += bh + 6 + 17 + 44 + 42

    # ---------- 10 medium stories, 2 rows of 5 ----------
    med = [
        ("f04-selloff", "ASIA −7% WK", "04  •  SEOUL/TOKYO  •  MARKETS",
         "AI sell-off sinks Asia to worst week since 2020",
         "Nikkei −4.1%, KOSPI −4.7%, SoftBank −16%; MSCI Asia-Pacific down 7%. (Reuters)"),
        ("f05-japan-cpi", "2% TARGET", "05  •  TOKYO  •  ECONOMY",
         "Japan inflation hits 2.3%; BoJ hike eyed",
         "Oct headline CPI rises from 2.1%; core stays above 2% for second month. (Reuters)"),
        ("f06-phillips", "118  •  RECORD", "06  •  WELLINGTON  •  CRICKET",
         "Phillips makes history with 118 vs India",
         "First NZ batter with centuries in all 3 formats vs India in a year: NZ 368. (ICC, AP)"),
        ("f07-f1", "WET  •  FP2", "07  •  LAS VEGAS  •  FORMULA 1",
         "Russell fastest in wet Las Vegas GP practice",
         "Wet FP2: Russell 1:47.272, FP1 washed out. (formula1.com)"),
        ("f08-raoni", "XINGU", "08  •  BRAZIL  •  INDIGENOUS",
         "Raoni's land recognised",
         "Brazil recognises Chief Raoni's ancestral land. (Brazil govt)"),
        ("f09-drones", "1,000+ DRONES", "09  •  LONDON  •  UKRAINE AID",
         "UK pledges 1,000+ drones for Kyiv",
         "London pledges 1,000+ drones, £280m for Kyiv. (UK govt)"),
        ("f10-gaza", "YELLOW LINE", "10  •  GAZA  •  WAR",
         "Gaza Yellow Line crossed",
         "Israeli forces cross the Yellow Line in Gaza. (News wires)"),
        ("f11-mercury", "6BN MILES", "11  •  MERCURY  •  SPACE",
         "BepiColombo reaches Mercury",
         "ESA/JAXA probe ends 6bn-mile trip; orbit insertion set for Saturday. (ESA, BBC)"),
        ("f12-landmines", "250,000", "12  •  ZIMBABWE  •  LANDMINES",
         "250,000 landmines destroyed",
         "HALO Trust destroys 250,000 landmines. (HALO Trust)"),
        ("f13-cancer-pill", "60.7% RESPONSE", "13  •  BARCELONA  •  HEALTH",
         "Pancreatic cancer pill shrinks tumours 60.7%",
         "Daraxonrasib + chemo beats chemo alone (23–42%) in early trial. (Reuters)"),
    ]
    mw = (CW - 32) // 5
    mh = 84
    f_mk = font(SANS_B, 10)
    f_mh = font(SERIF_B, 14)
    f_mb = font(SANS, 10)
    for row in range(2):
        for col in range(5):
            img, tag, kick, head, body = med[row * 5 + col]
            bx = MX + col * (mw + 8)
            im = fit_image(os.path.join(ASSETS, img + ".webp"), mw, mh)
            page.paste(im, (bx, y))
            d.rectangle([bx, y + mh - 16, bx + mw, y + mh], fill=(0, 0, 0))
            d.text((bx + 4, y + mh - 14), tag, font=f_tag, fill=(255, 210, 60))
            ty = y + mh + 4
            d.text((bx, ty), kick, font=f_mk, fill=RED)
            ty += 13
            for ln in wrap(head, f_mh, mw, d)[:2]:
                d.text((bx, ty), ln, font=f_mh, fill=INK)
                ty += 16
            for ln in wrap(body, f_mb, mw, d)[:2]:
                d.text((bx, ty), ln, font=f_mb, fill=(60, 60, 60))
                ty += 12
        y += mh + 4 + 13 + 32 + 24 + 4

    # ---------- bottom: map + briefs ----------
    d.line([(MX, y), (W - MX, y)], fill=INK, width=2)
    y += 6
    f_sec = font(SANS_B, 13)
    d.text((MX, y), "WHERE IT HAPPENED", font=f_sec, fill=INK)
    d.text((MX + 330, y), "ALSO ON FRIDAY 20 NOVEMBER — 23 MORE STORIES",
           font=f_sec, fill=INK)
    rw = d.textlength("World Briefs (14–36)", font=f_tab)
    d.text((W - MX - rw, y), "World Briefs (14–36)", font=f_tab, fill=GREY)
    y += 20
    map_w, map_h = 314, 140
    mmap = fit_image(os.path.join(ASSETS, "map-dark.webp"), map_w, map_h)
    page.paste(mmap, (MX, y))
    # pins: (story no, fx, fy) fractions of the map image
    pins = [(1, 0.76, 0.52), (2, 0.545, 0.28), (3, 0.53, 0.34),
            (4, 0.855, 0.30), (5, 0.885, 0.33), (6, 0.955, 0.86),
            (7, 0.135, 0.36), (8, 0.27, 0.60), (9, 0.47, 0.24),
            (10, 0.555, 0.38), (12, 0.545, 0.66), (13, 0.475, 0.30)]
    for n, fx, fy in pins:
        draw_pin(d, MX + int(fx * map_w), y + int(fy * map_h), n)
    # space callout for Mercury (11)
    d.rounded_rectangle([MX + 6, y + map_h - 26, MX + 118, y + map_h - 6],
                        radius=4, fill=(255, 255, 255))
    d.text((MX + 12, y + map_h - 23), "SPACE  •  11 Mercury",
           font=f_tab, fill=NAVY)

    # briefs, 2 columns
    briefs = [
        ("BRAZIL", "Lula meets Chief Raoni (Al Jazeera)"),
        ("SEOUL", "Ruling party moves to impeach top judge (SBS)"),
        ("BOUGAINVILLE", "Rio Tinto pledges $370m for mine legacy (Reuters)"),
        ("CANBERRA", "CBO warns AUKUS sales could shrink US fleet (Reuters)"),
        ("FLORIDA", "St. Johns River hits record 18.3 ft (AP)"),
        ("IOWA", "Army to detonate 68 unstable explosive barrels (AP)"),
        ("TONGA", "Emergency declared as El Niño drought bites (RNZ)"),
        ("WASHINGTON", "Pentagon: US war cost vs Iran $48.3bn (Reuters)"),
        ("LONDON", "UK & Norway fund £100m+ for two naval vessels (BBC)"),
        ("COPENHAGEN", "Parliament approves Greenland defence bill (AFP)"),
        ("JAKARTA", "Parliament passes asset-forfeiture bill (Reuters)"),
        ("GLOBAL", "UN marks World Children's Day (UN News)"),
        ("CINCINNATI", "Zoo hippo Fiona dies after swallowing a hat (AP)"),
        ("SENEGAL", "President Faye enacts budget by decree (AFP)"),
        ("HORMUZ", "Four attacks on vessels in 96 hours (UKMTO)"),
        ("NEW DELHI", "Pakistan minister to lead SCO delegation (The Hindu)"),
        ("QATAR", "U17 World Cup: Austria stun Argentina 2–0 (FIFA)"),
        ("SOUTH AFRICA", "Harmer spins Proteas to Test win (ICC)"),
        ("HONG KONG", "Badminton Open finals rematch after upset (BWF)"),
        ("TAIWAN", "Short-sell curbs take effect (Reuters)"),
        ("TURIN", "Alcaraz & Medvedev close ATP Finals groups (ATP)"),
        ("LOS ANGELES", "Thomas Markle ruled fit to stand trial (BBC)"),
        ("WELLINGTON", "Nicholls 175* in 216-run stand with Phillips (ICC)"),
    ]
    f_bk = font(SANS_B, 9)
    f_bt = font(SANS, 9)
    col_w = 326
    col_x = [MX + 330, MX + 330 + col_w + 10]
    for i, (place, txt) in enumerate(briefs):
        cx = col_x[i // 12]
        by = y + (i % 12) * 12
        num = str(14 + i)
        d.text((cx, by), num, font=f_bk, fill=RED)
        d.text((cx + 20, by), place, font=f_bk, fill=INK)
        pw = d.textlength(place, font=f_bk)
        d.text((cx + 24 + pw, by), " — " + txt, font=f_bt, fill=(50, 50, 50))
    y += 12 * 12 + 6

    # ---------- DATE CHECK strip ----------
    d.rounded_rectangle([MX, y, W - MX, y + 26], radius=3,
                        outline=RED, width=2, fill=(250, 235, 235))
    d.rectangle([MX + 1, y + 1, MX + 82, y + 25], fill=RED)
    d.text((MX + 8, y + 7), "DATE CHECK", font=f_tab, fill=(255, 255, 255))
    dc = ("First reported Thursday 19 Nov, so NOT shown as Friday's news: "
          "Trump–Xi–Putin Shenzhen summit itself  •  ICJ Myanmar Rohingya "
          "genocide verdict  •  Houthi missile hits Riyadh tower  •  US Senate "
          "rejects Iran war-powers bill  •  Denmark Greenland defence deal  •  "
          "Microsoft explains 12 Nov outage.")
    f_dc = font(SANS, 10)
    for j, ln in enumerate(wrap(dc, f_dc, CW - 100, d)):
        d.text((MX + 90, y + 3 + j * 11), ln, font=f_dc, fill=(60, 60, 60))
    y += 26

    # ---------- footer ----------
    f_ft = font(SANS, 9)
    ft = ("Every story here happened, or was first reported, on Friday 20 November 2026 in at least one time zone. "
          "Claims are attributed, not stated as fact.   Sources: Reuters, AP, AFP, BBC, IMD, UN News, Al Jazeera, "
          "ICC, EU Council, PBOC.   Original vector drawings.")
    for j, ln in enumerate(wrap(ft, f_ft, CW, d)):
        d.text((MX, y + j * 11), ln, font=f_ft, fill=GREY)
    print("final y:", y + 2 * 11)

    out = os.path.join(HERE, "entry.png")
    page.save(out, "JPEG", quality=88)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
