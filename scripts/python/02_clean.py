"""
02_clean.py -- Type coercion, missingness handling, unit conversion, derived
columns. Reads what 01_load.py wrote; writes what 03_analyze.py will read.
"""

import os
import pickle
from pathlib import Path

import numpy as np

PROJECT_SEED = int(os.environ.get("PROJECT_SEED", 20260413))
np.random.seed(PROJECT_SEED)

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "_outputs"

with open(OUT_DIR / "raw_main.pkl", "rb") as f:
    raw_main = pickle.load(f)

# ---- Example transformations ------------------------------------------
# - Coerce dtypes explicitly (don't rely on pandas inference for units/IDs)
# - Report and handle missingness explicitly (never silently drop rows)
# - Convert units to a single consistent basis (e.g., all masses in g, all
#   temperatures in degC) and document the basis in a comment
df = raw_main.copy()
df["temperature_c"] = df["temperature_c"].astype(float)
df["biochar_yield_pct"] = df["biochar_yield_pct"].astype(float)

n_missing = df.isna().sum().sum()
if n_missing:
    print(f"WARNING: {n_missing} missing values across {df.shape[1]} columns.")

with open(OUT_DIR / "df.pkl", "wb") as f:
    pickle.dump(df, f)

print(f"Cleaned data: {df.shape[0]} rows, {df.shape[1]} columns.")
