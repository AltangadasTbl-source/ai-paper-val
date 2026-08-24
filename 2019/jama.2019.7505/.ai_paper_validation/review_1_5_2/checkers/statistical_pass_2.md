# Statistical consistency review — pass 2

## Independent pass-2 scope and evidence basis

This is an independent second statistical pass by a fresh specialist runtime, `/root/statistics_pass_2`, distinct from statistical pass 1. It revisits all 31 canonical inferential-statistical relationships, `S001` through `S031`, after stable registration of `C001` through `C008` and after the mechanical recheck. The evidence basis is limited to the current 1.5.2 source-first inventories, fresh native/layout source assets and source-matched quantitative mappings for DOC-001 through DOC-005, the canonical candidate ledger, and `verification/evidence_recheck.md`. No previous audit derivative, web material, sibling package, GPU process, or external convention was used.

For every relationship, this pass revisited available denominator and arithmetic identities; point-estimate containment and endpoint ordering; sign/direction; effect-measure, population, reference, label, and scale; duplicated or repeated values; figure/cross-source matches; and implications of the complete candidate ledger and mechanical recheck. Interval/P-value/test/statistic/SE compatibility was considered only where the supplied sources name a compatible model or inferential rule. Where a numerical comparison is described as a **diagnostic approximation**, it is only a rounded display check and is not substituted for the reported analysis. Sidedness, degrees of freedom, covariance, variance estimator, multiplicity, denominator, model, or estimand mapping was never filled in from convention.

The fresh source text remains partly column-serialized on DOC-001 Table 2 (PDF p. 7) and Table 3 (PDF p. 9). Accordingly, no row-to-statistic association was inferred where the fresh assets do not preserve one. DOC-005 eFigures 1-7 have no recoverable plotted values or P values in current fresh text. These are definition/evidence limitations, not reasons to omit their relationships.

## Ledger and mechanical-recheck reconciliation

All eight existing stable candidates were revisited. This pass does not delete, renumber, adjudicate, rank, or assign a correction to any ID.

| Stable ID | Pass-2 relationship to the statistical scope | Recheck implication retained |
|---|---|---|
| C001 | The operational criteria discrepancy for intraoperative hypoxemia/hypotension affects interpretation of Table 3 fields within S011, but it is an outcome-definition comparison rather than a supplied compatible CI/P/test calculation. | Both distinct printed criteria and the missing rule identifying the count-generating definition remain recorded. No separate statistical duplicate was created. |
| C002 | The white-blood-cell unit/scale issue is a baseline laboratory-display relationship, not an `S` inferential relationship. | The factor-of-1000 scale question remains confined to its existing numeric/label record; it supplies no new inference contradiction. |
| C003 | The generic eTable 8 `Effect Estimate` header is directly relevant to S025. | Exact counts, denominators, estimates, and intervals were re-read. The generic label and absent measure/reference/model definitions remain the supplied-source issue; crude ratios remain diagnostic only. |
| C004 | The eFigure 11 mortality-versus-PEPC label mismatch is directly relevant to S031. | The title, rates, mortality HR/CI/P, eFigure 10 PEPC comparator, and main Table 3 mortality comparator remain distinct printed fields. This is the same label-identity observation, not a new candidate. |
| C005 | The abstract/Table 3 hypoxemia CI sign mismatch is directly relevant to S011. | The matched counts, contrast, point estimate, and opposite printed upper-endpoint signs remain source-grounded. This is the same cross-location observation, not a new candidate. |
| C006 | The matched synthetic-colloid P-value discrepancy is directly relevant to S020. | The `P=.09` and `P=.10` cells remain distinct direct displays for the same reported counts/population. The unstated row-specific test and rounding pipeline remain precisely missing. |
| C007 | The monitoring fraction/percentage mismatch is directly relevant to S006. | The fractions, parenthetical percentages, and displayed difference remain direct values. Ordinary one-decimal fraction rounding remains the applicable arithmetic check. |
| C008 | The reversal fraction/percentage mismatch is directly relevant to S006. | The fractions, parenthetical percentages, and displayed difference remain direct values. The calculation rule for the printed `0.2` difference remains unreported. |

No `P = 0`, `p = 0.000`, or equivalent finite-precision display-zero result was encountered in the assigned relationships. Printed `<.001`, `>.99`, and `1.00` displays were not treated as display-zero candidates, and no tail probability was derived to criticize a display format.

## Relationship-level pass-2 records

| ID | `PASS_2_COMPLETE` record | Existing candidate relationship / new provisional append key | Missing definition or evidence limitation retained |
|---|---|---|---|
| S001 | Sample-size stages were re-matched across main article, protocol, change history, and SAP: original `748`, revised `1912` plus 5% dropout `=2013`, target RR `.75`, power 80%, and final primary alpha `.044` identify planned chronology rather than competing observed estimates. No new candidate observation. | None / None | Full power inputs, actual spending-function implementation, and interim test outputs are not supplied; no power calculation was reconstructed. |
| S002 | Primary PPC counts, difference `-2.3% (-5.9 to 1.4)`, RR `.93 (.83-1.04)`, and `P=.23` have ordered intervals, appropriate null containment, coherent high-versus-low direction, and repeated-location agreement. A log-CI/P comparison is only a diagnostic approximation and gives no distinct observation. | None / None | The supplied Wald likelihood-ratio/chi-square wording does not provide a full RR estimand, variance, or count-to-estimate mapping. |
| S003 | Secondary RR, t-test/mean-difference, HR, and exploratory-alpha statements were re-compared with the SAP definitions. No matched supplied result contradicts a named rule. | None / None | Individual continuous-outcome row-to-test and variance details are not fully supplied. |
| S004 | Tidal-volume and PEEP estimates on DOC-001 p. 7 have ordered CIs containing their shown estimates; signs agree with group means and intervention direction. No new candidate observation. | None / None | Table-column serialization and absent continuous-outcome CI/test linkage preclude row-level P/CI reconstruction. |
| S005 | Recoverable peak/driving pressure, respiratory rate, FiO2, SpO2, CO2, heart-rate, and MAP differences retain ordered endpoints, estimate containment, and signs consistent with displayed arm values. No new candidate observation. | None / None | Same DOC-001 p. 7 serialized-column and unspecified test/variance limitations. |
| S006 | Procedure comparisons were rechecked for count/denominator arithmetic, direction, and available P/CI displays. Monitoring and reversal reproduce the already registered fraction/percentage observations C007 and C008; no other distinct mismatch was found. | C007; C008 / None | No compatible model for Table 2 interval/P reconciliation is supplied; the reversal-difference calculation rule is unreported. |
| S007 | Primary PPC repeats across abstract, Key Points, narrative, Table 3, and Figure 2 remain `211/989` versus `233/987`, difference `-2.3%`, RR `.93 (.83-1.04)`, `P=.23`. Interval/null and direction checks remain coherent. | None / None | Crude count ratio is not assumed to be the reported RR estimand. |
| S008 | Mild respiratory failure repeats as difference `-1.9% (-5.1 to 1.2)`, RR `.92 (.80-1.05)`, `P=.22`; endpoints, null containment, and direction remain coherent. | None / None | Complete row-level Table 3 model/variance mapping is unavailable. |
| S009 | Pleural-effusion difference `2.2% (.7 to 3.8)`, RR `1.35 (1.14-1.62)`, and `P=.005` remain directionally and cross-location coherent; both intervals exclude their applicable null values. | None / None | The precise RR estimator and test/CI linkage is not provided beyond the general primary-analysis description. |
| S010 | Remaining primary-component fields were reconsidered only where fresh extraction preserves a defensible row association. Recoverable displays retain endpoint order and estimate containment; no new candidate observation. | None / None | DOC-001 p. 9 column serialization prevents assigning every RR/CI/P sequence to a component row. |
| S011 | Secondary/postoperative/adverse-event fields were rechecked against ledger and source matches. C005 is the same abstract/Table 3 hypoxemia CI-sign mismatch, and C001 is the same criteria-definition mismatch affecting interpretation of intraoperative outcomes; no separate candidate was created. Other recoverable fields provide no new independent contradiction. | C001; C005 / None | Table 3 serialization prevents complete row-level inferential matching; exact operational rule that generated event counts is not specified where C001 applies. |
| S012 | Desaturation rescue, vasoactive drug use, and 5-day mortality retain ordered intervals containing their estimates and directionally compatible contrasts. The named Cox mortality result is diagnostically compatible with its CI/P at display precision; no new candidate observation. | None / None | The diagnostic approximation does not establish the exact test, sidedness, covariance, or binary-RR estimator. |
| S013 | Figure 2 subgroup RRs/CIs retain ordered endpoints, estimate containment, and directions matching displayed subgroup risks. Interaction P values are retained as displayed. | None / None | Interaction coefficients, covariance, model parameterization, and sidedness are absent; no interaction-P reconstruction was attempted. |
| S014 | Narrative ITT/per-protocol and sensitivity wording remains directionally compatible with separately labelled eTable 8/eTable 9 analyses. It does not create an identical-result comparison. | None / None | Some narrative claims lack numerical estimates; `similar` is not a mechanically defined effect. |
| S015 | Planned sample-size, alpha, power, RR, and re-estimation fields in the protocol/change history remain coherent versions of the trial plan and final enrollment. | None / None | No interim implementation outputs or complete power-calculation inputs are supplied. |
| S016 | Gamma-spending schedule, look sizes, efficacy/futility bounds, and planned model descriptions remain protocol definitions; final `.044` primary alpha matches main/SAP material. | None / None | No observed interim test statistics or final analysis-to-boundary mapping is supplied. |
| S017 | SAP primary RR/CI/chi-square and two-sided alpha `.044` retain agreement with the main article primary-analysis description. | None / None | General method wording does not define all estimator/variance details required for count-to-RR reproduction. |
| S018 | SAP secondary, subgroup, and sensitivity model labels were re-read. The stated Bonferroni confidence level is arithmetically compatible with `1-.05/12=.99583`, displayed as 99.58%; no new candidate observation. | None / None | No component-specific adjusted-CI result set permits a full planned-method-to-observed-result recheck. |
| S019 | ARISCAT ORs have ordered CIs containing their estimates; printed coefficients exponentiate to printed ORs within display precision as a diagnostic approximation. | None / None | Coefficient rounding, original covariance, and exact model fit are absent; diagnostic exponentiation is not a model audit. |
| S020 | eTable 3 was revisited for repeated values and P labels. The matched synthetic-colloid count row remains the existing C006 `.09` versus `.10` display discrepancy; all other matched summary-statistic comparisons remain nonidentical measures or concordant displays. | C006 / None | Row-specific test, sidedness, continuity rule, variance, unrounded P values, and rounding pipeline are not supplied. |
| S021 | eTable 4 vasoactive-use P `.02` remains matched to the main-table `.02`; other use/dose rows have no internally matched incompatible repetition. | None / None | Table-specific test type, distributional rule, and dose-model definition are not supplied. |
| S022 | eTable 5 medication P values retain their population, count/percentage, label, and scale checks; no matched same-result contradiction was found. | None / None | Test types and multiplicity treatment are unstated. |
| S023 | eTable 6 category and intra-abdominal-pressure P values retain label/scale/population checks; no duplicate-value or rate/count contradiction was found. | None / None | Multilevel-category test definitions and continuous-pressure inference rules are unstated. |
| S024 | Daily VAS means, observed denominators, and P displays remain compatible with the main qualitative `comparable` wording without representing an identical repeated result. | None / None | Repeated-measures method, missing-data handling, covariance, and row-specific test definition are not supplied. |
| S025 | Per-protocol eTable 8 endpoints contain their generic effect estimates and the PPC result is directionally compatible with its separately labelled analysis set. C003 remains the same generic-effect-label and crude-nonidentity observation; it is not an additional crude-ratio contradiction because the supplied measure/model/reference definitions are missing. | C003 / None | Effect measure, reference direction, estimand, adjustment set, model, variance, CI method, and test for eTable 8 remain unnamed. |
| S026 | Random-site, proportional-odds, common-GEE, interaction, and average-relative-effect outputs retain correct displayed endpoint order and labels. CI/P comparisons, including the average-relative-effect display, remain diagnostic only and yield no new candidate without a supplied common test/CI/variance/estimand rule. | None / None | Required linkage among transformation, CI, test statistic, covariance, GEE variance estimator, and average-relative-effect estimand is not provided. |
| S027 | eFigures 1-7 were rechecked for available mean/95% CI, scale, and mixed-model interaction labels. No exact plotted values or P values are recoverable to compare. | None / None | Fresh text has no usable plotted coordinates or figure-specific P values for DOC-005 pp. 31-37. |
| S028 | Time-to-PPC HR `.88 (.73-1.06)`, `P=.190`, and Schoenfeld P `.05` retain distinct stated roles; the HR CI contains 1 and its diagnostic log-scale P is broadly compatible with `.190`. | None / None | Schoenfeld P tests proportional-hazards assumptions, not the HR effect; exact Cox test/CI linkage and variance details are not supplied. |
| S029 | Time-to-severe-PPC HR `.85 (.66-1.09)`, `P=.197`, and Schoenfeld P `.28` retain ordered endpoints, null containment, and directional coherence; diagnostic CI/P comparison yields no new observation. | None / None | Schoenfeld P is a separate assumption test; exact Cox inference details are absent. |
| S030 | Time-to-PEPC HR `1.12 (.89-1.39)`, `P=.314`, and Schoenfeld P `.67` retain ordered endpoints, null containment, and label/measure distinction; diagnostic CI/P comparison yields no new observation. | None / None | Schoenfeld P is a separate assumption test; exact Cox inference details are absent. |
| S031 | Mortality HR `1.67 (.40-6.97)`, `P=.484`, and Schoenfeld P `.14` retain internally compatible display relationships and match the main mortality result at displayed precision. C004 remains the same eFigure 11 mortality-versus-PEPC body-label mismatch; no new candidate was created. | C004 / None | Schoenfeld P is distinct from the mortality-effect P; visual plot identity remains unavailable in current fresh assets. |

## Pass-2 completion markers

- S001 — `PASS_2_COMPLETE`
- S002 — `PASS_2_COMPLETE`
- S003 — `PASS_2_COMPLETE`
- S004 — `PASS_2_COMPLETE`
- S005 — `PASS_2_COMPLETE`
- S006 — `PASS_2_COMPLETE`
- S007 — `PASS_2_COMPLETE`
- S008 — `PASS_2_COMPLETE`
- S009 — `PASS_2_COMPLETE`
- S010 — `PASS_2_COMPLETE`
- S011 — `PASS_2_COMPLETE`
- S012 — `PASS_2_COMPLETE`
- S013 — `PASS_2_COMPLETE`
- S014 — `PASS_2_COMPLETE`
- S015 — `PASS_2_COMPLETE`
- S016 — `PASS_2_COMPLETE`
- S017 — `PASS_2_COMPLETE`
- S018 — `PASS_2_COMPLETE`
- S019 — `PASS_2_COMPLETE`
- S020 — `PASS_2_COMPLETE`
- S021 — `PASS_2_COMPLETE`
- S022 — `PASS_2_COMPLETE`
- S023 — `PASS_2_COMPLETE`
- S024 — `PASS_2_COMPLETE`
- S025 — `PASS_2_COMPLETE`
- S026 — `PASS_2_COMPLETE`
- S027 — `PASS_2_COMPLETE`
- S028 — `PASS_2_COMPLETE`
- S029 — `PASS_2_COMPLETE`
- S030 — `PASS_2_COMPLETE`
- S031 — `PASS_2_COMPLETE`

## Handoff

- **Canonical relationship coverage:** 31/31 (`S001` through `S031`), each explicitly marked `PASS_2_COMPLETE`.
- **Existing stable-candidate observations revisited:** 8/8 (`C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`); statistical-scope intersections are identified above without a new disposition.
- **Genuinely new candidate observations for append:** 0; therefore no provisional append key is emitted.
- **Display-zero result:** no applicable display-zero relationship encountered; no candidate was based on P-value formatting.
- **Key retained limitations:** DOC-001 pp. 7 and 9 column serialization; unrecoverable plotted values/P values for DOC-005 eFigures 1-7; and the specifically named missing estimator, test, variance/covariance, sidedness, model, reference-direction, or estimand definitions.
