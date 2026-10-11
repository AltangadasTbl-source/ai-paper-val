# Quantitative Quality-Control Consistency Review — jama.2018.9128

**Pending Human Adjudication**

Workflow 1.6.1. Every candidate below requires human review. Classification, evidence state and inclusion audit describe the review record; they do not supply a human adjudication.

## Executive Quality-Control Summary

Complete review of three supplied PDFs, comprising 132 physical pages, identified **2 stable candidate reporting issues**. Both concern planned-versus-reported contact duration and belong to `protocol_report`. C001 compares intensive telephone sessions described as 90 minutes in the article with 20 minutes in the revised protocol. C002 compares six shared school-readiness activities described as 30 minutes each with six 45-minute sessions in the revised design.

Independent inclusion screening evaluated five checker findings: two included representatives and three duplicate findings consolidated into the same two candidates. Exact-source mechanical recheck reproduced both comparisons, and the independent quality-control auditor recorded `CONFIRMED` inclusion for both. Neither comparison demonstrates a changed BMI effect estimate, altered trial conclusion or actual received intervention dose. The unresolved quantities could affect intervention-description extraction if human review confirms the candidates.

## Package and Reused-Evidence Provenance

The main article reports the randomized trial *Effect of a Behavioral Intervention for Underserved Preschool-Age Children on Change in Body Mass Index*. Document roles were assigned from content: the main article and results supplement are `REPORT`; the original/revised protocol, amendments and original/final SAP in the first supplement are `PLAN`.

| Source ID | Supplied filename | Role | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_barkin_2018_oi_180075.pdf](../jama_barkin_2018_oi_180075.pdf#page=1) | REPORT | 11 |
| DOC-002 | [joi180075supp1_prod.pdf](../joi180075supp1_prod.pdf#page=1) | PLAN | 113 |
| DOC-003 | [joi180075supp2_prod.pdf](../joi180075supp2_prod.pdf#page=1) | REPORT | 8 |
| Total | Three direct sources | | 132 |

The review reused 71 preserved files from the earlier preprocessing area: three native-text files, three layout-text files, eight OCR files, 54 rendered pages and three PDF metadata files. Native text byte-matches current direct extraction. Legacy generation-engine versions were unrecorded; source-content comparisons and current hashes establish the documented reuse basis. Existing OCR and extracted text aid location and transcription; exact supplied pages govern candidate evidence. Earlier candidate selections, screening decisions, classifications and final reports were excluded from discovery inputs.

The [source inventory](review_1_6_1/source_inventory.md) and [evidence asset inventory](review_1_6_1/evidence_asset_inventory.md) record source roles, unit coverage, asset fitness and derivative engines. The [before-source hashes](review_1_6_1/source_hashes_before.sha256) and [before-reuse hashes](review_1_6_1/reused_artifact_hashes_before.sha256) identify every protected input.

## Scope, Complete Coverage, and Exclusions

Review covered counts and denominators, estimate and test logic, statistical method logic, and planned-versus-reported statistical design under the supplied Workflow 1.6.1 scope. Every direct-source page, including sparse pages, embedded diagrams, figures, tables, plan versions and amendments, has an explicit mapping assignment. Reuse did not bound scientific coverage.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | 113 | 109 | 4 | 113 | COMPLETE |
| DOC-003 | 8 | 8 | 0 | 8 | COMPLETE |
| Total | 132 | 128 | 4 | 132 | COMPLETE |

The fresh-required units were PLAN pages 13, 54, 63 and 67, where native/layout text did not fully represent diagrams or encoded content. Direct CPU rendering and visual reading closed all four gaps. Additional targeted source confirmations did not add fresh-required units. The authoritative [source coverage](review_1_6_1/source_coverage.md), [coverage manifest](review_1_6_1/coverage_manifest.md), [main evidence map](review_1_6_1/extraction/main_quantitative_evidence.md) and [support evidence map](review_1_6_1/extraction/support_quantitative_evidence.md) document complete coverage.

Rounding and display precision, immediately resolvable notation or wording, model-based estimates compared with crude recomputations, conditional or merely unreported details, peripheral comparisons and out-of-focus observations were excluded under the supplied criteria. The review does not assess general clinical design, novelty, misconduct or raw participant data and does not prescribe an analysis. No expected candidate count or stopping cap was used.

## Quantitative and Statistical Relationship Coverage

The rebuilt [numeric relationship inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) contains **168 numeric groups**, retaining all component values and mapping crosswalks. The initial full numeric review exceeded the configured 120-relationship context bound. Two additional fresh medium-effort agents completed disjoint N001–N084 and N085–N168 scopes, 84 groups each. Their full results were merged with the preserved initial review. No relationship, finding or exclusion was dropped.

The [statistical relationship inventory](review_1_6_1/statistics/relationship_inventory.md) contains **116 relationships**, S001–S116. Each has explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records from distinct fresh high-effort agents. Both passes covered all relationships, including 72 printed estimate/interval/P rows, nine complete Benjamini–Hochberg families, primary and secondary model definitions, sample-size inputs, missing-data descriptions, decision rules, report-plan matching and the two registered duration comparisons. Named missing inputs bound exact mechanical reconstruction and are recorded rather than replaced with assumptions.

The [numeric checker](review_1_6_1/checkers/numeric_consistency.md), [cross-source checker](review_1_6_1/checkers/cross_source_consistency.md), [statistical pass 1](review_1_6_1/checkers/statistical_pass_1.md) and [statistical pass 2](review_1_6_1/checkers/statistical_pass_2.md) document completed reasoning and self-screening. Pass 2 revisited the complete ledger, screening record and exact-source recheck, emitted no new findings and therefore required no pass-2 inclusion screener. The [quality audit](review_1_6_1/quality/evidence_quality_audit.md) reviewed every stable ID, screening decision, checker exclusion, source-coverage row and classification.

## Inclusion Screening Summary

An included finding must be reproduced from supplied source evidence, fall within scope, remain unresolved at once by a statistically literate reader in the field from immediate context, and plausibly affect interpretation or extraction of a named result or value. The independent screen applied all four criteria. Five findings received exactly one decision each in the [screening log](review_1_6_1/screening/inclusion_screen.md).

| Decision | Reason code | Finding count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 2 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 3 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| Total | All finding decisions | 5 |

Included F-XS-001 maps to C001; included F-NUM-001 maps to C002. F-ST1-001 is a duplicate of C001; F-XS-002 and F-ST1-002 are duplicates of C002. Their provenance and locations remain represented in the evidence records without additional cards. The quality audit recorded no screening reversal or added finding.

Checker self-screening also produced **127 excluded-observation rows**, separately auditable in six artifacts. These are reviewer observations, potentially repeated across independent scopes, and are distinct from the five formally screened finding decisions above.

| Checker scope | Excluded-observation rows |
|---|---:|
| Preserved initial numeric review | 20 |
| Numeric repair N001–N084 | 25 |
| Numeric repair N085–N168 | 14 |
| Cross-source review | 24 |
| Statistical pass 1 | 22 |
| Statistical pass 2 | 22 |
| Total | 127 |

The auditor independently considered exclusion decisions in both directions and found no additional observation meeting all four inclusion requirements. Reason-code zero counts in the finding table do not imply absence of corresponding checker observations.

## Review-Domain Summary

`statistical_results` covers report-material counts, estimates, intervals, tests and statistical methods. `report_internal_inconsistency` covers conflicting attribution of a reported number to an outcome, time point, population or comparison. `protocol_report` covers report-versus-plan statistical design, endpoint, analysis or randomized intervention elements. `plan_material` covers plan-internal statistical design elements on which reported analysis relies.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 0 |
| report_internal_inconsistency | 0 |
| protocol_report | 2 |
| plan_material | 0 |
| Total | 2 |

| Relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 2 |
| P_P | Within PLAN material | 0 |
| S_C | Between REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| Total | | 2 |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 2 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 2 |

Both candidates have `All relationships: P_R` and inclusion audit `CONFIRMED`. A corroborating plan location or earlier version supplies context without adding a conflicting relationship. The precedence rule P_R > P_P > S_C > S_W therefore selects P_R without a mixed-type decision. All three count summaries reconcile to the two stable IDs.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Intensive telephone-session duration | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Shared school-readiness session duration | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

Every stable ID from the [candidate ledger](review_1_6_1/candidate_ledger.md) is included below in stable-ID order. All cards are **Pending Human Adjudication**. Classification values are copied exactly from the finalized ledger classification table; the five human fields remain blank for human completion.

## C001 — Intensive telephone-session duration

**Pending Human Adjudication**


**Candidate statement:** The report assigns 90 minutes to intensive-phase sessions delivered by in-person groups or telephone calls; the revised protocol assigns 20 minutes to the telephone alternative. The applicable telephone-session duration does not reconcile across the supplied descriptions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article p2 vs PLAN revised protocol p64

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Classification rationale:** The main article reports trial delivery; the revised protocol specifies prospective delivery. The conflicting comparison is REPORT versus PLAN, so P_R and protocol_report apply. The plan's 90-minute in-person specification corroborates the delivery-mode distinction and does not create a plan-internal relationship.

**Classification ambiguity:** None

**Exact source locations:** Decisive: [DOC-001 main article — PDF p2, Intervention Description](../jama_barkin_2018_oi_180075.pdf#page=2); [DOC-002 revised protocol — PDF p64, lines 2393–2398](../joi180075supp1_prod.pdf#page=64). Corroborating delivery-mode context: [DOC-002 — PDF p63, lines 2381–2384](../joi180075supp1_prod.pdf#page=63). Supplied amendment context: [DOC-002 — PDF p106](../joi180075supp1_prod.pdf#page=106), [p107](../joi180075supp1_prod.pdf#page=107), and [p113](../joi180075supp1_prod.pdf#page=113). Each location is physical PDF indexing.

**Source evidence:** The report describes weekly “90-minute skills-building sessions via either in-person groups or telephone calls” in the 12-week intensive phase. The revised protocol says the intensive telephone sessions “will be 20 minutes in length” because group discussion, hands-on child activities and cooking are omitted. Its in-person schedule specifies 90 minutes. The supplied, selective amendment summary allows intensive-phase makeup calls without supplying a changed telephone duration; the final SAP summary addresses statistical revisions. The package does not establish whether an unlisted dose amendment occurred.

**Reported-versus-comparator:** REPORT intensive telephone alternative: 90 minutes/session. PLAN matched alternative: 20 minutes/session. Maintenance coaching calls are a separate component.

**Reasoning procedure:** Match program phase, randomized arm, delivery mode and per-session quantity. Read the report sentence and revised protocol paragraph together with the design diagram and amendment context. Keep in-person and maintenance contacts separate. Do not infer actual received telephone minutes.

**Calculation:** 90 − 20 = 70 minutes/session; 90/20 = 4.5. Even conservative whole-minute display intervals [89.5, 90.5] and [19.5, 20.5] are disjoint. A cumulative telephone total is not established because the number of telephone-delivered sessions is unavailable.

**Affected result or extracted value:** Intensive telephone-contact duration used to characterize the behavioral intervention accompanying the primary 36-month child BMI trajectory comparison (joint P=.39). An intervention data extractor could take 90 or 20 minutes per telephone session.

**Why context does not resolve it:** The report explicitly applies its duration to either delivery mode, while the revised plan expressly gives a shorter telephone alternative and a content rationale. The supplied passages do not establish a revised 90-minute call or state that the report's duration applies only to in-person sessions. A field reader cannot select the applicable telephone dose at once.

**Alternative source-grounded interpretations:** The report may compress the in-person duration and shorter telephone substitute into one description, or delivery may have changed after the supplied protocol. Neither interpretation is established. The applicable telephone-session duration or a superseding amendment is the remaining missing definition.

**Mechanical evidence recheck:** Every listed decisive, corroborating and contextual location was found and read directly. Source statements, matching rule, 70-minute per-session difference and disjoint display intervals reproduce. Roles and P_R/protocol_report classification are confirmed; evidence state reproduced. Delivered telephone minutes and any superseding definition remain unavailable. See [the exact-source recheck](review_1_6_1/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If the candidate is confirmed in human review, intervention-description extraction could copy a different per-call contact duration. No change in the reported BMI estimate, trial conclusion or actual received exposure is demonstrated.

**Human verification steps:** Read the linked intervention descriptions and amendment entries; determine what duration applies to intensive telephone sessions and whether a supplied version or component definition reconciles the statements. Keep scheduled and received contact separate.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

Checker provenance retained: included F-XS-001 (cross-source reviewer); independently reproduced duplicate F-ST1-001 (statistical pass 1), screened DUPLICATE_OF_INCLUDED and linked to C001. Statistical relationship S110. No duplicate receives another stable candidate ID.

## C002 — Shared school-readiness session duration

**Pending Human Adjudication**


**Candidate statement:** The report describes six 30-minute shared school-readiness activities; the revised protocol's matched six-session diagram and narrative specify 45-minute sessions. The shared component's per-session duration does not reconcile across the supplied descriptions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article p3 vs PLAN revised protocol pp63–64

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Classification rationale:** The report's trial-delivery description conflicts with prospective revised protocol content. The primary and only conflicting relationship is P_R, requiring protocol_report. Earlier protocol versions and optional later visits supply context; they are not independent plan-internal conflicts in this candidate.

**Classification ambiguity:** None

**Exact source locations:** Decisive: [DOC-001 main article — PDF p3, control-condition paragraph](../jama_barkin_2018_oi_180075.pdf#page=3); [DOC-002 revised protocol — PDF p63, control box and shared-content footnote](../joi180075supp1_prod.pdf#page=63); [DOC-002 — PDF p64, lines 2407–2422](../joi180075supp1_prod.pdf#page=64). Optional follow-up context: [DOC-002 — PDF p65](../joi180075supp1_prod.pdf#page=65). Earlier version context: [DOC-002 — PDF p13](../joi180075supp1_prod.pdf#page=13), [p14](../joi180075supp1_prod.pdf#page=14), [p15](../joi180075supp1_prod.pdf#page=15). Amendment context: [DOC-002 — PDF p106](../joi180075supp1_prod.pdf#page=106), [p107](../joi180075supp1_prod.pdf#page=107), [p113](../joi180075supp1_prod.pdf#page=113).

**Source evidence:** The report says the school-readiness curriculum consisted of “six 30-minute group-based activities” delivered concurrently with data collection and received by both arms. The revised design diagram states six 45-minute control sessions and gives the intervention arm the control content as well. The revised narrative describes a 45-minute school-readiness/school-success program for both arms. It also mentions a later collection point; optional extension context separates it from the six core visits through 36 months.

**Reported-versus-comparator:** REPORT shared school-readiness component: six × 30 minutes. PLAN matched core diagram: six × 45 minutes; revised narrative corroborates 45 minutes per session.

**Reasoning procedure:** Match the school-readiness component, both randomized arms, per-session contact duration and six core contacts through 36 months. Separate the original 12-session/60-minute version and optional later follow-up from the revised core schedule. Read amendment context for a supplied duration change or component distinction.

**Calculation:** 45 − 30 = 15 minutes/session. Six matched scheduled contacts yield 6 × 45 = 270 versus 6 × 30 = 180 minutes, differing by 90 minutes. Whole-minute intervals [44.5, 45.5] and [29.5, 30.5] do not overlap; six-session intervals [267, 273] and [177, 183] also do not overlap. These totals are nominal scheduled contacts, not attendance-weighted received exposure.

**Affected result or extracted value:** Shared comparator/co-intervention contact duration accompanying the primary 36-month BMI trajectory and key secondary dietary/community-use comparisons: 30 versus 45 minutes per session, or 180 versus 270 scheduled core minutes.

**Why context does not resolve it:** The report and revised diagram identify the same shared school-readiness curriculum and agree on six core sessions, but give different durations. Optional seventh/later visits cannot reconcile the per-session difference. The supplied amendment entries do not define a shortened session or distinguish 30 minutes of activities from 45 minutes of scheduled contact. Their selective summary does not exclude an unlisted change.

**Alternative source-grounded interpretations:** Delivered sessions may have been shortened, or the report may describe a narrower component within a 45-minute session. The package does not establish either explanation or the applicable planned/delivered duration distinction. No implementation claim follows from the discrepancy alone.

**Mechanical evidence recheck:** Every listed decisive, corroborating and contextual location was found and read directly. The six 30-minute versus six 45-minute descriptions, 15-minute per-session difference, 180/270-minute nominal core totals and disjoint display intervals reproduce. Roles and P_R/protocol_report classification are confirmed; evidence state reproduced. Actual delivery, any component-time distinction and an unlisted amendment remain unavailable. See [the exact-source recheck](review_1_6_1/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed in human review, an intervention data extractor could record a different shared-session duration and nominal scheduled total. No changed primary effect estimate, conclusion or observed received dose is demonstrated.

**Human verification steps:** Read the report, revised diagram and revised narrative; establish which scheduled and delivered contact duration applies, and whether a supplied amendment or component definition reconciles 30 and 45 minutes. Keep optional extension contacts and observed attendance percentages separate.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

Checker provenance retained: included F-NUM-001 (numeric reviewer); independently reproduced duplicates F-XS-002 (cross-source reviewer) and F-ST1-002 (statistical pass 1), each screened DUPLICATE_OF_INCLUDED and linked to C002. Statistical relationship S111. No duplicate receives another stable ID.

## Downstream Evidence-Chain Considerations

Intervention descriptions can accompany effect estimates in systematic reviews, meta-analyses or guideline evidence tables. If human review confirms either candidate, a data extractor could select a different scheduled contact duration or nominal core total when describing the trial's behavioral and shared school-readiness components. Evidence extraction should retain the source, delivery mode, phase, session-count definition and distinction between scheduled and received contact.

The observed discrepancies do not establish propagation into another evidence product, a changed statistical conclusion, an implementation departure or actual exposure received by participants. They provide bounded questions about which duration description applies. The reported primary comparison and secondary quantities should retain their stated models and analysis populations while the contact-duration questions are adjudicated.

## Limitations and Missing Definitions

All 132 supplied pages are mapped, and all assigned numeric and statistical relationships are reviewed. Four embedded-content extraction gaps were closed by fresh visual mapping. Missing Tesseract and Office-conversion tools affected no remaining source unit; no new OCR, conversion or fallback installation was needed. Legacy extraction-engine versions were unavailable, while current source matching and hashes document reuse fitness. New derivatives use recorded direct CPU Poppler 25.03.0.

The package does not supply individual data, exact unlabeled graph coordinates, all joint-test covariance and coefficient-test implementation details, certain interval-construction procedures, full power-software settings and longitudinal variance inputs, calorie-moderator scaling, or all auxiliary/sensitivity outputs. These limit independent numerical reconstruction; missing details alone were not treated as qualifying contradictions.

Actual intensive telephone-call lengths, numbers of telephone-delivered sessions and attendance by mode are unavailable. The shared component's activity-versus-session time definition and measured delivered session lengths are also unavailable. Calculated totals concern six nominal scheduled core contacts and exclude optional extension visits. Neither attendance-weighted exposure nor altered BMI results follow from those calculations.

The supplied amendment summary is selective. Its listed entries do not reconcile the printed durations, but cannot establish that no unlisted amendment or delivery change occurred. The alternatives remain explicit in both cards and require human clarification. The numeric scope-bound repair and snapshot-link repair are documented operational closures, with all scientific content preserved. The complete [limitations record](review_1_6_1/limitations.md) retains these boundaries.

## Human Adjudication Checklist

For each stable ID, read every decisive, corroborating and contextual source location and confirm the matched phase, delivery mode, curriculum, session quantity and source version. Distinguish scheduled contact from received dose and assess whether a supplied component definition or amendment reconciles the competing statements. Check the reproduced arithmetic and display intervals against those definitions.

Review the candidate's classification and evidence state independently of its inclusion audit. Determine the appropriate human validity, importance and action, then enter initials and notes in the five blank fields. Preserve C001 and C002 and record the human reasoning for each. The inclusion screen and evidence recheck provide reproducible inputs to that decision; every card remains Pending Human Adjudication until human review.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_1/routing_preflight.md) records `PASS`, `Coordinator inference: PASS`, ten verified named presets, `INTERACTIVE_CLI` execution and provider `CURRENT_SESSION`. Every role uses `gpt-6.1-sol`; ordinary specialists use medium reasoning, while the coordinator, statistical reviewers, inclusion screener, evidence rechecker and quality auditor use high reasoning. Distinct runtime IDs record fresh mandatory specialist stages.

### Source integrity and reproducible evidence

| Supplied source | SHA-256 |
|---|---|
| jama_barkin_2018_oi_180075.pdf | 231de40e6ac86c81413c11d958fc410e49450ece9b6ddb0c22e2042d2c162e36 |
| joi180075supp1_prod.pdf | b67c573979a4264284b87711cc2dd9ff7a74c2d709e1b045993f54624a4c6196 |
| joi180075supp2_prod.pdf | 5417d3ddc9769fa45832d8495fb337bcbeb2396276f08c79c81efa7626556a9a |

The quality audit independently reproduced all three source hashes and all 71 reusable-artifact hashes. Source and reused artifacts were preserved. The final source-integrity records are [source hashes before](review_1_6_1/source_hashes_before.sha256), [source hashes after](review_1_6_1/source_hashes_after.sha256), [reused hashes before](review_1_6_1/reused_artifact_hashes_before.sha256) and [reused hashes after](review_1_6_1/reused_artifact_hashes_after.sha256).

The [tooling record](review_1_6_1/tooling_record.md) records the direct probe, available PDF/text/rendering/hashing tools and unavailable OCR/Office tools. The review used CPU-only Poppler 25.03.0 and GNU sha256sum 9.7. Pandoc 3.1.11.1 is available for standalone HTML rendering. The fallback environment was not needed or created. No external sources were used.

Source links use one-based physical PDF pages, including covers. Reused derivatives identify provenance; candidate evidence links resolve to supplied PDFs. Canonical [ledger](review_1_6_1/candidate_ledger.md), [screening](review_1_6_1/screening/inclusion_screen.md), [recheck](review_1_6_1/verification/evidence_recheck.md) and [audit](review_1_6_1/quality/evidence_quality_audit.md) artifacts preserve the complete evidence chain for both stable IDs.

### Agent execution

All 17 actual runtime identities, including the coordinator, mapping shards, bounded numeric repairs and this report generator, appear below. Each specialist started fresh. The authoritative [execution manifest](review_1_6_1/agent_execution_manifest.md) records one primary durable artifact per agent.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_2 | root/support_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_002.md |
| support_quantitative_mapper_shard_3 | root/support_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_003.md |
| support_quantitative_mapper_shard_4 | root/support_mapper_4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_004.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_consistency_reviewer_bound_repair_1 | root/numeric_bound_repair_1 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_repair_001.md |
| numeric_consistency_reviewer_bound_repair_2 | root/numeric_bound_repair_2 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_repair_002.md |
| inclusion_screener | root/inclusion_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Statistical pass 1 (`root/statistics_pass_1`) and pass 2 (`root/statistics_pass_2`) are distinct fresh high-effort executions covering all 116 registered statistical relationships. No pass-2 finding was emitted, so the conditional pass-2 screener stage was not applicable. Separate screening, recheck and audit agents completed their respective mandatory stages.

### Reproducibility performance

The package-specific target accounts for reuse and fresh-render burden, source formats, mixed result/plan material, relationship volume and mandatory agent waves. It is a planning range; no scientific scope was reduced to meet it. Timing ends immediately after complete Markdown assembly and excludes local rendering and mechanical validation. The exact fields below mirror the [run state](review_1_6_1/run_state.md).

- **Target basis:** Three PDF sources contain 132 units, all backed by source-matched reusable native text; four fresh-required embedded-content units identified during mapping, no Office conversion, and no new OCR initially needed. The 113-page protocol/SAP bundle requires four bounded support mapping shards; mixed results tables, trajectory graphics, multiple plan versions, two distinct statistical passes, screening, recheck, audit, and report assembly require several serial agent waves. Target accounts for this source-role and relationship complexity and full reuse rather than page count alone.
- **Total source units:** 132
- **Fresh-source units:** 4
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T02:52:34Z
- **Finished UTC:** 2026-10-11T03:30:39Z
- **Observed elapsed minutes:** 38.08
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Rendering and mechanical validation

The coordinator renders the finalized Markdown once with the supplied Workflow 1.6.1 renderer, records tooling cleanup, and runs the package validator. The durable [validation record](review_1_6_1/review_validation.json) records the resulting checks and status. These local commands preserve the report's evidence links and create standalone HTML with embedded CSS and a table of contents:

```bash
python3 workflow_1_6_1/scripts/render_report.py \
  .ai_paper_validation/final_report_1_6_1.md \
  .ai_paper_validation/final_report_1_6_1.html \
  --profile 1.6.1
python3 workflow_1_6_1/scripts/bootstrap_tooling.py remove
python3 workflow_1_6_1/scripts/validate_review.py --profile 1.6.1 --package .
```
