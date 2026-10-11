# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication. Ten independently screened issues are registered. Initial C001-C009 follow source order: earliest conflicting REPORT page, within-page paragraph order, then PLAN-only source/page order. The independently included pass-2 issue is appended as C010 without renumbering earlier IDs. All assigned IDs are stable and must remain visible. No candidate count was sought.

## Classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN original/final SAP vs REPORT main article and results supplement | reproduced | CONFIRMED | F-XS-004 |
| C002 | protocol_report | P_R | P_R | PLAN final protocol vs REPORT main article | reproduced | CONFIRMED | F-XS-101 |
| C003 | protocol_report | P_R | P_R | PLAN original/final SAP vs REPORT main article and results supplement | reproduced | CONFIRMED | F-XS-003 |
| C004 | protocol_report | P_R | P_R | PLAN original/final SAP vs REPORT main article and results supplement | reproduced | CONFIRMED | F-XS-002 |
| C005 | statistical_results | S_W | S_W | REPORT main article methods vs REPORT main article Table 2 and narrative | reproduced | CONFIRMED | F-ST1-001 |
| C006 | protocol_report | P_R | P_R | PLAN original/final SAP vs REPORT main article | reproduced | CONFIRMED | F-XS-001 |
| C007 | statistical_results | S_W | S_W | REPORT results supplement eTable 9 count/percentage vs REPORT same-table denominator | reproduced | CONFIRMED | F-NUM-001 |
| C008 | plan_material | P_P | P_P | PLAN SAP availability table vs PLAN same-bundle power table | reproduced | CONFIRMED | F-ST1-002 |
| C009 | plan_material | P_P | P_P | PLAN SAP detectable-difference prose vs PLAN same-bundle formula, probability table and summary | reproduced | CONFIRMED | F-ST1-003 |
| C010 | protocol_report | P_R | P_R | PLAN final protocol vs REPORT main article and results supplement | reproduced | CONFIRMED | F-ST2-101 |

## C001 — Planned anatomical relative-risk regression outputs are not reported

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-004

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original/final SAP vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route A, category 5

**Classification rationale:** The conflict compares prospective PLAN specifications with REPORT content or outputs; corroborating plan passages do not create an additional relationship.

**Classification ambiguity:** None; source-grounded alternatives and missing definitions remain below.

### Originating checker evidence and complete affected locations

- **Locations and roles:** PLAN [originalSAPp17prespecified subgroup analysis](../../joi190092supp3_prod.pdf#page=17), PLAN [finalSAPp58prespecified subgroup analysis](../../joi190092supp3_prod.pdf#page=58); REPORT [mainp1abstract anatomical results](../../jama_rathinam_2019_oi_190092.pdf#page=1), REPORT [mainp4anatomical analysis methods](../../jama_rathinam_2019_oi_190092.pdf#page=4), REPORT [mainp5anatomical result narrative](../../jama_rathinam_2019_oi_190092.pdf#page=5), REPORT [mainp6Table2 and intermediate result](../../jama_rathinam_2019_oi_190092.pdf#page=6), REPORT [results supplement contents](../../joi190092supp1_prod.pdf#page=1).
- **Printed comparison:** Both SAP versions say “We will also report relative risks in each substratum, using relative risk regression.” The history-based anatomical subgroup is prespecified. Report provides subgroup success proportions, risk differences and logistic ORs: intermediateOR.29(.08–1.05),RD−30.3%(−51.6–1.1); posterior/panOR2.35(1.16–4.90),RD19.1%(3.6–30.6). No anatomical regression relative-risk estimate/CI is reported in main or results supplement.
- **Comparison logic:** The anatomical success outcome is key secondary because it is reported in the abstract; the SAP contains a definite additional regression analysis and promised measure. OR, RD and RR are different outputs. Crude RRs can be computed from counts but cannot reproduce an unreported regression RR and are not substituted for it. Display precision does not apply to absence of the specified effect measure.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.
- **Checker qualifying route (provisional):** Route A, category5.
- **Affected result or extracted value:** The two prespecified anatomical key-secondary treatment-effect regression relative risks, potentially used for evidence synthesis instead of the displayed ORs.
- **Why context does not resolve it:** RouteAcategory5 covers a planned key-secondary analysis not reported. The supplied ORs and risk differences identify those measures unambiguously but do not supply the promised regression relative risks.
- **Supported alternatives:** The regression RRs may be reserved for another report or omitted as redundant; no such result or amendment is supplied. There is no claim that ORs were mislabeled or that a model-based RR equals a crude risk ratio.
- **Exact human question:** Where are the planned relative-risk regression estimates for each anatomical subgroup, or which supplied amendment changes that analysis commitment?

## C002 — Primary success composite differs in its late-injection component

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-101

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol vs REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route A, category 5

**Classification rationale:** The conflict compares prospective PLAN specifications with REPORT content or outputs; corroborating plan passages do not create an additional relationship.

**Classification ambiguity:** The applied primary definition/version and any unsupplied amendment remain unresolved; final-protocol application with an abbreviated report definition is possible.

### Originating checker evidence and complete affected locations

- **Compared locations and roles:** PLAN [final protocol p.80, §2.5.1](../../joi190092supp2_prod.pdf#page=80); REPORT [main p.3, Treatment and Outcomes](../../jama_rathinam_2019_oi_190092.pdf#page=3), [p.4, primary analysis](../../jama_rathinam_2019_oi_190092.pdf#page=4), and [p.6, late injection narrative](../../jama_rathinam_2019_oi_190092.pdf#page=6). PLAN [final SAP p.70, §3.5.1](../../joi190092supp3_prod.pdf#page=70) and [p.81, injection revision](../../joi190092supp3_prod.pdf#page=81) supply the alternative sensitivity rule, rather than a disclosed replacement of the primary composite.
- **Printed statements:** Protocol p.80 defines primary success with “no periocular or intravitreal corticosteroid injections after the first 90 days of follow up,” alongside inflammation, prednisone, topical steroid and prior failure requirements. REPORT p.3 enumerates three success criteria: controlled inflammation, oral/topical steroid limits, and no declared intolerability/safety failure. Its efficacy-failure definition cites the first two criteria, and late injections are separately called protocol deviations. REPORT p.4 includes all patients with a month6 visit or early failure in the primary analysis. REPORT p.6 says four patients in each arm received corticosteroid injections more than90 days after randomization. Final SAP p.70 explicitly labels assessment at injection time a sensitivity analysis: uncontrolled inflammation implies failure, while meeting success criteria at injection implies success.
- **Comparison logic and reproduction:** The final manual includes a mandatory no-late-injection component of the six-month patient-level success composite; the report's enumerated success definition and efficacy-failure definition do not include it. A protocol-deviation label does not specify failure status. This is a composite-definition comparison, not a recalculation of the primary counts. The image of exact protocol p.80 confirms the component. Eight reported patients had the relevant exposure; their individual outcome classifications are not supplied. No primary-count alteration is inferred.
- **Focus area:** D.
- **Proposed review domain:** `protocol_report`.
- **Proposed relationship type:** `P_R`; **All relationships:** `P_R`.
- **Checker qualifying route (provisional):** Route A, category 5.
- **Affected result or extracted value:** Six-month treatment success64/96 versus56/98, and the corresponding primary treatment comparison; extraction of the complete treatment-success definition.
- **Why context does not resolve it:** Route A category5 concerns changed composite definitions. The report discusses late injections as deviations but does not say whether every such patient was a primary failure, whether month6 inflammation was used despite injection, or whether the SAP injection-time sensitivity definition supplied the primary status.
- **Display precision:** Not applicable to the logical component comparison. Printed90 days and reported four patients per arm are discrete source values, not approximate arithmetic inputs; no numeric discrepancy or revised numerator is asserted.
- **Supported alternatives:** The no-late-injection criterion may have been applied but omitted from the reported definition; the primary endpoint may have used a broader composite; or the injection-time sensitivity rule may have been used for those patients. All remain source-grounded possibilities. Original protocol p.15 did not list the later-injection component, which makes version precedence relevant, but the supplied final protocol expressly includes it and no outcome-definition amendment removing it is supplied.
- **Classification ambiguity:** The cited SAP sensitivity rule is compatible with a distinct sensitivity estimand and does not independently establish a plan-only conflict. The original/final manual difference may reflect a disclosed intervention-window revision; this does not identify which definition generated the report's primary counts.
- **Exact human question:** For the eight patients receiving corticosteroid injections after90 days, did the six-month primary analysis classify them as failures under final protocol §2.5.1, classify them using their month6 inflammation/steroid status, or use the SAP injection-time sensitivity rule; and which complete composite definition generated64/96 and56/98?

## C003 — Prespecified primary-endpoint robustness outputs are not reported

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-003

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original/final SAP vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route B

**Classification rationale:** The conflict compares prospective PLAN specifications with REPORT content or outputs; corroborating plan passages do not create an additional relationship.

**Classification ambiguity:** The SAP calls non-complete-case methods supplementary. Registration uses the independent screen's Route B basis for explicitly promised analyses of the primary endpoint; it does not recast them as a separate primary endpoint.

### Originating checker evidence and complete affected locations

- **Locations and roles:** PLAN [originalSAPp22§3.3.1](../../joi190092supp3_prod.pdf#page=22), PLAN [originalSAPp28§3.5](../../joi190092supp3_prod.pdf#page=28), PLAN [originalSAPp29missing-data continuation](../../joi190092supp3_prod.pdf#page=29), PLAN [finalSAPp62§3.3.1](../../joi190092supp3_prod.pdf#page=62), PLAN [finalSAPp68§3.5](../../joi190092supp3_prod.pdf#page=68), PLAN [finalSAPp69four methods and longitudinal model](../../joi190092supp3_prod.pdf#page=69), PLAN [finalSAPp70§3.5.1](../../joi190092supp3_prod.pdf#page=70), PLAN [finalSAPp81injection-sensitivity amendment](../../joi190092supp3_prod.pdf#page=81); REPORT [mainp4StatisticalAnalyses](../../jama_rathinam_2019_oi_190092.pdf#page=4), REPORT [mainp6injection and sensitivity narrative](../../jama_rathinam_2019_oi_190092.pdf#page=6), REPORT [mainp7Figure2 and multiple-imputation result](../../jama_rathinam_2019_oi_190092.pdf#page=7), REPORT [results supplement contents](../../joi190092supp1_prod.pdf#page=1).
- **Printed comparison:** SAP§3.5 says results from all four methods will be reported: regression multiple imputation; longitudinal GLMM using all available measurements with visit/person/eye-within-person structure; missing outcomes assigned success/failure; and complete cases (primary). SAP§3.3.1 promises the lost-followup treatment effect needed to change the main hypothesis-test result. FinalSAP§3.5.1 additionally prespecifies primary-outcome assessment at injection-time inflammation for corticosteroid injections after90days. Main reports completecase OR1.50/P=.20 and MI OR1.4/P=.27, geographic and adherence sensitivities. It reports8 injection-deviation patients (4perarm) but no injection-time primary-endpoint sensitivity. Neither main nor any results-supplement table contains longitudinal GLMM, success/failure-assignment, lost-followup tipping-point or injection-time primary sensitivity results.
- **Comparison logic:** Match the same first-line six-month patient-success endpoint and randomized contrast. These are explicit promised alternative analyses of the primary endpoint, not unreported model diagnostics or unrelated ancillary endpoints. Complete REPORT scope contains only two of the four stated missing-data methods and lacks the specified primary tipping-point and injection sensitivity results. Missing replication count/covariates within the reported MI alone are not separate findings. Display precision is not applicable to absent prespecified outputs.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.
- **Checker qualifying route (provisional):** Route A, category5.
- **Affected result or extracted value:** Robustness of six-month primary success OR1.50(0.81–2.81),P=.20 under prespecified primary-outcome missingness and corticosteroid-injection analyses.
- **Why context does not resolve it:** RouteAcategory5 covers a planned primary analysis not reported; showing one supplementary imputation analysis does not supply the other explicitly promised primary-endpoint analyses. The disclosed list of other secondary outcomes not reported does not identify these primary-endpoint robustness results.
- **Supported alternatives:** Results may have been reserved for another manuscript or included only in an unsupplied study report. Some analyses may have been amended or not performed; no result direction is inferred. The SAP explicitly calls these supplementary analyses of the primary endpoint; the inclusion screener should distinguish that designation from a separate non-key secondary endpoint.
- **Exact human question:** Where are the prespecified longitudinal, missing-success/failure, lost-followup tipping-point and injection-time primary-success analyses, or what supplied amendment changes their reporting plan?

### Independent-screen registration rationale

Supplementary status is retained. Route B qualifies because the definite commitment to report all four primary-endpoint missing-data analyses and specified tipping-point/injection sensitivities is compared with complete supplied REPORT outputs. The named result is six-month primary success OR 1.50, P=.20. Missing outputs leave their prespecified robustness unavailable; no changed significance, result direction, or unperformed-analysis claim is inferred. Route A category 5 is an alternative broader reading, not required for this registration.

## C004 — Planned rescue primary model and individual confidence intervals are not reported

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-002

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original/final SAP vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route A, category 5

**Classification rationale:** The conflict compares prospective PLAN specifications with REPORT content or outputs; corroborating plan passages do not create an additional relationship.

**Classification ambiguity:** Primary analysis is within Specific Aim 2; the trial-wide secondary outcome designation is a nested hierarchy level, not a claimed status change.

### Originating checker evidence and complete affected locations

- **Locations and roles:** PLAN [originalSAPp21§3.2.3](../../joi190092supp3_prod.pdf#page=21), PLAN [originalSAPp25Aim2](../../joi190092supp3_prod.pdf#page=25), PLAN [finalSAPp61§3.2.3](../../joi190092supp3_prod.pdf#page=61), PLAN [finalSAPp62primary/secondary reporting](../../joi190092supp3_prod.pdf#page=62), PLAN [finalSAPp66Aim2primary probability estimates](../../joi190092supp3_prod.pdf#page=66); REPORT [mainp4StatisticalAnalyses](../../jama_rathinam_2019_oi_190092.pdf#page=4), REPORT [mainp6Table2 switching row and footnoteb](../../jama_rathinam_2019_oi_190092.pdf#page=6), REPORT [mainp7Prespecified12-MonthOutcomes](../../jama_rathinam_2019_oi_190092.pdf#page=7), REPORT [results supplement contents](../../joi190092supp1_prod.pdf#page=1).
- **Printed comparison:** SAP primary rescue logistic regression includes rescue-treatment group and reason for first-drug failure (lack of efficacy versus any other). SAPpp62,66 explicitly promise each rescue success probability with95%CI regardless of test outcome; p66 calls these two estimates primary analyses. Mainp4 says the same primary logistic model was applied at12months; Table2footnoteb specifies treatment fixed/site random for the switching OR, with no failure-reason term. The switching row gives20/29(69%) versus7/20(35%),RD34.2%(6.6–52.6),OR4.17(1.32–13.16),P=.02. These are between-treatment intervals, not either group's success-probabilityCI. Mainp7 gives the same between-group results; results supplement has no individual rescue-success intervals or failure-reason-adjusted rescue result.
- **Comparison logic:** The primary planned rescue predictors include a variable not present in the explicitly reported same-as-first-line model. Individual success-probability uncertainty and its failure-reason breakdown are distinct from the printed between-group OR/RD uncertainty. Complete REPORT scope was inspected, including all16 results-supplement pages; neither planned primary result appears. No confidence interval is inferred from crude aggregate ratios. Display precision is not applicable to this model/output comparison.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.
- **Checker qualifying route (provisional):** Route A, category5.
- **Affected result or extracted value:** Rescue treatment efficacy20/29 versus7/20 and the reported OR4.17/P=.02, plus individual rescue success95%CIs planned as primary estimands.
- **Why context does not resolve it:** RouteAcategory5 applies to a planned primary analysis that is replaced or not reported. The narrative's agreement with Table2 does not identify the planned failure-reason-adjusted analysis or supply either individual probabilityCI.
- **Supported alternatives:** Failure-reason-adjusted results may exist outside the supplied REPORT materials; additional covariates may have been fitted but omitted from the stated model; the manuscript may intentionally present an alternative secondary rescue comparison. Report-vs-plan rescue outcome status is separately reviewed by the outcomes checker and may overlap during inclusion screening.
- **Exact human question:** Was the SAP primary rescue analysis with first-drug failure reason performed, and where are its adjusted results and the two prespecified individual rescue-success95%CIs?

## C005 — Adherence summary inputs do not reproduce the printed Welch P value

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST1-001

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article methods vs REPORT main article Table 2 and narrative

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route B

**Classification rationale:** Both conflicting displayed elements are within the same REPORT source.

**Classification ambiguity:** None; source-grounded alternatives and missing definitions remain below.

### Originating checker evidence and complete affected locations

**Title:** Missed-dose means and standard deviations do not reproduce the printed Welch P value.

**Compared locations and document roles:** REPORT [main article p.4 Statistical Analyses](../../jama_rathinam_2019_oi_190092.pdf#page=4) states missed doses were compared with a Welch t test and significance is two-sided P<.05. REPORT [main article p.6 Table 2, missed-dose row and associated narrative](../../jama_rathinam_2019_oi_190092.pdf#page=6) prints mean (SD) 4.6% (1.0%) for methotrexate versus 4.3% (0.5%) for mycophenolate, P=.87. The patient-level table headings give n=96 and n=98. Table footnote j defines missed/expected doses throughout each patient's enrollment. REPORT [main article p.7 Figure 2](../../jama_rathinam_2019_oi_190092.pdf#page=7) has 90/94 participants in the <20%-missed-dose analysis, supporting a substantial patient population with calculated adherence rather than a two-person summary.

**Printed values:** 4.6 (1.0), 4.3 (0.5), n=96/98, P=.87; the same mean/SD/P appears in p.6 narrative. The label is SD, not standard error.

**Rule and calculation:** For the stated Welch comparison, t=(4.6−4.3)/sqrt(1.0²/96+0.5²/98)=2.634450; Welch–Satterthwaite df=139.060070; two-sided P=.009382747. This is direct reproduction using the source's stated test and table populations, not a normal approximation. Means and SDs are in percentage points; converting all to proportions leaves t unchanged.

**Display precision:** The input intervals are mean M [4.55,4.65], F [4.25,4.35], SD M [.95,1.05], F [.45,.55]; hence mean difference [.20,.40]. The largest admissible standard error at n 96/98 is sqrt(1.05²/96+.55²/98)=.120710852, giving t at least 1.656851868. Welch df is at least min(95,97)=95; the conservative two-sided P upper bound is .100848629. The smallest attainable P is nonnegative, so [0,.100848629] is a deliberately conservative enclosing recomputed interval. Printed P=.87 has rounding interval [.865,.875]. Gap at least .764151371; relative discrepancy at least .764151371/.87=.878334909. These intervals do not overlap and the discrepancy exceeds .05. As a population diagnostic, using the smaller 90/94 measured-adherence counts still gives conservative P≤.111356271. This secondary calculation is not a replacement analysis and does not establish the exact adherence-only n.

**Focus area:** B and C.

**Proposed review domain:** statistical_results.

**Proposed relationship type / all relationships:** S_W / S_W.

**Checker qualifying route (provisional):** Route B. The source supplies a named test and incompatible printed summary inputs/P for the displayed patient populations; the discrepancy affects extraction of adherence variability and between-arm test evidence.

**Affected result or extracted value:** The mean (SD) missed-dose percentages and the P=.87 adherence comparison, which accompany the per-protocol sensitivity of the primary outcome.

**Why context does not resolve it:** Both table and narrative repeat the same mean/SD/P. Neither identifies another adherence-only sample, another scale, or another test that produced P=.87. An SD-versus-standard-error relabeling also does not reproduce this P: treating 1.0 and .5 as standard errors yields t≈.268 and a large-df two-sided diagnostic P≈.788, with a different variability quantity. A reader cannot know which summary or test output to extract.

**Alternatives and missing definitions:** A separately restricted adherence analysis, another statistic labeled SD, a transformation, or a distinct P-value analysis could explain the mismatch, but none is identified in these source locations. Exact adherence-only n and original Welch output are missing. The large-df normal calculation for a possible standard-error alternative is a diagnostic approximation only.

**Exact human question:** What participant counts, summary-dispersion definition, and original test output produced the missed-dose P=.87, and how do those inputs correspond to the printed mean (SD) percentages and table populations?

## C006 — Reported per-protocol adherence cutoff differs from the planned cutoff

**Status:** Pending Human Adjudication

**Finding IDs:** F-XS-001

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN original/final SAP vs REPORT main article

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route B

**Classification rationale:** The conflict compares prospective PLAN specifications with REPORT content or outputs; corroborating plan passages do not create an additional relationship.

**Classification ambiguity:** None; source-grounded alternatives and missing definitions remain below.

### Originating checker evidence and complete affected locations

- **Locations and roles:** PLAN [original SAPp31§4.1](../../joi190092supp3_prod.pdf#page=31), PLAN [finalSAPp71§4.1](../../joi190092supp3_prod.pdf#page=71), PLAN [finalSAPp72§4.2](../../joi190092supp3_prod.pdf#page=72); REPORT [mainp6 sensitivity narrative](../../jama_rathinam_2019_oi_190092.pdf#page=6), REPORT [mainp7Figure2 model4 and footnotee](../../jama_rathinam_2019_oi_190092.pdf#page=7).
- **Printed comparison:** Both SAP versions exclude noncompliance defined as “less than50%” study drug received, plus major deviations. Figure2 labels its n=184 analysis “Per protocol”; its footnote and p6 narrative use patients who missed “less than20%” medication. Results are61/90 versus54/94,OR1.56(0.84–2.96),P=.17.
- **Comparison logic:** <20% missed corresponds to >80% received; it differs from the plan's noncompliance exclusion <50% received. Patients receiving50% through80% are treated differently by the stated thresholds. Major-deviation exclusions are explicit in the plan but not documented for Figure2; this latter absence alone is not treated as an additional discrepancy. The criterion numbers define decisions, not rounded estimates. Even treating50 and80 as rounded copies for a conservative check, intervals[49.5,50.5] and[79.5,80.5] have a29-point gap,29/50=.58>.05.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.
- **Checker qualifying route (provisional):** Route B.
- **Affected result or extracted value:** The primary-success per-protocol sensitivity estimate OR1.56(0.84–2.96),P=.17,n184 and which prespecified analysis population it represents.
- **Why context does not resolve it:** Neither supplied finalSAP nor change history introduces an80% adherence rule; immediate report context confirms the20%-missed criterion. This is a numerical analysis-set criterion, not two names for the same population.
- **Supported alternatives:** A stricter additional sensitivity may have been intended, or an adherence-threshold amendment may be unsupplied. Its reported membership and the originally planned per-protocol membership cannot be reconstructed from aggregate counts.
- **Exact human question:** Which adherence and major-deviation criteria produced Figure2's per-protocol analysis, and how does that population relate to the SAP-defined per-protocol population?

## C007 — Switching-group serious diarrhea percentage does not reconcile

**Status:** Pending Human Adjudication

**Finding IDs:** F-NUM-001

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement eTable 9 count/percentage vs REPORT same-table denominator

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route A, category 3

**Classification rationale:** Both conflicting displayed elements are within the same REPORT source.

**Classification ambiguity:** None; source-grounded alternatives and missing definitions remain below.

### Originating checker evidence and complete affected locations

**Title:** Switching-group serious diarrhea percentage does not reconcile with its column denominator.

**Exact source locations and document roles:** REPORT DOC-002 [joi190092supp1_prod.pdf, physical PDF p. 15, eTable 9](../../joi190092supp1_prod.pdf#page=15), Mycophenolate Mofetil column heading N=20 and Serious Systemic → Diarrhea row 1 (3.4). Same display comparators: Non-Serious Laboratory → Low hemoglobin 1 (5.0), Non-Serious Systemic → Allergic reaction 1 (5.0), and Fever 1 (5.0), all in the same N=20 column. REPORT DOC-002 [physical PDF p. 16, eTable 9 footnote b](../../joi190092supp1_prod.pdf#page=16) attributes drug-related serious events to diarrhea and fatigue but specifies no alternate denominator. The primary compared relationship is within the one REPORT supplement, S_W. Canonical numeric relationship N225.

**Printed inputs:** Mycophenolate Mofetil N=20; serious systemic diarrhea number of patients reporting at least one event 1 (3.4%). The adjacent methotrexate column N=29 shows diarrhea 0 (0.0%) and serious fatigue 1 (3.4%). Counts represent patients, not episodes, under the explicit heading.

**Rule and reproduced calculation:** For the printed column denominator, 100 × 1/20 = 5.0%. With one-decimal display precision the printed 3.4% interval is [3.35%, 3.45%]; the recomputed interval is [5.0%, 5.0%]. Counts and denominator are finite integer participant counts: the feasible integers in their half-unit intervals [0.5, 1.5] and [19.5, 20.5] are exactly 1 and 20, so input rounding does not allow fractional patients. The interval gap is 5.0−3.45=1.55 percentage points and relative discrepancy 1.55/3.4=0.455882 (>0.05). The other three printed one-patient entries in the same column reproduce 5.0%; their one-decimal intervals include the ratio. If a denominator of 29 were used instead, 100 × 1/29=3.448276%, within [3.35%, 3.45%], but 29 is the other treatment column's heading.

**Focus area:** A, counts and denominators. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Checker qualifying route (provisional):** Route A, category 3. The count, denominator and percentage in one display do not reconcile above the display-precision threshold. Category 4 additionally describes the numerical pattern: the patient-percentage calculation that reproduces other same-column rows does not reproduce this row.

**Affected result or extracted value:** The six- to twelve-month serious systemic diarrhea risk among patients switching to mycophenolate mofetil: its printed percentage is 3.4%, while its printed numerator and denominator imply 5.0%. This is a specific safety result; no claim about the primary treatment-effect conclusion is made.

**Why context does not resolve it:** Route A category 3 applies even when a reader could reconstruct an alternative percentage. The display provides both a percentage and a patient-count denominator that could be extracted, and does not identify a row-specific safety denominator. The p. 16 attribution footnote does not change N=20 or place the diarrhea event in the other treatment group.

**Source-grounded alternatives and missing definition:** A row-specific denominator of 29 would reproduce 3.4%, and 29 is visibly printed as the methotrexate column denominator; this calculation is an alternative interpretation, not an inferred production explanation. A different attribution of the event or an unstated diarrhea-specific population would also require source clarification. Other one-patient entries in the N=20 column support the conventional displayed 5.0% calculation, but this review assigns no final correction.

**Exact human question:** For eTable 9 serious systemic diarrhea in the Mycophenolate Mofetil N=20 column, which event count, denominator and percentage should be used, and does this row use a population different from the printed column population?

## C008 — Rescue power table sequence sizes differ from planned availability

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST1-002

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP availability table vs PLAN same-bundle power table

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route B

**Classification rationale:** Both conflicting statements are in original/final versions within the same bound PLAN source.

**Classification ambiguity:** None; source-grounded alternatives and missing definitions remain below.

### Originating checker evidence and complete affected locations

**Title:** Primary rescue power tables reverse the treatment-sequence sample sizes supplied by the preceding availability calculation.

**Compared locations and document roles:** PLAN [original SAP p.25–26](../../joi190092supp3_prod.pdf#page=25), especially [p.26 availability table](../../joi190092supp3_prod.pdf#page=26), versus PLAN [p.27 Power Table for Specific Aim 2](../../joi190092supp3_prod.pdf#page=27). The same pattern occurs in PLAN [final SAP p.66–67](../../joi190092supp3_prod.pdf#page=66), especially [p.67 availability table and power-table header](../../joi190092supp3_prod.pdf#page=67), and PLAN [p.68 power-table rows](../../joi190092supp3_prod.pdf#page=68). These are two versions inside the supplied PLAN bundle; no REPORT result is the other side of the inconsistency.

**Printed values:** Planning assumes 108 initially randomized per arm, retention .9, initial Drug A success 60% and Drug B success 40%, rescue retention .95. The availability table labels B/A expected enrollment 58.3/complete 55.4, and A/B expected enrollment 38.9/complete 36.9. Its narrative sets n1=58 and n0=38. The next power table labels its first column 'Drug A, then Drug B (number)' and its second 'Drug B, then Drug A (number)'; the main scenario instead prints 58 and 38 in those respective columns. The remaining scenarios change these numbers deliberately for sensitivity; they inherit the same column-to-sequence definitions.

**Rule and calculation:** Enrollment after B fails, followed by A, is 108*.9*(1−.4)=58.32; enrollment after A fails, followed by B, is 108*.9*(1−.6)=38.88. Applying rescue retention .95 gives 55.404 and 36.936, respectively. These reproduce the availability table, but the next table assigns the main-scenario 58 to A→B and 38 to B→A. This is a sequence-to-sample-size conflict, not the distinction between enrollment and completion; both power counts are described as enrolling.

**Display precision:** For the two printed copies assigned to A→B, availability 38.9 rounds to [38.85,38.95] and power-table 58 to [57.5,58.5]; gap 18.55, relative discrepancy 18.55/38.9=.476863753. For B→A, availability 58.3 rounds to [58.25,58.35] and power-table 38 to [37.5,38.5]; gap 19.75, relative discrepancy 19.75/58.3=.338765009. The explicit rounding-down step from 58.3 to 58 and 38.9 to 38 reconciles within each correctly assigned sequence; it cannot exchange their sequence labels. The formula arithmetic reproduces the enrollment table and is not a competing preferred method.

**Focus area:** C and D.

**Proposed review domain:** plan_material.

**Proposed relationship type / all relationships:** P_P / P_P.

**Checker qualifying route (provisional):** Route B. The conflict concerns the expected primary Aim 2 analysis populations and their power inputs, rather than a peripheral plan table label.

**Affected result or extracted value:** The planned numbers available in each primary rescue sequence and the treatment-specific success/sample-size pairing underlying the 87%/80% rescue power scenarios.

**Why context does not resolve it:** The immediately preceding calculation, its sample coding, the next table's treatment-order headings, and the drug-specific p0/p1 definitions cannot all retain their printed assignment. Generic A/B could in principle be recoded between displays, but no such recoding is stated. A reader selecting power inputs by the printed column headings obtains the opposite sequence sizes. The power formula is symmetric to swapping entire treatment distributions, but not to exchanging only n while retaining each p; therefore the mapping is consequential.

**Alternatives and missing definitions:** The power table may have used a new unstated A/B mapping, or the sequence headings/sample columns may refer to different coding than the availability calculation. The source gives no transition dictionary. Different response assumptions in the table are expressly described as sensitivity scenarios, but do not explain reversing the main scenario's allocation.

**Exact human question:** Which initial→rescue sequence corresponds to 58 versus 38 patients in the main Aim 2 power scenario, and how were the table's A/B labels matched to n0/n1 and p0/p1?

## C009 — Printed detectable rescue difference does not reconcile with probability inputs

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST1-003

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP detectable-difference prose vs PLAN same-bundle formula, probability table and summary

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route A, category 2

**Classification rationale:** Both conflicting statements are in original/final versions within the same bound PLAN source.

**Classification ambiguity:** None; source-grounded alternatives and missing definitions remain below.

### Originating checker evidence and complete affected locations

**Title:** The stated 17-percentage-point detectable rescue difference does not reconcile with the stated formula and 80%-power scenario.

**Compared locations and document roles:** PLAN [original SAP p.26 rescue power formula](../../joi190092supp3_prod.pdf#page=26) and [p.27 opening sentence, table and summary](../../joi190092supp3_prod.pdf#page=27); the repeated final version is PLAN [SAP p.67 formula and sentence](../../joi190092supp3_prod.pdf#page=67) and [p.68 table and summary](../../joi190092supp3_prod.pdf#page=68).

**Printed values:** With n1=58,n0=38, MMF rescue probability .42, the text states approximately 80% power to detect a 'difference of 17%'. The 80%-power table row instead prints rescue probabilities .42 and .17. The following summary describes approximately 80% power for a25% difference with success probability 42% and two-tailed alpha .05.

**Rule and calculation:** A difference between success probabilities .42 and .17 is.25, not .17. The explicitly printed normal-CDF power formula Phi(abs(p1−p0)/sqrt[p0(1−p0)/n0+p1(1−p1)/n1]−z(alpha/2)) gives .802453213 for .42/.17 and n58/38. A literal .17 difference from .42 implies the comparator .25, and the same printed formula gives .428097408. The numerical integration/CDF evaluation implements the source's approximation; it is not a preferred replacement power method.

**Display precision:** Inputs.42 and .17 permit probabilities[.415,.425] and[.165,.175], so their recomputed difference lies[.240,.260]. The printed 17% difference has interval[.165,.175]. Gap.065; relative discrepancy .065/.17=.382352941. The printed 25% summary has interval[.245,.255], which overlaps the recomputed interval. A literal 17-point effect is also incompatible with the source's80% output under its printed formula, well beyond display precision. The table's approximate 80% itself reconciles with the .802453 calculation.

**Focus area:** C and D.

**Proposed review domain:** plan_material.

**Proposed relationship type / all relationships:** P_P / P_P.

**Checker qualifying route (provisional):** Route A, category 2. The printed 17% absolute-effect value changes the magnitude of the detectable primary rescue difference relative to the 25% difference supplied by its probability inputs and summary. Reconstructing the companion value does not remove the printed quantitative reading. No production mechanism for the discrepancy is inferred.

**Affected result or extracted value:** The planned primary rescue detectable absolute effect and corresponding expected 80% power, which may be extracted as 17 or 25 percentage points.

**Why context does not resolve it:** The nearby row and summary permit reconstruction of a25-point contrast, but the prose explicitly calls 17% a difference. A reader can extract that smaller detectable effect as printed. The formula quantifies that the two readings represent materially different power rather than interchangeable terminology.

**Alternatives and missing definitions:** The sentence may use 17% to name the second-arm success probability rather than the between-arm difference, or it may reference a separate unstated scenario. The source supplies no alternative sample size/probability calculation producing 80% power for a17-point difference.

**Exact human question:** Does 17% name a rescue success probability or an absolute between-arm difference, and which effect size/formula scenario supports the stated 80% primary rescue power?


## C010 — Final primary safety-failure laboratory cutoffs differ at exact boundaries

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST2-101

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol vs REPORT main article and results supplement

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective final PLAN and repeated REPORT definitions give different exact-boundary membership for the laboratory safety-failure component of the primary composite. Agreeing REPORT locations corroborate one side; historical PLAN versions provide context without adding a second relationship.

**Classification ambiguity:** The implemented inclusive/exclusive rule and any unsupplied amendment are unavailable; no participant-level classification or count change is inferred.

### Originating checker evidence and complete affected locations


**Title:** Final primary safety-failure laboratory cutoffs differ from the repeated report definitions at exact boundaries.

**Compared locations and document roles:** PLAN DOC-003 [final protocol physical p.80, §2.5.1 treatment-success composite](../../joi190092supp2_prod.pdf#page=80), [p.81, §2.5.2 safety failure and Table 3 laboratory thresholds](../../joi190092supp2_prod.pdf#page=81), and [p.136, immediate laboratory serious-event failure](../../joi190092supp2_prod.pdf#page=136); REPORT DOC-001 [main physical p.3, success/failure definition](../../jama_rathinam_2019_oi_190092.pdf#page=3), [p.6, Table 2 safety-failure counts and footnote f](../../jama_rathinam_2019_oi_190092.pdf#page=6), [p.7, all five drug-related serious events are elevated liver-function tests](../../jama_rathinam_2019_oi_190092.pdf#page=7), and [p.8, Table 3 laboratory rows and definition pointer](../../jama_rathinam_2019_oi_190092.pdf#page=8); REPORT DOC-002 [results supplement physical p.5, eTable 1 laboratory-event definitions](../../joi190092supp1_prod.pdf#page=5). PLAN [revision p.148](../../joi190092supp2_prod.pdf#page=148) discloses an earlier laboratory-threshold revision, but the supplied final p.81 definition still has the boundaries cited here.

**Printed values and statements:** Final protocol p.80 requires no prior safety failure for primary treatment success. Final p.81 classifies AST/ALT 2 to <5 times the upper limit of normal (ULN) as nonserious, and ≥5 times ULN as serious. It separately makes persistent nonserious abnormalities at 28 days serious and declares treatment failure immediately. Protocol p.136 states that a laboratory serious event stops medication and declares treatment failure; these patients do not switch to Phase II. The same p.81 table makes leukocytes ≤1,000/µL serious and >1,000 to <2,500/µL nonserious.

Main p.3 defines safety failure through a laboratory result meeting the serious-event threshold, and Table 2 p.6 attributes primary safety failure to that rule, with 3/32 failures in the methotrexate group and 2/42 in the mycophenolate group. Main p.7 identifies all five drug-related serious events as elevated liver-function tests. Main Table 3 p.8 and results eTable 1 p.5 instead define immediate serious AST/ALT as >5 times ULN, and 2 to 5 times ULN as serious only if persistent for at least 28 days. The report supplement's immediate serious leukocyte cutoff is <1,000/µL, while its nonserious row begins >1,000/µL; the prolonged-abnormality alternative is <2,500/µL for at least 28 days.

**Rule and reproduced logical calculation:** Compare the complete primary safety-failure decision rule at the printed boundary without assuming any participant had that value. For AST/ALT exactly 5×ULN persisting fewer than 28 days, the final PLAN's ≥5 branch is immediately serious and hence treatment failure. The repeated REPORT's >5 branch does not include that value; its 2-to-5 branch requires persistence for ≥28 days before becoming serious. For leukocytes exactly 1,000/µL, the final PLAN's ≤1,000 immediate-serious branch includes that value, whereas the REPORT's <1,000 branch does not; its >1,000 nonserious branch also leaves the exact boundary unnamed before the prolonged-abnormality criterion. The issue is the classification rule supplying the no-safety-failure primary composite component, not an event-count calculation or a claim that any observed patient changes status.

**Display precision:** Not applicable to these exact decision-rule inequalities. The cutoff numerals are identical; the reproduced difference is the membership of the cutoff in an immediate serious/failure branch. No relative numerical discrepancy between two estimates is asserted. Rounding measured laboratory observations into boundary values is not assumed.

**Focus area:** D, planned versus reported primary endpoint threshold/component; C, the linkage between event definitions and primary safety failure.

**Proposed review domain:** `protocol_report`.

**Proposed relationship type:** `P_R`. **All relationships:** `P_R`. The two REPORT sources agree on >5 and corroborate the report definition; they do not form a separate REPORT conflict. The original/final historical revision is not a separately asserted PLAN-only conflict.

**Checker qualifying route (provisional):** Route A, category 5.

**Affected result or extracted value:** The complete six-month primary treatment-success/failure definition underlying 64/96 versus 56/98 and the reported 3 versus 2 primary safety failures; the immediate-versus-persistent classification of a laboratory result exactly at the printed boundary.

**Why context does not resolve it:** Route A category 5 applies to a planned primary composite/threshold definition differing in the report. This is distinguished from an isolated evidently resolvable symbol slip: the final protocol's adjoining 2-to-<5 and ≥5 categories partition the boundary coherently, while two report displays repeatedly use 2-to-5 and >5 with the separate 28-day condition. Neither report location says its >5 notation should be read as ≥5. The primary safety-failure link is explicit rather than inferred from a generic safety definition. The possible effect on actual participants is unknown and is not needed to reproduce the two printed rules.

**Source-grounded alternatives and missing definitions:** The report inequalities may abbreviate an implemented inclusive boundary; a different safety-threshold version may have been used; or the final protocol rule may have been applied while the report used another description. No supplied amendment identifies that transition. The actual laboratory values, their duration, the implemented classification algorithm and which of the five liver-function events crossed an exact boundary are not supplied. The review cannot recalculate primary success or safety-failure counts and does not claim any changed significance or direction.

**Direct observation versus inferred explanation:** Direct: final PLAN and repeated REPORT definitions include different exact-boundary observations in immediate serious laboratory failure, and both explicitly connect serious laboratory events to primary safety failure. No production mechanism, actual classification discrepancy, or changed participant outcome is inferred.

**Exact human question:** Which inclusive/exclusive AST/ALT and leukocyte boundary rules generated the primary safety-failure classifications: the supplied final protocol's ≥5×ULN/≤1,000 thresholds, the report's >5×ULN/<1,000 thresholds with the persistence alternative, or another documented rule; and did any primary safety classification depend on an exact-boundary observation?

This source-linked checker finding was independently included by the fresh pass-2 screener and registered as C010; the appended mechanical recheck assigns its evidence state.


