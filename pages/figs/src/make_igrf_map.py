# /// script
# requires-python = ">=3.11"
# dependencies = ["ppigrf>=2", "numpy", "matplotlib", "cartopy", "pillow"]
# ///
"""Draw the world map of the geomagnetic field used on the front page.

Field intensity is the background colour, declination the contours.

Regenerate with:

    uv run pages/figs/src/make_igrf_map.py

The output PNG is committed to the repository, so this only needs running
when the epoch or the IGRF generation changes.
"""

from datetime import datetime
from pathlib import Path

import cartopy.crs as ccrs
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import ppigrf
from PIL import Image

EPOCH = datetime(2025, 1, 1)
OUTFILE = Path(__file__).parents[1] / "igrf14_2025_map.png"

lon, lat = np.meshgrid(np.arange(-180, 181, 1.0), np.arange(-89.5, 90, 1.0))
Be, Bn, Bu = (b[0] for b in ppigrf.igrf(lon, lat, 0.0, EPOCH))
intensity = np.sqrt(Be**2 + Bn**2 + Bu**2)
declination = np.degrees(np.arctan2(Be, Bn))

fig, ax = plt.subplots(
    figsize=(10, 5.2), subplot_kw={"projection": ccrs.Robinson()}
)
ax.set_global()

filled = ax.contourf(
    lon, lat, intensity,
    levels=np.arange(22000, 66001, 2000),
    cmap="viridis", extend="both", transform=ccrs.PlateCarree(),
)
ax.coastlines(linewidth=0.5, color="0.35", alpha=0.9)

# Declination contours: red eastward, blue westward, black for the agonic
# lines (zero declination, where a compass points to true north). Every line
# carries a white outline, without which neither colour survives against both
# ends of the viridis ramp. Labelling only +/-30 keeps the convergence on the
# magnetic poles from turning into a thicket of text.
halo = [pe.withStroke(linewidth=2.4, foreground="white", alpha=0.85)]
WEST, EAST = "#1c58c4", "#d63229"


def declination_contour(level):
    """Draw one declination contour, all the way to the poles.

    Contouring the declination directly needs the +/-180 wrap masked off,
    and near the magnetic poles declination sweeps through a full turn
    within a few grid cells, so any such mask swallows whole regions. Work
    on the angular difference from the level instead: that is continuous
    across the line being drawn, and its own discontinuity sits half a turn
    away, where a narrow mask costs nothing.
    """
    delta = (declination - level + 180) % 360 - 180
    zero = level == 0
    contours = ax.contour(
        lon, lat, np.ma.masked_array(delta, np.abs(delta) > 170),
        levels=[0], colors="0.1" if zero else (EAST if level > 0 else WEST),
        linewidths=2.0 if zero else 0.9, transform=ccrs.PlateCarree(),
    )
    contours.set(path_effects=(
        [pe.withStroke(linewidth=4, foreground="white")] if zero else halo
    ))
    return contours


# The full range, not just the mid-latitude values: beyond each magnetic
# pole a compass points nearly due south or north, so leaving out the levels
# past +/-80 would leave the two polar caps blank.
labelled = {}
for level in range(-170, 171, 10):
    contours = declination_contour(level)
    if level in (-30, -20, -10, 0, 10, 20, 30):
        labelled[level] = contours

for level, contours in labelled.items():
    for label in ax.clabel(
        contours, fontsize=7, fmt={0: f"{level}°"}, inline_spacing=3
    ):
        # clabel is free to put a label hard against the map boundary, where
        # the axes clip path then slices it in half. Drop those rather than
        # ship a cropped number.
        _, y = ax.transAxes.inverted().transform(
            ax.transData.transform(label.get_position())
        )
        if 0.04 < y < 0.96:
            label.set(path_effects=halo)
        else:
            label.remove()

cbar = fig.colorbar(
    filled, ax=ax, orientation="horizontal",
    fraction=0.05, pad=0.03, aspect=45,
)
cbar.set_label("Field intensity (nT)", fontsize=9)
cbar.ax.tick_params(labelsize=8)

# The colour bar only accounts for half the figure, so spell out the other
# half. Offset in points, to clear the tick labels and the label above at
# whatever size the figure ends up.
cbar.ax.annotate(
    "Contour lines: declination (°) — eastward red, westward blue, zero black",
    xy=(0.5, 0), xycoords="axes fraction",
    xytext=(0, -36), textcoords="offset points",
    ha="center", va="top", fontsize=8, color="0.2",
)

fig.savefig(OUTFILE, dpi=150, bbox_inches="tight")

# The filled contours are only a couple of dozen flat colours, so a 256-entry
# palette is indistinguishable from truecolour and much smaller on the wire.
Image.open(OUTFILE).convert("RGB").quantize(colors=256).save(
    OUTFILE, optimize=True
)
print(f"{OUTFILE} ({OUTFILE.stat().st_size / 1024:.0f} KB)")
