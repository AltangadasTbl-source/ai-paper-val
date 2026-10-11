# Statistical pass 1 part: forest A

Runtime agent /root/stat1_forest_a (manifest normalized identity root/stat1_forest_a); fresh gpt-6.1-sol/high. Exact disjoint scope: DOC-006 physical PDF pp13-15, eFigures7-9, mapper A028-A030. Inventory: statistics/parts/forest_a.md, S1001-S1069, all69 records PASS_1_COMPLETE. Counts: 48 outcome rows (45 finite RR/95%CI and3asterisks),18 printed interaction tests,3 unprinted interaction slots;1 emitted finding;2 excluded-observation patterns. Source reading corrects the assignment's provisional17printed/4missing count to18printed/3missing without changing the21-slot scope.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md read completely. Report/model context taken only from supplied DOC-001 p4 and DOC-005 pp4-6 and fresh factual maps; no old conclusions or external evidence. Source roles: DOC-006/DOC-001 REPORT; DOC-005 PLAN. Full-page image review covers all48rows and21interaction slots. Candidate locations pp13-14 confirmed against fresh direct-PDF Poppler26.01.0 CPU renderings (preprocessing/stat1_forest_a/direct-p13.png and direct-p14.png); these agree with reusable images. No sources/reused artifacts modified.

## Checks and scope result

All45 finite intervals have ordered endpoints and contain their printed estimates. All positive-outcome finite estimates are at or above1 and align with eFigures7/8's rightward favors-EVT direction; all eFigure9 adverse-outcome estimates are below1 and align with its leftward favors-EVT direction. No adverse-direction discrepancy reproduced. All48pairs of printed counts/percentages reconcile with source-matched arm denominators at the displayed precision. Total subgroup n is not an arm denominator. ASPECTS component rows sum to their parent counts for each outcome. Outcome total across the three mutually exclusive ASPECTS sets is EVT34/MM12 for mRS0-2,EVT65/MM31 for mRS0-3,EVT76/MM102 for mRS5-6; these randomized-arm counts are not compared as duplicates of as-treated Table2 counts.

Every printed P is explicitly headed “Interaction p-value.” None is the P for its adjacent stratum-specific RR. All18 exceed.05, compatible with absence of significant treatment heterogeneity. No interval for the interaction contrast, coefficient/test statistic, degrees of freedom, or covariance is printed. Thus an exact Wald/likelihood/other interaction statistic cannot be numerically reconstructed from the subgroup effect intervals alone. No null-crossing estimate/CI/P contradiction is fabricated by pairing distinct tests. A printed lower limit1.00 on eFigure8 ASPECTS6-10 is retained as displayed; the source does not supply an effect P with which to test a decision discrepancy.

The stated secondary model is within-subgroup modified Poisson regression with robust standard errors (DOC-001 p4); the plan identifies age/NIHSS/time/core adjustment and omission of the subgroup-defining variable. These are model-based RRs. Raw ratios are diagnostic only; no covariance, fit, degrees of freedom or individual effect-test definition is inferred. No noninferiority/equivalence margin or subgroup stopping/multiplicity-adjusted decision is stated here. The exploratory two-sided .05 rule/no-multiplicity adjustment in DOC-001 p4 is internally coherent with the printed interaction decisions. Trial-design/plan discrepancies and the other forest figures are separately assigned.

### F-ST1-101

**Title:** Finite risk ratios and intervals for two all-zero outcome subgroups lack a reconciling estimation step.

**Relationships:** S1001 (eFigure7 ASPECTS0-2,mRS0-2) and S1017 (eFigure8 ASPECTS0-2,mRS0-3). Same subgroup and repeated estimation issue, consolidated into one finding.

**Exact source locations and roles:**
- REPORT DOC-006 physical p13,printed folio12,[eFigure7](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=13),ASPECTS0-2(n=19) row: Thrombectomy0(0.00%),Medical Management0(0.00%),Relative Risk(95%CI)1.00(0.37-2.72),with finite point/interval drawn on the forest.
- REPORT DOC-006 physical p14,printed folio13,[eFigure8](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=14),same ASPECTS0-2(n=19) row: Thrombectomy0(0.00%),Medical Management0(0.00%),Relative Risk(95%CI)1.00(0.37-2.72),again drawn as finite.
- REPORT DOC-001 physical p4,printed753,[Statistical Analysis](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4): secondary-outcome EVT treatment effects “within individual subgroups” evaluated with modified Poisson regression and robust standard errors. The same page states randomized allocation for treatment effects across imaging strata,no imputation.
- PLAN DOC-005 physical p4,[§5.2 items2-3](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=4),and item3 continuationp5: modified Poisson robust-standard-error models for mRS0-2/0-3,prognostic covariates; logistic fallback specifically for marginal probability plots. This corroborates the named regression method rather than contradicting a report element.

**Printed values compared:** Zero successes in each treatment arm for each endpoint,against a finite pointRR1.00 and two finite95%limits0.37/2.72 under the stated within-individual-subgroup regression. Counts are identical between the two outcomes because no ASPECTS0-2 participant achieved either threshold. Source-matched arm sizes are11EVT/8MM; they are corroborating denominator context,not needed to establish all19outcomes zero. Other sparse rows print an asterisk rather than a finite RR (eFigure7 core≥150mL and no≥1.2/10mL mismatch,eFigure8 core≥150mL); the figures do not explain a zero-event estimation rule.

**Rule and reproduced logical calculation:** In the stated ordinary within-subgroup modified Poisson fit,an all-zero response supplies no finite likelihood-based treatment-risk contrast. For a usual unrestricted fitted intercept,the Poisson log likelihood for this subgroup is L = -sum_i exp(eta_i). Decreasing the intercept increases L toward its supremum0 for every finite treatment coefficient; there is no finite intercept maximizer and no uniquely determined finite treatment RR/robust uncertainty from this all-zero subgroup. Covariate adjustment changes eta_i but supplies no positive outcome information. Robust standard errors change the uncertainty calculation,not the absence of an ordinary finite fit. This is a logical check of the named method,not a crude-ratio comparison and not a diagnostic substitution of a preferred model. The source does not state a constraint,penalty,continuity adjustment,pooling of subgroup risks,or another procedure supplying the missing finite estimation step. The finite printed values consequently do not reconcile with the provided within-subgroup method description without an additional definition.

**Display precision:** Integer count0 is exact; its half-unit interval contains no other admissible nonnegative integer. The printed RR interval is[0.995,1.005],the lower limit[0.365,0.375],and the upper limit[2.715,2.725]. Every permitted printed reading remains a finite estimate and finite interval alongside all-zero outcomes. The rule compares existence/identifiability of a finite model result,not two numerical copies; a recomputed finite RR interval and relative numeric discrepancy are not defined and must not be invented. Rounding does not supply the absent estimation step.

**Focus area:** C,statistical method logic.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_C,with All relationships S_C,S_W. The main-report model description is compared with the results-supplement rows; the zero counts versus finite estimates also conflict within the results supplement. PLAN corroboration is not P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The two90-day ASPECTS0-2 functional-independence/independent-ambulation treatmentRRs1.00 with95%CIs0.37-2.72. A data extractor could take these as finite,estimable subgroup treatment effects with finite uncertainty; interpretation differs if the displayed values are placeholders or derive from another,undisclosed estimator.

**Why context does not resolve it:** B1 applies because the stated analysis has a missing estimation step tied to two printed inferential results. B2 applies because neither the caption,figure nor supplied within-subgroup model description identifies how all-zero outcomes yield the finite point and interval; the nearby asterisk handling does not identify the procedure. B3 applies because both the result and its finite uncertainty are available for extraction. This is more than an absent generic model detail: the zero outcomes and finite model result directly conflict under the analysis as described.

**Source-grounded alternatives and precise missing definitions:** The RRs may derive from a constrained/regularized or pseudo-observation procedure,from a pooled model or marginal prediction that borrows data outside this subgroup,or may encode a plotting/reference placeholder. These are alternative explanations only,not asserted facts or recommended analyses. Need the actual subgroup fitting/prediction procedure,any zero-event treatment,its fitted population/constraints,and the confidence-interval/variance construction. The interaction Ps.9055/.6788 are separately printed tests and are not treated as the effect Ps; their degrees of freedom and treatment of the all-zero stratum remain undefined.

**Exact human question:** Which estimation procedure and zero-event handling produced RR1.00(95%CI0.37-2.72) for the ASPECTS0-2 strata in eFigures7/8 when both treatment arms have zero outcomes,and what fitted comparison and uncertainty do those finite values represent under the reported within-subgroup modified Poisson analysis?

## Excluded observations

Only apparent issues actually considered and not emitted are listed; reconciled containment,direction,count and interaction checks are not exclusions. Neither row below covers the all-zero finite-estimate pattern in F-ST1-101.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p14/eFigure8,no≥1.2/10mL mismatch row (S1029),with the same comparison limitation across nonzero forest rowspp13-15 | Diagnostic crudeRR from2/8EVT vs4/21MM is1.3125,whereas the forest RR is5.99(0.76-47.33). The source's adjusted/model-based regression supplies the contrast; this is not a stated crude estimate. Covariates and robust covariance are absent. The difference alone does not establish that the reported estimator fails to reproduce,so it is not routeA category4. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 pp13-15/eFigures7-9,especially p13core≥150/no≥1.2/10mL mismatch andp14core≥150asterisks (S1012,S1013,S1028); p13core150/mismatch≥1.2 andp14core150unprinted interaction slots (S1053,S1054,S1060); remaining finite interaction testsS1049-S1069except these missing slots | Asterisks and three missing interaction values have no estimate/test or estimation explanation; interaction-statistic/degrees-of-freedom/covariance definitions are absent. No contradictory finite value or subgroup inferential-decision claim is supplied at these locations. These omissions are recorded rather than supplied by convention. Planned-analysis reporting status is a separately assigned design scope,not inferred from these blank cells alone. | CONDITIONAL_OR_UNREPORTED |

## Limitations and completion

Coverage complete for the disjoint69relationships. Reproduction limits: source does not give individual model covariates/covariance/coefficient standard errors or interaction statistics/degrees of freedom; three asterisks and three absent interaction-test slots cannot be numerically reconstructed. The finite all-zero pattern is grounded in exact source counts,printed RR/CI,and the supplied model statement,not in missing raw data alone. No other qualifying observation arose in this scope. Statistical pass2 requires a different fresh high agent and the completed ledger,screening and mechanical recheck; this agent has performed only pass1.

