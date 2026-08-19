# Evidence-Quality and Complete-Coverage Audit

## Audit status and scope

**Coverage status:** Scientific coverage is complete. Artifact closure requires the coordinator repairs listed below.

This audit examined the complete direct-source and evidence-asset inventories, `source_coverage.md`, `coverage_manifest.md`, both canonical quantitative extraction maps, the numeric and statistical relationship inventories, the numeric and cross-source checker outputs, both statistical passes, `candidate_ledger.md`, `verification/evidence_recheck.md`, and `agent_execution_manifest.md`. It also independently reopened the exact supplied-PDF locations for C001, C002, and C003. All three stable candidates remain **Pending Human Adjudication**.

## Complete-coverage findings

- The four direct sources contain 91 stable PDF-page units: DOC-001 has 10, DOC-002 has 31, DOC-003 has 48, and DOC-004 has 2. The source hashes still match `source_hashes_before.sha256`.
- There were no eligible pre-existing reusable evidence assets. The source ledger therefore partitions every row as zero reusable units plus all units fresh-required: `0 + 10 = 10`, `0 + 31 = 31`, `0 + 48 = 48`, and `0 + 2 = 2`. Mapped units equal total units in every row, for 91 fresh-required and 91 mapped units overall.
- The mapping artifacts explicitly cover DOC-001 pages 1-10, DOC-002 pages 1-31, DOC-003 pages 1-48, and DOC-004 pages 1-2. Pages without an applicable result receive explicit no-applicable-unit records. No scientific-coverage gap remains.
- The numeric inventory contains all 53 assigned N relationships: N001-N010, N100-N121, N300-N308, and N500-N511. The numeric checker returns all 53 and also checks the numeric implications of all 35 S relationships.
- The statistical inventory contains all 35 assigned S relationships: S001-S004, S100-S113, S300-S307, and S500-S508. Both statistical checker artifacts enumerate the same 35 IDs once each and mark every relationship `PASS_1_COMPLETE` or `PASS_2_COMPLETE`, respectively.
- Statistical pass 1 and pass 2 were performed by distinct fresh agents, `/root/statistics_pass_1` and `/root/statistics_pass_2`. `agent_execution_manifest.md` records both as `gpt-5.6-terra`, high reasoning effort, and `FRESH_SPAWN`, with one primary artifact each.
- The cross-source checker covers all 88 N/S relationships and 15 matched cross-location families. The stable ID sets in the candidate ledger and mechanical recheck are identical: C001, C002, and C003.
- The discovery record is source-first and relationship-complete. The source inventory states that legacy candidate, queue, decision, and report records were not used as discovery inputs; all 91 direct units were freshly mapped; every N and S relationship was checked; and the candidate ledger states that there was no candidate cap. The three-candidate result is not evidence of a top-N boundary or count-based suppression.
- Every completed coverage-manifest row currently has exactly one plain relative artifact path, and each completed path resolves. The evidence-quality row will resolve to this artifact. The report-generation artifact does not yet exist.
- No registered candidate mentions or depends on `P = 0`, `p = 0.000`, or an equivalent display zero. Both statistical passes state that no such display occurred in the 35-relationship inventory. No conditional independent-contradiction field is required for C001-C003.

## Reproducibility and relationship reconciliation

- Candidate evidence links resolve to existing PDFs and valid page numbers. The source-level statements and comparators for all three candidates were independently found in fresh direct-PDF text and in the targeted rendered pages retained by the mechanical rechecker.
- Key arithmetic was reproduced independently. For C001, `630 + 698 = 1,328`, `5,739 + 5,678 = 11,417`, and `1,328 / 11,417 × 100 = 11.6318%`, which rounds to `11.6%`. This connects the narrative percentage to the `<20 ng/mL` baseline category. The dimensional diagnostic `20 mg/mL × 1,000,000 ng/mg = 20,000,000 ng/mL` is correct and is not presented as an inferred corrected value.
- The other recorded additive identities also reconcile, including randomized and risk-set totals, incident-plus-recurrent event totals, participant-flow subtraction, protocol demographic and power-table partitions, adherence percentages, sensitivity-analysis event partitions, sex-specific partitions, and the 11,417-person biomarker partition.
- Statistical calculations remain appropriately bounded. The source does not supply the unrounded coefficients, standard errors, covariance matrices, complete test statistics, variance estimators, sidedness, or person-time totals needed to reconstruct most inferential results or rates. Both passes use rounded-CI calculations only as labelled diagnostics and do not infer missing model definitions.
- Repeated values from different censoring, adjustment, competing-risk, exposure-scale, or time-window models are retained as distinct relationships rather than treated as duplicates. Candidate-level duplicate handling is appropriate: C001 combines the same unit proposition referred by numeric, statistical cross-lane, and cross-source checks; C002 combines the same table-locator proposition referred by those lanes; and C003 is the single cross-document locator proposition associated with S301. No second stable ID duplicates any of these rules and comparators.

## C001 — Vitamin-D concentration unit differs at the 20-unit baseline threshold

- **Status:** Pending Human Adjudication.
- **Category check:** `Measure, label, or scale inconsistency` is an allowed primary category and matches the printed concentration-unit conflict.
- **Direct source check:** [DOC-001 PDF p. 6](<../../../jama_okereke_2020_oi_200066.pdf#page=6>) prints a mean of `31.1 ng/mL` and then `11.6%` below `20 mg/mL`. [DOC-001 PDF p. 4](<../../../jama_okereke_2020_oi_200066.pdf#page=4>) and [DOC-001 PDF p. 8](<../../../jama_okereke_2020_oi_200066.pdf#page=8>) identify the corresponding 20 threshold in `ng/mL`. Supplement 2 separately prints the same low-vitamin-D definition on [PDF p. 38](<../../../joi200066supp2_prod.pdf#page=38>), [PDF p. 39](<../../../joi200066supp2_prod.pdf#page=39>), and [PDF p. 40](<../../../joi200066supp2_prod.pdf#page=40>).
- **Rule, arithmetic, and assumptions:** The same analyte and empirically linked threshold require a consistent concentration unit absent an explicit conversion or different definition. The count calculation reproduces the 11.6% narrative from the `<20 ng/mL` category. The printed mismatch is directly observed. The intended unit and any production mechanism remain unknown; the artifacts appropriately present a transcription or production explanation only as a possibility.
- **Alternative interpretation:** A different unstated analytic unit is logically possible but is not supported elsewhere in the supplied package. The same sentence, baseline table, subgroup figure, protocol threshold, and supplementary analyses use `ng/mL` for the matched quantity.
- **Duplicate and provenance check:** N009, S300/S301/S506 implications, numeric Proposition 1, the pass-1 cross-lane referral, the cross-source proposition, and the pass-2/recheck records concern the same unit comparator. Their consolidation into C001 before stable numbering preserves every relevant location and checker provenance without creating a duplicate stable ID.
- **Pagination check:** The candidate-ledger link labelled `PDF pp. 38-40` anchors only `#page=38`. The evidence itself is present on all three pages and the recheck links them separately, so this is a link-label precision defect rather than an evidence gap. The coordinator should replace the plural single-anchor citation with separate page-38, page-39, and page-40 links.
- **Evidence-card field audit:** The ledger and recheck together supply a candidate statement, allowed category, exact locations, printed evidence, comparator, rule, calculation, source-grounded alternatives, mechanical recheck, and exact human question. The numeric and cross-source checkers supply bounded quality-control relevance and human checking steps. The final report must still assemble these under every exact report-card label, state only the bounded possibility that an extractor could copy the wrong threshold unit, and include the blank adjudication template below. No paper-level conclusion change is established.
- **Unsupported or unbounded content:** None beyond the pagination repair. The card must not state that `ng/mL` is authoritatively intended unless an external production or author record is later supplied.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Protocol ICD-9-code prose cites Table 3 while the code list is Table 1

- **Status:** Pending Human Adjudication.
- **Category check:** `Measure, label, or scale inconsistency` is an allowed primary category and is used here for the printed table-reference label.
- **Direct source check:** [DOC-002 PDF p. 18](<../../../joi200066supp1_prod.pdf#page=18>) prints `ICD-9 codes will be used to identify depression (Table 3)` immediately above `Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders`. [DOC-002 PDF p. 23](<../../../joi200066supp1_prod.pdf#page=23>) identifies Table 3 as a recurrent-depression power table.
- **Rule, arithmetic, and assumptions:** The logical comparison `Table 3 ≠ Table 1` is reproducible, and the displayed Table 3 has power quantities rather than ICD-9 codes. No numeric tolerance applies. The evidence establishes the locator/content mismatch but not which printed field should change.
- **Alternative interpretation:** The reference may reflect an earlier numbering scheme, or the adjacent caption may have been renumbered. Appendix C may contain a longer code list, but the supplied text does not identify Appendix C itself as Table 3 and the supplied Table 3 is not a code list.
- **Duplicate and provenance check:** N121, numeric Proposition 2, the pass-1 cross-lane referral, and the cross-source proposition compare the same sentence, table caption, and locator rule. Their consolidation into C002 before stable numbering is appropriate and preserves provenance.
- **Pagination check:** Both PDF links resolve to the cited pages and their labels match their anchors. No false page location was found.
- **Evidence-card field audit:** The ledger and recheck together supply a candidate statement, allowed category, exact locations, evidence, comparator, rule, logical calculation, alternatives, mechanical recheck, and exact human question. The checkers supply bounded quality-control relevance and human checking steps. The final report must assemble the exact labelled card, limit downstream impact to the possibility that a reader or extractor could follow the wrong table locator, and include the blank adjudication template below. No effect on a reported trial estimate or paper-level conclusion is established.
- **Unsupported or unbounded content:** None. Any statement that Table 1 is the intended final locator remains conditional until version or production records establish intent.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Supplementary depression-risk subgroup narrative refers to main Figure 3, but its printed values match main Figure 4

- **Status:** Pending Human Adjudication.
- **Category check:** `Cross-document numeric inconsistency` is an allowed primary category. Here it is grounded in a cross-document figure locator whose four printed numerical results identify a different main figure.
- **Direct source check:** [DOC-003 PDF p. 13](<../../../joi200066supp2_prod.pdf#page=13>) prints the heading `Description of Results from Sub-Group Analyses in Figure 3 and eTable 2`, the phrase `main Figure 3`, and the values `.10`, `.06`, `0.87 (0.73-1.04)`, and `0.89 (0.77-1.04)`. [DOC-001 PDF p. 8](<../../../jama_okereke_2020_oi_200066.pdf#page=8>) Figure 4 prints all four matched depression-risk subgroup values. [DOC-001 PDF p. 7](<../../../jama_okereke_2020_oi_200066.pdf#page=7>) Figure 3 is a crude PHQ-8 score-distribution figure and does not print those values.
- **Rule, arithmetic, and assumptions:** Population, outcome, treatment contrast, subgroup, effect measure, and displayed precision match Figure 4. The four exact displayed-value identities reproduce the comparison; Figure 3 supplies none of them. The mismatch is directly observed, while the intended figure number and production history remain unknown.
- **Alternative interpretation:** An earlier main-article layout could have numbered the depression-risk figure as Figure 3. No such version is supplied, so this remains an unresolved source-grounded possibility rather than an explanation established by the package.
- **Duplicate and provenance check:** S301 contains the inferential relationship, the cross-source checker registers the locator proposition, pass 2 considers its statistical implications, and the rechecker confirms the source facts. No numeric or statistical checker created a separate stable proposition for the same comparator, so C003 is not duplicated.
- **Pagination check:** All three PDF links resolve and their page labels match their anchors. No false page location was found.
- **Evidence-card field audit:** The ledger and recheck together supply a candidate statement, allowed category, exact locations, evidence, comparator, rule, calculation by exact value matching, alternatives, mechanical recheck, and exact human question. The cross-source checker supplies human checking steps. The final report must add explicit bounded quality-control relevance and downstream-impact wording: if confirmed, an extractor could attribute the subgroup HRs and interaction P values to the wrong main figure. It must not claim that the subgroup estimates themselves differ, propagated elsewhere, or change the paper-level conclusion. The blank adjudication template below is required.
- **Unsupported or unbounded content:** None in the present artifacts. The phrase `wrong main-article figure` should remain a candidate statement subject to the unresolved prior-layout alternative, not a final production determination.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Coordinator repairs and remaining limitations

1. In `coverage_manifest.md`, change the `evidence_quality` exact scope to `C001, C002, C003` and its status to `COMPLETE` after accepting this artifact. Retain the single artifact path `quality/evidence_quality_audit.md`.
2. When report generation is complete, change the `report_generation` exact scope to `C001, C002, C003`, retain its single relative artifact path, and set the row to `COMPLETE`. The report artifact is not present at this audit cutoff.
3. Repair C001's plural Supplement 2 citation in `candidate_ledger.md` by using separate links for PDF pages 38, 39, and 40. Do not alter, combine, renumber, or suppress C001.
4. The direct-source paths, hashes, and page counts in `source_inventory.md` are correct, but its descriptive notes call DOC-003 a statistical analysis plan and DOC-004 a supplementary figure source. The mapped contents identify DOC-003 as Supplement 2 with eTables/eMethods and DOC-004 as the data-sharing statement. Correct these two descriptive notes without changing source IDs or coverage counts.
5. The canonical statistical-inventory header records completed two-pass status for all 35 S IDs, while retained mapper-stage sections still contain historical `PASS_1_PENDING; PASS_2_PENDING` cells. The pass artifacts establish current completion. The coordinator should either relabel those cells as mapper-stage snapshots or update them to prevent the final report from presenting them as current status.
6. The final report does not yet exist, so its exact card labels, bounded downstream-impact fields, blank human-adjudication subfields, complete C-ID set, local links, and report-generation coverage row remain to be checked by report assembly and final validation.
7. `run_state.md` still contains initialization-era workflow statuses and blank completion fields. These are outside the scientific candidate findings but must be finalized after Markdown report assembly as required by the workflow.

## Audit completion record

- **Direct-source units covered:** 91 of 91.
- **Numeric relationships covered:** 53 of 53.
- **Statistical relationships covered in each pass:** 35 of 35.
- **Stable candidates returned:** C001, C002, C003.
- **Candidate count:** 3.
- **Display-zero-only candidates:** 0.
- **Candidate status:** Pending Human Adjudication for every stable ID.
- **Artifact path:** `.ai_paper_validation/review_1_5_1/quality/evidence_quality_audit.md`.
