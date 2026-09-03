# Support quantitative evidence map: results supplement pp. 1-32

## Scope and evidence handling

- **Source ID:** `JAMA2025_9110_D04_RESULTS_SUPP`.
- **Direct source:** `joi250040supp3_prod_1753124024.38098.pdf`, PDF pages 1-32 (not the printed supplement-page numbers).
- **Scope status:** COMPLETE: 32/32 assigned PDF pages directly inspected. Existing source-matched native/normalized text and renders were used as locators. Direct `pdftotext` native/layout derivatives and pp. 1-5 renders were generated only in `preprocessing/results-supp-001/`. Tables and figures were visually checked against the PDF/rendered-page evidence; direct PDF is controlling.
- **Conventions:** values in parentheses in descriptive tables are median (IQR), unless the table labels `n (%)`. Treatment is Augmented Protein; control is Usual Protein. `RS1-N` is a numeric/reporting relationship and `RS1-S` an inferential relationship. These are provisional relationship IDs, not candidate IDs or dispositions.

## Page-by-page coverage

| PDF page | Content and quantitative coverage | Relationship IDs | Status |
|---:|---|---|---|
| 1 | Cover/list of eMethods, eTables 1-14, eFigures 1-7; no results beyond contents. | — | NO_APPLICABLE_RESULT |
| 2 | Detailed contents with section/page locators; no results. | — | NO_APPLICABLE_RESULT |
| 3 | Data collection days 1-5, 10, 20, 30, 90; duration of trial feeding is hours from first commencement through final cessation, including readmission episode. | RS1-N001 | MAPPED |
| 4 | Eight audits (four mid-cluster, three crossover, one completion); ventilation analysis changed from SAP time-to-event to lower-bounded continuous Tobit mixed model, adjusted for period/delayed start, ICU random effect, reported as mean difference (95% CI). AE ascertainment window starts at formula commencement to 48 h after cessation. | RS1-N002; RS1-S001 | MAPPED |
| 5 | Biochemistry collected ICU days 1, 5, 10. Primary-outcome secondary analyses: linear mixed model and Bayesian quantile mixed model; Bayesian estimate is treatment coefficient/difference in medians with 95% credible interval. Sensitivity exclusions: non-trial formula, palliative care, organ donation; no primary outcome missing data, so no imputation. | RS1-N003; RS1-S002 | MAPPED |
| 6 | Bayesian details: four chains, 1000 retained samples each after 1000 burn-in = 4000 per parameter; 95% CrI = posterior 2.5th/97.5th percentiles. Binary outcomes use Fay-Graubard small-sample sandwich correction; ICU/hospital discharge use cumulative incidence and cause-specific Cox; subgroup interaction uses LR test and subgroup CIs block bootstrap. | RS1-S003-RS1-S006 | MAPPED |
| 7 | Inclusion: age >=16, receiving/about to begin EN; exclusion includes >12 h nontrial EN. Start of outcome definitions. | RS1-N004 | MAPPED |
| 8 | Primary outcome = 90 minus index-hospital days after formula commencement minus pre-day-90 hospital readmission days; death by day 90 assigned zero. Survivors outcome applies same formula. Defines binary alive-at-day-90, nonnegative ventilation hours, competing-risk ICU/hospital discharge durations, tracheostomy and post-EN KRT incidence. | RS1-N005-RS1-N010 | MAPPED |
| 9 | eTable 3 sequence baseline: sequence 1 4 units n=2044, sequence 2 4 units n=1353; regional/site counts and percentages. | RS1-N011 | MAPPED |
| 10 | eTable 4 period/treatment baseline, first half: period/group denominators 480,335,298,530,551,368,352,483; sex, age, weight, BMI, IBW, APACHE II, admission type/category, frailty, diabetes. | RS1-N012 | MAPPED |
| 11 | eTable 4 continuation: ICU admission source, ventilation/vasopressor/KRT/parenteral-nutrition status, baseline biochemistry. | RS1-N013 | MAPPED |
| 12 | eTable 4 continuation: albumin/potassium/glucose and treatment-goal categories; units/definitions footnotes. | RS1-N014 | MAPPED |
| 13 | eTable 5 EN delivery at days 1,2,3,4,5,10,20,30,90; treatment/control denominators 1681/1716, n at each time, calorie/protein medians/IQR, PN and protein-supplement proportions. | RS1-N015 | MAPPED |
| 14 | eTable 6 all feeding days: IBW/ABW calories and protein medians (Q1,Q3), missing counts, 103 volume-only exclusions (49 treatment, 54 control). | RS1-N016 | MAPPED |
| 15 | eTable 7 excluding enrolment day: treatment/control N=1632/1662, same four intake metrics/missing counts and 103 volume-only exclusions. | RS1-N017 | MAPPED |
| 16 | eTable 8 protocol deviations by group: participant/event totals and five deviation types. | RS1-N018 | MAPPED |
| 17 | eTable 9 audit: mid-cluster/crossover/completion/total n=292/224/52/568; five formula-status categories and explanatory narrative. | RS1-N019 | MAPPED |
| 18 | eTable 10 period/group descriptive primary/secondary outcomes, denominators, medians/IQR and n(%); includes a printed comma in one percentage. | RS1-N020; seed RS1-N-SEED01 | MAPPED |
| 19 | eTable 11 biochemistry day 1/5/10 medians/IQR and available-n per group for urea, albumin, phosphate, glucose. | RS1-N021 | MAPPED |
| 20 | eTable 12 AEs/SAEs by group, participants with >=1 event and event counts, with named event components. | RS1-N022 | MAPPED |
| 21 | eTable 13 AE/SAE participants and event counts by period/treatment group. | RS1-N023 | MAPPED |
| 22 | eTable 14 total ICU/hospital, index-hospital ICU, post-index ICU, and post-index hospital readmission count distributions before day 90. | RS1-N024 | MAPPED |
| 23 | eFigure 1 cluster crossover: two groups of four ICUs over periods 1-4/months 1-12. eFigure 2 protein/calorie day trajectories with medians, Q1/Q3 and individual profiles. | RS1-N025 | MAPPED |
| 24 | eFigure 3 IBW-normalized protein/calories boxplots at days 1,2,3,4,5,10,20,30 with plotted sample sizes. | RS1-N026 | MAPPED |
| 25 | eFigure 4 ABW-normalized protein/calories boxplots at the same days with plotted sample sizes. | RS1-N027 | MAPPED |
| 26 | eFigure 5 histogram: primary outcome days free of index hospital/alive at day 90, treatment and control. | RS1-N028 | MAPPED |
| 27 | eFigure 6 Bayesian posterior: median difference -1.50 (95% CrI -3.86 to 0.90); plot shades benefit/harm about zero. | RS1-S007 | MAPPED |
| 28 | eFigure 7 subgroups (IMV, renal replacement therapy [RRT], age, BMI): N, median(IQR), median difference (95% CI), interaction P annotations. | RS1-S008-RS1-S011; seed RS1-S-SEED02 | MAPPED |
| 29 | ICEMAN form: mechanical-ventilation subgroup, outcome days free/alive day 90, measure median (95% CI), interaction P=0.023, four modifiers tested, overall credibility marked very low. | RS1-S008 | MAPPED |
| 30 | ICEMAN mechanical-ventilation continuation; result is an author-supplied credibility assessment, not an additional effect estimate. | RS1-N029 | MAPPED |
| 31 | ICEMAN renal-failure subgroup: outcome/measure as above, interaction P<0.001, four modifiers, patient subgroup Ns noted 122/119 and wide CI (-50.00, 23.62) days. | RS1-S009; RS1-N030 | MAPPED |
| 32 | ICEMAN renal-failure continuation; moderate credibility assessment; repeats CI context. | RS1-N031 | MAPPED |

## Quantitative relationship inventory

### Definitions and analysis relationships

- **RS1-N001 (p3):** intake time points and duration-of-trial-formula construction; unit hours. This is the denominator/time-window key for eTables 5-7.
- **RS1-N002 (p4):** audit design has 8 audit time points (4+3+1), matching eTable 9 pooled audit columns.
- **RS1-S001 (p4):** ventilation: Tobit mixed effects, adjusted period/delayed start, ICU random intercept; estimand is observed-outcome mean difference, 95% CI. Different outcome framework than the SAP statement is explicitly disclosed here.
- **RS1-S002 (p5):** primary outcome secondary analyses: linear mixed model and Bayesian quantile mixed model (difference in medians/95% CrI).
- **RS1-S003 (pp5-6):** primary quantile mixed model, Nelder-Mead, 1000 bootstrap replications for 95% CI; ICC based on residual/cluster variance.
- **RS1-S004 (p6):** Bayesian model has 4,000 retained posterior samples/parameter after burn-in; CrI 2.5th-97.5th percentiles.
- **RS1-S005 (p6):** binary alive/tracheostomy/KRT analyses use `xtgeebcv` Fay-Graubard correction; discharge duration uses cumulative incidence/cause-specific Cox.
- **RS1-S006 (p6):** subgroup interaction is LR test; subgroup-specific effects from interaction coefficients and block-bootstrap 95% CIs.
- **RS1-N004-RS1-N010 (pp7-8):** eligibility and exact outcome populations/scales, including primary zero assignment for deaths and competing-risk discharge outcomes.

### Table/figure result relationships

- **RS1-N011 (p9):** sequence totals 2044+1353=3397. Within-sequence region and site counts sum to the stated sequence n; displayed proportions are compatible with denominators under rounding.
- **RS1-N012-RS1-N014 (pp10-12):** eTable 4 period/treatment descriptive baseline. The eight group n values sum to 3397 (treatment 1681, control 1716). Numeric rows are medians(IQR) or n(%); category rows are interpreted against their individual group denominators.
- **RS1-N015 (p13):** eTable 5 delivery. Exact printed group totals: treatment/control 1681/1716. Day-specific calorie/protein medians(IQR), available n, and day-90 `n=0` treatment versus one control observation are mapped. PN 115/1681 (6.8%) vs 120/1716 (7.0%); protein supplement 12/1681 (0.7%) vs 10/1716 (0.6%).
- **RS1-N016 (p14):** eTable 6 all feeding days: treatment/control kcal/kg IBW 14(9,19)/14(8,19); protein/kg IBW 1.12(0.71,1.53)/0.69(0.40,0.95); kcal/kg ABW 10.9(6.4,14.9)/10.5(6.3,14.9); protein/kg ABW 0.87(0.51,1.18)/0.53(0.32,0.75). Missing 369/410 for IBW metrics and 215/248 for ABW metrics. Exclusion statement is 49+54=103.
- **RS1-N017 (p15):** eTable 7 excluding enrolment day: treatment/control N 1632/1662; IBW metrics 17(11,22)/17(10,22) and 1.33(0.88,1.78)/0.84(0.49,1.11); ABW 13(8,17)/13(8,17) and 1.04(0.63,1.38)/0.64(0.40,0.88). Missing 382/425 and 243/274 respectively.
- **RS1-N018 (p16):** eTable 8 protocol deviations: participants 151(9.4%)/95(5.6%), events 158/99; type-specific participants/events: clinical decision 92/96 vs 64/68; subsequent-administration error 34/37 vs 17/17; other 13/13 vs 3/3; initial-commencement error 11/11 vs 10/10; unable to locate 1/1 vs 1/1.
- **RS1-N019 (p17):** eTable 9 five categories add to audit totals in each column: 292,224,52,568. Narrative says one `other formula` case was not recorded as a protocol deviation; this is compatible with the table footnote (all other-formula instances except one were deviations).
- **RS1-N020 (p18):** eTable 10 is unadjusted period-by-treatment descriptive results. It maps primary day-free outcome, survivor day-free outcome, alive day 90, ICU/hospital duration, ventilation hours, tracheostomy, post-EN KRT, selected ICU destination, readmission and ICU-readmission duration. Percentages were checked against the printed n in each column with ordinary rounding.
- **RS1-N021 (p19):** eTable 11 medians(IQR) for biochemical measures and available n, declining by later study day as printed; unit mmol/L except albumin g/L.
- **RS1-N022-RS1-N023 (pp20-21):** AE/SAE counts by treatment and by period. Treatment totals reconcile to period counts: AEs treatment 3 and control 1; SAEs treatment 1 and control 1.
- **RS1-N024 (p22):** eTable 14 readmission distributions. Each printed count distribution sums to its group denominator 1681 or 1716; percentages are rounded.
- **RS1-N025 (p23):** figure 1 has two 4-ICU randomization groups/4 periods; figure 2 plots total g/day and kcal/day days 1-30, matching eTable 5 time points/sample counts (excluding day 90 display).
- **RS1-N026-RS1-N027 (pp24-25):** IBW and ABW boxplots identify medians/Q1/Q3 and treatment/control direction; plotted sample counts differ from eTable 5 because body-weight availability/scaling defines the figure populations.
- **RS1-N028 (p26):** primary-outcome histogram has a substantial zero spike in both groups, compatible with the p8 definition assigning zero to deaths; no exact bin counts printed.
- **RS1-S007 (p27):** Bayesian primary outcome median difference -1.50 days, 95% CrI -3.86 to 0.90, compatible with its interval order and the p5 description.
- **RS1-S008 (pp28-30):** IMV subgroup: treatment/control N 296/361 (IMV no) and 1385/1355 (yes); effects 2.7 (-5.24,10.64) and -3.44 (-9.64,2.76), interaction P=0.023, repeated on ICEMAN p29.
- **RS1-S009 (pp28,31-32):** renal-failure/RRT subgroup: N 1559/1597 (no), 122/119 (yes); effects 0 (-4.32,4.32) and -13.19 (-50,23.62); the direct-source-confirmed interaction P value is `P<0.001` on both p28 and p31.
- **RS1-S010 (p28):** age <70 N 1231/1211 effect -3 (-8.48,2.49); >=70 N 450/505 effect 0.85 (-8.98,10.68); displayed interaction P=0.106.
- **RS1-S011 (p28):** BMI <35 N 1066/1074 effect -3.46 (-12.44,5.53); >=35 N 222/206 effect 7.23 (-3.56,18.02); displayed interaction P=0.468.
- **RS1-N029-RS1-N031 (pp29-32):** ICEMAN is a structured credibility appendix. It records result-linked numbers/assessments but does not establish an additional treatment-effect model.

## Candidate seeds for coordinator review (not adjudications)

### RS1-N-SEED01 — printed percentage punctuation / numeric rendering

- **Source location:** supplement PDF p18, eTable 10, `Alive at day 90 [n (%)]`, Period 2 Usual Protein (n=530).
- **Direct observation:** printed `383 (72, 3%)`; 383/530 x 100 = 72.264..., which rounds to 72.3% at one decimal.
- **Rule and question:** comma punctuation makes the displayed percentage nonstandard/ambiguous while all analogous cells use decimal points (e.g., 67.3%, 77.0%, 76.8%, 74.0%). Does the intended printed result read `72.3%`? This is a small measure/label rendering issue, not a conclusion claim.

### RS1-S-SEED02 — resolved RRT/renal-failure interaction P-value transcription check (NONCANDIDATE)

- **Source locations:** supplement PDF p28 eFigure 7 directly confirms the RRT subgroup annotation `P<0.001`; PDF p31 ICEMAN renal-failure form also states `P<0.001` for the same outcome (days free of hospital and alive at day 90), effect measure (median [95% CI]), and renal-failure/RRT modifier. p32 repeats the small subgroup Ns 122/119 and CI (-50.00, +23.62) context.
- **Direct observation:** the p28 and p31 values are consistent. The earlier `p>0.001` entry was an OCR/map transcription issue, not printed-source evidence.
- **Status:** NONCANDIDATE; no unresolved human question remains for this matched P-value relationship.

## Limitations

- The document supplies descriptive values, figure labels and selected model outputs, but not participant-level data or full fitted-model objects; no unsupported recalculation of model-based estimates was attempted.
- PDF pp29-32 are author-supplied ICEMAN forms. Their credibility ratings are mapped as printed context only and are not treated as an adjudication.
