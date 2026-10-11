# Independent initial inclusion screen — Workflow 1.6.2

Runtime ID: 01a129c3-6696-7d12-977a-068c52ecf636. Fresh gpt-6.1-sol/high inclusion screener. Scope: all 22 findings in the frozen canonical numeric, cross-source and statistical-pass-1 checker artifacts. QUALITY_CONTROL_SCOPE.md and the complete review contract, including the inclusion-screen rules, were read. Each cited comparison was reread from the supplied PDFs independently of the checker transcription. Exact values and key definitions were additionally inspected in fresh CPU-rendered source pages. No earlier-run scientific conclusions or external evidence were used.

The coordinator assigned stable C IDs after the independent screen; all included and duplicate rows now name their corresponding stable ID. Temporary issue keys G001–G012 in the justifications and issue_groups.md are grouping aids, not stable candidate IDs. All resulting candidates remain Pending Human Adjudication. Findings within a repeated pattern were checked individually; unsupported occurrences and corroborating sources are distinguished in issue_groups.md.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-NUM-101 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-008 | cross_source_consistency_reviewer | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C011 |
| F-XS-009 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-002 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-003 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C011 |
| F-ST1-004 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C007 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C012 |
| F-ST1-007 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C003 |
| F-ST1-008 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-009 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST1-010 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C010 |
| F-ST1-011 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |

## Independent justifications

- F-NUM-001 → G001: Route A, category 1, because the source pairs the SCDE absolute difference −0.34 (95% CI −0.73 to 0.05), which includes zero, with P=.03, while the separate baseline-adjusted ratio and its interval support attribution of the P value to that ratio as an alternative rather than an exclusion.
- F-NUM-101 → G002: Route A, category 2, because the protocol appendix prints 0.9% while its body prints 0.09% and rounded baseline/relative-reduction inputs imply [0.088375%, 0.095275%], leaving relative discrepancy 0.838583 above 0.05.
- F-XS-001 → G003: Route A, category 5, because protocol SCDE membership requires fluids AND vasoactive therapy and ward death without transfer, whereas reported definitions allow fluids OR vasoactive therapy and death in the first ICU hour, with a further ≥60 versus >60 boundary between report locations.
- F-XS-002 → G004: Route A, category 5, because matched preventable-arrest, readmission and call/consultation outcomes are planned secondary outcomes yet appear as post hoc, and the planned PIM2-score analysis is described as not prespecified, while ambiguous ICU populations and non-DNR placement are bounded separately rather than counted as independent conflicts.
- F-XS-003 → G005: Route A, category 5, because the protocol and SAP expressly plan subgroup treatment analyses applicable to primary/key-secondary outcomes and the main expressly says the four subgroups are not reported, with no corresponding estimates or interactions in the supplied results.
- F-XS-004 → G006: Route A, category 5, because the SAP explicitly documents alternative-model sensitivity analyses for the primary/key-secondary effect measures while complete report inspection finds no alternative-model outputs, with its retrospective tense and undated timing retained as alternatives.
- F-XS-005 → G007: Route A, category 5, because the planned weighted hospital-logit primary model and size-stratum covariate are replaced by the SAP/report binomial GEE and two-predictor specification without a corresponding original-model output, despite disclosed removal of stratification.
- F-XS-006 → G008: Route A, category 5, because the SAP specifies baseline adjustment for the key-secondary SCDE rate difference but Table 3 identifies its reported −0.34 (−0.73 to 0.05) model as not baseline adjusted, with nonconvergence disclosed as a possible explanation.
- F-XS-007 → G009: Route A, category 5, because the planned all-seven/all-observation-set documentation analysis is replaced by the last-set ≥5 definition that produces the reported 38.1 percentage-point difference, even though the revision before analysis is disclosed.
- F-XS-008 → G002: The same protocol 0.9% versus 0.09% magnitude discrepancy is already included from F-NUM-101, and the main article merely corroborates the smaller scale.
- F-XS-009 → G010: Route B, because the planned-versus-reported ICU-readmission denominator is in focus, hospital and ICU discharges are distinct populations without a supplied amendment resolving the change, and it changes the extracted rates 28.40 and 21.25 per thousand.
- F-ST1-001 → G001: The same SCDE absolute-interval/P pairing is already included from F-NUM-001, preserving all three report occurrences and the separate-ratio interpretation.
- F-ST1-002 → G011: Route A, category 1, because the printed respiratory-rate 95% interval 0.02–1.68 excludes zero while the Holm-adjusted P=.18 is nonsignificant, with the explicit different multiplicity adjustment retained as the alternative explanation.
- F-ST1-003 → G002: The same protocol mortality absolute-reduction decimal discrepancy is already included from F-NUM-101, retaining the appendix scenario and body input locations.
- F-ST1-004 → G004: The same planned-versus-post-hoc/nonprespecified outcome-status pattern is already included from F-XS-002, with its additional urgent-versus-overall ICU and PIM2 distinctions preserved.
- F-ST1-005 → G005: The same omitted planned subgroup-analysis pattern is already included from F-XS-003, retaining protocol four-subgroup and SAP two-interaction specifications.
- F-ST1-006 → G006: The same unavailable model-choice sensitivity outputs are already included from F-XS-004, retaining both relative- and absolute-scale model lists.
- F-ST1-007 → G003: The same changed SCDE component and fluid-boundary pattern is already included from F-XS-001, preserving the main and supplementary report definitions separately.
- F-ST1-008 → G007: The same protocol-to-GEE primary specification replacement is already included from F-XS-005, with associated protocol secondary weighting/stratum and reported individual-level specifications retained as related pattern locations.
- F-ST1-009 → G009: The same all-seven/all-set to last-set ≥5 documentation replacement is already included from F-XS-007, retaining protocol measurement and report revision/result locations.
- F-ST1-010 → G010: The same planned hospital-discharge versus reported ICU-discharge readmission denominator change is already included from F-XS-009, retaining the baseline as well as intervention rate occurrences.
- F-ST1-011 → G012: Route A, category 5, because the protocol expressly plans mortality following DNR orders while the displayed sensitivity output is mortality without DNR and no modeled following-DNR result is supplied, although the report's limitation refers to such an analysis.

## Scope and limitations

22 unique finding decisions: 12 INCLUDE anchors, 10 SCREENED_OUT findings, all 10 with reason DUPLICATE_OF_INCLUDED; these represent 12 consolidated included issues (11 through route A and 1 through route B), with no count target applied. Other screened-out reason counts are zero at the full-finding level; bounded nonqualifying occurrences within included patterns are recorded separately in issue_groups.md and do not erase qualifying occurrences.

Source text derivatives were freshly produced directly with Poppler pdftotext 25.03.0, layout mode, CPU: preprocessing/screen-main.txt (main pp.1–9), screen-protocol10-16.txt, screen-protocol24.txt, screen-protocol29.txt, screen-sap.txt (SAP pp.1–7), and screen-results.txt (results pp.1–14). Extra exact-page extraction to standard output reread the protocol summary p.1, main p.9, main pp.1–3/p.8, and results pp.6–10. Fresh Poppler pdftoppm 25.03.0 CPU renders visually inspected: screen-main4.png, screen-main5.png, screen-main6.png, screen-main7.png, screen-protocol12.png, screen-protocol14.png, screen-protocol16.png, screen-protocol24.png, screen-protocol29.png, screen-sap1.png, screen-sap2.png, screen-sap3.png, screen-sap4.png, screen-sap5.png, screen-sap6.png, screen-results6.png and screen-results12.png. No OCR or fallback interpreter was used.

Main pp.10–11 (affiliations, contributions and references) and protocol p.13 were additionally reread directly with exact-page layout extraction to standard output, completing the full main-report inspection for absent analysis outputs. The supplied package has no dated SAP/amendment sequence, patient-level membership data, complete fitted-model output, or omitted subgroup/sensitivity estimate set; these bound interpretation and calculations but leave no unchecked finding. At initial reading, the statistical checker's PIM2/composite links naming a nonexistent “joi180015supplement 3_prod.pdf” were locator transcription issues: exact supplied joi180015supp3_prod.pdf pp.6 and12 independently reproduce the cited content and are used in issue_groups.md; the coordinator has subsequently repaired the checker/inventory link filenames without changing physical pages or source values.

Coordinator registration mapping: G001 → C001; G009 → C002; G003 → C003; G004 → C004; G007 → C005; G008 → C006; G005 → C007; G011 → C008; G012 → C009; G010 → C010; G002 → C011; G006 → C012. All included anchors and duplicate provenance are retained in the ledger.
