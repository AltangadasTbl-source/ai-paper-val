# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

> **Pending Human Adjudication.** Every candidate in this report requires human review. Classification, mechanical reproduction and inclusion-audit fields describe review records and do not adjudicate a candidate or the paper.

## Executive Quality-Control Summary

The complete supplied package contains **10 stable candidates**, C001–C010. Nine inclusion audits are CONFIRMED and C001 is QUESTIONED because its immediate six-hour context may resolve the oxygenation attribution. All ten evidence states are reproduced; all ten retain Pending Human Adjudication. The candidates comprise one statistical-results comparison, one report-internal attribution comparison and eight planned-versus-reported comparisons. No candidate was omitted after stable-ID assignment.

The review concerns quantitative reporting consistency and the result or annotation that a reader could extract. It establishes neither a paper-level conclusion change nor actual downstream propagation. Positive plan/report specification differences do not establish that a planned analysis was replaced or never performed.

## Package and Reused-Evidence Provenance

The supplied package is the HIGH randomized trial article and three PDF supplements. Document roles follow content: the 129-page bound protocol/SAP is PLAN; the article, results supplement and publication data-sharing statement are REPORT. The source PDFs remain authoritative.

| Source ID | Actual supplied filename | Role | PDF pages | Reusable-backed | Fresh-required | Mapped |
|---|---|---|---:|---:|---:|---:|
| DOC-001 | [jama_azoulay_2018_oi_180109.pdf](<../jama_azoulay_2018_oi_180109.pdf#page=1>) | REPORT | 9 | 9 | 0 | 9 |
| DOC-002 | [joi180109supp1_prod.pdf](<../joi180109supp1_prod.pdf#page=1>) | PLAN | 129 | 129 | 0 | 129 |
| DOC-003 | [joi180109supp2_prod.pdf](<../joi180109supp2_prod.pdf#page=1>) | REPORT | 5 | 5 | 0 | 5 |
| DOC-004 | [joi180109supp3_prod.pdf](<../joi180109supp3_prod.pdf#page=1>) | REPORT | 1 | 1 | 0 | 1 |
| Total | Four PDFs | | 144 | 144 | 0 | 144 |

The inventory records 396 reused evidence assets: 381 USABLE, 7 PARTIAL and 8 DUPLICATE. Overlapping usable native/layout assets cover every source page. Thirty-six fresh confirmation derivatives supplement reuse; these do not change the zero fresh-required source-unit count. The evidence-asset inventory therefore has 432 entries. Every page was checked against current-source extraction: 143 native byte matches and one whitespace-only match; four layout variations concern wrapping or figure-label placement. Earlier scientific selections and adjudication records supplied no discovery boundary.

Provenance is documented in [source inventory](review_1_6_1/source_inventory.md), [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md), and [reused-asset hash record](review_1_6_1/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

All **144/144 physical PDF pages** were scientifically mapped, including covers, references, administrative pages and historical background. Reusable plus fresh-required units partition each source total, and mapped units equal total units for every source. The main mapping contains 109 evidence groups; four disjoint support mappings contain 152 groups (13, 56, 36 and 47). Groups are evidence organization units, not candidate counts. See [source coverage](review_1_6_1/source_coverage.md), [coverage manifest](review_1_6_1/coverage_manifest.md), [main map](review_1_6_1/extraction/main_quantitative_evidence.md), and [support map](review_1_6_1/extraction/support_quantitative_evidence.md).

Scope covered counts and denominators, estimate/test logic, statistical method logic, and planned-versus-reported statistical design under QUALITY_CONTROL_SCOPE.md. Display precision, immediately resolved wording or notation, model-versus-crude comparisons, conditional numerical diagnostics, peripheral comparisons and out-of-focus observations were excluded through the specified screening rules. No raw-data, clinical, novelty, misconduct or broad study-design audit was undertaken, and no preferred analysis is proposed.

## Quantitative and Statistical Relationship Coverage

The rebuilt inventory contains **96 numeric relationships** and **90 statistical relationships**. All were audited. Distinct fresh gpt-6.1-sol/high agents completed statistical pass 1 and pass 2 on all 90 statistical records, with PASS_1_COMPLETE and PASS_2_COMPLETE coverage. Pass 2 used the full ledger, screening log and exact-source recheck and emitted no new finding; a second inclusion-screen stage was therefore not applicable.

Coverage includes participant flow, counts/denominators, interval ordering and estimate containment, source-established test and interval compatibility, matched result/reference direction, analysis/model/population definitions, plan versions, primary/key-secondary analysis promises, sample-size and decision-rule context. Where a numerical reconstruction required an unreported algorithm, model, variance or event-time input, the missing input was retained as a limitation rather than assumed.

See [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_1/statistics/relationship_inventory.md), [pass 1](review_1_6_1/checkers/statistical_pass_1.md), [pass 2](review_1_6_1/checkers/statistical_pass_2.md), and [quality audit](review_1_6_1/quality/evidence_quality_audit.md).

## Inclusion Screening Summary

The independent inclusion screen considered **19 finding rows**: **10 INCLUDE** rows forming ten distinct stable candidates and **9 SCREENED_OUT** rows. Inclusion required source reproduction, focus, absence of immediate contextual resolution and a named interpretation/extraction consequence. Audit subsequently questioned C001’s immediate-context criterion; the stable ID and its original screening decision remain visible.

| Decision | Reason code | Finding rows |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 10 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 7 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 1 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| Total | | 19 |

Separately, checker self-screening recorded **76 excluded-observation groups**: numeric 13, cross-source 21, statistical pass 1 28 and pass 2 14. These groups were audited in both directions and are not added to the 19 screened findings. No new qualifying audit finding or screening reversal was identified. See the [single screening log](review_1_6_1/screening/inclusion_screen.md).

## Review-Domain Summary

| Review domain | Meaning | Stable candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests and statistical methods in REPORT materials | 1 |
| report_internal_inconsistency | REPORT attribution of an outcome, time, population or comparison | 1 |
| protocol_report | REPORT differs from PLAN in a statistical design/analysis element | 8 |
| plan_material | A statistical-design inconsistency solely within PLAN material | 0 |
| Total | | 10 |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| S_W | Within one REPORT document | 1 |
| S_C | Between different REPORT documents | 1 |
| P_R | REPORT versus PLAN | 8 |
| P_P | Solely within PLAN | 0 |
| Total | | 10 |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 10 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 10 |

Primary relationship counts apply precedence P_R > P_P > S_C > S_W. C001 also involves S_W, and C006 also involves S_W; these additional relationships do not add candidates. Inclusion-audit counts are CONFIRMED 9 and QUESTIONED 1. Classifications are copied from the [candidate ledger](review_1_6_1/candidate_ledger.md).

## Candidate Index

| Stable ID and candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| C001 — Oxygenation result time and population attribution | report_internal_inconsistency | S_C | reproduced | QUESTIONED |
| C002 — Forest-plot HR reference and favor direction | statistical_results | S_W | reproduced | CONFIRMED |
| C003 — Planned longitudinal joint models and reported rank comparisons | protocol_report | P_R | reproduced | CONFIRMED |
| C004 — Infection competing-risk plan and reported proportion test | protocol_report | P_R | reproduced | CONFIRMED |
| C005 — ICU-stay analysis specification | protocol_report | P_R | reproduced | CONFIRMED |
| C006 — Prospective and displayed subgroup boundaries | protocol_report | P_R | reproduced | CONFIRMED |
| C007 — Primary relative-risk plan and reported hazard ratio | protocol_report | P_R | reproduced | CONFIRMED |
| C008 — Planned covariate adjustment and explicit univariable models | protocol_report | P_R | reproduced | CONFIRMED |
| C009 — Comparator rescue-HFNO permission | protocol_report | P_R | reproduced | CONFIRMED |
| C010 — Prespecified per-protocol primary result unavailable | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

Every card below is **Pending Human Adjudication**. Stable-ID order follows source order and does not imply a ranking.

## C001 — Oxygenation result time and population attribution

**Status:** Pending Human Adjudication

**Candidate statement:** The abstract defines oxygenation over three days after intubation, while its descriptive pair matches the six-hour-after-randomization supplementary table. The attribution question requires qualification because the same abstract results sentence also provides a six-hour cue.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main article pp.1,6 vs REPORT results supplement pp.2,4

**Evidence state:** reproduced

**Inclusion audit:** QUESTIONED

The auditor’s reason: the abstract’s same coordinated results sentence places higher oxygenation and lower respiratory rate after six hours, and the supplementary table confirms six hours after randomization. This immediate-context reading may resolve attribution at once; missing model details do not independently meet the threshold.

**Finding IDs:** F-XS-001

**Classification rationale:** Two REPORT documents conflict, with an additional within-main comparison; P_R is absent because PLAN does not conflict.

**Classification ambiguity:** Oxygenation contrast's precise measurement window and model remain unspecified; direct recheck must preserve this limitation.

**Exact source locations:** REPORT [main abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), [secondary results p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>); REPORT [results eTable p.2 — joi180109supp2_prod.pdf, PDF p. 2](<../joi180109supp2_prod.pdf#page=2>), [eFigure2 p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>). PLAN p.103 is corroboration only, and does not state after intubation.

Complete confirmed physical-page locations: [main abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>); [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>); [eTable, PDF p.2 — joi180109supp2_prod.pdf, PDF p. 2](<../joi180109supp2_prod.pdf#page=2>); [eFigure 2 panel B, PDF p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>); [secondary-endpoint definition, PDF p.103, lines 1694–1697 — joi180109supp1_prod.pdf, PDF p. 103](<../joi180109supp1_prod.pdf#page=103>).

**Source evidence:** REPORT [main abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>) lists PaO2:FIO2 over the three days after intubation, then reports 150 versus 119 and difference 19.5 (95% CI 4.4 to 34.6). Its results sentence also places lower respiratory rate after six hours. REPORT [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>) says PaO2:FIO2 was higher until day 4, prints the same 150/119 and mean difference 19.5 (4.4 to 34.6), and points to eFigure 2 and the eTable.

Yes. REPORT [eTable, PDF p.2 — joi180109supp2_prod.pdf, PDF p. 2](<../joi180109supp2_prod.pdf#page=2>) explicitly titles oxygenation and ventilation six hours after randomization and labels the PaO2/FiO2 row six hours after randomization: medians 150 [104–230] and 119 [86–165]. REPORT [eFigure 2 panel B, PDF p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>) uses Randomization, H6 and Day 1 through Day 7 on its time axis. Its printed contributor rows were read; no plotted coordinate was converted into an exact estimate. Corroborating PLAN [secondary-endpoint definition, PDF p.103, lines 1694–1697 — joi180109supp1_prod.pdf, PDF p. 103](<../joi180109supp1_prod.pdf#page=103>) says PaO2/FiO2 from day 1 to day 3 and does not attach an after-intubation qualifier.

**Reported-versus-comparator:** Abstract outcome window says three days after intubation; report gives 150 versus 119, mean difference 19.5 (95% CI 4.4–34.6). The eTable labels 150 [104–230] versus 119 [86–165] as six hours after randomization; eFigure 2 time axis is randomization-based.

**Reasoning procedure:** Match the descriptive pair before comparing the named window and population; do not equate medians with mean differences. matched-result attribution under focus B/C: the same displayed descriptive pair and associated contrast require an identifiable time origin, window and population. This is not a median-minus-median versus mean-difference calculation.

**Calculation:** The 150/119 pair and 19.5 (4.4–34.6) tuple match exactly between the two main occurrences; the pair also matches the specifically six-hour supplementary table. Integer display ranges are [149.5,150.5) and [118.5,119.5); the mean-difference range is [19.45,19.55), with endpoint ranges [4.35,4.45) and [34.55,34.65). These shared ranges establish numerical matching but cannot make postintubation and randomization-based windows the same. No difference of the two medians is used to test 19.5.

**Affected result or extracted value:** Time and population attribution of the abstract oxygenation result 150/119 and 19.5 (4.4–34.6).

**Why context does not resolve it:** Registration identified different explicit endpoint-definition and table windows. The final audit questions this criterion: the abstract's same coordinated results sentence places the higher oxygenation and lower respiratory-rate comparison after six hours, and the matching eTable expressly labels six hours after randomization. This immediate-context reading may resolve result attribution at once; unreported oxygenation-model details do not independently qualify.

**Alternative source-grounded interpretations:** The abstract's six-hour clause and the eTable support a six-hour randomized-arm descriptive comparison; the postintubation endpoint description could refer to another intended trajectory. The p.6 until-day-4 wording could refer to the broader trajectory. The sources do not explicitly assign the single mean contrast to one of these possibilities.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: the directly read postintubation outcome description and the directly read six-hour/randomization labels remain different for the matched descriptive result.

Necessary inputs available: Exact textual definitions, numeric tuple, supplementary table labels and figure time axis. **Exact missing inputs or definitions:** The measurement population, time origin/window and fitted analysis yielding 19.5; whether that contrast is pointwise or longitudinal; an explicit connection to the abstract's postintubation endpoint. An intubated-only denominator is not supplied for this tuple.

Direct observation and inferred explanation: The different time labels and matching printed pair are observed. Attribution to a distinct postintubation analysis, or an explanation based on how the abstract was composed, would be inference and is not established.

Checker provenance: Cross-source G01; duplicate F-ST1-009. Statistical relationships S007, S032, S033.

**Potential downstream evidence impact:** If the attribution concern is confirmed, an extractor could attach the oxygenation pair and contrast to a different time origin or population. The six-hour immediate-context reading may instead resolve that annotation. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which time origin, measurement window, population and analysis generated 150 versus 119 and mean difference 19.5 (4.4–34.6), and how does that result correspond to the abstract endpoint definition? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Forest-plot HR reference and favor direction

**Status:** Pending Human Adjudication

**Candidate statement:** Matched overall mortality and ventilation populations have HRs beyond display precision in opposite numerical orientations in Table 2 and Figure 3, without a stated reconciliation of the forest reference and favor labels.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article pp.1,4,5,6 vs REPORT main article Figure3 p.7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Classification rationale:** Conflicting effect and label locations are within one REPORT document; S_W/statistical_results.

**Classification ambiguity:** Exact fitted-model reference coding unavailable; no claim that every subgroup estimate is a crude ratio.

**Exact source locations:** REPORT [abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), [subgroup methods p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [Table2 p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), [results p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), [Figure3 p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>). Affected pattern: both panels, both all-patient rows, all24 subgroup rows, and both favor-label pairs; every tuple retained in main map M084–M109 and S039–S064.

Complete confirmed physical-page locations: [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>); [Table 2/primary results, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>); [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>); [subgroup methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [Figure 3, PDF p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>).

All 26 affected Figure 3 rows are listed below. H denotes HFNO and S standard oxygen; each row links its exact source page. Both panel A and panel B favor-label pairs are at [Figure 3 panel A labels — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) and [Figure 3 panel B labels — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>). IMV denotes invasive mechanical ventilation.

| Exact Figure 3 occurrence | H event/total | S event/total | Printed HR (95% CI) | Printed interaction P for pair |
|---|---:|---:|---|---|
| [A mortality, ICU admission 0–1 days — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 120/321 | 118/330 | 0.95 (0.74–1.22) | .15 |
| [A mortality, ICU admission ≥2 days — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 18/67 | 22/58 | 1.55 (0.83–2.90) | .15 |
| [A mortality, PaO2:FIO2 <200 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 99/237 | 95/251 | 0.89 (0.68–1.19) | .52 |
| [A mortality, PaO2:FIO2 ≥200 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 16/65 | 10/35 | 1.18 (0.54–2.60) | .52 |
| [A mortality, oxygen flow ≤9 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 122/348 | 127/347 | 1.06 (0.83–1.36) | .39 |
| [A mortality, oxygen flow >9 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 16/40 | 13/41 | 0.76 (0.36–1.57) | .39 |
| [A mortality, catecholamines No — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 121/355 | 126/349 | 1.08 (0.84–1.39) | .15 |
| [A mortality, catecholamines Yes — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 17/33 | 14/39 | 0.62 (0.31–1.26) | .15 |
| [A mortality, unknown diagnosis No — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 99/297 | 95/303 | 0.93 (0.70–1.23) | .12 |
| [A mortality, unknown diagnosis Yes — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 39/91 | 45/85 | 1.39 (0.90–2.13) | .12 |
| [A mortality, hematologic malignancy No — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 66/199 | 72/198 | 1.11 (0.79–1.55) | .5 |
| [A mortality, hematologic malignancy Yes — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 64/167 | 65/181 | 0.94 (0.67–1.33) | .5 |
| [A mortality, All patients — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 138/388 | 140/388 | 1.02 (0.81–1.29) | — |
| [B IMV, ICU admission 0–1 days — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 128/321 | 142/330 | 1.1 (0.87–1.40) | .17 |
| [B IMV, ICU admission ≥2 days — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 22/67 | 28/58 | 1.69 (0.96–2.95) | .17 |
| [B IMV, PaO2:FIO2 <200 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 99/237 | 117/251 | 1.17 (0.90–1.53) | .44 |
| [B IMV, PaO2:FIO2 ≥200 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 27/65 | 13/35 | 0.88 (0.46–1.71) | .44 |
| [B IMV, oxygen flow ≤9 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 136/348 | 151/347 | 1.15 (0.91–1.45) | .65 |
| [B IMV, oxygen flow >9 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 14/40 | 19/41 | 1.37 (0.68–2.72) | .65 |
| [B IMV, catecholamines No — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 137/355 | 154/349 | 1.18 (0.94–1.49) | .83 |
| [B IMV, catecholamines Yes — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 13/33 | 16/39 | 1.09 (0.52–2.26) | .83 |
| [B IMV, unknown diagnosis No — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 114/297 | 135/303 | 1.18 (0.92–1.52) | .9 |
| [B IMV, unknown diagnosis Yes — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 36/91 | 35/85 | 1.15 (0.72–1.82) | .9 |
| [B IMV, hematologic malignancy No — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 61/199 | 89/198 | 1.61 (1.16–2.23) | .01 |
| [B IMV, hematologic malignancy Yes — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 78/167 | 77/181 | 0.89 (0.65–1.22) | .01 |
| [B IMV, All patients — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) | 150/388 | 170/388 | 1.17 (0.94–1.46) | — |

**Source evidence:** REPORT [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>) and [Table 2/primary results, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>) print day-28 mortality HR 0.98 (0.77–1.24), with 138/388 HFNO and 140/388 standard oxygen. Table 2 and REPORT [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>) print ventilation HR 0.85 (0.68–1.06), with 150/388 and 170/388. REPORT [subgroup methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>) describes HFNO versus standard effects as Cox HRs displayed in forests; it does not name a reversed reference in Figure 3.

Yes. The direct render and native text of REPORT [Figure 3, PDF p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) confirm both favor-label pairs: values below 1 sit under Favors High-Flow Nasal Oxygen Therapy; above 1 under Favors Standard Oxygen Therapy. Both all-patient rows and all 24 subgroup rows are enumerated below. Each row is at that same exact PDF page, in the named panel/subset; H and S mean the printed HFNO and standard columns. Affected subgroup direction interpretations share the unresolved reference convention; no independently printed comparator HR is claimed for each subgroup.

**Reported-versus-comparator:** Table mortality 138/388 versus 140/388, HR 0.98 (0.77–1.24); forest same counts, HR 1.02 (0.81–1.29). Table ventilation 150/388 versus 170/388, HR 0.85 (0.68–1.06); forest same counts, HR 1.17 (0.94–1.46). Below 1 favors HFNO and above 1 favors standard in both forest panels.

**Reasoning procedure:** Compare matched model-based all-patient HRs and forest reference/favor labels; crude risk ratios are not the proof. matched model-based all-patient estimates should reconcile under their identified contrast, and the favor convention must identify which intervention has lower hazard. Event counts identify matched outcomes/populations; a crude count ratio is not the comparator.

**Calculation:** Mortality HR 0.98 allows [0.975,0.985), versus forest 1.02 allowing [1.015,1.025); these do not overlap. Ventilation HR 0.85 allows [0.845,0.855), versus forest 1.17 allowing [1.165,1.175); these do not overlap. Reciprocal diagnostics are 1/0.98 = 1.020408 and 1/0.85 = 1.176471. Allowing the table estimates' full rounding ranges gives inverse ranges approximately (1.015228,1.025641] and (1.169591,1.183432], which intersect the forest ranges. Thus reciprocal coding is compatible even though exact inversion of displayed 0.85 alone rounds to 1.18. This is a diagnostic, not confirmation of fitted-model reference coding. Reading every subgroup HR/CI and the shared favor labels confirms the scope of the reference question; no subgroup arithmetic contradiction is inferred from its crude events.

For every two-decimal subgroup HR/CI entry in the table above, the display interval is [x−.005,x+.005); the explicitly one-decimal HR 1.1 has [1.05,1.15). Two-decimal interaction P values use the same .005 half-unit; .5 and .9 use .05. These intervals preserve the printed quantities without inferring exact model output. For the nonhematologic IMV row, HR 1.61 allows [1.605,1.615) and its lower CI 1.16 allows [1.155,1.165), still above 1. That establishes the row's numerical side of the printed favor convention, not the unprinted model reference.

**Affected result or extracted value:** Mortality/ventilation HR reference group, including nonhematologic ventilation HR 1.61 (1.16–2.23), and all forest-row favor interpretations.

**Why context does not resolve it:** Neither caption nor methods identifies a reversal explaining the simultaneous effect and favor conventions.

**Alternative source-grounded interpretations:** Figure 3 may use standard-versus-HFNO reference coding whereas Table 2 uses HFNO-versus-standard; different model construction is another possibility. The reciprocal ranges support the first possibility, but the caption/methods do not establish it or reconcile the favor labels.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: matched overall rows carry HRs beyond display precision in opposite numerical orientations, with the same printed favor convention and no stated reference reconciliation.

Necessary inputs available: Matched all-patient counts, HRs/intervals, model descriptions and rendered favor labels. **Exact missing inputs or definitions:** Figure 3 treatment/reference coding and model specification; explicit explanation of how its overall HRs relate to Table 2; unrounded fitted estimates and event times.

Direct observation and inferred explanation: The two nonoverlapping overall HR displays and both label placements are directly observed. Inversion of coding, reversal of all subgroup effects or a specific mechanism is inferred and remains unestablished.

Checker provenance: Cross-source G02; duplicate F-ST1-001. Statistical relationships S012, S018, S039 through S076.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an overall or subgroup HR with an unresolved intervention reference or favor annotation, including the nonhematologic ventilation row. No reversal of every fitted subgroup estimate is established. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which treatment/reference coding and favor direction apply to both Figure 3 panels and every subgroup HR, and how do the two overall HRs relate to Table 2? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Planned longitudinal joint models and reported rank comparisons

**Status:** Pending Human Adjudication

**Candidate statement:** The plan prescribes joint longitudinal models accounting for right censoring, while the report explicitly specifies Wilcoxon rank-sum comparisons for comfort and dyspnea.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p.55 and SAP pp.82,105 vs REPORT main article pp.1,4,6 and results supplement pp.4,5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Classification rationale:** PLAN versus REPORT model specification; P_R/protocol_report. Oxygenation is contextual because its actual reported model is not specified.

**Classification ambiguity:** No independent claim that an oxygenation joint model was replaced; pointwise contributor-count differences are excluded.

**Exact source locations:** PLAN [protocol p.55 lines825–826 — joi180109supp1_prod.pdf, PDF p. 55](<../joi180109supp1_prod.pdf#page=55>), [original SAP p.82 lines1314–1315 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>), [final SAP p.105 lines1745–1747 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); REPORT [abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), [methods p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [results p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), [eFigure2 p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>), [eFigure3 p.5 — joi180109supp2_prod.pdf, PDF p. 5](<../joi180109supp2_prod.pdf#page=5>).

Complete confirmed physical-page locations: [protocol, PDF p.55, lines 825–826 — joi180109supp1_prod.pdf, PDF p. 55](<../joi180109supp1_prod.pdf#page=55>); [original SAP, PDF p.82, lines 1314–1315 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>); [final SAP, PDF p.105, lines 1745–1747 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>); [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>); [eFigure 3 panels A/B, PDF p.5 — joi180109supp2_prod.pdf, PDF p. 5](<../joi180109supp2_prod.pdf#page=5>); [eFigure 2 panels A/B, PDF p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>).

**Source evidence:** PLAN [protocol, PDF p.55, lines 825–826 — joi180109supp1_prod.pdf, PDF p. 55](<../joi180109supp1_prod.pdf#page=55>), [original SAP, PDF p.82, lines 1314–1315 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>) and [final SAP, PDF p.105, lines 1745–1747 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>) all prescribe joint models accounting for right censoring for longitudinal oxygenation, dyspnea and comfort.

Yes. REPORT [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>) explicitly chooses Wilcoxon rank-sum for visual analog comfort/dyspnea scores. REPORT [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>) reports no difference in comfort/dyspnea; REPORT [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>) says neither differs at any time. REPORT [eFigure 3 panels A/B, PDF p.5 — joi180109supp2_prod.pdf, PDF p. 5](<../joi180109supp2_prod.pdf#page=5>) displays comfort/dyspnea at Randomization, H6 and Day 1 through Day 7, with contributor rows. REPORT [eFigure 2 panels A/B, PDF p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>) supplies respiratory-rate/oxygenation context. Both supplementary pages were visually confirmed without reading exact estimates from coordinates.

**Reported-versus-comparator:** Joint models taking account of right censoring are planned for oxygenation, dyspnea and comfort; report names Wilcoxon rank-sum for comfort/dyspnea and no differences at any time.

**Reasoning procedure:** Compare explicitly named analytical methods and the secondary conclusions they support, preserving final-plan version context. focus D compares a prospective repeated-outcome analysis with the explicitly reported analysis supporting the abstract-reported comfort/dyspnea conclusion.

**Calculation:** Joint longitudinal models accounting for right censoring and rank-sum comparisons are different named analytical procedures. This is a textual method comparison, with no numeric half-unit input able to reconcile the two specifications. No exact graph effect, variance or test P was inferred. Absence of a reported oxygenation model does not positively establish replacement of its planned joint model.

**Affected result or extracted value:** Abstract-reported comfort/dyspnea treatment conclusions and their analytical basis.

**Why context does not resolve it:** The explicit rank-sum description does not explain the relationship to the final joint-model prescription.

**Alternative source-grounded interpretations:** Rank-sum comparisons could have replaced the planned models, or both analyses could have been performed with only rank-based conclusions identifiable in the supplied report.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: the final plan explicitly promises joint comfort/dyspnea models while the report explicitly names rank-sum comparisons for these outcomes.

Necessary inputs available: Three prospective method statements, explicit comfort/dyspnea report method, conclusion and longitudinal displays. **Exact missing inputs or definitions:** Actual fitted comfort/dyspnea joint-model results, if any; how censoring was implemented; whether rank-sum conclusions were pointwise, combined or supplementary to other analyses; actual reported oxygenation model.

Direct observation and inferred explanation: The named method difference is observed for comfort and dyspnea. Replacement of oxygenation analysis, a specific censoring mechanism, or an explanation for changing contributors would be inference and is not asserted.

Checker provenance: Cross-source G05; duplicate F-ST1-004. Statistical relationships S034–S036.

**Potential downstream evidence impact:** If confirmed, evidence extraction could annotate the comfort/dyspnea conclusions as joint longitudinal/censoring results or as rank-based comparisons without an identified connection between them. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which analyses generated the comfort/dyspnea conclusions, and how do the reported rank-sum comparisons relate to the planned joint models and their censoring provision? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Infection competing-risk plan and reported proportion test

**Status:** Pending Human Adjudication

**Candidate statement:** The planned infection cumulative-incidence/Gray comparison differs from the explicitly reported comparison of proportions by chi-square.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp.82,105 vs REPORT main article pp.1,4,5,6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Classification rationale:** PLAN versus REPORT analytical specification; P_R/protocol_report.

**Classification ambiguity:** Infection model adjustment and HR interval algorithm are not established; no separate variance contradiction is claimed.

**Exact source locations:** PLAN [original SAP p.82 lines1305–1310 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>), [final SAP p.105 lines1738–1742 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); REPORT [abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), [methods p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [Table2 p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), [results p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>).

Complete confirmed physical-page locations: [original SAP, PDF p.82, lines 1305–1310 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>); [final SAP, PDF p.105, lines 1738–1742 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>); [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>); [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>).

**Source evidence:** PLAN [original SAP, PDF p.82, lines 1305–1310 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>) and [final SAP, PDF p.105, lines 1738–1742 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>) explicitly include ICU-acquired infection among competing-risk endpoints, prescribe cumulative incidences with death or discharge alive from ICU competing, Gray comparison, and potential-confounder adjustment using cause-specific Cox models.

Yes. REPORT [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>) explicitly compares infection proportions by chi-square. REPORT [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>) prints 39/388 versus 41/388, 10.0% versus 10.6%, risk difference −0.6% (−4.6 to 4.1), cause-specific HR 1.01 (0.96–1.06) and P=.91. REPORT [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>) and [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>) repeat the infection percentages/absolute difference and no-significant-difference conclusion. Table 2 footnote d explicitly labels the HR cause-specific.

**Reported-versus-comparator:** Plan death or alive ICU discharge competing with infection, Gray test and adjusted cause-specific Cox; report proportions/chi-square,39/388 vs 41/388, RD−.6% (−4.6,4.1), cause-specific HR 1.01 (.96,1.06), P=.91.

**Reasoning procedure:** Compare planned estimator/test to explicit reported test, without deriving a Cox interval from crude counts. focus D requires the estimator/test of the abstract-reported infection comparison to be identifiable against the final analytical specification.

**Calculation:** Planned cumulative-incidence/Gray comparison versus reported proportions/chi-square is a positive method difference. Display ranges for the contextual RD −0.6%, CI −4.6% to 4.1%, HR 1.01 and P=.91 are respectively [−0.65,−0.55), [−4.65,−4.55), [4.05,4.15), [1.005,1.015) and [.905,.915). Allowing every such range does not change the named procedures. No variance reconstruction from crude events, HR-versus-risk-ratio comparison or independent P-value contradiction is claimed.

**Affected result or extracted value:** ICU-acquired infection treatment comparison and attribution of its RD, HR and P value.

**Why context does not resolve it:** The reported cause-specific HR does not identify the planned cumulative-incidence/Gray result or reconcile the explicit proportion-test description.

**Alternative source-grounded interpretations:** A proportion comparison could have replaced the planned competing-risk test; both could have been run but only the proportion comparison is identifiable. The printed cause-specific HR suggests an additional time-to-event component but does not identify a Gray comparison.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: explicit final-plan cumulative-incidence/Gray and explicit reported infection proportion/chi-square statements remain different.

Necessary inputs available: Prospective competing events/test, explicit report test, endpoint counts and estimate/test labels. **Exact missing inputs or definitions:** Event times, cumulative-incidence estimate and Gray result for infection, actual cause-specific HR model/adjustment and interval algorithm, and an explicit mapping of each reported effect/P to its analysis.

Direct observation and inferred explanation: Named estimator/test specifications differ directly. Which unreported models were run, why the framework changed, or how the HR interval was generated remains inference.

Checker provenance: Cross-source G06; duplicate F-ST1-007. Statistical relationships S022–S024.

**Potential downstream evidence impact:** If confirmed, an extractor could attach a cumulative-incidence/Gray or proportions/chi-square analysis designation to the infection RD, HR or P value without a supplied mapping. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which infection estimator, competing events and comparison test generated the reported RD, cause-specific HR and P=.91, and where is their relationship to the planned analysis specified? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — ICU-stay analysis specification

**Status:** Pending Human Adjudication

**Candidate statement:** The planned ICU-stay survival/competing-risk procedures and overall plus survivor/death-separated populations differ from the reported pooled rank-sum comparison.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp.82,105 vs REPORT main article pp.1,4,5,6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Classification rationale:** PLAN versus REPORT analytical specification; P_R/protocol_report.

**Classification ambiguity:** Plan former/latter phrase does not identify every event coding; preserve without choosing one.

**Exact source locations:** PLAN [original SAP p.82 lines1311–1313 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>), [final SAP p.105 lines1742–1745 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); REPORT [abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), [methods p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [Table2 p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), [results p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>).

Complete confirmed physical-page locations: [original SAP, PDF p.82, lines 1311–1313 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>); [final SAP, PDF p.105, lines 1742–1745 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>); [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>); [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>).

**Source evidence:** PLAN [original SAP, PDF p.82, lines 1311–1313 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>) and [final SAP, PDF p.105, lines 1742–1745 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>) prescribe ICU-stay analysis overall and separately in survivors/dead patients, using the former/latter Kaplan–Meier and competing-risk wording. That wording was preserved without assigning unprinted event coding.

Yes. REPORT [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>) chooses Wilcoxon rank-sum for ICU length of stay. REPORT [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>) presents both 388-person groups, medians 8 [4–14] versus 6 [4–13] days, mean difference 0.6 days (−1.0 to 2.2), P=.07; footnote b says quantitative-outcome differences are differences in means. REPORT [abstract, PDF p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>) and [secondary results, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>) repeat the 8/6-day summaries, 0.6-day contrast and lack of a significant difference. They identify no survivor/death-separated ICU-stay results.

**Reported-versus-comparator:** Plan ICU stay overall and separately in survivors/dead using Kaplan–Meier/competing-risk estimators, preserving former/latter wording. Report Wilcoxon rank-sum, medians 8 vs 6 days, mean difference.6 days (−1.0,2.2), P=.07.

**Reasoning procedure:** Compare method and population specifications; median difference 2 days is not equated with mean difference.6 days. focus D compares planned estimator/populations with the explicitly reported pooled rank-sum comparison for this abstract-reported outcome.

**Calculation:** Kaplan–Meier/competing-risk and overall plus survivor/death-separated analyses are not specified by the reported pooled rank-sum statement. Numeric ranges for medians 8 and 6 are [7.5,8.5) and [5.5,6.5); mean difference 0.6 allows [.55,.65), CI endpoints [−1.05,−.95) and [2.15,2.25), P=.07 allows [.065,.075). Medians and a difference in means are different summaries and were not equated. Their display precision cannot resolve the method/population specification difference.

**Affected result or extracted value:** Abstract-reported ICU-stay contrast and the population/estimand associated with.6 days and P=.07.

**Why context does not resolve it:** No supplied analysis-change explanation connects the explicit pooled rank-sum method to the final prospective estimators and population split.

**Alternative source-grounded interpretations:** Pooled rank-sum may have replaced the planned analyses, or the planned analyses may have been performed additionally without identifiable reporting. The plan's former/latter wording does not fully specify how every event is coded.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: the prospective survival/competing-risk procedures and population split differ from the explicitly named report rank-sum comparison, with no supplied connecting statement.

Necessary inputs available: Explicit prospective procedures/population split, report procedure and summary labels. **Exact missing inputs or definitions:** Planned time/event coding, separately reported survivor/death ICU-stay populations and estimates, survival/competing-risk results, and a reconciliation of those procedures with the reported rank-sum result.

Direct observation and inferred explanation: Method names, intended population split and pooled reporting are directly observed. A numerical inconsistency between medians and means, the event coding, or analysis replacement mechanism is not inferred.

Checker provenance: Cross-source G07; duplicate F-ST1-006. Statistical relationships S027, S029.

**Potential downstream evidence impact:** If confirmed, an extractor could attach a pooled or survivor/death-separated population and a rank-based or survival/competing-risk analysis designation to the ICU-stay contrast. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which ICU-stay population and analytical procedure generated the mean difference 0.6 days and P=.07, and how do these correspond to the planned overall and survivor/death-separated analyses? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Prospective and displayed subgroup boundaries

**Status:** Pending Human Adjudication

**Candidate statement:** The displayed predefined time subgroups place day 2 in the late group, whereas the prospective and reported randomization strata place it in the early group; the printed counts reproduce that membership difference.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_W

**Compared document roles:** PLAN strata pp.98,99 and SAP p.104 vs REPORT main article pp.2,4,7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Classification rationale:** Both PLAN/REPORT and within-REPORT comparisons apply; P_R has precedence over S_W, giving protocol_report.

**Classification ambiguity:** Oxygen equality boundary does not independently establish any changed membership/result; retain only as qualified context.

**Exact source locations:** PLAN [strata pp.98 — joi180109supp1_prod.pdf, PDF p. 98](<../joi180109supp1_prod.pdf#page=98>), [99 lines1600–1604 — joi180109supp1_prod.pdf, PDF p. 99](<../joi180109supp1_prod.pdf#page=99>), [final SAP p.104 lines1721–1722 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); REPORT [randomization p.2 — jama_azoulay_2018_oi_180109.pdf, PDF p. 2](<../jama_azoulay_2018_oi_180109.pdf#page=2>), [subgroup methods/Table1 p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [Figure3 p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>), both time rows in each panel and accompanying oxygen-flow rows.

Complete confirmed physical-page locations: [PDF p.98, lines 1600–1601 — joi180109supp1_prod.pdf, PDF p. 98](<../joi180109supp1_prod.pdf#page=98>); [PDF p.99, lines 1602–1604 — joi180109supp1_prod.pdf, PDF p. 99](<../joi180109supp1_prod.pdf#page=99>); [final SAP, PDF p.104, lines 1721–1722 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); [randomization, PDF p.2 — jama_azoulay_2018_oi_180109.pdf, PDF p. 2](<../jama_azoulay_2018_oi_180109.pdf#page=2>); [subgroup methods/Table 1, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [Figure 3, PDF p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>).

**Source evidence:** PLAN [PDF p.98, lines 1600–1601 — joi180109supp1_prod.pdf, PDF p. 98](<../joi180109supp1_prod.pdf#page=98>) and [PDF p.99, lines 1602–1604 — joi180109supp1_prod.pdf, PDF p. 99](<../joi180109supp1_prod.pdf#page=99>) define D0/D1/D2 versus ≥D3 and oxygen flow <9 versus ≥9 L/min, with interaction analyses on these strata. PLAN [final SAP, PDF p.104, lines 1721–1722 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>) refers primary-endpoint treatment-by-covariate interactions to the subsets defined above.

Yes. REPORT [randomization, PDF p.2 — jama_azoulay_2018_oi_180109.pdf, PDF p. 2](<../jama_azoulay_2018_oi_180109.pdf#page=2>) says time since ICU admission ≤2 versus ≥3 days, and oxygen >9 versus ≤9 L/min. REPORT [subgroup methods/Table 1, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>) links subgroup HRs to stratification variables and prints D0 244/251, D1 77/79, D2 47/38, ≥D3 20/20 for HFNO/standard. REPORT [Figure 3, PDF p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) labels time subgroups 0–1 and ≥2 days in both panels. Panel A rows are 120/321 versus 118/330, HR .95 (.74–1.22), and 18/67 versus 22/58, HR 1.55 (.83–2.90), interaction P=.15. Panel B rows are 128/321 versus 142/330, HR 1.1 (.87–1.40), and 22/67 versus 28/58, HR 1.69 (.96–2.95), interaction P=.17. The accompanying oxygen rows are ≤9/>9 in both panels: A 122/348 versus 127/347, HR 1.06 (.83–1.36), and 16/40 versus 13/41, HR .76 (.36–1.57), P=.39; B 136/348 versus 151/347, HR 1.15 (.91–1.45), and 14/40 versus 19/41, HR 1.37 (.68–2.72), P=.65. All row labels/counts were visually confirmed.

**Reported-versus-comparator:** Plan D 0,D 1,D 2 vs≥D 3; report strata≤2 vs≥3 days. Figure bins 0–1 vs≥2 days; early totals 321/330, late 67/58; Table 1 day 2 counts 47/38,≥day 3 counts 20/20. Mortality time-interaction P=.15; ventilation P=.17. Oxygen threshold plan<9/≥9 vs report≤9/>9 also retained as conditional context.

**Reasoning procedure:** Reconcile displayed membership with Table 1 day counts, then compare the predefined-strata claim to its planned boundary. focus D compares predefined subgroup membership to prospective strata and report methods; the time-boundary difference demonstrably changes primary/key-secondary subgroup populations.

**Calculation:** HFNO 244+77=321 and 47+20=67; standard 251+79=330 and 38+20=58. These exactly reproduce Figure 3's 0–1 and ≥2 denominators. Planned/reported-randomization ≤2 totals are 368 and 368, leaving ≥3 denominators 20/20. Thus 47 HFNO and 38 standard day-2 participants move relative to those strata. Counts are exact integers, not continuous rounded inputs; the categorical inequality boundary is exact. P=.15 and .17 have display ranges [.145,.155) and [.165,.175), but no rounding of P or HR can change membership. For oxygen, <9/≥9 versus ≤9/>9 differs only for participants exactly at 9; that count is unavailable, so no changed oxygen membership or effect is calculated.

**Affected result or extracted value:** Time-subgroup mortality/ventilation HR populations and prospective attribution of interaction P=.15/.17.

**Why context does not resolve it:** No explanation identifies a prospective different binning, while explicit counts demonstrate moved day2 membership.

**Alternative source-grounded interpretations:** A different subgroup cutpoint could have been prospectively intended independently of the randomization strata; the display may be describing different analysis bins. The supplied methods link the subgroups to strata and do not identify that distinct prospective rule.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: exact printed day counts reproduce the forest's ≥2 population, whereas the prospective/report-randomization late stratum starts at ≥3.

Necessary inputs available: Prospective strata, reported randomization/method statements, four Table 1 day counts per arm and both forest panels' denominators. **Exact missing inputs or definitions:** Prospective justification for a distinct 0–1/≥2 analysis rule, actual subgroup coding, and number of participants exactly at 9 L/min. A label difference alone is not used to infer the latter count.

Direct observation and inferred explanation: Day-2 membership follows exactly from printed denominators and Table 1 counts. An effect of the oxygen equality boundary, a changed HR from recoding, or the reason for adopting these bins is not inferred.

Checker provenance: Cross-source G09; duplicate F-ST1-008. Statistical relationships S006, S038, S039, S040, S052, S053, S065, S071.

**Potential downstream evidence impact:** If confirmed, an extractor could attach the four time-subgroup HRs and interaction tests to the displayed 0–1/≥2 groups or to the prospective ≤2/≥3 strata; their population definitions differ. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. What were the prospectively specified mortality and ventilation subgroup boundaries, and which time and oxygen-flow populations do the displayed HRs and interaction tests represent? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Primary relative-risk plan and reported hazard ratio

**Status:** Pending Human Adjudication

**Candidate statement:** The final plan specifies a binary day-28 mortality relative risk, while the report identifies a Cox hazard ratio as its primary relative effect and supplies no identifiable corresponding primary day-28 RR result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original/final SAP pp.82,104 vs REPORT main article pp.3,5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Classification rationale:** PLAN versus REPORT primary estimand/model; P_R/protocol_report. Separate C008 applies the independent adjustment rule.

**Classification ambiguity:** Hospital-death wording in the immediate binaryday28 clause is context-resolved and not a separate endpoint issue.

**Exact source locations:** PLAN [original SAP p.82 lines1297–1300 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>), [final SAP p.104 lines1731–1734 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); REPORT [primary methods p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), [Table2 p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>). REPORT p.8 is adjustment context in C008.

Complete confirmed physical-page locations: [original SAP, PDF p.82, lines 1297–1300 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>); [final SAP, PDF p.104, lines 1731–1734 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); [primary methods, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>); [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>).

**Source evidence:** PLAN [original SAP, PDF p.82, lines 1297–1300 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>) and [final SAP, PDF p.104, lines 1731–1734 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>) describe a binary alive/dead endpoint at day 28 and an experimental/control relative risk with 95% CI. Their hospital-death wording was read in that immediate day-28 binary context; it is not used for a separate endpoint candidate.

Yes. REPORT [primary methods, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>) describes Kaplan–Meier mortality estimation, risk difference and HR from univariable Cox models. REPORT [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>) labels primary all-cause day-28 mortality HR .98 (.77–1.24). Its separate ICU/hospital mortality RR rows are distinct outcomes, not the planned primary RR. The report's redesign paragraph on p.3 explains an early noninferiority-to-superiority change; the final SAP being compared already specifies superiority.

**Reported-versus-comparator:** Plan alive/dead by 28 days and experimental/control relative risk of hospital death with 95%CI; report Kaplan–Meier, risk difference and univariable Cox HR 0.98 (.77,1.24). ICU/hospital RRs are different endpoints.

**Reasoning procedure:** Compare supplied effect-measure/model specifications after final-plan version matching; isolate effect identity from covariate adjustment. focus D compares final planned primary estimand/model with the identifiable reported primary result. Effect-measure identity is independent of C008's covariate-adjustment comparison.

**Calculation:** A binary day-28 risk ratio and a Cox hazard ratio are distinct estimands regardless of numerical proximity. HR .98 allows [.975,.985); printed CI .77–1.24 allows [.765,.775) and [1.235,1.245). No value within these display ranges changes an HR into an RR. No crude RR was substituted for a model estimate, and the effect difference was not calculated from count ratios.

**Affected result or extracted value:** Primary mortality effect-measure identity and availability of the planned primary RR result.

**Why context does not resolve it:** Disclosed grant-stage redesign does not explain this difference against the final superiority SAP.

**Alternative source-grounded interpretations:** The HR may intentionally replace the planned RR; a primary RR analysis may also have been performed but is not identifiable in the supplied report. Neither possibility is specified by the redesign paragraph.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: the final SAP identifies an RR for the binary day-28 endpoint, while the report explicitly identifies its primary treatment effect as a Cox HR.

Necessary inputs available: Exact final and original estimand statements, report model and effect labels, primary endpoint definition. **Exact missing inputs or definitions:** Primary day-28 RR estimate/CI or an explicit explanation that the final primary estimand was changed to HR; event times and model output needed to reconstruct the HR.

Direct observation and inferred explanation: PLAN RR and REPORT HR labels/models differ directly. A change of numerical results, the actual effect of substituting estimands, or a rationale for that substitution is not inferred.

Checker provenance: Cross-source G03; duplicate F-ST1-002. Adjustment component of F-XS-003 belongs to C008. Statistical relationship S010.

**Potential downstream evidence impact:** If confirmed, evidence extraction could retain the reported HR under the intended HR designation, or seek the prospectively specified primary RR and its interval. The reported HR cannot be designated an RR solely because the numbers may be close. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which final primary estimand was intended, and where is the planned day-28 RR result or a reconciliation of that specification with the reported HR? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Planned covariate adjustment and explicit univariable models

**Status:** Pending Human Adjudication

**Candidate statement:** The planned potential-confounder adjustment for primary mortality and ventilation treatment effects differs from the report’s explicitly univariable models.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original/final SAP pp.82,104,105 vs REPORT main article pp.3,4,5,8

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Classification rationale:** PLAN versus REPORT model specification; P_R/protocol_report. One repeated adjustment pattern spans mortality and ventilation.

**Classification ambiguity:** Specific confounders unspecified; infection model is not asserted univariable.

**Exact source locations:** PLAN [original SAP p.82 lines1300–1310 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>), [final SAP p.104 line1734 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>), [p.105 line1742 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); REPORT [methods p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), [methods p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [Table2 p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), [limitations p.8 — jama_azoulay_2018_oi_180109.pdf, PDF p. 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>).

Complete confirmed physical-page locations: [original SAP, PDF p.82, lines 1300–1310 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>); [final SAP, PDF p.104, line 1734 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); [PDF p.105, lines 1738–1742 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>); [primary methods, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>); [ventilation methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>); [limitations, PDF p.8 — jama_azoulay_2018_oi_180109.pdf, PDF p. 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>).

**Source evidence:** PLAN [original SAP, PDF p.82, lines 1300–1310 — joi180109supp1_prod.pdf, PDF p. 82](<../joi180109supp1_prod.pdf#page=82>) prescribes potential-confounder adjustment for the primary analysis and cause-specific Cox adjustment for competing-risk endpoints including intubation. PLAN [final SAP, PDF p.104, line 1734 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>) repeats primary adjustment; PLAN [PDF p.105, lines 1738–1742 — joi180109supp1_prod.pdf, PDF p. 105](<../joi180109supp1_prod.pdf#page=105>) repeats competing-risk adjustment.

Yes. REPORT [primary methods, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>) explicitly identifies univariable Cox models; REPORT [ventilation methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>) explicitly identifies a univariable cause-specific Cox model. REPORT [Table 2, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>) supplies mortality HR .98 (.77–1.24) and ventilation HR .85 (.68–1.06), the affected treatment effects. REPORT [limitations, PDF p.8 — jama_azoulay_2018_oi_180109.pdf, PDF p. 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>) acknowledges that treatment estimates were not adjusted on stratification factors.

**Reported-versus-comparator:** Plan primary potential-confounder adjustment and secondary adjusted cause-specific Cox. Report univariable mortality and ventilation Cox estimates; mortality HR.98 (.77,1.24), ventilation HR.85 (.68,1.06); p.8 acknowledges estimates not adjusted on stratification factors.

**Reasoning procedure:** Compare explicit adjustment specifications across the same primary and key secondary treatment effects. No specific unprinted confounder is assigned. focus D compares explicit planned covariate adjustment with explicit reported treatment-only/univariable analyses for primary mortality and key-secondary ventilation. This rule does not depend on whether the primary effect is an RR or HR.

**Calculation:** Potential-confounder-adjusted and univariable model specifications differ logically; numeric rounding cannot supply covariates. Mortality HR display range is [.975,.985), ventilation [.845,.855), and their printed CI endpoint ranges are [.765,.775)/[1.235,1.245) and [.675,.685)/[1.055,1.065). All such values could arise under either adjustment designation, so no estimate calculation is used as proof of adjustment. The explicit text is decisive.

**Affected result or extracted value:** Adjustment designation and prospective analytical basis of the mortality/ventilation effects.

**Why context does not resolve it:** Acknowledging absent stratification adjustment does not identify the prescribed adjusted results or a reconciled final specification.

**Alternative source-grounded interpretations:** Univariable models could have replaced the prescribed adjusted analyses, or additional adjusted analyses may have been run without identifiable reporting. Absence of stratification adjustment in the limitations supports the report description but does not specify every potential confounder intended in the plan.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: directly read final adjustment prescriptions differ from directly read univariable mortality and ventilation model statements.

Necessary inputs available: Positive planned adjustment statements and positive reported univariable statements for both outcomes. **Exact missing inputs or definitions:** Named potential confounders, final covariate/model specification, adjusted mortality and ventilation estimates or a supplied reconciliation of the change. Infection's fitted adjustment is not specified; it is not asserted to be univariable.

Direct observation and inferred explanation: Adjusted versus univariable method text differs directly in the two named treatment effects. Particular omitted covariates, magnitude of any adjusted-result change, and an explanation for the selection are not inferred.

Checker provenance: Statistical G04; adjustment component of F-XS-003 retained without a second screening row. Statistical relationships S011, S021.

**Potential downstream evidence impact:** If confirmed, extraction could attach an adjusted or univariable designation to the mortality and ventilation HRs without a reconciliation of the planned covariate specifications. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Which final covariate-adjustment specifications applied to the primary mortality and ventilation treatment effects, and where are the planned adjusted results or a reconciliation with the reported univariable models? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Comparator rescue-HFNO permission

**Status:** Pending Human Adjudication

**Candidate statement:** The report explicitly permits conditional rescue HFNO in the comparator arm, whereas the supplied final plan categorically excludes HFNO in that arm.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN rationale pp.95,96 and intervention p.99 vs REPORT main article pp.3,5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Classification rationale:** PLAN versus REPORT randomized comparator rule; P_R/protocol_report.

**Classification ambiguity:** No supplied amendment identifies this rescue permission as a reconciled prospective change.

**Exact source locations:** PLAN [rationale p.95 — joi180109supp1_prod.pdf, PDF p. 95](<../joi180109supp1_prod.pdf#page=95>), [p.96 — joi180109supp1_prod.pdf, PDF p. 96](<../joi180109supp1_prod.pdf#page=96>), [intervention p.99 lines1616–1625 — joi180109supp1_prod.pdf, PDF p. 99](<../joi180109supp1_prod.pdf#page=99>); REPORT [treatments/Figure1 p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), [interventions p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>).

Complete confirmed physical-page locations: [rationale, PDF p.95, lines 1544–1552 — joi180109supp1_prod.pdf, PDF p. 95](<../joi180109supp1_prod.pdf#page=95>); [PDF p.96, lines 1553–1554 — joi180109supp1_prod.pdf, PDF p. 96](<../joi180109supp1_prod.pdf#page=96>); [final intervention, PDF p.99, lines 1616–1625 — joi180109supp1_prod.pdf, PDF p. 99](<../joi180109supp1_prod.pdf#page=99>); [treatments, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>); [intervention results, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>).

**Source evidence:** PLAN [rationale, PDF p.95, lines 1544–1552 — joi180109supp1_prod.pdf, PDF p. 95](<../joi180109supp1_prod.pdf#page=95>) sets the comparative oxygen strategies; PLAN [PDF p.96, lines 1553–1554 — joi180109supp1_prod.pdf, PDF p. 96](<../joi180109supp1_prod.pdf#page=96>) says HFNO will not be used in the control group. PLAN [final intervention, PDF p.99, lines 1616–1625 — joi180109supp1_prod.pdf, PDF p. 99](<../joi180109supp1_prod.pdf#page=99>) repeats that categorical rule at line 1621.

Yes. REPORT [treatments, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>) permits HFNO only for standard-arm patients with do-not-intubate orders whose standard therapy failed. Figure 1 on the same page records 30 standard-arm HFNO recipients. REPORT [intervention results, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>) records these 30 patients (7.7%) and 14 deaths (46.7%).

**Reported-versus-comparator:** Plan HFNO not used in control; report allows rescue for do-not-intubate controls after standard failure;30(7.7%) received HFNO,14(46.7%) died; Figure 1 records 30 control HFNO recipients.

**Reasoning procedure:** Compare explicit comparator strategy rules, not individual clinical appropriateness or mere occurrence of crossover. focus D compares an explicit randomized comparator-intervention rule, which defines the strategy underlying primary mortality and ventilation results. Occurrence of a crossover or individual clinical appropriateness is not the rule under examination.

**Calculation:** The categorical PLAN no-HFNO rule and REPORT conditional permission remain different irrespective of counts. Contextual arithmetic reproduces 100×30/388 = 7.731959%, inside the displayed 7.7% interval [7.65,7.75); 100×14/30 = 46.666667%, inside [46.65,46.75). These percentages reconcile. Exact integer counts and allowed numeric intervals do not transform a prohibition into conditional permission.

**Affected result or extracted value:** Comparator intervention definition underlying primary mortality and day 28 ventilation effects.

**Why context does not resolve it:** Report explains the rescue condition but does not reconcile permission with final-plan prohibition.

**Alternative source-grounded interpretations:** The intended final comparator may have included an additional rescue rule; individual departures from the categorical plan may instead have been reported as a general treatment description. The supplied evidence does not identify which applies.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: the final plan expressly excludes HFNO in controls whereas the report expressly permits conditional rescue HFNO.

Necessary inputs available: Explicit prospective restriction, explicit report permission and reported recipient counts. **Exact missing inputs or definitions:** A supplied prospective amendment or final-strategy specification reconciling the rescue permission with the final-plan restriction. Participant-level eligibility and individual reasons are neither required for this comparison nor inferred.

Direct observation and inferred explanation: Plan prohibition, report conditional permission and counts are directly observed. A protocol violation, justification of any individual crossover, or an effect on mortality is not inferred.

Checker provenance: Cross-source G08.

**Potential downstream evidence impact:** If confirmed, extraction could describe the comparator as standard oxygen with conditional rescue HFNO rather than the prospectively stated no-HFNO strategy. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. Was conditional rescue HFNO part of the intended final comparator strategy, and where is that permission reconciled with the supplied final-plan prohibition? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Prespecified per-protocol primary result unavailable

**Status:** Pending Human Adjudication

**Candidate statement:** The final plan unconditionally promises per-protocol analysis in the primary-analysis methodology, while the complete supplied REPORT package identifies only the ITT primary population/result and no separately identifiable per-protocol mortality result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final SAP p.104 vs REPORT main article pp.1-9 and results supplement pp.1-5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Classification rationale:** PLAN versus REPORT primary sensitivity-result availability; P_R/protocol_report.

**Classification ambiguity:** Absence is limited to supplied report content; no claim that the analysis was never performed or that its result differs from ITT.

**Exact source locations:** PLAN [final SAP p.104 lines1717–1723 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); REPORT [primary methods p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), [methods p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [results p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), [p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), [p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>); absence search covers REPORT main pp.1–9 and results supplement pp.1–5, with data-sharing statement p.1 administrative only.

Complete confirmed physical-page locations: [final SAP, PDF p.104, lines 1717–1723 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>); [main methods/Figure 1, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>); [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>); [Table 2/primary results, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>); [secondary results/primary survival figure, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>); [subgroup forest, PDF p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>); [abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>); [background/design p.2 — jama_azoulay_2018_oi_180109.pdf, PDF p. 2](<../jama_azoulay_2018_oi_180109.pdf#page=2>); [discussion/administrative p.8 — jama_azoulay_2018_oi_180109.pdf, PDF p. 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>); [administrative/references p.9 — jama_azoulay_2018_oi_180109.pdf, PDF p. 9](<../jama_azoulay_2018_oi_180109.pdf#page=9>); [cover p.1 — joi180109supp2_prod.pdf, PDF p. 1](<../joi180109supp2_prod.pdf#page=1>); [eTable p.2 — joi180109supp2_prod.pdf, PDF p. 2](<../joi180109supp2_prod.pdf#page=2>); [ventilation figure p.3 — joi180109supp2_prod.pdf, PDF p. 3](<../joi180109supp2_prod.pdf#page=3>); [oxygenation figure p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>); [comfort/dyspnea figure p.5 — joi180109supp2_prod.pdf, PDF p. 5](<../joi180109supp2_prod.pdf#page=5>); [data-sharing statement p.1 — joi180109supp3_prod.pdf, PDF p. 1](<../joi180109supp3_prod.pdf#page=1>).

**Source evidence:** PLAN [final SAP, PDF p.104, lines 1717–1723 — joi180109supp1_prod.pdf, PDF p. 104](<../joi180109supp1_prod.pdf#page=104>) places the main ITT comparison and primary-endpoint interaction analyses in its methodology section and ends with an unconditional promise that a per-protocol analysis will be performed. The subsequent missing-value section is separate and does not make that sentence conditional.

REPORT [main methods/Figure 1, PDF p.3 — jama_azoulay_2018_oi_180109.pdf, PDF p. 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>) describes ITT with only withdrawn-consent exclusions and includes 388 in each primary-analysis arm. REPORT [methods, PDF p.4 — jama_azoulay_2018_oi_180109.pdf, PDF p. 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), [Table 2/primary results, PDF p.5 — jama_azoulay_2018_oi_180109.pdf, PDF p. 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), [secondary results/primary survival figure, PDF p.6 — jama_azoulay_2018_oi_180109.pdf, PDF p. 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>) and [subgroup forest, PDF p.7 — jama_azoulay_2018_oi_180109.pdf, PDF p. 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>) contain no separately identified per-protocol population/result. Complete supplied-report inspection additionally covers [abstract p.1 — jama_azoulay_2018_oi_180109.pdf, PDF p. 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), [background/design p.2 — jama_azoulay_2018_oi_180109.pdf, PDF p. 2](<../jama_azoulay_2018_oi_180109.pdf#page=2>), [discussion/administrative p.8 — jama_azoulay_2018_oi_180109.pdf, PDF p. 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>), [administrative/references p.9 — jama_azoulay_2018_oi_180109.pdf, PDF p. 9](<../jama_azoulay_2018_oi_180109.pdf#page=9>), results supplement [cover p.1 — joi180109supp2_prod.pdf, PDF p. 1](<../joi180109supp2_prod.pdf#page=1>), [eTable p.2 — joi180109supp2_prod.pdf, PDF p. 2](<../joi180109supp2_prod.pdf#page=2>), [ventilation figure p.3 — joi180109supp2_prod.pdf, PDF p. 3](<../joi180109supp2_prod.pdf#page=3>), [oxygenation figure p.4 — joi180109supp2_prod.pdf, PDF p. 4](<../joi180109supp2_prod.pdf#page=4>), [comfort/dyspnea figure p.5 — joi180109supp2_prod.pdf, PDF p. 5](<../joi180109supp2_prod.pdf#page=5>), and [data-sharing statement p.1 — joi180109supp3_prod.pdf, PDF p. 1](<../joi180109supp3_prod.pdf#page=1>). None identifies a primary per-protocol definition, denominator or mortality effect. The data-sharing page is administrative and has no analysis result.

**Reported-versus-comparator:** Plan says per-protocol analysis will be performed. Report ITT excludes withdrawn consent only,388 per arm, with no PP definition, population or day 28 mortality effect.

**Reasoning procedure:** Compare an express prospective primary-analysis promise with complete supplied-report coverage; focus D expressly includes a prespecified primary analysis not reported. the explicit focus-D provision covers a prespecified primary analysis not reported. The comparison is the promise of a distinct per-protocol primary analysis versus its identifiable availability in the supplied reporting package, not the absence of an arbitrary method detail.

**Calculation:** Full supplied-report reading and a case-insensitive per-protocol/analysis-population text search found no identifiable PP result. ITT denominators 388/388 are exact counts. No numeric half-unit interval can supply an unreported PP definition, denominator or result. The 12 intervention switches and 30 comparator HFNO recipients were not subtracted from ITT denominators; treatment changes do not establish a PP exclusion rule.

**Affected result or extracted value:** Availability of prespecified primary per-protocol mortality population/result.

**Why context does not resolve it:** Conditional missingness and disclosed early design changes do not explain the unconditionally stated final primary sensitivity analysis.

**Alternative source-grounded interpretations:** A PP analysis could have been performed but not included in the supplied reports, or the final analysis promise could have changed. The complete local package establishes neither which alternative applies nor that PP and ITT results differ.

**Mechanical evidence recheck:** All cited source locations were found; printed source and comparator values/statements matched. No transcription correction or classification change was needed. Evidence state: reproduced. Determining fact: the final SAP unconditionally promises a PP analysis while every supplied REPORT page lacks an identifiable PP primary result/definition.

Necessary inputs available: Express final prospective promise, explicit report ITT definition, all supplied REPORT pages and their analysis displays. **Exact missing inputs or definitions:** Final PP eligibility/exclusion definition, PP participants/events, primary PP effect/interval/test, or a supplied statement explaining replacement/withdrawal of that prespecified analysis.

Direct observation and inferred explanation: The promise and absence of an identifiable PP result within the supplied REPORT package are directly observed. Never performing the analysis, any PP sample size, or the direction/magnitude of a PP effect would be inference and is not asserted.

Checker provenance: Statistical G10; cross-source exclusion of this observation was independently reconsidered by the screener. Statistical relationship S037.

**Potential downstream evidence impact:** If confirmed, an extractor would be unable to extract the promised primary per-protocol population and mortality estimate from the supplied reports. No value, direction or magnitude is inferred for that unavailable result. No actual downstream propagation, conclusion change or harm is established.

**Human verification steps:** Open every cited supplied PDF page and match the population, time, contrast and final-plan version before considering the comparison. What definition, population and mortality result implement the promised primary per-protocol analysis, or what supplied reconciliation explains its replacement or absence from the reports? Record the adjudication and any source-grounded reconciliation in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

A systematic review, meta-analysis or guideline may reuse a numerical estimate together with its endpoint, time, population, intervention reference and analysis designation. A confirmed reporting inconsistency could affect which source value or annotation is copied. The cards identify those specific extraction questions; the supplied package does not show actual propagation, a change in clinical conclusions or serious harm. Human review should distinguish the directly printed comparison from its possible explanation before reusing evidence.

## Limitations and Missing Definitions

All 144 supplied PDF pages are scientifically mapped; no source-coverage gap remains. Review conclusions concern the supplied reporting package and are Pending Human Adjudication.

- Supplied sources contain no raw participant data, individual event times, fitted model objects, explicit reference coding for the forest models, or per-protocol population/result. No such inputs were inferred.
- Exact construction of several confidence intervals and tests, model covariate lists, degrees of freedom, covariance estimates, and some baseline/subgroup available-case denominators are not supplied. Conditional numerical diagnostics do not substitute for source-established analyses.
- Supplementary longitudinal graphs lack exact printed coordinates and definitions of their bars and asterisks. Visual values are approximate and used for qualitative matching; the review does not treat bars as a particular interval type or graph centres as a specified mean/median without source support.
- Historical background Table4 in the PLAN PDF pp.127–128 visibly clips text at its right edge. These pages were inspected and mapped; obscured historical details were not reconstructed and do not leave a current-trial scientific-coverage gap.
- Original derivative engine versions are unavailable. Current Poppler25.03.0 confirmed native extraction for every page: 143 byte matches and one whitespace-only match; four layout differences concern wrapping or graphical label placement. Native text and direct/reusable page images supplied the required evidence. Sources remain final authority.
- Optional reusable render gaps were covered by usable text and targeted direct rendering. OCR and Office conversion are unavailable locally, but all supplied sources are text-bearing PDFs and neither capability was required. No fallback environment or global installation was needed.
- Candidate assertions about unreported analyses are limited to their absence from the complete supplied REPORT material. They do not establish whether an analysis was performed, what an unreported result would be, or whether a later specification existed outside this package.

The review does not conduct a raw-data, clinical, study-design, novelty or misconduct audit, propose a preferred analysis, or adjudicate any candidate.

C001’s source-label comparison reproduces, but its inclusion is QUESTIONED because the same-sentence six-hour cue may resolve the result attribution. Unprinted forest coding, model covariates, infection/ICU-stay implementation, oxygen-flow equality membership and primary per-protocol definitions/results remain bounded human questions. Positive analytical-specification differences do not establish actual replacement, nonperformance or bias. The complete absence comparison in C010 is restricted to supplied REPORT pages.

## Human Adjudication Checklist

- Confirm the printed values/statements on every exact source page, including all repeated-pattern occurrences.
- Identify the intended result, population, time, intervention reference and applicable final-plan version.
- Apply all four inclusion criteria, including immediate context; explicitly reconsider C001’s same-sentence six-hour cue.
- Distinguish direct source facts from diagnostic calculations and unreported implementation details.
- For plan/report comparisons, locate any supplied reconciliation or identifiable planned result before judging the candidate.
- Complete Validity, Importance, Action, Initials and Notes for every card. The report leaves these fields as `__` and supplies no human disposition.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_1/routing_preflight.md) records PASS, Coordinator inference: PASS, execution mode INTERACTIVE_CLI, Provider CURRENT_SESSION, and verification of all ten fixed named presets. Every specialist execution is fresh and has a distinct runtime ID. All agents use gpt-6.1-sol, with the effort recorded below.

### Source integrity and reproducibility

The supplied-source SHA-256 identities and 396 reused-asset identities were checked unchanged during the coverage audit. Final integrity and automated closeout records are maintained by the coordinator in the versioned review directory. The [source hash record](review_1_6_1/source_hashes_before.sha256) and [reused-artifact hash record](review_1_6_1/reused_artifact_hashes_before.sha256) identify the preserved inputs. The [automated validation record](review_1_6_1/review_validation.json) documents final mechanical validation.

```text
515e58637dd5489fa605d597e7d637c52297a954616e3924f6fc14fa46d1f0b6  jama_azoulay_2018_oi_180109.pdf
8036657a65b8d2de9f209729822652f95ba1436079ce8e524d6538b64f7f87c3  joi180109supp1_prod.pdf
13c31ed5f073920f8c5fcd98965e4ed6a19411480939559d4eb87a792276a868  joi180109supp2_prod.pdf
2fdd033524cf8076b380c2a1e9fe1bf12d2ad6b91e40781f50e3f2873442e528  joi180109supp3_prod.pdf
```

Direct PDF information, native/layout extraction and CPU rendering used Poppler 25.03.0; hashes used sha256sum. The historical derivative version is unavailable. No OCR or Office conversion was required; no fallback environment was created. Pandoc 3.1.11.1 is available for the coordinator’s standalone HTML rendering. See the [tooling record](review_1_6_1/tooling_record.md). This Markdown assembly used only durable source-linked review artifacts; no external literature or web evidence was used.

### Agent executions

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_part_2 | root/support_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_2.md |
| support_quantitative_mapper_part_3 | root/support_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_3.md |
| support_quantitative_mapper_part_4 | root/support_mapper_4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_4.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/audit_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_candidates_1 | root/audit_candidates_1 | gpt-6.1-sol | high | FRESH_SPAWN | quality/audit_candidates_part_1.md |
| quality_control_auditor_candidates_2 | root/audit_candidates_2 | gpt-6.1-sol | high | FRESH_SPAWN | quality/audit_candidates_part_2.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

- **Target basis:** Four PDFs contain 144 pages, all reusable-backed with 0 fresh-required pages; no Office conversion or OCR is needed. A 129-page multi-version plan bundle requires four bounded support mapping shards, followed by concurrent checking and separate screening, recheck, statistical pass 2, audit and report waves. Complete source reuse reduces preprocessing burden; plan-version comparisons and visual figures retain review work. Package-specific planning range is 25-40 minutes.
- **Total source units:** 144
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:52:45Z
- **Finished UTC:** 2026-10-11T03:36:49Z
- **Observed elapsed minutes:** 44.07
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Ten complete evidence rechecks and repeated-pattern source locations, three bounded high-effort audit shards, inclusion qualifications and full ten-card report assembly required additional agent waves beyond the 40-minute estimate. No coverage or candidate was omitted.

Performance values were finalized by the coordinator after complete Markdown assembly and report checks, using the same exact fields in [run state](review_1_6_1/run_state.md). Local rendering and mechanical validation are outside the review-duration window; any later model repair requires updated timing.
