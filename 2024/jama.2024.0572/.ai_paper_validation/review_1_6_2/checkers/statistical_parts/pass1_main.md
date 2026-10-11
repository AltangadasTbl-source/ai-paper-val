# Statistical pass 1 — main REPORT

Runtime agent: `/root/stat1_main`; fresh `gpt-6.1-sol` at `high`. Exact assigned scope: every DOC-001 main-report estimate, interval, interaction P, narrative test, and report statistical-method logic, physical PDF pp.1–14. Supplemental rows and PLAN logic are assigned to other disjoint shards. Scope and 1.6.2 review contract read completely. 72 relationships S001–S072 all receive PASS_1_COMPLETE in statistics/parts/main.md and the initial canonical statistical inventory. One consolidated finding and six excluded observations. Scientific source authority is the supplied main PDF; source-linked extracted text is a locator/transcription aid. No candidate IDs assigned.

## Complete checks

All Figure1 ordinal effect rows (16), its7 interaction tests, all16 Table2 arm-specific estimates across8 covariate/outcome rows and8 interaction tests, all Table3 printed aGenOR/aRR/aRD estimates across8 contrast/outcome records and7 printed interaction tests, all remaining narrative associations, trend tests, predictions, population/model definitions and decision rules are covered. Point containment, endpoint order and effect direction reconcile except the interval/significance pattern below. Interaction P values are never treated as individual-effect P values. Narrative descriptive IQRs are never treated as effect CIs. The report specifies two-sided tests, P<.05,95%CI and no exploratory multiplicity adjustment; no noninferiority/equivalence margin exists in this main source. No test statistic or numeric standard error is printed in main results. The report’s stopping boundary is not numerically specified; supplied PLAN rules are reviewed separately. No main-source sample-size inputs permit standalone power reproduction.

### F-ST1-001

**Title:** Printed confidence intervals end at the ratio null while the narrative calls the corresponding associations statistically significant.

**Relationship IDs:** S024 and S062. One repeated pattern, two affected prognostic associations.

**Exact compared locations and document roles:**

- REPORT DOC-001, [physical PDFp.6, printed755, lower-left Association of ASPECTS paragraph continuing upper-right](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6): in multivariable models without adjustment for volumetric measures, decreasing ASPECTS was associated with “significantly worse clinical outcomes” within EVT-treated patients; aGenOR0.91(95%CI0.82–1.00) per1-point ASPECTS decrease. REPORT same document [p.7, Table2 ordinal-ASPECTS EVT row](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7) reproduces 0.91(0.82–1.00); [p.1 abstract](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1) repeats it without the significance qualifier. The interval and significant claim are compared within the p.6 paragraph; p.1/p.7 corroborate the printed interval, rather than constitute different document relationships.
- REPORT DOC-001, [physical PDFp.10, printed759, upper-left Association of Age and Time paragraph](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10): CTP acquisition to reperfusion/endprocedure aRR0.97(95%CI0.93–1.00) per10-minute increment; the predicted probability of independent ambulation “significantly decreased.” That phrase applies jointly to increasing age and this imaging-time estimate. Age0.97(0.96–0.99) does not show this pattern and is not an affected interval.
- REPORT DOC-001, [physical PDFp.4, printed753, Statistical Analysis last paragraph](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4): all hypotheses evaluated by two-sided tests; P<.05 considered significant; analyses exploratory with no multiple-comparison adjustment.

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
