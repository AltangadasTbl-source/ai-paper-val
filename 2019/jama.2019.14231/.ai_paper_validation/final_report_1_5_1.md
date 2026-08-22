# 1. Quantitative Quality-Control Consistency Review

## 2. Pending Human Adjudication Notice

**All 11 candidate consistency issues in this report are Pending Human Adjudication.** This is a quantitative reporting quality-control review, not a validity determination, correction, or severity ranking. Small preventable defects can matter for downstream evidence extraction; this review does not assert propagation, conclusion change, or serious harm.

## 3. Executive Quality-Control Summary

Complete review coverage identified **11** stable, source-grounded candidate consistency issues (C001-C011). They concern one cross-document matching-direction statement, five displayed absolute-risk-difference reconciliations, one denominator difference, two label/cross-reference issues, one count-percentage reconciliation, and one signed-versus-absolute-value definition. All remain pending human adjudication.

## 4. Package and Reused-Evidence Provenance

The package contains three direct PDF sources: [main article](<../jama_aminian_2019_oi_190103.pdf#page=1>) (12 pages; SHA-256 `fcf715eadcef54b5c78a557ae684311a96c22c502f4297293156d6cf7f94e4b9`), [Supplement 1](<../joi190103supp1_prod.pdf#page=1>) (20 pages; SHA-256 `ec4e0375222279bcc2137db1be3649d22fd86997f308c1c8f0cba85cfba4c322`), and [protocol/Supplement 2](<../joi190103supp2_prod.pdf#page=1>) (7 pages; SHA-256 `254d15bd2cc32b6c0c21d399caa17ac84fd6b1136e320cd046e0cfefc3ed713f`).

Fifty-nine actively reused, source-linked artifacts were used as locators or transcription aids: 27 native-text pages, 21 rendered pages, OCR text/metadata for main-article page 3, and source/document maps. Direct PDFs remained the evidence authority. Twenty-seven normalized-text files were classified as duplicate optional locators and were not counted as additional coverage. The versioned [source inventory](<review_1_5_1/source_inventory.md>), [reused-evidence inventory](<review_1_5_1/evidence_asset_inventory.md>), and before-hash manifests document this provenance.

## 5. Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| `jama_aminian_2019_oi_190103.pdf` | 12 | 12 | 0 | 12 | COMPLETE |
| `joi190103supp1_prod.pdf` | 20 | 15 | 5 | 20 | COMPLETE |
| `joi190103supp2_prod.pdf` | 7 | 0 | 7 | 7 | COMPLETE |
| **Total** | **39** | **27** | **12** | **39** | **COMPLETE** |

The 12 uncovered units were freshly mapped: Supplement 1 PDF pp. 1-5 and protocol PDF pp. 1-7. The review covered numeric, denominator, statistical, cross-document, measure/label/scale, and rate-versus-count relationships. It did not conduct a broad clinical, methodological, novelty, misconduct, or raw-data audit. No card was created for a display-zero P value: the package uses threshold displays such as `P<.001`, not `P = 0` or equivalent.

## 6. Quantitative and Statistical Relationship Coverage

The current-run inventories contain **38 numeric relationships** (N001-N038) and **25 statistical relationships** (S001-S025). Numeric checks and matched cross-source checks covered the complete inventories. Statistical pass 1 and the independent statistical pass 2 each recorded `PASS_1_COMPLETE` and `PASS_2_COMPLETE`, respectively, for all 25 S IDs. Both passes used fresh, distinct high-effort Terra reviewers. Pass 2 revisited the cross-lane ledger and recheck facts, produced no new qualifying proposal, and did not alter the stable ID set.

The canonical inventories and pass records are available in [numeric relationships](<review_1_5_1/relationships/numeric_relationship_inventory.md>), [statistical relationships](<review_1_5_1/statistics/relationship_inventory.md>), [statistical pass 1](<review_1_5_1/checkers/statistical_pass_1.md>), and [statistical pass 2](<review_1_5_1/checkers/statistical_pass_2.md>).

## 7. Candidate Index

| ID | Candidate statement | Category |
|---|---|---|
| C001 | Protocol matching direction conflicts with the final matched cohort | Cross-document numeric inconsistency |
| C002 | Heart-failure ARD does not reconcile with displayed 8-year incidences | Numeric or arithmetic inconsistency |
| C003 | Coronary-disease ARD does not reconcile with displayed 8-year incidences | Numeric or arithmetic inconsistency |
| C004 | Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences | Numeric or arithmetic inconsistency |
| C005 | Nephropathy ARD does not reconcile with displayed 8-year incidences | Numeric or arithmetic inconsistency |
| C006 | Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences | Numeric or arithmetic inconsistency |
| C007 | Supplement tables use different nonsurgical medication denominators at baseline | Denominator, proportion, or total inconsistency |
| C008 | Medication comparison is labeled as two different named tests | Measure, label, or scale inconsistency |
| C009 | Time-varying-HR narrative cites eTable 4 while the displayed table is eTable 7 | Measure, label, or scale inconsistency |
| C010 | Biguanide count and percentage do not reconcile in eTable 3 | Denominator, proportion, or total inconsistency |
| C011 | Standardized-difference footnote says absolute value while columns contain negative values | Measure, label, or scale inconsistency |

## 8. Candidate Evidence Cards

## C001 — Protocol matching direction conflicts with the final matched cohort

**Candidate statement:** The protocol’s sentence-level matching direction conflicts with the final article’s realized cohort counts and direction.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article — PDF p. 1](<../jama_aminian_2019_oi_190103.pdf#page=1>), [PDF p. 3](<../jama_aminian_2019_oi_190103.pdf#page=3>), [PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>); [protocol — PDF p. 3](<../joi190103supp2_prod.pdf#page=3>).

**Source evidence:** The article reports 2,287 surgical patients and 11,435 matched nonsurgical controls, stating five nonsurgical patients per surgical patient. The protocol says each nonsurgical patient will be matched to five surgical patients.

**Reported-versus-comparator:** Final direction and counts: one surgical patient to five nonsurgical controls; protocol wording: one nonsurgical patient to five surgical patients.

**Reasoning procedure:** Compare the stated group direction against the reported one-to-five ratio and realized cohort counts.

**Calculation:** `2,287 × 5 = 11,435` nonsurgical controls.

**Alternative source-grounded interpretations:** The protocol may contain a planned-method wording inversion or use an unstated ratio convention.

**Mechanical evidence recheck:** All cited locations and statements were found and matched; matching code, MatchIt call, and version history are not supplied.

**Quality-control relevance:** A matching-direction statement should identify the same source and matched group as the realized ratio.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the matching direction incorrectly into an evidence table; no propagation or conclusion change is asserted.

**Human verification steps:** Review the matching code/object and protocol version history; confirm the implemented group direction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Heart-failure ARD does not reconcile with displayed 8-year incidences

**Candidate statement:** The displayed control-minus-surgery heart-failure ARD does not reconcile with the displayed 8-year cumulative incidences.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>), [PDF p. 7](<../jama_aminian_2019_oi_190103.pdf#page=7>); [Supplement 1 — PDF p. 7](<../joi190103supp1_prod.pdf#page=7>).

**Source evidence:** Heart-failure incidence is 6.8% for surgery and 18.9% for controls; Table 2 reports ARD 12.9% (95% CI 10.4%-15.1%).

**Reported-versus-comparator:** Reported ARD 12.9% versus displayed-incidence subtraction 12.1%.

**Reasoning procedure:** Apply the table’s stated nonsurgical-control-minus-surgery contrast and one-decimal rounding bounds.

**Calculation:** `18.9% − 6.8% = 12.1%`; discrepancy `0.8` percentage point. The two one-decimal display ranges do not overlap a displayed 12.9%.

**Alternative source-grounded interpretations:** The ARD point estimate may be separately estimated; the source expressly describes bootstrap CI generation but not a separate ARD point-estimation rule.

**Mechanical evidence recheck:** Locations, values, contrast, and calculation were reproduced; unrounded estimates, bootstrap replicates, and point-estimator formula are unavailable.

**Quality-control relevance:** A displayed absolute effect should be distinguishable from the displayed incidences used to interpret it.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a heart-failure absolute effect that differs from the displayed incidence difference; no conclusion change is asserted.

**Human verification steps:** Obtain the unrounded estimates and ARD point-estimation formula; verify whether 12.9% was intended to equal the displayed incidence subtraction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Coronary-disease ARD does not reconcile with displayed 8-year incidences

**Candidate statement:** The displayed control-minus-surgery coronary-disease ARD does not reconcile with the displayed 8-year cumulative incidences.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>), [PDF p. 7](<../jama_aminian_2019_oi_190103.pdf#page=7>); [Supplement 1 — PDF p. 7](<../joi190103supp1_prod.pdf#page=7>).

**Source evidence:** Coronary-disease incidence is 7.9% for surgery and 11.6% for controls; ARD is 4.2% (1.9%-6.8%).

**Reported-versus-comparator:** Reported ARD 4.2% versus displayed-incidence subtraction 3.7%.

**Reasoning procedure:** Apply the stated control-minus-surgery contrast and compare at the printed one-decimal precision.

**Calculation:** `11.6% − 7.9% = 3.7%`; discrepancy `0.5` percentage point, beyond ordinary displayed rounding.

**Alternative source-grounded interpretations:** A separately bootstrapped or otherwise distinct ARD point estimator may have been used, but is not defined.

**Mechanical evidence recheck:** Locations, values, contrast, arithmetic, and rounding bound were reproduced; unrounded inputs and estimator definition are absent.

**Quality-control relevance:** The displayed absolute effect needs an explicit reconciliation rule when it differs from the displayed incidence contrast.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a coronary-disease absolute effect that differs from the displayed incidence difference; no conclusion change is asserted.

**Human verification steps:** Verify the ARD point-estimation procedure and the corresponding unrounded inputs.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences

**Candidate statement:** The displayed control-minus-surgery cerebrovascular-disease ARD does not reconcile with the displayed 8-year cumulative incidences.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>), [PDF p. 7](<../jama_aminian_2019_oi_190103.pdf#page=7>); [Supplement 1 — PDF p. 7](<../joi190103supp1_prod.pdf#page=7>).

**Source evidence:** Cerebrovascular-disease incidence is 4.1% for surgery and 5.6% for controls; ARD is 1.8% (95% CI -0.03% to 3.4%).

**Reported-versus-comparator:** Reported ARD 1.8% versus displayed-incidence subtraction 1.5%.

**Reasoning procedure:** Apply the stated contrast and compare the printed one-decimal point estimates; the CI endpoint is not treated as a point-estimation rule.

**Calculation:** `5.6% − 4.1% = 1.5%`; discrepancy `0.3` percentage point, beyond the approximate 0.10-point rounding bound.

**Alternative source-grounded interpretations:** The ARD may use a distinct point estimator not stated in the supplied package.

**Mechanical evidence recheck:** Values, locations, and calculation were reproduced; the point-estimator definition and unrounded inputs are missing.

**Quality-control relevance:** The point estimate should be interpretable against its displayed cumulative incidences.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a cerebrovascular absolute effect that differs from the displayed incidence difference; no conclusion change is asserted.

**Human verification steps:** Confirm the ARD estimator and whether it was intended to reconcile to 1.5% at displayed precision.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Nephropathy ARD does not reconcile with displayed 8-year incidences

**Candidate statement:** The displayed control-minus-surgery nephropathy ARD does not reconcile with the displayed 8-year cumulative incidences.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>), [PDF p. 7](<../jama_aminian_2019_oi_190103.pdf#page=7>); [Supplement 1 — PDF p. 7](<../joi190103supp1_prod.pdf#page=7>).

**Source evidence:** Nephropathy incidence is 6.1% for surgery and 16.3% for controls; ARD is 11.1% (8.8%-13.6%).

**Reported-versus-comparator:** Reported ARD 11.1% versus displayed-incidence subtraction 10.2%.

**Reasoning procedure:** Apply the stated contrast and assess the difference at displayed precision.

**Calculation:** `16.3% − 6.1% = 10.2%`; discrepancy `0.9` percentage point.

**Alternative source-grounded interpretations:** The ARD may be separately estimated, but the table states only bootstrap CI generation and no separate point-estimate rule.

**Mechanical evidence recheck:** Direct values, contrast, and arithmetic were reproduced; estimator formula, unrounded inputs, and replicates are unavailable.

**Quality-control relevance:** A separate point-estimation convention should be stated when it changes the displayed absolute effect.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a nephropathy absolute effect that differs from the displayed incidence difference; no conclusion change is asserted.

**Human verification steps:** Obtain the ARD point-estimation procedure and unrounded 8-year values.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences

**Candidate statement:** The displayed control-minus-surgery atrial-fibrillation ARD does not reconcile with the displayed 8-year cumulative incidences.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Main article — PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>), [PDF p. 7](<../jama_aminian_2019_oi_190103.pdf#page=7>); [Supplement 1 — PDF p. 7](<../joi190103supp1_prod.pdf#page=7>).

**Source evidence:** Atrial-fibrillation incidence is 7.9% for surgery and 13.6% for controls; ARD is 6.5% (4.4%-8.7%).

**Reported-versus-comparator:** Reported ARD 6.5% versus displayed-incidence subtraction 5.7%.

**Reasoning procedure:** Apply the table’s control-minus-surgery rule and compare the printed point estimates.

**Calculation:** `13.6% − 7.9% = 5.7%`; discrepancy `0.8` percentage point, beyond ordinary displayed rounding.

**Alternative source-grounded interpretations:** The ARD may be separately estimated; the package does not define that point-estimation procedure.

**Mechanical evidence recheck:** Cited values, locations, contrast, arithmetic, and rounding bound were reproduced; unrounded inputs and estimator definition are absent.

**Quality-control relevance:** A reader needs to know whether an ARD is direct subtraction or a distinct estimator.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an atrial-fibrillation absolute effect that differs from the displayed incidence difference; no conclusion change is asserted.

**Human verification steps:** Confirm the source of the 6.5% estimate and its relation to the reported incidences.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Supplement tables use different nonsurgical medication denominators at baseline

**Candidate statement:** Two Supplement 1 baseline medication displays use nonsurgical denominators differing by two without a printed reconciliation rule.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 5](<../joi190103supp1_prod.pdf#page=5>), [PDF p. 14](<../joi190103supp1_prod.pdf#page=14>).

**Source evidence:** eTable 3 labels matched nonsurgical baseline medication data `N=11,435`; eTable 10 labels its nonsurgical year-0 medication-proportion sample `11,433`. Both surgery values are 2,287.

**Reported-versus-comparator:** eTable 3 nonsurgical `N=11,435` versus eTable 10 year-0 nonsurgical `N=11,433`.

**Reasoning procedure:** Compare same-group, baseline/index-date denominator labels and search the supplied pages for a missingness, timing, or inclusion rule.

**Calculation:** `11,435 − 11,433 = 2` participants.

**Alternative source-grounded interpretations:** eTable 10 may be a complete-case or availability subset, while eTable 3 may classify all matched controls.

**Mechanical evidence recheck:** Both labels and values were found; no printed rule accounts for the two-person difference.

**Quality-control relevance:** Baseline denominator definitions should be traceable across medication displays.

**Potential downstream evidence impact:** If confirmed, an extractor could select an inconsistent medication denominator; no propagation or conclusion change is asserted.

**Human verification steps:** Identify the inclusion, availability, or missingness rule governing the eTable 10 year-0 denominator.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Medication comparison is labeled as two different named tests

**Candidate statement:** Matched medication comparisons are associated with both a two-sample proportions-test label and a Fisher-exact-test label.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article — PDF p. 4](<../jama_aminian_2019_oi_190103.pdf#page=4>), [PDF p. 10](<../jama_aminian_2019_oi_190103.pdf#page=10>); [Supplement 1 — PDF p. 12](<../joi190103supp1_prod.pdf#page=12>).

**Source evidence:** Methods and eTable 8 name a two-sample proportions test. Figure 5 labels matched 8-year P values as Fisher exact tests. The same six result-family P values appear, including insulin `P=.008` and five `P<.001` values.

**Reported-versus-comparator:** Two-sample proportions-test label versus Fisher-exact-test label for the matched year-8 medication result family.

**Reasoning procedure:** Match outcome family, time point, population, and P-value displays, then compare the named procedures without assuming their implementation.

**Calculation:** Five matched categories show `P<.001` and insulin shows `P=.008` in the Figure 5/eTable 8 family; no test calculation is possible from the supplied aggregate displays.

**Alternative source-grounded interpretations:** “Two-sample proportions test” may be a generic family description, or Fisher exact testing may have been used specifically at year 8.

**Mechanical evidence recheck:** Both procedure labels and matched P-value family were reproduced; contingency cells, sidedness, software, and test settings are unavailable.

**Quality-control relevance:** A reported inferential procedure should be identifiable for the displayed result it accompanies.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an ambiguous test-method label; no numerical effect or conclusion change is asserted.

**Human verification steps:** Determine which procedure generated each 8-year medication P value and which label should govern.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Time-varying-HR narrative cites eTable 4 while the displayed table is eTable 7

**Candidate statement:** The time-varying-HR narrative cites eTable 4, while the adjacent and repeated display is labeled eTable 7; actual eTable 4 reports a different measure.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 6](<../joi190103supp1_prod.pdf#page=6>), [PDF p. 10](<../joi190103supp1_prod.pdf#page=10>), [PDF p. 19](<../joi190103supp1_prod.pdf#page=19>).

**Source evidence:** Page 19 says eTable 4 displays adjusted HRs/CIs at 2, 5, and 8 years, whereas the adjacent and repeated table is headed eTable 7. Actual eTable 4 reports cause-specific event rates.

**Reported-versus-comparator:** Narrative reference `eTable 4` versus matching HR display `eTable 7`; eTable 4’s displayed content is rates rather than time-varying HRs.

**Reasoning procedure:** Compare the narrative’s described measure/time points with the labels and content of the adjacent, repeated, and actual referenced tables.

**Calculation:** This is a label-and-content identity comparison, not an arithmetic calculation.

**Alternative source-grounded interpretations:** The narrative may preserve numbering from an earlier supplement version; the supplied package does not establish the intended wording.

**Mechanical evidence recheck:** The p. 19 narrative, p. 10 duplicate eTable 7, and p. 6 eTable 4 were directly confirmed.

**Quality-control relevance:** A table cross-reference should lead a reader to the table containing the named measure and time points.

**Potential downstream evidence impact:** If confirmed, a reader or extractor could follow the cited table number to a different measure; no effect-estimate or conclusion change is asserted.

**Human verification steps:** Check supplement version history and confirm whether the narrative should cite eTable 7 or a different intended display.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — Biguanide count and percentage do not reconcile in eTable 3

**Candidate statement:** The surgery-group biguanide count, printed denominator, and printed percentage do not reconcile.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 5](<../joi190103supp1_prod.pdf#page=5>).

**Source evidence:** eTable 3 labels the metabolic-surgery group `N=2,287` and prints biguanides as `1,530 (67.9%)`.

**Reported-versus-comparator:** Printed 67.9% versus 66.9% obtained from the printed count and denominator.

**Reasoning procedure:** Divide the printed numerator by the column denominator and round to one decimal place.

**Calculation:** `1,530 / 2,287 × 100 = 66.8999…%`, which rounds to `66.9%`; conversely, 67.9% of 2,287 is approximately 1,552.6.

**Alternative source-grounded interpretations:** The count or percentage may be transcribed incorrectly, or a different unprinted denominator may have been used.

**Mechanical evidence recheck:** The direct table location, numerator, denominator, percentage, and calculation were reproduced; no alternate denominator is printed.

**Quality-control relevance:** A count and percentage should reconcile to the displayed denominator or state an alternative denominator.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a discordant biguanide count or percentage; no broader effect or conclusion change is asserted.

**Human verification steps:** Verify the intended count, percentage, and denominator from the underlying medication dataset/table generation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — Standardized-difference footnote says absolute value while columns contain negative values

**Candidate statement:** Table 1’s footnote defines standardized differences as an absolute value, while the displayed columns include negative values.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_aminian_2019_oi_190103.pdf#page=5>), [PDF p. 6](<../jama_aminian_2019_oi_190103.pdf#page=6>).

**Source evidence:** Footnote b defines standardized differences as the “absolute value” of group difference divided by pooled SD. The columns contain negative values including index date `-42.6/-15.9`, men `-28.0/-2.9`, and age `-75.3/-19.9`.

**Reported-versus-comparator:** Absolute-value definition versus negative standardized-difference entries.

**Reasoning procedure:** Apply the nonnegativity of an absolute value and inspect whether the signs follow a stated directional convention.

**Calculation:** For any real value `x`, `|x| ≥ 0`; negative printed values cannot simultaneously be absolute values under the footnote. The signs follow checkable surgery-minus-control examples (for example, men 34.5% versus 48.2% and `-28.0`).

**Alternative source-grounded interpretations:** The columns may intentionally show signed standardized differences in surgery-minus-control direction, with “absolute value” retained in the footnote.

**Mechanical evidence recheck:** The footnote, negative entries, and direction examples were confirmed on the cited pages; table-generation convention is not supplied.

**Quality-control relevance:** The balance-measure definition and displayed sign convention should be mutually interpretable.

**Potential downstream evidence impact:** If confirmed, an extractor could copy or interpret the balance-measure convention inconsistently; no effect-estimate or conclusion change is asserted.

**Human verification steps:** Confirm whether signed standardized differences were intended and reconcile the footnote or displayed signs accordingly.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## 9. Downstream Evidence-Chain Considerations

If a candidate is confirmed, the relevant value, denominator, table reference, matching direction, or test label could be copied into a systematic review, meta-analysis, guideline evidence table, or other downstream extraction product. This is a bounded possibility only. The supplied package does not establish that copying occurred, that any conclusion changed, or that serious harm occurred.

## 10. Limitations and Missing Definitions

The supplied PDFs do not include matching code, analysis/table-generation code, unrounded cumulative-incidence and ARD inputs, bootstrap replicates, coefficient-level SEs, test statistics, degrees of freedom, covariance or variance-estimator details, raw medication contingency cells, exact test-function settings, reconciliation rules for the baseline medication denominators, or document version history. These absences limit only the specified reconstructions and adjudication questions; they do not negate the direct observations recorded above. See the canonical [limitations artifact](<review_1_5_1/limitations.md>).

## 11. Human Adjudication Checklist

1. Confirm every cited source location against the direct PDFs.
2. Obtain the missing code, unrounded inputs, or version history where required for the candidate.
3. Decide validity, importance, and any action in each card’s blank adjudication fields.
4. Preserve the stable candidate IDs and record any decision separately from this quality-control review.

## 12. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Direct-source page counts were obtained with `pdfinfo`; native/layout extraction and targeted reusable rendered/OCR assets served as locators only. Direct PDFs were not modified. The source coverage partition is `27 reusable + 12 fresh-required = 39`, and all 39 units were mapped. Before-run direct and reused-artifact hashes are recorded in `source_hashes_before.sha256` and `reused_artifact_hashes_before.sha256`; post-run integrity confirmation is coordinated after assembly.

### Agent-execution metadata

The manifest records the coordinator and ten fresh specialists, including this report generator. Statistical passes used distinct runtime IDs `root/statistics_pass_1` and `root/statistics_pass_2`, both `gpt-5.6-terra` at high reasoning effort. Other manifested stages comprise reuse curation, main/support mapping, numeric and cross-source checking, evidence recheck, and quality audit. See [agent execution manifest](<review_1_5_1/agent_execution_manifest.md>) and [coverage manifest](<review_1_5_1/coverage_manifest.md>).

### Performance

- **Target basis:** Three supplied PDFs contain 39 direct-source pages (12-page main article, 20-page results supplement, and 7-page protocol); reusable native text provisionally covers 27 pages, leaving 12 pages for fresh direct-source mapping. The package is materially smaller and has a lower fresh-extraction burden than the 102-unit/81-fresh calibration package, but still requires complete main/support mapping, two independent statistical passes, cross-lane review, candidate recheck, audit, and report generation.
- **Total source units:** 39
- **Fresh-source units:** 12
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-18T22:17:16Z
- **Finished UTC:** 2026-08-18T23:02:13Z
- **Observed elapsed minutes:** 45.0
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Final evidence-quality audit identified two source-grounded omissions requiring stable-ID append, direct-source recheck, and audit closure; full 11-card report assembly.

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

The runtime did not expose authoritative response-level token counts for the coordinator or any specialist. Accordingly, all 11 manifested agents have explicit `UNAVAILABLE` ledger rows with no inferred counts; the zero above is only the known subtotal and is not an estimate of actual use.

| Model | Agents | Unavailable records | Known total tokens | Known token cost (USD) | Complete estimated token cost (USD) | Status |
|---|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 3 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 8 | 8 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

Per-agent detail and the dated pricing basis are in [the token usage summary](<review_1_5_1/token_usage_summary.md>). The calculation status is `INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE`; no token count or price was approximated from review text.

Token amounts, once finalized, are token-only API-equivalent estimates under the dated pricing snapshot, not invoices; non-token tools, containers, storage, subscriptions, taxes, and other vendor charges are outside the calculation. Per-agent detail will be retained in `review_1_5_1/token_usage_summary.md`; cached input and cache-write counts are input subsets and reasoning tokens are output subsets, not additional total tokens.

This report includes all stable IDs in the current candidate ledger: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, and C011. Each remains **Pending Human Adjudication**. No review queue, top-N subset, severity ranking, deferred-by-cap section, or old AI disposition is included.
