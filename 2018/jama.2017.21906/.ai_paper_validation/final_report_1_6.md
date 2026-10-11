# ACS QUIK: Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6

> **Pending Human Adjudication.** All 28 stable candidate records are included. Evidence states and suggested dispositions describe mechanical review facts and pre-fill human review; they do not decide validity, importance, acceptance, or correction.

## Executive Quality-Control Summary

The review mapped all 80 physical pages of four supplied PDFs and checked 100 numeric relationship groups and 161 statistical relationship groups. Both statistical passes cover the complete relationship inventory. Discovery began anew from supplied sources and usable source-bound extraction assets, without a candidate-count limit or prior candidate/report inputs.

The ledger contains **28 stable candidates**: 25 recorded observations or conditional reporting questions, one registered discrepancy not reproduced by direct source recheck, and two records with unsupported input alignment. Those 25 observations are not 25 established errors. All records remain available for human adjudication.

Several main-report observations concern repeated beta-blocker effect displays and effect-measure definitions. Plan-material questions concern sample operational graphics, distribution definitions, rollout wording and conditional dropout arithmetic. The supplied SAP and reported age subgroup partition differ. Source recheck corrected a locator reading in Figure 1: cohort 2 step 5 has **28**, producing **295** lost follow-ups, consistent with the prose; C017 therefore retains its stable ID with `not_reproduced`. C018 and C019 retain `record_input_error` because their numerical comparisons assume unestablished equal estimands.

Small preventable reporting defects can matter when a later reviewer copies an interval, effect measure, denominator or date into an evidence product. This review establishes neither downstream propagation nor a change to the paper's conclusions.

## Package and Reused-Evidence Provenance

Only the supplied package was used. The [source inventory](review_1_6/source_inventory.md) records content roles, physical page counts and identity. No direct Office, workbook or CSV source is present.

| Source ID | Supplied source | Physical pages | Content role |
|---|---|---:|---|
| DOC-001 | [jama_huffman_2018_oi_170166.pdf](../jama_huffman_2018_oi_170166.pdf#page=1) | 12 | REPORT main article |
| DOC-002 | [joi170166supp1_prod.pdf](../joi170166supp1_prod.pdf#page=1) | 32 | PLAN protocol, including background and operational appendices |
| DOC-003 | [joi170166supp2_prod.pdf](../joi170166supp2_prod.pdf#page=1) | 9 | PLAN statistical analysis plan |
| DOC-004 | [joi170166supp3_prod.pdf](../joi170166supp3_prod.pdf#page=1) | 27 | Mixed: REPORT index p. 1 and results pp. 17–27; PLAN operational/sample toolkit pp. 2–16 |

The [evidence-asset inventory](review_1_6/evidence_asset_inventory.md) assesses and individually hashes 78 reusable native/layout text, OCR, image and source-map/provenance assets. All four reusable native-text files exactly match current direct extraction. Three support layout files also match; positional differences in main rotated graphics make the old main layout a locator rather than final authority. Source-linked OCR and images cover 14 scanned toolkit pages. Existing OCR's historical GPU metadata describes its earlier production; this CPU-only review invoked no GPU.

Reusable assets cover 79 unique source pages. The protocol's p. 14 Time and Events graphic required fresh direct native/layout extraction and visual mapping. Targeted direct rendering also confirmed candidate locations. Reuse and fresh rendering are overlapping derivative operations, not additional source units. Sources and pre-existing artifacts were preserved.

## Scope, Complete Coverage, and Exclusions

Every direct source unit was assigned and mapped. [Source coverage](review_1_6/source_coverage.md) and the [coverage manifest](review_1_6/coverage_manifest.md) identify the disjoint assignments and their durable outputs.

| Source | Total pages | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 | 32 | 31 | 1 | 32 | COMPLETE |
| DOC-003 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | 27 | 27 | 0 | 27 | COMPLETE |
| **Total** | **80** | **79** | **1** | **80** | **COMPLETE** |

The complete [main map](review_1_6/extraction/main_quantitative_evidence.md) covers 12 pages; the [support map](review_1_6/extraction/support_quantitative_evidence.md) covers 68 pages (32+9+27). Covers, references, consent and administrative material remain in the page ledgers even when no achieved-result relationship applies.

The review prioritizes arithmetic, counts, proportions, denominators, intervals, effect measures, scale/unit labels, reference groups and matched results. Population or analysis-unit issues qualify only where a concrete reported quantitative relationship is affected. It excludes broad methodology, study-design, clinical, novelty, misconduct and raw-data audits. No web or external literature was used. A coherent display-zero P value alone cannot create a candidate; both statistical passes applied that exclusion. No candidate card depends on such a display.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md) contains N001–N100, including constituent cells rather than one sampled cell per group. The [statistical inventory](review_1_6/statistics/relationship_inventory.md) contains 161 groups: S001–S080 for main evidence and S201–S281 for support evidence. The numbering gap is a disjoint source-shard convention, not omitted relationships.

Main mapping includes all 27 Table 1 rows, 21 Table 2 rows, 10 Table 3 rows, 20 Figure 1 boxes, 60 Figure 2 points/interval bars and all 14 Figure 3 subgroups. Statistical coverage includes 133 labeled main intervals and background relationships, all repeated occurrences and graphical intervals. Support coverage includes all seven result tables, all four result figures, 135 explicit interval cells, prospective definitions and all scanned sample graphics.

Fresh independent [numeric](review_1_6/checkers/numeric_consistency.md), [cross-source](review_1_6/checkers/cross_source_consistency.md) and [statistical pass 1](review_1_6/checkers/statistical_pass_1.md) reviewers produced 49 local observations. Only genuine printed-value/comparator/rule duplicates were consolidated before stable registration. Distinct footnotes, metric panels and comparison rules remain separate; no stable ID was subsequently removed.

After complete cross-lane registration and direct-source recheck, three new statistical agents completed [pass 2](review_1_6/checkers/statistical_pass_2.md). Two distinct fresh agents performed pass 1 and three other distinct fresh agents performed pass 2. Every S group has explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. Missing model definitions limit compatible-test reconstruction, rather than authorize skipping a relationship. Pass 2 found no new distinct candidate.

The complete [recheck](review_1_6/verification/evidence_recheck.md) covers every stable ID against direct source text/raster, using derivatives as locators. The [quality audit](review_1_6/quality/evidence_quality_audit.md) and its disjoint main/support coverage parts audit all 80 pages, 100 N groups, 161 S groups and all 28 candidate classifications. Context sharding bound input volume and never limited findings.

## Document-Role Classification Summary

Roles are assigned by content, not filename. `REPORT` denotes achieved-result article/supplement content; `PLAN` includes protocol, SAP, prospective operational material and historical/sample data presented within that material. The four relationship types are:

- `P_R`: substantive comparison between PLAN and REPORT; it does not establish a protocol violation.
- `P_P`: comparison solely within or between PLAN material.
- `S_C`: comparison between different REPORT documents.
- `S_W`: comparison within one REPORT document.

A corroborating document adds no discrepancy relationship. Primary precedence is P_R > P_P > S_C > S_W when multiple substantive relationships exist; every current candidate has one relationship. Domains and pre-fills follow the supplied mechanical rules.

| Primary relationship type | Count |
|---|---:|
| S_W | 14 |
| P_P | 13 |
| P_R | 1 |
| S_C | 0 |
| **Total** | **28** |

| Review domain | Count |
|---|---:|
| statistical_results | 8 |
| report_internal_inconsistency | 6 |
| plan_material | 13 |
| protocol_report | 1 |
| **Total** | **28** |

| Evidence state | Count | Mechanical suggested disposition |
|---|---:|---|
| recorded_candidate | 25 | retain |
| not_reproduced | 1 | exclude |
| record_input_error | 2 | discuss |
| repaired_residual | 0 | retain |
| **Total** | **28** | **25 retain; 1 exclude; 2 discuss** |

`recorded_candidate` includes located printed mismatches and registered conditional questions with named missing definitions. `not_reproduced` means direct source reading disproves the registered comparison. `record_input_error` identifies misassigned inputs or unsupported alignment with any residual question unsettled. `repaired_residual` would describe a corrected original input leaving a different conditional question. These are evidence-record distinctions. **Every suggested disposition is a mechanical pre-fill, and every record remains Pending Human Adjudication.**

## Candidate Index

| Stable ID | Candidate | Category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|---|
| C001 | Inpatient beta-blocker interval repeated upper endpoint | Statistical reporting inconsistency | S_W | statistical_results | recorded_candidate |
| C002 | Discharge beta-blocker risk difference repeated point estimate | Statistical reporting inconsistency | S_W | statistical_results | recorded_candidate |
| C003 | Discharge beta-blocker odds ratio repeated point estimate | Statistical reporting inconsistency | S_W | statistical_results | recorded_candidate |
| C004 | Door-to-balloon difference column percent versus time unit | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C005 | Door-to-needle difference column percent versus time unit | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C006 | Table2 odds-ratio definition says difference in marginal effects | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C007 | Table3 odds-ratio definition says difference in marginal effects | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C008 | Tobacco counseling described above95% despite94.7% | Numeric or arithmetic inconsistency | S_W | statistical_results | recorded_candidate |
| C009 | Toolkit ECG measure heading minutes versus percentage definition/display | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C010 | Toolkit three-month2014 scope versus four2011–2012 quarters | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C011 | Sample hospital gender percentages sum71% | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| C012 | Sample all-hospital gender percentages sum85% | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| C013 | Prespecified age subgroup cutpoints differ from SAP | Analysis-unit or population inconsistency | P_R | protocol_report | recorded_candidate |
| C014 | SAP four crossover periods versus five-cohort schedule | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C015 | Five-percent dropout allowance gives less than15000 retained | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C016 | Complete/missing follow-up table difference footnote names treatment arms | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C017 | Registered lost-follow-up discrepancy not reproduced | Denominator, proportion, or total inconsistency | S_W | statistical_results | not_reproduced |
| C018 | Door-to-balloon comparison uses unsupported estimand alignment | Statistical reporting inconsistency | S_W | statistical_results | record_input_error |
| C019 | Door-to-needle comparison uses unsupported estimand alignment | Statistical reporting inconsistency | S_W | statistical_results | record_input_error |
| C020 | Key Points duplicates negation in the statistical-significance statement | Statistical reporting inconsistency | S_W | statistical_results | recorded_candidate |
| C021 | residual subtraction label and directional caption differ | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C022 | STEMI/NSTEMI composite has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C023 | STEMI composite has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C024 | NSTEMI composite has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C025 | Discharge-AMI composite has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C026 | Arrival-aspirin graph has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C027 | Discharge-aspirin graph has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C028 | Discharge-beta-blocker graph has an additional timeline point | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |

# Candidate Evidence Cards

Every card repeats the current [ledger classification](review_1_6/candidate_ledger.md) exactly. Source locations use physical PDF pages. Calculation rules, alternatives and missing definitions are separated from direct observations; the following human fields are deliberately unfilled.

## C001 — Inpatient beta-blocker interval repeated upper endpoint

**Status:** Pending Human Adjudication

**Candidate statement:** The repeated adjusted inpatient beta-blocker risk difference has different upper confidence limits in Table 2 and the process-results prose.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 inpatient beta-blocker row vs REPORT main article p. 6 process prose

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 2 in-hospital beta-blocker row and final process-results paragraph in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** Table: 6.25% (95% CI, 4.10 to 8.40); prose: 6.25% (95% CI, 4.10 to 8.10). Both give OR 1.46 (1.29–1.65).

**Reported-versus-comparator:** Upper endpoint 8.40% versus 8.10% for the same displayed outcome, contrast, model and precision.

**Reasoning procedure:** Match the inpatient outcome and hospital/time-adjusted comparison, then compare the printed interval endpoints. Observe the discrepancy without assigning a transcription or model cause.

**Calculation:** 8.40−8.10=0.30 percentage points; the combined allowance for two independently rounded two-decimal endpoints is 0.01 percentage points.

**Alternative source-grounded interpretations:** A revised or different analysis could account for the values, but neither location identifies a different model or result.

**Mechanical evidence recheck:** Direct current PDF layout and fresh raster confirm both endpoints. The registered printed mismatch reproduces; the intended endpoint requires human confirmation. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** A matched effect interval should have one identifiable upper endpoint.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either upper limit into an inpatient beta-blocker effect record. No propagation is established.

**Human verification steps:** Inspect both p. 6 locations; match their outcome/model identifiers; obtain the intended adjusted output. Which upper limit, 8.40% or 8.10%, belongs to the reported 6.25% difference?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Discharge beta-blocker risk difference repeated point estimate

**Status:** Pending Human Adjudication

**Candidate statement:** The adjusted discharge beta-blocker risk difference differs between Table 2 and the discharge-results prose.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 discharge beta-blocker RD vs REPORT main article p. 7 discharge prose

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 2 discharge beta-blocker row in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6); discharge treatment paragraph in [jama_huffman_2018_oi_170166.pdf — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** Table: RD 6.69% (4.43–8.95); prose: RD 6.63% (4.43–8.95). Table counts are 5808/8894 and 6799/10178; prose summarizes 65% and 67%.

**Reported-versus-comparator:** Repeated adjusted point 6.69% versus 6.63%, with identical confidence limits.

**Reasoning procedure:** Match the discharge endpoint, contrast and adjustment. Compare adjusted points directly; do not reconstruct an adjusted RD from crude percentages.

**Calculation:** 6.69−6.63=0.06 percentage points, exceeding a combined two-decimal rounding allowance of 0.01.

**Alternative source-grounded interpretations:** An undocumented output revision or different model is possible; the supplied repeated description does not distinguish one.

**Mechanical evidence recheck:** Both direct-source points and identical intervals were confirmed. The point discrepancy reproduces. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Exact adjusted point extraction is ambiguous across two descriptions of one result.

**Potential downstream evidence impact:** If confirmed, a systematic-review extraction could record a different discharge beta-blocker RD depending on its chosen location.

**Human verification steps:** Inspect the row and paragraph and obtain the matched adjusted output. Is the intended RD 6.69% or 6.63%, and which point belongs with the 4.43–8.95 limits?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Discharge beta-blocker odds ratio repeated point estimate

**Status:** Pending Human Adjudication

**Candidate statement:** The adjusted discharge beta-blocker odds ratio is displayed as 1.48 in Table 2 and 1.47 in prose.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 discharge beta-blocker OR vs REPORT main article p. 7 discharge prose

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 2 discharge beta-blocker OR in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6); discharge beta-blocker prose in [jama_huffman_2018_oi_170166.pdf — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** Table OR 1.48 (1.30–1.68); prose OR 1.47 (1.30–1.68).

**Reported-versus-comparator:** Different two-decimal OR points with the same interval and reported endpoint.

**Reasoning procedure:** Match the repeated adjusted result and distinguish a displayed-value disagreement from evidence of different underlying estimates.

**Calculation:** 1.48−1.47=0.01. Under one nearest-rounding convention, bins [1.475,1.485) and [1.465,1.475) do not overlap. Differing tie handling at exactly 1.475 remains possible.

**Alternative source-grounded interpretations:** Different rounding conventions at a boundary or an output revision could explain the display; neither is specified.

**Mechanical evidence recheck:** Direct table and prose readings reproduce the different displayed points. No unrounded-output conflict is established. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Readers need the intended OR display and rounding convention.

**Potential downstream evidence impact:** If confirmed, exact OR extraction could depend on whether a reviewer uses the table or narrative.

**Human verification steps:** Compare both locations and check the original rounded output. Which displayed OR is intended, and was the same rounding rule applied?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Door-to-balloon difference column percent versus time unit

**Status:** Pending Human Adjudication

**Candidate statement:** The door-to-balloon time row uses minutes but its adjusted difference appears under a percent heading without a normalization definition.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 door-to-balloon minute row vs REPORT main article Table 2 percent difference header

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 2 door-to-balloon row, Difference,% header, and footnotes b/c in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** Median (IQR), min: control 65 (53–105), intervention 77 (55–118). Difference,%: 6.18 (−4.78 to 17.14); beta: 13.00 (3.64–22.36).

**Reported-versus-comparator:** Minute-valued outcome versus percent-labeled difference; the two adjusted columns are not assumed to share an estimand.

**Reasoning procedure:** Compare the row unit with the difference header and definitions. A native time difference retains minutes; a percentage requires a supplied normalization or denominator.

**Calculation:** min−min=min. No percent-change formula or denominator is printed; rounding cannot resolve a categorical unit ambiguity.

**Alternative source-grounded interpretations:** 6.18 could intentionally be a normalized percentage, while beta 13.00 could be a separate minute coefficient. The missing formula prevents selection between these interpretations.

**Mechanical evidence recheck:** Direct layout/raster confirm the units, header and values. The label-definition question remains recorded. C018 separately records unsupported numerical alignment. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** An extracted time effect needs a defined unit and contrast.

**Potential downstream evidence impact:** If confirmed, an extractor could classify 6.18 as a percentage when a minute difference was intended, or conversely.

**Human verification steps:** Inspect header and footnotes and request the column-specific formula. Is 6.18 a percentage or a minute difference, and what denominator defines any normalization?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Door-to-needle difference column percent versus time unit

**Status:** Pending Human Adjudication

**Candidate statement:** The door-to-needle time row uses minutes but its adjusted difference appears under a percent heading without a normalization definition.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 door-to-needle minute row vs REPORT main article Table 2 percent difference header

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 2 door-to-needle row, Difference,% header, and footnotes b/c in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** Median (IQR), min: control 44 (30–67), intervention 45 (27–75). Difference,%: 0.40 (−5.23 to 6.03); beta: 5.00 (−5.20–15.20).

**Reported-versus-comparator:** Minute outcome versus percent difference heading; 0.40 is not equated with beta 5.00.

**Reasoning procedure:** Read row units and column definitions independently. A native time subtraction has minute units; an intended percent change needs its formula.

**Calculation:** min−min=min; no normalization denominator is supplied. Numerical rounding does not resolve the label.

**Alternative source-grounded interpretations:** The columns may represent coherent percentage and native-unit summaries with different definitions.

**Mechanical evidence recheck:** Source values, minute label and percent header were confirmed. C019's equal-estimand premise is separate and unsupported. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The door-to-needle effect scale needs an explicit definition.

**Potential downstream evidence impact:** If confirmed, reuse of 0.40 could carry the wrong unit or transform into a time-effect extraction.

**Human verification steps:** Inspect this specific row and obtain the percent formula or minute-unit definition. What scale and contrast generates 0.40?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Table2 odds-ratio definition says difference in marginal effects

**Status:** Pending Human Adjudication

**Candidate statement:** Table 2 labels values as odds ratios while footnote b describes their calculation as intervention-minus-control differences in marginal effects.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 OR header and cells vs REPORT main article Table 2 footnote b

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 2 OR header, prehospital aspirin/inpatient beta-blocker rows, and footnote b in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** Footnote: “Odds ratios and β-coefficients … are calculated as the difference in marginal effects (intervention group minus control group).” Separate cells include aspirin RD 3.80%/OR 1.40 and inpatient beta-blocker RD 6.25%/OR 1.46.

**Reported-versus-comparator:** OR header/cells versus a subtraction definition applied to odds ratios.

**Reasoning procedure:** Distinguish a ratio of odds from subtraction of probabilities and read the separate RD column. This is a definition comparison, not a reconstruction of fitted regression coefficients.

**Calculation:** A raw probability difference lies in [−1,1] with null 0; an OR has null 1. OR 1.40 cannot itself be a raw probability subtraction. Label identity has no rounding tolerance.

**Alternative source-grounded interpretations:** The subtraction wording may have been intended for RD or beta columns. A specialized meaning of marginal effects would need an explicit ratio definition.

**Mechanical evidence recheck:** Direct source confirms the OR labels, example values and footnote wording. The printed definition question reproduces. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Effect-measure labels determine how a result is interpreted and extracted.

**Potential downstream evidence impact:** If confirmed, a data extractor could misclassify an odds ratio as an additive marginal difference.

**Human verification steps:** Read the entire footnote and identify which columns it defines. Request the OR computation and whether the subtraction wording applies to the RD column.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Table3 odds-ratio definition says difference in marginal effects

**Status:** Pending Human Adjudication

**Candidate statement:** Table 3 defines odds ratios with subtraction wording despite separately displaying odds ratios and risk differences.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 OR headers and cells vs REPORT main article Table 3 footnote a

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Table 3 OR headers, MACE/optimal inpatient medication rows, and footnote a in [jama_huffman_2018_oi_170166.pdf — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7); corroborating eTable 7 effect definitions in [joi170166supp3_prod.pdf — PDF p. 23](../joi170166supp3_prod.pdf#page=23).

**Source evidence:** Footnote: “Odds ratios … are calculated as the difference in marginal effects (intervention group minus control group).” MACE primary RD −0.09%/OR 0.98; optimal inpatient medication RD 6.00%/OR 1.45.

**Reported-versus-comparator:** OR definitions in this specific Table 3 context versus its separate OR and RD displays.

**Reasoning procedure:** Compare the measure identities and nulls. eTable 7 corroborates the ratio/difference distinction; it is not a conflicting comparator and adds no S_C relationship.

**Calculation:** Probability subtraction −0.0009 differs from OR 0.98; OR 1.45 exceeds the upper bound 1 of a raw probability difference. No rounding convention reconciles those measure identities.

**Alternative source-grounded interpretations:** The footnote may intend RD columns, or a specialized marginal definition may be omitted. The intended scope needs confirmation.

**Mechanical evidence recheck:** Direct table/raster confirmation reproduces the header-footnote mismatch. This printed footnote remains distinct from C006. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Correct measure definitions matter independently of coherent numeric effect values.

**Potential downstream evidence impact:** If confirmed, Table 3 outcomes could be entered into synthesis records under the wrong additive or multiplicative measure.

**Human verification steps:** Inspect the OR/RD columns and footnote a, then check the original model definitions. Which columns use subtraction, and how are the odds ratios computed?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Tobacco counseling described above95% despite94.7%

**Status:** Pending Human Adjudication

**Candidate statement:** The statement that tobacco cessation counseling rates were high (>95%) does not include the intervention rate of 94.7% under an each-group reading.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article p. 7 tobacco-counseling threshold prose vs REPORT main article Table 3 intervention percentage

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The scope of the prose threshold is not explicit; both compared locations are clearly REPORT.

**Exact source locations:** discharge counseling paragraph and Table 3 tobacco cessation advice row in [jama_huffman_2018_oi_170166.pdf — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** Prose: “Rates of discharge second antiplatelet use and tobacco cessation counseling were high (>95%).” Table: intervention 2618 (94.7%); control 3526 (96.0%).

**Reported-versus-comparator:** >95% threshold statement versus intervention counseling 94.7%; control 96.0% satisfies the threshold.

**Reasoning procedure:** Check the scope of the threshold language against each displayed counseling group. Do not substitute adjusted effects for observed percentages.

**Calculation:** 95−94.7=0.3 percentage points; the nearest one-decimal bin [94.65,94.75) is wholly below 95.

**Alternative source-grounded interpretations:** A loose or collective summary of several treatment/group rates could be intended rather than an assertion about every individual rate.

**Mechanical evidence recheck:** Direct source confirms the prose and both percentages. The registered threshold-scope question remains conditional on the intended reading. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** A numeric prose threshold should identify which groups it summarizes.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy an above-95% intervention uptake characterization despite the reported 94.7%.

**Human verification steps:** Compare the sentence with the tobacco row and establish its intended scope. Does >95% apply to each group or to a broader summary?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Toolkit ECG measure heading minutes versus percentage definition/display

**Status:** Pending Human Adjudication

**Candidate statement:** The sample toolkit ECG heading names minutes while its definition and displayed performance values describe percentages receiving ECG within ten minutes.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 9 ECG minute heading vs PLAN toolkit p. 9 percentage definition and display

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Section III measure 18 heading, definition, percentile and performance panels in [joi170166supp3_prod.pdf — PDF p. 9](../joi170166supp3_prod.pdf#page=9).

**Source evidence:** Heading: “Door-to-1st ECG in minutes.” Definition concerns AMI patients receiving ECG within 10 minutes. Percentiles: 99.8%, 96.1%, 92.0%, 87.6%, 71.5%; hospital scores: 87.6%, 93.4%, 94.7%, 98.5%; axes use percentages.

**Reported-versus-comparator:** Continuous time heading versus a within-threshold proportion definition and percentage display.

**Reasoning procedure:** Distinguish an elapsed-time measurement from the fraction meeting a timing threshold. Read the definition and axes together.

**Calculation:** Minutes and 100×(patients within 10 minutes/eligible patients) have different dimensions. No numeric rounding tolerance applies.

**Alternative source-grounded interpretations:** The heading may name the underlying timestamp field while the definition supplies the intended performance metric. These are sample operational values.

**Mechanical evidence recheck:** Fresh direct raster confirms the heading, definition and percentage panels. The missing intended metric label remains a recorded question. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Operational measure definitions should identify time versus threshold compliance.

**Potential downstream evidence impact:** If confirmed, reuse of this sample metric could assign minute units to percentage performance.

**Human verification steps:** Read the heading and definition together and confirm the intended audit metric. Are all displayed values percentages receiving ECG within 10 minutes?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Toolkit three-month2014 scope versus four2011–2012 quarters

**Status:** Pending Human Adjudication

**Candidate statement:** The sample ECG performance graph carries an October–December 2014 rolling-three-month heading but its x axis names four quarters in 2011–2012.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 9 rolling October-December 2014 heading vs PLAN toolkit p. 9 2011-2012 quarter labels

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** measure 18 rolling-performance heading and x-axis labels in [joi170166supp3_prod.pdf — PDF p. 9](../joi170166supp3_prod.pdf#page=9).

**Source evidence:** Heading: “Rolling 3 Months (Oct 2014–Dec 2014)”; axis: 2011Q3, 2011Q4, 2012Q1, 2012Q2. Four scores: 87.6%, 93.4%, 94.7%, 98.5%.

**Reported-versus-comparator:** 2014 three-month scope versus four differently dated quarter positions.

**Reasoning procedure:** Match the same panel's declared reporting window and time labels. Do not infer a chronology error in achieved trial data.

**Calculation:** Oct–Dec 2014 is 2014Q4; none of 2011Q3–2012Q2 overlaps that quarter. Four quarter positions are not three named months.

**Alternative source-grounded interpretations:** Historical example-axis labels or a deliberately illustrative template could explain the inconsistency; their illustrative status/window remains unspecified.

**Mechanical evidence recheck:** Fresh source raster confirms the heading and quarter labels. Both locations are sample PLAN content. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** A performance score needs an identifiable reporting date/window.

**Potential downstream evidence impact:** If confirmed, operational reuse could attach the four scores to the wrong sample reporting periods.

**Human verification steps:** Inspect all four labels and ask which dates/windows the scores represent and whether the 2014 heading applies.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Sample hospital gender percentages sum71%

**Status:** Pending Human Adjudication

**Candidate statement:** The sample Hospital gender bars total 71% of admissions; a complete common-denominator distribution would need the omitted 29% to be defined.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 10 Hospital gender bars vs PLAN toolkit p. 10 admissions distribution axis

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** Exhaustiveness and denominator identity are missing definitions; PLAN role is supported by sample toolkit content.

**Exact source locations:** Distribution of Gender chart, Hospital blue bars/legend, Percent of Admissions axis in [joi170166supp3_prod.pdf — PDF p. 10](../joi170166supp3_prod.pdf#page=10).

**Source evidence:** Hospital male 43%, female 28%; no additional gender category is displayed.

**Reported-versus-comparator:** The displayed 71% sum versus an exhaustive 100% admissions distribution, conditional on common denominator and category coverage.

**Reasoning procedure:** Add the two printed Hospital percentages and bound integer rounding. Separate the observed sum from the unestablished assumption that the two categories are exhaustive.

**Calculation:** 43+28=71%; 100−71=29 percentage points. Two nearest-integer percentages allow at most 1 percentage point combined sum error, insufficient to reach 100%.

**Alternative source-grounded interpretations:** Missing/other gender, different denominators or deliberately illustrative sample inputs could explain the gap. The chart labels none of these possibilities.

**Mechanical evidence recheck:** Fresh source raster confirms 43% and 28%. The sum reproduces, but denominator/category completeness is not established; the named question remains recorded. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The displayed sample distribution needs category and denominator definitions.

**Potential downstream evidence impact:** If confirmed as incomplete reporting, an operational extractor could mistake 71% for an exhaustive gender distribution or omit missingness.

**Human verification steps:** Inspect the Hospital bars and legend; obtain denominators and omitted-category counts. What accounts for 29%, and do both bars use the same admissions denominator?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Sample all-hospital gender percentages sum85%

**Status:** Pending Human Adjudication

**Candidate statement:** The sample All-hospital gender bars total 85%; the missing 15% needs explanation if the displayed categories form one complete admissions distribution.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 10 All-hospital gender bars vs PLAN toolkit p. 10 admissions distribution axis

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** Category coverage and denominator identity remain unspecified; both locations are PLAN sample content.

**Exact source locations:** Distribution of Gender chart, All orange bars/legend, Percent of Admissions axis in [joi170166supp3_prod.pdf — PDF p. 10](../joi170166supp3_prod.pdf#page=10).

**Source evidence:** All-hospital male 56%, female 29%; no further category is shown.

**Reported-versus-comparator:** Displayed sum 85% versus 100%, conditional on common denominator and exhaustive categories.

**Reasoning procedure:** Check the separate All-hospital pair, without borrowing the Hospital denominator or treating a missing category as proven data error.

**Calculation:** 56+29=85%; 100−85=15 percentage points. The combined integer-rounding allowance is at most 1 percentage point.

**Alternative source-grounded interpretations:** Omitted/missing gender, unequal denominators or sample template data remain source-grounded possibilities.

**Mechanical evidence recheck:** Fresh raster confirms both All-hospital values. The conditional reporting question reproduces independently of C011. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** A comparator distribution needs explicit denominator and missingness handling.

**Potential downstream evidence impact:** If confirmed, sample benchmark reuse could omit the unrepresented 15% or assume incorrect category completeness.

**Human verification steps:** Check the All series separately and obtain its common denominator/category definition. What accounts for the other 15%?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Prespecified age subgroup cutpoints differ from SAP

**Status:** Pending Human Adjudication

**Candidate statement:** The supplied SAP's a priori age split differs from the three age groups presented as prespecified in the main report.

**Category:** Analysis-unit or population inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP p. 7 age subgroup cut points vs REPORT main article Figure 3 age groups and prespecified label

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators are prospective SAP content (PLAN) and reported subgroup definitions (REPORT); P_R therefore derives protocol_report. This does not adjudicate a protocol violation. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** section 7.5.2, lines 1243–1253 in [joi170166supp2_prod.pdf — PDF p. 7](../joi170166supp2_prod.pdf#page=7); Figure 3 age groups in [jama_huffman_2018_oi_170166.pdf — PDF p. 9](../jama_huffman_2018_oi_170166.pdf#page=9); prespecified subgroup methods in [jama_huffman_2018_oi_170166.pdf — PDF p. 3](../jama_huffman_2018_oi_170166.pdf#page=3).

**Source evidence:** SAP: age <65 years and >65 years. Figure 3: <50, 50–69, ≥70. Intervention denominators 2079, 6606, 2623; control 2045, 5863, 2158.

**Reported-versus-comparator:** Two groups separated at 65 versus three groups separated at 50 and 70, with concrete reported subgroup denominators.

**Reasoning procedure:** Compare the numerical partition and prespecification label. Check reported totals independently; do not infer a protocol violation from an absent amendment.

**Calculation:** 2079+6606+2623=11308; 2045+5863+2158=10066. Totals reconcile, while a 60-year-old and 68-year-old fall in different SAP groups but the same reported 50–69 group.

**Alternative source-grounded interpretations:** An additional prespecification or amendment could support the reported partition. The SAP's exact-age-65 omission has no supplied participant count and is not separately registered.

**Mechanical evidence recheck:** Direct source confirms both partitions and the report's prespecified framing. The mismatch is quantitative population labeling, not a general design critique. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Subgroup effect extraction needs the correct age boundaries and plan reference.

**Potential downstream evidence impact:** If confirmed, an extractor could misidentify the reported subgroup definitions as those in the supplied SAP.

**Human verification steps:** Inspect the SAP section, methods and Figure 3; obtain any amendment or additional plan. Which prespecification supports <50/50–69/≥70?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — SAP four crossover periods versus five-cohort schedule

**Status:** Pending Human Adjudication

**Candidate statement:** The SAP schedules five intervention crossovers but states that a cohort crosses in each of four time periods.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP p. 3 five-crossover schedule vs PLAN SAP p. 4 four-period statement

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** design lines 1091–1105 and schedule diagram in [joi170166supp2_prod.pdf — PDF p. 3](../joi170166supp2_prod.pdf#page=3); randomization lines 1123–1124 in [joi170166supp2_prod.pdf — PDF p. 4](../joi170166supp2_prod.pdf#page=4).

**Source evidence:** Five cohort/step crossovers occur at 4, 8, 12, 16, 20 months. The randomization wording says “one cohort of hospitals … in each of the four time periods.”

**Reported-versus-comparator:** Five specified crossover dates versus four-period wording within the same PLAN.

**Reasoning procedure:** Count the scheduled intervention starts and compare the scope of the period statement. The main five-step description is corroboration, not a second discrepancy relationship.

**Calculation:** Five distinct dates minus four stated periods equals one; exact integer tolerance is zero.

**Alternative source-grounded interpretations:** The first crossover might be counted separately from four subsequent periods, or the wording may reflect an earlier plan version; the sentence does not specify that convention.

**Mechanical evidence recheck:** Direct layout confirms five dates and four-period wording. The intended period definition remains a recorded human question. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** A quantitative rollout description should identify the same period-count convention.

**Potential downstream evidence impact:** If confirmed, reconstruction of the planned rollout could use four rather than five crossover occasions.

**Human verification steps:** Read both SAP locations and establish whether the four periods exclude the first crossover. Which period convention is intended?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Five-percent dropout allowance gives less than15000 retained

**Status:** Pending Human Adjudication

**Candidate statement:** The stated 5% dropout allowance is additive padding; it falls short of exact retention of 15000 if loss is 5% of recruited participants.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p. 18 target and dropout allowance vs PLAN protocol p. 18 retention implication; PLAN SAP p. 4 repeats both

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The exact retained-target premise, denominator and rounding convention are unspecified; all substantive comparisons are PLAN.

**Exact source locations:** section 8.2, lines 573–579 in [joi170166supp1_prod.pdf — PDF p. 18](../joi170166supp1_prod.pdf#page=18); repeated in sample-size lines 1113–1116 in [joi170166supp2_prod.pdf — PDF p. 4](../joi170166supp2_prod.pdf#page=4); corroborating 15750/5% sample-size statement in [jama_huffman_2018_oi_170166.pdf — PDF p. 3](../jama_huffman_2018_oi_170166.pdf#page=3).

**Source evidence:** PLAN target 15000 increased to 15750 “to account for up to 5% drop out between discharge and 30-day follow-up.”

**Reported-versus-comparator:** 15750 recruitment target versus the total needed to retain exactly 15000 after a 5% recruitment-denominator loss; this retention premise is conditional.

**Reasoning procedure:** State the exact-retained-target and dropout-denominator assumptions before applying retention arithmetic. Do not infer a clustered-power failure or achieved-sample deficit.

**Calculation:** 15750×0.95=14962.5; 15000/0.95=15789.4737, requiring 15790 as an integer gross target. Printed 15750=15000×1.05. Conditional expected shortfall is 37.5 retained participants.

**Alternative source-grounded interpretations:** 15000 may be rounded or approximate, and additive 5% contingency may be intentional. The exact retained power target and full power calculation are not supplied.

**Mechanical evidence recheck:** Direct PLAN readings confirm 15000, 15750 and 5%. The conditional arithmetic reproduces; exact retention intent remains unresolved. Main corroboration adds no P_R. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Allowance reporting should distinguish additive padding from retention adjustment.

**Potential downstream evidence impact:** If confirmed, a reader reproducing the planning calculation could use the wrong inflation rule; no actual power or conclusion effect is established.

**Human verification steps:** Confirm whether 15000 is exact retained n or an approximate planning target and which denominator defines 5% loss. Was additive contingency intended?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C016 — Complete/missing follow-up table difference footnote names treatment arms

**Status:** Pending Human Adjudication

**Candidate statement:** eTable 1 compares complete versus missing follow-up, but its difference footnote names intervention minus control.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 1 follow-up-status headers vs REPORT results supplement eTable 1 treatment-arm footnote

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** eTable 1 complete/missing headers, age/male rows and footnote a in [joi170166supp3_prod.pdf — PDF p. 17](../joi170166supp3_prod.pdf#page=17).

**Source evidence:** Complete Follow Up n=21079; Missing Follow Up n=295. Age 60.6 versus 60.0, difference −0.6; male 75.8% versus 71.2%, difference −4.6. Footnote: “Difference=intervention minus control.”

**Reported-versus-comparator:** Follow-up-status columns and missing-minus-complete arithmetic versus a treatment-arm contrast definition.

**Reasoning procedure:** Check column identities before numeric direction. The discrepancy is reference-group labeling, rather than a separate candidate for each row.

**Calculation:** 60.0−60.6=−0.6; 71.2−75.8=−4.6 percentage points. These displayed differences match missing minus complete; rounding does not turn the column identities into treatment arms.

**Alternative source-grounded interpretations:** An unshown treatment-stratified contrast is conceivable, but no such analysis is described for the displayed two follow-up populations.

**Mechanical evidence recheck:** Direct layout/raster confirm headers, examples and footnote. The contrast-label question reproduces. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** An effect difference should identify its actual reference populations.

**Potential downstream evidence impact:** If confirmed, an extractor could incorrectly treat a missingness comparison as an intervention-control contrast.

**Human verification steps:** Inspect the full table and footnote. Should the definition name missing-follow-up minus complete-follow-up, and is any separate contrast intended?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C017 — Registered lost-follow-up discrepancy not reproduced

**Status:** Pending Human Adjudication

**Candidate statement:** The registered lost-follow-up discrepancy is not reproduced: correctly read Figure 1 losses sum to 295, matching the prose.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 1 lost-follow-up boxes vs REPORT main article p. 6 incomplete-outcome total

**Review domain:** statistical_results

**Evidence state:** not_reproduced

**Suggested review disposition:** exclude

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Figure 1 all 20 lost-follow-up boxes, especially cohort 2 step 5, and caption in [jama_huffman_2018_oi_170166.pdf — PDF p. 4](../jama_huffman_2018_oi_170166.pdf#page=4); outcome completeness prose in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6); corroborating eTable 1 missing/complete totals in [joi170166supp3_prod.pdf — PDF p. 17](../joi170166supp3_prod.pdf#page=17).

**Source evidence:** Authoritative cohort 2 step 5 count is 28, not the historical locator input 8. Control losses: 42,45,54,27,2. Intervention: cohort 1 2,6,0,3,10; cohort 2 18,4,6,28; cohort 3 10,8,7; cohort 4 7,7; cohort 5 9. Prose: 295 incomplete outcomes, comprising 215 site-not-followed and 80 unreachable.

**Reported-versus-comparator:** Corrected Figure 1 total 295 versus narrative 295. Historical 275 arose from reading 28 as 8 and is explicitly superseded.

**Reasoning procedure:** Use direct current PDF text and raster as authority, then sum disjoint boxes. Preserve the stable ID as a recheck record rather than present the historical mismatch as a live finding.

**Calculation:** Control=170; intervention=21+56+25+14+9=125; total=295. 215+80=295; 21374−295=21079, matching eTable 1.

**Alternative source-grounded interpretations:** No residual count contradiction remains under the registered rule. A missingness-category explanation is unnecessary once the source input is corrected.

**Mechanical evidence recheck:** Direct source explicitly disproves the registered 275-versus-295 comparison. Evidence state is not_reproduced; exclude is only the mechanical human-review pre-fill. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** This card documents correction of a locator transcription and prevents its reappearance as an apparent paper discrepancy.

**Potential downstream evidence impact:** The original false 275 total should not be carried into downstream extraction. No confirmed reporting defect or resulting harm is identified here.

**Human verification steps:** Read cohort 2 step 5 as 28, recalculate all losses and compare 295/21079 with prose/eTable 1. Human adjudication should review the preserved not-reproduced record.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C018 — Door-to-balloon comparison uses unsupported estimand alignment

**Status:** Pending Human Adjudication

**Candidate statement:** The registered door-to-balloon numerical comparison relies on an unsupported assumption that two adjusted columns have equal estimands and scales.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 door-to-balloon difference entry vs REPORT main article Table 2 beta entry and shared definition

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The unresolved issue is unsupported estimand/scale alignment, not uncertain REPORT role.

**Exact source locations:** Table 2 door-to-balloon row, both adjusted columns and footnotes b/c in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** Difference,% 6.18 (−4.78 to 17.14); beta 13.00 (3.64–22.36); control median 65 min and intervention 77 min. Footnote b defines odds ratios/beta by intervention-minus-control marginal differences; c identifies beta.

**Reported-versus-comparator:** The printed 6.18 and 13.00 are correct transcriptions, but the source does not establish that their columns should be numerically equal.

**Reasoning procedure:** Audit alignment before comparing points or intervals. Shared row/model context and a beta definition do not establish the first column's estimand, transform or variance.

**Calculation:** 13.00−6.18=6.82 is only a conditional diagnostic if equal untransformed contrasts were established. The necessary equality premise is unsupported; no same-test CI contradiction follows.

**Alternative source-grounded interpretations:** 6.18 may be a normalized percentage or distinct marginal summary, and 13.00 a minute coefficient. Different coherent estimands could explain the numbers.

**Mechanical evidence recheck:** Source values match, but equal-estimand input alignment is unsupported. Evidence state record_input_error pre-fills discuss; a residual numeric discrepancy cannot be settled. C004 separately retains the printed scale question. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** This card makes an unsupported comparison premise explicit rather than asserting an effect-estimate error.

**Potential downstream evidence impact:** Without column definitions, a reviewer could compare incompatible time effects. No demonstrated numeric reporting contradiction remains from this registered comparison.

**Human verification steps:** Obtain each column's estimand, scale, normalization denominator, marginalization and interval construction. Do they represent the same contrast at all?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C019 — Door-to-needle comparison uses unsupported estimand alignment

**Status:** Pending Human Adjudication

**Candidate statement:** The registered door-to-needle numerical comparison rests on an unsupported equal-estimand assumption for two adjusted columns.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 door-to-needle difference entry vs REPORT main article Table 2 beta entry and shared definition

**Review domain:** statistical_results

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** Column estimand/scale mapping is absent; both compared locations are REPORT.

**Exact source locations:** Table 2 door-to-needle row, both adjusted columns and footnotes b/c in [jama_huffman_2018_oi_170166.pdf — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** Difference,% 0.40 (−5.23 to 6.03); beta 5.00 (−5.20–15.20); control median 44 min and intervention 45 min. Footnote defines beta but supplies no mapping that equates both columns.

**Reported-versus-comparator:** Correctly transcribed 0.40 and 5.00 versus an unestablished same-contrast identity.

**Reasoning procedure:** Read column-specific definitions before subtraction or inference. Shared context does not establish equivalent marginalization, transform, variance or units.

**Calculation:** 5.00−0.40=4.60 only under an unsupported equal-scale/equal-estimand premise. Both intervals include zero; no P value is reconstructed.

**Alternative source-grounded interpretations:** One column may summarize a percentage/marginal effect and the other a minute coefficient, allowing coherent different values.

**Mechanical evidence recheck:** Direct source confirms numbers but not the equality premise. record_input_error pre-fills discuss; residual numeric inconsistency remains unsettled. C005 independently addresses the label-definition question. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Unsupported alignment must be visible before assessing numeric consistency.

**Potential downstream evidence impact:** A reviewer lacking the mapping could compare different measures or extract a time effect under an assumed scale. No confirmed numeric conflict is established here.

**Human verification steps:** Request both formulas, units, estimands, transformations and interval construction. Is numerical equality a valid comparison rule for these columns?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C020 — Key Points duplicates negation in the statistical-significance statement

**Status:** Pending Human Adjudication

**Candidate statement:** Key Points duplicates negation in its significance statement, whereas the abstract and primary-results prose state nonsignificance once.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article p. 2 Key Points negation vs REPORT main article pp. 1 and 7 nonsignificance statements

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** None

**Exact source locations:** Key Points Findings in [jama_huffman_2018_oi_170166.pdf — PDF p. 2](../jama_huffman_2018_oi_170166.pdf#page=2); abstract Results in [jama_huffman_2018_oi_170166.pdf — PDF p. 1](../jama_huffman_2018_oi_170166.pdf#page=1); primary adjusted-result paragraph in [jama_huffman_2018_oi_170166.pdf — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** Key Points: “a difference that did not reach not statistical significance after adjustment for cluster and temporal trends.” Abstract: “was not statistically significant after adjustment”; primary text: “was not statistically significant after further adjustment for temporal trends.” Matched primary RD −0.09% (−1.32 to 1.14), OR 0.98 (0.80–1.21).

**Reported-versus-comparator:** Two negations in Key Points versus a single nonsignificance statement for the matched result elsewhere.

**Reasoning procedure:** Compare the printed statistical interpretation, not reconstructed significance. The duplicated word can obscure the intended meaning while the surrounding result remains coherent.

**Calculation:** No numeric recalculation is necessary. “did not” plus “not statistical significance” supplies the duplicated-negation observation.

**Alternative source-grounded interpretations:** An accidental extra “not” is consistent with the nonsignificant abstract, primary prose and Key Points Meaning. Intended editorial wording remains the human question.

**Mechanical evidence recheck:** Direct text and fresh raster confirm the duplicated wording. The editorial statistical-interpretation question reproduces without evidence that the result is significant. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** Statistical interpretation should be clear in the concise results summary.

**Potential downstream evidence impact:** If confirmed, a secondary summary could quote an ambiguous significance sentence; no changed conclusion is established.

**Human verification steps:** Compare all three passages and confirm the intended edited statement. Does the duplicated negation accurately express the same nonsignificance?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C021 — residual subtraction label and directional caption differ

**Status:** Pending Human Adjudication

**Candidate statement:** The residual index names expected minus observed, while the directional caption describes negative residuals as lower-than-mean MACE; their compatibility depends on the unreported residual reference and formula.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement p. 1 expected-minus-observed index vs REPORT results supplement p. 24 residual direction caption

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The substantive comparators occur within one REPORT document, giving S_W. Corroborating-only source content adds no S_C or P_R. The review domain follows the category in the classification table. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** Common residual formula/reference is conditional; both comparators are REPORT parts of the same mixed bundle.

**Exact source locations:** index eFigure 1A line in [joi170166supp3_prod.pdf — PDF p. 1](../joi170166supp3_prod.pdf#page=1); eFigure 1A axis and explanatory caption in [joi170166supp3_prod.pdf — PDF p. 24](../joi170166supp3_prod.pdf#page=24).

**Source evidence:** Index: “Residual of 30-Day Major Adverse Cardiovascular Event Rate (Expected – Observed) by Individual Hospitals.” Caption describes cluster/time-adjusted model predictions, zero as mean MACE reference, negative/left hospitals as lower than mean and positive/right hospitals as higher. Axis runs approximately −3 to 2.

**Reported-versus-comparator:** Expected−observed subtraction wording versus negative-below-reference/positive-above-reference direction under a common reference.

**Reasoning procedure:** Compare signs algebraically only after stating the common-reference assumption. Do not infer exact hospital rates or diagnose model output from raster coordinates.

**Calculation:** If O<E for common expected/reference E and observed O, E−O>0; the caption instead assigns negative residuals to lower-rate hospitals. If O>E, E−O<0 while the caption assigns positive.

**Alternative source-grounded interpretations:** A fitted hospital random effect on log-odds scale, hospital-specific expectation, or different residual definitions could explain the caption. Formula, link scale, inclusion of random effects and expected reference are absent.

**Mechanical evidence recheck:** Direct source index/layout and source raster/caption confirm the wording and direction. The conditional definition question remains recorded, not a proven residual-model error. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** A residual graphic needs a consistent sign and reference definition.

**Potential downstream evidence impact:** If confirmed, an extractor could reverse residual direction or equate unlike residual measures when interpreting hospital variation.

**Human verification steps:** Read index and caption together; request the plotted residual formula, scale and reference. Which description correctly identifies the plotted quantity?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C022 — STEMI/NSTEMI composite has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample STEMI/NSTEMI composite performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 6 measure 1 three-month heading and labels vs PLAN toolkit p. 6 measure 1 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 1, STEMI/NSTEMI composite, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 6](../joi170166supp3_prod.pdf#page=6).

**Source evidence:** Three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific 11-measure composite panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Distinguish a fourth plotted time position from a disagreement in the correctly aligned first three scores. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 1's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The STEMI/NSTEMI composite sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 1 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C023 — STEMI composite has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample STEMI composite performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 6 measure 2 three-month heading and labels vs PLAN toolkit p. 6 measure 2 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 2, STEMI composite, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 6](../joi170166supp3_prod.pdf#page=6).

**Source evidence:** Three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific separate STEMI composite panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Distinguish a fourth plotted time position from a disagreement in the correctly aligned first three scores. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 2's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The STEMI composite sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 2 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C024 — NSTEMI composite has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample NSTEMI composite performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 6 measure 3 three-month heading and labels vs PLAN toolkit p. 6 measure 3 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 3, NSTEMI composite, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 6](../joi170166supp3_prod.pdf#page=6).

**Source evidence:** Three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific eight-measure NSTEMI composite panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Distinguish a fourth plotted time position from a disagreement in the correctly aligned first three scores. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 3's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The NSTEMI composite sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 3 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C025 — Discharge-AMI composite has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample Discharge-AMI composite performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 7 measure 4 three-month heading and labels vs PLAN toolkit p. 7 measure 4 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 4, Discharge-AMI composite, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 7](../joi170166supp3_prod.pdf#page=7).

**Source evidence:** Three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific six-discharge-measure composite panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Distinguish a fourth plotted time position from a disagreement in the correctly aligned first three scores. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 4's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The Discharge-AMI composite sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 4 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C026 — Arrival-aspirin graph has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample Arrival-aspirin performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 7 measure 5 three-month heading and labels vs PLAN toolkit p. 7 measure 5 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 5, Arrival-aspirin, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 7](../joi170166supp3_prod.pdf#page=7).

**Source evidence:** Rolling-three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific arrival aspirin, excluding transfers in and out panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Prior observations may underlie a rolling score, but they do not identify an additional displayed window-end date. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 5's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The Arrival-aspirin sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 5 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C027 — Discharge-aspirin graph has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample Discharge-aspirin performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 7 measure 6 three-month heading and labels vs PLAN toolkit p. 7 measure 6 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 6, Discharge-aspirin, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 7](../joi170166supp3_prod.pdf#page=7).

**Source evidence:** Rolling-three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific discharge aspirin panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Prior observations may underlie a rolling score, but they do not identify an additional displayed window-end date. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 6's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The Discharge-aspirin sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 6 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C028 — Discharge-beta-blocker graph has an additional timeline point

**Status:** Pending Human Adjudication

**Candidate statement:** The sample Discharge-beta-blocker performance panel shows four green time positions for three named October–December 2014 periods; the fourth position lacks a date/window.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN toolkit p. 8 measure 7 three-month heading and labels vs PLAN toolkit p. 8 measure 7 four plotted time positions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All substantive comparators belong to prospective plan or illustrative operational content. P_P therefore derives plan_material; these sample/plan values are not achieved trial results. Corroboration from REPORT content, where noted, adds no discrepancy relationship. The suggested disposition is a mechanical pre-fill, not a human adjudication.

**Classification ambiguity:** The fourth point's date, reporting window and illustrative/template status are missing definitions; operational PLAN role is supported.

**Exact source locations:** Measure 7, Discharge-beta-blocker, right performance panel, heading, month labels and green My Hospital series in [joi170166supp3_prod.pdf — PDF p. 8](../joi170166supp3_prod.pdf#page=8).

**Source evidence:** Rolling-three-month performance heading names Oct 2014–Dec 2014. Three assigned scores 87.6%, 93.4%, 94.7% align with October, November, December. Four green markers occupy distinct time positions; the fourth is beyond December and above the 98% tick, without a printed date. No exact fourth score is asserted.

**Reported-versus-comparator:** Four plotted positions versus three assigned month labels in this specific discharge beta-blocker sample metric panel. December 94.7% aligns correctly with the third point.

**Reasoning procedure:** Count this panel's markers and named periods independently. Prior observations may underlie a rolling score, but they do not identify an additional displayed window-end date. Repeated example values alone are not the candidate.

**Calculation:** 4 positions−3 named periods=1 additional unlabeled position; exact counting tolerance is zero. Raster height is used only qualitatively, not to fabricate the fourth value.

**Alternative source-grounded interpretations:** An extra historical/future period, forecast, separately dated rolling window or template artifact could explain the fourth point. The package does not provide its date or role.

**Mechanical evidence recheck:** Fresh direct-source raster confirms measure 7's four positions and three named months. The missing fourth-window definition remains a recorded conditional question. This sample PLAN panel is not an achieved trial outcome. The [complete recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md) preserve the source-authority, input-availability and observation-versus-inference facts for this stable ID.

**Quality-control relevance:** The Discharge-beta-blocker sample series needs identifiable time positions and window definitions.

**Potential downstream evidence impact:** If confirmed, operational reuse of this specific panel could attach its fourth point to an assumed date or conflate sample windows. No effect on trial results or actual propagation is established.

**Human verification steps:** Inspect measure 7 separately; count green markers, verify the first three score/month alignments and obtain every window's dates. What period or template function does the fourth point represent?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If human review confirms a reporting issue, a later extractor could carry forward a disputed endpoint, effect-measure definition, subgroup boundary, missingness contrast, unit or reporting window. Small preventable defects can therefore warrant proofreading attention even when they do not affect a study conclusion. Conditional sample/PLAN observations should remain distinct from achieved trial results.

This report does not establish that any candidate entered a systematic review, meta-analysis, guideline or later publication. It does not infer serious harm, a change in conclusions or a paper-level validity judgment. C017 specifically documents a disproven registered mismatch; C018/C019 document unsupported alignment rather than established numerical contradictions.

## Limitations and Missing Definitions

All 80 source pages are mapped; the limitations concern interpretation or reconstruction precision. The complete [limitations record](review_1_6/limitations.md) identifies these bounds:

- Figure points and interval endpoints without printed labels remain approximate; raster readings cannot supply exact unprinted values. Tiny illustrative toolkit percentile ticks also limit transcription precision.
- Variable-specific measurement/eligibility denominators are not always explicit. Missing gender categories, common bar denominators and fourth-point dates/window definitions are human questions.
- CI/test/SE/variance/covariance construction and compatible model rules are insufficient for some formal interval/P-value reconstructions. Diagnostic algebra does not replace the reported analysis.
- Time-column estimands, normalization, marginalization and percent-change denominators are missing. C018/C019 cannot support an equal-estimand comparison until those definitions are supplied.
- Residual formula, scale, model link and expected reference are not fully specified. C021 is conditional on common-reference alignment.
- C015 assumes an exact retained target and recruitment-denominator dropout only for its diagnostic; rounding or additive padding may explain the planning numbers. C013 may have a supporting prespecification/amendment outside the supplied package.
- Toolkit graphics are illustrative prospective operational content. Their observed labeling questions do not establish trial-outcome errors.
- Tesseract and Office conversion tools are absent. Source-bound reusable OCR/images and direct PDF tools close every affected PDF unit; no Office source exists and no fallback installation was needed.

Only supplied evidence was available. No raw data, undisclosed model output or outside amendment was sought. Missing definitions remain named rather than filled by assumptions.

## Human Adjudication Checklist

1. Read each cited PDF page directly and confirm endpoint, population, time, model, measure and reference alignment.
2. Review the calculation and its explicit assumptions; obtain the named missing definition where applicable.
3. Consider the source-grounded alternatives before deciding whether a reporting change is needed.
4. Review C017 with corrected 28/295 inputs, and C018/C019 as unsupported comparison records. Do not reinstate their historical premises.
5. Decide validity, importance and action independently of mechanical retain/exclude/discuss pre-fills; fill initials and notes. All five fields remain `__` in every card until human review.
6. If a correction is supported, identify the exact source wording/value and update any extraction record explicitly. This report prescribes no final source correction.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Local tooling and provenance

The [tooling record](review_1_6/tooling_record.md) documents Linux, Python 3.13.5 for supplied auxiliary helpers, direct Poppler 25.03.0 PDF information/text/rendering and direct sha256sum hashing. Pandoc 3.1.11.1 is available for standalone HTML rendering by the coordinator. The review ran CPU-only, installed no packages and created no fallback environment; removal status is NOT_CREATED. Derivative engines, commands and source locations are recorded in the asset, mapping and recheck artifacts.

The [routing preflight](review_1_6/routing_preflight.md) records PASS for current coordinator inference, INTERACTIVE_CLI operation, the fixed gpt-6.1-sol model/effort matrix and all nine named presets. The current provider was retained by explicit user instruction. The session continuation is recorded truthfully rather than asserting a different provider or launch command.

### Source and reused-artifact integrity

All four supplied PDFs and all 78 selected reusable assets have identical before/after SHA-256 records. Before-hash manifests are [sources](review_1_6/source_hashes_before.sha256) and [reused artifacts](review_1_6/reused_artifact_hashes_before.sha256); after-hash manifests are [sources](review_1_6/source_hashes_after.sha256) and [reused artifacts](review_1_6/reused_artifact_hashes_after.sha256). Direct cmp comparisons returned equality for both manifests. Sources and legacy audit artifacts remain preserved. HTML rendering and validation are mechanical completion checks.

### Validation provenance

The [validation override record](review_1_6/validation_override.md) documents that the supplied validator hardcodes an OpenRouter provider string and a particular launcher string, while the user expressly authorized the current provider/session. A preserved local copy adapts only those two routing provenance expectations. Scientific scope, classification, agent/model, evidence-link, hash, tooling and performance checks are unchanged.

The reproducible validation sequence runs the supplied unmodified validator and preserves its result in [the original routing result](review_1_6/review_validation_original.json), then runs the documented user-override-aware copy to produce [the final validation record](review_1_6/review_validation.json). This report does not claim that the unmodified routing expectations match the user's override. The final record supplies the completion status; validator output is a mechanical completion record, not human adjudication.

### Complete agent execution record

The following table copies every actual runtime in the [execution manifest](review_1_6/agent_execution_manifest.md). Artifact paths in the table are relative to review_1_6. Canonical task IDs omit their leading slash only for validator syntax. Every mandatory specialist is a distinct fresh spawn; additional disjoint audit/statistical shards also have fresh IDs. No role was promoted or reused for a different mandatory stage.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support | root/statistics_pass_1_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2_main_a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_b | root/statistics_pass_2_main_b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_main_b.md |
| statistics_pass_2_support | root/statistics_pass_2_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support.md |
| quality_support_coverage_auditor | root/quality_support_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/support_relationship_coverage_audit.md |
| quality_main_coverage_auditor | root/quality_main_coverage | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/main_relationship_coverage_audit.md |
| quality_control_auditor | root/quality_control_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

- **Target basis:** Four PDFs and 80 unique physical pages; 79 units have usable reusable text or source-bound images, one protocol graphic requires fresh visual mapping. The mixed protocol/SAP/results/toolkit package includes 14 scanned OCR-image units and dense main/supplement tables, requiring complete numeric, cross-source, two statistical, recheck, audit, and report stages across dependent agent waves; no fresh OCR or Office conversion is needed.
- **Total source units:** 80
- **Fresh-source units:** 1
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T00:43:38Z
- **Finished UTC:** 2026-10-11T01:25:13Z
- **Observed elapsed minutes:** 41.58
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Additional disjoint statistical and coverage-audit shards were required by the 200000-character and 120-relationship context bounds; source-raster corrections were propagated through the complete ledger and second pass; all 28 complete evidence cards required full report assembly. No coverage or candidate was omitted to meet the target.

The coordinator finalized the finish time, observed duration, target status and bounded exceedance causes immediately after complete Markdown assembly and copied those exact values from run_state.md. The package-specific target is a planning range and never limits coverage or candidate retention. HTML rendering and mechanical validation occur outside the observed review interval unless a later model repair requires updating its finish time.

