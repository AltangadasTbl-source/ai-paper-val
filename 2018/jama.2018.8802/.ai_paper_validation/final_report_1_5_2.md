# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

All eight observations in this report are **Pending Human Adjudication**. They are reproducible quality-control candidates, not findings of validity, severity, correction, acceptance, rejection, or paper-level conclusion change.

## Executive Quality-Control Summary

Fresh source-first review of the supplied paper package registered **8** distinct quantitative reporting-consistency candidates (C001-C008). The review covered all 44 direct PDF-page units, 72 numeric/reporting relationships, 61 statistical relationships, and 27 cross-source match keys. Small preventable reporting defects can matter when a data extractor, systematic review, meta-analysis, guideline, or later evidence product copies a printed value or definition; this report does not assert that such copying, propagation, or conclusion change occurred.

## Package and Fresh-Processing Provenance

The direct evidence set comprised three supplied PDFs: the main article ([jama_wang_2018_oi_180070.pdf — PDF p. 1](<../jama_wang_2018_oi_180070.pdf#page=1>), 10 pages), protocol/statistical-analysis-plan support ([joi180070supp1_prod.pdf — PDF p. 1](<../joi180070supp1_prod.pdf#page=1>), 25 pages), and supplementary results ([joi180070supp2_prod.pdf — PDF p. 1](<../joi180070supp2_prod.pdf#page=1>), 9 pages). Fresh SHA-256 records are in `review_1_5_2/source_hashes_before.sha256`.

All 44 pages received fresh native and layout text extraction. Thirty-nine result-relevant pages were freshly rendered for visual confirmation; zero pages required OCR. No Office, workbook, CSV, web, external literature, raw data, or previous audit derivative was used as evidence.

## Scope, Complete Coverage, and Exclusions

`source_coverage.md` records 10/10 mapped DOC-001 pages, 25/25 DOC-002 pages, and 9/9 DOC-003 pages. The pre-extraction coverage manifest contains 17 complete stage rows. The review prioritized reported numeric values, denominators/proportions/totals, inferential displays, matched cross-document values, and measure labels/scales.

Excluded from candidate registration were general methodology or design critique without a concrete reported-value inconsistency, unreported model detail without a direct mismatch, and display-zero reasoning. No assigned relationship printed `P = 0`, `p = 0.000`, or equivalent; threshold displays such as `P < .001` were not candidates solely on that basis.

## Quantitative and Statistical Relationship Coverage

- Numeric/reporting review: N001-N072, complete. Six provisional arithmetic/label proposals and the factual representation of C007 were resolved into the stable ledger.
- Cross-source review: 27 complete identity-matched keys, including one C007 proposal.
- Statistical pass 1: clean independent fresh Terra/high pass over S001-S061; two proposals were registered as C002 and C008.
- Statistical pass 2: different fresh Terra/high agent reviewed S001-S061, the entire C001-C008 ledger, and all mechanical recheck facts; no new candidate was identified.

The qualifying statistical executions were `root/statistics_pass_1_clean` and `root/statistics_pass_2`, both `gpt-5.6-terra` at `high` reasoning effort. An earlier pass-1 response was quarantined for possible legacy-label contamination and excluded from the scientific evidence chain; its manifested execution remains recorded for reproducibility and token accounting.

## Candidate Index

| ID | Candidate | Category | Primary source location |
|---|---|---|---|
| C001 | Table 1 CAD/previous-myocardial-infarction percentage does not reproduce | Numeric or arithmetic inconsistency | DOC-001 PDF p. 6 |
| C002 | LDL eligibility boundary differs between result labels and supplied measure definition | Measure, label, or scale inconsistency | DOC-001 p. 7; DOC-002 p. 15; DOC-003 pp. 3, 8 |
| C003 | eTable 4 discharge-antithrombotics control percentage does not reproduce | Denominator, proportion, or total inconsistency | DOC-003 PDF p. 8 |
| C004 | eTable 4 AF-anticoagulation control percentage does not reproduce | Denominator, proportion, or total inconsistency | DOC-003 PDF p. 8 |
| C005 | eTable 4 lipid-lowering control percentage does not reproduce | Denominator, proportion, or total inconsistency | DOC-003 PDF p. 8 |
| C006 | eTable 4 antidiabetic-medication control percentage does not reproduce | Denominator, proportion, or total inconsistency | DOC-003 PDF p. 8 |
| C007 | Baseline-survey patient total does not reconcile with stated per-cluster inclusion | Cross-document numeric inconsistency | DOC-001 p. 6; DOC-003 p. 2 |
| C008 | In-hospital death absolute-difference CI and P value do not reconcile | Statistical reporting inconsistency | DOC-001 pp. 4, 8 |

## Candidate Evidence Cards

## C001 — Table 1 CAD/previous-myocardial-infarction percentage does not reproduce

**Candidate statement:** The intervention cell prints `311 (13.05)` under a 2,400-patient column, but the displayed fraction does not yield 13.05%.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [jama_wang_2018_oi_180070.pdf — PDF p. 6](<../jama_wang_2018_oi_180070.pdf#page=6>), Table 1, `CAD/previous myocardial infarction`, intervention column and `Patients, No.` header.

**Source evidence:** The direct PDF prints intervention `Patients, No.` = 2400 and the row cell `311 (13.05)`.

**Reported-versus-comparator:** Reported 13.05% versus 311/2400.

**Reasoning procedure:** Apply ordinary percentage calculation to the printed count and whole-column patient total; no row-specific alternative denominator is printed.

**Calculation:** `311 / 2400 × 100 = 12.9583%`, which rounds to 13.0% at one decimal or 12.96% at two decimals, not 13.05%.

**Alternative source-grounded interpretations:** A row-specific denominator or nonstandard calculation may have been used, but neither is supplied.

**Mechanical evidence recheck:** The direct PDF location, `311 (13.05)`, and the `2400` header were found and the calculation was reproduced.

**Quality-control relevance:** A printed baseline percentage cannot be reproduced from its displayed count and column total under the stated table convention.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the printed percentage or count/denominator pair into a baseline-characteristic record.

**Human verification steps:** Check the Table 1 analysis dataset, intended row denominator, calculation rule, and production source for this cell.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — LDL eligibility boundary differs between result labels and supplied measure definition

**Candidate statement:** The main and sensitivity result rows use `LDL >100 mg/dL`, while supplied formal measure definitions use `LDL ≥100 mg/dL`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_wang_2018_oi_180070.pdf — PDF p. 7](<../jama_wang_2018_oi_180070.pdf#page=7>), Table 2 lipid-lowering row; [joi180070supp1_prod.pdf — PDF p. 15](<../joi180070supp1_prod.pdf#page=15>), definition; [joi180070supp2_prod.pdf — PDF p. 3](<../joi180070supp2_prod.pdf#page=3>), eTable 1 definition; and [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4 label.

**Source evidence:** The result labels print `>100 mg/dL`; both supplied definitions print `≥100 mg/dL` with additional eligibility conditions.

**Reported-versus-comparator:** A strict threshold excludes LDL exactly 100 mg/dL; an inclusive threshold includes it.

**Reasoning procedure:** Compare the printed inequality symbols in matched measure labels and definitions.

**Calculation:** `>100 ≠ ≥100`; no rounding tolerance applies.

**Alternative source-grounded interpretations:** The result-row wording may be abbreviated while the formal inclusive definition governed eligibility; the supplied package does not state this.

**Mechanical evidence recheck:** All four symbol locations were directly rechecked; patient-level LDL-at-100 counts and operational code were unavailable.

**Quality-control relevance:** The printed label and supplied definition identify nonidentical eligibility boundaries.

**Potential downstream evidence impact:** If confirmed, an extractor could code a different eligibility boundary when reusing the adherence result or denominator definition.

**Human verification steps:** Review the operational eligibility code and Table 2/eTable 4 analysis populations, including treatment of LDL exactly 100 mg/dL.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 4 discharge-antithrombotics control percentage does not reproduce

**Candidate statement:** The control cell prints `2141/2400 (89.3)`, but the fraction rounds to 89.2% at one decimal.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, `Antithrombotics`, control cell.

**Source evidence:** The cell under `No. / Total (%)` prints `2141/2400 (89.3)`.

**Reported-versus-comparator:** Reported 89.3% versus fraction-derived 89.2083%.

**Reasoning procedure:** Calculate the percentage from the explicit numerator and denominator and round to the table's one-decimal precision.

**Calculation:** `2141 / 2400 × 100 = 89.2083%`, which rounds to 89.2%; the nearest-tenth interval for 89.3% begins at 89.25%.

**Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied; the header defines the displayed fraction.

**Mechanical evidence recheck:** The direct PDF cell, header, numerator, denominator, percentage, and arithmetic were reproduced.

**Quality-control relevance:** The printed fraction and percentage do not reproduce under ordinary one-decimal rounding.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an inconsistent control numerator, denominator, or percentage from the sensitivity table.

**Human verification steps:** Check the sensitivity-analysis output and table-production calculations for the intended cell value and rounding rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTable 4 AF-anticoagulation control percentage does not reproduce

**Candidate statement:** The control cell prints `39/174 (22.5)`, but the fraction rounds to 22.4% at one decimal.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, `Anticoagulation for Atrial Fibrillation`, control cell.

**Source evidence:** The direct PDF prints `39/174 (22.5)` beneath `No. / Total (%)`.

**Reported-versus-comparator:** Reported 22.5% versus fraction-derived 22.4138%.

**Reasoning procedure:** Reproduce the table percentage from its explicit fraction at one decimal.

**Calculation:** `39 / 174 × 100 = 22.4138%`, which rounds to 22.4%, below the 22.45% lower boundary for 22.5%.

**Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied.

**Mechanical evidence recheck:** The exact cell and all printed components were found; the arithmetic was reproduced.

**Quality-control relevance:** The control-cell percentage does not reproduce from its stated fraction.

**Potential downstream evidence impact:** If confirmed, a downstream evidence table could carry an inconsistent AF-specific control proportion.

**Human verification steps:** Check the AF-specific sensitivity dataset, output, and rounding method.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 4 lipid-lowering control percentage does not reproduce

**Candidate statement:** The control cell prints `1439/1586 (90.8)`, but the fraction rounds to 90.7% at one decimal.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, `Lipid-lowering for LDL >100 mg/dL`, control cell.

**Source evidence:** The direct PDF prints `1439/1586 (90.8)` beneath `No. / Total (%)`.

**Reported-versus-comparator:** Reported 90.8% versus fraction-derived 90.7314%.

**Reasoning procedure:** Reproduce the displayed percentage from the explicit fraction at one decimal, separately from the threshold-label question in C002.

**Calculation:** `1439 / 1586 × 100 = 90.7314%`, which rounds to 90.7%, below the 90.75% lower boundary for 90.8%.

**Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied; C002 is a separate label/definition comparator.

**Mechanical evidence recheck:** The cell and its printed numerator, denominator, percentage, and table definition were directly rechecked.

**Quality-control relevance:** The sensitivity-table percentage does not reproduce from the printed fraction.

**Potential downstream evidence impact:** If confirmed, evidence extraction could copy an inconsistent lipid-lowering control percentage or fraction.

**Human verification steps:** Check the applicable sensitivity-analysis output, eligibility population, and rounding calculation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 4 antidiabetic-medication control percentage does not reproduce

**Candidate statement:** The control cell prints `557/688 (81.1)`, but the fraction rounds to 81.0% at one decimal.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi180070supp2_prod.pdf — PDF p. 8](<../joi180070supp2_prod.pdf#page=8>), eTable 4, `Antidiabetic Medication`, control cell.

**Source evidence:** The direct PDF prints `557/688 (81.1)` beneath `No. / Total (%)`.

**Reported-versus-comparator:** Reported 81.1% versus fraction-derived 80.9593%.

**Reasoning procedure:** Reproduce the table percentage from its explicit fraction using ordinary one-decimal rounding.

**Calculation:** `557 / 688 × 100 = 80.9593%`, which rounds to 81.0%, below the 81.05% lower boundary for 81.1%.

**Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied.

**Mechanical evidence recheck:** The direct cell, table header, printed values, and arithmetic were reproduced.

**Quality-control relevance:** The printed control proportion does not reproduce from the displayed numerator and denominator.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy an inconsistent antidiabetic-medication control proportion.

**Human verification steps:** Check the sensitivity-analysis output and table-production calculation for this control cell.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — baseline-survey patient total does not reconcile with stated per-cluster inclusion

**Candidate statement:** Table 1 reports 801 baseline-survey patients and 40 survey hospitals, while the supplement states that 20 patients per cluster were prospectively included, implying 800 under an exact fixed-count reading.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_wang_2018_oi_180070.pdf — PDF p. 6](<../jama_wang_2018_oi_180070.pdf#page=6>), Table 1 baseline-survey `Hospitals, No.` = 40 and `Patients, No.` = 801; [joi180070supp2_prod.pdf — PDF p. 2](<../joi180070supp2_prod.pdf#page=2>), eAppendix baseline-survey statement; [jama_wang_2018_oi_180070.pdf — PDF p. 5](<../jama_wang_2018_oi_180070.pdf#page=5>), Figure 1; [joi180070supp1_prod.pdf — PDF p. 4](<../joi180070supp1_prod.pdf#page=4>) and [PDF p. 7](<../joi180070supp1_prod.pdf#page=7>), 40-cluster statements.

**Source evidence:** Table 1 prints 40 hospitals and 801 patients in the baseline-survey column; the eAppendix prints `20 patients per cluster were prospectively included`.

**Reported-versus-comparator:** Reported total 801 versus `20 × 40 = 800` under the stated same-survey, exact-count interpretation.

**Reasoning procedure:** Match the baseline-survey population and cluster count across the direct sources, then multiply the stated per-cluster inclusion count.

**Calculation:** `20 × 40 = 800`; the difference from the Table 1 total is one patient.

**Alternative source-grounded interpretations:** Twenty may be an operational target rather than exact realized count, or one cluster may have contributed 21 patients; neither qualification is supplied.

**Mechanical evidence recheck:** The source-confirmed Table 1 locator is the `Baseline Survey, No. (%)` column, `Patients, No.` row = 801; the shorthand `Survey (n=801)` was not treated as verbatim source text.

**Quality-control relevance:** The printed cluster-level inclusion statement and matched survey total do not reconcile under an exact fixed-count reading.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a baseline-survey sample total or sampling description that cannot be reconciled without clarification.

**Human verification steps:** Check cluster-level baseline enrollment records, confirm contributing clusters and realized counts, and clarify whether 20 was a target or fixed count.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — in-hospital death absolute-difference CI and P value do not reconcile

**Candidate statement:** The in-hospital-death adjusted absolute-difference 95% CI contains zero, while the adjacent absolute-difference P-value cell is `.009` under the article's two-sided testing statement.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_wang_2018_oi_180070.pdf — PDF p. 8](<../jama_wang_2018_oi_180070.pdf#page=8>), Table 3 `Death` / `In hospital` row, absolute-difference and adjacent P-value columns; [jama_wang_2018_oi_180070.pdf — PDF p. 4](<../jama_wang_2018_oi_180070.pdf#page=4>), data-analysis statements.

**Source evidence:** Table 3 prints adjusted absolute difference `−0.7%` with 95% CI `−1.1% to 0.2%` and adjacent `.009`; page 4 describes adjusted absolute differences, 95% CIs, and two-sided tests.

**Reported-versus-comparator:** The CI includes zero, while `.009 < .05` for the corresponding adjacent absolute-difference pairing.

**Reasoning procedure:** Apply CI/test duality only conditionally to the displayed two-sided 95% CI and adjacent absolute-difference P-value column; do not use the separate HR column.

**Calculation:** `−1.1 < 0 < 0.2`, so zero is inside the printed CI; `.009 < .05`.

**Alternative source-grounded interpretations:** The P value may use a different estimand, model, or inferential construction, but the table places it adjacent to the absolute-difference column and supplies no distinction.

**Mechanical evidence recheck:** The point estimate, CI, P value, table-column pairing, confidence level, adjustment statement, and two-sided statement were directly reproduced. Exact test and CI construction were not supplied.

**Quality-control relevance:** The printed inferential pair warrants clarification of whether the P value and CI represent the same adjusted absolute-difference analysis.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a CI and P value as a matched inferential pair when their relationship needs clarification.

**Human verification steps:** Review the Table 3 analysis output, exact CI method, test statistic, and column-production mapping; confirm whether `.009` tests this absolute-difference estimand.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If human adjudication confirms a candidate, the relevant printed fraction, percentage, eligibility label, survey total, CI, or P value could be copied into a systematic review, meta-analysis, guideline evidence table, or other data-extraction product. The supplied sources do not establish that this occurred, that any conclusion changed, or that harm resulted.

## Limitations and Missing Definitions

The supplied package has no raw data, analysis code, workbook/CSV, cluster-level baseline-enrollment records, or operational LDL eligibility code. Native/layout text was usable on all pages, but PDF reading order can be difficult in tables; fresh renderings were used as visual aids. C001 lacks a row-specific denominator or percentage rule; C002 lacks implemented eligibility code and exact-100 counts; C003-C006 lack calculation output or a stated rounding rule; C007 lacks realized per-cluster counts; and C008 lacks the exact test statistic, CI construction, variance estimator, and explicit same-estimand confirmation. Several eTable 2 P values lacked named test/variance constructions and were recorded as missing-definition coverage outcomes rather than reconstructed. The clean pass-1 replacement was required because an earlier response was quarantined for possible legacy-label contamination.

## Human Adjudication Checklist

For each C ID, independently inspect the cited PDF page, confirm the transcription, consult the relevant analysis output or source dataset where available, decide whether an alternative supplied explanation applies, and record the decision only in the five human-adjudication fields on the card. No AI severity or disposition is supplied.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Profile:** 1.5.2
- **Run mode:** FULL_SOURCE_FIRST_RESTART
- **Direct sources:** 3 PDFs; 44 PDF-page units
- **Source units mapped:** 44/44
- **Fresh extraction:** 44 native/layout units; 39 result-relevant renders; 0 OCR units
- **Source hashes:** pre-run and post-run SHA-256 artifacts are retained under `review_1_5_2/`.
- **Contaminated-call quarantine:** the first pass-1 artifact was quarantined after an old label appeared; the clean replacement is the scientific pass-1 evidence artifact.

### Performance

- **Target basis:** Three direct PDF sources (one 10-page main article and two support PDFs totaling 34 pages), 44 unique PDF-page units, zero reusable units, all-native-first extraction, multiple dense result tables/figures, two complete statistical passes, and no Office/workbook conversion burden; bounded against but materially smaller than the 102-unit workflow 1.4.1 calibration package.
- **Total source units:** 44
- **Fresh-source units:** 44
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-24T01:49:45Z
- **Finished UTC:** 2026-08-24T02:37:50Z
- **Observed elapsed minutes:** 48.1
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** A potentially legacy-contaminated statistical pass 1 was quarantined and replaced with a new clean Terra/high pass; the final quality audit required appending and checking omitted support relationship UN031/N072 and repairing linked scopes/locators.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh_source_preprocessor | root/fresh_preprocessor | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency | root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| statistics_pass_1_discarded_contamination | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/discarded_statistical_pass_1_contaminated.md |
| statistics_pass_1 | root/statistics_pass_1_clean | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency | root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Token totals |
|---|---|
| gpt-5.6-sol | 3 agents; 0 known tokens; 3 unavailable records; known cost USD 0.000000; complete estimate __ |
| gpt-5.6-terra | 9 agents; 0 known tokens; 9 unavailable records; known cost USD 0.000000; complete estimate __ |

Per-agent detail is retained in `review_1_5_2/token_usage_ledger.csv` and the versioned token summary artifact. Amounts are token-only API-equivalent estimates under the dated price snapshot, not an invoice. Cached input/cache-write values are input subsets and reasoning values are output subsets; they are not added again to total tokens.
