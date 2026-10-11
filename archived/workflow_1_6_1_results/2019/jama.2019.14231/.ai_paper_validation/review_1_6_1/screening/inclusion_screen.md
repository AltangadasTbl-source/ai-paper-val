# Independent inclusion screen

Stage: initial. Runtime agent: `/root/inclusion_screen`. Fresh `qc161_inclusion_screener`, model `gpt-6.1-sol`, reasoning effort `high`. The complete `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6_1/review_contract.md` were read. Scope consists of every emitted finding in `checkers/numeric_consistency.md`, `checkers/cross_source_consistency.md`, and `checkers/statistical_pass_1.md`: F-NUM-001, F-XS-001, and F-ST1-001. Decisions apply the four inclusion criteria independently, without reference to earlier review conclusions, other papers, or a desired count.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-001 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |

- **F-NUM-001:** The five Table 2 absolute eight-year risk differences do not reproduce by the stated control-minus-surgery contrast of the adjacent Kaplan–Meier risks after display-precision allowance, concern abstract-reported secondary outcomes, lack an immediately resolving alternative point-estimator definition, and give an extractor two distinct absolute-effect values for each named outcome.
- **F-XS-001:** This finding reproduces the same five-row point-contrast pattern as F-NUM-001, with the supplement and abstract supplying corroboration and scope context rather than an independent issue.
- **F-ST1-001:** This finding reproduces the same five-row point-contrast pattern as F-NUM-001, with the methods and Figure 3 supplying estimator and risk-population context rather than an independent issue.

## Direct-source reread and consolidation

The one included issue consolidates the full pattern and retains all locations and checker provenance from F-NUM-001, F-XS-001, and F-ST1-001; the coordinator will replace the shared `PENDING` entries with its assigned candidate ID, including the duplicate-reference cells. No candidate ID is assigned here.

Source authority was the supplied PDFs. The five Table 2 rows, column headings, risk sets, ARD points and confidence intervals, and footnotes a and b were independently read from the fresh source-page image `extraction/main_direct_page_007.png` and from direct Poppler layout extraction of [REPORT main article, physical PDF p. 7](../../../jama_aminian_2019_oi_190103.pdf#page=7). The remaining cited locations were independently reread through direct Poppler extraction of the supplied PDFs:

- [REPORT main article, p. 1, abstract](../../../jama_aminian_2019_oi_190103.pdf#page=1): the six individual primary components are secondary end points and all seven prespecified secondary outcomes are reported in the abstract results, bringing the affected outcomes within the key-secondary comparison tier.
- [REPORT main article, p. 4, statistical analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4): cumulative-incidence estimates use Kaplan–Meier at eight years, absolute risk differences are calculated for each outcome, and percentile bootstrap iterations supply the difference intervals; the separately described adjusted Cox models do not define an alternative absolute-risk point estimator.
- [REPORT main article, p. 7, Table 2](../../../jama_aminian_2019_oi_190103.pdf#page=7): heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation rows; the surgical and control incidence columns, their outcome-specific risk sets, the absolute eight-year risk-difference column, footnote a specifying control minus surgery and bootstrap intervals, and footnote b specifying adjustment for HRs and P values.
- [REPORT main article, p. 8, Figure 3 panels B–F and caption](../../../jama_aminian_2019_oi_190103.pdf#page=8): matching outcomes, eight-year Kaplan–Meier framing, group orientation, and outcome-specific baseline exclusions; no distinct ARD population or point estimator is specified.
- [REPORT results supplement, p. 7, eTable 5](../../../joi190103supp1_prod.pdf#page=7): all five corresponding Year 8 surgical/nonsurgical pairs and their intervals repeat the Table 2 incidence values; this source corroborates the incidence side without adding a conflicting cross-document relationship.

## Independent four-criterion assessment

**Reproduced:** All five source-transcribed pairs and differences match the checker records. In percentage points, allowing each one-decimal risk its half-unit interval makes the control-minus-surgery interval the printed subtraction plus or minus 0.10; allowing each one-decimal ARD its half-unit interval gives plus or minus 0.05. The intervals remain disjoint:

- Heart failure: control 18.9, surgery 6.8; subtraction 12.1, allowable interval 12.00–12.20; printed ARD 12.9, allowable interval 12.85–12.95; printed ARD CI 10.4–15.1.
- Coronary artery disease: control 11.6, surgery 7.9; subtraction 3.7, allowable interval 3.60–3.80; printed ARD 4.2, allowable interval 4.15–4.25; printed ARD CI 1.9–6.8.
- Cerebrovascular disease: control 5.6, surgery 4.1; subtraction 1.5, allowable interval 1.40–1.60; printed ARD 1.8, allowable interval 1.75–1.85; printed ARD CI −0.03–3.4.
- Nephropathy: control 16.3, surgery 6.1; subtraction 10.2, allowable interval 10.10–10.30; printed ARD 11.1, allowable interval 11.05–11.15; printed ARD CI 8.8–13.6.
- Atrial fibrillation: control 13.6, surgery 7.9; subtraction 5.7, allowable interval 5.60–5.80; printed ARD 6.5, allowable interval 6.45–6.55; printed ARD CI 4.4–8.7.

The primary composite, secondary composite and mortality rows reconcile under the same point-subtraction rule. No separate marginal interval bounds were subtracted to reconstruct an ARD interval.

**In focus:** The pattern concerns estimate identity and statistical method specification (focus B/C, with numeric contrast arithmetic under A); the comparison is between two representations of abstract-reported secondary results, rather than peripheral contributor counts or a pointer alone. Proposed domain `statistical_results`; primary and all relationships `S_W`. All conflicting locations are REPORT content within the main article; the REPORT supplement corroborates one side, and no PLAN source is a conflicting side.

**Not resolved by context:** The table labels both risks and differences at eight years, and footnote a defines the direction. Bootstrapping is stated for intervals; no separate adjusted-risk, bootstrap point-summary, population, or censoring definition is given for the five ARD points. The explicit adjustment footnote applies to HRs and P values. Neither a distinct estimator nor a specific replacement value is recoverable at once from the adjacent risks, contrast column, methods, figure caption, or supplement. Thus the issue is neither a modeled estimate compared with a crude fraction nor an obvious isolated symbol or decimal slip.

**Bears on interpretation or extraction:** The named values are the eight-year absolute risk differences for heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation. An extractor could use 12.9, 4.2, 1.8, 11.1 and 6.5 from the labeled ARD column or obtain 12.1, 3.7, 1.5, 10.2 and 5.7 from the adjacent eight-year risks, so these distinct values require reconciliation. This assessment does not infer any change to the adjusted HR conclusions.

## Summary and limits

Findings screened: 3. Included findings: 1. Distinct included issues: 1, spanning five outcome rows. Screened-out findings: 2, both `DUPLICATE_OF_INCLUDED`; all other screened-out reason-code counts are zero. All assigned cited locations were reread. No source access or transcription limitation affected the screen. Original analysis outputs and an alternative point-estimator definition are not supplied, so the screen does not identify which displayed quantity should govern the final extraction. The later mechanical recheck and human adjudication remain separate stages. Sources, reused assets, checker files and other agents' artifacts were preserved.

Coordinator registration: C001 replaces all three shared candidate-reference placeholders. The included finding is F-NUM-001; F-XS-001 and F-ST1-001 are retained as duplicate provenance for the same stable issue.
