# Statistical consistency review — pass 1

- Runtime agent ID: `01a128e0-9c6c-75b0-bd7b-a4d7840873d2`.
- Role/model/effort: fresh `qc161_statistical_consistency_reviewer`, gpt-6.1-sol/high, FRESH_SPAWN.
- Exact scope: all32 M-S and17 U-S mapper groups; stable S001–S049, every eTable1/eTable2 contrast and every eTable3/eTable4 outcome row, all primary/key-secondary design dependencies, and all matching main/supplement/plan occurrences.
- Complete row accounting and evidence crosswalk: [relationship inventory](../statistics/relationship_inventory.md).
- Output: five self-screened findings,14 consolidated excluded observations. Findings require independent inclusion screening; no candidate IDs or human dispositions are assigned here.

Read QUALITY_CONTROL_SCOPE.md, complete1.6.1 review contract/settings/tooling record and both complete evidence maps. Used supplied sources and source-linked native/layout text; direct exact-page extraction confirms cited source language and direct p.7 supplement rendering confirms its day90 row. No old candidates, decisions, final reports, external literature or web used. No assumptions about unreported sidedness, covariance, degrees of freedom, interval algorithm, estimand or model were introduced.

## Full-scope checks and calculation limits

Checked all printed point estimates against ordered intervals, contrast direction, reference group, time point, population, and nominal decision; no point outside its printed interval or inverted interval remains. Primary superiority conclusion agrees with RD−6.4%,95%CI−12.0 to−.9,P=.02. No noninferiority/equivalence hypothesis, margin, multiplicity hierarchy, interim efficacy rule or numerical stopping boundary is supplied. Secondary results are explicitly exploratory; no multiplicity correction is inferred.

Source specifies main primary and categorical outcome comparisons by chi-square, two-tailed thresholdP<.05 and95%CIs; log-rank and logistic analyses are kept separate from count-based proportion tests. Source does not identify interval algorithms/continuity corrections for every contrast, exact continuous-outcome estimator/test choice, logistic covariance, or one-hour contributor counts. Therefore compatibility checks do not assume these ingredients. The adjusted primary OR.60(.38–.93),P=.02 is directionally coherent. A labelled diagnostic symmetric-log-interval calculation gives logSE≈[log(.93)−log(.38)]/3.91993=.2283,z≈−2.24,two-sided normalP≈.024,compatible with displayed.02; this diagnostic is not a reconstruction of the fitted model.

Sample-size diagnostic: standard two-proportion normal approximation with supplied pC=.18,pI=.10,pbar=.14,z(.975)=1.95996398,z(.80)=.84162123 gives total N≈588.26,consistent with chosen590. The formula used was total N=2×[1.95996398√(2×.14×.86)+.84162123√(.18×.82+.10×.90)]²/.08². This is labelled a diagnostic because the package does not state the exact planning algorithm. Inflation590×1.10=649 supports650 after enrollment rounding; neither comparison yields a finding.

All31 eTable1 P contrasts,71 eTable2 printed P contrasts and26 eTable3/eTable4 outcome rows were inspected. Exact list and pass-specific facts are in the inventory. Finite-sample allocation imbalance, overlapping disease/criterion categories, subgroup significance without interaction significance, and distinct chi-square/log-rank values do not themselves create findings.

## Findings

### F-ST1-001

**Title:** The same day7 respiratory-failure result has different reported absolute differences and P values.

**Locations and roles:** REPORT [main abstract p.1](../../../jama_thille_2019_oi_190108.pdf#page=1), REPORT [main Secondary Outcomes p.6](../../../jama_thille_2019_oi_190108.pdf#page=6), REPORT [main Table2 p.8](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT [results supplement eTable1 p.2](../../../joi190108supp2_prod.pdf#page=2). Statistical keys S008/S045.

**Printed values:** Main abstract and narrative: intervention21%,control29%,difference−8.7%(95%CI−15.2 to−1.8),P=.01. Main Table2: control88/302(29%),intervention70/339(21%),difference−8.5%(sameCI),P=.01. Supplement eTable1: same counts88/302 and70/339 and same day7 outcome,P=.02.

**Rule and calculation:** Matched outcome,population,time and comparison should identify a single reported analysis or identify separate analyses. Count-derived difference100×(70/339−88/302)=−8.4901053 percentage points,compatible with printed−8.5. Display intervals−8.7∈[−8.75,−8.65) and−8.5∈[−8.55,−8.45) are disjoint. P=.01 andP=.02 at the same two-decimal precision have disjoint interiors [ .005,.015) and[.015,.025). The article describes these rates as chi-square comparisons; no alternative test/correction label separates eTable1 from Table2. A different continuity correction could explain distinct P values, but the package does not identify that explanation. The finding concerns matched reporting, not a claim that a particular chi-square implementation is impermissible.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed primary relationship:** S_C. **All relationships:** S_C,S_W.

**Affected result or extracted value:** The abstract-reported secondary day7 postextubation respiratory-failure treatment difference and its reported P value.

**Why context does not resolve it:** Both main text and table label the same event counts,analysis population,time and comparison; the common interval does not identify whether−8.7 or−8.5 is the intended extracted point estimate. The supplement does not label a different test. Both P values are below.05,so this does not change their nominal significance classification, but the quantitative result to extract remains inconsistent.

**Alternatives and missing definitions:** The text difference could represent a distinct estimator or transcription; the supplement P could use a different chi-square correction. No separate model/adjustment or test-correction definition is supplied for these occurrences. The unadjusted source-described proportions reconcile with−8.5; no modeled estimate is compared as though it were necessarily crude.

**Exact human question:** Which day7 respiratory-failure absolute difference and P value should be extracted, and do the listed occurrences represent the same analysis or separately defined analyses?

### F-ST1-002

**Title:** The nonhypercapnic day90 mortality absolute difference does not reconcile with its source-specified proportions.

**Locations and roles:** REPORT [results supplement eTable4 p.7](../../../joi190108supp2_prod.pdf#page=7), columns for high-flow alone,n254 and high-flow with NIV,n276,day90 mortality row. Source-context REPORT [main Statistical Analysis p.4](../../../jama_thille_2019_oi_190108.pdf#page=4), which describes categorical rates and confines its stated covariate-adjusted logistic models to primary reintubation. Statistical key S048.

**Printed values:** Control54(21%),intervention50(18%),absolute difference−3.8(95%CI−9.9 to3.6),P=.3626; header population254/276. Direct rendering of the supplied p.7 confirms all cells,including−3.8.

**Rule and calculation:** For the displayed difference of arm mortality proportions,100×(50/276−54/254)=−3.14390049 percentage points. Exact integer counts and denominators permit no count rounding; the displayed−3.8 represents[−3.85,−3.75),which excludes−3.1439. Thus the difference shown is not the displayed proportion contrast. Other binary rows in this table reconcile to their arm proportions,including ICU mortality100×(19/276−21/254)=−1.3837 and hospital mortality100×(46/276−39/254)=1.3123. The midpoint of printedCI−9.9 to3.6 is−3.15,which is an additional diagnostic only,not an assumed interval symmetry rule. No adjusted day90 mortality estimand/model is stated for this table.

**Focus areas:** A/B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W. **All relationships:** S_W.

**Affected result or extracted value:** Nonhypercapnic subgroup day90 mortality absolute treatment difference.

**Why context does not resolve it:** The row identifies counts,denominators and an absolute difference but does not identify a distinct mortality estimator or analysis population that would yield−3.8. A reader cannot establish whether to retain that printed effect estimate or whether a different count/population produced it. The conclusion remains nonsignificant,but the point estimate for evidence extraction differs beyond display precision.

**Alternatives and missing definitions:** A distinct adjusted or modeled contrast would require an explicit model/estimand mapping; none is supplied. The printed point estimate or an arm count might have a transcription discrepancy. This finding is conditional on the table's source-described arm-proportion contrast,not a comparison of an explicitly adjusted estimate with a crude ratio. If recheck establishes an adjusted day90 contrast,this observation should be revisited under MODEL_VERSUS_CRUDE.

**Exact human question:** Which counts,population and estimand produce the day90 nonhypercapnic absolute difference−3.8,and which point estimate should be extracted for that row?

### F-ST1-003

**Title:** The planned key-secondary ICU mortality survival comparison is reported as a proportion comparison.

**Locations and roles:** PLAN [protocol p.34,section6.3 mortality survival analysis](../../../joi190108supp1_prod.pdf#page=34); REPORT [main Statistical Analysis p.4](../../../jama_thille_2019_oi_190108.pdf#page=4); REPORT [main abstract ICU mortality result p.1](../../../jama_thille_2019_oi_190108.pdf#page=1); REPORT [main Table2 p.8](../../../jama_thille_2019_oi_190108.pdf#page=8); REPORT [supplement survival eFigure p.9](../../../joi190108supp2_prod.pdf#page=9). Entire supplied article and results supplement inspected for the planned ICU survival comparison. Statistical keys S004/S014/S040/S049.

**Printed statements and results:** Plan mortality analysis explicitly includes ICU mortality and says Kaplan–Meier curves assess time from enrollment to death and are compared between the two treatment groups by log-rank. The report explicitly compares ICU and hospital mortality rates by chi-square and reports key-secondary ICU mortality RD−2.4%(−6.7 to1.7),P=.25. The supplied mortality survival figure is overall day90 log-rank P=.37. No ICU mortality log-rank comparison is identifiable in the report. Protocol also specifies prognostic Cox models for reintubation and mortality, but does not identify the treatment variable in their covariate set; those omissions do not independently establish an absent randomized treatment HR and are excluded below.

**Rule and logical comparison:** The planned key-secondary between-treatment ICU mortality comparison is log-rank for survival time; the reported comparison is chi-square for proportions. These are explicitly different analyses, not alternate names for the same test. The article does not identify the reported comparison as a replacement or provide the planned ICU comparison. The day90 log-rank result does not supply the distinct ICU mortality comparison. Neither choice is questioned as a methodological preference.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Affected result or extracted value:** Analysis identity of the abstract-reported key-secondary ICU mortality P=.25 and availability of its planned log-rank treatment comparison. A data extractor cannot equate the reported proportion-test P with the planned survival-test P.

**Why context does not resolve it:** Both methods are clearly labelled, but the supplied report does not explain how its chi-square ICU mortality comparison maps to the prospective between-treatment log-rank comparison. The day90 survival figure is for a different follow-up endpoint. The issue concerns the stated planned/reported method mapping, not the absence of an inferred conventional analysis.

**Alternatives and missing definitions:** A later SAP may have specified mortality proportion tests, or the planned ICU survival comparison may have been performed without being presented. No separate SAP/amendment crosswalk, ICU event-time data, censoring definition or planned ICU log-rank output resolves these alternatives. No expected numerical log-rank P is inferred from terminal counts.

**Exact human question:** How does the reported ICU mortality chi-square P=.25 map to the planned between-treatment ICU mortality log-rank comparison, and where is that planned result or the analysis amendment explaining its replacement?

### F-ST1-004

**Title:** Two prespecified primary-outcome subgroup analysis families are absent from the reported subgroup analysis set.

**Locations and roles:** PLAN [protocol p.34,section6.4](../../../joi190108supp1_prod.pdf#page=34); REPORT [main Statistical Analysis p.4](../../../jama_thille_2019_oi_190108.pdf#page=4); REPORT [main subgroup results p.7 andFigure3 p.8](../../../jama_thille_2019_oi_190108.pdf#page=7); REPORT [results supplement eTables3–4 pp.6–7](../../../joi190108supp2_prod.pdf#page=6). Entire supplied results set was inspected for the planned primary subgroup outputs. Statistical keys S006/S027/S028/S029/S042.

**Printed statements:** Plan explicitly says main and secondary subgroup analyses will be performed by PaCO2 group,underlying cardiac or respiratory disease,and type of weaning test(T-piece versus minimal pressure-support). Report defines and presents PaCO2 subgroup primary results and interactionP=.25. Reported subgroup tables/figures contain only PaCO2 strata. Baseline disease and weaning counts are supplied,but no primary treatment effect or interaction for the disease/weaning strata is reported.

**Rule and logical comparison:** Prespecified analyses of the primary outcome are in scope even when a subgroup is not a separately named key-secondary endpoint. The plan lists three subgroup families; report identifies one. A baseline category count is not a primary treatment-effect subgroup analysis. Disease and weaning-test omissions form one repeated planned subgroup-analysis reporting pattern,not separate findings per stratum. No alternate subgroup or preferred analysis is proposed.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Affected result or extracted value:** Completeness and identity of the prespecified primary reintubation treatment-effect subgroup analyses by underlying disease and weaning-test type.

**Why context does not resolve it:** The package gives explicit prospective subgroup commitments and sufficient labels to distinguish these from PaCO2 strata,but does not state whether the other primary subgroup analyses were replaced,deferred,not estimable or omitted. No baseline table or PaCO2 interactionP=.25 supplies their treatment-effect values.

**Alternatives and missing definitions:** A later SAP may have narrowed the subgroup set; the models may have been performed without being published. The supplied package has no separate SAP or amendment crosswalk resolving those alternatives. Disease-group overlap/precise subgroup model details are not invented.

**Exact human question:** What is the status of the prespecified primary disease and weaning-test subgroup analyses,and where are their results or the prospective analysis amendment that explains their absence from the reported set?

### F-ST1-005

**Title:** The respiratory-acidosis threshold contributing to the primary reintubation decision differs between plan and report.

**Locations and roles:** PLAN [protocol pp.30–31,section5.4](../../../joi190108supp1_prod.pdf#page=31); REPORT [main Outcomes p.4](../../../jama_thille_2019_oi_190108.pdf#page=4); REPORT [supplement eTable1 respiratory-acidosis criterion p.2](../../../joi190108supp2_prod.pdf#page=2). Statistical dependency S003/S007/S008/S036/S045.

**Printed statements:** Plan immediate reintubation for respiratory failure requires at least2 severe criteria,including respiratory acidosis pH<7.35 andPaCO2>45. Report severe respiratory failure leading to reintubation requires at least2 criteria,including pH<7.25 andPaCO2>45. Both separately use pH<7.35 for the less severe postextubation respiratory-failure outcome. Supplement severe respiratory-acidosis criterion counts are control12 andintervention9; primary day7 reintubations are55 and40.

**Rule and logical comparison:** Holding the other printed criterion and PaCO2 threshold fixed,pH values[7.25,7.35) satisfy the planned severe-acidosis item but not the reported one. Because two criteria trigger reintubation,the different pH threshold changes the prospective decision rule that helps determine the primary event. The cutoffs are definitions,not rounded measurements. This observation does not presume how many actual patients fall in that interval or claim the primary count necessarily changes.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship:** P_R. **All relationships:** P_R.

**Affected result or extracted value:** Definition of the primary day7 reintubation decision rule and the severe respiratory-acidosis criterion used to interpret primary event counts.

**Why context does not resolve it:** The report intentionally distinguishes ordinary respiratory failure(pH7.35) from severe failure(pH7.25),while plan's corresponding severe-reintubation definition prints7.35. Both are clinically intelligible thresholds and neither immediate paragraph identifies the other as an amendment. A reader can understand each rule but cannot establish which was implemented or intended for the trial's primary reintubation events.

**Alternatives and missing definitions:** A clarified severe threshold may have been adopted later,or one location may not reflect the operational threshold. No prospective amendment or participant-level criterion values are supplied. Criterion counts cannot establish which threshold produced them. No clinical judgment about the preferred threshold is made.

**Exact human question:** Which pH threshold was used for the severe respiratory-acidosis criterion contributing to reintubation,and how should the plan's7.35/report's7.25 difference be understood for interpretation of the primary outcome?

## Excluded observations

Each row has exactly one reason code. Repeated occurrences of the same excluded pattern are consolidated; zero-valued P formatting,notation,or display precision is never the basis of a finding.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.4; PLAN pp.34–35; S002/S043 | DiagnosticN588.26 vs planning590,and10% inflation649 vs chosen650,resolve as planning/enrollment rounding; exact planning algorithm not claimed. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.1,3–4; PLAN p.33; S003/S034 | Analysis excludes seven randomized participants with disclosed eligibility/pre-extubation death/missing-primary reasons; intention-to-treat name does not obscure the explicit641-person as-randomized analyzed set. | CONTEXT_RESOLVES |
| REPORT main p.8 and supplement pp.6–7; S012/S013/S024/S047/S048 | Length-of-stay or reintubation-time contrast need not equal difference of displayed medians; estimator,test andCI details not supplied,so no reconstructed median-difference contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT main Table2 p.8 | Shared percentage heading covers stay contrasts whose row units clearly say days; intended units understandable immediately. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p.7; S023 | Rounded21% vs19% can yield printed1.2 percentage points: true values in[20.5,21.5) and[18.5,19.5) allow differences1.0 to3.0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.7; S030/S031 | Adjusted primaryOR differs from crude counts or center-specific ratios; adjusted/multilevel models explicitly labelled. | MODEL_VERSUS_CRUDE |
| REPORT main p.7,Figure3; supplement pp.6–7; S027/S028/S029 | Nominal significance in hypercapnic subgroup and nonsignificance in other subgroup do not contradict interactionP=.25; significance labels apply to different hypotheses. | CONTEXT_RESOLVES |
| REPORT main p.8; supplement p.9; S017/S049 | Day90 proportion-testP=.30 and survivallog-rankP=.37 are different analyses; no same-test mismatch. | NOT_REPRODUCED |
| PLAN pp.33–34; REPORT main pp.4,7; S005/S030/S038/S039/S041 | Planned logistic/Cox descriptions concern variables predictive of reintubation or mortality; the reported primary logistic model estimates treatment after adjustment. A mapping of the plan's prognostic covariate models to a specific adjusted treatment OR/HR is not supplied, so changed primary treatment-model selection or an omitted treatment HR cannot be established from that mapping. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.7 vs supplement p.7; S029 | Nonhypercapnic narrativeP=.10,tableP=.1057 andlog-rankP=.11 do not establish incompatible tests: table and curve test labels differ; limited narrative precision/formatting does not change nonsignificance. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.7; S048 | 72hCI upper0.0 andP=.0505 are compatible with an unrounded endpoint close to zero; no threshold reversal established. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN pp.25,33; REPORT main pp.1,4,8; S040 | Planned support-free days through14days is not in the abstract and not designated key-secondary; omission alone is outside primary/key-secondary omitted-analysis focus. | OUT_OF_FOCUS |
| PLAN pp.30–31; REPORT main p.4; S008 | Plan ARF respiratory-rate criterion lasts≥2h; abbreviated report omits duration. The supplied report does not affirm a contrary implemented duration. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.33; REPORT main p.4,supplement p.9; S039/S049 | Enrollment/extubation time-origin wording and survival-axis Intubation caption differ; eligibility/extubation context identifies the event origin immediately. No alternative survival estimate/time denominator is supplied. | TERMINOLOGY_OR_WORDING |

## Limitations and handoff

All49 source-group S records have explicit PASS_1_COMPLETE and pass2 pending; no relationship omitted. Exact small-sample test/CI variants,continuous-outcome estimator/test choice,H1 contributor counts,logistic covariance andforced covariates remain unreported and were not inferred. No direct-source/reusable-asset edits; no Python extraction or review orchestration. Five findings F-ST1-001 through F-ST1-005 require the fresh independent screen before anyC assignment. Numeric count/percentage issues from baseline subgroup tables belong to the numeric lane and were still inspected for their statistical implications; no duplicate finding is emitted here solely from a descriptive baseline percentage. Pass2 must revisit all49 groups and all individual expansion rows using the complete ledger,screening log and exact-source recheck.

## Individual pass-1 completion crosswalk

Mechanical closure mirrors the already completed per-relationship pass-1 inventory rows individually below. This expands grouped checker ranges into explicit IDs; it adds no scientific assessment, finding or scope.

| Relationship ID | Existing pass-1 assessment from canonical inventory | Pass 1 status |
|---|---|---|
| S001 | Allocation, unit and stratum definitions coherent; finite allocation counts need not be equal after exclusions. | PASS_1_COMPLETE |
| S002 | Diagnostic standard two-proportion approximation N588.26 supports N590; 590×1.10=649 supports650 as enrollment rounding. | PASS_1_COMPLETE |
| S003 | 648−7=641 and302+339=641; reported eligibility/exclusion reasons and as-randomized treatment define analyzed population. | PASS_1_COMPLETE |
| S004 | Tests matched by estimand; key-secondary ICU mortality method comparison F-ST1-003. | PASS_1_COMPLETE |
| S005 | Fixed covariate adjustment and its printed OR are coherent within report; planned prognostic-model mapping is unreported and screened. | PASS_1_COMPLETE |
| S006 | No stated multiplicity/stopping rule violated; primary additional subgroup comparison F-ST1-004. | PASS_1_COMPLETE |
| S007 | Containment/order/direction and significant superiority agree; printed percentages and RD reconcile. | PASS_1_COMPLETE |
| S008 | Same result differs beyond display precision: F-ST1-001; all intervals ordered and contain estimates. | PASS_1_COMPLETE |
| S009 | Direction, containment, endpoint order, nominal significant decision and raw proportions reconcile. | PASS_1_COMPLETE |
| S010 | Same checks reconcile. | PASS_1_COMPLETE |
| S011 | Same checks and matching occurrences reconcile. | PASS_1_COMPLETE |
| S012 | Containment/order/nonsignificance coherent; difference estimator/CI algorithm unreported, no assumption made. | PASS_1_COMPLETE |
| S013 | Same; printed difference is not asserted to equal difference of displayed medians. | PASS_1_COMPLETE |
| S014 | Count proportions, direction, containment and nonsignificance reconcile; key-secondary planned log-rank comparison F-ST1-003. | PASS_1_COMPLETE |
| S015 | Count proportions, direction, containment and nonsignificance reconcile. | PASS_1_COMPLETE |
| S016 | Same checks reconcile. | PASS_1_COMPLETE |
| S017 | Different chi-square and log-rank analyses can yield .30 and .37; no matched-test contradiction. | PASS_1_COMPLETE |
| S018 | Count proportions, direction, containment and nominal significance reconcile. | PASS_1_COMPLETE |
| S019 | Same checks reconcile; composite logically at least its components and no greater than their sum. | PASS_1_COMPLETE |
| S020 | Exact alternate denominators, direction, containment and nonsignificance reconcile. | PASS_1_COMPLETE |
| S021 | Counts, proportions, direction, containment and nominal significant decision reconcile. | PASS_1_COMPLETE |
| S022 | 291−254=37; interval contains37, direction/significance coherent; exact contributors and inference algorithm absent. | PASS_1_COMPLETE |
| S023 | Rounded whole-percent inputs permit1.2; containment/order/nonsignificance coherent; contributors absent. | PASS_1_COMPLETE |
| S024 | Containment/order/nonsignificance coherent; no assertion that estimate equals difference of rounded medians. | PASS_1_COMPLETE |
| S025 | Count-based difference−1.49 reconciles; exact exploratory test algorithm absent, so no inferred Pearson/Fisher contradiction. | PASS_1_COMPLETE |
| S026 | Curves favor intervention; risk counts monotone; curve and chi-square primary are distinct analyses. | PASS_1_COMPLETE |
| S027 | No interaction claim agrees with nominal P>.05; subgroup significance alone is not a heterogeneity test. | PASS_1_COMPLETE |
| S028 | Order, containment, negative direction, nominal significance and rounding agree; separate log-rank retained. | PASS_1_COMPLETE |
| S029 | Different test labels and display precision are recorded, not conflated; nonsignificance coherent. | PASS_1_COMPLETE |
| S030 | Log-scale containment and direction coherent; diagnostic Wald P≈.024 under symmetric log-scale approximation rounds.02; covariance not reconstructed. | PASS_1_COMPLETE |
| S031 | Stated multilevel model internally coherent; hospital effect estimate/variance absent, so not reconstructed. | PASS_1_COMPLETE |
| S032 | Primary conclusion follows RD/CI/P; five nominal significant secondary outcomes and six nonsignificant reproduce11. | PASS_1_COMPLETE |
| S033 | Matches S001; no changed randomization-level or PaCO2 threshold identified. | PASS_1_COMPLETE |
| S034 | Report explicitly describes seven exclusions and complete-primary population; no unsupported claim that all648 were analyzed. | PASS_1_COMPLETE |
| S035 | Descriptive conventions coherent; no trial-specific imputation specified, no imputation inferred. | PASS_1_COMPLETE |
| S036 | Matches S003/S007 and primary conclusion; no NI/equivalence margin. | PASS_1_COMPLETE |
| S037 | Statistical methods internally coherent by data type; report does not provide predictor-analysis outputs, not confused with treatment crude estimates. | PASS_1_COMPLETE |
| S038 | Primary treatment-model mapping to S005/S030 is unreported and screened; named forced covariates absent, not invented. | PASS_1_COMPLETE |
| S039 | Prognostic Cox output absent; no treatment HR mapping inferred; enrollment/extubation time-origin wording screened. | PASS_1_COMPLETE |
| S040 | Main report mortality ICU/hospital chi-square versus planned survival analysis overlaps F-ST1-003 for key ICU mortality; nonkey free-days omission screened. | PASS_1_COMPLETE |
| S041 | Prognostic mortality Cox output absent; no treatment HR mapping inferred. | PASS_1_COMPLETE |
| S042 | PaCO2 reported; primary disease/weaning subgroup comparisons F-ST1-004. | PASS_1_COMPLETE |
| S043 | Same inputs as S002, sample-size approximation and inflation reconcile; historical rate rationale not treated as endpoint data. | PASS_1_COMPLETE |
| S044 | No inferred boundary or rule; generic ethical monitoring not a numerical stopping analysis. | PASS_1_COMPLETE |
| S045 | All rows inspected; respiratory-failure matched P differs (F-ST1-001); no invented local test definition. | PASS_1_COMPLETE |
| S046 | All71 printed P contrasts inspected; no inference from rounded moments to an unreported exact test; baseline cough/secretions counted by numeric lane. | PASS_1_COMPLETE |
| S047 | Every estimate contained/order/direction and nominal P/zero-exclusion relation inspected; differing small-sample CI/test algorithms not inferred. | PASS_1_COMPLETE |
| S048 | Every row inspected; day90 absolute difference F-ST1-002;72h boundary0.0/P.0505 reconciles display precision. | PASS_1_COMPLETE |
| S049 | Risk counts monotone and death counts compatible with survivors; main mortalityP=.30 is chi-square,not same analysis; axis wording screened. | PASS_1_COMPLETE |
