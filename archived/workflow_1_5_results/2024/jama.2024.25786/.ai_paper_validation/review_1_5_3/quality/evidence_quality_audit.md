# Final Evidence-Quality Audit

## Audit outcome

- **Audit status:** `AUDIT_COMPLETE_WITH_COORDINATOR_COMPLETION_ACTIONS`.
- **Stable candidate set audited:** C001, C002, C003, C004, C005, C006, C007, and C008. The ledger and mechanical recheck contain the same eight IDs, and every ID is returned below. No ID is deleted, merged, ranked, suppressed, renumbered, or assigned severity, validity, acceptance, exclusion, correction, or scientific disposition.
- **Candidate state:** Every candidate remains `Pending Human Adjudication`.
- **Direct-source coverage:** Five supplied PDFs; 144/144 PDF-page units mapped. Each source row closes because reusable units plus fresh-required units equal total units and mapped units equal total units: 144 reusable + 0 fresh-required = 144 total = 144 mapped. Main mapping covers 11/11 pages; the two disjoint support shards cover 52/52 and 81/81 pages.
- **Relationship coverage:** N001-N069 are present and the numeric checker covers all 69. S001-S036 are present; every S record has both `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. The cross-source checker records 29 matched quantitative relationships and 11 protocol/SAP planning or definition relationships. No stated relationship count or source-unit count was used as a candidate limit.
- **Discovery boundary:** The durable mapping and inventory artifacts expressly restart discovery from source-linked reusable evidence and complete direct-source assignments. They state that no old candidate, checker, verifier, critic, quality-decision, or final-report conclusion was used as a scientific input. The current ledger has eight candidates without a top-N, desired-count, review-queue, or early-stopping rule.
- **Routing and execution:** `routing_preflight.md` reports `PASS`, coordinator `gpt-5.6-sol`/`high`, execution mode `INTERACTIVE_CLI`, coordinator inference `PASS`, and all nine named presets verified. Statistical pass 1 uses fresh runtime `/root/statistics_pass_1`; pass 2 uses the distinct fresh runtime `/root/statistics_pass_2`. Both are recorded as `gpt-5.6-terra`/`high` with one primary artifact each. All mandatory runtime IDs manifested through this audit stage are distinct.
- **Source integrity:** Direct-source and reused-artifact baselines were rechecked with `sha256sum -c`; all five direct PDFs and all 38 inventoried reusable artifacts matched their recorded hashes.
- **Display-zero rule:** No supplied inferential P value is printed as `P = 0`, `p = 0.000`, or equivalent. No C ID is based on display-zero notation, finite precision, underflow, or mathematical nonzero-tail reasoning. C002 concerns a zero event numerator, and C008 concerns a doubled count separator; neither is a P-value display-zero case. No candidate requires the conditional `Independent contradiction beyond P=0 display` field.
- **Categories and tone:** Every ledger category exactly matches `QUALITY_CONTROL_SCOPE.md`. The wording is neutral quality control, separates direct observation from inference, and makes no paper-level conclusion claim.

## Coverage-manifest and reproducibility audit

Every current coverage row is `COMPLETE`, each `Artifact` cell contains one undecorated relative POSIX path, both support shard parts have separate rows, both statistical rows enumerate all 36 S IDs, and the candidate-registration, evidence-recheck, and evidence-quality rows explicitly enumerate C001-C008. The evidence-quality row names the single plain path `quality/evidence_quality_audit.md`. The coordinator must add the required `report_generation` row with the same explicit ID set and its one report-generation artifact after report assembly. That later row is a stage-completion action, not a scientific-coverage gap.

The coordinator repaired all 57 source-PDF links in `extraction/main_quantitative_evidence.md` from bare filenames to paths that resolve from the artifact directory. Candidate-ledger, checker, and recheck PDF links also resolve and end in truthful `#page=N` fragments. Direct extraction from the cited pages reconfirmed all candidate strings: Supplement 2 pages 15, 17, 20, 24, and 25 and main-article pages 3 and 8. No candidate has false pagination.

The coordinator repaired the stale opening narrative in `source_coverage.md`. It now states that the completed main and support mappings inspected every assigned unit and that mapped units equal total units for every direct source. The table counts and `COMPLETE` statuses remain correct.

## Evidence-card completion rule

The candidate ledger is a registration artifact, not the final card artifact. For every C ID below, the final report must add or relabel the following exact evidence-card fields that are not yet present as separate exact labels in the ledger: `Candidate statement`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, a separate `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The recheck and checker artifacts contain supportable material for these fields. Each final card must use exactly:

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

No human field may contain a dash, checkbox, inferred answer, or AI disposition. Potential downstream impact must identify only what a data extractor, systematic review, meta-analysis, or guideline could copy if the candidate is confirmed; it must not state that propagation, harm, or conclusion change occurred.

## C001 — Liberal walk-in transport percentage does not reconcile with 4/743

- **Category audit:** `Denominator, proportion, or total inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Supplement 2, PDF p. 15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15) directly prints `4/743 (5.3)` under `no./total no. (%)`. `100 × 4 / 743 = 0.538358...%`, which rounds to `0.5%` at one decimal, not `5.3%`. Arithmetic is correct and reproducible.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** Which of the count, denominator, or percentage is incorrect is unsupported and must remain an open human question. No alternate denominator is printed for this cell.
- **Duplicate audit:** C001 shares a page and general percentage rule with C002 but concerns a different row and different printed values. It is not a duplicate.
- **Impact boundary:** No paper-level conclusion impact is established. A bounded final statement may say that a baseline-characteristics extractor could copy either `5.3%` or a percentage derived from `4/743` if the cell is not clarified.

## C002 — Liberal vascular-surgery percentage is nonzero with a printed zero numerator

- **Category audit:** `Denominator, proportion, or total inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Supplement 2, PDF p. 15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15) directly prints `0/747 (1.1)` under `no./total no. (%)`. `100 × 0 / 747 = 0.0%`. Arithmetic is exact and reproducible.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** A typographic zero or carried-over percentage is only a possible explanation. The intended numerator and percentage are not supplied. This zero is a count, not a P value.
- **Duplicate audit:** C002 is distinct from C001 because it concerns vascular surgery and a zero-numerator identity rather than the walk-in cell.
- **Impact boundary:** No paper-level conclusion impact is established. A bounded final statement may identify possible copying of an unresolved rare baseline frequency into an extraction table.

## C003 — Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7

- **Category audit:** `Cross-document numeric inconsistency` is an exact allowed category and is used for a matched result across separate supplied locations.
- **Evidence and calculation:** [Supplement 2, eTable 4, PDF p. 17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17) prints `0.98 (0.68 to 1.41)`; [Supplement 2, eTable 7, PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) prints `0.98 (0.68 to 1.39)`. The displayed upper endpoints differ by `1.41 - 1.39 = 0.02`; the population counts, outcome, effect label, point estimate, lower endpoint, and precision match.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** Identical fitted-model identity is not established. The final card must preserve the conditional rule: if the models are identical, the endpoints conflict; if they differ, the supplied labels do not state the distinction needed for a same-result comparison. It must not assert model equality, reconstruct a P value, or select an authoritative endpoint.
- **Duplicate audit:** C003 is not duplicated by C004 or C005; it concerns an adjusted CI endpoint and a missing model distinction rather than a raw subgroup percentage.
- **Impact boundary:** No conclusion change is established. A bounded final statement may say that an adjusted-effect extractor could copy either upper CI endpoint, which could affect an extracted precision field if the candidate is confirmed.

## C004 — AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4

- **Category audit:** `Cross-document numeric inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Main article, Figure 4, PDF p. 8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8) prints `48/473 (10.1)`; [Supplement 2, eTable 7, PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) prints `48/473 (9.2)`. `100 × 48 / 473 = 10.147991...%`, which rounds to `10.1%` at one decimal. Arithmetic and matched-location identity are reproducible.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** An undisclosed analytic denominator or a transcription mechanism is not established. The printed denominator is 473 in both locations.
- **Duplicate audit:** C004 and C005 use the same figure/table comparison class but concern different subgroup rows, numerators, denominators, percentages, and arithmetic. They are not duplicates.
- **Impact boundary:** No paper-level or subgroup-conclusion impact is established. A bounded final statement may identify possible copying of `9.2%` rather than the count-derived and matched `10.1%` into subgroup extraction.

## C005 — Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4

- **Category audit:** `Cross-document numeric inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Main article, Figure 4, PDF p. 8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8) prints `14/69 (20.3)`; [Supplement 2, eTable 7, PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20) prints `14/69 (20.2)`. `100 × 14 / 69 = 20.289855...%`, which becomes `20.3%` under ordinary nearest rounding to one decimal.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** The package does not state a publication-wide rounding convention. The final card must say that ordinary nearest rounding gives 20.3% and retain truncation or production-time rounding as an alternative; it must not present a production mechanism as fact.
- **Duplicate audit:** C005 is distinct from C004 because it concerns a different subgroup row and a different numeric relation.
- **Impact boundary:** No conclusion impact is established. A bounded final statement may identify possible copying of either one-decimal subgroup percentage if the discrepancy is not clarified.

## C006 — Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1

- **Category audit:** `Cross-document numeric inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Supplement 2, eTable 10, PDF p. 24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24) prints `N=130`, restrictive `55/750 (45)`, and liberal `67/758 (55)`. [Main article, Figure 1, PDF p. 3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3) prints 59 and 71 exclusions. `55 + 67 = 122`; `130 - 122 = 8`; `59 + 71 = 130`; and each figure count exceeds its table count by 4. The table percentages also reproduce from the 122 classified counts: `55/122 = 45.08%` and `67/122 = 54.92%`.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** The exact four-person difference in each group is compatible with omission of the four Swiss-law consent-withdrawal cases shown in each Figure 1 branch, but eTable 10 does not state that rule. The final card must label this as an alternative interpretation, not a resolved explanation.
- **Duplicate audit:** C006 and C007 are on the same table page but concern different rows and rules: C006 is the 130-versus-122 postrandomization-exclusion total; C007 is the denominator concept used for secondary-exclusion percentages. They are not duplicates.
- **Impact boundary:** No effect-estimate or conclusion impact is established. A bounded final statement may identify possible copying of inconsistent participant-flow totals or group exclusion counts.

## C007 — Secondary-exclusion cells pair within-group denominators with cross-group partition percentages

- **Category audit:** `Denominator, proportion, or total inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Supplement 2, eTable 10, PDF p. 24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24) prints `N=341`, `174/750 (51)`, and `165/758 (49)`; [Main article, Figure 1, PDF p. 3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3) matches counts 174 and 165. `174 + 165 = 339`, and the two missing randomized-oxygen assignments explain `341 - 339 = 2`. The printed cell denominators yield `174/750 = 23.2%` and `165/758 = 21.8%`, whereas the printed percentages reproduce from the classified total: `174/339 = 51.3%` and `165/339 = 48.7%`.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** The intended estimand is not supplied. The final card must not choose between within-group exclusion incidence and allocation distribution among classified exclusions, and must state how the two missing assignments remain to be presented.
- **Duplicate audit:** C007 is distinct from C006 because the printed values, comparator, and denominator rule differ.
- **Impact boundary:** No paper-level conclusion impact is established. A bounded final statement may identify possible copying of 51%/49% as within-group rates or of 23.2%/21.8% as allocation shares if the denominator concept is not clarified.

## C008 — Missing-as-event primary count uses a doubled numerator/denominator separator

- **Category audit:** `Measure, label, or scale inconsistency` is an exact allowed category.
- **Evidence and calculation:** [Supplement 2, eTable 11, PDF p. 25](../../../joi240147supp2_prod_1738701765.29201.pdf#page=25) visibly and extractably prints `135//750 (18.0)` while the table convention and paired cell use a single slash. `100 × 135 / 750 = 18.0%`, so the numeric relationship reconciles; the reproducible observation is the doubled separator. High-resolution rendering, raw text, bounding-box extraction, and targeted CPU OCR independently retain both slash glyphs.
- **Missing final-card fields:** Candidate statement; separately labelled source evidence, reported-versus-comparator, reasoning procedure, and calculation; mechanical recheck; quality-control relevance; bounded downstream impact; verification steps; and the exact five blank human-adjudication subfields.
- **Assumption boundary:** The package does not establish whether the duplicate glyph arose in the source string, typesetting, encoding, or another production stage. The final card must not assert that a downstream extraction error occurred or that the publication intended a particular corrected string.
- **Duplicate audit:** C008 is distinct from every arithmetic or cross-location candidate because its count/percentage arithmetic is compatible and its rule concerns notation consistency.
- **Impact boundary:** No numeric estimate or conclusion impact is established. A bounded final statement may say that a machine or manual extractor could retain the malformed separator if the display is copied verbatim.

## Coordinator completion actions

1. Generate every final evidence card with all exact report-spec labels, the source-grounded limits above, bounded downstream language, and the exact five `__` human placeholders.
2. Add the required `report_generation` manifest row with the full explicit C001-C008 set and one plain artifact path after report assembly; add the fresh report-generator runtime to the execution manifest.
3. Complete post-report source and reused-artifact hash checks, token accounting, HTML rendering, and final validation. These later workflow artifacts do not yet exist or are not yet final, so this audit cannot attest to their eventual contents.

## Limitations

No raw data, table-production code, fitted-model objects, unrounded estimates, covariance matrices, IP weights, or publication production files were supplied. Consequently, the authoritative corrected fields for C001-C008, exact model identity for C003, rounding convention for C005, flow-population definitions for C006-C007, and production cause for C008 require human verification. Durable artifacts document the nonuse of legacy candidate conclusions, but an artifact audit cannot independently observe unrecorded private reasoning. These limitations do not leave a direct-source-unit, N-relationship, S-relationship, stable-ID, or mechanical-recheck coverage gap.
