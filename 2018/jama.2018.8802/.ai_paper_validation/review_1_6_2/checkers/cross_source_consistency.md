# Cross-source consistency review — Workflow 1.6.2

Scope: all 44 supplied PDF pages: DOC-001 pp.1–10 (REPORT), DOC-002 pp.1–25 (PLAN), DOC-003 pp.1–9 (REPORT). Reviewed the current main/support quantitative maps, the complete quality-control scope and review contract, direct Poppler layout extraction of applicable source pages, and reusable main p.5 page image. Direct PDFs remain authority. No legacy scientific review conclusion, external source, or web source was used. No source or reused asset was modified. Direct text inspection used pdftotext (Poppler 25.03.0), CPU; no derivative was produced. All links below are relative to this checker artifact.

The numeric reviewer owns N identifiers and the statistical reviewers own S identifiers. The XS keys below record this lane's matched-location coverage, not a competing numeric/statistical inventory. Models, analysis units, time, contrast, outcome, denominator and displayed precision were matched before assessing discrepancies. Findings: 4. Excluded observations: 10. No assigned coverage gap remains.

## Complete relationship review record

| Key | Exact matched scope | Comparison result |
|---|---|---|
| XS01 | DOC-001 pp.1–2 abstract/Key Points, pp.4–5 population/flow, p.6 Table1, p.7 Table2; DOC-002 pp.4–8 design/recruitment | 40 randomized hospitals, 20/20 arms, 4800 randomized patients, 2400/2400 treated agree. Primary-analysis labels versus population are F-XS-001. Replacement hospitals are pre-randomization in flow; no further clusters excluded. |
| XS02 | DOC-001 pp.1,4–5 follow-up, p.8 Table3/Figure2; DOC-003 p.5 eTable2 | 2003+1977=3980 followed-up; 397+423=820 lost. mRS availability 3949 and missing 851 is a distinct measurement-availability partition, not the overall follow-up partition. 1852+1798=3650 disability denominators plus 299 deaths at 12 months reconcile to 3949 available mRS; death is excluded from mRS3–5 survivor denominators. Figure2 numbers at risk are survival risk sets, not the final followed-up totals. |
| XS03 | DOC-001 pp.1–3,5,7 primary composite/all-or-none, p.9 conclusions; DOC-002 pp.13–16 endpoint hierarchy | Composite 88.2/84.8, adjusted difference 3.54 (0.68–6.40), P=.02 versus Table2 3.5 (0.7–6.4), P=.02 agree within rounding intervals. ORPA 1.39 (1.12–1.72), P=.003 matches narrative. All-or-none 53.8/47.8, difference 6.69 (−0.41–13.79), P=.06 versus 6.7 (−0.4–13.8), P=.06 agree; ORPA1.19 (0.85–1.67), P=.31 matches. Abstract, Key Points and conclusions distinguish the two co-primary results consistently. Primary aggregation definitions are F-XS-003. |
| XS04 | DOC-001 pp.3,5,7 all nine individual measure definitions/results; DOC-002 Tables2/3 pp.13–16; DOC-003 eTable1 pp.3–4 | Checked each of IV rtPA, early antithrombotics, dysphagia, DVT, discharge antithrombotics, AF/flutter anticoagulation, LDL lipid lowering, hypertension and diabetes. Main explicitly refers to the detailed supplement specification. Expanded AF/flutter, prior lipid-lowering/undocumented LDL and historical hypertension/diabetes criteria supply details to brief labels. Detailed plan Table3 and report eTable1 lists agree. Narrative significant individual measures DVT and antidiabetic agree with Table2; direction of all nine adherence proportions favors intervention. Brief timing/eligibility descriptions are recorded below as excluded observations, not assumed realized denominator changes. |
| XS05 | DOC-002 pp.15–16 eligibility exclusions and DOC-003 pp.3–4 identical denominator footnotes | Item-by-item match: intolerance, excessive adverse-reaction risk, refusal, terminal illness/comfort care; hospice/other short-term hospital; departure against advice before end day2; early death exception for rtPA; missing timing; outside-hospital rtPA; treatment after180 minutes; in-hospital death for discharge measures. No missing item or added exclusion in report detailed list. |
| XS06 | DOC-001 pp.1,3–5,8 secondary definitions and vascular/disability copies; DOC-002 pp.4,16–19 outcomes; DOC-003 pp.6–7 components | Vascular composite components ischemic stroke, hemorrhagic stroke, MI and vascular death agree. mRS3–5 disability and all-cause mortality agree. Narrative/abstract/Table3 vascular proportions and adjusted differences match at3/6/12 months; differences at two decimal places and Table3 one decimal have overlapping half-unit intervals, including −2.18/−2.2 and −3.13/−3.1. Vascular HRs0.65,0.72,0.72 and intervals match narrative and12-month Figure2. Disability proportions, adjusted differences and ORs0.76,0.74,0.74 match Table3. Follow-up origin discrepancy is F-XS-002. |
| XS07 | DOC-001 p.5 mortality conclusion, p.8 Table3/Figure2B |12-month death HR0.86 (0.68–1.09), P=.21 matches Figure2. In-hospital printed absolute-difference interval/P conflict is F-XS-004. The nonsignificant HR column is a separate analysis and explains a possible narrative convention; it cannot reconcile the same absolute-difference column's CI/P pair. |
| XS08 | DOC-001 p.5 rtPA hemorrhage and p.7 Table2 rtPA numerator; DOC-003 p.8 sensitivity |46 and23 treated agree across displays. Symptomatic intracerebral hemorrhage1/46 (2.2%) versus2/23 (8.7%) is a separate safety result; neither is equated with overall vascular hemorrhagic-stroke counts. |
| XS09 | DOC-001 pp.4–5 sensitivity; DOC-002 p.19 contraindication-inclusive sensitivity; DOC-003 eTable4 pp.8–9 | Planned overall-population sensitivity is reported. Composite85.3/80.91 versus85.3/80.9 agrees in precision; difference4.20 (1.77–6.63), ORPA1.36 (1.11–1.67), P=.003 matches ratio column. The eTable4 absolute-difference P<.001 belongs to its own difference column and is not treated as a copy of the ORPA P=.003. All nine individual rows retain numerators with unchanged or expanded eligibility denominators, consistent with the stated sensitivity. |
| XS10 | DOC-001 p.4 multivariable specification and pp.7–8 footnotes; DOC-002 pp.18–19 SAP; DOC-003 pp.7,9 adjustments | ITT specified in report and plan. GEE for within-hospital correlation and opportunity-level binary composite analysis match; the illustrative5-of7 example is identical. Report fixes age, sex, ischemic stroke history, hypertension, diabetes, hyperlipidemia, AF, CAD/MI, smoking, NIHSS, hospital grade, region, stroke unit, teaching and neurological beds; both supplement adjustment footnotes agree item by item. Plan promises identification of control variables, without a fixed contradictory covariate list. |
| XS11 | DOC-001 p.4 tests, missingness, Cox/mixed-model methods; DOC-002 pp.18–19 SAP | χ² categorical and Wilcoxon/Mann–Whitney continuous tests agree with plan's allowed tests. Plan GEE proportions/quantitative variables and Cox vascular/death analyses are reported. Mixed binary model for disability expands unspecified plan detail without a contradictory disability model. Report mode/median baseline imputation has no conflicting planned imputation instruction. Outcomes retain distinct logistic OR, Cox HR and adjusted absolute-difference labels. No unreported preferred model is inferred. |
| XS12 | DOC-001 pp.4,9 power; DOC-002 p.17 power; DOC-003 p.2 prerandomization survey |80% baseline composite,5% detectable improvement,80% power,5% significance,ICC.02,40 hospitals,median120 and4800 planned patients agree. Prior external4.33% improvement is contextual motivation rather than a different target. Main3.4% observed unadjusted score difference and3.54% adjusted difference are distinct quantities. No noninferiority/equivalence margin or direction is asserted. Missing reproducibility inputs are identified below, not supplied by assumption. |
| XS13 | DOC-001 pp.3–4 positivity/multiplicity/two-sided rules; DOC-002 pp.13,16–20 SAP/committee | Report either co-primary significant means positive, no multiplicity adjustment, P<.05, two-sided tests; plan supplies5% significance but no competing coprimary success or multiplicity rule. Secondary outcomes stay labeled secondary; exploratory qualification concerns inference. Report2400/group recruitment stop agrees with planned4800 total and is not an inferential stopping boundary. Plan executive safety/continuation remit is not a numeric efficacy/futility rule. No printed incompatible interim decision appears. |
| XS14 | DOC-001 pp.2–3 intervention, p.5 weekly observed feedback, p.9 duration; DOC-002 pp.8–13 intervention/batches | Four components,2-day workshop, two local leads, first7days/discharge daily plan, full-time coordinator, weekly feedback match. Plan Figure4 four30-patient batches (120) with three intervening improvement cycles agrees with120/cluster target; three cycles do not imply only90 enrolled. Main11-month recruitment period does not contradict a fixed plan calendar duration: none specified. No randomized dose or duration replacement is printed. |
| XS15 | DOC-002 Tables1–3 and SAP compared internally, pp.6–19 | All patient/hospital eligibility and all endpoint/analysis-set criteria inspected item by item, not summarized as interchangeable definitions. Detailed Table3 explains brief Table2 drug/condition labels. Composite definition and opportunity-level model are compatible inside plan; no plan-internal inferential rule conflict reproduced. Administrative/recruitment details and missing boundary definitions are separated below. |
| XS16 | DOC-001 pp.9–10 limitations/administration/references; DOC-002 pp.1–3,20–25 administrative/reference material; DOC-003 p.1 index | No additional applicable matched quantitative result or prospective statistical rule. No supplied Office/CSV/workbook or additional structured scientific source exists. These mapped pages remain covered without importing historical reference numbers as trial results. |

## Findings

### F-XS-001

**Title:** Primary-analysis participant totals differ between the flow diagram and primary result displays.

**Exact compared locations and document roles:** REPORT [main Results p.4](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT [Figure1 bottom boxes p.5](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT [Table2 all-or-none row p.7](../../../jama_wang_2018_oi_180070.pdf#page=7). Abstract [p.1](../../../jama_wang_2018_oi_180070.pdf#page=1) corroborates the distinction between4800 enrolled and3980 completing follow-up.

**Printed statements:** Results says4800 patients were enrolled and included in the primary analysis. Figure1 calls2003 intervention and1977 control patients “included in primary analysis” after397/423 lost at12 months. Table2 primary all-or-none fractions1290/2400 and1147/2400 use all randomized patients.

**Comparison logic and calculation:** Figure1 labels3980 patients as the primary-analysis population, while narrative and primary fractions specify4800. With half-unit intervals, reference2400 gives[2399.5,2400.5]; figure2003 gives[2002.5,2003.5], gap396 and relative discrepancy396/2400=.165. Figure1977 gives[1976.5,1977.5], gap422 and relative discrepancy422/2400=.17583. These exceed.05. The sums2003+397=2400 and1977+423=2400 establish that the figure's smaller values are also12-month follow-up completers.

**Focus area:** A. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The analyzed participant totals for the composite/all-or-none co-primary results.

**Why context does not resolve it:** Both competing displays explicitly identify a primary analysis; the reader can infer a likely follow-up label explanation but cannot retain both primary-analysis population statements when extracting the analysis set.

**Supported alternatives:** Figure1 bottom values may describe the12-month follow-up set, while the primary adherence analysis used4800; alternatively the diagram and primary table may refer to different analyses whose labels were not distinguished. No conclusion about actual patient exclusion is made.

**Exact human question:** Which participant set produced each co-primary adherence result, and do the2003/1977 bottom flow boxes denote12-month follow-up rather than the primary adherence analysis?

### F-XS-002

**Title:** Clinical outcome follow-up is described from discharge in Results and from stroke onset in Methods and the figure.

**Exact compared locations and document roles:** REPORT [Clinical Events opening p.5](../../../jama_wang_2018_oi_180070.pdf#page=5) versus REPORT [outcome definition p.3](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT [time-to-event methods p.4](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT [Table3 disability footnote and Figure2 axes/caption p.8](../../../jama_wang_2018_oi_180070.pdf#page=8). PLAN [secondary outcomes p.16](../../../joi180070supp1_prod.pdf#page=16) and PLAN [Cox analysis p.19](../../../joi180070supp1_prod.pdf#page=19) corroborate the onset definition only.

**Printed statements:** Results attributes the vascular/disability clinical outcomes to3,6,12 months “after discharge.” Methods says3,6,12 months after initial symptom onset; Figure2 axes read “Days After Stroke Symptom Onset,” and Table3 footnote specifies disability after stroke onset. Table1 [p.6](../../../jama_wang_2018_oi_180070.pdf#page=6) reports median hospital stay13 versus12 days, establishing nonidentical origins.

**Comparison logic:** The same named3-,6-,12-month results are assigned to two different origins. A follow-up window beginning at discharge differs from one beginning at stroke onset by the onset-to-discharge interval. No numerical recomputation of event rates is claimed; raw dates are absent. Display-precision relative discrepancy is not applicable to the semantic time-origin comparison.

**Focus area:** D (outcome time point) and matched result attribution. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship type:** S_W. **All relationships:** S_W. The plan confirms one side and is not itself a discrepant comparison.

**Qualifying route:** Route B.

**Affected result or extracted value:** Vascular/disability results at3,6,12 months, including abstract vascular differences−2.03,−2.18,−3.13 percentage points and Table3 disability outcomes.

**Why context does not resolve it:** Discharge and stroke onset are distinct events; Results explicitly refers to Table3 while the adjoining Methods and figure use onset. An extractor needs the actual time origin rather than a preferred phrase.

**Supported alternatives:** Results may use discharge as a shorthand for posthospital follow-up even though assessment windows were anchored at onset; clinical table windows might instead differ from the time-to-event figure. Both interpretations require confirmation of which applies to the printed numbers.

**Exact human question:** Were Table3/eTable3 clinical outcomes assessed3,6,12 months after stroke onset or after discharge, and does the same origin apply to the disability and survival analyses?

### F-XS-003

**Title:** The primary composite is defined as an aggregate opportunity proportion in plan/supplement and as an average of patient proportions in the main report.

**Exact compared locations and document roles:** PLAN [composite definition p.16 lines216–220](../../../joi180070supp1_prod.pdf#page=16), REPORT [baseline eAppendix definition p.2](../../../joi180070supp2_prod.pdf#page=2), REPORT [main composite definition p.3](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT [Table2 composite mean/SD p.7](../../../jama_wang_2018_oi_180070.pdf#page=7). PLAN [opportunity analysis pp.18–19](../../../joi180070supp1_prod.pdf#page=18) and REPORT [main opportunity analysis p.4](../../../jama_wang_2018_oi_180070.pdf#page=4) corroborate the separate inferential unit.

**Printed statements:** Plan composite is total interventions performed among eligible patients divided by total possible interventions among eligible patients. eAppendix repeats this and states the same endpoint definition was used in the randomized phase. Main defines performed/eligible measures “for a given patient,” then says the composite “was calculated for each patient and then averaged.” Table2 prints88.2 (15.1) and84.8 (18.2) as mean(SD).

**Comparison logic:** For received measures r_i and eligible opportunities e_i, the first definition is sum(r_i)/sum(e_i), an opportunity-weighted average; the second is mean(r_i/e_i), equally weighting patients. They coincide only under particular denominators/outcome patterns. The supplied plan/main illustrative5-of7 eligibility example and measure-specific denominators show that eligibility is patient dependent. As a purely illustrative calculation, patients1/1 and0/9 give pooled1/10=.10 versus average(1+0)/2=.50; this illustration is not a trial estimate. No recomputed trial composite or discrepancy percentage is claimed because patient-level opportunities are not supplied. Display-precision intervals are not applicable to the definition comparison.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, S_C.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Definition and weighting of the composite co-primary result88.2% versus84.8%, its adjusted absolute difference3.54 percentage points, and comparability to prerandomization composite inputs.

**Why context does not resolve it:** Category5 covers a changed composite definition. Explicitly averaging individual proportions and explicitly taking the ratio of totals specify different weights. The common opportunity-level OR analysis does not determine which descriptive composite or absolute-difference estimand was intended.

**Supported alternatives:** The protocol/eAppendix may have used aggregate wording loosely for the same patient average; the main descriptive mean could differ from the opportunity-based inferential contrast by design. Both require a definition connecting the printed composite results to the planned endpoint. The alternative is recorded without asserting actual data-level numerical disagreement.

**Exact human question:** Was the planned and reported composite calculated as a ratio of total fulfilled to total eligible opportunities or as the mean of each patient's fulfilled/eligible proportion, and which definition generated each printed descriptive and adjusted composite result?

### F-XS-004

**Title:** In-hospital mortality absolute-difference interval conflicts with its P value and the mortality narrative needs its analysis identified.

**Exact compared locations and document roles:** REPORT [Table3 in-hospital death row p.8](../../../jama_wang_2018_oi_180070.pdf#page=8), REPORT [Clinical Events mortality statement p.5](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT [significance/two-sided rules p.4](../../../jama_wang_2018_oi_180070.pdf#page=4).

**Printed values/statements:**11/2400 (0.5%) versus23/2400 (1.0%); adjusted absolute difference−0.7 (95%CI−1.1 to0.2), P=.009; separate adjusted HR0.96 (0.90–1.02), P=.14. Narrative says no significant difference in total mortality in hospital or at3,6,12 months. Tests are two-sided, significance P<.05.

**Comparison logic:** The same absolute-difference column's95%CI includes0 while P=.009 is below.05. The positive upper endpoint0.2 has half-unit interval[.15,.25], entirely above0, and the lower endpoint remains below0; P half-unit interval[.0085,.0095] is entirely below.05. Route A category1 is not screened by relative display precision. The separate HR/P is coherent and may be the narrative's chosen analysis; it does not eliminate the difference-column inconsistency.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Significance and interval of the adjusted in-hospital mortality absolute difference.

**Why context does not resolve it:** Category1 requires registration of interval/test conflicts. The printed row supplies separate P columns, and the conflict is within the absolute-difference pair, not obtained by combining HR and difference analyses.

**Supported alternatives:** The CI and P may derive from different inferential constructions; the narrative may summarize HR-based inference. No correction to a sign, endpoint or P is proposed.

**Exact human question:** Which analysis generated the in-hospital mortality absolute difference, its95%CI and P=.009, and which mortality analysis supports the narrative statement of no significant difference?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p.6 Table1; DOC-003 p.2 eAppendix | Baseline survey801 patients versus20 per each40 clusters (800 implied). Baseline survey recruitment wording does not change randomized4800 or any printed primary analysis denominator. | PERIPHERAL_COMPARISON |
| DOC-001 p.6 Table1; DOC-003 p.5 eTable2 | Pooled dyslipidemia305+291=596 versus285+62=347 across available/missing-mRS strata; pooled NIHSS medians4 versus3. These are duplicated descriptive baseline characteristics rather than primary/key-secondary effect results; individual display arithmetic is handled independently by numeric lane. | PERIPHERAL_COMPARISON |
| DOC-002 pp.10,13 Table2 versus pp.14–15 Table3; DOC-003 p.3 eTable1 | rtPA brief wording last-seen-well/normal versus initial symptom onset. Detailed eligibility is explicitly assigned to Table3/eTable1, and brief names do not establish a competing realized primary denominator or result. | TERMINOLOGY_OR_WORDING |
| DOC-002 pp.13–15; DOC-003 pp.3,9 |48hours of admission/hospitalization versus2days or end hospital day2 in brief acute-care definitions. Report and detailed plan specify the same hospital-day operational measures; no exact contrasting assessment timestamp is supplied. | TERMINOLOGY_OR_WORDING |
| DOC-002 p.6 Table1 versus DOC-001 p.2 Patients | Older than18 versus18years or older; no supplied minimum age or participant count identifies a changed analysis-population size. | PERIPHERAL_COMPARISON |
| DOC-001 p.4 versus DOC-002 pp.16–19 | Report mode/median imputation, including smoking and NIHSS; plan supplies no imputation replacement rule to contradict. No prespecification claim for this step is printed. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 pp.3–4 versus DOC-002 pp.13,16–19 | Report gives either-co-primary positive criterion and no multiplicity adjustment; plan gives no alternative multiplicity/success criterion. Absence alone does not reproduce a competing decision rule or an analysis falsely called prespecified. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p.4 versus DOC-002 pp.16,18–19 | Report says all secondary analyses interpreted exploratory while continuing to label the outcomes secondary in definitions/tables. This inferential qualification does not reassign outcome status. | TERMINOLOGY_OR_WORDING |
| DOC-001 p.4; DOC-002 p.17 | No composite SD or full sample-size equation supplied; reproducing a power calculation by assuming these would be conditional, and plan/report input lists agree. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p.4; DOC-002 pp.18–20 | No fixed planned disability model, full GEE working structure, numeric interim rule or margin appears; report extensions or omissions alone contain no printed competing primary/key-secondary analysis rule. | CONDITIONAL_OR_UNREPORTED |

## Limitations

Patient-level care opportunities, individual event/assessment dates, model coefficients, and full power-calculation inputs are not supplied. These limit recalculation of actual composite weights and time-origin effects, not source coverage. Historical reusable image renderer version is unrecorded; all cited textual findings were read from direct supplied PDFs using recorded available tooling. No missing tool prevented checking assigned content. Every applicable matched report/report, report/plan and plan/plan relationship represented by the44-page maps was reviewed; no additional structured source exists.
