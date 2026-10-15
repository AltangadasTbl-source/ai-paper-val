# Cross-source and planned-versus-reported consistency review

Fresh specialist: /root/cross_checker; qc162_cross_source_consistency_reviewer; gpt-6.1-sol / medium. Sources: DOC-001 REPORT, PDF pages 1–12; DOC-002 REPORT, PDF pages 1–20; DOC-003 PLAN, PDF pages 1–7, including original January 6, 2019 protocol and August 2, 2019 amendment. This is a retrospective matched-cohort study by content. No external source or earlier scientific conclusion was used. Complete scope and contract, both current mapper artifacts, source inventory, coverage and tooling were read. Findings below are independently screened observations, with no candidate IDs or adjudications.

## Evidence method and scope closure

Direct source native/layout text was freshly extracted with Poppler pdftotext 26.01.0 on CPU into `preprocessing/cross-main-layout.txt`, `preprocessing/cross-support-layout.txt`, and `preprocessing/cross-plan-layout.txt`. These derivatives cover all 39 supplied PDF pages and supplement source-linked current maps. Direct Poppler pdftoppm 26.01.0 CPU renders `preprocessing/cross-plan-p003.png` and `preprocessing/cross-plan-p004.png` visually confirm the matching statement and original endpoint code lists; the support mapper's exact DOC-002 p2 render visually confirms the AF code and bold primary-diagnosis convention. Text is a locator and transcription aid; linked supplied PDF pages are authority. No fresh OCR or fallback environment was used. References and administrative content were inspected as no-applicable quantitative units. No structured-data file exists.

| Matched scope | Locations and completed comparison | Outcome |
|---|---|---|
| Cohort and primary abstract/Key Points results | DOC-001 pp1–4, Figure1 p3, Table1 pp5–6, Table2/Figure2 p7; total13722, surgery2287, controls11435, primary385/3243, 8-year30.8/47.7, ARD16.9, HR.61(.55–.69), P<.001 | Printed copies match after population/time/model matching; rounded Discussion31/48 matches display precision |
| Mortality abstract and narrative | DOC-001 pp1,4,7–9; DOC-002 pp6–7,9; deaths112/1111, risks10.0/17.8, ARD7.8, HR.59(.48–.72), P<.001 | Copies match; event counts through study end are distinct from modeled 8-year risk |
| Other seven endpoint tuples | DOC-001 Table2 p7, Figure2 p7/Figure3 p8 and narrative pp4,6,9; DOC-002 eTables4–7 pp6–10 and repeated eTable7 p19 | All eight HR/CI/P tuples and group-specific 8-year risk/CI copies match; cause-specific rates and time-varying HRs are distinct quantities, not discordant copies |
| Figure risk sets and outcome populations | DOC-001 Figures2–3 pp7–8 versus Table2 p7 and baseline history pp5–6; original PLAN pp4–5 | Baseline denominators match; composite includes all2287/11435 and omits prior individual conditions from qualifying incident components; individual outcomes remove prior cases, nephropathy has extra PLAN exclusions |
| Primary subgroup results | DOC-001 p4 and DOC-002 eFigure1 p8; all16 subgroup HR/CI and eight interaction P values | Direction and no-heterogeneity statement agree; primary subgroup analyses are not claimed as prespecified |
| Longitudinal and prescriptions | DOC-001 pp3–4,7,9–10, Figures4–5; DOC-002 pp11–14,16 | Match units, group contrast, change versus level, time, and test; excluded details below; raw observation counts and smoothed-model estimates are distinct |
| Surgical adverse events | DOC-001 p7; DOC-002 eTable2 pp3–4, eTable11 p15, eFigure3 p16; amendment DOC-003 p7 | Early90-day findings and later cumulative intervention rates refer to different windows; nutritional and adverse-event additions are disclosed by amendment |
| Sensitivity analyses | DOC-001 pp4,8–9; DOC-002 pp17–20; DOC-003 pp3,6–7 | Five date draws × three ratios produce15 cohorts; all eight endpoints covered; 2/5/8-year time-varying tuples identical on supplement pp10/19; E-values added explicitly by amendment and all eight estimate/closest-null pairs reported |
| Primary and secondary hierarchy and composite components | DOC-001 pp1–3,11; DOC-002 p2; original PLAN pp4–5, amendment p7 | Six-component primary, death/MI/ischemic-stroke secondary, and six individual secondary outcomes match by status; operational phenotype criteria differ as findings below |
| Matching and primary model | REPORT DOC-001 pp3–4/Table2 p7; PLAN DOC-003 pp3,5–6 | Seven matching factors match item by item; matching orientation differs below; Cox, weighted-residual PH tests and five-dataset MICE/Rubin pooling agree; no claim that subgroup analyses were prespecified |
| Eligibility, analysis-set and success criteria | REPORT DOC-001 pp2–3; PLAN DOC-003 pp2–5 | Surgery procedure/chart confirmation, age18–80, BMI≥30, diabetes, liver/heart/lung transplant, severeHF EF<20%, ED≤5days, cancer/GI window, perioperativeGI/ulcer, first qualifying surgery date inspected individually. Comparator surgical removal, random date, prior T2DM, follow-up, death≤30days, age/BMI, transplant/ED/cancer/EF inspected individually. Composite component-history omission and individual risk sets inspected individually; apparent reporting omissions below |
| Missing data, hypothesis and multiplicity | REPORT DOC-001 p4; PLAN DOC-003 p6 | Per-outcome five imputations, numeric predictive mean matching, binary logistic, categorical polytomous logistic, Rubin pooling agree; .05 significance/95%CI and exploratory secondary treatment agree for vascular endpoints. No superiority/noninferiority margin, sample-size/power target, interim or stopping rule appears in supplied PLAN; these are not randomized-trial requirements for this observational cohort |
| Exposure definition and plan dependencies | REPORT DOC-001 pp1–4; PLAN DOC-003 pp2–3,6–7 | Surgery codes and first-surgery index definition agree; no randomized dose/duration exists; original matching orientation versus sensitivity 1:5 convention retained in finding; amendment adds safety/E-value rather than replacing cardiovascular hierarchy |

## Findings

### F-XS-001

**Title:** The original matching statement reverses the surgical-to-nonsurgical allocation stated in the report.

**Compared locations and document roles:** [PLAN original protocol p3, Matching Process](../../../joi190103supp2_prod.pdf#page=3); [PLAN original protocol p6, Sensitivity analyses](../../../joi190103supp2_prod.pdf#page=6); [REPORT main abstract p1](../../../jama_aminian_2019_oi_190103.pdf#page=1); [REPORT main Figure1 and matching caption p3](../../../jama_aminian_2019_oi_190103.pdf#page=3); [REPORT main statistical analysis p4](../../../jama_aminian_2019_oi_190103.pdf#page=4). Amendment [PLAN p7](../../../joi190103supp2_prod.pdf#page=7) adds safety/E-values and supplies no revised matching statement.

**Printed statements:** Original PLAN p3: “Each non-surgical patient will be matched ... to five (5) surgical patients.” REPORT p3: “each surgical patient was matched ... to 5 nonsurgical patients”; REPORT p4 repeats that direction. Reported populations are 2287 surgical and11435 matched nonsurgical patients. PLAN p6 says one reported dataset uses1:5 matching, without defining group direction in that sentence.

**Comparison logic:** Hold the exposure groups and primary matched analysis fixed. Five surgical per nonsurgical implies surgical:nonsurgical5:1; five nonsurgical per surgical implies1:5. Report count ratio11435/2287=5 agrees with the second statement. This is a categorical matching-specification comparison, not an estimate compared with a crude ratio; interval rounding cannot turn one orientation into the other. The p6 sensitivity convention suggests the reported orientation but does not revise the explicit p3 rule.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route B.

**Affected result or extracted value:** The matched population underlying the primary composite adjusted HR0.61(95%CI0.55–0.69) and its interpretation as a one-surgical-to-five-control analysis.

**Why context does not resolve it:** The report establishes the performed ratio; the supplied original plan explicitly describes its inverse. Knowing the performed ratio does not establish whether the planned primary matching allocation was reversed in wording or changed in implementation. The difference changes an analysis-population design element rather than names for equivalent groups.

**Supported alternatives:** The p3 group orientation may have been transposed when the plan was written; alternatively the final matching allocation may differ from that explicit rule. PLAN p6's1:5 wording is compatible with the report but does not independently specify direction.

**Human question:** Which surgical:nonsurgical matching allocation was intended for the primary analysis in the January6 protocol, and how should its p3 statement be reconciled with the reported2287:11435 matched cohort?

### F-XS-002

**Title:** The reported atrial-fibrillation code set adds a code absent from the original primary-component definition.

**Compared locations and document roles:** [PLAN original protocol p4, Atrial fibrillation and primary endpoint](../../../joi190103supp2_prod.pdf#page=4); [REPORT non-plan supplement p2, eTable1 Atrial fibrillation](../../../joi190103supp1_prod.pdf#page=2); [REPORT main endpoint definition p2](../../../jama_aminian_2019_oi_190103.pdf#page=2); [REPORT main Table2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7); [PLAN amendment p7](../../../joi190103supp2_prod.pdf#page=7).

**Printed statements:** PLAN lists AF ICD10 `i48.0, i48.2, i48.91`; REPORT eTable1 lists `i48.0, i48.1, i48.2, i48.91`. ICD9 `427.31` and CPT `93650,93653,93656,93657` agree. PLAN primary composite is the first occurrence of the six listed components, including AF; REPORT also includes AF. Amendment does not describe an AF-definition change.

**Comparison logic:** Compare the operational AF code criteria item by item, not merely the endpoint names. The report AF ICD10 list equals the plan list plus `i48.1`. A listed additional qualifying diagnosis is an expanded operational endpoint criterion even though the named six components remain the same. This categorical/code-set comparison has no rounding interval.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** AF qualifying events and AF baseline risk-set eligibility, its reported HR0.78(95%CI0.62–0.97), and the AF contribution to the primary six-component composite HR0.61(0.55–0.69).

**Why context does not resolve it:** Route A category5 applies to the reproduced operational definition change in a prespecified primary composite component. The package does not state whether the extra code was included in both planned and implemented ascertainment or added later. No event-count impact is inferred.

**Supported alternatives:** The original list may incompletely document the code set actually intended; the report may describe a broadened ascertainment rule; or the operational extraction may use another reconciled list. None is specified by the supplied amendment.

**Human question:** Was `i48.1` included when identifying baseline and incident AF for the primary composite and individual AF analyses, and which supplied plan definition documents that choice?

### F-XS-003

**Title:** The reported coronary-event definition adds primary-diagnosis restrictions not stated in the original component rule.

**Compared locations and document roles:** [PLAN original protocol p4, Coronary artery disease, Other and primary endpoint](../../../joi190103supp2_prod.pdf#page=4); [REPORT non-plan supplement p2, eTable1 Coronary artery disease and bold-text footnote](../../../joi190103supp1_prod.pdf#page=2); [REPORT main p2 coronary endpoint definition](../../../jama_aminian_2019_oi_190103.pdf#page=2); [REPORT main Table2 p7](../../../jama_aminian_2019_oi_190103.pdf#page=7); [PLAN amendment p7](../../../joi190103supp2_prod.pdf#page=7).

**Printed statements:** PLAN p4 lists `411.X, 411.X AND 414.X` with no primary-diagnosis condition. REPORT eTable1 renders the standalone `411.X` bold and renders `414.X` bold in the `411.X AND 414.X` pair; the accompanying footnote says bold text indicates it must be a primary diagnosis. The paired `411.X` is regular. The restriction therefore qualifies specific codes, not the whole row. Direct source-page visual inspection confirmed the distinction. PLAN p4 has no matching bold convention or primary-diagnosis statement, and the supplied amendment does not revise coronary ascertainment.

**Comparison logic:** The original rule accepts the specified diagnosis-code conditions without a position condition. The reported rule additionally requires primary-diagnosis status for the indicated codes. Code identity agrees, but item-by-item eligibility differs by diagnosis position. This is an operational component criterion comparison with no numerical display-precision calculation.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship type:** `P_R`. **All relationships:** `P_R`.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Coronary-event qualifying diagnoses and baseline-history/risk-set ascertainment, the coronary HR0.69(95%CI0.54–0.87), and the coronary component of the primary composite HR0.61(0.55–0.69).

**Why context does not resolve it:** Route A category5 applies to the additional operational requirement for a prespecified composite component. The footnote changes the logical qualifying criterion. It is not a visual-formatting observation: primary versus secondary diagnosis position can determine whether the listed diagnosis qualifies. No effect on event totals is inferred.

**Supported alternatives:** The original plan may leave diagnosis position implicit while the result supplement supplies the fuller intended specification; or a restriction may have been added between the original plan and reported ascertainment. The original plan refers to eTable1, which could incorporate its operational elaboration, but no supplied plan version records whether the restriction was intended originally or amended.

**Human question:** Were the primary-diagnosis requirements for standalone411.X and paired414.X used in both planned and reported coronary-event ascertainment, and how does the unqualified original rule relate to the reported restricted rule?

## Excluded observations

Only apparent differences considered and screened out are listed here; checks that reconcile are recorded in scope closure above.

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-003 p2 versus REPORT DOC-001 p2 | Surgical diabetes cutoff `HbA1c>6.4%` versus `≥6.5%`: half-unit intervals for one-decimal thresholds meet at6.45 and represent the immediately identifiable one-decimal diabetes threshold | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-003 p3 versus REPORT DOC-001 p4 | Matching BMI descriptions30–35/35–40/40+ versus30–34.9/35–39.9/≥40; the reported nonoverlapping decimal categories clarify the intended three bins | TERMINOLOGY_OR_WORDING |
| PLAN DOC-003 pp5–6 versus REPORT DOC-001 pp4–7/Table1 | Insurance and creatinine appear among planned collected variables, but not Table1; report says Table1 variables were included, without saying no other variable entered. An omitted list item alone does not reproduce a conflicting primary-model covariate statement | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 p5 versus REPORT DOC-001 p3,Table2 p7 | Plan additionally excludes baselineeGFR<60 and dialysis from nephropathy risk set; main gives condensed prior-condition exclusion and smaller risk sets. It does not state that those added exclusions were omitted | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 p3 versus REPORT DOC-001 pp2–3 | Nearest prior/absolute-time BMI fallback for controls is detailed in plan but not report; no opposing rule or participant-level evidence establishes a change | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003 p2 versus REPORT DOC-001 p2 | Active cancer/GI-cancer one-year criterion is expressed jointly in plan and separated in report; no supplied evidence establishes a different analysis population from those descriptions | TERMINOLOGY_OR_WORDING |
| PLAN DOC-003 p4 versus REPORT DOC-002 eTable1 p2 | Broad coronary/cerebrovascular rows omit separately printed MI/stroke ICD10 codes; eTable1 independently supplies those same MI/ischemic-stroke definitions and the main names those conditions in its composites, so the split rows do not independently reproduce an omitted component | CONTEXT_RESOLVES |
| REPORT DOC-001 p4 versus DOC-002 eFigure1 p8 | Main says interaction terms were added, supplement specifies replacing continuous covariate with dichotomous subgroup plus interaction. The more detailed supplement explains the subgroup model; main does not assert retaining the original continuous term | CONTEXT_RESOLVES |
| REPORT DOC-001 p4 versus DOC-002 pp10,19 | Main says spline×treatment was added, supplement says treatment term was replaced. Main does not assert the original treatment term remained; supplied detailed specification identifies the time-varying model | CONTEXT_RESOLVES |
| REPORT DOC-001 pp7,9 versus DOC-002 eTable8 p12 | Eight-year weight/HbA1c narrative intervals are95%, while the supplementary longitudinal table is98.8% Bonferroni; displayed point estimates agree after reversing group orientation, weight interval differs by0.1kg. These are non-key longitudinal displays and separately labeled inference levels, not a changed primary/key-secondary vascular result or planned decision rule | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p4 versus p10 Figure5 caption | Generic two-sample proportions test versus specified Fisher exact at8years: categorical-test detail is immediately clarified by the figure caption; no opposed result or inferential rule was reproduced in this cross-source check | CONTEXT_RESOLVES |
| REPORT DOC-002 p19 versus DOC-001 pp1–3 | The isolated “5-component MACE” wording occurs directly after the primary HR.61(.55–.69) and matchingE-values2.15/1.92 are specified; no five-component event definition or separate result is supplied, and the six-component primary outcome being discussed is identifiable at once | TERMINOLOGY_OR_WORDING |
| REPORT DOC-002 p19 | Time-varying narrative points to eTable4 although the complete labeled eTable7 is printed immediately below | PERIPHERAL_COMPARISON |
| REPORT DOC-002 p18 legend versus pp17,19 and PLAN p6 | Legend5:1/10:1 versus text1:5/1:10 uses reverse display orientation; narrative and reported group counts identify the comparator ratio directly | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 Table1 versus DOC-002 eTable3/eTable9/eTable10 | Small differences in copied baseline medication descriptions and time-zero/individual-time contributor totals do not alter primary or key secondary result, vascular analysis population, or planned decision rule | PERIPHERAL_COMPARISON |

## Limitations and completed status

All 39 direct-source units were covered via current maps and direct-source extraction; no scientific-coverage gap remains. No event-level data, code-execution logs or final analysis-design matrix is supplied, so operational consequences of the compared definition changes cannot be quantified. Those absent raw inputs do not remove reproduced statements. No outcome curve was digitized into exact values. All supplied sources and reused evidence assets were preserved. Finding count:3. Excluded-observation count:15.
