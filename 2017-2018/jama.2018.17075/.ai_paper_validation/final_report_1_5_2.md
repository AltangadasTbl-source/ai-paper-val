# Quantitative Quality-Control Consistency Review: POLAR Randomized Clinical Trial Package

## Pending Human Adjudication Notice

**All eight records in this report are Pending Human Adjudication.** They are source-grounded quantitative reporting quality-control candidates, not corrections, scientific validity findings, severity ratings, or editorial dispositions. No candidate is based solely on a displayed zero P value.

## Executive Quality-Control Summary

Fresh source-first processing identified **8** distinct quantitative reporting quality-control candidates: one numeric or arithmetic inconsistency, one cross-document numeric inconsistency, three statistical reporting inconsistencies, two measure/label/scale inconsistencies, and one denominator/proportion/total inconsistency. The complete stable set is C001-C008. Each candidate was mechanically rechecked at its cited supplied-source location and remains Pending Human Adjudication.

The review checked all direct sources and did not use external literature, the web, or prior audit derivatives as evidence. Small preventable reporting defects can matter when later evidence products extract values; this report does not assert that any value was propagated, changed a conclusion, or caused harm.

## Package and Fresh-Processing Provenance

The supplied package contains four direct PDFs: the 10-page main article, a 194-page protocol/SAP/DSMC supplement, a 24-page supplementary-results document, and a 1-page data-sharing statement. Their fresh evidence assets include native text, layout text, and 150-dpi page renderings. Native and layout text were usable for all result-relevant content; direct CPU OCR was therefore not required.

| Source ID | Supplied source | Units | SHA-256 |
|---|---|---:|---|
| DOC-001 | [jama_cooper_2018_oi_180132.pdf — PDF p. 1](<../jama_cooper_2018_oi_180132.pdf#page=1>) | 10 PDF pages | `14987ad9741b9c9f617a24af239ae72407ffe41ee14953df33665f1593e35253` |
| DOC-002 | [joi180132supp1_prod.pdf — PDF p. 1](<../joi180132supp1_prod.pdf#page=1>) | 194 PDF pages | `305596802f9ac59c1e76fd9233529b98d92ef918d13fccd35112109ed60cb547` |
| DOC-003 | [joi180132supp2_prod.pdf — PDF p. 1](<../joi180132supp2_prod.pdf#page=1>) | 24 PDF pages | `b00fbac777719817be84e45f350898aa031a3eb6d17fb73a42de710239f1ab7d` |
| DOC-004 | [joi180132supp3_prod.pdf — PDF p. 1](<../joi180132supp3_prod.pdf#page=1>) | 1 PDF page | `7d6634553269ddfc0208a4e0d7b46639b8212f3126d59e3add8b4b033d42ebf3` |

Fresh asset and extraction decisions are recorded in [evidence_asset_inventory.md](<review_1_5_2/evidence_asset_inventory.md>); the complete direct-source inventory is [source_inventory.md](<review_1_5_2/source_inventory.md>).

## Scope, Complete Coverage, and Exclusions

All 229 direct PDF-page units were freshly required and mapped: DOC-001 10/10, DOC-002 194/194, DOC-003 24/24, and DOC-004 1/1. The 16-stage coverage manifest was completed without a review queue, count cap, top-N boundary, or early stopping. The coverage plan and source-unit accounting are available in [coverage_manifest.md](<review_1_5_2/coverage_manifest.md>) and [source_coverage.md](<review_1_5_2/source_coverage.md>).

This is a quantitative consistency review. It addresses printed numeric, denominator, proportion, total, effect-measure, label, scale, inferential-statistical, and cross-document relationships. It does not perform a broad clinical, methodological, raw-data, misconduct, novelty, or external-literature audit. The supplied documents do not provide participant-level data, complete unrounded model output, all test variants, or all externally referenced SAP/update text.

## Quantitative and Statistical Relationship Coverage

The completed numeric inventory contains N001-N073 (73/73): 40 main-article and 33 support-source relationships. The inferential inventory contains S001-S032 (32/32): 10 main-article and 22 support-source relationships. The numeric and cross-source lanes processed all 73 numeric and all 32 statistical relationships.

Statistical pass 1 was an independent fresh `gpt-5.6-terra` high-effort review of S001-S032. It registered six source-grounded observations subsequently represented in C002-C007. Statistical pass 2 was a distinct fresh `gpt-5.6-terra` high-effort review of S001-S032 after complete ledger registration and mechanical recheck; it covered all eight IDs, found no genuinely new candidate, and did not alter the stable set. Both passes treated count-based RR/CI/P comparisons as diagnostic where exact test/model details were unavailable, not as reconstructions or corrections.

The definitive relationship records are [numeric_relationship_inventory.md](<review_1_5_2/relationships/numeric_relationship_inventory.md>), [relationship_inventory.md](<review_1_5_2/statistics/relationship_inventory.md>), [statistical_pass_1.md](<review_1_5_2/checkers/statistical_pass_1.md>), and [statistical_pass_2.md](<review_1_5_2/checkers/statistical_pass_2.md>).

## Candidate Index

| ID | Primary category | Concise candidate statement | Source pages |
|---|---|---|---|
| [C001](#c001--normothermia-injury-severity-score-median-is-below-its-printed-iqr-lower-endpoint) | Numeric or arithmetic inconsistency | Median is below printed IQR lower endpoint. | DOC-001 p. 5 |
| [C002](#c002--primary-risk-difference-has-opposite-signs-in-matched-main-article-locations) | Cross-document numeric inconsistency | Primary risk difference sign differs across matched locations. | DOC-001 pp. 1, 5, 7 |
| [C003](#c003--intracranial-bleeding-effect-and-p-value-reporting-conflicts-with-matched-evidence) | Statistical reporting inconsistency | Intracranial-bleeding effect/P display conflicts with matched evidence. | DOC-001 p. 7; DOC-003 p. 10 |
| [C004](#c004--extracranial-bleeding-effect-and-p-value-reporting-conflicts-with-matched-evidence) | Statistical reporting inconsistency | Extracranial-bleeding effect/P display conflicts with matched evidence. | DOC-001 p. 7; DOC-003 p. 10 |
| [C005](#c005--as-treated-evacuated-mass-lesion-cell-reverses-count-and-percentage-order) | Measure, label, or scale inconsistency | CT cell conflicts with its `No. (%)` header order. | DOC-003 p. 18 |
| [C006](#c006--as-treated-non-evacuated-mass-lesion-cell-reverses-count-and-percentage-order) | Measure, label, or scale inconsistency | CT cell conflicts with its denominator and `No. (%)` header. | DOC-003 p. 18 |
| [C007](#c007--adjusted-odds-ratio-confidence-interval-string-is-malformed) | Statistical reporting inconsistency | Adjusted OR confidence-interval string has no unambiguous two endpoints. | DOC-003 p. 22 |
| [C008](#c008--abstract-male-count-conflicts-with-its-percentage-and-table-1-total) | Denominator, proportion, or total inconsistency | Abstract male count conflicts with its percentage and Table 1 total. | DOC-001 pp. 1, 5 |

## Candidate Evidence Cards

## C001 — Normothermia Injury Severity Score median is below its printed IQR lower endpoint

**Candidate statement:** The normothermia Injury Severity Score median is lower than the lower endpoint of its printed IQR.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 5, Table 1, normothermia Injury Severity Score](<../jama_cooper_2018_oi_180132.pdf#page=5>).

**Source evidence:** The `median (IQR)` cell prints `20.0 (20.5-35.0)` for normothermia.

**Reported-versus-comparator:** Reported median `20.0`; comparator IQR lower endpoint `20.5` under the same explicit `median (IQR)` label.

**Reasoning procedure:** Apply the ordered summary relationship for a median and 25th-75th percentile IQR: lower quartile <= median <= upper quartile. The ordering violation is direct; a digit error or nonstandard convention would be an inferred explanation.

**Calculation:** `20.5 - 20.0 = 0.5` Injury Severity Score points; the labelled lower endpoint exceeds the labelled median.

**Alternative source-grounded interpretations:** An unstated convention could theoretically alter the reading, but the cell label, parentheses, and parallel hypothermia median/IQR layout support the ordinary interpretation. No alternative definition is printed.

**Mechanical evidence recheck:** The cited cell and row label were found in fresh native, layout, and rendered locators; all three displayed values required for the ordering check are present. Participant-level values and the quantile algorithm are absent, so intended replacements cannot be reconstructed.

**Quality-control relevance:** A baseline summary with internally incompatible order could be copied as a quantitative characteristic without the internal check.

**Potential downstream evidence impact:** If confirmed, a later extractor could copy an incompatible baseline median/IQR summary; this report does not assert that such copying occurred or altered any conclusion.

**Human verification steps:** Verify the source table against the production table or underlying baseline-summary output; establish the intended median and both IQR endpoints.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Primary risk difference has opposite signs in matched main-article locations

**Candidate statement:** The abstract prints a positive primary risk difference while matched Results and Table 2 locations print a negative risk difference with the same displayed counts and CI.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 1, abstract Results](<../jama_cooper_2018_oi_180132.pdf#page=1>); [PDF p. 5, Primary Outcome Results](<../jama_cooper_2018_oi_180132.pdf#page=5>); [PDF p. 7, Table 2 favorable outcome](<../jama_cooper_2018_oi_180132.pdf#page=7>).

**Source evidence:** All locations report hypothermia `117/240 (48.8%)`, normothermia `111/226 (49.1%)`, and CI `-9.4 to 8.7`. The abstract prints risk difference `0.4%`; Results and Table 2 print `-0.4` percentage points.

**Reported-versus-comparator:** Reported abstract point estimate `+0.4%`; matched comparator Results/Table 2 point estimate `-0.4`, with the same group order and CI.

**Reasoning procedure:** Directly compare the matched printed locations, then use the displayed arm order for a diagnostic subtraction. The cross-location sign mismatch is direct; a missing minus sign or differently defined contrast is not assumed.

**Calculation:** `(117/240 - 111/226) x 100 = -0.3650` percentage points, rounding to `-0.4`.

**Alternative source-grounded interpretations:** A reversed abstract contrast could produce approximately `+0.4`, but a correspondingly reversed CI would ordinarily be `-8.7 to 9.4`; the unchanged printed abstract CI does not fully reconcile that reading.

**Mechanical evidence recheck:** All three locations, counts, signs, and common CI were located. The abstract supplies no distinct contrast definition or unrounded analysis output.

**Quality-control relevance:** Effect-direction labels should remain consistent across an abstract, narrative, and outcome table.

**Potential downstream evidence impact:** If confirmed, an abstract-level reviewer or extractor could copy the positive sign rather than the matched negative sign; no propagation or conclusion change is asserted.

**Human verification steps:** Compare the abstract proof and analysis output with the body/table; confirm the contrast direction and its CI endpoints for each location.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Intracranial-bleeding effect and P-value reporting conflicts with matched evidence

**Candidate statement:** The intracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 7, Table 2, new or increased intracranial bleeding](<../jama_cooper_2018_oi_180132.pdf#page=7>); [joi180132supp2_prod.pdf — PDF p. 10, eTable 6, same outcome](<../joi180132supp2_prod.pdf#page=10>); [jama_cooper_2018_oi_180132.pdf — PDF p. 3, Statistical Analysis](<../jama_cooper_2018_oi_180132.pdf#page=3>).

**Source evidence:** Both result locations print `47/260 (18.1%)` versus `37/240 (15.4%)`. Table 2 prints RR `1.23 (0.43-3.5), P=.70`; eTable 6 prints `P=.43`.

**Reported-versus-comparator:** Reported Table 2 RR `1.23` and `P=.70`; comparator printed-proportion RR is approximately `1.17`, and the matched eTable P is `.43`.

**Reasoning procedure:** Directly compare P values for the same named row/population, and compute a crude RR from displayed counts only as a diagnostic compatibility check under the article's stated unadjusted comparison rule. A suspected adjacent-row token transposition is an inference, not a correction.

**Calculation:** `(47/260)/(37/240) = 1.1726`, rounding to `1.17`, not `1.23`. A diagnostic log-scale CI is approximately `0.79-1.74` and an uncorrected two-proportion comparison approximately `P=.43`; these diagnostics do not replace the reported analysis.

**Alternative source-grounded interpretations:** A differently modelled effect is conceivable, but Table 2 is labelled `Relative Risk` and no row-specific adjusted analysis is identified. The neighboring row is a possible source-grounded token-assignment hypothesis only.

**Mechanical evidence recheck:** The matched counts, Table 2 RR/CI/P, eTable P, and stated analysis rule were found. Exact SAS options, unrounded statistics, and production source are absent.

**Quality-control relevance:** Row-specific effect, interval, and P-value attachment must remain consistent with the named adverse-event outcome.

**Potential downstream evidence impact:** If confirmed, a later evidence extractor could assign the wrong RR, CI, or P value to intracranial bleeding; no downstream use or conclusion change is asserted.

**Human verification steps:** Retrieve the Table 2/eTable production source and unadjusted adverse-event output; verify which RR, CI, and P value belongs to this row.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Extracranial-bleeding effect and P-value reporting conflicts with matched evidence

**Candidate statement:** The extracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 7, Table 2, new significant extracranial bleeding](<../jama_cooper_2018_oi_180132.pdf#page=7>); [joi180132supp2_prod.pdf — PDF p. 10, eTable 6, same outcome](<../joi180132supp2_prod.pdf#page=10>); [jama_cooper_2018_oi_180132.pdf — PDF p. 3, Statistical Analysis](<../jama_cooper_2018_oi_180132.pdf#page=3>).

**Source evidence:** Both result locations print `8/260 (3.1%)` versus `6/240 (2.5%)`. Table 2 prints RR `1.17 (0.79-1.74), P=.43`; eTable 6 prints `P=.70`.

**Reported-versus-comparator:** Reported Table 2 RR `1.17` and `P=.43`; comparator printed-proportion RR is approximately `1.23`, and the matched eTable P is `.70`.

**Reasoning procedure:** Directly compare P values for the same named row/population and use displayed counts for a diagnostic crude-RR compatibility check. A suspected adjacent-row token transposition is not asserted as a correction.

**Calculation:** `(8/260)/(6/240) = 1.2308`, rounding to `1.23`, not `1.17`. A diagnostic log-scale CI is approximately `0.43-3.50` and an uncorrected two-proportion comparison approximately `P=.70`; these diagnostics do not reconstruct the reported analysis.

**Alternative source-grounded interpretations:** A differently modelled effect is possible in theory, but no row-specific adjusted analysis is supplied. The adjacent intracranial row mathematically aligns with the printed `1.17 (0.79-1.74), P=.43`, which is a hypothesis about token assignment, not an established explanation.

**Mechanical evidence recheck:** The named locations, counts, RR/CI/P, matched eTable P, and stated chi-square rule were found. Exact test settings and production source remain unavailable.

**Quality-control relevance:** Effect and P-value fields must stay attached to the correct adverse-event row.

**Potential downstream evidence impact:** If confirmed, a reviewer or extractor could associate an incorrect RR, CI, or P value with extracranial bleeding; this report does not claim that happened.

**Human verification steps:** Check original table/eTable production data and adverse-event output; verify the row-specific RR, CI, and P value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — As-treated evacuated-mass-lesion cell reverses count and percentage order

**Candidate statement:** An as-treated normothermia CT cell is inconsistent with its `No. (%)` header and displayed denominator.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, evacuated mass lesion V, normothermia](<../joi180132supp2_prod.pdf#page=18>).

**Source evidence:** Under `No. (%)`, normothermia `(n=196)` prints `34.7 (68)`; surrounding cells use count followed by percentage.

**Reported-versus-comparator:** Reported token order `34.7 (68)` versus the count-first header and denominator relationship represented by `68/196`.

**Reasoning procedure:** Test whether the first token can be a count and whether the parenthesized token is a percentage under the explicit header. The apparent token reversal is diagnostic only, not a final correction.

**Calculation:** `68/196 x 100 = 34.6939%`, rounding to `34.7%`; `34.7` is noninteger in the count position. With the adjacent reconciled category reading, the five CT counts can close at `3 + 108 + 15 + 68 + 2 = 196`.

**Alternative source-grounded interpretations:** A percentage-first convention would reconcile this one cell, but conflicts with `No. (%)` and surrounding count-first cells; no row-specific exception is printed.

**Mechanical evidence recheck:** The header, denominator, cell tokens, parallel convention, and CT-category cells were found. Record-level CT classifications and production source are absent.

**Quality-control relevance:** Headers and count/percentage token order should permit unambiguous mechanical extraction.

**Potential downstream evidence impact:** If confirmed, an extractor could copy `34.7` as a count and `68%` as a percentage rather than preserve the intended order; no actual downstream extraction is asserted.

**Human verification steps:** Inspect the eTable source data or table proof and confirm the intended count and percentage for this category.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — As-treated non-evacuated-mass-lesion cell reverses count and percentage order

**Candidate statement:** An as-treated normothermia CT cell does not reconcile with its `No. (%)` header, printed denominator, or displayed category total.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, non-evacuated mass lesion VI, normothermia](<../joi180132supp2_prod.pdf#page=18>).

**Source evidence:** Under `No. (%)`, normothermia `(n=196)` prints `1 (2)`; other CT rows print `3 (1.5)`, `108 (55.1)`, `15 (7.7)`, and the adjacent cell `34.7 (68)`.

**Reported-versus-comparator:** Reported literal count/percentage `1 (2)` versus `1/196` and the count-total relationship across the five displayed categories.

**Reasoning procedure:** Test the literal count-first interpretation against the stated denominator and total, then identify the order that diagnostic arithmetic would reconcile. That possible reversal is not a correction.

**Calculation:** `1/196 x 100 = 0.5102%`, not `2%`. Reading count `2` and percentage `1` gives `2/196 x 100 = 1.0204%`, and `3 + 108 + 15 + 68 + 2 = 196`; literal count `1` produces 195.

**Alternative source-grounded interpretations:** A row-specific denominator of 50 could make `1 (2)` arithmetically possible, but the table prints `n=196`, no row-specific denominator/missingness note, and five exhaustive categories.

**Mechanical evidence recheck:** The header, group denominator, all displayed CT tokens, and category-total comparison were found. Participant-level classifications, a possible row denominator, and production source are not supplied.

**Quality-control relevance:** Count/percentage fields should reconcile to their labelled denominator and permit correct category totals.

**Potential downstream evidence impact:** If confirmed, a later extractor could copy `1` as the count and `2%` as the percentage for this category; no propagation is claimed.

**Human verification steps:** Verify the table proof and underlying CT category counts, including any row-specific denominator or missingness convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Adjusted odds-ratio confidence-interval string is malformed

**Candidate statement:** The printed adjusted odds-ratio confidence-interval string does not provide two unambiguous endpoints.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 22, post-hoc adequate-cooling Results, final sentence](<../joi180132supp2_prod.pdf#page=22>).

**Source evidence:** The source prints `adjusted odds ratio hypothermia vs normothermia; 0.95 (0.55-275 1.64) P = .84`.

**Reported-versus-comparator:** Reported parenthesized sequence `0.55-275 1.64` versus the same page's explicit odds-ratio `(95% CI)` convention requiring two identifiable endpoints; the unadjusted example is `0.91 (0.59-1.41) P=.68`.

**Reasoning procedure:** Parse the literal printed sequence rather than delete or replace a token. Three numeric tokens with no source-defined delimiter cannot be assigned as exactly two CI endpoints. The plausible `0.55-1.64` reading is diagnostic and conjectural.

**Calculation:** The ordered sequence is `0.55`, `275`, `1.64`. Although point estimate `0.95` lies between `0.55` and `1.64`, no source-based calculation identifies the role of `275` or licenses removal of it.

**Alternative source-grounded interpretations:** The same-page syntax supports a possible `0.55-1.64` interval with an extraneous token, but the PDF does not define `275`; punctuation or digits may instead be missing.

**Mechanical evidence recheck:** Native text, layout text, and rendered page preserve the exact malformed string. Coefficient, SE/covariance, fitted model output, and a definition of `275` are unavailable.

**Quality-control relevance:** An interval must be printable as two unambiguous endpoints before it can be reliably extracted or interpreted.

**Potential downstream evidence impact:** If confirmed, a reviewer could face an ambiguous adjusted CI when extracting the post-hoc result; this report neither supplies a final interval nor claims later use.

**Human verification steps:** Obtain the adjusted-model output and final table/text proof; determine the exact two CI endpoints and the source of `275`.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Abstract male count conflicts with its percentage and Table 1 total

**Candidate statement:** The abstract's male count conflicts with both its stated percentage and the Table 1 arm total.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 1, abstract Results](<../jama_cooper_2018_oi_180132.pdf#page=1>); [PDF p. 5, Table 1, Men and Women rows](<../jama_cooper_2018_oi_180132.pdf#page=5>).

**Source evidence:** The abstract states `500 provided ongoing consent` and `402 men [80.2%]`. Table 1 gives hypothermia `207 (79.6)` and normothermia `194 (80.8)` men, and women `53 (20.4)` and `46 (19.2)`.

**Reported-versus-comparator:** Reported abstract `402/500 (80.2%)` versus the arithmetic percentage `80.4%` and Table 1 male subtotal `207+194=401`, which is `80.2%` of 500.

**Reasoning procedure:** Reconcile the abstract count and percentage to its stated total, then sum the matched Table 1 sex counts. A typographical count or unreported alternative denominator remains an explanation, not a correction.

**Calculation:** `402/500 x 100 = 80.4%`. `207 + 194 = 401`; `401/500 x 100 = 80.2%`; sex-category totals close as `401 + 53 + 46 = 500`.

**Alternative source-grounded interpretations:** A denominator near 501 could approximate `402` at `80.2%`, but the abstract anchors the text to 500 and Table 1 reports all 500 without a missingness note.

**Mechanical evidence recheck:** The abstract denominator/count/percentage and both Table 1 arm counts/denominators were located. Participant-level sex data, an alternative denominator, and intended abstract count are unavailable.

**Quality-control relevance:** Cohort-characteristic counts and percentages should reconcile across an abstract and baseline table.

**Potential downstream evidence impact:** If confirmed, an abstract-only extractor could copy an inconsistent male count/percentage; no actual reuse or study-level conclusion change is asserted.

**Human verification steps:** Check the abstract source, baseline dataset, and Table 1 production output; establish the intended male count and any distinct sex-analysis denominator.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If any candidate is confirmed, a systematic review, meta-analysis, guideline evidence table, or other data-extraction workflow could copy the relevant baseline summary, signed risk difference, adverse-event RR/CI/P field, CT count/percentage, or adjusted CI string. The possible downstream effect is bounded to the particular reported field and depends on later extraction choices. This review makes no claim that a downstream product used any candidate value, that evidence propagation occurred, or that any conclusion changed.

## Limitations and Missing Definitions

Only supplied-package evidence was used. The direct PDFs lack participant-level observations, unrounded summaries, complete model coefficients/SEs/covariances, exact variants of several tests, sequential information fractions, imputed records/strata, and embedded text for some cited SAP/update/correction materials. Those limitations preclude reconstruction of intended replacements and unsupported exact inference, while still permitting the direct printed-value comparisons in the cards.

Native PDF text can flatten tables or reading order. This was mitigated by freshly generated layout text and 150-dpi page renders for every source page. DOC-002 contains blank/non-substantive pages 140-162 and separator pages; these were nevertheless extracted, rendered, and counted. No Office, workbook, CSV, web, or external-literature source was in scope. See [limitations.md](<review_1_5_2/limitations.md>).

## Human Adjudication Checklist

- Confirm each cited PDF location against the publication record or production source.
- Obtain the relevant analysis output or source table when an intended replacement cannot be established from the supplied PDFs.
- Preserve the printed evidence and distinguish direct source comparisons from diagnostic arithmetic.
- Record any human determination only in the blank card fields; do not infer a correction from this review alone.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Profile:** 1.5.2 full source-first restart
- **Direct sources:** 4 PDFs
- **Total source units:** 229
- **Fresh-source units:** 229
- **Legacy audit evidence used:** No
- **Web or external literature used:** No
- **OCR decision:** 0 pages; native/layout text and renders were usable for every result-relevant unit.
- **Source hashes before review:** [source_hashes_before.sha256](<review_1_5_2/source_hashes_before.sha256>)
- **Source hashes after review:** [source_hashes_after.sha256](<review_1_5_2/source_hashes_after.sha256>); all four hashes are unchanged.
- **Coverage manifest:** 16 rows, all planned scopes covered; see [coverage_manifest.md](<review_1_5_2/coverage_manifest.md>).

### Agent execution

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | [run_state.md](<review_1_5_2/run_state.md>) |
| fresh source preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | [evidence_asset_inventory.md](<review_1_5_2/evidence_asset_inventory.md>) |
| main quantitative mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | [main_quantitative_evidence.md](<review_1_5_2/extraction/main_quantitative_evidence.md>) |
| support quantitative mapping | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | [support_quantitative_evidence.md](<review_1_5_2/extraction/support_quantitative_evidence.md>) |
| numeric consistency review | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | [numeric_consistency.md](<review_1_5_2/checkers/numeric_consistency.md>) |
| cross-source consistency review | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | [cross_source_consistency.md](<review_1_5_2/checkers/cross_source_consistency.md>) |
| statistical pass 1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | [statistical_pass_1.md](<review_1_5_2/checkers/statistical_pass_1.md>) |
| evidence recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) |
| statistical pass 2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | [statistical_pass_2.md](<review_1_5_2/checkers/statistical_pass_2.md>) |
| evidence-quality audit | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | [evidence_quality_audit.md](<review_1_5_2/quality/evidence_quality_audit.md>) |
| report generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | [report_generation.md](<review_1_5_2/report_generation.md>) |

The execution manifest is [agent_execution_manifest.md](<review_1_5_2/agent_execution_manifest.md>). Statistical pass 1 and pass 2 were separate fresh high-effort Terra agents and each covered S001-S032; pass 2 additionally integrated C001-C008 and the complete mechanical recheck.

### Performance

- **Target basis:** Four-PDF package with 229 fresh PDF-page units, including a 194-page protocol/SAP supplement, a 24-page statistical supplement, a 10-page main article, and a 1-page data-sharing supplement; all units require fresh native/layout extraction and result-relevant mapping, with two full statistical passes and cross-document review. The burden is materially above the 102-page calibration package, but most pages had usable native text and no Office conversion burden.
- **Total source units:** 229
- **Fresh-source units:** 229
- **Target elapsed minutes:** 70-105
- **Started UTC:** 2026-08-20T18:01:56Z
- **Finished UTC:** 2026-08-20T18:35:06Z
- **Observed elapsed minutes:** 33.2
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and token-only API-equivalent cost estimate

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agent responses | Input tokens | Output tokens | Total tokens | Token-only API-equivalent cost (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 unavailable | 0 | 0 | 0 | 0.000000 known; complete estimate __ |
| gpt-5.6-terra | 8 unavailable | 0 | 0 | 0 | 0.000000 known; complete estimate __ |

The exact model rollups come from [token_usage_summary.md](<review_1_5_2/token_usage_summary.md>) after the accounting-window cutoff. All 11 manifested agents have an authoritative `UNAVAILABLE` record because this runtime exposed no response-level token counts; zero therefore means zero known tokens, not zero actual usage. The per-agent detail is recorded in `review_1_5_2/token_usage_ledger.csv`. Cached input and cache-write counts are input subsets; reasoning is an output subset; they are not added again to total tokens. Amounts are token-only API-equivalent estimates under the dated 2026-08-18 pricing snapshot, not an invoice.
