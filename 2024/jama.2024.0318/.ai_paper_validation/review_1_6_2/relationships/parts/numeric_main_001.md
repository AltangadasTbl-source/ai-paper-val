# Numeric relationship inventory — main part 1

Scope: MAIN-001..MAIN-067, exactly 67 mapped relationship groups in DOC-001 physical PDF pages 1–4. Stable IDs N001..N067 correspond one-to-one to those groups. Role REPORT throughout. Matching pages 6–8 were read only for corroboration. No old findings, candidate sets, reports, or web sources were used.

Source authority: direct Poppler pdftotext layout extraction from the supplied PDF, plus retained page images 3 and 4 visually checked. Direct derivatives produced with CPU Poppler 26.01.0: checkers/numeric_main_direct_pp1-4.txt (command: pdftotext -layout -f 1 -l 4) and checkers/numeric_main_corrob_pp6-8.txt (-f 6 -l 8), both from jama_courcoulas_2024_oi_240004_1721756962.76052.pdf. Existing locator: extraction/parts/main_001.md, unchanged. Read full QUALITY_CONTROL_SCOPE.md, review contract, source inventory and tooling record.

Source links below resolve relative to this artifact; all evidence is [main REPORT PDF](../../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1). M=medical/lifestyle, B=bariatric, R=Roux-en-Y, S=sleeve, A=banding.

## Complete assigned relationship records

| N ID | Mapper group | Exact source location | Explicit check and result |
|---|---|---|---|
| N001 | MAIN-001 | p1 design; p2 study design | Four trial names counted; three surgery names counted. Date/calendar details are administrative; no applicable result arithmetic. |
| N002 | MAIN-002 | p1 outcome | Baseline→7y primary, up to12y follow-up identified; time scale retained, no applicable count arithmetic. |
| N003 | MAIN-003 | p1 enrolled | 100×262/305=85.9016%; half-unit input interval [85.5974,86.2069], printed86% [85.5,86.5], gap0. |
| N004 | MAIN-004 | p1 cohort characteristics | Age weighted (96×51.4+166×49.0)/262=49.8794; BMI weighted=36.4534. Printed49.9 and36.4 overlap rounding intervals. Women179/262=68.3206%; Black81/262=30.9160%; White177/262=67.5573%, last vs67.2 within threshold. SDs descriptive, no raw data to regenerate individual dispersion. |
| N005 | MAIN-005 | p1 crossover/follow-up; p7 crossover | 24/96=25%; input interval [24.3523,25.6545]% overlaps printed25% [24.5,25.5]. Median11 lies within reported7–15y range. |
| N006 | MAIN-006 | p1 M HbA1c; p3 M narrative; p6 Table2 | Positive decrease magnitude0.2; Table2 signed net change−0.2, CI−0.5..0.2. Narrative explicitly labels difference0.2. Sign-pattern finding F-NUM-002 documents this location with alternatives. |
| N007 | MAIN-007 | p1 B HbA1c; p3 B narrative; p6 Table2 | Positive1.6 with CI−1.8..−1.3 lies outside interval; signed Table2−1.6. F-NUM-002, routeA1, repeated sign pattern. |
| N008 | MAIN-008 | p1 year7 group effect | −1.4 lies within [−1.8,−1.0], excludes0, P<.001 agrees; Table2 exact match. |
| N009 | MAIN-009 | p1 year12 group effect | −1.1 lies within [−1.7,−0.5], excludes0, P=.002 agrees; p3 exact match. |
| N010 | MAIN-010 | p1 year7 remission | M6.2%, B18.2%, P=.02; matches p4. GEE-adjusted effects distinguished from raw ratios; no count denominator printed here to regenerate events. |
| N011 | MAIN-011 | p1 year12 remission | M0.0%, B12.7%, P<.001. Printed group percentages direction agrees; no numerator/denominator printed to infer events. |
| N012 | MAIN-012 | p1 deaths; p7 narrative; p8 Table3 | Count2+2=4 reconciles; pooled4/262=1.5267%, does not reproduce2.2% under half-unit intervals. F-NUM-001. |
| N013 | MAIN-013 | p1 result/conclusion | Qualitative glycemic/medication/remission claims match positive comparative direction; no standalone count arithmetic in this group. |
| N014 | MAIN-014 | p2 Key Points | Magnitudes1.4 and1.1 match signed−1.4 and−1.1 when expressed as superior glycemic control. No reversed direction. |
| N015 | MAIN-015 | p2 primary outcome/statistics | Baseline→7y and12y as applicable; endpoint scale/model labels passed to statistical/cross-source review. No event count printed. |
| N016 | MAIN-016 | p2 secondary outcomes | Thresholds7.0/6.5 and ≥3months medication-free remission retained as definitions, not arithmetic inputs. |
| N017 | MAIN-017 | p2 secondary analyses | Outcome status and randomized/procedure grouping preserved. No applicable numeric total. |
| N018 | MAIN-018 | p2 eligibility/intervention | BMI27..45, age18..65 are ordered ranges; four sites and three procedures match N001. |
| N019 | MAIN-019 | pp2–3 main model | LMM/site/baseline adjustment and participant random intercept recorded; displayed effects cannot be equated with crude mean differences without the fitted model. |
| N020 | MAIN-020 | p3 per-protocol | IPW/current treatment sensitivity distinguished from ITT; no count arithmetic other than crossover checked in N005. |
| N021 | MAIN-021 | p3 missing data | EHR recovery and random-censoring/MAR statements retained for statistical reviewer; no printed missingness tally here. |
| N022 | MAIN-022 | p3 binary models | GEE controlling site/baseline HbA1c; sandwich SEs; no multiplicity adjustment. Adjusted odds ratios identified as odds ratios, not risks. |
| N023 | MAIN-023 | pp2–3 exploratory/safety | BMI<35 subgroup definition and up-to12y safety window preserved; no standalone total. |
| N024 | MAIN-024 | p3 Figure1 initial flow | 155+88+69+43=355;145+78+61+32=316;355−39=316. Trial-specific decreases10+10+8+11=39. All exact, rounding intervals overlap. |
| N025 | MAIN-025 | p3 Figure1 exclusion flow/footnote | 12+2=14;316−14=302; three rerecruited gives302+3=305. Footnote explicitly closes apparent first transition gap. |
| N026 | MAIN-026 | p3 Figure1 branch counts | 106+49+38=193 exact. 193+122=315 vsparent305: half-unit sum[314,316] vs[304.5,305.5], gap8.5/305=.027869≤.05; excluded display precision. |
| N027 | MAIN-027 | p3 Figure1 enrolled; p4 Table1 | 166+96=262;89+41+36=166. Enrolled sizes≤branch sizes; procedure reductions17+8+2=27=193−166. |
| N028 | MAIN-028 | p3 narrative flow | 355−39=316;316−9−2=305;262/305×100=85.9016→86%;96+166=262. Figure footnote explains14 versus net11 as3 rerecruited. |
| N029 | MAIN-029 | p3 pooled characteristics | BMI<35:40+56=96;96/262×100=36.6412, half-unit interval[36.3810,36.9025]% overlaps36.6 [36.55,36.65]. HbA1c weighted (96×8.2+166×8.7)/262=8.5168→8.5; median11 in7–15. Other pooled checks N004. |
| N030 | MAIN-030 | p3 absolute HbA1c statement | Lower postbaseline B HbA1c direction retained; P<.001 is per-time absolute-level comparison, not the year12 change contrast P=.002. |
| N031 | MAIN-031 | p3 year7 HbA1c | Raw M8.0−8.2=−0.2; B7.2−8.7=−1.5 with half-unit range[−1.6,−1.4], overlaps signed Table2−1.6 interval[−1.65,−1.55]. Positive narrative signs handled F-NUM-002. |
| N032 | MAIN-032 | p3 year7/year12 group contrasts | −1.4[−1.8,−1.0],P<.001 and−1.1[−1.7,−0.5],P=.002 match abstract. Ordered limits and estimate containment pass. |
| N033 | MAIN-033 | p3 procedure changes | R−1.7[−2.0,−1.3];S−2.0[−2.6,−1.5];A−0.8[−1.3,−0.2]; all estimates contained, limits ordered, decreases consistent. |
| N034 | MAIN-034 | p3 procedure-comparison tests | R/S nonsignificant; A/S P=.007,A/R P=.03 concern between-procedure differences, not within-procedure zero-change tests; direction agrees −0.8 less negative than−2.0/−1.7. |
| N035 | MAIN-035 | p3 per-protocol estimates | M0.1[−0.5,0.7],B−1.4[−1.7,−1.2],group−1.5[−2.1,−0.9],P<.001. All contained;−1.4−0.1=−1.5; contrast interval excludes0 and P agrees. |
| N036 | MAIN-036 | p3 year1 remission | M0.5%,B50.8%; both within0..100; modeled percentages have no printed event denominators here; no invented event counts. |
| N037 | MAIN-037 | p4 year7 remission | OR crude diagnostic (18.2/81.8)/(6.2/93.8)=3.366, but printed adjusted3.4[1.3,9.2],P=.02 is GEE. OR3.39[1.25,9.17] Table2 rounding overlaps. Not mislabeled RR (crudeRR2.935). |
| N038 | MAIN-038 | p4 year7 procedure remission | R24.5%,S15.2%,A8.9% are bounded proportions; procedures have no printed corresponding year7 event denominators. Do not sum percentages across independent groups. |
| N039 | MAIN-039 | p4 year7 glycemic-control proportions | M26.7%,B54.1%; crude odds diagnostic (54.1/45.9)/(26.7/73.3)=3.236, direction/OR identity matches adjusted3.2[1.8,5.9],P<.001; Table2 OR3.22[1.76,5.88] precision overlaps. ≤6.5 versus <6.5 label context referred to statistical/cross-source reviewers. |
| N040 | MAIN-040 | p4 Table1 Age | Age: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N041 | MAIN-041 | p4 Table1 Women | Women: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N042 | MAIN-042 | p4 Table1 Men | Men: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N043 | MAIN-043 | p4 Table1 Black | Black: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N044 | MAIN-044 | p4 Table1 White | White: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N045 | MAIN-045 | p4 Table1 Other race | Other race: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N046 | MAIN-046 | p4 Table1 Waist | Waist: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked. M95≤96. |
| N047 | MAIN-047 | p4 Table1 Weight | Weight: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N048 | MAIN-048 | p4 Table1 BMI | BMI: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N049 | MAIN-049 | p4 Table1 BMI<35 | BMI<35: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N050 | MAIN-050 | p4 Table1 Systolic BP | Systolic BP: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N051 | MAIN-051 | p4 Table1 Diastolic BP | Diastolic BP: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N052 | MAIN-052 | p4 Table1 Diabetes duration | Diabetes duration: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N053 | MAIN-053 | p4 Table1 HbA1c | HbA1c: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked.  |
| N054 | MAIN-054 | p4 Table1 HbA1c<7.0% | HbA1c<7.0%: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N055 | MAIN-055 | p4 Table1 Fasting glucose | Fasting glucose: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked. M95≤96. |
| N056 | MAIN-056 | p4 Table1 Total cholesterol | Total cholesterol: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked. M95≤96. |
| N057 | MAIN-057 | p4 Table1 HDL | HDL: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked. M95≤96. |
| N058 | MAIN-058 | p4 Table1 LDL | LDL: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked. 88+41+30=159; M94≤96. |
| N059 | MAIN-059 | p4 Table1 Triglycerides | Triglycerides: all five descriptive cells inspected; two-ended parenthetic summary and mean(SD) labeling recorded as excluded terminology observation, no pooling of central values. M95≤96. |
| N060 | MAIN-060 | p4 Table1 Serum creatinine | Serum creatinine: all five descriptive cells inspected; weighted subgroup mean diagnostic below; nonnegative SD and denominators checked. M95≤96. |
| N061 | MAIN-061 | p4 Table1 Urine albumin:creatinine | Urine albumin:creatinine: all five descriptive cells inspected; two-ended parenthetic summary and mean(SD) labeling recorded as excluded terminology observation, no pooling of central values. 62+41+16=119; M74≤96. |
| N062 | MAIN-062 | p4 Table1 Statins | Statins: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N063 | MAIN-063 | p4 Table1 ACEi/ARB | ACEi/ARB: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N064 | MAIN-064 | p4 Table1 ACEi | ACEi: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N065 | MAIN-065 | p4 Table1 Insulin | Insulin: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |
| N066 | MAIN-066 | p4 Table1 β-blockers | β-blockers: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below. A uses explicit9/35; B30/166 versus18.2 is within display precision. |
| N067 | MAIN-067 | p4 Table1 ARB | ARB: all five count/denominator/percentage cells checked explicitly in arithmetic appendix. R+S+A count equals B; sex/race sums checked below.  |

## Table totals and mutual coverage checks

All Table1 columns use denominators M96,B166,R89,S41,A36, except explicit cell denominators. B procedure n89+41+36=166, overall96+166=262. Sex totals: M62+34=96;B117+49=166;R61+28=89;S32+9=41;A24+12=36. Race totals: M35+59+2=96;B46+118+2=166;R23+64+2=89;S13+28+0=41;A10+26+0=36. Surgical subgroup row sums: women61+32+24=117;men28+9+12=49;Black23+13+10=46;White64+28+26=118;other2+0+0=2;BMI<35 26+15+15=56;HbA1c<7 9+0+11=20;statins66+31+24=121;ACEi/ARB63+25+20=108;ACEi47+17+14=78;insulin46+17+19=82;β-blockers15+6+9=30;ARB16+8+6=30. All exact. Other race footnote2 Asian+2 multi-race=4=2M+2B. ACEi/ARB is a union, not an assertion of disjoint drug use; M59+8−65=2 possible overlaps is not a count inconsistency.

LDL subgroup observed counts88+41+30=159; UACR62+41+16=119; β-blocker procedure observed denominators89+41+35=165, consistent with9/35 explicit cell and B30(18.2) possibly using165. Both default166 and165 pass display precision. Enrollment flow: original355→eligible316; after net11 loss available305; enrolled262. Arm branch315 is recorded as screened-out difference, never silently replaced by305.

HbA1c conversion printed consistently in p2/p4:10.93×HbA1c−23.50. Other p4 printed conversions glucose×0.0555, cholesterol×0.0259, triglycerides×0.0113, creatinine×88.4 have no paired converted cells in assigned scope, so no arithmetic comparison is possible.

# Table 1 arithmetic checks

All cells: numerator and denominator receive half-unit input intervals. Percentage intervals use the printed one-decimal precision even where a trailing zero is omitted in this calculation table. Printed zeros without a percentage supply count checks only. All checks use source DOC-001 p4, role REPORT.

| N ID | Row | Column | Count/denominator | Exact recomputation (%) | Input-rounding recomputation interval (%) | Printed (%) | Printed interval (%) | Relative gap | Check |
|---|---|---|---|---:|---|---:|---|---:|---|
| N041 | Women | M | 62/96 | 64.5833 | [63.7306, 65.4450] | 64.6 | [64.55, 64.65] | 0.000000 | reconciles |
| N041 | Women | B | 117/166 | 70.4819 | [69.9700, 70.9970] | 70.5 | [70.45, 70.55] | 0.000000 | reconciles |
| N041 | Women | R | 61/89 | 68.5393 | [67.5978, 69.4915] | 68.5 | [68.45, 68.55] | 0.000000 | reconciles |
| N041 | Women | S | 32/41 | 78.0488 | [75.9036, 80.2469] | 78.0 | [77.95, 78.05] | 0.000000 | reconciles |
| N041 | Women | A | 24/36 | 66.6667 | [64.3836, 69.0141] | 66.7 | [66.65, 66.75] | 0.000000 | reconciles |
| N042 | Men | M | 34/96 | 35.4167 | [34.7150, 36.1257] | 35.4 | [35.35, 35.45] | 0.000000 | reconciles |
| N042 | Men | B | 49/166 | 29.5181 | [29.1291, 29.9094] | 29.5 | [29.45, 29.55] | 0.000000 | reconciles |
| N042 | Men | R | 28/89 | 31.4607 | [30.7263, 32.2034] | 31.5 | [31.45, 31.55] | 0.000000 | reconciles |
| N042 | Men | S | 9/41 | 21.9512 | [20.4819, 23.4568] | 22.0 | [21.95, 22.05] | 0.000000 | reconciles |
| N042 | Men | A | 12/36 | 33.3333 | [31.5068, 35.2113] | 33.3 | [33.25, 33.35] | 0.000000 | reconciles |
| N043 | Black | M | 35/96 | 36.4583 | [35.7513, 37.1728] | 36.5 | [36.45, 36.55] | 0.000000 | reconciles |
| N043 | Black | B | 46/166 | 27.7108 | [27.3273, 28.0967] | 27.7 | [27.65, 27.75] | 0.000000 | reconciles |
| N043 | Black | R | 23/89 | 25.8427 | [25.1397, 26.5537] | 25.8 | [25.75, 25.85] | 0.000000 | reconciles |
| N043 | Black | S | 13/41 | 31.7073 | [30.1205, 33.3333] | 31.7 | [31.65, 31.75] | 0.000000 | reconciles |
| N043 | Black | A | 10/36 | 27.7778 | [26.0274, 29.5775] | 27.8 | [27.75, 27.85] | 0.000000 | reconciles |
| N044 | White | M | 59/96 | 61.4583 | [60.6218, 62.3037] | 61.5 | [61.45, 61.55] | 0.000000 | reconciles |
| N044 | White | B | 118/166 | 71.0843 | [70.5706, 71.6012] | 71.1 | [71.05, 71.15] | 0.000000 | reconciles |
| N044 | White | R | 64/89 | 71.9101 | [70.9497, 72.8814] | 71.9 | [71.85, 71.95] | 0.000000 | reconciles |
| N044 | White | S | 28/41 | 68.2927 | [66.2651, 70.3704] | 68.3 | [68.25, 68.35] | 0.000000 | reconciles |
| N044 | White | A | 26/36 | 72.2222 | [69.8630, 74.6479] | 72.2 | [72.15, 72.25] | 0.000000 | reconciles |
| N045 | Other race | M | 2/96 | 2.0833 | [1.5544, 2.6178] | 2.1 | [2.05, 2.15] | 0.000000 | reconciles |
| N045 | Other race | B | 2/166 | 1.2048 | [0.9009, 1.5106] | 1.2 | [1.15, 1.25] | 0.000000 | reconciles |
| N045 | Other race | R | 2/89 | 2.2472 | [1.6760, 2.8249] | 2.3 | [2.25, 2.35] | 0.000000 | reconciles |
| N045 | Other race | S | 0/41 | 0.0000 | [0.0000, 1.2346] | not printed | not applicable | not applicable | zero count retained |
| N045 | Other race | A | 0/36 | 0.0000 | [0.0000, 1.4085] | not printed | not applicable | not applicable | zero count retained |
| N049 | BMI<35 | M | 40/96 | 41.6667 | [40.9326, 42.4084] | 41.7 | [41.65, 41.75] | 0.000000 | reconciles |
| N049 | BMI<35 | B | 56/166 | 33.7349 | [33.3333, 34.1390] | 33.7 | [33.65, 33.75] | 0.000000 | reconciles |
| N049 | BMI<35 | R | 26/89 | 29.2135 | [28.4916, 29.9435] | 29.2 | [29.15, 29.25] | 0.000000 | reconciles |
| N049 | BMI<35 | S | 15/41 | 36.5854 | [34.9398, 38.2716] | 36.6 | [36.55, 36.65] | 0.000000 | reconciles |
| N049 | BMI<35 | A | 15/36 | 41.6667 | [39.7260, 43.6620] | 41.7 | [41.65, 41.75] | 0.000000 | reconciles |
| N054 | HbA1c<7.0% | M | 11/96 | 11.4583 | [10.8808, 12.0419] | 11.5 | [11.45, 11.55] | 0.000000 | reconciles |
| N054 | HbA1c<7.0% | B | 20/166 | 12.0482 | [11.7117, 12.3867] | 12.0 | [11.95, 12.05] | 0.000000 | reconciles |
| N054 | HbA1c<7.0% | R | 9/89 | 10.1124 | [9.4972, 10.7345] | 10.1 | [10.05, 10.15] | 0.000000 | reconciles |
| N054 | HbA1c<7.0% | S | 0/41 | 0.0000 | [0.0000, 1.2346] | not printed | not applicable | not applicable | zero count retained |
| N054 | HbA1c<7.0% | A | 11/36 | 30.5556 | [28.7671, 32.3944] | 30.6 | [30.55, 30.65] | 0.000000 | reconciles |
| N062 | Statins | M | 71/96 | 73.9583 | [73.0570, 74.8691] | 74.0 | [73.95, 74.05] | 0.000000 | reconciles |
| N062 | Statins | B | 121/166 | 72.8916 | [72.3724, 73.4139] | 72.9 | [72.85, 72.95] | 0.000000 | reconciles |
| N062 | Statins | R | 66/89 | 74.1573 | [73.1844, 75.1412] | 74.2 | [74.15, 74.25] | 0.000000 | reconciles |
| N062 | Statins | S | 31/41 | 75.6098 | [73.4940, 77.7778] | 75.6 | [75.55, 75.65] | 0.000000 | reconciles |
| N062 | Statins | A | 24/36 | 66.6667 | [64.3836, 69.0141] | 66.7 | [66.65, 66.75] | 0.000000 | reconciles |
| N063 | ACEi/ARB | M | 65/96 | 67.7083 | [66.8394, 68.5864] | 67.7 | [67.65, 67.75] | 0.000000 | reconciles |
| N063 | ACEi/ARB | B | 108/166 | 65.0602 | [64.5646, 65.5589] | 65.1 | [65.05, 65.15] | 0.000000 | reconciles |
| N063 | ACEi/ARB | R | 63/89 | 70.7865 | [69.8324, 71.7514] | 70.8 | [70.75, 70.85] | 0.000000 | reconciles |
| N063 | ACEi/ARB | S | 25/41 | 60.9756 | [59.0361, 62.9630] | 61.0 | [60.95, 61.05] | 0.000000 | reconciles |
| N063 | ACEi/ARB | A | 20/36 | 55.5556 | [53.4247, 57.7465] | 55.6 | [55.55, 55.65] | 0.000000 | reconciles |
| N064 | ACEi | M | 59/96 | 61.4583 | [60.6218, 62.3037] | 61.5 | [61.45, 61.55] | 0.000000 | reconciles |
| N064 | ACEi | B | 78/166 | 46.9880 | [46.5465, 47.4320] | 47.0 | [46.95, 47.05] | 0.000000 | reconciles |
| N064 | ACEi | R | 47/89 | 52.8090 | [51.9553, 53.6723] | 52.8 | [52.75, 52.85] | 0.000000 | reconciles |
| N064 | ACEi | S | 17/41 | 41.4634 | [39.7590, 43.2099] | 41.5 | [41.45, 41.55] | 0.000000 | reconciles |
| N064 | ACEi | A | 14/36 | 38.8889 | [36.9863, 40.8451] | 38.9 | [38.85, 38.95] | 0.000000 | reconciles |
| N065 | Insulin | M | 36/96 | 37.5000 | [36.7876, 38.2199] | 37.5 | [37.45, 37.55] | 0.000000 | reconciles |
| N065 | Insulin | B | 82/166 | 49.3976 | [48.9489, 49.8489] | 49.4 | [49.35, 49.45] | 0.000000 | reconciles |
| N065 | Insulin | R | 46/89 | 51.6854 | [50.8380, 52.5424] | 51.7 | [51.65, 51.75] | 0.000000 | reconciles |
| N065 | Insulin | S | 17/41 | 41.4634 | [39.7590, 43.2099] | 41.5 | [41.45, 41.55] | 0.000000 | reconciles |
| N065 | Insulin | A | 19/36 | 52.7778 | [50.6849, 54.9296] | 52.8 | [52.75, 52.85] | 0.000000 | reconciles |
| N066 | β-blockers | M | 16/96 | 16.6667 | [16.0622, 17.2775] | 16.7 | [16.65, 16.75] | 0.000000 | reconciles |
| N066 | β-blockers | B | 30/166 | 18.0723 | [17.7177, 18.4290] | 18.2 | [18.15, 18.25] | 0.000000 | reconciles |
| N066 | β-blockers | R | 15/89 | 16.8539 | [16.2011, 17.5141] | 16.9 | [16.85, 16.95] | 0.000000 | reconciles |
| N066 | β-blockers | S | 6/41 | 14.6341 | [13.2530, 16.0494] | 14.6 | [14.55, 14.65] | 0.000000 | reconciles |
| N066 | β-blockers | A | 9/35 | 25.7143 | [23.9437, 27.5362] | 25.7 | [25.65, 25.75] | 0.000000 | reconciles |
| N067 | ARB | M | 8/96 | 8.3333 | [7.7720, 8.9005] | 8.3 | [8.25, 8.35] | 0.000000 | reconciles |
| N067 | ARB | B | 30/166 | 18.0723 | [17.7177, 18.4290] | 18.1 | [18.05, 18.15] | 0.000000 | reconciles |
| N067 | ARB | R | 16/89 | 17.9775 | [17.3184, 18.6441] | 18.0 | [17.95, 18.05] | 0.000000 | reconciles |
| N067 | ARB | S | 8/41 | 19.5122 | [18.0723, 20.9877] | 19.5 | [19.45, 19.55] | 0.000000 | reconciles |
| N067 | ARB | A | 6/36 | 16.6667 | [15.0685, 18.3099] | 16.7 | [16.65, 16.75] | 0.000000 | reconciles |

## Continuous descriptive rows

All five printed means and SDs are retained in MAIN040..067 of the current map and checked for nonnegative dispersion, applicable denominator ≤ column enrollment, and unit identity. The following direct weighted-mean diagnostic uses the three disjoint surgical subgroups. Each mean can vary ±0.05. With displayed counts held fixed, the recomputation interval below is a subset of the full permitted half-unit interval; permitting count rounding can only widen it. No row exceeds the relative-gap threshold even under these narrower bounds. SDs are descriptive, not confidence intervals. Triglyceride and urine albumin:creatinine two-ended summaries do not support additive pooling of their central values.

| N ID | Row | Surgical subgroup-weighted mean | Subset recomputation interval | Printed B interval | Relative gap under narrower bounds | Check |
|---|---|---:|---|---|---:|---|
| N040 | Age | 49.01084 | [48.96084, 49.06084] | [48.95, 49.05] | 0.000000 | threshold not exceeded |
| N046 | Waist | 115.06145 | [115.01145, 115.11145] | [114.95, 115.05] | 0.000000 | threshold not exceeded |
| N047 | Weight | 103.50964 | [103.45964, 103.55964] | [103.45, 103.55] | 0.000000 | threshold not exceeded |
| N048 | BMI | 36.58855 | [36.53855, 36.63855] | [36.55, 36.65] | 0.000000 | threshold not exceeded |
| N050 | Systolic BP | 134.46024 | [134.41024, 134.51024] | [134.35, 134.45] | 0.000000 | threshold not exceeded |
| N051 | Diastolic BP | 80.45422 | [80.40422, 80.50422] | [80.35, 80.45] | 0.000000 | threshold not exceeded |
| N052 | Diabetes duration | 8.27108 | [8.22108, 8.32108] | [8.25, 8.35] | 0.000000 | threshold not exceeded |
| N053 | HbA1c | 8.76446 | [8.71446, 8.81446] | [8.65, 8.75] | 0.000000 | threshold not exceeded |
| N055 | Fasting glucose | 172.05241 | [172.00241, 172.10241] | [171.95, 172.05] | 0.000000 | threshold not exceeded |
| N056 | Total cholesterol | 179.56928 | [179.51928, 179.61928] | [179.55, 179.65] | 0.000000 | threshold not exceeded |
| N057 | HDL | 42.87651 | [42.82651, 42.92651] | [42.85, 42.95] | 0.000000 | threshold not exceeded |
| N058 | LDL | 100.32201 | [100.27201, 100.37201] | [100.25, 100.35] | 0.000000 | threshold not exceeded |
| N060 | Creatinine | 0.72169 | [0.67169, 0.77169] | [0.65, 0.75] | 0.000000 | threshold not exceeded |

## Completion

67/67 assigned groups checked. There is no uninspected assigned group. Two findings, five excluded apparent observations. Limitations: raw participant-level data and fitted model objects are not supplied, so individual SDs, modeled percentages, and adjusted estimates cannot be regenerated from event counts that are not printed. This does not prevent printed count and percentage checks.

