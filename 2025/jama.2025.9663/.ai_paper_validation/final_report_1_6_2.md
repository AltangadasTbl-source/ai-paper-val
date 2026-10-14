# Quantitative Quality-Control Consistency Review — UK-ROX

**Pending Human Adjudication**

Workflow 1.6.2 evaluates quantitative reporting consistency in the supplied paper package. Every candidate below remains Pending Human Adjudication. Reproduction of a printed discrepancy and confirmation of inclusion are evidence-processing records, not adjudications of the authors' work or of a clinical conclusion.

## Executive Quality-Control Summary

Complete review of three supplied PDFs, comprising 176 physical pages, identified **five candidate reporting issues**. Nine independently screened findings consolidate into these five distinct issues: a retained primary-outcome companion analysis without a supplied result; differing protocol/SAP stay-analysis specifications; differing missing-data model specifications; hospital-duration censoring at one hour versus one day; and complementary pilot adherence numerator definitions under the same progression thresholds.

All five candidates have reproduced source evidence and CONFIRMED inclusion audits. Three belong to `protocol_report`, one to `statistical_results`, and one to `plan_material`. No candidate is assigned to `report_internal_inconsistency`. Both fresh independent statistical passes completed all 195 registered statistical relationships; numeric review completed all 233 numeric relationships. No interval-versus-P significance conflict was reproduced. No numerical effect change, actual pilot decision reversal, or paper-level conclusion change is established by this review.

## Package and Reused-Evidence Provenance

Document roles follow content. The bound prospective protocol/SAP is PLAN even though supplied as a supplement; the article and results supplement are REPORT. Page references throughout are one-based physical PDF pages, which can differ from printed footer numbers.

| Source ID | Supplied source | Role | Pages | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | [jama_martin_2025_oi_250042_1753377747.91025.pdf](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=1) | REPORT | 11 | `2081dc4315dd23f92712a5fd95cc03c5d3e9b7ee4fc8e24a27d8bf24d68c3266` |
| DOC-002 | [joi250042supp1_prod_1753377747.92525.pdf](../joi250042supp1_prod_1753377747.92525.pdf#page=1) | PLAN | 136 | `6fd5db6abde804baaa62264ddd158e664307941e4162fe1f2e80b4eb80662504` |
| DOC-003 | [joi250042supp2_prod_1753377747.93025.pdf](../joi250042supp2_prod_1753377747.93025.pdf#page=1) | REPORT | 29 | `bcd3bce5a729190ce6917128dc271f60ad99acb2f48395d86d69f88653e2469c` |

Of 483 assessed legacy evidence assets, 201 source-linked raw extraction, images or identity/provenance aids were reused. The other 282 were excluded: 273 unusable glyph-mapped text assets, three empty OCR assets and six mixed legacy extractor maps excluded in full because they contained scientific conclusions alongside extraction. Historical candidate, screening, classification, disposition and final-report records were preserved and excluded from scientific input. New discovery and classification were reconstructed from supplied sources.

Usable reused evidence covered 72 unique pages. All 104 uncovered pages received fresh source extraction and mapping. The user-requested RTX 5070 Laptop GPU supplied RapidOCR 1.4.4 transcription aids for all 136 PLAN pages through PowerShell 5.1, WSL and the existing `/home/juliz/venvs/stt/bin/python` environment. CPU rendering with pinned PyMuPDF 1.26.4 produced 104 new 170-dpi rasters; 32 unchanged reusable images supplied the remaining PLAN pages. Source images, not OCR, controlled printed-evidence confirmation. No package was installed into the shared interpreter.

The [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [fresh derivative inventory](review_1_6_2/preprocessing/fresh_derivative_inventory.md), [before-source hashes](review_1_6_2/source_hashes_before.sha256) and [before-reuse hashes](review_1_6_2/reused_artifact_hashes_before.sha256) retain the complete identities and provenance.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; statistical method logic; and planned-versus-reported statistical design. It does not extend to clinical suitability, novelty, misconduct, raw-data auditing or selection of a preferred analysis. Only supplied package evidence was used; no web or external literature was consulted.

| Source | Total pages | Reusable pages | Fresh-required pages | Mapped pages | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 article | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 protocol/SAP | 136 | 32 | 104 | 136 | COMPLETE |
| DOC-003 results supplement | 29 | 29 | 0 | 29 | COMPLETE |
| **Total** | **176** | **72** | **104** | **176** | **COMPLETE** |

Each source satisfies reusable plus fresh-required equals total and mapped equals total. Contents, references and administrative pages remain mapped, with their quantitative relevance stated explicitly. PLAN reusable pages are 29–56, 100, 120, 121 and 126; fresh-required pages are their complete complement: 1–28, 57–99, 101–119, 122–125 and 127–136. All 136 PLAN pages were visually corroborated, including lines omitted by OCR. No scientific source-unit gap remains.

Six mapper agents covered disjoint units: article 11 pages; results supplement 29 pages and opening PLAN 28 pages in separate parts; and further PLAN shards of 28, 32, 32 and 16 pages. Full source and stage assignments are recorded in [source coverage](review_1_6_2/source_coverage.md) and the [coverage manifest](review_1_6_2/coverage_manifest.md).

The inclusion threshold requires reproduction plus either an always-register category or all three general criteria: in focus, unresolved by immediate context, and relevant to a named interpretation or extracted quantity. For numeric comparisons, half-unit rounding intervals determine the gap; a relative discrepancy at most 0.05 is screened out. Interval-versus-P/test conflicts are always-register observations and cannot be dismissed as rounding. Model-based estimates are not replaced by crude calculations. Context-resolved wording, notation, conditional unreported details and peripheral comparisons do not generate candidate cards.

## Quantitative and Statistical Relationship Coverage

The complete [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains 233 distinct relationships: 87 main, 39 support and 107 further-PLAN records. [Numeric review](review_1_6_2/checkers/numeric_consistency.md) assessed every constituent of grouped displays, including 97 site rows and 222 explicit count/denominator/percentage cells; no cell sampling was used. The [cross-source review](review_1_6_2/checkers/cross_source_consistency.md) assessed 24 matched counterpart families across all three sources, using active amendments, outcome status, population, time point and model to match results.

The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains 195 distinct relationships: 40 main, 37 support/opening-PLAN and 118 further-PLAN records. Two different freshly spawned `gpt-6.1-sol`/high agents completed [pass 1](review_1_6_2/checkers/statistical_pass_1.md) and [pass 2](review_1_6_2/checkers/statistical_pass_2.md). Each pass retains bounded 77-record and 118-record assessment parts and explicit completion for all 195 IDs. Pass 2 read the complete stable ledger, screening and exact-source recheck, and independently reassessed all 26 prior checker excluded-observation rows against every always-register category and the display-precision rule. It emitted no new finding. The independent auditor also reassessed all 26 exclusions.

Checks included both available-case and imputed clinical result columns, all 11 confirmatory subgroup rows, all 13 posthoc rows and the exposure-difference intervals. Omnibus interaction P values were matched to their own hypotheses. Printed clinical point estimates lie within ordered intervals, and corresponding nonsignificant outcome P values agree with null-containing intervals. Exact unprinted tests or variance definitions were not assumed. A symmetric Wald diagnostic alone was not treated as proof of an incompatible one-year mortality P value. Sample-size diagnostics reconciled with rounded assumptions. These completed checks do not replace the missing implementation information named in the cards.

## Inclusion Screening Summary

The independent [screening log](review_1_6_2/screening/inclusion_screen.md) contains nine finding decisions. All nine are INCLUDE with `MEETS_THRESHOLD`; zero are SCREENED_OUT. Parallel checker findings describing the same issue retain their provenance as included rows sharing one stable ID, yielding five candidates. Pass 2 and audit raised no additional findings or screening reversals.

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 9 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |
| **Total** | **All finding decisions** | **9** |

The 26 checker **excluded observations** are separate from these nine formal findings and their decisions. Their independently retained reasons are precision 6, peripheral comparison 4, notation 1, not reproduced 3, conditional/unreported 5, context resolves 5, terminology 1 and model versus crude 1, totaling 26. They receive no stable IDs or cards. The [quality audit](review_1_6_2/quality/evidence_quality_audit.md) confirmed inclusion for five candidates and questioned none; no target candidate count governed screening.

## Review-Domain Summary

`statistical_results` concerns numerical results, test logic and statistical methods in REPORT material. `report_internal_inconsistency` concerns conflicting result attribution in REPORT material. `protocol_report` concerns prospective PLAN versus REPORT specifications. `plan_material` concerns statistical-design inconsistencies within PLAN content. Every candidate belongs to exactly one domain.

| Review domain | Candidates |
|---|---:|
| protocol_report | 3 |
| statistical_results | 1 |
| plan_material | 1 |
| report_internal_inconsistency | 0 |
| **Total** | **5** |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | PLAN versus REPORT | 3 |
| P_P | PLAN versus PLAN | 1 |
| S_C | Between REPORT documents | 1 |
| S_W | Within one REPORT document | 0 |
| **Total** | | **5** |

| Evidence state | Candidates |
|---|---:|
| reproduced | 5 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **5** |

Primary relationship counts count each candidate once. Additional relationships remain visible in the cards: C002 also involves P_P, and C003 also involves S_C. Precedence is P_R, then P_P, then S_C, then S_W. Corroborating context alone does not add a relationship.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Missing stratification-only primary-outcome analysis | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Retained protocol stay test versus SAP/report stay method | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | SAP all-outcome MICE versus reported predictors and stay censoring | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | Hospital missing-duration censoring at one hour versus one day | statistical_results | S_C | reproduced | CONFIRMED |
| C005 | Pilot adherence numerator and progression direction | plan_material | P_P | reproduced | CONFIRMED |

## Candidate Evidence Cards

Each card retains every affected supplied-source location and every included finding provenance ID from the [stable ledger](review_1_6_2/candidate_ledger.md). The [independent mechanical recheck](review_1_6_2/verification/evidence_recheck.md) confirmed source-image readings and classifications; the [independent quality audit](review_1_6_2/quality/evidence_quality_audit.md) confirmed inclusion. All cards remain Pending Human Adjudication.

## C001 — Missing stratification-only primary-outcome analysis

Pending Human Adjudication

**Candidate statement:** The final supplied protocol retains a 90-day mortality analysis adjusted only for randomization strata, alongside the fully adjusted primary model, but the supplied reports do not identify its treatment-effect result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol vs REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-002

**Qualifying route:** Route A, category 5

**Classification rationale:** The retained prospective protocol specification is PLAN and its absent counterpart is sought in REPORT content. The final SAP corroborates the reported fully adjusted model and provides possible supersession context; it is not an additional independently claimed P_P inconsistency.

**Classification ambiguity:** The detailed final SAP may intentionally supersede the protocol's companion analysis. The final protocol directs analyses to a SAP, but the supplied final SAP does not expressly identify removal of this retained analysis.

**Exact source locations:**

- PLAN original protocol: [joi250042supp1_prod_1753377747.92525.pdf — p. 30, §4.2.2](../joi250042supp1_prod_1753377747.92525.pdf#page=30).
- PLAN final protocol: [joi250042supp1_prod_1753377747.92525.pdf — p. 70, §4.2.2](../joi250042supp1_prod_1753377747.92525.pdf#page=70).
- REPORT model description: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 3, Statistical Analysis](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3).
- REPORT narrative effects: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 6, Primary and Secondary Outcomes](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=6).
- REPORT tabulated effects and adjustment sets: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 8, Table 2 and footnotes a/b](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8).
- PLAN alternative specification: [joi250042supp1_prod_1753377747.92525.pdf — p. 126, §5.3.1](../joi250042supp1_prod_1753377747.92525.pdf#page=126), [p. 127, continuation](../joi250042supp1_prod_1753377747.92525.pdf#page=127), and [p. 136, SAP changes](../joi250042supp1_prod_1753377747.92525.pdf#page=136).

**Source evidence:** Both original and final protocol pages explicitly specify analysis with stratification variables only and with additional baseline covariates; the fuller model is primary. This statement remains in final protocol v1.8, dated 14 October 2024. Main p. 3 specifies site and diagnostic subgroup plus age, SpO2, PaO2:FiO2, COVID-19 and date. Main p. 6 reports adjusted RD 0.7 percentage points (95% CI −0.7 to 2.0), P=.28, and expressly unadjusted RD 0.5 (−1.0 to 2.0). Table 2 gives available-case adjusted RD 0.7 (−0.6 to 2.1) and multiply-imputed adjusted RD 0.7 (−0.7 to 2.0), with RR 1.02 and OR 1.04; both columns have the full adjustment set. Complete current maps of the article's 11 pages and results supplement's 29 pages identify no separate stratification-only treatment-effect result.

**Reported-versus-comparator:** The protocol specifies two adjustment sets. The reports provide crude and fully adjusted estimates and two missingness columns, without a separately identified site/diagnostic-only regression effect.

**Reasoning procedure:** Match the primary endpoint, randomized contrast and covariate membership, then search the complete supplied REPORT scope for the companion model. A crude contrast does not reproduce adjustment for site and diagnostic strata. Available-case versus imputed data changes missingness handling, rather than removing extra covariates.

**Calculation:** No numerical companion estimate can be calculated from the supplied fuller model or crude contrast. Display-precision arithmetic is inapplicable to adjustment-set membership and absence of a named analysis; no difference between adjusted and crude RDs is treated as a numerical discrepancy.

**Affected result or extracted value:** The prespecified 90-day mortality treatment effect adjusted only for randomization strata, including its estimate and interval. Its numerical value is not inferred.

**Why context does not resolve it:** Route A, category 5 applies to a planned primary-outcome analysis without a result in the supplied reports. Possible SAP supersession remains an alternative rather than a basis for suppressing this reproduced retained specification.

**Alternative source-grounded interpretations:** Final SAP v1.1, dated 25 November 2024, may intentionally replace the shorter protocol specification; the final protocol says analyses will be lodged in a SAP. The SAP matches the reported fully adjusted model. Its changes page lists additions and expansions without an explicit cancellation of this companion model. A separately reported result outside the supplied package cannot be assumed.

**Mechanical evidence recheck:** Every listed location was found and visually reread. Printed protocol and report statements matched registration; full REPORT maps bounded the absent-counterpart search. The rechecker retained P_R/protocol_report and assigned reproduced without transcription correction. The missing companion result, implemented code and explicit replacement instruction are unprovided.

**Potential downstream evidence impact:** If confirmed, a data extractor could record the crude or fully adjusted result as the promised stratification-only companion analysis, or omit that prespecified analysis from an analysis inventory. No propagation or effect alteration is established.

## C002 — Retained protocol stay test versus SAP/report stay method

Pending Human Adjudication

**Candidate statement:** The final protocol retains survival-stratified Wilcoxon comparisons of ICU and acute-hospital stay, while both SAP versions and the report specify Fine–Gray competing-risk regression, without explicitly reconciling replacement versus addition.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN final protocol vs PLAN final SAP and REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004, F-ST1-004

**Qualifying route:** Route B

**Classification rationale:** Final protocol versus reported stay analysis is P_R; the retained final protocol versus final SAP is P_P. The SAP and report agree, so they add no separate relationship. P_R takes precedence and determines protocol_report.

**Classification ambiguity:** The later detailed SAP may have superseded the shorter protocol specification, or both analyses may have been retained. The supplied specifications do not explicitly state their relationship.

**Exact source locations:**

- PLAN original protocol: [joi250042supp1_prod_1753377747.92525.pdf — p. 30, §4.2.2](../joi250042supp1_prod_1753377747.92525.pdf#page=30).
- PLAN final protocol: [joi250042supp1_prod_1753377747.92525.pdf — p. 70, §4.2.2](../joi250042supp1_prod_1753377747.92525.pdf#page=70), and [p. 71, continuation](../joi250042supp1_prod_1753377747.92525.pdf#page=71).
- PLAN original SAP: [joi250042supp1_prod_1753377747.92525.pdf — p. 104, §5.3.2](../joi250042supp1_prod_1753377747.92525.pdf#page=104).
- PLAN final SAP: [joi250042supp1_prod_1753377747.92525.pdf — p. 128, §5.3.4](../joi250042supp1_prod_1753377747.92525.pdf#page=128).
- REPORT methods: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 3, Statistical Analysis](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3).
- REPORT stay results: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 8, Table 2](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8).
- PLAN amendment context: [joi250042supp1_prod_1753377747.92525.pdf — p. 136, SAP changes](../joi250042supp1_prod_1753377747.92525.pdf#page=136).

**Source evidence:** Original protocol p. 30 and final protocol pp. 70–71 prescribe Wilcoxon rank-sum tests stratified by survival status for ICU and acute-hospital duration. Original SAP p. 104 and final SAP p. 128 prescribe proportional-hazards regression using Fine and Gray to account for competing death. Main p. 3 expressly names Fine–Gray subdistribution hazards regression. Table 2 gives ICU sHR 1.00 (95% CI 0.96 to 1.04), P=.97, and hospital sHR 0.98 (0.94 to 1.02), P=.27. Complete supplied REPORT maps identify no separate Wilcoxon stay result.

**Reported-versus-comparator:** The report's named competing-risk regression agrees with the SAP and differs from the retained final protocol's survival-stratified rank-sum procedure for the same stay endpoints.

**Reasoning procedure:** Match outcomes and randomized contrast across active plan versions and report, distinguish rank-based comparison from competing-risk regression, and check whether the package explicitly describes replacement or an additional retained comparison. The report clearly identifies its method, but does not identify the status of the other retained prospective test.

**Calculation:** Method identity is a logical comparison; half-unit rounding intervals do not apply. No rank-sum statistic can be reconstructed from medians/IQRs. No sHR/P incompatibility or method preference is asserted.

**Affected result or extracted value:** The prospective analysis specification attached to ICU sHR 1.00 and hospital sHR 0.98 and their P values, including whether these results replace the retained protocol comparisons.

**Why context does not resolve it:** This is an eligible planned-versus-reported analysis-model comparison within focus D. The final protocol and SAP retain different explicit procedures without saying replacement versus addition; that uncertainty affects which prespecified analysis an extractor would associate with the named stay results.

**Alternative source-grounded interpretations:** The protocol directs analyses to a SAP, supporting possible intentional refinement by the detailed SAP. Alternatively both comparisons may have been retained with only one reported. The difference is present in the final supplied protocol, rather than relying solely on an obsolete version. No claim is made about the suitability of either procedure.

**Mechanical evidence recheck:** All cited source locations were visually confirmed, including the protocol sentence spanning pp. 70–71. The distinct procedure statements and reported sHRs reproduce the registered comparison. The rechecker retained P_R with P_P and protocol_report. The replacement/addition instruction, any retained Wilcoxon statistic and analysis code are absent.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could record the reported sHR analysis as implementing the protocol's rank-sum test, or record an unreconciled change in the prospective stay-analysis specification. No resulting effect or conclusion change is established.

## C003 — SAP all-outcome MICE versus reported selected predictors and stay censoring

Pending Human Adjudication

**Candidate statement:** Final SAP §7 specifies MICE models using all outcome variables, while the results supplement lists selected auxiliary outcomes or None and early censoring for unavailable stay times. Main p. 3's auxiliary description also differs from the one-year None entry, with a bounded ambiguity about its applicability to every outcome-specific model.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN final SAP vs REPORT main article and REPORT results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-003

**Qualifying route:** Route B

**Classification rationale:** Final SAP versus reported predictors and duration handling is P_R. Main p. 3's at-least-primary-outcome auxiliary statement versus the supplemental one-year None row supplies S_C within this same missing-data specification pattern. P_R precedence selects protocol_report. Main p. 8 explicitly states its duration exception and adds no S_W relationship. The duration-only checker observation is consolidated with the broader predictor pattern.

**Classification ambiguity:** The main auxiliary sentence may describe the imputation exercise generally rather than a universal requirement for every secondary model. The auxiliary column could list selected extras while other outcomes enter through an unprinted mechanism. These alternatives qualify interpretation of S_C; the explicit final-SAP/report specification difference remains.

**Exact source locations:**

- PLAN final SAP: [joi250042supp1_prod_1753377747.92525.pdf — p. 131, §7 start](../joi250042supp1_prod_1753377747.92525.pdf#page=131), and [p. 132, §7 continuation](../joi250042supp1_prod_1753377747.92525.pdf#page=132).
- REPORT imputation description: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 3, imputation paragraph](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3).
- REPORT effects and duration exception: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 8, all imputed Table 2 outcomes and footnote b](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8).
- REPORT complete outcome-specific model/auxiliary rows and baseline footnote: [joi250042supp2_prod_1753377747.93025.pdf — p. 24, eTable 7, every row and footnote a](../joi250042supp2_prod_1753377747.93025.pdf#page=24).
- REPORT missing ICU/hospital duration handling: [joi250042supp2_prod_1753377747.93025.pdf — p. 24, duration rows and footnote e](../joi250042supp2_prod_1753377747.93025.pdf#page=24).
- PLAN amendment context: [joi250042supp1_prod_1753377747.92525.pdf — p. 136, expanded missing-data description](../joi250042supp1_prod_1753377747.92525.pdf#page=136).

**Source evidence:** SAP pp. 131–132 anticipates unavailable secondary outcomes after refused/withdrawn consent and specifies MICE with all adjusted-model baseline variables and all outcome variables, imputed primary analysis with complete cases alongside, 20 datasets and Rubin combination. Computational alternatives are five datasets with 1000 bootstrap replications, or complete-case RD/OR with imputed OR only; neither states a predictor-selection or missing-stay censoring exception. Hourly treatment-delivery carry-forward is a separate task explicitly not affecting outcome analysis. Main p. 3 describes incorporating at least the primary outcome as an auxiliary supporting secondary-outcome imputation; p. 8 excepts ICU/hospital durations from multiple imputation. Every eTable 7 row was directly reread:

| Outcome | Printed imputation model | Printed auxiliary variables |
|---|---|---|
| 90-day mortality | Logit | Duration of acute hospital stay |
| ICU duration | Censoring | N/A |
| Acute-hospital duration | Censoring | N/A |
| Days alive and free from organ support at 30 days | Ordered logit | 90-day mortality; mortality at ICU discharge |
| Mortality at ICU discharge | Logit | 90-day mortality |
| Mortality at acute-hospital discharge | Logit | 90-day mortality; duration of acute hospital stay |
| 60-day mortality | Logit | 90-day mortality; one-year mortality |
| One-year mortality | Logit | None |

Footnote a separately includes allocated treatment and adjusted baseline predictors in all models. Missing ICU/hospital durations are 1653 (10.1%)/1677 (10.2%). One-year mortality has 1661 (12.7%) missing among 13052 reaching one year; Table 2 prints available-case RD 1.0 (95% CI −0.7 to 2.6) and imputed RD 3.3 (−0.7 to 7.3).

**Reported-versus-comparator:** The final SAP's all-outcome predictor specification differs from eTable 7's selected/None auxiliaries and its broad MICE procedure differs from explicit duration censoring. Main p. 3's at-least-primary auxiliary description is not explicitly reconciled with the one-year None row.

**Reasoning procedure:** Compare predictor membership and missing-data operation for each outcome, preserving the baseline footnote separately from outcome auxiliaries. Consolidate the duration-only and broader observations as one pattern. Do not equate differently labeled observed/imputed effects or infer numerical consequences from the printed specification differences.

**Calculation:** Predictor-set membership and imputation-versus-censoring require logical comparisons; half-unit intervals do not apply. The one-year RDs are distinct labeled analyses, so their difference is not a conflicting-copy calculation. SAP p. 132 prints 1000 bootstrap replications: an earlier current-run locator transcription of 100 was corrected before registration and is not a supplied-source finding.

**Affected result or extracted value:** Outcome-specific missing-data specifications for the primary and secondary imputed effects, particularly one-year RD 3.3, and for ICU/hospital sHRs 1.00/0.98. Their numerical change under alternative specifications is not observable here.

**Why context does not resolve it:** Predictor membership and missing-outcome procedures are explicit eligible analysis specifications within focus D. The baseline-only footnote does not supply the unlisted outcome predictors, and the stated computational alternatives do not identify a censoring exception. The report describes handling but does not reconcile it with the final prospective specification. These differences concern named extracted analyses, rather than only an incidental unreported detail.

**Alternative source-grounded interpretations:** The SAP may provide a general framework refined during implementation or intended only for discrete outcomes. eTable 7 might list selected extra auxiliary variables while other outcomes enter elsewhere, although its None entry and baseline footnote do not describe that mechanism. Main p. 3 might summarize a typical practice across models without requiring a primary-outcome predictor in every secondary model. The final changes page discloses expanded missingness planning, but does not explain departure from that final specification. No external amendment or implementation code is assumed.

**Mechanical evidence recheck:** Every named page, eTable row and relevant footnote was visually confirmed. The rechecker reproduced the printed predictor/procedure difference and retained P_R, S_C/protocol_report, explicitly preserving the nonuniversal auxiliary-sentence interpretation. No post-registration transcription correction occurred. Implemented predictor matrices, unlisted outcome-entry mechanisms, censoring integration and any implementation amendment are unavailable.

**Potential downstream evidence impact:** If confirmed, an extractor could record all-outcome MICE, selected auxiliary models or early censoring as the implemented missing-data strategy without distinguishing their supplied specifications. This could affect an analysis-description inventory or reproducibility extraction; no actual estimate change or propagation is established.

## C004 — Hospital missing-duration censoring at one hour versus one day

Pending Human Adjudication

**Candidate statement:** Main Table 2 assigns one-hour censoring to missing acute-hospital discharge durations, while supplemental eTable 7 assigns one-day censoring to those durations.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article vs REPORT results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-001

**Qualifying route:** Route B

**Classification rationale:** Both conflicting times are methods/results statements in different REPORT documents. They concern statistical method logic for the same hospital result, determining statistical_results and S_C. SAP imputation-versus-censoring is the distinct rule in C003 and is not added here.

**Classification ambiguity:** None

**Exact source locations:**

- REPORT hospital effect and censoring definition: [jama_martin_2025_oi_250042_1753377747.91025.pdf — p. 8, Table 2 acute-hospital stay row and footnote b](../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8).
- REPORT hospital missing count and outcome-specific censoring definition: [joi250042supp2_prod_1753377747.93025.pdf — p. 24, eTable 7 acute-hospital duration row and footnote e](../joi250042supp2_prod_1753377747.93025.pdf#page=24).

**Source evidence:** Main footnote b explicitly includes both ICU and acute-hospital duration and says unavailable discharge times were censored one hour after randomization. Supplement footnote e assigns one hour to ICU duration and one day to acute-hospital duration, with 1677 (10.2%) missing hospital durations. Table 2 prints hospital adjusted sHR 0.98 (95% CI 0.94 to 1.02), P=.27, in both available-case and imputed columns.

**Reported-versus-comparator:** The same missing hospital-duration observations have stated censoring at 1 hour in the main article and 1 day in the results supplement. Their ICU definitions agree and do not resolve the hospital distinction.

**Reasoning procedure:** Match hospital endpoint, unavailable duration population and randomization time origin across both footnotes; convert both stated times to hours; then apply a conservative display-precision check. Identical displayed hospital sHRs do not identify which cutoff generated the analysis.

**Calculation:** One day equals 24 hours; the specified operational gap is 24−1=23 hours. Even allowing half-unit intervals for printed integers gives main [0.5,1.5] hours and supplement [0.5,1.5] days=[12,36] hours. Minimum gap=12−1.5=10.5 hours; relative discrepancy against printed main 1 hour=10.5/1=10.5, above 0.05. The discrepancy remains under these unusually broad rounding intervals. No sHR or P value is recomputed.

**Affected result or extracted value:** The missing-discharge censoring cutoff attached to the acute-hospital sHR 0.98 analysis, concerning 1677 unavailable durations.

**Why context does not resolve it:** Contradictory explicit times are statistical method logic within focus C, rather than a peripheral observation count. Both footnotes name the hospital endpoint and neither identifies a separate analysis. Calendar-day measurement does not make one hour equal one day; the package does not identify the implemented cutoff at once. This leaves a specific extracted analysis definition unresolved.

**Alternative source-grounded interpretations:** The main footnote may generalize the ICU cutoff to hospital stay, or the supplement's hospital time may differ from implementation. Neither location states that it describes another model. The identical sHRs cannot choose between these interpretations. This is a quantity-changing definition, not a missing unit resolved by adjacent values.

**Mechanical evidence recheck:** Both entire footnotes and matched hospital row were visually reread. Their outcome attribution and printed times matched registration, and the nonoverlapping half-unit intervals reproduced the comparison. S_C/statistical_results and reproduced were retained without correction. Actual censoring timestamps and analysis code are unprovided.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either the one-hour or one-day hospital censoring convention into a methods inventory or reproduction specification. No change in the printed hospital effect, significance or conclusion is established.

## C005 — Pilot adherence numerator and progression direction

Pending Human Adjudication

**Candidate statement:** Both SAP pilot tables apply high-is-Green treatment-adherence thresholds to a footnoted fraction with at least one adjudicated protocol deviation, while the supplied adherence definition uses no deviation; these complementary event definitions imply different progression classifications.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN original SAP vs PLAN final SAP and PLAN final protocol

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route B

**Classification rationale:** Every conflicting definition and prospective decision rule is PLAN content. The final protocol corroborates the adherence interpretation; REPORT adherence descriptions are not conflicting comparators. Thus the candidate is P_P/plan_material with no added report relationship.

**Classification ambiguity:** None

**Exact source locations:**

- PLAN original SAP numerator and thresholds: [joi250042supp1_prod_1753377747.92525.pdf — p. 95, Table 1 and footnote](../joi250042supp1_prod_1753377747.92525.pdf#page=95).
- PLAN original SAP adherence definition: [joi250042supp1_prod_1753377747.92525.pdf — p. 98, §3.2.2 continuation](../joi250042supp1_prod_1753377747.92525.pdf#page=98).
- PLAN final SAP repeated numerator and thresholds: [joi250042supp1_prod_1753377747.92525.pdf — p. 118, Table 1 and footnote](../joi250042supp1_prod_1753377747.92525.pdf#page=118).
- PLAN final protocol adherence definition: [joi250042supp1_prod_1753377747.92525.pdf — p. 69, Table 2 adherence footnote](../joi250042supp1_prod_1753377747.92525.pdf#page=69).
- PLAN decision consequences: [joi250042supp1_prod_1753377747.92525.pdf — p. 70, §4.2.1](../joi250042supp1_prod_1753377747.92525.pdf#page=70), [p. 96, original SAP pilot continuation](../joi250042supp1_prod_1753377747.92525.pdf#page=96), and [p. 119, final SAP pilot continuation](../joi250042supp1_prod_1753377747.92525.pdf#page=119).

**Source evidence:** Both SAP tables label Treatment adherence: Green ≥75% cases, Amber 50–75%, Red <50%. Their progression footnotes define this percentage from conservative-group patients with one or more adjudicated protocol deviations. Original SAP p. 98 defines patient-level adherence as not experiencing any protocol deviation. Final protocol p. 69 defines adherence as ventilator-setting or supplemental-oxygen adjustments according to protocol. Final protocol p. 70 and SAP continuations state all-green progression unchanged, any-amber amendment and any-red stop, with final funder decision following TSC recommendation.

**Reported-versus-comparator:** The SAP's progression footnote uses the at-least-one-deviation fraction, while the adherence definition and protocol counterpart use adherence. The same high-is-Green thresholds are attached to complementary event memberships. This is solely a comparison within supplied PLAN material.

**Reasoning procedure:** Hold the conservative population and adjudicated event scope fixed; define deviation and no-deviation fractions as complements; map the printed traffic-light inequalities onto each numerator. Keep the algebraic demonstration separate from any observed trial fraction or actual decision.

**Calculation:** Let d be the fraction with at least one adjudicated deviation and a the fraction with none: a=1−d. Green d≥0.75 implies a≤0.25, while Green a≥0.75 implies d≤0.25. Red d<0.50 implies a>0.50. Illustrative a=0.80 and d=0.20 yields Green with the adherence numerator and Red with the footnote numerator; these are demonstration values, not trial observations. The conflict concerns event membership rather than a rounded percentage. Even a sensitivity allowing 75% to span [74.5%,75.5%] maps the deviation-based Green boundary to adherence [24.5%,25.5%], separated from the adherence-based boundary by at least 49 percentage points; relative gap 49/75≈0.653 exceeds 0.05. That sensitivity does not reinterpret the stated thresholds as actually rounded.

**Affected result or extracted value:** The prospective pilot adherence numerator and its ≥75%/50–75%/<50% progression classification. The actual pilot fraction, color or decision is not inferred.

**Why context does not resolve it:** A planned progression rule is explicitly within focus D. The footnote and adherence definition assign mathematically distinct quantities to the decision metric; a likely intended complement does not identify which was applied. This changes the possible classification of the named prospective rule and the numerator an extractor would record, rather than merely changing terminology.

**Alternative source-grounded interpretations:** The deviation fraction may have been intended for separate nonadherence reporting while progression used its complement. Alternatively the footnote may define the applied statistic, leaving the high-is-Green direction unclear. The no-deviation definition supports the first possibility but does not establish the actual applied rule. Exact equality conventions at threshold boundaries are separate and are excluded from this candidate.

**Mechanical evidence recheck:** Every cited table, definition and decision-consequence page was found and visually reread. The repeated deviation numerator and no-deviation adherence definition reproduced the complement calculation. P_P/plan_material and reproduced were retained without correction. The pilot denominator, adjudicated count, applied fraction/color and decision record are absent, preventing reconstruction of an actual decision.

**Potential downstream evidence impact:** If confirmed, an extractor could record the deviation fraction as the adherence progression metric or attach the opposite event membership to its thresholds. No actual pilot decision reversal, trial effect change or downstream propagation is established.

## Downstream Evidence-Chain Considerations

A synthesis or methods inventory may record an endpoint, effect measure, analysis population, covariate set, missing-data procedure and prospective decision rule together. These candidates concern the linkage between those fields. An effect estimate can remain numerically unchanged in the supplied displays while its accompanying prospective specification or censoring definition remains unresolved. Extracting an unlabeled companion analysis, selecting an hour/day cutoff or treating selected auxiliary predictors as all outcomes could therefore yield different descriptions of the same supplied result if the candidate is confirmed.

These are possible extraction consequences, not observed evidence-chain events. No raw-data reanalysis was performed; the review establishes neither a change in clinical inference nor harm, propagation or a preferred analysis. Independent recheck and inclusion audit confirm source evidence and workflow scope, while every candidate remains Pending Human Adjudication.

## Limitations and Missing Definitions

All 176 source pages and all registered relationships are mapped; there is no remaining scientific source-unit gap. The review is bounded to the three supplied PDFs. Analysis code, implementation amendments and participant-level records are unavailable. Absence of a counterpart is confined to the complete supplied REPORT scope, not an assertion about all possible publications.

Candidate-specific unavailable information includes the stratification-only companion result and explicit cancellation/replacement instruction for C001; replacement versus addition and any retained rank-sum result for C002; implemented predictor matrices, unlisted outcome-entry mechanisms and duration exceptions for C003; actual hospital censoring timestamps for C004; and the observed pilot denominator, count, progression fraction/color and decision record for C005. These inputs are necessary to establish implementation or consequences and were not invented.

Other bounded statistical limitations include unrounded test/variance/degree-of-freedom and bootstrap details, exact unknown-death-time estimation, actual repeat-enrollment contributions and exact graphical ordinates. Model-based estimates were not substituted with crude ratios, and diagnostic approximations did not replace stated analyses.

PLAN native/layout extraction is glyph-mapped and unusable. Some legacy engine metadata is incomplete; OCR can omit whole lines. Complete source-image mapping and independent exact-source recheck closed those derivative gaps. The first GPU smoke test omitted CUDA libraries and fell back to CPU; corrected setup and the 136-page batch did not report CPU fallback. Raw warning and provenance logs remain available. No packages were installed into the shared environment. These limitations and their bounded effects are retained in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and integrity

Run model is `gpt-6.1-sol`, source DEFAULT. [Routing preflight](review_1_6_2/routing_preflight.md) records PASS, CURRENT_SESSION provider, INTERACTIVE_CLI execution, coordinator inference PASS and all ten named presets verified against their fixed model/effort pairs. Credentials and provider configuration were not changed. Scientific input was limited to supplied sources and usable source-linked evidence aids; all historical scientific conclusions were excluded.

The [tooling record](review_1_6_2/tooling_record.md) records absent direct Linux PDF/OCR executables and a pinned package-local temporary fallback for PDF information/rendering, plus the user-requested RTX 5070 Laptop GPU OCR through PowerShell 5.1. Shared existing RapidOCR/ONNX/CUDA libraries were used without package installation. The workflow removes only its temporary fallback environment during coordinator closure after HTML rendering.

Before hashes identify all three direct sources and all 201 selected reused assets. The independent auditor checked every recorded entry with sha256sum and found matches. Fresh [after-source hashes](review_1_6_2/source_hashes_after.sha256) and [after-reuse hashes](review_1_6_2/reused_artifact_hashes_after.sha256) match their before manifests; the [integrity record](review_1_6_2/integrity_checks.md) records both comparisons as PASS. The tooling record records temporary-environment removal during final closure. The final [review_validation.json](review_1_6_2/review_validation.json) records the mechanical validation outcome; rendering and validation occur after complete Markdown assembly. Scientific source completeness and candidate inclusion do not substitute for that mechanical check.

Canonical scientific artifacts are the [main map](review_1_6_2/extraction/main_quantitative_evidence.md), [complete support map](review_1_6_2/extraction/support_quantitative_evidence.md), [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_2/statistics/relationship_inventory.md), [candidate ledger](review_1_6_2/candidate_ledger.md), [screening](review_1_6_2/screening/inclusion_screen.md), [recheck](review_1_6_2/verification/evidence_recheck.md) and [quality audit](review_1_6_2/quality/evidence_quality_audit.md). Bounded parts and every stage assignment remain linked through the [coverage manifest](review_1_6_2/coverage_manifest.md).

### Agent execution

The [execution manifest](review_1_6_2/agent_execution_manifest.md) records every actual agent exactly once. Canonical specialist runtime task identifiers are normalized without the leading slash; each specialist started fresh and retained its fixed role effort. The two high-effort statistical passes are different runtimes. Statistical pass 1 continued within its original stage to finalize durable output; it was not promoted or reused for another mandatory stage. No pass-2 inclusion screener was applicable because pass 2 emitted no new finding.

| Stage | Runtime agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | 01a12bb5-8e9a-7c13-9d8e-be103f4ff6f5 | gpt-6.1-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_plan_b_mapping | root/plan_b_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_plan_c_mapping | root/plan_c_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_plan_d_mapping | root/plan_d_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| support_plan_e_mapping | root/plan_e_mapper | gpt-6.1-sol | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistical_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistical_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN |

### Reproducibility performance

The fields below are copied from [run_state.md](review_1_6_2/run_state.md). The coordinator finalizes finish time, elapsed duration and target status immediately after complete Markdown assembly; local HTML rendering and validation are outside that review duration.

- **Target basis:** Three PDFs with 176 pages; 104 plan pages lack usable reusable extraction and require fresh rendering/OCR or visual mapping, while 72 pages have reusable aids. Versioned protocol/SAP comparisons, dense main/result tables, at least five bounded mapping scopes, GPU tooling setup and the mandatory two statistical/screening/recheck/audit/report waves support a 65-100 minute package target.
- **Total source units:** 176
- **Fresh-source units:** 104
- **Target elapsed minutes:** 65-100
- **Started UTC:** 2026-10-11T16:08:08Z
- **Finished UTC:** 2026-10-11T17:31:42Z
- **Observed elapsed minutes:** 83.57
- **Target status:** MET_TARGET
- **Exceedance causes:** None
