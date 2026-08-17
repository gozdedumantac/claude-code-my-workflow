---
paths:
  - "scripts/python/**/*.py"
  - "explorations/**/*.py"
---

# Python Code Standards

**Standard:** Senior Principal Data Engineer + PhD researcher quality

> **Scope:** These standards apply to **analysis scripts** — data work, process/kinetic-model fits, figure generation (a top-level seed, imports at the top, relative output paths). Mirrors [`r-code-conventions.md`](r-code-conventions.md); use whichever language a given script/collaborator needs. The numerical discipline in §8 applies to both languages.

---

## 1. Reproducibility

- `np.random.seed()` (and `random.seed()` if stdlib `random` is used) called ONCE at top, YYYYMMDD format
- All imports at the top of the file — no `import` inside functions except to avoid a genuine circular-import problem
- All paths relative to the repository root, resolved via `pathlib.Path` — never a hardcoded absolute path
- `Path(...).mkdir(parents=True, exist_ok=True)` for output directories

## 2. Function Design

- `snake_case` naming, verb-noun pattern
- Docstrings on every non-trivial function (Google or NumPy style)
- Default parameters, no magic numbers
- Return values are named (a `dataclass`, `TypedDict`, or explicit dict) — not bare tuples for anything beyond 2 elements

## 3. Domain Correctness

<!-- Customize for your field's known pitfalls -->
- Verify statistical/model implementations match the method described in the manuscript or slides
- Check known library gotchas (document below in Common Pitfalls) — e.g., `scipy.optimize.curve_fit` silently returning a local optimum without bounds/initial guesses; `pandas` silently upcasting int columns with NaNs to float

## 4. Visual Identity

```python
# --- Your institutional palette ---
PRIMARY_BLUE = "#012169"
PRIMARY_GOLD = "#B9975B"
ACCENT_GRAY = "#525252"
POSITIVE_GREEN = "#15803D"
NEGATIVE_RED = "#B91C1C"
```

### Custom theme

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 14,
    "axes.labelcolor": "#1A1A1A",
    "figure.facecolor": "none",
    "axes.facecolor": "none",
    "savefig.transparent": True,
})
```

### Figure dimensions for Beamer

```python
fig.savefig(filepath, bbox_inches="tight")  # figsize set at subplots() time, e.g. figsize=(12, 5)
```

## 5. Serialized-Object Pattern

**Heavy computations saved as pickled objects (or `.npz`/`.parquet` where more appropriate); slide/report rendering loads pre-computed data.**

```python
import pickle
with open(out_dir / "descriptive_name.pkl", "wb") as f:
    pickle.dump(result, f)
```

Prefer `.parquet` over `.pkl` for tabular DataFrames that need to be read from R or other tools; prefer `.npz` for large numeric arrays.

## 6. Common Pitfalls

<!-- Add your field-specific pitfalls here -->
| Pitfall | Impact | Prevention |
|---------|--------|------------|
| `savefig.transparent` not set | White boxes on slides | Set in `rcParams` or pass `transparent=True` to every `savefig()` |
| Hardcoded paths | Breaks on other machines | Use `pathlib.Path` relative to repo root |
| Mutable default argument (`def f(x, y=[])`) | Silent state leakage across calls | Default to `None`, initialize inside the function |

## 7. Line Length & Mathematical Exceptions

**Standard:** Keep lines <= 100 characters (PEP 8 default is 79; this project's exception widens it to match the R convention).

**Exception: Mathematical Formulas** -- lines may exceed 100 chars **if and only if:**

1. Breaking the line would harm readability of the math (kinetic-rate expressions, matrix operations, finite-difference approximations, formula implementations matching manuscript equations)
2. An inline comment explains the mathematical operation:
   ```python
   # Arrhenius rate constant: k = A * exp(-Ea / (R * T))
   k = A * np.exp(-Ea / (R_GAS * T))
   ```
3. The line is in a numerically intensive section (fitting routines, Monte Carlo loops, uncertainty propagation)

**Quality Gate Impact:**
- Long lines in non-mathematical code: minor penalty (-1 to -2 per line)
- Long lines in documented mathematical sections: no penalty

## 8. Numerical Discipline

See [`python-reviewer.md`](../agents/python-reviewer.md) for the full checklist. Headline rules (mirror `r-code-conventions.md` §8):

- **No float equality.** Never use `==` on floats. Use `math.isclose()` / `np.isclose()` or `abs(a - b) < tol`.
- **CDF clamping** to an OPEN interval. Exact 0 or 1 passed to `scipy.stats.norm.ppf()` etc. produces `±inf`. Project-wide epsilon:

  ```python
  eps = 1e-12
  p = np.clip(p, eps, 1 - eps)   # now safe for norm.ppf(p)
  ```

- **Explicit dtypes for counts.** Use `np.int64` / Python `int` for counts, never let an integer column silently upcast to `float64` because of NaNs — handle missingness explicitly first.
- **Pre-allocate arrays** before loops (`np.empty(n)`, `np.zeros(n)`), never grow with `list.append()` inside a hot numerical loop (list-of-scalars-then-`np.array()` at the end is fine; repeated `np.concatenate` in a loop is not).
- **Deterministic bootstrap/replication seeding.** Set the seed before the loop; for parallel replications (`multiprocessing`, `joblib`), pass an explicit per-worker seed (e.g., `seed_base + worker_id`) — never rely on process-inherited global RNG state.
- **Explicit `skipna` / `dropna` behavior.** Never rely on `pandas` defaults for `.mean()`, `.sum()`, `.std()` on data with potential NaNs — decide and state the behavior.

## 9. Code Quality Checklist

```
[ ] Imports at top, no import-inside-function (except to break a real cycle)
[ ] Seed set once at top (YYYYMMDD)
[ ] All paths relative via pathlib
[ ] Functions documented (docstrings)
[ ] Figures: transparent bg, explicit figsize
[ ] Every computed object saved (pickle/parquet/npz)
[ ] Comments explain WHY not WHAT
[ ] Numerical discipline: no float ==, CDF clamping with eps, pre-allocated arrays
```
