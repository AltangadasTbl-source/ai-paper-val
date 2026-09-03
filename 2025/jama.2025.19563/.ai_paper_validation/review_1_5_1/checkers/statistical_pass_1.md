# Statistical Consistency Review — Pass 1

## Execution and scope

- **Stage:** mandatory independent statistical consistency pass 1.
- **Reviewer runtime ID:** `/root/statistical_pass_1`.
- **Scope:** every canonical inferential relationship, S001-S034, in `statistics/relationship_inventory.md`.
- **Authority:** direct supplied PDFs. Current 1.5.1 extraction/mapping artifacts were used only to locate evidence. No legacy candidate, checker, verifier, critic, or report was used as scientific input.
- **Checks applied where source definitions allowed:** interval-endpoint ordering and estimate containment; arithmetic/sign/direction; measure, scale, label, population, and timepoint matching; repeated/cross-location values; and P value/test/statistic compatibility only when the direct source supplied the necessary test/model definition. A one-sided bound was not treated as a two-sided interval.
- **Display-zero control:** no relationship in this assigned inventory displayed `P = 0`, `p = 0.000`, or equivalent. `DISPLAY_ZERO_NOT_CANDIDATE` was therefore not applicable.

## Provisional qualifying candidates

These are quality-control candidates only. They are not severity, validity, verification, rejection, correction, or adjudication decisions; each remains pending human adjudication.

### STAT1-CAND-001 — MICE sensitivity table: printed risk-difference sign/arithmetic does not match its printed pooled arm percentages

- **Relationships:** S019 and S031 (method and reported MICE sensitivity).
- **Direct evidence:** `joi250084supp2_prod_1765403089.61751.pdf#page=59`, eTable 16. The row headed “Primary Outcome: Diabetes Risk Reduction at 12 mo. (Pooled)” prints AI-DPP 32.2 and Human-Coach-DPP 31.9 under “% achieving outcome (MI-pooled),” but prints risk difference `-1.1 (-11.5)` percentage points.
- **Rule and diagnostic:** for the displayed AI-minus-human contrast, the two displayed one-decimal percentages imply approximately `+0.3` percentage points, not `-1.1`. Ordinary one-decimal rounding cannot reverse the sign: values displayed as 32.2 and 31.9 give a difference bounded approximately from +0.1 to +0.5 percentage points. This is a diagnostic arithmetic/sign comparison of the printed values, not a reconstructed CI or P value.
- **Exact human question:** Does the risk-difference cell use an adjusted or otherwise differently standardized estimand that is not identified in the table, or is one of the displayed pooled percentages/contrast values inconsistent? The supplied table header does not state an adjustment or alternate contrast that would reconcile the sign.

### STAT1-CAND-002 — Prohibited-medication proportion table labels its P value as Wilcoxon rank-sum although its supplied method specifies chi-squared

- **Relationships:** S018 and S028 (eTable 10 method and reported comparison).
- **Direct evidence:** `joi250084supp2_prod_1765403089.61751.pdf#page=29` says eTable 10 reports a proportion by assigned group and that a “Chi-squared test [was] used for comparison between study groups.” `joi250084supp2_prod_1765403089.61751.pdf#page=52`, eTable 10b, prints AI `6/183 (3.3%)`, Human `7/185 (3.8%)`, `P = 0.793`, with footnote `Wilcoxon Rank Sum Test`.
- **Rule:** the same supplied analysis material assigns a chi-squared test to the binary proportion comparison, whereas the result table labels its P value Wilcoxon rank-sum. The issue is the incompatible printed test label, not a newly calculated P value.
- **Exact human question:** Which test generated the displayed `P = 0.793`, and should the eTable 10b footnote or the supplied eTable 10 method description be changed to identify it consistently?

### STAT1-CAND-003 — Completer/dropout baseline-table footnote pairs a no-significance statement with `p<0.05`

- **Relationship:** S026.
- **Direct evidence:** `joi250084supp2_prod_1765403089.61751.pdf#page=47`, eTable 7 footnote 1, states: “No baseline characteristics were statistically significant different between groups (p<0.05).” The same page’s footnote 2 uses the conventional positive comparator for a different statement: age differed with `p = 0.014`; all other baseline characteristics were similar with `p > 0.05`.
- **Rule:** the printed `p<0.05` criterion attached to “No ... statistically significant” conflicts with the page’s own significance-direction wording and produces an internally ambiguous conclusion. No unprinted P value is inferred.
- **Exact human question:** Is the less-than comparator in eTable 7 footnote 1 a transcription/labeling error, or does it have a stated meaning different from the comparator used in footnote 2?

## Relationship-level pass-1 record

| Stable ID | PASS_1_COMPLETE result | Direct evidence checked and limitation/diagnostic note |
|---|---|---|
| S001 | NO_CANDIDATE | Main p. 1/4: ITT, AI-minus-human RD, one-sided 95% lower-bound and -15 pp rule are mutually labeled consistently. |
| S002 | NO_CANDIDATE | Main p. 4: 138 per arm x 2 = 276; 25% attrition converts to 184 per arm/368. Formula/variance convention not supplied, so power was not reconstructed. |
| S003 | NO_CANDIDATE | Main p. 4: analysis and sensitivity families are definitions; no incompatible observed coefficient/test was printed in this relationship. |
| S004 | NO_CANDIDATE | Main pp. 1/4/7: 58/183 versus 59/185 gives approximately -0.2 pp; lower bound -8.2 remains above -15 pp under the stated one-sided rule. |
| S005 | NO_CANDIDATE | Main p. 7 Figure 2 explicitly labels component one-sided bounds descriptive and no multiplicity adjustment; no conflicting formal-test assertion found. |
| S006 | NO_CANDIDATE | Main p. 4: initiation/completion directions agree with 171/183 versus 153/185 and 117/183 versus 93/185; chi-square family and printed P values are compatible at display precision. |
| S007 | NO_CANDIDATE | Main p. 4 and supplement p. 56: 8/183 and 7/185 correspond to 4.4% and 3.8%; `P=.78` is not contradicted by supplied counts/model label. |
| S008 | NO_CANDIDATE_MISSING_DEFINITION | Protocol pp. 6/15-16 defines the planned binary endpoint/noninferiority objective, but this slice does not supply margin/CI/test/population details. No unsupported inference made. |
| S009 | NO_CANDIDATE_MISSING_DEFINITION | Protocol pp. 36-37 confirms 15 pp relation, 50% assumption, 276 analyzable/368 target, 80%/5%; exact formula and CI convention remain insufficient for recalculation. Its one-sided CI wording is not inconsistent with the published noninferiority frame. |
| S010 | NO_CANDIDATE_MISSING_DEFINITION | Protocol pp. 37-39 specifies planned logistic/linear/mixed models and populations but no observed coefficient, interval, statistic, or P value. |
| S011 | NO_CANDIDATE | Protocol pp. 38-39 gives a conditional PA-missingness rule; it is not an observed inferential result and no contradiction was located. |
| S012 | NO_CANDIDATE_MISSING_DEFINITION | Protocol p. 39 defines a 3% discounted Markov/QALY/ICER plan; no observed economic result or uncertainty estimate is supplied. |
| S013 | NO_CANDIDATE_MISSING_DEFINITION | Supplement p. 8 gives an A1C device-discordance threshold outside a 95% CI but no estimate, CI endpoints, statistic, or P value to test. |
| S014 | NO_CANDIDATE | Supplement p. 28 and p. 34: age-adjusted RD is explicitly a distinct estimand from raw percentages; its one-sided bound and -15 pp label are coherent. |
| S015 | NO_CANDIDATE | Supplement pp. 28/35: subgroup RDs, AI-minus-human direction, one-sided bounds, exploratory/no-multiplicity status, and -15 pp line are explicitly supplied; raw subgroup values agree with displayed directions at rounding precision. |
| S016 | NO_CANDIDATE | Supplement p. 29 describes chi-squared for proportions and Wilcoxon rank-sum for continuous eTable 4 measures; no result-table contradiction was located for this relationship. |
| S017 | NO_CANDIDATE | Supplement pp. 29/51: p=.016 is attached to the stated 12-month outside-window days comparison; proportions and continuous-measure test families are separately defined. No compatible variance/test details justify further recalculation. |
| S018 | CANDIDATE: STAT1-CAND-002 | Supplement p. 29 assigns chi-squared to eTable 10’s proportion comparison; p. 52 labels the displayed P value Wilcoxon rank-sum. |
| S019 | CANDIDATE: STAT1-CAND-001 | Supplement p. 30 supplies the 20-set MICE/Rubin rule; p. 59’s printed pooled percentages and RD have the recorded sign/arithmetic mismatch. |
| S020 | NO_CANDIDATE | Supplement p. 34 age-adjusted primary/component RDs have correct stated scale/direction; departures from raw proportions are expected for the explicitly age-adjusted estimand. |
| S021 | NO_CANDIDATE | Supplement p. 35 eFigure 4 subgroup RDs agree in direction and ordinary rounding with displayed counts; bounds are one-sided and correctly not treated as two-sided intervals. |
| S022 | NO_CANDIDATE | Supplement pp. 39-40 age `p=.014` and all-other-characteristics `p>.05` agree with the printed matched main-table statement at its coarser `.01` precision. |
| S023 | NO_CANDIDATE_MISSING_DEFINITION | Supplement p. 41 says no significant eligibility differences but supplies no test/statistic/exact P; no source-grounded incompatibility is observable. |
| S024 | NO_CANDIDATE | Supplement pp. 42-43 separates site-comparison P values from the repeated randomized-arm footnote; matched populations/comparators differ, so values are not treated as duplicates. |
| S025 | NO_CANDIDATE | Supplement pp. 44-45 baseline-A1C strata have site/ethnicity P values and `p>.05` for the remainder; no same-comparator repetition conflicts. |
| S026 | CANDIDATE: STAT1-CAND-003 | Supplement p. 47 eTable 7 footnote attaches `p<0.05` to a no-significance statement while footnote 2 uses `p>.05` for similarity. |
| S027 | NO_CANDIDATE | Supplement p. 51 attendance/outside-window values, windows, P=.016, and `p>.05` statements have no direct internal conflict; test details beyond the stated family are not inferred. |
| S028 | CANDIDATE: STAT1-CAND-002 | Supplement p. 52 eTable 10b’s binary arm proportions and `P=.793` carry the Wilcoxon footnote conflicting with the p. 29 eTable 10 chi-squared method. |
| S029 | NO_CANDIDATE | Supplement pp. 53-54 per-protocol baseline age/sex P values are tied to a distinct complete/no-prohibited-medication population; no same-result mismatch found. |
| S030 | NO_CANDIDATE | Supplement p. 58 per-protocol count-derived RDs agree in sign and displayed precision with their one-sided lower bounds; population and baseline-A1C restriction are labeled. |
| S031 | CANDIDATE: STAT1-CAND-001 | Supplement p. 59 MI-pooled arm percentages 32.2/31.9 conflict in sign with the printed AI-minus-human RD -1.1, subject to the stated adjudication question. |
| S032 | NO_CANDIDATE | Supplement p. 60: 58/183 (31.7%) minus 70/185 (37.8%) is -6.1 pp at displayed precision; lower bound -14.3 and stated pattern-mixture assumption are coherent. |
| S033 | NO_CANDIDATE | Supplement p. 61: 58/183 (31.7%) minus 60/185 (32.4%) is approximately -0.74 pp, agreeing with each table’s one-sided bound and stated scenario. |
| S034 | NO_CANDIDATE | Supplement p. 62: raw 31.7% minus 31.9% agrees with RD -0.20; distinct cluster rules explain distinct one-sided lower bounds -4.8/-6.8. |

## Pass-1 summary and limitations

- **Relationships completed:** 34/34 (S001-S034), each explicitly marked `PASS_1_COMPLETE` in the table above.
- **Distinct provisional candidates:** 3 (`STAT1-CAND-001` through `STAT1-CAND-003`). Candidate 1 spans S019/S031 and candidate 2 spans S018/S028; this preserves all relationship provenance without duplicating the same printed contradiction.
- **Direct pages visually confirmed for candidates:** DOC-003 PDF pp. 29, 47, 52, and 59.
- **Limitations:** planned protocol relationships lack formulas, estimands, or observed statistics in several cases; no sidedness, degrees of freedom, variance estimator, covariance, multiplicity, or adjustment was inferred where not supplied. The MICE-table comparison is explicitly a displayed-value diagnostic and leaves the table’s unreported estimand/adjustment as the human question.

`PASS_1_COMPLETE`
