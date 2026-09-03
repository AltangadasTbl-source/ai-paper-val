# Final Evidence-Quality Audit

This audit covers the complete Workflow 1.5.1 pre-report evidence chain. It is a quality-control record, not a scientific disposition. Every stable candidate remains **Pending Human Adjudication**.

## Coverage and execution audit

- **Direct-source closure:** Five supplied PDFs contain 272 source pages. `source_coverage.md` closes every row: 27 reusable units plus 245 fresh-required units equals 272 total units, and 272 mapped units equals 272 total units. Each of DOC-001 through DOC-005 is `COMPLETE`.
- **Mapping closure:** DOC-001 pp. 1-11, DOC-002 pp. 1-35, DOC-003 pp. 1-162, DOC-004 pp. 1-48, and DOC-005 pp. 1-16 are assigned and mapped. The DOC-004 pp. 16-48 visual repair closes the earlier semantic extraction limitation.
- **Numeric relationship closure:** `N001` through `N129` occur once in the canonical numeric inventory and once in the numeric checker (129/129).
- **Statistical relationship closure:** `S001` through `S056` occur once in the canonical statistical inventory and once in each statistical-pass table (56/56). Every canonical S row records both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`.
- **Candidate-set closure:** The ledger, evidence recheck, this audit, and the candidate-stage manifest scopes each contain `C001` through `C010`. No stable ID is deleted, merged, ranked, suppressed, or assigned a scientific disposition.
- **No count boundary:** The source maps, 129 numeric checks, 56 statistical checks, 24 cross-source matches, and ten-ID ledger show full-scope processing. The ledger explicitly states that ten was the observed count, not a limit or target. No old candidate set or top-N queue appears as a discovery scope.
- **Statistical-agent requirement:** `/root/statistics_pass_1` and `/root/statistics_pass_2` are distinct runtime IDs. Both are recorded as fresh `gpt-5.6-terra` agents at high reasoning effort with separate artifacts.
- **Manifest path form:** Every existing coverage row has exactly one plain relative artifact path. All completed-stage paths resolve. At audit time, `evidence_quality` remains `IN_PROGRESS`, and `report_generation` remains `NOT_STARTED` with a nonenumerated scope. The coordinator must mark the former `COMPLETE` after this artifact exists and must enumerate `C001 C002 C003 C004 C005 C006 C007 C008 C009 C010` and mark the report row `COMPLETE` only after report generation.
- **Agent-manifest completion:** The coordinator, all mapping/checking agents, both statistical agents, the evidence rechecker, and this auditor are recorded once. The eventual report-generator agent must be added exactly once when spawned.
- **Display-zero boundary:** No candidate is based on `P = 0`, `p = 0.000`, finite-precision underflow, or nonzero-tail reasoning. The only reviewed eTable P values are nonzero (`P = .004` and `P = .42`). No conditional independent-contradiction field is required for C001-C010.
- **Link reproducibility:** The PDF links in `verification/evidence_recheck.md` resolve to the supplied package files and use truthful `#page=N` anchors. The source links in `checkers/cross_source_consistency.md` use `../../../../` from the checker directory and resolve one directory above this package; they require a one-level path repair before reuse. From the final report in `.ai_paper_validation/`, source links must use `../filename.pdf#page=N`.

## Cross-artifact evidence correction required

The direct-source recheck supersedes the scientific transcriptions in the earlier mapping, numeric-checker, cross-source-checker, and ledger prose for C002, C003, C005, and C006. Those earlier artifacts must remain preserved, but the final report must not repeat their contradicted values as source facts. The stable IDs remain in every downstream artifact and are presented as nonreproduced quality-control records pending human adjudication.

## C001 — eTable 4 expands RR as risk difference although the table reports relative risk

- **State:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` follows the controlled scope.
- **Evidence audit:** Reproduced at DOC-005 [PDF p. 7](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=7>) and [PDF p. 8](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=8>). The header and binary-model text identify relative risk, while the abbreviation line says `RR = risk difference`.
- **Calculation audit:** For the PDA row, the crude ratio is `(159/319)/(175/308) = 0.8772`; the crude difference is `100 x (159/319 - 175/308) = -6.97` percentage points. These are different scales. Exact reproduction of adjusted RR `.86` is unnecessary for the printed label conflict.
- **Alternative and assumptions:** A localized abbreviation-line error is plausible but is not established. Individual data and fitted robust-Poisson output are absent; no claim is made about the numeric estimate itself.
- **Duplicate audit:** The merge of NUM-CAND-001, CROSS-CAND-001, and STAT1-CAND-003 is genuine because they concern the same line, comparator, and rule. It is not a duplicate of C009 or C010, which concern different tables and estimator wording.
- **Impact wording:** If confirmed, an evidence extractor could copy an incorrect effect-measure expansion. No change to the paper-level conclusion is established.
- **Remaining human question:** Should the p. 8 abbreviation expand RR as `relative risk`, consistently with the header, model text, and ratio-scale values?
- **Report repair:** Build the full final evidence card from the recheck, including the exact report-spec labels for reported-versus-comparator, calculation, alternatives, mechanical recheck, bounded downstream impact, and verification steps.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Eligibility upper gestational-age bound differs across supplied trial documents

- **State:** Pending Human Adjudication.
- **Category audit:** The ledger uses the secondary category `Analysis-unit or population inconsistency`; that category is relevant only if a concrete eligibility-bound conflict exists. The direct-source recheck did not reproduce one.
- **Evidence audit:** DOC-002 [PDF p. 4](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=4>) directly prints `22 0/7-28 6/7 weeks`, not `22 0/7-27 6/7`. DOC-003 p. 7, DOC-004 pp. 8 and 15, and DOC-001 p. 2 also identify the upper bound as `28 6/7`.
- **Calculation audit:** The compared upper-bound difference is `0 days`, not 7 days. The ledger calculation relied on an incorrect source transcription.
- **Alternative and assumptions:** A custom-font decoding or visual transcription error may explain the earlier `27 6/7`, but the mechanism is inferred. No cited supplied page supports that value.
- **Duplicate audit:** The stable ID correctly retains the merged numeric and cross-source provenance, but its originally claimed mismatch is not reproduced. It must not be merged with or suppressed in favor of another ID.
- **Impact wording:** The supplied direct sources do not currently establish a paper-level eligibility inconsistency or a resulting downstream extraction risk. The final report should describe only the retained, nonreproduced record.
- **Remaining human question:** Does any other supplied direct-source passage print `27 6/7`, or should human adjudication proceed from the consistently printed `28 6/7` bound?
- **Report repair:** Replace the ledger's asserted source fact with the exact corrected value and prominently state that direct-source recheck contradicts the ledger transcription and that the claimed mismatch was not reproduced.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — First-dose poractant alfa volume differs across supplied trial documents

- **State:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` is the ledger category, but the direct-source recheck did not reproduce the claimed first-dose conflict.
- **Evidence audit:** DOC-002 [PDF p. 4](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=4>) directly prints `2.5 mL/kg` for the poractant alfa/Curosurf first dose in both arms, not `1.25 mL/kg`. DOC-003 pp. 7 and 12, DOC-004 p. 8, DOC-001 p. 2, and DOC-005 p. 4 agree on `2.5 mL/kg` for dose 1; `1.25 mL/kg` is identified as dose 2.
- **Calculation audit:** The matched first-dose comparison is `2.5 - 2.5 = 0 mL/kg` and `2.5/2.5 = 1`. The original factor-of-two calculation compared a mis-transcribed first dose with the true first dose.
- **Alternative and assumptions:** Transfer of the second-dose value into the first-dose record or custom-font misreading is plausible but not established.
- **Duplicate audit:** The merged numeric and cross-source provenance concerns one intended relationship. The ID remains, but the asserted mismatch is nonreproduced.
- **Impact wording:** No supplied-source first-dose inconsistency or conclusion impact is established. Any downstream statement must be limited to the risk of copying the erroneous audit transcription, not attributed to the paper.
- **Remaining human question:** Does any supplied direct-source location assign `1.25 mL/kg` to dose 1, or should adjudication use the cited pages' consistent `2.5 mL/kg` first-dose value?
- **Report repair:** Use the corrected dose/order facts from the recheck and state explicitly that the original mismatch was not reproduced.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Severe-NDI GMFCS cutoff differs between the manual and SAP

- **State:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` follows the controlled scope because the printed cutoff changes endpoint membership.
- **Evidence audit:** Reproduced at DOC-003 [PDF p. 14](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=14>) and [PDF p. 16](<../../../joi250072supp2_prod_1761000786.6938.pdf#page=16>), which use GMFCS `3-5`, versus DOC-004 [PDF p. 10](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=10>) and [PDF p. 33](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=33>), which use `4-5`.
- **Calculation audit:** `{3,4,5} minus {4,5} = {3}`; GMFCS level 3 is included under one printed definition and excluded under the other.
- **Alternative and assumptions:** A versioned definition change is possible. The package does not supply a governing amendment, implementation record, or level-3 participant data.
- **Duplicate audit:** This is distinct from C005 because the GMFCS cutoff and cognitive instrument edition are separate statements and rules, even though they occur in the same endpoint definition.
- **Impact wording:** If confirmed and used in a later outcome report, an extractor could copy a different severe-NDI component threshold. No numerical endpoint or current-paper conclusion effect can be quantified from the supplied package.
- **Remaining human question:** Which cutoff governed severe-NDI classification, and is there a supplied amendment or implementation record explaining `3-5` versus `4-5`?
- **Report repair:** Preserve the prospective-definition context and avoid asserting that participant classifications changed without level-3 data.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Severe-NDI cognitive instrument edition differs within supplied definitions

- **State:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` is the original ledger category, but the cited direct sources do not reproduce an edition conflict.
- **Evidence audit:** DOC-003 pp. 14 and 16 identify BSID-IV. DOC-004 [PDF p. 10](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=10>) prints `BSID IV < 70`, and [PDF p. 33](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=33>) prints `Bayley's Scale for Infant Development, 4th edition (BSID-IV) cognitive score < 70`. Page 34 continues the same definition. It does not print Bayley-III at the cited location.
- **Calculation audit:** `4th edition` and `BSID-IV` identify the same edition; all cited definitions use the `<70` threshold. The claimed III-versus-IV comparison is not reproduced.
- **Alternative and assumptions:** Misreading `IV` as `III` or template carry-forward in the earlier map is plausible but not established.
- **Duplicate audit:** The ID remains separate from C004, but the original C005 source relationship is nonreproduced and must not be presented as additional support for C004.
- **Impact wording:** No supplied-source instrument-edition inconsistency or current outcome effect is established. The final report must not imply that a different instrument was administered.
- **Remaining human question:** Does another supplied direct-source passage identify Bayley-III for severe NDI, or should adjudication use the consistently printed BSID-IV/fourth-edition text?
- **Report repair:** Replace `Bayley-III` with the exact printed `4th edition (BSID-IV)` and prominently state that direct-source recheck contradicts the ledger transcription.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — First interim nominal alpha differs tenfold between protocol and SAP

- **State:** Pending Human Adjudication.
- **Category audit:** `Statistical reporting inconsistency` is the original ledger category, but the direct-source recheck did not reproduce the asserted alpha difference.
- **Evidence audit:** DOC-002 [PDF p. 29](<../../../joi250072supp1_prod_1761000786.68881.pdf#page=29>) and DOC-004 [PDF p. 26](<../../../joi250072supp3_prod_1761000786.6988.pdf#page=26>) both print first-look alpha `0.000015`, followed by `.0030`, `.0183`, and `.0440`.
- **Calculation audit:** `0.000015/0.000015 = 1`, and the difference is `0`. The tenfold ratio in the ledger results from a dropped zero in the earlier transcription.
- **Alternative and assumptions:** A custom-font transcription error is plausible but not established. This is not a display-zero P-value issue.
- **Duplicate audit:** The numeric and cross-source provisional records genuinely address one planned-alpha relationship, but their asserted mismatch is nonreproduced. C006 remains distinct from C007's `.049` versus planned `.0440` question.
- **Impact wording:** No supplied-source first-look alpha conflict is established. Do not claim altered inference, spending, or conclusions from this nonreproduced transcription.
- **Remaining human question:** Does any other supplied protocol page state `0.00015`, or should adjudication use the identical `0.000015` values on the cited pages?
- **Report repair:** Replace the incorrect protocol value and state explicitly that direct-source recheck contradicts the ledger and that the claimed mismatch was not reproduced.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Final primary-analysis alpha differs between the article and prospective documents

- **State:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` follows the controlled scope as a printed prospective-versus-executed threshold comparison, with the conditional context retained.
- **Evidence audit:** Reproduced at DOC-001 [PDF p. 3](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=3>) and [PDF p. 7](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=7>), which state `.049`, versus DOC-002 p. 29 and DOC-004 p. 26, which state planned final alpha `.0440`.
- **Calculation audit:** `.049 - .0440 = .0050`; `.049/.0440 = 1.1136`. This is not a rounding-only difference.
- **Alternative and assumptions:** A realized Lan-DeMets boundary, recovery of unspent alpha, changed information timing, fewer performed looks, or an amendment could explain the values. The package lacks realized information fractions, spending output, and amendment history.
- **Duplicate audit:** C007 is not a duplicate of C006: it compares the executed article threshold with the planned final threshold, whereas C006 retained a nonreproduced first-look transcription.
- **Impact wording:** If unresolved, an extractor could record different primary significance thresholds. The supplied estimates and confidence intervals are not shown to be incorrect, and no conclusion change is established.
- **Remaining human question:** What realized information fractions and alpha-spending output produced `.049`, and how was that threshold derived from or amended relative to `.0440`?
- **Report repair:** State the comparison conditionally and do not call `.049` inconsistent with the plan without the missing execution details.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Trial center count differs between final and prospective documents

- **State:** Pending Human Adjudication.
- **Category audit:** `Cross-document numeric inconsistency` follows the controlled scope if the counts use the same center definition and operational period; those matching conditions are not yet established.
- **Evidence audit:** Reproduced at DOC-001 [PDF p. 1](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=1>), which states 17 centers, versus DOC-002 p. 29 and DOC-004 p. 8, which state 15 planned centers.
- **Calculation audit:** `17 - 15 = 2` centers.
- **Alternative and assumptions:** The SAP uses prospective language (`plan to participate`), while the article describes completed conduct. Later site activation or different center/hospital/pooling definitions are plausible. Activation records and the final center mapping are absent.
- **Duplicate audit:** This is a distinct trial-setting relationship and is not duplicated by the model-adjustment relationships.
- **Impact wording:** If the counting basis remains unclear, an extractor could copy 15 or 17 as the trial setting. No model estimate or conclusion effect is established.
- **Remaining human question:** Which centers enrolled participants, when were any additional centers activated, and do the two counts use the same definition?
- **Report repair:** Preserve prospective-versus-completed timing and avoid asserting that either count is erroneous without activation records.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Table 3 RR label conflicts with a stated common-OR approximation

- **State:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` follows the controlled scope.
- **Evidence audit:** Reproduced at DOC-001 [PDF p. 8](<../../../jama_ambalavanan_2025_oi_250072_1761000786.6838.pdf#page=8>). The row labels `.69 (.33 to 1.46)` as RR, while footnote g refers to a common-OR approximation after robust-Poisson nonconvergence.
- **Calculation audit:** Crude RR `(13/312)/(18/299) = 0.6921`; crude OR `[13 x 281]/[299 x 18] = 0.6787`. The crude calculations cannot identify the stated stratified Mantel-Haenszel/common-OR result.
- **Alternative and assumptions:** The target estimand may remain relative risk while the common OR is used as a sparse-event approximation. Stratum counts, weights, model output, and interval construction are absent.
- **Duplicate audit:** This concerns a main-article Table 3 row and is distinct from C010's supplement-wide marked-row header/footnote relationship.
- **Impact wording:** If confirmed, an extractor could classify the point estimate as RR or OR differently. No numerical result or paper conclusion is shown to be wrong.
- **Remaining human question:** Is `.69 (.33 to 1.46)` formally a Mantel-Haenszel RR, a common OR, or an OR approximation to an RR target, and which label should accompany it?
- **Report repair:** Keep crude calculations diagnostic only and do not claim estimator incompatibility beyond the printed ambiguity.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — eTable 3 relative-risk header conflicts with odds-ratio approximation footnote

- **State:** Pending Human Adjudication.
- **Category audit:** `Measure, label, or scale inconsistency` follows the controlled scope.
- **Evidence audit:** Reproduced at DOC-005 [PDF p. 5](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=5>) and [PDF p. 6](<../../../joi250072supp4_prod_1761000786.6988.pdf#page=6>). The column header names relative risk, while footnote b identifies crude unadjusted odds-ratio approximations with exact 95% CIs for marked sparse rows.
- **Calculation audit:** The marked point estimates are supported by crude OR diagnostics: `(3 x 309)/(319 x 4) = 0.7265`, `(2 x 310)/(320 x 3) = 0.6458`, and `(8 x 310)/(314 x 3) = 2.6327`, close to `.73`, `.65`, and `2.64`.
- **Alternative and assumptions:** The header may name the target measure while the footnote transparently identifies an approximating estimator. Exact CI reproduction needs the precise exact-interval algorithm, tail convention, and row-specific denominators.
- **Duplicate audit:** S053 and S054 are correctly treated as one table-level candidate. C010 remains distinct from C009 and C001.
- **Impact wording:** If confirmed, a row-level data extractor could classify marked estimates as RR or OR differently. No conclusion change or actual downstream propagation is established.
- **Remaining human question:** For superscript-b rows, should the displayed effect be extracted as an OR or as an explicitly labelled OR approximation to RR?
- **Report repair:** Identify the affected rows and preserve the target-measure-versus-approximating-estimator alternative without overstating ambiguity as numeric error.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Coordinator and report-generator repair requirements

1. Preserve all ten stable IDs in the ledger, recheck, quality audit, final report, and candidate-stage manifest scopes.
2. For C002, C003, C005, and C006, use the exact direct-source values from the evidence recheck, state that the ledger transcription is contradicted, and state that the originally claimed mismatch is not reproduced. Do not silently reuse the earlier mapping/checker text.
3. Expand every final report card to all exact report-spec fields. The current ledger does not itself contain the exact-labeled fields for `Reported-versus-comparator`, `Calculation`, `Alternative source-grounded interpretations`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, or the required blank adjudication template.
4. Keep every downstream-impact statement bounded to what an extractor, systematic review, meta-analysis, or guideline could copy if the candidate is confirmed. Do not state that propagation, harm, or conclusion change occurred.
5. Repair cross-source-checker link depth when reusing those citations. Every final-report PDF link must resolve and end in `#page=N`.
6. Update `coverage_manifest.md` after this audit and final report generation, and add the report-generator agent to `agent_execution_manifest.md` exactly once.

## Audit conclusion

Coverage is complete through evidence quality: five direct sources, 272/272 mapped units, 129/129 numeric relationships, 56/56 statistical relationships in each of two passes, and 10/10 stable IDs mechanically rechecked and audited. Six IDs have reproduced source support (C001, C004, C007, C008, C009, C010). Four IDs are preserved as required but have contradicted ledger transcriptions and nonreproduced original mismatches (C002, C003, C005, C006). Completion of the overall run still requires the coordinator's manifest updates, report generation, token accounting, integrity rehashing, HTML rendering, and final validator pass.
