# Statistical consistency review — pass 2

- Runtime agent ID: /root/statistics_2.
- Model: gpt-6.1-sol.
- Reasoning effort: high.
- Start mode: FRESH_SPAWN; distinct from /root/statistics_1.
- Exact scope: all 86 existing statistical relationships, enumerated individually below, the complete 107-row numeric inventory, all five initial screening decisions, C001 and its completed mechanical recheck.
- Output: 86 PASS_2_COMPLETE records; 0 new findings; 17 consolidated excluded observations. No candidate count was assumed.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely. Read the complete S inventory, pass-1 checker, numeric inventory and checker, cross-source checker, initial inclusion screen, complete candidate ledger and mechanical recheck, and the main/support mapper reconstruction sections. Used targeted direct Poppler pdftotext 25.03.0 layout extraction of main pp. 3-5 and 7, protocol pp. 9-10 and 19-21, and supplement pp. 2-3 and 6. Visually reread the exact-source-correspondent supplement p. 2 render established by the current curator. The complete main/support maps locate remaining displays; the current recheck independently confirms all C001 definition/context pages. Extraction is a locator and transcription aid, and supplied PDF text and source-correspondent visuals are authority. No web, legacy review conclusions, Python scientific orchestration, GPU, source mutation or reused-asset mutation was used.

## Rule application and reconciliation

Each S record was revisited for count/denominator implications, estimate containment and endpoint order, effect direction, stated test/model/estimand, matching report occurrences, applicable plan/report rules and the source-recheck implications. Numeric facts remain distinct from inferential implementation. Binary arm fractions and risk differences match the displays within half-percentage-point intervals. Continuous contrasts use the stated Hodges-Lehmann estimator rather than subtraction of marginal medians. A point estimate and its own printed confidence interval are checked for containment independently of a P value; a common test/interval inversion is required only when the supplied source specifies it. No sidedness, degrees of freedom, covariance, variance estimator, interaction scale, additional adjustment or unstated denominator is inferred.

The primary difficult-airway result is 191/198 versus 150/182, difference 14 points (95% CI 8-20), P<.001; the key secondary all-patient result is 373/381 versus 328/376, difference 11 (7-14), P<.001. Both directions and superiority conclusions agree with the stated two-sided .05 rule. All arm estimates are within their intervals. There is no supplied noninferiority/equivalence margin or decision. The main overall-duration interval is printed in reverse order, but the intended limits are immediately identifiable and the supplement prints -1 to 4; this is not an unresolved statistical relationship.

Diagnostic calculations use the stated printed counts, not an asserted reconstruction of an unnamed implementation. For primary success, the pooled two-sample binary diagnostic gives chi-square 20.3176 and two-sided normal-tail P approximately .00000656; for all-patient success it gives 31.4285 and P approximately .0000000207. These support the printed P<.001 conclusions. The sample-size diagnostic with p1=.95, p2=.86, two-sided alpha=.05 and power=.80 gives uncorrected normal n=165.4353 per arm and continuity-corrected n=186.9973, rounding to 187 per arm/374 total. The protocol supplies the Stata 12.1 sampsi command; its unavailable local execution is not replaced by a claim that the diagnostic is the exact software implementation.

The small grade-4 subgroup's 60-point interval (17-100) and chi-square P=.09 do not establish a common-procedure contradiction. A diagnostic unpooled Wald interval from 3/3 versus 2/5 has lower limit about 17.1 points and an upper limit above 100 before truncation, while the pooled chi-square diagnostic gives P approximately .0897. This explicitly illustrates how the supplied pair can coexist without importing CI inversion; it does not identify the authors' unspecified interval construction. Similarly, clustered overall-duration P=.95 is not mechanically inverted from a 1-second interval (-1 to 4) without its test, covariance/variance procedure and rank data. The source expressly recalculates clustered difference/P/interaction columns while retaining the arm columns. Distinct main and supplementary analyses are matched by label, not treated as repeated identical tests.

For difficult-only HR 1.29 (1.04-1.60), the diagnostic log-Wald calculation gives two-sided P about .021; for overall HR 1.12 (.97-1.30) it gives about .129. The actual printed P values .02 and .12 are log-rank tests, not assumed Cox-Wald tests. Their directions and significance descriptions agree. Failed-attempt censoring and the proportional-hazards limitation are explicitly disclosed. Comparing censored Kaplan-Meier success levels or Cox HRs with crude final success percentages would not be a valid identity check.

C001's source recheck reproduces the written cuff-inflation versus blade-removal/attempt-completion definitions and confirms P_R/protocol_report. Both REPORT documents agree, and the PLAN form corroborates a procedural attempt boundary rather than supplying a separate duration-outcome definition. No S_C, S_W or P_P conflict is added. Patient-level numerical changes in duration, hypoxemia, composite success or HRs do not follow from the written definitions alone. C001 remains Pending Human Adjudication and is not re-emitted as a pass-2 finding.

The interim screen distinguishes the primary outcome measure from the final difficult-airway main-analysis population. The source's immediate 500-enrolled/1,000-total equal-allocation projection supports the all-enrolled first-pass-success calculation. From 250/257 and 213/250, a diagnostic completion to 500 per arm under the capped uplift gives (250+243)/500=.986 versus (213+250×.852)/500=.852, difference .134, consistent with continuation. This is a diagnostic application of the written rule, not an assertion of the unpublished exact projected table/P. The all-enrolled population observation already screened as CONTEXT_RESOLVES is not re-emitted. The accrual observation already screened as CONDITIONAL_OR_UNREPORTED also is not re-emitted: closure before the calendar endpoint cannot be inferred from the published count/September-August period. Missing actual stopping dates or a trigger record are named limits, not a new contradiction.

## Findings

No new observation met all four inclusion criteria. New finding count: 0. The existing five screening decisions are retained; no F-ST2 ID is assigned, and no stable candidate is added or removed.

## Every statistical relationship revisited

For all binary rows, the pass-2 check includes the supplied arm fractions/proportions, each arm CI, the risk-difference estimate/CI, displayed P value, and interaction P if present. Integer percentages and interval endpoints retain half-unit display intervals. Explicit process/complication rows are preserved even when cross-location comparisons are peripheral. The exact locations, source roles and full printed inputs remain in the companion inventory; the following records the independent pass-2 result and missing definitions for every ID.

| S ID | Pass-2 reconciliation and bounded result | Pass 2 |
|---|---|---|
| S001 | Allocation/block specification and primary subset revisited with N001/N002/N096; facial/neck stratum wording does not establish a changed primary model or population. Actual alternative stratum-adjusted result is absent. No new finding. | PASS_2_COMPLETE |
| S002 | First-device failure, device switch, no passage and difficult-subset definition match flow/result populations; 198+182=380. Outcome measure and final analysis subset kept distinct for interim. No new finding. | PASS_2_COMPLETE |
| S003 | Direct cuff-inflation versus attempt-completion oxygen-window clauses remain in reproduced C001; implementation and event-time equality unreported. No numerical consequence or additional relationship inferred. | PASS_2_COMPLETE |
| S004 | Cuff-based duration and blade-based duration are explicit C001 occurrences; first-attempt/successful-only/event-time analyses remain distinct. Source recheck supplies no change in an estimate or HR. | PASS_2_COMPLETE |
| S005 | 95%/86%, 9 points, 80%, two-sided .05 and 187/arm corroborated by labelled continuity-corrected diagnostic. Stata 12.1 unavailable; exact command not executed. No new finding. | PASS_2_COMPLETE |
| S006 | Achieved 380 difficult/757 total meets target; published September-August period permits the calendar endpoint. Existing screened accrual observation retained; operative day-level trigger is absent. | PASS_2_COMPLETE |
| S007 | Randomized 381/376 and difficult 198/182 retained, including crossovers and 11 no-device failures; laryngoscope insertion is an attempted procedure. No alternative ITT exclusion set demonstrated. | PASS_2_COMPLETE |
| S008 | Binary chi-square, two-sided .05, 95% CI and risk difference labels align with primary/key secondary results. Binary interval construction/common inversion unspecified. No new finding. | PASS_2_COMPLETE |
| S009 | Wilcoxon and Hodges-Lehmann descriptions are internally coherent; marginal median differences need not equal the estimated shift. Individual ranks and exact duration contributors absent. No new finding. | PASS_2_COMPLETE |
| S010 | Every displayed interaction revisited, including .36/.35 for the primary subgroup across distinct analyses. Interaction model/link/scale and covariance not supplied, so no numerical identity is imposed. | PASS_2_COMPLETE |
| S011 | Exploratory subgroups and no multiplicity correction expressly disclosed; .05 superiority threshold agrees with conclusions. The 9% planning effect is not a supplied margin decision. | PASS_2_COMPLETE |
| S012 | Kaplan-Meier/log-rank/unadjusted Cox and failed-attempt censoring match captions. PH limitation expressly disclosed; patient times/censoring records missing. No source-grounded contradictory method step found. | PASS_2_COMPLETE |
| S013 | Post hoc physician clustering, ICC<.001, CI upper bound .03 and recalculated columns disclosed. Specific clustered test/variance implementation absent; no unreported identity is inferred. | PASS_2_COMPLETE |
| S014 | N056 and N059/N062/N085 missingness examined: absent waveforms and known primary failure can yield different evaluable composite/hypoxemia sets. Patient cross-classification absent; primary outcome remains unambiguous. | PASS_2_COMPLETE |
| S015 | All-enrolled 507=257+250 calculation fits immediate primary-outcome/1,000-total rule; diagnostic .986 versus .852 supports continuation. Existing screened population observation not re-emitted. | PASS_2_COMPLETE |
| S016 | DSMB safety/additional-analysis discretion and futility-only assessment do not conflict with a reported stopping event. No safety/superiority halt or revised primary threshold supplied. | PASS_2_COMPLETE |
| S017 | Planned descriptive and Kaplan-Meier summaries revisited; omitted summaries alone establish no replaced primary/key secondary analysis or conflicting number. No new finding. | PASS_2_COMPLETE |
| S018 | Patient randomization/analysis unit and form's attempt/device-switch definitions match result partitions; ancillary safety windows do not establish a changed key-secondary count. Timing pattern remains C001 only. | PASS_2_COMPLETE |
| S019 | Non-rebreather 267/381 versus 276/376, -3 (-10 to 3), P=.31: fractions, interval, direction and binary diagnostic agree. No new finding. | PASS_2_COMPLETE |
| S020 | Flush-rate 204/267 versus 210/276, 0 (-7 to 7), P=.93: nested denominator explicit; containment and null-compatible direction agree. | PASS_2_COMPLETE |
| S021 | Bag/mask 47/381 versus 37/376, 2 (-2 to 7), P=.27: containment/direction and pooled binary diagnostic agree. | PASS_2_COMPLETE |
| S022 | Noninvasive positive-pressure 18/381 versus 24/376, -2 (-5 to 2), P=.32: counts and inferential direction agree. | PASS_2_COMPLETE |
| S023 | Extraglottic 27/381 versus 17/376, 3 (-1 to 6), P=.13: interval contains estimate; direction and diagnostic agree. | PASS_2_COMPLETE |
| S024 | Any sedative 338/381 versus 341/376, -2 (-6 to 2), P=.37: fractions and direction agree; unlisted drugs resolve incomplete subcategory sums. | PASS_2_COMPLETE |
| S025 | Etomidate 332/381 versus 333/376, -1 (-6 to 3), P=.54: containment/direction consistent; minor process diagnostic P difference lacks complete implementation and no key-result implication. | PASS_2_COMPLETE |
| S026 | Ketamine 4/381 versus 4/376, 0 (-1 to 1), P=.99: near-null direction and containment agree; no test/CI identity inferred. | PASS_2_COMPLETE |
| S027 | Any blockade 366/381 versus 367/376, -2 (-4 to 1), P=.23: fractions, containment and direction agree; named drugs need not exhaust total. | PASS_2_COMPLETE |
| S028 | Succinylcholine 214/381 versus 229/376, -5 (-12 to 2), P=.19: effect direction/containment and binary diagnostic agree. | PASS_2_COMPLETE |
| S029 | Rocuronium 147/381 versus 137/376, 2 (-5 to 9), P=.54: fractions and direction agree; no new finding. | PASS_2_COMPLETE |
| S030 | Sniffing 222/381 versus 244/376, -7 (-14 to 0), P=.06: near-null endpoint and nonsignificant P compatible with whole-point display. | PASS_2_COMPLETE |
| S031 | Neutral cervical spine 117/381 versus 96/376, 5 (-1 to 12), P=.11: interval, direction and diagnostic agree. | PASS_2_COMPLETE |
| S032 | Extension 39/381 versus 32/376, 2 (-2 to 6), P=.42: null-compatible interval and direction agree; form permits other positions. | PASS_2_COMPLETE |
| S033 | Saturation 100 (98-100) in both arms, shift 0 (0-0), P=.60: discrete/displayed shift and rank test need not invert; rank data absent. | PASS_2_COMPLETE |
| S034 | Start saturation<90%, 22/360 versus 27/343, -2 (-6 to 2), P=.36: printed evaluable denominators used; missing 21/33 matches N056. | PASS_2_COMPLETE |
| S035 | Start saturation<80%, 13/360 versus 8/343, 1 (-1 to 4), P=.32: subset bounds and containment/direction agree. | PASS_2_COMPLETE |
| S036 | Apneic nasal cannula 221/381 versus 227/376, -2 (-9 to 5), P=.51: fractions, interval and diagnostic direction agree. | PASS_2_COMPLETE |
| S037 | Senior/fellow 318/381 versus 334/376, -5 (-10 to 0), P=.03: rounded near-zero bound does not contradict P; process count partition observation remains peripheral. | PASS_2_COMPLETE |
| S038 | Junior 57/381 versus 37/376, 5 (0-10), P=.03: whole-point endpoint can conceal positive lower limit; process-category sum is not primary population size. | PASS_2_COMPLETE |
| S039 | Faculty 8/381 versus 5/376, 1 (-1 to 3), P=.42: containment and direction agree; operator-category count observation remains peripheral. | PASS_2_COMPLETE |
| S040 | C-MAC 362/381 versus 366/376, -2 (-5 to 0), P=.10: null-compatible whole-point interval and diagnostic align; laryngoscope totals match arms. | PASS_2_COMPLETE |
| S041 | GlideScope 12/381 versus 8/376, 1 (-1 to 3), P=.38: fraction, interval and direction checks reconcile. | PASS_2_COMPLETE |
| S042 | Direct Macintosh 7/381 versus 2/376, 1 (0-3), P=.10: 0 displayed lower endpoint does not assert a strictly positive CI; no common inversion inferred. | PASS_2_COMPLETE |
| S043 | Screen never 218/377 versus 182/372, 9 (2-16), P=.02: known evaluable denominators, positive effect and test direction agree; small diagnostic difference is process-only and implementation-dependent. | PASS_2_COMPLETE |
| S044 | Screen entire attempt 78/377 versus 90/372, -4 (-9 to 2), P=.25: fractions/interval/direction agree; form supplies unlisted applicable categories. | PASS_2_COMPLETE |
| S045 | Screen during passage 75/377 versus 98/372, -6 (-12 to 0), P=.04: displayed 0 limit can round from a negative bound; diagnostic direction agrees. | PASS_2_COMPLETE |
| S046 | View grade 1, 269/373 versus 269/359, -3 (-9 to 4), P=.39: counts/denominators and negative difference agree. | PASS_2_COMPLETE |
| S047 | View grade 2, 74/373 versus 62/359, 3 (-3 to 8), P=.39: containment/direction agree; small diagnostic difference in process composition has no established primary/key-secondary implication. | PASS_2_COMPLETE |
| S048 | View grade 3, 27/373 versus 23/359, 1 (-3 to 4), P=.66: interval and binary diagnostic agree. | PASS_2_COMPLETE |
| S049 | View grade 4, 3/373 versus 5/359, -1 (-2 to 1), P=.44: bounds, containment and direction agree. | PASS_2_COMPLETE |
| S050 | Actual bougie first 372/381 versus 25/376, 91 (88-94), P<.001: effect direction and large diagnostic association agree; distinguished from randomized efficacy. | PASS_2_COMPLETE |
| S051 | Actual tube first 4/381 versus 345/376, -91 (-94 to -88), P<.001: reciprocal adherence pattern, effect and direction agree. | PASS_2_COMPLETE |
| S052 | No device 5/381 versus 6/376, 0 (-2 to 1), P=.75: 11 failures included in ITT; near-null interval/test agree. | PASS_2_COMPLETE |
| S053 | Primary 191/198 versus 150/182, 14 (8-20), P<.001: exact counts, arm intervals, matched abstract/narrative and superiority direction agree. Interaction scale unreported; clustered occurrence distinguished. | PASS_2_COMPLETE |
| S054 | Difficult composite 156/191 versus 123/177, 12 (3-21), P=.006: fractions/arm CIs/effect/test direction agree. Oxygen-anchor occurrence belongs to C001; joint missingness absent. | PASS_2_COMPLETE |
| S055 | Difficult duration 39 versus 40, shift -1 (-6 to 3), P=.50: containment and no-difference description agree. Ranks absent; event-time HR is a different analysis, and timing pattern is C001. | PASS_2_COMPLETE |
| S056 | All-patient success 373/381 versus 328/376, 11 (7-14), P<.001: complements of difficult/no-difficult success sum; matching abstract/narrative and superiority agree. | PASS_2_COMPLETE |
| S057 | Overall composite 317/371 versus 282/366, 8 (3-14), P=.003: printed evaluable fractions, arm CIs and direction agree. Joint missingness absent; C001 does not establish different event numbers. | PASS_2_COMPLETE |
| S058 | Overall duration 38 versus 36, shift 1, printed 4 to -1, P=.24: intended -1 to 4 immediately recoverable and corroborated; Hodges-Lehmann differs from crude median subtraction. | PASS_2_COMPLETE |
| S059 | Blood/vomit 79/83 versus 55/67, 13 (3-23), P=.01: baseline denominators and success subgroup match; positive CI/test direction agree. Interaction .31 not inverted without scale. | PASS_2_COMPLETE |
| S060 | Cervical immobilization 49/49 versus 28/36, 22 (9-36), P=.001: arm/contrast intervals contain estimates; displayed P matches diagnostic to precision. No identity with interaction .25 inferred. | PASS_2_COMPLETE |
| S061 | Obesity 55/57 versus 51/68, 21 (10-33), P=.001: subgroup denominators match physician classification; positive direction and intervals agree. BMI-based descriptive population distinct. | PASS_2_COMPLETE |
| S062 | No difficulty 182/183 versus 178/194, 8 (4-12), P<.001: complements match overall counts and narrative; significance direction agrees. Interaction .36 concerns effect modification, not subgroup P. | PASS_2_COMPLETE |
| S063 | C-MAC success 356/362 versus 321/366, 11 (7-14), P<.001: device-subset denominators match process table; containment/direction and narrative agree. | PASS_2_COMPLETE |
| S064 | Grade-1 success 265/269 versus 258/269, 3 (0-5), P=.07: arm/effect intervals contain estimates; nonsignificant main P is distinct from interaction .04. No scale inferred. | PASS_2_COMPLETE |
| S065 | Grade-2 success 72/74 versus 41/62, 31 (19-44), P<.001: denominator/view matching and positive test direction agree. Pooled grade-2-4 narrative is not this single subgroup. | PASS_2_COMPLETE |
| S066 | Grade-3 success 26/27 versus 11/23, 48 (27-71), P<.001: estimates inside all intervals; counts/positive direction agree. | PASS_2_COMPLETE |
| S067 | Grade-4 success 3/3 versus 2/5, 60 (17-100), P=.09: containment/order/direction checked; unpooled CI versus pooled chi-square diagnostics can coexist. CI construction absent; no contradiction registered. | PASS_2_COMPLETE |
| S068 | Actual-device success 392/402 versus 309/355, 10 (7-14), P<.001: footnote's 5/6 no-device assignment reproduces denominators; exact risk difference 10.4701 points rounds to 10. | PASS_2_COMPLETE |
| S069 | Successful-only duration 38 versus 34, shift 4 (2-7), P<.001: positive effect/test direction agree; analysis set explicitly post hoc and distinct from overall. Ranks/contributor details absent. | PASS_2_COMPLETE |
| S070 | Difficult HR 1.29 (1.04-1.60), log-rank P=.02: population 198/182 and risk-row bounds match; containment/direction/diagnostic align. PH limit disclosed; C001 adds no demonstrated HR change. | PASS_2_COMPLETE |
| S071 | Overall HR 1.12 (.97-1.30), log-rank P=.12: matched main/supplement population 381/376 and nonsignificance agree. Cox/log-rank identity not imposed; times absent. | PASS_2_COMPLETE |
| S072 | Any complication 66/381 versus 63/376, 1 (-5 to 6), P=.83: near-null interval/direction agree; one-person composite need not equal summed component events. | PASS_2_COMPLETE |
| S073 | Hypoxemia 47/371 versus 50/364, -1 (-6 to 4), P=.67: exact incidence reproduces 13%/14%; available waveform denominator differs from composite conditionally. Definition comparison retained in C001. | PASS_2_COMPLETE |
| S074 | Pneumothorax 9/381 versus 9/376, 0 (-2 to 2), P=.99: containment and near-null direction agree; small diagnostic difference alone does not establish test implementation or change key result. | PASS_2_COMPLETE |
| S075 | Unexplained pneumothorax 1/381 versus 3/376, -1 (-2 to 1), P=.31: count bounds, CI/direction and diagnostic agree. | PASS_2_COMPLETE |
| S076 | Lip laceration 7/381 versus 3/376, 1 (-1 to 3), P=.21: fraction, interval/direction and diagnostic agree. | PASS_2_COMPLETE |
| S077 | Witnessed aspiration 3/381 versus 1/376, 1 (-1 to 2), P=.32: containment and count/test direction agree. | PASS_2_COMPLETE |
| S078 | Iatrogenic bleeding 2/381 versus 2/376, 0 (-1 to 1), P=.99: null-compatible estimate/CI and diagnostic agree. | PASS_2_COMPLETE |
| S079 | Dental trauma 1/381 versus 1/376, 0 (-1 to 1), P=.99: near-null difference and interval/test direction agree. | PASS_2_COMPLETE |
| S080 | Esophageal intubation 0/381 versus 3/376, -1 (-2 to 0), P=.08: bounds, negative direction and nonsignificant description agree with printed precision. | PASS_2_COMPLETE |
| S081 | Clustered primary 14 (7-21), P<.001, interaction .35: arm inputs match S053; estimate inside CI and superiority retained. Distinct cluster analysis explicit; implementation absent. | PASS_2_COMPLETE |
| S082 | Clustered difficult composite 12 (2-22), P=.015, interaction .61: arm fractions match S054; positive interval/test agree. C001 remains definition-only; clustered variance construction absent. | PASS_2_COMPLETE |
| S083 | Clustered difficult duration -1 (-6 to 3), P=.31, interaction .17: arm medians match S055; containment/order and null-compatible conclusion agree. Clustered rank/test implementation absent. | PASS_2_COMPLETE |
| S084 | Clustered overall success 11 (6-15), P<.001: same 373/381 versus 328/376; containment/direction and superiority agree. Different interval is disclosed cluster result. | PASS_2_COMPLETE |
| S085 | Clustered overall composite 8 (2-15), P=.02: same 317/371 versus 282/366; interval/test direction agree. Definition pattern retained in C001, no event-number consequence inferred. | PASS_2_COMPLETE |
| S086 | Clustered overall duration 1 (-1 to 4), P=.95: exact source table visually matches; estimate/order and nonsignificance agree. Common test/CI inversion, variance procedure and ranks absent; no new finding. | PASS_2_COMPLETE |

## Excluded observations

Each repeated observation is recorded once here with exactly one reason code. Previously screened findings are referenced to preserve their decisions, not re-emitted as new findings.

| Location | Observation | Reason code |
|---|---|---|
| PLAN [protocol pp. 9-10](../../../joi180054supp1_prod.pdf#page=9); REPORT [main p. 3](../../../jama_driver_2018_oi_180054.pdf#page=3), Tables 3/5, supplement pp. 2-3 | Explicit timing-anchor pattern is already C001/F-XS-001 with F-ST1-001 as its duplicate; recheck reproduces definitions, with no demonstrated numeric/HR consequence. | DUPLICATE_OF_INCLUDED |
| PLAN [protocol p. 19](../../../joi180054supp1_prod.pdf#page=19); REPORT main pp. 1-4 | Actual pre-calendar closure caused by crossing 374 is not supplied; existing F-ST1-002 screening retained. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocol p. 21](../../../joi180054supp1_prod.pdf#page=21); REPORT [supplement p. 6](../../../joi180054supp2_prod.pdf#page=6) | Outcome-only interim rule and 1,000-total projection explain all-enrolled rates; existing F-XS-002/F-ST1-003 decisions retained. | CONTEXT_RESOLVES |
| REPORT [main p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7), overall duration; supplement p. 2 | Reversed printed 4 to -1 limits have immediately recoverable intended order -1 to 4. | NOTATION_OR_TYPOGRAPHY |
| REPORT main pp. 4/7, all duration and saturation shift rows | Stated Hodges-Lehmann effects do not require equality to differences of displayed medians. | MODEL_VERSUS_CRUDE |
| REPORT main p. 7, grade-4 success | Positive difference CI and chi-square P=.09 do not establish common inversion; diagnostic unpooled interval and pooled test can coexist. | CONDITIONAL_OR_UNREPORTED |
| REPORT [supplement p. 2](../../../joi180054supp2_prod.pdf#page=2), overall duration | P=.95 and CI -1 to 4 cannot be inverted without the exact clustered test/variance construction and ranks. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p. 4; [supplement p. 3](../../../joi180054supp2_prod.pdf#page=3) | Cluster implementation beyond physician ICC/upper-bound use is absent; no necessary step is shown to be contradicted. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p. 7 and supplement pp. 2-3 | Clustered versus main intervals/tests differ under expressly distinguished analyses with matching arm values. | CONTEXT_RESOLVES |
| REPORT main pp. 4/7 and supplement pp. 2-3 | Interaction model/link/contrast scale and covariance unavailable; selected subgroup or effect-scale reconstruction would assume missing definitions. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp. 5/8-10 and supplement p. 4 | PH limitation and failed-attempt censoring disclosed; requesting an alternative method would be broad methodology preference. | OUT_OF_FOCUS |
| REPORT main p. 4 exploratory methods | No multiple-comparison correction expressly disclosed and no contradictory planned correction supplied. | OUT_OF_FOCUS |
| PLAN protocol p. 11; REPORT main p. 3 | Stratum-list difference has no demonstrated changed primary model/result or analysis-population size. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp. 20-21; REPORT main p. 4 | Missing-primary paragraph's composite wording is resolved by repeated first-pass primary definition; no ambiguous primary result/excluded case supplied. | TERMINOLOGY_OR_WORDING |
| PLAN protocol p. 19; REPORT main/supplement analysis displays | Unprinted mean/SD/extrema/Kaplan-Meier percentile summaries are details alone, without a shown replaced primary/key secondary analysis. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp. 6/9, process/complication diagnostics and operator-category sum | Small implementation-dependent diagnostic differences and process-category composition do not establish a changed primary/key secondary result or analysis population. | PERIPHERAL_COMPARISON |
| REPORT main pp. 7/9, composite versus hypoxemia denominators | Equality of the composite and hypoxemia observed sets would assume unavailable patient-level joint missingness; known first-attempt failure can establish composite failure independently of waveform. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

All 86 existing S IDs are PASS_2_COMPLETE in this artifact and the companion [statistical inventory](../statistics/relationship_inventory.md). The entire ledger/screen/recheck set was revisited: C001 and all five finding decisions; no screened observation was re-emitted. All 107 numeric relationships and the complete mapper reconstruction union informed count/denominator, population, label and source matching. No new finding requires a pass-2 inclusion screen.

Missing patient-level ranks/times/waveforms, outcome/missingness cross-classifications, exact binary CI construction, interaction model/link/scale, clustered variance/test implementation, exact accrual day/operative trigger and a dated applicable endpoint amendment limit mechanical reproduction. Stata 12.1 is unavailable for the supplied command. These are bounded evidence limits rather than source-unit omissions. The existing C001 evidence state/domain/relationship remain reproduced/protocol_report/P_R; human adjudication remains pending. Pass-1 facts and stable IDs are preserved; only the reserved pass-2 status column and pass-2 completion provenance were added to the inventory.
