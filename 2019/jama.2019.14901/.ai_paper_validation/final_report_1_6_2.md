# Quantitative Reporting Quality-Control Consistency Review — HIGH-WEAN Trial

**Pending Human Adjudication**

Workflow 1.6.2 examines quantitative reporting consistency in the supplied package for JAMA article DOI 10.1001/jama.2019.14901. Candidate inclusion, classification and evidence reproduction are quality-control records; they do not adjudicate the paper or select corrections.

## Executive Quality-Control Summary

Complete inspection of four supplied PDFs, comprising 69 pages, identified five stable candidates. Four concern planned-versus-reported endpoint or analysis reporting, and one concerns four count/percentage cells in a supplementary baseline table. Independent source recheck reproduced all five, and the inclusion audit recorded CONFIRMED for each. Every candidate remains Pending Human Adjudication.

The principal boundaries are substantive. The respiratory-failure definition candidate establishes a printed omission, without establishing a changed operational definition or event count. Planned Cox and subgroup outputs are absent from the supplied reports, without establishing nonperformance. The logistic candidate concerns the supplied mapping of a predefined adjustment rule; potentially distinct prognostic and treatment models remain a supported alternative. The percentage candidate establishes four arithmetic discrepancies without selecting the intended fields.

Ten checker findings received independent screening: five INCLUDE and five SCREENED_OUT, comprising four duplicates of included issues and one peripheral comparison. A separate second statistical pass and final audit reconsidered all relationships and checker exclusions; neither added findings. Candidate count was determined by the inclusion threshold, without a count target or ranked subset.

## Package and Reused-Evidence Provenance

The supplied article compares high-flow nasal oxygen alone with high-flow nasal oxygen plus noninvasive ventilation (NIV) after extubation in high-risk patients. Unless stated otherwise, comparisons below use HFNC alone as control, HFNC with NIV as intervention, analyzed arm denominators 302 and 339, and intervention-minus-control absolute differences in percentage points. The source counts distinguish 648 randomized from 641 analyzed participants.

| Source ID | Supplied source | Role by content | PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_thille_2019_oi_190108.pdf — article](<../jama_thille_2019_oi_190108.pdf#page=1>) | REPORT | 11 |
| DOC-002 | [joi190108supp1_prod.pdf — protocol version 4, October 17, 2017](<../joi190108supp1_prod.pdf#page=1>) | PLAN | 48 |
| DOC-003 | [joi190108supp2_prod.pdf — results supplement](<../joi190108supp2_prod.pdf#page=1>) | REPORT | 9 |
| DOC-004 | [joi190108supp3_prod.pdf — data-sharing statement](<../joi190108supp3_prod.pdf#page=1>) | REPORT | 1 |
| **Total** | Four PDF sources; no Office or CSV source | | **69** |

The curator inventoried 153 eligible extraction/layout/page-map/image assets and hashed 152 reused assets. One partial selected-results map was inventoried without reuse. Source-linked native/layout text, OCR and rasters were reused as locators and transcription aids; previous candidate sets, screens and reports did not define discovery. Source PDFs remained the authority. The [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md) records coverage and fitness, and the [source inventory](review_1_6_2/source_inventory.md) records document roles.

All 69 pages had usable reusable-backed evidence; none initially required fresh extraction to close coverage. Fifteen new direct-source derivatives were nevertheless produced for numeric confirmation and mechanical recheck: two numeric-check rasters and thirteen recheck text/raster outputs. These are recorded new assets, separate from the reused hash inventory. Direct Poppler 26.01.0 extraction/rendering used the CPU. No new OCR, Office conversion, GPU processing or fallback environment was needed.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators, estimate and test logic, statistical method logic, and planned-versus-reported statistical design under [QUALITY_CONTROL_SCOPE.md](../QUALITY_CONTROL_SCOPE.md). Every supplied source unit was mapped, including administrative/reference pages with explicit completed applicability records, the image-dependent protocol appendix on PDF p. 42, and the graphical supplementary survival page.

| Source | Total units | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | 48 | 48 | 0 | 48 | COMPLETE |
| DOC-003 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **69** | **69** | **0** | **69** | **COMPLETE** |

The [source-coverage ledger](review_1_6_2/source_coverage.md), [coverage manifest](review_1_6_2/coverage_manifest.md), [main quantitative map](review_1_6_2/extraction/main_quantitative_evidence.md) and [support quantitative map](review_1_6_2/extraction/support_quantitative_evidence.md) preserve full assignments and evidence. No scientific source-coverage gap remains. Reusable-derivative limitations are stated separately below.

Differences allowed by the display-precision rule, display-zero P values, readily resolved notation or wording, model-based estimates compared with crude ratios, conditional observations without a printed conflict, peripheral comparisons and out-of-focus observations do not become candidates. The review does not perform a broad study-design, clinical, novelty, misconduct or raw-data audit, and proposes no preferred analysis. No external literature or web evidence was used.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains 45 complete grouped relationships: N001–N038 and N201–N207. Coverage includes all display subrows, flow arithmetic, explicit row denominators, baseline distributions, outcome counts, subgroup recombination, center totals and figure risk sets. Counts belonging to overlapping conditions and risk-set depletion subject to censoring were not treated as compulsory partitions.

The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains 47 groups, S001–S032 and S201–S215. Both fresh statistical agents covered every group and all 130 supplementary S215 subrecords: 31 eTable 1 records, 72 eTable 2 records, 26 eTables 3–4 outcome records and one survival-figure record. These include 129 printed supplementary P values and the 26 subgroup estimate/interval/P rows. Each record carries PASS_1_COMPLETE and PASS_2_COMPLETE.

| Stage | Actual fresh runtime ID | Model / effort | Completed scope |
|---|---|---|---|
| Statistical pass 1 | root/statistical_pass_one | gpt-6.1-sol / high | 47 groups and 130 supplementary subrecords |
| Statistical pass 2 | root/statistical_pass_two | gpt-6.1-sol / high | Same complete scope; stable ledger, screen and recheck facts; checker exclusions reconsidered |
| Quality audit | root/quality_audit | gpt-6.1-sol / high | Every stable ID, 10 screening decisions, 59 checker exclusion rows, both passes, classification and coverage |

The checker exclusion tables contain 59 rows in total: numeric 5, cross-source 12, statistical pass 1 20 and statistical pass 2 22. These are apparent observations considered and excluded within their lanes, distinct from the ten emitted finding rows. Pass 2 and the independent audit reconsidered them against route-A categories and display precision. A duration observation excluded in one cross-source lane is retained as C001 through its independently included finding; it was not lost. No additional qualifying issue or screening reversal arose. Complete records are in the [pass-1 checker](review_1_6_2/checkers/statistical_pass_1.md), [pass-2 checker](review_1_6_2/checkers/statistical_pass_2.md) and [quality audit](review_1_6_2/quality/evidence_quality_audit.md).

## Inclusion Screening Summary

A finding qualifies only when reproduced and satisfying either route A (an always-register category) or all route-B conditions: in focus, not resolved at once by immediate context, and bearing on a named result's interpretation or extraction. Numeric reconstruction allows half-unit rounding intervals for each printed input and output; remaining relative discrepancy at most 0.05 is screened as display precision. Interval-versus-P/test conflicts are exempt from that rounding exclusion.

| Decision | Reason code | Finding count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 5 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 4 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 1 |
| **Total** | | **10** |

All other screened-out reason codes have zero emitted-finding rows. The [screening log](review_1_6_2/screening/inclusion_screen.md) contains exactly one decision per finding. Its five INCLUDE rows map to C001–C005. Duplicate provenance is preserved in the ledger: F-ST1-002 with C002, F-ST1-001 with C003, F-ST1-003 with C004 and F-ST1-007 with C005; these duplicate rows do not create additional cards or appear as included Finding IDs. Statistical pass 2 emitted no new finding, so a second inclusion screen was not required.

The single peripheral finding concerns absence of an ordinary secondary support-free-days outcome, without a supplied primary/key designation, competing reported hierarchy status, composite change, population-size change or decision-rule effect. It received no stable candidate ID. The independent audit reviewed all screening decisions in both directions and recorded no reversal.

## Review-Domain Summary

The four domains organize human review: `statistical_results` concerns counts, estimates, intervals, tests or methods in REPORT material; `report_internal_inconsistency` concerns report conflicts over the identity of a quantitative result; `protocol_report` compares prospective PLAN specifications with REPORT content; and `plan_material` concerns statistical-design inconsistencies solely within PLAN material. Classification is not an adjudication.

| Review domain | Candidate count |
|---|---:|
| statistical_results | 1 |
| report_internal_inconsistency | 0 |
| protocol_report | 4 |
| plan_material | 0 |
| **Total** | **5** |

| Relationship type | Meaning | Candidate count |
|---|---|---:|
| P_R | PLAN versus REPORT | 4 |
| P_P | PLAN versus PLAN | 0 |
| S_C | Different REPORT documents | 0 |
| S_W | Within one REPORT document | 1 |
| **Total** | | **5** |

| Evidence state | Candidate count |
|---|---:|
| reproduced | 5 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **5** |

All five inclusion audits are CONFIRMED; zero are QUESTIONED. C001–C004 involve only P_R, while C005 involves only S_W. Corroborating sources do not create additional conflicting relationships; no mixed-type precedence decision is needed.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001--reported-respiratory-failure-definition-omits-planned-tachypnea-duration) | Printed respiratory-failure duration omission | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#c002--planned-primary-and-key-mortality-cox-results-are-not-reported) | Planned prognostic Cox outputs absent from supplied reports | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#c003--primary-adjusted-logistic-model-prespecification-mapping-is-unclear) | Primary adjusted logistic rule lacks supplied prespecification mapping | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#c004--two-planned-primary-outcome-subgroup-families-are-not-reported) | Two planned primary subgroup families lack supplied outputs | protocol_report | P_R | reproduced | CONFIRMED |
| [C005](#c005--four-hypercapnic-cough-and-secretion-percentages-do-not-reconcile) | Four within-display count/percentage discrepancies | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Reported respiratory-failure definition omits planned tachypnea duration

**Pending Human Adjudication**

**Candidate statement:** The explicit reported day-7 postextubation respiratory-failure definition omits the protocol's requirement that qualifying tachypnea persist for at least two hours. The printed mapping leaves the duration governing the reported endpoint unclear.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p. 30 vs REPORT main article pp. 1, 4, 8

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-006

**Qualifying route:** Route B

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

**Exact source locations:** PLAN [joi190108supp1_prod.pdf — PDF p. 30, acute respiratory-failure criteria](<../joi190108supp1_prod.pdf#page=30>); REPORT [jama_thille_2019_oi_190108.pdf — PDF p. 4, Outcomes](<../jama_thille_2019_oi_190108.pdf#page=4>), [PDF p. 1, abstract endpoint/result](<../jama_thille_2019_oi_190108.pdf#page=1>) and [PDF p. 8, Table 2 respiratory-failure row](<../jama_thille_2019_oi_190108.pdf#page=8>). Corroborating endpoint identity is at [protocol PDF p. 25](<../joi190108supp1_prod.pdf#page=25>); the shortened criterion/counts are also at [results supplement PDF p. 2, eTable 1](<../joi190108supp2_prod.pdf#page=2>).

**Source evidence:** The protocol requires at least two respiratory-failure criteria and qualifies respiratory rate greater than 25 breaths/min by a minimum two-hour duration. The report also requires at least two criteria and lists respiratory rate greater than 25 breaths/min, without that duration. Table 2 reports 88/302 versus 70/339 events, difference −8.5 percentage points (95% CI −15.2 to −1.8), P=.01; the abstract reports this endpoint, establishing key-secondary status.

**Reported-versus-comparator:** Report: rate threshold without a stated minimum duration. Plan: the same rate threshold with at least two hours of persistence. Counts are contextual anchors, not conflicting independently classified event totals.

**Reasoning procedure:** Align endpoint, day-7 window and criterion lists; identify the positive planned duration condition; inspect the complete supplied REPORT content for an incorporation statement. The report's explicit list does not identify the operational duration. B1 is focus D, B2 is unresolved definition mapping, and B3 is the definition attached to the named key-secondary event counts.

**Calculation:** Not applicable to a printed duration omission. The rate threshold itself agrees at 25 breaths/min. A shorter episode illustrates the literal definition gap but supplies no evidence that any participant was classified differently; no events or effects are recomputed.

**Affected result or extracted value:** Day-7 respiratory-failure endpoint definition attached to 88/302 HFNC-alone and 70/339 HFNC-with-NIV events.

**Why context does not resolve it:** The report presents an explicit criterion list without stating whether the planned persistence requirement remains operative. Common context cannot identify the duration actually used for the reported counts.

**Alternative source-grounded interpretations:** The article may condense the protocol while retaining the two-hour operational rule; shared endpoint identity and other thresholds support this possibility. A documented amended definition is another possibility, but no separate supplied SAP/amendment establishes it. Printed omission does not establish removal in practice or a numerical count change.

**Mechanical evidence recheck:** Direct source text and rendered pages confirmed all cited statements and counts, with no transcription correction. The evidence state reproduces the reporting-definition gap only. The operational algorithm and participant duration records are absent. The remaining question is whether the reported counts applied the protocol duration or a different documented definition.

**Potential downstream evidence impact:** An extractor could attach a duration-free criterion to this key-secondary endpoint if relying on the printed article definition. If confirmed, the reporting issue could affect endpoint-definition coding; no participant reclassification, propagated estimate or changed conclusion is established.

## C002 — Planned primary and key mortality Cox results are not reported

**Pending Human Adjudication**

**Candidate statement:** The supplied plan specifies outcome-associated prognostic Cox modeling for primary reintubation and mortality, including key ICU mortality, but corresponding model outputs are absent from the complete supplied REPORT package.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp. 33–34 vs REPORT main article pp. 1, 4, 6–8 and results supplement pp. 1–9

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route A, category 5

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

**Exact source locations:** PLAN [joi190108supp1_prod.pdf — PDF p. 33, section 6.2 primary Cox specification](<../joi190108supp1_prod.pdf#page=33>) and [PDF p. 34, mortality specification for ICU, hospital, day 28 and day 90](<../joi190108supp1_prod.pdf#page=34>). REPORT [jama_thille_2019_oi_190108.pdf — PDF p. 1, primary/key mortality results](<../jama_thille_2019_oi_190108.pdf#page=1>), [PDF p. 4, methods](<../jama_thille_2019_oi_190108.pdf#page=4>), [PDF p. 6, results](<../jama_thille_2019_oi_190108.pdf#page=6>), [PDF p. 7, adjusted OR and reintubation curves](<../jama_thille_2019_oi_190108.pdf#page=7>) and [PDF p. 8, Table 2 and Figure 3](<../jama_thille_2019_oi_190108.pdf#page=8>). Every results-supplement page was inspected: [joi190108supp2_prod.pdf — PDF p. 1, contents](<../joi190108supp2_prod.pdf#page=1>), [p. 2, eTable 1](<../joi190108supp2_prod.pdf#page=2>), [p. 3, baseline](<../joi190108supp2_prod.pdf#page=3>), [p. 4, baseline continuation](<../joi190108supp2_prod.pdf#page=4>), [p. 5, footnotes](<../joi190108supp2_prod.pdf#page=5>), [p. 6, hypercapnic outcomes](<../joi190108supp2_prod.pdf#page=6>), [p. 7, nonhypercapnic outcomes](<../joi190108supp2_prod.pdf#page=7>), [p. 8, center counts](<../joi190108supp2_prod.pdf#page=8>) and [p. 9, survival figure](<../joi190108supp2_prod.pdf#page=9>). All eleven article pages and the [data-sharing PDF p. 1](<../joi190108supp3_prod.pdf#page=1>) were additionally covered by the full presence audit in the recheck.

**Source evidence:** The primary plan screens outcome-associated variables at P<.20 for Cox backward selection, retaining P<.05 variables and reporting adjusted relative risk/HR with 95% intervals. Analogous mortality modeling is specified for all four mortality time points. The reports supply primary chi-square, Kaplan–Meier/log-rank, adjusted logistic OR and mortality proportions/differences. ICU mortality is 26/302 versus 21/339, difference −2.4 (95% CI −6.7 to 1.7), P=.25. No corresponding Cox-model estimates, predictor coefficients or final-model output appears.

**Reported-versus-comparator:** Planned prognostic Cox outputs for primary reintubation and ICU/hospital/day-28/day-90 mortality versus supplied proportions, logistic treatment adjustment and log-rank curves. Primary reintubation and abstract-key ICU mortality anchor inclusion; all repeated mortality-plan occurrences remain in this consolidated reporting pattern.

**Reasoning procedure:** Read both positive prospective commitments; align each outcome/time point; inspect every REPORT page and graphical display; use named text searches as supplementary locators. Curves/log-rank tests and a logistic OR do not supply a covariate-selected Cox model. Complete-page inspection, rather than search absence alone, supports the bounded reporting absence.

**Calculation:** No numerical HR is calculated or inferred. Display precision does not apply to absent model outputs, and no comparison of an adjusted estimate with a crude ratio is made.

**Affected result or extracted value:** Availability of prespecified primary reintubation and key ICU-mortality prognostic Cox estimates and their associated adjusted relative-risk/HR intervals, with the other planned mortality occurrences retained.

**Why context does not resolve it:** Route A, category 5 includes a positively planned primary or key-secondary analysis not reported. Neither a corresponding output nor a supplied explanation of its reporting change is present.

**Alternative source-grounded interpretations:** The outcome-predictor framing supports prognostic models potentially distinct from published treatment-effect analyses. No promised treatment HR is inferred. Models could have been fitted but omitted, reported outside this supplied package, or superseded through an unsupplied SAP/amendment. The package establishes none of those explanations and does not establish nonperformance.

**Mechanical evidence recheck:** Fresh full article/results extraction, complete page-by-page output inspection and visual survival-page confirmation reproduced the absence. All planned locations and every repeated mortality outcome were matched. Missing inputs are model outputs, predictor lists, coefficients, event/censoring records and any separate SAP/amendment. The remaining question is where the planned prognostic outputs or documented reporting change can be located.

**Potential downstream evidence impact:** A reviewer could record the planned primary/key-mortality adjusted model output as unavailable in this package or misidentify a supplied log-rank/logistic result as that output. If confirmed, the issue could affect analysis-availability and effect-measure coding, without establishing a missing treatment HR, propagated effect or changed conclusion.

## C003 — Primary adjusted logistic model prespecification mapping is unclear

**Pending Human Adjudication**

**Candidate statement:** The report describes its primary adjustment analysis as predefined, but its PaCO2-plus-baseline-imbalance selection rule is absent from the supplied plan, which describes a potentially distinct outcome-predictor logistic exercise. The supplied prespecification mapping for the published adjusted OR is unclear.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p. 33 vs REPORT main article pp. 4, 7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route A, category 5

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

**Exact source locations:** PLAN [joi190108supp1_prod.pdf — PDF p. 33, section 6.2 logistic selection](<../joi190108supp1_prod.pdf#page=33>); REPORT [jama_thille_2019_oi_190108.pdf — PDF p. 4, Statistical Analysis](<../jama_thille_2019_oi_190108.pdf#page=4>) and [PDF p. 7, Subgroup Analysis and Additional Analyses](<../jama_thille_2019_oi_190108.pdf#page=7>). [Article PDF p. 6, Table 1 footnote](<../jama_thille_2019_oi_190108.pdf#page=6>) corroborates chronic lung disease as the sole baseline characteristic with P=.02.

**Source evidence:** The protocol introduces predictors of reintubation, then multivariate logistic modeling after interaction testing, with outcome-associated P<.20 terms plus relevant forced variables, followed by backward elimination retaining outcome-associated P<.05 and forced variables. The article states that analyses followed a predefined SAP and adjusts for PaCO2 and baseline-unbalanced variables defined by between-arm P<.05. Chronic lung disease is the sole added variable. The adjusted day-7 reintubation OR is 0.60 (95% CI 0.38–0.93), P=.02.

**Reported-versus-comparator:** Between-arm baseline imbalance at P<.05 plus PaCO2 versus outcome association at P<.20, forced terms and backward retention at P<.05. These predicates concern different association targets; the same logistic model family does not establish the same exercise or supplied prespecification.

**Reasoning procedure:** Match the reported predefined claim and printed adjustment rule to the supplied prospective material; distinguish prognostic selection from treatment adjustment; attach the unresolved mapping to the published primary OR. The report-specific rule is not located in the supplied plan, but the evidence does not show that the two models were necessarily the same analysis or that one replaced the other.

**Calculation:** No adjusted OR is recomputed from aggregate counts. The estimate/CI/P were source-matched and separately reviewed for statistical consistency. Display precision is inapplicable to differing selection predicates rather than two rounded copies of one threshold.

**Affected result or extracted value:** Prespecified-analysis and covariate-selection coding for adjusted day-7 reintubation OR 0.60 (0.38–0.93), P=.02.

**Why context does not resolve it:** Route A, category 5 covers an analysis described as predefined whose stated specification is absent from the supplied plan. Final covariates identify the published model but do not supply its governing prospective SAP or mapping to the planned predictor exercise.

**Alternative source-grounded interpretations:** The protocol's explicit predictor framing and the report's treatment-adjustment framing support distinct analyses that could coexist coherently. A separate unsupplied SAP could prespecify the article rule. Differing rules therefore do not establish replacement, require the planned predictor exercise to generate this treatment OR, or demonstrate a changed fitted coefficient.

**Mechanical evidence recheck:** Direct source text and rasters confirmed the two predicates, predefined claim, covariates and OR without transcription correction. Missing inputs include separate SAP/amendment, model coefficients/covariance, forced predictors and selection/interactions output. The remaining question is which predefined specification governs this OR and how it relates to the protocol predictor exercise.

**Potential downstream evidence impact:** An extractor could code this adjusted OR as arising from the supplied protocol's predictor-selection model or assign its prespecification status without the missing mapping. If confirmed, the issue could affect model/covariate documentation; no changed OR, propagation or conclusion change is established.

## C004 — Two planned primary-outcome subgroup families are not reported

**Pending Human Adjudication**

**Candidate statement:** Primary day-7 reintubation subgroup outputs for underlying cardiac/respiratory disease and for T-piece versus minimal pressure-support breathing tests are absent from the supplied REPORT package despite explicit prospective commitments. Both families are retained in one reporting pattern.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p. 34 vs REPORT main article pp. 4, 7–8 and results supplement pp. 1, 3–7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** The inconsistency compares prospective PLAN specifications with REPORT methods or results; P_R governs, and the domain is protocol_report.

**Classification ambiguity:** No separately supplied SAP or amendment establishes whether a changed or distinct analysis was documented; classification is based on supplied content.

**Exact source locations:** PLAN [joi190108supp1_prod.pdf — PDF p. 34, section 6.4](<../joi190108supp1_prod.pdf#page=34>); REPORT [jama_thille_2019_oi_190108.pdf — PDF p. 4, subgroup methods](<../jama_thille_2019_oi_190108.pdf#page=4>), [PDF p. 7, subgroup results](<../jama_thille_2019_oi_190108.pdf#page=7>) and [PDF p. 8, Figure 3](<../jama_thille_2019_oi_190108.pdf#page=8>); REPORT [joi190108supp2_prod.pdf — PDF p. 1, contents](<../joi190108supp2_prod.pdf#page=1>), [p. 3, disease baseline entries](<../joi190108supp2_prod.pdf#page=3>), [p. 4, breathing-test baseline entries](<../joi190108supp2_prod.pdf#page=4>), [p. 5, category footnotes](<../joi190108supp2_prod.pdf#page=5>), [p. 6, hypercapnic outcomes](<../joi190108supp2_prod.pdf#page=6>) and [p. 7, nonhypercapnic outcomes](<../joi190108supp2_prod.pdf#page=7>). Complete REPORT-page inspection, including all other article, results and data-sharing pages, is recorded in the [mechanical recheck](review_1_6_2/verification/evidence_recheck.md).

**Source evidence:** The plan specifies main/secondary-criterion analyses by PaCO2, underlying cardiac or respiratory disease, and pre-extubation weaning test (T-piece versus minimal pressure support). The reports provide PaCO2 interaction P=.25, primary contrasts and Figure 3/eTables 3–4. Neither of the other two primary-outcome subgroup families has output. Disease characteristics, breathing-test counts and chronic-lung-disease adjustment are present but are different quantities.

**Reported-versus-comparator:** PaCO2 family: supplied. Disease family: planned primary subgroup analyses without supplied contrasts. Breathing-test family: planned primary subgroup analyses without supplied contrasts. The latter two are the affected occurrences; no ordinary secondary omission is added to this card.

**Reasoning procedure:** Compare each planned subgroup family separately against complete methods, results, contents and displays. Distinguish baseline characteristics and overall covariate adjustment from subgroup outcome contrasts. Retain both missing primary families under the same positively specified nonreporting pattern.

**Calculation:** No subgroup effect is calculated from baseline totals. Display precision is inapplicable to absent outputs. Disease-category overlap and aggregate arm counts cannot supply subgroup outcome numerators or interactions.

**Affected result or extracted value:** Availability and prespecified subgroup-universe coding for day-7 reintubation analyses by underlying cardiac/respiratory disease and breathing-test type.

**Why context does not resolve it:** Route A, category 5 includes a planned primary-outcome analysis not reported. The supplied reports contain neither the two outputs nor documented withdrawal/replacement; presenting the PaCO2 family does not supply them.

**Alternative source-grounded interpretations:** The analyses could have been performed and omitted, or changed through an unsupplied SAP/amendment. Cardiac/respiratory categories may overlap and require definitions. These possibilities limit implementation claims but do not provide the planned outputs; no subgroup effect or heterogeneity direction is inferred.

**Mechanical evidence recheck:** Complete REPORT-page inspection, direct extraction and selected visual confirmation reproduced absence of both named primary families. No transcription or classification correction was needed. Missing inputs include subgroup definitions, event counts/contrasts, interactions and any amendment. The remaining question is where the two planned outputs or documented reporting change are located.

**Potential downstream evidence impact:** A reviewer could record only PaCO2 as the supplied planned primary subgroup universe or miss the availability distinction for the two other prespecified families. If confirmed, the issue could affect subgroup-availability documentation; no nonperformance, propagated subgroup effect or conclusion change is established.

## C005 — Four hypercapnic cough and secretion percentages do not reconcile

**Pending Human Adjudication**

**Candidate statement:** All four hypercapnic ineffective-cough and abundant-secretions cells in eTable 2 print percentages that do not reconcile with their own explicit numerators and denominators after the required display-precision allowance.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement p. 4 count and denominator vs percentage in the same display

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 3

**Classification rationale:** All conflicting counts, denominators and percentages are in one REPORT table; corroborating main-table values do not create another relationship. S_W governs, and the domain is statistical_results.

**Classification ambiguity:** None

**Exact source locations:** Four separate affected cells in [joi190108supp2_prod.pdf — PDF p. 4, eTable 2](<../joi190108supp2_prod.pdf#page=4>): [ineffective cough, hypercapnic HFNC alone, 14/45 (69)](<../joi190108supp2_prod.pdf#page=4>); [ineffective cough, hypercapnic HFNC with NIV, 16/59 (73)](<../joi190108supp2_prod.pdf#page=4>); [abundant secretions, hypercapnic HFNC alone, 20/46 (57)](<../joi190108supp2_prod.pdf#page=4>); [abundant secretions, hypercapnic HFNC with NIV, 23/61 (62)](<../joi190108supp2_prod.pdf#page=4>). Row footnotes are at [PDF p. 5](<../joi190108supp2_prod.pdf#page=5>). Corroboration is at [jama_thille_2019_oi_190108.pdf — PDF p. 6, Table 1](<../jama_thille_2019_oi_190108.pdf#page=6>); a possible explanatory percentage pair is at [results supplement PDF p. 3, chronic lung disease](<../joi190108supp2_prod.pdf#page=3>).

**Source evidence:** Both row labels state No./total No. (%). The printed hypercapnic triples are 14/45 (69), 16/59 (73), 20/46 (57) and 23/61 (62). Full column totals 48 and 63 are separately printed; the available-case denominators 45, 59, 46 and 61 are explicit. No footnote supplies another percentage definition or population.

**Reported-versus-comparator:** Parenthetical percentages 69%, 73%, 57% and 62% versus 100 times the explicit within-cell fractions, approximately 31.11%, 27.12%, 43.48% and 37.70%, respectively. All four locations are one repeated adjacent-block pattern.

**Reasoning procedure:** Confirm each label, arm, numerator, denominator and printed percentage directly; compute the labeled fraction; allow half-unit rounding of every input and output; calculate the remaining interval gap divided by the absolute printed percentage. Each relative discrepancy exceeds 0.05. Model-based estimates or an assumed alternative denominator are not involved.

**Calculation:** For numerator n and denominator d, the permissive recomputed percentage interval runs from 100(n−0.5)/(d+0.5) to 100(n+0.5)/(d−0.5). The printed whole-percentage interval runs from p−0.5 to p+0.5. Relative discrepancy is the disjoint-interval gap divided by the absolute printed percentage.

| Exact cell | Printed triple | Direct percentage | Recomputed half-unit interval, % | Printed interval, % | Gap, percentage points | Relative discrepancy |
|---|---|---:|---|---|---:|---:|
| Ineffective cough / hypercapnic HFNC alone | 14/45 (69) | 31.111111 | [29.670330, 32.584270] | [68.5, 69.5] | 35.915730 | 0.520518 |
| Ineffective cough / hypercapnic HFNC with NIV | 16/59 (73) | 27.118644 | [26.050420, 28.205128] | [72.5, 73.5] | 44.294872 | 0.606779 |
| Abundant secretions / hypercapnic HFNC alone | 20/46 (57) | 43.478261 | [41.935484, 45.054945] | [56.5, 57.5] | 11.445055 | 0.200790 |
| Abundant secretions / hypercapnic HFNC with NIV | 23/61 (62) | 37.704918 | [36.585366, 38.842975] | [61.5, 62.5] | 22.657025 | 0.365436 |

All four remain disjoint even under half-unit allowances for integer counts. Using full column totals 48/63 also does not generate the printed percentages; the labeled available-case fractions remain the primary comparator.

**Affected result or extracted value:** Baseline prevalence of ineffective cough and abundant secretions among hypercapnic patients in each randomized arm, including each printed count, available denominator and percentage.

**Why context does not resolve it:** Route A, category 3 includes count/denominator/percentage discrepancies within one display. The printed percentages remain extractable magnitudes beyond tolerance even when fractions allow a reconstructed alternative; no final field is thereby selected.

**Alternative source-grounded interpretations:** The adjacent chronic-lung-disease row prints 33 (69) and 46 (73), suggesting a possible carried percentage pair for cough, but the production mechanism is unestablished and does not itself explain secretions. An unlabeled different population/quantity is possible but unsupported by labels/footnotes. Hypercapnic plus nonhypercapnic inputs reproduce the main counts: cough 51+14=65 and 70+16=86, with denominators 239+45=284 and 263+59=322; secretions 101+20=121 and 91+23=114, with denominators 242+46=288 and 265+61=326. This corroboration does not establish intended final fields or a correction.

**Mechanical evidence recheck:** Direct native extraction and a fresh CPU source-page raster confirmed all four triples, labels and headings. Independent interval arithmetic reproduced every discrepancy without transcription correction. No arithmetic input is missing; intended table fields, alternate-population definitions and production explanation are unavailable. The remaining question is which values/population the four percentages are intended to represent.

**Potential downstream evidence impact:** An extractor could copy 69%/73% cough prevalence or 57%/62% secretion prevalence despite the incompatible explicit fractions. If confirmed, the issue could affect baseline subgroup-prevalence extraction; it does not establish a changed primary treatment effect, propagation or paper-level conclusion.

## Downstream Evidence-Chain Considerations

These cards distinguish endpoint-definition coding, model-prespecification mapping, analysis availability and baseline-prevalence extraction. A systematic review, meta-analysis or guideline evidence table may copy a printed definition, model label, available estimate or descriptive percentage. Preserving source locations and the distinction between reported quantities, planned specifications and unavailable outputs helps keep those extraction choices traceable.

Any downstream relevance remains conditional on human adjudication. The supplied package does not establish that an inconsistency propagated, changed an evidence-synthesis result or altered a clinical conclusion. No replacement analysis or numerical correction is selected by this review.

## Limitations and Missing Definitions

No separate predefined SAP/amendment, participant-level data, event/censoring records or missing Cox/subgroup outputs was supplied. The data-sharing statement says data are not available. These limits prevent establishing implementation, nonperformance, model replacement, intended alternative estimates or participant reclassification; absence claims apply to this supplied package only.

C001 lacks an operational tachypnea-duration algorithm and duration records. C002 lacks prognostic Cox coefficients, predictor lists and outputs. C003 lacks the separate prespecification mapping, forced-variable identities and model coefficients/covariance. C004 lacks disease/breathing-test subgroup definitions, counts, contrasts and interactions. C005 has all arithmetic inputs but lacks intended final fields, any alternate percentage population and the production explanation. The cards retain the corresponding source-grounded alternatives.

Some row-specific contributors, exact/t/rank-test choices, interval algorithms and continuous-difference estimands are not specified. Rounded summaries do not authorize reconstructing participant-level distributions or imposing a common inferential convention. The review does not infer a candidate solely from those absent details.

Legacy raster and some OCR engine versions were unrecorded. Protocol p. 42 native extraction is partial but its complete raster was visually mapped; main pp. 5–8 lack OCR but have usable layout text and images. Complete source coverage and direct confirmation close scientific coverage despite those derivative limitations. Further detail is in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

Routing preflight is PASS: run model gpt-6.1-sol, source DEFAULT, coordinator high, ordinary specialists medium, statistical/screen/recheck/audit specialists high. Coordinator inference, fixed model matrix and all ten named presets were checked. Execution mode is INTERACTIVE_CLI and provider is CURRENT_SESSION; no provider credentials or configuration were introduced. Every mandatory specialist stage used a distinct fresh runtime agent. The complete [routing record](review_1_6_2/routing_preflight.md) and [execution manifest](review_1_6_2/agent_execution_manifest.md) are retained.

| Stage | Actual agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/asset_curation | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapping | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_mapping | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_check | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_source_check | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistical_pass_one | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | root/initial_screening | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistical_pass_two | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | root/report_generation | gpt-6.1-sol | medium | FRESH_SPAWN |

The independent audit confirmed unchanged SHA-256 values for all four direct PDFs and all 152 hashed reused assets. The before records are [source_hashes_before.sha256](review_1_6_2/source_hashes_before.sha256) and [reused_artifact_hashes_before.sha256](review_1_6_2/reused_artifact_hashes_before.sha256). The coordinator repeats and records integrity verification after report assembly. Sources and legacy audit artifacts are preserved. Fresh derivatives, engine/command provenance and CPU processing are documented in the [tooling record](review_1_6_2/tooling_record.md), asset inventory and recheck.

The current [candidate ledger](review_1_6_2/candidate_ledger.md), [recheck](review_1_6_2/verification/evidence_recheck.md), [quality audit](review_1_6_2/quality/evidence_quality_audit.md) and this report contain the identical stable set C001–C005. Every card copies its classification values from the ledger table. HTML rendering and final mechanical validation follow complete Markdown assembly; the coordinator records their final result separately.

### Reproducibility performance

- **Target basis:** Four PDF-only sources with 69 total pages and 0 initially fresh-required pages; all pages have source-matched reusable layout text or rendered/OCR evidence, including a scanned French plan appendix on p. 42. Main and supplemental tables and figures need visual mapping, and the 48-page protocol requires complete prospective-design mapping. No Office conversion or new OCR is initially needed. Allow concurrent main/support mapping, concurrent three-checker review, independent inclusion screen, evidence recheck, distinct statistical pass 2, quality audit and report assembly: eight bounded review waves after curation. Target reflects reuse burden and visual/plan complexity, not page count alone.
- **Total source units:** 69
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T04:55:30Z
- **Finished UTC:** 2026-10-11T05:36:42Z
- **Observed elapsed minutes:** 41.20
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete high-effort two-pass statistical review and 59-row exclusion audit; full five-candidate report assembly across eight review waves; post-assembly consolidation of 47 pass-1 records for mechanical validation
