# Limitations and Missing Definitions

- The supplied package contains four PDFs but no participant-level dataset, analysis program, workbook, or CSV. Candidate-specific ambiguities therefore remain for human adjudication rather than source-package resolution.
- DOC-002 and DOC-004 had no reusable page extraction. All 77 affected pages were freshly mapped from the direct PDFs; the derivative gap is closed scientifically but remains a reuse limitation.
- Some embedded SAP pages in DOC-002 required CPU OCR plus rendered-page confirmation. Degraded OCR on administrative or diagram pages did not leave unmapped scientific units.
- Several absolute-difference results do not state a common subtraction/reference convention. No candidate was registered solely from an apparent sign change where direction could not be matched.
- C001 lacks an explicit denominator/day-record definition for the printed means. C003 lacks participant-level adherence output. C004 lacks an outcome-specific denominator statement. C005 lacks an explicit adjusted/unadjusted ARD definition. C006 lacks source-version/unrounded output. C007 lacks underlying category tabulation. C008 lacks CI construction, test distribution/degrees of freedom, transformation detail, and unrounded model output.
- The package contains no display-zero P value. Inequality displays such as `P<.001` were not treated as display zeros or candidates.
- Runtime/API response-level token counts are not exposed to the coordinator by the available runtime interface; token accounting will therefore use authoritative `UNAVAILABLE` records and will not estimate counts from text.

