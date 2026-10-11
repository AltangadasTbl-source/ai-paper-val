# Independent initial inclusion screen

Read QUALITY_CONTROL_SCOPE.md and the complete Workflow 1.6.1 review contract, including its inclusion-screen section, and inspected all findings in the current numeric, cross-source and statistical-pass-1 checker artifacts; the cross-source artifact contains no findings. This fresh screen uses supplied sources and current source-linked derivatives only, with no count target, external evidence or earlier scientific conclusions.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |

- **F-NUM-001:** The directly reread Table 2 counts, risk-ratio label and intervals reproduce a repeated effect-identity discrepancy beyond display precision, including abstract key secondary results, and neither an established binary model nor immediate context identifies the quantity to extract.
- **F-ST1-001:** The directly reread methods, Table 2 and abstract independently support the same unresolved binary-effect definition and its extraction implications, so this finding joins F-NUM-001 in one consolidated issue rather than creating another issue.

## Consolidation and exact retained locations

The two INCLUDE rows constitute **one included issue**, registered by the coordinator as C001. Both checker provenance records, every occurrence and the union of their source locations are retained.

- REPORT [main article PDF page 6, printed page 1877, Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6): ICU mortality, hospital mortality, development of ARDS, development of pneumonia, pneumothorax, atelectasis, extrapulmonary infection, extrapulmonary sepsis, delirium and need for tracheostomy; the randomized-strategy column headings, each explicit event fraction, each RR and 95% CI, and footnote c are retained.
- REPORT [main article PDF page 1, printed page 1872, Abstract Results](../../../jama_simonis_2018_oi_180108.pdf#page=1): repeated ARDS, pneumonia, severe atelectasis and pneumothorax percentages, RRs, intervals and P values.
- REPORT [main article PDF page 4, printed page 1875, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4): secondary binary outcomes assessed using risk ratios, Wald likelihood ratio approximation intervals and chi-square tests; nearby explicitly specified Cox, inverse-Gaussian and other models distinguish those analyses.
- PLAN [updated SAP PDF page 13, Secondary outcomes](../../../joi180108supp2_prod.pdf#page=13): intervention effects on ICU/hospital mortality and other secondary outcomes assessed with risk ratios, Wald approximation intervals and chi-square tests; this location corroborates the report's effect label rather than supplying a conflicting plan specification.

Each cited supplied page was reread directly with Poppler 25.03.0 pdftotext -layout, with output read in this screening session; the current run's directly rendered main page 6, preprocessing/st1-main-p6.png, was also visually inspected to confirm the column alignment, all ten binary rows and footnote c. No source or reused asset was modified.

## Independent threshold evaluation

**Comparison tier and focus:** The issue concerns a label and numerical transformation that changes the effect quantity, including pulmonary-complication results reported in the abstract; it qualifies for comparison before threshold screening and is not a peripheral descriptive comparison. It falls in focus areas B/C, with supporting numerator/denominator arithmetic in A, within REPORT material. The proposed domain is statistical_results and the relationship is S_W; the corroborating PLAN page does not establish P_R.

**Reproduction and display precision:** Independently recalculated event-risk ratios from the source fractions are ICU mortality 1.168232, hospital mortality 1.094400, ARDS 0.762228, pneumonia 1.147451, pneumothorax 1.375000, atelectasis 1.013534, extrapulmonary infection 0.738202, extrapulmonary sepsis 0.775112, delirium 1.188025 and tracheostomy 1.053701. Their printed RRs are respectively 1.11, 1.06, 0.86, 1.07, 1.16, 1.00, 0.84, 0.87, 1.15 and 1.03. Even conservatively allowing every printed count and denominator its half-unit interval, eight event-risk-ratio intervals do not intersect the printed RR's two-decimal interval: ICU/hospital mortality, ARDS, pneumonia, pneumothorax, infection, sepsis and delirium. For ARDS the conservative interval is 0.722479–0.803849 versus the printed 0.855–0.865; for pneumothorax it is 1.187291–1.597257 versus 1.155–1.165. Atelectasis and tracheostomy overlap under this conservative test and are retained only as corroborating locations in the repeated pattern, not independent discrepancies.

For counts a/n in the low group and c/m in the intermediate group, the diagnostic alternative [a/(a+c)]/[(n−a)/(n+m−a−c)] instead conditions treatment-group membership on event status. Independent calculation gives ARDS 0.857889 with diagnostic log-Wald interval 0.594560–1.237844, and pneumothorax 1.163636 with interval 0.735670–1.840566, closely tracking the displayed effects and intervals; the same orientation tracks the whole row family. This is diagnostic evidence for an unresolved effect identity, not a statement about the computation code or exact numerical formatting. It does not establish a separate CI/P contradiction: chi-square association testing is symmetric under contingency-table transposition.

**Immediate context and exclusion catalogue:** MODEL_VERSUS_CRUDE is not source-established for these binary rows: the cited report and SAP specify RR/Wald/chi-square analysis without establishing an adjusted, stratified or otherwise model-based binary estimate, while other model families are expressly described for their separate results. This screen does not infer that absent binary-model details prove a particular computation; an undocumented model remains a possible explanation to clarify. The evidence supporting inclusion is the repeated alternative conditional quantity and its interval pattern under a treatment-event RR label, rather than merely an isolated comparison of a modeled estimate with crude counts. A statistically literate reader can calculate an event-risk ratio from the fractions but cannot identify at once what generated the printed RR and CI or whether that displayed quantity represents the stated intervention contrast. The discrepancy is not resolved by changing a symbol, a familiar outcome name, final-digit precision, or the stated nonsignificant P values.

**Named interpretation/extraction consequence:** In particular, the abstract and Table 2 ARDS RR 0.86 (0.59–1.24), pneumonia RR 1.07 (0.78–1.47) and pneumothorax RR 1.16 (0.73–1.84) may be extracted as effects of low versus intermediate tidal-volume ventilation on event occurrence, although the printed fractions establish different event-risk ratios. Clarifying the effect definition could change the effect quantity, magnitude and interval used in evidence synthesis. This screen does not infer a change in the paper's nonsignificance statements or its primary-outcome conclusion, select a replacement analysis, assign an evidence state, or propose a disposition.

## Compact counts and limitations

Findings screened: 2; INCLUDE findings: 2; consolidated included issues: 1; SCREENED_OUT findings: 0; screened-out counts by reason code: none. Cross-source findings: 0. Source locations reread: all cited locations in both findings. Limitations: the package does not supply the binary computation code or a complete additional binary-model definition; diagnostic formulas do not establish either. No assigned screening coverage gap remains.

Coordinator registration: both INCLUDE findings were assigned C001 as one consolidated issue, preserving all locations and provenance. Registration is complete.
