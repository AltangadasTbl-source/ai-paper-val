# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication.** All 14 candidates remain Pending Human Adjudication. Evidence-state and inclusion-audit fields describe mechanical reproduction and threshold screening, respectively; they are not human adjudications.

## Executive Quality-Control Summary

The complete supplied package yielded **14 stable candidate reporting issues**, consolidated from **25 included findings**. Independent screening considered 28 findings and screened out three. All 14 inclusion audits are CONFIRMED; 13 evidence states are reproduced and one is reproduced_after_transcription_correction. The review covers all 91 physical PDF pages, 104 numeric relationship groups, and 93 statistical relationship groups in two fresh, distinct statistical passes.

The candidates concern continuation population policy and model-weight mapping, allocation denominators, primary credible limits and effect direction, a prespecified posterior criterion, planned robustness reporting, secondary result denominators and quantity identity, design-distribution summaries, prior-interval mapping, repeated decimal-scale readings, a distinct six-month credible interval, and the dose attached to a design input. The cards preserve the supplied readings and bounded alternatives; they assign no final numerical correction.

## Package and Reused-Evidence Provenance

The paper is *Smoking Cessation After Initial Treatment Failure With Varenicline or Nicotine Replacement: A Randomized Clinical Trial*. The source roles below were assigned by content. Physical PDF pages include covers, contents and references. No Office, workbook, CSV or other direct source was supplied.

| Source | Actual filename and source link | Role | Physical pages |
|---|---|---|---:|
| DOC-001 | [jama_cinciripini_2024_oi_240036_1716416465.98349.pdf](<../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1>) | REPORT: published article/results | 10 |
| DOC-002 | [joi240036supp1_prod_1716416466.00349.pdf](<../joi240036supp1_prod_1716416466.00349.pdf#page=1>) | PLAN: Protocol 2014-0213, August 23, 2023 | 45 |
| DOC-003 | [joi240036supp2_prod_1716416466.01349.pdf](<../joi240036supp2_prod_1716416466.01349.pdf#page=1>) | REPORT: supplementary methods/results | 36 |

The review reused 297 individually hashed assets: 241 text files, 47 rendered images and nine metadata/maps. Fitness counts are USABLE 91, DUPLICATE 150, PARTIAL 53, STALE 3 and UNREADABLE 0. Each reusable text file matched its exact current PDF page/range after whitespace-only normalization, retaining the order of all non-whitespace characters. Duplicate derivatives do not add source units. Historical main/supplement hashes and absolute paths were stale; current direct identity checks superseded them. Historical images had incomplete renderer provenance and served as locators, with relevant graphical content confirmed against current sources.

The [source inventory](review_1_6_2/source_inventory.md), [asset inventory](review_1_6_2/evidence_asset_inventory.md), and [reused-asset hash manifest](review_1_6_2/reused_artifact_hashes_before.sha256) retain exact paths and methods. Existing scientific candidate/report records did not define discovery or coverage.

## Scope, Complete Coverage, and Exclusions

The review addressed counts and denominators, estimate/test logic, statistical method logic, and planned-versus-reported statistical design under QUALITY_CONTROL_SCOPE.md. All supplied source units were mapped anew using usable reusable text and targeted direct-source checks. Zero units initially required fresh extraction because every page had source-matched reusable text; current-source extraction and rendering still confirmed focal content.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_cinciripini_2024_oi_240036_1716416465.98349.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | joi240036supp1_prod_1716416466.00349.pdf | PDF_PAGE | 45 | 45 | 0 | 45 | COMPLETE |
| DOC-003 | joi240036supp2_prod_1716416466.01349.pdf | PDF_PAGE | 36 | 36 | 0 | 36 | COMPLETE |

Every source closes total = reusable + fresh-required and mapped = total. The [coverage manifest](review_1_6_2/coverage_manifest.md), [main map](review_1_6_2/extraction/main_quantitative_evidence.md), [support map](review_1_6_2/extraction/support_quantitative_evidence.md), and [plan shard](review_1_6_2/extraction/parts/plan_quantitative_evidence.md) document the complete disjoint unit assignments.

The scope excludes broad methodology, clinical, novelty, misconduct and raw-data assessment. Peripheral baseline/administrative comparisons, immediately resolvable wording or symbols, unestablished conditional analyses, model-versus-crude differences and display-precision differences were screened under the normative rules. Printed-copy comparisons use half-unit intervals and the remaining relative gap; gaps at most 0.05 are screened out. Bayesian benefit probabilities were kept distinct from frequentist P values.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains 104 N groups, preserving all 96 mapper numeric groups and eight statistical-display cross-references. The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains 93 S groups; every group has explicit PASS_1_COMPLETE and PASS_2_COMPLETE records. Grouping preserves every displayed component rather than sampling rows. Coverage includes baseline and flow, every adverse-event and compliance display, seven NNT relationships, ten beta-design boxes, all simulation effect/power rows, all primary and secondary contrasts, and six post hoc GEE pathways.

[Statistical pass 1](review_1_6_2/checkers/statistical_pass_1.md) used root/statistical_pass1, gpt-6.1-sol/high, and emitted ten findings plus nine excluded observations. [Statistical pass 2](review_1_6_2/checkers/statistical_pass_2.md) used the distinct fresh root/statistical_pass2, gpt-6.1-sol/high, after the ledger, screen and recheck existed. It revisited all 93 groups, all 14 candidates, all 28 screened findings and all 36 preceding exclusions, emitted no new finding, and recorded one additional terminology/wording exclusion. A second inclusion screener was therefore not applicable.

The [quality audit](review_1_6_2/quality/evidence_quality_audit.md) examined all 37 excluded observations and screening decisions in both directions. NUM-E10/N058’s population-size observation is already represented by C008; its original peripheral rationale was superseded without introducing a duplicate stable issue. No new distinct qualifying finding or screening-decision change resulted. Exact beta/normal calculations concern explicitly defined distributions; absent model code, covariance, posterior draws and simulation realizations bound fitted-result reproduction. No stated noninferiority/equivalence margin or current-trial efficacy stopping boundary was present; future adaptive arm dropping was not treated as a current stopping rule.

## Inclusion Screening Summary

A finding qualifies only when reproduced and supported either by a Route A always-register category or by all three Route B criteria: in focus, not immediately resolved by context, and bearing on a named result’s interpretation or extraction. Independent source rereading covered every finding. Counts below reconcile to the single [screening log](review_1_6_2/screening/inclusion_screen.md).

| Screening stage | Findings screened | INCLUDE | SCREENED_OUT | Consolidated stable candidates |
|---|---:|---:|---:|---:|
| Initial | 28 | 25 | 3 | 14 |
| Pass 2 new findings | 0 | 0 | 0 | 0 additional |
| Audit new findings/decision changes | 0 | 0 | 0 | 0 additional |
| Total | 28 | 25 | 3 | 14 |

| Decision | Reason code | Count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 25 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 1 |
| SCREENED_OUT | OUT_OF_FOCUS | 1 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 1 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |

The three screened findings concern a peripheral cross-location employment descriptor, eligibility wording without a demonstrated statistical population change, and a symbolic predictor expression resolved by the adjacent coding/master equation. Checker exclusion observations are separately audited and are not additional finding rows. Multiple INCLUDE findings can map to one consolidated issue; all 25 finding IDs remain attached to their canonical candidates.

## Review-Domain Summary

| Review domain | Definition | Candidate count |
|---|---|---:|
| statistical_results | REPORT counts, estimates, intervals, tests and statistical methods | 9 |
| report_internal_inconsistency | REPORT inconsistency identifying which outcome, population, time point or comparison a number represents | 1 |
| protocol_report | REPORT versus PLAN statistical design or analysis element | 3 |
| plan_material | PLAN-internal statistical design element relied on by the analysis | 1 |
| Total | | 14 |

| Primary relationship type | Definition | Candidate count |
|---|---|---:|
| S_C | Different REPORT documents | 6 |
| S_W | Within one REPORT document | 4 |
| P_R | REPORT versus PLAN | 3 |
| P_P | Within PLAN material | 1 |
| Total | | 14 |

| Evidence state | Candidate count |
|---|---:|
| reproduced | 13 |
| reproduced_after_transcription_correction | 1 |
| not_reproduced | 0 |
| Total | 14 |

All 14 inclusion audits are CONFIRMED; zero are QUESTIONED. Primary relationships use precedence P_R > P_P > S_C > S_W. Additional relationships are preserved in each card; corroborating documents do not create a conflicting relationship.

## Candidate Index

| Stable ID and issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| [C001 — Planned and reported primary continuation populations](#c001) | protocol_report | P_R | reproduced | CONFIRMED |
| [C002 — Weight mapping for 75 assigned continuation participants](#c002) | statistical_results | S_C | reproduced | CONFIRMED |
| [C003 — Mixed denominators in abstract allocation percentages](#c003) | statistical_results | S_W | reproduced | CONFIRMED |
| [C004 — Primary CNRT lower credible limit differs across locations](#c004) | statistical_results | S_C | reproduced | CONFIRMED |
| [C005 — Primary varenicline-to-CNRT direction, sign, and attribution](#c005) | statistical_results | S_C | reproduced | CONFIRMED |
| [C006 — Reported prespecified posterior criterion differs from plan](#c006) | protocol_report | P_R | reproduced | CONFIRMED |
| [C007 — Planned primary-model robustness analyses absent from reports](#c007) | protocol_report | P_R | reproduced | CONFIRMED |
| [C008 — EOT plus 30-day varenicline continuation denominator](#c008) | statistical_results | S_C | reproduced | CONFIRMED |
| [C009 — Six-month CNRT summary probabilities and risk difference](#c009) | statistical_results | S_C | reproduced | CONFIRMED |
| [C010 — Week-6 design intervals and generating beta distributions](#c010) | plan_material | P_P | reproduced | CONFIRMED |
| [C011 — Revised normal prior variance and printed odds interval](#c011) | statistical_results | S_W | reproduced | CONFIRMED |
| [C012 — Repeated EOT plus 30-day decimal-scale discrepancies](#c012) | statistical_results | S_W | reproduced | CONFIRMED |
| [C013 — Six-month responder credible limits differ across locations](#c013) | statistical_results | S_W | reproduced | CONFIRMED |
| [C014 — Augmented-CNRT dose attached to the primary-design input](#c014) | report_internal_inconsistency | S_C | reproduced_after_transcription_correction | CONFIRMED |

## Candidate Evidence Cards

Abbreviations: CNRT, combination nicotine replacement therapy; VAR, varenicline; EOT, end of treatment; RD/ARD, risk difference/absolute risk difference; CrI, credible interval; IPW, inverse-probability weighting. Every card below is Pending Human Adjudication. Direct observations are distinguished from possible production mechanisms and unobserved fitted-result consequences.

<a id="c001"></a>

## C001 — Planned and reported primary continuation populations

Pending Human Adjudication.

**Candidate statement:** The planned second-stage continuation reference populations are defined through rerandomization, while the reported primary populations additionally include 40 CNRT and 35 varenicline nonreturners assigned to continuation. The supplied plan does not explicitly specify that treatment-assignment policy.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN prospective second-stage assignment/analysis vs REPORT assigned-continuation primary populations

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-009

**Qualifying route:** Route A, category 5

**Classification rationale:** Retain PLAN/REPORT, primary/all P_R, protocol_report: the compared issue is prospective versus actual primary-analysis membership, not a conflict between the mutually consistent report counts.

**Classification ambiguity:** Possible additional amendment or interpretation of the broad intention-to-treat policy; no content-role ambiguity.

**Exact source locations:**

- [p.7, Participants](../joi240036supp1_prod_1716416466.00349.pdf#page=7)
- [p.24, final pharmacotherapy paragraph](../joi240036supp1_prod_1716416466.00349.pdf#page=24)
- [p.25, first paragraph](../joi240036supp1_prod_1716416466.00349.pdf#page=25)
- [p.28, general strategy and coding/model](../joi240036supp1_prod_1716416466.00349.pdf#page=28)
- [p.29, Aims 2–3](../joi240036supp1_prod_1716416466.00349.pdf#page=29)
- [p.30, continuing Aim 3 contrasts](../joi240036supp1_prod_1716416466.00349.pdf#page=30)
- [main p.1, both Results paragraphs](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)
- [Main p.4, Results/flow prose](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)
- [Main p.6, Figure 2 and footnote c](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6)
- [Main p.8, first limitation](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8)
- [supplement p.6, phase-II weighting/coding](../joi240036supp2_prod_1716416466.01349.pdf#page=6)

**Source evidence:**

Location found; source value/text matched: PLAN [p.7, Participants](../joi240036supp1_prod_1716416466.00349.pdf#page=7) specifies rerandomization of patients failing abstinence to continuation, switching, or augmentation. PLAN [p.24, final pharmacotherapy paragraph](../joi240036supp1_prod_1716416466.00349.pdf#page=24) repeats a second randomization for week-6 smokers; [p.25, first paragraph](../joi240036supp1_prod_1716416466.00349.pdf#page=25) describes their subsequent medication. PLAN [p.28, general strategy and coding/model](../joi240036supp1_prod_1716416466.00349.pdf#page=28), [p.29, Aims 2–3](../joi240036supp1_prod_1716416466.00349.pdf#page=29), and [p.30, continuing Aim 3 contrasts](../joi240036supp1_prod_1716416466.00349.pdf#page=30) use second-stage continuation as the reference. The missing-observations-as-smoking and intention-to-treat commitments are explicitly present on p.28.

Comparator matched: REPORT [main p.1, both Results paragraphs](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) adds 40 CNRT and 35 VAR nonreturners to continuation. [Main p.4, Results/flow prose](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) states assignment for phase-2 analyses and all-participant primary intention-to-treat analysis. [Main p.6, Figure 2 and footnote c](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) explicitly shows 50 randomized plus 40 assigned CNRT continuers, and 42 randomized plus 35 assigned VAR continuers, with primary-analysis totals 90 and 77. [Main p.8, first limitation](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) explains assignment because those participants were exposed to one strategy. REPORT [supplement p.6, phase-II weighting/coding](../joi240036supp2_prod_1716416466.01349.pdf#page=6) specifies the rerandomized-nonresponder pathway.

**Reported-versus-comparator:** Planned second-stage rerandomization and missing-as-smoking policy versus reported 90 = 50 + 40 CNRT and 77 = 42 + 35 VAR continuation populations.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. The focal comparison is a documented policy, model-mapping or analysis-status comparison; it does not assign an unstated implemented procedure. 

**Calculation:**

Focus D, route A category 5: a primary analysis-population/strategy specification differs between PLAN and REPORT. Exact counts give 90 = 50 + 40, 77 = 42 + 35, and 75 = 40 + 35. This is a comparison of documented membership policies, not a claim that the plan printed sample sizes 50 or 42. Intention-to-treat imputation of an outcome as smoking does not itself specify assignment of a second-stage treatment. Display precision is not applicable to the logical policy comparison; counts reconcile internally.

**Affected result or extracted value:** Primary continuation population membership and its prespecified status for week-12 rescue contrasts.

**Why context does not resolve it:** Route A, category 5 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** The plan's broad intention-to-treat commitment could have been implemented through continuation assignment, consistent with the report's explanation, or an additional amendment could have specified it. Neither supplies the absent explicit second-stage policy in this package.

Necessary inputs available: Prospective second-stage design and contrasts; reported deterministic additions and analyzed totals. Exact missing inputs or definitions: A prospective rule or disclosed amendment assigning nonreturners to second-stage continuation, and any separate rerandomized-only primary result. The complete plan text was searched for nonreturner/assigned-continuation policies; the cited plan sections supply no such rule.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. The actual primary continuation populations explicitly include 40/35 participants who did not undergo the planned second randomization, without an explicit supplied prospective assignment rule.  Planned rerandomization and actual assigned additions are observed. Whether assignment was a planned implementation, later decision, or amendment is not established.

**Potential downstream evidence impact:** A data extractor could record the reported continuation populations as entirely rerandomized or as prospectively specified without capturing the 75 assigned participants. This card does not establish a numerical shift in the reported effects.

<a id="c002"></a>

## C002 — Weight mapping for 75 assigned continuation participants

Pending Human Adjudication.

**Candidate statement:** The reported primary Bayesian model includes 75 assigned nonreturners, but its explicit per-observation inverse-probability weight mapping identifies only responders and rerandomized nonresponders. The probability basis and model treatment of the assigned pathway are not identified.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main actual assigned-continuation population and IPW claim vs REPORT supplement per-observation weight specification

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-009

**Qualifying route:** Route B

**Classification rationale:** Retain REPORT/REPORT, S_C primary, all S_C and S_W, statistical_results. Cross-document population/method mapping is focal; the main report internally combines all-participant analysis with the design-IPW description, and the supplement pairs that method with 90/77 cell membership. The plan does not establish this implementation conflict.

**Classification ambiguity:** Implemented weight/coding are absent; source roles are clear.

**Exact source locations:**

- [main p.1, assigned counts](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)
- [p.4, statistical methods and participant flow](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)
- [p.6, Figure 2/footnote c](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6)
- [main p.7, Figure 3](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7)
- [supplement p.5, opening eAppendix 3](../joi240036supp2_prod_1716416466.01349.pdf#page=5)
- [P.6, first two paragraphs and coding](../joi240036supp2_prod_1716416466.01349.pdf#page=6)
- [Supplement p.19, eTable 3 headings](../joi240036supp2_prod_1716416466.01349.pdf#page=19)

**Source evidence:**

Location found; source value/text matched: REPORT [main p.1, assigned counts](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1), [p.4, statistical methods and participant flow](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4), and [p.6, Figure 2/footnote c](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) establish 75 deterministically assigned nonreturners and IPW primary analyses. The resulting reference groups are also explicitly displayed at [main p.7, Figure 3](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7): 7/90 CNRT, 8% (6%–10%), and 2/77 VAR, 3% (1%–4%).

Comparator matched: REPORT [supplement p.5, opening eAppendix 3](../joi240036supp2_prod_1716416466.01349.pdf#page=5) calls randomization probabilities known fixed design quantities. [P.6, first two paragraphs and coding](../joi240036supp2_prod_1716416466.01349.pdf#page=6) states first-stage p = 0.5, responder continuation p = 1, nonresponder rerandomization p = 0.33; weights 2 and 6.06; and multiplication of each observation's log-posterior contribution by its corresponding weight. Its formula explicitly describes nonresponders who were rerandomized. [Supplement p.19, eTable 3 headings](../joi240036supp2_prod_1716416466.01349.pdf#page=19) confirms 90/77 continuation cells.

**Reported-versus-comparator:** Reported 40 + 35 assigned nonreturners in 90/77-person primary cells versus weights 2 and 6.06 explicitly defined for responder and rerandomized pathways.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. The focal comparison is a documented policy, model-mapping or analysis-status comparison; it does not assign an unstated implemented procedure. 

**Calculation:**

Focus C, route B: a necessary mapping step is absent for an explicitly included nonrandomized pathway. 1/0.5 = 2; 1/(0.5 × 1) = 2; 1/(0.5 × 0.33) = 6.060606, consistent with printed 6.06. Allowing p = 0.5 ± 0.05 and p = 0.33 ± 0.005 gives a conservative rerandomized-weight range [5.4274,6.8376], overlapping 6.06 ± 0.005. Thus the numerical formula reconciles; the reproduced issue is the mapping for 40 + 35 assigned observations, which is not a rounding comparison and does not determine their implemented weight.

**Affected result or extracted value:** Primary CNRT/VAR continuation posterior probabilities 8%/3%, their credible intervals, rescue risk differences, and the assigned-observation weight specification.

**Why context does not resolve it:** B1: Focus C concerns a required per-observation mapping step for a documented included pathway. B2: The fixed randomization probabilities and weight formulas do not identify the implemented weight/coding of the 75 assigned nonreturners; the primary-model context supplies no mapping. B3: This affects the identifiable specification behind the 8%/3% continuation posteriors, their intervals and rescue RDs. Clarifying C001’s prospective policy would not settle this implementation question.

**Alternative source-grounded interpretations:** Assigned observations may share a nonresponder design weight, receive another weight, or enter through an imputation/augmentation convention. The separately reported post hoc GEE/data augmentation analysis on supplement pp.12–13 does not identify the primary Bayesian assigned-pathway mapping.

Necessary inputs available: Actual analyzed membership; fixed probability formulas; per-observation implementation statement. Exact missing inputs or definitions: The assigned nonreturners' weight, probability basis, coding, likelihood inclusion/imputation convention, and any model code confirming their treatment.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. The reported model includes a documented 75-person nonrerandomized pathway that the explicit randomization-based weight mapping does not identify.  Presence of assigned participants and the restricted explicit weight formulas are observed; no numerical bias, actual weight, or consequence for posterior estimates is inferred.

**Potential downstream evidence impact:** An extractor could copy the displayed primary model description without knowing which weights and likelihood contributions produced the continuation estimates. No implemented weight, posterior shift, or preferred model is assigned.

<a id="c003"></a>

## C003 — Mixed denominators in abstract allocation percentages

Pending Human Adjudication.

**Candidate statement:** Four abstract rescue allocation percentages do not reconcile with the 191 CNRT and 157 VAR nonabstainers stated in the same display, although their counts and continuation percentages do. The rescue percentages instead reproduce using the rerandomized subsets of 151 and 122.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main abstract counts/percentages and flow counts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001, F-XS-011

**Qualifying route:** Route A, category 3

**Classification rationale:** Retain REPORT/REPORT within main, S_W only, statistical_results; the relevant rule concerns counts within one display.

**Classification ambiguity:** None in roles/relationships; denominator intent remains the human question.

**Exact source locations:**

- [main p.1, CNRT and VAR Results paragraphs](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)
- [main p.6, Figure 2 branches](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6)

**Source evidence:**

Location found; source value/text matched: REPORT [main p.1, CNRT and VAR Results paragraphs](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) prints, among 191 CNRT nonabstainers, 90 (47%) continuation, 50 (33%) increase, and 51 (34%) switch; among 157 VAR nonabstainers, 77 (49%) continuation, 39 (32%) increase, and 41 (34%) switch.

Comparator matched: REPORT [main p.6, Figure 2 branches](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) reproduces every count and distinguishes rerandomized totals 151 and 122 from full nonabstainer totals 191 and 157. Within the abstract, the common population descriptions and continuation percentages provide the denominator comparator.

**Reported-versus-comparator:** CNRT 50 (33%) and 51 (34%) among 191; VAR 39 (32%) and 41 (34%) among 157, versus percentages computed using those stated populations.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus A, route A category 3. All four affected percentages are preserved below. Conservative half-unit count/denominator envelopes are used.

| Population; count; printed percentage | Recomputed percentage interval | Printed interval | Relative remaining gap |
|---|---|---|---:|
| CNRT 191; increase 50; 33% | [25.848564,26.509186]% | [32.5,33.5]% | 0.181540 |
| CNRT 191; switch 51; 34% | [26.370757,27.034121]% | [33.5,34.5]% | 0.190173 |
| VAR 157; increase 39; 32% | [24.444444,25.239617]% | [31.5,32.5]% | 0.195637 |
| VAR 157; switch 41; 34% | [25.714286,26.517572]% | [33.5,34.5]% | 0.205366 |

Exact counts sum: 90 + 50 + 51 = 191; 77 + 39 + 41 = 157. Continuation fractions 90/191 and 77/157 reproduce 47% and 49%. The rescue percentages instead reproduce using 151 and 122: 50/151 = 33.1126%, 51/151 = 33.7748%, 39/122 = 31.9672%, 41/122 = 33.6066%. All four common-denominator gaps exceed 0.05.

**Affected result or extracted value:** The four abstract increase/switch allocation proportions and their denominators.

**Why context does not resolve it:** Route A, category 3 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** Continuation percentages use all nonabstainers, while rescue percentages deliberately use rerandomized participants; Figure 2 supplies these two possible denominators.

Necessary inputs available: Every count, common population size, and printed percentage. Exact missing inputs or definitions: Explicit per-percentage denominator labels distinguishing full nonabstainers from rerandomized participants.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. Four count/percentage pairs do not reconcile with the abstract's stated 191/157-person populations beyond display precision, while continuation pairs do.  Printed percentages and denominator populations are observed; deliberate mixing versus production mechanism is inferred and unresolved.

**Potential downstream evidence impact:** A data extractor could take the stated full nonabstainer totals as the denominators of the rescue percentages, or take rerandomized totals from the flow display. The card concerns allocation extraction and does not establish changed abstinence estimates.

<a id="c004"></a>

## C004 — Primary CNRT lower credible limit differs across locations

Pending Human Adjudication.

**Candidate statement:** The abstract gives a 6% lower 95% credible limit for each primary CNRT rescue risk difference, while the body and supplementary table give 2% for both matched contrasts. The lower-limit copies differ beyond display precision.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main abstract/body CNRT contrasts vs REPORT supplement eTable 4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-003, F-XS-001, F-ST1-001

**Qualifying route:** Route A, category 2

**Classification rationale:** Retain S_C primary, all S_C/S_W, statistical_results: main-to-supplement and abstract-to-body interval comparisons concern numeric inference.

**Classification ambiguity:** Different combined-versus-individual contrast construction is possible but undisclosed; all compared locations are REPORT.

**Exact source locations:**

- [main p.1, CNRT Results](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)
- [main p.5, Smoking Cessation End of Phase 2, CNRT paragraph](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5)
- [supplement p.21, eTable 4](../joi240036supp2_prod_1716416466.01349.pdf#page=21)

**Source evidence:**

Location found; source value/text matched: REPORT [main p.1, CNRT Results](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) assigns both rescue strategies an absolute RD 6%, 95% CrI 6%–11%. REPORT [main p.5, Smoking Cessation End of Phase 2, CNRT paragraph](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5) prints RD 6%, CrI 2%–11%, for both switching and dose increase.

Comparator matched: REPORT [supplement p.21, eTable 4](../joi240036supp2_prod_1716416466.01349.pdf#page=21) has CNRT increase-minus-stay 6% (2%–11%) and switch-minus-stay 6% (2%–10%). Both affected contrast rows were confirmed, not just the increase row.

**Reported-versus-comparator:** Abstract RD 6% (6%–11%) versus body RD 6% (2%–11%); eTable 4 increase 6% (2%–11%) and switch 6% (2%–10%).

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus B, route A category 2, matched primary interval-limit copies. Lower-limit intervals [5.5,6.5]% and [1.5,2.5]% leave gap 3 percentage points; relative gap to abstract 6% is 0.50. The 10%/11% upper-limit copies have touching [9.5,10.5]/[10.5,11.5] intervals, gap zero; that comparison does not add an issue.

**Affected result or extracted value:** The lower 95% credible limits for primary CNRT dose-increase and switch-versus-continuation risk differences.

**Why context does not resolve it:** Route A, category 2 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** The abstract may summarize a separately pooled rescue contrast or use a different interval construction. No such distinction is stated; the body and two table rows supply the alternative 2% lower limits.

Necessary inputs available: Time point, primary endpoint, baseline treatment, rescue contrasts, RD, credible level, and all compared limits. Exact missing inputs or definitions: Any different pooled posterior/interval calculation specifically intended by the combined abstract statement; posterior draws are absent but unnecessary to establish printed-copy disagreement.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. Abstract lower limit 6% does not overlap or fall within 5% relative precision of the matched body/table lower limit 2%.  The lower-limit disagreement is directly observed; a substituted digit or distinct posterior is an explanation, not an established mechanism.

**Potential downstream evidence impact:** An extractor could copy either 6% or 2% as the lower credible limit. Both versions remain positive, so this comparison does not establish a significance reversal or a changed primary conclusion.

<a id="c005"></a>

## C005 — Primary varenicline-to-CNRT direction, sign, and attribution

Pending Human Adjudication.

**Candidate statement:** The primary VAR-to-CNRT switch result has opposite signs across the main report and eTable 4. The body describes continuation as worse despite displayed switch/continuation probabilities of 0%/3%, and the abstract attaches the −3% result to higher-dose wording before separately reporting the higher-dose 18% result.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main abstract/body/figure direction and contrast vs REPORT supplement eTable 4 sign

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-004, F-XS-002, F-ST1-002

**Qualifying route:** Route A, category 2

**Classification rationale:** Retain S_C primary, all S_C/S_W, statistical_results: signed numerical effects and their direction are focal even though the abstract also changes attribution. All compared content is REPORT.

**Classification ambiguity:** Undefined unsigned/reversed ARD convention; no role ambiguity.

**Exact source locations:**

- [main p.1, VAR Results](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)
- [main p.5, VAR nonabstainer paragraph](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5)
- [main p.7, Figure 3 VAR nonabstainer rows](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7)
- [supplement p.21, eTable 4 VAR switch-CNRT versus VAR-stay row](../joi240036supp2_prod_1716416466.01349.pdf#page=21)
- [Main p.8, Discussion](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8)

**Source evidence:**

Location found; source value/text matched: REPORT [main p.1, VAR Results](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) prints RD −3% (−4% to −1%), followed by wording that continuation was worse than switching to a higher dosage; a separate next sentence assigns increased dosage RD 18%. REPORT [main p.5, VAR nonabstainer paragraph](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5) explicitly attaches −3% (−4% to −1%) to switching from VAR to CNRT relative to VAR continuation, but says continuing was worse than switching.

Comparator matched: REPORT [main p.7, Figure 3 VAR nonabstainer rows](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) prints switch 0% (0%–0%), continuation 3% (1%–4%), and increase 20% (16%–26%). REPORT [supplement p.21, eTable 4 VAR switch-CNRT versus VAR-stay row](../joi240036supp2_prod_1716416466.01349.pdf#page=21) prints +3% (+1%–+4%) for the explicitly labeled switch-versus-stay contrast. [Main p.8, Discussion](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) additionally describes a 3% decrement between continuation 3% and switching 0%, corroborating the modeled direction rather than creating another candidate.

**Reported-versus-comparator:** Main switch RD −3% (−4% to −1%) versus table +3% (+1% to +4%); modeled switch 0% versus continuation 3%, with reversed benefit wording and higher-dose attribution.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus B, route A category 2. Signed point intervals [−3.5,−2.5]% and [2.5,3.5]% have gap 5, relative 5/3 = 1.666667. The negative body interval and positive table interval cannot share the same signed contrast convention. The displayed model switch and continuation probabilities order switch below continuation; the body benefit-direction sentence reverses that order. This uses printed model ordering, not a crude event fraction. The higher-dose abstract attribution is separately checked against the adjacent 18% higher-dose result.

**Affected result or extracted value:** The signed primary VAR-to-CNRT switch risk difference, its credible limits, direction, reference group, and treatment-strategy attribution.

**Why context does not resolve it:** Route A, category 2 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** eTable 4 may present an unsigned magnitude or reversed subtraction, despite its switch-versus-stay label. The abstract may intend its later higher-dose contrast while attaching the −3% result. Neither supplies one coherent direction and contrast for all printed locations.

Necessary inputs available: Explicit contrast labels, primary time point, signed effects/limits, group probabilities, and direction statements. Exact missing inputs or definitions: Table signed-versus-absolute ARD convention and the treatment/contrast intended by the abstract −3% sentence.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. Matched switch-versus-continuation point estimates have opposite printed signs, and body benefit wording conflicts with its modeled ordering.  Signs, labels, group order, and narrative benefit direction are observed; missing-sign production and reversed-contrast convention remain explanations.

**Potential downstream evidence impact:** An extractor could copy a positive or negative switch effect, assign it to a different strategy, or reverse its reference group. This describes possible extraction choices without asserting a downstream recommendation or conclusion change.

<a id="c006"></a>

## C006 — Reported prespecified posterior criterion differs from plan

Pending Human Adjudication.

**Candidate statement:** The report calls a posterior probability cutoff of 0.80 prespecified for confirmation/future evaluation, while the supplied plan explicitly selects 0.90 for advancement. Multiple cutoff scenarios are tabulated, but no separate prospective 0.80 confirmation selection is supplied.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN selected posterior advancement criterion vs REPORT asserted prespecified confirmation criterion

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-008

**Qualifying route:** Route A, category 5

**Classification rationale:** Retain PLAN/REPORT, P_R only, protocol_report. Corroborating cutoff scenarios and matching power-table copies do not create additional within-report or plan relationships.

**Classification ambiguity:** Distinct decision targets or an additional amendment may explain the comparison; roles are clear.

**Exact source locations:**

- [p.31, paragraph preceding Data Simulation Model](../joi240036supp1_prod_1716416466.00349.pdf#page=31)
- [Plan p.33, power prose](../joi240036supp1_prod_1716416466.00349.pdf#page=33)
- [p.34, Table 3](../joi240036supp1_prod_1716416466.00349.pdf#page=34)
- [main p.4, Sample Size Determination and Statistical Analysis Plan](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)
- [supplement p.9, first paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=9)
- [supplement p.18, eTable 2](../joi240036supp2_prod_1716416466.01349.pdf#page=18)

**Source evidence:**

Location found; source value/text matched: PLAN [p.31, paragraph preceding Data Simulation Model](../joi240036supp1_prod_1716416466.00349.pdf#page=31) selects posterior probability ≥0.90 for sufficient evidence to advance to further evaluation; its inline formula uses >0.90. [Plan p.33, power prose](../joi240036supp1_prod_1716416466.00349.pdf#page=33) refers to detecting 0.90 benefit probability, and [p.34, Table 3](../joi240036supp1_prod_1716416466.00349.pdf#page=34) tabulates 0.80, 0.85, 0.90, and 0.95 options.

Comparator matched: REPORT [main p.4, Sample Size Determination and Statistical Analysis Plan](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) describes more than 80% posterior probability as prespecified and sufficient to confirm hypotheses. REPORT [supplement p.9, first paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=9) calls ≥0.80 a prespecified confirmation criterion for clinical decisions/future trials, with >0.80 in the formula. REPORT [supplement p.18, eTable 2](../joi240036supp2_prod_1716416466.01349.pdf#page=18) also tabulates multiple cutoffs and mentions 0.90 in power prose; it does not separately select a prospective 0.80 rule.

**Reported-versus-comparator:** PLAN selected posterior probability 0.90 for advancement versus REPORT prespecified 0.80 for confirmation/future use.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus D, route A category 5: analysis described as prespecified does not match the selected supplied plan rule. At common hundredth precision, intervals [0.895,0.905] and [0.795,0.805] have gap 0.09; relative to plan 0.90, 0.10 >0.05. The criterion is a design definition, so equality comparator glyphs are not used as an independent numeric issue. Searching the complete plan finds tabulated 0.80 scenarios but no separately selected 0.80 confirmation decision.

**Affected result or extracted value:** The prespecified posterior decision criterion and the decision purpose attached to reported benefit probabilities.

**Why context does not resolve it:** Route A, category 5 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** Confirmation in this study and advancement to a later confirmatory trial could be distinct decisions. Both supplied descriptions mention further evaluation/future trials, leaving that distinction unstated.

Necessary inputs available: Selected numeric cutoffs, their stated uses, and complete supplied plan. Exact missing inputs or definitions: An amendment or prospective distinction between 0.80 confirmation and 0.90 advancement decisions.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. The report calls 0.80 prespecified, while the supplied plan explicitly selects 0.90 and contains no separate prospective 0.80 selection for the stated confirmation use.  The selected cutoffs and prespecification claims are observed; a changed rule versus separate intended decisions is unresolved.

**Potential downstream evidence impact:** An extractor could record either 0.80 or 0.90 as the selected prespecified criterion. Probabilities between those cutoffs would receive different status only if the same decision rule applied; many primary benefits above 99% satisfy both. No primary rule is automatically applied to all secondary contrasts.

<a id="c007"></a>

## C007 — Planned primary-model robustness analyses absent from reports

Pending Human Adjudication.

**Candidate statement:** The supplied plan commits to joint observed/missing-outcome modeling and missing-data and optimistic/pessimistic/skeptical-prior robustness analyses for the abstinence model, but the complete supplied reports contain no corresponding results or disclosed replacement.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN general analytic-strategy robustness commitments vs complete supplied REPORT scope

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006, F-ST1-010

**Qualifying route:** Route A, category 5

**Classification rationale:** Retain PLAN/REPORT, P_R only, protocol_report: this is a planned-versus-reported analysis-status comparison. It is not a method preference or an inferred failure of fitted results.

**Classification ambiguity:** Additional outputs or amendments outside this supplied package are unknown; the pattern-mixture promise should not be described as evidence that nonignorable missingness occurred.

**Exact source locations:**

- [p.28, general analytic strategy and prior paragraphs](../joi240036supp1_prod_1716416466.00349.pdf#page=28)
- [p.4, methods/intent-to-treat](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)
- [p.7, secondary outcomes](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7)
- [p.8, post hoc analyses/limitations](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8)
- [pp.1–3, complete contents](../joi240036supp2_prod_1716416466.01349.pdf#page=1)
- [p.5](../joi240036supp2_prod_1716416466.01349.pdf#page=5)
- [p.6](../joi240036supp2_prod_1716416466.01349.pdf#page=6)
- [p.7](../joi240036supp2_prod_1716416466.01349.pdf#page=7)
- [p.8](../joi240036supp2_prod_1716416466.01349.pdf#page=8)
- [p.9](../joi240036supp2_prod_1716416466.01349.pdf#page=9)
- [p.10](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [p.11](../joi240036supp2_prod_1716416466.01349.pdf#page=11)
- [p.12](../joi240036supp2_prod_1716416466.01349.pdf#page=12)
- [p.13](../joi240036supp2_prod_1716416466.01349.pdf#page=13)

**Source evidence:**

Location found; source value/text matched: PLAN [p.28, general analytic strategy and prior paragraphs](../joi240036supp1_prod_1716416466.00349.pdf#page=28) states that primary analyses use intention-to-treat with missing outcomes imputed as smoking; secondary analyses implement joint modeling of observed outcomes/missing data; sensitivity analyses evaluate robustness to missing data; nonignorable patterns are addressed through pattern-mixture methods; and optimistic and pessimistic/skeptical prior sensitivity analyses evaluate prior assumptions. These are prospective commitments in the strategy governing the abstinence model. Joint missing-data modeling and the robustness/prior analysis commitments are not qualified by baseline-covariate imbalance. The pattern-mixture component concerns nonignorable patterns if relevant; the recheck does not assume such patterns occurred.

Comparator matched, including complete absence scope: The entire supplied REPORT scope was examined in direct extraction: main physical pp.1–10 and supplement pp.1–36, not only selected search hits. Main [p.4, methods/intent-to-treat](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4), [p.7, secondary outcomes](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7), and [p.8, post hoc analyses/limitations](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) describe reported primary, secondary, and GEE pathway analyses. Supplement [pp.1–3, complete contents](../joi240036supp2_prod_1716416466.01349.pdf#page=1), [p.5](../joi240036supp2_prod_1716416466.01349.pdf#page=5), [p.6](../joi240036supp2_prod_1716416466.01349.pdf#page=6), [p.7](../joi240036supp2_prod_1716416466.01349.pdf#page=7), [p.8](../joi240036supp2_prod_1716416466.01349.pdf#page=8), [p.9](../joi240036supp2_prod_1716416466.01349.pdf#page=9), [p.10](../joi240036supp2_prod_1716416466.01349.pdf#page=10), [p.11](../joi240036supp2_prod_1716416466.01349.pdf#page=11), [p.12](../joi240036supp2_prod_1716416466.01349.pdf#page=12), and [p.13](../joi240036supp2_prod_1716416466.01349.pdf#page=13) cover all statistical method/results appendices. Supplement pp.14–18 contain design/outcome figures and simulation tables; pp.19–21 baseline/primary contrasts; pp.22–30 adverse events; pp.31–32 visit/medication compliance; pp.33–35 secondary contrasts and GEE pathways; p.36 references. None supplies results for the promised joint missing-data modeling, missingness robustness, or optimistic/pessimistic/skeptical prior sensitivity families. Full-scope searches for sensitivity, pattern-mixture, missingness, optimism/pessimism, skepticism, and robustness were followed by reading the methods, contents, and result-display identities, so this is not a search-only absence claim.

**Reported-versus-comparator:** PLAN general analytic-strategy commitments versus all 46 supplied REPORT pages; missing-as-smoking, convergence-driven prior revision, posterior predictive checking, and post hoc GEE results describe other analyses.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. The focal comparison is a documented policy, model-mapping or analysis-status comparison; it does not assign an unstated implemented procedure. 

**Calculation:**

Focus D, route A category 5: prespecified primary-model robustness analyses are not reported in the supplied REPORT documents. Missing = smoking is the base analysis, not the promised joint-model/sensitivity result. The intercept-prior change on supplement p.8 is expressly to obtain convergence, and posterior predictive checking assesses fit; neither is identified as an optimistic/pessimistic/skeptical prior sensitivity comparison. The GEE pathways are expressly post hoc and estimate another quantity. Display precision does not apply to this analysis-status comparison.

**Affected result or extracted value:** Availability and reported status of the planned abstinence-model joint missing-data and robustness analyses.

**Why context does not resolve it:** Route A, category 5 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** These analyses may have been performed but omitted, supplied elsewhere, or replaced by an amendment. The package establishes report absence only; it cannot establish whether they were performed. The general-strategy wording rather than a separate primary-endpoint sensitivity heading is retained as scope context.

Necessary inputs available: Prospective commitments and complete supplied report scope. Exact missing inputs or definitions: The named sensitivity/joint-model results, a disclosed replacement/amendment, and any condition under which the promised analyses were not applicable. No missing participant-level data are needed to establish that the supplied reports do not contain the results.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. The unconditional robustness/joint-model/prior-analysis commitments are present, but their specified analysis results or disclosed replacement are absent from the complete supplied reports.  Prospective commitments and absence of their results from the 46 supplied REPORT pages are observed. Nonperformance, effect on conclusions, and causes of omission are not inferred.

**Potential downstream evidence impact:** An evidence extractor could record the base model results without the named planned robustness outputs or their reported applicability. The package establishes reporting absence only; it does not establish nonperformance or any sensitivity-induced effect change.

<a id="c008"></a>

## C008 — EOT plus 30-day varenicline continuation denominator

Pending Human Adjudication.

**Candidate statement:** The matched EOT-plus-30-day VAR continuation result is labeled n = 42 in the main and supplementary narratives but 0/77 in eFigure 2, whose caption identifies cell sample sizes. No matched-result statement defines a different secondary analysis population.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main/supplement narrative VAR continuation size vs REPORT supplement eFigure 2 size

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-010

**Qualifying route:** Route B

**Classification rationale:** Retain REPORT/REPORT, S_C primary, all S_C/S_W, statistical_results: main-to-supplement and supplement-summary-to-figure population-size comparisons both occur.

**Classification ambiguity:** The figure may show a full assigned cell while the prose reports only rerandomized membership; no source-role ambiguity.

**Exact source locations:**

- [main p.7, Secondary Outcomes of Abstinence](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7)
- [supplement p.10, opening continuation of summarized analysis](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [supplement p.15, eFigure 2 final VAR nonabstainer-to-VAR row](../joi240036supp2_prod_1716416466.01349.pdf#page=15)
- [main p.6, VAR continuation branch](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6)

**Source evidence:**

Location found; source value/text matched: REPORT [main p.7, Secondary Outcomes of Abstinence](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) describes among 157 phase-1 VAR nonabstainers the EOT+30 continuation result as 0%; n = 42. REPORT [supplement p.10, opening continuation of summarized analysis](../joi240036supp2_prod_1716416466.01349.pdf#page=10) repeats 0%; n = 42 for the same result.

Comparator matched: REPORT [supplement p.15, eFigure 2 final VAR nonabstainer-to-VAR row](../joi240036supp2_prod_1716416466.01349.pdf#page=15) prints 0/77, 0% (0%–0%); its caption calls the right-hand counts cell sample size. REPORT [main p.6, VAR continuation branch](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6) establishes 42 rerandomized plus 35 assigned = 77 primary continuers.

**Reported-versus-comparator:** Main/supplement narrative n = 42 versus eFigure 2 cell denominator 77; main flow separates 42 rerandomized and 35 assigned participants.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus A, route B; matched secondary-result analysis-population size escapes the peripheral count exclusion. Half-unit size intervals [41.5,42.5] and [76.5,77.5] have gap 34; relative to narrative 42, 34/42 = 0.809524. Zero probability copies themselves reconcile and are not treated as an independent display-zero issue.

**Affected result or extracted value:** The EOT-plus-30-day VAR continuation analysis-population size and denominator.

**Why context does not resolve it:** B1: Focus A concerns a matched analysis-population size, which satisfies the explicit exception to peripheral contributor-count comparisons. B2: The nested 42 + 35 = 77 membership explanation is available in the flow figure but neither EOT+30 result defines whether its n denotes only randomized membership or a separate analyzed population. B3: The extractable denominator of this named VAR continuation result is therefore 42 or 77.

**Alternative source-grounded interpretations:** The narrative may list rerandomized participants while the figure includes assigned nonreturners. Main Figure 2 shows precisely these nested groups, but neither matched EOT+30 location explains that denominator convention or a switch of analysis population.

Necessary inputs available: Matched time point, treatment pathway, result and explicit narrative/figure sizes. Exact missing inputs or definitions: Whether n = 42 identifies the actually analyzed result population, only randomized members of a 77-person population, or a separate secondary analysis.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. The same EOT+30 VAR continuation result has two explicit extractable sample sizes, 42 and 77, without a stated secondary population distinction.  The 42/77 printed population-size comparison is observed; which population generated the reported posterior is not inferred.

**Potential downstream evidence impact:** A data extractor could copy 42 or 77 as the denominator or analysis-set size for the same secondary result. The printed zero probabilities reconcile, so the denominator comparison alone establishes no effect change.

<a id="c009"></a>

## C009 — Six-month CNRT summary probabilities and risk difference

Pending Human Adjudication.

**Candidate statement:** The six-month summaries read as CNRT increase/continuation probabilities of 3%/0%, while the detailed analysis and figure give 6%/3%. A 3% risk difference is separately tabulated, leaving the quantity represented by the summary percentages unclear.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main/supplement six-month CNRT summary vs REPORT supplement detailed probabilities/figure/table

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-005, F-XS-004, F-ST1-004

**Qualifying route:** Route A, category 2

**Classification rationale:** Retain S_C primary, all S_C/S_W, statistical_results: the numeric probability/RD identity is focal, rather than merely wording. Both locations are REPORT; six months qualifies as key secondary because it appears in the abstract.

**Classification ambiguity:** Summary quantity and continuation scope are undefined.

**Exact source locations:**

- [main p.7, six-month Secondary Outcomes sentence](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7)
- [supplement p.10, six-month summarized analysis](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [Main p.1, final Results sentence](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1)
- [supplement p.11, six-month CNRT detailed paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=11)
- [Supplement p.16, eFigure 3 matched CNRT rows](../joi240036supp2_prod_1716416466.01349.pdf#page=16)
- [Supplement p.33, eTable 9 six-month CNRT+ contrast](../joi240036supp2_prod_1716416466.01349.pdf#page=33)

**Source evidence:**

Location found; source value/text matched: REPORT [main p.7, six-month Secondary Outcomes sentence](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) describes CNRT dose increase (3%) and VAR dose increase (2%) providing benefit over continuation (0%) in both groups. REPORT [supplement p.10, six-month summarized analysis](../joi240036supp2_prod_1716416466.01349.pdf#page=10) repeats the CNRT+ 3%/continuation 0% reading. [Main p.1, final Results sentence](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1) designates six-month continuous abstinence as a reported secondary outcome.

Comparator matched: REPORT [supplement p.11, six-month CNRT detailed paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=11) prints switch 4%, increase 6%, continuation 3%, and increase-minus-continuation ARD 3% with 96% benefit probability. [Supplement p.16, eFigure 3 matched CNRT rows](../joi240036supp2_prod_1716416466.01349.pdf#page=16) confirms increase 3/50, 6% (4%–9%), and continuation 3/90, 3% (2%–5%). [Supplement p.33, eTable 9 six-month CNRT+ contrast](../joi240036supp2_prod_1716416466.01349.pdf#page=33) prints RD 3% (0%–6%) and benefit probability 96%.

**Reported-versus-comparator:** Summary CNRT increase 3% and continuation 0% versus detailed/figure increase 6% and continuation 3%; eTable 9 separately gives increase-minus-continuation RD 3%.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus B, route A category 2: the printed arm probabilities/readings differ in magnitude for a key secondary result. For increase, 3% ± 0.5 versus 6% ± 0.5 gives gap 2, relative 2/3 = 0.666667. For CNRT continuation, 0% ± 0.5 versus 3% ± 0.5 gives gap 2 against printed zero, reproducing under the zero-value rule. This compares matched model summaries rather than recomputing crude rates. If the summary percentages denote RDs, 3% can instead match eTable 9, but that changes the extracted quantity represented by those parenthetical percentages.

**Affected result or extracted value:** Six-month CNRT dose-increase and continuation abstinence probabilities versus their 3% risk difference.

**Why context does not resolve it:** Route A, category 2 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** The summary may express benefit magnitude above a zero reference, making CNRT 3% an RD; continuation 0% may intend only VAR. The neighboring VAR 2% can serve either probability or RD because its continuation is zero, while the CNRT distinction cannot be resolved numerically without defining the summary quantity.

Necessary inputs available: Reported time point, model arm probabilities, summary labels, contrast RD and benefit probability. Exact missing inputs or definitions: Whether summary percentages represent arm probabilities, RDs, or mixed quantities, and whether continuation 0% refers only to VAR rather than both initial treatments.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. The summary's CNRT 3%/continuation 0% arm readings do not reconcile with detailed/figure 6%/3%; interpreting 3% as RD requires a different quantity definition.  Both sets of printed values/labels are observed. Conflation of RD with arm probability is an explanation, not established intent.

**Potential downstream evidence impact:** An extractor could take 3% as the increase-arm probability rather than the risk difference, or take 0% as CNRT continuation. These are possible quantity-selection effects without an assertion that evidence synthesis has changed.

<a id="c010"></a>

## C010 — Week-6 design intervals and generating beta distributions

Pending Human Adjudication.

**Candidate statement:** The two week-6 95% design intervals do not reproduce from their stated beta distributions, although the same distribution-quantile method reproduces all eight week-12 comparator boxes within the prescribed display-precision rule. The pattern occurs within both the plan and the report supplement.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P, S_W

**Compared document roles:** PLAN distribution definition vs PLAN Figure 2; REPORT distribution definition vs REPORT eFigure 1

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-007

**Qualifying route:** Route A, category 4

**Classification rationale:** Retain primary P_P, all P_P/S_W, plan_material. There is a distribution-to-summary inconsistency within the plan, repeated within the report; agreement between the two documents does not create P_R or S_C. P_P precedes S_W.

**Classification ambiguity:** The supplement remains REPORT by content; an unstated historical-range/simulation-shape distinction is possible.

**Exact source locations:**

- [p.31, Data Simulation Model](../joi240036supp1_prod_1716416466.00349.pdf#page=31)
- [p.32, Figure 2](../joi240036supp1_prod_1716416466.00349.pdf#page=32)
- [supplement p.5, eFigure 1 description](../joi240036supp2_prod_1716416466.01349.pdf#page=5)
- [supplement p.14, eFigure 1](../joi240036supp2_prod_1716416466.01349.pdf#page=14)

**Source evidence:**

Location found; source value/text matched: PLAN [p.31, Data Simulation Model](../joi240036supp1_prod_1716416466.00349.pdf#page=31) defines Figure 2 point estimates and 95% credible intervals as corresponding to its beta distributions. PLAN [p.32, Figure 2](../joi240036supp1_prod_1716416466.00349.pdf#page=32) prints CNRT week-6 0.48, 0.38–0.58, Beta(193,210); VAR week-6 0.50, 0.40–0.60, Beta(785,869).

Comparator matched; every repeated and comparator box: REPORT [supplement p.5, eFigure 1 description](../joi240036supp2_prod_1716416466.01349.pdf#page=5) gives the same distribution-to-summary definition. REPORT [supplement p.14, eFigure 1](../joi240036supp2_prod_1716416466.01349.pdf#page=14) repeats both affected week-6 boxes and all eight week-12 boxes. Every one of these ten boxes was read in both figures. The eight same-method comparator boxes, shown below, occur on both PLAN p.32 and REPORT p.14; ordering differs for two CNRT rescue rows but treatment labels match.

**Reported-versus-comparator:** CNRT 0.38–0.58 with Beta(193,210) and VAR 0.40–0.60 with Beta(785,869) versus their exact beta 2.5th/97.5th percentiles.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus D for PLAN and C for REPORT, route A category 4: printed intervals do not reproduce under the distribution method that reproduces the other boxes. Exact qbeta(.025,.975) gives CNRT [0.430320464,0.527694225] and VAR [0.450581241,0.498690952]. Allowing each integer beta shape ±0.5 gives:

| Affected box | Recomputed lower envelope | Printed lower interval | Relative gap | Recomputed upper envelope | Printed upper interval | Relative gap |
|---|---|---|---:|---|---|---:|
| CNRT week 6 | [0.429090867,0.431550363] | [0.375,0.385] | 0.116029 | [0.526454098,0.528934051] | [0.575,0.585] | 0.079424 |
| VAR week 6 | [0.450280035,0.450882456] | [0.395,0.405] | 0.113200 | [0.498388256,0.498993640] | [0.595,0.605] | 0.160011 |

All four endpoint gaps exceed 0.05. Independent pbeta coverage of printed week-6 ranges is 0.9999500444 for CNRT and 0.9999999996 for VAR, not 0.95. Equal-tail convention is independently supported by the eight comparison boxes; no empirical simulation realization is substituted for the stated beta inputs.

| Week-12 comparator box, in both figures | Printed point; limits; beta shapes | Exact qbeta lower/upper | Relative remaining lower/upper gaps after each input's displayed precision |
|---|---|---|---|
| CNRT responder continuation | 0.50; 0.40–0.60; (47.3,47.3) | 0.400000185 / 0.599999815 | 0 / 0 |
| CNRT nonresponder continuation | 0.02; 0.0007–0.0978; (1.02,35.48) | 0.000773798 / 0.099786534 | 0.011878 / 0.017019 |
| CNRT nonresponder switch to VAR | 0.40; 0.25–0.57; (14.4,21.5) | 0.249238653 / 0.563431726 | 0 / 0.000277 |
| CNRT nonresponder increase | 0.20; 0.10–0.34; (8.90,34.6) | 0.099982998 / 0.334863059 | 0 / 0 |
| VAR responder continuation | 0.75; 0.65–0.83; (62.2,21.0) | 0.649542760 / 0.834381659 | 0 / 0 |
| VAR nonresponder continuation | 0.15; 0.05–0.30; (4.35,23.1) | 0.050067649 / 0.313547295 | 0 / 0.026139 |
| VAR nonresponder switch to CNRT | 0.20; 0.15–0.26; (42.8,170.0) | 0.150159095 / 0.257414844 | 0 / 0 |
| VAR nonresponder increase | 0.40; 0.26–0.55; (17.3,25.7) | 0.262529872 / 0.550732379 | 0 / 0 |

The complete half-unit envelopes, including median envelopes, are preserved in `preprocessing/evidence_rechecker/calculations.txt`. All eight comparator point estimates reconcile with their qbeta medians within display precision. The week-6 VAR median 0.4745968 versus point 0.50 leaves a relative precision gap about 0.0402, at most 0.05; it is not an additional reproduced point discrepancy. The earlier 0.0285 VAR-continuation-upper calculation uses fixed exact shapes; allowing their displayed half-unit intervals gives the more conservative 0.026139 above, with the same precision conclusion.

**Affected result or extracted value:** The week-6 CNRT and VAR design distributions, 95% ranges, and their identity as primary sample-size/power simulation inputs.

**Why context does not resolve it:** Route A, category 4 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** Week-6 boxes may combine historical anticipated ranges with separately selected simulation shapes. Both texts instead state correspondence, so that distinction requires clarification.

Necessary inputs available: Explicit distribution family/shapes, 95% interval claim, exact box labels, and eight supporting method comparisons. Exact missing inputs or definitions: Whether the two week-6 intervals came from other beta shapes, a different uncertainty distribution, or a separate summary construction; the exact realized simulation inputs/code are absent. A new power value cannot be computed from these checks alone.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. Both week-6 boxes, on both source pages, retain four endpoint gaps above 0.05, while all eight same-method comparator boxes reconcile under the specified precision rule.  Printed beta shapes/limits and qbeta/pbeta incompatibility are observed. Which parameters were used in power simulations and any replacement power result are not inferred.

**Potential downstream evidence impact:** An extractor could copy the printed ranges or the beta shapes as interchangeable summaries of the same design distributions. The card does not determine which inputs were simulated, calculate replacement power/sample size, or propose another beta specification.

<a id="c011"></a>

## C011 — Revised normal prior variance and printed odds interval

Pending Human Adjudication.

**Candidate statement:** The revised intercept prior is defined as normal with variance 10, but its printed 95% odds limits are on the scale generated by an SD near 10. Exponentiating the defined normal quantiles does not reproduce either printed endpoint, even with conservative input-rounding allowances.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement normal variance definition vs its claimed 95% prior odds limits

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route B

**Classification rationale:** Retain REPORT/REPORT within supplement, S_W only, statistical_results. The plan's historical original prior merely corroborates original context and does not create P_R.

**Classification ambiguity:** Implemented variance-versus-SD convention is absent; document role is clear.

**Exact source locations:**

- [supplement p.7, initial coefficient-prior paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=7)
- [p.8, first prior paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=8)
- [p.8 model-fitting paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=8)

**Source evidence:**

Location found; source value/text matched: REPORT [supplement p.7, initial coefficient-prior paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=7) and [p.8, first prior paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=8) define the original Normal(mean 0, variance 1 × 10^6) and approximate 95% log limits −1960 to 1960. P.8's model-fitting paragraph changes the intercept to Normal(mean 0, variance 10) on the log scale.

Comparator matched: The same [p.8 model-fitting paragraph](../joi240036supp2_prod_1716416466.01349.pdf#page=8) claims the revised 95% prior interval for intercept odds is 3.07 × 10^−9 to 325,215,956, and explains that treatment-coefficient priors remained unchanged and posterior predictive checking indicated fit.

**Reported-versus-comparator:** Normal mean 0, variance 10 versus claimed prior odds limits 3.07 × 10^−9 to 325,215,956; defined variance gives about 0.0020336 to 491.7401.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus C, route B: the defined prior does not generate its stated interval. The original variance gives qnorm(.975) × 1000 = 1959.963984, consistent with ±1960. Revised variance 10 gives exp(±1.959963984 × sqrt(10)) = [0.002033594579,491.7400991]. Allowing variance [9.5,10.5] gives lower envelope [0.001744985241,0.002379143534] and upper [420.3193232,573.0707494]. The printed lower interval is [3.065,3.075] × 10^−9; upper [325215955.5,325215956.5]. Relative remaining lower gap exceeds 568000; upper gap is about 0.99999824. Even additionally allowing printed mean 0 a conservative half-unit interval [−0.5,0.5] gives lower [0.00105838705,0.00392254455] and upper [254.9365564,944.8339342]; remaining relative gaps still exceed 344000 and 0.99999709. Thus interpreting zero as an exact defined prior center is unnecessary to the conclusion.

An SD of 10 gives exact odds [3.075987511 × 10^−9,325098849.2]; the approximation ±1.96 × 10 gives about [3.07488 × 10^−9,325215956.1]. This supplies a bounded alternative specification, not an assigned replacement prior.

**Affected result or extracted value:** The primary Bayesian model intercept-prior variance/concentration and its 95% prior odds interval.

**Why context does not resolve it:** B1: Focus C concerns a defined normal-distribution-to-interval mapping. B2: Disclosure of a convergence-driven revision does not establish whether variance 10, SD 10, or another convention was implemented, and the same paragraph supplies incompatible numerical descriptions. B3: The primary model’s intercept-prior specification and concentration cannot be copied as a single coherent definition.

**Alternative source-grounded interpretations:** The numerical odds limits are consistent within scope precision with an SD near 10 rather than variance 10. A different prior parameterization may have been intended. The reported convergence-driven revision does not select which numeric convention was implemented.

Necessary inputs available: Distribution, log scale, mean/variance, 95% level, and stated exponentiation mapping. Exact missing inputs or definitions: Whether the implemented intercept normal prior used variance 10, SD 10/variance 100, or another parameter convention; fitted code is absent.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. Normal variance 10 cannot generate either stated odds endpoint, even with conservative half-unit variance and mean allowances.  The variance-to-odds interval inconsistency is observed; a variance/SD parameter mix and any effect on posterior results are not established.

**Potential downstream evidence impact:** An extractor could record variance 10 while using an interval that implies a different prior concentration. This bounds model-specification reproducibility; fitted code and posterior draws are absent, so no treatment-effect sensitivity or posterior change is computed.

<a id="c012"></a>

## C012 — Repeated EOT plus 30-day decimal-scale discrepancies

Pending Human Adjudication.

**Candidate statement:** Seven EOT-plus-30-day narrative occurrences contain point estimates or credible limits at a different decimal scale from their matched figure/table copies. The first six also print reversed interval endpoints and points outside even the numerically ordered ranges.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement seven EOT+30 narrative occurrences vs matched eFigure 2/eTables 9–11

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-006, F-XS-003, F-ST1-003

**Qualifying route:** Route A, category 2; occurrences 1–6 additionally qualify under Route A, category 1.

**Classification rationale:** Retain S_W only, statistical_results: every focal numeric comparison and containment check occurs in one REPORT supplement. The main's summarized counterparts merely corroborate some comparator values and are not required conflicting relationships.

**Classification ambiguity:** None in content roles or relationship identity; intended scale/model remains undefined.

**Exact source locations:**

- [Supplement p.10, CNRT nonabstainer switch probability](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [P.15, eFigure 2 CNRT nonabstainer→VAR](../joi240036supp2_prod_1716416466.01349.pdf#page=15)
- [P.10, same CNRT probability sentence, increase](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [P.15, eFigure 2 CNRT nonabstainer→CNRT+](../joi240036supp2_prod_1716416466.01349.pdf#page=15)
- [P.10, CNRT switch-minus-continuation ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [P.33, eTable 9 EOT+30 CNRT VAR-switch column](../joi240036supp2_prod_1716416466.01349.pdf#page=33)
- [P.10, final VAR nonabstainer probability sentence, increase](../joi240036supp2_prod_1716416466.01349.pdf#page=10)
- [P.15, eFigure 2 VAR nonabstainer→VAR+](../joi240036supp2_prod_1716416466.01349.pdf#page=15)
- [P.11, first paragraph, VAR increase-minus-continuation ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=11)
- [P.33, eTable 9 EOT+30 VAR+ column](../joi240036supp2_prod_1716416466.01349.pdf#page=33)
- [P.11, second paragraph, VAR increase-minus-switch ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=11)
- [P.34, eTable 10 EOT+30 VAR column](../joi240036supp2_prod_1716416466.01349.pdf#page=34)
- [P.11, phase-1 abstainers paragraph, CNRT versus VAR ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=11)
- [P.35, eTable 11 EOT+30 row](../joi240036supp2_prod_1716416466.01349.pdf#page=35)

**Source evidence:**

Location found; source value/text matched; every comparator matched: All seven affected occurrences were read visually and in fresh direct extraction. Every paired result matches treatment pathway, EOT+30 time point, probability-versus-ARD identity, and contrast.

| Occurrence | Direct REPORT narrative location and printed reading | Direct REPORT comparator and printed reading |
|---|---|---|
| 1 | [Supplement p.10, CNRT nonabstainer switch probability](../joi240036supp2_prod_1716416466.01349.pdf#page=10): 1.0% (7.0%–1.3%) | [P.15, eFigure 2 CNRT nonabstainer→VAR](../joi240036supp2_prod_1716416466.01349.pdf#page=15): 10% (7%–13%); p.9 summarized narrative also prints 10% |
| 2 | [P.10, same CNRT probability sentence, increase](../joi240036supp2_prod_1716416466.01349.pdf#page=10): 8.0% (5.0%–1.1%) | [P.15, eFigure 2 CNRT nonabstainer→CNRT+](../joi240036supp2_prod_1716416466.01349.pdf#page=15): 8% (5%–11%) |
| 3 | [P.10, CNRT switch-minus-continuation ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=10): 6.0% (3.0%–1.0%) | [P.33, eTable 9 EOT+30 CNRT VAR-switch column](../joi240036supp2_prod_1716416466.01349.pdf#page=33): 6% (3%–10%) |
| 4 | [P.10, final VAR nonabstainer probability sentence, increase](../joi240036supp2_prod_1716416466.01349.pdf#page=10): 8.0% (5.0%–1.1%) | [P.15, eFigure 2 VAR nonabstainer→VAR+](../joi240036supp2_prod_1716416466.01349.pdf#page=15): 8% (5%–11%) |
| 5 | [P.11, first paragraph, VAR increase-minus-continuation ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=11): 8.0% (5.0%–1.1%) | [P.33, eTable 9 EOT+30 VAR+ column](../joi240036supp2_prod_1716416466.01349.pdf#page=33): 8% (5%–11%) |
| 6 | [P.11, second paragraph, VAR increase-minus-switch ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=11): 8.0% (5.0%–1.1%) | [P.34, eTable 10 EOT+30 VAR column](../joi240036supp2_prod_1716416466.01349.pdf#page=34): 8% (5%–11%) |
| 7 | [P.11, phase-1 abstainers paragraph, CNRT versus VAR ARD](../joi240036supp2_prod_1716416466.01349.pdf#page=11): 1.1% (−1.0%–22%) | [P.35, eTable 11 EOT+30 row](../joi240036supp2_prod_1716416466.01349.pdf#page=35): 11% (−1%–22%), probability 97% |

**Reported-versus-comparator:** The seven individually linked narrative/figure/table pairs below; disputed copies include 1.0/10, 1.3/13, and 1.1/11 percentage points.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. Check all seven matched occurrences individually and check interval ordering/point containment independently of rounding.

**Calculation:**

Focus B, route A categories 1 and 2. Occurrences 1–6 have reversed endpoint order; their points lie outside even the numerically ordered printed endpoint range. For occurrence 1, [1.3,7.0] cannot contain 1.0; for occurrences 2/4/5/6, [1.1,5.0] cannot contain 8.0; for occurrence 3, [1.0,3.0] cannot contain 6.0. These containment observations are independent of rounding. Printed-copy gaps also reproduce:

| Compared numeric copies, percentage points | Reference interval | Comparator interval | Gap | Relative gap | Occurrences |
|---|---|---|---:|---:|---|
| 1.0 vs 10 | [0.95,1.05] | [9.5,10.5] | 8.45 | 8.45 | 1 point; 3 upper limit |
| 1.3 vs 13 | [1.25,1.35] | [12.5,13.5] | 11.15 | 8.576923 | 1 upper limit |
| 1.1 vs 11 | [1.05,1.15] | [10.5,11.5] | 9.35 | 8.50 | 2/4/5/6 upper limits; 7 point |

All other matched point/limit copies in these rows overlap within their own displayed precision: e.g., 8.0/8, 5.0/5, 6.0/6, 3.0/3, −1.0/−1 and 22/22. They are not additional differences.

**Affected result or extracted value:** All seven named EOT-plus-30-day probability and risk-difference readings, including the affected point estimates and credible limits.

**Why context does not resolve it:** Route A, category 2 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** The figure/table readings provide a plausible alternative decimal scale for every affected value. A distinct narrative model could explain some cross-location values, but would not reconcile the narrative's own endpoint ordering/containment.

Necessary inputs available: All printed points/limits, matching figure/table values, credible level, and contrast labels. Exact missing inputs or definitions: Intended narrative scales and any separately fitted narrative analysis. No such distinct model is disclosed for these copies; posterior draws are absent but unnecessary for the printed containment/copy comparisons.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. All seven registered printed occurrences are present; each has at least one matched-copy gap above 0.05, and the first six additionally fail printed interval ordering/containment.  Seven numeric and six containment/order discrepancies are observed; a shared decimal-production mechanism is inferred, not established. The six-month responder interval in overlapping F-XS-003/F-ST1-003 provenance remains separately represented by C013, with its own rule and question rather than being silently omitted.

**Potential downstream evidence impact:** An extractor could copy the narrative decimal readings or the matched figure/table readings for these seven named results. This does not establish a shared production mechanism or a universal change in secondary conclusions.

<a id="c013"></a>

## C013 — Six-month responder credible limits differ across locations

Pending Human Adjudication.

**Candidate statement:** The six-month responder risk-difference interval is −1.3% to 1.1% in the narrative but −11% to 12% in eTable 11. Its point and benefit-probability copies reconcile within precision; multiplying the narrative limits by ten does not reproduce the table interval.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement six-month responder narrative credible limits vs eTable 11

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-007

**Qualifying route:** Route A, category 2

**Classification rationale:** Retain REPORT/REPORT within supplement, S_W only, statistical_results: credible-limit extraction is focal. Figure p.16 supplies population context without adding a different document relationship.

**Classification ambiguity:** Contrast direction and interval construction are unstated.

**Exact source locations:**

- [supplement p.12, Continuous Abstinence at 6 months for Abstainers](../joi240036supp2_prod_1716416466.01349.pdf#page=12)
- [supplement p.35, eTable 11 six-month Continuous Abstinence row](../joi240036supp2_prod_1716416466.01349.pdf#page=35)
- [P.16, eFigure 3 responder rows](../joi240036supp2_prod_1716416466.01349.pdf#page=16)

**Source evidence:**

Location found; source value/text matched: REPORT [supplement p.12, Continuous Abstinence at 6 months for Abstainers](../joi240036supp2_prod_1716416466.01349.pdf#page=12) prints CNRT/VAR arm probabilities 39%/40%; difference probability 55%; ARD 1.0% (−1.3%–1.1%), with wording of a small VAR benefit.

Comparator matched: REPORT [supplement p.35, eTable 11 six-month Continuous Abstinence row](../joi240036supp2_prod_1716416466.01349.pdf#page=35) prints ARD 1% (−11%–12%), probability 56%, under the column heading ARD for CNRT vs VAR. [P.16, eFigure 3 responder rows](../joi240036supp2_prod_1716416466.01349.pdf#page=16) confirms the same six-month responder arm identities and 39%/40% probabilities. The p.12/p.35 component of F-XS-003/F-ST1-003 is retained as additional provenance to canonical F-NUM-007.

**Reported-versus-comparator:** Narrative ARD 1.0% (−1.3%–1.1%), probability 55%, versus table ARD 1% (−11%–12%), probability 56%.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus B, route A category 2, matched credible-limit magnitudes. Lower intervals [−1.35,−1.25]% and [−11.5,−10.5]% leave gap 9.15, relative to 1.3 is 7.038462. Upper intervals [1.05,1.15]% and [11.5,12.5]% leave gap 10.35, relative to 1.1 is 9.409091. The point copies 1.0/1 overlap, and probability intervals 55 ±0.5 and 56 ±0.5 touch; they have zero gap. This occurrence has ordered limits and an in-interval point, so containment is not its determining rule. Multiplying the narrative limits by ten gives −13/+11, not the table −11/+12; sign reversal alone also fails to reconcile their widths.

**Affected result or extracted value:** The six-month CNRT-versus-VAR responder risk-difference credible interval and contrast orientation.

**Why context does not resolve it:** Route A, category 2 applies as an always-register category to the reproduced comparison. Reconstruction from another location does not remove that qualifying category.

**Alternative source-grounded interpretations:** A distinct analysis, summary definition, or contrast orientation may apply. Different direction wording is present, but cannot by itself explain the order-of-magnitude width comparison.

Necessary inputs available: Six-month responder population, matched ARD, credible limits, and probability values. Exact missing inputs or definitions: Which credible interval and contrast orientation are intended; whether distinct posterior models or interval constructions generated the two displays.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. Both credible-limit pairs differ beyond 0.05 under half-unit intervals, independently of the point/probability copies that reconcile within precision.  Limit magnitudes/widths are observed; the EOT+30 production explanation is not assumed for this distinct occurrence.

**Potential downstream evidence impact:** An extractor could copy markedly different interval limits and widths for the responder contrast. Both intervals include zero, so this comparison does not establish a significance reversal.

<a id="c014"></a>

## C014 — Augmented-CNRT dose attached to the primary-design input

Pending Human Adjudication.

**Candidate statement:** The anticipated primary-design CNRT+ cell is defined with 4-mg lozenges in eFigure 1, but the matching simulation-table and trial regimen definitions specify 2 mg. The supplied report does not identify whether a historical dose assumption explains the design-cell attribution.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT supplement anticipated CNRT+ dose vs REPORT main/supplement regimen definitions

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Classification rationale:** Retain S_C primary, all S_C/S_W, report_internal_inconsistency: the numerical dose assigns a primary-design value to a different intervention identity across REPORT locations. The plan only corroborates one side, so P_R does not apply.

**Classification ambiguity:** Historical anticipated dose versus implemented trial/simulation-table dose is possible; the supplement remains REPORT by content.

**Exact source locations:**

- [supplement p.14, eFigure 1 caption and CNRT+ week-12 cell](../joi240036supp2_prod_1716416466.01349.pdf#page=14)
- [supplement p.17, eTable 1 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=17)
- [Supplement p.18, eTable 2 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=18)
- [P.15, eFigure 2 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=15)
- [p.16, eFigure 3 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=16)
- [main p.4, first medication paragraph](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4)
- [main p.7, Figure 3 caption](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7)
- [Main p.8, second limitation](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8)
- [p.25, medication paragraph](../joi240036supp1_prod_1716416466.00349.pdf#page=25)

**Source evidence:**

Location found; source value/text matched: REPORT [supplement p.14, eFigure 1 caption and CNRT+ week-12 cell](../joi240036supp2_prod_1716416466.01349.pdf#page=14) defines dose increase as two 21-mg patches plus 4-mg lozenges, attaching CNRT+ to the anticipated primary-outcome input 0.20, interval 0.10–0.34, Beta(8.90,34.6).

Comparator matched; every cited regimen location: REPORT [supplement p.17, eTable 1 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=17) defines CNRT+ as two 21-mg patches plus 2-mg lozenges for the simulation results. [Supplement p.18, eTable 2 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=18) repeats the 2-mg simulation-table definition. [P.15, eFigure 2 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=15) and [p.16, eFigure 3 caption](../joi240036supp2_prod_1716416466.01349.pdf#page=16) define the two-patch plus lozenge pathway without specifying lozenge mg; they provide pathway context only. REPORT [main p.4, first medication paragraph](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4) explicitly continues 2-mg phase-1 lozenges with increased patches; [main p.7, Figure 3 caption](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7) repeats 2 mg. [Main p.8, second limitation](../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=8) states that use of 2-mg rather than 4-mg lozenges was a practical choice. PLAN [p.25, medication paragraph](../joi240036supp1_prod_1716416466.00349.pdf#page=25) corroborates purchase/use of 2-mg lozenges; it does not supply a conflicting planned design input for this candidate. This caption-specific clarification follows the independent audit's direct visual reread; the focal 4-mg and explicit 2-mg comparators remain reproduced.

**Reported-versus-comparator:** eFigure 1 CNRT+ 4-mg lozenges, anticipated probability 0.20 and Beta(8.90,34.6), versus simulation-table/trial 2-mg definitions. Captions on supplement pp.15–16 specify no lozenge mg.

**Reasoning procedure:** Match the source-defined treatment pathway, population, time point and quantity before applying the stated arithmetic, distribution or logical rule. Allow every displayed numerical input and compared copy its own half-unit interval, then compute the remaining gap relative to the reference printed value. Defined-distribution calculations use the supplied family and parameters. 

**Calculation:**

Focus D/C-related primary-design intervention identity, route B. Integer printed dose intervals [3.5,4.5] mg and [1.5,2.5] mg have gap 1 mg; relative to the focal 4-mg copy, 1/4 = 0.25 >0.05. The comparison concerns which intervention the primary-design probability/distribution denotes, not matching anticipated 0.20 to an observed outcome or inferring a dose-dependent power change.

**Affected result or extracted value:** The intervention dose attached to the CNRT+ anticipated probability 0.20 and Beta(8.90,34.6) primary-design input.

**Why context does not resolve it:** B1: The numeric regimen defines the intervention attached to a primary-design probability/distribution, rather than a peripheral panel pointer. B2: A historical 4-mg anticipated regimen and a 2-mg simulation/trial regimen are possible, but no supplied statement identifies which generated the 0.20/Beta(8.90,34.6) cell. B3: Intervention-dose and design-input extraction can therefore differ.

**Alternative source-grounded interpretations:** The anticipated figure could retain a historical 4-mg regimen while the trial and other simulation displays use 2 mg. The main limitation establishes the actual 2-mg choice, but neither resolves which regimen the anticipated beta input represents.

Necessary inputs available: Numeric caption dose, same CNRT+ pathway/cell identity, simulation-table regimen definitions, and actual report regimen. Exact missing inputs or definitions: Whether the anticipated design distribution assumed 4-mg lozenges historically or 2-mg lozenges as defined in the simulation tables, and any disclosed change relating those assumptions.

**Mechanical evidence recheck:** Every cited affected location and comparator was found and source-matched using fresh direct PDF extraction and relevant current-source visual checks. The stated rule and precision/logical comparison reproduced. eFigure 1 attaches 4-mg lozenges to the CNRT+ design input, while its matched simulation-table and trial regimen definitions specify 2 mg beyond display precision. The pp.15–16 captions were corrected to pathway context without a lozenge mg specification; explicit 2-mg comparators remain independently present. Caption/table dose readings are observed; a historical-dose assumption or carryover mechanism is not established. No change in effect or power is inferred.

**Potential downstream evidence impact:** An extractor could attribute the anticipated CNRT+ distribution to either a 4-mg or 2-mg lozenge regimen. No comparison of anticipated 0.20 with observed 14% is used, and no dose-specific effect or power change is inferred.

## Downstream Evidence-Chain Considerations

Systematic reviewers, meta-analysts and guideline teams may extract population sizes, arm probabilities, signed contrasts, interval limits, intervention doses and prespecified analysis status from different report locations. If a candidate is confirmed, its specific evidence choice could warrant a corresponding clarification in extraction records. The cards identify the affected values and definitions without claiming that propagation, an evidence-synthesis conclusion change or harm has occurred. Population-policy and implementation questions are kept distinct, and model-based estimates are not replaced with crude ratios.

## Limitations and Missing Definitions

The package contains published aggregate results and one prospective protocol, but no participant-level raw data, fitted model code/coefficient vector/covariance, posterior draws, simulation realization/seed/sampler settings, or complete amendment history. These limits prevent full reconstruction of fitted posteriors, GEE estimates and Monte Carlo power, and prevent choosing among some source-grounded alternatives. They do not leave an unmapped source page or unreviewed registered relationship.

Issue-specific missing definitions are the prospective assigned-continuation policy (C001), assigned-observation weights/coding (C002), allocation percentage denominators (C003), primary interval construction (C004), signed contrast/strategy attribution (C005), selected confirmation/advancement rule (C006), planned robustness outputs and applicability (C007), secondary population convention (C008), summary probability-versus-RD identity (C009), beta-summary/simulation input identity (C010), implemented prior parameter convention (C011), narrative decimal scale/model identity (C012), six-month interval/contrast construction (C013), and anticipated dose assumption (C014).

C007 describes absence from the complete supplied REPORT scope; it cannot establish whether the planned analyses were performed. Its pattern-mixture component remains conditional on nonignorable patterns being applicable, without assuming that such patterns occurred. C006 retains the possibility of distinct confirmation and advancement decisions. Stale historical identity fields and incomplete historical image-engine provenance were addressed through current-source checks. The durable [limitations record](review_1_6_2/limitations.md) preserves these bounds.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_2/routing_preflight.md) records PASS, run model gpt-6.1-sol from DEFAULT, CURRENT_SESSION provider, INTERACTIVE_CLI execution and the ten verified role presets. Ordinary specialists use medium reasoning effort; the coordinator, statistical passes, screen, recheck and audit use high. Mandatory stages used fresh distinct runtime agents; the optional plan mapper covered a disjoint bounded support shard.

Tooling was local CPU: Poppler 26.01.0 supplied pdfinfo, pdftotext and pdftoppm; R 4.5.2 supplied defined beta/normal arithmetic. Tesseract 5.5.0 and Pandoc 3.7.0.2 were available. No OCR or fallback environment was needed; fallback environment removed is NOT_CREATED. Source confirmation derivatives name their engine and exact source ranges in the canonical artifacts.

### Source integrity

Direct source SHA-256 values are:

| Source | SHA-256 |
|---|---|
| DOC-001 | f51fd5b8f20a10df81121eb8aa19f1c4defb98d04ad476ce1e60dd95c68a18d1 |
| DOC-002 | eb73035cb7b875a25b3c955e6f730eb7f6ef88b711b3d18f0296ee3a857ed004 |
| DOC-003 | 51a06c53356580e94c262ebe16a3efc634ef1130da3ad33c478f97e0eae6f566 |

The [before-source hashes](review_1_6_2/source_hashes_before.sha256) and [before-reuse hashes](review_1_6_2/reused_artifact_hashes_before.sha256) identify all three sources and 297 reused assets. The coordinator recomputed every hash after complete Markdown assembly: the [after-source hashes](review_1_6_2/source_hashes_after.sha256) and [after-reuse hashes](review_1_6_2/reused_artifact_hashes_after.sha256) are identical to their before manifests. All 300 entries remain unchanged. Standalone HTML is rendered from this complete report; the final mechanical validator records its completion checks and result in [review_validation.json](review_1_6_2/review_validation.json).

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_plan_mapper_shard | root/plan_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/plan_quantitative_evidence.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistical_pass1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistical_pass2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Every actual runtime, including the coordinator, the optional plan-mapping shard and this report generator, is recorded once in the [execution manifest](review_1_6_2/agent_execution_manifest.md). The report generator owns complete Markdown assembly and the limitations record; it does not render HTML.

### Reproducibility performance

- **Target basis:** Three PDFs with 91 unique pages and complete source-matched reusable text; no Office conversion or initial OCR required. The report includes a sequential trial, Bayesian results, inverse-probability modeling, multiple supplementary tables and figures, and one 45-page prospective protocol. Two concurrent mapping agents, three concurrent checker agents, two mandatory statistical passes, independent screening, recheck, audit, and report assembly remain required. Plan 25-40 minutes for this combination of low fresh-extraction burden and substantial relationship/review-wave work; the range is not derived from protocol length or page count alone.
- **Total source units:** 91
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T06:37:03Z
- **Finished UTC:** 2026-10-11T07:47:59Z
- **Observed elapsed minutes:** 70.93
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Full source-linked checker wave over 104 numeric and 93 statistical groups; independent source rereading and grouping of 28 findings; direct mechanical recheck of every location for 14 registered candidates; mandatory second statistical pass and independent bidirectional audit with caption/provenance repairs; complete 14-card report assembly; mechanical validation path/index repairs

The coordinator finalizes these exact performance values immediately after complete Markdown assembly. The 25–40-minute planning range is a package-specific expectation, not a candidate or coverage limit. Local HTML rendering and mechanical validation are outside observed review time; any later model-based repair requires a refreshed finish time.
