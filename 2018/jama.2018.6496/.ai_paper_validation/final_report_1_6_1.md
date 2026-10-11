# Quantitative Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication.** This report prepares candidate reporting issues for human review. Classification and evidence-state fields describe the review record; they do not adjudicate validity, importance or action.

## Executive Quality-Control Summary

Complete review of the three supplied PDFs identified **one stable candidate, C001**. The candidate concerns written protocol-versus-report timing definitions for first-attempt duration and the hypoxemia observation window. The protocol uses cuff inflation; the published definitions use blade removal or first-attempt completion. The independently screened and mechanically reproduced comparison could affect the endpoint specification recorded with a reported result in evidence extraction. The supplied material does not establish any changed duration, event count, composite proportion, hazard ratio, implementation or conclusion.

All **49 of 49 physical source pages** were freshly mapped using reusable source-matched extraction assets. Review covered **107 numeric relationships**, **86 statistical relationships**, and **23 cross-source comparison families**. Two distinct fresh high-effort statistical agents completed all 86 statistical relationships. Five checker findings received five independent screening decisions: one INCLUDE and four SCREENED_OUT. The independent quality audit confirmed C001's inclusion and retained every screening decision; no additional finding arose in statistical pass 2 or the audit.

## Package and Reused-Evidence Provenance

The paper is *Effect of Use of a Bougie vs Endotracheal Tube and Stylet on First-Attempt Intubation Success Among Patients With Difficult Airways Undergoing Emergency Intubation*. Direct evidence comprises the following files; page numbers throughout this report mean physical PDF pages.

| Source ID | Actual filename | Content and document role | Physical pages |
|---|---|---|---:|
| DOC-001 | jama_driver_2018_oi_180054.pdf | Main randomized-trial article; REPORT | 11 |
| DOC-002 | joi180054supp1_prod.pdf | BEAM clinical trial protocol, including statistical plan sections; PLAN | 25 |
| DOC-003 | joi180054supp2_prod.pdf | Results supplement; REPORT for results and PLAN for the quoted prospective rule and operational form | 13 |
| Total | Three supplied PDFs | No direct Office or CSV sources; no separate SAP supplied | 49 |

The current [source inventory](review_1_6_1/source_inventory.md) assigns roles by content. In DOC-003, pages 7-13 reproduce a prospective data-collection instrument; page 6 distinguishes a quoted PLAN rule from its REPORT application.

The [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md) records **47 reused assets** from `review_1_5_2/preprocessing/`: three native texts, three layout texts and 41 rendered PNG pages. All were assessed as usable. Every native text and both support layout texts byte-match current direct extraction. The main layout text has only a Figure 2 vertical-axis-title reading-order displacement, resolved by native text and visual evidence. All 41 PNGs byte-match current 200-dpi source rendering. Derivatives aid location and transcription; the supplied PDFs remain authority. Earlier candidate, checker, screening, adjudication and report conclusions were preserved without being used to discover candidates.

## Scope, Complete Coverage, and Exclusions

The review addresses counts and denominators, estimate and test logic, statistical method logic, and planned-versus-reported statistical design under [QUALITY_CONTROL_SCOPE.md](../QUALITY_CONTROL_SCOPE.md). Every source unit was assigned and mapped, including cover, contents, administrative, historical, form and reference pages. Applicable quantities and definitions were reconstructed; non-result content was explicitly recorded.

| Source | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | PDF_PAGE | 25 | 25 | 0 | 25 | COMPLETE |
| DOC-003 | PDF_PAGE | 13 | 13 | 0 | 13 | COMPLETE |
| Total | PDF_PAGE | 49 | 49 | 0 | 49 | COMPLETE |

Reusable coverage and fresh-required coverage partition the 49 units. Zero fresh-required extraction units means that usable extraction already existed, while all pages still received new scientific mapping. The [source coverage](review_1_6_1/source_coverage.md) and [coverage manifest](review_1_6_1/coverage_manifest.md) record complete assignments and durable artifacts.

Rounding and display precision, immediately resolvable notation or wording, model-based quantities compared with crude calculations, conditional or unreported details, peripheral comparisons and out-of-focus observations were screened under the prescribed rules. The review does not extend to broad methodology, clinical practice, novelty, misconduct or raw-data assessment, and proposes no preferred analysis. There was no candidate-count target, ranking or cap.

## Quantitative and Statistical Relationship Coverage

The [main map](review_1_6_1/extraction/main_quantitative_evidence.md) reconstructs 122 internal records across all 11 main pages. The [support map](review_1_6_1/extraction/support_quantitative_evidence.md) reconstructs 45 groups across 25 protocol and 13 supplement pages, including six clustered outcome rows, the overall survival figure, the interim application and the 27-question operational instrument.

| Review component | Complete scope | Durable record |
|---|---|---|
| Numeric review | 107 relationships, including flow, totals, fractions, subsets, matching quantities and effect-measure identity | [Numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) and [numeric checker](review_1_6_1/checkers/numeric_consistency.md) |
| Cross-source review | 23 families, matching outcomes, populations, contrasts, models and applicable plan specifications | [Cross-source checker](review_1_6_1/checkers/cross_source_consistency.md) |
| Statistical pass 1 | All 86 statistical relationships; PASS_1_COMPLETE for each | [Pass 1](review_1_6_1/checkers/statistical_pass_1.md) |
| Statistical pass 2 | All 86 relationships, complete ledger, five decisions and mechanical recheck; PASS_2_COMPLETE for each | [Pass 2](review_1_6_1/checkers/statistical_pass_2.md) |
| Statistical accountability | 86 unique rows with both pass records | [Statistical inventory](review_1_6_1/statistics/relationship_inventory.md) |

Checks included estimate containment, interval ordering and direction, source-established test and model compatibility, statistical-method logic, sample-size inputs, planned populations, missing-data handling, interim, stopping and multiplicity rules, and matched report occurrences. Printed precision was respected using half-unit intervals. Hodges-Lehmann contrasts, Cox hazard ratios and Kaplan-Meier quantities were distinguished from crude summaries. Diagnostic calculations were labelled and did not substitute for an unspecified implementation. No noninferiority or equivalence margin, test statistic, standard error, rate or person-time result was supplied for a corresponding check. Missing inputs limit mechanical reproduction rather than leaving a relationship unreviewed.

The two statistical passes used distinct fresh runtime agents, `root/statistics_1` and `root/statistics_2`, both `gpt-6.1-sol` with high reasoning effort. Pass 2 emitted zero new findings, so a second inclusion screen was not applicable.

## Inclusion Screening Summary

A finding was included only when reproduced from the supplied source, in focus, unresolved by immediate context for a statistically literate reader in the field, and able to bear on interpretation or extraction of a named result or value. A fresh independent screener reread all five findings; the quality auditor subsequently reviewed the decisions in both directions.

| Decision | Reason code | Count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 2 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 1 |
| Total findings screened | All decisions | 5 |

These counts reconcile to the [single screening log](review_1_6_1/screening/inclusion_screen.md): F-XS-001 is INCLUDE and maps to C001; F-ST1-001 is a screened duplicate associated with C001; F-XS-002 and F-ST1-003 are CONTEXT_RESOLVES; F-ST1-002 is CONDITIONAL_OR_UNREPORTED. Thus one included finding and its duplicate association form one candidate. The duplicate's directly stated hypoxemia-window occurrence and all associated locations are retained in C001. The classification Finding IDs field contains only the INCLUDE finding.

Separately, the checkers recorded **72 exclusion records**: numeric 18, cross-source 22, statistical pass 1 15 and statistical pass 2 17. The [quality audit](review_1_6_1/quality/evidence_quality_audit.md) independently audited all 72. These records are distinct from the five findings screened and are not a deduplicated issue count; observations can recur across independent lanes. The cross-source checker's initial hypoxemia-window exclusion is reconciled by the independent screen's inclusion of its direct clauses within the C001 pattern. No additional stable ID or screening repair was required.

## Review-Domain Summary

The four domains describe the content and document relationship of a candidate, without adjudicating it.

| Review domain | Definition | Stable candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests and statistical-method logic within or between REPORT materials | 0 |
| report_internal_inconsistency | REPORT materials conflict about the outcome, time point, population or comparison to which a result belongs | 0 |
| protocol_report | REPORT differs from PLAN in a statistical design or analysis element | 1 |
| plan_material | PLAN is internally inconsistent in a statistical design element relied upon by reported analysis | 0 |
| Total | All four domains | 1 |

| Relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 1 |
| P_P | Within or between PLAN materials | 0 |
| S_C | Between different REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| Total | Primary relationship types | 1 |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 1 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 1 |

Inclusion audit counts are CONFIRMED 1 and QUESTIONED 0. Each summary reconciles to the one-candidate ledger. Relationship precedence is P_R > P_P > S_C > S_W; C001 involves only P_R.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Planned cuff-inflation timing anchors differ from reported first-attempt timing anchors | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Planned cuff-inflation timing anchors differ from reported first-attempt timing anchors

**Pending Human Adjudication.**

**Candidate statement:** The supplied protocol specifies cuff inflation as the stopping event for first-attempt duration and cuff inflation plus one minute as the end of hypoxemia observation. The main report and results supplement specify blade removal for duration and first-attempt completion plus one minute for hypoxemia observation. The package does not reconcile these written endpoint definitions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp. 9-10 vs REPORT main pp. 3, 7, 9 and REPORT results supplement pp. 2-3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Classification rationale:** The conflicting clauses compare prospective protocol PLAN specifications with published main and supplementary REPORT definitions, within focus area D. Both REPORT documents agree. The prospective operational form is PLAN by content but corroborates a procedural attempt boundary without explicitly prescribing an incompatible duration-outcome or oxygen-monitoring endpoint. It therefore adds no P_P; the agreeing reports add no S_C or S_W. P_R is the sole relationship and satisfies precedence. F-ST1-001 is the screened duplicate/pattern association, not an additional INCLUDE finding.

**Classification ambiguity:** None

**Exact source locations:** Every registered comparison and contextual page is retained below, with actual filenames and physical PDF pages.

| Source location and evidence link | Role | Compared statement or contextual function |
|---|---|---|
| [joi180054supp1_prod.pdf — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>), section 2.2, lines 304-317 and 325 | PLAN | Planned duration stop at cuff inflation; oxygen observation ends one minute after cuff inflation; separate hypoxemia uses that definition. Attempt/switch context appears at lines 284-291. |
| [joi180054supp1_prod.pdf — PDF p. 10](<../joi180054supp1_prod.pdf#page=10>), section 3.2, lines 340-347 and 353-354 | PLAN | Repeated cuff-based oxygen stop, 20-second observations and stopwatch measurement according to section 2.2. |
| [jama_driver_2018_oi_180054.pdf — PDF p. 3](<../jama_driver_2018_oi_180054.pdf#page=3>), Measurements and Trial Outcomes | REPORT | Collection through one minute after first-attempt end; duration between blade insertion and removal. |
| [jama_driver_2018_oi_180054.pdf — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>), Table 3, duration/composite rows and footnotes b/c | REPORT | Repeated attempt-completion oxygen window and blade-removal duration; difficult-airway and overall results; distinct successful-only row retained as context. |
| [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>), Table 5, hypoxemia row and footnote b | REPORT | Hypoxemia result with attempt-completion monitoring window and available-waveform qualification. |
| [jama_driver_2018_oi_180054.pdf — PDF p. 1](<../jama_driver_2018_oi_180054.pdf#page=1>), abstract | REPORT | Named duration, hypoxemia and composite secondary outcomes; overall 38 versus 36 seconds and 13% versus 14% hypoxemia. |
| [joi180054supp2_prod.pdf — PDF p. 2](<../joi180054supp2_prod.pdf#page=2>), eTable 1 | REPORT | Matching duration and success-without-hypoxemia arm results in the physician-clustering analysis. |
| [joi180054supp2_prod.pdf — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>), eTable 1 footnotes * and dagger | REPORT | Repeated blade-entry-to-removal duration and attempt-completion oxygen window; analytic explanation. |
| [joi180054supp2_prod.pdf — PDF p. 10](<../joi180054supp2_prod.pdf#page=10>), Attempt 1 instructions above question 13 | PLAN | Operational blade-insertion-to-removal attempt boundary; question 16 separately distinguishes first-device success and switching. |
| [joi180054supp2_prod.pdf — PDF p. 11](<../joi180054supp2_prod.pdf#page=11>), Attempt 2 instructions above question 19 | PLAN | Repeated operational attempt boundary; corroborating context. |
| [jama_driver_2018_oi_180054.pdf — PDF p. 5](<../jama_driver_2018_oi_180054.pdf#page=5>), Secondary Trial Outcomes | REPORT | Distinct difficult-airway and overall time-to-success analyses, and post hoc successful-first-attempt-only duration. |
| [jama_driver_2018_oi_180054.pdf — PDF p. 8](<../jama_driver_2018_oi_180054.pdf#page=8>), Figure 2 and caption | REPORT | Difficult-airway time-to-success context, failed-attempt censoring and disclosed proportional-hazards limitation. |
| [joi180054supp2_prod.pdf — PDF p. 4](<../joi180054supp2_prod.pdf#page=4>), eFigure 1 and caption | REPORT | Overall time-to-success context with the corresponding censoring and proportional-hazards qualification. |

**Source evidence:** Protocol p. 9 defines first-attempt time to intubation from attempt start to ETT cuff inflation with the tube in the trachea. It independently ends hypoxemia observation one minute after cuff inflation; p. 10 repeats and operationalizes these rules. Main p. 3 defines duration from laryngoscope-blade insertion to removal and collection through one minute after first-attempt end. Main Table 3 and supplementary footnotes repeat the duration and oxygen-window definitions; main Table 5 repeats the oxygen window. Hypoxemia thresholds agree: saturation below 90%, or an absolute decrease greater than 10% when starting below 90%. The comparison concerns the stopping event, not that threshold.

**Reported-versus-comparator:** The protocol's cuff-based duration and monitoring stop are compared with the report's blade-based duration and attempt-completion monitoring stop. Main Table 3 and eTable 1 report difficult-airway median durations of 39 (IQR 29-52) versus 40 (27-63) seconds and overall durations of 38 (29-51) versus 36 (25-54) seconds, bougie versus tube/stylet. Composite successes without hypoxemia are 156/191 versus 123/177 in difficult airways and 317/371 versus 282/366 overall. Main Table 5 reports hypoxemia 47/371 (13%) versus 50/364 (14%). The different successful-only medians of 38 versus 34 seconds are explicitly post hoc and belong to another analysis set. The contextual HRs, 1.29 (95% CI 1.04-1.60) in difficult airways and 1.12 (0.97-1.30) overall, are distinct analyses; no changed HR is inferred.

**Reasoning procedure:** Match endpoint names and populations before comparing specifications. Read the protocol outcome definition with its measurement instructions and compare both against main methods and repeated result footnotes. Retain the operational form's attempt boundary as corroborating context, while distinguishing first-device failure/switching from physical blade removal. Check the oxygen window directly from its own clauses rather than extrapolating it from duration. Separate the reproduced written-event comparison from any hypothesis about measurement implementation or patient-level numerical differences.

**Calculation:** Let b be blade entry/attempt start, c cuff inflation, r blade removal and a reported first-attempt completion. Planned duration is c−b; reported duration is r−b; the expressions differ by r−c. Planned oxygen observation ends at c+60 seconds; reported observation ends at a+60 seconds; the expressions differ by a−c. These expressions identify distinct written event anchors. No numerical separation or patient-level identity among a, c and r is established.

Display precision does not resolve named-event definitions. Matching printed whole-second medians have the same half-unit intervals: 38 permits [37.5, 38.5), 36 [35.5, 36.5), 39 [38.5, 39.5) and 40 [39.5, 40.5). The successful-only 34-second median permits [33.5, 34.5) in its distinct subset. No report-versus-report median discrepancy is present. Transcription arithmetic gives 100×47/371=12.66846% and 100×50/364=13.73626%, within the 13% and 14% display intervals. Composite fractions give 81.67539%, 69.49153%, 85.44474% and 77.04918%, within the displayed 82%, 69%, 85% and 77% intervals. These checks establish no additional percentage discrepancy and cannot determine the implemented observation window. No subtraction of marginal medians replaces the stated Hodges-Lehmann estimator.

**Affected result or extracted value:** The endpoint specification accompanying the abstract's overall first-attempt duration of 38 versus 36 seconds, the difficult-airway duration of 39 versus 40 seconds, and the hypoxemia/composite outcomes named above. An extractor needs to distinguish duration to cuff inflation from blade-based attempt duration, and cuff-based from attempt-completion oxygen monitoring.

**Why context does not resolve it:** Each side explicitly and repeatedly defines its stopping event. Immediate context identifies the reported blade-based clock and the planned cuff-based clock but does not equate them or supply an applicable endpoint amendment. The form identifies a procedural attempt boundary without specifying the stopwatch or oxygen stop. Consequently, a reader cannot establish that the published results implement the same written endpoint specification as the protocol merely from the adjacent text. The discrepancy is supported at the definition level without requiring proof of a changed numerical outcome.

**Alternative source-grounded interpretations:** The repeated report definitions and operational form may describe the measurement actually collected. Alternatively, the protocol's cuff-based measurement may have been implemented while the report describes attempt duration. Timing anchors may have coincided in particular cases, or an applicable prospective clarification may reconcile the specifications. The supplied clauses support these bounded possibilities but do not select an implementation, document a change or establish numerical equivalence.

**Mechanical evidence recheck:** A fresh independent rechecker found and visually matched all 13 registered comparison/context pages using exact-source-correspondent 200-dpi renders; direct layout text aided location. The written definitions, comparator values and consistency rule were reproduced, including contextual and display-precision checks. No transcription or location correction was required. Document roles, protocol_report and sole P_R were confirmed; evidence state is reproduced. Necessary inputs are available for the written-definition comparison. Missing inputs are individual blade-entry, device-switch/failure, cuff-inflation, blade-removal and attempt-completion timestamps; actual stopwatch and oxygen-observation stop events; oxygen trajectories and waveform availability; joint outcome/missingness records; and an applicable dated prospective clarification or amendment. Direct observations are the printed clauses and matched values. An operational change, event coincidence or numerical consequence is an inference that remains unestablished. The remaining question is which events generated the reported measurements and whether an applicable clarification reconciles the definitions. Full facts appear in the [recheck](review_1_6_1/verification/evidence_recheck.md); the [independent audit](review_1_6_1/quality/evidence_quality_audit.md) confirmed inclusion and classification.

**Potential downstream evidence impact:** If confirmed by human review, this reporting issue could affect the endpoint definition or monitoring window copied into an evidence table with the reported duration, hypoxemia or composite values. The record supplies no replacement numerical value and establishes no propagation, changed synthesis, changed conclusion or implementation consequence.

**Human verification steps:**

1. Reread protocol sections 2.2 and 3.2 alongside main methods, Table 3/5 footnotes and eTable 1 footnotes on the linked pages.
2. Distinguish physical blade removal, first-device failure/switch and successful cuff inflation; confirm which event stopped the stopwatch and which ended oxygen observation for each reported outcome.
3. Check whether an applicable dated prospective clarification or amendment reconciles the written definitions, and record its scope and source if available.
4. If assessing numerical consequences, obtain the relevant individual timestamps, oxygen observations and waveform/missingness records; do not infer them from group medians, percentages or contextual HRs.
5. Record the human determination in the fields below without treating the review classification as adjudication.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Evidence extraction joins a numerical result to its outcome definition, population, time point and analysis. A confirmed reporting discrepancy can require clarification of that joined record before reuse in a systematic review, meta-analysis or guideline. For C001, the bounded relevance is the timing specification recorded with duration and oxygen-related outcomes. This review establishes neither downstream propagation nor a changed numerical synthesis or paper conclusion. Human adjudication should retain the source citations and the distinction between written definitions and actual measurements.

## Limitations and Missing Definitions

All supplied units and registered relationships were reviewed; no scientific-coverage gap remains. The package does not provide individual timing, ranks, oxygen trajectories, waveforms, actual stopwatch/observation implementation or outcome/missingness cross-classifications. It also lacks exact binary-interval construction, interaction model/link/scale and detailed clustered test/variance procedures. Thus mechanical reproduction cannot impose a common test/interval inversion or infer a patient-level consequence from a written definition discrepancy.

The exact day-level accrual closure and operative trigger, and an applicable dated endpoint clarification or amendment, are not supplied. Stata 12.1 is unavailable locally; the stated sample-size command was corroborated by a labelled continuity-corrected diagnostic, not executed. No separate SAP or raw-data source is supplied.

Eight pages lack a reused image derivative: DOC-001 p. 11 and DOC-002 pp. 1-4 and 23-25. Usable native/layout text and explicit fresh mapping cover them. The main layout reading-order displacement contains no absent content. Missing CPU OCR and Office conversion tools do not affect this native-text PDF package. Existing derivative-generation versions are not independently documented, but current-engine source correspondence is recorded. See the durable [limitations record](review_1_6_1/limitations.md).

## Human Adjudication Checklist

Human review should confirm the cited source statements, consider any applicable clarification, distinguish endpoint wording from actual implementation, and identify any additional records required to assess numerical consequences. For C001, record validity, importance, action, initials and notes in the exact blank fields. Preserve the stable ID, provenance, all locations and evidence-state facts when documenting the human decision. The candidate remains Pending Human Adjudication until that review occurs.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

The current review follows [review_contract.md](../workflow_1_6_1/review_contract.md), [report_spec.md](../workflow_1_6_1/report_spec.md), [settings.toml](../workflow_1_6_1/settings.toml) and [PERFORMANCE_PROFILE.md](../PERFORMANCE_PROFILE.md). The [routing preflight](review_1_6_1/routing_preflight.md) records PASS, Coordinator inference: PASS, ten verified named presets, INTERACTIVE_CLI and Provider: CURRENT_SESSION. No provider configuration was changed.

The [tooling record](review_1_6_1/tooling_record.md) records Linux, Poppler 25.03.0 and Pandoc 3.1.11.1. Direct pdfinfo, pdftotext, pdftoppm, pdftocairo and hashing were available; tesseract and libreoffice were absent. No OCR, Office conversion, GPU, global package installation or fallback environment was needed; fallback environment removed is NOT_CREATED.

The three direct-source hashes and 47 reused-asset hashes are recorded in [source_hashes_before.sha256](review_1_6_1/source_hashes_before.sha256) and [reused_artifact_hashes_before.sha256](review_1_6_1/reused_artifact_hashes_before.sha256). All 50 checks returned OK during the independent audit. After Markdown assembly, final recomputation confirmed that both hash sets are unchanged; [source hashes after review](review_1_6_1/source_hashes_after.sha256) and [reused-asset hashes after review](review_1_6_1/reused_artifact_hashes_after.sha256) byte-match their respective before records. Sources and reused assets were preserved throughout report assembly. Local evidence links name the supplied file and physical page; rendered derivatives serve as provenance only.

### Agent execution

The [execution manifest](review_1_6_1/agent_execution_manifest.md) records the coordinator and 11 distinct fresh specialists, 12 runtime agents in total. Every role uses gpt-6.1-sol. Canonical task names omit their leading slash in this table, consistently with the manifest.

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_source | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistics_1 | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | root/screen_initial | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | root/rechecker | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistics_2 | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/auditor | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | root/reporter | gpt-6.1-sol | medium | FRESH_SPAWN |

No specialist was repurposed for another mandatory stage. Pass 2 emitted no findings, so no pass-2 screener was required. Durable artifacts, complete relationship inventories, screening, recheck, audit and the ledger preserve reproducibility independently of conversational summaries.

### Reproducibility performance

The following exact fields are copied from [run_state.md](review_1_6_1/run_state.md). The coordinator captured completion values immediately after complete Markdown assembly and updated them after the final metadata review; local HTML rendering and mechanical validation are outside the observed review window.

- **Target basis:** Three native-text PDFs contain 49 physical pages: an 11-page main article, a 25-page protocol and a 13-page results/instrument supplement. All 49 pages have source-matched reusable native text and complementary layout text; 41 pages also have reusable visual renders. No fresh extraction, Office conversion or OCR is initially required. The protocol/report comparisons, clustered-results supplement and interim-analysis material require full mapping followed by concurrent checker review, independent screening, mechanical recheck, a distinct second statistical pass, audit and report generation. These mandatory specialist waves support a bounded 20-35 minute planning range.
- **Total source units:** 49
- **Fresh-source units:** 0
- **Target elapsed minutes:** 20-35
- **Started UTC:** 2026-10-11T02:52:26Z
- **Finished UTC:** 2026-10-11T03:24:38Z
- **Observed elapsed minutes:** 32.20
- **Target status:** MET_TARGET
- **Exceedance causes:** None
