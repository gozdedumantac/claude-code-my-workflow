# Archived: Economics & Political Science Journal Profiles

**Archived:** 2026-08-17, when the active `.claude/references/journal-profiles.md` was narrowed to a single active discipline (Bioenergy & Circular Biorefinery, 17 journals). This file preserves the original template's five econ top-5 and three political-science journal profiles verbatim, for reference or restoration.

Not loaded by any active skill or agent.

---

## Econ Top-5

> **AEA Data Editor / DCAS policy (applies to all AEA-imprint journals — AER, AEJ:*, JEL, JEP).** Acceptance is conditional on a replication package that clears the **AEA Data and Code Availability Standard** under the Data Editor: a complete deposit (openICPSR), a data availability statement, and code that reproduces every reported number. Econometrica, ReStud, and the political-science journals below enforce comparable archives at acceptance.

### American Economic Review (AER)

**Short name:** `AER`

**Focus.** General-interest economics across all fields. Strongest bar for substantive contribution and policy relevance. Favors credible identification + interpretable magnitudes + clear narrative over technical novelty.

**Bar.** "Publishing here means the top-10 people in your field will read it." Topic must matter beyond specialists. Contribution must be crisp in one paragraph.

**Domain-referee adjustments.**
- Contribution 30 → 35 (the bar on importance is higher)
- External validity 15 → 20 (generalizability matters more)
- Fit 10 → 5 (AER publishes across fields; fit is less of a constraint)

**Methods-referee adjustments.**
- Identification 35 → 40 (credibility is load-bearing)
- Replication 5 → 10 (AER Data and Code Availability Policy is strict)

**Typical concerns.**
- "Is the research question important enough for a general-interest journal?"
- "Is the identification strategy credible to a skeptical non-specialist?"
- "Does the magnitude tell us something we didn't already know?"
- "Are the robustness checks addressing the obvious threats, or are they theater?"
- "Is the replication package complete enough for the AEA Data Editor?"

**Referee-pool weights.**
- CREDIBILITY: 0.30
- POLICY: 0.25
- STRUCTURAL: 0.15
- MEASUREMENT: 0.15
- THEORY: 0.05
- SKEPTIC: 0.10

**Table format override.** No significance stars (AEA policy since 2023). Use SE in parentheses only; indicate p-values in notes if needed.

---

### Quarterly Journal of Economics (QJE)

**Short name:** `QJE`

**Focus.** Identification-first empirical work and theory with sharp predictions. Taste for clever natural experiments, rich data, and economic insight over methodological flash.

**Bar.** Identification must be near-airtight. Willing to accept narrow settings if the design is exceptional. Wants a paper that could be taught in a graduate class.

**Domain-referee adjustments.**
- Contribution 30 → 30 (unchanged)
- Substance 20 → 25 (taste matters — clever > competent)

**Methods-referee adjustments.**
- Identification 35 → 45 (this is the QJE house style)
- Robustness 15 → 10 (QJE referees are less tolerant of robustness-as-theater)

**Typical concerns.**
- "Is the research design genuinely clever, or is this yet another DiD?"
- "Does the first-stage / exclusion restriction / parallel-trends assumption have teeth?"
- "Would I teach this paper's identification strategy?"
- "What's the one-sentence economic insight here?"

**Referee-pool weights.**
- CREDIBILITY: 0.40
- STRUCTURAL: 0.20
- MEASUREMENT: 0.15
- POLICY: 0.10
- THEORY: 0.10
- SKEPTIC: 0.05

**Table format override.** Three-decimal point estimates standard; SE in parentheses.

---

### Journal of Political Economy (JPE)

**Short name:** `JPE`

**Focus.** Economic theory + empirical work tightly connected to theory. Chicago-flavored taste: markets, incentives, mechanism. Less sympathetic to pure reduced-form.

**Bar.** Theory component must be present and nontrivial — even in empirical papers, "what does the theory predict before we estimate" is expected.

**Domain-referee adjustments.**
- Contribution 30 → 30 (unchanged)
- Substance 20 → 30 (theory connection is load-bearing)

**Methods-referee adjustments.**
- If paper type is `theory+empirics`: Model 20 → 30, Prediction sharpness 25 → 30
- If paper type is `reduced-form`: Identification 35 → 30, expect explicit theoretical framing

**Typical concerns.**
- "What does the theory predict, and does the empirical work speak to that prediction?"
- "Is the mechanism spelled out, or are we just estimating a reduced-form coefficient?"
- "Do the magnitudes match what a reasonable model would imply?"
- "Is the paper arguing against a specific alternative theory, or waving at 'possible mechanisms'?"

**Referee-pool weights.**
- THEORY: 0.30
- STRUCTURAL: 0.25
- CREDIBILITY: 0.15
- MEASUREMENT: 0.10
- POLICY: 0.10
- SKEPTIC: 0.10

**Table format override.** None journal-specific.

---

### Econometrica (ECMA)

**Short name:** `ECMA`

**Focus.** Econometric theory, structural estimation, formal theory. Less sympathetic to reduced-form papers without methodological contribution. Mathematical rigor expected.

**Bar.** A methodological or theoretical advance must be visible. Applied papers clear the bar only if they bring a new estimator or a novel identification argument.

**Domain-referee adjustments.**
- Contribution 30 → 35 (methodological contribution weight)
- Fit 10 → 5 (ECMA tolerates narrower settings if the method generalizes)

**Methods-referee adjustments.**
- If paper type is `structural`: Model spec 20 → 30, Parameter ID 30 → 35, Counterfactuals 15 → 15
- If paper type is `reduced-form`: Identification 35 → 40, expect proofs / formal arguments
- Replication 5 → 10 (code + proofs must match)

**Typical concerns.**
- "What's the methodological contribution?"
- "Are the identifying assumptions stated formally, not just verbally?"
- "Are the asymptotic properties of the estimator established?"
- "Would an econometrician who reads only the abstract know what's new here?"

**Referee-pool weights.**
- STRUCTURAL: 0.30
- THEORY: 0.25
- MEASUREMENT: 0.20
- CREDIBILITY: 0.15
- POLICY: 0.05
- SKEPTIC: 0.05

**Table format override.** None specific; mathematical notation must be consistent throughout.

---

### Review of Economic Studies (ReStud)

**Short name:** `ReStud`

**Focus.** Conceptually ambitious work across theory, empirical, and macro. European-flavored taste: willing to publish unfashionable topics if the idea is strong. Values careful reasoning over technical fireworks.

**Bar.** A clear "intellectual arc" — the paper should leave the reader understanding something new about how the world works, not just a new estimate.

**Domain-referee adjustments.**
- Contribution 30 → 35
- Substance 20 → 25

**Methods-referee adjustments.**
- Identification 35 → 35 (unchanged; care but not QJE-level obsession)
- Honesty (for theory+empirics) 15 → 20

**Typical concerns.**
- "What do we understand about the world that we didn't before?"
- "Is the argument careful, or is it a victory lap?"
- "Are the limitations honestly stated, or buried?"
- "Does the conclusion generalize beyond this specific setting, and if so, how?"

**Referee-pool weights.**
- STRUCTURAL: 0.20
- CREDIBILITY: 0.20
- THEORY: 0.20
- POLICY: 0.15
- MEASUREMENT: 0.15
- SKEPTIC: 0.10

**Table format override.** None specific.

---

## Political Science (Top-3)

### American Political Science Review (APSR)

**Short name:** `APSR`

**Focus.** Highest-bar general-interest political-science journal; APSA's flagship. Publishes across IR, comparative politics, American politics, formal theory, and political theory. Strongest preference for theoretically motivated work that speaks to multiple subfields.

**Bar.** "Top-3 in your subfield should know this." A clear theoretical contribution is load-bearing.

**Domain-referee adjustments.**
- Contribution 30 → 35
- Lit positioning 25 → 25 (unchanged)
- Fit 10 → 5

**Methods-referee adjustments.**
- Identification 35 → 30
- For `formal-theory` papers: Comparative-static sharpness 25 → 30
- For `survey-experiment` papers: sampling-frame validity is a desk-level concern

**Typical concerns.**
- "Where is the theoretical contribution?"
- "Is the design appropriate to the population the paper claims to speak about?"
- "Does the paper engage seriously with formal theory, or only with reduced-form empirics?"
- "Is the conclusion testable, or vacuous?"

**Referee-pool weights.**
- THEORY: 0.30
- CREDIBILITY: 0.20
- STRUCTURAL: 0.15
- MEASUREMENT: 0.15
- POLICY: 0.10
- SKEPTIC: 0.10

**Table format override.** APSA Style Manual; significance stars typical (0.05/0.01/0.001 floor).

### American Journal of Political Science (AJPS)

**Short name:** `AJPS`

**Focus.** General political-science journal with strong methods orientation. Receptive to causal-inference, survey experiments, formal-empirical work.

**Bar.** "The method is at least as interesting as the substance." AJPS Replication Policy (since 2015) enforced.

**Domain-referee adjustments.**
- External validity 15 → 20

**Methods-referee adjustments.**
- Identification 35 → 40
- For `survey-experiment` papers: manipulation checks and balance tables mandatory
- Replication 5 → 10

**Typical concerns.**
- "Is identification credible to a methodologist?"
- "Is the design pre-registered?"
- "Are the standard errors clustered at the right level?"
- "Is the replication archive complete?"

**Referee-pool weights.**
- CREDIBILITY: 0.30
- MEASUREMENT: 0.20
- STRUCTURAL: 0.15
- THEORY: 0.15
- SKEPTIC: 0.10
- POLICY: 0.10

**Table format override.** APSA Style; significance stars allowed.

### Journal of Politics (JOP)

**Short name:** `JOP`

**Focus.** Top-3 political-science journal, slight tilt toward American/comparative politics. Receptive to shorter research notes alongside full articles.

**Bar.** "A clear contribution to a substantive question that political scientists care about."

**Domain-referee adjustments.**
- Contribution 30 → 35
- Substance 20 → 25
- Fit 10 → 5

**Methods-referee adjustments.**
- Robustness 15 → 20

**Typical concerns.**
- "What specifically does this paper add?"
- "Is the argument tight?"
- "Are the robustness checks responsive to real threats?"
- "Could this be a research note instead?"

**Referee-pool weights.**
- SKEPTIC: 0.25
- CREDIBILITY: 0.20
- THEORY: 0.15
- MEASUREMENT: 0.15
- STRUCTURAL: 0.15
- POLICY: 0.10

**Table format override.** APSA Style; standard significance stars allowed.
