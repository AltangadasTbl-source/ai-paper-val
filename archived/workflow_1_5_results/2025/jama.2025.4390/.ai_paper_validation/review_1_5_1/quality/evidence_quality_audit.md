# Evidence Quality Audit

This quality-control audit covers the complete Workflow 1.5.1 scientific record available at the audit cutoff: the four-source coverage ledger, coverage manifest, quantitative evidence maps, `N001`-`N067` and `S001`-`S035` relationship inventories, numeric and cross-source checker outputs, both statistical passes, candidate ledger, evidence recheck, and agent execution manifest. The stable candidate set is `C001`, `C002`, and `C003`. Every candidate remains **Pending Human Adjudication**.

## Coverage audit

### Direct-source closure

| Source | Total units | Reusable scientific units | Fresh-required units | Mapped units | Audit check |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 0 | 12 | 12 | Closed |
| DOC-002 | 18 | 0 | 18 | 18 | Closed |
| DOC-003 | 7 | 0 | 7 | 7 | Closed |
| DOC-004 | 49 | 0 | 49 | 49 | Closed |
| **Package** | **86** | **0** | **86** | **86** | **Closed** |

For every direct-source row, reusable scientific units plus fresh-required units equal total units, mapped units equal total units, and the source ledger records `COMPLETE`. All 86 fresh-required PDF pages are assigned to and represented in page-complete mapper artifacts. No scientific source unit remains uncovered.

The source and evidence-asset inventories show that legacy derivatives were used only for provenance/fitness assessment: source-mismatched assets were marked stale, source-matched metadata without scientific extraction was not credited as reusable scientific coverage, and all pages were freshly mapped. Discovery was count-unbounded and rebuilt from the direct sources; no old candidate selection or review queue controlled the mapped relationships or checker scope.

### Relationship and checker closure

- The numeric inventory contains `N001`-`N067`; the numeric checker returns an explicit outcome for 67/67 relationships.
- The statistical inventory contains `S001`-`S035`; both statistical artifacts return an explicit completion record for 35/35 relationships.
- The cross-source checker covers all 67 numeric and all 35 statistical relationships.
- The numeric and cross-source checkers produced three distinct supportable proposals. Statistical pass 1 independently reproduced the two proposals with statistical implications; statistical pass 2 found no additional distinct proposal after reviewing the complete cross-lane ledger and recheck. All three distinct proposals are registered once as `C001`, `C002`, and `C003`.
- Ledger, evidence-recheck, and this quality-audit ID sets are identical: `C001`, `C002`, `C003`. Every stable ID has a complete direct-source mechanical recheck.
- No candidate is based on a display-zero P value. The only relevant very-small-P notation is inequality notation recorded as `DISPLAY_ZERO_NOT_CANDIDATE` in statistical pass 2; it has no role in `C001`-`C003`.

### Statistical execution audit

The execution manifest records two distinct fresh statistical agents:

| Pass | Agent ID | Model | Effort | Start mode | Relationships |
|---|---|---|---|---|---|
| Statistical pass 1 | `/root/statistics_pass_1` | `gpt-5.6-terra` | `high` | `FRESH_SPAWN` | S001-S035, 35/35 |
| Statistical pass 2 | `/root/statistics_pass_2` | `gpt-5.6-terra` | `high` | `FRESH_SPAWN` | S001-S035, 35/35 |

The runtime IDs are different, and neither statistical pass reused a mapper or checker agent.

### Coverage-manifest path and stage audit

Every currently recorded coverage row contains exactly one plain POSIX-style relative artifact path. All scientific mapping, relationship checking, candidate registration, evidence recheck, and statistical-pass rows enumerate their complete assigned source, `N`, `S`, or `C` scope without a count boundary.

Two expected downstream bookkeeping repairs remain before workflow completion:

1. After this artifact is accepted, change the existing `evidence_quality` row from `ASSIGNED` to `COMPLETE`; retain the exact enumerated scope `C001, C002, C003` and the single path `quality/evidence_quality_audit.md`.
2. After the report is generated, add a `report_generation` coverage row with exact scope `C001, C002, C003`, exactly one plain relative artifact path, and `COMPLETE`. Add the report-generator runtime agent to `agent_execution_manifest.md` exactly once when that agent is spawned. These downstream records were not yet available at the audit cutoff.

## C001 — Figure 3 all-patient rate-column conflict with the matched primary-outcome rate

**Status:** Pending Human Adjudication

**Category audit:** `Cross-document numeric inconsistency` is an allowed primary category and accurately describes the repeated primary result across the main-paper figure, table, abstract, and narrative. A measure/label/scale implication is present but does not require a second primary category or a duplicate candidate.

**Exact evidence and pagination audit:** The cited values are present in the current sources at [DOC-001 Figure 3 — PDF p. 9](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9>), [DOC-001 Table 2 — PDF p. 8](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8>), [DOC-001 abstract — PDF p. 1](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1>), and [DOC-001 primary-outcome narrative — PDF p. 6](<../../../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6>). All links resolve to the 12-page current PDF, and no false pagination was found.

**Arithmetic and relationship audit:** Figure 3 prints the same all-patient composite outcome, arm order, event counts `163/173`, and HR `0.96 (0.77-1.19)` as the matched primary analysis, but prints `71.0/71.0` under columns labeled `Rate per 100 patient-years`. Table 2 prints `2.30/2.44`, and the abstract/narrative print `2.3/2.4`, under the same rate unit. Ordinary rounding reconciles the table with the prose but cannot reconcile `71.0` with either matched rate. The recheck's exposure-scale calculation is reproducible: `163/7100*100=2.2958` and `173/7100*100=2.4366`; this is explicitly a diagnostic alternative, not proof of the intended figure measure.

**Observation/inference audit:** Directly observed printed values are kept separate from the possible explanations of an unlabeled exposure quantity, a mislabeled header, or a production/transcription error. The ledger does not prescribe a replacement. One wording repair is required in the eventual report: do not repeat the ledger phrase `validated primary-outcome analysis`, because the package establishes a matched comparator but does not establish which display is authoritative. Use `matched primary-outcome analysis` and retain the recheck's neutral human question.

**Assumption, duplication, and impact audit:** No unsupported statistical model or exact person-time denominator is assumed. `N003`, `N030`, `S001`, `S005`, `S007`, `S010`, and `S017` are correctly linked as occurrences of the same relationship; the shared Figure 3 column problem across subgroup rows is not split into duplicate candidate IDs. Paper-level conclusion change is not established. A bounded downstream statement is supportable: if confirmed, a data extractor could copy `71.0` as an event rate or reuse the figure's mislabeled subgroup column.

**Missing final-report evidence-card fields:** The ledger contains the necessary substance, but it does not use all exact final-report labels. The report generator must add or normalize `Category`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The mechanical recheck should be summarized from the dedicated recheck artifact, and the downstream statement must remain conditional and bounded as above.

**Human verification steps audited:** Inspect the locked Figure 3 production dataset and specification; identify the intended quantity and denominator for every displayed `71.0`-partitioning field; calculate arm-specific rates from exact person-time; then verify the values and header together.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Bedtime-diuretic six-month timing count triplets differ between eFigure 4 and eTable 6

**Status:** Pending Human Adjudication

**Category audit:** `Cross-document numeric inconsistency` is an allowed primary category and fits the same six-month medication-class relationship displayed in a figure and table. The denominator/proportion implication is secondary and does not warrant a duplicate candidate.

**Exact evidence and pagination audit:** The direct figure values are present at [DOC-004 eFigure 4 — PDF p. 26](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=26>), and the comparator is present at [DOC-004 eTable 6 — PDF p. 42](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=42>) in the current 49-page PDF. The table begins on PDF page 41, as stated. Both links and page references are reproducible.

**Arithmetic and relationship audit:** For the same bedtime allocation, six-month time point, diuretic class, and three timing categories, eFigure 4 prints `278/138/8` and eTable 6 prints `277/139/8`. Both sum to the same total: `278+138+8=424` and `277+139+8=424`. The table percentages reproduce its counts: `277/424=65.33%`, `139/424=32.78%`, and `8/424=1.89%`, displayed as `65.3%`, `32.8%`, and `1.9%`. The figure's first two counts would instead yield `65.6%` and `32.5%`. The discrepancy is one medicine exchanged between two categories, not a rounding artifact.

**Observation/inference audit:** The two printed triplets and their common total are direct observations. Recoding, different undisclosed data locks, and production transcription are explicitly alternatives; none is asserted as fact, and no intended replacement is prescribed.

**Assumption, duplication, and impact audit:** The exact matched population/time/class/category keys are supplied. `N058` and `N064` are the two sides of one relationship and are correctly merged as one stable ID. No statistical P-value issue is implied. Paper-level conclusion change is not established. A bounded downstream statement is supportable: if confirmed, a data extractor could copy one incorrect class-specific adherence numerator and calculate a correspondingly incorrect percentage.

**Missing final-report evidence-card fields:** The ledger contains the necessary substance, but it does not use all exact final-report labels. The report generator must add or normalize `Category`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The conditional downstream language above should be used without claiming observed propagation.

**Human verification steps audited:** Compare the locked medication-level extracts, data-freeze dates, and coding rules used for eFigure 4 and eTable 6; identify the single discrepant medication record; confirm the intended category; then regenerate or relabel the affected display as authorized by a human reviewer.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 5 `Other` ethnicity row duplicates White/Caucasian values and exceeds randomized `Other` totals

**Status:** Pending Human Adjudication

**Category audit:** `Numeric or arithmetic inconsistency` is an allowed primary category and fits the duplicated counts and parent-subset count conflict. A label implication is present but does not require a duplicate candidate.

**Exact evidence and pagination audit:** The duplicated subgroup rows are present at [DOC-004 eTable 5 — PDF p. 37](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=37>), and the randomized parent-arm category totals are present at [DOC-004 eTable 3 — PDF p. 29](<../../../joi250019supp3_prod_1749674951.30054.pdf#page=29>). Both links resolve to the current 49-page source, and the cited pagination is accurate.

**Arithmetic and relationship audit:** eTable 5 states morning `n=44` and bedtime `n=57`, then prints both White/Caucasian and `Other` as morning `40 (90.9%)` and bedtime `53 (93.0%)`. Those percentages reproduce the duplicated counts: `40/44=90.91%` and `53/57=92.98%`. eTable 3 prints only `5` morning and `9` bedtime participants as `Other` in the full randomized arms. Under the same category definition, the subgroup-to-parent comparisons are impossible: `40>5` and `53>9`. The exact eTable 3 ethnicity counts also sum to their randomized-arm totals, supporting the displayed categorical structure.

**Observation/inference audit:** Duplication and the printed parent totals are direct observations. Copying, row misalignment, or an undisclosed category recoding are explicitly possible explanations. The missing data dictionary prevents an assertion that the intended replacement values are known, and the ledger correctly leaves that question to human review.

**Assumption, duplication, and impact audit:** The candidate is conditional on a common `Other` category definition, and the missing definition is explicitly named. `N063` and the `S034` table context are correctly represented once; the associated ethnicity P value is not promoted to a separate candidate because its test definition and corrected input row are unavailable. Paper-level conclusion change is not established. A bounded downstream statement is supportable: if confirmed, a data extractor could copy the duplicated subgroup counts or reuse an ethnicity-comparison result based on an incorrect displayed row.

**Missing final-report evidence-card fields:** The ledger contains the necessary substance, but it does not use all exact final-report labels. The report generator must add or normalize `Category`, `Source evidence`, `Reported-versus-comparator`, `Reasoning procedure`, `Calculation`, `Mechanical evidence recheck`, `Quality-control relevance`, `Potential downstream evidence impact`, `Human verification steps`, and `Human adjudication fields`. The report must preserve the category-definition uncertainty and must not assert corrected counts or a corrected P value.

**Human verification steps audited:** Inspect the eTable 5 analysis export and participant-level baseline ethnicity coding for the morning `n=44` and bedtime `n=57` cohort; confirm whether coding matches eTable 3; recover the intended `Other` cells; and rerun the associated ethnicity comparison if the displayed inputs change.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Audit summary and coordinator repair note

- **Stable IDs audited:** C001, C002, C003 (3/3).
- **Direct-source support:** All three candidates have exact current-source support, correct PDF pagination, reproducible comparisons, and applicable quality-control categories.
- **Candidate-level supportable omissions:** No additional distinct candidate is supportable from the checker proposals. No candidate should be deleted, merged, renumbered, ranked, or assigned a scientific disposition.
- **Wording repair:** One final-report wording repair is required for C001: replace the implication that the Table 2 result is already `validated` with neutral matched-comparator wording.
- **Evidence-card assembly repairs:** For each of C001-C003, populate every exact final-report field listed above, carry over the mechanical recheck, use the bounded conditional downstream statement, and preserve all five human fields exactly as `__`.
- **Workflow bookkeeping repairs:** Mark `evidence_quality` complete after accepting this artifact; add the complete `report_generation` row and the report-generator agent record after those downstream actions occur.
- **Limitations:** The supplied package lacks the Figure 3 production dataset and exact person-time fields, medication-level version/coding history, eTable 5 export/data dictionary, and row-specific test outputs. These limitations prevent selection of intended replacement values but do not prevent reproduction of the printed inconsistencies.
