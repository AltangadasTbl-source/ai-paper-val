# Statistical relationship inventory — second pass primary shard

Runtime agent: `/root/statistical_pass2`; run model `gpt-6.1-sol`; reasoning effort `high`; FRESH_SPAWN. Exact owned scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050.

Every original assigned record and its PASS_1_COMPLETE facts are preserved below; PASS_2_COMPLETE and individually authored second-pass facts are appended. Original shared provenance describes the original larger pass-1 scope only; this updated shard owns exactly the 50 IDs stated above. Current complete ledger, screening log, mechanical recheck and all 53 original exclusions were read. New findings: 0; new excluded observations: 0. Complete exclusion reread and limits are in ../../checkers/statistical_pass_2.md. The coordinator merges this artifact with the disjoint other pass-2 parts.

## Preserved original shared methods and provenance

# Statistical relationship inventory — PASS 1 primary shard

Runtime agent: `/root/statistical_pass1`; run model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. Scope: every main-paper inferential relationship, every protocol inferential/design/power relationship, report eTables2/4 and all report eFigures/models. Independent extra shard owns only eTables3/5/6: S121-S222. Numeric namespace 101 through 120 remains unassigned and contains no omitted evidence. This artifact owns S001-S100; the coordinator performs the canonical merge. All source roles below are assigned by content: DOC001 main REPORT, DOC002 protocol PLAN, DOC003 results/methods supplement REPORT; DOC004 data-sharing page REPORT contains no inferential relationship.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Inputs are exact supplied PDFs, new evidence maps and source-linked usable locators, with no earlier findings or conclusions. Direct Poppler26.01.0 CPU extraction produced `statistics/protocol_statistical_direct.txt` (DOC002 pp26-36) and `statistics/supplement_outcomes_direct.txt` (DOC003 pp15-18). Commands: `pdftotext -layout -f 26 -l 36 joi240004supp1_prod_1721756962.80052.pdf .../statistics/protocol_statistical_direct.txt` and `pdftotext -layout -f 15 -l 18 joi240004supp2_prod_1721756962.82552.pdf .../statistics/supplement_outcomes_direct.txt`. No OCR/fallback environment/new rendering. Visually inspected source-linked images DOC001 p6 and fresh mapper images DOC002 pp26/28; protocol formulas/power illustrations additionally have complete visual confirmation in the new support map. Exact direct native pages supplied the other stated text.

Table row records contain every group estimate and interval, together with the between-group test: they do not collapse independently tested outcomes. Genuine repeated occurrences are cross-referenced. Every record checks all estimates in that row for ordered endpoints and containment, and checks its corresponding group CI/test. Limits on exact test reconstruction are named, rather than silently filling in degrees of freedom, sidedness, covariance or estimator. All CIs below are printed95% unless specified; parentheses for raw values are SD and square brackets for raw medians are IQR. Medical M; surgery B. No candidate IDs or adjudications are assigned.

## Shared row check specification

MainTable2 headers M baseline96/year7 82 and B baseline166/year7 136 are displayed headers, not outcome-specific observed denominators. eTable2 has no outcome-specific denominators; eTable1 separately describes130 participants reaching12years. Raw summaries and model estimates differ by design. Continuous group contrasts are surgery change minus medical change (null0); within-group fold changes and all odds ratios have null1. Every point is within its ordered interval. Every numerical group CI excludes/includes its null consistently with its own printed P at.05, including nonsignificant rows; year12 remission has no group CI to test. No inferential conclusion is generated from raw IQR/SD ranges. All significance conclusions and effect directions reconcile within each displayed row. Exact P reconstruction is limited by absent reported test distribution/degrees of freedom; normal z values from interval width are diagnostic only. MainTable2 binary log-interval symmetry has one reproduced exception S013/F-ST1-007; every other binary cell permits its log-symmetric center within half-unit rounding bounds.



## Updated assigned original records

### S001 — Year-7 HbA1c net change, percentage points

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 1; MAIN-076. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 8.2(1.2)→8.0(1.8); −0.2[−0.5,0.2]; B: 8.7(1.7)→7.2(1.4); −1.6[−1.8,−1.3]; group estimate/95%CI: −1.4[−1.8,−1.0]; group P <.001.
- **Checks:** Shared row specification applied to all three tabulated intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Matched abstract/p3 between-group −1.4[−1.8,−1.0],P<.001 agrees. The positive abstract/narrative surgery point1.6 lies outside its signed negative interval: F-ST1-009 under routeA1. A deliberate reduction-magnitude reading is preserved as an alternative. Planned scale comparison S064/F-ST1-002.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Table 2 signed changes −0.2 and −1.6 and group −1.4 [−1.8,−1.0], P<.001 reconcile for containment, direction, group subtraction and significance. Positive prose surgery 1.6 outside its negative interval remains C001; primary scale and covariate/sensitivity mapping remain C004/C007/C008. No new issue; covariance/df and exact fitted output remain absent.


### S002 — Year-7 Fasting glucose relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 2; MAIN-077. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 156.5(50.0)→144.6(57.3); −3.8[−14.8,7.2]; B: 172.0(69.7)→125.1(47.0); −14.1[−22.0,−6.3]; group estimate/95%CI: −10.3[−23.6,2.9]; group P .13.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** All three intervals contain their estimates; group −10.3 [−23.6,2.9], P=.13 both include/support the null. Surgery-minus-medical modeled changes reproduce within half-unit bounds. Missing MED percent glyph is resolved by relative-change footnote and does not alter a number; raw glucose ratios are not substituted.


### S003 — Year-7 Weight relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 3; MAIN-078. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 105.6(15.5)→96.2(16.6); −8.3[−10.5,−6.1]; B: 103.5(15.3)→83.6(15.8); −19.9[−21.6,−18.1]; group estimate/95%CI: −11.6[−14.3,−8.9]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** All intervals are ordered and containing; modeled losses −8.3/−19.9 give contrast −11.6 [−14.3,−8.9], P<.001. Narrative positive loss magnitudes pair with positive loss intervals consistently. Raw-to-adjusted and ITT-to-PP quantities remain distinct.


### S004 — Year-7 SBP relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 4; MAIN-079. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 129.7(15.8)→128.7(15.7); −1.1[−3.9,1.7]; B: 134.4(17.7)→128.6(15.3); −3.4[−5.6,−1.2]; group estimate/95%CI: −2.3[−5.8,1.1]; group P .19.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Modeled changes −1.1/−3.4 and group −2.3 [−5.8,1.1], P=.19 reconcile; both group CI and P support nonsignificance. Overall supplementary SBP P=.16 is a different trajectory test, not this year-7 contrast.


### S005 — Year-7 DBP relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 5; MAIN-080. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 79.5(9.6)→74.6(9.7); −4.3[−7.0,−1.6]; B: 80.4(10)→74.3(10.4); −6.0[−8.1,−3.8]; group estimate/95%CI: −1.7[−5.0,1.7]; group P .32.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Modeled changes −4.3/−6.0 give group −1.7; its CI [−5.0,1.7] contains zero and P=.32 is nonsignificant. All three estimates are contained with ordered endpoints; df/covariance absent, so no exact alternative P is imposed.


### S006 — Year-7 LDL relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 6; MAIN-081. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 96.3(33.2)→97.6(36.6); 5.5[−3.3,14.3]; B: 100.3(34.2)→103.1(36.4); 10.8[3.8,17.9]; group estimate/95%CI: 5.4[−5.6,16.3]; group P .34.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Modeled changes 5.5/10.8 and printed difference 5.4 reconcile with half-unit subtraction intervals despite central difference 5.3. Group [−5.6,16.3], P=.34 both support null inclusion; overall LDL P=.83 is a different trajectory contrast.


### S007 — Year-7 HDL relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 7; MAIN-082. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 44.3(13.2)→52.0(17.0); 20.5[14.5,26.6]; B: 42.9(11.6)→56.5(16.5); 37.4[32.6,42.3]; group estimate/95%CI: 16.9[9.4,24.4]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Modeled HDL changes 20.5/37.4 give 16.9 [9.4,24.4], P<.001; endpoints, containment, direction and narrative agree. All within-group and group intervals are checked separately; no crude mean ratio replaces a fitted change.


### S008 — Year-7 Total cholesterol relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 8; MAIN-083. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 172.6(38.5)→171.7(41.6); −0.7[−5.6,4.1]; B: 179.6(44.8)→181.4(40.6); 4.9[1.0,8.7]; group estimate/95%CI: 5.6[−0.4,11.6]; group P .07.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Changes −0.7/4.9 give group 5.6 [−0.4,11.6], P=.07. Group null inclusion and nonsignificance reconcile, while surgery's own interval excludes zero; these are different contrasts and do not conflict.


### S009 — Year-7 Triglyceride relative change, %; raw median[IQR]

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 9; MAIN-084. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 140[92.5,221.5]→125[88,178.3]; 2.3[−8.6,13.2]; B: 144[103,231]→107[82,142]; −19.0[−27.8,−10.2]; group estimate/95%CI: −21.3[−34.9,−7.8]; group P .002.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Changes 2.3/−19.0 give group −21.3 [−34.9,−7.8], P=.002, with ordered containing intervals and consistent reductions. Raw median/IQR values are distinct from modeled relative changes and their CIs.


### S010 — Year-7 Serum creatinine relative change, %

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 10; MAIN-085. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 0.7(0.2)→0.8(0.4); 9.5[1.8,17.1]; B: 0.7(0.2)→0.8(0.2); 10.5[4.4,16.7]; group estimate/95%CI: 1.1[−8.4,10.5]; group P .83.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Creatinine changes 9.5/10.5 and difference 1.1 reconcile within half-unit subtraction bounds. Group [−8.4,10.5], P=.83 support null inclusion; individually positive changes are not the between-group test.


### S011 — Year-7 Urine albumin:creatinine fold change; raw median[IQR]

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 11; MAIN-086. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 6[4,12]→8[4,13.5]; 1.3[0.9,1.9]; B: 9[4.5,23]→6[4,10]; 0.9[0.7,1.2]; group estimate/95%CI: −0.4[−1.0,0.1]; group P .10.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Fold changes 1.3 [0.9,1.9]/0.9 [0.7,1.2] have null 1; between-group additive difference −0.4 [−1.0,0.1], P=.10 has null 0. Quantities, direction, containment and subtraction agree; no ratio-of-folds is substituted for the stated difference.


### S012 — Year-7 Remission %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 12; MAIN-087. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 0.6→6.2; 10.4[0.4,279.4]; B: 0.6→18.2; 36.2[1.9,699.0]; group estimate/95%CI: 3.39[1.25,9.17]; group P .02.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p4 OR3.4[1.3,9.2],P=.02 agrees after rounding; p1 rates6.2/18.2 agree.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Within-group and group ORs all contain their points; group 3.39 [1.25,9.17], P=.02 excludes null 1 and is significant. Narrative 3.4 [1.3,9.2] matches rounding. Modeled remission rates, observed contributors and baseline-to-visit ORs are distinct; endpoint/model mapping remains C005/C009.


### S013 — Year-7 Diabetes medication %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 13; MAIN-088. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 99.0→96.0; 0.10[0.01,3.27]; B: 97.6→60.5; 0.03[0.01,0.11]; group estimate/95%CI: 0.09[0.03,0.24]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. The medical within-group OR interval does not reproduce the log-symmetric center pattern of the same display: F-ST1-007. Medical baseline-change P=.19 (p4) and surgical P<.001 (pp4/6) agree with their intervals' null inclusion/exclusion.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Medication group OR .09 [.03,.24], P<.001 and surgery within-group .03 [.01,.11] agree in direction/significance; medical .10 [.01,3.27] contains null with prose P=.19. Medical log-center discrepancy remains precisely C010 with half-unit relative gap .227693234; it is not a crude-ratio or significant/nonsignificant issue and is not re-emitted.


### S014 — Year-7 Oral/GLP1 only %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 14; MAIN-089. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 57.3→40.0; 0.53[0.29,0.97]; B: 47.0→44.5; 0.74[0.46,1.20]; group estimate/95%CI: 0.98[0.53,1.82]; group P .95.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. 
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Group oral/GLP1 OR .98 [.53,1.82], P=.95 includes null 1; MED .53 [.29,.97] and SURG .74 [.46,1.20] are distinct within-group contrasts. All points are contained; model-based ORs need not equal crude odds from displayed percentages.


### S015 — Year-7 Insulin and/or oral/GLP1 %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 15; MAIN-090. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 41.7→56.0; 1.93[1.07,3.46]; B: 50.6→16.0; 0.18[0.11,0.31]; group estimate/95%CI: 0.13[0.06,0.29]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p6 insulin16% surgery vs56% medical,P<.001 agrees.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Insulin group OR .13 [.06,.29], P<.001 excludes null in the lower-surgery direction; MED 1.93 [1.07,3.46] and SURG .18 [.11,.31] are consistent within-group changes. Narrative 16%/56% agrees with displayed year-7 percentages.


### S016 — Year-7 HbA1c<7.0 %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 16; MAIN-091. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 11.7→26.7; 2.77[1.38,5.54]; B: 15.5→54.1; 6.42[3.63,11.4]; group estimate/95%CI: 3.22[1.76,5.88]; group P <.001.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p4 OR3.2[1.8,5.9],P<.001 agrees after rounding.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** HbA1c<7 group OR 3.22 [1.76,5.88], P<.001 and narrative 3.2 [1.8,5.9] reconcile. Both within-group ORs and all intervals are containing and ordered. Surgical upper bound 11.4 retains one-decimal precision; planned binary model replacement remains C009.


### S017 — Year-7 HbA1c<6.5 %, within OR; group OR

- **Source/role:** REPORT [DOC1 p6](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6), Table2 row 17; MAIN-092. Governing methods REPORT [DOC1 p3](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3) and [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4).
- **Printed inputs:** M baseline→year7 and within-group estimate: 8.3→17.3; 2.30[1.19,4.47]; B: 12.0→37.7; 4.44[2.46,8.01]; group estimate/95%CI: 2.89[1.48,5.64]; group P .002.
- **Checks:** Shared row specification applied to all three intervals. Continuous group difference arithmetic reconciles with half-unit input/contrast intervals; binary group and within-year ORs use distinct contrasts, so an OR ratio is not substituted for the year-7 group OR. Narrative p4 glycemic-threshold P=.002 agrees; < versus ≤ symbol alone does not establish different extracted results.
- **Named limits:** Covariance, numerical SE, exact df/test distribution and outcome-specific observed n are not printed. They are not inferred. Raw-to-adjusted differences are not findings.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** HbA1c<6.5 group OR 2.89 [1.48,5.64], P=.002 excludes null 1 and matches narrative test; all within-group estimates contain. Adjacent ≤ versus < wording identifies the same reported row and supplies no changed boundary result; no new endpoint-status issue follows from the glyph.


### S018 — Year-12 HbA1c net change, percentage points

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 1, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 7.9(1.4); −0.3[−0.8,0.1]; B: 7.3(1.5); −1.4[−1.7,−1.1]; group estimate/95%CI: −1.1[−1.7,−0.5]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Matched main abstract/p3 same−1.1[−1.7,−.5] butP=.002 does not reconcile with supplementaryP<.001: F-ST1-001. Each significance conclusion is internally compatible with its CI. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 net HbA1c −0.3/−1.4 give −1.1 [−1.7,−0.5]; containing intervals and significance agree. Main P=.002 versus supplement P<.001 remains C002 with relative displayed gap at least .25; the correction notice concerns the registry link. Copied year-7 footnotes do not obscure the year-12 columns.


### S019 — Year-12 Fasting glucose relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 2, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 137.6(45.4); −6[−19.6,7.6]; B: 130.3(47.2); −11.1[−20,−2.2]; group estimate/95%CI: −5.1[−21,10.9]; group P .53. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 changes −6/−11.1 give −5.1 [−21,10.9], P=.53; all estimates are inside ordered intervals and group null inclusion agrees. Preserve integer precision of −6 and endpoints; no exact fitted P or outcome n is inferred.


### S020 — Year-12 Weight relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 3, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 92.8(13.5); −10.8[−13.5,−8.2]; B: 83.7(17.8); −19.3[−21.3,−17.3]; group estimate/95%CI: −8.4[−11.7,−5.2]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Model difference−8.4 vsrounded within-group difference−8.5 reconciles: inputs yield[−8.6,−8.4],printed contrast[−8.45,−8.35],overlap. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 losses −10.8/−19.3 and difference −8.4 reconcile because subtraction [−8.6,−8.4] overlaps printed [−8.45,−8.35]. Group [−11.7,−5.2], P<.001 and positive loss-magnitude narrative agree after scale matching.


### S021 — Year-12 SBP relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 4, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 125.6(15.9); −4.7[−8.5,−1]; B: 128.4(15.8); −4.5[−7.1,−1.9]; group estimate/95%CI: 0.3[−4.2,4.7]; group P .91. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Difference.3 vsrounded component difference.2 reconciles: inputs yield[.1,.3],printed[.25,.35],overlap. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 −4.7/−4.5 produce subtraction [.1,.3], overlapping difference .3 band [.25,.35]. Group [−4.2,4.7], P=.91 includes null; both individually negative changes test different quantities.


### S022 — Year-12 DBP relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 5, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 71.8(10.2); −7.7[−11.4,−4]; B: 74.7(10); −6.6[−9.1,−4.1]; group estimate/95%CI: 1.1[−3.2,5.5]; group P .61. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 −7.7/−6.6 give 1.1 [−3.2,5.5], P=.61; estimates, intervals, direction and additive contrast reconcile. Group nonsignificance is compatible with both within-group reductions.


### S023 — Year-12 LDL relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 6, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 90.9(39.4); −7.9[−19.9,4]; B: 87.6(31.2); −11.9[−20.2,−3.7]; group estimate/95%CI: −4[−18.2,10.2]; group P .58. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 LDL −7.9/−11.9 give −4 [−18.2,10.2], P=.58 with null included. Ordered containing intervals and their actual printed integer/decimal precision are retained; no crude-to-adjusted comparison becomes a finding.


### S024 — Year-12 HDL relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 7, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 50.5(13.2); 16.6[8.4,24.7]; B: 57.7(17.9); 38.1[32.5,43.7]; group estimate/95%CI: 21.5[11.9,31.2]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 HDL 16.6/38.1 give 21.5 [11.9,31.2], P<.001, with positive direction and contained points. Both within-group intervals are positive; no incompatible significance conclusion appears.


### S025 — Year-12 Total cholesterol relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 8, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 170.8(48.1); −4.2[−11.1,2.6]; B: 168.9(38.9); −5.5[−10,−0.9]; group estimate/95%CI: −1.2[−9.3,6.9]; group P .77. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Difference−1.2 vsrounded component difference−1.3 reconciles within input/contrast rounding bounds. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 cholesterol −4.2/−5.5 yields central −1.3 but rounded subtraction [−1.4,−1.2] overlaps printed −1.2 band [−1.25,−1.15]. Group [−9.3,6.9], P=.77 supports null inclusion; zero display gap.


### S026 — Year-12 Triglyceride relative change, %; raw median[IQR]

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 9, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 119[89,164]; 9.8[−4.9,24.5]; B: 104[75,126.8]; −23.3[−33.3,−13.2]; group estimate/95%CI: −33.1[−50.5,−15.7]; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 triglyceride modeled changes 9.8/−23.3 give −33.1 [−50.5,−15.7], P<.001. All intervals are containing and ordered; median/IQR summaries do not constrain a crude fitted-change calculation.


### S027 — Year-12 Serum creatinine relative change, %

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 10, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 0.9(0.7); 29.5[19.3,39.7]; B: 0.9(0.3); 20.3[13.3,27.3]; group estimate/95%CI: −9.2[−21.2,2.9]; group P .14. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 creatinine 29.5/20.3 gives −9.2 [−21.2,2.9], P=.14; between-group CI includes null while each within-group change is positive. Different contrasts explain those conclusions without additional findings.


### S028 — Year-12 Urine albumin:creatinine fold change; raw median[IQR]

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 11, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 12.1[6.4,30.8]; 2.2[1.4,3.6]; B: 8.1[5.2,20.1]; 1.5[1.1,2.1]; group estimate/95%CI: −0.7[−1.9,0.4]; group P .20. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 fold changes 2.2 [1.4,3.6]/1.5 [1.1,2.1] exclude their null 1; additive group −.7 [−1.9,.4], P=.20 includes its null 0. Scale, containment and arithmetic agree; group test is not either within-group fold test.


### S029 — Year-12 Remission %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 12, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 0%; OR NA; footnote modeled probability2e−16; B: 12.7%; 23.6[1.2,465.3]; group estimate/95%CI: NA; footnote almost infinite; group P <.001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Medical probability2e−16 is described as yielding near-zero within-group and almost-infinite group OR; NA entries are not zero numerical ORs. The reported groupP<.001 has no groupCI, so exact Wald/test compatibility cannot be assessed. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 medical 0% and footnote probability 2e−16 accompany NA within/group OR cells, not finite zero/infinite estimates with CIs. Surgery OR 23.6 [1.2,465.3] is contained and ordered. Group P<.001 has no printed group CI/test statistic, so no interval-P conflict is established; C005/C009 remain relevant.


### S030 — Year-12 Diabetes medication %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 13, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 93.8; 0.06[0.002,2.16]; B: 82.6; 0.10[0.02,0.39]; group estimate/95%CI: 0.45[0.15,1.36]; group P .16. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 medication group OR .45 [.15,1.36], P=.16 includes null 1; MED .06 [.002,2.16] also includes it and SURG .10 [.02,.39] excludes it. All points are contained; interval-center half-unit bands permit the printed centers, unlike the already registered year-7 medical cell.


### S031 — Year-12 Oral/GLP1 only %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 14, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 34.4; 0.45[0.23,0.85]; B: 53.5; 1.14[0.70,1.85]; group estimate/95%CI: 1.80[0.85,3.82]; group P .12. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 oral/GLP1 group OR 1.80 [.85,3.82], P=.12 includes null; MED .45 [.23,.85] and SURG 1.14 [.70,1.85] are different within-group contrasts. Ordered intervals, containment and direction reconcile.


### S032 — Year-12 Insulin and/or oral/GLP1 %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 15, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 59.4; 2.31[1.23,4.32]; B: 29.1; 0.40[0.25,0.64]; group estimate/95%CI: 0.25[0.10,0.58]; group P .001. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 insulin group OR .25 [.10,.58], P=.001 excludes null in the lower-surgery direction; MED 2.31 [1.23,4.32] and SURG .40 [.25,.64] have coherent opposite within-group trends. Distinct OR contrasts are retained, with no ratio-of-OR substitution.


### S033 — Year-12 HbA1c<7.0 %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 16, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 29.4; 3.15[1.20,8.30]; B: 54.6; 6.57[3.56,12.1]; group estimate/95%CI: 2.90[1.15,7.29]; group P .02. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 HbA1c<7 group OR 2.90 [1.15,7.29], P=.02 excludes null; both within-group ORs are contained and ordered. Decimal precision, modeled probabilities and key binary-plan mapping remain explicit.


### S034 — Year-12 HbA1c<6.5 %, within OR; group OR

- **Source/role:** REPORT [DOC3 p15](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=15), eTable2 row 17, footnotes [DOC3 p16](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=16); SUPPORT-B-031–034. Governing methods REPORT [DOC3 p4](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=4)–p6.
- **Printed inputs:** M raw year12 and within-group estimate: 19.6; 2.68[0.92,7.81]; B: 40.0; 4.90[2.54,9.48]; group estimate/95%CI: 2.75[1.09,6.90]; group P .03. Baseline comparator is stated in the table footnote; raw baseline values are not reprinted.
- **Checks:** Shared row checks applied. Continuous difference arithmetic or binary model quantity checks reconcile within the appropriate half-unit bounds; ORs are not treated as crude count ratios. The source footnotes retain year-7 wording while the heading is year12; immediate context establishes year12 and this wording alone is excluded.
- **Named limits:** Exact test distribution/df, covariance, outcome-specific observed n and (for binary models) numerical sandwich SE are absent; no exact alternative P is imposed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-12 HbA1c<6.5 group OR 2.75 [1.09,6.90], P=.03 excludes null; MED 2.68 [.92,7.81] includes null while SURG 4.90 [2.54,9.48] excludes it. Those separate contrasts create no interval-test conflict.


### S035 — Nutritional least-square Hemoglobin g/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row1; SUPPORT-B-036.
- **Printed inputs:** M13.7 SE0.2; B13 SE0.1; difference−0.8 SE0.2; P<.001.
- **Check:** All rounding intervals for means permit−0.8. Diagnostic z=−4; significant direction coheres. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 hemoglobin 13.7/13 and contrast −.8, SE .2, P<.001 reconcile under actual mean precision; coarse surgery 13 permits −.8. Diagnostic normal z≈−4 agrees with significant direction; no df/CI supplied, so no exact t test is imposed.


### S036 — Nutritional least-square Iron μg/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row2; SUPPORT-B-036.
- **Printed inputs:** M83.9 SE3.2; B85.3 SE2.5; difference1.4 SE4.1; P=.74.
- **Check:** 85.3−83.9=1.4; diagnostic z=.341, normal P≈.733; rounded inputs permit .74. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 iron 83.9/85.3 gives 1.4 with SE4.1 and P=.74; printed contrast and mean rounding intervals overlap. Normal z≈.341/P≈.733 are diagnostic and rounded inputs permit .74. Model covariance and df remain absent.


### S037 — Nutritional least-square Vitamin B12 pg/mL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row3; SUPPORT-B-036.
- **Printed inputs:** M760.8 SE105.1; B1173.2 SE80.6; difference412.4 SE132.4; P=.002.
- **Check:** 1173.2−760.8=412.4; diagnostic z=3.115, normal P≈.00184; .002 compatible. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 B12 760.8/1173.2 gives 412.4 with SE132.4 and P=.002. Diagnostic normal z≈3.115/P≈.00184 agrees with displayed significance and precision. No CI or exact distribution is printed.


### S038 — Nutritional least-square Vitamin D ng/mL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row4; SUPPORT-B-036.
- **Printed inputs:** M35.2 SE1.8; B40.5 SE1.4; difference5.3 SE2.3; P=.02.
- **Check:** 40.5−35.2=5.3; diagnostic z=2.304, normal P≈.0212; .02 compatible. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 vitamin D 35.2/40.5 gives 5.3, SE2.3 and P=.02; diagnostic normal z≈2.304/P≈.0212 is compatible. Direction matches main narrative and no interval-test contradiction is supplied.


### S039 — Nutritional least-square Calcium mg/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row5; SUPPORT-B-036.
- **Printed inputs:** M9.6 SE0.04; B9.5 SE0.03; difference−0.1 SE0.0; P=.03.
- **Check:** SE0.0 is printed one-decimal precision, interval[0,.05), not established zero variance. Unrounded contrast/SE can yield .03. No division by printed0.0. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 calcium 9.6/9.5 gives contrast −.1, SE0.0 and P=.03. One-decimal SE band [0,.05] permits a positive SE; mean/contrast bands permit a .03 test. No division by an assumed exact zero or forced independent variance is used.


### S040 — Nutritional least-square PTH pg/mL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row6; SUPPORT-B-036.
- **Printed inputs:** M51.1 SE3.3; B60.3 SE2.5; difference9.2 SE4.2; P=.03.
- **Check:** 60.3−51.1=9.2; diagnostic z=2.190, normal P≈.0285; .03 compatible. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 PTH 51.1/60.3 gives 9.2, SE4.2 and P=.03; diagnostic normal z≈2.190/P≈.0285 agrees. Mean subtraction, direction and displayed precision reconcile; df/covariance not supplied.


### S041 — Nutritional least-square Albumin g/dL

- **Source/role:** REPORT [DOC3 p18](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=18), eTable4 row7; SUPPORT-B-036.
- **Printed inputs:** M4.1 SE0.03; B4.1 SE0.02; difference−0.01 SE0.04; P=.72.
- **Check:** Mean intervals both[4.05,4.15) allow−.01. Contrast[−.015,−.005),SE[.035,.045) permit normal P from≈.668 to.912, including .72. Null difference0; footnote defines surgery minus medical. Model SEs are not inferred from independent raw-group variance. Normal approximations are diagnostics, as the report does not state df or exact test distribution here.
- **Named limits:** Exact df/covariance absent; no CI printed. Display half-unit intervals distinguish a rounded SE0.0 from exact zero.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** eTable 4 albumin means 4.1/4.1 allow contrast −.01. Contrast [−.015,−.005] and SE [.035,.045] permit diagnostic normal P≈.668–.912, including .72; printed means do not imply exact equality. No CI is supplied.


### S042 — Procedure HbA1c contrasts

- **Exact location and role:** REPORT DOC001 p3 Figure2B narrative.
- **Printed inputs/specification:** RYGB change −1.7 (−2.0,−1.3)%; SG −2.0 (−2.6,−1.5)%; AGB −0.8 (−1.3,−0.2)%. AGB vs SG P=.007; vs RYGB P=.03; RYGB vs SG nonsignificant.
- **Check and reproduction/limits:** All three estimates are contained in ordered 95% CIs, with reductions in the stated direction. Pairwise P values test different contrasts from each procedure's individual change. Exact pairwise reproduction needs the covariance, degrees of freedom and adjustment family, which are not supplied.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Procedure HbA1c changes RYGB−1.7 [−2.0,−1.3], SG−2.0 [−2.6,−1.5], AGB−.8 [−1.3,−.2] are containing and ordered. AGB-vs-SG P=.007 and AGB-vs-RYGB P=.03 concern pairwise contrasts, with source-stated multiplicity adjustment distinct from individual change intervals; covariance/df/adjustment name absent.


### S043 — Procedure weight contrasts

- **Exact location and role:** REPORT DOC001 p6 Figure2D narrative.
- **Printed inputs/specification:** Year-7 loss RYGB22.7%, AGB14.0%, RYGB vs AGB P<.001; SG19.7%, differences vs other procedures nonsignificant.
- **Check and reproduction/limits:** Greater loss for R than A agrees with the printed direction and P<.001. S comparisons are separately described as nonsignificant. No interval or standard error is printed for these pairwise tests.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Year-7 procedure losses RYGB22.7/AGB14.0/SG19.7 agree with narrative and plotted direction. RYGB-vs-AGB P<.001 and nonsignificant SG comparisons have no printed contrast interval/SE; their distinct tests cannot be reconstructed by comparing individual plotted distributions.


### S044 — PP HbA1c sensitivity

- **Exact location and role:** REPORT DOC001 p3; DOC003 p9 eFigure2A, p5 methods.
- **Printed inputs/specification:** Year-7 medical0.1 (−0.5,0.7)%, surgery−1.4 (−1.7,−1.2)%; difference−1.5 (−2.1,−0.9)%, P<.001.
- **Check and reproduction/limits:** Estimate containment, endpoint order, surgery-minus-medical arithmetic and CI/P significance agree. Robust IPW inference is explicitly stated. The planned additional postcrossover-censor sensitivity is tracked in F-ST1-004.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** PP HbA1c .1 [−.5,.7]/−1.4 [−1.7,−1.2] gives −1.5 [−2.1,−.9], P<.001 with ordered containing intervals. Reported IPW reassigns postcrossover treatment and uses sandwich inference; the separately promised outcome-discard/censoring sensitivity package remains C008 rather than a duplicate finding.


### S045 — PP weight sensitivity

- **Exact location and role:** REPORT DOC001 pp6-7; DOC003 p9 eFigure2B.
- **Printed inputs/specification:** Year-7 medical/surgery loss5.6%/20.4%; year-12 7.7%/19.4%. eFigure2 caption gives the same year-7 values; no PP interval or P printed.
- **Check and reproduction/limits:** ITT and PP losses are explicitly distinct and match the supplementary figure caption at year 7. No PP confidence interval or P value is printed for the weight contrast; exact annual coordinates are unlabeled.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** PP weight losses year7 5.6/20.4 and year12 7.7/19.4 remain distinct from ITT 8.3/19.9 and 10.8/19.3. Main narrative/eFigure 2 caption agree at year7; no PP confidence limits/P are printed. No unlabeled graph coordinates or missing sensitivity estimates are inferred.


### S046 — BMI subgroup HbA1c contrasts

- **Exact location and role:** REPORT DOC001 p7; DOC003 p13 eFigure6A.
- **Printed inputs/specification:** BMI<35: M−.4%, B−1.5%, difference−1.2 (−1.8,−.5)%; BMI≥35: M−.1%, B−1.6%, difference−1.5 (−2.1,−1.0)%; interaction P=.40. Year-7 absolute LS M/B8.3/7.4 low and8.1/7.0 high.
- **Check and reproduction/limits:** Both subgroup estimates are contained in ordered CIs excluding zero. The low-BMI change difference −1.1 vs printed −1.2 reconciles within half-unit intervals. P=.40 is an interaction, not either subgroup's individual effect test. Absolute LS means require their baseline-adjustment mapping before comparison with changes.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** BMI subgroup HbA1c differences −1.2 [−1.8,−.5] and −1.5 [−2.1,−1.0] are contained and exclude zero. Low-BMI component subtraction −1.1 permits −1.2 under half-unit bounds. Interaction P=.40 tests effect difference, not either subgroup effect. Absolute LS means versus changes need baseline mapping; > versus ≥ glyph alone supplies no changed participant/result.


### S047 — BMI subgroup weight contrasts

- **Exact location and role:** REPORT DOC001 p7; DOC003 p13 eFigure6B.
- **Printed inputs/specification:** BMI<35: losses M5.6%, B20.4%, difference14.8 (10.8,18.8)%, P<.001; BMI≥35: M10.1%, B19.3%, difference9.2 (5.6,12.9)%; interaction P=.03.
- **Check and reproduction/limits:** Within each BMI subgroup the surgery-minus-medical loss differences reproduce exactly, and the CIs exclude zero in the stated direction. P=.03 refers to the difference between subgroup effects; its covariance and standard error are absent.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** BMI subgroup weight losses 5.6/20.4 give 14.8 [10.8,18.8], P<.001; 10.1/19.3 give 9.2 [5.6,12.9]. Both positive-loss contrasts are contained and ordered; interaction P=.03 concerns the between-subgroup effect difference with unprinted covariance/SE.


### S048 — Annual HbA1c LS trajectories

- **Exact location and role:** REPORT DOC001 p5 Figure2A/B; p3 allpostbaseline P<.001.
- **Printed inputs/specification:** Visits0-12, M/B and AGB/RYGB/SG least-square means plus raw boxplots; all contributor Ns in MAIN-068/069. Surgery higher baseline but lower at all postbaseline visits, narrative P<.001; no numerical point CI/SE.
- **Check and reproduction/limits:** All visits and procedures are mapped, including contributor counts. The boxes and whiskers show raw distributions, not confidence intervals. The stated postbaseline direction agrees with the plotted trajectories; exact point coordinates and per-visit test statistics are not printed.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** All visits0–12 and three procedures were revisited on exact Figure 2: postbaseline lower surgical HbA1c direction agrees with prose. Caption identifies raw boxplots/IQR whiskers separately from model LS means; those are not inferential CIs. Outcome-specific contributor rows do not imply a changed randomized analysis set; no numerical point CI/test output is printed.


### S049 — Annual weight LS trajectories

- **Exact location and role:** REPORT DOC001 p5 Figure2C/D; DOC003 p9 eFigure2B.
- **Printed inputs/specification:** Visits0-12, M/B and AGB/RYGB/SG least-square means plus raw boxplots; all contributor Ns in MAIN-070/071. Surgery/RYGB/SG show larger loss. Numeric confidence limits and point-specific tests not printed.
- **Check and reproduction/limits:** All annual group/procedure trajectories and contributor counts are mapped. Loss direction agrees with the narrative. Modeled baseline values cannot be treated as raw zero-change observations; unprinted numeric coordinates and confidence limits are not invented.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** All visits0–12 modeled group/procedure weight trajectories show greater surgical loss as described; raw boxplots are distinct. Figure 2 baseline LS loss is not forced to raw zero, and contributor counts may differ by measured outcome. Caption/eFigure 2 distinguish ITT from PP; no unlabeled numeric confidence limit is invented.


### S050 — Annual remission inference

- **Exact location and role:** REPORT DOC001 p7 Figure3,p1,p4; DOC003 p15 remissionrow.
- **Printed inputs/specification:** Year-1 M0.5%, B50.8%; year-7 M6.2%, B18.2%, OR3.4 (1.3,9.2), P=.02; year-12 M0%, B12.7%, P<.001. Annual contributor Ns in MAIN-111/112.
- **Check and reproduction/limits:** Year-7 OR/CI rounding agrees between narrative and Table 2. Model-derived percentages are distinct from raw contributor-count ratios. Year-12 group OR/CI are NA with the near-zero medical probability explained; no finite OR or CI is inferred.
- **Pass1:** PASS_1_COMPLETE
- **Pass2:** PASS_2_COMPLETE
- **Second-pass facts:** Annual remission year1 .5/50.8, year7 6.2/18.2 with OR3.4 [1.3,9.2], P=.02, and year12 0/12.7, P<.001 match table/narrative after model/time/precision matching. Year12 NA OR/CI and near-zero probability do not provide a finite interval-test comparison. C005/C009 retain window/model questions; no crude ratio from contributor n replaces the modeled OR.


