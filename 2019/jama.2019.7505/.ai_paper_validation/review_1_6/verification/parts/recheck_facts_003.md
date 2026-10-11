# Recheck facts part 003 for statistical pass 2 and audit

Scope: C073–C106; 34 stable IDs; 21 recorded_candidate and 13 record_input_error. All remain Pending Human Adjudication. Exact source links, source inputs, calculations, alternatives and full classification rationales are preserved for every ID in evidence_recheck_003.md. This compact handoff makes no adjudication and omits no facts from the full durable cards.

## C073 — Waist-to-hip ratio assigned a length unit

- Determining fact/state: recorded_candidate. The directly printed ratio heading carries cm; the dimensional comparison reproduces. Diagnostic: Length/length has dimension 1; cm is a length unit, so it cannot denote that ratio. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: No raw measurement is needed; exact construction is not stated independently. Human question: Does cm belong to a different variable, or is the Figure 2 ratio intended to be dimensionless?

## C074 — Waist-to-hip ≥1.0 point versus crude risks

- Determining fact/state: recorded_candidate. Counts, RR label and point are confirmed; the registered conditional point-estimator/label question remains. The Methods GLM sentence explicitly concerns heterogeneity, so it does not independently identify or disprove the row-point estimator. Diagnostic: (98/447)/(112/449) = 0.878915; rounds to 0.88, versus 0.92. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Link, model formula, covariates, point-estimator derivation/standardization and whether plotted RR is marginal or conditional. Human question: Which link, contrast, adjustment and postprocessing generated 0.92, and does that point purport to equal the two displayed crude arm risks?

## C075 — Mortality caption names extrapulmonary complications

- Determining fact/state: recorded_candidate. Direct render shows mortality title/axis and an extra-pulmonary caption on the same page. Diagnostic: 0.5%/0.3% and HR/CI match mortality; extra-pulmonary comparator is 16.9%/15.2%. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Underlying endpoint code is absent; it is not needed to observe the literal label mismatch. Human question: Which endpoint was plotted in eFigure 11, and should its caption name mortality or extra-pulmonary complications?

## C076 — Collapsed composite OR/RR headings

- Determining fact/state: recorded_candidate. The literal OR header above collapsed composite is confirmed in the current render; main labels identical display RR. Diagnostic: RR=pH/pL; OR=[pH/(1−pH)]/[pL/(1−pL)]. Identical point and CI are printed under the two headings. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Which estimator the collapsed-composite row actually uses; whether global header has a row exception. Human question: Does the Global Tests OR heading apply to Collapsed Composite, and what estimator produced that row versus main Table 3?

## C077 — Synthetic-colloid count P differs

- Determining fact/state: recorded_candidate. Direct native source confirms different P values for the same printed binary receipt counts. Diagnostic: 0.10−0.09 = 0.01; displays have the same two-decimal precision. No tail test is substituted. Classification S_C; all S_C; statistical_results; no role/type code correction.
- Missing definition and human question: Exact test and continuity correction/Fisher convention for each row; exact unrounded output. Human question: Were the two binary receipt P values generated with the same test/analysis set; if different, what conventions produced .09 and .10?

## C078 — Mild respiratory failure oxygen boundary

- Determining fact/state: recorded_candidate. Current source image confirms =2, while main prints 2 L or less. Diagnostic: A response at 1 L/min satisfies ≤2 but not =2. No revised count is inferable. Classification S_C; all S_C; statistical_results; no role/type code correction.
- Missing definition and human question: Operational oxygen test and endpoint dictionary; classification below 2 L/min. Human question: How were patients responding below 2 L/min classified, and which boundary generated the mild respiratory-failure counts?

## C079 — Emergency counts across baseline/surgery tables

- Determining fact/state: recorded_candidate. Exact repeated emergency counts differ as registered; the missing mapping remains the named conditional question. Diagnostic: Main−supplement emergency =8 high/9 low; emergency+urgent =22/24; priority totals =984/982. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Baseline versus surgical-time definition, urgency crosswalk, missing records and actual observed denominators. Human question: Are main emergency procedure and supplemental emergency priority the same field/time; if so, how are 21/20 reconciled with 13/11, and if not, what mapping defines them?

## C080 — Hypoxemia duration-qualified/unqualified definitions

- Determining fact/state: record_input_error. The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled. Diagnostic: Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it. Classification S_C; all S_C, S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Counted event field, duration filtering, whole-intraoperative versus recruitment-only window, and whether footnote/eMethods abbreviate the Methods. Human question: Which exact variable/window generated 49/134 hypoxemia, did it apply the Methods duration, and are footnote/eMethods abbreviated descriptions of that same variable?

## C081 — Hypotension duration-qualified/unqualified definitions

- Determining fact/state: record_input_error. The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled. Diagnostic: Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it. Classification S_C; all S_C, S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Counted event field, duration filtering, whole-intraoperative versus recruitment-only window, and whether footnote/eMethods abbreviate the Methods. Human question: Which exact variable/window generated 313/170 hypotension, did it apply the Methods duration, and are footnote/eMethods abbreviated descriptions of that same variable?

## C082 — Conditional thoracic VAS moment bound

- Determining fact/state: recorded_candidate. Direct source confirms the tuple and 10 cm plan description; the registered bounded-support question remains conditional on its explicitly missing origin/scale identity. Diagnostic: At m1.4,n841, maximum SD=3.47194. Allowing mean rounding up to1.45 gives 3.52310, below minimum rounding-consistent SD3.85 by 0.32690 cm. Classification P_R; all P_R; protocol_report; no role/type code correction.
- Missing definition and human question: Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention. Human question: Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used?

## C083 — Conditional event-count mean versus component sum

- Determining fact/state: recorded_candidate. Count tuple and component totals are confirmed; arithmetic reproduces the registered conditional high-arm rounding question. Diagnostic: High sum353;353/989=0.356926→0.36, versus0.35. Low sum376;376/987=0.380952→0.38. High two-decimal0.35 permits integer totals342–351 under ordinary rounding. Alternative353/1011=0.349159→0.35 and376/1002=0.375250→0.38. Classification S_C; all S_C; statistical_results; no role/type code correction.
- Missing definition and human question: First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention. Human question: Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it?

## C084 — Median follow-up versus day-five risk count — eFigure 8 PPC

- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 8 PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C085 — Median follow-up versus day-five risk count — eFigure 9 severe PPC

- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 9 severe PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C086 — Median follow-up versus day-five risk count — eFigure 10 extrapulmonary

- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1673 exceeds988 by685. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 10 extrapulmonary, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C087 — Median follow-up versus day-five risk count — eFigure 11 mortality

- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1971 exceeds988 by983. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 11 mortality, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C088 — Mild respiratory failure sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (135/989)/(154/987)=0.874851; absolute distance from0.92=0.045149, larger than .005. Interval is positive, ordered and contains its printed point (0.76≤0.92≤1.12). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C089 — Moderate respiratory failure sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (42/989)/(58/987)=0.722674; absolute distance from0.83=0.107326, larger than .005. Interval is positive, ordered and contains its printed point (0.59≤0.83≤1.17). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C090 — Severe respiratory failure sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (30/989)/(36/987)=0.831648; absolute distance from0.91=0.078352, larger than .005. Interval is positive, ordered and contains its printed point (0.61≤0.91≤1.34). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C091 — Aspiration sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (2/989)/(1/987)=1.995956; absolute distance from1.33=0.665956, larger than .005. Interval is positive, ordered and contains its printed point (0.41≤1.33≤4.30). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C092 — Bronchospasm sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (12/989)/(10/987)=1.197573; absolute distance from1.09=0.107573, larger than .005. Interval is positive, ordered and contains its printed point (0.62≤1.09≤1.91). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C093 — ARDS sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (3/989)/(1/987)=2.993933; absolute distance from1.50=1.493933, larger than .005. Interval is positive, ordered and contains its printed point (0.65≤1.50≤3.44). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C094 — Atelectasis sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (44/989)/(55/987)=0.798382; absolute distance from0.88=0.081618, larger than .005. Interval is positive, ordered and contains its printed point (0.64≤0.88≤1.23). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C095 — Cardiopulmonary edema sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (17/989)/(9/987)=1.885069; absolute distance from1.31=0.575069, larger than .005. Interval is positive, ordered and contains its printed point (0.87≤1.31≤1.98). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C096 — Pleural effusion sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (43/989)/(21/987)=2.043478; absolute distance from1.36=0.683478, larger than .005. Interval is positive, ordered and contains its printed point (1.05≤1.36≤1.76). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C097 — Pneumothorax sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (1/989)/(3/987)=0.332659; absolute distance from0.50=0.167341, larger than .005. Interval is positive, ordered and contains its printed point (0.04≤0.50≤5.96). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C098 — Pulmonary infiltrates sensitivity-forest point versus crude risks

- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (14/989)/(18/987)=0.776205; absolute distance from0.87=0.093795, larger than .005. Interval is positive, ordered and contains its printed point (0.49≤0.87≤1.55). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C099 — Protocol current total748 versus revised2013

- Determining fact/state: recorded_candidate. Current source confirms future-tense748 alongside explicitly revised2013 in the same PLAN version. Diagnostic: 2013−748=1265. The initial748 is explicitly historical in section6.4, but section7.2 retains a current future-tense total. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Whether section7.2 was intended as retained historical text despite future tense. Human question: In version2.6, does section7.2 still prescribe748 or retain a historical paragraph; what current total was intended?

## C100 — Tabulated futility inequality versus central plotted region

- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.225 but lies outside the pink central region at N956. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

## C101 — Tabulated futility inequality versus central plotted region

- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.929 but lies outside the pink central region at N1434. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

## C102 — Tabulated futility inequality versus central plotted region

- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+2.012 but lies outside the pink central region at N1912. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

## C103 — Primary-analysis phrase combines odds ratio and relative risks

- Determining fact/state: recorded_candidate. Current render confirms adjacent odds ratio relative risks; source-label ambiguity reproduces without relying on an OCR error. Diagnostic: For supplied assumptions RR=.30/.40=.75; OR=(.30/.70)/(.40/.60)=.642857. This illustrates scale difference, not an observed-result recalculation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Intended measure(s), contrast and logistic postprocessing for original sentence. Human question: Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval?

## C104 — Tabulated efficacy positive inequality versus negative plotted region

- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.75 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

## C105 — Tabulated efficacy positive inequality versus negative plotted region

- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.432 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

## C106 — Tabulated efficacy positive inequality versus negative plotted region

- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.012 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?


