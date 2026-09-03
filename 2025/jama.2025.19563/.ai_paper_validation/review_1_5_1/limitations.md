# Workflow 1.5.1 Limitations and Missing Definitions

## Scientific-resolution limitations

- **C001:** The supplied package lacks a dated protocol amendment/final SAP version history and component-achievement status for the 15 participants with diabetes-range A1C. The number of endpoint classifications, if any, affected by the definition difference cannot be calculated.
- **C002:** Participant-level A1C records, device logs, an explicit statement that the three follow-up method rows are exhaustive, and the unmatched participant/method identity are absent.
- **C003:** The figure-production source and a literal baseline-weight summary in kilograms are absent; the package supports the label/unit comparison but not its production cause.
- **C004:** Individual-level age data and complete test outputs for site, baseline-A1C, completion-status, and randomized-arm contrasts are absent. The repeated p=.014 comparator scope cannot be conclusively assigned from the supplement table alone.
- **C005:** Characteristic-specific completion-status P values, test statistics, and the intended footnote inequality are absent.
- **C006:** Analysis code, named software output, continuity correction, exact/asymptotic setting, and tie-handling details are absent. The displayed P value cannot identify which printed test label is correct.
- **C007:** Full-precision per-imputation estimates, the analysis/standardization model, contrast coding, covariance estimates, pooling steps, and standard-error calculation are absent. The displayed confidence bound cannot be recreated from the two displayed percentages.

## Extraction and source-format limitations

- DOC-002 has a glyph-encoded native/layout text layer. Its 90 pages were nevertheless mapped from direct CPU-rendered pages; this is not a scientific-coverage gap.
- Native PDF extraction can flatten multi-column and table layout. Candidate locations were checked against the direct PDFs or retained direct page renders where alignment was material.
- The attempted OCR for DOC-003 p. 67 was unusable, but direct native/layout extraction and page rendering were sufficient to map the page.
- No Office workbook, Word document, or CSV source is present. There are no formula-versus-cached-value relationships to audit.

## Statistical reproducibility limitations

Several planned or reported relationships do not supply all formulas, exact test options, degrees of freedom, covariance/variance estimators, full individual-level values, or adjusted-estimand definitions. No missing convention was inferred. One-sided confidence bounds were not treated as two-sided intervals. Diagnostic arithmetic was limited to displayed values and explicit contrast order.

DOC-002 p. 37 directly says “one-sided 95% confidence interval.” Two workflow records currently transcribe this as “two-sided”; they require correction before report assembly. Both statistical checker passes use the correct one-sided wording.

## Review boundary

The review is limited to supplied-package quantitative and statistical reporting consistency. It does not adjudicate candidate validity, importance, or action; audit study design generally; infer raw-data errors; or claim that any candidate changes the paper's conclusion. No web or external literature was used. Every candidate remains **Pending Human Adjudication**.
