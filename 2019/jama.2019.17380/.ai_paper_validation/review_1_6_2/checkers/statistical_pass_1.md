# Statistical consistency pass 1 — Workflow 1.6.2

Runtime agent ID: /root/statistical_pass_1. Fresh qc162_statistical_consistency_reviewer; gpt-6.1-sol / high; PASS_1_COMPLETE.

Exact scope: all 82 stable relationships S001–S082 from the two complete source-linked evidence maps, including every constituent inferential row in the grouped supplementary tables and figures. No S ID was added or omitted. Both maps total 186922 bytes, below the assigned 200000-byte context bound. The scientific checks include counts and populations where they affect inference, containment, interval order, direction, estimate/CI/P compatibility, stated hypothesis/alpha, interactions, methods, planned versus reported analysis, original/amended power and parent monitoring. The independent numeric and cross-source lanes additionally own their complete count/design comparisons; this pass does not use their conclusions as scientific input.

Nine findings and eight excluded apparent observations. All results remain for independent inclusion screening and human adjudication. No candidate IDs or AI adjudication assigned. Read completely QUALITY_CONTROL_SCOPE.md, the review contract and START_PROMPT.md. Direct supplied PDFs control transcription; source-matched native/layout text and unchanged canonical CPU renderings were used to locate and visually inspect exact pages. New direct pdftotext derivatives are recorded in statistics/relationship_inventory.md.

## Findings

### F-ST1-001

**Title:** Primary analysis population differs from the amended plan.

**Relationships:** S006, S071; P_R. **Compared roles:** PLAN amended analytic plan [p32, section15c](../../../joi190122supp1_prod.pdf#page=32); REPORT main article [p3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p4, Retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4), and [p6, Figure 1 primary-analysis boxes](../../../jama_de_boer_2019_oi_190122.pdf#page=6).

**Printed statements and values:** The implemented addendum defines intent to treat as including all participants who return at least one follow-up biosample. The report states that all participants were analyzed regardless of adherence or follow-up. Figure 1 includes 370+333+289+320=1312 in primary analysis. The report identifies 1090 returning at least one follow-up blood sample and 1091 returning at least one follow-up urine sample.

**Rule and calculation:** Primary-population definitions must be compared after matching the current year 5 eGFR analysis. Report inclusion does not apply the plan's follow-up condition. The number potentially eligible under a blood-only interpretation is 1090; a union-of-blood/urine interpretation is not supplied and cannot be inferred. The logical conflict remains independently of that undefined union. For the blood contrast, allowing half-unit intervals1090±0.5 and1312±0.5 leaves gap221; relative to1312 this is0.16845, above0.05. Counts here corroborate the explicit definition comparison rather than supply an assumed urine/blood union.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** The primary eGFR active-versus-placebo contrasts0.9(−0.7,2.5) and0.9(−0.7,2.6), and their analytic-population definition.

**Why context does not resolve it:** The endpoint amendment is supplied, but the implemented plan retains a follow-up eligibility condition absent from the reported full analytic population. Immediate context does not identify another amendment of that condition.

**Alternatives and missing definitions:** A later unsupplied amendment may have expanded the population; “at least one follow-up biosample” may mean a blood/urine union. Neither alternative changes the printed contrast between conditional and unconditional inclusion, and the union denominator is not supplied.

**Human question:** Which final primary-analysis population was intended, and where is the change from follow-up-conditioned inclusion to all randomized participants documented?

### F-ST1-002

**Title:** Number of imputation datasets differs from the amended plan.

**Relationships:** S006, S071; P_R. **Compared roles:** PLAN [p32, section15c](../../../joi190122supp1_prod.pdf#page=32); REPORT [p3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3).

**Printed statements and values:** Plan: results from 10 imputation datasets combined using Rubin rules. Report: multiple imputation M=20, including missing follow-up outcomes, with estimates combined using Rubin rules.

**Rule and calculation:** Match the primary year 5 eGFR missing-data implementation.10 and20 are differing implementation counts. Half-unit intervals[9.5,10.5] and[19.5,20.5] leave gap9; relative to the report's 20,0.45>0.05. This calculation screens the printed-count discrepancy only; no unreported between-imputation variance or pooled degrees of freedom is inferred.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** The method and uncertainty calculation accompanying both primary 0.9 eGFR treatment contrasts and the M count taken into analysis extraction.

**Why context does not resolve it:** Both documents explicitly specify a count for the same imputation/pooling step. The report does not identify an amendment of the count.

**Alternatives and missing definitions:** More imputations may represent a later implementation refinement. No substantive direction or size of an effect on the reported SE is claimed; actual between-imputation variation and final pooling df are unavailable.

**Human question:** Was M=20 a documented amendment or implementation change from the supplied M=10 plan, and which imputation specification applies to the reported primary estimates?

### F-ST1-003

**Title:** Fixed primary covariate adjustment differs from the amended primary model.

**Relationships:** S005, S062, S073, S074; P_R. **Compared roles:** PLAN [p32, section15e/Equation 2](../../../joi190122supp1_prod.pdf#page=32) and [p33, continuation](../../../joi190122supp1_prod.pdf#page=33); REPORT [p3, Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3) and [p8, Table 2 footnotea](../../../jama_de_boer_2019_oi_190122.pdf#page=8).

**Printed statements:** Amended primary Equation 2 includes treatment, categorical time, treatment×time and random patient intercept. The plan places added baseline-characteristic terms in sensitivity analyses conditional on imbalance. The report includes age, sex and their interactions with time in the continuous primary model; eGFR additionally includes baseline urineACR and its time interaction. Table 2 calls its contrast derived from this adjusted model.

**Rule and calculation:** Compare the specified primary model term sets, rather than raw versus adjusted estimates. The report's fixed primary term set contains age/sex/ACR and time interactions absent from Equation 2; the plan's optional sensitivity clause does not specify them as fixed primary covariates. This is a logical model-specification comparison; a numerical rounding interval is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** Table 2 primary adjusted eGFR mean differences0.9(−0.7,2.5) and0.9(−0.7,2.6), and the prespecified-versus-reported primary model extracted for them.

**Why context does not resolve it:** Current plan and report describe different primary term sets. The report gives the actual adjustment but no source-linked revision making those adjustments primary.

**Alternatives and missing definitions:** An unsupplied later plan may add fixed covariates, or the conditional imbalance clause may have been applied to the reported primary analysis. Neither is documented as the explanation. This card does not question the stated, internally coherent adjusted LMM or propose another analysis.

**Human question:** Which final primary model was prespecified, and what source documents making age, sex, baseline ACR and their time interactions fixed primary adjustments rather than conditional sensitivity terms?

### F-ST1-004

**Title:** High-adherence sensitivity population uses a different threshold and continuity rule.

**Relationships:** S006, S064, S076, S079, S080; P_R. **Compared roles:** PLAN [p19, sectionVIg](../../../joi190122supp1_prod.pdf#page=19) and implemented [p33, section15g](../../../joi190122supp1_prod.pdf#page=33); REPORT [p3, Covariates/Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), supplement [p6, eTable 1 definitions](../../../joi190122supp2_prod.pdf#page=6), [p10, eTable 5 footnote](../../../joi190122supp2_prod.pdf#page=10), and [p13, eTable 8 footnote](../../../joi190122supp2_prod.pdf#page=13).

**Printed statements and values:** Both original and amended plans specify adherence≥80%; the addendum specifies continuous adherence. The report defines high adherence as study medications at least two-thirds of the time. eTables 5/8 use that report on at least 4 of 6 questionnaires, with N=1032 for each intervention.

**Rule and calculation:** Match the planned adherence sensitivity analysis. At least2/3=66.6667% is lower than80%, and4 of 6 qualifying reports is a distinct temporal rule from continuous adherence. Treating80% as[79.5,80.5]% and the exact fraction2/3 as66.6667% leaves gap12.8333percentagepoints; relative to80%,0.16042>0.05. Four/six is the supplied questionnaire criterion, not an assumed average drug-use percentage.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route B.

**Affected result or extracted value:** Adherent-primary eGFR contrasts0.89(−0.74,2.52),P.28 and0.42(−1.22,2.06),P.61 in eTable 5, their sensitivity-population definition, and analogous ACR sensitivity results in eTable 8.

**Why context does not resolve it:** Both supplied plan versions retain80%, whereas report tables explicitly define a lower per-questionnaire cutoff and a noncontinuous qualification count. No supplied revision links these populations.

**Alternatives and missing definitions:** The report may adopt an available questionnaire category or later operational amendment. Actual eligible N at the plan's threshold is not supplied, so no claimed difference in effect size or patient count is calculated.

**Human question:** Was the ≥80% continuous-adherence rule replaced by ≥2/3 on at least 4 of 6 questionnaires, and which population definition should be attributed to the prespecified sensitivity analysis?

### F-ST1-005

**Title:** Prespecified bioavailable 25(OH)D subgroup analysis of the primary outcome is not reported.

**Relationships:** S007, S063, S075; P_R. **Compared roles:** PLAN [p33, section15f](../../../joi190122supp1_prod.pdf#page=33); REPORT [p3, subgroup methods](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p8, Figure 3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), and supplementary [p18, eFigure 2](../../../joi190122supp2_prod.pdf#page=18). Complete main and support displays were checked to locate a matching result.

**Printed statements:** Amended plan explicitly specifies baseline total AND bioavailable serum 25(OH)D subgroup analyses. Report methods name25(OH)D concentrations; Figure 3 displays the total-concentration categories<20,20–<30,≥30ng/mL. The supplementary ACR figure also labels total25(OH)D. No bioavailable-defined primary eGFR subgroup or interaction result appears in the supplied package.

**Rule and calculation:** Match the two distinct planned exposure definitions, rather than treating a shortened name as the other measurement. The supplied results contain total-concentration categories but no second bioavailable-defined result. This is an analysis-presence comparison, so display-precision arithmetic is not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned effect modification of the primary five-year eGFR treatment contrast by baseline bioavailable 25(OH)D; extraction of which prespecified subgroup analyses were reported.

**Why context does not resolve it:** Route A category 5 applies to a planned primary-outcome analysis not reported. The package does not say that the bioavailable analysis was withdrawn or replaced; total and bioavailable were separately specified.

**Alternatives and missing definitions:** Bioavailable measurements may have been unavailable, the analysis may have been omitted, or a later amendment may have removed it. No measurement-availability fact or amended removal is supplied. This finding does not demand a preferred biomarker.

**Human question:** Was the prespecified bioavailable 25(OH)D subgroup analysis performed or removed, and where is its primary-outcome result or amendment documented?

### F-ST1-006

**Title:** Standalone time-to-ACR-doubling analysis is called prespecified but is absent from the amended endpoint list.

**Relationships:** S012, S045, S048, S049, S054, S056, S070; P_R. **Compared roles:** PLAN original [p17, sectionsVIb/VIc](../../../joi190122supp1_prod.pdf#page=17) and implemented [p32, section15b](../../../joi190122supp1_prod.pdf#page=32); REPORT [p3, Prespecified secondary outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3) and [p9, Table 3/footnotea](../../../jama_de_boer_2019_oi_190122.pdf#page=9).

**Printed statements and values:** Report calls change in urineACR prespecified and says it was analyzed continuously AND as time to doubling with final ACR≥30mg/g. Table 3 gives separate categorical ACR HRs1.34(1.00–1.80),P.05 forD and1.08(0.81–1.44),P.60 foromega. Amended endpoint list specifies continuous ACR changes at years 2/5, time to≥40%eGFR loss, and the eGFR loss/ESRD/death composite. Original plan contains ACR doubling≥30mg/g as a COMPONENT of a different composite, not as a separate time-to-event ACR endpoint.

**Rule and calculation:** A composite component in an older plan is not the same estimand/status as a standalone event-time endpoint in the current report. Search of supplied outcome and hypothesis-testing sections finds no standalone categorical ACR hazard analysis designated prespecified. Logical outcome/analysis comparison; rounding arithmetic not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified status of the two Table 3 ACR-doubling HR results and their endpoint/estimand definition.

**Why context does not resolve it:** Route A category 5 applies to an analysis called prespecified that the supplied plan does not contain. Continuous change, a component of a multicomponent composite and standalone time-to-doubling are distinct analyses.

**Alternatives and missing definitions:** An unsupplied later amendment may prespecify this endpoint; the investigators may have regarded it as an alternative analysis of prespecified continuous ACR. Either interpretation needs documentation of the categorical endpoint/status and is not assumed from the shared biomarker.

**Human question:** Which supplied or later plan prespecified the standalone time-to-ACR-doubling≥30mg/g analysis, and should its reported status be distinguished from continuous ACR and the original composite component?

### F-ST1-007

**Title:** Favor-direction labels are reversed on both ACR active/placebo ratio plots.

**Relationships:** S082; S_W. **Compared roles:** REPORT supplement [p18, eFigure 2 axis and direction arrows](../../../joi190122supp2_prod.pdf#page=18), [p19, eFigure 3 axis and direction arrows](../../../joi190122supp2_prod.pdf#page=19). REPORT supplement [p11, eTable 6 ratio definition](../../../joi190122supp2_prod.pdf#page=11) corroborates the active/placebo quantity; REPORT main [p3, ACR doubling definition](../../../jama_de_boer_2019_oi_190122.pdf#page=3) and [p4, ACR increase narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) corroborate progression direction. PLAN [p17](../../../joi190122supp1_prod.pdf#page=17) also calls ACR increase progression and does not introduce a separate conflicting relationship.

**Printed values and labels:** Both plots explicitly label ratio of change active/placebo(95%CI), with null 1 and ticks0.5,0.7,1,1.3,1.7. The left side<1 is labeled Favors Placebo; the right side>1 is labeled Favors Vitamin D or Favors Omega-3. eTable 6 defines individual change as follow-up/baseline ratio and treatment effect as active/placebo ratio. ACR increases are the reported progression outcome. All26 plotted rows retain these same axes.

**Rule and calculation:** Let R=(ACR follow-up/ACR baseline)_active divided by the corresponding placebo ratio, using the plot's stated quantity. R<1 means less ACR increase with active assignment; R>1 means more ACR increase with active assignment. Thus the favorable direction of an outcome defined as ACR progression is opposite the printed arrows. No crude subgroup ratio is used to reproduce an adjusted forest coefficient. Direction is a logical consequence of the explicit ratio definition; numerical endpoint rounding does not alter sides ofnull 1 or either arrow label.

**Focus area:** B. **Proposed review domain:** statistical_results. **Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Direction of every overall/subgroup ACR treatment effect in eFigures 2/3, especially a reader interpreting a left-side estimate as favoringplacebo despite a smaller active/placebo ACR change ratio.

**Why context does not resolve it:** Route A category 2 applies to a direction statement reversing the printed quantity. The axis says active/placebo, and two identically oriented favor labels are printed; choosing whether to reverse the axis estimand or the favor wording cannot be adjudicated from immediate context.

**Alternatives and missing definitions:** The favor labels may reflect a copied eGFRplot convention, or the ratio reference group may have been intended in the opposite order. These are possible production explanations only. The figure-column count pattern is reviewed separately by the numeric lane; it is not used to establish this direction finding.

**Human question:** Do the plots represent active/placebo ACR change as labeled, and which favorable direction should be attributed to each side ofnull 1 in both figures?

### F-ST1-008

**Title:** Prespecified outcome hierarchy changes from the original protocol to the reported trial.

**Relationships:** S003, S054, S055, S066, S069, S070; primary P_R; all relationships P_R, P_P. **Compared roles:** PLAN original [p17, sectionsVIb/VIc](../../../joi190122supp1_prod.pdf#page=17), PLAN amended [p32, section15b](../../../joi190122supp1_prod.pdf#page=32); REPORT [p2, Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=2) and [p3, secondary outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3).

**Printed statements:** Original protocol labels continuous baseline-to-year 4 urineACR change primary and eGFR change secondary. Implemented addendum states that baseline-to-year 5 eGFR change supplants prior albuminuria/eGFR primary outcomes; ACR change becomes secondary. Report identifies eGFR primary and ACR secondary, and explicitly discloses a2016 primary-outcome modification.

**Rule and calculation:** A prespecified outcome whose primary/secondary status changes falls under route A category 5. Original-versus-reported hierarchy is different even though the supplied amendment and report document the revision. Logical status comparison; display-precision arithmetic not applicable.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Status and time point assigned to the primary 0.9 eGFR contrasts and secondary continuous ACR results when extracting original-versus-final prespecification.

**Why context does not resolve it:** Route A category 5 registers the reproduced status change; disclosed amendment explains its history but does not erase the changed status.

**Alternatives and missing definitions:** The2016 implemented addendum directly supports an authorized amendment. Classification ambiguity: comparison against the latest amended plan alone reconciles, while the required original-plan/report and plan-version comparison tracks the status change. No undocumented cause or preferred hierarchy is asserted.

**Human question:** Should the reported eGFR primary/ACR secondary hierarchy be attributed to the supplied2016 amendment, with original hierarchy and time points retained in prespecification extraction?

### F-ST1-009

**Title:** Prespecified secondary composite components and decline threshold change.

**Relationships:** S056, S069, S070; primary P_R; all relationships P_R, P_P. **Compared roles:** PLAN original [p17, sectionVIc](../../../joi190122supp1_prod.pdf#page=17), PLAN amended [p32, section15b](../../../joi190122supp1_prod.pdf#page=32); REPORT [p3, secondary outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p4, composite results](../../../jama_de_boer_2019_oi_190122.pdf#page=4), and [p9, Table 3](../../../jama_de_boer_2019_oi_190122.pdf#page=9).

**Printed statements and values:** Original composite contains ACR doubling with final ACR≥30mg/g, absolute eGFR loss≥12mL/min over 4 years, ESRD and/or death. Amended and reported composite contains relative eGFR loss≥40%, ESRD/kidney failure and/or death, evaluated throughyear 5; ACR progression is absent from that composite. Report gives composite HR0.92(0.68–1.25) and1.11(0.81–1.50).

**Rule and calculation:** A changed prespecified composite definition qualifies under route A category 5. Component removal and absolute-versus-relative decline are distinct outcome definitions. For illustration only,12/eGFRbaseline equals40% only at baseline 30; the two thresholds are not generally equivalent. No baseline distribution or individual event recoding is inferred. Logical endpoint comparison; display rounding does not reconcile component presence/absence or threshold type.

**Focus area:** D. **Proposed review domain:** protocol_report. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Definition and original-versus-final prespecified status of the164-event secondary composite and its two reportedHRs.

**Why context does not resolve it:** Route A category 5 registers the reproduced composite change. Latest amendment documents the current definition but does not make it identical to the original.

**Alternatives and missing definitions:** The supplied2016 amendment is direct documentary support for the revision. Classification ambiguity: final-plan/report definitions agree; original-plan/report and plan-version definitions differ. No outcome under the original composite is reconstructed from current counts.

**Human question:** Which amendment should be cited for removal of ACR progression and replacement of absolute≥12 loss with relative≥40% loss, and which composite definition belongs to the extracted reportedHRs?

## Excluded observations

Only apparent issues intentionally not emitted are listed; reconciled checks appear below.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainp8 Table 2; supppp9–14 eTables 4–9 | Raw arithmetic on rounded arm means/changes need not equal the explicitly adjusted/imputed treatment contrast; no source says the contrast is crude. | MODEL_VERSUS_CRUDE |
| REPORT mainp9 Table 3 and suppp15 eTable 10 | HR need not equal the ratio of event counts or rounded incidence rates; it is explicitly from Cox regression. | MODEL_VERSUS_CRUDE |
| REPORT suppp12 eTable 7; p13 eTable 8 | Some normal diagnostics from central printed ratio/CI values differ from printed P, but half-unit estimate/endpoint rounding permits reconciliation; no exact Rubin df is supplied. For eTable 8 D, ratio1.015 within printed1.02±.005 andSE≈.092 givesP≈.871, compatible with.87. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT mainp8 Figure 3 BMI≥30 | A closing parenthesis is missing afterSD15.0; the numeric value and interpretation remain evident. | NOTATION_OR_TYPOGRAPHY |
| PLANp33 section15g vs REPORT suppp17 eFigure 1 | Planned biomarker-replacement LMM versus printed correlations r−.05/−.02: the figure does not identify a regression coefficient or state that correlations replaced the planned model. Nonreporting alone does not establish a conflict for this exploratoryanalysis. | CONDITIONAL_OR_UNREPORTED |
| PLANp32 Equation 1 versus Equation 2 | Equation 1 lacks a time-main term; adding one would assume an unrestricted interaction model not independently required by a supplied statement. A stated constrained model is not questioned merely because another model could be preferred. | OUT_OF_FOCUS |
| PLANp17 versus p19 Table 2/narrative, with amendedp32 | Originalsecondary versus co-primary eGFR terminology: the final relied-on plan explicitly replaces prior endpoints with year 5 eGFR primary; no ambiguity in the current primary decision rule or extracted estimand remains. | CONTEXT_RESOLVES |
| REPORT mainp3 clinical relevance wording | Detectable2.3difference and surrogate3.75difference are distinct stated thresholds, and the report's confidence-limit claim explicitly uses3.75; wording does not assert their numeric equivalence. | TERMINOLOGY_OR_WORDING |

## Estimate–interval–P diagnostics

Diagnostic approximations only: linear SE=(U−L)/3.92; ratio/logHR SE=(logU−logL)/3.92; diagnostic two-sided normalP from the displayed estimate. These calculations do not assert a common unreported test, Rubin df or confidence estimator. Every printed effect is inside its ordered interval; all ratio intervals below include1 and all linear contrast intervals include0. P values are nonsignificant except the printed boundary.05, which is not<.05. Interval/P decisions therefore reconcile. Diagnostic differences were checked using half-unit rounding before any exclusion; no route A category 1 conflict is excluded.

| Relationship / matched row | Estimate | Lower | Upper | Printed P | Diagnostic SE (linear or log scale) | Diagnostic normal P |
|---|---:|---:|---:|---:|---:|---:|
| S018 | 0.9 | -0.7 | 2.5 | 0.25 | 0.8163 | 0.2702 |
| S020 | 0.9 | -0.7 | 2.6 | 0.27 | 0.8418 | 0.2850 |
| S080 eTable 4 D | 0.87 | -0.83 | 2.58 | 0.32 | 0.8699 | 0.3173 |
| S080 eTable 4 O | 0.09 | -1.61 | 1.8 | 0.92 | 0.8699 | 0.9176 |
| S080 eTable 5 D | 0.89 | -0.74 | 2.52 | 0.28 | 0.8316 | 0.2845 |
| S080 eTable 5 O | 0.42 | -1.22 | 2.06 | 0.61 | 0.8367 | 0.6157 |
| S043 | 0.92 | 0.68 | 1.25 | 0.61 | 0.1553 | 0.5914 |
| S044 | 0.97 | 0.63 | 1.51 | 0.9 | 0.2230 | 0.8914 |
| S045 | 1.34 | 1 | 1.8 | 0.05 | 0.1499 | 0.0510 |
| S046 | 1.11 | 0.81 | 1.5 | 0.52 | 0.1572 | 0.5067 |
| S047 | 0.99 | 0.64 | 1.54 | 0.97 | 0.2240 | 0.9642 |
| S048 | 1.08 | 0.81 | 1.44 | 0.6 | 0.1468 | 0.6000 |
| S080 eTable 6 D | 0.99 | 0.84 | 1.17 | 0.9 | 0.0845 | 0.9054 |
| S080 eTable 6 O | 0.96 | 0.81 | 1.14 | 0.64 | 0.0872 | 0.6396 |
| S080 eTable 7 D | 1.03 | 0.86 | 1.22 | 0.77 | 0.0892 | 0.7404 |
| S080 eTable 7 O | 0.93 | 0.78 | 1.11 | 0.44 | 0.0900 | 0.4201 |
| S080 eTable 8 D | 1.02 | 0.85 | 1.22 | 0.87 | 0.0922 | 0.8299 |
| S080 eTable 8 O | 0.99 | 0.83 | 1.19 | 0.94 | 0.0919 | 0.9129 |
| S080 eTable 9 D | 0.99 | 0.84 | 1.17 | 0.9 | 0.0845 | 0.9054 |
| S080 eTable 9 O | 0.98 | 0.83 | 1.16 | 0.8 | 0.0854 | 0.8130 |
| S081 D40FK | 1.03 | 0.68 | 1.58 | 0.88 | 0.2151 | 0.8907 |
| S081 D30FKD | 0.82 | 0.64 | 1.05 | 0.12 | 0.1263 | 0.1161 |
| S081 D30FK | 0.82 | 0.61 | 1.09 | 0.17 | 0.1481 | 0.1802 |
| S081 D30 | 0.79 | 0.59 | 1.06 | 0.12 | 0.1495 | 0.1148 |
| S081 O40FK | 1.07 | 0.7 | 1.63 | 0.77 | 0.2156 | 0.7537 |
| S081 O30FKD | 0.96 | 0.75 | 1.23 | 0.77 | 0.1262 | 0.7463 |
| S081 O30FK | 0.89 | 0.66 | 1.19 | 0.44 | 0.1504 | 0.4384 |
| S081 O30 | 0.86 | 0.64 | 1.15 | 0.31 | 0.1495 | 0.3131 |

The main DCI−0.7,2.5 permits true difference0.94 and limits near−0.66,2.54 (all within half-unit intervals), giving diagnosticP≈.250, which demonstrates compatibility with the printed.25. The omegaCI−0.7,2.6 permits difference near0.93 and symmetric endpoints near−0.72,2.58, givingP≈.269, compatible with.27. No finite-MI calculation is claimed from these examples.

## Full grouped-display checks

S080 covers eTables 4–9 in full: six time rows per table, both arm means/geometric means and their printed CIs, both arm changes and their printed CIs, all 24 nonbaseline between-arm contrasts, and all 12 printed year-5 P values. Containment, interval order and null/P checks reconcile. Baseline reference rows are not inferential zero-effect conclusions. Modeled/imputed quantities remain distinct from raw changes in marginal means. The eTable 7 participant/exclusion-footnote conflict is covered by the independent numeric lane and remains relevant to mechanical recheck: comparing 991 to 944 alone falls under 5%, whereas comparing printed exclusion count 320 to 1311−944=367 exceeds 5%.

S081 covers all eight eTable 10 outcome/intervention rows, both rates and their CIs, rate differences/CIs, HR/CIs and P values. Every estimate is contained and all HR/P significance decisions reconcile. A normal incidence-rate diagnostic SE=rate/sqrt(events) reproduces the rate intervals within displayed precision across rows, with no printed outlier exceeding the inclusion threshold. Event-time/person-time details are absent, so no Cox estimate is replaced with a crude ratio.

S082 covers both correlation panels and all 26 ACR forest rows: 15 in eFigure 2 and 11 in eFigure 3, including all geometric means/geometric SDs, Ns, interaction P values, markers/intervals and captions. Every graphical interval contains its marker and spans one. Interaction P values test subgroup heterogeneity, not one subgroup effect. Numeric graph coordinates were not invented. Every direction arrow is included in the single repeated-pattern F-ST1-007.

Original sample-size diagnostics use supplied ANCOVA assumptions only. With total 1200 and equal marginal arms of 600, eGFR residual SD=25×sqrt(1−.834²)=13.794 and difference SE=.7964. Log-ACR residual SD=1.59×sqrt(1−.78²)=.9950 and difference SE=.05745. Favorable ACR percentage changes are treated as decreases, consistent with the protocol's reduction hypothesis. Resulting power rows are respectively 70.9,78.9,85.4,90.4,94.0,96.5% and 80.8,90.0,95.6,98.4,99.5,99.9%, reconciling the printed rows. Attrition of 10%/30% yields powers near 93%/86%; combination-pair arms of 300 yield approximately 80% at eGFR difference 3.2 and ACR reduction 20%. The latter ACR diagnostic around 78.4% versus printed 80% is within the relative 5% display rule. Adherent effects 17/.8=21.25% and 2.6/.8=3.25 agree with 21%/3.2 at allowed rounding. The amended simulation cannot be regenerated without the preliminary variation/covariances, which are not substituted from the original unrelated cohort.

## Per-relationship completion records

### S001 — PASS_1_COMPLETE

Primary vitamin D estimates, CIs and nonsignificance agree across abstract, Key Points, narrative and Table 2. Every estimate is contained in its ordered CI; active-minus-placebo direction is positive.

### S002 — PASS_1_COMPLETE

Primary omega-3 estimates, CIs and nonsignificance agree across matched locations. Difference 0.9 (−0.7, 2.6) includes zero and has the reported positive direction.

### S003 — PASS_1_COMPLETE

Original ACR primary versus amended/reported eGFR primary is F-ST1-008 under route A, category 5. The supplied 2016 amendment is a documented alternative, not an exclusion ground.

### S004 — PASS_1_COMPLETE

1320 × 80% = 1056 versus plan 1058 is within display precision. Final simulation lacks the preliminary variance/covariance inputs needed for exact power reproduction; no substitute variance is assumed.

### S005 — PASS_1_COMPLETE

Repeated observations, random intercept, categorical time and year-5 interaction test are coherent. Fixed primary covariates differ from amended Equation 2: F-ST1-003. Two-sided alpha .05 and exploratory secondary interpretation agree.

### S006 — PASS_1_COMPLETE

All randomized participants and 20 imputations differ from the amended follow-up-conditioned population and 10 imputations: F-ST1-001/002. Complete-case sensitivity is a distinct population. Adherence comparison is F-ST1-004.

### S007 — PASS_1_COMPLETE

Subgroup P values test heterogeneity, rather than individual subgroup effects. Bioavailable 25(OH)D analysis is absent: F-ST1-005. BMI and fish-intake additions are disclosed.

### S008 — PASS_1_COMPLETE

Cox PH and Schoenfeld checks match the stated time-to-event design. Risk sets, event times, tie method and exact test type are unavailable; no printed HR/CI/P conflict is established.

### S009 — PASS_1_COMPLETE

Biomarker differences 11.6 ng/mL and 1.3 percentage points have the expected active-exposure direction and stated P<.001. Test identity and exact sample counts are absent; SDs alone do not reproduce the tests.

### S010 — PASS_1_COMPLETE

Full-imputed −12.7 and paired-participant −12.4 changes describe different populations. Both CIs are ordered and contain their estimates, so they are not competing estimates for one matched analysis.

### S011 — PASS_1_COMPLETE

Treatment interaction P=.42 supports marginal factorial comparisons under the stated rule. Sensitivity estimates and all subgroup interaction tests reconcile; biomarker correlations are checked separately.

### S012 — PASS_1_COMPLETE

Composite HRs include one and support nonsignificance. Other secondary triples reconcile. Standalone categorical ACR prespecification is F-ST1-006.

### S013 — PASS_1_COMPLETE

Report explicitly labels the additional composites post hoc, matching eTable 10. All eight inferential triples include the null and have P>.05.

### S014 — PASS_1_COMPLETE

No printed Schoenfeld statistic conflicts with the PH narrative. Discussion nonsignificance agrees with results. “Akin to slope” is a contextual analogy to five-year change.

### S015 — PASS_1_COMPLETE

Primary upper CI limits 2.5 and 2.6 exclude the stated 3.75 five-year improvement threshold; .75 × 5 = 3.75. No noninferiority or equivalence conclusion is claimed.

### S016 — PASS_1_COMPLETE

Baseline counts 701+607=1308 reconcile with four missing of 1312. Both mean CIs contain their estimates and have ordered endpoints.

### S017 — PASS_1_COMPLETE

Every vitamin D year-2 mean, change and contrast CI is ordered and contains its estimate. Positive contrast direction agrees with the arm changes. No year-2 P is printed, as inference is reserved for year 5.

### S018 — PASS_1_COMPLETE

Vitamin D year-5 contrast 0.9 (−0.7, 2.5), P=.25 agrees on significance. Normal diagnostic P=.270 reconciles after half-unit rounding; no Rubin degrees of freedom are inferred.

### S019 — PASS_1_COMPLETE

Every omega-3 baseline/year-2 CI contains its estimate. Negative year-2 adjusted contrast agrees with greater active-arm decline. Rounded arm changes are not substituted for a modeled contrast.

### S020 — PASS_1_COMPLETE

Omega-3 year-5 contrast 0.9 (−0.7, 2.6), P=.27 agrees on significance. Normal diagnostic P=.285 reconciles after rounding. Footnote distinguishes imputed summaries from adjusted contrasts.

### S021 — PASS_1_COMPLETE

Figure 3 overall forest estimate is positive and its CI spans zero, matching Table 2. The printed group-count assignment discrepancy belongs to the numeric lane; SDs do not reconstruct the adjusted effect.

### S022 — PASS_1_COMPLETE

White subgroup marker is contained and its interval spans zero. Race P=.58 is a shared interaction test, not a test of the white subgroup effect.

### S023 — PASS_1_COMPLETE

Black subgroup marker is contained and its interval spans zero. Race P=.58 agrees with nonsignificant heterogeneity; the adjusted forest estimate remains separate from the crude mean difference.

### S024 — PASS_1_COMPLETE

ACR<30 subgroup forest is positive with a CI spanning zero. P=.36 tests heterogeneity across ACR strata, rather than this stratum's null effect.

### S025 — PASS_1_COMPLETE

ACR≥30 subgroup marker is contained and its CI spans zero. Shared P=.36 is nonsignificant heterogeneity; no numeric CI is fabricated from counts and SDs.

### S026 — PASS_1_COMPLETE

Low 25(OH)D subgroup forest is positive and spans zero. P=.15 is the categorical interaction test, not this subgroup's effect test.

### S027 — PASS_1_COMPLETE

Middle 25(OH)D subgroup marker is contained and its interval spans zero; shared interaction P=.15 agrees with the narrative.

### S028 — PASS_1_COMPLETE

High 25(OH)D subgroup forest is negative and spans zero, consistent with printed changes −12.3 versus −11.5. Interaction P=.15 remains a different null.

### S029 — PASS_1_COMPLETE

Both eGFR strata have positive markers contained in CIs spanning zero. Interaction P=.18 agrees with the hypothesis-generating narrative.

### S030 — PASS_1_COMPLETE

Both lower BMI strata have positive markers and CIs spanning zero. Global BMI interaction P=.79 supplies no significant heterogeneity.

### S031 — PASS_1_COMPLETE

BMI≥30 forest is positive and spans zero; P=.79 is global heterogeneity. Missing parenthesis after SD 15.0 changes no numeric reading and is excluded.

### S032 — PASS_1_COMPLETE

Both omega-assignment strata have positive markers and CIs spanning zero. P=.42 agrees with the primary treatment-interaction rule. Numeric lane covers crossed-cell count headers.

### S033 — PASS_1_COMPLETE

Figure 4 overall forest is positive and spans zero, matching the primary omega result. Count/header assignment is independently checked by the numeric lane.

### S034 — PASS_1_COMPLETE

Low EPA/DHA forest is positive and spans zero. P=.72 tests interaction across strata and is not an individual subgroup P value.

### S035 — PASS_1_COMPLETE

High EPA/DHA forest is positive and spans zero; shared P=.72 agrees with nonsignificant heterogeneity. Crude means/SDs do not recreate the adjusted interval.

### S036 — PASS_1_COMPLETE

ACR<30 omega subgroup forest is positive and spans zero. P=.70 is the shared ACR interaction test.

### S037 — PASS_1_COMPLETE

ACR≥30 omega subgroup forest is near zero and its CI spans zero. A negative crude mean difference need not equal the adjusted marker. P=.70 tests interaction.

### S038 — PASS_1_COMPLETE

Low hsCRP subgroup forest is positive and spans zero. P=.73 tests heterogeneity, with no significant subgroup-effect claim.

### S039 — PASS_1_COMPLETE

High hsCRP subgroup forest is positive and spans zero; direction agrees with the printed changes and interaction P=.73.

### S040 — PASS_1_COMPLETE

Lower fish-intake forest is positive and spans zero. Interaction P=.51 is nonsignificant; this exploratory subgroup addition is disclosed.

### S041 — PASS_1_COMPLETE

Higher fish-intake forest is positive and spans zero. Shared P=.51 agrees with the stated lack of heterogeneity.

### S042 — PASS_1_COMPLETE

Both vitamin D assignment strata have positive markers and CIs spanning zero. P=.42 agrees with the main interaction result; adjusted contrasts are not replaced by crude differences.

### S043 — PASS_1_COMPLETE

Vitamin D composite HR .92 (.68, 1.25), P=.61 has containment, ordered endpoints and consistent null inclusion. Rate estimates and differences lie within their CIs.

### S044 — PASS_1_COMPLETE

Vitamin D ≥40% decline HR .97 (.63, 1.51), P=.90 reconciles. Rate difference −.1 (−.7, .6) includes zero. Person-time denominators are absent.

### S045 — PASS_1_COMPLETE

Vitamin D ACR HR 1.34 (1.00, 1.80), P=.05 is at the printed boundary; neither interval excludes the null nor printed P is<.05. Endpoint prespecification is F-ST1-006.

### S046 — PASS_1_COMPLETE

Omega composite HR 1.11 (.81, 1.50), P=.52 reconciles. Rate difference .3 (−.5, 1.1) includes zero. Cox HR and rounded incidence rates are separate quantities.

### S047 — PASS_1_COMPLETE

Omega ≥40% decline HR .99 (.64, 1.54), P=.97 reconciles. Equal event counts do not require HR exactly one, because event timing and risk sets matter.

### S048 — PASS_1_COMPLETE

Omega ACR HR 1.08 (.81, 1.44), P=.60 and rate difference .3 (−.8, 1.4) reconcile. Standalone outcome status is F-ST1-006.

### S049 — PASS_1_COMPLETE

Tests explicitly use null HR=1. Baseline exclusions of four/one match measurable outcomes. Standalone time-to-ACR-doubling is called prespecified but absent from the amended endpoint list: F-ST1-006.

### S050 — PASS_1_COMPLETE

Discussion identifies favorable subgroup point estimates but null-crossing CIs and nonsignificant interaction, explicitly as hypothesis-generating. Primary five-year nonsignificance agrees.

### S051 — PASS_1_COMPLETE

Eligibility and analysis-population implications were inspected. Age and insulin-exclusion comparisons are assigned to the cross-source design lane; no unstated eligibility model is inferred.

### S052 — PASS_1_COMPLETE

Individual factorial randomization in blocks of eight matches the report. Age-only versus age/sex/race strata is assigned to the cross-source design lane; there is no cluster or paired-test mismatch.

### S053 — PASS_1_COMPLETE

D 2000 IU and EPA+DHA 840 mg within a 1000-mg capsule match total dose quantities. Component-ratio deviations are within precision. IU/µg pairing is assigned to the numeric lane.

### S054 — PASS_1_COMPLETE

Original ACR primary becomes secondary in the amended/report hierarchy: F-ST1-008. The amendment is documented. Current log-LMM ratio representation is coherent.

### S055 — PASS_1_COMPLETE

Original eGFR secondary becomes primary: F-ST1-008. The estimating-equation comparison is assigned to the cross-source lane. “Dichotomous” beside explicit continuous equations does not establish a binary model.

### S056 — PASS_1_COMPLETE

Original composite includes ACR progression and absolute ≥12 loss; amended/report composite removes ACR and uses relative ≥40% loss: F-ST1-009. The documented amendment remains an alternative.

### S057 — PASS_1_COMPLETE

Original additive/multiplicative interaction is superseded by the final LMM interaction specification. Original joint-treatment binary indicator is coherent and is not treated as an arithmetic sum.

### S058 — PASS_1_COMPLETE

Treatment interaction P=.42>.05 supports marginal contrasts under the amended conditional rule. No significant printed interaction requires the unreported combination comparisons.

### S059 — PASS_1_COMPLETE

Original ANCOVA exp(β)−1 and current LMM exp(β) are different representations; the amendment authorizes log-LMM. Wording alone does not establish a conflicting extracted effect measure.

### S060 — PASS_1_COMPLETE

Original ANCOVA/chi-square is explicitly replaced by final LMM/discrete Cox. Both are stated choices; no preferred model or unreported rank-sum substitution is assumed.

### S061 — PASS_1_COMPLETE

Original complete-case ITT is superseded by the amended plan. Current follow-up-conditioned versus all-randomized difference is F-ST1-001; imputation count is F-ST1-002. Nominal alpha/exploratory interpretation agree.

### S062 — PASS_1_COMPLETE

Original optional covariates are secondary; final model retains conditional sensitivity terms rather than fixed primary adjustment. This primary term-set comparison is F-ST1-003. Conditional mediation alone does not imply an omitted mandatory analysis.

### S063 — PASS_1_COMPLETE

Original subgroup definitions match reported total 25(OH)D, ACR, eGFR, race, omega index and CRP. Final bioavailable subgroup is absent: F-ST1-005. Individual intervals are not interaction tests.

### S064 — PASS_1_COMPLETE

Original adherence threshold ≥80% is reiterated in the final plan and differs from the report: F-ST1-004. Printed biomarker correlations alone do not identify a replacement regression method.

### S065 — PASS_1_COMPLETE

Original ANCOVA power diagnostics use only supplied SDs, baseline correlations and 1200 follow-up participants. Exact amended preliminary variance is not substituted from historical cohorts.

### S066 — PASS_1_COMPLETE

Every original power row reproduces within display precision. Attrition/adherence and combination comparisons reconcile. Original/final outcome hierarchy is F-ST1-008; old table wording does not create ambiguity in the current decision rule.

### S067 — PASS_1_COMPLETE

Joint incidence is not reconstructed by summing overlapping components. Diagnostic two-proportion tests support the stated original RR ranges. Graph-only power curves do not supply exact additional observations.

### S068 — PASS_1_COMPLETE

Parent DSMB z=3 gives two-sided normal P=.00270, matching .0027. This is a parent cancer/CVD rule, not an inferred ancillary interim rule; no reported kidney stopping decision conflicts.

### S069 — PASS_1_COMPLETE

Implemented 2016 amendment matches report disclosure. Hierarchy/composite revisions are F-ST1-008/009. Older two-/four-year history does not change the current five-year decision rule.

### S070 — PASS_1_COMPLETE

Amended eGFR primary and continuous ACR/≥40% loss/composite definitions match final report, with original revisions F-ST1-008/009. Standalone categorical ACR prespecification is F-ST1-006.

### S071 — PASS_1_COMPLETE

Amended follow-up-conditioned population and M=10 differ from reported all randomized and M=20: F-ST1-001/002. Chained-equation predictors are not fully detailed in the report but no predictor conflict is established.

### S072 — PASS_1_COMPLETE

Printed interaction model and P=.42 decision were inspected. Adding a time-main term would infer an unrestricted model not independently required by supplied text; the apparent omission is excluded without proposing a preferred model.

### S073 — PASS_1_COMPLETE

Final random intercept, categorical treatment/time interaction and year-5 inference match the report, except fixed primary covariates: F-ST1-003. No continuous numeric slope is assumed from categorical-time notation.

### S074 — PASS_1_COMPLETE

“Discrete Cox” versus “Cox” alone does not establish a changed tie/risk-set method. Conditional mediator exploration does not require output in the absence of its condition. Fixed primary adjustment is F-ST1-003.

### S075 — PASS_1_COMPLETE

Planned bioavailable 25(OH)D primary subgroup is not reported: F-ST1-005. Race-hypothesis wording changes in a supplied update while tests remain two-sided and reported groups remain matched.

### S076 — PASS_1_COMPLETE

Adherence threshold/continuity differs: F-ST1-004. Planned biomarker-replacement LMM versus printed r alone cannot establish replacement because no regression method/coefficient is named.

### S077 — PASS_1_COMPLETE

Final 2000-replication simulation, equal allocation, 1058 participants and 2.3/80% result agree with the report at precision. Preliminary variance/covariances are absent, preventing exact simulation reconstruction.

### S078 — PASS_1_COMPLETE

Post-shift standard calibration and pre-shift harmonization are sequential coherent operations. 5.96 versus 5.961 is display precision. Correlation .999 and identity plot agree; QC sample data are unavailable for exact SEs.

### S079 — PASS_1_COMPLETE

Response denominators and longitudinal adherence N=1032 are distinct. Two-thirds on two/three or four/six questionnaires is explicitly defined. Planned ≥80% comparison is F-ST1-004.

### S080 — PASS_1_COMPLETE

All 36 continuous-table time rows, arm mean/change intervals, 24 nonbaseline contrast intervals and 12 printed year-5 P values were checked. Containment/order/null decisions reconcile. eTable 7 population/exclusion inconsistency is assigned to the numeric lane.

### S081 — PASS_1_COMPLETE

All eight post hoc outcome rows, counts, rates/CIs, differences/CIs, HR/CIs and P values were checked. Every interval contains its estimate and all HR intervals include one with P>.05. Rate-SE diagnostics reproduce displayed precision.

### S082 — PASS_1_COMPLETE

Both biomarker panels and all 26 ACR forest rows were checked. All graphical intervals contain markers and span one; interaction P values are nonsignificant. Reversed favor-direction arrows are F-ST1-007. Count-column comparisons belong to the numeric lane.

## Reconstruction limits and handoff

No supplied raw longitudinal measurements, imputed datasets, covariance matrices, pooling degrees of freedom, event times/risk sets, or final preliminary simulation variance permit exact model regeneration. These are named reconstruction limits, not source-unit or relationship omissions. No inferential relationship was left unchecked, and no source or reusable artifact was changed. The next statistical pass must use a different newly spawned runtime ID and revisit every S ID using the complete screened ledger and direct-source mechanical recheck.

Durable outputs: statistics/relationship_inventory.md and checkers/statistical_pass_1.md. Scope 82/82; findings 9; excluded observations 8. Runtime /root/statistical_pass_1.

