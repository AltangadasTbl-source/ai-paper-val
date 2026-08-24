# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

All observations in this report are **Pending Human Adjudication**. They are source-grounded quantitative reporting quality-control candidates, not conclusions about the paper, its authors, study validity, or clinical consequences.

## Executive Quality-Control Summary

Fresh source-first processing of the three supplied PDFs identified 11 stable candidate consistency observations (C001-C011). The work covered all 44 supplied PDF pages, 61 numeric/reporting relationships, and 67 inferential-statistical relationships in two independent statistical passes. No candidate was registered solely because of a display-zero P value; no mapped result used that display format.

The report preserves a corrected discovery record for C004: direct recheck shows `23/238 (9.66)`, which reconciles at two decimal places. The retained stable ID documents that correction and is not presented as a source percentage defect.

## Package and Fresh-Processing Provenance

Only the supplied direct research sources were used:

| Source ID | Source | Role | Fresh units | Hash (SHA-256) |
|---|---|---|---:|---|
| DOC-001 | `jama_wang_2018_oi_180070.pdf` | Main article | 10 PDF pages | `f921847452d4f5ab012a3eaaa58f25542a73c2f06a858974efc443be4af70fb9` |
| DOC-002 | `joi180070supp1_prod.pdf` | Supplement 1 | 25 PDF pages | `5faf07d9e18fb1b9dcc415818622846fb502b410d67255be7ab28aca5e52d138` |
| DOC-003 | `joi180070supp2_prod.pdf` | Supplement 2 | 9 PDF pages | `78ebed75675211c520c6eae88b8a1963c9b1f00dc66b2b6ff324d957a1e39645` |

Fresh native text and coordinate-layout extraction covered all 44 pages; 13 result-relevant pages also received fresh full-page visual confirmation. No result-relevant page required OCR. Legacy audit derivatives were excluded from the evidence chain.

## Scope, Complete Coverage, and Exclusions

Each direct source has 0 reusable units, fresh-required units equal to its total, and mapped units equal to its total: 44/44 total and fresh-required units were mapped. The review addressed numeric/arithmetic, denominator/proportion/total, statistical, cross-document, measure/label/scale, rate-versus-count, and concrete analysis-unit/population inconsistencies.

It did not perform a broad study-design, clinical, novelty, misconduct, or raw-data audit. Planned quantities were not treated as observed results, and different explicitly stated analysis sets were not treated as competing denominators. Coherent finite-precision P-value display zero would be excluded as a stand-alone candidate.

## Quantitative and Statistical Relationship Coverage

- Numeric/reporting relationships: 61/61 mapped and checked.
- Statistical relationships: 67/67 mapped; statistical pass 1 marked all 67 `PASS_1_COMPLETE` and the distinct statistical pass 2 marked all 67 `PASS_2_COMPLETE` after review of the full ledger and mechanical recheck.
- Cross-source matching: all 61 numeric/reporting and 67 statistical relationships were matched where population, time point, contrast, model, measure, scale, reference condition, and precision permitted comparison.
- Stable candidates: C001-C011; one genuine duplicate discovery record for the LDL boundary was merged before stable-ID assignment. No count cap, ranking, queue, or deferred-by-cap selection was used.

## Candidate Index

| ID | Candidate statement | Category |
|---|---|---|
| [C001](#c001--table-1-cadprevious-mi-percentage-does-not-reconcile-with-3112400) | CAD/previous-MI percentage versus displayed count and group total | Numeric or arithmetic inconsistency |
| [C002](#c002--ldl-eligibility-threshold-is-printed-as-both-100-and-100-mgdl) | LDL eligibility boundary differs across sources | Measure, label, or scale inconsistency |
| [C003](#c003--exact-20-patients-per-cluster-statement-conflicts-with-the-801-baseline-total) | Per-cluster statement versus baseline total | Denominator, proportion, or total inconsistency |
| [C004](#c004--direct-recheck-finds-the-rtpa-cell-prints-966-and-reconciles-with-23238) | Corrected rtPA discovery transcription retained after registration | Denominator, proportion, or total inconsistency |
| [C005](#c005--etable-4-discharge-antithrombotics-control-percentage-does-not-reconcile-with-21412400) | Discharge-antithrombotics fraction versus percentage | Denominator, proportion, or total inconsistency |
| [C006](#c006--etable-4-af-anticoagulation-control-percentage-does-not-reconcile-with-39174) | AF-anticoagulation fraction versus percentage | Denominator, proportion, or total inconsistency |
| [C007](#c007--etable-4-lipid-lowering-control-percentage-does-not-reconcile-with-14391586) | Lipid-lowering fraction versus percentage | Denominator, proportion, or total inconsistency |
| [C008](#c008--etable-4-antidiabetic-medication-control-percentage-does-not-reconcile-with-557688) | Hypoglycemic-therapy fraction versus percentage | Denominator, proportion, or total inconsistency |
| [C009](#c009--in-hospital-death-absolute-difference-p-value-conflicts-with-its-displayed-95-ci) | In-hospital-death absolute-difference CI versus P value | Statistical reporting inconsistency |
| [C010](#c010--composite-adherence-has-conflicting-patient-level-and-care-opportunity-analysis-descriptions) | Composite analysis unit differs across descriptions | Analysis-unit or population inconsistency |
| [C011](#c011--dvt-prophylaxis-window-is-labeled-as-both-within-48-hours-and-by-end-of-hospital-day-2) | DVT timing definition differs across sources | Measure, label, or scale inconsistency |

## Candidate Evidence Cards

## C001 — Table 1 CAD/previous-MI percentage does not reconcile with 311/2400

**Candidate statement:** The Table 1 intervention CAD/previous-MI cell prints a percentage that does not reproduce from the displayed count and group total, conditional on 2400 being the row denominator.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 6](<../jama_wang_2018_oi_180070.pdf#page=6>), Table 1, CAD/previous myocardial infarction, intervention column.

**Source evidence:** The cell visibly prints `311 (13.05)` and the intervention column total is 2400.

**Reported-versus-comparator:** Reported `13.05%` versus `311/2400 × 100`.

**Reasoning procedure:** Apply the displayed group total as the denominator and nearest rounding at the shown relevant precision; keep an unprinted row denominator as an alternative rather than assuming it absent.

**Calculation:** `311/2400 × 100 = 12.9583…%`, which rounds to `13.0%` at one decimal or `12.96%` at two decimals, not `13.05%`.

**Alternative source-grounded interpretations:** An unstated row-specific nonmissing denominator or a production transcription could explain the cell; neither is supplied.

**Mechanical evidence recheck:** Location, printed count, percentage, group total, and arithmetic were reproduced. The missing inputs are a CAD-row denominator or missingness count; the source-grounded alternative is a hidden nonmissing denominator.

**Quality-control relevance:** The displayed baseline prevalence cannot be reproduced from the visible count and group total under the stated arithmetic rule.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a baseline CAD/previous-MI prevalence that does not reproduce from the printed count and group total. This report does not establish an effect on outcomes or conclusions.

**Human verification steps:** Confirm the cell and Table 1 header in the cited PDF, then inspect the table-production data for a row-specific denominator, missingness count, or intended percentage.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — LDL eligibility threshold is printed as both >100 and ≥100 mg/dL

**Candidate statement:** The reported lipid-lowering measure uses `>100 mg/dL`, while supplied protocol/eTable definitions use `≥100 mg/dL` with additional eligibility routes.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 3](<../jama_wang_2018_oi_180070.pdf#page=3>) Outcomes and [jama_wang_2018_oi_180070.pdf — PDF p. 7](<../jama_wang_2018_oi_180070.pdf#page=7>) Table 2; DOC-002, [joi180070supp1_prod.pdf — PDF p. 14](<../joi180070supp1_prod.pdf#page=14>) and [joi180070supp1_prod.pdf — PDF p. 15](<../joi180070supp1_prod.pdf#page=15>); DOC-003, [joi180070supp2_prod.pdf — PDF p. 3](<../joi180070supp2_prod.pdf#page=3>) eTable 1.

**Source evidence:** DOC-001 says more than/`>100 mg/dL`; DOC-002 and DOC-003 print `≥100 mg/dL` and also describe prior lipid-lowering treatment and undocumented LDL routes.

**Reported-versus-comparator:** `LDL >100 mg/dL` versus `LDL ≥100 mg/dL` plus the detailed eligibility routes.

**Reasoning procedure:** Compare the explicitly printed inequality predicates and complete eligibility wording for the same discharge performance measure.

**Calculation:** At `LDL = 100 mg/dL`, `100 > 100` is false and `100 ≥ 100` is true; the two displayed boundary definitions are therefore not set-equivalent.

**Alternative source-grounded interpretations:** The main article may abbreviate the detailed specification; the package does not identify which rule constructed the reported denominators.

**Mechanical evidence recheck:** All cited symbols and eligibility text were found and matched. Missing inputs are the implemented data rule, number of exactly-100 values, and whether the article label intentionally incorporated the other routes.

**Quality-control relevance:** The boundary and eligibility routes affect interpretation of the measure and its denominators.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer or data extractor could copy a different LDL eligibility definition for this performance measure. The supplied evidence does not show that any patient was differently classified.

**Human verification steps:** Confirm each cited predicate, then inspect the analysis dataset, codebook, or prespecified measure form for the implemented boundary and eligibility routes.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Exact 20-patients-per-cluster statement conflicts with the 801 baseline total

**Candidate statement:** The unqualified 20-patients-per-cluster statement does not equal the reported 801 baseline patients when paired with 40 hospitals.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 2](<../joi180070supp2_prod.pdf#page=2>) eAppendix; DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 3](<../jama_wang_2018_oi_180070.pdf#page=3>) and [jama_wang_2018_oi_180070.pdf — PDF p. 6](<../jama_wang_2018_oi_180070.pdf#page=6>) Table 1.

**Source evidence:** DOC-003 states that 20 patients per cluster were prospectively included; DOC-001 identifies 40 hospitals and Table 1 prints 801 baseline-survey patients.

**Reported-versus-comparator:** Reported baseline total `801` versus `20 patients/cluster × 40 clusters`.

**Reasoning procedure:** Treat the printed per-cluster count as exact unless the source qualifies it as a target or approximation, then compare its product with the printed total.

**Calculation:** `20 × 40 = 800`, one fewer than 801.

**Alternative source-grounded interpretations:** One cluster may have included an additional patient, or 20 may describe a target; neither qualification appears in the eAppendix sentence.

**Mechanical evidence recheck:** The locations, statement, hospital count, and Table 1 total were found and reproduced. Missing inputs are cluster-specific counts and confirmation that all 40 Table 1 hospitals map one-for-one to the described clusters.

**Quality-control relevance:** The comparison concerns the baseline-sample denominator used to describe baseline characteristics.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a baseline enrollment total or per-cluster description that is not mutually reproducible. No downstream conclusion change is established.

**Human verification steps:** Confirm the cited wording and inspect the cluster-level baseline enrollment record or recruitment specification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Direct recheck finds the rtPA cell prints 9.66 and reconciles with 23/238

**Candidate statement:** A discovery transcription recorded `9.6`; direct PDF recheck instead establishes `23/238 (9.66)`, which reconciles at two decimals. The registered ID is retained to preserve the review record, without asserting a source percentage defect.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, IV rt-PA 2 Hour, control column.

**Source evidence:** The direct PDF visibly prints `23/238 (9.66)`; the paired intervention cell prints `46/254 (18.11)`.

**Reported-versus-comparator:** Direct-source `23/238 (9.66)` versus the earlier discovery transcription `23/238 (9.6)`; the direct-source fraction versus its two-decimal percentage.

**Reasoning procedure:** Give priority to the supplied PDF and reapply the fraction-to-percentage calculation at the two-decimal precision visibly printed in the row.

**Calculation:** `23/238 × 100 = 9.6639…%`, rounding to `9.66%`; `46/254 × 100 = 18.1102…%`, rounding to `18.11%`.

**Alternative source-grounded interpretations:** The row may intentionally use two-decimal precision or a production-formatting precision convention; the direct printed fraction and percentage themselves reconcile.

**Mechanical evidence recheck:** The cited location, direct PDF text, comparator, and arithmetic were reproduced. The necessary fraction and percentage inputs are available; the remaining question is whether row-specific precision was intentional.

**Quality-control relevance:** Preserving the stable ID with its corrected fact prevents the earlier discovery transcription from being reused as source evidence.

**Potential downstream evidence impact:** If a discovery transcription rather than the source were reused, a data extractor could copy `9.6` instead of the source’s `9.66`. The source does not establish that any published result requires correction.

**Human verification steps:** Open the cited eTable cell, confirm the two-decimal display, and inspect the table-production record if the intended row precision needs clarification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 4 discharge-antithrombotics control percentage does not reconcile with 2141/2400

**Candidate statement:** The eTable 4 control percentage does not reproduce from the printed discharge-antithrombotics fraction.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, discharge-antithrombotics control cell.

**Source evidence:** The cell prints `2141/2400 (89.3)`.

**Reported-versus-comparator:** Reported `89.3%` versus `2141/2400 × 100`.

**Reasoning procedure:** Apply nearest one-decimal percentage rounding to the displayed numerator and denominator.

**Calculation:** `2141/2400 × 100 = 89.2083…%`, which rounds to `89.2%`, not `89.3%`.

**Alternative source-grounded interpretations:** The package gives no alternate denominator or rounding rule.

**Mechanical evidence recheck:** The location, fraction, percentage, and arithmetic were reproduced. The missing inputs are any unprinted denominator or nonstandard rounding convention.

**Quality-control relevance:** The printed sensitivity-analysis percentage cannot be reproduced from its visible fraction.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a control adherence percentage that does not reproduce from the displayed fraction. No effect on conclusions is claimed.

**Human verification steps:** Confirm the eTable cell and inspect the tabulation data for the intended count, denominator, percentage, and rounding rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 4 AF-anticoagulation control percentage does not reconcile with 39/174

**Candidate statement:** The eTable 4 control AF-anticoagulation percentage does not reproduce from the printed fraction.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, atrial-fibrillation/flutter anticoagulation control cell.

**Source evidence:** The cell prints `39/174 (22.5)`.

**Reported-versus-comparator:** Reported `22.5%` versus `39/174 × 100`.

**Reasoning procedure:** Apply nearest one-decimal percentage rounding to the displayed fraction.

**Calculation:** `39/174 × 100 = 22.4138…%`, which rounds to `22.4%`, not `22.5%`.

**Alternative source-grounded interpretations:** The package supplies no alternate denominator or percentage convention.

**Mechanical evidence recheck:** The source cell and calculation were reproduced; necessary displayed inputs are available. An unprinted denominator or rounding convention remains unknown.

**Quality-control relevance:** The control adherence proportion cannot be mechanically reproduced from the displayed fraction.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy a control adherence percentage that differs from the fraction shown in the supplied eTable. No propagation is asserted.

**Human verification steps:** Confirm the cited cell and inspect the sensitivity-analysis tabulation data and formatting rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — eTable 4 lipid-lowering control percentage does not reconcile with 1439/1586

**Candidate statement:** The eTable 4 control lipid-lowering percentage does not reproduce from the printed fraction.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, lipid-lowering control cell.

**Source evidence:** The cell prints `1439/1586 (90.8)`.

**Reported-versus-comparator:** Reported `90.8%` versus `1439/1586 × 100`.

**Reasoning procedure:** Apply nearest one-decimal rounding to the printed numerator and denominator; treat the distinct LDL-boundary issue as C002.

**Calculation:** `1439/1586 × 100 = 90.7314…%`, which rounds to `90.7%`, not `90.8%`.

**Alternative source-grounded interpretations:** The package supplies no alternate denominator or percentage convention.

**Mechanical evidence recheck:** The source cell, fraction, percentage, and arithmetic were reproduced. The applicable threshold-label comparison is separately captured in C002.

**Quality-control relevance:** The displayed sensitivity-analysis percentage cannot be reproduced from the visible fraction.

**Potential downstream evidence impact:** If confirmed, a meta-analysis or data extractor could copy a percentage that does not reproduce from the eTable fraction. This does not establish a change to any effect estimate.

**Human verification steps:** Confirm the cited cell and review the analysis-table source for the intended fraction, denominator, percentage, and rounding rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — eTable 4 antidiabetic-medication control percentage does not reconcile with 557/688

**Candidate statement:** The eTable 4 control hypoglycemic-therapy percentage does not reproduce from the printed fraction.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, hypoglycemic-therapy control cell.

**Source evidence:** The cell prints `557/688 (81.1)`.

**Reported-versus-comparator:** Reported `81.1%` versus `557/688 × 100`.

**Reasoning procedure:** Apply nearest one-decimal percentage rounding to the displayed fraction.

**Calculation:** `557/688 × 100 = 80.9593…%`, which rounds to `81.0%`, not `81.1%`.

**Alternative source-grounded interpretations:** The package supplies no alternate denominator or rounding rule.

**Mechanical evidence recheck:** The cited cell and arithmetic were reproduced. Necessary visible inputs are available; any hidden denominator or nonstandard convention is not supplied.

**Quality-control relevance:** The control-row percentage is not mechanically reproducible from its displayed numerator and denominator.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy a control hypoglycemic-therapy proportion that differs from the displayed fraction. No conclusion change is claimed.

**Human verification steps:** Confirm the cell and review the source data or table-production specification for the intended values.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — In-hospital-death absolute-difference P value conflicts with its displayed 95% CI

**Candidate statement:** The Table 3 in-hospital-death absolute-difference interval includes 0 while the adjacent same-column P value is `.009`.

**Category:** Statistical reporting inconsistency

**Exact source locations:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 8](<../jama_wang_2018_oi_180070.pdf#page=8>), Table 3, Death—In hospital row.

**Source evidence:** The adjusted absolute difference is `−0.7` with `95% CI, −1.1 to 0.2` and adjacent P=`.009`; the separately labelled HR is `.96 (95% CI, .90 to 1.02)` with P=`.14`.

**Reported-versus-comparator:** Same-column P=`.009` versus the displayed absolute-difference 95% CI `−1.1 to 0.2`.

**Reasoning procedure:** Check whether the displayed interval excludes its null value and use a rough CI-derived diagnostic only as a diagnostic, not as a replacement analysis.

**Calculation:** The absolute-difference CI includes 0. Its midpoint is `−0.45`, half-width `0.65`, approximate SE `0.33`, and approximate `|z|=1.36`; this does not reproduce a conventional two-sided P near `.009`.

**Alternative source-grounded interpretations:** The package does not state a special non-common CI/P construction, estimator, degrees-of-freedom rule, or column assignment that reconciles the printed pair.

**Mechanical evidence recheck:** The row, estimate, interval, P value, separately labelled HR, and logical comparison were reproduced. The exact CI/P construction and any special testing convention are missing.

**Quality-control relevance:** The displayed inferential elements require a human check of column assignment and analysis specification.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an absolute difference, interval, and P value as one matched inferential result when the supplied display does not reconcile under the stated diagnostic. This does not establish an effect on the paper’s conclusions.

**Human verification steps:** Confirm the Table 3 columns in the PDF, then obtain the model output or statistical analysis specification that generated the interval and P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Composite adherence has conflicting patient-level and care-opportunity analysis descriptions

**Candidate statement:** The package describes the composite as a patient-level average, a care-opportunity-level binary analysis, and a pooled performed/possible-interventions ratio without reconciling the analysis unit for reported quantities.

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 3](<../jama_wang_2018_oi_180070.pdf#page=3>) Outcomes, [jama_wang_2018_oi_180070.pdf — PDF p. 4](<../jama_wang_2018_oi_180070.pdf#page=4>) analysis unit, and [jama_wang_2018_oi_180070.pdf — PDF p. 7](<../jama_wang_2018_oi_180070.pdf#page=7>) Table 2; DOC-002, [joi180070supp1_prod.pdf — PDF p. 18](<../joi180070supp1_prod.pdf#page=18>) and [joi180070supp1_prod.pdf — PDF p. 19](<../joi180070supp1_prod.pdf#page=19>); DOC-003, [joi180070supp2_prod.pdf — PDF p. 2](<../joi180070supp2_prod.pdf#page=2>).

**Source evidence:** DOC-001 says the composite was calculated for each patient and averaged; DOC-002 says each eligible care opportunity contributed a binary observation; DOC-003 defines a pooled performed/possible-interventions quantity.

**Reported-versus-comparator:** Patient-averaged composite description versus care-opportunity binary analysis and pooled opportunity proportion under the same composite label.

**Reasoning procedure:** Compare analysis weights implied by the stated units rather than assuming that related descriptive and inferential summaries use one estimand.

**Calculation:** A mean of patient percentages gives each patient equal weight; a pooled opportunity proportion weights patients by their number of eligible opportunities. These can produce different percentages, differences, and model interpretations.

**Alternative source-grounded interpretations:** Descriptive and inferential summaries may intentionally use different units, but the supplied package does not reconcile them for the printed `88.2%/84.8%`, adjusted difference, and ORPA.

**Mechanical evidence recheck:** All cited descriptions and Table 2 locations were found. The missing input is a complete estimator-to-output mapping showing which unit generated each printed summary.

**Quality-control relevance:** Analysis-unit language can affect the interpretation of a reported composite percentage and its related estimates.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer or guideline evidence extractor could copy a composite result while assigning it a different analysis unit from the one used to generate it. No change to the observed result is claimed.

**Human verification steps:** Confirm each cited definition, then inspect the statistical analysis specification or code that generated the Table 2 means, difference, and ORPA.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — DVT-prophylaxis window is labeled as both within 48 hours and by end of hospital day 2

**Candidate statement:** The protocol table labels the DVT measure as within 48 hours of admission, whereas detailed specifications and the reported table use by end of hospital day 2.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-002, [joi180070supp1_prod.pdf — PDF p. 13](<../joi180070supp1_prod.pdf#page=13>) protocol Table 2, [joi180070supp1_prod.pdf — PDF p. 14](<../joi180070supp1_prod.pdf#page=14>) Table 3, and [joi180070supp1_prod.pdf — PDF p. 15](<../joi180070supp1_prod.pdf#page=15>) Table 3 continuation; DOC-003, [joi180070supp2_prod.pdf — PDF p. 3](<../joi180070supp2_prod.pdf#page=3>) eTable 1; DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 7](<../jama_wang_2018_oi_180070.pdf#page=7>) Table 2 footnote.

**Source evidence:** DOC-002 p. 13 says `within 48 hours of admission`; DOC-002 pp. 14 and 15, DOC-003 p. 3, and DOC-001 p. 7 say `by end of hospital day 2` for the measure with displayed `178/645` and `66/592` results.

**Reported-versus-comparator:** Elapsed-time `within 48 hours` versus calendar-boundary `by end of hospital day 2`.

**Reasoning procedure:** Compare the ordinary operational boundaries without presuming that the source defines hospital day 2 as 48 elapsed hours.

**Calculation:** The boundaries can include different events for a late-day admission unless an operational convention equates them; the supplied package does not provide that convention.

**Alternative source-grounded interpretations:** Hospital day 2 may have been operationalized as 48 elapsed hours, or the protocol table may use shorthand; neither equivalence is stated.

**Mechanical evidence recheck:** All separately linked pages and wording were found. The missing inputs are the hospital-day convention, timestamp inclusion rule, and executable definition used for the reported denominators.

**Quality-control relevance:** The labels can change the measure definition used to interpret DVT-prophylaxis adherence.

**Potential downstream evidence impact:** If confirmed, an extractor or guideline reviewer could copy a different DVT timing definition for the reported adherence measure. The supplied package does not show that any patient was reclassified or that an effect estimate changes.

**Human verification steps:** Confirm the four source definitions and inspect the protocol case-report-form, time-stamp rule, or data dictionary to identify the implemented timing boundary.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable reporting defects can matter if later systematic reviews, meta-analyses, guidelines, or data-extraction workflows copy a count, denominator, percentage, timing definition, analysis unit, or inferential display. The supplied package does not establish that any candidate propagated, changed a conclusion, or caused harm. The potential impact statements above are conditional on human confirmation.

## Limitations and Missing Definitions

The package provides no raw patient-level or cluster-level data, row-specific missingness/hidden denominators, executable LDL eligibility rule, hospital-day timestamp convention, complete estimator-to-output mapping for the composite, or exact CI/P construction details. These limitations prevent resolution beyond the stated supplied-source comparisons. Fresh native/layout text was usable for all result-relevant pages; direct visual confirmation was available for 13 selected result pages. The direct C004 fraction and percentage are available and reproduce mathematically.

## Human Adjudication Checklist

1. Confirm every cited source location and printed value in the supplied PDF.
2. Obtain the needed underlying table, analysis, protocol, or code definition identified in each card.
3. Decide the intended reported value or definition and record the decision only in the card’s blank human-adjudication fields.
4. Keep the source-grounded observation distinct from any inferred production explanation.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source integrity and execution

Source hashes were recorded before fresh processing and matched the current direct sources during the evidence-quality audit. The current execution manifest records every agent used in the review window:

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh_source_preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_evidence_mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_evidence_mapping | root/support_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_checks | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| cross_source_checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation.md` |

### Reproducibility performance

- **Target basis:** Three supplied PDFs comprise 44 fresh page units (10-page main article plus 25-page and 9-page supplements), with native and layout extraction, visual result-page review, parallel relationship mapping, and two full statistical passes required; preferred Linux PDF tools are absent, adding a bounded local-tool fallback burden.
- **Total source units:** 44
- **Fresh-source units:** 44
- **Target elapsed minutes:** 30-60
- **Started UTC:** 2026-08-24T00:16:27Z
- **Finished UTC:** 2026-08-24T01:15:46Z
- **Observed elapsed minutes:** 59.3
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Total tokens | Known token cost (USD) |
|---|---:|---:|
| gpt-5.6-sol | 0 known; incomplete | 0.000000 |
| gpt-5.6-terra | 0 known; incomplete | 0.000000 |

The runtime exposed no authoritative response-level token counts for the coordinator or any specialist, so each manifested agent has an `UNAVAILABLE` ledger record with exact `__` token fields. The known subtotal is therefore zero while the complete package count and price remain explicitly incomplete. Per-agent detail is in `review_1_5_2/token_usage_summary.md`. Cached input and cache-write are input subsets, and reasoning tokens are output subsets; they are not added again to total tokens. Any amount is a token-only API-equivalent estimate under the 2026-08-18 pricing snapshot, not an invoice; non-token tools, containers, storage, subscriptions, taxes, and other vendor charges are excluded.
