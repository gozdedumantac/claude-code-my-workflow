"""
00_run_all.py -- Orchestrator. Run this, not the individual scripts.

Reproducibility contract (enforced by /review-python and /audit-reproducibility):
  - Fixed seed set below.
  - Project root resolved via pathlib relative to this file -- no hardcoded paths.
  - Every package version logged via `pip freeze` (or a requirements.txt lockfile).
  - Outputs written to scripts/python/_outputs/ and listed at the end.
  - Environment captured so reviewers can verify the setup.
"""

import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

# Seed applies to everything downstream. Change ONLY with a reason in the
# session log -- this is load-bearing for identical numerical outputs.
PROJECT_SEED = 20260413
np.random.seed(PROJECT_SEED)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "_outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PIPELINE = [
    "01_load.py",
    "02_clean.py",
    "03_analyze.py",
    "04_tables.py",
    "05_figures.py",
]


def main() -> None:
    print(f"Running reproducibility pipeline with seed {PROJECT_SEED}...")
    timings = {}

    for script in PIPELINE:
        path = SCRIPT_DIR / script
        if not path.exists():
            raise FileNotFoundError(f"Missing pipeline script: {path}")

        start = time.time()
        child_env = {**os.environ, "PROJECT_SEED": str(PROJECT_SEED)}
        result = subprocess.run(
            [sys.executable, str(path)],
            cwd=REPO_ROOT,
            env=child_env,
        )
        if result.returncode != 0:
            raise RuntimeError(f"{script} failed with exit code {result.returncode}")
        elapsed = time.time() - start
        timings[script] = elapsed
        print(f"  {script} -> {elapsed:.2f}s")

    # ---- Environment capture -------------------------------------------
    freeze = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True
    )
    (OUT_DIR / "environment.txt").write_text(
        f"Python: {sys.version}\n\n{freeze.stdout}"
    )

    # ---- Report -----------------------------------------------------------
    outputs = sorted(p.name for p in OUT_DIR.iterdir())
    print()
    print(f"Pipeline complete. Total time: {sum(timings.values()):.2f}s")
    print(f"Outputs in {OUT_DIR}:")
    for f in outputs:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
