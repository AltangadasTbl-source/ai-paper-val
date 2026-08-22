# Quantitative Quality-Control Consistency Review — jama.2020.8556

## Pending Human Adjudication

**All eight candidate consistency issues in this report are Pending Human Adjudication.** They are quantitative reporting quality-control observations, not final corrections or conclusions about the paper.

## Executive Quality-Control Summary

Complete source coverage and two independent statistical passes identified eight stable quantitative reporting-consistency candidates: C001 through C008. The review considered numeric arithmetic, denominators, proportions, cross-document agreement, labels, rates, and source-supported inferential compatibility. The candidates are limited to printed values and stated rules; they do not establish that the paper's conclusion is wrong. Small preventable reporting defects can matter if a downstream evidence product copies an affected value, but this report does not assert propagation, conclusion change, or serious harm.

## Package and Reused-Evidence Provenance

The supplied package contains four immutable PDFs: the 10-page main article, a 76-page protocol/SAP support PDF, a 13-page results supplement, and a one-page data-sharing support PDF. The direct-source and reused-asset inventories, with before-review hashes, are recorded in [source inventory](<review_1_5_1/source_inventory.md>) and [reused-evidence inventory](<review_1_5_1/evidence_asset_inventory.md>). Existing native text covered the 10 main-article pages and 13 results-supplement pages; existing renders supported visual confirmation where available. Those derivatives were used as locators and transcription aids, while candidate facts were rechecked against the cited supplied PDF pages.

## Scope, Complete Coverage, and Exclusions

All 100 of 100 direct-source PDF-page units were mapped: 23 reusable-backed units and 77 fresh-required units. Each source row is complete in the [source coverage ledger](<review_1_5_1/source_coverage.md>): DOC-001, 10/10; DOC-002, 76/76; DOC-003, 13/13; and DOC-004, 1/1.

The review did not perform a broad clinical, design, misconduct, raw-data, or external-literature audit. No coherent display-zero P value was registered as a candidate; the package contains no `P = 0` or equivalent display-zero notation. Inequality displays such as `P < .001` were not treated as display zeros.

## Quantitative and Statistical Relationship Coverage

The complete relationship inventories contain 71 numeric/reporting relationships (`N001`–`N071`) and 93 inferential-statistical relationships (`S001`–`S093`). Numeric and cross-source checks covered their applicable mapped relationships. Statistical pass 1 and the independent, fresh statistical pass 2 each completed all 93 S relationships. Pass 2 reviewed all eight stable candidates for statistical implications and added no candidate. Definition-limited relationships were retained as coverage records without inferring missing model, denominator, reference, confidence-interval, or test details.

## Candidate Index

| Stable ID | Candidate statement | Category |
|---|---|---|
| C001 | Person-day totals do not reconcile with stated mean follow-up days | Denominator, proportion, or total inconsistency |
| C002 | Administration-method percentage conflicts with its printed fraction | Denominator, proportion, or total inconsistency |
| C003 | Adherence median is below its IQR and conflicts across main and supplement | Cross-document numeric inconsistency |
| C004 | Nonprophylactic-antibiotic percentages conflict with printed counts and denominators | Denominator, proportion, or total inconsistency |
| C005 | Three-month oral-candidiasis ARD conflicts with printed proportions and supplement | Cross-document numeric inconsistency |
| C006 | Matched *B animalis* interval has two different lower endpoints | Cross-document numeric inconsistency |
| C007 | eTable 4 percentage does not reproduce from 20/119 | Denominator, proportion, or total inconsistency |
| C008 | CACE coefficient, confidence interval, and P value need reconciliation | Statistical reporting inconsistency |

## Candidate Evidence Cards

## C001 — Person-day totals do not reconcile with stated mean follow-up days

**Candidate statement:** The printed arm person-day totals do not reproduce the printed mean days per participant under either displayed arm denominator set.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../jama_butler_2020_oi_200054.pdf#page=4>), participant-flow and follow-up narrative.

**Source evidence:** The page prints 39,798 probiotic person-days and mean 252.4 days, and 37,974 placebo person-days and mean 242.9 days. It also prints 155 randomized per arm and 152 probiotic versus 153 placebo participants in the primary analysis.

**Reported-versus-comparator:** Reported means are 252.4 and 242.9 days. Comparators obtained from the printed totals are 39,798/155, 37,974/155, 39,798/152, and 37,974/153 days.

**Reasoning procedure:** Total person-days divided by participant count should reproduce a mean only if the stated total and mean use the same participant set and day definition. Both printed denominator sets were checked; no unreported denominator was assumed.

**Calculation:** 39,798/155 = 256.7613; 37,974/155 = 244.9935; 39,798/152 = 261.8289; and 37,974/153 = 248.1961. Conversely, 39,798/252.4 = 157.6783 and 37,974/242.9 = 156.3359 participants, each above 155. Printed one-decimal rounding cannot bridge these differences.

**Alternative source-grounded interpretations:** The page discusses observed and unobserved days, including death and other missing-day causes. The totals and means may use different, unstated participant sets, day-inclusion rules, or weighting conventions.

**Mechanical evidence recheck:** The cited page and all stated values were visually confirmed. The recheck reproduced each calculation and records that the exact participant set, day inclusion, missing-day handling, weighting rule, and unrounded means are not supplied.

**Quality-control relevance:** A total, a mean, and their population label should be internally interpretable together. The source does not identify which definition governs the mismatch.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a person-time total, mean follow-up, or exposure denominator that is not comparable with the other printed quantity. This report does not assert that this has occurred or that it changes a conclusion.

**Human verification steps:** Obtain the arm-specific analytic participant sets, day-record inclusion and weighting rules, and unrounded means; then determine whether each printed total and mean is intended to describe the same population.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Administration-method percentage conflicts with its printed fraction

**Candidate statement:** The administration-method percentage 89.4% does not reproduce from its attached printed fraction 68,356/73,302.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../jama_butler_2020_oi_200054.pdf#page=4>), Intervention Fidelity paragraph.

**Source evidence:** The paragraph prints 89.4% (68,356/73,302) swallowed as capsules or sprinkled on food, 4.4% (3,258/73,302) in liquid, and 2.3% (1,688/73,302) unknown method.

**Reported-versus-comparator:** Reported 89.4% is compared with 93.3%, the one-decimal result of the printed fraction.

**Reasoning procedure:** A percentage explicitly attached to a numerator and denominator is checked as numerator/denominator × 100, at the printed precision. The route counts also test whether the stated denominator partitions the displayed routes.

**Calculation:** 68,356/73,302 × 100 = 93.2526%, which rounds to 93.3%, not 89.4%. The three route counts sum to 73,302. The other fractions give 4.4446% and 2.3028%, reproducing 4.4% and 2.3%; the three printed percentages sum to 96.1%.

**Alternative source-grounded interpretations:** The percentage may have used another eligible-dose denominator, but that denominator and its route-population definition are not supplied and the sentence explicitly pairs 89.4% with 68,356/73,302.

**Mechanical evidence recheck:** The source values and both comparator route fractions were visually confirmed; the fraction calculation and route-count sum were reproduced directly.

**Quality-control relevance:** The printed fraction identity is directly checkable and needs no model assumption. The intended percentage, numerator, or denominator remains unresolved.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy an inconsistent administration-route percentage or fraction. This does not establish propagation or a change in the study conclusion.

**Human verification steps:** Check the dose-level adherence tabulation and determine whether 89.4%, 68,356, or 73,302 is intended, including any separate eligible-dose denominator.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Adherence median is below its IQR and conflicts across main and supplement

**Candidate statement:** The main article's printed median adherence is below its lower IQR endpoint, and the main and supplement print different medians with the same IQR.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../jama_butler_2020_oi_200054.pdf#page=4>), Intervention Fidelity paragraph; [joi200054supp2_prod.pdf — PDF p. 5](<../joi200054supp2_prod.pdf#page=5>), text above eTable 2.

**Source evidence:** The main article prints median 93.3%, IQR 93.56%–99.45%, for 302 initiators. The supplement prints median 97.8%, IQR 93.56%–99.45%, beside eTable 2.

**Reported-versus-comparator:** The reported main median 93.3% is compared with its lower quartile 93.56%; the reported main median is also compared with the supplement's 97.8% median under identical printed IQR endpoints.

**Reasoning procedure:** Within one summary, a conventional median cannot fall below its lower quartile. Cross-location equality is assessed separately and remains definition-limited because the supplement does not name its descriptive-adherence population.

**Calculation:** 93.56% − 93.3% = 0.26 percentage points, placing the main median below its lower IQR endpoint. The supplement-minus-main median difference is 97.8% − 93.3% = 4.5 percentage points. The displayed precisions cannot make a one-decimal 93.3% median reach a two-decimal 93.56% lower quartile under ordinary rounding.

**Alternative source-grounded interpretations:** The main source names 302 initiators, while nearby supplement context gives CACE N=305. Different populations, adherence-record rules, or quantile derivations could explain the cross-source difference, but not by themselves the within-main ordering.

**Mechanical evidence recheck:** Both pages and all printed median/IQR values were visually confirmed. The recheck separates the independently sufficient within-main order check from the definition-limited cross-source comparison and records missing population, inclusion-rule, and quantile-algorithm details.

**Quality-control relevance:** A median/IQR summary needs coherent order and a cross-document repeated summary needs a clear population definition.

**Potential downstream evidence impact:** If confirmed, downstream extraction could copy a pooled adherence median or use it as CACE context. This report does not infer an effect on CACE results or the paper conclusion.

**Human verification steps:** Verify the intended median, adherence population, record-inclusion rule, and quantile method; determine whether the main 93.3% is meant to describe a different quantity.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Nonprophylactic-antibiotic percentages conflict with printed counts and denominators

**Candidate statement:** The printed overall and arm-specific antibiotic-use percentages do not reproduce from their printed counts and denominators.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 5](<../jama_butler_2020_oi_200054.pdf#page=5>), antibiotic-use paragraph; [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../jama_butler_2020_oi_200054.pdf#page=4>), randomized and primary-analysis denominator context.

**Source evidence:** Page 5 prints overall 202 (66.2%), probiotic 63.4% (97/155), and placebo 69.1% (105/155); 97 + 105 = 202. Page 4 prints 152 and 153 in the primary analysis and 305 overall.

**Reported-versus-comparator:** The reported 63.4%, 69.1%, and 66.2% are compared with the results from 97/155, 105/155, and 202/310 respectively.

**Reasoning procedure:** Percentages attached to explicit fractions are checked at one-decimal precision. Alternative 152/153 and 305 denominators are diagnostic context only because the source does not identify them as the antibiotic-use denominators.

**Calculation:** 97/155 = 62.5806%, 105/155 = 67.7419%, and 202/310 = 65.1613%, which round to 62.6%, 67.7%, and 65.2%. The displayed percentages approximately reproduce 97/153 = 63.3987%, 105/152 = 69.0789%, and 202/305 = 66.2295%.

**Alternative source-grounded interpretations:** Outcome-data denominators could underlie the percentages, but they are not the printed fraction denominators and the source does not state an outcome-specific denominator rule.

**Mechanical evidence recheck:** The two source pages, all counts, percentages, and denominator context were visually confirmed; calculations for the printed and alternate denominators were reproduced.

**Quality-control relevance:** The explicit `/155` labels and overall count need an identifiable denominator basis. The evidence does not establish which values should be changed.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract an inconsistent descriptive antibiotic-exposure percentage, count, or denominator. No propagation or conclusion change is claimed.

**Human verification steps:** Identify the analysis denominator for each percentage and determine whether the fractions or percentages require correction or relabeling.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Three-month oral-candidiasis ARD conflicts with printed proportions and supplement

**Candidate statement:** The main three-month oral-candidiasis ARD does not reconcile with the printed raw fractions, while the matched supplement prints a different, proportion-scale difference.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 7](<../jama_butler_2020_oi_200054.pdf#page=7>), Table 3; [joi200054supp2_prod.pdf — PDF p. 8](<../joi200054supp2_prod.pdf#page=8>), eTable 5.

**Source evidence:** The main article prints 88/113 (77.9%) versus 80/105 (76.2%) and ARD −0.2% (−11.3% to 10.9%). The supplement repeats the fractions and prints difference 0.02 (−0.10 to 0.13).

**Reported-versus-comparator:** The main ARD −0.2% is compared with the two possible raw proportion differences, +1.6856 and −1.6856 percentage points; the supplement's 0.02 is compared on its printed proportion scale.

**Reasoning procedure:** Raw fractions were calculated in both arm orders without assuming the main ARD's unreported reference or estimator. The matched supplement provides a separate displayed comparator.

**Calculation:** 88/113 = 77.8761% and 80/105 = 76.1905%. Probiotic minus placebo is +1.6856 percentage points; reverse order is −1.6856. Neither rounds to −0.2%; +0.02 as a proportion is compatible with the raw fractions. The main interval is internally centred on −0.2%, but its relation to the fractions remains unresolved.

**Alternative source-grounded interpretations:** The main ARD might be adjusted or model-derived, but neither cited location labels it adjusted or defines a different estimator, population, direction, or variance method.

**Mechanical evidence recheck:** Both source pages and their fractions, differences, and intervals were visually confirmed. The recheck reproduced both raw directions and retained the adjusted-estimator possibility as unresolved rather than assumed.

**Quality-control relevance:** A difference estimate should have an identifiable scale, direction, estimator, and relation to the reported proportions.

**Potential downstream evidence impact:** If confirmed, an evidence synthesis could copy a three-month oral-candidiasis difference estimate or interval that is not aligned with the displayed fractions. This report makes no claim about a microbiology or conclusion change.

**Human verification steps:** Obtain the ARD estimator, reference direction, population, and variance method; reconcile the main −0.2% with the supplement's 0.02 and the raw fractions.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Matched B animalis interval has two different lower endpoints

**Candidate statement:** Matched main-article and supplement results print different two-decimal lower confidence-interval endpoints.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_butler_2020_oi_200054.pdf — PDF p. 5](<../jama_butler_2020_oi_200054.pdf#page=5>); [joi200054supp2_prod.pdf — PDF p. 8](<../joi200054supp2_prod.pdf#page=8>), three-month *B animalis* result.

**Source evidence:** For 29/56 versus 2/52 at three months, the main article prints adjusted OR 26.90 (95% CI 5.94–121.66), while eTable 5 prints 26.9 (95% CI 5.95–121.66).

**Reported-versus-comparator:** Main lower endpoint 5.94 is compared with supplement lower endpoint 5.95; counts, effect measure, point estimate at displayed precision, upper endpoint, and P display match.

**Reasoning procedure:** Matched repeated results should display the same endpoint when they report the same model output at the same two-decimal precision. The package does not establish whether they arose from a version difference.

**Calculation:** 5.95 − 5.94 = 0.01. Both endpoints are printed to two decimals and cannot be identical displayed values.

**Alternative source-grounded interpretations:** Separate document-output versions or unprovided unrounded calculations could explain the discrepancy.

**Mechanical evidence recheck:** Both pages, fractions, effect estimates, interval endpoints, and P displays were visually confirmed; the recheck identified the lower endpoint as the only displayed mismatch for the matched result.

**Quality-control relevance:** A repeated confidence interval should permit a reader to identify a single lower endpoint for the same result.

**Potential downstream evidence impact:** If confirmed, a data extractor may copy one of two lower confidence limits for the matched result. No changed effect direction or conclusion is asserted.

**Human verification steps:** Consult the model output or documented document versions and confirm which lower endpoint is intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — eTable 4 percentage does not reproduce from 20/119

**Candidate statement:** One eTable 4 cell prints 20/119 (16.0), but the fraction rounds to 16.8%; adjacent-category arithmetic corroborates a repeated-cell inconsistency.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi200054supp2_prod.pdf — PDF p. 7](<../joi200054supp2_prod.pdf#page=7>), eTable 4, placebo group at three months, `(+)` category and adjacent category rows.

**Source evidence:** The cited cell prints 20/119 (16.0). The four placebo three-month categories print numerators 20, 20, 38, and 42 against a common printed denominator 119, with displayed percentages 16.8%, 16.0%, 31.9%, and 35.3%.

**Reported-versus-comparator:** Reported 16.0% is compared with 16.8%, calculated from the printed 20/119 fraction.

**Reasoning procedure:** A percentage beside an explicit fraction is checked directly. The adjacent-category check is corroboration for the same cell, not a separate candidate and not a determination of which printed element is intended.

**Calculation:** 20/119 × 100 = 16.8067%, which rounds to 16.8%, not 16.0%. The four numerators sum to 20 + 20 + 38 + 42 = 120 against denominator 119, while the displayed percentages sum to 16.8 + 16.0 + 31.9 + 35.3 = 100.0%.

**Alternative source-grounded interpretations:** A cell-specific unreported denominator, a numerator transcription error, or a percentage transcription error could explain the combination; the supplied table does not distinguish them.

**Mechanical evidence recheck:** The cell and adjacent rows were visually confirmed on the cited source page. The fraction calculation, numerator sum, and percentage sum were reproduced; the underlying category tabulation is unavailable.

**Quality-control relevance:** The directly printed fraction/percentage identity does not reconcile, and the same-cell corroboration supports review without assigning a cause.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy an inconsistent ordinal-candidiasis cell or category distribution. This report does not state that this has occurred or affects a conclusion.

**Human verification steps:** Check the underlying ordinal-category tabulation and determine whether the numerator, denominator, or percentage is intended for the `(+)` cell.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — CACE coefficient, confidence interval, and P value need reconciliation

**Candidate statement:** The displayed CACE point estimate is not centred in its confidence interval; compatibility with the reported P value requires source definitions that are not supplied.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [joi200054supp2_prod.pdf — PDF p. 3](<../joi200054supp2_prod.pdf#page=3>), CACE model description; [joi200054supp2_prod.pdf — PDF p. 5](<../joi200054supp2_prod.pdf#page=5>), eTable 2; [joi200054supp1_prod.pdf — PDF p. 52](<../joi200054supp1_prod.pdf#page=52>), two-sided 95% SAP convention.

**Source evidence:** The 2SLS CACE model states that coefficient and CI are multiplied by 100 for presentation. eTable 2 prints coefficient 0.01, 95% CI −0.20 to 0.41, P=.52; the SAP states two-sided 95% inference.

**Reported-versus-comparator:** Reported coefficient 0.01 and P=.52 are compared with interval midpoint 0.105 and endpoint distances 0.21 and 0.40 on the displayed coefficient scale.

**Reasoning procedure:** The off-centre interval is directly observed. Any interval/P compatibility assessment is only a conditional diagnostic assuming a common symmetric Wald interval on the displayed linear scale; it does not reconstruct or replace the reported analysis.

**Calculation:** (−0.20 + 0.41)/2 = 0.105, not 0.01. Distances from 0.01 are 0.21 and 0.40, with half-width 0.305. Multiplication by positive 100 preserves symmetry and does not itself explain the shifted midpoint.

**Alternative source-grounded interpretations:** A non-Wald interval, finite-sample method, transformation, different unrounded coefficient, separately constructed P value, or other output linkage could account for the combination. CI construction, test distribution, degrees of freedom, standard error, cluster count, small-sample correction, and common-output status are not supplied.

**Mechanical evidence recheck:** All three PDF locations were visually confirmed. The midpoint and distances were reproduced; the recheck explicitly labels compatibility reasoning conditional and names the missing inferential definitions.

**Quality-control relevance:** A point estimate, confidence interval, scale multiplier, and P value need enough shared construction detail for their displayed relationship to be evaluated.

**Potential downstream evidence impact:** If confirmed, an extractor could copy or interpret a CACE coefficient, interval, or P value without the reconciliation needed to identify the intended output. No claim is made that the model is wrong or that a conclusion changes.

**Human verification steps:** Obtain unrounded CACE output, coefficient scale, standard error, CI construction, test distribution and degrees of freedom, cluster/small-sample treatment, and confirm whether the estimate, CI, and P value share one output.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, a systematic review, meta-analysis, guideline, or other data extractor could copy the affected total, percentage, adherence summary, difference estimate, confidence limit, table cell, or CACE result. This is a bounded quality-control consideration only: the review does not claim that any downstream product has copied an affected value, that the issue propagated, that serious harm occurred, or that the paper's conclusions change.

## Limitations and Missing Definitions

The supplied package has no participant-level dataset, analysis program, workbook, or CSV. All 77 pages without reusable extraction were freshly mapped, so this reuse limitation leaves no scientific-coverage gap. Candidate-specific unresolved definitions include the C001 day/participant and weighting rules; C003 adherence population and quantile method; C004 outcome denominator; C005 ARD estimator and direction; C006 source version or unrounded output; C007 underlying tabulation; and C008 inferential construction and unrounded output. Several absolute-difference results elsewhere lack a common subtraction/reference convention and were not made into candidates solely on an apparent sign change.

## Human Adjudication Checklist

For each stable ID, verify the cited physical source location, reproduce the printed comparison, obtain the listed missing definition or source output where necessary, document the intended value or label, and complete the five human-adjudication fields in that card. Keep any correction decision separate from this quality-control review record.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- Direct-source coverage: 100/100 mapped PDF-page units (23 reusable-backed; 77 fresh-required).
- Relationship coverage: 71 numeric/reporting relationships and 93 statistical relationships.
- Statistical passes: two distinct fresh `gpt-5.6-terra` high-effort passes, each complete for S001–S093.
- Candidate, recheck, and quality-audit stable sets: C001, C002, C003, C004, C005, C006, C007, C008.
- Integrity provenance: before-review SHA-256 inventories are [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>) and [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>). Recomputed [source](<review_1_5_1/source_hashes_after.sha256>) and [reused-artifact](<review_1_5_1/reused_artifact_hashes_after.sha256>) manifests match exactly; supplied sources and reused assets are unchanged.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_record.md |

### Performance

- **Target basis:** Four supplied PDFs contain 100 pages; the package has a 76-page supplement and extensive result tables, while existing reusable extraction appears concentrated in the 10-page main article and 13-page results supplement. This is comparable to the 102-total/81-fresh calibration package, subject to final curator partitioning.
- **Total source units:** 100
- **Fresh-source units:** 77
- **Target elapsed minutes:** 35-50
- **Started UTC:** 2026-08-18T23:21:16Z
- **Finished UTC:** 2026-08-19T00:01:51Z
- **Observed elapsed minutes:** 40.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

The versioned [token-usage summary](<review_1_5_1/token_usage_summary.md>) provides per-agent detail after coordinator finalization. Cached input and cache-write tokens are input subsets, and reasoning tokens are an output subset; none is added again to total tokens. Any amount is a token-only API-equivalent estimate under the dated pricing snapshot, not an invoice.
