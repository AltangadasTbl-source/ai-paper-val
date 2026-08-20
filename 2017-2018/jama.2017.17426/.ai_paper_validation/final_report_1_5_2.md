# Quantitative Quality-Control Consistency Review: AMPLE Paper Package

## Pending Human Adjudication

This supplied-source review identifies reporting-consistency candidates for human review. Every candidate below is **Pending Human Adjudication**. It is not a correction, validity determination, or conclusion-level assessment.

## Executive Quality-Control Summary

Complete fresh processing of three supplied PDFs (81 of 81 PDF-page units) identified five distinct source-grounded quantitative reporting-consistency candidates: one count/percentage mismatch, one within-document sample-size arithmetic mismatch, one cross-document sample-size-input mismatch, one ITT population-label mismatch, and one unlabeled contrast-direction mismatch. No candidate was selected by a cap, queue, ranking, or significance threshold. No candidate was registered from a display-zero P value.

The review is a quantitative reporting quality-control exercise. Small preventable numeric or labeling defects can matter if later evidence extractors copy them; the supplied package does not establish downstream propagation, conclusion change, or harm.

## Package and Fresh-Processing Provenance

The direct supplied sources were [jama_thomas_2017_oi_170130.pdf](<../jama_thomas_2017_oi_170130.pdf#page=1>), [joi170130supp1_prod.pdf](<../joi170130supp1_prod.pdf#page=1>), and [joi170130supp2_prod.pdf](<../joi170130supp2_prod.pdf#page=1>). Their fresh source-first inventory, native/layout extraction, selected rendering, and targeted CPU-only OCR decision are documented in [the evidence-asset inventory](<review_1_5_2/evidence_asset_inventory.md>). Existing audit derivatives were not evidence inputs or discovery boundaries.

All three direct PDFs were processed with fresh native and layout text. Result-relevant pages were rendered; only the graphical SAP placeholder flowchart on DOC-002 PDF p. 66 required targeted OCR, and its rendered page remains the authority.

## Scope, Complete Coverage, and Exclusions

The supplied-source scope covered numeric, denominator/proportion/total, inferential-statistical, cross-document, measure-label/scale, and rate/count relationships. It did not audit raw data, analysis code, clinical validity, study design generally, novelty, misconduct, or paper validity.

| Source | Units | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---|
| DOC-001 main article | 10 | 10 | 10 | COMPLETE |
| DOC-002 protocol/SAP supplement | 69 | 69 | 69 | COMPLETE |
| DOC-003 MI eTable supplement | 2 | 2 | 2 | COMPLETE |
| **Total** | **81** | **81** | **81** | **COMPLETE** |

The complete stage allocation is retained in [coverage_manifest.md](<review_1_5_2/coverage_manifest.md>). Planned material, different populations, definitions, methods, scales, and rounded values were not treated as contradictions unless the supplied source established a concrete inconsistency.

## Quantitative and Statistical Relationship Coverage

The numeric inventory covered **N001-N059 (59 of 59)**. The statistical inventory covered **S001-S051 (51 of 51)**. Numeric and cross-source checking were completed across all assigned relationships. Independent statistical pass 1 and independent statistical pass 2 each completed **51 of 51** relationships; pass 2 also reconsidered C001-C005 and all mechanical recheck facts. No new candidate was appended in pass 2.

The durable review records are [numeric consistency](<review_1_5_2/checkers/numeric_consistency.md>), [cross-source consistency](<review_1_5_2/checkers/cross_source_consistency.md>), [statistical pass 1](<review_1_5_2/checkers/statistical_pass_1.md>), [statistical pass 2](<review_1_5_2/checkers/statistical_pass_2.md>), and [mechanical evidence recheck](<review_1_5_2/verification/evidence_recheck.md>).

## Candidate Index

| ID | Candidate | Category | Principal evidence |
|---|---|---|---|
| [C001](#c001--talc-arm-ecog-unknown-percentage-does-not-match-the-count-and-denominator) | Talc-arm ECOG unknown percentage | Denominator, proportion, or total inconsistency | [main PDF p. 4](<../jama_thomas_2017_oi_170130.pdf#page=4>) |
| [C002](#c002--final-protocol-sample-size-addition-does-not-equal-the-printed-total) | Final-protocol sample-size addition | Numeric or arithmetic inconsistency | [supplement 1 PDF p. 37](<../joi170130supp1_prod.pdf#page=37>) |
| [C003](#c003--final-protocol-and-sapmain-article-give-different-sample-size-inputs-for-the-same-target) | Sample-size inputs across documents | Cross-document numeric inconsistency | [supplement 1 PDF p. 37](<../joi170130supp1_prod.pdf#page=37>) |
| [C004](#c004--sap-itt-definition-conflicts-with-the-reported-144-patient-itt-denominator) | SAP versus reported ITT denominator | Analysis-unit or population inconsistency | [supplement 1 PDF p. 62](<../joi170130supp1_prod.pdf#page=62>) |
| [C005](#c005--estimated-difference-contrast-direction-is-unlabeled-and-reverses-between-the-main-and-mi-tables) | Unlabelled estimated-difference direction | Measure, label, or scale inconsistency | [main PDF p. 6](<../jama_thomas_2017_oi_170130.pdf#page=6>) |

## Candidate Evidence Cards

## C001 — Talc-arm ECOG unknown percentage does not match the count and denominator

**Candidate statement:** The talc-arm ECOG Unknown cell prints `5 (17)` although the stated column denominator is 72 and the count implies 7% under the table’s demonstrated whole-percent convention.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_thomas_2017_oi_170130.pdf — PDF p. 4](<../jama_thomas_2017_oi_170130.pdf#page=4>), Table 1, `ECOG score, No. (%)`, talc pleurodesis column.

**Source evidence:** The talc column header is `n = 72`; its ECOG entries are `53 (74)`, `14 (19)`, and Unknown `5 (17)`. The counts total 72.

**Reported-versus-comparator:** Reported Unknown percentage `17%` versus `5/72 × 100 = 6.944...%`, rounding to `7%`.

**Reasoning procedure:** Applied the stated column denominator to the count in a `No. (%)` table and checked the companion cells’ whole-percent rounding.

**Calculation:** `53 + 14 + 5 = 72`; `100 × 5 / 72 = 6.944...`, which rounds to 7, not 17.

**Alternative source-grounded interpretations:** The percentage may contain an extra digit, or the count/denominator may be wrong. No alternative denominator is printed, and the supplied source cannot identify the intended field.

**Mechanical evidence recheck:** The direct PDF location, denominator, all three cells, count total, comparator, and calculation were reproduced. The table-production record and participant-level data are not supplied.

**Quality-control relevance:** This is a printed baseline `No. (%)` identity. Its values do not reconcile under the demonstrated table rule.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an incorrect baseline ECOG Unknown percentage into a study-characteristics table or narrative evidence summary.

**Human verification steps:** Check the baseline dataset or table-production record for the talc-arm Unknown numerator, denominator, and intended percentage.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Final-protocol sample-size addition does not equal the printed total

**Candidate statement:** The final protocol states 62 patients per group, an additional 24 for loss to follow-up, and total recruitment of 146; the stated whole-person components add to 148.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [joi170130supp1_prod.pdf — PDF p. 37](<../joi170130supp1_prod.pdf#page=37>), AMPLE protocol Version 4, section 5, `SAMPLE SIZE CALCULATIONS`.

**Source evidence:** The page prints 62 patients in each group, a 20% loss-to-follow-up rate, an additional 24 patients, and a total target of 146.

**Reported-versus-comparator:** Reported target `146` versus `62 + 62 + 24 = 148`.

**Reasoning procedure:** Applied direct addition of the printed whole-person base groups and printed allowance; separately checked the printed percentage statement without assuming a particular attrition convention.

**Calculation:** `62 × 2 = 124`; `124 + 24 = 148`; `146 − 124 = 22`; `20% × 124 = 24.8`.

**Alternative source-grounded interpretations:** One displayed component may represent a different calculation stage. The power output, attrition-inflation convention, rounding decision, and production record are not supplied.

**Mechanical evidence recheck:** The same-paragraph quantities, version/date, comparator, and arithmetic were directly reproduced. Neither the stated 24 nor ordinary rounding of 24.8 yields 146 from base 124.

**Quality-control relevance:** Sample-size rationale and recruitment targets are reported planning numbers; the printed components do not reconcile under direct whole-person addition.

**Potential downstream evidence impact:** If confirmed, a reviewer or data extractor could copy an internally inconsistent recruitment target or attrition allowance into study-design evidence tables.

**Human verification steps:** Retrieve the approved sample-size calculation and its attrition and rounding rule; determine which printed component was intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Final protocol and SAP/main article give different sample-size inputs for the same target

**Candidate statement:** The final protocol and the SAP/main article present different base-size and attrition inputs while each presents a target of 146, without a supplied record explicitly linking the calculations.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [joi170130supp1_prod.pdf — PDF p. 37](<../joi170130supp1_prod.pdf#page=37>), final protocol; [joi170130supp1_prod.pdf — PDF p. 62](<../joi170130supp1_prod.pdf#page=62>), SAP section 3; [jama_thomas_2017_oi_170130.pdf — PDF p. 3](<../jama_thomas_2017_oi_170130.pdf#page=3>), Methods.

**Source evidence:** Protocol p. 37 gives 62 per group, 20%/24 additional participants, target 146. SAP p. 62 and main p. 3 give 65 per group, 12% loss, 73 per group, target 146.

**Reported-versus-comparator:** `62` per group and `20%`/24 versus `65` per group and `12%`, with the same stated total target.

**Reasoning procedure:** Matched the named trial and target, compared the printed planning inputs, and checked the supplied version-history context without inferring supersession.

**Calculation:** Protocol base `62 × 2 = 124`; SAP/main target `73 × 2 = 146`; SAP/main inflation `130 × 1.12 = 145.6`, compatible with 146 after whole-person rounding.

**Alternative source-grounded interpretations:** The later SAP/main basis may deliberately supersede the protocol basis. The change summary records addition of a sample-size section on [supplement 1 PDF p. 51](<../joi170130supp1_prod.pdf#page=51>), but no supplied amendment explicitly identifies the operative replacement.

**Mechanical evidence recheck:** Protocol, SAP, and main values, dates/versions, shared target, and arithmetic were reproduced. The missing operative amendment, approved calculation record, and recruitment-governing parameter set prevent resolution.

**Quality-control relevance:** Cross-document planning parameters should agree or be linked by a supplied revision trail that identifies which calculation governed recruitment.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy conflicting planned sample-size or attrition inputs into trial-registry, design, or risk-of-bias context summaries.

**Human verification steps:** Check approved amendments and trial-master records for a dated replacement and clarify which parameter set governed recruitment.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — SAP ITT definition conflicts with the reported 144-patient ITT denominator

**Candidate statement:** The SAP defines ITT as all randomized subjects, including those not receiving assigned treatment, while the main report excludes two randomized pre-intervention withdrawals from all analyses and calls 144 participants ITT.

**Category:** Analysis-unit or population inconsistency

**Exact source locations:** [joi170130supp1_prod.pdf — PDF p. 62](<../joi170130supp1_prod.pdf#page=62>) and [PDF p. 63](<../joi170130supp1_prod.pdf#page=63>), SAP section 4.2; [jama_thomas_2017_oi_170130.pdf — PDF p. 3](<../jama_thomas_2017_oi_170130.pdf#page=3>), flow; [PDF p. 4](<../jama_thomas_2017_oi_170130.pdf#page=4>), analysis population; [PDF p. 6](<../jama_thomas_2017_oi_170130.pdf#page=6>), Table 2.

**Source evidence:** The SAP includes every randomized subject and those not receiving assigned treatment. The main article reports 74 + 72 = 146 randomized, one pre-treatment withdrawal per arm, exclusions from all analyses, and Table 2 ITT denominators 73 + 71 = 144.

**Reported-versus-comparator:** Reported ITT `73 + 71 = 144` versus SAP-defined ITT of all `74 + 72 = 146` randomized participants.

**Reasoning procedure:** Applied the printed SAP population definition to printed randomization and exclusion counts, preserving the source’s own treatment-receipt clause.

**Calculation:** `74 + 72 = 146`; `73 + 71 = 144`; `146 − 144 = 2`, matching the one excluded pre-intervention withdrawal in each arm.

**Alternative source-grounded interpretations:** An unstated modified-ITT convention, later amendment, or withdrawal-related data-use restriction may explain the exclusions. No supplied page names such a rule.

**Mechanical evidence recheck:** SAP definition, randomized totals, flow exclusions, Results text, ITT label, and Table 2 denominators were directly reproduced. Missing are an operative amendment, modified-ITT definition, data-use rule, and analysis-program population flag.

**Quality-control relevance:** The concrete analysis-population definition determines the denominator and label attached to reported results.

**Potential downstream evidence impact:** If confirmed, a systematic-review data extractor could copy an ITT population size or analysis-set label that is inconsistent with the supplied SAP definition.

**Human verification steps:** Locate the operative amendment or withdrawal rule, if any, and confirm the exact analysis-population definition and effective date.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Estimated-difference contrast direction is unlabeled and reverses between the main and MI tables

**Candidate statement:** The main Table 2 and MI eTable list IPC before talc and label signed estimates `Estimated Difference (95% CI)` without a subtraction order; their displayed signs imply opposite directions.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_thomas_2017_oi_170130.pdf — PDF p. 6](<../jama_thomas_2017_oi_170130.pdf#page=6>), Table 2; [joi170130supp2_prod.pdf — PDF p. 2](<../joi170130supp2_prod.pdf#page=2>), multiple-imputation eTable.

**Source evidence:** Main baseline is IPC 50.0 versus talc 52.2 with `+2.27`; day 1 is 64.5 versus 69.7 with `+5.25`. MI baseline is 49.8 versus 51.9 with `−2.06`; day 1 is 65.5 versus 71.7 with `−6.19`. Neither footnote names the subtraction order.

**Reported-versus-comparator:** Main signs imply talc minus IPC; MI signs imply IPC minus talc, despite the same displayed group order and unlabelled signed-estimate heading.

**Reasoning procedure:** Reconstructed sign direction from multiple displayed arm estimates, retaining allowance for rounding and not requiring equality between rounded means and model-based contrasts.

**Calculation:** Main: `52.2 − 50.0 = +2.2` and `69.7 − 64.5 = +5.2`, compatible with `+2.27` and `+5.25`. MI: `49.8 − 51.9 = −2.1` and `65.5 − 71.7 = −6.2`, compatible with `−2.06` and `−6.19`.

**Alternative source-grounded interpretations:** Opposite parameterizations may have been intentional and MI can change displayed means. These explain magnitude differences but neither supplied footnote labels the reconstructed contrast directions.

**Mechanical evidence recheck:** Both headers, group order, values, signed estimates, and footnotes were directly reproduced. Exact contrast coding, unrounded estimates, model coefficients, and table-production specifications are not supplied.

**Quality-control relevance:** A signed effect requires a named reference group or subtraction order so that its direction can be interpreted consistently across related tables.

**Potential downstream evidence impact:** If confirmed, a meta-analysis or evidence table could copy a signed mean difference with its direction reversed or ambiguous.

**Human verification steps:** Check the model specifications and table-production records for each reference group and state the subtraction order explicitly.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, it could affect a copied baseline percentage, planned sample-size parameter, analysis-population label, or signed effect direction in a systematic review, meta-analysis, guideline evidence table, or other extraction product. These are bounded possibilities only; this review makes no claim that copying, propagation, conclusion change, or harm occurred.

## Limitations and Missing Definitions

The supplied package has no participant-level data, analysis code, table-production records, operative amendment explicitly reconciling the sample-size calculations, or modified-ITT/withdrawal data-use rule. Exact rank-test, mixed-model, Cox, power-calculation, and multiple-imputation construction details are also absent. The graphical DOC-002 p. 66 flowchart required visual review because native/layout text was unusable. Diagnostic approximations were not used as replacements for reported analyses. See [limitations.md](<review_1_5_2/limitations.md>) for the complete list.

## Human Adjudication Checklist

For each C ID, a human reviewer should confirm the cited direct PDF locations, retrieve any table-production or approved protocol/SAP record needed to resolve missing definitions, record a decision only in the five blank fields of that candidate card, and preserve the original stable ID. This report does not supply an adjudication, correction, severity rating, validity determination, or acceptance/exclusion decision.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Fresh direct-source checksums recorded before review:

| Source | SHA-256 |
|---|---|
| `jama_thomas_2017_oi_170130.pdf` | `2638f5947ee9d89211beb4daa767e962939fda0df25a93e3546c2d442751c239` |
| `joi170130supp1_prod.pdf` | `d269a035b2f2542a9563005f41c6c7bf4f7b2a877bcd0c87def494c82bc57ee7` |
| `joi170130supp2_prod.pdf` | `890ac8383d825d992466a46e8edf0a1e8f5c776733742d5aab2023ab345e904c` |

The before-review hash artifact is [source_hashes_before.sha256](<review_1_5_2/source_hashes_before.sha256>). Post-assembly SHA-256 recomputation matched all three pre-review values exactly; the duplicate after-review record is [source_hashes_after.sha256](<review_1_5_2/source_hashes_after.sha256>).

### Agent execution

| Stage | Agent ID | Model | Effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh source preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main quantitative mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | main_quantitative_evidence.md |
| support quantitative mapping | root/support_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | support_quantitative_evidence.md |
| numeric checks | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | numeric_consistency.md |
| statistical pass 1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | statistical_pass_1.md |
| cross-source checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | cross_source_consistency.md |
| evidence recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | evidence_recheck.md |
| statistical pass 2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | statistical_pass_2.md |
| evidence quality | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | evidence_quality_audit.md |
| report generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation_summary.md |

The execution manifest is [agent_execution_manifest.md](<review_1_5_2/agent_execution_manifest.md>). The two statistical passes used distinct fresh `gpt-5.6-terra`/high agents.

### Performance

- **Target basis:** Three direct PDF sources totaling 81 pages, all requiring fresh native and layout extraction; one 69-page technical supplement creates substantial quantitative mapping scope, while no Office/workbook conversion is required; targeted rendering/OCR and five prescribed review/verification stages are included.
- **Total source units:** 81
- **Fresh-source units:** 81
- **Target elapsed minutes:** 30-50
- **Started UTC:** 2026-08-20T16:51:45Z
- **Finished UTC:** 2026-08-20T17:24:34Z
- **Observed elapsed minutes:** 32.8
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and token-only API-equivalent cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Input tokens | Output tokens | Total tokens | Token-only API-equivalent cost (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 | 0 | 0 | 0 | 0.000000 known; complete estimate __ |
| gpt-5.6-terra | 8 | 0 | 0 | 0 | 0.000000 known; complete estimate __ |

The versioned [token_usage_summary.md](<review_1_5_2/token_usage_summary.md>) contains per-agent detail. The runtime exposed no authoritative response-level token counts for the coordinator or specialists, so every manifested agent has an `UNAVAILABLE` ledger row; zero is only the known subtotal, not a claim of zero actual usage. Cached input/cache-write values are input subsets and reasoning is an output subset; none is added again to total tokens. Amounts are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not invoices.
