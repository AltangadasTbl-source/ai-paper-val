# Quantitative Quality-Control Consistency Review — STOP-PD II Paper Package

**Pending Human Adjudication — all 15 stable candidates.** Evidence states and suggested review dispositions describe mechanical review records. Human reviewers decide validity, importance and action; all adjudication fields remain blank.

# Executive Quality-Control Summary

Workflow 1.6 reviewed all **63 physical PDF pages across four supplied sources** and registered **15 distinct quality-control candidates**. Fourteen have the evidence state `recorded_candidate`, including conditional observations awaiting named definitions. One, C009, has `record_input_error`: its initial graphical comparison assumes a model-to-plot estimand alignment that the package does not establish. C009 remains fully documented for human discussion.

The observations concern printed percentages and totals, scale footnotes and units, prospective targets and durations, historical denominator framing, and a report-versus-plan numerical endpoint definition. The report does not establish incorrect trial conclusions. Small preventable reporting defects can matter when numbers or definitions are copied into downstream evidence extraction, but actual propagation, conclusion change and harm are not demonstrated here.

Discovery restarted from supplied evidence without a finding limit. All assigned stable IDs are preserved. Separate total-cholesterol and LDL outcomes remain C007 and C008 even though their displayed inputs coincide. Current-run extraction and calculation repairs are documented separately in the quality audit and do not become paper candidates.

# Package and Reused-Evidence Provenance

| Source ID | Supplied source and truthful first-page link | Content role | Physical pages |
|---|---|---|---:|
| DOC-001 | [jama_flint_2019_oi_190079.pdf](../jama_flint_2019_oi_190079.pdf#page=1) | REPORT: main article | 10 |
| DOC-002 | [joi190079supp1_prod.pdf](../joi190079supp1_prod.pdf#page=1) | PLAN: protocol, data analytic plan and pharmacotherapy appendix; historical data retain PLAN role | 42 |
| DOC-003 | [joi190079supp2_prod.pdf](../joi190079supp2_prod.pdf#page=1) | REPORT: cover and nine results eFigures | 10 |
| DOC-004 | [joi190079supp3_prod.pdf](../joi190079supp3_prod.pdf#page=1) | PLAN: prospective data-access conditions; administrative role ambiguity retained | 1 |

Two REPORT sources contain 20 pages; two PLAN sources contain 43 pages. No Office, workbook, CSV, participant-level dataset or additional direct source is supplied. Full inventories are [source inventory](review_1_6/source_inventory.md) and [evidence assets](review_1_6/evidence_asset_inventory.md).

The eligible reused inventory contains 187 immutable assets: 143 USABLE and 44 PARTIAL. Partial figure text is complemented by source-matched rendered images, so the union covers every source page. Legacy native/rendered evidence originated from PyMuPDF, with historical versions unavailable; existing OCR originated from rapidocr-cuda and was reused only as text. Current review did not invoke a GPU. Protocol and administrative native/layout text were source-matched using Poppler 26.01.0. Extraction-only maps supplied locations, without importing old candidate selection, classifications, checker decisions or reports.

Every registered source observation was subsequently checked against its exact supplied PDF page. The fresh evidence rechecker extracted 24 distinct pages and visually inspected seven fresh renders. Text and OCR remained transcription aids; PDF content was final authority. [Evidence recheck](review_1_6/verification/evidence_recheck.md) records commands and page-specific facts.

# Scope, Complete Coverage, and Exclusions

| Source | Total units | Reusable units | Fresh-required units | Newly mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 42 | 42 | 0 | 42 | COMPLETE |
| DOC-003 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 63 | 63 | 0 | 63 | COMPLETE |

Reusable plus fresh-required units equals total for each source; mapped equals total. Zero fresh-required units refers to initial extraction availability, not absence of new scientific mapping or direct-source confirmation. Covers, references, historical plan results and administrative pages were inspected and explicitly mapped, including units with no applicable quantitative result. [Source coverage](review_1_6/source_coverage.md) and [coverage manifest](review_1_6/coverage_manifest.md) preserve disjoint assignments and one artifact path per row.

The scope prioritizes arithmetic, denominators, inferential reporting, cross-document numeric matching, measure labels and scales, and rate-versus-count consistency. Population and analysis-unit questions qualify only when connected to a concrete printed quantitative relationship. Broad methodology, clinical judgment, novelty, misconduct, raw-data auditing and external literature were excluded. Missing model details alone did not create candidates. Coherent finite-precision display-zero P values are excluded under `DISPLAY_ZERO_NOT_CANDIDATE`; no supplied display-zero result generated a card.

# Quantitative and Statistical Relationship Coverage

The main mapper reconstructed 113 grouped quantitative match records plus definitions and 37 displayed inferential relationships. Support mappers covered all 53 remaining source pages, including prospective quantities, historical results and all nine result figures. The numeric checker processed 400 individually registered relationships N001–N400 in four disjoint origin shards of 96, 83, 105 and 116 records. Cross-source checking matched 70 families X001–X070. These lane counts overlap and must not be summed as a count of unique scientific relationships.

Both statistical passes independently covered all **108** registered relationships S001–S108: 37 main displayed inferential results, 25 historical/background results, nine graphical relationships, 12 power scenarios and 25 model or interpretation relationships. Pass 1 and pass 2 used different fresh high-effort agents. Pass 2 read the full cross-lane ledger and exact-source recheck facts; it emitted no genuinely new candidate requiring appended registration.

Checks included interval ordering and containment, positive ratio scales, direction and reference groups, matched repetitions, compatible labelled statistic-to-tail calculations, power-table bounds and matched scenario directions, and graphical unit/time/model correspondence. Holm-adjusted P values were distinguished from nominal tails reconstructed from marginal intervals. Model slopes were distinguished from raw changes and endpoint secants; historical and prospective populations remained separate. No unsupported covariance, degrees of freedom, link function, exact CI construction or simulation model was imposed.

Durable records: [main map](review_1_6/extraction/main_quantitative_evidence.md), [support map](review_1_6/extraction/support_quantitative_evidence.md), [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md), [numeric checks](review_1_6/checkers/numeric_consistency.md), [cross-source checks](review_1_6/checkers/cross_source_consistency.md), [statistical inventory](review_1_6/statistics/relationship_inventory.md), [pass 1](review_1_6/checkers/statistical_pass_1.md), [pass 2](review_1_6/checkers/statistical_pass_2.md), and [complete quality audit](review_1_6/quality/evidence_quality_audit.md).

# Document-Role Classification Summary

Content determines document role. REPORT presents study results; PLAN includes prospective operational material and historical/background results inside a plan. Primary relationship precedence is `P_R` > `P_P` > `S_C` > `S_W`. Corroboration alone does not create an additional discrepancy relationship.

| Primary relationship | Definition | Candidates |
|---|---|---:|
| S_W | Within one REPORT document | 7 |
| S_C | Between separate REPORT documents | 2 |
| P_P | Solely within PLAN material or plan versions | 5 |
| P_R | REPORT versus PLAN; does not establish a protocol violation | 1 |
| Total | | 15 |

| Derived review domain | Candidates |
|---|---:|
| statistical_results | 5 |
| report_internal_inconsistency | 4 |
| plan_material | 5 |
| protocol_report | 1 |
| Total | 15 |

| Evidence state | Candidates |
|---|---:|
| recorded_candidate | 14 |
| record_input_error | 1 |
| not_reproduced | 0 |
| repaired_residual | 0 |
| Total | 15 |

Suggested review dispositions are mechanical pre-fills: `recorded_candidate` and `repaired_residual` map to `retain`; `record_input_error` maps to `discuss`; `not_reproduced` maps to `exclude`. This ledger therefore has 14 retain and one discuss pre-fill, totaling 15. None is a human adjudication. C005 has both S_C and S_W, with S_C taking precedence. C004's PLAN and C011's REPORT only corroborate one side. C009's model description supports interpretation and adds no separate S_W discrepancy.

# Candidate Index

| Stable ID | Category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C002 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C003 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C004 | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | recorded_candidate |
| C005 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | recorded_candidate |
| C006 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C007 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C008 | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| C009 | Measure, label, or scale inconsistency | S_C | report_internal_inconsistency | record_input_error |
| C010 | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C011 | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| C012 | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| C013 | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| C014 | Numeric or arithmetic inconsistency | P_P | plan_material | recorded_candidate |
| C015 | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |

# Candidate Evidence Cards

Classification strings below reproduce the [stable ledger](review_1_6/candidate_ledger.md) exactly. Each calculation is a diagnostic comparison under its stated rule, not a prescribed final correction.

## C001 — Hyperlipidemia percentages do not reconcile with arm denominators

**Pending Human Adjudication.**

**Candidate statement:** The hyperlipidemia percentages do not reproduce the printed arm denominators.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table1 arm headers vs hyperlipidemia cells

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** One REPORT table; S_W; denominator category derives statistical_results.

**Classification ambiguity:** Unprinted row denominator or arm assignment.

**Exact source locations:** [Main PDF p.5, Table 1](../jama_flint_2019_oi_190079.pdf#page=5), REPORT column headers and hyperlipidemia row.

**Source evidence:** Olanzapine n=64, hyperlipidemia 18 (29.0%); placebo n=62, 19 (29.7%). No row-specific n or denominator footnote is supplied.

**Reported-versus-comparator:** The hyperlipidemia percentages do not reproduce the printed arm denominators. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Printed counts, percentages and headers conflict under the stated column denominators. Opposite denominators reproduce the numbers diagnostically, without establishing a production mechanism.

**Calculation:** 100×18/64=28.125%→28.1%; 100×19/62=30.645161%→30.6%. Printed percentages lie outside the ±0.05 percentage-point nearest-rounding tolerance. Using opposite denominators yields 18/62→29.0% and 19/64→29.7%.

**Alternative source-grounded interpretations:** A reduced olanzapine denominator 62 could explain one cell; placebo 29.7% with count 19 would require about 64, exceeding its n 62. Determine intended counts, arm placement and denominators. No correction is assigned.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C001 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of baseline hyperlipidemia prevalence, its arm assignment or denominator supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of baseline hyperlipidemia prevalence, its arm assignment or denominator into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: A reduced olanzapine denominator 62 could explain one cell; placebo 29.7% with count 19 would require about 64, exceeding its n 62. Determine intended counts, arm placement and denominators. No correction is assigned. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Placebo living-arrangement rows account for 60 of 62 participants

**Pending Human Adjudication.**

**Candidate statement:** The three displayed placebo living-arrangement counts total 60 under a header of 62; interpretation depends on exhaustiveness and missingness.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table1 placebo header vs living-arrangement categories

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Internal REPORT total/missingness comparison; S_W; statistical_results.

**Classification ambiguity:** Whether categories were intended as exhaustive.

**Exact source locations:** [Main PDF p.5, Table 1](../jama_flint_2019_oi_190079.pdf#page=5), REPORT placebo header and living-arrangement block.

**Source evidence:** Placebo n 62; with others 49 (79.0%), alone 10 (16.1%), senior residence 1 (1.6%). No other/missing category or reduced n is printed. Olanzapine 46+17+1=64 is a corroborating control.

**Reported-versus-comparator:** The three displayed placebo living-arrangement counts total 60 under a header of 62; interpretation depends on exhaustiveness and missingness. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** The listed category counts do not cover the header population. A complete partition is conditional because exhaustiveness and missingness are not explicitly defined.

**Calculation:** 49+10+1=60; deficit 62−60=2; displayed percentages sum 96.7%. Two participants are 3.225806% of 62. Individual percentages use 62 correctly; displayed rounding cannot remove the integer deficit.

**Alternative source-grounded interpretations:** Are the two participants missing/unlisted, was a count misprinted, and is 62 the intended percentage denominator? An intentionally incomplete category block could explain it, but needs a stated missingness definition.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C002 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of baseline living-arrangement distribution and missingness supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of baseline living-arrangement distribution and missingness into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Are the two participants missing/unlisted, was a count misprinted, and is 62 the intended percentage denominator? An intentionally incomplete category block could explain it, but needs a stated missingness definition. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — DKEFS color-word row carries a Barnes scale footnote

**Pending Human Adjudication.**

**Candidate statement:** The DKEFS color-word row is attached to a footnote describing a different construct and range.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table2 DKEFS row marker vs scale footnotes

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** One REPORT table; S_W; measure category derives report_internal_inconsistency.

**Classification ambiguity:** Intended marker placement.

**Exact source locations:** [Main PDF p.6, Table 2](../jama_flint_2019_oi_190079.pdf#page=6), REPORT DKEFS color-word row and footnotes h/i.

**Source evidence:** DKEFS color-word condition 3 means 8.6 (2.9) and 7.6 (2.8), superscript i. Footnote i names Barnes global akathisia range 0–5, higher worse. Footnote h defines both DKEFS tasks, scaled 1–19, higher better. The Barnes row lacks i.

**Reported-versus-comparator:** The DKEFS color-word row is attached to a footnote describing a different construct and range. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** A printed marker-to-measure conflict, not proof the cognitive values are incorrect. A displaced marker is a possible explanation.

**Calculation:** A row's measure/range must match its attached footnote. Means 8.6 and 7.6 exceed attached maximum 5 by 3.6 and 2.6; rounding cannot explain it. Both are inside DKEFS1–19.

**Alternative source-grounded interpretations:** Does h cover both DKEFS tasks, and is i intended for Barnes? Inspect original superscripts and intended scale associations.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C003 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the cognitive measure, its score range or direction supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the cognitive measure, its score range or direction into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Does h cover both DKEFS tasks, and is i intended for Barnes? Inspect original superscripts and intended scale associations. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — UKU criterion includes score 4 outside its stated range

**Pending Human Adjudication.**

**Candidate statement:** The UKU operational criterion includes score 4 although the same paragraph defines an item range ending at 3.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main UKU item range vs adverse-effect criterion

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Main range versus main rule is the discrepancy, S_W; corroborating PLAN does not create P_R. Domain report_internal_inconsistency.

**Classification ambiguity:** Unprinted recoding.

**Exact source locations:** [Main PDF p.4, tolerability paragraph](../jama_flint_2019_oi_190079.pdf#page=4), REPORT item range and operational rule. [Protocol PDF p.15](../joi190079supp1_prod.pdf#page=15) is PLAN corroboration only.

**Source evidence:** UKU range 0–3 on each of 48 items; adverse effect requires a 2-point increase or a score 3 or 4 with an increase from baseline. The plan names score 3.

**Reported-versus-comparator:** The UKU operational criterion includes score 4 although the same paragraph defines an item range ending at 3. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Internal scale/rule inconsistency. The extra unattainable branch may be operationally redundant, so adverse-event counts are not asserted wrong.

**Calculation:** Under declared integer codes {0, 1, 2, 3}, criterion 4 exceeds maximum 3 by 1. No disclosed recoding supplies 4.

**Alternative source-grounded interpretations:** Was there recoding to 1–4, surplus wording, or a different intended criterion? Confirm implemented codes and threshold.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C004 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the adverse-effect coding rule supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the adverse-effect coding rule into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Was there recoding to 1–4, surplus wording, or a different intended criterion? Confirm implemented codes and threshold. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — HbA1c model coefficient uses mg/dL while the outcome is percent

**Pending Human Adjudication.**

**Candidate statement:** The HbA1c daily coefficient is labeled mg/dL, while its named outcome is labeled percent in the main table and result figure.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main HbA1c coefficient vs main Table4 and REPORT results eFigure8 units

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Substantive within-main S_W and main-to-results-report S_C unit comparisons; S_C precedence; report_internal_inconsistency.

**Classification ambiguity:** Unprinted transformation.

**Exact source locations:** REPORT [Main PDF p.1 abstract](../jama_flint_2019_oi_190079.pdf#page=1), [p.7 secondary outcomes](../jama_flint_2019_oi_190079.pdf#page=7), [p.8 Table 4](../jama_flint_2019_oi_190079.pdf#page=8); REPORT [Results supplement p.9, eFigure 8](../joi190079supp2_prod.pdf#page=9).

**Source evidence:** Daily HbA1c coefficient−0.0002 mg/dL, 95%CI−0.0021 to 0.0016, adjusted P=.99 in narrative; abstract repeats mg/dL. Table 4 labels HbA1c, % and figure axis HbA1c(%), baseline around 5.9.

**Reported-versus-comparator:** The HbA1c daily coefficient is labeled mg/dL, while its named outcome is labeled percent in the main table and result figure. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Exact printed units conflict; the response transformation, if any, is not supplied. Figure slopes are optional diagnostic corroboration only.

**Calculation:** A slope for a percentage response retains percentage-point/time units absent a stated response conversion; mass concentration mg/dL is a different dimension. No numeric conversion is prescribed. Matching raw means to model coefficients is unnecessary for this printed-unit comparison.

**Alternative source-grounded interpretations:** Was a separate concentration-transformed response modeled, or what unit was intended for the daily estimate and CI? Raw change and model slope are different estimands but that alone does not explain a response-unit change.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C005 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the HbA1c daily coefficient and its outcome unit supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the HbA1c daily coefficient and its outcome unit into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Was a separate concentration-transformed response modeled, or what unit was intended for the daily estimate and CI? Raw change and model slope are different estimands but that alone does not explain a response-unit change. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Eleven of 34 hospitalizations is printed as 32.3%

**Pending Human Adjudication.**

**Candidate statement:** The explicit fraction 11 of 34 does not produce 32.3% under nearest one-decimal rounding.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main hospitalization count fraction vs printed percentage

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** S_W within REPORT; denominator category derives statistical_results.

**Classification ambiguity:** Unstated display convention.

**Exact source locations:** REPORT [Main PDF p.8, opening tolerability continuation](../jama_flint_2019_oi_190079.pdf#page=8); [p.7 Table 3](../jama_flint_2019_oi_190079.pdf#page=7) corroborates numerator 11.

**Source evidence:** Placebo 11 (32.3%) of 34 required psychiatric hospitalization because of relapse; adjacent olanzapine 6 (46.2%) of 13.

**Reported-versus-comparator:** The explicit fraction 11 of 34 does not produce 32.3% under nearest one-decimal rounding. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Explicit count fraction and percent differ under nearest rounding. Truncation could yield 32.3 but is not stated and differs from the adjacent display convention.

**Calculation:** 100×11/34=32.352941%→32.4% under nearest one-decimal rounding. Printed 32.3 differs 0.052941 percentage point, beyond±0.05. 6/13=46.153846%→46.2%.

**Alternative source-grounded interpretations:** Determine whether truncation was intentional or which printed count/percent should reconcile. No clinical consequence is inferred.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C006 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the hospitalization proportion among participants who relapsed supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the hospitalization proportion among participants who relapsed into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Determine whether truncation was intentional or which printed count/percent should reconcile. No clinical consequence is inferred. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Total-cholesterol unadjusted risk difference does not match counts

**Pending Human Adjudication.**

**Candidate statement:** The independently labeled total-cholesterol unadjusted difference does not reproduce its displayed counts under nearest rounding.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table5 total-cholesterol counts vs unadjusted difference

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** One REPORT table, S_W; statistical_results.

**Classification ambiguity:** Unprinted estimator/display rule. This remains distinct from LDL C008 because the outcome identity differs.

**Exact source locations:** REPORT [Main PDF p.9, Table 5 total-cholesterol row](../jama_flint_2019_oi_190079.pdf#page=9), arm headers and unadjusted-difference label.

**Source evidence:** Olanzapine 9 (14.1%)/64, placebo 6 (9.7%)/62; absolute unadjusted difference 4.3 percentage points, 95%CI−8 to 17.2. Qualifying threshold 240 mg/dL and above baseline.

**Reported-versus-comparator:** The independently labeled total-cholesterol unadjusted difference does not reproduce its displayed counts under nearest rounding. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Arithmetic from explicit unadjusted counts differs from printed point estimate; the separate CI is ordered and contains the estimate.

**Calculation:** 100×(9/64−6/62)=4.385080645 percentage points→4.4. Printed 4.3 lies 0.085080645 point away, beyond±0.05; printed 14.1−9.7=4.4. No CI method is assumed.

**Alternative source-grounded interpretations:** Was there deliberate truncation, a different denominator or a different estimator despite the unadjusted label? Identify the denominator/rounding rule used for this outcome.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C007 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the total-cholesterol incidence risk difference supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the total-cholesterol incidence risk difference into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Was there deliberate truncation, a different denominator or a different estimator despite the unadjusted label? Identify the denominator/rounding rule used for this outcome. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — LDL unadjusted risk difference does not match counts

**Pending Human Adjudication.**

**Candidate statement:** The independently labeled LDL unadjusted difference does not reproduce its displayed counts under nearest rounding.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table5 LDL counts vs unadjusted difference

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Internal REPORT arithmetic, S_W; statistical_results.

**Classification ambiguity:** Unprinted estimator/display rule. Shared numerical inputs do not erase the different LDL result identity.

**Exact source locations:** REPORT [Main PDF p.9, Table 5 LDL row](../jama_flint_2019_oi_190079.pdf#page=9), arm headers and unadjusted-difference label.

**Source evidence:** Olanzapine 9 (14.1%)/64, placebo 6 (9.7%)/62; difference 4.3 percentage points, 95%CI−8 to 17.2; LDL threshold 160 mg/dL and above baseline.

**Reported-versus-comparator:** The independently labeled LDL unadjusted difference does not reproduce its displayed counts under nearest rounding. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** This separately extractable LDL point estimate fails the same explicit count-difference rule; no participant identity or CI convention is inferred.

**Calculation:** 100×(9/64−6/62)=4.385080645 percentage points→4.4, outside 4.3±0.05. Printed group percentages subtract to 4.4. Identical counts with cholesterol are plausible and not an independent duplication candidate.

**Alternative source-grounded interpretations:** Which LDL-specific denominators, estimator and rounding rule produced 4.3 under the printed unadjusted heading?

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C008 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the separately labeled LDL incidence risk difference supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the separately labeled LDL incidence risk difference into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Which LDL-specific denominators, estimator and rounding rule produced 4.3 under the printed unadjusted heading? Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Weekly SAS points label and plotted trajectories require an estimand mapping

**Pending Human Adjudication.**

**Candidate statement:** The initial comparison of a weekly SAS coefficient with an approximate graphical secant assumes an unsupported estimand alignment. A residual reporting discrepancy cannot be settled from the supplied definitions.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main weekly SAS points label vs REPORT results eFigure9 score trajectories

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Main label versus separate REPORT result figure is S_C; main model wording only supports interpretation and adds no independently established S_W. Domain report_internal_inconsistency.

**Classification ambiguity:** Approximate figure and unprinted link/estimand mapping.

**Exact source locations:** REPORT [Main PDF p.7, extrapyramidal result](../jama_flint_2019_oi_190079.pdf#page=7); REPORT [Results supplement p.10, eFigure 9](../joi190079supp2_prod.pdf#page=10). [Main PDF p.4, Poisson model](../jama_flint_2019_oi_190079.pdf#page=4) continuing on [p.5](../jama_flint_2019_oi_190079.pdf#page=5) is a model locator/supporting definition, not an independent conflicting coefficient.

**Source evidence:** Weekly SAS change contrast 0.022 points, 95%CI0.009–0.036, adjustedP=.009; figure Week 0–36, SAS Total Score. Approximate means O.56→.73, P.685→.40. Model Poisson with overdispersion; link/back-transformation unprinted.

**Reported-versus-comparator:** The initial comparison of a weekly SAS coefficient with an approximate graphical secant assumes an unsupported estimand alignment. A residual reporting discrepancy cannot be settled from the supplied definitions. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Exact points label and axes versus approximate graphical diagnostic. Direct-source recheck cannot establish identical estimand and additive interpretation; the registered numerical comparison therefore has evidence state record_input_error and suggested review disposition discuss. A residual label discrepancy cannot be settled from supplied definitions. No significance or clinical conclusion is recomputed.

**Calculation:** Conditional additive-score diagnostic: [(0.73−0.56)−(0.40−0.685)]/36=.012639 points/week; ±.02 for each endpoint permits about.010417–.014861, separate from printed rounding interval.0215–.0225. Constant additive.022 over 36 weeks yields.792 points versus approximate plotted difference-of-changes.455. Log diagnostic [ln(.73/.56)−ln(.40/.685)]/36≈.0223/week; it is not proof of a supplied link.

**Alternative source-grounded interpretations:** Is.022 a link-scale coefficient, a marginal derivative at a particular time, or another transformed contrast? Obtain exact plotted means/link/reference population to reconcile the points label. Do not infer a log link merely from Poisson convention.

**Mechanical evidence recheck:** The fresh recheck found the coefficient, figure and model wording, but did not establish equality between an additive endpoint secant and the reported model estimand. This supersedes earlier lane wording suggesting an established mismatch. No log link, wrong coefficient, incorrect significance or proven residual unit defect is inferred. See the corresponding C009 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the scale and estimand assigned to the SAS coefficient supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the scale and estimand assigned to the SAS coefficient into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Is.022 a link-scale coefficient, a marginal derivative at a particular time, or another transformed contrast? Obtain exact plotted means/link/reference population to reconcile the points label. Do not infer a log link merely from Poisson convention. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Protocol acute recruitment is 82 versus 98 per site

**Pending Human Adjudication.**

**Candidate statement:** The plan prints 82 acute recruits per site in one passage and 98 per site in its target table.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN recruitment paragraph vs PLAN Table4 and overall target

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancies within one PLAN bundle, P_P; plan_material.

**Classification ambiguity:** Possible embedded target revision without version boundary.

**Exact source locations:** PLAN [Protocol PDF p.21, lines 995–997](../joi190079supp1_prod.pdf#page=21); [p.17 Table 4](../joi190079supp1_prod.pdf#page=17); [p.7 overview/Figure 1](../joi190079supp1_prod.pdf#page=7), with p.8 corroborating recruitment target.

**Source evidence:** Four sites each 82 patients; Table 4 each 98 acute recruits and 44 randomized; overall 392 acute and 176 randomized.

**Reported-versus-comparator:** The plan prints 82 acute recruits per site in one passage and 98 per site in its target table. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Two printed prospective acute targets conflict if the recruitment population is identical. No comparison to actual 269/126 recruitment is made.

**Calculation:** 4×98=392; 4×82=328; difference 64 total or 16/site. Acute and randomized targets are not interchanged.

**Alternative source-grounded interpretations:** Is 82 a version-specific target or subgroup? Locate a supplied amendment/population qualifier that reconciles 82 with 98/392, if present.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C010 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the prospective acute recruitment target supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the prospective acute recruitment target into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Is 82 a version-specific target or subgroup? Locate a supplied amendment/population qualifier that reconciles 82 with 98/392, if present. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Protocol MMSE threshold heading and paragraph name different phases

**Pending Human Adjudication.**

**Candidate statement:** The plan attaches the MMSE threshold of 24 to different phase-entry labels.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN MMSE threshold heading vs PLAN operational phase labels

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN heading versus PLAN operational paragraph, P_P; plan_material. Main report agrees with the operational paragraph and is corroboration, not a P_R discrepancy.

**Classification ambiguity:** Heading shorthand or an unprinted second gate.

**Exact source locations:** PLAN [Protocol PDF p.9, line 438 and lines 439–444](../joi190079supp1_prod.pdf#page=9), continuing line 445 on [p.10](../joi190079supp1_prod.pdf#page=10); [p.7 operational threshold](../joi190079supp1_prod.pdf#page=7); [p.11 Table 1 footnoteH](../joi190079supp1_prod.pdf#page=11) corroborates assessment time.

**Source evidence:** Heading MMSE≥24 to enter Stabilization; paragraph MMSE<24 at end Stabilization excludes RCT, with case exceptions. Overview assigns≥24 to RCT entry. Standard Stabilization is 8 weeks.

**Reported-versus-comparator:** The plan attaches the MMSE threshold of 24 to different phase-entry labels. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** The printed cutoff value is the same, but its phase label changes from entry into Stabilization in the heading to entry into the RCT after Stabilization in the operational paragraph. No score or observed eligibility count is inferred incorrect.

**Calculation:** Same numeric gate has different entry-phase labels; Stabilization entry and RCT entry are ordinarily 8 weeks apart. This is a concrete threshold label comparison, not an asserted difference in scores, eligibility counts or study-design quality.

**Alternative source-grounded interpretations:** Is the cutoff for Stabilization entry, RCT entry or two separate gates? Which operational definition reconciles heading, paragraph and scheduled end-Stabilization MMSE?

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C011 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the phase-specific MMSE eligibility cutoff supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the phase-specific MMSE eligibility cutoff into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Is the cutoff for Stabilization entry, RCT entry or two separate gates? Which operational definition reconciles heading, paragraph and scheduled end-Stabilization MMSE? Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — Historical 35% changes denominator between protocol passages

**Pending Human Adjudication.**

**Candidate statement:** Two plan passages attach the historical 35% value to different denominator identities.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN historical 35% fraction-of-relapses wording vs PLAN participant-risk framing

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Historical/background content in one PLAN remains PLAN, P_P; plan_material.

**Classification ambiguity:** Historical denominator or second distinct estimate unprinted.

**Exact source locations:** PLAN [Protocol PDF p.4, lines 175–177](../joi190079supp1_prod.pdf#page=4); [p.15, lines 728–732](../joi190079supp1_prod.pdf#page=15).

**Source evidence:** Historical Aronson account says approximately 35% of relapses occurred following antipsychotic discontinuation; power framing assumes 35% participant relapse after discontinuation and calls it the same reported rate from that study. The planned 35%−15%=20 point contrast itself reconciles.

**Reported-versus-comparator:** Two plan passages attach the historical 35% value to different denominator identities. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Printed denominator/framing difference, with symbolic diagnostic. The package does not provide the underlying historical study's full data.

**Calculation:** With D=relapses following discontinuation, R=all relapses and E=discontinuers at risk, the first wording is D/R≈.35 and the latter participant-risk identity is D/E≈.35. Different denominators cannot be treated as the same measure without a supplied mapping. No R/D/E counts are given and no historical risk is reconstructed.

**Alternative source-grounded interpretations:** Did the historical study report both quantities, did the first passage compress its denominator, or do R and E have an explicit identity? Clarify what 35% represents in the supplied protocol account; no external literature is used.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C012 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the historical relapse quantity used to explain a power assumption supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the historical relapse quantity used to explain a power assumption into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Did the historical study report both quantities, did the first passage compress its denominator, or do R and E have an explicit identity? Clarify what 35% represents in the supplied protocol account; no external literature is used. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Historical Week6 completers differ between race and ethnicity partitions

**Pending Human Adjudication.**

**Candidate statement:** The historical Week 6 percentages imply different integer completion totals across two apparently matched population partitions.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN historical Table5 race vs ethnicity Week6 completion partitions

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Same historical table within PLAN, P_P; plan_material.

**Classification ambiguity:** Unprinted alternative denominators or unmatched completion classification.

**Exact source locations:** PLAN [Protocol PDF p.29, Table 5](../joi190079supp1_prod.pdf#page=29), historical STOP-PD randomized n and Week 6 completion columns.

**Source evidence:** Race Asian 12/75.0%, Black 29/75.9%, White 218/74.8%; ethnicity Hispanic 30/80.0%, non-Hispanic 229/73.8%. Both denominator partitions sum 259. Historical, not current continuation-trial results.

**Reported-versus-comparator:** The historical Week 6 percentages imply different integer completion totals across two apparently matched population partitions. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Denominators, percentages and common endpoint are printed; inferred integer numerators and totals are explicitly derived. Exhaustive/mutually exclusive matching of the two axes is supported by their totals, but raw flags are not supplied.

**Calculation:** Nearest one-decimal intervals permit unique integer completers 9, 22, 163 versus 24, 169; sums 194 versus 193. Row count interval width.001 n≤.229 admits at most one integer. Difference 1/259=.386100 percentage point. Week 12 counts 6+15+121 and 16+126 both sum 142.

**Alternative source-grounded interpretations:** Do both axes partition identical participants and use the printed n as completion denominator? Obtain raw completer counts and any missingness/definition difference; no single row is declared incorrect.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C013 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the historical Week 6 completion total supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the historical Week 6 completion total into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Do both axes partition identical participants and use the printed n as completion denominator? Obtain raw completer counts and any missingness/definition difference; no single row is declared incorrect. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Protocol exposure range omits the permitted extended path

**Pending Human Adjudication.**

**Candidate statement:** The printed maximum pre-RCT sertraline duration does not explicitly accommodate the conditionally permitted extended pathway.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN pre-RCT exposure range vs PLAN phase durations and allowed extension

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All compared prospective statements within PLAN, P_P; plan_material.

**Classification ambiguity:** Ordinary-course summary versus exception-inclusive range and medication clock.

**Exact source locations:** PLAN [Protocol PDF p.41, lines 2069–2070](../joi190079supp1_prod.pdf#page=41); [p.10 Table 1](../joi190079supp1_prod.pdf#page=10); [p.11 footnotesA/D](../joi190079supp1_prod.pdf#page=11); [p.7 lines 326–332](../joi190079supp1_prod.pdf#page=7); [p.40 stabilization dosing](../joi190079supp1_prod.pdf#page=40). Pp.13–14 and 25 corroborate ordinary duration/continuation.

**Source evidence:** Minimum 10/max 20 weeks sertraline beforeRCT; acute 4–12 weeks after starting study medication; ordinary stabilization 8 weeks on treatment; p.7 allows two additional weekly stabilization visits for near-remitters not yet meeting final criteria.

**Reported-versus-comparator:** The printed maximum pre-RCT sertraline duration does not explicitly accommodate the conditionally permitted extended pathway. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Printed range, components and extension versus conditional arithmetic, not actual exposure data or a protocol violation.

**Calculation:** Ordinary sequential course 4–12+8=12–20 weeks. If the explicitly permitted extension follows 12 acute weeks with continuous sertraline, 12+8+2=22 weeks, exceeding printed max 20 by 2. Minimum 10 could be a conservative lower bound compatible with≥12, so that component is weaker and conditional.

**Alternative source-grounded interpretations:** Does p.41 summarize only the ordinary course, excluding authorized extension, or use another medication clock? Where is the qualification stated? Is 10 a loose lower bound or a permitted 2-week acute course? Confirm continuous exposure along the extended path.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C014 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the permitted pre-randomization medication timeline supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the permitted pre-randomization medication timeline into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Does p.41 summarize only the ordinary course, excluding authorized extension, or use another medication clock? Where is the qualification stated? Is 10 a loose lower bound or a permitted 2-week acute course? Confirm continuous exposure along the extended path. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C015 — Report HDRS relapse threshold omits the plan's five-point qualifier

**Pending Human Adjudication.**

**Candidate statement:** The report’s HDRS relapse threshold omits the plan’s numerical five-point-rise qualifier; applied patient rules are unknown.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT relapse HDRS threshold vs PLAN threshold and five-point-rise qualifier

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** REPORT numeric endpoint label versus PLAN criterion, P_R; protocol_report.

**Classification ambiguity:** Summary wording versus operative amended/full rule.

## Registration completion

All fifteen distinct discovered candidates have stable IDs. All are Pending Human Adjudication. The completed fresh recheck preserved every ID, confirmed content-based roles and primary/all relationships, and assigned exactly one allowed evidence state to each. Suggested review disposition is derived mechanically, never an AI adjudication. All ledger source links are truthful physical PDF locators. Missing definitions are candidate-specific limitations rather than source-coverage gaps.

**Exact source locations:** REPORT [Main PDF p.4, primary outcome](../jama_flint_2019_oi_190079.pdf#page=4); PLAN [Protocol PDF p.12, lines 556–557](../joi190079supp1_prod.pdf#page=12). [Main PDF p.6](../jama_flint_2019_oi_190079.pdf#page=6) supplies 13/64 and 34/62 relapse results whose endpoint is defined, not differing counts.

**Source evidence:** Report relapse requires≥1 listed criterion, including 17-itemHDRS≥18. Plan adds mean absolute increase 5 points on at leastone visit relative toRCT entry. Near-remission baseline may beHDRS11–15.

**Reported-versus-comparator:** The report’s HDRS relapse threshold omits the plan’s numerical five-point-rise qualifier; applied patient rules are unknown. The specific printed inputs and comparator are reproduced above; the numerical or label comparison follows below.

**Reasoning procedure:** Exact numeric endpoint definitions differ; whether applied rules or observed 13/34 counts differ cannot be established from supplied aggregate data.

**Calculation:** Score≥18 alone differs from score≥18 plus rise≥5 for baseline 14–15. Illustrative 15→18 rises 3 and meets the report's printed threshold but not the plan qualifier; this is an example, not an observed participant. At baseline≤13, ≥18 entails≥5 rise.

**Alternative source-grounded interpretations:** Was the report compressed while the full plan rule was applied, was an amendment disclosed, or did the operative rule change? Determine the actual rule and whether any person met≥18 without≥5 rise and without another relapse criterion. No violation or conclusion change is asserted.

**Mechanical evidence recheck:** The fresh rechecker found the cited source locations, matched the printed inputs and comparator, and independently reproduced the comparison under the stated rule. The named missing definitions remain unresolved; the quality audit confirmed the evidence record and classification. See the corresponding C015 record in [the direct-source recheck](review_1_6/verification/evidence_recheck.md) and [quality audit](review_1_6/quality/evidence_quality_audit.md).

**Quality-control relevance:** Consistent reporting of the numerical relapse endpoint definition supports accurate, reproducible extraction. The question concerns the printed record and its stated definitions.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an inconsistent version of the numerical relapse endpoint definition into a systematic review or evidence table. No actual propagation, clinical harm or conclusion change is established.

**Human verification steps:** Reopen each linked physical PDF page and compare the original headers, row labels, footnotes and definitions. Reproduce the calculation under its explicit assumptions, then resolve this question: Was the report compressed while the full plan rule was applied, was an amendment disclosed, or did the operative rule change? Determine the actual rule and whether any person met≥18 without≥5 rise and without another relapse criterion. No violation or conclusion change is asserted. Record the human decision without treating the mechanical pre-fill as an adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

# Downstream Evidence-Chain Considerations

Reported values and definitions can pass from articles into extraction forms, systematic reviews, meta-analyses, guidelines and later publications. Small preventable defects can therefore be worth checking even when they do not change a paper’s conclusions. Here the bounded possibilities are copying a percentage, point estimate, denominator, score range, unit, prospective target or endpoint definition without its necessary qualification.

The package provides no evidence that these observations have propagated or caused harm. C009 particularly requires resolution of the comparison’s unsupported alignment before a residual reporting issue can be established. PLAN-internal historical or prospective observations must not be represented as mistakes in the current randomized trial’s observed results.

# Limitations and Missing Definitions

All source units were mapped; there is no unresolved scientific-coverage gap. Remaining limits concern the definitions needed to interpret or reconstruct particular relationships:

- Table-specific denominators, category exhaustiveness and missingness; intended superscript associations and implemented score coding; intended HbA1c response transformation and coefficient unit.
- Display rounding or truncation and the exact unadjusted estimator behind Table 5 point estimates. Missing interval algorithms do not support a separate CI claim.
- Exact SAS figure coordinates, link function, coefficient scale, marginal or conditional interpretation, reference population and back-transformation. Its additive graphical secant is not supplied as the coefficient estimand.
- Plan version or target population for recruitment; the phase at which MMSE 24 applies; underlying historical relapse denominators; historical completion numerators, partition identity and percentage-denominator definitions.
- Medication-exposure clock, extension applicability and whether the 20-week maximum summarizes the ordinary course. A 10-week lower bound alone can be conservative; no actual 22-week exposure is documented.
- The operative relapse rule and any amendment or compressed reporting. Hypothetical baseline-score examples distinguish definitions, but patient-level event adjudications and other relapse branches are unavailable.

Statistical reconstruction also lacks exact Cox test/CI construction, mixed-model covariance and degrees of freedom, full multiplicity-family mapping, paired subset definitions, pattern-mixture weights and power-simulation generators. Historical t-test sidedness, dispersion definitions, effective sample sizes and variance estimators are not fully specified. Main testing is explicitly two-sided. Conventional Welch or Wald diagnostics cannot replace missing supplied definitions; crude-risk NNT is not automatically the reported HR-based NNT. Band overlap is not an interaction test, and plotted means are approximate.

Historical extraction/render engine versions are partly unavailable; not every prose page has a reusable render. Direct source coverage nevertheless closes every page. Administrative DOC-004 has a bounded PLAN-versus-disclosure role ambiguity and enters no candidate. No external literature, raw data or unpublished model output was obtained. Full limitations and each candidate-specific human question are preserved in [limitations](review_1_6/limitations.md).

# Human Adjudication Checklist

For each permanent ID, inspect original sources, confirm the population/time/outcome and denominator or scale identity, reproduce only the applicable source-grounded rule, and resolve its named alternatives. C009 needs an estimand mapping before its initial diagnostic comparison can support a residual question. Distinguish source-printed numbers from inferred integer counts, graphical readings and illustrative eligibility examples.

Review document roles and relationship precedence, then decide validity, importance and action independently of the suggested pre-fill. Enter initials and notes in the five blank fields, retaining every stable ID and the supporting record. Any correction or author query is for human decision; this report assigns none.

# Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

## Source integrity and durable artifacts

SHA-256 baselines were recorded before content inspection. The audit confirmed all four source hashes and all 187 reused hashes unchanged. The coordinator performs the final before/after comparison following report assembly. Full source identities:

| Source | SHA-256 baseline |
|---|---|
| jama_flint_2019_oi_190079.pdf | f3480ac424a06c1a7747c03a4e9523b1b391ed918562f402c84ad516f85cf05f |
| joi190079supp1_prod.pdf | 68aaf0377b631a63a25438ed4d101acb8f19a75ce9c5a9243ab5d75718a06b8f |
| joi190079supp2_prod.pdf | 648b40127a28c8b919ee94918cd879a6cd8001810a4d5db61394d6fa0bae6d53 |
| joi190079supp3_prod.pdf | d335f3d8b8ca330abc569a368e62e561f588309d621b89a9af1dd64ab6c7e199 |

Full checksum records: [source before](review_1_6/source_hashes_before.sha256), [source after](review_1_6/source_hashes_after.sha256), [reused assets before](review_1_6/reused_artifact_hashes_before.sha256) and [reused assets after](review_1_6/reused_artifact_hashes_after.sha256). Reused evidence was immutable. New derivative engines, commands and sources are recorded in the asset inventory. Editorial/transcription repairs to current-run maps, locators and diagnostics are documented in the quality audit, without altering supplied sources or permanent candidates.

## Routing, tools and validation basis

The actual provider is **openai**, expressly authorized by the user in place of the configured **openrouter** provider. All fixed `gpt-6.1-sol` model and effort requirements were retained. [Routing preflight](review_1_6/routing_preflight.md) passes the user-amended provider requirement, with coordinator inference confirmed and all nine named presets checked. Runtime provenance supports `INTERACTIVE_CLI`; `codex --approve-for-me` is the required launch-command field, not independently observed command-line arguments.

The original bundled validator remains unchanged. Its result in [original validation](review_1_6/validation/original_review_validation.json) applies the original provider contract. [Canonical validation](review_1_6/review_validation.json) applies the sole user-authorized provider exception through a run-local copy changing only the expected provider string to openai. All other checks remain identical. Readers can inspect both actual local outputs; the original provider requirement is not represented as satisfied. [Provider-exception documentation](review_1_6/validation/provider_exception.md) records the sole diff and helper hashes.

Direct local tools were available: Poppler 26.01.0 for PDF information/text/rendering, Tesseract 5.5.0, LibreOffice and Pandoc 3.7.0.2. No fallback environment was needed or created; no global packages were installed. The coordinator renders standalone HTML with embedded CSS and a table of contents, records tooling completion, and runs final local validation. See [tooling record](review_1_6/tooling_record.md).

## Actual agent execution

All 15 actual agents appear below: coordinator, ten mandatory specialist stages and four extra disjoint mapping/numeric shards. Each specialist stage used a fresh distinct runtime. Both statistical agents, the rechecker and auditor used high effort; other specialists used medium effort. The coordinator used high effort.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12860-cec4-7f22-bd5d-22a027867aab | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12862-ddad-7a52-8190-b8730a1cfe2e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12865-5284-7fd3-8b3b-5e3162260ca4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12865-7761-7463-94e9-82162135e72a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_plan_second_shard | 01a12865-9452-7e81-82ac-345be361fa05 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_second.md |
| numeric_consistency_reviewer | 01a1286a-6645-7930-8d1b-45686ffab070 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_report_last_shard | 01a1286a-814f-7b12-a00b-e90ab6064dbe | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_report_last.md |
| numeric_plan_first_shard | 01a1286a-9bc9-7b92-a717-2777aa292dbf | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_plan_first.md |
| numeric_plan_last_shard | 01a1286a-b71f-73c2-90f9-22d2fd35e362 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_plan_last.md |
| statistics_pass_1 | 01a1286a-d824-7281-a62a-c73b450e930c | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | 01a1286a-f59b-7f01-8800-04b775b11953 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_rechecker | 01a12872-9b72-7460-86ab-0229340c9851 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12878-d12a-7d81-a8cf-041b2a0b54f7 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a1287d-2993-7d60-a161-d4cc0ebd7edd | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12881-d989-7242-8223-53733c47a31a | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

## Reproducibility performance

Timing fields below are copied from [run state](review_1_6/run_state.md). The coordinator finalizes the finish time immediately after complete Markdown assembly. Local HTML rendering and validation are excluded; any later model-based repair advances the recorded finish time.

- **Target basis:** Four PDFs contain 63 pages: 10 article pages, 42 protocol/data analytic and pharmacotherapy-plan pages, 10 results-supplement pages including nine vector plots, and one operational data-sharing page. All 63 pages have usable reusable evidence; zero pages require fresh extraction. The review still requires new complete mapping of article tables, historical and prospective plan quantities, and graphical results, with parallel main/support mapping, three parallel checking lanes, distinct two-pass statistical review, exact-source recheck, quality audit, and report generation. Allow 30-45 minutes for these agent waves and targeted visual confirmation; this target is based on reusable coverage and relationship complexity as well as source-unit count.
- **Total source units:** 63
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T00:35:03Z
- **Finished UTC:** 2026-10-11T01:14:01Z
- **Observed elapsed minutes:** 38.967
- **Target status:** MET_TARGET
- **Exceedance causes:** None
