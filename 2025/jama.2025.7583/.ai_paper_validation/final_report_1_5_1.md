# Quantitative Quality-Control Consistency Review: EMPROTECT Paper Package

## Pending Human Adjudication

Every observation in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a conclusion-validity, severity, correction, acceptance, or exclusion determination.

## Executive Quality-Control Summary

Complete uncapped review of the supplied package identified **3** distinct candidate consistency issues: one endpoint-boundary label inconsistency, one planned sample-size/attrition arithmetic inconsistency, and one surgery-type denominator/counting-rule inconsistency. The stable set is C001, C002, and C003. No candidate was registered for a coherent display-zero P value, and no top-N, review-queue, or deferred-by-cap process was used.

## Package and Reused-Evidence Provenance

The review covered five supplied PDFs: the 9-page main article, 63-page protocol, 23-page administrative supplement, 15-page results supplement, and 9-page statistical analysis plan (SAP). Direct PDFs were authoritative. Reused native text, normalized text, OCR, rendered pages, and document maps served only as source-linked locators or transcription aids; 92 reused artifacts were inventoried and integrity-checked.

Direct-source identities and baseline SHA-256 values are recorded in [source inventory](<review_1_5_1/source_inventory.md>) and [source hashes](<review_1_5_1/source_hashes_before.sha256>). Reused-asset provenance and hashes are recorded in [evidence asset inventory](<review_1_5_1/evidence_asset_inventory.md>) and [reused-artifact hashes](<review_1_5_1/reused_artifact_hashes_before.sha256>). The quality audit recorded unchanged revalidation of all five direct-source hashes and all 92 reused-artifact hashes.

## Scope, Complete Coverage, and Exclusions

The complete direct-source scope was 119 PDF pages: DOC-001 pp. 1-9, DOC-002 pp. 1-63, DOC-003 pp. 1-23, DOC-004 pp. 1-15, and DOC-005 pp. 1-9. Coverage closed at **119/119 mapped units**: 24 reusable units plus 95 fresh-required units. Every source row is `COMPLETE` in [source coverage](<review_1_5_1/source_coverage.md>).

The review assessed numeric, denominator, statistical, cross-document, measure/label/scale, and rate-versus-count relationships. It did not perform a general methodology, clinical, raw-data, misconduct, or external-literature audit. Protocol and SAP planning statements were compared with realized results only when population, time, contrast, outcome, model/estimand, scale, and precision established a matched relationship. No web sources were used.

## Quantitative and Statistical Relationship Coverage

The numeric inventory contains **N001-N089**; all 89 relationships received explicit numeric checking. The inferential-statistical inventory contains **S001-S052**. Each of its 52 relationships received `PASS_1_COMPLETE` in the first fresh statistical pass and `PASS_2_COMPLETE` in the distinct second fresh statistical pass. Both passes used `gpt-5.6-terra` at high reasoning effort and are documented in [statistical pass 1](<review_1_5_1/checkers/statistical_pass_1.md>) and [statistical pass 2](<review_1_5_1/checkers/statistical_pass_2.md>). The complete scope and one-artifact-per-row assignments are in the [coverage manifest](<review_1_5_1/coverage_manifest.md>).

## Candidate Index

| Stable ID | Candidate consistency issue | Category | Status |
|---|---|---|---|
| [C001](#c001--primary-endpoint-midline-shift-boundary-differs-across-matched-supplied-sources) | Primary-endpoint midline-shift boundary differs across matched supplied sources | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C002](#c002--printed-sample-size-attrition-allowance-does-not-reconcile-with-the-printed-target) | Printed sample-size attrition allowance does not reconcile with the printed target | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| [C003](#c003--standard-care-surgery-type-counts-exceed-their-shared-printed-denominator) | Standard-care surgery-type counts exceed their shared printed denominator | Denominator, proportion, or total inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Primary-endpoint midline-shift boundary differs across matched supplied sources

**Candidate statement:** Matched supplied sources define the same six-month primary-endpoint imaging component with different inclusion operators: inclusive `>=5 mm` versus strict `>5 mm`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main article — PDF p. 3](<../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>); [protocol — PDF p. 7](<../joi250033supp1_prod_1750956987.76581.pdf#page=7>); [protocol — PDF p. 16](<../joi250033supp1_prod_1750956987.76581.pdf#page=16>); [results supplement — PDF p. 15](<../joi250033supp4_prod_1750956987.77981.pdf#page=15>); [SAP — PDF p. 3](<../joi250033supp5_prod_1750956987.78281.pdf#page=3>).

**Source evidence:** The main article prints “5 mm or greater”; protocol pp. 7 and 16 and the results supplement print `>=5 mm`; the SAP prints `>5 mm`. Each occurrence is the same six-month homolateral-CSDH primary-endpoint imaging component, alongside the same symptomatic-CSDH alternative.

**Reported-versus-comparator:** The inclusive `>=5 mm` wording in the main article, protocol, and results supplement is compared with the SAP’s strict `>5 mm` wording.

**Reasoning procedure:** Match trial, endpoint, time point, imaging component, unit, and comparator wording; then compare the printed inequality operators. The operator difference is a direct observation, while its operational cause and any affected case are not established.

**Calculation:** For shift `x`, `x >= 5` includes `x = 5`; `x > 5` excludes `x = 5`. The set difference is the boundary value alone. Rounding cannot reconcile the two operators.

**Alternative source-grounded interpretations:** The SAP expression may be typographic or version-specific, or it may state the operational rule while the repeated inclusive expression states a different version. The supplied package does not identify the programmed adjudication rule or report whether any case had exactly 5-mm shift.

**Mechanical evidence recheck:** All five cited locations were found and their printed text directly matched. The endpoint, time point, unit, and component were matched; the logical comparison reproduced. Missing inputs are the operational rule, adjudication records, and participant-level measurements. The remaining human question is which boundary governed final adjudication and whether an exactly-5-mm case existed.

**Quality-control relevance:** A matched endpoint definition should preserve its threshold operator across supplied source documents so that the same condition is extracted and interpreted.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could encode an inclusive rather than exclusive endpoint boundary (or the reverse) from different supplied documents. No propagation, outcome-count change, or conclusion change is asserted.

**Human verification steps:** Confirm the approved protocol/SAP version and adjudication rule; inspect the adjudication charter or eCRF for the treatment of exactly 5 mm; determine whether any adjudicated recurrence had exactly 5-mm shift; and annotate or correct the discrepant source expression if warranted.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Printed sample-size attrition allowance does not reconcile with the printed target

**Candidate statement:** The printed 142-per-group requirement, stated 20% loss-to-follow-up allowance, and 171-per-group/342-total target do not reconcile under a true loss-fraction convention.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [Protocol — PDF p. 50](<../joi250033supp1_prod_1750956987.76581.pdf#page=50>); [SAP — PDF p. 4](<../joi250033supp5_prod_1750956987.78281.pdf#page=4>); [SAP — PDF p. 5](<../joi250033supp5_prod_1750956987.78281.pdf#page=5>); [main article — PDF p. 3](<../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>).

**Source evidence:** Protocol and SAP print 142 required participants per group, a 20% loss-to-follow-up assumption, and 342 total participants (171 per group); the main article repeats the 20% allowance and total 342. The protocol and SAP state that 142 per group accounts for the planned sequential tests.

**Reported-versus-comparator:** Printed enrollment is 171 per group/342 total. The comparator is the enrollment required to retain 142 per group after a stated 20% loss fraction.

**Reasoning procedure:** Establish the printed evaluable target and equal two-arm design, apply the stated retained fraction of 0.80, and distinguish an aggregate calculation from balanced whole-participant arm allocation. Do not infer an unprinted attrition convention.

**Calculation:** `142 * 2 = 284`. Under a 20%-of-enrollment loss fraction, `284 / 0.80 = 355` aggregate participants. With 1:1 whole-person allocation, `142 / 0.80 = 177.5`, requiring 178 per arm and **356 total**. The printed target gives `171 * 0.80 = 136.8` expected retained participants per arm. By contrast, adding 20% to the required count gives `142 * 1.20 = 170.4`, which can round upward to 171 per arm.

**Alternative source-grounded interpretations:** The authors may have treated “20% loss” as an addition to the required count, or an unstated sequential-design adjustment or unrounded software output may explain 342. The supplied sources do not state the attrition denominator, calculation convention, separate adjustment, or calculation trace.

**Mechanical evidence recheck:** The cited protocol, SAP, and main-article statements were directly located and matched. The arithmetic reproduced both the loss-fraction result and the alternative 20%-addition result. Necessary printed inputs are present; missing inputs are the unrounded output, attrition convention, and calculation trace. The remaining human question is which convention or documented calculation produced 171 per group.

**Quality-control relevance:** Planned enrollment and attrition assumptions should be arithmetically traceable, especially where a source supplies a per-arm requirement and enrollment target.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could reconstruct a different planned enrollment or attrition convention from the printed design information. No realized analysis defect, outcome change, or conclusion change is asserted.

**Human verification steps:** Retrieve the sample-size calculation output and sequential-design specification; identify the denominator and convention for the 20% allowance; verify any unrounded base or additional design adjustment; and reconcile or annotate the 142-per-group and 171-per-group statements.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Standard-care surgery-type counts exceed their shared printed denominator

**Candidate statement:** In Table 1’s standard-care column, two surgery-type numerators total 164 against their shared printed denominator of 163; clarification is required because the table does not state the participant-versus-procedure overlap rule.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Main article — PDF p. 5](<../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5>), Table 1, Treatment rows.

**Source evidence:** The standard-care column prints `146/163 (89.6%)` for trepanation burr-hole craniostomy and `18/163 (11.0%)` for trephine craniostomy. The header defines entries as `No./total No. (%)`; footnote e describes procedures performed either with a cranial drill or a skull trephine cylindrical saw.

**Reported-versus-comparator:** The two printed numerators, 146 and 18, are compared with their repeated denominator, 163, under the table’s participant-framed `No./total No. (%)` presentation.

**Reasoning procedure:** Reproduce the integer and percentage arithmetic, then retain the applicability of a mutually exclusive participant-category total as conditional because the source does not explicitly define overlap for bilateral procedures or participant-versus-procedure counting.

**Calculation:** `146 + 18 = 164`, one above 163. `146 / 163 * 100 = 89.570...%` rounds to 89.6%, and `18 / 163 * 100 = 11.042...%` rounds to 11.0%; the printed percentages sum to 100.6%. Rounding cannot remove the one-membership integer excess.

**Alternative source-grounded interpretations:** A participant with bilateral surgery could have received different techniques and been counted in both rows, allowing 164 row memberships among 163 participants. Alternatively, a printed numerator or denominator may need correction. The package does not establish either explanation.

**Mechanical evidence recheck:** Table 1 and the footnote were directly found and the printed fractions and percentages matched. The arithmetic reproduced. The necessary missing definition is whether technique rows are mutually exclusive per participant, whether bilateral procedures can appear in both rows, and whether numerators count people or procedures. The remaining human question is the applicable counting rule and, if overlap is not allowed, which printed value requires review.

**Quality-control relevance:** A shared denominator and category-count presentation should state overlap or counting rules when row memberships can exceed participant totals.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic review, meta-analysis, or guideline could treat 164 technique memberships as mutually exclusive participants under denominator 163. No actual reuse, outcome change, or conclusion change is asserted.

**Human verification steps:** Inspect participant-level procedure records and Table 1 programming; determine whether bilateral procedures can use different techniques and count in both rows; confirm whether numerators are participants or procedures; and correct or annotate the table if its printed counting rule is incomplete or a value is erroneous.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable reporting defects can matter when source values, definitions, denominators, or planned design features are later transcribed into evidence tables, systematic reviews, meta-analyses, guidelines, or related publications. These are bounded possibilities only: this review does not assert that any candidate propagated, caused harm, altered a result, or changed the paper’s conclusions.

## Limitations and Missing Definitions

See the durable [limitations record](<review_1_5_1/limitations.md>). The package lacks participant-level imaging and procedure records, the endpoint-adjudication implementation rule, and the sample-size calculation trace/attrition convention. These omissions prevent final adjudication and exact reconstruction beyond the printed relationships, but do not leave a direct-source, relationship, recheck, or statistical-pass coverage gap. DOC-003 administrative pp. 16-22 were image-only; rendered-page inspection completed their source-page review although derivative OCR was unreliable.

## Human Adjudication Checklist

1. Confirm the stable candidate ID and every cited direct-source page.
2. Separate the printed observation from any inferred explanation.
3. Obtain the missing source records named in the applicable evidence card.
4. Determine the applicable endpoint, attrition, or counting rule.
5. Complete the five blank human-adjudication fields in each card.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

All five direct-source PDFs and all 92 reused assets were hashed before review. The audit recorded unchanged revalidation. The canonical review artifacts, including maps, relationship inventories, checker outputs, recheck, audit, limitations, and coverage manifest, are retained below `review_1_5_1/`.

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_evidence_mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_protocol_1 | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_protocol_2 | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_admin_sap | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_evidence_mapping | root/support_results_supp | gpt-5.6-terra | medium | FRESH_SPAWN |
| mapping_consolidation | root/mapping_consolidator | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_checks | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_checks | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN |

The authoritative primary-artifact paths are recorded in the [agent execution manifest](<review_1_5_1/agent_execution_manifest.md>).

### Performance

- **Target basis:** Five supplied PDFs comprise 119 pages, including a 9-page main article and 110 support pages; reusable page-level text covers 24 pages while 95 support pages require fresh native/layout mapping, with protocol, administrative appendix, results supplement, and SAP relationships requiring cross-source review. Calibrated above the 102-unit/81-fresh reference because this package has more total and fresh units plus three newly mapped support documents.
- **Total source units:** 119
- **Fresh-source units:** 95
- **Target elapsed minutes:** 45-70
- **Started UTC:** 2026-09-03T03:49:55Z
- **Finished UTC:** 2026-09-03T04:46:29Z
- **Observed elapsed minutes:** 56.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token-Usage and Cost Metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|
| gpt-5.6-sol | 0 known; complete count unavailable | 0.000000 known; complete estimate __ |
| gpt-5.6-terra | 0 known; complete count unavailable | 0.000000 known; complete estimate __ |

The runtime exposed no authoritative response-level token counts for the coordinator or specialists, so the ledger correctly records one `UNAVAILABLE` entry per manifested agent and does not estimate usage from text. The [versioned token summary](<review_1_5_1/token_usage_summary.md>) provides per-agent detail. Cached input and cache-write are input subsets, and reasoning tokens are output subsets; none are added again to total tokens. Every shown amount is a token-only API-equivalent estimate under the 2026-08-18 pricing snapshot, not an invoice; the complete estimate is unavailable.
