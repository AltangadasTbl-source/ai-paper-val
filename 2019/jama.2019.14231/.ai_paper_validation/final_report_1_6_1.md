# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication**

This review prepares source-grounded candidate reporting issues for human assessment. Evidence reproduction and inclusion audit are evidence-record fields; every candidate remains Pending Human Adjudication.

## Executive Quality-Control Summary

The supplied package for *Association of Metabolic Surgery With Major Adverse Cardiovascular Outcomes in Patients With Type 2 Diabetes and Obesity* was reviewed completely. All 39 physical pages of three PDFs were freshly mapped using source-linked reusable extraction. Review covered 77 numeric relationship groups and 50 statistical relationship groups, with two fresh, distinct high-effort statistical passes.

One stable candidate, C001, consolidates five nonfatal endpoint rows in main-article Table 2. The printed eight-year absolute risk differences do not reconcile with the adjacent cumulative incidences under the stated nonsurgical-control-minus-surgery contrast, after full display-precision allowance. The independent inclusion screen retained one finding and consolidated two duplicate findings. Direct-source recheck reproduced all five comparisons; the independent quality auditor confirmed inclusion and classification. The supplied package does not identify which absolute-risk representation should govern extraction. No change to adjusted hazard-ratio significance or the paper's conclusions is established.

## Package and Reused-Evidence Provenance

Document roles follow content. The main article and results supplement are REPORT material; the original protocol and disclosed amendment form one PLAN bundle. The supplied study is a retrospective matched cohort, and its observational design is retained throughout this review.

| Source ID | Supplied source and complete physical scope | Document role | Content |
|---|---|---|---|
| DOC-001 | [jama_aminian_2019_oi_190103.pdf — PDF p. 1](../jama_aminian_2019_oi_190103.pdf#page=1), pp. 1–12 | REPORT | Main article; printed JAMA pp. 1271–1282 |
| DOC-002 | [joi190103supp1_prod.pdf — PDF p. 1](../joi190103supp1_prod.pdf#page=1), pp. 1–20 | REPORT | Definitions, results tables, figures, longitudinal and sensitivity analyses |
| DOC-003 | [joi190103supp2_prod.pdf — PDF p. 1](../joi190103supp2_prod.pdf#page=1), pp. 1–7 | PLAN | Original protocol dated January 6, 2019; amendment dated August 2, 2019 on p. 7 |

The curator inventoried and hash-protected 90 reusable assets: 27 native page texts, 27 normalized page texts, 21 rendered page images, one flow OCR text, one OCR metadata record, four native/layout range files, two preprocessing manifests or engine records, four package/document records, and three source-linked result/location maps. Partial older maps did not restrict discovery. Later source-matched range extraction supplies results-supplement pp. 1–5 and all seven plan pages, closing earlier derivative omissions. Normalized duplicates do not add source units.

The supplied PDFs are the final evidence authority. Reusable derivatives are locators and transcription aids. Fresh confirmation derivatives comprise main-article layout extraction for pp. 1–12 and a direct page 7 rendering, produced with CPU-only Poppler 26.01.0. No new whole-document OCR or Office conversion was needed. Earlier candidate, screening, adjudication and report records were preserved and excluded from scientific discovery. Complete provenance is recorded in [source_inventory.md](review_1_6_1/source_inventory.md) and [evidence_asset_inventory.md](review_1_6_1/evidence_asset_inventory.md).

## Scope, Complete Coverage, and Exclusions

The review examines counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design. Every source unit was included, including definitions, contents, references, original plan and amendment. Reusable extraction availability is distinct from fresh scientific mapping.

| Source | Total units | Reusable units | Fresh-required extraction units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 | 20 | 20 | 0 | 20 | COMPLETE |
| DOC-003 | 7 | 7 | 0 | 7 | COMPLETE |
| **Total** | **39** | **39** | **0** | **39** | **COMPLETE** |

There is no scientific-coverage gap. All supplied pages had usable reusable extraction, so zero fresh-required extraction units does not mean that scientific mapping was omitted. Main and support mappers reconstructed the complete relationships independently of prior selection. See [source_coverage.md](review_1_6_1/source_coverage.md), [coverage_manifest.md](review_1_6_1/coverage_manifest.md), [main quantitative map](review_1_6_1/extraction/main_quantitative_evidence.md), and [support quantitative map](review_1_6_1/extraction/support_quantitative_evidence.md).

Rounding and display precision, obvious notation, immediately resolved wording, model-versus-crude comparisons, assumptions about unreported details, peripheral comparisons, and out-of-focus observations were screened out under the supplied scope. Baseline descriptions and per-time-point contributor counts qualify only if they change a primary or key secondary result, an analysis-population size, or a planned decision rule. The review does not perform a broad clinical, study-design, raw-data or misconduct audit, propose a preferred analysis, or import external literature.

## Quantitative and Statistical Relationship Coverage

The numeric inventory contains 59 main-article groups and 18 support groups: 77 groups with all member rows, cells and panels retained. Checks cover participant flow, partitions and percentages, outcome-specific risk sets, observed event counts, cumulative incidence, person-time rates, repeated results, longitudinal quantities, and effect-measure identity. The numeric reviewer inspected 138 three-column Table 1 count/percentage cells, 24 supplementary medication pairs, 80 risk counts, 120 measurement-availability counts, and the source-linked outcome and intervention displays.

The statistical inventory contains 24 main-article groups and 26 support groups: 50 groups. Coverage includes eight endpoint risk/HR/test families, 48 outcome cumulative-incidence triples, 16 subgroup HR/CI pairs and eight interaction tests, 24 time-varying HR/CI pairs plus repeats, 24 intervention cumulative-incidence triples, 52 longitudinal estimate/CI/P triplets, 16 E-values and 40 comparison HR/CI pairs, 120 graphical sensitivity estimate/CI pairs, and all applicable model, endpoint, population, missing-data, multiplicity and amendment specifications. Group counts are coverage units, not counts of candidates.

| Review stage | Complete scope | Runtime | Completion |
|---|---|---|---|
| Numeric consistency | 77 numeric groups, every member | root/numeric_checker | Complete |
| Cross-source consistency | Matched REPORT/REPORT and PLAN/REPORT relationships; all supplied statistical design elements | root/cross_checker | Complete |
| Statistical pass 1 | All 50 statistical groups and every member | root/statistics_one | 50 PASS_1_COMPLETE records |
| Statistical pass 2 | All 50 groups and every member; complete ledger, screening and source-recheck implications | root/statistics_two | 50 PASS_2_COMPLETE records; no new findings |
| Quality audit | All coverage, three screening decisions, 77 checker-exclusion rows, C001 and its classification | root/quality_audit | Complete; no screening repair or additional finding |

The two statistical passes used distinct fresh gpt-6.1-sol/high agents. Pass 2 revisited the full statistical inventory after the ledger, screen and mechanical recheck existed; it did not re-emit C001. A second-pass inclusion screen was therefore not applicable. See [numeric relationship inventory](review_1_6_1/relationships/numeric_relationship_inventory.md), [statistical relationship inventory](review_1_6_1/statistics/relationship_inventory.md), and [statistical pass 2](review_1_6_1/checkers/statistical_pass_2.md).

Tests were compared only after matching estimand, model, population, time, direction and confidence level. Adjusted Cox HRs, fixed-time Kaplan–Meier risks, bootstrap risk contrasts and cause-specific rates retain their distinct definitions. Diagnostic approximations do not replace fitted analyses. No numerical sample-size/power, noninferiority/equivalence margin, interim boundary or stopping rule was supplied for this available observational cohort; none was invented.

## Inclusion Screening Summary

A finding was included only if reproduced from supplied sources, in focus, unresolved at once by immediate context, and able to change interpretation of a named result or the value taken for evidence extraction. Independent screening reread every cited source location and consolidated the common five-row pattern.

| Screening decision | Findings |
|---|---:|
| INCLUDE — MEETS_THRESHOLD | 1 |
| SCREENED_OUT | 2 |
| **Total findings screened** | **3** |
| **Distinct stable candidates** | **1** |

| Screened-out reason code | Findings |
|---|---:|
| NOT_REPRODUCED | 0 |
| ROUNDING_OR_DISPLAY_PRECISION | 0 |
| NOTATION_OR_TYPOGRAPHY | 0 |
| TERMINOLOGY_OR_WORDING | 0 |
| MODEL_VERSUS_CRUDE | 0 |
| CONTEXT_RESOLVES | 0 |
| CONDITIONAL_OR_UNREPORTED | 0 |
| PERIPHERAL_COMPARISON | 0 |
| OUT_OF_FOCUS | 0 |
| DUPLICATE_OF_INCLUDED | 2 |
| **Total screened out** | **2** |

F-NUM-001 is the included finding for C001. F-XS-001 and F-ST1-001 are screened out as DUPLICATE_OF_INCLUDED, both referencing C001; their locations and provenance remain represented in its evidence card. These counts reconcile to [inclusion_screen.md](review_1_6_1/screening/inclusion_screen.md). The checkers separately recorded 77 self-screened observation rows: 17 numeric, 20 cross-source, 17 statistical pass 1, and 23 statistical pass 2. Those rows have no finding IDs and are distinct from the three independently screened findings. The auditor reconsidered all 77 rows and all three decisions in both directions; no appended candidate or decision change was required.

## Review-Domain Summary

The four review domains distinguish numerical/statistical results (`statistical_results`), ambiguity about which reported outcome/population/time a result belongs to (`report_internal_inconsistency`), planned versus reported statistical design (`protocol_report`), and plan-internal statistical design (`plan_material`). Classification pre-fills human review and is not adjudication.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 1 |
| report_internal_inconsistency | 0 |
| protocol_report | 0 |
| plan_material | 0 |
| **Total** | **1** |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 0 |
| P_P | Within PLAN material | 0 |
| S_C | Between different REPORT documents | 0 |
| S_W | Within one REPORT document | 1 |
| **Total** | | **1** |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **1** |

Inclusion audit: CONFIRMED 1; QUESTIONED 0. C001 has only S_W; supplement corroboration does not add a conflicting S_C relationship. No PLAN location is a conflicting side. All summaries reconcile to the [candidate ledger](review_1_6_1/candidate_ledger.md).

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Five component-outcome eight-year absolute-risk contrasts | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Five nonfatal endpoint absolute eight-year risk differences do not reconcile with the displayed risks

**Status:** Pending Human Adjudication

**Candidate statement:** For heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation, Table 2's absolute eight-year risk differences do not reconcile with the adjacent Kaplan–Meier cumulative incidences under the stated nonsurgical-minus-surgery subtraction, even allowing displayed rounding. One repeated pattern includes all five rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 cumulative-incidence columns vs REPORT main article Table 2 absolute-risk-difference column and footnote a

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Checker provenance:** Numeric reviewer root/numeric_checker emitted F-NUM-001, included by fresh root/inclusion_screen. Cross-source reviewer root/cross_checker independently emitted F-XS-001 and statistical pass 1 reviewer root/statistics_one emitted F-ST1-001; both are screened out as DUPLICATE_OF_INCLUDED and reference C001. Their complete affected locations and estimator context are retained here. The Finding IDs classification field lists the sole INCLUDE finding, as required by the contract.

**Classification rationale:** Both conflicting displays are in the same REPORT main article, making S_W the sole conflicting relationship. REPORT supplement eTable 5 corroborates the marginal risks; corroboration does not add S_C. No PLAN source is a conflicting comparator. Numerical risk-contrast identity belongs to statistical_results rather than result-attribution ambiguity.

**Classification ambiguity:** None

**Exact source locations:**

- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2 heart failure row](../jama_aminian_2019_oi_190103.pdf#page=7): surgical/control incidences, initial risk sets, ARD point and CI.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2 coronary artery disease row](../jama_aminian_2019_oi_190103.pdf#page=7): surgical/control incidences, initial risk sets, ARD point and CI.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2 cerebrovascular disease row](../jama_aminian_2019_oi_190103.pdf#page=7): surgical/control incidences, initial risk sets, ARD point and CI.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2 nephropathy row](../jama_aminian_2019_oi_190103.pdf#page=7): surgical/control incidences, initial risk sets, ARD point and CI.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2 atrial fibrillation row](../jama_aminian_2019_oi_190103.pdf#page=7): surgical/control incidences, initial risk sets, ARD point and CI.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 7, Table 2 headings and footnotes a/b](../jama_aminian_2019_oi_190103.pdf#page=7): eight-year column definitions, control-minus-surgery direction, bootstrap intervals, and separate Cox adjustment.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 4, Statistical Analysis](../jama_aminian_2019_oi_190103.pdf#page=4): eight-year Kaplan–Meier cumulative incidence and absolute-risk differences, percentile bootstrap intervals from 1000 iterations, separate fully adjusted Cox models.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 1, abstract](../jama_aminian_2019_oi_190103.pdf#page=1): all seven prespecified secondary outcomes are reported, establishing the affected component endpoints as key secondary for this review.
- [jama_aminian_2019_oi_190103.pdf — PDF p. 8, Figure 3 panels B–F and caption](../jama_aminian_2019_oi_190103.pdf#page=8): corresponding outcome curves and individual risk-set rules; no separate ARD population is specified.
- [joi190103supp1_prod.pdf — PDF p. 7, eTable 5 Year 8 rows](../joi190103supp1_prod.pdf#page=7): all corresponding marginal risks/CIs corroborate the incidence side. This is supplementary corroboration, not an additional conflicting relationship.

**Source evidence:** Table 2 labels the absolute eight-year risk difference and footnote a defines nonsurgical control minus metabolic surgery. Footnote b assigns adjustment to Cox HRs and P values. Source-matched direct layout text and direct page 7 rendering agree; independent inclusion screening reread all cited source locations.

**Reported-versus-comparator:** All incidence and contrast values below are percentage points at eight years. The reported CIs remain source values; no CI is inferred by subtracting marginal limits.

| Outcome | Surgery/control initial risk sets | Surgical risk % | Control risk % | Printed ARD (95% CI) | Difference of displayed risks | Allowable subtraction interval | Allowable printed ARD interval |
|---|---|---:|---:|---|---:|---|---|
| Heart failure | 2049/10093 | 6.8 | 18.9 | 12.9 (10.4–15.1) | 12.1 | 12.00–12.20 | 12.85–12.95 |
| Coronary artery disease | 2050/10331 | 7.9 | 11.6 | 4.2 (1.9–6.8) | 3.7 | 3.60–3.80 | 4.15–4.25 |
| Cerebrovascular disease | 2245/11077 | 4.1 | 5.6 | 1.8 (−0.03–3.4) | 1.5 | 1.40–1.60 | 1.75–1.85 |
| Nephropathy | 1937/9190 | 6.1 | 16.3 | 11.1 (8.8–13.6) | 10.2 | 10.10–10.30 | 11.05–11.15 |
| Atrial fibrillation | 2135/10734 | 7.9 | 13.6 | 6.5 (4.4–8.7) | 5.7 | 5.60–5.80 | 6.45–6.55 |

**Reasoning procedure:** Match each row's endpoint, eight-year time, risk set and group direction. Read the absolute-risk subtraction rule in footnote a and the separate Cox adjustment in footnote b. Apply half-unit rounding intervals before comparing point contrasts. Check the methods and repeated marginal risks for an immediately stated alternate point estimator. Consolidate the common rule/pattern across the five rows.

**Calculation:** Each one-decimal risk and ARD allows ±0.05 percentage points. The difference of the two risks allows ±0.10 around the displayed subtraction; the reported ARD allows ±0.05. All five resulting interval pairs are disjoint. The primary composite, secondary composite and mortality rows reconcile under the same subtraction rule. No modeled HR is compared to a crude ratio, and no original model variance is reconstructed.

Every printed ARD point lies inside its own reported interval. Those intervals are not independently shown to fail and are not reassigned to the subtraction comparators.

**Affected result or extracted value:** The eight-year absolute risk differences and associated reported bootstrap uncertainty for the five named component outcomes. A data extractor can obtain distinct points by copying the ARD column or subtracting the reported risks.

**Why context does not resolve it:** The same outcome/time/risk-set labels and explicit subtraction direction provide two nonreconciling representations. The package describes bootstrapping for intervals and adjustment for HRs, but does not identify a distinct adjusted-risk, bootstrap-point-summary, population or censoring definition for these ARD points. A reader cannot select the intended extracted risk difference at once from those displays.

**Alternative source-grounded interpretations:** The ARDs may derive from a distinct, unstated risk point-estimation procedure or population; alternatively, the displayed marginal risks and contrast need reconciliation against the original analysis output. The supplied package establishes neither explanation. Outcome-or-death rates in eTable 4 are a separately defined person-time measure and do not establish an alternative eight-year risk contrast.

**Mechanical evidence recheck:** Fresh root/evidence_recheck independently found all cited source and comparator locations, matched every printed value and rule, reproduced all five disjoint half-unit interval comparisons, and confirmed statistical_results/S_W with evidence state reproduced. No transcription correction or classification change was needed. Original ARD point estimator and analysis inputs remain unavailable; see the [complete evidence recheck](review_1_6_1/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed by human review, a systematic reviewer or data extractor could carry different absolute association estimates for these five outcomes depending on which Table 2 columns are used. No propagation, paper-level conclusion change, or change to adjusted HR significance is asserted.

**Human verification steps:** Confirm the five rows/footnote against the supplied PDF; identify the original eight-year group risks, the point estimator and analysis population used for each ARD; establish whether the risk and contrast columns share the same estimand; reconcile the associated bootstrap intervals once the estimand is identified. The displayed subtractions are comparators, not suggested final corrections.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

Fresh quality auditor root/quality_audit confirms the inclusion threshold and classification for C001, with no screening repair or additional candidate. Every five-row occurrence remains one stable candidate; human adjudication remains pending.

## Downstream Evidence-Chain Considerations

Evidence extraction should retain the outcome, time horizon, population, direction, effect measure and uncertainty definition attached to a number. C001 presents two distinct representations of five eight-year absolute associations. If human review confirms that reconciliation is required, an extractor using the labeled ARD column could take different points from an extractor subtracting the adjacent cumulative incidences. The supplied bootstrap intervals remain associated with the printed points until their estimand is established; they must not be reassigned to the subtraction comparators on this review's authority.

This is potential downstream relevance, not evidence that propagation, a meta-analysis change, a guideline change or clinical harm occurred. No alternative point is endorsed, and no change in adjusted Cox inference or the paper-level conclusions is asserted.

## Limitations and Missing Definitions

All 39 source pages, all 77 numeric groups and all 50 statistical groups have complete scientific coverage. No source access or direct-tool limitation remains. Reconstruction limits are separate from source-coverage gaps.

- Some reusable native-text extraction and page-rendering engine versions were not recorded. Source identity, SHA-256 matching and current source-text comparisons establish their fitness as locators; direct supplied pages controlled candidate confirmation. Fresh main-article derivatives use Poppler 26.01.0.
- Exact unannotated graphical trajectories and sensitivity points were not digitized. All panels were mapped by outcome, scale, time, direction, confidence display and source keys, with printed/annotated values retained.
- Raw data, event/censoring histories, person-time totals, fitted-model outputs, numerical pooled Cox standard errors, coefficient-test identity, degrees of freedom, imputation-model details and subgroup interaction covariance are unavailable. They limit independent reconstruction of fits and tests.
- Medication numerator counts and exact confidence-interval/test routines, longitudinal covariance/variance estimator and degrees of freedom, and detailed time-spline implementation are not supplied. Missing detail alone does not establish an analysis contradiction.
- The HR-to-risk-ratio conversion formula and inputs for E-value regeneration are absent. No external formula was assumed.
- C001 lacks the original unrounded risks, ARD point-estimation output/operation, any distinct risk-set or censoring specification, and bootstrap replicates. These inputs are needed to identify the intended final extraction value and reconcile its associated uncertainty. Their absence does not prevent the printed-value and display-precision comparisons.

The consolidated durable record is [limitations.md](review_1_6_1/limitations.md). This review is limited to the supplied package and the defined quantitative reporting scope; it does not verify raw-data implementation or causal interpretation.

## Human Adjudication Checklist

For C001, inspect all five Table 2 rows, the adjacent risk columns, footnote a and the eight-year methods definition. Obtain or identify the original point estimator, unrounded group risks, population and event/censoring rules. Establish whether the incidence and contrast columns share an estimand, then reconcile the associated bootstrap output. Keep adjusted HR tests distinct from fixed-time risk contrasts. Record validity, importance, action, initials and notes in the five blank fields on the card. Every stable ID remains Pending Human Adjudication until the human review is recorded.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Source integrity and tooling

The package-only review used direct local tools with CPU processing. The recorded probe found pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract, libreoffice and pandoc available. No fallback environment was created, and no global packages were installed. See [tooling_record.md](review_1_6_1/tooling_record.md).

The initial SHA-256 manifests cover all three supplied sources and all 90 reused assets: [source hashes before](review_1_6_1/source_hashes_before.sha256) and [reused artifact hashes before](review_1_6_1/reused_artifact_hashes_before.sha256). The quality auditor's independent hash checks matched both initial manifests. After Markdown assembly, the coordinator recomputed [source hashes after](review_1_6_1/source_hashes_after.sha256) and [reused artifact hashes after](review_1_6_1/reused_artifact_hashes_after.sha256); both are identical to the initial manifests. Sources and reused assets were preserved. Standalone HTML rendering and mechanical validation use the supplied workflow scripts, with the validation result recorded in `review_1_6_1/review_validation.json`. Local rendering and validation are outside the review timing window.

### Agent execution

Routing preflight is PASS, with Coordinator inference PASS, ten named presets verified, execution mode INTERACTIVE_CLI and Provider CURRENT_SESSION. Every actual runtime appears below; the coordinator used the current session and all 11 mandatory specialists were fresh distinct spawns. All roles use the fixed exact model gpt-6.1-sol. No provider configuration or authentication change was made. Canonical runtime names are recorded without the leading slash. The two statistical passes have distinct runtime IDs and high reasoning effort.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |


The primary artifact paths in the execution table are relative to review_1_6_1. Full stage and evidence assignments are recorded in [agent_execution_manifest.md](review_1_6_1/agent_execution_manifest.md) and [coverage_manifest.md](review_1_6_1/coverage_manifest.md). The report generator writes both this report and the consolidated limitations artifact. A second-pass screen was not applicable because pass 2 emitted no new finding.

### Reproducibility performance

- **Target basis:** Three native-text PDFs contain 39 total physical pages and 0 pages lacking usable reusable extraction. The main observational matched-cohort report has participant flow, tables and multicomponent outcome figures; the 20-page results supplement adds Cox models, longitudinal displays and sensitivity analyses, and the 7-page plan bundle contains an original protocol plus amendment. Twenty-one existing page images and one flow OCR aid visual checks. No Office conversion or new whole-document OCR is needed. Two mapping agents can cover the disjoint source scopes in one concurrent wave, followed by parallel numeric/cross-source/statistical review and the mandatory sequential screening, recheck, second statistical pass, audit and report stages. A 22-35 minute target allows these waves and targeted confirmations without limiting findings.
- **Total source units:** 39
- **Fresh-source units:** 0
- **Target elapsed minutes:** 22-35
- **Started UTC:** 2026-10-11T02:45:53Z
- **Finished UTC:** 2026-10-11T03:15:37Z
- **Observed elapsed minutes:** 29.73
- **Target status:** MET_TARGET
- **Exceedance causes:** None

The planning range is package-specific and never restricts coverage or candidate count. Finish and observed-duration fields are finalized and identical to run_state.md. All 39 source units, 77 numeric groups, 50 statistical groups in both passes, three screening decisions and C001's complete evidence record are covered. Source and reused-asset integrity checks are unchanged. Standalone HTML rendering, tooling finalization and mechanical validation follow report assembly.
