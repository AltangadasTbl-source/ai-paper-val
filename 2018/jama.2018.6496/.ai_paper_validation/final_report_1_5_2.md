# Quantitative Quality-Control Consistency Review: JAMA 2018.6496

# 1. Pending Human Adjudication Notice

**Pending Human Adjudication:** This report records source-grounded quantitative reporting quality-control candidates. It does not determine validity, severity, acceptance, exclusion, correction, or clinical consequences. Every candidate below remains Pending Human Adjudication.

# 2. Executive Quality-Control Summary

Complete fresh review of 49 supplied PDF pages identified seven distinct quantitative reporting consistency candidates (`C001`–`C007`). They concern baseline availability denominators, category completeness, a confidence-interval endpoint order, an outcome-endpoint definition, and an interim-analysis-set comparison. No candidate is based solely on a small displayed P value; no coherent display-zero P value was encountered.

These observations are framed for quantitative reporting quality control. If confirmed, small preventable defects can matter when downstream evidence products extract counts, denominators, intervals, definitions, or analysis-set descriptions. This review does not assert that any defect propagated, changed a conclusion, or caused harm.

# 3. Package and Fresh-Processing Provenance

Only the three supplied package-root PDFs were used as scientific evidence. No web or external literature was used, and no prior audit derivative was used as evidence. Fresh page images and CPU OCR were prepared for all units; the PDFs remain authoritative.

| Document | Supplied source | Fresh units | SHA-256 |
|---|---|---:|---|
| DOC001 | [jama_driver_2018_oi_180054.pdf — PDF p. 1](<../jama_driver_2018_oi_180054.pdf#page=1>) | 11 PDF pages | `684db2edf58f16d1d24e8ddb6a463429b027450314c923e06700acdd0167e7d2` |
| DOC002 | [joi180054supp1_prod.pdf — PDF p. 1](<../joi180054supp1_prod.pdf#page=1>) | 25 PDF pages | `38c1822278c238d2e9f217cd626c307b9d7ad8152f93f3281a03f58990e6108c` |
| DOC003 | [joi180054supp2_prod.pdf — PDF p. 1](<../joi180054supp2_prod.pdf#page=1>) | 13 PDF pages | `b8b7e9731b69407ff10ffc262eb42477965333e3697461e848d8fe50e13b4b31` |

The fresh source inventory and preprocessing record are in `review_1_5_2/source_inventory.md` and `review_1_5_2/evidence_asset_inventory.md`.

# 4. Scope, Complete Coverage, and Exclusions

All 49 direct-source units were freshly prepared, given a result-relevance disposition, and mapped: DOC001 11/11, DOC002 25/25, and DOC003 13/13. The coverage manifest assigns all source, mapping, checking, registration, recheck, quality, and reporting stages without a review queue, top-N subset, or count cap.

The review focused on numeric, denominator/proportion/total, inferential-statistical, cross-document, effect-measure/label/scale, and rate-versus-count consistency. It did not conduct a broad clinical, design, misconduct, novelty, or raw-data audit. Analysis-unit or population issues were considered only where they created a concrete reported-number or interpretation consistency question.

# 5. Quantitative and Statistical Relationship Coverage

The fresh main mapper recorded 35 numeric/reporting relationships and 28 statistical relationships; the fresh support mapper recorded 20 numeric/reporting relationships and 10 statistical relationships. The canonical inventories therefore contain 55 numeric/reporting relationships (`N001`–`N055`) and 38 statistical relationships (`S001`–`S038`).

Numeric and cross-source checks completed their assigned relationships. Independent statistical pass 1 and independent statistical pass 2 each completed all 38 statistical relationships. The second pass reviewed the complete cross-lane ledger and all mechanical recheck facts; it appended no new candidate. The inventories and complete pass records are in `review_1_5_2/relationships/numeric_relationship_inventory.md`, `review_1_5_2/statistics/relationship_inventory.md`, and `review_1_5_2/checkers/`.

# 6. Candidate Index

| ID | Pending quantitative reporting quality-control question | Primary locations |
|---|---|---|
| [C001](#c001--baseline-oxygenation-denominators-conflict-with-stated-saturation-missingness) | Oxygen-saturation denominators versus stated missingness | DOC001 p. 5 |
| [C002](#c002--patient-position-rows-leave-unreported-observations-in-both-arms) | Patient-position rows versus arm totals and fourth form option | DOC001 p. 6; DOC003 p. 9 |
| [C003](#c003--final-intubator-categories-exceed-the-bougie-arm-total) | Final-intubator categories versus Bougie arm total | DOC001 p. 6; DOC003 p. 7 |
| [C004](#c004--video-screen-use-categories-do-not-account-for-their-printed-denominators) | Screen-use rows versus available-data denominators and N/A form option | DOC001 p. 6; DOC003 p. 10 |
| [C005](#c005--main-table-3-reverses-duration-confidence-interval-endpoints) | Reversed Table 3 duration interval endpoints | DOC001 p. 7; DOC003 pp. 2-3 |
| [C006](#c006--published-duration-outcome-uses-a-different-endpoint-from-the-protocol) | Protocol cuff-inflation endpoint versus published blade-removal endpoint | DOC002 pp. 9-10; DOC001 pp. 3, 7; DOC003 p. 3 |
| [C007](#c007--reported-507-patient-interim-set-differs-from-the-protocols-first-500-analysis-set) | Protocol first-500 interim data versus reported 507 denominators | DOC002 p. 21; DOC003 p. 6 |

# 7. Candidate Evidence Cards

## C001 — Baseline oxygenation denominators conflict with stated saturation missingness

**Candidate statement:** Table 1 oxygen-saturation available-data denominators imply 61 missing values, while its oxygen-saturation footnote reports 43.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC001 `jama_driver_2018_oi_180054.pdf` — PDF p. 5, Table 1 and footnote b](<../jama_driver_2018_oi_180054.pdf#page=5>).

**Source evidence:** Arm totals are 381 and 376; oxygen-saturation rows use denominators 352 and 344. Footnote b reports oxygen saturation unavailable for 43 patients, split 19 and 24.

**Reported-versus-comparator:** Reported missingness is 19 + 24 = 43; arm totals minus displayed oxygen-saturation denominators give 29 + 32 = 61.

**Reasoning procedure:** Applied the same-field available-data identity to each printed arm total and denominator, then compared the implied missing counts with the footnote's stated oxygen-saturation counts.

**Calculation:** `381 - 352 = 29`; `376 - 344 = 32`; `29 + 32 = 61`; footnote `19 + 24 = 43`.

**Alternative source-grounded interpretations:** The threshold rows may use a distinct unstated availability field or time point; vital-sign labels or group splits in the footnote may be transposed. The package does not establish either explanation.

**Mechanical evidence recheck:** The cited Table 1 values, denominators, footnote ordering, and arithmetic were found and reproduced in `review_1_5_2/verification/evidence_recheck.md`.

**Quality-control relevance:** A baseline availability denominator and missingness statement should identify the same underlying field if both are intended to describe oxygen saturation.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an inconsistent baseline oxygen-saturation availability or missingness count into a descriptive evidence table.

**Human verification steps:** Inspect the source data dictionary, Table 1 production file, and any erratum to identify the field/time point behind denominators 352 and 344 and footnote b.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Patient-position rows leave unreported observations in both arms

**Candidate statement:** The three published patient-position rows total 378/381 and 372/376, while the source form provides a fourth `Seated Upright` option with no published counts.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC001 — PDF p. 6, Table 2](<../jama_driver_2018_oi_180054.pdf#page=6>); [DOC003 — PDF p. 9, postintubation form item 11](<../joi180054supp2_prod.pdf#page=9>).

**Source evidence:** Table 2 lists Bougie counts 222, 117, and 39 and ETT+stylet counts 244, 96, and 32. DOC003 item 11 instructs selection of one of four positions, including `Seated Upright` in addition to the three displayed types.

**Reported-versus-comparator:** The printed rows are compared with randomized-arm headers 381 and 376, conditional on whether the table intended them to be exhaustive.

**Reasoning procedure:** Summed the printed categories and compared each sum with its arm header; then checked the supplied form for an omitted defined response.

**Calculation:** `222 + 117 + 39 = 378`; `381 - 378 = 3`. `244 + 96 + 32 = 372`; `376 - 372 = 4`.

**Alternative source-grounded interpretations:** `Seated Upright` or missing/unclassified observations may account for residuals, but the package provides no arm counts for that form option. The residuals must not be assigned to it without counts.

**Mechanical evidence recheck:** All six counts, headers, and DOC003's four-option instruction were rechecked at the cited pages; category exhaustiveness remains an explicit unresolved premise.

**Quality-control relevance:** A reader needs the complete response set and denominator to interpret reported procedural position frequencies.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could treat the three published rows as a complete position distribution when a fourth response or missing category was present.

**Human verification steps:** Reproduce Table 2 from the patient-position form records, including `Seated Upright`, missing, and unclassified responses by arm.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Final-intubator categories exceed the Bougie arm total

**Candidate statement:** Bougie final-intubator counts total 383 against an arm total of 381, although the form calls for one training-level choice and includes PA/Other options not shown in Table 2.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC001 — PDF p. 6, Table 2 and footnote f](<../jama_driver_2018_oi_180054.pdf#page=6>); [DOC003 — PDF p. 7, postintubation form item 2](<../joi180054supp2_prod.pdf#page=7>).

**Source evidence:** Bougie rows are 318 senior resident/fellow, 57 junior resident, and 8 faculty. Footnote f labels these the final intubating physician. DOC003 item 2 says to circle one training level from G1, G2, G3, G4+/Fellow, Faculty, PA, or Other.

**Reported-versus-comparator:** Three published Bougie counts are compared with the Bougie randomized-arm total under the singular final-intubator description.

**Reasoning procedure:** Added the three published categories and compared the result with 381, while preserving uncertainty about the mapping from the full form response set to Table 2.

**Calculation:** `318 + 57 + 8 = 383`; `383 - 381 = 2`.

**Alternative source-grounded interpretations:** The PA/Other form choices may have been mapped into published categories, or a count/denominator transcription difference may exist. The one-choice instruction disfavors within-form overlap, but the package does not provide the coding map.

**Mechanical evidence recheck:** The counts, arm total, final-physician footnote, one-choice instruction, and PA/Other options were rechecked in `review_1_5_2/verification/evidence_recheck.md`.

**Quality-control relevance:** Final-operator categories should have a transparent classification rule when presented against an arm-level denominator.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an operator-training distribution whose published total is not reconciled to its patient denominator.

**Human verification steps:** Inspect the Table 2 coding specification and source form records to map every one-choice training-level response into the published rows.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Video-screen-use categories do not account for their printed denominators

**Candidate statement:** Three screen-use rows total 371/377 and 370/372; the form includes an additional explicit N/A response whose arm counts are not published.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC001 — PDF p. 6, Table 2 and footnote g](<../jama_driver_2018_oi_180054.pdf#page=6>); [DOC003 — PDF p. 10, postintubation form item 14](<../joi180054supp2_prod.pdf#page=10>).

**Source evidence:** Bougie counts are 218/377, 78/377, and 75/377; ETT+stylet counts are 182/372, 90/372, and 98/372. Footnote g gives four missing values per arm. DOC003 offers the three table patterns plus `N/A - Blade inserted and removed before attempting intubation`.

**Reported-versus-comparator:** The sums of the three displayed rows are compared with their explicit available-data denominators, conditionally on whether rows were intended to partition those observations.

**Reasoning procedure:** Reproduced availability denominators from the footnote, summed table rows, and checked the form for source-defined responses absent from the display.

**Calculation:** `381 - 4 = 377`; `376 - 4 = 372`. `218 + 78 + 75 = 371`; `377 - 371 = 6`. `182 + 90 + 98 = 370`; `372 - 370 = 2`.

**Alternative source-grounded interpretations:** The N/A response may account for some observations, or the three rows may overlap or be nonexhaustive. The package gives no N/A counts; residuals 6 and 2 must not be assigned to it.

**Mechanical evidence recheck:** The fractions, missingness footnote, and explicit DOC003 N/A response were rechecked; exclusivity and exhaustiveness are not stated.

**Quality-control relevance:** Table rows and denominators need a complete response-category rule to support accurate interpretation of procedural screen use.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy incomplete screen-use category frequencies or attach the available-data denominators to an incomplete response set.

**Human verification steps:** Reproduce the table from all four form responses plus missing values, with arm-specific counts and the production inclusion rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Main Table 3 reverses duration confidence-interval endpoints

**Candidate statement:** Main Table 3 prints the all-patient duration difference as `1 (4 to -1)` seconds, whereas the supplied clustered supplement prints ordered endpoints `1 (-1 to 4)`.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC001 — PDF p. 7, Table 3](<../jama_driver_2018_oi_180054.pdf#page=7>); [DOC003 — PDF p. 2, eTable 1](<../joi180054supp2_prod.pdf#page=2>); [DOC003 — PDF p. 3, clustering note](<../joi180054supp2_prod.pdf#page=3>).

**Source evidence:** DOC001 gives medians 38 versus 36 seconds and difference `1 (4 to -1)`, P=.24. DOC003 gives the same medians and point difference with `1 s (-1 s to 4 s)`, P=.95, and states that inferential columns were recalculated for physician clustering.

**Reported-versus-comparator:** The direct comparator is the conventional lower-to-upper order for a confidence interval in DOC001. DOC003 is corroborating endpoint-order evidence, not the same inferential model.

**Reasoning procedure:** Tested whether the printed bounds are ascending and contain the displayed point estimate, then compared the endpoint order with the separately clustered display without equating the two models.

**Calculation:** `4 > -1`; literal lower-to-upper reading would require `4 <= 1 <= -1`, which fails. Reordering yields `-1 <= 1 <= 4`.

**Alternative source-grounded interpretations:** A typographical endpoint transposition is possible. The clustered analysis may independently round to the same endpoints and does not prove the intended unadjusted interval.

**Mechanical evidence recheck:** The printed strings and clustering qualification were rechecked at all cited pages. Raw unadjusted confidence-interval output is not supplied.

**Quality-control relevance:** Confidence-interval endpoint order affects the direction and uncertainty an evidence user records.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer or meta-analytic data extractor could reverse or miscopy the duration interval endpoints.

**Human verification steps:** Inspect the unadjusted Table 3 statistical output and production table source to establish the intended lower and upper limits.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Published duration outcome uses a different endpoint from the protocol

**Candidate statement:** The protocol defines first-attempt time to intubation through ETT-cuff inflation, while the published tabular duration measure ends at laryngoscope-blade removal.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC002 — PDF p. 9, protocol section 2.2](<../joi180054supp1_prod.pdf#page=9>); [DOC002 — PDF p. 10, section 3.2](<../joi180054supp1_prod.pdf#page=10>); [DOC001 — PDF p. 3](<../jama_driver_2018_oi_180054.pdf#page=3>); [DOC001 — PDF p. 7, Table 3](<../jama_driver_2018_oi_180054.pdf#page=7>); [DOC003 — PDF p. 3, eTable footnote](<../joi180054supp2_prod.pdf#page=3>).

**Source evidence:** DOC002 defines first-attempt time from attempt beginning to ETT-cuff inflation in the trachea. DOC001 and DOC003 define their tabular duration from blade entry into the mouth to blade removal; Table 3 reports medians and differences using that published definition.

**Reported-versus-comparator:** The named protocol timing outcome is compared with the named published tabular duration outcome: their start event aligns, but cuff inflation and blade removal are distinct end events.

**Reasoning procedure:** Compared source definitions event by event and separated direct evidence for tabular medians/differences from the unsupplied variable mapping for time-to-event analyses.

**Calculation:** Protocol interval: `[laryngoscope entry, ETT-cuff inflation]`. Published tabular interval: `[blade entry, blade removal]`. The elapsed time between terminal events is not supplied.

**Alternative source-grounded interpretations:** An intentional amendment, renamed distinct variable, or recording change may reconcile the definitions. The package has no dated amendment, data dictionary, or analysis mapping. It is not directly established that every Kaplan-Meier curve or Cox hazard ratio used blade removal as its terminal event.

**Mechanical evidence recheck:** The protocol and publication definitions and Table 3/eTable locations were rechecked. Direct tabular endpoint evidence is distinct from the unresolved curve/HR terminal-event mapping.

**Quality-control relevance:** Identically or similarly named duration outcomes require an explicit event-boundary mapping across protocol and publication.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could treat blade-removal duration as the protocol's cuff-inflation time-to-intubation endpoint without preserving the distinction.

**Human verification steps:** Obtain the dated amendment or analysis plan, timing-variable dictionary, and model input definitions for each tabular and time-to-event result.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Reported 507-patient interim set differs from the protocol’s first-500 analysis set

**Candidate statement:** The protocol describes an interim analysis of data from the first 500 patients, while the eAppendix reports interim denominators totaling 507; operational overshoot remains a supplied-source-grounded alternative.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC002 — PDF p. 21, section 8.6.2](<../joi180054supp1_prod.pdf#page=21>); [DOC003 — PDF p. 6, eAppendix 1](<../joi180054supp2_prod.pdf#page=6>).

**Source evidence:** DOC002 says the analysis will occur after 500 patients are enrolled and specifically describes analysis of data from the first 500 patients. DOC003 says the interim analysis occurred after 507 and reports 250/257 versus 213/250.

**Reported-versus-comparator:** The direct comparison is the protocol's first-500 analysis-set language versus reported interim denominators totaling 507. “After 500” alone is not treated as an exact-500 requirement.

**Reasoning procedure:** Added the reported arm denominators and compared that total with the explicit first-500 protocol analysis-set language, retaining trigger-window and cutoff definitions as missing inputs.

**Calculation:** `257 + 250 = 507`; `507 - 500 = 7`.

**Alternative source-grounded interpretations:** Operational enrollment overshoot, delayed cutoff, data cleaning, or an authorized trigger window may explain the seven-record difference. The package supplies no cutoff rule, interim dataset definition, DSMB record, or amendment.

**Mechanical evidence recheck:** The protocol wording, eAppendix denominators, and arithmetic were rechecked. No inference about protocol compliance, the futility decision, or trial conclusions is made.

**Quality-control relevance:** Interim analysis-set size and trigger wording should be sufficiently explicit for readers to reconcile planned and reported quantities.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy an interim analysis-set size or trigger description without the protocol's first-500 qualification.

**Human verification steps:** Inspect contemporaneous enrollment/cutoff records, the interim dataset definition, DSMB documentation, and any amendment defining the permitted window.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

# 8. Downstream Evidence-Chain Considerations

The candidates are pending source-document questions, not determinations of downstream use. If confirmed, they could affect how a systematic review, meta-analysis, guideline evidence table, or other extractor records baseline availability, procedural category frequencies, interval bounds, duration definitions, or interim sample-set descriptions. No supplied package evidence establishes propagation, conclusion change, or harm.

# 9. Limitations and Missing Definitions

The supplied package lacks individual-level data, production tables, statistical code and output, complete variable mappings, confidence-interval construction details, protocol amendments, a complete table-to-form codebook, and interim cutoff/DSMB records. These omissions prevent reconstruction and limit explanatory conclusions. OCR can introduce reading or layout error; material pages were checked against fresh rendered images and the direct PDFs, which remain the authority. Native/layout PDF text and direct table reconstruction were unavailable in the local environment; see `review_1_5_2/limitations.md`.

# 10. Human Adjudication Checklist

For each pending card, a human reviewer should inspect the cited PDF pages and the relevant source-production or data-definition record; reproduce the stated arithmetic or definition comparison; determine whether a source-grounded alternative explains the display; document any correction or clarification outside this report; and complete the five blank fields on the applicable card. Human review should preserve the distinction between directly printed evidence and inferred explanations.

# 11. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

## Source integrity and execution record

The pre-review hashes are retained in `review_1_5_2/source_hashes_before.sha256`. Direct-source coverage is 49/49 mapped units. The complete stage assignments are retained in `review_1_5_2/coverage_manifest.md`; the mechanically rechecked stable-ID set is identical to the ledger set (`C001`–`C007`).

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| source_preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `source_inventory.md` |
| main_quantitative_mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_quantitative_mapping | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_checks | root/numeric_checks | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_checks | root/cross_source_checks | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality | root/evidence_quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation_summary.md` |

## Performance profile

- **Target basis:** Three PDFs with 49 wholly fresh page units, full browser-render and CPU-OCR fallback burden, one main trial report plus protocol and methods supplements, moderate expected quantitative relationship volume, and all mandated independent review lanes
- **Total source units:** 49
- **Fresh-source units:** 49
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-08-24T00:17:53Z
- **Finished UTC:** 2026-08-24T01:21:58Z
- **Observed elapsed minutes:** 64.1
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Direct Linux PDF text/raster/OCR tools were unavailable, requiring an offline Chrome-render plus direct CPU-Tesseract fallback for all 49 pages; complete review retained all 93 canonical relationships, two independent statistical passes, seven rechecks, and the final evidence-quality audit

## Token accounting and token-only API-equivalent cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

All amounts, when finalized, are token-only API-equivalent estimates under the dated local price snapshot, not invoices. Cached input/cache-write counts are input subsets and reasoning tokens are output subsets; they are not added again to total tokens. Per-agent detail is retained in `review_1_5_2/token_usage_ledger.csv` and `review_1_5_2/token_usage_summary.md`.

| Model | Known total tokens | Token count status | Token-only API-equivalent estimate (USD) |
|---|---:|---|---:|
| gpt-5.6-sol | 0 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE | __ |
| gpt-5.6-terra | 0 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE | __ |
