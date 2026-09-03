# Limitations and Missing Definitions — Workflow 1.5.1

## Scientific-evidence limitations

- The supplied package does not contain participant-level data, analysis datasets, fitted model objects, or full variance/test internals. Mixed-model effects, bootstrap quantile intervals, Bayesian posterior quantities, corrected-GEE inferences, and cause-specific Cox inferences therefore cannot be independently refitted from the package.
- For several corrected-GEE and cause-specific-Cox results, the package does not fully specify a single shared test statistic, confidence-interval construction, variance-estimator application, and sidedness sufficient for an exact independent P-value/interval reconstruction. The review did not turn normal-theory diagnostics into candidate rules.
- Protocol, SAP, PRO-SCAN, and external-feasibility quantities are prospective, contextual, or from distinct populations where identified. Nonidentical planned and final values or methods were not treated as contradictions without a matched population, time, contrast, estimand, and analysis version.
- C001 lacks an explicit definition of the two endpoints in each Table 2 ventilation group display. C003 lacks an explicit definition of the Bayesian-row group summaries. C004 lacks any printed matched day-10 mean values or a defined mean-based analysis.
- C002 has complete numeric inputs, but the source does not state whether its isolated comma-and-space was intentional. C005 and C006 have complete numeric inputs, but the source does not state which percent-sign convention was intended.
- Reused text, OCR, renders, and document maps were locators and transcription aids. Candidate evidence was rechecked on direct PDF pages, but no author manuscript, production proof, or correction history is supplied to identify how a printed inconsistency arose.

## Resolved audit findings

- The S013 renal/RRT interaction transcription has been corrected across the component support map, merged support map, and both global inventories. Direct PDF pp. 28 and 31 both print `P<0.001`; the former `p>0.001` locator transcription is now identified only as a corrected noncandidate record.
- Candidate-ledger, numeric-checker, cross-source-checker, statistical-pass-2, evidence-recheck, and quality-audit PDF links resolve to the supplied package sources.
- All 78 source-link occurrences in `extraction/main_quantitative_evidence.md` now use the correct package-root-relative path and resolve to the supplied main PDF.
- The candidate ledger's opening summary now states the complete six-candidate set, C001–C006, while preserving the pass-2 append history.

## Remaining artifact limitations requiring coordinator closure

- At audit completion, report assembly, final timing/token accounting, post-review hash comparison, HTML rendering, and mechanical validation remain coordinator stages. `coverage_manifest.md` must mark evidence quality complete and add the required report-generation row after those artifacts are produced.

These limitations do not authorize omission of a source unit, relationship, candidate, recheck, or report card. They do not rank or adjudicate any candidate.
