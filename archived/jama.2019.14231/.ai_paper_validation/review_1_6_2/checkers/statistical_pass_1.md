# Statistical consistency pass 1

Runtime: /root/statistics_pass_1. Fresh qc162_statistical_consistency_reviewer, gpt-6.1-sol/high, FRESH_SPAWN. Exact scope: all inferential relationships in DOC-001 REPORT pp1–12, DOC-002 REPORT pp1–20, and DOC-003 PLAN pp1–7, reconstructed from both fresh complete mapper maps and direct sources. Scope/contract read completely. No web, raw-data audit, preferred analysis, previous review conclusion, or candidate quota. All100 stable records S001–S100 explicitly PASS_1_COMPLETE in [relationship inventory](../statistics/relationship_inventory.md), including all52 eTable8 tuples,120 sensitivity comparisons,40 known-factor HRs, and all planned/statistical dependencies. Findings6; excluded observations7. Every issue remains a checker finding awaiting independent screening; no C IDs assigned here.

## Evidence and inference boundaries

Poppler pdftotext26.01.0 CPU full-source layout extraction: preprocessing/stat1-main-layout.txt, preprocessing/stat1-supp-layout.txt, preprocessing/stat1-plan-layout.txt. Commands: `pdftotext -layout jama_aminian_2019_oi_190103.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-main-layout.txt`; analogous source/output commands for joi190103supp1_prod.pdf and joi190103supp2_prod.pdf. Reusable exact-page images visually confirmed mainp7 and supplementpp8,12,18,20; no new rendering/OCR and no fallback. Supplied PDF is final authority. All printed tuples checked for containment/order/direction/null status and applicable source-grounded method/cross-source dependencies. Methods define two-sided.05 and95% generally; eTable8 specifically defines98.8% Bonferroni intervals. Its effective comparison alpha is.012 (or.0125 if98.75% rounded), not.05. Raw medication P and PH/interaction P are distinguished. Numeric standard errors, exact df/test statistics/covariances and raw samples are absent; approximate Wald reconstructions are diagnostics, not assumed source methods.

Current fresh numeric/cross-source checker outputs were consulted only after this pass independently inspected its source evidence. Shared ARD and matching findings retain this pass's own finding IDs for subsequent screening consolidation. Insurance omission was independently excluded because the report does not claim an exclusive covariate list.

## Findings

### F-ST1-001

**Title:** Five individual-outcome absolute8-year risk differences do not reproduce the difference of the displayed group risks.

**Exact locations and document roles:** REPORT [main Table2p7](../../../jama_aminian_2019_oi_190103.pdf#page=7), five rows heart failure, coronary artery disease, cerebrovascular disease, nephropathy and atrial fibrillation; surgery/control risk columns versus ARD column/footnotea. REPORT [main statistical methodsp4](../../../jama_aminian_2019_oi_190103.pdf#page=4) states KM risk estimates and percentile bootstrap95%CIs1000iterations. REPORT [eTable5p7](../../../joi190103supp1_prod.pdf#page=7) corroborates the same group risks; it is not a conflicting source. S004–S008.

**Printed values, rule and calculation:** ARD is labeled nonsurgical−surgical risk at8y. That subtraction reproduces primary47.7−30.8=16.9, secondary27.6−17.0=10.6, and death17.8−10.0=7.8 in the same display. For one-decimal inputs, each±.05; recomputed difference permits±.10 and printed difference permits±.05 percentage points.

| Outcome | Surgery;control8yrisks | PrintedARD95%CI | RecomputedARD interval | PrintedARD interval | Gap | Relative discrepancy |
|---|---|---|---|---|---|---|
| HF | 6.8;18.9 | 12.9(10.4,15.1) | [12.00,12.20] | [12.85,12.95] | .65 | .65/12.9=.0503876 |
| CAD | 7.9;11.6 | 4.2(1.9,6.8) | [3.60,3.80] | [4.15,4.25] | .35 | .0833333 |
| Cerebrovascular | 4.1;5.6 | 1.8(−.03,3.4) | [1.40,1.60] | [1.75,1.85] | .15 | .0833333 |
| Nephropathy | 6.1;16.3 | 11.1(8.8,13.6) | [10.10,10.30] | [11.05,11.15] | .75 | .0675676 |
| AF | 7.9;13.6 | 6.5(4.4,8.7) | [5.60,5.80] | [6.45,6.55] | .65 | .1000000 |

All exceed.05 after half-unit allowance. This is one repeated pattern in a single difference column, not five findings. Confidence limits are retained, not inferred from subtracting marginal intervals.

**Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The five reported absolute8-year outcome risk reductions12.9/4.2/1.8/11.1/6.5 percentage points rather than group-risk subtraction12.1/3.7/1.5/10.2/5.7.

**Why context does not resolve it:** Route A4: the same explicitly defined method reproduces the three composite/death rows but not these five. This compares KM risk differences to KM group risks, not adjustedHR to crude ratios.

**Alternatives and missing definition:** Bootstrap resampling is specified for CI construction; an alternative bootstrap mean or standardization might define the point column, but no such point-estimate definition is supplied. Separate baseline-history exclusions do not themselves explain why a within-row difference uses different risks. No mechanism inferred.

**Exact human question:** Which point-estimate construction and group risks produced the five individual-outcome absolute8-year risk differences, and which values should be extracted with their printed intervals?

### F-ST1-002

**Title:** The cerebrovascular8-year risk-difference interval includes the null while the displayed treatment test is significant.

**Exact locations and document roles:** REPORT [main Table2p7 cerebrovascular row and footnotesa/b](../../../jama_aminian_2019_oi_190103.pdf#page=7); REPORT [main p6 lower-incidence narrative](../../../jama_aminian_2019_oi_190103.pdf#page=6); REPORT [main p4 confidence/significance methods](../../../jama_aminian_2019_oi_190103.pdf#page=4). Corroborating adjusted HR/P appears in REPORT [Figure3Dp8](../../../jama_aminian_2019_oi_190103.pdf#page=8) and REPORT [eTable6p9](../../../joi190103supp1_prod.pdf#page=9). S006,S038; corroborating copies do not add a conflicting relationship.

**Printed values, rule and calculation:** ARD1.8 percentage points,95%CI−.03 to3.4 contains null0: −.03≤0≤3.4. Same row adjustedHR.67(.48,.94),P=.02; .02<.05, HR interval excludes1. General alpha.05 two-sided/95%CI. Thus the displayed95% risk-difference interval and significant displayed treatment test give different null/significance readings. The HR/CI/P tuple itself reconciles. Scope RouteA1 explicitly retains an interval/test conflict even when assigned to different analyses.

**Display precision:** RouteA1 is exempt from the relative-gap rounding screen. Lower limit−.03 has half-unit[−.035,−.025], still negative; upper3.4 is positive; P=.02 half-unit[.015,.025], still significant at.05. No numerical estimate/P identity is imposed across estimands.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Cerebrovascular8-year absolute risk difference with its95%CI, and the significance attached to the reported reduction in cerebrovascular incidence.

**Why context does not resolve it:** RouteA1 applies to the printed interval versus test conflict. The table's stated Cox-versus-bootstrap distinction is an alternative interpretation that explains why different estimands may yield different decisions; under this review scope it does not remove the finding.

**Alternatives and missing definition:** Footnotea identifies bootstrap8yrisk difference, footnoteb adjusted instantaneous-hazard test. The P may intentionally concern only the HR and not the8yrisk difference; no risk-difference test/P is supplied. This finding does not assert those analyses should be numerically equivalent.

**Exact human question:** Should the significant cerebrovascularP=.02 and lower-incidence statement be read solely as the adjustedHR inference, while the printed8-year risk-difference95%CI includes0, and how should the absolute-risk result be interpreted/extracted?

### F-ST1-003

**Title:** The year5 hemoglobin98.8% interval includes zero while its P value is below.001.

**Exact locations and document roles:** REPORT [eTable8p12 Hemoglobin(g/dL), year5 estimate/CI/P](../../../joi190103supp1_prod.pdf#page=12), column heading98.8% and Bonferroni footnote, spline×treatment method footnote. REPORT [main methodsp4](../../../jama_aminian_2019_oi_190103.pdf#page=4) supplies two-sided testing and spline comparisons. S054.

**Printed values, rule and calculation:** −.1g/dL,98.8%CI(−.2,0),P<.001*. The interval includes null0; its corresponding alpha.012 (.0125 for98.75%rounded) exceeds.001, so a same-analysisP<.001 rejects at both.012 and.0125 while the printed interval includes the null. This remains a CI/test conflict even under the explicitly corrected interval level; it is not generated by comparing98.8% to.05. Years1/2/8 intervals exclude0 withP<.001 and reconcile.

**Display precision:** RouteA1 does not permit excluding a printed zero-endpoint interval/test conflict as rounding. A small negative unrounded upper limit could print0; that is preserved as an alternative for human review. No covariance/df or numerical splineSE is supplied to recover an unrounded interval; no Wald diagnostic used to infer an exactP.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The year5 surgery-versus-nonsurgery hemoglobin mean-change contrast−.1g/dL and whether its Bonferroni interval excludes0.

**Why context does not resolve it:** RouteA1 applies to the printed interval/test decision. The source does not identify an alternative test target for that P, and the displayed confidence limit0 is a extractable numerical endpoint, not a notation-only observation.

**Alternatives and missing definition:** The upper limit may be a rounded negative number, or P may test a different spline association/contrast than the time-specific interval. Source supplies neither unrounded limit nor a different P estimand; these possibilities are not adjudicated.

**Exact human question:** What unrounded year5 hemoglobin interval and test/contrast produced the printed98.8%CI(−.2,0) andP<.001, and do both refer to the same time-specific mean-change difference?

### F-ST1-004

**Title:** The primary E-value pair does not reproduce the transformation supported by the other seven rows of the same display.

**Exact locations and document roles:** REPORT [eTable12p20 primary E-values2.15/1.92 and seven comparator rows](../../../joi190103supp1_prod.pdf#page=20); REPORT [p19 E-value definition/primary explanation](../../../joi190103supp1_prod.pdf#page=19); REPORT [eTable6p9 treatmentHR/upperCI](../../../joi190103supp1_prod.pdf#page=9) and REPORT [main Table2p7](../../../jama_aminian_2019_oi_190103.pdf#page=7) corroborate primaryHR.61/upper.69. S076–S083. PLANamendmentp7 merely corroborates intended8outcome analyses and is not a conflicting location.

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

### F-ST1-005

**Title:** Bonferroni-corrected longitudinal intervals are reported despite the original plan's unadjusted secondary-analysis rule.

**Exact locations and document roles:** PLAN [original protocolp6 Statistical analysis](../../../joi190103supp2_prod.pdf#page=6), weight/HbA1c comparison paragraph followed by significance/multiplicity paragraph; PLAN [amendmentp7](../../../joi190103supp2_prod.pdf#page=7) adds nutritional/adverse-event/E-value work without a revised multiplicity rule. REPORT [eTable8p12](../../../joi190103supp1_prod.pdf#page=12) all52 intervals and confidence/method footnotes; REPORT [main p4](../../../jama_aminian_2019_oi_190103.pdf#page=4) general.05/95% exploratory secondary rule. S094, S049–S061.

**Printed statements and logical rule:** PLANp6 says significance.05,95%CIs where applicable, and adjustment for multiple comparisons of secondary endpoints is not performed. REPORTeTable8 expressly labels every estimate interval98.8%(Bonferroni-corrected). This is an explicit adjustment in the longitudinal comparison display, not different decimal precision for95%.98.75% corresponds to Bonferroni4 at familyalpha.05, rounded98.8%; the exact corrected family is not named. Row other-antihypertensive1y−2.7(−5.6,.3),P=.02 exemplifies an inference whose rawP<.05 while corrected interval contains0. That row itself reconciles at its stated98.8% confidence level and is not an additional CI/P finding.

**Display precision:** Categorical rule/analysis comparison; no half-unit arithmetic can reconcile an expressly unadjusted rule with an expressly Bonferroni-corrected display. The correction family and amendment history, rather than a numeric rounding gap, are the missing definitions.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The prespecified weight/HbA1c longitudinal comparisons and the related medication/nutritional comparison intervals; specifically which confidence level and multiplicity rule should accompany their extracted effects and how year1 antihypertensiveP=.02 is read.

**Why context does not resolve it:** The plan states an unadjusted secondary rule and the report adds a correction without specifying which family is covered or whether these longitudinal outcomes are exempt from that plan rule. The changed confidence level bears directly on interpretation of reported intervals. The explicit vascular exploratory rule does not alone state a separate planned longitudinal adjustment.

**Alternatives and missing definition:** The plan's no-adjustment rule may intend only the seven vascular secondary outcomes, leaving longitudinal analyses a separate family; alternatively a correction may have been introduced for time-point comparisons. The amendment adds nutritional outcomes but no confidence/multiplicity clarification. The table fully discloses that its intervals are corrected; no concealed change is asserted.

**Exact human question:** What analysis family and prospective or amended rule underlie the98.8% Bonferroni intervals, and how does that longitudinal rule relate to the original plan's unadjusted secondary-analysis statement?

### F-ST1-006

**Title:** The supplied original matching statement reverses the reported surgical-to-control matching allocation.

**Exact locations and document roles:** PLAN [p3 Matching Process](../../../joi190103supp2_prod.pdf#page=3); PLAN [p6 sensitivity](../../../joi190103supp2_prod.pdf#page=6); REPORT [main p4 Statistical analysis](../../../jama_aminian_2019_oi_190103.pdf#page=4), [Figure1p3](../../../jama_aminian_2019_oi_190103.pdf#page=3), [abstractp1](../../../jama_aminian_2019_oi_190103.pdf#page=1). PLANamendmentp7 adds no matching revision. S087.

**Printed statements, rule and calculation:** PLAN each nonsurgical patient matched to five surgical patients implies surgery/control=5. REPORT each surgical matched to five nonsurgical patients implies surgery/control=.2; counts2287/11435=.2. The two explicit directions differ by factor25. This is primary-cohort matching design, not a modeled effect compared with a crude count ratio. PLANp6 lists1:1,1:5,1:10 without defining reference group in that sentence.

**Display precision:** Discrete categorical allocation, not rounded measurements; rounding cannot invert the stated exposure-group direction. No recomputed confidence interval applies.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** The matched cohort and primary adjustedHR.61(.55,.69), reported as one surgical to five nonsurgical patients.

**Why context does not resolve it:** The implemented allocation is clear from report/counts, but the explicit original plan uses the inverse. Reading the report cannot establish whether the planned primary matching specification was transposed in text or changed in implementation. Allocation changes primary analysis population design.

**Alternatives and missing definition:** PLANp3 group labels may have been transposed; PLANp6 shorthand may refer to the reported direction; or implementation may have differed from the original statement. No proposed revision or adjudication.

**Exact human question:** Which surgical:nonsurgical matching allocation was intended in the original plan, and how should its explicit five-surgical-per-nonsurgical statement be reconciled with the reported2287:11435 cohort?

## Excluded observations

Only apparent observations considered and not emitted appear below. Checks that reconcile are retained in S records, not repeated as exclusions. None is a reproduced RouteA observation.

| Location | Observation | Reason code |
|---|---|---|
| REPORT mainp7 weight reduction29.1 versus8.7 and difference20.3kg | Half-unit risks allow subtraction[20.30,20.50], displayed difference[20.25,20.35]; overlap, gap0. Different main95% versus supplement98.8% limits not equated. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT Table1pp5–6 standardized-difference columns/footnote | Signed surgery−control values versus “absolute value” wording; evident signed convention, no different clinical effect/CI/test or baseline count reading. | TERMINOLOGY_OR_WORDING |
| REPORT mainp4/eTable8 versus Figure5p10 | General two-sample proportions test and specified Fisher exact8y; figure specifies the test and all6same8yP match. No exclusive competing statistic or discrepant numeric test is supplied. | CONTEXT_RESOLVES |
| REPORT spline descriptions/eTable9 repeated measurements | Dependence/variance details not supplied; source does not assert independence of repeated observations or contradict a stated variance model. An absent detail alone cannot establish method inconsistency. | CONDITIONAL_OR_UNREPORTED |
| PLANp3 sampling motivation versus REPORT sensitivitypp17–19 | Prediction accuracy mentioned alongside baseline/effect sensitivity but no reported accuracy metric; ancillary comparison does not change primary/keysecondary result or planned decision rule. | PERIPHERAL_COMPARISON |
| REPORT supplementp19 “5-component MACE” | Same paragraph supplies primaryHR.61(.55,.69) and its E-values, with no separate5-component estimate; intended six-component primary reference identifiable at once. | TERMINOLOGY_OR_WORDING |
| PLANpp5–6 insurance/creatinine variables versus REPORT Table1/model text | Collection list includes insurance/creatinine but Table1 does not; report says Table1 variables included, not exclusively used. No supplied final-design matrix or explicit exclusion reproduces an omitted model covariate. Creatinine contributes to defined eGFR. | CONDITIONAL_OR_UNREPORTED |

## Complete scope and bounded limitations

All100 natural S records cover the full result-relevant inferential union. Core displayed tuple count372 includes all120 graphical sensitivity comparisons and all52 longitudinal comparisons; no finding cap or sampling. All covariance/test/SE implications were checked where supplied; missing exact inferential inputs are named in the records. No supplied superiority/NI/equivalence margin, power/sample target, interim/stopping or randomized-clustering statement needed a decision-rule calculation. Nonrandomized matched cohort methods are coherent as stated apart from the specific observations above; no broad design or clinical audit is attempted.

Absent raw data, exact graphical endpoints, covariance/df, bootstrap samples and medication numerators limit full reconstruction. They do not leave a source unit uncovered or permit dismissal of a reproduced printed mismatch. Pass2 must use a fresh different runtime ID and the full ledger/screen/recheck, and must revisit every excluded observation against RouteA and display precision. Stable S inventory ready for that handoff.

## Explicit pass-1 relationship completion pointers

Coordinator mechanical documentation repair after validation: the original fresh pass-1 specialist's complete per-relationship assessments and source tuples already exist in statistics/relationship_inventory.md, with PASS_1_COMPLETE on every record. The table below serializes an explicit pointer for every S ID in this checker artifact. It adds no scientific assessment, changes no candidate or calculation, and does not replace the distinct fresh pass-1 execution.

| Relationship ID | Existing pass-1 assessment and source tuples | Completion |
|---|---|---|
| S001 | [Canonical inventory, exact S001 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S002 | [Canonical inventory, exact S002 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S003 | [Canonical inventory, exact S003 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S004 | [Canonical inventory, exact S004 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S005 | [Canonical inventory, exact S005 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S006 | [Canonical inventory, exact S006 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S007 | [Canonical inventory, exact S007 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S008 | [Canonical inventory, exact S008 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S009 | [Canonical inventory, exact S009 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S010 | [Canonical inventory, exact S010 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S011 | [Canonical inventory, exact S011 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S012 | [Canonical inventory, exact S012 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S013 | [Canonical inventory, exact S013 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S014 | [Canonical inventory, exact S014 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S015 | [Canonical inventory, exact S015 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S016 | [Canonical inventory, exact S016 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S017 | [Canonical inventory, exact S017 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S018 | [Canonical inventory, exact S018 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S019 | [Canonical inventory, exact S019 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S020 | [Canonical inventory, exact S020 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S021 | [Canonical inventory, exact S021 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S022 | [Canonical inventory, exact S022 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S023 | [Canonical inventory, exact S023 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S024 | [Canonical inventory, exact S024 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S025 | [Canonical inventory, exact S025 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S026 | [Canonical inventory, exact S026 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S027 | [Canonical inventory, exact S027 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S028 | [Canonical inventory, exact S028 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S029 | [Canonical inventory, exact S029 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S030 | [Canonical inventory, exact S030 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S031 | [Canonical inventory, exact S031 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S032 | [Canonical inventory, exact S032 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S033 | [Canonical inventory, exact S033 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S034 | [Canonical inventory, exact S034 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S035 | [Canonical inventory, exact S035 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S036 | [Canonical inventory, exact S036 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S037 | [Canonical inventory, exact S037 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S038 | [Canonical inventory, exact S038 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S039 | [Canonical inventory, exact S039 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S040 | [Canonical inventory, exact S040 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S041 | [Canonical inventory, exact S041 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S042 | [Canonical inventory, exact S042 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S043 | [Canonical inventory, exact S043 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S044 | [Canonical inventory, exact S044 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S045 | [Canonical inventory, exact S045 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S046 | [Canonical inventory, exact S046 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S047 | [Canonical inventory, exact S047 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S048 | [Canonical inventory, exact S048 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S049 | [Canonical inventory, exact S049 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S050 | [Canonical inventory, exact S050 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S051 | [Canonical inventory, exact S051 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S052 | [Canonical inventory, exact S052 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S053 | [Canonical inventory, exact S053 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S054 | [Canonical inventory, exact S054 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S055 | [Canonical inventory, exact S055 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S056 | [Canonical inventory, exact S056 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S057 | [Canonical inventory, exact S057 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S058 | [Canonical inventory, exact S058 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S059 | [Canonical inventory, exact S059 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S060 | [Canonical inventory, exact S060 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S061 | [Canonical inventory, exact S061 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S062 | [Canonical inventory, exact S062 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S063 | [Canonical inventory, exact S063 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S064 | [Canonical inventory, exact S064 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S065 | [Canonical inventory, exact S065 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S066 | [Canonical inventory, exact S066 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S067 | [Canonical inventory, exact S067 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S068 | [Canonical inventory, exact S068 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S069 | [Canonical inventory, exact S069 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S070 | [Canonical inventory, exact S070 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S071 | [Canonical inventory, exact S071 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S072 | [Canonical inventory, exact S072 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S073 | [Canonical inventory, exact S073 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S074 | [Canonical inventory, exact S074 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S075 | [Canonical inventory, exact S075 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S076 | [Canonical inventory, exact S076 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S077 | [Canonical inventory, exact S077 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S078 | [Canonical inventory, exact S078 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S079 | [Canonical inventory, exact S079 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S080 | [Canonical inventory, exact S080 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S081 | [Canonical inventory, exact S081 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S082 | [Canonical inventory, exact S082 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S083 | [Canonical inventory, exact S083 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S084 | [Canonical inventory, exact S084 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S085 | [Canonical inventory, exact S085 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S086 | [Canonical inventory, exact S086 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S087 | [Canonical inventory, exact S087 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S088 | [Canonical inventory, exact S088 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S089 | [Canonical inventory, exact S089 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S090 | [Canonical inventory, exact S090 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S091 | [Canonical inventory, exact S091 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S092 | [Canonical inventory, exact S092 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S093 | [Canonical inventory, exact S093 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S094 | [Canonical inventory, exact S094 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S095 | [Canonical inventory, exact S095 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S096 | [Canonical inventory, exact S096 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S097 | [Canonical inventory, exact S097 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S098 | [Canonical inventory, exact S098 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S099 | [Canonical inventory, exact S099 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |
| S100 | [Canonical inventory, exact S100 row](../statistics/relationship_inventory.md) | PASS_1_COMPLETE |

