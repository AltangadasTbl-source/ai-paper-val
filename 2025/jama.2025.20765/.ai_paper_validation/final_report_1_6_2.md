# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

> **Pending Human Adjudication.** All 19 candidates remain Pending Human Adjudication. Evidence states, review domains and inclusion audits describe the review record; they are not human adjudications.

## Executive Quality-Control Summary

Complete fresh review of all 134 supplied PDF pages produced **19 stable candidates**, consolidating 29 included findings from 30 independently screened findings. The audit confirmed inclusion for 18 candidates and questioned inclusion for C008, whose full source-based reason is retained. Exact-source rechecks recorded 18 candidates as `reproduced` and C008 as `reproduced_after_transcription_correction`.

Candidates concern printed counts and percentages, effect-measure derivation, uncertainty intervals, outcome attribution, and planned-versus-reported endpoint, intervention and analysis specifications. Repeated occurrences are preserved within one candidate card per issue. The cards identify bounded relevance for evidence extraction and retain source-grounded alternatives and missing definitions; no propagation, paper-level conclusion change or harm is established.

## Package and Reused-Evidence Provenance

The supplied package contains exactly three direct PDFs. Document roles follow content: the trial article and results supplement are REPORT; the protocol/SAP/amendment/prospective SMS bundle is PLAN. No supplied Office, workbook or CSV source is present.

| Source ID | Actual source filename | Role | PDF pages |
|---|---|---|---:|
| DOC-001 | jama_zahid_2025_oi_250093_1768590553.08463.pdf | REPORT | 9 |
| DOC-002 | joi250093supp1_prod_1768590553.08963.pdf | PLAN | 109 |
| DOC-003 | joi250093supp2_prod_1768590553.09463.pdf | REPORT | 16 |

The curator inventoried and hashed 386 reusable extraction, image and metadata artifacts. Article native/normalized text and layout, results-supplement text/images, and all 109 PLAN rendered page locators supported the new mapping. PLAN native/layout text is garbled; its twelve empty OCR files and seven partial nonempty OCR files were treated as limited aids. All PLAN pages received visual mapping. Historical extraction engine versions are not consistently documented. Reused images/text are locators and transcription aids, while the exact supplied PDF pages remain authoritative.

Current provenance is recorded in the [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [source hash baseline](review_1_6_2/source_hashes_before.sha256) and [reused-asset hash baseline](review_1_6_2/reused_artifact_hashes_before.sha256). Earlier scientific selections and dispositions were preserved and excluded from discovery inputs.

## Scope, Complete Coverage, and Exclusions

The review covers counts/denominators, estimate/test logic, statistical method logic, and planned-versus-reported statistical design under [QUALITY_CONTROL_SCOPE.md](../QUALITY_CONTROL_SCOPE.md). Every PDF page is a stable unit, including front matter, administrative material and unreported-phase context.

| Source | Total units | Reusable units | Fresh-required units | Freshly mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | 109 | 109 | 0 | 109 | COMPLETE |
| DOC-003 | 16 | 16 | 0 | 16 | COMPLETE |
| **Total** | **134** | **134** | **0** | **134** | **COMPLETE** |

Reusable and fresh-required extraction counts partition the unique source units. Zero fresh-required units means usable locators existed for every page; it does not mean earlier scientific mapping was adopted. Fresh main/support mapping covered all 134 units. The [source coverage ledger](review_1_6_2/source_coverage.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) record closure and disjoint assignments.

The scope excludes broad methodology, clinical merit, novelty, misconduct, raw-data review and preferences for another analysis. Peripheral comparisons, context-resolved wording, model-versus-crude comparisons, unsupported conditional observations and display-precision differences were screened under the stated rules. No coverage or candidate-count target governed inclusion.

## Quantitative and Statistical Relationship Coverage

Fresh maps enumerate **212 numeric relationships**, **114 statistical relationships** and **90 cross-source relationships**. Numeric records N001–N119 and N201–N293 are COMPLETE. Statistical records S001–S114 each have both `PASS_1_COMPLETE` and `PASS_2_COMPLETE` records. The two statistical stages used fresh, distinct high-effort agents, with disjoint evidence shards and complete merged coverage.

Pass 1 examined count/denominator, containment, direction, estimate/test, effect-measure, method and planned-design logic. Pass 2 revisited every statistical relationship, all 19 stable candidates, the screening decisions and exact-source recheck facts. It independently revisited all **45 actual initial checker excluded-observation rows** and added one new excluded precision observation concerning main CO<6 per-protocol 39/318 and printed 11.9%. Its relative percentage gap is 0.011589, and its RD gap is 0.001913; these are within the 0.05 rule. Pass 2 produced no new findings, so no second independent finding-screen stage was applicable.

The audit reconciled duplicate observation crosswalks to existing C006/C004 rather than adding issues. It also recorded the governing monthly-mean sum 174.29 from the supplied inputs, while preserving the earlier 174.19 handoff; half-unit intervals still overlap the printed total and the precision exclusion remains unchanged. These are process reconciliations, not additional candidates.

Complete relationship evidence is in the [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_2/statistics/relationship_inventory.md), [statistical pass 1](review_1_6_2/checkers/statistical_pass_1.md), [statistical pass 2](review_1_6_2/checkers/statistical_pass_2.md), [cross-source check](review_1_6_2/checkers/cross_source_consistency.md) and [quality audit](review_1_6_2/quality/evidence_quality_audit.md).

## Inclusion Screening Summary

Inclusion requires reproduction and either an always-register Route A category or all Route B criteria: in focus, unresolved by immediate context, and bearing on interpretation or extraction. Numeric comparisons allow each displayed input/output its half-unit interval; a remaining relative gap at most 0.05 is display precision. Interval-versus-P/test conflicts are exempt from that rounding rule. A display-zero P value alone does not qualify.

| Screening decision | Findings | Reason code | Stable candidate groups |
|---|---:|---|---:|
| INCLUDE | 29 | MEETS_THRESHOLD | 19 |
| SCREENED_OUT | 1 | CONDITIONAL_OR_UNREPORTED | 0 |
| **Total** | **30** | | **19** |

| Screened-out reason code | Findings in independent screening log |
|---|---:|
| NOT_REPRODUCED | 0 |
| ROUNDING_OR_DISPLAY_PRECISION | 0 |
| NOTATION_OR_TYPOGRAPHY | 0 |
| TERMINOLOGY_OR_WORDING | 0 |
| MODEL_VERSUS_CRUDE | 0 |
| CONTEXT_RESOLVES | 0 |
| CONDITIONAL_OR_UNREPORTED | 1 |
| PERIPHERAL_COMPARISON | 0 |
| OUT_OF_FOCUS | 0 |
| DUPLICATE_OF_INCLUDED | 0 |
| **Total SCREENED_OUT** | **1** |

F-ST1-007 was screened out because country-stratified computer-generated lists can implement volume-and-country minimization; an omitted implementation detail does not establish a printed incompatible algorithm or result. Multiple INCLUDE findings consolidated into one issue retain all 29 finding memberships. The 45 checker exclusions and one pass-2 precision exclusion are separate observation records, not additional findings in the screening-log denominator. The audit created no new findings and changed no initial screening decisions. C008’s questioned inclusion audit remains visible without suppressing its stable ID. Counts reconcile to the [independent inclusion screen](review_1_6_2/screening/inclusion_screen.md).

## Review-Domain Summary

`statistical_results` covers result counts, estimates, intervals, tests and method logic; `report_internal_inconsistency` covers conflicting result attribution within report materials; `protocol_report` covers REPORT versus PLAN statistical design/analysis specifications; `plan_material` covers relevant conflicts solely inside PLAN material.

| Review domain | Candidates |
|---|---:|
| statistical_results | 6 |
| report_internal_inconsistency | 1 |
| protocol_report | 10 |
| plan_material | 2 |
| **Total** | **19** |

| Primary relationship type | Definition | Candidates |
|---|---|---:|
| P_R | REPORT versus PLAN | 10 |
| P_P | PLAN versus PLAN | 2 |
| S_C | Different REPORT documents | 1 |
| S_W | Within one REPORT document | 6 |
| **Total** | | **19** |

Mixed relationships use precedence P_R > P_P > S_C > S_W. Corroborating documents do not create conflicting relationships. Every card preserves its complete relationship list and compared-role string from the current ledger.

| Evidence state | Candidates |
|---|---:|
| reproduced | 18 |
| reproduced_after_transcription_correction | 1 |
| not_reproduced | 0 |
| **Total** | **19** |

| Inclusion audit | Candidates |
|---|---:|
| CONFIRMED | 18 |
| QUESTIONED | 1 |
| **Total** | **19** |

## Candidate Index

| Stable ID | Candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001) | Protocol SMS totals and frequency schedules do not reconcile | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#c002) | Operational eligibility criteria differ from the plan list | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#c003) | Prospective quit-date and reminder calendar differ from the report | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#c004) | Primary cotinine verification lacks a planned-to-reported criterion crosswalk | protocol_report | P_R | reproduced | CONFIRMED |
| [C005](#c005) | Primary model changes from protocol Poisson/log link to SAP/report logistic | protocol_report | P_R | reproduced | CONFIRMED |
| [C006](#c006) | Risk-ratio derivation from stated logistic analysis is unclear | statistical_results | S_W | reproduced | CONFIRMED |
| [C007](#c007) | Planned tobacco-use-form adjustment has no reported primary counterpart | protocol_report | P_R | reproduced | CONFIRMED |
| [C008](#c008) | CO<6 sensitivity results appear under a primary-outcome status label | protocol_report | P_R | reproduced_after_transcription_correction | QUESTIONED |
| [C009](#c009) | Primary missing-outcome handling differs between protocol and SAP/report | protocol_report | P_R | reproduced | CONFIRMED |
| [C010](#c010) | Prespecified gender-specific primary analyses are not reported | protocol_report | P_R | reproduced | CONFIRMED |
| [C011](#c011) | Current primary-data attrition assumptions differ | protocol_report | P_R | reproduced | CONFIRMED |
| [C012](#c012) | All-cause mortality percentage is attributed to TB-specific mortality | report_internal_inconsistency | S_C | reproduced | CONFIRMED |
| [C013](#c013) | Adverse-event narrative reverses two any-symptom arm directions | statistical_results | S_W | reproduced | CONFIRMED |
| [C014](#c014) | Fourteen interval rows do not reproduce a rule fitting other display rows | statistical_results | S_W | reproduced | CONFIRMED |
| [C015](#c015) | Latest protocol and SAP prescribe different failure windows | plan_material | P_P | reproduced | CONFIRMED |
| [C016](#c016) | Current Phase3 power statements retain different cluster allocations | plan_material | P_P | reproduced | CONFIRMED |
| [C017](#c017) | Two cause-of-death percentages do not reconcile within eTable4 | statistical_results | S_W | reproduced | CONFIRMED |
| [C018](#c018) | Site 2008 death count and percentage do not reproduce the table denominator | statistical_results | S_W | reproduced | CONFIRMED |
| [C019](#c019) | Treatment-failure absolute difference has the opposite signed contrast | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

The following cards contain every stable ID in source order. All remain Pending Human Adjudication. Exact source links use the actual package filenames and PDF page numbers.

## C001 — Protocol SMS totals and frequency schedules do not reconcile

Pending Human Adjudication.

**Candidate statement:** Protocol SMS totals and frequency schedules do not reconcile.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.16,53 and SAP p.80 vs REPORT DOC-001 pp.1,3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: the randomized intervention's planned message dose/duration is an expressly permitted planned-versus-reported element. B2: each protocol paragraph pairs a per-participant total with a frequency schedule that cannot produce it even under widened half-unit allowances; pilot-refinement permission does not name the governing revised schedule. B3: the extractable intervention schedule attached to the primary six-month abstinence RR 3.0 is unresolved. The issue is bounded to printed intervention specifications.

**Finding IDs:** F-NUM-104, F-XS-005

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 1](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), abstract intervention; REPORT.
- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Intervention; REPORT.
- [DOC-002 — PDF p. 16](<../joi250093supp1_prod_1768590553.08963.pdf#page=16>), lines386–390, earlier-component dose paragraph; PLAN.
- [DOC-002 — PDF p. 53](<../joi250093supp1_prod_1768590553.08963.pdf#page=53>), lines1526–1530, later-component dose paragraph; PLAN.
- [DOC-002 — PDF p. 77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>), change note; PLAN.
- [DOC-002 — PDF p. 80](<../joi250093supp1_prod_1768590553.08963.pdf#page=80>), lines2532–2536, SAP dose; PLAN.

**Source evidence:** The earlier-component paragraph says each participant receives 178 SMS over six months: first two months 4–5/day, next two months 2–3/day, final two months 1–2/week. The later-component paragraph says 134 SMS: first two months 4–5/day, next two months 1–2/day, final two months 1/week. SAP says 134 over six months, 3–4/day in month 1, 1/day in month 2, then 1/month for months 3–6. The report says 100 in month 1, 30 in month 2, and four further messages, one monthly during months 3â6: 134 total.

**Reported-versus-comparator:** Protocol totals 178/134 and daily/weekly segments versus SAP/report 134 and a two-month daily/four-month monthly schedule.

**Reasoning procedure:** Enumerate each transmission segment, calculate conservative minima and widened half-unit schedule enclosures, then compare the reported and prospective phase-specific schedules.

**Calculation:** Nominal conservative 28-day-month minima are 344 and 288, respectively. Allow every two-month duration [1.5,2.5] months, every frequency endpoint ±0.5, and calendar months 28–31 days: earlier enclosure [213,725.178572], later [171,636.607143]; totals178±0.5 and 134±0.5 yield gaps34.5/178=.193820 and 36.5/134=.272388. For month 2, later-protocol lower 4/day±.5 and report1/day±.5 yield gap 2/day, relative 2.0. The categorical duration/frequency schedules also differ. The amendment between 178 and 134 totals is context, not an independent finding.

**Affected result or extracted value:** Planned per-participant intervention dose and the delivered schedule attached to the primary abstinence RR 3.0[2.0,4.9].

**Why context does not resolve it:** The same protocol paragraphs state per-participant receipts and transmission schedules; immediate pilot-refinement permission does not identify which quantitative schedule governs or reconcile the internal totals. This is intervention dose in the permitted cross-comparison tier, not general intervention critique.

**Alternative source-grounded interpretations:** Totals could denote unique templates/branches rather than actual transmissions, or the protocol could retain a preliminary schedule. SAP/report could implement a pilot-refined schedule. The affected paragraphs do not define those substitutions. Actual delivery logs and a schedule revision crosswalk are absent.

Missing definition to resolve: What per-participant totals and phase-specific transmission schedules governed Phase 3, and how do the protocol's178/134 totals and printed daily/weekly segments map to the SAP/report's134-message schedule?

**Classification rationale:** Prospective protocol and SAP content are PLAN; implemented intervention descriptions are REPORT. Internal protocol schedule/total contrasts and protocol–SAP contrast give P_P; protocol–report gives P_R, which has precedence. Agreeing report abstract/SAP passages corroborate the implemented side and do not create S_C.

**Classification ambiguity:** Unique templates or branching might differ from per-person transmissions; pilot refinement is expressly possible. Actual transmissions and the applied schedule revision are absent.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. REPORT [DOC-001 p.1](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) states daily messages for two months, then monthly for four; [p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) specifies 134 unique messages: 100 in month 1, 30 in month 2, four thereafter. PLAN [DOC-002 p.16](<../joi250093supp1_prod_1768590553.08963.pdf#page=16>), lines386–390, prints each participant receiving 178 over six months, first two months 4–5/day, next two 2–3/day, final two 1–2/week. PLAN [p.53](<../joi250093supp1_prod_1768590553.08963.pdf#page=53>), lines1526–1530, prints 134, first two months 4–5/day, next two 1–2/day, last two 1/week. PLAN SAP [p.80](<../joi250093supp1_prod_1768590553.08963.pdf#page=80>), lines2532–2536, prints 134: month1 3–4/day, month2 1/day, final four months 1/month. PLAN [p.77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>) change note was found; it lists sample-size, outcome and operational changes but does not supply a schedule crosswalk. Adjacent pp.16,53,80 permit pilot refinement.

Inputs available; exact missing inputs: All printed totals, phase lengths and frequencies are available. Actual per-person transmission logs, whether counts denote unique templates rather than transmissions, and the implemented pilot-revision crosswalk are absent.

Determining recheck fact: Both within-paragraph totals remain below conservative rounded schedule minima, and the month 2 protocol/report schedules remain separated.

**Potential downstream evidence impact:** If confirmed, intervention dose/frequency metadata attached to the primary abstinence effect could differ in an evidence-extraction table.

## C002 — Operational eligibility criteria differ from the plan list

Pending Human Adjudication.

**Candidate statement:** Operational eligibility criteria differ from the plan list.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.11,49 vs REPORT DOC-001 pp.2,4 and DOC-003 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: the explicitly planned recent-stop/reduction exception and the reported operational reader exclusion bear on the primary analysis population. B2: phone access is not an immediate equivalent of an available SMS reader, and the finite plan lists do not map the exception to the≥25-day condition. B3: eligibility definitions attached to the 1080-participant primary trial can be copied differently. No changed participant count is inferred.

**Finding IDs:** F-XS-008

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 2](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>), eligibility paragraph; REPORT.
- [DOC-001 — PDF p. 4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 exclusions; REPORT.
- [DOC-002 — PDF p. 11](<../joi250093supp1_prod_1768590553.08963.pdf#page=11>), lines235–255 complete participant lists; PLAN.
- [DOC-002 — PDF p. 49](<../joi250093supp1_prod_1768590553.08963.pdf#page=49>), lines1375–1395 complete participant lists; PLAN.
- [DOC-003 — PDF p. 3](<../joi250093supp2_prod_1768590553.09463.pdf#page=3>), eTable1 smoking and SMS-reader reasons; REPORT.

**Source evidence:** Both plan lists permit daily smoking or stopping/reducing below daily since TB diagnosis and require personal mobile access; neither lists ≥25 smoking days or a patient/household SMS reader. Main report requires≥25 days in the last month. Figure1/eTable 1 include236 excluded for inability to read with no household reader; eTable 1 gives7069 not meeting the recent-smoking rule.

**Reported-versus-comparator:** Planned daily-smoking/recent-reduction exception and personal phone access versus reported ≥25-day smoking and patient/household SMS-reader conditions.

**Reasoning procedure:** Match every item in both complete planned eligibility lists to the operational report and exclusion display; retain overlapping exclusion reasons without deriving unique participant deficits.

**Calculation:** Match each finite eligibility-list item. Diagnosis, age, consent, quit willingness and mobile access match; the explicit recent-reduction exception and reader criterion do not have matched counterparts. Reasons overlap, so236 is a reason count rather than an inferred additional unique exclusion deficit; no adjusted population-size arithmetic is asserted.

**Affected result or extracted value:** Selection rules for 1080 randomized participants and the population to which the primary abstinence estimate applies.

**Why context does not resolve it:** These are actual operational selection rules with a printed exclusion reason, not interchangeable wording for daily smoking/phone ownership. The plan exception can permit patients failing the report's recent-smoking requirement.

**Alternative source-grounded interpretations:** Some recent reducers may meet25 days; a later operational amendment might introduce the reader rule. The amount of participant overlap and any amendment are absent.

Missing definition to resolve: Were recent-stop/reduction smokers eligible as planned, and where were the≥25-day and patient/household SMS-reader criteria prespecified or amended?

**Classification rationale:** Planned prospective eligibility versus actual selection gives P_R/protocol_report. Report and results supplement agree on the exclusion and are corroborating locations, not an S_C conflict.

**Classification ambiguity:** Some recently reduced smokers could meet25days; a later operational amendment could govern. Criterion overlap and amendment provenance are missing.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. PLAN [DOC-002 p.11](<../joi250093supp1_prod_1768590553.08963.pdf#page=11>), lines235–255, and [p.49](<../joi250093supp1_prod_1768590553.08963.pdf#page=49>), lines1375–1395, contain complete participant lists: daily smoking OR stopping/reducing below daily only since diagnosis, and personal-mobile access; neither lists a ≥25-day or SMS-reader criterion. REPORT [DOC-001 p.2](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=2>) defines daily smoking as at least one puff on ≥25 days in the last month. [p.4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) Figure1 prints236 unable to read with nobody at home able to read SMS; REPORT [DOC-003 p.3](<../joi250093supp2_prod_1768590553.09463.pdf#page=3>) eTable1 prints the corresponding236 and7069 not smoking at least25 days in the past month.

Inputs available; exact missing inputs: Printed criteria and reason counts are available. Individual criterion overlap, the number uniquely excluded by each changed rule, and any implementing amendment are absent.

Determining recheck fact: The complete planned lists retain the recent-stop/reduction exception and lack the reported recent-smoking and SMS-reader criteria.

**Potential downstream evidence impact:** If confirmed, the eligibility and population-definition metadata accompanying the primary trial effect could differ; no change in the randomized count is established.

## C003 — Prospective quit-date and reminder calendar differ from the report

Pending Human Adjudication.

**Candidate statement:** Prospective quit-date and reminder calendar differ from the report.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SMS log pp.101,103,104,109 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: quit date defines the primary continuous-abstinence start, and the dated reminders define the randomized intervention calendar. B2: Q(−8), the ordinal8th-day wording and 5 days after enrollment are not mapped by the supplied clock definitions or immediate report description. B3: the extractable endpoint-start/intervention timing differs. Participant-level implementation and outcome reclassification are not inferred.

**Finding IDs:** F-XS-006

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes and Trial Intervention; REPORT.
- [DOC-002 — PDF p. 101](<../joi250093supp1_prod_1768590553.08963.pdf#page=101>), enrollment Q(−8)/Tx(+1), message6 and footnotes; PLAN.
- [DOC-002 — PDF p. 103](<../joi250093supp1_prod_1768590553.08963.pdf#page=103>), Q(−1)/Tx(+8) and quit transition; PLAN.
- [DOC-002 — PDF p. 104](<../joi250093supp1_prod_1768590553.08963.pdf#page=104>), quit-date ordinal label and messages39–44; PLAN.
- [DOC-002 — PDF p. 109](<../joi250093supp1_prod_1768590553.08963.pdf#page=109>), messages129–134 and follow-up phase; PLAN.

**Source evidence:** Report sets quit date5 days after enrollment and sends4 messages,1/month during months 3–6. Log pairs enrollment withQ(−8)/Tx(+1), Q(−1)/Tx(+8) with a tomorrow-quit instruction, and quit date with “8th day since joining mTB-Tobacco”; message6 atQ(−7) says7 days from today. Final daily messages endQ(+41)/Tx(+50). Reminder132 isQ(+52)/Tx(+61),133Q(+112)/Tx(+121),134Q(+180)/Tx(+189), with texts naming treatmentmonths2,4,6.

**Reported-versus-comparator:** Prospective Q(−8)/ordinal eighth-day quit anchor and dated reminders versus reported five days after enrollment and monthly reminders in months 3–6.

**Reasoning procedure:** Read the Q/Tx footnotes and all dated quit/reminder anchors; compare elapsed-day and inclusive ordinal alternatives against the report schedule.

**Calculation:** For the direct Q(−8) versus 5-day anchors, rounded ranges[7.5,8.5] and[4.5,5.5] yield gap 2/5=.40. Inclusive ordinal-day reading could yield7elapsed days; [6.5,7.5] versus[4.5,5.5] yields gap 1/5=.20. Three versus four reminders alone has touching count intervals and does not qualify independently. The different dated calendar and primary-start anchors remain the basis.

**Affected result or extracted value:** Start of the primary continuous-abstinence assessment and intervention reminder timing/duration.

**Why context does not resolve it:** Neither the dated prospective log nor report maps joining, enrollment and treatment clocks to the other schedule or identifies an implemented revision; the primary endpoint is defined since quit date.

**Alternative source-grounded interpretations:** The log may be preliminary and refined after piloting; enrollment and treatment dates may differ; ordinal day numbering may count enrollment as day1. The report's actual delivered-log revision and clock crosswalk are absent.

Missing definition to resolve: How do the report's5 days after enrollment and the log'sQ(−8)/“8th day since joining” quit anchors map, and which reminder-calendar revision was delivered?

**Classification rationale:** A prospective operational message log is PLAN by content; actual reported endpoint/intervention timing is REPORT. This is P_R/protocol_report. No plan-only clock contrast is registered separately.

**Classification ambiguity:** Joining, enrollment, quit-date and treatment clocks require a supplied crosswalk; ordinal counting and pilot refinement are alternative explanations.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. REPORT [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) sets quitdate5 days after enrollment and four reminders, one/month in months3–6. PLAN prospective [DOC-002 p.101](<../joi250093supp1_prod_1768590553.08963.pdf#page=101>) labels enrollment Q(−8)/Tx(+1); footnotes define Q as days to quitdate and Tx(+1) as first treatment day; message6 atQ(−7) says seven days from today. [p.103](<../joi250093supp1_prod_1768590553.08963.pdf#page=103>) labels Q(−1)/Tx(+8) and message38 quitting tomorrow. [p.104](<../joi250093supp1_prod_1768590553.08963.pdf#page=104>) labels QUIT DATE the8th day since joining; messages39–44 are quit-day messages. [p.109](<../joi250093supp1_prod_1768590553.08963.pdf#page=109>) ends daily messages129–131 atQ(+41)/Tx(+50), then reminder132Q(+52)/Tx(+61),133Q(+112)/Tx(+121),134Q(+180)/Tx(+189), naming treatmentmonths2,4,6.

Inputs available; exact missing inputs: Log timing labels, footnote definitions and report schedule are available. Delivered-log revision, enrollment/joining/treatment clock crosswalk and operational quit-date choice are absent.

Determining recheck fact: The footnoted Q(−8) enrollment anchor and ordinal label cannot be matched to the reported5-day anchor by ordinary half-unit precision; no explicit clock crosswalk is printed.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a different continuous-abstinence start or intervention reminder calendar.

## C004 — Primary cotinine verification lacks a planned-to-reported criterion crosswalk

Pending Human Adjudication.

**Candidate statement:** Primary cotinine verification lacks a planned-to-reported criterion crosswalk.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 pp.8,47,84 vs REPORT DOC-001 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: this compares explicit planned and implemented primary biochemical endpoint decision specifications. B2: the named graded NicAlert level <3 rule and binary-negative AllTest rule do not supply a common concentration definition; assay names do not establish equivalence. B3: the verification criterion attached to primary abstinence among concomitant smokeless-tobacco users cannot be extracted as a single supplied numeric criterion. This is not a demonstrated concentration change or changed event count.

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Trial Outcomes cotinine verification; REPORT.
- [DOC-002 — PDF p. 8](<../joi250093supp1_prod_1768590553.08963.pdf#page=8>), lines158–161 primary endpoint; PLAN.
- [DOC-002 — PDF p. 47](<../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1298–1301 primary endpoint; PLAN.
- [DOC-002 — PDF p. 84](<../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2661–2665 SAP primary endpoint; PLAN.

**Source evidence:** Protocol names Accutest NicAlert strips on a 0–6scale and level <3, described as 100–200 ng/mL, as abstinence. SAP repeats the graded level <3criterion. Report names a Hangzhou AllTest rapid-test cassette and defines a negative result as verification of abstinence for concomitant smokeless-tobacco use.

**Reported-versus-comparator:** Planned NicAlert graded level <3 criterion versus reported negative AllTest cassette criterion; concentration equivalence is undefined.

**Reasoning procedure:** Match the named assay, scale and abstinence decision criterion; identify the absent concentration crosswalk without inferring assay nonequivalence.

**Calculation:** Match the explicit primary classification procedure and decision criterion: graded level <3 on a specified strip versus a binary negative result on a named different cassette. Numerical threshold equivalence cannot be computed because the cassette negative-result concentration is absent. No numerical threshold discrepancy or participant reclassification is asserted.

**Affected result or extracted value:** Biochemical primary-abstinence classification among baseline concomitant smokeless-tobacco users.

**Why context does not resolve it:** The supplied sources specify different decision outputs and named assays for the same primary classification, with no mapping; a reader cannot identify the operative concentration criterion from immediate report text. This is an endpoint specification comparison within focusD, not a critique of assay choice.

**Alternative source-grounded interpretations:** The cassette negative cutoff may implement exactly the planned graded threshold, or an amended criterion may have been used. Those are source-bounded alternatives; equivalence is not inferable from assay names. The assay crosswalk is absent.

Missing definition to resolve: What concentration criterion defined a negative AllTest cassette result, and how did it implement the planned NicAlertlevel <3primary criterion?

**Classification rationale:** Protocol/SAP endpoint rules are PLAN; the implemented endpoint procedure is REPORT. All relationships are P_R, hence protocol_report. Agreement among plan passages introduces no P_P.

**Classification ambiguity:** Equivalent classifications by the two assays remain possible. The cutoff crosswalk and applicable assay amendment are absent.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. PLAN [DOC-002 p.8](<../joi250093supp1_prod_1768590553.08963.pdf#page=8>), lines158–161, and [p.47](<../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1298–1301, name Accutest NicAlert strips, graded0–6, level<3, described as100–200ng/mL. PLAN SAP [p.84](<../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2661–2665, repeats graded0–6 andlevel<3. REPORT [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names Hangzhou AllTest rapid-test cassette; a negative result verifies abstinence for concomitant baseline smokeless-tobacco use.

Inputs available; exact missing inputs: Named procedures and decision outputs are available; cassette concentration cutoff, grade-to-binary mapping and any assay amendment are absent.

Determining recheck fact: The report uses a differently named assay/output without stating how its negative result implements the planned graded criterion.

**Potential downstream evidence impact:** If confirmed, primary biochemical-verification metadata could specify a different or incompletely defined decision criterion; no event-count effect is established.

## C005 — Primary model changes from protocol Poisson/log link to SAP/report logistic

Pending Human Adjudication.

**Candidate statement:** Primary model changes from protocol Poisson/log link to SAP/report logistic.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP pp.91,92 and REPORT DOC-001 p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category5: the planned Poisson/log-link primary analysis has no supplied reported counterpart, and SAP/report name logistic analysis for that categorical primary endpoint. SAP/report agreement or a possible superseding plan is an alternative explanation, not removal of this always-register planned-analysis comparison.

**Finding IDs:** F-XS-001, F-ST1-003

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Statistical Analysis; REPORT.
- [DOC-002 — PDF p. 28](<../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764 statistical-analysis paragraph; PLAN.
- [DOC-002 — PDF p. 66](<../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016 statistical-analysis paragraph; PLAN.
- [DOC-002 — PDF p. 77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>), change note; PLAN.
- [DOC-002 — PDF p. 91](<../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2884–2889 primary model; PLAN.
- [DOC-002 — PDF p. 92](<../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926 adjusted model; PLAN.

**Source evidence:** Both protocol statistical-analysis paragraphs specify generalized linear mixed models with log link and underlying Poisson distribution, cluster random intercept, crude/adjustedRRs and 95% CIs. SAP specifies mixed-effects logistic regression with site random effect andRR; report specifies logistic regression within the mixed-effects framework for categorical outcomes.

**Reported-versus-comparator:** Protocol Poisson/log-link primary model versus SAP/report logistic model for the same categorical endpoint.

**Reasoning procedure:** Match the primary endpoint across named model families/links and inspect the supplied amendment context for a replacement mapping.

**Calculation:** Compare explicitly named families/links for the same primary six-month binary abstinence analysis: log(p)=η versus logit(p)=η are distinct model specifications. No display-precision rule applies to categorical model-family statements. The supplied change note identifies other amendments but gives no model-replacement mapping.

**Affected result or extracted value:** Primary ITTRR 3.0[2.0,4.9], adjustedRR3.2[2.2,5.2], and their analysis-prespecification provenance.

**Why context does not resolve it:** Route A category5 registers a planned primary analysis replaced/notreported; SAP/report agreement does not remove the protocol's planned model or document its replacement.

**Alternative source-grounded interpretations:** SAP may supersede the protocol; a separate Poisson analysis may exist; the report's family wording may describe another computation. Model code, hierarchy and replacement disclosure are absent.

Missing definition to resolve: Which family/link generated the reported primary RRs/CIs, and where is the protocol Poisson/log-link replacement or distinct-analysis mapping documented?

**Classification rationale:** Protocol–SAP gives P_P; protocol–report gives P_R. P_R takes precedence, giving protocol_report. A physical supplement containing the plan remains PLAN.

**Classification ambiguity:** Final plan hierarchy, actual fitted family/link and whether a separate Poisson analysis exists remain unknown.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. PLAN [DOC-002 p.28](<../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764, and [p.66](<../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016, state generalized linear mixed models, log link, underlying Poisson distribution, cluster random intercept and crude/adjustedRRs with95%CIs. PLAN SAP [p.91](<../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2884–2889, states mixed-effects logistic regression for the primary result, site random effect andRR; [p.92](<../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926, also names logistic. REPORT [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) states logistic regression within the mixed-effects framework for categorical outcomes. PLAN [DOC-002 p.77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>) change note gives other amendments but no model replacement.

Inputs available; exact missing inputs: Model-family text, random-effect statements and primary-analysis attribution are available. Final fitted code, protocol/SAP hierarchy, model replacement disclosure and result-to-model mapping are absent.

Determining recheck fact: Both protocol model paragraphs retain Poisson/log-link while SAP/report print logistic for the primary categorical analysis.

**Potential downstream evidence impact:** If confirmed, extracted primary model-family and prespecification metadata could differ. An alternative treatment-effect estimate is not calculated.

## C006 — Risk-ratio derivation from stated logistic analysis is unclear

Pending Human Adjudication.

**Candidate statement:** Risk-ratio derivation from stated logistic analysis is unclear.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.3 method vs REPORT DOC-001 p.6 RR labels; REPORT DOC-003 pp.11,13,14 affected displays

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: a source-grounded model-to-effect-measure chain is statistical method logic. B2: logistic regression plus anRR label alone does not identify the required prediction/conversion or different fitted link, and immediate methods/table notes do not state one. B3: the conditional or marginal risk estimand attached to primaryRR3.0/3.2 and its uncertainty is unresolved. This is not a demonstration that a coefficient odds ratio was numerically printed as a risk ratio.

**Finding IDs:** F-ST1-002

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), Statistical Analysis categorical model; REPORT.
- [DOC-001 — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 RR columns and notea; REPORT.
- [DOC-003 — PDF p. 11](<../joi250093supp2_prod_1768590553.09463.pdf#page=11>), eTable7 relative-risk row; REPORT.
- [DOC-003 — PDF p. 13](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9 RR columns; REPORT.
- [DOC-003 — PDF p. 14](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>), eTable9 notee; REPORT.

**Source evidence:** The report states mixed-effects logistic regression for categorical outcomes. Table 2 labels primary 3.0 [2.0,4.9] and adjusted 3.2 [2.2,5.2] as RR; eTables 7/9 repeat RR labels.

**Reported-versus-comparator:** Reported logistic mixed-effects model versus RR output labels without an identified prediction/conversion step.

**Reasoning procedure:** Trace the stated categorical model to the named effect measure; distinguish coefficient odds ratios from risk quantities requiring another operation, without assuming which computation occurred.

**Calculation:** For logit(p)=η, exponentiating a treatment coefficient produces an OR. An RR requires prediction, standardization, conversion, or a different fitted link. No step is named between the stated logistic model and these risk-based estimates; no OR-to-RR numerical identity or crude-ratio discrepancy is asserted.

**Affected result or extracted value:** The risk-based estimand and uncertainty attached to primary RR 3.0/3.2 and other displayed RRs.

**Why context does not resolve it:** A needed estimand-producing step is absent from the stated model-to-effect-measure chain, leaving marginal versus conditional risk quantities unidentified from immediate methods and notes.

**Alternative source-grounded interpretations:** Standardized predicted risks may produce the RRs; a log-link model may have been fitted; logistic wording may describe a separate analysis. Model code, averaging distribution, conversion rule and row-specific mapping are absent.

Missing definition to resolve: What prediction, standardization, conversion or fitted-link rule produced the printed RRs and CIs from the stated logistic mixed-effects analysis?

**Classification rationale:** Main method-to-label comparison is inside one REPORT, giving S_W/statistical_results. Supplementary risk labels repeat affected output conventions; they do not conflict with main risk labels and therefore do not create S_C. A corroborating SAP is not a relationship.

**Classification ambiguity:** A legitimate predicted-risk derivation, another fitted link or separate analysis is possible. Conditional versus marginal estimand andCI construction are missing definitions.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. REPORT [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) names mixed-effects logistic regression for categorical outcomes. REPORT [p.6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 prints primaryRR3.0[2.0,4.9], adjustedRR3.2[2.2,5.2], and RR labels for remaining fitted categorical rows; notea names mixed-effects models forRR. REPORT [DOC-003 p.11](<../joi250093supp2_prod_1768590553.09463.pdf#page=11>) eTable7 ends with a relative-risk95%CI row; [p.13](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>) eTable9 prints crude/adjustedRR columns including primary2.9[1.8,6.4]/3.1[1.9,6.5]; [p.14](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>) notee names mixed-effectsRR models, without a risk-conversion rule.

Inputs available; exact missing inputs: Model-family statement, risk labels and printed results are available. Fitted link per result, transformation/prediction formula, averaging distribution, conditional versus marginal estimand and correspondingCI procedure are absent.

Determining recheck fact: The logistic statement and RR result labels are present, but no operation connecting them is stated in the cited methods/notes.

**Potential downstream evidence impact:** If confirmed, an extractor could attach a different conditional or marginal risk estimand and uncertainty interpretation to the printed RRs.

## C007 — Planned tobacco-use-form adjustment has no reported primary counterpart

Pending Human Adjudication.

**Candidate statement:** Planned tobacco-use-form adjustment has no reported primary counterpart.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP p.92 vs REPORT DOC-001 pp.3,4,6 and DOC-003 p.14

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category5: the explicitly planned tobacco-use-form term in the fully adjusted primary model has no counterpart in repeated finite reported adjustment lists or a separately supplied planned-model result. Possible omission from the description is an alternative, not evidence that the planned result was supplied.

**Finding IDs:** F-XS-003, F-ST1-005

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), finite post hoc fixed-effect list; REPORT.
- [DOC-001 — PDF p. 4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Primary Outcome adjusted analysis; REPORT.
- [DOC-001 — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 notea; REPORT.
- [DOC-002 — PDF p. 92](<../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926 fully adjusted models; PLAN.
- [DOC-003 — PDF p. 14](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>), eTable9 notee; REPORT.

**Source evidence:** SAP fully adjusted models include sociodemographic variables alongside tobacco use form and other baseline characteristics. The report and Table 2/eTable 9 notes repeatedly give the finite post hoc set age, sex, education, occupation, smoking duration; tobacco form is absent. Primary adjusted RR is 3.2 [2.2,5.2] and death-excluded adjusted RR 3.1 [1.9,6.5].

**Reported-versus-comparator:** Planned tobacco-use-form adjustment versus the repeated finite five-term reported post hoc adjustment list.

**Reasoning procedure:** Match the explicitly planned primary covariate to every finite reported adjustment list and seek a separately reported planned-model result.

**Calculation:** Item-match the explicitly planned tobacco-form term to the finite reported list. No term or result for that prespecified fully adjusted primary model is supplied; precision is inapplicable to covariate inclusion.

**Affected result or extracted value:** Adjusted primary and sensitivity RRs and whether they represent the planned fully adjusted analysis.

**Why context does not resolve it:** Route A category 5 applies to a planned primary analysis replaced or not reported; post hoc selection does not supply the planned model's result.

**Alternative source-grounded interpretations:** Tobacco form may have been fitted but omitted from repeated descriptions, dropped intentionally or merged into another variable. The fitted list and planned-model result are absent.

Missing definition to resolve: Was tobacco use form included, and where is the planned fully adjusted primary result or its documented replacement?

**Classification rationale:** Prospective SAP adjustment rule versus reported model descriptions gives P_R/protocol_report. Agreement among reported lists is corroboration, without S_C/S_W conflict.

**Classification ambiguity:** The term might be fitted but omitted in prose, aliased, intentionally removed or amended. Actual model formula, term mapping and planned-model result are absent.



**Mechanical evidence recheck:** Location found; source and comparator matched: Every cited location was found. PLAN [DOC-002 p.92](<../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2919–2926, specifies fully adjusted models controlled for sociodemographic variables alongside tobacco-use form and other baseline characteristics. REPORT [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) gives post hoc fixed effects age, sex, education, occupation and smoking duration. REPORT [p.4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) adjusted-primary paragraph repeats those five andRR3.2[2.2,5.2]; [p.6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 notea gives the same five. REPORT [DOC-003 p.14](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>) eTable9 notee repeats those five for death-excluded adjusted results. All four affected reported descriptions were matched.

Inputs available; exact missing inputs: Planned covariate and reported lists are available. Actual model matrix/formula, any alias for tobacco form, the planned-model result and documented replacement are absent.

Determining recheck fact: Tobacco-use form is expressly planned yet lacks a counterpart in every cited reported primary/adjusted-model list.

**Potential downstream evidence impact:** If confirmed, adjustment-set and planned-versus-post-hoc provenance attached to primary/sensitivity RRs could differ.

## C008 — CO<6 sensitivity results appear under a primary-outcome status label

Pending Human Adjudication.

**Candidate statement:** CO<6 sensitivity results appear under a primary-outcome status label.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C, S_W

**Compared document roles:** PLAN DOC-002 p.84 primary definition vs REPORT DOC-001 p.6 and DOC-003 p.13 primary blocks; REPORT DOC-001 p.3 sensitivity statement

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** QUESTIONED
The printed headings and threshold descriptions reproduce, but an actual change of outcome status under Route A, category 5 is not established. Main methods explicitly call CO<6 a post hoc sensitivity performed for the primary outcome; eTable 9 explicitly identifies its entire display as post-hoc sensitivity. Grouping sensitivities of the primary construct under a primary-outcome block can reconcile the cited locations at once. The cited sources do not state that CO<6 became a prespecified primary endpoint. Thus the Route A5 premise depends on interpreting a block heading as formal endpoint hierarchy, and Route B2 is not established by these immediate contexts. This is an inclusion audit question, not a change to the original INCLUDE decision or the stable candidate's status.

**Finding IDs:** F-ST1-008

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), primaryCO<10 and posthocCO<6 sensitivity; REPORT.
- [DOC-001 — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 Primary outcome block, both CO<6 ITT and PP rows; REPORT.
- [DOC-002 — PDF p. 84](<../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2653–2669 primary endpoint; PLAN.
- [DOC-003 — PDF p. 13](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9 Primary outcomes CO<6row; REPORT.

**Source evidence:** SAP defines primary verification as CO<10 ppm. Main p.3 explicitly calls CO<6 post hoc sensitivity. Main p.6 nevertheless places both CO<6 rows in Primary outcome: ITT264/720 vs38/360, RR 3.7[2.4,5.8], adjusted 3.9[2.4,6.9]; PP264/667 vs39/318 (printed usual-care percentage 11.9%), RR 3.6[2.14,6.87], adjusted 3.8[2.3,7.7]. eTable 9, titled Post-hoc sensitivity analysis after excluding deaths, also places CO<6 under Primary outcomes:264/695 vs38/333, RR 3.6[2.4,5.4], adjusted 3.8[2.4,6.2]. The status convention remains an explicit alternative; promotion to a prespecified endpoint is not inferred.

**Reported-versus-comparator:** Planned CO<10 primary definition and explicitly post hoc CO<6 sensitivity versus primary-outcome block placement of all three CO<6 rows.

**Reasoning procedure:** Read the planned threshold, methods sensitivity statement, both main rows and the entire supplementary title/block; distinguish endpoint hierarchy from display grouping.

**Calculation:** Compare categorical outcome status for the same biochemical threshold. The primary-status block contains an alternative post hoc threshold alongside the prespecified primary threshold; numeric rounding does not apply.

**Affected result or extracted value:** Outcome-status extraction accompanying both main CO<6 ITT and PP rows and the supplementary excluding-deaths CO<6 row.

**Why context does not resolve it:** Route A category 5 applies to a reproduced planned-outcome status difference; the post hoc table title supplies a possible display convention without removing its printed Primary outcomes block.

**Alternative source-grounded interpretations:** The block may organize analyses of the primary construct, including sensitivities, rather than declare additional primary endpoints. That convention is not explicitly distinguished.

Missing definition to resolve: Do all three CO<6 rows retain post hoc sensitivity status despite placement in primary blocks, and what outcome-status metadata accompanies their estimates?

**Classification rationale:** Roles follow content: prospective SAP is PLAN, trial tables/methods are REPORT. The registered status comparison generates P_R, S_C and S_W, with P_R taking precedence and protocol_report following that type. Preserve these registered fields while carrying the ambiguity below; the underlying formal-status interpretation is not independently confirmed by this audit. The recheck's p.6 location correction and addition of S_W are supported, so its evidence state remains reproduced_after_transcription_correction.

**Classification ambiguity:** If primary blocks merely group analyses of the primary construct, the plan corroborates the CO<10 endpoint rather than providing a conflicting status statement. P_R and the cross-report status comparison therefore depend on the same unestablished formal-hierarchy reading. No hierarchy promotion, prespecification claim, or implemented threshold change is inferred.



**Mechanical evidence recheck:** Location found; source and comparator matched: All four cited locations were found. [DOC-002 p.84](<../joi250093supp1_prod_1768590553.08963.pdf#page=84>), lines2654–2660, defines the primary endpoint as six-month continuous abstinence verified by CO<10 ppm. [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) explicitly identifies CO<6 ppm as a post hoc sensitivity of the primary outcome. [DOC-001 p.6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2, places both CO<6 rows in the Primary outcome block: ITT 264/720 versus38/360, RR3.7 [2.4,5.8]; PP264/667 versus39/318, RR3.6 [2.14,6.87]. [DOC-003 p.13](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9, is explicitly titled Post-hoc sensitivity analysis (intention to treat) after excluding deaths, but its Primary outcomes block also contains CO<6:264/695 versus38/333, crudeRR3.6 [2.4,5.4], adjustedRR3.8 [2.4,6.2]. Every affected CO<6 row at the cited displays was confirmed.

Necessary inputs available; missing definitions: Threshold definitions, table titles, and block headings are available. The missing input is the intended status convention of the primary blocks: formal endpoint hierarchy versus grouping all analyses of the primary construct.

**Potential downstream evidence impact:** If confirmed, the outcome-status metadata accompanying CO<6 sensitivity estimates could differ. The questioned audit and explicit sensitivity context constrain this possibility.

## C009 — Primary missing-outcome handling differs between protocol and SAP/report

Pending Human Adjudication.

**Candidate statement:** Primary missing-outcome handling differs between protocol and SAP/report.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.28,66 vs PLAN DOC-002 SAP p.91 and REPORT DOC-001 pp.3,4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: missing-outcome handling for the primary ITT is focus D. B2: the separately headed protocol outcomes paragraph says MAR, while SAP/report assign missing primary outcomes nonabstinent status, without an outcome-specific mapping or replacement hierarchy. Adjacent economic text is a plausible restriction but does not expressly restrict the paragraph. B3: the missingness assumptions attached to primary ITT 300/720 versus 55/360 and RR 3.0 [2.0,4.9] could differ in extraction or interpretation. The observation is a printed specification contrast, not merely an absent imputation detail.

**Finding IDs:** F-XS-002, F-ST1-004

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), missing-primary-outcome paragraph; REPORT.
- [DOC-001 — PDF p. 4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 attrition and analysis totals; REPORT.
- [DOC-002 — PDF p. 28](<../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764 separately headed Statistical analysis; PLAN.
- [DOC-002 — PDF p. 66](<../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2012–2016 separately headed Statistical analysis; PLAN.
- [DOC-002 — PDF p. 91](<../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2890–2892 ITT and Russell Standard; PLAN.

**Source evidence:** Protocol says outcomes primarily analyzed in a missing-at-random architecture. SAP regards dropout/incomplete data as continuing smokers. Report treats missing primary outcomes as negative/not abstinent: 53/720 and 42/360, total 95, are missing; primary ITT retains 720/360 and complete-case sensitivity discards missing.

**Reported-versus-comparator:** Protocol missing-at-random architecture versus SAP/report deterministic missing-as-smoking primary classification.

**Reasoning procedure:** Read the separately headed protocol analysis paragraphs, SAP primary ITT rule and report missing-outcome handling; retain economic adjacency as an alternative restriction.

**Calculation:** MAR is a stated missingness architecture; assigning all missing primary outcomes nonabstinent is a deterministic classification. No supplied passage maps them to a combined or separately identified primary analysis. No bias or alternative efficacy result is calculated.

**Affected result or extracted value:** Missing-outcome assumptions attached to ITT 300/720 versus 55/360 and RR 3.0 [2.0,4.9].

**Why context does not resolve it:** The MAR paragraph has its own Statistical analysis heading; adjacency to economic imputation does not restrict it explicitly to costs/QALYs/covariates. Complete-case sensitivity is separately stated.

**Alternative source-grounded interpretations:** MAR may concern another imputation/covariate/economic model, or SAP may supersede the protocol. Neither restriction nor replacement mapping is supplied.

Missing definition to resolve: Which primary missing-data architecture applied, and how do MAR and missing-as-smoking map to identified analyses or amendments?

**Classification rationale:** Prospective protocol and SAP passages are PLAN; article methods/flow are REPORT. Protocol versus report yields P_R; protocol versus SAP yields P_P. P_R precedes P_P and fixes protocol_report. The flow only corroborates retained denominators; it creates no additional relationship. Evidence state reproduced is supported by the direct-source recheck.

**Classification ambiguity:** MAR and deterministic smoking status can apply to distinct analyses; the source does not map their scope. Economic adjacency and possible SAP supersession are retained alternatives, rather than inferred chronology.



**Mechanical evidence recheck:** Location found; source and comparator matched: [DOC-002 p.28](<../joi250093supp1_prod_1768590553.08963.pdf#page=28>), lines759–764, and [p.66](<../joi250093supp1_prod_1768590553.08963.pdf#page=66>), lines2011–2016, separately headed Statistical analysis, both state that outcomes will primarily be analyzed in a missing-at-random architecture. Both follow economic complete-case/imputation paragraphs but say Outcomes without an economic restriction. [SAP p.91](<../joi250093supp1_prod_1768590553.08963.pdf#page=91>), lines2890–2892, explicitly identifies primary ITT and regards dropout/incomplete data as continuing smokers. [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) treats missing primary outcomes as negative/not abstinent and separately discards missing outcomes for complete-case analysis. [DOC-001 p.4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1, confirms missing53 and42, including deaths25 and27, and primary analysis totals720 and360.

Necessary inputs available; missing definitions: Printed handling statements and retained denominators are available; outcome-specific MAR applicability, the imputation model/variables, and an explicit replacement/amendment hierarchy are absent.

**Potential downstream evidence impact:** If confirmed, missing-data assumptions recorded for the primary ITT effect could differ; the effect of another missing-data analysis is unestablished.

## C010 — Prespecified gender-specific primary analyses are not reported

Pending Human Adjudication.

**Candidate statement:** Prespecified gender-specific primary analyses are not reported.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 SAP pp.92,93,99 vs REPORT DOC-001 pp.3,5 and DOC-003 p.12

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category 5: an explicitly planned subgroup analysis of the primary treatment effect is not reported in the complete supplied subgroup results or matched main narrative. This is distinct from omission of ancillary non-key secondary outcomes. The SAP anticipates disclosure of unavailable confidence intervals, so sparse enrollment does not supply an observed removal or nonestimation explanation.

**Finding IDs:** F-XS-004, F-ST1-006

**Qualifying route:** Route A, category 5

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), prespecified subgroup list; REPORT.
- [DOC-001 — PDF p. 5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), subgroup consistency narrative; REPORT.
- [DOC-002 — PDF p. 92](<../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2936–2939 subgroup analysis introduction; PLAN.
- [DOC-002 — PDF p. 93](<../joi250093supp1_prod_1768590553.08963.pdf#page=93>), lines2940–2952, gender and interval disclosure; PLAN.
- [DOC-002 — PDF p. 99](<../joi250093supp1_prod_1768590553.08963.pdf#page=99>), Gender Male/Female table shell; PLAN.
- [DOC-003 — PDF p. 12](<../joi250093supp2_prod_1768590553.09463.pdf#page=12>), complete eTable8; REPORT.

**Source evidence:** SAP specifies primary treatment-effect sensitivity models by age, education, occupation, gender male/female, and smoking duration, each with RR and 95% CI and disclosure of missing CIs. eTable 8 and main subgroup narrative contain age, education, occupation, smoking duration, reading SMS, without gender rows/results or nonestimability explanation. Male baseline counts are 698/720 and 345/360.

**Reported-versus-comparator:** Planned male/female primary subgroup RR/CI analyses versus their absence from the complete supplied subgroup results.

**Reasoning procedure:** Match planned subgroup prose and table shells to the complete main narrative and eTable 8; distinguish unreported results from evidence that no analysis was performed.

**Calculation:** Match each planned subgroup to the complete supplied subgroup display and narrative. Gender has no reported counterpart; the blank Male/Female SAP shell corroborates the planned prose and is not a result.

**Affected result or extracted value:** Planned male/female primary RRs/CIs and the robustness scope of the primary abstinence analysis.

**Why context does not resolve it:** Route A category 5 applies to an unreported planned primary analysis. Sparse female observations may explain nonestimation, but the SAP expressly anticipates unavailable-interval disclosure.

**Alternative source-grounded interpretations:** The analysis may have been infeasible, performed but omitted, or removed by amendment. No explanation or result is supplied.

Missing definition to resolve: Where are the planned male/female primary results or the disclosed reason estimates/CIs were unavailable or removed?

**Classification rationale:** PLAN SAP versus REPORT methods/results gives P_R and protocol_report. Main/supplement omissions agree; there is no S_C discrepancy. The recheck establishes cited plan wording and absence at complete report displays, supporting reproduced. One issue contains both male/female planned rows and both checker findings.

**Classification ambiguity:** Absence is bounded to the complete supplied report package; it does not establish that an analysis was never performed.



**Mechanical evidence recheck:** Location found; source and comparator matched: [SAP p.92](<../joi250093supp1_prod_1768590553.08963.pdf#page=92>), lines2936–2939, specifies subgroup sensitivity analyses of primary treatment-effect stability. [p.93](<../joi250093supp1_prod_1768590553.08963.pdf#page=93>), lines2940–2952, includes gender male/female, separate mixed-effects subgroup models, RR/95%CI, and disclosure of missing CIs. [p.99](<../joi250093supp1_prod_1768590553.08963.pdf#page=99>) contains blank Gender Male/Female table-shell rows. [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) lists prespecified age, education, employment, and smoking-duration subgroups; [p.5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) narrative adds reading SMS but reports no gender effect; its baseline table shows male698/720 and345/360, female22 and15. The complete [DOC-003 p.12](<../joi250093supp2_prod_1768590553.09463.pdf#page=12>), eTable8, contains All, Age, Education, Occupation, Smoking Duration, Reading SMS, and no gender rows.

Necessary inputs available; missing definitions: Plan models and complete reported subgroup categories are available. Male/female RR/CI outputs, sex-specific abstinence counts/model estimability, and a reason for omission/removal are absent.

**Potential downstream evidence impact:** If confirmed, an evidence summary could overstate the reported coverage of prespecified primary subgroup analyses or omit the absence of sex-specific estimates.

## C011 — Current primary-data attrition assumptions differ

Pending Human Adjudication.

**Candidate statement:** Current primary-data attrition assumptions differ.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN DOC-002 protocol pp.48,62 vs PLAN DOC-002 pp.63,64,83 and REPORT DOC-001 p.3; PLAN DOC-002 p.77 amendment context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: attrition allowance is focus D and is attached to the reported primary sample-size/power rationale. B2: 10% appears in combined-plan overview and statistics introduction, while both phase-specific calculations and the SAP combined overview use 20%; no explicit differing definition or surviving-input hierarchy reconciles them. B3: a reader could extract 10% or 20% as the attrition assumption supporting the 1080-participant, 90%-power primary design. Amendment context changes sample sizes but does not expressly reconcile these percentages.

**Finding IDs:** F-XS-010, F-ST1-010

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), sample-size20%attrition; REPORT.
- [DOC-002 — PDF p. 48](<../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1344–1347 primary-data10%; PLAN.
- [DOC-002 — PDF p. 62](<../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines1861–1863 primary-data10%; PLAN.
- [DOC-002 — PDF p. 63](<../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1894–1898 Phase3 20%calculation; PLAN.
- [DOC-002 — PDF p. 64](<../joi250093supp1_prod_1768590553.08963.pdf#page=64>), lines1936–1938 Phase4 contextual20%calculation; PLAN.
- [DOC-002 — PDF p. 77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>), sample-sizeamendment; PLAN.
- [DOC-002 — PDF p. 83](<../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2624–2638 SAP20%; PLAN.

**Source evidence:** Current protocol overview/statistics introduction uses 10% missing primary outcome data. Detailed Phase 3 calculation uses 20%, 587+(587×.2)=704, then 1080. SAP and report also use 20%; Phase 4 20% is contextual rather than an additional reported result.

**Reported-versus-comparator:** Printed 10% primary-data missingness inputs versus detailed PLAN/SAP/report 20% attrition inputs.

**Reasoning procedure:** Match combined-study and phase-specific inputs, SAP and report power rationale, and the explicit amendment; compare printed percentage intervals.

**Calculation:** Printed input copies 10±0.5% and 20±0.5% give gap 9 percentage points and relative gap 9/10=0.90. The expressly stated additive inflation formula is not challenged; no alternative power result is asserted.

**Affected result or extracted value:** Attrition assumption attached to reported 90% power and 1080-participant primary design.

**Why context does not resolve it:** Current passages refer to the same primary-data assumption without distinguishing phase or missingness type; the amendment does not map surviving 10% statements to a superseded input.

**Alternative source-grounded interpretations:** Overview/introduction may retain a previous assumption while detail/SAP/report use 20%. A final hierarchy or dated calculation is absent.

Missing definition to resolve: Which primary-data attrition assumption governed Phase 3, and how do the surviving 10% and 20% specifications relate?

**Classification rationale:** Protocol versus SAP/detail inputs yields P_P; 10% protocol versus 20% report yields P_R. P_R takes precedence and fixes protocol_report. The amendment is PLAN context; it is not a separate conflicting relationship. The exact-source recheck supports reproduced.

**Classification ambiguity:** Combined-study missingness could have a separate definition, or 10% could be a retained overview input. No final hierarchy is inferred solely from bundle order, labels, or surviving prose. Describe these as supplied-plan passages rather than claim an undisclosed chronological precedence.



**Mechanical evidence recheck:** Location found; source and comparator matched: [DOC-002 p.48](<../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1344–1347, combined study total2716 assumes10% do not provide primary data. [p.62](<../joi250093supp1_prod_1768590553.08963.pdf#page=62>), lines1861–1863, repeats2716 and10%. [p.63](<../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1894–1898, Phase3 assumes20% and prints587+(587×0.2)=704. [p.64](<../joi250093supp1_prod_1768590553.08963.pdf#page=64>), lines1936–1938, Phase4 likewise uses20%,864+(864×0.2)=1036. [SAP p.83](<../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2624–2638, combined overview and Phase3 both use20%; Phase3 proceeds to1080. [DOC-001 p.3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) also says anticipated20% attrition in the1080-participant calculation. [DOC-002 p.77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2416–2424, discloses sample-size revisions from888 to1080 for Phase3 and1480 to1620 for Phase4, without explicitly reconciling attrition percentages.

Necessary inputs available; missing definitions: Percentages, phase labels, additive formula and amendment summary are available. A dated applicable-input hierarchy or explanation distinguishing combined-study missingness from phase-specific attrition is absent.

**Potential downstream evidence impact:** If confirmed, sample-size/power metadata could carry 10% or 20% as the governing attrition assumption; achieved power is not recalculated.

## C012 — All-cause mortality percentage is attributed to TB-specific mortality

Pending Human Adjudication.

**Candidate statement:** All-cause mortality percentage is attributed to TB-specific mortality.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 p.8 discussion vs REPORT DOC-001 pp.1,4,5,6 and DOC-003 p.6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route B. B1: this is an explicitly in-scope misattributed result; cause-specific versus all-cause mortality changes which outcome receives a printed risk. B2: the report distinguishes 32 TB deaths and 52 total deaths but describes 4.8% of participants as dying of TB; the immediate discussion supplies no alternate numerator or cause definition. B3: six-month TB-specific mortality could be extracted as 4.8% or 32/1080≈3.0%. The outcome-attribution domain is appropriate, rather than a separate claim that the death totals fail.

**Finding IDs:** F-NUM-001, F-XS-012

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-001 — PDF p. 1](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), 1080randomized,corroboratingdenominator; REPORT.
- [DOC-001 — PDF p. 4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>), Figure1 death25/27 and1080enrolled; REPORT.
- [DOC-001 — PDF p. 5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), TBcause32/52; REPORT.
- [DOC-001 — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2 deaths25/720and27/360; REPORT.
- [DOC-001 — PDF p. 8](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>), discussion4.8%diedofTB; REPORT.
- [DOC-003 — PDF p. 6](<../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4 total52 andTB32; REPORT.

**Source evidence:** Discussion says 4.8% of trial participants died of TB within six months. Main results say TB caused 61.5% [32/52] of deaths. Figure 1/Table 2 show 25+27=52 deaths among 1080 participants. eTable 4 separately identifies 32 TB and 20 other-cause deaths.

**Reported-versus-comparator:** Discussion TB-specific mortality 4.8% versus 32 TB-attributed deaths/1080; 52 all-cause deaths/1080 instead reproduces 4.8%.

**Reasoning procedure:** Match cause labels, total/cause counts and enrolled denominator across narrative, flow and tables; reconstruct both cause-specific and all-cause risks.

**Calculation:** 32/1080×100=2.962963% versus 52/1080×100=4.814815%. TB rounded-input range is 100×[31.5/1080.5,32.5/1079.5]=[2.915317,3.010653]%, disjoint from printed 4.8±.05=[4.75,4.85]%; gap 1.739347/4.8=.362364. The all-cause ratio overlaps 4.8%.

**Affected result or extracted value:** Six-month TB-specific mortality risk, extractable as 4.8% or 32/1080≈3.0%.

**Why context does not resolve it:** The cause label changes which outcome receives the number; the report explicitly distinguishes TB from other causes and supplies no alternate cause population.

**Alternative source-grounded interpretations:** The discussion may intend all-cause mortality among participants with TB; another cause classification or denominator might underlie 4.8%, but none is stated.

Missing definition to resolve: Does 4.8% mean all-cause mortality among participants with TB or TB-attributed deaths, and which numerator/denominator defines the latter?

**Classification rationale:** Main discussion versus main cause report yields S_W; discussion versus supplementary cause report yields S_C. S_C takes precedence; both sources are REPORT by result content. The inconsistency concerns outcome attribution and fixes report_internal_inconsistency. Denominator/death summaries corroborate the arithmetic. No prospective plan relationship is added. Recheck supports reproduced.

**Classification ambiguity:** The discussion may mean all-cause mortality among trial participants with TB rather than TB-attributed deaths; that interpretation explains 52/1080 but is not its literal cause label.



**Mechanical evidence recheck:** Location found; source and comparator matched: [DOC-001 p.8](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=8>) explicitly attributes4.8% within six months to deaths of TB. [p.5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>) specifies TB as61.5% [32/52] of deaths. [DOC-003 p.6](<../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4, confirms52 total,25/27 by arm,32 TB deaths,16/16 by arm, and20 deaths across other causes. [DOC-001 p.1](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>) confirms1080 randomized; [p.4](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4>) Figure1 confirms720/360, deaths25/27; [p.6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) Table2 Death confirms25/720 and27/360. Every cited supporting location was visually matched.

Necessary inputs available; missing definitions: Counts, enrollment, time horizon and cause table are available. No alternate TB-attributable cause definition, denominator, or adjudication mapping yielding4.8% is supplied.

**Potential downstream evidence impact:** If confirmed, an extractor could take 4.8% as TB-specific mortality rather than distinguish it from all-cause mortality and 32/1080.

## C013 — Adverse-event narrative reverses two any-symptom arm directions

Pending Human Adjudication.

**Candidate statement:** Adverse-event narrative reverses two any-symptom arm directions.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.5 prevalence pairs vs same-paragraph direction; REPORT DOC-003 p.15 corroborates and supplies severity alternative

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Reproduced and qualifying by Route A, category 2: the arm-direction statement reverses the adjacent any-symptom percentages for two symptoms, with relative precision gaps above 0.05. Immediate recoverability of the numeric direction does not remove an always-register direction conflict. Preserve the distinct moderate/severe interpretation as a source-grounded alternative.

**Finding IDs:** F-NUM-002, F-XS-013

**Qualifying route:** Route A, category 2

**Exact source locations:**

- [DOC-001 — PDF p. 5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), Adverse Events ordered percentages and summarysentence; REPORT.
- [DOC-003 — PDF p. 15](<../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable10 irritability/anxiety severity rows; REPORT.

**Source evidence:** Main Adverse Events fixes arm order mHealth versus usual care, prints irritability 40.5% versus 43.4% and anxiety 33.3% versus 36.8%, then says both were more common in mHealth. eTable 10 None percentages 59.5/56.6 and 66.7/63.2 corroborate those prevalences; moderate/severe frequencies are higher in mHealth.

**Reported-versus-comparator:** Any-irritability 40.5% versus 43.4% and any-anxiety 33.3% versus 36.8%, in mHealth/usual-care order, versus a sentence stating greater frequency in mHealth.

**Reasoning procedure:** Fix the printed arm order, compare any-symptom direction to the adjacent sentence, then examine the separate moderate/severe quantities as an alternative.

**Calculation:** mHealth-minus-usual-care rounded prevalence differences are [−3.00,−2.80] and [−3.60,−3.40] percentage points. Gap/control-reference ratios are 2.80/43.4=.064516 and 3.40/36.8=.092391. Both directions remain lower mHealth. Dry mouth 62.7 versus 55.7 agrees and is contextual.

**Affected result or extracted value:** Any-irritability and any-anxiety frequency directions by randomized arm.

**Why context does not resolve it:** Route A category 2 applies to a printed direction reversing the values, even when the intended direction may be reconstructed immediately.

**Alternative source-grounded interpretations:** The sentence may refer instead to moderate/severe symptoms; eTable 10 supports that distinct quantity, but the sentence names no switch.

Missing definition to resolve: Does more common refer to any irritability/anxiety or moderate/severe burden, and which quantity and arm direction should be extracted?

**Classification rationale:** Competing percentages and direction are within a single REPORT paragraph, giving S_W/statistical_results. Supplementary severity/prevalence rows corroborate the printed percentages and supply an alternative quantity; they are not a conflicting report and add no S_C. Recheck supports reproduced. No plan is a comparator.

**Classification ambiguity:** The paragraph might switch from any symptom to moderate/severe burden without stating that switch; severity and prevalence are separate quantities.



**Mechanical evidence recheck:** Location found; source and comparator matched: [DOC-001 p.5](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5>), Adverse Events, fixes mHealth/usual-care order, prints irritability40.5%/43.4% and anxiety33.3%/36.8%, then says dry mouth, irritability and anxiety were more common in mHealth. [DOC-003 p.15](<../joi250093supp2_prod_1768590553.09463.pdf#page=15>), eTable10, confirms irritability None59.5%/56.6% and anxiety None66.7%/63.2%, whose complements match those any-symptom frequencies. Moderate/severe percentages are irritability11.2+4.3=15.5% versus7.2+1.2=8.4%; anxiety6.9+2.4=9.3% versus3.6+0.3=3.9%. Both repeated affected symptoms were confirmed.

Necessary inputs available; missing definitions: Arm order, any-symptom percentages, and severity rows are available. The missing definition is whether more common switches from any symptom to moderate/severe burden.

**Potential downstream evidence impact:** If confirmed, an evidence summary could copy the sentence’s symptom-frequency direction or the opposite direction from the any-symptom percentages.

## C014 — Fourteen interval rows do not reproduce a rule fitting other display rows

Pending Human Adjudication.

**Candidate statement:** Fourteen interval rows do not reproduce a rule fitting other display rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** The exact recheck confirms all fourteen triples and the independent calculation reproduces all fourteen relative gaps above .05. Route A category 4 applies because the same diagnostic reproduces other rows of each display within the workflow tolerance. Unreported row-specific construction remains a human question, not a reason to suppress the observed pattern.

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 4

**Exact source locations:**

- [DOC-001 — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2CO10PPadjusted,CO6PPcrude/adjusted,self-reportadjusted; REPORT.
- [DOC-003 — PDF p. 12](<../joi250093supp2_prod_1768590553.09463.pdf#page=12>), eTable8All,age≥40,primary,secondary,active,dependent,smoking<24,readingNo; REPORT.
- [DOC-003 — PDF p. 13](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9CO10crude/adjusted; REPORT.
- [DOC-003 — PDF p. 14](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>), population/adjustmentnotes; REPORT.

**Source evidence:** All 14 affected RR/lower/upper triples and their rounded-input reconstruction ranges are preserved in the detailed numeric list below. The Table 2 adjusted self-report upper endpoint is literally 42 in the supplied source, without a decimal point. Each source row was visually confirmed.

**Reported-versus-comparator:** Fourteen printed RR interval triples versus the rounded-input U*=E²/L reconstruction that reproduces other rows of each display.

**Reasoning procedure:** Read every affected triple at the exact display, preserve its literal precision, construct half-unit enclosures, and apply the same diagnostic to comparator rows in that display.

**Calculation:** Apply U*=E²/L, with range [(E−hE)²/(L+hL),(E+hE)²/(L−hL)] versus [U−hU, U+hU], using exact displayed half-units. Every listed gap/U exceeds .05. The rule reproduces other rows of each display; it is a reconstruction diagnostic rather than a claim about an unstated Wald method. No point is outside its printed CI and no CI/P conflict is inferred.

**Affected result or extracted value:** The 14 upper CI endpoints and corresponding primary/sensitivity/subgroup uncertainty.

**Why context does not resolve it:** Route A category 4 requires inclusion when a rule reproduces other display rows but fails these rows beyond precision; unknown row-specific construction is the human question.

**Alternative source-grounded interpretations:** Profile likelihood, bootstrap, marginal-risk or other nonsymmetric intervals may explain rows; procedures may differ by row. Fitted covariance/SE and construction definitions are absent.

Missing definition to resolve: Which estimate/interval construction produced every listed row, and are the printed limits, including 42, intended for that construction?

**Classification rationale:** Every comparison is within its own REPORT display. Combining occurrences of one rule does not create S_C. No PLAN location is a conflicting comparator; S_W/statistical_results is retained.

**Classification ambiguity:** Row-specific interval procedures are unavailable. No universal Wald or log-symmetric interval requirement is asserted.

### Detailed interval reconstruction for C014

Each line gives display/row, printed E; L; U, independently recomputed U* interval, gap, and gap/|U|. Every displayed input/output receives its own half-unit; a literal42 receives±0.5, not±0.05.

- Table 2 CO10 PP adjusted: 3.1; 2.1; 5.2; reconstructed [4.326744,4.840244]; gap 0.309756; relative 0.059568.
- Table 2 CO6 PP crude: 3.6; 2.14; 6.87; reconstructed [5.875291,6.240047]; gap 0.624953; relative 0.090968.
- Table 2 CO6 PP adjusted: 3.8; 2.3; 7.7; reconstructed [5.984043,6.587778]; gap 1.062222; relative 0.137951.
- Table 2 self-report adjusted: 2.8; 1.9; 42; reconstructed [3.878205,4.390541]; gap 37.109459; relative 0.883559.
- eTable 8 All: 2.890; 1.983; 4.709; reconstructed [4.209332,4.214371]; gap 0.494129; relative 0.104933.
- eTable 8 Age≥40: 2.953; 2.048; 5.092; reconstructed [4.255434,4.260397]; gap 0.831103; relative 0.163217.
- eTable 8 Primary: 2.638; 1.849; 4.07; reconstructed [3.761236,3.766125]; gap 0.298875; relative 0.073434.
- eTable 8 Secondary: 2.719; 1.348; 4.83; reconstructed [5.480343,5.488445]; gap 0.645343; relative 0.133611.
- eTable 8 Active: 2.989; 1.933; 4.885; reconstructed [4.619153,4.624637]; gap 0.259863; relative 0.053196.
- eTable 8 Dependent: 2.587; 1.329; 3.986; reconstructed [5.031954,5.039636]; gap 1.045454; relative 0.262281.
- eTable 8 Smoke<24: 3.511; 1.884; 7.127; reconstructed [6.539459,6.546659]; gap 0.579841; relative 0.081358.
- eTable 8 Reading No: 2.198; 1.288; 3.299; reconstructed [3.747774,3.754099]; gap 0.448274; relative 0.135882.
- eTable 9 CO10 crude: 2.9; 1.8; 6.4; reconstructed [4.390541,4.972857]; gap 1.377143; relative 0.215179.
- eTable 9 CO10 adjusted: 3.1; 1.9; 6.5; reconstructed [4.770513,5.363514]; gap 1.086486; relative 0.167152.

Reproducing comparators: Table 2 self-report crude 2.7 [1.8,4.1], week 9 crude 2.6 [1.8,3.9]/adjusted 2.7 [1.8,4.3], month 6 crude 2.7 [2.0,3.8]/adjusted 2.7 [1.9,4.0], and success 1.2 [.9,1.6]/1.2 [.9,1.5] have overlapping reconstruction/printed intervals. In eTable 8, age <40 gives [4.846799,4.853725] versus [4.8565,4.8575], relative gap .000571; smoking ≥24 gives [3.857124,3.862770] versus [3.9105,3.9115], relative gap .012204; no formal education and reading Yes also pass the .05 rule. In eTable 9, CO<6 3.6 [2.4,5.4]/3.8 [2.4,6.2], week 9 2.5 [1.7,3.6]/2.6 [1.7,3.8], month 6 2.58 [1.8,3.6]/2.7 [1.8,4.0], and success 1.1 [.7,1.6]/1.1 [.7,1.5] have overlapping intervals. These source-confirmed comparators establish the observed reproducing rule without asserting a universal inferential construction.



**Mechanical evidence recheck:** Location found; source and comparator matched: Yes for every affected row in [DOC-001 p.6, Table 2](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), [DOC-003 p.12, eTable 8](<../joi250093supp2_prod_1768590553.09463.pdf#page=12>) and [DOC-003 p.13, eTable 9](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>). [DOC-003 p.14 notes](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>) identify RR, covariate adjustment and mixed-effects clustering, but no row-specific interval construction. All are REPORT by displayed trial-results content. Table 2 self-report adjusted upper endpoint is literally `42`, and its lower endpoint is `1.9`; no decimal was silently inserted.

Necessary inputs available: Every printed triple and display precision needed for this diagnostic is available. Exact missing inputs/definitions: Fitted coefficients/covariance, transformation from model to RR, interval-construction algorithm and any row-specific method switches are absent. No universal Wald construction, confidence-interval/P-value conflict or point-outside-interval issue is inferred.

Determining fact: all 14 printed triples match and all 14 diagnostic interval gaps remain >.05 relatively.

**Potential downstream evidence impact:** If confirmed, one or more of the 14 printed upper limits could be copied with an uncertainty construction that differs from the intended row-specific procedure. No pooled-effect or conclusion change is established.

## C015 — Latest protocol and SAP prescribe different failure windows

Pending Human Adjudication.

**Candidate statement:** Latest protocol and SAP prescribe different failure windows.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route B is reproduced and meets B1 through a planned key-secondary endpoint definition, B2 because retained protocol/SAP definitions and the report do not specify their governing hierarchy, and B3 because the definition attached to the reported failure result remains unresolved.

**Finding IDs:** F-XS-009, F-ST1-011

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-002 — PDF p. 9](<../joi250093supp1_prod_1768590553.08963.pdf#page=9>), lines179–180 month-5 definition, explicitly headed V6.0; PLAN.
- [DOC-002 — PDF p. 47](<../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1319–1320month6definition; PLAN.
- [DOC-002 — PDF p. 77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2413–2415 explicit5→6amendment; PLAN.
- [DOC-002 — PDF p. 85](<../joi250093supp1_prod_1768590553.08963.pdf#page=85>), lines2685–2686SAPmonth5; PLAN.
- [DOC-001 — PDF p. 1](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), key-secondaryfailureproportions; REPORT.
- [DOC-001 — PDF p. 3](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), outcomedetailpointer; REPORT.
- [DOC-001 — PDF p. 6](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2failure1/720versus2/360; REPORT.

**Source evidence:** Protocol p.9, explicitly headed V6.0, and SAP p.85 define failure as remaining smear-positive at month 5 or later; protocol p.47 uses month 6 or later. The amendment explicitly replaces month 5 with month 6 in v6. Report prints failure 1/720 versus 2/360 without an explicit competing window.

**Reported-versus-comparator:** Current supplied protocol/SAP failure definitions of month 5 or later versus month 6 or later and an explicit 5→6 amendment.

**Reasoning procedure:** Read current version headers, both categorical failure windows and the explicit amendment, then locate the abstract proportions and Table 2 counts without adding an unstated report window.

**Calculation:** These are exact categorical endpoint windows, not rounded month measurements. The amendment reconciles historical protocol changes but not the SAP's retained month-5 rule. No patient reclassification or event-count discrepancy is inferred.

**Affected result or extracted value:** Definition attached to abstract key-secondary failure proportions0.1% and 0.5%, Table 2 counts 1/720 and 2/360, and TB programme outcome classification.

**Why context does not resolve it:** SAP and amended protocol prescribe different windows for a reported key-secondary endpoint; the report does not identify which classified its three events.

**Alternative source-grounded interpretations:** The amended month-6 rule, SAP month-5 rule or programme-register rule may govern. A finalized endpoint dictionary is absent.

Missing definition to resolve: Were failures classified using month 5 or later or month 6 or later, and which supplied plan rule governed the three reported events?

**Classification rationale:** All conflicting thresholds are prospective PLAN content in one bundle. The report supplies no competing month threshold and therefore adds no P_R. P_P/plan_material is retained.

**Classification ambiguity:** Final endpoint dictionary and governing amendment/SAP hierarchy are absent. PDF p.9 is explicitly headed V6.0; its earlier position does not establish an earlier version.



**Mechanical evidence recheck:** Location found; source value/text matched; comparator matched: Yes. [DOC-002 p.9 lines179–180](<../joi250093supp1_prod_1768590553.08963.pdf#page=9>) says month 5 or later and is headed V6.0 07.03.25; [p.47 lines1319–1320](<../joi250093supp1_prod_1768590553.08963.pdf#page=47>) says month 6 or later; [p.77 lines2413–2415](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>) explicitly describes replacing month 5 with month 6 in v6; [SAP p.85 lines2685–2686](<../joi250093supp1_prod_1768590553.08963.pdf#page=85>) retains month 5 or later. All four are PLAN by prospective endpoint/amendment content. REPORT impact locations [DOC-001 p.1 abstract](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), [p.3 Trial Outcomes](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>) and [p.6 Table 2](<../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>) contain the secondary failure result/pointer; Table 2 prints 1/720 versus 2/360. Abstract prints failure 0.1% versus0.5%; it does not itself print the event counts or define a smear window.

Inputs available/missing: Competing definitions, explicit amendment and three reported events are available. Final endpoint dictionary, amendment/SAP hierarchy, event smear dates and programme-register classification rules actually used are absent. Alternative interpretation: Amended protocol could govern, SAP could govern, or programme records could apply a separately defined rule. Direct versus inferred: Contradictory printed windows are direct; participant reclassification or numerical outcome effects are unestablished.

Determining fact: exact plan month-5 and month-6 windows remain different after reading the amendment.

**Potential downstream evidence impact:** If confirmed, endpoint-definition metadata for the three reported treatment failures could specify month 5 or month 6; patient reclassification is unestablished.

## C016 — Current Phase 3 power statements retain different cluster allocations

Pending Human Adjudication.

**Candidate statement:** Current Phase 3 power statements retain different cluster allocations.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route B is reproduced and satisfies B1 for primary trial power/allocation inputs, B2 because the current repeated paragraph is not explicitly historical or a distinct calculation, and B3 for allocation assumptions attached to the 1080-participant/27-cluster primary design. The qualifying relative gap is .0625 for the intervention-arm input.

**Finding IDs:** F-XS-011, F-ST1-009

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-002 — PDF p. 48](<../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1348–1353poweroverview; PLAN.
- [DOC-002 — PDF p. 63](<../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1886–1907Phase3power/allocation; PLAN.
- [DOC-002 — PDF p. 64](<../joi250093supp1_prod_1768590553.08963.pdf#page=64>), Phase4allocationcontext; PLAN.
- [DOC-002 — PDF p. 65](<../joi250093supp1_prod_1768590553.08963.pdf#page=65>), lines1958–1963repeatedpowerparagraph; PLAN.
- [DOC-002 — PDF p. 77](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2416–2424allocationamendment; PLAN.
- [DOC-002 — PDF p. 83](<../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2629–2642SAPallocation; PLAN.

**Source evidence:** Current overview/detail/SAP give Phase 3 18 intervention and 9 control clusters, total 27, 90% power at 5%, 18%/8% abstinence. The repeated current protocol paragraph gives 16 and 8 with the same power/rates. The amendment changes 16/8 to 18/9. Its Phase 4 20/20 versus other 18/18 is unreported-phase peripheral context.

**Reported-versus-comparator:** Current Phase 3 power inputs 18/9 versus 16/8 intervention/control clusters with the same rates and power.

**Reasoning procedure:** Match Phase 3 rates, power and allocation in each current PLAN paragraph and amendment; calculate arm-input precision gaps and retain Phase 4 only as context.

**Calculation:** 18±.5 versus 16±.5 yields gap 1/16=.0625. Independently rounded arm sums give [26,28] versus [23,25], gap 1/24=.041667, which does not independently qualify; 9-versus-8 intervals touch. The intervention-arm power input supplies the reproduced basis.

**Affected result or extracted value:** Phase 3 allocation and power inputs underlying the 1080-participant,27-cluster primary trial.

**Why context does not resolve it:** The repeated current paragraph attaches the same power/rates to 16/8 without labeling it historical; this changes a primary analysis-population/power input rather than an administrative site copy.

**Alternative source-grounded interpretations:** The repeated paragraph may carry forward earlier text, or both allocations may have been evaluated without being distinguished. The governing final power calculation is absent.

Missing definition to resolve: Which Phase 3 allocation and power calculation governs, and should the current 16/8 paragraph be read as historical?

**Classification rationale:** Conflicting power inputs are solely PLAN content. The observed27-cluster trial corroborates one specification without adding P_R. P_P/plan_material is retained.

**Classification ambiguity:** The amendment discloses the change; p.65 may retain historical text without naming it. Separate unreported Phase4 inputs remain peripheral context.



**Mechanical evidence recheck:** Location found; source and comparator matched: Yes. PLAN [DOC-002 p.48 lines1348–1350](<../joi250093supp1_prod_1768590553.08963.pdf#page=48>) gives 18 intervention and 9 control clusters, 90% power, 5% level, 18%/8% abstinence; [p.63 lines1886–1907](<../joi250093supp1_prod_1768590553.08963.pdf#page=63>) gives these rates/power and 27 clusters, 18/9 allocation, and1080 participants; [p.65 lines1958–1961](<../joi250093supp1_prod_1768590553.08963.pdf#page=65>) retains 16 intervention and8 control with the same rates/power; [p.77 lines2416–2424](<../joi250093supp1_prod_1768590553.08963.pdf#page=77>) explicitly describes increasing Phase3 v4 16/8,888 participants to v6 18/9,1080; [SAP p.83 lines2629–2638](<../joi250093supp1_prod_1768590553.08963.pdf#page=83>) gives27 clusters,2:1,90%/5%,18%/8%,1080. All are PLAN by prospective design/power content. Peripheral PLAN [p.64 Phase4](<../joi250093supp1_prod_1768590553.08963.pdf#page=64>) uses18/18, while the repeated p.65 Phase4 paragraph uses20/20; p.77 amendment describes40→36 Phase4 clusters. This context does not expand the included Phase3 issue.

Inputs available/missing: Allocations, rates, significance/power and disclosed amendment are available. A final governing power calculation and an explicit statement that p.65 is historical or a distinct scenario are absent. Alternative interpretation: p.65 may retain earlier-version text; both allocations might have been evaluated without being differentiated. The source itself discloses the change, so no undisclosed amendment is asserted. Direct versus inferred: Direct is the incompatible repeated current-plan power-input paragraph; its production mechanism is inferred and unestablished.

Determining fact: current supplied plan power paragraphs retain18 versus 16 intervention clusters beyond the workflow precision threshold.

**Potential downstream evidence impact:** If confirmed, primary trial power/allocation metadata could carry 16 or 18 intervention clusters as the governing design input.

## C017 — Two cause-of-death percentages do not reconcile within eTable 4

Pending Human Adjudication.

**Candidate statement:** Two cause-of-death percentages do not reconcile within eTable 4.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.6 affected cells vs same-table death total

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route A category3 applies to each source-confirmed count/denominator/percentage cell. Both half-unit reconstructions leave relative gap .228327>.05. Recovering a likely percentage does not remove the printed reading; both occurrences belong to one pattern.

**Finding IDs:** F-NUM-101

**Qualifying route:** Route A, category 3

**Exact source locations:**

- [DOC-003 — PDF p. 6](<../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4usual-careDruguser,Severepneumonia,Totaldeaths; REPORT.

**Source evidence:** eTable 4 usual-care Drug user and Severe pneumonia each print 1(7.4%), with Total deaths 27. Overall affected counts are 1 and mHealth 0. Stroke 2(7.4%) and fall 1(3.7%) support the common denominator; all cause counts sum 27.

**Reported-versus-comparator:** Usual-care Drug user and Severe pneumonia each 1 (7.4%) versus the same-table total of 27 deaths.

**Reasoning procedure:** Match each affected count/percentage cell to the co-located death total and corroborating percentage pattern; apply numerator/denominator/output half-unit intervals.

**Calculation:** 100×1/27=3.703704%. Required rounded range 100×[.5/27.5,1.5/26.5]=[1.818182,5.660377]% versus [7.35,7.45]% gives gap 1.689623/7.4=.228327. Both cells fail the same within-display rule and form one issue.

**Affected result or extracted value:** Usual-care death-cause percentages associated with drug use and severe pneumonia.

**Why context does not resolve it:** Route A category 3 applies to co-located count/denominator/percentage inconsistency; recoverable percentage values do not remove the printed 7.4% readings.

**Alternative source-grounded interpretations:** 7.4% could represent two deaths or another denominator; sums corroborate one death but do not assign a correction. No cause-specific denominator is given.

Missing definition to resolve: What counts, denominators and percentages should be used for the two affected usual-care cause rows?

**Classification rationale:** Counts, percentages and death total are REPORT results in one table; S_W/statistical_results is retained.

**Classification ambiguity:** None.



**Mechanical evidence recheck:** Location found; source and comparator matched: Yes: REPORT [DOC-003 p.6 eTable4](<../joi250093supp2_prod_1768590553.09463.pdf#page=6>) prints usual-care Drug user1(7.4%) and Severe pneumonia1(7.4%), usual-care total deaths27, each overall affected count1 and mHealth0. Same-display stroke2(7.4%) and fall1(3.7%) corroborate the27 denominator. All usual-care cause counts sum27.

Inputs available/missing: Printed count, common death total, percentages and sums are available. No separate cause-specific denominator is defined. Alternative interpretation: The7.4% could correspond to two deaths or another denominator, but no such switch is printed; table sums support the displayed one death in each row. Direct versus inferred: Count/percentage/denominator mismatch is observed; copying or other production mechanisms are unestablished.

Determining fact: both 1(7.4%) cells fail the co-located27-death denominator rule beyond precision.

**Potential downstream evidence impact:** If confirmed, an extractor could copy 7.4% for either affected usual-care cause of death despite the count/total reconstruction.

## C018 — Site 2008 death count and percentage do not reproduce the table denominator

Pending Human Adjudication.

**Candidate statement:** Site 2008 death count and percentage do not reproduce the table denominator.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route A category4 independently supports inclusion: the same-display N40 rule reproduces the other death cells and leaves relative gap .474815 for this cell. N40 is supported inference, not an explicit eTable 6 denominator column. Category3 describes the related count/percentage framing, but category4 is the clearest primary qualifying route.

**Finding IDs:** F-NUM-102

**Qualifying route:** Route A, category 4

**Exact source locations:**

- [DOC-003 — PDF p. 9](<../joi250093supp2_prod_1768590553.09463.pdf#page=9>), eTable6Controlsite2008cell5(7.5),otherdeathrows; REPORT.
- [DOC-003 — PDF p. 8](<../joi250093supp2_prod_1768590553.09463.pdf#page=8>), eTable5site2008recruitmentandITT40,observed35; REPORT.

**Source evidence:** eTable 6 Control site 2008 prints 5(7.5). All other death rows use N=40, including 3(7.5),4(10.0), site2012 5(12.5). eTable 5 prints recruitment/ITT population 40 and observed contributors 35 for site 2008.

**Reported-versus-comparator:** Site 2008 death cell 5 (7.5) versus the N=40 percentage rule reproducing every other death cell; N=40 is inferred and corroborated on page 8.

**Reasoning procedure:** Identify the percentage rule from every other death cell and corroborate the site population separately; apply half-unit intervals without presenting the inferred denominator as an explicit column.

**Calculation:** 100×5/40=12.5%. Rounded range 100×[4.5/40.5,5.5/39.5]=[11.111111,13.924051]% versus [7.45,7.55]% gives gap 3.561111/7.5=.474815. N40 rule reproduces other death cells.

**Affected result or extracted value:** Site 2008 cluster mortality count/percentage.

**Why context does not resolve it:** Route A category 4 applies because the same-display denominator rule reproduces the other rows and fails this row beyond0.05. The N40 rule is inferred from the display and corroborated onp8; eTable 6 has no explicit denominator column. Co-located counts also support category3 framing, rather than a peripheral copy comparison.

**Alternative source-grounded interpretations:** 7.5% represents three of 40, while five of 40 is12.5%; another denominator would require definition. Counts sum overall52/usual-care27/mHealth25, corroborating counts without assigning a correction.

Missing definition to resolve: What death count, denominator and percentage governs site 2008 in eTable 6?

**Classification rationale:** The affected cell and reproducing row pattern are in one REPORT table. The site population corroborator is in the same REPORT document; S_W/statistical_results is retained.

**Classification ambiguity:** eTable6 has no separate N column. N40 is inferred from the complete same-display pattern and corroborated by eTable5 recruitment/ITT population; a distinct mortality denominator is undefined.



**Mechanical evidence recheck:** Location found; source and comparator matched: Yes: REPORT [DOC-003 p.9 eTable6](<../joi250093supp2_prod_1768590553.09463.pdf#page=9>) prints Control2008 5(7.5). All other death cells follow an N40 percentage rule, e.g. Control2002 3(7.5), Control2004 4(10.0), mHealth2012 5(12.5). REPORT [p.8 eTable5](<../joi250093supp2_prod_1768590553.09463.pdf#page=8>) prints site2008 recruitment40/484 and ITT12/40, with observed12/35; denominator35 belongs to observed abstinence contributors, not a defined mortality denominator. eTable6 death counts sum52:27 control and25 mHealth.

Inputs available/missing: Death count, percentage, matching other cells and site population are available. A separate mortality denominator or row-specific population definition is absent. Alternative interpretation: Three of 40 would produce7.5%, whereas five of 40 produces12.5%; another denominator requires a definition. Counts/sums corroborate five without assigning a corrected value. Direct versus inferred: Printed5(7.5) and other-cell pattern are direct; N40 is supported inference; production mechanism is unestablished.

Determining fact: the source cell does not reproduce the N40 rule fitting all other death cells, with relative gap>.05.

**Potential downstream evidence impact:** If confirmed, cluster mortality extraction could pair site 2008 count 5 with 7.5% or an alternative defined denominator; no corrected cell is assigned.

## C019 — Treatment-failure absolute difference has the opposite signed contrast

Pending Human Adjudication.

**Candidate statement:** Treatment-failure absolute difference has the opposite signed contrast.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route A category2 applies to the source-confirmed sign comparison under the common display contrast, whose relative gap is1.367585. The unsigned-magnitude or row-specific reference alternative remains explicit; it is not assumed away.

**Finding IDs:** F-NUM-103

**Qualifying route:** Route A, category 2

**Exact source locations:**

- [DOC-003 — PDF p. 13](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9TreatmentFailuresabsolute-difference0.5andarmrisks; REPORT.
- [DOC-003 — PDF p. 14](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>), notebAbsolute difference; REPORT.

**Source evidence:** eTable 9 failure risks are mHealth 1/695,0.1%[0.01,0.8], versus usual-care 2/333,0.6%[0.1,2.2]. Absolute difference prints +0.5[-0.4,1.3]. Other rows use mHealth-minus-usual-care:43.2−16.5=26.7; 38.0−11.4=26.6; 50.8−22.5=28.3; 57.5−24.6=32.9; 3.2−2.1=1.1; success difference0.

**Reported-versus-comparator:** Printed treatment-failure difference +0.5 versus the common mHealth-minus-usual-care signed contrast from 1/695 and 2/333.

**Reasoning procedure:** Match the signed contrast across other rows, reconstruct failure risk difference from printed counts and risks, and retain unsigned or row-specific reference alternatives.

**Calculation:** 100×(1/695−2/333)=−.456716 percentage points. Rounded count/denominator range [−.679989,−.233792] versus [.45,.55] gives gap .683792/.5=1.367585. Printed arm risks independently allow [−.60,−.40], remaining negative.

**Affected result or extracted value:** Signed failure risk difference in the excluding-deaths sensitivity.

**Why context does not resolve it:** Route A category 2 applies to a sign reversing the common displayed contrast; the word Absolute is an alternative interpretation rather than removal of the direction mismatch.

**Alternative source-grounded interpretations:** This row may use unsigned magnitude, reversed reference group or another model-based contrast; no row-specific switch is named. The signed interval and other rows remain printed. No CI construction is inferred.

Missing definition to resolve: Does Treatment Failures use mHealth-minus-usual-care, and what signed difference and matching interval should be extracted?

**Classification rationale:** Arm risks, point difference, comparator rows and note are within one REPORT document; S_W/statistical_results is retained.

**Classification ambiguity:** “Absolute difference” could denote an unsigned magnitude, a row-specific reverse reference or another contrast. No explicit signed reference or row-specific switch is printed.


**Mechanical evidence recheck:** Location found; source and comparator matched: Yes: REPORT [DOC-003 p.13 eTable9](<../joi250093supp2_prod_1768590553.09463.pdf#page=13>) prints mHealth1/695,0.1%[0.01,0.8] versus usual-care2/333,0.6%[0.1,2.2], difference0.5[-0.4,1.3]. REPORT [p.14 note b](<../joi250093supp2_prod_1768590553.09463.pdf#page=14>) identifies “Absolute difference” without a row-specific reversal. Other rows reproduce mHealth-minus-usual-care:43.2−16.5=26.7;38.0−11.4=26.6;50.8−22.5=28.3;57.5−24.6=32.9;3.2−2.1=1.1; success92.5−92.5=0.

Inputs available/missing: Counts, populations, risks, point difference, interval and other-row contrast are available. An explicit signed-reference definition or unsigned/row-specific contrast switch is absent. Alternative interpretation: “Absolute” may mean an unsigned magnitude, or this row could reverse the reference groups; a different model-based contrast could be intended. The common pattern and signed interval are retained rather than assuming a universal meaning of “absolute.” Direct versus inferred: Positive printed point difference versus negative common signed contrast is observed; intended reference or mechanism is inferred and unresolved.

Determining fact: exact printed positive.5 fails the mHealth-minus-usual-care rule fitting the other rows, beyond display precision.

**Potential downstream evidence impact:** If confirmed, extraction of the failure risk difference could carry a positive rather than negative mHealth-minus-usual-care direction.

## Downstream Evidence-Chain Considerations

Evidence extraction can separate endpoint status, time window, analysis population, model, adjustment, missingness assumption, intervention schedule, event risk and uncertainty interval. If a candidate is confirmed, the affected value or metadata may need a different reading before reuse in a systematic review, meta-analysis, guideline or structured evidence table. The cards specify that potential at the result level. The supplied package does not establish that any candidate propagated, changed a synthesis, changed the paper’s conclusions or caused harm.

## Limitations and Missing Definitions

All 134 supplied PDF pages were freshly mapped from source-linked evidence. There is no remaining scientific source-coverage gap. Reusable extraction reduced preprocessing, while source PDFs and exact page confirmations remained authoritative.

The 109-page PLAN bundle has semantically garbled native/layout extraction. Twelve historical OCR files are empty and seven nonempty OCR pages are partial aids. Complete visual mapping and targeted direct-source confirmation closed coverage. Historical extraction/OCR engine versions are not consistently recorded. Source clipping at the bottom of PLAN diagram pages 13 and 51 was confirmed; adjacent allocation prose remained readable and mapped. No workbook, CSV, or Office source was supplied.

No participant-level data, fitted model code, coefficients/covariance matrices, or row-specific interval-construction procedures were supplied. The interval reconstruction in C014 is a diagnostic that fits other rows within each display, rather than an assertion of a universal interval method. Logistic-to-risk-ratio prediction, standardization or conversion details, the averaging population, conditional/marginal estimand and corresponding interval procedure are absent.

Actual per-person SMS transmission logs, unique-template versus transmission definitions, the implemented pilot revision, and enrollment/joining/treatment/quit-date clock crosswalks are absent. Eligibility-rule overlap and implementing amendments are unavailable. The cotinine cassette concentration criterion and its mapping to the planned graded assay are absent; assay equivalence, event reclassification and changes in participant counts are unestablished.

The supplied bound PLAN includes protocol components, an amendment, SAP and prospective SMS materials. Bundle order and component labels do not establish a final governing hierarchy. Outcome-specific applicability of missing-at-random handling, the fitted adjustment list and tobacco-form mapping, planned male/female primary results or nonestimability explanations, the final failure endpoint dictionary and smear dates, and the governing allocation/attrition power calculation are absent. The report is limited to the supplied printed specification comparisons.

For C008, primary-outcome blocks may group sensitivities of the primary construct. The methods and eTable 9 title explicitly describe post hoc sensitivity analyses; formal promotion of CO<6 to a prespecified primary endpoint is not established. The inclusion audit is QUESTIONED, and the stable candidate remains Pending Human Adjudication with its full audit reason. The main per-protocol CO<6 usual-care count is 39/318 with printed 11.9%; that percentage's relative precision gap is 0.011589 and is excluded under the workflow precision rule.

Mortality cause definitions, symptom prevalence versus moderate/severe interpretation, possible cause-specific or site-specific denominators, and the signed versus unsigned failure contrast are bounded alternative interpretations named in the cards. Site-2008 N=40 is inferred from the same-display reproducing rule and corroborated by eTable 5; eTable 6 does not explicitly print an N column. No corrected value or participant reclassification is assigned.

The review uses only supplied package evidence. It does not assess raw data, broad methodology, clinical merit, novelty, misconduct or preferred analyses. Candidate evidence states and inclusion audits are review records, and every candidate remains Pending Human Adjudication. Potential downstream relevance is limited to values or metadata an evidence extractor could copy if a candidate is confirmed; no propagation, paper-level conclusion change or harm is established.

Direct PDF information/extraction/rendering and OCR tools were unavailable. The pinned package-local fallback covered required PDF capabilities after an authorized installation retry. Rendering used the CPU; the user explicitly approved RTX 5070 Laptop GPU OCR with RapidOCR/ONNX Runtime CUDA. Targeted GPU outputs on PLAN pages 10 and 80 are locator aids. An initial page-29 OCR trial ran on the CPU and is preserved as such.

Full limitations are retained in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The [routing preflight](review_1_6_2/routing_preflight.md) records PASS, run model `gpt-6.1-sol`, source `DEFAULT`, provider `CURRENT_SESSION`, execution mode `INTERACTIVE_CLI`, coordinator inference PASS and all ten verified presets. The prescribed launch command is recorded as `codex --approve-for-me`; the original process invocation was not independently observable. Every mandatory specialist stage used a fresh distinct runtime agent at its required model/effort pair. The manifest below lists every actual agent exactly once, including optional evidence shards and this report generator.

Source integrity is traceable through the before/after hash manifests. The coordinator’s preassembly source and reused-asset checks passed. Governing completed cleanup and mechanical check results are recorded in [tooling_record.md](review_1_6_2/tooling_record.md) and [review_validation.json](review_1_6_2/review_validation.json). The report makes no prospective claim about the validator outcome.

Direct `sha256sum` and `file` were available; native PDF info/text/rendering tools and Tesseract/LibreOffice were unavailable. Bundled helpers used the package-local pinned PyMuPDF 1.26.4/pypdf 5.9.0 environment. Rendering was CPU-based. The user explicitly approved GPU OCR on the RTX 5070 Laptop with RapidOCR ONNX Runtime 1.4.4 and ONNX Runtime GPU 1.28.0; targeted page 10/80 outputs are transcription aids. Initial page-29 CPU fallback is preserved separately. No source or reusable artifact was changed.

### Direct-source SHA-256 baseline

```text
08d435cbc9ce99ba2e85de0a0edb7ee8e5015f3970a42550420ac3f9ae4cf103  jama_zahid_2025_oi_250093_1768590553.08463.pdf
0dcbfdf53363088fa65146d05d2f0e58b9c9f2fa001c9d60232207bbdec440a1  joi250093supp1_prod_1768590553.08963.pdf
a2b6c06f49f22bf3c5557b7943804c7598154d2e7ca40e7fcbad4dc32bed25e6  joi250093supp2_prod_1768590553.09463.pdf
```

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a12c37-1893-74f1-897e-a267d3ec6c91 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a12c3a-ad69-7ce3-9b2b-fe66c6bb1a9e | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a12c3e-01ad-7673-9de4-6a93ac228f9a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a12c3e-2db0-7c93-be73-02205fb46d25 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_002 | 01a12c3e-4cf1-7ae0-abe5-92f8e7eeeb7a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_002.md |
| support_quantitative_mapper_shard_003 | 01a12c3e-6be1-7ae3-bfde-811b576aabdb | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_003.md |
| support_quantitative_mapper_shard_004 | 01a12c3e-9878-7643-ac34-dc470d601834 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_004_results.md |
| numeric_consistency_reviewer | 01a12c43-4b9c-7822-9aac-7a3316381f85 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_reviewer_support_shard | 01a12c43-8381-77c0-a329-6a6ab73645eb | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| cross_source_consistency_reviewer | 01a12c43-c216-7643-8a0e-dfb48b6c9195 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a12c43-fb96-7943-933b-ea7e7d98f89b | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a12c4f-b7b6-7203-8c95-cfee2debbcc0 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| inclusion_source_confirmation_shard | 01a12c50-f19c-7ce1-aab5-f9cdca5b913f | gpt-6.1-sol | high | FRESH_SPAWN | screening/source_confirmation_plan.md |
| evidence_rechecker | 01a12c63-86c3-78d0-84d8-ccea451f5769 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| evidence_rechecker_shard_002 | 01a12c63-aaf3-7ea2-b202-3ccc33a45f88 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/recheck_002.md |
| evidence_rechecker_shard_003 | 01a12c63-ca83-7d51-ad07-f4248a018f40 | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/recheck_003.md |
| statistics_pass_2 | 01a12c69-56be-71f0-b3ab-86730a0e1482 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_b | 01a12c69-7ef5-7931-8e31-fcfee62a592a | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2b.md |
| statistics_pass_2_shard_c | 01a12c69-a5a4-7881-b225-dcd2aeae5d0f | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2c.md |
| quality_control_auditor | 01a12c70-5a35-7fc1-9c30-a421a32d87bf | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_candidates_002 | 01a12c70-9043-7552-8bc3-bac08204fa08 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_candidates_002.md |
| quality_control_auditor_candidates_003 | 01a12c70-bd04-7fb0-bfda-088b9ae10bfc | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_candidates_003.md |
| quality_control_auditor_source_coverage | 01a12c70-fcf0-7223-bf50-7ba7d37585a9 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_source_coverage.md |
| quality_control_auditor_statistical_coverage | 01a12c71-3159-7be1-afc7-7b767f8097c0 | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/audit_statistical_coverage.md |
| report_generator | 01a12c78-d931-75e1-90c1-ce1e873a2138 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

The authoritative execution record is [agent_execution_manifest.md](review_1_6_2/agent_execution_manifest.md).

### Reproducibility performance

- **Target basis:** Three PDF sources contain 134 unique pages. All pages have reusable evidence, but the 109-page bound PLAN has garbled layout text, only seven nonempty partial OCR pages, and readable rendered pages requiring complete visual mapping in bounded shards. Native article and results-supplement text reduces extraction work; protocol versions, SAP, intervention materials, statistical relationships, independent screening, direct recheck, two statistical passes, and final audit require multiple fresh agent waves. A 40-65 minute planning interval accounts for visual-only mapping and required review waves, independent of candidate count.
- **Total source units:** 134
- **Fresh-source units:** 0
- **Target elapsed minutes:** 40-65
- **Started UTC:** 2026-10-11T18:29:03Z
- **Finished UTC:** 2026-10-11T19:43:49Z
- **Observed elapsed minutes:** 74.77
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Fallback installation and approved GPU tooling preflight; visual-only mapping of the 109-page PLAN; bounded source-confirmation and candidate-recheck shards; three statistical-pass-2 shards and five independent audit shards; complete 19-card report assembly

Performance values are synchronized with [run_state.md](review_1_6_2/run_state.md) immediately after complete Markdown assembly. Local HTML rendering and mechanical validation are outside the review-duration window. A later model-based repair requires the coordinator to move the finish time forward and synchronize the timing record.
