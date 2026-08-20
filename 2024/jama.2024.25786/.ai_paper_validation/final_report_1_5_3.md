# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.5.3

## Pending Human Adjudication

Every observation in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a conclusion about the paper, its authors, or clinical validity. Small preventable reporting defects can matter for downstream evidence extraction if confirmed; this report does not claim that any defect propagated, changed a conclusion, or caused harm.

## Executive Quality-Control Summary

Complete source and relationship coverage produced **8** stable candidate consistency observations (C001-C008). They concern two count/percentage identities, one conditionally matched confidence-interval endpoint, two subgroup percentage discrepancies, two participant-flow/denominator presentations, and one malformed count separator. No candidate is based on a display-zero P value. Each observation remains pending human adjudication.

## Package and Reused-Evidence Provenance

The supplied package contains five direct PDFs: the 11-page main article, 103-page protocol/SAP, 26-page results supplement, 3-page collaborator supplement, and 1-page data-sharing supplement. Their 144 PDF-page units were mapped. Reused page-delimited native text covered all 144 units; direct PDFs remained authoritative for candidate confirmation. The reuse inventory recorded 38 artifacts (36 usable and 2 duplicate derivatives); no source, workbook, CSV, DOC, or DOCX evidence was used.

## Scope, Complete Coverage, and Exclusions

| Direct source | Total units | Reusable | Fresh required | Mapped |
|---|---:|---:|---:|---:|
| Main article (DOC-001) | 11 | 11 | 0 | 11 |
| Protocol/SAP (DOC-002) | 103 | 103 | 0 | 103 |
| Results supplement (DOC-003) | 26 | 26 | 0 | 26 |
| Collaborator supplement (DOC-004) | 3 | 3 | 0 | 3 |
| Data-sharing supplement (DOC-005) | 1 | 1 | 0 | 1 |
| **Total** | **144** | **144** | **0** | **144** |

The review prioritized numeric, denominator/proportion/total, statistical, cross-document, measure/label/scale, and rate-versus-count consistency. It excluded broad methodology, clinical, novelty, misconduct, raw-data, and external-literature review. Planning quantities in the protocol/SAP were not treated as observed-result conflicts unless an applicable matched relationship was established.

## Quantitative and Statistical Relationship Coverage

The numeric relationship inventory contains N001-N069; all 69 were checked. The statistical relationship inventory contains S001-S036; both independent statistical passes completed every relationship. Cross-source review covered 29 matched quantitative relationships and 11 protocol/SAP planning or definition relationships. The stable candidate set was not limited by a queue, ranking, cap, or top-N subset.

## Candidate Index

| ID | Candidate statement | Category |
|---|---|---|
| [C001](#c001--liberal-walk-in-transport-percentage-does-not-reconcile-with-4743) | Liberal walk-in transport percentage does not reconcile with 4/743 | Denominator, proportion, or total inconsistency |
| [C002](#c002--liberal-vascular-surgery-percentage-is-nonzero-with-a-printed-zero-numerator) | Liberal vascular-surgery percentage is nonzero with a printed zero numerator | Denominator, proportion, or total inconsistency |
| [C003](#c003--matched-all-patient-adjusted-confidence-interval-upper-limit-differs-between-etables-4-and-7) | Matched adjusted CI upper limit differs between eTables 4 and 7 | Cross-document numeric inconsistency |
| [C004](#c004--ais-less-than-3-subgroup-percentage-conflicts-with-its-count-and-matched-figure-4) | AIS less-than-3 subgroup percentage conflicts with count and Figure 4 | Cross-document numeric inconsistency |
| [C005](#c005--known-lung-disease-subgroup-percentage-conflicts-with-its-count-and-matched-figure-4) | Known-lung-disease subgroup percentage conflicts with count and Figure 4 | Cross-document numeric inconsistency |
| [C006](#c006--postrandomization-exclusion-total-and-group-counts-do-not-reconcile-across-etable-10-and-figure-1) | Postrandomization-exclusion totals and group counts do not reconcile | Cross-document numeric inconsistency |
| [C007](#c007--secondary-exclusion-cells-pair-within-group-denominators-with-cross-group-partition-percentages) | Secondary-exclusion cells pair incompatible denominator concepts | Denominator, proportion, or total inconsistency |
| [C008](#c008--missing-as-event-primary-count-uses-a-doubled-numeratordenominator-separator) | Missing-as-event count uses a doubled separator | Measure, label, or scale inconsistency |

## Candidate Evidence Cards

## C001 — Liberal walk-in transport percentage does not reconcile with 4/743

**Candidate statement:** The liberal-group walk-in transport cell does not reconcile under its printed count/total/percentage format.  
**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Exact source locations:** [Supplement 2, eTable 2, PDF p. 15](<../joi240147supp2_prod_1738701765.29201.pdf#page=15>), liberal oxygen group, walk-in transport row.  
**Source evidence:** The direct PDF prints `4/743 (5.3)` under `no./total no. (%)`.  
**Reported-versus-comparator:** Reported `5.3%` versus the percentage derived from the paired printed numerator and denominator.  
**Reasoning procedure:** Apply `100 × numerator / denominator` and round to the table’s one-decimal precision.  
**Calculation:** `100 × 4 / 743 = 0.538358...%`, which rounds to `0.5%`, not `5.3%`.  
**Alternative source-grounded interpretations:** The count, denominator, or percentage may be mistranscribed; adjacent cells use denominator 743 and no footnote supplies an alternative.  
**Mechanical evidence recheck:** Direct layout extraction and rendered-page inspection confirmed `4/743 (5.3)` and the count/total/percentage label.  
**Quality-control relevance:** The printed fields form an internally reproducible percentage mismatch; the authoritative field is not identifiable from the package.  
**Potential downstream evidence impact:** If confirmed, a baseline-characteristics extractor could copy `5.3%` or a count-derived percentage without knowing which is authoritative; no propagation or conclusion change is asserted.  
**Human verification steps:** Verify the underlying transport record or table output and identify the authoritative numerator, denominator, and percentage.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Liberal vascular-surgery percentage is nonzero with a printed zero numerator

**Candidate statement:** The liberal vascular-surgery cell pairs a zero numerator with a nonzero percentage.  
**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Exact source locations:** [Supplement 2, eTable 2, PDF p. 15](<../joi240147supp2_prod_1738701765.29201.pdf#page=15>), liberal oxygen group, vascular surgery row.  
**Source evidence:** The direct PDF prints `0/747 (1.1)` under `no./total no. (%)`.  
**Reported-versus-comparator:** Reported `1.1%` versus the percentage implied by numerator `0` and denominator `747`.  
**Reasoning procedure:** Apply the displayed count/total/percentage identity.  
**Calculation:** `100 × 0 / 747 = 0.0%`, not `1.1%`.  
**Alternative source-grounded interpretations:** A typographic zero, carried-over percentage, or unprinted qualifier is possible; no footnote provides another rule.  
**Mechanical evidence recheck:** Direct layout extraction and rendered-page inspection confirmed the printed cell and format label.  
**Quality-control relevance:** The count and percentage cannot both represent the stated quantity under the printed format.  
**Potential downstream evidence impact:** If confirmed, an extractor could copy an unresolved rare baseline frequency into a descriptive table; no propagation or conclusion change is asserted.  
**Human verification steps:** Check the source surgery records or table-production output and identify the authoritative numerator and percentage.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7

**Candidate statement:** Two apparently matched all-patient adjusted results show different displayed upper confidence limits without a table-specific model distinction.  
**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Exact source locations:** [Supplement 2, eTable 4, PDF p. 17](<../joi240147supp2_prod_1738701765.29201.pdf#page=17>), further-adjusted primary outcome; [Supplement 2, eTable 7, PDF p. 20](<../joi240147supp2_prod_1738701765.29201.pdf#page=20>), all-patient adjusted odds ratio; relevant methods [Main article, PDF p. 5](<../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=5>).  
**Source evidence:** eTable 4 prints `0.98 (0.68 to 1.41)` and eTable 7 prints `0.98 (0.68 to 1.39)` for the same displayed counts, outcome, contrast, effect label, point estimate, and lower endpoint.  
**Reported-versus-comparator:** Upper limit `1.41` versus upper limit `1.39` at the same displayed precision.  
**Reasoning procedure:** Compare the matched printed result fields; the relationship is conditional because the two tables do not explicitly bind their adjusted columns to one identical table-specific model.  
**Calculation:** `1.41 − 1.39 = 0.02` displayed upper-limit difference.  
**Alternative source-grounded interpretations:** The models may differ but be insufficiently labelled; if the models are identical, one endpoint is inconsistent. Unrounded intervals and fitted-model details are not supplied.  
**Mechanical evidence recheck:** Direct extraction and page inspection confirmed both intervals, matched event counts, and the absence of a table-specific model formula resolving the comparison.  
**Quality-control relevance:** A repeated adjusted result needs either matching displayed endpoints or enough model labelling to prevent a false same-result comparison.  
**Potential downstream evidence impact:** If confirmed, an adjusted-effect extractor could copy either upper confidence limit into a precision field; no propagation or conclusion change is asserted.  
**Human verification steps:** Determine whether the fitted models and data handling are identical; if so, verify the authoritative unrounded and displayed upper interval.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4

**Candidate statement:** The eTable 7 liberal AIS-less-than-3 percentage conflicts with its printed count/denominator and the matched Figure 4 display.  
**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Exact source locations:** [Main article, Figure 4, PDF p. 8](<../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8>), AIS score less than 3; [Supplement 2, eTable 7, PDF p. 20](<../joi240147supp2_prod_1738701765.29201.pdf#page=20>), AIS less than 3.  
**Source evidence:** Figure 4 prints liberal `48/473 (10.1)`; eTable 7 prints liberal `48/473 (9.2)`.  
**Reported-versus-comparator:** eTable 7 `9.2%` versus Figure 4 `10.1%` and the percentage derived from the shared `48/473`.  
**Reasoning procedure:** Match subgroup, group, numerator, denominator, and outcome, then apply ordinary one-decimal percentage rounding.  
**Calculation:** `100 × 48 / 473 = 10.147991...%`, which rounds to `10.1%`, not `9.2%`.  
**Alternative source-grounded interpretations:** eTable 7 may contain a transcription error or use an undisclosed denominator inconsistent with its printed 473.  
**Mechanical evidence recheck:** Direct page inspection confirmed both printed strings and the shared numerator/denominator.  
**Quality-control relevance:** The same displayed subgroup count and denominator support incompatible percentages across supplied locations.  
**Potential downstream evidence impact:** If confirmed, a subgroup extractor could copy `9.2%` rather than the count-derived and matched `10.1%`; no propagation or conclusion change is asserted.  
**Human verification steps:** Verify the subgroup source data, intended denominator, and authoritative displayed percentage.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4

**Candidate statement:** The eTable 7 liberal known-lung-disease percentage differs from the matched Figure 4 percentage despite the same printed count and denominator.  
**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Exact source locations:** [Main article, Figure 4, PDF p. 8](<../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8>), known lung disease, yes; [Supplement 2, eTable 7, PDF p. 20](<../joi240147supp2_prod_1738701765.29201.pdf#page=20>), known lung disease, yes.  
**Source evidence:** Figure 4 prints liberal `14/69 (20.3)`; eTable 7 prints liberal `14/69 (20.2)`.  
**Reported-versus-comparator:** eTable 7 `20.2%` versus Figure 4 `20.3%` and ordinary nearest rounding of `14/69`.  
**Reasoning procedure:** Match the subgroup and printed count/denominator, then calculate the one-decimal percentage while retaining an unspecified rounding convention as an alternative.  
**Calculation:** `100 × 14 / 69 = 20.289855...%`, which is `20.3%` under ordinary nearest rounding.  
**Alternative source-grounded interpretations:** An unreported truncation or production-time rounding convention, or a transcription difference, may explain the discrepancy; the package does not state a publication-wide rounding rule.  
**Mechanical evidence recheck:** Direct page inspection confirmed both values and the shared `14/69`.  
**Quality-control relevance:** Matched one-decimal subgroup displays are inconsistent unless a different rounding rule is established.  
**Potential downstream evidence impact:** If confirmed, a subgroup extractor could copy either one-decimal percentage without a stated convention; no propagation or conclusion change is asserted.  
**Human verification steps:** Verify the intended rounding convention and authoritative subgroup percentage.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1

**Candidate statement:** eTable 10’s postrandomization-exclusion total and group counts do not reconcile with each other or with Figure 1 without an explained population restriction.  
**Status:** Pending Human Adjudication  
**Category:** Cross-document numeric inconsistency  
**Exact source locations:** [Supplement 2, eTable 10, PDF p. 24](<../joi240147supp2_prod_1738701765.29201.pdf#page=24>), exclusion after randomization; [Main article, Figure 1, PDF p. 3](<../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3>), excluded after randomization.  
**Source evidence:** eTable 10 states `N=130` and prints restrictive `55/750 (45)` and liberal `67/758 (55)`; Figure 1 prints 59 restrictive and 71 liberal exclusions, totaling 130.  
**Reported-versus-comparator:** eTable group total `122` versus its stated `130` and Figure 1’s `130`, with each Figure 1 group count four higher.  
**Reasoning procedure:** Sum the displayed eTable group counts and compare them with the eTable total and matched Figure 1 branches.  
**Calculation:** `55 + 67 = 122`; `130 − 122 = 8`; `59 + 71 = 130`; each figure count exceeds its table count by `4`.  
**Alternative source-grounded interpretations:** eTable 10 may intentionally omit four Swiss-law consent-withdrawal cases per group, but neither its row label nor footnote defines that restriction.  
**Mechanical evidence recheck:** Direct page inspection confirmed the eTable values, Figure 1 values, and the absence of an eTable explanation for the eight-person difference.  
**Quality-control relevance:** Participant-flow totals and group counts should state any population restriction needed to reconcile linked displays.  
**Potential downstream evidence impact:** If confirmed, an evidence extractor could copy inconsistent flow totals or group exclusions; no effect-estimate impact, propagation, or conclusion change is asserted.  
**Human verification steps:** Determine whether the eight omissions are intentional; if so, label the population and reconcile total, denominators, and footnote.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Secondary-exclusion cells pair within-group denominators with cross-group partition percentages

**Candidate statement:** eTable 10 pairs within-group denominators with percentages that instead partition the classified cross-group total.  
**Status:** Pending Human Adjudication  
**Category:** Denominator, proportion, or total inconsistency  
**Exact source locations:** [Supplement 2, eTable 10, PDF p. 24](<../joi240147supp2_prod_1738701765.29201.pdf#page=24>), secondary exclusion; count comparator [Main article, Figure 1, PDF p. 3](<../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3>).  
**Source evidence:** eTable 10 states `N=341` and prints restrictive `174/750 (51)` and liberal `165/758 (49)`; its footnote notes two missing randomized-oxygen assignments. Figure 1 matches counts 174 and 165.  
**Reported-versus-comparator:** Printed `51%` and `49%` versus `23.2%` and `21.8%` from the printed cell denominators; the printed percentages instead reproduce from the 339 classified exclusions.  
**Reasoning procedure:** Calculate percentages using each printed cell denominator and compare them with the cross-group classified-total partition.  
**Calculation:** `174/750 = 23.2%`; `165/758 = 21.8%`; `174 + 165 = 339`; `174/339 = 51.3%`; `165/339 = 48.7%`; `341 − 339 = 2`.  
**Alternative source-grounded interpretations:** The intended estimand may be within-group exclusion incidence or allocation distribution among classified exclusions; the table does not choose one consistently or explain how to present the two unassigned patients.  
**Mechanical evidence recheck:** Direct page inspection confirmed the values, footnote, and Figure 1 count comparator.  
**Quality-control relevance:** The display combines incompatible denominator concepts in a count/total/percentage cell.  
**Potential downstream evidence impact:** If confirmed, an extractor could copy 51%/49% as within-group rates or 23.2%/21.8% as allocation shares; no propagation or conclusion change is asserted.  
**Human verification steps:** Establish the intended estimand, use one denominator consistently, and describe the two missing assignments.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Missing-as-event primary count uses a doubled numerator/denominator separator

**Candidate statement:** The restrictive missing-as-event primary-outcome count has a doubled numerator/denominator separator despite otherwise reconciling numerically.  
**Status:** Pending Human Adjudication  
**Category:** Measure, label, or scale inconsistency  
**Exact source locations:** [Supplement 2, eTable 11, PDF p. 25](<../joi240147supp2_prod_1738701765.29201.pdf#page=25>), primary outcome with missing counted as event.  
**Source evidence:** The direct PDF visibly prints restrictive `135//750 (18.0)` under `no./total no. (%)`; the paired liberal cell is `155/758 (20.4)`.  
**Reported-versus-comparator:** Doubled `//` separator versus the table’s single-slash count/denominator notation and paired cell.  
**Reasoning procedure:** Confirm the glyph string directly and compare it with the table convention; separately confirm that the numeric percentage reconciles.  
**Calculation:** `100 × 135 / 750 = 18.0%`; the numeric relation reconciles, while the doubled separator does not match the notation.  
**Alternative source-grounded interpretations:** The doubled slash may be a typographic, encoding, or production artifact; the package does not identify its source stage or intended correction.  
**Mechanical evidence recheck:** Direct rendering, high-resolution crop, raw-text and bounding-box extraction, and targeted CPU OCR all retained both slash glyphs.  
**Quality-control relevance:** A malformed count separator can impair manual or machine extraction even when its arithmetic is coherent.  
**Potential downstream evidence impact:** If confirmed, a manual or machine extractor could retain the malformed separator when copying the display verbatim; no propagation or conclusion change is asserted.  
**Human verification steps:** Confirm the authoritative publication string and determine whether clarification of the notation is needed.  
**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these observations could affect the values, denominators, confidence-interval endpoint, participant-flow fields, or notation copied into a systematic review, meta-analysis, guideline evidence table, or other structured extraction. The package does not establish that any downstream reuse occurred, that any conclusion changed, or that serious harm resulted.

## Limitations and Missing Definitions

No raw data, table-production files, statistical code, fitted-model objects, unrounded estimates, covariance matrices, inverse-probability weights, or publication-production files were supplied. The package therefore cannot resolve authoritative corrections for C001-C002 and C004-C005; model identity for C003; population and denominator definitions for C006-C007; or production cause for C008. This was not a clinical, broad methodological, raw-data, or external-literature audit. See [limitations.md](<review_1_5_3/limitations.md>).

## Human Adjudication Checklist

1. Confirm each cited direct-PDF string against the authoritative publication display.
2. Consult underlying data, statistical output, or production records where needed.
3. Resolve only the stated human question for each candidate and document any correction or clarification outside this report.
4. Complete all five human-adjudication fields for every C ID.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Routing preflight passed with coordinator inference recorded as PASS in INTERACTIVE_CLI mode. Baseline source hashes cover all five PDFs, and baseline reused-artifact hashes cover 38 assets. Final post-report `sha256sum -c` verification matched every direct source and every reused artifact.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort |
|---|---|---|---|
| Coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high |
| Reuse asset curator | root/reuse_asset_curator | gpt-5.6-terra | medium |
| Main quantitative mapper | root/main_mapper | gpt-5.6-terra | medium |
| Support quantitative mapper shard A | root/support_mapper_a | gpt-5.6-terra | medium |
| Support quantitative mapper shard B | root/support_mapper_b | gpt-5.6-terra | medium |
| Numeric consistency reviewer | root/numeric_reviewer | gpt-5.6-terra | medium |
| Cross-source consistency reviewer | root/cross_source_reviewer | gpt-5.6-terra | medium |
| Statistical pass 1 | root/statistics_pass_1 | gpt-5.6-terra | high |
| Evidence rechecker | root/evidence_rechecker | gpt-5.6-sol | high |
| Statistical pass 2 | root/statistics_pass_2 | gpt-5.6-terra | high |
| Evidence-quality auditor | root/quality_auditor | gpt-5.6-sol | high |
| Report generator | root/report_generator | gpt-5.6-terra | medium |

### Performance profile

- **Target basis:** Five direct PDFs contain 144 page units; all units have usable page-delimited native text, so no fresh extraction or OCR is required, but complete quantitative mapping still spans a 103-page protocol/SAP, an 11-page article, a 26-page results supplement with tables, and two short supplements. The target includes the required parallel mapping, three first-pass reviews, recheck, second statistical pass, audit, and report stages.
- **Total source units:** 144
- **Fresh-source units:** 0
- **Target elapsed minutes:** 55-75
- **Started UTC:** 2026-08-19T05:22:40Z
- **Finished UTC:** 2026-08-19T05:50:47Z
- **Observed elapsed minutes:** 28.1
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

The runtime did not expose authoritative response-level token counts for this session or its specialists. Every actual manifested agent therefore has an `UNAVAILABLE` ledger record; no token count was estimated from text. Cached input and cache-write counts are input subsets, and reasoning is an output subset; none is added again to total tokens.

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

The per-agent details are in `review_1_5_3/token_usage_summary.md`. The known amount uses the bundled rates dated 2026-08-18 and is a token-only estimate, not an invoice; the complete token count and complete price remain unavailable.
