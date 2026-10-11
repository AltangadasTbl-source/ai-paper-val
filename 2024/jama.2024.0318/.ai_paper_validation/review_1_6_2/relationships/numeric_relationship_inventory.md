# Numeric relationship inventory — main part 1

Scope: MAIN-001..MAIN-067, exactly 67 mapped relationship groups in DOC-001 physical PDF pages 1–4. Stable IDs N001..N067 correspond one-to-one to those groups. Role REPORT throughout. Matching pages 6–8 were read only for corroboration. No old findings, candidate sets, reports, or web sources were used.

Source authority: direct Poppler pdftotext layout extraction from the supplied PDF, plus retained page images 3 and 4 visually checked. Direct derivatives produced with CPU Poppler 26.01.0: checkers/numeric_main_direct_pp1-4.txt (command: pdftotext -layout -f 1 -l 4) and checkers/numeric_main_corrob_pp6-8.txt (-f 6 -l 8), both from jama_courcoulas_2024_oi_240004_1721756962.76052.pdf. Existing locator: extraction/parts/main_001.md, unchanged. Read full QUALITY_CONTROL_SCOPE.md, review contract, source inventory and tooling record.

Source links below resolve relative to this artifact; all evidence is [main REPORT PDF](../../../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1). M=medical/lifestyle, B=bariatric, R=Roux-en-Y, S=sleeve, A=banding.

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

# Numeric relationship inventory: results and support shard

All116 assigned grouped numeric relationships are complete. N068–N144 map one-to-one to MAIN-068–MAIN-144; N145–N183 map in order to SUPPORT-B-001–SUPPORT-B-039. Each grouped relationship includes every underlying printed row/cell, definition, contributor sequence and footnote in its exact evidence-map key. Counts are grouped tracking records, not a limitation on the number of checked cells. No records were skipped. Source paths and physical page locators are inherited from the explicitly keyed source maps, not from older scientific findings.

Evidence-map locations relative to this inventory: [main part2](../extraction/main_quantitative_evidence_part_02.md) and [support shard2](../extraction/parts/support_002.md). Exact source-page links appear in those complete source maps and candidate cards. Main DOC-001 is REPORT; support DOC-002 is PLAN, DOC-003 and DOC-004 are REPORT. All main keys here are REPORT. The support source-role field below is the source content role.

Check outcome text uses COMPLETE to mean every applicable count/denominator/percentage, subgroup total, quantitative label, definition and displayed-precision arithmetic in that group was reviewed. Statistical intervals/P are also read for containment and null membership, while inferential reconstruction is independently assigned to statistical specialists. Detailed rules, coherent computations, four exclusions and F-NUM-101/F-NUM-102 are in [numeric checker](../checkers/parts/numeric_results_extra.md). Full numeric inputs are retained below as the mapper table-row content; all complete underlying transcriptions remain in the source maps.

## Main relationship records

| Relationship ID | Mapper key | All printed inputs and context | Numeric check outcome |
|---|---|---|---|
| N068 | MAIN-068 | 2A absolute HbA1c%,M/B ; B:[166,164,160,157,147,152,118,136,119,126,119,100,83];M:[96,92,88,86,80,86,78,82,72,71,68,55,31] ; y-axis4,6,8,10,12,14%; B blue-gray,M orange; B higher baseline then lower at every visit1–12 | COMPLETE; every annual contributor N and surgical subgroup sum checked at all13 visits; sums reconcile |
| N069 | MAIN-069 | 2B HbA1c%,A/R/S ; A:[36,35,33,34,34,30,29,33,22,24,23,10,16];R:[89,88,86,84,75,82,60,70,65,68,63,58,40];S:[41,41,41,39,38,40,29,33,32,34,33,32,27] ; Same HbA1c axis;A tan,R coral,S blue. Baseline S highest;A generally highest later,R/S similar after first year | COMPLETE; every annual contributor N and surgical subgroup sum checked at all13 visits; sums reconcile |
| N070 | MAIN-070 | 2C weight loss%,M/B ; B:[166,164,161,158,144,149,122,139,121,126,121,106,85];M:[96,91,84,86,79,78,77,75,73,73,70,60,34] ; y-axis20,10,0,−10,−20,−30,−40,−50%; B consistently more negative; source calls plotted quantity weight loss | COMPLETE; every annual contributor N and surgical subgroup sum checked at all13 visits; sums reconcile |
| N071 | MAIN-071 | 2D weight loss%,A/R/S ; A:[36,34,33,32,31,29,32,31,22,24,25,12,18];R:[89,89,87,86,75,81,60,74,64,68,62,61,41];S:[41,41,41,40,38,39,30,34,35,34,34,33,26] ; Same weight axis;R and S more negative than A; labels same colors as2B | COMPLETE; every annual contributor N and surgical subgroup sum checked at all13 visits; sums reconcile |
| N072 | MAIN-072 | 2A all-visit model trajectory, unlabelled coordinates ; M approximately8.2 baseline,7.5 year1,then around8.0–8.5; B about8.7 baseline,6.5 year1,then6.5–7.5 ; These are coarse visual locators only, not exact extracted numbers. Exact primary7y/12y contrasts MAIN-008/009 and MAIN-076 | COMPLETE; unlabelled curve/boxplot coordinates inspected as locators; exact values not inferred from pixels |
| N073 | MAIN-073 | 2B all-visit model trajectory, unlabelled coordinates ; A baselineabout8.2,year1about6.8,thenaround7–8;R baselineabout8.7,year1about6.5,thenaround6.5–7.5;S baselineabout9.4,year1about6.4,thenaround6.5–7.5 ; Exact procedure7y change/CI/P records MAIN-033/034. No CI or P printed on panel | COMPLETE; unlabelled curve/boxplot coordinates inspected as locators; exact values not inferred from pixels |
| N074 | MAIN-074 | 2C all-visit model trajectory, unlabelled coordinates ; Baseline model dot B visually below0 (about−5),M near0;B around−25 at1y,then−20 to−25;M around−5 to−10 after1y ; Preserve displayed baseline model dot without assuming it is observed zero-change raw data. Exact7y/12y magnitudes MAIN-095/096 | COMPLETE; unlabelled curve/boxplot coordinates inspected as locators; exact values not inferred from pixels |
| N075 | MAIN-075 | 2D all-visit model trajectory, unlabelled coordinates ; Baseline R near0,A near−5,S around+5;after1y R/S roughly−20 to−30,A roughly−10 to−15 ; Coarse visual locators. Entire13-visit raw box/IQR/whisker displays retained in page image; no printed numeric limits. Exact7y procedure means MAIN-097 | COMPLETE; unlabelled curve/boxplot coordinates inspected as locators; exact values not inferred from pixels |
| N076 | MAIN-076 | Primary HbA1c%,mean(SD) ; 8.2(1.2) ; 8.0(1.8) ; −0.2(−0.5 to0.2) ; 8.7(1.7) ; 7.2(1.4) ; −1.6(−1.8 to−1.3) ; −1.4(−1.8 to−1.0) ; <.001 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N077 | MAIN-077 | Fasting glucose,mg/dL,mean(SD) ; 156.5(50.0) ; 144.6(57.3) ; −3.8(−14.8% to7.2%) ; 172.0(69.7) ; 125.1(47.0) ; −14.1%(−22.0% to−6.3%) ; −10.3%(−23.6% to2.9%) ; .13 | COMPLETE; percent-change unit follows footnoteb; missing sign unit excluded as notation |
| N078 | MAIN-078 | Weight,kg,mean(SD) ; 105.6(15.5) ; 96.2(16.6) ; −8.3%(−10.5% to−6.1%) ; 103.5(15.3) ; 83.6(15.8) ; −19.9%(−21.6% to−18.1%) ; −11.6%(−14.3% to−8.9%) ; <.001 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N079 | MAIN-079 | SBP,mmHg,mean(SD) ; 129.7(15.8) ; 128.7(15.7) ; −1.1%(−3.9% to1.7%) ; 134.4(17.7) ; 128.6(15.3) ; −3.4%(−5.6% to−1.2%) ; −2.3%(−5.8% to1.1%) ; .19 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N080 | MAIN-080 | DBP,mmHg,mean(SD) ; 79.5(9.6) ; 74.6(9.7) ; −4.3%(−7% to−1.6%) ; 80.4(10) ; 74.3(10.4) ; −6.0%(−8.1% to−3.8%) ; −1.7%(−5.0% to1.7%) ; .32 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N081 | MAIN-081 | LDL,mg/dL,mean(SD) ; 96.3(33.2) ; 97.6(36.6) ; 5.5%(−3.3% to14.3%) ; 100.3(34.2) ; 103.1(36.4) ; 10.8%(3.8% to17.9%) ; 5.4%(−5.6% to16.3%) ; .34 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N082 | MAIN-082 | HDL,mg/dL,mean(SD) ; 44.3(13.2) ; 52.0(17.0) ; 20.5%(14.5% to26.6%) ; 42.9(11.6) ; 56.5(16.5) ; 37.4%(32.6% to42.3%) ; 16.9%(9.4% to24.4%) ; <.001 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N083 | MAIN-083 | Total cholesterol,mg/dL,mean(SD) ; 172.6(38.5) ; 171.7(41.6) ; −0.7%(−5.6% to4.1%) ; 179.6(44.8) ; 181.4(40.6) ; 4.9%(1.0% to8.7%) ; 5.6%(−0.4% to11.6%) ; .07 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N084 | MAIN-084 | Triglycerides,mg/dL,median(IQR) ; 140(92.5–221.5) ; 125(88–178.3) ; 2.3%(−8.6% to13.2%) ; 144(103 to231) ; 107(82 to142) ; −19.0%(−27.8% to−10.2%) ; −21.3%(−34.9% to−7.8%) ; .002 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N085 | MAIN-085 | Serum creatinine,mg/dL,mean(SD) ; 0.7(0.2) ; 0.8(0.4) ; 9.5%(1.8% to17.1%) ; 0.7(0.2) ; 0.8(0.2) ; 10.5%(4.4% to16.7%) ; 1.1%(−8.4% to10.5%) ; .83 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N086 | MAIN-086 | Urine albumin:creatinine ratio,median(IQR) ; 6(4–12) ; 8(4–13.5) ; 1.3(0.9 to1.9) ; 9(4.5 to23) ; 6(4 to10) ; 0.9(0.7 to1.2) ; −0.4(−1.0 to0.1) ; .10 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N087 | MAIN-087 | Remission diabetes,% ; 0.6 ; 6.2 ; 10.4(0.4 to279.4) ; 0.6 ; 18.2 ; 36.2(1.9 to699.0) ; 3.39(1.25 to9.17) ; .02 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N088 | MAIN-088 | Diabetes medication use,% ; 99.0 ; 96.0 ; 0.10(0.01 to3.27) ; 97.6 ; 60.5 ; 0.03(0.01 to0.11) ; 0.09(0.03 to0.24) ; <.001 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N089 | MAIN-089 | Oral/GLP1 only,% ; 57.3 ; 40.0 ; 0.53(0.29 to0.97) ; 47.0 ; 44.5 ; 0.74(0.46 to1.20) ; 0.98(0.53 to1.82) ; .95 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N090 | MAIN-090 | Insulin and/or oral/GLP1,% ; 41.7 ; 56.0 ; 1.93(1.07 to3.46) ; 50.6 ; 16.0 ; 0.18(0.11 to0.31) ; 0.13(0.06 to0.29) ; <.001 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N091 | MAIN-091 | HbA1c<7.0%,% ; 11.7 ; 26.7 ; 2.77(1.38 to5.54) ; 15.5 ; 54.1 ; 6.42(3.63 to11.4) ; 3.22(1.76 to5.88) ; <.001 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N092 | MAIN-092 | HbA1c<6.5%,% ; 8.3 ; 17.3 ; 2.30(1.19 to4.47) ; 12.0 ; 37.7 ; 4.44(2.46 to8.01) ; 2.89(1.48 to5.64) ; .002 | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N093 | MAIN-093 | p6 below Table2,medication paragraph; starts p4 ; B diabetes medication use baseline97.6%(162/166),year1 38.0%(62/163),year7 60.5%(72/119),P<.001 vs baseline. M use no significant change:P=.19 year7,.12 year12. These explicit fractions are narrative observed counts; table headers remain separate. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N094 | MAIN-094 | p6 below Table2 ; Insulin use B16% vs M56% at7y,P<.001. Incretin/GLP1 use higher M across all annual visits,P<.001;pointer eFigure4. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N095 | MAIN-095 | p6 weight paragraph ; Year7 weight loss M8.3%(6.1–10.5),B19.9%(18.1–21.6),P<.001;positive loss magnitudes matching negative-change Table2 row. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N096 | MAIN-096 | p6 right lower paragraph ; Year12 M loss10.8%(8.2–13.5),B19.3%(17.3–21.3),P<.001;Figure2C pointer. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N097 | MAIN-097 | p6 procedure weight paragraph ; Year7 R22.7% vs A14.0% loss,P<.001;S19.7%,no significant difference vs other procedures. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N098 | MAIN-098 | p6 right lower paragraph ; BMI≤25,described nonobesity:year7 M2.7%,B14.4%;year12 M0%,B15.3%. No numerators or P printed. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N099 | MAIN-099 | p6 last sentence continuing p7 first column ; PP crossover-accounted weight loss:year7 M5.6%,B20.4%;year12 M7.7%,B19.4%. Pointer eFigure2B;no interval/P printed here. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N100 | MAIN-100 | p7 first column lipid/BP paragraph ; No significant between-group SBP or LDL differences7y;HDL higher B over time,P<.001;triglycerides lower B over time,P<.001. The over-time tests are distinguishable from Table2 single7y comparison. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N101 | MAIN-101 | p7 first column ; Year7 HDL change M20.5%,B37.4%,difference16.9%(9.4–24.4),P<.001;TG change M2.3%,B−19.0%,P=.002. No significant between-group serum creatinine or UACR changes. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N102 | MAIN-102 | p7 exploratory BMI paragraph ; Analysis of96 BMI27–<35 participants vs BMI≥35 at randomization;B lower HbA1c at all points,P<.001. No statement that subgroup analysis was prespecified;called exploratory. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N103 | MAIN-103 | p7 lowerBMI HbA1c ; Year7 M−0.4%,B−1.5%;difference−1.2%(−1.8 to−0.5). Text says significantly greater B reduction;no numerical P for this contrast. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N104 | MAIN-104 | p7 higherBMI HbA1c ; Year7 M−0.1%,B−1.6%;difference−1.5%(−2.1 to−1.0). Difference from lowerBMI effect nonsignificant,P=.40. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N105 | MAIN-105 | p7 lowerBMI weight ; Year7 M5.6%,B20.4%;difference14.8%(10.8–18.8),P<.001. Positive weight-loss quantities. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N106 | MAIN-106 | p7 higherBMI weight,continuation right top ; Year7 M10.1%,B19.3%;difference9.2%(5.6–12.9);different from lowerBMI effect,P=.03. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N107 | MAIN-107 | p7 right safety paragraph ; Four deaths over12y:two M(gunshot,disability following strokes),two B(cardiac,COVID19). Cardiovascular/other adverse events similar except fractures,anemia Hb<11.5g/dL,low iron<59μg/dL more B. B hemoglobin lower,B12/D higher. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N108 | MAIN-108 | p7 right safety paragraph ; Dialysis2/96(2.1%) M vs none B;retinopathy5/96(5.2%) M vs2/166(1.2%) B. Table3 matching rows. More GI abdominal pain,dumping,nausea/vomiting B;no P here. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N109 | MAIN-109 | p7 crossover paragraph ; M24/96(25%) crossed to surgery:R8,S15,A1;median crossover4.5(range0.4–9.8)y. Procedures no significant differences except pooled crossovers/conversions/revisions more M. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N110 | MAIN-110 | p7 revision paragraph ; B15participants(9%) conversion/revision:A removal7,A→R4,A→S1,S→R3(two reflux,one chronic fistula). Components and reasons retained;denominatorB166 from adjacent context. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N111 | MAIN-111 | M contributors and remission plotted points ; Counts0–12:[96,92,87,82,78,84,76,79,72,70,67,55,31]. Remission exact matching narrative0.5% at1y,6.2% at7y,0.0% at12y;unlabelled other points are visually about0.6,1.5,2,3.5,6.5,5.5,6,5.5,4.5,2.5,3.5% at visits0,2,3,4,5,6,8,9,10,11 respectively. These approximations are locators only. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N112 | MAIN-112 | B contributors and remission plotted points ; Counts0–12:[166,164,151,149,140,146,108,131,116,125,117,99,82]. Exact matching narrative50.8% at1y,18.2% at7y,12.7% at12y;other points visually about0.6,41,32,25.5,23.5,19,18,14.5,12.5,18% at visits0,2,3,4,5,6,8,9,10,11. No unlabeled pixel approximation substitutes for an exact tabular value. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N113 | MAIN-113 | Cross-location remission definition and inference ; Caption threshold/remission medication definition preserved;7y OR3.39(1.25–9.17),P=.02 belongs Table2 not Figure3;12y P<.001 belongs abstract/p4. Contributor counts are outcome-specific and differ from HbA1c Figure2A counts. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N114 | MAIN-114 | Death ; 2(2.1) ; 2(1.2) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N115 | MAIN-115 | Coronary revascularization ; 7(7.3) ; 15(9) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N116 | MAIN-116 | Myocardial infarction ; 4(4.2) ; 10(6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N117 | MAIN-117 | Unstable angina ; 2(2.1) ; 4(2.4) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N118 | MAIN-118 | Significant arrhythmia ; 4(4.2) ; 7(4.2) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N119 | MAIN-119 | Heart failure ; 1(1) ; 5(3) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N120 | MAIN-120 | Stroke/transient ischemic attack ; 3(3.1) ; 5(3) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N121 | MAIN-121 | Peripheral arterial disease ; 0 ; 2(1.2) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N122 | MAIN-122 | Venous thromboembolism ; 2(2.1) ; 1(0.6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N123 | MAIN-123 | Severe hypoglycemia ; 7(7.3) ; 11(6.6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N124 | MAIN-124 | Diabetic ketoacidosis ; 1(1) ; 0 | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N125 | MAIN-125 | Gastric/anastomotic ulcer ; 2(2.1) ; 10(6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N126 | MAIN-126 | Bowel obstruction ; 1(1) ; 3(1.8) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N127 | MAIN-127 | Gastrointestinal leaks ; 0 ; 1(0.6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N128 | MAIN-128 | Gallstones/cholecystitis ; 3(3.1) ; 9(5.4) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N129 | MAIN-129 | Pancreatitis ; 1(1) ; 3(1.8) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N130 | MAIN-130 | Alcohol-associated cirrhosis ; 0 ; 2(1.2) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N131 | MAIN-131 | Kidney stones ; 2(2.1) ; 11(6.6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N132 | MAIN-132 | Initiation dialysis ; 2(2.1) ; 0 | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N133 | MAIN-133 | Retinopathy ; 5(5.2) ; 2(1.2) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N134 | MAIN-134 | Blindness ; 1(1) ; 0 | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N135 | MAIN-135 | Blood transfusion for anemia ; 3(3.1) ; 20(12) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N136 | MAIN-136 | Blood transfusion for GI bleeding ; 2(2.1) ; 5(3) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N137 | MAIN-137 | Fracture ; 5(5.2) ; 22(13.3) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N138 | MAIN-138 | Cancer ; 4(4.2) ; 9(5.4) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N139 | MAIN-139 | Suicide attempt ; 0 ; 1(0.6) | COMPLETE; both n/96 and n/166 percentages reconcile with display intervals; no disjoint-event assumption |
| N140 | MAIN-140 | p8 first discussion column ; Rounded remission B51% at1y,18% at7y versus M0.5%,6%;mean diabetes duration8y;baseline HbA1c8.5%. Matches MAIN-036/037/052/029;clinical explanation does not change printed figures. | COMPLETE; printed quantities/roles/denominators and source-supported arithmetic reconcile; model/raw and time-point context retained |
| N141 | MAIN-141 | p8 cited historical comparisons ; Supplied discussion only:DiRECT duration3.1y,2y follow-up;19% less microvascular disease per remission-year from cited work;Ikramuddin5y120participants and composite HbA1c<7%,LDL<100mg/dL,SBP<130mmHg in23% of57R vs4% of56M;Mingrone10y60participants,remission37.5% of40surgical vs5.5% of18M. These are external-study background within supplied text,not ARMMS results;no external source sought. | COMPLETE; historical/interpretive/administrative context reviewed; no new applicable ARMMS count inconsistency |
| N142 | MAIN-142 | p9 left discussion column ; BMI≥35/<35 surgical HbA1c reductions similar;weight difference greater BMI<35. More than one-third baselineBMI<35;three procedures;more than one-fourth racial/ethnic minorities. Anemia/fractures/GI higher B. These interpretation claims match prior numerical rows. | COMPLETE; historical/interpretive/administrative context reviewed; no new applicable ARMMS count inconsistency |
| N143 | MAIN-143 | p9 limitations ; Open-label trials;different protocols/treatments and nonuniform complication assessment;ratios not all1:1 because some had two surgical groups;different enrollment timelines and follow-up lengths;MAR untestable;PP strong assumptions regarding time-varying exposure/outcome,absence uncontrolled time-varying confounding and weight-model specification. Analysis not powered for differences among three procedures,major cardiovascular events,microvascular events,cancer or mortality. No numerical sample-size/power calculation printed. | COMPLETE; historical/interpretive/administrative context reviewed; no new applicable ARMMS count inconsistency |
| N144 | MAIN-144 | p7–9 conclusions;pp10–11 no-applicable ; Superior glycemic control,less medication,higher remission after7–12y;HDL/TG advantages and nutritional/GI/fracture tradeoffs. P10 article disclosures/funding/reference numbers andp11 references carry no new quantitative ARMMS relation. Both pages fully read and explicitly recorded no-applicable. | COMPLETE; historical/interpretive/administrative context reviewed; no new applicable ARMMS count inconsistency |

## Support relationship records

| Relationship ID | Mapper key | Source location/role | All printed inputs and context | Numeric check outcome |
|---|---|---|---|---|
| N145 | SUPPORT-B-001 | DOC-002 p55 PLAN | All five cohort flow and baseline rows. Fixed order CCF/UPMC/Joslin RYGB/Joslin LAGB/UW: randomized 155,69,43,45,43; intervention 154,61,38,40,32; died 2,0,0,1,0; lost 12,5,3,0,0; eligible 140,56,35,39,32. All dates and baseline cells below.; matches Original-trial flow and population selection | COMPLETE; all5 column flow identities reconcile, but randomized-minus-treated total30 versus dropout38 is F-NUM-102 |
| N146 | SUPPORT-B-002 | DOC-002 p56 PLAN | Every one-year weight and HbA1c <6.0/<6.5 without medication cell. Footnotes: 38 dropped at randomization, 20 lost across 4 sites, 3 of 5 UPMC verbal re-engagement commitments.; matches Population and remission definitions | COMPLETE; all5 column flow identities reconcile, but randomized-minus-treated total30 versus dropout38 is F-NUM-102 |
| N147 | SUPPORT-B-003 | DOC-002 pp57-59 PLAN | SF-36 all 36 items, response categories, four-week and prior-year recall. No patient results or scoring formula.; matches Quality-of-life endpoint | COMPLETE; questionnaire items/categories/recall periods; no observed patient-result counts |
| N148 | SUPPORT-B-004 | DOC-002 p60 PLAN | AUDIT-C 3 items, original AUDIT 10 items; a-e score 0,1,2,3,4; total 0-12; male positive >=4, female >=3; score 0 means no alcohol; skip items 2-3 if never. All drink/frequency categories below.; matches Alcohol and safety definition | COMPLETE; 3 items with0-4 scores sum0-12; male>=4/female>=3 thresholds preserved |
| N149 | SUPPORT-B-005 | DOC-002 pp61-63 PLAN | Inferential ancillary cost utility: primary ICER <$100000/QALY; aim BMI 30-35, requested data BMI <=35; Markov microsimulation, two strategies; payer perspective excludes time; QoL-derived QALYs; survey mortality; national costs/utilization; probabilistic sensitivity; longitudinal outcome probabilities; TreeAge Pro2018/Excel2017.; matches Ancillary outcome status and analysis | COMPLETE; ancillary monetary/QALY thresholds and BMI ranges inspected as prospective design; no forced current-result comparison |
| N150 | SUPPORT-B-006 | DOC-003 p3 REPORT | Eligibility: original randomized and underwent allocated intervention; T2D, BMI 27-45, age 18-65; 4 trials, 3 operations; site-specific randomization; no team masking; lifestyle at least 1 year.; matches Participant population and intervention | COMPLETE; every retained input, count, displayed unit and applicable numeric relationship reviewed; no qualifying numeric discrepancy |
| N151 | SUPPORT-B-007 | DOC-003 pp3-4 REPORT | Annual 12-month window +/-6 months; prior missed visits do not remove eligibility; remote/EMR retrieval except fasting glucose; BP after 5 minutes; central laboratory; available 305 of 316 randomized/treated; OSMB twice yearly, no formal safety stopping rules.; matches Visit windows, flow and stopping | COMPLETE; every retained input, count, displayed unit and applicable numeric relationship reviewed; no qualifying numeric discrepancy |
| N152 | SUPPORT-B-008 | DOC-003 p4 REPORT | Inferential ITT HbA1c change mixed-effects: fixed group, visit, interaction, site, baseline HbA1c; participant Gaussian mean-zero random intercept; LS means and linear contrasts; year 7 primary.; matches Primary analysis | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N153 | SUPPORT-B-009 | DOC-003 p4 REPORT | Inferential four-category treatment replacement for pairwise comparisons with multiplicity adjustment.; matches Surgery-type contrasts | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N154 | SUPPORT-B-010 | DOC-003 pp4-5 REPORT | Inferential continuous secondary percent change uses same mixed model with site/baseline value; binary GEE group, visit, interaction, site, baseline HbA1c; LS estimates/sandwich SE; secondary results hypothesis generating, no multiplicity adjustment.; matches Secondary methods, effect measures and tests | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N155 | SUPPORT-B-011 | DOC-003 p5 REPORT | Inferential exploratory baseline BMI <35 restriction, same methods.; matches BMI subgroup | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N156 | SUPPORT-B-012 | DOC-003 p5 REPORT | Inferential ITT E(Y_t)=alpha_t+beta_t X+gamma^T Z; t=1..12; X=0 MED,1 SURG; Z=site/baseline HbA1c; beta is SURG-minus-MED mean change. PP uses X_t=0 before crossover and 1 after; no reverse crossover.; matches PP exposure and estimand | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N157 | SUPPORT-B-013 | DOC-003 p5 REPORT | Inferential stabilized w_t=product k=1..t of P(X_k given treatment history)/P(X_k given treatment and prior HbA1c histories,Z). Logistic numerator previous groups; denominator adds site/HbA1c; R ipw; truncate 2.5/97.5 percentiles; weighted mixed-effects/robust sandwich SE; also weight; ATE entire population; no unmeasured confounding, positivity and model assumptions.; matches PP IPW sensitivity | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N158 | SUPPORT-B-014 | DOC-003 pp5-6 REPORT | Inferential follow-up 7-15 years, all minimum 7; staggered entry causes structural absence years 8-12; missed clinical/lab EMR recovery; death/loss random censoring, monotone MAR; mixed-effects/GEE under MAR.; matches Missing data and populations | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N159 | SUPPORT-B-015 | DOC-003 p6 REPORT | Inferential adverse-event/outcome percentages chi-squared or Fisher exact; RStudio/SAS9.4.; matches Safety test conventions | COMPLETE; numeric indexing, population, exposure and estimand definitions reviewed; inferential specialist independent coverage required |
| N160 | SUPPORT-B-016 | DOC-003 p8 REPORT | eFigure1 complete BMI distributions, ticks, labels and units below.; matches Baseline BMI | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N161 | SUPPORT-B-017 | DOC-003 p9 REPORT | Inferential eFigure2 HbA1c LS means years 0-12, solid ITT/dashed PP; full visual reconstruction below; no printed CI/P.; matches HbA1c and PP | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N162 | SUPPORT-B-018 | DOC-003 p9 REPORT | Inferential eFigure2 weight year7 ITT 8.3 MED/19.9 SURG, PP 5.6/20.4; total percent initial weight loss.; matches Weight and PP | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N163 | SUPPORT-B-019 | DOC-003 p10 REPORT | eFigure3 medication categories at annual visits 0,7,12; MED/SURG Ns 96/166,50/119,32/86; all bars below.; matches Medication and Table2 | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N164 | SUPPORT-B-020 | DOC-003 p11 REPORT | Inferential eFigure4 annual incretin percentages years 0-12, overall P<.001; all bars below.; matches Incretin narrative | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N165 | SUPPORT-B-021 | DOC-003 p12 REPORT | Inferential eFigure5 SBP mmHg LS means/one SE/overall P=.16; all thirteen contributor Ns below.; matches SBP and Table2/eTable2 | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N166 | SUPPORT-B-022 | DOC-003 p12 REPORT | Inferential eFigure5 HDL mg/dL LS means/one SE/overall P<.001; all contributor Ns below.; matches Lipids and Table2/eTable2 | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N167 | SUPPORT-B-023 | DOC-003 p12 REPORT | Inferential eFigure5 LDL mg/dL LS means/one SE/overall P=.83; all contributor Ns below.; matches Lipids and Table2/eTable2 | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N168 | SUPPORT-B-024 | DOC-003 p12 REPORT | Inferential eFigure5 triglyceride mg/dL LS means/one SE/overall P<.001; all contributor Ns below.; matches Lipids and Table2/eTable2 | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N169 | SUPPORT-B-025 | DOC-003 p13 REPORT | Inferential eFigure6 HbA1c LS means/one SE, BMI <35/>35; year7 low BMI MED8.3/SURG7.4, high BMI MED8.1/SURG7.0.; matches BMI and HbA1c | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N170 | SUPPORT-B-026 | DOC-003 p13 REPORT | Inferential eFigure6 year7 weight low BMI MED5.6/SURG20.4, high BMI MED10.1/SURG19.3; differences 14.8 low/9.2 high; P=.03.; matches BMI and weight | COMPLETE; all figure numbers/series/contributor arrays/units reviewed; unlabelled coordinates not exact inputs; printed caption values reconcile |
| N171 | SUPPORT-B-027 | DOC-003 p14 REPORT | eTable1 N262 at7 years/N130 at12 years; every age/sex/race cell below; other race 4(1.9),2(1.5) retained.; matches Baseline and analysis Ns | COMPLETE; categorical totals/percentages checked; Other4(1.9%) withN262 does not reconcile: F-NUM-101 |
| N172 | SUPPORT-B-028 | DOC-003 p14 REPORT | eTable1 every waist/weight/BMI/BMI<35/BP/duration cell below.; matches Baseline anthropometrics | COMPLETE; every categorical n/N/% and continuous summary cell checked; quantities/dispersion types distinguished |
| N173 | SUPPORT-B-029 | DOC-003 p14 REPORT | eTable1 every HbA1c/glucose/lipid/creatinine/urine ACR cell below.; matches Baseline laboratories | COMPLETE; every categorical n/N/% and continuous summary cell checked; quantities/dispersion types distinguished |
| N174 | SUPPORT-B-030 | DOC-003 p14 REPORT | eTable1 every medication n/% below; continuous mean(SD)/median[P25,P75]; all reached7 years, subset130 reached12.; matches Baseline medication and follow-up | COMPLETE; every categorical n/N/% and continuous summary cell checked; quantities/dispersion types distinguished |
| N175 | SUPPORT-B-031 | DOC-003 pp15-16 REPORT | Inferential eTable2 all11 continuous rows, observed year12 mean(SD)/median[IQR], two changes/95%CIs, between-group change/95%CI/P, every cell below.; matches Year12 outcomes and Table2 | COMPLETE; all eTable2 cells/within-changes/between-contrasts/OR labels reviewed; contrasts reconcile under half-unit intervals; year7 footnote wording excluded |
| N176 | SUPPORT-B-032 | DOC-003 pp15-16 REPORT | Inferential remission MED0%,change NA; SURG12.7%,OR23.6(1.2,465.3); group NA; P<.001; footnote MED2e-16 yields near-zero within-group OR and near-infinite between-group OR.; matches Year12 remission | COMPLETE; all eTable2 cells/within-changes/between-contrasts/OR labels reviewed; contrasts reconcile under half-unit intervals; year7 footnote wording excluded |
| N177 | SUPPORT-B-033 | DOC-003 pp15-16 REPORT | Inferential eTable2 total/oral-GLP1/insulin medication and HbA1c<7/<6.5; every percentage, within-OR/between-OR,95%CI/P below.; matches Year12 medication and glycemic control | COMPLETE; all eTable2 cells/within-changes/between-contrasts/OR labels reviewed; contrasts reconcile under half-unit intervals; year7 footnote wording excluded |
| N178 | SUPPORT-B-034 | DOC-003 pp15-16 REPORT | Effect definitions: net HbA1c change, urine ACR fold change, other relative changes, binary OR; continuous SURG minus MED, binary odds SURG/MED; title year12 and several footnotes year7. Fasting glucose study in-person only. Exact wording retained.; matches Time point and quantity identity | COMPLETE; all eTable2 cells/within-changes/between-contrasts/OR labels reviewed; contrasts reconcile under half-unit intervals; year7 footnote wording excluded |
| N179 | SUPPORT-B-035 | DOC-003 p17 REPORT | Inferential eTable3 every abnormality threshold, each group n/N/%/P below; MED reference, observed assay denominator.; matches Nutritional abnormality and safety | COMPLETE; all8 abnormalities and every n/N/%/procedure sum checked; assay denominators147/151 distinct from166 |
| N180 | SUPPORT-B-036 | DOC-003 p18 REPORT | Inferential eTable4 all seven nutritional LS means/group SEs/SURG-minus-MED difference SE/P below.; matches Nutritional variables | COMPLETE; all7 LSmean/SE/difference rows reconcile with precision; rounded calciumSE0.0 excluded as display precision |
| N181 | SUPPORT-B-037 | DOC-003 pp19-20 REPORT | Inferential eTable5 all48 adverse-event rows, MED96/SURG166, n/%/P and operation-specific footnotes below.; matches Adverse events and safety | COMPLETE; all48 rows and procedure footnotes checked; n96/166 percentages and reconstructed footnote counts reconcile |
| N182 | SUPPORT-B-038 | DOC-003 p21 REPORT | Inferential eTable6 all25 procedure rows, MED96/SURG166, n/%/P below.; matches Procedures and safety | COMPLETE; all25 procedure rows checked; n96/166 percentages reconcile |
| N183 | SUPPORT-B-039 | DOC-003 p22 REPORT | Crossovers24/96(25%), AGB1/96(1%), SG15/96(16%), RYGB8/96(8%); AGB removal7/36(19%), toRYGB4/36(11%),toSG1/36(3%);SGtoRYGB3/41(7%); crossover median4.5years,range[.4,9.8].; matches Flow, PP and crossover | COMPLETE; all explicit fractions/totals checked;1+15+8=24,7+4+1+3=15 and all printed percentages reconcile |

## Completeness and limitations

Every assigned numeric group is complete, including no-applicable main pages10–11, DOC-002 administrative/reference pages41–54 and64–65, supplement cover/contents/reference units and DOC-004 data-sharing page. Figure lines/boxes without printed coordinates cannot supply exact per-point data; this is an extraction precision limitation, closed for scientific review by complete image-based mapper records and all exact printed caption/tabular values. No scientific-coverage gap, missing source, missing tool or unprocessed group. Native numerical summaries do not identify unavailable individual-level observations; none are inferred.

Direct new candidate-location derivatives were generated by Poppler26.01.0 pdftotext-layout on CPU; their paths and source coverage are recorded in the checker. Sources and reused assets are unchanged. Relationship count116; findings2; excluded apparent observations4.
# Numeric relationship inventory — protocol first-half shard

Scope: DOC-002 physical PDF pp.1–40, PLAN throughout; all 90 PLAN-A mapping keys, N184–N273, one key per row in source order (earliest source occurrence; source-layout order for ties). Source: [supplied protocol](../../../joi240004supp1_prod_1721756962.80052.pdf#page=1). Locator evidence: extraction/parts/support_001.md and source-matched reusable Poppler layout; candidate evidence, if any, requires direct source authority. Only this artifact and checkers/parts/numeric_plan_extra.md are owned by this shard. No other source or prior conclusions were used.

Each COMPLETE row records the numeric check or explicitly records no applicable standalone numeric check. Context/design relationships remain available to the cross-source and statistical lanes; numeric completion does not assert that those distinct checks reconcile. All percentages below are percentages, not fractions, unless explicitly stated.

| N ID | Mapping key | PLAN location | Numeric rule, inputs, and completed check |
|---|---|---|---|
| N184 | PLAN-A-VERSION | p1; pp1–40 | COMPLETE: administrative version/date context; no applicable count, denominator, or result arithmetic. |
| N185 | PLAN-A-ABBREVIATIONS | p6 | COMPLETE: label context; no applicable numeric check. |
| N186 | PLAN-A-AIMS | p7; p16 | COMPLETE: three aim labels identify distinct analyses; no participant subtotal inferred. |
| N187 | PLAN-A-PRIMARY | p7; p8; p16–17; p26; p29 | COMPLETE: relative percent HbA1c change, not percentage-point change; no displayed primary effect to recompute in this PLAN scope. |
| N188 | PLAN-A-SECONDARY | p7; p16; p18; pp29–30 | COMPLETE: endpoint hierarchy/design context; no applicable count arithmetic. |
| N189 | PLAN-A-PREDICTORS | p7; pp15–16 | COMPLETE: predictor definitions; no standalone numerical estimate. |
| N190 | PLAN-A-FLOW | p8 | COMPLETE: randomized and treated cohort, consent, annual/quarterly contact; no participant counts printed in diagram. |
| N191 | PLAN-A-PRIMARY-TIME | p8; p27 | COMPLETE: 7-year primary contrast distinguished from annual secondary contrasts; no numeric subtotal. |
| N192 | PLAN-A-COHORT-BASE | p9; pp16–17 | COMPLETE: 355 randomized and302 available planning counts repeat pp27–28; 35% BMI<35 vs one-third is approximate and differs below display threshold. |
| N193 | PLAN-A-PARENT-MEDICAL | pp13–14 | COMPLETE: intervention context; historical results not final package results. |
| N194 | PLAN-A-DURATION | pp16–17; p7 | COMPLETE: 7 additional years, five years collected, baseline-to7/up-to13 retained as distinct printed timing statements; no denominator arithmetic; endpoint/time comparison assigned cross-source lane. |
| N195 | PLAN-A-DESIGN | p17 | COMPLETE: four parent sites match four site columns elsewhere; design context. |
| N196 | PLAN-A-POPULATION | p17 | COMPLETE: BMI27–45 and treatment-initiation population; no displayed analyzed numerator/denominator. |
| N197 | PLAN-A-ORIGINAL-ELIGIBILITY | p17 | COMPLETE: seven criteria, age20–65 and BMI>27 to45 retained; threshold context, no count arithmetic. |
| N198 | PLAN-A-CONTROL | p18; p29 | COMPLETE: HbA1c<7.0 on/off medication binary proportion; no event count denominator printed. |
| N199 | PLAN-A-REMISSION | p18; p29 | COMPLETE: HbA1c<6.5 off medication; no numerator/denominator printed. |
| N200 | PLAN-A-PARTIAL | p18; p29 | COMPLETE: HbA1c<6.5 with/without medication; nested endpoint, not mutually exclusive categories to sum. |
| N201 | PLAN-A-RELAPSE-DEFINITION | p18; p30 | COMPLETE: remitter-only risk set; HbA1c≥6.5 and/or restarting medication; no survival denominator printed. |
| N202 | PLAN-A-BODY | p18; p29 | COMPLETE: two continuous relative-change endpoints weight/BMI; no displayed effect arithmetic. |
| N203 | PLAN-A-CARDIOMETABOLIC | p18; pp29–30 | COMPLETE: percentage-change endpoint definitions and measured-microalbumin subset; no denominator inferred. |
| N204 | PLAN-A-QOL | p18; p25; p29 | COMPLETE: eight subscales listed; physical/mental components distinct from subscales; no participant subtotal. Absolute/relative change comparison belongs design lane. |
| N205 | PLAN-A-EVENTS | p18; p30 | COMPLETE: four listed components stroke/retinopathy/nephropathy/foot ulcer; binary occurrence can overlap, not additive counts. |
| N206 | PLAN-A-SAFETY-ASCERTAINMENT | p18 | COMPLETE: event vs AE/source-verification context; no numeric denominator. |
| N207 | PLAN-A-TABLE1 | p19 | COMPLETE: fifteen cluster rows reconcile stated fifteen; components are overlapping definitions, no event-count sum specified. |
| N208 | PLAN-A-EXPLORATORY | p20 | COMPLETE: three endpoint groups; no result count arithmetic. |
| N209 | PLAN-A-ENROLLMENT | p20 | COMPLETE: initiated randomized treatment and consent define cohort; no final enrollment total stated. |
| N210 | PLAN-A-CROSSOVER-ELIGIBILITY | p20 | COMPLETE: later surgery does not exclude initially medical participants; no subgroup count displayed. |
| N211 | PLAN-A-WITHDRAWAL | pp20–21 | COMPLETE: records/telephone follow-up distinguish visit absence from withdrawal; no numerical retention claim. |
| N212 | PLAN-A-OBSERVATIONAL-CARE | p21 | COMPLETE: no new intervention; no numerical dose comparison. |
| N213 | PLAN-A-GLYCEMIC-TARGET | p21 | COMPLETE: clinical target<6.5 differs by purpose from control endpoint<7; no arithmetic conflict. |
| N214 | PLAN-A-HISTORICAL-LABS | p22 | COMPLETE: historical measurement availability is conditional; no assumed complete denominator. |
| N215 | PLAN-A-VISIT-WINDOW | pp22–23 | COMPLETE: annual12months preferred±3 accepted±6; nested windows reconcile Table2 footnote. |
| N216 | PLAN-A-LABS | pp22–23; p25 | COMPLETE: Chem20 list contains20 analytes; height first annual only; no result-count denominator. |
| N217 | PLAN-A-INTERIM-CONTACT | pp23–24 | COMPLETE: three contacts at3/6/9months between annual visits; preferred±1 accepted±1.5, consistent schedule. |
| N218 | PLAN-A-SCHEDULE | pp24–25 | COMPLETE: annual/interim windows reproduce narrative; height first annual; historical measurements not assumed available for every participant. |
| N219 | PLAN-A-SAFETY-START | pp25–26 | COMPLETE: consent-date ascertainment context; no count arithmetic. |
| N220 | PLAN-A-EMERGENCY | p26 | COMPLETE: procedure adaptation context; no alternate numeric endpoint/model specified. |
| N221 | PLAN-A-BASELINE-TESTS | p26 | COMPLETE: site-adjusted continuous and CMH categorical methods; no displayed baseline counts here. |
| N222 | PLAN-A-A1-MODEL | pp26–27 | COMPLETE: i=1..4 sites, j=1..n_i patients, X=1/0 groups; effect-scale identity relative HbA1c change. Fixed/random specification assigned statistical lane; no effect printed here. |
| N223 | PLAN-A-A1-TEST | p27 | COMPLETE: beta7 group contrast, null0, two-sided alpha.05; no reported test estimate to recompute. |
| N224 | PLAN-A-OTHER-YEARS | p27 | COMPLETE: annual contrasts up to13years secondary, not separate cohort totals. |
| N225 | PLAN-A-A2-MODEL | p27 | COMPLETE: logit outcome and beta7 log OR surgery vs nonsurgical; no crude ratio printed to conflict with label. |
| N226 | PLAN-A-RELAPSE-METHOD | p27 | COMPLETE: descriptive KM, remitter-only analysis, no group-test count. |
| N227 | PLAN-A-POWER-INPUTS | p27 | COMPLETE: year1 −24.0/−9.1; year3 −21.6/−0.1; year5 approx−20/−2; assumed surgery−20→−15 yields +2.5 percentage points/year over5→7; nonsurgery scenarios−7..+2 not claimed observed extrapolations. |
| N228 | PLAN-A-COHORT-POWER | pp27–28 | COMPLETE:325−20−3=302; randomized355−initiated325=30; 20/325×100=6.1538 rounds6%;3/325×100=.9231 rounds.9%;302×.8=241.6≈242. |
| N229 | PLAN-A-POWER-SIMULATION | p28 | COMPLETE:500 simulations,.05,SD.06/.15/.10,rho.13; power percentage increments.2%; no reproducible simulation result from numeric inputs alone; model logic assigned statistical lane. |
| N230 | PLAN-A-REMISSION-POWER | p28 | COMPLETE:46/1 year1,32/0 year3 are group percentages without counts; assumed20/5 year7;94.6%=473/500 is possible simulation fraction. |
| N231 | PLAN-A-PARTIAL-POWER | p28 | COMPLETE:assumed27/7 year7;98.6%=493/500 is possible simulation fraction; no raw event counts to recompute. |
| N232 | PLAN-A-CONTROL-POWER | p28 | COMPLETE:75/52,63/38,48/22 at1/3/5years; assumed39/11 at7years; absent fitted linear-logit slope/intercept, unique projection unavailable; statistical lane retains claim. |
| N233 | PLAN-A-FIGURE-A1 | p29 | COMPLETE:302×(1−0/.1/.2/.3)=302/271.8/241.6/211.4, displayed302/272/242/211, all round; legend surgery−15 vs−7/−5/0/+2. Unlabeled point ordinates not invented. |
| N234 | PLAN-A-POWER-MISSING | p29 | COMPLETE:discard any-missing simulated participants vs all-available actual analysis; no additional arithmetic claim. |
| N235 | PLAN-A-TABLE-A1 | pp29–30 | COMPLETE:hierarchy/types repeat endpoint definitions; four vascular components reconcile; no percentage sums of overlapping outcomes. |
| N236 | PLAN-A-MISSING-MAR | p30 | COMPLETE:.9% mortality repeats cohort3/325=.9231%, within display intervals; no new denominator. |
| N237 | PLAN-A-MICE | p30 | COMPLETE:imputation/combination context; no stated imputation count to reconcile. |
| N238 | PLAN-A-PATTERN-MIXTURE | p30 | COMPLETE:missingness context; no numeric estimate. |
| N239 | PLAN-A-CROSSOVER-MSM | pp30–31 | COMPLETE:weight=IPTW×censoring weight, noncrossoversIPTW1 as stated; no displayed weights or counts to recompute. |
| N240 | PLAN-A-PER-PROTOCOL | p31 | COMPLETE:post-crossover outcomes discarded, not necessarily all participant outcomes; no population-size number. |
| N241 | PLAN-A-A3-INTERVENTIONS | p31 | COMPLETE:four intervention indicators match RYGB/LAGB/SG/nonsurgery;4×3/2=6 possible pairwise contrasts per year, no printed multiplicity count to conflict. |
| N242 | PLAN-A-HETEROGENEITY | p31 | COMPLETE:site model/interval context belongs statistical logic; no printed site-effect count beyond four. |
| N243 | PLAN-A-TAXONOMY | pp31–32 | COMPLETE:four component classes exercise/diet/medication/other; exercise further supervised/unsupervised, not a fifth class. |
| N244 | PLAN-A-TABLE-A2 | p32 | COMPLETE:176+196=372;12+222=234;0+183=183;0+174=174hrs/year, exact column totals; diet32/22/2/28 and other26/22/2/28 have no aggregate claim. |
| N245 | PLAN-A-MEDICATION-CLASSES | p32 footnote | COMPLETE:drug-class context; no numeric count/percentage claim. |
| N246 | PLAN-A-SURGERY-COUNTS | pp32–33 TableA3 | COMPLETE:104+49+39=192;RYGB50+20+19+15=104;SG49;AGB21+18=39; site50+49=99,20+21=41,19+18=37,15;99+41+37+15=192. |
| N247 | PLAN-A-SURGERY-NARRATIVE | pp32–33 | COMPLETE:construction15–20/40mL,150/75cm,approx50cm,32French,75–80% retained; no outcome estimate or participant denominator. Narrative/table range differences listed once as peripheral. |
| N248 | PLAN-A-TABLE-A4 | p33 | COMPLETE:N104=50+20+19+15; site counts match TableA3. Operative ranges not treated as statistical effect estimates. |
| N249 | PLAN-A-A4-TAXONOMY | pp33–34 | COMPLETE:three surgery indicators, fourth coefficient supervised exercise;beta71−100beta74 matches stated RYGB-versus100hours contrast; no printed effect to recompute. |
| N250 | PLAN-A-TAXONOMY-DATA | p34 | COMPLETE:quarterly values normalized yearly; no observed dosage values. |
| N251 | PLAN-A-BASELINE-SENSITIVITY | p34; p35 | COMPLETE:P<.05 selection rule no printed P/value conflict. |
| N252 | PLAN-A-BMI-SUBGROUP | p34 | COMPLETE:BMI<35 threshold preserved; no subgroup denominator claimed. |
| N253 | PLAN-A-AIM2-MODELS | p34 | COMPLETE:2×2 event tables are categorical framework, no table cells printed. |
| N254 | PLAN-A-AIM2-POWER | pp34–35 | COMPLETE:delta.43–.47×SD6%=2.58–2.82%;approx2.8 fits, no conflict;20%missing and80%power design assumptions; OR3.03 matches TableA5. |
| N255 | PLAN-A-TABLE-A5 | p35 | COMPLETE:delta.47/.43,OR3.03/2.46 atp10/20; OR nonsurgical/surgical explicit, not RR. No event counts support conflicting identity. rho.1 plus footnote1 is not .11. |
| N256 | PLAN-A-AIM2-MULTIPLICITY | p35 | COMPLETE:unadjusted power for secondary endpoints distinct from Bonferroni intervention pairwise comparisons; no arithmetic conflict. |
| N257 | PLAN-A-AIM2-SENSITIVITY | p35 | COMPLETE:sensitivity design context; no numeric result. |
| N258 | PLAN-A-AIM3-PREDICTORS | pp35–36 | COMPLETE:predictor selection context; no model coefficient values. |
| N259 | PLAN-A-AIM3-COX | p36 | COMPLETE:HR multiplicative scale; no printed event count/effect-label conflict. |
| N260 | PLAN-A-AIM3-AFT | p36 | COMPLETE:log-time additive scale distinguished from HR; no numeric result. |
| N261 | PLAN-A-AIM3-RELAPSE | p36 | COMPLETE:remitters-only risk set, no printed denominator. |
| N262 | PLAN-A-AIM3-MULTISTATE | p36 | COMPLETE:three states initial/remission/death match stated count. |
| N263 | PLAN-A-SOFTWARE | p36 | COMPLETE:version9.3 administrative software identifier; no applicable numeric result. |
| N264 | PLAN-A-TABLE-A6 | p36 | COMPLETE:30%,R².1,HR1.36 narrative exactly matches table; at20/30/40% HRs decrease as events increase and increase withR².1/.2/.5; PASS11 settings insufficient for full numeric rerun, statistical lane covers inferential reproduction. |
| N265 | PLAN-A-ANALYSIS-POPULATION | p36 | COMPLETE:consent and original allocation ITT; no numeric analyzed total stated. |
| N266 | PLAN-A-SERIOUS-OUTCOMES | p37 | COMPLETE:event-definition context; no count arithmetic. |
| N267 | PLAN-A-AE-DEFINITION | p38 | COMPLETE:AE-definition context; no numerical count. |
| N268 | PLAN-A-EVENT-VERIFICATION | p38 | COMPLETE:Grade1/2 laboratory exclusion is criterion, not event-count denominator. |
| N269 | PLAN-A-DEATH-RECORDING | p38 | COMPLETE:24-hour notification is operational window; no additional mortality count. |
| N270 | PLAN-A-ADJUDICATION | p39 | COMPLETE:five external members administrative panel count; no result arithmetic. |
| N271 | PLAN-A-STOPPING | p39 | COMPLETE:no formal stopping rule,6monthly oversight; no numeric efficacy boundary to recompute. |
| N272 | PLAN-A-CONSENT-REVOCATION | p39 | COMPLETE:retained prior data, no population-size numeric claim. |
| N273 | PLAN-A-HISTORICAL-DATA | p40 | COMPLETE:historical-data provenance; no additional quantitative relationship. |

## Display precision and mechanical checks

Integer participant counts used as exact counts above; allowing mandated half-unit intervals only widens reconciliation. For20/325, half-unit bounds give5.9908–6.3174%, overlapping6% display interval5.5–6.5. For3/325, bounds give.7680–1.0786%, overlapping.9% interval.85–.95. For missing20%,302±.5 and20±.5% produce retained-count interval239.6925–243.5125, overlapping242±.5. Figure displayedN272/242/211 all overlap corresponding rounded-input product ranges. All have zero interval gap and zero relative discrepancy. Figure0% is a no-missing scenario; its N302 repeats cohort directly.

For residual SD6±.5 and detectable delta bounded by printed endpoints.43±.005 and.47±.005, their product allows2.3375–3.0875%, overlapping2.8±.05%. Even central values2.58–2.82 include2.8. The table superscript afterrho=.1 is the footnote marker; it supplies no substituted decimal digit.

## Closure

90/90 mapping keys checked;90 COMPLETE rows;0 numeric findings;5 excluded observations in companion checker;0 scientific coverage gaps. Unlabeled FigureA1 ordinate values and unavailable Monte Carlo/PASS settings are limitations on exact reproduction, not omissions of any printed relationship. No new extraction/rendering/OCR derivative was required; reusable assets unchanged. Cross-source endpoint/status/model checks and statistical method/power reproduction belong to their separate full-scope lanes.
