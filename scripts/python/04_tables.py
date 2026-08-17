"""
04_tables.py -- Publication-ready tables from 03_analyze.py's saved results.
"""

import pickle
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "_outputs"

with open(OUT_DIR / "results.pkl", "rb") as f:
    results = pickle.load(f)

# ---- Example: a minimal regression table -------------------------------
lines = [
    r"\begin{tabular}{lcc}",
    r"\toprule",
    "Term & Estimate & SE \\\\",
    r"\midrule",
]
for term, estimate in results["params"].items():
    se = results["bse"][term]
    lines.append(f"{term} & {estimate:.3f} & ({se:.3f}) \\\\")
lines += [
    r"\bottomrule",
    f"\\multicolumn{{3}}{{l}}{{$N$ = {results['nobs']}, $R^2$ = {results['rsquared']:.3f}}} \\\\",
    r"\end{tabular}",
]

(OUT_DIR / "table_main.tex").write_text("\n".join(lines))

print(f"Wrote {OUT_DIR / 'table_main.tex'}")
