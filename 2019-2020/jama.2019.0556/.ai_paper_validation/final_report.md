# Human Adjudication Report

**Package:** `jama.2019.0556`  
**Submission status:** **Human Adjudication**

## Scope and provenance

- Scientific audit scope: `DOC-001` main article result-relevant pages and `DOC-004` results-supplement PDF pages 16–23. Pages 1–2 of `DOC-004` were retained only for document labels/context.
- `DOC-002` protocol, `DOC-003` statistical analysis plan, and `DOC-005` administrative/data-sharing statement were **Not Audited by Design** for scientific reporting issues.
- Preprocessing used `/usr/bin/python3` with a workspace-local Tesseract 5.5.0 runtime. The validated backend was `tesseract-cpu`.
- Fresh OCR was performed through `scripts/ocr_page.py` for `DOC-001` PDF pages 3 and 5–8 and `DOC-004` PDF pages 16–23. Native text was retained.
- SHA-256 rechecks confirmed that all five source PDFs were unchanged.
- The audit used only the supplied article package. No web search or external scientific evidence was used.

## AI Training Restriction Summary

This is a separate document-content compliance screen, not a scientific reporting-error category and not legal advice. Silence is not treated as permission.

| Document ID | Filename | Status | Exact evidence location and quoted language | Human Compliance Review |
|---|---|---|---|---|
| `DOC-001` | `jama_bot_2019_oi_190007.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1: “© 2019 American Medical Association. All rights reserved.” No AI-training, fine-tuning, model-improvement, or TDM clause was located in the supplied file or metadata. | No |
| `DOC-002` | `joi190007supp1_prod.pdf` | No AI Training Restriction Located in Provided Materials | Entire supplied PDF and available embedded metadata searched; no rights or AI-use wording was located. | No |
| `DOC-003` | `joi190007supp2_prod.pdf` | No AI Training Restriction Located in Provided Materials | Entire supplied PDF and available embedded metadata searched; no rights or AI-use wording was located. | No |
| `DOC-004` | `joi190007supp3_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1: “© 2019 American Medical Association. All rights reserved.” No AI-training, fine-tuning, model-improvement, or TDM clause was located in the supplied file or metadata. | No |
| `DOC-005` | `joi190007supp4_prod.pdf` | Conditional / Permission Required | PDF p. 1, “Additional Information”: “researchers whose proposed use of the data has been approved” and “data can only be used for the analysis outlined in the approved analysis plan.” The condition applies to underlying study-data access/use, is not AI-specific, and does not state a restriction on the supplied PDF text. | **Yes**—before AI-training or model-improvement use of the underlying study data. |

## Scientific issue summary

Four verified minor issues were retained after one evidence-verification stage and one critic stage. None changes a reported participant total, outcome estimate, or stated interpretation on the supplied evidence.

| Issue | Category | Severity | Document and location |
|---|---|---|---|
| Table 2 footnote assigns 22 events to the wrong treatment label | Presentation inconsistency | Minor | `DOC-001`, PDF p. 6, Table 2, footnote d |
| Baseline GAD-7 P value is displayed as zero | Statistical reporting inconsistency | Minor | `DOC-004`, PDF p. 19, eAppendix 10B |
| Two country subgroup tables share identifier C2 | Presentation inconsistency | Minor | `DOC-004`, PDF p. 20, eAppendix 10 |
| eAppendix 8 markers do not correspond to their footnote subjects | Presentation inconsistency | Minor | `DOC-004`, PDF p. 16, eAppendix 8 |

## Issue 1 — Table 2 footnote assigns 22 events to the wrong treatment group

**Issue statement:** Table 2 footnote d labels both component supplement groups “without therapy,” although 22/256 is assigned elsewhere to supplements with therapy.

**Category:** Presentation inconsistency  
**Severity:** Minor

**Locations**

- `DOC-001`, `jama_bot_2019_oi_190007.pdf`, PDF p. 6, Table 2, Supplements row and footnotes d and f.
- `DOC-001`, same file, PDF p. 7, Results, “Onset of MDD,” first paragraph.

**Reported item**

- Footnote d: “Thirty-two of 256 participants (12.5%) in the supplements without therapy group and 22 of 256 (8.6%) in the supplements without therapy group.”

**Comparator**

- Footnote f: “22 of 256 (8.6%) in the supplements with therapy group.”
- PDF p. 7 Results: “32 (12.5%) receiving supplements alone, and 22 (8.6%) receiving supplements with therapy.”

**Reproducible check**

- `32 / 256 × 100 = 12.5%`.
- `22 / 256 × 100 = 8.59375%`, which rounds to `8.6%` at one decimal place.
- `32 + 22 = 54`, matching Table 2’s pooled supplement-event total.
- The values reconcile as two distinct supplement cells: 32 without therapy and 22 with therapy. Repeating “without therapy” for both is therefore a label error, not a numerical discrepancy.

**Rounding tolerance:** Percentages agree at one decimal place; rounding cannot resolve the label discrepancy.

**Bounded impact:** The footnote misidentifies the arm contributing 22 events. Counts, percentages, pooled total, and model estimate are unaffected.

**Human verification**

1. Confirm that footnote d on PDF p. 6 uses “supplements without therapy” twice.
2. Confirm that footnote f and the PDF p. 7 Results assign 22/256 to supplements with therapy.
3. The issue is confirmed if the second label in footnote d is the only conflicting assignment; changing it to “with therapy” resolves it.

## Issue 2 — Baseline GAD-7 P value is displayed as zero

**Issue statement:** eAppendix 10B displays `P = 0` for Baseline GAD-7, whereas the finite estimate and confidence interval support threshold notation and neighboring tables use `P < .001`.

**Category:** Statistical reporting inconsistency  
**Severity:** Minor

**Locations**

- `DOC-004`, `joi190007supp3_prod.pdf`, PDF p. 19, eAppendix 10B, “Baseline GAD-7” row, B/95% CI/P columns.
- Comparator formatting: `DOC-004`, PDF p. 18, eAppendix 10A, “Baseline PHQ-9” row; PDF p. 20, eAppendix 10C1, “Baseline health utility” row.

**Reported values**

- Baseline GAD-7: `B = 0.464`; `95% CI, 0.409 to 0.52`; `P = 0`.

**Comparator values**

- Baseline PHQ-9 and Baseline health utility are both reported as `P < .001`.

**Reproducible conservative calculation**

- Approximate standard error under a symmetric-normal 95% CI:
  `SE ≈ (0.520 − 0.409) / (2 × 1.96) = 0.0283`.
- Approximate test statistic:
  `z ≈ 0.464 / 0.0283 = 16.4`.
- Allowing rounding of `B` and the CI endpoints, including ±0.005 for the displayed upper endpoint `0.52`, gives a maximum approximate `SE = (0.525 − 0.4085) / 3.92 = 0.0297` and a minimum `z = 0.4635 / 0.0297 ≈ 15.6`.
- These rounded inputs conservatively support only `P < .001`; the exact P value cannot be reconstructed from the published entries.

**Rounding tolerance:** Explicitly included above. Rounding prevents recovery of an exact P value but does not justify literal zero.

**Bounded impact:** Only the P-value display for an adjustment covariate is affected. Its significance, direction, the supplement-by-baseline-GAD interaction, and intervention conclusions are unchanged.

**Human verification**

1. Confirm the literal `0` in the P column on PDF p. 19.
2. Confirm neighboring `<0.001` notation on PDF pp. 18 and 20.
3. Check the unrounded model output and intended formatting.
4. A positive P value displayed as an appropriate threshold confirms the correction; contrary unrounded analysis output would resolve the issue.

## Issue 3 — Two country subgroup tables share identifier C2

**Issue statement:** eAppendix 10 labels both the United Kingdom and Netherlands subgroup tables `C2`.

**Category:** Presentation inconsistency  
**Severity:** Minor

**Location:** `DOC-004`, `joi190007supp3_prod.pdf`, PDF p. 20, eAppendix 10, the two subgroup headings following Table C1.

**Reported item**

- “C2. Subgroup analysis for United Kingdom for health utility score after 12-month follow-up.”

**Comparator**

- “C2. Subgroup analysis for the Netherlands for health utility score after 12-month follow-up.”

**Reproducible logical check:** The country headings and different coefficient rows establish that these are distinct tables, yet both carry the same identifier. No calculation or rounding tolerance applies.

**Bounded impact:** References to “C2” are ambiguous; country attribution and numerical estimates remain visible and unchanged. The supplied evidence does not establish the intended replacement identifier.

**Human verification**

1. Confirm both headings on PDF p. 20.
2. Confirm that the tables contain different country-specific results.
3. Duplicate visible identifiers confirm the issue; consult the source/layout record to determine the intended corrected label.

## Issue 4 — eAppendix 8 footnote markers do not correspond to their subjects

**Issue statement:** Four adherence rows carry `*` although the `*` note describes the unmarked Morisky row, while the Kappa `**` note has no visible corresponding marker.

**Category:** Presentation inconsistency  
**Severity:** Minor

**Location:** `DOC-004`, `joi190007supp3_prod.pdf`, PDF p. 16, eAppendix 8, Adherence rows and footnotes.

**Marked rows**

- “Multinutrient adherence ≥70% from pill weight*”
- “Multinutrient adherence ≥70% from self-report*”
- “Omega adherence ≥70% from pill weight*”
- “Omega adherence ≥70% from self-report *”

**Unmarked comparator**

- “Morisky score (average), median (IQR).”

**Footnotes**

- `*`: “average Morisky score over the four follow-up moments. Calculated when at least 1 follow-up value was available”
- `**`: “Kappa for pill weight and self-report adherence for multinutrient=0.73 and omega=0.70.”

**Reproducible logical check:** The single-star note explicitly concerns Morisky, whose row is unmarked, while its markers appear on four other rows. The double-star note concerns pill-weight/self-report agreement, but no `**` appears beside those rows. No arithmetic or rounding tolerance applies.

**Bounded impact:** Readers cannot reliably map the averaging rule and Kappa values to their intended measures. The displayed adherence values themselves are not shown to be wrong.

**Human verification**

1. Confirm the four visible single-star markers and absence of a marker on the Morisky row.
2. Confirm the subjects of the `*` and `**` notes.
3. Search the table for a visible `**` marker.
4. The mismatch is confirmed if the published page remains as described; the author/layout source is required to establish the intended marker placement.

## Major reconciliations and non-findings

The following checks reconciled and did not produce a final issue:

- Figure 1 screening chain: `5965 − 3730 = 2235`; `2235 − 462 = 1773`; `1773 − 523 = 1250`; `1250 − 225 = 1025`. Randomized groups sum to 1025.
- Figure 1 follow-up: month-3 group counts sum to 831, month-6 counts sum to 771, and month-12 counts sum to 779. Month-12 losses `65 + 62 + 58 + 61 = 246`.
- Factorial primary totals reconcile: participants `513 + 512 = 1025`; events `51 + 54 = 57 + 48 = 105`; Table 2’s narrower dropout definition gives `113 + 126 = 122 + 117 = 239`.
- Table 3 effect-coded estimates and confidence intervals reconcile with the prose after the stated multiplication by 2, allowing for pre-rounding differences of 0.01.
- `DOC-004` adherence percentages reconcile with stated row denominators. Hospitalizations `24 + 24 + 26 + 24 = 98`, and deaths total 1, matching `DOC-001`.
- CACE values, concealment totals/percentages, and main-article versus supplement sensitivity estimates reconcile.

## Rejected and uncertain candidates

- **Rejected after critic review:** The Abstract phrase “for their combination” was not retained as an issue. `DOC-001` Abstract Methods explicitly defines the analysis as “in combination (interaction)” and reports the interaction P value; possible ambiguity was not a demonstrated reporting inconsistency.
- **Uncertain, not promoted:** Table 2/eAppendix effect-coded odds-ratio scaling cannot be resolved without raw coefficients or an explicit transformation statement.
- **Uncertain, not promoted:** Apparent site-confidence-interval asymmetry in eAppendix 10B cannot be resolved without the model specification and unrounded output.

## Adjudication request

Please perform Human Adjudication of the four retained minor issues and the `DOC-005` Human Compliance Review flag. No further automated verification or critic round is planned.
