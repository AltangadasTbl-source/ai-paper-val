# Workflow 1.6.2 Exact-Source Evidence Recheck

Scope: every registered stable ID, C001, C002, C003, C004, C005 and C006, including each affected location in the registered patterns. All remain **Pending Human Adjudication**. This artifact records evidence facts and classification; it assigns no disposition.

The complete QUALITY_CONTROL_SCOPE.md and the mechanical recheck/classification contract were read, together with the current ledger, screening log, source inventory and tooling record. The supplied PDFs are authority. I independently viewed the current source-page renders listed below, created directly from those PDFs at 200 dpi by PyMuPDF 1.26.4 through the permitted fallback helper. The provenance in screening/inclusion_screen.md identifies the exact source and PDF page for every render. Fresh directly extracted main/results text was also used to search the complete reporting scope; OCR and mapper/checker transcriptions were locators only. No older scientific review or external evidence was used. No new extraction, rendering or OCR was needed at this stage, and no source or reused artifact was modified.

## Confirmed classification table

Inclusion audit remains PENDING for the separate quality-control auditor. Every classification agrees with registration; no role or relationship correction is required.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | REPORT main article versus PLAN manual and SAP; PLAN manual narrative versus PLAN appendix and SAP | reproduced | PENDING | F-XS-003, F-XS-1002 |
| C002 | protocol_report | P_R | P_R | REPORT main article versus PLAN protocol and SAP | reproduced | PENDING | F-XS-002, F-ST1-001, F-ST1-1003 |
| C003 | protocol_report | P_R | P_R | PLAN protocol and SAP versus REPORT main article and results supplement | reproduced | PENDING | F-XS-001, F-ST1-002, F-ST1-004, F-ST1-1002, F-ST1-1004 |
| C004 | plan_material | P_P | P_P | PLAN protocol Table 2 count and denominator versus percentage | reproduced | PENDING | F-NUM-1001, F-ST1-1001 |
| C005 | plan_material | P_P | P_P | PLAN manual Table 1 printed factor versus relationship supported by other cells | reproduced | PENDING | F-NUM-2001 |
| C006 | statistical_results | S_W | S_W | REPORT results supplement interval values versus its interval-method footnotes | reproduced | PENDING | F-ST1-003 |

## C001 — Moderate-hyperglycemia qualification pathways

**Status:** Pending Human Adjudication. **Evidence state:** reproduced. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, P_P. **Finding IDs:** F-XS-003, F-XS-1002.

### Every affected source location

Every row was found and visually matched to its exact supplied source page.

| Exact source location | Content role | Independently matched source/comparator fact |
|---|---|---|
| [Main PDF p1, abstract](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1) | REPORT | Hyperglycemia 66.7% versus 49.8%; adjusted RR 1.33, 95% CI 1.17–1.51. This establishes the named abstract result affected by the definition comparison. |
| [Main PDF p3, Outcomes](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3) | REPORT | Moderate glucose 120–180 mg/dL on two consecutive determinations at least six hours apart OR more than two determinations within 24 hours without intervening normal values. Severe glucose is described as greater than 180 mg/dL. |
| [Main PDF p6, Safety Outcomes](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=6) | REPORT | Increased adverse-event experience is attributed primarily to moderate hyperglycemia; serious adverse events are described separately. |
| [Results PDF p5, eTable 3 hyperglycemia](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5) | REPORT | 214 (66.7%) versus 156 (49.8%), RR 1.33 (1.17, 1.51). This corroborates the result rather than supplying a conflicting report relationship. |
| [Manual PDF p39, Chapter 7 hyperglycemia](../../../joi250072supp2_prod_1761000786.6938.pdf#page=39) | PLAN | Moderate includes the same OR branch as the report. Severe includes the repeated >180 mg/dL OR branch and initiation of insulin. Life-threatening >600 mg/dL uses four hours for the separated determinations and also includes the OR branch. |
| [Manual PDF p59, Appendix A hyperglycemia row](../../../joi250072supp2_prod_1761000786.6938.pdf#page=59) | PLAN | Moderate requires two consecutive determinations at least six hours apart, with no additional OR branch. Severe retains the separated-determination or insulin criterion but omits the additional readings branch; life-threatening retains two determinations at least four hours apart without that branch. |
| [SAP PDF p11, §3.2.4.1 hyperglycemia](../../../joi250072supp3_prod_1761000786.6988.pdf#page=11) | PLAN | Moderate prints two determinations at least six hours apart, without the extra OR branch or consecutive qualifier. Severe prints two >180 mg/dL determinations at least six hours apart or initiation of insulin; life-threatening prints two >600 mg/dL determinations at least four hours apart. |

**Applicable rule and reproduced comparison:** Route B, focus D. This is a substantive event-definition comparison for an abstract-reported result; the workflow explicitly permits that tier of comparison. The two moderate criterion lists are not logically identical: three qualifying determinations at hours 0, 1 and 2 without normal intervening values can satisfy the report/manual-narrative alternative without satisfying the separated-determination criterion. This is a logical counterexample, not an assertion that any participant had those measurements. Display-precision intervals are inapplicable to the presence of a logical OR branch; the numerical effect and its CI are not claimed to conflict. Severe and life-threatening locations are retained as associated occurrences of the printed branch pattern, not independently qualifying result comparisons.

**Necessary inputs and exact missing inputs:** The definition texts and abstract/table result are available. Participant-level glucose values, times, event adjudication records, and the actual operational criterion used to generate 214 and 156 are not supplied. The source does not provide a priority rule or disclosed amendment reconciling narrative, toxicity table and SAP.

**Alternative interpretation:** The report and manual narrative may contain the complete operational definition while the toxicity table and SAP summarize it. That is source-grounded because the narrative gives more branches, but no supplied statement explicitly establishes such abbreviation or priority. No observed reclassification or effect-size change follows from the package evidence.

**Direct observation versus inferred explanation:** The printed logical lists differ directly. Abbreviation, source-version priority or implementation history are possible explanations, not observed facts.

**Classification confirmation and ambiguity:** Main/results are REPORT because they present observed trial results. Manual/SAP are PLAN because they prescribe prospective ascertainment/analysis. P_R directly links the reported criterion to different plan lists. P_P directly links the manual narrative to its toxicity appendix and SAP. P_R takes precedence and fixes protocol_report. The results supplement merely corroborates the reported numeric outcome, so it adds neither S_C nor S_W. Unresolved source priority is classification ambiguity; roles themselves are clear.

**Determining recheck fact:** All cited definition texts and named result match the sources, and the logical non-equivalence remains; therefore reproduced.

**Exact remaining human question:** Which moderate-hyperglycemia qualification pathway generated the reported participant counts and adjusted RR, and how should the differing prospective definition lists be reconciled?

## C002 — Ordinal BPD-severity model versus displayed generalized logits

**Status:** Pending Human Adjudication. **Evidence state:** reproduced. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Finding IDs:** F-XS-002, F-ST1-001, F-ST1-1003.

### Every affected source location

Every row was found and visually matched.

| Exact source location | Content role | Independently matched source/comparator fact |
|---|---|---|
| [Main PDF p3, Outcomes](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3) | REPORT | Pragmatic BPD severity is listed as ordinal among secondary outcomes; NIH-definition severity is listed among exploratory outcomes. |
| [Main PDF p8, Table 3 and footnote a](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8) | REPORT | ORs are explicitly estimated by logistic regression, generalized logit. Pragmatic grades 1/2/3 versus no BPD: 0.87 (0.54–1.41), 0.88 (0.55–1.42), 0.99 (0.51–1.89). NIH grades: 1.13 (0.59–2.17), 0.63 (0.30–1.34), 0.87 (0.47–1.63), again versus no BPD. |
| [Protocol PDF p21, secondary/exploratory outcomes](../../../joi250072supp1_prod_1761000786.68881.pdf#page=21) | PLAN | Pragmatic BPD grades are ordered no BPD, grade 1, grade 2, grade 3; NIH severity is no/mild/moderate/severe. |
| [Protocol PDF p25, §5.1](../../../joi250072supp1_prod_1761000786.68881.pdf#page=25) | PLAN | Proportional odds is specified for ordinal outcomes; generalized logits for nominal outcomes with more than two levels. |
| [SAP PDF p32, §9.2.2.3](../../../joi250072supp3_prod_1761000786.6988.pdf#page=32) | PLAN | Pragmatic BPD severity type is expressly Ordinal at 36 weeks PMA. |
| [SAP PDF p33, ordinal continuation](../../../joi250072supp3_prod_1761000786.6988.pdf#page=33) | PLAN | Pragmatic severity coded 0=no BPD, 1=mild, 2=moderate, 3=severe. |
| [SAP PDF p34, §9.2.3.1](../../../joi250072supp3_prod_1761000786.6988.pdf#page=34) | PLAN | NIH-consensus BPD severity type is expressly Ordinal. |
| [SAP PDF p35, NIH coding continuation](../../../joi250072supp3_prod_1761000786.6988.pdf#page=35) | PLAN | NIH severity is coded 0=no BPD, 1=mild, 2=moderate, 3=severe. |
| [SAP PDF p39, §9.5](../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | PLAN | BPD severity/grade is expressly the ordinal-model example: proportional odds, with partial proportional odds or Mantel–Haenszel mean-score fallback if its assumption fails. Generalized logits are specified separately for outcomes without inherent ordering. |

**Applicable rule and reproduced comparison:** Route B, focus D. The planned ordinal cumulative contrasts and the printed category-versus-no-BPD generalized-logit contrasts represent different model outputs. The planned fallbacks do not name the displayed generalized-logit replacement for ordinal severity. The comparison affects the severity contrast extracted from Table 3. Model identity is categorical, so display precision is inapplicable; no adjusted-versus-crude recomputation or preferred-model claim is used. The NIH rows retain the repeated pattern, while the explicit ordinal prospective specification supplies its anchor.

**Necessary inputs and exact missing inputs:** Model-family statements, output labels and all six printed OR/CI pairs are available. Individual-level ordinal outcomes, fitted coefficients/covariances, proportional-odds diagnostics, and the planned ordinal model outputs are not supplied. No explicit amendment or explanation connecting the model families was found in the supplied report/plan passages.

**Alternative interpretation:** The report may deliberately present category-specific ORs in addition to a planned ordinal assessment, or an unreported assumption/convergence assessment may have motivated a model change. The package does not identify the planned ordinal outputs or state that such an assessment led to the displayed family. Generalized-logit estimation is coherent as described; this recheck does not criticize that choice.

**Direct observation versus inferred explanation:** Different named model families and reference-category contrasts are directly printed. The reason for the difference and its possible effect on inference are not directly observed.

**Classification confirmation and ambiguity:** Every compared report passage is REPORT; protocol and SAP are PLAN by prospective content. All conflicts are P_R, hence protocol_report. Consistent plan definitions and models merely corroborate the plan side; they do not create P_P. A possible unreported amendment is the remaining ambiguity.

**Determining recheck fact:** Exact-source model and ordinal definitions match the registered facts and retain the distinct contrast specifications; therefore reproduced.

**Exact remaining human question:** What is the relationship between the prespecified ordinal BPD-severity analyses and the generalized-logit category-specific ORs in Table 3, including any disclosed change and the availability of planned ordinal outputs?

## C003 — Prespecified primary analyses absent or presented with different outcome/group definitions

**Status:** Pending Human Adjudication. **Evidence state:** reproduced. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Finding IDs:** F-XS-001, F-ST1-002, F-ST1-004, F-ST1-1002, F-ST1-1004.

### Every affected source location

Every listed source location was found and visually matched. Absence claims are bounded to the supplied complete main/results reporting scope, not to whether an analysis was actually performed.

| Exact source location | Content role | Independently matched source/comparator fact |
|---|---|---|
| [Protocol PDF p25, §5.1](../../../joi250072supp1_prod_1761000786.68881.pdf#page=25) | PLAN | In addition to ITT analyses, prespecified secondary analyses by treatment received will be performed. |
| [SAP PDF p22, §5](../../../joi250072supp3_prod_1761000786.6988.pdf#page=22) | PLAN | SAF groups infants by actual treatment received; mITT includes treated infants but groups by randomized assignment; PP is also defined. |
| [SAP PDF p29, §7.7](../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) | PLAN | Primary robust-Poisson treatment interactions will investigate site/center, GA group as used in randomization, race and sex. Significant/suggestive interactions may lead to subgroup displays; that later condition does not qualify the initial investigation requirement. |
| [SAP PDF p36, §9.3](../../../joi250072supp3_prod_1761000786.6988.pdf#page=36) | PLAN | Primary model response y=1 is BPD/death and y=0 is survival without BPD. |
| [SAP PDF p37, §9.3 continuation and sample code](../../../joi250072supp3_prod_1761000786.6988.pdf#page=37) | PLAN | BPD_DEATH 1=unfavorable, 0=favorable; RANDSTRAT is the GA randomization stratum; sample robust-Poisson model uses BPD_DEATH as its response. |
| [SAP PDF p38, §§9.4.1–9.4.2](../../../joi250072supp3_prod_1761000786.6988.pdf#page=38) | PLAN | Explicitly prespecified primary-outcome secondary analyses replicate primary methods for mITT, PP and SAF, including an as-treated assessment. An additional baseline-predictor model includes known BPD predictors, for example birth weight, sex and race/ethnicity, with final adjusted RR/CI to be reported. Extra imbalanced characteristics and variable selection are permitted, without removing the stated model/output requirement. |
| [Main PDF p3, statistical analysis](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3) | REPORT | Primary robust-Poisson model adjusts for randomization center and GA; efficacy generally uses ITT, whereas safety/clinical/growth outcomes use actual treatment. |
| [Main PDF p4, Figure 1 and footnotes f,j](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=4) | REPORT | Four treatment switches are displayed, with receipt of either budesonide dose determining the actual-treatment group. Footnote j identifies two primary sensitivity subpopulations: treated ITT and PP; it supplies no SAF primary result. |
| [Main PDF p7, Table 2 and sensitivity/subgroup text](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7) | REPORT | Every Table 2 treatment group is explicitly randomized assignment. Primary RRs: ITT 1.00 (0.90–1.11), treated ITT 1.00 (0.90–1.10), PP 1.00 (0.90–1.11); adjustment is GA strata and pooled center only. Text lists these two sensitivity populations and Figure 2 favorable-outcome subgroups. |
| [Main PDF p9, Figure 2, caption and footnote a](../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=9) | REPORT | Models explicitly concern favorable survival without BPD; GA uses actual clinical estimate regardless of randomization strata. Overall 101/321 versus 102/318, RR 1.00 (0.81–1.24). GA rows 22/140 versus 22/130, RR 0.92 (0.54–1.58), and 79/181 versus 80/188, RR 1.03 (0.82–1.30). Sex RRs 0.88 (0.64–1.22), 1.12 (0.84–1.48); race RRs 1.18 (0.86–1.63), 0.84 (0.61–1.15), 0.93 (0.33–2.66). Printed GA/sex/race P values .72/.28/.33 are found, but their separate interaction-model response is not identified. |
| [Results PDF p2, eTable 1](../../../joi250072supp4_prod_1761000786.6988.pdf#page=2) | REPORT | Treated randomized groups 320/315 and actual-treatment SAF groups 322/313 are distinguished. The table lists population disposition, not the SAF primary endpoint estimate. |
| Main PDF pp1–11 and results PDF pp1–16, complete reporting scope | REPORT | Complete directly extracted current source text and the relevant result-page visuals disclose main Tables 1–3/Figures 1–2 and results eTables 1–8. No separately identified primary SAF fit, extra baseline-predictor fit, site/center interaction result, or adverse-outcome/randomization-GA counterpart to Figure 2 is supplied. |

**Applicable rule and reproduced comparison:** Route A, category 5, focus D: the exact plan requires the listed primary-outcome analyses, while the supplied reporting scope does not identify their outputs or presents different explicitly named outcome/group definitions. SAF is not interchangeable with treated ITT: both include treated infants, but actual versus randomized grouping differs. Complementing outcomes does not preserve a robust-Poisson risk-ratio interaction hypothesis: adverse RR=pA/pB, favorable RR=(1−pA)/(1−pB). Actual GA grouping is expressly stated in Figure 2 rather than inferred from its counts. Display precision cannot reconcile model-output absence, response coding, population grouping or randomization-stratum identity. Printed model estimates are not compared against crude ratios.

**Necessary inputs and exact missing inputs:** All prospective requirements, displayed model/group definitions and report population counts are available. Missing are SAF primary RR/CI, final extra baseline-covariate RR/CI and selected covariates, site/center interaction output, the identified adverse-outcome/randomization-GA interaction models, fitted coefficients/covariances, and participant-level joint data needed to reconstruct them. The source does not identify whether the printed subgroup P values came from a different primary-response model than the captioned favorable-outcome fits.

**Alternative interpretation:** Some required fits may have been performed but omitted for space, or model convergence/early termination may have prompted changes. The SAP expressly permits additional ad hoc analyses, so Figure 2 may be an additional descriptive display. These possibilities do not identify the prespecified missing outputs. If its P values were computed from the planned adverse-outcome model, that would resolve part of the interaction-output question but is not stated in the package.

**Direct observation versus inferred explanation:** Requirements, published model labels, differing grouping definitions and absence of identified outputs in supplied reporting material are direct documentary observations. Nonexecution, convergence failure, numerical changes and causal explanations are not asserted.

**Classification confirmation and ambiguity:** Protocol/SAP are PLAN; main article/results tables are REPORT. All required-analysis-versus-output comparisons are P_R and domain protocol_report. Report disposition tables corroborate different population definitions without creating a report-only conflict; aligned prospective passages add no P_P. Whether an undisclosed amendment or separate source contains the outputs remains unresolved, but neither is supplied evidence.

**Determining recheck fact:** The mandatory primary-analysis language and the stated report scope/definitions match; the missing or differently defined outputs remain unaccounted for within the supplied package; therefore reproduced.

**Exact remaining human question:** Where are the prespecified primary SAF, baseline-predictor and site/center interaction outputs, and what supplied disclosure maps the planned adverse-outcome/randomization-GA interaction analyses to the favorable-outcome/actual-GA display and its P values?

## C004 — Historical protocol Grade 3 count/percentage

**Status:** Pending Human Adjudication. **Evidence state:** reproduced. **Review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P. **Finding IDs:** F-NUM-1001, F-ST1-1001.

**Every affected location found; source and comparator matched:** [Protocol PDF p12, Table 2](../../../joi250072supp1_prod_1761000786.68881.pdf#page=12), PLAN. In the NICHD BPD Workshop Grading 2018 block, Grade 3 surfactant is visually 20% (31/294), combination is 12% (21/173), and P=.02 with the chi-square marker. Adjacent surfactant cells are Grade 3 or Death 31% (91/294), Death 11% (31/294), No BPD 29% (85/294), Grade 1 14% (41/294), and Grade 2 26% (77/294). Every affected and corroborating cell was matched to the direct source render; none is an OCR-only reading.

**Applicable rule and reproduced calculation:** Route A, category 3, focus A. Nominal 100×31/294=10.5442176871%. Allowing the numerator [30.5,31.5] and denominator [293.5,294.5] gives [10.3565365025,10.7325383305]%. Printed 20% permits [19.5,20.5]%; nonoverlap gap=8.7674616695 percentage points; relative gap/20=0.4383730835 > .05. This independent arithmetic reproduces the registered within-cell discrepancy. Restricting participant counts to integers would strengthen, not remove, it. The displayed grade counts plus death sum 265 rather than 294, and composite 91 minus death31 suggests60 as an alternative count. Those are supporting diagnostics rather than required assumptions about exhaustive historical categories. The chi-square diagnostic is not necessary for the evidence state or asserted as the uniquely implemented test.

**Necessary inputs and exact missing inputs:** The count, denominator and printed percentage are fully available. Missing are the historical underlying cohort tabulation, the intended numerator/percentage pairing, and exact test implementation. No BiB participant-level input is needed to reproduce this printed-cell arithmetic.

**Alternative interpretation:** Percentage20 and composite-minus-death60 are compatible with a different historical numerator; alternatively, the displayed count31 could be retained with a different percentage. The table does not establish which pairing is intended. Neither alternative is assigned as a correction.

**Direct observation versus inferred explanation:** 20% (31/294) and adjacent cells are direct source observations; a possible repeated death numerator or substituted count is an inference only.

**Classification confirmation and ambiguity:** This is PLAN protocol background, not an observed BiB result. The conflict is solely within PLAN, hence P_P and plan_material. Historical/peripheral background is explicitly retained as scope ambiguity, but reproduced always-register count–denominator–percentage comparisons cannot be removed solely on that basis. No effect on the current trial's design or conclusions is inferred.

**Determining recheck fact:** The exact printed cell was found and its half-unit relative gap is 0.4383730835; therefore reproduced.

**Exact remaining human question:** Which historical numerator, percentage and associated test correspond to the Grade 3 surfactant row?

## C005 — One nasal-cannula lookup factor

**Status:** Pending Human Adjudication. **Evidence state:** reproduced. **Review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P. **Finding IDs:** F-NUM-2001.

**Every affected location found; source and comparator matched:** [Manual PDF p152, Appendix J Table 1 and instructions](../../../joi250072supp2_prod_1761000786.6938.pdf#page=152), PLAN, visually prints factor4 for flow0.125 LPM (also labeled 1/8 LPM) and weight2.5 kg. All 16 flow rows ×9 weight columns were independently reread, including every one of the other143 comparator cells. The 2.5-kg column at flows .15,.25,.5,.75,1.0,1.25,1.5,2.0 prints6,10,20,30,40,50,60,80. Instructions select the nearest tabulated input when an exact value is absent, with half-way ties rounded up. [Manual PDF p154, Table 2](../../../joi250072supp2_prod_1761000786.6938.pdf#page=154), PLAN, prints effective oxygen24% at factor4/100% concentration and25% at factor5/100%; these are consequence-locator cells, not a second independent discrepancy.

**Applicable rule and reproduced calculation:** Route A, category 4, focus C/D. The relationship min(100,100×flow/weight), with each decimal input's printed half-unit interval and each factor's ±.5 interval, satisfies the workflow precision rule in143 of144 cells. Independent arithmetic on the visually reread matrix reproduces that comparator count. For the affected cell, [.1245,.1255] LPM and [2.45,2.55] kg give [4.8823529412,5.1224489796]; factor4 permits [3.5,4.5]. Gap=.3823529412; relative gap/4=.0955882353 > .05. Using exact1/8 LPM gives [4.9019607843,5.1020408163], so its alternate fractional label also does not reconcile the factor. Input-nearest instructions address values absent from the grid and do not explain a different method for an exact grid cell. Table 2's24/25 distinction is an operational lookup consequence, not an asserted observed endpoint change.

**Necessary inputs and exact missing inputs:** Every tabulated flow, weight and factor is available; no source-reading gap remains. The underlying factor-generating algorithm, its derivation and any exception for this particular cell are not supplied. Participant-level use of the cell and outcome data are unavailable and not needed for the display-method comparison.

**Alternative interpretation:** An unstated flow/weight convention or deliberate exception may govern this cell. The accompanying prose gives no exception, and the same reproducible relationship supports all143 other cells within permitted precision. No physiological method is imported and no replacement factor is assigned.

**Direct observation versus inferred explanation:** The tabulated4 and associated inputs/comparator cells are direct observations. The formula is an empirically reproduced display relationship, not an explicitly printed generating equation. A production mechanism or actual participant impact is not observed.

**Classification confirmation and ambiguity:** Both conflicting quantities are within a prospective operational PLAN; P_P and plan_material are confirmed. The main article's mention of conversion tables only corroborates relevance and does not make a P_R relationship. The unstated generating method is the bounded ambiguity.

**Determining recheck fact:** Exact-source factor4 remains separated from the reproduced interval by relative gap .0955882353 while the other143 cells reconcile; therefore reproduced.

**Exact remaining human question:** What factor-generating method or documented exception explains the0.125 LPM/2.5 kg cell in Table 1?

## C006 — Exact-CI statement and sparse log-Wald interval pattern

**Status:** Pending Human Adjudication. **Evidence state:** reproduced. **Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Finding IDs:** F-ST1-003.

### Every affected source location and repeated row

All eight non-NA affected rows and both method statements were found and visually reread. The eTable 3 denominator header is322/313; individual nonmissing denominators for its sparse rows are not printed.

| Exact source location | Content role | Matched source event counts and displayed estimate/CI |
|---|---|---|
| [Results PDF p5, eTable 3 AE endotracheal blockage, superscript b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5) | REPORT | 3 versus4;0.73 (0.16,3.28). |
| [Results PDF p5, AE hypoxemia/bradycardia, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5) | REPORT | 2 versus3;0.65 (0.11,3.90). |
| [Results PDF p5, SAE endotracheal blockage, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5) | REPORT | 1 versus1;0.98 (0.06,15.66). |
| [Results PDF p5, SAE hypoxemia/bradycardia, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=5) | REPORT | 1 versus2;0.49 (0.04,5.39). |
| [Results PDF p6, SAE hyperglycemia, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=6) | REPORT | 8 versus3;2.64 (0.69,10.05). |
| [Results PDF p6, SAE early sepsis, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=6) | REPORT | 4 versus2;1.96 (0.36,10.79). |
| [Results PDF p6, SAE late sepsis, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=6) | REPORT | 5 versus2;2.46 (0.47,12.78). |
| [Results PDF p6, eTable 3 footnote b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=6) | REPORT | Crude unadjusted OR with exact95% confidence intervals due to low event prevalence, expressly contrasting the ordinary robust-Poisson method. |
| [Results PDF p7, eTable 4 PDA surgery/catheterization, b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=7) | REPORT | 5/319 versus3/308;1.62 (0.38,6.83). |
| [Results PDF p8, eTable 4 denominator text and b](../../../joi250072supp4_prod_1761000786.6988.pdf#page=8) | REPORT | n/N uses participants with a nonmissing outcome; b expressly states crude unadjusted OR with exact95% confidence intervals. |

**Applicable rule and reproduced calculation:** Route B, focus C/B. The fully specified PDA row supplies independent inputs; no assumed eTable 3 denominator is needed for the inclusion anchor. Its four integer cell counts are5,314,3,305; restricting half-unit count intervals to counts leaves those inputs unique. Independently reproduced OR=5×305/(314×3)=1.6188959660; SE=sqrt(1/5+1/314+1/3+1/305)=0.7347086057. With z=.975 standard-normal quantile1.95996398454, the log-Wald interval is [0.3835604698,6.8328838734]. The point estimate lies in printed1.62's [1.615,1.625] interval, and both endpoints lie in printed [.375,.385] and[6.825,6.835], so Wald-versus-print gaps are zero. This confirms the registered derived SE; the checker SE clarification had already occurred before registration and does not require an evidence-state transcription correction.

For a separately labeled **diagnostic** conditional equal-tail exact inversion, weights choose(319,x)choose(308,8−x)theta^x and equations Pr(X≥5)=.025, Pr(X≤5)=.025 give [0.3116657003,10.5065044240]. Compared with the printed endpoints' half-unit intervals, relative gaps are (.375−.3116657003)/.38=.1666692098 and(10.5065044240−6.835)/6.83=.5375555526. These exceed .05. This calculation shows why the mapping between the explicit exact-CI statement and the reproducible asymptotic pattern needs clarification; the source does not name this equal-tail convention, so these endpoints are not asserted to be the uniquely required source method.

The seven eTable 3 rows reproduce the same log-Wald pattern using diagnostic nonmissing denominators321/313. Their independently recalculated intervals, in source order, are [.1617821749,3.2828767340], [.1075183994,3.9037025017], [.0607184019,15.6562915124], [.0438404197,5.3862452863], [.6942207051,10.0478840500], [.3568166367,10.7898932910], [.4738151378,12.7766706051]. Every endpoint overlaps its displayed ±.005 interval; each corresponding point estimate also rounds to the source value. These are supporting diagnostics because321 is reconstructed, whereas the header322 alone does not establish each nonmissing denominator. The NA hypertension row is not an interval occurrence and is not included in the eight-row pattern.

**Necessary inputs and exact missing inputs:** All decisive PDA counts and both method footnotes are available. Missing are the actual interval-producing procedure/options, exact-interval tail/order convention, code or output establishing the implemented algorithm, and individual nonmissing denominators for the seven eTable 3 rows. Participant-level data are unnecessary for the fully specified PDA diagnostic, but no algorithm identity is claimed to be uniquely proven merely from endpoint coincidence.

**Alternative interpretation:** The exact statement may refer to a different exact confidence procedure or unreported software option; alternatively, it may have been applied broadly while some rows used asymptotic intervals. The source expressly attaches exact to the CI, not only to an exact test. Neither an unreported convention nor a production mechanism is established. The available evidence supports an unresolved method-mapping question rather than replacement endpoints or a preferred analysis.

**Direct observation versus inferred explanation:** Exact-CI wording, cell counts and endpoints are direct observations. The all-row log-Wald reproduction is a calculation; attributing the implemented procedure to Wald is an inference supported by that pattern, not observed source code. No interval/P-value significance conflict is asserted.

**Classification confirmation and ambiguity:** Counts, intervals and method statements are inside one observed-results REPORT, so S_W and statistical_results are confirmed. Other report/plan descriptions are unnecessary to this conflict and add no relationship. Exact-algorithm identity and eTable 3 denominator ascertainment are the bounded ambiguities.

**Determining recheck fact:** Exact source counts/CI/method wording match, and independent arithmetic confirms the printed asymptotic interval pattern and substantial exact-tail diagnostic separation; the registered unresolved method mapping remains, therefore reproduced.

**Exact remaining human question:** Which confidence-interval algorithm/options produced these superscript-b intervals, how does it implement the stated exact95% CI method, and what were the nonmissing eTable 3 denominators?

## Recheck coverage and limitations

Coverage is six of six stable IDs, with no deletion or classification change. Each registered affected location was found; source values and comparators matched. Evidence states: six reproduced, zero reproduced_after_transcription_correction, zero not_reproduced. The C006 derived-SE clarification was already incorporated into registration and is independently confirmed here.

Current exact-source render inspection used screening/parts/inclusion_source_*.png for main pages1,3,4,6,7,8,9; protocol12,21,25; manual39,59,152,154; SAP11,22,29,32,33,34,35,36,37,38,39; and results2,5,6,7,8. Fresh source-native text screening/parts/inclusion_source_main.txt and inclusion_source_results.txt was used to bound the full supplied reporting scope. No OCR-only source reading determines an evidence state. No unreadable cited page or unresolved page-location gap remains.

Remaining questions concern operational criterion priority, undisclosed model/output mappings, historical intended cell pairing, factor-generating conventions, interval algorithm/options and participant-level data not supplied. These limitations are recorded separately per ID above. They do not establish nonexecution, observed patient reclassification, paper-level conclusion changes, or a disposition.
