# Final Evidence-Quality Audit

**Audit status:** PASS FOR REPORT ASSEMBLY. The scientific coverage, relationship coverage, stable-candidate identity, and mechanical evidence requirements are complete. The coordinator must perform the two normal post-audit state transitions recorded below when updating `coverage_manifest.md`: enumerate `C001, C002, C003` and mark the `evidence_quality` row `COMPLETE`, then enumerate the same IDs and mark `report_generation` `COMPLETE` only after the report exists. These are workflow-state updates, not scientific-coverage gaps.

## Audited scope and global findings

- **Direct-source coverage:** 3/3 PDFs and 176/176 PDF pages are mapped. The source rows close exactly: DOC-001 `11 = 11 reusable + 0 fresh`; DOC-002 `136 = 0 reusable + 136 fresh`; DOC-003 `29 = 26 reusable + 3 fresh`. Package totals are `176 = 37 reusable + 139 fresh-required`, and mapped units are 176. Every source row is `COMPLETE`.
- **Mapping coverage:** the main-paper shard covers DOC-001 pp. 1-11; five disjoint DOC-002 shards cover pp. 1-28, 29-56, 57-84, 85-112, and 113-136; the DOC-003 shard covers pp. 1-29. The parts form a complete, nonoverlapping union of the three sources. Every reusable gap was assigned to fresh direct-source mapping; no scientific-coverage gap remains.
- **Relationship coverage:** 33/33 numeric/reporting relationships (`N001`-`N033`) have explicit numeric-check records. Both statistical passes contain 34/34 explicit relationship records (`S001`-`S034`), and the cross-source checker covers all 33 N relationships plus all 34 S relationships. Pass 2 also reconciles all three stable candidates and every recheck fact.
- **Discovery boundary:** the inventories, mapper outputs, checker records, and ledger explicitly document complete discovery without a candidate limit. Reused artifacts were used as locators and transcription aids; old candidate, checker, verifier, critic, endetail, and report records did not control source scope or discovery. No top-N or former 10-candidate boundary is present in the new scientific artifacts.
- **Stable-ID identity:** the ledger and mechanical recheck sets are both exactly `C001, C002, C003`; this audit returns exactly the same set. No ID was deleted, merged after assignment, renumbered, ranked, or given a scientific disposition. Every candidate remains **Pending Human Adjudication**.
- **Statistical-agent requirement:** pass 1 is runtime agent `/root/statistical_pass_1` and pass 2 is the distinct runtime agent `/root/statistical_pass_2`; both are recorded as fresh `gpt-5.6-terra` agents at high reasoning effort. Their artifacts explicitly cover `S001`-`S034` and record `PASS_1_COMPLETE` and `PASS_2_COMPLETE` for every relationship.
- **Execution manifest:** the manifest contains 16 unique rows through this audit: the coordinator and every curator, mapper, consolidator, checker, rechecker, statistical reviewer, and auditor used so far, each exactly once with one primary artifact. The later report-generator agent must be appended exactly once when spawned.
- **Coverage-manifest path rule:** all 17 current manifest rows contain one plain relative artifact path per row; no cell contains multiple paths, prose, a Markdown link, a comma-separated path set, or a semicolon-separated path set. Fifteen predecessor rows are `COMPLETE`; the audit and report rows require the stage transitions described above.
- **Source integrity and links:** all three direct-source SHA-256 records rechecked successfully, and the reused-asset hash check returned the listed assets unchanged. Candidate evidence links resolve to existing supplied PDFs and use physical-PDF fragments ending in `#page=N`.
- **Resolved provenance repair:** C001 is physically on DOC-001 PDF p. 6 (printed article p. 403). During this audit, the formerly incorrect p. 5 location was repaired in the main mapping part and canonical extraction, numeric relationship inventory, statistical relationship inventory, and statistical pass-1 observation. The ledger, numeric checker, cross-source checker, and recheck already used PDF p. 6. No false candidate pagination remains in the current canonical artifacts.
- **Display-zero exclusion:** no stable candidate is based on `P = 0`, `P = .000`, underflow, finite precision, or nonzero-tail reasoning. The statistical records distinguish prospective `P < .05` and `P < .001` thresholds from display-zero results. The signed rounded risk difference `-0` in S015 is not a P value. No candidate card mentions a display-zero P value, so the conditional independent-contradiction field is not applicable.
- **Categories and tone:** each stable ID uses the normative category `Measure, label, or scale inconsistency`. The observations are direct label, unit, or reference-identity checks tied to quantitative evidence. Wording remains neutral, separates observation from explanation, makes no paper-level conclusion claim, and assigns no severity, validity, acceptance, rejection, or correction.

## C001 — Extraneous pressure unit after the usual-group SpO2 summary

**Evidence-quality assessment:** Mechanically supported and report-ready after applying the field instructions below. The main-paper string and supplement comparator are exact, the physical pagination is now consistent, and the candidate is not an inferential-result contradiction.

- **Evidence and links:** [DOC-001 PDF p. 6, Oxygen Exposure paragraph](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=6) prints `95.1% (2.4%) mm Hg` as the first usual-group value in a sentence pairing SpO2 and PaO2 “respectively.” [DOC-003 PDF p. 21, eTable 5](../../../joi250042supp2_prod_1753377747.93025.pdf#page=21) labels `95.1 (2.4)` as SpO2 on a percent scale and `79.5 (17.9)` as PaO2 in mm Hg.
- **Reproducibility and calculation:** no arithmetic is needed. The reproducible logical pairing is first measure/value = SpO2/percent and second measure/value = PaO2/mm Hg for each arm. The extra pressure unit is printed immediately after the usual-arm SpO2 summary. The recheck confirms the source text, comparator text, rule, available inputs, and remaining human question.
- **Unsupported assumptions:** none are required to observe the printed unit conflict. A typesetting carryover, unit displacement, or production error is only a possible explanation and must not be stated as established. The alternative visual reading that the pressure unit was intended to anticipate the following PaO2 phrase must remain explicit.
- **Relationship/provenance boundary:** N014 is the substantive relationship supporting the candidate. S004 and S012 record the statistical review context in which the duplicate observation was noticed; they do not establish a primary-outcome, P-value, model, or inferential contradiction. The report card must not imply that C001 challenges the mortality estimate or statistical analysis.
- **Duplicate review:** mapper O-001, numeric Observation 1, statistical-pass-1 SP1-O001, and cross-source Observation 1 compare the same printed string, comparator, and unit-pairing rule. Their merger into C001 is genuine and preserves all checker provenance.
- **Conclusion and downstream wording:** state only that the printed unit placement is a candidate consistency issue. A bounded downstream statement may say that an extractor could copy the SpO2 summary with a pressure unit if the candidate is confirmed; do not claim that extraction error, evidence propagation, or conclusion change has occurred.
- **Final-card field repair:** explicitly populate `Candidate statement`, `Category`, `Exact source locations`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation` (state “No arithmetic; logical unit pairing reproduced”), `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, and `Human verification steps`. The ledger contains the underlying content but not all final-report labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

**Status:** Pending Human Adjudication

## C002 — Results-supplement contents page does not identify actual eTables 1–4

**Evidence-quality assessment:** Mechanically supported and report-ready after applying the field instructions below. All eight number-title pairs and all physical PDF pages are available, and the four mismatches are one document-identity relationship rather than four separately ranked findings.

- **Evidence and links:** [DOC-003 PDF p. 1, contents](../../../joi250042supp2_prod_1753377747.93025.pdf#page=1) identifies eTables 1-4 as quality assessment, serological-test combinations, patients randomized by site, and additional patient characteristics. The actual headings are [eTable 1 on PDF p. 15](../../../joi250042supp2_prod_1753377747.93025.pdf#page=15), [eTable 2 on p. 17](../../../joi250042supp2_prod_1753377747.93025.pdf#page=17), [eTable 3 on p. 18](../../../joi250042supp2_prod_1753377747.93025.pdf#page=18), and [eTable 4 on p. 19](../../../joi250042supp2_prod_1753377747.93025.pdf#page=19), with the four titles transcribed in the ledger and recheck.
- **Reproducibility and calculation:** this is an identity comparison, not arithmetic. Match table number 1, 2, 3, and 4 between the contents and actual heading; none of the four titles agrees with its same-numbered actual table. The recheck also records that the contents eTable 3 topic equals actual eTable 1 and the contents eTable 4 topic approximates actual eTable 2.
- **Unsupported assumptions:** none are required for the four observed identity mismatches. A stale template, retained content from another supplement, or a two-position shift is an inferred production explanation only. The report must not assert a mechanism or presume the intended replacement wording beyond the headings printed in the supplied PDF.
- **Duplicate review:** the four title mismatches share the same contents list, same comparator set, and same table-number/title identity rule. Their registration as one C002 candidate is supportable. C002 is not duplicative of C003: C002 compares wrong table identities, whereas C003 concerns one unresolved internal reference target.
- **Conclusion and downstream wording:** state only that the contents entries do not identify the same-numbered printed tables. A bounded downstream statement may say that a reviewer or extractor relying on the contents page could cite or open the wrong table if the candidate is confirmed; do not claim that mis-citation or evidence propagation has occurred.
- **Final-card field repair:** explicitly populate every required final-report field. For `Calculation`, state “No arithmetic; four same-number identity comparisons reproduced.” For `Human verification steps`, require comparison with the approved supplement contents or production source without assuming that the actual table bodies require alteration.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

**Status:** Pending Human Adjudication

## C003 — Final SAP contains an unresolved reference after quantitative separation/adherence rules

**Evidence-quality assessment:** Mechanically supported and report-ready after applying the field instructions below. The direct rendered source visibly contains the unresolved-reference string after quantitative threshold and adherence definitions. The existence of the reference failure is observed; the importance or content of its intended target remains unknown.

- **Evidence and link:** [DOC-002 PDF p. 118, SAP p. 8](../../../joi250042supp1_prod_1753377747.92525.pdf#page=118) visibly prints `See Section 3.2 and Error! Reference source not found.` immediately after Table 1, traffic-light thresholds, and the treatment-adherence definition. The page also separately identifies Section 3.2 and a Section 3.2.2 caveat.
- **Reproducibility and calculation:** no numeric recalculation is needed. The logical check identifies two promised destinations joined by “and”: Section 3.2 resolves, while the second destination is replaced by literal error text and therefore cannot be located. The recheck accurately marks comparator matching as partial and names the missing input: the intended second destination and its content.
- **Unsupported assumptions:** the report must not assert that the missing target necessarily contains an additional quantitative definition, changes a threshold, or prevents application of the rule. It may state only that the promised second source of further details cannot be identified. An unrefreshed Word field is a possible production explanation, not a source-established fact.
- **Duplicate review:** N030 supplies the adjacent quantitative threshold context and N033 tracks the broken reference. The DOC-002 mapper observation, numeric Observation 3, cross-source Observation 3, and pass-2 duplicate note concern the same string and reference-resolution rule; their merger into C003 is genuine. C003 is distinct from C002 for the reason stated above.
- **Conclusion and downstream wording:** state the unresolved cross-reference as a candidate quantitative-definition navigation issue. A bounded downstream statement may say that a reviewer applying or extracting the thresholds could lack the promised second detail source if the candidate is confirmed; do not claim that anyone has misapplied a threshold or that a trial result is affected.
- **Final-card field repair:** explicitly populate every required final-report field. For `Calculation`, state “No arithmetic; one of two stated reference destinations is identifiable and the other is not.” The `Alternative source-grounded interpretations` field must say that Sections 3.2 and 3.2.2 may already supply sufficient detail. `Human verification steps` should request the approved SAP/Word cross-reference field and a check of whether the missing target adds any definition.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

**Status:** Pending Human Adjudication

## Report-readiness handoff

- Include all and only `C001`, `C002`, and `C003` in the candidate index and evidence-card section. The ledger, recheck, audit, and report ID sets must remain identical.
- Preserve the correct physical page links above. Do not reintroduce the repaired DOC-001 p. 5 location for C001.
- Use all exact required bold evidence-card labels from `report_spec.md`, including a bounded `Potential downstream evidence impact` and the five exact `__` human-adjudication placeholders for every card.
- Do not add an `Independent contradiction beyond P=0 display` field to these cards because none mentions or depends on a display-zero P value.
- Preserve **Pending Human Adjudication** and neutral quality-control language. Do not add severity, validity, acceptance, rejection, scientific disposition, or an asserted correction.
- Remaining non-scientific completion work is coordinator-owned: complete the two coverage-manifest stage transitions, append the report-generator execution row, assemble the full Markdown report, close timing/token accounting, recompute final hashes, render the standalone HTML, and run the versioned validator.

## Limitations

- Graph-only ordinates and bin heights that are not printed as exact values were not digitized; this does not create a source-unit or relationship-coverage gap.
- Several secondary-outcome P values cannot be exactly reconstructed because the supplied article does not fully identify their test scale, variance, covariance, degrees of freedom, or imputation-combination rule. Both statistical passes correctly retained those missing definitions without manufacturing candidates.
- DOC-002 native text is glyph-mapped; direct rendered inspection supplied authoritative evidence for C003. The later DOC-002 mapping limitation concerns transcription granularity in planning/administrative pages, not mapped-page closure.
- Final timing, token-accounting, report-generation, HTML-rendering, and validator status are necessarily unavailable at this pre-report audit stage and must be finalized after the report-generator response.
