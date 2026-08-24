# Quantitative Quality-Control Consistency Review: JAMA 2018 Paper Package

> ## Pending Human Adjudication
>
> This is a quantitative reporting quality-control review. Every candidate below is **Pending Human Adjudication**. It identifies reproducible supplied-source consistency questions; it does not determine an intended correction, study validity, or a paper-level conclusion.

## Executive Quality-Control Summary

Complete fresh-stage coverage registered **4** distinct candidate consistency issues: one denominator/proportion issue, one arithmetic-display issue, one statistical reporting issue, and one measure/unit issue. All 4 were mechanically rechecked at their exact supplied-source locations and retained by the quality audit. No candidate was registered solely because of a display-zero P value; none occurred in the reviewed relationships.

Small preventable reporting defects can matter when a systematic reviewer, meta-analyst, guideline team, or data extractor copies a displayed count, denominator, effect, interval, or unit. This report does not claim that any such propagation, conclusion change, or harm occurred.

## Package and Fresh-Processing Provenance

The package contains three direct supplied PDFs: the 9-page main article (DOC-001), the 134-page protocol/statistical-analysis supplement (DOC-002), and the 3-page additional supplement (DOC-003), for 146 PDF-page units. All 146 units were freshly mapped; reusable-unit count is zero.

Native extraction used the logged PyMuPDF command-line fallback in simple and layout modes because `pdfinfo`, `pdftotext`, `pdftoppm`, and `pdftocairo` were unavailable. The user expressly authorized reuse of existing source-hash-matched OCR only for DOC-002 pp. 52, 108-109, and 126-133. No new CPU or GPU OCR was performed. DOC-002 p. 134 is an empty direct-text page and had no authorized OCR.

Fresh artifacts: [source inventory](review_1_5_2/source_inventory.md), [source coverage](review_1_5_2/source_coverage.md), [evidence assets](review_1_5_2/evidence_asset_inventory.md), [coverage manifest](review_1_5_2/coverage_manifest.md), and [PyMuPDF extraction log](review_1_5_2/preprocessing/pymupdf_extraction_log.md).

## Scope, Complete Coverage, and Exclusions

The review covered numeric, denominator/proportion/total, inferential-statistical, cross-document, measure/label/scale, and rate-versus-count relationships in all result-relevant supplied material. It did not perform a broad methodology, clinical, misconduct, raw-data, or external-literature audit.

| Coverage domain | Completed coverage |
|---|---:|
| Direct source units | 146/146 |
| DOC-001 pages | 9/9 |
| DOC-002 pages | 134/134 |
| DOC-003 pages | 3/3 |
| Coverage-manifest rows | 23/23 prepared review rows |
| Stable candidates mechanically rechecked | 4/4 |

The direct-source inventory excludes only the operating-system `Zone.Identifier` sidecar, which is not scientific source content. No old audit conclusion, candidate set, final report, or web source was used as evidence.

## Quantitative and Statistical Relationship Coverage

The numeric inventory is complete and gap-free at **N001-N098** (98 relationships): 29 main-article, 17 first-support-shard, 38 second-support-shard, and 14 third-support-shard records. The statistical inventory is complete and gap-free at **S001-S055** (55 relationships): 17 main-article, 14 first-support-shard, 14 second-support-shard, and 10 third-support-shard records.

The numeric consistency lane completed 98/98 relationships. The cross-source lane completed 153/153 matched numeric/statistical relationships after population, time, contrast, model/test, scale, and precision controls. Statistical pass 1 and the distinct statistical pass 2 each completed 55/55 relationships. Pass 2 also revisited C001-C004 and registered zero genuinely new distinct propositions.

Supporting artifacts: [numeric relationship inventory](review_1_5_2/relationships/numeric_relationship_inventory.md), [statistical relationship inventory](review_1_5_2/statistics/relationship_inventory.md), [numeric review](review_1_5_2/checkers/numeric_consistency.md), [cross-source review](review_1_5_2/checkers/cross_source_consistency.md), [statistical pass 1](review_1_5_2/checkers/statistical_pass_1.md), and [statistical pass 2](review_1_5_2/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Category | Exact supplied-source location | Status |
|---|---|---|---|
| [C001](#c001--per-protocol-eti-rosc-percentage-does-not-reconcile-with-its-printed-numerator-denominator-and-signed-difference) | Denominator, proportion, or total inconsistency | DOC-001 Table 2, [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>) | Pending Human Adjudication |
| [C002](#c002--per-protocol-day-28-survival-point-difference-is-not-supported-by-the-printed-counts-and-denominators-at-one-decimal-precision) | Numeric or arithmetic inconsistency | DOC-001 Table 2, [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>) | Pending Human Adjudication |
| [C003](#c003--per-protocol-day-28-survival-confidence-interval-has-a-scale-inconsistency-with-the-displayed-rates-and-same-row-inferential-display) | Statistical reporting inconsistency | DOC-001 Table 2, [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>) | Pending Human Adjudication |
| [C004](#c004--centre-5-pause-difference-uses-a-time-unit-for-a-named-count-outcome) | Measure, label, or scale inconsistency | DOC-001 Results, [PDF p. 4](<../jama_jabre_2018_oi_180004.pdf#page=4>) | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Per-protocol ETI ROSC percentage does not reconcile with its printed numerator, denominator, and signed difference

**Candidate statement:** The per-protocol ETI ROSC percentage, `30.0%`, does not reconcile with its printed numerator/denominator (`377/943`) or with the same-row signed BMV-minus-ETI difference.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** DOC-001, main article Table 2, Per-Protocol Analysis, “Return of spontaneous circulation,” [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>); fresh locator: [layout text](review_1_5_2/preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt).

**Source evidence:** BMV is `342 (34.4)` of PP `n = 995`; ETI is `377 (30.0)` of PP `n = 943`; the table prints BMV-minus-ETI `−5.6 (−9.9 to −1.3)` and `P = .01`.

**Reported-versus-comparator:** Reported ETI `30.0%` versus `100 × 377/943`, and versus the same-row signed difference.

**Reasoning procedure:** A `No. of Patients (%)` cell is checked as `100 × count / stated denominator` with ordinary one-decimal rounding. The difference is checked on the table’s stated BMV-minus-ETI percentage-point scale.

**Calculation:** `100 × 377/943 = 39.978791%`, rounding to `40.0%`, not `30.0%`. `100 × (342/995 − 377/943) = −5.606932` pp, compatible with printed `−5.6`; displayed percentages give `34.4 − 30.0 = +4.4` pp. The 9.978791-pp percentage separation exceeds the 0.05-pp one-decimal tolerance.

**Alternative source-grounded interpretations:** Another denominator near 1257 could yield 30.0%, but none is printed for this row. A production or transcription issue could affect one of the count, denominator, percentage, or difference; the source does not identify which.

**Mechanical evidence recheck:** Location, source text, comparator, direction, denominators, arithmetic, and rounding rule were found and reproduced. The direct evidence and remaining unknowns are documented in [evidence recheck](review_1_5_2/verification/evidence_recheck.md).

**Quality-control relevance:** This links a secondary-outcome percentage, denominator, and signed risk difference; the printed values do not reconcile under the stated rule.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the incorrect ETI percentage or an internally inconsistent rate/difference pairing into a systematic review, meta-analysis, guideline evidence table, or later evidence product. No propagation or conclusion change is asserted.

**Human verification steps:** Verify the publisher-quality Table 2 source, PP analysis denominator, ETI ROSC count, and generated risk difference; determine which printed element reflects the intended result.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Per-protocol day-28 survival point difference is not supported by the printed counts and denominators at one-decimal precision

**Candidate statement:** The printed PP day-28 survival difference of `0.1` pp does not reproduce from the printed count/denominator pairs under ordinary one-decimal rounding.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-001, main article Table 2, Per-Protocol Analysis, “Survival at 28 d,” [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>); fresh locator: [layout text](review_1_5_2/preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt).

**Source evidence:** The row prints BMV `54 (5.4)` of `n = 995`, ETI `51 (5.4)` of `n = 943`, and BMV-minus-ETI `0.1 (−10 to 9.7)`, `P = .99`.

**Reported-versus-comparator:** Reported `0.1` percentage-point difference versus the count-derived BMV-minus-ETI difference.

**Reasoning procedure:** When the displayed counts and PP denominators define the displayed proportion-difference estimator, compute `100 × (54/995 − 51/943)` and apply ordinary one-decimal rounding.

**Calculation:** `100 × 54/995 = 5.427136%`; `100 × 51/943 = 5.408271%`; difference `0.018864` pp. This rounds to `0.0` pp. `|0.100000 − 0.018864| = 0.081136` pp, exceeding the 0.05-pp tolerance. Both displayed group percentages round to `5.4%`.

**Alternative source-grounded interpretations:** An unprinted retained-precision calculation, alternate denominator, or differently defined PP estimator could yield 0.1, but none is specified in the row, footnote, or stated table heading.

**Mechanical evidence recheck:** The row, counts, denominators, percentages, direction, calculation, and tolerance were independently reproduced; the source lacks the exact point-estimator definition. See [evidence recheck](review_1_5_2/verification/evidence_recheck.md).

**Quality-control relevance:** A secondary-outcome point estimate that does not reproduce from its displayed inputs can affect direct quantitative extraction.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a point difference that does not correspond to the displayed count/denominator pairs into later evidence products. No propagation or conclusion change is asserted.

**Human verification steps:** Obtain the exact PP estimator, analysis denominator, and retained group rates used for this cell; verify whether they differ from `54/995` and `51/943`.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Per-protocol day-28 survival confidence interval has a scale inconsistency with the displayed rates and same-row inferential display

**Candidate statement:** The printed PP survival 95% CI, `−10 to 9.7`, has a scale/span inconsistency with the displayed percentage-point effect, matched event rates, and near-null same-row P-value context; the exact source CI construction is not supplied.

**Category:** Statistical reporting inconsistency

**Exact source locations:** DOC-001, main article Table 2, Per-Protocol Analysis, “Survival at 28 d,” including heading and footnote, [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>); fresh locators: [simple text](review_1_5_2/preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt) and [layout text](review_1_5_2/preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt).

**Source evidence:** BMV `54/995 (5.4%)`, ETI `51/943 (5.4%)`, difference `0.1`, 95% CI `−10 to 9.7`, and `P = .99`. The heading is BMV(%) minus ETI(%) (95% CI); footnote alternatives are chi-square or Fisher exact tests.

**Reported-versus-comparator:** Reported 19.7-pp CI span versus the matched count-derived rates on the table’s percentage-point scale. `P = .99` is retained only as observed near-null context, not as an independent CI reconstruction.

**Reasoning procedure:** Calculate the printed rates and, as a diagnostic approximation only, an unpooled binomial risk-difference interval. Keep the source-specific CI method distinct because it is not stated.

**Calculation:** Rates are `5.427136%` and `5.408271%`, with count-derived difference `+0.018864` pp. Diagnostic unpooled binomial SE is about `1.028756` pp and approximate 95% interval `−1.997498` to `2.035226` pp, rather than printed `−10` to `9.7`. No rounding tolerance applies to this scale/span question.

**Alternative source-grounded interpretations:** A different CI method, alternate unprinted analysis set, adjustment, or decimal/transcription issue could explain the display, but the package supplies no row-specific formula, settings, or intended limits. This does not assert a replacement interval.

**Mechanical evidence recheck:** The source row, heading, footnote, rates, P value, diagnostic calculation, and missing-method boundary were reproduced. See [evidence recheck](review_1_5_2/verification/evidence_recheck.md).

**Quality-control relevance:** A confidence interval whose displayed scale does not reconcile with its matched effect display may affect statistical extraction.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy an interval with a wrong scale or span into a systematic review, meta-analysis, guideline table, or later evidence product. No propagation or conclusion change is asserted.

**Human verification steps:** Obtain the row-specific CI method, software options, analysis set, and generated limits; determine whether either displayed limit has a decimal or transcription issue.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Centre-5 pause difference uses a time unit for a named count outcome

**Candidate statement:** A named count outcome is paired with a time-unit label: the report calls it the number of qualifying pauses, gives `27` versus `16`, and labels the difference `11 seconds`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** DOC-001, Results “Post-Hoc Analyses,” [PDF p. 4](<../jama_jabre_2018_oi_180004.pdf#page=4>); outcome definition in Methods, [PDF p. 3](<../jama_jabre_2018_oi_180004.pdf#page=3>); fresh locators: [simple text](review_1_5_2/preprocessing/pymupdf_simple_text/DOC-001_jama_jabre_2018_oi_180004.txt) and [layout text](review_1_5_2/preprocessing/pymupdf_layout_text/DOC-001_jama_jabre_2018_oi_180004.txt).

**Source evidence:** The paper names the outcome “number of pauses greater than 2 seconds during CPR,” reports BMV `27` versus ETI `16`, “difference, `11 seconds` [95% CI, 7 to 15]; P < .001,” and separately reports chest-compression fraction `86%` versus `87%`.

**Reported-versus-comparator:** Reported `seconds` unit for the difference/CI versus the stated count outcome and its two group values.

**Reasoning procedure:** For values explicitly presented as numbers of qualifying events, their difference retains the count measure. The two-second duration is the event-defining threshold, not necessarily the unit of the count difference.

**Calculation:** `27 − 16 = 11`, consistent with a count difference of 11 pauses. No numerical tolerance applies; the check is categorical (count measure versus duration unit).

**Alternative source-grounded interpretations:** The values might be undisclosed duration summaries, which could support seconds, but that conflicts with the repeated “number of pauses” description. The supplied source does not define whether 27 and 16 are totals, means, medians, or another summary.

**Mechanical evidence recheck:** The results and methods wording, group values, arithmetic difference, threshold, unit label, and separate CCF measure were found and reproduced. See [evidence recheck](review_1_5_2/verification/evidence_recheck.md).

**Quality-control relevance:** Confusing a count with a duration can misstate the effect measure and unit available for quantitative extraction.

**Potential downstream evidence impact:** If confirmed, a later extractor could record the difference/CI as seconds rather than pauses, or misclassify the outcome measure in a systematic review, meta-analysis, guideline, or other evidence product. No propagation or conclusion change is asserted.

**Human verification steps:** Determine whether `27` and `16` are counts or duration summaries, identify the summary statistic and CI method, and verify the intended unit for the difference and interval.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these issues concern fields commonly copied into structured evidence extraction: numerators, denominators, percentages, risk differences, confidence intervals, and outcome units. Verification at the source or publisher-quality table level can help keep later evidence products internally consistent. The supplied package provides no evidence that any candidate propagated, changed a conclusion, or caused harm.

## Limitations and Missing Definitions

This review is limited to supplied local evidence. [Complete limitations](review_1_5_2/limitations.md) include the source-boundary constraint, user-authorized hash-matched OCR reuse without new OCR, absent Poppler tools, PyMuPDF extraction fallback, and DOC-002 p. 134 empty-page limitation.

For C001, the intended ETI ROSC element or alternate denominator is not supplied. For C002, the exact point estimator and retained rates are not supplied. For C003, the row-specific CI construction is not supplied. For C004, the group-summary definition and intended unit are not supplied. These omissions bound the inferences and preserve the questions for human adjudication.

## Human Adjudication Checklist

- Confirm each cited PDF page against publisher-quality source material.
- Check analysis population, denominator, estimator, scale, unit, and rounding convention before deciding any correction.
- Preserve the original printed evidence and record any external confirmation separately.
- Complete all five fields in each candidate card; no candidate has a preassigned validity, importance, action, initials, or notes value.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

| Direct source | PDF units | SHA-256 before review |
|---|---:|---|
| `jama_jabre_2018_oi_180004.pdf` | 9 | `114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839` |
| `joi180004supp1_prod.pdf` | 134 | `70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913` |
| `joi180004supp2_prod.pdf` | 3 | `937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46` |

The pre-review source hashes are recorded in [source_hashes_before.sha256](review_1_5_2/source_hashes_before.sha256). The quality audit independently recomputed all three and recorded matches. Authorized OCR provenance is [DOC-002 provenance](review_1_5_2/preprocessing/reused_ocr/DOC-002_authorized_ocr_provenance.md).

### Agent execution

| Stage | Agent ID | Model | Effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh source preprocessing | ec752004-1fe1-53b2-8232-b61a88e90fc1 | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main quantitative mapping | 1ab14919-011a-52bd-8466-6b46d349699d | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support mapping 001 | f80933af-4be1-59f1-a3a1-249e4965f15b | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/parts/support_001_pp001_050.md` |
| support mapping 002 | fcf1ed1a-48ee-54cc-b67e-b469c1e1920a | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/parts/support_002_pp051_100.md` |
| support mapping 003 | 4451ad83-7d98-5b94-92e6-c0ff6ac951a9 | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/parts/support_003_pp101_134_doc003.md` |
| relationship inventory merge | 3605d978-cb09-5b5c-a2c1-d372918b8298 | gpt-5.6-terra | medium | FRESH_SPAWN | `relationships/numeric_relationship_inventory.md` |
| numeric consistency review | d8d97fbf-b16d-578f-882d-50c8e3c2f980 | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross-source consistency review | 9c8b1144-85b7-594d-a423-3821bcf2dd2f | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistical pass 1 | 73b64cf4-d780-58b8-b200-d7723373321d | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| candidate registration | b7f215f2-95c6-5b76-9caf-e193e8bb69d0 | gpt-5.6-terra | medium | FRESH_SPAWN | `candidate_ledger.md` |
| evidence recheck | 38085982-19f9-5d61-abf9-4673515661e6 | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistical pass 2 | 23866370-c384-545f-af7b-e837892be6b0 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence quality audit | bb503380-c331-5f67-8566-108424ee529e | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report generation | f7216cee-425c-5269-98c0-50f46806fa65 | gpt-5.6-terra | medium | FRESH_SPAWN | `../final_report_1_5_2.md` |

### Performance and token-accounting patch block

- **Target basis:** Three supplied PDFs with 146 total pages: a 9-page main article, a 134-page protocol/statistical-analysis supplement, and a 3-page additional supplement. The package has substantial cross-document and table/statistical scope. Eleven source-hash-matched OCR pages are already supplied for difficult supplement pages and are reused under the user's explicit instruction; all scientific mapping and checking is newly performed. The normal Poppler command-line tools are absent, which may increase extraction effort.
- **Total source units:** 146
- **Fresh-source units:** 146
- **Target elapsed minutes:** 45-70
- **Started UTC:** 2026-08-24T00:24:32Z
- **Finished UTC:** 2026-08-24T01:07:00Z
- **Observed elapsed minutes:** 42.5
- **Target status:** MET_TARGET
- **Exceedance causes:** None
- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Unavailable records | Known input tokens | Known output tokens | Known total tokens | Known token cost (USD) | Complete estimated token cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 | 3 | 0 | 0 | 0 | 0.000000 | __ |
| gpt-5.6-terra | 12 | 12 | 0 | 0 | 0 | 0.000000 | __ |

Per-agent accounting detail will be in [token_usage_ledger.csv](review_1_5_2/token_usage_ledger.csv); calculated per-model totals will be in [token_usage_summary.md](review_1_5_2/token_usage_summary.md). Cached input and cache-write counts are input subsets; reasoning counts are output subsets and are not added to total tokens. All amounts are token-only API-equivalent estimates under the dated local price snapshot, not invoices.
