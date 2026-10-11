# Final Evidence-Quality Audit

## Audit result

- **Coverage status:** COMPLETE for scientific source coverage, quantitative relationship coverage, both statistical passes, and stable-candidate evidence review. Coordinator-owned manifest and report-stage repairs listed below remain required before workflow completion.
- **Direct-source coverage:** 7 PDFs, 227/227 page units mapped. The source ledger closes every row: 67 reusable-backed units plus 160 fresh-required units equals 227 total units, and mapped units equal total units for every source.
- **Relationship coverage:** N001 through N113 are present in the numeric inventory and assigned to the numeric checker; S001 through S077 each have explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. The two statistical passes used distinct fresh Terra/high runtime IDs: `/root/statistics_pass_1` and `/root/statistics_pass_2`.
- **Stable candidate set:** C001 and C002. The ledger and evidence recheck contain identical stable-ID sets, and this audit returns both IDs under exact stable-ID headings. Neither ID is deleted, merged, renumbered, ranked, suppressed, or assigned an adjudication or severity.
- **Discovery boundary:** No top-N rule, desired count, old candidate list, or legacy disposition controlled discovery. The maps cover the full direct-source union, the numeric inventory contains 113 relationships, and both statistical passes cover all 77 statistical relationships. The asset inventory states that legacy candidate, queue, verifier, critic, checker, and final-report content was not used as discovery scope.
- **Display-zero rule:** No candidate mentions `P = 0`, `p = 0.000`, or an equivalent display zero. The checker artifacts explicitly report no display-zero candidate. The conditional independent-contradiction field is therefore not applicable to C001 or C002.
- **Integrity and reproducibility:** All 7 direct-source hashes and all 137 reused-artifact hashes reproduce with `sha256sum --check`. Every candidate PDF link resolves to a supplied PDF and ends in a valid `#page=N` fragment. Direct PDF inspection reproduced the cited headings, values, figure labels, table entries, and pagination.
- **Scope and tone:** C001 uses `Cross-document numeric inconsistency`; C002 uses `Measure, label, or scale inconsistency`. Both are categories from `QUALITY_CONTROL_SCOPE.md`. Both remain neutral quality-control observations, separate direct observations from inferred explanations, state unresolved human questions, bound downstream reuse risk, and expressly avoid claiming that the paper's overall conclusion changes.

## Source and artifact coverage audit

| Source | Total | Reusable | Fresh-required | Mapped | Audit result |
|---|---:|---:|---:|---:|---|
| DOC-001-MAIN | 14 | 14 | 0 | 14 | Closed |
| DOC-002-ADMIN-COLLAB | 30 | 0 | 30 | 30 | Closed |
| DOC-003-PROTOCOL | 82 | 0 | 82 | 82 | Closed |
| DOC-004-SAP-TRIAL | 40 | 0 | 40 | 40 | Closed |
| DOC-005-SAP-ANALYSIS | 7 | 0 | 7 | 7 | Closed |
| DOC-006-RESULTS-SUPP | 53 | 53 | 0 | 53 | Closed |
| DOC-007-ADMIN-DATA | 1 | 0 | 1 | 1 | Closed |
| **Total** | **227** | **67** | **160** | **227** | **Closed** |

The main map documents all 14 main-article pages. The support map documents all 213 support pages, including 160 fresh-required pages and direct-PDF confirmation of 53 reusable-backed supplement pages. No scientific-coverage gap remains. The coverage manifest has one undecorated relative artifact path in every row; its evidence-quality and report-generation rows still require the coordinator updates stated below.

## Routing and execution audit

`routing_preflight.md` reports `PASS`, coordinator `gpt-5.6-sol`/`high`, ordinary specialists `gpt-5.6-terra`/`medium`, statistical specialists `gpt-5.6-terra`/`high`, Sol specialists `gpt-5.6-sol`/`high`, `Coordinator inference: PASS`, execution mode `INTERACTIVE_CLI`, and all nine required presets verified. The execution manifest gives distinct fresh IDs for the curator, both mappers, numeric reviewer, cross-source reviewer, statistical pass 1, evidence rechecker, and statistical pass 2. The two statistical runtime IDs are distinct and satisfy the required model and effort.

The execution manifest was inspected before this audit artifact was written. It does not yet contain this auditor and cannot yet contain the later report generator. Those are coordinator-owned completion items, not scientific-coverage gaps.

## Required coordinator repairs

1. Add the auditor exactly once to `agent_execution_manifest.md`: stage `quality_control_auditor`, agent ID `/root/quality_control_auditor`, model `gpt-5.6-sol`, effort `high`, start mode `FRESH_SPAWN`, artifact `quality/evidence_quality_audit.md`.
2. Change the `coverage_manifest.md` evidence-quality row to exact scope `C001, C002`, artifact `quality/evidence_quality_audit.md`, status `COMPLETE`. Change the report-generation scope to `C001, C002`; retain `PENDING` only until the report artifact exists, then mark it `COMPLETE`.
3. Repair C001's candidate-ledger provenance without changing any stable ID: `N082` is the unrelated MR-DWI growth relationship. The direct eTable 2 comparator is `N069`; retain the applicable Figure 2 and population-support relationships.
4. Repair C002's candidate-ledger provenance without changing any stable ID: `N017` and the undifferentiated `N042-N059` range include unrelated relationships and omit the most direct numeric records. Use exact relevant numeric provenance, including `N052`, `N056`, `N078`, `N110`, and `N111`, alongside the already stated S relationships and checker provenance.
5. During report generation, instantiate every required evidence-card label for both IDs. The ledger is not yet a final report card and therefore does not contain all exact final-card labels. The source material needed for each label is available across the ledger, checker output, and mechanical recheck. Use the exact human-adjudication template with `__` in all five subfields.
6. After report generation, complete the remaining execution-manifest, token-ledger, timing, hash-after, rendering, and validator steps required by Workflow 1.5.3. These artifacts were not expected to be final during this mandatory pre-report audit.

## C001 — ITT Figure 2 mRS distributions conflict with ITT eTable 2 threshold counts

- **Stable-ID and category audit:** Retain C001 unchanged. Its category, `Cross-document numeric inconsistency`, follows the normative scope.
- **Evidence locations and pagination:** Confirmed at [main article PDF p. 7](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), [Supplement 5 PDF p. 38](<../../../joi240006supp5_prod_1708623115.01733.pdf#page=38>), [main article PDF p. 4](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>), and [Supplement 5 PDF p. 8](<../../../joi240006supp5_prod_1708623115.01733.pdf#page=8>). No false pagination was found.
- **Direct evidence and comparator:** Figure 2 and eTable 2 both state an intention-to-treat 90-day mRS context with 168 participants per arm. The direct figure has the four reported core-stratum denominators and fixed legend order; eTable 2 has the exact threshold and mortality counts recorded in the recheck.
- **Arithmetic audit:** The nearest-whole-percentage feasibility calculation is correct. The unique Figure-derived mRS 0-6 vectors are EVT below 100 mL `[2, 7, 21, 26, 17, 9, 35]`, EVT at least 100 mL `[1, 3, 5, 10, 0, 5, 27]`, MM below 100 mL `[0, 2, 9, 17, 27, 24, 40]`, and MM at least 100 mL `[1, 0, 2, 8, 0, 8, 30]`. They yield Figure/eTable counts of 39/34 and 14/12 for mRS 0-2, 75/65 and 39/31 for mRS 0-3, and 76/76 and 102/102 for mRS 5-6 in EVT and MM order. Reconstructed mortality is 62/62 and 70/70. No arithmetic error was found in the registered card or recheck.
- **Unsupported assumptions and missing definitions:** Nearest-whole-percentage rounding is a transparent diagnostic rule, not a source-stated production rule. The ledger and recheck correctly keep this conditional and name the missing raw category counts, unrounded percentages, calculation rule, figure dataset/version, outcome derivation, and missing-outcome handling. The candidate does not assume which display is wrong.
- **Possible duplicate relationships:** C001 is distinct from C002. Repeated population and figure/table relationships are supporting occurrences of the same C001 comparison, not separate stable candidates. The candidate-ledger reference to `N082` is erroneous provenance and requires the repair above; it does not undermine the direct source evidence.
- **Impact-language audit:** The statement that an extractor could copy conflicting ITT functional-outcome counts or proportions is bounded and source-specific. The card expressly states that it does not establish a change in the paper's overall conclusion. No downstream propagation is claimed to have occurred.
- **Evidence-card field audit:** Category, exact locations, direct observations, calculation, alternatives, quality-control relevance, and the human question are supported. The report generator must instantiate the exact final labels for candidate statement, source evidence, reported-versus-comparator, reasoning procedure, calculation, alternative interpretations, mechanical recheck, downstream impact, human verification steps, and human adjudication fields.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — `aRR` is labeled as an absolute risk reduction but displayed and interpreted as a ratio

- **Stable-ID and category audit:** Retain C002 unchanged. Its category, `Measure, label, or scale inconsistency`, follows the normative scope.
- **Evidence locations and pagination:** Confirmed at [main article PDF p. 6](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), [main article PDF p. 7](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>), [main article PDF p. 9](<../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>), [trial SAP PDF p. 17](<../../../joi240006supp3_prod_1708623114.99733.pdf#page=17>), [secondary-analysis SAP PDF pp. 4-5](<../../../joi240006supp4_prod_1708623115.00733.pdf#page=4>), and [Supplement 5 PDF p. 43](<../../../joi240006supp5_prod_1708623115.01733.pdf#page=43>). No false pagination was found.
- **Direct evidence and comparator:** The main narrative and Tables 2-3 directly expand `aRR` as “absolute risk reduction.” The table footnotes directly interpret values greater than 1 as a higher rate ratio, the printed estimates and intervals are centered on the ratio null of 1, Table 3 separately reports `aRD` on an additive scale, and the supplied SAPs specify modified-Poisson relative-risk analyses.
- **Logical and arithmetic audit:** No model reconstruction or P-value calculation is required. The additive-versus-multiplicative measure-class comparison is reproducible from the direct text, null values, representative estimates, and separately printed aRD. No arithmetic or scale-rule error was found in the registered card or recheck.
- **Unsupported assumptions and missing definitions:** The card correctly treats “adjusted risk ratio” and “adjusted rate ratio” only as possible intended expansions. The authoritative abbreviation dictionary, intended meaning of `a`, intended risk-versus-rate term, and any nonstandard mathematical definition are absent and are named as the remaining human question. No correction is prescribed.
- **Possible duplicate relationships:** Numeric, cross-source, and statistical checker observations concern the same abbreviation, comparator, and effect-measure rule and were appropriately merged before stable IDs. C002 is not a duplicate of C001. Its current numeric provenance range is overbroad and partly unrelated; the exact-provenance repair above is required without changing any N, S, or C identifier.
- **Impact-language audit:** The statement that an extractor could assign a relative estimate to an absolute effect-measure class is bounded to a specific extraction error and does not claim that propagation occurred or that the paper's conclusion changes.
- **Display-zero audit:** C002 contains no display-zero P value. No conditional independent-contradiction field is required.
- **Evidence-card field audit:** Category, exact locations, direct observations, logical comparison, alternatives, quality-control relevance, and the human question are supported. The report generator must instantiate the exact final labels for candidate statement, source evidence, reported-versus-comparator, reasoning procedure, calculation, alternative interpretations, mechanical recheck, downstream impact, human verification steps, and human adjudication fields.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Limitations

- C001 cannot be causally reconciled without the raw mRS category counts, unrounded Figure 2 percentages, figure-generation dataset/version, and explicit percentage-calculation rule.
- C002 cannot be finally relabeled without an authoritative intended expansion and effect-measure name for `aRR`.
- This audit precedes final report assembly by contract. Report-card field instantiation, report-generation manifest closure, token accounting, final timing, after-hash artifacts, standalone HTML rendering, and mechanical validation remain coordinator-owned completion stages.
- These limitations do not create an uncovered source unit, an unchecked N or S relationship, an unrechecked stable ID, or a basis to suppress either candidate.
