# Workflow 1.6.2 Stable Candidate Ledger

Pending Human Adjudication. The independent initial screen included 19 findings, consolidated into 13 distinct issues. Stable IDs are assigned in source order by the first substantive conflicting statement/value: main REPORT pages and position within each page, then the plan-internal issue, then the results-supplement interim issue. Corroborating or affected-result-only locations do not reorder issues. Every finding and affected location is retained. No stable ID may be removed.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R, P_P | REPORT main article primary-subgroup definition vs PLAN protocol and operational-form definitions | reproduced | CONFIRMED | F-XS-001 |
| C002 | protocol_report | P_R | P_R | REPORT main article randomization vs PLAN protocol randomization | reproduced | CONFIRMED | F-XS-002, F-ST1-008 |
| C003 | protocol_report | P_R | P_R | REPORT main article and results-supplement hypoxemia windows vs PLAN protocol window | reproduced | CONFIRMED | F-XS-004, F-ST1-005 |
| C004 | protocol_report | P_R | P_R | REPORT main article and results-supplement duration endpoint vs PLAN protocol endpoint | reproduced | CONFIRMED | F-XS-003, F-ST1-004 |
| C005 | protocol_report | P_R | P_R | REPORT main article enrollment stopping rule vs PLAN protocol stopping rule | reproduced | CONFIRMED | F-XS-005, F-ST1-007 |
| C006 | protocol_report | P_R | P_R | REPORT main article and results-supplement time analyses vs PLAN protocol planned summaries | reproduced | CONFIRMED | F-XS-008 |
| C007 | statistical_results | S_W | S_W | REPORT main article Table 1 saturation denominators vs REPORT same-table missingness footnote | reproduced | CONFIRMED | F-NUM-002 |
| C008 | statistical_results | S_W | S_W | REPORT main article Table 1 medical-indication percentages vs REPORT same-table counts and denominators | reproduced | CONFIRMED | F-NUM-001 |
| C009 | statistical_results | S_W | S_W | REPORT main article Table 2 process intervals vs REPORT same-table P values and methods | reproduced | CONFIRMED | F-ST1-001 |
| C010 | statistical_results | S_W | S_W | REPORT main article Table 3 all-patient duration interval vs REPORT same-document interval order and methods | reproduced | CONFIRMED | F-ST1-003 |
| C011 | statistical_results | S_W | S_W | REPORT main article Table 3 Grade-4 interval vs REPORT same-table P value and methods | reproduced | CONFIRMED | F-ST1-002 |
| C012 | plan_material | P_P | P_P | PLAN protocol primary definition vs PLAN same-protocol primary missing-data recovery target | reproduced | CONFIRMED | F-XS-007, F-ST1-009 |
| C013 | protocol_report | P_R | P_R | REPORT results-supplement observed interim population vs PLAN protocol primary-population interim rule | reproduced | CONFIRMED | F-XS-006, F-ST1-006 |

## Registration evidence

The sections below preserve the independent screening evidence and all affected locations. Full checker arithmetic, alternative interpretations and human questions remain in the provenance artifacts referenced by each finding ID; subsequent direct-source recheck determines evidence state and confirms classification.

## C001 — subgroup-definition

**Finding IDs:** F-XS-001

Status: Pending Human Adjudication.


Suggested primary relationship **P_R**; all relationships **P_R, P_P**; domain **protocol_report**. PLAN [protocol p.13 §5.1 lines 427–431](../../joi180054supp1_prod.pdf#page=13) lists facial or neck trauma and airway edema; REPORT [main p.2 Patient Selection](../../jama_driver_2018_oi_180054.pdf#page=2) and [p.4 Figure 1 definition](../../jama_driver_2018_oi_180054.pdf#page=4) list facial trauma and obstruction or edema; PLAN [form p.9 item 12](../../joi180054supp2_prod.pdf#page=9) independently lists the operational features and gives obstruction examples, while [form p.7 item 3a](../../joi180054supp2_prod.pdf#page=7) distinguishes facial from neck trauma. The REPORT [main p.1 outcome definition](../../jama_driver_2018_oi_180054.pdf#page=1) confirms the published list and [p.7 Table 3 primary row](../../jama_driver_2018_oi_180054.pdf#page=7) supplies affected successes 191/198 and 150/182 in 380 patients. Cervical immobility versus immobilization, blood/vomit versus body fluids, and first-pass versus first-attempt names alone do not support this issue; the independent criterion omissions/addition do. No membership change is numerically inferred. A possible amendment or complete overlap of affected features remains a bounded alternative, not a source-supplied resolution.


## C002 — randomization-strata

**Finding IDs:** F-XS-002, F-ST1-008

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_R**; domain **protocol_report**. PLAN [protocol p.11 §4.1.1 lines 373–378](../../joi180054supp1_prod.pdf#page=11) includes apparent facial/neck trauma as an independent stratification feature; REPORT [main p.2 Randomization opening](../../jama_driver_2018_oi_180054.pdf#page=2) and [p.3 continuation](../../jama_driver_2018_oi_180054.pdf#page=3) retain obesity and cervical immobilization only. Matching 1:1 allocation and blocks 2,4,6,8,10 cannot settle the third criterion. The affected primary result is [main p.7 Table 3](../../jama_driver_2018_oi_180054.pdf#page=7). This allocation-rule issue is distinct from the primary subgroup-definition rule; both can be clarified independently.


## C003 — hypoxemia-window

**Finding IDs:** F-XS-004, F-ST1-005

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_R**; domain **protocol_report**. PLAN [protocol p.9 §2.2(1)/(4) lines 304–325](../../joi180054supp1_prod.pdf#page=9), [p.10 §3.2 lines 340–344,353–354](../../joi180054supp1_prod.pdf#page=10) ends capture one minute after cuff inflation; REPORT [main p.3 Measurements/Trial Outcomes](../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table 3 note b](../../jama_driver_2018_oi_180054.pdf#page=7), [p.9 Table 5 note b](../../jama_driver_2018_oi_180054.pdf#page=9), and [supplement p.3 hypoxemia note](../../joi180054supp2_prod.pdf#page=3) use first-attempt completion. Retain all composite cells: difficult 156/191 versus 123/177, overall 317/371 versus 282/366; standalone hypoxemia 47/371 versus 50/364. Identical thresholds do not equate capture windows, especially after unsuccessful first attempts. No numerical event-count change is inferred. This rule defines hypoxemia capture, separate from the duration variable's endpoint.


## C004 — duration-endpoint

**Finding IDs:** F-XS-003, F-ST1-004

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_R**; domain **protocol_report**. PLAN [protocol p.9 §2.2(2) lines 315–317](../../joi180054supp1_prod.pdf#page=9), [p.10 §3.2 lines 346–347](../../joi180054supp1_prod.pdf#page=10), and [p.19 §8.1 lines 657–660](../../joi180054supp1_prod.pdf#page=19); REPORT [main p.3 Trial Outcomes](../../jama_driver_2018_oi_180054.pdf#page=3), [p.7 Table 3 duration rows/note c](../../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../../jama_driver_2018_oi_180054.pdf#page=8), [supplement p.2 eTable 1 duration rows](../../joi180054supp2_prod.pdf#page=2), [p.3 duration note](../../joi180054supp2_prod.pdf#page=3), and [p.4 eFigure 1](../../joi180054supp2_prod.pdf#page=4). Cuff inflation with tracheal tube placement is the planned terminal event; laryngoscope removal is the published terminal event. Retain difficult medians 39/40 seconds, overall 38/36, contrasts and time-to-success analysis locations; [main p.1 abstract](../../jama_driver_2018_oi_180054.pdf#page=1) establishes key-secondary relevance. The statistical finding's ancillary reference to omitted KM summaries belongs to the independently retained planned-summary issue below, without creating a second duration-endpoint issue.


## C005 — enrollment-stop

**Finding IDs:** F-XS-005, F-ST1-007

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_R**; domain **protocol_report**. PLAN [protocol p.19 §8.2 lines 665–674](../../joi180054supp1_prod.pdf#page=19) versus REPORT [main p.3 Statistical Analysis](../../jama_driver_2018_oi_180054.pdf#page=3); retain [main p.1 study interval](../../jama_driver_2018_oi_180054.pdf#page=1), [p.2 trial dates](../../jama_driver_2018_oi_180054.pdf#page=2), and primary/final size context. One year/1000 and more than 374 difficult patients are distinct stated decision rules. The observed 380 difficult and 757 overall patients do not by themselves establish disagreement with either realized boundary; the unresolved question is whether the rules coincided, supplemented each other, or were amended.


## C006 — planned-km-summaries

**Finding IDs:** F-XS-008

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_R**; domain **protocol_report**. PLAN [protocol p.19 §8.1 lines 657–660](../../joi180054supp1_prod.pdf#page=19), with [p.9 §2.2(2)](../../joi180054supp1_prod.pdf#page=9); REPORT [main p.4 time methods](../../jama_driver_2018_oi_180054.pdf#page=4), [p.5 secondary results](../../jama_driver_2018_oi_180054.pdf#page=5), [p.7 Table 3](../../jama_driver_2018_oi_180054.pdf#page=7), [p.8 Figure 2](../../jama_driver_2018_oi_180054.pdf#page=8), [supplement p.2 eTable 1](../../joi180054supp2_prod.pdf#page=2), [p.3 notes](../../joi180054supp2_prod.pdf#page=3), and [p.4 eFigure 1](../../joi180054supp2_prod.pdf#page=4). The supplied sources prescribe KM estimates of 25th,50th,75th percentiles with two-sided 95% CIs and percent censored, but supply raw medians/IQR, difference CIs, curves, risk tables, log-rank tests and HR CIs. This issue is distinct from duration-endpoint replacement: even if cuff inflation and blade removal were equated, the prescribed percentile CIs and censoring percentage remain unreported; supplying or formally replacing those summaries would not itself establish equivalence of terminal events. The planned KM-summary clause cited inside F-ST1-004 is retained here as ancillary overlapping evidence, not another finding row or another duration candidate.


## C007 — initial-saturation-counts

**Post-registration precision refinement:** Mandatory continuous half-unit input ranges, rather than the exact-count sensitivity below, govern final precision reproduction. The implied per-arm missing-count ranges[28,30] and[31,33] remain separate from printed ranges[18.5,19.5] and[23.5,24.5]; the total range[59,63] versus[42.5,43.5] has gap15.5 and relative discrepancy15.5/43=0.36047. Final independent recheck confirms these intervals.


**Finding IDs:** F-NUM-002

Status: Pending Human Adjudication.


Suggested primary/all relationship **S_W**; domain **statistical_results**. REPORT [main p.5 Table 1 headers, oxygen-saturation median/threshold rows and note b](../../jama_driver_2018_oi_180054.pdf#page=5). Independent exact arithmetic: 381−352=29 and 376−344=32; total 61, versus printed 19+24=43 missing initial saturation. Exact patient-count intervals are singletons: [29,29] versus [19,19], [32,32] versus [24,24], and [61,61] versus [43,43]. Relative gaps 10/19=.52632, 8/24=.33333 and 18/43=.41860 exceed .05. The comparison is expressly printed missingness for the same measurement, rather than dividing the discrepancy by the larger observation denominators. Threshold-specific exclusions or different availability for the median versus threshold summaries are possible, but not supplied. The fact that threshold denominators match the heart-rate missingness counts is corroboration of a possible alignment explanation, not a correction.


## C008 — medical-percentages

**Post-registration precision refinement:** Under mandatory continuous half-unit input ranges, the two medical Other cells independently sustain this candidate (relative gaps0.12892 and0.11139). The respiratory/cardiac cells have relative gaps0.03272 and0.03453 and are contextual locations compatible with display precision; the registration arithmetic below used exact-count singleton sensitivity. Final recheck calculations control the report.


**Finding IDs:** F-NUM-001

Status: Pending Human Adjudication.


Suggested primary/all relationship **S_W**; domain **statistical_results**. REPORT [main p.5 Table 1, medical parent, all six nested indication rows and arm headers](../../jama_driver_2018_oi_180054.pdf#page=5). Exact count/base arithmetic produces singleton percentage intervals: 16/381×100=[4.19948,4.19948], 23/376×100=[6.11702,6.11702], 44/381×100=[11.54856,11.54856], and 41/376×100=[10.90426,10.90426]. Printed integer percentage intervals are [4.5,5.5], [6.5,7.5], [13.5,14.5], [12.5,13.5]; the remaining gaps divided by printed 5,7,14,13 are .06010,.05471,.13939,.12275. Counts sum to medical parents 318/315; dividing these four counts by those parents gives 5.031%,7.302%,13.836%,13.016%, but altered-mental-status counts would give 58.176%/54.921%, unlike printed 49%/46%, so indentation cannot explain one uniform conditional denominator. Consolidate all four cells as one denominator-switch pattern. No cross-source baseline-copy comparison is involved.


## C009 — process-interval-tests

**Finding IDs:** F-ST1-001

Status: Pending Human Adjudication.


Suggested primary/all relationship **S_W**; domain **statistical_results**. REPORT [main p.6 Table 2 senior resident/fellow, junior resident, video during passage rows](../../jama_driver_2018_oi_180054.pdf#page=6), with [p.4 methods](../../jama_driver_2018_oi_180054.pdf#page=4). Independently read differences −5 (−10 to0),5 (0 to10),−6 (−12 to0), each 95%, versus P=.03,.03,.04 at two-sided .05. The printed intervals contain zero, while tests are significant. Diagnostic unrounded endpoints could exclude zero, but route A category 1 explicitly exempts these conflicts from the display-precision exclusion; neither process-outcome peripherality nor recoverability from rounding can remove them. Retain all three rows as one repeated zero-endpoint pattern; do not merge the separate Grade-4 conflict with it merely because both concern interval/test compatibility.


## C010 — duration-interval-order

**Finding IDs:** F-ST1-003

Status: Pending Human Adjudication.


Suggested primary/all relationship **S_W**; domain **statistical_results**. REPORT [main p.7 Table 3, all-patient duration difference](../../jama_driver_2018_oi_180054.pdf#page=7), with [p.4 continuous-analysis methods](../../jama_driver_2018_oi_180054.pdf#page=4); REPORT [supplement p.2 corresponding eTable 1 cell](../../joi180054supp2_prod.pdf#page=2) and [p.3 clustering note](../../joi180054supp2_prod.pdf#page=3) corroborate a possible ascending ordering under a disclosed different analysis. Main prints 1 second (95% CI 4 to−1),P=.24. Endpoint half-unit ranges [3.5,4.5] and [−1.5,−.5] retain at least 4 seconds separation in descending order, relative to first endpoint 4 giving 1.00>.05. A numeric lower/upper interpretation requires selecting a changed printed reading; merely labeling the character spacing a typographic matter does not supply consistent extracted fields. The supplement's −1 to4,P=.95 is not a matched unadjusted duplicate: its different analysis and corroborating ordering do not create S_C or an additional P-value conflict. The exact original interval construction is not available to establish a final numeric reinterpretation.


## C011 — grade4-interval-test

**Finding IDs:** F-ST1-002

Status: Pending Human Adjudication.


Suggested primary/all relationship **S_W**; domain **statistical_results**. REPORT [main p.7 Table 3 Grade 4](../../jama_driver_2018_oi_180054.pdf#page=7), with [p.4 methods](../../jama_driver_2018_oi_180054.pdf#page=4). Arm counts 3/3 and2/5, arm intervals29–100/5–85, difference60 (17–100),P=.09,interactionP=.78 were read independently. Lower endpoint rounding interval [16.5,17.5] stays above zero; P rounding interval [.085,.095] stays above .05. The interval excludes zero while the P is nonsignificant. Different interval/test constructions are a human explanation to examine, not an inclusion-screen exclusion; interaction P belongs to another hypothesis. This conflict lacks the zero-endpoint pattern of the process issue and remains separate.


## C012 — primary-recovery-target

**Finding IDs:** F-XS-007, F-ST1-009

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_P**; domain **plan_material**. PLAN [protocol p.8 §2.1](../../joi180054supp1_prod.pdf#page=8), [p.9 primary continuation and §2.2(1)](../../joi180054supp1_prod.pdf#page=9), [p.20 §8.4.1/§8.6.1 lines719–720](../../joi180054supp1_prod.pdf#page=20), and [p.21 §8.6.1 lines721–722](../../joi180054supp1_prod.pdf#page=21). Primary target first-pass success differs from the specified primary recovery target first-pass success without hypoxemia, which elsewhere is expressly secondary. REPORT [main p.7 Table 3](../../jama_driver_2018_oi_180054.pdf#page=7) identifies the affected primary/composite results only; it does not conflict with the recovery instruction and creates no P_R relationship. No actual use of this pathway or changed patient classification is inferred. The primary analysis step relies on an internally different composite criterion; reconstructing both endpoints separately is a possible but unstated implementation.


## C013 — interim-population

**Finding IDs:** F-XS-006, F-ST1-006

Status: Pending Human Adjudication.


Suggested primary/all relationship **P_R**; domain **protocol_report**. PLAN [protocol p.20 §8.4.1/§8.5 lines693–706](../../joi180054supp1_prod.pdf#page=20) defines primary difficult-airway analysis and secondary all-enrolled analysis; [p.21 §8.6.2 lines730–741](../../joi180054supp1_prod.pdf#page=21) specifies primary-only interim. REPORT [supplement p.6 observed interim results and continuation sentence](../../joi180054supp2_prod.pdf#page=6) supplies 250/257 and213/250 after507 enrollment; 257+250=507 exactly. Retain REPORT [main p.3 primary population](../../jama_driver_2018_oi_180054.pdf#page=3) and the quoted protocol passage on supplement p.6 as corroboration of the original PLAN rule. That quotation need not be treated as a separate plan document to establish P_R: the original supplied protocol is the direct comparator. Rates reproduce their rounded percentages (250/257=97.276%,213/250=85.2%); the issue is the displayed population and decision basis. A separately performed unreported primary-only interim analysis, or all507 patients meeting a difficult feature, remains a bounded possibility; neither is supplied, and the documented overall calculation does not report the planned primary-subgroup result.


**C013 alternative clarification:** The final757-patient cohort contains380 difficult-airway participants, so all507 interim participants cannot belong to that primary subgroup under unchanged classification and complete final inclusion. An earlier suggestion that all507 might be difficult is not a source-supported resolution under those conditions. A separately performed but unreported primary-only interim calculation or documented population/definition amendment remains an open interpretation; no unseen implementation is inferred.
