# Quantitative Reporting Quality-Control Consistency Review — ImmunoSep

> **Pending Human Adjudication.** Every candidate in this report awaits human adjudication. Evidence states record mechanical reproduction; inclusion audits record application of the quality-control scope. These fields are not adjudications or suggested dispositions.

## Executive Quality-Control Summary

The complete supplied package yielded **14 stable candidate reporting issues** after independent screening, direct-source recheck and quality audit: seven protocol/report comparisons, six statistical-result issues and one report-internal result-attribution issue. All fourteen have evidence state `reproduced` and inclusion audit `CONFIRMED`; all remain Pending Human Adjudication.

The review mapped all **167 physical pages in five supplied PDFs**, using reusable evidence for 156 pages and fresh direct-source mapping for eleven. Numeric review covered 72 relationship groups. Two distinct fresh high-effort statistical specialists each covered all 111 statistical relationships. Twenty-three initial findings received independent screening decisions; fourteen were included and nine screened out. Statistical pass 2 and the independent audit emitted no additional findings.

The candidates concern endpoint and analysis specification, outcome hierarchy, missing-data rules, reported subgroup quantities and outcome attribution. They do not establish a change in the trial’s conclusions, a patient-level consequence or any downstream use of a discrepant value. Their potential relevance is limited to the specific interpretation or extraction described in each card.

## Package and Reused-Evidence Provenance

The supplied main article is *Precision Immunotherapy to Improve Sepsis Outcomes*. Document roles were assigned from content. A prospective protocol/SAP remains PLAN even though it is supplied as a supplement; results and administrative study appendices are REPORT.

| Source ID | Actual supplied file and content | Role | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — main article](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1) | REPORT | 12 |
| DOC-002 | [joi250116supp1_prod_1771885794.26255.pdf — protocol/SAP bundle](../joi250116supp1_prod_1771885794.26255.pdf#page=1) | PLAN | 72 |
| DOC-003 | [joi250116supp2_prod_1771885794.27755.pdf — results supplement](../joi250116supp2_prod_1771885794.27755.pdf#page=1) | REPORT | 54 |
| DOC-004 | [joi250116supp3_prod_1771885794.28255.pdf — collaborator appendix](../joi250116supp3_prod_1771885794.28255.pdf#page=1) | REPORT | 28 |
| DOC-005 | [joi250116supp4_prod_1771885794.28755.pdf — data-sharing statement](../joi250116supp4_prod_1771885794.28755.pdf#page=1) | REPORT | 1 |
| **Total** | **Five PDFs** | | **167** |

DOC-002 contains protocol version 1.0 dated December 4, 2020, and SAP version 2.0 dated May 18, 2024. Its historical PROVIDE appendix was mapped as background and was not matched to current ImmunoSep outcomes or operative design. No direct Office, workbook or CSV source was supplied.

The curator inventoried and preservation-hashed **461 retained extraction/evidence assets**, including native/layout text, OCR, rendered pages and source-identity metadata. Some were partial, duplicate or unreadable; their presence did not establish usable coverage. Legacy scientific conclusions, candidate sets, screening decisions, classifications and final reports were not inputs to discovery. Reused derivatives remained immutable and served as source-matched locators/transcription aids. Exact original source pages governed every candidate.

Retained base assets record Poppler text/rendering and rapidocr_onnxruntime CUDA OCR on an RTX 5070 Laptop. Some older versioned derivatives do not record exact engine versions; that provenance limitation is preserved. New direct-source PDF information, text and rendering used the supplied helper with pinned PyMuPDF 1.26.4 and pypdf 5.9.0. New renders were 200 dpi on CPU. The user-requested GPU was confirmed through PowerShell; no new OCR or GPU computation was needed.

Detailed records: [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [source hashes](review_1_6_2/source_hashes_before.sha256) and [reused-asset hashes](review_1_6_2/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators, estimate/test logic, statistical-method logic and planned-versus-reported statistical design under Workflow 1.6.2. It checks matched results, rather than substituting a broad methodology, clinical, raw-data or misconduct assessment. No external literature was used and no preferred analysis was proposed.

| Source | Total units | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002 | 72 | 61 | 11 | 72 | COMPLETE |
| DOC-003 | 54 | 54 | 0 | 54 | COMPLETE |
| DOC-004 | 28 | 28 | 0 | 28 | COMPLETE |
| DOC-005 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **167** | **156** | **11** | **167** | **COMPLETE** |

Every unit is a physical PDF page, including covers, references and administrative material. DOC-002 fresh-required pages are p.18 and pp.55–64. The initial reusable partition was refined when the retained p.18 image proved unreadable; a fresh render closed that unit. A readable alternate retained image covers p.71. Glyph-corrupted plan text was mapped visually rather than adopted as authority. Administrative pages have explicit no-applicable-result records.

Mapping assignments were disjoint: DOC-001 pp.1–12; DOC-002 pp.1–32, 33–64 and 65–72; and DOC-003/004/005 pp.1–54, 1–28 and 1 respectively. The [source-coverage ledger](review_1_6_2/source_coverage.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) document closure and every durable stage/shard artifact. There is no scientific-coverage gap.

Differences within the half-unit display-precision rule and relative discrepancy ≤.05 were screened out unless an always-register interval/test category applied. Immediate-context wording, symbols and terminology, modeled-versus-crude differences, unsupported method assumptions and peripheral comparisons were excluded according to scope. Non-key secondary/exploratory reporting absences do not become primary/key-secondary issues by association. Screened-out observations have no evidence cards.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains **N001–N072**, covering all 44 main-paper mapping groups and 28 support groups, including their constituent subgroup and safety rows. Checks include totals, numerator/denominator percentages, event versus patient units, matched copies and effect-measure identity.

The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains **S001–S111**: 16 main-paper relationships, 73 support inferential rows and 22 prospective/statistical-specification groups. Each relationship has explicit `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. Relevant checks include point containment, limit order, effect direction, null/test agreement, same-display method reproduction, analysis population/window/contrast matching, power assumptions and planned analysis mapping. An absent variance, model, coding or test definition was not invented to force exact reconstruction.

| Review stage | Complete scope | Durable record |
|---|---|---|
| Numeric consistency | 72 groups; 1 finding and 8 excluded observations | [Numeric checker](review_1_6_2/checkers/numeric_consistency.md) |
| Cross-source consistency | Complete matched report/plan relationships; 7 findings and 15 exclusions | [Cross-source checker](review_1_6_2/checkers/cross_source_consistency.md) |
| Statistical pass 1 | All 111 S relationships; 15 findings and 23 exclusions | [Pass 1](review_1_6_2/checkers/statistical_pass_1.md) |
| Independent inclusion screening | All 23 initial findings | [Screening log](review_1_6_2/screening/inclusion_screen.md) |
| Direct-source evidence recheck | All 14 stable IDs and every affected location | [Merged recheck](review_1_6_2/verification/evidence_recheck.md) |
| Statistical pass 2 | All 111 S relationships, ledger, screen/recheck and all 46 original exclusions | [Pass 2](review_1_6_2/checkers/statistical_pass_2.md) |
| Independent quality audit | All stable IDs, screening decisions, exclusions, classifications and coverage | [Audit](review_1_6_2/quality/evidence_quality_audit.md) |

The two statistical passes used distinct fresh gpt-6.1-sol/high agents. Pass 2 independently reconsidered all **46 original checker exclusions** (8 numeric, 15 cross-source and 23 statistical), as well as the two substantive screening exclusions. It found no new qualifying issue; consequently no pass-2 screen was required. The audit reconsidered inclusion and screening in both directions, confirmed all fourteen inclusion audits and made no screening changes. Five auxiliary inventory/diagnostic tracking refinements did not alter source readings, candidates or classifications.

## Inclusion Screening Summary

A finding qualifies only when reproduced and either in an always-register Route A category or meeting all three Route B criteria: in focus, unresolved by immediate context and relevant to a named interpretation/extraction. Numeric comparisons use half-unit input/output intervals and their remaining relative gap. Route A interval-versus-test/containment comparisons are never removed as rounding.

| Screening decision | Count |
|---|---:|
| INCLUDE | 14 |
| SCREENED_OUT | 9 |
| **Findings independently screened** | **23** |

| Decision/reason code | Count |
|---|---:|
| INCLUDE — MEETS_THRESHOLD | 14 |
| SCREENED_OUT — DUPLICATE_OF_INCLUDED | 7 |
| SCREENED_OUT — NOT_REPRODUCED | 1 |
| SCREENED_OUT — CONTEXT_RESOLVES | 1 |
| SCREENED_OUT — ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT — NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT — TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT — MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT — CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT — PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT — OUT_OF_FOCUS | 0 |
| **Total decisions** | **23** |

The seven duplicates preserve checker provenance and affected locations within the included candidates; they are not seven additional candidates. The separate 46 checker-exclusion rows precede independent finding screening and are not added to the 23-row screening denominator. All counts reconcile to the [single screening table](review_1_6_2/screening/inclusion_screen.md). Pass 2 and audit produced zero new findings and zero additional screening decisions.

## Review-Domain Summary

`statistical_results` covers report counts, estimates, intervals, tests and method logic. `report_internal_inconsistency` covers unresolved numeric-result attribution within report materials. `protocol_report` covers a prospective-plan versus report statistical-design/analysis comparison. `plan_material` covers a statistical-design inconsistency solely within prospective material.

| Review domain | Stable candidates |
|---|---:|
| protocol_report | 7 |
| statistical_results | 6 |
| report_internal_inconsistency | 1 |
| plan_material | 0 |
| **Total** | **14** |

| Primary relationship type | Stable candidates |
|---|---:|
| P_R | 7 |
| P_P | 0 |
| S_C | 0 |
| S_W | 7 |
| **Total** | **14** |

Mixed candidates record all relationships, while their primary type follows P_R > P_P > S_C > S_W. C001/C003 also contain P_P; C002 also contains S_C and S_W. Corroborating-only locations do not create relationships.

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 14 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **14** |

Inclusion audits total CONFIRMED 14 and QUESTIONED 0. All fourteen statuses remain Pending Human Adjudication.

## Candidate Index

| Candidate | Reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#C001) | Primary mean/Welch versus responder/Fisher specification | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#C002) | Home-discharge versus ICU-discharge carry-forward eligibility | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#C003) | Infection and omics outcome-status pattern | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#C004) | Immune-reversal endpoint window, composite and ascertainment | protocol_report | P_R | reproduced | CONFIRMED |
| [C005](#C005) | Continuous versus binary primary-outcome power basis | protocol_report | P_R | reproduced | CONFIRMED |
| [C006](#C006) | Binary planned versus ordinal reported infection analysis | protocol_report | P_R | reproduced | CONFIRMED |
| [C007](#C007) | Prespecified primary and key-secondary analysis families not located | protocol_report | P_R | reproduced | CONFIRMED |
| [C008](#C008) | Unadjusted day-15 immunoparalysis OR | statistical_results | S_W | reproduced | CONFIRMED |
| [C009](#C009) | MALS NNH1 harm/benefit direction | statistical_results | S_W | reproduced | CONFIRMED |
| [C010](#C010) | NNH1 intervals versus specified safety tests | statistical_results | S_W | reproduced | CONFIRMED |
| [C011](#C011) | Five subgroup P values | statistical_results | S_W | reproduced | CONFIRMED |
| [C012](#C012) | Repeated APACHE coefficient/interval construction | statistical_results | S_W | reproduced | CONFIRMED |
| [C013](#C013) | Six-row output attributed to two outcomes | report_internal_inconsistency | S_W | reproduced | CONFIRMED |
| [C014](#C014) | 90-day interaction point outside its interval | statistical_results | S_W | reproduced | CONFIRMED |

# Candidate Evidence Cards

<a id="C001"></a>

## C001 — Primary mean/Welch versus responder/Fisher specification

**Status:** Pending Human Adjudication

**Candidate statement:** The original protocol specifies a between-arm mean SOFA analysis with Welch’s t test, whereas the later SAP and report specify a patient-level responder analysis with Fisher’s exact test and a different death-handling rule. The corresponding day-15 endpoint follows the same pattern.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol vs PLAN SAP and REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective protocol and SAP are PLAN; the main article is REPORT. The protocol-to-report comparison supplies P_R and the original-protocol-to-later-SAP difference supplies P_P. P_R takes precedence.

**Classification ambiguity:** The later SAP agrees with the reported responder specification and may represent an authorized revision. The supplied package does not explicitly map the original endpoint, test and death rule to that revision.

**Exact source locations:** PLAN [DOC-002 p.7 synopsis](../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p.24 primary endpoint/death rule](../joi250116supp1_prod_1771885794.26255.pdf#page=24), [p.25 corresponding day-15 mean](../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.27 Welch analysis](../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.66 SAP responder/death rule](../joi250116supp1_prod_1771885794.26255.pdf#page=66), [p.67 Fisher analysis](../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p.68 day-15 construction](../joi250116supp1_prod_1771885794.26255.pdf#page=68), [p.69 day-15 responder continuation](../joi250116supp1_prod_1771885794.26255.pdf#page=69); REPORT [DOC-001 p.3 endpoint](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=3), [p.5 imputation/secondary definition](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 Table 2 and statistical analyses](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6).

**Source evidence:** Protocol pp.7 and 24 specify the comparative difference in mean total SOFA through day 9, an arm-level decrease of at least 1.4 points, and averaging through death for patients dying before day 9. P.27 names Welch’s t test. P.25 states the corresponding day-15 mean endpoint. SAP pp.66–67 instead form each patient’s baseline minus the mean of days 2–9, classify attainment/nonattainment, replace missing scores after death with 24, and use Fisher’s exact test with ORs and 95% CIs. Pp.68–69 repeat that approach through day 15. The article reports primary attainment in 46/131 versus 26/145, OR 2.48 (95% CI 1.42–4.32), P=.002.

**Reported-versus-comparator:** Reported: binary patient-level attainment, Fisher comparison and death-score imputation of 24. Comparator: original continuous between-arm mean difference, Welch comparison and observed mean through death. The later SAP corroborates the report while differing from the original protocol.

**Reasoning procedure:** Match the current-trial endpoint window, unit of analysis, test and death handling across original protocol, later SAP and article. Treat the related day-15 change as another location of the same specification pattern. Do not equate a continuous mean comparison with a dichotomized responder comparison merely because both mention 1.4 points.

**Calculation:** This is a categorical endpoint/test/death-rule comparison; half-unit rounding intervals and a numeric relative discrepancy are not applicable. The reported primary responder table itself yields (46×119)/(85×26)=2.4769, consistent with printed 2.48. The strict >1.4 versus ≥1.4 symbol difference is excluded from this candidate: integer daily-score averages on 8- or 14-value grids cannot equal 1.4, since 1.4×8=11.2 and 1.4×14=19.6 are nonintegers.

**Affected result or extracted value:** The primary day-9 responder definition, analysis method and death handling; the analogous day-15 endpoint construction; interpretation of the reported primary OR 2.48.

**Why context does not resolve it:** Route A, category 5 covers a replaced planned primary analysis and changed endpoint construction. Agreement between the later SAP and report is retained as a revision alternative, rather than removing the source-confirmed original-to-report comparison.

**Alternative source-grounded interpretations:** An authorized SAP revision or operational clarification may connect the specifications. Its operative version history and scope are not printed. Individual SOFA trajectories would be needed to quantify any participant-level consequences; no such consequences are asserted.

**Mechanical evidence recheck:** Every cited original page was rendered directly and visually reread. The rechecker confirmed both specifications, their document roles and the P_R/P_P precedence without a source-transcription correction. The independent audit confirmed inclusion.

**Potential downstream evidence impact:** A data extractor could record the responder effect together with an endpoint/test/death-handling specification that does not identify its relationship to the original continuous design. This review does not quantify a change in treatment effect or trial conclusions.

Checker provenance retained: F-XS-001 INCLUDE; F-ST1-009 duplicate.

<a id="C002"></a>

## C002 — Home-discharge versus ICU-discharge carry-forward eligibility

**Status:** Pending Human Adjudication

**Candidate statement:** The SAP and article methods condition last-observation-carried-forward SOFA values on discharge home, while the article results and eTable 8 describe ICU discharge. Their eligibility sets are not explicitly equated for the 23 carry-forward cases.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN SAP vs REPORT main article and REPORT results supplement; REPORT main article internal descriptions

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** The PLAN-home versus REPORT-ICU comparison supplies P_R; article-home versus supplement-ICU supplies S_C; article-home versus article-ICU supplies S_W. P_R takes precedence and places the candidate in protocol_report.

**Classification ambiguity:** It is unknown whether all 23 ICU discharges also constituted home discharges or whether ICU terminology abbreviates the operational home criterion. The roles and precedence are otherwise explicit.

**Exact source locations:** PLAN [DOC-002 p.66](../joi250116supp1_prod_1771885794.26255.pdf#page=66); REPORT [DOC-001 p.3 daily ICU observation](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=3), [p.5 home-discharge rule](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 ICU-discharge result](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [DOC-003 p.20 eTable 8](../joi250116supp2_prod_1771885794.27755.pdf#page=20), [p.46 sensitivity population](../joi250116supp2_prod_1771885794.27755.pdf#page=46).

**Source evidence:** SAP p.66 carries forward the last recorded SOFA after discharge home before day 9; article p.5 uses that rule and separately names loss to follow-up. Article p.3 describes daily SOFA during ICU stay until discharge, and p.6 attributes 8.3% carry-forward to ICU discharge. eTable 8 names earlier ICU discharge and prints assumed day-9 counts of 10 and 13. eFigure 2 excludes carried-forward discharge cases and reports 38/121 (31.4%) versus 19/132 (14.4%), OR 2.72 (1.47–5.05), P=.001.

**Reported-versus-comparator:** Printed methods/SAP criterion: home discharge before day 9. Printed results/supplement criterion: ICU discharge before day 9. The compared quantities are the observation window and carry-forward eligibility, rather than the coherently reported patient counts.

**Reasoning procedure:** Compare the explicit triggering event across the SAP, article methods/results and supplement. Verify carry-forward totals and sensitivity exclusions independently. Keep an operational-rule question separate from any unobserved patient destination or actual reclassification.

**Calculation:** 10+13=23 and 23/276×100=8.333333%, consistent with printed 8.3%. Conservatively allowing half-unit ranges gives [22/276.5,24/275.5]×100=[7.95660%,8.71143%], overlapping printed [8.25%,8.35%]; gap=0 and relative discrepancy=0. Sensitivity denominator changes also reconcile: 131−121=10 and 145−132=13. No arithmetic discrepancy is registered.

**Affected result or extracted value:** The primary endpoint’s missing-data eligibility and observation window, and the definition of the carry-forward-excluded sensitivity population.

**Why context does not resolve it:** All Route B criteria apply: the primary missing-data rule is in focus; immediate context does not say that ICU discharge and home discharge identified the same patients at the same time; the distinction can affect how the primary and sensitivity analyses are interpreted or extracted.

**Alternative source-grounded interpretations:** All ICU discharge cases may also have been home discharges, or the result wording may summarize the home rule. The package does not establish either explanation. Exact home/ward discharge dates and the applied stop-observation transition are unavailable, so no participant-level change is inferred.

**Mechanical evidence recheck:** The exact SAP, article and supplement pages were visually confirmed. Counts and sensitivity denominator differences were reproduced and found coherent. The operational-label distinction remained, and the rechecker and auditor confirmed the full P_R/S_C/S_W classification.

**Potential downstream evidence impact:** An evidence extractor could record ICU discharge or home discharge as the primary missing-data trigger, with different implications for the observation window. No actual patient reclassification or resulting effect change is established.

Checker provenance retained: F-XS-007 INCLUDE.

<a id="C003"></a>

## C003 — Infection and omics outcome-status pattern

**Status:** Pending Human Adjudication

**Candidate statement:** Current-trial infection resolution is secondary in the protocol synopsis, later SAP and report, but exploratory in the detailed protocol and endpoint appendix. The same secondary/exploratory pattern affects omics outcomes within PLAN material.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN protocol synopsis vs PLAN detailed protocol and SAP vs REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** The detailed PLAN infection hierarchy versus REPORT supplies P_R. The synopsis versus detailed PLAN infection/omics hierarchy supplies P_P. P_R takes precedence; the omics component remains plan-internal and creates no asserted missing REPORT result.

**Classification ambiguity:** The synopsis and later SAP may represent the intended or revised hierarchy, or secondary may have been used as an umbrella term. The detailed protocol explicitly separates exploratory endpoints and does not state that convention.

**Exact source locations:** PLAN [DOC-002 p.7 synopsis](../joi250116supp1_prod_1771885794.26255.pdf#page=7), [p.25 detailed hierarchy](../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.27 infection test hierarchy](../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.57 resolution appendix](../joi250116supp1_prod_1771885794.26255.pdf#page=57), [p.70 SAP infection](../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p.5 prespecified secondary endpoints](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 main secondary table](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 sixth secondary result](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7).

**Source evidence:** Protocol p.7 lists infection resolution and genomic, epigenomic, proteomic, metabolomic and microbiomic surrogate biomarkers as secondary endpoints. P.25 places both under a distinct exploratory heading; p.27 names their analyses exploratory. P.57 labels the current ImmunoSep infection-resolution appendix as exploratory. SAP p.70 places infection resolution in its secondary sequence. Article pp.5–7 calls infection resolution by day 15 one of six prespecified secondary endpoints and reports OR 0.59 (0.38–0.91), P=.02.

**Reported-versus-comparator:** Reported/SAP/synopsis infection status: secondary. Detailed protocol and resolution appendix status: exploratory. Omics shows the same synopsis-versus-detailed-plan status difference, without a reported omics counterpart in this comparison.

**Reasoning procedure:** Match the same current-trial outcomes under the printed endpoint headings and analysis hierarchy. Distinguish current ImmunoSep content from historical PROVIDE material. Consolidate the repeated hierarchy pattern into one candidate without inferring an obligation to report exploratory omics.

**Calculation:** Outcome status is categorical; half-unit rounding and numeric relative discrepancy do not apply. OR 0.59, CI 0.38–0.91 and P=.02 identify the affected infection result, rather than establishing another numeric inconsistency.

**Affected result or extracted value:** The prespecified status assigned to the day-15 infection-resolution result and the accompanying plan-internal omics hierarchy.

**Why context does not resolve it:** Route A, category 5 covers a prespecified outcome whose status changes. Distinct secondary and exploratory headings are source-confirmed; an unprinted umbrella or amendment convention does not remove that comparison.

**Alternative source-grounded interpretations:** The synopsis and later SAP support the article’s secondary classification and could reflect a revised hierarchy. An operative amendment/version or explicit umbrella definition is missing. No missing omics effect or requirement to publish exploratory omics is inferred.

**Mechanical evidence recheck:** All affected current-trial hierarchy headings and report locations were directly visually reread. Secondary versus exploratory designations reproduced without transcription changes. The audit confirmed P_R/P_P precedence and the bounded omics component.

**Potential downstream evidence impact:** A systematic-review extraction could classify the infection result as a prespecified secondary or exploratory outcome depending on the supplied location. The candidate concerns that status and plan hierarchy, not a demonstrated change in the effect estimate.

Checker provenance retained: F-XS-004 INCLUDE; F-ST1-012 duplicate.

<a id="C004"></a>

## C004 — Immune-reversal endpoint window, composite and ascertainment

**Status:** Pending Human Adjudication

**Candidate statement:** The planned day-15 immune-reversal endpoint uses a biomarker conjunction and death/nonattainment handling, whereas the report ties the displayed result to day 28 with sustained biomarker change and at least two serial draws in a 125-patient subset.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol and SAP vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** Protocol/SAP endpoint definitions are PLAN; article and results-supplement definitions are REPORT. Their prospective-versus-reported comparison supplies P_R. Report locations corroborate one another; contextually resolved target wording and plan shorthand add no independent relationships.

**Classification ambiguity:** A supplementary day-28 analysis or an unprinted applied ferritin criterion could explain parts of the comparison. The supplied package does not map the displayed counts to a distinct day-15 result or identify the operative revised definition.

**Exact source locations:** PLAN [DOC-002 p.25](../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.69](../joi250116supp1_prod_1771885794.26255.pdf#page=69), [p.70 continuation](../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p.5 definition](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 Table 2/footnote](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 by-day-28 result](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [DOC-003 p.50 eFigure 6](../joi250116supp2_prod_1771885794.27755.pdf#page=50).

**Source evidence:** Protocol p.25 specifies day-15 reversal: MALS ferritin decreases at least 15%; immunoparalysis Quantibrite exceeds 8000 AB/C together with ferritin below 4420 ng/mL. SAP pp.69–70 censors at day 15, repeats that conjunction and classifies death before day 15 as nonachievement. Article pp.5–6 omits the immunoparalysis ferritin conjunction in its printed definition and requires sustained change plus at least two serial draws; fewer draws mean nonattainment. It reports 46/59 (78.0%) versus 32/66 (48.5%), OR 3.76 (1.72–8.22). P.7 ties those counts to day 28. eFigure 6 describes draws and censoring through day 28, missing draws from death/discharge, the 59/66 sampled population and Cox HR 2.38 (1.50–3.77).

**Reported-versus-comparator:** Planned: day 15, phenotype-specific biomarker criteria including the immunoparalysis ferritin conjunction, and pre-day-15 death handling. Reported: displayed day-28 result with sustained-change/two-draw rules and a 125-person sampled denominator, without that printed conjunction.

**Reasoning procedure:** Compare the window, composite components, persistence/serial-draw requirements and denominator/death rules as one endpoint-specification pattern. Use the report’s absolute HLA-DR target footnote/caption to resolve isolated increase-of wording. Do not reinterpret a coherent subset count as a numerical denominator discrepancy.

**Calculation:** Categorical specification differences have no rounding interval. Subset size is coherent: 59+66=125. The percentages reproduce: 46/59×100=77.9661% lies in [77.95%,78.05%], and 32/66×100=48.4848% lies in [48.45%,48.55%]. These identifiers therefore have zero gap to their displayed percentage intervals. The specification comparison does not calculate a revised endpoint count or effect.

**Affected result or extracted value:** The immune-reversal endpoint’s follow-up window, composite definition, ascertainment and analytic population; extraction of its OR 3.76 and day-28 Cox HR 2.38.

**Why context does not resolve it:** Route A, category 5 covers changes in a prespecified outcome/composite definition. Direct-source confirmation retains day 15 versus day 28 and the changed printed conjunction/persistence rules. Those are separate from immediately resolved absolute-target wording.

**Alternative source-grounded interpretations:** The day-28 time-to-event analysis may supplement a day-15 endpoint, or ferritin below 4420 may have been applied without repetition. The displayed counts are expressly tied to day 28, and no separate day-15 version is located. Exact biomarker/death/discharge histories, operative revision and disposition of cases without sufficient serial draws are unavailable.

**Mechanical evidence recheck:** Every planned and reported endpoint page was directly visually confirmed. Report counts and percentages reconcile. The recheck and audit reproduced the window/composite/ascertainment comparison and confirmed P_R without adding contextually resolved P_P, S_C or S_W relationships.

**Potential downstream evidence impact:** An evidence extractor could associate the immune-reversal effect with different follow-up windows, composite components or sampled-population rules. No participant-level reclassification or numerical consequence is established.

Checker provenance retained: F-XS-003 INCLUDE; F-ST1-011 duplicate.

<a id="C005"></a>

## C005 — Continuous versus binary primary-outcome power basis

**Status:** Pending Human Adjudication

**Candidate statement:** The protocol bases primary-outcome power on a continuous mean SOFA difference, while the report bases it on binary attainment probabilities of 40% versus 20%; no supplied prospective calculation links those distinct bases.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol power specification vs REPORT main article power specification

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route B

**Classification rationale:** The prospective protocol power section is PLAN and the article power section is REPORT. Their effect-scale/input comparison supplies P_R and protocol_report. No separate plan-only or report-only numerical sample-size conflict is included.

**Classification ambiguity:** A revised binary calculation may have retained the same sample target, or response planning may have accompanied the continuous calculation. The revision, exact procedure and interpretation of the protocol’s dispersion wording are not supplied.

**Exact source locations:** PLAN [DOC-002 p.25 power introduction](../joi250116supp1_prod_1771885794.26255.pdf#page=25), [p.26 calculation](../joi250116supp1_prod_1771885794.26255.pdf#page=26); REPORT [DOC-001 p.5 Sample Size Calculation](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5). The complete supplied SAP pp.63–72 has no revised binary power calculation.

**Source evidence:** Protocol pp.25–26 power a 1.4-point mean SOFA reduction with printed dispersion 3.2, 90% power, 5% significance, a two-sided independent-groups t test and nQuery Advisor 6.02. It states 117 participants per arm and 280 after approximately 15% dropout. Its 40%/60% pair describes anticipated phenotype recruitment, not treatment-arm response probabilities. Article p.5 anticipates primary attainment in 40% versus 20%, with the same nominal power, significance level and sample targets. The complete supplied SAP contains no revised binary calculation.

**Reported-versus-comparator:** Reported: binary response probabilities 0.40 and 0.20. Comparator: mean difference 1.4 with dispersion 3.2 and an independent-groups t-test calculation. Common 90% power, 5% significance and 117/group do not themselves connect these distinct planning assumptions.

**Reasoning procedure:** Compare the printed primary-outcome scale, effect-size inputs and calculation procedure. Keep normal approximations and dropout arithmetic as contextual diagnostics rather than treating an unidentified exact method as a reproduced sample-size conflict.

**Calculation:** No numeric sample-size inconsistency is registered. The contextual dropout calculation 234/.85=275.2941 differs from 280 within the workflow rule. Allowing 117±.5 per arm and 15%±.5 percentage points gives [233/.855,235/.845]=[272.5146,278.1065]; printed 280 has [279.5,280.5], leaving gap 1.3935 and relative discrepancy about .00498≤.05. Normal power approximations of 109.79/group for the continuous inputs and 108.24/group for the binary inputs are diagnostics only; input rounding and the unreported exact procedure do not establish that 117 fails. Rounding cannot identify an operative continuous-to-binary design mapping.

**Affected result or extracted value:** Interpretation and extraction of the claimed 90% power for the reported binary primary endpoint and its prospective sample-size basis.

**Why context does not resolve it:** All Route B criteria apply: power assumptions are in focus; the immediate text does not link a continuous mean calculation to the stated binary probabilities; that linkage determines what prospective power claim applies to the reported responder endpoint.

**Alternative source-grounded interpretations:** A prospective revision or parallel binary calculation could support the article while preserving 117/group. Its formula, continuity convention, inputs and version are missing. No preferred calculation, actual achieved power or underpowering consequence is asserted.

**Mechanical evidence recheck:** Both original power sections were directly visually reread, and the complete SAP map plus analytic pages were checked for a revised calculation. The effect-scale difference reproduced. The auditor confirmed that approximate sample-size and dropout comparisons do not create an additional candidate.

**Potential downstream evidence impact:** A review could copy the 90% binary-response power claim without identifying the prospective calculation that supports that scale. The candidate does not establish a numerical shortfall in sample size or achieved power.

Checker provenance retained: F-XS-002 INCLUDE; F-ST1-010 duplicate.

<a id="C006"></a>

## C006 — Binary planned versus ordinal reported infection analysis

**Status:** Pending Human Adjudication

**Candidate statement:** The plan prescribes a binary resolved/not-resolved infection comparison with Fisher/Mantel–Haenszel analysis, while the report presents four-state ordinal regression without mapping it to the planned binary result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol and SAP infection analysis vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Qualifying route:** Route B

**Classification rationale:** Both protocol and SAP locations are PLAN; article and results supplement are REPORT. P_R governs the analysis-specification difference. The reported ordinal displays corroborate each other and create no independent S_C conflict.

**Classification ambiguity:** The ordinal analysis may supplement or replace the binary analysis. The supplied package does not identify that mapping, a revised specification or a corresponding binary estimate/test.

**Exact source locations:** PLAN [DOC-002 p.27 Fisher/Mantel–Haenszel infection analysis](../joi250116supp1_prod_1771885794.26255.pdf#page=27), [p.70 binary resolved/not-resolved SAP analysis](../joi250116supp1_prod_1771885794.26255.pdf#page=70); REPORT [DOC-001 p.6 Table 2/statistical analysis/SAP-following statement](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 ordinal result](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [DOC-003 p.49 four-state figure](../joi250116supp2_prod_1771885794.27755.pdf#page=49).

**Source evidence:** Protocol p.27 names Fisher’s exact infection-resolution comparison and Mantel–Haenszel OR/CIs. SAP p.70 explicitly splits attainment/nonattainment of resolution and prescribes those methods with infection/immune strata. Article p.6 states ordinal regression for resolved, intermediate, failure and superinfection while stating that analyses followed the SAP. Counts are 58,11,32,30 of 131 versus 46,9,44,46 of 145. Article pp.6–7 and eFigure 5 report a worse-disposition OR 0.59 (0.38–0.91), with P=.02 in the article and .018 in the figure.

**Reported-versus-comparator:** Reported effect: four-category ordinal worse-disposition OR 0.59. Planned comparison: binary infection resolution/nonresolution analyzed with Fisher and Mantel–Haenszel. Reported resolution counts 58/131 and 46/145 do not supply a named planned binary effect/test.

**Reasoning procedure:** Match the same infection outcome across the plan and reported model, retaining the explicitly stated ordinal contrast. Distinguish an analysis-specification comparison from a model-versus-crude arithmetic comparison, and from a preferred-analysis recommendation.

**Calculation:** The category counts total 58+11+32+30=131 and 46+9+44+46=145. P=.018 has half-unit interval [.0175,.0185], overlapping P=.02’s [.015,.025]; copy gap and relative discrepancy=0. A crude binary resolution OR is (58×99)/(73×46)=1.70935, but this is diagnostic only and is not a conflicting comparator for the modeled ordinal OR .59. Numeric rounding does not equate the two stated analysis specifications.

**Affected result or extracted value:** Interpretation/extraction of the infection-resolution effect as a binary resolution contrast or ordinal disposition contrast, and its mapping to the prespecified analysis.

**Why context does not resolve it:** All Route B criteria apply: the planned analysis is in focus; immediate report context clearly identifies ordinal regression but does not reconcile it with the explicit binary plan; the distinction changes the quantity represented by the infection OR.

**Alternative source-grounded interpretations:** Ordinal regression could be an added analysis or a replacement; the worse-disposition caption could summarize the ordinal estimand. A revised specification, corresponding binary output, and exact ordinal coding/link/adjustment details are not supplied. No requirement that the model equal a crude ratio is imposed.

**Mechanical evidence recheck:** All five cited plan/report locations were directly visually confirmed. The binary/ordinal comparison reproduced; counts and P-value copies reconcile. Rechecker and auditor confirmed P_R and the bounded plan-mapping question.

**Potential downstream evidence impact:** A meta-analysis extractor could treat the ordinal .59 as a binary infection-resolution estimate if the analysis mapping were overlooked. No actual propagation or consequence to a pooled result is established.

Checker provenance retained: F-XS-005 INCLUDE; F-ST1-013 duplicate.

<a id="C007"></a>

## C007 — Prespecified primary and key-secondary analysis families not located

**Status:** Pending Human Adjudication

**Candidate statement:** Four prespecified primary/key-secondary analysis families are not located in the complete supplied article and results supplement, and the package does not explicitly map them to replacement or withdrawn analyses.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP primary and key secondary analyses vs complete REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Qualifying route:** Route A, category 5

**Classification rationale:** The SAP specifies prospective analyses and is PLAN; the complete article and results supplement are REPORT. Their prescribed-versus-supplied reporting comparison supplies P_R. Closest report destinations are context, rather than mutually conflicting results that add report/report relationships.

**Classification ambiguity:** Reported model interactions may have replaced planned homogeneity tests, or additional results may exist outside the supplied package. Neither mapping is identified in the supplied report. Nonlocation does not establish that the analyses were never performed.

**Exact source locations:** PLAN [DOC-002 p.67 immune-state response homogeneity](../joi250116supp1_prod_1771885794.26255.pdf#page=67), [p.68 survivor secondary means and 28-day immune-state mortality](../joi250116supp1_prod_1771885794.26255.pdf#page=68), [p.71 severity/homogeneity and antibiotics](../joi250116supp1_prod_1771885794.26255.pdf#page=71), [p.72 antibiotic-primary continuation](../joi250116supp1_prod_1771885794.26255.pdf#page=72); REPORT [DOC-001 p.5 endpoint definitions](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=5), [p.6 methods/results](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), [p.7 response/mortality/post hoc results](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), [p.8 interaction continuation](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8), [DOC-003 p.16 antibiotic footnote](../joi250116supp2_prod_1771885794.27755.pdf#page=16), [p.21 primary model](../joi250116supp2_prod_1771885794.27755.pdf#page=21), [p.22 immune response](../joi250116supp2_prod_1771885794.27755.pdf#page=22), [p.23 subset baseline](../joi250116supp2_prod_1771885794.27755.pdf#page=23), [p.24 subset baseline continuation](../joi250116supp2_prod_1771885794.27755.pdf#page=24), [p.47 overall mortality](../joi250116supp2_prod_1771885794.27755.pdf#page=47), [p.51 primary severity](../joi250116supp2_prod_1771885794.27755.pdf#page=51), [p.52 28-day severity](../joi250116supp2_prod_1771885794.27755.pdf#page=52), [p.53 90-day severity](../joi250116supp2_prod_1771885794.27755.pdf#page=53), with absence assessed against complete DOC-001 pp.1–12 and DOC-003 pp.1–54 result maps and source-linked text.

**Source evidence:** SAP p.67 prescribes primary-response OR homogeneity across MALS/immunoparalysis with Breslow–Day and Tarone. P.68 prescribes 28-day mortality comparisons within those immune states. P.71 prescribes primary and key-28-day severity-stratum OR/homogeneity analyses with immune-state stratification and named homogeneity tests. Pp.71–72 prescribe primary response by appropriate/non-appropriate antibiotics. The report supplies phenotype-specific response ORs, overall mortality, baseline antibiotic information, severity-specific comparisons and model interactions, but no identified outputs or replacement statements for the four families.

**Reported-versus-comparator:** Planned families versus closest supplied content:

| Prespecified family | Closest report content | Specific output not located |
|---|---|---|
| Primary immune-state response homogeneity | Article p.7 and eTable 10 p.22 phenotype response estimates | Breslow–Day/Tarone comparison of immune-state ORs |
| Key-secondary 28-day mortality within MALS/IP | Article pp.6–7 and eFigure 3 p.47 overall mortality | Within-immune-state 28-day mortality comparisons |
| Primary response by antibiotic appropriateness | Baseline antibiotic frequencies 34/41 versus 33/38 and eTable 6 footnote p.16 | Responder comparisons/effects/tests by antibiotic appropriateness |
| Primary/key-28-day severity homogeneity and immune-within-severity | eFigures 7/8 pp.51–52 severity comparisons and model interactions | Named homogeneity outputs and immune-within-severity results or explicit replacement mapping |

**Reasoning procedure:** Check complete DOC-001 pp.1–12 and DOC-003 pp.1–54 maps, the supplement index of 15 eTables/9 eFigures and fresh full-source native text; visually confirm the plausible table/figure destinations where native extraction is incomplete. Searches include Breslow, Tarone, homogeneity, appropriate, antibiotic, MALS, immunoparalysis, mortality, survivor, interaction, replacement, withdrawal and amendment. Consolidate the four structurally similar primary/key-secondary reporting-absence families into one candidate.

**Calculation:** This is bounded nonlocation of named analyses, not a numerical discrepancy; half-unit intervals and relative discrepancy are not applicable. Separate subgroup ORs are not homogeneity tests, baseline antibiotic counts are not responder outcomes, and overall mortality is not a within-immune-state result. The supplied data do not permit calculating the absent effects. Complete reporting scope is 12+54=66 pages.

**Affected result or extracted value:** Availability and prespecification mapping of the four named primary/key-secondary analysis families, including their subgroup effects and homogeneity tests.

**Why context does not resolve it:** Route A, category 5 covers planned primary or key-secondary analyses that are not reported. The closest supplied outputs do not identify the named analyses or explicitly replace/remove them. The claim is limited to nonlocation in the complete supplied reporting.

**Alternative source-grounded interpretations:** The report’s interaction analyses could replace homogeneity tests; phenotype response estimates could have been regarded as sufficient; results could exist in an unsupplied document. No such mapping is printed. Missing named outputs, subgroup cross-tabulations and replacement/removal specifications prevent effect reconstruction. The survivor-only day-1–9 mean/Student t comparison is non-key secondary context and is excluded from this candidate, as are non-key 90-day immune analyses, day-15 survivor means and exploratory ROC/omics absences. Original mean/Welch replacement is separately C001.

**Mechanical evidence recheck:** The rechecker verified every prospective statement, complete page maps/index, full-source text search and all plausible report destinations, using direct visual checks for figure content. The auditor confirmed all four included families and explicitly reaffirmed the non-key survivor-mean exclusion. The evidence state records bounded supplied-report nonlocation, not whether analyses were performed.

**Potential downstream evidence impact:** An extractor could lack named prespecified primary/key-secondary subgroup or homogeneity results, or assign nearby model interactions to them without an explicit mapping. No unreported effect size, selective-reporting mechanism or conclusion change is inferred.

Checker provenance retained: F-XS-006 INCLUDE; F-ST1-015 duplicate.


<a id="C008"></a>

## C008 — Unadjusted day-15 immunoparalysis odds ratio does not reconcile with its counts

Pending Human Adjudication.

**Candidate statement:** The final row of eTable 10 prints an unadjusted odds ratio of 1.194 for day-15 SOFA response in sepsis-induced immunoparalysis. Its displayed counts yield 1.943574 under the count-based method that reproduces all three companion rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 10 final row vs companion rows and displayed counts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 4.

**Classification rationale:** The point, counts, unadjusted label and supporting companion rows are reported results within one results supplement. This is an estimate-construction comparison, with no conflicting PLAN location. F-ST1-004 independently described the same issue and was screened as duplicate provenance.

**Classification ambiguity:** The document roles are clear. An alternative unadjusted computation or analysis population that would associate 1.194 with this row is not identified.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.22, eTable 10, final day-15 immunoparalysis row and all three companion rows](../joi250116supp2_prod_1771885794.27755.pdf#page=22).

**Source evidence:** The affected row reports precision immunotherapy 40/106 (37.7%) and placebo 29/122 (23.8%), difference 13.9 (1.9–25.6), unadjusted OR 1.194 (95% CI, 1.09–3.45), and P=.030. The other three rows report counts 12/25 versus 4/23 with OR 4.38; 34/106 versus 22/122 with OR 2.15; and 12/25 versus 5/23 with OR 3.32. Direct source inspection confirms that the affected point reads 1.194, rather than 1.94.

**Reported-versus-comparator:** Printed 1.194 is compared with the count-cross-product OR 1.943573668. The comparator is justified by the explicit unadjusted label and the same display's three reproducing rows; this is not a comparison of an adjusted estimate with a crude ratio.

**Reasoning procedure:** Read the row, outcome window and column alignment from the source page. Compute event odds in each arm and their ratio. Apply the same construction to the other three rows, then allow the displayed inputs and point their half-unit precision intervals. The unresolved question is which unadjusted computation and population produced the printed point, rather than which estimate should replace it.

**Calculation:** The affected OR is `40×(122−29)/[(106−40)×29]=1.943573668`. Companion values are 4.384615385, 2.146464646 and 3.323076923, reproducing their displayed points. Conservatively allowing independent count/denominator half-unit ranges gives `[39.5×92/(67×29.5),40.5×94/(65×28.5)]=[1.838603592,2.055060729]`. Printed 1.194 allows [1.1935,1.1945]. The minimum gap is .644103592 and relative discrepancy `.644103592/1.194=.539450245`, above .05. Exact-integer inputs would narrow the comparator range. The CI's geometric center, approximately 1.93920, is additional corroboration and is not adopted as a replacement estimate.

**Affected result or extracted value:** The unadjusted day-15 SOFA-response OR for the immunoparalysis subgroup, specifically its effect magnitude.

**Why context does not resolve it:** Route A, category 4 applies: a printed estimate does not reproduce beyond the display threshold under a method that reproduces the companion rows. Reconstructing a plausible intended point does not remove the printed reading that an extractor could take.

**Alternative source-grounded interpretations:** A different underlying population or unprinted unadjusted computation could account for the point. The display identifies neither distinction. A substituted digit is another possible explanation, but no production mechanism or intended replacement is established.

**Mechanical evidence recheck:** A fresh 200-dpi CPU render of the exact source page was visually read; every affected and companion count/point was confirmed. Independent arithmetic reproduced the discrepancy with no source transcription or location change. The evidence state records this comparison, without adjudicating an intended value.

**Potential downstream evidence impact:** If confirmed, the issue could affect extraction of the subgroup's unadjusted OR and its magnitude. No propagation or change to a synthesized conclusion is established.

<a id="C009"></a>

## C009 — MALS number-needed-to-harm direction does not reconcile with patient risks

Pending Human Adjudication.

**Candidate statement:** eTable 15 labels positive MALS NNH1=8.8 as the number needed to treat to induce at least one serious treatment-emergent adverse event, whereas the corresponding patient risks are lower under anakinra than placebo.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 13 Any SAE counts vs eTable 15 MALS NNH1

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route A, category 2.

**Classification rationale:** The harm-induction label, NNH point and corresponding patient risks are conflicting REPORT content within the results supplement. Its patient-count footnote is corroboration. No prospective plan comparison participates.

**Classification ambiguity:** The table does not specify a sign convention or whether an unsigned reciprocal is used for both prevention and induction of harm. This uncertainty does not alter the source roles or relationship.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.27, eTable 13, MALS Any SAE row](../joi250116supp2_prod_1771885794.27755.pdf#page=27); [physical PDF p.44, eTable 15, MALS NNH1 and induce-harm definition](../joi250116supp2_prod_1771885794.27755.pdf#page=44). Definition support: [physical PDF p.29, eTable 13 footnote a](../joi250116supp2_prod_1771885794.27755.pdf#page=29).

**Source evidence:** Any SAE occurs in 20/25 (80.0%) MALS patients under anakinra and 21/23 (91.3%) under placebo. The marked footnote confirms numbers of patients for this row, rather than numbers of events. eTable 15 prints NNH1=8.8 (95% CI, 3.2–10.0) and defines this quantity as patients needed to treat to induce at least one serious TEAE; NNH is defined as number needed to harm.

**Reported-versus-comparator:** The positive harm-induction reading is compared with a negative treatment-minus-placebo risk difference and its negative signed reciprocal. The unsigned reciprocal magnitude is close to 8.8; direction and reference convention, rather than that magnitude's rounding, are the issue.

**Reasoning procedure:** Confirm that the adverse-event inputs count patients with at least one event. Calculate treatment risk minus placebo risk, then its signed reciprocal. Test whether the direction survives conservative half-unit ranges and compare it with the explicit induce-harm label. The unresolved question is whether 8.8 denotes prevention or induction, and which reference/sign convention governs it.

**Calculation:** `20/25−21/23=−.113043478`; its signed reciprocal is −8.846153846. Conservative count/denominator ranges give risk difference `[19.5/25.5−21.5/22.5,20.5/24.5−20.5/23.5]=[−.190849673,−.035605732]`. Its reciprocal range is [−28.085365854,−5.239726027], separated from the printed point range [8.75,8.85] by at least 13.989726027; relative discrepancy is 1.589741594. Printed risk precision also preserves the negative direction: [79.95,80.05]% minus [91.25,91.35]% gives [−11.40,−11.20] percentage points.

**Affected result or extracted value:** The harm-versus-benefit interpretation and treatment/reference direction of MALS NNH1=8.8.

**Why context does not resolve it:** Route A, category 2 applies: the explicit harm-induction reading reverses the direction supported by the corresponding patient risks, beyond display precision. The source does not explain an unsigned or reversed-reference convention.

**Alternative source-grounded interpretations:** An absolute reciprocal convention, or placebo relative to anakinra as the reference direction, could generate positive 8.8. Neither is stated in the label, which does not distinguish prevention from induction for this row. The card does not choose among these explanations.

**Mechanical evidence recheck:** Fresh source renders of pp.27,29 and44 were visually reread. Patient counts, denominators, footnote marker, NNH point and harm wording were confirmed; independent signed-risk and half-unit calculations reproduced the direction comparison without transcription changes. C010 separately examines confidence-set compatibility, using a distinct rule.

**Potential downstream evidence impact:** If confirmed, extraction could associate 8.8 with induction rather than prevention of serious TEAEs, or assign a different reference direction. This is a bounded evidence-description concern, not a clinical safety judgment.

<a id="C010"></a>

## C010 — Finite NNH1 intervals versus nonsignificant source-specified safety comparisons

Pending Human Adjudication.

**Candidate statement:** The finite positive 95% NNH1 intervals for MALS and immunoparalysis omit the no-effect/infinite-number limit, while independently applying the supplied two-sided Fisher safety test to the corresponding patient counts gives nonsignificant comparisons. The connection between the confidence procedure and that test is not specified.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 13 MALS/IP counts vs eTable 15 NNH1 intervals; supplied safety test is corroboration

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-006

**Qualifying route:** Route A, category 1.

**Classification rationale:** The conflicting numerical displays are within the REPORT results supplement. The main article's methods and PLAN SAP supply the safety-test definition as corroboration; neither prints a competing numerical result. They therefore add neither S_C nor P_R.

**Classification ambiguity:** The NNH confidence construction, its analysis population and its correspondence to the Fisher safety test are undefined. The candidate does not assume identical confidence and test procedures.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.27, eTable 13, MALS and immunoparalysis Any SAE patient rows](../joi250116supp2_prod_1771885794.27755.pdf#page=27); [physical PDF p.44, eTable 15, both NNH1 intervals](../joi250116supp2_prod_1771885794.27755.pdf#page=44). Patient-count support: [physical PDF p.29, footnote a](../joi250116supp2_prod_1771885794.27755.pdf#page=29). Test corroboration: [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — physical PDF p.6, significance and SAP-following statements](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6); [joi250116supp1_prod_1771885794.26255.pdf — physical PDF p.70, SAP Safety and two-sided significance specification](../joi250116supp1_prod_1771885794.26255.pdf#page=70).

**Source evidence:** MALS NNH1 is 8.8 (95% CI, 3.2–10.0); immunoparalysis NNH1 is 47.6 (95% CI, 9.9–55.8), both labeled for induction of at least one serious TEAE. Corresponding patient counts are MALS 20/25 versus 21/23 and immunoparalysis 96/106 versus 108/122. The SAP specifies Fisher's exact comparisons of serious/nonserious TEAE incidence by immune stratum and two-sided .05 significance; the article states that analyses followed the SAP.

**Reported-versus-comparator:** Printed finite positive confidence bounds are compared with independently recomputed Fisher probabilities .419120073 and .669907887. These probabilities are calculations from supplied counts and the stated test; they are not printed publication P values. Under an ordinary reciprocal risk-difference confidence-set reading, the bounds exclude zero risk difference and the infinite-NNH no-effect limit.

**Reasoning procedure:** Confirm the patient-risk pairs, confidence level and safety-test specification. Enumerate the fixed-margin probability-order two-sided Fisher tests. Invert the positive finite NNH limits to identify the risk-difference values they represent, then compare their no-effect compatibility with those tests. The question is what confidence transformation, population and sign/set convention produced the bounds and how they relate to the named safety comparisons.

**Calculation:** The independently recomputed two-sided Fisher probabilities are .419120073 for MALS and .669907887 for immunoparalysis, both above .05. Reciprocals of the printed intervals give MALS `[1/10.0,1/3.2]=[.100000,.312500]` and immunoparalysis `[1/55.8,1/9.9]=[.017921,.101010]`, neither containing zero. Each exact-count half-unit interval contains only its displayed integer for contingency enumeration. Bound rounding also preserves positive finite limits: MALS [3.15,3.25] and [9.95,10.05]; immunoparalysis [9.85,9.95] and [55.75,55.85]. It cannot reach infinity/no effect. Route A category 1 is not screened by the .05 relative-discrepancy rule.

**Affected result or extracted value:** Confidence-set interpretation and no-effect compatibility of the two NNH1 entries, rather than the separately registered MALS direction issue in C009.

**Why context does not resolve it:** Route A, category 1 applies to the interval-versus-specified-test comparison. The missing procedure remains a bounded explanation question; attributing the interval and test to different analyses is an alternative, rather than removal of this category.

**Alternative source-grounded interpretations:** A different confidence procedure or patient population may underlie the intervals. Their finite bounds could also abbreviate a split confidence set crossing the reciprocal singularity, or use an absolute-risk-difference convention. A confidence procedure and Fisher test need not be computationally identical. None of these mappings is supplied, and no replacement interval is proposed.

**Mechanical evidence recheck:** Fresh original-page renders confirmed both confidence intervals, both patient-count pairs, the patient-count footnote and methodological corroboration. Independent exact-test enumeration reproduced the two nonsignificant probabilities. The state records the specified interval/test comparison, without determining which unreported confidence-set interpretation applies.

**Potential downstream evidence impact:** If confirmed, an extractor could record finite confidence bounds as excluding no effect despite the nonsignificant named safety comparisons, or interpret an abbreviated confidence set as an ordinary connected interval. No downstream use or conclusion change is asserted.

<a id="C011"></a>

## C011 — Five subgroup P values do not reproduce under the companion-row test

Pending Human Adjudication.

**Candidate statement:** Five panel-A P values across eFigures 7–9 do not reproduce under probability-order two-sided Fisher calculations from their printed integer counts, beyond the display threshold. The same calculation reproduces all 13 other rows under that rule.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigures 7, 8 and 9 panel A P values vs same-display counts and companion rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4.

**Classification rationale:** The conflicting counts and P values are within the REPORT results supplement. Main-article Fisher methods corroborate the calculation but do not supply a conflicting result or add S_C. This repeated pattern is one candidate; it does not assign a crude count test to panel-B model interactions.

**Classification ambiguity:** A row-specific alternative test, analysis population, sidedness or adjustment could explain the affected values, but no such distinction is printed.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.51, eFigure 7 panel A, primary response, APACHE II≥25, CCI≥5 and SOFA≥10 rows](../joi250116supp2_prod_1771885794.27755.pdf#page=51); [physical PDF p.52, eFigure 8 panel A, 28-day mortality, SOFA≥10 row](../joi250116supp2_prod_1771885794.27755.pdf#page=52); [physical PDF p.53, eFigure 9 panel A, 90-day mortality, SOFA≥10 row](../joi250116supp2_prod_1771885794.27755.pdf#page=53). Each page's remaining panel-A rows supplies companion evidence. Corroborating methods: [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — physical PDF p.6](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6).

**Source evidence:** Panel-A captions identify primary attainment, 28-day mortality and 90-day mortality. Counts below are reordered to treatment first and placebo second; reversing the source's column order does not change a two-sided Fisher probability. The five printed P values are .439, .003, .035, .045 and .209 for the named rows.

**Reported-versus-comparator:** The complete affected pattern is:

| Outcome / stratum | Treatment events/total | Placebo events/total | Printed P | Recomputed Fisher P | Minimum precision gap | Relative gap |
|---|---|---|---:|---:|---:|---:|
| Primary response, APACHE II≥25 | 12/38 | 8/40 | .439 | .303200218 | .135299782 | .308199958 |
| Primary response, CCI≥5 | 20/54 | 7/76 | .003 | .000158910 | .002341090 | .780363217 |
| Primary response, SOFA≥10 | 25/67 | 11/68 | .035 | .006531327 | .027968673 | .799104929 |
| 28-day mortality, SOFA≥10 | 35/67 | 48/68 | .045 | .034400792 | .010099208 | .224426837 |
| 90-day mortality, SOFA≥10 | 49/67 | 57/68 | .209 | .146989715 | .061510285 | .294307583 |

**Reasoning procedure:** Read every panel-A row directly and independently enumerate the exact probability-order two-sided Fisher test for its integer contingency table. Establish the method's reproduction in each display through companion rows before applying the precision rule to the five affected rows. Which test and contingency population produced those five P values remains unspecified; no source mechanism is inferred.

**Calculation:** For treatment sample size n, placebo size m, total events K and treatment events a, sum `choose(K,x)×choose(n+m−K,n−x)/choose(n+m,n)` over feasible integer x whose probability is no greater than the observed table's probability. Printed three-decimal P intervals are P±.0005: [.4385,.4395], [.0025,.0035], [.0345,.0355], [.0445,.0455] and [.2085,.2095]. Exact input-count half-unit intervals contain only the printed integer, so each recomputed P interval is a singleton. Its distance from the printed interval, divided by printed P, gives the table's relative gap; all five exceed .05.

All 13 companion rows reproduce under the stipulated rule:

| Outcome / stratum | Treatment events/total | Placebo events/total | Printed P | Recomputed Fisher P | Relative precision gap |
|---|---|---|---:|---:|---:|
| Primary response, APACHE II<25 | 34/93 | 18/105 | .002 | .002176542 | 0 |
| Primary response, CCI<5 | 26/77 | 19/69 | .475 | .474644233 | 0 |
| Primary response, SOFA<10 | 21/64 | 15/77 | .083 | .082691021 | 0 |
| 28-day mortality, APACHE II≥25 | 22/38 | 27/40 | .489 | .483109060 | .011024416 |
| 28-day mortality, APACHE II<25 | 35/93 | 45/105 | .472 | .471707802 | 0 |
| 28-day mortality, CCI≥5 | 24/54 | 50/76 | .020 | .019643739 | 0 |
| 28-day mortality, CCI<5 | 33/77 | 22/69 | .231 | .231037136 | 0 |
| 28-day mortality, SOFA<10 | 22/64 | 24/77 | .721 | .720788007 | 0 |
| 90-day mortality, APACHE II≥25 | 31/38 | 32/40 | >.99 | 1.000000000 | Inequality satisfied |
| 90-day mortality, APACHE II<25 | 59/93 | 66/105 | >.99 | 1.000000000 | Inequality satisfied |
| 90-day mortality, CCI≥5 | 39/54 | 64/76 | .123 | .125049970 | .012601380 |
| 90-day mortality, CCI<5 | 51/77 | 34/69 | .045 | .044623206 | 0 |
| 90-day mortality, SOFA<10 | 41/64 | 41/77 | .231 | .231336669 | 0 |

The two nonzero companion relative gaps remain below .05; exact agreement to every printed digit is not claimed.

**Affected result or extracted value:** The five named subgroup P values and their interpretation for primary response, 28-day mortality and 90-day mortality.

**Why context does not resolve it:** Route A, category 4 applies: the calculation reproducing all companion rows does not reproduce the five printed results beyond display precision. An unstated row-specific method is the explanation question, not a reason to treat the comparison as conditional.

**Alternative source-grounded interpretations:** Different tests, contingency populations or adjustments could underlie the five values. No immediate row label identifies such differences. These possibilities are retained without asserting which value or procedure was intended, and no exact forest-plot interval is inferred from pixels.

**Mechanical evidence recheck:** Fresh source renders confirmed all 18 contingency tables, all P entries and outcome labels. Independent exact calculations reproduced the five discrepancies and the 13 supporting rows, with no source transcription or location change.

**Potential downstream evidence impact:** If confirmed, extraction could take any of the five printed subgroup P values rather than the value produced by the companion-supported method. This concern is limited to those five entries; it does not establish a change in overall trial inference.

<a id="C012"></a>

## C012 — Repeated APACHE coefficient does not reproduce the companion interval construction

Pending Human Adjudication.

**Candidate statement:** In panel B of both eFigures 7 and 8, the APACHE II≥25 main-effect OR .47 does not reproduce the geometric center of its 95% CI .30–1.62 beyond display precision, while all five companion rows reproduce that construction under the workflow rule.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigures 7 and 8 panel B APACHE coefficient vs interval and companion rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route A, category 4.

**Classification rationale:** The points, intervals and method-support comparators are REPORT content within one results supplement. No PLAN location or cross-document conflicting result is involved. C013 separately addresses outcome attribution rather than interval construction.

**Classification ambiguity:** The precise confidence procedure is not printed. A row-specific non-log-symmetric procedure remains possible, but no such distinction is identified.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.51, eFigure 7 panel B, APACHE II≥25 main-effect row and five companions](../joi250116supp2_prod_1771885794.27755.pdf#page=51); [physical PDF p.52, eFigure 8 panel B, corresponding row and five companions](../joi250116supp2_prod_1771885794.27755.pdf#page=52).

**Source evidence:** Both pages print APACHE II≥25 OR .47 (95% CI, .30–1.62), P=.70. This is the main-effect row, distinct from the APACHE-treatment interaction immediately beneath it. The other five points and intervals are identical on both pages and are listed below.

**Reported-versus-comparator:** The point .47 is compared with `sqrt(.30×1.62)=.697137002`, the center of a log-symmetric ratio interval. Same-display companion reproduction supports the construction. The printed P=.70 is retained as a source fact; this candidate does not assert an independent exact Wald-test contradiction.

**Reasoning procedure:** Confirm the point, confidence limits, row identity and companion rows on both original pages. Evaluate the geometric center and its range over rounded interval endpoints, then compare with the printed point's precision range. Determine whether the construction also reproduces the other rows. The remaining question is which coefficient and confidence procedure produced the repeated APACHE point/interval pairing.

**Calculation:** Limits [.295,.305] and [1.615,1.625] allow center range [.690235467,.704006392]. Point .47 allows [.465,.475], giving minimum gap .215235467 and relative discrepancy `.215235467/.47=.457947802`. All five companion rows satisfy the .05 threshold:

| Row on both pages | OR (95% CI) | Geometric center | Center range from rounded limits | Minimum point-range gap | Relative gap |
|---|---|---:|---|---:|---:|
| APACHE II≥25×precision immunotherapy | 1.85 (.66–5.19) | 1.850783618 | [1.842871401,1.858675604] | 0 | 0 |
| CCI≥5 | .22 (.09–.53) | .218403297 | [.211246302,.225444006] | 0 | 0 |
| CCI≥5×precision immunotherapy | 5.79 (2.34–15.05) | 5.934391291 | [5.927062932,5.941714820] | .132062932 | .022808797 |
| SOFA≥10 | .56 (.27–1.19) | .566833309 | [.560379336,.573258232] | 0 | 0 |
| SOFA≥10×precision immunotherapy | 3.08 (1.37–6.96) | 3.087911916 | [3.081164553,3.094652646] | 0 | 0 |

The CCI-treatment row has a nonzero precision gap, but its relative gap is below .05. Thus the statement is reproduction under the workflow rule, not exact log symmetry at every printed digit.

**Affected result or extracted value:** The repeated APACHE II≥25 main-effect point and its associated confidence interval in the primary-response and 28-day-mortality panel-B outputs.

**Why context does not resolve it:** Route A, category 4 applies: the printed point does not reproduce the construction supported by all five other rows, beyond display precision. The source does not supply a row-specific interval method explaining its separation.

**Alternative source-grounded interpretations:** A non-log-symmetric confidence procedure could apply to this row, or the point and limits could refer to different coefficients or analyses. Neither interpretation is specified. No preferred procedure or replacement coefficient is proposed, and unavailable coefficient standard errors/covariance prevent reconstructing the original fit.

**Mechanical evidence recheck:** Both complete source panels were freshly rendered and visually inspected. Every source point and limit was confirmed, and independent arithmetic reproduced the affected gap and companion support. Refined companion-center arithmetic changed no source transcription, so the evidence state remains reproduced.

**Potential downstream evidence impact:** If confirmed, extraction could pair .47 with an interval generated under an unidentified construction or from a different coefficient. This concern is bounded to the repeated APACHE rows and does not establish any downstream effect.

<a id="C013"></a>

## C013 — Complete six-row output has unresolved attribution to two outcomes

Pending Human Adjudication.

**Candidate statement:** The complete six-row panel-B OR/CI/P array is identical in eFigures 7 and 8, although the captions explicitly assign it to primary response and 28-day mortality respectively. The supplied material does not identify the outcome-model mapping that explains this repeated array.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigure 7 primary-response panel B vs eFigure 8 28-day-mortality panel B

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-008

**Qualifying route:** Route B.

**Classification rationale:** The issue concerns which outcome a reported numeric array belongs to within the REPORT results supplement, rather than estimate arithmetic; its domain is therefore report_internal_inconsistency. Main-article narrative corroborates use for both outcomes but prints no competing coefficient array, so it does not add S_C. C012 independently concerns interval construction.

**Classification ambiguity:** The document roles are clear. The fitted dependent outcome, coding, coefficient meaning and model-output assignment remain insufficiently specified to explain the complete repeated array. Identical rounded outputs from distinct analyses are possible.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.51, eFigure 7 complete panel B and primary-response caption](../joi250116supp2_prod_1771885794.27755.pdf#page=51); [physical PDF p.52, eFigure 8 complete panel B and 28-day-mortality caption](../joi250116supp2_prod_1771885794.27755.pdf#page=52). Narrative corroboration: [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf — physical PDF p.7, Post Hoc and Subgroup Analyses opening](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7); [physical PDF p.8, interaction continuation](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8).

**Source evidence:** The captions expressly identify interaction tests for different outcomes. Both panels print every row below:

| Corresponding row | OR | 95% CI | P |
|---|---:|---|---:|
| APACHE II≥25 | .47 | .30–1.62 | .70 |
| APACHE II≥25×precision immunotherapy | 1.85 | .66–5.19 | .24 |
| CCI≥5 | .22 | .09–.53 | .001 |
| CCI≥5×precision immunotherapy | 5.79 | 2.34–15.05 | <.0001 |
| SOFA≥10 | .56 | .27–1.19 | .13 |
| SOFA≥10×precision immunotherapy | 3.08 | 1.37–6.96 | .007 |

**Reported-versus-comparator:** The primary-response array is compared row by row with the 28-day-mortality array, including all points, limits, P values and interaction markers. Their different panel-A event counts confirm distinct endpoints: treatment/placebo APACHE-high counts are 12/38 versus 8/40 for response and 22/38 versus 27/40 for death; CCI-high counts are 20/54 versus 7/76 and 24/54 versus 50/76; SOFA-high counts are 25/67 versus 11/68 and 35/67 versus 48/68. The main narrative associates significant high-CCI/high-SOFA interactions with both primary attainment and decreased 28-day mortality.

**Reasoning procedure:** Confirm both full arrays and the explicit outcome captions; compare corresponding rows and inspect the narrative's attribution. Distinguish direct printed equality from an explanation of how that equality arose. The unresolved question is which outcome model generated each array and which coefficients apply to each named outcome, including whether a model/coding specification explains coincident rounded output.

**Calculation:** All six ORs, 12 confidence endpoints and six P entries match between pages; their precision intervals overlap completely, giving zero numeric copy discrepancy. This is not a beyond-rounding numeric mismatch. No modeled interaction estimate is tested against a crude subgroup OR. The registered observation is the unresolved attribution of the complete repeated array to two separately named analyses with different event arrays.

**Affected result or extracted value:** Outcome assignment of all six panel-B rows, especially the CCI and SOFA interaction coefficients and tests used in the 28-day-mortality narrative.

**Why context does not resolve it:** Route B applies: the comparison concerns estimate/test attribution in focus B/C; immediate captions and narrative assign the array to distinct outcomes without explaining the model mapping; and an extractor must associate these six results with a specific outcome. Neither caption identifies a common dependent outcome or coding convention that reconciles that assignment at once.

**Alternative source-grounded interpretations:** Two distinct outcome analyses could coincidentally yield identical rounded arrays, or model/coding distinctions could explain the equality. A misassigned caption or production-stage duplication is another possible explanation, but no copying mechanism is asserted. Equality alone does not prove that the two analyses cannot coincide. The source model outputs, dependent-variable coding, reference groups, covariates and coefficient meanings needed to select an explanation are not supplied in sufficient detail.

**Mechanical evidence recheck:** Fresh source renders confirmed both complete arrays, both explicit outcome captions, different event arrays and supporting narrative. The reproduced state records those direct observations and their unresolved attribution; it is not a determination that distinct analyses must produce different numbers.

**Potential downstream evidence impact:** If confirmed, an extractor could assign these six coefficients and tests to primary response, 28-day mortality, or both without a documented model mapping. No propagation, conclusion change or judgment about the trial's overall validity follows from this card.

<a id="C014"></a>

## C014 — 90-day APACHE-treatment point lies outside its stated confidence interval

Pending Human Adjudication.

**Candidate statement:** eFigure 9 panel B prints an APACHE II≥25×precision-immunotherapy OR .11 with 95% CI .36–3.42. The point is below the interval's lower limit, including all allowed half-unit readings.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eFigure 9 panel B APACHE-treatment point vs its interval

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 1.

**Classification rationale:** The point and its confidence bounds are in one REPORT display. The issue is point containment, so the domain is statistical_results. No PLAN statement or cross-document conflicting result participates.

**Classification ambiguity:** None for document roles, row identity or containment. The source model output needed to identify the intended point/interval pairing is unavailable.

**Exact source locations:** [joi250116supp2_prod_1771885794.27755.pdf — physical PDF p.53, eFigure 9 panel B, APACHE II≥25×precision-immunotherapy row and 90-day-mortality caption](../joi250116supp2_prod_1771885794.27755.pdf#page=53).

**Source evidence:** The interaction row prints OR .11, 95% CI .36–3.42, P=.86. It is distinct from the APACHE main-effect row above it. The panel caption identifies 90-day mortality.

**Reported-versus-comparator:** The point .11 is compared with its same-row lower bound .36 and upper bound 3.42. The CI contains 1 and P=.86 is nonsignificant; the registered issue is the point outside the interval, not a separately inferred CI/P disagreement.

**Reasoning procedure:** Confirm row and column alignment from the exact source page, then test containment of the point in its labeled interval. Expand each displayed number by its half-unit precision range. No fitted-model reconstruction or raw data are necessary for this containment comparison. The unresolved question is which point and confidence limits belong to the named interaction row.

**Calculation:** `.11<.36`. The point permits [.105,.115], lower bound [.355,.365], and upper bound [3.415,3.425]. Even the maximum permitted point is below the minimum lower bound, with gap `.355−.115=.240`; relative gap `.240/.11=2.181818182`. No allowed half-unit reading permits containment. Route A category 1 is never removed by the .05 rounding exclusion.

**Affected result or extracted value:** The APACHE II≥25×precision-immunotherapy OR and confidence interval for 90-day mortality.

**Why context does not resolve it:** Route A, category 1 applies directly to a point estimate outside its interval. The immediate row does not identify a different quantity or analysis for either point or limits.

**Alternative source-grounded interpretations:** A digit or decimal substitution, or limits associated with another coefficient, could account for the display. The source does not select an explanation. Neither a geometric center nor a neighboring coefficient is adopted as a replacement point, and no exact underlying model is inferred.

**Mechanical evidence recheck:** The original page was freshly rendered and visually reread. The named interaction label, point, both bounds, P value and outcome caption matched registration. Independent half-unit arithmetic reproduced noncontainment without a source transcription or location change.

**Potential downstream evidence impact:** If confirmed, an extractor could copy this noncontaining point/interval pairing for a 90-day mortality interaction. No actual evidence propagation or conclusion change is established.
## Downstream Evidence-Chain Considerations

A reporting inconsistency may matter when a systematic review, meta-analysis, guideline or database copies a count, effect, interval, test or endpoint definition from one supplied location. The cards identify the exact quantities and specification mappings that could be affected if confirmed. They do not establish that any value has propagated, that an evidence synthesis would change, or that serious consequences occurred.

Plan/report candidates concern how prespecification and analysis definitions accompany a reported effect. Statistical-result candidates concern specific entries and confidence/test interpretation. The attribution candidate concerns which named outcome receives a coefficient array. These bounded concerns do not substitute for patient-level reanalysis or a judgment about the study as a whole.

## Limitations and Missing Definitions

All five direct sources and all 167 physical PDF pages are mapped. There is no scientific-coverage gap. The following limits constrain what can be inferred from the supplied evidence, rather than which units were reviewed.

- This is quantitative reporting quality control of the supplied paper package. No external literature, patient-level database, broad clinical or methodological assessment, or preferred-analysis comparison was used. The report does not determine study conduct, revision authorization, production mechanisms or the paper's overall validity.
- Individual SOFA trajectories and home/ward discharge histories are absent. C001/C002 can identify printed endpoint and missing-data specification differences, but cannot quantify any patient reclassification or effect change.
- The operative original-protocol-to-SAP amendment mapping, revised binary power calculation, endpoint hierarchy convention and revised infection/reversal analysis mapping are not supplied. A later SAP may legitimately revise an earlier protocol; differences are recorded without an authorization judgment.
- Biomarker trajectories, actual applied ferritin criteria and complete inclusion rules for the 125-person serial-draw subset are absent. C004 does not reconstruct its endpoint under another window or invent a denominator change.
- C007 establishes bounded nonlocation within the complete supplied article and results supplement. It does not establish that the four analysis families were never performed or that results do not exist elsewhere. Non-key survivor means, 90-day immune analyses and exploratory ROC/omics absences do not enlarge that candidate.
- Patient incidences at two through five serious adverse events, NNH confidence-construction details, signed/unsigned direction conventions and confidence-set topology are not supplied. Repeated-event totals cannot replace patient incidence. C009/C010 retain their source-confirmed comparisons while preserving alternative conventions.
- Row-specific tests/populations, coefficient standard errors/covariance, interaction outcome coding and full model definitions are unavailable. Exact forest-plot interval endpoints are not inferred from pixels. Same-display reproducing calculations are distinguished from diagnostic approximations and model-versus-crude comparisons.
- Identical rounded model outputs can occur across distinct analyses. C013 therefore concerns unresolved result-to-outcome attribution; it does not prove a production mechanism.
- Linux direct PDF/OCR executables were absent. The pinned package-local PyMuPDF/pypdf fallback, usable retained assets and direct visual inspection closed all affected units. Glyph-corrupted PLAN text was not transcription authority; unreadable retained p.18 and low-resolution pp.55–64 were freshly rendered and mapped. A readable alternative image covers p.71.
- The user-authorized RTX 5070 Laptop GPU was confirmed through PowerShell. No new OCR was needed; fresh PDF rendering was CPU. Retained GPU OCR was reused only as a source-matched locator/transcription aid.
- All fourteen candidates remain Pending Human Adjudication. Evidence state and inclusion audit document reproduction and scope-screening facts; neither constitutes an adjudication, disposition or demonstrated downstream consequence.

Candidate-specific missing inputs and supported alternative interpretations are recorded in every card. The [limitations artifact](review_1_6_2/limitations.md) preserves these boundaries separately. No missing input is filled with an inferred correction or preferred analysis.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Source and evidence preservation

Direct `sha256sum` checks confirmed all **five direct sources** and **461 retained evidence assets** unchanged at the independent audit. The before hash lists are preserved; the coordinator repeats the integrity check after Markdown assembly. New extraction, mapping, check, screening, recheck, audit and report-part artifacts are stored under `review_1_6_2/`. No old scientific review artifact was used as the discovery boundary or modified.

Canonical records are available through the [coverage manifest](review_1_6_2/coverage_manifest.md), [stable ledger](review_1_6_2/candidate_ledger.md), [recheck](review_1_6_2/verification/evidence_recheck.md) and [quality audit](review_1_6_2/quality/evidence_quality_audit.md). The final report contains every stable C ID in ledger order. Separate complete report-card parts are retained for [C001–C007](review_1_6_2/report_parts/candidate_cards_001_007.md) and [C008–C014](review_1_6_2/report_parts/candidate_cards_008_014.md), merged without dropping cards.

### Routing and local tooling

[Routing preflight](review_1_6_2/routing_preflight.md) is PASS: exact run model `gpt-6.1-sol`, source DEFAULT, coordinator high, ordinary specialists medium, and statistical/screening/recheck/audit specialists high. All ten named presets were verified. Provider is CURRENT_SESSION and execution mode INTERACTIVE_CLI. Each mandatory specialist stage used a fresh distinct runtime agent; additional plan, recheck and report-card shards have separate recorded agents.

[Tooling record](review_1_6_2/tooling_record.md) records missing Linux PDF/OCR commands, the package-local pinned fallback and derivative engines. Bootstrap ran through the user-specified `/home/juliz/venvs/stt/bin/python`; an initially restricted package-index connection was followed by an authorized successful local installation. No global package installation was performed. Windows PowerShell confirmed NVIDIA GeForce RTX 5070 Laptop GPU, driver 616.56, memory 8151 MiB. GPU_USER_REQUESTED records the user's preference; the fresh PDF derivatives used CPU and no new OCR was required. The temporary environment is removed after HTML rendering and before final validation; its removal record and the validation result are linked below.

### Agent execution

The table below reproduces every actual agent record through report assembly. Runtime IDs omit the leading slash in the durable manifest encoding. Every specialist used FRESH_SPAWN; the coordinator used CURRENT_SESSION.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_plan_1 | root/plan_mapper_1 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/plan_pages_001_032.md |
| support_quantitative_mapper_plan_2 | root/plan_mapper_2 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/plan_pages_033_064.md |
| support_quantitative_mapper_plan_3 | root/plan_mapper_3 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/plan_pages_065_072.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/inclusion_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_results_shard | root/evidence_recheck_results | gpt-6.1-sol | high | FRESH_SPAWN | verification/results_candidates_recheck.md |
| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_results_cards_shard | root/report_results_cards | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/candidate_cards_008_014.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

The complete [execution manifest](review_1_6_2/agent_execution_manifest.md) preserves primary artifact paths. [Coverage assignments](review_1_6_2/coverage_manifest.md) additionally enumerate all stage/shard artifacts and their disjoint scopes.

### Reproducibility performance

The package-specific target is a planning range, never a coverage or candidate limit. Review timing ends immediately after complete Markdown assembly; local HTML rendering and mechanical validation are excluded. The following exact fields are copied from [run state](review_1_6_2/run_state.md) at complete Markdown assembly.

- **Target basis:** Five PDFs contain 167 physical pages, including a 72-page protocol/SAP requiring visual rather than glyph-corrupted native extraction, a 54-page table/figure-rich results supplement, a 12-page main article, and 29 administrative pages. Usable source-matched assets cover 156 pages; eleven protocol pages require fresh rendering and visual mapping or user-authorized GPU OCR. Mapping needs disjoint visual shards and the mandatory checking, screening, two statistical passes, recheck, audit, and report waves. A 45-70 minute planning range allows the visual burden and full staged review despite substantial reuse.
- **Total source units:** 167
- **Fresh-source units:** 11
- **Target elapsed minutes:** 45-70
- **Started UTC:** 2026-10-11T18:28:39Z
- **Finished UTC:** 2026-10-11T19:39:04Z
- **Observed elapsed minutes:** 70.42
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete staged visual review and full fourteen-card assembly used 68.92 minutes; a post-assembly metadata repair aligned the target-status code with the validator contract and advanced the required finish record beyond the 70-minute upper bound.

### Mechanical completion record

Post-assembly SHA-256 recomputation confirms all five source PDFs and all 461 reused assets unchanged. All fourteen report cards match the final ledger's classification fields; their 294 required evidence labels are complete. Every source unit is mapped and every coverage row is complete. The standalone HTML uses the supplied 1.6.2 renderer. Temporary-environment removal is recorded in the [tooling record](review_1_6_2/tooling_record.md), and the supplied validator's final result is recorded in the [validation record](review_1_6_2/review_validation.json). These local mechanical steps are excluded from review timing.

