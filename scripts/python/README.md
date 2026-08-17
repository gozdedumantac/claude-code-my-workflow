# `scripts/python/` — Reproducibility-first analysis template

This directory ships a numbered-script template for **reproducible** data analysis, mirroring `scripts/R/` for projects (or collaborators) that prefer Python. Every script has one responsibility; all orchestration happens through `00_run_all.py`.

## Conventions

- **Run everything from `00_run_all.py`** — never run mid-pipeline scripts individually unless you're debugging.
- **Paths via `pathlib` relative to the repo root** — resolved once in `00_run_all.py` via `Path(__file__).resolve().parents[2]`, never hardcoded absolute paths.
- **Fixed seed** set once in `00_run_all.py`: `np.random.seed(20260413)` (and `random.seed(20260413)` if the stdlib `random` module is used anywhere). Stochastic scripts also re-seed locally so running them directly for debugging still produces deterministic outputs. Change only with a recorded reason in the session log.
- **Environment captured** to `scripts/python/_outputs/environment.txt` (`pip freeze` or `python -m pip list`) at the end of `00_run_all.py`, mirroring R's `sessionInfo()`.
- **Outputs to `scripts/python/_outputs/`** — tables (`.csv`, `.tex`), figures (`.pdf`, `.svg`, `.png`), and serialized objects (`.pkl` via `pickle`, or `.npz`/`.parquet` where more appropriate than pickle). `.gitignore`d in most setups; decide per-project.
- **No hardcoded absolute paths anywhere.** `/review-python` enforces this.
- **Log package versions** either via a `requirements.txt` / `environment.yml` lockfile or `/capture-environment`.

## Files

| Script | Responsibility |
| --- | --- |
| `00_run_all.py` | Orchestrator. Runs 01–05 in order, writes `environment.txt`, prints timing. |
| `01_load.py` | Read raw data (CSV/Excel) into `pandas` DataFrames. No transformations. |
| `02_clean.py` | Type coercion, missingness handling, join logic, derived columns/units. |
| `03_analyze.py` | Statistical tests, regressions, kinetic/process-model fits. Save results. |
| `04_tables.py` | Publication-ready tables → `.tex` / `.csv`. |
| `05_figures.py` | `matplotlib`/`seaborn` figures → PDF + SVG/PNG. |

## Standard stack

```
pandas, numpy, scipy, statsmodels, matplotlib, seaborn
```

Both this pipeline and `scripts/R/` accept Excel (`.xlsx`) and CSV input directly. Data exported from OriginPro, openLCA/SimaPro, or Aspen Plus should be exported to CSV/Excel first — there is no direct file-format integration with those tools.

## First-time setup

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl
```

`openpyxl` is required for `.xlsx` read/write via `pandas`.

Then run:

```bash
python scripts/python/00_run_all.py
```

Expected outputs in `scripts/python/_outputs/`:

| File | Condition |
| --- | --- |
| `fig_main.pdf` | Always |
| `fig_main.svg` | Always |
| `table_main.tex` | Always |
| `results.pkl` | Always |
| `environment.txt` | Always |

Verify:

```bash
ls scripts/python/_outputs/
```

## Reviewing

`/review-python scripts/python/03_analyze.py` runs the Python code-review agent. `/audit-reproducibility` verifies fixed seeds, no absolute paths, environment capture, and that `00_run_all.py` actually regenerates all outputs — the same contract as the R pipeline.

## Choosing R vs. Python

Both pipelines are first-class; neither is primary. `/data-analysis` infers a default from the dataset/task (e.g., an existing `.R`/`.py` script in the repo, or an explicit request) and asks if it's ambiguous. Use whichever your collaborators or downstream tooling (e.g., a Quarto slide sourcing RDS objects) expect.

## Removing this template

Once you have your own analysis, the scripts 01–05 become yours. Delete this README (or rewrite it for your project). Keep `00_run_all.py` — the convention is the part that matters.
