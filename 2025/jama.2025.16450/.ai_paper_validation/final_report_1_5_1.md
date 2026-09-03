# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

Every observation in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review of supplied local sources. It does not determine validity, importance, action, correction, or paper-level conclusions.

## Executive Quality-Control Summary

Complete source coverage produced 10 stable candidate consistency issues (`C001`-`C010`). Six have reproduced direct-source support (C001, C004, C007-C010). Four retained audit-trail IDs (C002, C003, C005, C006) have direct-source rechecks that contradict the earlier ledger transcription; their originally claimed mismatches were not reproduced. No candidate is based solely on a display-zero P value.

## Package and Reused-Evidence Provenance

The package contains five supplied PDFs: the 11-page main article (DOC-001), 35-page protocol (DOC-002), 162-page manual (DOC-003), 48-page SAP (DOC-004), and 16-page results supplement (DOC-005). All direct PDF pages were retained as the evidence authority. Existing page-level native text was usable for DOC-001 and DOC-005 (27 units); it served as a locator and transcription aid, not a replacement for direct-source confirmation. The evidence-asset inventory records 63 hashed reused artifacts and their fitness.

## Scope, Complete Coverage, and Exclusions

The review mapped all 272 direct-source PDF-page units: 27 reusable-backed and 245 fresh-required units. Every source row is complete (272 mapped units). Scope emphasized numeric, denominator/proportion/total, inferential-statistical, cross-document, effect-measure/label/scale, and rate-versus-count consistency. It excluded web material, external literature, raw data, pharmacy records, analysis programs, and amendment history not supplied in the package.

## Quantitative and Statistical Relationship Coverage

The canonical inventories contain 129 numeric relationships and 56 statistical relationships. Numeric and cross-source review was completed, and both independent statistical passes completed all 56 statistical relationships. Exact-source mechanical recheck and the final evidence-quality audit each covered all 10 stable IDs.

## Candidate Index

| ID | Candidate | Direct-source recheck status |
|---|---|---|
| [C001](#c001--etable-4-expands-rr-as-risk-difference-although-the-table-reports-relative-risk) | eTable 4 RR expansion | Reproduced |
| [C002](#c002--registered-eligibility-bound-discrepancy-is-not-reproduced-on-direct-source-recheck) | Eligibility upper bound | Original mismatch not reproduced |
| [C003](#c003--registered-first-dose-discrepancy-is-not-reproduced-on-direct-source-recheck) | First-dose volume | Original mismatch not reproduced |
| [C004](#c004--severe-ndi-gmfcs-cutoff-differs-between-the-manual-and-sap) | Severe-NDI GMFCS cutoff | Reproduced |
| [C005](#c005--registered-severe-ndi-instrument-edition-discrepancy-is-not-reproduced-on-direct-source-recheck) | Severe-NDI instrument edition | Original mismatch not reproduced |
| [C006](#c006--registered-first-interim-alpha-discrepancy-is-not-reproduced-on-direct-source-recheck) | First interim alpha | Original mismatch not reproduced |
| [C007](#c007--final-primary-analysis-alpha-differs-between-the-article-and-prospective-documents) | Final primary-analysis alpha | Reproduced, conditional interpretation |
| [C008](#c008--trial-center-count-differs-between-final-and-prospective-documents) | Trial center count | Reproduced, conditional interpretation |
| [C009](#c009--table-3-rr-label-conflicts-with-a-stated-common-or-approximation) | Table 3 RR/common-OR wording | Reproduced |
| [C010](#c010--etable-3-relative-risk-header-conflicts-with-odds-ratio-approximation-footnote) | eTable 3 RR/OR wording | Reproduced |

## Candidate Evidence Cards

## C001 — eTable 4 expands RR as risk difference although the table reports relative risk

**Candidate statement:** eTable 4 uses `RR` for ratio-scale relative-risk estimates but its abbreviation line expands `RR` as risk difference.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-005 [results supplement — PDF p. 7](<../joi250072supp4_prod_1761000786.6988.pdf#page=7>) (eTable 4 header and PDA row); [results supplement — PDF p. 8](<../joi250072supp4_prod_1761000786.6988.pdf#page=8>) (abbreviations and binary-outcome model text).

**Source evidence:** Page 7 prints `Relative Risk (RR) or Mean Difference (MD)` and PDA `RR: 0.86 (0.75, 0.99)`; page 8 prints `RR = risk difference` while stating binary outcomes report relative risks.

**Reported-versus-comparator:** The abbreviation says risk difference; the table header, model description, and estimates say or use relative risk.

**Reasoning procedure:** Compare the printed expansion with the stated measure and the null/scale implied by the displayed estimate.

**Calculation:** From displayed PDA counts, `(159/319)/(175/308) = 0.8772`; `100 x (159/319 - 175/308) = -6.97` percentage points. The adjusted `.86` is ratio-scale.

**Alternative source-grounded interpretations:** The p. 8 line may be an isolated copyediting or transcription error; the package does not establish cause.

**Mechanical evidence recheck:** Reproduced directly: header, ratio-form estimate, abbreviation, and model text are present on the cited pages.

**Quality-control relevance:** One abbreviation should not identify two distinct measures with different scales and null values.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could copy the RR abbreviation as risk difference rather than relative risk; no propagation or conclusion change is asserted.

**Human verification steps:** Confirm the p. 8 abbreviation against the eTable 4 header and the binary-outcome model description; determine the intended expansion.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Registered eligibility-bound discrepancy is not reproduced on direct-source recheck

**Candidate statement:** The prior ledger recorded `27 6/7` weeks for DOC-002, but direct-source recheck shows `28 6/7`; the original cross-document mismatch is not reproduced.

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** DOC-002 [protocol — PDF p. 4](<../joi250072supp1_prod_1761000786.68881.pdf#page=4>); DOC-003 [manual — PDF p. 7](<../joi250072supp2_prod_1761000786.6938.pdf#page=7>); DOC-004 [SAP — PDF p. 8](<../joi250072supp3_prod_1761000786.6988.pdf#page=8>) and [SAP — PDF p. 15](<../joi250072supp3_prod_1761000786.6988.pdf#page=15>); DOC-001 [main article — PDF p. 2](<../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=2>).

**Source evidence:** The protocol directly prints `22 0/7 - 28 6/7 weeks gestation`; the compared direct sources also print an upper bound of 28 weeks 6 days.

**Reported-versus-comparator:** Earlier ledger transcription `27 6/7` versus direct-page `28 6/7` in DOC-002 and every comparator.

**Reasoning procedure:** Directly read each eligibility passage, match the upper bound, and compare values.

**Calculation:** Pairwise upper-bound difference is 0 days, not 7 days.

**Alternative source-grounded interpretations:** The earlier extraction may have misread a custom-encoded `8` as `7`; the mechanism is inferred, not established.

**Mechanical evidence recheck:** Not reproduced as a source mismatch. Direct-page inspection contradicts the ledger transcription.

**Quality-control relevance:** Preserving this stable ID documents correction of a source-transcription issue and prevents it from being reused as a scientific discrepancy.

**Potential downstream evidence impact:** If confirmed as a transcription correction, an extractor could avoid copying `27 6/7` as the eligibility limit; no downstream use or conclusion effect is asserted.

**Human verification steps:** Read DOC-002 p. 4 visually and confirm whether any supplied direct page prints `27 6/7`.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Registered first-dose discrepancy is not reproduced on direct-source recheck

**Candidate statement:** The prior ledger assigned `1.25 mL/kg` to the first dose in DOC-002, but direct-source recheck shows `2.5 mL/kg`; the original mismatch is not reproduced.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-002 [protocol — PDF p. 4](<../joi250072supp1_prod_1761000786.68881.pdf#page=4>); DOC-003 [manual — PDF p. 7](<../joi250072supp2_prod_1761000786.6938.pdf#page=7>) and [manual — PDF p. 12](<../joi250072supp2_prod_1761000786.6938.pdf#page=12>); DOC-004 [SAP — PDF p. 8](<../joi250072supp3_prod_1761000786.6988.pdf#page=8>); DOC-001 [main article — PDF p. 2](<../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=2>); DOC-005 [results supplement — PDF p. 4](<../joi250072supp4_prod_1761000786.6988.pdf#page=4>).

**Source evidence:** All cited pages identify `2.5 mL/kg` as dose 1; the manual and results supplement identify `1.25 mL/kg` as dose 2.

**Reported-versus-comparator:** Earlier first-dose transcription `1.25 mL/kg` versus direct-source first-dose `2.5 mL/kg`.

**Reasoning procedure:** Match dose order, volume, and intervention context across the cited direct pages.

**Calculation:** `2.5 / 2.5 = 1`; difference `0 mL/kg` for the compared first-dose values.

**Alternative source-grounded interpretations:** Earlier extraction may have transferred the second-dose value or misread the first-dose volume; cause is not documented.

**Mechanical evidence recheck:** Not reproduced as a source mismatch. Direct-page inspection contradicts the ledger transcription.

**Quality-control relevance:** The audit trail prevents an incorrect dose-order transcription from being treated as a trial-document inconsistency.

**Potential downstream evidence impact:** If confirmed as a correction, an extractor could avoid copying `1.25 mL/kg` as the first dose; no downstream use or conclusion effect is asserted.

**Human verification steps:** Confirm the dose-order wording on DOC-002 p. 4 and the second-dose wording on DOC-003 p. 12 or DOC-005 p. 4.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Severe-NDI GMFCS cutoff differs between the manual and SAP

**Candidate statement:** The manual defines severe NDI using GMFCS levels `3-5`, whereas the SAP uses `4-5`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-003 [manual — PDF p. 14](<../joi250072supp2_prod_1761000786.6938.pdf#page=14>) and [manual — PDF p. 16](<../joi250072supp2_prod_1761000786.6938.pdf#page=16>); DOC-004 [SAP — PDF p. 10](<../joi250072supp3_prod_1761000786.6988.pdf#page=10>) and [SAP — PDF p. 33](<../joi250072supp3_prod_1761000786.6988.pdf#page=33>).

**Source evidence:** The manual prints `3-5`; the SAP prints `4-5`/`level 4-5` for the severe-NDI component.

**Reported-versus-comparator:** Manual threshold `{3,4,5}` versus SAP threshold `{4,5}`.

**Reasoning procedure:** Compare the direct endpoint-definition cutoffs and identify category membership that differs.

**Calculation:** Exact set difference is `{3}`; the cutoff shifts by one GMFCS level.

**Alternative source-grounded interpretations:** A versioned definition change is possible, but no governing amendment or implemented follow-up algorithm is supplied.

**Mechanical evidence recheck:** Reproduced directly on the cited manual and SAP pages.

**Quality-control relevance:** A binary endpoint component should use one traceable threshold or be explicitly version-qualified.

**Potential downstream evidence impact:** If confirmed and later reported, an extractor could copy a different severe-NDI component threshold; no endpoint effect or conclusion change is established.

**Human verification steps:** Identify the governing endpoint definition, amendment history, and treatment of GMFCS level 3.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Registered severe-NDI instrument-edition discrepancy is not reproduced on direct-source recheck

**Candidate statement:** The prior ledger reported Bayley-III versus BSID-IV, but direct-source recheck shows BSID-IV/fourth edition throughout; the original mismatch is not reproduced.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-003 [manual — PDF p. 14](<../joi250072supp2_prod_1761000786.6938.pdf#page=14>) and [manual — PDF p. 16](<../joi250072supp2_prod_1761000786.6938.pdf#page=16>); DOC-004 [SAP — PDF p. 10](<../joi250072supp3_prod_1761000786.6988.pdf#page=10>), [SAP — PDF p. 33](<../joi250072supp3_prod_1761000786.6988.pdf#page=33>), and [SAP — PDF p. 34](<../joi250072supp3_prod_1761000786.6988.pdf#page=34>).

**Source evidence:** The cited passages print BSID-IV or `4th edition (BSID-IV)` with cognitive score `<70`; none prints Bayley-III.

**Reported-versus-comparator:** Earlier ledger Bayley-III transcription versus direct-source fourth-edition/BSID-IV wording.

**Reasoning procedure:** Match instrument edition and threshold in the direct endpoint-definition passages.

**Calculation:** `4th edition` and `BSID-IV` are the same edition; all cited passages retain `<70`.

**Alternative source-grounded interpretations:** The prior extraction may have read `IV` as `III` or carried text from another template; cause is not established.

**Mechanical evidence recheck:** Not reproduced as a source mismatch. Direct-page inspection contradicts the ledger transcription.

**Quality-control relevance:** The record distinguishes a corrected transcription from an instrument-definition conflict.

**Potential downstream evidence impact:** If confirmed as a correction, an extractor could avoid recording Bayley-III for this endpoint; no different instrument use or conclusion effect is asserted.

**Human verification steps:** Confirm the SAP p. 33 wording and determine whether any supplied direct page identifies Bayley-III for severe NDI.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Registered first-interim-alpha discrepancy is not reproduced on direct-source recheck

**Candidate statement:** The prior ledger recorded protocol alpha `0.00015`, but both direct pages print `0.000015`; the original tenfold mismatch is not reproduced.

**Category:** Statistical reporting inconsistency

**Exact source locations:** DOC-002 [protocol — PDF p. 29](<../joi250072supp1_prod_1761000786.68881.pdf#page=29>); DOC-004 [SAP — PDF p. 26](<../joi250072supp3_prod_1761000786.6988.pdf#page=26>).

**Source evidence:** Both schedules print first-look alpha `0.000015`, followed by `.0030`, `.0183`, and `.0440`.

**Reported-versus-comparator:** Earlier protocol transcription `0.00015` versus direct protocol and SAP `0.000015`.

**Reasoning procedure:** Compare matched 25% efficacy-look nominal-alpha strings on the direct pages.

**Calculation:** `0.000015 / 0.000015 = 1`; difference `0`.

**Alternative source-grounded interpretations:** The earlier extraction may have dropped one zero in custom-encoded text; cause is inferred only.

**Mechanical evidence recheck:** Not reproduced as a source mismatch. Direct-page inspection contradicts the ledger transcription.

**Quality-control relevance:** The audit trail prevents a dropped-zero transcription from being reused as a statistical reporting conflict.

**Potential downstream evidence impact:** If confirmed as a correction, an extractor could avoid copying `0.00015` as the first-look alpha; no altered inference or conclusion effect is asserted.

**Human verification steps:** Visually confirm the decimal strings in both schedules and search supplied protocol pages for an alternative `0.00015` statement.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Final primary-analysis alpha differs between the article and prospective documents

**Candidate statement:** The article reports primary-analysis alpha `.049`; the protocol and SAP list planned final alpha `.0440`.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001 [main article — PDF p. 3](<../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3>) and [main article — PDF p. 7](<../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7>); DOC-002 [protocol — PDF p. 29](<../joi250072supp1_prod_1761000786.68881.pdf#page=29>); DOC-004 [SAP — PDF p. 26](<../joi250072supp3_prod_1761000786.6988.pdf#page=26>).

**Source evidence:** Article text and Table 2 footnote state `.049`; the prospective schedules state `.0440` for the planned final look.

**Reported-versus-comparator:** Executed article alpha `.049` versus prospective planned final alpha `.0440`.

**Reasoning procedure:** Compare matched primary-analysis thresholds while preserving planned-versus-realized context.

**Calculation:** `.049 - .0440 = .0050`; `.049/.0440 = 1.1136`.

**Alternative source-grounded interpretations:** A realized Lan-DeMets boundary, recovery of unspent alpha, different information timing, unperformed looks, or amendment could explain the values. Relevant execution output is absent.

**Mechanical evidence recheck:** Reproduced values; the consistency question remains conditional because planned and realized boundaries need not be equal.

**Quality-control relevance:** The executed threshold should be traceable to the prospective alpha-spending framework or a documented recalculation.

**Potential downstream evidence impact:** If confirmed unresolved, an extractor could record different primary significance thresholds; no incorrect estimate, propagation, or conclusion change is asserted.

**Human verification steps:** Obtain realized information fractions, look dates/status, alpha-spending output, and amendment/recovery documentation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Trial center count differs between final and prospective documents

**Candidate statement:** The article states 17 centers; the protocol and SAP state 15 centers in prospective context.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001 [main article — PDF p. 1](<../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1>); DOC-002 [protocol — PDF p. 29](<../joi250072supp1_prod_1761000786.68881.pdf#page=29>); DOC-004 [SAP — PDF p. 8](<../joi250072supp3_prod_1761000786.6988.pdf#page=8>).

**Source evidence:** DOC-001 reports 17 US centers; the prospective documents refer to 15 NRN centers/planned participation.

**Reported-versus-comparator:** Completed-study count 17 versus planned count 15.

**Reasoning procedure:** Match the trial setting and compare counts while retaining the documents' time-tense and counting-basis context.

**Calculation:** `17 - 15 = 2` centers.

**Alternative source-grounded interpretations:** Later site activation or a different center/hospital/pooling definition is plausible; activation/enrollment records are absent.

**Mechanical evidence recheck:** Reproduced values; whether they are inconsistent is conditional on shared operational period and definition.

**Quality-control relevance:** Trial-setting counts should be time/version qualified when prospective and completed counts differ.

**Potential downstream evidence impact:** If confirmed unresolved, an extractor could copy 15 or 17 as the trial setting; no model-estimate or conclusion effect is asserted.

**Human verification steps:** Obtain center activation and enrollment records and determine the center-counting definition used in each document.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Table 3 RR label conflicts with a stated common-OR approximation

**Candidate statement:** Table 3 labels an estimate RR while footnote g describes a common-OR approximation after robust-Poisson nonconvergence.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-001 [main article — PDF p. 8](<../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8>) (Table 3 additional open-label surfactant row and footnote g).

**Source evidence:** The row prints `RR: 0.69 (0.33 to 1.46)` for 13/312 versus 18/299; footnote g names Mantel-Haenszel methods `approximated by the common OR`.

**Reported-versus-comparator:** RR row label versus common-OR approximation wording.

**Reasoning procedure:** Compare the measure label, estimator description, and diagnostic crude measures without treating crude values as the stratified result.

**Calculation:** Crude RR `(13/312)/(18/299) = 0.6921`; crude OR `[13 x 281]/[299 x 18] = 0.6787`.

**Alternative source-grounded interpretations:** The target estimand may be RR while a common OR was used as a sparse-event approximation. Stratum counts, weights, and model output are unavailable.

**Mechanical evidence recheck:** Reproduced directly on Table 3 and footnote g.

**Quality-control relevance:** The reported estimator and target measure should be unambiguous because RR and OR are distinct measures.

**Potential downstream evidence impact:** If confirmed, an extractor, systematic review, meta-analysis, or guideline could classify the estimate as RR or OR differently; no numeric error, propagation, or conclusion change is asserted.

**Human verification steps:** Review the model output and stratified Mantel-Haenszel specification; determine the formal estimator and label.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — eTable 3 relative-risk header conflicts with odds-ratio approximation footnote

**Candidate statement:** eTable 3's effect-estimate header says relative risk while footnote b identifies odds-ratio approximations for marked sparse rows.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-005 [results supplement — PDF p. 5](<../joi250072supp4_prod_1761000786.6988.pdf#page=5>) and [results supplement — PDF p. 6](<../joi250072supp4_prod_1761000786.6988.pdf#page=6>) (eTable 3 header and footnote b).

**Source evidence:** The header says `Relative Risk (95% CI) or P-value`; footnote b says marked low-prevalence rows use crude unadjusted odds ratios with exact 95% CIs as an approximation. Marked examples include `.73`, `.65`, and `2.64`.

**Reported-versus-comparator:** Table-level RR header versus odds-ratio approximation footnote for superscript-b rows.

**Reasoning procedure:** Compare header and row-footnote measure wording and calculate crude OR diagnostics from displayed counts.

**Calculation:** `(3 x 309)/(319 x 4) = 0.7265`; `(2 x 310)/(320 x 3) = 0.6458`; `(8 x 310)/(314 x 3) = 2.6327`, close to `.73`, `.65`, and `2.64`.

**Alternative source-grounded interpretations:** The header may name the target measure and the footnote the approximating estimator. Exact CI reproduction needs the specified exact-interval algorithm and row inputs.

**Mechanical evidence recheck:** Reproduced directly on the cited eTable 3 pages.

**Quality-control relevance:** Rows using OR approximations should have an unambiguous reported measure label.

**Potential downstream evidence impact:** If confirmed, a row-level extractor, systematic review, meta-analysis, or guideline could classify marked estimates as RR or OR differently; no conclusion change or actual propagation is asserted.

**Human verification steps:** Determine intended extraction labels for superscript-b rows and confirm the exact interval and estimator convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable numeric or labeling defects can matter when evidence is later abstracted into systematic reviews, meta-analyses, guidelines, or other structured evidence products. This report only identifies what could be copied if a candidate is confirmed. It does not assert propagation, harm, or a change to any study conclusion.

## Limitations and Missing Definitions

The review uses only the five supplied PDFs. Nonstandard embedded fonts in DOC-002 through DOC-004 required direct-render visual inspection for exact transcription. Individual/stratum-level data, fitted-model output, exact CI algorithms, realized alpha-spending output, amendment history, and center activation/enrollment records are unavailable. These gaps limit C004, C007-C010 to the printed relationships and their specified human questions. Four historical candidate transcriptions (C002, C003, C005, C006) are contradicted by direct-source recheck and are retained solely as required audit trail IDs.

## Human Adjudication Checklist

- Confirm each cited source location against the direct PDF page.
- Determine whether a reproduced difference is explained by version, timing, estimator, or definition.
- Complete the five blank human-adjudication fields on each card.
- Record any action in an adjudication system separate from this report; this review makes none.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source Integrity and Coverage

- **Direct sources:** 5 PDFs.
- **Source-unit counts:** 272 total; 27 reusable; 245 fresh-required; 272 mapped.
- **Source integrity baseline:** `review_1_5_1/source_hashes_before.sha256`.
- **Reused-artifact integrity baseline:** `review_1_5_1/reused_artifact_hashes_before.sha256`.
- **Coverage and evidence artifacts:** `review_1_5_1/source_coverage.md`, `review_1_5_1/coverage_manifest.md`, relationship inventories, checker artifacts, `verification/evidence_recheck.md`, and `quality/evidence_quality_audit.md`.

### Agent Execution

The execution manifest records the coordinator plus reuse curation, main and support mapping, numeric, cross-source, two independent statistical-pass, exact-source recheck, evidence-quality, and report-generation agents. Statistical passes 1 and 2 were completed by distinct new `gpt-5.6-terra` high-effort agents. See `review_1_5_1/agent_execution_manifest.md` for runtime IDs, models, efforts, start modes, and artifact ownership.

### Performance

- **Target basis:** Five-PDF paper package with 272 direct-source pages, including a 162-page manual and a 48-page SAP; reusable page-level text is visibly available for the 11-page main article and 16-page results supplement, while three support PDFs require unit-level curator confirmation and likely fresh native/layout mapping. The range allows parallel evidence mapping plus two mandatory full statistical passes and complete recheck/audit/report stages.
- **Total source units:** 272
- **Fresh-source units:** 245
- **Target elapsed minutes:** 100-150
- **Started UTC:** 2026-09-03T03:43:52Z
- **Finished UTC:** 2026-09-03T06:48:20Z
- **Observed elapsed minutes:** 184.5
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Severe host CPU contention (load approximately 610 on 8 allocated CPUs); embedded-font extraction and empty OCR required rendered-page inspection of 245 fresh units and a 33-page SAP coverage repair; canonical relationship ranges required expansion to 185 individual IDs; direct-source recheck corrected four extraction-derived candidate transcriptions.

### Token Accounting and Cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Token-accounting status | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---|---:|---:|
| gpt-5.6-sol | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE | 0 (known; incomplete) | 0.000000 known; complete estimate unavailable |
| gpt-5.6-terra | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE | 0 (known; incomplete) | 0.000000 known; complete estimate unavailable |

The accounting window is closed. The runtime exposed no authoritative response-level token counts for the coordinator or any specialist, so each manifested agent has an `UNAVAILABLE` record and no text-length estimate was substituted. The displayed zero is the known subtotal from exact records, not a claim of zero actual usage. Cached input and cache-write counts are input subsets and reasoning counts are output subsets; they are not added again to total tokens. Any cost is a token-only API-equivalent estimate under the 2026-08-18 pricing snapshot, not an invoice. Per-agent detail is in `review_1_5_1/token_usage_summary.md` and `review_1_5_1/token_usage_ledger.csv`.
