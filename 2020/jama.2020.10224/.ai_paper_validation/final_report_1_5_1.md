# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

All three candidate consistency issues in this report are **Pending Human Adjudication**. They are quality-control observations, not findings of invalidity or conclusions about authors, corrections, or the paper's conclusions.

## 1. Executive Quality-Control Summary

Complete source-first quantitative reporting quality control identified **3** distinct stable candidates: C001, C002, and C003. All 91 direct PDF-page units were mapped; 53 numeric/reporting relationships and 35 inferential-statistical relationships were reviewed. Both independent fresh statistical passes completed all 35 statistical relationships.

The observations are potentially preventable reporting or locator inconsistencies. If confirmed, small defects can matter to downstream evidence extraction; this review does not assert that any defect propagated, changed a conclusion, or caused serious harm.

## 2. Package and Reused-Evidence Provenance

| Source ID | Supplied source | Units | SHA-256 |
|---|---|---:|---|
| DOC-001 | `jama_okereke_2020_oi_200066.pdf` | 10 PDF pages | `5d7ca4528c3c0d6c32e105598d4d862726b54a72ef8b76dfd3200de12b05b50e` |
| DOC-002 | `joi200066supp1_prod.pdf` | 31 PDF pages | `0a3b7b0905eaa8152dbf9b3b675992fc80ec8a35b258ca236a428bce81ffbe07` |
| DOC-003 | `joi200066supp2_prod.pdf` | 48 PDF pages | `efba5b6eeb6411c34ce02f9fb123ab90161c2b63c7e685298690959601a7be81` |
| DOC-004 | `joi200066supp3_prod.pdf` | 2 PDF pages | `4f48f06519cc7ddcfd8d914c9aa52381b1557c3f95efdcf9aa5000757644924e` |

No eligible pre-existing direct-source-backed evidence asset was available. Consequently, 0 direct units were reusable and all 91 were freshly extracted and mapped from supplied PDFs. Fresh native/layout derivatives were used as locators and transcription aids; direct PDF pages were the authority for candidate evidence. The non-source package graphic was not treated as an independent scientific source.

## 3. Scope, Complete Coverage, and Exclusions

| Source ID | Total units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 0 | 10 | 10 | COMPLETE |
| DOC-002 | 31 | 0 | 31 | 31 | COMPLETE |
| DOC-003 | 48 | 0 | 48 | 48 | COMPLETE |
| DOC-004 | 2 | 0 | 2 | 2 | COMPLETE |
| **Total** | **91** | **0** | **91** | **91** | **COMPLETE** |

The review covered numeric, denominator, proportion, total, inferential, cross-document, measure/label/scale, and rate-versus-count relationships. Protocol planning assumptions were not treated as achieved-result comparators. Distinct censoring, adjustment, competing-risk, exposure-scale, outcome, or time-window analyses were not forced to agree. No structured dataset or workbook was supplied.

Excluded as non-candidates were coherent finite-precision displays, including any display-zero P value alone; no display-zero P value occurred in the statistical inventory. There is no review queue, top-N subset, deferred-by-cap section, or candidate cap.

## 4. Quantitative and Statistical Relationship Coverage

- Numeric/reporting relationships: 53 of 53 (N001-N010, N100-N121, N300-N308, and N500-N511).
- Inferential-statistical relationships: 35 of 35 (S001-S004, S100-S113, S300-S307, and S500-S508).
- Cross-location matched families: 15.
- Statistical pass 1: 35 of 35 relationships, `PASS_1_COMPLETE`.
- Statistical pass 2: 35 of 35 relationships, `PASS_2_COMPLETE`.

Both statistical passes were separate fresh `gpt-5.6-terra` high-reasoning executions. They applied interval containment/order, null/sign/direction, labels/scales, population/contrast/model identity, linked arithmetic, duplication, and cross-source checks where source definitions supported them. Exact reconstruction of many inferential results was not attempted where unrounded coefficients, standard errors, covariance, test statistics, sidedness, variance estimators, or person-time were absent.

## 5. Candidate Index

| Stable ID | Candidate | Category | Status |
|---|---|---|---|
| [C001](#c001--vitamin-d-concentration-unit-differs-at-the-20-unit-baseline-threshold) | Vitamin-D concentration unit differs at the 20-unit baseline threshold | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C002](#c002--protocol-icd-9-code-prose-cites-table-3-while-the-code-list-is-table-1) | Protocol ICD-9-code prose cites Table 3 while the code list is Table 1 | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C003](#c003--supplementary-depression-risk-subgroup-narrative-refers-to-main-figure-3-but-its-printed-values-match-main-figure-4) | Supplementary depression-risk subgroup narrative refers to main Figure 3, but its printed values match main Figure 4 | Cross-document numeric inconsistency | Pending Human Adjudication |

## 6. Candidate Evidence Cards

## C001 — Vitamin-D concentration unit differs at the 20-unit baseline threshold

**Status:** Pending Human Adjudication.

**Candidate statement:** The main-results baseline narrative prints a 20-unit 25-hydroxyvitamin-D threshold as `mg/mL`, while matched descriptions print the threshold as `ng/mL`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 main article — PDF p. 6](<../jama_okereke_2020_oi_200066.pdf#page=6>), Results, “Baseline Characteristics”; [DOC-001 main article — PDF p. 4](<../jama_okereke_2020_oi_200066.pdf#page=4>), Table 1; [DOC-001 main article — PDF p. 8](<../jama_okereke_2020_oi_200066.pdf#page=8>), Figure 4; [DOC-003 Supplement 2 — PDF p. 38](<../joi200066supp2_prod.pdf#page=38>), eTable 14a; [DOC-003 Supplement 2 — PDF p. 39](<../joi200066supp2_prod.pdf#page=39>), eTable 14c footnote; and [DOC-003 Supplement 2 — PDF p. 40](<../joi200066supp2_prod.pdf#page=40>), eTable 14 narrative.

**Source evidence:** DOC-001 p. 6 prints: “The mean 25-hydroxyvitamin D level was 31.1 ng/mL and 11.6% of participants had levels lower than 20 mg/mL.”

**Reported-versus-comparator:** The reported threshold is `20 mg/mL`. Table 1 and Figure 4 label the matched analyte/categories `<20` and `≥20 ng/mL`; Supplement 2 defines low vitamin D as `<20 ng/ml`.

**Reasoning procedure:** Match the analyte, baseline cohort, threshold, and linked percentage; then compare the unit attached to the repeated threshold. A repeated concentration threshold requires a consistent unit unless an alternative conversion or definition is supplied.

**Calculation:** Table 1 gives `630 + 698 = 1,328` and `5,739 + 5,678 = 11,417`; `1,328 / 11,417 × 100 = 11.63%`, which rounds to 11.6% and connects the narrative percentage to the `<20 ng/mL` category. As a dimensional diagnostic, `20 mg/mL × 1,000,000 ng/mg = 20,000,000 ng/mL`, not `20 ng/mL`; this is not a proposed corrected value.

**Alternative source-grounded interpretations:** The narrative could refer to a different unstated analytic unit, but the same sentence reports a `31.1 ng/mL` mean and no alternative conversion or threshold is supplied. A transcription or production mechanism is possible but is not established by the supplied files.

**Mechanical evidence recheck:** Every cited page was visually found. The printed `mg/mL` and all listed `ng/mL`/`ng/ml` comparators were confirmed; the arithmetic above was reproduced. The package lacks an authoritative intended-unit statement, production history, author query, or alternative laboratory-unit definition.

**Quality-control relevance:** The printed values do not reconcile under the stated unit rule. A unit-label inconsistency can make a biomarker threshold ambiguous during routine evidence extraction.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy an incompatible vitamin-D threshold unit. This report does not assert that this occurred or that it changed any conclusion.

**Human verification steps:** Reopen the cited pages; verify the p. 6 unit letters and Table 1/Figure 4/eTable 14 threshold labels; then inspect authoritative production or author-query material, if available, to establish the intended unit.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Protocol ICD-9-code prose cites Table 3 while the code list is Table 1

**Status:** Pending Human Adjudication.

**Candidate statement:** The protocol prose locates depression-identifying ICD-9 codes in Table 3, while the adjacent code list is Table 1 and the supplied Table 3 is a recurrent-depression power table.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 protocol — PDF p. 18](<../joi200066supp1_prod.pdf#page=18>), ICD-9-code paragraph and immediately following table; [DOC-002 protocol — PDF p. 23](<../joi200066supp1_prod.pdf#page=23>), Table 3.

**Source evidence:** DOC-002 p. 18 states: “ICD-9 codes will be used to identify depression (Table 3).” The table directly below is captioned “Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders.”

**Reported-versus-comparator:** The reported locator is `Table 3`; the adjacent code-list caption is `Table 1`. DOC-002 p. 23 Table 3 contains power percentages by assumed risk ratio, rather than an ICD-9 code list.

**Reasoning procedure:** Compare the numeric table locator and its displayed contents with the explicitly referenced ICD-9-code list. A locator for the code list should identify the displayed table that contains that list.

**Calculation:** `Table 3 ≠ Table 1`. The p. 23 Table 3 contains recurrent-depression power scenarios, so it cannot be the code-list table named by the p. 18 sentence; no rounding rule applies.

**Alternative source-grounded interpretations:** The parenthetical may be retained from an earlier numbering scheme, or the adjacent caption may have been renumbered. Appendix C may contain a longer code list, but the supplied text does not identify it as Table 3.

**Mechanical evidence recheck:** The referring sentence, adjacent Table 1 caption/content, and p. 23 Table 3 were visually confirmed. The package lacks version history, cross-reference fields, table-renumbering records, an author query, or another authoritative protocol version that resolves intended numbering.

**Quality-control relevance:** The printed table reference does not identify the matching displayed code list, which may impair reliable identification of the stated depression-ascertainment definition.

**Potential downstream evidence impact:** If confirmed, a protocol reader or data extractor could follow the wrong table locator when documenting outcome ascertainment. This report does not assert that this happened or that it changed a trial estimate or conclusion.

**Human verification steps:** Inspect pp. 18 and 23; determine whether an authoritative version contains a code-list Table 3; compare version-control or typesetting records, if available, before selecting any correction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Supplementary depression-risk subgroup narrative refers to main Figure 3, but its printed values match main Figure 4

**Status:** Pending Human Adjudication.

**Candidate statement:** The Supplement 2 subgroup narrative names main Figure 3, although its displayed subgroup interaction P values and hazard ratios match main Figure 4 and do not occur in Figure 3.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-003 Supplement 2 — PDF p. 13](<../joi200066supp2_prod.pdf#page=13>), subgroup heading and narrative; [DOC-001 main article — PDF p. 8](<../jama_okereke_2020_oi_200066.pdf#page=8>), Figure 4; [DOC-001 main article — PDF p. 7](<../jama_okereke_2020_oi_200066.pdf#page=7>), Figure 3.

**Source evidence:** DOC-003 p. 13 names “Figure 3” and “main Figure 3,” then reports women `p-interaction=0.10`, BMI `p-interaction=0.06`, baseline vitamin-D-use `HR=0.87 (95% CI: 0.73-1.04)`, and baseline 25(OH)D `≥20 ng/ml HR=0.89 (95% CI: 0.77-1.04)`.

**Reported-versus-comparator:** DOC-001 Figure 4 prints `.10`, `.06`, `0.87 (0.73-1.04)`, and `0.89 (0.77-1.04)` for the matching depression-risk subgroups. DOC-001 Figure 3 is a crude PHQ-8 score-distribution figure and does not print those values.

**Reasoning procedure:** Match population, outcome, treatment contrast, subgroup, effect measure, and displayed precision before testing the figure locator. A depression-related subject alone is not sufficient for a figure match.

**Calculation:** The four exact displayed comparisons are `0.10 = .10`, `0.06 = .06`, `0.87 (0.73-1.04) = 0.87 (0.73-1.04)`, and `0.89 (0.77-1.04) = 0.89 (0.77-1.04)`. All occur in Figure 4; none occurs in Figure 3.

**Alternative source-grounded interpretations:** A prior main-article layout might have numbered the depression-risk figure as Figure 3. No accepted-manuscript layout, production cross-reference field, or alternative supplied main-article version establishes that possibility.

**Mechanical evidence recheck:** The supplementary heading, narrative, and all four values were visually confirmed. The same values were found in main Figure 4 and were absent from Figure 3. The intended figure number and production history remain unavailable.

**Quality-control relevance:** The numerical narrative and its main-figure locator identify different figures in the supplied package, requiring human confirmation of the intended reference.

**Potential downstream evidence impact:** If confirmed, an extractor, systematic review, meta-analysis, or guideline evidence table could attribute the subgroup hazard ratios and interaction P values to the wrong main figure. This report does not assert that the estimates differ, that propagation occurred, or that any conclusion changed.

**Human verification steps:** Reopen DOC-003 p. 13 and DOC-001 pp. 7-8; verify the values and captions; inspect accepted-manuscript or production cross-reference records, if available, to determine whether the heading, parenthetical, or figure numbering was intended to differ.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## 7. Downstream Evidence-Chain Considerations

These quality-control observations concern a concentration-unit label and two internal/cross-document locators. If a candidate is confirmed, it could affect what a later evidence extractor records about a threshold, outcome-definition table, or figure provenance. The review does not claim that downstream reuse, propagation, conclusion change, or serious harm occurred.

## 8. Limitations and Missing Definitions

The supplied package lacks raw data, person-time denominators, full unrounded model outputs, standard errors, covariance matrices, many test statistics, variance estimators, sidedness details, amendment history, production sources, figure/table renumbering history, and author-query records. These omissions limit exact reconstruction and resolution of intended units/locators, but did not prevent direct confirmation of the printed comparisons. Protocol planning quantities were treated as planning quantities, not assumed mismatches with achieved results. See [limitations.md](<review_1_5_1/limitations.md>) for the complete limitations record.

## 9. Human Adjudication Checklist

1. Confirm each cited page against the supplied PDF.
2. Confirm that the stated comparator is the same population, outcome, time, contrast, model, and scale where applicable.
3. Review the calculation or logical comparison and its stated limits.
4. Obtain authoritative production, version-control, author-query, or source-data documentation if a decision requires intended wording or numbering.
5. Complete the five `__` adjudication fields in each card; retain the stable ID and evidence trail.

## 10. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Source hashes were recorded before review in [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>). The pre-existing featured PNG is recorded in [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>) as a partial provenance-only graphic; it contributes zero reusable direct-source units. Direct-PDF evidence, complete source coverage, relationship inventories, both statistical passes, the candidate ledger, and mechanical rechecks are retained below `review_1_5_1/`.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| reuse_asset_curation | root/reuse_asset_curation | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_evidence_mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_mapping_doc002 | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_mapping_doc003a | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_mapping_doc003b_doc004 | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_checks | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_quality | root/evidence_quality_audit | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN |

### Reproducibility performance

- **Target basis:** Initial package inventory identified four direct PDF sources totaling 91 pages and one supplied derivative featured graphic outside the formal direct-source unit count, with no pre-existing `.ai_paper_validation` evidence assets. The package therefore requires fresh mapping of all 91 direct-source units, including a 48-page rotated supplement, plus comparison of the graphic against its source figure, followed by the full multi-lane and two-pass statistical workflow. The bounded target is calibrated to, but not inferred solely from, the 102-unit/81-fresh-unit reference run.
- **Total source units:** 91
- **Fresh-source units:** 91
- **Target elapsed minutes:** 40-60
- **Started UTC:** 2026-08-18T23:22:08Z
- **Finished UTC:** 2026-08-19T00:00:02Z
- **Observed elapsed minutes:** 37.9
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Known total tokens | Total-count status | Known token cost (USD) | Estimated complete token cost (USD) |
|---|---:|---:|---|---:|---:|
| gpt-5.6-sol | 3 | 0 | INCOMPLETE | 0.000000 | __ |
| gpt-5.6-terra | 10 | 0 | INCOMPLETE | 0.000000 | __ |

Authoritative response-level runtime usage was unavailable for all 13 manifested agents. The ledger therefore uses `UNAVAILABLE` records with exact `__` token fields and does not estimate usage from review text. The displayed zero is the sum of known token records, not a claim of zero actual usage; the complete package count and price remain unavailable. See `review_1_5_1/token_usage_summary.md` for per-agent detail. Token costs are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not an invoice; non-token tools, containers, storage, subscriptions, taxes, and other charges are excluded. Cached input and cache-write counts are input subsets, and reasoning tokens are an output subset; they are not added again to total tokens.
