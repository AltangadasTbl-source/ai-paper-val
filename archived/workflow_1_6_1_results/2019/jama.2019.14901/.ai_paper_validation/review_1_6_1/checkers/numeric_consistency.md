# Numeric consistency review

Runtime `01a128e0-6129-7883-87fc-83aefc195357`; fresh numeric reviewer, gpt-6.1-sol/medium. Read the complete scope, review contract, settings, tooling record and both current extraction maps. Scope: N001–N118, crosswalk M-N001–M-N097 and U-N001–U-N021. Every row of the full support table transcriptions was checked. No historical checker/candidate/report conclusions, external evidence or Python review orchestration used. Sources and reusable assets preserved.

## Arithmetic conventions and complete check record

Displayed decimals retain half of the last printed unit; interval intersections, rather than equality to printed centers, decide display-precision compatibility. Integer participant counts also retain their discrete counting meaning; where useful, a conservative continuous half-unit sensitivity interval is additionally reported. Percent means count divided by the explicitly printed denominator times 100. Absolute categorical differences have intervention minus control direction; adjusted logistic odds ratios are kept separate from crude risks. All interval endpoints and displayed medians/IQRs were checked for containment/order; inferential algorithm compatibility remains with the statistical reviewers. Each stable inventory row is COMPLETE, including groups whose absence of unreported inputs prevents a further reconstruction.

| Complete scope | Rules, inputs and resulting check record |
|---|---|
| N001–N006 | Flow: 927+414+101+18=1460; 3121−1460=1661; 274+182+119+41+39+37=692; 1661−692=969; 270+51=321; 969−321=648; 306+342=648; 306−4=302; 342−3=339; 302+339=641; exclusions 3+1+3=7. Randomized/received/analyzed populations are distinguished. No discrepancy. |
| N007–N016 | Recruitment and intervention values retain time/unit definitions. Difficult/prolonged 92+7+93+14=206, 206/641=32.14%; hypercapnic 111/641=17.32%; intolerance 20/339=5.90%; continued treatment 86/339=25.37%,106/302=35.10%; reintubation criteria 39+57=96 of 41+59=100; rescue 28/88=31.82%,12/28=42.86%; deaths among reintubated 21+11=32/100. Nonexclusive reintubation reasons are not summed as distinct persons. |
| N017–N071 | Every Table1 continuous value, SD, IQR, count, percentage, scale and footnote checked. Sex 195+107=302 and230+109=339. Six intubation causes sum302/339. Weaning203+92+7=302 and232+93+14=339; ventilator42+260=302 and49+290=339; trial188+114=302 and206+133=339. Chronic disease subtypes overlap explicitly. Cough65/284=22.89%,86/322=26.71%; secretions121/288=42.01%,114/326=34.97%. Rounded means/SDs cannot establish unreported raw-data differences; center medians not treated as arm totals. |
| N072–N085 | Every Table2 outcome row checked, including all numerator/denominator pairs, differences, intervals and displayed P labels. Exact categorical intervention-minus-control differences in row order excluding stays: −6.4125,−8.4901,−4.8409,−6.7134,−7.4420,−2.4146,+0.6974,+0.5773,−3.2341,−7.0689,−6.1478 percentage points; deaths among reintubated11/41−21/59=−8.7639520463 points. Printed rounding is compatible, including conservative half-unit sensitivity for composite −6.2. Length-of-stay estimators are not inferred from displayed medians. |
| N086–N088 | All overall/stratum risk-table cells inspected: each series nonincreasing; hypercapnic+nonhypercapnic equals overall at all8 times for both arms (e.g. C37+206=243,I58+233=291 at7d). Risk-set attrition includes censoring and is not an event tally. Axes, units, group/reference and curve direction retained. |
| N089–N097 | Primary exact rates40/339=11.7994%,55/302=18.2119% match11.8/18.2 throughout. Matched ICU reintubation and ICU mortality agree. Respiratory-failure repeated difference discrepancy retained as F-NUM-001. One-hour gas difference291−254=37 agrees; unknown contributor counts and continuous comparison estimators not inferred. Stratum111+530=641. Operational thresholds and disclosed corrected-source context read in full. |
| N098–N110 | All13 PLAN numeric groups checked: current endpoint, secondary families, eligibility, screening, treatment/time/physiologic thresholds, schedules and p42 form values; historical studies clearly separated from current results. Trial-specific values do not become historical outcome denominators. Threshold/design comparisons preserved for cross-source checker; historical/admin internal differences excluded below. No current analyzed count can be derived from unfilled form cells. |
| N111 | All31 eTable1 result/criterion/reason rows checked with302/339 denominators; percentages compatible with display rounding. Main respiratory-failure88/70 and ICU reintubation59/41 match. Component criteria and causes overlap, so row sums exceeding event totals do not establish a distinct-person contradiction. P columns are separately labeled inferential quantities. |
| N112–N114 | All eTable2 cells, four strata254/276/48/63, and all continuous/categorical rows and footnotes checked. Stratum totals254+48=302,276+63=339; intubation and weaning categories each sum their stratum size. Subtype counts overlap explicitly. Cough51+14=65,70+16=86,239+45=284,263+59=322; secretions101+20=121,91+23=114,242+46=288,265+61=326. Hypercapnic printed percentages do not match these pairs, but baseline extraction pairs remain explicit and this is excluded below. |
| N115 | Every13 hypercapnic outcome rows checked, with48/63 denominators or exact reintubated denominators10/6. Categorical differences (excluding stays and exact reintubated pair): −12.8968,−27.7778,−5.1587,−12.4008,−11.3095,−11.8056,−7.2421,−13.3929,−1.8849,−3.8690 points. Conditional mortality2/6−4/10=−6.6667 points. All printed differences compatible; small whole-percentage boundary differences excluded as display/context. |
| N116 | Every13 nonhypercapnic outcome rows checked, with254/276 or49/35 denominators. Corresponding categorical differences: −5.0354,−4.9070,−4.6274,−5.5403,−6.6102,−6.0425,−1.3837,−4.5618,+1.3123,−3.1439 points. Conditional mortality9/35−17/49=−8.9796 points; −8.9 is compatible under half-unit input intervals. Day90 mortality difference retained as F-NUM-002. Each pair of subgroup event counts sums to the corresponding main count, including54+11=65 and50+12=62 deaths at90d. |
| N117 | Every30 center rows and all3 count/denominator/percentage columns checked. Per-row arm numerators and denominators sum to pooled center totals. Arm denominators sum302/339; event numerators55/40; pooled641/95. Percentages match integer rounding. Center detail is not a hospital random-effect estimate. |
| N118 | Survival risk-table14 cells inspected: initial302/339, nonincreasing to237/277 at90d. C302−237=65 matches total deaths; I339−277=62 likewise. Time-axis caption discrepancy is excluded as context-resolved. No curve coordinates inferred from pixels. |

## Findings

### F-NUM-001

**Exact source locations and roles:** REPORT [main abstract PDF p.1](../../../jama_thille_2019_oi_190108.pdf#page=1), REPORT [Secondary Outcomes narrative PDF p.6](../../../jama_thille_2019_oi_190108.pdf#page=6), and REPORT [Table2 respiratory-failure row PDF p.8](../../../jama_thille_2019_oi_190108.pdf#page=8). Stable relationships N073,N090 (M-N073,M-N090).

**Printed inputs:** The abstract and narrative give day7 respiratory failure21% versus29%, absolute difference−8.7% (95%CI−15.2% to−1.8%),P=.01. Table2 gives70/339 versus88/302, absolute difference−8.5% with the same interval and P value. These are the same population, endpoint, time and contrast. Direct Poppler reads of the supplied PDF pages confirmed all occurrences.

**Rule and calculation:** Repeated presentations of the same absolute difference should share a value within display precision. The one-decimal difference intervals [−8.75,−8.65] and [−8.55,−8.45] percentage points are disjoint. The printed event counts give100×(70/339−88/302)=−8.4901053 points, agreeing with Table2. Even allowing all count/denominator inputs continuous half-unit ranges does not remove the direct conflict between the two printed effect estimates.

**Focus area:** A/B, matched result and estimate identity. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W; all relationships S_W.

**Affected result or extracted value:** Overall day7 postextubation respiratory-failure absolute risk difference, a secondary result explicitly reported in the abstract.

**Why context does not resolve it:** Both narrative/abstract and table present their value as the same unqualified absolute difference, alongside identical interval and P value; no alternate population or adjusted estimator is attached to either value. A reader extracting the reported effect must choose between two printed estimates.

**Alternatives and missing definition:** Counts support the table value; an unreported alternative estimator or denominator could in principle explain the narrative value, but none is identified. This observation does not prescribe a replacement value.

**Exact human question:** Which reported absolute risk difference should be extracted for overall day7 respiratory failure, and do the abstract/narrative and Table2 refer to the same calculation?

### F-NUM-002

**Exact source locations and roles:** REPORT [eTable4, Mortality at day90 row and arm population headings, PDF p.7](../../../joi190108supp2_prod.pdf#page=7). Stable relationship N116 (U-N019). Direct Poppler extraction from this supplied source confirmed the complete row and headings; reusable page image was also visually checked as a transcription aid.

**Printed inputs:** Nonhypercapnic HFNC-alone n=254,54 deaths(21%); HFNC+NIV n=276,50 deaths(18%). Absolute difference−3.8 (95%CI−9.9 to3.6),P=.3626. The column identifies absolute differences and the surrounding categorical rows use NIV minus HFNC with these arm denominators. No adjusted-model or alternate-denominator label accompanies this row.

**Rule and calculation:** The indicated absolute difference from counts is100×(50/276−54/254)=−3.14390049 percentage points. Printed−3.8 retains [−3.85,−3.75], which excludes that value. Conservatively allowing all four integer inputs continuous half-unit intervals yields [−3.596663,−2.691302] points, still disjoint from the printed effect interval. This check compares the count-based absolute-difference identity within the same result row; it does not compare a subgroup secondary display with a peripheral value elsewhere.

**Focus area:** A/C, categorical effect-measure computation identity. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W; all relationships S_W.

**Affected result or extracted value:** The reported absolute mortality difference at90d in the nonhypercapnic subgroup, if extracted from eTable4.

**Why context does not resolve it:** The explicit event counts/arm sizes and absolute-difference column yield different numerical effects beyond display precision, and the table supplies no alternate estimator, adjustment or population for the mortality row. Neither a rounding interval nor a stated model identifies how−3.8 was produced.

**Alternatives and missing definition:** A separately modeled estimate or different mortality denominator could explain the value if established, but neither is printed for this result. Do not infer raw data, censoring-adjusted risk, or a preferred estimator. The reported CI and P value are not used as exact raw-risk diagnostics because their algorithm is not specified locally.

**Exact human question:** What calculation and denominators produced the nonhypercapnic day90 mortality absolute difference−3.8, and how does that value relate to the printed54/254 and50/276?

## Excluded observations

Each distinct potential observation is listed once with exactly one scope reason code. Reconciled checks are documented above rather than repeated as speculative observations.

| Location | Observation | Reason code |
|---|---|---|
| Main pp.1,3–5; N001,N018,N019 | Abstract219 women among648 randomized versus216 women among641 analyzed: seven excluded persons distinguish the populations; no contradiction in the printed analysis-population counts. | CONTEXT_RESOLVES |
| Main p.5, N041; supplementary p.6,N115; Table2 composite N084 | Whole-percent boundary examples92/302 printed31%,6/63 printed9%, and composite difference−6.2 versus exact−6.1478: conservative half-unit displayed-input intervals permit the printed values, and explicit counts identify each quantity. | ROUNDING_OR_DISPLAY_PRECISION |
| Main pp.6–7 and supplement p.2,N013,N014,N111 | Criteria/cause totals exceed reintubated persons; multiple simultaneous criteria are allowed, so summing them as mutually exclusive persons is unsupported. | CONTEXT_RESOLVES |
| Main pp.5–6 and supplementary pp.3–4,N017–N071,N112–N113 | Baseline subgroup recombination differs for SAPS II, some chronic disease subtypes, and blood-gas contributor counts; baseline descriptive comparisons do not change an analysis-population size or primary/key-secondary effect. | PERIPHERAL_COMPARISON |
| Supplement p.4,N113 | Hypercapnic cough14/45 printed69%,16/59 printed73%; secretions20/46 printed57%,23/61 printed62%. Actual count-based percentages31.11%,27.12%,43.48%,37.70%. These are descriptive baseline cells, with exact pairs explicitly given; no primary/key-secondary result or analysis-population size changes. | PERIPHERAL_COMPARISON |
| Main p.8,N077–N078; supplement pp.6–7,N115–N116 | Continuous stay differences differ from subtraction of displayed medians; estimator not stated and rounded medians do not establish a raw-data contrast. | CONDITIONAL_OR_UNREPORTED |
| Main p.8,N077–N078 | Shared percent heading covers stay rows individually labeled days; row units make the intended quantity immediately identifiable. | NOTATION_OR_TYPOGRAPHY |
| Main p.7,N094 versus Figure3B p.8,N088 | Narrative P=.10 versus figure log-rank P=.11 uses distinct categorical and time-to-event tests, with explicit figure label. | CONTEXT_RESOLVES |
| Main p.7 adjusted logistic result | Adjusted OR.60 differs from crude risk ratio and crude odds ratio; source explicitly identifies covariate-adjusted odds. | MODEL_VERSUS_CRUDE |
| Main Figures2/3,N086–N088 | Risk-set losses exceed reintubation counts; censoring is not an event and full individual times are not supplied. | CONDITIONAL_OR_UNREPORTED |
| Supplement p.9,N118 | Caption extubation-to90d versus axis Days Since Intubation: both risk rows begin with full extubated randomized population, and the caption identifies survival follow-up. Intended outcome/time origin is apparent. | CONTEXT_RESOLVES |
| Protocol pp.11,32,N107 |51-month total versus printed36+12 months at one location and39+12 elsewhere is an administrative calendar comparison. | PERIPHERAL_COMPARISON |
| Protocol pp.15,17,N110 | Historical large-study narrative400 versus table202+204=406 is background evidence, not the current analysis population or a planned decision rule. | PERIPHERAL_COMPARISON |
| Protocol p.42,N109 versus surrounding readiness text | Embedded form offers operational thresholds and workflow; unfilled form is not a reported patient outcome, and clinical implementation differences alone fall outside this numeric scope. | OUT_OF_FOCUS |
| Main/supplement small rounded rates and categorical differences throughout,N017–N085,N111–N117 | Other printed percentages, single-decimal differences and displayed precision changes are compatible when every input retains its half-unit interval; this includes conditional mortality9/35−17/49 versus−8.9. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p.7,N093 | One-hour hypercapnia21% versus19% with reported difference1.2%; unknown contributor denominators and half-unit rate intervals do not establish a contradiction. | ROUNDING_OR_DISPLAY_PRECISION |

## Completion and limitations

118/118 numeric groups complete;97 main and21 support groups. Findings2; excluded observations16. All full eTable1–5 rows, Figure1–3 and survival risk values are included, with no sampling. No scientific coverage gap. Raw individual data, exact continuous-outcome estimators and exact one-hour contributor counts are not supplied and are not inferred. Plan/report design differences remain source-mapped and are reviewed independently in the cross-source/statistical lanes. Every finding is provisional checker output for independent inclusion screening; no C IDs or human disposition assigned.

## Audit transcription repair

The final auditor recomputed the auxiliary main-table conditional mortality contrast as 100×(11/41−21/59)=−8.7639520463 percentage points, matching statistical pass 2 and the printed −8.8. The arithmetic transcription in the complete-check summary was updated accordingly. No finding, inclusion decision, stable ID, classification or scope changed.
