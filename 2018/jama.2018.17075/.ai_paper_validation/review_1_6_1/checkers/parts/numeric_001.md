# Numeric consistency review — shard 1

Scope: N001–N084, 84 relationships. REPORT: main article PDF pp.1–8. PLAN: original protocol and final opening PDF pp.13–49,68–69. Full main and plan_001 maps read; source relationships checked with direct Poppler pdftotext -layout and source-matched rendered main p7. Engine: direct Poppler (tooling record); reused images retained unchanged. No old checker, ledger or report scientific input; no web. Every assigned relationship reviewed, including all components in grouped rows. Counts printed as participant/event integers retain their exact integer value; continuous displayed inputs retain their half-unit rounding intervals. No invented graph ordinates, unreported covariates, or analysis denominators.

## Findings

### F-NUM-001

**Relationship:** N058; statistical cross-reference S010/S011.  
**Locations and roles:** REPORT [main article PDF p3, Statistical Analysis](../../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [main article PDF p7, Table2, both bleeding rows](../../../../jama_cooper_2018_oi_180132.pdf#page=7). Main p7 table was confirmed visually against the supplied PDF-matched page image and direct layout extraction.  
**Printed inputs:** New/increased intracranial bleeding:47/260(18.1%) versus 37/240(15.4%), absolute difference 2.7(−3.9 to 9.2)pp, relative risk 1.23(0.43–3.5), P=.70. New significant extracranial bleeding:8/260(3.1%) versus 6/240(2.5%), difference 0.6(−2.3 to 3.5)pp, relative risk 1.17(0.79–1.74), P=.43. Methods specify unadjusted χ² comparisons and relative risks for these adverse events.  
**Rule and calculation:** For each unadjusted H-versus-C risk ratio, RR=(H events/H denominator)/(C events/C denominator). Intracranial RR=(47/260)/(37/240)=1.172557; extracranial RR=(8/260)/(6/240)=1.230769. These do not lie in the respective printed RR rounding intervals [1.225,1.235) and[1.165,1.175). Exact integer count inputs leave no rounding ambiguity. Even treating the intracranial printed percentages as half-unit intervals yields RR  in [18.05/15.45,18.15/15.35]=[1.1683,1.1824], disjoint from printed 1.23. Each displayed RR corresponds numerically to the other bleeding outcome's counts. CI widths and P values also travel with the opposite point-estimate pattern, but the inconsistency is established by the exact RR identity alone.  
**Focus area:** A/C, counts to unadjusted effect-measure identity.  
**Proposed review domain:** statistical_results.  
**Proposed relationship type:** S_W; all relationships S_W.  
**Affected result or extracted value:** The unadjusted relative risk and associated 95% CI/P attributed to each of new/increased intracranial bleeding and significant extracranial bleeding. Intracranial bleeding is reported in the abstract; selecting the printed 1.23(0.43–3.5) rather than the count-compatible 1.17 changes its extracted effect and precision.  
**Why context does not resolve it:** The row labels assign two complete inferential packages to distinct outcomes while the row counts and differences remain in the opposite alignment. The table contains no note authorizing reassignment. Computing the risk ratios detects the conflict, but a reader cannot treat the complete printed CI/P attribution as established solely by identifying a likely transposition. The methods do not offer an adjusted-model explanation.  
**Alternatives:** A transposition of the RR/CI/P cells between the two rows explains the point-estimate pattern; a separately unreported analysis producing these numbers would conflict with the stated unadjusted methods. These are possible explanations, not assumed facts.  
**Human question:** Which RR, 95% CI and P value should be attributed to each bleeding outcome, given the printed counts and stated unadjusted analysis?

### F-NUM-002

**Relationship:** N030.  
**Location and role:** REPORT [main article PDF p5 Table1, Injury Severity Score row, normothermia column](../../../../jama_cooper_2018_oi_180132.pdf#page=5). Direct layout extraction and source-matched page image agree.  
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
| N005, main p1 versus p5 Table1 | Abstract 402 men conflicts with207+194=401;80.2% of 500=401 and both group percentages identify the intended baseline count at once. | CONTEXT_RESOLVES |
| N053, main p1 versus pp5/7 | Abstract RD 0.4% lacks minus;117/240<111/226, RR.99, and both narrative/Table2−0.4 identify direction at once. | NOTATION_OR_TYPOGRAPHY |
| N009/N011, main pp4/8 | 27% never 33°C versus19% withdrawn early plus further 13%; denominators/nesting are not established as a common exclusive partition and exposure summaries do not alter primary denominators. | CONDITIONAL_OR_UNREPORTED |
| N042/N044, main p6 Figure2 | Contributor counts sometimes increase between intervals; caption defines unique observed contributors in each interval, not cumulative survivors. | CONTEXT_RESOLVES |
| N047/N071, main pp3/7 and original plan pp15/25 | Injury versus randomisation six-month wording uses adjacent clinical follow-up anchors separated by the ≤3 h recruitment window, with the endpoint clearly identified. | TERMINOLOGY_OR_WORDING |
| N061, main p6 | Display 70.5%−57.1%=13.4pp versus RD13.3; input intervals [70.45,70.55),[57.05,57.15) permit differences in [13.30,13.50), overlapping RDroundinginterval[13.25,13.35). | ROUNDING_OR_DISPLAY_PRECISION |
| N063/N065, plan p27 | Linear 12% attrition division alone would not produce 496, but 384/.88²=495.87 fits treatment-dilution inflation; the exact inflation formula is unprinted. | CONDITIONAL_OR_UNREPORTED |
| N066/N068/N083, original versus final protocol and main | Changed eligibility, target and temperature details are versioned/amended plans, not simultaneous final specifications; final target 510 amendment resolves 500 synopsis. | CONTEXT_RESOLVES |
| N070, plan p35 Appendix C | Initial bleeding screen placeholder time is clarified by explicit insertion/first-hour thresholds immediately in withdrawal text and original§12.4. | CONTEXT_RESOLVES |
| N075, plan pp26/29 versus main p3 | SAE reporting through 7 days after cessation and AE analysis within 10 days are separate surveillance/analysis definitions; no incompatible matched event count supplied. | CONTEXT_RESOLVES |
| N076, plan p36 | Pa O2 m Hg is an obvious unit-character omission alongside other mm Hg thresholds. | NOTATION_OR_TYPOGRAPHY |
| N080/N081, original plan pp46–49 | Old QOL instrument form format differences concern a secondary instrument not reported here; later amendments replace AQOL with SF12. | PERIPHERAL_COMPARISON |
| N084, plan background | Historical mortality RR.76with CI .05–1.05 is background literature, not POLAR outcome or decision-rule input requiring this confidence interval. | PERIPHERAL_COMPARISON |

## Relationship completion

| Relationship ID | Status | Check result |
|---|---|---|
| N001 | COMPLETE | 266+245=511;231+280=511;231/511=45.205%. |
| N002 | COMPLETE | 266−16−6−4=240;245−13−5−1=226;240+226=466. |
| N003 | COMPLETE | 266−6=260;245−5=240;260+240=500; mortality follows known vital status. |
| N004 | COMPLETE | 132+161=293. |
| N005 | COMPLETE | Age weighted mean 34.568 rounds within input intervals to 34.5; male abstract discrepancy excluded. |
| N006 | COMPLETE | 35°C induction then 33°C maintenance; stated bleeding exceptions explain 33–35°C. |
| N007 | COMPLETE | 72h assessment,≤.25°C/h and 7 d limit coherent conditional rules. |
| N008 | COMPLETE | 233/260=89.615%;186/260=71.538%. |
| N009 | COMPLETE | 85/260=32.692%→33%; never33°C narrative comparison excluded. |
| N010 | COMPLETE | Distinct initiation, attainment, maintenance and rewarming times;22.5h matches. |
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
| N053 | COMPLETE | 117/240=48.75%;111/226=49.115%; RR.992568; RD−.365044pp. |
| N054 | COMPLETE | 52/260=20%;43/239=17.992%; RR1.111628; RD2.008368pp. |
| N055 | COMPLETE | 54/256=21.094%;44/239=18.410%; RR1.145774; RD2.683708pp. |
| N056 | COMPLETE | 143/260=55%;123/240=51.25%; RR1.073171; RD3.75pp. |
| N057 | COMPLETE | Bacteremia RR1.461538, RD2.307692pp; other infection RR.874494, RD−1.987179pp. |
| N058 | COMPLETE | Both bleeding count/percentage/RD rows reconcile; RR/CI/P attribution pattern F-NUM-001. |
| N059 | COMPLETE | 66+174=240;68+158=226;22+95=117;27+84=111; RRs.839506/1.026956. |
| N060 | COMPLETE | 69+171=240;71+155=226;22+95=117;28+83=111; RRs.808489/1.037502. |
| N061 | COMPLETE | 70.5−57.1 nominal 13.4; half-unit input intervals permit 13.3; RR1.23 coherent. |
| N062 | COMPLETE | 70.7−54.6=16.1; RR1.294872→1.29. |
| N063 | COMPLETE | 182×2=364;498+2×7 sites=512; run-in explicitly separate. |
| N064 | COMPLETE | 65−50=15pp;(65/50−1)×100=30%;1/.15=6.6667→NNT7. |
| N065 | COMPLETE | 8+2+2=12%;364/.95=383.158→384;384/.88²=495.868→496 possible dilution inflation; rule not forced. |
| N066 | COMPLETE | Original eligibility repeated consistently; later amendments distinguish final criteria. |
| N067 | COMPLETE | 2000 m L=2 L; 4°C 0.9% saline and 35°C induction coherent. |
| N068 | COMPLETE | Original 33°C 72 h maintenance versus 36.5–37°C control coherently stated in version 1. |
| N069 | COMPLETE | 60 h resumption, 72 h assessment, .25°C/h and 7 d maximum preserve separate time anchors. |
| N070 | COMPLETE | Appendix C placeholder time resolved by immediate withdrawal thresholds; excluded. |
| N071 | COMPLETE | GOSE 5–8/1–4 boundaries coherent; injury/randomisation anchor wording excluded. |
| N072 | COMPLETE | Secondary scale/time point/proportions retained; GOSE survivor denominator distinct from total. |
| N073 | COMPLETE | Two run-in patients per site explicitly excluded from randomized trial population. |
| N074 | COMPLETE | Schedule's conditional 4–7 d cooling aligns with ICP-directed rewarming. |
| N075 | COMPLETE | SAE reporting window distinguishes surveillance from 10 d reported AE analysis; no imputed comparison. |
| N076 | COMPLETE | Shared care thresholds show no arithmetic contradiction; Pa O2 unit typography excluded. |
| N077 | COMPLETE | Dose/ranges/intervals are cointerventions; no preferred care audit. |
| N078 | COMPLETE | ICP flowchart doses/thresholds read; no trial-effect extraction contrast. |
| N079 | COMPLETE | GOSE structured levels align with favourable 5–8; GOS 1–5 is a distinct scale. |
| N080 | COMPLETE | AQOL8 has eight four-choice questions; later replacement instrument amended. |
| N081 | COMPLETE | EQ5D form mobility text/levels differ; secondary original instrument format observation excluded. |
| N082 | COMPLETE | 3 d=72 h; 33°C versus 37°C coherent at summary level. |
| N083 | COMPLETE | Final synopsis target 500 predates August amendment to 510; 35°C→33°C stages retained. |
| N084 | COMPLETE | Historical favourable 52%+unfavourable 48%=100%; background trial sample sizes separate. |

Counts: 84 relationships COMPLETE; 2 findings; 13 excluded observations. Limitations: unlabelled graph quantiles cannot be mechanically recovered; original power/inflation formulas do not establish every computational detail. All assigned numeric relationships inspected; no scientific coverage gap.

