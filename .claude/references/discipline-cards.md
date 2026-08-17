# Discipline Cards

Short reference cards naming each discipline's dominant paper-type frequencies, top journals, reporting/preregistration norms, and method conventions. Read by `/research-ideation`, `/interview-me`, `/preregister`, and the `editor` agent (in `/review-paper --peer`) when the user gives a `paper_type` or domain hint without specifying a target journal.

**Scope.** This fork ships one active card: **Bioenergy & Circular Biorefinery** — the primary and only discipline this workflow is calibrated to. The original template's economics and political-science cards are preserved for reference in [`_archive/economics-tools/references/discipline-cards-econ-polisci.md`](../../_archive/economics-tools/references/discipline-cards-econ-polisci.md); they are not loaded by any active skill or agent. To add another discipline, copy a card section, fill the four fields (paper-type frequencies, journals, reporting/preregistration norms, method conventions), and reference the new short-name from `journal-profiles.md` and `methods-referee.md`.

**Maintenance.** When you add a journal profile to `journal-profiles.md`, cross-reference it here. When you add a paper type to `methods-referee.md`, cross-reference it here.

---

## Bioenergy & Circular Biorefinery (`bioenergy`)

Covers thermochemical conversion (pyrolysis, gasification), hydrothermal conversion (liquefaction/carbonization), biochar production and characterization, hydrogen production (thermochemical and biological/microbial), microbial/biochemical conversion, waste valorization, and the life-cycle and techno-economic assessment (LCA/TEA) of these pathways.

**Paper-type frequencies (rough share of work in the journal set below).**

| Type | Share | Notes |
|---|---|---|
| Experimental (lab/pilot-scale) | ~45% | Conversion-condition studies (temperature, residence time, catalyst, feedstock), product characterization, yield/composition reporting. The dominant mode. |
| Process modeling | ~20% | Kinetic models (Arrhenius, decomposition rate laws), reactor/process simulation, parameter estimation and validation against experimental data. |
| LCA / TEA | ~20% | Life-cycle assessment (ISO 14040/14044) and techno-economic assessment of a conversion pathway or biorefinery configuration; frequently paired with an experimental or modeling study rather than standalone. |
| Review / meta-analysis | ~10% | Synthesis across feedstocks, technologies, or a specific conversion pathway's state of the art. |
| Pilot/demonstration-scale process reporting | ~5% | Scale-up performance data, often with a TEA component. |

**Dominant journals (shipped in `journal-profiles.md`).** Bioresource Technology, Applied Energy, Biomass and Bioenergy, GCB Bioenergy, International Journal of Hydrogen Energy, Journal of Cleaner Production, Fuel, Energy Conversion and Management, Biomass Conversion and Biorefinery, Waste Management, ACS Sustainable Chemistry & Engineering, Chemical Engineering Journal, Sustainable Production and Consumption, Energy, Renewable Energy, Resources Conservation & Recycling, Bioenergy Research.

**Reporting / preregistration norms.**
- **Preregistration is not a field norm** for experimental or process-modeling work — unlike RCT-heavy fields, there is no equivalent registry expectation. Do not force a preregistration recommendation on this discipline by default; if a study genuinely has a confirmatory hypothesis-testing design (rare in this field), OSF is the fallback registry.
- **Reporting rigor substitutes for preregistration** as the field's trust mechanism: mass/energy balance closure reported with a stated tolerance; replicate count and type (independent vs. technical) stated explicitly; characterization method stated and matched to the claim it supports; for LCA, the functional unit, system boundary, and allocation method stated per ISO 14040/14044; for TEA, cost basis, cost year, and discount rate stated.
- **Data/code availability** is increasingly expected (Elsevier/Springer/ACS journals in this set commonly request a data-availability statement) but is not yet a uniform hard gate the way AEA's DCAS is for economics.

**Method conventions.**
- **Units and basis** must be stated explicitly and consistently: dry vs. as-received basis, mass % vs. energy % yield, HHV vs. LHV. Ambiguous basis is the field's most common silent-error class.
- **Replicates:** independent/biological replicates (separate runs/batches) must be distinguished from technical/analytical replicates (repeated measurements on one sample); technical replicates are not independent *n* for statistical purposes.
- **Statistical treatment:** ANOVA + post-hoc (Tukey/Dunn's) for multi-condition comparisons is standard; regression is used when the question is a genuine continuous predictor–response relationship, not as a default tool.
- **Kinetic/process modeling:** parameter estimates reported with uncertainty (confidence intervals), not point estimates alone; model validated against data not used in fitting where possible.
- **LCA:** ISO 14040/14044 compliance expected at top venues; system boundary diagram and functional unit stated explicitly; allocation method (mass, energy, economic) justified when co-products exist.
- **TEA:** cost basis, cost year, and discount rate stated; sensitivity analysis on key cost/price parameters expected.
- **Code:** R and Python both common; process simulation frequently done in Aspen Plus (results reported, not necessarily with released input files); LCA in openLCA/SimaPro; instrumental data processing sometimes in OriginPro.

**Cross-references.** `methods-referee.md` paper types: `experimental`, `process-modeling`, `lca-tea`, `review`. `journal-profiles.md`: the 17-journal set above.

---

## How skills consume these cards

- **`/research-ideation`** — when the user names a topic without a discipline, the skill may infer one from context (citation style, vocabulary). The card supplies the default `paper_type` distribution to bias hypothesis generation.
- **`/interview-me`** — Phase 1 paper-type question uses the card's frequency table to order the option list (most-likely-first per discipline).
- **`/preregister`** — for this discipline, defaults to noting preregistration is not a field norm (per "Reporting / preregistration norms" above) rather than defaulting to a registry style.
- **`editor`** (`/review-paper --peer`) — when the user gives `--peer` without naming a specific journal but with a discipline hint, the editor uses the card's "Dominant journals" list as the candidate set and asks for clarification.

---

## Adding a new discipline card

Copy this template:

```markdown
## [Discipline name] (`short-slug`)

**Paper-type frequencies.**
| Type | Share | Notes |
|---|---|---|
| ... |

**Dominant journals (shipped in `journal-profiles.md`).** [list]. [Optional: subfield outlets.]

**Reporting / preregistration norms.**
- [registry conventions per study type, or a note that they don't apply]

**Method conventions.**
- [significance stars / SE conventions / replication norms / dominant code language]
```

Then:

1. Add the card section above (alphabetically by short-slug).
2. Add concrete journal profiles to `journal-profiles.md` for at least the top-3 journals.
3. Add paper types to `methods-referee.md` if your field uses categories not already there.
4. Cross-reference the new short-slug from `/research-ideation` and `/interview-me` if those skills should respect the new defaults.

---

## Where this file lives

- **File:** `.claude/references/discipline-cards.md`
- **Schema parallel:** `.claude/references/journal-profiles.md` (per-journal) and `.claude/references/audit-pet-peeves.md` (living-catalogue format).
- **Consumed by:** `/research-ideation`, `/interview-me`, `/preregister`, `editor` agent.
- **Archived siblings:** the economics and political-science cards from the original template live in [`_archive/economics-tools/references/discipline-cards-econ-polisci.md`](../../_archive/economics-tools/references/discipline-cards-econ-polisci.md), preserved for restoration but not active.
