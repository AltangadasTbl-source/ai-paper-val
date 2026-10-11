# Quantitative Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication.** Every candidate below is a candidate reporting issue. Evidence states and inclusion-audit records describe the review evidence; they are not human adjudications.

## Executive Quality-Control Summary

Complete review of the supplied STOP-PD II package identified **5 stable candidates**, C001, C002, C003, C004 and C005. All five concern printed comparisons between prospective plan material and reporting material and belong to `protocol_report`. Their evidence states are `reproduced`; their inclusion audits are `CONFIRMED`. Two qualify through Route A, category 5, and three through Route B.

The candidates concern a primary-relapse score condition, four absent prespecified key-secondary counterparts consolidated as one pattern, adverse-event baseline eligibility, safety treatment classification, and placement of a planned metabolic observation exclusion. The package establishes these reporting comparisons but does not establish changed participant classifications, numerical estimates, or conclusions. All 63 supplied pages, 127 numeric relationships and 70 statistical relationships were covered. Both distinct statistical passes covered every registered statistical relationship.

## Package and Reused-Evidence Provenance

Document roles follow content. The main article and non-plan supplements are REPORT; the protocol/analytic-plan/pharmacotherapy bundle is PLAN.

| Source ID | Actual supplied filename and opening page | Role | PDF pages |
|---|---|---|---:|
| DOC-001 | [jama_flint_2019_oi_190079.pdf](<../jama_flint_2019_oi_190079.pdf#page=1>) | REPORT | 10 |
| DOC-002 | [joi190079supp1_prod.pdf](<../joi190079supp1_prod.pdf#page=1>) | PLAN | 42 |
| DOC-003 | [joi190079supp2_prod.pdf](<../joi190079supp2_prod.pdf#page=1>) | REPORT | 10 |
| DOC-004 | [joi190079supp3_prod.pdf](<../joi190079supp3_prod.pdf#page=1>) | REPORT | 1 |
| Total | Four direct sources | | 63 |

The [source inventory](review_1_6_2/source_inventory.md) and [evidence asset inventory](review_1_6_2/evidence_asset_inventory.md) document 194 hashed reusable assets: 171 USABLE, 22 PARTIAL and 1 DUPLICATE. No STALE or UNREADABLE asset was recorded. Partial plot text is paired with usable full-page images; duplicate derivatives do not increase unique-page coverage. Assets include source identities, page maps, native/layout text, normalized text, OCR and rendered pages. No supplied Office, workbook or CSV source was found.

Historical PyMuPDF and rapidocr_onnxruntime/rapidocr-cuda provenance is retained as historical metadata. This run used direct Poppler text/layout extraction and targeted CPU page rendering, with no new OCR. Historical GPU provenance does not describe processing in this run. Derivatives were locators and transcription aids; the evidence rechecker visually read exact source-derived pages. Discovery and classification were rebuilt from supplied-source evidence, without using legacy candidate or adjudication conclusions as discovery inputs.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; source-grounded statistical method logic; and planned versus reported statistical design. It is quantitative reporting quality control. The [source coverage record](review_1_6_2/source_coverage.md) closes every direct-source partition:

| Source ID | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 42 | 42 | 0 | 42 | COMPLETE |
| DOC-003 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| Total | 63 | 63 | 0 | 63 | COMPLETE |

Zero fresh-required units means that usable source-matched extraction already covered every page. Fresh scientific mapping still covered every page. The main map covers abstract, Key Points, narrative, five tables, two figures, captions, footnotes and end matter. Support mapping covers the entire plan and appendix, all nine supplementary plots and the administrative data-sharing page. Bibliography and administrative units have explicit applicability records. Missing reusable page images were supplemented by usable text and targeted current source renders where visual confirmation was needed; no scientific source-unit gap remains.

The review excludes broad methodology, clinical, novelty, misconduct and raw-data audits and does not propose a preferred analysis. Context-resolved wording and notation, model-based versus crude comparisons, display precision, conditional unreported details, peripheral cross-document comparisons and out-of-focus observations were handled under the stated inclusion scope. No candidate was selected by a count target. Complete assignments and durable outputs are recorded in the [coverage manifest](review_1_6_2/coverage_manifest.md).

## Quantitative and Statistical Relationship Coverage

| Scope | Numeric relationships | Statistical relationships | Completion |
|---|---:|---:|---|
| Main article | 79 | 39 | Complete |
| Plan core | 22 | 18 | Complete |
| Plan appendix | 26 | 4 | Complete |
| Nine supplementary plots | Cross-referenced to main outcomes | 9 | Complete |
| Total | 127 | 70 | Complete |

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) and [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) retain complete source relationships. Allocated ID-block gaps are preserved assignment boundaries. Table 4 paired-change rows and all four Table 5 contrasts are explicitly covered rather than replaced by marginal-mean or crude reconstructions.

Fresh, distinct gpt-6.1-sol/high agents `root/statistics_pass_one` and `root/statistics_pass_two` each covered all 70 statistical relationships. Every inventory row records `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. Pass 2 also reread all five candidates, 13 screening decisions, recheck facts and all 37 checker exclusions. It emitted no new finding. The independent audit found no additional finding or screening reversal. Exact fitted-model reconstruction remained bounded by the missing inputs listed below; diagnostic calculations did not replace the reported analyses.

## Inclusion Screening Summary

A candidate requires reproduction and either an always-register Route A category or all three Route B criteria: in focus, not resolved by immediate context, and bearing on interpretation or extraction of a named result. For applicable numeric comparisons, half-unit rounding intervals and the relative-discrepancy threshold of 0.05 govern reproduction; interval-versus-test conflicts are always registered when reproduced.

The [independent screening log](review_1_6_2/screening/inclusion_screen.md) contains **13 finding decisions: 10 INCLUDE and 3 SCREENED_OUT**. The 10 included finding rows consolidate into **5 stable issues**. They retain every included finding ID.

| Decision | Reason code | Finding rows |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 10 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 3 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |
| Total | | 13 |

| Checker | Findings screened | INCLUDE | SCREENED_OUT |
|---|---:|---:|---:|
| Numeric consistency | 2 | 0 | 2 |
| Cross-source consistency | 5 | 5 | 0 |
| Statistical pass 1 | 6 | 5 | 1 |
| Total | 13 | 10 | 3 |

The peripheral decisions concern recruitment projections, historical relapse-denominator wording, and H3 open-label age-by-weight nonreporting. H3 is outside the article's Aims 1–2, is not in the abstract and is not designated key secondary; it is excluded from C002. These are finding-level screening decisions. Separately, the checkers self-screened **37 excluded-observation rows**: 13 numeric, 9 cross-source and 15 statistical. Pass 2 and audit revisited all 37 without new findings or reversals. These rows are not added to the denominator of 13 screened findings. No additional pass-2 screen was applicable because pass 2 emitted no finding.

## Review-Domain Summary

`statistical_results` covers report counts, estimates, intervals, tests and statistical methods. `report_internal_inconsistency` covers conflicting attribution of reported numbers to outcomes, times, populations or comparisons. `protocol_report` covers a statistical design or analysis comparison between PLAN and REPORT. `plan_material` covers inconsistent statistical design elements solely within PLAN material. These are review categories, not adjudications.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 0 |
| report_internal_inconsistency | 0 |
| protocol_report | 5 |
| plan_material | 0 |
| Total | 5 |

| Relationship type | Stable candidates |
|---|---:|
| P_R | 5 |
| P_P | 0 |
| S_C | 0 |
| S_W | 0 |
| Total | 5 |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 5 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 5 |

Inclusion audits are CONFIRMED for 5 and QUESTIONED for 0. Qualifying routes are Route A, category 5 for 2 and Route B for 3. Each summary reconciles to the complete five-candidate set.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | Additional primary-relapse score condition | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | Four absent prespecified counterparts | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Adverse-event baseline eligibility | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | Safety treatment classification | protocol_report | P_R | reproduced | CONFIRMED |
| C005 | Principal versus sensitivity observation rule | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Primary relapse score component differs from the plan

**Pending Human Adjudication.**

**Candidate statement:** The report lists HDRS ≥18 as a sufficient primary-relapse score component, whereas the plan also requires a 5-point increase relative to RCT entry.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main p.4 primary relapse criteria vs PLAN protocol p.12 relapse definition

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-001

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective primary endpoint definition is compared directly with the reported sufficient-condition list. P_R is the only conflicting relationship and determines protocol_report. Agreeing report result copies are affected outputs and do not add another relationship.

**Classification ambiguity:** None as to document roles; operational abbreviation or an unprovided amendment remains possible.

**Exact source locations:** PLAN [joi190079supp1_prod.pdf — PDF p.12, §3.9.8, lines 553–568](<../joi190079supp1_prod.pdf#page=12>); REPORT [jama_flint_2019_oi_190079.pdf — PDF p.4, Primary Outcome: Relapse](<../jama_flint_2019_oi_190079.pdf#page=4>). Affected outputs and context: [main PDF p.1, abstract](<../jama_flint_2019_oi_190079.pdf#page=1>), [main PDF p.6, primary results](<../jama_flint_2019_oi_190079.pdf#page=6>) and [main PDF p.7, Table 3 and footnotes](<../jama_flint_2019_oi_190079.pdf#page=7>).

**Source evidence:** The PLAN score route requires 17-item HAM-D ≥18 and a mean absolute increase of 5 points on at least one visit relative to RCT entry. REPORT p.4 requires at least one listed relapse criterion and lists 17-item HDRS 18 or higher without that conjunction. HAM-D/HDRS refers to the same instrument in this context. The psychiatric-hospitalization causes reconcile through Table 3's footnote; the SADS confirmation is operational context and does not support an additional candidate.

**Reported-versus-comparator:** REPORT score threshold alone versus PLAN score threshold plus the additional increase condition. The issue is the printed score component, not disagreement among the reported event-count or HR copies.

**Reasoning procedure:** Match phase, instrument and primary composite; compare the sufficient conditions; distinguish the disputed score route from the other composite routes. Retain the source's additional conjunction without assuming its averaging convention or changing any observed event classification.

**Calculation:** Hypothetical diagnostic illustration only: RCT-entry score 15 followed by 18 gives 18−15=3, which meets the printed report threshold but not the plan's additional 5-point increase. Another composite route could still establish relapse. This is not an observed participant. Display-precision intervals and relative discrepancy are not applicable to the presence of an exact decision-rule conjunction.

**Affected result or extracted value:** The primary-relapse composite underlying 13/64 versus 34/62 events and adjusted HR 0.25 (95% CI 0.13–0.48).

**Why context does not resolve it:** Route A, category 5 covers a changed printed primary composite definition, including when an unchanged operational rule may have been abbreviated.

**Alternative source-grounded interpretations:** The report may abbreviate an unchanged operational rule, or an unprovided amendment may have changed the score component. The supplied package establishes neither explanation.

**Mechanical evidence recheck:** Every cited location and both printed definitions were found and visually matched. The conjunction comparison reproduced after source confirmation of ≥18. Hospitalization causes were reconciled, with no registration transcription or classification correction. Operational classification instructions, endpoint amendments, participant entry/follow-up scores and component-specific relapse assignments are unavailable; the phrase mean absolute increase is not further operationalized. The reproduced evidence concerns printed specifications, not actual event reclassification.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a score-only relapse definition for the reported counts and HR rather than the planned conjunctive definition. The supplied package does not establish altered counts, HR, or conclusions.

## C002 — Four prespecified key secondary counterparts are absent

**Pending Human Adjudication.**

**Candidate statement:** The supplied reporting record has no counterpart for the planned HOMA glycemic measure, separate BMI alternative analysis, depression-related-weight-loss analysis or Intent-to-Attend treatment-effect comparison associated with the reported key secondary weight/metabolic outcomes.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main/supplement key secondary analysis record vs PLAN protocol pp.10,14,16 specifications

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-XS-004, F-ST1-002, F-ST1-006

**Qualifying route:** Route A, category 5

**Classification rationale:** Explicit prospective specifications are compared with the complete supplied REPORT record. P_R is the only conflict. The report documents agree on result scope; PLAN p.14 corroborates the identity of insulin resistance without creating a plan-internal conflict or expanding the issue to exploratory aims.

**Classification ambiguity:** Scope is limited to Aims 1–2 and their reported key secondary outcomes. Unprovided outcome results, scope decisions or amendments could explain the bounded absence.

**Exact source locations:** PLAN [joi190079supp1_prod.pdf — PDF p.10, lines 473–488](<../joi190079supp1_prod.pdf#page=10>), [PLAN PDF p.14, analysis context](<../joi190079supp1_prod.pdf#page=14>) and [PLAN PDF p.16, Strategies for Attrition, lines 769–772](<../joi190079supp1_prod.pdf#page=16>). The complete supplied REPORT absence-check union is listed page by page below; every linked page was inspected in the mechanical recheck.

| REPORT source page | Content and comparison purpose |
|---|---|
| [jama_flint_2019_oi_190079.pdf — PDF p.1](<../jama_flint_2019_oi_190079.pdf#page=1>) | Abstract and eight headline secondary effects |
| [main PDF p.2](<../jama_flint_2019_oi_190079.pdf#page=2>) | Key Points and explicit Aims 1–2 scope |
| [main PDF p.3](<../jama_flint_2019_oi_190079.pdf#page=3>) | Participant flow and methods |
| [main PDF p.4](<../jama_flint_2019_oi_190079.pdf#page=4>) | Outcome collection and model definitions |
| [main PDF p.5](<../jama_flint_2019_oi_190079.pdf#page=5>) | Premorbid-weight description and missingness/sensitivity methods |
| [main PDF p.6](<../jama_flint_2019_oi_190079.pdf#page=6>) | Primary results and safety/multiplicity context |
| [main PDF p.7](<../jama_flint_2019_oi_190079.pdf#page=7>) | Secondary effects and tolerability results |
| [main PDF p.8](<../jama_flint_2019_oi_190079.pdf#page=8>) | Table 4 and discussion |
| [main PDF p.9](<../jama_flint_2019_oi_190079.pdf#page=9>) | Table 5, limitations and conclusion |
| [main PDF p.10](<../jama_flint_2019_oi_190079.pdf#page=10>) | End matter and references |
| [joi190079supp2_prod.pdf — PDF p.1](<../joi190079supp2_prod.pdf#page=1>) | Complete eFigure index |
| [results supplement PDF p.2](<../joi190079supp2_prod.pdf#page=2>) | Weight model means |
| [results supplement PDF p.3](<../joi190079supp2_prod.pdf#page=3>) | Waist model means |
| [results supplement PDF p.4](<../joi190079supp2_prod.pdf#page=4>) | Total-cholesterol model means |
| [results supplement PDF p.5](<../joi190079supp2_prod.pdf#page=5>) | LDL model means |
| [results supplement PDF p.6](<../joi190079supp2_prod.pdf#page=6>) | HDL model means |
| [results supplement PDF p.7](<../joi190079supp2_prod.pdf#page=7>) | Triglyceride pattern-mixture means |
| [results supplement PDF p.8](<../joi190079supp2_prod.pdf#page=8>) | Glucose model means |
| [results supplement PDF p.9](<../joi190079supp2_prod.pdf#page=9>) | HbA1c model means |
| [results supplement PDF p.10](<../joi190079supp2_prod.pdf#page=10>) | Simpson-Angus model means |
| [joi190079supp3_prod.pdf — PDF p.1](<../joi190079supp3_prod.pdf#page=1>) | Administrative data-sharing statement |

**Source evidence:** PLAN p.10 designates HOMA as the primary glycemic-function measure, separately specifies BMI and waist as alternative analyses, and specifies a secondary weight-change analysis accounting for depression-related weight loss. PLAN p.16 specifies treatment-effect comparison with Intent-to-Attend models. The complete 21-page REPORT union contains related glucose/HbA1c, waist, premorbid-weight and pattern-mixture material but no counterpart for these four named measures or analyses.

**Reported-versus-comparator:**

| Planned counterpart | Related supplied report material | Distinction remaining |
|---|---|---|
| Primary glycemic HOMA measure | Glucose and HbA1c results | Neither is identified as HOMA/insulin resistance |
| Separate BMI alternative model | Weight and waist models | Waist does not supply the separately specified BMI model |
| Depression-related-weight-loss analysis | Descriptive premorbid weight and premorbid-reference adverse weight thresholds | These uses do not identify the specified longitudinal analysis or result |
| Intent-to-Attend treatment-effect comparison | Pattern-mixture investigations and triglyceride averaging | The other named attrition approach is not identified |

**Reasoning procedure:** Match each explicit PLAN specification to the reported Aims 1–2 outcomes; inspect the entire supplied REPORT union for a corresponding model/result; distinguish related measures and procedures from the named counterparts. Consolidate the repeated absence-of-counterpart pattern while retaining all four members. Keyword searches were locators; complete page inspection supplies the absence evidence.

**Calculation:** Four explicit planned counterparts versus zero matching counterparts in the complete supplied REPORT record. This is a logical presence/absence comparison, not a coefficient reconstruction. No rounding interval, numerical gap or relative discrepancy is defined for an absent outcome/model result.

**Affected result or extracted value:** The prespecified glycemic safety record and supporting analyses of abstract weight 0.13 lb/day, waist 0.009 in/day and the metabolic treatment-by-time effects.

**Why context does not resolve it:** Route A, category 5 covers planned primary or key secondary analyses not reported. The additional age/genetic aims and non-key H3 hypothesis are excluded from this candidate.

**Alternative source-grounded interpretations:** The counterparts may have been performed and reported elsewhere, deferred, unavailable or modified by an unprovided amendment. The report explicitly limits its aims, but no supplied location accounts for these four Aims 1–2 counterparts. Absence from this package does not establish nonperformance.

**Mechanical evidence recheck:** Every planned specification and all 21 supplied REPORT pages were directly inspected, including every plot title and the data-sharing statement. Each of the four absence comparisons reproduced independently; all related reported procedures were found and distinguished. No registration transcription or classification correction was needed. Missing inputs include the four outputs, amendments or scope explanations, and participant insulin/height/weight-loss/Intent-to-Attend data and model outputs. No missing coefficient or numerical consequence was inferred.

**Potential downstream evidence impact:** If confirmed, an extractor could treat the available glucose/HbA1c and weight/metabolic results as the complete prespecified record without identifying these missing counterparts. The review does not establish whether those analyses were performed elsewhere or whether their results would change any conclusion.

## C003 — Adverse-event baseline differs between plan and report

**Pending Human Adjudication.**

**Candidate statement:** The plan restricts phase-specific adverse-event incidence to participants not meeting the specified criteria at acute-phase baseline, while the report defines UKU increases and incident akathisia using randomized-phase baseline conditions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main pp.4,7 adverse-event criteria/results vs PLAN protocol p.15 safety baseline

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005

**Qualifying route:** Route B

**Classification rationale:** The comparison concerns a prospective safety-event eligibility rule and the reported event definition/results, so P_R determines protocol_report. Phase descriptions merely corroborate the distinct epochs and add no report-internal conflict.

**Classification ambiguity:** None as to roles; actual eligibility implementation and any effect on individual counts are unavailable.

**Exact source locations:** PLAN [joi190079supp1_prod.pdf — PDF p.15, Non-Metabolic Safety Data, lines 705–717](<../joi190079supp1_prod.pdf#page=15>); REPORT [jama_flint_2019_oi_190079.pdf — PDF p.4, Other Measures of Tolerability](<../jama_flint_2019_oi_190079.pdf#page=4>) and [main PDF p.7, adverse-effect/akathisia results](<../jama_flint_2019_oi_190079.pdf#page=7>). Phase context: [main PDF p.2](<../jama_flint_2019_oi_190079.pdf#page=2>) and [main PDF p.3](<../jama_flint_2019_oi_190079.pdf#page=3>).

**Source evidence:** The PLAN explicitly excludes participants meeting the adverse-event criteria at acute-phase baseline from phase-specific incidence eligibility. The REPORT explicitly identifies RCT-baseline conditions for UKU increase and incident Barnes akathisia. Acute entry precedes up to 12 weeks of acute treatment and 8 weeks of stabilization; RCT baseline follows these phases. The PLAN's generic UKU phrase from baseline does not independently identify an epoch and is not the comparison anchor. The score-4 wording supplies no separate issue.

**Reported-versus-comparator:** Explicit RCT-baseline reported conditions versus explicit acute-baseline planned incidence eligibility. The comparison does not assert a cross-arm percentage discrepancy.

**Reasoning procedure:** Match the planned safety incidence restriction with the report's UKU and Barnes definitions; identify the named epochs from trial-phase descriptions; retain the eligibility/reference distinction without assuming an epoch for generic baseline wording.

**Calculation:** A person can meet or cease to meet a criterion between acute entry and RCT entry; therefore absence of a criterion at these two epochs defines potentially different incidence eligibility. This is a logical possibility, not an observed reassignment. Participant trajectories and operational denominators are unavailable. Display-precision intervals cannot resolve a definition difference; no candidate numerical gap or relative discrepancy is defined.

**Affected result or extracted value:** UKU sleepiness/sedation 7.8%/3.2%, orthostatic dizziness 7.8%/3.2%, nausea/vomiting 3.1%/8.1%, and incident akathisia 4.7%/4.8%, for olanzapine/placebo respectively.

**Why context does not resolve it:** Focus D applies to the event/reference-population definition. Immediate context supplies no reconciliation of explicit acute-baseline eligibility with explicit RCT-baseline conditions. The named percentages could be interpreted as incidence in different eligible populations.

**Alternative source-grounded interpretations:** The report may intentionally describe randomized-phase emergent events, or an unprovided amendment may change the prospective rule. No preferred reference epoch is proposed.

**Mechanical evidence recheck:** Every location, both definite baseline statements and the affected incidence results were found and visually matched. UKU and akathisia were separately rechecked, and the logical epoch comparison reproduced without transcription/classification correction. Missing inputs are acute-entry, RCT-entry and follow-up UKU/Barnes observations, acute-baseline exclusions, operational denominators and safety-endpoint amendments. The recheck establishes printed definitions, not changed participant eligibility or counts.

**Potential downstream evidence impact:** If confirmed, an extractor could attach the printed percentages to an acute-baseline incident-event population or an RCT-baseline population. The supplied record does not quantify any actual difference between those populations or results.

## C004 — Safety treatment classification differs from the plan

**Pending Human Adjudication.**

**Candidate statement:** Planned safety models classify participants by medication taken during protocolized treatment, while explicit supplementary model-result titles identify randomized-group safety contrasts.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main/supplement randomized safety groups vs PLAN protocol pp.14,16 medications-taken classification

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route B

**Classification rationale:** A prospective safety treatment-group rule is compared with REPORT model-result group definitions/presentation. P_R determines protocol_report. The agreeing PLAN passages and corroborating main/supplement presentation do not create P_P or S_C conflicts.

**Classification ambiguity:** Actual operational treatment coding remains unspecified.

**Exact source locations:** PLAN [joi190079supp1_prod.pdf — PDF p.14, H2](<../joi190079supp1_prod.pdf#page=14>) and [PLAN PDF p.16, attrition/classification](<../joi190079supp1_prod.pdf#page=16>); REPORT [jama_flint_2019_oi_190079.pdf — PDF p.3, Figure 1](<../jama_flint_2019_oi_190079.pdf#page=3>), [main PDF p.4, Statistical Analyses](<../jama_flint_2019_oi_190079.pdf#page=4>), [main PDF p.7, secondary effects](<../jama_flint_2019_oi_190079.pdf#page=7>) and [main PDF p.8, Table 4](<../jama_flint_2019_oi_190079.pdf#page=8>). Every affected randomized-group model title is linked separately:

| Model result | Exact REPORT plot |
|---|---|
| Weight | [joi190079supp2_prod.pdf — PDF p.2, eFigure 1](<../joi190079supp2_prod.pdf#page=2>) |
| Waist | [results supplement PDF p.3, eFigure 2](<../joi190079supp2_prod.pdf#page=3>) |
| Total cholesterol | [results supplement PDF p.4, eFigure 3](<../joi190079supp2_prod.pdf#page=4>) |
| LDL cholesterol | [results supplement PDF p.5, eFigure 4](<../joi190079supp2_prod.pdf#page=5>) |
| HDL cholesterol | [results supplement PDF p.6, eFigure 5](<../joi190079supp2_prod.pdf#page=6>) |
| Triglycerides | [results supplement PDF p.7, eFigure 6](<../joi190079supp2_prod.pdf#page=7>) |
| Glucose | [results supplement PDF p.8, eFigure 7](<../joi190079supp2_prod.pdf#page=8>) |
| HbA1c | [results supplement PDF p.9, eFigure 8](<../joi190079supp2_prod.pdf#page=9>) |

**Source evidence:** Both PLAN passages specify safety classification based on medications taken during protocolized treatment, separately from primary H1 ITT. All eight supplementary model-result titles explicitly name randomized groups. REPORT p.4 includes all randomized participants, and Figure 1 documents departures from assigned treatment. All-randomized inclusion and Table 4 descriptive arm totals alone do not establish the model coding; the explicit model-result titles anchor the comparison.

**Reported-versus-comparator:** Randomized-group model means/contrasts versus medication-taken prospective classification. The supplied record does not identify a coding algorithm that reconciles them.

**Reasoning procedure:** Separate inclusion of participants from coding of treatment; compare explicit model-result group definitions with the planned classification rule; use Figure 1 only to establish that assignment and treatment exposure need not coincide. Do not impose fixed or time-varying grouping or infer which participants would be reclassified.

**Calculation:** Figure 1 reconciles exactly: 59+5=64 and 60+2=62; 3+2=5 and 1+1=2. These are contextual treatment-departure counts, not disputed counts. No assumption is made that all seven departures would be recoded or that they coincide with another sensitivity set. Display precision does not reconcile categorical group rules; no numerical discrepancy in model estimates is calculated.

**Affected result or extracted value:** The treatment contrast generating the eight headline anthropometric/metabolic interaction effects and plotted means, including weight 0.13 lb/day, waist 0.009 in/day and total cholesterol 0.29 mg/dL/day.

**Why context does not resolve it:** Focus D covers the safety group/contrast specification. The printed rules differ in a package with treatment departures, and immediate context supplies no treatment-coding rule. An extractor cannot determine whether the named effects represent randomized assignment or medication-taken classification from the supplied presentation alone.

**Alternative source-grounded interpretations:** Randomized labels may describe presentation while medications-taken coding was otherwise operationalized; later observations may have been excluded so analyzed exposures remained aligned; or randomized assignment may have been intentionally adopted. The supplied record does not distinguish these explanations.

**Mechanical evidence recheck:** Both prospective passages, all four main pages and all eight model-title pages were found and directly read. The grouping comparison reproduced without transcription/classification correction. Missing inputs include the medication-taken algorithm, medication-change timing, retained observations, fixed/time-varying coding, post-discontinuation/switch handling, actual design matrix and amendments. Reproduction concerns printed specifications/presentation, not proven coding or a coefficient change.

**Potential downstream evidence impact:** If confirmed, an extractor could classify the eight safety effects as assignment-based or exposure-based contrasts. No actual reclassification, numerical impact or conclusion change is demonstrated.

## C005 — Planned metabolic observation exclusion is placed in sensitivity analysis

**Pending Human Adjudication.**

**Candidate statement:** The plan places exclusion of post-hyperlipidemia-treatment observations within the H2 mixed model, while the report describes the corresponding operation within post hoc sensitivity analysis compared with all-participant analyses.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main pp.5,7 metabolic sensitivity analysis vs PLAN protocol p.14 principal observation rule

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-004

**Qualifying route:** Route B

**Classification rationale:** The prospective principal-model observation rule is compared with reported sensitivity methods/results. P_R determines protocol_report. The reported counterpart exists, so this is an analysis-role comparison rather than the absent-counterpart pattern in C002. Agreeing headline outputs add no S_W conflict.

**Classification ambiguity:** It is unspecified whether post hoc describes the entire exclusion operation or only its extension to hypoglycemic agents.

**Exact source locations:** PLAN [joi190079supp1_prod.pdf — PDF p.14, H2, lines 673–679](<../joi190079supp1_prod.pdf#page=14>); REPORT [jama_flint_2019_oi_190079.pdf — PDF p.1, abstract secondary effects](<../jama_flint_2019_oi_190079.pdf#page=1>), [main PDF p.5, final Statistical Analyses paragraph](<../jama_flint_2019_oi_190079.pdf#page=5>) and [main PDF p.7, secondary/drug-change results](<../jama_flint_2019_oi_190079.pdf#page=7>).

**Source evidence:** PLAN H2 states that pertinent later metabolic data will be excluded from the mixed model after hyperlipidemia treatment starts/changes, while collection continues for safety reporting. REPORT p.5 describes exclusion after statin or hypoglycemic starts/changes as post hoc sensitivity. REPORT p.7 calls those results qualitatively similar to analyses including all participants. The hypoglycemic extension is not asserted to have been planned.

**Reported-versus-comparator:** PLAN placement within the prospective H2 model versus REPORT placement within post hoc sensitivity. All participants does not establish that all later observations were included: earlier observations could retain participants even when later observations are excluded.

**Reasoning procedure:** Compare the analysis role of the stated exclusion; distinguish participant inclusion from observation retention and the planned hyperlipidemia rule from the additional hypoglycemic extension. Do not infer the principal model's observation set from qualitative similarity.

**Calculation:** Drug-change counts reconcile: 6+6=12 statin changes and 2+1=3 hypoglycemic-agent changes. These are context, not a numerical discrepancy. Separate principal/sensitivity coefficients and observation sets are unavailable; no coefficient difference, rounding interval or relative discrepancy can be calculated for the candidate.

**Affected result or extracted value:** The observation-selection rule and prespecification role underlying the headline cholesterol/triglyceride treatment-by-time effects, including total cholesterol 0.29 (95% CI 0.13–0.45) mg/dL/day and triglyceride −0.153 (95% CI −0.306–0.004) mg/dL/day.

**Why context does not resolve it:** Focus D covers the principal-model observation specification. Qualitative similarity does not identify which observation rule generated the principal coefficients or explain the printed principal-versus-sensitivity placement. This can affect extraction of the analysis role even without demonstrated numerical differences.

**Alternative source-grounded interpretations:** The principal model may retain the planned statin exclusion and post hoc may refer only to the hypoglycemic extension, with all participants represented by earlier observations. Alternatively, an unprovided amendment may move the entire operation to sensitivity analysis. The supplied wording does not distinguish these possibilities.

**Mechanical evidence recheck:** Every location and both placement statements were found and directly matched; the analysis-role comparison reproduced without transcription/classification correction. Missing inputs are the principal observation rule, removed outcome-specific measurements, separate model outputs, the intended breadth of post hoc and amendments. The recheck does not establish inclusion of all later observations or numerical impact.

**Potential downstream evidence impact:** If confirmed, an extractor could attribute the headline lipid effects to a different observation-selection rule or describe a planned principal operation as post hoc sensitivity. No actual change in coefficients or conclusions is established.

## Downstream Evidence-Chain Considerations

Evidence extraction commonly records endpoint definitions, incident-event populations, treatment contrasts, principal versus sensitivity analyses and the availability of prespecified outcomes alongside numerical effects. If a candidate is confirmed, its reporting ambiguity could affect one of those extracted fields. A review or synthesis could also reuse a printed effect with a definition or analysis role that the supplied record does not reconcile. These are potential uses of the reported evidence, not observations of actual propagation, changed conclusions or harm. This review supplies no substitute estimates or preferred analyses.

## Limitations and Missing Definitions

Complete coverage means that every supplied unit and registered relationship was reviewed; it does not mean that all underlying analyses can be independently recreated. The [limitations record](review_1_6_2/limitations.md) names these bounded reconstruction limits:

- Operational endpoint instructions, the averaging convention for the additional relapse-score rise, endpoint/safety amendments and participant component-specific relapse assignments are unavailable.
- The four C002 counterparts and their amendment/scope explanations are absent from this supplied reporting record. Participant insulin, height, depression-related-weight-loss and Intent-to-Attend data/model outputs are not supplied. Their absence does not establish that analyses were not performed elsewhere.
- Participant UKU/Barnes trajectories, acute-baseline eligibility exclusions and operational incidence denominators are unavailable, preventing event-count reconstruction under competing baseline definitions.
- Safety treatment-coding algorithms, medication/exposure timing, post-switch/discontinuation observation handling and fitted design matrices are unavailable. Randomized inclusion does not establish actual group coding.
- Principal versus sensitivity observation sets, outcome-specific drug-change exclusions and separate coefficients are unavailable. Inclusion of all participants does not establish inclusion of all measurements.
- Exact plot coordinates, numerical curves and shaded-band definitions are not supplied. Visual direction/label checks do not recreate exact estimates or contrast variances.
- Raw paired participant data, some Table 4 baseline contributor cells, survival event/censor times and fitted outputs are unavailable. Marginal summaries do not reconstruct paired changes or exact survival tests.
- Mixed/Poisson covariance matrices, test degrees of freedom, link/back-transformation details, exact contrasts and pattern-mixture weights are not supplied. Diagnostic approximations remain distinct from fitted-model reproduction.
- Full survival-power and repeated-measure simulation generators, replication counts and covariance inputs are not supplied. Diagnostic power checks cannot recreate the complete simulations.

No scientific source-unit coverage gap or missing-tool limitation remains. Undisclosed amendments and outputs outside this package are not inferred. The evidence supports printed comparisons and bounded supplied-record absence, not actual implementation changes, nonperformance or paper-level conclusion effects.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The run used only this package's supplied sources and local evidence. Routing preflight is PASS; run model is gpt-6.1-sol, run model source DEFAULT, execution mode INTERACTIVE_CLI, Provider CURRENT_SESSION and Coordinator inference PASS. All ten named presets were checked against their required model/effort pairs. Rendering/text processing used the CPU; direct pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract, libreoffice and pandoc were available. Fallback environment NOT_NEEDED; removal NOT_CREATED. No web or external literature was used.

The [before-source hashes](review_1_6_2/source_hashes_before.sha256) cover all four sources; [before-reuse hashes](review_1_6_2/reused_artifact_hashes_before.sha256) cover all 194 reused assets. The coverage auditor independently checked both sets without a mismatch. Final after-hash records, standalone HTML rendering and mechanical validation are coordinator completion steps after Markdown assembly. Supplied sources and reused artifacts remained read-only in report generation.

### Agent execution

The [execution manifest](review_1_6_2/agent_execution_manifest.md) records every actual agent, including optional bounded shards and this report generator. All specialists below started as FRESH_SPAWN; the coordinator uses CURRENT_SESSION. Distinct runtime IDs identify the two mandatory statistical passes and each other mandatory stage.

| Stage | Runtime agent ID | Model | Reasoning effort |
|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-6.1-sol | high |
| reuse_asset_curator | root/asset_curation | gpt-6.1-sol | medium |
| main_quantitative_mapper | root/main_mapping | gpt-6.1-sol | medium |
| support_quantitative_mapper | root/support_mapping | gpt-6.1-sol | medium |
| support_quantitative_mapper_shard_2 | root/support_appendix_mapping | gpt-6.1-sol | medium |
| numeric_consistency_reviewer | root/numeric_main_review | gpt-6.1-sol | medium |
| numeric_consistency_reviewer_support_shard | root/numeric_support_review | gpt-6.1-sol | medium |
| cross_source_consistency_reviewer | root/cross_source_review | gpt-6.1-sol | medium |
| statistics_pass_1 | root/statistics_pass_one | gpt-6.1-sol | high |
| inclusion_screener | root/initial_inclusion_screen | gpt-6.1-sol | high |
| evidence_rechecker | root/evidence_recheck | gpt-6.1-sol | high |
| statistics_pass_2 | root/statistics_pass_two | gpt-6.1-sol | high |
| quality_control_auditor | root/quality_inclusion_audit | gpt-6.1-sol | high |
| quality_control_auditor_coverage_shard | root/quality_coverage_audit | gpt-6.1-sol | high |
| report_generator | root/report_generation | gpt-6.1-sol | medium |

### Reproducibility performance

- **Target basis:** Four native-text PDFs contain 63 unique pages: a 10-page main article with several tables and a participant-flow figure, a 42-page protocol/analysis/pharmacotherapy bundle, a 10-page results supplement with nine plotted outcomes, and one administrative page. All 63 pages have source-matched reusable evidence, including images for the nine result plots; no Office conversion or fresh OCR is initially required. The target allows parallel main/support mapping, three checker lanes, independent screening, exact-source recheck, a distinct second statistical pass, audit and report generation; plot inspection and plan/report matching drive effort beyond page count.
- **Total source units:** 63
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T04:55:38Z
- **Finished UTC:** 2026-10-11T05:41:06Z
- **Observed elapsed minutes:** 45.47
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Exact-source recheck and evidence-card assembly across 26 visually inspected pages; context-bounded two-agent audit of all coverage and 37 excluded observations; sequential mandatory evidence, statistical, audit and report handoffs

Timing fields await coordinator finalization immediately after complete Markdown assembly. Local rendering and mechanical validation are outside the review window; a later model-assisted repair requires updated timing. The planning range does not limit source coverage, relationships or candidate cards.
