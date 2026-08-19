# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.5.3

> **Pending Human Adjudication:** Every candidate below is a quality-control observation retained for human review. This report does not make a final correction or conclusion about the paper.

## Executive Quality-Control Summary

Complete source and relationship coverage produced **3 stable candidate IDs**: C001, C002, and C003. The review concerns numeric reconciliation, cross-document percentages, and effect-measure labeling. Small preventable reporting defects can matter for downstream evidence extraction if confirmed; this report does not assert that any propagation, conclusion change, or serious harm occurred.

## Package and Reused-Evidence Provenance

The supplied package contains three direct PDF sources: [jama_dupuis_2024_oi_240111_1733431204.38761.pdf](<../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=1>), [joi240111supp1_prod_1733431204.57929.pdf](<../joi240111supp1_prod_1733431204.57929.pdf#page=1>), and [joi240111supp2_prod_1733431204.76024.pdf](<../joi240111supp2_prod_1733431204.76024.pdf#page=1>). Direct-source hashes and reusable-asset hashes were recorded before review in [source_hashes_before.sha256](<review_1_5_3/source_hashes_before.sha256>) and [reused_artifact_hashes_before.sha256](<review_1_5_3/reused_artifact_hashes_before.sha256>).

Reusable native text covered all 11 pages of DOC-001 and all 23 pages of DOC-003; DOC-002's 46 pages were freshly mapped from the supplied PDF. Reused derivatives were provenance and locating aids, not substitutes for direct-source confirmation. The reusable-asset inventory is [evidence_asset_inventory.md](<review_1_5_3/evidence_asset_inventory.md>).

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 protocol/SAP supplement | 46 | 0 | 46 | 46 | COMPLETE |
| DOC-003 results supplement | 23 | 23 | 0 | 23 | COMPLETE |
| **Total** | **80** | **34** | **46** | **80** | **COMPLETE** |

The coverage manifest and source ledger record a complete, disjoint mapping without a review queue, top-N subset, candidate cap, or deferred-by-cap section: [coverage_manifest.md](<review_1_5_3/coverage_manifest.md>) and [source_coverage.md](<review_1_5_3/source_coverage.md>). This review excludes broad study-design, clinical, novelty, misconduct, and raw-data auditing. Coherent display-zero P values were not treated as candidates; none of the three cards concerns a `P = 0` display.

## Quantitative and Statistical Relationship Coverage

The numeric inventory contains N001-N080, all checked by the numeric and cross-source lanes. The inferential inventory contains S001-S057. Statistical pass 1 and the independent statistical pass 2 each completed every S relationship; pass 2 revisited the full ledger and mechanical-recheck facts. C003 applies to S045-S047 and is recorded once because it concerns one shared header and one methods comparator.

- [Numeric relationship inventory](<review_1_5_3/relationships/numeric_relationship_inventory.md>) — N001-N080.
- [Statistical relationship inventory](<review_1_5_3/statistics/relationship_inventory.md>) — S001-S057, with `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records.
- [Statistical pass 1](<review_1_5_3/checkers/statistical_pass_1.md>) and [statistical pass 2](<review_1_5_3/checkers/statistical_pass_2.md>) — independent complete passes.
- [Mechanical evidence recheck](<review_1_5_3/verification/evidence_recheck.md>) — C001-C003.

## Candidate Index

| ID | Category | Short description | Status |
|---|---|---|---|
| [C001](#c001--usual-care-exclusion-hierarchy-requires-source-layout-confirmation) | Numeric or arithmetic inconsistency | Stable record retained to confirm the visual exclusion hierarchy; the source-grounded hierarchy reconciles. | Pending Human Adjudication |
| [C002](#c002--main-text-rejected-statement-percentage-conflicts-with-the-supplement-counts) | Cross-document numeric inconsistency | Main-text 6.4% rejected versus the displayed eTable 3 aggregate of 142/1,350 = 10.5%. | Pending Human Adjudication |
| [C003](#c003--etable-10-labels-logistic-regression-odds-ratios-as-differences) | Measure, label, or scale inconsistency | eTable 10 `Difference (95% CI)` header versus eMethods odds-ratio estimand. | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Usual-care exclusion hierarchy requires source-layout confirmation

**Candidate statement:** Stable C001 is retained for human confirmation of Figure 1's visual parent-child hierarchy. The direct source supports reconciliation, not a 71-versus-58 mismatch: the nested reasons sum to their parent and the top-level reasons sum to 58.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [jama_dupuis_2024_oi_240111_1733431204.38761.pdf — Figure 1, PDF p. 5](<../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5>), usual-care branch.

**Source evidence:** The source prints `58 Patients excluded`. Visual indentation places `13 Physician preference` at the top level and `7 Disease status or progression`, `4 Perceived psychosocial issues`, and `2 Reason not provided` beneath it. The other top-level counts are 15, 14, 7, 4, 3, and 2. The parallel branch presents a matching parent-child convention: 32 + 4 + 2 + 4 = 42.

**Reported-versus-comparator:** The printed exclusion total is 58; the source-layout comparator is the top-level hierarchy, not a flat list of all displayed counts.

**Reasoning procedure:** Reconcile children to their immediate parent, then reconcile only top-level reasons to the parent exclusion count. This avoids double-counting a parent and its nested children.

**Calculation:** 7 + 4 + 2 = 13. Then 13 + 15 + 14 + 7 + 4 + 3 + 2 = 58. The surrounding flow also reconciles: 323 - 58 = 265 and 265 - 41 = 224.

**Alternative source-grounded interpretations:** A production-layout error could make the indentation misleading, although the parallel branch supports the hierarchy interpretation. No flat 71-versus-58 comparison is carried forward.

**Mechanical evidence recheck:** Direct page inspection found the cited box, counts, indentation, and parallel branch. Counts and indentation are direct observations; interpreting indentation as hierarchy is the source-grounded logical reading. The remaining question is whether the production source confirms that intended hierarchy.

**Quality-control relevance:** A stable candidate record requires human layout confirmation because flattened extraction can lose nesting. The printed hierarchy itself reconciles; this card does not assert a participant-flow defect.

**Potential downstream evidence impact:** If the hierarchy were misread, a data extractor could double-count the physician-preference parent and its subreasons. This is a bounded possibility, not a claim that downstream propagation or conclusion change occurred.

**Human verification steps:** Inspect the production Figure 1 layout and confirm whether the indentation and parallel branch encode the stated parent-child structure; retain the top-level reconciliation if confirmed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Main-text rejected-statement percentage conflicts with the supplement counts

**Candidate statement:** The main text reports 6.4% rejected across intervention sites, whereas the displayed eTable 3 reject counts and equal denominators imply 142/1,350 = 10.5%.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_dupuis_2024_oi_240111_1733431204.38761.pdf — narrative, PDF p. 2](<../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2>) and [joi240111supp2_prod_1733431204.76024.pdf — eTable 3, PDF p. 6](<../joi240111supp2_prod_1733431204.76024.pdf#page=6>).

**Source evidence:** The main text prints 40.8% adopted, 48.7% adapted, and 6.4% rejected across intervention sites. eTable 3 prints n=135 at each of 10 sites and reject counts of 15, 23, 5, 25, 9, 25, 12, 11, 11, and 6.

**Reported-versus-comparator:** Reported: 6.4% rejected. Comparator from the displayed eTable 3 rejection counts and denominators: 10.5% to one decimal place.

**Reasoning procedure:** Sum the printed reject counts and divide by the common displayed decision total of 10 x 135. Confirm the common denominator from the three adaptation-choice counts at each site.

**Calculation:** Rejects = 15 + 23 + 5 + 25 + 9 + 25 + 12 + 11 + 11 + 6 = 142; total decisions = 10 x 135 = 1,350; 142 / 1,350 x 100 = 10.5185...%, or 10.5%. Keep and adapt totals are 551 and 657, reproducing 40.8% and 48.7%, respectively.

**Alternative source-grounded interpretations:** The narrative could use an unprinted unique-statement population or narrower rejection definition rather than site-statement decisions. The supplied locations do not provide the numerator, denominator, exclusions, weighting, or aggregation rule necessary to reproduce 6.4%; equal site denominators make ordinary weighting insufficient as an explanation.

**Mechanical evidence recheck:** Direct-source inspection matched the narrative, every eTable 3 denominator, counts, row labels, and site percentages. The aggregate calculation is arithmetic; a different population or definition is an unprinted possible explanation. The remaining human question is the exact basis of 6.4%.

**Quality-control relevance:** The printed percentage and table-implied aggregate do not reconcile under the displayed common denominator, so the reporting basis needs human clarification.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer, meta-analyst, guideline developer, or data extractor could copy either 6.4% or 10.5% as the intervention-implementation rejection proportion. This report does not claim that any such reuse occurred or changed a conclusion.

**Human verification steps:** Identify the numerator, denominator, decision population, exclusions, and aggregation method used for the narrative percentage; then reconcile the narrative and eTable 3 or document their distinct definitions.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 10 labels logistic-regression odds ratios as differences

**Candidate statement:** eTable 10 labels its modeled-effect columns `Difference (95% CI)`, while eMethods states that the documentation, any-intervention, and symptom-specific-intervention analyses estimate odds ratios using logistic regression.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi240111supp2_prod_1733431204.76024.pdf — eTable 10 start, PDF p. 13](<../joi240111supp2_prod_1733431204.76024.pdf#page=13>); [joi240111supp2_prod_1733431204.76024.pdf — eTable 10 continued values, PDF p. 14](<../joi240111supp2_prod_1733431204.76024.pdf#page=14>); [joi240111supp2_prod_1733431204.76024.pdf — eTable 10 footnote, PDF p. 15](<../joi240111supp2_prod_1733431204.76024.pdf#page=15>); and [joi240111supp2_prod_1733431204.76024.pdf — eMethods, PDF p. 22](<../joi240111supp2_prod_1733431204.76024.pdf#page=22>).

**Source evidence:** On p. 13, eTable 10 prints `Difference (95% CI)` under each cohort group. Examples include 0.53 (0.28, 1.01) on p. 13 and 5.30 (2.50, 11.24) and 17.96 (1.03, 313.1) on p. 14; p. 15 identifies mixed- or fixed-effects logistic regression for P values. On p. 22, eMethods states that the relevant logistic-regression analyses estimate the odds ratio.

**Reported-versus-comparator:** Reported table label: `Difference (95% CI)`. Methods comparator: odds ratio, a multiplicative effect measure with null value 1.

**Reasoning procedure:** Compare the shared table header with the effect measure expressly named for all three outcome blocks in eMethods. This is a label-to-estimand identity check, not a reconstruction of P values, standard errors, or model coefficients.

**Calculation:** No arithmetic reconstruction is needed. The representative estimates and intervals are organized around the multiplicative null of 1, consistent with the named odds-ratio estimand.

**Alternative source-grounded interpretations:** `Difference` may have been intended as a generic umbrella label for the modeled comparison while every cell remains an odds ratio. The package does not define that usage or identify any block as an additive difference.

**Mechanical evidence recheck:** Direct inspection confirmed the header, three cohort and outcome blocks, representative values, logistic-regression footnote, and eMethods odds-ratio statement. The logical comparison is source-grounded; a generic-heading intent is inferred rather than stated.

**Quality-control relevance:** Effect-measure labels guide how estimates are interpreted and extracted. The observation concerns the column heading, not a claim that the reported odds-ratio values or inferential conclusions are numerically incorrect.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could misclassify these odds ratios as additive differences. This is a bounded risk statement and does not assert actual propagation, conclusion change, or harm.

**Human verification steps:** Confirm the intended estimand for each eTable 10 block; if all are odds ratios, determine whether the shared header should explicitly identify odds ratios, or document any block using another measure.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Reporting defects can be copied when structured data are abstracted into evidence tables, systematic reviews, meta-analyses, guidelines, or secondary analyses. Here, the bounded possibilities are double-counting a nested flow reason (C001), selecting a nonreconciling rejection percentage (C002), or assigning the wrong effect-measure type (C003). These are conditional extraction risks only; the package supplies no evidence that any downstream product used the values, that a paper conclusion changed, or that serious harm occurred.

## Limitations and Missing Definitions

The full limitations record is [limitations.md](<review_1_5_3/limitations.md>). In brief, C002 lacks the printed definition needed to reproduce 6.4%; C003 lacks a definition for the word `Difference`; C001 needs production-layout confirmation even though the visual hierarchy reconciles; and several inferential results lack details needed for reverse-engineering. No external sources were used.

## Human Adjudication Checklist

1. Confirm the Figure 1 hierarchy for C001 from the production layout.
2. Determine the numerator, denominator, population, and aggregation for C002's 6.4% value.
3. Confirm the intended eTable 10 estimand and header for C003.
4. Complete every five-field adjudication block in the evidence cards; no field has been pre-filled.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

Routing preflight passed under the required interactive route, with all nine named role presets verified: [routing_preflight.md](<review_1_5_3/routing_preflight.md>). Direct and reusable asset hashes were captured before review; post-run hash comparison remains a coordinator completion step.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort |
|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium |
| numeric_consistency_reviewer | root/numeric_consistency_reviewer | gpt-5.6-terra | medium |
| cross_source_consistency_reviewer | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high |
| quality_control_auditor | root/quality_control_auditor | gpt-5.6-sol | high |
| report_generator | root/report_generator | gpt-5.6-terra | medium |

The authoritative execution manifest is [agent_execution_manifest.md](<review_1_5_3/agent_execution_manifest.md>).

### Reproducibility performance

- **Target basis:** This package has 80 unique PDF-page units across a main article, a 46-page protocol/SAP lacking any reusable extraction, and a 23-page results supplement. Thirty-four pages have complete native reusable text, while 46 require fresh direct extraction. The package therefore has a substantial fresh-PDF burden plus cross-document/table/figure relationship work, but less total unit volume than the 102-unit calibration package.
- **Total source units:** 80
- **Fresh-source units:** 46
- **Target elapsed minutes:** 45-65
- **Started UTC:** 2026-08-19T04:38:04Z
- **Finished UTC:** 2026-08-19T05:06:24Z
- **Observed elapsed minutes:** 28.3
- **Target status:** MET_TARGET
- **Exceedance causes:** None

The timing window closed immediately after complete Markdown assembly; local calculation, rendering, and validation are excluded.

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |

Authoritative runtime token counts were not exposed for the coordinator or specialist responses, so every manifested agent has an `UNAVAILABLE` record and the complete count and price remain incomplete. The displayed zeros are known subtotals only, not estimates of unexposed usage. Per-agent detail is in [token_usage_summary.md](<review_1_5_3/token_usage_summary.md>). Cached input and cache-write tokens are input subsets, and reasoning tokens are an output subset; none is added again to total tokens. Any available cost uses the bundled dated fixed-model rates, is token-only, and is not an invoice.
