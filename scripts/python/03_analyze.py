"""
03_analyze.py -- Statistical tests, regressions, kinetic/process-model fits.
Save every computed object -- tables and figures read from disk, not from
in-memory state.
"""

import os
import pickle
from pathlib import Path

import numpy as np
import statsmodels.formula.api as smf

PROJECT_SEED = int(os.environ.get("PROJECT_SEED", 20260413))
np.random.seed(PROJECT_SEED)

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "_outputs"

with open(OUT_DIR / "df.pkl", "rb") as f:
    df = pickle.load(f)

# ---- Example: replace with your real analysis ---------------------------
# ANOVA / regression for an experimental design; kinetic-model (e.g.,
# Arrhenius) fit via scipy.optimize.curve_fit; mass/energy balance check;
# LCA/TEA summary statistics. State the model, report effect sizes and
# uncertainty (not just point estimates), and check residuals.
model = smf.ols("biochar_yield_pct ~ temperature_c", data=df).fit()

results = {
    "model_summary": model.summary().as_text(),
    "params": model.params.to_dict(),
    "bse": model.bse.to_dict(),
    "rsquared": model.rsquared,
    "nobs": int(model.nobs),
}

with open(OUT_DIR / "results.pkl", "wb") as f:
    pickle.dump(results, f)

print("Analysis complete:")
print(results["model_summary"])
