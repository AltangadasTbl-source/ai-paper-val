# Statistical consistency pass 1 — main A and PLAN

Runtime agent: /root/statistics_1_main_a; newly spawned qc161_statistical_consistency_reviewer, gpt-6.1-sol/high. Scope: S001–S094 plus S400–S417 (112 relationships). Each has an explicit PASS_1_COMPLETE row in statistics/parts/statistical_main_a.md. This is pass 1 only; a different fresh runtime agent must perform pass 2.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6_1/review_contract.md, PERFORMANCE_PROFILE.md, workflow_1_6_1/report_spec.md, settings.toml, tooling/source inventories and current main/support maps. Supplied source text and exact pages govern; prior candidate/review/report conclusions and external evidence were not used. Tooling: direct Poppler pdftotext25.03.0 selected-page source reads; reused native/layout and rendered source pages. Source render DOC-001 p.6 and p.9 confirmed table/figure quantities and captions; mapper's new protocolp14 render confirmed the contact timeline. No derivative files were created, no Python scientific orchestration, no GPU.

## Completed inferential checks

112 assigned relationships: 94 main model/design/result keys plus18 PLAN families SUP-P01–P18 (S400–S417). All main Table1 differences (27), Table2 process/time tuples (21), Table3 cluster-only and hospital/time tuples (20), Figure3 subgroup tuples (14), primary/secondary/post hoc narrative matches and eight model/design keys received source-grounded checks. Methods were checked against hospital-cluster randomization, stepped-wedge time structure, population eligibility, missingness language, explicit primary/secondary definitions, planned models/covariates, sample-size inputs, interim thresholds and exploratory multiplicity statements. Every estimate is contained in its ordered interval. Matched RD/OR directions agree. The primary null-spanning intervals agree with no demonstrated primary decrease. No NI/equivalence margin or conclusion is reported. No interim statistic or numerical stopping decision is supplied.

Absent test statistic, standard error, degrees of freedom, interval construction, variance estimator, or interaction parameter definitions were not filled by convention. Only diagnostic approximations are used where named below. The point/CI/P compatibility for the troponin statement cannot be determined as the same test from the package. The exact primary regression contributor count and outcome coding for295 incomplete outcomes are also not established; ITT accounting was not equated to complete binary outcomes. Precise missing definitions are retained in the inventory.

## Self-screened findings

### F-ST1-001

**Candidate statement:** Table2 reports two adjusted time contrasts for each of door-to-balloon and door-to-needle time, but does not identify the separate analyses or estimands that produced the difference and beta-coefficient columns.

**Relationships:** S046 and S048; N078 and N080. One repeated time-outcome mapping pattern.

**Exact source locations and document roles:** REPORT [main article physical p.6, printedp572, Table2, door-to-balloon and door-to-needle rows, both effect columns, title and footnotesb/c](../../../../jama_huffman_2018_oi_170166.pdf#page=6). REPORT [main article physicalp3, printedp569, Statistical Analysis](../../../../jama_huffman_2018_oi_170166.pdf#page=3) supplies the general cluster/time model description but no separate time-outcome contrast specification.

**Printed values and statements:** Table2's title states adjustment for within-hospital clustering and temporal trends. Door-to-balloon median times: control65(53–105)min, n4022; intervention77(55–118)min, n3639. The difference column prints6.18(95%CI−4.78 to17.14); the beta column prints13.00(3.64–22.36). Door-to-needle: control44(30–67)min,n1455; intervention45(27–75)min,n1433; difference0.40(−5.23 to6.03); beta5.00(−5.20–15.20). Footnotec identifies beta-coefficients. Footnoteb attaches the same intervention/control and marginal-effects description to both columns and names mixed-effects logistic or quantile regression including within-hospital clustering and temporal trends. The displayed difference header is percent, while the row descriptors are minutes.

**Rule and calculation:** A method description must identify what analysis and quantity a reported effect represents when distinct outputs have different inferential readings. This is a mapping observation; no equality between a conditional coefficient and a marginal contrast is assumed. The balloon point contrasts differ by13.00−6.18=6.82. Two-decimal display intervals[6.175,6.185] and[12.995,13.005] are disjoint. The needle contrasts differ by5.00−0.40=4.60, with disjoint point display intervals[.395,.405] and[4.995,5.005]. The balloon difference95%CI spans0; the beta95%CI has lower3.64>0. Display precision cannot supply their estimand mapping. Each estimate is inside its own CI, and no P value/test statistic is inferred. The percent header alone is screened out as notation, because minute outcome rows establish their measurement unit; the independent concern is the unidentified distinct contrasts and their different null-inclusion reading.

**Focus area:** C (statistical method logic; analysis description does not identify which analysis produced each time-effect number).
**Proposed review domain:** statistical_results.
**Proposed relationship type:** S_W.
**Compared document roles:** REPORT main Table2 values and method labels versus REPORT main Statistical Analysis.

**Affected result or extracted value:** The adjusted intervention effect on door-to-balloon and door-to-needle time, especially extraction of balloon6.18(−4.78,17.14) versus13.00(3.64,22.36), which give different conclusions about exclusion of zero at the printed95% confidence level.

**Why context does not resolve it:** The distinct column labels show that two outputs are presented, but the common adjustment title/footnote does not define whether they differ by model, quantile, conditional/marginal target, outcome transformation, standardization or contrast population. Immediate context supplies no formula or separate model mapping for the two quantities. A reader can identify time in minutes, yet cannot identify which adjusted time effect applies to a specified analysis.

**Source-grounded alternatives and missing definitions:** A marginal time contrast and a conditional quantile-regression coefficient could be intentionally distinct; different time models or transformations could also yield different outputs. These are possible interpretations, not asserted methods. Needed definitions are each column's model/estimand, quantile or outcome scale, standardization/reference population, units, and interval construction. No preferred analysis is proposed.

**Exact human question:** Which models, estimands, units and reference populations produced the difference and beta-coefficient columns for the two time outcomes in Table2, and which adjusted door-to-balloon result should a reader extract for each specified analysis?

Self-screen: directly source-confirmed; in focusC; immediate context does not map the distinct analyses; the specific time-effect estimate and interval extracted can change. Both rows are consolidated.

### F-ST1-002

**Candidate statement:** The age subgroup boundaries used for the primary30-day MACE result differ from those in the supplied SAP, while the report calls the Figure3 groups prespecified.

**Relationships:** S006,S077,S078,S079,S410 (SUP-P11). One age-subgroup specification pattern.

**Exact source locations and document roles:** PLAN [SAP physicalp7, section7.5.2, lines1243–1254, especiallyline1251](../../../../joi170166supp2_prod.pdf#page=7). REPORT [main physicalp3, Statistical Analysis subgroup description](../../../../jama_huffman_2018_oi_170166.pdf#page=3). REPORT [main physicalp9, Figure3 title/age rows and first Results paragraph](../../../../jama_huffman_2018_oi_170166.pdf#page=9). REPORT [main physicalp2, Methods Study Design](../../../../jama_huffman_2018_oi_170166.pdf#page=2) states analysis according to the supplied SAP and is contextual, not a separate conflicting relationship.

**Printed values and statements:** SAP7.5.2 calls its analyses a priori and specifies age(<65years and>65years). Main methods call age subgroups prespecified; Figure3 title also calls its groups prespecified. Figure3 instead uses<50,50–69,≥70years. Their adjusted MACE ORs are respectively1.53(.83–2.79),.89(.67–1.19),.98(.71–1.35), and RDs1.42%(−.71,3.54),−.57%(−2.02,.88),−.23%(−3.32,2.85). The intervention/control event-denominator pairs are58/2079 versus68/2045;297/6606 versus326/5863;247/2623 versus251/2158.

**Rule and calculation:** A planned-versus-reported primary endpoint subgroup specification must be matched by boundaries, not merely by variable name. The SAP two-way age partition at65 differs from the reported three-way partition at50 and70. Ages50–64 and65–69 lie in the same reported middle group but on different sides of the planned65 boundary; ages below50 and50–64 are separated in the report but together in the plan. This remains irrespective of how age65 itself is assigned in the SAP's abbreviated bounds. Report denominators2079+6606+2623=11308 and2045+5863+2158=10066 account for both arms; events58+297+247=602 and68+326+251=645 account for primary MACE totals. Thus this is a different age analysis of the same primary endpoint/population, not a count discrepancy or display rounding. Adjusted age65 effects cannot be reconstructed by averaging the three displayed adjusted ORs/RDs.

**Focus area:** D (planned-versus-reported statistical analysis, primary endpoint subgroup).
**Proposed review domain:** protocol_report.
**Proposed relationship type:** P_R.
**All relationships:** P_R.
**Compared document roles:** PLAN SAP subgroup boundaries versus REPORT main Figure3/Methods subgroup specification.

**Affected result or extracted value:** The primary30-day MACE age-specific effect estimates and their interpretation as prespecified analyses; the package does not report the planned<65/>65 effect estimates in Figure3.

**Why context does not resolve it:** Neither the reported figure nor adjacent methods/results identifies a revised age specification or explains replacement of the planned65 boundary. This is not a synonym or omitted comparison symbol: the participant partitions differ materially and cannot be mapped one-to-one. A reader cannot establish whether the displayed estimates correspond to a disclosed amendment, a different prespecified plan, or a subsequently chosen grouping.

**Source-grounded alternatives and missing definitions:** The supplied SAP may have been superseded by an amendment not supplied; the65-year analysis may have been performed separately; or Figure3 may use additional age groups while “prespecified” refers more generally to the age variable. The package does not establish which explanation applies. The absent item is a source-defined link between the planned and displayed age subgroup specifications, not a recommendation for alternate cutoffs.

**Exact human question:** What supplied prespecification or disclosed amendment defines the<50,50–69 and≥70year MACE groups in Figure3, and how do those results relate to the SAP's planned<65/>65year subgroup analysis?

Self-screen: source-confirmed beyond display precision; in focusD because the primary endpoint analysis is compared; immediate context does not explain the changed analysis; primary subgroup extraction and prespecified-status interpretation can change. No judgment on the choice of age groups is assigned.

## Excluded observations

Each pattern is listed once with exactly one scope reason code. Concordant relationships without an apparent discrepancy are completion records, not exclusion observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 Table2p6, Table3p7, Figure3p9 | Several adjusted RDs/ORs differ from crude percentages/ratios, including direction reversals. Hospital/time models are expressly reported, so crude recomputation does not test the adjusted estimand. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 Tables1–3/Figure3 and p6 troponin; REPORT DOC-004p17 eTable1; DOC-004p22 eTable6 | Exact CI/test/P compatibility and interaction interpretation require absent definitions. For troponin, median difference3.3(.1,6.5) versus mainP<.001: a diagnostic normal-Wald approximation gives SE(6.5−.1)/3.92≈1.633,z≈2.02,P≈.043, but no source identifies that as the printed test or CI construction. Interaction coefficient/time reference likewise absent; no contradictory test is asserted. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 Table1p5 creatinine, all displayed means/medians/proportions, Table3p7/null-adjacent ORs, p3interim rules; PLAN SAPp8 | Rounded baseline differences,0.0(0.0,0.0),OR upper1.00 and numerical z/P boundary displays do not establish inconsistencies. Standard-normal-tail diagnostics forz2.797 and1.977 give approximately.00516 and.0480 and agree at displayed precision; no stopping result is supplied. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001p6 Table2footnoteb andp7 Table3footnotea | Footnote wording attributes “difference in marginal effects” to ORs, but neighboring separate difference and OR columns, scales and narrative identify the intended binary quantities immediately; no evidence that an OR was computed as a difference. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001p6 Table2time rows/header | Percentage header on minute time rows alone is immediately resolved by minute row descriptors and beta labels. The independent model/estimand mapping concern is F-ST1-001. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001p6in-hospitalbeta narrative/Table2 | Narrative upperCI8.10 versus Table2upper8.40 forRD6.25,lower4.10 is a single-character slip whose intended table value is evident; both intervals have the same direction and null-exclusion interpretation. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001p7dischargebeta narrative versusp6Table2 | Narrative RD6.63/OR1.47 versus table6.69/1.48 with identical printed CIs concerns an individual secondary process measure, not the primary result, analysis-population size or decision rule; no key-secondary status for that individual measure is established. | PERIPHERAL_COMPARISON |
| REPORT DOC-001p3sample size; PLAN DOC-002p18, DOC-003p4 | Exact80% stepped-wedge power cannot be reproduced from onlyN/ICC/risk/effect/alpha without cluster-period sizes/allocation and calculation implementation. No default balance/covariance or alternative power formula is inferred. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002p18,DOC-003p4; REPORT DOC-001p3 | Sample increase15000→15750 equals addition5%; division by.95 instead gives15789.47, while15750×.95=14962.5. Immediate context resolves conventional approximate5% inflation, with no distinct retained-count claim or decision discrepancy. | CONTEXT_RESOLVES |
| PLAN DOC-003p4section5 versusp3design/diagram | “Each of the four time periods” conflicts lexically with five cohorts, but its immediate design/diagram specifies the five crossovers at months4,8,12,16,20; intended schedule is clear. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001p4flowcaption,p6missingness,p7primaryimputation; PLAN DOC-003p6 | Lost participants remain in analysis accounting;295 have incomplete follow-up; primary imputation/coding and model contributor count are not stated. These facts do not establish that all295 were missing all binary outcome information or that ITT total equals regression n. No missing=no-event or complete-case assumption is used. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002pp11,13,14timeline; REPORT DOC-001p3outcomes | Plan's discharge+30day contact date versus report's30day outcome wording lacks a source-defined competing admission-origin cutoff. Contact timing is not automatically an outcome window; no planned-versus-reported endpoint change is established. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003p5; REPORT DOC-001p3,Table3p7 | Inpatient statin is planned but explicitly disclosed as not collected in main methods. Heparin versus anticoagulant label alone is immediately understood here without a source-established changed composite population. | CONTEXT_RESOLVES |
| PLAN DOC-003pp5,7–8; REPORT DOC-001p3process/subgroups | Toolkit-use subgroup/substudies are not displayed as main numeric results and process evaluation is expressly to be reported separately; report hospital-type subgroup does not establish absence of another prespecification. No missing-result or unreported-amendment hypothesis is registered. | CONDITIONAL_OR_UNREPORTED |

## Handoff

Pass1 complete. Exact scope112 relationships: S001–S094,S400–S417. Findings2: F-ST1-001,F-ST1-002. Excluded observations14. Assigned scientific gaps0. Missing exact test/CI construction, time-effect model/estimand mapping, contributor counts/missing-outcome coding, cluster-period power inputs and interaction reference definitions are recorded with source-grounded limitations. Candidate assignment, independent inclusion screen, evidence-state assignment and human adjudication belong to later stages. No severity, disposition or correction is assigned.

Artifacts: statistics/parts/statistical_main_a.md; checkers/parts/statistical_main_a.md. All evidence links in these part artifacts use four-level parent traversal; the coordinator must rewrite to three levels when merging into canonical statistics/relationship_inventory.md or checkers/statistical_pass_1.md.

