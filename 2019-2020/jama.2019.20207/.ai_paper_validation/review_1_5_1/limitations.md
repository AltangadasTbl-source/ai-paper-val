# Limitations and Missing Definitions

These are bounded source, definition, extraction, and runtime limitations. They do not create a remaining direct-source coverage gap and do not assign a scientific disposition to any candidate.

## Source and definition limitations

- The supplied package does not contain randomization-system configuration or audit records, participant-level ages, screening records, Cox-model stratum encoding, or an amendment implementation crosswalk. These inputs are needed to resolve the age-70 randomization and eligibility questions in C001 and C002.
- No separate supplied progression-endpoint version using `<=70/>70`, event-level endpoint classifications, or endpoint implementation code is present. The cited endpoint definitions use `<70/>=70`; C003 therefore remains a version-confirmation question.
- Exact counseling-phase start/end anchors, an inclusive-boundary convention, and participant call-delivery logs are absent for the 16-versus-17-month schedule comparison in C004.
- The exact denominators behind 183 (81.7%) and 171 (79.5%) are not printed. The source also does not define whether the two displayed PSA categories in Table 1 are intended to exhaust their stated denominators.
- The pilot source does not define whether intervention `n=45` and control `n=23` are randomized-arm totals or an evaluable paired-dietary subset, and it does not account for the six-person difference from the stated total of 74.
- Editorial intent for the narrative phrase “cruciferous servings” is not supplied, although the attached units and exact table matches identify the printed values as the grams/day row.
- For C009-C013, the package does not supply unrounded mixed-model estimates, covariance or contrast matrices, degrees of freedom, exact test statistics, variance estimators, analytic data versions, table-production records, or a rounding convention. Interval-based normal calculations are diagnostic only and cannot identify the intended model P value.

## Extraction limitations

- DOC-004 contains a pre-existing `rendered_page.png` without a truthful page identity. It was excluded from evidence use. Other mapped native and rendered assets cover DOC-004 page 3, so this asset limitation does not create scientific undercoverage.
- Main Table 2 and the DOC-004 eTable are dense landscape tables. Direct PDF visual confirmation was required to resolve layout-text column order, signs, and the visible double-hyphen artifact before the energy control interval. No remaining cited table value depends solely on OCR.
- The eFigure supplies axes and graphical marks but no printed quartiles, medians, means, whisker endpoints, or outlier values. It cannot support exact numeric reconstruction of those summaries.
- No workbook, spreadsheet, CSV, DOC, or DOCX direct source is present. All source locations are PDF pages.

## Runtime and finalization limitations

- The two statistical passes are recorded with distinct fresh Terra/high runtime IDs and complete S001-S017 scope, but model-runtime token accounting is finalized only after the complete Markdown report and all in-window model work are finished.
- At the time this quality artifact was assembled, report generation, final timing and token accounting, standalone HTML rendering, and mechanical validation were coordinator-owned downstream stages. Their completion status must be taken from the final `run_state.md`, token summaries, coverage manifest, and `review_validation.json`, not inferred from this audit.
