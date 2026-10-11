# Independent inclusion screen — statistical pass 2

Assigned scope: the sole new pass-2 finding F-ST2-501 in `checkers/parts/statistical_pass_2_support.md`; the main pass-2 checker emits no new finding. The complete `QUALITY_CONTROL_SCOPE.md`, complete review contract (including its inclusion-screen section), tooling record, current candidate ledger, initial screening artifact, and current mechanical recheck were read. The current ledger and screening/recheck were used to test overlap only; the decision below comes from the supplied sources. No legacy conclusions, external sources, count target, severity, validity, or disposition were used. The coordinator owns the canonical screening table and stable-ID assignment.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-ST2-501 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C007 |

## One-sentence justification

- **F-ST2-501:** Route A, category 5 applies because the supplied SAP expressly plans complete-case sensitivity analysis for missing primary-outcome data, while the supplied report identifies multiple imputation and hypothetical scenarios without an identifiable complete-case primary-MACE result or a definition mapping an existing result to that planned analysis.

## Included issue card for coordinator registration

### COMPLETE_CASE — Planned complete-case primary-MACE sensitivity result is not identified

**Supporting finding and provenance:** F-ST2-501, `statistics_pass_2`, support part `checkers/parts/statistical_pass_2_support.md`; underlying relationships S516, with S515/S518 and main S005 providing analysis-population/model context. This issue is distinct from C001's medication components, C002's expanded-outcome status/identity, C003's subgroup specifications, C004's time contrasts, C005's residual direction, and C006's LDL interval construction.

**Compared source locations and roles:**

- PLAN [SAP physical p.6, §7.1, lines 1190–1198, and §7.2, lines 1205–1210](../../../joi170166supp2_prod.pdf#page=6): prospective intention-to-treat and missing-outcome provisions, including complete-case analysis and multiple imputation.
- PLAN [SAP physical p.7, §7.5, lines 1229–1238](../../../joi170166supp2_prod.pdf#page=7): primary 30-day MACE and primary hospital/time mixed logistic model.
- REPORT [main physical p.3, Statistical Analysis and outcome follow-up description](../../../jama_huffman_2018_oi_170166.pdf#page=3): reported model, intention-to-treat statement, and three-contact loss-to-follow-up rule.
- REPORT [main physical p.6, follow-up paragraph beneath Table 2](../../../jama_huffman_2018_oi_170166.pdf#page=6): 295 incomplete outcomes, comprising 215 not followed by the site and 80 unreachable after three attempts; randomized-arm totals 10,066 and 11,308.
- REPORT [main physical p.7, Table 3 primary-MACE row, footnote a, and Primary Analysis paragraph](../../../jama_huffman_2018_oi_170166.pdf#page=7): reported primary effect and missing-data sensitivity summaries.
- REPORT [results supplement physical p.17, eTable 1 title, complete/missing headers and table](../../../joi170166supp3_prod.pdf#page=17): descriptive baseline comparison for complete follow-up n=21,079 and missing follow-up n=295; this is not a primary-MACE sensitivity result.
- REPORT [results supplement physical p.21, eTable 5 title, primary row, headers and footnotes](../../../joi170166supp3_prod.pdf#page=21): GRACE, transfer, insurance and prehospital-aspirin adjustment analyses.
- REPORT [results supplement physical p.22, eTable 6 title, primary row and footnotes](../../../joi170166supp3_prod.pdf#page=22): time-exposed interaction analysis.
- REPORT [results supplement physical p.23, eTable 7 title, outcome rows, headers and footnotes](../../../joi170166supp3_prod.pdf#page=23): expanded-composite and component analyses.

**Independent source comparison:** SAP §7.1 expressly assigns the subsequent missing-data methods to primary and secondary endpoints; §7.2 says sensitivity analyses will use complete-case analysis and multiple imputation to evaluate missing outcomes. SAP §7.5 identifies primary 30-day MACE. The main report says all results use intention-to-treat analysis. Its primary result is OR 0.98 (95% CI 0.80–1.21) and risk difference −0.09 percentage points (95% CI −1.32 to 1.14). The same paragraph states that results were similar after multiple imputation and describes broader but consistent results from hypothetical missing-event scenarios and multiple imputation. Neither that paragraph nor the inspected model descriptions/tables identify a complete-case primary-MACE result. Complete supplied main/results-supplement text searches found no complete-case analysis designation or mapping. Supplemental eTable 1 compares baseline characteristics by follow-up availability; eTables 5–7 identify other analyses rather than a complete-case missing-outcome sensitivity.

**Logical rule and reproduction:** The planned primary-outcome missing-data sensitivity set explicitly contains complete-case analysis and multiple imputation; the reported missing-data sensitivity set explicitly identifies multiple imputation and hypothetical scenarios without defining any reported result as the complete-case analysis. Thus a planned primary-outcome sensitivity analysis has no identified reported counterpart. This reproduces the planned-versus-reported observation within the supplied package; it does not establish that complete-case analysis was never performed. An existing result could implement the planned analysis, but the mapping is absent.

**Display precision:** The finding concerns categorical analysis availability/identity rather than a numerical comparison; recomputed rounding intervals and relative discrepancy are inapplicable. The coherent identities 21,079 + 295 = 21,374 and 10,066 + 11,308 = 21,374 do not identify the primary model's contributing population or missing-outcome coding. No complete-case event count, OR, risk difference, interval, or arm-specific complete-case total is inferred from these cohort numbers.

**Qualifying route and comparison tier:** Route A, category 5; a prespecified primary-outcome sensitivity analysis without an identified reported result is an always-register planned-versus-reported analysis observation. It is within focus area D and the protected report-versus-plan analysis-specification tier. The peripheral-comparison rule does not apply: the relevant difference is the primary-MACE missing-outcome sensitivity analysis, rather than a copied baseline value, isolated contributor count, pointer, calendar or administrative detail.

**Affected result or extracted value:** Availability, identity and analysis population of the SAP-prespecified complete-case sensitivity estimate for the primary 30-day MACE intervention effect, alongside the reported primary OR 0.98 (0.80–1.21) and risk difference −0.09 percentage points (−1.32 to 1.14). The supplied evidence does not show that reporting the complete-case result would change the overall trial conclusion.

**Proposed classification:** Review domain `protocol_report`; primary relationship type `P_R`; all relationships `P_R`; compared roles PLAN SAP versus REPORT main and trial-results supplement. The report locations jointly establish what is reported and do not conflict with one another, so they add no `S_C` or `S_W` relationship. SAP p.7 is supporting primary-endpoint/model context, not a plan-internal conflict. No role ambiguity is present.

**Why context does not remove the issue:** Route A category 5 directly applies. Intention-to-treat describes assignment/analysis principles but does not specify how missing outcomes entered the primary model. Full cohort table headers and the complete/missing descriptive table do not supply that model definition. A named imputation result or an unspecified hypothetical scenario also does not, by itself, identify the planned complete-case analysis.

**Source-grounded alternatives and exact missing definitions:** The reported primary model may itself have used complete cases while retaining full cohort descriptive headings; a hypothetical scenario could implement complete-case analysis; or the planned sensitivity may have been replaced or deferred. These alternatives remain possible because the report does not define the primary model's inclusion/coding of the 295 missing outcomes or the hypothetical scenarios. The missing elements are the complete-case outcome-availability rule and contributing population, the result or narrative result identified as that sensitivity analysis, the mapping from any existing primary/scenario result to complete-case analysis, and any supplied documentation of replacement or deferral. No alternative is assumed.

**Exclusion rationale and consolidation:** This is not solely an unreported imputation-model detail: the supplied plan explicitly names the primary-outcome analysis to be reported, bringing it under Route A category 5. It is not duplicated by the current six candidates, whose rules and results differ. No independent issue is added for imputation-model internals, hypothetical-scenario internals alone, or the conditionally planned hospital-imbalance sensitivity. Those elements supply no separate reproduced conflict in this assigned finding.

**Exact human question:** Where is the SAP-prespecified complete-case sensitivity analysis for primary 30-day MACE reported, with its contributing population and result, or which reported primary/scenario analysis implements it and what supplied definition establishes that mapping?

**Status:** Pending Human Adjudication.

## Direct-source reread, derivatives and limitations

Fresh direct Poppler 25.03.0 `pdftotext -layout` derivatives were created on CPU from the supplied main article and complete results supplement as `preprocessing/screen2/main-layout.txt` and `preprocessing/screen2/supp3-layout.txt`, and SAP pp.6–7 as `preprocessing/screen2/sap6-7-layout.txt`. These derivatives locate text and support complete-report term searches; current-source images provide final authority for the cited statements and table identities. Inspected current-source images were `preprocessing/st2-support/sap6.png`, `preprocessing/curator/sap7.png`, `preprocessing/curator/main3.png`, `preprocessing/curator/main-6.png`, `preprocessing/curator/main-7.png`, and `preprocessing/curator/supp3-17.png`, `supp3-21.png`, `supp3-22.png`, `supp3-23.png`. Existing images and assets were preserved. No new rendering, OCR, fallback installation, Python review, external data or web was needed.

Exact derivative commands, from the package root:

```bash
pdftotext -layout jama_huffman_2018_oi_170166.pdf .ai_paper_validation/review_1_6_2/preprocessing/screen2/main-layout.txt
pdftotext -layout joi170166supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/screen2/supp3-layout.txt
pdftotext -f 6 -l 7 -layout joi170166supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/screen2/sap6-7-layout.txt
```

All cited locations were available. The only issue-specific limitation is the absent complete-case result/population and model/scenario mapping; the absence statement is confined to supplied REPORT materials. It does not imply absence from external publications, unsupplied code, or other records.

Counts: findings 1; INCLUDE rows 1; distinct included issues 1; SCREENED_OUT findings 0. Screened-out counts by reason: NOT_REPRODUCED 0; ROUNDING_OR_DISPLAY_PRECISION 0; NOTATION_OR_TYPOGRAPHY 0; TERMINOLOGY_OR_WORDING 0; MODEL_VERSUS_CRUDE 0; CONTEXT_RESOLVES 0; CONDITIONAL_OR_UNREPORTED 0; PERIPHERAL_COMPARISON 0; OUT_OF_FOCUS 0; DUPLICATE_OF_INCLUDED 0.
