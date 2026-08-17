"""
05_figures.py -- matplotlib/seaborn figures. Transparent background,
explicit dimensions, project theme, both PDF (Beamer) and SVG (Quarto).
"""

import pickle
from pathlib import Path

import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "_outputs"

with open(OUT_DIR / "df.pkl", "rb") as f:
    df = pickle.load(f)

# ---- Project theme -------------------------------------------------------
# Match Preambles/header.tex palette when this repo's institutional colors
# are finalized; placeholders below.
PRIMARY = "#012169"
ACCENT = "#B9975B"

plt.rcParams.update(
    {
        "font.size": 14,
        "axes.edgecolor": "#333333",
        "axes.labelcolor": "#1A1A1A",
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.transparent": True,
    }
)

fig, ax = plt.subplots(figsize=(12, 5))
ax.scatter(df["temperature_c"], df["biochar_yield_pct"], color=PRIMARY, alpha=0.8)
ax.set_xlabel("Pyrolysis temperature (°C)")
ax.set_ylabel("Biochar yield (%)")
ax.set_title("Biochar yield vs. pyrolysis temperature")

fig.savefig(OUT_DIR / "fig_main.pdf", bbox_inches="tight")
fig.savefig(OUT_DIR / "fig_main.svg", bbox_inches="tight")
plt.close(fig)

print(f"Wrote {OUT_DIR / 'fig_main.pdf'} and {OUT_DIR / 'fig_main.svg'}")
