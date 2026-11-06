# WCA vinyl signs

**Draft, about 80% done. UNTESTED on a real cutter.** The board has not approved these designs, and nothing has been ordered or cut.

| Folder or file | What it holds |
|---|---|
| `signs/` | One real-size proof per sign, with the board and holes drawn in. Not for cutting |
| `cut-files/` | One file per sign per vinyl color. Each item is its own group so it can be moved on the vinyl |
| `previews/` | PNG preview of every proof and cut file |
| `materials.md`, `materials.csv` | Materials, costs, order list, and cutter-day plan |
| `manifest.json` | Measurements taken from the cut files |
| `source/` | Build scripts and the traced art |

## Cut files

All text is converted to outlines, overlapping letter shapes are merged, and no file contains live fonts or transforms. Files are 100 units per inch. Check the size after importing:

| File | Artboard | Artwork left, top, right, bottom (in) |
|---|---|---|
| `yard-sign-24x18--green.svg` | 24 × 18 in | 1.30, 1.78, 22.63, 16.20 |
| `yard-sign-24x18--gold.svg` | 24 × 18 in | 11.22, 11.49, 22.03, 12.76 |
| `meeting-strip-24x6--green.svg` | 24 × 6 in | 1.97, 0.97, 22.18, 5.25 |
| `door-magnet-24x12--black.svg` | 24 × 12 in | 0.96, 2.08, 22.14, 10.11 |
| `door-magnet-24x12--rust.svg` | 24 × 12 in | 2.66, 2.17, 22.59, 9.11 |
| `table-banner-72x24--green.svg` | 72 × 24 in | 3.60, 3.29, 66.53, 21.81 |
| `table-banner-72x24--gold.svg` | 72 × 24 in | 47.03, 12.22, 63.78, 16.49 |

Some programs ignore inch sizes on import, so compare against this table before cutting.

## Known limits

- **Warbler bird:** an auto-traced placeholder with rough edges. It needs a hand redraw before anyone sees it up close.
- **Seal:** traced from a low-resolution scan, with visible wobble at full size. Rescan the original before permanent use, and keep it about 6 inches tall or larger.
- **Thin strokes:** a few strokes in the bird, the seal, and the serif letters are under 1/8 inch and could tear while weeding. The test cut will show.
- **Color:** screen colors only until checked against a vinyl color chart.

## Rebuilding

Run these from a temp venv, not the repo. The commands are at the top of `source/build_signs.py`. Fonts are Playfair Display and Outfit from Google Fonts (SIL Open Font License), and they aren't stored here.

```bash
python source/build_signs.py <folder with Playfair.ttf and Outfit.ttf>
python source/materials_calc.py
```
