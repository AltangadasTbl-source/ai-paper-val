# Quantitative Quality-Control Consistency Review — Workflow 1.5.2

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. This is a source-first quantitative reporting quality-control review, not a finding about authors, study conclusions, or clinical effects.

## Executive Quality-Control Summary

Complete fresh review of six supplied PDFs (100 PDF-page units) registered **8** distinct candidate consistency issues: two denominator/proportion displays, two cross-document numeric displays, and four measure, label, or scale displays. Small preventable reporting defects can matter when a later data extractor or evidence product reuses a printed field; this review does not establish propagation, a conclusion change, or serious harm.

## Package and Fresh-Processing Provenance

The direct package comprised the main article `jama_bluth_2019_oi_190055_16092.pdf` (DOC-001; 14 pages) and support PDFs `joi190055supp1_prod_16092.pdf` through `joi190055supp5_prod_16092.pdf` (DOC-002–DOC-006; 36, 3, 3, 43, and 1 pages). All 100 units were freshly processed; no prior audit derivative was used as evidence. Fresh native and layout text were generated for every unit. The source inventory, extraction decisions, and SHA-256 values are recorded in [the current-run source inventory](review_1_5_2/source_inventory.md), [evidence-asset inventory](review_1_5_2/evidence_asset_inventory.md), and [pre-review hashes](review_1_5_2/source_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

All direct-source rows are complete: DOC-001 14/14, DOC-002 36/36, DOC-003 3/3, DOC-004 3/3, DOC-005 43/43, and DOC-006 1/1 freshly mapped units, for **100/100**. The coverage plan assigns every stage a separate artifact path and records report generation for all eight stable IDs in [the coverage manifest](review_1_5_2/coverage_manifest.md).

The scope was numeric, denominator/proportion/total, inferential-statistical, cross-document, measure/label/scale, and rate-versus-count consistency. It excluded broad methodology, clinical, misconduct, raw-data, and conclusion audits. No candidate was created from P-value display precision alone; no coherent `P = 0` display was encountered in the reviewed relationships.

## Quantitative and Statistical Relationship Coverage

The fresh numeric relationship inventory contains **55/55** canonical relationships (N001–N055). The statistical inventory contains **31/31** relationships (S001–S031). Independent statistical pass 1 completed 31/31 and independent statistical pass 2 completed 31/31; the second pass revisited every stable candidate and added none. Completion markers and relationship-level limitations are in [numeric consistency review](review_1_5_2/checkers/numeric_consistency.md), [statistical pass 1](review_1_5_2/checkers/statistical_pass_1.md), [cross-source review](review_1_5_2/checkers/cross_source_consistency.md), and [statistical pass 2](review_1_5_2/checkers/statistical_pass_2.md).

## Candidate Index

| ID   | Candidate consistency issue                                      | Category                                        |
|------|------------------------------------------------------------------|-------------------------------------------------|
| C001 | Intraoperative adverse-event threshold definitions differ        | Measure, label, or scale inconsistency          |
| C002 | White-blood-cell magnitude and unit use incompatible scales      | Measure, label, or scale inconsistency          |
| C003 | Per-protocol effect estimates have a generic, unreconciled label | Measure, label, or scale inconsistency          |
| C004 | eFigure 11 body label conflicts with mortality statistics        | Measure, label, or scale inconsistency          |
| C005 | Abstract hypoxemia interval upper endpoint differs in sign       | Cross-document numeric inconsistency            |
| C006 | Matched synthetic-colloid rows have different P values           | Cross-document numeric inconsistency            |
| C007 | Monitoring percentages do not reproduce from fractions           | Denominator, proportion, or total inconsistency |
| C008 | Reversal percentages do not reproduce from fractions             | Denominator, proportion, or total inconsistency |

## Candidate Evidence Cards

## C001 — Intraoperative adverse-event threshold definitions differ within the main article

**Candidate statement:** The methods and Table 3 footnotes print different operational criteria for the same named intraoperative hypoxemia and hypotension outcomes. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 3](../jama_bluth_2019_oi_190055_16092.pdf#page=3); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Source evidence:** P. 3 defines hypoxemia as SpO2 at or below 92% for more than 1 minute and hypotension as systolic pressure below 90 mm Hg for more than 2 minutes. P. 10 adds baseline-dependent alternative thresholds (greater than 5% SpO2 decline when already below 92%; greater than 10-mm-Hg systolic decline when already below 90) and does not print the durations.

**Reported-versus-comparator:** The same named outcomes have a duration-based methods definition versus a table-footnote definition with extra baseline-dependent branches.

**Reasoning procedure:** Direct observation: the two printed rule sets are textually nonidentical. Diagnostic inference: the alternative branches could affect reported numerators, but the package does not identify which complete algorithm generated Table 3.

**Calculation:** Logical comparison only: the methods contain “more than 1 minute” and “more than 2 minutes”; the footnotes omit these durations and add two alternative branches.

**Alternative source-grounded interpretations:** P. 3 may be abbreviated while p. 10 is complete, or the footnote may describe a table-specific rescue convention. The supplied package does not resolve this.

**Mechanical evidence recheck:** Recheck located both pages, reproduced the nonidentical criteria, and retained the unavailable visual decoding of the p. 3 inequality glyph as a limitation.

**Quality-control relevance:** Outcome algorithms should be identifiable when interpreting Table 3 event counts.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a different hypoxemia or hypotension definition into a systematic review or later evidence product; no downstream use or conclusion change is established.

**Human verification steps:** Visually inspect both pages; identify the count-generating algorithm, its durations, and whether either definition is explicitly abbreviated or superseded.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — White-blood-cell magnitude and unit are on incompatible printed scales

**Candidate statement:** Table 1 pairs white-blood-cell values in the thousands with a `×10^9/L` unit. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](../jama_bluth_2019_oi_190055_16092.pdf#page=6); [joi190055supp4_prod_16092.pdf — PDF p. 20](../joi190055supp4_prod_16092.pdf#page=20).

**Source evidence:** DOC-001 prints `White blood cells, ×10^9/L` with 8224 (2346) and 8347 (2758). DOC-005 uses leukocyte thresholds below 4000 or above 12000 cells/mm3.

**Reported-versus-comparator:** Four-digit values are displayed beneath a per-litre `10^9` unit, while the supplied supplement gives comparable four-digit cells/mm3 thresholds.

**Reasoning procedure:** Direct observation: the printed magnitude/unit pairing differs by scale from the internal threshold scale. Diagnostic inference: a unit-label carryover or omitted decimal placement could explain it; neither is documented.

**Calculation:** `8224 cells/mm3 = 8.224 ×10^9/L`; `8347 cells/mm3 = 8.347 ×10^9/L`; conversely, `8224 ×10^9/L = 8,224,000 cells/mm3`. This is a factor-of-1000 identity, not a rounding difference.

**Alternative source-grounded interpretations:** The intended unit may be cells/mm3, or the intended displayed values under `×10^9/L` may be about 8.224 and 8.347.

**Mechanical evidence recheck:** Recheck found the Table 1 row and supplement thresholds and reproduced the conversion. The multiplication glyph on p. 6 requires visual confirmation.

**Quality-control relevance:** Laboratory measure units and magnitudes should be mutually interpretable within the supplied package.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incompatible baseline laboratory unit or magnitude into a review table or later evidence product; no downstream use or conclusion change is established.

**Human verification steps:** Visually inspect the unit glyph and obtain the authoritative laboratory export or table specification to determine whether the unit or decimal placement is intended.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Per-protocol effect estimates are generically labeled and do not reproduce as crude ratios

**Candidate statement:** Supplement eTable 8 labels its column only `Effect Estimate 95% CI`, and the printed estimates do not equal crude ratios from its displayed counts. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi190055supp4_prod_16092.pdf — PDF p. 29](../joi190055supp4_prod_16092.pdf#page=29); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Source evidence:** eTable 8 gives PPC 186/917 versus 209/912 with 0.92, pleural effusion 38/917 versus 18/912 with 1.37, and cardiopulmonary edema 15/917 versus 7/912 with 1.36, under a generic header. The analogous main Table 3 calls its effect column `Risk Ratio`.

**Reported-versus-comparator:** Generic eTable 8 estimates are compared with crude risk and odds ratios from their own exact inputs; the main table is a label comparator, not a numerical per-protocol comparator.

**Reasoning procedure:** Direct observation: the header is generic and the printed effects do not equal the crude ratios. Diagnostic inference: the estimates could be adjusted or model-based; the package does not name their measure, direction, estimand, model, variance method, or adjustment set.

**Calculation:** Crude high-versus-low risk ratios are 0.885100, 2.099600, and 2.131173; crude odds ratios are 0.855864, 2.147137, and 2.149984. None equals 0.92, 1.37, or 1.36 at displayed precision. These diagnostics do not assert an error in an unidentified model.

**Alternative source-grounded interpretations:** An adjusted, clustered, site-effect, time-to-event, or other model could produce different values, but its definition is absent from the eTable 8 display.

**Mechanical evidence recheck:** Recheck confirmed the counts, denominators, estimates, intervals, generic header, and main-table label; it retained the unreported model definition as the exact missing input.

**Quality-control relevance:** An effect estimate should have an identifiable measure, reference direction, and model when it cannot be read as a crude ratio.

**Potential downstream evidence impact:** If confirmed, a review or meta-analysis extractor could misclassify the eTable 8 effect measure or direction; no downstream use or conclusion change is established.

**Human verification steps:** Obtain the per-protocol analysis specification and confirm the named estimand, reference direction, model, adjustments, variance, interval, and test for eTable 8.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eFigure 11 body text assigns mortality statistics to extra-pulmonary complications

**Candidate statement:** eFigure 11 identifies 5-day mortality in its title and numerical result, while its body sentence names postoperative extra-pulmonary complications. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi190055supp4_prod_16092.pdf — PDF p. 41](../joi190055supp4_prod_16092.pdf#page=41); [joi190055supp4_prod_16092.pdf — PDF p. 40](../joi190055supp4_prod_16092.pdf#page=40); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](../jama_bluth_2019_oi_190055_16092.pdf#page=10).

**Source evidence:** eFigure 11 prints 0.5% versus 0.3%, hazard ratio 1.67 (0.40–6.97), P=.484 for 5-day mortality, but calls the rate postoperative extra-pulmonary complications. eFigure 10 prints PEPC 16.9% versus 15.2%, HR 1.12 (0.89–1.39), P=.314; DOC-001 matches the mortality result.

**Reported-versus-comparator:** The p. 41 body label is compared with its mortality title/statistics, the matching main-table mortality result, and the separately printed PEPC statistics on p. 40.

**Reasoning procedure:** Direct observation: mortality and PEPC are distinct named outcomes attached to distinct supplied statistic sets. Diagnostic inference: a p. 40 production carryover is plausible but is not documented.

**Calculation:** Identity comparison: the p. 41 0.5%/0.3% and HR 1.67 match mortality, not the p. 40 PEPC 16.9%/15.2% and HR 1.12.

**Alternative source-grounded interpretations:** The body phrase may have been copied from eFigure 10 while the p. 41 title and mortality statistics are intended. The plot itself was not visually available.

**Mechanical evidence recheck:** Recheck confirmed all three locations and the distinct statistic sets; the visual identity of the p. 41 curve remains unavailable.

**Quality-control relevance:** A figure body label should identify the same outcome as its title and displayed statistics.

**Potential downstream evidence impact:** If confirmed, an extractor could assign mortality statistics to PEPC, or vice versa, in an evidence table; no downstream use or conclusion change is established.

**Human verification steps:** Visually inspect eFigure 11 and its curve/axes, then confirm the intended outcome name for its body text.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Abstract hypoxemia confidence interval loses the negative sign on its upper endpoint

**Candidate statement:** The abstract and Table 3 print opposite signs for the upper endpoint of the same hypoxemia difference interval. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](../jama_bluth_2019_oi_190055_16092.pdf#page=1); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](../jama_bluth_2019_oi_190055_16092.pdf#page=9).

**Source evidence:** The abstract prints 5.0% versus 13.6%, difference −8.6%, interval −11.1% to 6.1%, P\<.001. Table 3 prints the matched 49/989 and 134/987, the same rounded percentages/difference, and interval −11.1 to −6.1.

**Reported-versus-comparator:** Matched outcome, population, contrast, estimate, and interval displays differ only in the sign of the upper endpoint.

**Reasoning procedure:** Direct observation: the upper endpoints are 6.1 and −6.1. Diagnostic inference: a typographical minus-sign omission is plausible, but the package does not identify the authoritative production value.

**Calculation:** `49/989 × 100 = 4.9545%`; `134/987 × 100 = 13.5765%`; the unrounded difference is −8.6220 percentage points, consistent with −8.6. The Table 3 interval is wholly negative and contains −8.6; the abstract interval crosses zero. Rounding cannot change the endpoint sign.

**Alternative source-grounded interpretations:** The abstract may have omitted a minus sign, or Table 3 may be the intended display; no correction record is supplied.

**Mechanical evidence recheck:** Recheck found both matched displays, reproduced the fractions, and confirmed that the endpoint sign difference is not a rounding issue.

**Quality-control relevance:** Repeated confidence intervals for the same result should retain their endpoint signs.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a confidence interval that crosses zero instead of one that does not into a systematic review or later evidence product; no downstream use or conclusion change is established.

**Human verification steps:** Compare the abstract, Table 3, and authoritative production/statistical output to identify the intended upper endpoint.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Matched synthetic-colloid-use rows print different P values

**Candidate statement:** The main article and supplement repeat the same synthetic-colloid-use counts but print P=.09 and P=.10. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](../jama_bluth_2019_oi_190055_16092.pdf#page=8); [joi190055supp4_prod_16092.pdf — PDF p. 24](../joi190055supp4_prod_16092.pdf#page=24).

**Source evidence:** Both locations print 74/989 (7.5%) versus 56/987 (5.7%). The main table prints difference 1.8 (−0.3 to 4.0), P=.09; eTable 3 prints P=.10 for the synthetic-colloid row.

**Reported-versus-comparator:** Identical displayed group sizes, counts, percentages, population, and contrast have P displays .09 versus .10.

**Reasoning procedure:** Direct observation: `.09 ≠ .10`. Diagnostic inference: different tests or rounding pipelines could explain it, but neither location identifies a row-specific rule; no tail probability is reconstructed.

**Calculation:** `74/989 = 7.4823%`; `56/987 = 5.6738%`; difference = 1.8085 percentage points. The candidate comparison is the printed P values, not a reconstructed P value.

**Alternative source-grounded interpretations:** The displays may use different undocumented tests or rounding pipelines, or one may be transcribed differently.

**Mechanical evidence recheck:** Recheck confirmed p. 24’s 0.10 belongs to synthetic colloids and that its separate 0.09 belongs to the next summary line, not this row.

**Quality-control relevance:** A matched repeated binary result should identify any intentional difference in its P-value calculation or display.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a different P value for this row into a review table or later evidence product; no downstream use or conclusion change is established.

**Human verification steps:** Check the row-specific test, sidedness, continuity/variance rule, unrounded P values, and rounding pipeline for both displays.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Neuromuscular-monitoring percentages do not match their printed fractions

**Candidate statement:** Table 2 monitoring percentages do not reproduce from their printed numerators and denominators. **Pending Human Adjudication.**

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](../jama_bluth_2019_oi_190055_16092.pdf#page=8).

**Source evidence:** The monitoring row prints 632/982 (64.9%) versus 651/984 (67.7%), with difference −1.8 (−6.0 to 2.4), P=.40.

**Reported-versus-comparator:** Each parenthetical percentage is compared with its adjacent printed fraction; the row difference is also compared with the fraction-derived and displayed-percentage differences.

**Reasoning procedure:** Direct observation: neither percentage equals its fraction under one-decimal rounding and the printed percentages subtract to a different difference. Diagnostic inference: the displayed −1.8 may have been generated from counts, but the table does not state its rule.

**Calculation:** `632/982 × 100 = 64.3585%` → 64.4%, not 64.9%; `651/984 × 100 = 66.1585%` → 66.2%, not 67.7%. Count-derived difference = −1.8001 points; printed percentage subtraction = −2.8 points.

**Alternative source-grounded interpretations:** One or more counts, denominators, percentages, or the difference may have been transcribed differently; an alternative denominator or adjustment is not supplied.

**Mechanical evidence recheck:** Recheck located the complete row and reproduced both fraction-to-percentage calculations and the two different displayed differences.

**Quality-control relevance:** A `No./total No. (%)` display should let readers reconcile adjacent counts, denominators, and percentages.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy inconsistent monitoring proportions or a different contrast into a systematic review or later evidence product; no downstream use or conclusion change is established.

**Human verification steps:** Verify the authoritative numerator, denominator, percentage, and difference fields and determine whether an unprinted denominator, weighting, or adjustment was used.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Neuromuscular-reversal percentages do not match their printed fractions

**Candidate statement:** Table 2 reversal percentages do not reproduce from their printed numerators and denominators. **Pending Human Adjudication.**

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](../jama_bluth_2019_oi_190055_16092.pdf#page=8).

**Source evidence:** The reversal row prints 724/982 (74.3%) versus 723/984 (75.2%), with difference 0.2 (−3.6 to 4.1), P=.90.

**Reported-versus-comparator:** Each parenthetical percentage is compared with its adjacent printed fraction; the printed percentages imply a different-sign difference from the displayed difference.

**Reasoning procedure:** Direct observation: neither percentage equals its fraction under one-decimal rounding, and 74.3 − 75.2 = −0.9 while the row prints +0.2. Diagnostic inference: a model-based calculation or unprinted inputs could explain +0.2, but no such rule is supplied.

**Calculation:** `724/982 × 100 = 73.7271%` → 73.7%, not 74.3%; `723/984 × 100 = 73.4756%` → 73.5%, not 75.2%. Fraction-derived difference = +0.2515 points, which ordinarily rounds to +0.3, not +0.2; printed percentage subtraction = −0.9 points.

**Alternative source-grounded interpretations:** One or more counts, denominators, percentages, or the difference may have been transcribed differently, or the difference may use a model or unprinted inputs.

**Mechanical evidence recheck:** Recheck located the complete row and reproduced the fraction arithmetic, ordinary one-decimal rounding, and the sign disagreement.

**Quality-control relevance:** A `No./total No. (%)` display should let readers reconcile its fractions, percentages, and stated contrast.

**Potential downstream evidence impact:** If confirmed, an extractor could copy inconsistent reversal proportions or a conflicting direction into a systematic review or later evidence product; no downstream use or conclusion change is established.

**Human verification steps:** Verify the authoritative numerator, denominator, percentage, and difference fields and obtain the exact rule, unrounded inputs, or model for the positive 0.2 difference.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

These are candidate reporting-consistency issues, not demonstrated downstream effects. If a candidate is confirmed, the relevant counts, percentages, intervals, effect labels, outcome labels, definitions, units, or P value could be copied into a data-extraction form, systematic review, meta-analysis, guideline, or later evidence product. The supplied package does not show that such copying occurred, that any conclusion changed, or that harm resulted.

## Limitations and Missing Definitions

Fresh text covered all 100 source units, but `pdfinfo`, Linux rendering tools, and CPU Tesseract were unavailable. DOC-001’s fresh text has 14 form-feed pages despite a preliminary 10-page `file` string; the fresh count governed coverage. Page rendering/OCR were unavailable; DOC-001 Tables 2/3 are partly column-serialized, graphical values on DOC-005 pp. 31–37 and 42 were not invented, and the eFigure 11 plotted curve could not be visually identified. The p. 3 inequality and p. 6 multiplication glyphs also need visual confirmation. Candidate-specific missing definitions include the complete adverse-event algorithm, intended white-blood-cell scale, eTable 8 measure/model/reference/variance/test, synthetic-colloid tests and rounding, and authoritative neuromuscular row fields. These limitations do not establish a conclusion change and do not remove any stable ID. See [limitations](review_1_5_2/limitations.md).

## Human Adjudication Checklist

For each card, confirm the cited original PDF locations, reproduce the stated arithmetic or identity comparison, identify any missing analysis or production definition, determine the intended display from the authoritative record, and complete all five blank fields on that card. Keep each C ID distinct when documenting a decision.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The current-run coverage and exact fresh-processing methods are recorded in the linked provenance artifacts above. The initial source SHA-256 inventory covers six supplied PDFs; the coordinator must compare it with the post-review hash inventory before final validation. No web source or prior audit derivative was used as review evidence.

### Agent execution

| Stage               | Runtime agent ID            | Model         | Reasoning effort | Start mode      |
|---------------------|-----------------------------|---------------|------------------|-----------------|
| coordinator         | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol   | high             | CURRENT_SESSION |
| fresh preprocessing | /root/fresh_preprocessing   | gpt-5.6-terra | medium           | FRESH_SPAWN     |
| main mapping        | /root/main_mapping          | gpt-5.6-terra | medium           | FRESH_SPAWN     |
| support mapping     | /root/support_mapping       | gpt-5.6-terra | medium           | FRESH_SPAWN     |
| numeric review      | /root/numeric_checks        | gpt-5.6-terra | medium           | FRESH_SPAWN     |
| cross-source review | /root/cross_source_checks   | gpt-5.6-terra | medium           | FRESH_SPAWN     |
| statistical pass 1  | /root/statistics_pass_1     | gpt-5.6-terra | high             | FRESH_SPAWN     |
| evidence recheck    | /root/evidence_recheck      | gpt-5.6-sol   | high             | FRESH_SPAWN     |
| statistical pass 2  | /root/statistics_pass_2     | gpt-5.6-terra | high             | FRESH_SPAWN     |
| quality audit       | /root/quality_audit         | gpt-5.6-sol   | high             | FRESH_SPAWN     |
| report generation   | /root/report_generation     | gpt-5.6-terra | medium           | FRESH_SPAWN     |

The coordinator will normalize the manifest IDs and complete final source-integrity and accounting checks after Markdown assembly.

### Performance

- **Target basis:** Six direct PDF sources comprising one 14-page main article and five heterogeneous support files (36, 3, 3, 43, and 1 pages); all 100 PDF pages require fresh inventory and mapping, with two long support documents, multiple cross-document checks, and no reusable evidence units. The 100-unit scope is near the 102-page calibration package but has one additional direct source and a fully fresh burden, so a bounded 40-60 minute planning target is selected.
- **Total source units:** 100
- **Fresh-source units:** 100
- **Target elapsed minutes:** 40-60
- **Started UTC:** 2026-08-24T00:20:28Z
- **Finished UTC:** 2026-08-24T01:07:37Z
- **Observed elapsed minutes:** 47.2
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model                             | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|-----------------------------------|-------------:|--------------------:|-------------------:|--------------:|-----------------:|-------------:|-----------------------------------------:|
| gpt-5.6-sol | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 known; complete estimate __ |
| gpt-5.6-terra | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 known; complete estimate __ |

The coordinator will replace these single-line accounting placeholders from the authoritative response-level ledger and dated pricing snapshot after this report-agent response. Cached input and cache-write values are input subsets, and reasoning is an output subset; they are not added again to total tokens. Per-agent detail is in [token_usage_summary.md](review_1_5_2/token_usage_summary.md); all monetary amounts are token-only API-equivalent estimates, not invoices.
