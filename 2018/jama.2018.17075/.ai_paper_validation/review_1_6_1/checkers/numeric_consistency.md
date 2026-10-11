# Complete numeric consistency review

Scope: N001–N140, 140 numeric relationships reviewed by two disjoint fresh numeric agents. Aggregate: 2 findings, 28 excluded observations, 140 explicit COMPLETE records. No scientific coverage gap. The complete shard evidence, self-screening notes and limitations follow; source links are rebased to this canonical artifact.

# Numeric consistency review — shard 1

Scope: N001–N084, 84 relationships. REPORT: main article PDF pp.1–8. PLAN: original protocol and final opening PDF pp.13–49,68–69. Full main and plan_001 maps read; source relationships checked with direct Poppler pdftotext -layout and source-matched rendered main p7. Engine: direct Poppler (tooling record); reused images retained unchanged. No old checker, ledger or report scientific input; no web. Every assigned relationship reviewed, including all components in grouped rows. Counts printed as participant/event integers retain their exact integer value; continuous displayed inputs retain their half-unit rounding intervals. No invented graph ordinates, unreported covariates, or analysis denominators.

## Findings

### F-NUM-001

**Relationship:** N058; statistical cross-reference S010/S011.  
**Locations and roles:** REPORT [main article PDF p3, Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [main article PDF p7, Table2, both bleeding rows](../../../jama_cooper_2018_oi_180132.pdf#page=7). Main p7 table was confirmed visually against the supplied PDF-matched page image and direct layout extraction.  
**Printed inputs:** New/increased intracranial bleeding:47/260(18.1%) versus 37/240(15.4%), absolute difference 2.7(−3.9 to 9.2)pp, relative risk 1.23(0.43–3.5), P=.70. New significant extracranial bleeding:8/260(3.1%) versus 6/240(2.5%), difference 0.6(−2.3 to 3.5)pp, relative risk 1.17(0.79–1.74), P=.43. Methods specify unadjusted χ² comparisons and relative risks for these adverse events.  
**Rule and calculation:** For each unadjusted H-versus-C risk ratio, RR=(H events/H denominator)/(C events/C denominator). Intracranial RR=(47/260)/(37/240)=1.172557; extracranial RR=(8/260)/(6/240)=1.230769. These do not lie in the respective printed RR rounding intervals [1.225,1.235) and [1.165,1.175). Exact integer count inputs leave no rounding ambiguity. Even treating the intracranial printed percentages as half-unit intervals yields RR  in [18.05/15.45,18.15/15.35]=[1.1683,1.1824], disjoint from printed 1.23. Each displayed RR corresponds numerically to the other bleeding outcome's counts. CI widths and P values also travel with the opposite point-estimate pattern, but the inconsistency is established by the exact RR identity alone.  
**Focus area:** A/C, counts to unadjusted effect-measure identity.  
**Proposed review domain:** statistical_results.  
**Proposed relationship type:** S_W; all relationships S_W.  
**Affected result or extracted value:** The unadjusted relative risk and associated 95% CI/P attributed to each of new/increased intracranial bleeding and significant extracranial bleeding. Intracranial bleeding is reported in the abstract; selecting the printed 1.23(0.43–3.5) rather than the count-compatible 1.17 changes its extracted effect and precision.  
**Why context does not resolve it:** The row labels assign two complete inferential packages to distinct outcomes while the row counts and differences remain in the opposite alignment. The table contains no note authorizing reassignment. Computing the risk ratios detects the conflict, but a reader cannot treat the complete printed CI/P attribution as established solely by identifying a likely transposition. The methods do not offer an adjusted-model explanation.  
**Alternatives:** A transposition of the RR/CI/P cells between the two rows explains the point-estimate pattern; a separately unreported analysis producing these numbers would conflict with the stated unadjusted methods. These are possible explanations, not assumed facts.  
**Human question:** Which RR, 95% CI and P value should be attributed to each bleeding outcome, given the printed counts and stated unadjusted analysis?

### F-NUM-002

**Relationship:** N030.  
**Location and role:** REPORT [main article PDF p5 Table1, Injury Severity Score row, normothermia column](../../../jama_cooper_2018_oi_180132.pdf#page=5). Direct layout extraction and source-matched page image agree.  
**Printed inputs:** Row label “Injury Severity Score, median (IQR)”; normothermia 20.0 (20.5–35.0), n=240. Hypothermia 26.0 (18.0–34.0) has coherent ordering. Footnote defines the score range 0–75 and higher scores as greater injury severity.  
**Rule and calculation:** For the same outcome distribution, Q1 ≤ median ≤ Q3. Allowing the half-unit intervals for one-decimal display gives median in [19.95,20.05) and Q1 in [20.45,20.55). Even the largest possible median is below the smallest possible Q1 by at least 0.40 points. No combination of rounding-compatible inputs satisfies the quantile ordering.  
**Focus area:** B, estimate and interval/order logic.  
**Proposed review domain:** statistical_results.  
**Proposed relationship type:** S_W; all relationships S_W.  
**Affected result or extracted value:** The normothermia group's baseline Injury Severity Score median and interquartile range extracted from Table1, used to describe the injury-severity distribution of the analyzed trial population.  
**Why context does not resolve it:** Neither the footnote nor adjacent rows supplies an alternative median or lower quartile. The reader can identify incompatible quantile ordering but cannot identify which numeric component should be used. This is an internal relationship within one displayed distribution, rather than a cross-location comparison of peripheral baseline summaries.  
**Alternatives:** The median may have been transcribed differently from the underlying summary, or the lower quartile may represent a different value. The supplied row does not establish either alternative; no replacement number is proposed.  
**Human question:** What median and lower quartile describe the normothermia Injury Severity Score distribution underlying Table1?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| N005, main p1 versus p5 Table1 | Abstract 402 men conflicts with 207+194=401;80.2% of 500=401 and both group percentages identify the intended baseline count at once. | CONTEXT_RESOLVES |
| N053, main p1 versus pp5/7 | Abstract RD 0.4% lacks minus;117/240<111/226, RR.99, and both narrative/Table2−0.4 identify direction at once. | NOTATION_OR_TYPOGRAPHY |
| N009/N011, main pp4/8 | 27% never 33°C versus 19% withdrawn early plus further 13%; denominators/nesting are not established as a common exclusive partition and exposure summaries do not alter primary denominators. | CONDITIONAL_OR_UNREPORTED |
| N042/N044, main p6 Figure2 | Contributor counts sometimes increase between intervals; caption defines unique observed contributors in each interval, not cumulative survivors. | CONTEXT_RESOLVES |
| N047/N071, main pp3/7 and original plan pp15/25 | Injury versus randomisation six-month wording uses adjacent clinical follow-up anchors separated by the ≤3 h recruitment window, with the endpoint clearly identified. | TERMINOLOGY_OR_WORDING |
| N061, main p6 | Display 70.5%−57.1%=13.4 pp versus RD13.3; input intervals [70.45,70.55),[57.05,57.15) permit differences in [13.30,13.50), overlapping RD rounding interval [13.25,13.35). | ROUNDING_OR_DISPLAY_PRECISION |
| N063/N065, plan p27 | Linear 12% attrition division alone would not produce 496, but 384/.88²=495.87 fits treatment-dilution inflation; the exact inflation formula is unprinted. | CONDITIONAL_OR_UNREPORTED |
| N066/N068/N083, original versus final protocol and main | Changed eligibility, target and temperature details are versioned/amended plans, not simultaneous final specifications; final target 510 amendment resolves 500 synopsis. | CONTEXT_RESOLVES |
| N070, plan p35 Appendix C | Initial bleeding screen placeholder time is clarified by explicit insertion/first-hour thresholds immediately in withdrawal text and original§12.4. | CONTEXT_RESOLVES |
| N075, plan pp26/29 versus main p3 | SAE reporting through 7 days after cessation and AE analysis within 10 days are separate surveillance/analysis definitions; no incompatible matched event count supplied. | CONTEXT_RESOLVES |
| N076, plan p36 | PaO2 mHg is an obvious unit-character omission alongside other mmHg thresholds. | NOTATION_OR_TYPOGRAPHY |
| N080/N081, original plan pp46–49 | Old QOL instrument form format differences concern a secondary instrument not reported here; later amendments replace AQOL with SF12. | PERIPHERAL_COMPARISON |
| N084, plan background | Historical mortality RR.76 with CI .05–1.05 is background literature, not POLAR outcome or decision-rule input requiring this confidence interval. | PERIPHERAL_COMPARISON |


Counts: 84 relationships COMPLETE; 2 findings; 13 excluded observations. Limitations: unlabelled graph quantiles cannot be mechanically recovered; original power/inflation formulas do not establish every computational detail. All assigned numeric relationships inspected; no scientific coverage gap.


# Numeric consistency review — shard 2

Assigned scope: canonical N085–N140 inclusive, 56 relationships. Status: COMPLETE. Findings: 0. Excluded observations: 15. Sources and reused assets preserved. This artifact extends the mandatory numeric stage; the main numeric reviewer owns the canonical merge.

Read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md; also START_PROMPT.md, tooling record, canonical numeric inventory, plan_002 mapping and the relevant support_003 complete page transcriptions, visual numerical context and appendices. Checked underlying rows, footnotes, population definitions and matching quantitative relationships, rather than numeric inventory summaries alone. Final-plan source text was read directly using Poppler pdftotext -layout for pp70–101 and 108–132; result tables were read in complete mapped source-page transcriptions. Reusable source-matched page images for DOC-003 pp12,16,17,20 were opened to inspect every flow box and crossover direction. Sources remain final authority. No Python, external sources, prior candidate selection or prior reports used.

Integer participant/event counts are exact. Every displayed percentage or continuous input is allowed its half-unit rounding interval at its printed precision. A percentage is compatible when the exact count/denominator proportion intersects that interval. Means/medians and model-based results are not substituted for one another. No qualifying discrepancy remains after source context and exclusions in this scope.


## Findings

None. No F-NUM identifiers assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC002 pp70–71/79/112, N085–N087 | Historical effect, cohort and forest-plot quantities are background rather than POLAR results; historical cross-location differences cannot change a supplied trial result or planned decision rule. | PERIPHERAL_COMPARISON |
| PLAN DOC002 pp75/97, N089 | Up-to2000 mL general cooling instruction includes intubation-specific1000 mL/2000 mL instructions; no conflicting dose required by printed context. | CONTEXT_RESOLVES |
| PLAN DOC002 pp77/99–100, N092 |0.17°C/h,.5°C per 3 h and 24 h33→37°C rewarming reconcile with half-unit intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC002 pp77/97/99, N092 | Injury-versus-randomisation72 h anchor, late-start minimum 48 h, and daily-versus12 h reassessment differ in operational instruction; no changed primary/key-secondary result, analysis size or statistical decision rule established. | PERIPHERAL_COMPARISON |
| PLAN DOC002 pp77/101, N093 | Post-rewarming pads up to 7 days versus 96 h postrandomisation are different operational plan instructions; no reported outcome/analysis-population/decision-rule change follows solely from this plan-internal comparison. REPORT-versus-PLAN randomized-intervention comparison belongs to independent cross-source review. | PERIPHERAL_COMPARISON |
| PLAN DOC002 p83, N095 | Literal 496+2=498 differs from explicitly stated practical 500 recruitment target; inflation/disclosed amendments show intended 500 at once and do not leave target extraction unclear. | CONTEXT_RESOLVES |
| PLAN DOC002 p84, N096 |11 interim tests versus 6 recruitment points counts separate endpoint tests: five points×2 outcomes plus 450 mortality-only=11. | CONTEXT_RESOLVES |
| PLAN DOC002 pp108–132/139–180, N102–N115 | Nested renal/energy/biomarker/TEG/PK definitions, formula wording and evolving operational versions provide no independently conflicting main-trial primary/key-secondary result or applicable statistical decision rule. | PERIPHERAL_COMPARISON |
| REPORT DOC003 p5, N122 | Caption probability-of-death wording alongside Kaplan–Meier survival axis is immediately resolved by the survival plot and mortality-hazard comparison; risk-table counts reflect censoring. | TERMINOLOGY_OR_WORDING |
| REPORT DOC003 pp6/11, N123/N128 |186 baseline hypothermia patients reached 33°C whereas 175 primary-outcome-evaluable patients occupy reached-target groups; populations differ. | CONTEXT_RESOLVES |
| REPORT DOC003 pp8/15/16, N125/N132/N133 | Wrapped very-small P,37–41 h axis label and '<72 hours' flow wording are resolved by local table/sequence/majority 72 h footnote; retain printed values without registration. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC003 pp12–20, N129–N137 | Baseline, outcome, mortality and 72 h/96 h dose subsets have different denominators; each flow reconciles and immediate definitions identify the intended population. | CONTEXT_RESOLVES |
| REPORT DOC003 p18, N135 | Normothermia Marshall V34.7(68)and VI1(2) reverse n(%)order; integer counts 68/2 and percentages 34.7/1 are identifiable at once, and full Marshall total196 reconciles. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC003 p21, N138 | Multiple-imputation133/260 does not need to equal printed pooled 51.1%, nor crude 133/260 versus 121/240 ratio need equal stratified RR1.00; quantities are modeled/pooled and count summaries rounded. | MODEL_VERSUS_CRUDE |
| REPORT DOC003 pp22–23, N139 | Adjusted OR CI stray 275 is a visibly misplaced character sequence;0.95 lies in .55–1.64. Mean-time  P.01 versus median-time  P.02 uses distinct summaries and tests. | NOTATION_OR_TYPOGRAPHY |

## Limitations

No scientific coverage gap in the 56 assigned relationships. Exact eFigure1/4 ordinate values and intervals are not printed; review uses supplied graphic mappings and source-matched visual context without inventing numerical precision. Raw data and masked DSMC allocation key are absent; no reconstruction of patient-level data, clinical audit, or unmasking attempted. Detailed inferential identity, power and interval/test compatibility are independently assigned to statistical specialists; this shard retains every displayed numeric relation and does not claim absent modeling inputs can establish a contradiction.

## Complete relationship status table

| Relationship ID | Status | Exact checked content and numeric reconciliation |
|---|---|---|
| N001 | COMPLETE | 266+245=511;231+280=511;231/511=45.205%. |
| N002 | COMPLETE | 266−16−6−4=240;245−13−5−1=226;240+226=466. |
| N003 | COMPLETE | 266−6=260;245−5=240;260+240=500; mortality follows known vital status. |
| N004 | COMPLETE | 132+161=293. |
| N005 | COMPLETE | Age weighted mean 34.568 rounds within input intervals to 34.5; male abstract discrepancy excluded. |
| N006 | COMPLETE | 35°C induction then 33°C maintenance; stated bleeding exceptions explain 33–35°C. |
| N007 | COMPLETE | 72 h assessment,≤.25°C/h and 7 d limit coherent conditional rules. |
| N008 | COMPLETE | 233/260=89.615%;186/260=71.538%. |
| N009 | COMPLETE | 85/260=32.692%→33%; never33°C narrative comparison excluded. |
| N010 | COMPLETE | Distinct initiation, attainment, maintenance and rewarming times; 22.5 h matches. |
| N011 | COMPLETE | 19% plus further 13% not assigned unreported common denominator; excluded. |
| N012 | COMPLETE | Eligibility cutoffs define population, not competing count totals. |
| N013 | COMPLETE | Countries/dates/interim recruitment points matched; administrative comparisons excluded. |
| N014 | COMPLETE | 1:1 allocation need not yield equal realised totals; blocks and strata do not contradict totals. |
| N015 | COMPLETE | 207/260=79.615%;194/240=80.833%. |
| N016 | COMPLETE | 53/260=20.385%;46/240=19.167%; sex counts exhaust 260/240. |
| N017 | COMPLETE | 35.0 and 34.1 mean/SD labels retained; no unprinted pooled SD reconstructed. |
| N018 | COMPLETE | Median 6 within IQR4–7 and GCS3–15. |
| N019 | COMPLETE | Motor median 3 within IQR1–4/2–5. |
| N020 | COMPLETE | 220/260=84.615%;202/240=84.167%. |
| N021 | COMPLETE | 26/257=10.117%;27/239=11.297%. |
| N022 | COMPLETE | 37/256=14.453%;39/237=16.456%. |
| N023 | COMPLETE | Temperatures refer to 162/143 available scene observations. |
| N024 | COMPLETE | 18/260=6.923%;17/240=7.083%. |
| N025 | COMPLETE | 152/260=58.462%;128/240=53.333%. |
| N026 | COMPLETE | 18/260=6.923%;20/240=8.333%. |
| N027 | COMPLETE | 69/260=26.538%;72/240=30%. |
| N028 | COMPLETE | 3/260=1.154%;3/240=1.25%; Marshall counts sum 260/240. |
| N029 | COMPLETE | Probabilities .46 lie in 0–1; SDs nonnegative. |
| N030 | COMPLETE | Median 20.0 below Q1 20.5 exceeds half-unit display precision; F-NUM-002. |
| N031 | COMPLETE | 84/260=32.308%;89/240=37.083%. |
| N032 | COMPLETE | 29/260=11.154%;18/240=7.5%. |
| N033 | COMPLETE | 20/260=7.692%;20/240=8.333%. |
| N034 | COMPLETE | 28/260=10.769%;37/240=15.417%. |
| N035 | COMPLETE | 24/260=9.231%;16/240=6.667%. |
| N036 | COMPLETE | 60/260=23.077%;54/240=22.5%. |
| N037 | COMPLETE | 15/260=5.769%;6/240=2.5%; cause counts sum 260/240. |
| N038 | COMPLETE | 92/208=44.231%;89/193=46.114%. |
| N039 | COMPLETE | 74/208=35.577%;69/193=35.751%; high ethanol counts nested in positive. |
| N040 | COMPLETE | Medians 1.8/2.0 lie in IQR1.0–2.7/1.1–2.8; pooled median not mean of medians. |
| N041 | COMPLETE | Temperature graph units/median trajectories agree with assigned treatment targets. |
| N042 | COMPLETE | Every contributor count≤260/240; counts need not decrease monotonically. |
| N043 | COMPLETE | ICP graph units/medians agree with narrative; exact quantiles not printed. |
| N044 | COMPLETE | Every ICP contributor count≤260/240; not cumulative follow-up counts. |
| N045 | COMPLETE | Observed unique contributors≤6 observations each; caption distinguishes patients/measurements. |
| N046 | COMPLETE | 2+1=3 episodes; one death not asserted to be an additional event. |
| N047 | COMPLETE | GOSE distribution favourable boundary aligns with117/240 and111/226; death denominator differs. |
| N048 | COMPLETE | GOSE categories1–8 partition favourability1–4/5–8; explicit unreported outcomes retained. |
| N049 | COMPLETE | 500→510 documented blinded attrition review; power method detail belongs statistical checks. |
| N050 | COMPLETE | Historical 1.46 is 46% relative increase; not POLAR estimate. |
| N051 | COMPLETE | Historical figures/background not POLAR participant counts. |
| N052 | COMPLETE | PP/AT definitions use eligibility then cooling compliance; sensitivity uses 72 h rather than 96 h. |
| N053 | COMPLETE | 117/240=48.75%;111/226=49.115%; RR.992568; RD−.365044 pp. |
| N054 | COMPLETE | 52/260=20%;43/239=17.992%; RR1.111628; RD2.008368 pp. |
| N055 | COMPLETE | 54/256=21.094%;44/239=18.410%; RR1.145774; RD2.683708 pp. |
| N056 | COMPLETE | 143/260=55%;123/240=51.25%; RR1.073171; RD3.75 pp. |
| N057 | COMPLETE | Bacteremia RR1.461538, RD2.307692 pp; other infection RR.874494, RD−1.987179 pp. |
| N058 | COMPLETE | Both bleeding count/percentage/RD rows reconcile; RR/CI/P attribution pattern F-NUM-001. |
| N059 | COMPLETE | 66+174=240;68+158=226;22+95=117;27+84=111; RRs.839506/1.026956. |
| N060 | COMPLETE | 69+171=240;71+155=226;22+95=117;28+83=111; RRs.808489/1.037502. |
| N061 | COMPLETE | 70.5−57.1 nominal 13.4; half-unit input intervals permit 13.3; RR1.23 coherent. |
| N062 | COMPLETE | 70.7−54.6=16.1; RR1.294872→1.29. |
| N063 | COMPLETE | 182×2=364;498+2×7 sites=512; run-in explicitly separate. |
| N064 | COMPLETE | 65−50=15 pp;(65/50−1)×100=30%;1/.15=6.6667→NNT7. |
| N065 | COMPLETE | 8+2+2=12%;364/.95=383.158→384;384/.88²=495.868→496 possible dilution inflation; rule not forced. |
| N066 | COMPLETE | Original eligibility repeated consistently; later amendments distinguish final criteria. |
| N067 | COMPLETE | 2000 mL=2 L; 4°C 0.9% saline and 35°C induction coherent. |
| N068 | COMPLETE | Original 33°C 72 h maintenance versus 36.5–37°C control coherently stated in version 1. |
| N069 | COMPLETE | 60 h resumption, 72 h assessment, .25°C/h and 7 d maximum preserve separate time anchors. |
| N070 | COMPLETE | Appendix C placeholder time resolved by immediate withdrawal thresholds; excluded. |
| N071 | COMPLETE | GOSE 5–8/1–4 boundaries coherent; injury/randomisation anchor wording excluded. |
| N072 | COMPLETE | Secondary scale/time point/proportions retained; GOSE survivor denominator distinct from total. |
| N073 | COMPLETE | Two run-in patients per site explicitly excluded from randomized trial population. |
| N074 | COMPLETE | Schedule's conditional 4–7 d cooling aligns with ICP-directed rewarming. |
| N075 | COMPLETE | SAE reporting window distinguishes surveillance from 10 d reported AE analysis; no imputed comparison. |
| N076 | COMPLETE | Shared care thresholds show no arithmetic contradiction; PaO2 unit typography excluded. |
| N077 | COMPLETE | Dose/ranges/intervals are cointerventions; no preferred care audit. |
| N078 | COMPLETE | ICP flowchart doses/thresholds read; no trial-effect extraction contrast. |
| N079 | COMPLETE | GOSE structured levels align with favourable 5–8; GOS 1–5 is a distinct scale. |
| N080 | COMPLETE | AQOL8 has eight four-choice questions; later replacement instrument amended. |
| N081 | COMPLETE | EQ5 D form mobility text/levels differ; secondary original instrument format observation excluded. |
| N082 | COMPLETE | 3 d=72 h; 33°C versus 37°C coherent at summary level. |
| N083 | COMPLETE | Final synopsis target 500 predates August amendment to 510; 35°C→33°C stages retained. |
| N084 | COMPLETE | Historical favourable 52%+unfavourable 48%=100%; background trial sample sizes separate. |
| N085 | COMPLETE | PLAN p70 historical ATBIS363/16, SAFE318, RSI150 and their follow-up percentages distinguished from POLAR; outcomes/time windows differ and historical arithmetic does not determine trial extraction. |
| N086 | COMPLETE | PLAN pp70–71,79,112 historical RR/CI/P and cooling-duration rationale read with historical attribution; not POLAR results. |
| N087 | COMPLETE | PLAN p71 background forest-plot six study counts; denominators sum354/340 and events179/132; random-effects pooled1.46 distinguished from crude pooled risk ratio. |
| N088 | COMPLETE | PLAN pp73–74,91–93 complete eligibility thresholds; ≥18/<60, GCS<9,3 h injury window versus2.5 h transport window are different quantities; SBP90/HR120 criteria matched. |
| N089 | COMPLETE | PLAN pp75–76,91/93/97 initial35°C, saline4°C/0.9%,100 mL/min,1000 mL after versus2000 mL before intubation; general up-to2000 mL instruction includes both specific doses. |
| N090 | COMPLETE | PLAN p77 and cooling appendix targets33°C/32.5–33.5°C and37±0.5°C/36.5–37.5°C reconcile; >38°C fever trigger is distinct from maintenance target. |
| N091 | COMPLETE | PLAN pp76–77/92 withholding/restarting within48 h,35–37°C bleeding management, permanent cessation with retained follow-up distinguished from withdrawal of consent. |
| N092 | COMPLETE | PLAN pp77/97/99–10172 h timing, late-start minimum 48 h, ICP20 gate, >5 min sustained rises, daily/12 h assessment and0.17°C/h/.5°C per 3 h; .5/3=.166667, inside .17 interval [.165,.175).33→37 over24 h reconciles. |
| N093 | COMPLETE | PLAN pp77/101 post-rewarming pads7 d versus 96 h statements read separately from maximum hypothermia7 d; purely operational plan comparison excluded below. |
| N094 | COMPLETE | PLAN p78/p96 run-in4 at lead site,2 at other sites,1:1 block randomisation,4×2 stratification levels and control rescue35°C; no fabricated total run-in count from sites. |
| N095 | COMPLETE | PLAN p83 full power/attrition inputs:364=182×2;65−50=15 percentage points;65/50−1=30%;1/.15=6.667→NNT7;8+2+2=12% assumed withdrawal;364/.95=383.158→384. Nonadherence dilution versus simple lost observations distinguished; practical 500 target stated explicitly. |
| N096 | COMPLETE | PLAN p84 amended366 evaluable,82.3% power and11 interim outcome tests versus 6 recruitment points; ten mortality/neurological plus one mortality-only test account for11; original/amended power assumptions not treated as observed counts. |
| N097 | COMPLETE | PLAN pp85–86 monitoring125/250/300/350/400/450; six-month outcomes except28-day450 mortality; commencement through7 d postcessation SAE window and 24 h reporting delay distinct. |
| N098 | COMPLETE | PLAN pp89–90 entire event schedule and p81 follow-up; assessment-day7/day8–14, survival discharge/6 mo, GOSE and QOL6 mo, ICP-dependent cooling continuation distinguished. |
| N099 | COMPLETE | PLAN pp94–98 all physiology, nutrition, sedation ranges and units read;70%predicted feed not a treatment allocation percentage; propofol temperature/time safety conditions distinguished. |
| N100 | COMPLETE | PLAN pp103–105 full mapped instrument values: GOSE1–8 and GOS1–5, home8 h/work/social/relationship thresholds, missingness labels; favorable GOSE5–8 versus1–4 partition correct. |
| N101 | COMPLETE | PLAN pp106–107 full mapped EQ5 D three-level dimensions/VAS0–100 and SF12 response levels/four-week recall; prospective scale definitions without reported aggregate results. |
| N102 | COMPLETE | PLAN p108500=250×2, main acute kidney sub-study7 d initial/10 d extended creatinine and10 d outcome horizon; no main clinical result depends on replacing these horizons. |
| N103 | COMPLETE | PLAN pp109–110 first50, four sampling occasions0/24/48/72 h after first sample, two urine/plasma samples per occasion; no observed biomarker counts supplied. |
| N104 | COMPLETE | PLAN pp114–11840=20×2,16/.8=20,400/2000=20%,400 SD/400 difference=1 SD; measurement30 min and5 min steady-state/discard windows coherent; no main-trial energy outcome printed. |
| N105 | COMPLETE | PLAN pp119–12080=40+40,10 mL daily5 days,2000 g/−70°C, six-month GOSE, r.4542 versus rounded.45; prospective sub-study distinct from reported trial outcomes. |
| N106 | COMPLETE | PLAN pp122–12620+20=40,33/37°C paired samples48–72 h, second120±12 h;360µL=.36 mL,1/.5/3 mL assay aliquots and10 mL arterial discard distinguished. |
| N107 | COMPLETE | PLAN pp128–13210-person paired PK,34–35°C versus36.5–38°C,0–200 mg/h,60/30 min windows,0/5/10/15/30/60 min samples and12 mL per occasion; clearance units mg/h÷mg/L=L/h. Prospective extrapolation wording does not identify a reported main-trial result. |
| N108 | COMPLETE | PLAN p131 schematic log concentration10^-3–10^1 versus time−20–80 min and stop0; illustrative sampling curve not trial data. |
| N109 | COMPLETE | PLAN pp139–140 V1→V2 mapped tracked changes:2.5 h,48 h,2 L,35–37/36.5–37.5°C, run-in6, renal21 d and biomarker12/24/48/72 h; chronology retained. |
| N110 | COMPLETE | PLAN pp141–142 mapped targets ICP<20/CPP>60 and rescue≥35°C; prospective clinical thresholds read in their distinct intervention branches. |
| N111 | COMPLETE | PLAN pp144–153 mapped tracked sample-size512→500, pilot6→4,498→500,0.3→0.7%,1000/2000 mL,4×2 strata; disclosed revisions distinguished from simultaneous specifications. |
| N112 | COMPLETE | PLAN pp156–157 disclosed2.5→3 h eligibility-window amendment and10% rationale; not an observed result denominator. |
| N113 | COMPLETE | PLAN pp158–162 mapped rescue35°C/sedation34/>36.5°C/fluid500 mL guidance; co-management thresholds and chronological amendments not replaced by main-result counts. |
| N114 | COMPLETE | PLAN pp163–170 full TEG mapped methods corroborate20+20,48–72 h,120±12 h,33/37°C and assay units; no main-trial effect estimate supplied. |
| N115 | COMPLETE | PLAN pp174–180 entire amended ITT/monitoring and recruitment-letter content checked:500→510,496 recruited,2.5% versus2% consent/7% versus5%loss; no claim that interim percentages are final realized counts. |
| N116 | COMPLETE | PLAN pp183–187 complete mapped SAP text/templates;511 and X/XX/XXX are placeholder flows, deaths48–96 h explicitly added; no arithmetic performed on unspecified subgroup counts. |
| N117 | COMPLETE | PLAN pp189–190 all8 GOSE rows/means/percentages/aggregate rows and block arrays checked. X sum140, Y133, total273; unfavorable63/69, survivors36/42; mean4.392857/4.075188 rounds4.39/4.08. Twelve mortality blocks sum27/27 and denominator140/133; unfavorable blocks sum63/69. |
| N118 | COMPLETE | PLAN pp191–192 all8 GOSE rows/means/percentages/aggregates and14 block arrays checked. X168, Y153, total321=350−7−22; survival341=321+20; unfavorable82/80, favorable86/73, unfavorable survivors48/48; means4.267857/4.098039→4.27/4.10. Mortality blocks deaths34/32; survival denominator181/160, total341. |
| N119 | COMPLETE | PLAN pp193–194 all8 GOSE rows/means/percentages/aggregates and16 block arrays checked. X184, Y180, total364=400−8−28; survival390=364+26. Unfavorable89/91, favorable95/89, survivors53/56; means4.288043/4.183333→4.3/4.2. Mortality36/35 and denominators200/190, total390; favorable-block denominators184/180 and events95/89. |
| N120 | COMPLETE | REPORT p3 entire eligibility table thresholds and differences between prehospital/ED exclusion branches;3 h randomisation/2.5 h transport windows distinct. |
| N121 | COMPLETE | REPORT p4 all nine rewarming-bin graph positions and mapped95%CI/mixed-model caption; no exact graphical ordinates fabricated. |
| N122 | COMPLETE | REPORT p5 complete risk rows260/240→206/196→202/195→200/195→91/88→23/17; late numbers account for follow-up/censoring and are not denominators for a fixed180 day risk; HR distinguished from crude RR. |
| N123 | COMPLETE | REPORT p6 every eTable2 cell:123+137=260,101+139=240; percentages47.3/52.7,42.1/57.9;233/260 = 89.615→89.6%,186/260 = 71.538→71.5%; all four medians/IQR and units read. |
| N124 | COMPLETE | REPORT p7 every eTable3 count/percent/definition:9+51+35+1+3=99;99/260 = 38.077→38.1%; each reason percentage reconciles;23/240 = 9.583→9.6%. Withdrawal first96 h and>1 h control mild cooling differ from later dose-defined subsets. |
| N125 | COMPLETE | REPORT p8 every eTable4 process count/percentage, median/IQR, unit and footnote checked:205/260 = 78.8%,192/240 = 80%; therapy/neurosurgical/fluid counts use260/240 and percentages reconcile. All medians lie within IQR; individual-patient ICP/CPP index medians cannot be computed from separate duration medians. Procedures may overlap. |
| N126 | COMPLETE | REPORT p9 all eTable5 rows/units:8.3/6.9,11.9/11.4,19.8/18.8 medians within IQR; GOSE available240/226, mean4.2(SD2.2)both; survivors240−54=186,226−44=182 give69/186 = 37.1%,71/182 = 39.0%. |
| N127 | COMPLETE | REPORT p10 every eTable6 count/percentage/footnote: all cardiovascular, infection, bleeding rows reconcile to260/240; ICP explicitly43/260 = 16.5%,43/239 = 18.0%; unavailable induction/maintenance control cells are NA, not0. |
| N128 | COMPLETE | REPORT p11 all eTable7 counts/percentages/limits:49+67+59+65=240;18+28+32+39=117;18/49 = 36.7%,28/67 = 41.8%,32/59 = 54.2%,39/65 = 60.0%; all points contained in ordered CI.175 evaluable reached 33°C versus186 in larger baseline population is not same set. |
| N129 | COMPLETE | REPORT p12 visual each eFigure3 box:266−6−14−29=217;245−5−10−29=201;217−50−35−8=124;201−4−35−1−1−9=151; pre-outcome132/161 agreeeTable8; all exclusion subcounts sum. |
| N130 | COMPLETE | REPORT p13 every eTable8 baseline cell/footnote: sex107+25=132,132+29=161; Marshall2+72+14+44+0=132,2+84+15+58+2=161; cause43+14+12+15+13+28+7=132,59+12+14+28+10+34+4=161; all n/N percentages and means/medians intervals checked. |
| N131 | COMPLETE | REPORT p14 every eTable9 numerator/denominator/percentage/RR:58/124 = 46.8%,69/151 = 45.7%, crude RR1.0236→1.02; hospital/six-month deaths132/160 distinguish from baseline132/161; all infection/bleeding rates reconcile. Hematoma41+83=124,54+97=151/events12+46=58,20+49=69; mass56+95=151/events21+48=69. Other printed crude RRs agree two-decimal precision. |
| N132 | COMPLETE | REPORT p15 complete mapped17 temperature positions and intervals;37–41 label in consecutive6 h sequence is readily identified typography; no exact values inferred. |
| N133 | COMPLETE | REPORT p16 visual every sensitivity-flow box:217−50−39−8=120;39=35 survivors+4 deaths; N151 retained;55/120 = 45.8%,69/151 = 45.7%, RR1.0030→1.00; majority 72 h definition supplied in immediate footnote. |
| N134 | COMPLETE | REPORT p17 visual each eFigure6 box:217−50−35+1−8=125;201−4−35−1+35−1−11=184; baseline133/196 agreeeTable10; crossovers directions retained;35=30 survivors+5 deaths. |
| N135 | COMPLETE | REPORT p18 every eTable10 baseline cell/footnote: sex108+25=133,158+38=196; Marshall H2+73+14+44+0=133; N3+108+15+68+2=196 with visibly transposed V/VI n(%)cells; causes43+14+12+15+13+29+7=133 and70+18+16+31+13+43+5=196; all remaining percentages and continuous intervals checked. |
| N136 | COMPLETE | REPORT p19 every eTable11 outcome/subgroup cell:59/125 = 47.2%,82/184 = 44.6%, RR1.0591→1.06; all hospital/6 mo/infection/bleeding percentages/RR agree. Hematoma41+84=125,64+120=184, event12+47=59,23+59=82; mass41+84=125,66+118=184, event12+47=59,24+58=82. |
| N137 | COMPLETE | REPORT p20 visual each eFigure7 box:217−50−39+1−8=121;201−4−35−1+39−1−11=188;56/121 = 46.3%,85/188 = 45.2%, RR1.0236→1.02. Different dose window accounts for altered crossovers. |
| N138 | COMPLETE | REPORT p21 every eTable12 scenario cell:20+14=34;34/500 = 6.8%,20/260 = 7.7%,14/240 = 5.8%; worst117/260 versus(111+14)/240125/240, RR.8640→.86, RD−7.083→−7.1; best(117+20)/260137/260 versus111/240, RR1.1393→1.14, RD6.442→6.4; MI pooled counts/risks/stratified estimates kept separate from crude arithmetic; all displayed estimate containment/order checked. |
| N139 | COMPLETE | REPORT pp22–23 every posthoc result and eTable13 baseline cell:58/124 = 46.8%,111/226 = 49.1%, crude OR(58×115)/(66×111)=.910456→.91; means2.00−1.73=.27 h=16.2 min supports16 min. Mean versus median time comparisons distinct. Sex100+24=124,180+46=226; Marshall2+67+14+41+0=124,14+121+20+68+3=226; causes41+14+11+14+12+25+7=124 and82+17+20+35+16+50+6=226; all n/N percentages, units, continuous intervals checked. |
| N140 | COMPLETE | REPORT DOC004 p1 administrative data-sharing24 Oct2021; no applicable trial numerical result or denominator; explicitly reviewed. |

