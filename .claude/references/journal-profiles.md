<!-- Pipeline shape (journal-calibration schema, referee-pool weights, disposition
     taxonomy) adapted from Hugo Sant'Anna's clo-author (github.com/hugosantanna/clo-author),
     used with permission. The original economics/political-science journal profiles
     this file shipped with are archived at
     _archive/economics-tools/references/journal-profiles-econ-polisci.md — this
     file's journal set has been replaced with a bioenergy/circular-biorefinery
     set; the underlying calibration schema and pipeline mechanics are unchanged. -->

# Journal Profiles

Calibration data for the `/review-paper --peer [journal]` simulated peer-review pipeline. Each profile tells the editor how to select referees (disposition-pool weights), what concerns that journal typically emphasizes, and any journal-specific formatting conventions.

**How this file is used.** The `editor` agent reads this file before each `--peer` run, picks the requested `[journal]`, and uses its Referee-pool weights + Typical concerns to select two referees with different dispositions and to seed their pet-peeve priors.

**This fork's active set.** This file ships **17 bioenergy/circular-biorefinery journals** — this fork's primary and only active discipline. The original template's five top-5 econ journals and three political-science journals are preserved at [`_archive/economics-tools/references/journal-profiles-econ-polisci.md`](../../_archive/economics-tools/references/journal-profiles-econ-polisci.md) for reference or restoration; they are not loaded by any active skill or agent. To add a journal in a different field, copy `templates/journal-profile-template.md` into a new section below and follow [Field adaptation](#field-adaptation) at the bottom.

---

## Schema

Every profile has these fields:

- **Short name** — the string you pass to `--peer [name]` (e.g., `BRT`, `ACS-SCE`).
- **Focus** — what the journal publishes; what it doesn't.
- **Bar** — what it takes to clear the desk; typical acceptance rate context.
- **Domain-referee adjustments** — how the substance referee should re-weight their dimensions for this journal (defaults: Contribution & Novelty 30 / Literature Positioning 25 / Substantive Arguments 20 / External Validity 15 / Fit 10 — see `domain-referee.md`).
- **Methods-referee adjustments** — how the methods referee should re-weight for this journal, per paper type (`experimental` / `process-modeling` / `lca-tea` / `review` — see `methods-referee.md`).
- **Typical concerns** — 3–5 direct-quote questions a referee at this journal will ask.
- **Referee-pool weights** — probability weights over the 6 dispositions (STRUCTURAL / CREDIBILITY / MEASUREMENT / POLICY / THEORY / SKEPTIC). Editor draws two *different* dispositions from this distribution.
- **Table format override** (optional) — any journal-specific formatting rule.

---

## Bioenergy & Circular Biorefinery

### Bioresource Technology (BRT)

**Short name:** `BRT`

**Focus.** High-volume bioprocessing and bioresource-conversion journal — thermochemical and biochemical conversion technologies, biofuels, enzyme/microbial processes, waste-to-value. Application- and performance-focused; less tolerant of purely theoretical work with no experimental performance data.

**Bar.** Solid experimental rigor with clear yield/performance metrics benchmarked against the literature. High throughput, fast turnaround — desk-rejects narrow incremental optimization studies that don't add a mechanistic or performance insight.

**Domain-referee adjustments.**
- Contribution 30 → 25 (incremental performance gains are publishable if rigorously shown; the bar on conceptual novelty is moderate)
- Fit 10 → 15 (must be squarely bioprocessing/conversion technology — LCA-only or pure-economics papers are a weaker fit)

**Methods-referee adjustments.**
- If paper type is `experimental`: Statistical treatment 25 → 30, Reproducibility 20 → 25 (replicate rigor is heavily scrutinized)

**Typical concerns.**
- "Are the yields/performance metrics benchmarked against comparable literature conditions?"
- "Are independent replicates reported, and is the statistical treatment appropriate?"
- "Is the characterization method (GC, HPLC, elemental analysis) appropriate for the claim?"
- "Is the mass balance closed and reported?"

**Referee-pool weights.**
- MEASUREMENT: 0.30
- CREDIBILITY: 0.20
- STRUCTURAL: 0.15
- POLICY: 0.10
- THEORY: 0.10
- SKEPTIC: 0.15

**Table format override.** None specific; units and basis must be stated in every table header.

---

### Applied Energy

**Short name:** `AppEnergy`

**Focus.** Broad energy-systems journal — technology performance, techno-economic and environmental impact quantification, system-level integration. Values work that connects conversion technology to system- or policy-relevant implications, not bench-scale results alone.

**Bar.** Must demonstrate relevance beyond the bench — system-level energy/exergy accounting, techno-economic framing, or clear pathway-to-deployment argument. Narrow lab-only papers without broader implications face an uphill fit argument.

**Domain-referee adjustments.**
- Contribution 30 → 30 (unchanged)
- External validity 15 → 20 (system-level generalizability matters more here)
- Fit 10 → 15 (must connect to energy-systems relevance)

**Methods-referee adjustments.**
- If paper type is `lca-tea`: System boundary & functional unit 25 → 30
- If paper type is `experimental`: expect an explicit discussion of scale-up/system implications even for bench-scale work

**Typical concerns.**
- "What is the system-level or deployment-relevant implication of this bench-scale/model result?"
- "Is the techno-economic or energy-efficiency framing quantitatively grounded, not just asserted?"
- "How does this compare to competing conversion pathways on a consistent basis?"
- "Is the sensitivity of the headline result to key cost/efficiency assumptions shown?"

**Referee-pool weights.**
- POLICY: 0.25
- STRUCTURAL: 0.20
- MEASUREMENT: 0.20
- CREDIBILITY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.10

**Table format override.** None specific.

---

### Biomass and Bioenergy

**Short name:** `B&B`

**Focus.** Feedstock-to-energy full chain — biomass production, characterization, supply-chain logistics, and conversion. Values feedstock characterization rigor and a life-cycle-aware framing of the conversion pathway.

**Bar.** Solid, well-characterized feedstock data plus a clearly motivated conversion or supply-chain question. Less tolerant of conversion-only papers with sparse feedstock characterization.

**Domain-referee adjustments.**
- Contribution 30 → 25
- Lit positioning 25 → 30 (expects careful positioning against the feedstock/agronomy literature, not just conversion literature)

**Methods-referee adjustments.**
- If paper type is `experimental`: Characterization-method fit 20 → 25 (feedstock characterization completeness is a desk-level concern)

**Typical concerns.**
- "Is the feedstock fully characterized (proximate/ultimate analysis, moisture, ash)?"
- "Is the basis (dry vs. as-received) consistent throughout?"
- "Does the paper consider supply-chain or feedstock-variability implications?"
- "Are yields reported on a consistent, stated basis?"

**Referee-pool weights.**
- MEASUREMENT: 0.30
- STRUCTURAL: 0.15
- CREDIBILITY: 0.15
- POLICY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.15

**Table format override.** None specific.

---

### GCB Bioenergy

**Short name:** `GCBB`

**Focus.** Bioenergy through a global-change/environmental-sustainability lens — GHG accounting, land-use implications, ecological sustainability of feedstock production and conversion. LCA/GHG framing is close to mandatory, not optional.

**Bar.** High bar on environmental/climate rigor — GHG accounting must be methodologically sound (system boundary, counterfactual land-use baseline) even for a conversion-technology paper. Purely process-performance papers without an environmental framing are a weak fit.

**Domain-referee adjustments.**
- Contribution 30 → 25
- External validity 15 → 25 (climate/environmental generalizability is central)
- Fit 10 → 15

**Methods-referee adjustments.**
- If paper type is `lca-tea`: Methodological transparency 25 → 30 (GHG accounting scrutiny is the house specialty)

**Typical concerns.**
- "Is the GHG accounting methodologically sound, including the land-use-change counterfactual?"
- "Is the environmental claim supported by a full life-cycle accounting, or just a partial one?"
- "Does the paper address ecological/sustainability trade-offs, not just carbon?"
- "Is uncertainty in emission factors propagated to the headline result?"

**Referee-pool weights.**
- MEASUREMENT: 0.25
- POLICY: 0.25
- CREDIBILITY: 0.15
- STRUCTURAL: 0.15
- THEORY: 0.10
- SKEPTIC: 0.10

**Table format override.** GHG results should be reported per stated functional unit with the counterfactual baseline explicit.

---

### International Journal of Hydrogen Energy (IJHE)

**Short name:** `IJHE`

**Focus.** Hydrogen-specific across production (thermochemical, electrolytic, biological/microbial), storage, and utilization, plus techno-economics. Technical rigor on yield/purity/efficiency is central.

**Bar.** Clear, quantified hydrogen yield/purity/energy-efficiency data benchmarked against the production route's state of the art. Novelty can be incremental if the characterization is rigorous.

**Domain-referee adjustments.**
- Contribution 30 → 25
- Fit 10 → 15 (must be squarely hydrogen-relevant)

**Methods-referee adjustments.**
- If paper type is `experimental`: Statistical treatment 25 → 25 (unchanged), Characterization-method fit 20 → 25 (gas-composition/purity measurement rigor is scrutinized)
- If paper type is `process-modeling`: Validation against independent experimental data 25 → 30

**Typical concerns.**
- "Is hydrogen yield/purity reported with the measurement method stated (GC, mass spec)?"
- "How does the energy efficiency compare to competing hydrogen-production routes on a consistent basis?"
- "Is the mass/energy balance for the reactor system closed?"
- "Is the techno-economic viability at least qualitatively addressed?"

**Referee-pool weights.**
- MEASUREMENT: 0.30
- STRUCTURAL: 0.20
- CREDIBILITY: 0.15
- POLICY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.10

**Table format override.** None specific.

---

### Journal of Cleaner Production (JCLP)

**Short name:** `JCLP`

**Focus.** Broad sustainability and circular-economy journal — LCA-heavy, systemic/policy-relevant framing. Not bioenergy-exclusive; a bioenergy submission must connect to cleaner-production or circular-economy relevance explicitly.

**Bar.** Methodological transparency in LCA/sustainability assessment is close to mandatory; a purely technical conversion-performance paper without a sustainability assessment component is a weak fit.

**Domain-referee adjustments.**
- Contribution 30 → 25
- External validity 15 → 20
- Fit 10 → 20 (fit to the cleaner-production/circular-economy scope is a real constraint, not a formality)

**Methods-referee adjustments.**
- If paper type is `lca-tea`: System boundary & functional unit 25 → 30, Methodological transparency 25 → 30

**Typical concerns.**
- "Does this paper's contribution connect clearly to cleaner production or circular economy, or is it a conversion-technology paper without that framing?"
- "Is the LCA methodology ISO 14040/14044 compliant and fully transparent?"
- "Are the sustainability trade-offs (not just benefits) discussed honestly?"
- "Is the functional unit and system boundary appropriate for the comparison being made?"

**Referee-pool weights.**
- POLICY: 0.25
- MEASUREMENT: 0.20
- CREDIBILITY: 0.15
- STRUCTURAL: 0.15
- SKEPTIC: 0.15
- THEORY: 0.10

**Table format override.** None specific.

---

### Fuel

**Short name:** `Fuel`

**Focus.** Fundamental fuel science — combustion, fuel characterization, kinetics of thermochemical conversion. Deep chemistry/engineering rigor on fundamentals; less LCA/systems-framing than the journals above.

**Bar.** Rigorous fundamental characterization (proximate/ultimate analysis, calorific value, combustion/kinetic behavior) is expected regardless of application framing. Values mechanistic insight into fuel chemistry.

**Domain-referee adjustments.**
- Contribution 30 → 30 (unchanged)
- Substantive arguments 20 → 25 (mechanistic rigor is the house taste)

**Methods-referee adjustments.**
- If paper type is `process-modeling`: Model structure 20 → 25 (kinetic-model rigor is heavily scrutinized)
- If paper type is `experimental`: Characterization-method fit 20 → 25

**Typical concerns.**
- "Is the kinetic model mechanistically justified, or just curve-fit?"
- "Is the fuel fully characterized (proximate/ultimate analysis, HHV/LHV, ash composition)?"
- "Are the reported kinetic parameters (activation energy, pre-exponential factor) consistent with the literature range for this feedstock class?"
- "Is the combustion/decomposition behavior mechanistically interpreted, not just tabulated?"

**Referee-pool weights.**
- STRUCTURAL: 0.25
- MEASUREMENT: 0.25
- THEORY: 0.15
- CREDIBILITY: 0.15
- SKEPTIC: 0.10
- POLICY: 0.10

**Table format override.** Kinetic parameters reported with units and the fitting method stated.

---

### Energy Conversion and Management (ECM)

**Short name:** `ECM`

**Focus.** Energy conversion technologies with a strong process modeling/optimization and techno-economic emphasis. Values quantitative process design and optimization over descriptive characterization alone.

**Bar.** A process-design, optimization, or techno-economic contribution is expected — purely descriptive experimental characterization without a process-engineering angle is a weaker fit.

**Domain-referee adjustments.**
- Substantive arguments 20 → 25 (process-engineering rigor is the house taste)
- Fit 10 → 15

**Methods-referee adjustments.**
- If paper type is `process-modeling`: Model structure 20 → 25, Sensitivity analysis 20 → 25
- If paper type is `lca-tea`: Uncertainty & sensitivity analysis 20 → 25

**Typical concerns.**
- "Is this a process-design or optimization contribution, or purely descriptive characterization?"
- "Is the techno-economic analysis's cost basis and discount rate transparent?"
- "Is the process model validated, and is a sensitivity analysis included?"
- "How does the conversion efficiency compare to the state of the art?"

**Referee-pool weights.**
- STRUCTURAL: 0.25
- MEASUREMENT: 0.20
- POLICY: 0.15
- CREDIBILITY: 0.15
- THEORY: 0.15
- SKEPTIC: 0.10

**Table format override.** None specific.

---

### Biomass Conversion and Biorefinery (BCAB)

**Short name:** `BCAB`

**Focus.** Biorefinery-concept journal integrating thermochemical and biochemical conversion with valorization pathways. Application-focused, mid-tier rigor bar, receptive to multi-product biorefinery framing.

**Bar.** A clear conversion or valorization result with reasonable characterization; less demanding on novelty than BRT or Fuel, but expects a biorefinery-relevant framing (multi-product, integration, or circularity angle).

**Domain-referee adjustments.**
- Contribution 30 → 20 (lower novelty bar than the top-tier journals in this set)
- Fit 10 → 20 (biorefinery/integration framing is a real constraint)

**Methods-referee adjustments.**
- If paper type is `experimental`: unchanged from base weights

**Typical concerns.**
- "Does this connect to a biorefinery or multi-product valorization framing, or is it a single-pathway conversion study?"
- "Are yields and product quality reported with the basis stated?"
- "Is the work positioned against the broader biorefinery-integration literature?"

**Referee-pool weights.**
- MEASUREMENT: 0.25
- STRUCTURAL: 0.20
- POLICY: 0.15
- CREDIBILITY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.15

**Table format override.** None specific.

---

### Waste Management

**Short name:** `WasteMgmt`

**Focus.** Waste valorization and management — waste-to-energy pathways, environmental impact of waste treatment, policy-relevant waste-stream framing. LCA of waste-management alternatives is common.

**Bar.** Must connect clearly to a waste-stream or waste-management framing; a conversion-technology paper using biomass unrelated to waste streams is a weaker fit unless reframed.

**Domain-referee adjustments.**
- Fit 10 → 20 (waste-stream relevance is a real constraint)
- External validity 15 → 20 (generalizability across waste-stream compositions matters)

**Methods-referee adjustments.**
- If paper type is `lca-tea`: comparison against a conventional waste-management baseline (landfill, incineration) expected in System boundary & functional unit

**Typical concerns.**
- "Is this framed around a genuine waste stream, and is the comparison against the conventional waste-management baseline shown?"
- "Does the waste-stream heterogeneity/composition variability get addressed?"
- "Is the environmental/economic comparison against landfill or incineration explicit?"

**Referee-pool weights.**
- POLICY: 0.25
- MEASUREMENT: 0.20
- CREDIBILITY: 0.15
- STRUCTURAL: 0.15
- SKEPTIC: 0.15
- THEORY: 0.10

**Table format override.** None specific.

---

### ACS Sustainable Chemistry & Engineering (ACS SCE)

**Short name:** `ACS-SCE`

**Focus.** ACS's flagship sustainability-chemistry journal — green chemistry principles, catalysis, novel synthesis with explicit sustainability framing. Strong chemistry-fundamentals bar combined with life-cycle-aware thinking.

**Bar.** High chemistry rigor (mechanism, selectivity, catalyst characterization) plus an explicit sustainability argument (green chemistry principles, atom economy, life-cycle awareness) — a technically sound but sustainability-blind paper is a weak fit.

**Domain-referee adjustments.**
- Contribution 30 → 30 (unchanged)
- Substantive arguments 20 → 25 (chemistry rigor is the house taste)
- Fit 10 → 15 (sustainability framing must be explicit, not incidental)

**Methods-referee adjustments.**
- If paper type is `experimental`: Characterization-method fit 20 → 25 (catalyst/product characterization rigor scrutinized)

**Typical concerns.**
- "Is the sustainability argument explicit (green chemistry metrics, atom economy, life-cycle awareness), or just asserted in the title?"
- "Is the catalyst/product fully characterized with appropriate spectroscopic/analytical methods?"
- "Is the mechanism proposed and supported by evidence, not just inferred from the product distribution?"
- "How does this compare to existing green-chemistry approaches to the same transformation?"

**Referee-pool weights.**
- STRUCTURAL: 0.25
- MEASUREMENT: 0.25
- THEORY: 0.15
- CREDIBILITY: 0.15
- POLICY: 0.10
- SKEPTIC: 0.10

**Table format override.** ACS style guide for spectroscopic data reporting.

---

### Chemical Engineering Journal (CEJ)

**Short name:** `CEJ`

**Focus.** Broad chemical engineering — reactor design, process intensification, catalysis, separations. Not bioenergy-specific but frequently publishes pyrolysis/gasification/catalytic-upgrading work. High mechanistic/engineering rigor bar.

**Bar.** A genuine chemical-engineering contribution (reactor design, mechanism, process intensification) is expected; a purely applied performance paper without an engineering-science angle is a weaker fit.

**Domain-referee adjustments.**
- Substantive arguments 20 → 25
- Fit 10 → 15 (must read as chemical engineering, not applied bioenergy alone)

**Methods-referee adjustments.**
- If paper type is `process-modeling`: Model structure 20 → 25, Parameter identification/calibration 25 → 25 (unchanged, already weighted heavily)

**Typical concerns.**
- "Is there a genuine reactor-engineering or mechanistic contribution here, or is this an applied performance study?"
- "Is the process model derived from first principles or purely empirical curve-fitting?"
- "Is the reactor/process design choice justified against alternatives?"

**Referee-pool weights.**
- STRUCTURAL: 0.30
- MEASUREMENT: 0.20
- THEORY: 0.15
- CREDIBILITY: 0.15
- SKEPTIC: 0.10
- POLICY: 0.10

**Table format override.** None specific.

---

### Sustainable Production and Consumption (SPC)

**Short name:** `SPC`

**Focus.** Circular-economy and systems-level sustainability assessment — LCA/TEA of production-consumption systems, policy-relevant framing. Similar territory to JCLP but with a tighter production-consumption-systems lens.

**Bar.** A systems-level sustainability assessment (LCA, TEA, or material-flow analysis) with clear policy or industrial relevance; narrow bench-scale technical work without a systems framing is a weak fit.

**Domain-referee adjustments.**
- External validity 15 → 20
- Fit 10 → 20

**Methods-referee adjustments.**
- If paper type is `lca-tea`: unchanged from base weights — this is the journal's core paper type

**Typical concerns.**
- "Is this framed at the production-consumption-system level, or is it a single-technology performance study?"
- "Is the circular-economy argument (material/resource loop closure) substantiated quantitatively?"
- "Is the LCA/TEA methodology transparent and reproducible?"

**Referee-pool weights.**
- POLICY: 0.30
- MEASUREMENT: 0.20
- CREDIBILITY: 0.15
- STRUCTURAL: 0.15
- SKEPTIC: 0.10
- THEORY: 0.10

**Table format override.** None specific.

---

### Energy

**Short name:** `Energy`

**Focus.** Broad energy-systems journal — quantitative energy/exergy analysis, techno-economic and system-integration studies across all energy technologies, not bioenergy-exclusive.

**Bar.** Rigorous quantitative energy (and ideally exergy) accounting; a bioenergy submission must demonstrate energy-systems relevance, not just conversion-technology performance.

**Domain-referee adjustments.**
- External validity 15 → 20
- Fit 10 → 15

**Methods-referee adjustments.**
- If paper type is `process-modeling`: expect explicit energy (and where relevant exergy) balance closure as part of Model structure

**Typical concerns.**
- "Is a full energy balance (and ideally exergy analysis) reported, not just a headline efficiency number?"
- "How does this technology compare to alternatives on a consistent energy-systems basis?"
- "Is the techno-economic sensitivity to energy-price assumptions shown?"

**Referee-pool weights.**
- STRUCTURAL: 0.25
- MEASUREMENT: 0.20
- POLICY: 0.20
- CREDIBILITY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.10

**Table format override.** Energy and mass balances reported on a consistent, stated basis.

---

### Renewable Energy

**Short name:** `RenewEnergy`

**Focus.** Broad renewables journal (solar, wind, bioenergy, etc.) — technology performance, techno-economic viability, and policy relevance. Bioenergy submissions compete against a broad renewables portfolio for fit.

**Bar.** Technology performance data plus a techno-economic or deployment-relevant argument; the novelty bar is moderate but the paper must clearly earn its place among broader renewables coverage.

**Domain-referee adjustments.**
- Fit 10 → 15
- External validity 15 → 20

**Methods-referee adjustments.**
- If paper type is `lca-tea`: unchanged from base weights

**Typical concerns.**
- "How does this bioenergy pathway compare to other renewable options on a consistent techno-economic basis?"
- "Is the deployment/scale-up pathway credible?"
- "Is the environmental/economic trade-off honestly presented, not just favorable framing?"

**Referee-pool weights.**
- POLICY: 0.25
- STRUCTURAL: 0.20
- MEASUREMENT: 0.20
- CREDIBILITY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.10

**Table format override.** None specific.

---

### Resources, Conservation & Recycling (RCR)

**Short name:** `RCR`

**Focus.** Resource recovery, recycling, and circular-economy assessment — heavily LCA-oriented, waste-valorization and material-flow relevant. Close cousin of Waste Management and SPC with a resource-recovery emphasis.

**Bar.** A resource-recovery or circularity argument substantiated by LCA/material-flow analysis; purely technical conversion performance without a resource-recovery framing is a weaker fit.

**Domain-referee adjustments.**
- Fit 10 → 20
- External validity 15 → 20

**Methods-referee adjustments.**
- If paper type is `lca-tea`: System boundary & functional unit 25 → 30 (resource-recovery accounting scrutinized closely)

**Typical concerns.**
- "Is the resource-recovery/circularity claim substantiated by a material-flow or LCA analysis?"
- "Is the comparison against the linear (non-recovery) baseline explicit?"
- "Is the allocation method for recovered resources justified?"

**Referee-pool weights.**
- MEASUREMENT: 0.25
- POLICY: 0.25
- CREDIBILITY: 0.15
- STRUCTURAL: 0.15
- SKEPTIC: 0.10
- THEORY: 0.10

**Table format override.** None specific.

---

### Bioenergy Research

**Short name:** `BioenergyRes`

**Focus.** Bioenergy-specific, spanning feedstock production/agronomy through conversion. Springer journal with a moderate rigor bar, receptive to both fundamental science and applied conversion work.

**Bar.** Solid, well-documented work across the feedstock-to-conversion spectrum; moderate novelty bar relative to BRT or Fuel, with room for applied and agronomy-adjacent contributions.

**Domain-referee adjustments.**
- Contribution 30 → 25 (moderate novelty bar)
- Lit positioning 25 → 25 (unchanged)

**Methods-referee adjustments.**
- If paper type is `experimental`: unchanged from base weights

**Typical concerns.**
- "Is the feedstock-to-conversion link clearly established and characterized?"
- "Are yields and performance data reported on a consistent basis with adequate replication?"
- "Is the work positioned against both agronomy and conversion literatures where relevant?"

**Referee-pool weights.**
- MEASUREMENT: 0.25
- STRUCTURAL: 0.20
- CREDIBILITY: 0.15
- POLICY: 0.15
- THEORY: 0.10
- SKEPTIC: 0.15

**Table format override.** None specific.

---

## Field adaptation

The 17 profiles above are bioenergy/circular-biorefinery-specific. The **pipeline is field-agnostic** — nothing in `editor.md`, `domain-referee.md`, or `methods-referee.md` hard-codes this discipline. What varies by field is the journal profile and the paper-type taxonomy.

**To adapt for a different field:**

1. Copy `templates/journal-profile-template.md` into a new section below (use `### Journal Name (SHORT)`).
2. Fill each schema field:
   - **Focus** — what the journal publishes (look at the last 6 months of TOC).
   - **Bar** — acceptance rate + one sentence on what the editor is looking for.
   - **Domain-referee adjustments** — re-weight contribution / lit-positioning / substance / external validity / fit for this journal's taste.
   - **Methods-referee adjustments** — for a field whose paper types differ from this fork's (`experimental` / `process-modeling` / `lca-tea` / `review`), edit `methods-referee.md` to add your field's paper types and their dimension weights.
   - **Typical concerns** — read 2–3 recent reviews and distill 3–5 recurring referee questions.
   - **Referee-pool weights** — the 6 dispositions are general enough to apply to any field. Re-weight based on what that journal's referees actually ask about. Weights must sum to 1.0.
   - **Table format** — any field-specific conventions.

**The archived economics/political-science profiles** (`_archive/economics-tools/references/journal-profiles-econ-polisci.md`) and their paper-type taxonomy (`_archive/economics-tools/agents/methods-referee-econ-polisci.md`) are a complete worked example of a from-scratch field adaptation, preserved for reference.

---

## Cross-references

- `.claude/agents/editor.md` — reads this file.
- `.claude/agents/domain-referee.md` — applies domain-referee adjustments.
- `.claude/agents/methods-referee.md` — applies methods-referee adjustments.
- `.claude/skills/review-paper/SKILL.md` — `--peer [journal]` mode entry point.
- `templates/journal-profile-template.md` — skeleton for adding your own.
