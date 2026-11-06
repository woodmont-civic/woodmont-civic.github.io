# WCA vinyl signs: materials and cutter-day plan

**Status: about 80% done, and the designs will change.** Nothing has been cut on a real machine. Prices are estimates from supplier pages checked **November 6, 2026**, and shipping is an allowance, not a quote. Nothing has been ordered.

The order list is in [materials.csv](materials.csv). Vinyl areas come from the cut files, recorded in [manifest.json](manifest.json). To change a quantity or a price, edit `source/materials_calc.py` and re-run it.

## Bottom line

| | 12-inch cutter | 24-inch cutter |
|---|---|---|
| Materials and tools | $162.04 | $198.01 |
| Shipping allowance | $20.00 | $20.00 |
| **Estimated total** | **$182.04** | **$218.01** |
| Total if magnets wait for the bird redraw | about $142 | about $157 |

That's about 9 to 11 households' dues. The total drops if the uncle already has the tools or suitable vinyl.

**Quantity assumption:** 4 yard signs, 4 "Meeting tonight" strips, 4 door magnets (two cars), and 1 table banner. Yard signs are one-sided. Two-sided signs would use about twice the yard sign vinyl, roughly 5 more feet of green on a 12-inch roll, and the rolls listed would still cover it.

## Vinyl colors

The plan assumes outdoor permanent adhesive vinyl. Oracal 651 is rated up to 6 years outdoors for standard colors and 4 years for metallics ([Atlanta Vinyl](https://atlantavinylstore.com/products/oracal-651-permanent-vinyl), [SignWarehouse](https://signwarehouse.com/collections/oracal-651)). These matches come from color names only, so **check them on a $3.49 color chart before buying rolls.**

| Design color | Screen hex | Proposed stock | Notes |
|---|---|---|---|
| Forest green | `#1b4d1f` | 651 **613 Forest Green** | 060 Dark Green is the backup |
| Gold | `#c98a14` | 651 **020 Golden Yellow** | Non-metallic, so it lasts longer. It has lower contrast on white than the green, so check the join line from driving distance. If it's hard to read, cut the same file in green. 824 Imitation Gold and 091 Gold Metallic are alternatives |
| Warbler black | `#16181a` | 651 **070 Black** | |
| Warbler rust | `#b8682a` | 651 **081 Light Brown** | Least certain match. Compare with 083 Nut Brown and 092 Copper Metallic on the chart |

## Per sign

Ink is the vinyl left on the sign. Piece area is the total of the rectangles around each piece, which is closer to what you use. The thinnest stroke is measured from the cut file (5th percentile of stroke widths).

| Sign | Size and stock | Qty | Color | Ink, sq in each | Piece area, sq in each | Thinnest stroke | Longest piece |
|---|---|---|---|---|---|---|---|
| Yard sign | 24 × 18 in, 4 mm corrugated plastic | 4 | Green | 80.6 | 185.2 | 0.06 in | 14.4 in (seal) |
| | | | Gold | 4.0 | 13.7 | 0.16 in | 10.8 in |
| Meeting strip | 24 × 6 in, cut from a blank | 4 | Green | 23.3 | 65.8 | 0.13 in | 20.2 in |
| Door magnet | 24 × 12 in, 30 mil magnet | 4 | Black | 19.7 | 96.8 | 0.04 in | 11.1 in |
| | | | Rust | 13.6 | 50.3 | 0.16 in | 11.6 in |
| Table banner | 72 × 24 in, 13 oz grommeted | 1 | Green | 244.2 | 659.9 | 0.14 in | 50.2 in |
| | | | Gold | 16.8 | 55.9 | 0.22 in | 16.8 in |

The 0.04-inch strokes on the magnet are mostly in the bird trace, and the 0.06-inch strokes on the yard sign are in the seal and the serif letters. Either could tear during weeding. The test cut will show whether they hold.

Hardware and substrate by sign:

- **Yard sign:** one 18 × 24 in blank and one 10 × 30 in H-stake each. The flutes must run along the 18-inch side so the stake slides in from the bottom. The product page doesn't state flute direction, so confirm before ordering. US Cutter sells [blanks with a flute choice](https://uscutter.com/18-x-24-corrugated-plastic-sheets) at about $2.20 each.
- **Meeting strip:** cut one blank across its 18-inch side into three 24 × 6 in strips. Four strips use two blanks and leave two spares. The strip sits on top of the yard sign, joined by two 10-inch pieces of stiff wire pushed into the flutes of both boards. This is untested, so check it in wind. Use the strip only for meetings open to all neighbors, since it says "All neighbors welcome."
- **Door magnet:** pre-cut rounded blanks, sold in sets of 2.
- **Table banner:** one pre-grommeted 2 × 6 ft blank. Confirm its grommet layout against the proof before cutting. Roll it with the lettering facing out and never fold it, since this vinyl is made for flat surfaces.

## Vinyl needed for the whole run

These lengths include a 1/2-inch gap between pieces, 20% for waste, and 1 foot per color for test cuts. They assume about 11.5 or 23.5 inches of usable width.

| Color | 12-in plan needs | 12-in roll to buy | 24-in plan needs | 24-in roll to buy |
|---|---|---|---|---|
| Green | 21.3 ft | 10 yd, $18.95 | 12.3 ft | 5 yd, $22.95 |
| Gold | 2.7 ft | 5 yd, $11.95 | 2.7 ft | 5 yd, $22.95 |
| Black | 6.0 ft | 5 yd, $9.95 | 4.0 ft | 5 yd, $19.95 |
| Rust | 4.4 ft | 5 yd, $11.95 | 3.0 ft | 5 yd, $22.95 |
| Transfer tape | 27.9 ft | 2 × 5 yd, $20.98 | 14.0 ft | 1 × 5 yd, $20.95 |

## Combined order list

SignWarehouse is the single source here to keep shipping simple. Its pages showed these items in stock on November 6, 2026.

**Both plans**

| Item | Qty | Each | Total |
|---|---:|---:|---:|
| [Oracal 651 color chart](https://signwarehouse.com/collections/oracal-651), buy first | 1 | $3.49 | $3.49 |
| [Corrugated blanks, 18 × 24 in, white, pack of 5](https://signwarehouse.com/products/endura-corrugated-plastic-sign-blanks-packs) | 1 | $9.99 | $9.99 |
| [Corrugated blank, single](https://signwarehouse.com/products/endura-corrugated-plastic-sign-blanks) | 2 | $2.49 | $4.98 |
| [H-stakes, 10 × 30 in, pack of 5](https://signwarehouse.com/products/endurastakes-yard-sign-stakes-10-in-x-30-in-packs) | 1 | $9.99 | $9.99 |
| [Magnet blanks, 12 × 24 in, gloss white, set of 2](https://signwarehouse.com/products/enduramag-pre-cut-magnetic-sign-blanks-set-of-2) | 2 | $8.99 | $17.98 |
| [Banner blank, 13 oz, 2 × 6 ft, white](https://signwarehouse.com/products/enduramax-13-oz-premium-grommeted-banner-blanks-all-sizes-4-colors) | 1 | $11.95 | $11.95 |
| [Weeding tool](https://signwarehouse.com/products/signwarehouse-dual-weeding-tool), skip if the uncle has them | 2 | $3.95 | $7.90 |
| [4-inch squeegee](https://signwarehouse.com/products/yellow-4-in-poly-blend-squeegee), skip if the uncle has them | 2 | $2.99 | $5.98 |
| Stiff galvanized wire, 8 pieces about 10 in long; hardware store or from home, price not looked up | 1 lot | $4.00 | $4.00 |
| Rubbing alcohol, lint-free cloths, masking tape, utility knife, and ruler; local or from home, price not looked up | 1 lot | $12.00 | $12.00 |
| **Subtotal** | | | **$88.26** |

**Add one vinyl set**

| Item | 12-inch plan | 24-inch plan |
|---|---:|---:|
| Forest Green (613) | [10 yd](https://signwarehouse.com/products/oracal-651-adhesive-craft-vinyl-12-in-x-10-yds), $18.95 | [5 yd](https://signwarehouse.com/products/oracal-651-adhesive-vinyl-24-in-x-5-yds), $22.95 |
| Golden Yellow (020) | [5 yd](https://signwarehouse.com/products/oracal-651-adhesive-craft-vinyl-12-in-x-5-yds), $11.95 | 5 yd, $22.95 |
| Black (070) | 5 yd, $9.95 | 5 yd, $19.95 |
| Light Brown (081) | 5 yd, $11.95 | 5 yd, $22.95 |
| [Medium-tack transfer tape](https://signwarehouse.com/products/2670-series-clear-grid-transfer-tape-medium-tack) | 2 × 12 in × 5 yd, $20.98 | 1 × 24 in × 5 yd, $20.95 |
| **Subtotal** | **$73.78** | **$109.75** |

For comparison, ordering these signs printed looks like about $310 or more: about [$30 per yard sign](https://www.quill.com/custom-full-color-plastic-yard-signs-18-x-24-4-mm-white-corrugated-plastic-2-sided-horizontal/cbs/55348591.html), [$36 to $50 per magnet](https://www.magnetguys.com/12x24-Custom-Round-Corners-Outdoor-Car-Sign-Magnets-30-Mil), and [$44 or more for a banner](https://www.4over4.com/product/business-banners). These are listed prices, not quotes, and they don't include the strips.

## What depends on the cutter

| Question | 12-inch cutter | 24-inch cutter |
|---|---|---|
| Banner seal | Fits. The seal is set to 17.5 in tall by 10.8 in wide, smaller than the mock's 18.8 in, so one file works on both machines | Fits. It could go back up to 18.8 in tall |
| Yard sign lettering | Cut each line separately, then align on the sign | Can be cut and applied as one block |
| Roll or mat | **A mat machine is the main risk.** Three banner pieces are longer than a typical 24-inch mat: the name line at 50.2 in, "Association" at 26.7 in, and the web address at 24.8 in. Split them at letter gaps | Normally roll-fed, so no splitting |
| Transfer tape | 12-inch rolls | 24-inch rolls |

The seal must stay about 6 inches tall or larger.

## Cutter-day plan

**Before the day**

1. Send the uncle the questions below and the `cut-files` folder.
2. Buy the color chart first, confirm the colors, then order everything else. Allow time for shipping.
3. Open each file in the cutter's software and compare its size with the table in the README. Some programs ignore inch sizes on import.
4. If the Warbler redraw isn't ready, leave the magnets for a second session.
5. Clean the boards, magnets, and banner with rubbing alcohol and let them dry. Apply indoors on a warm, flat table, since cold weather can weaken the bond.

**Cut order, grouped by color so each roll loads once**

| Order | Color | Cut | Copies | Rough cut time |
|---|---|---|---:|---:|
| 1 | Green | **Test cut first:** the seal at 6 and 8 in tall, plus "Civic Association" from the magnet at full size | 1 | 15 min, plus checking |
| 2 | Green | Meeting strip | 4 | 10 min |
| 3 | Green | Yard sign | 4 | 30 min |
| 4 | Green | Banner | 1 | 20 min |
| 5 | Gold | Yard sign line, then banner lines | 4 + 1 | 10 min |
| 6 | Rust | Magnet, after the redraw | 4 | 15 min |
| 7 | Black | Magnet, after the redraw | 4 | 15 min |

**Rough volunteer time, all estimates until the test cut:**

| Sign | Cut, weed, and apply, each | Run total |
|---|---:|---:|
| Yard sign | 60 min (the seal takes most of the weeding) | 4 hr |
| Meeting strip | 15 min | 1 hr |
| Door magnet | 50 min (two layers to line up) | 3.5 hr |
| Table banner | 1.5 hr | 1.5 hr |
| **Total** | | **about 10 volunteer hours** |

With 2 or 3 people, that's a 4-to-5-hour day. Without the magnets, it's about 6.5 volunteer hours, or a 3-hour day. Weed in stages while the machine cuts so nobody is waiting on it.

## Questions for the uncle

1. What's the make and model, and what's the actual usable cut width?
2. Does it feed from a roll or use a mat? What's the longest piece it can cut accurately?
3. What file types does its software take? These files are SVG, and we can make DXF or another format if needed.
4. What vinyl and transfer tape are on hand, and in what colors? Is any of it rated for outdoor use?
5. Can we run a test cut of the seal before ordering all the vinyl?
6. How much time could the machine be available, and is there a table big enough to weed and apply a 6-foot banner?
7. How would the uncle like to be thanked or reimbursed for blades and wear?
