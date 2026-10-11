# Quantitative Quality-Control Consistency Review — HIGH-WEAN Trial

**Pending Human Adjudication**

This Workflow 1.6.1 review prepares candidate reporting issues for human assessment. Evidence states and inclusion audits describe the review record; they do not adjudicate the candidates or the paper. Every human adjudication field remains `__`.

## Executive Quality-Control Summary

Complete review of four supplied PDFs, covering all 69 pages, produced **five stable candidates: C001–C005**. Two concern reported absolute treatment differences; three concern prospective versus reported endpoint or analysis specifications. All five were reproduced by an independent exact-source recheck and received a CONFIRMED inclusion audit. All remain Pending Human Adjudication.

Twelve checker findings received independent inclusion decisions: ten INCLUDE records consolidate into five distinct issues, and two findings were screened out. A separate audit reviewed all 71 checker excluded-observation records. Both fresh statistical passes covered all 49 statistical relationship groups; the numeric inventory covers all 118 numeric groups. Candidate selection applied the supplied inclusion threshold without a count target.

## Package and Reused-Evidence Provenance

The supplied package concerns high-flow nasal oxygen alone versus high-flow nasal oxygen alternating with noninvasive ventilation after extubation. In the cards, control denotes the former and intervention the latter. The analyzed populations are 302 and 339 respectively unless a subgroup is specified. Document roles follow content.

| Source ID | Actual source filename and scope | Role | Content |
|---|---|---|---|
| DOC-001 | [jama_thille_2019_oi_190108.pdf — pp.1–11](<../jama_thille_2019_oi_190108.pdf#page=1>) | REPORT | Main randomized trial article and appended material |
| DOC-002 | [joi190108supp1_prod.pdf — pp.1–48](<../joi190108supp1_prod.pdf#page=1>) | PLAN | Prospective protocol, version 4, 17 October 2017, with appendices |
| DOC-003 | [joi190108supp2_prod.pdf — pp.1–9](<../joi190108supp2_prod.pdf#page=1>) | REPORT | eTables 1–5 and survival eFigure |
| DOC-004 | [joi190108supp3_prod.pdf — p.1](<../joi190108supp3_prod.pdf#page=1>) | REPORT | Administrative data-sharing statement |

The curator inventoried and hashed 128 reusable native/layout text, OCR, rendered-page, map and provenance assets. They served as source locators and transcription aids. Existing native text matches current source extraction after whitespace normalization on all 69 pages, including the partial protocol p.42 extraction. Partial historical maps did not restrict this review. Earlier candidate selections, classifications and reports were preserved and were not discovery inputs. The supplied sources were the only scientific evidence; no external literature was used.

Detailed provenance is in [Source inventory](review_1_6_1/source_inventory.md) and [Evidence-asset inventory](review_1_6_1/evidence_asset_inventory.md). Source PDFs, rather than their derivatives, control the candidate evidence.

## Scope, Complete Coverage, and Exclusions

The review covered counts and denominators, estimate and test logic, statistical method logic, and planned versus reported statistical design. It did not perform a raw-data, broad clinical, methodology, novelty or misconduct audit, or propose a preferred analysis.

| Source | Unit type | Total | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | PDF_PAGE | 48 | 47 | 1 | 48 | COMPLETE |
| DOC-003 | PDF_PAGE | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004 | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | PDF_PAGE | **69** | **68** | **1** | **69** | **COMPLETE** |

All supplied pages were mapped, including administrative, bibliography and ethical material with no applicable current-trial numeric relationship. Protocol p.42 lacked usable full-form reusable extraction. Fresh Poppler rendering, complete visual transcription and targeted Tesseract CPU OCR closed that unit. Partial OCR did not control its inequality transcription. Historical missing OCR on main pp.5–8 was covered by substantial layout text and readable images. There is no scientific source-coverage gap.

The inclusion threshold requires reproduced source evidence, focus-area eligibility, an issue not resolved at once by immediate context for a statistically literate reader, and plausible relevance to a named result's interpretation or extraction. Rounding/display precision, immediately resolved terminology or typography, explicitly modeled-versus-crude comparisons, conditional observations, peripheral comparisons and out-of-focus observations were screened out. Missing definitions were recorded rather than filled from convention. See [Complete source coverage](review_1_6_1/source_coverage.md) and [Coverage manifest](review_1_6_1/coverage_manifest.md).

## Quantitative and Statistical Relationship Coverage

| Inventory or review stage | Completed scope | Findings | Checker excluded observations |
|---|---|---:|---:|
| Numeric inventory/check | N001–N118: 118/118 groups | 2 | 16 |
| Cross-source review | Complete matched report/plan relationships and report comparisons | 5 | 25 |
| Statistical pass 1 | S001–S049: 49/49 PASS_1_COMPLETE | 5 | 14 |
| Statistical pass 2 | S001–S049: 49/49 PASS_2_COMPLETE, after ledger/screen/recheck | 0 new | 16 |
| **Total checker records** | Complete assigned evidence | **12 findings** | **71 excluded observations** |

Grouped records include every attached table row and cell, rather than sampled examples: all 31 eTable 1 contrasts, 71 printed eTable 2 P contrasts, 26 subgroup outcome rows, 30 center rows and survival risk-table cells. Main and support maps crosswalk 97+21 numeric groups and 32+17 statistical groups to the complete inventories. Both passes cover every registered statistical relationship. Exact tests or estimators unavailable from the package remain bounded reconstruction limitations.

Statistical pass 1 and pass 2 used distinct fresh gpt-6.1-sol/high runtimes. Pass 2 produced no new findings; a second inclusion screen was therefore unnecessary. See [Numeric relationships](review_1_6_1/relationships/numeric_relationship_inventory.md), [Statistical relationships](review_1_6_1/statistics/relationship_inventory.md), [Pass 1](review_1_6_1/checkers/statistical_pass_1.md) and [Pass 2](review_1_6_1/checkers/statistical_pass_2.md).

## Inclusion Screening Summary

| Decision | Reason code | Finding records |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 10 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 1 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| **Total** | All decisions | **12** |

The ten included records consolidate by issue into C001 (three findings), C002 (two), C003 (one), C004 (two) and C005 (two). All other screened-out reason codes have zero finding records. F-XS-002's main/supplement P-value comparison was screened out under half-unit display precision. F-XS-004's purported omitted randomized-treatment Cox effect depended on a mapping not established by the supplied plan. The P subpart of included F-ST1-001 was also excluded within that finding and does not create another finding record or candidate relationship.

These twelve independently screened findings are distinct from the 71 checker self-excluded observations, all of which were audited in both directions. The final auditor identified no additional qualifying issue or screening reversal. Display-zero P values alone do not qualify. The reconciled decisions and provenance are in [Inclusion screen](review_1_6_1/screening/inclusion_screen.md).

## Review-Domain Summary

| Review domain | Definition | Candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests or statistical method logic within REPORT material | 2 |
| report_internal_inconsistency | Conflicting REPORT attribution of a numeric result to outcome, time, population or comparison | 0 |
| protocol_report | Prospective PLAN versus REPORT statistical design or analysis element | 3 |
| plan_material | Statistical design inconsistency solely within PLAN material | 0 |
| **Total** | | **5** |

| Relationship type | Meaning | Candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 3 |
| P_P | PLAN versus PLAN | 0 |
| S_C | Two different REPORT documents | 0 |
| S_W | Within one REPORT document | 2 |
| **Total** | | **5** |

| Evidence state | Candidates |
|---|---:|
| reproduced | 5 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **5** |

Inclusion audits are CONFIRMED=5 and QUESTIONED=0. Relationships obey P_R > P_P > S_C > S_W precedence; corroborating context does not add a conflicting relationship. These classifications pre-fill human review and do not constitute adjudication.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001--day-7-respiratory-failure-absolute-difference-differs-within-the-main-report) | Repeated day-7 respiratory-failure absolute difference | statistical_results | S_W | reproduced | CONFIRMED |
| [C002](#c002--severe-acidosis-threshold-differs-between-plan-and-reported-reintubation-rule) | Severe-acidosis endpoint-rule threshold | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#c003--icu-mortality-comparison-is-planned-as-log-rank-and-reported-as-chi-square) | Planned/reported ICU mortality comparison | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#c004--prespecified-disease-and-weaning-test-primary-subgroup-results-are-absent) | Two planned primary subgroup factor families | protocol_report | P_R | reproduced | CONFIRMED |
| [C005](#c005--nonhypercapnic-day-90-mortality-absolute-difference-does-not-reconcile) | Subgroup mortality absolute-difference quantity | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Day-7 respiratory-failure absolute difference differs within the main report

**Pending Human Adjudication**

**Candidate statement:** The same overall day-7 respiratory-failure contrast is reported as −8.7 percentage points in the abstract/narrative and −8.5 in Table 2.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main abstract and narrative vs REPORT main Table 2

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-001

**Classification rationale:** The conflicting effects are within one REPORT. Supplementary counts merely corroborate the endpoint; the P-value subpart was independently screened out and adds no S_C relationship.

**Classification ambiguity:** None

**Exact source locations:** Affected occurrences: [jama_thille_2019_oi_190108.pdf — p.1 abstract Results](<../jama_thille_2019_oi_190108.pdf#page=1>), [p.6 Secondary Outcomes](<../jama_thille_2019_oi_190108.pdf#page=6>) and [p.8 Table 2 respiratory-failure row/headings](<../jama_thille_2019_oi_190108.pdf#page=8>). Method context: [main p.4](<../jama_thille_2019_oi_190108.pdf#page=4>). Count corroboration: [joi190108supp2_prod.pdf — p.2 eTable 1](<../joi190108supp2_prod.pdf#page=2>), [p.6 eTable 3](<../joi190108supp2_prod.pdf#page=6>) and [p.7 eTable 4](<../joi190108supp2_prod.pdf#page=7>).

**Source evidence:** Abstract and narrative give intervention 21% versus control 29%, difference −8.7 (95% CI −15.2 to −1.8), P=.01. Table 2 gives 70/339 versus 88/302, difference −8.5 with the same interval and P value. Supplementary stratum counts sum to those table events and denominators.

**Reported-versus-comparator:** Matched reported effect −8.7 in two prose locations versus −8.5 in the same article's table. This candidate concerns the risk difference only.

**Reasoning procedure:** Match endpoint, population, day, arm direction and interval across all three locations; compare the two printed effect intervals under half-unit display precision. Use the event-fraction calculation as corroboration without assuming a separate modeled estimate must be crude.

**Calculation:** 100 × (70/339 − 88/302) = −8.4901052961 percentage points. The printed-effect intervals [−8.75, −8.65] and [−8.55, −8.45] are disjoint. Supplementary events are 14+56=70 and 24+64=88; denominators are 63+276=339 and 48+254=302.

**Affected result or extracted value:** Overall day-7 postextubation respiratory-failure absolute treatment difference, an abstract-reported key secondary result.

**Why context does not resolve it:** Both effects are unqualified and identify the same endpoint, day, population and interval. No distinct estimator or denominator explains the repeated narrative effect. Counts support the table arithmetic but do not identify how the narrative value was generated.

**Alternative source-grounded interpretations:** An unlabelled narrative calculation or reporting transcription could explain the difference; the package establishes neither. An explicitly distinct modeled estimate, if documented, would require its own interpretation.

**Mechanical evidence recheck:** The independent rechecker confirmed all three printed effects using direct PDF layout text and source-derived images; no location or transcription correction was required. Its reproduced state concerns the disjoint repeated-effect values, with supplementary content serving as corroboration. The independent audit confirmed this bounded scope.

**Potential downstream evidence impact:** An extractor could copy −8.7 from the abstract or −8.5 from the table as the overall absolute effect. This identifies a possible extraction choice; no propagation or trial-conclusion change is established.

**Human verification steps:** Compare all three affected occurrences and establish the intended estimator, denominator and source calculation for each. Keep the independently screened P-value comparison outside this candidate.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Severe-acidosis threshold differs between plan and reported reintubation rule

**Pending Human Adjudication**

**Candidate statement:** The acidosis component of the two-component severe respiratory-failure rule uses pH<7.35 in the plan and pH<7.25 in the report, each with PaCO2>45 mm Hg.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol severe-reintubation definition vs REPORT main Outcomes definition

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-005

**Classification rationale:** A prospective PLAN operational decision rule is compared with a REPORT definition underlying the primary reintubation endpoint.

**Classification ambiguity:** No role ambiguity; no separate applicable amendment is supplied.

**Exact source locations:** Core comparison: [joi190108supp1_prod.pdf — p.30 section 5.4 start](<../joi190108supp1_prod.pdf#page=30>), [p.31 severe-rule continuation](<../joi190108supp1_prod.pdf#page=31>) and [jama_thille_2019_oi_190108.pdf — p.4 Outcomes](<../jama_thille_2019_oi_190108.pdf#page=4>). Affected endpoint context: [main p.8 Table 2 primary row](<../jama_thille_2019_oi_190108.pdf#page=8>). Corroborating criterion counts: [joi190108supp2_prod.pdf — p.2 eTable 1](<../joi190108supp2_prod.pdf#page=2>).

**Source evidence:** Both severe respiratory-failure definitions require at least two qualifying components. The corresponding acidosis item is pH<7.35 with PaCO2>45 in the plan and pH<7.25 with PaCO2>45 in the report. The separately defined secondary respiratory-failure rule uses pH<7.35 in both sources. Primary day-7 reintubation is 40/339 versus 55/302; supplementary severe-acidosis counts are 9 versus 12.

**Reported-versus-comparator:** Reported severe-rule pH<7.25 versus planned severe-rule pH<7.35, within the same two-component operational criterion.

**Reasoning procedure:** Read the protocol rule across its page break; distinguish severe reintubation from the separate secondary respiratory-failure definition; compare corresponding pH conditions while retaining the common PaCO2 requirement and other indications.

**Calculation:** With PaCO2>45, pH in [7.25, 7.35) satisfies the planned acidosis component but not the reported one. Exactly one other qualifying component, absent an independently sufficient indication, can distinguish the stated rule eligibility. This is a logical illustration, not an observed participant reclassification. Even permissive two-decimal rounding bands [7.345, 7.355] versus [7.245, 7.255] are disjoint.

**Affected result or extracted value:** Operational criterion underpinning primary day-7 reintubation (40/339 versus 55/302), and the endpoint definition copied with that result.

**Why context does not resolve it:** The severe cutoffs are explicit and differ from the separately identifiable secondary rule. Neither the immediate text nor the supplied criterion counts identify an applicable amendment or the cutoff implemented.

**Alternative source-grounded interpretations:** A later applicable amendment/SAP or a reporting transcription could explain the discrepancy. The supplied package establishes neither; criterion counts alone cannot quantify participants affected by either definition.

**Mechanical evidence recheck:** Direct source text and images confirmed the planned severe-rule cutoff across pp.30–31 and the reported cutoff on p.4. Corresponding content roles and P_R classification were confirmed without transcription correction. The final independent audit confirmed inclusion.

**Potential downstream evidence impact:** A reviewer could characterize the primary endpoint using either acidosis threshold, affecting the extracted decision-rule description or endpoint comparability. Actual event-count changes and clinical consequences are not established.

**Human verification steps:** Establish which dated operational cutoff governed primary reintubation decisions, and inspect any applicable amendment, SAP or reporting explanation. Participant-level simultaneous criteria would be required to assess actual recategorization; no preferred cutoff is proposed.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — ICU mortality comparison is planned as log-rank and reported as chi-square

**Pending Human Adjudication**

**Candidate statement:** The plan expressly includes ICU mortality in treatment-group Kaplan–Meier/log-rank comparisons, whereas the report assigns the abstract-reported ICU mortality result to chi-square and provides no separately identified ICU log-rank result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol ICU mortality treatment-comparison specification vs REPORT main ICU mortality methods and result

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Classification rationale:** Explicit PLAN and REPORT statistical specifications for the same key secondary outcome are compared; coherent distinct tests do not establish an explanation of the change.

**Classification ambiguity:** No role ambiguity; no separate applicable SAP or amendment is supplied.

**Exact source locations:** Core comparison: [joi190108supp1_prod.pdf — p.34 section 6.3](<../joi190108supp1_prod.pdf#page=34>) and [jama_thille_2019_oi_190108.pdf — p.4 Statistical Analysis](<../jama_thille_2019_oi_190108.pdf#page=4>). Matched result: [main p.1 abstract](<../jama_thille_2019_oi_190108.pdf#page=1>) and [p.8 Table 2 ICU mortality row](<../jama_thille_2019_oi_190108.pdf#page=8>). Distinct day-90 context: [joi190108supp2_prod.pdf — p.9 survival eFigure](<../joi190108supp2_prod.pdf#page=9>). Full main pp.1–11 and results pp.1–9 were assessed for ICU output availability, including [results p.1 contents](<../joi190108supp2_prod.pdf#page=1>).

**Source evidence:** The plan unconditionally lists ICU, hospital, day-28 and day-90 mortality in Kaplan–Meier/log-rank treatment comparisons. The report specifies chi-square for ICU/hospital mortality and reports ICU deaths 21/339 versus 26/302, difference −2.4 (95% CI −6.7 to 1.7), P=.25. Its separately labeled overall day-90 survival figure has log-rank P=.37.

**Reported-versus-comparator:** Reported ICU mortality chi-square comparison versus the explicit planned ICU mortality log-rank comparison. The day-90 figure concerns another endpoint/window and does not supply the ICU output.

**Reasoning procedure:** Match the unconditional prospective treatment-comparison sentence to the abstract-reported ICU outcome and its method. Inspect the complete supplied report inventory for a separately identified ICU survival comparison. Distinguish the subsequent conditional Cox passage from this commitment.

**Calculation:** Categorical specification comparison: planned ICU log-rank versus reported ICU chi-square. As context only, 100 × (21/339 − 26/302) = −2.4145812577 points, compatible with printed −2.4. Final death counts cannot reconstruct a log-rank statistic or P value without individual event and censoring times.

**Affected result or extracted value:** Analysis identity of the key-secondary ICU mortality P=.25 and availability of its specified log-rank comparison.

**Why context does not resolve it:** Distinct internally coherent tests do not explain the prospective versus reported ICU specification difference. The day-90 figure is expressly a different result; no applicable change explanation or ICU log-rank output is supplied.

**Alternative source-grounded interpretations:** An applicable later SAP may have amended the ICU comparison, or a retained ICU analysis may exist outside the supplied reporting. Neither possibility is established. Conditional Cox omissions do not enlarge this candidate.

**Mechanical evidence recheck:** Exact plan p.34 and report p.4 statements were confirmed; direct reading of all report pages and the source-derived day-90 figure confirmed the outcome distinction and supplied-output limitation. Roles, P_R classification and reproduced state required no correction. The independent audit confirmed the unconditional-only scope.

**Potential downstream evidence impact:** Evidence extraction could identify the ICU P=.25 as the prespecified mortality comparison without recording the method difference, or treat the day-90 curve as its output. The package does not establish changed mortality conclusions or any downstream use.

**Human verification steps:** Check the applicable ICU mortality analysis specification and locate its planned log-rank output or an amendment/reporting explanation. Recover event/censoring inputs only if numerical reconstruction is required; no alternative P value or preferred test is proposed.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Prespecified disease and weaning-test primary subgroup results are absent

**Pending Human Adjudication**

**Candidate statement:** The plan commits to primary-outcome subgroup analyses by underlying cardiac/respiratory disease and weaning-test type, but the complete supplied subgroup results cover PaCO2 only.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol primary-subgroup commitments vs REPORT supplied subgroup analysis set

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-004

**Classification rationale:** Two factors within the same repeated planned primary-analysis reporting pattern form one candidate. PLAN commitments are compared with REPORT analysis availability.

**Classification ambiguity:** No role ambiguity; a separate applicable SAP or amendment is not supplied.

**Exact source locations:** Commitment: [joi190108supp1_prod.pdf — p.34 section 6.4](<../joi190108supp1_prod.pdf#page=34>). Report methods/output: [jama_thille_2019_oi_190108.pdf — p.4 subgroup methods](<../jama_thille_2019_oi_190108.pdf#page=4>), [p.7 subgroup results](<../jama_thille_2019_oi_190108.pdf#page=7>), [p.8 Figure 3](<../jama_thille_2019_oi_190108.pdf#page=8>), [joi190108supp2_prod.pdf — p.1 contents](<../joi190108supp2_prod.pdf#page=1>), [p.6 eTable 3](<../joi190108supp2_prod.pdf#page=6>) and [p.7 eTable 4](<../joi190108supp2_prod.pdf#page=7>). Baseline corroboration: [main p.5](<../jama_thille_2019_oi_190108.pdf#page=5>), [main p.6 continued Table 1](<../jama_thille_2019_oi_190108.pdf#page=6>), [results p.3](<../joi190108supp2_prod.pdf#page=3>), [p.4](<../joi190108supp2_prod.pdf#page=4>) and [p.5](<../joi190108supp2_prod.pdf#page=5>). Complete main pp.1–11/results pp.1–9 were assessed for both absent families.

**Source evidence:** The protocol specifies main/secondary outcome subgroup analyses for underlying cardiac/respiratory disease and for T-piece versus minimum pressure-support weaning test, in addition to PaCO2. The supplied primary subgroup methods/results concern PaCO2: interaction P=.25, with primary differences −12.9 and −5.0. Disease/weaning baseline descriptors and disease covariate adjustment provide no matching subgroup treatment effects.

**Reported-versus-comparator:** Prospective primary subgroup set includes PaCO2, disease and weaning-test families; the supplied primary subgroup output set includes PaCO2 only.

**Reasoning procedure:** Identify explicit primary-outcome subgroup commitments, inventory all supplied subgroup methods/tables/figures, and distinguish descriptive factor counts and overall covariate adjustment from subgroup outcome contrasts. Consolidate the two absent factor families as one reporting pattern.

**Calculation:** Set-membership comparison: the disease and weaning-test primary subgroup families are present in the plan and absent from the supplied outcome-output set. Rounding of existing PaCO2 estimates cannot create outputs for the two other families. Their numeric treatment effects or interactions cannot be recovered from baseline totals alone.

**Affected result or extracted value:** Completeness and prespecified interpretation of primary day-7 reintubation subgroup evidence by disease and weaning-test mode.

**Why context does not resolve it:** Explicit commitments to primary subgroup analyses have no corresponding supplied results or change explanation. Neither baseline factor rows nor overall disease adjustment identifies the intended subgroup effects or their availability.

**Alternative source-grounded interpretations:** An applicable SAP may have changed the subgroup set, or results may exist outside the supplied package. Neither is established. The exact disease partition—separate or combined cardiac/respiratory groups—is not fully specified by the supplied commitment. No subgroup heterogeneity or performed/unperformed analysis status is inferred.

**Mechanical evidence recheck:** Exact protocol p.34 and the entire main/results inventory were read directly and cross-checked against complete maps. Both factor families' supplied-output absence was confirmed without transcription correction. The independent audit retained one P_R candidate limited to the primary-outcome commitment.

**Potential downstream evidence impact:** An extractor could treat the PaCO2 analysis as the full prespecified primary subgroup set or lack the intended disease/weaning contrasts. This describes possible completeness and labeling consequences; no selective-analysis cause or downstream conclusion change is established.

**Human verification steps:** Establish whether both primary subgroup families were retained in the applicable SAP, clarify the intended disease partition, and locate their results or a reporting explanation. Keep non-key secondary subgroup omissions outside this candidate.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Nonhypercapnic day-90 mortality absolute difference does not reconcile

**Pending Human Adjudication**

**Candidate statement:** eTable 4 prints a mortality absolute difference of −3.8 percentage points with counts 54/254 and 50/276, whose stated proportion contrast is −3.14390049 points. The exact absolute-difference estimator is not identified; the reproduced issue is the quantity mapping to the displayed event fractions.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 4 counts and headings vs REPORT same-table absolute-difference entry

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002, F-ST1-002

**Classification rationale:** The quantity-identity discrepancy is within one REPORT table. It is not a peripheral cross-location subgroup comparison, and no adjusted day-90 mortality estimator is identified.

**Classification ambiguity:** None

**Exact source locations:** Core: [joi190108supp2_prod.pdf — p.7 eTable 4 population headings and mortality-at-day-90 row](<../joi190108supp2_prod.pdf#page=7>). Local corroboration: [same p.7 day-7 reintubation and hospital-mortality rows](<../joi190108supp2_prod.pdf#page=7>). Method context: [jama_thille_2019_oi_190108.pdf — p.4 Statistical Analysis](<../jama_thille_2019_oi_190108.pdf#page=4>).

**Source evidence:** Nonhypercapnic control n=254 has 54 deaths (21%); intervention n=276 has 50 (18%). The row prints absolute difference −3.8 (95% CI −9.9 to 3.6), P=.3626. Neighboring binary rows follow intervention-minus-control event proportions. The main adjusted logistic specifications concern primary reintubation; a distinct adjusted nonhypercapnic day-90 mortality difference is not locally identified.

**Reported-versus-comparator:** Printed absolute difference −3.8 versus the displayed-fraction intervention-minus-control contrast −3.1439004907 percentage points. The source does not explicitly name the absolute-difference estimator, so this comparison does not establish that every possible modeled estimate must equal the crude fraction difference.

**Reasoning procedure:** Match subgroup, arm headings, denominators and mortality time point; identify the table's local binary-difference convention; compute the displayed event-proportion difference and apply exact and conservatively permissive half-unit input bounds. Retain estimator identity as a human question.

**Calculation:** Exact printed fractions give 100 × (50/276 − 54/254) = −3.1439004907 points. Printed −3.8 permits [−3.85, −3.75]. Even allowing continuous half-unit bands for all four integers gives a minimum 100 × (49.5/276.5 − 54.5/253.5) = −3.5966629930 and maximum 100 × (50.5/275.5 − 53.5/254.5) = −2.6913024720; that entire range is disjoint from the printed-effect band. Coarse percentages alone are less informative than the supplied counts. Neighboring day-7 and hospital-mortality fractions give −5.0353760128 and 1.3123359580, rounding to printed −5.0 and 1.3. No CI-symmetry or P-value incompatibility claim is used.

**Affected result or extracted value:** Nonhypercapnic day-90 mortality absolute effect extracted from eTable 4.

**Why context does not resolve it:** Counts/headings and the unqualified difference column yield distinct quantities beyond display precision, while no alternate population, denominator or estimator identifies how −3.8 was generated. The overall day-90 survival analysis is not linked to this subgroup effect entry.

**Alternative source-grounded interpretations:** An unlabelled adjusted or survival-based estimator, alternative denominator, or reporting transcription could explain the difference if documented. No explanation is established. If a distinct modeled estimator is established, the human can reconsider the displayed-fraction mapping; no numerical replacement or preferred method is prescribed.

**Mechanical evidence recheck:** Direct source p.7 confirmed all headings, counts and the printed −3.8; exact and conservative half-unit arithmetic reproduced non-reconciliation. Roles and S_W classification required no correction. The reproduced state records the displayed-quantity comparison, not proof of an undisclosed estimator's identity. The independent audit confirmed this limitation explicitly.

**Potential downstream evidence impact:** An extractor could copy −3.8 as a proportion-based absolute effect or recompute approximately −3.14 from the printed fractions, yielding distinct extracted quantities. No changed nonsignificance conclusion or actual evidence-synthesis consequence is established.

**Human verification steps:** Establish the estimator, population, denominators and any adjustment/censoring underlying −3.8, then document its relationship to the displayed 54/254 and 50/276. Obtain exact CI/test settings if needed for further reconstruction.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

A systematic review, meta-analysis, guideline or structured evidence table may copy effect estimates, endpoint definitions, statistical-test identities and prespecified-analysis labels from different package locations. If a candidate is confirmed by human adjudication, documenting the intended quantity and its provenance can make those extraction choices explicit. These cards identify possible reuse implications for named results. They do not establish that any candidate propagated, changed a conclusion or caused harm. Reported trial conclusions remain separate from extraction questions.

## Limitations and Missing Definitions

All supplied scientific source units were covered and all registered source locations were confirmed. The package does not supply the separately referenced applicable SAP or a reconciling amendment, raw participant data, full individual event/censoring times, exact confidence-interval algorithms, row-specific continuous estimators or model covariance/variance settings. One-hour contributor counts and some forced-covariate specifications are also unavailable. Diagnostic calculations were not substituted for unreported exact analyses.

Candidate-specific missing information comprises the narrative respiratory-failure estimator (C001), dated operational severe-acidosis rule and participant criteria (C002), ICU time-to-event output and its applicable specification (C003), disease/weaning primary subgroup outputs and disease partition (C004), and the nonhypercapnic day-90 absolute-difference estimator/population/denominator mapping (C005). These gaps limit causal explanation or numerical reconstruction, rather than supplied-source coverage.

Legacy rendered-page engine versions are incompletely recorded. Historical OCR gaps have usable companion text/images, and partial fresh protocol p.42 OCR was supplemented by complete visual mapping. No required direct-tool limitation remains. Absence from supplied reporting does not establish absence of performed work. See [Limitations record](review_1_6_1/limitations.md).

## Human Adjudication Checklist

For each stable ID, inspect every exact-source occurrence, distinguish the core comparison from corroborating context, verify the named calculation or prospective commitment, and establish any applicable estimator, operational rule, SAP or amendment. Assess whether the unresolved quantity bears on interpretation or extraction under the stated scope. Record the human decisions only in Validity, Importance, Action, Initials and Notes; these fields currently contain `__` for all five cards. No candidate is pre-adjudicated by a reproduced evidence state or a CONFIRMED inclusion audit.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The durable records are [Candidate ledger](review_1_6_1/candidate_ledger.md), [Mechanical recheck](review_1_6_1/verification/evidence_recheck.md), [Evidence-quality audit](review_1_6_1/quality/evidence_quality_audit.md), [Coverage/provenance audit](review_1_6_1/quality/coverage_integrity_audit.md), [Routing preflight](review_1_6_1/routing_preflight.md), [Tooling record](review_1_6_1/tooling_record.md) and [Execution manifest](review_1_6_1/agent_execution_manifest.md). All five stable IDs occur in the ledger, recheck, inclusion audit and this report.

Routing preflight records PASS, coordinator gpt-6.1-sol/high, ordinary specialists medium, statistical/screening/recheck/audit specialists high, all ten named presets verified, Coordinator inference: PASS, execution mode INTERACTIVE_CLI and Provider: CURRENT_SESSION. No provider credentials or configuration changes are part of the evidence package.

Direct local CPU tools include Poppler 26.01.0, Tesseract 5.5.0 and Pandoc 3.7.0.2. No fallback environment was needed or created. Twenty-five current-run derivatives are individually recorded with producing stage/source/engine: support mapping 3, cross-source review 8, statistical pass 1 six, mechanical recheck 8. Sources and reused assets were preserved. The completed independent integrity audit confirmed 4/4 source and 128/128 reused-artifact hashes unchanged against their before manifests. Final coordinator recomputation confirmed that all after hashes match their before manifests.

The standalone HTML is rendered from finalized Markdown with embedded CSS and a table of contents. The mechanical completion result is recorded at `review_1_6_1/review_validation.json`.

### Complete agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a128da-3b69-7bb0-9554-2128186ea149 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a128da-f857-7961-9e0d-1495d8ad392c | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a128dc-ff7f-7141-8b09-40baa2432582 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a128dd-1b8f-7d40-98dd-4089fca540b7 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a128e0-6129-7883-87fc-83aefc195357 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a128e0-7bc2-7152-a260-a42c4a4fcd31 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a128e0-9c6c-75b0-bd7b-a4d7840873d2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a128e8-3ee6-74b0-9150-548d0b31afea | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a128ec-690f-7e03-a5dc-029f8535c3c2 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a128f0-78bd-77c1-be66-4735054846bc | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_coverage_auditor | 01a128f4-fe55-7b90-9ca7-0485ea5d80b0 | gpt-6.1-sol | high | FRESH_SPAWN | quality/coverage_integrity_audit.md |
| quality_control_auditor | 01a128f5-2ac8-7143-95a3-8ab7bc6b3e85 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a128f9-2907-7943-8fb5-26efdedbd5f0 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

All 13 actual runtimes are recorded once: the coordinator, eleven mandatory fresh specialist stages and one additional disjoint coverage/provenance audit shard. The two final audit scopes were split by the documented context bound; the mandatory auditor integrated the sibling's durable result. Every specialist retains its configured fixed model/effort and starts FRESH_SPAWN; no earlier agent was promoted to another mandatory stage.

### Reproducibility performance

- **Target basis:** Four PDFs contain 69 pages, including an 11-page report, 48-page protocol, 9-page results supplement, and 1-page administrative statement. Reusable text covers 68 pages; one image-only protocol appendix needs rendering and visual mapping. No Office conversion, full-document OCR, or fallback setup is needed. Eight sequential review waves with parallel mapping and three concurrent checkers determine the 25-40 minute planning range.
- **Total source units:** 69
- **Fresh-source units:** 1
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T02:46:34Z
- **Finished UTC:** 2026-10-11T03:24:47Z
- **Observed elapsed minutes:** 38.217
- **Target status:** MET_TARGET
- **Exceedance causes:** None

These exact performance fields were finalized immediately after complete Markdown assembly. Local HTML rendering and mechanical validation are excluded from review duration. The planning target did not constrain source coverage, relationship review, screening or the stable candidate set.
