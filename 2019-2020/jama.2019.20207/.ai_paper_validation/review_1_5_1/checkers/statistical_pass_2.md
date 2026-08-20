# Statistical Consistency Pass 2

## Scope, execution, and method

- **Reviewer execution:** fresh, independent statistical pass 2; `gpt-5.6-terra`, high effort; runtime agent ID `root/statistical_pass_2`.
- **Exact scope:** every canonical inferential relationship `S001`; `S002`; `S003`; `S004`; `S005`; `S006`; `S007`; `S008`; `S009`; `S010`; `S011`; `S012`; `S013`; `S014`; `S015`; `S016`; and `S017` in `statistics/relationship_inventory.md`, plus the complete stable ledger `C001` through `C012` and `verification/evidence_recheck.md`.
- **Direct-source check:** native/layout extraction was used only to locate content. The supplied PDFs were revisited at the cited source pages: main article pp. 1-7; Supplement 1 pp. 2, 12-13, 15-16, 25, 28-29, 34, and 38-42; Supplement 2 pp. 1-10; and Supplement 3 pp. 2-3.
- **Applied checks:** denominator and displayed arithmetic; point-estimate containment and ordered interval endpoints; sign/direction; measure, unit, scale, contrast, and reference labels; repeated values and cross-location comparators; and interval/P/test/statistic/SE relations only where compatible definitions are supplied. Planned rules were not treated as observed results.
- **Inferential limit:** The package does not supply the unrounded mixed-model estimates, covariance matrix, contrast matrix, degrees of freedom, variance estimator, table-production version, or exact model test statistics for Table 2/eTable P values. No sidedness, covariance, denominator, model, or estimand mapping was inferred from convention. Any interval-based normal calculation below is explicitly a diagnostic only.
- **Display-zero check:** No assigned source displays `P = 0`, `p = 0.000`, or equivalent. `DISPLAY_ZERO_NOT_CANDIDATE` is not applicable.

## Ledger and mechanical-recheck implications

| Stable candidate | Statistical relationship implication | Pass-2 source-comparator record |
|---|---|---|
| C001 | S004 | **Directly supported.** The article's randomization boundary `<70`/`>=70` and the Update-10/final-protocol/SAP boundary `<=70`/`>70` assign exactly age 70 differently. The actual randomization-system and adjusted-Cox encoding remain unavailable. |
| C002 | No linked S ID | Reviewed as a cross-lane population-definition implication. Its exact eligibility comparators are printed; governing participant-level protocol version remains unavailable. |
| C003 | S009 | **Needs narrower framing.** The exact cited progression-endpoint comparators in the article, protocol p. 31, and SAP p. 2 all use `<70`/`>=70`; the `<=70`/`>70` SAP text on p. 1 is an eligibility definition, not the endpoint comparator. The claimed opposite endpoint assignment is not directly supplied. No event-level classifications or endpoint code are supplied. |
| C004 | No linked S ID | Reviewed as a cross-lane schedule implication. The 16-versus-17-month statements are directly printed; phase start/end and inclusive-boundary definitions are unavailable. |
| C005 | No linked S ID | Reviewed as a denominator implication. The arithmetic from the immediately linked arm totals is directly reproducible; the percentage denominators are not supplied. |
| C006 | No linked S ID | Reviewed as a distribution/denominator implication. The printed Table 1 rows leave stated remainders; whether the displayed distribution was intended to be partial is not supplied. |
| C007 | No linked S ID | Reviewed as a measure-label implication. The narrative values and intervals map directly to the `g/d` row, distinct from the printed servings/day row. |
| C008 | S008 | **Directly supported with missing denominator definition.** The pilot total is 74 and the table headers are 45 plus 23; the source does not state whether the table is a paired/evaluable subset. |
| C009 | S005; S017 | **Needs narrower framing.** Main Table 2 prints the 24-month energy change contrast `-119.71` (95% CI `-211.78 to -27.65`), `P=.01`; the eTable prints matching components `-250.01` and `-130.3`, whose displayed subtraction reproduces `-119.71`, and prints cross-group `P<.001`. The eTable does not itself print the contrast estimate or interval. The direct comparator is therefore the labelled cross-group P value plus displayed components, not an identically printed full contrast/interval. |
| C010 | S005; S017 | **Needs narrower framing.** Main Table 2 prints a 24-month deep-yellow-vegetable control change `0.05`, contrast `0.14` (95% CI `0.05 to 0.23`), `P=.004`; the eTable prints control change `0.06` and cross-group `P=.003`, but no contrast estimate/interval. The P comparison is direct under the same labelled cross-group semantics, while the component difference is separately recorded below. |
| C011 | S005; S017 | **Directly supported.** Both tables print intervention 12-month red-meat change `-11.54` (95% CI `-19.03 to -4.06`) and same within-group/mixed-model semantics, paired with `.003` and `.001`. Exact test-output inputs are unavailable. |
| C012 | S005; S017 | **Directly supported.** Both tables print control 12-month red-meat change `-9.83` (95% CI `-17.26 to -2.41`) and same within-group/mixed-model semantics, paired with `<.001` and `.01`. Exact test-output inputs are unavailable. |

## New pass-2 candidate proposal (no stable C identifier assigned)

### SP2-P01 — Deep-yellow-vegetable 24-month control mean change differs between the main table and eTable

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** `jama_parsons_2020_oi_190140.pdf#page=7`, Table 2, Deep yellow vegetables, control 24-month change; `joi190140supp3_prod.pdf#page=2`, eTable, Deep yellow vegetables, control 24-month change.
- **Direct observation:** Main Table 2 prints control 24-month change `0.05` servings/d (95% CI, `-0.02 to 0.11`). The eTable prints `0.06` servings/day with the same displayed interval `(-0.02, 0.11)` for the same labelled control, measure, and time point.
- **Consistency rule:** A repeated same-arm, same-time, same-measure estimate should agree at its stated two-decimal display precision unless a separate population, model, or production output is identified.
- **Direct versus diagnostic:** This is a direct printed-value comparison; no inferential reconstruction is used. The difference is `0.06 - 0.05 = 0.01` servings/day.
- **Missing inputs:** The package does not provide the unrounded means, model output, analysis data set/version, or a statement that these table rows intentionally use different outputs. Those missing items could explain how two separately rounded values arose but do not identify a printed distinction.
- **Human question:** Which displayed control 24-month change, `0.05` or `0.06` servings/day, was intended for the repeated deep-yellow-vegetable result, and does it correspond to the cross-group result reported beside it?

## Relationship-by-relationship pass-2 completion

### S001 — Primary composite TTP Cox/log-rank result

- **Recheck:** Unadjusted HR `.96` (95% CI `.75-1.24`) and adjusted HR `.97` (`.76-1.25`) remain contained in ascending intervals. Their directions, the `P=.76` log-rank figure label, and the 24-month Kaplan-Meier difference `2.1%` (`-8.1% to 12.2%`) remain internally and cross-location compatible when log-rank and Cox outputs are not conflated.
- **Compatibility limit:** No common Cox test statistic/variance definition is printed for a P-value reconstruction.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S002 — Biopsy-only TTP sensitivity

- **Recheck:** HR `1.40` (95% CI `.79-2.46`), `P=.24`, 49 events, and 24-month difference `-.3%` (`-7.3% to 6.7%`) have ordered intervals, correct containment, and compatible biopsy-only direction. Figure 2B repeats the log-rank `P=.24`.
- **Compatibility limit:** The figure P is labelled log-rank, not a stated Wald P for the Cox interval.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S003 — Initial sample-size design

- **Recheck:** The main article, protocol, and SAP retain the same planned two-sided `.05`, 418 eligible participants, at least 80% power, 57 events, and 464-target context. HR `2.1`/`2.118` is compatible displayed precision; adaptive `HR=.472` is its reciprocal under the stated reversed planning orientation.
- **Compatibility limit:** No unrounded event/sample-size calculation or alpha-spending formula is supplied.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S004 — Analysis populations and primary-model definitions

- **Recheck:** Kaplan-Meier, log-rank, Cox, three-stratum adjustment, proportional-hazards check, ITT support, biopsy-only sensitivity, and frailty analysis remain distinguishable rather than duplicate results. C001's age-boundary comparator remains directly printed; implementation inputs are missing as recorded above.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S005 — Repeated diet/carotenoid mixed-model framework and Table 2

- **Recheck:** The article and eTable explicitly label a mixed-model analysis and distinguish within-group (`*`/`c`) from intervention-change versus control-change (`†`/`d`) P values. Directly inspected point estimates remain inside ascending intervals and their signs agree with labelled changes. C009-C012 retain the revised source-comparator framing above. The 12-month saturated-fat cross-group displays `<.001` in the main table and `<.01` in the eTable; these nested threshold displays do not independently establish a contradiction. 
- **New implication:** The separately printed deep-yellow-vegetable 24-month control component is `0.05` versus `0.06`; this is SP2-P01, not a duplicate of the P-value comparator in C010.
- **Compatibility limit:** No covariance, degrees of freedom, contrast matrix, or matched model-output definition permits interval/P compatibility to decide an intended P value.
- **Status:** `PASS_2_COMPLETE` — new proposal `SP2-P01`.

### S006 — Active-treatment comparisons

- **Recheck:** The 6/226 (`2.7%`) versus 4/217 (`1.8%`) Fisher exact `P=.75` and time-to-treatment HR `1.38` (95% CI `.39-4.90`), `P=.61`, are distinct supplied analyses. The HR is contained within ordered endpoints; no rate/count label is confused.
- **Compatibility limit:** The time-to-treatment test statistic and variance definition are absent.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S007 — Plasma-carotenoid mixed-model contrast

- **Recheck:** Difference `.10` log-micromol/L (95% CI `.02-.18`), `P=.01`, retains positive containment and the printed log-micromol/L scale. A diagnostic normal approximation from rounded endpoints is broadly compatible but cannot identify the model P value.
- **Compatibility limit:** Covariance and exact mixed-model output are absent.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S008 — MEAL pilot P-value definitions and total-carotenoid result

- **Recheck:** Pilot `n=45`/`n=23` table labels, `*`/`†` significance semantics, and narrative total-carotenoid `P=.02` remain source-specific. C008 records the separate 74-versus-68 population-total comparator with its absent evaluability denominator; no test/statistic compatibility rule is supplied for the pilot P values.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S009 — PSADT and progression-analysis definitions

- **Recheck:** The log(2)/least-squares-slope PSADT formulation, censoring, eligible/ITT contexts, and updated all-available-value rule remain definition-aware. Recheck of C003 shows that the cited progression endpoint statements use `<70`/`>=70` consistently; the contrary `<=70`/`>70` text is an eligibility definition. No event-level endpoint code is supplied.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S010 — Planned endpoint and time-point definitions

- **Recheck:** Planned clinical, active-treatment, anxiety/QOL, PSA, diet, and biomarker endpoint/time-point definitions are not printed observed estimates. No matched statistical comparator is supplied.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S011 — Planned correlative-biomarker models

- **Recheck:** The protocol's Cox/power/allocation/interaction/lasso and carotenoid t-test/regression/Cox descriptions are planned-model definitions, without a duplicate observed marker estimate, interval, statistic, or P value.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S012 — Planned QOL/diet longitudinal analyses

- **Recheck:** Protocol t-test/linear-regression/GEE/Bang-Jung-George language and later SAP Wilcoxon/no-imputation language are versioned plans, not a matched observed same-test result. The package has no amendment crosswalk or observed QOL comparator.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S013 — Interim superiority/futility plan

- **Recheck:** One-sided interim alpha `.0025`, final `.025`, 4-5 interims, and futility one-sided `P>=.5` or statistic `<0` are separate defined decision rules. No observed interim statistic or alpha-spending function supports further compatibility testing.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S014 — Adaptive sample-size rule

- **Recheck:** The control-PGR `<20%` rule, `HR=.472`, two-sided `.05`, 80% power, maximum 20% increase, and 18%/466 example are coherently labelled as a planning recalculation. No unrounded formula inputs are supplied.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S015 — SAP QOL inferential rules

- **Recheck:** Instrument-specific two-sided Wilcoxon rank-sum tests, time points, 5% individual tests without multiplicity adjustment, 15% interaction threshold, and missing-data rule remain labelled planned QOL analyses. No realized QOL statistic is supplied for comparison.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S016 — SAP scales and eFigure plotting definition

- **Recheck:** The SAP's instrument ranges/transforms/favourable direction and the eFigure's boxplot definition concern separately labelled outputs. The eFigure prints no numerical estimate, interval, P value, or test statistic.
- **Status:** `PASS_2_COMPLETE` — no new proposal.

### S017 — eTable P-value semantics

- **Recheck:** The eTable directly defines `*` as within-group follow-up versus baseline and `†` as intervention-change versus control-change under a mixed-model analysis. This supports matching the P-value columns by contrast; it does not make the eTable print a contrast estimate/interval that it omits. C009-C012 and SP2-P01 are recorded without inferring unreported model details.
- **Status:** `PASS_2_COMPLETE` — new proposal `SP2-P01` cross-referenced through S005.

## Compact completion record

- **Relationships revisited:** 17/17 (`S001` through `S017`); every record is explicitly `PASS_2_COMPLETE`.
- **Stable ledger reviewed:** 12/12 (`C001` through `C012`), with C003, C009, and C010 given source-comparator-specific pass-2 records.
- **New candidate proposals:** 1 (`SP2-P01`), deliberately without a stable `C` ID.
- **Limitations:** no unrounded mixed-model output, test statistics, covariance/variance estimator, degrees of freedom, analytic-version record, randomization-system record, event-level endpoint coding, or pilot evaluability denominator is supplied. These missing definitions are not filled by convention.
- **Artifact:** `.ai_paper_validation/review_1_5_1/checkers/statistical_pass_2.md`.
