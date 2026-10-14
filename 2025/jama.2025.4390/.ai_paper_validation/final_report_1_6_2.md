# BedMed: Quantitative Reporting Quality-Control Consistency Review

**Pending Human Adjudication**

Workflow 1.6.2. All 13 candidate reporting issues remain Pending Human Adjudication. Evidence reproduction and an inclusion audit establish eligibility for this review; they do not establish a human disposition or a final source correction.

## Executive Quality-Control Summary

Complete review of four supplied PDFs, covering all 86 physical pages, identified 13 distinct candidates: five concerning reported rates, counts, fractions or same-display statistical tests, and eight concerning supplied prospective specifications versus reported endpoints, analyses or statistical decision inputs. Twenty checker findings received independent inclusion decisions: 13 were included and seven screened out, including four duplicate findings retained as provenance. A distinct second statistical pass and independent quality audit found no additional unregistered qualifying issue.

All 78 numeric relationships and all 110 statistical relationships were covered. Both fresh statistical reviewers completed every statistical relationship, including every constituent entry within grouped displays. Exact-source recheck reproduced 12 candidates and reproduced C008 after three reviewer-transcription changes to interval limits. The inclusion auditor recorded CONFIRMED for all 13 candidates and QUESTIONED for none. These are workflow evidence and threshold states, with human adjudication pending.

The primary adjusted treatment result, HR 0.96 (95% CI 0.77–1.19), P=.70, was consistent across matched locations. C001 concerns the quantity or scale of its Figure 3 rate columns. No interval-versus-P-value conflict was reproduced. The report makes no claim that any candidate changed a trial conclusion, propagated into another publication, or caused downstream harm.

## Package and Reused-Evidence Provenance

The source package is `jama.2025.4390`, reporting the BedMed randomized trial. Document roles were assigned from content. All evidence is supplied locally; referenced publications not present in the package were not consulted.

| Source ID | Supplied filename and opening page | Role | Physical pages |
|---|---|---|---:|
| DOC-001 | [jama_garrison_2025_oi_250019_1749674951.29054.pdf](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1) | REPORT: main article | 12 |
| DOC-002 | [joi250019supp1_prod_1749674951.29554.pdf](../joi250019supp1_prod_1749674951.29554.pdf#page=1) | PLAN: original protocol and amendment log | 18 |
| DOC-003 | [joi250019supp2_prod_1749674951.30054.pdf](../joi250019supp2_prod_1749674951.30054.pdf#page=1) | PLAN: SAP and attestation | 7 |
| DOC-004 | [joi250019supp3_prod_1749674951.30054.pdf](../joi250019supp3_prod_1749674951.30054.pdf#page=1) | REPORT: supplemental methods, figures and tables | 49 |

The curator inventoried and hashed 233 retained extraction/provenance assets: 173 STALE, 28 USABLE, six DUPLICATE, 18 UNREADABLE and eight PARTIAL. These are asset counts, not page counts. Current main/results source hashes differ from historical recorded identities, and later historical derivatives lack independent matching-hash proof; all 61 main/results pages therefore received fresh extraction and mapping. Protocol/SAP source identity matched, supporting reuse for 25 pages. Fresh agents reconstructed discovery and classification; old candidates, screening decisions and reports did not supply scientific inputs.

Source-matched protocol layout text and SAP page images were reused unchanged. SAP native/layout text is encoded and unusable; all seven page images were visually inspected. Readable OCR on SAP pages 1–3 served as a locator, while empty OCR on pages 4–5 and absent readable OCR on pages 6–7 did not limit source coverage. Historical extraction/rendering engine versions are unrecorded. Current extraction and 200-dpi CPU rendering used the bundled helper with pinned PyMuPDF 1.26.4; pypdf 5.9.0 was also installed in the temporary package-local fallback.

Detailed provenance is in [source_inventory.md](review_1_6_2/source_inventory.md), [evidence_asset_inventory.md](review_1_6_2/evidence_asset_inventory.md), [source hashes before review](review_1_6_2/source_hashes_before.sha256) and [retained asset hashes before review](review_1_6_2/reused_artifact_hashes_before.sha256). Exact supplied PDF pages, rather than OCR or inherited commentary, remain the authority for candidate evidence.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design under the supplied scope. It does not conduct a general clinical, methodological, novelty, misconduct or raw-data audit, and does not recommend a preferred analysis.

| Source | Total pages | Reusable-backed | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 0 | 12 | 12 | COMPLETE |
| DOC-002 | 18 | 18 | 0 | 18 | COMPLETE |
| DOC-003 | 7 | 7 | 0 | 7 | COMPLETE |
| DOC-004 | 49 | 0 | 49 | 49 | COMPLETE |
| Total | 86 | 25 | 61 | 86 | COMPLETE |

Every physical page was mapped, including covers, references, signatures and administrative content; pages without applicable scientific relationships have explicit records. Four disjoint mapping scopes covered the main article, both plans, results pages 1–24 and results pages 25–49. The complete support map is a lossless merge of all three support scopes. No source was sampled, and there is no scientific coverage gap. See [source_coverage.md](review_1_6_2/source_coverage.md) and [coverage_manifest.md](review_1_6_2/coverage_manifest.md).

Display precision uses each printed continuous value's half-unit interval. Integer participant/event counts retain their discrete values within those intervals. A remaining relative interval gap at most .05 is screened out. Interval-versus-test conflicts follow the always-register rule rather than that rounding allowance. Model-based effects are not equated with crude ratios. Within-subgroup effects and treatment-interaction tests are different parameters. Peripheral baseline copies, administrative details, immediately resolved wording and absent details without a conflicting source statement do not become cards.

## Quantitative and Statistical Relationship Coverage

| Evidence family | Numeric relationships | Statistical relationships | Coverage |
|---|---:|---:|---|
| Main article | 17 | 50 | All 12 pages, every displayed Table 1/Table 2/Figure 3 row and matched narrative |
| Protocol and SAP | 17 | 29 | All 25 pages, outcome lists, ordered covariates, subgroup/sensitivity lists and amendments |
| Results supplement pages 1–24 | 19 | 12 | Ascertainment, adjudication, models, changes and all graphic values |
| Results supplement pages 25–49 | 25 | 19 | All figure/table entries, including grouped retention tests and 11 ABPM entries |
| Total | 78 | 110 | Complete |

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) records NUMERIC_COMPLETE for all 78 IDs. The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) records PASS_1_COMPLETE and PASS_2_COMPLETE for every one of the 110 actual, noncontiguous S IDs. The two fresh high-effort statistical runtimes are distinct and separately recorded below. Each pass covers every constituent of grouped relationships, rather than one representative row.

Checks included participant-flow closure, fraction/percentage reconciliation, matched result identity, interval order and containment, null-versus-test compatibility, effect direction and units, power/stopping inputs, ordered model/covariate lists, analysis populations, censoring, planned endpoints and sensitivity/subgroup specifications. Pass 2 revisited all 13 stable candidates and 20 initial screening decisions, and independently reconsidered all 36 earlier checker exclusions. It also itemized all 88 eTable 4/5 inferential entries, six count-based ABPM diagnostics and five continuous ABPM entries. Exact fitted covariance, some test engines and individual-level inputs are absent and are named as limits; diagnostic calculations do not replace the reported analysis.

## Inclusion Screening Summary

A reproduced finding qualifies through an always-register category (Route A) or through all three Route B criteria: in focus, not immediately resolved by context, and bearing on a specific interpretation or extracted value. No expected candidate count was applied. Every formal finding has exactly one independent screening decision in [inclusion_screen.md](review_1_6_2/screening/inclusion_screen.md).

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 13 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 4 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 1 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| Total | All decisions | 20 |

All other screened-out reason codes have zero formal-finding decisions. Numeric, cross-source and first statistical checkers emitted three, nine and eight findings respectively. Pass 2 emitted zero additional findings; no conditional second inclusion-screen stage was needed. The quality auditor changed no formal screening decision and raised no additional finding.

The 36 self-screened checker observations are separate from those 20 formal findings. Both pass 2 and the auditor reread all 36: 35 retain their exclusion rationale, and the cross-source withdrawal-sensitivity observation has effective DUPLICATE_OF_INCLUDED status because its Route A category 5 issue is already C009. The original checker row is preserved. This overlap does not increase the number of findings or candidates. Audit refinements to low-discrepancy arithmetic did not change a screening decision.

## Review-Domain Summary

| Review domain | Definition | Candidates |
|---|---|---:|
| statistical_results | Counts, estimates, tests or statistical-method relationships in REPORT materials | 5 |
| report_internal_inconsistency | REPORT materials conflict about the outcome, time, population or comparison to which a number belongs | 0 |
| protocol_report | A REPORT differs from supplied PLAN statistical design or analysis content | 8 |
| plan_material | A statistical-design inconsistency solely within PLAN material | 0 |
| Total | One primary domain per candidate | 13 |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | PLAN versus REPORT | 8 |
| P_P | PLAN versus PLAN | 0 |
| S_C | Different REPORT documents | 0 |
| S_W | Within one REPORT document | 5 |
| Total | Primary types | 13 |

C006 and C007 also contain P_P relationships; P_R takes precedence. Their plan versions are not assumed simultaneously operative. Corroboration alone does not add a conflicting relationship.

| Evidence state | Candidates |
|---|---:|
| reproduced | 12 |
| reproduced_after_transcription_correction | 1 |
| not_reproduced | 0 |
| Total | 13 |

Inclusion audit: CONFIRMED 13; QUESTIONED 0. All 13 remain Pending Human Adjudication. See the [canonical ledger](review_1_6_2/candidate_ledger.md), [mechanical recheck](review_1_6_2/verification/evidence_recheck.md) and [independent quality audit](review_1_6_2/quality/evidence_quality_audit.md).

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Figure 3 rate quantity/scale | statistical_results | S_W | reproduced | CONFIRMED |
| C002 | Acute/unplanned utilization event restriction | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Adaptive diuretic decision time/population | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | Allocation specification | protocol_report | P_R | reproduced | CONFIRMED |
| C005 | LTC medication-timing-control restriction | protocol_report | P_R | reproduced | CONFIRMED |
| C006 | Versioned health/glaucoma outcome hierarchy | protocol_report | P_R | reproduced | CONFIRMED |
| C007 | Vision recall reference and aggregation | protocol_report | P_R | reproduced | CONFIRMED |
| C008 | Six medication subgroup prespecification axes | protocol_report | P_R | reproduced_after_transcription_correction | CONFIRMED |
| C009 | Planned within-arm withdrawal sensitivity contrast | protocol_report | P_R | reproduced | CONFIRMED |
| C010 | eTable 4 chronotype test reproduction | statistical_results | S_W | reproduced | CONFIRMED |
| C011 | eTable 5 ethnicity totals | statistical_results | S_W | reproduced | CONFIRMED |
| C012 | Identical medication comparisons, differing tests | statistical_results | S_W | reproduced | CONFIRMED |
| C013 | ARB bedtime Other Reason fraction | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

Every card below is Pending Human Adjudication. Classification values are copied exactly from the ledger's final classification table. Source readings and reproduced arithmetic incorporate the completed recheck and independent audit. Where another checker emitted the same issue, that provenance is retained without creating a second card.

## C001 — Figure 3 primary and subgroup rate quantity/scale

Pending Human Adjudication.

Consolidated checker provenance: F-XS-001 and F-ST1-008 repeats this included pattern; every affected location is retained.

**Candidate statement:** The Figure 3 columns labeled rate per 100 patient-years print 71.0 in both arms for the primary result, while matched Table 2 rates are 2.30 and 2.44; the same quantity/scale ambiguity extends to all 38 subgroup rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Figure 3 vs REPORT main article abstract, Key Points, narrative and Table 2

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route B

**Classification rationale:** All compared content is REPORT within the main article. The substantive issue concerns the quantity and scale of rates, so statistical_results and S_W apply; plan material is not a conflicting comparator.

**Classification ambiguity:** None

**Exact source locations:**

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 9](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 1](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 2](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 6](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6)

**Source evidence:** [Main p.9 Figure 3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) explicitly labels both columns Rate per 100 patient-years and prints all-patient 71.0/71.0 with 163/173 events and HR .96 (.77–1.19). [Main p.8 Table 2](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8) prints the same primary 163/173 events and HR with rates 2.30/2.44. [Abstract p.1](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1), [Key Points p.2](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2) and [primary narrative p.6](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6) each print 2.3/2.4 per 100 patient-years. Outcome, arms, primary events and model identity match. The Figure 3 caption explains treatment-interaction models and unadjusted intervals, with no alternate definition of these columns.

Every Figure 3 affected row was read separately; bedtime/morning order is retained:

| Source p.9 row | Exact affected location | Bedtime events; labeled rate | Morning events; labeled rate | Source match |
|---|---|---|---|---|
| All patients | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 163; 71.0 | 173; 71.0 | Yes |
| Male | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 80; 30.5 | 94; 30.4 | Yes |
| Female | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 83; 40.5 | 79; 40.6 | Yes |
| Age ≥75 yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 77; 14.9 | 81; 14.5 | Yes |
| Age ≥75 no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 86; 56.1 | 92; 56.5 | Yes |
| Physically frail yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 47; 12.4 | 50; 12.7 | Yes |
| Physically frail no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 116; 58.6 | 123; 58.3 | Yes |
| Polypharmacy yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 80; 23.0 | 91; 22.4 | Yes |
| Polypharmacy no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 83; 48.0 | 82; 48.6 | Yes |
| Overall health ≤75 yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 91; 28.5 | 77; 25.1 | Yes |
| Overall health ≤75 no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 72; 42.5 | 96; 45.9 | Yes |
| Resistant hypertension yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 33; 7.7 | 46; 7.0 | Yes |
| Resistant hypertension no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 130; 63.3 | 127; 64.0 | Yes |
| Heart failure yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 6; 1.1 | 15; 1.1 | Yes |
| Heart failure no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 157; 69.8 | 158; 69.9 | Yes |
| Diabetes yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 37; 12.5 | 50; 12.5 | Yes |
| Diabetes no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 126; 58.5 | 123; 58.5 | Yes |
| Coronary artery disease yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 38; 7.0 | 46; 7.3 | Yes |
| Coronary artery disease no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 125; 63.9 | 127; 63.7 | Yes |
| Stroke/TIA yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 16; 4.6 | 25; 4.8 | Yes |
| Stroke/TIA no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 147; 66.4 | 148; 66.2 | Yes |
| Sleep apnea yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 37; 16.0 | 38; 14.4 | Yes |
| Sleep apnea no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 126; 55.0 | 135; 56.6 | Yes |
| Chronic kidney disease yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 19; 4.8 | 25; 4.8 | Yes |
| Chronic kidney disease no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 144; 66.2 | 148; 66.2 | Yes |
| Sedentary yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 50; 17.7 | 60; 18.3 | Yes |
| Sedentary no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 113; 53.2 | 113; 52.7 | Yes |
| ACE inhibitor yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 54; 24.4 | 78; 25.8 | Yes |
| ACE inhibitor no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 109; 46.6 | 95; 45.2 | Yes |
| ARB yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 56; 22.8 | 39; 19.7 | Yes |
| ARB no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 107; 48.2 | 134; 51.3 | Yes |
| Beta-blocker yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 59; 11.6 | 55; 10.9 | Yes |
| Beta-blocker no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 104; 59.4 | 118; 60.1 | Yes |
| Calcium channel blocker yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 64; 19.2 | 75; 19.8 | Yes |
| Calcium channel blocker no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 99; 51.7 | 98; 51.2 | Yes |
| Diuretic yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 50; 18.6 | 63; 19.6 | Yes |
| Diuretic no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 113; 52.4 | 110; 51.4 | Yes |
| Combination medication yes | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 20; 14.1 | 23; 13.4 | Yes |
| Combination medication no | [Figure 3, this row](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 143; 56.9 | 150; 57.6 | Yes |


**Reported-versus-comparator:** Figure 3: 71.0/71.0; Table 2: 2.30/2.44; abstract, Key Points and narrative: 2.3/2.4 per 100 patient-years, for the same 163/173 events.

**Reasoning procedure:** Match outcome, arms, event counts and HR, then compare the printed rate intervals. Retain every row under the shared columns as one repeated pattern. Use the additive subgroup pattern and scaled person-time only as supporting diagnostics.

**Calculation:** Matched primary rates with identical labels must reconcile. Figure interval [70.95,71.05] versus Table 2 bedtime [2.295,2.305] gives gap 68.645/71=.96683099; morning [2.435,2.445] gives 68.505/71=.96485915. Both exceed .05. Abstract/Key Points/body intervals [2.25,2.35]/[2.35,2.45] overlap Table 2, while remaining disjoint from 71.0. All 19 complementary subgroup event pairs sum exactly 163/173; their labeled-rate pairs sum 70.9 or 71.0. Their summed half-unit intervals [70.8,71.0] or [70.9,71.1] intersect the displayed all-patient [70.95,71.05]. This additive pattern supports common-column quantity ambiguity; no rule requiring true subgroup incidence rates to add is assumed. No independent benchmark rate is supplied for the 38 subgroup rows.


**Affected result or extracted value:** The primary and all 38 subgroup values labeled incidence rates in Figure 3; the primary HR is not challenged by this comparison.

**Why context does not resolve it:** The explicit rate headings and caption do not identify another quantity or scaling. Primary matching reproduces an over-tolerance discrepancy, and intended subgroup rates require an unstated definition/person-time.

**Alternative source-grounded interpretations:** Direct observation is the same-unit primary discrepancy and the 39-row common pattern. If 71.0 represented hundreds of patient-years, 163/71.0=2.29577465 and 173/71.0=2.43661972. Its rounding envelopes [163/71.05,163/70.95] and [173/71.05,173/70.95] overlap Table 2. Scaled person-time is an inferred possible explanation, not a supplied definition or replacement. HR/model-versus-crude comparisons are not this issue.


Unresolved source definition: What quantity and scale do both Figure 3 columns encode, and what primary and subgroup incidence rates should be extracted?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Labels, matched rates and event counts are available. Actual total and subgroup person-time and the definition/scale of the Figure columns are absent. They are unnecessary for the primary printed-copy discrepancy but necessary to reconstruct intended subgroup rates.


**Potential downstream evidence impact:** If confirmed, a data extractor could copy 71.0 or the subgroup column values as incidence rates under their printed units. Clarification could alter extracted rate/quantity fields; no actual downstream use or changed treatment estimate is established.

## C002 — Utilization endpoint restriction

Pending Human Adjudication.

**Candidate statement:** The reported utilization endpoint requires acute/unplanned presentations, whereas the supplied protocol/SAP specifies all-cause hospitalization or ED use without that event restriction.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol and SAP utilization endpoint vs REPORT main article and results supplement utilization definition

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route B

**Classification rationale:** Protocol and SAP are PLAN; the main article and results supplement are REPORT. Their reports corroborate the same restricted endpoint, so the conflicting relationship is P_R rather than S_C.

**Classification ambiguity:** An unavailable prospective operational definition or amendment may establish that all-cause was always restricted to acute/unplanned events.

**Exact source locations:**

PLAN [joi250019supp1_prod_1749674951.29554.pdf — physical PDF p. 3](../joi250019supp1_prod_1749674951.29554.pdf#page=3)

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 2](../joi250019supp2_prod_1749674951.30054.pdf#page=2)

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 4](../joi250019supp2_prod_1749674951.30054.pdf#page=4)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 1](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 15](../joi250019supp3_prod_1749674951.30054.pdf#page=15)

**Source evidence:** PLAN [protocol p.3](../joi250019supp1_prod_1749674951.29554.pdf#page=3) secondary item 2 is all-cause hospital admission. PLAN [SAP p.2](../joi250019supp2_prod_1749674951.30054.pdf#page=2) secondary item 2 and [SAP p.4 Table 1](../joi250019supp2_prod_1749674951.30054.pdf#page=4) both say all-cause hospitalization/ED visit, without an unplanned qualifier. REPORT [main abstract p.1](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=1), [main outcome definition p.3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3) and [Table 2 p.8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8) identify unplanned hospitalization/ED, with 993/1047 events, HR .93 (.85–1.02), P=.10. REPORT [results supplement p.15](../joi250019supp3_prod_1749674951.30054.pdf#page=15) requires likely symptom-driven acute presentation and excludes unclear unplanned status, elective surgery/ED procedures, overnight stays after planned day surgery without a new presentation, specified nonacute cancer admissions, departures before being seen, medication refill, palliative-care initiation and nonhospital urgent-care attendance.


**Reported-versus-comparator:** Unqualified planned all-cause utilization versus restricted reported utilization: 993 bedtime/1047 morning events, HR .93 (.85–1.02), P=.10.

**Reasoning procedure:** Compare literal event-membership criteria, not endpoint names alone. Distinguish the coherent original-to-final addition of ED visits from the acute/unplanned restriction. Match the affected result before considering definitions.

**Calculation:** The comparator is endpoint event membership, not a synonymous label. An unqualified utilization endpoint and the explicitly acute/unplanned restricted result do not state the same event set. The final SAP already includes ED visits; that coherent version extension is not another discrepancy. Rounding intervals cannot change inclusion criteria, so numerical display precision is not applicable; the supporting HR/CI/P themselves reconcile.


**Affected result or extracted value:** The endpoint definition attached to the abstract-listed utilization result, 993/1047 events and HR .93.

**Why context does not resolve it:** The report explicitly defines its acute/unplanned event set but does not establish that this is the same prospective set as the unqualified SAP definition. Ordinary all-cause wording does not determine whether elective/nonacute presentations were intended.

**Alternative source-grounded interpretations:** Direct observation is the absence/presence of the event restriction in cited statements. All-cause may have intended all causes within acute admissions, or operational criteria may have been prospectively accepted. That intended equivalence is not supplied; timing of acceptance is an inferred question.


Unresolved source definition: Which prospective utilization event definition governs the 993/1047-event result, and where were the acute/unplanned-only exclusions specified?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Printed endpoint statements and exclusions are available. A prospective document establishing that all-cause was intended to mean acute/unplanned only, and counts of excluded planned events by arm, are absent. No numerical change in HR is inferred.


**Potential downstream evidence impact:** If confirmed, an extractor could classify the same HR under all-cause utilization or under acute/unplanned utilization. This could affect endpoint grouping without establishing a changed count, HR or synthesis conclusion.

## C003 — Adaptive diuretic decision time/population

Pending Human Adjudication.

**Candidate statement:** The adaptive decision to continue diuretic-only enrollment is described using a six-month monotherapy assessment instead of the supplied six-week comparison among all bedtime BP-medicine users.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol adaptive diuretic enrollment rule vs REPORT main article decision assessment

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** The prospective protocol decision rule is PLAN and the reported assessment is REPORT. Its time/population inputs govern a planned enrollment decision, yielding P_R and protocol_report.

**Classification ambiguity:** Both assessments may have occurred or an unsupplied amendment may bridge them; only the supplied-versus-reported comparison is classified.

**Exact source locations:**

PLAN [joi250019supp1_prod_1749674951.29554.pdf — physical PDF p. 4](../joi250019supp1_prod_1749674951.29554.pdf#page=4)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 2](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2)

**Source evidence:** PLAN [protocol p.4 Diuretic tolerance](../joi250019supp1_prod_1749674951.29554.pdf#page=4) triggers after 200 participants whose only BP drug is a diuretic, including combination pills; it assesses six-week compliance for all BP medicines in all bedtime-allocated participants, comparing diuretics against other drugs and excluding further diuretic-only enrollment if substantially worse. REPORT [main p.2 Participants](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=2) describes a predefined six-month assessment of bedtime diuretic adherence in monotherapy participants, approximately three-fourths adherent, with no enrollment change needed.


**Reported-versus-comparator:** Plan: after 200 diuretic-only enrollees, compare six-week bedtime adherence of diuretic versus other drugs among all bedtime users. Report: six-month monotherapy adherence, approximately three-fourths, with no enrollment change.

**Reasoning procedure:** Compare the trigger, assessment time, comparison population and decision purpose item by item. Treat the reported three-fourths as approximate source context, and do not invent a substantially-worse threshold.

**Calculation:** Six weeks and six months are distinct specified decision times; all-bedtime-users' medicine comparison and monotherapy adherence are different specified decision inputs. This governs adaptive enrollment, not a peripheral follow-up count. No numeric cutoff was printed. Display precision does not reconcile time/population definitions; three-fourths is supporting report context, not an invented exact count.


**Affected result or extracted value:** The prospective basis and approximately 75% assessment used to support continuing diuretic-only recruitment.

**Why context does not resolve it:** Different times and populations feed the enrollment decision. Immediate context does not indicate whether the planned six-week comparative assessment or a prospective replacement supported the reported decision.

**Alternative source-grounded interpretations:** The stated input differences are directly observed. Both times may have been used, or the separately cited unsupplied publication/later protocol may contain an amendment. Absence from the package does not establish absence from all trial records.


Unresolved source definition: What prospective time, population and diuretic-versus-other comparison governed continuation of diuretic-only recruitment?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Both specified times, populations and decision purposes are available. Actual six-week comparator adherence, participant-level data, a numeric substantially-worse cutoff and a supplied amendment connecting the assessments are absent. Whether both assessments occurred cannot be established.


**Potential downstream evidence impact:** If confirmed, extraction of the adaptive decision rule and adherence assessment could use a different time, population or comparator. No recruitment-composition or primary-effect change is quantified.

## C004 — Allocation specification

Pending Human Adjudication.

Consolidated checker provenance: F-ST1-007 repeats this included pattern; every affected location is retained.

**Candidate statement:** The main article reports permuted blocks of sizes 10/12 stratified by province, while the supplied original protocol specifies simple allocation without blocking or stratification.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol allocation specification vs REPORT main article allocation and primary-model context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Classification rationale:** The allocation specification in the protocol is PLAN and the reported allocation is REPORT. Province adjustment in SAP/report corroborates the final model but does not create an additional P_P allocation conflict.

**Classification ambiguity:** The original protocol is earlier; an unavailable later protocol or operational amendment may establish the reported allocation.

**Exact source locations:**

PLAN [joi250019supp1_prod_1749674951.29554.pdf — physical PDF p. 4](../joi250019supp1_prod_1749674951.29554.pdf#page=4)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 7](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7)

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 4](../joi250019supp2_prod_1749674951.30054.pdf#page=4)

**Source evidence:** PLAN [protocol p.4 Allocation](../joi250019supp1_prod_1749674951.29554.pdf#page=4) states simple randomization with no stratification or blocking. REPORT [main p.3 Intervention](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3) states permuted blocks of random sizes 10 or 12 stratified by province, with individual 1:1 allocation. REPORT [main p.7 Figure 2 caption](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7) includes province in primary Cox covariates. PLAN [SAP p.4 Table 1](../joi250019supp2_prod_1749674951.30054.pdf#page=4) includes province as four model variables; this confirms adjustment, not allocation. The complete supplied protocol/amendment map and source-linked text disclose multiple changes but no explicit allocation replacement.


**Reported-versus-comparator:** No blocking/no stratification versus random blocks of 10 or 12 with province stratification; randomized arms 1677/1680 and primary adjusted HR .96 (.77–1.19).

**Reasoning procedure:** Compare allocation procedures directly and review supplied amendment coverage. Separate province adjustment from province-stratified sequence generation and do not infer actual allocation from nearly equal arm totals.

**Calculation:** No blocking/no stratification differs from specified blocking/province stratification. Integer block sizes and 1:1 do not supply a rounding reconciliation for categorical allocation procedures. Arm totals 1677/1680 are not a discrepancy or a test of whether either procedure occurred.


**Affected result or extracted value:** Randomization and stratification provenance accompanying the adjusted primary result.

**Why context does not resolve it:** The later report clearly identifies its procedure, but does not locate the prospective replacement of the supplied unblocked specification. A model province term does not establish an allocation amendment.

**Alternative source-grounded interpretations:** Printed specifications directly differ. A later operational/protocol amendment may explain them. Province adjustment alone cannot establish provincial stratification.


Unresolved source definition: Which prospective amendment established the reported blocked, province-stratified allocation and its relation to the original no-block/no-stratification specification?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Both procedures and province adjustment are available. Prospective replacement allocation amendment, sequence-generation record and unsupplied final published protocol are absent. No preference for either method or claim about actual randomization sequence is inferred.


**Potential downstream evidence impact:** If confirmed, a design extractor could record different blocking/stratification specifications or amendment provenance. No actual sequence reconstruction or changed primary HR is asserted.

## C005 — LTC medication-control criterion

Pending Human Adjudication.

**Candidate statement:** The reported LTC/nursing-home endpoint requires loss of personal medication-timing control, a restriction not explicit in the SAP inclusion of nursing home or assisted-living admission.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP LTC definition vs REPORT main article and results supplement nursing-home definition

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Qualifying route:** Route B

**Classification rationale:** SAP endpoint content is PLAN and both printed outcome definitions are REPORT. The reports agree with one another, so the substantive comparison is P_R, protocol_report.

**Classification ambiguity:** SAP assisted living may intend only higher-care medication administration; facility terminology alone does not establish that restriction.

**Exact source locations:**

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 2](../joi250019supp2_prod_1749674951.30054.pdf#page=2)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 16](../joi250019supp3_prod_1749674951.30054.pdf#page=16)

**Source evidence:** PLAN [SAP p.2 item 3](../joi250019supp2_prod_1749674951.30054.pdf#page=2) expands LTC admission as nursing home or assisted-living facility. REPORT [main p.3 secondary list](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3) says nursing home; REPORT [Table 2 p.8 nursing-home row and footnote g](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8) defines group living where participants no longer control their medication timing and prints 38/26, HR 1.38 (.83–2.27), P=.21. REPORT [results p.16 Nursing Home admission](../joi250019supp3_prod_1749674951.30054.pdf#page=16) explicitly counts a move from low-care assisted living with timing control to higher care with nurses/care aides administering medicines.


**Reported-versus-comparator:** SAP: nursing home or assisted-living facility. Report: group living without medication-timing control, 38/26 events, HR 1.38 (.83–2.27), P=.21.

**Reasoning procedure:** Compare inclusion criteria using the source-defined example of lower-care assisted living versus higher-care medication administration. Do not infer that a participant experienced a hypothetical admission or estimate changed event membership.

**Calculation:** SAP's assisted-living alternative does not explicitly require lost timing control; Table 2 does. A low-care assisted-living admission retaining personal control satisfies the literal plan alternative and may fail the report definition. This is a logical event-membership diagnostic, not an assertion that a participant experienced it. No precision interval changes a functional criterion; the HR/CI/P themselves reconcile.


**Affected result or extracted value:** The care-level/functional definition attached to the 38/26-event LTC analysis.

**Why context does not resolve it:** An assisted-living admission with retained medication-timing control can satisfy the literal SAP alternative but not the printed report criterion. Immediate context does not supply the prospective care-level bridge.

**Alternative source-grounded interpretations:** Direct observation is the additional printed control restriction. SAP may intend assisted living only at higher-care medication administration. Facility synonyms alone do not establish that equivalence.


Unresolved source definition: Did the prospective LTC endpoint cover all assisted-living admissions, or only admissions with loss of personal medication-timing control?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Definitions and effect are available. Prospective assisted-living care-level definition, classification of actual admissions and a bridging amendment are absent. No changed count is estimated.


**Potential downstream evidence impact:** If confirmed, an extractor could group the HR as all LTC/assisted-living admission or as admission involving lost medication-timing control. No numerical effect of that distinction is demonstrated.

## C006 — Versioned health/glaucoma outcome hierarchy

Pending Human Adjudication.

**Candidate statement:** Supplied plan versions and report materials show overall health moving from secondary to exploratory and glaucoma from safety to secondary hierarchy, with disclosed blinded outcome evolution.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN original protocol vs PLAN SAP; PLAN outcome hierarchy vs REPORT main article and results supplement hierarchy

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** Original protocol and later SAP are PLAN; main/results output is REPORT. Both P_P and P_R are substantive; P_R takes precedence, giving protocol_report.

**Classification ambiguity:** Versioned changes need not be simultaneously operative. Safety may overlap secondary hierarchy and tolerability may be a safety subset; the latter taxonomy is retained as ambiguity.

**Exact source locations:**

PLAN [joi250019supp1_prod_1749674951.29554.pdf — physical PDF p. 3](../joi250019supp1_prod_1749674951.29554.pdf#page=3)

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 2](../joi250019supp2_prod_1749674951.30054.pdf#page=2)

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 3](../joi250019supp2_prod_1749674951.30054.pdf#page=3)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 7](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 21](../joi250019supp3_prod_1749674951.30054.pdf#page=21)

**Source evidence:** every affected location. PLAN [original p.3](../joi250019supp1_prod_1749674951.29554.pdf#page=3) places EQ-5D functional measures/overall health in Secondary, new glaucoma in Safety, and nocturia count/burden and lightheadedness in Tolerability. PLAN [SAP p.2](../joi250019supp2_prod_1749674951.30054.pdf#page=2) makes new glaucoma secondary item 5, and puts lightheadedness/nocturia under Supplementary Safety; [SAP p.3](../joi250019supp2_prod_1749674951.30054.pdf#page=3) continues nocturia burden and explicitly places overall health at 12 months under Exploratory. REPORT [main p.3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3) lists glaucoma as secondary, other symptoms/nocturia as safety, and says it also examined 12-month overall health. REPORT [main p.7](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=7) reports health difference −.75 (−1.69,.19), P=.12. REPORT [Table 2 p.8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8) places glaucoma under secondary safety and prints HR 1.13 (.73–1.74), P=.58; lightheadedness RR .95 (.90–1.00), P=.06. REPORT [results p.21 Changes to secondary outcomes](../joi250019supp3_prod_1749674951.30054.pdf#page=21) discloses fully blinded outcome evolution and says health changed from baseline change to 12-month score; it also describes glaucoma, nocturia and other named measures as added secondary safety analyses.


**Reported-versus-comparator:** Original health secondary versus later SAP exploratory; original glaucoma safety versus later secondary/report secondary safety. Health difference −.75 (−1.69,.19), P=.12; glaucoma HR 1.13 (.73–1.74), P=.58.

**Reasoning procedure:** Compare named outcome statuses across versions and final report, preserving dates and explicit fully blinded evolution. Distinguish outcome collection from detailed analysis prespecification and overlapping safety/tolerability taxonomy.

**Calculation:** Yes for directly printed secondary→exploratory health and safety→secondary glaucoma status transitions, route A5. This does not imply simultaneous operative versions. No half-unit arithmetic applies to status labels. Health's changed estimand is expressly disclosed and matches final SAP. Tolerability→supplementary-safety wording for nocturia/lightheadedness is preserved as taxonomy ambiguity; it is not needed as an additional independently demonstrated hierarchy change. Syncope, falling, hip fracture and vision remain safety and are not extra transitions. Numeric HR/CI/P and health estimate/CI/P are matched, ordered and null-consistent; lightheadedness upper 1.00 with P=.06 does not create an interval/test conflict.


**Affected result or extracted value:** Hierarchy and prospective status of overall health, glaucoma, and the linked safety/tolerability analyses, including lightheadedness RR .95 (.90–1.00), P=.06 and separately reported nocturia.

**Why context does not resolve it:** Route A category 5 covers reproduced changes in prespecified outcome status. Disclosed blinded changes and plausible overlapping taxonomy are retained as alternatives rather than suppressing the health/glaucoma transitions.

**Alternative source-grounded interpretations:** Direct observations are the printed hierarchy assignments and fully blinded change disclosure. These may reflect intentional amendments, overlapping safety/secondary axes or tolerability as a safety subset. The report's statement that analyses were newly prespecified is not treated as proof that the original protocol failed to collect them. The main health prose itself does not expressly call its final analysis secondary; the differing plan statuses and the supplement's secondary-change description remain the evidence.


Unresolved source definition: What final hierarchy applied to overall health and new glaucoma, when/how was it prospectively changed, and how do safety, supplementary safety and tolerability categories relate?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: All named status lists, version dates, disclosure and supplied results are available. Exact prospective reclassification date/document, whether safety is orthogonal to secondary hierarchy, and the separately published nocturia output are absent. Detailed analysis prespecification is distinguished from collecting a named safety measure.


**Potential downstream evidence impact:** If confirmed, evidence extraction could assign different prospective hierarchy/status to these outcomes. No change in their printed effect estimates or overall trial conclusion is established.

## C007 — Vision recall reference and aggregation

Pending Human Adjudication.

**Candidate statement:** The original vision statement refers to worsening since study start, while the final SAP/report uses previous-follow-up comparisons and a repeated-slight-worsening aggregation rule.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN original protocol vs PLAN SAP vision definition; PLAN original vision definition vs REPORT main article vision definition

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Classification rationale:** Original protocol and final SAP are PLAN; main article is REPORT. Original-versus-final window differences create P_P and P_R; P_R has precedence. Final SAP/report agreement is corroboration rather than S_C.

**Classification ambiguity:** The earlier wording may summarize cumulative collection, or a later amendment may establish the interval question; actual questionnaire versions are unavailable.

**Exact source locations:**

PLAN [joi250019supp1_prod_1749674951.29554.pdf — physical PDF p. 3](../joi250019supp1_prod_1749674951.29554.pdf#page=3)

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 2](../joi250019supp2_prod_1749674951.30054.pdf#page=2)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 8](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8)

**Source evidence:** PLAN [original p.3 Safety](../joi250019supp1_prod_1749674951.29554.pdf#page=3) states worsening since study start, unchanged/slightly worse/much worse. PLAN [SAP p.2 Vision](../joi250019supp2_prod_1749674951.30054.pdf#page=2) uses last-follow-up reference and much worse once or slightly worse on two or more occasions; its note states that the three-category question compares with last follow-up. REPORT [main p.3](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=3) and [Table 2 p.8 footnote d](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=8) reproduce the latter definition. Table 2 prints 420 (25.0%)/411 (24.5%), RR 1.02 (.89–1.17), P=.74.


**Reported-versus-comparator:** Since study start versus since previous follow-up; final result 420/411, 25.0%/24.5%, RR 1.02 (.89–1.17), P=.74, with one much-worse or at least two slightly-worse reports.

**Reasoning procedure:** Compare temporal references and aggregation separately. A persistent small decline illustrates non-equivalence of reference windows without supplying hypothetical event counts. Check that the reported numerical result itself reconciles.

**Calculation:** Since study start and since last follow-up use different reference windows. A persistent small decline can remain worse relative to start but unchanged relative to the immediately preceding visit. This demonstrates definition non-equivalence without inventing events. Two slightly-worse reports versus the original three-category description is also an aggregation specification not printed originally. Numeric precision does not reconcile reference/aggregation definitions; 420/1677 and 411/1680 reconcile their percentages under half-unit intervals, and CI includes one with nonsignificant P.


**Affected result or extracted value:** The recalled reference and aggregation defining subjective vision worsening for the reported safety result.

**Why context does not resolve it:** Study-start and previous-visit references encode different observations. Final SAP/report agreement identifies the reported rule but does not establish the prospective bridge or actual administered question relative to the original window.

**Alternative source-grounded interpretations:** Direct observation is the different window language. Original wording may summarize cumulative safety collection; a later amendment may establish the administered interval question. No claim about actual administration follows from document wording alone.


Unresolved source definition: What vision reference and aggregation were prospectively specified and actually administered, and when was any change established?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Both window/aggregation statements and result are available. Actual questionnaire versions, date of reference-window amendment and participant response trajectories are absent. No estimate of changed membership is possible.


**Potential downstream evidence impact:** If confirmed, extraction could use a different vision reference window/aggregation when grouping safety outcomes. No number of reclassified responses or changed RR can be inferred.

## C008 — Six medication-class subgroup prespecification axes

Pending Human Adjudication.

Consolidated checker provenance: F-ST1-004 repeats this included pattern; every affected location is retained.

**Candidate statement:** Six primary-outcome medication-class subgroup axes fall under the Figure 3 prespecified caption but lack counterparts in the supplied 13-axis SAP subgroup list.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP subgroup list vs REPORT main article medication subgroup prespecification caption and narrative

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route A, category 5

**Classification rationale:** SAP/protocol specification is PLAN and the subgroup narrative/caption is REPORT. The list-to-caption comparison is P_R, protocol_report; medication collection or adherence studies do not create a prospective treatment-interaction counterpart.

**Classification ambiguity:** An unsupplied prospective subgroup specification or a caption intended only for the first 13 axes could explain the label.

**Exact source locations:**

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 6](../joi250019supp2_prod_1749674951.30054.pdf#page=6)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 6](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6)

REPORT [jama_garrison_2025_oi_250019_1749674951.29054.pdf — physical PDF p. 9](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9)

**Source evidence:** PLAN [SAP p.6 Subgroup Analyses](../joi250019supp2_prod_1749674951.30054.pdf#page=6) lists exactly 13 axes: age ≥75, sex, physical frailty ≥3, polypharmacy ≥5 medications, health ≤75, resistant hypertension ≥3 BP drugs, HF, diabetes, CAD, stroke/TIA, sleep apnea, CKD with/without dialysis and sedentary exercise 0 days/week. REPORT [main p.6 primary narrative](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=6) says all predefined subgroups; REPORT [main p.9 Figure 3 and shared caption](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) includes the following six additional medication axes and calls subgroup interaction analyses prespecified. Complete supplied plan mapping and amendment text supply no corresponding primary treatment-effect medication-axis list; baseline drug collection, medication self-change order, external validity and diuretic adherence serve other purposes.

| Figure 3 axis | Exact affected location | Yes HR (95% CI), source matched | No HR (95% CI), source matched | Interaction P, matched | SAP primary subgroup counterpart |
|---|---|---|---|---|---|
| ACE inhibitor | [Figure 3, this axis](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | .74 (.52–1.05) | 1.14 (.86–1.51) | .05 | Absent |
| ARB | [Figure 3, this axis](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 1.07 (.70–1.64) | .93 (.72–1.20) | .44 | Absent |
| Beta-blocker | [Figure 3, this axis](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | 1.04 (.71–1.52) | .91 (.70–1.19) | .54 | Absent |
| Calcium channel blocker | [Figure 3, this axis](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | .92 (.65–1.30) | .99 (.74–1.31) | .66 | Absent |
| Diuretic | [Figure 3, this axis](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | .91 (.62–1.33) | .97 (.74–1.27) | .43 | Absent |
| Combination medication | [Figure 3, this axis](../jama_garrison_2025_oi_250019_1749674951.29054.pdf#page=9) | .95 (.49–1.85) | .93 (.74–1.17) | .72 | Absent |

**Transcription correction provenance:** The registered C008 narrative copied ARB No CI (.71–1.20); exact current main p.9 prints (.72–1.20). It copied CCB No (.76–1.31); source prints (.74–1.31). It copied diuretic Yes (.63–1.31); source prints (.62–1.33). Point estimates, other intervals, six P values and substantive prespecification comparison match. These are changes to the reviewer transcription, not proposed source alterations. The canonical current source map already has the source-matched limits.


**Reported-versus-comparator:** SAP 13 axes versus Figure 3 19 axes: six additional medication classes with all 12 HR/CI pairs and six interaction P values retained below.

**Reasoning procedure:** Compare every plan-list item and every printed axis. Retain all six medication axes as one prespecification pattern. Use the source-matched interval limits established by recheck; do not substitute interaction tests for within-subgroup tests.

**Calculation:** Six primary-outcome medication axes are under the printed prespecified caption but absent from the supplied prospective list, route A5. Set membership and caption coverage have no rounding interval. All twelve estimates remain inside ordered intervals that include one. Interaction tests concern heterogeneity, not within-subgroup significance; .05 is allowed its [.045,.055] interval and is not separately treated as a significance conflict. No independent log-HR-difference approximation substitutes for the stated interaction model.


**Affected result or extracted value:** Prespecification provenance of ACE inhibitor, ARB, beta-blocker, calcium channel blocker, diuretic and combination-medication primary-outcome subgroup effects/interactions.

**Why context does not resolve it:** Route A category 5 covers an analysis described as prespecified that the supplied plan does not contain. The full supplied specification has no counterpart for these six primary treatment-effect medication axes.

**Alternative source-grounded interpretations:** Direct observations are the six additional printed axes and prespecified caption versus supplied list. An unavailable prospective plan or limited caption scope may explain the comparison. Medication collection or a diuretic adherence substudy is not itself a primary treatment-interaction specification.


Unresolved source definition: Which prospective specification supports each of these six axes, or which exact axes does Figure 3's prespecified caption cover?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced_after_transcription_correction. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Caption, all six axes/effects/interactions and full supplied 13-axis SAP list are available. A supplemental prospective analysis specification and whether the caption intended to cover only the first 13 axes are absent. Individual model coefficients/covariance are not supplied; they are unnecessary for this membership comparison.


**Potential downstream evidence impact:** If confirmed, a subgroup extractor could classify these effects/interactions as prospectively specified based on the shared caption. Clarification affects prespecification metadata, without establishing a changed primary treatment result.

## C009 — Planned within-arm withdrawal sensitivity contrast

Pending Human Adjudication.

**Candidate statement:** Neither displayed retention table supplies the SAP primary-survival sensitivity comparison of censored versus not-censored participants within treatment groups.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP primary withdrawal sensitivity comparison vs REPORT results supplement eTables 4 and 5 contrasts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route A, category 5

**Classification rationale:** SAP sensitivity content is PLAN and the result-table contrasts are REPORT. The issue is the specified contrast/population rather than a preference between Fisher and Pearson tests; P_R and protocol_report apply.

**Classification ambiguity:** According to treatment group might have been intended more loosely, or an unprovided analysis may exist; absence is bounded to complete supplied report coverage.

**Exact source locations:**

PLAN [joi250019supp2_prod_1749674951.30054.pdf — physical PDF p. 6](../joi250019supp2_prod_1749674951.30054.pdf#page=6)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 33](../joi250019supp3_prod_1749674951.30054.pdf#page=33)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 34](../joi250019supp3_prod_1749674951.30054.pdf#page=34)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 35](../joi250019supp3_prod_1749674951.30054.pdf#page=35)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 36](../joi250019supp3_prod_1749674951.30054.pdf#page=36)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 37](../joi250019supp3_prod_1749674951.30054.pdf#page=37)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 38](../joi250019supp3_prod_1749674951.30054.pdf#page=38)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 39](../joi250019supp3_prod_1749674951.30054.pdf#page=39)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 40](../joi250019supp3_prod_1749674951.30054.pdf#page=40)

**Source evidence:** PLAN [SAP p.6 Sensitivity Analyses](../joi250019supp2_prod_1749674951.30054.pdf#page=6) specifies presenting, according to treatment group, baseline characteristics of those censored due to withdrawal/loss and comparing them with those not censored in that way using Fisher's exact test. REPORT eTable 4 at [p.33](../joi250019supp3_prod_1749674951.30054.pdf#page=33), [p.34](../joi250019supp3_prod_1749674951.30054.pdf#page=34), [p.35](../joi250019supp3_prod_1749674951.30054.pdf#page=35), [p.36](../joi250019supp3_prod_1749674951.30054.pdf#page=36) consistently compares pooled completed/death n2726 against interview withdrawal/loss n631. REPORT eTable 5 at [p.37](../joi250019supp3_prod_1749674951.30054.pdf#page=37), [p.38](../joi250019supp3_prod_1749674951.30054.pdf#page=38), [p.39](../joi250019supp3_prod_1749674951.30054.pdf#page=39), [p.40](../joi250019supp3_prod_1749674951.30054.pdf#page=40) compares morning n44 against bedtime n57 only among those lacking both interview and administrative follow-up. Every continuation header/content/footnote was visually inspected; none supplies within-arm censored-versus-other columns.


**Reported-versus-comparator:** Planned within-arm censored-versus-other comparison with Fisher exact versus pooled 2726/631 interview retention and cross-arm 44/57 all-follow-up-unavailable displays.

**Reasoning procedure:** Read all eight table pages and footnotes, then match contrast, treatment stratification and censoring population against the SAP. Distinguish interview loss from unavailable survival follow-up and search complete supplied report maps for the specified counterpart.

**Calculation:** The planned contrast requires censored versus not-censored within treatment groups; pooled interview-retention and cross-arm unavailable-follow-up comparisons are different contrasts. The current complete report maps/text contain no displayed counterpart. 44+57=101 and 631−101=530 are exact integer relationships; they reinforce that 631 includes people still administratively trackable, rather than all being unavailable to survival follow-up. No half-unit interval reconciles a different contrast or population. This concerns a prespecified primary survival-analysis sensitivity comparison, route A5, without recommending a preferred test.


**Affected result or extracted value:** The prospective withdrawal sensitivity analysis addressing composition of the primary survival-analysis population.

**Why context does not resolve it:** Route A category 5 covers a planned primary-analysis sensitivity comparison not reported in the supplied package. Different displayed contrasts do not provide the literal within-arm censored-versus-other comparison.

**Alternative source-grounded interpretations:** Column differences are directly observed. According to treatment group might have been intended more loosely; an unprovided output may exist. The two displayed analyses can be useful for different questions without establishing the specified contrast.


Unresolved source definition: Where is the specified within-arm censored-versus-not-censored comparison, or how were eTables 4/5 intended to implement that SAP sensitivity analysis?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Planned contrast and displayed columns are available. Within-arm baseline distributions for censored and not-censored people, exact analysis-specific censoring membership, and any unshown sensitivity table are absent. The supplied displays directly fail to implement the literal columns; absence of another output is supported by complete current maps/search and remains bounded to this package.


**Potential downstream evidence impact:** If confirmed, extraction could identify the displayed retention tables as the prespecified primary sensitivity analysis despite their different contrasts/populations. No numerical change in the primary survival result is asserted.

## C010 — eTable 4 chronotype test reproduction

Pending Human Adjudication.

**Candidate statement:** eTable 4 chronotype P=.09 does not reproduce from its displayed 2×3 counts using a method that reproduces other categorical rows of the same display.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 4 chronotype vs REPORT same-table supported categorical tests

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 4

**Classification rationale:** All compared counts, P values and comparator rows are REPORT within one results supplement. The statistical test-reproduction issue is S_W, statistical_results; the distinct planned contrast in C009 adds no P_R.

**Classification ambiguity:** None in roles/type; the chronotype-specific original test, coding or analytic subset is not supplied.

**Exact source locations:**

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 33](../joi250019supp3_prod_1749674951.30054.pdf#page=33)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 34](../joi250019supp3_prod_1749674951.30054.pdf#page=34)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 35](../joi250019supp3_prod_1749674951.30054.pdf#page=35)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 36](../joi250019supp3_prod_1749674951.30054.pdf#page=36)

**Source evidence:** REPORT [results p.33 eTable 4](../joi250019supp3_prod_1749674951.30054.pdf#page=33) gives completed/death n2726 early bird 1388, night owl 818, neither 520; withdrawal/loss n631 gives 352,154,125; chronotype P=.09. Same-page age, sex, education, ethnicity and province rows were read. REPORT [p.34](../joi250019supp3_prod_1749674951.30054.pdf#page=34) contains health/SBT/deprivation and binary tests, and REPORT [p.35](../joi250019supp3_prod_1749674951.30054.pdf#page=35) contains medication-count categories. [p.36 footnotes](../joi250019supp3_prod_1749674951.30054.pdf#page=36) allow missing data and define variables, with no chronotype-specific model or test.


**Reported-versus-comparator:** Printed P=.09 for [1388,818,520] versus [352,154,125]; Pearson from these margins gives P=.017964632.

**Reasoning procedure:** Establish the same-display method through independently reproducing categorical rows, then compute expected counts from margins and Pearson sum(O−E)^2/E for chronotype. Apply printed-value intervals and exact-count discreteness.

**Calculation:** Both printed chronotype columns sum exactly to their headers. Pearson Σ(O−E)²/E gives X²=8.038700681138563, df2, P=exp(−X²/2)=.017964632041896. The count half-unit intervals contain only those integers, giving a point recomputation interval. Printed .09 interval [.085,.095] leaves gap .067035367958104; relative gap/.09=.74483742>.05. No significance/CI claim is inferred; route A4 concerns supported-method reproduction.

Independently recomputed same-display support:

| Source location/row | Printed P | Pearson X²; df; recomputed P | Precision comparison |
|---|---|---|---|
| p.33 age | <.001 | 30.217601; 4; .00000441972 | Inequality matches |
| p.33 sex | .11 | 2.623387; 1; .10529946 | Within [.105,.115] |
| p.33 education | <.001 | 44.806702; 4; .00000000436 | Inequality matches |
| p.33 ethnicity | .008 | 18.854835; 7; .00865446 | Gap from [.0075,.0085]≈.00015446/.008=.01931≤.05 |
| p.33 province | <.001 | 24.020802; 4; .0000791115 | Inequality matches |
| p.35 BP medication categories | .15 | 5.395208; 3; .14504236 | Within [.145,.155] |
| p.35 non-BP categories | .21 | 5.913123; 4; .20573094 | Within [.205,.215] |

The p.34 rows and their definitions were inspected as additional same-display context; no assumption that continuous-median tests use Pearson is made. The categorical method is supported by multiple independent rows, including the medication categories cited in registration.


**Affected result or extracted value:** The extracted chronotype retention-association P value and its .05 reading.

**Why context does not resolve it:** Route A category 4 applies because the printed result does not reproduce beyond tolerance under a method supported by other rows. An unreported row-specific analysis remains a missing definition rather than removing this candidate.

**Alternative source-grounded interpretations:** The counts and .09 are directly observed, and Pearson .0179646 is reproduced arithmetic. A row-specific adjusted model/subset/coding could produce another P but is not disclosed. A production mechanism is not inferred.


Unresolved source definition: What exact test, coding and analysis population produced chronotype P=.09 when the printed categories under the same-display reproducing method yield approximately .018?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: All six chronotype counts, margins and P plus comparator-category counts are available. Original engine, chronotype-specific coding, analytic subset or adjusted test are unreported. These are the human question; no assumed method unsupported by the display is needed.


**Potential downstream evidence impact:** If confirmed, a reader could extract .09 for chronotype rather than the value associated with the same-display reproducing calculation. This concerns a retention-table test and does not establish a changed primary survival conclusion.

## C011 — eTable 5 ethnicity totals

Pending Human Adjudication.

**Candidate statement:** eTable 5 ethnicity category counts total 85/111 against morning/bedtime populations 44/57, with Other repeating White values and no printed overlap definition.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 5 ethnicity categories vs REPORT same-table population headers and footnotes

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 3

**Classification rationale:** All categories, population headers and footnotes are REPORT within one supplement. This is within-display count arithmetic, yielding S_W and statistical_results rather than a peripheral baseline-copy comparison.

**Classification ambiguity:** None in roles/type; the meaning of Other and permission for overlapping ethnicity responses remain undefined.

**Exact source locations:**

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 37](../joi250019supp3_prod_1749674951.30054.pdf#page=37)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 40](../joi250019supp3_prod_1749674951.30054.pdf#page=40)

**Source evidence:** REPORT [p.37 eTable 5](../joi250019supp3_prod_1749674951.30054.pdf#page=37) headers are morning n44 and bedtime n57. Exact ethnicity rows are White 40(90.9)/53(93.0), Asian 1(2.3)/1(1.8), Indigenous 1(2.3)/1(1.8), South East Asian/Indian 1(2.3)/1(1.8), Black 0(0.0)/1(1.8), Latino 1(2.3)/0(0.0), Other 40(90.9)/53(93.0), declined 1(2.3)/1(1.8). Every category was read visually; White and Other repeat exactly. REPORT [p.40 footnotes](../joi250019supp3_prod_1749674951.30054.pdf#page=40) allow percentages below total because data were missing and define other variables; no ethnicity overlap or aggregate-Other meaning is printed.


**Reported-versus-comparator:** Morning category total 85 versus n44; bedtime total 111 versus n57; percentage totals 193.3%/195.0%.

**Reasoning procedure:** Sum all eight categories and compare with each header, then assess percentage envelopes and footnote permissions. Do not infer replacement cells or reconstruct the ethnicity test from fabricated adjusted counts.

**Calculation:** Exact category totals 85 and 111 versus headers 44 and 57 give gaps 41/54, relative .93181818/.94736842. Half-unit count intervals intersected with integers remain point totals; even the wider continuous eight-count totals [81,89]/[107,115] versus header [43.5,44.5]/[56.5,57.5] leave gaps 36.5/49.5, far above .05. Percentages sum 193.3%/195.0%; the conservative sum intervals [192.9,193.7]/[194.6,195.4] cannot approach 100%. Individual displayed fractions, including Other, reconcile with headers; the issue is the simultaneous categorical distribution. Removing Other still gives 45/58 and does not supply an inferred replacement distribution. Route A3 applies within one display.


**Affected result or extracted value:** The ethnicity distribution for the 101 participants unavailable for both interviews and administrative follow-up, particularly Other 40 (90.9%)/53 (93.0%).

**Why context does not resolve it:** Route A category 3 applies to counts within one display. A missing-data note does not reconcile above-population totals, and an overlapping/aggregate Other meaning is not printed.

**Alternative source-grounded interpretations:** Direct observations are duplication and sums. An overlapping-Other definition or intended different cells might reconcile a different meaning; copying is an inferred possibility only, not a source fact.


Unresolved source definition: How is Other defined, are categories overlapping, and which ethnicity distribution should be extracted for morning44/bedtime57 given totals85/111?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: All categories, population totals and footnotes are available. Whether ethnicity permits multiple responses and whether Other is overlapping/aggregate rather than a mutually exclusive category are unreported. Missing data cannot by itself explain over-totaling.


**Potential downstream evidence impact:** If confirmed, a descriptive-data extractor could copy the repeated Other entries or above-population ethnicity distribution. No trial-wide composition change or corrected distribution is asserted.

## C012 — Identical medication tables, differing P values

Pending Human Adjudication.

**Candidate statement:** The identical diuretic and combination-medication comparisons in eTable 5 carry disjoint P values .34 and .38; the same-display reproducing calculation supports .38.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 5 diuretic vs REPORT same-table combination medication comparison

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4

**Classification rationale:** All comparison counts, tests, headers and comparator rows are REPORT in one results supplement. This is S_W, statistical_results; medication overlap does not distinguish identical individual binary tables.

**Classification ambiguity:** None in roles/type; a row-specific original method/model/subset is not disclosed.

**Exact source locations:**

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 39](../joi250019supp3_prod_1749674951.30054.pdf#page=39)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 37](../joi250019supp3_prod_1749674951.30054.pdf#page=37)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 40](../joi250019supp3_prod_1749674951.30054.pdf#page=40)

**Source evidence:** REPORT [p.39 eTable 5](../joi250019supp3_prod_1749674951.30054.pdf#page=39) prints both diuretic and combination BP medication as morning9(20.5)/bedtime16(28.1), with P=.34 and .38 respectively. REPORT [p.37 headers](../joi250019supp3_prod_1749674951.30054.pdf#page=37) supplies n44/n57. Same p.39 ACE 18/21, ARB13/11, CCB14/19 and beta-blocker8/14 comparator rows and tests were visually matched. [p.40 footnotes](../joi250019supp3_prod_1749674951.30054.pdf#page=40) supply no different denominators or row-specific test instructions for these two classes.


**Reported-versus-comparator:** Both morning 9/44 versus bedtime 16/57: diuretic P=.34, combination P=.38; Pearson P≈.379220621.

**Reasoning procedure:** Construct both full 2×2 tables including complements, confirm they are identical, and establish the reproducing method through other binary rows. Compare both printed P intervals and the computed P interval; do not presume the undisclosed original engine.

**Calculation:** Both exact 2×2 tables are [[9,35],[16,41]], Pearson X²=.773226936959624, df1. Independent numerical integration of the chi-square df1 tail gives P=.379220621 (about .37922062), reproducing combination .38. Count half-unit intervals intersected with integer domain permit no alternate table. P-copy intervals [.335,.345] and [.375,.385] leave gap .030, relative .030/.38=.07894737>.05. Recomputed P versus diuretic interval leaves gap .034220621/.34=.10064889>.05. The nine/44 and16/57 percentages round to20.5/28.1 and do not conflict.

Same-display binary support: ACE Pearson P≈.67721685 matches .68; ARB .23024913 matches .23; CCB .87210996 matches .87; beta-blocker .44119323 matches .44. Their half-unit P intervals overlap the recomputations. Same-page BP-medication categories P≈.31721536 matches .32 and non-BP categories .32416278 matches .32. Medication-class overlap does not distinguish the identical individual binary tables. Route A4 applies.


**Affected result or extracted value:** The diuretic-comparison P value in the unavailable-follow-up display.

**Why context does not resolve it:** Route A category 4 applies to a printed result not reproduced by a method supported elsewhere in the same display. Different undisclosed analyses are retained as alternatives, without being asserted as the source explanation.

**Alternative source-grounded interpretations:** Identical counts and differing P values are direct; Pearson reproduction is arithmetic. Different undisclosed row-specific methods could explain values, but their use is not a source fact and no source alteration is proposed.


Unresolved source definition: What exact analysis produced diuretic .34 rather than the identical combination comparison's .38, and did those rows use different populations or tests?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Exact event/non-event counts, population totals and both tests are available. Unstated row-specific method, adjusted model or subset would be needed to distinguish .34/.38. Original test engine is not supplied.


**Potential downstream evidence impact:** If confirmed, extraction could use .34 or .38 for identical printed count comparisons without a disclosed method distinction. No effect on the primary treatment estimate is demonstrated.

## C013 — ARB bedtime Other Reason fraction

Pending Human Adjudication.

**Candidate statement:** The eTable 8 ARB bedtime Other Reason/Cannot Remember cell prints 1/37 (7.7%), while the displayed fraction computes to 2.7027%.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 8 ARB bedtime Other Reason fraction vs REPORT same-table percentage and denominator definitions

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-003

**Qualifying route:** Route A, category 3

**Classification rationale:** The fraction, percentage, denominator context and footnote all belong to REPORT within the same supplement. Within-display ratio arithmetic is S_W, statistical_results.

**Classification ambiguity:** None in roles/type; the intended reason population/fraction is not supplied.

**Exact source locations:**

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 46](../joi250019supp3_prod_1749674951.30054.pdf#page=46)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 45](../joi250019supp3_prod_1749674951.30054.pdf#page=45)

REPORT [joi250019supp3_prod_1749674951.30054.pdf — physical PDF p. 48](../joi250019supp3_prod_1749674951.30054.pdf#page=48)

**Source evidence:** REPORT [results p.46 eTable 8](../joi250019supp3_prod_1749674951.30054.pdf#page=46), ARB PM Other Reason/Cannot Remember, prints 1/37 (7.7%). Same row neighboring CCB PM prints 2/26(7.7%). REPORT [p.45 ARB PM](../joi250019supp3_prod_1749674951.30054.pdf#page=45) prints failed attempts37/45(82.2%), side effects13/37(35.1%); p.46 side-effect subtypes use denominator13. REPORT [p.48 footnotes](../joi250019supp3_prod_1749674951.30054.pdf#page=48) restricts to once-daily baseline medicines still used at six months and explicitly permits multiple reasons per participant.


**Reported-versus-comparator:** Printed 1/37 (7.7%); recomputed 100/37=2.7027027%; neighboring CCB 2/26 gives 7.6923%, while ARB side-effect subtypes use denominator 13.

**Reasoning procedure:** Match the sparse ARB PM column visually, read failed-attempt and nested side-effect denominators, and compute the individual fraction with its display allowance. Distinguish multiple-response sums from one numerator/denominator ratio.

**Calculation:** Exact1/37×100=2.7027027027%, a point after integer-domain half-unit allowance. Printed7.7% interval[7.65,7.75] gives gap4.9472972973 percentage points, relative4.9472972973/7.7=.6425061425>.05. Even unconstrained continuous numerator/denominator half-unit intervals give100×[.5/37.5,1.5/36.5]=[1.33333333,4.10958904]%, still disjoint: gap≥3.54041096/7.7=.45979363>.05. Multiple responses can make sums exceed100 but cannot alter the printed ratio. Neighbor2/26×100=7.69230769 lies in[7.65,7.75]; failed-attempt and side-effect percentages also reconcile. Route A3 applies.


**Affected result or extracted value:** Other Reason/Cannot Remember frequency among failed ARB bedtime timing-change attempts at six months.

**Why context does not resolve it:** Route A category 3 applies to the individual fraction and percentage within the display. Multiple-response permission can affect summed categories but cannot change 1/37 into 7.7%.

**Alternative source-grounded interpretations:** Direct observation is1/37 beside7.7. Numerically7.7 also matches1/13 or adjacent2/26, but those are possible explanations, not the printed fraction for this cell. No intended replacement is inferred.


Unresolved source definition: What population and fraction applies to the ARB PM Other Reason/Cannot Remember cell, and which percentage should be extracted?


**Mechanical evidence recheck:** Every cited affected location was found; source and comparator readings matched the exact supplied PDF authority, and the consistency rule and calculation/logical comparison were reproduced. Final evidence state is reproduced. The independent auditor recorded CONFIRMED for inclusion. Necessary inputs and remaining definitions: Printed fraction, percentage, denominator context and multiple-response footnote are available. A definition assigning Other Reason to the side-effect subset13, or a different numerator/denominator, is absent.


**Potential downstream evidence impact:** If confirmed, a frequency extractor could copy 7.7% alongside 1/37 or assume an unstated denominator. No intended replacement value, trial-wide adherence effect or downstream propagation is established.

## Downstream Evidence-Chain Considerations

These candidates identify specific fields that might be copied into evidence extraction: incidence-rate quantities, endpoint event membership and recall windows, outcome hierarchy and subgroup prespecification, allocation/adaptive-rule provenance, sensitivity-analysis contrasts, categorical distributions, reason frequencies and displayed P values. If a candidate is confirmed through human adjudication, clarification could change how the affected field is recorded or how comparable outcomes/analyses are grouped.

No supplied evidence demonstrates that any candidate has propagated into a systematic review, meta-analysis or guideline, or changed an overall conclusion. Exact downstream numerical effects cannot be quantified from the package. A reconstructed diagnostic is not a final replacement for a source value; plausible amendments, overlapping definitions and undisclosed test conventions remain explicit alternatives.

## Limitations and Missing Definitions

Coverage is complete for all supplied evidence; missing definitions and unavailable additional inputs limit interpretation rather than source inspection. No individual-level dataset, workbook, CSV or executable analysis code is supplied. Exact total/subgroup person-time, original row-specific tests/models/subsets, fitted covariance and variance conventions, raw continuous distributions, interim tests and withdrawal dates are unavailable. Adjusted effects therefore were not required to equal crude calculations, and median/IQR displays were not treated as sufficient to reconstruct distributional tests.

Candidate-specific limits are Figure 3 quantity/scaling and person-time; prospective bridges for utilization/LTC criteria, allocation and adaptive diuretic assessment; outcome hierarchy/taxonomy and vision questionnaire versions; prospective counterparts or caption scope for six medication subgroup axes; the unshown within-arm censored-versus-other sensitivity comparison; chronotype/diuretic test conventions; ethnicity overlap and Other meaning; and the ARB Other Reason denominator. Source-grounded alternatives are retained in each card. The supplied original protocol is earlier than the final SAP, and the results supplement expressly discloses fully blinded changes. Version differences do not establish that two specifications were simultaneously operative or that a protocol violation occurred.

Referenced final-protocol, detailed prospective and separate nocturia/diuretic publications are not supplied. Their contents were not inferred or obtained externally. Current source annotations were not reviewer judgments. An annotation partly overlaps an administrative practice-map inset on results p.22; visible labels and all result-relevant evidence were mapped.

Historical SAP rendering/OCR engine versions remain unrecorded, despite matched source identity. Encoded SAP text and incomplete OCR derivatives were covered by visual reading of all seven page images. Missing direct PDF utilities were supplied by a pinned temporary package-local fallback; the first restricted-network installation attempt failed and an approved retry succeeded. GPU access was verified as requested, but readable source evidence required no new OCR and no GPU OCR engine was executed. Full durable limitations are in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The governing local controls are Workflow 1.6.2 scope, review contract, report specification, settings and performance profile. [Routing preflight](review_1_6_2/routing_preflight.md) records PASS, exact run model gpt-6.1-sol (DEFAULT), coordinator/high, ordinary specialists/medium and statistical/screen/recheck/audit specialists/high. Execution is INTERACTIVE_CLI with Provider CURRENT_SESSION; no provider credentials were written. Ten named presets were checked. The recorded launch command is the required convention, while process flags were not independently inspected.

Source and retained-asset integrity are recorded in the four-source and 233-asset before manifests and their [source after manifest](review_1_6_2/source_hashes_after.sha256) and [retained-asset after manifest](review_1_6_2/reused_artifact_hashes_after.sha256). Repeated completed checks found all hashes unchanged. Supplied sources, retained derivatives and earlier audit artifacts were preserved.

### Tooling and compute provenance

The [tooling record](review_1_6_2/tooling_record.md) documents the Linux probe, absent direct PDF/OCR/Office tools, available Pandoc, pinned fallback setup and final removal record. Missing capabilities used were info, native text, sorted/layout text and rendering. New renders were CPU, 200 dpi, PyMuPDF 1.26.4 through the bundled helper. The user's corrected interpreter `/home/juliz/venvs/stt/bin/python` initiated the successful bootstrap; no global installation was performed.

Compute device is recorded as GPU_USER_REQUESTED because the user authorized GPU OCR. Approved read-only PowerShell 5.1.26100.9444/NVIDIA access confirmed an RTX 5070 Laptop GPU, driver 616.56, 8151 MiB. This records authorization and access; actual review rendering was CPU and no new OCR/GPU OCR was necessary. HTML rendering and final mechanical validation use the supplied workflow scripts; they do not introduce external scientific evidence.

### Every actual agent execution

Each specialist was freshly spawned with a distinct runtime, fixed model and role-specific effort. Two optional support shards supplement the mandatory support stage. Pass 2 raised no findings, so the conditional second-screen stage was unnecessary. Artifact paths in the following table are relative to `review_1_6_2/`.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12bb5-744c-75d0-8603-7d2ccb5b6631 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12bb9-f5b3-73a3-8e07-0cd0adccbc02 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12bbc-5da9-7d42-af3f-0d5325decd82 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12bbc-89d0-7212-83f3-af724f1a019a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_results_a | 01a12bbc-b231-73f0-826a-30815634b6da | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_results_001_024.md |
| support_quantitative_mapper_results_b | 01a12bbc-d26c-7380-a8cf-40bfd4b5f2e4 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_results_025_049.md |
| numeric_consistency_reviewer | 01a12bc2-c4ca-7963-bbef-5b49f8963c59 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a12bc2-f62f-7690-92dd-2374810a7228 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12bc3-34f6-7a90-9ccf-69efae0c63b2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12bcf-3c84-72a3-8667-fcaaa0aecdfa | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a12bd9-199c-79b3-ad30-d9f4cbcb0965 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a12be3-797f-7a41-97f5-fe8093d565ce | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | 01a12beb-ba4e-7280-9114-0dfca0e1cd60 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a12bf3-79ae-7cf0-a5ed-a9ce0c457895 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

The package-specific planning target reflects fresh-source burden, visual-table complexity, relationship volume and mandatory review waves; it is not a coverage or candidate limit. The following values are copied from the coordinator's run record. Timing closes immediately after complete Markdown assembly; local HTML rendering and mechanical validation are outside that window.

- **Target basis:** Four PDFs of the BedMed trial, 86 total pages: 61 main/results pages require fresh mapping because prior source hashes differ; 25 protocol/SAP pages have matched reusable text/images, with SAP visual inspection needed for encoded text. No Office conversion. Four parallel mapping scopes, three initial checker roles, two statistical passes, independent screening, recheck, audit and report waves, plus pinned tooling setup justify a 40-65 minute package-specific planning range.
- **Total source units:** 86
- **Fresh-source units:** 61
- **Target elapsed minutes:** 40-65
- **Started UTC:** 2026-10-11T16:08:30Z
- **Finished UTC:** 2026-10-11T17:21:06Z
- **Observed elapsed minutes:** 72.60
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Fresh mapping of 61 main/results pages after historical source-hash mismatch; exact-source confirmation across 27 cited pages; complete two-pass review of 110 statistical relationships and 36 excluded observations; artifact-first audit and complete candidate-card assembly; network-restricted tooling setup followed by an approved pinned-package retry.
