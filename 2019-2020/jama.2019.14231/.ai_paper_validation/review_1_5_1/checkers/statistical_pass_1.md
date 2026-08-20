# Statistical Consistency Review — Pass 1

## Scope and method

- **Reviewer runtime ID:** `root/statistics_pass_1`
- **Execution:** fresh `gpt-5.6-terra` agent at `high` reasoning effort.
- **Assigned scope:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025 (25/25).
- **Authority and locations:** the three supplied PDFs were checked directly. The current source-linked mapper inventories and reusable page locators were used only to locate and organize the checks. No legacy candidate, checker, verifier, critic, adjudication, or report artifact was used as a scientific input.
- **Checks applied:** point-estimate containment; endpoint order; direction and contrast labels; effect-measure, scale, and test labels; matching repetitions; and interval/P/test/statistic/SE compatibility only where the supplied source gives a compatible inferential definition. Unstated models, sidedness, degrees of freedom, covariance, variance estimators, multiplicity families, and denominators were not inferred.
- **Display-zero rule:** no assigned relationship prints `P = 0`, `p = 0.000`, or equivalent. Printed `<.001` values are threshold displays, not display zeros. Thus no `DISPLAY_ZERO_NOT_CANDIDATE` entry applies.

## Temporary proposal register

### STAT1-P001 — Incorrect eTable cross-reference for the time-varying hazard-ratio display

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 PDF p. 19](../../../joi190103supp1_prod.pdf#page=19); matched duplicate [DOC-002 PDF p. 10](../../../joi190103supp1_prod.pdf#page=10).
- **Direct observation:** The p. 19 time-varying-HR narrative states that “eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years.” Immediately below, the displayed table is headed “eTable 7. Time-Varying Hazard Ratios and 95% CIs ...”; the same table is headed eTable 7 on p. 10 and its 24 HR/CI cells are identical there and on p. 19.
- **Consistency rule:** A narrative cross-reference for a displayed result should identify the table that actually contains that result. The supplied source provides both comparator labels and the duplicated table identity.
- **Human question:** Confirm whether “eTable 4” in the p. 19 narrative is an unintended cross-reference rather than a reference to a different omitted display.
- **Status:** Pending Human Adjudication. This is a temporary pass-1 proposal only; it is not a stable `C` ID, severity, validity finding, or correction.

## Relationship-level pass-1 records

### S001 — Primary-composite adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 1, 4, and 7](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) consistently print fully adjusted surgery-versus-nonsurgery HR 0.61 (95% CI 0.55-0.69), with `P<.001`. The estimate is within ordered positive endpoints and the HR/CI direction (below 1) agrees with the stated lower relative instantaneous risk and lower cumulative incidence in surgery. The repeated values agree after matching outcome, contrast, model, and rounding. The supplied source identifies adjusted Cox models and two-sided .05/95% conventions, but does not provide coefficient SE, test statistic, degrees of freedom, exact P, or model covariance; no numerical P/CI reconstruction was performed. No proposal.

### S002 — Secondary-composite adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 4 and 7](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.62 (0.53-0.72), `P<.001`, fully adjusted Cox model. The point estimate is contained, endpoints are ordered, and the below-null direction agrees with lower surgery cumulative incidence. No compatible SE/statistic/exact-P inputs are supplied. No proposal.

### S003 — All-cause-mortality adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 1, 4, and 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.59 (0.48-0.72), `P<.001`, for the fully adjusted Cox model. The estimate is contained in ordered endpoints and agrees with lower surgery mortality incidence. No compatible SE/statistic/exact-P inputs are printed. No proposal.

### S004 — Heart-failure adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.38 (0.30-0.49), `P<.001`. The estimate is contained in ordered endpoints and its direction agrees with lower surgery cumulative incidence; both sources identify the fully adjusted Cox analysis and outcome-specific risk set. No compatible SE/statistic/exact-P inputs are printed. No proposal.

### S005 — Coronary-disease adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.69 (0.54-0.87), `P=.002`. The estimate is contained in ordered endpoints and direction agrees with lower surgery cumulative incidence. The fully adjusted Cox label is supplied, but no compatible SE, test statistic, exact testing rule, or degrees of freedom is printed for a numerical P/CI check. No proposal.

### S006 — Cerebrovascular-disease adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.67 (0.48-0.94), `P=.02`. The HR lies within ordered endpoints and below-null direction agrees with lower surgery cumulative incidence. No compatible SE/statistic/exact-P inputs are supplied. No proposal.

### S007 — Nephropathy adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.40 (0.31-0.52), `P<.001`. The estimate is contained in ordered endpoints and direction agrees with lower surgery cumulative incidence; the sources identify fully adjusted Cox models and outcome-specific exclusions. No compatible SE/statistic/exact-P inputs are printed. No proposal.

### S008 — Atrial-fibrillation adjusted HR

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7-8](../../../jama_aminian_2019_oi_190103.pdf#page=7) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) agree on HR 0.78 (0.62-0.97), outcome `P=.03`. The estimate is contained in ordered endpoints and direction agrees with lower surgery cumulative incidence. The distinct PH-assumption P=.04 is explicitly labeled in the eTable and is not the outcome P value; no P mismatch is created. No compatible SE/statistic/exact-P inputs are printed. No proposal.

### S009 — Composite and mortality 8-year absolute risk differences

**PASS_1_COMPLETE.** [DOC-001 PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7) labels ARD as nonsurgical minus surgery and labels the intervals 95% bootstrap CIs from 1,000 samples. Primary 16.9 (13.1-20.4), secondary 10.6 (7.5-13.6), and mortality 7.8 (5.1-10.2) each contain their estimate with correctly ordered endpoints; positive differences agree with the displayed higher nonsurgical 8-year incidences. The stated percentile-bootstrap construction does not supply bootstrap replicates, sampling details, or covariance, so no diagnostic recalculation was attempted. No proposal.

### S010 — Individual-endpoint 8-year absolute risk differences

**PASS_1_COMPLETE.** [DOC-001 PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7) gives nonsurgical-minus-surgery ARDs with 95% 1,000-sample bootstrap CIs: heart failure 12.9 (10.4-15.1), coronary disease 4.2 (1.9-6.8), cerebrovascular disease 1.8 (-0.03 to 3.4), nephropathy 11.1 (8.8-13.6), and atrial fibrillation 6.5 (4.4-8.7). Every estimate is contained in ordered endpoints and positive directions agree with the displayed incidence contrasts. Bootstrap inputs needed for an inferential recalculation are absent. No proposal.

### S011 — Longitudinal weight-difference estimates

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7 and 9](../../../jama_aminian_2019_oi_190103.pdf#page=9) and [DOC-002 PDF p. 12](../../../joi190103supp1_prod.pdf#page=12) are compatible after contrast matching: the main article reports an 8-year reduction difference of 20.3 kg (20.1-20.6) and total-weight-loss difference 14.7% (14.5-14.9), while eTable 8 reports surgery-minus-nonsurgery change of -20.3 kg (-20.6 to -20.0). The sign reversal follows the stated contrast/representation (larger positive reduction versus signed change), not a conflict. All reported estimates are contained in ordered intervals. The flexible treatment-interacted 4-knot spline is named, but coefficient covariance, fit specification, and exact P-test details are absent; no P/CI reconstruction. No proposal.

### S012 — Longitudinal HbA1c-difference estimates

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 7 and 9](../../../jama_aminian_2019_oi_190103.pdf#page=9) reports a 1.1% between-group change difference (1.0-1.2), `P<.001`; [DOC-002 PDF p. 12](../../../joi190103supp1_prod.pdf#page=12) gives surgery-minus-nonsurgery HbA1c change -1.1 (-1.2 to -1.0), `P<.001`, at 8 years. The signs are compatible with the opposite stated contrast and all estimates are contained in ordered CIs. The source uses `%` for HbA1c; it does not explicitly distinguish a percentage-point wording from a relative-percent-change wording, so the exact intended terminology remains a reporting-definition question, not a contradiction. Spline covariance and exact test definition are absent. No proposal.

### S013 — Medication proportion differences and test labels

**PASS_1_COMPLETE.** [DOC-001 PDF p. 4](../../../jama_aminian_2019_oi_190103.pdf#page=4) calls the longitudinal comparison a two-sample proportions test at 1, 2, 5, and 8 years; [DOC-001 PDF p. 10](../../../jama_aminian_2019_oi_190103.pdf#page=10) identifies the displayed 8-year Figure 5 P values as Fisher exact tests; [DOC-002 PDF p. 12](../../../joi190103supp1_prod.pdf#page=12) labels medication estimates as percentage-point differences and gives matching 8-year P values, including insulin `.008` and `<.001` for the other five rows. The generic two-sample-proportions description can encompass a Fisher exact comparison, so the supplied wording alone does not establish incompatible tests. All 8-year signs are surgery-minus-nonsurgery negative and agree with the figure’s lower surgery medication use. Exact denominators, test implementation, sidedness, and any P-value adjustment rule are not supplied; no test/CI calculation was inferred. No proposal.

### S014 — Primary-composite subgroup HRs and interaction P values

**PASS_1_COMPLETE.** Direct visual confirmation on [DOC-002 PDF p. 8](../../../joi190103supp1_prod.pdf#page=8) finds all 16 subgroup HRs within ordered 95% CIs, with every HR below 1 and direction labeled decreased risk. The eight interaction P values (.35, .93, .90, .80, .94, .53, .72, .98) are positioned and described as interaction tests, not P values for the individual subgroup HRs; they therefore cannot be mechanically compared to each individual HR CI. The caption supplies the replacement-covariate/interacted-Cox construction but not interaction coefficients, SEs, covariance, or degrees of freedom. No proposal.

### S015 — Proportional-hazards assumption results

**PASS_1_COMPLETE.** [DOC-001 PDF p. 6](../../../jama_aminian_2019_oi_190103.pdf#page=6) and [DOC-002 PDF p. 9](../../../joi190103supp1_prod.pdf#page=9) identify weighted-residual PH testing. eTable 6 labels final-column values `.89/.76/.63/.65/.24/.10/.46/.04` as PH-assumption P values, separate from outcome P values. The AF `.04` is thus not a duplicate or conflict with the AF outcome `P=.03`; it flags the named assumption test. Residual statistic, test distribution, and degrees of freedom are absent, so no numerical diagnostic is available. No proposal.

### S016 — Fifteen-dataset sensitivity analysis

**PASS_1_COMPLETE.** [DOC-001 PDF pp. 4 and 8-9](../../../jama_aminian_2019_oi_190103.pdf#page=4) and [DOC-002 PDF pp. 17-18](../../../joi190103supp1_prod.pdf#page=17) agree that five index-date assignments times three matching ratios form 15 datasets, each analyzed with fully adjusted Cox HRs/95% CIs. The counts of significant datasets (15 for five endpoints; 13/12/11 for cerebrovascular/coronary/AF) are internally coherent with a maximum of 15. eFigure 4 provides visual rather than exact tabulated HR/CI values, and the significance criterion/statistics for the 15 individual fits are not printed; no unsupported visual or P-value reconstruction was made. No proposal.

### S017 — Imputation methods and Rubin-formula SE context

**PASS_1_COMPLETE.** [DOC-001 PDF p. 4](../../../jama_aminian_2019_oi_190103.pdf#page=4) and [DOC-003 PDF p. 6](../../../joi190103supp2_prod.pdf#page=6) both state five imputed datasets, predictive mean matching/logistic/polytomous logistic methods by variable type, and Rubin-formula imputation-corrected SEs. These are matching analysis definitions, not a printed estimate/SE pair. No coefficient-level SE, between/within-imputation variance, degrees of freedom, or contrast definition is supplied, so no SE compatibility calculation applies. No proposal.

### S018 — Two-sided alpha, CIs, and multiplicity context

**PASS_1_COMPLETE.** [DOC-001 PDF p. 4](../../../jama_aminian_2019_oi_190103.pdf#page=4) and [DOC-003 PDF p. 6](../../../joi190103supp2_prod.pdf#page=6) agree on two-sided alpha .05 and 95% CIs where applicable, with secondary-endpoint analyses exploratory because no multiplicity adjustment was performed. This does not state a universal adjusted-P/CI relationship, and no contrary label occurs in the matched overall-Cox results. No proposal.

### S019 — Cause-specific rates and rate differences

**PASS_1_COMPLETE.** [DOC-002 PDF p. 6](../../../joi190103supp1_prod.pdf#page=6) labels values as rates per 100 patient-years, with nonsurgical-minus-surgery differences and 95% 1,000-sample bootstrap CIs; [DOC-003 PDF p. 6](../../../joi190103supp2_prod.pdf#page=6) supplies the matching planned measure. Printed arithmetic reconciles at displayed precision for all eight endpoints (for example, 7.45 - 4.51 = 2.94; 3.64 - 2.11 = 1.53; 1.77 - 1.14 = .63). Difference estimates are within ordered endpoints and positive direction agrees with the labeled contrast. Parenthetical individual-outcome values are expressly composite death-with-outcome rates, not second treatment rates. Person-time and bootstrap inputs are absent. No proposal.

### S020 — Cumulative-incidence estimates by endpoint/time/treatment

**PASS_1_COMPLETE.** [DOC-002 PDF p. 7](../../../joi190103supp1_prod.pdf#page=7) prints every surgery/nonsurgery cumulative-incidence point estimate within ordered 95% CI endpoints for eight outcomes at years 2, 5, and 8. The matched 8-year values and intervals agree with [DOC-001 PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7) after matching endpoint and treatment group. The table uses Kaplan-Meier estimates but does not supply risk sets/censoring details at every endpoint/time or variance estimator inputs; no recalculation was attempted. No proposal.

### S021 — Time-varying adjusted HRs and duplicate equality

**PASS_1_COMPLETE.** [DOC-002 PDF pp. 10 and 19](../../../joi190103supp1_prod.pdf#page=10) contain identical 24 endpoint-by-time HR/95% CI pairs. Every point estimate is within ordered endpoints; intervals crossing 1 at the applicable times are not mislabeled as fixed-direction significance claims. The table correctly identifies fully adjusted Cox models with the treatment term replaced by an observed-follow-up restricted-cubic-spline interaction. Coefficient covariance, spline knots/basis details beyond the label, and time-specific test statistics are absent. The separate erroneous eTable reference is proposed under S024, not duplicated here. No further proposal.

### S022 — Surgery-only intervention cumulative incidences

**PASS_1_COMPLETE.** [DOC-002 PDF p. 15](../../../joi190103supp1_prod.pdf#page=15) identifies eTable 11 as Kaplan-Meier cumulative incidences after metabolic surgery only. All 24 printed point estimates lie within ordered 95% CIs and the surgery-only population/time label is explicit; no nonsurgery contrast is claimed. Exact risk sets, censoring, and variance inputs are not printed. No proposal.

### S023 — E-values on the risk-ratio scale

**PASS_1_COMPLETE.** [DOC-002 PDF pp. 19-20](../../../joi190103supp1_prod.pdf#page=19) and [DOC-003 PDF p. 7](../../../joi190103supp2_prod.pdf#page=7) consistently define the E-value on the risk-ratio scale for each HR estimate and the 95% CI limit closest to the null. Each of the eight endpoint pairs identifies an E-value for the estimate and one for the closest-to-null CI limit, and the primary narrative reproduces the matching primary HR 0.61 (0.55-0.69), E-values 2.15/1.92. The source does not state the HR-to-risk-ratio conversion, outcome-risk inputs, or computational formula used; a formula-based diagnostic would therefore require unsupported assumptions and was not made. The risk-factor HRs are expressly comparison-of-magnitude values, not values expected to equal E-values. No proposal.

### S024 — Time-varying-HR cross-reference label

**PASS_1_COMPLETE.** [DOC-002 PDF p. 19](../../../joi190103supp1_prod.pdf#page=19) states that eTable 4 displays time-varying adjusted HRs/95% CIs but immediately presents a table headed eTable 7. The same 24-cell table is headed eTable 7 on [DOC-002 PDF p. 10](../../../joi190103supp1_prod.pdf#page=10). This is an exact supplied-source label contradiction, independent of any unreported inferential detail. **Temporary proposal emitted: STAT1-P001.**

### S025 — Complete eTable 8 estimates, signs, units, CIs, and P values

**PASS_1_COMPLETE.** [DOC-002 PDF p. 12](../../../joi190103supp1_prod.pdf#page=12) was checked across metabolic, nutritional, and medication rows at all four times. All printed estimates lie within ordered 98.8% Bonferroni CIs. Signs accord with stated surgery-versus-nonsurgery changes and units are consistently shown (lb/kg, HbA1c %, g/dL, ug/L, or medication percentage points). The 8-year weight and HbA1c rows match their appropriately contrast-aligned main-article summaries. The table explicitly identifies the spline for continuous variables and two-sample proportions tests for medication rows. It does not say whether displayed P values received the same Bonferroni adjustment as the CIs; consequently an unadjusted P (for example other antihypertensive medication at year 1, `.02`) alongside a 98.8% CI containing zero is not a source-established incompatibility. No adjusted-P/CI compatibility calculation was inferred. No proposal.

## Pass-1 summary and limitations

- **Coverage:** 25/25 assigned S IDs have an explicit `PASS_1_COMPLETE` record.
- **Temporary proposals:** 1 (`STAT1-P001`); no stable candidate ID was assigned.
- **No display-zero candidate:** no display-zero P value occurred in scope.
- **Principal limitations:** the supplied PDFs omit coefficient-level SEs, test statistics, degrees of freedom, covariance/variance estimators, bootstrap samples, individual person-time/risk-set inputs for all displayed time points, exact P values behind threshold displays, and some multiplicity/test-implementation details. These omissions prevented only the named compatibility calculations; they do not erase the direct checks completed above.
