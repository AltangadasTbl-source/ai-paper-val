# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a determination that the paper is invalid or that a correction is required. Small preventable reporting defects can matter for downstream evidence extraction; this report does not claim that any defect propagated, changed a conclusion, or caused serious harm.

## Executive Quality-Control Summary

Complete source coverage identified six stable candidate consistency issues: C001-C006. They concern a matched absolute-difference value, a protocol/article cutoff, two fraction-percentage mismatches, a matched P-value display, and a protocol-duration decomposition. All are retained for human adjudication without ranking or suppression. No candidate was created from a coherent display-zero P value; none of the six cards mentions such a value.

## Package and Reused-Evidence Provenance

The supplied package contains four direct PDF sources: [jama_thille_2019_oi_190108.pdf — PDF p. 1](<../jama_thille_2019_oi_190108.pdf#page=1>), [joi190108supp1_prod.pdf — PDF p. 1](<../joi190108supp1_prod.pdf#page=1>), [joi190108supp2_prod.pdf — PDF p. 1](<../joi190108supp2_prod.pdf#page=1>), and [joi190108supp3_prod.pdf — PDF p. 1](<../joi190108supp3_prod.pdf#page=1>). Reused native text, OCR, rendered pages, manifests, and source-location maps were used only as locators and transcription aids; direct supplied PDF pages were the authority for candidate evidence.

| Source ID | Source | Units | Reused / fresh-required | SHA-256 |
|---|---|---:|---:|---|
| DOC-001 | jama_thille_2019_oi_190108.pdf | 11 | 9 / 2 | `4909b853613eab3c15f1a76acffeb0f70a1578e52f2bf288757bb39d68f22183` |
| DOC-002 | joi190108supp1_prod.pdf | 48 | 0 / 48 | `06dcc6653df3b6e37f246ed461d2a5f4b4afbbf9f0399ef682e2d1f0b22c969c` |
| DOC-003 | joi190108supp2_prod.pdf | 9 | 9 / 0 | `196ab20ad83da77d6dc53c3462f7a2ec201ec5ee927c94a30c87f725b6ff789b` |
| DOC-004 | joi190108supp3_prod.pdf | 1 | 0 / 1 | `30c05cacae13b3124acb648bdc8168f4df612f8b1c5369ebf4c571dd17e52702` |

The reusable-asset inventory records 59 hashed pre-existing evidence assets. Source and reused-asset integrity are recorded in [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>) and [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>).

## Scope, Complete Coverage, and Exclusions

The review covered supplied-package numeric, denominator/proportion/total, inferential-statistical, cross-document, measure/label/scale, and rate-versus-count consistency. It did not undertake a broad methodology, clinical, novelty, misconduct, or raw-data audit.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 9 | 2 | 11 | COMPLETE |
| DOC-002 | 48 | 0 | 48 | 48 | COMPLETE |
| DOC-003 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | 1 | 0 | 1 | 1 | COMPLETE |
| **Package** | **69** | **18** | **51** | **69** | **COMPLETE** |

Reusable and fresh-required units partition every source row, and mapped units equal total units. There was no review queue, top-N subset, deferred-by-cap section, or candidate count cap.

## Quantitative and Statistical Relationship Coverage

The relationship inventories contain 59 numeric/reporting relationships (N001-N059) and 39 inferential-statistical relationships (S001-S039). All 59 numeric relationships received an explicit check. Statistical pass 1 and the distinct statistical pass 2 each completed all 39 S relationships; pass 2 appended no statistical candidate. C006 was later registered from N027 and has no S relationship.

Both statistical passes were fresh, distinct `gpt-5.6-terra` high-effort executions. They separated direct observations from diagnostic calculations and did not infer missing test, model, or display conventions. Neither pass found a literal `P = 0`, `p = 0.000`, or equivalent display-zero P value.

## Candidate Index

| ID | Candidate | Category |
|---|---|---|
| C001 | Day-7 respiratory-failure absolute difference differs across matched article locations | Numeric or arithmetic inconsistency |
| C002 | Reintubation respiratory-acidosis cutoff differs between article and protocol | Measure, label, or scale inconsistency |
| C003 | Hypercapnic ineffective-cough percentages conflict with printed fractions | Denominator, proportion, or total inconsistency |
| C004 | Hypercapnic abundant-secretion percentages conflict with printed fractions | Denominator, proportion, or total inconsistency |
| C005 | Matched nonhypercapnic day-7 reintubation P values differ across article and supplement | Cross-document numeric inconsistency |
| C006 | Protocol total-duration breakdown does not arithmetically reach the printed total | Numeric or arithmetic inconsistency |

## Candidate Evidence Cards

## C001 — Day-7 respiratory-failure absolute difference differs across matched article locations

- **Status:** Pending Human Adjudication
- **Candidate statement:** The abstract and Results narrative print a day-7 respiratory-failure absolute difference of -8.7 percentage points, while Table 2 prints -8.5 for the otherwise matched result.
**Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** [jama_thille_2019_oi_190108.pdf — PDF p. 1](<../jama_thille_2019_oi_190108.pdf#page=1>), abstract Results; [jama_thille_2019_oi_190108.pdf — PDF p. 6](<../jama_thille_2019_oi_190108.pdf#page=6>), Secondary Outcomes; [jama_thille_2019_oi_190108.pdf — PDF p. 8](<../jama_thille_2019_oi_190108.pdf#page=8>), Table 2.
- **Source evidence:** Pages 1 and 6 print 21% versus 29%, difference -8.7% (95% CI -15.2% to -1.8%; P=.01). Page 8 prints 88/302 versus 70/339, difference -8.5% with the same interval and P value.
- **Reported-versus-comparator:** Reported prose value -8.7 percentage points versus Table 2 and displayed-count value -8.5 percentage points.
- **Reasoning procedure:** Match population, endpoint, day, treatment direction, interval, and P value; compare point estimates and reproduce the difference from displayed counts.
- **Calculation:** `(70 / 339 - 88 / 302) x 100 = -8.490105296`, which rounds to -8.5 percentage points at one decimal; the printed estimates differ by 0.2 points.
- **Alternative source-grounded interpretations:** The prose may reflect an unprinted analysis output or editing stage; Table 2 may reflect displayed counts. No cited location labels a distinct population, endpoint, model, or denominator for -8.7.
- **Mechanical evidence recheck:** All three locations were directly inspected; both values, shared interval/P value, and count-derived calculation were reproduced. The unavailable input is the analysis output or rule behind -8.7.
- **Quality-control relevance:** This supports a bounded request to reconcile one matched point estimate; it does not establish the intended value or a paper-level conclusion change.
- **Potential downstream evidence impact:** If confirmed, a data extractor or meta-analytic reviewer could copy either -8.7 or -8.5 for the same result. The package does not establish propagation or conclusion change.
- **Human verification steps:** Compare analysis output and edit history, identify the intended denominator/calculation, then reconcile the abstract, narrative, and table.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Reintubation respiratory-acidosis cutoff differs between article and protocol

- **Status:** Pending Human Adjudication
- **Candidate statement:** The article and supplied protocol print different pH cutoffs for the respiratory-acidosis component of the reintubation respiratory-failure criterion.
**Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [jama_thille_2019_oi_190108.pdf — PDF p. 4](<../jama_thille_2019_oi_190108.pdf#page=4>), Outcomes; [joi190108supp1_prod.pdf — PDF p. 30](<../joi190108supp1_prod.pdf#page=30>) and [joi190108supp1_prod.pdf — PDF p. 31](<../joi190108supp1_prod.pdf#page=31>), protocol section 5.4 continuation.
- **Source evidence:** The article prints pH below 7.25 with PaCO2 above 45 mm Hg. Protocol section 5.4 prints pH below 7.35 with PaCO2 above 45 mm Hg for the same reintubation-rule component.
- **Reported-versus-comparator:** Article cutoff `<7.25` versus protocol cutoff `<7.35`, with the same PaCO2 condition and criterion role.
- **Reasoning procedure:** Match decision context, at-least-two-criteria structure, physiological component, unit, and PaCO2 threshold, then compare pH thresholds.
- **Calculation:** `7.35 - 7.25 = 0.10` pH units.
- **Alternative source-grounded interpretations:** The article may reflect a later approved amendment or implementation-specific refinement. The package has protocol version 4 but no amendment history, final case-report definition, or operational adjudication rule.
- **Mechanical evidence recheck:** The article location and protocol continuation were directly inspected; criterion role and threshold pairs matched. Missing inputs are final amendment history and operative ascertainment definition.
- **Quality-control relevance:** This supports a bounded question about the printed threshold governing ascertainment; it does not show a changed participant classification or event count.
- **Potential downstream evidence impact:** If confirmed, a protocol reviewer or outcome-definition extractor could record different reintubation criteria. The package does not demonstrate altered results or propagation.
- **Human verification steps:** Retrieve final protocol amendments and operative case-report/adjudication instructions, determine the effective threshold and date, then reconcile the descriptions.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Hypercapnic ineffective-cough percentages conflict with printed fractions

- **Status:** Pending Human Adjudication
- **Candidate statement:** In the hypercapnic eTable 2 ineffective-cough row, each printed percentage conflicts with its adjacent printed numerator and denominator.
**Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [joi190108supp2_prod.pdf — PDF p. 4](<../joi190108supp2_prod.pdf#page=4>), eTable 2; [jama_thille_2019_oi_190108.pdf — PDF p. 6](<../jama_thille_2019_oi_190108.pdf#page=6>), Table 1 aggregate row.
- **Source evidence:** eTable 2 prints `14/45 (69)` and `16/59 (73)` under `Ineffective cough, No./total No. (%)`; its nonhypercapnic values are `51/239 (21)` and `70/263 (27)`. Table 1 prints `65/284 (23)` and `86/322 (27)`.
- **Reported-versus-comparator:** Printed 69% versus 14/45 = 31.1%; printed 73% versus 16/59 = 27.1%.
- **Reasoning procedure:** Apply the row's numerator/denominator/percentage identity, then test complementary proportions and stratum-to-aggregate sums.
- **Calculation:** `14/45 x 100 = 31.1111%`; `16/59 x 100 = 27.1186%`. Complements `31/45 = 68.8889%` and `43/59 = 72.8814%` reproduce 69% and 73%. Strata reconcile: `51+14=65`, `239+45=284`, `70+16=86`, and `263+59=322`.
- **Alternative source-grounded interpretations:** Percentages may describe effective rather than ineffective cough, or the numerators, percentages, or row label may contain a transcription/coding mismatch; the source does not name an inverse measure.
- **Mechanical evidence recheck:** The row and aggregate comparator were directly inspected. Both conflicts, complements, and aggregate identities were reproduced; intended cough-status coding is unavailable.
- **Quality-control relevance:** This supports reconciliation of two baseline-characteristic cells and their label; it does not establish an outcome-analysis defect or conclusion change.
- **Potential downstream evidence impact:** If confirmed, a baseline-characteristic extractor could copy 69% or 73% as ineffective-cough prevalence despite adjacent fractions. The package does not show that this occurred.
- **Human verification steps:** Check the data dictionary and table-production code, determine whether numerator, percentage, or label expresses the intended category, then reconcile cells and aggregate representation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Hypercapnic abundant-secretion percentages conflict with printed fractions

- **Status:** Pending Human Adjudication
- **Candidate statement:** In the hypercapnic eTable 2 abundant-secretions row, each printed percentage conflicts with its adjacent printed numerator and denominator.
**Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [joi190108supp2_prod.pdf — PDF p. 4](<../joi190108supp2_prod.pdf#page=4>), eTable 2; [jama_thille_2019_oi_190108.pdf — PDF p. 6](<../jama_thille_2019_oi_190108.pdf#page=6>), Table 1 aggregate row.
- **Source evidence:** eTable 2 prints `20/46 (57)` and `23/61 (62)` under `Abundant secretions, No./total No. (%)`; its nonhypercapnic values are `101/242 (42)` and `91/265 (34)`. Table 1 prints `121/288 (42)` and `114/326 (35)`.
- **Reported-versus-comparator:** Printed 57% versus 20/46 = 43.5%; printed 62% versus 23/61 = 37.7%.
- **Reasoning procedure:** Apply the row's numerator/denominator/percentage identity, then check complementary proportions and stratum-to-aggregate sums.
- **Calculation:** `20/46 x 100 = 43.4783%` (43% at whole-percent precision) and `23/61 x 100 = 37.7049%` (38%). Complements `26/46 = 56.5217%` and `38/61 = 62.2951%` reproduce 57% and 62%. Strata reconcile: `101+20=121`, `242+46=288`, `91+23=114`, and `265+61=326`.
- **Alternative source-grounded interpretations:** Percentages may describe absence rather than presence of abundant secretions, or numerator, percentage, or label may contain a transcription/coding mismatch; no inverse measure is labelled.
- **Mechanical evidence recheck:** The row and aggregate comparator were directly inspected. Both conflicts, complements, and aggregate identities were reproduced; intended secretion-status coding is unavailable.
- **Quality-control relevance:** This supports reconciliation of two baseline-characteristic cells and their label; it does not establish an outcome-analysis defect or conclusion change.
- **Potential downstream evidence impact:** If confirmed, a baseline-characteristic extractor could copy 57% or 62% as abundant-secretions prevalence despite adjacent fractions. The package does not show that this occurred.
- **Human verification steps:** Check the data dictionary and table-production code, determine whether numerator, percentage, or label expresses the intended category, then reconcile cells and aggregate representation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Matched nonhypercapnic day-7 reintubation P values differ across article and supplement

- **Status:** Pending Human Adjudication
- **Candidate statement:** The article and eTable 4 print different P values for a matched nonhypercapnic day-7 reintubation result.
**Category:** Cross-document numeric inconsistency
- **Exact source locations:** [jama_thille_2019_oi_190108.pdf — PDF p. 7](<../jama_thille_2019_oi_190108.pdf#page=7>), subgroup Results; [joi190108supp2_prod.pdf — PDF p. 7](<../joi190108supp2_prod.pdf#page=7>), eTable 4.
- **Source evidence:** The article prints 13% versus 18%, difference -5.0% (95% CI -11.2% to 1.1%), P=.10. eTable 4 prints 35/276 versus 45/254, the same difference and interval, and P=.1057.
- **Reported-versus-comparator:** Main-text P=.10 versus supplement P=.1057 for matching population, endpoint, counts-derived percentages, contrast, difference, and interval.
- **Reasoning procedure:** Match all result descriptors and effect components before comparing P values. Count-based reconstruction is diagnostic because the exact subgroup test and display rule are not fully supplied.
- **Calculation:** `45/254 x 100 = 17.7165%`; `35/276 x 100 = 12.6812%`; intervention-minus-control difference is -5.0354 points, reproducing -5.0. At ordinary two-decimal rounding, .1057 becomes .11, not .10.
- **Alternative source-grounded interpretations:** Different test variants, separately generated outputs, or an unstated truncation/display convention may explain the values; the package does not identify which applies.
- **Mechanical evidence recheck:** Both pages were directly inspected and matched descriptors, P values, and count-derived effect were reproduced. Missing inputs are subgroup-test setting, correction choice, analysis output, and editorial display rule.
- **Quality-control relevance:** This supports a bounded request to reconcile or explain two printed P values. Both are above .05; the package does not establish a different scientific conclusion.
- **Potential downstream evidence impact:** If confirmed, an extractor could copy either `.10` or `.1057` for the same result. No propagation, pooled-estimate effect, guideline effect, or conclusion change is established.
- **Human verification steps:** Compare subgroup-analysis output and table/narrative formatting rules, identify the test and precision convention at each location, then reconcile or explicitly distinguish displays.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Protocol total-duration breakdown does not arithmetically reach the printed total

- **Status:** Pending Human Adjudication
- **Candidate statement:** Protocol section 5.6 prints a total duration of 51 months but names only 36 study months plus 12 analysis months in the same breakdown sentence.
**Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** [joi190108supp1_prod.pdf — PDF p. 11](<../joi190108supp1_prod.pdf#page=11>), synopsis study duration; [joi190108supp1_prod.pdf — PDF p. 32](<../joi190108supp1_prod.pdf#page=32>), section 5.6.
- **Source evidence:** Page 11 prints 36 months of inclusion, 3 months of participation for each patient, and 51 months total comprising 39 study months plus 12 analysis months. Page 32 prints 3 months' participation, 36 months' recruitment, then 51 months total with 36 months for study and 12 months for analysis.
- **Reported-versus-comparator:** Page-32 named breakdown `36 + 12 = 48` months versus its printed 51-month total; page 11 reconciles `39 + 12 = 51`, with `36 + 3 = 39` context.
- **Reasoning procedure:** Treat explicitly named total-duration components as additive, reproduce both decompositions, and retain adjacent participation time as a possible explanation rather than silently adding an omitted component.
- **Calculation:** Page 11: `36 + 3 = 39`; `39 + 12 = 51`. Page 32: `36 + 12 = 48`, three months below 51. Adding separately stated participation gives `36 + 3 + 12 = 51`, but the total sentence does not state that relationship.
- **Alternative source-grounded interpretations:** Page 32's “36 months for the study” may be shorthand for recruitment plus final-participant follow-up. Page 11 supports the intended schedule, but page 32's literal two-part arithmetic remains incomplete.
- **Mechanical evidence recheck:** Both pages were directly inspected. Durations, decompositions, three-month difference, and final-participant-follow-up interpretation were reproduced. Whether analysis overlaps follow-up is not specified.
- **Quality-control relevance:** This supports a bounded request to clarify one protocol timeline sentence; it does not establish an inconsistency in outcomes, effect estimates, or conclusions.
- **Potential downstream evidence impact:** If confirmed, a protocol timeline extractor could record 48 or 51 months or misunderstand the recruitment/follow-up boundary. The package does not show propagation or altered trial results.
- **Human verification steps:** Confirm the intended timeline and whether final-participant follow-up follows recruitment; then state 39 study months plus 12 analysis months or an explicit 36 + 3 + 12 decomposition.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If any candidate is confirmed, an evidence extractor could copy a mismatched point estimate, outcome definition, baseline percentage, P value, or protocol duration. Such information can be reused in systematic reviews, meta-analyses, guidelines, or later evidence products. This is a bounded possibility only: the supplied package does not establish propagation, changed pooled estimates, changed recommendations, conclusion change, or harm.

## Limitations and Missing Definitions

- No raw participant data, analysis code, structured result dataset, workbook, CSV, or underlying statistical output is supplied; DOC-004 states that data are unavailable.
- Protocol version 4 is supplied without amendment history, final operative case-report definition, or event-adjudication manual.
- Exact confidence-interval construction, variance estimators, test choices, degrees of freedom, multiplicity procedures, and some subgroup display conventions are incomplete; diagnostic calculations do not replace reported analyses.
- The analysis output behind -8.7, intended coding for the two eTable 2 rows, and complete duration timing definitions are unavailable.
- DOC-002 PDF p. 42 has a heading-only native text layer but was mapped by direct visual inspection; this is not a scientific-coverage gap.
- Survival curves were not digitized because exact plotted probabilities were not printed.

## Human Adjudication Checklist

For each C ID, verify the cited source pages, inspect the named analysis output or protocol/table-production record where needed, identify the intended displayed value or definition, record the determination in the five blank fields on that card, and reconcile source locations only after human review. Every card remains Pending Human Adjudication unless and until that review is documented.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Canonical review artifacts are under [review_1_5_1](<review_1_5_1/>), including the source inventory, evidence-asset inventory, coverage manifest, relationship inventories, stable ledger, mechanical evidence recheck, evidence-quality audit, and limitations. Direct-source hashes and 59 reused-artifact hashes were recorded before review; the final integrity comparison is reserved for coordinator completion.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curation | /root/reuse_asset_curation | gpt-5.6-terra | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapping | /root/main_quantitative_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapping | /root/support_quantitative_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_review | /root/numeric_consistency_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_review | /root/cross_source_consistency_review | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | /root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | /root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | /root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality_audit | /root/evidence_quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generation | /root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | ../final_report_1_5_1.md |

### Reproducibility performance

<!-- Coordinator finalizes fields below immediately after Markdown assembly. -->

- **Target basis:** Four supplied PDFs with 69 total PDF pages; 51 pages appear to require fresh native-text mapping, while 18 result-relevant pages have reusable page-linked extraction. The protocol is long but natively extractable, the package has no Office/workbook sources, and the expected cross-document relationship volume is moderate. Final counts will be reconciled to the curator inventory before completion.
- **Total source units:** 69
- **Fresh-source units:** 51
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-18T23:16:46Z
- **Finished UTC:** 2026-08-19T00:04:17Z
- **Observed elapsed minutes:** 47.5
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete mapping of the 48-page protocol; six-candidate direct evidence recheck and quality-audit cycle; quality repair and recheck of appended C006; complete six-card report assembly

### Token accounting and cost

Authoritative response-level token counts were not exposed by this runtime for the coordinator or any specialist response. The ledger therefore records one `UNAVAILABLE` row per manifested agent and does not estimate token counts from text.

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Token-only API-equivalent cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |

The compact model rows reproduce [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>), which retains per-agent detail and the explicit unavailable-record counts. The displayed zeros are known recorded subtotals, not estimates of unavailable usage. Cached input and cache-write values are input subsets, and reasoning values are output subsets, so none is added again to total tokens. Any dollar figure is a token-only API-equivalent estimate under the pricing snapshot dated 2026-08-18T00:00:00Z, not an invoice.
