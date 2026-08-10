# Table arithmetic and internal-consistency check

**Scope.** Result-relevant tables named in the package manifest and evidence maps only: main-article Tables 1-3 and Supplement 2 eTables 1-6. No protocol/SAP material or external sources were used. Source PDFs were not modified.

## Candidate issues for verification

### TAC-01 — Baseline dependence-index denominators disagree across the main article and eTable 4

- **Category:** Cross-document inconsistency
- **Locations:** Main article PDF p. 4 (printed p. 716), Table 1, `PSECDI, mean (SD)` and `e-FTCD, mean (SD)`; Supplement 2 PDF p. 13, eTable 4 (continued), the same two rows. Source artifacts: [main p4 text](../document_outputs/D001_main_article/preprocessing/native_text/page_004.txt), [main p4 image](../document_outputs/D001_main_article/preprocessing/page_images/page_004.png), [supplement p13 text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_013.txt), [supplement p13 image](../document_outputs/D003_results_supplement/preprocessing/page_images/page_013.png).
- **Source values:** Table 1 gives `n=733` intervention and `n=727` assessment-only control for both indices. eTable 4 gives `n=428` among non-responders and `n=1,025` among responders for both indices. eTable 4's columns explicitly partition the same randomized two-arm sample (`439 + 1,064 = 1,503`).
- **Calculation:** `733 + 727 = 1,460`; `428 + 1,025 = 1,453`; difference `1,460 - 1,453 = 7` participants, for each index. By contrast, eTable 4's other categorical baseline variables reproduce the corresponding Table 1 totals (for example, PEARLS: `631 + 617 = 362 + 886 = 1,248`), making this a localized discrepancy.
- **Reasoning:** Both displays identify the same baseline indices and the same two-arm population, but show incompatible visible nonmissing denominators without an explanation of a distinct analytic subset.
- **Verification instruction:** Confirm whether seven index observations were intentionally excluded only from eTable 4 and, if so, add the analytic-denominator rationale; otherwise reconcile the printed `n` values.

### TAC-02 — eTable 4 labels fractional values as medians (IQR) on a 1-to-5 scale

- **Category:** Presentation inconsistency
- **Location:** Supplement 2 PDF p. 12, eTable 4, `Motivation to quit vaping, median (IQR)` and `Confidence to quit vaping, median (IQR)`; footnote b. Source artifacts: [p12 text](../document_outputs/D003_results_supplement/preprocessing/native_text/page_012.txt), [p12 image](../document_outputs/D003_results_supplement/preprocessing/page_images/page_012.png).
- **Source values:** The table labels the rows as `median (IQR)` and reports motivation as `4.1 (0.8)` in non-responders (`n=439`) and responders (`n=1,064`); it reports confidence as `3.2 (1.1)` and `3.5 (1.1)`, respectively. Footnote b specifies the measures' 1-to-5 response range. The main article's Table 1 presents the same measures as integer-valued medians with IQRs, e.g., motivation `4.0 (4.0-5.0)` and confidence `3.0 (3.0-4.0)`.
- **Calculation / logical check:** For an odd-sized non-responder group (`n=439`), a median of an integer-coded 1-to-5 item must be one of 1, 2, 3, 4, or 5; the displayed medians `4.1` and `3.2` cannot be such medians. For the responder group (`n=1,064`), averaging two ordered integer middle values can produce only an integer or a half-integer, so `4.1` and `3.5` cannot both be medians (`3.5` is possible; `4.1` is not). The displayed form instead resembles mean (SD).
- **Reasoning:** The label and values are internally incompatible; either the summary-statistic label is wrong or one or more displayed statistics is wrong. This is a presentation issue, not a claim about the underlying data.
- **Verification instruction:** Check the analysis output for these two variables and relabel them `mean (SD)` if those are means, or replace the values with the intended medians and IQRs.

## Checks completed with no candidate issue

- **Main Table 1 and Supplement eTables 1, 2, and 4 categorical blocks:** visible category counts equal their printed nonmissing denominators and percentages round correctly. Examples: main Table 1 race: `11+16+76+3+469+139+34=748` and control `=737`; eTable 2 waitlist grade: `0+7+30+62+70+4+4=177`; eTable 4 gender: `254+153+29=436` and `501+475+81=1,057`.
- **Main Table 2 and Supplement eTable 5:** the unweighted primary and repeated-outcome cells reconcile to their visible counts. Examples: `287/759=37.81% -> 37.8%`, `208/744=27.96% -> 28.0%`, `131/759=17.26% -> 17.3%`, and `61/744=8.20% -> 8.2%`; the displayed rate differences, RRs, and raw-rate odds ratios round compatibly.
- **Main Table 3:** all four outcome columns sum to each displayed analytic subgroup; the two treatment rows sum to the full analytic sample (`501+515=1,016`), and the baseline subgroup rows sum to their treatment totals (`300+201=501`; `298+217=515`). Percentages round correctly.
- **Supplement eTable 3:** for each visible row, `Diff.vape=P1-P0`; the displayed RRs and ORs round compatibly with P1 and P0. Example MAR row: `52.26-40.48=11.78` percentage points, which rounds to `11.79` given underlying unrounded values; `52.26/40.48=1.291` -> `1.29`.
- **Supplement eTable 6:** displayed nominal P values are compatible with beta/SE rounding for checked entries (for example, racial minority: `.514/.227=2.26`, two-sided normal P approximately `.024`).

## Rejected / uncertain lead (not a candidate)

- **eTable 5, 30-day ppa IPRW odds-ratio CI:** the printed OR is `1.92 (95% CI, 1.50-2.24)`. Its log-scale interval is asymmetric around the point estimate, unlike nearby conventional intervals, but the table does not state the CI construction method and the weighted analysis cannot be reconstructed from visible data. It is therefore **not reported as an issue**; no error should be inferred without the analysis output.

