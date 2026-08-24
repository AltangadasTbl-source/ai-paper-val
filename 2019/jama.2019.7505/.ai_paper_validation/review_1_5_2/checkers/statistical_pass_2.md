# Statistical Consistency Review — Pass 2

## Independent pass-2 scope and evidence boundary

This fresh, distinct statistical pass revisited all canonical inferential relationships: `S001`–`S038` and `S200`–`S214` (53 total). It used only the supplied six PDFs, current-run fresh preprocessing/evidence maps, the complete current numeric and cross-source checker artifacts, `candidate_ledger.md` (`C001`–`C004`), and `verification/evidence_recheck.md`. Preserved prior-run material and the web were not used.

For each relationship, pass 2 rechecked applicable denominator/count arithmetic, point-estimate containment, endpoint order, sign/direction, effect-measure/scale/label, duplicate/repeated values, cross-source identity, and the mechanical-recheck implications. Interval/P-value/test/statistic/SE compatibility was required only where the PDFs supply compatible inferential definitions. Sidedness, degrees of freedom, covariance, variance estimator, zero-cell rule, multiplicity implementation, model-to-estimand mapping, and denominators were not supplied by convention.

`PASS_2_COMPLETE` is a coverage record only. It makes no severity, validity, acceptance, rejection, correction, or other adjudication decision. No literal `P = 0`, `p = 0.000`, or equivalent was a candidate in this scope; no such display was found as a relationship-specific issue.

## Per-relationship pass-2 records

| ID | Exact supplied-source scope | Pass-2 reconciliation and result |
|---|---|---|
| S001 | DOC-001 PDF pp. 1, 9 | Primary PPC counts/rates, high-minus-low difference, RR, ordered CIs, and abstract/Table 3 repetition agree. `PASS_2_COMPLETE` — no new proposal. |
| S002 | DOC-001 PDF pp. 1, 9 | Both printed intervals contain the −8.6-point estimate, but their upper endpoints have opposite signs for an otherwise matched result; C001 recheck supports that direct cross-location mismatch. `PASS_2_COMPLETE` — covered by C001; no new proposal. |
| S003 | DOC-001 PDF p. 4 | Primary alpha `.044`, RR/CI, chi-square, Cox HR, and random-site sensitivity labels are stated; no result-level comparator is supplied here. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S004 | DOC-001 PDF p. 4 | Binary RR, hospital-free-day mean-difference/t-test, mortality Cox-HR, and secondary-alpha labels distinguish measures/scales. `PASS_2_COMPLETE` — no new proposal. |
| S005 | DOC-001 PDF p. 7 Table 2 | Tidal-volume estimates are contained in ordered CIs and their displayed directions agree with group means. Table-specific test/CI/repeated-measure rules are absent. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S006 | DOC-001 PDF p. 7 Table 2 | PEEP differences, positive CIs, units, and group direction agree. `PASS_2_COMPLETE` — unnamed Table 2 inference rule prevents P reconstruction; no new proposal. |
| S007 | DOC-001 PDF p. 7 Table 2 | Recruitment counts, 97.1-point difference, CI order/containment, and direction reconcile. `PASS_2_COMPLETE` — no new proposal. |
| S008 | DOC-001 PDF p. 7 Table 2 | Peak-pressure effects are contained in positive ordered CIs and agree with means. `PASS_2_COMPLETE` — Table 2 inferential construction not named; no new proposal. |
| S009 | DOC-001 PDF p. 7 Table 2 | Driving-pressure effects/CIs are negative as expected from high-minus-low means; the plateau-minus-PEEP definition fixes the scale. `PASS_2_COMPLETE` — no new proposal. |
| S010 | DOC-001 PDF p. 7 Table 2 | Respiratory-rate effects/CIs agree with group direction; displayed zero endpoints are compatible with finite rounding. `PASS_2_COMPLETE` — no new proposal. |
| S011 | DOC-001 PDF p. 7 Table 2 | FIO2 effects/CIs agree with group means and units; a printed endpoint `0` is finite rounding, not an inferential contradiction. `PASS_2_COMPLETE` — no new proposal. |
| S012 | DOC-001 PDF p. 7 Table 2 | SpO2 effects are contained in positive ordered CIs and directions agree. `PASS_2_COMPLETE` — no new proposal. |
| S013 | DOC-001 PDF p. 7 Table 2 | End-tidal CO2 directions, CI order/containment, and units agree. `PASS_2_COMPLETE` — Table 2 test/CI definition absent; no new proposal. |
| S014 | DOC-001 PDF p. 7 Table 2 | Heart-rate directions and all estimates/ordered CIs agree with displayed means. `PASS_2_COMPLETE` — no new proposal. |
| S015 | DOC-001 PDF p. 7 Table 2 | Mean-arterial-pressure effects are contained and sign-consistent; apparent mean/difference granularity is compatible with rounding. `PASS_2_COMPLETE` — no new proposal. |
| S016 | DOC-001 PDF pp. 7-8 Table 2 | Categorical distributions, available differences/CIs, denominators, and P labels are coherent; treatment subtypes are not falsely treated as one partition. `PASS_2_COMPLETE` — Table 2 categorical-test rule absent; no new proposal. |
| S017 | DOC-001 PDF p. 8 Table 2 | Blockade/monitoring/reversal counts, denominators, effects, CIs, and direction reconcile. `PASS_2_COMPLETE` — no new proposal. |
| S018 | DOC-001 PDF p. 8 Table 2 | Fluid, colloid, and urine labels distinguish volume, use, median/IQR, and difference; estimates are contained in ordered CIs. `PASS_2_COMPLETE` — medians versus displayed difference estimator/test not defined; no new proposal. |
| S019 | DOC-001 PDF p. 8 Table 2 | Blood-product/count-rate distinctions and continuous-measure CIs are coherent; `P > .99` is not a display-zero result. `PASS_2_COMPLETE` — unnamed Table 2 rules; no new proposal. |
| S020 | DOC-001 PDF p. 9 Table 3 | Mild/moderate/severe respiratory-failure counts, RRs, CIs, and directions reconcile. `PASS_2_COMPLETE` — no new proposal. |
| S021 | DOC-001 PDF p. 9 Table 3 | Atelectasis, pleural effusion, and infiltrates labels/effects/CIs agree with event direction; pleural CI excludes 1 consistently with its printed P. `PASS_2_COMPLETE` — no new proposal. |
| S022 | DOC-001 PDF p. 9 Table 3 | Edema through pneumothorax effects are contained and direction-consistent at printed precision; `P > .99` does not denote a display-zero. `PASS_2_COMPLETE` — no new proposal. |
| S023 | DOC-001 PDF p. 9 Table 3 | Severe-PPC and extrapulmonary-composite event risks/RRs/CIs agree. `PASS_2_COMPLETE` — no new proposal. |
| S024 | DOC-001 PDF p. 9 Table 3 | SIRS, sepsis, severe-sepsis, and shock RRs/CIs/directions agree with displayed risks. `PASS_2_COMPLETE` — no new proposal. |
| S025 | DOC-001 PDF p. 9 Table 3 | GI-failure RR/CI is contained and the grade-distribution P is separately labeled. `PASS_2_COMPLETE` — distribution-test definition absent; no new proposal. |
| S026 | DOC-001 PDF p. 9 Table 3 | AKI RR/CI and grade totals/rates reconcile; grade-distribution P is separately labeled. `PASS_2_COMPLETE` — distribution-test definition absent; no new proposal. |
| S027 | DOC-001 PDF pp. 4, 9-10 Table 3 | DIC prints 1/989 versus 0/987 with finite RR `2.00 (1.91-2.09)` and `P > .99`; C002 recheck confirms that a zero-cell rule/alternate estimator is missing and that interval/P duality cannot be imposed across differently named procedures. `PASS_2_COMPLETE` — covered by C002; no new proposal. |
| S028 | DOC-001 PDF p. 9 Table 3 | Wound-healing and unexpected-ICU RRs/CIs/directions agree with event counts. `PASS_2_COMPLETE` — no new proposal. |
| S029 | DOC-001 PDF p. 9 Table 3 | Hospital-free-days mean difference is contained in its ordered CI and the mean-difference/t-test label is explicit. `PASS_2_COMPLETE` — no new proposal. |
| S030 | DOC-001 PDF p. 9 Table 3 | Hypoxemia, hypotension, and bradycardia event directions/RRs/CIs agree; the hypoxemia abstract interval is separately C001/S002. `PASS_2_COMPLETE` — no new proposal. |
| S031 | DOC-001 PDF p. 9 Table 3 | In-hospital-mortality RR is contained in its CI; scale/timepoint remain distinct from five-day Cox mortality. `PASS_2_COMPLETE` — no new proposal. |
| S032 | DOC-001 PDF p. 10 Table 3 | Rescue and vasoactive outcome effects/CIs/directions agree. `PASS_2_COMPLETE` — no new proposal. |
| S033 | DOC-001 PDF p. 10 Table 3 | Five-day mortality HR is contained in an ordered CI; the Cox label distinguishes it from the Table 3 RRs. `PASS_2_COMPLETE` — no new proposal. |
| S034 | DOC-001 PDF p. 10 Figure 2 | Surgery and BMI subgroup RRs/CIs are contained and ordered; interaction P values have no printed model coefficients/variance. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S035 | DOC-001 PDF p. 10 Figure 2 | SpO2, incision, waist/hip subgroup RRs/CIs and labels reconcile; interaction reconstruction is not defined. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S036 | DOC-001 PDF pp. 1, 9-10 | All-patient PPC RR `.93 (.83-1.04)` repeats across abstract, Table 3, and Figure 2 with matched population/contrast. `PASS_2_COMPLETE` — no new proposal. |
| S037 | DOC-001 PDF pp. 8, 10; Table 3 pp. 9-10 | Narrative primary/mild/pleural/adverse-event statements retain the Table 3 values and directions. `PASS_2_COMPLETE` — no new proposal. |
| S038 | DOC-001 PDF pp. 10-12; DOC-005 PDF pp. 29-30 | ITT, per-protocol, adjusted, and sensitivity analyses are distinct estimands; qualitative “similar/not significantly different” text has no numerical same-model comparator. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S200 | DOC-002 PDF pp. 9-10; DOC-003 PDF pp. 2-3 | Original/revised sample-size assumptions agree when matched by protocol version; no software/rounding implementation supports an independent reconstruction. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S201 | DOC-002 PDF pp. 20-23; DOC-003 PDF pp. 2-3 | Interim looks, gamma, and efficacy/futility boundaries repeat exactly. `PASS_2_COMPLETE` — spending implementation and sidedness not fully supplied; no new proposal. |
| S202 | DOC-002 physical PDF p. 23 (footer p. 22); DOC-004 PDF pp. 2-3 | The uninterrupted protocol phrase combines `odds ratio` and `relative risks`; C003 recheck confirms no separator, conversion, or intended measure is supplied, while final SAP names primary RR. `PASS_2_COMPLETE` — covered by C003; no new proposal. |
| S203 | DOC-004 PDF pp. 1-3; DOC-001 PDF p. 4 | Final-SAP and article definitions agree on primary RR/CI, alpha `.044`, and time-to-event methods. `PASS_2_COMPLETE` — no new proposal. |
| S204 | DOC-004 PDF pp. 1-3 | Secondary RR/CI/chi-square, day-90 mean difference/t test, and zero-inflated-beta mean ratio are explicitly distinguished. `PASS_2_COMPLETE` — no direct result comparator for the mean-ratio model; no new proposal. |
| S205 | DOC-004 PDF pp. 2-3; DOC-005 PDF p. 30 | Interaction, mixed-effect, proportional-odds, Bonferroni CI, GEE OR, and average-relative-effect labels are distinguished and agree with eTable 9 footnotes where applicable. `PASS_2_COMPLETE` — no unprinted mapping inferred; no new proposal. |
| S206 | DOC-005 PDF p. 22; DOC-002 PDF pp. 27-33 | ARISCAT OR/CIs, betas, score arithmetic, score scale, and `n=1624` match between sources; beta-times-10 rounding is defined. `PASS_2_COMPLETE` — no new proposal. |
| S207 | DOC-005 PDF pp. 24-28 | eTables 3-7 counts/percentages/means and P columns have no supplied per-table test, variance, or repeated-measure rule. `PASS_2_COMPLETE` — definition-bounded; no new proposal. |
| S208 | DOC-005 PDF p. 29; DOC-004 PDF pp. 1-3 | eTable 8's `Effect Estimate 95% CI` header omits a measure label. The complete ledger records this as a missing definition only; no same-result contradictory label or explicit mapping is supplied. `PASS_2_COMPLETE` — definition-bounded, no new proposal. |
| S209 | DOC-005 PDF p. 30; DOC-004 PDF pp. 2-3 | eTable 9 separates random-effect OR, proportional-odds OR/Wilcoxon, common-effect GEE OR, interaction P, and average-relative effect; CIs are ordered and estimates contained. `PASS_2_COMPLETE` — full coefficients/variance not printed; no new proposal. |
| S210 | DOC-005 PDF pp. 31-37 | eFigures 2-7 label means/95% CIs and time-by-group mixed-effect P values. `PASS_2_COMPLETE` — coordinates, variance, and repeated-measure details do not permit a mechanical P recheck; no new proposal. |
| S211 | DOC-005 PDF p. 38 | PPC HR `.88 (.73-1.06)`, P `.190`, and Schoenfeld P `.05` use identified but different quantities. Diagnostic log-HR/rounded-CI Wald approximation is about `.18`; common effect-test/CI construction is not supplied. `PASS_2_COMPLETE` — diagnostic only, no new proposal. |
| S212 | DOC-005 PDF p. 39 | Severe-PPC HR `.85 (.66-1.09)`, P `.197`, and Schoenfeld P `.28` are label-distinguished. Diagnostic log-HR/rounded-CI Wald approximation is about `.20`; compatible rule absent. `PASS_2_COMPLETE` — diagnostic only, no new proposal. |
| S213 | DOC-005 PDF p. 40 | PEPC HR `1.12 (.89-1.39)`, P `.314`, and Schoenfeld P `.67` are label-distinguished. Diagnostic log-HR/rounded-CI Wald approximation is about `.32`; compatible rule absent. `PASS_2_COMPLETE` — diagnostic only, no new proposal. |
| S214 | DOC-005 PDF p. 41; DOC-001 PDF p. 10; DOC-005 PDF p. 40 | eFigure 11's title/axis, HR/CI/P, and matched Table 3 values identify five-day mortality, while its narrative calls the same `.5%/.3%` values extra-pulmonary complications; C004 recheck supports the label mismatch. `PASS_2_COMPLETE` — covered by C004; no new proposal. |

## Existing stable-candidate reconciliation

| Stable ID | Statistical relationship(s) revisited | Pass-2 support check |
|---|---|---|
| C001 | S002 | The abstract and Table 3 are same population/outcome/contrast/estimate/confidence level and visibly print `+6.1` versus `−6.1` as the upper endpoint. Both contain `−8.6`; the supported issue is the cross-location sign mismatch, not noncontainment. |
| C002 | S027 | Displayed counts have a zero low-group risk; a finite RR requires an unprinted zero-cell rule/alternate estimator. CI/P incompatibility was not mechanically asserted because the source names different CI and P procedures. |
| C003 | S202 | The protocol’s unseparated compound odds-ratio/relative-risk phrase is directly printed; final SAP distinguishes primary RR and separate OR contexts. No intended protocol estimand can be inferred. |
| C004 | S214 | eFigure 11 narrative outcome noun conflicts with its mortality title/axis/effect label and Table 3 matching mortality values; eFigure 10 supplies the distinct PEPC comparator. |

All four stable records remain supported by the mechanical recheck facts. This pass assigns no disposition beyond the ledger’s existing `Pending Human Adjudication` status.

## New proposals

None. Every source-grounded statistical inconsistency identified in this pass is already represented by `C001`–`C004`. No proposal was emitted for display notation, an unreported inferential definition, a diagnostic approximation, or a non-comparable analysis/population/effect measure.

## Limitations

- Table 2 does not state table-specific tests, CI construction, variance estimators, degrees of freedom, or repeated-time handling.
- eTables 3-7 and eFigures 2-7 lack all definitions needed to reconstruct displayed P values from summaries.
- Group-sequential calculations lack a fully reproducible spending/software/sidedness specification.
- The DIC record lacks its estimator, zero-cell correction, exact CI formula, chi-square variant, and analysis-output alignment.
- Survival figures do not state a compatible common effect-test statistic and CI construction; the stated Schoenfeld P values concern a different diagnostic.
- eTable 8 does not identify its effect-measure column; the supplied sources do not explicitly map it to a specific per-protocol estimand.

## Pass-2 counts

- **Relationship scope completed:** 53 (`S001`–`S038`; `S200`–`S214`).
- **Existing stable candidates revisited:** 4 (`C001`, `C002`, `C003`, `C004`).
- **Genuinely new proposals:** 0.
- **Display-zero-only candidates:** 0.
