# Quantitative Quality-Control Consistency Review — jama.2025.4390

## Pending Human Adjudication

**All three candidate consistency issues in this report are Pending Human Adjudication.** This review is a quantitative reporting quality-control aid. It does not determine validity, importance, a correction, or any paper-level conclusion.

## Executive Quality-Control Summary

Complete source coverage identified **3** distinct, source-grounded quantitative reporting candidates: C001, C002, and C003. The candidates concern a figure rate-column conflict, a medication-timing count discrepancy between a figure and table, and a duplicated subgroup ethnicity row whose printed counts conflict with parent-arm totals. No candidate was registered for a display-zero P value alone.

The review found no basis to state that any candidate changed the paper's conclusion, propagated to another product, or caused harm. Small preventable reporting defects can nevertheless matter if a downstream evidence extractor copies a displayed number, label, denominator, or measure without its surrounding context.

## Package and Reused-Evidence Provenance

The direct-source package comprises four PDFs: the 12-page main article, an 18-page protocol supplement, a 7-page statistical analysis plan supplement, and a 49-page results supplement. Current source SHA-256 values are recorded in [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>).

One hundred eight pre-existing evidence assets were hashed before review. Six source-matched metadata records were usable as locators, two renders were partial, and 100 assets were stale; none was accepted as reusable scientific page coverage. In particular, legacy derivatives for DOC-001 and DOC-004 did not match the current source identities. The retained assets are documented as provenance in [evidence_asset_inventory.md](<review_1_5_1/evidence_asset_inventory.md>), not as final evidentiary authority.

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 12 PDF pages | 0 | 12 | 12 | COMPLETE |
| DOC-002 protocol supplement | 18 PDF pages | 0 | 18 | 18 | COMPLETE |
| DOC-003 SAP supplement | 7 PDF pages | 0 | 7 | 7 | COMPLETE |
| DOC-004 results supplement | 49 PDF pages | 0 | 49 | 49 | COMPLETE |
| **Total** | **86** | **0** | **86** | **86** | **COMPLETE** |

Every direct-source page was freshly mapped from the current PDFs. The complete stage and shard partition is retained in [coverage_manifest.md](<review_1_5_1/coverage_manifest.md>). This review assessed supplied-package numeric, denominator, rate/count, label/scale, inferential, and cross-document consistency. It did not undertake a broad clinical, methodology, misconduct, raw-data, or external-literature audit.

## Quantitative and Statistical Relationship Coverage

The numeric/reporting map covers all **67** relationships, `N001` through `N067`, in [numeric_relationship_inventory.md](<review_1_5_1/relationships/numeric_relationship_inventory.md>). The inferential-statistical map covers all **35** relationships, `S001` through `S035`, in [relationship_inventory.md](<review_1_5_1/statistics/relationship_inventory.md>).

Both independent statistical passes completed all 35 relationships. Pass 1 was performed by `/root/statistics_pass_1` and pass 2 by the distinct `/root/statistics_pass_2`; both used `gpt-5.6-terra` at high reasoning effort. The pass records are [statistical_pass_1.md](<review_1_5_1/checkers/statistical_pass_1.md>) and [statistical_pass_2.md](<review_1_5_1/checkers/statistical_pass_2.md>). No display-zero-only candidate was registered; the only display-zero item considered in pass 2 was recorded as `DISPLAY_ZERO_NOT_CANDIDATE`.

## Candidate Index

| Stable ID | Candidate consistency issue | Category | Status |
|---|---|---|---|
| [C001](#c001--figure-3-all-patient-rate-column-conflict-with-the-matched-primary-outcome-rate) | Figure 3 all-patient rate-column conflict with the matched primary-outcome rate | Cross-document numeric inconsistency | Pending Human Adjudication |
| [C002](#c002--bedtime-diuretic-six-month-timing-count-triplets-differ-between-efigure-4-and-etable-6) | Bedtime-diuretic six-month timing count triplets differ between eFigure 4 and eTable 6 | Cross-document numeric inconsistency | Pending Human Adjudication |
| [C003](#c003--etable-5-other-ethnicity-row-duplicates-whitecaucasian-values-and-exceeds-randomized-other-totals) | eTable 5 `Other` ethnicity row duplicates White/Caucasian values and exceeds randomized `Other` totals | Numeric or arithmetic inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Figure 3 all-patient rate-column conflict with the matched primary-outcome rate

**Status:** Pending Human Adjudication

**Candidate statement:** Figure 3 prints `71.0` for both all-patient treatment arms under columns labeled `Rate per 100 patient-years`, whereas the matched primary-outcome analysis reports 2.30 and 2.44 per 100 patient-years for the same arm-specific event counts.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_garrison_2025_oi_250019_1749674951.29054.pdf — Figure 3, PDF p. 9](<../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9>); [jama_garrison_2025_oi_250019_1749674951.29054.pdf — Table 2, PDF p. 8](<../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8>); [main article abstract, PDF p. 1](<../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1>); [primary-outcome narrative, PDF p. 6](<../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6>).

**Source evidence:** Figure 3 names the composite primary outcome and prints all-patient events of 163 (bedtime) and 173 (morning), followed by `71.0` and `71.0` beneath `Rate per 100 patient-years`; it also prints HR 0.96 (95% CI 0.77-1.19). Table 2 prints the same endpoint, arm order, event counts, and HR, with rates 2.30 and 2.44 per 100 patient-years. The abstract and narrative give rounded rates 2.3 and 2.4.

**Reported-versus-comparator:** Reported Figure 3 values: 71.0/71.0 under the printed rate header. Matched comparator: Table 2 2.30/2.44 per 100 patient-years, with abstract/narrative rounding to 2.3/2.4.

**Reasoning procedure:** Match the population (all randomized patients), comparison (bedtime versus morning), composite endpoint, arm-specific event counts, effect estimate, and stated rate unit across locations. Compare only at displayed precision and distinguish direct observations from possible production explanations.

**Calculation:** Ordinary rounding reconciles 2.30 with 2.3 and 2.44 with 2.4, but cannot reconcile 71.0 with either rate under the shared printed unit. The exact event counts match: 163 = 163 and 173 = 173. As a diagnostic alternative only, if 71.0 were hundreds of patient-years, `163 / 7100 × 100 = 2.2958` and `173 / 7100 × 100 = 2.4366`, which round to the Table 2 rates; the PDF does not label 71.0 that way.

**Alternative source-grounded interpretations:** The values may represent an unlabeled exposure quantity, the Figure 3 column header may be mislabeled, a figure value may have entered production incorrectly, or the figure may use an unreported denominator. The supplied package does not identify which display is authoritative.

**Mechanical evidence recheck:** The current PDF was directly re-opened and the cited pages were freshly extracted and rendered. The figure header, values, matched events, and comparator rate values were confirmed. Complementary Figure 3 subgroup values also partition to 71.0 (for example, bedtime male + female: 30.5 + 40.5), which supports but does not prove the exposure-scale interpretation.

**Quality-control relevance:** A matched primary result has a printed rate-column mismatch. The record is kept as one candidate despite the related measure/label implication because it concerns the same printed values, comparator, and consistency rule.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy 71.0 as an event rate or reuse the Figure 3 rate-column labeling. This report does not establish that this occurred or changed any conclusion.

**Human verification steps:** Inspect the locked Figure 3 production dataset and specification; identify the intended measure and denominator for every displayed 71.0 field; calculate arm-specific rates from exact person-time; then verify the values and header together.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Bedtime-diuretic six-month timing count triplets differ between eFigure 4 and eTable 6

**Status:** Pending Human Adjudication

**Candidate statement:** eFigure 4 and eTable 6 print different medication-level timing counts for the same six-month bedtime-allocation diuretic total of 424.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [joi250019supp3_prod_1749674951.30054.pdf — eFigure 4, PDF p. 26](<../joi250019supp3_prod_1749674951.30054.pdf#page=26>); [joi250019supp3_prod_1749674951.30054.pdf — eTable 6, PDF p. 42](<../joi250019supp3_prod_1749674951.30054.pdf#page=42>) (table begins on [PDF p. 41](<../joi250019supp3_prod_1749674951.30054.pdf#page=41>)).

**Source evidence:** eFigure 4 identifies PM as the bedtime group and prints diuretic counts 278 as allocated, 138 off allocation, and 8 twice or more daily. eTable 6 reports the same bedtime diuretic total of 424 as 277/424 (65.3%) as allocated, 139/424 (32.8%) off allocation, and 8/424 (1.9%) twice or more daily.

**Reported-versus-comparator:** Reported figure triplet: 278/138/8. Matched table triplet: 277/139/8 of 424, with the stated percentages.

**Reasoning procedure:** Match allocation (bedtime), time point (six months), medicine class (diuretic), three displayed timing categories, and total medication count. Test the triplets and displayed percentages at their printed precision; do not infer an undisclosed coding rule or data freeze.

**Calculation:** Both triplets sum to 424: `278 + 138 + 8 = 424` and `277 + 139 + 8 = 424`. The first two cells differ by one in opposite directions; 8 agrees. The table percentages reproduce its counts: `277/424 × 100 = 65.33%`, `139/424 × 100 = 32.78%`, and `8/424 × 100 = 1.89%`, rounding to 65.3%, 32.8%, and 1.9%. The figure's first two counts instead yield 65.6% and 32.5% at one decimal.

**Alternative source-grounded interpretations:** One medication may have been recoded between as-allocated and off-allocation, the displays may use undisclosed data cuts, or one figure/table value may have changed during production. Both triplets are compatible with the shared total; the source does not select an intended triplet.

**Mechanical evidence recheck:** The current PDF was directly re-opened and the figure and table pages were freshly extracted and rendered. Titles, arm key, category labels, total, triplets, and table percentages were confirmed.

**Quality-control relevance:** The same class-specific six-month relationship has discordant numerators across a figure and table. The total alone does not resolve the category assignment.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy one incorrect class-specific adherence numerator and derive a correspondingly incorrect percentage. This report does not establish propagation or conclusion change.

**Human verification steps:** Compare the locked medication-level extracts, data-freeze dates, and coding rules used for eFigure 4 and eTable 6; identify the discrepant medication record; confirm the intended category; then regenerate or relabel the affected display as authorized by a human reviewer.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 5 `Other` ethnicity row duplicates White/Caucasian values and exceeds randomized `Other` totals

**Status:** Pending Human Adjudication

**Candidate statement:** In eTable 5, the `Other` ethnicity row repeats the White/Caucasian values for participants unable to be followed through administrative data; those repeated counts exceed the randomized baseline `Other` counts for each allocation arm in eTable 3.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi250019supp3_prod_1749674951.30054.pdf — eTable 5, PDF p. 37](<../joi250019supp3_prod_1749674951.30054.pdf#page=37>); [joi250019supp3_prod_1749674951.30054.pdf — eTable 3, PDF p. 29](<../joi250019supp3_prod_1749674951.30054.pdf#page=29>).

**Source evidence:** eTable 5 is headed morning allocation n=44 and bedtime allocation n=57. Its White/Caucasian row prints 40 (90.9%) and 53 (93.0%); its later `Other` row prints exactly the same values. eTable 3 gives randomized baseline `Other` counts of 5/1680 (0.3%) morning and 9/1677 (0.5%) bedtime, while its White counts are 1587/1680 and 1565/1677.

**Reported-versus-comparator:** Reported eTable 5 `Other` row: morning 40 (90.9%) and bedtime 53 (93.0%), identical to White/Caucasian. Matched parent-arm comparator: eTable 3 `Other` counts of 5 morning and 9 bedtime.

**Reasoning procedure:** Compare the directly printed eTable 5 rows with each other and then with the matched allocation-arm baseline category totals. Treat a common `Other` category definition as a necessary condition and state that its data dictionary is not supplied.

**Calculation:** The duplicated eTable 5 counts reproduce its displayed percentages: `40/44 × 100 = 90.91%` and `53/57 × 100 = 92.98%`. Under the displayed common category definition, the subgroup-to-parent comparisons are impossible: `40 > 5` morning and `53 > 9` bedtime. These are printed-count conflicts, not rounding differences.

**Alternative source-grounded interpretations:** Values may have been duplicated from White/Caucasian, a row may be mislabeled or misplaced, or an undisclosed coding difference may exist. The package does not state that `Other` overlaps White/Caucasian and does not provide the data dictionary needed to determine intended replacement cells.

**Mechanical evidence recheck:** The current PDF was directly re-opened and both table pages were freshly extracted and rendered. The eTable 5 cohort denominators, duplicated White/Caucasian and `Other` values, and the eTable 3 parent-arm `Other` totals were confirmed.

**Quality-control relevance:** The record preserves a direct row duplication and a parent-subset count conflict as one candidate. It does not assert a corrected count or an associated corrected P value.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy duplicated subgroup counts or reuse an ethnicity-comparison result based on an incorrect displayed row. This report does not establish that either occurred or altered a conclusion.

**Human verification steps:** Inspect the eTable 5 analysis export and participant-level baseline ethnicity coding for the morning n=44 and bedtime n=57 cohort; confirm whether coding matches eTable 3; recover the intended `Other` cells; and rerun the associated ethnicity comparison if the displayed inputs change.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, a downstream systematic review, meta-analysis, guideline, or data-extraction workflow could copy a rate, class-specific numerator, percentage, category count, or table label from the affected display. This is a general conditional risk statement only: the supplied package does not show downstream reuse, propagation, harm, or a changed paper-level conclusion.

## Limitations and Missing Definitions

The bounded source, production, and model-definition limitations are recorded in [limitations.md](<review_1_5_1/limitations.md>). Missing production datasets, timing-code history, an ethnicity data dictionary, and row-specific test output prevent selection of intended replacement values. DOC-003's embedded-text encoding limitation was addressed with direct rendering. These constraints do not create a scientific-coverage gap because all 86 source pages were directly mapped.

## Human Adjudication Checklist

- Confirm each cited current-PDF location and the matched population, time point, contrast, outcome, unit, and category definition.
- Retrieve the applicable locked production source, data extract, code, or data dictionary before selecting any replacement value or label.
- Determine whether each printed mismatch is a value, label, timing, coding, or layout issue; document any corrected calculations.
- Record the human decision only in each card's five adjudication fields.
- Recheck any affected cross-location display after an authorized correction.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The source inventory, before-run hashes, asset inventory, coverage manifest, relationship maps, checks, recheck, and quality audit are retained under [review_1_5_1](<review_1_5_1/>). Direct-source evidence was authoritative for every candidate recheck. After report assembly, every direct-source hash and all 108 reused-asset hashes were recomputed and matched their before-run ledgers.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| Coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| Reuse asset curation | task:/root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| Main evidence mapping | task:/root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| Support evidence mapping | task:/root/support_protocol_sap_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_protocol_sap.md |
| Support evidence mapping | task:/root/support_results_a_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_results_001_024.md |
| Support evidence mapping | task:/root/support_results_b_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_results_025_049.md |
| Numeric checks | task:/root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| Cross-source checks | task:/root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| Statistical pass 1 | task:/root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| Evidence recheck | task:/root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| Statistical pass 2 | task:/root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| Evidence quality | task:/root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| Report generation | task:/root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | limitations.md |

The authoritative one-agent-per-row record is [agent_execution_manifest.md](<review_1_5_1/agent_execution_manifest.md>).

### Performance

- **Target basis:** Four-PDF package with 86 pages, all 86 requiring fresh direct-source mapping after source-hash fitness checks, plus table-dense results requiring cross-document and two-pass statistical review; bounded against the 102-page/81-fresh-page calibration while accounting for slightly fewer total units but a fully fresh evidence burden.
- **Total source units:** 86
- **Fresh-source units:** 86
- **Target elapsed minutes:** 40-60
- **Started UTC:** 2026-09-03T03:48:59Z
- **Finished UTC:** 2026-09-03T04:56:53Z
- **Observed elapsed minutes:** 67.9
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** All 86 pages required fresh mapping after stale-derivative hash findings; malformed DOC-003 embedded text required rendered-page inspection; table-dense cross-source checks and direct visual evidence rechecks exceeded the upper bound.

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Response count | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Token-only API-equivalent cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |

Authoritative response-level runtime/API token counts were not exposed for this coordinator session or any spawned agent, so each agent is recorded as `UNAVAILABLE` with exact `__` token fields in the ledger; no text-length estimate was substituted. The zero values above are known recorded subtotals, not a claim of zero actual use. Per-agent detail is in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>). Cached input and cache-write counts are input subsets; reasoning is an output subset; none is added again to total tokens. Amounts are token-only API-equivalent estimates under the dated price snapshot, not an invoice.
