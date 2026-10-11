# Statistical pass 1 — main REPORT

Runtime agent: `/root/stat1_main`; fresh `gpt-6.1-sol` at `high`. Exact assigned scope: every DOC-001 main-report estimate, interval, interaction P, narrative test, and report statistical-method logic, physical PDF pp.1–14. Supplemental rows and PLAN logic are assigned to other disjoint shards. Scope and 1.6.2 review contract read completely. 72 relationships S001–S072 all receive PASS_1_COMPLETE in statistics/parts/main.md and the initial canonical statistical inventory. One consolidated finding and six excluded observations. Scientific source authority is the supplied main PDF; source-linked extracted text is a locator/transcription aid. No candidate IDs assigned.

## Complete checks

All Figure1 ordinal effect rows (16), its7 interaction tests, all16 Table2 arm-specific estimates across8 covariate/outcome rows and8 interaction tests, all Table3 printed aGenOR/aRR/aRD estimates across8 contrast/outcome records and7 printed interaction tests, all remaining narrative associations, trend tests, predictions, population/model definitions and decision rules are covered. Point containment, endpoint order and effect direction reconcile except the interval/significance pattern below. Interaction P values are never treated as individual-effect P values. Narrative descriptive IQRs are never treated as effect CIs. The report specifies two-sided tests, P<.05,95%CI and no exploratory multiplicity adjustment; no noninferiority/equivalence margin exists in this main source. No test statistic or numeric standard error is printed in main results. The report’s stopping boundary is not numerically specified; supplied PLAN rules are reviewed separately. No main-source sample-size inputs permit standalone power reproduction.

### F-ST1-001

**Title:** Printed confidence intervals end at the ratio null while the narrative calls the corresponding associations statistically significant.

**Relationship IDs:** S024 and S062. One repeated pattern, two affected prognostic associations.

**Exact compared locations and document roles:**

- REPORT DOC-001, [physical PDFp.6, printed755, lower-left Association of ASPECTS paragraph continuing upper-right](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6): in multivariable models without adjustment for volumetric measures, decreasing ASPECTS was associated with “significantly worse clinical outcomes” within EVT-treated patients; aGenOR0.91(95%CI0.82–1.00) per1-point ASPECTS decrease. REPORT same document [p.7, Table2 ordinal-ASPECTS EVT row](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7) reproduces 0.91(0.82–1.00); [p.1 abstract](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1) repeats it without the significance qualifier. The interval and significant claim are compared within the p.6 paragraph; p.1/p.7 corroborate the printed interval, rather than constitute different document relationships.
- REPORT DOC-001, [physical PDFp.10, printed759, upper-left Association of Age and Time paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10): CTP acquisition to reperfusion/endprocedure aRR0.97(95%CI0.93–1.00) per10-minute increment; the predicted probability of independent ambulation “significantly decreased.” That phrase applies jointly to increasing age and this imaging-time estimate. Age0.97(0.96–0.99) does not show this pattern and is not an affected interval.
- REPORT DOC-001, [physical PDFp.4, printed753, Statistical Analysis last paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4): all hypotheses evaluated by two-sided tests; P<.05 considered significant; analyses exploratory with no multiple-comparison adjustment.

**Printed values/statements:** ASPECTS aGenOR0.91,95%CI[0.82,1.00],significantly worse; imaging-time aRR0.97,95%CI[0.93,1.00],significantly decreased. No numeric individual-effect P is printed for either in main. The interactionP=.83 in Table2 is a separate heterogeneity test and is not the comparator for ASPECTS significance.

**Rule and calculation:** At the printed95%CI level and stated two-sided.05 decision rule, each ratio interval includes null1 at its upper endpoint:0.82≤1≤1.00 and0.93≤1≤1.00. The narrative states statistical significance for the same corresponding association. These are interval-versus-stated-test/significance conflicts under the literal printed intervals; the point estimates are contained and the interval order is coherent. No distributional, covariance or conventional-SE reconstruction is assumed.

**Display precision:** The source prints upper1.00 for both. A half-unit representation would cover[0.995,1.005), which could include an underlying limit below1; such an underlying value is an alternative interpretation below. Under QUALITY_CONTROL_SCOPE RouteA category1, an interval-versus-test conflict is never screened as rounding. No relative-discrepancy threshold is applied to this category, and no hidden endpoint is substituted for the printed1.00.

**Focus area:** B, estimate and test logic.

**Proposed review domain:** `statistical_results`.

**Proposed relationship type:** `S_W`; all relationships `S_W`; compared roles REPORT versus REPORT within DOC-001. The p.4 rule and p.6/p.10 estimate/significance statements are report material; no PLAN is in conflict in this finding.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The statistical significance attached to aGenOR0.91 per1-point ASPECTS decrease in EVT-treated patients, and to aRR0.97 per10-minute imaging-to-reperfusion/endprocedure increase for independent ambulation. A reader extracts intervals reaching1 while the narrative attaches significance.

**Why context does not resolve it:** RouteA category1 requires registration of a reproduced interval-versus-stated-test conflict. The p.6 and p.10 statements attach significance directly to the estimates/intervals. Their printed endpoints do not display exclusion of1. Context identifies the associations but does not provide their exact P values or unrounded confidence limits.

**Source-grounded alternatives and missing definitions:** The underlying upper confidence limit may be below1 and round to1.00. The significant test may use a different inferential procedure from the printed confidence interval; PIM and modified Poisson models are stated, but their exact effect tests and unrounded limits are not supplied here. The narrative could refer to another adjustment or marginal-probability analysis; p.6 says no volumetric adjustment and gives this same estimate, whereas p.10 describes a predicted probability and references eFigure18. These alternatives require the unrounded upper limits, numeric two-sided effect P values, and exact test/interval procedure and mapping to the cited analyses. No alternative is treated as a resolved human disposition.

**Exact human question:** What are the unrounded95% upper confidence limits and the corresponding two-sided effect P values for these two associations, and which test/interval procedure supports the narrative significance statements when the printed intervals end at1.00?

**Direct source confirmation:** Poppler direct text pp.6/7/10 agrees with the reusable extraction. Reused main p.6 image visually confirms ASPECTS paragraph and1.00. Fresh direct rendering of main p.10 visually confirms both imaging-time1.00 and “significantly decreased.” No OCR-only finding.

## Excluded observations

Each row is one apparent observation that was considered and self-screened out; reconciled checks are retained in S records. These rows receive no finding IDs. Missing definitions are named rather than replaced by conventional assumptions. Pass2 must revisit them against always-register categories.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp.6–7 and9, aRR expansion/footnote |The expansion “absolute risk reduction” appears alongside positive ratio-scale estimates, multiplicative intervals, and a footnote explicitly saying aRR>1 means a higher rate ratio. The intended ratio reading is identifiable at once; no printed numerical value changes. The footnote’s “with endovascular thrombectomy” is read with the explicit within-arm column/reference structure, rather than as a separate treatment contrast.|TERMINOLOGY_OR_WORDING|
| REPORT DOC-001 p.9 Table3, mismatch counts versus adjusted effects |Examples: definitionB EVT independence crude ratio(28/111)/(6/59)=2.480...,versus printed adjustedaRR1.20; definitionB EVT dependence/death crude risks46/111 vs31/59 decrease while adjustedaRR1.18>1. The model explicitly adjusts age,NIHSS,time andcore. These are modeled associations, not printed crude estimates; crude recomputation does not test their stated method.|MODEL_VERSUS_CRUDE|
| REPORT DOC-001 p.7 Table2, core/ambulation interactionP=.25;S029/S037 |Both arm-specificaRR point estimates print0.91,withCIs[0.87,0.95] and[0.85,0.98]. Diagnostic only: assuming independent identical-estimand log-Wald arm estimates, SEs≈0.02244/0.03631 giveP≈1; allowing all inputs half-unit precision yields maximum diagnostic absolute z≈0.283 and minimumP≈.777. The source does not establish that its treatment×core interaction coefficient equals the difference of these separate-arm model coefficients, nor name the contrast/df/covariance/common-nuisance fit. No independent-Wald method reproducing the same display is established. Thus the diagnostic is conditional,not a reproduced interval-versus-own-test conflict.|CONDITIONAL_OR_UNREPORTED|
| REPORT DOC-001 p.9 Table3, definitionB dependence/death interactionP>.99;S047/S054 |Diagnostic only: independent log-Wald comparison ofaRR1.18[0.82,1.70] andaRR1.05[0.79,1.38] givesSEs≈.18599/.14230,z≈.49844,P≈.618. The printedP>.99 is an interaction,whose RR-versus-RD scale,contrast,model coefficient mapping andcovariance/testdf are not printed. This calculation does not reproduce the stated interaction method for other rows,so cannot establish a source conflict.|CONDITIONAL_OR_UNREPORTED|
| REPORT DOC-001 p.9 Table3, definitionA MM independence;S041 |Printed adjustedaRR1.01 andadjustedaRD−0.001 have opposite tiny point directions. Main methods state modifiedPoisson for secondary outcomes and predictedmargins,without specifying howaRD is generated or whetherboth estimands derive from one common pair ofadjustedprobabilities. Bothintervals include null. A direction contradiction follows only if that unreported mapping is assumed; no printed number is reconstructed or changed.|CONDITIONAL_OR_UNREPORTED|
| REPORT DOC-001 pp.3–4 PIM covariate-direction prose;pp.1,6–7 |PIM prose refers to higher values of the covariate of interest while ASPECTS associations are per1-point decrease. Immediate scale labels in narrative/Table2 define the covariate as a decrease and core as an increase; direction is readable without reversing any printedestimate. No proposed alternative analysis.|CONTEXT_RESOLVES|

The diagnostic independence calculations are arithmetic aids, not reconstructions of the reported fitted interaction. For ratio rows with no numeric effect P, log-symmetry is not used to infer a missing SE/test or to create a finding.

## Provenance and limitations

Direct text authority checks used `pdftotext -layout -f N -l N source.pdf -` for main pp.1,6–10; Poppler26.01.0. Source-matched reusable layout and fresh complete mapper supply other main locations. Reused image p.6 inspected. Rendering: `pdftoppm -f 10 -l 10 -singlefile -scale-to 2000 -png jama_sarraj_2024_oi_240006_1708623114.96234.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1_main/page-10`; enginePoppler26.01.0,deviceCPU; output preprocessing/stat1_main/page-10.png. NoPython/OCR/network/external literature or oldcandidate/checker/report inputs. Sources and prior assets preserved. Missing test/contrast definitions limit exact interaction/trend reproduction; there is no uncovered main inferential unit. Full package coverage requires the separate supporting/PLAN shards and a fresh statisticalPASS2agent.
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
- REPORT DOC-006 physical p13,printed folio12,[eFigure7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=13),ASPECTS0-2(n=19) row: Thrombectomy0(0.00%),Medical Management0(0.00%),Relative Risk(95%CI)1.00(0.37-2.72),with finite point/interval drawn on the forest.
- REPORT DOC-006 physical p14,printed folio13,[eFigure8](../../../joi240006supp5_prod_1708623115.01733.pdf#page=14),same ASPECTS0-2(n=19) row: Thrombectomy0(0.00%),Medical Management0(0.00%),Relative Risk(95%CI)1.00(0.37-2.72),again drawn as finite.
- REPORT DOC-001 physical p4,printed753,[Statistical Analysis](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4): secondary-outcome EVT treatment effects “within individual subgroups” evaluated with modified Poisson regression and robust standard errors. The same page states randomized allocation for treatment effects across imaging strata,no imputation.
- PLAN DOC-005 physical p4,[§5.2 items2-3](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4),and item3 continuationp5: modified Poisson robust-standard-error models for mRS0-2/0-3,prognostic covariates; logistic fallback specifically for marginal probability plots. This corroborates the named regression method rather than contradicting a report element.

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

# Statistical pass 1: forest B

- Runtime agent identity: /root/stat1_forest_b
- Model/effort: gpt-6.1-sol/high
- Start mode: FRESH_SPAWN
- Exact assigned scope: DOC-006 physical pp16-19,eFigures10-13,A031-A034;64 effect/CI rows and32 interaction tests.
- Relationship IDs: S2001-S2096; every record PASS_1_COMPLETE.
- Findings:1,F-ST1-201. Excluded apparent observations:3. Scientific coverage gaps:0.
- Relationship artifact: statistics/parts/forest_b.md.
- Sources and reused evidence preserved; no web, old candidate conclusions or unapproved extraction helpers used.

The complete scope and review contract were read. All four forest source-linked images were read visually, with direct PDF text establishing captions and directly read main-report/current-analysis-SAP methods supplying adjustment, endpoint and test context. Every printed point estimate is inside its95%CI and all interval endpoints are ordered;64/64 containment checks reconcile. Interaction P values were treated as tests of treatment heterogeneity, never as individual row-effect P values. No superiority, noninferiority, equivalence or stopping claim is made by these displays. Numeric findings are restricted to reproduced source observations; no adjusted RR is replaced by a crude ratio.

### F-ST1-201

**Title:** eFigure13 direction annotations reverse the interpretation of the printed complete-dependence/death relative risks.

**Exact compared locations and document roles:** REPORT [DOC-006 physical p19,eFigure13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19), title (“complete dependence or death(mRS5-6) at90-day follow-up”), column “Relative Risk(95%CI),” both treatment-event columns, all16 plotted rows, and bottom axis “Relative Risk of achieving mRS5-6(95%CI) in Thrombectomy group compared to Medical Management group.” On that same axis, the left side is labeled “Favours Medical Management” and the right side “Favours Thrombectomy.” The comparison is entirely within this REPORT page. [REPORT main article p3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) identifies mRS5-6 as complete dependence or death; it corroborates endpoint identity without being a second side of the discrepancy.

**Printed values and affected locations:**

| S ID | eFigure13 row | Printed EVT event count(percent) | Printed MM event count(percent) | Printed relative risk(95%CI) |
|---|---|---|---|---|
| S2049 | 1: NCCT<70 (N=132) | 27(39.71) | 39(60.94) | .68(.49-.95) |
| S2050 | 2: NCCT≥70 (N=204) | 49(49.00) | 63(60.58) | .77(.62-.97) |
| S2051 | 3: largest<70 (N=80) | 14(33.33) | 17(44.74) | .82(.49-1.37) |
| S2052 | 4: largest≥70 (N=256) | 62(49.21) | 85(65.38) | .72(.60-.88) |
| S2053 | 5: NCCT<100 (N=207) | 37(35.92) | 60(57.69) | .61(.46-.81) |
| S2054 | 6: NCCT≥100 (N=129) | 39(60.00) | 42(65.62) | .87(.69-1.10) |
| S2055 | 7: largest<100 (N=165) | 26(32.50) | 44(51.76) | .62(.44-.86) |
| S2056 | 8: largest≥100 (N=171) | 50(56.82) | 58(69.88) | .78(.64-.96) |
| S2057 | 9: NCCT<150 (N=297) | 69(45.70) | 85(58.22) | .76(.62-.93) |
| S2058 | 10: NCCT≥150 (N=39) | 7(41.18) | 17(77.27) | .55(.33-.94) |
| S2059 | 11: largest<150 (N=273) | 59(43.70) | 78(56.52) | .72(.58-.90) |
| S2060 | 12: largest≥150 (N=63) | 17(51.52) | 24(80.00) | .69(.48-.97) |
| S2061 | 13: largest profile ratio≥1.2/volume≥10:0 (N=74) | 12(35.29) | 23(57.50) | .67(.41-1.10) |
| S2062 | 14: largest profile ratio≥1.2/volume≥10:1 (N=262) | 64(47.76) | 79(61.72) | .74(.61-.90) |
| S2063 | 15: largest profile ratio≥1.8/volume≥15:0 (N=211) | 50(45.05) | 61(61.00) | .76(.60-.95) |
| S2064 | 16: largest profile ratio≥1.8/volume≥15:1 (N=125) | 26(45.61) | 41(60.29) | .71(.53-.97) |

**Rule and reproduced calculation:** For the printed adverse outcome and printed contrast, RR=risk(mRS5-6|EVT)/risk(mRS5-6|MM). Values below1 correspond to less complete dependence/death with EVT; values above1 correspond to more of that outcome with EVT. All16 printed point estimates are below1, with RR ranging.55-.87, but each lies on the axis side labeled as favoring medical management. For example, row1 prints RR.68(.49-.95), EVT27(39.71%) and MM39(60.94%); its modeled RR shows lower adverse-outcome risk with EVT, while the side annotation assigns that region to medical-management benefit. Descriptive arm proportions also have the same lower-risk direction, but no crude proportion ratio is substituted for the adjusted RR.

**Display-precision calculation:** This is a categorical reversal of the direction attached to an explicitly printed risk contrast, rather than disagreement between two numeric copies. No recomputed numeric interval or relative numeric discrepancy applies to the label itself. The direction is nevertheless invariant to half-unit rounding: row1 printed RR.68 permits [.675,.685], wholly below null1; all16 printed points have upper half-unit limits at most.875, also below1. Thirteen printed CIs are wholly below1; the other three contain1, but their point estimates still share the direction mismatch. The issue is the direction label, not significance claimed for those three intervals.

**Focus area:** B, estimate and test logic; agreement between estimate, endpoint and direction annotations.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W. **All relationships:** S_W. **Compared document roles:** REPORT vs REPORT within DOC-006 p19. Main-method text only corroborates the adverse-outcome definition and is not an additional comparison relationship.

**Qualifying route:** Route A, category2.

**Affected result or extracted value:** The EVT-versus-MM interpretation of every eFigure13 relative risk for complete dependence or death at90days, including.68(.49-.95) for NCCT<70mL and.55(.33-.94) for NCCT≥150mL. A reader using the figure's printed favor annotations could assign the direction of these estimates to the opposite treatment.

**Why context does not resolve it:** Route A category2 requires registration of a reproduced direction statement that reverses printed values. The title and axis identify an adverse-outcome RR in EVT relative to MM, while the favor labels identify the lower-risk region as favoring MM. Immediate counts make the lower-event-rate arm identifiable but do not remove the opposite interpretation explicitly printed on the axis.

**Source-grounded alternatives and missing definitions:** The side annotations could have been carried over from desirable-outcome forests; that production mechanism is not inferred as fact. Alternatively, the annotations might be intended for avoiding mRS5-6, or the reciprocal MM/EVT contrast, but the printed title, count columns and axis identify achieving mRS5-6 and EVT relative to MM. Those alternative readings would require a different stated outcome or contrast. No raw-data or covariance definition is needed to reproduce this categorical inconsistency.

**Exact human question:** Which outcome direction and treatment contrast should a reader use when interpreting the “Favours Medical Management” and “Favours Thrombectomy” annotations in eFigure13, given the printed EVT/MM risk of complete dependence or death and the16 relative risks below1?

**Human review status:** Pending Human Adjudication.

## Excluded observations

Only apparent issues decided against emission are listed; reconciling checks are retained in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Printed adjusted RR.12(.01-1.05) contrasts with a crude ratio from1/17 versus1/22, equal to22/17=1.2941. The stated modified Poisson model adjusts prognostic variables, so crude direction and magnitude do not reproduce its adjusted estimate. The missing fitted coefficients cannot establish a conflicting adjusted calculation. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 p17,eFigure11,NCCT≥150mL,S2026 | Log-center diagnostic sqrt(.01×1.05)=.10247 differs from printed.12. Allowing endpoint half-unit intervals [.005,.015] and[1.045,1.055] gives a geometric-center interval [.072284,.125797], overlapping the point's[.115,.125]. Display-precision gap0; relative discrepancy0. This diagnostic does not assume the CI method as final authority. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-006 p16,eFigure10,NCCT150 interaction,S2069 with effect rowsS2009-S2010 | A diagnostic independent-normal reconstruction from GenOR1.70(1.33-2.19) and2.21(1.16-4.19) yields SE of log-difference≈.35146,z≈.74650,two-sided P≈.455, whereas printed interactionP=.8886. This diagnostic assumes independent subgroup estimates and a common log-Wald test; the source supplies neither that covariance nor the interaction coefficient/test statistic. It is not a method shown to reproduce the other interaction rows of this display. | CONDITIONAL_OR_UNREPORTED |

The final exclusion does not remove any interval-versus-own-P conflict: the printed P is explicitly an interaction test, not the P of either subgroup's treatment effect. Subgroup effect CIs do not establish the fitted interaction covariance or test. No Route A category4 observation has been reproduced by a method reproducing the other rows.

## Limits and handoff

Exact adjusted-model estimate/CI regeneration and exact interaction P regeneration require D1/D2 inputs named in the relationship inventory; their absence is documented without treating it as a conflicting printed result. No missing input blocks interval containment, endpoint ordering, endpoint/reference identity, within-display percentages, or source-defined direction checks. All96 assigned relationships are complete for pass1. Pass2 must be a distinct fresh high-effort statistical agent and revisit every ID together with the full ledger, screen and mechanical recheck; this agent has not assigned any stable candidate IDs or adjudication.

Artifact paths: statistics/parts/forest_b.md and checkers/statistical_parts/pass1_forest_b.md.

# Statistical pass 1: remaining A

Fresh runtime ID root/stat1_remaining_a; gpt-6.1-sol/high. Scope: DOC005 all7pages and DOC006pp1-12/20-32, with main method/matched-result context. 78 stable relationships S3001-S3078 are recorded in statistics/parts/remaining_a.md, all PASS_1_COMPLETE. Findings:6. Excluded apparent observations:8. Assigned scientific gaps:None. Sources/derivatives preserved; CPU direct Poppler26.01.0 text checks and reused source-linked image inspection. Exact graph coefficients/pointwise coordinates, trend bin denominators/test algorithm and individual graph-model calibration choices remain absent. These limits do not prevent the completed direction, endpoint, test-label, method and design checks.

Full-source counterpart lookup for S3011/S3016 was independently supplied by the complete REPORT reviewer in checkers/cross_source_parts/reports.md, section Requested bounded REPORT-counterpart confirmation. That handoff is factual location/absence evidence; this statistical shard independently applies the inclusion threshold. Main mRS distribution is primary (abstractp1); independent ambulation is a secondary outcome (mainp3), not identified as key secondary and not separately reported in the abstract.

## Findings

### F-ST1-301

**Title:** EVT continuous mismatch-volume probability directions differ between narrative and cited curves.

**Compared locations and document roles:** REPORT main [physicalp8, mismatch paragraph spanning both columns](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8), REPORT results supplement [physicalp23, eFigure17A/B and legend](../../../joi240006supp5_prod_1708623115.01733.pdf#page=23). Relationships S3042/S3043; source mapping M110/A038. Proposed relationship type S_C; all relationships S_C.

**Printed values/statements:** Main: as mismatch volume increased, marginal probability of functional independence and independent ambulation increased for EVT but decreased for MM, citing eFigure17. Both cyan curves in eFigure17A(mRS0-2)/B(mRS0-3) decrease as the x-axis Mismatch Vol(mL) increases; salmon MM curves also decrease. The legend explicitly names cyan EVT. Positive mismatch ticks0/100/200/300/400 increase left to right.

**Rule and calculation:** A positive EVT probability association in the narrative and a negative EVT curve direction for the same predictor/outcomes do not reconcile. Across any two well-separated positive mismatch ticks, the rightward EVT curve ordinate is smaller. This reproduces the direction comparison, without treating approximate graph ordinates as printed fitted estimates. Half-unit numeric intervals and relative discrepancy are inapplicable to a discrete direction conflict; no exact fitted values are fabricated. The two outcomes form one repeated direction pattern.

**Focus area:** B. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Direction of the EVT continuous mismatch-volume association with predicted90-day independence/ambulation.

**Why context does not resolve it:** Always-register direction reversal applies. Main text cites these exact panels, with no different predictor/model specified. Binary mismatch-presence associations are distinct contrasts and cannot determine the continuous curve slope.

**Alternatives and missing definition:** Narrative or plotted predictor/curves could correspond to a different intended fitted model; no supplied text identifies that alternative. Graph coefficients and reference covariates are absent, but absence is not the basis of the finding.

**Exact human question:** Which EVT continuous mismatch-volume probability direction was intended, and how should the increasing narrative reconcile with the decreasing curves in eFigure17A/B?

### F-ST1-302

**Title:** Core measurement underlying age/time prediction surfaces is unclear across figure captions and narrative.

**Compared locations and document roles:** REPORT results [physicalp24, eFigure18 title/explanation and70/100/150mL panels](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), REPORT results [physicalp25, eFigure19 title/explanation and70/100/150mL panels](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25); REPORT main [physicalp10, Association of Age and Time paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10), [physicalp3, composite definition](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3). Relationships S3046-S3051; mapping A039/A040/M115/M116. Proposed relationship type S_C; all relationships S_C,S_W.

**Printed values/statements:** eFigure18 title says CTP/MRI core fixed70,100,150mL; following prose calls those values composite core. eFigure19 title and prose say composite core fixed70,100,150mL. Main paragraph describes both referenced figures and says estimated CTP/MRI core volumes were set70,100,150mL. Main defines composite=max(CT hypodensity,CTP/MRI core), a distinguishable measurement.

**Rule and calculation:** Conditioning a probability surface on70/100/150mL of a perfusion/diffusion measurement does not identify a surface conditional on70/100/150mL of a maximum of two measurements. The displayed number settings are equal but the conditioning quantity differs. Half-unit numeric intervals and relative discrepancy are inapplicable to model-variable identity; no numerical fitted prediction is invented or recomputed.

**Focus area:** C. **Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** The core-volume measurement that defines each EVT independent-ambulation surface and the reported150mL prognosis.

**Why context does not resolve it:** B1: conflicting predictor identity prevents identification of which analysis produced the fitted result. B2: eFigure18 itself supplies competing measurement names; eFigure19 conflicts with the common main description. B3: a reader applying the predicted probabilities to a150mL imaging estimate must know which numerical measurement is intended. The generic panel heading Core Volume does not select either measurement.

**Alternatives and missing definition:** One figure might use perfusion/diffusion and the other composite; both may use composite; explanatory text may name a different fitted model. None is selected. A fitted covariate list identifying the actual core variable for each surface is missing.

**Exact human question:** Which core-volume variable was used in each eFigure18/19 model, and which measurement underlies the70/100/150mL values in the main narrative?

### F-ST1-303

**Title:** Planned all-as-treated primary treatment comparison is reported using randomized allocation.

**Compared locations and document roles:** PLAN analysis SAP [physicalp3,5.1 Principles](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3), [physicalp4,5.2.1 ordinal analysis](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4); REPORT main [physicalp4,Statistical Analysis population paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), [physicalp6,Figure1 and footnote](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6); REPORT results [physicalp8,eFigure3 allocated/received populations](../../../joi240006supp5_prod_1708623115.01733.pdf#page=8). Relationships S3006/S3008/S3022. Proposed relationship type P_R; all relationships P_R.

**Printed values/statements:** SAP says all analyses will use an as-treated approach; specifies90-day mRS PIM analyses. Main methods explicitly use randomized groups when evaluating treatment association across imaging strata, and received groups for within-treatment associations. Retained allocated arms168/168 differ from received arms170/166 because2 MM patients received EVT. Figure1 primary mRS comparisons use allocated treatment groups.

**Rule and calculation:** A planned as-treated primary comparison and a reported allocated-treatment comparison use different treatment attribution. Arm changes are EVT170-168=2 andMM168-166=2; the substantive comparator is the explicit allocation rule, not a rounding discrepancy. No statistical effect is recomputed from crude counts. Display-precision intervals and relative discrepancy are inapplicable to analysis-population definition.

**Focus area:** D. **Proposed review domain:** protocol_report.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned versus reported treatment-assignment estimand for primary90-day mRS treatment effects across imaging strata.

**Why context does not resolve it:** A planned primary as-treated comparison is replaced by allocated-treatment reporting. Main explains the actual convention clearly, but the supplied analysis SAP has no corresponding amendment limiting all-as-treated to within-arm models. It remains a planned-versus-reported analysis relationship, without judging the methodological choice.

**Alternatives and missing definition:** A subsequent amendment may have separated treatment-effect and prognostic populations; supplied post hoc appendix does not state such a change. As-treated within-arm estimates are not the same as the planned primary across-treatment comparison. Which supplied plan/amendment governs that comparator is the remaining definition.

**Exact human question:** Which planned treatment-assignment rule applies to the primary imaging-stratified treatment comparisons, and how does the all-as-treated SAP reconcile with randomized-allocation reporting?

### F-ST1-304

**Title:** Core-volume primary/sensitivity hierarchy and prespecification differ between SAP and report.

**Compared locations and document roles:** PLAN SAP [physicalp3,Imaging definitions,primary/sensitivity bullets](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3), [physicalp7,AppendixI,item1](../../../joi240006supp4_prod_1708623115.00733.pdf#page=7); REPORT main [physicalp4,post hoc sensitivity statement](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), [physicalp1,primary outcome measurement and core-strata results](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1), [physicalp6,Figure1](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6); REPORT results [physicalp16,eFigure10 composite comparisons](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16). Relationships S3004/S3018; graphS3038-S3041 corroborates actual composite variable but is not a separate mismatch.

**Printed values/statements:** SAP primary analysis uses larger of perfusion/diffusion and hypodensity; perfusion/diffusion-only is sensitivity. Appendix identifies composite as prespecified, adds CT hypodensity as third estimate post hoc. Main presents perfusion/MRI core as the principal volume basis for primary mRS results and calls composite/hypodensity analyses post hoc sensitivities. Composite treatment effects are supplemental.

**Rule and calculation:** Composite=max(two measurements) and perfusion-only are distinguishable planned inputs; swapping which is primary/sensitivity and calling an explicitly prespecified composite analysis post hoc changes its planned analysis status. No arithmetic or fitted effect recalculation is needed. Half-unit numeric intervals/relative discrepancy are inapplicable to hierarchy/prespecification statements.

**Focus area:** D. **Proposed review domain:** protocol_report. Proposed relationship type P_R; all relationships P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Which volume-based90-day mRS analysis was primary and prespecified, versus sensitivity/post hoc.

**Why context does not resolve it:** The SAP specifically labels the volume choices primary and sensitivity; its appendix specifically says composite was prespecified. Reporting composite results somewhere does not reconcile their stated hierarchy and post hoc status. This does not assert that either volume definition is preferable.

**Alternatives and missing definition:** A later amendment or a distinction between a composite-primary analysis and a separately devised composite sensitivity could explain status. No supplied statement identifies such separate composite analyses or governing amendment.

**Exact human question:** Which core measurement and analysis hierarchy governed this prespecified primary imaging analysis, and how should the SAP composite-primary designation reconcile with the report's post hoc composite sensitivity description?

### F-ST1-305

**Title:** Planned mismatch-volume50/100mL primary outcome strata have no supplied report counterpart.

**Compared locations and document roles:** PLAN SAP [physicalp6,5.3.3 second/third bullets](../../../joi240006supp4_prod_1708623115.00733.pdf#page=6), [physicalp4,5.2.1](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4); REPORT main [physicalp6,Figure1 mismatch strata](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), [physicalp8,mismatch results](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8); REPORT results [physicalp23,eFigure17](../../../joi240006supp5_prod_1708623115.01733.pdf#page=23), [physicalp43,eTable7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=43). Complete supplied REPORT scope DOC001pp1-14,DOC006pp1-53,DOC002pp1-30,DOC007p1 was searched by the complete REPORT reviewer; factual counterpart handoff documented. S3016.

**Printed values/statements:** SAP: patients additionally stratified by mismatch volume thresholds50mL and100mL, with outcomes/treatment effect evaluated as5.2 specifies, including90-day mRS distribution. Reported mismatch strata use joint ratio/volume profiles1.2/10 or1.8/15. eFigure17 treats mismatch volume continuously. No50/100mL mismatch outcome strata appear in supplied REPORT material. Core-volume50/100mL bins or graph-axis ticks measure different quantities or are not analyses at those strata.

**Rule and calculation:** A continuous model or different joint mismatch-profile cutoffs do not report the specified categorical50/100mL mismatch-volume primary mRS comparisons. The planned outcome includes the main abstract's primary90-day mRS distribution, meeting the primary-analysis inclusion requirement. Half-unit rounding intervals/relative discrepancy are inapplicable to presence/absence and threshold identity;50 and100 are exact planned cutoffs.

**Focus area:** D. **Proposed review domain:** protocol_report. Proposed relationship type P_R; all relationships P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified primary90-day mRS treatment/outcome analyses by mismatch-volume50/100mL strata.

**Why context does not resolve it:** Always-register absent planned primary analysis applies. The complete source-linked REPORT counterpart search finds only different profile contrasts and continuous mismatch predictions. No supplied statement explains omitting or replacing the50/100mL strata.

**Alternatives and missing definition:** The comparisons may have been conducted but not supplied, or replaced by continuous or profile analyses. Human review must establish their reporting/status; no absence beyond the supplied package is claimed.

**Exact human question:** Where are the planned50/100mL mismatch-volume primary mRS analyses reported, or what supplied amendment/status explains their replacement or omission?

### F-ST1-306

**Title:** Planned age/time independent-ambulation prediction uses a different time origin from the supplied report surfaces.

**Compared locations and document roles:** PLAN SAP [physicalp5,5.2.3 predicted-probability bullet](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5); REPORT results [physicalp24,eFigure18](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), [physicalp25,eFigure19](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25); REPORT main [physicalp10,Age and Time results](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10). Complete REPORT counterpart search as documented above finds no age×LKW-to-randomization ambulation surface. S3011/S3046-S3051.

**Printed values/statements:** SAP specifies EVT predicted probability of independent ambulation combining age and time LKW-to-randomization. eFigure18 instead uses imaging acquisition-to-reperfusion/end procedure; eFigure19 uses LKW-to-reperfusion/end procedure. Main reports the first time association aRR.97(95%CI.93-1.00) per10min and the second1.00(.99-1.00), alongside differing significance descriptions. These values belong to different explicitly named predictors and are not directly compared as numerically conflicting estimates.

**Rule and calculation:** Randomization and reperfusion/end procedure are different time endpoints. An age×LKW-to-reperfusion surface does not identify the prespecified age×LKW-to-randomization model. Merely including LKW-to-randomization as an adjustment covariate elsewhere does not report its planned joint prediction surface. Half-unit numerical discrepancy does not apply to predictor identity; the printed aRR/CI checks remain main-shard relationships.

**Focus area:** D. **Proposed review domain:** protocol_report. Proposed relationship type P_R; all relationships P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The prespecified versus reported age/time predictor definition for EVT independent-ambulation probability, including the interpretation of treatment-delay-related prognosis.

**Why context does not resolve it:** B1: the scope's qualifying PLAN/REPORT comparisons explicitly include analysis specification and prespecified analyses, here a named time predictor for a fitted probability analysis. B2: the supplied plan and report name different time endpoints with no disclosed change for this prediction. B3: onset-to-randomization and onset/imaging-to-reperfusion express different timing quantities for applying these prognostic predictions. Independent ambulation is not established as key secondary, so this finding does not claim RouteA5 absent-key-secondary status; independent screening should decide this RouteB analysis-specification comparison.

**Alternatives and missing definition:** The reperfusion models may be added exploratory predictions rather than replacements, with the planned model unreported. The package lacks a status explanation linking the explicitly planned prediction to the reported surfaces. This is not a proposal to prefer one timing predictor.

**Exact human question:** Was the age×LKW-to-randomization ambulation prediction reported or replaced, and how do the supplied reperfusion-based surfaces relate to the specifically planned time predictor?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC005p3 mismatch-ratio wording versus REPORT mainp3/DOC006p5 | SAP says ratio 'of' core and hypoperfused volumes, but does not print core/hypoperfused equation. Field context, threshold>1 and report examples immediately identify conventional hypoperfused/core; no explicit numerical reverse equation was reproduced. | TERMINOLOGY_OR_WORDING |
| PLAN DOC005p3 ADC notation versus REPORT mainp2 | ADC unit/exponent typography differs; intended imaging threshold is identifiable from immediate imaging context and consistent threshold620, with no changed extracted result established. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC005p5,mRS5-6 descriptive bullet | Descriptive bullet says independent ambulation under the complete-dependence/death heading; neighboring model bullet explicitly gives5-6. Endpoint identity is immediately recoverable and no numeric outcome is misattributed. | TERMINOLOGY_OR_WORDING |
| REPORT DOC006pp10-12,eFigures5/6 | Trend algorithm, bin denominators, fitted coefficient and test statistic are absent. Comparing P to an unweighted bar slope or assumed trend test would depend on unsupported method inputs; no interval/test conflict is printed. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC006pp20-25,eFigures14-19 | Individual panel binary-model/logistic calibration choice, reference covariate distribution and coefficients are not stated. SAP permits logistic calibration fallback; absence alone does not contradict plotted values. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC006pp26-32,eFigure20a-aa versus PLAN DOC005p4 | Separate descriptive5/6 bars appear despite merged modeled ordinal outcome. Descriptive distributions do not establish that5-to6 shifts contributed to PIM/g-computation treatment success. | CONTEXT_RESOLVES |
| REPORT DOC006pp24-25,contour time axes | Time units are omitted from axes, while mainp10 explicitly describes increments in minutes and figures clearly name each time origin. The omission alone does not change a printed quantity or fitted result. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC006p9 68+33%;p12 28+73%,83+18%;eFigure20 rounded category totals | Integer-percentage totals101% are compatible with individual±.5-point rounding intervals, which include a100% total. These are not independent inferential tests. | ROUNDING_OR_DISPLAY_PRECISION |

## Completion

Findings F-ST1-301,F-ST1-302,F-ST1-303,F-ST1-304,F-ST1-305,F-ST1-306;78relationships;8excluded observations;no assigned scientific gap. Shared report direction/core-identity and PLAN allocation/hierarchy patterns may consolidate with other fresh checker findings during independent screening. Stable IDs remain for every relationship regardless of finding count. No candidate IDs or human dispositions assigned.
# Statistical pass 1 — eTables 3–7 shard

- Runtime ID: root/stat1_tables_a.
- Model/effort/start: gpt-6.1-sol / high / FRESH_SPAWN.
- Exact scope: REPORT DOC-006 eTables3–7, physical pp.39–44; fresh 115-relationship inventory S4001–S4115 in `statistics/parts/tables_a.md`.
- Findings: 1, F-ST1-401. Excluded apparent-observation groups: 5.
- Read QUALITY_CONTROL_SCOPE.md and the complete 1.6.2 review contract; direct source layout for all assigned pages and all six exact source-page images; supplied main statistical methods pp.3–4, eMethods p.4, and analysis SAP pp.4–7 as method context. No web or old conclusions used. Source and reused assets preserved. Compute device CPU.

All printed point estimates are within their ordered intervals; interval endpoints and direction align with their own measures. No row-specific effect P value is printed in eTables3–4. All eTable5 P values refer to interaction contrasts. eTable7 last-column values are treated as interactions by supplied main/SAP context, with locally absent headings preserved as a definition limit. The eTable7 P=.83 is not compared as a same-effect test with the MM RD interval. eTable6 composite modality minimizes both criteria and maximizes both binary AUCs, consistent with its stated preference rule. No assigned table supplies a margin, multiplicity, interim or stopping conclusion. Parameter-level exact replication is limited by absent raw fit output, numerical standard errors, covariance and RD confidence-procedure definitions; no unreported detail is assumed merely to obtain a finding.

## Findings

### F-ST1-401

**Title:** Composite mismatch MM complete-dependence/death result has different null-inference readings on its two adjusted scales without a defined analysis mapping.

**Compared locations and document roles:** REPORT DOC-006 [eTable7, physical p.43, ≥10mL/ratio≥1.2 composite mismatch, complete dependence or death (mRS5–6), MM effect-size cell](../../../joi240006supp5_prod_1708623115.01733.pdf#page=43): its aRR and aRD estimate/95%CI. REPORT DOC-006 [physical p.44 adjustment footnote](../../../joi240006supp5_prod_1708623115.01733.pdf#page=44) specifies age, NIHSS, last-known-well-to-randomization and CTP/MRI core volume adjustment. REPORT main article [physical p.4 statistical analysis](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4) provides binary modified-Poisson/robust-standard-error methods and two-sided P<.05 but does not identify the RD estimator or link its estimand/confidence procedure to this RR. The main methods corroborate model context; the compared inconsistency is within the one REPORT supplement.

**Relationship IDs:** S4095, S4096; S4097 is contextual interaction evidence, not the effect test. **Proposed relationship type:** S_W. **All proposed relationships:** S_W. **Focus areas:** B, C. **Proposed review domain:** statistical_results.

**Printed values:** In the MM column, no mismatch 23/40 (57.5%); mismatch78/126 (61.9%). Same effect-size cell prints aRR1.29 (95%CI0.93–1.79) and aRD0.168 (95%CI0.011–0.325). Title says association of presence/absence of mismatch with outcomes within EVT and MM, as treated. No mismatch is reference. Last-column .83 is a heterogeneity/interaction value rather than the MM effect P value.

**Rule and reproduced comparison:** Both adjusted measures are presented for the named MM mismatch-versus-no-mismatch contrast. The ratio interval contains1; the difference interval excludes0. They therefore provide different 95%-interval readings of whether there is an adjusted association with this outcome. This is not an arithmetic claim that adjusted RD must equal the crude difference (.61905−.575=.04405), and it is not a claim that an interaction P must match a within-arm CI. The reporting issue is the combination of these printed null-inference readings with absent identification of which RD analysis/estimand generated the latter result.

**Display precision:** Ratio lower limit0.93 allows[0.925,0.935], upper1.79 allows[1.785,1.795], so every rounded interval contains1. RD lower0.011 allows[0.0105,0.0115], upper0.325 allows[0.3245,0.3255], so every rounded interval excludes0. The printed estimates1.29 and0.168 allow[1.285,1.295] and[0.1675,0.1685] and remain within their intervals. The null-inference distinction survives all half-unit input intervals. There is no common numerical value being recomputed across RR and RD scales, so a relative-value discrepancy is not defined; the observation rests on null inclusion and the stated analysis mapping, not a >5% comparison of unlike quantities.

**Diagnostic approximations (not reported tests):** Assuming symmetric normal intervals on the printed log-RR and RD scales only for diagnostic illustration, log-RR SE≈(log1.79−log.93)/(2×1.959964)=.167040 and z≈log1.29/.167040=1.524435, implying two-sided diagnostic P≈.1274. RD SE≈(.325−.011)/(2×1.959964)=.080104 and z≈.168/.080104=2.097286, diagnostic P≈.0360. These approximations illustrate the two null-inference readings; they do not establish the authors' test statistic, sidedness beyond the stated main methods, covariance, variance estimator or RD estimand. No proposed numerical replacement is given.

**Qualifying route:** Route B. B1: estimate/test and method interpretation within REPORT, focused on one named outcome result. B2: supplied methods do not map the two adjusted measures to distinct conditional/marginal estimands or distinct confidence procedures, so the reader cannot identify which analysis accounts for the different null readings from this cell/footnote. B3: extracting this MM mismatch association can lead to different conclusions about whether the adjusted 95% interval excludes the relevant null, depending on which scale is taken. Route A category1 is not claimed because the table does not state a same-effect P value or test statistic for this result; .83 is an interaction value.

**Affected result or extracted value:** As-treated MM composite mismatch (≥10mL and ratio≥1.2) association with 90-day complete dependence/death: adjusted risk difference0.168 (0.011–0.325) versus adjusted risk ratio1.29 (0.93–1.79).

**Why context does not resolve it:** Count-based crude risks, shared adjustment footnote and table layout identify the contrast but do not specify RD construction or whether the two estimates target different adjusted populations/estimands. The visible printed distinction remains; a statistical reader cannot select an analysis explanation from the supplied cell. The different readings are not equated with a clinical direction reversal: both point estimates indicate increased unfavorable outcome.

**Source-grounded alternatives and missing definitions:** The RR may be a conditional modified-Poisson coefficient while RD may be a marginal standardized contrast, possibly using different normal, delta-method or resampling confidence procedures; nonlinear finite-sample intervals can have different null-inference readings. Main methods mention predicted margins/marginal probabilities for imaging-outcome illustrations but do not identify this RD calculation. Alternatively, one displayed interval may correspond to a different fitted analysis/population. These are alternative interpretations for adjudication, not inferred facts. Exact RD estimand, fitted model, analysis population and confidence procedure, plus mapping to the printed RR, are the missing definitions.

**Exact human question:** Which analysis, estimand and 95% confidence procedure produced the MM aRD0.168 (0.011–0.325) for ≥10mL/ratio≥1.2 composite mismatch and mRS5–6, and how should its exclusion of0 be interpreted alongside the printed aRR1.29 (0.93–1.79) for that same named contrast?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-006 eTable5 p.41, mRS0–2 composite and both mRS0–3 volume rows; S4056,S4059,S4062 | Subtracting the separately printed arm-specific log slopes with independent-slope SEs would give diagnostic P≈.327 rather than .82 for mRS0–2 composite; identical printed mRS0–3 slopes give central diagnostic P≈1 rather than .32/.82. The source describes interaction models separately from within-arm associations and does not identify their coefficients/covariance with those separate fits. The reconstruction is not a method demonstrated to reproduce the whole display, so it cannot establish a printed same-analysis conflict or routeA4. No interaction P is treated as either arm's slope-effect P. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-006 eTable7 pp.43–44, all binary within-arm mismatch cells | Several crude mismatch/no-mismatch ratios and differences differ from the printed aRR/aRD. The table expressly adjusts age, NIHSS, timing and core volume; the supplied report does not state these estimates are crude. Model-based quantities need not equal crude count comparisons. | MODEL_VERSUS_CRUDE |
| REPORT DOC-006 eTable6 p.42 footnote versus main REPORT statistical methods p.4 | Main primary ordinal associations use PIM, while eTable6 specifies ordinal logistic regression for model-comparison criteria. This explicitly identified additional model-comparison analysis does not represent a mislabeled PIM estimate. | CONTEXT_RESOLVES |
| REPORT DOC-006 eTable7 pp.43–44, numeric column headings and last-column values | Local arm/last-column headings are absent, but denominator totals170/166 and supplied main/SAP interaction descriptions identify the arm association and heterogeneity structure. There is no reproduced misattribution to a different outcome/population or numerical conflict from the heading omission. | CONTEXT_RESOLVES |
| REPORT DOC-006 eTable7 p.43 EVT mRS0–2 aRD; S4084 | Negative displayed zero −0.000 can suggest an apparent sign disagreement with ratio1.02. It is a zero at the printed precision, no significant direction is asserted, and the difference scale is not specified as a fixed transformation of the ratio-scale coefficient. The signed-zero notation alone does not change the extracted printed zero or null reading. | NOTATION_OR_TYPOGRAPHY |

## Scope completion and limitations

Complete scope: every printed inferential effect interval and each distinct test in eTables3–7 has a stable relationship record; all model comparison values are preserved. Relationships115; findings1; excluded-observation groups5. No scientific coverage gap. Exact fitted coefficient/testing replication remains limited by missing fit outputs and the source-grounded definition limits named in the inventory. The finding is for independent inclusion screening, with no candidate ID, severity, acceptance, correction or final adjudication assigned.
# Statistical pass 1 checker: tables B and plan methods

- Fresh shard: /root/stat1_tables_b_plan, gpt-6.1-sol/high, FRESH_SPAWN.
- Exact scope: DOC-006 eTables8–13, physical pp45–53; DOC-003 protocol pp1–82 statistical method, sample-size, power, adaptive/interim/stopping and historical inferential facts; DOC-004 parent SAP pp1–40 corresponding methods and numerical rules.
- Relationship inventory: statistics/parts/tables_b_plan.md; 120 records S5001–S5120, all PASS_1_COMPLETE.
- Findings: 6, F-ST1-501–F-ST1-506. Excluded observations:15 consolidated rows. No scientific gap.
- Direct-source authority and source-matched images used; no prior conclusions, web, unsupplied Python, raw-data audit or preferred analysis. Source and reused artifacts preserved. Main-report methods, DOC-005 and other results are disjoint fresh-agent assignments.

### F-ST1-501

**Title:** Two historical SELECT 95% intervals include the null boundary while their P values are significant.

**Locations and roles:** [DOC-003 protocol p13](../../../joi240006supp2_prod_1708623114.99233.pdf#page=13), PLAN, functional-independence and ordinal-shift sentences in the historical SELECT rationale. Direct native/layout and freshly rendered page13 confirm both readings.

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

**Locations and roles:** [DOC-003 p8 synopsis](../../../joi240006supp2_prod_1708623114.99233.pdf#page=8), PLAN; [DOC-003 p37 outcome section](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN; [DOC-003 p50 secondary analysis](../../../joi240006supp2_prod_1708623114.99233.pdf#page=50), PLAN. DOC-004 [p13](../../../joi240006supp3_prod_1708623114.99733.pdf#page=13)/[p17](../../../joi240006supp3_prod_1708623114.99733.pdf#page=17) corroborate secondary status but do not create an additional relationship.

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

**Locations and roles:** [DOC-003 p49 Table3 scenario#4](../../../joi240006supp2_prod_1708623114.99233.pdf#page=49), PLAN; [DOC-004 p11 operating-characteristics table scenario#4](../../../joi240006supp3_prod_1708623114.99733.pdf#page=11), PLAN. Direct protocol layout and source-matched SAP image confirm21.2% and51.2%.

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

**Locations and roles:** [DOC-003 p80 rank/statistic/stopping definition](../../../joi240006supp2_prod_1708623114.99233.pdf#page=80), PLAN; [DOC-003 p81 hypothesis/variable definitions](../../../joi240006supp2_prod_1708623114.99233.pdf#page=81), PLAN; [DOC-003 p37 score interpretation](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN; corresponding [DOC-004 p39](../../../joi240006supp3_prod_1708623114.99733.pdf#page=39)/[p40](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40), PLAN. Formula images directly read. All repeated locations form one direction issue.

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

**Locations and roles:** [DOC-004 p9 planned interim schedule](../../../joi240006supp3_prod_1708623114.99733.pdf#page=9), PLAN; [DOC-004 p11 sample-size/interim assumptions](../../../joi240006supp3_prod_1708623114.99733.pdf#page=11), PLAN; [DOC-004 p12 section7.5 actual stopping chronology](../../../joi240006supp3_prod_1708623114.99733.pdf#page=12), PLAN; [DOC-004 p40 boundaries](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40), PLAN. Source-matched page12 directly inspected.

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

**Locations and roles:** [DOC-003 p16 historical SELECT early-window safety paragraph](../../../joi240006supp2_prod_1708623114.99233.pdf#page=16), PLAN. Direct layout extraction confirms the full sentence and its immediate context.

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



## Every first-pass relationship explicitly indexed

The coordinator mechanically expands all 550 fresh first-pass scope records below. Each first-pass inventory contains the agent-authored per-S source values, method/logic checks and PASS_1_COMPLETE record; each index row links to that durable evidence. This expansion preserves the checker text and introduces no additional scientific review.

| S ID | First-pass runtime | Agent-authored evidence inventory | Pass 1 |
|---|---|---|---|
| S001 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S002 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S003 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S004 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S005 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S006 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S007 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S008 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S009 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S010 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S011 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S012 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S013 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S014 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S015 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S016 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S017 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S018 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S019 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S020 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S021 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S022 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S023 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S024 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S025 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S026 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S027 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S028 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S029 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S030 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S031 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S032 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S033 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S034 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S035 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S036 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S037 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S038 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S039 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S040 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S041 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S042 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S043 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S044 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S045 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S046 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S047 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S048 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S049 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S050 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S051 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S052 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S053 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S054 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S055 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S056 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S057 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S058 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S059 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S060 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S061 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S062 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S063 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S064 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S065 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S066 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S067 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S068 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S069 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S070 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S071 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S072 | root/stat1_main | [main per-S record](../statistics/parts/main.md) | PASS_1_COMPLETE |
| S1001 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1002 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1003 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1004 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1005 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1006 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1007 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1008 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1009 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1010 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1011 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1012 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1013 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1014 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1015 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1016 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1017 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1018 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1019 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1020 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1021 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1022 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1023 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1024 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1025 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1026 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1027 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1028 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1029 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1030 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1031 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1032 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1033 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1034 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1035 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1036 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1037 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1038 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1039 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1040 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1041 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1042 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1043 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1044 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1045 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1046 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1047 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1048 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1049 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1050 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1051 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1052 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1053 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1054 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1055 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1056 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1057 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1058 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1059 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1060 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1061 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1062 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1063 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1064 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1065 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1066 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1067 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1068 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S1069 | root/stat1_forest_a | [forest_a per-S record](../statistics/parts/forest_a.md) | PASS_1_COMPLETE |
| S2001 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2002 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2003 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2004 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2005 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2006 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2007 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2008 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2009 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2010 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2011 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2012 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2013 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2014 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2015 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2016 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2017 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2018 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2019 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2020 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2021 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2022 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2023 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2024 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2025 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2026 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2027 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2028 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2029 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2030 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2031 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2032 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2033 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2034 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2035 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2036 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2037 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2038 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2039 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2040 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2041 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2042 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2043 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2044 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2045 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2046 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2047 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2048 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2049 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2050 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2051 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2052 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2053 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2054 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2055 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2056 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2057 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2058 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2059 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2060 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2061 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2062 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2063 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2064 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2065 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2066 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2067 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2068 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2069 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2070 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2071 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2072 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2073 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2074 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2075 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2076 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2077 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2078 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2079 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2080 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2081 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2082 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2083 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2084 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2085 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2086 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2087 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2088 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2089 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2090 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2091 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2092 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2093 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2094 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2095 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S2096 | root/stat1_forest_b | [forest_b per-S record](../statistics/parts/forest_b.md) | PASS_1_COMPLETE |
| S3001 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3002 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3003 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3004 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3005 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3006 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3007 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3008 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3009 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3010 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3011 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3012 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3013 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3014 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3015 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3016 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3017 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3018 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3019 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3020 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3021 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3022 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3023 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3024 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3025 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3026 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3027 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3028 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3029 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3030 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3031 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3032 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3033 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3034 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3035 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3036 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3037 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3038 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3039 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3040 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3041 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3042 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3043 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3044 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3045 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3046 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3047 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3048 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3049 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3050 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3051 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3052 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3053 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3054 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3055 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3056 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3057 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3058 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3059 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3060 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3061 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3062 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3063 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3064 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3065 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3066 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3067 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3068 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3069 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3070 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3071 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3072 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3073 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3074 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3075 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3076 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3077 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S3078 | root/stat1_remaining_a | [remaining_a per-S record](../statistics/parts/remaining_a.md) | PASS_1_COMPLETE |
| S4001 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4002 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4003 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4004 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4005 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4006 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4007 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4008 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4009 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4010 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4011 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4012 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4013 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4014 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4015 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4016 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4017 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4018 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4019 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4020 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4021 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4022 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4023 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4024 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4025 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4026 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4027 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4028 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4029 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4030 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4031 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4032 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4033 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4034 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4035 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4036 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4037 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4038 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4039 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4040 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4041 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4042 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4043 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4044 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4045 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4046 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4047 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4048 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4049 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4050 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4051 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4052 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4053 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4054 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4055 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4056 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4057 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4058 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4059 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4060 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4061 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4062 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4063 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4064 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4065 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4066 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4067 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4068 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4069 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4070 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4071 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4072 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4073 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4074 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4075 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4076 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4077 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4078 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4079 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4080 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4081 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4082 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4083 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4084 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4085 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4086 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4087 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4088 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4089 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4090 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4091 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4092 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4093 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4094 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4095 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4096 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4097 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4098 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4099 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4100 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4101 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4102 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4103 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4104 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4105 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4106 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4107 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4108 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4109 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4110 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4111 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4112 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4113 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4114 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S4115 | root/stat1_tables_a | [tables_a per-S record](../statistics/parts/tables_a.md) | PASS_1_COMPLETE |
| S5001 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5002 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5003 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5004 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5005 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5006 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5007 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5008 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5009 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5010 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5011 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5012 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5013 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5014 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5015 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5016 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5017 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5018 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5019 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5020 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5021 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5022 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5023 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5024 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5025 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5026 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5027 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5028 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5029 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5030 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5031 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5032 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5033 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5034 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5035 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5036 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5037 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5038 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5039 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5040 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5041 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5042 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5043 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5044 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5045 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5046 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5047 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5048 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5049 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5050 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5051 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5052 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5053 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5054 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5055 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5056 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5057 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5058 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5059 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5060 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5061 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5062 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5063 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5064 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5065 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5066 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5067 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5068 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5069 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5070 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5071 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5072 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5073 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5074 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5075 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5076 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5077 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5078 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5079 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5080 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5081 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5082 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5083 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5084 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5085 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5086 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5087 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5088 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5089 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5090 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5091 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5092 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5093 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5094 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5095 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5096 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5097 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5098 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5099 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5100 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5101 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5102 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5103 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5104 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5105 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5106 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5107 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5108 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5109 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5110 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5111 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5112 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5113 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5114 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5115 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5116 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5117 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5118 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5119 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
| S5120 | root/stat1_tables_b_plan | [tables_b_plan per-S record](../statistics/parts/tables_b_plan.md) | PASS_1_COMPLETE |
