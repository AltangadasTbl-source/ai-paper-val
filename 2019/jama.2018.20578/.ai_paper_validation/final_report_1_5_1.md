# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

> ## Pending Human Adjudication
>
> All seven candidate consistency issues below are **Pending Human Adjudication**. They are neutral quality-control observations, not automated conclusions about the paper or paper-level impact.

## Executive Quality-Control Summary

This complete review identified **7 stable candidate consistency issues**: C001 through C007. They concern a unit/scale label, two separately reported percentage-point differences, a displayed model-selection rule, an estimate/standard-error/test-statistic vector, an endpoint-membership/count comparison, and two baseline percentages. Small preventable reporting defects can matter for downstream evidence extraction; this review does not claim that any candidate propagated, changed a conclusion, or caused serious harm.

## Package and Reused-Evidence Provenance

The direct-source package contains three PDFs and 46 PDF pages: DOC-001, the STOP-PD II psychotic-depression randomized trial; DOC-002, an aspirin primary-prevention meta-analysis protocol supplement; and DOC-003, that aspirin meta-analysis results supplement. The direct PDFs remained authoritative. Reused source-linked maps, native/layout text, rendered pages, and OCR were locators and transcription aids only.

The supplied package has a provenance mismatch: DOC-001 is STOP-PD II, whereas DOC-002 and DOC-003 support a different aspirin meta-analysis. This is recorded as a package limitation, not as a quantitative candidate. No result from DOC-001 was compared as though it were a repeated result from DOC-002 or DOC-003.

Reusable-asset inventory: 74 assets (56 usable, 5 partial, 2 stale, 11 duplicate, 0 unreadable). Partial reading order/layout derivatives were supplemented by source-linked maps and direct-PDF confirmation for every candidate.

## Scope, Complete Coverage, and Exclusions

| Source | Units | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 — `jama_flint_2019_oi_190079.pdf` | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 — `joi180151supp1_prod.pdf` | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-003 — `joi180151supp2_prod.pdf` | 29 | 29 | 0 | 29 | COMPLETE |
| **Total** | **46** | **46** | **0** | **46** | **COMPLETE** |

The review covered result-relevant numeric, denominator, statistical, cross-document, measure/label/scale, and rate/count relationships. It did not perform a broad clinical, methodological, misconduct, raw-data, or external-literature audit. No candidate was created for a coherent display-zero P value; no reviewed relationship had such a display-zero record.

## Quantitative and Statistical Relationship Coverage

The numeric inventory covers **N001–N068**. The statistical inventory covers **S001–S021**. Statistical pass 1 completed every S relationship; independent statistical pass 2 completed every S relationship after cross-lane review and mechanical recheck. Both passes were performed by distinct fresh `gpt-5.6-terra` agents at high reasoning effort. The relationship records include compatible nonfindings and missing-definition limits as well as the candidate-bearing relationships.

## Candidate Index

| ID | Candidate consistency issue | Category |
|---|---|---|
| C001 | HbA1c daily-rate unit conflicts with the table scale | Measure, label, or scale inconsistency |
| C002 | Total-cholesterol percentage-point difference does not reconcile with printed counts | Denominator, proportion, or total inconsistency |
| C003 | LDL percentage-point difference does not reconcile with printed counts | Denominator, proportion, or total inconsistency |
| C004 | Incident-cancer model label does not follow the printed DIC/I2 rule | Statistical reporting inconsistency |
| C005 | Egger estimate and standard error do not reproduce the printed t statistic at displayed precision | Statistical reporting inconsistency |
| C006 | ASCEND is excluded for all stroke but included in the total-stroke forest plot | Cross-document numeric inconsistency |
| C007 | Hyperlipidemia percentages reproduce only with the opposite arm denominators | Denominator, proportion, or total inconsistency |

## Candidate Evidence Cards

## C001 — HbA1c daily-rate unit conflicts with the table scale

**Candidate statement:** The repeated HbA1c daily-rate coefficient is labelled `mg/dL`, while Table 4 labels HbA1c as `%`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 abstract — PDF p. 1](<../jama_flint_2019_oi_190079.pdf#page=1>); [DOC-001 Results — PDF p. 7](<../jama_flint_2019_oi_190079.pdf#page=7>); [DOC-001 Table 4 — PDF p. 8](<../jama_flint_2019_oi_190079.pdf#page=8>).

**Source evidence:** PDF pp. 1 and 7 print `-0.0002 mg/dL` (95% CI, `-0.0021 to 0.0016`); Table 4 labels the analyte `HbA1c, %`.

**Reported-versus-comparator:** Reported unit: `mg/dL`; comparator named-analyte scale: `%`.

**Reasoning procedure:** Compare the unit attached to the repeated coefficient with the scale printed for the same named analyte.

**Calculation:** Categorical comparison: `%` and `mg/dL` are different units; no rounding operation converts one to the other.

**Alternative source-grounded interpretations:** The text unit may be a carryover label from adjacent metabolic analytes, or an unreported response transformation may exist.

**Mechanical evidence recheck:** All three locations and the repeated estimate/interval were found. The source does not provide the modeled response scale, transformation, or a percentage-points-per-day statement. Direct observations are the two text labels and Table 4 scale; the explanations are inferred.

**Quality-control relevance:** The same measured outcome has inconsistent scale information across report locations.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the coefficient with the wrong HbA1c unit or scale.

**Human verification steps:** Confirm the modeled HbA1c response scale, unit per day, and any transformation in the analysis output or approved source.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Total-cholesterol percentage-point difference does not reconcile with printed counts

**Candidate statement:** The Total cholesterol row’s printed 4.3 percentage-point difference does not reconcile with its displayed arm counts, denominators, or percentages.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 Table 5 — PDF p. 9](<../jama_flint_2019_oi_190079.pdf#page=9>), Total cholesterol row.

**Source evidence:** The row prints olanzapine `9 (14.1)`, placebo `6 (9.7)`, and an absolute unadjusted difference of `4.3` percent; headers print `n = 64` and `n = 62`.

**Reported-versus-comparator:** Reported difference: `4.3`; comparator differences: `9/64 − 6/62` and `14.1 − 9.7` percentage points.

**Reasoning procedure:** Reproduce the unadjusted arm-proportion difference from the printed counts/denominators and independently subtract the printed percentages.

**Calculation:** `(9/64 − 6/62) × 100 = 4.385080...`, which displays as `4.4`; `14.1 − 9.7 = 4.4`. `4.385080...` is outside the ordinary one-decimal interval for `4.3`.

**Alternative source-grounded interpretations:** An unstated evaluable denominator, weighting method, missing-data convention, or calculation output may have produced `4.3`.

**Mechanical evidence recheck:** The cited row, arm denominators, counts, percentages, and point difference were found. Those inputs reproduce 4.4; measure-specific denominators and calculation output are absent. Printed facts are direct observations; any production explanation is inferred.

**Quality-control relevance:** A displayed unadjusted difference is not reproducible from the row’s own printed proportions.

**Potential downstream evidence impact:** If confirmed, a systematic reviewer or data extractor could copy an incorrect percentage-point effect for this outcome row.

**Human verification steps:** Identify the exact row-specific denominators and unadjusted calculation that generated `4.3`.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — LDL percentage-point difference does not reconcile with printed counts

**Candidate statement:** The distinct LDL row’s printed 4.3 percentage-point difference does not reconcile with its displayed arm counts, denominators, or percentages.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 Table 5 — PDF p. 9](<../jama_flint_2019_oi_190079.pdf#page=9>), LDL row.

**Source evidence:** The LDL row independently prints olanzapine `9 (14.1)`, placebo `6 (9.7)`, and an absolute unadjusted difference of `4.3` percent; headers print `n = 64` and `n = 62`.

**Reported-versus-comparator:** Reported difference: `4.3`; comparator differences: `9/64 − 6/62` and `14.1 − 9.7` percentage points.

**Reasoning procedure:** Reproduce the unadjusted arm-proportion difference and subtract the displayed percentages for this distinct labelled outcome.

**Calculation:** `(9/64 − 6/62) × 100 = 4.385080...`, displaying as `4.4`; `14.1 − 9.7 = 4.4`, not `4.3`.

**Alternative source-grounded interpretations:** An unstated LDL-specific evaluable denominator or calculation convention may exist; a shared production mechanism with a neighboring row is possible but not observed.

**Mechanical evidence recheck:** The distinct LDL row and all cited printed values were found. The reproduced proportion and percentage differences display as 4.4. Missing inputs are row-specific denominators, weighting, and calculation output; explanations beyond the printed mismatch are inferred.

**Quality-control relevance:** This separately extractable outcome row has a nonreproducible displayed difference.

**Potential downstream evidence impact:** If confirmed, an evidence product could extract the wrong LDL percentage-point effect.

**Human verification steps:** Confirm the LDL row’s intended denominator and unadjusted calculation convention.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Incident-cancer model label does not follow the printed DIC/I2 rule

**Candidate statement:** The all-patients incident-cancer row displays `random` although the printed DIC/I2 rule and displayed inputs select otherwise.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 eMethods 2 — PDF p. 4](<../joi180151supp2_prod.pdf#page=4>); [DOC-003 eMethods 3 — PDF p. 5](<../joi180151supp2_prod.pdf#page=5>), all-patients incident-cancer row.

**Source evidence:** The rule favors random effects within 3 DIC units when fixed-effect `I2 >25%`. The row prints fixed DIC `27.06`, random DIC `27.93`, `I2=25%`, and model `random`.

**Reported-versus-comparator:** Reported model: `random`; comparator: the model selected by the displayed strict threshold and DIC values.

**Reasoning procedure:** Apply the printed decision rule only to the displayed row values.

**Calculation:** `27.93 − 27.06 = 0.87` (within 3). Displayed `25 > 25` is false, and fixed has lower displayed DIC.

**Alternative source-grounded interpretations:** Unrounded I2 may exceed 25%, or an inclusive threshold or other unprinted rule may have been used.

**Mechanical evidence recheck:** Rule and row values were found on the cited pages. The strict displayed comparison and DIC difference reproduce the mismatch. The unrounded I2 and exact threshold/rounding convention are missing; any explanation is inferred.

**Quality-control relevance:** The selected-model label is not reproducible from the report’s displayed decision rule at printed precision.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy a model-selection label or associated result without its correct documented selection basis.

**Human verification steps:** Obtain the unrounded fixed-effect I2 and the exact internal threshold and rounding convention for this row.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Egger estimate and standard error do not reproduce the printed t statistic at displayed precision

**Candidate statement:** Conditional on the adjacent estimate and standard error being the inputs to the displayed test, their ordinary two-decimal display intervals cannot reproduce `t=-0.59`.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 eFigure 3 — PDF p. 21](<../joi180151supp2_prod.pdf#page=21>).

**Source evidence:** The figure prints Egger estimate `-0.47`, standard error `0.77`, `t=-0.59`, and `P=.57`.

**Reported-versus-comparator:** Reported t statistic: `-0.59`; comparator: estimate divided by standard error under the stated conditional identity.

**Reasoning procedure:** Evaluate `t = estimate / SE` only if the displayed estimate and SE are the test inputs; use nearest-hundredth intervals rather than a reconstructed P value.

**Calculation:** `-0.47/0.77 = -0.6104`, displaying as `-0.61`. Nearest-hundredth intervals permit an absolute ratio about `0.600` to `<0.621`; a displayed `0.59` requires `0.585` to `<0.595`.

**Alternative source-grounded interpretations:** The t statistic may refer to a distinct unreported parameter, variance estimate, or software-output field; ordinary rounding and truncation do not bridge the displayed ratio.

**Mechanical evidence recheck:** The complete vector was found. The interval comparison was reproduced and pass 2 resolved pass 1’s contrary diagnostic. Missing inputs are the exact Egger test definition, parameter mapping, unrounded inputs, degrees of freedom, and sidedness. No P value was reconstructed.

**Quality-control relevance:** A commonly extracted estimate/SE/test-statistic vector is conditionally inconsistent at its displayed precision.

**Potential downstream evidence impact:** If confirmed, a small-study-bias assessment could be extracted with an inconsistent estimate, SE, or test statistic.

**Human verification steps:** Confirm the parameter, standard error, unrounded inputs, degrees of freedom, and calculation used for the printed t statistic.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — ASCEND is excluded for all stroke but included in the total-stroke forest plot

**Candidate statement:** The supplied all-stroke exclusion for ASCEND conflicts with its inclusion in the `Total stroke` frequentist forest plot without a stated distinct endpoint convention.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-002 protocol change — PDF p. 7](<../joi180151supp1_prod.pdf#page=7>); [DOC-003 eTable 1 — PDF p. 9](<../joi180151supp2_prod.pdf#page=9>); [DOC-003 eTable 4 — PDF p. 16](<../joi180151supp2_prod.pdf#page=16>); [DOC-003 eFigure 4 — PDF p. 24](<../joi180151supp2_prod.pdf#page=24>).

**Source evidence:** eTable 1 says ASCEND is not included for all stroke because it reports only ischaemic stroke. eTable 4 gives 12 studies and `73,883/72,317`; the Total stroke forest plot gives 13 rows and `81,623/80,057`, including ASCEND `240/7,740` versus `263/7,740`.

**Reported-versus-comparator:** Reported forest endpoint membership/totals versus the eTable all-stroke exclusion and 12-study totals.

**Reasoning procedure:** Keep Bayesian HR/CrI and frequentist RR/CI analyses distinct; compare only source-defined endpoint membership, study count, and participant-total identity.

**Calculation:** `81,623 − 73,883 = 7,740` and `80,057 − 72,317 = 7,740`, exactly the displayed ASCEND denominator in each arm. The same ASCEND vector appears in the ischaemic-stroke panel.

**Alternative source-grounded interpretations:** The frequentist analysis may intentionally use ischaemic stroke as a total-stroke proxy under an unstated endpoint convention distinct from the Bayesian table.

**Mechanical evidence recheck:** The exclusion cell, table count/totals, forest labels/totals, ASCEND row, and duplicate vector were found. Required missing inputs are the frequentist endpoint convention, model-specific ASCEND inclusion rule, and extraction record. Intentional proxy use is inferred, not observed.

**Quality-control relevance:** A matched endpoint-membership and count identity is not explained consistently across supplied supplement displays.

**Potential downstream evidence impact:** If confirmed, a meta-analysis or data extractor could copy the wrong study count, denominators, endpoint membership, or associated total-stroke result.

**Human verification steps:** Confirm whether ASCEND was intentionally included in the frequentist Total stroke panel and document the endpoint and inclusion rule.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Hyperlipidemia percentages reproduce only with the opposite arm denominators

**Candidate statement:** The Hyperlipidemia row’s two printed percentages reproduce only when each count is divided by the opposite arm’s header denominator.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 Table 1 — PDF p. 5](<../jama_flint_2019_oi_190079.pdf#page=5>), Hyperlipidemia row and arm headers.

**Source evidence:** The olanzapine header is `n=64` with `18 (29.0)`; the placebo header is `n=62` with `19 (29.7)`.

**Reported-versus-comparator:** Reported percentages: `29.0%` and `29.7%`; comparator own-arm percentages: `18/64` and `19/62`.

**Reasoning procedure:** Calculate each within-arm percentage using its printed numerator and own-arm header, then check whether the displayed percentages correspond to another stated denominator.

**Calculation:** Own-arm values are `18/64=28.1%` and `19/62=30.6%`. Opposite-arm values are `18/62=29.0%` and `19/64=29.7%`, exactly matching the display.

**Alternative source-grounded interpretations:** Unstated evaluable denominators, missing-status handling, a denominator reversal, or transposed values could explain the display; no row-specific denominator is stated.

**Mechanical evidence recheck:** Both headers and row entries were found. All four calculations were reproduced. Missing inputs are Hyperlipidemia-specific denominators, missing-status counts, and the table-production record. Production mechanisms are inferred.

**Quality-control relevance:** Within-arm baseline percentages are not reproducible from the table’s own arm headers.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy incorrect baseline Hyperlipidemia percentages or counts.

**Human verification steps:** Verify the intended arm-specific denominators and whether the percentages should be recomputed from `18/64` and `19/62`.

**Status:** Pending Human Adjudication

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

The candidates are framed for quantitative reporting quality control. If a candidate is confirmed, a later evidence product could copy the specified unit, difference, model label, statistical vector, endpoint membership, count, or percentage. The supplied package does not establish that any such copying occurred, that conclusions changed, or that harm resulted.

## Limitations and Missing Definitions

- The package combines DOC-001 STOP-PD II material with DOC-002/DOC-003 aspirin meta-analysis supplements; this provenance mismatch limits package-level study linkage but is not itself a quantitative candidate.
- The exact HbA1c modeled response scale/transformation, Table 5 row-specific denominators/calculation outputs, unrounded I2 and selection convention, Egger test definition/unrounded inputs/df/sidedness, frequentist ASCEND endpoint convention, and Hyperlipidemia row denominators are not supplied.
- DOC-001 p. 8 native-text reading order and DOC-003 visual-layout text are partial derivatives, though direct-PDF inspection and usable source-linked maps closed scientific coverage.
- No individual-participant data, analysis dataset/code, author correspondence, or external evidence was available or used.

## Human Adjudication Checklist

1. Confirm every cited printed value against the linked source PDF page.
2. Obtain the missing source definitions or analysis outputs identified in the relevant card.
3. Determine whether each comparison rule applies to the intended population, endpoint, model, and precision convention.
4. Complete the five blank human-adjudication fields in each card.
5. Record any correction or follow-up in a human-controlled record; retain stable IDs.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Direct-source hashes were captured before review and are retained in [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>). The direct-source SHA-256 values are DOC-001 `bc0a0760a27cbb664dd094b4ee12659acb000baf7c1207930f2558cb39affa45`, DOC-002 `d47557e5447470a6d517fe82e52441b897d764ab96736d65d0e94ca564ce7e58`, and DOC-003 `971a6088660ab2c02bbe5e73540d0c3231c779ca551a77a561295738500fb8a0`. The before-review reused-asset hash record covers 74 assets at [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>). No source or reused artifact was modified.

Canonical review artifacts: [source inventory](<review_1_5_1/source_inventory.md>), [source coverage](<review_1_5_1/source_coverage.md>), [coverage manifest](<review_1_5_1/coverage_manifest.md>), [candidate ledger](<review_1_5_1/candidate_ledger.md>), [mechanical evidence recheck](<review_1_5_1/verification/evidence_recheck.md>), [quality audit](<review_1_5_1/quality/evidence_quality_audit.md>), and [limitations](<review_1_5_1/limitations.md>).

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_checks | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_checks | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_quality | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN |

### Performance

- **Target basis:** Three supplied PDFs contain 46 total pages, all covered by usable source-linked reusable maps or text/render/OCR aids, leaving 0 fresh-required source units. The package still contains mixed article/supplement tables, forest plots, cross-document matches, and two mandatory statistical passes. The 25-40 minute target is bounded below the 102-page/81-fresh-page reference while retaining full relationship reconstruction and evidence rechecking.
- **Total source units:** 46
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-18T22:11:04Z
- **Finished UTC:** 2026-08-18T22:48:31Z
- **Observed elapsed minutes:** 37.45
- **Target status:** MET_TARGET
- **Exceedance causes:** None

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

Authoritative response-level runtime/API usage counts were not exposed for the coordinator or specialists, so every manifested agent has an `UNAVAILABLE` record and the package total remains explicitly incomplete; the zeros above are known counted subtotals, not estimates of actual use. Cached input and cache-write counts are input subsets; reasoning tokens are an output subset and are not added again to total tokens. Any amount is a token-only API-equivalent estimate under the dated price snapshot, not an invoice. Per-agent detail is retained in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>).
