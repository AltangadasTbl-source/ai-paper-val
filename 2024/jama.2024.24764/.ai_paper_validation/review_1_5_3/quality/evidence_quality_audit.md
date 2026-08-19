# Final Evidence-Quality Audit

## Coverage status

- **Audit status:** Complete through the evidence-quality stage, with coordinator repairs required before report generation and final validation.
- **Stable candidate set covered:** C001, C002, C003, C004, C005, C006, C007, and C008. Every ID appears in `candidate_ledger.md` and in the canonical `verification/evidence_recheck.md`; C008 also has a preserved append recheck.
- **Direct-source coverage:** Four PDFs and 114 PDF-page units are inventoried. The source ledger closes 11/11, 46/46, 9/9, and 48/48 mapped pages. Its arithmetic closes exactly: 20 reusable units plus 94 fresh-required units equals 114 total units, and 114 mapped units equals 114 total units. The main mapper covers DOC-001 pp. 1-11; the support mapper covers DOC-002 pp. 1-46, DOC-003 pp. 1-9, and DOC-004 pp. 1-48. The extraction artifacts contain page-level mapped or mapped-no-applicable records for every assigned page.
- **Relationship coverage:** The numeric inventory contains N001-N060 and the statistical inventory contains S001-S035. The numeric checker covers all 60 N records. Both statistical passes enumerate and complete all 35 S records. The cross-source checker documents its full four-source comparison scope and matched-result rules.
- **Coverage manifest paths:** Every current manifest data row contains one plain relative artifact path. The quality artifact now exists at the assigned path. The report-generation row remains pending and must be completed after the report generator is spawned.
- **Routing and agent execution:** `routing_preflight.md` reports PASS with the required fixed model/effort matrix. Statistical pass 1 is `/root/statistical_pass_1` and statistical pass 2 is `/root/statistical_pass_2`; both are distinct fresh `gpt-5.6-terra`/`high` agents with separate artifacts. All mandatory stages through this audit have distinct runtime IDs and the prescribed models and efforts. A fresh report-generator row is not yet present because that downstream stage has not started.
- **Discovery boundary:** The inventories, mapping artifacts, and checkers explicitly state complete source/relationship scope and reconstruction without a count target. No current-run discovery artifact uses an old candidate list, top-N boundary, ranking, or early-stopping rule. This is an artifact-based process confirmation; runtime conduct beyond the durable records is not independently observable.
- **Integrity and links:** Current SHA-256 checks match all four direct-source hashes and all 51 reused-artifact hashes recorded before review. The source PDFs have the recorded page counts of 11, 46, 9, and 48. Candidate PDF links resolve to supplied files and end in valid `#page=N` fragments. The C008 protocol statement is on DOC-004 PDF p. 24, not p. 25.
- **Display-zero exclusion:** No stable candidate is based on, or mentions as evidence, `P = 0`, `p = 0.000`, or equivalent. The statistical inventory and both passes record that no observed display-zero result was present. No conditional independent-contradiction field is therefore required for C001-C008.
- **Categories and tone:** Each stable ID uses one category allowed by `QUALITY_CONTROL_SCOPE.md`. The analysis-population category for C008 is tied to a concrete reported result. The records remain neutral quality-control questions and do not assign severity, scientific disposition, or a paper-level conclusion effect.

## Required coordinator repairs before report generation

1. Change the opening of `candidate_ledger.md` from “All seven records” to “All eight records.” Do not alter, merge, renumber, or suppress any stable ID.
2. Change the opening scope of canonical `verification/evidence_recheck.md` from C001-C007 to C001-C008. That canonical file already contains all eight headings.
3. Correct the C008 protocol locator in the statistical-pass-2 provenance from DOC-004 PDF p. 25 to PDF p. 24. The current ledger and canonical recheck already use p. 24. The append recheck's statement that “the C008 ledger cites” p. 25 is now stale; clarify that the original pass-2 handoff, not the current ledger, had the false locator.
4. Preserve both C008 recheck artifacts, but clarify their roles. Treat `verification/evidence_recheck.md` as the current canonical C001-C008 recheck and `verification/evidence_recheck_append_C008.md` as preserved page-correction provenance. Update the coverage-manifest scopes so they do not imply that the canonical file stops at C007 or that two competing current C008 cards exist.
5. Update the canonical statistical inventory's introductory and S008 wording that still describes the pass-2 population record as being “without a C ID”; it is now C008.
6. After report generation, enumerate C001-C008 in the report-generation coverage row, set the quality and report rows to complete, add the fresh `gpt-5.6-terra`/`medium` report-generator runtime ID to `agent_execution_manifest.md`, and perform the required timing, token-ledger, report-rendering, hash, and validation closeout.
7. Assemble every final report card with all exact report-spec labels. The ledger and recheck supply the underlying facts, but none of the pre-report records currently contains the full final-card field set. In particular, each card still needs an explicit candidate statement, reported-versus-comparator field, reasoning procedure, mechanical-recheck summary, quality-control relevance, bounded potential downstream evidence impact, human verification steps, and the exact blank human template:

   **Human adjudication fields:**

   - **Validity:** __
   - **Importance:** __
   - **Action:** __
   - **Initials:** __
   - **Notes:** __

## C001 — Smoking percentages use a different denominator from the printed smoking totals

- **Evidence and link:** DOC-001 [PDF p. 5, Table 1](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5>) contains the group headers, `Total No.` rows, six category counts, and six percentages. The link and pagination are truthful.
- **Reproduced calculation:** `220+95+90=405` and `223+70+109=402`. The printed percentages reproduce the group headers: `220/411=53.53%`, `95/411=23.11%`, `90/411=21.90%`, `223/410=54.39%`, `70/410=17.07%`, and `109/410=26.59%`. Using the printed smoking totals gives 54.32%, 23.46%, 22.22%, 55.47%, 17.41%, and 27.11%, respectively. The arithmetic in the ledger and recheck is correct.
- **Assumption boundary:** Do not state as fact that 405 and 402 must be the percentage denominators. The source-grounded observation is that the percentages use 411 and 410 even though the category counts sum to the separately printed totals; the intended convention and treatment of six and eight unclassified participants are not stated.
- **Duplicate check:** No other stable ID compares these smoking counts and denominator convention. It is distinct from the surgeon-level denominator records.
- **Card-field repair:** Add an explicit comparator field contrasting 405/402 with 411/410, a mechanical-recheck summary, a bounded quality-control relevance statement, verification steps for the table convention/missingness definition, and the blank adjudication template.
- **Impact wording:** Limit downstream impact to the possibility that a data extractor could copy different smoking prevalence or missingness denominators if the convention remains unclear. Do not claim actual propagation or any effect on the trial conclusion.

## C002 — Operating-surgeon level totals exceed participant denominators without a multi-response qualifier

- **Evidence and link:** DOC-001 [PDF p. 7, Table 2](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>) contains the participant headers and operating-surgeon rows. Pagination is truthful.
- **Reproduced calculation:** `319+123+4=446`, exceeding 411 by 35; `318+110+1=429`, exceeding 410 by 19. Printed percentages sum to 108.5% and 104.6%. The arithmetic is correct.
- **Assumption boundary:** Mutual exclusivity is not supplied. The applicable rule is conditional: the excess conflicts with a single participant category, while multiple surgeons per operation could make the rows intentionally multi-response. The final card must not call the counts wrong without the missing response-unit definition.
- **Duplicate check:** C002, C003, and C004 apply the same conditional denominator rule to different printed row families and different values. They are related but not duplicate relationships and must remain separate IDs.
- **Card-field repair:** Add the conditional reasoning procedure, explicit mechanical-recheck result, verification of whether multiple operator levels may be recorded, bounded downstream impact, and the exact blank adjudication template.
- **Impact wording:** Limit the potential impact to extraction of these rows as exclusive participant proportions or as an operator-level distribution. Do not infer an outcome-analysis or paper-conclusion effect.

## C003 — Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier

- **Evidence and link:** DOC-001 [PDF p. 7, Table 2 continuation](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>) contains the fascia-closing rows and group headers. Pagination is truthful.
- **Reproduced calculation:** `201+218+26=445`, exceeding 411 by 34; `193+225+15=433`, exceeding 410 by 23. Percentages sum to 108.2% and 105.7%. The arithmetic is correct.
- **Assumption boundary:** The rule depends on a single-response participant interpretation. Co-closure by more than one surgeon level is a source-grounded alternative, and the table does not provide the response-unit definition needed to choose between interpretations.
- **Duplicate check:** This is not a duplicate of C002 or C004 because it concerns a different table statement, printed values, and operational role. Preserve the separate stable ID.
- **Card-field repair:** Add explicit reported-versus-comparator, conditional rule, mechanical-recheck summary, unit-definition verification steps, bounded downstream impact, and the exact blank adjudication template.
- **Impact wording:** Limit downstream risk to possible extraction of the fascia-closing rows under the wrong unit or exclusivity assumption.

## C004 — Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier

- **Evidence and link:** DOC-001 [PDF p. 7, Table 2 continuation](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7>) contains the skin-closing rows and group headers. Pagination is truthful.
- **Reproduced calculation:** `115+214+96=425`, exceeding 411 by 14; `102+241+73=416`, exceeding 410 by 6. Percentages sum to 103.5% and 101.5%. The arithmetic is correct.
- **Assumption boundary:** As for C002-C003, the rule is conditional on mutually exclusive participant categories. Multiple people participating in one closure could explain the totals, but the source does not state the counting rule.
- **Duplicate check:** The relationship is related to, but not a duplicate of, C002-C003 because it uses a distinct row family and printed comparator.
- **Card-field repair:** Add explicit conditional reasoning, the mechanical result, verification of response-unit and denominator definitions, bounded downstream impact, and the exact blank adjudication template.
- **Impact wording:** Limit the potential impact to reuse of these rows as patient-level or operator-level proportions under an unsupported assumption.

## C005 — Control-arm mortality differs between participant flow and 30-day safety reporting

- **Evidence and links:** Figure 1 on DOC-001 [PDF p. 3](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=3>) reports 25 deaths, 10 and 15 by arm. The safety narrative on [PDF p. 6](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6>) and Table 3 on [PDF p. 8](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>) report 30-day mortality of 10 and 14. All links and pages are truthful.
- **Reproduced calculation:** Figure total `10+15=25`; 30-day total `10+14=24`. The intervention count agrees, and the control count differs by one. The arithmetic is correct.
- **Assumption boundary:** The Figure 1 footnote does not name a mortality window. Do not present the counts as a contradiction for the same time window unless that window is established. Frame the record around the unresolved difference between an unspecified “total deaths reported” window and an explicit 30-day window.
- **Duplicate check:** No other stable ID compares mortality counts or windows. Statistical pass 2 correctly keeps this separate from inferential relationships because no mortality effect estimate is printed.
- **Card-field repair:** Add an explicit time-window comparator, mechanical recheck, source-grounded post-day-30 alternative, event-date/window verification steps, bounded downstream impact, and the exact blank adjudication template.
- **Impact wording:** Limit potential downstream impact to extraction of a control-arm mortality count, total, or window. Do not state that mortality or the paper's conclusion is wrong.

## C006 — Longitudinal quality-of-life covariance specification differs between SAP and final article

- **Evidence and links:** The SAP on DOC-002 [PDF p. 26](<../../../joi240145supp1_prod_1741627844.87412.pdf#page=26>) states an unstructured covariance structure with robust sandwich standard errors and applies the SF-12 method to EQ-5D. The final article on DOC-001 [PDF p. 4](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4>) states an independent covariance structure. Both locators are truthful.
- **Reproduced comparison:** `Unstructured` and `independent` are distinct named working covariance specifications. Arithmetic is not applicable. The article is silent about robust sandwich variance estimation; silence is not evidence that the sandwich estimator was absent.
- **Assumption boundary:** Do not call the difference an undocumented departure, analytic error, or cause of changed P values. The package does not supply executed code/output, an amendment, or the final variance-estimation setting. A condensed or amended analysis description remains possible.
- **Duplicate check:** This is distinct from C007 and C008: C006 concerns longitudinal QoL covariance/variance specification, not the LOS effect measure or population.
- **Card-field repair:** State “not applicable” for arithmetic while preserving the logical comparison, summarize the mechanical recheck, provide execution-setting/amendment verification steps, bound downstream impact, and include the exact blank adjudication template.
- **Impact wording:** Limit potential downstream impact to extraction or interpretation of the reported QoL model specification and uncertainty method if the candidate is confirmed. Do not claim that the QoL estimates, P values, or paper conclusion changed.

## C007 — Length-of-stay effect measure and model differ between SAP/protocol and final article

- **Evidence and links:** The SAP on DOC-002 [PDF p. 25](<../../../joi240145supp1_prod_1741627844.87412.pdf#page=25>) specifies an adjusted mean difference. The protocol on DOC-004 [PDF p. 39](<../../../joi240145supp4_prod_1741627844.90412.pdf#page=39>) specifies an adjusted mean difference or, for skewed data, an unadjusted median difference. The final article on DOC-001 [PDF p. 4](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4>) describes log transformation and exponentiation; Table 3 on [PDF p. 8](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>) reports ratios of geometric means. All pages are truthful.
- **Reproduced comparison:** Mean difference and median difference are additive measures in days; ratio of geometric means is multiplicative and dimensionless. The final ratios 0.91 and 0.96 cannot be reconstructed from the printed medians/IQRs without group geometric means, model coefficients, or participant-level data. No unsupported calculation should be inserted.
- **Assumption boundary:** Do not call the final approach an error or an undocumented change. Nonnormality is printed and may have motivated a documented decision, but the supplied protocol's skewness branch names a different measure and no amendment/decision rule is supplied. Keep the UK-only 0.91 result as the population-matched comparison; reserve the all-country population question for C008.
- **Duplicate check:** C007 and C008 concern the same endpoint but different consistency rules and comparators. C007 is the effect-measure/model relationship; C008 is the analysis-population relationship. They are not duplicates.
- **Card-field repair:** Add explicit additive-versus-multiplicative comparator language, “not reproducible from aggregate printed data” for numerical reconstruction, the mechanical recheck, model-decision/amendment verification steps, bounded downstream impact, and the exact blank adjudication template.
- **Impact wording:** Limit potential downstream impact to extraction of the LOS effect measure, scale, or model label. Do not claim the reported ratios or conclusion are wrong.

## C008 — Australia-inclusive length-of-stay result differs from the stated UK-only analysis population

- **Evidence and links:** The SAP defines UK-only LOS reporting on DOC-002 [PDF p. 18](<../../../joi240145supp1_prod_1741627844.87412.pdf#page=18>) and explicitly excludes Australian-randomized participants on [PDF p. 25](<../../../joi240145supp1_prod_1741627844.87412.pdf#page=25>). The protocol statement is on DOC-004 [PDF p. 24](<../../../joi240145supp4_prod_1741627844.90412.pdf#page=24>). The final article reports the all-country result in the abstract on DOC-001 [PDF p. 1](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1>) and presents both population rows in Table 3 on [PDF p. 8](<../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8>). The current ledger and canonical recheck use the correct protocol page.
- **Reproduced comparison:** `UK patients only` is not the same analysis population as `UK and Australian patients`. No arithmetic reconstruction is required. The exact contributing treatment-by-country denominators and missing-data rules are not printed.
- **Assumption boundary:** The sources do not establish whether the all-country result was planned, amended, sensitivity, exploratory, or post hoc. Do not assign one of those labels or imply impropriety. The UK-only row remains reported, so frame the question around the status and labeling of the additional population-specific result.
- **False-pagination repair:** Statistical pass 2 originally cites DOC-004 p. 25 for the protocol statement; direct inspection and both C008 rechecks locate it on p. 24. Final reporting must cite p. 24.
- **Duplicate check:** C008 is distinct from C007 because the printed comparator and rule are population identity rather than effect-measure scale. The two C008 recheck artifacts are duplicate presentations of one stable ID, not two candidate relationships; preserve both but identify the canonical current record.
- **Card-field repair:** Add explicit population comparator, no-arithmetic statement, mechanical-recheck summary, verification steps for any later SAP/amendment plus model denominators/missingness, bounded downstream impact, and the exact blank adjudication template.
- **Impact wording:** Limit potential downstream impact to extraction or pooling of the LOS estimate under a UK-only versus all-country population label. Do not claim that the additional analysis changes the paper's conclusion.

## Limitations

- The audit can confirm durable artifacts, direct supplied-source pages, arithmetic, recorded model routing, and current hashes. It cannot independently recover unrecorded runtime conduct, participant-level data, executed analysis code, later analysis amendments, or unprinted denominator definitions.
- Exact CI/P/statistic reconstruction is unavailable where the sources omit result-specific standard errors, degrees of freedom, covariance estimates, variance estimators, or model fallback details. Diagnostic approximations in the statistical artifacts were not treated as source authority.
- The final report, HTML, token ledger and summaries, finalized timing, after-hashes, report-generator manifest row, and mechanical validation do not yet exist at this pre-report audit stage. Their completion remains a coordinator responsibility and is not claimed here.

All C001-C008 records remain **Pending Human Adjudication**.
