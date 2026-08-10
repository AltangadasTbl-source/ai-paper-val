# Human Adjudication Report — JAMA 2019.12618

**Purpose:** This report presents four accepted, document-grounded findings for human adjudication. It is not a conclusion about the publication, underlying data, or study conduct. No more than the accepted findings are reported.

## Package processing record

| Document ID | Filename | Classification and scientific-audit status | Extraction/OCR status |
|---|---|---|---|
| JAMA2019-12618-MAIN | `jama_rathinam_2019_oi_190092.pdf` | Main article — Audited | PDF pp. 1–10: usable native text extracted; OCR not required. |
| JAMA2019-12618-SUPP-RESULTS | `joi190092supp1_prod.pdf` | Results supplement — Audited on results-relevant pages | PDF pp. 1–16: usable native text extracted; OCR not required. |
| JAMA2019-12618-PROTOCOL | `joi190092supp2_prod.pdf` | Protocol/manual of operations — **Not Audited by Design** | No broad extraction, rendering, OCR, or result checking. |
| JAMA2019-12618-SAP | `joi190092supp3_prod.pdf` | Statistical analysis plan — **Not Audited by Design** | No broad extraction, rendering, OCR, or result checking. |
| JAMA2019-12618-DATA-SHARING | `joi190092supp4_prod.pdf` | Administrative data-sharing statement — **Not Audited by Design** | No scientific extraction, rendering, OCR, or result checking. |

OCR backend selection was **RapidOCR CPU** (`rapidocr-cpu`; CPU execution path selected). OCR was not required because all selected audit pages had usable native text.

## Scientific issues for adjudication

### 1. Table 3 mycophenolate denominator label

**Issue statement:** Table 3 labels the mycophenolate mofetil column `n = 109`, while its displayed percentages use 108 recipients; the footnote explains the nonrecipient, but the header does not state the percentage denominator, which makes the presentation internally inconsistent.

**Category:** Presentation inconsistency  
**Severity:** Minor

**Evidence**

- **Source A — header and cells:** `JAMA2019-12618-MAIN`, `jama_rathinam_2019_oi_190092.pdf`, PDF p. 8, Table 3, measurement header and Mycophenolate Mofetil column; rows “Elevated ALT or AST (2 to 5 times upper limit of normal <28 d)” and “Headache.” Reported wording/values: “No. (%) of Patients Reporting ≥1 Adverse Event”; “Mycophenolate Mofetil (n = 109)ᵇ”; `8 (7.4)`; `45 (41.7)`.
- **Source B — footnote:** same document, PDF p. 8, Table 3, footnote b. Reported wording: “One patient in the mycophenolate mofetil group never received mycophenolate mofetil due to medical contraindication discovered postrandomization.”

**Direct comparison:** The reported header denominator is 109. The footnote-derived exposed-recipient comparator is `109 − 1 = 108`; `8 (7.4)` and `45 (41.7)` match 108, not 109.

**Reproducible calculation:** Inputs: 8 events, 45 events, displayed header `n=109`, and one stated nonrecipient. Rule: percentage = count/denominator × 100, rounded to one decimal. `8/109 × 100 = 7.339% → 7.3%`; `8/108 × 100 = 7.407% → 7.4%`. `45/109 × 100 = 41.284% → 41.3%`; `45/108 × 100 = 41.667% → 41.7%`. At one decimal, the 109-denominator values fall outside the rounding intervals for 7.4% and 41.7% (±0.05 percentage point around the displayed value).

**Bounded impact:** Confirmation would require correction or clarification of the Table 3 mycophenolate percentage denominator presentation only; the evidence does not change the two event counts or establish different patient-level events.

**Human verification**

1. On PDF p. 8, check the `n = 109` header, superscript b, footnote b, and the two cited cells.
2. Calculate both cells with 109 and 108; values rounding to 7.4% and 41.7% only with 108 confirm the denominator-label mismatch.

### 2. Table 3 methotrexate elevated ALT or AST percentage

**Issue statement:** Table 3 reports methotrexate elevated ALT or AST as `14 (13.0)`, although 14 of the stated 107 patients rounds to 13.1%, making the displayed percentage inconsistent with its count and column denominator.

**Category:** Arithmetic inconsistency  
**Severity:** Minor

**Evidence**

- **Source A — denominator and target cell:** `JAMA2019-12618-MAIN`, `jama_rathinam_2019_oi_190092.pdf`, PDF p. 8, Table 3, Nonserious laboratory, row “Elevated ALT or AST (2 to 5 times upper limit of normal <28 d)”, Methotrexate column. Reported wording/values: “Methotrexate (n = 107)” and `14 (13.0)`.
- **Source B — internal comparator:** same document, PDF p. 8, Table 3, Nonserious systemic, row “Allergic reaction,” Methotrexate column. Reported value: `14 (13.1)`.

**Direct comparison:** Reported percentage: 13.0%. Comparator: the reported count of 14 and stated `n=107` yield 13.1%; the same-table same-numerator comparator is also `14 (13.1)`.

**Reproducible calculation:** Inputs: 14 and 107. Rule: `14/107 × 100 = 13.0841%`, rounded to one decimal = **13.1%**. Rounding tolerance for 13.0% is `[12.95%, 13.05%)`; 13.0841% is outside that interval.

**Bounded impact:** Confirmation would correct or clarify one Table 3 percentage cell, understated by 0.1 displayed percentage point; the reported count of 14 and other Table 3 results are not altered by this finding.

**Human verification**

1. On PDF p. 8, check the `n=107` header, target `14 (13.0)` cell, and `14 (13.1)` allergic-reaction cell.
2. Compute `14/107 × 100`; a one-decimal result of 13.1% confirms the issue unless the table documents a different row-specific denominator.

### 3. eTable 9 mycophenolate serious systemic diarrhea percentage

**Issue statement:** eTable 9 reports serious systemic diarrhea as `1 (3.4)` in the mycophenolate mofetil `N=20` column, although one of 20 is 5.0% and 3.4% corresponds to the adjacent `N=29` denominator, making the displayed percentage inconsistent with its stated column denominator.

**Category:** Arithmetic inconsistency  
**Severity:** Minor

**Evidence**

- **Source A — headers and target cell:** `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`, PDF p. 15, eTable 9, Serious Systemic, “Diarrheaᵇ” row, Mycophenolate Mofetil column. Reported values: “Methotrexate (N=29)”; “Mycophenolate Mofetil (N=20)”; target cell `1 (3.4)`.
- **Source B — same-column comparators:** same document, PDF p. 15, eTable 9, Mycophenolate Mofetil `N=20` column, Low hemoglobin and Allergic reaction rows. Reported values: `1 (5.0)` and `1 (5.0)`.
- **Source C — adjacent-column comparator:** same document, PDF p. 15, eTable 9, Methotrexate `N=29` column. Reported value pattern: `1 (3.4)`.

**Direct comparison:** Reported: 3.4% for one patient under `N=20`. Comparator/expected value: `1/20 = 5.0%`, consistent with the same-column one-patient cells. The reported 3.4% matches `1/29`, the adjacent-column denominator; discrepancy = **1.6 percentage points lower** than the `N=20` result.

**Reproducible calculation:** Inputs: 1 event, stated `N=20`, adjacent `N=29`. Rule: percentage = count/denominator × 100, shown to one decimal. `1/20 × 100 = 5.0%`; `1/29 × 100 = 3.4483% → 3.4%`. The 1.6-percentage-point difference is larger than one-decimal rounding tolerance (±0.05 percentage point).

**Bounded impact:** Confirmation would require correction or clarification of the displayed percentage for this one serious-adverse-event cell. The visible event count remains one; the supplied evidence does not determine whether a production correction should change the percentage, count, or denominator.

**Human verification**

1. On PDF p. 15, confirm that `1 (3.4)` is located under Mycophenolate Mofetil `N=20`, and check the cited same-column `1 (5.0)` cells.
2. Compute `1/20 × 100` and compare with `1/29 × 100`; 5.0% for the stated column denominator confirms the displayed inconsistency.

### 4. eTable 4 mycophenolate eye-floaters percentage

**Issue statement:** eTable 4 reports mycophenolate eye floaters as `5 (4.7)`, although five of the stated 108 recipients rounds to 4.6%, making the displayed percentage inconsistent with its stated denominator.

**Category:** Arithmetic inconsistency  
**Severity:** Minor

**Evidence**

- **Source A — target header and cell:** `JAMA2019-12618-SUPP-RESULTS`, `joi190092supp1_prod.pdf`, PDF p. 10, eTable 4, “Eye floaters” row, Mycophenolate Mofetil column. Reported values: “Mycophenolate Mofetil (N=108)” and `5 (4.7)`.
- **Source B — adjacent comparator:** same document, PDF p. 10, eTable 4, “Eye floaters” row, Methotrexate `N=107` column. Reported value: `5 (4.7)`.
- **Source C — denominator footnote:** same document, PDF p. 10, eTable 4, footnote a. Reported wording: “Out of 107 patients who received methotrexate and 108 patients who received mycophenolate mofetil.”

**Direct comparison:** Reported percentage: 4.7% with `N=108`. Comparator/expected value: `5/108 = 4.6%` to one decimal. The reported percentage instead matches `5/107 = 4.7%`; discrepancy = **0.1 percentage point higher** than the stated-`N=108` result.

**Reproducible calculation:** Inputs: 5 events, stated `N=108`, adjacent `N=107`. Rule: percentage = count/denominator × 100, rounded to one decimal. `5/108 × 100 = 4.6296% → 4.6%`; `5/107 × 100 = 4.6729% → 4.7%`. Rounding tolerance for 4.7% is `[4.65%, 4.75%)`; 4.6296% is outside that interval.

**Bounded impact:** Confirmation would correct or clarify one displayed percentage, overstated by 0.1 percentage point; the reported event count of five is unaffected.

**Human verification**

1. On PDF p. 10, confirm the Mycophenolate Mofetil `N=108` header, footnote a, and `5 (4.7)` eye-floaters cell.
2. Compute `5/108 × 100`; a one-decimal result of 4.6% confirms the issue unless an explicit row-specific denominator replaces 108.

## AI Training Restriction Summary

This document-level screen is separate from the scientific issue list and is **not legal advice**. It does not infer permission from silence. The project instruction states that AI-training permissions are assumed given.

| Document ID | Status | Exact evidence location and quoted language/value | Human Compliance Review |
|---|---|---|---|
| JAMA2019-12618-MAIN | No AI Training Restriction Located in Provided Materials | `jama_rathinam_2019_oi_190092.pdf`, PDF pp. 1–10 repeated footer (first PDF p. 1): “© 2019 American Medical Association. All rights reserved.” | No — not triggered by this screen. |
| JAMA2019-12618-SUPP-RESULTS | No AI Training Restriction Located in Provided Materials | `joi190092supp1_prod.pdf`, PDF pp. 1–16 repeated footer (first PDF p. 1): “© 2019 American Medical Association. All rights reserved.” | No — not triggered by this screen. |
| JAMA2019-12618-PROTOCOL | No AI Training Restriction Located in Provided Materials | `joi190092supp2_prod.pdf`, title/front matter PDF pp. 1–3; end matter PDF p. 153; text-layer rights/AI-use term search and embedded metadata: no AI-training, fine-tuning, model-improvement, rights, license, or terms statement located. | No — not triggered by this screen. |
| JAMA2019-12618-SAP | No AI Training Restriction Located in Provided Materials | `joi190092supp3_prod.pdf`, PDF p. 2, Statistical Analysis Plan title page: “Confidential”; PDF pp. 1–3, p. 83, text-layer rights/AI-use term search, and embedded metadata: no language connecting this label to AI training, fine-tuning, or model improvement located. | No — not triggered by this screen. |
| JAMA2019-12618-DATA-SHARING | No AI Training Restriction Located in Provided Materials | `joi190092supp4_prod.pdf`, PDF p. 1, Data Sharing Statement, “How to access data,” “Who can access the data,” and “Any additional restrictions”: “Data requests will be reviewed on a case-by-case basis by Dr. Nisha Acharya and the FAST Executive Committee.” “Data will be made available to researchers whose proposed use of the data has been approved by Dr. Nisha Acharya and the FAST Executive Committee.” “Data provided will be de-identified.” | No — not triggered by this screen. |
