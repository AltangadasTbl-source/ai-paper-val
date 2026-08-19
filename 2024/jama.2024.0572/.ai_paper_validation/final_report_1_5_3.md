# 1. Quantitative Quality-Control Consistency Review — Workflow 1.5.3

## 2. Pending Human Adjudication

> **Pending Human Adjudication**
>
> This report records reproducible quantitative reporting quality-control candidates from the supplied package. All candidate determinations and any corrective action require human adjudication.

## 3. Executive Quality-Control Summary

Complete source coverage produced **2 stable candidate consistency issues**: C001 and C002. Both are **Pending Human Adjudication**. The review found a potentially inconsistent pair of ITT mRS displays and a repeated effect-measure label/scale inconsistency. Small preventable reporting defects can matter for downstream evidence extraction; this report does not claim that either issue propagated, changed a conclusion, or caused serious harm.

## 4. Package and Reused-Evidence Provenance

The supplied package contains seven direct PDFs: a 14-page main article, five support/administrative PDFs, and a 53-page results supplement. Direct-source identity and page counts are recorded in [source inventory](<review_1_5_3/source_inventory.md>); pre-review source hashes are in [source_hashes_before.sha256](<review_1_5_3/source_hashes_before.sha256>).

Reusable, source-linked native text, rendered pages, page manifests, and document maps covered all 14 main-article pages and all 53 results-supplement pages. The remaining 160 pages were directly mapped. Reused artifacts were treated as locators and transcription aids, not as final authority; their inventory and pre-review hashes are in [evidence_asset_inventory.md](<review_1_5_3/evidence_asset_inventory.md>) and [reused_artifact_hashes_before.sha256](<review_1_5_3/reused_artifact_hashes_before.sha256>).

## 5. Scope, Complete Coverage, and Exclusions

All **227/227** direct PDF page units were mapped: 67 reusable-backed units and 160 fresh-required units. Every direct-source row is complete in [source_coverage.md](<review_1_5_3/source_coverage.md>).

| Source | Total | Reusable | Fresh-required | Mapped |
|---|---:|---:|---:|---:|
| Main article | 14 | 14 | 0 | 14 |
| Support/administrative PDFs | 160 | 0 | 160 | 160 |
| Results supplement | 53 | 53 | 0 | 53 |
| **Total** | **227** | **67** | **160** | **227** |

The review considered numeric, denominator, statistical, cross-document, label/scale, and rate/count consistency. It excluded broad methodological or clinical judgments, external evidence, and coherent display-zero P values alone. No candidate was created solely from `P = 0`, `p = 0.000`, finite precision, underflow, or a reconstructed tiny P value.

## 6. Quantitative and Statistical Relationship Coverage

The complete numeric inventory covers **N001-N113**. The statistical inventory covers **S001-S077**. Numeric, cross-source, and first statistical-pass reviews were completed before stable candidate registration. A distinct second statistical pass revisited all 77 statistical relationships, the cross-lane ledger, and mechanical recheck facts; it emitted no new candidate.

The two statistical passes have explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records for every S relationship in [statistical pass 1](<review_1_5_3/checkers/statistical_pass_1.md>) and [statistical pass 2](<review_1_5_3/checkers/statistical_pass_2.md>). Detailed coverage scopes are in [coverage_manifest.md](<review_1_5_3/coverage_manifest.md>).

## 7. Candidate Index

| Stable ID | Category | Short description | State |
|---|---|---|---|
| [C001](#c001--itt-figure-2-mrs-distributions-conflict-with-itt-etable-2-threshold-counts) | Cross-document numeric inconsistency | ITT Figure 2 mRS distribution thresholds do not reconcile with ITT eTable 2 counts. | Pending Human Adjudication |
| [C002](#c002--arr-is-labeled-as-an-absolute-risk-reduction-but-displayed-and-interpreted-as-a-ratio) | Measure, label, or scale inconsistency | `aRR` is expanded as an absolute risk reduction while displayed and interpreted on a ratio scale. | Pending Human Adjudication |

## 8. Candidate Evidence Cards

## C001 — ITT Figure 2 mRS distributions conflict with ITT eTable 2 threshold counts

**Candidate statement:** The Figure 2 ITT 90-day mRS distributions and Supplement 5 eTable 2 ITT threshold counts do not reconcile under ordinary nearest-whole-percentage rounding, despite matching ITT labels and 168 participants per arm.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article Figure 2 — PDF p. 7](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>); [Supplement 5 eTable 2 — PDF p. 38](<../joi240006supp5_prod_1708623115.01733.pdf#page=38>); [main Results population statement — PDF p. 4](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4>); and [Supplement 5 eFigure 3 — PDF p. 8](<../joi240006supp5_prod_1708623115.01733.pdf#page=8>).

**Source evidence:** Figure 2 is titled as an intention-to-treat 90-day mRS distribution. Its core-stratum denominators total EVT 117+51=168 and medical management (MM) 119+49=168. eTable 2 is also explicitly ITT with EVT N=168 and MM N=168, and prints mRS 0-2 as 34/168 and 12/168, mRS 0-3 as 65/168 and 31/168, and mRS 5-6 as 76/168 and 102/168, respectively.

**Reported-versus-comparator:** From Figure 2's printed percentages and denominators, the uniquely feasible mRS 0-6 counts are EVT <100 mL `[2, 7, 21, 26, 17, 9, 35]`, EVT >=100 mL `[1, 3, 5, 10, 0, 5, 27]`, MM <100 mL `[0, 2, 9, 17, 27, 24, 40]`, and MM >=100 mL `[1, 0, 2, 8, 0, 8, 30]`. These yield Figure-derived EVT/MM mRS 0-2 counts of 39/14 and mRS 0-3 counts of 75/39, versus eTable 2 counts of 34/12 and 65/31. The mRS 5-6 counts reconcile at 76/102; reconstructed mRS-6 counts 62/70 also reconcile with eTable mortality.

**Reasoning procedure:** For each printed whole percentage `p`, stated denominator `n`, and integer count `k`, the diagnostic applies ordinary nearest-whole-percent feasibility: `p - 0.5 <= 100k/n < p + 0.5`. The mutually exclusive mRS categories 0-6 must total each printed bar denominator. Threshold counts are then summed across the two core strata within each randomized arm.

**Calculation:** The Figure-derived minus eTable 2 differences are +5 EVT and +2 MM for mRS 0-2; +10 EVT and +8 MM for mRS 0-3; and 0/0 for mRS 5-6. The direct sources do not state the figure's unrounded values or percentage-production rule, so this is a reproducible diagnostic comparison, not an attribution of cause.

**Alternative source-grounded interpretations:** The displays may use different outcome derivations or versions despite identical ITT labels and arm totals; Figure 2 percentages, labels, or segment assignments may contain a production issue; eTable 2 may use an unstated outcome set; or an unstated non-nearest rounding, normalization, or weighting rule may invalidate the reconstruction.

**Mechanical evidence recheck:** Direct-PDF recheck located both displays, matched the Figure 2 title, legend order, four denominators, eTable 2 headings and threshold rows, and reproduced the integer-feasibility calculation. It records the missing raw category counts, unrounded percentages, generation dataset/version, and stated calculation rule in [evidence_recheck.md](<review_1_5_3/verification/evidence_recheck.md>).

**Quality-control relevance:** If confirmed, this is a candidate consistency issue because a data extractor could select conflicting ITT functional-outcome counts or proportions from supplied displays.

**Potential downstream evidence impact:** A systematic reviewer, meta-analyst, guideline evidence extractor, or tabulator could copy different ITT mRS threshold values if this discrepancy is confirmed. This report does not assert that such copying occurred or that the paper's conclusion changed.

**Human verification steps:** Obtain the authoritative mRS 0-6 counts by treatment and core stratum; confirm whether Figure 2 and eTable 2 share the same ITT records, category definitions, missing-outcome handling, and data version; then document the percentage-calculation rule and the display that should control.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — `aRR` is labeled as an absolute risk reduction but displayed and interpreted as a ratio

**Candidate statement:** The main narrative and tables expand `aRR` as “absolute risk reduction,” while printed estimates, a greater-than-1 interpretation, separate `aRD` values, and supplied SAP statements indicate a ratio-scale measure.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Main narrative — PDF p. 6](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>); [Main Table 2 — PDF p. 7](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7>); [Main Table 3 — PDF p. 9](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9>); [trial SAP — PDF p. 17](<../joi240006supp3_prod_1708623114.99733.pdf#page=17>); [secondary-analysis SAP — PDF p. 4](<../joi240006supp4_prod_1708623115.00733.pdf#page=4>); and [Supplement 5 eTable 7 — PDF p. 43](<../joi240006supp5_prod_1708623115.01733.pdf#page=43>).

**Source evidence:** The narrative and Tables 2-3 expand `aRR` as “absolute risk reduction.” Table 2 states that values greater than 1 indicate a higher rate ratio and prints values including 0.89 (0.84-0.95), 0.91 (0.87-0.95), and 1.05 (1.02-1.08). Table 3 separately labels `aRD` as adjusted risk difference and gives, for example, aRR 1.33 (0.52-3.44) alongside aRD 0.178 (-0.109 to 0.465). The SAPs specify modified-Poisson relative-risk analyses.

**Reported-versus-comparator:** An absolute risk reduction/risk difference is additive, expressed in risk units, and has a null value of 0. A risk or rate ratio is multiplicative, dimensionless, and has a null value of 1. The printed estimates, confidence intervals, and explicit greater-than-1 rate-ratio interpretation fit the latter scale; the repeated expansion “absolute risk reduction” does not reconcile with it.

**Reasoning procedure:** Compare the direct abbreviation expansion, table interpretation, printed null scale, representative estimates and intervals, separately labelled `aRD`, and supplied modified-Poisson/relative-risk descriptions. No unreported coefficient, standard error, P value, or model reconstruction is required.

**Calculation:** This is a logical scale comparison rather than a numerical reconstruction. A value 1.33 with a confidence interval 0.52-3.44 is ratio-scale and centered on a null of 1; the separately printed aRD 0.178 with an interval spanning 0 is additive-scale. The source's own rate-ratio sentence confirms the mismatch.

**Alternative source-grounded interpretations:** `aRR` may have been intended as adjusted risk ratio, while “absolute risk reduction” was a repeated abbreviation-key error. The tables' rate-ratio sentence may instead be unintended, or an unreported nonstandard term may have been used. The supplied package provides no definition that makes an absolute reduction compatible with the displayed ratio scale.

**Mechanical evidence recheck:** Direct-PDF inspection matched the narrative, abbreviation keys, values, footnotes, separate `aRD` values, and SAP model statements. The recheck identifies the absent authoritative abbreviation dictionary and intended effect-measure name in [evidence_recheck.md](<review_1_5_3/verification/evidence_recheck.md>).

**Quality-control relevance:** If confirmed, a data extractor could classify a relative effect as an absolute effect, changing the recorded measure class, null value, and scale.

**Potential downstream evidence impact:** A systematic review, meta-analysis, guideline evidence table, or data-extraction workflow could record a relative estimate under an absolute-effect field if the label is confirmed to be inconsistent. This report does not claim that propagation occurred or that the study conclusion changed.

**Human verification steps:** Confirm the authoritative expansion of `aRR`, whether `a` denotes adjusted, and whether `RR` denotes risk ratio or rate ratio; reconcile the narrative, Tables 2-3, SAP-linked descriptions, and supplementary labels with the intended measure while retaining the separately reported `aRD` distinction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## 9. Downstream Evidence-Chain Considerations

If confirmed, C001 could affect which ITT mRS threshold count is extracted, and C002 could affect effect-measure classification. These are bounded possibilities for later evidence products; no downstream propagation, conclusion change, or harm is asserted.

## 10. Limitations and Missing Definitions

The complete limitations record is in [limitations.md](<review_1_5_3/limitations.md>). C001 lacks raw category counts, unrounded percentages, a figure-generation version, and a stated percentage rule. C002 lacks an authoritative `aRR` expansion and intended effect-measure name. The review used supplied local evidence only and did not undertake a raw-data or clinical-methodology audit.

## 11. Human Adjudication Checklist

For each stable ID, a human reviewer should: confirm each cited direct-source page; inspect the printed values and comparator; reproduce the stated comparison; obtain the named missing definition or source record; decide whether a correction is warranted; and complete the five `__` fields in the card. Both IDs remain Pending Human Adjudication unless and until that review occurs.

## 12. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Routing preflight passed, including the fixed model matrix, coordinator inference, interactive execution mode, and nine named role presets; see [routing_preflight.md](<review_1_5_3/routing_preflight.md>). The evidence-quality audit reports 7 direct-source and 137 reused-artifact hash records reproducing at its review point, complete 227/227 mapping, identical C001/C002 ledger/recheck/audit sets, and valid PDF page links; see [evidence_quality_audit.md](<review_1_5_3/quality/evidence_quality_audit.md>).

### Agent execution

The final manifest records the coordinator and all ten completed specialist stages: curator, main mapper, support mapper, numeric reviewer, cross-source reviewer, statistical pass 1, evidence rechecker, statistical pass 2, quality-control auditor, and report generator. Models and reasoning efforts are recorded in [agent_execution_manifest.md](<review_1_5_3/agent_execution_manifest.md>); every actual runtime agent appears exactly once.

### Performance

- **Target basis:** Seven direct PDFs contain 227 page units. One 14-page main article and one 53-page results supplement have page-linked reusable evidence, while 160 pages across five support or administrative PDFs require fresh direct mapping; one 40-page scanned statistical analysis plan may require targeted visual inspection or CPU OCR. The planned work also includes two mapping lanes, three concurrent checker lanes, two distinct statistical passes, evidence recheck, quality audit, and report assembly.
- **Total source units:** 227
- **Fresh-source units:** 160
- **Target elapsed minutes:** 75-110
- **Started UTC:** 2026-08-19T04:31:45Z
- **Finished UTC:** 2026-08-19T05:07:17Z
- **Observed elapsed minutes:** 35.5
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) | Count status |
|---|---:|---:|---:|---:|---|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 | INCOMPLETE |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 | INCOMPLETE |

Authoritative response-level token counts were not exposed by this interactive coordinator or the specialist runtime, so every manifested agent has an `UNAVAILABLE` ledger record. Zero is the known subtotal only, not an estimate of actual usage. Per-agent detail is in [token_usage_summary.md](<review_1_5_3/token_usage_summary.md>). Cached input and cache-write counts are input subsets and reasoning tokens are an output subset; they are not additional total tokens. The known amount uses the bundled rates dated 2026-08-18 and is a token-only API-equivalent estimate, not an invoice; the complete estimate remains unavailable.
