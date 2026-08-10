# Evidence verification — JAMA 2019.12618

Original PDFs were reopened at the cited pages. Round 1 checked source text and table structure; round 2 visually checked rendered original pages for column placement, footnotes, and cohort labels. No candidate received more than two rounds.

| Candidate | Disposition | Category | Severity |
|---|---|---|---|
| V1 | Verified | Presentation inconsistency | Minor |
| V2 | Verified | Arithmetic inconsistency | Minor |
| V3 | Verified | Arithmetic inconsistency | Minor |
| V4 | Verified | Arithmetic inconsistency | Minor |
| V5 | Rejected | Proposed cross-document inconsistency | — |

## V1 — Verified

**Issue statement:** Main Table 3 labels the mycophenolate mofetil column `n = 109`, but its displayed percentages use 108 recipients; footnote b explains the one nonrecipient but the percentage denominator is not stated in the column header.

**Location:** `JAMA2019-12618-MAIN`; `jama_rathinam_2019_oi_190092.pdf`; PDF p. 8; Table 3; header and Mycophenolate Mofetil column; rows “Elevated ALT or AST (2 to 5 times upper limit of normal <28 d)” and “Headache.”

**Source evidence:** Measurement header: “No. (%) of Patients Reporting ≥1 Adverse Event.” Column header: “Mycophenolate Mofetil (n = 109)ᵇ.” Cells: `8 (7.4)` and `45 (41.7)`. Footnote b: “One patient in the mycophenolate mofetil group never received mycophenolate mofetil due to medical contraindication discovered postrandomization.”

**Reported versus comparator:** The printed header supplies 109, whereas the footnote-derived exposed denominator is `109 − 1 = 108`.

**Calculation:** `8/109 × 100 = 7.339%`, which rounds to 7.3%, while `8/108 × 100 = 7.407%`, which rounds to the reported 7.4%. Likewise, `45/109 × 100 = 41.284%`, which rounds to 41.3%, while `45/108 × 100 = 41.667%`, which rounds to the reported 41.7%. For one-decimal rounding, 7.4% requires `[7.35%, 7.45%)` and 41.7% requires `[41.65%, 41.75%)`; the n=109 results fall outside both intervals.

**Logical basis:** The footnote makes the use of an exposed cohort understandable, but the header still labels the percentage column with the randomized count of 109. Multiple cells independently show that 108 is the operative denominator.

**Bounded impact:** The inconsistency affects denominator presentation for the mycophenolate percentages in Table 3; it does not contradict the event counts or establish different patient-level events.

**Human verification:**

1. On PDF p. 8, confirm the `n = 109` header, superscript b, footnote text, and the two cited cells.
2. Recalculate both cells with 109 and 108. Results of 7.4% and 41.7% only with 108 confirm the presentation inconsistency; an explicit statement elsewhere that Table 3 percentages use recipients would explain the convention but would not change the printed header.

## V2 — Verified

**Issue statement:** Main Table 3 reports methotrexate elevated ALT or AST as `14 (13.0)`, although 14 of the stated 107 patients rounds to 13.1%.

**Location:** `JAMA2019-12618-MAIN`; `jama_rathinam_2019_oi_190092.pdf`; PDF p. 8; Table 3; Nonserious laboratory; row “Elevated ALT or AST (2 to 5 times upper limit of normal <28 d)”; Methotrexate column.

**Source evidence:** Column header: “Methotrexate (n = 107).” Target cell: `14 (13.0)`. Same table and column, Nonserious systemic “Allergic reaction” row: `14 (13.1)`.

**Reported versus comparator:** Reported 13.0%; numerator/header calculation and the same-numerator internal comparator give 13.1%.

**Calculation:** `14/107 × 100 = 13.0841%`, which rounds to 13.1% to one decimal. A displayed 13.0% permits `[12.95%, 13.05%)`; 13.0841% is outside that interval by 0.0341 percentage points and differs from the display by 0.0841 percentage points.

**Logical basis:** The count, denominator, and percent are printed in the same table without a row-specific denominator footnote. The identical `14` count elsewhere in the same n=107 column is correctly displayed as 13.1%.

**Bounded impact:** One percentage cell is understated by 0.1 displayed percentage point; the count of 14 and other Table 3 results are unaffected.

**Human verification:**

1. Confirm the n=107 header, `14 (13.0)` target cell, and `14 (13.1)` allergic-reaction cell on PDF p. 8.
2. Compute `14/107 × 100`; 13.0841%, rounding to 13.1%, confirms the issue unless a different row-specific denominator is documented.

## V3 — Verified

**Issue statement:** Supplement eTable 9 reports serious systemic diarrhea in the mycophenolate mofetil N=20 column as `1 (3.4)`, although one of 20 is 5.0%; 3.4% corresponds to the adjacent N=29 denominator.

**Location:** `JAMA2019-12618-SUPP-RESULTS`; `joi190092supp1_prod.pdf`; PDF p. 15; eTable 9; Serious Systemic; “Diarrheaᵇ” row; Mycophenolate Mofetil column.

**Source evidence:** Column headers: “Methotrexate (N=29)” and “Mycophenolate Mofetil (N=20).” Target cell: `1 (3.4)`. In the same N=20 column, Low hemoglobin and Allergic reaction each read `1 (5.0)`. The adjacent N=29 column repeatedly displays `1 (3.4)`.

**Reported versus comparator:** Reported 3.4%; N=20 calculation and same-column one-patient cells give 5.0%.

**Calculation:** `1/20 × 100 = 5.0%`; `1/29 × 100 = 3.4483%`, which rounds to 3.4%. The reported value is 1.6 percentage points below the N=20 result and is outside the 3.4% rounding interval `[3.35%, 3.45%)` for the stated denominator calculation.

**Logical basis:** Visual review confirms that `1 (3.4)` is in the N=20 mycophenolate cell, not the adjacent N=29 methotrexate cell. Same-column cells demonstrate the table's usual N=20 percentage.

**Bounded impact:** The displayed percentage for one serious adverse-event cell is affected; the visible event count remains one.

**Human verification:**

1. Confirm the target cell's column placement under Mycophenolate Mofetil N=20 on PDF p. 15.
2. Compute `1/20 × 100` and compare with the same-column `1 (5.0)` cells. A result of 5.0% confirms the inconsistency; source production data would be needed to identify whether the intended correction is the percentage, count, or denominator.

## V4 — Verified

**Issue statement:** Supplement eTable 4 reports mycophenolate eye floaters as `5 (4.7)`, although five of the stated 108 recipients rounds to 4.6%.

**Location:** `JAMA2019-12618-SUPP-RESULTS`; `joi190092supp1_prod.pdf`; PDF p. 10; eTable 4; “Eye floaters” row; Mycophenolate Mofetil column.

**Source evidence:** Column header: “Mycophenolate Mofetil (N=108).” Target cell: `5 (4.7)`. Adjacent Methotrexate N=107 cell: `5 (4.7)`. Footnote a states: “Out of 107 patients who received methotrexate and 108 patients who received mycophenolate mofetil.”

**Reported versus comparator:** Reported 4.7%; the stated N=108 calculation gives 4.6%. The displayed value instead matches the adjacent N=107 calculation.

**Calculation:** `5/108 × 100 = 4.6296%`, which rounds to 4.6%. `5/107 × 100 = 4.6729%`, which rounds to 4.7%. A displayed 4.7% requires `[4.65%, 4.75%)`; 4.6296% is outside that interval.

**Logical basis:** The header and footnote independently establish 108 recipients, and visual review confirms the cell's placement. The identical adjacent count and percentage provide a document-grounded copying/denominator comparator, without establishing the production cause.

**Bounded impact:** One displayed percentage is overstated by 0.1 percentage point; the event count of five is unaffected.

**Human verification:**

1. Confirm the N=108 header, footnote, and `5 (4.7)` cell on PDF p. 10.
2. Compute `5/108 × 100`; 4.6296%, rounding to 4.6%, confirms the issue unless an explicit row-specific denominator replaces 108.

## V5 — Rejected

The proposed cross-document inconsistency is not supported because the compared denominators are not defined as the same analysis population. Supplement p. 14 eTable 8 reports interval adverse events from six to 12 months among patients continuing after success (`N=62`, `N=56`). Main p. 3 Figure 1 labels `60` and `54` as patients who continued and “were included in the 12-month secondary analysis”; main p. 6 Table 2 reports 12-month point-outcome denominators `48/60` and `40/54`, and footnote h says those 60 and 54 continued the same antimetabolite “through 12 months.” Table 2 separately shows 64 and 56 six-month successes. Thus eTable 8 differs from the 12-month efficacy cohort by `+2` per arm, while it is smaller than/equal to the six-month-success cohort (`64−62=2`; `56−56=0`). Figure 1 also records withdrawal/loss before the 12-month visit. An interval safety population can include partial follow-up that is excluded from a 12-month point analysis, so equality is not required. The exact eTable 8 inclusion dataset is not provided; without evidence that it is identical to the 12-month efficacy cohort, no cross-document inconsistency is verified.
