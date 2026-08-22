# Workflow 1.5 Quantitative Quality-Control Scope

This document is normative for both workflow 1.5 profiles.

## Review objective

Detect reproducible reporting-consistency candidates in the supplied paper package and prepare them
for human adjudication. The workflow is a quality-control and proofreading aid. It is not an attempt
to expose serious defects, judge authors, or declare a paper invalid.

Many useful candidates will be small and may not alter the paper's conclusions. Their value is still
real: preventable numeric or labeling defects can be copied into data extraction, systematic reviews,
meta-analyses, guidelines, or later publications. Describe this as bounded downstream evidence-chain
risk, not as an assumed downstream effect.

## Primary target categories

Use exactly one of these primary categories when applicable:

1. `Numeric or arithmetic inconsistency`
   - conflicting values, impossible ordering, transcription differences, row/column totals, subgroup
     sums, or displayed arithmetic that does not reconcile under the stated rule.
2. `Denominator, proportion, or total inconsistency`
   - numerator/denominator mismatches, percentages, analysis totals, missingness totals, or mutually
     exclusive categories that do not reconcile.
3. `Statistical reporting inconsistency`
   - point estimate versus interval, interval endpoint/order, sign/direction, P value/test/statistic/SE
     relationships when the source supplies a compatible rule, or conflicting inferential results.
4. `Cross-document numeric inconsistency`
   - a matched result differs between abstract, main text, tables, figures, captions, appendices,
     supplement, protocol/SAP, or provided structured data after population/time/contrast/model matching.
5. `Measure, label, or scale inconsistency`
   - OR, RR, RD, HR, mean difference, standardized mean difference, unit, transform, direction,
     reference group, or scale is mislabeled or conflicts with the displayed values.
6. `Rate-versus-count inconsistency`
   - event count, proportion, risk, incidence rate, person-time rate, frequency, or percentage is
     confused with or labeled as a different quantity.

## Secondary category

Use `Analysis-unit or population inconsistency` only when a sample unit, cluster/randomization level,
analysis population, or denominator definition produces a concrete inconsistency in a reported value,
statistic, label, comparison, or interpretation. Do not turn a general design concern into a candidate.

Participant flow belongs in the main review only when it yields a numeric, denominator, population,
or cross-location inconsistency. General flow-description quality is out of scope.

## Candidate threshold

A candidate needs all of the following:

- one or more exact supplied-source locations;
- the printed values or statements being compared;
- a reproducible arithmetic, statistical, labeling, or identity rule;
- a distinction between direct observation and derived diagnostic reasoning;
- the exact unresolved human question when the package lacks a necessary definition.

Do not manufacture a candidate merely because a model detail is unreported. Do not discard an
observable printed mismatch merely because its production mechanism or inferential convention is
unknown. Record the missing definition as the human question.

## Display-zero P values are not candidates

Do not register a candidate merely because a very small P value is printed as `P = 0`, `p = 0.000`,
or an equivalent display zero. Treat that notation as conventional finite-precision rounding,
software export, or numeric underflow when it is otherwise compatible with the reported estimate,
interval, test direction, and narrative. It does not by itself create a factual inconsistency or a
meaningful risk of reader misunderstanding. Do not reconstruct a tiny tail probability solely to
argue that an exact probability cannot be zero, and do not prescribe a replacement threshold.

Record the relationship as `DISPLAY_ZERO_NOT_CANDIDATE` in the statistical checker when useful for
coverage. A candidate is allowed only when supplied-package evidence establishes an independent
inconsistency beyond display precision, such as a conflicting P value for the same matched result, an
interval or statistic incompatible under the stated same test, or prose that explicitly interprets
zero as an absolute probability. Frame any candidate around that independent contradiction, not
around the `P = 0` notation.

There is no expected candidate count. Zero is valid after complete coverage. One is valid. More than
10 is valid. Continue until all assigned source and relationship units have been checked.

## Tone

Use neutral phrases such as `candidate consistency issue`, `quality-control observation`, `the printed
values do not reconcile under the stated rule`, and `requires human adjudication`. Avoid sensational
or prosecutorial language. Do not assign severity. Keep paper-level conclusion impact separate from
potential downstream evidence reuse, and claim neither without package evidence.
