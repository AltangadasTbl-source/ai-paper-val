# Candidate Ledger

Stable IDs were assigned only after merging the complete numeric, statistical-pass-1, and cross-source checker outputs. No genuine duplicate proposals existed. Stable IDs are immutable. All candidates remain **Pending Human Adjudication**.

## C001 — Conflicting printed P values for matched day-60 mortality result

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** Statistical consistency pass 1, proposal SP1-01. Numeric review found the counts and proportions coherent. Cross-source review independently recorded the difference but treated the unknown test behind the prose value as a possible source-grounded alternative rather than a same-model contradiction.
- **Related stable relationships:** S008, S021; N025, N047.
- **Exact source locations:** DOC-001 PDF p. 1 (abstract); DOC-001 PDF p. 4 (Results, expressly directing the reader to eFigure 2); DOC-001 PDF p. 3 (mortality-analysis method); DOC-003 PDF p. 7 (SAP mortality-analysis method); DOC-004 PDF p. 11 (Supplement 3 eFigure 2, day-60 panel).
- **Direct observation:** For day-60 mortality, DOC-001 reports 28/101 (27.7%) in the levosimendan group and 26/104 (25.0%) in the placebo group and prints `P = .78` in the abstract and Results. DOC-004 eFigure 2 shows the same day-60 cumulative death counts and prints `p = 0.56, Log-rank`.
- **Comparator:** Printed `.78` versus printed `.56` for the matched day-60 mortality comparison.
- **Consistency rule:** A matched endpoint, time point, population, and treatment contrast should not carry different P values when they represent the same indicated test/result. The methods and SAP name log-rank for mortality, and the Results directs the reader to eFigure 2.
- **Diagnostic reasoning:** The difference is not display rounding. No P value was reconstructed from the RR confidence interval, because that interval and a log-rank comparison need not use the same test.
- **Alternative source-grounded interpretation:** The prose `.78` may intentionally come from a different, pre-specified analysis than eFigure 2's labelled log-rank test. The supplied prose does not state that test, model, estimand, or censoring rule.
- **Exact remaining human question:** Does `.78` represent a different pre-specified analysis, and if so which test/model, estimand, analysis population, and time-to-event/censoring rule; or is either displayed P value erroneous?

Candidate count: 1.

