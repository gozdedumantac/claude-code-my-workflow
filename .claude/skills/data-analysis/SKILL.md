---
name: data-analysis
description: End-to-end R or Python data analysis pipeline for experimental, thermochemical/biochemical-conversion, process, and LCA/TEA data — validation → descriptive statistics → appropriate statistical testing or modeling → publication-ready tables and figures. Use when user says "analyze this dataset", "explore this CSV/Excel file", "full analysis workflow", "compare these conditions statistically", "fit a kinetic model to this data", "check this mass balance", or points at a `.csv`/`.xlsx`/`.rds` and asks for experimental, process, or LCA/TEA results. Produces numbered scripts in `scripts/R/` or `scripts/python/` and outputs to the matching `_outputs/` directory.
argument-hint: "[dataset path or description of analysis goal]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task", "Monitor"]
---

# Data Analysis Workflow

Run an end-to-end data analysis in R or Python: validate, describe, test/model appropriately, and produce publication-ready output. This is not a regression-first pipeline — the default path is data validation and descriptive statistics; a specific statistical test, kinetic/process model, or regression is chosen because the question calls for it, not applied by default.

**Input:** `$ARGUMENTS` — a dataset path (e.g., `data/pyrolysis_yields.csv`) or a description of the analysis goal (e.g., "compare biochar yield across three feedstocks", "fit an Arrhenius model to these kinetics data", "check whether this mass balance closes", "propagate parameter uncertainty through this TEA").

---

## Constraints

- **Follow the matching code conventions:** `.claude/rules/r-code-conventions.md` for R, `.claude/rules/python-code-conventions.md` for Python
- **Save all scripts** to `scripts/R/` or `scripts/python/` with descriptive names, following the numbered-pipeline convention in each directory's README
- **Save all outputs** (figures, tables, serialized objects) to the corresponding `_outputs/` directory
- **Save every computed object** — `saveRDS()` in R, `pickle`/`.parquet`/`.npz` in Python — downstream slides/reports may need them
- **Use project theme** for all figures (check for custom theme in `.claude/rules/`)
- **Never silently drop data.** Outliers, failed replicates, and excluded points are flagged and reported, never silently removed — see Phase 2.
- **Never treat technical/analytical replicates as independent observations.** Aggregate them to one value per independent/biological unit before any statistical test; check explicitly for pseudoreplication — see Phase 1–2.
- **Run `r-reviewer` (R) or `python-reviewer` (Python)** on the generated script before presenting results

### Choosing R or Python

Both languages are first-class — neither is the default. Infer the language from context (an existing script in the repo, the user's explicit request, the collaborator/tool the output feeds into), and if genuinely ambiguous, ask. Both pipelines accept the same input formats (CSV, Excel `.xlsx`). Data exported from **OriginPro**, **openLCA/SimaPro**, or **Aspen Plus** should be exported to CSV/Excel first — this workflow does not integrate with those tools' native file formats directly.

---

## Workflow Phases

### Phase 0: Pre-Flight Report

**Before writing any analysis code, produce a Pre-Flight Report** showing you read the inputs. This prevents the common failure mode where the agent hallucinates variable names, invents units, or skips project conventions.

```markdown
## Pre-Flight Report

**Dataset:** [path]
- Variables found: [list from head()/names() or df.columns]
- Rows: [count]; replicates per condition: [n independent/biological replicates, and n technical/analytical replicates per independent unit if any — or "unclear — ask"]
- Key types: [e.g., "yield_pct=numeric, feedstock=categorical, temperature_c=numeric"]
- Units and basis: [state the basis for every quantity — dry vs. as-received, mass % vs. energy %, MJ/kg, kg CO2-eq / functional unit, cost year + discount rate for TEA, etc.]
- Missing-data summary: [% missing per key var]

**Language:** [R / Python — one-line reason for the choice]

**Task interpretation:** [one sentence restating what the user asked for]

**Plan:** [3-6 bullet outline of which phases below apply and why — not every analysis needs kinetic modeling or sensitivity analysis]
```

If any input cannot be read, or units/basis are genuinely ambiguous, stop and ask the user before proceeding — do not guess a basis.

### Phase 1: Setup, Data Loading, and Validation

1. Create a script with a proper header (title, purpose, inputs, outputs, units/basis)
2. Load required packages/imports at the top
3. Set seed once at top in YYYYMMDD format (per the matching conventions file), e.g. `set.seed(20260415)` / `np.random.seed(20260415)` (INV-9) — needed for any bootstrap, Monte Carlo, or resampling step later
4. Load the dataset and **validate before analyzing:**
   - Are units internally consistent (no mixed °C/K, mixed mass/energy basis)?
   - Do physically-constrained quantities respect their constraints (yields summing to ~100%, no negative concentrations, mass fractions in [0,1])?
   - **Classify every replicate.** Distinguish **independent/biological replicates** (separate experimental units — separate batches, separate reactor runs, separate cultures) from **technical/analytical replicates** (repeated measurements or repeated injections on the *same* experimental unit — e.g., triplicate GC-MS injections of one sample). This distinction must be explicit in the Pre-Flight Report and in the script header, not inferred silently.
   - **Check for pseudoreplication.** If technical/analytical replicates exist, they are not independent observations and must not inflate the sample size used for statistical testing. Flag any case where technical replicates appear to be feeding into a test's *n* as if they were independent units.
   - Flag anything that fails validation and stop to ask rather than silently coercing it.

### Phase 2: Descriptive Statistics, Replicates, and Outlier Assessment

- **Aggregate technical/analytical replicates before treating anything as an independent observation.** Collapse technical replicates to one summary value (typically the mean) per independent/biological unit *first* — e.g., average triplicate GC-MS injections to one value per sample before that sample enters any group comparison. The unit of statistical analysis is the independent replicate, never the technical-replicate count.
- **Per-condition summary:** mean, SD (or SE), n (independent replicates only — never inflated by technical replicates), and coefficient of variation for every measured quantity, grouped by condition
- **Report both levels of variability separately when both exist:** technical/analytical variability (within-sample measurement precision) and biological/independent variability (between-sample variation) answer different questions — conflating them overstates precision. Note where each was computed.
- **Uncertainty is reported alongside every point estimate** from here on — a mean without a spread is incomplete
- **Outlier assessment, never automatic deletion:** apply a stated, defensible rule (e.g., Grubbs' test, modified Z-score, 1.5×IQR) to *flag* candidate outliers among independent replicates. Report flagged points explicitly; do not remove them without an explicit, documented scientific justification (e.g., a recorded instrument fault) confirmed by the user. When a flagged point is excluded, report the result both with and without it.

### Phase 3: Exploratory Data Analysis

- **Distributions:** histograms/boxplots for key continuous variables, by condition
- **Relationships:** scatter plots, correlation matrices — for visual inspection, not as a substitute for a stated test
- **Process/time patterns:** if time- or temperature-resolved data (e.g., TGA weight-loss curves, batch-reactor time series), plot the trend directly
- **Group comparisons:** visual comparison (boxplot/dot plot with error bars) before any formal test

Save all diagnostic figures to the matching `_outputs/diagnostics/`.

### Phase 4: Statistical Testing and Modeling

Choose the method the question calls for — do not default to regression, and do not select a test mechanically off a single normality/variance p-value. Test choice is a judgment call informed jointly by:

- **Experimental design** — fully randomized, blocked, repeated-measures/paired, factorial? The design dictates the test family (e.g., a blocked or repeated-measures design needs a paired test, repeated-measures ANOVA, or a mixed-effects model — an unpaired test on paired data is wrong regardless of what any normality check says).
- **Independence** — confirmed by Phase 1/2 (no pseudoreplication: technical replicates already aggregated to independent units before this phase).
- **Sample size** — small-*n* designs (common in bench-scale experiments) limit which tests have any power and make normality tests themselves unreliable; don't lean on a Shapiro–Wilk result from *n* = 3–5 as decisive.
- **Distribution shape and variance structure** — inspect (histograms/QQ plots from Phase 3), don't just gate on one p-value. Shapiro–Wilk and Levene's are inputs to the decision, never the sole decision rule — they are underpowered at small *n* and oversensitive at large *n*.
- **The scientific question itself** — comparing discrete conditions vs. a continuous dose–response vs. a time-course all call for different tools even with identical data shape.

With those considered, typical choices:
- **Two-condition comparison:** two-sample t-test (independent design) or paired t-test (paired/repeated-measures design); Mann–Whitney U or Wilcoxon signed-rank as non-parametric/small-*n* alternatives.
- **Three-or-more-condition comparison:** one-way ANOVA + Tukey HSD post-hoc, repeated-measures ANOVA / mixed-effects model if the design is blocked or repeated, or Kruskal–Wallis + Dunn's post-hoc when parametric assumptions are genuinely untenable.
- **Regression** — use *only* when the scientific question is genuinely about a continuous predictor–response relationship (e.g., yield as a continuous function of temperature across a swept range), not as a default tool for comparing discrete conditions. State the model form and check residuals.
- **Kinetic / process-model fitting** — nonlinear least squares (`nls` in R, `scipy.optimize.curve_fit` in Python) for rate laws relevant to this domain (Arrhenius temperature dependence, first-order or pseudo-second-order decomposition kinetics, Monod kinetics for microbial conversion). Report parameter estimates with confidence intervals and a goodness-of-fit measure, not just point estimates.
- **Mass/energy balance check** — sum inputs vs. outputs on a consistent basis, report % closure, and flag explicitly if closure falls outside a stated tolerance (state the tolerance and its rationale).
- **LCA/TEA aggregation** — aggregate impact-category or cost results by scenario/feedstock, with the functional unit, system boundary, and (for TEA) cost year and discount rate stated in the script header, not just in prose.

**Report effect sizes and uncertainty intervals alongside every p-value, whenever appropriate** — e.g., Cohen's d or Hedges' g for a two-group comparison, eta-squared/omega-squared for ANOVA, and confidence intervals on every estimate. A p-value alone ("significant"/"not significant") without an effect size and its uncertainty is an incomplete result.

### Phase 5: Sensitivity Analysis (when the analysis involves a parameterized model)

For process models, kinetic fits, or LCA/TEA calculations with more than one input parameter:

- **One-at-a-time (OAT) sensitivity** — vary each parameter across a plausible range holding others fixed; report which parameters dominate the output.
- **Monte Carlo uncertainty propagation** — when parameter uncertainty needs to propagate jointly (not one-at-a-time), hand off to [`/simulation-study`](../simulation-study/SKILL.md) for the full DGP/replication/MCSE treatment rather than reimplementing it here.
- Report results as a tornado diagram or ranked sensitivity table, not just a list of reruns.

Skip this phase when the analysis is purely descriptive/comparative with no fitted model.

### Phase 6: Publication-Ready Output

**Tables:**
- Include every element needed to judge the result on its own: point estimate, uncertainty (SD/SE/CI), n, and (for a fitted model) a goodness-of-fit measure
- R: build via `knitr::kable()`/`gt`, or `modelsummary` *specifically when the output is a fitted regression/model object* — not as a default for every table
- Python: build the table directly as a DataFrame reshaped for output (see `scripts/python/04_tables.py`)
- Export as `.tex` for LaTeX inclusion and `.csv` for quick viewing/re-use

**Figures:**
- R: `ggplot2` with project theme. Python: `matplotlib`/`seaborn` with the project `rcParams` theme.
- Transparent background for Beamer compatibility (`bg = "transparent"` in R, `savefig.transparent` in Python)
- Proper axis labels (sentence case, units — e.g., "Pyrolysis temperature (°C)", not "temp")
- Error bars/shaded uncertainty bands wherever Phase 2/5 produced a spread
- Explicit dimensions; save as both `.pdf` and `.svg`/`.png`

### Phase 7: Save and Review

1. Save all key objects (validated data, summary statistics, test/model results, sensitivity results) — `saveRDS()` in R, `pickle`/`.parquet` in Python
2. Create output subdirectories as needed
3. Run the matching review agent on the generated script:

```
Delegate to the r-reviewer agent:
"Review the script at scripts/R/[script_name].R"

# or

Delegate to the python-reviewer agent:
"Review the script at scripts/python/[script_name].py"
```

4. Address any Critical or High issues from the review.

---

## Script Structure

Two separate templates — R and Python are independent pipelines, not a shared one. Section markers below follow the phase numbering above; for a quick one-off analysis they can live in a single script, but when producing durable output prefer distributing them across the numbered pipeline files each directory already scaffolds (`01_load`/`02_clean` cover Phases 1–2, `03_analyze` covers Phases 3–5, `04_tables` and `05_figures` cover Phase 6) per `scripts/R/README.md` / `scripts/python/README.md`.

### R (`scripts/R/`)

```r
# ============================================================
# [Descriptive Title]
# Purpose: [What this script does]
# Inputs: [Data files]
# Units/basis: [state explicitly — e.g., "yields on dry-ash-free basis, mass %"]
# Outputs: [Figures, tables, RDS files]
# ============================================================

# 0. Setup ----
library(tidyverse)

set.seed(20260415)  # YYYYMMDD per r-code-conventions.md (INV-9)
dir.create(here::here("scripts", "R", "_outputs"), recursive = TRUE, showWarnings = FALSE)

# 1. Load & Validate ----
# [Load data; check units/basis consistency, physical-bound constraints;
#  classify replicates as independent/biological vs. technical/analytical]

# 2. Descriptive Statistics & Outlier Assessment ----
# [Aggregate technical replicates to one value per independent unit FIRST;
#  per-condition mean/SD/CV on independent n only; flag (never auto-drop) outliers]

# 3. Exploratory Analysis ----
# [Distributions, relationships, group visualizations]

# 4. Statistical Testing / Modeling ----
# [Test choice follows design + independence + n + distribution/variance shape +
#  the scientific question jointly -- not a mechanical Shapiro-Wilk/Levene's gate;
#  paired/repeated-measures/mixed-effects tests if the design calls for them;
#  regression only if the question is a continuous predictor-response relationship;
#  nls() for kinetic/process fits; mass/energy balance closure check;
#  report effect sizes + uncertainty intervals alongside every p-value]

# 5. Sensitivity Analysis ----
# [OAT sweep or hand off to /simulation-study for Monte Carlo propagation — if applicable]

# 6. Tables and Figures ----
# [Publication-ready output, uncertainty shown throughout]

# 7. Export ----
# [saveRDS for every computed object, ggsave for every figure]
```

### Python (`scripts/python/`)

```python
"""
[Descriptive Title]
Purpose: [What this script does]
Inputs: [Data files]
Units/basis: [state explicitly]
Outputs: [Figures, tables, serialized objects]
"""

# 0. Setup
import numpy as np
import pandas as pd

np.random.seed(20260415)  # YYYYMMDD per python-code-conventions.md (INV-9)
OUT_DIR = ...  # pathlib.Path relative to repo root; mkdir(parents=True, exist_ok=True)

# 1. Load & Validate
# [Load data; check units/basis consistency, physical-bound constraints;
#  classify replicates as independent/biological vs. technical/analytical]

# 2. Descriptive Statistics & Outlier Assessment
# [Aggregate technical replicates to one value per independent unit FIRST;
#  per-condition mean/SD/CV on independent n only; flag (never auto-drop) outliers]

# 3. Exploratory Analysis
# [Distributions, relationships, group visualizations]

# 4. Statistical Testing / Modeling
# [Test choice follows design + independence + n + distribution/variance shape +
#  the scientific question jointly -- not a mechanical Shapiro-Wilk/Levene's gate;
#  paired/repeated-measures/mixed-effects tests if the design calls for them;
#  statsmodels regression only if the question is a continuous predictor-response relationship;
#  scipy.optimize.curve_fit for kinetic/process fits; mass/energy balance closure check;
#  report effect sizes + uncertainty intervals alongside every p-value]

# 5. Sensitivity Analysis
# [OAT sweep or hand off to /simulation-study for Monte Carlo propagation — if applicable]

# 6. Tables and Figures
# [Publication-ready output, uncertainty shown throughout]

# 7. Export
# [pickle/parquet for every computed object, savefig for every figure]
```

---

## Important

- **Reproduce, don't guess.** If the user specifies a particular test or model, run exactly that.
- **Validate before describing; describe before testing; test before modeling.** Don't skip ahead to a statistical test or model fit before Phases 1–3 are done.
- **Flag, don't delete.** Outliers and excluded points are reported, never silently dropped (see Phase 2).
- **No pseudoreplication.** Technical/analytical replicates are not independent observations — aggregate to one value per independent unit before they enter a test's *n* (see Phase 1–2).
- **No mechanical test selection.** A normality or variance test is one input among several (design, independence, sample size, distribution/variance shape, the scientific question) — never the sole gate on parametric vs. non-parametric choice (see Phase 4).
- **Report effect sizes and uncertainty, not just p-values.** Every test result includes an effect size and its uncertainty interval alongside the p-value, whenever appropriate (see Phase 4).
- **Use relative paths.** All paths relative to repository root (`here::here()` in R, `pathlib.Path` in Python).
- **No hardcoded values.** Use named variables for thresholds, unit-conversion factors, tolerance bands, etc.
- **State the basis for every quantity.** Ambiguous units/basis are a common source of silent errors in this domain — resolve them in Phase 0/1, not in a footnote.

## Long-running fits: use the Monitor tool

For kinetic fits, bootstrap loops, or Monte Carlo sensitivity runs that take more than a couple of minutes, launch via Bash with `run_in_background: true` and then use Anthropic's **Monitor tool** to stream stdout into the conversation in real time. Pattern:

1. Background-launch: `Rscript scripts/R/03_analyze.R` or `python scripts/python/03_analyze.py` with `run_in_background: true`. Capture the `bash_id`.
2. Use Monitor on the `bash_id` until a milestone fires (e.g., a "results written" message, or process exit).
3. Continue or course-correct based on what the stream reveals.

This avoids the polling-loop anti-pattern (`sleep 30; check; sleep 30; check`) and avoids burning cache on idle waits.
