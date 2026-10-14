# Quantitative Quality-Control Consistency Review — AMALFI, Workflow 1.6.2

**Pending Human Adjudication**

Paper: *Remote Screening for Asymptomatic Atrial Fibrillation: The AMALFI Randomized Clinical Trial*, Rohan Wijesurendra and colleagues; package `jama.2025.15440`.

## Executive Quality-Control Summary

The complete supplied package yielded **1 stable candidate reporting issue**, C001. It concerns prospective subgroup power within the protocol: the age-under-75 row prints 34% power at total trial size 5000 and two-sided .01, whereas a diagnostic method supported by all 23 other power cells produces a conservative printed-input enclosure of 27.225013–29.972805%. The relative interval gap is .103741, exceeding the workflow precision threshold .05.

An independent inclusion screen, source evidence recheck, second statistical pass and quality-control audit supported its registration. C001 is `plan_material`, relationship `P_P`, evidence state `reproduced`, inclusion audit `CONFIRMED`. These fields record workflow evidence and classification; C001 remains **Pending Human Adjudication**. No replacement power is assigned, and this candidate establishes no discrepancy in an observed primary treatment-effect result.

All **70 physical PDF pages** across four supplied sources were mapped: 34 reusable-backed pages and 36 fresh-required pages. The review covered 91 numeric relationship groups and 52 statistical relationship groups through two distinct complete statistical passes. Two checker findings received independent screening: one was included and one screened out. The 24 checker exclusions were separately reconsidered in statistical pass 2 and the audit; neither stage raised a new finding.

## Package and Reused-Evidence Provenance

The evidence package contains the main article, trial protocol, statistical analysis plan (SAP) and results supplement. Roles follow content: the protocol and SAP are PLAN even though supplied as supplements; the article and non-plan results supplement are REPORT. There are no supplied Office, workbook or CSV sources.

| Source | Actual supplied file and identity | Role | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf](../jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1), main article | REPORT | 9 |
| DOC-002 | [joi250068supp1_prod_1760999665.28862.pdf](../joi250068supp1_prod_1760999665.28862.pdf#page=1), protocol v2.0, 8 June 2021 | PLAN | 26 |
| DOC-003 | [joi250068supp2_prod_1760999665.29862.pdf](../joi250068supp2_prod_1760999665.29862.pdf#page=1), SAP v1.2, 26 June 2025 | PLAN | 24 |
| DOC-004 | [joi250068supp3_prod_1760999665.30362.pdf](../joi250068supp3_prod_1760999665.30362.pdf#page=1), supplemental methods, eTables 1–3 and eFigures 1–4 | REPORT | 11 |

The fresh curator inventoried and hashed 58 retained source-linked assets: 32 USABLE, 15 DUPLICATE, 10 PARTIAL and 1 UNREADABLE; no entire asset was classified STALE. These are asset fitness counts, distinct from unique page coverage. Existing native/layout text, OCR, source-page images and document maps supplied locators and reusable extraction. Previous candidate, checker, screening, classification, recheck, audit and report conclusions were preserved without use as scientific inputs. Discovery and classification were rebuilt from this run's maps and direct-source confirmation.

Protocol native font mapping was unreadable. All 26 protocol pages received fresh CPU source rendering and explicitly user-approved GPU OCR: RapidOCR 1.4.4 with ONNX Runtime GPU 1.28.0 and its CUDA backend on the NVIDIA GeForce RTX 5070 Laptop GPU, accessed through Windows PowerShell 5.1 → WSL → the existing `~/venvs/stt/bin/python`. The OCR served as a locator, with source visuals authoritative for tables and candidate evidence. Native extraction and rendering used the recorded temporary package-local fallback, PyMuPDF 1.26.4 and pypdf 5.9.0; rendering was CPU at 200 dpi. No new GPU package installation was needed.

Detailed provenance: [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [tooling record](review_1_6_2/tooling_record.md).

## Scope, Complete Coverage, and Exclusions

The review addressed counts and denominators, estimate/test compatibility, statistical method logic and planned-versus-reported statistical design. It matched outcome, analysis population, time window, contrast, model and quantity before comparing locations. All physical pages, including covers, contents, methods and references, were inspected and mapped; units without additional applicable results were explicitly documented.

| Source | Total pages | Reusable pages | Fresh-required pages | Mapped pages | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | 26 | 0 | 26 | 26 | COMPLETE |
| DOC-003 | 24 | 16 | 8 | 24 | COMPLETE |
| DOC-004 | 11 | 9 | 2 | 11 | COMPLETE |
| **Total** | **70** | **34** | **36** | **70** | **COMPLETE** |

Reusable page coverage was main pp. 1–9, SAP pp. 7–22, and results p. 1 and pp. 4–11. Fresh-required coverage was protocol pp. 1–26, SAP pp. 1–6 and 23–24, and results pp. 2–3. Reusable and fresh-required counts partition every source. No scientific source-unit gap remains. [Source coverage](review_1_6_2/source_coverage.md) and the [coverage manifest](review_1_6_2/coverage_manifest.md) retain the assignments and durable artifacts.

The scope screens out display-precision differences with relative interval gap at most .05, immediately resolved notation/wording, model-based estimates compared with crude ratios, unsupported conditional observations and peripheral comparisons. Interval-versus-P/test conflicts receive the always-register rule rather than a rounding exemption. The review does not extend to a broad study-design, clinical, novelty, misconduct or raw-data audit and does not propose a preferred analysis. No external literature or web evidence was used.

## Quantitative and Statistical Relationship Coverage

| Review component | Complete scope and durable record |
|---|---|
| Main mapping | All 9 article pages; N001–N080 and S001–S028; complete flow, baseline table, figures, captions and statistical statements. [Main map](review_1_6_2/extraction/main_quantitative_evidence.md) |
| Support mapping | All 61 support pages; N101–N111 and S101–S124; full protocol projection/power tables, SAP definitions, 3 supplementary tables and 4 figures. [Support map](review_1_6_2/extraction/support_quantitative_evidence.md) |
| Numeric checking | 91/91 numeric groups, including 38 baseline count rows, 38 compliance count rows, 13 arrhythmia rows, 5 primary and 5 sensitivity rows, 6 clinical rows and flow/design relationships. [Numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) |
| Cross-source checking | Every applicable REPORT/REPORT, PLAN/REPORT and PLAN/PLAN match, including primary/key secondary definitions, models, populations, intervention, time windows, outcome status and decision rules. [Cross-source review](review_1_6_2/checkers/cross_source_consistency.md) |
| Statistical pass 1 | Fresh `root/statistics_pass1`, gpt-6.1-sol/high; all 52 statistical groups PASS_1_COMPLETE. [Pass 1](review_1_6_2/checkers/statistical_pass_1.md) |
| Statistical pass 2 | Different fresh `root/statistics_pass2`, gpt-6.1-sol/high; all 52 groups PASS_2_COMPLETE, complete ledger/recheck/screen implications and all 24 exclusions reconsidered. [Pass 2](review_1_6_2/checkers/statistical_pass_2.md) |
| Independent quality audit | All source coverage, 91 numeric and 52 dual-pass statistical groups, 24 exclusions, 2 finding decisions and C001 evidence/classification. [Audit](review_1_6_2/quality/evidence_quality_audit.md) |

The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) records both pass statuses for S001–S028 and S101–S124. Detailed checks covered 49 power cells, 31 sample-size outputs and all 31 supplementary P comparisons. Count-based primary/sensitivity estimates and intervals were reconstructed where source inputs support them; crude ratios were distinguished from censored log-rank estimates. Subgroup heterogeneity tests were matched to their between-subgroup hypotheses. Available primary, sensitivity and exploratory estimate/interval/test relationships were coherent; absence of event histories or individual outcomes was recorded without inventing those inputs.

## Inclusion Screening Summary

A finding was included only when source reproduction supported an always-register category (Route A) or all three Route B criteria: in focus, not resolved by immediate context, and bearing on interpretation or extraction. For applicable numeric comparisons, both displayed-input and printed-output half-unit intervals were allowed before measuring the relative gap. There was no candidate count target.

| Screening decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 1 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| **Total** | | **2** |

All other screened-out reason codes have zero finding decisions. F-ST1-001 was included as C001 under Route A, category 4. F-XS-001 was screened out because the SAP permits later additional exploratory clinical analyses and defers their details; printed clinical estimates/intervals without clinical P values or a clinical-specific prespecification claim do not establish a prohibited hypothesis test or another reproduced conflict. It receives no candidate card. The independent audit retained both decisions without amendments. No consolidation was required; no pass-2 or audit finding was added. [Canonical screening log](review_1_6_2/screening/inclusion_screen.md).

The **24 excluded observations** in checker tables—8 numeric, 7 cross-source and 9 statistical pass 1—are distinct from those two emitted findings. All 24 were individually reconsidered under Route A and display precision in pass 2 and the audit; no qualifying excluded observation was identified. Statistical pass 2 added no new exclusions. Reconciled routine checks remain in relationship records rather than inflating screening counts.

## Review-Domain Summary

| Review domain | Definition | Stable candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests or statistical method logic in REPORT materials | 0 |
| report_internal_inconsistency | REPORT materials disagree about the outcome, time, population or comparison belonging to a result | 0 |
| protocol_report | REPORT differs from PLAN in a statistical design or analysis element | 0 |
| plan_material | Statistical design inconsistency within PLAN material | 1 |
| **Total** | | **1** |

| Relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 0 |
| P_P | Within or between PLAN material | 1 |
| S_C | Between REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| **Total** | | **1** |

| Evidence state | Candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **1** |

Inclusion audit: CONFIRMED 1; QUESTIONED 0. These are threshold-audit records, not human adjudications. All relationships for C001 are solely P_P, so no mixed-relationship precedence decision is needed. Every domain, relationship and evidence-state count reconciles to the one stable candidate.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001) | Age-under-75 planned power at 5000/.01 | plan_material | P_P | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Age-under-75 subgroup power does not reconcile with a reproducing same-table calculation {#c001}

**Candidate statement:** Protocol Table 4 prints 34% power for the age-under-75 subgroup at total trial size 5000 and two-sided significance level .01. A continuity-corrected two-proportion reconstruction that satisfies the workflow precision rule for the other 23 power cells gives a central diagnostic power of 28.585280%; its full conservative printed-input enclosure remains below the printed 34% interval.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol Table 4 affected power cell versus PLAN protocol Table 4 assumptions and all 23 other power cells.

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 4

**Classification rationale:** The affected power, its numerical inputs and the reproducing comparison cells are prospective PLAN content in one protocol. This is plan-internal, P_P. The report's trial context corroborates the design but is not a conflicting comparator, so it creates no P_R relationship.

**Classification ambiguity:** None for document roles or relationship. The exact Table 4 software/function and underlying correction implementation are not supplied.

**Exact source locations:** [Protocol, PDF p. 22, Table 4](../joi250068supp1_prod_1760999665.28862.pdf#page=22), age <75 row, rightmost “Power for total of 5000, 2p<0.01” cell; all input and other-power comparison cells in the same Table 4. Contextual design support only: [protocol, PDF p. 20, Table 2](../joi250068supp1_prod_1760999665.28862.pdf#page=20), continuity-corrected sample-size heading, and [protocol, PDF p. 21, Table 3](../joi250068supp1_prod_1760999665.28862.pdf#page=21), whole-trial power design.

**Source evidence:** Table 4 age <75 row: population 25%; patch AF 2.52%; active AF at 2.5 years 2.96%; active/control ratio 2.5; implied control AF 1.18%; 90%-power sample sizes 2924 at .05 and 4048 at .01. Powers at total trial 4000/.05, 4000/.01, 5000/.05 and 5000/.01 are 41%, 20%, 52% and 34%. The screen independently inspected the printed cell and same-table comparators visually.

**Reported-versus-comparator:** Printed 34% versus diagnostic 28.585280%. At 4000/.01 the same method gives 20.530754% versus 20%; at 4000/.05 and 5000/.05 it gives 41.851152% and 52.055448% versus 41% and 52%. All other 23 Table 4 power outputs satisfy the precision threshold; all 12 displayed sample-size outputs also track the reconstruction within 1% central discrepancy. No corrected power is assigned.

**Reasoning procedure:** Use equal allocation, subgroup per-arm size m=Tf/2, control and active rates p0 and p1, and the source-grounded continuity-corrected two-proportion normal reconstruction. Establish same-display tracking across every Table 4 power cell, then apply full conservative interval arithmetic for each displayed input and the affected printed power. The source does not identify the exact power implementation; this is an empirically reproducing diagnostic method, not an asserted universal algorithm.

**Calculation:** Let d=p1−p0, A=√[(p0+p1)(1−(p0+p1)/2)], B=√[p0(1−p0)+p1(1−p1)], z=Φ⁻¹(1−α/2). Power (%) = 100{Φ[(√m d−zA−1/√m)/B]+Φ[(−√m d−zA−1/√m)/B]}. At p0=.0118, p1=.0296, T=5000, f=.25, α=.01 and m=625, the diagnostic value is 28.585280%. Allow p0∈[.01175,.01185], p1∈[.02955,.02965], f∈[.245,.255], and conservatively T∈[4999.5,5000.5], while .01 remains the exact decision threshold. Full interval arithmetic gives 27.225013–29.972805%; printed 34% permits [33.5,34.5]%. Minimum gap = 33.5−29.972805 = 3.527195 percentage points; relative discrepancy = 3.527195/34 = .103741 > .05. The narrower endpoint envelope 27.350760–29.844731% likewise remains separated. Allowing rates independently is conservative; imposing the displayed ratio can only narrow the permitted box.

**Affected result or extracted value:** The planned age-under-75 subgroup power at total trial size 5000 and two-sided .01. No discrepancy in the primary reported treatment-effect result or the reported age-80/sex .05 power claim is established by this candidate.

**Why context does not resolve it:** Route A, category 4: a printed result remains separated from the precision enclosure of a method that tracks the other rows/cells of the same display. The unknown exact implementation becomes the human question, rather than an exclusion.

**Alternative source-grounded interpretations:** A cell-specific correction or underlying unprinted rate/subgroup input may account for 34%. An uncorrected normal calculation gives 35.699810%, near 34% under the workflow threshold, but gives 27.416397% at 4000/.01 and does not track the same row's printed 20%. The source does not supply a separate rule for the affected cell.

**Mechanical evidence recheck:** Completed by fresh runtime /root/evidence_rechecker. All cited locations, printed 34%, inputs and 23 power comparators were found and matched against source visuals. The rule and independent full interval calculation reproduce the discrepancy. PLAN/PLAN, P_P and plan_material are confirmed; evidence state is reproduced. No source-transcription or classification correction was required. The outward numerical guard of ±0.00002 percentage point is included in the enclosure reported above; the exact implementation remains unspecified.

**Potential downstream evidence impact:** If a reviewer uses the protocol for design extraction, they could copy 34% as the stated subgroup power. This candidate does not establish any change to observed trial results or downstream conclusions.


C001 remains **Pending Human Adjudication**. Additional direct design support is [protocol PDF p. 19, Appendix 2](../joi250068supp1_prod_1760999665.28862.pdf#page=19), which states 1:1 equal allocation and that Table 4 gives the same calculations for subgroups. The [independent recheck](review_1_6_2/verification/evidence_recheck.md) preserves the complete six-row Table 4 transcription, all 24 reconstructed powers, all 12 sample-size comparisons, and every source-location fact. Its [computation record](review_1_6_2/preprocessing/recheck-initial-power-computation.json) contains the interval calculation. The [quality audit](review_1_6_2/quality/evidence_quality_audit.md) independently reproduced the guarded separation and confirmed inclusion and classifications. Its independent approximation differed by approximately .000001 percentage point within the explicit numerical guard; the final card retains the recheck enclosure.

The formula is a diagnostic reconstruction empirically supported across the same display. Neither its exact attribution to the source software nor an explanation of how 34% arose is established. The unspecified calculation convention and underlying inputs remain a bounded missing definition; no final correction is inferred.

## Downstream Evidence-Chain Considerations

A design extractor could copy the protocol's 34% planned subgroup power into a systematic-review table or evidence summary. If subsequent human adjudication identifies a reporting issue, that design entry could require clarification. The affected quantity is prospective age-under-75 power at 5000/.01; it is not an observed randomized treatment-effect estimate. This review provides no evidence that propagation occurred, that a synthesis or guideline conclusion changed, or that a clinical outcome was affected.

## Limitations and Missing Definitions

All supplied pages and available quantitative relationships were covered. Exact Table 4 power software/function, correction convention and unrounded inputs are not supplied. Individual/imputed continuous outcomes, permutation details and confidence-interval construction; log-rank O−E/V and event/censoring histories; exact quantile, continuous/trend procedures and individual ranks; and unlabeled histogram bin counts limit exact replication beyond the available aggregate checks. Separately referenced outcome-derivation/economic documents and later clinical-analysis details are absent. Some legacy derivative engine versions were not retained.

These limitations were kept distinct from source-unit coverage: fresh extraction and visual confirmation closed all reusable-derivative gaps. No missing detail alone was treated as a candidate, and no unreported input or preferred method was imposed. Full bounded limitations are retained in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Source integrity and tooling

The [before source hashes](review_1_6_2/source_hashes_before.sha256) identify all four supplied PDFs; the [after source hashes](review_1_6_2/source_hashes_after.sha256) retain the recomputed comparison. The [before reused-asset hashes](review_1_6_2/reused_artifact_hashes_before.sha256) and [after reused-asset hashes](review_1_6_2/reused_artifact_hashes_after.sha256) cover all 58 reused files. The quality audit independently checked both sets unchanged. All supplied sources and pre-existing audit artifacts were preserved. Final integrity checks and automated conformance are recorded in [review_validation.json](review_1_6_2/review_validation.json); that record is authoritative for final validation status.

The [tooling record](review_1_6_2/tooling_record.md) documents the initial probe, missing direct tools, package-local fallback, exact engines, user-approved GPU device and environment-removal record. Raw GPU OCR bounding boxes, confidences and timing are retained per page. Local inspection of every protocol log found no CUDA-provider shift or initialization/library-load failure. Source confirmation remained visual. HTML rendering and final automated validation are performed by the coordinator after this Markdown assembly.

### Routing and agent execution

[Routing preflight](review_1_6_2/routing_preflight.md) is PASS: execution mode INTERACTIVE_CLI, provider CURRENT_SESSION, run model gpt-6.1-sol, source DEFAULT; coordinator inference, fixed role matrix and all ten named role presets passed. No provider or authentication configuration was changed. Every mandatory specialist used a fresh, distinct runtime. Both statistical reviewers and screening/recheck/audit specialists used high effort; ordinary specialists used medium effort.

The [execution manifest](review_1_6_2/agent_execution_manifest.md) records 13 actual runtimes: the coordinator, 11 mandatory specialists and one additional numeric-documentation repair specialist. IDs below reproduce its canonical task-name notation, which omits the leading slash.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_documentation_repair | root/numeric_documentation_repair | gpt-6.1-sol | medium | FRESH_SPAWN | quality/numeric_documentation_repair.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Manifest artifact paths are relative to `review_1_6_2/`. No conditional second inclusion-screen stage was needed because statistical pass 2 emitted no new finding. The optional documentation repair retained the numeric role's medium effort; a subsequent audit-located two-value diagnostic transcription repair was documented without changing sources, findings, screening or candidate classifications.

### Reproducibility performance

The package-specific planning target considers reusable coverage, fresh OCR/native extraction, visual table requirements, relationship volume and required distinct agent waves. It was not derived from SAP length or page count alone. The coordinator finalizes the following exact run-state fields immediately after complete Markdown assembly. HTML rendering and local automated validation are outside the observed review-duration window.

- **Target basis:** Four PDFs with 70 total pages, 34 reusable pages and 36 fresh-required pages; 26 protocol pages need GPU OCR because native font mapping is unreadable, while 10 other fresh pages need native extraction. No Office conversion. Main and support mapping and three checkers run concurrently; 11 distinct mandatory specialist stages plus conditional screening and recheck waves. Target reflects OCR startup, visual table confirmation and complete planned-versus-reported analysis coverage.
- **Total source units:** 70
- **Fresh-source units:** 36
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-10-11T18:29:30Z
- **Finished UTC:** 2026-10-11T19:25:03Z
- **Observed elapsed minutes:** 55.55
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Twenty-six fresh GPU OCR pages and CUDA startup; complete same-table power and sample-size reconstruction with display-precision enclosures; sequential independent screening, source recheck, second statistical pass and quality audit; audit documentation and transcription repair; complete report assembly.
