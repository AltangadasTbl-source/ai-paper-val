# Statistical relationship inventory — PASS 1 primary shard

Runtime agent: `/root/statistical_pass1`; run model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. Scope: every main-paper inferential relationship, every protocol inferential/design/power relationship, report eTables2/4 and all report eFigures/models. Independent extra shard owns only eTables3/5/6: S121-S222. Numeric namespace 101 through 120 remains unassigned and contains no omitted evidence. This artifact owns S001-S100; the coordinator performs the canonical merge. All source roles below are assigned by content: DOC001 main REPORT, DOC002 protocol PLAN, DOC003 results/methods supplement REPORT; DOC004 data-sharing page REPORT contains no inferential relationship.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Inputs are exact supplied PDFs, new evidence maps and source-linked usable locators, with no earlier findings or conclusions. Direct Poppler26.01.0 CPU extraction produced `statistics/protocol_statistical_direct.txt` (DOC002 pp26-36) and `statistics/supplement_outcomes_direct.txt` (DOC003 pp15-18). Commands: `pdftotext -layout -f 26 -l 36 joi240004supp1_prod_1721756962.80052.pdf .../statistics/protocol_statistical_direct.txt` and `pdftotext -layout -f 15 -l 18 joi240004supp2_prod_1721756962.82552.pdf .../statistics/supplement_outcomes_direct.txt`. No OCR/fallback environment/new rendering. Visually inspected source-linked images DOC001 p6 and fresh mapper images DOC002 pp26/28; protocol formulas/power illustrations additionally have complete visual confirmation in the new support map. Exact direct native pages supplied the other stated text.

Table row records contain every group estimate and interval, together with the between-group test: they do not collapse independently tested outcomes. Genuine repeated occurrences are cross-referenced. Every record checks all estimates in that row for ordered endpoints and containment, and checks its corresponding group CI/test. Limits on exact test reconstruction are named, rather than silently filling in degrees of freedom, sidedness, covariance or estimator. All CIs below are printed95% unless specified; parentheses for raw values are SD and square brackets for raw medians are IQR. Medical M; surgery B. No candidate IDs or adjudications are assigned.

## Shared row check specification

MainTable2 headers M baseline96/year7 82 and B baseline166/year7 136 are displayed headers, not outcome-specific observed denominators. eTable2 has no outcome-specific denominators; eTable1 separately describes130 participants reaching12years. Raw summaries and model estimates differ by design. Continuous group contrasts are surgery change minus medical change (null0); within-group fold changes and all odds ratios have null1. Every point is within its ordered interval. Every numerical group CI excludes/includes its null consistently with its own printed P at.05, including nonsignificant rows; year12 remission has no group CI to test. No inferential conclusion is generated from raw IQR/SD ranges. All significance conclusions and effect directions reconcile within each displayed row. Exact P reconstruction is limited by absent reported test distribution/degrees of freedom; normal z values from interval width are diagnostic only. MainTable2 binary log-interval symmetry has one reproduced exception S013/F-ST1-007; every other binary cell permits its log-symmetric center within half-unit rounding bounds.

### S001 — Year-7 HbA1c net change, percentage points

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 1; MAIN-076. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 8.2(1.2)→8.0(1.8); −0.2[−0.5,0.2]; B: 8.7(1.7)→7.2(1.4); −1.6[−1.8,−1.3]; group estimate/95%CI: −1.4[−1.8,−1.0]; group P <.001.
- **Checks:** Shared row specification applied to all three tabulated intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Matched abstract/p3 between-group −1.4[−1.8,−1.0],P<.001 agrees. The positive abstract/narrative surgery point1.6 lies outside its signed negative interval: F-ST1-009 under routeA1. A deliberate reduction-magnitude reading is preserved as an alternative. Planned scale comparison S064/F-ST1-002.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S002 — Year-7 Fasting glucose relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 2; MAIN-077. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 156.5(50.0)→144.6(57.3); −3.8[−14.8,7.2]; B: 172.0(69.7)→125.1(47.0); −14.1[−22.0,−6.3]; group estimate/95%CI: −10.3[−23.6,2.9]; group P .13.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S003 — Year-7 Weight relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 3; MAIN-078. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 105.6(15.5)→96.2(16.6); −8.3[−10.5,−6.1]; B: 103.5(15.3)→83.6(15.8); −19.9[−21.6,−18.1]; group estimate/95%CI: −11.6[−14.3,−8.9]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S004 — Year-7 SBP relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 4; MAIN-079. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 129.7(15.8)→128.7(15.7); −1.1[−3.9,1.7]; B: 134.4(17.7)→128.6(15.3); −3.4[−5.6,−1.2]; group estimate/95%CI: −2.3[−5.8,1.1]; group P .19.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S005 — Year-7 DBP relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 5; MAIN-080. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 79.5(9.6)→74.6(9.7); −4.3[−7.0,−1.6]; B: 80.4(10)→74.3(10.4); −6.0[−8.1,−3.8]; group estimate/95%CI: −1.7[−5.0,1.7]; group P .32.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S006 — Year-7 LDL relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 6; MAIN-081. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 96.3(33.2)→97.6(36.6); 5.5[−3.3,14.3]; B: 100.3(34.2)→103.1(36.4); 10.8[3.8,17.9]; group estimate/95%CI: 5.4[−5.6,16.3]; group P .34.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S007 — Year-7 HDL relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 7; MAIN-082. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 44.3(13.2)→52.0(17.0); 20.5[14.5,26.6]; B: 42.9(11.6)→56.5(16.5); 37.4[32.6,42.3]; group estimate/95%CI: 16.9[9.4,24.4]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S008 — Year-7 Total cholesterol relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 8; MAIN-083. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 172.6(38.5)→171.7(41.6); −0.7[−5.6,4.1]; B: 179.6(44.8)→181.4(40.6); 4.9[1.0,8.7]; group estimate/95%CI: 5.6[−0.4,11.6]; group P .07.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S009 — Year-7 Triglyceride relative change, %; raw median[IQR]

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 9; MAIN-084. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 140[92.5,221.5]→125[88,178.3]; 2.3[−8.6,13.2]; B: 144[103,231]→107[82,142]; −19.0[−27.8,−10.2]; group estimate/95%CI: −21.3[−34.9,−7.8]; group P .002.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S010 — Year-7 Serum creatinine relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 10; MAIN-085. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 0.7(0.2)→0.8(0.4); 9.5[1.8,17.1]; B: 0.7(0.2)→0.8(0.2); 10.5[4.4,16.7]; group estimate/95%CI: 1.1[−8.4,10.5]; group P .83.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S011 — Year-7 Urine albumin:creatinine fold change; raw median[IQR]

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 11; MAIN-086. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 6[4,12]→8[4,13.5]; 1.3[0.9,1.9]; B: 9[4.5,23]→6[4,10]; 0.9[0.7,1.2]; group estimate/95%CI: −0.4[−1.0,0.1]; group P .10.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S012 — Year-7 Remission %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 12; MAIN-087. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 0.6→6.2; 10.4[0.4,279.4]; B: 0.6→18.2; 36.2[1.9,699.0]; group estimate/95%CI: 3.39[1.25,9.17]; group P .02.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p4 OR3.4[1.3,9.2],P=.02 agrees after rounding; p1 rates6.2/18.2 agree.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S013 — Year-7 Diabetes medication %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 13; MAIN-088. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 99.0→96.0; 0.10[0.01,3.27]; B: 97.6→60.5; 0.03[0.01,0.11]; group estimate/95%CI: 0.09[0.03,0.24]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. The medical within-group OR interval does not reproduce the log-symmetric center pattern of the same display: F-ST1-007. Medical baseline-change P=.19 (p4) and surgical P<.001 (pp4/6) agree with their intervals' null inclusion/exclusion.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S014 — Year-7 Oral/GLP1 only %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 14; MAIN-089. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 57.3→40.0; 0.53[0.29,0.97]; B: 47.0→44.5; 0.74[0.46,1.20]; group estimate/95%CI: 0.98[0.53,1.82]; group P .95.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S015 — Year-7 Insulin and/or oral/GLP1 %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 15; MAIN-090. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 41.7→56.0; 1.93[1.07,3.46]; B: 50.6→16.0; 0.18[0.11,0.31]; group estimate/95%CI: 0.13[0.06,0.29]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p6 insulin16% surgery vs56% medical,P<.001 agrees.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S016 — Year-7 HbA1c<7.0 %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 16; MAIN-091. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 11.7→26.7; 2.77[1.38,5.54]; B: 15.5→54.1; 6.42[3.63,11.4]; group estimate/95%CI: 3.22[1.76,5.88]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p4 OR3.2[1.8,5.9],P<.001 agrees after rounding.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S017 — Year-7 HbA1c<6.5 %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 17; MAIN-092. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 8.3→17.3; 2.30[1.19,4.47]; B: 12.0→37.7; 4.44[2.46,8.01]; group estimate/95%CI: 2.89[1.48,5.64]; group P .002.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p4 glycemic-threshold P=.002 agrees; < versus ≤ symbol alone does not establish different extracted results.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S018 — Year-12 HbA1c net change, percentage points

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 1, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 7.9(1.4); −0.3[−0.8,0.1]; B: 7.3(1.5); −1.4[−1.7,−1.1]; group estimate/95%CI: −1.1[−1.7,−0.5]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Matched main abstract/p3 same−1.1[−1.7,−.5] butP=.002 does not reconcile with supplementaryP<.001: F-ST1-001. Each significance conclusion is internally compatible with its CI. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S019 — Year-12 Fasting glucose relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 2, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 137.6(45.4); −6[−19.6,7.6]; B: 130.3(47.2); −11.1[−20,−2.2]; group estimate/95%CI: −5.1[−21,10.9]; group P .53. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S020 — Year-12 Weight relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 3, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 92.8(13.5); −10.8[−13.5,−8.2]; B: 83.7(17.8); −19.3[−21.3,−17.3]; group estimate/95%CI: −8.4[−11.7,−5.2]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Model difference−8.4 vsrounded within-group difference−8.5 reconciles: inputs yield[−8.6,−8.4],printed contrast[−8.45,−8.35],overlap. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S021 — Year-12 SBP relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 4, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 125.6(15.9); −4.7[−8.5,−1]; B: 128.4(15.8); −4.5[−7.1,−1.9]; group estimate/95%CI: 0.3[−4.2,4.7]; group P .91. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Difference.3 vsrounded component difference.2 reconciles: inputs yield[.1,.3],printed[.25,.35],overlap. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S022 — Year-12 DBP relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 5, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 71.8(10.2); −7.7[−11.4,−4]; B: 74.7(10); −6.6[−9.1,−4.1]; group estimate/95%CI: 1.1[−3.2,5.5]; group P .61. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S023 — Year-12 LDL relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 6, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 90.9(39.4); −7.9[−19.9,4]; B: 87.6(31.2); −11.9[−20.2,−3.7]; group estimate/95%CI: −4[−18.2,10.2]; group P .58. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S024 — Year-12 HDL relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 7, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 50.5(13.2); 16.6[8.4,24.7]; B: 57.7(17.9); 38.1[32.5,43.7]; group estimate/95%CI: 21.5[11.9,31.2]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S025 — Year-12 Total cholesterol relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 8, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 170.8(48.1); −4.2[−11.1,2.6]; B: 168.9(38.9); −5.5[−10,−0.9]; group estimate/95%CI: −1.2[−9.3,6.9]; group P .77. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Difference−1.2 vsrounded component difference−1.3 reconciles within input/contrast rounding bounds. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S026 — Year-12 Triglyceride relative change, %; raw median[IQR]

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 9, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 119[89,164]; 9.8[−4.9,24.5]; B: 104[75,126.8]; −23.3[−33.3,−13.2]; group estimate/95%CI: −33.1[−50.5,−15.7]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S027 — Year-12 Serum creatinine relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 10, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 0.9(0.7); 29.5[19.3,39.7]; B: 0.9(0.3); 20.3[13.3,27.3]; group estimate/95%CI: −9.2[−21.2,2.9]; group P .14. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S028 — Year-12 Urine albumin:creatinine fold change; raw median[IQR]

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 11, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 12.1[6.4,30.8]; 2.2[1.4,3.6]; B: 8.1[5.2,20.1]; 1.5[1.1,2.1]; group estimate/95%CI: −0.7[−1.9,0.4]; group P .20. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S029 — Year-12 Remission %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 12, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 0%; OR NA; footnote modeled probability2e−16; B: 12.7%; 23.6[1.2,465.3]; group estimate/95%CI: NA; footnote almost infinite; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Medical probability2e−16 is described as yielding near-zero within-group and almost-infinite group OR; NA entries are not zero numerical ORs. The reported groupP<.001 has no groupCI, so exact Wald/test compatibility cannot be assessed. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S030 — Year-12 Diabetes medication %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 13, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 93.8; 0.06[0.002,2.16]; B: 82.6; 0.10[0.02,0.39]; group estimate/95%CI: 0.45[0.15,1.36]; group P .16. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S031 — Year-12 Oral/GLP1 only %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 14, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 34.4; 0.45[0.23,0.85]; B: 53.5; 1.14[0.70,1.85]; group estimate/95%CI: 1.80[0.85,3.82]; group P .12. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S032 — Year-12 Insulin and/or oral/GLP1 %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 15, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 59.4; 2.31[1.23,4.32]; B: 29.1; 0.40[0.25,0.64]; group estimate/95%CI: 0.25[0.10,0.58]; group P .001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S033 — Year-12 HbA1c<7.0 %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 16, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 29.4; 3.15[1.20,8.30]; B: 54.6; 6.57[3.56,12.1]; group estimate/95%CI: 2.90[1.15,7.29]; group P .02. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S034 — Year-12 HbA1c<6.5 %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 17, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 19.6; 2.68[0.92,7.81]; B: 40.0; 4.90[2.54,9.48]; group estimate/95%CI: 2.75[1.09,6.90]; group P .03. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S035 — Nutritional least-square Hemoglobin g/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row1; SUPPORT-B-036.
- **Printed inputs:** M13.7 SE0.2; B13 SE0.1; difference−0.8 SE0.2; P<.001.
- **Check:** All rounding intervals for means permit−0.8. Diagnostic z=−4; significant direction coheres. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S036 — Nutritional least-square Iron μg/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row2; SUPPORT-B-036.
- **Printed inputs:** M83.9 SE3.2; B85.3 SE2.5; difference1.4 SE4.1; P=.74.
- **Check:** 85.3−83.9=1.4; diagnostic z=.341, normal P≈.733; rounded inputs permit .74. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S037 — Nutritional least-square Vitamin B12 pg/mL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row3; SUPPORT-B-036.
- **Printed inputs:** M760.8 SE105.1; B1173.2 SE80.6; difference412.4 SE132.4; P=.002.
- **Check:** 1173.2−760.8=412.4; diagnostic z=3.115, normal P≈.00184; .002 compatible. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S038 — Nutritional least-square Vitamin D ng/mL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row4; SUPPORT-B-036.
- **Printed inputs:** M35.2 SE1.8; B40.5 SE1.4; difference5.3 SE2.3; P=.02.
- **Check:** 40.5−35.2=5.3; diagnostic z=2.304, normal P≈.0212; .02 compatible. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S039 — Nutritional least-square Calcium mg/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row5; SUPPORT-B-036.
- **Printed inputs:** M9.6 SE0.04; B9.5 SE0.03; difference−0.1 SE0.0; P=.03.
- **Check:** SE0.0 is printed one-decimal precision, interval[0,.05), not established zero variance. Unrounded contrast/SE can yield .03. No division by printed0.0. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S040 — Nutritional least-square PTH pg/mL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row6; SUPPORT-B-036.
- **Printed inputs:** M51.1 SE3.3; B60.3 SE2.5; difference9.2 SE4.2; P=.03.
- **Check:** 60.3−51.1=9.2; diagnostic z=2.190, normal P≈.0285; .03 compatible. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S041 — Nutritional least-square Albumin g/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row7; SUPPORT-B-036.
- **Printed inputs:** M4.1 SE0.03; B4.1 SE0.02; difference−0.01 SE0.04; P=.72.
- **Check:** Mean intervals both[4.05,4.15) allow−.01. Contrast[−.015,−.005),SE[.035,.045) permit normal P from≈.668 to.912, including .72. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S042 — Procedure HbA1c contrasts

- **Exact location and role:** REPORT DOC001 p3 Figure2B narrative.
- **Printed inputs/specification:** RYGB change −1.7 (−2.0,−1.3)%; SG −2.0 (−2.6,−1.5)%; AGB −0.8 (−1.3,−0.2)%. AGB vs SG P=.007; vs RYGB P=.03; RYGB vs SG nonsignificant.
- **Check and reproduction/limits:** All three estimates are contained in ordered 95% CIs, with reductions in the stated direction. Pairwise P values test different contrasts from each procedure's individual change. Exact pairwise reproduction needs the covariance, degrees of freedom and adjustment family, which are not supplied.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S043 — Procedure weight contrasts

- **Exact location and role:** REPORT DOC001 p6 Figure2D narrative.
- **Printed inputs/specification:** Year-7 loss RYGB22.7%, AGB14.0%, RYGB vs AGB P<.001; SG19.7%, differences vs other procedures nonsignificant.
- **Check and reproduction/limits:** Greater loss for R than A agrees with the printed direction and P<.001. S comparisons are separately described as nonsignificant. No interval or standard error is printed for these pairwise tests.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S044 — PP HbA1c sensitivity

- **Exact location and role:** REPORT DOC001 p3; DOC003 p9 eFigure2A, p5 methods.
- **Printed inputs/specification:** Year-7 medical0.1 (−0.5,0.7)%, surgery−1.4 (−1.7,−1.2)%; difference−1.5 (−2.1,−0.9)%, P<.001.
- **Check and reproduction/limits:** Estimate containment, endpoint order, surgery-minus-medical arithmetic and CI/P significance agree. Robust IPW inference is explicitly stated. The planned additional postcrossover-censor sensitivity is tracked in F-ST1-004.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S045 — PP weight sensitivity

- **Exact location and role:** REPORT DOC001 pp6-7; DOC003 p9 eFigure2B.
- **Printed inputs/specification:** Year-7 medical/surgery loss5.6%/20.4%; year-12 7.7%/19.4%. eFigure2 caption gives the same year-7 values; no PP interval or P printed.
- **Check and reproduction/limits:** ITT and PP losses are explicitly distinct and match the supplementary figure caption at year 7. No PP confidence interval or P value is printed for the weight contrast; exact annual coordinates are unlabeled.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S046 — BMI subgroup HbA1c contrasts

- **Exact location and role:** REPORT DOC001 p7; DOC003 p13 eFigure6A.
- **Printed inputs/specification:** BMI<35: M−.4%, B−1.5%, difference−1.2 (−1.8,−.5)%; BMI≥35: M−.1%, B−1.6%, difference−1.5 (−2.1,−1.0)%; interaction P=.40. Year-7 absolute LS M/B8.3/7.4 low and8.1/7.0 high.
- **Check and reproduction/limits:** Both subgroup estimates are contained in ordered CIs excluding zero. The low-BMI change difference −1.1 vs printed −1.2 reconciles within half-unit intervals. P=.40 is an interaction, not either subgroup's individual effect test. Absolute LS means require their baseline-adjustment mapping before comparison with changes.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S047 — BMI subgroup weight contrasts

- **Exact location and role:** REPORT DOC001 p7; DOC003 p13 eFigure6B.
- **Printed inputs/specification:** BMI<35: losses M5.6%, B20.4%, difference14.8 (10.8,18.8)%, P<.001; BMI≥35: M10.1%, B19.3%, difference9.2 (5.6,12.9)%; interaction P=.03.
- **Check and reproduction/limits:** Within each BMI subgroup the surgery-minus-medical loss differences reproduce exactly, and the CIs exclude zero in the stated direction. P=.03 refers to the difference between subgroup effects; its covariance and standard error are absent.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S048 — Annual HbA1c LS trajectories

- **Exact location and role:** REPORT DOC001 p5 Figure2A/B; p3 allpostbaseline P<.001.
- **Printed inputs/specification:** Visits0-12, M/B and AGB/RYGB/SG least-square means plus raw boxplots; all contributor Ns in MAIN-068/069. Surgery higher baseline but lower at all postbaseline visits, narrative P<.001; no numerical point CI/SE.
- **Check and reproduction/limits:** All visits and procedures are mapped, including contributor counts. The boxes and whiskers show raw distributions, not confidence intervals. The stated postbaseline direction agrees with the plotted trajectories; exact point coordinates and per-visit test statistics are not printed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S049 — Annual weight LS trajectories

- **Exact location and role:** REPORT DOC001 p5 Figure2C/D; DOC003 p9 eFigure2B.
- **Printed inputs/specification:** Visits0-12, M/B and AGB/RYGB/SG least-square means plus raw boxplots; all contributor Ns in MAIN-070/071. Surgery/RYGB/SG show larger loss. Numeric confidence limits and point-specific tests not printed.
- **Check and reproduction/limits:** All annual group/procedure trajectories and contributor counts are mapped. Loss direction agrees with the narrative. Modeled baseline values cannot be treated as raw zero-change observations; unprinted numeric coordinates and confidence limits are not invented.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S050 — Annual remission inference

- **Exact location and role:** REPORT DOC001 p7 Figure3,p1,p4; DOC003 p15 remissionrow.
- **Printed inputs/specification:** Year-1 M0.5%, B50.8%; year-7 M6.2%, B18.2%, OR3.4 (1.3,9.2), P=.02; year-12 M0%, B12.7%, P<.001. Annual contributor Ns in MAIN-111/112.
- **Check and reproduction/limits:** Year-7 OR/CI rounding agrees between narrative and Table 2. Model-derived percentages are distinct from raw contributor-count ratios. Year-12 group OR/CI are NA with the near-zero medical probability explained; no finite OR or CI is inferred.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S051 — Incretin annual contrast

- **Exact location and role:** REPORT DOC001 p6; DOC003 p11 eFigure4.
- **Printed inputs/specification:** Visits0-12 incretin medication percentages, medical greater after baseline; overall P<.001. All annual bar readings retained in SUPPORT-B-020.
- **Check and reproduction/limits:** The overall longitudinal P<.001 agrees with greater medical incretin use after baseline. All annual bars are mapped. No CI, standard error, exact bar values or denominators are printed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S052 — Annual SBP contrast

- **Exact location and role:** REPORT DOC003 p12 eFigure5A; DOC001 p7.
- **Printed inputs/specification:** SBP least-square means±oneSE at visits0-12; overall P=.16. Full Ns SUPPORT-B-021.
- **Check and reproduction/limits:** Overall P=.16 is distinct from single-year .19/.91. One-SE bars are not 95% CIs; no significance conflict is present.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S053 — Annual HDL contrast

- **Exact location and role:** REPORT DOC003 p12 eFigure5B; DOC001 p7.
- **Printed inputs/specification:** HDL least-square means±oneSE at visits0-12; overall P<.001. Full Ns SUPPORT-B-022.
- **Check and reproduction/limits:** Overall P<.001 agrees with higher postoperative surgical HDL. One-SE bars are not 95% CIs, and the annual exact coordinates are not printed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S054 — Annual LDL contrast

- **Exact location and role:** REPORT DOC003 p12 eFigure5C; DOC001 p7.
- **Printed inputs/specification:** LDL least-square means±oneSE at visits0-12; overall P=.83. Full Ns SUPPORT-B-023.
- **Check and reproduction/limits:** Overall P=.83 is distinct from the year-7/year-12 tests. No numerical CI or test statistic is available for exact reproduction.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S055 — Annual triglyceride contrast

- **Exact location and role:** REPORT DOC003 p12 eFigure5D; DOC001 p7.
- **Printed inputs/specification:** Triglyceride least-square means±oneSE at visits0-12; overall P<.001. Full Ns SUPPORT-B-024.
- **Check and reproduction/limits:** Overall P<.001 agrees with lower postoperative surgical triglyceride levels. Model LS means are distinct from raw medians and IQRs.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S056 — BMI subgroup trajectories

- **Exact location and role:** REPORT DOC003 p13 eFigure6; DOC001 p7.
- **Printed inputs/specification:** Four group/BMI trajectories visits0-12. HbA1c least-square means±oneSE; weight percent initial loss. Year-7 caption values low M/B8.3/7.4 and high8.1/7.0; weight low5.6/20.4%, high10.1/19.3%.
- **Check and reproduction/limits:** All four BMI/group trajectories across all 13 visits are covered. Exact year-7 caption values and interaction tests are retained in the preceding subgroup records. The >35 versus ≥35 notation alone does not establish changed subgroup membership.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S057 — Reported primary LMM

- **Exact location and role:** REPORT DOC001 pp2-3; DOC003 pp4-5.
- **Printed inputs/specification:** ITT fixed group, visit, interaction, site and baseline HbA1c; zero-mean Gaussian participant random intercept; least-square means and linear contrasts; year-7 primary. E(Yt)=alpha_t+beta_t X+gamma^T Z; beta surgery−medical.
- **Check and reproduction/limits:** The stated longitudinal individual-level design and participant random intercept are coherent. Surgery-minus-medical contrasts are defined. Residual covariance, test distribution and degrees of freedom are unreported; no convention is imposed. F-ST1-002 tracks the primary outcome scale change.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S058 — Reported binary GEE

- **Exact location and role:** REPORT DOC001 p3; DOC003 pp4-5.
- **Printed inputs/specification:** Binary GEE: group, visit, interaction, site, baseline HbA1c; least-square estimates, sandwich standard errors; remission/control/medication values labeled odds ratios.
- **Check and reproduction/limits:** The reported GEE and sandwich approach is explicit. Odds-ratio identity comes from the table footnotes, without comparing adjusted ORs to crude counts. F-ST1-003 tracks the planned model change and F-ST1-007 tracks one interval that does not reproduce the pattern of the same display.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S059 — Reported continuous secondary models

- **Exact location and role:** REPORT DOC003 p4; DOC001 Table2/eTable2.
- **Printed inputs/specification:** Same primary mixed model for continuous secondary outcomes with site and baseline value. Table footnotes: HbA1c net change; UACR fold change; other numeric relative change.
- **Check and reproduction/limits:** Net HbA1c change, fold UACR change and relative changes are distinguished from raw group summaries. The same longitudinal model is described with outcome-specific baseline adjustment. No conflict is created merely from adjusted versus crude differences.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S060 — Reported IPW sensitivity

- **Exact location and role:** REPORT DOC003 p5; DOC001 p3.
- **Printed inputs/specification:** X_t switches0→1 at crossover. Stabilized weight product over k≤t of P(X_k|pastX)/P(X_k|pastX,pastHbA1c,Z); logistic fits, R ipw; truncation at2.5/97.5percentiles; weighted mixed model, robust sandwich; whole-population ATE.
- **Check and reproduction/limits:** Exposure switches at crossover; numerator and denominator histories have the stated temporal order. Weight truncation and robust inference are explicit, and assumptions are disclosed. The planned censoring-weight/postcrossover-censor components are tracked in F-ST1-004.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S061 — Reported missingness

- **Exact location and role:** REPORT DOC001 p3,p9; DOC003 pp5-6.
- **Printed inputs/specification:** Later entry causes absent years8-12; EMR recovery except fasting glucose; death/loss random censoring; monotone missingness MAR; mixed model/GEE described as accounting for missingness under MAR.
- **Check and reproduction/limits:** Structural absence of later follow-up and actual dropout are distinct. Random-censoring/MAR assumptions are disclosed. Their empirical suitability is not audited. The GEE missingness mechanism is not given, so no convention-dependent additional claim is made. F-ST1-004 tracks planned missing-data sensitivities.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S062 — Reported safety tests

- **Exact location and role:** REPORT DOC003 p6; eTables3,5,6.
- **Printed inputs/specification:** Adverse events/outcomes summarized as percentages; chi-squared or Fisher exact comparisons. Main Table3 has counts without P values; eTables3/5/6 contain the individual tests.
- **Check and reproduction/limits:** Test families are explicitly supplied. Extra shard S121-S222 performs every applicable row check; main Table 3 has no printed inferential tests. Adverse events need not be mutually exclusive.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S063 — Reported multiplicity/design conclusion

- **Exact location and role:** REPORT DOC001 p3,p9; DOC003 pp4-5; PLAN DOC002 p27,p31,p35.
- **Printed inputs/specification:** Primary planned two-sided.05; adjusted pairwise procedure comparisons; unadjusted hypothesis-generating secondary tests; glycemic-control superiority. No NI/equivalence/interim efficacy rule.
- **Check and reproduction/limits:** Primary superiority is consistent with the interval direction and significance. Pairwise procedure adjustment is separate from unadjusted secondary endpoint tests. No noninferiority, equivalence, interim efficacy or alpha-spending rule is stated.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S064 — Primary endpoint scale matching

- **Exact location and role:** PLAN DOC002 pp7-8,16-17,26-29; REPORT DOC001 pp1-3,6; DOC003 pp4-5,15.
- **Printed inputs/specification:** Plan relative-percent change in HbA1c; report net change with year-7 −1.4 and year-12 −1.1 percentage-point group contrasts.
- **Check and reproduction/limits:** The plan defines a relative-percent HbA1c change, while the report footnotes define net change; F-ST1-002 preserves the scale discrepancy.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S065 — Remission endpoint window

- **Exact location and role:** PLAN DOC002 p18,p29; REPORT DOC001 p2,p7.
- **Printed inputs/specification:** Plan HbA1c<6.5% off diabetes medications; report HbA1c<6.5% without medication for at least3months, assessed annually; Figure3 gives abbreviated threshold/medication definition.
- **Check and reproduction/limits:** The plan's threshold/off-medication definition and the report's additional three-month medication-free window are compared without assuming what an unstated plan duration means. F-ST1-005 records the supplied difference.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S066 — Analysis population

- **Exact location and role:** PLAN DOC002 pp17,20,36; REPORT DOC001 pp2-3; DOC003 pp3-4.
- **Printed inputs/specification:** Original randomized/treated and consenting observational cohort; original-assignment ITT. Final N262, M96, B166; earlier planned available302, final available305.
- **Check and reproduction/limits:** Treated, consenting observational participants and original-assignment ITT are explicit. Earlier available-cohort counts do not replace the final analysis denominator or establish a planning-rule conflict.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S067 — Planned baseline comparisons

- **Exact location and role:** PLAN DOC002 p26.
- **Printed inputs/specification:** Planned continuous baseline comparisons: linear regression with site covariate, skewed variable transformation; categorical CMH comparisons.
- **Check and reproduction/limits:** Baseline inferential comparisons are planned, but their absence is not a missing primary/key-secondary result. No preferred baseline test is proposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S068 — Planned A1 model

- **Exact location and role:** PLAN DOC002 pp26-27.
- **Printed inputs/specification:** A1: Y_ijt=alpha_t+beta_t X_ij+gamma^T Z+b_i+c_ij+e_ijt. b_i fixed site; c_ij~N(0,sigma_c²), residual MVN(0,Sigma_e); covariance chosen by AIC; Z four site indicators; coefficient identifiability constraints.
- **Check and reproduction/limits:** Identifiability constraints explicitly permit parameter constraints for the duplicated site terms. The separate fixed-site versus site-variance power specification is recorded in F-ST1-006.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S069 — Planned primary hypothesis

- **Exact location and role:** PLAN DOC002 p27.
- **Printed inputs/specification:** Primary beta_7 surgery−nonsurgical mean relative-percent change; H0 beta_7=0, two-sided P<.05; other annual contrasts secondary through13years.
- **Check and reproduction/limits:** Primary null, year, effect direction and two-sided level are explicit. No margin is stated. The reported net-change scale differs from the planned relative-percent contrast, as in F-ST1-002.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S070 — Planned Aim1 trajectory/power inputs

- **Exact location and role:** PLAN DOC002 p27.
- **Printed inputs/specification:** Observed year-1 change−24/−9.1%, year-3−21.6/−.1%, year-5≈−20/−2%. Assumed surgical−20% at5years to−15% at7; nonsurgical year-7−7..+2% depending crossover; observed crossover0.8%.
- **Check and reproduction/limits:** Observed preliminary data and prospective power assumptions are kept separate. Final outcomes need not equal power inputs. No closed-form sample-size result is stated here.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S071 — Planned cohort/power size

- **Exact location and role:** PLAN DOC002 pp27-29,p55.
- **Printed inputs/specification:** 355 randomized,325 initiated,20 lost,3 died,302 available; ≥80% follow-up, n≈242. Figure Ns302/272/242/211 at missingness0/10/20/30%.
- **Check and reproduction/limits:** 325−20−3=302 and 302×.8=241.6≈242. Figure sample sizes at 0/10/20/30% missing reproduce integer-rounded retention counts. No arithmetic discrepancy is found.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S072 — Planned primary Monte Carlo power

- **Exact location and role:** PLAN DOC002 p28.
- **Printed inputs/specification:** 500 Monte Carlo simulations, two-sided alpha.05; sigma_b=.06, sigma_c=.15, sigma_e=.10, rho=.13, AR(1); >90% power except30% missing.
- **Check and reproduction/limits:** All printed variance/correlation/simulation inputs are retained. Exact simulations cannot be recreated without allocation/site/sample and implementation details. F-ST1-006 concerns the fixed-site versus variance-component specification, rather than an invented simulated power value.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S073 — Planned primary power figure

- **Exact location and role:** PLAN DOC002 p29 FigureA1.
- **Printed inputs/specification:** Four surgical/nonsurgical relative-change series−15/−7,−15/−5,−15/0,−15/+2%; N302/272/242/211; reference90%/95%; worst series≈93% at20% missing, below90% at30%; simulations discard any incomplete participant.
- **Check and reproduction/limits:** Visual ordering of power by effect size and the >90% statement except the 30% missing scenario agree. Exact graph ordinates are unlabeled. Discarding incomplete participants in simulations is explicitly distinguished from the available-data analysis.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S074 — Planned remission power

- **Exact location and role:** PLAN DOC002 p28.
- **Printed inputs/specification:** Preliminary remission year-1 46/1%, year-3 32/0%; assume surgery20% at7 from linear log odds starting46% year-1, nonsurgical5%;500 simulations,20% missing,two-sided.05; power94.6%.
- **Check and reproduction/limits:** Assumed 46% at year 1 and 20% at year 7 define a prospective trend, rather than imposing a trend through every observed preliminary point. Exact logistic random-effect variances and simulation allocation are absent.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S075 — Planned partial-remission power

- **Exact location and role:** PLAN DOC002 p28.
- **Printed inputs/specification:** Assume year-7 partial remission surgery27%, nonsurgical7%; mixed logistic power98.6%; context500 simulations,.05,20% missing.
- **Check and reproduction/limits:** The assumed larger binary separation is consistent with a greater claimed power. Exact mixed-model power cannot be calculated from two endpoint probabilities alone.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S076 — Planned glycemic-control power

- **Exact location and role:** PLAN DOC002 p28.
- **Printed inputs/specification:** Preliminary glycemic control year-1 75/52%, year-3 63/38%, year-5 48/22%; assumed linear log odds yield year-7 39/11%; power>99%, approximately98% even40% missing.
- **Check and reproduction/limits:** Printed 39%/11% are preserved as assumed projections. A diagnostic linear-logit fit to the preliminary rates yields about 34% for surgery, but the source does not specify the fitting rule or make those observations exact constraints; that conditional observation is excluded.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S077 — Planned A2 binary model

- **Exact location and role:** PLAN DOC002 p27.
- **Printed inputs/specification:** A2: logit(P_ijt)=alpha_t+beta_t X_ij+gamma^T Z+b_i+c_ij; same patient/site notation as A1. beta_7 logOR; glycemic control, remission and partial remission; other annual estimates.
- **Check and reproduction/limits:** The conditional mixed-logistic patient random intercept is explicit, and differs from the reported GEE model. F-ST1-003 records that comparison without a crude-OR calculation.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S078 — Planned Aim1 relapse

- **Exact location and role:** PLAN DOC002 p27,p30.
- **Printed inputs/specification:** Aim1 relapse descriptive Kaplan-Meier only, no treatment-group comparison; relapse HbA1c≥6.5% and/or restarting medication; remitters only.
- **Check and reproduction/limits:** Aim-1 descriptive relapse is distinct from Aim-3 predictor analyses. No report result is supplied; the endpoint is not labeled key secondary, so absence alone does not qualify as a primary/key-secondary missing analysis.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S079 — Planned MICE primary sensitivity

- **Exact location and role:** PLAN DOC002 p30.
- **Printed inputs/specification:** MICE sensitivity: rectangular dataset with baseline and chronologically arranged endpoints; fit each mixed model to each imputed dataset; combine by Rubin's rule; 'will also perform'.
- **Check and reproduction/limits:** The plan explicitly promises chained-equation imputation and Rubin combination for primary sensitivity analyses. No such result appears in the supplied report package; F-ST1-004 records the pattern.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S080 — Planned pattern-mixture primary sensitivity

- **Exact location and role:** PLAN DOC002 p30.
- **Printed inputs/specification:** Pattern-mixture sensitivity for informative dropout; death and other dropout mechanisms may have different distributions; 'will also perform'.
- **Check and reproduction/limits:** The plan explicitly promises a pattern-mixture primary sensitivity. No corresponding result appears in supplied report materials; F-ST1-004 records the pattern.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S081 — Planned MSM/censoring sensitivity

- **Exact location and role:** PLAN DOC002 pp30-31; REPORT DOC003 p5.
- **Printed inputs/specification:** MSM sensitivity stabilized IPTW using past treatment/baseline covariates; noncrossovers weight1; final weight IPTW×censoring weight. Report describes treatment IPW under random censoring.
- **Check and reproduction/limits:** The final planned weighting scheme includes treatment and censoring weights. Reported weights are treatment weights under random censoring. This changed/unreported primary sensitivity component is retained in F-ST1-004.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S082 — Planned postcrossover-censor PP

- **Exact location and role:** PLAN DOC002 p31; REPORT DOC003 p5.
- **Printed inputs/specification:** Additional planned PP sensitivity discards all outcomes observed after crossover; report PP reassigns treatment after crossover with IPW.
- **Check and reproduction/limits:** Discarding postcrossover outcomes is an explicit additional sensitivity, distinct from reassigning treatment after crossover with IPW. Its supplied absence is retained in F-ST1-004.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S083 — Planned A3 four treatments/multiplicity

- **Exact location and role:** PLAN DOC002 p31; REPORT DOC003 p4.
- **Printed inputs/specification:** A3: four treatment indicators D, visit indicators T, vectorized D T^T interaction, site/patient/residual terms; annual least-square percent-change estimates; Bonferroni pairwise comparisons.
- **Check and reproduction/limits:** Four-category visit interactions and adjusted procedure comparisons are consistent with the report. The report does not name an exact Bonferroni family or provide a conflicting adjusted numeric result, so none is inferred.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S084 — Planned A4 taxonomy model

- **Exact location and role:** PLAN DOC002 pp33-34.
- **Printed inputs/specification:** A4: alpha_t+beta_t^T W_ijt+gamma^T Z+b_i+c_ij+e_ijt. W includes3procedure dummies, supervised/unsupervised exercise hours, nutrition hours, medication count, adjustment provider and other lifestyle hours. beta_71−100 beta_74 contrasts RYGB with100 supervised hours/year.
- **Check and reproduction/limits:** The source order of taxonomy components supports its RYGB-versus-100-supervised-hours contrast. Expected intervention doses are not actual individual doses. No primary/key-secondary taxonomy result is claimed by the report.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S085 — Planned taxonomy missing-covariate options

- **Exact location and role:** PLAN DOC002 p34.
- **Printed inputs/specification:** Taxonomy covariate MI if more than minimal missingness; simpler alternative fixed yearly averages; A3/A4 extensions to glycemic control, remission and partial remission.
- **Check and reproduction/limits:** These are conditional exploratory alternatives dependent on missing taxonomy covariates. No observed covariate missingness or conflicting numeric result is supplied.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S086 — Planned baseline-covariate sensitivities

- **Exact location and role:** PLAN DOC002 p34,p35; REPORT DOC003 p4.
- **Printed inputs/specification:** Further baseline sensitivities add HbA1c, BMI and every baseline characteristic differing P<.05. Report primary model includes HbA1c but no supplied additional BMI/imbalance-covariate sensitivity result.
- **Check and reproduction/limits:** Reported baseline HbA1c adjustment is a planned sensitivity option. It does not replace the separately promised additional BMI/imbalance-covariate sensitivity, whose missing report result is included in F-ST1-004.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S087 — Planned BMI subgroup

- **Exact location and role:** PLAN DOC002 p34; REPORT DOC001 p3,p7; DOC003 p5,p13.
- **Printed inputs/specification:** Repeat all earlier analyses in baseline BMI<35. Report uses exploratory same-method restriction;96 low-BMI participants.
- **Check and reproduction/limits:** The baseline BMI<35 cutoff and same-method restriction agree. A prospectively described exploratory analysis remains exploratory; the report does not state it was unplanned.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S088 — Planned Aim2 continuous methods

- **Exact location and role:** PLAN DOC002 p34; REPORT DOC003 p4.
- **Printed inputs/specification:** Aim2 continuous weight, BMI, CHD risk, QOL and risk-factor percent changes analyzed as primary relative HbA1c change model.
- **Check and reproduction/limits:** Weight relative-change quantity agrees across sources. Missing non-key ancillary clinical outcomes are not converted into findings solely because the plan lists them; urine microalbumin versus ACR requires endpoint mapping.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S089 — Planned Aim2 binary safety methods

- **Exact location and role:** PLAN DOC002 pp34-35; REPORT DOC003 p6.
- **Printed inputs/specification:** Aim2 micro/macrovascular events:2×2tables with CMH; safety major events/complications same. Report chi-squared/Fisher for adverse events/outcomes.
- **Check and reproduction/limits:** The plan states CMH for these outcomes and the report states chi-squared/Fisher. F-ST1-008 records the changed analysis family; the stratification variable is not inferred from convention.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S090 — Planned Aim2 continuous power

- **Exact location and role:** PLAN DOC002 pp34-35 TableA5.
- **Printed inputs/specification:** Aim2 continuous power80%,two-sided.05,20% missing; standardized delta.47 at rho.1 and.43 at rho.8; residual SD6%,rho≈.7 gives detectable≈2.8%; observed year-3 weight difference≈20%.
- **Check and reproduction/limits:** Multiplying 6% residual SD by the detectable standardized range gives approximately 2.6%-2.8%, consistent with the illustrative 2.8%. Exact simulation assumptions are not fully supplied. Covariance-diagonal versus SD wording alone does not alter a printed result.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S091 — Planned Aim2 binary power

- **Exact location and role:** PLAN DOC002 p35 TableA5.
- **Printed inputs/specification:** Aim2 binary power80%,two-sided.05,20% missing; OR nonsurgical/surgical3.03 at surgical risk10%,2.46 at20%.
- **Check and reproduction/limits:** The explicit nonsurgical-versus-surgical OR reference yields medical event probabilities .2519/.3808 at the stated surgical risks. Full power reproduction lacks allocation and stratified-test inputs; no conflicting report power is stated.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S092 — Planned Aim2 multiplicity

- **Exact location and role:** PLAN DOC002 p35; REPORT DOC003 p5.
- **Printed inputs/specification:** Power for multiple secondary endpoints not multiplicity-adjusted; procedure pairwise Bonferroni separately specified; low-rate safety outcomes may have limited power.
- **Check and reproduction/limits:** Endpoint multiplicity and pairwise intervention multiplicity are distinct families. The report's hypothesis-generating secondary designation agrees with the stated absence of endpoint adjustment.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S093 — Planned Aim3 prediction/selection

- **Exact location and role:** PLAN DOC002 pp35-36.
- **Printed inputs/specification:** Aim3 first-remission predictors: age, sex/gender, race, procedure, T2D severity/duration, hypertension, dyslipidemia, metabolic syndrome, insulin/HbA1c/glucose, early weight loss/BMI change. Each univariate, then full adaptive-lasso multivariable; exploratory.
- **Check and reproduction/limits:** Exploratory predictor models are prospectively listed but no report prediction result is claimed. Variable selection is a stated coherent choice; its merits are outside this review.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S094 — Planned Aim3 Cox

- **Exact location and role:** PLAN DOC002 p36.
- **Printed inputs/specification:** Cox prediction: HR multiplicative scale; Schoenfeld proportional-hazards diagnostic; site strata; randomized-group control.
- **Check and reproduction/limits:** Cox HR scale, site strata and PH diagnostic are coherent with time-to-first-remission. No numerical HR result is supplied for inferential checking.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S095 — Planned Aim3 AFT

- **Exact location and role:** PLAN DOC002 p36.
- **Printed inputs/specification:** AFT sensitivity models log time with additive covariate effects.
- **Check and reproduction/limits:** AFT log-time sensitivity is a stated coherent alternative. No distribution or reported numerical result conflicts with it.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S096 — Planned Aim3 relapse model

- **Exact location and role:** PLAN DOC002 p36.
- **Printed inputs/specification:** Relapse prediction uses the same time-to-event models restricted to remitters; secondary Aim3.
- **Check and reproduction/limits:** The analysis is restricted to remitters and predicts relapse, distinct from the Aim-1 descriptive treatment-group comparison. No contradiction is established by their different purposes.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S097 — Planned multistate model

- **Exact location and role:** PLAN DOC002 p36.
- **Printed inputs/specification:** Three-state initial/remission/death Markov process; Cox transition intensities; exploratory.
- **Check and reproduction/limits:** Three states and Cox transition intensities are specified. No observed transitions or numerical results are supplied; a raw-data/model-preference audit is outside scope.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S098 — Planned Aim3 power TableA6

- **Exact location and role:** PLAN DOC002 p36.
- **Printed inputs/specification:** Aim3 preliminary remission23%; assumption30% yields HR1.36 per1SD at80% power,two-sided.05,R².1. Table HRs at R².1/.2/.5:20% remission1.46/1.50/1.67;30%1.36/1.39/1.52;40%1.31/1.33/1.43. PASS11; R² explained by other covariates.
- **Check and reproduction/limits:** A labeled diagnostic normal/Schoenfeld calculation at N302 reproduces the rounded HR table. The largest last-digit difference is within the 5% display rule. N302 is a diagnostic reproduction, not an inferred exact PASS setting; detailed censoring assumptions are not supplied.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S099 — Stopping and oversight

- **Exact location and role:** PLAN DOC002 p39; REPORT DOC003 p4.
- **Printed inputs/specification:** OSMB twice yearly; observational study has no formal stopping rules; discretionary ethical stop possible.
- **Check and reproduction/limits:** Both plan and report state no formal stopping rule and twice-yearly oversight. Quarterly retention contacts are not statistical interim looks. No margin or alpha-spending rule is invented.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

### S100 — Ancillary cost-utility design

- **Exact location and role:** PLAN DOC002 pp61-63.
- **Printed inputs/specification:** Ancillary cost-utility primary hypothesis ICER<$100000/QALY; BMI30-35, requested data BMI≤35; Markov microsimulation, two strategies, payer perspective, QoL-derived QALYs, mortality/cost/utilization, probabilistic sensitivity; TreeAgePro2018/Excel2017.
- **Check and reproduction/limits:** The ancillary cost-utility hypothesis and Markov design are distinct from the main clinical primary endpoint. No reported ICER is supplied, so there is no matched inferential value or primary clinical analysis conflict.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PENDING

## Coverage closure

S001-S017 cover every mainTable2 outcome with all within-group and group intervals/tests; S018-S034 cover every eTable2 outcome; S035-S041 cover every eTable4 SE/test. S042-S056 preserve every remaining exact narrative contrast and all model-based annual figure panels, with every visit inspected through the complete fresh maps. S057-S063 cover reported models, assumptions, populations, multiplicity and inference rules. S064-S100 cover all protocol endpoint/analysis/power relationships, formulas A1-A4, Figures/TableA1/A5/A6 and ancillary cost utility, including records with no report counterpart. Extra shard S121-S222 covers every remaining report table test; descriptive counts without inference remain in the numeric inventory and full evidence maps. DOC001 pp8-11, DOC002 remaining administrative/instrument/historical pages, DOC003 cover/reference/baseline/count-only tables, and DOC004 p1 introduce no additional inferential relationship beyond the linked maps. No scientific coverage gap. Graphs' unlabeled exact coordinates, absent model df/covariance and unreproducible simulation implementation are named limitations; all printed inputs and applicable checks remain covered.

