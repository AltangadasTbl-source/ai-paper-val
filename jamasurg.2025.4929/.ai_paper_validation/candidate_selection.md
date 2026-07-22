# Coordinator Candidate Selection

Date: 2026-07-21

Nine deduplicated candidates are submitted for the single evidence-verification stage. DOC-002 was not audited by design. No external evidence is permitted.

## C-01 — pN N3 regression row is internally incompatible

- **Category:** Statistical reporting inconsistency
- **Location:** DOC-003, PDF p. 3, eTable 2, pN/N3 row; cross-check DOC-001, PDF p. 7, Table 4.
- **Evidence:** `29/74 (25.7%), OR 0.431 (95% CI, 0.60-3.37), P=.431`; other pN morbidity numerators are 10 and 16; total morbidity is 45.
- **Basis:** 29/74=39.2%; 10+16+29=55 rather than 45; OR 0.431 is outside 0.60-3.37 and has the opposite direction from the displayed rates.
- **Verification:** Inspect the original eTable 2 cells and cross-check all displayed totals; do not infer corrected values without source support.

## C-02 — Age row percentage and univariate OR disagree with displayed cells

- **Category:** Statistical reporting inconsistency
- **Location:** DOC-003, PDF p. 3, eTable 2, Age block.
- **Evidence:** `<60: 13/88 (14.8%), reference`; `>=60: 32/120 (27.7%), OR 2.28 (1.12-4.64), P=.040`.
- **Basis:** 32/120=26.7%; displayed 2-by-2 cells yield OR `(32/88)/(13/75)=2.10`, not 2.28.
- **Verification:** Recalculate strictly from visible cells and determine whether the discrepancy is document-verifiable without raw data.

## C-03 — Several other univariate ORs do not reproduce from displayed cells

- **Category:** Statistical reporting inconsistency
- **Location:** DOC-003, PDF p. 3, eTable 2, Sex, Approach, BMI, Comorbidity, and ASA blocks.
- **Evidence:** Reported vs count-derived ORs: female/male 0.97 vs 0.90; ODG/LDG 0.85 vs 0.94; BMI >=25/<25 0.64 vs 0.59; comorbidity yes/no 3.10 vs 2.85; ASA 3/1 2.76 vs 2.51.
- **Basis:** For each displayed two-level categorical contrast, recompute the unadjusted odds ratio from the visible event/denominator cells.
- **Verification:** Confirm table orientation and arithmetic from the original page; reject if the reported model could validly use a different documented analysis set or coding.

## C-04 — Main text calls the approach estimate multivariable, but eTable 2 places it under univariate

- **Category:** Cross-document inconsistency
- **Locations:** DOC-001, PDF p. 6, “Risk Factors Related to Postoperative Morbidity”; DOC-003, PDF p. 3, eTable 2, Approach block.
- **Evidence:** Main text introduces “multivariate analyses” and calls approach an independent predictor result using OR 0.85 (0.44-1.63), P=.62. eTable 2 shows those exact numbers in univariate columns and blank multivariable cells.
- **Verification:** Inspect column headers/cell placement and the exact prose; determine whether the package documents an adjusted approach estimate.

## C-05 — Multiple main-table count/percentage cells do not round from displayed denominators

- **Category:** Arithmetic inconsistency
- **Locations:** DOC-001 Table 1 p.4 anemia LDG `30 (28.9)`; Table 2 p.5 intraoperative injury ODG `4 (3.9)`; Table 3 p.6 undifferentiated ODG `58 (55.6)`; Table 4 p.7 paralytic ileus ODG `5 (4.9)`, systemic infection ODG `4 (3.9)`, surgical complications ODG `17 (16.4)`. Each group denominator is 104.
- **Basis:** One-decimal calculations are 28.8%, 3.8%, 55.8%, 4.8%, 3.8%, and 16.3%, respectively.
- **Verification:** Check original table cells, denominators, and conventional one-decimal rounding; classify as a grouped minor issue only if all cited cells are verified.

## C-06 — GOO “No” percentage differs from displayed fraction

- **Category:** Arithmetic inconsistency
- **Location:** DOC-003, PDF p. 3, eTable 2, GOO/No.
- **Evidence:** `35/148 (23.7%)`.
- **Basis:** 35/148=23.6486%, which rounds to 23.6% at one decimal.
- **Verification:** Confirm the original fraction and printed percentage.

## C-07 — “No. (%)” table spanner covers continuous summaries

- **Category:** Presentation inconsistency
- **Locations:** DOC-001, Tables 1-4, PDF pp. 4-7.
- **Evidence:** The LDG/ODG columns are headed “No. (%)” while containing mean (SD) and median (IQR) values.
- **Verification:** Inspect all four table headers and continuous rows; retain only if the header visibly and misleadingly applies to those cells.

## C-08 — CONSORT refusal wording conflicts with postrandomization placement

- **Category:** Presentation inconsistency
- **Location:** DOC-001, PDF p. 3, CONSORT Figure; nearby flow prose on p. 4.
- **Evidence:** All 240 participants are described as willing to sign consent and randomized, after which 3 LDG and 2 ODG participants are labeled “Refused trial enrollment.”
- **Verification:** Confirm figure geometry and exact wording; retain only as a presentation inconsistency, not a count error.

## C-09 — Supplementary table contains inconsistent label spellings

- **Category:** Presentation inconsistency
- **Location:** DOC-003, PDF p. 3, eTable 2; compare DOC-001 Table 2/text.
- **Evidence:** `Aproach` and `Rouxx-En-Y` versus `Approach` and `Roux-en-Y` in the main article.
- **Verification:** Inspect source renderings and confirm exact spellings.
