"""Work out vinyl and tape needs from manifest.json, then write materials.csv. Standard library only.

Change QTY, WASTE or the PRICES table and re-run. Prices are hand-entered estimates; see materials.md for the date and links.
"""
import csv, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
M = json.loads((ROOT / "manifest.json").read_text())["signs"]
QTY = {"yard-sign-24x18": 4, "meeting-strip-24x6": 4, "door-magnet-24x12": 4, "table-banner-72x24": 1}
WASTE, GAP, TEST_CUT_FT = 0.20, 0.5, 1.0  # 20% mistakes and trim, 1/2 in between pieces, 1 ft of test cuts per color
USABLE = {12: 11.5, 24: 23.5}  # a roll loses margin to the pinch rollers; confirm with the uncle
ROLL_YD = (5, 10)


def run_length(pieces, usable):
    """Simple shelf packing along the roll, with each piece's long side running with the roll."""
    items = sorted(((max(w, h), min(w, h)) for w, h in pieces), reverse=True)
    shelves = []  # [length, width used]
    for length, across in items:
        if across > usable:
            raise SystemExit(f"piece too wide for {usable} in: {length} x {across}")
        for s in shelves:
            if s[1] + across + GAP <= usable and length <= s[0]:
                s[1] += across + GAP
                break
        else:
            shelves.append([length, across])
    return sum(s[0] + GAP for s in shelves) / 12


per_sign, per_color = [], {}
for name, sign in M.items():
    for color, c in sign["colors"].items():
        ps = [(p["w"], p["h"]) for p in c["pieces"]]
        per_sign.append(dict(sign=name, color=color, qty=QTY[name], ink=c["ink_sqin"],
                             bbox=round(sum(w * h for w, h in ps), 1), thin=c["thin_stroke_p5_in"], islands=c["islands"],
                             longest=round(max(max(p) for p in ps), 1), widest_short=round(max(min(p) for p in ps), 1)))
        per_color.setdefault(color, []).extend(ps * QTY[name])

plan = {}
for color, ps in per_color.items():
    plan[color] = {"ink_sqin_run": round(sum(r["ink"] * r["qty"] for r in per_sign if r["color"] == color), 0)}
    for width, usable in USABLE.items():
        ft = run_length(ps, usable)
        total = ft * (1 + WASTE) + TEST_CUT_FT
        roll = next((y for y in ROLL_YD if y * 3 >= total), None)
        n = 1 if roll else math.ceil(total / 30)
        plan[color][width] = dict(run_ft=round(ft, 1), order_ft=round(total, 1), roll_yd=roll or 10, rolls=n)

tape_sqft = sum(sum((w + 1) * (h + 1) for w, h in ps) for ps in per_color.values()) / 144 * (1 + WASTE)
tape = {12: round(tape_sqft, 1), 24: round(tape_sqft / 2, 1)}

for r in per_sign: print(r)
print(json.dumps(plan, indent=0)); print("tape sq ft", round(tape_sqft, 1), "=> 12in ft", tape[12], "24in ft", tape[24])

# Item, used by, plan, qty, unit, unit price, link
SW = "https://signwarehouse.com/products/"
V12_5, V12_10 = SW + "oracal-651-adhesive-craft-vinyl-12-in-x-5-yds", SW + "oracal-651-adhesive-craft-vinyl-12-in-x-10-yds"
V24_5, V24_10 = SW + "oracal-651-adhesive-vinyl-24-in-x-5-yds", SW + "oracal-651-adhesive-vinyl-24-in-x-10-yds"
PRICE = {(12, 5): (11.95, V12_5), (12, 10): (18.95, V12_10), (24, 5): (22.95, V24_5), (24, 10): (32.95, V24_10)}
BLACK = {(12, 5): 9.95, (12, 10): 16.95, (24, 5): 19.95, (24, 10): 28.95}
LABEL = {"green": ("Oracal 651 Forest Green (613)", "Yard signs, strips, banner"),
         "gold": ("Oracal 651 Golden Yellow (020)", "Yard signs, banner"),
         "black": ("Oracal 651 Black (070)", "Magnets"),
         "rust": ("Oracal 651 Light Brown (081)", "Magnets")}
rows = []
for color, (name, used) in LABEL.items():
    for w in USABLE:
        p = plan[color][w]
        price, link = PRICE[(w, p["roll_yd"])]
        if color == "black": price = BLACK[(w, p["roll_yd"])]
        rows.append([f"{w}-in plan", "Vinyl", f'{name}, {w} in x {p["roll_yd"]} yd', used, p["rolls"], "roll", price, link,
                     f'needs about {p["order_ft"]} ft of {p["roll_yd"] * 3} ft'])
tape12 = 2 if tape[12] > 15 else 1
rows += [["12-in plan", "Transfer tape", "2670 clear grid, medium tack, 12 in x 5 yd", "All", tape12, "roll", 10.49, SW + "2670-series-clear-grid-transfer-tape-medium-tack", f"needs about {tape[12]} ft"],
         ["24-in plan", "Transfer tape", "2670 clear grid, medium tack, 24 in x 5 yd", "All", 1, "roll", 20.95, SW + "2670-series-clear-grid-transfer-tape-medium-tack", f"needs about {tape[24]} ft"]]
shared = [["Substrate", "Corrugated plastic blanks, 18 x 24 in, white, pack of 5", "Yard signs, strips", 1, "pack", 9.99, SW + "endura-corrugated-plastic-sign-blanks-packs", "4 yard signs + 1 spare; confirm flute direction"],
          ["Substrate", "Corrugated plastic blank, 18 x 24 in, white", "Strips", 2, "each", 2.49, SW + "endura-corrugated-plastic-sign-blanks", "each blank cuts into 3 strips: 4 strips + 2 spares"],
          ["Hardware", "H-stakes, 10 x 30 in, pack of 5", "Yard signs", 1, "pack", 9.99, SW + "endurastakes-yard-sign-stakes-10-in-x-30-in-packs", "4 + 1 spare"],
          ["Hardware", "Stiff galvanized wire, 8 pieces about 10 in long", "Strips", 1, "lot", 4.00, "", "hardware store or from home; price not looked up"],
          ["Substrate", "EnduraMAG magnet blanks, 12 x 24 in, gloss white, set of 2", "Magnets", 2, "set", 8.99, SW + "enduramag-pre-cut-magnetic-sign-blanks-set-of-2", "4 magnets, 30 mil, rounded corners"],
          ["Substrate", "EnduraMAX 13 oz banner blank, 2 x 6 ft, white, grommeted", "Banner", 1, "each", 11.95, SW + "enduramax-13-oz-premium-grommeted-banner-blanks-all-sizes-4-colors", "confirm grommet layout"],
          ["Tools", "Dual weeding tool", "Shared", 2, "each", 3.95, SW + "signwarehouse-dual-weeding-tool", "skip if the uncle has them"],
          ["Tools", "4 in squeegee", "Shared", 2, "each", 2.99, SW + "yellow-4-in-poly-blend-squeegee", "skip if the uncle has them"],
          ["Tools", "Oracal 651 color chart", "Shared", 1, "each", 3.49, SW.replace("products/", "collections/oracal-651"), "order first; check real colors before buying rolls"],
          ["Supplies", "Rubbing alcohol, lint-free cloths, masking tape, utility knife, ruler", "Shared", 1, "lot", 12.00, "", "local or from home; price not looked up"]]
for s in shared:
    rows.append(["Both plans", *s])
totals = {}
for w in USABLE:
    totals[w] = round(sum(r[4] * r[6] for r in rows if r[0] in (f"{w}-in plan", "Both plans")), 2)
ship = 20.00
with (ROOT / "materials.csv").open("w", newline="") as f:
    o = csv.writer(f)
    o.writerow(["Plan", "Category", "Item", "Used for", "Qty", "Unit", "Est unit price USD", "Est line total USD", "Supplier link (prices checked 2026-11-06)", "Note"])
    for r in rows:
        o.writerow([*r[:6], f"{r[6]:.2f}", f"{r[4] * r[6]:.2f}", *r[7:]])
    o.writerow(["Both plans", "Shipping", "Shipping allowance, not a quote", "All", 1, "lot", f"{ship:.2f}", f"{ship:.2f}", "", "supplier page says free shipping over $200"])
    for w in USABLE:
        o.writerow([f"{w}-in plan", "TOTAL", f"Estimated total with shipping, {w}-in plan", "", "", "", "", f"{totals[w] + ship:.2f}", "", "estimate"])
print("subtotals", totals, "with ship", {k: round(v + ship, 2) for k, v in totals.items()})
for r in rows: print(r[0], r[2], r[4], r[6], r[-1])
