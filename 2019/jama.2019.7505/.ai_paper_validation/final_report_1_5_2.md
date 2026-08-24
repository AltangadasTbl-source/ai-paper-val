# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

Every observation in this report is a **Pending Human Adjudication** quality-control candidate. This review does not assign validity, importance, severity, acceptance, exclusion, correction, or a paper-level conclusion.

## Executive Quality-Control Summary

Fresh source-first processing of six supplied PDFs (100 of 100 physical PDF-page units mapped) identified four distinct quantitative reporting-consistency candidates: one abstract/table confidence-interval mismatch, one count-to-risk-ratio reconciliation issue, and two measure/outcome-label issues. The review is limited to supplied-package evidence. Small preventable reporting defects can matter to later evidence extraction, but this report does not claim downstream propagation, conclusion change, or harm.

## Package and Fresh-Processing Provenance

The evidence set was the six direct supplied PDFs only: DOC-001 main article; DOC-002 protocol; DOC-003 protocol-change overview; DOC-004 final statistical analysis plan (SAP); DOC-005 online supplement; and DOC-006 data-sharing statement. Existing audit derivatives were preserved but excluded from evidence and discovery.

Fresh local processing created native and layout text for all source PDFs and rendered 67 result-relevant pages. Native/layout text was usable for every result-relevant page, so no OCR was required. No web, GPU, Office conversion, raw data, analysis code, or external evidence was used.

## Scope, Complete Coverage, and Exclusions

All six direct sources were fully mapped: DOC-001 14/14 pages, DOC-002 36/36, DOC-003 3/3, DOC-004 3/3, DOC-005 43/43, and DOC-006 1/1; total 100/100 (100%). The review checked numeric, denominator, arithmetic, inferential, cross-document, effect-measure/label/scale, and rate/count relationships where the supplied sources supported comparison.

There was no review queue, top-N selection, candidate cap, or deferred-by-cap category. A visually resolved apparent ARISCAT extraction ambiguity and the undefined eTable 8 effect-measure heading were retained as non-candidate limitations because they did not meet the supplied-source contradiction threshold. A coherent display-zero P value was never registered solely because of its display notation.

## Quantitative and Statistical Relationship Coverage

The complete numeric/reporting inventory contains 69 mapped relationships: N001-N049 and N200-N219. The complete inferential-statistical inventory contains 53 relationships: S001-S038 and S200-S214.

Statistical pass 1 was performed by `root/statistics_pass_1` (gpt-5.6-terra, high) and statistical pass 2 by the distinct `root/statistics_pass_2` (gpt-5.6-terra, high). Both passes covered all 53 statistical relationships. Pass 2 revisited the complete cross-lane ledger and all mechanical recheck facts; it made no new proposal.

## Candidate Index

| ID | Candidate | Category | Status |
|---|---|---|---|
| [C001](#c001--hypoxemia-confidence-interval-endpoint-sign-differs-between-abstract-and-table-3) | Hypoxemia CI endpoint sign differs between abstract and Table 3 | Cross-document numeric inconsistency | Pending Human Adjudication |
| [C002](#c002--dic-row-finite-risk-ratio-and-narrow-interval-do-not-reconcile-with-zero-comparator-events) | DIC finite risk ratio/interval does not reconcile with zero comparator events | Statistical reporting inconsistency | Pending Human Adjudication |
| [C003](#c003--protocol-analysis-sentence-combines-odds-ratio-and-relative-risk-labels) | Protocol sentence combines odds-ratio and relative-risk labels | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C004](#c004--efigure-11-mortality-values-are-described-as-extra-pulmonary-complications) | eFigure 11 mortality values are described as extra-pulmonary complications | Measure, label, or scale inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Hypoxemia confidence-interval endpoint sign differs between abstract and Table 3

**Status:** Pending Human Adjudication

**Candidate statement:** The abstract and Table 3 print opposite signs for the upper endpoint of the otherwise matched high-minus-low hypoxemia risk-difference confidence interval.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001, [`jama_bluth_2019_oi_190055_16092.pdf` — PDF p. 1, abstract](<../jama_bluth_2019_oi_190055_16092.pdf#page=1>) and [PDF p. 9, Table 3](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>).

**Source evidence:** Both locations report intraoperative hypoxemia of 49/989 (5.0%) versus 134/987 (13.6%), a difference of -8.6 percentage points, and P < .001. The abstract prints 95% CI -11.1 to +6.1; Table 3 prints -11.1 to -6.1 and RR 0.51 (0.40 to 0.65).

**Reported-versus-comparator:** Abstract upper endpoint +6.1 versus Table 3 upper endpoint -6.1 for the same matched result.

**Reasoning procedure:** Match population, outcome, treatment order, point estimate, confidence level, precision, and P value across locations, then compare interval endpoints including sign.

**Calculation:** 5.0 - 13.6 = -8.6 percentage points. The printed upper endpoint changes by 12.2 percentage points. A direct unpooled Wald calculation from the displayed counts is a diagnostic approximation of about -11.15 to -6.09 percentage points; it supports Table 3's displayed precision but does not determine which source should be corrected.

**Alternative source-grounded interpretations:** Either the abstract or Table 3 may contain the production error. A dropped abstract minus sign is plausible, but the package does not provide an authoritative analysis-output record or designate an authoritative display.

**Mechanical evidence recheck:** The cited pages, printed values, comparator, and sign mismatch were independently found and reproduced. Necessary counts, denominators, treatment order, confidence level, and endpoints are available; the exact published interval implementation and authoritative output are unavailable. Direct observation is the sign mismatch; any production explanation is inferred.

**Quality-control relevance:** The two locations cannot both represent the same interval at the displayed precision and therefore require human confirmation.

**Potential downstream evidence impact:** If confirmed, an abstract-focused extractor could copy an interval crossing zero while a table-focused extractor could copy an interval wholly below zero. No propagation or conclusion change is claimed.

**Human verification steps:** Inspect the publisher proof/source and analysis output for the hypoxemia high-minus-low risk-difference CI; confirm the intended upper endpoint and align every supplied representation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — DIC row finite risk ratio and narrow interval do not reconcile with zero comparator events

**Status:** Pending Human Adjudication

**Candidate statement:** The Table 3 DIC row prints 1 versus 0 events but a finite RR 2.00 with a narrow interval excluding 1; the source does not supply the estimator needed to reconcile these values.

**Category:** Statistical reporting inconsistency

**Exact source locations:** DOC-001, [`jama_bluth_2019_oi_190055_16092.pdf` — PDF p. 9, Table 3](<../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [PDF p. 10, continued Table 3 footnotes](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>); and [PDF p. 4, binary-outcome method](<../jama_bluth_2019_oi_190055_16092.pdf#page=4>).

**Source evidence:** The row prints disseminated intravascular coagulation as 1/989 (0.1%) versus 0/987, absolute difference 0.1 (95% CI -0.1 to 0.3), RR 2.00 (95% CI 1.91 to 2.09), and P > .99. Table footnotes label the effect as a risk ratio and identify broad interval/test methods.

**Reported-versus-comparator:** A finite RR 2.00 with interval [1.91, 2.09] is displayed against a comparator risk of zero; the same row prints P > .99.

**Reasoning procedure:** Apply the ordinary printed risk-ratio identity to the displayed event counts, then identify the exact source-supplied method information needed for an alternative finite estimate. The interval/P comparison remains conditional because the source names different broad procedures without complete implementations.

**Calculation:** High risk = 1/989 = 0.0010111; low risk = 0/987 = 0. Thus (1/989)/(0/987) has a zero denominator and is not a finite direct RR. The printed interval excludes 1. No replacement RR, CI, or P value is calculated.

**Alternative source-grounded interpretations:** An unstated zero-cell correction, alternate estimator, cell alignment issue, or transcription error could explain part of the display. The supplied package does not identify a zero-cell rule, exact interval formula/software call, chi-square variant, or row-specific alternate population.

**Mechanical evidence recheck:** The row, denominators, RR, CI, P value, table footnotes, and general method were independently found. The direct count-to-RR conflict was reproduced. Missing inputs are the zero-cell/estimator rule and exact inferential implementations; possible explanations are not treated as established.

**Quality-control relevance:** The printed effect and interval require a stated reconciliation rule before their relationship to the displayed 1-versus-0 events can be understood.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a precise finite RR/CI without the undisclosed rule needed to reconcile it with the displayed counts. No propagation or paper-level conclusion change is claimed.

**Human verification steps:** Retrieve the analysis output or method call; identify the zero-cell rule, estimator, interval formula, and hypothesis-test implementation; then confirm whether the RR, CI, and P-value cells align with the 1-versus-0 row.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol analysis sentence combines odds-ratio and relative-risk labels

**Status:** Pending Human Adjudication

**Candidate statement:** A protocol planned-analysis sentence joins “odds ratio” and “relative risks” without a separator, alternative-analysis definition, or conversion rule, while the final SAP specifies a primary risk ratio.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-002, [`joi190055supp1_prod_16092.pdf` — physical PDF p. 23 (footer p. 22), section 8.2 Analysis](<../joi190055supp1_prod_16092.pdf#page=23>); comparator definitions in DOC-004, [`joi190055supp3_prod_16092.pdf` — PDF p. 2](<../joi190055supp3_prod_16092.pdf#page=2>) and [PDF p. 3](<../joi190055supp3_prod_16092.pdf#page=3>).

**Source evidence:** DOC-002 states that “the odds ratio relative risks with corresponding 95% confidence levels interval” will be calculated using logistic regression. DOC-004 identifies the primary effect as a risk ratio and separately uses odds ratios for specified exploratory analyses.

**Reported-versus-comparator:** The uninterrupted compound protocol label “odds ratio relative risks” versus the final SAP's explicit primary-outcome risk-ratio label and distinct exploratory odds-ratio contexts.

**Reasoning procedure:** Compare the exact planned-analysis measure labels. Odds ratio and risk ratio are distinct measures; one output must identify the intended measure or expressly identify separate analyses/conversion.

**Calculation:** No arithmetic is needed. The reproducible comparison is the uninterrupted compound label against the SAP's measure-specific wording.

**Alternative source-grounded interpretations:** The phrase may be an editing artifact; the final SAP may supersede earlier wording by selecting risk ratio for the primary outcome; or distinct analyses may have been intended. The package does not resolve which explanation applies.

**Mechanical evidence recheck:** Physical PDF p. 23 visibly contains the uninterrupted phrase; footer page 22 is an internal footer, not the PDF page locator. The SAP comparator pages explicitly distinguish primary risk-ratio and exploratory odds-ratio contexts. The intended punctuation, estimand, and any conversion are missing.

**Quality-control relevance:** The protocol's printed planned-analysis effect-measure label is internally indeterminate and should be clarified by a human reviewer.

**Potential downstream evidence impact:** If confirmed, a protocol or registry extractor could code the planned effect measure ambiguously. No claim is made that the final analysis used the wrong estimand or that conclusions changed.

**Human verification steps:** Inspect the archived protocol source/proof and associated analysis plan; determine whether section 8.2 intended an odds ratio, a risk ratio, or distinct analyses, and clarify the archived wording if appropriate.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eFigure 11 mortality values are described as extra-pulmonary complications

**Status:** Pending Human Adjudication

**Candidate statement:** eFigure 11's narrative calls its displayed mortality values postoperative extra-pulmonary complications, although its title, axis, effect label, and matching Table 3 values identify five-day mortality.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-005, [`joi190055supp4_prod_16092.pdf` — PDF p. 41, eFigure 11](<../joi190055supp4_prod_16092.pdf#page=41>); comparator [PDF p. 40, eFigure 10](<../joi190055supp4_prod_16092.pdf#page=40>); and DOC-001, [`jama_bluth_2019_oi_190055_16092.pdf` — PDF p. 10, Table 3](<../jama_bluth_2019_oi_190055_16092.pdf#page=10>).

**Source evidence:** eFigure 11 is titled “Probability of death in the first 5 postoperative days,” labels the effect “hazard ratio for 5-day mortality,” and prints 0.5% versus 0.3%, HR 1.67 (0.40 to 6.97), P = .484. Its narrative calls those same values “the rate of postoperative extra-pulmonary complications.” eFigure 10 separately prints extra-pulmonary complications of 16.9% versus 15.2%, HR 1.12; Table 3 matches the eFigure 11 mortality values.

**Reported-versus-comparator:** The eFigure 11 narrative outcome noun conflicts with its mortality title, axis, effect label, and matched mortality values; eFigure 10 supplies the distinct extra-pulmonary-complication comparator.

**Reasoning procedure:** Match title, axis, effect label, percentages, HR/CI, and cross-document values, then check whether the narrative names the same outcome.

**Calculation:** 5/989 = 0.5056% and 3/987 = 0.3040%, rounding to 0.5% and 0.3%. These mortality values are not rounding variants of the separately displayed 16.9% and 15.2% extra-pulmonary-complication values.

**Alternative source-grounded interpretations:** Carry-forward wording from neighboring eFigure 10 is plausible, or the sentence may refer to a neighboring figure, but neither explanation is stated in the supplied sources.

**Mechanical evidence recheck:** The title, axis, mortality label, values, HR/CI/P, local narrative noun, eFigure 10 comparator, and Table 3 mortality row were independently found and matched. The direct observation is the conflicting outcome noun; the production mechanism and appropriate correction remain unknown.

**Quality-control relevance:** A figure narrative should identify the same outcome as its displayed values and effect estimate.

**Potential downstream evidence impact:** If confirmed, an extractor could misclassify a five-day mortality effect as an extra-pulmonary-complication effect. No propagation, harm, or conclusion change is claimed.

**Human verification steps:** Inspect the final eFigure 11 proof/source, confirm the outcome noun associated with 0.5%/0.3% and HR 1.67, and determine whether the figure narrative or another linked representation needs correction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed by human adjudication, the candidates identify specific fields that could be copied differently by abstract/table, protocol, or figure extractors: a confidence-interval endpoint, a finite effect estimate and interval, a planned effect-measure label, or an outcome label. This is a bounded evidence-extraction concern only; the supplied package does not establish downstream reuse, propagation, conclusion change, or harm.

## Limitations and Missing Definitions

- The package contains published PDFs but no raw data, analysis code, unrounded output, publisher production source, or author clarification.
- Several tables and figures lack enough test, variance, repeated-measures, interval-construction, or group-sequential implementation detail for strict reconstruction; unreported conventions were not imported.
- The DIC row does not identify a zero-cell correction or alternate estimator; no replacement RR, CI, or P value is proposed.
- eTable 8's “Effect Estimate 95% CI” header omits a measure label but has no conflicting printed label, so it remains a limitation rather than a candidate.
- The DOC-001 ARISCAT phrase was visually resolved as superscript reference 18 following “score,” followed by “of 26 or greater”; it is not a candidate.
- No coherent display-zero P value was treated as a candidate.
- DOC-006 is a data-sharing statement with no result-bearing numeric/statistical relationship.

## Human Adjudication Checklist

For each candidate, confirm the cited locations against authoritative publication/analysis materials if available; determine whether the printed values or labels represent a reportable defect; record validity, importance, action, initials, and notes in the card template; and preserve the stable candidate ID regardless of the human decision.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

Fresh source hashes recorded before preprocessing and recomputed during quality audit matched for all six direct PDFs. The source inventory records these SHA-256 values: DOC-001 `a76e0d8789cfcdbb51d86edaaf407e29ada6f2c0d3a2a8a7b95bb50565d12bc1`; DOC-002 `60c2f9990f89ad4a7199ea7b682a6c5b80f84532c589cacace5778fce686e1e2`; DOC-003 `0d830c7fcdb532f85c16b9ce4afd2e6e8a8577a4758a66aadcc5cbbb60bf73f9`; DOC-004 `768cc455241d2cfa437b613adcfd878d03ceff6ddcd324819f057652d3a9a11b`; DOC-005 `93774bc97dc923b3d322fa299c2659f014ed2ff9ee12226c6e8c4caee6f3a605`; DOC-006 `7ff68bf44095d24434ed4f366e4e13dbc9c125b10f1f802015c19e0acae25385`.

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh_source_preprocessor | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_quantitative_mapper | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_consistency_reviewer | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_consistency_reviewer | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_rechecker | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality_auditor | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation.md` |

### Reproducibility Performance

- **Target basis:** Six supplied PDFs totaling 100 pages require fresh native and layout extraction, complete mapping, two statistical passes, and report regeneration; this is close to the 102-unit calibration package but has 100 fresh-required units rather than 81, so a bounded 40-60 minute planning range is selected.
- **Total source units:** 100
- **Fresh-source units:** 100
- **Target elapsed minutes:** 40-60
- **Started UTC:** 2026-08-24T01:52:52Z
- **Finished UTC:** 2026-08-24T02:27:53Z
- **Observed elapsed minutes:** 35.0
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token Accounting and Cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) | Estimated complete token cost (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 | __ |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 | __ |

Token amounts, when finalized, are authoritative response-level runtime/API counts through Finished UTC. Costs are token-only API-equivalent estimates under the dated pricing snapshot, not invoices; non-token tools, containers, storage, subscriptions, taxes, and other vendor charges are excluded. See `review_1_5_2/token_usage_summary.md` for per-agent detail.
