# Archived: Economics & Political Science Paper-Type Taxonomy (`methods-referee` agent)

**Archived:** 2026-08-17, when the active `.claude/agents/methods-referee.md` was narrowed to a bioenergy-only paper-type taxonomy (`experimental` / `process-modeling` / `lca-tea` / `review`). This file preserves the original template's six-way economics/political-science taxonomy, dimension weights, and mandatory sanity checks verbatim, for reference or restoration.

Not loaded by any active agent.

---

## Paper-type identification (original)

- **Reduced-form** — DiD, IV, RD, event study, synthetic control, etc. The paper estimates a treatment effect without committing to a full structural model.
- **Structural** — structural estimation, DSGE, GE calibration, game-theoretic empirical model. Parameters of a fully-specified model are recovered.
- **Theory+empirics** — theoretical model with empirical test of its predictions. The model is the contribution; the empirics validate it.
- **Descriptive** — measurement, data construction, pattern documentation. No causal claim.
- **Formal-theory** — pure theory paper (game-theoretic model, mechanism design, formal political theory, etc.). The contribution *is* the model and its comparative statics; there is no empirical test in this paper.
- **Survey-experiment** — randomized survey experiments (vignette, conjoint, list experiment, factorial). Common in political science (AJPS, JOP) and experimental psychology.

## Dimension weights by paper type (original)

### Reduced-form
| # | Dimension | Weight |
|---|---|---|
| 1 | Identification | 35% |
| 2 | Estimation | 25% |
| 3 | Inference (SEs, clustering, MHT) | 20% |
| 4 | Robustness | 15% |
| 5 | Replication | 5% |

### Structural
| # | Dimension | Weight |
|---|---|---|
| 1 | Model specification | 20% |
| 2 | Parameter identification | 30% |
| 3 | Estimation | 20% |
| 4 | Fit / validation | 15% |
| 5 | Counterfactuals | 15% |

### Theory + empirics
| # | Dimension | Weight |
|---|---|---|
| 1 | Model | 20% |
| 2 | Prediction sharpness | 25% |
| 3 | Test design | 25% |
| 4 | Honesty (report non-confirming results too) | 15% |
| 5 | Execution | 15% |

### Descriptive
| # | Dimension | Weight |
|---|---|---|
| 1 | Construct validity | 30% |
| 2 | Construction (data cleaning, coding) | 25% |
| 3 | Validation (external checks, benchmarking) | 25% |
| 4 | Analysis | 15% |
| 5 | Replication | 5% |

### Formal-theory
| # | Dimension | Weight |
|---|---|---|
| 1 | Model originality / interest | 30% |
| 2 | Comparative-static sharpness | 25% |
| 3 | Proof rigour | 20% |
| 4 | Robustness to alternative assumptions | 15% |
| 5 | Applicability / interpretability | 10% |

### Survey-experiment
| # | Dimension | Weight |
|---|---|---|
| 1 | Design (treatment construction, control adequacy) | 25% |
| 2 | Sample (recruitment, eligibility, representativeness) | 25% |
| 3 | Measurement (DV validity, manipulation checks) | 20% |
| 4 | Attrition + balance | 20% |
| 5 | Replication / preregistration adherence | 10% |

## Mandatory pre-scoring sanity checks (original)

### Reduced-form
- **Sign check.** Does the headline coefficient have the expected sign under the author's theory?
- **Magnitude check.** Is the coefficient in a reasonable range (not 0.0001, not 10×)?
- **Dynamics check.** If DiD/event study: do pre-trends look flat? If IV: is the first-stage F-stat > 10?
- **Clustering check.** Are standard errors clustered at the correct level (treatment unit)?
- **Sample check.** Is the analysis sample constructed and reported clearly?

### Structural
- **Parameter plausibility.** Are estimated parameters in ranges consistent with prior literature?
- **Fit.** Does the model fit moments it was not calibrated to?
- **Counterfactual within support.** Are policy counterfactuals inside the data's covariate support?
- **Identification argument.** Is it stated formally?

### Theory + empirics
- **Prediction sharpness.** Does the theory predict a specific magnitude/sign, or just "some effect"?
- **Test power.** Is the empirical test well-powered to reject the null predicted by the theory?
- **Honest reporting.** Are non-confirming predictions reported?

### Descriptive
- **Construct validity.** Does the measure capture what it claims to capture?
- **Construction transparency.** Is the data-cleaning / coding pipeline reproducible?
- **Validation.** Does the measure correlate with related measures in the expected way?

### Formal-theory
- **Equilibrium existence.** Is existence proven (or rigorously argued), not assumed?
- **Comparative-static direction.** Are the signs of comparative statics derived and stated explicitly?
- **Assumption tractability.** Are the assumptions reasonable, or are they doing the heavy lifting?
- **Robustness to assumption relaxation.** Does the headline result survive at least one substantive relaxation?
- **Notation discipline.** Is notation defined before use?

### Survey-experiment
- **Balance check.** Are pre-treatment covariates balanced across arms?
- **Manipulation-check pass rate.** Did respondents notice the treatment?
- **Attrition asymmetry.** Is attrition rate similar across arms?
- **Sampling-frame validity.** Is the platform (MTurk/Lucid/Prolific) appropriate for the claimed population?
- **Preregistration adherence.** Are the analyses in the paper the ones pre-registered?
