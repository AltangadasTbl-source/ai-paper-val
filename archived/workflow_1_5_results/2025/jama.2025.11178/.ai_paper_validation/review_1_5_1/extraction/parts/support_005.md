# Support quantitative evidence map — support-005

## Scope and evidence method

- **DOC-005:** `joi250046supp4_prod_1755300121.15587.pdf`, PDF pp. 15-19. Reused canonical normalized text was used for pp. 15-18. Page 19 was freshly extracted from the direct PDF with `pdftotext -layout -f 19 -l 19`; it is a reference page.
- **DOC-006:** `joi250046supp5_prod_1755300121.16087.xlsx`, complete native worksheet `eTable 3`, A1:J115. The native workbook is the authority; the current Office-structure extraction and its one-page LibreOffice PDF were used only to locate and read cells. The structure extraction reports no formula in any populated cell: all values below are displayed/cached native values, not calculated formulas.
- This is an evidence map, not a candidate diagnosis. Direct arithmetic relationships are retained for later checking.

## DOC-005: unadjusted analyses and references

**PDF p. 15, eTable 9 (relationship group N-S005-ET9).** The introductory text says the replicated Tables 2 and 3 analyses have no adjustment, weighting, or imputation; it identifies eTable 9 as binary primary/secondary outcomes, eTable 10 as change-from-baseline secondary outcomes, and eTable 11 as mean secondary outcomes. eTable 9 labels the outcome as 30% improvement in pain score (n/N [%]) and labels the estimates *Relative Risk (95% CI)* in the contrasts PT vs UC, HC vs UC, and HC vs PT. `a` marks 3 months as the primary time point. `b` states that RR/95% CIs use a modified Poisson GEE model for each binary outcome **without adjustment**.

| Outcome / time | PT n/N (%) | HC n/N (%) | UC n/N (%) | PT vs UC RR (95% CI) | HC vs UC RR (95% CI) | HC vs PT RR (95% CI) |
|---|---|---|---|---|---|---|
| Pain Severity, 3 mo a | 179/542 (33.0) | 229/635 (36.1) | 151/621 (24.3) | 1.36 (1.13, 1.63) | 1.48 (1.26, 1.75) | 1.09 (0.94, 1.27) |
| Pain Severity, 6 mo | 225/547 (41.1) | 259/621 (41.7) | 167/622 (26.8) | 1.53 (1.30, 1.80) | 1.55 (1.32, 1.83) | 1.01 (0.88, 1.17) |
| Pain Severity, 12 mo | 246/583 (42.2) | 269/639 (42.1) | 197/639 (30.8) | 1.37 (1.18, 1.59) | 1.37 (1.21, 1.54) | 1.00 (0.90, 1.10) |
| Pain Intensity, 3 mo a | 164/543 (30.2) | 192/635 (30.2) | 129/621 (20.8) | 1.46 (1.19, 1.78) | 1.46 (1.18, 1.79) | 1.00 (0.83, 1.21) |
| Pain Intensity, 6 mo | 183/548 (33.4) | 222/622 (35.7) | 153/623 (24.6) | 1.36 (1.13, 1.63) | 1.45 (1.20, 1.74) | 1.06 (0.90, 1.26) |
| Pain Intensity, 12 mo | 218/583 (37.4) | 238/641 (37.1) | 191/639 (29.9) | 1.25 (1.07, 1.47) | 1.24 (1.08, 1.42) | 0.99 (0.87, 1.12) |
| Pain-related Interference, 3 mo a | 206/543 (37.9) | 249/635 (39.2) | 169/620 (27.3) | 1.39 (1.17, 1.64) | 1.44 (1.25, 1.65) | 1.03 (0.92, 1.17) |
| Pain-related Interference, 6 mo | 249/546 (45.6) | 277/620 (44.7) | 176/621 (28.3) | 1.61 (1.38, 1.88) | 1.58 (1.35, 1.85) | 0.98 (0.86, 1.12) |
| Pain-related Interference, 12 mo | 267/583 (45.8) | 293/638 (45.9) | 221/638 (34.6) | 1.32 (1.15, 1.52) | 1.33 (1.18, 1.48) | 1.00 (0.91, 1.10) |

**PDF p. 16, eTable 10 (relationship group S005-ET10).** Values are change-from-baseline medians (25th,75th percentile) for PT/HC/UC; estimates are unadjusted between-group mean differences (95% CI), followed by omnibus P. `a`: 3 months primary time point. `b`: mean change and CIs were calculated by linear-regression GEE for each continuous outcome, without adjustment.

| Outcome / time | PT median (IQR) | HC median (IQR) | UC median (IQR) | PT-UC MD (95% CI) | HC-UC MD (95% CI) | HC-PT MD (95% CI) | P |
|---|---|---|---|---|---|---|---|
| Severity 3 mo a | -1.1 (-2.1,-0.1) | -1.1 (-2.3,-0.1) | -0.6 (-1.6,0.2) | -0.4 (-0.6,-0.3) | -0.4 (-0.6,-0.3) | 0.0 (-0.2,0.2) | <0.001 |
| Severity 6 mo | -1.3 (-2.5,-0.1) | -1.4 (-2.5,-0.2) | -0.8 (-1.8,0.2) | -0.4 (-0.7,-0.2) | -0.5 (-0.8,-0.3) | -0.1 (-0.3,0.1) | <0.001 |
| Severity 12 mo | -1.3 (-2.5,-0.3) | -1.4 (-2.5,-0.2) | -0.8 (-2.2,0.1) | -0.4 (-0.7,-0.2) | -0.4 (-0.6,-0.2) | 0.0 (-0.1,0.2) | <0.001 |
| Intensity 3 mo a | -0.8 (-1.8,0.0) | -0.8 (-2.0,0.0) | -0.5 (-1.5,0.2) | -0.3 (-0.5,-0.2) | -0.3 (-0.5,-0.1) | 0.0 (-0.1,0.2) | <0.001 |
| Intensity 6 mo | -1.0 (-2.0,0.0) | -1.0 (-2.2,0.0) | -0.8 (-1.5,0.2) | -0.3 (-0.5,-0.1) | -0.3 (-0.5,-0.2) | -0.1 (-0.3,0.1) | <0.001 |
| Intensity 12 mo | -1.0 (-2.2,0.0) | -1.0 (-2.2,0.0) | -0.8 (-2.0,0.2) | -0.3 (-0.5,-0.1) | -0.2 (-0.4,-0.1) | 0.0 (-0.1,0.2) | <0.001 |
| Interference 3 mo a | -1.3 (-2.4,-0.1) | -1.3 (-2.6,0.0) | -0.7 (-1.9,0.1) | -0.5 (-0.7,-0.3) | -0.5 (-0.7,-0.3) | 0.0 (-0.2,0.2) | <0.001 |
| Interference 6 mo | -1.4 (-2.9,0.0) | -1.6 (-2.9,-0.1) | -0.9 (-2.1,0.1) | -0.6 (-0.8,-0.3) | -0.6 (-0.9,-0.4) | -0.1 (-0.4,0.2) | <0.001 |
| Interference 12 mo | -1.6 (-3.0,-0.1) | -1.6 (-3.0,-0.1) | -1.0 (-2.6,0.1) | -0.5 (-0.8,-0.3) | -0.5 (-0.7,-0.3) | 0.0 (-0.1,0.3) | <0.001 |
| Social role 3 mo a | 1.8 (-2.0,5.8) | 1.9 (-1.9,6.0) | 0.0 (-2.2,4.3) | 0.9 (0.1,1.7) | 1.5 (0.7,2.2) | 0.5 (-0.2,1.3) | <0.001 |
| Social role 6 mo | 1.9 (-1.9,6.5) | 1.9 (-1.9,7.4) | 1.5 (-3.2,5.5) | 1.3 (0.4,2.2) | 1.7 (0.9,2.6) | 0.4 (-0.5,1.4) | <0.001 |
| Social role 12 mo | 1.9 (-1.9,7.5) | 2.0 (-1.7,7.7) | 0.0 (-3.2,5.8) | 1.4 (0.4,2.3) | 1.4 (0.8,2.1) | 0.1 (-0.7,0.8) | <0.001 |
| Physical function 3 mo a | 1.6 (-0.8,3.6) | 1.2 (-0.8,3.8) | 0.9 (-1.4,3.2) | 0.6 (0.1,1.1) | 0.8 (0.3,1.2) | 0.1 (-0.3,0.6) | 0.002 |
| Physical function 6 mo | 1.7 (-0.8,4.4) | 1.2 (-0.9,4.4) | 1.0 (-1.0,3.6) | 0.8 (0.3,1.4) | 0.5 (0.1,0.9) | -0.3 (-0.8,0.2) | <0.001 |
| Physical function 12 mo | 1.9 (-0.9,5.0) | 1.3 (-1.2,4.6) | 0.9 (-1.7,3.6) | 1.1 (0.5,1.7) | 0.8 (0.2,1.5) | -0.3 (-0.9,0.4) | <0.001 |

**PDF pp. 17-18, eTable 11 (relationship group S005-ET11).** Raw-score medians (IQR), unadjusted mean differences (95% CI), and omnibus P; same `a` definition and `b` unadjusted linear-GEE definition as eTable 10. Page 18 contains only these footnotes, not a separate result.

| Outcome / time | PT | HC | UC | PT-UC | HC-UC | HC-PT | P |
|---|---|---|---|---|---|---|---|
| Severity 3/6/12 mo | 5.1 (4.9,5.2); 5.0 (4.8,5.1); 4.8 (4.6,4.9) | 4.6 (4.4,4.7); 4.4 (4.2,4.6); 4.2 (4.1,4.4) | 4.6 (4.5,4.7); 4.4 (4.2,4.5); 4.3 (4.2,4.5) | -0.5 (-0.7,-0.3); -0.6 (-0.8,-0.3); -0.5 (-0.8,-0.3) | -0.5 (-0.7,-0.3); -0.6 (-0.8,-0.3); -0.4 (-0.6,-0.2) | 0.0 (-0.2,0.2); -0.0 (-0.2,0.2); 0.1 (-0.1,0.3) | all <0.001 |
| Intensity 3/6/12 mo | 4.9 (4.7,5.0); 4.8 (4.6,4.9); 4.6 (4.4,4.7) | 4.5 (4.3,4.6); 4.4 (4.2,4.5); 4.2 (4.1,4.4) | 4.5 (4.4,4.6); 4.4 (4.3,4.5); 4.3 (4.2,4.4) | -0.4 (-0.6,-0.2); -0.4 (-0.6,-0.2); -0.3 (-0.6,-0.1) | -0.3 (-0.5,-0.1); -0.4 (-0.6,-0.2); -0.2 (-0.4,-0.1) | 0.0 (-0.2,0.2); -0.0 (-0.2,0.2); 0.1 (-0.1,0.3) | all <0.001 |
| Interference 3/6/12 mo | 5.2 (5.0,5.3); 5.1 (4.9,5.2); 4.9 (4.7,5.1) | 4.6 (4.4,4.8); 4.4 (4.2,4.6); 4.2 (4.0,4.4) | 4.6 (4.5,4.7); 4.4 (4.2,4.6); 4.3 (4.2,4.5) | -0.6 (-0.8,-0.3); -0.7 (-0.9,-0.4); -0.6 (-0.9,-0.4) | -0.6 (-0.8,-0.4); -0.7 (-0.9,-0.4); -0.5 (-0.8,-0.3) | 0.0 (-0.2,0.2); -0.0 (-0.3,0.2); 0.1 (-0.1,0.3) | all <0.001 |
| Social role 3/6/12 mo | 43.4 (42.8,44.0); 43.6 (42.9,44.2); 43.9 (43.3,44.6) | 44.6 (43.9,45.3); 45.4 (44.7,46.0); 45.8 (45.1,46.5) | 44.8 (44.4,45.2); 45.1 (44.7,45.4); 45.3 (44.8,45.8) | 1.2 (0.3,2.1); 1.8 (0.9,2.7); 1.8 (0.9,2.8) | 1.4 (0.7,2.2); 1.5 (0.8,2.2); 1.4 (0.5,2.2) | 0.2 (-0.5,1.0); -0.3 (-1.0,0.4); -0.5 (-1.3,0.3) | 0.001; <0.001; <0.001 |
| Physical function 3/6/12 mo | 37.7 (37.1,38.2); 37.9 (37.3,38.4); 37.9 (37.3,38.4) | 38.2 (37.7,38.8); 38.9 (38.4,39.5); 39.1 (38.5,39.7) | 38.2 (37.7,38.8); 38.3 (37.8,38.8); 38.8 (38.1,39.4) | 0.6 (-0.2,1.3); 1.1 (0.3,1.9); 1.2 (0.4,2.0) | 0.6 (-0.2,1.3); 0.4 (-0.3,1.1); 0.9 (0.0,1.8) | 0.0 (-0.8,0.8); -0.6 (-1.4,0.1); -0.3 (-1.2,0.6) | 0.212; 0.005; 0.001 |
| PGIC-Pain 3/6/12 mo | 2.9 (2.8,2.9); 2.8 (2.7,2.9); 2.8 (2.7,2.9) | 2.0 (1.0,3.0); 2.1 (2.0,2.2); 2.1 (2.0,2.2) | 1.9 (1.9,2.0); 2.1 (2.0,2.2); 2.2 (2.1,2.3) | -0.8 (-0.9,-0.6); -0.7 (-0.8,-0.5); -0.7 (-0.8,-0.5) | -0.9 (-1.0,-0.8); -0.7 (-0.8,-0.5); -0.6 (-0.7,-0.4) | -0.2 (-0.3,-0.0); -0.0 (-0.2,0.1); 0.1 (-0.1,0.2) | all <0.001 |
| PGIC-General 3/6/12 mo | 2.7 (2.6,2.7); 2.5 (2.4,2.6); 2.6 (2.4,2.7) | 2.0 (1.0,2.0); 2.0 (1.9,2.1); 1.9 (1.8,2.1) | 1.6 (1.5,1.6); 1.8 (1.7,1.9); 1.9 (1.7,2.0) | -0.8 (-0.9,-0.6); -0.6 (-0.7,-0.4); -0.6 (-0.8,-0.4) | -1.1 (-1.2,-1.0); -0.8 (-0.9,-0.6); -0.7 (-0.8,-0.5) | -0.3 (-0.5,-0.2); -0.2 (-0.3,-0.0); -0.1 (-0.2,0.1) | all <0.001 |

**PDF p. 19 (fresh direct extraction):** eReferences only: Zou (2004), Wang and Fitzmaurice (2006), and White and Thompson (2003). No result-relevant quantitative relationship, table, or statistical definition occurs on this page.

## DOC-006: complete native worksheet eTable 3

**Table identity and definitions, cells A1:J4 and A110:J114 (relationship group N-S005-WK-HEAD).** Title: baseline characteristics overall and by primary-outcome completion: missing all 3 follow-up points, missing 1/2 follow-ups, or all follow-ups observed. The four value columns are Overall (B; N=2331), Missing All (C; N=295), Missing 1 or 2 (D; N=468), All Observed (E; N=1568). G is pre-specified adjustment-variable flag; H, I, J are respectively P values related to primary MCID outcome, overall non-response, and missingness at the 3-month primary time point. Footnote a: missing is n and excluded from percentage denominator. b: HEAL common data element. c: EHR-derived. Sex note: self-reported sex unless missing, then EHR sex. Bold means relation (P<0.10) to 3-month MCID after pre-specified adjustment and to missingness at 3 months or all time points after adjustment.

All B:E strings below are displayed native values in column order **Overall | Missing all | Missing 1/2 | All observed**. A cell range is the exact authoritative workbook location. `X` is the displayed adjustment-variable flag; every listed P is a displayed cached value, with no formula.

### Clinical site and demographics (A4:J48)

- **A4:E8 Clinical site, N (%); G4=X:** A: `566 (24.3) | 51 (17.3) | 109 (23.3) | 406 (25.9)`; B: `609 (26.1) | 68 (23.1) | 162 (34.6) | 379 (24.2)`; C: `606 (26.0) | 119 (40.3) | 117 (25.0) | 370 (23.6)`; D: `550 (23.6) | 57 (19.3) | 80 (17.1) | 413 (26.3)`.
- **A10:E11:** Age years c, mean (sd): `58.8 (14.3) | 56.3 (15.2) | 57.7 (13.8) | 59.6 (14.1)`, G10=X. Female*,b,c N (%): `1713 (73.5) | 206 (69.8) | 343 (73.3) | 1164 (74.2)`, G11=X.
- **A12:E17 Education b:** high school or less `627 (27.2)|86 (29.5)|146 (31.8)|395 (25.4)`; associate/technical `657 (28.5)|100 (34.2)|139 (30.3)|418 (26.9)`; college `597 (25.9)|64 (21.9)|109 (23.7)|424 (27.2)`; doctoral/postgraduate `426 (18.5)|42 (14.4)|65 (14.2)|319 (20.5)`; missing `24|3|9|12`. H12=0.016 (cached 0.0156), J12=0.050.
- **A18:E19 Not employed,b N (%):** `1234 (53.4)|135 (45.9)|213 (46.3)|886 (57)`; missing `22|1|8|13`. H18=<0.001, I18=0.023 (cached 0.0228), J18=0.059 (cached 0.0591).
- **A20:E26 Household income,b N (%):** <$24,999 `273 (13.7)|40 (16.4)|53 (13.7)|180 (13.2)`; $25,000-$49,999 `461 (23.1)|65 (26.6)|93 (24)|303 (22.2)`; $50,000-$99,999 `736 (36.9)|86 (35.2)|131 (33.9)|519 (38)`; $100,000-$149,999 `316 (15.8)|29 (11.9)|65 (16.8)|222 (16.3)`; >=150000 `209 (10.5)|24 (9.8)|45 (11.6)|140 (10.3)`; missing `336 (14.4)|51 (17.3)|81 (17.3)|204 (13)`. H20=0.019 (cached 0.0186).
- **A27:E28 Married/domestic partnered,b N (%):** `1507 (65.5)|181 (61.6)|290 (63)|1036 (67)`; missing `31|1|8|22`.
- **A29:E37 Race/ethnicity,b N(%):** White non-Hispanic `1699 (75)|212 (74.1)|313 (70.3)|1174 (76.5)`; Black/African American non-Hispanic `350 (15.4)|40 (14)|96 (21.6)|214 (13.9)`; Hispanic `77 (3.4)|15 (5.2)|13 (2.9)|49 (3.2)`; Asian `27 (1.2)|2 (0.7)|4 (0.9)|21 (1.4)`; American Indian/Alaska Native `28 (1.2)|7 (2.4)|3 (0.7)|18 (1.2)`; Native Hawaiian/other Pacific Islander `2 (0.1)|0 (0)|2 (0.4)|0 (0)`; >1 race `83 (3.7)|10 (3.5)|14 (3.1)|59 (3.8)`; missing `65|9|23|33`.
- **A38:E48:** Rural/medically underserved residency,c N(%): `1030 (44.2)|136 (46.1)|204 (43.6)|690 (44)`, G38=X. Any negative social determinant N(%): `758 (33)|125 (42.7)|174 (38.2)|459 (29.6)`; missing `33|2|12|19`; H39=0.064 (cached .0636), I39=0.020 (cached .0196). Financial strain `567 (24.5)|93 (31.6)|130 (28.2)|344 (22.1)`; missing `19|1|7|11`; H41=0.053 (cached .0525). Food insecurity `333 (14.4)|59 (20.1)|78 (17.0)|196 (12.6)`; missing `21|2|8|11`; H43=0.058 (cached .0576). Transportation insecurity `170 (7.3)|29 (9.8)|37 (7.9)|104 (6.7)`; missing `12|0|2|10`; H45=0.031 (cached .0308). Housing insecurity `364 (15.9)|75 (25.7)|88 (19.3)|201 (13.0)`; missing `35|3|12|20`; I47=0.0002.

### Clinical characteristics (A49:J94)

- **A51:E56:** pain-related encounters/year,c mean(sd) `9.3 (9.4)|7.3 (7)|9.8 (10.8)|9.5 (9.3)`, I51=0.001. Musculoskeletal conditions/year,c: mean(sd) `2.5 (1.3)|2.5 (1.3)|2.5 (1.3)|2.5 (1.3)`; >1 N(%) `1710 (73.4)|213 (72.2)|353 (75.4)|1144 (73)`, G54=X, H54=0.0051. Long-term opioid use,c N(%) `163 (9.6)|14 (8.2)|31 (9.1)|118 (10)`; missing (data only 3/4 sites) `634|124|126|384`.
- **A58:E73 specific pain condition in last 3 months:** back `1225 (52.6)|162 (54.9)|258 (55.1)|805 (51.4)`, missing `2|0|0|2`, H58=0.062 (cached .0615); neck `622 (26.7)|83 (28.1)|126 (26.9)|413 (26.3)`, missing blank cells, H60=0.0017; hand/arm/shoulder `883 (37.9)|120 (40.7)|176 (37.7)|587 (37.5)`, missing `2|0|1|1`; hip/knee/foot `1476 (63.3)|176 (59.7)|303 (64.7)|997 (63.6)`, missing `0|0|blank|blank`; headache/migraine `343 (14.7)|56 (19)|72 (15.4)|215 (13.7)`, missing `1|0|0|1`, H66=0.0323; abdominal/pelvic/genital `197 (8.5)|19 (6.4)|39 (8.4)|139 (8.9)`, missing `4|0|1|3`, H68=0.010; toothache/jaw `143 (6.1)|18 (6.1)|28 (6)|97 (6.2)`, missing `1|1|0|0`; whole-body pain `460 (19.8)|60 (20.4)|104 (22.3)|296 (18.9)`, missing `4|1|1|2`, H72=<0.001.
- **A74:E78 pain duration,b N(%):** <=1 year `107 (4.6)|16 (5.4)|21 (4.5)|70 (4.5)`; >1-5 years `614 (26.4)|84 (28.5)|123 (26.3)|407 (26)`; >5 years `1609 (69.1)|195 (66.1)|324 (69.2)|1090 (69.6)`; missing `1|0|0|1`; H74=<0.001.
- **A80:E94 health conditions:** anxiety/depression diagnosis,c N(%) `965 (41.4)|141 (47.8)|209 (44.7)|615 (39.2)`, G80=X. PHQ-8 (0-24),b mean(sd) `9.8 (5.6)|11 (5.5)|10.3 (5.8)|9.5 (5.5)`, H81=<0.001, I81=0.010 (cached .0095). Current depression PHQ-8>=10,c No.(%) `1116 (47.9)|162 (54.9)|243 (51.9)|711 (73.2)`; missing `2|0|0|2`. GAD-7 (0-21),b mean(sd) `6.9 (5.4)|7.9 (5.3)|7 (5.2)|6.7 (5.4)`, H84=0.033 (cached .0327), I84=0.033 (cached .0331). Moderate/severe anxiety GAD-7>=10,c No.(%) `648 (27.8)|102 (34.6)|126 (27.0)|420 (26.8)`; missing `2|0|2|0`. Substance-use diagnosis,c N(%) `86 (3.7)|16 (5.4)|22 (4.7)|48 (3.1)`, H87=0.011 (cached .0108). Charlson index,c mean(sd) `1.2 (1.7)|1 (1.6)|1.3 (1.9)|1.1 (1.6)`; 0 conditions `1162 (49.8)|156 (52.9)|225 (48.1)|781 (49.8)`; 1-2 `812 (34.8)|95 (32.2)|160 (34.2)|557 (35.5)`; >=3 `357 (15.3)|44 (14.9)|83 (17.7)|230 (14.7)`. PROMIS sleep disturbance,b mean(sd) `58.8 (8.3)|59.2 (9)|59.4 (8)|58.5 (8.2)`; moderate/severe T-score >60,c N.(%) `1005 (43.3)|136 (46.4)|221 (47.6)|648 (41.5)`; missing `12|2|4|6`.

### Baseline outcomes (A95:J109)

- **A96:E98 primary:** pain severity (0-10),b: mean(sd) `5.9 (1.7)|6 (1.7)|6.1 (1.7)|5.8 (1.6)`; >=7 score N(%) `594 (25.5)|89 (30.2)|147 (31.4)|358 (22.8)`.
- **A100:E109 secondary:** pain intensity (0-10),b mean(sd) `5.5 (1.6)|5.7 (1.7)|5.7 (1.6)|5.4 (1.6)`, H100=0.0492. Pain-related interference (0-10),b mean(sd) `6.1 (1.9)|6.2 (1.9)|6.3 (2)|6 (1.9)`, H101=0.0492. PROMIS social role mean(sd) `42.5 (7.4)|41.8 (7.6)|42.1 (7.7)|42.7 (7.3)`, H102=<.0001; <=40,b labeled mean(sd), values `818 (35.7)|113 (38.8)|180 (38.7)|525 (34.2)`, missing `38|4|3|31`. PROMIS physical function,b mean(sd) `36.6 (5.9)|36.8 (6.2)|35.9 (6.1)|36.7 (5.8)`, H105=<.0001; <=40,b labeled mean(sd), values `1709 (74.1)|209 (72.6)|357 (76.8)|1143 (73.6)`, missing `24|7|3|14`. PEG (0-30),b mean(sd) `20.5 (4.4)|21 (4.5)|21.2 (4.5)|20.2 (4.4)`, missing `1|0|0|1`, H108=0.0245, I108=0.0405.

## Relationship and coverage notes

- **Numerical relationship inventory:** DOC-005 includes 9 binary outcome/timepoint/three-contrast RR relationships (eTable 9), 15 continuous outcome/timepoint/three-contrast mean-difference plus P relationships (eTable 10), and 21 raw-score outcome/timepoint/three-contrast mean-difference plus P relationships (eTable 11), all at the exact PDF pages above. DOC-006 includes every populated native worksheet cell across A1:J115, mapped by its exact cells/ranges above.
- **Direct check inputs retained:** eTable 9 exposes numerator/denominator/percent triads; DOC-006 identifies percentage denominators through A110. Displayed P values are source facts; values such as `<0.001` and `<.0001` are not literal-zero P values.
- **Coverage:** DOC-005 pp. 15, 16, 17, 18, and 19 mapped (5/5); DOC-006 worksheet `eTable 3` A1:J115 mapped (1/1). No OCR was needed. The only non-result page in this shard is DOC-005 p. 19.
