# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a determination of paper validity or a finding about authors or conclusions.

## Executive Quality-Control Summary

Complete mapping of the five supplied PDFs identified five stable quantitative reporting-quality candidates: three visibly incomplete PPV-difference cells, one visibly incomplete cutoff header, and one repeated cutoff expression lacking an explicit microgram prefix. The review found no coherent display-zero P-value candidate. The cards retain direct observations, diagnostic calculations where appropriate, source-grounded alternatives, and the remaining question for human review.

Small preventable reporting defects can matter for downstream evidence extraction if confirmed. The supplied package does not establish propagation, a change in any conclusion, or serious harm.

## Package and Reused-Evidence Provenance

The direct-source inventory covers five PDFs and 88 PDF pages: [jama_brenner_2019_oi_190039.pdf](<../jama_brenner_2019_oi_190039.pdf#page=1>) (DOC-001, 7 pages), [joi190039supp1_prod.pdf](<../joi190039supp1_prod.pdf#page=1>) (DOC-002, 62 pages), [joi190039supp2_prod.pdf](<../joi190039supp2_prod.pdf#page=1>) (DOC-003, 10 pages), [joi190039supp3_prod.pdf](<../joi190039supp3_prod.pdf#page=1>) (DOC-004, 8 pages), and [joi190039supp4_prod.pdf](<../joi190039supp4_prod.pdf#page=1>) (DOC-005, 1 page).

Direct PDFs were the evidence authority. Reused native/layout text, OCR, rendered pages, document maps, and table locators were used only for location and transcription support. The reusable-asset inventory records 90 hashed assets: 12 usable unique page units, seven targeted rendered-page units, and stale/partial derivatives retained as provenance. The full inventories and baseline hashes are in [source_inventory.md](review_1_5_1/source_inventory.md), [evidence_asset_inventory.md](review_1_5_1/evidence_asset_inventory.md), [source_hashes_before.sha256](review_1_5_1/source_hashes_before.sha256), and [reused_artifact_hashes_before.sha256](review_1_5_1/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

All 88 direct PDF-page units were mapped. Reusable and fresh-required units partition each source, and mapped units equal total units.

| Source ID | Source | Total | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_brenner_2019_oi_190039.pdf | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-002 | joi190039supp1_prod.pdf | 62 | 0 | 62 | 62 | COMPLETE |
| DOC-003 | joi190039supp2_prod.pdf | 10 | 0 | 10 | 10 | COMPLETE |
| DOC-004 | joi190039supp3_prod.pdf | 8 | 5 | 3 | 8 | COMPLETE |
| DOC-005 | joi190039supp4_prod.pdf | 1 | 0 | 1 | 1 | COMPLETE |
| **Total** | **Five supplied PDFs** | **88** | **12** | **76** | **88** | **COMPLETE** |

The review covered numeric arithmetic, denominators and percentages, labels and scales, matched cross-document values, and supplied inferential relationships. It did not conduct a raw-data, clinical, misconduct, novelty, or external-literature review. No web source was used. The current review had no review queue, count cap, deferred-by-cap section, or top-N subset.

## Quantitative and Statistical Relationship Coverage

The quantitative map contains 62 stable numeric/reporting relationships, N001-N062. The statistical inventory contains 23 stable inferential/statistical relationships, S001-S023. The numeric checker, cross-source checker, and direct-PDF recheck were complete. Details are retained in [numeric_relationship_inventory.md](review_1_5_1/relationships/numeric_relationship_inventory.md), [numeric_consistency.md](review_1_5_1/checkers/numeric_consistency.md), and [cross_source_consistency.md](review_1_5_1/checkers/cross_source_consistency.md).

Two independent fresh high-effort statistical passes each explicitly completed S001-S023. Pass 1 registered the source-grounded unit-label proposal that became C005; pass 2 reviewed all stable candidates and added none. Both passes treated unavailable row-level test definitions as limitations rather than reconstructing unsupported inferential quantities. See [relationship_inventory.md](review_1_5_1/statistics/relationship_inventory.md), [statistical_pass_1.md](review_1_5_1/checkers/statistical_pass_1.md), and [statistical_pass_2.md](review_1_5_1/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Candidate | Category | Status |
|---|---|---|---|
| C001 | Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C002 | Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C003 | Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| C004 | eTable 5 visible cutoff header truncates after `[µg` | Measure, label, or scale inconsistency | Pending Human Adjudication |
| C005 | One SAP occurrence omits the microgram prefix from the 10.2 cutoff | Measure, label, or scale inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent

**Candidate statement:** In the Women/Quantitative/10.2 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi190039supp3_prod.pdf — PDF p. 7](<../joi190039supp3_prod.pdf#page=7>), DOC-004 eTable 5, Women/Quantitative/10.2, Difference in PPV; comparator [joi190039supp3_prod.pdf — PDF p. 6](<../joi190039supp3_prod.pdf#page=6>), DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis.

**Source evidence:** Page 7 visibly prints aspirin PPV 15.9%, placebo PPV 34.1%, a lone hyphen in the point-estimate position, and 95% CI [-34.7, -1.3]. Page 6 prints TP/FP 11/58 for aspirin and 14/27 for placebo.

**Reported-versus-comparator:** The reported cell is `-` versus a numeric aspirin-minus-placebo PPV difference that is diagnostically supported by the matched counts and displayed arm PPVs; no numeric magnitude is visibly rendered in the cell.

**Reasoning procedure:** Confirm the matched row identity and contrast direction, then compare the visible incomplete cell with PPVs derived from eTable 4 counts. The calculation is diagnostic, not a prescribed correction, because exact unrounded output and the table-rendering convention are not supplied.

**Calculation:** `11/(11+58) × 100 = 15.9420%`; `14/(14+27) × 100 = 34.1463%`; aspirin minus placebo = `-18.2043` percentage points, rounding to `-18.2`. The displayed values also give `15.9 - 34.1 = -18.2`.

**Alternative source-grounded interpretations:** A detached `18.2` PDF text fragment may indicate displaced, clipped, or suppressed table content, but the direct rendering does not visibly connect it to the cell. Alternatively, an undocumented hyphen-only convention may have been intended.

**Mechanical evidence recheck:** Location, printed values, comparator counts, contrast rule, and diagnostic calculation were reproduced directly from the supplied pages. Exact unrounded analysis output and an explicit dash/rendering convention are missing; direct observation is separated from the possible production explanation in [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md).

**Quality-control relevance:** A named difference column with arm values and a confidence interval but no visible point-estimate magnitude is an incomplete quantitative display requiring human confirmation.

**Potential downstream evidence impact:** If confirmed, a data extractor or later evidence synthesis could record a missing PPV difference or reconstruct it inconsistently. The package does not show that this occurred or changed a conclusion.

**Human verification steps:** Open the cited PDF pages; confirm the hyphen, CI, and matched count row; then inspect author-approved table output or analysis records for the intended estimate and any dash convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent

**Candidate statement:** In the Women/Quantitative/17.0 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi190039supp3_prod.pdf — PDF p. 7](<../joi190039supp3_prod.pdf#page=7>), DOC-004 eTable 5, Women/Quantitative/17.0, Difference in PPV; comparator [joi190039supp3_prod.pdf — PDF p. 6](<../joi190039supp3_prod.pdf#page=6>), DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis.

**Source evidence:** Page 7 visibly prints aspirin PPV 17.1%, placebo PPV 42.9%, a lone hyphen in the point-estimate position, and 95% CI [-48.4, -0.7]. Page 6 prints TP/FP 6/29 for aspirin and 9/12 for placebo.

**Reported-versus-comparator:** The reported cell is `-` versus a count-derived diagnostic difference that rounds to -25.7 percentage points; subtracting the independently rounded printed PPVs gives -25.8. Neither numeric value is visibly printed in the named cell.

**Reasoning procedure:** Match the row and contrast, reproduce PPV from the source counts, and separately subtract the displayed one-decimal PPVs. These are diagnostics, not prescribed corrections: the unrounded analysis output and point-estimate rounding basis are absent.

**Calculation:** `6/(6+29) × 100 = 17.1429%`; `9/(9+12) × 100 = 42.8571%`; count-derived aspirin minus placebo = `-25.7143`, rounding to `-25.7` percentage points. Displayed-value subtraction is `17.1 - 42.9 = -25.8`; the 0.1-point difference is compatible with rounding paths.

**Alternative source-grounded interpretations:** A detached `25.7` PDF text fragment may indicate displaced, clipped, or suppressed content, but it is not visible in the cell. The intended display may have used unrounded proportions, or the hyphen may represent an undocumented convention.

**Mechanical evidence recheck:** Direct rendering confirmed the cited cell, CI, comparator counts, and matched identity. The calculation was reproduced; missing inputs are the unrounded analysis output, intended rounding basis, and rendering convention. See [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md).

**Quality-control relevance:** The table visibly lacks the numeric magnitude for a specified comparative PPV result, even though the arm values and interval are presented.

**Potential downstream evidence impact:** If confirmed, a downstream extractor could enter a missing value or use different rounding when reconstructing the difference. Neither propagation nor conclusion change is established.

**Human verification steps:** Inspect the cited pages and the source analysis/table-production output to determine the intended signed estimate, rounding basis, and whether a hyphen-only display rule exists.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent

**Candidate statement:** In the Women/Qualitative/10.2 row of eTable 5, the Difference in PPV point-estimate position visibly contains only a hyphen although both arm PPVs and a negative confidence interval are printed.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi190039supp3_prod.pdf — PDF p. 7](<../joi190039supp3_prod.pdf#page=7>), DOC-004 eTable 5, Women/Qualitative/10.2, Difference in PPV; comparator [joi190039supp3_prod.pdf — PDF p. 6](<../joi190039supp3_prod.pdf#page=6>), DOC-004 eTable 4, same population, test, cutoff, day, and per-protocol analysis.

**Source evidence:** Page 7 visibly prints aspirin PPV 9.7%, placebo PPV 31.2%, a lone hyphen in the point-estimate position, and 95% CI [-38.9, -3.9]. Page 6 prints TP/FP 6/56 for aspirin and 10/22 for placebo.

**Reported-versus-comparator:** The reported cell is `-` versus a count-derived diagnostic difference that rounds to -21.6 percentage points; displayed-value subtraction gives -21.5. No numeric magnitude is visibly printed in the cell.

**Reasoning procedure:** Confirm the matched qualitative-test row and contrast, then compute PPV from the source confusion-matrix counts and compare this diagnostic result with the rounded displayed values. It is not a prescribed correction because the unrounded output and rendering convention are unavailable.

**Calculation:** `6/(6+56) × 100 = 9.6774%`; `10/(10+22) × 100 = 31.2500%`; count-derived aspirin minus placebo = `-21.5726`, rounding to `-21.6` percentage points. Displayed-value subtraction is `9.7 - 31.2 = -21.5`; the difference is compatible with independent rounding.

**Alternative source-grounded interpretations:** A detached `21.6` PDF text fragment may reflect displacement, clipping, or suppression during production without establishing that mechanism. The hyphen could instead be an undocumented display convention.

**Mechanical evidence recheck:** The direct pages support the visible hyphen, arm values, interval, counts, and diagnostic arithmetic. Exact unrounded output, intended rounding basis, and table convention remain missing. See [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md).

**Quality-control relevance:** The row presents a confidence interval for a specified PPV comparison but no visibly rendered numeric point estimate.

**Potential downstream evidence impact:** If confirmed, quantitative evidence extraction could treat this as missing or reconstruct it under a different rounding path. The supplied materials do not establish downstream use or conclusion impact.

**Human verification steps:** Verify the source cells and counts on the cited pages, then consult the approved table source or analysis output for the intended estimate and display convention.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTable 5 visible cutoff header truncates after `[µg`

**Candidate statement:** eTable 5 visibly renders `Cutoff` and a second-line `[µg` fragment, without visibly rendered `Hb/g]`, while matched cutoff displays use the full µg Hb/g scale.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi190039supp3_prod.pdf — PDF p. 7](<../joi190039supp3_prod.pdf#page=7>), DOC-004 eTable 5 visible cutoff header; comparator [joi190039supp3_prod.pdf — PDF p. 6](<../joi190039supp3_prod.pdf#page=6>), DOC-004 eTable 4 header `Cutoff [µg Hb/g]`; additional matched main-table display [jama_brenner_2019_oi_190039.pdf — PDF p. 5](<../jama_brenner_2019_oi_190039.pdf#page=5>).

**Source evidence:** The direct rendering on page 7 visibly shows `Cutoff` and `[µg`; neither `Hb/g` nor the closing bracket is visibly rendered. The same page applies cutoff values 10.2 and 17.0. Page 6 visibly renders `Cutoff [µg Hb/g]` for the corresponding day-2 per-protocol FIT context.

**Reported-versus-comparator:** The visible eTable 5 label ends at `[µg` versus the matched eTable 4 and main-table concentration scale `µg Hb/g`. The incomplete string is the direct observation; the complete form is the comparator, not an asserted transcription of page 7.

**Reasoning procedure:** Align cutoff values, tests, day, and analysis context across eTables 4 and 5. Compare their dimensional labels: outcome columns differ, but the cutoff scale should remain the same for the matched test values.

**Calculation:** No arithmetic is applicable. The reproducible comparison is the visible incomplete mass-unit fragment `[µg` against the matched mass-per-mass scale `µg Hb/g`.

**Alternative source-grounded interpretations:** A detached `Hb/g]` PDF text fragment supports a possible layout or clipping explanation but is not visibly connected to the header. Readers may have been expected to carry the unit from adjacent tables, although the page gives no such instruction.

**Mechanical evidence recheck:** Direct rendering confirmed the incomplete header, exact comparator headers, matched cutoff values, and the absence of a printed inheritance note. The text fragment is retained as a source-grounded alternative, not as proof of a production mechanism. See [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md).

**Quality-control relevance:** A visibly incomplete unit label can obscure whether a cutoff is a mass value or a mass-per-mass concentration scale.

**Potential downstream evidence impact:** If confirmed, an extractor could omit the denominator or transcribe the cutoff as mass-only when reusing PPV/NPV data. The package does not show a changed analytical scale, propagation, or conclusion change.

**Human verification steps:** Inspect the directly rendered headers on pages 6-7 and the author-approved supplement table source or legend to determine whether the full cutoff scale should render in eTable 5.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — One SAP occurrence omits the microgram prefix from the 10.2 cutoff

**Candidate statement:** One SAP sentence prints `17 μg Hb/g feces and 10.2 Hb/g feces`, while matched occurrences specify the lower cutoff as `10.2 μg Hb/g feces`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi190039supp2_prod.pdf — PDF p. 6](<../joi190039supp2_prod.pdf#page=6>), DOC-003 §3.2; comparator [joi190039supp2_prod.pdf — PDF p. 8](<../joi190039supp2_prod.pdf#page=8>), DOC-003 §5.4; matched context [jama_brenner_2019_oi_190039.pdf — PDF p. 1](<../jama_brenner_2019_oi_190039.pdf#page=1>) and [jama_brenner_2019_oi_190039.pdf — PDF p. 5](<../jama_brenner_2019_oi_190039.pdf#page=5>).

**Source evidence:** DOC-003 p. 6 visibly prints `17 μg Hb/g feces and 10.2 Hb/g feces`. DOC-003 p. 8 prints `Manufacturer’s threshold (17 μg Hb/g feces)` and `threshold for positivity (10.2 μg Hb/g feces)`. The article supplies the same two FIT-cutoff context and complete unit headers.

**Reported-versus-comparator:** The lower cutoff is printed as `10.2 Hb/g feces` on p. 6 versus `10.2 μg Hb/g feces` on p. 8 for the same lower quantitative-FIT threshold.

**Reasoning procedure:** Match the numerical threshold, test context, and repeated definition, then compare whether the numerator-unit prefix is retained. This is a source-label comparison, not a conversion or assertion that the analyzed scale changed.

**Calculation:** No arithmetic is required. The logical comparison checks whether the same 10.2 cutoff retains its `μg` numerator unit across the matched SAP occurrences.

**Alternative source-grounded interpretations:** The first `μg` may be intended to govern both coordinated thresholds grammatically. Because `Hb/g feces` is repeated after both numbers, that inheritance is not explicit; the package gives no editorial rule resolving it.

**Mechanical evidence recheck:** Direct PDF inspection reproduced both SAP phrases and the matched article context. The necessary source text is available; the missing definition is an explicit unit-inheritance convention. See [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md).

**Quality-control relevance:** Repeated cutoff labels should make the unit scale unambiguous where they are reused in analytical definitions.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the lower cutoff without its microgram prefix or interpret the repeated expression inconsistently. No downstream propagation, altered result, or conclusion change is established.

**Human verification steps:** Compare the cited SAP sections and article tables, then consult the approved SAP source or editorial guidance to determine whether `μg` was intentionally shared or should be printed locally.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these are bounded reporting-quality issues relevant to extraction of PPV differences or FIT cutoff units. They could affect how a systematic review, meta-analysis, guideline, or data-extraction workflow transcribes a value or label. This report does not claim that any such reuse occurred, that results propagated, or that the paper’s conclusions changed.

## Limitations and Missing Definitions

The complete limitations record is in [limitations.md](review_1_5_1/limitations.md). In brief, raw participant-level data, exact unrounded PPV-difference output, author-approved table-production files, a dash/rendering convention, and an explicit unit-inheritance convention are not supplied. These missing inputs constrain interpretation but do not leave a scientific-coverage gap: all 76 fresh-required pages were directly mapped. Inferential reviewers did not impose unsupported P-value, CI, or test reconstructions where required definitions were absent.

## Human Adjudication Checklist

For each card, confirm the direct source rendering, exact matched comparator, and identity of population, test, cutoff, time point, and contrast. Then inspect author-approved analysis or production records where the card identifies missing output or a possible rendering convention. Record the human decision only in the blank fields on the corresponding card; retain the diagnostic-versus-observed distinction and do not infer a conclusion effect from these quality-control observations alone.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The source and reused-asset baseline hash inventories are linked above. The evidence-quality audit reports that all five direct-source hashes and all 90 reused-artifact hashes reproduced their baselines before final report assembly. Mapping, coverage, recheck, and audit provenance are preserved in [coverage_manifest.md](review_1_5_1/coverage_manifest.md), [source_coverage.md](review_1_5_1/source_coverage.md), [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md), and [evidence_quality_audit.md](review_1_5_1/quality/evidence_quality_audit.md).

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |

### Reproducibility performance

- **Target basis:** Five-PDF package with 88 total PDF-page units, 76 fresh-required pages, one 62-page technical supplement, and expected table/statistical cross-source complexity; closely comparable but slightly smaller than the 102-total/81-fresh calibration package.
- **Total source units:** 88
- **Fresh-source units:** 76
- **Target elapsed minutes:** 35-50
- **Started UTC:** 2026-08-18T22:12:56Z
- **Finished UTC:** 2026-08-18T22:48:09Z
- **Observed elapsed minutes:** 35.2
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting

The runtime did not expose authoritative response-level token counts for the coordinator or any specialist, so each manifested agent has an `UNAVAILABLE` ledger row and no text-length estimate was substituted. The known subtotal is therefore zero while the complete package count and price remain explicitly unavailable. Cached input and cache-write tokens are input subsets, and reasoning tokens are an output subset; none is added again to total tokens. Per-agent detail is retained in [token_usage_summary.md](review_1_5_1/token_usage_summary.md).

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 known; complete estimate unavailable |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 known; complete estimate unavailable |

All amounts are token-only API-equivalent estimates under the pricing snapshot dated 2026-08-18 UTC, not invoices; non-token tools, containers, storage, subscriptions, taxes, and other charges are outside the estimate.
