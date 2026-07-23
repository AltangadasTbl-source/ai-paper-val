# Human Adjudication Report — jama.2025.9110

Scope: supplied PDFs only; source PDFs unchanged. Six accepted minor findings are presented below. This report is not a legal opinion.

## Package Manifest

| Document ID | File | Classification and audit status | Document-level output |
|---|---|---|---|
| `JAMA2025_9110_D01_MAIN` | `jama_summers_2025_oi_250040_1753124024.36498.pdf` | Main article; audited, PDF pp. 1-10 | [Record](document_outputs/JAMA2025_9110_D01_MAIN/inventory_record.md) · [Processing](document_outputs/JAMA2025_9110_D01_MAIN/preprocessing_record.md) |
| `JAMA2025_9110_D02_PROTOCOL` | `joi250040supp1_prod_1753124024.37199.pdf` | Protocol; **Not Audited by Design** (no result-relevant scope) | [Record](document_outputs/JAMA2025_9110_D02_PROTOCOL/inventory_record.md) · [Processing](document_outputs/JAMA2025_9110_D02_PROTOCOL/preprocessing_record.md) |
| `JAMA2025_9110_D03_SAP` | `joi250040supp2_prod_1753124024.37799.pdf` | Statistical analysis plan; **Not Audited by Design** (no result-relevant scope) | [Record](document_outputs/JAMA2025_9110_D03_SAP/inventory_record.md) · [Processing](document_outputs/JAMA2025_9110_D03_SAP/preprocessing_record.md) |
| `JAMA2025_9110_D04_RESULTS_SUPP` | `joi250040supp3_prod_1753124024.38098.pdf` | Results supplement; audited, PDF pp. 1-32 (results scope) | [Record](document_outputs/JAMA2025_9110_D04_RESULTS_SUPP/inventory_record.md) · [Processing](document_outputs/JAMA2025_9110_D04_RESULTS_SUPP/preprocessing_record.md) |

## AI Training Restriction Summary

Separate compliance screen; not part of the scientific findings. Permissions are assumed given per package instruction. This summary is not legal advice.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| `JAMA2025_9110_D01_MAIN` | Explicit AI Training Restriction | PDF p. 1 bottom copyright notice; repeats pp. 2-10: “All rights reserved, including those for text and data mining, AI training, and similar technologies.” | **Required**; permissions assumed given per package instruction. |
| `JAMA2025_9110_D02_PROTOCOL` | No AI Training Restriction Located in Provided Materials | Visible PDF pp. 1 and 40; embedded document-info/XMP metadata; garbled native text keyword-screened. No qualifying language located. | Not flagged; silence is not permission. |
| `JAMA2025_9110_D03_SAP` | No AI Training Restriction Located in Provided Materials | Visible PDF pp. 1 and 31; embedded document-info/XMP metadata; garbled native text keyword-screened. No qualifying language located. | Not flagged; silence is not permission. |
| `JAMA2025_9110_D04_RESULTS_SUPP` | Explicit AI Training Restriction | PDF p. 1 bottom copyright notice; repeats pp. 2-22: “All rights reserved, including those for text and data mining, AI training, and similar technologies.” | **Required**; permissions assumed given per package instruction. |

Detailed rights records: [D01](document_outputs/JAMA2025_9110_D01_MAIN/ai_training_restriction_record.md), [D02](document_outputs/JAMA2025_9110_D02_PROTOCOL/ai_training_restriction_record.md), [D03](document_outputs/JAMA2025_9110_D03_SAP/ai_training_restriction_record.md), [D04](document_outputs/JAMA2025_9110_D04_RESULTS_SUPP/ai_training_restriction_record.md).

## Scientific Findings

All six accepted findings are **Minor**.

### 1. Period 3 augmented-protein sex counts do not reconcile

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Location:** D04, PDF p. 10, eTable 4, Period 3—Augmented Protein, Sex rows; compare D01, PDF p. 5, Table 1, Sex rows.
- **Compared values:** D04: `n=551`, male `359 (65.2)`, female `190 (34.5)`; D01 overall augmented-protein: male `1070 (63.7)`, female `611 (36.3)`, `n=1681`.
- **Basis:** `359 + 190 = 549`, two below 551; percentages total 99.7%. Across augmented periods, male `303+187+359+220=1069` and female `177+111+190+132=610`, each one below D01; no missing/other row or explanatory footnote is displayed.
- **Verify:** Re-add D04 Period 3 sex counts and all augmented-period sex counts; reconcile with the D01 denominator and totals, or disclose/correct an omitted category.

### 2. Protocol-deviation participant percentage matches the event count

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Location:** D04, PDF p. 16, eTable 8, Total protocol deviations, Augmented Protein.
- **Compared values:** `n=1681`; participants with at least one event `151 (9.4)`; events `158`.
- **Basis:** `151/1681 × 100 = 9.0%` (one decimal); `158/1681 × 100 = 9.4%`. The displayed percentage beside participant count matches the event count.
- **Verify:** Recalculate both percentages and confirm whether the participant entry should be `151 (9.0%)`.

### 3. Figure 1 uses patient-level randomization wording although ICUs were randomized

- **Category / severity:** Presentation inconsistency / Minor.
- **Location:** D01, PDF p. 3, Figure 1, four patient-count treatment boxes; compare D01, PDF p. 2, Design/Trial Procedures, and p. 8, Limitations.
- **Compared statements:** Figure 1 states patient counts “Randomized to” augmented/usual protein, including primary-analysis boxes. Methods states the trial was cluster randomized and “ICUs were randomly assigned”; Limitations states randomization occurred at cluster rather than patient level.
- **Basis:** The box wording attributes randomization to patients while the stated randomization unit is the ICU/cluster. This addresses terminology only, not the counts or allocation process.
- **Verify:** Compare the box labels with the stated randomization unit; assess changing “Randomized to” to assigned/allocated or equivalent cluster-period wording.

### 4. Bayesian primary-outcome row labels median/IQR values as mean (SD)

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Location:** D01, PDF p. 7, Table 2, primary outcome secondary-analysis Bayesian quantile mixed-model row; compare D04, PDF p. 27, eFigure 6.
- **Compared values/statements:** The row label ends `mean (SD)`, but cells are `62.0 (0 to 77)` and `64.0 (0 to 77)` with `Median difference, -1.50 (-3.86 to 0.90)`. The row above labels the same summaries `median (IQR)`; eFigure 6 labels `Median Difference: -1.50 (95% CrI: -3.86, 0.90)`.
- **Basis:** The repeated center and quartile endpoints, model name, and effect label identify median/IQR summaries, inconsistent with `mean (SD)`.
- **Verify:** Compare the two Table 2 rows and eFigure 6; confirm whether the Bayesian row should read `median (IQR)`.

### 5. Ventilation group summaries are labeled mean (SD) although the supplement identifies median (IQR)

- **Category / severity:** Cross-document inconsistency / Minor.
- **Location:** D01, PDF p. 7, Table 2, Duration of invasive ventilation; compare D04, PDF p. 18, eTable 10/footer, and p. 4, eMethods.
- **Compared values/statements:** D01 label: `mean (SD), h`; cells: `84.0 (35.0 to 178.9)` and `78.0 (33.2 to 161.0)`. D04 eTable 10 footer: “Data presented as median (IQR) or n (%).” D04 eMethods reserves “difference in means” for the model treatment effect.
- **Basis:** D01 displays a center plus two endpoints, while the supplement identifies the descriptive format as median/IQR; the model-based mean difference is a distinct measure.
- **Verify:** Compare the D01 label/cells with the D04 footer and eMethods; determine whether the group-summary label should be `median (IQR)`.

### 6. Table 2 directs eFigure 6 to Supplement 1 although it is in Supplement 3

- **Category / severity:** Presentation inconsistency / Minor.
- **Location:** D01, PDF p. 7, Table 2 footnote f; compare D01, PDF p. 4, Primary Outcome, and D04, PDF p. 27, eFigure 6.
- **Compared statements:** Footnote f: “Bayesian model diagram is shown in eFigure 6 in Supplement 1.” D01 Primary Outcome places eFigures 5 and 6 in Supplement 3; D04 is Supplement 3 and contains “eFigure 6: Bayesian model analysis.”
- **Basis:** The Table 2 document locator conflicts with the Results text and actual supplied location.
- **Verify:** Confirm the three locators; change `Supplement 1` to `Supplement 3` if intended.

## Rejected and Uncertain Candidates

- **C06 — Uncertain; not accepted.** Proposed statistical reporting inconsistency. D01 p. 8 Discussion calls day-10 urea concentrations “mean”; D01 p. 5 and D04 p. 19 eTable 11 display medians (IQR), `13.0 (8.2-18.8)` versus `10.6 (7.1-15.4)` mmol/L. The documents do not establish that the sentence restates those medians rather than unreported arithmetic means. **Verify:** If source analysis output is available, determine whether day-10 arithmetic means were calculated; if not, assess changing “mean” to “median.”
- **Rejected candidates:** None.

## Human Adjudication Checklist

- Confirm each of the six findings against the cited PDF page, table, figure, and values.
- Decide the appropriate correction or explanatory disclosure for each accepted minor finding.
- Retain C06 as uncertain unless source analysis output resolves whether arithmetic means were calculated.
- Keep D02 and D03 as Not Audited by Design unless a specific result-relevant comparison is requested.
- Complete Human Compliance Review for D01 and D04 as applicable; permissions are assumed given per package instruction.
