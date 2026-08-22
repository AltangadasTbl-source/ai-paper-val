# Statistical Consistency Pass 1

## Scope, method, and boundary

- **Reviewer execution:** fresh statistical pass 1; `gpt-5.6-terra`, high effort; runtime agent ID `root/statistical_pass_1`.
- **Exact scope:** every canonical inferential relationship `S001` through `S017` in `statistics/relationship_inventory.md`.
- **Sources checked directly:** `jama_parsons_2020_oi_190140.pdf` (PDF pp. 1-9); `joi190140supp1_prod.pdf` (PDF pp. 2, 12-13, 15, 25, 28-29, 34, 38-42); `joi190140supp2_prod.pdf` (PDF pp. 1, 3-8, 10); and `joi190140supp3_prod.pdf` (PDF pp. 2-3). Native/layout text was used as a locator; main Table 2 (PDF p. 7) and Supplement 3 eTable (PDF p. 2) were visually confirmed from the direct PDFs.
- **Checks applied where defined:** estimate containment, endpoint order, sign/direction, effect measure and scale/reference labels, duplicate/cross-location repetition, and interval/P/test/statistic compatibility only where the source states a matching analysis definition. Planned designs were not treated as observed estimates.
- **Diagnostic convention:** normal-approximation calculations below use the displayed 95% interval as estimate +/- 1.96 SE after rounding. They are diagnostics only; they do not infer degrees of freedom, covariance, variance estimator, sidedness, or an unprinted model parameter.
- **Display-zero check:** no assigned source prints `P = 0`, `p = 0.000`, or an equivalent display zero. `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable.
- **Outcome:** 17/17 relationships completed; 5 candidate proposals, all pending human adjudication and without candidate IDs.

## Candidate proposals from this pass

### SP1-P01 — Age-stratification boundary differs between the main article and its final protocol/SAP material

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=2`; `joi190140supp1_prod.pdf#page=2`; `joi190140supp1_prod.pdf#page=40`; `joi190140supp2_prod.pdf#page=5`.
- **Direct observation:** The main article describes stratified randomization as age `<70 years vs >=70 years`. Supplement 1 PDF p. 2 says that this factor was corrected from `<70 years vs >=70 years` to `<=70 years vs >70 years`; Supplement 1 PDF p. 40 and the SAP’s adjusted-Cox definition on Supplement 2 PDF p. 5 use the latter boundary. The main article also says its supportive Cox model adjusted for the three stratification factors.
- **Rule:** The printed age boundary for the same randomization stratum/adjustment factor should agree after matching the protocol version and analysis population.
- **Diagnostic versus direct:** Direct, source-to-source definition comparison; no statistical calculation is used.
- **Human question:** Which boundary was implemented for randomization and the adjusted Cox analysis, and should the main article’s stratification wording be corrected or explicitly identified as describing a different version?

### SP1-P02 — 24-month energy between-group P value differs across the main Table 2 and eTable

**Later pass-2/recheck qualification:** This pass-1 proposal is retained as provenance. Direct recheck established that the main table prints the full contrast and interval, while the eTable prints the two component changes plus the labelled cross-group `†` P value; the displayed eTable components reproduce the main contrast by subtraction. Stable C009 uses that narrower comparator framing.

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`, Table 2, Energy, 24-month between-group difference; `joi190140supp3_prod.pdf#page=2`, eTable, Energy, 24-month `p-value†`.
- **Direct observation:** Both locations print the intervention-minus-control 24-month change as `-119.71` with 95% CI `-211.78 to -27.65` and define the comparison as changes in intervention compared with changes in control in a mixed-model analysis. The main table prints `P = .01`; the eTable prints `P < 0.001`.
- **Rule:** A matched estimate, interval, contrast, time point, and model-labelled P value should have one compatible printed P value across repeated source locations.
- **Diagnostic versus direct:** Direct contradiction is the two printed P values. Diagnostic only: the rounded interval gives SE about `46.97`, `|z|` about `2.55`, and a two-sided normal tail near `.011`, which is compatible with `.01` but not with `<.001`.
- **Human question:** Which P value is the intended mixed-model result for the 24-month energy change contrast?

### SP1-P03 — 24-month deep-yellow-vegetable between-group P value differs across the main Table 2 and eTable

**Later pass-2/recheck qualification:** This pass-1 proposal is retained as provenance. Direct recheck established that the main table prints the full contrast and interval, while the eTable prints component changes plus the labelled cross-group `†` P value and does not print the contrast/interval. The control component also differs by 0.01 and is separately registered as C013. Stable C010 uses the narrowed P-value comparator framing.

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`, Table 2, Deep yellow vegetables, 24-month between-group difference; `joi190140supp3_prod.pdf#page=2`, eTable, Deep yellow vegetables, 24-month `p-value†`.
- **Direct observation:** Both locations print the 24-month intervention-minus-control change as `0.14` with 95% CI `0.05 to 0.23`, with the same mixed-model/change-versus-change definition. The main table prints `P = .004`; the eTable prints `P = .003`.
- **Rule:** Repeated P values for the same matched result should agree to the stated display precision.
- **Diagnostic versus direct:** Direct contradiction is the printed `.004` versus `.003`. Diagnostic only: the rounded interval gives SE about `.046`, `z` about `3.05`, and a two-sided normal tail near `.0023`; rounding and unreported inferential details prevent this approximation from selecting a source value.
- **Human question:** Which rounded P value is intended for this 24-month change contrast?

### SP1-P04 — 12-month intervention red-meat within-group P value differs across the main Table 2 and eTable

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`, Table 2, Red meat, 12-month MEAL intervention-group change; `joi190140supp3_prod.pdf#page=2`, eTable, Red meat, 12-month intervention `p-value*`.
- **Direct observation:** Both locations print intervention mean change `-11.54 g/d` with 95% CI `-19.03 to -4.06`; both define `*` as within-group follow-up compared with baseline and state mixed-model P values. The main table prints `P = .003`; the eTable prints `P = .001`.
- **Rule:** Repeated P values for the same matched estimate, interval, arm, time point, and within-group contrast should agree to the stated display precision.
- **Diagnostic versus direct:** Direct contradiction is the printed `.003` versus `.001`. Diagnostic only: the rounded interval gives SE about `3.82`, `|z|` about `3.02`, and a two-sided normal tail near `.0025`; this cannot replace the reported mixed-model result.
- **Human question:** Which rounded P value is intended for the intervention arm’s 12-month red-meat change?

### SP1-P05 — 12-month control red-meat within-group P value differs across the main Table 2 and eTable

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`, Table 2, Red meat, 12-month control-group change; `joi190140supp3_prod.pdf#page=2`, eTable, Red meat, 12-month control `p-value*`.
- **Direct observation:** Both locations print control mean change `-9.83 g/d` with 95% CI `-17.26 to -2.41` and the same within-group/mixed-model P-value definition. The main table prints `P < .001`; the eTable prints `P = .01`.
- **Rule:** A matched repeated result should not be reported both as below `.001` and as `.01`.
- **Diagnostic versus direct:** Direct contradiction is the printed `<.001` versus `.01`. Diagnostic only: the rounded interval gives SE about `3.79`, `|z|` about `2.59`, and a two-sided normal tail near `.010`; the estimate does not establish the source’s exact variance or test computation.
- **Human question:** Which P value is the intended mixed-model result for the control arm’s 12-month red-meat change?

## Relationship-by-relationship completion record

### S001 — Primary composite TTP Cox/log-rank result

- **Direct check:** Main PDF pp. 1 and 5 report intervention-versus-control unadjusted HR `.96` (95% CI `.75-1.24`) and adjusted HR `.97` (`.76-1.25`); Figure 2A on p. 6 prints log-rank `P=.76`. Each HR is contained in its ascending interval, both directions are compatible with no clear intervention advantage, and the 24-month Kaplan-Meier difference `2.1%` (`-8.1% to 12.2%`) is contained in its ascending interval.
- **Compatibility limit:** The source distinguishes the log-rank test from Cox estimation, but does not state enough common inferential detail to reconstruct a Cox P value from an interval. No such reconstruction was used.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S002 — Biopsy-only TTP sensitivity

- **Direct check:** Main PDF p. 5 reports HR `1.40` (95% CI `.79-2.46`), `P=.24`, 49 events, and intervention-minus-control 24-month progression-free difference `-.3%` (`-7.3% to 6.7%`); Figure 2B (p. 6) repeats log-rank `P=.24`. Estimate containment, endpoint order, and directions agree after retaining this as a biopsy-only sensitivity analysis rather than the composite outcome.
- **Compatibility limit:** The direct source labels the figure P as log-rank; it does not establish that the displayed P is a Wald test for the Cox interval.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S003 — Initial sample-size design

- **Direct check:** Main PDF p. 3, Supplement 1 PDF p. 40, and Supplement 2 PDF p. 3 consistently describe a planned two-sided `.05` log-rank design, 418 eligible participants, at least 80% power, 57 events, and target enrollment 464 after a 10% dropout assumption. The 20% control versus 10% experimental progression assumptions and HR `2.1`/`2.118` are planning values, not observed risks. Supplement 1’s adaptive `HR=.472` is the reciprocal direction of the design HR and is explicitly tied to a reversed comparison orientation.
- **Compatibility limit:** Exact sample-size computations, alpha spending, and unrounded inputs are not supplied; no independent re-calculation was used to criticize rounded planning values.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S004 — Analysis populations and primary-model definitions

- **Direct check:** The main article defines Kaplan-Meier/log-rank/Cox analyses, three-factor adjustment, ITT support, proportional-hazards assessment (`P=.46`), biopsy-only sensitivity, and shared frailty. The main primary analysis population (443 after eligibility/pathology exclusions) is not conflated with ITT or the sensitivity analyses. The direct cross-source age-stratification mismatch is proposed in **SP1-P01**.
- **Compatibility limit:** The SAP’s modified-ITT wording and the reported primary set differ in operational exclusion detail, but the sources identify planned versus observed analysis contexts and do not supply a same-estimand numerical contradiction.
- **Status:** `PASS_1_COMPLETE` — proposal **SP1-P01**.

### S005 — Main repeated diet/carotenoid mixed-model framework and Table 2

- **Direct check:** Main PDF pp. 4 and 7 specify a linear mixed-effects model with diet group, categorical time, and group-by-time interaction; `c` P values are within-group follow-up versus baseline and `d` P values are intervention-change versus control-change. Across energy, vegetables, cruciferous measures, meats/fats, and carotenoids, all directly inspected point estimates are contained within ascending displayed intervals and have directions consistent with their labels. The printed intervals and P values are not used to infer unreported covariance or degrees of freedom.
- **Cross-location check:** Supplement 3 p. 2 uses the same mixed-model footnote and matched rows. Four non-nested P-value contradictions are proposed in **SP1-P02** through **SP1-P05**. Saturated-fat 12-month between-group reporting is `<.001` in the main table and `<.01` in the eTable: the bounds are non-identical but nested, so this is recorded as a coherent precision/display difference rather than a candidate proposal.
- **Status:** `PASS_1_COMPLETE` — proposals **SP1-P02**, **SP1-P03**, **SP1-P04**, **SP1-P05**.

### S006 — Active-treatment comparisons

- **Direct check:** Main PDF p. 5 reports 6/226 (`2.7%`) versus 4/217 (`1.8%`), Fisher exact `P=.75`, and time-to-treatment HR `1.38` (95% CI `.39-4.90`), `P=.61`. The HR is contained in an ascending interval; the proportion comparison and time-to-event comparison have separate supplied tests and are not treated as duplicates.
- **Compatibility limit:** The source does not supply the full time-to-treatment test-statistic/variance definition needed to derive a P value from the HR interval.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S007 — Plasma-carotenoid mixed-model contrast

- **Direct check:** Main PDF p. 6 reports baseline-to-12-month intervention-minus-control mean-change difference `.10` log-micromol/L (95% CI `.02-.18`), `P=.01`; the point estimate is inside an ascending positive interval and the scale is explicitly log-micromol/L. Diagnostic only: the rounded interval gives SE about `.041` and `z` about `2.45`, broadly compatible with a two-decimal `.01` display.
- **Compatibility limit:** Exact model covariance and P-value calculation are not printed.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S008 — MEAL pilot table P-value labels and total-carotenoid result

- **Direct check:** Supplement 1 PDF pp. 12-13 identifies the pilot as intervention `n=45` and control `n=23`; `dagger` denotes between-group `P<.05`, `double dagger` within-group `P<.05`, and narrative total-carotenoid comparison is `P=.02`. Directions of the marked intake/carotenoid changes agree with the stated arms and time period.
- **Compatibility limit:** The source does not state the pilot test, sidedness, model, or interval/SE definition. No P/interval reconstruction is applicable.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S009 — PSADT derivation and progression-analysis definitions

- **Direct check:** Main PDF p. 3 and Supplement 1 PDF pp. 28 and 41 use `log(2)` divided by the least-squares slope of log(PSA); the updated protocol explains the month-6/three-value start and later all-available-value rule. TTP log-rank/Cox, treatment censoring, and eligible/ITT distinctions are consistently labelled as definitions/plans rather than matched observed effects.
- **Compatibility limit:** Earlier protocol text’s “last three” PSA wording is versioned; it is not compared as an observed numeric result against the updated definition.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S010 — Planned primary and secondary endpoint/time-point definitions

- **Direct check:** Supplement 1 PDF pp. 15, 25, and 29 supplies the planned clinical-progression, active-treatment, anxiety/HRQOL, PSA, QOL, diet, and biomarker assessment contexts. No observed effect estimate, interval, P value, or test statistic is printed for this relationship.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S011 — Planned correlative-biomarker models

- **Direct check:** Supplement 1 PDF pp. 38-41 specifies the biomarker Cox/power context (`n=334`, log-HR/coefficient `.4`, 95% power, two-sided alpha `.05`, 85% two-year PFS) and planned allocation/interaction/gradient-lasso models. These are planned-model definitions, not results; their population, predictor, and adjustment labels are preserved.
- **Compatibility limit:** No observed marker coefficient, interval, P value, or variance estimate is supplied for comparison.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S012 — Planned QOL/diet longitudinal analyses

- **Direct check:** Supplement 1 PDF pp. 34 and 41 describes exploratory t-test/linear-regression and GEE/Bang-Jung-George plans; the SAP (Supplement 2 pp. 6-8) specifies later Wilcoxon rank-sum analyses by instrument/time point, no multiplicity adjustment for secondary/supportive analyses, and no longitudinal imputation. These are document-version planning specifications, not an observed same-test result.
- **Compatibility limit:** The package does not supply an amendment crosswalk or observed QOL result that would establish a concrete numerical or inferential inconsistency between plans.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S013 — Interim superiority/futility plan

- **Direct check:** Supplement 1 PDF p. 42 specifies one-sided interim alpha `.0025`, final alpha `.025`, 4-5 interims, and a futility rule of one-sided `P>=.5` or standardized log-rank statistic `<0`. The same text states that a one-sided P below `.5` with positive statistic indicates experimental-arm direction.
- **Compatibility limit:** The source supplies no observed interim statistic, alpha-spending function, or definition equating the directional `.5` statement with the rejection boundary. No sidedness or contradiction is inferred from convention.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S014 — Adaptive sample-size rule

- **Direct check:** Supplement 1 PDF p. 42 defines a control-PGR `<20%` recalculation with `HR=.472`, two-sided `.05`, 80% power, a maximum 20% increase, and the 18%/466-eligible example. Its HR direction is coherent with the reciprocal of the earlier 20%-versus-10% planning HR once the stated arm orientation is retained.
- **Compatibility limit:** Unrounded calculation inputs and the adaptive-event formula are not supplied; no re-calculation was substituted for the source plan.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S015 — SAP QOL inferential rules

- **Direct check:** Supplement 2 PDF pp. 7-8 states instrument-specific two-sided Wilcoxon rank-sum P values at baseline/6/12/18/24 months, primary alpha 5%, secondary/supportive individual 5% tests without multiplicity adjustment, 15% interaction threshold, and no exploratory imputation. Test, population, time, and scale labels are internally distinct.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S016 — SAP instrument scales and eFigure plotting definition

- **Direct check:** Supplement 2 PDF p. 10 gives the instrument ranges/transforms and favorable-direction statement; Supplement 3 PDF p. 3 defines boxplot quartiles, median, mean circle, and non-outlier whiskers. The eFigure prints no numerical inferential estimate, interval, P value, or test.
- **Status:** `PASS_1_COMPLETE` — no proposal.

### S017 — Supplement 3 eTable P-value semantics

- **Direct check:** Supplement 3 PDF p. 2 explicitly defines `*` as within-group follow-up versus baseline and `dagger` as intervention-change versus control-change, with P values from a mixed-model analysis. The eTable’s shared estimates/intervals, scales, and time points match the corresponding main Table 2 rows.
- **Cross-location check:** Its four non-nested P-value discrepancies with the main Table 2 are the direct observations in **SP1-P02** through **SP1-P05**. The nested saturated-fat thresholds are not a candidate as noted under S005.
- **Status:** `PASS_1_COMPLETE` — proposals **SP1-P02**, **SP1-P03**, **SP1-P04**, **SP1-P05**.

## Pass-1 handoff

- **Relationships covered:** 17 (`S001`-`S017`), each marked `PASS_1_COMPLETE` above.
- **Candidate proposals:** 5 (`SP1-P01`-`SP1-P05`); no stable `C` ID, severity, validity, disposition, or correction is assigned.
- **Limitations requiring later human review:** exact mixed-model covariance/test calculations are not printed; the package does not provide an amendment crosswalk for all planned-analysis wording; and interval-based normal approximations are diagnostic only.
- **Artifact:** `.ai_paper_validation/review_1_5_1/checkers/statistical_pass_1.md`.
