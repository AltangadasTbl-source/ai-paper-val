# Evidence-Quality Audit

## Audit result

**Workflow status after coordinator repair:** `REPAIRS_COMPLETED` before report generation. All eight stable candidates are retained as **Pending Human Adjudication**; this audit makes no scientific disposition, severity assignment, ranking, deletion, suppression, merge, or renumbering decision.

- **Stable-ID coverage:** `8/8` (`C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`) occur in both `candidate_ledger.md` and `verification/evidence_recheck.md`, and every ID is returned below.
- **Direct-source coverage:** five supplied PDFs, `263/263` pages mapped. Each source row closes arithmetically: reusable plus fresh-required equals total, mapped equals total, and status is `COMPLETE`. Totals are 26 reusable, 237 fresh-required, and 263 mapped units.
- **Relationship coverage:** `N001`-`N282` and `S001`-`S101` are inventoried. Numeric checking covers `282/282`; cross-source checking covers the complete disjoint union of 282 N and 101 S relationships; both statistical passes enumerate `101/101` S relationships. The candidate ledger was not used as the discovery boundary.
- **No count boundary:** the inventories, checker scopes, and coverage records document every assigned unit without a desired count, review queue, or early-stopping rule. The eight-candidate count is an output, not a discovery limit.
- **Statistical execution:** `/root/statistics_pass_1` and `/root/statistics_pass_2` are distinct runtime IDs, each recorded as a fresh `gpt-5.6-terra`/`high` spawn with one durable artifact. Both passes cover every S ID. Pass 2 also revisits all eight stable candidates.
- **Display-zero rule:** no candidate is based on `P = 0`, `p = 0.000`, or an equivalent display zero. Both statistical passes record zero display-zero relationships. No conditional independent-contradiction field is therefore required for C001-C008.
- **Source integrity:** `sha256sum -c` reproduced all five direct-source hashes and all listed reused-artifact hashes. Existing coverage rows contain one plain relative artifact path each. The source-linked candidate PDF pages are within the verified 10-, 16-, and 153-page source bounds and resolve from the candidate ledger and recheck locations.
- **Candidate identity:** C007 and C008 are the only documented pre-ID duplicate merges; in each case the merged records concern the same printed cell or label, comparator, and rule. No remaining pair of stable IDs has the same source statement, comparator, and consistency rule.

## Required report-card field conversion

For each C ID, the ledger supplies category, source locations, printed evidence, comparison logic, an alternative, and human verification steps, but it is not yet in the exact final report-card schema. For every C ID below, the report generator must add or relabel these exact fields: **Candidate statement**, **Source evidence**, **Reported-versus-comparator**, **Reasoning procedure**, **Calculation**, **Alternative source-grounded interpretations**, **Mechanical evidence recheck**, **Quality-control relevance**, **Potential downstream evidence impact**, and **Human adjudication fields**. The report must retain the already supported **Category**, **Exact source locations**, and **Human verification steps** fields.

Every candidate's adjudication section must use exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No populated adjudication value appears in the audited candidate ledger or recheck.

## C001 — protocol timeline end date

- **Evidence quality facts:** Protocol PDF p. 11, Table 1 prints enrollment through May 2015, six-month completion through December 2015, and maximum 12-month follow-up plus a one-month window through July 2015. The page and table are found; the ledger and recheck transcriptions agree.
- **Rule and reproducibility:** Under the stated last-enrollment/month-duration reading, May 2015 plus 13 months reaches approximately June 2016. Independently, July 2015 is five months earlier than the same table's December 2015 completion of the shorter follow-up phase. Calendar ordering requires no rounding tolerance.
- **Assumption and alternative boundary:** Applying the maximum follow-up to the final enrollee is a stated diagnostic reading, not a source observation. An earlier-cohort interpretation, a typographical year, or a later amendment remains possible because exact final-enrollment date and amendment history are absent.
- **Pagination and links:** Protocol PDF p. 11 is truthful physical PDF pagination and the relative link resolves.
- **Category and duplication:** `Numeric or arithmetic inconsistency` is one allowed primary category. No other C ID uses this date statement and calendar rule.
- **Conclusion and impact boundary:** The evidence supports only a timeline-reporting question. The report may state that a protocol-date extractor could copy a conflicting follow-up endpoint if confirmed; it must not claim that observed follow-up or the paper's conclusion changed.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** None beyond exact report-card conversion.

## C002 — eligible failure total vs switching denominators

- **Evidence quality facts:** Main PDF p. 7 prints 49 of 68 eligible failures and arm fractions 20/32 and 29/42; Table 2 on p. 6 prints 32 and 42 failures; Figure 1 on p. 3 prints 20 and 29 switches. All cited pages and values are found.
- **Rule and reproducibility:** `20 + 29 = 49`, `32 + 42 = 74`, and `74 - 68 = 6`. The printed arm percentages reproduce as 62.5% and 69.0%. The unresolved point is the identity of the arm denominators within the prose's eligible population, not the arithmetic of either arm fraction.
- **Assumption and alternative boundary:** The source may intentionally use all-failure denominators for the arm fractions while using 68 for the eligible subset. The six exclusions' arm allocation and reasons are unavailable, so the card must frame a denominator-definition question rather than assert that the fractions are numerically wrong.
- **Pagination and links:** Main PDF pp. 3, 6, and 7 are truthful physical PDF pages and all relative links resolve.
- **Category and duplication:** `Denominator, proportion, or total inconsistency` is one allowed primary category. C002 is not a duplicate of the 12-month endpoint-definition candidate C004 or the adverse-event denominator candidates C006-C007 because its population and rule differ.
- **Conclusion and impact boundary:** A data extractor could attach 62.5% and 69.0% to all failures or eligible failures differently if the intended denominator is not clarified. No paper-level effect estimate or conclusion change is established.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** `candidate_ledger.md` and `checkers/cross_source_consistency.md` cite `N025`/`N026`, but the canonical numeric checker places this draft at `N010`; N025 concerns macular-thickness wording and N026 concerns injections/dose reductions. Replace the false provenance with `N010` and retain N009/Table 2/Figure 1 as supporting source relationships where useful.

## C003 — allocation block sizes

- **Evidence quality facts:** Main PDF p. 2 lists block sizes 4 and 6; Protocol PDF p. 13 lists 4, 6, or 8 with equal probability. The two source pages and printed sets are found.
- **Rule and reproducibility:** The direct set comparison is `{4,6}` versus `{4,6,8}`, with symmetric difference `{8}`. No arithmetic beyond set identity is required.
- **Assumption and alternative boundary:** Treating the 2012 protocol rule as the implementation rule is not established. The supplied SAP itself provides source-grounded version evidence: SAP PDF p. 9 and revised SAP pp. 49-50 specify block size 4 with probability 2/3 and size 6 with probability 1/3, matching the article's possible-size set. The candidate remains a cross-document reporting/version question, but that supplied alternative must not be omitted.
- **Pagination and links:** Main p. 2 and Protocol p. 13 are truthful physical PDF pages. SAP pp. 9 and 49-50 are also truthful physical pages for the omitted alternative.
- **Category and duplication:** `Cross-document numeric inconsistency` is one allowed primary category. This is distinct from C004 because it compares allocation-set definitions rather than endpoint classification.
- **Conclusion and impact boundary:** The report may say that a design extractor could record different possible block sizes depending on document version. It must not infer compromised randomization or changed trial results.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** Add the later supplied SAP evidence (`N196` and `N237`) to the alternative interpretation and human check. Remove unrelated `S001` from checker provenance; `S014` is the protocol allocation record, while the main allocation relationship must be represented precisely rather than through the primary-outcome S001 record. If N002 is retained as provenance, amend it to state the p. 2 block-size text or append and completely check a dedicated N relationship.

## C004 — six-month success injection-after-90-days criterion

- **Evidence quality facts:** Main PDF p. 3 omits injection status from its enumerated success definition and describes nonpermitted injections as protocol deviations. Protocol manual PDF p. 80, internal p. 16, Version 4.5, expressly requires no periocular or intravitreal corticosteroid injection after the first 90 days. Main PDF p. 6 reports four such cases per arm. Protocol p. 80 was visually confirmed because its native text layer is unusable.
- **Rule and reproducibility:** The matched criterion sets differ by an explicit post-day-90 injection condition. The available count is `4 + 4 = 8`; participant outcome classifications are absent, so no revised `64/96` or `56/98` numerator can be calculated.
- **Assumption and alternative boundary:** Version 4.5's applicability to the published primary endpoint and automatic mapping from protocol deviation to failure are not established. The supplied SAP adds material context: physical SAP PDF p. 70, section 3.5.1, specifies a sensitivity classification using inflammation at the injection for a corticosteroid injection at 90 days. That definition must be considered without assuming it is the primary analysis rule.
- **Pagination and links:** Main pp. 3 and 6 and Protocol p. 80 are truthful. The SAP injection section is on physical PDF p. 70, not p. 69.
- **Category and duplication:** `Cross-document numeric inconsistency` is one allowed primary category because the explicit 90-day rule affects a result classification. C004 is not a duplicate of C002; the compared statements and classification rule differ.
- **Conclusion and impact boundary:** The source supports an endpoint-definition question only. The report may state that an outcome-definition extractor could code the injection rule differently if confirmed; it must not claim that any of the eight cases changed a success count.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** Add protocol relationship `N112` and SAP relationship `N263` as relevant provenance/context. Correct N263's false page from SAP PDF p. 69 to p. 70 in the support extraction, numeric checker, and cross-source shard before citing it. The SAP wording is “90 days after enrollment”; the separate major-deviation text on the following page uses `>90 days`, so neither should be silently normalized.

## C005 — missed-dose Welch P=.87 compatibility

- **Evidence quality facts:** Main PDF p. 6 prints MTX 4.6 (SD 1.0)% under n=96 and MMF 4.3 (SD 0.5)% under n=98 with `P=.87`; p. 4 names a Welch t test. Both locations and values are found.
- **Rule and reproducibility:** Conditional on the displayed n values being row-specific and the SDs being the tested between-patient SDs, `SE = sqrt(1.0^2/96 + 0.5^2/98) = 0.113875753`, `t = 0.3/SE = 2.634450`, Welch degrees of freedom are approximately 139.06, and the two-sided diagnostic P value is approximately 0.00938. The diagnostic is incompatible with `.87` under those explicit conditions but is not a replacement analysis.
- **Assumption and alternative boundary:** Row-specific nonmissing n, unrounded inputs, transformation, weighting, participant-level observations, and row analysis output are absent. Each is named in the recheck, so no unreported mechanism or corrected P value may be asserted.
- **Pagination and links:** Main pp. 4 and 6 are truthful physical PDF pages and both relative links resolve.
- **Category and duplication:** `Statistical reporting inconsistency` is one allowed primary category. No other stable ID compares these summaries with the Welch P value.
- **Conclusion and impact boundary:** A meta-analysis or data extraction could copy the printed missed-dose P value together with apparently incompatible summaries if the row is confirmed. The evidence does not establish a changed primary outcome or paper conclusion.
- **Display-zero compliance:** This is `P=.87`, not a display-zero P value; no conditional display-zero field is required.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** None beyond exact report-card conversion and preserving the conditional diagnostic wording.

## C006 — main Table 3 MMF n=109 header vs supplement N=108/percentages

- **Evidence quality facts:** Main PDF p. 8, Table 3 prints MMF `n=109`, 19 (17.6) decreased/defective vision, and 59 (54.6) fatigue, with a footnote that one assigned patient never received MMF. Supplement eTables 4-6 on pp. 10-12 each use treated MMF `N=108`; only eTable 4 repeats the same decreased/defective-vision cell 19 (17.6). The fatigue value is an internal main-table denominator check, not an eTable 6 repeated cell.
- **Rule and reproducibility:** `100*19/108 = 17.5926%` and `100*59/108 = 54.6296%`, displaying as 17.6% and 54.6%; with 109 the corresponding values display as 17.4% and 54.1%. The calculations in the ledger and recheck are correct.
- **Assumption and alternative boundary:** The header may intentionally state randomized assignment while percentages use the 108 treated patients, with the footnote signaling the population switch. The approved table convention and row-level denominator note are absent; a mislabeled header must not be asserted as fact.
- **Pagination and links:** Main p. 8 and Supplement pp. 10-12 are truthful physical pages. All links resolve, but the comparator must not be described as the same cells across eTables 4-6.
- **Category and duplication:** The ledger currently gives two primary categories separated by a semicolon. `QUALITY_CONTROL_SCOPE.md` requires exactly one primary category. Use `Cross-document numeric inconsistency` as the primary category and describe the denominator relationship in the reasoning, without adding a second category. C006 is distinct from C007 because it concerns a table-header/population convention and different cells.
- **Conclusion and impact boundary:** A safety-table extractor could attach the printed percentages to N=109 or N=108 differently if the convention is not clarified. No adverse-event frequency or paper-level conclusion change is established.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** Correct `checkers/numeric_consistency.md` N029-N030, which currently claim Table 3 uses 107/109 denominators and that every nonzero percentage reconciles to them. Correct `checkers/cross_source_consistency.md`, which says eTables 4-6 print “the same cells.” Correct the stale sentence in `verification/evidence_recheck.md` that attributes that broad phrase to the now-repaired ledger. Expand provenance from N276-N278 to the corresponding main-table records N029, N030, and N034 as applicable.

## C007 — eTable 9 MMF serious diarrhea 1 (3.4) vs N=20

- **Evidence quality facts:** Supplement PDF p. 15, eTable 9 prints MMF `N=20`, defines entries as patients reporting at least one event (%), and gives Serious Systemic diarrhea as 1 (3.4). The cell was visually confirmed. Other N=20 count-one cells print 5.0%, while N=29 count-one cells print 3.4%.
- **Rule and reproducibility:** `100*1/20 = 5.0%` to one decimal; `100*1/29 = 3.4483%`, displaying as 3.4%. No cell-specific denominator exception is printed.
- **Assumption and alternative boundary:** A transposed percentage is plausible but inferred. An unprinted event denominator, count/header issue, or typesetting mechanism remains possible because event-level tabulation is absent.
- **Pagination and links:** Supplement p. 15 is truthful physical PDF pagination and the relative link resolves.
- **Category and duplication:** `Denominator, proportion, or total inconsistency` is one allowed primary category. The N280/N281 numeric and cross-source drafts were properly merged before C007 because they concern the same cell, N=20 comparator, and arithmetic rule.
- **Conclusion and impact boundary:** A downstream extractor could copy 3.4% as the MMF serious-diarrhea proportion if confirmed. No broader adverse-event rate or conclusion effect is established.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** None beyond exact report-card conversion.

## C008 — eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition

- **Evidence quality facts:** Supplement p. 5, eTable 1 classifies ocular hypertension at least 24 mm Hg as non-serious and surgery required as serious. Supplement p. 14, eTable 8 repeats `Ocular hypertension >24mm Hg` in both non-serious and serious sections; the serious row is MTX 1 (1.6), MMF 0 (0.0). Supplement p. 15, eTable 9 provides the additional serious label “Ocular hypertension, surgery required.”
- **Rule and reproducibility:** This is a categorical label comparison. The p. 14 serious-row label states the pressure criterion associated with the p. 5 non-serious definition rather than the surgery-required serious definition. The percentages are not the mismatch.
- **Assumption and alternative boundary:** The serious event may have required surgery despite an abbreviated or copied label. Event-level records are absent. The p. 14 footnote actually says criteria are in “eFigure 2”; no eFigure 2 content appears in the supplied supplement text. It does not direct to eTable 1.
- **Pagination and links:** Supplement pp. 5, 14, and 15 are truthful physical PDF pages and the links resolve.
- **Category and duplication:** `Measure, label, or scale inconsistency` is one allowed primary category. The N279/N282 numeric and cross-source drafts were properly merged before C008 because they use the same label, seriousness comparator, and categorical rule.
- **Conclusion and impact boundary:** A safety-data extractor could classify the displayed event differently if the label is confirmed to be incomplete. No event-level clinical consequence or paper-conclusion effect is established.
- **Missing exact report-card fields:** Candidate statement; Source evidence; Reported-versus-comparator; Reasoning procedure; Calculation; Alternative source-grounded interpretations; Mechanical evidence recheck; Quality-control relevance; Potential downstream evidence impact; Human adjudication fields.
- **Candidate-specific repair:** Correct `parts/support_supp_results_pp001_016.md`, `checkers/numeric_consistency.md`, and `checkers/cross_source_consistency.md`, all of which incorrectly say the p. 14 footnote directs to eTable 1. Preserve the repaired candidate-ledger and recheck wording: the printed target is eFigure 2, and eTable 1 is a separate supplied comparator.

## Repair completion record

The coordinator completed the seven repair groups below before report generation; the list is retained as an audit trail.

1. Repair C002 relationship provenance from unrelated N025/N026 to N010, retaining the supporting source relationships without changing C002.
2. Repair C003 provenance and alternative evidence: remove unrelated S001, represent the main p. 2 block-size relationship precisely, and add supplied SAP N196/N237 evidence from pp. 9 and 49-50.
3. Repair C004 provenance/context by adding N112 and N263, and correct the N263 injection section's false physical pagination from SAP p. 69 to p. 70 in the extraction and downstream checker records.
4. Repair C006's category to exactly one allowed primary category; repair numeric checker N029-N030, the cross-source “same cells” claim, the stale recheck attribution, and incomplete main-table provenance.
5. Repair C008's footnote target in the support extraction and both canonical checkers: the source says eFigure 2, not eTable 1.
6. Convert all eight final report cards to the exact required field labels, use the exact `__` adjudication placeholders, keep impact statements bounded, and include no severity or AI disposition.
7. Before completion, change the existing evidence-quality coverage row to `COMPLETE`; add a separate coverage-manifest row with the single artifact path `limitations.md`; add the required `report_generation` row enumerating C001-C008 and its single report artifact path; and add the fresh report-generator agent exactly once to `agent_execution_manifest.md` and the token ledger.

## Report-readiness boundary

After the seven repairs above, the stable candidate set remains C001-C008. No candidate depends only on a display-zero P value, no candidate should be deleted or suppressed, and no additional stable candidate is created by this audit. Final report readiness also depends on the coordinator's later report-generation, timing/token-accounting, hash-after, rendering, and validator stages; those artifacts did not yet exist at the evidence-quality cutoff and are not scientific limitations.
