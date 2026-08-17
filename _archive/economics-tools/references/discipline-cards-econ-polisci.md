# Archived: Economics & Political Science Discipline Cards

**Archived:** 2026-08-17, when this fork's active `.claude/references/discipline-cards.md` was narrowed to a single active discipline (Bioenergy & Circular Biorefinery). These two cards are the original template's shipped disciplines, preserved verbatim for reference or restoration — see `_archive/economics-tools/README.md` for the restore procedure.

They are **not** loaded by any active skill or agent. The active `discipline-cards.md` does not reference them.

---

## Economics (`econ`)

**Paper-type frequencies (rough share of empirical work in top-5 journals).**

| Type | Share | Notes |
|---|---|---|
| Reduced-form | ~55% | DiD, IV, RD, event study, synthetic control. The dominant mode. |
| Structural | ~20% | DSGE, GE, IO empirical. Concentrated in macro / IO / labour. |
| Theory + empirics | ~15% | Theory-paper-with-empirical-test or empirical-paper-with-theory-section. |
| Descriptive | ~5% | Measurement / data-construction. Often the AEA P&P route. |
| Formal-theory | ~5% | Pure theory (micro, IO, contracts). More common in ECMA / TE / JET. |

**Dominant journals.** AER, QJE, JPE, ECMA, ReStud. AEA P&P (proceedings) for descriptive / measurement work.

**Preregistration norms.**
- **Field experiments / RCTs:** mandatory in the **AEA RCT Registry** since 2018 for AEA-journal submission.
- **Lab experiments:** OSF / AsPredicted increasingly common; not yet uniformly required.
- **Observational / archival:** preregistration uncommon; pre-analysis plans appearing in some applied-micro corners.
- **Replication packages:** AEA Data and Code Availability Policy enforced; replication archive at JEL data archive.

**Method conventions.**
- Significance stars: AEA journals do **NOT** use stars in tables (since 2018 AEA Code style guide). Other journals (e.g., ReStud, JPubE) still allow them.
- Standard-error reporting: clustered SEs at treatment-assignment level expected; Conley / spatial SEs required for spatial data.
- Code: R, Stata, Python, Julia all accepted; replication packages must be self-contained and deterministic (`set.seed`).

**Cross-references (as shipped originally).** `methods-referee.md` paper types: reduced-form, structural, theory+empirics, descriptive, formal-theory. `journal-profiles.md`: AER, QJE, JPE, ECMA, ReStud.

---

## Political Science (`poli-sci`)

**Paper-type frequencies (rough share of empirical work in top-3 journals).**

| Type | Share | Notes |
|---|---|---|
| Reduced-form | ~40% | Causal inference (DiD, IV, RD), observational identification. Strongest at AJPS. |
| Survey-experiment | ~25% | Vignette, conjoint, list-experiment, factorial. Strong at AJPS, JOP; rising at APSR. |
| Formal-theory | ~15% | Game-theoretic, mechanism-design, formal political theory. Strongest at APSR. |
| Descriptive | ~10% | Cross-national / historical / case-study description. |
| Theory + empirics | ~10% | Formal theory with empirical test of equilibrium predictions. |

**Dominant journals.** APSR, AJPS, JOP. Subfield outlets (IO, World Politics, JOP-research-notes track) also strong.

**Preregistration norms.**
- **Survey experiments / lab experiments / field experiments:** OSF or AsPredicted increasingly expected. **AJPS Replication Policy** (since 2015) makes replication archive mandatory at acceptance, but preregistration itself is a community norm not a hard requirement.
- **Observational:** PAP (preanalysis plan) appearing in applied work; not yet uniform.
- **AEA RCT Registry** is for econ; political-science field experiments more often use OSF or EGAP's repository (egap.org) — though EGAP merged its registry into OSF in 2022.

**Method conventions.**
- Significance stars: ARE used (typical floor 0.05/0.01/0.001). APSA Style Manual governs citations.
- Standard-error reporting: clustered SEs at subject level for survey experiments, robust SEs (HC2 or HC3) standard.
- Replication archive: AJPS Replication Policy requires deposit before acceptance; APSR and JOP recommend.
- Code: R is dominant; Stata still common in IR / comparative; Python rising for text-as-data work.

**Cross-references (as shipped originally).** `methods-referee.md` paper types: reduced-form, formal-theory, survey-experiment, theory+empirics, descriptive (structural is rare in poli-sci). `journal-profiles.md`: APSR, AJPS, JOP.
