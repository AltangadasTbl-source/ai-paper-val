# Statistical pass 1 — complete independent review

- Runtime agent ID: root/statistics_pass1.
- Preset: fresh qc161_statistical_consistency_reviewer; model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN.
- Exact scope: all inferential values, tests, statistical methods, power specifications, endpoint/population definitions and statistical decision rules in DOC-001 REPORT pp.1-11, DOC-002 PLAN pp.1-37, DOC-003 PLAN pp.1-7 and DOC-004 REPORT pp.1-14. All 69 physical pages were represented in fresh quantitative maps, with applicable and no-applicable units distinguished.
- Relationship count:84. Finding count:1. Excluded-observation count:20. No candidate count target was used.
- Read completely: QUALITY_CONTROL_SCOPE.md; workflow_1_6_1/review_contract.md; START_PROMPT.md; tooling_record.md; both fresh quantitative evidence maps and the complete numeric relationship inventory. No legacy scientific conclusion or web evidence was used.
- Direct source confirmation engine: pdftotext -layout, Poppler 25.03.0, targeted source PDF pages. Direct outputs used as locators and exact printed text; eventual mechanical rechecker must retain direct-source authority. The supplied source PDF pages were read directly for each finding component; no extraction-only discrepancy is advanced.

## Checks and limits

All point estimates are inside their printed intervals, all endpoints are ordered, and directions were checked against their population, outcome, link, baseline adjustment and reference arm. Hospital all-cause mortality, no-DNR mortality, SCDE, all 13 Table 3 rows, all 8 Table 2 inferential rows and all 15 supplementary eTable 4 triples were reviewed without sampling. Repeated main/abstract/narrative/supplement occurrences are included in their matching S record. Weighted kappa, the slope comparison, Bayesian cluster-variation estimate and all 22 historical AUC/P tuples have explicit records. Historical quantities remain contextual rather than becoming current-trial findings.

GEE hospital grouping, exchangeable correlation, link, baseline adjustment, two-sided P testing and 95% confidence intervals are stated. Exact variance/covariance estimates, specific coefficient test/interval construction, degrees of freedom and small-sample correction are not supplied. Diagnostic normal calculations use SE approximately(U-L)/(2*1.96) for additive effects and SE approximately(log U-log L)/(2*1.96) for ratios, with two-sided normal tail probabilities. They are explicitly diagnostics, not a substitution for the source analysis. No numerical diagnostic alone establishes a finding. Displayed inputs were allowed their half-unit intervals; for example 0.85(0.02,1.68),P.05 is compatible once each displayed number varies by.005.

Primary and main secondary conclusions were checked as superiority statements; no supplied noninferiority/equivalence margin or conclusion exists. Holm adjustments are monotone relative to raw P, and all ten exploratory Table 3 values can equal 1 after Holm. Exact Table 2 and 21-outcome family membership is unavailable, so the printed adjusted values cannot be uniquely reconstructed. No unreported family membership was inferred.

Power review covers mortality 5.1/1000, alternative 3.2/1000, SCDE 2/1000 days, code-blue.75/1000 days and stat 8.13/1000 days, all supplied inputs, ratios and absolute reductions. Mortality 18%/.178 maps to about.9/1000, SCDE 31% maps to.62/1000 and code-blue 41% maps to.3075/1000. Exact named Hayes/Bennett equations, cluster-number convention and baseline-adjustment covariance are absent; an unadjusted generic formula or an assumed correlation would be a conditional diagnostic, not exact reproduction. Annual bed-based volume is a labelled diagnostic because the appendix does not identify the 99389-discharge period. Actual/anticipated event totals and rates were checked against their denominators.

Statistical method review includes all SAP model code, binary zero corrections, count offsets, identity time products, mixed-unit predictor scaling, individual versus aggregate GEE, all 8 relative-effect and 5 absolute-effect sensitivity specifications, the two SAP subgroup interaction specifications versus four protocol subgroups, per-patient ICU aggregation/exclusion, weights and strata, fallback identity models, prospective/revised documentation definition, missingness conventions, endpoint windows, outcome hierarchy, no interim analysis and implementation progression rules. Syntax and isolated variable-name slips in illustrative code are self-screened; an absent downstream scaling step is not asserted to have been omitted in the actual analysis.

## Explicit complete relationship coverage

Every ID below has PASS_1_COMPLETE and its source-specific check/calculation/limit in statistics/relationship_inventory.md. This table enumerates each ID; no ID range substitutes for a check.

| Relationship ID | Pass status | Explicit checker record |
|---|---|---|
| S001 | PASS_1_COMPLETE | Primary mortality estimates,CI,P,matching occurrences and conclusion checked. |
| S002 | PASS_1_COMPLETE | No-DNR mortality estimates,CI,P checked. |
| S003 | PASS_1_COMPLETE | Main SCDE ratio/difference distinct model inference checked. |
| S004 | PASS_1_COMPLETE | ICU mortality per ICU discharge checked. |
| S005 | PASS_1_COMPLETE | ICU mortality per hospital discharge checked. |
| S006 | PASS_1_COMPLETE | Arrest interval,ratio,P and rounding checked. |
| S007 | PASS_1_COMPLETE | Preventable arrest interval,ratio,P checked. |
| S008 | PASS_1_COMPLETE | Resuscitation call estimates and distinct links checked. |
| S009 | PASS_1_COMPLETE | Immediate physician call distinct adjustment checked. |
| S010 | PASS_1_COMPLETE | Urgent ICU consultation estimates checked. |
| S011 | PASS_1_COMPLETE | Urgent admission event-level inference checked. |
| S012 | PASS_1_COMPLETE | ICU readmission inference checked. |
| S013 | PASS_1_COMPLETE | Hospital readmission inference checked. |
| S014 | PASS_1_COMPLETE | Heart-rate frequency inference checked. |
| S015 | PASS_1_COMPLETE | Respiratory-rate frequency inference and half-unit precision checked. |
| S016 | PASS_1_COMPLETE | Systolic-pressure frequency inference checked. |
| S017 | PASS_1_COMPLETE | Oxygen-saturation frequency inference checked. |
| S018 | PASS_1_COMPLETE | Respiratory-effort frequency inference checked. |
| S019 | PASS_1_COMPLETE | Capillary-refill frequency inference checked. |
| S020 | PASS_1_COMPLETE | Oxygen-therapy frequency inference checked. |
| S021 | PASS_1_COMPLETE | Documentation completeness inference checked. |
| S022 | PASS_1_COMPLETE | Urgent ICU patient mortality inference checked. |
| S023 | PASS_1_COMPLETE | Predicted PIM mortality inference and fractional prediction distinction checked. |
| S024 | PASS_1_COMPLETE | Mean PIM score inference checked. |
| S025 | PASS_1_COMPLETE | Total ICU LOS inference checked. |
| S026 | PASS_1_COMPLETE | Average ICU LOS inference checked. |
| S027 | PASS_1_COMPLETE | Ventilator-free days inference checked. |
| S028 | PASS_1_COMPLETE | Mechanical ventilation days inference checked. |
| S029 | PASS_1_COMPLETE | Mechanical ventilation binary use inference checked. |
| S030 | PASS_1_COMPLETE | HFOV use inference checked. |
| S031 | PASS_1_COMPLETE | Nitric-oxide use inference checked. |
| S032 | PASS_1_COMPLETE | ECMO use inference checked. |
| S033 | PASS_1_COMPLETE | Dialysis use inference checked. |
| S034 | PASS_1_COMPLETE | Technology-day sum inference checked. |
| S035 | PASS_1_COMPLETE | ICU-stay PELOD inference checked. |
| S036 | PASS_1_COMPLETE | First 24 h PELOD inference checked. |
| S037 | PASS_1_COMPLETE | Weighted kappa interval and consensus relation checked. |
| S038 | PASS_1_COMPLETE | Slopes,difference,P and common-slope decision checked. |
| S039 | PASS_1_COMPLETE | Bayesian k interval and SD/rate comparison checked. |
| S040 | PASS_1_COMPLETE | Mortality power inputs,relative/absolute reduction and missing formula checked. |
| S041 | PASS_1_COMPLETE | Alternative mortality baseline and power inputs checked. |
| S042 | PASS_1_COMPLETE | SCDE power inputs,reduction and event totals checked. |
| S043 | PASS_1_COMPLETE | Code-blue power inputs and reduction checked. |
| S044 | PASS_1_COMPLETE | Stat-call power inputs and reduction checked. |
| S045 | PASS_1_COMPLETE | Randomization,analysis and observation units checked. |
| S046 | PASS_1_COMPLETE | Allocation and strata relation checked. |
| S047 | PASS_1_COMPLETE | Baseline,run-in,intervention and progression rules checked. |
| S048 | PASS_1_COMPLETE | Primary eligibility,DNR and discharge conventions checked. |
| S049 | PASS_1_COMPLETE | SCDE circulatory conjunction directly checked;F-ST1-001. |
| S050 | PASS_1_COMPLETE | SCDE death window directly checked;F-ST1-001. |
| S051 | PASS_1_COMPLETE | SCDE fluid threshold wording checked and self-screened. |
| S052 | PASS_1_COMPLETE | ICU event/patient aggregation and exclusion checked. |
| S053 | PASS_1_COMPLETE | Every repeated-admission and VFD missingness rule checked. |
| S054 | PASS_1_COMPLETE | Readmission operational windows and denominator definitions checked. |
| S055 | PASS_1_COMPLETE | Fractional PIM predictions and inverse-logit examples checked. |
| S056 | PASS_1_COMPLETE | Protocol/SAP/report primary models and size-weight definition checked. |
| S057 | PASS_1_COMPLETE | Binary GEE and zero correction checked. |
| S058 | PASS_1_COMPLETE | Count log link,offset and printed code checked. |
| S059 | PASS_1_COMPLETE | Identity-link count code and scaling algebra checked. |
| S060 | PASS_1_COMPLETE | Planned weighted hospital means versus Gaussian patient GEE checked. |
| S061 | PASS_1_COMPLETE | Documentation units,sampling and models checked. |
| S062 | PASS_1_COMPLETE | Disclosed documentation threshold/set revisions checked. |
| S063 | PASS_1_COMPLETE | Every identity baseline-failure exception checked. |
| S064 | PASS_1_COMPLETE | Disclosed hospital-size stratum removal checked. |
| S065 | PASS_1_COMPLETE | Sidedness,confidence level and null/margin rules checked. |
| S066 | PASS_1_COMPLETE |21-prespecified-outcome Holm specification and missing family mapping checked. |
| S067 | PASS_1_COMPLETE | All 8 Table 2 raw/adjusted P pairs checked. |
| S068 | PASS_1_COMPLETE | All 10 Table 3 exploratory Holm adjustments checked. |
| S069 | PASS_1_COMPLETE | All 4 protocol and 2 SAP subgroup structures/report absence checked. |
| S070 | PASS_1_COMPLETE | No interim and no numeric stopping boundary checked. |
| S071 | PASS_1_COMPLETE | Primary follow-up and discharge-population conventions checked. |
| S072 | PASS_1_COMPLETE | All 8 relative-effect sensitivity methods checked. |
| S073 | PASS_1_COMPLETE | All 5 absolute-effect sensitivity methods checked. |
| S074 | PASS_1_COMPLETE | Outcome hierarchy and prespecification labels checked. |
| S075 | PASS_1_COMPLETE | Every patient-level ICU model/outcome type checked. |
| S076 | PASS_1_COMPLETE | Shell readmission Poisson versus general binary analysis checked. |
| S077 | PASS_1_COMPLETE | Preventability score enumeration and agreement stages checked. |
| S078 | PASS_1_COMPLETE | All anticipated/actual size,event,rate and variation inputs checked. |
| S079 | PASS_1_COMPLETE | Primary mortality conclusion and 47% interpretation checked. |
| S080 | PASS_1_COMPLETE | Main secondary superiority narrative and endpoint relation checked. |
| S081 | PASS_1_COMPLETE | Mortality figure arm/point/line correspondence checked. |
| S082 | PASS_1_COMPLETE | PIM/PELOD scale,time and prediction definitions checked. |
| S083 | PASS_1_COMPLETE | All 22 contextual historical AUC/CI/P tuples checked. |
| S084 | PASS_1_COMPLETE | Historical score reliability and prospective competence rules checked. |

## Finding

### F-ST1-001

**Title:** The main secondary composite endpoint has broader qualifying components in the report than in the supplied protocol.

**Relationships:** S049,S050,S003,S080. **Focus area:** D, planned versus reported statistical design. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; **All relationships:** P_R. The main article and results supplement agree on these components, so their agreement does not create an S_C relationship. The supplied protocol is PLAN by prospective content; the article and results supplement are REPORT by outcome/result content.

**Exact locations and printed statements:**

- PLAN [protocol physical p24, Table 5 category 4](../../../joi180015supp1_prod.pdf#page=24): circulatory support qualifies when ">60 ml/kg" fluid resuscitation in the 12 hours before transfer **and** administration of an inotrope or vasopressor in that window. Categories 4 and 5 are SCDE-positive.
- PLAN [protocol physical p10, main secondary outcome](../../../joi180015supp1_prod.pdf#page=10) defines qualifying death as death without DNR "in an inpatient ward"; PLAN [physical p24, Table 5 category 7](../../../joi180015supp1_prod.pdf#page=24) again specifies ward death with "No transfer from ward area".
- REPORT [results supplement physical p6, eTable 1 SCDE componentsb,d](../../../joi180015supp3_prod.pdf#page=6) joins fluid and vasoactive medication with **and/or**, and qualifies death "on an inpatient ward, or within an hour of urgent ICU admission" without DNR.
- REPORT [main article physical p4, main secondary outcome definition](../../../jama_parshuram_2018_oi_180015.pdf#page=4) defines the composite as "1 or more" components, listing vasoactive medication or fluid boluses in the 12 hours before ICU admission and death in the first hour of ICU admission.
- Affected REPORT result: [main article physical p7, Table 3 SCDE row](../../../jama_parshuram_2018_oi_180015.pdf#page=7), corroborated in [supplement physical p11, eTable 3](../../../joi180015supp3_prod.pdf#page=11):127 events/251859 patient-days versus 259/307584 patient-days, RR 0.77(95% CI 0.61 to 0.97),P=.03; absolute difference-0.34(-0.73 to 0.05) uses the separately disclosed baseline-omitting model.

**Rule and calculation:** Composite membership depends on its component predicates. Let F be qualifying fluid resuscitation and V be qualifying inotrope/vasopressor administration. The protocol circulatory predicate is F∩V; the reported predicate is F∪V. The difference comprises(F\V)∪(V\F), apart from patients already qualifying through other components. Let W denote no-DNR ward death and I no-DNR death within 1 hour after urgent ICU admission. The printed death component changes from W to W∪I. These are logical comparisons of source definitions, not calculations of a revised event count. All non-boundary distinctions persist after half-unit display allowances; conjunction and death location are not numerical-rounding differences. Exact counts of the newly qualifying subsets are not supplied.

**Affected result or extracted value:** The endpoint definition attached to the 386 reported main secondary events and to RR 0.77(0.61,0.97),P=.03 could be extracted as the protocol-defined narrower composite or the report-defined broader composite. Which definition formed the observed events bears directly on this key secondary result's interpretation and endpoint harmonization in evidence synthesis. No change in the event counts or the treatment conclusion is asserted without raw component data.

**Why context does not resolve it:** The main article and eTable 1 clearly describe the reported broader components, but the supplied prospective protocol explicitly requires both circulatory treatments and restricts the death component to ward deaths. Immediate context supplies neither a dated endpoint amendment nor a component-count mapping that explains whether the 386 events were classified by one definition throughout the trial or were reclassified for reporting. The difference is a composite-membership specification, rather than a synonym for late ICU admission. Knowing the label and the final counts does not identify the protocol-to-report endpoint mapping.

**Source-grounded alternatives and missing definition:** The report may state a revised composite used consistently in data collection/analysis; the protocol conjunction or ward-only death description may have been revised before assessment; the added subsets may overlap completely with respiratory/CPR/ECMO components and contribute no additional observed events. The package supplies no amendment date, explicit reconciliation or component-specific counts permitting those alternatives to be selected. No preferred endpoint or analysis is proposed.

**Exact human question:** Which circulatory-treatment conjunction and death-location/time rule were used to classify the 127 versus 259 main secondary events, and does a supplied endpoint amendment or component mapping reconcile that definition with protocol Table 5?

## Excluded observations

Each observation appears once with exactly one scope reason code. These are self-screened observations, not finding IDs. Routine relationships with no observation are covered above and in the inventory.

| Location | Observation | Reason code |
|---|---|---|
| M pp 1,6,7,9;S003,S063,S080 | SCDE absolute CI includes 0 while ratio CI excludes 1/P.03; difference explicitly omits baseline and ratio adjusts baseline, so they are separate fitted contrasts. | CONTEXT_RESOLVES |
| M p7;S001-S013;R p12;S022-S036 | Model-based effects differ from crude count ratios, post means or unadjusted differences; no source statement makes these crude effects. | MODEL_VERSUS_CRUDE |
| M p6;S015,S017;R p12;S026,S027,S036 | Small normal-Wald diagnostic deviations from printed P reconcile within display precision or do not establish a shared exact test/interval identity. | ROUNDING_OR_DISPLAY_PRECISION |
| M p6/Table 2;S067 | Holm values do not reproduce by assuming only the 8 displayed tests, but no exact family membership or complete ordered P vector is supplied; main 21-prespecified text does not explicitly assign Table 2 to that family. | CONDITIONAL_OR_UNREPORTED |
| P p29 versuspp 1,14;S040 |0.9% appendixabsolute reduction versus 0.09% body and 0.9/1000 summary; explicit 5.1/1000 and 18% makes intended 0.9/1000 immediately identifiable. | NOTATION_OR_TYPOGRAPHY |
| P pp 14,29,30;M p4;S040-S044 | Exact power does not mechanically reproduce from unspecified Hayes/Bennett equation/baseline covariance/cluster-number convention; substituting a generic unadjusted formula would be conditional. | CONDITIONAL_OR_UNREPORTED |
| P pp 14,29;S040,S042 | Annual bed-volume diagnostic differs from 99389 anticipateddischarges, but the protocol does not identify that count's observation period/effective exposure; no annual denominator is inferred. | CONDITIONAL_OR_UNREPORTED |
| P p30;S043,S044 | Historical code-blue.75 per 1000 days versus 150/(55963*4), and stat 8.13*.181=1.47153 versus 1.45, concern tertiary background power inputs; neither changes primary/key outcome,population size or a planned decision rule. | PERIPHERAL_COMPARISON |
| A pp 3,4;S058,S059,S075 | Illustrative code offset parentheses, EPOCH$$,d$Group,NlinG/GNlin and x/y slips are resolvable from neighboring definitions and prose. | NOTATION_OR_TYPOGRAPHY |
| A p3;M p7;S059 | Identity code has Nlin=N/1000 and GNlin=N*group; algebra gives a per-day treatment coefficient convertible by 1000. No operational output/downstream conversion is supplied, so absence of conversion is not established. | CONDITIONAL_OR_UNREPORTED |
| P p16;A pp 1,2;M pp 4,5;S056 | Missing numerical hospital-size weighting definition does not establish that aggregate binomial denominator weighting contradicts intended weights. | CONDITIONAL_OR_UNREPORTED |
| P p16;A p4;M p5;R p13;S060,S064 | Report clearly identifies patient Gaussian GEE and explicitly explains stratum removal because only 3 largehospitals; planned/actual models are identifiable, without a contradicted count or unclear produced number. | CONTEXT_RESOLVES |
| P p16;M pp 3,4,6;S062 | Documentation changedallseven to>=5 of 7 andlastsetbeforeanalysis; the revision and reported threshold are disclosed, so the reported quantity is immediately identifiable. | CONTEXT_RESOLVES |
| P p16;A p6;M p5;S069,S072,S073 | Subgroup analyses explicitly not reported and sensitivity estimates not supplied; no subgroup/sensitivity result or conclusion is asserted from an absent number. | CONDITIONAL_OR_UNREPORTED |
| A p5 versuspp 1,2;M p7;S076 | Readmission shell says Poisson while generalbinary analysis and reported OR clearly indicate logistic; isolated shellfamily descriptor resolves from full method. | CONTEXT_RESOLVES |
| P pp 11,28;M p7;R p6;S077 | Plan>4 immediately enumerates 4,5,6 and Table 7 states>=4, making the preventability cutoff immediately identifiable. | NOTATION_OR_TYPOGRAPHY |
| P pp 12,16;M p7;R p6;S054 |48-hour shorthand versusbeforethirdmidnight has matching operationaldefinitions inplan/report; general ICUdenominator wording versuslater SAPICUdischarges is peripheral to primary/key outcome and no analyzed-population change is established. | PERIPHERAL_COMPARISON |
| P p24;M p4;R p6;S051 | >60 m L/kgversus 60 or greater is an isolated boundary wording/symbol difference for the same clinical fluid threshold; no boundary-specificeventmapping supplied. When in doubt, field-readable threshold wording is excluded. | TERMINOLOGY_OR_WORDING |
| R p7;S055,S082;P pp 19,20;S083,S084 | Approximate PIMupper-example 99.9 versusinverse-logit 99.994%, andhistoricalscorevalidation displays, are contextual ratherthanprimary/key trial comparisons. | PERIPHERAL_COMPARISON |
| M p8 caption/legend;R pp 2,3;S081 | Mortalitylinecolor/style labeling differs, but exact labeledhospitalcoordinates,arm assignments andprimary numeric result remain supplied; no resultmisattribution follows. | PERIPHERAL_COMPARISON |

## Completion and limitations

PASS_1_COMPLETE for every S record. All 84 relationships are enumerated explicitly, and no direct-source coverage gap remains. The 1 finding requires the independent inclusion screen before candidate registration. Exact model covariance/test construction,power equation/baseline covariance,Holm family membership,operational SAP code/output,component counts and a dated endpoint amendment are not supplied. Diagnostic approximations do not replace those inputs. Output paths: statistics/relationship_inventory.md; checkers/statistical_pass_1.md. All classification proposals pre-fill human review; no adjudication is assigned.
