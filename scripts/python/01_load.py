"""
01_load.py -- Load raw data. No transformations, no derivations.

This script's only job is to read files into DataFrames and pickle them for
02_clean.py to pick up. It should be boring and idempotent.
"""

import os
import pickle
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_SEED = int(os.environ.get("PROJECT_SEED", 20260413))
np.random.seed(PROJECT_SEED)

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "_outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# pd.read_csv(...) / pd.read_excel(...)   # uncomment as needed

# ---- Example: replace with your real load calls ----------------------------
# raw_main = pd.read_csv(REPO_ROOT / "data" / "raw" / "pyrolysis_yields.csv")

# Placeholder dataset so the pipeline runs end-to-end on a fresh fork.
# Delete this when you wire up real data.
raw_main = pd.DataFrame(
    {
        "run_id": np.arange(1, 51),
        "temperature_c": np.repeat([400, 500, 600, 700, 800], 10),
        "biochar_yield_pct": np.random.normal(loc=35, scale=4, size=50),
    }
)

with open(OUT_DIR / "raw_main.pkl", "wb") as f:
    pickle.dump(raw_main, f)

print(f"Loaded {len(raw_main)} rows into `raw_main`.")
