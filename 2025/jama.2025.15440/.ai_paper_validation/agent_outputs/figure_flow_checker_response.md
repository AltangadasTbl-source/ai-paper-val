# Figure and Participant-Flow Check

- Scope: `doc_001_main_article`, PDF pages 1-8, and `doc_004_results_supplement`, PDF pages 1 and 4-11.
- Visual review: main Figure 1, Table, and Figures 2-4; supplementary eTables 1-3 and eFigures 1-4.
- Excluded by design: protocol, SAP, administrative material, and results-supplement pages 2-3.
- External sources: none.

## Retained candidates

### FFC-01 - Statistical reporting inconsistency - high confidence

- **File and location:** `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, structured abstract Results, PDF p. 1; Results text, PDF p. 5; Figure 4B ("Death and stroke"), PDF p. 7.
- **Visible evidence:** The abstract reports any stroke in 69 patch-group participants (2.7%) and 64 usual-care participants (2.5%), rate ratio 1.08 with 95% CI **0.76-1.53**. Figure 4B displays the same event counts and point estimate but a 95% CI of **0.77-1.51**. The nearby Results text on p. 5 also gives **0.77-1.51**.
- **Logical basis:** The same outcome, event counts, point estimate, and 2.5-year comparison are accompanied by two different confidence intervals. Both CI limits differ, so this is not only a formatting difference.
- **Verification instruction:** Compare the "Stroke occurred..." sentence in the p. 1 abstract with the "Any stroke" row of Figure 4B on p. 7 and the final Results paragraph on p. 5; confirm which CI is the intended time-to-event estimate.

### FFC-02 - Participant flow inconsistency - moderate confidence

- **File and location:** `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, Figure 1, PDF p. 4.
- **Visible evidence:** Figure 1 shows an estimated **368,000 assessed for eligibility**, followed directly by **22,044 invited**, with no count for the **345,956** not invited. It then shows 22,044 invited minus 1,186 practice-level exclusions = **20,858 included**, followed by **5,116 replies received**, but no box for the **15,742** included/invited individuals from whom no reply was received. The displayed later transition is complete: 5,116 replies minus 76 exclusions = 5,040 randomized.
- **Logical basis:** Two large losses between displayed flow nodes are not explicitly accounted for, although smaller exclusions are shown. This is a participant-flow reporting omission, not a claim that the randomized total is arithmetically wrong.
- **Verification instruction:** Trace every Figure 1 arrow and reconcile consecutive displayed nodes. Confirm whether the source materials define the unshown 345,956 and 15,742 categories or whether Figure 1 should explicitly label "not eligible/not invited" and "no reply."

## Uncertain candidate - do not retain without adjudication

### FFC-U01 - Presentation inconsistency - semantic ambiguity

- **File and location:** `joi250068supp3_prod_1760999665.30362.pdf`, eFigure 1 caption, PDF p. 8; main article Methods, PDF p. 3; main Figure 2, PDF p. 6.
- **Visible evidence:** Supplementary eFigure 1 explicitly plots the sensitivity outcome of a **primary- or secondary-care** AF record and reports an overall ratio of proportions **1.21 (95% CI 1.02-1.45)**. Its caption says, "The primary outcome of ratio of proportions overall is represented by a diamond." The article defines the trial primary outcome as AF in **primary-care records** only; main Figure 2 reports that result as **1.26 (95% CI 1.02-1.57)**.
- **Reason for uncertainty:** "Primary outcome" in the eFigure caption may be copied trial-outcome terminology, but it could also be intended only to describe the overall row/diamond within that sensitivity figure. The text is potentially misleading but not an unambiguous numerical contradiction.
- **Verification instruction:** Ask the authors whether "primary outcome" in the eFigure 1 caption is intended to mean the trial primary outcome; if not, revise it to "overall estimate" or "sensitivity-analysis outcome."

## Rejected checks

- **Figure 1 deaths versus Figure 4B:** Figure 1 shows 98 and 118 deaths within the complete-primary-care-follow-up boxes, whereas Figure 4B shows 103 and 126 total deaths. Rejected as a contradiction because Figure 1's counts are nested within the 2,408 and 2,410 complete-primary-care subsets, while Figure 4B reports all randomized participants using death records.
- **Supplement p. 7 malformed title/row spacing in the retained preprocessor PNG:** Rejected as a source-document issue. An independent source-PDF render displayed eTable 3 normally; the defect is confined to the derived PNG.
- **Risk sets:** Main Figures 3 and 4A and supplementary eFigure 3 show monotone, denominator-compatible risk sets. No document-verifiable mismatch with the stated events or nearby text was identified.
- **Patch rhythm figures:** eFigure 2 panel D percentages 9% + 29% + 20% + 42% = 100%; eFigure 4 panel D percentages 10% + 26% + 18% + 46% = 100%. Their labels and the main-text AF-duration claims agree.
