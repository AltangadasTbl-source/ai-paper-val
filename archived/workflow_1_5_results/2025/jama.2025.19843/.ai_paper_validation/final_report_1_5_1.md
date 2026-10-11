# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

This report records source-grounded quantitative reporting consistency observations for human review. It does not determine validity, importance, correction, or any paper-level conclusion. Every candidate below is **Pending Human Adjudication**.

## Executive Quality-Control Summary

Complete source coverage and two corrected independent statistical passes identified **1** stable quantitative reporting quality-control candidate: `C001`. The observation concerns differing printed P values for a matched day-60 mortality result. The available package does not establish whether the values were intentionally produced by distinct analyses or whether either display requires correction. No severity rating, AI disposition, or conclusion-impact judgment is made.

Small preventable reporting defects can matter to downstream evidence extraction. That is a bounded quality-control consideration only: this review does not assert that any defect propagated, changed a conclusion, or caused harm.

## Package and Reused-Evidence Provenance

The package contains six supplied direct-source PDFs (`DOC-001` through `DOC-006`) and no supplied Office workbook, word-processing, or CSV source. Direct PDFs were the evidentiary authority. Existing native text, rendered pages, document records, and evidence maps were used only as source-linked locators or transcription aids; direct-source confirmation controlled candidate evidence.

The reusable-asset inventory identified 58 eligible pre-existing assets: 28 native-text files, 20 rendered-page files, 7 document records, 2 evidence maps, and 1 preprocessing record. Reusable page coverage was limited to all 10 pages of `DOC-001` and all 18 pages of `DOC-004`; the remaining 166 PDF pages were mapped through fresh direct-source extraction. Baseline source hashes are recorded in [source_hashes_before.sha256](review_1_5_1/source_hashes_before.sha256), and baseline reused-asset hashes are recorded in [reused_artifact_hashes_before.sha256](review_1_5_1/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

The review covered every stable PDF-page unit in every supplied direct source. It prioritized numeric, denominator/proportion/total, inferential-statistical, cross-document numeric, measure/label/scale, and rate-versus-count consistency. Analysis-unit or population matters were considered only when they could create a concrete reporting inconsistency.

| Source ID | Direct source | Units | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | [jama_combes_2025_oi_250087_1766516490.94011.pdf — PDF p. 1](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1) | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | [joi250087supp1_prod_1766516490.96011.pdf — PDF p. 1](../joi250087supp1_prod_1766516490.96011.pdf#page=1) | 153 | 0 | 153 | 153 | COMPLETE |
| DOC-003 | [joi250087supp2_prod_1766516490.96511.pdf — PDF p. 1](../joi250087supp2_prod_1766516490.96511.pdf#page=1) | 9 | 0 | 9 | 9 | COMPLETE |
| DOC-004 | [joi250087supp3_prod_1766516490.97011.pdf — PDF p. 1](../joi250087supp3_prod_1766516490.97011.pdf#page=1) | 18 | 18 | 0 | 18 | COMPLETE |
| DOC-005 | [joi250087supp4_prod_1766516490.97511.pdf — PDF p. 1](../joi250087supp4_prod_1766516490.97511.pdf#page=1) | 3 | 0 | 3 | 3 | COMPLETE |
| DOC-006 | [joi250087supp5_prod_1766516490.97511.pdf — PDF p. 1](../joi250087supp5_prod_1766516490.97511.pdf#page=1) | 1 | 0 | 1 | 1 | COMPLETE |
| **Total** | — | **194** | **28** | **166** | **194** | **COMPLETE** |

Excluded from this bounded review were broad methodology, clinical-care, novelty, misconduct, and raw-data audits. A coherent finite-precision display-zero P value alone was not eligible for a candidate. No such display-zero issue generated a stable ID in this review.

## Quantitative and Statistical Relationship Coverage

The complete numeric inventory contains `N001` through `N052` (52/52), and the numeric checker records an explicit no-candidate outcome for each. Checks included displayed arithmetic, totals, denominators, percentages, available-case populations, units, labels, and repeated source occurrences.

The complete inferential-statistical inventory contains `S001` through `S024` (24/24). Corrected independent statistical pass 1 and pass 2 each record explicit completion for every canonical statistical relationship. The corrected records preserve `S021` as the day-30/day-60 mortality-figure relationship, `S022` as the MACE-figure relationship, `S023` as the RMST display relationship, and `S024` as the supplementary subgroup source occurrence. `C001` is revisited through `S008` and `S021`; no second candidate was created.

| Review lane | Complete scope | Result |
|---|---|---|
| Numeric consistency | N001-N052 (52/52) | Complete; C001 context retained without a duplicate candidate |
| Statistical pass 1, corrected | S001-S024 (24/24) | Complete; C001 implication retained |
| Cross-source consistency, corrected | N001-N052 and S001-S024 | Complete; C001 retained |
| Mechanical evidence recheck | C001 (1/1) | Complete |
| Statistical pass 2, corrected | S001-S024 and C001 | Complete; no new candidate |
| Final evidence-quality audit | C001; coverage; execution | PASS_READY |

Durable coverage details are available in [coverage_manifest.md](review_1_5_1/coverage_manifest.md), [numeric relationship inventory](review_1_5_1/relationships/numeric_relationship_inventory.md), [statistical relationship inventory](review_1_5_1/statistics/relationship_inventory.md), [corrected statistical pass 1](review_1_5_1/checkers/statistical_pass_1_repair.md), and [corrected statistical pass 2](review_1_5_1/checkers/statistical_pass_2_repair.md).

## Candidate Index

| Stable ID | Candidate | Category | Status |
|---|---|---|---|
| [C001](#c001--conflicting-printed-p-values-for-matched-day-60-mortality-result) | Conflicting printed P values for matched day-60 mortality result | Cross-document numeric inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Conflicting printed P values for matched day-60 mortality result

**Candidate statement:** The supplied main article prints `P = .78` for the matched day-60 mortality comparison, while the directly referenced supplementary eFigure 2 prints `p = 0.56, Log-rank` for the same day-60 endpoint, randomized groups, and terminal cumulative deaths. The package does not identify the analysis that produced `.78`, so whether these displays are intentionally distinct or constitute a reporting mismatch requires human adjudication.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 — PDF p. 1](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=1) (abstract); [DOC-001 — PDF p. 3](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=3) (statistical methods); [DOC-001 — PDF p. 4](../jama_combes_2025_oi_250087_1766516490.94011.pdf#page=4) (Results and eFigure 2 cross-reference); [DOC-003 — PDF p. 7](../joi250087supp2_prod_1766516490.96511.pdf#page=7) (planned mortality analysis); and [DOC-004 — PDF p. 11](../joi250087supp3_prod_1766516490.97011.pdf#page=11) (Supplement 3 eFigure 2).

**Source evidence:** DOC-001 reports day-60 mortality as 28/101 (27.7%) in the levosimendan group and 26/104 (25.0%) in the placebo group, with a 2.7 percentage-point risk difference (95% CI, -9.0 to 15.3), RR 1.11 (95% CI, 0.70-1.75), and `P = .78`. The Results expressly directs the reader to eFigure 2. DOC-004 eFigure 2 displays the same day-60 terminal cumulative deaths, 28 and 26, and labels its P value `p = 0.56, Log-rank`.

**Reported-versus-comparator:** Reported prose P value: `.78` for the day-60 mortality result in DOC-001. Comparator: `.56`, expressly labelled `Log-rank`, for the matched day-60 mortality panel in DOC-004 eFigure 2. The matched counts, endpoint, time point, group labels, and treatment contrast align.

**Reasoning procedure:** Compare only the supplied matched result locations and their printed analysis labels. A P value can differ when it arises from a distinct defined analysis; therefore this card does not assume that the prose value is log-rank. If the two values are intended as the same day-60 mortality inferential result, they should not differ by ordinary display rounding.

**Calculation:** `28 / 101 = 0.2772`, rounding to 27.7%; `26 / 104 = 0.2500`, or 25.0%; and `27.72% - 25.00% = 2.72` percentage points, rounding to the printed 2.7. Thus the counts, denominators, percentages, and risk difference reconcile. The printed P-value difference is `.78 - .56 = .22`, which cannot be two rounded displays of one underlying P value. No P value was reconstructed from the RR confidence interval because a binary RR interval and a time-to-event log-rank test need not represent the same analysis.

**Alternative source-grounded interpretations:** DOC-001 describes categorical-outcome testing with chi-square or Fisher exact tests and censored outcome testing with log-rank tests, while DOC-004 expressly labels `.56` as log-rank. Thus `.78` could represent an unnamed fixed-time categorical or another distinct analysis, rather than the figure's log-rank result. This is an inferred reconciliation possibility, not a definition printed with `.78`.

**Mechanical evidence recheck:** All cited locations and printed values were directly rechecked. The supplied package identifies the endpoint, time point, groups, denominators, counts, proportions, risk difference, RR, prose P value, figure P value, figure test label, and planned mortality/log-rank method. It does not identify the prose `.78` test/model, estimand, adjustment, analysis population, censoring rule, or complete event/risk-set data. Direct observation is separated from the possible distinct-analysis explanation in [evidence_recheck.md](review_1_5_1/verification/evidence_recheck.md).

**Quality-control relevance:** The same endpoint, time point, randomized groups, counts, and direct supplement reference have two different printed P values without a supplied definition that reconciles them. This is a candidate consistency issue for human review, not a determination that either value is incorrect.

**Potential downstream evidence impact:** If human adjudication confirms a reporting mismatch, a systematic reviewer, meta-analyst, guideline developer, or data extractor could copy a different P value depending on whether the main prose or supplementary figure is used. This is a bounded possibility; this review does not claim that such propagation, conclusion change, or harm occurred.

**Human verification steps:** Identify the exact test/model, estimand, analysis population, adjustment, and time-to-event/censoring rule that generated `.78`; compare it with the labelled eFigure 2 log-rank analysis and the planned mortality analysis; then determine whether the two displays intentionally represent distinct analyses or whether one requires correction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Quantitative reporting consistency matters because source values may later be transcribed into evidence tables, systematic reviews, meta-analyses, guidelines, or other evidence products. For C001, the bounded concern is selection of different printed P values from two supplied locations if a human reviewer confirms they should represent the same analysis. This report makes no claim that any downstream reuse occurred or that the study conclusion changes.

## Limitations and Missing Definitions

- The package does not identify the test/model, estimand, adjustment, analysis population, or censoring rule behind prose `P=.78` for day-60 mortality.
- Individual death times, censoring times, and complete risk-set information needed to independently reproduce the eFigure 2 log-rank result are not supplied.
- Some model-derived intervals and curve coordinates cannot be independently regenerated from aggregate displays; checks were limited to supported arithmetic, ordering, direction, labels, precision, and matched-location comparisons.
- No reusable page-level extraction existed for DOC-002, DOC-003, DOC-005, or DOC-006. This was an evidence-asset limitation, not a scientific-coverage gap, because every page was freshly mapped.

These limitations preserve the exact human question for C001 and do not leave a direct source unit or canonical numeric/statistical relationship unmapped. See [limitations.md](review_1_5_1/limitations.md).

## Human Adjudication Checklist

- Confirm that each cited PDF page and printed value has been reviewed against the supplied direct source.
- For C001, establish the exact analytical provenance of prose `.78`, including test/model, estimand, population, adjustment, and time-to-event/censoring handling.
- Compare that provenance with eFigure 2's labelled log-rank analysis and the prespecified mortality analysis.
- Decide whether the two P values intentionally represent distinct analyses or whether a correction is warranted.
- Complete the five blank human-adjudication fields in the candidate card. No AI validity, importance, or action determination is supplied here.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source Integrity

Six direct-source PDFs and 58 reused evidence assets were SHA-256 hashed before review. The final evidence-quality audit recorded that all six direct-source hashes and all 58 reused-asset hashes matched their baseline records, with no source or reused asset changed. Source identity, page counts, and classification are recorded in [source_inventory.md](review_1_5_1/source_inventory.md); reused-asset fitness and coverage are recorded in [evidence_asset_inventory.md](review_1_5_1/evidence_asset_inventory.md).

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| statistics_pass_1_repair | root/statistics_pass_1_repair | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1_repair.md |
| cross_source_repair | root/cross_source_repair | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency_repair.md |
| statistics_pass_2_repair | root/statistics_pass_2_repair | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2_repair.md |
| quality_control_auditor_final | root/quality_auditor_final | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit_final.md |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_record.md |

The execution manifest is retained in [agent_execution_manifest.md](review_1_5_1/agent_execution_manifest.md). The two required original statistical passes were distinct fresh `gpt-5.6-terra` high-effort agents; corrective passes were also separately recorded.

### Reproducibility Performance

- **Target basis:** Six supplied PDFs contain 194 pages, including one 153-page protocol/SAP-scale supplement, several table- and figure-bearing result supplements, and a 10-page main article. Existing page-level native text is visibly available for 28 pages and document-map assets may reduce fresh extraction, but the remaining page burden and expected cross-document/statistical relationship volume make this materially larger than the 102-page calibration package.
- **Total source units:** 194
- **Fresh-source units:** 166
- **Target elapsed minutes:** 70-105
- **Started UTC:** 2026-09-03T03:45:59Z
- **Finished UTC:** 2026-09-03T04:58:46Z
- **Observed elapsed minutes:** 72.8
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token Accounting and Cost

The accounting window runs from `Started UTC` through `Finished UTC` and includes the coordinator and every manifested specialist response. Counts must be authoritative runtime/API usage only; cached input and cache-write tokens are input subsets, and reasoning tokens are an output subset, not additional total tokens. Amounts are token-only API-equivalent estimates under the dated pricing snapshot, not invoices.

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Responses | Total tokens | Known token cost (USD) | Complete cost status |
|---|---:|---:|---:|---|
| gpt-5.6-sol | 4 unavailable agent records | 0 known | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 11 unavailable agent records | 0 known | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

Per-agent details and the deterministic rollups are retained in `review_1_5_1/token_usage_ledger.csv` and `review_1_5_1/token_usage_summary.md` after coordinator finalization.
