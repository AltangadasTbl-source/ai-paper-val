# Table arithmetic and internal-consistency check

## Scope

Audited only result-relevant tables in `basis_main_article` and in the results supplement, PDF pages 10–25. No protocol, SAP, administrative material, or supplementary PDF pages 3–9 were accessed. Calculations use the displayed numerator and displayed/group denominator and round to one decimal by ordinary nearest rounding.

## Candidate issues for verification

1. **Arithmetic inconsistency — Table 1, female baseline percentage**
   - **Location:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.6 / print p.1064, Table 1, “Sex, No. (%) — Female,” balloon angioplasty group.
   - **Source values:** group denominator `n=249`; female `77 (30.1)`.
   - **Calculation:** `77 / 249 × 100 = 30.92%`, which rounds to **30.9%**, not 30.1%.
   - **Relevance/severity:** Moderate; a visible baseline-table percentage is internally inconsistent with its numerator and denominator.
   - **Verification:** Recalculate this single displayed cell against the printed group denominator; check the intended percentage in the production source.

2. **Arithmetic inconsistency — Table 1, NIHSS 2–4 percentage**
   - **Location:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.6 / print p.1064, Table 1, “NIHSS score at admission, No. (%) — 2–4,” aggressive medical management group.
   - **Source values:** group denominator `n=252`; value `51 (20.5)`.
   - **Calculation:** `51 / 252 × 100 = 20.24%`, which rounds to **20.2%**, not 20.5%.
   - **Relevance/severity:** Moderate; visible baseline percentage conflicts with the printed numerator and denominator.
   - **Verification:** Recalculate the cell using `51/252` and confirm whether either the numerator, denominator, or percentage was intended to differ.

3. **Arithmetic inconsistency — Table 1, 90%–99% stenosis percentage**
   - **Location:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p.6 / print p.1064, Table 1, “Stenosis of symptomatic artery, No. (%) — 90%–99%,” balloon angioplasty group.
   - **Source values:** group denominator `n=249`; value `25 (10.4)`.
   - **Calculation:** `25 / 249 × 100 = 10.04%`, which rounds to **10.0%**, not 10.4%.
   - **Relevance/severity:** Moderate; the row numerator also participates in a displayed category total of 249, so the denominator is explicit.
   - **Verification:** Recalculate against `n=249`; inspect the source data or production table for a transposed/miscopied percentage.

4. **Arithmetic inconsistency — Table S6 balloon-arm percentage**
   - **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.19, Table S6, primary outcome, balloon angioplasty group.
   - **Source values:** header `n=249`; outcome `9 (3.9)`.
   - **Calculation:** `9 / 249 × 100 = 3.61%`, which rounds to **3.6%**, not 3.9%.
   - **Relevance/severity:** Moderate; this post hoc adjustment table gives a displayed percentage incompatible with its own header denominator.
   - **Verification:** Recalculate `9/249`; if 3.9% is intended, confirm the actual analysis denominator and correct/clarify the header.

5. **Presentation inconsistency — Table S7 group headers conflict with its site totals and displayed percentages**
   - **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.20, Table S7.
   - **Source values:** column headers state balloon `N=233` and medical management `N=238`; site totals are `256` and `245` (total `501`). Event cells are balloon `4 (2.9)` and `7 (6.3)`, medical `19 (16.1)` and `15 (11.2)`.
   - **Calculation:** Header totals are `233 + 238 = 471`, incompatible with the two displayed site totals: `256 + 245 = 501`. Conversely, the reported percentages imply approximate stratum denominators of `4/0.029≈138` and `7/0.063≈111` (sum ≈249), and `19/0.161≈118` and `15/0.112≈134` (sum ≈252), rather than 233 and 238.
   - **Relevance/severity:** High; the denominators displayed in the same table cannot support the percentages or the adjacent site-total column.
   - **Verification:** Confirm the analysis population for Table S7 and revise either the two column headers or the site/percentage entries. Table S10 (PDF p.23) separately labels the per-protocol denominators as 233 and 238, which makes the discrepancy especially checkable.

6. **Presentation inconsistency — Table S8 per-protocol headers do not match its displayed percentages**
   - **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.21, Table S8, column headers and primary/composite component rows.
   - **Source values:** table title says per-protocol population; headers show balloon `n=249`, medical management `n=252`. Examples: primary `9 (3.9)` vs `33 (13.9)`; component rows `6 (2.6)` vs `4 (1.7)`, `1 (0.4)` vs `18 (7.6)`, and `3 (1.3)` vs `20 (8.4)`.
   - **Calculation:** The values consistently use `n=233` and `n=238`: `9/233=3.86%→3.9`; `33/238=13.87%→13.9`; `6/233=2.58%→2.6`; `20/238=8.40%→8.4`. They do not use the printed 249/252 headers (e.g., `9/249=3.6%`, `33/252=13.1%`).
   - **Relevance/severity:** High; every displayed percentage is internally inconsistent with the denominator labels but coherent with a different per-protocol denominator.
   - **Verification:** Confirm the PPS denominators and replace/clarify the headers. Table S10 (PDF p.23) displays PPS denominators `N=233` and `N=238`.

7. **Presentation/arithmetic inconsistency — Table S9 as-treated headers, and one BA percentage, cannot be reconciled**
   - **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.22, Table S9.
   - **Source values:** title says as-treated population; headers show balloon `n=249`, medical management `n=252`. The primary outcome is `11 (4.5)` vs `34 (13.4)`. The 30-day component is `8 (3.3)` vs `4 (1.6)`.
   - **Calculation:** The primary values instead correspond to `n=247` and `n=254`: `11/247=4.45%→4.5` and `34/254=13.39%→13.4`; Table S10 (PDF p.23) displays those as-treated denominators. The `8 (3.3)` cell is incompatible with both: `8/249=3.21%→3.2` and `8/247=3.24%→3.2`.
   - **Relevance/severity:** High; the stated population denominator conflicts with the percentages, and the 30-day BA percentage is unreconciled even after using the apparent as-treated denominator.
   - **Verification:** Confirm the actual ATS denominators and recalculate all percentages; specifically verify whether the BA 30-day count or its 3.3% value was transcribed incorrectly.

8. **Presentation inconsistency — Table S2 contains an unassigned evaluated-patient row**
   - **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p.15, Table S2, directly between “Current smoking, n (%)” and the next “No. Patients evaluated” row that precedes “Activity level per week.”
   - **Source values:** the intervening row is labelled only “No. Patients evaluated,” with `249, 249, NA` for balloon angioplasty and `252, 252, NA` for medical management; no associated characteristic or values appear.
   - **Calculation/logical basis:** The table presents two consecutive evaluated-patient rows, but only the second is adjacent to a measure (activity level). The first has no visible measure to which it can serve as a denominator, so it cannot be interpreted or verified from the table.
   - **Relevance/severity:** Low–moderate; presentation defect that makes an apparent denominator row unusable, without inferring a missing raw-data value.
   - **Verification:** Inspect the production source for a dropped characteristic/value row; either restore the associated measure or remove/label this denominator row.

## Not advanced as candidates

- Table S3’s `234 (93.9)` aspirin value at 3 months is 93.98% using the displayed `n=249`, but the 0.1-point difference may reflect a nonstandard truncation/display convention. It was not advanced because the table does not provide a separate 3-month evaluated denominator.
- The reviewed remaining displayed totals and percentages in Tables 2 and S1–S5 and S10–S12 were internally reconcilable at the stated display precision, or their component rows could overlap by definition.
