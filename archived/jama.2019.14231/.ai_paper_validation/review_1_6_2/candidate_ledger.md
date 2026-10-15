# Stable Candidate Ledger

Pending Human Adjudication. Registration follows the independent initial inclusion screen. Every assigned ID is retained through completion. Source order uses the first display that hosts the conflicting statement or number, in source-inventory order; corroborating occurrences and general method locations do not move an issue ahead of its conflicting display. Main matching precedes Table 2; within Table 2 the consolidated arithmetic pattern precedes the independent interval/test issue. In supplement p2 the coronary row precedes AF; in p12 the inference heading/footnote precedes the hemoglobin row.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN original protocol p3 vs REPORT main matching statement pp3–4 | reproduced | CONFIRMED | F-XS-001 |
| C002 | statistical_results | S_W | S_W | REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk differences | reproduced | CONFIRMED | F-NUM-001 |
| C003 | statistical_results | S_W | S_W | REPORT main Table 2 cerebrovascular risk-difference interval vs REPORT main Table 2 adjusted hazard test | reproduced | CONFIRMED | F-ST1-002 |
| C004 | protocol_report | P_R | P_R | PLAN original protocol p4 coronary criteria vs REPORT results supplement eTable 1 p2 coronary criteria | reproduced | CONFIRMED | F-XS-003 |
| C005 | protocol_report | P_R | P_R | PLAN original protocol p4 AF codes vs REPORT results supplement eTable 1 p2 AF codes | reproduced | CONFIRMED | F-XS-002 |
| C006 | protocol_report | P_R | P_R | PLAN original protocol p6 inference rule vs REPORT results supplement eTable 8 p12 Bonferroni intervals | reproduced | CONFIRMED | F-ST1-005 |
| C007 | statistical_results | S_W | S_W | REPORT results supplement eTable 8 p12 hemoglobin interval vs REPORT results supplement eTable 8 p12 hemoglobin P value | reproduced | CONFIRMED | F-ST1-003 |
| C008 | statistical_results | S_W | S_W | REPORT results supplement eTable 12 p20 primary E-values vs REPORT results supplement eTable 12 p20 nonprimary reproducing comparator | reproduced | CONFIRMED | F-ST1-004 |

## C001 — Primary matching allocation differs between plan and report

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original protocol p3 vs REPORT main matching statement pp3–4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route B

**Classification rationale:** The directly compared operational or analysis statements belong to PLAN and REPORT by content; P_R determines protocol_report.

**Classification ambiguity:** The printed PLAN orientation may be a transposed statement or a different intended allocation; the supplied plan does not establish intent or a revision.

**Checker provenance:** cross_source_consistency; independent inclusion_screener initial. F-ST1-006 was screened as DUPLICATE_OF_INCLUDED; all of its affected locations remain in this issue.

**Title:** The original matching statement reverses the surgical-to-nonsurgical allocation stated in the report.

**Compared locations and document roles:** [PLAN original protocol p3, Matching Process](../../joi190103supp2_prod.pdf#page=3); [PLAN original protocol p6, Sensitivity analyses](../../joi190103supp2_prod.pdf#page=6); [REPORT main abstract p1](../../jama_aminian_2019_oi_190103.pdf#page=1); [REPORT main Figure1 and matching caption p3](../../jama_aminian_2019_oi_190103.pdf#page=3); [REPORT main statistical analysis p4](../../jama_aminian_2019_oi_190103.pdf#page=4). Amendment [PLAN p7](../../joi190103supp2_prod.pdf#page=7) adds safety/E-values and supplies no revised matching statement.

**Printed statements:** Original PLAN p3: “Each non-surgical patient will be matched ... to five (5) surgical patients.” REPORT p3: “each surgical patient was matched ... to 5 nonsurgical patients”; REPORT p4 repeats that direction. Reported populations are 2287 surgical and11435 matched nonsurgical patients. PLAN p6 says one reported dataset uses1:5 matching, without defining group direction in that sentence.

**Comparison logic:** Hold the exposure groups and primary matched analysis fixed. Five surgical per nonsurgical implies surgical:nonsurgical5:1; five nonsurgical per surgical implies1:5. Report count ratio11435/2287=5 agrees with the second statement. This is a categorical matching-specification comparison, not an estimate compared with a crude ratio; interval rounding cannot turn one orientation into the other. The p6 sensitivity convention suggests the reported orientation but does not revise the explicit p3 rule.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route B.

**Affected result or extracted value:** The matched population underlying the primary composite adjusted HR0.61(95%CI0.55–0.69) and its interpretation as a one-surgical-to-five-control analysis.

**Why context does not resolve it:** The report establishes the performed ratio; the supplied original plan explicitly describes its inverse. Knowing the performed ratio does not establish whether the planned primary matching allocation was reversed in wording or changed in implementation. The difference changes an analysis-population design element rather than names for equivalent groups.

**Supported alternatives:** The p3 group orientation may have been transposed when the plan was written; alternatively the final matching allocation may differ from that explicit rule. PLAN p6's1:5 wording is compatible with the report but does not independently specify direction.

**Human question:** Which surgical:nonsurgical matching allocation was intended for the primary analysis in the January6 protocol, and how should its p3 statement be reconciled with the reported2287:11435 matched cohort?

## C002 — Five absolute risk differences do not reproduce displayed risk subtraction

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 group risks vs REPORT main Table 2 absolute risk differences

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 4

**Classification rationale:** The conflicting printed results are within one REPORT document; S_W determines statistical_results. Other documents that only corroborate a value do not add a relationship.

**Classification ambiguity:** None

**Checker provenance:** numeric_consistency; independent inclusion_screener initial. F-ST1-001 was screened as DUPLICATE_OF_INCLUDED; all of its affected locations remain in this issue.

**Title:** Five Table2 individual-outcome absolute risk differences do not reproduce from the displayed8-year risks.

**Exact compared locations and document roles:** REPORT main article [PDFp7,Table2](../../jama_aminian_2019_oi_190103.pdf#page=7),heart failure,coronary artery disease,cerebrovascular disease,nephropathy,and atrial fibrillation rows:Metabolic Surgery and Nonsurgical Control cumulative-incidence columns versus Absolute8-Year Risk Difference column and footnotea. REPORT main article [PDFp4,Statistical Analysis](../../jama_aminian_2019_oi_190103.pdf#page=4) specifies Kaplan–Meier cumulative incidence and bootstrapped8-year absolute risk differences. REPORT results supplement [PDFp7,eTable5](../../joi190103supp1_prod.pdf#page=7) corroborates the five displayed group risks;it is corroboration,not a separate conflicting source relationship.

**Focus area:** B (estimate logic),with arithmetic difference identity under C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category4.

**Printed inputs,rule and calculation:** Footnotea defines the difference as nonsurgical control−metabolic surgery. The same difference method reproduces the primary47.7−30.8=16.9,secondary27.6−17.0=10.6,and mortality17.8−10.0=7.8 rows. All inputs and differences below print one decimal;allow each risk ±0.05 percentage points and each printed difference ±0.05. Each difference interval is [control−surgery−0.10,control−surgery+0.10]. All units are percentage points.

| Outcome | Surgery risk | Control risk | Printed ARD(95%CI) | Control−surgery | Recomputed interval | Printed ARD interval | Remaining gap | Relative discrepancy |
|---|---:|---:|---|---:|---|---|---:|---:|
| Heart failure |6.8|18.9|12.9(10.4–15.1)|12.1|[12.00,12.20]|[12.85,12.95]|0.65|0.0503876|
| Coronary artery disease |7.9|11.6|4.2(1.9–6.8)|3.7|[3.60,3.80]|[4.15,4.25]|0.35|0.0833333|
| Cerebrovascular disease |4.1|5.6|1.8(−0.03 to3.4)|1.5|[1.40,1.60]|[1.75,1.85]|0.15|0.0833333|
| Nephropathy |6.1|16.3|11.1(8.8–13.6)|10.2|[10.10,10.30]|[11.05,11.15]|0.75|0.0675676|
| Atrial fibrillation |7.9|13.6|6.5(4.4–8.7)|5.7|[5.60,5.80]|[6.45,6.55]|0.65|0.1000000|

The relative discrepancy divides the remaining gap by the absolute printed ARD. Every value exceeds0.05;heart failure remains just above the threshold after the complete half-unit calculation. The displayed method that reproduces three other rows does not reproduce these five rows. Consolidate these repeated failures of the same explicitly defined difference column as one reporting issue.

**Affected result or extracted value:** The8-year absolute reduction in each of the five individual outcomes;a data extractor could use12.9,4.2,1.8,11.1,and6.5 percentage points or the displayed group-risk differences12.1,3.7,1.5,10.2,and5.7. The reported ARD interval limits are retained as printed and cannot be reconstructed from marginal group confidence limits.

**Why context does not resolve it:** This is route A category4:a printed result does not reproduce under the difference method that reproduces other rows of the same display. Footnotea supplies orientation and bootstrap CI construction,but supplies no alternate point-estimate definition for these five rows. The supplied description does not identify which extraction value applies. The known point estimates and labelled risk differences are compared,not adjusted Cox HRs against crude ratios.

**Source-grounded alternatives and missing definition:** Bootstrap resampling is stated for95%CIs;an unstated bootstrap mean,alternate risk-set standardization,or another point-estimate construction might explain the difference column,but the source does not state such a distinction. Individual baseline-history exclusions exist,but both group risks and their difference occupy the same individual-outcome rows. The observed discrepancy does not establish its production mechanism. No preferred analysis or numerical correction is proposed.

**Exact human question:** What point-estimate definition produced the five individual-outcome absolute8-year risk differences,and which group risks and analysis populations should be used to interpret or extract them?

## C003 — Cerebrovascular risk interval and treatment test give different null readings

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 cerebrovascular risk-difference interval vs REPORT main Table 2 adjusted hazard test

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting printed results are within one REPORT document; S_W determines statistical_results. Other documents that only corroborate a value do not add a relationship.

**Classification ambiguity:** None

**Checker provenance:** statistical_pass_1; independent inclusion_screener initial.

**Title:** The cerebrovascular8-year risk-difference interval includes the null while the displayed treatment test is significant.

**Exact locations and document roles:** REPORT [main Table2p7 cerebrovascular row and footnotesa/b](../../jama_aminian_2019_oi_190103.pdf#page=7); REPORT [main p6 lower-incidence narrative](../../jama_aminian_2019_oi_190103.pdf#page=6); REPORT [main p4 confidence/significance methods](../../jama_aminian_2019_oi_190103.pdf#page=4). Corroborating adjusted HR/P appears in REPORT [Figure3Dp8](../../jama_aminian_2019_oi_190103.pdf#page=8) and REPORT [eTable6p9](../../joi190103supp1_prod.pdf#page=9). S006,S038; corroborating copies do not add a conflicting relationship.

**Printed values, rule and calculation:** ARD1.8 percentage points,95%CI−.03 to3.4 contains null0: −.03≤0≤3.4. Same row adjustedHR.67(.48,.94),P=.02; .02<.05, HR interval excludes1. General alpha.05 two-sided/95%CI. Thus the displayed95% risk-difference interval and significant displayed treatment test give different null/significance readings. The HR/CI/P tuple itself reconciles. Scope RouteA1 explicitly retains an interval/test conflict even when assigned to different analyses.

**Display precision:** RouteA1 is exempt from the relative-gap rounding screen. Lower limit−.03 has half-unit[−.035,−.025], still negative; upper3.4 is positive; P=.02 half-unit[.015,.025], still significant at.05. No numerical estimate/P identity is imposed across estimands.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Cerebrovascular8-year absolute risk difference with its95%CI, and the significance attached to the reported reduction in cerebrovascular incidence.

**Why context does not resolve it:** RouteA1 applies to the printed interval versus test conflict. The table's stated Cox-versus-bootstrap distinction is an alternative interpretation that explains why different estimands may yield different decisions; under this review scope it does not remove the finding.

**Alternatives and missing definition:** Footnotea identifies bootstrap8yrisk difference, footnoteb adjusted instantaneous-hazard test. The P may intentionally concern only the HR and not the8yrisk difference; no risk-difference test/P is supplied. This finding does not assert those analyses should be numerically equivalent.

**Exact human question:** Should the significant cerebrovascularP=.02 and lower-incidence statement be read solely as the adjustedHR inference, while the printed8-year risk-difference95%CI includes0, and how should the absolute-risk result be interpreted/extracted?

## C004 — Coronary diagnosis-position criteria differ between printed plan and report

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original protocol p4 coronary criteria vs REPORT results supplement eTable 1 p2 coronary criteria

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route A, category 5

**Classification rationale:** The directly compared operational or analysis statements belong to PLAN and REPORT by content; P_R determines protocol_report.

**Classification ambiguity:** The original protocol refers to eTable 1; incorporation of a fuller definition may reconcile the criteria, but no separately dated incorporated table or explicit precedence is supplied.

**Checker provenance:** cross_source_consistency; independent inclusion_screener initial.

**Title:** The printed coronary-event descriptions differ in diagnosis-position detail.

**Compared locations and document roles:** [PLAN original protocol p4, Coronary artery disease, Other and primary endpoint](../../joi190103supp2_prod.pdf#page=4); [REPORT non-plan supplement p2, eTable1 Coronary artery disease and bold-text footnote](../../joi190103supp1_prod.pdf#page=2); [REPORT main p2 coronary endpoint definition](../../jama_aminian_2019_oi_190103.pdf#page=2); [REPORT main Table2 p7](../../jama_aminian_2019_oi_190103.pdf#page=7); [PLAN amendment p7](../../joi190103supp2_prod.pdf#page=7).

**Printed statements:** PLAN p4 lists `411.X, 411.X AND 414.X` with no primary-diagnosis condition. REPORT eTable1 renders the standalone `411.X` bold and renders `414.X` bold in the `411.X AND 414.X` pair; the accompanying footnote says bold text indicates it must be a primary diagnosis. The paired `411.X` is regular. The restriction therefore qualifies specific codes, not the whole row. Direct source-page visual inspection confirmed the distinction. PLAN p4 has no matching bold convention or primary-diagnosis statement, and the supplied amendment does not revise coronary ascertainment.

**Comparison logic:** The inline PLAN passage does not state diagnosis position. The REPORT list expressly requires primary-diagnosis status for the indicated codes; the original incorporated eTable 1 could already supply that condition. Code identity agrees, but the printed passages differ in diagnosis-position detail. This is an operational component criterion comparison with no numerical display-precision calculation.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Coronary-event qualifying diagnoses and baseline-history/risk-set ascertainment, the coronary HR0.69(95%CI0.54–0.87), and the coronary component of the primary composite HR0.61(0.55–0.69).

**Why context does not resolve it:** Route A category5 applies to the additional operational requirement for a prespecified composite component. The footnote changes the logical qualifying criterion. It is not a visual-formatting observation: primary versus secondary diagnosis position can determine whether the listed diagnosis qualifies. No effect on event totals is inferred.

**Supported alternatives:** The original plan may leave diagnosis position implicit while the result supplement supplies the fuller intended specification; or a restriction may have been added between the original plan and reported ascertainment. The original plan refers to eTable1, which could incorporate its operational elaboration, but no supplied plan version records whether the restriction was intended originally or amended.

**Human question:** Were the primary-diagnosis requirements for standalone411.X and paired414.X used in both planned and reported coronary-event ascertainment, and how does the unqualified original rule relate to the reported restricted rule?

**Registration clarification:** PLAN p4 expressly refers to eTable 1 for diagnosis codes and definitions. This is a source-grounded incorporation alternative, not evidence that all diagnosis positions or an expanded code set were implemented differently. No event-count effect or timing of an operational change is asserted.

## C005 — Atrial-fibrillation code criterion differs between printed plan and report

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original protocol p4 AF codes vs REPORT results supplement eTable 1 p2 AF codes

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route A, category 5

**Classification rationale:** The directly compared operational or analysis statements belong to PLAN and REPORT by content; P_R determines protocol_report.

**Classification ambiguity:** The original protocol refers to eTable 1; incorporation of a fuller definition may reconcile the criteria, but no separately dated incorporated table or explicit precedence is supplied.

**Checker provenance:** cross_source_consistency; independent inclusion_screener initial.

**Title:** The printed REPORT AF code list includes i48.1 beyond the inline PLAN list.

**Compared locations and document roles:** [PLAN original protocol p4, Atrial fibrillation and primary endpoint](../../joi190103supp2_prod.pdf#page=4); [REPORT non-plan supplement p2, eTable1 Atrial fibrillation](../../joi190103supp1_prod.pdf#page=2); [REPORT main endpoint definition p2](../../jama_aminian_2019_oi_190103.pdf#page=2); [REPORT main Table2 p7](../../jama_aminian_2019_oi_190103.pdf#page=7); [PLAN amendment p7](../../joi190103supp2_prod.pdf#page=7).

**Printed statements:** PLAN lists AF ICD10 `i48.0, i48.2, i48.91`; REPORT eTable1 lists `i48.0, i48.1, i48.2, i48.91`. ICD9 `427.31` and CPT `93650,93653,93656,93657` agree. PLAN primary composite is the first occurrence of the six listed components, including AF; REPORT also includes AF. Amendment does not describe an AF-definition change.

**Comparison logic:** Compare the operational AF code criteria item by item, not merely the endpoint names. The printed REPORT AF ICD10 list equals the inline PLAN list plus `i48.1`. The printed REPORT list contains an additional qualifying code relative to the inline PLAN list, while the named six components remain the same. The original incorporated eTable 1 could already supply that fuller list; an implemented expansion is not established. This categorical/code-set comparison has no rounding interval.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** AF qualifying events and AF baseline risk-set eligibility, its reported HR0.78(95%CI0.62–0.97), and the AF contribution to the primary six-component composite HR0.61(0.55–0.69).

**Why context does not resolve it:** Route A category5 applies to the reproduced operational definition change in a prespecified primary composite component. The package does not state whether the extra code was included in both planned and implemented ascertainment or added later. No event-count impact is inferred.

**Supported alternatives:** The original list may incompletely document the code set actually intended; the report may describe a broadened ascertainment rule; or the operational extraction may use another reconciled list. None is specified by the supplied amendment.

**Human question:** Was `i48.1` included when identifying baseline and incident AF for the primary composite and individual AF analyses, and which supplied plan definition documents that choice?

**Registration clarification:** PLAN p4 expressly refers to eTable 1 for diagnosis codes and definitions. This is a source-grounded incorporation alternative, not evidence that all diagnosis positions or an expanded code set were implemented differently. No event-count effect or timing of an operational change is asserted.

## C006 — Planned multiplicity rule and reported longitudinal intervals differ

Pending Human Adjudication.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original protocol p6 inference rule vs REPORT results supplement eTable 8 p12 Bonferroni intervals

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-005

**Qualifying route:** Route B

**Classification rationale:** The directly compared operational or analysis statements belong to PLAN and REPORT by content; P_R determines protocol_report.

**Classification ambiguity:** The unadjusted rule may cover vascular secondary outcomes only, leaving a separately corrected longitudinal family; its boundary is not specified.

**Checker provenance:** statistical_pass_1; independent inclusion_screener initial.

**Title:** Bonferroni-corrected longitudinal intervals are reported despite the original plan's unadjusted secondary-analysis rule.

**Exact locations and document roles:** PLAN [original protocolp6 Statistical analysis](../../joi190103supp2_prod.pdf#page=6), weight/HbA1c comparison paragraph followed by significance/multiplicity paragraph; PLAN [amendmentp7](../../joi190103supp2_prod.pdf#page=7) adds nutritional/adverse-event/E-value work without a revised multiplicity rule. REPORT [eTable8p12](../../joi190103supp1_prod.pdf#page=12) all52 intervals and confidence/method footnotes; REPORT [main p4](../../jama_aminian_2019_oi_190103.pdf#page=4) general.05/95% exploratory secondary rule. S094, S049–S061.

**Printed statements and logical rule:** PLANp6 says significance.05,95%CIs where applicable, and adjustment for multiple comparisons of secondary endpoints is not performed. REPORTeTable8 expressly labels every estimate interval98.8%(Bonferroni-corrected). This is an explicit adjustment in the longitudinal comparison display, not different decimal precision for95%.98.75% corresponds to Bonferroni4 at familyalpha.05, rounded98.8%; the exact corrected family is not named. Row other-antihypertensive1y−2.7(−5.6,.3),P=.02 exemplifies an inference whose rawP<.05 while corrected interval contains0. That row itself reconciles at its stated98.8% confidence level and is not an additional CI/P finding.

**Display precision:** Categorical rule/analysis comparison; no half-unit arithmetic can reconcile an expressly unadjusted rule with an expressly Bonferroni-corrected display. The correction family and amendment history, rather than a numeric rounding gap, are the missing definitions.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The prespecified weight/HbA1c longitudinal comparisons and the related medication/nutritional comparison intervals; specifically which confidence level and multiplicity rule should accompany their extracted effects and how year1 antihypertensiveP=.02 is read.

**Why context does not resolve it:** The plan states an unadjusted secondary rule and the report adds a correction without specifying which family is covered or whether these longitudinal outcomes are exempt from that plan rule. The changed confidence level bears directly on interpretation of reported intervals. The explicit vascular exploratory rule does not alone state a separate planned longitudinal adjustment.

**Alternatives and missing definition:** The plan's no-adjustment rule may intend only the seven vascular secondary outcomes, leaving longitudinal analyses a separate family; alternatively a correction may have been introduced for time-point comparisons. The amendment adds nutritional outcomes but no confidence/multiplicity clarification. The table fully discloses that its intervals are corrected; no concealed change is asserted.

**Exact human question:** What analysis family and prospective or amended rule underlie the98.8% Bonferroni intervals, and how does that longitudinal rule relate to the original plan's unadjusted secondary-analysis statement?

## C007 — Year-5 hemoglobin interval and P value give different null readings

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 8 p12 hemoglobin interval vs REPORT results supplement eTable 8 p12 hemoglobin P value

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting printed results are within one REPORT document; S_W determines statistical_results. Other documents that only corroborate a value do not add a relationship.

**Classification ambiguity:** None

**Checker provenance:** statistical_pass_1; independent inclusion_screener initial.

**Title:** The year5 hemoglobin98.8% interval includes zero while its P value is below.001.

**Exact locations and document roles:** REPORT [eTable8p12 Hemoglobin(g/dL), year5 estimate/CI/P](../../joi190103supp1_prod.pdf#page=12), column heading98.8% and Bonferroni footnote, spline×treatment method footnote. REPORT [main methodsp4](../../jama_aminian_2019_oi_190103.pdf#page=4) supplies two-sided testing and spline comparisons. S054.

**Printed values, rule and calculation:** −.1g/dL,98.8%CI(−.2,0),P<.001*. The interval includes null0; its corresponding alpha.012 (.0125 for98.75%rounded) exceeds.001, so a same-analysisP<.001 rejects at both.012 and.0125 while the printed interval includes the null. This remains a CI/test conflict even under the explicitly corrected interval level; it is not generated by comparing98.8% to.05. Years1/2/8 intervals exclude0 withP<.001 and reconcile.

**Display precision:** RouteA1 does not permit excluding a printed zero-endpoint interval/test conflict as rounding. A small negative unrounded upper limit could print0; that is preserved as an alternative for human review. No covariance/df or numerical splineSE is supplied to recover an unrounded interval; no Wald diagnostic used to infer an exactP.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The year5 surgery-versus-nonsurgery hemoglobin mean-change contrast−.1g/dL and whether its Bonferroni interval excludes0.

**Why context does not resolve it:** RouteA1 applies to the printed interval/test decision. The source does not identify an alternative test target for that P, and the displayed confidence limit0 is a extractable numerical endpoint, not a notation-only observation.

**Alternatives and missing definition:** The upper limit may be a rounded negative number, or P may test a different spline association/contrast than the time-specific interval. Source supplies neither unrounded limit nor a different P estimand; these possibilities are not adjudicated.

**Exact human question:** What unrounded year5 hemoglobin interval and test/contrast produced the printed98.8%CI(−.2,0) andP<.001, and do both refer to the same time-specific mean-change difference?

## C008 — Primary E-values do not reproduce the comparator supported by other rows

Pending Human Adjudication.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 12 p20 primary E-values vs REPORT results supplement eTable 12 p20 nonprimary reproducing comparator

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-004

**Qualifying route:** Route A, category 4

**Classification rationale:** The conflicting printed results are within one REPORT document; S_W determines statistical_results. Other documents that only corroborate a value do not add a relationship.

**Classification ambiguity:** None

**Checker provenance:** statistical_pass_1; independent inclusion_screener initial.

**Title:** The primary E-value pair does not reproduce the transformation supported by the other seven rows of the same display.

**Exact locations and document roles:** REPORT [eTable12p20 primary E-values2.15/1.92 and seven comparator rows](../../joi190103supp1_prod.pdf#page=20); REPORT [p19 E-value definition/primary explanation](../../joi190103supp1_prod.pdf#page=19); REPORT [eTable6p9 treatmentHR/upperCI](../../joi190103supp1_prod.pdf#page=9) and REPORT [main Table2p7](../../jama_aminian_2019_oi_190103.pdf#page=7) corroborate primaryHR.61/upper.69. S076–S083. PLANamendmentp7 merely corroborates intended8outcome analyses and is not a conflicting location.

**Printed values, rule and calculation:** PrimaryHR.61(.55,.69), E-value2.15 and upper-limitE-value1.92. Use within-display reproducing algebraic comparator E(h)=1/h+sqrt((1/h)(1/h−1)), h<1. No formula is supplied and this comparator is not assumed from convention: it reproduces both entries of each of the seven nonprimary rows after their stated display precision.

| Outcome | PrintedHR/upperCI | RecomputedEpoint interval | PrintedEpoint | RecomputedElimit interval | PrintedElimit |
|---|---|---|---|---|---|
| Secondary | .62/.72 | [2.57980,2.63493] | 2.62 | [2.10263,2.14525] | 2.11 |
| Death | .59/.72 | [2.75025,2.81061] | 2.81 | [2.10263,2.14525] | 2.13 |
| HF | .38/.49 | [4.63434,4.77485] | 4.69 | [3.45583,3.54152] | 3.52 |
| CAD | .69/.87 | [2.23348,2.27920] | 2.27 | [1.54692,1.58084] | 1.55 |
| Cerebrovascular | .67/.94 | [2.32606,2.37412] | 2.35 | [1.30637,1.34219] | 1.31 |
| Nephropathy | .40/.52 | [4.37373,4.50080] | 4.46 | [3.21753,3.29402] | 3.29 |
| AF | .78/.97 | [1.86456,1.90238] | 1.9 | [1.18781,1.23014] | 1.21 |

Each printedEvalue half-unit interval overlaps its recomputation interval. For primaryHR half-unit[.605,.615], Epoint[2.6349328,2.6917194] versus printed[2.145,2.155]; gap.4799328/2.15=.2232246. PrimaryupperCI[.685,.695] givesElimit[2.2334792,2.2791950] versus printed[1.915,1.925]; gap.3084792/1.92=.1606663. Both exceed.05. Consolidated one transformation-pattern finding across its point and limit entries and duplicated p19 explanation.

**Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** Primary-outcome robustness E-value2.15 and closest-null-limitE-value1.92, repeatedly interpreted as minimum confounding strengths in p19/mainp9.

**Why context does not resolve it:** RouteA4: a comparator supported by all14 nonprimary entries does not reproduce the primary entries by more than5%. The table gives no primary-specific transformation choice. This is not an unsupported external formula assertion or isolated missing-definition observation.

**Alternatives and missing definition:** The primary endpoint has a larger cumulative risk and may intentionally use a different HR-to-RR conversion than other endpoints. The source defines E-values on RR scale but does not specify transformation, incidence threshold or primary-specific input. A distinct conversion could reconcile the pair; this is the human question, not a reason to exclude the observable same-display mismatch. No external E-value formula or literature was consulted.

**Exact human question:** Which HR-to-risk-ratio transformation and inputs produced primaryE-values2.15/1.92, and why do those entries use a construction different from the one reproducing the other seven outcome rows?

