# Quantitative Quality-Control Consistency Review — Workflow 1.5.3

## Pending Human Adjudication

All six candidate consistency issues in this report are **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a determination that a correction is required or that the paper's conclusions are changed.

## Executive Quality-Control Summary

Complete source coverage identified six stable candidate consistency issues: two denominator/proportion/total issues, one cross-document numeric issue, and three measure, label, or scale issues. The review rebuilt discovery comprehensively and retained every stable ledger ID, C001 through C006. The observations are confined to supplied-source reporting consistency. Small preventable defects can matter when information is later extracted into evidence products, but this review does not claim that propagation, conclusion change, or serious harm occurred.

## Package and Reused-Evidence Provenance

The package contains four supplied PDFs: the main article (DOC-001), protocol/SAP (DOC-002), Supplement 2 (DOC-003), and data-sharing statement (DOC-004). Direct PDFs were the authority. Existing native/layout text and rendered pages were reused only as source-matched locators or transcription aids.

| Source | Direct-source units | Reusable units | Fresh direct-source units | Mapped units |
|---|---:|---:|---:|---:|
| DOC-001 main article | 11 | 11 | 0 | 11 |
| DOC-002 protocol/SAP | 65 | 0 | 65 | 65 |
| DOC-003 Supplement 2 | 22 | 15 | 7 | 22 |
| DOC-004 data-sharing statement | 1 | 0 | 1 | 1 |
| **Total** | **99** | **26** | **73** | **99** |

The reusable-asset inventory records 54 source-linked assets: 43 usable and 11 partial. No reused asset was treated as final authority. Source and reused-asset provenance is recorded in `review_1_5_3/source_inventory.md`, `review_1_5_3/evidence_asset_inventory.md`, and the corresponding before-review hash manifests.

## Scope, Complete Coverage, and Exclusions

All 99 of 99 PDF-page units were mapped, with 26 reusable-backed and 73 fresh direct-source units. The review covered numeric, denominator, proportion, total, inferential, cross-document, measure/label/scale, and rate/count relationships. Protocol planning quantities, contextual literature quantities, administrative text, and sparse unlabelled plot coordinates were mapped but not manufactured into observed-result comparisons. There were no supplied structured data, Office, workbook, or CSV sources.

Coherent display-zero P values were excluded from candidate registration. No stable card is based on `P = 0`, `p = 0.000`, finite precision, underflow, or reconstructed tail probabilities.

## Quantitative and Statistical Relationship Coverage

- Numeric/reporting relationships: 91 stable relationships (N001-N088 plus N038a, N038b, and N039a).
- Statistical/inferential relationships: 151 stable relationships (S001-S148 plus S028a, S028b, and S029a).
- Statistical pass 1: all 151 relationships received `PASS_1_COMPLETE` coverage.
- Statistical pass 2: all 151 relationships received `PASS_2_COMPLETE` coverage after ledger and recheck review.

The supplied model definitions supported direction, label, interval-order, and matched-result checks. Exact statistical reconstruction was not used where row-specific test details, degrees of freedom, covariance, variance, confidence conventions, or unrounded output were absent.

## Candidate Index

| Stable ID | Primary category | Candidate statement |
|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | Figure 1 allocation branches total 315 beneath a displayed parent cohort of 305. |
| C002 | Measure, label, or scale inconsistency | Supplement eTable 2 mixes year-12 headings with year-7 quantitative footnote definitions. |
| C003 | Cross-document numeric inconsistency | Matched 12-year HbA1c results have incompatible printed P values. |
| C004 | Measure, label, or scale inconsistency | The same year-7 HbA1c outcome uses `<=6.5%` in narrative and `<6.5%` in Table 2. |
| C005 | Denominator, proportion, or total inconsistency | The abstract's 2.2% for four deaths does not reconcile with displayed group counts and denominators. |
| C006 | Measure, label, or scale inconsistency | The same BMI subgroup boundary is labeled both `>=35` and `>35`. |

## Candidate Evidence Cards

## C001 — Figure 1 allocation branches exceed the displayed available cohort by 10 participants

**Candidate statement:** Figure 1 displays a 305-person available cohort that branches to treatment counts totaling 315.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 3](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3>), Figure 1 and adjoining Results text.

**Source evidence:** The figure states `305 Available for long-term follow-up and randomized`, then shows `193 Randomized to undergo bariatric surgery` and `122 Randomized to undergo medical/lifestyle intervention`. Its enrolled counts are 166 and 96.

**Reported-versus-comparator:** Reported parent: 305 available. Comparator branches: 193 + 122 = 315. Separately, enrolled counts 166 + 96 = 262.

**Reasoning procedure:** Treat the connected treatment boxes as a partition only conditionally, because the source does not separately define the 193/122 population. Compare their displayed sum to the displayed parent and keep the enrolled identity distinct.

**Calculation:** `193 + 122 = 315`; `315 - 305 = 10`. Separately, `166 + 96 = 262`, and `262 / 305 × 100 = 85.90%`, consistent with the printed 86% after rounding.

**Alternative source-grounded interpretations:** The branch counts may preserve an earlier assignment cohort; the parent total may be wrong; or one or both branch counts or population labels may be wrong. The treatment-arm distribution of the 11 persons between 316 eligible and 305 available is not supplied.

**Mechanical evidence recheck:** Direct PDF inspection found the 305 parent, 193/122 branches, 166/96 enrolled counts, and adjoining flow text. The arithmetic was reproduced; no participant-level flow crosswalk is available.

**Quality-control relevance:** This is a reproducible printed flow/denominator identity issue. It does not establish that a treatment-effect analysis used an incorrect denominator.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an allocation count, available-cohort count, retention denominator, or missingness quantity inconsistently. No propagation or conclusion change is asserted.

**Human verification steps:** Inspect the participant-flow source dataset and figure-production record; identify the population represented by 193 and 122; then align the relevant parent count, branch count, or population label.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Supplement eTable 2 mixes year-12 headings with year-7 quantitative footnote definitions

**Candidate statement:** eTable 2 presents year-12 headings while key footnotes define its quantitative outputs at year 7.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi240004supp2_prod_1721756962.82552.pdf — PDF p. 15](<../joi240004supp2_prod_1721756962.82552.pdf#page=15>), eTable 2 title, columns, rows, and footnotes a-b; [joi240004supp2_prod_1721756962.82552.pdf — PDF p. 16](<../joi240004supp2_prod_1721756962.82552.pdf#page=16>), footnotes c-e; [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 3](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3>), Results pointer to eTable 2.

**Source evidence:** The supplement title and both value columns state year 12; footnote e calls remission a 12-year rate. Footnotes a-c refer to baseline and year-7 data, 7-year-over-baseline ratios/odds, 7-year changes, and odds at year 7. The main article identifies the HbA1c eTable 2 result as at 12 years.

**Reported-versus-comparator:** Reported headings and main-text pointer: year 12. Comparator footnote definitions: year 7.

**Reasoning procedure:** Compare explicit time labels that define the same table's descriptive values, changes, comparisons, binary odds ratios, and P values. No rounding rule can reconcile distinct follow-up times.

**Calculation:** No arithmetic is required: `year 12` and `year 7` are distinct timepoint definitions.

**Alternative source-grounded interpretations:** Footnotes may retain residual year-7 wording; the title/columns may be wrong; or the table may intentionally combine year-12 descriptive values with year-7 modeled quantities without a printed explanation.

**Mechanical evidence recheck:** Direct PDF inspection confirmed the title, two year-12 columns, footnotes a-c, footnote e, and the main-paper pointer. The missing input is a column-to-visit analysis or table-generation specification.

**Quality-control relevance:** The issue concerns timepoint/estimand labeling, not a determination that any displayed estimate is numerically wrong.

**Potential downstream evidence impact:** If confirmed, an extractor could attach a 7-year or 12-year timepoint to the wrong descriptive value, change, odds ratio, or P value. No actual propagation is asserted.

**Human verification steps:** Inspect eTable 2 analysis output and journal production proof; establish the intended visit for every descriptive, change, comparison, binary-odds, and P-value column; align all title, column, and footnote wording.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Matched 12-year HbA1c result has incompatible printed P values

**Candidate statement:** The main article and eTable 2 print the same displayed 12-year HbA1c estimate and interval with different P values.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 1](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1>), Abstract Results; [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 3](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3>), Results; [joi240004supp2_prod_1721756962.82552.pdf — PDF p. 15](<../joi240004supp2_prod_1721756962.82552.pdf#page=15>), eTable 2 HbA1c row.

**Source evidence:** Main-paper pages 1 and 3 print a surgery-minus-medical/lifestyle difference of `-1.1%` (95% CI, `-1.7% to -0.5%`) with `P = .002`; page 3 points to eTable 2. eTable 2 prints `-1.1 (-1.7, -0.5)` under its year-12 heading with `P < .001`.

**Reported-versus-comparator:** Main result: `P = .002`. Supplement comparator for the matching displayed estimate and interval: `P < .001`.

**Reasoning procedure:** Match population, timepoint label, contrast, estimate, and interval at printed precision, then compare the two P-value displays without reconstructing a test or tail probability.

**Calculation:** The estimate and interval agree at displayed precision. `.002 < .001` is false, so a displayed P value of `.002` is incompatible with `<.001` for an otherwise matched result.

**Alternative source-grounded interpretations:** One P value may be intended; the supplement may use a different unlabeled timepoint, test, model, or variance method. C002's conflicting timepoint footnotes leave the supplement estimand incompletely defined.

**Mechanical evidence recheck:** Direct PDF inspection confirmed both main-paper displays, the supplement row, and the cross-reference. Unrounded P values and complete row-specific analysis-output details are not supplied.

**Quality-control relevance:** This is a printed cross-document consistency issue. It does not determine which P value belongs to the intended analysis.

**Potential downstream evidence impact:** If confirmed as the same analysis, an extractor could copy `.002` or `<.001` for one effect record. No effect on a meta-analysis, guideline, or paper conclusion is asserted.

**Human verification steps:** Retrieve the exact year-12 model contrast and table-generation record; determine whether the locations use the same timepoint, test, model, and variance method; then align the P-value display or explicitly label the distinction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — The same year-7 glycemic outcome is labeled as both HbA1c less than or equal to 6.5% and HbA1c below 6.5%

**Candidate statement:** The narrative cites Table 2 for the same year-7 outcome while using `<=6.5%`; Table 2 uses `<6.5%`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 4](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=4>), Results narrative; [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 6](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=6>), Table 2; [joi240004supp2_prod_1721756962.82552.pdf — PDF p. 4](<../joi240004supp2_prod_1721756962.82552.pdf#page=4>), binary-analysis context.

**Source evidence:** The narrative states HbA1c `less than or equal to 6.5%` with `P = .002; Table 2`. The cited table row is `HbA1c <6.5%, %`, with 17.3% and 37.7%, OR 2.89 (95% CI 1.48-5.64), and `P = .002`.

**Reported-versus-comparator:** Reported narrative operator: `<=6.5%`. Table comparator operator: `<6.5%`, linked by the same P value and direct Table 2 citation.

**Reasoning procedure:** Compare the two threshold operators as measure definitions for the cited same outcome. Preserve uncertainty about data precision and programmed classification.

**Calculation:** `{x: x < 6.5}` is a subset of `{x: x <= 6.5}`; only values exactly equal to 6.5 differ in membership.

**Alternative source-grounded interpretations:** The prose may be imprecise, the table may omit equality, or an undocumented measurement-precision/rounding convention may reconcile the labels. The package does not report the number at exactly 6.5%.

**Mechanical evidence recheck:** Direct PDF inspection confirmed the narrative, cited table row, matching P value, and supporting GEE context. The programmed dichotomization condition, preclassification precision, row analysis counts, and boundary-value count are unavailable.

**Quality-control relevance:** The threshold operator is part of the outcome measure label. The observation does not establish a changed OR, P value, participant classification, or conclusion.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy different binary-outcome definitions. Any numerical impact remains conditional on observations exactly at 6.5%.

**Human verification steps:** Inspect the outcome-program condition, data dictionary, measurement precision, and analysis dataset for the row with `P = .002`; align the narrative, Table 2, and supporting definition to the verified condition.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Abstract percentage for four deaths does not reconcile with displayed group counts and denominators

**Candidate statement:** The abstract's 2.2% for four deaths does not match the combined percentage implied by displayed group counts and denominators.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 1](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=1>), Abstract Results; [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 3](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=3>), enrolled groups; [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 7](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7>), death narrative; [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 8](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=8>), Table 3.

**Source evidence:** The abstract reports `4 deaths (2.2%), 2 in each group`. The displayed enrolled groups are 96 medical/lifestyle and 166 surgery. Table 3 reports 2 (2.1%) of 96 and 2 (1.2%) of 166; the Results narrative also states four deaths, two per group.

**Reported-versus-comparator:** Abstract: four deaths, 2.2%. Comparator: four deaths among displayed group denominators totaling 262.

**Reasoning procedure:** Reproduce the two within-group percentages and the combined crude percentage from printed counts/denominators. Do not assume an unstated abstract risk set is absent.

**Calculation:** `2 / 96 × 100 = 2.0833%` → 2.1%; `2 / 166 × 100 = 1.2048%` → 1.2%; `4 / (96 + 166) × 100 = 1.5267%` → 1.5%, not 2.2%.

**Alternative source-grounded interpretations:** The abstract may use an unstated risk-set denominator or measure; its percentage may be a transcription difference; or Table 3 may represent a population not distinguished in the abstract. The package does not identify the abstract denominator.

**Mechanical evidence recheck:** Direct PDF inspection confirmed the abstract, group counts, death narrative, Table 3 counts, and their pages. The displayed within-group percentages reproduce; no participant-level mortality risk-set definition is supplied.

**Quality-control relevance:** This is a count/denominator consistency issue. It does not assume that 2.2% is a crude proportion or establish a change in the treatment comparison.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a mortality count, percentage, or denominator without a shared population definition. No propagation or paper-level conclusion change is asserted.

**Human verification steps:** Inspect the mortality analysis dataset, risk-set definition, and abstract production record; identify the denominator and measure for 2.2%; then align the abstract and Table 3 population wording or percentage as appropriate.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — The same exploratory BMI subgroup boundary is labeled as both 35 or greater and greater than 35

**Candidate statement:** The main article defines the higher exploratory BMI subgroup as 35 or greater, whereas eFigure 6 labels it greater than 35.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_courcoulas_2024_oi_240004_1721756962.76052.pdf — PDF p. 7](<../jama_courcoulas_2024_oi_240004_1721756962.76052.pdf#page=7>), Results narrative; [joi240004supp2_prod_1721756962.82552.pdf — PDF p. 13](<../joi240004supp2_prod_1721756962.82552.pdf#page=13>), eFigure 6 title, legends, and explanatory text.

**Source evidence:** The main article describes BMI 27 to `<35` versus BMI `35 or greater` and cites eFigure 6. eFigure 6 repeatedly labels the groups `BMI <35` and `BMI >35` for the corresponding HbA1c and weight-loss analysis.

**Reported-versus-comparator:** Main higher subgroup: `BMI >=35`. eFigure higher subgroup: `BMI >35`, with lower subgroup `BMI <35`.

**Reasoning procedure:** Compare complementary boundary operators for the explicitly linked two-part subgroup analysis, while keeping subgroup-code and boundary-value data absent.

**Calculation:** The complement of `{x: x < 35}` is `{x: x >= 35}`. The figure pair `{x: x < 35}` and `{x: x > 35}` leaves `x = 35` unassigned, whereas the main-text higher set includes it.

**Alternative source-grounded interpretations:** The figure may have omitted equality; the main wording may be imprecise; or no participant may have had unrounded BMI exactly 35. The supplied package does not establish which operator was implemented.

**Mechanical evidence recheck:** A fresh targeted direct-PDF recheck confirmed the main Results wording and repeated eFigure labels. Subgroup-creation code, data dictionary, unrounded BMI values, boundary-handling rule, and count exactly at 35 are unavailable.

**Quality-control relevance:** The observation concerns a subgroup-boundary label. It does not establish a different membership, estimate, P value, or paper-level conclusion.

**Potential downstream evidence impact:** If confirmed, an extractor could copy `>=35` or `>35` as the subgroup definition. Any impact on membership or quantitative estimates remains conditional on unavailable boundary data.

**Human verification steps:** Inspect subgroup-program code, data dictionary, input precision, and boundary-value handling; determine the implemented operator and align the main-text and figure labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these observations could affect the consistency with which a later systematic-review, meta-analysis, guideline, or data-extraction workflow records participant flow, timepoint, P value, threshold, event denominator, or subgroup definition. They are quality-control candidates only. The supplied package does not establish that any downstream record propagated an issue, that an effect estimate changed, or that the paper's conclusions changed.

## Limitations and Missing Definitions

The complete canonical limitations summary is in [limitations.md](<review_1_5_3/limitations.md>). The supplied PDFs lack several source records needed to resolve intended values or labels, including participant-level flow and risk-set definitions, analysis code, data dictionaries, row-specific model output, and unrounded boundary data. Sparse figures lacked tabulated coordinates. These constraints limit adjudication, not the completed coverage or inclusion of stable candidates.

## Human Adjudication Checklist

For each stable candidate, a human reviewer should:

1. Confirm the cited direct-source page(s) and transcription.
2. Inspect the named source dataset, analysis output, code, table-generation record, or production proof when available.
3. Decide whether a reporting inconsistency exists and, if so, identify the intended population, timepoint, analysis, threshold, denominator, or boundary.
4. Record validity, importance, action, initials, and notes in the card fields without altering stable IDs.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Routing preflight:** PASS; coordinator inference PASS; execution mode INTERACTIVE_CLI; all nine named presets verified.
- **Source coverage:** 99/99 mapped units; 26 reusable and 73 fresh direct-source units.
- **Direct-source hashes before review:** DOC-001 `0f153cf27727015b19cf33ba400d4c0cc36e20f58a1b85c08f74bd61f1d06647`; DOC-002 `75275168ca11fb55b11821a0a07067812181adfe0ccc4487e04ff2a0673f2958`; DOC-003 `4c2e87ee8ac1bcde5927e63f7b27ade27ace05dae1b6085dc81cb293c56afd81`; DOC-004 `cfdde1a6a79f4b81980f2a69b095d9c0fed24c77759968078fffecd5f26979f8`.
- **Reused-evidence integrity:** 54 hashed source-linked assets are listed in `review_1_5_3/reused_artifact_hashes_before.sha256`; final recomputation is coordinator-controlled.
- **Canonical review artifacts:** coverage, relationship inventories, checker records, ledger, recheck, audit, and limitations are retained under `review_1_5_3/`.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| reuse_asset_curator | runtime:/root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_quantitative_mapper | runtime:/root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_quantitative_mapper | runtime:/root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | runtime:/root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | runtime:/root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | runtime:/root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_rechecker | runtime:/root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | runtime:/root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_recheck_repair_c006 | runtime:/root/evidence_recheck_c006 | gpt-5.6-sol | high | FRESH_SPAWN |
| quality_control_auditor | runtime:/root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generator | runtime:/root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN |

### Performance profile

- **Target basis:** Four supplied PDFs contain 99 page units. Twenty-six units have source-matched reusable native text or rendered-page evidence, while 73 units require fresh direct-PDF mapping, including a 65-page protocol with no page-level derivative, seven uncovered supplement pages, and one administrative page. This scope is close to the 102-unit/81-fresh calibration but has mixed reusable visual evidence and requires full four-source coverage; 50-70 minutes is the bounded planning target.
- **Total source units:** 99
- **Fresh-source units:** 73
- **Target elapsed minutes:** 50-70
- **Started UTC:** 2026-08-19T04:28:49Z
- **Finished UTC:** 2026-08-19T04:58:55Z
- **Observed elapsed minutes:** 30.1
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Responses | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 4 unavailable records | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 8 unavailable records | 0 | 0 | 0 | 0.000000 |

Per-agent detail is recorded in `review_1_5_3/token_usage_summary.md`. Cached-input and cache-write tokens are input subsets; reasoning tokens are an output subset and are not added again to total tokens. The known amount uses the bundled dated fixed-model rates and is a token-only estimate, not an invoice; complete cost remains unavailable with runtime usage counts.
