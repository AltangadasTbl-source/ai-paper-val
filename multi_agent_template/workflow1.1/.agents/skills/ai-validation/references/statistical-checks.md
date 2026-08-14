# Statistical consistency checks

The statistical lane is mandatory, exhaustive over result-relevant reported relationships, and never displaced by candidates from other lanes.

## Required coverage matrix

Create `audit/statistics/coverage_matrix.md`. Use one row per distinct reported inferential relationship, identified by outcome, population, time point, contrast, adjustment/model label, and source location. Record:

- point estimate and scale;
- confidence/credible interval and level;
- P value and stated null, test, sidedness, or multiplicity convention when supplied;
- test statistic, standard error, degrees of freedom, and event counts when supplied;
- matching occurrences in abstract, text, table, figure, and supplement;
- checks performed;
- inputs unavailable for a valid check;
- candidate IDs produced, if any.

Do not sample only primary outcomes or significant rows. If a table is too large to check completely, state the uncovered rows explicitly; never imply complete coverage.

## First-pass checks

Perform every applicable document-grounded check:

1. Endpoint ordering and containment of the displayed point estimate.
2. Direction/sign agreement among estimate, interval, labels, narrative wording, and graph.
3. Compatibility of interval exclusion/inclusion of the stated null with the displayed P-value threshold, but only when the source establishes compatible estimand, test, sidedness, variance estimator, confidence level, and adjustment convention.
4. Exact and near-exact repetition of estimates, intervals, P values, standard errors, test statistics, or whole rows where distinct rows are expected.
5. Agreement across abstract, results text, tables, figures, captions, and supplements after matching population, time point, contrast, units, scale, model, and displayed precision.
6. Agreement between effect measure and event/count direction when the printed inputs make the relationship determinate.
7. Confidence interval, standard error, test statistic, and P-value relationships when the reported method supplies a valid formula.
8. Percentages, denominators, missingness, analysis populations, and subgroup labels that change the meaning of an inferential result.
9. Inequality symbols, decimal places, scientific notation, negative signs, swapped endpoints, impossible bounds, and unit/scale conversions.
10. Narrative claims such as increase/decrease, benefit/harm, significant/non-significant, or interaction/subgroup differences against the exact displayed result they cite.

Treat medians, means, adjusted estimates, unadjusted estimates, within-group tests, between-group tests, interaction tests, and change scores as different quantities unless the source explicitly equates them.

## Diagnostic calculations

Show inputs, rule, calculation, output, units, and rounding tolerance. Label an approximation diagnostic when exact model details are missing. Never replace the reported model with a normal approximation and present the approximation as authoritative.

Do not assume that a P value tests a zero coefficient or that a P value and confidence interval use the same test. Do not infer degrees of freedom, covariance structure, variance estimator, multiplicity adjustment, or analytic denominator from convention alone.

## Second reconciliation pass

After the complete candidate registry and evidence-recheck file exist:

1. Compare every statistical coverage row with all arithmetic, flow, cross-document, and presentation candidates.
2. Determine whether changed denominators, mislabeled rows, duplicated cells, flow discrepancies, or figure labels create additional statistical reporting candidates.
3. Reopen any method or footnote cited as defining the relevant statistical relationship.
4. Append new candidates; do not overwrite or renumber existing ones.
5. Update the coverage matrix with the second-pass result and candidate IDs.
6. Record every relationship that remains not mechanically checkable and the exact missing definition or model output a human would need.

The second pass is complete only when every coverage row has a recorded result. Candidate quantity elsewhere in the audit is never a reason to stop.
