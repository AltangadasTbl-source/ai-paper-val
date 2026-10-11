# Evidence Quality Audit

This canonical audit covers all six stable candidates, all current coverage and source-coverage rows, the 53 numeric/reporting relationships, the 65 inferential/statistical relationships, both independent statistical passes, the complete mechanical recheck, and the agent execution manifest as it existed at audit time. It is a quality-control audit, not a scientific disposition. Every candidate remains **Pending Human Adjudication**.

### Overall coverage result

- The stable ID sets in `candidate_ledger.md` and `verification/evidence_recheck.md` are identical: C001, C002, C003, C004, C005, and C006. Each ID occurs once as a level-two candidate heading in each artifact.
- `source_coverage.md` contains four direct-source rows and 80 unique PDF-page units. For every row, reusable units are 0, fresh-required units equal total units, mapped units equal total units, and status is `COMPLETE`. Totals are 80/80 fresh-required and 80/80 mapped.
- The numeric inventory contains 53 unique relationships: N001-N037 and N300-N315. The numeric checker and cross-source checker cover all 53.
- The statistical inventory contains 65 unique relationships: S001-S053 and S300-S311. All 65 have both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`; both statistical-pass artifacts explicitly cover the same complete 65-ID set.
- Statistical pass 1 and pass 2 were performed by distinct fresh agents: `/root/statistical_pass_1` and `/root/statistical_pass_2`. Both are recorded as `gpt-5.6-terra`, reasoning effort `high`, start mode `FRESH_SPAWN`, with one distinct canonical checker artifact each.
- The execution manifest contains the coordinator and every agent manifested through this audit stage exactly once: 10 unique IDs across coordinator, preprocessing, two mapping lanes, numeric review, cross-source review, two statistical passes, evidence recheck, and this evidence-quality audit. The report generator had not yet been spawned at audit time and must be added when used.
- All existing coverage-manifest rows are `COMPLETE`, enumerate their assigned source or relationship units, and contain exactly one plain relative artifact path. Required stage rows for `evidence_quality` and `report_generation` were not yet present at audit time. Coordinator repair is required: after this artifact exists, add one `evidence_quality` row whose exact scope explicitly enumerates `C001 C002 C003 C004 C005 C006` and whose artifact is `quality/evidence_quality_audit.md`; after report assembly, add the required `report_generation` row with the same explicit ID set and its one assigned artifact path.
- No evidence artifact cites `previous_runs/`, an old candidate set, an old checker decision, or an old report as evidence. The preprocessor used the user-directed, source-hash- and page-matched OCR only as text fallback for DOC-004 pp. 3-16 after fresh native/layout extraction was unusable. The direct PDFs remain the evidence authority, and the fallback did not select pages, relationships, or candidates.
- Complete relationship processing and the six-record stable ledger show no top-N, target-count, severity, ranking, queue, or early-stop boundary. Duplicate discoveries were reconciled by printed statement, comparator, and rule before stable registration; no stable ID is deleted, suppressed, renumbered, or merged here.
- No stable candidate mentions or depends on `P = 0`, `p = 0.000`, or equivalent display-zero notation. The statistical passes explicitly report that no literal display-zero P value occurs. Therefore no conditional display-zero field is applicable to C001-C006.
- All eight unique PDF evidence links in the mechanical recheck use existing filenames and page anchors within the verified document page counts: DOC-001 pp. 3, 6, 7, and 9 of 12; DOC-003 p. 7 of 9; and DOC-004 pp. 17, 21, and 22 of 27. Their `../../../<filename>.pdf#page=N` paths resolve from the recheck directory. Final-report links must instead use `../<filename>.pdf#page=N` because the final Markdown is stored directly in `.ai_paper_validation/`.

### Final-card assembly requirements applying to every ID

The stable ledger and recheck provide the evidence needed for all six final cards, but they are not themselves the final report and do not use every exact report-card label. During report assembly, each C001-C006 card must contain all exact labels required by `report_spec.md`, including a bounded `Potential downstream evidence impact` statement and source-specific `Human verification steps`. Each card must end with exactly these blank subfields, without inferred values or prose substituted for the blanks:

```markdown
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
```

This requirement was not yet verifiable against a current final report at audit time because report generation follows this stage. It is a mandatory coordinator/report-generator repair and validation item.

## C001 — In-hospital beta-blocker adjusted-risk-difference CI endpoint differs between Table 2 and narrative

- **Audit status:** Pending Human Adjudication. Category `Statistical reporting inconsistency` follows the primary scope because two repetitions of the same named adjusted result print different CI endpoints.
- **Exact evidence and calculation:** DOC-001 PDF p. 6, Table 2 prints adjusted risk difference 6.25% with 95% CI 4.10% to 8.40%; the adjacent narrative prints 6.25% with 95% CI 4.10% to 8.10%. The OR 1.46 and its 1.29-to-1.65 CI also match. The reproduced endpoint difference is `8.40 - 8.10 = 0.30` percentage point.
- **Source-grounding and inference boundary:** The two endpoint strings and the matching result elements are direct observations. Identity as one adjusted result is a well-supported inference from the same outcome, contrast, point estimate, lower endpoint, OR, OR interval, and same-page adjustment context. A transcription or unlabelled distinct output is only an alternative interpretation; it is not asserted as the cause.
- **Missing inputs and human question:** Unrounded output, execution records, and production files are absent. The exact unresolved question is which upper confidence limit is supported by the final adjusted analysis output.
- **Duplicate review:** This relationship was discovered in S009/SP1-001. It is not a duplicate of C002, which concerns a different outcome/time point and different conflicting fields.
- **Pagination and link audit:** DOC-001 p. 6 exists; the cited Table 2 row and adjacent narrative were found directly. The recheck link resolves and ends in `#page=6`.
- **Impact boundary:** A data extractor could copy either 8.10% or 8.40% as the upper CI endpoint if the candidate is confirmed. The supplied package does not show that either value has propagated or changed a paper-level conclusion.
- **Card-field audit and repair request:** Evidence supports every required final-card field. No ledger or recheck repair is needed. The report generator must express the same-result identity as an inference, carry forward the alternative explanation and exact human verification step, use the bounded impact statement above, and append all five exact `__` adjudication blanks.

## C002 — Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative

- **Audit status:** Pending Human Adjudication. Category `Cross-document numeric inconsistency` is within the defined cross-location category, which includes main-text and table repetitions, even though both locations occur in DOC-001.
- **Exact evidence and calculation:** DOC-001 PDF p. 6, Table 2 prints adjusted risk difference 6.69% (4.43% to 8.95%) and OR 1.48 (1.30 to 1.68). DOC-001 PDF p. 7 narrative prints 6.63% with the same risk-difference interval and OR 1.47 with the same OR interval. Reproduced differences are `6.69 - 6.63 = 0.06` percentage point and `1.48 - 1.47 = 0.01`.
- **Source-grounding and inference boundary:** The differing estimates and identical intervals are direct observations. Treating the occurrences as one result is inferred from the same named discharge outcome, contrast, adjustment presentation, and interval endpoints. A different unlabelled run or output-selection/transcription issue remains possible and is not presented as fact.
- **Missing inputs and human question:** Unrounded model output, code, run/version record, and production history are absent. Human review must determine whether both locations use the same adjusted model and eligible discharge population and, if so, which estimates are supported.
- **Duplicate review:** N036/NC-001, S052/SP1-002, and XC-001 concern the same printed pairs, comparator, and exact-repetition rule and were properly consolidated as C002. S022 supplies the Table 2 side but is not a separate candidate. C001 concerns in-hospital use and a CI endpoint, so it remains distinct.
- **Pagination and link audit:** DOC-001 pp. 6 and 7 exist; both cited statements were found directly. Both recheck links resolve and end in the correct page anchors.
- **Impact boundary:** A data extractor could select 6.69%/1.48 or 6.63%/1.47 for the same named result if confirmed. No propagation, meta-analytic change, or conclusion change is established.
- **Card-field audit and repair request:** No ledger or recheck repair is needed. The final card must preserve both possible model/run interpretations, avoid calling rounding alone a proven cause, include source-specific verification of model/population/unrounded output, state bounded extraction risk, and append all five exact `__` adjudication blanks.

## C003 — eTable 1 difference footnote names groups not displayed in the table

- **Audit status:** Pending Human Adjudication. Category `Measure, label, or scale inconsistency` follows the scope because the printed contrast label conflicts with the displayed comparison groups and arithmetic direction.
- **Exact evidence and calculation:** DOC-004 PDF p. 17 displays complete-follow-up and missing-follow-up columns but footnote a says `Difference = intervention minus control`. The point differences reproduce as missing minus complete for multiple rows: age `60.0 - 60.6 = -0.6`, male percentage `71.2 - 75.8 = -4.6`, and initial troponin `4.6 - 1.3 = 3.3`.
- **Source-grounding and inference boundary:** Table title, headers, sizes, row values, point differences, and footnote are direct. A carried-over footnote is a plausible production explanation only. The package does not define every CI calculation or explicitly state the intended follow-up-group contrast order.
- **Missing inputs and human question:** The intended complete/missing comparator order, CI method, table shell, and generation code are absent. Human review must establish the contrast and sign convention for every difference and CI.
- **Duplicate review:** N308/NC-002, S305/SP1-003, and XC-002 compare the same table groups, footnote, and label rule and were properly consolidated as C003. The troponin repetition in N037/S053 is coherent and is supporting context, not a separate candidate.
- **Pagination and link audit:** DOC-004 p. 17 exists; the table, footnote, and cited values were found directly. The recheck link resolves and ends in `#page=17`.
- **Impact boundary:** If confirmed, a reviewer or structured extractor could assign the displayed differences to the wrong comparator or reverse their direction. The evidence does not show that this occurred or that any clinical conclusion changed.
- **Card-field audit and repair request:** No ledger or recheck repair is needed. The final card should keep the numeric values separate from the label defect, state that missing-minus-complete is demonstrated only for the checked point differences, request confirmation of every CI contrast, use the bounded impact statement, and append all five exact `__` adjudication blanks.

## C004 — Reported prespecified age-subgroup boundaries differ from the supplied SAP

- **Audit status:** Pending Human Adjudication. Category `Cross-document numeric inconsistency` follows the scope because numeric subgroup boundaries under a prespecified label differ between the article and supplied SAP.
- **Exact evidence and comparison:** DOC-003 PDF p. 7, section 7.5.2 prints a priori age groups `<65 years and >65 years`. DOC-001 PDF p. 3 describes reported subgroup results as prespecified; Figure 3 on p. 9 is titled `Prespecified Subgroups` and uses `<50`, `50-69`, and `>=70`. The comparison changes two groups bounded at 65 to three groups bounded at 50 and 70; neither Figure 3 boundary is 65.
- **Source-grounding and inference boundary:** Both definitions and the prespecified labels are direct observations. The possible existence of a later amendment or broader prespecification record is an alternative, not supplied evidence. The SAP's literal omission of age exactly 65 is an additional missing-definition fact, not a separate defect or a basis for resolving the final categories.
- **Missing inputs and human question:** No dated amendment, later SAP, database-lock record, or explanation of the final label is supplied. Human review must establish whether the Figure 3 categories were prespecified and what source the article's label references.
- **Duplicate review:** S038-S040 and S303/SP1-004 supply the same age-definition relationship, and the age portion of XC-003 is the same candidate. C006 uses the shared prespecified-label context but concerns a different subgroup variable and a different list mismatch, so C004 and C006 must remain separate.
- **Pagination and link audit:** DOC-003 p. 7 and DOC-001 pp. 3 and 9 all exist; the section, prose, figure title, and cut points were found directly. Each recheck link resolves and ends in the correct page anchor.
- **Impact boundary:** If confirmed, an evidence reviewer could classify the displayed age subgroup estimates or their prespecification status differently. No subgroup estimate is declared invalid, and no downstream or paper-level conclusion change is established.
- **Card-field audit and repair request:** No ledger or recheck repair is needed. The final card must not assume an amendment exists or does not exist, must retain the exact printed inequality symbols, must identify the record to retrieve, use bounded downstream wording, and append all five exact `__` adjudication blanks.

## C005 — The named optimal in-hospital medication composite uses different component labels across final-result tables

- **Audit status:** Pending Human Adjudication. Category `Measure, label, or scale inconsistency` follows the scope because the same named composite has a non-identical printed component definition.
- **Exact evidence and comparison:** DOC-001 PDF pp. 3 and 7 and DOC-004 PDF p. 21 define the composite with aspirin, an ADP-receptor antagonist, an `anticoagulant`, and a beta-blocker. DOC-004 PDF p. 22 uses the same composite name but prints `heparin` as the fourth component. Three component categories match; the fourth label is `anticoagulant` versus `heparin`.
- **Source-grounding and inference boundary:** The repeated name and component wording are direct. Whether heparin exhausted the operational anticoagulant category is not supplied and remains an alternative interpretation; the audit does not assume either equivalence or nonequivalence in the analyzed records.
- **Missing inputs and human question:** Medication coding, eligibility rules, a qualifying-anticoagulant list, and analysis/table-generation code are absent. Human review must determine whether eTable 6 used the same composite and what exact component was implemented.
- **Duplicate review:** S033, S307, S308, and SP1-005 are different locations within the same named-component identity check and were properly consolidated as C005. This does not duplicate a numeric effect disagreement because the qualifying issue is the composite definition.
- **Pagination and link audit:** DOC-001 pp. 3 and 7 and DOC-004 pp. 21 and 22 exist; all definitions were found directly. The four recheck links resolve and end in the correct page anchors.
- **Impact boundary:** If confirmed, an extractor could encode the composite as a broad anticoagulant component or a heparin-only component. The package does not establish propagation or a difference in effect estimates or conclusions.
- **Card-field audit and repair request:** No ledger or recheck repair is needed. The final card must describe the issue as a component-label substitution, preserve the possible extensional-equivalence interpretation, request the coding/eligibility definition, use bounded downstream wording, and append all five exact `__` adjudication blanks.

## C006 — Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list

- **Audit status:** Pending Human Adjudication. Category `Cross-document numeric inconsistency` is supportable because the article applies a prespecified label to quantitative hospital-type subgroup results while the supplied SAP's a priori subgroup list does not include hospital type.
- **Exact evidence and comparison:** DOC-001 PDF pp. 3 and 9 call the subgroup results prespecified and Figure 3 displays government (9 hospitals), nonprofit (12), and private (42). DOC-003 PDF p. 7 lists site-level a priori subgroups as hospital size and use of quality-improvement toolkit components; hospital type is absent. The displayed hospital-type counts reproduce the full hospital partition: `9 + 12 + 42 = 63`. This sum confirms implementation, not prespecification.
- **Source-grounding and inference boundary:** The article label, category counts, and SAP list are direct. A later amendment or separate plan is a possible but unsupplied explanation. The ledger phrase that the final set `substitutes` hospital type for toolkit-component use is stronger than the evidence: the sources establish differing lists and absence from Figure 3, not an intentional one-for-one replacement.
- **Missing inputs and human question:** No dated amendment, final SAP, database-lock record, or alternate prespecification is supplied. Human review must determine whether hospital type was prespecified and how the article's label relates to the supplied SAP list.
- **Duplicate review:** S049-S051 and S303/SP2-001 supply this hospital-type/list relationship. XC-003 originally discussed age and hospital type together, but the stable ledger correctly separates the different variable, comparison, and human question into C004 and C006. They must not be merged after stable assignment.
- **Pagination and link audit:** DOC-001 pp. 3 and 9 and DOC-003 p. 7 exist; the prose, figure categories/counts, and SAP list were found directly. Each recheck link resolves and ends in the correct page anchor.
- **Impact boundary:** If confirmed, an evidence reviewer could classify the hospital-type estimates or their prespecification status differently. The package does not establish invalid estimates, propagation, or a changed paper-level conclusion.
- **Card-field audit and repair request:** Coordinator/report-generator repair is required: replace the unsupported causal wording `substitutes` with a direct list comparison such as `the article includes hospital type and Figure 3 does not display the SAP-listed toolkit-component-use subgroup`. Preserve the amendment alternative and 63-hospital arithmetic as supporting context only, use bounded downstream wording, and append all five exact `__` adjudication blanks. No stable-ID change is authorized.

### Repair summary and limitations

- **Supportable repair requests:** (1) add the required evidence-quality coverage row for C001-C006; (2) add the report-generation coverage row and report-generator manifest row when those stages occur; (3) assemble every final card with all exact required labels and all five adjudication placeholders set to `__`; and (4) revise C006's final-card wording to report a list difference rather than an established substitution. No other candidate-specific evidence repair is needed.
- **No ID action:** No candidate is deleted, merged, ranked, suppressed, renumbered, or adjudicated. The canonical audit heading set is exactly C001-C006.
- **Limitations:** The package lacks the raw/model/production records needed to resolve C001-C002, the intended contrast and CI documentation for C003, final/amended prespecification records for C004 and C006, and medication coding/eligibility rules for C005. The final report, HTML, post-run hashes, performance/token accounting, and validator result did not yet exist at this audit stage and therefore remain coordinator completion checks rather than evidence-quality conclusions.
