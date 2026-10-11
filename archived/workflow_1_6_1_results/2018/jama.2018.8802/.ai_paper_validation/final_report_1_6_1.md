# Quantitative Quality-Control Consistency Review — GOLDEN BRIDGE–AIS

**Pending Human Adjudication**

Workflow 1.6.1 • Paper package `jama.2018.8802` • Supplied main article and two supplements.

## Executive Quality-Control Summary

Complete review of three supplied PDFs identified **one stable candidate, C001**. It concerns the composite co-primary endpoint: the main article explicitly averages patient-specific adherence fractions, whereas the prospective protocol and the results supplement describe a pooled fulfilled-opportunity proportion. The supplement expressly links its definition to the randomized phase. Both summaries are coherent, but their weighting differs and the supplied counts yield distinct descriptive values beyond display precision.

C001 has evidence state `reproduced`, review domain `protocol_report`, primary relationship `P_R`, and inclusion audit `CONFIRMED`. These fields organize human review; they do not adjudicate validity, importance or action. Three independently emitted findings were screened into this single issue: one INCLUDE and two consolidated duplicates. No additional finding emerged from statistical pass 2 or the quality audit.

All **44/44 source pages**, **156 numeric relationships**, and **129 statistical relationships in both passes** were covered. The candidate's potential relevance concerns endpoint interpretation and extraction. The supplied evidence does not establish another adjusted effect, a changed significance decision, or a changed trial conclusion.

## Package and Reused-Evidence Provenance

The supplied package comprises the completed cluster-randomized trial article, a prospective protocol dated April 17, 2014, and a results supplement. Document roles follow content. The protocol remains PLAN although supplied as a supplement. No Office, workbook or CSV source was supplied.

| Source ID | Actual supplied filename | Role | Source units |
|---|---|---|---:|
| DOC-001 | `jama_wang_2018_oi_180070.pdf` | REPORT | 10 PDF pages |
| DOC-002 | `joi180070supp1_prod.pdf` | PLAN | 25 PDF pages |
| DOC-003 | `joi180070supp2_prod.pdf` | REPORT | 9 PDF pages |

Sixty-five immutable source-linked assets from `review_1_5_2/preprocessing/` were reused: nine native/layout text or coordinate TSV files, three PDF metadata records, one extraction-status record and 52 page images. Native text and coordinate page keys cover all 44 unique pages; 52 overlapping images cover 39 unique pages. Discovery and scientific mapping were rebuilt from the beginning. Historical candidate selections, screens, classifications and reports were not discovery inputs.

The curator compared every native-text page with current direct-source extraction; ordered alphanumeric content matched on all 44 pages. This confirms correspondence, while punctuation, symbols and dense table alignment require source inspection. Historical extraction is attributed to Acrobat COM without complete version information; historical rendering engines are incompletely documented. Direct Poppler 25.03.0 source text and targeted CPU page rendering supported current checks and the mechanical recheck. Full provenance is recorded in [the evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md).

## Scope, Complete Coverage, and Exclusions

The review covered counts and denominators, estimate/test logic, statistical method logic, and planned versus reported statistical design under the supplied scope contract. Main/support mapping included every table row, figure, caption, result occurrence, endpoint definition and analysis specification; reference and administrative units were explicitly mapped as nonapplicable where appropriate.

| Direct source | Total | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| `jama_wang_2018_oi_180070.pdf` | 10 | 10 | 0 | 10 | COMPLETE |
| `joi180070supp1_prod.pdf` | 25 | 25 | 0 | 25 | COMPLETE |
| `joi180070supp2_prod.pdf` | 9 | 9 | 0 | 9 | COMPLETE |
| **Total unique PDF pages** | **44** | **44** | **0** | **44** | **COMPLETE** |

Zero fresh-required units means existing transcription assets were adequate; every page still received fresh scientific mapping. Protocol p.5's embedded flow diagram was visually mapped from readable source-matched imagery. Missing historical images for main p.10 and protocol pp.22–25 do not leave scientific gaps: their source-linked text was readable and completely mapped.

Rounding/display precision, readily resolved notation or wording, modeled-versus-crude comparisons, unsupported conditional observations and peripheral comparisons were excluded under the scope rules. A broad clinical, methodology, novelty, misconduct or raw-data audit was outside scope. No preferred analysis or external literature was introduced. Disjoint assignments and all durable parts appear in [the coverage manifest](review_1_6_1/coverage_manifest.md).

## Quantitative and Statistical Relationship Coverage

The fresh maps contain 80 main-paper groups and 34 support groups. These were expanded into 156 numeric IDs and 129 statistical IDs without treating grouping as a limit on coverage or findings.

| Relationship scope | IDs | Complete count |
|---|---|---:|
| Main numeric relationships | N001–N080 | 80 |
| Support numeric relationships | N081–N156 | 76 |
| Statistical results | S001–S100 | 100 |
| Statistical design and methods | S101–S129 | 29 |
| Statistical pass 1 | S001–S129 | 129 |
| Statistical pass 2 | S001–S129 | 129 |

Coverage includes all primary/adherence and clinical outcome rows, both adjusted inference columns, all supplementary vascular and sensitivity rows, baseline P values, safety, figure matches, populations, cluster/analysis units, endpoint weighting, sample-size inputs, covariates, missing-data descriptions and decision rules. Every S row records `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. Missing definitions constrain exact reconstruction where named; conventional model or test defaults were not substituted.

Both passes used distinct fresh `gpt-6.1-sol`/`high` statistical agents with separate fresh design-shard agents. Pass 2 revisited the full ledger, screening decisions and recheck facts, emitted zero new findings, and therefore required no additional inclusion screen. The complete records are in [the numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [the statistical inventory](review_1_6_1/statistics/relationship_inventory.md), [pass 1](review_1_6_1/checkers/statistical_pass_1.md) and [pass 2](review_1_6_1/checkers/statistical_pass_2.md).

The independent quality audit also examined all **119 checker excluded-observation records**: numeric 23; cross-source 23; pass 1 original 19 plus design 15; pass 2 results 18 plus design 21. These retain independent checker provenance and are distinct from the three findings submitted to inclusion screening. No screening reversal or new audit finding was identified.

## Inclusion Screening Summary

Inclusion required a reproduced, in-focus comparison that immediate context does not resolve and that can affect interpretation or extraction of a named result. No candidate count was targeted. The following counts reconcile to [the single screening log](review_1_6_1/screening/inclusion_screen.md).

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 1 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 2 |
| **Total screened findings** | | **3** |

All other screened-out reason-code counts are zero: `NOT_REPRODUCED`, `ROUNDING_OR_DISPLAY_PRECISION`, `NOTATION_OR_TYPOGRAPHY`, `TERMINOLOGY_OR_WORDING`, `MODEL_VERSUS_CRUDE`, `CONTEXT_RESOLVES`, `CONDITIONAL_OR_UNREPORTED`, `PERIPHERAL_COMPARISON` and `OUT_OF_FOCUS`.

F-XS-001 is the representative INCLUDE mapped to C001. F-ST1-001 and F-ST1-101 are independently reproduced occurrences consolidated as `DUPLICATE_OF_INCLUDED`, also mapped to C001. Their source-location union and checker provenance remain preserved; they receive no separate evidence cards. INCLUDE 1 + SCREENED_OUT 2 = 3 findings screened, yielding one distinct stable candidate.

## Review-Domain Summary

Each candidate has one review domain, one primary relationship type and one evidence state. The summaries below each reconcile to one candidate.

| Review domain | Meaning | Candidates |
|---|---|---:|
| statistical_results | Report counts, estimates, intervals, tests or statistical methods | 0 |
| report_internal_inconsistency | Report attribution of a result to an outcome, time, set or comparison | 0 |
| protocol_report | Planned versus reported statistical design or analysis | 1 |
| plan_material | Plan-internal statistical design inconsistency relied on by the report | 0 |
| **Total** | | **1** |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 1 |
| P_P | Within PLAN material | 0 |
| S_C | Between REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| **Total** | | **1** |

C001 also involves S_C; its primary relationship is P_R under `P_R > P_P > S_C > S_W`. The secondary relationship does not add a candidate to the primary-type totals.

| Evidence state | Candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **1** |

Inclusion audits: CONFIRMED 1; QUESTIONED 0. These are inclusion-threshold assessments, with human adjudication pending.

## Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Composite endpoint weighting definitions | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Composite primary endpoint uses different patient and care-opportunity weighting definitions

**Pending Human Adjudication**

**Candidate statement:** The main article explicitly averages patient-specific fulfilled/eligible measure ratios, whereas the prospective protocol defines the composite as total fulfilled interventions divided by total possible interventions among eligible patients. The results supplement repeats the pooled definition and states that the randomized phase used the same endpoint definition. These summaries assign different weights, and all nine Table 2 count pairs yield descriptive pooled percentages distinct from the reported patient means.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** REPORT main article p.3 vs PLAN protocol p.16; REPORT main article p.3 vs REPORT results supplement p.2

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

Checker provenance also includes F-ST1-001 (`root/statistics_1`) and F-ST1-101 (`root/statistics_1_design`), screened as duplicates of C001. The representative INCLUDE originates from `root/cross_source`.

**Classification rationale:** The prospective protocol is PLAN by content. Main article and results supplement are REPORT. The conflicting planned/report primary definition supplies P_R; the supplement's expressly randomized-phase definition also supplies S_C. P_R takes precedence. Opportunity-model paragraphs corroborate a separately modeled odds result and are not additional conflicts.

**Classification ambiguity:** No supplied endpoint-definition amendment is identified. The pooled language might have intended a patient-level average, but no supplied statement expressly reconciles it. This affects interpretation of the wording, rather than the document-role assignment.

**Exact source locations:**

1. REPORT [jama_wang_2018_oi_180070.pdf — PDF p.1, abstract Results](<../jama_wang_2018_oi_180070.pdf#page=1>): repeated composite 88.2% versus 84.8%; difference 3.54% (95% CI 0.68%–6.40%), P=.02. Adjustment is specified in the detailed methods/results and table.
2. REPORT [jama_wang_2018_oi_180070.pdf — PDF p.2, Key Points](<../jama_wang_2018_oi_180070.pdf#page=2>): repeated percentages and composite improvement statement.
3. REPORT [jama_wang_2018_oi_180070.pdf — PDF p.3, Outcomes](<../jama_wang_2018_oi_180070.pdf#page=3>): conflicting main definition, each patient's fulfilled/eligible fraction calculated and averaged.
4. REPORT [jama_wang_2018_oi_180070.pdf — PDF p.4, Data Analysis](<../jama_wang_2018_oi_180070.pdf#page=4>): corroborating opportunity-level binary-observation ORPA method, adjustment and within-hospital correlation context.
5. REPORT [jama_wang_2018_oi_180070.pdf — PDF p.5, primary Results](<../jama_wang_2018_oi_180070.pdf#page=5>): repeated composite means, adjusted difference and ORPA 1.39 (1.12–1.72), P=.003.
6. REPORT [jama_wang_2018_oi_180070.pdf — PDF p.7, Table 2](<../jama_wang_2018_oi_180070.pdf#page=7>): composite mean(SD), all nine fulfilled/eligible pairs, both inference columns and adjustment footnote.
7. PLAN [joi180070supp1_prod.pdf — PDF p.16, printed lines 216–220](<../joi180070supp1_prod.pdf#page=16>): conflicting pooled total-intervention endpoint definition.
8. PLAN [joi180070supp1_prod.pdf — PDF p.18, printed lines 266–274](<../joi180070supp1_prod.pdf#page=18>): corroborating correlation-aware opportunity odds analysis.
9. PLAN [joi180070supp1_prod.pdf — PDF p.19, printed lines 275–279](<../joi180070supp1_prod.pdf#page=19>): corroborating binary-observation example continuing that model description.
10. REPORT [joi180070supp2_prod.pdf — PDF p.2, eAppendix](<../joi180070supp2_prod.pdf#page=2>): conflicting pooled definition expressly identified as the randomized-phase endpoint definition. Baseline 80.2% versus 79.5% is contextual, not compared with randomized percentages.

**Source evidence:** Main p.3 describes fulfilled eligible measures divided by measures for which a given patient was eligible, calculated for each patient and then averaged. PLAN p.16 instead divides total interventions performed among eligible patients by total possible interventions among eligible patients. Results supplement p.2 repeats that operation immediately after its same-randomized-endpoint statement. Main Table 2 labels 88.2 (15.1) and 84.8 (18.2) as mean(SD), not pooled event fractions. The opportunity-model paragraphs separately describe one binary observation per care opportunity and a population-average odds ratio.

**Reported-versus-comparator:** Reported patient composite means are 88.2% and 84.8%. Literal pooled aggregation of the Table 2 fulfilled/eligible counts gives 10699/12064 = 88.6853448276% and 9930/11688 = 84.9589322382%, displaying as 88.7% and 85.0%. The issue compares descriptive endpoint definitions. The adjusted difference 3.54 percentage points (95% CI 0.68–6.40), P=.02, and ORPA 1.39 (1.12–1.72), P=.003, retain their separate modeled labels and are not required to equal crude arithmetic.

**Reasoning procedure:** For patient i, let a_i be fulfilled eligible opportunities and b_i eligible opportunities. The main definition is U=(1/n)Σ(a_i/b_i). The pooled definition is W=Σa_i/Σb_i=Σ[b_i/Σb_j](a_i/b_i). U weights patients equally; W weights their fractions in proportion to eligibility. Sum every Table 2 count pair across the nine measures; repeated patients across measures are intended because the sums count care opportunities. Compare the resulting pooled percentages with the reported mean display intervals and propagate half-unit allowances through every input. Keep descriptive weighting separate from adjusted inference.

**Calculation:**

| Table 2 measure | Intervention fulfilled/eligible | Control fulfilled/eligible |
|---|---|---|
| Intravenous rtPA | 46/212 | 23/204 |
| Early antithrombotics | 2307/2353 | 2253/2330 |
| Dysphagia screening | 2255/2328 | 2040/2139 |
| DVT prophylaxis | 178/645 | 66/592 |
| Discharge antithrombotics | 2272/2324 | 2141/2305 |
| Anticoagulation for atrial fibrillation | 63/155 | 39/137 |
| Lipid-lowering | 1415/1481 | 1439/1547 |
| Antihypertensive medication | 1510/1838 | 1372/1771 |
| Antidiabetic medication | 653/728 | 557/663 |
| **Exact sums** | **10699/12064** | **9930/11688** |

The pooled percentages 88.6853448276% and 84.9589322382% lie outside printed-mean half-unit intervals [88.15%,88.25%) and [84.75%,84.85%). Their gaps above the respective upper bounds are 0.4353448276 and 0.1089322382 percentage points. The integer counts are exact trial quantities; SDs do not enlarge a displayed mean's rounding interval.

For an additionally conservative calculation, allow every numerator and denominator continuously ±0.5, enlarging each nine-row sum by ±4.5. The propagated bounds are:

- Intervention: [100×10694.5/12068.5, 100×10703.5/12059.5] = [88.6149894353%,88.7557527261%].
- Control: [100×9925.5/11692.5, 100×9934.5/11683.5] = [84.8877485568%,85.0301707536%].

Both lower bounds still exceed the reported-mean upper bounds, by 0.3649894353 and 0.0377485568 percentage points. The crude pooled contrast is 3.7264125894 percentage points, a diagnostic consequence of that definition only. It is not an alternative adjusted trial effect. The narrative adjusted difference and its CI reconcile with Table 2's one-decimal 3.5 (0.7–6.4).

**Affected result or extracted value:** The composite co-primary percentages 88.2% versus 84.8%, their patient-average versus opportunity-weighted meaning, and their correspondence with the prespecified endpoint. Extraction of the accompanying adjusted absolute difference requires clarity about its target summary.

**Why context does not resolve it:** The main definition explicitly averages patient fractions; the plan and supplement explicitly divide totals. The supplement states that its definition applies to the randomized phase, preventing a baseline-only explanation. The separately specified opportunity ORPA model explains its own observation unit but supplies no reconciliation of the descriptive endpoint definitions or mapping of the adjusted difference to them. A reader can identify the main report's operation while the planned-and-reported correspondence remains unclear.

**Alternative source-grounded interpretations:** The report may use a patient-average descriptive endpoint where the plan described pooled weighting; alternatively, pooled language in the plan/supplement may intend patient averaging without spelling it out. Neither an endpoint amendment nor an explicit reconciliation selects between these interpretations in the supplied package. No preferred analysis is proposed.

**Mechanical evidence recheck:** The fresh rechecker found all ten cited locations, matched both definitions and every Table 2 pair, confirmed roles and adjustment labels, and reproduced exact sums and conservative display bounds using direct Poppler source extraction and visual page confirmation. No transcription or classification amendment was required, yielding `reproduced`. Necessary inputs are available for the definition comparison and pooled calculation. Participant fractions, joint eligibility, treatment of any zero-opportunity patient and the exact adjusted-difference target/computation are unavailable; the patient mean/SD and an alternative adjusted analysis cannot be independently reconstructed. Full separate facts are in [the mechanical recheck](review_1_6_1/verification/evidence_recheck.md), with inclusion and classification independently assessed in [the quality audit](review_1_6_1/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed, this candidate could affect whether a systematic-review data extractor labels the primary composite as an equal-patient adherence score or a pooled opportunity proportion, and how its accompanying absolute difference is described. The package does not establish downstream propagation, another significance decision or a changed paper-level conclusion.

**Human verification steps:** Read main p.3, PLAN p.16 and results supplement p.2 together; establish whether the pooled wording is literal or shorthand for patient averaging. Verify all nine Table 2 pairs and reproduce sums and display intervals. Distinguish the patient descriptive means, adjusted absolute difference and opportunity-based ORPA. Clarify which aggregation was prespecified and used, how it relates to the adjusted absolute difference, and whether a supplied amendment or clarification reconciles the wording before adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Evidence reuse should preserve each result's endpoint, aggregation unit, eligibility denominator, population, time point, contrast and adjustment label. Patient-average scores, pooled opportunity proportions, adjusted absolute differences and population-average odds ratios represent distinct quantities. A systematic review, meta-analysis or guideline extraction can carry these labels with the source-page references and any human clarification. This review identifies a potential extraction ambiguity; it supplies no evidence that a downstream synthesis used the ambiguous definition or that conclusions changed.

## Limitations and Missing Definitions

All 44 supplied pages are mapped, with no scientific coverage gap. The review uses only supplied PDFs and their source-linked derivatives. Participant records, analysis programs, fitted-model output and event times were not supplied, so reported adjusted analyses cannot be refitted.

Exact test/interval reconstruction is limited by absent numerical standard errors and test statistics, adjusted-difference computational/variance mappings, GEE working-correlation/variance details, clinical Cox cluster/censoring implementation, disability random-effects/link mappings and table-specific tests for safety or mRS-availability comparisons. Sample-size variance and calculation formula are absent. The plan supplies no explicit imputation algorithm, multiplicity rule or numerical interim boundary; missing detail alone was not a candidate.

C001 additionally requires clarification of endpoint weighting and the adjusted-difference target. Aggregate measure totals do not determine participant-specific fractions, joint eligibility, zero-opportunity handling or patient mean(SD). These limits prevent an alternative adjusted estimate or significance claim.

Historical extraction/rendering versions and five missing legacy page images are provenance limits, with their source units completely mapped. Tesseract and Office conversion are unavailable; supplied sources are PDFs covered by native text and visual evidence, so no fallback environment was necessary. Full final limits appear in [limitations.md](review_1_6_1/limitations.md).

## Human Adjudication Checklist

1. Open every linked source location and verify its document role, endpoint, population and result label.
2. Reproduce the candidate's comparison and calculation, including propagated display bounds.
3. Determine whether immediate source context or a documented clarification reconciles the competing definitions.
4. Establish the intended primary composite aggregation and its relation to the adjusted absolute-difference analysis.
5. Decide validity, importance and action independently; record reviewer initials and notes in the blank fields. Retain the stable ID and source-linked record.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

Scientific evidence is confined to this package. Current source/asset identity manifests are [source SHA-256](review_1_6_1/source_hashes_before.sha256) and [reused-asset SHA-256](review_1_6_1/reused_artifact_hashes_before.sha256). The quality audit's checks passed for all three source files and all 65 reused assets, with no source or reusable asset changed. Final coordinator recomputation matches both before manifests byte-for-byte: all three source files and all 65 reused assets pass SHA-256 checks.

Local Linux tooling provides pdfinfo, pdftotext, pdftoppm, pdftocairo and Pandoc. Direct Poppler 25.03.0 and GNU sha256sum 9.7 supplied current PDF inspection and hashing. The recorded probe used the bundled helper with Python 3.13.5; no global installation, GPU or external literature was used. Fallback environment status is NOT_NEEDED, with no environment created. See [tooling_record.md](review_1_6_1/tooling_record.md).

Routing preflight reports PASS: coordinator `gpt-6.1-sol`/`high`; ordinary specialists `gpt-6.1-sol`/`medium`; statistical, screening, recheck and audit specialists `gpt-6.1-sol`/`high`. All ten named presets were verified. Execution mode is INTERACTIVE_CLI, provider CURRENT_SESSION, and coordinator inference PASS. Every actual runtime appears once below, as recorded in [the execution manifest](review_1_6_1/agent_execution_manifest.md).

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact relative to review_1_6_1 |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_map | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_map | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_design_shard | root/statistics_1_design | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_design.md |
| inclusion_screener | root/screen_initial | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_design_shard | root/statistics_2_design | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_design.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility Performance

- **Target basis:** Three PDF-only sources contain 44 unique pages, all backed by source-matched reusable native text and complete coordinate TSV page keys; no Office conversion or fresh OCR is required. Reusable images cover 39 pages with five derivative-image gaps that can be rendered directly if needed. Parallel main/support mapping and parallel numeric/cross-source/statistical pass 1 checks are followed by the required screening, recheck, distinct statistical pass 2, audit and report waves. A 20–35 minute planning range accounts for the reuse advantage and these mandatory waves without limiting scope.
- **Total source units:** 44
- **Fresh-source units:** 0
- **Target elapsed minutes:** 20-35
- **Started UTC:** 2026-10-11T02:52:33Z
- **Finished UTC:** 2026-10-11T03:27:48Z
- **Observed elapsed minutes:** 35.25
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete row-level relationship expansion and independent design shards in both statistical passes, followed by complete screening, source recheck, exclusion audit and report assembly; final mechanical compatibility repair expanded pass-1 grouped references and aligned coverage stage labels.

Local HTML rendering and mechanical validation are outside observed review duration. The coordinator finalizes these exact timing fields immediately after complete Markdown assembly, then renders standalone HTML and validates source coverage, classification/ID equality, screening reconciliation, links, immutable hashes, tooling and routing.
