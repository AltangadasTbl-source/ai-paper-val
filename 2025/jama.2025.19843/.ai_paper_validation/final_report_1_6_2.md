# LEVOECMO Trial: Quantitative Quality-Control Consistency Review

**Pending Human Adjudication**

Workflow 1.6.2. Every candidate below is a reporting quality-control item for human adjudication. Evidence states describe reproduction from supplied sources; inclusion audit values describe compliance with the review scope. Neither field determines a human disposition.

## Executive Quality-Control Summary

Seven stable candidate reporting issues were identified after complete mapping of six supplied PDFs, comprising 194 pages. One concerns primary-model covariate descriptions within the main article; six concern planned versus reported endpoint definitions, analysis populations, time windows or adjusted outputs. All seven have evidence state **reproduced** and inclusion audit **CONFIRMED**, and all remain **Pending Human Adjudication**.

The initial checker wave produced 15 findings. Independent screening included 14 contributing findings, consolidated into seven issues, and screened out one conditional observation. A different fresh statistical reviewer revisited every statistical relationship and all checker exclusions; no additional finding was emitted. The final independent audit retained every registered candidate and screening decision. The review establishes reporting comparisons, not that a numerical treatment effect or trial conclusion changed.

## Package and Reused-Evidence Provenance

The supplied package concerns levosimendan versus placebo for successful weaning from venoarterial extracorporeal membrane oxygenation. Document roles follow content: the main article and observed-result/administrative supplements are REPORT; prospective protocol versions and the statistical analysis plan (SAP) are PLAN.

| Source | Actual filename | Role | Pages |
|---|---|---|---:|
| DOC-001 | jama_combes_2025_oi_250087_1766516490.94011.pdf | REPORT | 10 |
| DOC-002 | joi250087supp1_prod_1766516490.96011.pdf | PLAN | 153 |
| DOC-003 | joi250087supp2_prod_1766516490.96511.pdf | PLAN | 9 |
| DOC-004 | joi250087supp3_prod_1766516490.97011.pdf | REPORT | 18 |
| DOC-005 | joi250087supp4_prod_1766516490.97511.pdf | REPORT | 3 |
| DOC-006 | joi250087supp5_prod_1766516490.97511.pdf | REPORT | 1 |
| Total | Six supplied PDFs | Content-defined roles | 194 |

A fresh curator inventoried and hashed 116 existing text, OCR, image, map and metadata assets, recording usable, partial, duplicate and unreadable fitness separately. Earlier candidate sets, screening/classification decisions and reports did not supply candidate discovery. Reuse provided source locators and transcriptions; fresh agents rebuilt the scientific maps and directly inspected uncovered units. The exact inventories are preserved in [source inventory](review_1_6_2/source_inventory.md) and [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md).

## Scope, Complete Coverage, and Exclusions

| Source | Total pages | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 153 | 150 | 3 | 153 | COMPLETE |
| DOC-003 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | 18 | 18 | 0 | 18 | COMPLETE |
| DOC-005 | 3 | 3 | 0 | 3 | COMPLETE |
| DOC-006 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 194 | 191 | 3 | 194 | COMPLETE |

Protocol physical pages 4, 49 and 95 are signed image pages and received fresh rendering and visual mapping. The page-95 gap was identified and closed in the coverage audit. Every scanned SAP page was visually mapped; unavailable native text or incomplete historical OCR did not leave an unmapped source unit. All six source rows satisfy reusable plus fresh-required equals total, with mapped equal to total. [Source coverage](review_1_6_2/source_coverage.md) and the [coverage manifest](review_1_6_2/coverage_manifest.md) retain the complete disjoint stage assignments.

The review addresses counts and denominators, estimate/test logic, statistical method logic and planned versus reported statistical design. It excludes broad clinical or methodological critique, analysis preferences and unsupplied participant-data reconstruction. Routine wording, symbols, contextual differences, modeled-versus-crude comparisons and peripheral administrative comparisons are screened under the supplied scope. Numeric comparisons use half-unit display intervals; relative gaps at most 0.05 are screened as display precision. Interval-versus-P-value/test conflicts remain independently qualifying. No candidate rests solely on a display-zero P value.

## Quantitative and Statistical Relationship Coverage

| Review lane | Complete scope | Findings emitted |
|---|---|---:|
| Numeric consistency | 205 families: N001–N095 and N201–N310 | 0 |
| Cross-source consistency | 123 matched groups, including the remaining three-group shard | 7 |
| Statistical pass 1 | S001–S107; every row PASS_1_COMPLETE | 8 |
| Statistical pass 2 | S001–S107; every row PASS_2_COMPLETE | 0 new |

The numeric inventory covers participant flow, denominators, table totals, event percentages, binary effect identities and plan arithmetic. Cross-source comparisons cover report/report, plan/report and plan/plan relationships. Statistical coverage includes the primary Fine–Gray analysis and competing events, secondary contrasts and survival displays, endpoint windows/definitions, subgroups, sample-size inputs and planned analysis outputs. These are relationship groups, not a count of independent hypotheses.

Statistical pass 1 was performed by root/statistics_1 and pass 2 by the different fresh root/statistics_2, both gpt-6.1-sol/high. Pass 2 incorporated the complete ledger, screening decisions and direct-source recheck, and individually reconsidered all 44 checker Excluded observations rows against both inclusion routes and display precision. No new finding required another screen. The final audit closes every numeric, cross-source and statistical relationship through complete disjoint audit parts. Full records are the [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_2/statistics/relationship_inventory.md), [first statistical pass](review_1_6_2/checkers/statistical_pass_1.md), [second statistical pass](review_1_6_2/checkers/statistical_pass_2.md) and [complete quality audit](review_1_6_2/quality/evidence_quality_audit.md).

## Inclusion Screening Summary

A reproduced observation qualifies through Route A, one of the five always-register categories, or through Route B: in focus, unresolved by immediate context and bearing on a named result or extracted value. The independent screener reread the exact supplied locations and consolidated repeated issues while preserving every finding and location. There was no candidate-count target.

| Decision | Reason code | Finding rows |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 14 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| Total | All initial findings | 15 |

Fourteen included rows represent seven stable candidates, each with two contributing findings. All other screened-out reason codes have zero finding rows. F-ST1-007 was screened because the apparent kidney-replacement-duration contradiction required unprinted duration-population, receipt-equivalence and zero-coding assumptions; missing coding alone did not establish a reproduced conflict. It receives no evidence card. The 44 self-screened checker observations are separate from these 15 finding rows: 13 numeric, 16 cross-source and 15 statistical. Pass 2 and the auditor revisited all 44; no reversal or new finding resulted. [The screening log](review_1_6_2/screening/inclusion_screen.md) supplies every decision and rationale.

## Review-Domain Summary

The four domains are statistical_results for counts, estimates, tests or methods within REPORT material; report_internal_inconsistency for conflicting outcome/population/time attribution within REPORT material; protocol_report for PLAN/REPORT statistical-design comparisons; and plan_material for statistical-design inconsistencies solely in PLAN material. Relationship precedence is P_R > P_P > S_C > S_W. Corroboration alone does not add a conflicting relationship.

| Review domain | Candidates |
|---|---:|
| statistical_results | 1 |
| report_internal_inconsistency | 0 |
| protocol_report | 6 |
| plan_material | 0 |
| Total | 7 |

| Primary relationship type | Candidates |
|---|---:|
| P_R | 6 |
| P_P | 0 |
| S_C | 0 |
| S_W | 1 |
| Total | 7 |

| Evidence state | Candidates |
|---|---:|
| reproduced | 7 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 7 |

Inclusion audits: seven CONFIRMED and zero QUESTIONED. C005 also involves P_P and S_C relationships; it is counted once under its primary P_R relationship. The [ledger classification table](review_1_6_2/candidate_ledger.md) is the authoritative source for the exact fields below.

## Candidate Index

| ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Primary adjustment covariate descriptions do not reconcile | statistical_results | S_W | reproduced | CONFIRMED |
| C002 | Organ-failure threshold differs between SAP and report | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Planned day-60 free-day results are absent from supplied reports | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | Planned hierarchical LV-function composite differs from reported LVEF contrast | protocol_report | P_R | reproduced | CONFIRMED |
| C005 | Dialysis membership differs across MACE definitions | protocol_report | P_R | reproduced | CONFIRMED |
| C006 | Planned post-arrest subgroup differs from reported predefined other-etiology subgroup | protocol_report | P_R | reproduced | CONFIRMED |
| C007 | Planned adjusted key-secondary analyses lack supplied outputs | protocol_report | P_R | reproduced | CONFIRMED |

# Candidate Evidence Cards

All cards remain **Pending Human Adjudication**. Exact locations below use physical PDF pages and actual filenames. Absence comparisons are limited to all 32 supplied REPORT pages: main article 1–10, results supplement 1–18, roster 1–3 and sharing statement 1. They do not assert that an analysis was never performed or that no output exists elsewhere.

## C001 — Primary adjustment covariate descriptions do not reconcile

**Pending Human Adjudication**

**Candidate statement:** The main article describes adjustment on minimization factors, identified as etiology and center, but its primary-model footnote specifies etiology alone.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Randomization/Statistical Analysis vs REPORT Table 2 footnote c; PLAN SAP corroborates only

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-001

**Qualifying route:** Route B

**Classification rationale:** Both conflicting model descriptions are within the REPORT main article, so S_W/statistical_results applies. The PLAN SAP corroborates etiology-only wording and does not create a P_R conflict.

**Classification ambiguity:** None in content roles or relationship precedence. Operational/model explanations remain bounded by the supplied evidence.

**Exact source locations:** [main PDF p.2](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=2); [main PDF p.3](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); [main PDF p.6](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6); [SAP PDF p.6, corroboration only](../joi250087supp2_prod_1766516490.96511.pdf#page=6)

**Source evidence:** Randomization names primary cardiogenic-shock etiology and center. Statistical Analysis describes adjustment on minimization stratification factors. Table 2 footnote c describes a Fine–Gray model adjusted for etiology; the reported primary successful-weaning sHR is 1.02 (95% CI 0.74–1.39).

**Reported-versus-comparator:** General primary-adjustment description: {etiology, center}; specific table footnote: {etiology}.

**Reasoning procedure:** Match the randomization factors to the analysis sentence and the table model description. Separate observed wording from any inference about the fitted model; the actual model formula is not supplied.

**Calculation:** Categorical set comparison: the stated factor sets differ by center. Half-unit display intervals do not apply to covariate membership. No alternative sHR or numerical discrepancy in 1.02 is asserted.

**Affected result or extracted value:** The covariate specification attached to primary successful-weaning sHR 1.02 (0.74–1.39).

**Why context does not resolve it:** Etiology and center are distinct factors. The immediate report context does not establish whether footnote c is abbreviated or exhaustive, leaving the fitted covariate set unclear.

**Alternative source-grounded interpretations:** The fitted model may include center despite an abbreviated footnote, or the general sentence may intend etiology alone. Neither interpretation is demonstrated by a model formula or output.

**Mechanical evidence recheck:** Every main location and the SAP corroboration were found and matched; the main pages were directly rendered and visually read. Footnote c was already the registered locator, so the state is reproduced. Missing formula, center coding and footnote exhaustiveness remain bounded definitions. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An extractor could attach an etiology-only or etiology-plus-center adjustment label to the same primary sHR. The review does not establish which model was fitted.

## C002 — Organ-failure threshold differs between SAP and report

**Pending Human Adjudication**

**Candidate statement:** The SAP defines organ failure by a component SOFA score >2, while the report defines organ-failure-free days by every component score being 0–1.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP vs REPORT main Outcomes/results eTable 3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-004

**Qualifying route:** Route B

**Classification rationale:** The operational threshold in PLAN SAP is compared with the REPORT endpoint description and summaries, giving P_R/protocol_report. The supplementary figure corroborates score categories rather than adding a report/report conflict.

**Classification ambiguity:** None in content roles or relationship precedence. Operational/model explanations remain bounded by the supplied evidence.

**Exact source locations:** [sap PDF p.4](../joi250087supp2_prod_1766516490.96511.pdf#page=4); [sap PDF p.7](../joi250087supp2_prod_1766516490.96511.pdf#page=7); [main PDF p.3](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); [results PDF p.5](../joi250087supp3_prod_1766516490.97011.pdf#page=5); [results PDF p.12](../joi250087supp3_prod_1766516490.97011.pdf#page=12)

**Source evidence:** Both SAP occurrences print >2 in at least one of six organ systems. The main Outcomes section requires 0–1 for each component for freedom from organ failure. eFigure 3 separately displays score 2. eTable 3 reports free-day medians 12 (0–21) versus 14 (0–23), difference −2 (−10 to 4), and failure-day medians 9 (6–17) versus 12 (6–18), difference −3 (−5 to 2).

**Reported-versus-comparator:** SAP failure threshold >2 versus report free-day threshold all components ≤1.

**Reasoning procedure:** Compare the two explicit operational rules at the integer score-2 boundary, using a living-patient day so death-zero coding cannot explain the difference. Link the rule comparison to the printed organ-day summaries.

**Calculation:** For one component equal to 2 and all other components 0 or 1: no component exceeds 2, but not every component is ≤1. The rules classify that day differently. This logical example does not establish that such a day occurred. Display precision does not reconcile decision thresholds.

**Affected result or extracted value:** Organ-failure-free medians 12/14 and difference −2, and organ-failure-duration medians 9/12 and difference −3 in eTable 3.

**Why context does not resolve it:** No supplied coding statement explains the classification of score-2 days under both definitions. A displayed integer category cannot be reconciled by numerical rounding or death-zero coding.

**Alternative source-grounded interpretations:** The SAP threshold may be abbreviated, or the report may describe a distinct operational free-day rule. A separately specified score-2 treatment could reconcile implementation, but none is supplied.

**Mechanical evidence recheck:** Both SAP repetitions, main Outcomes, eTable 3 and eFigure 3 were located and visually matched. The logical boundary contrast was reproduced. Endpoint code, missing-component handling and participant score histories are unavailable; revised summaries cannot be calculated. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An evidence extractor could record different SOFA thresholds for the same organ-day outcomes. No number of affected participant-days or change in the printed treatment contrast is inferred.

## C003 — Planned day-60 free-day results are absent from supplied reports

**Pending Human Adjudication**

**Candidate statement:** Planned day-60 ECMO-free and ventilation-free analyses have no corresponding output in the supplied reports, which present day-30 free-day summaries.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol/SAP vs REPORT main/results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-008

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN protocol/SAP specify key-secondary windows; the REPORT package lacks their day-60 counterparts, so P_R/protocol_report applies. Agreement among plan versions adds no P_P relationship.

**Classification ambiguity:** None in content roles or relationship precedence. Operational/model explanations remain bounded by the supplied evidence.

**Exact source locations:** Every repeated protocol endpoint occurrence: [protocol PDF p.8](../joi250087supp1_prod_1766516490.96011.pdf#page=8); [protocol PDF p.14](../joi250087supp1_prod_1766516490.96011.pdf#page=14); [protocol PDF p.15](../joi250087supp1_prod_1766516490.96011.pdf#page=15); [protocol PDF p.53](../joi250087supp1_prod_1766516490.96011.pdf#page=53); [protocol PDF p.59](../joi250087supp1_prod_1766516490.96011.pdf#page=59); [protocol PDF p.60](../joi250087supp1_prod_1766516490.96011.pdf#page=60); [protocol PDF p.99](../joi250087supp1_prod_1766516490.96011.pdf#page=99); [protocol PDF p.105](../joi250087supp1_prod_1766516490.96011.pdf#page=105); [protocol PDF p.106](../joi250087supp1_prod_1766516490.96011.pdf#page=106). SAP: [sap PDF p.4](../joi250087supp2_prod_1766516490.96511.pdf#page=4); [sap PDF p.7](../joi250087supp2_prod_1766516490.96511.pdf#page=7); [sap PDF p.8](../joi250087supp2_prod_1766516490.96511.pdf#page=8). REPORT: [main PDF p.1](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1); [main PDF p.3](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); [main PDF p.6](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6); [results PDF p.5](../joi250087supp3_prod_1766516490.97011.pdf#page=5)

**Source evidence:** All nine protocol endpoint lists and the relevant SAP sections specify D30 and D60 free-day windows. Main Outcomes also names both windows. The abstract names ECMO-free and ventilation-free outcomes, making them key secondary under this scope. Table 2 reports ECMO-free by day 30, 24 (0–26) versus 23 (12–26), difference 1 (−1 to 4). eTable 3 reports ventilation-free by day 30, 6 (3–11) versus 6 (3–13), difference −0 (−3 to 2).

**Reported-versus-comparator:** Planned matched-window set {D30, D60}; supplied corresponding free-day summaries {D30}.

**Reasoning procedure:** Match outcome names and windows across all protocol versions, SAP and main endpoint definition; inspect all 32 supplied REPORT pages and every scientific display for the D60 distributions or treatment contrasts.

**Calculation:** No matched D60 free-day output was found. Numeric display intervals do not convert a day-30 endpoint into a day-60 endpoint. D60 mortality, stay duration and follow-up confirming D30 weaning success represent different quantities.

**Affected result or extracted value:** The unavailable D60 ECMO-free and D60 ventilation-free distributions and treatment contrasts; the printed D30 contrasts remain distinct.

**Why context does not resolve it:** Route A, category 5: planned key-secondary analyses are not reported in the supplied REPORT union. The abstract establishes key-secondary status; the issue concerns endpoint windows rather than peripheral contributor counts.

**Alternative source-grounded interpretations:** The D60 outputs may exist in unsupplied material, or a later documented amendment may have removed them. Neither is established by the package; no assertion is made that the analyses were never performed.

**Mechanical evidence recheck:** All nine protocol endpoint occurrences, SAP pp.4/7/8 and the exact main/table locations matched. Complete REPORT coverage confirmed the bounded absence. D60 values and any window-removing amendment are not supplied. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An extractor could treat the day-30 result as the only available free-day estimate while assuming that both planned windows were reported. The package supplies no D60 effect for extraction.

## C004 — Planned hierarchical LV-function composite differs from reported LVEF contrast

**Pending Human Adjudication**

**Candidate statement:** The SAP specifies a death/transplant/LV-function hierarchical composite and Global Net Benefit, while the supplied LV-function result is a marginal LVEF median contrast.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP vs REPORT main Outcomes/results eTable 3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004, F-ST1-002

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN SAP defines the hierarchical composite; REPORT main/results material supplies the marginal LVEF result, yielding P_R/protocol_report. Protocol endpoint lists corroborate D30 LV-function context.

**Classification ambiguity:** None in content roles or relationship precedence. Whether the LVEF result substitutes for or supplements the planned composite remains unresolved.

**Exact source locations:** Protocol context, every occurrence: [protocol PDF p.8](../joi250087supp1_prod_1766516490.96011.pdf#page=8); [protocol PDF p.14](../joi250087supp1_prod_1766516490.96011.pdf#page=14); [protocol PDF p.15](../joi250087supp1_prod_1766516490.96011.pdf#page=15); [protocol PDF p.53](../joi250087supp1_prod_1766516490.96011.pdf#page=53); [protocol PDF p.59](../joi250087supp1_prod_1766516490.96011.pdf#page=59); [protocol PDF p.60](../joi250087supp1_prod_1766516490.96011.pdf#page=60); [protocol PDF p.99](../joi250087supp1_prod_1766516490.96011.pdf#page=99); [protocol PDF p.105](../joi250087supp1_prod_1766516490.96011.pdf#page=105); [protocol PDF p.106](../joi250087supp1_prod_1766516490.96011.pdf#page=106). [SAP PDF p.8, Left Ventricular Function](../joi250087supp2_prod_1766516490.96511.pdf#page=8); [main PDF p.3](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3); [results PDF p.5](../joi250087supp3_prod_1766516490.97011.pdf#page=5); [results PDF p.6](../joi250087supp3_prod_1766516490.97011.pdf#page=6)

**Source evidence:** SAP p.8 orders death, heart transplantation and LV-function improvement/LVEF >30% in experimental/control pairwise comparisons, with bootstrap confidence intervals for Global Net Benefit. eTable 3 instead supplies LVEF medians 45 (30–50), n=100, versus 40 (25–50), difference 5 (−0 to 10). Footnote a uses D30 LVEF in survivors and the last available pre-death value in decedents; footnote b describes the median contrast and bootstrap interval.

**Reported-versus-comparator:** Prespecified hierarchical composite/net-benefit quantity versus supplied marginal LVEF percentage-point median contrast.

**Reasoning procedure:** Compare endpoint ordering, handling of death/transplantation and the statistic produced. Inspect complete supplied reports for a hierarchical or Global Net Benefit output, retaining the possibility that the marginal result is additional descriptive reporting.

**Calculation:** 45−40=5; half-unit input intervals [44.5,45.5] and [39.5,40.5] permit difference [4,6], overlapping the printed difference interval [4.5,5.5]: gap 0, relative discrepancy 0. The medians reconcile numerically; they do not encode wins/losses/ties or the death-first hierarchy. Global Net Benefit cannot be recomputed from marginal medians.

**Affected result or extracted value:** The endpoint and estimand attached to the LVEF difference 5 (−0 to 10), and the unsupplied planned hierarchical net-benefit output.

**Why context does not resolve it:** Route A, category 5: a prespecified composite definition changes in the supplied outcome presentation. This category applies independently of key-secondary status; a marginal median does not supply the death/transplant hierarchy.

**Alternative source-grounded interpretations:** The LVEF result may be an additional descriptive summary while the hierarchical analysis was performed but omitted. Replacement versus addition remains unresolved, and neither establishes a supplied composite output.

**Mechanical evidence recheck:** Every protocol context occurrence and the exact SAP hierarchy, LVEF row and footnotes were matched; image-based statements were visually confirmed. The distinct quantity comparison was reproduced. Participant death/transplant/LVEF records, operational ties and net-benefit output are absent. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An extractor could equate the LVEF median difference with the planned LV-function composite, although they represent different outcomes and effect measures. No effect of this difference on trial conclusions is asserted.

## C005 — Dialysis membership differs across MACE definitions

**Pending Human Adjudication**

**Candidate statement:** Dialysis is included in the protocol/main MACE definition but omitted from the SAP and supplementary figure definition.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P, S_C

**Compared document roles:** PLAN protocol vs PLAN SAP vs REPORT main/results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-003

**Qualifying route:** Route A, category 5

**Classification rationale:** The composite definitions conflict across PLAN/REPORT (P_R), protocol/SAP PLAN/PLAN (P_P) and main/results REPORT/REPORT (S_C). P_R has precedence, giving protocol_report; all three relationships are retained.

**Classification ambiguity:** None in content roles or relationship precedence. Operational/model explanations remain bounded by the supplied evidence.

**Exact source locations:** Every repeated protocol composite occurrence: [protocol PDF p.8](../joi250087supp1_prod_1766516490.96011.pdf#page=8); [protocol PDF p.14](../joi250087supp1_prod_1766516490.96011.pdf#page=14); [protocol PDF p.15](../joi250087supp1_prod_1766516490.96011.pdf#page=15); [protocol PDF p.53](../joi250087supp1_prod_1766516490.96011.pdf#page=53); [protocol PDF p.59](../joi250087supp1_prod_1766516490.96011.pdf#page=59); [protocol PDF p.60](../joi250087supp1_prod_1766516490.96011.pdf#page=60); [protocol PDF p.99](../joi250087supp1_prod_1766516490.96011.pdf#page=99); [protocol PDF p.105](../joi250087supp1_prod_1766516490.96011.pdf#page=105); [protocol PDF p.106](../joi250087supp1_prod_1766516490.96011.pdf#page=106). SAP: [sap PDF p.4](../joi250087supp2_prod_1766516490.96511.pdf#page=4); [sap PDF p.7](../joi250087supp2_prod_1766516490.96511.pdf#page=7). Main: [main PDF p.3](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3). Results contents, component rows and figure: [results PDF p.1](../joi250087supp3_prod_1766516490.97011.pdf#page=1); [results PDF p.5](../joi250087supp3_prod_1766516490.97011.pdf#page=5); [results PDF p.6](../joi250087supp3_prod_1766516490.97011.pdf#page=6); [results PDF p.13](../joi250087supp3_prod_1766516490.97011.pdf#page=13)

**Source evidence:** Protocol and main Outcomes list death, cardiac transplantation, permanent LVAD, stroke, dialysis and heart-failure rehospitalization. Both SAP lists and the contents/eFigure 4 title list the other five components without dialysis. D30 MACE is 35/101 versus 36/104, RR 1.00 (0.69–1.46); D60 is 36/101 versus 39/104, RR 0.95 (0.66–1.36). Dialysis at D30 is 29/101 versus 38/104; D60 dialysis entries are dashes. eFigure 4 repeats MACE final events 35/36 and 36/39, log-rank P=.87/.94.

**Reported-versus-comparator:** Six-component protocol/main definition versus five-component SAP/figure definition; their set difference is dialysis.

**Reasoning procedure:** Compare each component list at every repeated location, then match the printed MACE table counts with figure copies. Do not sum components because participant overlap is unavailable. Separate composite-definition reproduction from contextual subset arithmetic.

**Calculation:** Six-member set minus five-member set = {dialysis}. A contextual placebo subset diagnostic compares dialysis 38 with MACE 36 at D30: input intervals [37.5,38.5] versus [35.5,36.5] leave gap 1 and relative gap 1/36=0.027778, at most 0.05. It does not separately qualify as a numerical discrepancy under this workflow. Composite membership is categorical and is not reconciled by rounding; no revised event count is inferred.

**Affected result or extracted value:** The composite definition attached to D30/D60 MACE counts and RRs, including whether dialysis contributes to those events.

**Why context does not resolve it:** Route A, category 5: the component definition of a prespecified composite differs. The figure title is substantive because it enumerates members, and the qualification does not rely on the small numerical subset diagnostic.

**Alternative source-grounded interpretations:** The analyzed definition may be the five-component SAP/figure version with dialysis retained in the main/protocol wording, or the analyzed composite may include dialysis with abbreviated SAP/figure lists. A different dialysis window or subset could alter the contextual diagnostic. None is specified.

**Mechanical evidence recheck:** All nine protocol lists, both SAP lists, main definition, repeated figure title and relevant table/curve counts were found and visually matched. The dialysis membership difference reproduces; actual composite coding, participant overlap/event dates and any component amendment are unavailable. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An extractor could pool a five-component and six-component MACE quantity under one label. The supplied aggregate evidence does not determine the implemented composite or quantify any changed effect.

## C006 — Planned post-arrest subgroup differs from reported predefined other-etiology subgroup

**Pending Human Adjudication**

**Candidate statement:** The plan names post-cardiac-arrest patients for subgroup analyses, whereas the report calls a broader Other-etiology subgroup predefined and supplies no separate arrest-specific primary result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol/SAP vs REPORT main Figure 3/results eTable 6/eFigure 9

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007, F-ST1-005

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN subgroup prescriptions are compared with REPORT analytic populations and prespecification statements, so P_R/protocol_report applies. A separate allocation category is a different planning function and does not itself establish a P_P conflict.

**Classification ambiguity:** None in content roles or relationship precedence. An unsupplied subgroup amendment remains possible.

**Exact source locations:** Every repeated endpoint/subgroup prescription: [protocol PDF p.8](../joi250087supp1_prod_1766516490.96011.pdf#page=8); [protocol PDF p.14](../joi250087supp1_prod_1766516490.96011.pdf#page=14); [protocol PDF p.15](../joi250087supp1_prod_1766516490.96011.pdf#page=15); [protocol PDF p.53](../joi250087supp1_prod_1766516490.96011.pdf#page=53); [protocol PDF p.59](../joi250087supp1_prod_1766516490.96011.pdf#page=59); [protocol PDF p.60](../joi250087supp1_prod_1766516490.96011.pdf#page=60); [protocol PDF p.99](../joi250087supp1_prod_1766516490.96011.pdf#page=99); [protocol PDF p.105](../joi250087supp1_prod_1766516490.96011.pdf#page=105); [protocol PDF p.106](../joi250087supp1_prod_1766516490.96011.pdf#page=106). [Protocol PDF p.107, allocation/minimization](../joi250087supp1_prod_1766516490.96011.pdf#page=107). Complete SAP boundary: [sap PDF p.1](../joi250087supp2_prod_1766516490.96511.pdf#page=1); [sap PDF p.2](../joi250087supp2_prod_1766516490.96511.pdf#page=2); [sap PDF p.3](../joi250087supp2_prod_1766516490.96511.pdf#page=3); [sap PDF p.4](../joi250087supp2_prod_1766516490.96511.pdf#page=4); [sap PDF p.5](../joi250087supp2_prod_1766516490.96511.pdf#page=5); [sap PDF p.6](../joi250087supp2_prod_1766516490.96511.pdf#page=6); [sap PDF p.7](../joi250087supp2_prod_1766516490.96511.pdf#page=7); [sap PDF p.8](../joi250087supp2_prod_1766516490.96511.pdf#page=8); [sap PDF p.9](../joi250087supp2_prod_1766516490.96511.pdf#page=9). REPORT: [main PDF p.4](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4); [main PDF p.7](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7); [results PDF p.9](../joi250087supp3_prod_1766516490.97011.pdf#page=9); [results PDF p.18](../joi250087supp3_prod_1766516490.97011.pdf#page=18)

**Source evidence:** All protocol endpoint lists name acute MI, myocarditis, post-cardiac surgery and post-cardiac arrest for primary/secondary assessments. Protocol p.107 separately uses other causes in minimization; SAP p.6 lists etiology adjustment categories but no SAP page prescribes subgroup analysis. Main methods/Figure 3 call subgroup analyses predefined/prespecified. The displayed Other subgroup has successful weaning 15/21 versus 12/21 and sHR 1.61 (0.78–3.33). eTable 6 identifies six diagnoses, with cardiac arrest 5/21 versus 1/21; eFigure 9 repeats the Other population.

**Reported-versus-comparator:** Planned post-arrest subgroup versus reported heterogeneous Other subgroup; an allocation factor is not automatically an analytic subgroup prescription.

**Reasoning procedure:** Read all repeated subgroup endpoint lists and complete SAP; distinguish randomization/minimization from analysis prescriptions. Compare the exact Other diagnosis counts, figure population and prespecification language, and search the full REPORT union for arrest-specific output.

**Calculation:** Other total=21+21=42; its arrest component=5+1=6. Half-unit summation permits Other [41,43] and arrest [5,7], gap 34, relative gap 34/42=0.809524 (>0.05). The membership difference is substantive; no arrest-specific effect is derived from the Other sHR.

**Affected result or extracted value:** The population and prespecified status attached to Other-subgroup sHR 1.61 (0.78–3.33), and the missing planned post-arrest primary subgroup output.

**Why context does not resolve it:** Route A, category 5: a reported prespecified analysis is absent from supplied analytic prescriptions, while a planned primary subgroup analysis is not reported. Six arrest patients and 42 Other patients are not interchangeable labels.

**Alternative source-grounded interpretations:** An unsupplied detailed amendment may prescribe minimization categories as analytic subgroups, or the arrest subgroup may have been broadened for reasons not documented in the package. The allocation paragraph alone does not establish such an amendment.

**Mechanical evidence recheck:** Every protocol occurrence, allocation paragraph, all nine SAP pages, main methods/figure, eTable 6 and eFigure 9 matched. Full REPORT inspection found no arrest-specific primary output. Missing dated analytic amendment and event-time/model inputs constrain explanation and numerical reconstruction. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An extractor could code the reported Other effect as the planned post-arrest subgroup effect or accept its prespecified status without the matching plan. No arrest-specific effect or reason for the population change is inferred.

## C007 — Planned adjusted key-secondary analyses lack supplied outputs

**Pending Human Adjudication**

**Candidate statement:** Explicitly planned etiology-adjusted analyses for abstract-named key secondary outcomes have no identified treatment output in the supplied reports.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol/SAP vs REPORT main/results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006, F-ST1-006

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective protocol/SAP regression prescriptions are PLAN and observed methods/displays are REPORT, yielding P_R/protocol_report. Missing key-secondary adjusted outputs form one repeated pattern; C003 separately covers missing D60 windows.

**Classification ambiguity:** None in content roles or relationship precedence. Omitted adjusted outputs or an unsupplied model revision remain possible.

**Exact source locations:** Every protocol adjusted-analysis occurrence: [protocol PDF p.35](../joi250087supp1_prod_1766516490.96011.pdf#page=35); [protocol PDF p.37](../joi250087supp1_prod_1766516490.96011.pdf#page=37); [protocol PDF p.81](../joi250087supp1_prod_1766516490.96011.pdf#page=81); [protocol PDF p.82](../joi250087supp1_prod_1766516490.96011.pdf#page=82); [protocol PDF p.83](../joi250087supp1_prod_1766516490.96011.pdf#page=83); [protocol PDF p.84](../joi250087supp1_prod_1766516490.96011.pdf#page=84); [protocol PDF p.127](../joi250087supp1_prod_1766516490.96011.pdf#page=127); [protocol PDF p.128](../joi250087supp1_prod_1766516490.96011.pdf#page=128); [protocol PDF p.129](../joi250087supp1_prod_1766516490.96011.pdf#page=129); [protocol PDF p.130](../joi250087supp1_prod_1766516490.96011.pdf#page=130). SAP model prescriptions: [sap PDF p.7](../joi250087supp2_prod_1766516490.96511.pdf#page=7); [sap PDF p.8](../joi250087supp2_prod_1766516490.96511.pdf#page=8); [sap PDF p.9](../joi250087supp2_prod_1766516490.96511.pdf#page=9). Main abstract/methods/tables: [main PDF p.1](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1); [main PDF p.4](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4); [main PDF p.6](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=6); [main PDF p.7](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=7). Results and retained contextual displays: [results PDF p.5](../joi250087supp3_prod_1766516490.97011.pdf#page=5); [results PDF p.6](../joi250087supp3_prod_1766516490.97011.pdf#page=6); [results PDF p.11](../joi250087supp3_prod_1766516490.97011.pdf#page=11); [results PDF p.13](../joi250087supp3_prod_1766516490.97011.pdf#page=13); [results PDF p.16](../joi250087supp3_prod_1766516490.97011.pdf#page=16); [results PDF p.17](../joi250087supp3_prod_1766516490.97011.pdf#page=17)

**Source evidence:** SAP p.7 prescribes etiology-adjusted Cox mortality and ICU/hospital models plus adjusted general linear ECMO-duration/free-day and organ-failure/free-day models; p.8 specifies adjusted ventilation-duration/free-day models; p.9 specifies etiology-adjusted Poisson serious-event comparisons. The abstract names mortality, ECMO-, ventilation- and organ-failure-free outcomes, ICU/hospital stay and serious adverse events. Supplied outputs include mortality RR 1.11 (0.70–1.75), ECMO difference −1 (−2 to 1), ECMO-free difference 1 (−1 to 4), ICU RMST difference −1 (−5 to 3), hospital RMST difference −7 (−12 to −2), organ-free difference −2 (−10 to 4), ventilation-free difference −0 (−3 to 2), and serious-event patients 59/101 versus 61/104 with an event-frequency histogram.

**Reported-versus-comparator:** Explicit adjusted Cox/general-linear/Poisson model prescriptions versus marginal RR, median difference, RMST contrast, any-event patient proportion or frequency displays lacking an identified adjusted secondary coefficient/output.

**Reasoning procedure:** Match each abstract-named key secondary outcome to its SAP model and inspect the complete 32-page REPORT union for the corresponding adjusted effect. Retain all protocol and checker locations while distinguishing qualifying key outcomes from non-key contextual prescriptions.

**Calculation:** Mortality: adjusted Cox versus RR/log-rank reporting. Free-day endpoints: adjusted general linear model versus marginal medians/differences. Stays: adjusted Cox versus RMST contrasts. Serious-event counts: adjusted Poisson versus patient-any-event counts/frequency histogram. Aggregate summaries cannot supply the missing treatment coefficients; no crude estimate is substituted for an adjusted effect. Numeric precision cannot create absent model outputs.

**Affected result or extracted value:** The unavailable adjusted treatment outputs for mortality, ECMO/free days, organ/ventilation-free days, ICU/hospital stays and serious adverse events named in the abstract.

**Why context does not resolve it:** Route A, category 5: explicit planned key-secondary analyses are not reported in the supplied package. Footnotes explain secondary-table P-value omission for multiplicity concerns, which does not identify adjusted coefficients or explain their omission.

**Alternative source-grounded interpretations:** Adjusted models may have been fitted but their outputs omitted, or replaced under a revision not supplied. MACE adjustment, catecholamine/RRT adjustment and nonserious/recurrent drug-reaction passages remain contextual non-key occurrences; they do not independently broaden this registered absence claim.

**Mechanical evidence recheck:** All ten protocol analysis locations and SAP pp.7/8/9 matched, along with the abstract and every identified result display. All 32 REPORT pages were checked. No adjusted key-secondary output was identified; model formulas, coefficients, input data and any removing amendment are unavailable. The [complete direct-source recheck](review_1_6_2/verification/evidence_recheck.md) and [independent audit](review_1_6_2/quality/evidence_quality_audit.md) preserve all source observations and limitations.

**Potential downstream evidence impact:** An extractor could assume a reported marginal/RMST/any-event contrast represents the prespecified adjusted model or fail to distinguish event-count and patient-risk estimands. No unreported coefficient or change in conclusions is inferred.

## Downstream Evidence-Chain Considerations

If a candidate is confirmed through human adjudication, an evidence extractor could copy a model label, composite membership, subgroup population or outcome window that differs from the intended analysis. A reported marginal contrast could also be extracted as a planned adjusted or hierarchical estimate. Keeping the exact source location, quantity and comparison together supports traceable extraction and prevents silent substitution of an unavailable result. This report does not assert that such propagation, a changed conclusion or harm occurred.

## Limitations and Missing Definitions

The review uses only the six supplied PDFs. No participant-level data, fitted model objects, bootstrap replicates or external registrations were supplied. Missing exact model formulas, operational endpoint coding, event membership/times and dated amendments prevent reconstruction of unreported outputs or identification of the implementation behind conflicting descriptions. Absence findings are confined to the complete supplied REPORT union, not to analyses performed elsewhere.

Specific missing definitions include center coding/inclusion in the primary model; treatment of SOFA score-2 and missing daily components; D60 free-day outputs; hierarchical LV-function pairwise wins/losses/ties and net-benefit output; dialysis membership/window for MACE; a dated Other-subgroup prescription and arrest-specific output; and adjusted key-secondary coefficients. KRT-duration population/zero coding, exact bootstrap/RR algorithm, interaction covariance/model degrees of freedom and the full subject-count sample-size equation also constrain mechanical diagnostics; they do not independently establish additional candidates.

Historic extraction/OCR/image engine versions and a complete historic source-to-derivative hash crosswalk are unavailable. Fresh content checks, direct-source rechecks and hash inventories support local provenance. All 194 source pages are mapped, including the three signed-image gaps; derivative limitations leave no scientific coverage gap.

Direct PDF/OCR utilities were absent. Native text and rendering used the pinned package-local PyMuPDF 1.26.4 fallback. Rendering ran on CPU. At the user's explicit request, targeted SAP pp.5–6 OCR used RapidOCR 1.4.4/onnxruntime-gpu 1.28.0 through PowerShell 5.1, requesting CUDA execution on the RTX 5070 Laptop GPU. An initial attempt shifted to CPU because of a missing library path; reruns used a process-local path to existing CUDA13/cuDNN9 libraries. CUDA use is inferred from the engine's provider verification and absence of its CPU-shift warning, rather than an affirmative per-process NVIDIA activity snapshot. OCR remained a locator; source-page visual inspection was final authority. No global Python or shared environment package installation was performed.

The temporary fallback environment is removed by the coordinator after HTML rendering and before final validation, with completion recorded in tooling_record.md. Final hash snapshots, report timing, HTML rendering and validator status are coordinator completion metadata. The actual initial CLI argument vector is unavailable; routing preflight distinguishes the required launch command from observed INTERACTIVE_CLI/CURRENT_SESSION execution. These constraints do not change the bounded scientific comparisons or confer human adjudication.

The standalone [limitations record](review_1_6_2/limitations.md) preserves these boundaries.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

Routing preflight reports PASS; run model gpt-6.1-sol, source DEFAULT; execution INTERACTIVE_CLI; provider CURRENT_SESSION; all ten named presets verified. Every mandatory specialist stage uses a fresh distinct runtime ID, and both statistical passes use different high-effort agents. Additional shards reflect bounded evidence scopes. No provider credentials are recorded.

Before-review identities are preserved in [source hashes](review_1_6_2/source_hashes_before.sha256) and [reused-asset hashes](review_1_6_2/reused_artifact_hashes_before.sha256). The audit's independent snapshot matched all six sources and 116 reusable artifacts. Final direct sha256sum recomputation matches both before inventories byte for byte: all six sources and 116 inventoried existing assets are unchanged. [Source after hashes](review_1_6_2/source_hashes_after.sha256), [asset after hashes](review_1_6_2/reused_artifact_hashes_after.sha256) and the [integrity record](review_1_6_2/integrity_record.md) preserve that closure. Final validation is recorded in review_validation.json. No source or reused asset was modified. Derivative engines/device details and temporary-environment removal are recorded in [tooling record](review_1_6_2/tooling_record.md) and [GPU OCR engine record](review_1_6_2/preprocessing/gpu_ocr/engine_record.md).

### Agent execution

All 21 actual agents, including the coordinator once, appear below. Runtime canonical task IDs omit their leading slash, matching the execution manifest.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12c36-c3f5-7e80-904c-40dfa4343c9d | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_inventory | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapping | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_protocol_001 | root/protocol_mapping_001 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001.md |
| support_protocol_002 | root/protocol_mapping_002 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_002.md |
| support_protocol_003 | root/protocol_mapping_003 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_003.md |
| numeric_consistency_reviewer | root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_support_checker | root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_remaining_checker | root/cross_source_remaining | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/cross_source_remaining.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| inclusion_screener | root/inclusion_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| audit_mapping_main_protocol | root/audit_mapping_main_protocol | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_main_protocol.md |
| audit_mapping_support | root/audit_mapping_support | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_support.md |
| audit_cross_relationships | root/audit_cross_relationships | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/cross_source_audit.md |
| audit_statistical_relationships | root/audit_statistical_relationships | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/statistical_audit.md |
| statistics_pass_2 | root/statistics_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_control_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generation | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Primary artifact paths in the execution table are relative to review_1_6_2/. The [execution manifest](review_1_6_2/agent_execution_manifest.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) retain exact ownership and all shard parts. Full quantitative maps and checker artifacts are preserved without a ranked subset or a candidate cap.

### Reproducibility performance

- **Target basis:** Six PDF sources provide 194 unique pages, including a 153-page multi-version protocol with approximately 550000 text characters requiring three bounded mapping shards, a nine-page scanned SAP with reusable images but usable OCR only on four pages, 28 main/results pages with native text and visual evidence, and four administrative pages. Reuse covers191 units; three protocol image pages require fresh visual inspection (pp.4,49 initially and p.95 identified and closed during coverage audit). Native PDF fallback is ready, direct OCR tools are absent, and visual tables plus distinct mapping, checker, screening, recheck, second-statistical-pass, audit, and report waves determine a package-specific 50-85 minute planning range.
- **Total source units:** 194
- **Fresh-source units:** 3
- **Target elapsed minutes:** 50-85
- **Started UTC:** 2026-10-11T18:30:06Z
- **Finished UTC:** 2026-10-11T19:42:03Z
- **Observed elapsed minutes:** 72.0
- **Target status:** MET_TARGET
- **Exceedance causes:** None

Observed review duration ends at complete Markdown assembly. Local rendering and mechanical validation are outside that window. The package-specific planning target does not limit coverage or the candidate set. Final performance fields are completed by the coordinator immediately after assembly.
