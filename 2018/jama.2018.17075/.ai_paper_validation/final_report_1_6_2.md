# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication.** Every stable candidate remains pending. Evidence states and inclusion-audit records describe the supplied-source review; they do not determine human adjudication.

## Executive Quality-Control Summary

Complete review of four supplied PDFs identified 15 stable candidate reporting issues, C001–C015. Fourteen have reproduced evidence and confirmed inclusion; C008 has not_reproduced evidence and QUESTIONED inclusion after the mandatory display-precision recheck. Its stable ID and historical registration remain visible. Seven candidates concern statistical results, seven concern planned versus reported statistical design, and one concerns plan-internal statistical design.

All 229 physical PDF pages were scientifically mapped. Numeric review covered 159 relationships; two distinct fresh statistical passes each covered all 369 statistical relationships. Independent screening recorded 28 findings: 15 INCLUDE and 13 SCREENED_OUT decisions. The complete candidate set follows below without selection by count. Potential relevance is confined to interpretation and evidence extraction from the supplied materials; no downstream propagation or conclusion change is established.

## Package and Reused-Evidence Provenance

The package contains the POLAR randomized-trial article and three supplied supplements. Direct sources are authoritative; source-linked extraction and page images served as locators and transcription aids. Fresh discovery used complete current-run maps rather than previous candidate decisions. SHA-256 identities and the reusable-asset inventory are recorded in [source hashes](review_1_6_2/source_hashes_before.sha256), [reused-artifact hashes](review_1_6_2/reused_artifact_hashes_before.sha256) and the [asset inventory](review_1_6_2/evidence_asset_inventory.md).

| Source ID | Actual supplied filename | Content role | Physical PDF pages |
|---|---|---|---:|
| DOC-001 | jama_cooper_2018_oi_180132.pdf | REPORT: trial article | 10 |
| DOC-002 | joi180132supp1_prod.pdf | Overall PLAN: original/final protocols, amendments, SAP updates and monitoring material | 194 |
| DOC-003 | joi180132supp2_prod.pdf | REPORT: supplementary results | 24 |
| DOC-004 | joi180132supp3_prod.pdf | REPORT: retrospective publication data-sharing statement | 1 |

Within DOC-002, observed DSMB result displays on physical pp.189–194 are REPORT content for location-specific classification; prospective stopping rules remain PLAN. Content determines roles. External protocol/SAP/charter pointer pages were covered as supplied; their linked documents were not fetched.

The 305 preserved reusable assets comprise eight whole-document native/layout files, 229 rendered pages, 50 metadata/text locators and 18 page-specific derivatives. Native text matched the current four PDFs; layout text matched three, with a vertical-axis placement difference in the article layout handled by source precedence. Reusable images cover all 30 plan pages without usable body text. Historical extraction/rendering engine versions are unspecified; current direct confirmation used Poppler 25.03.0 on CPU. Asset overlap does not increase unique page coverage.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators, estimate/test logic, statistical method logic, and planned versus reported statistical design under the supplied [quality-control scope](../QUALITY_CONTROL_SCOPE.md). Complete source-unit mapping includes cover, administrative, pointer, reference, scanned, table and figure pages. Reuse avoided unnecessary preprocessing and did not replace fresh scientific mapping.

| Source ID | Source path | Unit type | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---|---|---:|---:|---:|---:|---|
| DOC-001 | jama_cooper_2018_oi_180132.pdf | PDF_PAGE | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | joi180132supp1_prod.pdf | PDF_PAGE | 194 | 194 | 0 | 194 | COMPLETE |
| DOC-003 | joi180132supp2_prod.pdf | PDF_PAGE | 24 | 24 | 0 | 24 | COMPLETE |
| DOC-004 | joi180132supp3_prod.pdf | PDF_PAGE | 1 | 1 | 0 | 1 | COMPLETE |

No Office or CSV direct sources were supplied. No unresolved source-unit mapping gap remains. Boundaries exclude raw-data audit, broad clinical or methodological appraisal, novelty assessment and preferred-analysis recommendations. Display-zero P values alone, display-precision differences, immediately resolvable wording, model-versus-crude comparisons and peripheral comparisons were screened according to the normative scope.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains 159 relationships across all mapped report and plan materials. The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains 369 unique relationships: 95 main-report, 107 supplementary-report, 82 plan, and 85 observed-monitoring relationships. Every statistical relationship has explicit PASS_1_COMPLETE and PASS_2_COMPLETE records.

Pass 1 and pass 2 used different fresh gpt-6.1-sol/high agents, with disjoint context-bounded shards. Pass 2 reviewed the complete ledger, source rechecks and screening facts, and revisited all 59 checker excluded observations against always-register categories and the display-precision rule. It emitted one new included issue, C015. The subsequent independent quality audit covered all candidates, screening decisions, excluded observations, classification fields, source-unit coverage and execution records. Its two duplicate-provenance findings did not add stable candidates. Complete assignments and durable parts are retained in the [coverage manifest](review_1_6_2/coverage_manifest.md).

## Inclusion Screening Summary

Registration requires reproduction and either an always-register Route A category or all Route B criteria: in focus, unresolved by immediate context, and bearing on a named result's interpretation or extraction. Display-precision comparisons use half-unit input and output intervals, followed by the relative-discrepancy threshold. Assigned IDs remain visible when later recheck questions reproduction.

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 15 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 10 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 1 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 1 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 1 |
| **Total** | All decisions | **28** |

Initial screening covered 25 findings, with 14 INCLUDE and 11 SCREENED_OUT decisions. Pass-2 screening added one INCLUDE decision. Audit added two SCREENED_OUT/DUPLICATE_OF_INCLUDED findings. Thus 15 + 13 = 28, and all 15 INCLUDE rows map to the 15 stable IDs. Other screened-out reason codes have zero rows. Duplicate rows preserve provenance and locations without separate cards. The [single screening log](review_1_6_2/screening/inclusion_screen.md) preserves C008's historical INCLUDE; the current card separately reports its reconciled evidence and questioned inclusion.

## Review-Domain Summary

Domains describe reporting relationships: statistical_results covers numerical and statistical logic in report material; report_internal_inconsistency covers conflicting attribution of reported numbers to outcomes, times or populations; protocol_report covers report-versus-plan statistical design; plan_material covers plan-internal statistical design. Relationship precedence is P_R > P_P > S_C > S_W when more than one conflict is present. Corroboration alone adds no relationship.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 7 |
| report_internal_inconsistency | 0 |
| protocol_report | 7 |
| plan_material | 1 |
| **Total** | **15** |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 7 |
| P_P | PLAN versus PLAN | 1 |
| S_C | Between REPORT documents | 3 |
| S_W | Within one REPORT document | 4 |
| **Total** | | **15** |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 14 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 1 |
| **Total** | **15** |

The inclusion audit records 14 CONFIRMED and 1 QUESTIONED candidate. These records and evidence states are copied from the current ledger and do not replace human adjudication.

## Candidate Index

| ID | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| C001 | protocol_report | P_R | reproduced | CONFIRMED |
| C002 | statistical_results | S_W | reproduced | CONFIRMED |
| C003 | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | protocol_report | P_R | reproduced | CONFIRMED |
| C005 | protocol_report | P_R | reproduced | CONFIRMED |
| C006 | protocol_report | P_R | reproduced | CONFIRMED |
| C007 | statistical_results | S_C | reproduced | CONFIRMED |
| C008 | statistical_results | S_C | not_reproduced | QUESTIONED |
| C009 | protocol_report | P_R | reproduced | CONFIRMED |
| C010 | statistical_results | S_C | reproduced | CONFIRMED |
| C011 | plan_material | P_P | reproduced | CONFIRMED |
| C012 | statistical_results | S_W | reproduced | CONFIRMED |
| C013 | statistical_results | S_W | reproduced | CONFIRMED |
| C014 | statistical_results | S_W | reproduced | CONFIRMED |
| C015 | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Protocolized temperature-management window

**Status:** Pending Human Adjudication

**Candidate statement:** The reported seven-day temperature-management window does not identify how it relates to final-plan 96-hour device/pyrexia instructions and contemporaneous seven-day instructions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT DOC-001 pp.1,3 vs PLAN DOC-002 pp.77,89,101; PLAN final V9 sections compared

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-202

**Qualifying route:** Route B

**Classification rationale:** Confirmed. P_R takes precedence over the independent P_P component. These are intervention specifications in protocol material, and observed/published intervention descriptions in report material.

**Classification ambiguity:** The p.77 seven-day time origin and post-96-hour ordinary-care definition remain unspecified; role assignments are clear.

**Exact source locations:** Yes, at every registered location: REPORT [DOC-001 p.1, Interventions](../jama_cooper_2018_oi_180132.pdf#page=1) and [p.3, Rewarming and Normothermia](../jama_cooper_2018_oi_180132.pdf#page=3); PLAN [DOC-002 p.77, §12.11](../joi180132supp1_prod.pdf#page=77), [p.89, Appendix A events table](../joi180132supp1_prod.pdf#page=89), and [p.101, Appendix F infection/pyrexia instructions](../joi180132supp1_prod.pdf#page=101).

**Source evidence:** Yes. Abstract: temperature managed in both groups for seven days. Main p.3: after reaching 37°C, normothermic management using automated wraps if required for up to seven days postrandomization.

**Reported-versus-comparator:** Yes. Final V9 p.77: postrewarming normothermia with pads up to a maximum seven days or earlier ICU discharge; this sentence does not explicitly give the time origin. Control pyrexia prevention is up to 96 hours postrandomization, then unit protocol. Events table p.89 marks standard-care temperature-control device continuation through Day 7. Appendix p.101 gives normothermic pads for 96 hours postrandomization, then ward protocol, and pyrexia prevention in all patients up to 96 hours postrandomization, then unit protocol. These are distinct contemporaneous sections, rather than only historical versions.

**Reasoning procedure:** Yes. Focus D and Route B concern the assigned intervention/comparator duration. REPORT seven-day specification differs from PLAN 96-hour specification; PLAN event/detailed-section seven-day specifications differ from PLAN Appendix F 96-hour specification.

**Calculation:** Seven days = 168 hours. Conservatively allowing seven displayed days [6.5,7.5] gives [156,180] hours; 96 hours gives [95.5,96.5]. Gap 59.5 hours; relative discrepancy 59.5/96 = 0.61979. This is a comparison of specifications, not a claim about actual patient exposure. The seven-day hypothermia maximum itself reconciles and is context.

**Affected result or extracted value:** Assigned temperature-management/device-use duration for each randomized arm attached to the primary six-month favorable-GOSE comparison.

**Why context does not resolve it:** Optional pads, earlier ICU discharge and subsequent ward care do not define whether seven days and 96 hours describe the same arm-specific assigned management window. The final protocol retains both schedules without an explicit hierarchy.

**Alternative source-grounded interpretations:** Seven days may describe the full management window, with compulsory protocol measures ending at 96 hours and later measures supplied by routine care; pads are explicitly optional when required, and ICU discharge can shorten use. This does not define a common arm-specific device maximum across the compared statements.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. The direct PDFs retain seven-day and 96-hour specifications in the registered report and contemporaneous final-plan sections, separated beyond display precision. Necessary inputs: Yes for the textual/duration comparison. **Exact missing inputs or definitions:** Which section governed arm-specific device use, the seven-day time origin on p.77, and whether routine ward/unit management after 96 hours was intended to constitute the same assigned seven-day intervention. Actual device-use records are unavailable. Direct observation and inference: The competing printed schedules and events-table ticks are direct observations. A retained appendix from an earlier practice or a distinction between active device management and ordinary care is an unestablished explanation. No adherence consequence is inferred. See the complete durable [C001 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could record different assigned temperature-management durations for the randomized arms. Actual device exposure, adherence and outcome consequences are not established.

Checker provenance: Included finding F-ST1-202; duplicate findings F-XS-007. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C002 — Signed primary risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The abstract prints a positive primary risk difference of 0.4%, while the body and Table 2 print −0.4 percentage points for the same outcome, counts and confidence interval.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 abstract p.1 vs body p.5 and Table2 p.7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 2

**Classification rationale:** Confirmed. Every conflicting copy is in one published report; this concerns a signed estimate, so statistical_results applies.

**Classification ambiguity:** None.

**Exact source locations:** Yes: REPORT [DOC-001 p.1, abstract Results](../jama_cooper_2018_oi_180132.pdf#page=1), [p.5, Primary Outcome](../jama_cooper_2018_oi_180132.pdf#page=5), and [p.7, Table 2 primary row](../jama_cooper_2018_oi_180132.pdf#page=7).

**Source evidence:** Yes. Abstract prints risk difference 0.4%, CI −9.4% to 8.7%, RR 0.99, P=.94, with favorable counts 117 and 111.

**Reported-versus-comparator:** Yes. Body and Table 2 print −0.4 percentage points, identical interval −9.4 to8.7, with counts 117/240 and 111/226.

**Reasoning procedure:** Yes: focus B, Route A category 2, opposite signed readings of the same primary absolute effect.

**Calculation:** H−N = 100(117/240−111/226) = −0.36504425 percentage points. Positive0.4 interval [0.35,0.45] versus negative −0.4 interval [−0.45,−0.35] leaves gap 0.70; relative discrepancy 0.70/0.4=1.75. Count-derived intervals are unnecessary to establish the separated printed copies.

**Affected result or extracted value:** Signed primary absolute risk difference for favorable six-month GOSE, hypothermia versus normothermia.

**Why context does not resolve it:** Route A, category 2 applies to opposite printed signs changing the extracted effect direction; reconstructing a sign from counts does not remove the candidate.

**Alternative source-grounded interpretations:** Reverse contrast or absolute magnitude could account for positive 0.4. The unchanged asymmetric CI and RR below1 accompany the original H-versus-N contrast and do not define such a switch.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Fresh source renders show positive 0.4 in the abstract and negative −0.4 in both other copies, beyond precision. Necessary inputs: Yes. **Exact missing inputs or definitions:** Whether the abstract uses unsigned magnitude or an explicitly different contrast; neither is stated. Direct observation and inference: Three source signs, counts and intervals are direct observations. The origin of the sign difference is not established; no significance change is claimed. See the complete durable [C002 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could copy the positive abstract estimate or the negative body/table estimate as the signed primary effect. No significance or paper-level conclusion change is established.

Checker provenance: Included finding F-NUM-001; duplicate findings F-ST1-001, F-XS-001. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C003 — Cooling-duration anchor and late-cooling minimum

**Status:** Pending Human Adjudication

**Candidate statement:** The final protocol and report give different cooling-duration anchors, with further 72 hours after target attainment versus 72 hours after randomization and a conditional 48-hour late-cooling minimum.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT DOC-001 pp.3–4 vs PLAN DOC-002 pp.69,77,97,99; PLAN final V9 sections compared

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-201

**Qualifying route:** Route B

**Classification rationale:** Confirmed. Report-versus-plan and independent final-plan specification differences coexist, so P_R precedes P_P.

**Classification ambiguity:** Ideal-versus-operative wording and the conditional48-hour exception require interpretation; roles remain clear.

**Exact source locations:** Yes: REPORT [DOC-001 p.3, Maintenance/Rewarming](../jama_cooper_2018_oi_180132.pdf#page=3), [p.4, target-attainment results](../jama_cooper_2018_oi_180132.pdf#page=4); PLAN [DOC-002 p.69, §6.5](../joi180132supp1_prod.pdf#page=69), [p.77, §12.11](../joi180132supp1_prod.pdf#page=77), [p.97, §26.3.1](../joi180132supp1_prod.pdf#page=97), and [p.99, rewarming flowchart and late-start note](../joi180132supp1_prod.pdf#page=99).

**Source evidence:** Yes. Report maintains hypothermia for at least72 hours after randomization and assesses rewarming at 72 hours after randomization; maximum is seven days. Target attainment results show only 186 patients reached33°C and report injury-to33°C median10.1 hours; these are context, not individual duration arithmetic.

**Reported-versus-comparator:** Yes. Final synopsis p.69 reaches33°C then maintains for a further72 hours. Detailed p.77 assesses72 hours after randomization. Appendix p.97 says ideally72 hours after severe head injury. Flowchart p.99 uses72 hours postrandomization and requires at least48 hours of actual cooling before considering rewarming if cooling commenced late.

**Reasoning procedure:** Yes. Focus D, Route B: duration/time-origin specification for the randomized intervention. The synopsis's further72-hour target-temperature period differs from the detailed randomization-based rule plus late-start48-hour minimum. The latter minimum is conditional, so it is not asserted to apply to every patient.

**Calculation:** Nominal minima72 and 48 hours give intervals [71.5,72.5] and [47.5,48.5], gap 23 hours and relative 23/72=0.31944. Time origins differ logically even when the numeral72 matches. If target attainment occurs after randomization, attainment+72 and randomization+72 do not identify the same endpoint; source-level medians are not subtracted to estimate any individual's duration.

**Affected result or extracted value:** Assigned cooling dose, minimum duration and time origin for the primary favorable-GOSE comparison.

**Why context does not resolve it:** The final synopsis and operative flowchart do not specify how ideal target-temperature exposure, the randomization anchor and the conditional late-cooling rule are reconciled.

**Alternative source-grounded interpretations:** The synopsis may give an ideal target-temperature dose while the operational flowchart supplies clinically conditional implementation. That is possible, but it leaves the dose/time-origin extracted from the ordinary assigned intervention unspecified across final V9 and report.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. The final synopsis explicitly specifies a further72 hours after target attainment, while report/detailed plan and late-start flowchart explicitly use the other anchors/minimum. Necessary inputs: Yes for specifications. **Exact missing inputs or definitions:** Governing time origin, definition of actual cooling for the48-hour condition, and hierarchy among synopsis, detailed protocol and appendix. Patient-level target attainment, exceptions and exposure are unavailable. Direct observation and inference: Printed anchors,72-hour phrases and 48-hour note are direct. Actual shortening of individual cooling or its clinical consequences is not established. See the complete durable [C003 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could characterize the intervention using different cooling-duration anchors or minima. Individual exposure and neurological consequences are not established.

Checker provenance: Included finding F-ST1-201; duplicate findings F-XS-006. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C004 — Routine rewarming rate

**Status:** Pending Human Adjudication

**Candidate statement:** The report describes a routine rewarming target up to 0.25°C/h, while the final plan recommends an aim/maximum of approximately 0.17°C/h; the relationship between the ordinary specifications remains unclear.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 p.3 vs PLAN DOC-002 pp.77,99,100; PLAN p.21 historical context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-203

**Qualifying route:** Route B

**Classification rationale:** Confirmed. This concerns an intervention specification. The superseded0.25 historical plan does not add P_P.

**Classification ambiguity:** Recommended aim versus broad reported ceiling is explicitly retained; no rigid ban or actual rate violation is inferred.

**Exact source locations:** Yes: REPORT [DOC-001 p.3, Rewarming](../jama_cooper_2018_oi_180132.pdf#page=3); PLAN [DOC-002 p.77, §12.11](../joi180132supp1_prod.pdf#page=77), [p.99, flowchart rate aim](../joi180132supp1_prod.pdf#page=99), [p.100, management and special considerations](../joi180132supp1_prod.pdf#page=100). Historical [PLAN p.21, V1 §12.11](../joi180132supp1_prod.pdf#page=21) was also found and read.

**Source evidence:** Yes. The report gives gradual controlled rewarming at a target rate up to0.25°C/h.

**Reported-versus-comparator:** Yes. Final p.77 gives gradual rewarming0.17°C/h, with a recommended maximum0.5°C every three hours. Flowchart p.99 says the rate aim is0.17°C/h. Management p.100 repeats0.17 and 0.5°C every three hours and permits faster rates in urgent situations under the intensivist. Historical p.21 gives0.25°C/h; that is disclosed version context, not an independent contemporaneous plan conflict.

**Reasoning procedure:** Yes, Route B and focus D, as a comparison of reported routine specification with final-plan recommended routine specification. It is not a comparison of actual patient rates and not a claim that a recommendation legally prohibits every higher rate.

**Calculation:** Intervals [0.165,0.175] and [0.245,0.255] have gap 0.070; relative 0.070/0.17=0.41176. The displayed0.5°C/3h rule is consistent with approximately0.1667°C/h and confirms the0.17 recommendation.

**Affected result or extracted value:** Routine assigned rewarming target/maximum used to characterize the randomized cooling intervention.

**Why context does not resolve it:** The immediate context does not specify whether the broader report ceiling represents a revised routine aim or contains the final-plan recommended aim. Emergency exceptions do not define the ordinary target.

**Alternative source-grounded interpretations:** A routine rate0.17 satisfies the report's broader up-to0.25 ceiling. The recommendation may remain operative within that ceiling, so actual adherence could reconcile. The registered issue is the different descriptions of the routine maximum/aim; emergency exceptions are expressly disclosed and do not identify a new routine aim.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Direct sources confirm the reported up-to0.25 routine target and final-plan0.17 recommended aim/maximum descriptions, with separated numeric specification intervals. Necessary inputs: Yes for routine target/recommendation comparison. **Exact missing inputs or definitions:** Whether0.25 is merely a broad outer ceiling containing the recommended0.17 aim, whether a later operative update changed that aim, and the implemented routine-rate specification. Actual temperature traces cannot be inferred from these descriptions. Direct observation and inference: The rate phrases, recommendation and urgent exceptions are direct. An actual protocol departure or mechanism for the differing report statement is not established. See the complete durable [C004 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could record 0.25°C/h or approximately 0.17°C/h as the routine specification. Actual patient rates and adherence cannot be inferred.

Checker provenance: Included finding F-ST1-203; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

Audit finding F-QA-102 is SCREENED_OUT/DUPLICATE_OF_INCLUDED provenance, not an additional included Finding ID.

## C005 — Primary analysis-population definition

**Status:** Pending Human Adjudication

**Candidate statement:** The primary analysis-population definition differs between the report and final plan regarding the joint class of patients who were ineligible and never received the intervention.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 pp.3–4 and DOC-003 pp.12,17 vs PLAN DOC-002 pp.84,174–175

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-204

**Qualifying route:** Route B

**Classification rationale:** Confirmed. This is a planned-versus-reported primary analysis definition; the report sensitivity populations are contextual, not a separate S_C inconsistency.

**Classification ambiguity:** Realized equality of the two primary sets is unresolved; roles are clear.

**Exact source locations:** Yes: REPORT [DOC-001 p.3, a-priori analyses definition](../jama_cooper_2018_oi_180132.pdf#page=3), [p.4, Figure1 and evaluable population](../jama_cooper_2018_oi_180132.pdf#page=4), [DOC-003 p.12, per-protocol definition](../joi180132supp2_prod.pdf#page=12), [p.17, as-treated definition](../joi180132supp2_prod.pdf#page=17); PLAN [DOC-002 p.84, §15.2](../joi180132supp1_prod.pdf#page=84), [p.174, V8 modified-ITT amendment](../joi180132supp1_prod.pdf#page=174), and [p.175, amendment continuation](../joi180132supp1_prod.pdf#page=175).

**Source evidence:** Yes. All a-priori analyses use randomized assignment excluding consent withdrawals unless otherwise indicated. Report p.4 removes6+5=11 withdrawals from511, leaving500; primary outcome available for 240 and 226. Supplement defines broader eligibility and compliance exclusions for sensitivity populations.

**Reported-versus-comparator:** Yes. Final §15.2 excludes consent withdrawals and those not fulfilling inclusion criteria and never receiving the intervention. The V8 amendment specifically describes addition of modified intention-to-treat analysis to accommodate this joint class; p.175 continues its rationale, rather than supplying membership counts.

**Reasoning procedure:** Yes, focus D and Route B: differing primary-population membership specification. The conjunctive criterion requires both ineligibility and never receiving intervention; it must not be replaced by an exclusion of every ineligible patient.

**Calculation:** 511−(6+5)=500, and 240+226=466, reconcile. There is no reproduced numerical population-count difference; a precision discrepancy is zero for these count identities. The reproduced comparison is logical set definition: REPORT randomized minus consent withdrawals versus PLAN that set minus the joint exclusion class. The latter may be empty.

**Affected result or extracted value:** Primary analysis-set definition underlying favorable outcomes 117/240 versus 111/226.

**Why context does not resolve it:** The report does not state whether the planned joint exclusion was applied or had no members. Sensitivity-population definitions do not establish primary-set membership.

**Alternative source-grounded interpretations:** The joint class could contain nobody in the primary dataset; alternatively a later SAP may define implementation. Report sensitivity exclusions do not establish whether the same joint exclusion operated in the primary analysis.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Final-plan joint exclusion and report consent-only definition remain different as printed; no count mismatch is asserted. Necessary inputs: Yes to compare definitions; no to calculate a changed population. **Exact missing inputs or definitions:** Patient-level membership of the joint class, which primary analyses applied the modified definition, and any operative SAP explanation underlying 'unless otherwise indicated.' Direct observation and inference: Differing explicit set definitions and printed500/466 totals are direct. Different realized membership, patient exclusions and any effect on117/240 versus 111/226 are unestablished. See the complete durable [C005 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could use different descriptions of the primary analysis set. A changed realized denominator or effect estimate is not established.

Checker provenance: Included finding F-ST1-204; duplicate findings F-XS-005. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C006 — Planned binary primary odds ratio not supplied

**Status:** Pending Human Adjudication

**Candidate statement:** The supplied final plan promises a binary primary GOSE odds ratio and 95% confidence interval that are absent from the matched supplied report outputs.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 p.84 vs REPORT DOC-001 pp.1,3,5,7 and DOC-003 pp.1–24

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** Confirmed. It is planned-versus-reported primary output presence; no report-to-report conflict is asserted.

**Classification ambiguity:** External SAP amendments are not supplied.

**Exact source locations:** Yes: PLAN [DOC-002 p.84, §15.2](../joi180132supp1_prod.pdf#page=84); REPORT [DOC-001 p.1, abstract primary results](../jama_cooper_2018_oi_180132.pdf#page=1), [p.3, primary statistical method](../jama_cooper_2018_oi_180132.pdf#page=3), [p.5, primary and ordinal outcomes](../jama_cooper_2018_oi_180132.pdf#page=5), [p.7, Table2](../jama_cooper_2018_oi_180132.pdf#page=7), and [DOC-003 p.22, post-hoc OR results](../joi180132supp2_prod.pdf#page=22). Full source-native search/read covered DOC-003 physical pages1–24: [1](../joi180132supp2_prod.pdf#page=1), [2](../joi180132supp2_prod.pdf#page=2), [3](../joi180132supp2_prod.pdf#page=3), [4](../joi180132supp2_prod.pdf#page=4), [5](../joi180132supp2_prod.pdf#page=5), [6](../joi180132supp2_prod.pdf#page=6), [7](../joi180132supp2_prod.pdf#page=7), [8](../joi180132supp2_prod.pdf#page=8), [9](../joi180132supp2_prod.pdf#page=9), [10](../joi180132supp2_prod.pdf#page=10), [11](../joi180132supp2_prod.pdf#page=11), [12](../joi180132supp2_prod.pdf#page=12), [13](../joi180132supp2_prod.pdf#page=13), [14](../joi180132supp2_prod.pdf#page=14), [15](../joi180132supp2_prod.pdf#page=15), [16](../joi180132supp2_prod.pdf#page=16), [17](../joi180132supp2_prod.pdf#page=17), [18](../joi180132supp2_prod.pdf#page=18), [19](../joi180132supp2_prod.pdf#page=19), [20](../joi180132supp2_prod.pdf#page=20), [21](../joi180132supp2_prod.pdf#page=21), [22](../joi180132supp2_prod.pdf#page=22), [23](../joi180132supp2_prod.pdf#page=23), [24](../joi180132supp2_prod.pdf#page=24). [DOC-004 p.1](../joi180132supp3_prod.pdf#page=1) supplies data-sharing statements, not such an output.

**Source evidence:** Yes. Final §15.2 promises an unadjusted RR and 95% CI, RD and 95% CI, and OR and 95% CI for midpoint-dichotomized primary GOSE.

**Reported-versus-comparator:** Yes. Main primary binary results give RR/RD, while OR 0.97(0.71–1.34), P=.88 is explicitly for ordinal GOSE. The supplement's OR 0.91(0.59–1.41) and adjusted0.95 result are explicitly post-hoc adequate-cooling58/124 versus 111/226; they do not match primary117/240 versus 111/226. Per-protocol, as-treated and missingness outputs are labeled RR, and their populations differ. No matched primary binary OR/CI is supplied.

**Reasoning procedure:** Yes, focus D and Route A category 5: an explicitly promised primary analysis output is absent from matched supplied reports.

**Calculation:** This is an output-presence and result-identity comparison; numeric rounding cannot turn an ordinal OR or adequate-cooling OR into the planned primary binary output. The crude odds-ratio identity would use117/(240−117) divided by111/(226−111), but recomputing it cannot substitute for a reported planned OR/CI and is not used as a numeric discrepancy.

**Affected result or extracted value:** Availability of the planned primary midpoint-dichotomized GOSE OR and 95% CI for 117/240 versus 111/226.

**Why context does not resolve it:** Route A, category 5 concerns an explicitly planned primary output absent from matched supplied reporting. Ordinal and post hoc subset ORs have different outcomes/populations and do not provide that output.

**Alternative source-grounded interpretations:** The published RR/RD may have been selected as the primary reporting format by an external/later SAP. That document is not supplied, and the distinct reported ORs do not resolve the matched-output absence.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Direct primary-report renders and complete supplementary output search confirm only unmatched ordinal/subset ORs, while the final plan explicitly promises the matched binary primary OR/CI. Necessary inputs: Yes to identify the planned output and distinguish all supplied OR results. **Exact missing inputs or definitions:** The primary binary OR/CI output or a supplied operative amendment withdrawing that planned output. External SAP references supply pointers only and were not accessed. Direct observation and inference: The promise, report effect-measure labels and absent matched output are direct supplied-source observations. A reason for omission or undocumented amendment is not inferred. See the complete durable [C006 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, evidence extraction could identify a planned primary OR/CI as unavailable in the supplied reports or associate an unmatched OR with that planned output. No replacement estimate is proposed.

Checker provenance: Included finding F-XS-004; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C007 — Survival analysis window

**Status:** Pending Human Adjudication

**Candidate statement:** The survival method states six-month censoring, while the corresponding supplementary curve retains positive risk sets at 200 and 250 days.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT DOC-001 pp.2,4–5 vs REPORT DOC-003 p.5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route B

**Classification rationale:** Confirmed. The comparison concerns a survival method and corresponding results in two reports; contextual main-page copies do not add an independent S_W conflict.

**Classification ambiguity:** Whether corresponding Cox and Kaplan–Meier windows truly coincide is unresolved.

**Exact source locations:** Yes: REPORT [DOC-001 p.2, Data Collection](../jama_cooper_2018_oi_180132.pdf#page=2), [p.4, Statistical Analysis survival method](../jama_cooper_2018_oi_180132.pdf#page=4), [DOC-003 p.5, eFigure2 plot, risk table and caption](../joi180132supp2_prod.pdf#page=5). The repeated HR result was also confirmed at [DOC-001 p.5, Secondary Outcomes](../jama_cooper_2018_oi_180132.pdf#page=5).

**Source evidence:** Yes. Follow-up is to death or six months after randomization; Cox analysis is described as censored at six months or last-known-contact, with corresponding Kaplan–Meier curves/log-rank test.

**Reported-versus-comparator:** Yes. Figure2's time axis is survival days; at 200 days risk sets are91/88 and at 250days23/17, with later censor ticks. Caption describes probability/risk of death at six months and HR 1.13(0.76–1.69), P=.54; plot log-rank P=.5349. These P values are compatible as differently labeled tests/display precision and are not an additional issue.

**Reasoning procedure:** Yes, focus C and Route B: the named survival result's censoring window is compared with its corresponding plotted risk process.

**Calculation:** Even a conservative upper bound of186 days for six calendar months is below200 days. Universal administrative censoring by that bound implies zero at-risk subjects at 200/250 days. Half-unit risk-count intervals at 200 days [90.5,91.5] and [87.5,88.5], and at 250 days [22.5,23.5] and [16.5,17.5], remain positive. Their gaps from zero exceed precision; for printed23 the minimum relative discrepancy is22.5/23=0.97826. Exact survival records are not required to establish this literal-window mismatch.

**Affected result or extracted value:** Observation/censoring horizon associated with mortality HR 1.13 (95% CI 0.76–1.69), P = .54.

**Why context does not resolve it:** The method and caption do not identify different Cox and Kaplan–Meier windows or an extended assessment allowance; therefore the horizon of the named HR is not identifiable from immediate context.

**Alternative source-grounded interpretations:** Six-month assessment may allow delayed contact, or Cox and Kaplan–Meier presentations may use different windows. The stated corresponding-curve method and caption do not specify either distinction.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Direct-source eFigure2 retains positive risk sets beyond any literal six-calendar-month cutoff while the main method states such a cutoff. Necessary inputs: Yes for rule-versus-plot comparison. **Exact missing inputs or definitions:** Actual administrative cutoff, definition of six-month assessment window, event/censor times, and whether Cox and plot used identical datasets/windows. Direct observation and inference: Printed censor rule, caption and positive risk sets are direct. A changed HR or significance conclusion is not inferred. See the complete durable [C007 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could attach a six-month or longer observation horizon to the reported survival result. No revised HR or significance assessment is established.

Checker provenance: Included finding F-ST1-003; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C008 — Cooling-time equal-proportions test

**Status:** Pending Human Adjudication

**Candidate statement:** The registered count-to-P comparison for cooling-time categories is retained as a candidate reporting issue with not_reproduced evidence: permitted half-unit inputs reconcile with P = .09.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 pp.4–5 vs REPORT DOC-003 p.11; REPORT DOC-003 same-display counts and P

**Evidence state:** not_reproduced

**Inclusion audit:** QUESTIONED

The audit questions inclusion because half-unit inputs reproduce the printed .09 and no matched global estimate/interval/test establishes Route A category 1.

**Finding IDs:** F-ST1-004

**Qualifying route:** Route A, category 1

This is the historical registration route; the current recheck and audit do not establish its reproduction or category-1 linkage.

**Classification rationale:** Relationship/domain fields describe the registered comparisons and are retained. Evidence state records their precision reconciliation; stable identity is unchanged.

**Classification ambiguity:** The global table P's exact implementation is not identified; the claimed category 1 interval/test linkage is absent.

**Exact source locations:** Yes: REPORT [DOC-001 p.4, favorable outcome versus time-to33°C method](../jama_cooper_2018_oi_180132.pdf#page=4), [p.5, Additional Outcomes nonsignificance statement](../jama_cooper_2018_oi_180132.pdf#page=5), [DOC-003 p.11, eTable7 four categories and P value](../joi180132supp2_prod.pdf#page=11).

**Source evidence:** Yes. Main states an unadjusted chi-square test for equal proportions in cooled patients and nonsignificant results. Table labels four categories1–7h,8–13h,>13h,Never; totals 49,67,59,65; favorable counts 18,28,32,39; P=.09. Individual percentages36.7,41.8,54.2,60.0 have marginal95% CIs 22.8–50.7,29.6–53.9,41.2–67.3,47.8–72.2.

**Reported-versus-comparator:** Confirmed four-category totals 49, 67, 59, 65 and favorable counts 18, 28, 32, 39 versus printed P = .09. The main method names an equal-proportions chi-square test; the individual CIs are marginal proportion intervals.

**Reasoning procedure:** The count-based P recomputation is applicable, but the registered Route A category 1 exemption is not established. Its definition concerns a printed estimate/interval versus P/test conflict, a P/test unable to belong to a printed estimate/interval, or point-estimate containment. Here the printed intervals are marginal proportion intervals, not a global contrast CI; they overlap a common proportion, and there is no printed global test statistic or global effect interval contradicting P=.09. Recomputed exact-count significance alone is not such a printed interval/P conflict. The mandatory display rule therefore applies to this recomputation.

**Calculation:** Pool 117/240. Pearson statistic sum over groups of (a_i−n_i*117/240)^2/[n_i*(117/240)*(123/240)] =8.133762156, df 3; P=.04332664. Restricting to the three reaching-target categories gives3.658952, df 2, P=.16050, also a different exact-count result. Allowing every displayed count/denominator its required half-unit range, admissible numerators(18.5,28.5,31.5,38.5) with totals(48.5,66.5,59.5,65.5) give chi-square6.162765031, df 3, P=.10395436. Along the continuous path from printed centers to these permitted endpoints, the recomputed P interval includes [.04332664,.10395436], hence overlaps the printed [.085,.095] range. Gap0; relative discrepancy 0. This is an interval-arithmetic feasibility check, not a claim that fractional participants were observed. Printed percentages are outputs of the same display, not additional count inputs to this stated-count recomputation.

**Affected result or extracted value:** Association-test attribution for favorable primary GOSE across the four cooling-time categories; the registered numerical inconsistency does not survive the required precision check.

**Why context does not resolve it:** The historical Route A, category 1 justification is disputed: no printed matched global estimate/interval/test statistic establishes that category, and the count-to-P comparison reconciles under the prescribed half-unit rule. There is no current reproduced inconsistency to support that route.

**Alternative source-grounded interpretations:** A different subset or categorical implementation may generate.09; the main method and table do not distinguish it. The reported marginal CIs and nonsignificance statement reconcile with.09. No marginal-CI/global-test conflict is reproduced.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. The recomputed P range overlaps [.085,.095], and no printed global estimate/CI or test statistic establishes a Route A category 1 exception. Thus the numerical comparison reconciles under the required display rule despite the exact-count diagnostic difference. Necessary inputs: Yes for the prescribed precision check. **Exact missing inputs or definitions:** Exact test implementation/group inclusion that generated.09 is absent, but no missing definition is needed to establish the mandatory interval overlap. Direct observation and inference: The exact-count diagnostic difference is observed computationally; the reported count-to-P inconsistency does not survive the normative half-unit rule. A different analysis or production mechanism is not established. See the complete durable [C008 source recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** The retained card records a questioned historical comparison and its precision reconciliation. It does not support copying an alternative P value or assuming a changed significance conclusion; exact test attribution remains unspecified.

Checker provenance: Included finding F-ST1-004; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.


## C009 — Final significance-rule specification

Pending Human Adjudication

**Candidate statement:** The report's all-analysis .05 rule and final protocol's explicitly substituted .0459 final boundary do not specify the same decision region.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 p.4 vs PLAN DOC-002 p.84; PLAN p.188 earlier-version context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route B

**Classification rationale:** Completed-report methods versus prospective final V9 methods supplies P_R alone. The earlier two-look charter is historical context, not a simultaneous P_P conflict.

**Classification ambiguity:** Nominal .05 reporting and operational .0459 testing may coexist, but the supplied report does not establish this distinction.

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 4, REPORT significance paragraph p.4](<../jama_cooper_2018_oi_180132.pdf#page=4>); [joi180132supp1_prod.pdf — PDF p. 84, PLAN final §15.1.3 p.84](<../joi180132supp1_prod.pdf#page=84>); [joi180132supp1_prod.pdf — PDF p. 188, earlier charter p.188](<../joi180132supp1_prod.pdf#page=188>).

**Source evidence:** Report says two-sided P < .05 for all analyses. Final plan says final ±1.996 SD/P = .0459 rather than ±1.96 SD/P = .05 after expanded interim monitoring. The earlier charter gives |Z| ≥ 1.975/P = .048 and alpha .05 for the original two-look design.

**Reported-versus-comparator:** All-analysis .05 versus explicitly replaced final .0459 rule; earlier charter retained as history.

**Reasoning procedure:** Compare explicit decision specifications, separating fixed critical regions from rounded copies and operational consequences from observed results.

**Calculation:** Copy intervals [.04585,.04595] and [.045,.055] overlap: gap 0, relative 0. They cannot establish a copy discrepancy. A hypothetical exact P = .048 meets P < .05 but not P < .0459; it illustrates the different specified regions only. Actual primary P = .94 meets neither.

**Affected result or extracted value:** Final primary-test alpha and its relation to expanded interim monitoring.

**Why context does not resolve it:** The report does not explain whether .05 is nominal reporting accompanied by the adjusted final decision boundary.

**Alternative source-grounded interpretations:** Nominal .05 reporting may coexist with operational .0459 testing; the earlier charter may be superseded by final V9's additional monitoring.

**Mechanical evidence recheck:** Source text, physical pages, roles and fixed-rule comparison confirmed. P_R/domain/reproduced agree with recheck. Actual operational rule and unsupplied SAP clarification remain missing. Remaining human question: which final rule applied, and was nominal reporting distinguished from adjusted decisions?

**Potential downstream evidence impact:** A methods extractor could copy .05 or .0459 as final alpha. No observed significance reversal or downstream conclusion change is established.

## C010 — Bleeding RR, CI and P attribution pattern

Pending Human Adjudication

**Candidate statement:** Main-table bleeding RR/CI/P tuples reproduce the opposite outcome's counts, while the supplement assigns the P values to the other outcomes.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 Table2 p.7 vs REPORT DOC-003 eTable6 p.10; REPORT DOC-001 same-display counts/intervals

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 4

**Classification rationale:** Two distinct REPORT documents supply S_C; main-table counts versus intervals supply S_W. S_C precedes S_W. Estimates, intervals and tests require statistical_results despite the attribution component.

**Classification ambiguity:** Separate undisclosed analyses remain possible; document roles are clear.

**Exact source locations:** [jama_cooper_2018_oi_180132.pdf — PDF p. 3, unadjusted method p.3](<../jama_cooper_2018_oi_180132.pdf#page=3>); [jama_cooper_2018_oi_180132.pdf — PDF p. 7, Table2 both bleeding rows p.7](<../jama_cooper_2018_oi_180132.pdf#page=7>); [joi180132supp2_prod.pdf — PDF p. 10, eTable6 both bleeding rows p.10](<../joi180132supp2_prod.pdf#page=10>); corroborating [jama_cooper_2018_oi_180132.pdf — PDF p. 1, abstract p.1](<../jama_cooper_2018_oi_180132.pdf#page=1>) and [jama_cooper_2018_oi_180132.pdf — PDF p. 5, narrative p.5](<../jama_cooper_2018_oi_180132.pdf#page=5>).

**Source evidence:** Intracranial 47/260 versus 37/240 prints RR 1.23 (.43–3.5), P = .70; extracranial 8/260 versus 6/240 prints RR 1.17 (.79–1.74), P = .43. eTable 6 repeats counts but gives intracranial .43/extracranial .70. Main RD columns reproduce own rows.

**Reported-versus-comparator:** Main RR/CI/P tuples versus own-row count-based calculation and supplementary P assignment.

**Reasoning procedure:** RR=(a/n)/(c/m); SE(logRR)=sqrt(1/a−1/n+1/c−1/m); limits=RR×exp(±1.95996398454×SE). Check stated Pearson equal-proportion diagnostic, neighboring rows and half-unit input corners. Consolidate both rows once.

**Calculation:** Intracranial RR 1.17255717, CI [.79118130,1.73776899], P = .42666956; extracranial RR 1.23076923, CI [.43334502,3.49558164], P = .69603919. Primary, mortality and infection rows reproduce their printed intervals. Half-unit intracranial lower-limit bounds [.76973897,.81321980] versus printed [.425,.435] leave .33473897/.43=.77846; extracranial bounds [.37662053,.49716491] versus [.785,.795] leave .28783509/.79=.36435. P-copy intervals [.695,.705]/[.425,.435] leave .260/.70=.371429 or .260/.43=.604651. Point-RR differences alone are within precision.

**Affected result or extracted value:** Outcome-specific bleeding confidence limits and P values.

**Why context does not resolve it:** Route A category 4: the same reproducing method yields different own-row intervals; immediate reconstruction does not remove the printed values.

**Alternative source-grounded interpretations:** Separate analyses could explain the displays, but the supplied methods do not assign them to these rows or explain exact opposite-row reproduction.

**Mechanical evidence recheck:** Both tables' labels, counts and tuples confirmed visually and in fresh text; bounds reproduced independently. Classification and reproduced state agree. Missing definition: any separate analysis and row mapping. Remaining human question: which RR/CI/P belongs to each outcome, and were separate analyses used?

**Potential downstream evidence impact:** Extraction could associate the wide/narrow interval or .70/.43 with the other bleeding outcome. Both displayed P values exceed .05; no trial-conclusion change is asserted.

## C011 — Interim normal boundary and P threshold

Pending Human Adjudication

**Candidate statement:** A fixed normal |Z| ≥ 3 monitoring rule is paired with approximate P < .001, leaving the operative threshold unclear.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 p.188 internal normal boundary/P threshold; PLAN pp.84,152 method/version context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-205

**Qualifying route:** Route B

**Classification rationale:** Prospective charter instructions are PLAN; comparison within that content supplies P_P/plan_material. Final sidedness and the earlier amendment are context, not REPORT relationships or an additional simultaneous version conflict.

**Classification ambiguity:** Approximate P may be shorthand; the intended tail convention and operative rule hierarchy remain unspecified.

**Exact source locations:** [joi180132supp1_prod.pdf — PDF p. 188, charter boundary paragraph p.188](<../joi180132supp1_prod.pdf#page=188>); [joi180132supp1_prod.pdf — PDF p. 84, final 3SD/two-sided convention p.84](<../joi180132supp1_prod.pdf#page=84>); [joi180132supp1_prod.pdf — PDF p. 152, historical amendment p.152](<../joi180132supp1_prod.pdf#page=152>).

**Source evidence:** Conventional three-standard-deviation |Z_k| ≥ 3 boundary, normal approximation to discrete binomial proportions, approximate P < .001. Final V9 uses two-sided tests unless specified. Earlier .005 language is version context.

**Reported-versus-comparator:** Charter's fixed 3 boundary versus literal .001 critical region; not an observed statistic/P pair.

**Reasoning procedure:** Independently integrate the normal tail under the explicitly named approximation; examine both tail conventions and retain approximate wording.

**Calculation:** At 3, one-sided P = .00134989803163 and two-sided P = .00269979606326. Literal two-sided .001 corresponds |Z| > 3.290527; one-sided corresponds Z > 3.090232. Some larger Z values satisfy both descriptions, but the boundaries differ. A fixed rule 3 is not a rounded observed statistic varying over [2.5,3.5]. Numeric-copy interval arithmetic is not applicable to this explicit decision-rule comparison. If approximate P is descriptive shorthand, it remains an alternative rather than an observed conflict.

**Affected result or extracted value:** Interim stopping specification for primary GOSE/mortality.

**Why context does not resolve it:** The source names a normal approximation but does not specify whether 3 SD or literal P < .001 controls operational decisions.

**Alternative source-grounded interpretations:** 3 SD may govern with P shorthand; a discrete calibration may exist, but no replacement boundary is supplied. Earlier .005 may be superseded.

**Mechanical evidence recheck:** Exact source and scanned amendment confirmed; normal tails independently reproduced. P_P/domain/reproduced agree with recheck; route narrowed to B. Missing operational interpretation remains bounded. Remaining human question: which threshold, tail convention and meaning of approximate applied?

**Potential downstream evidence impact:** A methods extractor could record 3 SD or a literal .001 rule. No observed crossing, stopping consequence or treatment identity is inferred.

## C012 — July 2016 cumulative primary-outcome Y series

Pending Human Adjudication

**Candidate statement:** The favorable-GOSE cumulative Y curve does not reproduce favorable block-count sums that reproduce X in the same display.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT observed interim DOC-002 p.192 block table vs cumulative chart; REPORT DOC-002 p.191 corroborates

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-301

**Qualifying route:** Route A, category 4

**Classification rationale:** Both compared displays contain observed outcomes in one supplied PDF, hence S_W/statistical_results. Prospective rules are not a conflicting comparator; p.191 only corroborates totals.

**Classification ambiguity:** Structured chart coordinates are unavailable; mixed favorable/unfavorable plotting is a possible explanation.

**Exact source locations:** [joi180132supp1_prod.pdf — PDF p. 192, favorable block table and cumulative chart p.192](<../joi180132supp1_prod.pdf#page=192>); [joi180132supp1_prod.pdf — PDF p. 191, July2016 GOSE totals p.191](<../joi180132supp1_prod.pdf#page=191>).

**Source evidence:** Both titles say favorable GOSE 5–8. Y favorable block numerators 7,2,11,5,8,6,3,5,6,5,2,4,3,6. Second cumulative Y point lies near 12 above 10;7+2=9. Page 191 prints favorable Y 73/unfavorable Y 80.

**Reported-versus-comparator:** Favorable block-count sum versus same-title blue cumulative curve; graphical readings are distinguished from exact printed numerators.

**Reasoning procedure:** Sum numerators, reproduce X, compare an early point with widened graphical uncertainty, and avoid using the accumulated endpoint as the precision anchor.

**Calculation:** Y favorable cumulative 7,9,20,25,33,39,42,47,53,58,60,64,67,73. X 10,18,20,27,36,41,50,57,62,66,69,78,81,86 reproduces orange X. Y denominator complements sum 6,12,17,22,24,30,35,42,50,57,64,69,77,80, compatible with approximate blue readings. Second favorable sum interval [8,10] versus graphical [11,13] leaves gap ≥ 1, conservative relative ≥ 1/13=.076923. Central denominator 12 gives .083333, not the lower bound. Endpoint 73/near 80 is corroboration only because fourteen half-unit inputs can overlap.

**Affected result or extracted value:** Cumulative favorable primary-GOSE Y count/curve in the July 2016 monitoring report.

**Why context does not resolve it:** Route A category 4: one cumulative method reproduces X while Y differs under the same favorable title. Reconstructed complements do not remove the graph.

**Alternative source-grounded interpretations:** Y may intentionally plot unfavorable counts while X plots favorable, but titles/legend do not define that mixture. Exact graph data are absent.

**Mechanical evidence recheck:** Source images at 110/220 dpi confirm titles, pairs and early blue point; conservative bounds reproduce. Recheck's REPORT/S_W/statistical_results/reproduced agrees. Arm identity and exact structured series are unavailable. Remaining human question: which outcome and structured series does Y represent?

**Potential downstream evidence impact:** Extraction could copy a graph-derived cumulative count instead of favorable numerator sums or misidentify Y coding. No DSMB reliance or stopping consequence is asserted.

## C013 — As-treated CT count and percentage ordering

Pending Human Adjudication

**Candidate statement:** Two normothermia CT category cells do not reconcile with No.(%) and n = 196.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 eTable10 p.18 internal heading/denominator and Marshall V/VI cells

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-101

**Qualifying route:** Route A, category 3

**Classification rationale:** Heading and cells in one results table give REPORT/S_W/statistical_results; no conflicting plan or separate report is involved.

**Classification ambiguity:** Intended pair ordering remains unspecified.

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 18, eTable10 normothermia CT V/VI cells and headings p.18](<../joi180132supp2_prod.pdf#page=18>).

**Source evidence:** n = 196, No.(%); V 34.7 (68), VI 1 (2); other categories 3 (1.5),108 (55.1),15 (7.7) use count-first order.

**Reported-versus-comparator:** Literal count-first cell readings versus percentage arithmetic and category sum.

**Reasoning procedure:** Compute 100×count/denominator with half-unit inputs and sum category-count intervals; consolidate both cells.

**Calculation:** V implies [17.633588,17.774936]% versus [67.5,68.5], gap 49.725064/68=.731251. VI implies [.254453,.767263]% versus [1.5,2.5], gap .732737/2=.366368. Literal count sum 161.7 interval [159.65,163.75] versus denominator [195.5,196.5] leaves 31.75/196=.161990. Reversed counts 68/2 and percentages 34.7/1 reconcile the category sum 196; this is an alternative only.

**Affected result or extracted value:** As-treated normothermia Marshall V/VI counts and proportions.

**Why context does not resolve it:** Route A category 3 always registers a reproduced within-display count/denominator/percentage discrepancy even when a likely intended reading is apparent.

**Alternative source-grounded interpretations:** Both cells may use percentage(count) despite the shared count-first heading; no category-specific denominator or presentation exception is stated.

**Mechanical evidence recheck:** Visual page and fresh text confirm both cells/denominator; independent arithmetic reproduces all gaps. S_W/domain/reproduced agree. Remaining human question: which counts/proportions should be taken under the shared heading?

**Potential downstream evidence impact:** Extraction could take literal pairs or reversed readings. No primary-effect or shared-test consequence is inferred without intended values.

## C014 — Adjusted odds-ratio interval token

Pending Human Adjudication

**Candidate statement:** The adjusted OR interval prints 275 between the lower limit and 1.64.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.22 adjusted OR and printed confidence-interval tokens

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-102

**Qualifying route:** Route A, category 2

**Classification rationale:** One completed supplementary results statement gives S_W/statistical_results; the prior unadjusted OR is a different analysis, not a comparator.

**Classification ambiguity:** The intended role of 275 is unspecified.

**Exact source locations:** [joi180132supp2_prod.pdf — PDF p. 22, post hoc adjusted OR statement p.22](<../joi180132supp2_prod.pdf#page=22>).

**Source evidence:** Adjusted OR 0.95 (0.55-275 1.64), P = .84, after time-to-randomization adjustment. Prior unadjusted OR 0.91 (.59–1.41), P = .68 is distinct.

**Reported-versus-comparator:** Undefined 275 and 1.64 both follow the lower-limit hyphen in a result presented as 95% CI.

**Reasoning procedure:** Confirm source numeral and quantify possible upper-limit magnitudes without reconstructing the unavailable adjusted model or inferring the token's origin.

**Calculation:** [274.5,275.5] versus [1.635,1.645] gives gap 272.855/1.64=166.375. Both .55–275 and .55–1.64 contain .95/null 1; no significance reversal is asserted.

**Affected result or extracted value:** Upper 95% confidence limit of the adjusted favorable-outcome OR.

**Why context does not resolve it:** Route A category 2 covers a numerical slip changing magnitude; reconstructing the likely two-limit reading does not remove 275.

**Alternative source-grounded interpretations:** 275 may be an additional insertion and the limits may be .55/1.64; another annotation is possible but undefined locally.

**Mechanical evidence recheck:** Direct-source image and fresh layout confirm 275 itself; alternative-limit arithmetic reproduces. Classification/state agree. Adjusted output remains unavailable. Remaining human question: intended upper limit and meaning of 275?

**Potential downstream evidence impact:** Extraction could take upper limit 275 or 1.64. No fitted-model reconstruction, significance conflict or observed downstream use is established.

## C015 — Planned adjusted key-secondary sensitivity analyses

Pending Human Adjudication

**Candidate statement:** Planned covariate-adjusted sensitivity analyses have no matched pneumonia or intracranial-bleeding outputs in the supplied reports.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.84–85,183–184,187 vs REPORT DOC-001 pp.1,3–7 and DOC-003 pp.1–24; DOC-004 p.1 absence scope

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST2-201

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective analysis promise versus completed-report absence gives P_R/protocol_report. Other reports corroborate absence; the update supplies context rather than a separate P_P conflict.

**Classification ambiguity:** Full external SAP is unsupplied; no supplied withdrawal of these adjusted outputs is identified.

**Exact source locations:** PLAN [joi180132supp1_prod.pdf — PDF p. 84, binary models p.84](<../joi180132supp1_prod.pdf#page=84>), [joi180132supp1_prod.pdf — PDF p. 85, adjusted primary/secondary promise p.85](<../joi180132supp1_prod.pdf#page=85>), [joi180132supp1_prod.pdf — PDF p. 183, update p.183](<../joi180132supp1_prod.pdf#page=183>), [joi180132supp1_prod.pdf — PDF p. 184, adjustment footnotes p.184](<../joi180132supp1_prod.pdf#page=184>), [joi180132supp1_prod.pdf — PDF p. 187, aligned update p.187](<../joi180132supp1_prod.pdf#page=187>), [joi180132supp1_prod.pdf — PDF p. 181, SAP pointer p.181](<../joi180132supp1_prod.pdf#page=181>). REPORT [jama_cooper_2018_oi_180132.pdf — PDF p. 1, abstract p.1](<../jama_cooper_2018_oi_180132.pdf#page=1>), [jama_cooper_2018_oi_180132.pdf — PDF p. 3, outcomes/methods p.3](<../jama_cooper_2018_oi_180132.pdf#page=3>), [jama_cooper_2018_oi_180132.pdf — PDF p. 4, continuation p.4](<../jama_cooper_2018_oi_180132.pdf#page=4>), [jama_cooper_2018_oi_180132.pdf — PDF p. 5, results p.5](<../jama_cooper_2018_oi_180132.pdf#page=5>), [jama_cooper_2018_oi_180132.pdf — PDF p. 6, unadjusted sensitivity pneumonia p.6](<../jama_cooper_2018_oi_180132.pdf#page=6>), [jama_cooper_2018_oi_180132.pdf — PDF p. 7, Table2 p.7](<../jama_cooper_2018_oi_180132.pdf#page=7>); [joi180132supp2_prod.pdf — PDF p. 10, eTable6 p.10](<../joi180132supp2_prod.pdf#page=10>), [joi180132supp2_prod.pdf — PDF p. 14, eTable9 p.14](<../joi180132supp2_prod.pdf#page=14>), [joi180132supp2_prod.pdf — PDF p. 19, eTable11 p.19](<../joi180132supp2_prod.pdf#page=19>), GOSE outputs [joi180132supp2_prod.pdf — PDF p. 16, p.16](<../joi180132supp2_prod.pdf#page=16>), [joi180132supp2_prod.pdf — PDF p. 20, p.20](<../joi180132supp2_prod.pdf#page=20>), [joi180132supp2_prod.pdf — PDF p. 21, p.21](<../joi180132supp2_prod.pdf#page=21>), [joi180132supp2_prod.pdf — PDF p. 22, p.22](<../joi180132supp2_prod.pdf#page=22>). Absence scope: all DOC-001 physical pp.1–10, DOC-003 pp.1–24 and [joi180132supp3_prod.pdf — PDF p. 1, DOC-004 p.1](<../joi180132supp3_prod.pdf#page=1>).

**Source evidence:** Plan promises regression sensitivities of primary/secondary outcomes adjusted for prespecified baseline covariates plus any imbalanced covariates. Abstract reports pneumonia 55.0%/51.3% and intracranial bleeding 18.1%/15.4%. Adjusted labels accompany GOSE, not these adverse-event rows; main p.6 explicitly calls subset pneumonia unadjusted. Updates limit covariates for subset analyses but do not expressly withdraw the final promise.

**Reported-versus-comparator:** Explicit planned adjusted key-secondary sensitivities versus absent matched output, with ordinary unadjusted rows and distinct adjusted GOSE output present.

**Reasoning procedure:** Independently read all supplied final REPORT pages, match outcome/population/adjustment, confirm promise and abstract status, and distinguish absent output from unsupported fitted-model inference. Consolidate both outcomes under one specification.

**Calculation:** Logical comparison: explicit adjusted-secondary promise + named abstract secondary outcomes + no matched supplied adjusted output. Numeric intervals/relative discrepancy are not applicable. No adjusted effect is recomputed or inferred from counts.

**Affected result or extracted value:** Availability and planned-versus-reported status of adjusted pneumonia/intracranial-bleeding sensitivities.

**Why context does not resolve it:** Route A category 5: planned key-secondary analysis is not reported. Exploratory interpretation for multiplicity does not withdraw outcome status or adjustment promise.

**Alternative source-grounded interpretations:** Unsupplied SAP could narrow the promise or outputs may exist elsewhere; neither provides supplied-source withdrawal/output. PP/as-treated execution is a distinct specification.

**Mechanical evidence recheck:** Full report/supplement layout, contents and all sensitivity/post hoc outputs independently read; exact plan/update images and adjusted-label placement confirmed. Appended recheck reproduces P_R/domain/state. Missing external SAP and adjusted outputs/covariates remain bounded. Remaining human question: where are these outputs, or which supplied amendment withdrew/narrowed the promise?

**Potential downstream evidence impact:** Extraction could record adjusted sensitivities unavailable or confuse unadjusted outputs with promised adjusted results. No change to estimates or clinical conclusions is asserted.


## Downstream Evidence-Chain Considerations

A data extractor may select a signed estimate, interval, count/percentage pairing, analysis population, observation horizon or assigned intervention specification from the abstract, a table, a figure or a protocol. If a reproduced candidate is confirmed, these choices could affect how that particular value or specification is entered into a systematic review, meta-analysis or guideline evidence table. A missing planned output could also affect the recorded availability of a prespecified analysis. The report identifies those possible pathways without asserting that a value was propagated, a conclusion changed or harm occurred. C008's reconciled precision comparison supports no alternative numerical extraction.

## Limitations and Missing Definitions

- All four supplied PDFs and all 229 physical pages have complete scientific maps. There is no unresolved source-unit coverage gap.
- The plan bundle supplies original and final protocols, amendment scans, SAP-update scans and their correction, and DSMC charter material and monitoring reports. Some pages are pointers to external published protocol/SAP/charter documents rather than the full linked text. Only the supplied pages and embedded material were reviewed; external documents were not fetched or presumed.
- Historical versions of the extraction and rendering engines are not recorded for the reused evidence. Native text was matched to the current sources for all four PDFs, layout text for three, and a scan-page render matched directly. The article layout has a vertical-axis placement difference on one page; visual source evidence governs interpretation.
- Thirty plan pages have no usable body text in the native extraction. These pages were visually inspected through reusable page images. Tesseract and LibreOffice were unavailable; no Office sources or unresolved OCR-dependent units remain.
- Some plotted box summaries, category shares, and interval bars are graphical without exact printed coordinates. The maps preserve the complete visible displays and identify approximate graphical readings; they do not invent exact values.
- This review uses supplied publication material. It does not examine raw participant data or perform a broader methodological, clinical, or study-design audit. Missing numerical definitions needed for individual comparisons are recorded with those relationships and evidence cards.

## Candidate-specific missing definitions and bounded evidence qualifications

- Intervention specifications: the governing hierarchy of the final protocol's synopsis, detailed instructions and appendices; the seven-day time origin; the relationship between post-96-hour ordinary care and assigned device management; the conditional late-cooling exposure definition; and whether the reported 0.25°C/h ceiling contained or replaced the final-plan recommended 0.17°C/h aim. Patient-level device use, temperature traces and adherence are unavailable.
- Primary population and output: membership of the ineligible-and-never-intervention joint class and the operative primary analysis-set implementation are unavailable. The promised primary binary OR/CI and matched adjusted pneumonia/intracranial-bleeding sensitivity outputs are absent from the supplied report inventory. Unprovided external SAP contents or later outputs cannot be presumed.
- Survival and inferential attribution: actual administrative cutoffs, event/censor records, equality of Cox and Kaplan–Meier windows, exact cooling-time group/test implementation, and separate bleeding-row analysis/tuple assignments are unavailable.
- Monitoring and graphical definitions: the operative final significance rule, tail convention and hierarchy of approximate P and fixed normal boundary; structured cumulative graph coordinates and blinded-arm identity; and the outcome series represented by the cumulative Y curve remain unspecified. Graph-based comparison preserves conservative visual bounds.
- Printed cell and interval definitions: the intended pair ordering of the two normothermia CT cells and the role of the additional 275 token in the adjusted OR interval are not specified in the immediate display. The adjusted model output is not supplied.
- C008 remains a stable candidate with not_reproduced evidence and QUESTIONED inclusion. Its exact-center Pearson calculation is a diagnostic; feasible half-unit inputs overlap the printed P interval, and no matched global estimate/interval/test statistic establishes the historical Route A category 1 exception. Keeping its ID does not establish a reproduced inconsistency.

All 229 supplied source units are mapped. These limits concern interpretation, numerical definitions and unprovided material; none is an unresolved scientific source-unit coverage gap. Potential extraction relevance is conditional and does not establish propagation, a changed conclusion or harm.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The review used only supplied package evidence and local tools. The [routing preflight](review_1_6_2/routing_preflight.md) records PASS, run model gpt-6.1-sol, source DEFAULT, CURRENT_SESSION provider, INTERACTIVE_CLI execution, coordinator high effort and all ten named presets verified. Every actual agent is listed below with its runtime ID, model, effort, start mode and primary artifact relative to review_1_6_2. Mandatory stages and context-bounded shards used distinct fresh runtimes.

Direct tool probe: pdfinfo, pdftotext, pdftoppm, pdftocairo and pandoc available; Tesseract and LibreOffice absent. Compute device: CPU. No fallback environment, OCR or Office conversion was required; fallback environment status NOT_NEEDED and removal status NOT_CREATED. Source-linked image inspection closed all text gaps. Current derivatives and engines are documented in the [tooling record](review_1_6_2/tooling_record.md) and stage artifacts.

All four direct-source hashes and all 305 reusable-asset hashes match their before-and-after records. The [source after hashes](review_1_6_2/source_hashes_after.sha256) and [reused-asset after hashes](review_1_6_2/reused_artifact_hashes_after.sha256) preserve this confirmation. The accompanying standalone HTML is rendered locally; the [mechanical validation record](review_1_6_2/review_validation.json) records the final completion gate. Supplied evidence and prior audit artifacts remain preserved.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-70e5-7f72-80a0-6613a01bbb24 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129b0-f753-7063-bd19-d468d23f6caf | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b4-045d-7910-b98e-2eeafcaa15c0 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_plan_mapper_a | 01a129b4-3f17-7c51-9f95-75431d8b2433 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_a.md |
| support_plan_mapper_b | 01a129b4-6407-7290-94af-d95244e7d3bc | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_b.md |
| support_plan_mapper_c | 01a129b4-83d9-7a20-a3fa-5232fa737f12 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_c.md |
| support_plan_mapper_d | 01a129b4-a84d-7ea2-a4e0-6654dc94857b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_plan_d.md |
| support_quantitative_mapper | 01a129b4-c709-70b1-9d71-591188a0a35a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a129ba-7aa6-77c0-9fab-ab97751545fe | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support | 01a129ba-a075-7e40-8815-b16cd5e4d1ad | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | 01a129ba-d0ae-7972-ad30-ec98db09c65f | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support | 01a129ba-f6dd-7cd3-ac0d-591be72882c8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_support_pass_1.md |
| statistics_pass_1_plan | 01a129bb-2346-7d93-89e3-266a9f7a3f14 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_plan_pass_1.md |
| cross_source_consistency_reviewer | 01a129bb-6a63-7c90-8382-58982d46908a | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1_monitoring | 01a129be-d2f9-73e3-94d5-a2df0a75cd43 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_monitoring_pass_1.md |
| inclusion_screener | 01a129c4-9c36-7e01-be3f-8b97966c8822 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129cf-7c7a-7882-8c5f-12ba5ca391b4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129d9-0afb-7071-a4ab-bc2c2e152fc2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support | 01a129d9-3869-7ef2-bdca-396e4635945a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_report_support_pass_2.md |
| statistics_pass_2_plan | 01a129d9-67a8-73b1-896f-eabbacc1a39a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_plan_pass_2.md |
| statistics_pass_2_monitoring | 01a129d9-9035-77c3-b829-b5118f5f2bd9 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_monitoring_pass_2.md |
| inclusion_screener_pass_2 | 01a129e1-b558-7331-b786-a24a51c7f784 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | 01a129e4-f611-7510-9c03-ccbe60dedc0d | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_appended.md |
| quality_control_auditor | 01a129e9-8c39-7691-945e-b490f062019c | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_support | 01a129ea-c9cd-7963-af96-35c47b46ef8d | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_support.md |
| report_generator | 01a129f7-1283-7ce3-8e08-59d0c5a16f05 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |
| report_generator_support | 01a129f7-5ba3-7ea0-b777-3fb3752dbc06 | gpt-6.1-sol | medium | FRESH_SPAWN | report_parts/support.md |

### Reproducibility performance

- **Target basis:** Four PDF sources with 229 physical pages; all pages have reusable extraction or rendered images, with 27 textless and three header-only plan pages requiring visual mapping. Main article and 24-page results supplement require table/figure reconstruction; the 194-page multi-version plan includes amendments, scanned SAP updates and DSMC decisions. Disjoint mapping shards keep text under 200000 characters and visual inputs under 32 pages; subsequent parallel numeric/cross-source/statistical checks and sequential inclusion, recheck, fresh statistical pass 2, audit and reporting waves determine the planning range. No Office conversion is needed.
- **Total source units:** 229
- **Fresh-source units:** 0
- **Target elapsed minutes:** 40-65
- **Started UTC:** 2026-10-11T06:39:51Z
- **Finished UTC:** 2026-10-11T08:02:16Z
- **Observed elapsed minutes:** 82.42
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** The fresh second statistical pass identified F-ST2-201, requiring separate independent inclusion screening and exact-source recheck. Audit inputs expanded to 222627 characters, requiring two disjoint fresh audit shards, 72 excluded-observation reviews and two duplicate-provenance repairs. Complete report cards also required parallel context-bounded generation; coverage and stable IDs were preserved.

Review timing was finalized by the coordinator immediately after complete Markdown assembly; local HTML rendering and mechanical validation are outside the recorded review duration. The package-specific planning target never limits source coverage or candidate count.
