# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

> **Pending Human Adjudication.** Every candidate in this report awaits human adjudication. Evidence states and inclusion audits describe the review record; they do not decide the authors’ results or a candidate’s disposition.

## Executive Quality-Control Summary

Complete review of six supplied sources identified **18 stable candidate reporting issues**: 14 concern statistical results and four concern planned versus reported statistical specifications. All 18 have source-reproduced evidence and CONFIRMED inclusion audits. They address counts and denominators, standardized-effect and NNT construction, interval/test compatibility, fitted-model specification, analysis hierarchy and raw-summary identity. Repeated patterns are retained as single candidates with every affected location.

The review covers all 147 source units, 84 numeric relationship families and 263 statistical relationships through two fresh statistical passes. Independent screening recorded 27 finding decisions: 20 included findings consolidated into 18 candidates and seven screened-out findings. These counts describe this package’s completed review rather than an expected finding count.

## Package and Reused-Evidence Provenance

The supplied package reports the randomized painTRAINER, health-coach and usual-care-plus trial. Document roles follow content: the protocol and SAP are PLAN material; the main article, published intervention description, results supplement and results workbook are REPORT material.

| Source ID | Source path | Unit type | Total units | Document role | Role by content |
|---|---|---|---:|---|---|
| DOC-001 | jama_debar_2025_oi_250046_1755300121.13587.pdf | PDF_PAGE | 14 | REPORT | Main article reports randomized trial results, with abstract, methods, tables, figures and discussion. |
| DOC-002 | joi250046supp1_prod_1755300121.14087.pdf | PDF_PAGE | 77 | PLAN | UH3 study protocol, Version 5.0, November 10, 2022; prospective trial design and amendment history. |
| DOC-003 | joi250046supp2_prod_1755300121.15087.pdf | PDF_PAGE | 29 | PLAN | Statistical analysis plan specifying analyses before the reported results. |
| DOC-004 | joi250046supp3_prod_1755300121.15087.pdf | PDF_PAGE | 7 | REPORT | Published TIDieR description of study interventions; retrospective supplement describing the performed trial interventions, not a prospective operational manual. |
| DOC-005 | joi250046supp4_prod_1755300121.15587.pdf | PDF_PAGE | 19 | REPORT | Published results and analysis-method supplement with eTables and eFigures. |
| DOC-006 | joi250046supp5_prod_1755300121.16087.xlsx | WORKSHEET | 1 | REPORT | eTable 3 baseline characteristics by outcome-completion group and related reported statistics. |

Discovery was rebuilt from supplied-source evidence. At the user’s direction, earlier 1.6.2 generated content was deleted before restart and was not reused. The run reused 178 eligible immutable assets from earlier workflows, initially supporting 60 distinct units. The 87 remaining units received fresh direct-source recovery and mapping. OCR, extracted text and rendered pages serve as locators and transcription aids; exact supplied PDF pages and workbook cells control candidate evidence.

Full provenance is recorded in the [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [source hash record](review_1_6_2/source_hashes_before.sha256) and [reused-asset hash record](review_1_6_2/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

Review was limited to counts/denominators, estimate/test logic, statistical method logic and planned-versus-reported statistical design under [QUALITY_CONTROL_SCOPE.md](../QUALITY_CONTROL_SCOPE.md). No preferred analysis, clinical interpretation, novelty assessment or raw-data audit is proposed. Administrative, reference and copyright-only units were mapped along with result-bearing units.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_debar_2025_oi_250046_1755300121.13587.pdf | PDF_PAGE | 14 | 14 | 0 | 14 | COMPLETE |
| DOC-002 | joi250046supp1_prod_1755300121.14087.pdf | PDF_PAGE | 77 | 20 | 57 | 77 | COMPLETE |
| DOC-003 | joi250046supp2_prod_1755300121.15087.pdf | PDF_PAGE | 29 | 0 | 29 | 29 | COMPLETE |
| DOC-004 | joi250046supp3_prod_1755300121.15087.pdf | PDF_PAGE | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-005 | joi250046supp4_prod_1755300121.15587.pdf | PDF_PAGE | 19 | 18 | 1 | 19 | COMPLETE |
| DOC-006 | joi250046supp5_prod_1755300121.16087.xlsx | WORKSHEET | 1 | 1 | 0 | 1 | COMPLETE |

Total: **147 units = 60 initially reusable + 87 fresh-required; 147 mapped.** There is no scientific source-coverage gap. Workbook coverage includes worksheet `eTable 3`, A1:J115, with all 525 populated literal cells mapped.

Fresh visual mapping closed glyph-encoded protocol/SAP text gaps. Protocol mapping partitions physical pages 1–32, 33–64 and 65–77; all 29 SAP pages were mapped. The results supplement’s previously uncovered physical page 12 was freshly inspected. See the [complete source coverage](review_1_6_2/source_coverage.md) and [stage coverage manifest](review_1_6_2/coverage_manifest.md).

Precision-compatible differences, immediately resolvable wording, peripheral comparisons, model-versus-crude differences and unsupported conditional observations were screened under the supplied scope. A very small P value displayed as zero is not an inclusion basis. No screened-out finding has an evidence card.

## Quantitative and Statistical Relationship Coverage

The review mapped **84 numeric families** and **263 statistical relationships**, including source-matched outcome/time/contrast identities, counts and percentages, adjustment and population definitions, interval containment, effect-measure construction and planned/report specifications. Both statistical passes cover every registered statistical relationship with explicit PASS_1_COMPLETE and PASS_2_COMPLETE records, including reconciled relationships and those with named missing fitted inputs.

Pass 1 used four fresh high-effort agents. Active pass 2 used eight fresh high-effort agents across disjoint scopes after ledger, screening and recheck evidence existed. The earlier 43-page PLAN pass-2 stage remains superseded provenance; three fresh bounded repair shards, with 31, 32 and 32 inspected pages, replace it and cover all 64 PLAN relationships and all 47 original checker exclusions. Seven complementary bounded quality audits were merged without loss into the [canonical evidence-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

Numeric, cross-source and statistical checkers independently self-screened observations. Fresh inclusion screening, exact-source recheck and final inclusion/classification audit followed. The second statistical pass reopened a supported same-display test comparison, independently screened and rechecked as C018. Review coverage is documented in the [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_2/statistics/relationship_inventory.md), [pass 1](review_1_6_2/checkers/statistical_pass_1.md) and [pass 2](review_1_6_2/checkers/statistical_pass_2.md).

## Inclusion Screening Summary

A candidate requires reproduced source evidence and either an always-register category (Route A) or all three Route B conditions: in focus, unresolved by immediate context and bearing on interpretation or extraction. Numeric reproduction uses half-unit input/output intervals and the .05 relative-discrepancy threshold; interval-versus-P/test and point-containment category 1 comparisons are exempt from precision-based removal.

| Screening stage | Finding decisions | INCLUDE | SCREENED_OUT |
|---|---:|---:|---:|
| Initial | 26 | 19 | 7 |
| Pass 2 | 1 | 1 | 0 |
| Total | 27 | 20 | 7 |

| Decision | Reason code | Count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 20 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 5 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 1 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| Total | | 27 |

The 20 INCLUDE rows map to 18 distinct stable IDs. Duplicates retain their provenance and affected locations within the corresponding included issue. The final audit refined C007’s qualifying rationale to Route B while retaining its screening decision. The separately declined S218 source-expansion proposal is precision-compatible and is not an additional finding decision or candidate. Checker exclusions are reviewed in their own durable tables; they do not inflate these 27 finding decisions. Counts reconcile to the [canonical screening log](review_1_6_2/screening/inclusion_screen.md).

## Review-Domain Summary

`statistical_results` covers counts, estimates, intervals, tests and method logic in reports. `report_internal_inconsistency` covers irreconcilable attribution of a result to an outcome, time, analysis set or comparison within report material. `protocol_report` covers planned-versus-reported statistical specifications. `plan_material` covers statistical design inconsistencies solely within plan material.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 14 |
| report_internal_inconsistency | 0 |
| protocol_report | 4 |
| plan_material | 0 |
| Total | 18 |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| S_W | Within one REPORT document | 14 |
| S_C | Between different REPORT documents | 0 |
| P_R | REPORT versus PLAN | 4 |
| P_P | Solely within PLAN material | 0 |
| Total | | 18 |

Each candidate has one primary type, chosen by P_R > P_P > S_C > S_W. C005 additionally records S_C and S_W; C007 additionally records P_P. These additional relationships do not create additional candidates. Corroborating documents alone do not create a relationship.

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 18 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 18 |

All 18 inclusion audits are CONFIRMED; none is QUESTIONED. These are inclusion-threshold records and remain distinct from human adjudication.

## Candidate Index

| Stable ID and reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| [C001 — Planned versus reported online session duration](#c001) | protocol_report | P_R | reproduced | CONFIRMED |
| [C002 — Therapeutic-dose adherence percentage](#c002) | statistical_results | S_W | reproduced | CONFIRMED |
| [C003 — SMD construction across Table 3](#c003) | statistical_results | S_W | reproduced | CONFIRMED |
| [C004 — Reciprocal NNT point-reproduction pattern](#c004) | statistical_results | S_W | reproduced | CONFIRMED |
| [C005 — Age as a prespecified base adjustment covariate](#c005) | protocol_report | P_R | reproduced | CONFIRMED |
| [C006 — Secondary-analysis adjustment specification](#c006) | protocol_report | P_R | reproduced | CONFIRMED |
| [C007 — Primary versus sensitivity missing-data analysis roles](#c007) | protocol_report | P_R | reproduced | CONFIRMED |
| [C008 — RR versus finite NNT null coverage](#c008) | statistical_results | S_W | reproduced | CONFIRMED |
| [C009 — NNT point outside its confidence interval](#c009) | statistical_results | S_W | reproduced | CONFIRMED |
| [C010 — SMD points outside printed confidence intervals](#c010) | statistical_results | S_W | reproduced | CONFIRMED |
| [C011 — Covariate set of restricted primary analyses](#c011) | statistical_results | S_W | reproduced | CONFIRMED |
| [C012 — Final response-weight model predictor membership](#c012) | statistical_results | S_W | reproduced | CONFIRMED |
| [C013 — Education coding and coefficient attribution](#c013) | statistical_results | S_W | reproduced | CONFIRMED |
| [C014 — Coefficient CI versus P-value null-significance pattern](#c014) | statistical_results | S_W | reproduced | CONFIRMED |
| [C015 — Within-header three-month subset counts](#c015) | statistical_results | S_W | reproduced | CONFIRMED |
| [C016 — Raw-score summary statistic and bounds in eTable 11](#c016) | statistical_results | S_W | reproduced | CONFIRMED |
| [C017 — Workbook All Observed depression percentage](#c017) | statistical_results | S_W | reproduced | CONFIRMED |
| [C018 — Physical-function omnibus P values and contrast intervals](#c018) | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

PT denotes painTRAINER; HC denotes health coach; UC denotes usual care plus. MD is mean difference, SMD standardized mean difference, RR risk ratio, RD risk difference, OR odds ratio and NNT number needed to treat. Confidence intervals retain the source’s printed endpoints. Source-page links below use physical PDF pages.

<a id="c001"></a>

## C001 — Planned versus reported online session duration

**Candidate statement:** Candidate reporting issue: The planned 45–60-minute online session range differs from the reported 30–45-minute range, leaving the extractable session-duration convention unresolved.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main/TIDieR intervention duration vs PLAN protocol intervention duration

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route B

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** None

**Exact source locations:** Yes, all five locations: REPORT [main p.3, Health Coach Program and Online Program — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=3); PLAN [protocol p.43 §10.1.1 — joi250046supp1_prod_1755300121.14087.pdf](../joi250046supp1_prod_1755300121.14087.pdf#page=43) and [p.44 coach overview — joi250046supp1_prod_1755300121.14087.pdf](../joi250046supp1_prod_1755300121.14087.pdf#page=44); REPORT [TIDieR p.3 Procedures — joi250046supp3_prod_1755300121.15087.pdf](../joi250046supp3_prod_1755300121.15087.pdf#page=3) and [p.4 When and How Much — joi250046supp3_prod_1755300121.15087.pdf](../joi250046supp3_prod_1755300121.15087.pdf#page=4).

**Source evidence:** Main online session expectation is approximately 30–45 minutes; TIDieR prints 30–45 minutes each at both cited rows. Main/TIDieR coach expectation is 45–60 minutes. The main and TIDieR also identify eight sessions and intended completion over 12 weeks.

Protocol p.43 says each online session takes 45–60 minutes; p.44 coach sessions take 60 minutes. Both identify eight sessions and approximately weekly completion. The coach comparison overlaps and is context, not an additional duration discrepancy.

**Reported-versus-comparator:** Protocol p.43 says each online session takes 45–60 minutes; p.44 coach sessions take 60 minutes. Both identify eight sessions and approximately weekly completion. The coach comparison overlaps and is context, not an additional duration discrepancy.

**Reasoning procedure:** Focus D, Route B, permitted randomized-intervention duration comparison. Matching range endpoints describe different extracted expected session doses.

**Calculation:** Lower endpoints 45 versus 30 have intervals [44.5,45.5] and [29.5,30.5], gap 14, relative 14/45=.311111. Upper endpoints 60 versus 45 have [59.5,60.5] and [44.5,45.5], gap 14, relative 14/60=.233333. These calculations compare corresponding stated endpoints; they do not claim the two duration ranges have no overlap.

**Affected result or extracted value:** Planned and reported painTRAINER online session duration: eight sessions intended over 12 weeks.

**Why context does not resolve it:** Self-pacing and pause/resume describe delivery but do not say whether the two ranges represent content duration, expected completion time or observed time. Corresponding endpoints support different extracted session durations.

**Alternative source-grounded interpretations:** Available inputs: Session counts, stated duration ranges, intervention identity, self-pacing and pause/resume description. Missing inputs and definitions: Whether the ranges are planned content duration, anticipated self-paced completion time or observed completion time; any duration-specific amendment.

The self-paced protocol permits stopping and resuming. A changed practical estimate or a planned-versus-observed duration convention may explain the shorter range without changed content.

Does 30–45 versus 45–60 minutes describe revised online session content/dose, actual completion time or different duration conventions, and which planned and delivered duration should be extracted?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: correctly read corresponding online endpoints remain separated above .05 after display precision.

Different printed range endpoints are directly observed. A revised treatment dose or content is an unestablished explanation.

Recheck provenance: [C001](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of planned and reported painTRAINER online session duration: eight sessions intended over 12 weeks. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c002"></a>

## C002 — Therapeutic-dose adherence percentage

**Candidate statement:** Candidate reporting issue: The printed randomized painTRAINER adherence count of 371 (43%) does not reconcile with the randomized denominator of 776 under the stated display-precision rule.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main adherence paragraph vs REPORT main Figure1 counts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 3

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [main p.4 Results adherence paragraph — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) and [p.5 Figure 1 PT allocation/session counts — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=5).

**Source evidence:** Of those randomized to painTRAINER, 371 (43%) completed at least six sessions; 527 (68%) completed at least one.

Figure 1: PT randomized 776; completed 6–8 sessions 371, 1–5 sessions 156, none 249. The category counts sum to 776, and 371+156=527.

**Reported-versus-comparator:** Figure 1: PT randomized 776; completed 6–8 sessions 371, 1–5 sessions 156, none 249. The category counts sum to 776, and 371+156=527.

**Reasoning procedure:** Focus A; Route A category 3, count/denominator/percentage reconciliation for the same adherence description.

**Calculation:** 100×371/776=47.809278%. Half-unit inputs give [100×370.5/776.5,100×371.5/775.5]=[47.714102,47.904578]%. Printed 43% gives [42.5,43.5]%. Gap 4.214102 points; relative .098002. Initiator denominator 527 would give 70.398482%, not 43%.

**Affected result or extracted value:** Randomized painTRAINER completion of at least six sessions: numerator 371, denominator 776 and printed 43%.

**Why context does not resolve it:** Route A, category 3 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: Randomized denominator, exact dose-category numerator and repeated figure count. Missing inputs and definitions: Any other denominator or category underlying 43%.

The percentage could refer to an unstated denominator or adherence category; the repeated numerator and explicitly randomized wording do not identify either.

Which numerator, denominator and percentage represent randomized painTRAINER participants completing at least six sessions?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: the directly confirmed numerator and randomized denominator give a percentage interval disjoint from 43% by relative gap .098002.

The printed inputs and arithmetic discrepancy are direct. The source-production mechanism is unknown.

Recheck provenance: [C002](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of randomized painTRAINER completion of at least six sessions: numerator 371, denominator 776 and printed 43%. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c003"></a>

## C003 — SMD construction across Table 3

**Candidate statement:** Candidate reporting issue: Twenty Table 3 outcome/time rows do not reconcile with the stated common usual-care-change standard deviation for standardized mean differences, through additive, scaling or sign manifestations of one construction pattern.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main SMD definition vs REPORT main Table3 contrasts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-004, F-ST1-004

**Qualifying route:** Route A, category 4

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [main p.4 SMD definition — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [p.10 Table 3 — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10), and [p.11 continuation and footnote d — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). All twenty registered outcome/time rows and all three point-contrast columns per row were read directly.

| Individually affected location | Exact supplied-source page |
|---|---|
| Severity 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Severity 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Intensity 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Intensity 6 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Intensity 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Interference 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Interference 6 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Interference 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Social 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Social 6 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Social 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 6 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| PGIC pain 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC pain 6 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC pain 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC general 3 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC general 6 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC general 12 months | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |

**Source evidence:** The adjusted between-group mean difference is divided by the SD of change in the usual-care-plus group at the given outcome/time. Footnote d repeats the common UC denominator.

The complete printed SMD triples, and MD triples needed for the additional scaling/sign manifestations, appear below. Contrasts are PT−UC / HC−UC / HC−PT. PGIC rows are p.11; other rows p.10.

**Reported-versus-comparator:** The complete printed SMD triples, and MD triples needed for the additional scaling/sign manifestations, appear below. Contrasts are PT−UC / HC−UC / HC−PT. PGIC rows are p.11; other rows p.10.

**Reasoning procedure:** Focus B/C, stated method construction; Route A category 4 for the consolidated pattern, with Route B for the additive component. For common adjusted means and one positive SD, b=a+c. This compares model contrasts with model contrasts, not adjusted results with crude group ratios.

**Calculation:** Each printed two-decimal SMD has ±.005. Recomputed b=a+c has ±.010; displayed b has ±.005. Gap=max(0,|b−a−c|−.015). The table gives every additive manifestation, including its reference denominator |b|.

| Outcome/time | a: PT−UC | b: HC−UC | c: HC−PT | Recomputed b interval | Displayed b interval | Gap | Gap/absolute b |
|---|---:|---:|---:|---|---|---:|---:|
| Severity 3 months | −.25 | −.34 | −.13 | [−.390,−.370] | [−.345,−.335] | .025 | .073529 |
| Intensity 6 months | −.17 | −.27 | −.04 | [−.220,−.200] | [−.275,−.265] | .045 | .166667 |
| Intensity 12 months | −.16 | −.27 | −.03 | [−.200,−.180] | [−.275,−.265] | .065 | .240741 |
| Interference 3 months | −.25 | −.34 | −.13 | [−.390,−.370] | [−.345,−.335] | .025 | .073529 |
| Interference 6 months | −.27 | −.37 | −.14 | [−.420,−.400] | [−.375,−.365] | .025 | .067568 |
| Social 3 months | .12 | .01 | .20 | [.310,.330] | [.005,.015] | .295 | 29.500000 |
| Social 6 months | .18 | .06 | .26 | [.430,.450] | [.055,.065] | .365 | 6.083333 |
| Social 12 months | .19 | .07 | .27 | [.450,.470] | [.065,.075] | .375 | 5.357143 |
| Physical 3 months | .09 | −.02 | .16 | [.240,.260] | [−.025,−.015] | .255 | 12.750000 |
| Physical 6 months | .15 | .02 | .22 | [.360,.380] | [.015,.025] | .335 | 16.750000 |
| Physical 12 months | .20 | .07 | .27 | [.460,.480] | [.065,.075] | .385 | 5.500000 |
| PGIC pain 3 months | −.62 | −.62 | −.37 | [−1.000,−.980] | [−.625,−.615] | .355 | .572581 |
| PGIC pain 6 months | −.54 | −.55 | −.29 | [−.840,−.820] | [−.555,−.545] | .265 | .481818 |
| PGIC pain 12 months | −.55 | −.57 | −.29 | [−.850,−.830] | [−.575,−.565] | .255 | .447368 |
| PGIC general 3 months | −.66 | −.66 | −.40 | [−1.070,−1.050] | [−.665,−.655] | .385 | .583333 |
| PGIC general 6 months | −.46 | −.50 | −.24 | [−.710,−.690] | [−.505,−.495] | .185 | .370000 |
| PGIC general 12 months | −.53 | −.58 | −.28 | [−.820,−.800] | [−.585,−.575] | .215 | .370690 |

The remaining three registered rows have additive triples compatible with precision but fail MD/SMD scaling. With k=1/SD, k is constrained by |PT−UC SMD|/|PT−UC MD|. One-decimal MDs have ±.05; two-decimal SMDs have ±.005. The HC−PT MD is printed 0.0, giving [−.05,.05]. Its largest possible standardized magnitude is .05×(|a|+.005)/(|PT−UC MD|−.05).

| Outcome/time | Printed MD triple | Printed SMD triple | Recomputed HC−PT SMD interval | Displayed HC−PT interval | Gap | Relative gap |
|---|---|---|---|---|---:|---:|
| Severity 12 months | −.4 / −.4 / 0.0 | −.25 / −.36 / −.11 | [−.036429,.036429] | [−.115,−.105] | .068571 | .623377 |
| Intensity 3 months | −.3 / −.3 / −0.0 | −.21 / −.29 / −.08 | [−.043000,.043000] | [−.085,−.075] | .032000 | .400000 |
| Interference 12 months | −.5 / −.5 / 0.0 | −.26 / −.37 / −.12 | [−.029444,.029444] | [−.125,−.115] | .085556 | .712963 |

Additional sign manifestations within already-listed rows were confirmed: physical 3-month HC−UC MD .7 [ .65,.75 ] versus SMD −.02 [−.025,−.015]; physical 6-month HC−PT MD −.3 [−.35,−.25] versus SMD .22 [.215,.225]; physical 12-month HC−PT MD −.1 [−.15,−.05] versus SMD .27 [.265,.275]; PGIC pain 12-month HC−PT MD .1 [.05,.15] versus SMD −.29 [−.295,−.285]. A positive SD cannot reverse these signs. Additive manifestations in the table already independently satisfy the numeric precision threshold for these rows.

The same construction gives a precision-compatible reference at severity 6 months: MD −.4/−.5/−.1 and SMD −.26/−.36/−.12. From PT−UC, k∈[.255/.45,.265/.35]=[.566667,.757143]; predicted HC−UC SMD∈[−.416429,−.255], overlapping [−.365,−.355]; predicted HC−PT∈[−.113571,−.028333], gap to [−.125,−.115] .001429/.12=.011905. Its additive identity gap is .005: predicting HC−UC from the other two SMDs yields relative gap .005/.36=.013889; predicting HC−PT yields [−.110,−.090] against [−.125,−.115], relative gap .005/.12=.041667. Both remain within the .05 display-precision tolerance. This supports the same-display reproduction premise without supplying an absolute SD.

**Affected result or extracted value:** All three standardized contrasts in each of the twenty listed Table 3 outcome/time rows, including direction and standardized magnitude.

**Why context does not resolve it:** Route A, category 4 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: All point contrasts, their displayed precision, common-denominator definition and contrast headings. Missing inputs and definitions: Actual UC change SD by outcome/time; exact fitted contrasts; unrounded values; any distinct standardizers or separate-model assignments. These are needed for replacement values, not the reproduced identities.

Contrast-specific standardizers, distinct model fits or a displaced outcome/contrast assignment could explain some SMDs, but differ from the printed common-denominator definition and require explicit mapping.

Which adjusted mean differences, positive usual-care change SDs and outcome/time/contrast assignments produced every registered SMD triple, and does the printed common-SD definition apply to all Table 3 rows?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: seventeen directly read triples exceed .05 after precision, and the other three fail the same MD/SMD scaling by relative gaps .623377, .400000 and .712963.

All printed point comparisons and algebraic failures under the stated definition are direct. A column displacement or production mechanism is unestablished. No covariance, degrees of freedom or pairwise test has been reconstructed.

Recheck provenance: [C003](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of all three standardized contrasts in each of the twenty listed Table 3 outcome/time rows, including direction and standardized magnitude. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c004"></a>

## C004 — Reciprocal NNT point-reproduction pattern

**Candidate statement:** Candidate reporting issue: Three reported NNT points do not reproduce from their locally matched adjusted response percentages under the stated reciprocal definition and half-unit display rule; upward integer reporting remains an explicit alternative.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main NNT method/Table2 internally; REPORT results supplement eTable8 internally

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-005

**Qualifying route:** Route A, category 4

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [main p.4 NNT definition — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT [main p.9 Table 2 severity 6-month HC/UC, interference 6-month HC/UC and footnote d — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9); REPORT [results p.14 eTable 8 reminder-letter 6-month PT/UC and footnote d — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=14). All three affected rows were read.

| Individually affected location | Exact supplied-source page |
|---|---|
| Main severity 6 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Main interference 6 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Reminder-letter subset 6 months PT/UC | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |

**Source evidence:** NNT points are 8, 7 and 8 respectively. **Comparator matched:** Corresponding adjusted percentages are 37.1/22.9, 40.9/24.3 and 35.6/21.3. Each local footnote defines one over the adjusted response-proportion difference.

**Reported-versus-comparator:** NNT points are 8, 7 and 8 respectively. **Comparator matched:** Corresponding adjusted percentages are 37.1/22.9, 40.9/24.3 and 35.6/21.3. Each local footnote defines one over the adjusted response-proportion difference.

**Reasoning procedure:** Focus C; Route A category 4. NNT=100/(percentage-point difference), with percentage inputs ±.05 and integer point ±.5. These are adjusted proportions, not crude counts.

**Calculation:** 

| Exact affected row | Difference interval | Recomputed NNT interval | Printed NNT interval | Gap | Relative gap |
|---|---|---|---|---:|---:|
| Main severity 6-month HC/UC, 37.1−22.9 | [14.1,14.3] | [6.993007,7.092199] | [7.5,8.5] | .407801 | .050975 |
| Main interference 6-month HC/UC, 40.9−24.3 | [16.5,16.7] | [5.988024,6.060606] | [6.5,7.5] | .439394 | .062771 |
| Reminder-letter subset 6-month PT/UC, 35.6−21.3 | [14.2,14.4] | [6.944444,7.042254] | [7.5,8.5] | .457746 | .057218 |

The three reciprocal intervals above independently match the registered calculations. Same-display comparators also support the rule: main severity 12-month HC/UC 38.3−27.1 yields [8.849558,9.009009], overlapping printed 9 [8.5,9.5]; reminder-letter 3-month PT/UC 31.6−20.5 yields [8.928571,9.090909], overlapping printed 9 [8.5,9.5]. Main severity 3-month PT/UC 26.6−20.8 yields [16.949153,17.543860], overlapping printed 18 [17.5,18.5].

**Affected result or extracted value:** Main severity six-month HC/UC NNT 8; main interference six-month HC/UC NNT 7; reminder-letter subset six-month PT/UC NNT 8.

**Why context does not resolve it:** Route A, category 4 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: Adjusted rates, integer points, contrast matching and reciprocal definition. Missing inputs and definitions: Unrounded adjusted risk differences, integer reporting convention and any alternative point formula.

Upward integer rounding could explain all three points, including the supplementary row: the true reciprocal permitted by source half-unit percentage inputs can reach 7.04225352, whose ceiling is 8, while the printed-center reciprocal 6.99300699 has ceiling7. An undisplayed modeled RD could differ from the displayed rate difference. The stated half-unit rule still leaves all three printed points above the threshold; no alternative formula is supplied.

Which unrounded adjusted risk differences and integer-reporting rule produced these three NNT points?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: all three locally matched point calculations remain disjoint above relative .05.

Printed reciprocal nonreproduction is direct. Upward rounding or another RD is an explanation, not an observed implementation.

Recheck provenance: [C004](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of main severity six-month HC/UC NNT 8; main interference six-month HC/UC NNT 7; reminder-letter subset six-month PT/UC NNT 8. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c005"></a>

## C005 — Age as a prespecified base adjustment covariate

**Candidate statement:** Candidate reporting issue: Age is reported as a prespecified base adjustment factor, while the supplied explicit primary plan lists and main methods list contain six factors without age.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** REPORT main/results/workbook adjustment sets vs PLAN protocol/SAP primary adjustment sets

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** None

**Exact source locations:** Yes: PLAN [protocol p.56 §15.5 — joi250046supp1_prod_1755300121.14087.pdf](../joi250046supp1_prod_1755300121.14087.pdf#page=56); PLAN [SAP p.20 §§13–14 — joi250046supp2_prod_1755300121.15087.pdf](../joi250046supp2_prod_1755300121.15087.pdf#page=20); REPORT [main p.4 adjustment sentence — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT results [p.4 Adjustment — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.7 eTable 2 all-model variables — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8 eTable 3 age — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9 eTable 4 age — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.10 eTable 5 age — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=10); REPORT [workbook — joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, cells G2, A10, G10, directly decoded.

**Source evidence:** Supplement p.4 first lists six planned factors, then describes a prespecified base set containing seven, including age. eTable 2 includes age ≥65 versus <65 in all models. Age coefficients are .19 (.12,.27), RR 1.15 (1,1.33) and OR .97 (.70,1.35). G2 shared string 138 reads Pre-specified Adjustment Variables; A10 string 4 reads Age in years; G10 string 146 is X.

Protocol/SAP primary lists and main list contain baseline severity, sex, site, residence, multisite pain and mental-health condition, without age. SAP §13 names age as a candidate baseline variable and subgroup factor; it does not make age a fixed factor in §14's primary list.

**Reported-versus-comparator:** Protocol/SAP primary lists and main list contain baseline severity, sex, site, residence, multisite pain and mental-health condition, without age. SAP §13 names age as a candidate baseline variable and subgroup factor; it does not make age a fixed factor in §14's primary list.

**Reasoning procedure:** Focus D, Route A category 5, reported prespecification versus supplied explicit plan specification; additionally the report descriptions differ.

**Calculation:** Itemwise six-factor versus seven-factor sets differ exactly by age. Numeric coefficient equality is not the rule here. No arithmetic precision interval or relative discrepancy is applicable to membership/prespecification.

**Affected result or extracted value:** Prespecified versus implemented primary covariate set, specifically age ≥65 versus <65, and its reported base-set status.

**Why context does not resolve it:** Route A, category 5 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: All cited lists, reported coefficients, workbook selection flag and prospective document identity. Missing inputs and definitions: A prospective statement establishing age as a fixed primary adjustment term; final main-model covariate vector and timing of age's addition.

The generic baseline candidate list may have been intended to permit age selection; the base-set wording may use prespecified broadly; another amendment may have specified age. Its use is directly supported, its prespecification is unresolved.

Which prospective specification made age a fixed primary covariate, and was age included in the main-result model as prespecified or subsequently added?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: source-confirmed report language and workbook flag call age prespecified/base despite its absence from the explicit supplied primary lists.

List membership and fitted age terms are direct. Selection timing is not inferred from the age coefficients.

Recheck provenance: [C005](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of prespecified versus implemented primary covariate set, specifically age ≥65 versus <65, and its reported base-set status. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c006"></a>

## C006 — Secondary-analysis adjustment specification

**Candidate statement:** Candidate reporting issue: The report explicitly adds the baseline value of each secondary outcome to adjustment, while the plans’ explicit secondary lists name baseline pain severity and stratification variables.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main secondary adjustment vs PLAN protocol/SAP secondary adjustment

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route B

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** None

**Exact source locations:** Yes: PLAN [protocol p.57 §15.6 — joi250046supp1_prod_1755300121.14087.pdf](../joi250046supp1_prod_1755300121.14087.pdf#page=57); PLAN [SAP p.21 §15 — joi250046supp2_prod_1755300121.15087.pdf](../joi250046supp2_prod_1755300121.15087.pdf#page=21); REPORT [main p.4 secondary methods — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4), [p.10 Table 3 — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11 continuation — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

**Source evidence:** Report applies the same modeling structures as the primary analysis with added adjustment for the given baseline secondary outcome. The primary paragraph names multisite pain and mental-health condition as well as baseline severity and stratification factors.

Both plans say secondary analyses follow the same proposed approach as Aim 1; their explicit final secondary covariate sentence names baseline pain severity and all stratification variables, without the given baseline secondary-outcome value.

**Reported-versus-comparator:** Both plans say secondary analyses follow the same proposed approach as Aim 1; their explicit final secondary covariate sentence names baseline pain severity and all stratification variables, without the given baseline secondary-outcome value.

**Reasoning procedure:** Focus D, Route B, planned/reported adjustment of named secondary estimates. The outcome-specific baseline addition is the clearest explicit unmatched specification.

**Calculation:** Baseline severity and strata match; the report expressly adds each baseline secondary outcome. Importing multisite/mental-health factors is plausible under both inheritance phrases and is retained as ambiguity, not treated as an established exclusion from the plans. No numerical rounding interval applies to covariate sets.

**Affected result or extracted value:** Adjustment specification for secondary pain intensity, interference, social and physical functioning and PGIC models; the availability of a baseline PGIC value is unresolved.

**Why context does not resolve it:** The same-approach inheritance phrase could import primary factors, but does not explicitly reconcile the additional outcome-specific baseline term with the plans’ final secondary lists. The exact fitted per-outcome vector remains unidentified.

**Alternative source-grounded interpretations:** Available inputs: Both explicit secondary lists, inheritance language, main primary paragraph and secondary-result headings. Missing inputs and definitions: Planned and implemented per-outcome covariate vectors; how baseline adjustment applies to PGIC items that measure change; any prospective expansion statement.

The general same-approach language might import primary factors and the explicit plan list might be a minimum. A separate outcome-specific baseline specification may have been intended.

What exact covariate set was planned and used for each secondary outcome, including its baseline value, multisite pain and mental-health condition, and where was any expansion documented?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: the report expressly specifies an additional given-baseline-secondary-outcome adjustment absent from both explicit plan lists.

The differently explicit lists are direct. The actual fitted inclusion/exclusion of each inherited covariate is not established by these lists alone.

Recheck provenance: [C006](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of adjustment specification for secondary pain intensity, interference, social and physical functioning and PGIC models; the availability of a baseline PGIC value is unresolved. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c007"></a>

## C007 — Primary versus sensitivity missing-data analysis roles

**Candidate statement:** Candidate reporting issue: The retained SAP primary follow-up/MAR wording and the reported primary weighted-MNAR/sensitivity roles leave the final analysis hierarchy unclear, despite the disclosed amendment and conditional weighted first approach.

**Status:** Pending Human Adjudication

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT main/results primary and sensitivity roles vs PLAN SAP roles; PLAN SAP amendment vs PLAN SAP retained methods

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Qualifying route:** Route B

**Classification rationale:** A report specification conflicts with prospective plan content; P_R takes precedence over other recorded relationships.

**Classification ambiguity:** The SAP amendment and conditional weighted-first branch may explain the reported primary analysis; the retained unconditional MAR wording remains the registered comparator. Mechanical recheck confirms P_R and P_P while retaining this alternative.

**Exact source locations:** Yes: PLAN [SAP p.19 §11 — joi250046supp2_prod_1755300121.15087.pdf](../joi250046supp2_prod_1755300121.15087.pdf#page=19), PLAN [p.4 July 17, 2024 amendment — joi250046supp2_prod_1755300121.15087.pdf](../joi250046supp2_prod_1755300121.15087.pdf#page=4); REPORT [main p.4 missing-data paragraph — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4); REPORT results [p.4 Missing Data — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 Non-Response Weighting — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.9 eTable 4 — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.11 sensitivity narrative and complete-case block — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=11). P.5 was read as disclosed-amendment context in addition to the registered comparisons.

**Source evidence:** Report primary analysis uses MNAR pattern-mixture imputation among those with follow-up, nonresponse weighting for none and adjustment. Results p.4 says the >15% or differential-missingness criteria were met for this primary approach; p.5 says nonresponse weighting was formally incorporated into the SAP. eTable 4 labels the primary fit imputed and weighted; the follow-up/complete-case fit is described as sensitivity at p.11.

SAP p.19 retains the primary-follow-up/MAR sentence. Its next branch says missingness will be analyzed and sensitivity analyses conducted as required (>15% or differential); its first approach explicitly relaxes MAR using pattern-mixture imputation plus IPW, and its second approach is worst/best-case sensitivity. SAP p.4 explicitly adds IPW for no follow-up and calls pattern mixture the current approach, extending interpretation to all randomized. These amendment/branch facts are not omitted.

**Reported-versus-comparator:** SAP p.19 retains the primary-follow-up/MAR sentence. Its next branch says missingness will be analyzed and sensitivity analyses conducted as required (>15% or differential); its first approach explicitly relaxes MAR using pattern-mixture imputation plus IPW, and its second approach is worst/best-case sensitivity. SAP p.4 explicitly adds IPW for no follow-up and calls pattern mixture the current approach, extending interpretation to all randomized. These amendment/branch facts are not omitted.

**Reasoning procedure:** Focus D, Route B, primary-analysis role specification, with retained plan wording considered together with the disclosed amendment.

**Calculation:** Primary-follow-up/MAR wording remains alongside amended pattern-mixture/IPW wording and differs from the reported primary MNAR designation. No numeric-copy comparison is made: main/eTable 4 primary 3-month RRs 1.28,1.54,1.20 differ from eTable 7 complete-case RRs 1.34 (1.12,1.61),1.48 (1.24,1.75),1.10 (.94,1.29) because these are expressly distinct analyses. Precision intervals are not applicable to their primary/sensitivity labels. The complete-case results are present; no absence is asserted.

**Affected result or extracted value:** Which primary missing-data assumptions, target population and sensitivity role belong to the reported primary treatment estimates.

**Why context does not resolve it:** The SAP amendment supports IPW and current pattern-mixture estimation, and its first conditional approach could authorize the reported primary method. The retained unconditional primary-follow-up/MAR sentence and reported sensitivity label are not explicitly reconciled into one final hierarchy.

**Alternative source-grounded interpretations:** Available inputs: Final supplied SAP amendment, retained §11 language, report role labels, threshold and both reported analysis families. Missing inputs and definitions: A final approved hierarchy explicitly assigning primary versus sensitivity status and reconciling the retained MAR sentence with the amended first approach.

The amendment and conditional first approach may authorize MNAR/IPW as primary, leaving earlier primary-MAR text retained; the report may implement that intended branch. This is substantive source support, not merely a hypothetical missing amendment. The residual question is role reconciliation, not whether IPW was disclosed.

In the final approved SAP hierarchy, was primary status assigned to follow-up/MAR or weighted MNAR pattern-mixture estimation, and which clause or amendment reconciles the retained primary-MAR sentence and reported sensitivity label?


Audited qualifying-route refinement: Route B covers focusD, unresolved retained primary/MAR hierarchy versus reported primary MNAR/sensitivity designation, and the extractable primary-analysis specification. The follow-up analysis is reported as sensitivity; SAP4amendment and SAP19weightedfirstbranch remain alternatives. This refinement changes no ID, screeningdecision, evidence state, document roles or relationship codes.

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: direct final-source reading confirms the competing unconditional primary-MAR sentence and reported primary MNAR assignment, while also confirming amendment support for the latter.

Competing role/assumption statements are direct. A protocol violation, absence of the follow-up result, or lack of IPW authorization is not inferred.

Recheck provenance: [C007](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of which primary missing-data assumptions, target population and sensitivity role belong to the reported primary treatment estimates. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c008"></a>

## C008 — RR versus finite NNT null coverage

**Candidate statement:** Candidate reporting issue: Six matched HC-versus-PT RR and NNT intervals display different response-equality null coverage, without an identified RD interval construction that reconciles their extraction.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table2 RR intervals vs REPORT main Table2 NNT intervals

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-006

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [main p.9 Table 2 HC/PT columns and footnotes b,d,e — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), all six registered contrast/time rows; REPORT [p.4 binary model and NNT method — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

| Individually affected location | Exact supplied-source page |
|---|---|
| Severity 6 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Severity 12 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Intensity 3 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Intensity 12 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Interference 6 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |
| Interference 12 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 9](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) |

**Source evidence:** Each NNT interval is finite positive. **Comparator matched:** Each same-outcome/time/HC−PT RR interval contains 1. The exact pairs and reciprocal implications are reproduced below.

**Reported-versus-comparator:** Each NNT interval is finite positive. **Comparator matched:** Each same-outcome/time/HC−PT RR interval contains 1. The exact pairs and reciprocal implications are reproduced below.

**Reasoning procedure:** Focus B, Route B, ambiguity about null coverage of matched adjusted-response contrasts under the printed NNT infinity rule. RR=1 and RD=0 express equality of the same responses. This is not an interval-versus-P assertion: no pairwise P is reconstructed from omnibus P.

**Calculation:** 

| Outcome/time, HC−PT | RR (95% CI) | NNT (95% CI) | Reciprocal implied RD interval |
|---|---|---|---|
| Severity 6 months | 1.13 (.98,1.30) | 24 (12,186) | [1/186,1/12]=[.005376,.083333] |
| Severity 12 months | 1.07 (.96,1.19) | 41 (17,76) | [1/76,1/17]=[.013158,.058824] |
| Intensity 3 months | 1.11 (.93,1.33) | 37 (14,57) | [1/57,1/14]=[.017544,.071429] |
| Intensity 12 months | 1.05 (.92,1.20) | 63 (18,38) | [1/38,1/18]=[.026316,.055556] |
| Interference 6 months | 1.10 (.96,1.27) | 26 (11,67) | [1/67,1/11]=[.014925,.090909] |
| Interference 12 months | 1.07 (.97,1.18) | 39 (16,79) | [1/79,1/16]=[.012658,.062500] |

All six displayed RR intervals contain 1, while reciprocals of all finite positive NNT endpoints imply RD intervals strictly above zero. Main footnote e says an RD interval containing zero gives NNT limits reaching infinity and a negative NNH branch. Even with ±.5 on integer endpoints, all NNT endpoints remain positive finite; even with ±.005 on two-decimal RR endpoints, the listed RR lower/upper endpoints still straddle 1. The comparison is of null inclusion/interval interpretation, not a numeric-copy gap; no relative-discrepancy value is applicable to this logical observation. A common-confidence-set contradiction cannot be calculated because the RD interval construction is unspecified.

**Affected result or extracted value:** The six listed HC/PT NNT benefit intervals and their null interpretation alongside the corresponding adjusted RR intervals.

**Why context does not resolve it:** The local infinity rule explains inversion of an RD interval containing zero, but the source does not identify the RD confidence construction. Different RR/RD interval methods could reconcile the readings; immediate context does not identify which construction applies.

**Alternative source-grounded interpretations:** Available inputs: Exact matched contrasts, intervals, common binary-model description and local RD-to-NNT infinity rule. Missing inputs and definitions: RD interval endpoints before inversion; parameter-specific CI methods; joint response covariance and any distinct analyses underlying the RR/NNT columns.

RR and RD confidence intervals can use different interval constructions and yield different finite-sample null coverage. That alternative is consistent with the source's separate parameter displays; no shared variance formula is assumed.

Which RD intervals and confidence construction produced these six NNT intervals, and how should their null coverage be interpreted alongside the same-contrast RR intervals?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: all six exact-source matched pairs retain their different displayed null coverage and the source does not identify the RD interval construction needed to interpret the finite NNT limits.

Different printed null readings and reciprocal implications are direct. Incompatibility under one exact common confidence construction is not established. The intensity 12-month point-containment rule is separately recorded in C009.

Recheck provenance: [C008](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of the six listed HC/PT NNT benefit intervals and their null interpretation alongside the corresponding adjusted RR intervals. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c009"></a>

## C009 — NNT point outside its confidence interval

**Candidate statement:** Candidate reporting issue: The Table 2 twelve-month pain-intensity HC-versus-PT NNT point 63 lies outside its printed 95% interval of 18–38.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table2 NNT point vs REPORT main Table2 NNT interval

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [main p.9 Table 2 pain intensity 12 months, HC/PT NNT column — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9).

**Source evidence:** Point 63. **Comparator matched:** Printed 95% interval 18–38, in the same tuple.

**Reported-versus-comparator:** Point 63. **Comparator matched:** Printed 95% interval 18–38, in the same tuple.

**Reasoning procedure:** Focus B, Route A category 1, point containment.

**Calculation:** 63>38. Point interval [62.5,63.5] is above the largest possible upper endpoint 38.5 by 24; diagnostic relative gap 24/63=.380952. Category 1 applies directly without rounding-based removal or a distributional assumption.

**Affected result or extracted value:** The exact twelve-month pain-intensity HC/PT NNT point-and-interval tuple 63 (18–38).

**Why context does not resolve it:** Route A, category 1 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: Same-row point, endpoints and 95% label. Missing inputs and definitions: Unrounded interval and its construction, or an explicit point/interval mapping that supplies the intended tuple. No missing input prevents the containment reading.

A point or interval may belong to a different contrast/time, or a separate construction may have supplied the endpoints. No replacement is inferred from neighboring rows.

What point estimate and 95% interval belong to the 12-month pain-intensity HC/PT NNT?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: the source reads exactly 63 (18–38), and the point remains outside even after half-unit expansion.

The outside point is direct. A production mechanism or replacement endpoint is unestablished.

Recheck provenance: [C009](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of the exact twelve-month pain-intensity HC/PT NNT point-and-interval tuple 63 (18–38). The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c010"></a>

## C010 — SMD points outside printed confidence intervals

**Candidate statement:** Candidate reporting issue: Fourteen Table 3 SMD points lie outside the numerical bounds of their printed 95% intervals; endpoint sorting does not resolve the containment readings.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table3 SMD points vs REPORT main Table3 SMD intervals

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [main p.10 Table 3 — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) and [p.11 PGIC-pain continuation — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11). Every one of the fourteen registered tuples was read directly; all matched the ledger.

| Individually affected location | Exact supplied-source page |
|---|---|
| Severity 12 months PT/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Severity 12 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Intensity 12 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Interference 12 months PT/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Interference 12 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 6 months PT/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 6 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 6 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 12 months PT/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 12 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| Physical 12 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 10](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=10) |
| PGIC pain 12 months PT/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC pain 12 months HC/UC | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |
| PGIC pain 12 months HC/PT | [jama_debar_2025_oi_250046_1755300121.13587.pdf — PDF p. 11](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) |

**Source evidence:** Each point and both endpoints below are printed in the same SMD tuple; the headers say 95% CI. Physical-function endpoints are transcribed in printed order.

**Reported-versus-comparator:** Each point and both endpoints below are printed in the same SMD tuple; the headers say 95% CI. Physical-function endpoints are transcribed in printed order.

**Reasoning procedure:** Focus B, Route A category 1, point containment. Numerical sorting of physical endpoints does not remove containment failures.

**Calculation:** 

| Page; outcome/time | Contrast | Source point (printed endpoints) | Direct comparison with nearest endpoint | Half-unit point/endpoint gap |
|---|---|---|---|---:|
| 10; severity 12 months | PT/UC | −.25 (−.24,.01) | −.25<−.24 | 0 |
| 10; severity 12 months | HC/UC | −.36 (−.35,−.12) | −.36<−.35 | 0 |
| 10; intensity 12 months | HC/UC | −.27 (−.26,−.12) | −.27<−.26 | 0 |
| 10; interference 12 months | PT/UC | −.26 (−.25,.01) | −.26<−.25 | 0 |
| 10; interference 12 months | HC/UC | −.37 (−.36,−.11) | −.37<−.36 | 0 |
| 10; physical 6 months | PT/UC | .15 (.09,−.06) | .15>.09 | .05 |
| 10; physical 6 months | HC/UC | .02 (−.03,−.18) | .02>−.03 | .04 |
| 10; physical 6 months | HC/PT | .22 (.16,.05) | .22>.16 | .05 |
| 10; physical 12 months | PT/UC | .20 (.18,−.03) | .20>.18 | .01 |
| 10; physical 12 months | HC/UC | .07 (.04,−.16) | .07>.04 | .02 |
| 10; physical 12 months | HC/PT | .27 (.25,.09) | .27>.25 | .01 |
| 11; PGIC pain 12 months | PT/UC | −.55 (−.50,.05) | −.55<−.50 | .04 |
| 11; PGIC pain 12 months | HC/UC | −.57 (−.54,−.08) | −.57<−.54 | .02 |
| 11; PGIC pain 12 months | HC/PT | −.29 (−.25,.14) | −.29<−.25 | .03 |

For each printed two-decimal point and endpoint, ±.005 expansion reduces its nearest-bound separation by .010. The final column records max(0,separation−.010), including five boundary-touching cases. Category 1 applies to the direct printed point-versus-interval reading and expressly exempts it from precision-based removal, so a zero expanded gap in those five cases does not erase the observed printed containment failure. No relative-gap threshold decides these tuples.

**Affected result or extracted value:** The fourteen listed SMD point-and-interval tuples in Table 3, including their outcome/time/contrast correspondence.

**Why context does not resolve it:** Route A, category 1 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: All fourteen points/endpoints, matched row/contrast and CI label. Missing inputs and definitions: Unrounded SMD tuples, exact SMD interval method and intended contrast/time mapping needed to identify replacement values. Those inputs are unnecessary for the printed containment check.

Points or intervals may originate from distinct contrast/time assignments or another analysis. Endpoint order alone cannot explain the outside point, because it is outside the numerical minimum/maximum in every row.

Which SMD point and 95% interval belong together for each of these fourteen outcome/time/contrast tuples?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: all fourteen exact-source points lie outside both corresponding endpoints in numerical order.

All fourteen printed containment failures are direct. The cause, intended column mapping and replacement numbers are unestablished.

Recheck provenance: [C010](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of the fourteen listed SMD point-and-interval tuples in Table 3, including their outcome/time/contrast correspondence. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c011"></a>

## C011 — Covariate set of restricted primary analyses

**Candidate statement:** Candidate reporting issue: The restricted-primary subset analysis attribution and its explicit adjustment footnote differ on education and employment membership from the full selected primary model.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement full primary adjustment vs REPORT results supplement restricted primary adjustment

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-205

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT results [p.4 Adjustment — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.7 eTable 2 final imputation/estimation set — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.13 Protocol Change Subset Analyses — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=13), [p.14 eTable 8 all three blocks and footnote b — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=14). Fitted education/employment terms at [p.8 — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=8) and [p.9 — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=9) were also read as corroboration.

| Individually affected location | Exact supplied-source page |
|---|---|
| Before enhancement, 3 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| Before enhancement, 6 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| Before enhancement, 12 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| After enhancement, 3 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| After enhancement, 6 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| After enhancement, 12 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| Reminder letters, 3 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| Reminder letters, 6 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |
| Reminder letters, 12 months; all adjusted percentage, RR and NNT columns | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 14](../joi250046supp4_prod_1755300121.15587.pdf#page=14) |

**Source evidence:** P.13 identifies eTable 8 as results of the primary analysis restricted to subsets of the randomized population. Footnote b applies to every adjusted percentage/RR row and explicitly lists sex, age, site, rural/urban residence, multisite condition, mental-health diagnosis and baseline pain severity.

P.4 selection narrative and p.7 final list add education and unemployment to the primary imputation/estimation models; pp.8–9 contain both. These two selected terms are absent from eTable 8's explicit list.

**Reported-versus-comparator:** P.4 selection narrative and p.7 final list add education and unemployment to the primary imputation/estimation models; pp.8–9 contain both. These two selected terms are absent from eTable 8's explicit list.

**Reasoning procedure:** Focus C, Route B, identifying the model generating primary-outcome subset estimates. This is an explicit model-attribution comparison, not inference that unspecified imputation or weights were absent.

**Calculation:** The seven-factor subset list versus seven base factors plus education/employment is a membership difference, with no numerical precision interval. All nine affected outcome/time rows below share the footnote and restricted-primary attribution; each row's percentages, three RR/NNT contrast columns were visually located. The RR triples identify every row precisely, rather than comparing different subsets numerically.

| eTable 8 block and time | PT/UC RR | HC/UC RR | HC/PT RR | Common model-description comparison |
|---|---:|---:|---:|---|
| Before enhancement, 3 months | .96 | 1.34 | 1.39 | Full primary model versus base-only footnote b |
| Before enhancement, 6 months | 1.31 | 1.29 | .98 | Same |
| Before enhancement, 12 months | 1.59 | 1.84 | 1.16 | Same |
| After enhancement, 3 months | 1.37 | 1.60 | 1.17 | Same |
| After enhancement, 6 months | 1.53 | 1.72 | 1.13 | Same |
| After enhancement, 12 months | 1.29 | 1.33 | 1.03 | Same |
| Reminder letters, 3 months | 1.54 | 1.67 | 1.08 | Same |
| Reminder letters, 6 months | 1.67 | 1.90 | 1.14 | Same |
| Reminder letters, 12 months | 1.46 | 1.49 | 1.02 | Same |

**Affected result or extracted value:** The covariate vector generating all nine restricted-primary eTable 8 outcome/time row families, especially the three-month primary-outcome subset estimates.

**Why context does not resolve it:** The source calls these restricted primary analyses while the explicit footnote lists only the base factors. It does not say whether education/employment were dropped in refitting or only omitted from the description.

**Alternative source-grounded interpretations:** Available inputs: Full and subset covariate descriptions, model attribution and all affected rows. Missing inputs and definitions: Implemented covariate vector for each subset; whether additional predictors were reselected, dropped or only omitted from the footnote.

A deliberately refitted base-only model or an abbreviated footnote could be coherent; the source does not identify which interpretation generated these results.

Which covariates entered each eTable 8 subset estimation model, and did primary analysis restricting to subsets use the full primary set or the base-only set printed in footnote b?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: all nine row families share the restricted-primary attribution but a printed adjustment list omitting the two selected primary factors.

The different explicit lists and common attribution are direct. Actual education/employment omission from the fitted subset design matrix is not established by silence alone.

Recheck provenance: [C011](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of the covariate vector generating all nine restricted-primary eTable 8 outcome/time row families, especially the three-month primary-outcome subset estimates. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c012"></a>

## C012 — Final response-weight model predictor membership

**Candidate statement:** Candidate reporting issue: The final selected nonresponse-weight predictor list names education, while the displayed fitted model names employment and contains no education coefficient.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement weight predictor list vs REPORT results supplement fitted weight-model coefficients

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT results [p.4 Adjustment/selection — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 Non-Response Weighting — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=5), [p.7 eTable 2 final nonresponse predictors — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.10 eTable 5 full coefficient display — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=10); corroborating REPORT [workbook — joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, cells A18, H18, I18, J18.

**Source evidence:** ETable 2 additional weighting list: PEG, PHQ-8, GAD-7, any negative SDOH and education (any college versus HS or less).

ETable 5 full fit includes PEG, PHQ-8, GAD-7, negative SDOH and Not employed, OR 1.49 (1.11,2.00), P=.008; it has no education row. The local note excludes healthcare-site information, not education. Direct XML: A18 is Not employed; H18 string 356 is <.001; I18 cached .0228; J18 cached .0591. Workbook H/I/J headings distinguish primary outcome/nonresponse/3-month missingness selection tests.

**Reported-versus-comparator:** ETable 5 full fit includes PEG, PHQ-8, GAD-7, negative SDOH and Not employed, OR 1.49 (1.11,2.00), P=.008; it has no education row. The local note excludes healthcare-site information, not education. Direct XML: A18 is Not employed; H18 string 356 is <.001; I18 cached .0228; J18 cached .0591. Workbook H/I/J headings distinguish primary outcome/nonresponse/3-month missingness selection tests.

**Reasoning procedure:** Focus C, Route B, final primary weight-model membership.

**Calculation:** Four additional predictors match; the final list names education while the displayed final fit names employment. No numeric-copy or coefficient-significance comparison is the rule; rounding intervals/relative discrepancy are inapplicable to predictor membership. The workbook tests corroborate possible employment selection and do not reconcile education's absence.

**Affected result or extracted value:** Education/employment membership of the fitted response-weight model used in primary analysis.

**Why context does not resolve it:** The selected final list and full fitted display name different additional predictor membership. The local healthcare-site exclusion and workbook selection tests do not establish whether education, employment or both generated the weights.

**Alternative source-grounded interpretations:** Available inputs: Complete final selected list, displayed coefficient fit, primary weight-model narrative and selection tests. Missing inputs and definitions: Implemented predictor vector and whether an education term was omitted from display, replaced or retained in the calculated weights.

A prior selected-variable list may have persisted, the fitted display may omit education, or employment may have replaced it. The selection tests allow employment to qualify under the stated .10 criterion.

Did the final nonresponse model include education, employment or both, and which predictor vector generated the primary-analysis weights?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: exact-source final selection list and fitted coefficient display name different additional predictor membership.

Different lists are direct; implemented substitution/omission cannot be inferred solely from coefficient absence.

Recheck provenance: [C012](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of education/employment membership of the fitted response-weight model used in primary analysis. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c013"></a>

## C013 — Education coding and coefficient attribution

**Candidate statement:** Candidate reporting issue: The final education specification is binary, while each of two fitted displays contains three nonreference education coefficients with two identically printed AA labels.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement binary education specification vs REPORT results supplement education coefficients

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT results [p.7 eTable 2 final primary predictor list — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.8 eTable 3 all three education rows — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9 eTable 4 all three education rows — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=9); corroborating REPORT [workbook — joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, cells A12:A16.

| Individually affected location | Exact supplied-source page |
|---|---|
| eTable 3 first AA versus HS or less | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 second AA versus HS or less | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 graduate versus HS or less | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 4 first AA versus HS or less | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 9](../joi250046supp4_prod_1755300121.15587.pdf#page=9) |
| eTable 4 second AA versus HS or less | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 9](../joi250046supp4_prod_1755300121.15587.pdf#page=9) |
| eTable 4 graduate versus HS or less | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 9](../joi250046supp4_prod_1755300121.15587.pdf#page=9) |

**Source evidence:** Selected education is any college versus HS degree or less, a binary grouping.

All six displayed coefficients and labels below were read directly. Workbook A12 is Education; A13 High school degree or less; A14 Associate's or Technical degree; A15 College degree; A16 Doctoral or Postgraduate degree. These are direct decoded shared strings 9,10,12,14,16.

| Source model and printed row | Effect | Printed 95% CI | P |
|---|---:|---|---:|
| eTable 3 first AA versus HS or less | −.02 | [−.11,.08] | .866 |
| eTable 3 second AA versus HS or less | .16 | [.07,.25] | .077 |
| eTable 3 graduate versus HS or less | .39 | [.29,.49] | <.001 |
| eTable 4 first AA versus HS or less | RR .97 | [.82,1.16] | .770 |
| eTable 4 second AA versus HS or less | RR 1.16 | [1,1.33] | .046 |
| eTable 4 graduate versus HS or less | RR 1.35 | [1.13,1.61] | <.001 |

**Reported-versus-comparator:** All six displayed coefficients and labels below were read directly. Workbook A12 is Education; A13 High school degree or less; A14 Associate's or Technical degree; A15 College degree; A16 Doctoral or Postgraduate degree. These are direct decoded shared strings 9,10,12,14,16.

**Reasoning procedure:** Focus C, Route B, primary-model design-matrix identity and coefficient attribution. Repeated AA wording alone is not the rule; binary specification versus three distinct model parameters is.

**Calculation:** One binary variable relative to one reference group has one coefficient; both reported fits show three nonreference education coefficients. The repeated AA labels cannot map each to the distinct available categories with certainty. No numeric estimate equality is claimed and no rounding interval/relative gap applies to parameter-count/coding comparison.

**Affected result or extracted value:** Education design-matrix parameterization for imputation/estimation and attribution of all six printed education coefficients.

**Why context does not resolve it:** Three nonreference coefficients cannot identify a binary education design matrix. The duplicated AA wording and available workbook levels do not establish which coefficient belongs to which educational category or whether selection and fitting used different coding.

**Alternative source-grounded interpretations:** Available inputs: Binary selected grouping, six coefficient tuples/reference labels and available workbook categories. Missing inputs and definitions: Final education design matrix in each fit, category-to-row correspondence and whether selection coding differed from final-fit coding.

Binary education may have been used for selection while four-category education was used for final fitting; the list may summarize selection coding rather than implementation. The source does not state that distinction.

Was education binary or represented by three nonreference levels in each final imputation/estimation model, and which educational level does each printed coefficient represent?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: both exact fitted displays have three education parameters despite the explicit binary final-list specification.

Binary phrase, three coefficients and duplicated labels are direct. Assigning the second AA row to college is an unestablished reconstruction and is not made.

Recheck provenance: [C013](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of education design-matrix parameterization for imputation/estimation and attribution of all six printed education coefficients. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c014"></a>

## C014 — Coefficient CI versus P-value null-significance pattern

**Candidate statement:** Candidate reporting issue: Ten supplementary coefficient rows display 95% interval-versus-P null-significance inconsistencies under the stated .05 level.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement coefficient intervals vs REPORT results supplement coefficient P values

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-201, F-ST1-202

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT results [p.8 eTable 3 seven registered rows — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=8), [p.9 eTable 4 age and second AA rows — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=9), [p.10 eTable 5 PEG row — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=10). Method context was read at results [p.4 — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=4), [p.5 — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=5), and REPORT [main p.4 two-sided alpha=.05 — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4).

| Individually affected location | Exact supplied-source page |
|---|---|
| eTable 3 Pattern 2 follow-ups | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 Pattern 1 follow-up | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 Pattern 2 × PT | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 Pattern 2 × HC | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 Site 3 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 Site 4 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 3 second AA row | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 8](../joi250046supp4_prod_1755300121.15587.pdf#page=8) |
| eTable 4 Age ≥65 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 9](../joi250046supp4_prod_1755300121.15587.pdf#page=9) |
| eTable 4 second AA row | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 9](../joi250046supp4_prod_1755300121.15587.pdf#page=9) |
| eTable 5 PEG | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 10](../joi250046supp4_prod_1755300121.15587.pdf#page=10) |

**Source evidence:** Every same-row estimate/95% CI and P below was directly read. All ten match the ledger.

**Reported-versus-comparator:** Every same-row estimate/95% CI and P below was directly read. All ten match the ledger.

**Reasoning procedure:** Focus B, Route A category 1, displayed interval-versus-P null/significance compatibility at 95%/.05. This rule does not require reconstructing an exact test statistic.

**Calculation:** 

| Page/table; row | Source estimate (95% CI) | Comparator P | Null | Direct logical comparison |
|---|---|---:|---:|---|
| 8/eTable 3; Pattern 2 follow-ups | −.28 (−.47,−.08) | .150 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Pattern 1 follow-up | −.20 (−.36,−.03) | .226 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Pattern 2 × PT | −.30 (−.58,−.02) | .280 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Pattern 2 × HC | −.47 (−.74,−.19) | .090 | 0 | Upper endpoint <0; P>.05 |
| 8/eTable 3; Site 3 | .19 (.08,.29) | .069 | 0 | Lower endpoint >0; P>.05 |
| 8/eTable 3; Site 4 | .15 (.05,.24) | .124 | 0 | Lower endpoint >0; P>.05 |
| 8/eTable 3; second AA row | .16 (.07,.25) | .077 | 0 | Lower endpoint >0; P>.05 |
| 9/eTable 4; Age ≥65 | RR 1.15 (1,1.33) | .046 | 1 | Printed interval contains 1; P<.05 |
| 9/eTable 4; second AA row | RR 1.16 (1,1.33) | .046 | 1 | Printed interval contains 1; P<.05 |
| 10/eTable 5; PEG | OR .96 (.92,1.00) | .037 | 1 | Printed interval contains 1; P<.05 |

For the seven linear rows, even ±.005 endpoint expansion excludes zero: closest bounds become −.075,−.025,−.015,−.185,.075,.045,.065; ±.0005 P intervals remain above .05. For the two RR rows, the endpoint is literally printed 1; for PEG, 1.00. Unrounded endpoints may lie just inside the null boundary, but the scope exempts category 1 from precision-based removal. The significant P intervals [.0455,.0465] and [.0365,.0375] remain below .05. No relative numeric-gap threshold is applied to any of the ten comparisons.

**Affected result or extracted value:** The interval/P pair for each of the ten listed fitted coefficients, including three null-adjacent ratio endpoints.

**Why context does not resolve it:** Route A, category 1 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: Coefficient identity, point and interval columns, 95% labels and source .05 level. Missing inputs and definitions: Unrounded null-adjacent endpoints; coefficient-test family, variance estimator for each column, reference distribution/degrees of freedom and any different analysis assignment. The source supplies robust GEE descriptions, but not the exact numeric ingredients needed to reproduce P values.

Rounded null-adjacent endpoints may explain the three ratio rows. P values and intervals may use distinct variance/confidence constructions or correspond to different analyses. Those alternatives are retained; no normal-Wald standard errors, sidedness or df are invented.

Which analysis, variance and CI/test construction generated each of these ten rows; what are the three null-adjacent unrounded endpoints; and which interval/P pair should be extracted for every listed coefficient?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: all ten correctly read tuples show the registered displayed interval/P null-significance pattern under category 1, including the three explicitly retained null-adjacent endpoint cases.

The printed null/P comparisons are direct. A particular computation mechanism or replacement P/interval is unestablished.

Recheck provenance: [C014](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of the interval/P pair for each of the ten listed fitted coefficients, including three null-adjacent ratio endpoints. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c015"></a>

## C015 — Within-header three-month subset counts

**Candidate statement:** Candidate reporting issue: The first eTable 8 header’s three-month arm counts total 454, exceeding its 366 participants with any follow-up; the randomized-target-population interpretation remains possible.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable8 any-follow-up total vs REPORT results supplement eTable8 three-month arm counts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-003

**Qualifying route:** Route A, category 3

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: REPORT [results p.14 eTable 8 first subgroup header — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=14); corroborating REPORT [p.7 eTable 1 — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=7), [p.13 subset definition — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=13), and the second/third headers on p.14.

**Source evidence:** First header: randomized prior to 8/9/2021 N=454; PT=149, HC=153, UC=152 at 3 months.

Same header says 366 with at least one follow-up. Next block gives post-enhancement observed-at-three-month UC512/PT448/HC527; eTable 1 gives full observed-at-three-month UC621/PT542/HC635.

**Reported-versus-comparator:** Same header says 366 with at least one follow-up. Next block gives post-enhancement observed-at-three-month UC512/PT448/HC527; eTable 1 gives full observed-at-three-month UC621/PT542/HC635.

**Reasoning procedure:** Focus A, Route A category 3, nested contributors in the same header: observed-at-three-month contributors are within those with any follow-up.

**Calculation:** 149+153+152=454>366. Sum interval [452.5,455.5] versus any-follow-up [365.5,366.5] leaves minimum excess 86; relative 86/366=.234973. Corroborating full minus post-enhancement arithmetic gives UC109/PT94/HC108, total311, conditional on disjoint observed-count populations. This subtraction is not a required replacement. The first sum exactly equals randomized N=454, which supports the alternative target-population interpretation.

**Affected result or extracted value:** First eTable 8 subgroup at-three-month arm denominators PT149, HC153 and UC152, versus 366 with any follow-up.

**Why context does not resolve it:** Route A, category 3 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: All first-header counts/labels, any-follow-up total and neighboring contributor headers. Missing inputs and definitions: Whether first-header arm counts denote randomized population or observed three-month contributors; whether weighted representation explains the different count convention.

The arm counts may be randomized target-population denominators, including those represented through weights, rather than observed contributors. The header's at-three-month phrase does not identify this departure from the other blocks.

Do PT149, HC153 and UC152 denote randomized arm sizes or observed three-month contributors, and which count convention applies to the first sensitivity-analysis subgroup?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: directly read at-three-month counts exceed the same header's any-follow-up count after precision, with the denominator convention unresolved.

The count sum, labels and within-header arithmetic are direct. Subtraction-derived alternative counts and weighting interpretation are conditional explanations, not replacements.

Recheck provenance: [C015](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of first eTable 8 subgroup at-three-month arm denominators PT149, HC153 and UC152, versus 366 with any follow-up. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c016"></a>

## C016 — Raw-score summary statistic and bounds in eTable 11

**Candidate statement:** Candidate reporting issue: The eTable 11 narrative calls the raw summaries means, while its title and header call them medians and quartiles; the identity of all 21 raw-summary rows remains unclear.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement mean-summary narrative vs REPORT results supplement median/quartile table labels and values

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None. Mechanical recheck confirms S_W; the initial S_C proposal was aligned because the main scale definition is corroborating only.

**Exact source locations:** Yes: REPORT [results p.15 Additional Unadjusted Data and Analyses — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=15), [p.17 eTable 11 title/header and all 21 rows — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=17), [p.18 note b — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=18); corroborating REPORT [main p.11 PGIC footnotes h/i — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11).

| Individually affected location | Exact supplied-source page |
|---|---|
| Severity 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Severity 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Severity 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Intensity 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Intensity 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Intensity 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Interference 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Interference 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Interference 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Social 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Social 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Social 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Physical 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Physical 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| Physical 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC pain 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC pain 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC pain 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC general 3 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC general 6 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC general 12 months; PT, HC and UC raw cells | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC pain PT 6 months, 2.8 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC pain PT 12 months, 2.8 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC pain UC 12 months, 2.2 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC general PT 3 months, 2.7 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |
| PGIC general UC 6 months, 1.8 | [joi250046supp4_prod_1755300121.15587.pdf — PDF p. 17](../joi250046supp4_prod_1755300121.15587.pdf#page=17) |

**Source evidence:** Introduction says eTable 11 provides unadjusted mean secondary outcomes. Title says unadjusted median and interquartile ranges; raw-column header says Raw Score Median (25%-tile,75%tile). P.18 specifies unadjusted between-group MD/95% CI from linear GEE, without defining the raw-arm summaries.

All 21 rows' three raw-arm cells below were read directly, retaining printed bounds and mixed-width HC three-month PGIC cells. Main defines one item per PGIC pain/general outcome with response categories 1–7; it does not supply a conflicting mean/median definition.

| Outcome/time | PT raw cell | HC raw cell | UC raw cell |
|---|---|---|---|
| Severity 3 months | 5.1 (4.9,5.2) | 4.6 (4.4,4.7) | 4.6 (4.5,4.7) |
| Severity 6 months | 5.0 (4.8,5.1) | 4.4 (4.2,4.6) | 4.4 (4.2,4.5) |
| Severity 12 months | 4.8 (4.6,4.9) | 4.2 (4.1,4.4) | 4.3 (4.2,4.5) |
| Intensity 3 months | 4.9 (4.7,5.0) | 4.5 (4.3,4.6) | 4.5 (4.4,4.6) |
| Intensity 6 months | 4.8 (4.6,4.9) | 4.4 (4.2,4.5) | 4.4 (4.3,4.5) |
| Intensity 12 months | 4.6 (4.4,4.7) | 4.2 (4.1,4.4) | 4.3 (4.2,4.4) |
| Interference 3 months | 5.2 (5.0,5.3) | 4.6 (4.4,4.8) | 4.6 (4.5,4.7) |
| Interference 6 months | 5.1 (4.9,5.2) | 4.4 (4.2,4.6) | 4.4 (4.2,4.6) |
| Interference 12 months | 4.9 (4.7,5.1) | 4.2 (4.0,4.4) | 4.3 (4.2,4.5) |
| Social 3 months | 43.4 (42.8,44.0) | 44.6 (43.9,45.3) | 44.8 (44.4,45.2) |
| Social 6 months | 43.6 (42.9,44.2) | 45.4 (44.7,46.0) | 45.1 (44.7,45.4) |
| Social 12 months | 43.9 (43.3,44.6) | 45.8 (45.1,46.5) | 45.3 (44.8,45.8) |
| Physical 3 months | 37.7 (37.1,38.2) | 38.2 (37.7,38.8) | 38.2 (37.7,38.8) |
| Physical 6 months | 37.9 (37.3,38.4) | 38.9 (38.4,39.5) | 38.3 (37.8,38.8) |
| Physical 12 months | 37.9 (37.3,38.4) | 39.1 (38.5,39.7) | 38.8 (38.1,39.4) |
| PGIC pain 3 months | 2.9 (2.8,2.9) | 2.0 (1.0,3.0) | 1.9 (1.9,2.0) |
| PGIC pain 6 months | 2.8 (2.7,2.9) | 2.1 (2.0,2.2) | 2.1 (2.0,2.2) |
| PGIC pain 12 months | 2.8 (2.7,2.9) | 2.1 (2.0,2.2) | 2.2 (2.1,2.3) |
| PGIC general 3 months | 2.7 (2.6,2.7) | 2.0 (1.0,2.0) | 1.6 (1.5,1.6) |
| PGIC general 6 months | 2.5 (2.4,2.6) | 2.0 (1.9,2.1) | 1.8 (1.7,1.9) |
| PGIC general 12 months | 2.6 (2.4,2.7) | 1.9 (1.8,2.1) | 1.9 (1.7,2.0) |

**Reported-versus-comparator:** All 21 rows' three raw-arm cells below were read directly, retaining printed bounds and mixed-width HC three-month PGIC cells. Main defines one item per PGIC pain/general outcome with response categories 1–7; it does not supply a conflicting mean/median definition.

**Reasoning procedure:** Focus C, Route B, extractable statistical summary identity and bounds. Mean and median/quartile labels name different statistical quantities. This affects all 21 raw-summary rows, regardless of the additional numerical diagnostic.

**Calculation:** The mean narrative and median/quartile title/header do not establish the same summary. For an ordinary empirical median of one-item integer responses, the central value is on the integer/half-integer grid. Comparing a one-decimal printed center interval ±.05 with the nearest exact grid value gives the five above-threshold centers below. The grid constraint uses exact integer response categories, not rounded sample inputs.

| Exact PGIC cell | Printed-center interval | Nearest ordinary-median value | Gap | Relative gap |
|---|---|---:|---:|---:|
| Pain PT 6 months, 2.8 | [2.75,2.85] | 3 | .15 | .053571 |
| Pain PT 12 months, 2.8 | [2.75,2.85] | 3 | .15 | .053571 |
| Pain UC 12 months, 2.2 | [2.15,2.25] | 2 | .15 | .068182 |
| General PT 3 months, 2.7 | [2.65,2.75] | 2.5 | .15 | .055556 |
| General UC 6 months, 1.8 | [1.75,1.85] | 2 | .15 | .083333 |

The stated gap is the distance to the nearest grid value. Other fractional PGIC centers were checked: 2.9 gives .05/2.9=.017241; 2.6 gives .05/2.6=.019231; 2.1 gives .05/2.1=.023810; 1.9 gives .05/1.9=.026316; 1.6 gives .05/1.6=.031250; 2.0 and 2.5 have zero gap. These do not independently exceed .05. The numerical median diagnostic is restricted to its stated ordinary definition; the summary-label conflict does not assume that every possible interpolated/set-valued median excludes these values. No equality between raw medians and fitted MDs is assumed, and no arm permutation is inferred.

**Affected result or extracted value:** The central statistic and bound type in every eTable 11 raw-arm cell, especially the mixed-width HC three-month PGIC cells and the five precision-qualified centers.

**Why context does not resolve it:** The mean narrative and median/quartile header name different extractable quantities; the GEE note defines between-group differences only. Neither the raw-arm summary definition nor possible intentional mixing of summary types is specified.

**Alternative source-grounded interpretations:** Available inputs: Narrative/title/header identities, all 63 raw cells, local MD-method note and one-item scale definition. Missing inputs and definitions: Raw central-statistic and bound method per arm/outcome/time; empirical/interpolated/weighted median definition; whether summary types are intentionally mixed; raw item responses/sample medians needed to reconstruct values.

Most cells could be means with confidence intervals while the two wide HC three-month PGIC cells are medians/quartiles; an interpolated, set-valued or model-based summary could explain fractional centers. The local note defines between-group MDs only and does not resolve the raw-arm columns.

What central statistic and bound method were used for each raw-arm eTable 11 cell, especially the HC three-month PGIC cells; was any interpolation or mixed summary intentional; and which entries should be extracted as means/CI versus medians/quartiles?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: exact-source narrative and table raw-summary labels remain different, all 21 affected rows are located, and five stated-definition median diagnostics exceed precision tolerance.

Conflicting summary labels and exact cell shapes are direct. Calling cells means, medians, confidence intervals or quartiles beyond the printed competing labels is an unestablished reconstruction. The ordinary-median grid result is an explicitly qualified calculation.

Recheck provenance: [C016](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of the central statistic and bound type in every eTable 11 raw-arm cell, especially the mixed-width HC three-month PGIC cells and the five precision-qualified centers. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c017"></a>

## C017 — Workbook All Observed depression percentage

**Candidate statement:** Candidate reporting issue: The workbook All Observed depression entry 711 (73.2) does not reconcile with N=1568, two missing values and the stated nonmissing-denominator rule.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT workbook eTable3 count/percentage vs REPORT workbook denominator/missing count/footnote

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 3

**Classification rationale:** The conflicting values or specifications are internal to the report material; corroborating definitions do not create a cross-document relationship.

**Classification ambiguity:** None

**Exact source locations:** Yes: supplied REPORT [workbook — joi250046supp5_prod_1755300121.16087.xlsx](../joi250046supp5_prod_1755300121.16087.xlsx), worksheet exactly `eTable 3`, E3, A82, E82, A83, E83, A110. Direct workbook.xml confirms worksheet name and worksheet relationship; direct sheet1.xml/sharedStrings.xml confirms all cells. B82/C82/D82 were also read as count-partition corroboration.

**Source evidence:** E82 has shared-string index 290, decoded as 711 (73.2). A82 index 96 reads Current depression (PHQ-8 ≥10), No. (%).

E3 index144=(N=1568); A83 index109=Missing; E83 numeric2; A110 index355 says missing is reported as n but excluded from the denominator in the reported percentage. E2's All Observed group identity is consistent with the source group headings. B82=1116 (47.9), C82=162 (54.9), D82=243 (51.9) corroborate count alignment: 162+243+711=1116.

**Reported-versus-comparator:** E3 index144=(N=1568); A83 index109=Missing; E83 numeric2; A110 index355 says missing is reported as n but excluded from the denominator in the reported percentage. E2's All Observed group identity is consistent with the source group headings. B82=1116 (47.9), C82=162 (54.9), D82=243 (51.9) corroborate count alignment: 162+243+711=1116.

**Reasoning procedure:** Focus A, Route A category 3, same-workbook-display numerator/percentage/denominator reconciliation under the explicit missing-value footnote.

**Calculation:** Nonmissing denominator 1568−2=1566; 100×711/1566=45.402299%. Half-unit N/missing inputs give denominator [1565,1567], numerator [710.5,711.5]. Recomputed percentage interval [100×710.5/1567,100×711.5/1565]=[45.341417,45.463259]%. Printed percentage [73.15,73.25]%. Gap 27.686741 points; relative 27.686741/73.2=.378234. A denominator approximately 711/.732=971.311475 would be required for the central printed percentage, rather than the stated nonmissing 1566.

**Affected result or extracted value:** Workbook eTable 3 E82 All Observed current-depression count/percentage and its assessment denominator.

**Why context does not resolve it:** Route A, category 3 applies to the reproduced rule above. The inclusion scope retains this category even when the intended quantity may be reconstructable or an inferential/reporting convention remains unnamed.

**Alternative source-grounded interpretations:** Available inputs: Exact cached source cell text, group denominator, missing count, current-depression label and percentage rule. Missing inputs and definitions: Any restricted PHQ-8 assessment denominator supporting 73.2, or an alternate numerator definition for that cell.

A restricted assessment population might produce another denominator, but no such denominator is stated in the cell/group/footnote. The source-production mechanism remains unknown.

What numerator and nonmissing denominator support the 73.2% printed in `eTable 3` E82?

**Mechanical evidence recheck:** All cited locations and compared values were directly confirmed against the supplied source. Determining fact: direct source XML confirms 711 (73.2), N1568, missing2 and the nonmissing-denominator rule, leaving relative gap .378234.

Decoded cells and arithmetic are direct. Restricted denominator or substituted percentage is an unestablished explanation; no replacement is assigned.

Recheck provenance: [C017](review_1_6_2/verification/evidence_recheck.md) and [inclusion-quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed in human adjudication, this candidate could affect extraction of workbook eTable 3 E82 All Observed current-depression count/percentage and its assessment denominator. The review does not establish that downstream reuse or a conclusion change occurred.

<a id="c018"></a>

## C018 — Physical-function omnibus P values and contrast intervals

**Candidate statement:** Candidate reporting issue: The eTable 11 six- and twelve-month physical-function omnibus P values do not reconcile with their contrast intervals under an explicitly diagnostic normal-CI/common-covariance/chi-square-2 Wald reconstruction that is precision-feasible for the other 19 rows.

**Status:** Pending Human Adjudication

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable11 omnibus P values vs REPORT results supplement MD95%CI contrasts and method context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST2-1001

**Qualifying route:** Route A, category 1

**Classification rationale:** Both compared inferential columns are internal to REPORT results supplement eTable11; main REPORT methods corroborate the tested family and do not add a conflicting cross-document relationship.

**Classification ambiguity:** Exact CI/test reference distributions, degrees of freedom, covariance and estimand mapping are not supplied. Different inferential implementations remain explicit alternatives.

**Exact source locations:**

| Exact supplied-source location | Location found | Source value/text matched | Comparator matched | Content role |
|---|---|---|---|---|
| [Results supplement PDF p17, eTable 11 Physical Functioning 6 months — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; every affected contrast and P cell visually read | PT−UC 1.1 (0.3,1.9); HC−UC 0.4 (−0.3,1.1); HC−PT −0.6 (−1.4,0.1) | Omnibus P=0.005 in the same six-month row | REPORT |
| [Results supplement PDF p17, eTable 11 Physical Functioning 12 months — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; every affected contrast and P cell visually read | PT−UC 1.2 (0.4,2.0); HC−UC 0.9 (0.0,1.8); HC−PT −0.3 (−1.2,0.6) | Omnibus P=0.001 in the same twelve-month row | REPORT |
| [Results supplement PDF p17, all other 19 eTable 11 outcome/time rows — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=17) | Yes; all 57 corroborating mean-difference/CI tuples and 19 Ps visually read | Complete transcription appears below | All 19 feasible witnesses independently recalculated against their own exact printed tuples, not against the target rows | REPORT, same-display corroboration |
| [Results supplement PDF p18, eTable 11 note b — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=18) | Yes | Unadjusted between-group mean differences and 95% confidence intervals were calculated with a linear regression model fit using generalized estimating equations for each continuous outcome | Matches the inferential-column identity of eTable 11; no explicit normal critical value, covariance, omnibus distribution or df supplied | REPORT |
| [Results supplement PDF page 15, Additional Unadjusted Data and Analyses — joi250046supp4_prod_1755300121.15587.pdf](../joi250046supp4_prod_1755300121.15587.pdf#page=15) | Yes | Tables 2 and 3 replicated with no adjustment, weighting or imputation; eTable 10 gives unadjusted mean change and eTable 11 gives unadjusted mean secondary outcomes | Supplies broad replicated-analysis context, not an explicit statement that every inferential implementation is identical | REPORT |
| [Main article PDF p11, Table 3 note c — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=11) | Yes | Omnibus P value is the Wald test assessing any difference among the three groups; between-group comparisons follow omnibus P<.05 using the least significant difference approach | Corroborates a three-group Wald family for the main adjusted display; not an exact supplement df/covariance declaration | REPORT, corroboration only |
| [Main article PDF p4, Statistical Analysis — jama_debar_2025_oi_250046_1755300121.13587.pdf](../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) | Yes | GEE with working-independence correlation and robust sandwich standard errors; linear GEE for continuous secondary outcomes; all tests two-sided with alpha=.05 | Corroborates the broad fitted family and confidence/testing context; exact eTable 11 inferential distributions remain absent | REPORT, corroboration only |

The rendered p17 heading is unadjusted between-group mean differences (95%CI), with PT vs UC, HC vs UC and HC vs PT columns and a separately named omnibus P column. No pairwise P value is printed. The comparison does not equate raw medians with fitted means, and does not equate a single pairwise null with the omnibus null.

**Source evidence:**

All entries below were reread visually from the exact supplied-source p17 render. The 19 remaining rows support a reproducible numerical family; only physical six/twelve months are affected locations of this candidate.

| Relationship | Outcome/time | PT−UC estimate (95%CI) | HC−UC estimate (95%CI) | HC−PT estimate (95%CI) | Omnibus P |
|---|---|---|---|---|---|
| S601 | Pain severity 3 months | -0.5 (-0.7, -0.3) | -0.5 (-0.7, -0.3) | 0 (-0.2, 0.2) | <.001 |
| S602 | Pain severity 6 months | -0.6 (-0.8, -0.3) | -0.6 (-0.8, -0.3) | 0 (-0.2, 0.2) | <.001 |
| S603 | Pain severity 12 months | -0.5 (-0.8, -0.3) | -0.4 (-0.6, -0.2) | 0.1 (-0.1, 0.3) | <.001 |
| S604 | Pain intensity 3 months | -0.4 (-0.6, -0.2) | -0.3 (-0.5, -0.1) | 0 (-0.2, 0.2) | <.001 |
| S605 | Pain intensity 6 months | -0.4 (-0.6, -0.2) | -0.4 (-0.6, -0.2) | 0 (-0.2, 0.2) | <.001 |
| S606 | Pain intensity 12 months | -0.3 (-0.6, -0.1) | -0.2 (-0.4, -0.1) | 0.1 (-0.1, 0.3) | <.001 |
| S607 | Pain-related interference 3 months | -0.6 (-0.8, -0.3) | -0.6 (-0.8, -0.4) | 0 (-0.2, 0.2) | <.001 |
| S608 | Pain-related interference 6 months | -0.7 (-0.9, -0.4) | -0.7 (-0.9, -0.4) | 0 (-0.3, 0.2) | <.001 |
| S609 | Pain-related interference 12 months | -0.6 (-0.9, -0.4) | -0.5 (-0.8, -0.3) | 0.1 (-0.1, 0.3) | <.001 |
| S610 | Social functioning 3 months | 1.2 (0.3, 2.1) | 1.4 (0.7, 2.2) | 0.2 (-0.5, 1) | 0.001 |
| S611 | Social functioning 6 months | 1.8 (0.9, 2.7) | 1.5 (0.8, 2.2) | -0.3 (-1, 0.4) | <.001 |
| S612 | Social functioning 12 months | 1.8 (0.9, 2.8) | 1.4 (0.5, 2.2) | -0.5 (-1.3, 0.3) | <.001 |
| S613 | Physical functioning 3 months | 0.6 (-0.2, 1.3) | 0.6 (-0.2, 1.3) | 0 (-0.8, 0.8) | 0.212 |
| S614 | Physical functioning 6 months | 1.1 (0.3, 1.9) | 0.4 (-0.3, 1.1) | -0.6 (-1.4, 0.1) | 0.005 |
| S615 | Physical functioning 12 months | 1.2 (0.4, 2) | 0.9 (0, 1.8) | -0.3 (-1.2, 0.6) | 0.001 |
| S616 | PGIC pain 3 months | -0.8 (-0.9, -0.6) | -0.9 (-1, -0.8) | -0.2 (-0.3, 0) | <.001 |
| S617 | PGIC pain 6 months | -0.7 (-0.8, -0.5) | -0.7 (-0.8, -0.5) | 0 (-0.2, 0.1) | <.001 |
| S618 | PGIC pain 12 months | -0.7 (-0.8, -0.5) | -0.6 (-0.7, -0.4) | 0.1 (-0.1, 0.2) | <.001 |
| S619 | PGIC general 3 months | -0.8 (-0.9, -0.6) | -1.1 (-1.2, -1) | -0.3 (-0.5, -0.2) | <.001 |
| S620 | PGIC general 6 months | -0.6 (-0.7, -0.4) | -0.8 (-0.9, -0.6) | -0.2 (-0.3, 0) | <.001 |
| S621 | PGIC general 12 months | -0.6 (-0.8, -0.4) | -0.7 (-0.8, -0.5) | -0.1 (-0.2, 0.1) | <.001 |

**Reported-versus-comparator:** Physical functioning at six months: PT−UC 1.1 (0.3,1.9), HC−UC 0.4 (−0.3,1.1), HC−PT −0.6 (−1.4,0.1), omnibus P=.005. At twelve months: PT−UC 1.2 (0.4,2.0), HC−UC 0.9 (0.0,1.8), HC−PT −0.3 (−1.2,0.6), omnibus P=.001. The independently supported diagnostic bounds are P≥.013869766053172373 and P≥.0021537112129520757, respectively. These bounds describe the tested reconstruction, not replacement reported P values.

**Reasoning procedure:** Test an explicitly diagnostic family using symmetric normal 95% contrast intervals, common contrast covariance and a two-dimensional chi-square Wald tail. Establish its same-display numerical support with precision-feasible witnesses for every other row, then bound both affected rows over conservative half-unit input domains. Exact CI and test reference distributions are not supplied; the diagnostic does not identify the actual fitted implementation.

**Calculation:**

**Rule applicable:** Yes, as an explicitly labeled diagnostic reconstruction supported by the same display. Let a=PT−UC, b=HC−UC and c=HC−PT=b−a. Under symmetric normal 95% intervals use z=1.959963984540054, interval halfwidths h_j, variances v_j=(h_j/z)^2 and covariance u=(v_a+v_b−v_c)/2. The two-dimensional joint Wald statistic is

Q=(v_b a²+v_a b²−2uab)/(v_a v_b−u²),

with diagnostic chi-square with 2 degrees of freedom tail P=exp(−Q/2). This reconstructed covariance is algebra within the tested family; it is not a claim about the authors' actual fitted covariance.

For every witness below, the independent rechecker checked additive contrast identity, positive determinant, each point and both symmetric endpoints against the corresponding source number ±.05, and the computed tail against numeric P±.0005 or printed <.001. Arithmetic tolerance 1e−12 only accommodates floating-point endpoints. All 19 pass. These witnesses prove feasibility for these rows under this diagnostic family, not the actual undisclosed fitted implementation.

| Relationship | Witness (a,b,c) | Witness halfwidths | Diagnostic Q | Diagnostic P | Largest point/endpoint gap | All witness constraints met |
|---|---|---|---:|---:|---:|---|
| S601 | (-0.549, -0.549, 0) | (0.199, 0.199, 0.15) | 34.077570344 | 3.9824434849e-8 | 0.050000 | Yes |
| S602 | (-0.6, -0.6, 0) | (0.25, 0.25, 0.15) | 24.315167920 | 0.0000052484174757 | 0.050000 | Yes |
| S603 | (-0.549, -0.449, 0.1) | (0.201, 0.199, 0.15) | 29.340551305 | 4.2538310425e-7 | 0.050000 | Yes |
| S604 | (-0.398, -0.349, 0.049) | (0.152, 0.199, 0.199) | 28.892830604 | 5.3211015956e-7 | 0.050000 | Yes |
| S605 | (-0.449, -0.449, 0) | (0.199, 0.199, 0.15) | 22.793793846 | 0.000011230279251 | 0.050000 | Yes |
| S606 | (-0.349, -0.249, 0.1) | (0.201, 0.101, 0.15) | 23.354754552 | 0.0000084835863752 | 0.050000 | Yes |
| S607 | (-0.6, -0.649, -0.049) | (0.25, 0.199, 0.199) | 41.641881462 | 9.0694370878e-10 | 0.050000 | Yes |
| S608 | (-0.7, -0.7, 0) | (0.25, 0.25, 0.25) | 40.156049539 | 1.9064465561e-9 | 0.050000 | Yes |
| S609 | (-0.649, -0.549, 0.1) | (0.201, 0.201, 0.15) | 41.341524438 | 1.0539063750e-9 | 0.050000 | Yes |
| S610 | (1.151, 1.4, 0.249) | (0.899, 0.75, 0.701) | 13.411989543 | 0.0012235549409 | 0.050000 | Yes |
| S611 | (1.751, 1.451, -0.3) | (0.899, 0.699, 0.65) | 18.441295422 | 0.000098974559956 | 0.050000 | Yes |
| S612 | (1.802, 1.351, -0.451) | (0.948, 0.801, 0.799) | 15.726369532 | 0.00038464690825 | 0.050000 | Yes |
| S613 | (0.551, 0.552, 0.001) | (0.701, 0.798, 0.849) | 3.101587512 | 0.21207956755 | 0.050000 | Yes |
| S616 | (-0.798, -0.949, -0.151) | (0.148, 0.099, 0.101) | 375.441268582 | 2.9782722021e-82 | 0.050000 | Yes |
| S617 | (-0.7, -0.7, 0) | (0.15, 0.15, 0.15) | 111.544582053 | 6.0034619739e-25 | 0.050000 | Yes |
| S618 | (-0.7, -0.6, 0.1) | (0.15, 0.15, 0.15) | 97.886061801 | 5.5502398618e-22 | 0.050000 | Yes |
| S619 | (-0.8, -1.149, -0.349) | (0.15, 0.099, 0.101) | 611.340829900 | 1.7742936821e-133 | 0.050000 | Yes |
| S620 | (-0.6, -0.8, -0.2) | (0.15, 0.15, 0.15) | 118.373842178 | 1.9744528631e-26 | 0.050000 | Yes |
| S621 | (-0.649, -0.7, -0.051) | (0.199, 0.15, 0.101) | 93.615347054 | 4.6955414279e-21 | 0.050000 | Yes |

In particular social three months produces .001223554941 within [.0005,.0015], physical three months .21207956755 within [.2115,.2125], and all other 17 witnesses produce P<.001. The witnesses match source printed values and demonstrate same-display numerical support; no witness is offered as an author estimate.

Each displayed target point and CI endpoint receives ±.05. Numeric omnibus P receives ±.0005. Full feasible point/endpoint coupling is conservatively relaxed when forming the following bounding domains.

For physical six months: a∈[1.05,1.15], b∈[.35,.45], c=b−a∈[−.65,−.55] yields the point triangle (1.05,.40), (1.05,.45), (1.10,.45). Endpoint rounding permits the enlarged halfwidth boxes [.75,.85], [.65,.75], [.70,.80]. The independent rechecker separately evaluated all 24 point/variance-vertex combinations. Minimum covariance determinant 0.01195380636846352; maximum Q=8.556087823817016 at a=1.10,b=.45,h=(.75,.75,.70). Thus diagnostic P≥0.013869766053172373.

For physical twelve months: deliberately retain the larger point rectangle a∈[1.15,1.25], b∈[.85,.95], dropping the c constraint, and enlarged halfwidth boxes [.75,.85], [.85,.95], [.85,.95]. The independent rechecker separately evaluated all 32 point/variance-vertex combinations. Minimum covariance determinant 0.02217991416023505; maximum Q=12.281125558721055 at a=1.25,b=.95,h=(.75,.85,.95). Thus diagnostic P≥0.0021537112129520757.

The proof is not a grid search: Q=d′V⁻¹d is convex in d for fixed positive-definite V and convex in positive-definite V for fixed d; V is affine in the three contrast variances. All variance-box vertices are positive definite, hence so is their convex hull. Successive convexity therefore bounds Q by its point/variance-vertex maximum. Dropping point/endpoint halfwidth coupling, and the twelve-month c constraint, enlarges the feasible domains and preserves the bounds. Every actually precision-feasible tuple lies inside these conservative domains.

| Affected result | Conservative recomputed diagnostic P interval | Printed P half-unit interval | Minimum separating gap | Gap / absolute printed P |
|---|---|---|---:|---:|
| Physical functioning 6 months | [.013869766053172373,1] | [.0045,.0055] | .008369766053172373 | 1.6739532106344746 |
| Physical functioning 12 months | [.0021537112129520757,1] | [.0005,.0015] | .0006537112129520757 | .6537112129520757 |

**Calculation reproduced:** Yes, independently in JavaScript V8. Both outer diagnostic P intervals remain separated from the printed intervals even after conservative allowance for all displayed input precision. Route A category 1 is independently exempt from rounding-based removal. The intervals' upper endpoints of 1 are deliberately loose logical bounds, not attainable maxima or fitted-P estimates. No replacement P is proposed. Both printed omnibus Ps and at least one contrast interval in each affected row indicate a result below .05; this candidate makes no claim of a .05-level conclusion reversal.

**Affected result or extracted value:** The unadjusted six- and twelve-month physical-function omnibus significance strength and the fitted analysis represented by P=.005/.001 alongside the three MD/95%CI contrasts.

**Why context does not resolve it:** Route A, category 1 applies to this independently supported interval/test compatibility comparison. A common reconstruction is precision-feasible for the other 19 rows, while both target rows remain separated under conservative bounds. The unnamed inferential mapping remains the question; it does not establish any actual author covariance or a .05-level conclusion reversal.

**Alternative source-grounded interpretations:**

**Necessary inputs available:** Every printed target estimate, both interval limits, row/time and contrast identity, confidence level 95%, corresponding numeric omnibus P, all 19 same-display comparators, linear-GEE interval definition and broad replicated Wald-test context. These are sufficient to reproduce the diagnostic comparison and precision bounds.

**Necessary inputs unavailable for identification of the actual fitted analysis:** Unrounded estimates/interval endpoints; actual contrast covariance matrix; actual confidence critical value/reference distribution; omnibus reference distribution and degrees of freedom; explicit mapping of each omnibus P and contrast interval to the same covariance, fitted analysis and estimand; per-outcome/time sample size and missingness denominators; participant-level observations. The normal z and chi-square with 2 degrees of freedom reference distribution are diagnostic choices, not reported facts.

**Source-grounded alternative interpretation:** eTable 11 note b identifies GEE intervals without explicitly naming their reference distribution, and the page 15 replication statement may preserve broad structure rather than identical inferential details. An outcome/time-specific confidence distribution, a different omnibus reference distribution or df, separate covariance estimators, separate fitted analyses or another estimand/time-specific omnibus comparison could reconcile actual values. The table does not establish which of these applies. Missing definitions remain the human question rather than an inferred production mechanism.

**Direct observation versus inferred explanation:** Direct: the exact physical-function six- and twelve-month printed tuples, the two Ps and the stated model context. Reproduced mathematical observation: these tuples cannot yield those Ps within the independently supported normal-CI/common-covariance/chi-square with 2 degrees of freedom reconstruction after half-unit rounding. Inferred only: that the authors used that exact reconstruction, that any particular production mechanism caused the discrepancy, or that one printed number should replace another. None of those inferences is asserted.

The unresolved source question is which fitted analysis, contrast covariance, confidence critical value/reference distribution and omnibus reference distribution/degrees of freedom produced these two P values and contrast intervals, whether the columns share an outcome/time/covariance/estimand, and which reported values should be extracted if their inferential constructions differ.

**Mechanical evidence recheck:** A fresh high-effort appended-candidate recheck visually confirmed both target rows, all 19 method-support rows and five distinct supplied-source context pages. Separate JavaScript arithmetic reproduced every witness and the 24/32 conservative vertex bounds, including positive minimum determinants .01195380636846352/.02217991416023505. Exact-source transcriptions required no correction; evidence state is reproduced. These mathematical findings do not identify the authors’ actual implementation. See the [complete C018 recheck](review_1_6_2/verification/evidence_recheck.md), [independent calculation record](review_1_6_2/preprocessing/pass2_screen/independent_calculation.md) and [quality audit](review_1_6_2/quality/evidence_quality_audit.md).

**Potential downstream evidence impact:** If confirmed, this candidate could affect extraction of the unadjusted physical-function omnibus P values or identification of the analysis corresponding to their intervals. Both printed omnibus Ps and at least one contrast interval per row indicate a result below .05. No pairwise P conflict, .05-level conclusion reversal or actual downstream propagation is established.

## Downstream Evidence-Chain Considerations

A systematic review or meta-analysis could copy an adherence percentage, denominator, SMD, NNT, coefficient interval/P pair or raw summary directly from these displays. A guideline or other evidence user could also retain the reported model, missing-data hierarchy or intervention-duration specification. If human adjudication confirms a candidate, the corresponding extraction may need clarification of the value, summary type or analysis identity before reuse. This report does not establish propagation, a changed pooled estimate, a changed clinical conclusion or serious harm.

Source-linked cards distinguish direct printed observations from inferred explanations. Potentially different interval constructions, fitted analyses, target populations and prospective amendments remain explicit alternatives. Related cards applying different rules retain separate IDs, while repeated instances of one rule remain consolidated with all locations.

## Limitations and Missing Definitions

All 147 source units are scientifically mapped and exact candidate source locations are readable. Complete coverage does not supply unreported fitted inputs or determine an intended replacement value. Participant-level data, fitted model code, outcome-specific usual-care change SDs, unrounded tuples, covariance matrices and detailed simulation implementation are not supplied. Those absences alone are not candidates.


All 147 supplied source units have complete scientific mapping: 60 were initially reusable-backed and 87 required fresh direct-source recovery. There is no scientific source-coverage gap. Earlier 1.6.2 generated content was deleted and excluded at the user’s direction; 178 eligible original earlier-workflow assets remained immutable.

Protocol and SAP native/layout text is glyph encoded. Fresh page rendering and page-by-page visual inspection closed those extraction gaps; targeted pinned RapidOCR 1.3.24 on CPU supplied transcription aids. Unfinished OCR outputs were not used as evidence. Earlier reusable-engine versions are not consistently retained; unchanged source hashes and exact source pages/cells establish identity and evidence authority. Histogram bins lack exact numeric labels, so approximate heights were not treated as exact participant counts.

The user-requested GPU was accessible outside the restricted sandbox, but the existing approved RapidOCR 1.4.4/onnxruntime-gpu 1.28.0 environment lacked libcublasLt.so.13. CUDA OCR did not run. Fresh scientific processing used CPU; the GPU compatibility log was excluded from scientific input.

| Candidate | Exact unresolved definitions or fitted inputs |
|---|---|
| C001 | Whether session ranges mean planned content, expected self-paced completion or observed duration; any duration-specific amendment. |
| C002 | Any alternative denominator or adherence category underlying 43%. |
| C003 | Actual outcome/time UC-change SDs, unrounded fitted contrasts, and any distinct standardizers or contrast/model assignments. |
| C004 | Unrounded adjusted risk differences, upward-integer reporting convention and any alternative NNT point construction. |
| C005 | Prospective specification and timing making age a fixed primary covariate; exact main fitted covariate vector. |
| C006 | Planned and implemented per-outcome adjustment vectors, inheritance of primary factors and baseline-value interpretation for PGIC. |
| C007 | Final approved primary/sensitivity hierarchy reconciling retained follow-up/MAR wording with the disclosed pattern-mixture/IPW amendment and conditional first approach. |
| C008 | Pre-inversion RD intervals, parameter-specific confidence methods, joint response covariance and any distinct RR/NNT fitted analyses. |
| C009 | Unrounded NNT interval construction and intended point/interval contrast-time mapping. |
| C010 | Unrounded SMD tuples, SMD interval method and intended outcome/time/contrast mapping. |
| C011 | Exact covariate vector per restricted subset and whether education/employment were dropped, reselected or only omitted from the footnote. |
| C012 | Whether education, employment or both entered the final predictor vector generating nonresponse weights. |
| C013 | Education design matrices, category-to-coefficient correspondence and any distinction between selection coding and final-fit coding. |
| C014 | Unrounded null-adjacent endpoints; coefficient-test family, variance estimators, CI/test reference distributions, degrees of freedom and analysis assignments. |
| C015 | Whether the first subgroup arm counts are randomized target-population sizes, weighted representation or observed three-month contributors. |
| C016 | Raw central statistic and bound method per cell; empirical/interpolated/weighted/set-valued median conventions; intentional mixed summary types. |
| C017 | Any restricted PHQ-8 assessment denominator or alternate numerator supporting workbook E82 73.2%. |
| C018 | Actual confidence critical value/reference distribution, contrast covariance, omnibus distribution/degrees of freedom, common estimand/analysis mapping, unrounded tuples and outcome/time sample sizes or missingness denominators. |

The package also lacks participant-level data, fitted analysis code and the detailed simulation implementation. Diagnostic calculations remain explicitly conditional on their stated mathematical family and do not establish the authors’ actual covariance or provide replacement statistics. Every source-grounded alternative remains in the corresponding card. These limitations concern reproducibility and extractable quantity identity; every candidate remains Pending Human Adjudication.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_2/routing_preflight.md) records PASS, run model gpt-6.1-sol from DEFAULT, CURRENT_SESSION provider, INTERACTIVE_CLI execution and verification of all ten named role presets. The coordinator uses high reasoning effort, ordinary specialists medium, and statistical, screening, recheck and audit specialists high. Runtime identifiers are preserved literally in the [runtime identity record](review_1_6_2/execution/runtime_identifiers.json); the manifest below omits only the leading root separator for validator syntax. Distinct runtime IDs document fresh mandatory stages and all actual aborted, shard, repair and audit executions.

Direct local tools were preferred where available. Recorded pinned PyMuPDF 1.26.4 CPU renders and targeted RapidOCR 1.3.24 CPU outputs support fresh recovery; exact workbook XML/shared strings support cell evidence. Tool versions, device history and fallback lifecycle are recorded in the [tooling record](review_1_6_2/tooling_record.md). 

### Source Integrity

The metadata handoff records unchanged hashes for all six direct sources and all 178 reused assets. Canonical before/after SHA-256 manifests provide the full reproducible comparison. Source hashes at inventory were:

| Exact supplied source | SHA-256 |
|---|---|
| `jama_debar_2025_oi_250046_1755300121.13587.pdf` | `9f2cbc621ab2226b4e288f98c21ab084ca115eef5d301f1999f78f14bc53ca9d` |
| `joi250046supp1_prod_1755300121.14087.pdf` | `b94033e19e7781f6ea0a7100e9ccb9b32d6226c23fd268b13f81183361880af0` |
| `joi250046supp2_prod_1755300121.15087.pdf` | `2ca40f50cdcc33ad6dfb9d6e9fb2241dfc59737c62c96803acfb70830d7b4ab3` |
| `joi250046supp3_prod_1755300121.15087.pdf` | `148b4cebf4693e1fb2b5022ca5ff394aa440454049564b5407c693dbb10f8ff7` |
| `joi250046supp4_prod_1755300121.15587.pdf` | `66a709f597668cb84d895f6f998fbd8a14331e84fac36fee2e5b7b423864c3ca` |
| `joi250046supp5_prod_1755300121.16087.xlsx` | `5ff42dc1be5bf16b3fc27ab339d526e73c00b7f3940f9679a0ab4366dfa53893` |

See [source hashes before](review_1_6_2/source_hashes_before.sha256), [source hashes after](review_1_6_2/source_hashes_after.sha256), [reused hashes before](review_1_6_2/reused_artifact_hashes_before.sha256) and [reused hashes after](review_1_6_2/reused_artifact_hashes_after.sha256). No supplied source or reused asset was modified by report generation.

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION-20261014 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| aborted_reuse_asset_curator | root/curator_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/curator_20261014_aborted.md |
| aborted_main_mapping | root/main_mapper_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/main_mapper_20261014_aborted.md |
| aborted_support_mapping | root/support_mapper_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/support_mapper_20261014_aborted.md |
| aborted_protocol_a_mapping | root/protocol_a_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/protocol_a_20261014_aborted.md |
| aborted_protocol_b_mapping | root/protocol_b_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/protocol_b_20261014_aborted.md |
| aborted_protocol_c_mapping | root/protocol_c_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/protocol_c_20261014_aborted.md |
| aborted_sap_mapping | root/sap_mapper_20261014 | gpt-6.1-sol | medium | FRESH_SPAWN | execution/sap_mapper_20261014_aborted.md |
| reuse_asset_curator | root/curator_restart | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_mapper_protocol_a | root/protocol_a_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_001_032_restart.md |
| support_mapper_protocol_b | root/protocol_b_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_033_064_restart.md |
| support_mapper_protocol_c | root/protocol_c_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/protocol_065_077_restart.md |
| support_mapper_sap | root/sap_restart | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/sap_001_029_restart.md |
| numeric_consistency_reviewer | root/numeric_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_source_review | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/stat1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_reports | root/stat1_reports | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1_reports.md |
| statistics_pass_1_plans | root/stat1_plans | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1_plans.md |
| statistics_pass_1_raw | root/stat1_raw | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat1_raw.md |
| inclusion_screener | root/initial_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/stat2_main_early | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_main_late | root/stat2_main_late | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_main_late.md |
| statistics_pass_2_reports_early | root/stat2_reports_early | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_reports_early.md |
| statistics_pass_2_reports_late | root/stat2_reports_late | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_reports_late.md |
| statistics_pass_2_plans | root/stat2_plans | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plans.md |
| statistics_pass_2_raw | root/stat2_raw | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_raw.md |
| inclusion_screener_pass_2 | root/pass2_screen | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_appended | root/recheck_c018 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/append_C018.md |
| statistics_pass_2_plan_a_repair | root/stat2_plan_a_repair | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plan_a_repair.md |
| statistics_pass_2_plan_b_repair | root/stat2_plan_b_repair | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plan_b_repair.md |
| statistics_pass_2_plan_c_repair | root/stat2_plan_c_repair | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/stat2_plan_c_repair.md |
| quality_audit_main_early | root/qa_main_early | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_main_early.md |
| quality_audit_main_late | root/qa_main_late | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_main_late.md |
| quality_audit_workbook_numeric | root/qa_workbook_numeric | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_workbook_numeric.md |
| quality_audit_reports_early | root/qa_reports_early | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_reports_early.md |
| quality_audit_reports_late | root/qa_reports_late | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_reports_late.md |
| quality_audit_protocol | root/qa_protocol | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_protocol.md |
| quality_audit_sap | root/qa_sap | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_sap.md |
| quality_control_auditor | root/final_candidate_audit | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_complete | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility Performance

- **Target basis:** Six direct sources contain 146 PDF pages and one results worksheet. Original assets support 60 unique units; 87 require fresh direct-source recovery, including 57 protocol pages and 29 SAP pages with unreadable glyph-encoded text and one results-supplement page with absent content extraction. Fourteen additional image-backed protocol pages lack readable OCR. Recovery uses CPU fallback PDF rendering/RapidOCR, one structured worksheet requires cell-level reading, and mandatory mapping, parallel checkers, screening, recheck, second statistics pass, quality audit and reporting require successive agent waves. User-directed deletion and restart of prior 1.6.2 derivatives increases preprocessing work; earlier superseded work remains inside the supplied start time.
- **Total source units:** 147
- **Fresh-source units:** 87
- **Target elapsed minutes:** 40-70
- **Started UTC:** 2026-10-14T16:23:10Z
- **Finished UTC:** 2026-10-14T18:34:05Z
- **Observed elapsed minutes:** 130.917
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** User-directed deletion and restart of earlier 1.6.2 derivatives; fresh 87-unit recovery of glyph-encoded/absent extraction with CPU rendering and targeted OCR; complete 263-relationship independent two-pass review and 18-candidate screening/recheck; repair of a 43-page statistical shard through three fresh bounded replacements; seven bounded full-evidence audit shards plus independent candidate audit and complete reporting
