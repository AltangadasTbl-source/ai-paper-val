# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

All observations in this report are **Pending Human Adjudication**. They are quality-control candidates, not determinations of validity, importance, correction, or paper-level conclusion impact.

## Executive Quality-Control Summary

Complete review of the supplied package identified **2** distinct quantitative reporting quality-control candidates: C001 and C002. C001 is a repeated-reporting mismatch in confidence-interval endpoints for a matched any-stroke rate ratio. C002 is a reproducible event-count comparison whose relevance remains conditional on an unspecified subtype-overlap and unit-of-count rule. No candidate was created solely from a display-zero P value, and no candidate set was capped, ranked, deferred, or restricted to a review queue.

Small preventable reporting defects can matter when quantitative results are copied into downstream evidence extraction. This report does not assert that any propagation, clinical harm, meta-analytic change, or change in the paper’s conclusion has occurred.

## Package and Reused-Evidence Provenance

The supplied package contains four direct PDF sources and no DOC, DOCX, XLS, XLSX, or CSV source. Direct-source PDFs were authoritative. Pre-existing normalized text, OCR, rendered pages, document records, and extraction maps were used only as source-linked locators and transcription aids; they were not scientific authority or a discovery boundary.

| Source ID | Direct source | Stable PDF pages | Reusable page-level units | Fresh-required units |
|---|---|---:|---:|---:|
| DOC-001 | [jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf — PDF p. 1](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1>) | 9 | 8 | 1 |
| DOC-002 | [joi250068supp1_prod_1760999665.28862.pdf — PDF p. 1](<../joi250068supp1_prod_1760999665.28862.pdf#page=1>) | 26 | 0 | 26 |
| DOC-003 | [joi250068supp2_prod_1760999665.29862.pdf — PDF p. 1](<../joi250068supp2_prod_1760999665.29862.pdf#page=1>) | 24 | 0 | 24 |
| DOC-004 | [joi250068supp3_prod_1760999665.30362.pdf — PDF p. 1](<../joi250068supp3_prod_1760999665.30362.pdf#page=1>) | 11 | 9 | 2 |
| **Package** | **Four supplied PDFs** | **70** | **17** | **53** |

The reused-evidence inventory records 51 pre-existing source-linked assets. Its coverage determination is preserved in [evidence_asset_inventory.md](<review_1_5_1/evidence_asset_inventory.md>).

## Scope, Complete Coverage, and Exclusions

All 70 direct-source PDF pages were mapped: DOC-001 9/9, DOC-002 26/26, DOC-003 24/24, and DOC-004 11/11. Reusable plus fresh-required units equal total units for each source, and mapped units equal total units. The complete page-level accounting is in [source_coverage.md](<review_1_5_1/source_coverage.md>) and the stage-level scope is in [coverage_manifest.md](<review_1_5_1/coverage_manifest.md>).

The review assessed numeric, denominator/proportion/total, inferential-statistical, cross-document, measure/label/scale, and rate-versus-count consistency in supplied sources. It did not perform a broad methodology, clinical, raw-data, misconduct, novelty, or external-literature review. A failed protocol text/OCR derivative did not leave a coverage gap: all 26 DOC-002 pages were mapped through direct rendered-page inspection.

## Quantitative and Statistical Relationship Coverage

The normalized quantitative/reporting inventory contains N001-N062 (62/62 reviewed). The inferential-statistical inventory contains S001-S024 (24/24 reviewed). The main and support mapping artifacts preserve all relationship definitions and source locations: [main quantitative evidence](<review_1_5_1/extraction/main_quantitative_evidence.md>), [support quantitative evidence](<review_1_5_1/extraction/support_quantitative_evidence.md>), [numeric relationship inventory](<review_1_5_1/relationships/numeric_relationship_inventory.md>), and [statistical relationship inventory](<review_1_5_1/statistics/relationship_inventory.md>).

Both independent statistical passes completed every S001-S024 relationship. Pass 1 was performed by `root/statistical_pass_1` (gpt-5.6-terra, high) and recorded `PASS_1_COMPLETE` for 24/24 relationships in [statistical_pass_1.md](<review_1_5_1/checkers/statistical_pass_1.md>). Pass 2 was performed by the distinct `root/statistical_pass_2` (gpt-5.6-terra, high) and recorded `PASS_2_COMPLETE` for 24/24 relationships in [statistical_pass_2.md](<review_1_5_1/checkers/statistical_pass_2.md>). Neither pass registered a display-zero-only candidate.

## Candidate Index

| Stable ID | Candidate | Primary category | Status |
|---|---|---|---|
| [C001](#c001--conflicting-confidence-intervals-for-the-matched-any-stroke-rate-ratio) | Conflicting confidence intervals for the matched any-stroke rate ratio | Cross-document numeric inconsistency | Pending Human Adjudication |
| [C002](#c002--stroke-subtype-counts-do-not-partition-the-displayed-any-stroke-count-in-the-patch-group) | Stroke subtype counts do not partition the displayed any-stroke count in the patch group | Numeric or arithmetic inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Conflicting confidence intervals for the matched any-stroke rate ratio

**Candidate statement:** The abstract and detailed results/Figure 4B report the same any-stroke arm counts and rate-ratio point estimate but different 95% confidence-interval endpoints.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** DOC-001: [jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf — PDF p. 1](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1>) (abstract); [PDF p. 5](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5>) (results narrative); and [PDF p. 7](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7>) (Figure 4B).

**Source evidence:** Page 1 prints patch 69 (2.7%) versus usual care 64 (2.5%), rate ratio 1.08 (95% CI 0.76-1.53). Pages 5 and 7 print the same 69 versus 64 and rate ratio 1.08 but 95% CI 0.77-1.51 for the 2.5-year any-stroke comparison.

**Reported-versus-comparator:** Abstract CI 0.76-1.53 versus detailed-results/Figure 4B CI 0.77-1.51 for the same displayed counts, follow-up context, and point estimate.

**Reasoning procedure:** Match population, contrast, outcome, follow-up, effect measure, counts, and point estimate, then compare the two-decimal CI endpoints. No distinct estimand or interval method is labeled at the cited locations.

**Calculation:** Lower endpoints differ by `0.77 - 0.76 = 0.01`; upper endpoints differ by `1.53 - 1.51 = 0.02`. This direct printed-value comparison does not select either interval as correct.

**Alternative source-grounded interpretations:** One location may contain a transcription or production-rounding difference; separate interval calculations may have been used but not labeled; or one display may not have received the same update. Event times, O-E, V, unrounded endpoints, and the exact CI procedure are not supplied.

**Mechanical evidence recheck:** Direct PDF inspection found all three cited locations and matched the same groups, counts, percentages, 2.5-year context, and rate ratio. The detailed narrative and Figure 4B agree with each other. The recheck reproduced the 0.01 and 0.02 endpoint differences and confirmed that the supplied sources lack inputs needed to select an intended interval.

**Quality-control relevance:** A reader or evidence extractor could treat the two interval pairs as separate or choose one without knowing which is intended.

**Potential downstream evidence impact:** If confirmed, an extractor, systematic review, or meta-analysis could copy a nonauthoritative CI endpoint pair for this outcome; no effect on the paper’s conclusion is inferred.

**Human verification steps:** Inspect the analysis output for the 69-versus-64 any-stroke comparison, confirm the CI method and estimand, and compare the intended rounded endpoints with all three printed locations.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Stroke subtype counts do not partition the displayed any-stroke count in the patch group

**Candidate statement:** Figure 4B prints patch-group presumed ischemic and hemorrhagic stroke counts whose sum exceeds the patch-group `Any stroke` count, while the usual-care counts reconcile.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** DOC-001: [jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf — PDF p. 7](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7>), Figure 4B rows `Presumed ischemic stroke`, `Hemorrhagic stroke`, and `Any stroke`, including its caption/footnote. The matching any-stroke total also appears on [PDF p. 5](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5>) and [PDF p. 1](<../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1>).

**Source evidence:** Figure 4B prints patch/usual care respectively: presumed ischemic stroke 60 (2.4%)/58 (2.3%); hemorrhagic stroke 12 (0.5%)/6 (0.2%); and any stroke 69 (2.7%)/64 (2.5%). The figure labels the columns `No. of events (%)`, describes events from randomization through 2.5 years, and defines presumed ischemic stroke as including unspecified stroke.

**Reported-versus-comparator:** If subtype rows are mutually exclusive participant-level components counted under the same rule, patch subtypes total 72 versus `Any stroke` 69, while usual-care subtypes total 64 versus `Any stroke` 64.

**Reasoning procedure:** Compare the displayed integer component counts with the displayed total under a conditional partition identity; separate direct arithmetic from the unresolved overlap and counting convention. The supplied figure does not establish that the subtype rows are mutually exclusive, exhaustive, or unique-participant counts.

**Calculation:** Patch: `60 + 12 = 72`, three above 69. Usual care: `58 + 6 = 64`, equal to 64. Displayed patch percentages give 2.4% + 0.5% = 2.9% versus 2.7%, but integer counts establish the observation. The individual percentages reproduce from `n = 2520`, so percentage rounding does not explain the integer-count relationship.

**Alternative source-grounded interpretations:** Stroke types may overlap; one participant may contribute multiple stroke records/types; `Any stroke` may count unique participants while subtype rows count events; or record-source/classification rules may create overlap. The supplied figure does not specify the necessary counting convention. The usual-care equality does not establish exclusivity.

**Mechanical evidence recheck:** Direct Figure 4B inspection matched all six printed values, shared denominators, 2.5-year window, and `No. of events (%)` label. It reproduced patch `60 + 12 = 72` versus 69 and usual-care `58 + 6 = 64`, and confirmed that the source supplies no exclusivity, overlap, recurrence, participant-level uniqueness, or deduplication rule.

**Quality-control relevance:** Without the counting rule, a reader may incorrectly treat the subtype rows as a mutually exclusive partition of all stroke outcomes.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could sum nonexclusive subtype counts or misstate the all-stroke composition in a systematic review or evidence table; no conclusion change is inferred.

**Human verification steps:** Inspect participant-level derivation and event-classification rules; determine whether subtype rows count unique participants or events and whether overlap is permitted; then verify the three patch counts and corresponding footnote.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, C001 could affect which confidence-interval endpoints are entered for the matched stroke rate ratio, and C002 could affect how subtype counts are summed or described. These are bounded possibilities for evidence extraction, systematic reviews, meta-analyses, guidelines, or evidence tables. The supplied package does not establish that any downstream reuse occurred or that a paper-level conclusion changed.

## Limitations and Missing Definitions

- DOC-002’s native text layer was unusable and a targeted local CPU Tesseract attempt produced empty text; direct rendered-page inspection nevertheless mapped all 26 protocol pages.
- The supplied aggregate sources do not include event times, arm-specific censoring records, O-E, V, unrounded endpoints, or exact confidence-interval output needed to select the intended C001 interval.
- The supplied aggregate sources do not include participant-level stroke classifications, overlap counts, recurrence rules, or an event-versus-participant counting convention needed to determine whether C002 subtype rows should partition `Any stroke`.
- Several permutation, heterogeneity, and time-to-event relationships cannot be exactly reconstructed because raw observations, resampling output, test statistics, degrees of freedom, covariance, or complete model output were not supplied. Diagnostic checks did not replace reported analyses.
- No structured participant-level dataset was supplied. These evidence limitations did not leave any direct-source page unmapped.

## Human Adjudication Checklist

For C001, verify the intended 95% CI from source analysis output, its estimand, and any analysis-snapshot or interval-method distinction. For C002, verify each row’s unit of count, whether subtype overlap is permitted, and the `Any stroke` deduplication or first-event rule. Record each decision only in the card’s blank adjudication fields after human review.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

- **Profile:** 1.5.1
- **Package root:** `/home/bulunte/ai-paper-val/2025/jama.2025.15440`
- **Direct-source inventory:** [source_inventory.md](<review_1_5_1/source_inventory.md>)
- **Coverage ledger:** [source_coverage.md](<review_1_5_1/source_coverage.md>)
- **Coverage manifest:** [coverage_manifest.md](<review_1_5_1/coverage_manifest.md>)
- **Source hashes before review:** [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>)
- **Reused-asset hashes before review:** [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>)
- **Source hashes after review:** Recomputed against [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>); 4/4 matched.
- **Reused-asset hashes after review:** Recomputed against [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>); 51/51 matched.
- **Source-integrity result:** PASS — all 4 direct sources and all 51 reused artifacts were unchanged; see [integrity verification](<review_1_5_1/integrity_verification.md>).

### Agent Execution

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode | Canonical artifact |
|---|---|---|---|---|---|
| Coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | [run_state.md](<review_1_5_1/run_state.md>) |
| Asset curation | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | [evidence_asset_inventory.md](<review_1_5_1/evidence_asset_inventory.md>) |
| Main mapping | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | [main quantitative evidence](<review_1_5_1/extraction/main_quantitative_evidence.md>) |
| Support mapping | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | [support quantitative evidence](<review_1_5_1/extraction/support_quantitative_evidence.md>) |
| Numeric review | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | [numeric consistency](<review_1_5_1/checkers/numeric_consistency.md>) |
| Statistical pass 1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | [statistical pass 1](<review_1_5_1/checkers/statistical_pass_1.md>) |
| Cross-source review | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | [cross-source consistency](<review_1_5_1/checkers/cross_source_consistency.md>) |
| Evidence recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | [evidence recheck](<review_1_5_1/verification/evidence_recheck.md>) |
| Statistical pass 2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | [statistical pass 2](<review_1_5_1/checkers/statistical_pass_2.md>) |
| Evidence-quality audit | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | [evidence quality audit](<review_1_5_1/quality/evidence_quality_audit.md>) |
| Report generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | [final_report_1_5_1.md](<final_report_1_5_1.md>) |

### Performance

- **Target basis:** Four supplied PDFs contain 70 pages, including a 9-page main article, two method-support documents totaling 50 pages, and an 11-page results supplement; 17 pages have reusable source-linked extraction while 53 pages require fresh native/layout inspection, with moderate table and cross-document relationship complexity.
- **Total source units:** 70
- **Fresh-source units:** 53
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-09-03T03:43:05Z
- **Finished UTC:** 2026-09-03T04:24:17Z
- **Observed elapsed minutes:** 41.2
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token-Usage and Cost Metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Responses | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 unavailable runtime records | 0 known | 0 known | 0 known | 0.000000 known; complete estimate unavailable |
| gpt-5.6-terra | 8 unavailable runtime records | 0 known | 0 known | 0 known | 0.000000 known; complete estimate unavailable |

Token accounting is an incomplete token-only API-equivalent estimate under the 2026-08-18 pricing snapshot, not an invoice. The runtime exposed no authoritative per-response token counts for the coordinator or 10 specialists, so 0 means known tokens only and the complete count and price remain unavailable. Cached-input and cache-write values, when present, are input subsets; reasoning values, when present, are output subsets and are not added again to total tokens. Model and per-agent details are retained in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>) and [token_usage_ledger.csv](<review_1_5_1/token_usage_ledger.csv>).
