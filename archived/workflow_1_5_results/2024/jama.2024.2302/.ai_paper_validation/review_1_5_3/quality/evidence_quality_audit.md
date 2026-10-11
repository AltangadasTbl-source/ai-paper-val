# Final Evidence-Quality Audit

## Audit status and boundaries

- **Audit scope completed:** routing preflight; direct-source and reused-asset inventories and hashes; source and coverage ledgers; both quantitative maps; all `N001`-`N041` and `S001`-`S020` relationship records; numeric, cross-source, and both statistical checker outputs; `C001`-`C005`; the mechanical evidence recheck; and the execution manifest.
- **Stable ID set:** `C001`, `C002`, `C003`, `C004`, and `C005` occur in both the candidate ledger and evidence recheck and are all returned below. No stable ID was deleted, merged, renumbered, ranked, suppressed, or scientifically adjudicated.
- **Discovery boundary:** The artifacts document source-wide mapping and uncapped checking rather than a top-N selection. The prior limited package manifest and the legacy assertion DOCX were used only for identity, reusable-asset location, or structural exclusion. No old candidate list supplied discovery scope, and the run state states `Candidate limit: None`.
- **Display-zero exclusion:** No mapped statistical relationship or candidate contains `P = 0`, `p = 0.000`, or equivalent. None of the five stable candidates depends on a display-zero argument, so no conditional independent-contradiction field is applicable.
- **Tone and disposition:** Categories use the names in `QUALITY_CONTROL_SCOPE.md`, wording remains neutral quality control, and every ledger record remains `Pending Human Adjudication`. No severity, validity, acceptance, exclusion, correction, or scientific disposition is assigned here.

## Source, relationship, and execution coverage

- The five direct-source rows close at 290 total units: 14 reusable plus 276 fresh-required equals 290, and 290 mapped units equals 290 total units. The main map covers PDF-001 pages 1-10. The support map covers PDF-002 pages 1-25, PDF-003 pages 1-10, PDF-004 pages 1-8, and the documented structural exclusion of DOCX-001 paragraphs 1-237 and tables 1-5. The DOCX exclusion is required by the prohibition on using legacy candidate assertions as discovery input and is not an unassigned unit.
- The numeric inventory contains 41 relationships and the numeric checker records all `N001`-`N041`. The statistical inventory contains 20 relationships, and both statistical outputs explicitly record every `S001`-`S020` as complete. Cross-source review covers 19 named result or definition families across the four scientific PDFs.
- Statistical pass 1 is `/root/statistical_pass_1` and statistical pass 2 is `/root/statistical_pass_2`. They are distinct fresh runtime IDs, each recorded as `gpt-5.6-terra` with `high` reasoning effort and one primary artifact. The quality auditor is separately recorded as `/root/quality_control_auditor`, `gpt-5.6-sol`, `high`, `FRESH_SPAWN`.
- All five direct-source hashes and all 30 reused-asset hashes were recomputed during this audit and matched their before-review ledgers.
- The coverage manifest contains all 12 required stages, exactly one plain relative artifact path per row, complete explicit `N`, `S`, and `C` scopes where required, and no ID-range shorthand. The `evidence_quality` and `report_generation` rows remain pending because coordinator finalization and report generation follow this audit.

## Required coordinator repairs before report finalization

1. In `extraction/support_quantitative_evidence.md`, change each of the nine direct-PDF link prefixes from `../../` to `../../../`. The current links resolve below `.ai_paper_validation/` instead of the package root. The affected displayed pages are PDF-002 pages 2, 5, 6, and 12; PDF-003 pages 2 and 9; and PDF-004 pages 2, 5, and 6.
2. In `checkers/numeric_consistency.md`, change each of the eleven direct-PDF link prefixes from `../../` to `../../../`. All eleven current links resolve below `.ai_paper_validation/` rather than to the package-root PDFs. The candidate-ledger, statistical-inventory, cross-source, and evidence-recheck links tested as resolvable.
3. In `source_coverage.md`, replace the statement that mapped units mean only inventory assignments. At the current completed stage, explain that each mapped count is supported by the complete main or support scientific map, including explicit no-applicable units and the required structural exclusion. The numeric rows are closed, but their current explanatory sentence understates the completed scientific mapping required by the contract.
4. For C005 in `candidate_ledger.md`, add PDF-001 page 3 as the article's primary-outcome randomization-origin evidence. Retain PDF-001 page 6 only as secondary-outcome context and state that footnote `g` attaches to the hospital-stay row, not directly to the primary SAE row. This prevents false source attribution while preserving C005.
5. In the evidence recheck and final report, keep alternatives source-grounded. For C001, do not present the unsupported possibility of no exactly-one-SAE infants as a source-grounded alternative; it is only an unresolved logical condition. For C004, do not present the unsupported possibility of no exactly-28-week infants as source-grounded; retain the SAP's own page 8 `>=28` usage and the displayed complete partition as the grounded alternative context. For C002, keep the SAP's explicit correction and page-12 mean/median distinction; describe unprovided drafting or amendment history only as a limitation. For C003, describe an unprovided amendment only as a limitation, not evidence.
6. Soften the C001 recheck question from assuming that every conflicting label must be version-qualified to asking whether any location requires correction, clarification, or version qualification. Apply the same nonprescriptive construction to C002's proposed version note.
7. After this audit, change the coverage-manifest `evidence_quality` row to `COMPLETE`. When the fresh report generator is spawned, append it exactly once to `agent_execution_manifest.md` with its distinct runtime ID, required model and effort, `FRESH_SPAWN`, and one primary artifact; then complete the report-generation coverage row. The current execution manifest is complete through this audit but does not yet contain the pending report-generator stage.

## C001 — Primary SAE endpoint is labeled `>1` and `>=1` or “any” for matched results

- **Evidence support:** Source text and matched 44/159 and 27/149 results were found at PDF-001 page 6 and PDF-004 page 5; the competing protocol and SAP definitions were also found. The percentage calculations and integer-set comparison reproduce correctly.
- **Assumptions and alternatives:** The direct contradiction is the printed threshold label attached to matched counts. Informal use of `>1` for more than zero is supported as a possible interpretation by repeated “any,” “at least one,” and `>=1` wording. The absence of infants with exactly one SAE is not supplied evidence and must remain a named missing input, not a source-grounded alternative.
- **Arithmetic, pagination, and duplication:** Arithmetic is correct and cited physical PDF pages exist. C001 is not a duplicate of C004 because the endpoint, comparator, and consistency rule concern SAE count thresholds rather than a gestational-age partition. It is not a duplicate of C005 because the latter concerns the observation-window origin.
- **Category and impact boundary:** `Measure, label, or scale inconsistency` is an allowed category. The package does not establish that the analyzed numerator or paper-level conclusion changes. If confirmed, a data extractor could copy the wrong endpoint threshold alongside 44/159 and 27/149; no actual propagation is claimed.
- **Missing final evidence-card fields:** Add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. Existing category, locations, source evidence, alternative interpretation, and human question can be adapted under the report specification.

## C002 — Planned median hospital-day values conflict across protocol and SAP locations

- **Evidence support:** Protocol page 3 prints medians 18/15; protocol page 12 prints medians 8/5 and means 18/13; SAP page 3 explicitly calls 18/15 incorrect and identifies 8/5 as intended. The calculations `18 - 15 = 3`, `8 - 5 = 3`, `18 - 8 = 10`, and `15 - 5 = 10` reproduce.
- **Assumptions and alternatives:** The page-12 mean/median distinction and SAP clarification are source-grounded. Drafting history, amendment timing, and executable power inputs are not supplied and must remain limitations. The card must not presume that a correction or version note is the human outcome.
- **Arithmetic, pagination, and duplication:** Arithmetic and physical pages are correct. C002 concerns arm-specific prospective design medians and is distinct from observed hospital-day results and from all other stable relationships.
- **Category and impact boundary:** `Cross-document numeric inconsistency` is an allowed category. The preserved three-day contrast does not establish any change to the observed trial result or conclusion. If confirmed, an evidence extractor or replication reviewer could copy the wrong arm-specific planning medians; no downstream use is assumed.
- **Missing final evidence-card fields:** Add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The ledger's existing calculation should be placed under the exact `Calculation` label.

## C003 — Bayesian intervention-prior ranges differ between the article and SAP

- **Evidence support:** PDF-001 page 4 prints a common 0.33-3.0 intervention-effect range for categorical and count outcomes. PDF-003 page 8 prints categorical OR 0.2-4 with log-OR Normal(0, 0.7) and count RR 0.33-3.3. The endpoint differences reproduce directly.
- **Assumptions and alternatives:** The recheck's exponential calculation is explicitly diagnostic and arithmetically reproducible, but the exact quantile and rounding convention are not supplied. It is unnecessary to establish the printed cross-source mismatch and should not be used to infer the fitted prior. Any amendment, simplification, or outcome-specific implementation remains unprovided.
- **Arithmetic, pagination, and duplication:** Endpoint subtractions are correct and the pages exist. C003 is the only prior-specification relationship and is not duplicated by a model-label or subgroup candidate.
- **Category and impact boundary:** `Statistical reporting inconsistency` is an allowed category. The sources do not establish which prior was fitted or that any estimate or conclusion changes. If confirmed, a replication or evidence-synthesis reader could copy the wrong stated prior; no propagated error is claimed.
- **Missing final evidence-card fields:** Add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`.

## C004 — Gestational-age subgroup boundary is printed as `>=28` and `>28` weeks

- **Evidence support:** PDF-001 page 8 prints `<28` and `>=28` with subgroup counts that sum to 159 and 149. PDF-003 pages 3 and 9 print `<28` and `>28`, while PDF-003 page 8 itself prints `<28` and `>=28`. The truth-value comparison at exactly 28 and both denominator sums reproduce.
- **Assumptions and alternatives:** The SAP's internal `>=28` wording and the article's complete displayed partition support a possible label inconsistency. The number of infants recorded exactly at 28 weeks, representation in weeks and days, and analysis code are missing; their values must not be assumed.
- **Arithmetic, pagination, and duplication:** Arithmetic and pages are correct. C004 is a gestational-age boundary relationship and is distinct from C001's SAE threshold and C005's time-window origin.
- **Category and impact boundary:** `Measure, label, or scale inconsistency` is an allowed category. No supplied evidence shows that any infant was reassigned or that the subgroup estimates or paper conclusion change. If confirmed, an extractor could copy the wrong subgroup boundary with the reported subgroup effects; no actual propagation is claimed.
- **Missing final evidence-card fields:** Add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`.

## C005 — Primary-outcome time origin is labeled enrollment and randomization

- **Evidence support:** PDF-002 pages 3 and 11 print enrollment-based windows; PDF-003 page 7 prints randomization to 10 months after randomization; PDF-001 page 3 states that data were collected for 10 months after randomization. The symbolic comparison of `[E, E + 10 months]` with `[R, R + 10 months]` is logically correct.
- **Assumptions and alternatives:** The protocol's own mixed enrollment/randomization terminology supports possible interchangeable usage, but operational simultaneity is not established. Paired timestamps, case-report-form rules, executable event-window code, and boundary-event counts are missing. No numeric impact may be inferred.
- **Arithmetic, pagination, and duplication:** The cited pages exist, but the candidate ledger must repair the PDF-001 page-6 attribution as directed above. C005 concerns time origin and is distinct from C001's event threshold even though both affect the primary-outcome definition.
- **Category and impact boundary:** `Measure, label, or scale inconsistency` is an allowed category. The package does not establish a difference in event inclusion, estimates, or paper conclusion. If confirmed, an extractor could copy an incorrect primary-outcome observation window; no downstream effect is assumed.
- **Missing final evidence-card fields:** Add the exact labels `Candidate statement`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`.

## Human-adjudication placeholder control

No current ledger card contains human-adjudication subfields, so none can yet be certified in place. Every final card for C001-C005 must include exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No dash, checkbox, prose value, inferred disposition, or alternative blank marker may replace `__`.

## Limitations

- This audit confirms reporting evidence, reproducibility, coverage, and neutral card construction from the supplied package only. It does not assign a scientific or human disposition.
- Raw data, final model code, endpoint and observation-window code, paired enrollment/randomization timestamps, exact gestational-age coding, and amendment history are not supplied. Those absences bound the five human questions and do not authorize suppression of any stable ID.
- Report-generation, final token accounting, final hash ledgers, HTML rendering, and mechanical validation occur after this audit and were therefore not available for final-state confirmation here.
