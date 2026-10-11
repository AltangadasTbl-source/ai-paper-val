# Statistical pass 1 checker: tables B and plan methods

- Fresh shard: /root/stat1_tables_b_plan, gpt-6.1-sol/high, FRESH_SPAWN.
- Exact scope: DOC-006 eTables8–13, physical pp45–53; DOC-003 protocol pp1–82 statistical method, sample-size, power, adaptive/interim/stopping and historical inferential facts; DOC-004 parent SAP pp1–40 corresponding methods and numerical rules.
- Relationship inventory: statistics/parts/tables_b_plan.md; 120 records S5001–S5120, all PASS_1_COMPLETE.
- Findings: 6, F-ST1-501–F-ST1-506. Excluded observations:15 consolidated rows. No scientific gap.
- Direct-source authority and source-matched images used; no prior conclusions, web, unsupplied Python, raw-data audit or preferred analysis. Source and reused artifacts preserved. Main-report methods, DOC-005 and other results are disjoint fresh-agent assignments.

### F-ST1-501

**Title:** Two historical SELECT 95% intervals include the null boundary while their P values are significant.

**Locations and roles:** [DOC-003 protocol p13](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=13), PLAN, functional-independence and ordinal-shift sentences in the historical SELECT rationale. Direct native/layout and freshly rendered page13 confirm both readings.

**Printed values:** Functional independence EVT30% versusMM13%, adjusted OR2.92, 95%CI1.00–7.91, P=.041. Ordinal shift adjusted OR2.01, 95%CI1.00–4.03, P=.049. Both described as benefit/significant shift.

**Rule and calculation:** Ratio null=1. Each closed printed95%CI contains1 at its lower endpoint; both P values are below.05. Point estimates are contained and endpoints ordered; the issue concerns CI-versus-test significance. At displayed precision, 1.00 means [.995,1.005), and an unrounded lower bound above1 is possible, but routeA category1 expressly exempts this comparison from the display-precision screen. No Wald, model covariance, degrees of freedom or test sidedness is inferred. This is one repeated printed-boundary pattern, not two findings.

**Focus area:** B.
**Proposed review domain:** plan_material.
**Proposed relationship type / all relationships:** P_P / P_P.
**Qualifying route:** Route A, category1.
**Affected result or extracted value:** The supplied protocol's historical SELECT functional-independence OR2.92 and ordinal OR2.01 with their95%CIs/P values.
**Why context does not resolve it:** Category1 requires registration of a printed interval-versus-test conflict. The historical source status does not remove an always-register observation under the stated scope rule.
**Alternatives and missing definitions:** Rounding an unprinted lower bound just above1, or calculating CI andP by different methods, could explain the display. Underlying interval endpoints and exact test/CI methods are not supplied in this historical paragraph.
**Classification ambiguity:** This is PLAN historical rationale, not an observed SELECT2 result or direct prospective analysis input. The strict routeA requirement overrides peripheral exclusion; plan_material/P_P is the content-based provisional classification for independent screen/recheck.
**Human question:** What unrounded95%CI limits and tests accompany the two historical SELECT ORs, and how should their printed lower bound1.00 be interpreted alongside P=.041/.049?
**S records:** S5104,S5105.
**Status:** Pending Human Adjudication.

### F-ST1-502

**Title:** The dated protocol assigns primary and secondary status to the same90-day functional-independence endpoint.

**Locations and roles:** [DOC-003 p8 synopsis](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=8), PLAN; [DOC-003 p37 outcome section](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN; [DOC-003 p50 secondary analysis](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=50), PLAN. DOC-004 [p13](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=13)/[p17](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=17) corroborate secondary status but do not create an additional relationship.

**Printed statements:** p8 calls mRS0–2 the second primary outcome. p37 states primary outcome#1=mRS distribution and primary outcome#2=percentage with good outcome(mRS0–2) at90days, then reiterates retaining the dichotomized second primary outcome. p50 calls proportion withmRS0–2 atday90 “Our secondary endpoint.”

**Rule and calculation:** Match endpoint, time point, randomized treatment contrast and population. All locations address the same90-daymRS0–2 functional independence; status is primary versus secondary in the same protocol dated4August2021. This is a hierarchy distinction, not a numerical-rounding comparison. No distinct outcome or population explains it.

**Focus area:** D.
**Proposed review domain:** plan_material.
**Proposed relationship type / all relationships:** P_P / P_P.
**Qualifying route:** Route A, category5.
**Affected result or extracted value:** Planned status of the90-day functional-independence result and the interpretation/extraction of the outcome hierarchy.
**Why context does not resolve it:** Category5 expressly includes outcome-status changes. Repeated explicit second-primary wording and explicit secondary analysis wording cannot both assign one stable hierarchy.
**Alternatives and missing definitions:** The synopsis/outcome section might retain an earlier hierarchy while the statistical section reflects an amendment. This bundle supplies no amendment describing that hierarchy change. The later SAP's secondary status is retained as context rather than used to suppress the internal protocol observation.
**Human question:** Which outcome hierarchy applied to90-daymRS0–2, and where is any amendment reconciling the second-primary and secondary statements documented?
**S record:** S5068.
**Status:** Pending Human Adjudication.

### F-ST1-503

**Title:** Identical adaptive-design scenario4 inputs accompany different fixed-design powers in the supplied plans.

**Locations and roles:** [DOC-003 p49 Table3 scenario#4](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49), PLAN; [DOC-004 p11 operating-characteristics table scenario#4](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=11), PLAN. Direct protocol layout and source-matched SAP image confirm21.2% and51.2%.

**Printed values:** Both rows give group standardized effects(.4,.4,.4,.4,−.1,−.1), average.1, adaptive averageN502/power78.5%, fixedN560. Protocol fixed power21.2%; SAP fixed power51.2%. Each surrounding description uses5000 simulated trials and group proportions14%,6%,14%,6%,42%,18%.

**Rule and calculation:** Matching scenario, effect vector, group frequencies, sample size and displayed operating-characteristic fields establishes copies of one scenario. Weighted effect=.4*(.14+.06+.14+.06)−.1*(.42+.18)=.10. Printed power intervals are[21.15,21.25)% and[51.15,51.25)%; gap29.90percentage points; relative discrepancy29.90/21.2=1.410377>.05. Other corresponding row values match. No theoretical power approximation substitutes for the supplied simulations.

**Focus area:** D (primary-design sample-size/power basis).
**Proposed review domain:** plan_material.
**Proposed relationship type / all relationships:** P_P / P_P.
**Qualifying route:** Route B.
**Affected result or extracted value:** Scenario4 fixed-design power used to describe the operating characteristics and power advantage motivating the adaptive560-patient primary design.
**Why context does not resolve it:** The same printed assumptions and adjacent adaptive results accompany two materially different fixed powers, without a changed simulation definition. A data extractor cannot reproduce or identify one common operating-characteristic value from these matched rows alone.
**Alternatives and missing definitions:** The later SAP may reflect a recalculated simulation or revised fixed-test implementation. No changed computation, seed or method is described for this row. This asks about supplied numerical assumptions, without a preferred design.
**Human question:** Which fixed-design scenario4 power applies under the displayed assumptions, and what changed simulation or reporting detail explains21.2% versus51.2%?
**S record:** S5080.
**Status:** Pending Human Adjudication.

### F-ST1-504

**Title:** The printed efficacy alternative directs the Rankin-score comparison toward medical management.

**Locations and roles:** [DOC-003 p80 rank/statistic/stopping definition](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=80), PLAN; [DOC-003 p81 hypothesis/variable definitions](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=81), PLAN; [DOC-003 p37 score interpretation](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN; corresponding [DOC-004 p39](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=39)/[p40](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=40), PLAN. Formula images directly read. All repeated locations form one direction issue.

**Printed statements and values:** Y is MM Rankin score; X is EVT Rankin score. H0:P(Y≤X)=1/2; HA:P(Y≤X)=1/2+theta. theta=(z_(1−alpha)+z_(1−beta))/sqrt(3N)=.0791, withN560,alpha.025,power.9. EVT-rank sum standardized as Z=[W_EVT−n_EVT*(N+1)/2]/sqrt[n_EVT*n_MM*(N+1)/12]; efficacy ifZ≥2.604(interim) orZ≥2.772(final), declared EVT efficacy. The clinical outcome section describes lowermRS categories as improved functional outcome.

**Rule and calculation:** Computedtheta=(1.959964+1.281552)/sqrt(1680)=.07908489, matching printed.0791. The literal alternativeP(MMscore≤EVTscore)=.5791 makes a lower/better MM score more probable, while the stated claim is EVT benefit. A direction-only illustrative probe, not patient data: an EVTscore0 andMMscore6 pair is favorable toEVT but givesY≤X=false, so moves this probability downward. Ascending numeric ranks would likewise give lowerrank sums/Z for EVT benefit; ranking convention is not supplied, so this rank-sign observation is subsidiary to the explicit probability orientation. No tie correction is assumed.

**Focus area:** B,D.
**Proposed review domain:** plan_material.
**Proposed relationship type / all relationships:** P_P / P_P.
**Qualifying route:** Route A, category2.
**Affected result or extracted value:** Direction of the prespecified adaptive efficacy hypothesis and boundary decision used to claim EVT benefit.
**Why context does not resolve it:** A reversed comparison/reference-group definition changes the direction tested. The explicit Y=MM/X=EVT alternative and efficacy claim do not identify one compatible direction at once.
**Display precision:** theta's own rounding interval[.07905,.07915) remains positive; orientation comparison is logical, with no rounding adjustment that reverses it.
**Alternatives and missing definitions:** X/Y might be interchanged in the printed variable definitions, or the probability inequality might be reversed. Reverse ranks could explain theZ sign but do not by themselves reconcile the explicit clinical-score probability. The actual implementation's orientation, ranking and tie definitions are absent.
**Human question:** What variable order, probability direction and ranking convention were used for EVT efficacy, and how do they reconcile the printedP(Y≤X)=.5+theta withY=MM/X=EVT?
**S record:** S5093.
**Status:** Pending Human Adjudication.

### F-ST1-505

**Title:** The parent SAP describes efficacy stopping at300 using a schedule of200/380 while stating that no additional interim analysis was incorporated.

**Locations and roles:** [DOC-004 p9 planned interim schedule](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=9), PLAN; [DOC-004 p11 sample-size/interim assumptions](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=11), PLAN; [DOC-004 p12 section7.5 actual stopping chronology](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=12), PLAN; [DOC-004 p40 boundaries](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=40), PLAN. Source-matched page12 directly inspected.

**Printed statements:** Prespecified interims follow200 and380 completed90-day patients. At the requested300-patient review, the steering committee decided to provide data “without making any alteration to the study design or incorporating any additional interim analyses.” The same section states that the DSMB applied prespecified interim boundaries after examination of300 completed90-day patients and recommended stopping because efficacy was crossed; the committee stopped recruitment and made a null-hypothesis rejection at family-wise TypeI error rate.05.

**Rule and logical reproduction:** An efficacy-boundary decision based on300 completed outcomes is an inferential look at300;300 is distinct from both scheduled200/380. The supplied boundary appendix conditions its design on200/380/560 and supplies no300-stage calibration or mapping. Both an unchanged/no-additional-analysis statement and a boundary-triggered300 efficacy decision are expressly printed. The chronology is disclosed; the observation is not based on the absence of disclosure.

**Focus area:** C,D.
**Proposed review domain:** plan_material.
**Proposed relationship type / all relationships:** P_P / P_P.
**Qualifying route:** Route B.
**Affected result or extracted value:** The parent SELECT2 efficacy-stopping conclusion and its stated prespecified/family-wise inferential rule, which underlies this supplied secondary-analysis package.
**Why context does not resolve it:** The reader can see when enrollment stopped but cannot determine how the300-outcome boundary decision fits an unchanged200/380 inferential schedule. No P,observedZ or recalibrated300 boundary is supplied.
**Display precision:**200,300,380 are exact stage counts; their differences are not display rounding. Comparison concerns the applied decision rule, not an estimated sample-size arithmetic.
**Alternatives and missing definitions:** DSMB review may have used an operational or discretionary safety/efficacy assessment distinct from a scheduled inferential interim analysis; alternatively a boundary could have been validly mapped to300. The supplied paragraph nevertheless links the stop and null rejection directly to a prespecified boundary without giving that mapping. One-sided.025 versus family-wise.05 alone is not the finding.
**Human question:** Which inferential boundary/rule applied to the300 completed90-day outcomes, and how was it reconciled with the stated200/380 schedule and no-additional-analysis statement?
**S record:** S5094.
**Status:** Pending Human Adjudication.

### F-ST1-506

**Title:** A historical sICH comparison withP=.072 is included in a statement that the safety outcomes significantly increased.

**Locations and roles:** [DOC-003 p16 historical SELECT early-window safety paragraph](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16), PLAN. Direct layout extraction confirms the full sentence and its immediate context.

**Printed values and statement:** sICH8/173(5%) versus3/18(17%),P=.072; neurological worsening14/173(8%) versus5/18(28%),P=.023; mortality15/173(9%) versus7/18(39%),P=.001. The sentence includes all three parenthesized outcomes and says they “also significantly increased” with large core.

**Rule and calculation:** At default significance level.05, .072>.05 while.023/.001<.05. The significance statement encompasses a listed sICH test that is nonsignificant. P=.072 rounding interval[.0715,.0725) remains entirely above.05. Counts/percentages and direction reconcile; only stated statistical significance is questioned. No chi-square/Fisher/Wald test is assumed or reconstructed.

**Focus area:** B.
**Proposed review domain:** plan_material.
**Proposed relationship type / all relationships:** P_P / P_P.
**Qualifying route:** Route A, category1.
**Affected result or extracted value:** The supplied historical SELECT sICH comparison and whether its evidence is described as statistically significant in the protocol rationale.
**Why context does not resolve it:** Category1 includes a supplied P-versus-stated-test conflict. The always-register requirement prevents peripheral exclusion solely because this is historical PLAN rationale.
**Alternatives and missing definitions:** “Significantly increased” may describe the safety pattern collectively, emphasizing the other two tests or clinical rather than statistical significance; alternatively a different significance threshold may have applied. No collective test, alternate threshold or clinical-significance qualification is supplied in this sentence.
**Classification ambiguity:** Historical rather than an observed SELECT2 result; retainPLAN/P_P/plan_material provisionally for independent screening.
**Human question:** Does the significant-increase statement include the historical sICH comparison withP=.072, and what significance threshold or collective test supports that reading?
**S record:** S5118.
**Status:** Pending Human Adjudication.

## Excluded observations

Only apparent issues not emitted are listed. Checks that reconcile are documented in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| DOC-006 eTable8 pp45–46;S5001–S5024 | Several adjusted profile RR/RD directions differ from crude ratios/differences, notably EVT mRS0–2 D1 crude(21/76)/(10/75)=2.072 vsadjustedRR.51. Source labels adjusted; no crude-effect claim. | MODEL_VERSUS_CRUDE |
| DOC-006 eTables8–10 pp45–50;S5025–S5062 | Individual effect intervals excluding1 beside nonsignificant last-column P initially resemble null-test conflicts; heading explicitly says interaction, a different contrast. No matched interval/P contradiction reproduced. | NOT_REPRODUCED |
| DOC-006 eTable12 p52;S5063–S5066 | P<.001 cannot be reconstructed from medians/IQRs alone; no contradictory matched effectCI/statistic or named ranks supplied. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p14;S5111 | HistoricalOR2.56(2.50–8.47),P=.04 is asymmetric under a diagnostic log-Wald convention; point containment/significance agree. CI method/test not stated, and no same-display method reproduced. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p78;S5084 | Target-mismatch minimization weight blank; later SAPp37 provides2. No executed allocation discrepancy supplied. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 pp55–56;S5086 | Absolute/relative scale of MMmortality increase>20% unspecified without an executed triggering comparison. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p45;S5069 | GeneralizedCMH “stratified” adjustment names continuous age/NIHSS/time/core, but stratum construction missing; no executed numeric implementation contradicts text. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p46/DOC-004p11;S5072 | Diagnostic normalN363.579 vsfixed376; half-unit input ranges approximately349–379 overlap376±.5; exact WMW/simulation variance not claimed. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 p46/DOC-004pp10–11;S5071 | Diagnostic half-tie untie-normal standardizedeffect.324760 vsprinted.34 differs4.48% before rounding; named standardized-effect implementation absent. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-003 pp62–63;S5091,S5092 | Beta(.4,.6) posterior atN60 reaches>.95 with31events(.9644096), printed threshold32. Integer intervals[30.5,31.5]and[31.5,32.5]touch; gap0. Even exact integer discrepancy1/32=.03125≤.05. Same pattern consolidated. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p16;S5096 | ARD's probability description differs from explicit2(WMW−.5) transformation; source formula immediately identifies net effect and no executedARDvalue is supplied. | TERMINOLOGY_OR_WORDING |
| DOC-003 p51;S5067 | First second-aim comparison repeats unfavorableCT/favorableCTP in two word orders; opposite profiles are identified by p22, second p51 paragraph and p71diagram. | TERMINOLOGY_OR_WORDING |
| DOC-003 p48/DOC-004p10;S5075 | Earlier final overall-failure subgroup-rescue branch not restated in later SAP; no final analysis executed because300stop disclosed, and no numerical final result is in conflict. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p46/DOC-004pp11–12;S5072,S5094 | Fixedalpha.05 vsone-sided.025 andfamily-wise.05 do not by themselves establish inconsistent calibration; sidedness is specified at distinct stages. | CONTEXT_RESOLVES |
| DOC-003 p16;S5118–S5120 | Narrative says safety outcomes “doubled” although displayed crude increases are3.60,3.43,4.49fold; this contextual qualitative increase is historical wording, and exact values remain explicit. Separate P-versus-significance issue emittedF-ST1-506. | TERMINOLOGY_OR_WORDING |

## Limitations and coverage conclusion

All assigned inferential estimates, intervals, P values and operative plan rules are tracked; no gap remains. Exact unspecified CI/P and simulation implementations cannot be reproduced from summary values and are not inferred. No scientific issue is emitted merely for missing definitions. Historical routeA findings retain their source role and classification ambiguity for the independent inclusion screen. All six findings remain Pending Human Adjudication; no severity, acceptance or correction assigned.

