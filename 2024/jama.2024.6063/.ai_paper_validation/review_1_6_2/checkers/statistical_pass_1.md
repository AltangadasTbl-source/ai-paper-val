# Statistical consistency review — pass 1 — Workflow 1.6.2

Runtime ID: 01a129b5-1c4b-7ed3-955e-c6ca5e85d0b6. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Read the complete quantitative scope, review contract and both complete new extraction maps before checking. Scope is all 104 stable S relationships in `../statistics/relationship_inventory.md`, covering all supplied current-trial inferential displays, supplied statistical design/method decisions and ancillary/historical inference. All 41 physical source pages are closed by mapper coverage; no legacy conclusions or external evidence were used. This output self-screens observations and assigns no candidate IDs or adjudications.

All19 main Table2 rows, all 3 eTable1 rows and all 62 eTable4 rows were checked. Every result point lies within its interval, interval endpoints are ordered and every between-arm CI null inclusion agrees with its P relative to the stated two-sided .05. No interval-versus-significance conflict was found. Normal/log-normal inversions are labelled diagnostics because exact test critical values, degrees of freedom and covariance are not supplied; they do not replace the reported analysis. Contrasts are tested against the report's explicit difference of modeled arm changes, never against crude final-minus-baseline summaries. Historical pilot/background data are distinct from adopted current-trial power inputs.

Seven findings remain after self-screening. Eleven apparent observations are excluded once in the table below. Every finding is offered for independent screening and remains Pending Human Adjudication if registered.

## Findings

### F-ST1-001

**Title:** Printed differences in change do not reconcile with the corresponding modeled arm changes.

**Relationships:** S032, S064, S019. **Focus area:** B and C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W. All compared content is REPORT. Repeated failure of the same explicitly stated point-contrast identity is consolidated into one issue with every affected location.

**Exact locations and printed values:**

| REPORT source location | Krill modeled change | Placebo modeled change | Printed between-group difference in change | Other affected cells |
|---|---:|---:|---:|---|
| [Results supplement p5, eTable4, WOMAC weight-bearing pain, week4](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5) | −84(95%CI−122,−46) | −103(−141,−65) | +3(−10,16),P=.66 | The two arm changes and CIs exactly repeat WOMAC function week4 on the same page, which prints difference−19(−73,35),P=.48. |
| [Results supplement p6, eTable4, hsCRP, week12](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6) | −.53(−1.32,.26) | +.24(−.55,1.03) | +.07(−1.19,1.33),P=.92 | Week24 hsCRP on this page prints−.76/−.12 with contrast+.64, which satisfies the stated identity. |
| [Main p6, Table2, ICOAP total pain, week24](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) | −9.9(−13.3,−6.57) | −8.2(−11.9,−4.5) | +2.05(−2.64,6.74),P=.39 | Placebo change/CI exactly repeats the ICOAP intermittent row directly above. |

**Rule and calculation:** [Main p7 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) (REPORT) says arm changes and differences in changes are calculated using linear combinations of estimated coefficients. The continuous contrast direction elsewhere in both displays is placebo minus krill. Subtracting the reported modeled changes is an algebraic comparison within the stated model, not a comparison with crude means. The same rule reproduces other rows including WOMAC function4, hsCRP24, primary VAS24, triglyceride24 and ICOAP intermittent24.

| Affected row | Point recomputation P−K | Recomputed interval from half-unit rounding | Printed contrast half-unit interval | Gap | Relative discrepancy |
|---|---:|---|---|---:|---:|
| Weight-bearing4 | −103−(−84)=−19 | [−20,−18] | [2.5,3.5] |20.5|20.5/3=6.8333|
| hsCRP12 | .24−(−.53)=.77 | [.76,.78] | [.065,.075] |.685|.685/.07=9.7857|
| ICOAP total24 | −8.2−(−9.9)=1.7 | [1.60,1.80] | [2.045,2.055] |.245|.245/2.05=.1195|

All exceed .05. The CIs and P values in the contrast cells agree with each other about significance; that separate check does not reconcile the differing point contrasts. Reversing a common reference direction cannot reconcile these three values.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The week4 WOMAC weight-bearing change and contrast, week12 hsCRP contrast and week24 ICOAP total contrast; each could supply a different magnitude or direction in extraction. The first row's model changes also affect whether function and pain results have been distinguished.

**Why context does not resolve it:** This is a reproduced printed-model contrast mismatch in an always-register category. The point values are incompatible after permitted display precision even though adjacent rows indicate the usual identity.

**Alternatives and missing definitions:** The arm changes and contrast could come from different adjustment or marginalization procedures; the paper does not identify such a distinction. Repetition of other rows' cells is directly observed, but any production mechanism is inferred and is not asserted. The exact model output and row-specific contrast definitions are absent. Both the displayed arm changes and displayed contrast remain possible extraction readings pending human review.

**Exact human question:** Which modeled arm changes and between-arm contrast belong to each of these three endpoint/time rows, and were any arm changes and contrast estimates obtained from distinct models or marginalization procedures?

### F-ST1-002

**Title:** The week12 glucose contrast interval does not reproduce the interval-width rule supported by the neighboring modeled results.

**Relationships:** S068, with comparators S016, S064, S065, S066, S067. **Focus area:** B and C. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. Every location is REPORT.

**Exact locations and printed values:** [Results supplement p6, eTable4, fasting glucose week12](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6): Kchange .09(95%CI−.07,.24), Pchange .15(−.01,.31), difference .07(−1.19,1.33),P=.92. On the same page the entire contrast tuple .07(−1.19,1.33),P=.92 appears for hsCRP week12. Glucose week24 on this page and [main p6](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) prints K .07(−.12,.26), P .11(−.08,.29), difference .04(−.23,.30),P=.79.

**Rule and calculation:** The empirical display rule combines the two arm-change CI half-widths as sqrt(hK²+hP²). This is a diagnostic reproducing rule, not an assumption that unpublished model covariance is zero. It reproduces glucose24: sqrt(.190²+.185²)=.2652, printed contrast half-width .265; TG12 sqrt(.125²+.125²)=.1768 vs printed .175; HDL12 sqrt(.040²+.040²)=.0566 vs printed .060; LDL12 sqrt(.105²+.105²)=.1485 vs printed .1475, within display precision. Glucose12 arm half-widths .155 and .160 produce .2228, whereas printed contrast half-width is1.260. Even the sum of arm half-widths is only .315, showing how much greater the reported width is than these two components under a common-critical-value linear contrast. The exact critical value and covariance are missing, so this latter bound is diagnostic and the human question concerns the unstated producing method.

Allowing each arm CI endpoint ±.005 gives hK[.150,.160],hP[.155,.165], root-sum-square half-width[.21570,.22984]. Centering at the printed difference interval[.065,.075] yields a diagnostic lower endpoint[−.16484,−.14070] and upper[.28070,.30484]. Printed lower[−1.195,−1.185] has gap1.02016/1.19=.8573; printed upper[1.325,1.335] has gap1.02016/1.33=.7670. Both exceed .05. The printed CI and P are internally compatible; this finding concerns the interval against a method that reproduces the other rows, not a categorical null/P disagreement.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** Week12 fasting-glucose between-group confidence interval and its associated test; the displayed interval would provide substantially less precision in evidence synthesis than the rule that reproduces the adjacent glucose/metabolic rows.

**Why context does not resolve it:** The display contains a reproduced interval-width discrepancy and a repeated hsCRP contrast tuple. A reproducing method, rather than a preference for another analysis, establishes the comparison. Always-register category4 applies; the unidentified method is a human question.

**Alternatives and missing definitions:** Different models, variance estimates, critical values or contrast covariance could apply specifically to the glucose contrast, despite no such distinction in the table. The duplicated tuple might be a coincidental numerical equality; a copying mechanism is not established. Unpublished model output could explain the discrepancy. No raw data, row-specific covariance or exact CI method is supplied.

**Exact human question:** Which confidence-interval and test calculation produced the week12 glucose contrast, and why does its .07(−1.19,1.33),P=.92 tuple match hsCRP12 while failing the interval-width rule that reproduces the glucose24 and neighboring lipid rows?

### F-ST1-003

**Title:** The planned96% effusion power does not reproduce from its supplied effect, variability and sample size inputs.

**Relationships:** S072, S071. **Focus area:** C and D. **Proposed review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P. All compared content is PLAN.

**Exact locations and printed values:** [Protocol p12, Power calculations](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) states the pain design needs234 participants, inflated to260 (130/arm) for10%loss, and says this gives96%power for a20% difference in effusion size with mean2.24cm² and SDofchange1.35. [Protocol p2](../../../joi240048supp1_prod_1727199125.7845.pdf#page=2) states the20%effusion hypothesis over24weeks. [Protocol p12 Statistics and SAP p1](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1) establish between-group linear regression and two-tailed .05.

**Rule and calculation:** Labelled diagnostic for an equal-size two-arm mean-change comparison: absolute difference=.20×2.24=.448cm²; SEofdifference=1.35×sqrt(2/n). With117/arm (234total), noncentral standardized difference2.538 and normal two-sidedα.05 power=.71844. With130/arm (260total), it is2.675 and power=.76286. The normal diagnostic sample needed for96% is approximately500total. These are diagnostic calculations from supplied inputs, not a declaration that a particular unreported exact-test convention must be used.

Conservative input rounding envelopes:20%[19.5%,20.5%],mean[2.235,2.245],SD[1.345,1.355]. They give diagnostic power[69.151%,74.447%] at234total or[73.670%,78.778%] at260total. Claimed96%has interval[95.5%,96.5%]; even the favorable260total envelope leaves16.722percentage-point gap/96=.1742, above .05. Thus neither possible referent of 'this' reconciles with the claim under the supplied simple two-arm model. Using a finite-sample t calculation would not supply the missing improvement to96%.

**Qualifying route:** Route B.

**Affected result or extracted value:** The effusion-synovitis planned power and its20%target difference; the claimed sensitivity of the sample to this structural endpoint changes materially under the supplied inputs.

**Why context does not resolve it:** The adopted sample, effect, SD and power are explicit in one paragraph, but a large gap remains after precision and both interpretations of the effective sample. No correlation, covariate-efficiency or alternative variance input is specified to reproduce96%.

**Alternatives and missing definitions:** A different effective SD, a within-person correlation or covariate adjustment, another effect definition, or a distinct power method may have been used. The source does not identify it. A historical alternative WOMAC calculation in the next paragraph is explicitly considered overly optimistic and is not substituted here. Exact powering software, test formula and adjustment assumptions are absent.

**Exact human question:** What calculation and additional assumptions produced96%power for a20%effusion difference using mean2.24cm²,SDchange1.35 and234or260total participants?

### F-ST1-004

**Title:** The reported power assumptions differ from the supplied planned pain and effusion assumptions.

**Relationships:** S073. **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Exact locations and printed values:** PLAN [protocol p12](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12): pain10mm,SD25.5,90%,234beforeloss/260after10%loss; effusion20%of2.24cm²,SD1.35,96%. REPORT [main p4 Power Calculations](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4):130/group provides90%power for10-pointVAS with SD23.8 and4.5mLbetween-arm effusion-volume change atα.05. Both remain stated designs for the same trial, with no supplied revised plan tying these changed assumptions together.

**Rule and calculation:** Compare the planned and reported inputs and endpoint quantities before comparing final sample size. Pain SD display intervals[25.45,25.55] and[23.75,23.85] have gap1.60/25.5=.06275>.05. Effusion20%area target is .448cm² under the plan, whereas the report uses4.5mLvolume; these are different endpoint dimensions without a supplied mapping. Effusion96%versus90%display intervals[95.5,96.5] and[89.5,90.5] leave gap5/96=.05208>.05. Same130/arm does not reconcile these changes.

**Qualifying route:** Route B.

**Affected result or extracted value:** Trial power/design extraction: pain change SD and effusion target quantity/power. Interpretation of which structural endpoint the trial was powered for is unclear across the supplied documents.

**Why context does not resolve it:** The article cites other clinical-trial sources for its power paragraph, but neither supplied plan nor report provides an amendment or explanation connecting the changed SD, effusion dimension, target and claimed power.

**Alternatives and missing definitions:** A revised calculation may have used additional trial evidence or updated imaging methodology. Different source references are observed; an undisclosed or separately supplied amendment is possible but cannot be inferred. The volume SD needed to reproduce the report's effusion calculation is missing. This comparison does not claim a protocol violation or favor either calculation.

**Exact human question:** Which power assumptions were adopted for this trial, and is there a revised calculation explaining the pain SD25.5→23.8 and effusion area20%/96%→volume4.5mL/90%changes?

### F-ST1-005

**Title:** The primary pain endpoint uses a different recall period in the report and plan.

**Relationships:** S074. **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Exact locations and printed values:** PLAN [protocol p8, Primary outcome: Pain](../../../joi240048supp1_prod_1727199125.7845.pdf#page=8) specifies the100mmVAS question asking pain 'today' at each time point. REPORT [main p3 Primary Outcome](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3) specifies self-reported knee pain over the past7days; [main p5 Table1 footnote b](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) repeats the past7days definition. Both are for the primary24weekVAS change; both scales span0–100.

**Rule and calculation:** An endpoint's recall window is part of its definition. 'Today' and 'past7days' identify different reference periods, despite matching scale and24weektimepoint. No arithmetic rounding rule is applicable to a categorical window comparison.

**Qualifying route:** Route B.

**Affected result or extracted value:** The definition of the primary knee-pain VAS outcome whose reported contrast is−.3(95%CI−6.9,6.4). A data extractor needs the reference period used for the primary measure.

**Why context does not resolve it:** Each document is internally clear, but the supplied package does not identify an amended questionnaire or endpoint-window change reconciling the primary definition across PLAN and REPORT.

**Alternatives and missing definitions:** The actual questionnaire may have been revised or the protocol wording may have summarized a question used alongside a7daymeasure. Neither bridge is supplied. No claim is made about which window was actually administered without the questionnaire/amendment.

**Exact human question:** Did the trial's primary VAS ask about pain today or over the past7days, and what supplied amendment or instrument explains the changed reference period?

### F-ST1-006

**Title:** The primary analysis reported is a mixed repeated-measures model rather than the planned change-score linear regression.

**Relationships:** S075. **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Exact locations and printed statements:** PLAN [protocol p12 Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) and [SAP p1 lines5–7](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1) prescribe linear regression comparing changes in pain/maximal effusion/function with univariate and conditional multivariable modeling. REPORT [main p4 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) and [p7 continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) specify a linear mixed model with treatment,month,treatment×month,participant/center random intercepts and month random slope; main/secondary numbers are linear combinations of its coefficients. No separate change-score regression primary estimate appears in the complete REPORT maps.

**Rule and calculation:** Match the primary endpoint/time first, then compare its producing analysis specification. The report describes a longitudinal random-effects model that the supplied SAP/protocol do not specify, and it does not provide the originally stated primary regression result. No numerical rounding rule applies to this categorical model comparison. Both models may be statistically coherent; this finding concerns the planned/reported analysis record.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The analysis producing the primary−.3(−6.9,6.4),P=.94 and the identification of that result as the planned primary analysis.

**Why context does not resolve it:** The planned primary analysis is replaced in the supplied report by a materially different model without a supplied revised SAP or separate original-model result. This is an always-register planned-versus-reported analysis category.

**Alternatives and missing definitions:** The mixed model might be an approved amendment or an operational elaboration recorded elsewhere. The supplied four-line SAP is explicitly an excerpt of protocol v2,dated02Feb2016; it supplies no longitudinal random-effects specification. An amendment is possible but not observed. No analysis is preferred or judged inappropriate.

**Exact human question:** Was the primary model amended from the supplied change-score linear regression to the reported mixed model, and where is the relevant prespecification or original-model primary result?

### F-ST1-007

**Title:** The planned per-protocol efficacy analysis is not supplied with the primary results.

**Relationships:** S079. **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Exact locations and printed statements:** PLAN [protocol p12 Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) and [SAP p1 lines8–9](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1) unconditionally state per-protocol analyses will be completed for participants consuming≥80%ofcapsules. REPORT [main p4,p7 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p6 Table2](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [result supplement p2 eTable1](../../../joi240048supp3_prod_1727199125.83025.pdf#page=2) give primary main,age-adjusted andmultiple-imputationresults. [Result supplement p3 eTable2](../../../joi240048supp3_prod_1727199125.83025.pdf#page=3) gives adherence≥80%counts but no restricted-population efficacy estimate. Complete REPORT Mpp1–10/Rpp1–15 map contains no per-protocol primary result.

**Rule and calculation:** Check presence of an unconditionally planned primary analysis and its population restriction in the complete supplied results. Adherence counts or age/MI sensitivity results do not implement the≥80%per-protocol efficacy analysis. No arithmetic precision rule applies to a missing analysis specification/result.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Availability of the planned primary knee-pain efficacy estimate among≥80%adherent participants, including its interval and population size.

**Why context does not resolve it:** The explicit planned analysis is not conditional on apositiveprimarytrial or sufficient events, and no reported efficacy result is identified as using that adherence restriction. Always-register category5 applies.

**Alternatives and missing definitions:** It might have been performed and omitted or recorded in another unsupplied document, or the plan may have been amended. Adherence denominator issues belong to separate numeric checking and do not supply the missing efficacy estimate. No preferred additional analysis is proposed; only the supplied prespecification is compared with its reporting status.

**Exact human question:** Was the prespecified≥80%per-protocol primary efficacy analysis performed, and where are its population definition, estimate and interval or the amendment removing it?

## Excluded observations

Only apparent issues considered and excluded are listed; successful checks are recorded in the S inventory. Each row has exactly one reason code. No excluded observation is a reproduced interval-versus-P/null/test conflict.

| Location | Observation | Reason code |
|---|---|---|
| REPORT R p6 eTable4 strength12; S057 | Negative modeled arm changes despite positive descriptive final-minus-baseline differences, and tuple equality with backVAS4, do not establish a conflicting model output without replacing modeled changes with crude mean differences. The24wkstrength row itself also shows model-versus-crude differences. | MODEL_VERSUS_CRUDE |
| REPORT M p6/R p5 WOMACtotal24; S003 | Independent-arm root-sum-square CIwidth≈33.2 versus printed27.5; baseline-adjusted model has unsupplied cross-arm coefficient covariance and exact critical values. No row-specific copied tuple or impossible bound is established by this diagnostic alone. | CONDITIONAL_OR_UNREPORTED |
| REPORT M p6 ICOAPintermittent; S018 | Normal-Wald diagnostic P≈.58 versus printed.62 leaves≤.05 relative gap under displayed estimate/endpoints; exact test degrees of freedom also unavailable. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN P p12 adoptedVASpower; S071 | Exact-input normal diagnostic requires273.3 versus234participants, but conservative half-unit input rounding gives242.67–309.48; nearestgap8.17/234=.0349≤.05. The10%inflation234/.9=260 reproduces. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT M p4 power; S070 | 130/arm versus diagnostic119/arm for90%painpower is compatible with a conservative recruited sample and the statement that it provides90%, rather than an assertion of exact minimum size. | CONTEXT_RESOLVES |
| PLAN P p12/A p1 vs REPORT M pp4,6/R p6 missingness; S078 | Propensity weighting is planned only 'as appropriate'; report's age-related sensitivity does not state that an appropriate weighting requirement was disregarded. Missing weights alone do not prove a conflict. | CONDITIONAL_OR_UNREPORTED |
| REPORT M p6/R p6 no-imputation footnote vs R p2 labelledMI sensitivity; S021,S078 | Main tables use no imputation; a separately labelled multiple-imputation sensitivity result does not make the main-analysis statement inconsistent. | CONTEXT_RESOLVES |
| PLAN P p11 ICOAPschedule vs REPORT M p4 posthoc; S082 | Prospective collection ofICOAP does not supply a prespecified ICOAPanalysis or outcome status, so posthoc analysis designation is not contradicted by collection alone. | CONDITIONAL_OR_UNREPORTED |
| PLAN P pp6–7 secondary list vs REPORT M p7 exploratorycaution; S080 | Report still labels these secondary outcomes; exploratory interpretation due multiplicity does not establish a changed endpoint status. | NOT_REPRODUCED |
| REPORT M p7 'no changes in posthoc outcomes' vs p6 arm-changeCIs; S104 | Adjacent between-arm comparison establishes the intended comparative statement; all 3between-armICOAPintervals include0. Within-arm changes remain printed and extractable. | CONTEXT_RESOLVES |
| REPORT M p6 responder superscriptf missingdefinition vs R p7 log-binomialRRfootnote; S011,S085 | The matching supplementary row explicitly identifies RR/log-binomial regression, resolving the main missing footnote's measure identity. No printed value or quantity conflicts. | CONTEXT_RESOLVES |

## Evidence provenance and limitations

Fresh derivatives: `../preprocessing/statistical_pass_1/main-p04-p07.txt`, `result-p05-p07.txt`, `protocol-p08.txt`, `protocol-p12.txt`, `sap-p01.txt`, `result-p02.txt`: direct pdftotext -layout,Poppler26.01.0. Current-source images `main-p06.png`,`result-p05.png`,`result-p06.png`,`protocol-p12.png`: direct pdftoppm,Poppler26.01.0,CPU,visually inspected. Model/power diagnostic calculations used R4.5.2 (base stats), without Python scientific orchestration; saved `diagnostic_power.txt` with labelled normal/t outputs. Source locations and derivative engines are recorded here. No source or reused asset was modified.

104 relationships complete;7 findings;11 excluded observations. No scientific coverage gap. Missing exact covariance/df/model-output,imputationdetails,powerformula and original questionnaires/amendments are source limits named per record. The root coordinator supplies independent inclusion screening, stablecandidateassignment and later mechanical source recheck. This pass assigns no severity, validity, disposition or correction.

## Explicit pass completion records

The following IDs match the canonical inventory exactly. Each carries PASS_1_COMPLETE; a different fresh pass 2 agent must revisit every ID.

| Relationship ID | Pass 1 status |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
| S054 | PASS_1_COMPLETE |
| S055 | PASS_1_COMPLETE |
| S056 | PASS_1_COMPLETE |
| S057 | PASS_1_COMPLETE |
| S058 | PASS_1_COMPLETE |
| S059 | PASS_1_COMPLETE |
| S060 | PASS_1_COMPLETE |
| S061 | PASS_1_COMPLETE |
| S062 | PASS_1_COMPLETE |
| S063 | PASS_1_COMPLETE |
| S064 | PASS_1_COMPLETE |
| S065 | PASS_1_COMPLETE |
| S066 | PASS_1_COMPLETE |
| S067 | PASS_1_COMPLETE |
| S068 | PASS_1_COMPLETE |
| S069 | PASS_1_COMPLETE |
| S070 | PASS_1_COMPLETE |
| S071 | PASS_1_COMPLETE |
| S072 | PASS_1_COMPLETE |
| S073 | PASS_1_COMPLETE |
| S074 | PASS_1_COMPLETE |
| S075 | PASS_1_COMPLETE |
| S076 | PASS_1_COMPLETE |
| S077 | PASS_1_COMPLETE |
| S078 | PASS_1_COMPLETE |
| S079 | PASS_1_COMPLETE |
| S080 | PASS_1_COMPLETE |
| S081 | PASS_1_COMPLETE |
| S082 | PASS_1_COMPLETE |
| S083 | PASS_1_COMPLETE |
| S084 | PASS_1_COMPLETE |
| S085 | PASS_1_COMPLETE |
| S086 | PASS_1_COMPLETE |
| S087 | PASS_1_COMPLETE |
| S088 | PASS_1_COMPLETE |
| S089 | PASS_1_COMPLETE |
| S090 | PASS_1_COMPLETE |
| S091 | PASS_1_COMPLETE |
| S092 | PASS_1_COMPLETE |
| S093 | PASS_1_COMPLETE |
| S094 | PASS_1_COMPLETE |
| S095 | PASS_1_COMPLETE |
| S096 | PASS_1_COMPLETE |
| S097 | PASS_1_COMPLETE |
| S098 | PASS_1_COMPLETE |
| S099 | PASS_1_COMPLETE |
| S100 | PASS_1_COMPLETE |
| S101 | PASS_1_COMPLETE |
| S102 | PASS_1_COMPLETE |
| S103 | PASS_1_COMPLETE |
| S104 | PASS_1_COMPLETE |
