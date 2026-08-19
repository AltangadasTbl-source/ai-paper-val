# Statistical Consistency Review — Pass 2

## Completion record

- **Pass:** 2 of 2, independently performed after the complete candidate ledger and mechanical evidence recheck were available.
- **Exact scope:** every registered inferential relationship, **S001-S080**, in `statistics/relationship_inventory.md`; complete candidate ledger **C001-C017**; `checkers/numeric_consistency.md`; `checkers/cross_source_consistency.md`; and `verification/evidence_recheck.md`.
- **Source authority:** supplied DOC-001, DOC-002, and DOC-003 PDFs. Current maps and recheck records were locators and cross-lane evidence summaries; no web source or legacy conclusion was used.
- **Result:** all 80 relationships revisited and marked `PASS_2_COMPLETE` in the inventory. No genuinely new candidate proposal was identified. The five pass-1 statistical proposals are already represented by stable candidates C017, C004, C005, C006, and C007; the additional Table S6 matched-count contradiction is already C016.
- **Display-zero policy:** no `P = 0`, `p = 0.000`, or equivalent P-value display occurs in this scope. Printed zero event counts and `0.0%` cells are not P-value display zeros. No tail probability was derived and no display-zero proposal was emitted.

## Pass-2 relationship register

`PASS_2_COMPLETE` records a completed consistency check, not a validity, severity, acceptance, rejection, correction, or other adjudication. `MISSING_DEFINITION` names an input not supplied by the PDFs; it is not itself a candidate. Log-scale interval-to-tail comparisons remain diagnostics only.

| S ID | Pass-2 reconciliation across statistical, numeric, cross-source, and recheck lanes | Pass-2 status |
|---|---|---|
| S001 | Primary KM/log-rank/Cox framework, HR measure, 95% CI, contrast, and unadjusted-centre label remain matched to the main result. | PASS_2_COMPLETE |
| S002 | Schoenfeld P=.12 has no printed statistic or df; no reconstruction inferred. | PASS_2_COMPLETE — MISSING_DEFINITION(statistic, df) |
| S003 | Generalized-OR scale and favorable BA direction remain matched; WMW statistic and variance are absent. | PASS_2_COMPLETE — MISSING_DEFINITION(test statistic, variance) |
| S004 | Primary HR 0.32 (0.16-0.63), P<.001 is contained, ordered, directionally coherent, and repeated compatibly across main locations. Log-rank P and Cox CI remain distinct analyses. | PASS_2_COMPLETE |
| S005 | Thirty-day HR/CI contains the estimate and agrees in direction; the prior log-scale tail comparison remains diagnostic only because the row P test is unnamed. | PASS_2_COMPLETE — DIAGNOSTIC ONLY; MISSING_DEFINITION(row P test) |
| S006 | Post-hoc qualifying-artery stroke HR/CI is ordered, contains the estimate, and carries the correct post-hoc/time label. | PASS_2_COMPLETE |
| S007 | Post-hoc revascularization HR/CI is ordered, contains the estimate, and carries the correct post-hoc/time label. | PASS_2_COMPLETE |
| S008 | Ninety-day HR/CI contains the estimate and has compatible direction; row P test is not supplied. | PASS_2_COMPLETE — MISSING_DEFINITION(row P test) |
| S009 | NA HR remains compatible with the printed zero-event arm; the P-test definition is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(row P test) |
| S010 | Ninety-day generalized OR/CI is ordered, contains the estimate, and uses the stated favorable-shift scale; log-scale tail check remains diagnostic. | PASS_2_COMPLETE — DIAGNOSTIC ONLY |
| S011 | One-year target-territory HR/CI contains the estimate; direction and repeated narrative agree; row P test is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(row P test) |
| S012 | One-year revascularization HR/CI contains the estimate and has compatible direction; row P test is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(row P test) |
| S013 | The incidence-difference estimate -0.4% remains outside its printed CI (-2.4% to -1.7%); direct source and crude count-direction check match C017. HR/CI/P itself is not reconstructed because the row P test is unnamed. | PASS_2_COMPLETE — EXISTING C017; MISSING_DEFINITION(incidence-difference CI method, row P test) |
| S014 | One-year generalized OR/CI is ordered, contains the estimate, and uses the stated favorable-shift scale; log-scale tail check remains diagnostic. | PASS_2_COMPLETE — DIAGNOSTIC ONLY |
| S015 | Combined-vascular-events HR/CI contains the estimate and direction agrees; row P test is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(row P test) |
| S016 | Narrative secondary-result repetitions remain matched to Table 2 after outcome, time-window, and measure matching. | PASS_2_COMPLETE |
| S017 | Centre-adjusted and removal-of-revascularization estimates/P values remain matched to Tables S6/S10. Table S6 population/count/percentage implications are existing C004 and C016, not a new inferential contradiction. | PASS_2_COMPLETE — EXISTING C004, C016 |
| S018 | Disabling-stroke direction and P=.02 remain matched to Table S11; source labels chi-square but does not supply statistic/df for exact reconstruction. | PASS_2_COMPLETE — MISSING_DEFINITION(chi-square statistic, df) |
| S019 | Figure 2 overall HR/CI exactly repeats the matched primary result. | PASS_2_COMPLETE |
| S020 | Age-subgroup HRs are contained in ordered CIs and interaction label/direction is coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S021 | Sex-subgroup HRs are contained in ordered CIs and interaction label/direction is coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S022 | Hypertension-subgroup HRs are contained in ordered CIs and interaction label/direction is coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S023 | Diabetes-subgroup HRs are contained in ordered CIs and interaction label/direction is coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S024 | Smoking-subgroup HRs are contained in ordered CIs and interaction label/direction is coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S025 | eGFR subgroup labels/units, HRs, CIs, and interaction direction are coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S026 | Stenosis subgroup thresholds, HRs, CIs, and interaction direction are coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S027 | Figure BMI grouping differs from the three-level planned definition, but the final subgroup model is absent and no matched-result contradiction is supplied. | PASS_2_COMPLETE — MISSING_DEFINITION(final subgroup-model specification) |
| S028 | Hypoperfusion Yes HR/CI is coherent; NA for No remains explained by zero AMM events. | PASS_2_COMPLETE |
| S029 | Circulation subgroup HRs/CIs and interaction label are coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S030 | TIA/stroke subgroup HRs/CIs and interaction label are coherent; statistic/df absent. | PASS_2_COMPLETE — MISSING_DEFINITION(interaction statistic, df) |
| S031 | Figure 3 primary HR/CI/P exactly repeats S004/S019 with the same direction. | PASS_2_COMPLETE |
| S032 | Landmark HRs are contained in ordered CIs; early estimate matches S005. Selection/censoring/model details are absent. | PASS_2_COMPLETE — MISSING_DEFINITION(landmark analysis specification) |
| S033 | Centre-adjusted HR/CI/P remains internally ordered and matches S017. The BA 9 (3.9) versus n=249 discrepancy is mechanically confirmed as existing C004; its different matched event count is existing C016. | PASS_2_COMPLETE — EXISTING C004, C016 |
| S034 | Site HRs/CIs and interaction P match S017. Header total 471 versus site total 501 and cell-percentage implications are mechanically confirmed as existing C005. | PASS_2_COMPLETE — EXISTING C005 |
| S035 | PPS primary HR/CI/P is ordered and contains the estimate. PPS header/percentage population mismatch is mechanically confirmed as existing C006. | PASS_2_COMPLETE — EXISTING C006 |
| S036 | PPS 30-day component HR/CI is ordered and contains the estimate; shared PPS-header issue is existing C006. | PASS_2_COMPLETE — EXISTING C006 |
| S037 | PPS qualifying-artery-stroke HR/CI is ordered and contains the estimate; shared PPS-header issue is existing C006. | PASS_2_COMPLETE — EXISTING C006 |
| S038 | PPS revascularization HR/CI is ordered and contains the estimate; shared PPS-header issue is existing C006. | PASS_2_COMPLETE — EXISTING C006 |
| S039 | ATS primary HR/CI/P is ordered and contains the estimate. ATS header/percentage population mismatch is mechanically confirmed as existing C007. | PASS_2_COMPLETE — EXISTING C007 |
| S040 | ATS 30-day HR/CI is ordered and contains the estimate; shared ATS-header issue is existing C007. | PASS_2_COMPLETE — EXISTING C007 |
| S041 | ATS qualifying-artery-stroke HR/CI is ordered and contains the estimate; shared ATS-header issue is existing C007. | PASS_2_COMPLETE — EXISTING C007 |
| S042 | ATS revascularization HR/CI is ordered and contains the estimate; shared ATS-header issue is existing C007. | PASS_2_COMPLETE — EXISTING C007 |
| S043 | ITT post-hoc HR/CI/P contains the estimate and matches S017. | PASS_2_COMPLETE |
| S044 | PPS post-hoc HR/CI/P contains the estimate; denominators 233/238 remain the direct comparator for C006. | PASS_2_COMPLETE — EXISTING C006 CONTEXT |
| S045 | ATS post-hoc HR/CI/P contains the estimate; denominators 247/254 remain the direct comparator for C007. | PASS_2_COMPLETE — EXISTING C007 CONTEXT |
| S046 | Table S11 overall counts/percentages and P=.84 retain the named chi-square label; no statistic/df or exact variant is supplied. | PASS_2_COMPLETE — MISSING_DEFINITION(chi-square statistic, df, variant) |
| S047 | Table S11 nervous-system counts/percentages and P=.35 retain the named chi-square label; no statistic/df or exact variant is supplied. | PASS_2_COMPLETE — MISSING_DEFINITION(chi-square statistic, df, variant) |
| S048 | Table S11 symptomatic-ICH counts/percentages and P=.37 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S049 | Table S11 asymptomatic-ICH counts/percentages and P=.12 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S050 | Table S11 any-ICH counts/percentages and P=.07 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S051 | Table S11 disabling-stroke counts and P=.02 repeat S018; chi-square statistic/df and variant are absent. | PASS_2_COMPLETE — MISSING_DEFINITION(chi-square statistic, df, variant) |
| S052 | Table S11 vascular/lymphatic counts/percentages and P=.62 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S053 | Table S11 metabolic/nutritional counts/percentages and P=1.00 retain the Fisher label; this is not a display-zero P value. Sidedness/exact convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S054 | Table S11 infection counts/percentages and P=.50 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S055 | Table S11 operations counts/percentages and P=.25 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S056 | Table S11 respiratory counts/percentages and P=1.00 retain the Fisher label; this is not a display-zero P value. Sidedness/exact convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S057 | Table S11 gastrointestinal counts/percentages and P=1.00 retain the Fisher label; this is not a display-zero P value. Sidedness/exact convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S058 | Table S11 injury/poisoning counts/percentages and P=1.00 retain the Fisher label; this is not a display-zero P value. Sidedness/exact convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S059 | Table S11 tumour/cyst/polyp counts/percentages and P=.50 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S060 | Table S11 reproductive/breast counts/percentages and P=.50 retain the Fisher label; sidedness/exact test convention is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(Fisher sidedness/convention) |
| S061 | Original-protocol sample-size/log-rank assumptions remain historical planning values; hazard, accrual, and censoring definitions are insufficient for reconstruction. | PASS_2_COMPLETE — MISSING_DEFINITION(hazard, accrual, censoring) |
| S062 | Original-protocol interim alpha values are versioned planning definitions, not a realised-result comparator. | PASS_2_COMPLETE |
| S063 | Protocol analysis framework remains label-compatible with the main paper; realised statistic/variance are absent. | PASS_2_COMPLETE — MISSING_DEFINITION(realised statistic, variance) |
| S064 | Original 802-case planning arithmetic is internally coherent at printed precision; sample-size equation is absent. | PASS_2_COMPLETE — MISSING_DEFINITION(sample-size equation) |
| S065 | Original-protocol interim plan is historical and is distinguished from later revision. | PASS_2_COMPLETE |
| S066 | Planned subgroup definitions match main labels except final BMI grouping/model, which is not supplied. | PASS_2_COMPLETE — MISSING_DEFINITION(final subgroup model) |
| S067 | Revised 7%/15%, 80%, one-sided 2.5%, N=512 planning values are arithmetically coherent; relative-reduction calculation remains diagnostic only. | PASS_2_COMPLETE — DIAGNOSTIC ONLY |
| S068 | V2.3 framework labels remain compatible with main results; realised statistic/variance are absent. | PASS_2_COMPLETE — MISSING_DEFINITION(realised statistic, variance) |
| S069 | V2.3 15%/7%, one-sided 2.5%, N=512 planning relationship is internally coherent. | PASS_2_COMPLETE |
| S070 | V2.3 subgroup labels match main labels except the unreported final BMI subgroup model. | PASS_2_COMPLETE — MISSING_DEFINITION(final subgroup model) |
| S071 | SAP v1/v2 KM/log-rank/Cox framework matches main labels. No exact P-from-CI comparison is appropriate because the reported log-rank P and Cox CI are distinct analyses. | PASS_2_COMPLETE |
| S072 | SAP secondary Cox framework agrees with matched main secondary HR labels/time windows; later unreported endpoints are not compared as results. | PASS_2_COMPLETE |
| S073 | SAP ordinal-logistic/common-OR plan and main WMW-derived generalized OR are explicitly separated by the reported proportional-odds failure; no contradiction. | PASS_2_COMPLETE |
| S074 | SAP restenosis logistic-OR plan has no matched reported OR/CI; absence of output is recorded, not treated as a contradiction. | PASS_2_COMPLETE — MISSING_DEFINITION(reported model output) |
| S075 | SAP permits t-test/Wilcoxon for EQ-5D; main gives P=.40 but not selected test/statistic, so no reconstruction. | PASS_2_COMPLETE — MISSING_DEFINITION(selected test, statistic) |
| S076 | SAP safety Fisher plan and Table S11 row labels do not establish a mismatch; event-versus-person basis remains unspecified. | PASS_2_COMPLETE — MISSING_DEFINITION(event/person basis) |
| S077 | SAP medication chi-square/Fisher plan has no matched observed inferential medication output. | PASS_2_COMPLETE — MISSING_DEFINITION(observed output, selected test) |
| S078 | SAP v1 interim plan is explicitly historical in the v1/v2 revision table. | PASS_2_COMPLETE |
| S079 | SAP v2 no-interim rule is explicitly revised, so it is not a contradiction with S078. | PASS_2_COMPLETE |
| S080 | SAP v1/v2 sample-size assumptions are version-labelled and account for 802 versus 512; no observed-result contradiction. | PASS_2_COMPLETE |

## Cross-lane candidate reconciliation

- **C004/C016 and S033:** The evidence recheck confirms both distinct observations in Table S6: the internal `9 (3.9)` versus `n=249` percentage mismatch and the separate 9-versus-11 matched primary-event-count issue. They remain distinct existing stable IDs.
- **C005 and S034:** The evidence recheck confirms that Table S7's stated 233/238 headers, 501 site total, and site cell percentages cannot all describe one disclosed population.
- **C006 and S035-S038; C007 and S039-S042:** The evidence recheck confirms that Tables S8/S9 effect estimates have coherent displayed point estimates and CIs, while their header/percentage populations are separate, already-registered denominator-label issues.
- **C014 and S039-S042 context:** The Table S9 `8 (3.3)` issue remains an existing arithmetic/denominator proposal; it does not create a new HR/CI/P incompatibility.
- **C017 and S013:** The evidence recheck directly confirms the incidence-difference non-containment. It is the same observation as pass-1 SP-01 and existing C017, not a new proposal.
- **C001-C003, C008-C015:** Their recheck facts concern arithmetic, denominator, population, definition, label, or cross-document relationships. None establishes an additional unregistered contradiction in an S relationship.

## Candidate-proposal result

- **New candidate proposals:** 0.
- **Existing candidate links revisited:** C004, C005, C006, C007, C016, and C017.
- **Stable candidates altered, renumbered, or deleted:** none.

## Limitations and missing definitions

The PDFs do not provide Cox coefficients/SEs, covariance or variance estimators, exact interaction or Schoenfeld statistics/df, selected row-level tests for most Table 2 P values, Fisher sidedness convention, chi-square variant/statistic/df, final subgroup model details, landmark-analysis specification, or event/person safety basis. No sidedness, df, denominator, covariance, model, estimand mapping, multiplicity procedure, or variance estimator was inferred from convention. Where an interval-to-tail comparison was retained, it is explicitly a diagnostic and does not replace the supplied analysis.

## Compact handoff

**Explicit pass-2 relationship register:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080.

- **S coverage:** 80 of 80, S001-S080, each `PASS_2_COMPLETE`.
- **New proposals:** 0.
- **Display-zero-only proposals:** 0.
- **Artifact:** `.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md`.
