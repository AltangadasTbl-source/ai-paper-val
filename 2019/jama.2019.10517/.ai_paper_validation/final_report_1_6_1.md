# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.1

**Pending Human Adjudication**

This review concerns the supplied STOP-PD II paper package, *Effect of Continuing Olanzapine vs Placebo on Relapse Among Patients With Psychotic Depression in Remission: The STOP-PD II Randomized Clinical Trial*, JAMA, 2019, DOI 10.1001/jama.2019.10517. Every candidate below requires human adjudication. Evidence-state and inclusion-audit fields record source reproduction and application of the review scope; they do not supply a human decision.

## Executive Quality-Control Summary

Complete review of four supplied PDFs, comprising **63 of 63 pages**, produced **two stable candidates: C001 and C002**. Both concern a prospective protocol specification compared with the published report. C001 concerns the additional baseline-change condition in the score-based component of the primary relapse definition. C002 concerns the relationship between prospective metabolic observation exclusion and the reported main-versus-sensitivity analysis hierarchy.

Both candidates have review domain `protocol_report`, relationship type `P_R`, evidence state `reproduced`, and inclusion audit `CONFIRMED`. All seven C001 and four C002 source-location instances were mechanically rechecked. The source comparison does not establish a changed event count, coefficient, statistical significance, or study conclusion. In particular, C001 uses possible-score illustrations rather than observed participant records; C002 does not equate inclusion of all participants with inclusion of all their later observations.

All **167 numeric relationships** and **88 statistical/design relationships** are accounted for. Each statistical relationship received two complete reviews by different fresh specialists. Six initial findings received independent screening: two were included, two consolidated as duplicates, and two screened out for substantive scope reasons. Statistical pass 2 and both quality-audit scopes produced no additional qualifying finding. No candidate-count target was applied.

## Package and Reused-Evidence Provenance

Document roles are assigned by content. The bound protocol/analytic/operational supplement is `PLAN`; the result-figure supplement is `REPORT`. The data-access document is operational `PLAN` material with no applicable trial-result or inferential relationship.

| Source ID | Actual supplied filename | Content role | PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_flint_2019_oi_190079.pdf — title and abstract, PDF p.1](<../jama_flint_2019_oi_190079.pdf#page=1>) | REPORT: main trial article | 10 |
| DOC-002 | [joi190079supp1_prod.pdf — protocol contents, PDF p.1](<../joi190079supp1_prod.pdf#page=1>) | PLAN: protocol, analytic plan and operational/pharmacotherapy appendices | 42 |
| DOC-003 | [joi190079supp2_prod.pdf — supplementary contents, PDF p.1](<../joi190079supp2_prod.pdf#page=1>) | REPORT: nine supplementary result figures | 10 |
| DOC-004 | [joi190079supp3_prod.pdf — data-access conditions, PDF p.1](<../joi190079supp3_prod.pdf#page=1>) | PLAN: prospective operational access conditions | 1 |
| Total | Four direct sources; no supplied Office, workbook or CSV source | Two REPORT and two PLAN documents | 63 |

The curator inventoried and hashed **187 reused evidence assets**, including native, layout, normalized and OCR text, complete source-linked page renderings, extraction/document maps and location metadata. Overlapping aids do not increase source-page counts. Every page had a usable extraction or rendering aid. Sparse chart text was supplemented by complete renderings; exact unprinted plot coordinates were not invented. Existing OCR was reused read-only. All scientific mapping, finding discovery, screening and classification were performed anew; earlier candidate, screening, classification, adjudication and report outputs were excluded from scientific input.

Direct CPU Poppler tools supplied exact PDF text and targeted source renderings. The mechanical rechecker visually confirmed the defining passages using current-run renderings and reread every candidate location directly from the supplied PDFs. Derivatives remain locators and transcription aids; the PDF page links in the cards identify the evidence authority. The [evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md), [source inventory](review_1_6_1/source_inventory.md) and [tooling record](review_1_6_1/tooling_record.md) retain engine, identity, fitness and location provenance.

## Scope, Complete Coverage, and Exclusions

The review applies the four inclusion criteria in QUALITY_CONTROL_SCOPE.md: a reproduced comparison, an in-focus quantitative/statistical relationship, an unresolved intended value or meaning after immediate context, and plausible relevance to interpretation or extraction of a named result. It covers counts and denominators, estimate/test logic, statistical method logic, and prospective versus reported statistical design. It does not conduct a broad methodology, clinical, novelty, misconduct or raw-data audit, and it proposes no preferred analysis.

| Direct source | Total pages | Reusable-backed pages | Fresh-required pages | Newly mapped pages | Status |
|---|---:|---:|---:|---:|---|
| jama_flint_2019_oi_190079.pdf | 10 | 10 | 0 | 10 | COMPLETE |
| joi190079supp1_prod.pdf | 42 | 42 | 0 | 42 | COMPLETE |
| joi190079supp2_prod.pdf | 10 | 10 | 0 | 10 | COMPLETE |
| joi190079supp3_prod.pdf | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 63 | 63 | 0 | 63 | COMPLETE |

Main mapping covered PDF pp.1–10. Disjoint support mapping covered protocol pp.1–21 plus every result-supplement page and the data-access page, and protocol pp.22–42 in a separate bounded shard. The canonical support artifact merges both parts without adding pages. All main Tables 1–5, protocol power/historical/switch tables, nine supplementary figures, reference pages, administrative pages and units without applicable results have explicit mapping records. Zero fresh-required pages denotes complete reusable extraction availability; it does not denote reuse of scientific conclusions.

Differences resolved by rounding/display precision, evident notation or terminology, immediate context, different modeled versus crude quantities, unestablished assumptions, peripheral comparisons and out-of-focus content were excluded under their recorded reason codes. Cross-document comparisons were retained when they concerned primary/key secondary results or relevant prospective analysis/endpoint rules. Baseline descriptions, individual-time-point contributor counts, pointers, site calendars and historical quantities were not promoted without the qualifying link to a result, population size or decision rule.

The [source-coverage ledger](review_1_6_1/source_coverage.md), [coverage manifest](review_1_6_1/coverage_manifest.md), [main map](review_1_6_1/extraction/main_quantitative_evidence.md), [support map](review_1_6_1/extraction/support_quantitative_evidence.md) and [auxiliary mapping/numeric audit](review_1_6_1/quality/mapping_coverage_audit.md) document complete closure. There is no source-unit, scientific-coverage or reusable-derivative coverage gap.

## Quantitative and Statistical Relationship Coverage

| Review component | Complete scope | Completion |
|---|---|---|
| Numeric relationships | 167 unique N IDs: 133 mapper keys plus 34 explicit table-row expansions | 167/167 accounted for; table expansions add no source pages |
| Statistical/design inventory | 88 unique S IDs: 40 main, 25 initial-support and 23 later-protocol relationships | 88/88 inventoried |
| Statistical pass 1 | Every S relationship, including nonsignificant, auxiliary, historical and operational records | 88/88 PASS_1_COMPLETE |
| Statistical pass 2 | Every S relationship after ledger, screening and source recheck; both stable candidates reconciled | 88/88 PASS_2_COMPLETE |
| Mechanical candidate recheck | C001 and C002; 11 location instances on nine unique PDF pages | 2/2 reproduced; zero classification/location/transcription changes |
| Final audit | Both candidates, all six screening decisions, all 90 checker-exclusion rows, coverage and execution | 2 CONFIRMED; 0 QUESTIONED; no new candidate |

The [numeric inventory](review_1_6_1/relationships/numeric_relationship_inventory.md) preserves counts, denominators, totals, available-case summaries and effect-measure identities. The [statistical inventory](review_1_6_1/statistics/relationship_inventory.md) records each relationship and both completion states. [Pass 1](review_1_6_1/checkers/statistical_pass_1.md) used runtime `01a128e0-66b3-7712-a4ca-02deb3251b1f`; [pass 2](review_1_6_1/checkers/statistical_pass_2.md) used the distinct fresh runtime `01a128ec-6356-7b23-be7b-9115db681a2b`. Both used `gpt-6.1-sol` with high reasoning effort.

Checks covered point/interval containment and order, contrast direction, null consistency, test/interval attribution, declared multiplicity and sidedness, analysis populations, censoring, missingness, nonlinear models, pattern mixtures, power assumptions and prospective decision rules. Approximate test calculations remained diagnostics when exact variance/test algorithms were unavailable. Nominal confidence intervals were not equated with Holm-adjusted P values. Model-based slopes were not treated as crude termination changes, and simulation power was not replaced with an assumed elementary formula. Table 4 describes within-arm baseline-to-termination changes with explicit missing-data context; exact participant-pair membership is not supplied.

## Inclusion Screening Summary

Every initial checker finding received exactly one independent decision in the [screening log](review_1_6_1/screening/inclusion_screen.md). Inclusion required all four criteria above, with no expected number of candidates. Repeated findings were consolidated into one issue while retaining all affected locations.

| Screening decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 2 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 2 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 1 |
| Total | Six independently screened findings | 6 |

Included findings are F-XS-001 → C001 and F-XS-002 → C002. Statistical findings F-ST1-001 and F-ST1-002 corroborate these same issues and were screened as duplicates; they are retained as checker provenance, not added to the cards' included Finding IDs. F-ST1-003 depends on an unestablished medication-based classification algorithm; F-ST1-004 concerns HOMA's designation within auxiliary glycemic measurements without an established trial-primary/key-secondary reporting conflict. Neither receives a candidate card. Pass 2 emitted zero new findings, so no additional inclusion-screen stage was required. Auditors identified no screening reversal or additional qualifying finding.

Checker self-screening is a separate accounting layer: **24 numeric + 31 cross-source + 17 pass-1 + 18 pass-2 = 90 lane-specific excluded-observation patterns**. These may overlap in content across lanes; they are neither 90 unique issues nor additional rows in the six-finding screen.

| Checker-exclusion reason code | Consolidated lane-specific patterns |
|---|---:|
| CONTEXT_RESOLVES | 34 |
| CONDITIONAL_OR_UNREPORTED | 23 |
| MODEL_VERSUS_CRUDE | 6 |
| ROUNDING_OR_DISPLAY_PRECISION | 5 |
| NOTATION_OR_TYPOGRAPHY | 5 |
| TERMINOLOGY_OR_WORDING | 2 |
| NOT_REPRODUCED | 4 |
| PERIPHERAL_COMPARISON | 10 |
| OUT_OF_FOCUS | 1 |
| Total | 90 |

The [final quality audit](review_1_6_1/quality/evidence_quality_audit.md) independently reviewed both included and screened-out directions and every checker exclusion. Its reason-code counts reconcile to the complete checker tables.

## Review-Domain Summary

`statistical_results` covers count, estimate, interval, test and method logic in REPORT material. `report_internal_inconsistency` covers conflicting attribution of a reported number to an outcome, population, time or comparison within/between REPORT documents. `protocol_report` covers prospective PLAN versus REPORT statistical-design/analysis differences. `plan_material` covers relevant statistical-design inconsistencies solely within PLAN material. Domains prefill human review and do not adjudicate the candidates.

| Review domain | Candidates |
|---|---:|
| statistical_results | 0 |
| report_internal_inconsistency | 0 |
| protocol_report | 2 |
| plan_material | 0 |
| Total | 2 |

| Primary relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | PLAN versus REPORT | 2 |
| P_P | PLAN versus PLAN | 0 |
| S_C | Different REPORT documents | 0 |
| S_W | Within one REPORT document | 0 |
| Total | | 2 |

| Evidence state | Candidates |
|---|---:|
| reproduced | 2 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 2 |

Both candidates involve `P_R` alone. Supporting report locations agree rather than forming additional relationships. Thus the precedence rule P_R > P_P > S_C > S_W requires no mixed-relationship selection. Inclusion audits total two `CONFIRMED` and zero `QUESTIONED`.

## Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Additional HDRS change condition in primary relapse definition | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Prospective metabolic observation exclusion versus reported sensitivity hierarchy | protocol_report | P_R | reproduced | CONFIRMED |

The complete stable set is {C001, C002}; both cards follow in stable-ID order.

## Candidate Evidence Cards

## C001 — Additional HDRS change condition in the primary relapse definition

**Pending Human Adjudication**

**Candidate statement:** The planned HDRS component of the primary relapse endpoint requires a score of at least 18 and an additional five-point rise from randomized baseline; the reported component specifies the absolute score threshold alone. Allowed near-remission entry scores make these definitions nonequivalent. This is a candidate reporting issue in endpoint specification; it does not establish a discrepancy in the reported event totals.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p.12 vs REPORT main article p.4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

Checker provenance: Cross-source F-XS-001 was independently corroborated by F-ST1-001, which received SCREENED_OUT / DUPLICATE_OF_INCLUDED and maps to C001. Its additional eligibility and primary-result locations remain included below.

**Classification rationale:** A positive prospective primary-endpoint specification in PLAN is compared with the reported endpoint definition in REPORT. Supporting eligibility/result passages establish relevance and do not add independent relationships. P_R implies protocol_report.

**Classification ambiguity:** No content-role ambiguity. The package does not identify whether the shorter reported definition abbreviates an operationally retained condition or reflects an amendment.

**Exact source locations:**

- PLAN [joi190079supp1_prod.pdf — PDF p.12, section 3.9.8, printed lines 553–573, especially 556–557](<../joi190079supp1_prod.pdf#page=12>): prospective score-based relapse component.
- PLAN [joi190079supp1_prod.pdf — PDF p.7, section 3.9.1, remission/near-remission eligibility](<../joi190079supp1_prod.pdf#page=7>): permitted randomized-entry score range.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.4, Primary Outcome: Relapse](<../jama_flint_2019_oi_190079.pdf#page=4>): corresponding reported component.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.3, near-remission and randomization eligibility beneath Figure 1](<../jama_flint_2019_oi_190079.pdf#page=3>): reported eligibility and randomized/event counts.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.1, abstract primary result](<../jama_flint_2019_oi_190079.pdf#page=1>): headline result attached to the endpoint.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.6, Primary Outcome paragraph](<../jama_flint_2019_oi_190079.pdf#page=6>): event totals and multivariable Cox result.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.7, primary-result continuation and Table 3](<../jama_flint_2019_oi_190079.pdf#page=7>): continued analysis and overlapping relapse-event categories.

**Source evidence:** Protocol p.12 joins HAM-D ≥18 to a “mean absolute increase of 5 points on at least one visit relative to entry into the RCT.” The preferred one-week duration is separately discretionary. Article p.4 requires at least one composite component and states its score component as “17-item HDRS score of 18 or higher,” without the baseline-change conjunction. Protocol p.7 and article p.3 permit near-remission entry with scores 11–15. HAM-D/HDRS identify the same 17-item Hamilton depression instrument; the abbreviation difference is not the issue.

**Reported-versus-comparator:** REPORT: absolute score ≥18. PLAN: absolute score ≥18 together with an additional five-point randomized-baseline change condition. The comparison concerns the same primary 36-week relapse endpoint.

**Reasoning procedure:** Compare both positive definitions; use the supplied eligible entry-score range to ask whether the extra condition is necessarily redundant. Keep the possible-score demonstration separate from actual observed events. Review the alternative composite components and overlapping Table 3 categories; these do not disclose the algorithm used for score-only events. Match the primary result across the abstract and narrative rather than treating their agreeing numbers as a separate inconsistency.

**Calculation:** An illustrative eligible entry score of 15 followed by 18 yields a three-point increase; entry 14 followed by 18 yields four points. Both meet the printed absolute threshold, but neither meets a five-point increase under the ordinary baseline-to-visit reading. These are logical possible-score examples, not supplied participant observations. Integer thresholds cannot be reconciled by rounding. As a matched-result check, 13/64 × 100 = 20.3125% and 34/62 × 100 ≈ 54.8387%, consistent with displayed 20.3% and 54.8%. No revised event count or HR is calculated.

**Affected result or extracted value:** The operational score-based component of the primary composite-relapse definition attached to **13/64 versus 34/62 events** and **adjusted HR 0.25 (95% CI 0.13–0.48), P<.001**. These printed numbers agree across the affected report locations; the unresolved extracted element is the endpoint criterion attached to them.

**Why context does not resolve it:** The article presents its list as the requirements for declaring relapse without identifying the additional change requirement as retained or revised. Near-remission eligibility prevents universal redundancy of that conjunction. The plan's discretionary persistence duration does not expressly waive the separate five-point condition. Aggregate baseline summaries and overlapping event categories cannot identify the final operational score-based algorithm.

**Alternative source-grounded interpretations:** The article may abbreviate an algorithm that retained the five-point condition, or the score component may have been revised to the absolute threshold alone. Other composite components may independently qualify the same events, or all actual score-based events may satisfy both definitions. The phrase “mean absolute increase” lacks a further operational definition in the compared passage. Participant-level baseline/event scores, final endpoint instructions and any relevant amendment are not supplied; their absence from this package does not establish that an amendment did not exist. No event reclassification, count change or conclusion change is inferred.

**Mechanical evidence recheck:** All seven cited location instances were found and source/comparator text matched. Direct Poppler layout extraction reread the nine unique candidate pages; protocol p.12 and main p.4 defining passages were additionally visually confirmed on current-run source renderings. The primary-endpoint comparison rule applies and the logical nonequivalence reproduces; necessary statement/eligibility/result inputs are available. Supporting percentages reconcile within their half-unit display intervals, while exact integer decision criteria cannot reconcile through display precision. Document roles, P_R relationship and protocol_report domain were confirmed without correction. The determining `reproduced` fact is the difference between positive printed endpoint specifications, not an observed event difference. Full records: [mechanical recheck](review_1_6_1/verification/evidence_recheck.md) and [final quality audit](review_1_6_1/quality/evidence_quality_audit.md). Renderings `cross-plan-p12.png` and `cross-main-p04.png` are Poppler provenance aids below review_1_6_1/preprocessing; the linked supplied PDFs remain authority.

**Potential downstream evidence impact:** If confirmed by human review, an extractor could attach the ≥18-only definition or the additional baseline-change condition to the same primary result when describing eligibility, endpoint comparability or a meta-analysis outcome. The package does not establish that either interpretation has propagated, altered an estimate or changed a conclusion.

**Human verification steps:**

1. Read the full protocol conjunction and the reported composite definition at the linked pages.
2. Identify the final approved score-based relapse algorithm, the operational meaning of the five-point wording and any amendment.
3. Establish whether that condition was retained for event ascertainment; use event-assessment records and randomized-baseline/event scores to examine numerical consequences only if those records become available.
4. Answer: Was the five-point condition retained or prospectively revised before generating the reported primary events and HR?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned metabolic observation exclusion appears as a post hoc sensitivity

**Pending Human Adjudication**

**Candidate statement:** The prospective H2 specification excludes pertinent metabolic observations after new or changed hyperlipidemia treatment. The report describes this operation as a post hoc sensitivity beside analyses including all participants, leaving the relation of the headline estimates to the prospective rule unclear. This candidate concerns the positive planned-rule versus reported analysis-hierarchy comparison; participant inclusion alone does not identify the headline observation set.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p.14 vs REPORT main article pp.5,7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

Checker provenance: Cross-source F-XS-002 was independently corroborated by F-ST1-002, which received SCREENED_OUT / DUPLICATE_OF_INCLUDED and maps to C002. All its affected locations are retained. The source-confirmed recheck bounds any initial inference that all post-change observations entered the headline models.

**Classification rationale:** A prospective observation-inclusion specification in PLAN is compared with the reported main-versus-sensitivity implementation in REPORT for H2 key secondary outcomes. Multiple report passages form one plan/report issue; no distinct report-internal conflict is asserted. P_R implies protocol_report.

**Classification ambiguity:** No content-role ambiguity. A later supplied-source amendment or exact sensitivity coefficients are unavailable; the issue does not establish which individual observations changed an estimate.

**Exact source locations:**

- PLAN [joi190079supp1_prod.pdf — PDF p.14, H2, printed lines 660–679, especially 673–675](<../joi190079supp1_prod.pdf#page=14>): prospective model and post-hyperlipidemia-treatment observation rule.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.5, Statistical Analyses continuation](<../jama_flint_2019_oi_190079.pdf#page=5>): post hoc sensitivity exclusion and triglyceride pattern-mixture reporting.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.7, Secondary Outcomes and medication-change sensitivity paragraph](<../jama_flint_2019_oi_190079.pdf#page=7>): headline coefficients, medication-change counts and qualitative sensitivity comparison.
- REPORT [jama_flint_2019_oi_190079.pdf — PDF p.1, abstract cholesterol/triglyceride results](<../jama_flint_2019_oi_190079.pdf#page=1>): matching headline key secondary estimates.

**Source evidence:** Protocol p.14 specifies H2 mixed models for weight, total cholesterol and triglycerides. For new/changed hyperlipidemia treatment, pertinent metabolic data thereafter “will be excluded from the mixed model,” while measurement continues for safety reporting. Article p.5 describes pertinent post-statin/hypoglycemic-change exclusion as post hoc sensitivity; it also explicitly states that triglyceride estimates are pattern-mixture averaged. Article p.7 reports 12 statin starts/changes, six per arm, and three hypoglycemic starts/changes, two versus one. It describes sensitivity results as qualitatively similar to analyses “including all participants.” The hypoglycemic extension is context; the registered prospective-rule comparison concerns hyperlipidemia treatment.

**Reported-versus-comparator:** PLAN places relevant post-hyperlipidemia-treatment observation exclusion in the H2 model specification. REPORT describes that operation in a separate post hoc sensitivity and compares it with all-participant analyses. The supplied descriptions do not fully connect the headline estimates, observation-inclusion rule and prospective analysis hierarchy. This is more than a comparison of the phrase post hoc alone.

**Reasoning procedure:** Match H2 outcomes and the positive exclusion instruction to the report's corresponding sensitivity and abstract/narrative coefficients. Verify that treatment changes occurred. Separate the inclusion of a participant from inclusion of each of that participant's observations: an individual can remain represented by earlier measurements after later observation censoring. Retain explicit triglyceride pattern-mixture averaging rather than treating its coefficient as a single ordinary mixed-model fit. Do not infer medication-based participant reassignment or substitute a preferred data-handling procedure.

**Calculation:** Six plus six equals **12** reported statin starts/changes; the contextual hypoglycemic count is two plus one equals **3**. These establish reported medication changes, not the number of analyte-specific post-change measurements. Abstract and narrative cholesterol 0.29 (0.13–0.45) and triglyceride −0.153 (−0.306 to 0.004) agree at their printed precision. No exact medication-censored coefficient, interval or P value is supplied for numerical recomputation. Rounding cannot reconcile the positive analysis-hierarchy descriptions, and qualitative similarity does not establish equality of exact outputs.

**Affected result or extracted value:** The relationship of the printed **total-cholesterol daily coefficient 0.29 mg/dL (95% CI 0.13–0.45; adjusted P=.003)** and **pattern-mixture-averaged triglyceride coefficient −0.153 mg/dL (95% CI −0.306 to 0.004; adjusted P=.25)** to the prospectively specified medication-censored H2 analysis. The coefficients themselves are matched between report locations; no replacement estimate is available.

**Why context does not resolve it:** The report identifies an exclusion sensitivity and qualitative agreement, but provides neither the exact medication-censored outputs nor the final prospective specification that reconciles its principal/sensitivity ordering with the supplied H2 instruction. “Including all participants” does not prove that every later observation was included. The supplied context therefore leaves the actual headline observation rule and its relationship to the prospective analysis unresolved, including how medication exclusion interacts with triglyceride pattern-mixture averaging.

**Alternative source-grounded interpretations:** A prospective amendment may have revised the principal analysis; the planned operation may have been implemented only as sensitivity; or the article may label a procedure post hoc although it was prospectively specified. Headline models may retain some or all post-change observations, or all participants may remain represented after appropriate later observation censoring. Exact medication dates, analyte-specific observation sets, final analysis instructions/amendments, censored coefficients and pattern-mixture components/weights are not supplied. None of these alternatives is established. No absence of an amendment, complete participant removal, uncensored headline dataset, changed coefficient/significance or conclusion change is asserted.

**Mechanical evidence recheck:** All four location instances were found; complete prospective and report analysis passages and both headline results matched. Direct source extraction and visual confirmation of protocol p.14/main p.5 reproduce the positive prospective-rule versus sensitivity-description comparison. All necessary inputs for that bounded statement comparison are available; observation-level records and exact sensitivity outputs needed for numerical consequences are unavailable. Medication counts are exact; matching coefficient/interval displays reconcile within half-unit precision. Roles, P_R and protocol_report were confirmed without correction. `reproduced` applies to the analysis-hierarchy comparison, not proof of which post-change measurements entered a fitted model. Full records: [mechanical recheck](review_1_6_1/verification/evidence_recheck.md), [statistical pass 2](review_1_6_1/checkers/statistical_pass_2.md) and [final quality audit](review_1_6_1/quality/evidence_quality_audit.md). Renderings `cross-plan-p14.png` and `cross-main-p05.png` are CPU Poppler provenance aids below review_1_6_1/preprocessing; supplied PDF pages remain authority.

**Potential downstream evidence impact:** If confirmed, an extractor could annotate the headline coefficients as implementing the prospective medication-censored H2 rule or as a distinct analysis, and could seek exact censored estimates when that prespecified comparison is required. Qualitative similarity alone cannot supply those exact coefficients. No actual downstream propagation or changed evidence-synthesis conclusion is established.

**Human verification steps:**

1. Compare the complete H2 observation-exclusion instruction with the article's sensitivity description and qualitative result.
2. Identify the final approved H2 specification and any amendment that defines the principal-versus-sensitivity hierarchy.
3. Identify analyte-specific observations used in each headline model, medication-change dates and exclusions; separate observation censoring from participant removal.
4. Obtain exact cholesterol and triglyceride sensitivity outputs, including pattern-mixture components, weights and averaging/censoring rules, without assuming that their coefficients differ.
5. Answer: Which observation-inclusion rule generated the headline H2 estimates, and how does the final prospective specification reconcile it with the reported hierarchy?

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

An evidence extractor ordinarily copies an estimate together with its endpoint definition, population, time window and analysis specification. An unresolved endpoint component can affect how otherwise agreeing results are grouped or described. An unresolved principal/sensitivity hierarchy can affect which analysis is annotated as prospective and whether a requested sensitivity estimate is numerically available. A systematic review, meta-analysis or guideline may therefore need operational clarification before attaching those descriptors to the supplied values.

These are potential evidence-use considerations. The supplied package establishes neither propagation to another source nor a changed pooled estimate, clinical recommendation or paper conclusion. No numerical replacement, preferred method or human action is assigned by this report.

## Limitations and Missing Definitions

All supplied units and registered relationships have completed coverage; remaining limits concern evidence needed to settle operational interpretation or numerical consequences. Full details are retained in [limitations.md](review_1_6_1/limitations.md).

- C001: the final operational score-based relapse algorithm, further meaning of “mean absolute increase,” any relevant approved amendment, participant randomized-baseline/event scores, event-assessment forms and score-only versus other qualifying composite components are not supplied. Event/censoring records and complete Cox inputs are unavailable for any numerical-consequence analysis.
- C002: final approved H2 observation instructions/amendments, medication-change dates, analyte-specific post-change measurements, model observation sets, exact medication-censored coefficients/intervals/P values and triglyceride pattern-mixture components/weights are not supplied. All-participant wording cannot resolve the observation sets.
- Other relationships: full-precision test/variance identities, complete Holm family/rank inputs, exact interval algorithms, NNT survival/formula inputs, Poisson link/backtransformation, exact Table 4 participant-pair membership/covariance, and complete simulation generation/attrition/covariance recipes are unavailable. Their absence was treated as a bounded limitation, not an assumed contradiction.
- Figures: all nine result figures were visually mapped, but exact unprinted coordinates, band definitions and contributor counts cannot be recovered as exact source values. Curves support only the precision actually supplied.
- Scope: only supplied package evidence was used. No participant-level dataset, separate later SAP/amendment or external literature was inspected. The operational data-access statement describes possible access and does not itself supply analysis data.

No tool limitation, fallback installation failure, reusable-derivative coverage gap or uninspected source unit remains. Direct CPU tools were available; no new OCR, Office conversion, global installation or GPU invocation was needed. Initial derivative transcription/wording repairs described by the auxiliary audit affect current-run extraction records only and do not add a stable candidate or change a supplied source.

## Human Adjudication Checklist

1. Read each complete linked source passage and retain its content role; use the supplied PDF as authority.
2. Confirm that the candidate remains reproduced, in focus, unresolved by immediate context and relevant to the named extracted result.
3. For C001, establish the final endpoint algorithm before considering any participant reclassification or numerical consequence.
4. For C002, establish the final observation-inclusion/hierarchy rule and exact censored outputs; preserve the participant/observation distinction and explicit triglyceride averaging.
5. Distinguish a reproduced specification comparison from proof of changed counts, coefficients or conclusions.
6. Complete each card's validity, importance, action, initials and notes fields during human adjudication. All five remain `__` in this report.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

Workflow 1.6.1 ran within this paper package using English artifacts and local CPU tooling. [Routing preflight](review_1_6_1/routing_preflight.md) records PASS, `gpt-6.1-sol`/high coordinator inference, `INTERACTIVE_CLI`, `CURRENT_SESSION` and all ten named fixed-model presets. Mandatory stages use fresh distinct specialist runtimes. No provider configuration or credentials were introduced.

The [before-source hash record](review_1_6_1/source_hashes_before.sha256) and [before-reuse hash record](review_1_6_1/reused_artifact_hashes_before.sha256) preserve four supplied sources and 187 reused assets. Final recomputation after complete Markdown assembly reproduced **4/4 source hashes and 187/187 reused-asset hashes**. The [after-source record](review_1_6_1/source_hashes_after.sha256) and [after-reuse record](review_1_6_1/reused_artifact_hashes_after.sha256) are byte-identical to their respective before records. Standalone HTML and review_1_6_1/review_validation.json provide the rendering and mechanical closure records; all source and reused evidence remains unchanged.

| Direct source | SHA-256 |
|---|---|
| jama_flint_2019_oi_190079.pdf | f3480ac424a06c1a7747c03a4e9523b1b391ed918562f402c84ad516f85cf05f |
| joi190079supp1_prod.pdf | 68aaf0377b631a63a25438ed4d101acb8f19a75ce9c5a9243ab5d75718a06b8f |
| joi190079supp2_prod.pdf | 648b40127a28c8b919ee94918cd879a6cd8001810a4d5db61394d6fa0bae6d53 |
| joi190079supp3_prod.pdf | d335f3d8b8ca330abc569a368e62e561f588309d621b89a9af1dd64ab6c7e199 |

Direct engines include Poppler 26.01.0 for information/text/rendering; tesseract 5.5.0 and Pandoc 3.7.0.2 were available. The fallback environment was NOT_NEEDED and NOT_CREATED. Engine/source/page provenance for every new rendering is retained by its producing checker/screener artifact. No new source derivative is produced by report generation. Source preservation and source-page links remain separately testable from scientific adjudication.

### Agent execution

The [execution manifest](review_1_6_1/agent_execution_manifest.md) lists **14 actual agents once each**: the coordinator, 11 mandatory specialists, one additional support mapper and one auxiliary mapping/numeric auditor. All use fixed model `gpt-6.1-sol`; role effort and primary durable artifact are reproduced below. Auxiliary scopes bound context without selecting findings or replacing mandatory stages.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128d9-a47a-7bc0-923d-93b713cb413d | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128da-514a-7621-aecc-501c34ed647e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128dc-926b-7a82-afaf-ecf5979714d5 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128dc-b0b1-7732-a436-11caded5ed10 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_part_2 | 01a128dc-c8fe-7331-af32-86f9549a95bd | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_part_2.md |
| numeric_consistency_reviewer | 01a128e0-2fbf-77f3-984e-57bcaa473d9b | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a128e0-4895-7462-a9b3-56b2a6829db4 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e0-66b3-7712-a4ca-02deb3251b1f | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128e6-6a07-77c2-b638-35eb9cc1bf9d | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128e9-2d33-7973-9e79-24863cbc6ab4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128ec-6356-7b23-be7b-9115db681a2b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor_mapping_coverage | 01a128ed-a118-7e10-acc8-30a8588fcb41 | gpt-6.1-sol | high | FRESH_SPAWN | quality/mapping_coverage_audit.md |
| quality_control_auditor | 01a128f1-d646-7e31-a992-ec2915bbbead | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a128f5-b60f-7283-aaa7-c589054ee727 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

The following exact fields reproduce the finalized run-state record. The finish time was captured after full Markdown assembly and refreshed for the coordinator mechanical record-format repair. Final elapsed, target-status and exceedance values agree with run_state.md; local rendering and mechanical validation are outside the observed review window.

- **Target basis:** Four native-text PDFs contain 63 unique pages with reusable aids for all 63 and zero extraction gaps. The 42-page protocol requires two bounded support scopes; nine graphical result pages have reusable rendering and OCR aids. No Office conversion or fresh OCR is required. Parallel mapping and three initial checker lanes are followed by screening, direct-source recheck, distinct statistical pass 2, audit and complete report assembly. A 25-40 minute planning range reflects these bounded review waves and figure confirmation, rather than source-page count alone.
- **Total source units:** 63
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:45:51Z
- **Finished UTC:** 2026-10-11T03:22:18Z
- **Observed elapsed minutes:** 36.45
- **Target status:** MET_TARGET
- **Exceedance causes:** None
