# Fresh Evidence-Quality Audit

## Audit status and evidence boundary

This audit covers the current source and evidence inventories, every row of `source_coverage.md` and
`coverage_manifest.md`, the main and support quantitative mappings, the canonical numeric and
statistical relationship inventories, the numeric and cross-source checkers, both clean statistical
passes, the stable candidate ledger, the mechanical evidence recheck, and every row of the current
agent execution manifest. The supplied PDFs and current fresh derivatives were the only evidence
chain. The discarded contaminated statistical artifact, preserved archive, prior reports, prior
quality outputs, web, and external evidence were not read or used.

The audit returns all eight stable IDs, `C001` through `C008`. Every ID remains **Pending Human
Adjudication**. No ID is deleted, merged, renumbered, ranked, suppressed, assigned severity, given a
scientific disposition, or prescribed a correction.

**Current audit outcome:** `COMPLETE`. Source-unit coverage, numeric and statistical relationship
coverage, candidate identity, recheck coverage, and execution requirements are complete. The one
freshly extracted support numeric block initially missing from the canonical numeric inventory was
appended as UN031/N072 and checked without deleting, merging, or renumbering any existing relationship
or stable candidate.

## Source and evidence inventory audit

| Source ID | Direct source | Total units | Reusable units | Fresh-required units | Mapped units | Audit record |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | `jama_wang_2018_oi_180070.pdf` | 10 PDF pages | 0 | 10 | 10 | Complete source coverage; fresh native and layout text for all pages; pp. 1-9 rendered; no OCR threshold met. |
| DOC-002 | `joi180070supp1_prod.pdf` | 25 PDF pages | 0 | 25 | 25 | Complete source coverage; fresh native and layout text for all pages; pp. 1-21 rendered; no OCR threshold met. |
| DOC-003 | `joi180070supp2_prod.pdf` | 9 PDF pages | 0 | 9 | 9 | Complete source coverage; fresh native and layout text and rendering for all pages; no OCR threshold met. |

For every direct source, fresh-required units and mapped units equal total units, reusable units equal
zero, and status is `COMPLETE`. The source inventory identifies exactly three direct PDFs and no
Office, workbook, or CSV source. The evidence inventory accounts for 44 unique PDF pages and 39
result-relevant renders. Its native-first and no-OCR decisions are source-specific and bounded.

The fresh extraction maps cover DOC-001 pp. 1-10, DOC-002 pp. 1-25, and DOC-003 pp. 1-9. DOC-003
p. 2's baseline-survey numeric block is represented in `extraction/support_quantitative_evidence.md`,
provisional record UN031, canonical relationship N072, the numeric checker, and the cross-source
checker. The repaired relationship chain is complete.

## Coverage-manifest row audit

Every `Artifact` cell contains exactly one plain relative path. All recorded paths resolve after this
audit artifact is written. Statuses below are the statuses recorded at audit time; downstream stages
remain the coordinator's responsibility.

| Stage / shard | Exact assigned coverage | One artifact path | Recorded status | Audit record |
|---|---|---|---|---|
| `source_inventory` / `source-001` | DOC-001-DOC-003 identities, units, roles, hashes | `source_inventory.md` | COMPLETE | Complete. |
| `source_inventory` / `source-002` | DOC-001-DOC-003 pre-run hashes | `source_hashes_before.sha256` | COMPLETE | Complete. |
| `evidence_assets` / `assets-001` | All 44 PDF pages | `evidence_asset_inventory.md` | COMPLETE | Complete. |
| `main_evidence_mapping` / `main-001` | DOC-001 pp. 1-10 | `extraction/main_quantitative_evidence.md` | COMPLETE | Complete. |
| `main_evidence_mapping` / `main-002` | MN001-MN041 | `relationships/parts/main_numeric_relationships.md` | COMPLETE | Complete. |
| `main_evidence_mapping` / `main-003` | MS001-MS024 | `statistics/parts/main_statistical_relationships.md` | COMPLETE | Complete. |
| `support_evidence_mapping` / `support-001` | DOC-002 pp. 1-25 and DOC-003 pp. 1-9 | `extraction/support_quantitative_evidence.md` | COMPLETE | Extraction complete. |
| `support_evidence_mapping` / `support-002` | UN001-UN031 | `relationships/parts/support_numeric_relationships.md` | COMPLETE | Complete, including DOC-003 p. 2 as UN031. |
| `support_evidence_mapping` / `support-003` | US001-US037 | `statistics/parts/support_statistical_relationships.md` | COMPLETE | Complete. |
| `numeric_checks` / `numeric-001` | N001-N072 | `checkers/numeric_consistency.md` | COMPLETE | Complete; 72/72 explicit records. |
| `statistics_pass_1` / `statistics-001` | S001-S061 | `checkers/statistical_pass_1.md` | COMPLETE | 61/61 explicit clean pass-1 records. |
| `cross_source_checks` / `cross-source-001` | N001-N072 and S001-S061 | `checkers/cross_source_consistency.md` | COMPLETE | Complete, including N072 and the exact C007 Table 1 locator. |
| `candidate_registration` / `candidates-001` | C001-C008 | `candidate_ledger.md` | COMPLETE | Complete 8/8 stable IDs. |
| `evidence_recheck` / `recheck-001` | C001-C008 | `verification/evidence_recheck.md` | COMPLETE | Complete 8/8 stable IDs. |
| `statistics_pass_2` / `statistics-002` | S001-S061, C001-C008, cross-lane ledger, recheck | `checkers/statistical_pass_2.md` | COMPLETE | 61/61 S records and 8/8 candidate reconciliations. |
| `evidence_quality` / `quality-001` | C001-C008 and every coverage/execution row | `quality/evidence_quality_audit.md` | PENDING | Artifact and repairs are complete; coordinator should now mark this row `COMPLETE`. |
| `report_generation` / `report-001` | C001-C008 and complete run metadata | `report_generation.md` | PENDING | Expected downstream status; do not mark complete until the report is assembled. |

## Quantitative, statistical, checker, and identity audit

| Inventory or lane | Current coverage | Audit record |
|---|---|---|
| Main numeric mapping | MN001-MN041 | Complete for the mapped main source. |
| Support numeric mapping | UN001-UN031 | Complete, including the DOC-003 p. 2 baseline-survey numeric block as UN031. |
| Canonical numeric inventory and numeric checker | 72 unique sequential IDs, N001-N072; 72 explicit checker records | Complete. N072 factually represents existing C007 and yields no new candidate. |
| Main statistical mapping | MS001-MS024 | Complete. |
| Support statistical mapping | US001-US037 | Complete. |
| Canonical statistical inventory | 61 unique sequential IDs, S001-S061 | Complete. |
| Clean statistical pass 1 | S001-S061 | Complete, uncapped, and independent. |
| Statistical pass 2 | S001-S061 plus C001-C008 and recheck facts | Complete, uncapped, and independent of the discarded artifact. |
| Cross-source checker | 27 match keys covering N001-N072 and S001-S061 | Complete; XCHK013 covers N072 and uses the exact C007 Table 1 locator. |
| Stable ledger / recheck / pass-2 candidate set | C001-C008 / C001-C008 / C001-C008 | Identical 8-ID sets. This quality artifact also returns C001-C008. |

The omission repair appended UN031 and N072 for DOC-003 p. 2's statement that 20 patients per cluster
were prospectively included, composite 80.2% versus 79.5%, and the nine printed baseline
performance-measure percentages. N072 has an explicit numeric checker record and cross-source
coverage. The 20-by-40 comparison remains existing C007; the other p. 2 percentages lack printed
counts/denominators or a matched result identity sufficient for an additional arithmetic candidate.
C007 provenance now includes N025, N028, N042, and N072.

No top-N, expected-count, queue, or early-stopping boundary controlled discovery. The current checker
lanes explicitly process every registered `N` and `S` ID, and the stable ledger contains every
distinct proposal after one genuine pre-ID duplicate merge. No candidate is based on `P = 0`,
`p = 0.000`, literal-zero formatting, underflow, or mathematical nonzero-tail reasoning. C008 uses
`.009` and an independently printed interval/test-column pairing; it is not a display-zero candidate.

## Agent-execution audit

| Stage | Agent ID | Model / effort / start | Primary artifact | Audit record |
|---|---|---|---|---|
| coordinator | `COORDINATOR-CURRENT-SESSION` | gpt-5.6-sol / high / current session | `run_state.md` | Present exactly once. |
| fresh source preprocessor | `root/fresh_preprocessor` | gpt-5.6-terra / medium / fresh spawn | `evidence_asset_inventory.md` | Present. |
| main quantitative mapper | `root/main_mapper` | gpt-5.6-terra / medium / fresh spawn | `extraction/main_quantitative_evidence.md` | Present. |
| support quantitative mapper | `root/support_mapper` | gpt-5.6-terra / medium / fresh spawn | `extraction/support_quantitative_evidence.md` | Present. |
| numeric consistency | `root/numeric_checker` | gpt-5.6-terra / medium / fresh spawn | `checkers/numeric_consistency.md` | Present. |
| discarded contaminated pass 1 | `root/statistics_pass_1` | gpt-5.6-terra / high / fresh spawn | `checkers/discarded_statistical_pass_1_contaminated.md` | Correctly retained for execution/accounting only; not accepted as a scientific pass and not read by this audit. |
| clean statistical pass 1 | `root/statistics_pass_1_clean` | gpt-5.6-terra / high / fresh spawn | `checkers/statistical_pass_1.md` | Qualifying fresh pass 1. |
| cross-source consistency | `root/cross_source_checker` | gpt-5.6-terra / medium / fresh spawn | `checkers/cross_source_consistency.md` | Present. |
| evidence recheck | `root/evidence_rechecker` | gpt-5.6-sol / high / fresh spawn | `verification/evidence_recheck.md` | Present. |
| statistical pass 2 | `root/statistics_pass_2` | gpt-5.6-terra / high / fresh spawn | `checkers/statistical_pass_2.md` | Qualifying fresh pass 2. |
| evidence quality | `root/quality_auditor` | gpt-5.6-sol / high / fresh spawn | `quality/evidence_quality_audit.md` | Present. |

The two qualifying statistical agents are distinct fresh runtime IDs:
`root/statistics_pass_1_clean` and `root/statistics_pass_2`. Both are recorded as
`gpt-5.6-terra` with `high` reasoning effort and `FRESH_SPAWN` start mode. Every manifested agent has
one primary artifact path. The discarded call remains manifested because it consumed runtime, while
the clean pass artifacts explicitly exclude it from their evidence chain. A future report-generator
or repair agent must be added exactly once when spawned.

## Stable candidate audit

The final-report-only labels currently absent from every ledger entry are `Reasoning procedure`,
`Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`,
`Human verification steps`, and `Human adjudication fields`. Their absence from the ledger does not
remove an ID, but the report generator must supply them for every final card from the ledger, recheck,
and this audit. The required blank adjudication template is repeated under every ID below.

## C001 — Table 1 CAD/previous-myocardial-infarction percentage does not reproduce

- **Category audit:** `Numeric or arithmetic inconsistency` is an allowed primary category and matches the displayed percentage-reproduction rule.
- **Exact source support:** DOC-001, [`jama_wang_2018_oi_180070.pdf` PDF p. 6](<../../../jama_wang_2018_oi_180070.pdf#page=6>), Table 1 intervention column prints `Patients, No.` = 2,400 and `CAD/previous myocardial infarction` = `311 (13.05)`.
- **Comparator, rule, and calculation:** Compare 13.05% with `311 / 2400 x 100 = 12.9583333333%`. At the printed two-decimal precision this rounds to 12.96%, not 13.05%.
- **Exact human question:** Was 2,400 the intended row denominator, and if so which displayed element is intended?
- **Assumption and limitation audit:** The whole-column total is printed, but no row-specific denominator is repeated. The ledger and recheck appropriately keep an unprinted row-specific denominator as an unresolved alternative; they do not assert a correction.
- **Arithmetic, pagination, and duplication audit:** Arithmetic reproduced; PDF p. 6 is correct; no duplicate stable relationship. C001 has a different printed cell and rule from every other ID.
- **Tone and impact audit:** No paper-level conclusion impact or downstream propagation is claimed. A bounded final-card impact may state only that a data extractor could copy 13.05% or reconstruct 12.96% from the displayed count and total if the candidate is confirmed.
- **Human verification steps for the final card:** Check the Table 1 source table, denominator definition, and analysis output for this row; determine which displayed count, denominator, or percentage was intended.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — LDL eligibility boundary differs between result labels and supplied measure definition

- **Category audit:** `Measure, label, or scale inconsistency` is an allowed primary category and matches the strict-versus-inclusive threshold-label comparison.
- **Exact source support:** DOC-001 [`PDF p. 7`](<../../../jama_wang_2018_oi_180070.pdf#page=7>) and DOC-003 [`PDF p. 8`](<../../../joi180070supp2_prod.pdf#page=8>) print result labels `LDL >100 mg/dL`; DOC-002 [`PDF p. 15`](<../../../joi180070supp1_prod.pdf#page=15>) and DOC-003 [`PDF p. 3`](<../../../joi180070supp2_prod.pdf#page=3>) print formal definitions `LDL >=100 mg/dL`.
- **Comparator, rule, and calculation:** A strict boundary excludes exactly 100 mg/dL; an inclusive boundary includes it. The discrete comparison is `>100` not equal to `>=100`; rounding does not apply.
- **Exact human question:** Which boundary governed the Table 2 and eTable 4 denominators, especially for patients whose LDL was exactly 100 mg/dL?
- **Assumption and limitation audit:** No supplied count establishes that any patient had LDL exactly 100 mg/dL, and no operational eligibility code is supplied. The card must not claim an observed denominator change. The possible abbreviated-label interpretation remains explicit.
- **Arithmetic, pagination, and duplication audit:** Logical comparison and pages reproduced. NCAND002 and P1CAND002 were one genuine pre-ID duplicate and are properly represented once as C002 with both provenances. C005 is not a duplicate because it compares a fraction with a percentage in one cell, not the threshold label with its definition.
- **Tone and impact audit:** No conclusion-impact claim is present. A bounded final-card impact may say that a data extractor could encode different eligibility boundaries and therefore potentially select different denominators if the candidate is confirmed; no affected count or propagation is established.
- **Human verification steps for the final card:** Inspect the operational eligibility rule and counts at LDL exactly 100 mg/dL; determine whether the result labels are abbreviations or whether the formal definition differs from the implemented rule.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 4 discharge-antithrombotics control percentage does not reproduce

- **Category audit:** `Denominator, proportion, or total inconsistency` is an allowed primary category and matches the explicit fraction/percentage identity.
- **Exact source support:** DOC-003, [`joi180070supp2_prod.pdf` PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4 control cell prints `2141/2400 (89.3)` under `No. / Total (%)`.
- **Comparator, rule, and calculation:** `2141 / 2400 x 100 = 89.2083333333%`, which rounds to 89.2%, not 89.3%, at one decimal.
- **Exact human question:** Which of 2,141, 2,400, or 89.3% is the intended control result, and was any rule other than ordinary one-decimal rounding used?
- **Assumption and limitation audit:** The fraction is explicit; no alternative denominator changes the identity printed in the same cell. Possible transcription, stale display, or nonstandard production history remains inference only.
- **Arithmetic, pagination, and duplication audit:** Arithmetic reproduced; PDF p. 8 is correct. Similar one-tenth discrepancies in C004-C006 concern distinct rows and printed values, so they are not duplicate relationships.
- **Tone and impact audit:** No conclusion impact is asserted. A bounded final-card impact may state only that an extractor could copy 89.3% or mechanically derive 89.2% from the printed fraction if the candidate is confirmed.
- **Human verification steps for the final card:** Inspect the eTable 4 source values and calculation output and determine which count, total, percentage, or rounding rule was intended.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTable 4 AF-anticoagulation control percentage does not reproduce

- **Category audit:** `Denominator, proportion, or total inconsistency` is an allowed primary category and matches the explicit fraction/percentage identity.
- **Exact source support:** DOC-003, [`joi180070supp2_prod.pdf` PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4 AF-anticoagulation control cell prints `39/174 (22.5)`.
- **Comparator, rule, and calculation:** `39 / 174 x 100 = 22.4137931034%`, which rounds to 22.4%, not 22.5%, at one decimal.
- **Exact human question:** Which of 39, 174, or 22.5% is the intended AF-anticoagulation control result, and was any nonstandard rounding rule used?
- **Assumption and limitation audit:** The AF-specific denominator is explicit. Any production-history explanation is unestablished and must remain an alternative, not a finding.
- **Arithmetic, pagination, and duplication audit:** Arithmetic reproduced; PDF p. 8 is correct; C004 uses a distinct AF-specific fraction and is not duplicative of C003, C005, or C006.
- **Tone and impact audit:** No conclusion impact is asserted. A bounded final-card impact may state only that an extractor could copy 22.5% or derive 22.4% from the printed fraction if the candidate is confirmed.
- **Human verification steps for the final card:** Inspect the eTable 4 source calculation and AF denominator and determine the intended displayed value or rounding rule.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 4 lipid-lowering control percentage does not reproduce

- **Category audit:** `Denominator, proportion, or total inconsistency` is an allowed primary category and matches the explicit fraction/percentage identity.
- **Exact source support:** DOC-003, [`joi180070supp2_prod.pdf` PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4 lipid-lowering control cell prints `1439/1586 (90.8)`.
- **Comparator, rule, and calculation:** `1439 / 1586 x 100 = 90.7313997478%`, which rounds to 90.7%, not 90.8%, at one decimal.
- **Exact human question:** Which of 1,439, 1,586, or 90.8% is the intended sensitivity result, and was any nonstandard rounding rule used?
- **Assumption and limitation audit:** The cell arithmetic is independent of whether C002's strict or inclusive LDL threshold governed eligibility. No production-history explanation is established.
- **Arithmetic, pagination, and duplication audit:** Arithmetic reproduced; PDF p. 8 is correct. C005 and C002 share a result row but use different printed comparators and consistency rules and must remain separate IDs.
- **Tone and impact audit:** No conclusion impact is asserted. A bounded final-card impact may state only that an extractor could copy 90.8% or derive 90.7% from the printed fraction if the candidate is confirmed.
- **Human verification steps for the final card:** Inspect the eTable 4 source calculation and denominator and determine the intended displayed value or rounding rule separately from the eligibility-boundary question.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 4 antidiabetic-medication control percentage does not reproduce

- **Category audit:** `Denominator, proportion, or total inconsistency` is an allowed primary category and matches the explicit fraction/percentage identity.
- **Exact source support:** DOC-003, [`joi180070supp2_prod.pdf` PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4 antidiabetic-medication control cell prints `557/688 (81.1)`.
- **Comparator, rule, and calculation:** `557 / 688 x 100 = 80.9593023256%`, which rounds to 81.0%, not 81.1%, at one decimal.
- **Exact human question:** Which of 557, 688, or 81.1% is the intended control result, and was any nonstandard rounding rule used?
- **Assumption and limitation audit:** The fraction is explicit. Any transcription or production-history account is unestablished and remains an alternative only.
- **Arithmetic, pagination, and duplication audit:** Arithmetic reproduced; PDF p. 8 is correct; C006 concerns a distinct row and printed fraction.
- **Tone and impact audit:** No conclusion impact is asserted. A bounded final-card impact may state only that an extractor could copy 81.1% or derive 81.0% from the printed fraction if the candidate is confirmed.
- **Human verification steps for the final card:** Inspect the eTable 4 source calculation and denominator and determine the intended displayed value or rounding rule.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — baseline-survey patient total does not reconcile with stated per-cluster inclusion

- **Category audit:** `Cross-document numeric inconsistency` is an allowed primary category and matches the same-survey total-versus-per-cluster comparison.
- **Exact source support:** DOC-001 [`PDF p. 6`](<../../../jama_wang_2018_oi_180070.pdf#page=6>) prints `Baseline Survey, No. (%)`, `Hospitals, No.` = 40 and `Patients, No.` = 801. DOC-003 [`PDF p. 2`](<../../../joi180070supp2_prod.pdf#page=2>) states that `20 patients per cluster were prospectively included`. DOC-001 [`PDF p. 5`](<../../../jama_wang_2018_oi_180070.pdf#page=5>) and DOC-002 [`PDF p. 4`](<../../../joi180070supp1_prod.pdf#page=4>) and [`PDF p. 7`](<../../../joi180070supp1_prod.pdf#page=7>) establish 40 trial hospitals/clusters.
- **Comparator, rule, and calculation:** Under an exact fixed-count and same-survey reading, `20 x 40 = 800`, while Table 1 prints 801, a difference of one.
- **Exact human question:** Did each of the 40 baseline-survey clusters contribute exactly 20 included patients, and if so what accounts for the 801st Table 1 patient?
- **Assumption and limitation audit:** The exact-fixed-count premise is not confirmed by cluster-level records. The card must retain the possible target-versus-realized, replacement, or one-extra-patient interpretation and must not state that the 801 value is necessarily incorrect.
- **Arithmetic, pagination, and duplication audit:** Arithmetic and pages reproduced. The earlier cross-source proposal's nonliteral `Survey (n=801)` shorthand was repaired; the ledger, recheck, and cross-source checker now use the exact `Baseline Survey, No. (%)` column, `Patients, No.` = 801 locator. C007 is not a duplicate of a within-cell percentage candidate.
- **Tone and impact audit:** The ledger remains conditional and neutral. A bounded final-card impact may state only that an extractor could record either the printed total 801 or an expected fixed-count total 800 if the exact fixed-count interpretation is confirmed; no downstream use or conclusion change is established.
- **Human verification steps for the final card:** Inspect cluster-level baseline-survey enrollment records; confirm realized patient counts for all contributing clusters, replacements, and exclusions; determine whether 20 was exact or a target.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — in-hospital death absolute-difference CI and P value do not reconcile

- **Category audit:** `Statistical reporting inconsistency` is an allowed primary category and matches the conditional CI/P compatibility question.
- **Exact source support:** DOC-001 [`PDF p. 8`](<../../../jama_wang_2018_oi_180070.pdf#page=8>) prints in-hospital death adjusted absolute difference `-0.7% (95% CI, -1.1% to 0.2%)` and the corresponding adjacent absolute-difference P-value cell `.009`. DOC-001 [`PDF p. 4`](<../../../jama_wang_2018_oi_180070.pdf#page=4>) states that comparative absolute differences have 95% CIs and that all tests are two-sided.
- **Comparator, rule, and calculation:** `-1.1 < 0 < 0.2`, so the displayed interval contains the null; `.009 < .05`. Under an identical-estimand, identical-inferential-method two-sided 95% CI/P pairing, the threshold conclusions differ.
- **Exact human question:** Does `.009` test the same adjusted absolute-difference estimand represented by the printed 95% CI; if so, what accounts for the non-duality of the displayed pair?
- **Assumption and limitation audit:** The exact P-value test, CI construction, variance estimator, and explicit same-estimand mapping are not supplied. The candidate must remain an unresolved conditional pairing question. The separate HR `0.96 (0.90-1.02), P=.14` is not the comparator.
- **Arithmetic, pagination, and duplication audit:** Null containment and P threshold reproduced; pp. 4 and 8 are correct; no duplicate candidate. The ledger now correctly says `corresponding adjacent absolute-difference P-value cell`; the P value occupies its own adjacent table column.
- **Tone and impact audit:** No conclusion-impact claim is present. A bounded final-card impact may state only that an extractor could classify the displayed absolute-difference result differently from the CI and from the P value if the candidate is confirmed; no propagation or overall conclusion change is established.
- **Human verification steps for the final card:** Inspect the model output and table-layout source; confirm the estimand, test, CI construction, variance estimator, and column assignment for `.009` and `-0.7% (-1.1% to 0.2%)`.
- **Missing final-card labels:** `Reasoning procedure`; `Mechanical evidence recheck`; `Quality-control relevance`; `Potential downstream evidence impact`; `Human verification steps`; `Human adjudication fields`.
- **Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Repair completion and remaining downstream instructions

1. Completed: UN031/N072 were appended without renumbering; N072 has an explicit numeric checker
   record, cross-source coverage, and complete manifest scope.
2. Completed: C007 provenance includes N025, N028, N042, and N072; its cross-source locator uses the
   exact Table 1 column and rows.
3. Completed: C008 uses `corresponding adjacent absolute-difference P-value cell` without changing
   its source values, rule, question, category, or stable ID.
4. Remaining administrative step: update the evidence-quality manifest row to `COMPLETE`. Keep
   report generation pending until every final card contains all exact required labels, a bounded
   downstream-impact statement, human verification steps, and the exact five `__` adjudication
   placeholders.
5. If a report-generator or later repair agent is spawned, add it exactly once to
   `agent_execution_manifest.md` and later to the token ledger. Do not treat the discarded pass-1
   agent as either qualifying statistical pass.

## Limitations

- The supplied package contains no raw or cluster-level records, operational LDL eligibility code,
  unrounded analysis output, or complete CI/test construction. These missing inputs are preserved as
  exact human questions and do not authorize an AI disposition.
- Direct PDF page content and fresh text/rendered assets support every candidate transcription. The
  16 evidence-link occurrences in the recheck resolve to 11 unique local PDF-page targets, all within
  the three direct sources' page counts.
- Source integrity after the run, final report-card assembly, token accounting, HTML rendering, and
  final validator status occur after this audit and must be checked by the coordinator.
