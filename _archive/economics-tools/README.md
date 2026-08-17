# Archived: Economics-Specific Tooling

**Archived:** 2026-08-17, when this fork was repurposed from its origin project (Econ 730: Causal Panel Data, Emory University) into the **Bioenergy and Circular Biorefinery Academic Research Workflow**.

## What's here

- `skills/did-event-study/` — the `/did-event-study` skill: staggered difference-in-differences / event-study estimation via `did` (Callaway–Sant'Anna), `fixest::sunab` (Sun–Abraham), HonestDiD sensitivity, and Stata equivalents (`csdid`, `drdid`).
- `skills/stata-replication/` — the `/stata-replication` skill: Stata `.do`-file replication-package conventions.
- `rules/did-conventions.md` — the DiD/event-study coding standard (LONG data + `gname` coding, doubly-robust default, control-group rule, uniform-band inference, mandatory pre-trend/HonestDiD/didFF diagnostics).
- `rules/stata-code-conventions.md` — Stata `.do`-file coding conventions.
- `tikz-snippets/` — three econometrics-specific diagram templates (`did-two-period.tex`, `event-study.tex`, `supply-demand.tex`) moved out of `templates/tikz-snippets/` for the same reason.
- `references/discipline-cards-econ-polisci.md` — the original Economics and Political Science discipline cards, moved out of `.claude/references/discipline-cards.md` when that file was narrowed to a single active bioenergy discipline.
- `references/journal-profiles-econ-polisci.md` — the original 5 econ-journal + 3 political-science-journal peer-review calibration profiles, moved out of `.claude/references/journal-profiles.md`.
- `agents/methods-referee-econ-polisci.md` — the original economics/political-science paper-type taxonomy (reduced-form / structural / theory+empirics / descriptive / formal-theory / survey-experiment), dimension weights, and sanity checks, moved out of `.claude/agents/methods-referee.md`, which now carries a bioenergy-only taxonomy (`experimental` / `process-modeling` / `lca-tea` / `review`).
- `agents/editor-econ-peeves.md` — the original economics/political-science-flavored critical and constructive pet-peeve pools, moved out of `.claude/agents/editor.md`, which now carries bioenergy-retargeted pools.
- `agents/domain-reviewer-econ.md` — the original un-customized `domain-reviewer.md` template (generic econometrics-flavored illustrative examples), preserved before this fork customized the active agent for bioenergy substance review.

## Why archived, not deleted

Bioenergy/biomass-conversion research is predominantly experimental, process-modeling, and LCA/TEA work — not causal-panel econometrics, and the current workflow does not use Stata. These tools don't apply to that work, but they're preserved (not deleted) in case a future project on this fork needs causal-inference or Stata tooling again.

## How to restore

The moves were done with `git mv`, so file history is intact. To bring a tool back into active use:

```bash
git mv _archive/economics-tools/skills/did-event-study .claude/skills/did-event-study
git mv _archive/economics-tools/rules/did-conventions.md .claude/rules/did-conventions.md
```

Then re-add the corresponding rows to `README.md`'s skill/rule tables and `CLAUDE.md`'s Skills Quick Reference (removed as part of the 2026-08-17 archive pass — see `git log` on those files around that date for the exact diff to reverse).

## What was NOT archived

`/simulation-study` keeps its Monte Carlo machinery (DGP/estimator-grid/bias/RMSE/coverage/MCSE) — that framework is domain-agnostic and directly reusable for bioenergy uncertainty quantification (e.g., TEA/LCA Monte Carlo, kinetic-parameter recovery). Only its illustrative example (TWFE vs. Callaway–Sant'Anna) was retargeted, not the skill itself.
