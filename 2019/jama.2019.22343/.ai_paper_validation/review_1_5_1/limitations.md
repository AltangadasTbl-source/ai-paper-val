# Limitations and Missing Definitions

## Evidence-derivative limitations

- The package contains three direct PDFs and no supplied workbook, CSV, DOC, or DOCX source. The scientific scope is therefore page-based.
- Reusable native text covers 40 of 75 source pages. The 35-page derivative gap was closed by fresh native and layout extraction from the direct PDFs: all 15 DOC-002 pages and DOC-003 pages 1-16 and 46-49. DOC-003 page 8 required a direct visual confirmation because its text layer is sparse. This is a derivative limitation, not a remaining scientific-coverage gap.
- No reusable OCR text, layout-text collection, standalone machine-readable table extraction, or workbook extraction was available. Existing rendered pages and prior maps were locator aids only. Direct PDFs remain authoritative.
- Some source table cells are printed as `NR` or `NOS`. These are source-reported missing entries, not extraction omissions, and no values were inferred for them.

## Source and reporting definitions absent from the package

- C001 and C002 lack unrounded pooled endpoints, pooled standard errors, final model output, and a figure-versus-narrative rounding or export rule. Those absences prevent determining which printed endpoint was intended.
- C003 lacks study-level extracted means, sign-reversal operations, an explicit intervention-minus-control or control-minus-intervention convention, and a statement distinguishing standardized SMD direction from native instrument direction in Table 2. Figure 4 directly places negative values toward “Favors NIPPV” and positive values toward “Favors No NIPPV”; the missing subtraction order prevents inferring which sign intrinsically represents intervention benefit.
- C004 lacks group summary data, the exact standard error, confidence-interval construction, analysis output, and a version history that could explain the two printed interval widths.
- C005 lacks explicit enrolled, randomized, treated, baseline-characterized, and outcome-analysis population definitions for the Cheung 2010 displays. Outcome event numerators and exact outcome denominators are not printed.
- C006 lacks per-synthesis statistical commands and output, degrees of freedom, critical-value and variance settings, and a dated amendment or reconciliation of the protocol and final-article model descriptions. The supplied confidence intervals do not establish whether Knapp-Hartung was used.
- Across the statistical inventory, the sources do not provide a compatible result-specific test statistic, standard error, degrees of freedom, covariance for change scores, confidence-interval construction, continuity correction, final study weights, variance estimator, or exact mapping from rounded intervals to displayed P values.
- `S002` remains diagnostic only. The printed HMV mortality OR and interval permit an approximate log-scale CI-to-P calculation, but the exact effect-test and interval definitions are absent. The approximation cannot establish a stable candidate and was not promoted to a C ID.
- `S021` through `S023`, `S039`, `S044` through `S054`, `S065` through `S067`, and `S071` lack one or more estimates, intervals, P values, test statistics, or denominator inputs needed for a broader exact inferential reconstruction. Their available source fields were still mapped and checked.
- The package does not supply raw participant data, source-study analysis files, meta-analysis code, or a protocol amendment. These absences limit resolution of the registered comparisons but do not create new candidates by themselves.

## Interpretation boundaries

- No stable candidate is based on a P value displayed as zero. The zero in `S056` is a non-P incidence display with a nonzero upper interval endpoint.
- The audit does not determine which printed value, label, population, or model description should replace another. Every C ID remains **Pending Human Adjudication**.
- Potential downstream relevance is limited to what a reviewer, systematic-review extractor, meta-analyst, or guideline evidence table could copy if a candidate is confirmed. The package does not establish that propagation or a paper-level conclusion change occurred.
