# Statistical Consistency Pass 2

## Scope, independence, and method

**Reviewer execution:** a distinct fresh `gpt-5.6-terra` / high-effort statistical-pass-2 specialist. The coordinator records this runtime agent ID and the distinct pass-1/pass-2 execution identity in `agent_execution_manifest.md`.

**Assigned scope:** all 38 canonical inferential relationships (`S001`--`S038`), the complete stable ledger (`C001`--`C023`), the fresh main/support statistical mappings, the numeric and cross-source check artifacts, and the mechanical recheck record. Only supplied direct PDFs and the fresh assets derived for this run were used. No web source or legacy audit derivative was used.

For each relationship, this independent pass revisited printed estimate/interval containment and order, contrast direction, measure and scale labels, direct denominator/arithmetic implications, matched repetitions, and the recheck facts. Interval--P/test/SE compatibility was assessed only where the supplied source gave a compatible enough rule; calculations based on rounded interval endpoints are explicitly diagnostic and do not replace the reported analysis. No severity, validity disposition, correction, or adjudication was assigned.

## Relationship-by-relationship PASS_2_COMPLETE record

| S ID | PASS_2_COMPLETE record | Current-ledger implication |
|---|---|---|
| S001 | VFD MD -0.27 is contained in the ordered 95% CI -1.74 to 1.19; low-minus-intermediate direction agrees with 15.2 versus 15.5 to displayed precision, and abstract/table/narrative agree. The supplied two-sided t-test rule makes P=.71 directionally compatible. | None. |
| S002 | Sensitivity P=.72 is a separately labelled GLMM result. The random effects are named, but the estimate, variance, test statistic, and model output required for a numerical reconstruction are absent; no cross-location contradiction was found. | None; missing model output recorded. |
| S003 | Survivor ventilation-days MD -0.56 is contained in -1.61 to 0.49, and its sign agrees with 5.4 minus 6.0 to displayed precision. No P value or further compatible inferential definition is printed. | None. |
| S004 | ICU-stay MD 0.39 is contained in -1.09 to 1.89 and agrees with 9.6 minus 9.2 to displayed precision. The inverse-Gaussian GLM is named, but no coefficient SE/dispersion/model output is supplied to reconstruct P=.58. | None; missing GLM inputs recorded. |
| S005 | ICU-stay curve HR 0.94 is inside ordered 0.80-1.09 limits and P=.41 is compatible with a null-crossing interval. The Schoenfeld P=.21 is a proportional-hazards diagnostic, not the treatment-effect P; HR and Table 2 MD remain separately labelled estimands. | None. |
| S006 | Hospital-stay MD -0.60 is contained in -3.52 to 2.31 and agrees with 20.4 minus 21.0 to displayed precision. The inverse-Gaussian GLM inputs needed to reconstruct P=.68 are absent. | None; missing GLM inputs recorded. |
| S007 | Hospital-stay curve HR 1.02 is inside ordered 0.87-1.19 limits; P=.83 is compatible with the null-crossing interval. Schoenfeld P=.82 is a diagnostic only, and the curve HR is not interchanged with the Table 2 MD. | None. |
| S008 | ICU-mortality RR 1.11 is inside ordered 0.96-1.27 limits. The displayed risks yield crude low/intermediate RR 1.168, not 1.11; the source labels the estimate RR but does not give the estimator/population needed to reconcile it. The main Methods HR/Cox wording conflicts with the table/SAP RR description. Rounded-limit diagnostic P compatibility does not resolve either issue. | C011 and C012 are represented. |
| S009 | Hospital-mortality RR 1.06 is inside ordered 0.93-1.22 limits. Printed risks yield crude RR 1.094, not 1.06; the estimator/population is not supplied. The same main-Methods versus table/SAP measure-label issue applies. | C011 and C013 are represented. |
| S010 | 28-day mortality HR 1.12 is inside 0.90-1.40; P=.30 is compatible with the null-crossing CI and abstract/table repetition. The Cox/time-to-event inputs and SE are not supplied for an exact reconstruction. | None. |
| S011 | 90-day mortality HR 1.07 is inside 0.87-1.31; P=.54 is compatible with the null-crossing CI and abstract/table/Figure 2B repetitions. Schoenfeld P=.13 is diagnostic only. | None. |
| S012 | ARDS RR 0.86 is inside 0.59-1.24. The printed risks give crude RR 0.762, not 0.86. Rounded log-interval/P diagnostics are broadly compatible with P=.38 but cannot identify the missing estimator or population. | C014 is represented. |
| S013 | Pneumonia RR 1.07 is inside 0.78-1.47. Printed risks give crude RR 1.147, not 1.07; a rounded log-interval diagnostic is compatible with P=.67, without defining the reported RR computation. | C015 is represented. |
| S014 | Pneumothorax RR 1.16 is inside 0.73-1.84. Printed risks give crude RR 1.375, not 1.16; rounded interval/P comparison does not establish the unreported estimator. | C016 is represented. |
| S015 | Atelectasis RR 1.00 is inside 0.81-1.23. Printed risks give crude RR 1.014; its small difference from 1.00 may reflect rounding or a different estimation procedure, neither of which is supplied. P=.94 is not a display-zero issue. | C017 is represented. |
| S016 | Extrapulmonary-infection RR 0.84 is inside 0.60-1.18. Printed risks give crude RR 0.738, not 0.84; no estimator/population definition reconciles them. | C018 is represented. |
| S017 | Extrapulmonary-sepsis RR 0.87 is inside 0.56-1.33. Printed risks give crude RR 0.775, not 0.87; no estimator/population definition reconciles them. | C019 is represented. |
| S018 | Delirium RR 1.15 is inside 0.99-1.34. Printed risks give crude RR 1.188, not 1.15. A rounded log-interval diagnostic is compatible with P=.06, but model/analysis-set inputs remain unavailable. | C020 is represented. |
| S019 | Tracheostomy RR 1.03 is inside 0.84-1.26. Printed risks give crude RR 1.054, not 1.03; rounded interval/P diagnostic compatibility does not supply the estimator. | C021 is represented. |
| S020 | Free-from-invasive-ventilation HR 0.99 is inside 0.86-1.14 with ordered limits; P=.92 is compatible with a null-crossing interval. Cox/Kaplan-Meier endpoint remains distinct from the VFD t-test and Schoenfeld P=.68 is diagnostic only. | None. |
| S021 | The two subgroup MDs are inside their printed ordered bounds and their signs agree with displayed means to rounding. Exact repeated values are labelled IQR in the main narrative but 95% CI in eTable 5; the interval-type conflict is direct and the interaction P=.01 is not a within-subgroup P. | C022 is represented. |
| S022 | The mixed longitudinal model, random intercepts, and continuous time are specified, but DOC-001 contains no numerical coefficient/interval/test output for an exact inferential reconciliation. | None; no numerical output in this record. |
| S023 | Two-sided alpha=.05 and no multiplicity adjustment are stated as a global rule. It neither changes a displayed point estimate nor creates a separate result-level contradiction. | None. |
| S024 | Protocol/SAP sample-size assumptions agree: 397 per arm, 1-day difference, common SD 5, 80% power, two-sided alpha=.05, and 20% inflation to 476 per arm after whole-person rounding. Later actual enrollment is not the same planned quantity. | None. |
| S025 | This is a protocol planned-analysis statement (Cox, 95% confidence, ITT/per-protocol), with no matched reported estimate in the record; no inferential calculation applies. | None. |
| S026 | The protocol test/model catalogue is prospective only. No result is paired to an exact planned procedure here, so it does not establish a result inconsistency. | None. |
| S027 | The SAP identifies VFD t test/mean difference and liberation Kaplan-Meier/log-rank. The matched main-paper VFD analysis uses a mean difference/t test; no discrepant matched result was found. | None. |
| S028 | The SAP explicitly distinguishes 28/90-day Cox HR from ICU/hospital RR and agrees with the table's specific mortality labels. It leaves unresolved the generic main-Methods wording that describes mortality as Cox HR. | C011 is represented. |
| S029 | Per-protocol, subgroup-interaction, and exploratory-model definitions are planned analysis descriptions. eTable 5 P values are interaction P values as labelled; no matching result/model contradiction is printed. | None. |
| S030 | Amendment material explicitly records planned-to-final analysis changes, including t test/mean difference and Gaussian subgroup GLM. A documented final-plan change is not itself a result inconsistency. | None. |
| S031 | eTable 1 count/percentage arithmetic and IQR ordering remain coherent. Its `<.001` entries are finite-precision inequality displays, not literal-zero P values and not candidates; no exact per-cell test is named. | DISPLAY_ZERO_NOT_CANDIDATE convention applied where relevant; no ledger candidate. |
| S032 | eTable 2 mode/time denominators partition eTable 1 totals at each matched timepoint. The Other-mode intermediate post-titration PEEP `8 (5-1)` has reversed, non-containing IQR bounds; its unnamed P=.50 test cannot resolve the display. | C001 is represented. |
| S033 | eTable 3 mode-stratum totals match eTables 1--2. `7/20 (35.)` is numerically consistent with 35.0%, and `---` P cells accompany double-zero comparisons rather than a P=0 printout. | No ledger candidate; no display-zero candidate. |
| S034 | eTable 4 explicit fractions reproduce their printed percentages. The four count-plus-percent rows lack row totals and do not reproduce from arm headers; P values, including P=1.00, do not independently resolve the denominators. | C007, C008, C009, and C010 are represented. |
| S035 | All 18 subgroup MDs are contained in ordered 95% CIs and agree in sign with low-minus-intermediate group means to displayed precision. The duplicate ICU-location interval-label conflict is the same matched-result issue recorded for S021. | C022 is represented. |
| S036 | eFigure 1 gives labelled cumulative VFD curves but no printed effect estimate, CI, test, or P. No numerical inferential reconciliation is available. | None. |
| S037 | eFigures 2--4 provide distributions and labels but no printed effect estimate, CI, test, or P for a numerical inferential check. | None. |
| S038 | DOC-005 has no applicable statistical result. | None. |

**Pass-2 relationship completion:** `S001`--`S038`, 38/38, are `PASS_2_COMPLETE` in this checker. The coordinator must update the `Pass 2` column for all 38 canonical rows in `statistics/relationship_inventory.md` to `PASS_2_COMPLETE` during canonical-stage merge.

## Current stable-ledger implication coverage

| Stable candidate | Pass-2 statistical implication review |
|---|---|
| C001 | Represented by S032; the median/IQR definition makes the endpoint-order contradiction directly checkable, while the unnamed P=.50 test adds no reconciliation. |
| C002 | This Table 1 denominator/percentage candidate has no separately mapped inferential S relationship; pass 2 found no additional statistical consequence. |
| C003 | This Table 1 denominator/percentage candidate has no separately mapped inferential S relationship; pass 2 found no additional statistical consequence. |
| C004 | This Table 1 category-denominator candidate has no separately mapped inferential S relationship; pass 2 found no additional statistical consequence. |
| C005 | This Table 1 category-denominator candidate has no separately mapped inferential S relationship; pass 2 found no additional statistical consequence. |
| C006 | This Table 1 category-denominator candidate has no separately mapped inferential S relationship; pass 2 found no additional statistical consequence. |
| C007 | Represented by S034; the printed P=.63 does not identify or replace the undisclosed denominator. |
| C008 | Represented by S034; the printed P=.53 does not identify or replace the undisclosed denominator. |
| C009 | Represented by S034; the printed P=.55 does not identify or replace the undisclosed denominator. |
| C010 | Represented by S034; the printed P=.19 does not identify or replace the undisclosed denominator. |
| C011 | Represented by S008, S009, and S028. Table/SAP specific RR labels agree with one another; the unresolved conflict is the main Methods sentence's generic HR/Cox description of mortality rates. |
| C012 | Represented by S008; the source prints a RR but does not provide the estimator/population needed to reconcile it with displayed ICU-mortality risks. |
| C013 | Represented by S009; the source prints a RR but does not provide the estimator/population needed to reconcile it with displayed hospital-mortality risks. |
| C014 | Represented by S012; the ARDS printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C015 | Represented by S013; the pneumonia printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C016 | Represented by S014; the pneumothorax printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C017 | Represented by S015; the small crude-versus-printed difference is retained as the registered observation, with rounding/estimation details unresolved. |
| C018 | Represented by S016; the printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C019 | Represented by S017; the printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C020 | Represented by S018; the printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C021 | Represented by S019; the printed-risk ratio differs from the printed RR and the source lacks the estimator/population definition. |
| C022 | Represented by S021 and S035; identical matched subgroup bounds are labelled IQR in the main narrative and 95% CI in eTable 5. |
| C023 | This is an enrollment-date cross-document candidate, not a separately mapped inferential-statistical relationship. Pass 2 found no additional statistical implication. |

**Ledger coverage:** C001-C023, 23/23, reviewed for statistical implications. Existing IDs were neither deleted, renumbered, merged, ranked, nor adjudicated. Every remains **Pending Human Adjudication**.

## New-candidate register

No genuinely new, nonduplicate pass-2 candidate was identified (`P2F001...`: none). The direct contradictions found in this pass are already represented by C001, C007-C022, and their cited S records; the remaining current candidates were reviewed for possible additional statistical implications.

## Display-zero and calculation boundaries

- No candidate was registered from a coherent finite-precision P-value display. In particular, eTable 1 `<.001` values are inequality displays; eTable 3 `---` cells are not P=0; and eTable 4 P=1.00 is an ordinary rounded value. These are `DISPLAY_ZERO_NOT_CANDIDATE` where that coverage label is relevant.
- The binary-outcome table supplies labels and broad Wald/chi-square wording, but not the RR estimator direction, weighting/stratification, exact analysis population, or model outputs required to reproduce the published RRs from displayed 2-by-2 margins. Crude-risk-ratio calculations are therefore direct diagnostics from printed values, not a substitute analysis.
- Rounded CI endpoint checks can support containment/order and broad P-direction compatibility. They cannot resolve a likelihood-ratio-versus-Wald implementation, variance estimator, sidedness beyond the explicitly stated two-sided global rule, covariance, multiplicity implementation, or unreported model outputs.
- The supplied PDFs contain no patient-level data, code, randomization-time log, detailed missingness denominator documentation, or analytic output. These absences define the remaining human questions; they are not adverse dispositions.

## Completion status

- Canonical statistical relationships reviewed: 38/38 (`S001`--`S038`).
- Current stable candidates reviewed for statistical implications: 23/23 (`C001`--`C023`).
- New nonduplicate pass-2 candidates: 0.
- Status of all existing and newly considered observations: **Pending Human Adjudication**.
