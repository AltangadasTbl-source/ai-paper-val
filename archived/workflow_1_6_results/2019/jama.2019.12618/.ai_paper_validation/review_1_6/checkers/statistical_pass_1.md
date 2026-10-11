# Statistical consistency pass 1 — Workflow 1.6

- **Runtime agent:** `/root/statistics_pass1` (canonical runtime ID; manifest-compatible form `root/statistics_pass1`).
- **Role/model/effort:** fresh `qc16_statistical_consistency_reviewer`, `gpt-6.1-sol`, `high`.
- **Provider:** current provider unchanged.
- **Pass:** 1, complete; pass 2 requires a different newly spawned runtime agent.
- **Exact scope:** all 103 stable global S IDs below; main17, results interaction3, original MOP1, final MOPtail2, original SAPearly23, SAPmiddle18, finalSAPtail39. Every prospective and descriptive statistical-definition record is retained.
- **Candidates emitted:** 10 distinct provisional evidence observations STAT-A through STAT-J; no stable C IDs assigned here, no finding-count boundary.
- **Scientific source coverage:** complete263-page package mapping; no scientific gap in this statistical assignment.
- **Display-zero exclusion:** no inferential display-zero found; descriptive AE0/0.0notP. Any coherent inferential displayzero is DISPLAY_ZERO_NOT_CANDIDATE. No candidate below depends on a displayzero.
- **Status:** All observations remain Pending Human Adjudication. No severity, scientific acceptance or correction assigned.

## Evidence and compatible-definition rules

Inputs were newly reconstructed maps in extraction/ plus exact supplied PDF-native lookups. No old candidate sets, checker conclusions, verifier dispositions, classifications or finalreports were read. Tools available per tooling_record.md: Poppler26.01.0 native/layout extraction and rendering; view_image for direct mainp6 andfinalSAPp68 images. Source pages/old reusable assets were preserved.

Source confirmation used direct `pdftotext -layout -f N -l N SOURCE -` for mainpp4–7 andSAPpp16–18,24–27,57–58,61,65–68,75. Existing direct mainp6andSAPp68images visually inspected to confirm summaries,footnotepositions,powertablecells. Only supplied evidence used; no external literature or web.

Auxiliary deterministic statistical calculations used R4.5.2 (`Rscript`): Welch formula plus `pt`, `fisher.test`, `power.t.test`; no Python orchestrator/extractor. Auxiliary JS normal-CDF approximation checked the explicitly printed approximatepowerformula; Fisher hypergeometricmass calculation independently replicatedR. Rversionis a calculationengine, not assumed tobetheoriginalcall. Exactmodel/variance/testdefinitions absentfromsourceare explicitlynamed; diagnosticapproximation neverreplacesreportedanalysis.

Required checks coveredpointcontainment,endpointordering,sign/direction,effect/scale/reference labels,matchedrepetitionsandcompatibleCI/P/test/statistic/SErelationships. Primarylogistic/permutationP/CIconstructionlacks exactvariance andinversionoutput; numericalWaldreconstructionisnotauthority. No reportedSE/teststatistic is reconstructedfrommedians/IQRs. Prospective modelrecords were checkedfor source-groundedcoefficient/null/contrast/modelidentities ratherthanmanufacturing realizedresults.

## Complete pass 1 record

| ID | Local key | Role | Status | Source-grounded check and named limitations |
|---|---|---|---|---|
| S001 | S001 | REPORT | PASS_1_COMPLETE | RD and OR estimates lie inside ordered CIs; primary repeats agree. OR>1 and RD>0 favor MTX with MMF reference. Both intervals cross their nulls and P=.20/narrative are coherent. Exact CI/P reconstruction unavailable: permutation inversion rule, random-effect variance/estimation and test output not printed; no Wald assumption substituted. |
| S002 | S002 | REPORT | PASS_1_COMPLETE | 19.1 is between3.6 and30.6;2.35 is between1.16 and4.90. Both favor MTX and exclude null;P=.02 and abstract/table/prose agree. Subgroup permutation/likelihood/inversion details and site variances absent; no exact CI/P criticism. |
| S003 | S003 | REPORT | PASS_1_COMPLETE | -30.3 is between-51.6 and1.1;0.29 is between0.08 and1.05. Direction favors MMF;both CIs include null and P=.07 is nonsignificant. Exact subgroup test/covariance absent; log-Wald diagnostic need not equal reported test. |
| S004 | S004 | REPORT | PASS_1_COMPLETE | Anatomical interaction P=.004 repeats correctly, independent of posterior and intermediate simple-treatment tests. Under source alpha.05, significant-interaction narrative coherent. No interaction coefficient/SE/statistic/df or covariance printed, so do not infer a test from the two subgroup estimates. |
| S005 | S005 | REPORT | PASS_1_COMPLETE | Primary lower bound-5.3 is above negative10% loss boundary when contrast is MTX-MMF; conclusion coherent on reported orientation. Plan rule has separate observable inequality/bound ambiguity (STAT-B); main supplies no additional standalone mismatch. |
| S006 | S006 | REPORT | PASS_1_COMPLETE | Failure category counts26+3+3=32 and38+2+2=42; groupedP=.55 is not a test of overall treatment success. Specific category-test definition, tail ordering and conditional population not named; no reconstructed test substituted. |
| S007 | S007 | REPORT | PASS_1_COMPLETE | Continuing success48/60 versus40/54, RD5.9[-12.2,17.0],OR1.40[.57,3.56] all contain point and include null. Direction, P=.47 and repeated narrative agree. Same mixed model supplied, but variance/inversion unavailable; modest crude-versus-adjusted differences not contradictions. |
| S008 | S008 | REPORT | PASS_1_COMPLETE | Received-drug crossover contrast20/29 versus7/20 is maintained. RD34.2[6.6,52.6],OR4.17[1.32,13.16] contain point/exclude null;P=.02 coherent. Rounded OR4.2[1.3,13.2] agrees. No unintended original-assignment denominator substituted. |
| S009 | S009 | REPORT | PASS_1_COMPLETE | STAT-A: p6 prints mean (SD) percentages 4.6 (1.0) versus 4.3 (0.5), P=.87; p4 specifies a two-sided Welch test. Actual adherence n and tested variable are not explicitly given. For any same-summary participant-level Welch test with n>=2, nearest-tenth rounding implies absolute t>=.23862 and df>=1, so a conservative two-sided P bound is .8508784, below .865 required to round to .87. Hypothetical n96/98 yields P=.009382747 as a diagnostic only. Missing n does not remove the same-summary contradiction; SD/SE or tested-variable identity requires human clarification. |
| S010 | S010 | REPORT | PASS_1_COMPLETE | Mean modeled line-difference.2 with interval-1.7 to2.0 contains point and null;P=.83/narrative coherent. logMAR decreases correspond to positive gain; medians are descriptive and need not equal modeled mean difference. Patient-cluster variance, random-effect covariance/df and exact fitted estimates absent. |
| S011 | S011 | REPORT | PASS_1_COMPLETE | Modeled thickness difference2.4[-78.0,82.8] contains point, is symmetrically centered and crosses0;P=.95 coherent. Negative median changes are reductions, not unsigned magnitudes. Baseline/cluster covariance and df absent, so do not infer SE from medians/IQRs. |
| S012 | S012 | REPORT | PASS_1_COMPLETE | STAT-J conditional precision observation: dose-reduction table21/107 versus15/109 with two-sided Fisher givesR probability-ordering P=.276681552, nearest hundredth.28 versus printed.27. Test-tail convention, exact analysis inclusion and rounding policy not explicitly printed; truncation is an alternative. Counts/proportions themselves agree. |
| S013 | S013 | REPORT | PASS_1_COMPLETE | India OR1.02[.44,2.37] contains point and null;P=.93 compatible qualitative conclusion. Crude proportions are not adjusted OR. InteractionP=.15 agrees with supplementS018 and figure; interaction estimate/statistic/df unavailable. |
| S014 | S014 | REPORT | PASS_1_COMPLETE | Outside-India OR2.51[.89,7.08],RD22.7[-2.6,43.1] contain point and null;P=.08/narrative agree. Rounded OR2.5[.9,7.1] agrees. CountryinteractionP=.45 matchesS020, and is not this simple effect. |
| S015 | S015 | REPORT | PASS_1_COMPLETE | Per-protocol OR1.56[.84,2.96] contains point/null;P=.17 and figure direction coherent. n90+94=184 and success61/90 versus54/94 correctly aligned. Plan adherence cutoff belongs cross-source review, not a fabricated inferential contradiction. |
| S016 | S016 | REPORT | PASS_1_COMPLETE | MI OR1.4[.8,2.4],RD7.6[-5.9,19.1] ordered/contain point/include null, consistentP=.27. Counts66/107 versus59/109 match proportions. MI pooled-test/covariance, replicate values and Rubin df absent; no single complete-data Wald reconstruction imposed. |
| S017 | S017 | REPORT | PASS_1_COMPLETE | Descriptive safety only.14 event occurrences and5 drug-related events versus patient≥1-event cells are distinct measures. No safetyCI/P/test supplied, hence statistical compatibility not applicable; exposure denominators remain numerical/cross-source scope. |
| S018 | SR001 | REPORT | PASS_1_COMPLETE | India interactionP=.15 matchesmain; fixedinteractionmodeldiffersprimarysite-randomsimpleeffect and isnotinferred tobe samecontrast. Interactioncoefficient,SE,df,testfamily andsidednessabsent fromtable; noexactcompatibility. |
| S019 | SR002 | REPORT | PASS_1_COMPLETE | Site interactionP=.20 non-significantunderarticlealpha.05. CoincidencewithprimaryP=.20 isnotindependentduplicationevidence becauseestimandsdiffer. No coefficient/SE/statistic/dfsupplied. |
| S020 | SR003 | REPORT | PASS_1_COMPLETE | CountryinteractionP=.45 matchesmainUS/Mexicocombineddescription; tablecountryfixed versus mainsite-randomsimpleeffectdifferentmodels. No missingcovariance inferred. |
| S021 | PE-S001 | PLAN | PASS_1_COMPLETE | OriginalMOPinterim1/3fraction/conservativeDSMCauthority isprospective. Alpha boundary/sidedness/teststatisticnot givenpp60–61; SAP supplieslaterplan butno observedinterimP. No missingdefinitioncandidate. |
| S022 | S-PT001 | PLAN | PASS_1_COMPLETE | FinalMOPinterim1/3and2/3matchesSAPschedule; SAEs6monthreportingdistinct frominferentiallooks. NonnumericboundarydefinitioncrosslinkedSAP; no realizedtest. |
| S023 | S-PT002 | PLAN | PASS_1_COMPLETE | Versioned26Sep2012primarypredictors treatment/site disclosedamendment. Finalsite-random SAPandmainagree; originalcountry/sitefixed historicalchangesnotautomaticcandidate. |
| S024 | S-SAPE001 | PLAN | PASS_1_COMPLETE | Future-manuscript/posthoc labeling rule reviewed; prospective/reporting definition only, no effect/interval/P to reconcile. |
| S025 | S-SAPE002 | PLAN | PASS_1_COMPLETE | Latent haze sensitivity definition preserves true-versus-observed direction and cataract bias statement; no fitted probabilities, coefficients,SE or realized test. |
| S026 | S-SAPE003 | PLAN | PASS_1_COMPLETE | Primary Equation1 site-fixed/treatment coefficientb1 and one-dfLRT supplied. Country-interaction coefficientb12 named on next page is absent from equation: STAT-F. Model alternatives remain alternatives, not numerical results. |
| S027 | S-SAPE004 | PLAN | PASS_1_COMPLETE | Two-sidedalpha.05 and block permutation supplied. STAT-F links b12=0 country interaction to Equation1 that contains no b12 or interaction. Permutation reference set, statistic and adjusted variance not reported; exact P compatibility unavailable. |
| S028 | S-SAPE005 | PLAN | PASS_1_COMPLETE | Two anatomical categories and beta13 interaction supplied. STAT-G: H0 beta13=0 is glossed as 'there is a difference', conflicting with zero coefficient's no-interaction direction. RR supplemental label is retained separately from OR primary. |
| S029 | S-SAPE006 | PLAN | PASS_1_COMPLETE | STAT-I: 12mo 'same ... Wald procedure' and joint treatment/interaction null do not match primary one-coefficient one-df LRT label/model inS026. Explicit planned alternatives do not repair this claimed identity without clarification. |
| S030 | S-SAPE007 | PLAN | PASS_1_COMPLETE | CoxPH/Wald and parametric/interval-censored sensitivities clearly identified; survival outcome perpatient. No hazard estimates/events/SE,df or censoring data; no numerical compatibility calculation possible. |
| S031 | S-SAPE008 | PLAN | PASS_1_COMPLETE | Country binary coding/site indicators and pooling definitions reviewed. Two-US/two-India version retained; no realized statistical estimate and no inference of additional sites for original version. |
| S032 | S-SAPE009 | PLAN | PASS_1_COMPLETE | Eye-level BSCVA change and patient random effect defined;LRT/MLR labels distinct from means or median summaries. No realized regression/cluster covariance. Changes vs baseline-adjusted final acuity are proposed alternative estimands. |
| S033 | S-SAPE010 | PLAN | PASS_1_COMPLETE | QoL linear mixed/Wald labels, baseline/site adjustments and SF36/vision scales reviewed. No realized coefficients,intervals,variance components or df. |
| S034 | S-SAPE011 | PLAN | PASS_1_COMPLETE | Four discontinuation categories and2x4Fisher before cause-specific tests distinguish unconditional stopping from conditional failure-only distribution. Steroid-free12mo primary-like model separately reviewed; no realized categorytest. |
| S035 | S-SAPE012 | PLAN | PASS_1_COMPLETE | Edema proportion Fisher and thickness linear regression are distinct. Baseline-edema subset explicitly named; transformations are conditional options. No realized edema counts or model output, so no inferential statistic reconstructed. |
| S036 | S-SAPE013 | PLAN | PASS_1_COMPLETE | Bayesian posterior/prior sensitivity and alternative failure definitions reviewed. Equation1 likelihood is original fixedsite model; no posterior quantiles/realized prior values in package, no inconsistency inferred. |
| S037 | S-SAPE014 | PLAN | PASS_1_COMPLETE | Haze ordinal clustered/polytomous, binary McNemar alternative,AE risk/rate CI,VKH and dose logistic definitions reviewed. A proportion is not forced to be recurrent rate. No realized estimates in this plan record. |
| S038 | S-SAPE015 | PLAN | PASS_1_COMPLETE | Rescue logistic controls failure reason(efﬁcacyvsother) and gives95%CIs regardless significance; treatment contrast and site-adjusted supplemental estimates are prospective. No CI/P to reconcile. |
| S039 | S-SAPE016 | PLAN | PASS_1_COMPLETE | Loss tipping points and diagnostics/transforms/robust/bootstrap alternatives reviewed individually. No realized residual tests or rawdiagnostic outputs. Named options do not establish an exact final test's variance. |
| S040 | S-SAPE017 | PLAN | PASS_1_COMPLETE | Primary sample-size expression/80%target/.4vs.6/two-sided.05 and10%loss reviewed. Diagnostic normal planning givesabout196 evaluable or218 afterloss, close216 stated approximate target. Printed Z_alpha convention not inferred; all25sensitivity cells preserved below. |
| S041 | S-SAPE018 | PLAN | PASS_1_COMPLETE | STAT-C: lambdaC labels MTX but is assigned log(2)/3.5 from an explicitly MMF historical median. Formula,6mo censoring and2.47mo detection claim retained; unreported median-vs-mean difference and alternativehazard prevent exact inversepower adjudication. Secondary power inputs preserved below. |
| S042 | S-SAPE019 | PLAN | PASS_1_COMPLETE | Rescue formula inputs and87%claim arithmetically compatible. STAT-D 17% difference conflicts25%summary and.42/.17 table; STAT-E sequence/sample mapping contradicts enrollmenttable. All35power-table cells retained below. |
| S043 | S-SAPE020 | PLAN | PASS_1_COMPLETE | Three-reason withinrescue logistic LRT alpha.05/2=.025 arithmetic coherent. Confidenceintervals by rescue/anatomy require no overall significance. No realizedLRT statistic/df. |
| S044 | S-SAPE021 | PLAN | PASS_1_COMPLETE | Complete-caseprimary versus supplementaryMI/GLMM/extremescenarios are explicitly differentiated. Tenimputations/hotdeck and patient/eye random effects supplied; no realized RubinSE/df or replicate estimates. ITT-priority label alone does not establish raw-result contradiction. |
| S045 | S-SAPE022 | PLAN | PASS_1_COMPLETE | Overall test before subgroup/secondary rule and two-sidedalpha.05 reviewed. Source does not explicitly require significant overall test before conducting every subgroup test; no gate inferred from convention. Interim fractions and spending crosslinkS047. |
| S046 | S-SAPE023 | PLAN | PASS_1_COMPLETE | 2xN Fisher deviations and chi-square discontinuation definitions reviewed; frequency denominators stated. No realized plan P/count comparison. N denotes categorycount, not numeric test statistic. |
| S047 | S-SAPL001 | PLAN | PASS_1_COMPLETE | Alpha-spending formula gamma-5.623626 produces.0010000003 at1/3 and.0075178357 at2/3, compatible printed.001/.0075. Exact spending versus crossingboundary distinction retained; no realized interimlooks. |
| S048 | S-SAPL002 | PLAN | PASS_1_COMPLETE | No-futility rule and safety risk-logistic/recurrent-ratePoisson labels coherent. No observed harm boundary demanded because DSMCjudgment explicit. |
| S049 | S-SAPL003 | PLAN | PASS_1_COMPLETE | Four pooledAE patient proportions Fisher versus recurrentratesPoisson/NB remain distinct. No suppliedobserved rate/exposure or inferential estimates. |
| S050 | S-SAPL004 | PLAN | PASS_1_COMPLETE | Final future/posthoc-label specification reviewed; no realized posthoc numeric result in assigned record. |
| S051 | S-SAPL005 | PLAN | PASS_1_COMPLETE | HiddenMarkov/dynamic-process and inflammation thresholds identify explorations; no transition probabilities/stats/SE given. No method-general criticism. |
| S052 | S-SAPL006 | PLAN | PASS_1_COMPLETE | Latent haze/cataract sensitivity direction reviewed as final prospective definition; no numerical model output. |
| S053 | S-SAPL007 | PLAN | PASS_1_COMPLETE | Final primary treatment/site-random model, H0 treatmentcoefficient0 andLRT1df agree with article primary model description. Permutationdefined, but exact variance/test output unavailable. STAT-I crosslink same-Wald claim onp58. |
| S054 | S-SAPL008 | PLAN | PASS_1_COMPLETE | STAT-G nullzero glossed as difference repeats; STAT-H final subgroup 'beginEquation1' points to superseded fixedsite equation not finalrandomsite model. beta13 and anatomicalcoding otherwise retained; no invented country adjustment mapping. |
| S055 | S-SAPL009 | PLAN | PASS_1_COMPLETE | STAT-I same-Wald/jointnull claim versus primaryLRTsingle treatment coefficient repeated. Explicit adjusted/unadjusted/interaction sensitivity models not assumed to be primary. |
| S056 | S-SAPL010 | PLAN | PASS_1_COMPLETE | CoxPH/Wald perpatient timecontrol and model/country sensitivities reviewed; no hazard estimate,SE,df,event/censoring count. |
| S057 | S-SAPL011 | PLAN | PASS_1_COMPLETE | Eyechange linear mixedpatientrandom model andLRT, transformations/longitudinal/LOCF alternatives reviewed; compatible generic article clustering description. No model-fit output or covariance. |
| S058 | S-SAPL012 | PLAN | PASS_1_COMPLETE | QoL Wald,4categorydiscontinuation2x4Fisher and steroid-free logistic remain separate estimands/tests. No realized CI/P. |
| S059 | S-SAPL013 | PLAN | PASS_1_COMPLETE | EdemaFisher,thicknessbaseline regression andBayesianlikelihood alternatives reviewed. Equation1 likelihood reference supports STAT-H obsolete model-referent observation, not a new candidate. No posterior/SE/statistic values. |
| S060 | S-SAPL014 | PLAN | PASS_1_COMPLETE | STAT-B: lower95%CI 'less than10%' NIrule conflicts loss-margin interpretation irrespective of undocumented contrast orientation; lower-tail decision would accept large negative losses if MTX-MMF, whereas MMF-MTX needs upperbound. Missing bound/contrast named. |
| S061 | S-SAPL015 | PLAN | PASS_1_COMPLETE | Haze/AE/VKH/dose definitions preserve proportions vs rates,ordinal vsbinary and scales. Plan dosage-logistic vs articleFisher is cross-source matched-test scope; no observed P inferred. |
| S062 | S-SAPL016 | PLAN | PASS_1_COMPLETE | Rescue treatmentcoefficient and two firstline/rescue analysesalpha.05 preserve contrast/outcome/95%CIs. Failure reason controlled, unlike crude test. No output covariance or teststatistic. |
| S063 | S-SAPL017 | PLAN | PASS_1_COMPLETE | All model diagnostics and transformations reviewed; no realized tests. No assumption of covariance or goodmodel-fit from named diagnostics. |
| S064 | S-SAPL018 | PLAN | PASS_1_COMPLETE | Final primary-power216/.4/.6/80%/.05/10%loss and exact25cellpower table reviewed as original repetition. Approximate planning target tolerates218vs216normal diagnostic; interim-adjustedcriticalvalue unspecified. |
| S065 | S-ST001 | PLAN | PASS_1_COMPLETE | 12mo78%power/20%effect includes additional5%loss; no exact inverseformula or criticalvalue provided here. Normal-planningdiagnostic around78% coherent; no reportedtrialCI/P. |
| S066 | S-ST002 | PLAN | PASS_1_COMPLETE | STAT-C repeated hazard-arm labeling conflict. Supplied exponentialplanning equation preserved; median/expected-difference estimand not silently inferred.6moT and2.47mo detectable statement covered. |
| S067 | S-ST003 | PLAN | PASS_1_COMPLETE | SD6.5letters/n108/delta2.63/80%power coherent if10%loss yields97.2evaluable: Rpower.t.test about.8014; ignoringloss gives.8413. Diagnostic only; sample-size meaning/expected rounding named. |
| S068 | S-ST004 | PLAN | PASS_1_COMPLETE | SD8.4/r.6 givesvariance reduction.36 and adjustedSD6.72 exactly. Rpower.t.test n108/delta2.57 gives.7989, coherent approximate80%. Attrition treatment not explicit for this item; not inferred as observed contradiction. |
| S069 | S-ST005 | PLAN | PASS_1_COMPLETE | Tolerability13%vs4% and10%loss/61%power retain distinct safety5%vs5%; referenced Freedmanformula not printed here. No external formula imported and noexactpower criticism. |
| S070 | S-ST006 | PLAN | PASS_1_COMPLETE | Edema19%vs38% correctly half/factortwo;80%approxpower. Formula/continuity correction not supplied in thisitem; no unseen convention inferred. |
| S071 | S-ST007 | PLAN | PASS_1_COMPLETE | ThicknessSD160μm/delta65μm/n108beforeloss yieldsrough80%after10%loss; baselineadjustment explicitly increasespower. No realized thicknessSE or covariance. |
| S072 | S-ST008 | PLAN | PASS_1_COMPLETE | Primary rescue probability/95%CI/threefailurereasons definition reviewed. No reportedtrialCI/P; descriptiveestimates retainedregardless overalltest. |
| S073 | S-ST009 | PLAN | PASS_1_COMPLETE | Available-completern_j expression includesboth r1.9 andr2.95; enrollmenttable separatelyexcludes r2.95.55.4/36.9completers are coherent. STAT-E separately concernssequence/samplecolumns inpower table. |
| S074 | S-ST010 | PLAN | PASS_1_COMPLETE | Printed normalCDFpower gives.8741653 for.42/.15 and58/38, compatible.87. Quantile usesalpha/2 withtwo-sided.05supplied; no externaltest imposed. STAT-E sample/groupassignment retained. |
| S075 | S-ST011 | PLAN | PASS_1_COMPLETE | STAT-D: 'difference17%' contradicted by same.42MMF scenario's80%row.42-.17=.25 andsummary25%. Literal17%absolute-delta diagnosticpower42.81%; exact printed contradictorydifference is primary observation. |
| S076 | S-ST012 | PLAN | PASS_1_COMPLETE | Row1allfivecells retained;suppliedformula87.4165% rounds87%, coherent. STAT-E sequence58/38mapping conflict remains separate fromformula's arithmetic. |
| S077 | S-ST013 | PLAN | PASS_1_COMPLETE | Row2formula80.2453% rounds80%;.42-.17=.25 confirms STAT-D, not17%. Allfivecells retained andSTAT-E sequenceassignment preserved. |
| S078 | S-ST014 | PLAN | PASS_1_COMPLETE | Row3formula82.8952% rounds83%;switchingprobabilities changespowerasexpected with unequaln. No copy/paste candidate. |
| S079 | S-ST015 | PLAN | PASS_1_COMPLETE | Row4formula94.0835% rounds94%;doubling secondsequence n38->76 increasespower. Allcells retained. |
| S080 | S-ST016 | PLAN | PASS_1_COMPLETE | Row5formula95.5020% rounds96%;doubling firstsequence58->116 increasespower. Allcells retained. |
| S081 | S-ST017 | PLAN | PASS_1_COMPLETE | Row6formula80.0441% rounds80%;40/40sample and.42/.15validunderprintedformula. Allcells retained. |
| S082 | S-ST018 | PLAN | PASS_1_COMPLETE | Row7formula82.3322% versusprintedapproximate80% is coarseapproximately80%statement, not independent contradiction at unstated approximation tolerance. No candidate solely for2.3percentagepointcoarsepower rounding. Allcells retained. |
| S083 | S-ST019 | PLAN | PASS_1_COMPLETE | 25%difference/.42/80%summary matchesrow2difference. STAT-D contradicts17%prose;STAT-E '58DrugA38DrugB' labelsretainsequencequestion. |
| S084 | S-ST020 | PLAN | PASS_1_COMPLETE | Rescue/anatomicCIprospective, individualCIsremain computable withonearm small. Confidencelevel not restated here, primary95%crosslinkretained; no actual interval tocheck. |
| S085 | S-ST021 | PLAN | PASS_1_COMPLETE | Withinrescue3categoryLRTalpha.05/2=.025 is arithmeticcoherent; additionalrescuevsfirstline andAim1similar methodsprospective. No observed statistic/df/P. |
| S086 | S-ST022 | PLAN | PASS_1_COMPLETE | Completecaseprimary/ITTpriority and supplementalMI/GLMM/extremes are differentiated; no additional inference fromlabelalone. |
| S087 | S-ST023 | PLAN | PASS_1_COMPLETE | TenregressionMI/crossvalidation/LittleRubin overalltest covariates/timings retained; no perimputationparameters, pooledvariance/df or realizedtests. |
| S088 | S-ST024 | PLAN | PASS_1_COMPLETE | Hotdecktenreplications sensitivity and nonmissingassignmentpreserved. No test statistic/SE. |
| S089 | S-ST025 | PLAN | PASS_1_COMPLETE | LongitudinalGLMMperson/eye random nesting andvisit-interactions retain distinct longitudinalestimand; no outcome probabilities,covariance orfittedcoefficients. |
| S090 | S-ST026 | PLAN | PASS_1_COMPLETE | Post90day injection assignsoutcomefrom contemporaneous control; prospective sensitivity, not observedwrongnumerator. No unprovided denominator or model inferred. |
| S091 | S-ST027 | PLAN | PASS_1_COMPLETE | Overallbeforeeachsubgroup/secondary test andalpha.05source rule reviewed. Not explicit significancegate; no gate inferred. Multiplecomparisons caution inreportcompatible with exploratorylabel. |
| S092 | S-ST028 | PLAN | PASS_1_COMPLETE | Interim1/3,2/3 approximate/flexiblespending andsamefinalmodel definition reviewed; no realized interimtest or informationfractions. |
| S093 | S-ST029 | PLAN | PASS_1_COMPLETE | Deviation2xNFisher andcounts/% meaningreviewed. Multiplicationsign loss islocatortext noted, not numerical candidate. |
| S094 | S-ST030 | PLAN | PASS_1_COMPLETE | Discontinuationchi-squarefrequency/reason versusdescriptiveotherflow preserved; no observed statistical output. |
| S095 | S-ST031 | PLAN | PASS_1_COMPLETE | LanDeMetsbenefitboundaries/flexiblealpha and projectedUS15/30conservatism coherentprospective rules; no observedstoppingdecision. |
| S096 | S-ST032 | PLAN | PASS_1_COMPLETE | Exactformula gamma-5.623626 reproducesalpha.0010000003/.0075178357 at1/3,2/3. Alpha=.05overall andactualinformationfractions explicit; noone/two-sidedspending conversion inferred. |
| S097 | S-ST033 | PLAN | PASS_1_COMPLETE | HarmDSMCjudgment/nofutility explicitly differentiatesstoppingtypes. No mandatoryquantitativeharm boundary manufactured. |
| S098 | S-ST034 | PLAN | PASS_1_COMPLETE | Subjectany-eventlogistic(age+treatment,siterandom) givesrisk/proportionmodel, not eventcount. No observedOR/CI. |
| S099 | S-ST035 | PLAN | PASS_1_COMPLETE | Recurrent-eventPoissonage+treatment,siterandom usesfollowuprate, notsubjectrisk; person-time/exposure values not suppliedhere. |
| S100 | S-ST036 | PLAN | PASS_1_COMPLETE | Fourpooledpatient-eventproportionsFisher test prospective; no realizedP/counts. |
| S101 | S-ST037 | PLAN | PASS_1_COMPLETE | OverallAErecurrentratePoisson/NB alternatives remainrates rather thanproportions. No observedexposure/stats. |
| S102 | S-ST038 | PLAN | PASS_1_COMPLETE | 13Jan2015 site-randomeffect amendment explicit; originalfixedsite versusfinalrandomsite is disclosedchange, not standalonecandidate. STAT-H obsoletefinalEquation1reference separate. |
| S103 | S-ST039 | PLAN | PASS_1_COMPLETE | NIamendmententry prespecifieslimit butdoesnotgive numericlimit;10%availablep61crosslink STAT-B. Missing numericalmargin onthisentry alone notcandidate. |

The canonical inventory at `statistics/relationship_inventory.md` preserves every source input and location and all constituent power cells; all 103 ID sets are identical. Pass 2 should reuse stable IDs, examine the complete cross-lane ledger and recheck, and append genuinely new candidates without renumbering. S018, S019 and S020 are specifically [results supplement PDF p13, eTable7](../../../joi190092supp1_prod.pdf#page=13), India, Site and Country interaction rows respectively; each location is REPORT by content.

## Emitted candidate observations

These are source-grounded observations for coordinator registration and mechanical direct-source recheck. Similar plan topics are not merged merely because they are nearby. Repeated original/final clauses within each observation use the same printed values/comparator/rule and preserve both locations. Coordinator assigns stableCIDs and finalclassification mechanically.

### STAT-A — Missed-dose mean/SD summaries and attached Welch P value

- **Relationship IDs:** S009
- **Primary category:** Statistical reporting inconsistency
- **Compared document roles and provisional relationship:** REPORT versus REPORT, within main article (provisional S_W).
- **Exact compared locations:** [Main p4 Statistical Analyses](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 Table2 missed-dose row and narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6). Both locations REPORT.
- **Printed evidence:** P4 states missed doses compared using a Welch t test, with two-sided P values. P6 twice prints mean(SD) percentage4.6(1.0) MTX and4.3(.5) MMF, followed by P=.87. Table main patient headern96/98 does not explicitly define adherence-test n.
- **Reproducible rule and direct observation:** For a two-sample Welch test of these participant percentages, t=(meanMTX-meanMMF)/sqrt(SDMTX²/nMTX+SDMMF²/nMMF). Any sample SD requiresn≥2. Even allowing every printed mean/SD to have rounded to nearest.1, the difference cannot be smaller than.20 and SDs cannot exceed1.05/.55, so |t|≥.23862. Welch df≥1; the conservative df1 two-sided tail is at most.8508784. Thus a same-summary Welch test cannot round to P=.87 (which would requireP≥.865). This bound does not assume actualn96/98 or any particular Welch df.
- **Derived calculation or diagnostic:** R4.5.2 pt computation confirms conservative bound. With hypothetical n96/98, t2.63445,df139.0601,P.009382747; with107/108,P.00613967. These latter values are diagnostics only, not reconstructed actual results. The direct observation is the summaries, labels and P printed together.
- **Source-grounded alternatives / missing definitions:** The dispersion may mean SE rather than SD; the Welch test may use raw dose counts, a transformed quantity, different summaries, or another analysis population. Different actualn alone does not repair the same-summary bound. None of these alternatives is confirmed by supplied evidence.
- **Exact unresolved human question:** What exact variable and analysis-setn were used in the missed-dose Welch test, do1.0/.5 label SD or SE, and doesP=.87 belong to those displayed means/dispersion values?
- **Bounded evidence-reuse implication:** A reader extracting means, SDs and P could infer a different precision or adherence comparison; no effect on primary conclusion is asserted.
- **Adjudication:** Pending Human Adjudication.

### STAT-B — Noninferiority lower-bound direction and unsigned margin in final SAP

- **Relationship IDs:** S005, S060, S103
- **Primary category:** Statistical reporting inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN for the inconsistent criterion; main REPORT is contextual corroboration, not automatically a distinct PLAN–REPORT discrepancy (provisional P_P; coordinator to classify exact comparators).
- **Exact compared locations:** [Final SAP p61 §3.2.2 item16](../../../joi190092supp3_prod.pdf#page=61); [p46 primary difference orientation](../../../joi190092supp3_prod.pdf#page=46) and [p57 treatment coding](../../../joi190092supp3_prod.pdf#page=57). All PLAN. [Main p4 NI methods/result](../../../jama_rathinam_2019_oi_190092.pdf#page=4) is REPORT context.
- **Printed evidence:** Final SAP states10%noninferiority margin and that MTX is noninferior if the lower limit of95%CI for treatment success at6months is less than10%. The plan primary aim describes difference of MMF versus MTX success fractions, but this NI clause does not name a contrast. Main printsMTX–MMF RD9.5[-5.3,21.8] and says lowerbound-5.3 excluded10%margin.
- **Reproducible rule and direct observation:** A lowerCI bound less than+10% does not establish that MTX loses less than10percentagepoints of success. If contrastMTX-MMF, lowerbound must limit negative loss; an arbitrarily negative lowerbound would still satisfy printed<+10%. If contrastMMF-MTX, the relevant loss restriction is an upperbound. If absolute MTX success alone, lower<10%also does not bound comparative inferiority. Thus the printed bound/direction/quantity is not coherent with its declared comparative loss-margin purpose.
- **Derived calculation or diagnostic:** Counterexample lowerbound-50% would satisfy<+10%forMTX-MMF while allowing far more than10%loss. This is a diagnostic logical example, not a trial result. Observed trial interval itself is compatible with reported noninferiority onMTX-MMF orientation.
- **Source-grounded alternatives / missing definitions:** The clause may contain a sign, bound-name or inequality transcription error, or describe a different unsigned loss estimand. The protocol/report's intended inferential rule and any amendment need human confirmation.
- **Exact unresolved human question:** Which contrast/quantity, signed boundary, bound endpoint and comparison direction were intended in this exact NI criterion?
- **Bounded evidence-reuse implication:** The decision-rule wording can be copied into prespecification extraction; the candidate does not claim observed noninferiority conclusion is wrong.
- **Adjudication:** Pending Human Adjudication.

### STAT-C — Historical time-to-success median assigned to the opposite hazard label

- **Relationship IDs:** S041, S066
- **Primary category:** Measure, label, or scale inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN, same bound original/final SAP (provisional P_P).
- **Exact compared locations:** [Original SAP p24 time-power item2](../../../joi190092supp3_prod.pdf#page=24), [final SAP p65 same item2](../../../joi190092supp3_prod.pdf#page=65). All PLAN.
- **Printed evidence:** Both pages define lambdaC as hazard inMTX group and lambdaI as hazard inMMF group, then say previous studies suggest median success time3.5months forMMF, but parenthetical note setslambdaC=log(2)/3.5months.
- **Reproducible rule and direct observation:** A historical median explicitly attributed toMMF is assigned tolambdaC, explicitly defined asMTX. Under the same source treatment labels, the source parameter attribution is crossed. The symmetric sample-size equation does not resolve the hazard-label identity.
- **Derived calculation or diagnostic:** No external literature used and no numeric survival fit reconstructed. Direct observed conflict is the same-page arm names and hazard symbol attribution;2.47monthpower claim not independently criticized.
- **Source-grounded alternatives / missing definitions:** Either hazard labels were exchanged, the historical drug name is wrong, or the note assigns a baseline control median intentionally but leaves that change unexplained. Symmetry may leave some power calculations unchanged.
- **Exact unresolved human question:** Should the3.5monthhistoricalMMFmedian define lambdaI, or was lambdaC/drug attribution deliberately different?
- **Bounded evidence-reuse implication:** Power assumptions or hazard-arm labels could be extracted under the wrong treatment identity; no realized trial effect contradiction asserted.
- **Adjudication:** Pending Human Adjudication.

### STAT-D — Rescue detectable difference printed as17% versus25%

- **Relationship IDs:** S042, S075, S077, S083
- **Primary category:** Numeric or arithmetic inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN inside original/final SAP (provisional P_P).
- **Exact compared locations:** [Original SAP p26 final sentence/p27 table and summary](../../../joi190092supp3_prod.pdf#page=26), [original p27](../../../joi190092supp3_prod.pdf#page=27), [final p67 formula/prose](../../../joi190092supp3_prod.pdf#page=67), [final p68 table/summary](../../../joi190092supp3_prod.pdf#page=68). All PLAN.
- **Printed evidence:** Prose claims approximately80%power to detect a difference17%ifMMFsuccess.42. The associated80%power row hasp1=.42,p0=.17,n1=58,n0=38; summary says80%power difference25%given42%success andsame58/38sample.
- **Reproducible rule and direct observation:** For the displayed80%scenario,.42-.17=.25, which is25percentagepoints, not17. The matched prose andsummary differ under the same probability/sample scenario.17%is the lower success probability inrow2, not its absolute difference.
- **Derived calculation or diagnostic:** Supplied normal-CDFformula produces80.2453%power for.42/.17and58/38; a literal17pointdifference with.42/.25produces42.8097%underthatformula. These are source-formula planning calculations, not observed trial inference.
- **Source-grounded alternatives / missing definitions:** 'difference17%' may have been intended as lower-group success17%, or the prose may refer to another scenario whoseinputs were omitted. The printed25%summary androw2give explicit comparators.
- **Exact unresolved human question:** Does17%denote the lower-group success probability or a different detectable effect, and which prose/table scenario was intended?
- **Bounded evidence-reuse implication:** The detectable effect might be extracted as17rather than25percentagepoints.
- **Adjudication:** Pending Human Adjudication.

### STAT-E — Rescue sequence sample sizes reversed between enrollment and power table

- **Relationship IDs:** S042, S073, S074, S076, S077, S078, S079, S080, S083
- **Primary category:** Denominator, proportion, or total inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN within original/final SAP (provisional P_P).
- **Exact compared locations:** [Original SAP p26 enrollmenttable](../../../joi190092supp3_prod.pdf#page=26), [original p27 powertable](../../../joi190092supp3_prod.pdf#page=27), [final p66 A/B assumptions](../../../joi190092supp3_prod.pdf#page=66), [final p67 enrollmenttable and powerheader](../../../joi190092supp3_prod.pdf#page=67), [final p68 powerrows](../../../joi190092supp3_prod.pdf#page=68). All PLAN.
- **Printed evidence:** WithAinitialsuccess60%andB40%, the expected enrollment table gives initialB/secondA58.3(complete55.4) andinitialA/secondB38.9(complete36.9). The power-tablefirstcolumns are 'DrugA,thenDrugB(number)' and 'DrugB,thenDrugA(number)', yet base rows print58and38 respectively; thusA/Bassigned58rather than38,andB/A38rather than58. Summary says58DrugA/38DrugB without stating initialversusrescue identity.
- **Reproducible rule and direct observation:** Under unchanged treatment-sequence identity, AthenBexpectedenrollment108*.9*.4=38.88andBthenA108*.9*.6=58.32. Rounding down yields38and58. Basepower-tableheaders reverse these two matched sequence samples. The lowercompletecounts includeadditionalr2.95andare separately coherent.
- **Derived calculation or diagnostic:** Direct observation is printed sequence names and58/38ordering. Arithmetic explains the expected-enrollment side; no unknown observed outcome or rawdata is required. Powerformulaarithmetic is largely coherent if one accepts its ownn/probabilityassignment.
- **Source-grounded alternatives / missing definitions:** DrugA/Bidentities may have been intentionally swapped between enrollment and power sections, or the two powercolumnheaders/values were exchanged. No such reassignment is stated in supplied plan.
- **Exact unresolved human question:** WereA/Bdrugidentities changed at the powertable, and which sequence actually receivesn58versusn38in each displayed calculation?
- **Bounded evidence-reuse implication:** Wrong sequence denominators can propagate into power/contrast extraction. This is plan-only; not a realized trial denominatorclaim.
- **Adjudication:** Pending Human Adjudication.

### STAT-F — Country-interaction test refers to absent coefficient b12 in Equation1

- **Relationship IDs:** S026, S027
- **Primary category:** Statistical reporting inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN in original SAP (provisional P_P).
- **Exact compared locations:** [Original SAP p16 Equation1](../../../joi190092supp3_prod.pdf#page=16), [p17 first sentence](../../../joi190092supp3_prod.pdf#page=17). Both PLAN.
- **Printed evidence:** Equation1 shows logit(Yi)=b0+b1Xi1+b2iZ2i+b3iZ3i+b4iZ4i, and declaresprimarynullb1=0 withone-dfLRT. P17 says treatment-countryinteraction evidence is determined byWaldT-test ofb12=0 'inEquation(1)'. No country×treatment or b12 term appears in printedEquation1.
- **Reproducible rule and direct observation:** A named model's coefficient can be tested only if that coefficient is defined in its printed model/parameterization. The b12test is assigned to an equation that lacks b12and interaction. Models(a)–(d)include exploratory interactions but are not Equation1.
- **Derived calculation or diagnostic:** This is a direct model/test-reference identity mismatch, not inferred inadequacy of a chosen model. No P/SE calculation or inference of unreported interactions.
- **Source-grounded alternatives / missing definitions:** The test could refer to exploratorymodel(d)instead ofEquation1, or an interactionterm was omitted from the displayed equation/reference.
- **Exact unresolved human question:** Which supplied model and coefficient actually define the country-interaction Waldtest calledb12inEquation1?
- **Bounded evidence-reuse implication:** A reader may map the planned interaction statistic to a treatment-only/site-adjusted model.
- **Adjudication:** Pending Human Adjudication.

### STAT-G — Zero interaction null described as a difference in efficacy

- **Relationship IDs:** S028, S054
- **Primary category:** Statistical reporting inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN inside original/final SAP (provisional P_P).
- **Exact compared locations:** [Original SAP p17 anatomical subgroup paragraph](../../../joi190092supp3_prod.pdf#page=17), [final SAP p58 same paragraph](../../../joi190092supp3_prod.pdf#page=58). All PLAN.
- **Printed evidence:** Both passages addbeta3Xi3+beta13Xi1Xi3and state hypothesisbeta13=0, followed by 'i.e.thatthereisadifferenceintreatmentefficacybetweentheanatomiclocations,controllingforcountry'.
- **Reproducible rule and direct observation:** In the printed treatment×anatomical-location model, beta13=0 means no difference in the treatment coefficient between codedanatomic groups. A difference corresponds to a nonzero interaction alternative. The equation's zero direction and its 'i.e.'interpretation conflict.
- **Derived calculation or diagnostic:** Direct observation is the zerohypothesis and supplied interpretation; algebra ofthetwoX3groups gives treatment coefficientsbeta1andbeta1+beta13. No fittedinteractionestimate required.
- **Source-grounded alternatives / missing definitions:** The words may have intended 'testwhetherthereisadifference' or todescribe thealternative rather thannull; theliteral'equivalence'needsclarification.
- **Exact unresolved human question:** Does the prose describe the nonzero alternative rather thanbeta13=0null, and how should the statedhypothesis be read?
- **Bounded evidence-reuse implication:** Prespecified null/alternative direction could be extracted incorrectly; no observedinteractionPresult disputed.
- **Adjudication:** Pending Human Adjudication.

### STAT-H — Final subgroup model refers to superseded Equation1

- **Relationship IDs:** S053, S054, S059
- **Primary category:** Measure, label, or scale inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN within same bound SAPversions (provisional P_P).
- **Exact compared locations:** [Final SAP p57 primary model](../../../joi190092supp3_prod.pdf#page=57), [p58 subgroup 'beginwithEquation(1)'](../../../joi190092supp3_prod.pdf#page=58), [original p16 actualEquation1](../../../joi190092supp3_prod.pdf#page=16), [final p60–61 BayesianEquation1reference](../../../joi190092supp3_prod.pdf#page=60). All PLAN.
- **Printed evidence:** Finalprimarymodel uses treatmentpredictor andstudy-site random intercept, without a displayed numberedEquation1. Finalsubgroup says 'beginwithEquation(1)' andaddanatomy/interactionterms. The supplied boundbundle'sEquation1is originalp16fixedsite regression. BayesianfinalitemalsoreferstolikelihoodcorrespondingtoEquation1.
- **Reproducible rule and direct observation:** The final reference does not identify a final numberedmodel matching its own random-siteprimary specification; literal suppliedEquation1hasfixedsitecoefficients. The reference therefore points to a different printed model identity. The disclosed fixed-to-random amendment itself is not thecandidate.
- **Derived calculation or diagnostic:** Observation is old-equationreferent and finalchangedmodel, not a broad critique ofrandomversusfixedeffects. No claim that the reportedanalysis followed theoldmodel.
- **Source-grounded alternatives / missing definitions:** The author may have intended 'thefinalprimarymodel' while retaining an old equationlabel, or deliberately intended a fixedsite subgroupalternative. No explicit mapping supplied.
- **Exact unresolved human question:** Does final 'Equation1' mean the final random-intercept primarymodel, originalfixedsiteformula, or a separate subgroup/Bayesianmodel?
- **Bounded evidence-reuse implication:** A reader mapping subgroup model-adjustmentlabels may assign wrong site treatment/covariate structure.
- **Adjudication:** Pending Human Adjudication.

### STAT-I — Twelve-month 'same Wald procedure' conflicts with primary LRT/null definition

- **Relationship IDs:** S026, S029, S053, S055
- **Primary category:** Statistical reporting inconsistency
- **Compared document roles and provisional relationship:** PLAN versus PLAN inside original/final SAP (provisional P_P).
- **Exact compared locations:** [Original SAP p16 primarytest](../../../joi190092supp3_prod.pdf#page=16), [original p18 twelve-monthitem1](../../../joi190092supp3_prod.pdf#page=18), [final p57 primarytest](../../../joi190092supp3_prod.pdf#page=57), [final p58 twelve-monthitem1](../../../joi190092supp3_prod.pdf#page=58). All PLAN.
- **Printed evidence:** Bothprimarysections define null treatmentcoefficient=0 andone-dfLRT; finalprimarysite-random model has no anatomyinteraction. Both12monthsections say same statisticalmodel '(andWaldprocedure)' asprimary, then jointnulltreatment andtreatment/anatomyinteractionbothzero.
- **Reproducible rule and direct observation:** LRT andWald are separately named procedures. The asserted same-primary Wald identity doesnotmatchprintedprimaryLRT; jointtreatment+interactionnullalso differsfromtheprintedone-treatmentcoefficientprimarynull/model. This is a concrete test/modelidentity mismatch in the source's own 'same' claim.
- **Derived calculation or diagnostic:** No equality ofrealizedPvalues assumed. A single model may be analyzedby bothLRTandWald, but theplandoesnotidentify a primaryWaldprocedure orclarify changedjointcontrast inthisclaim.
- **Source-grounded alternatives / missing definitions:** 12monthmay intentionally useWald onanexpandedanatomicalinteractionmodel, with thephrase 'same' retainedfromolderdraft; permutationPprimarymay supplementLRTbutdoesnotbyitselfsupplythisWaldjointtest.
- **Exact unresolved human question:** Which model andjointcontrast define the12monthtest, and doesWald apply thereas a deliberatelydifferentprocedurefromprimaryLRT?
- **Bounded evidence-reuse implication:** Future analysis/test-label extraction may misidentify the planned12month test; observed12monthPresults not declared wrong.
- **Adjudication:** Pending Human Adjudication.

### STAT-J — Dose-reduction exact Fisher P and printed hundredth

- **Relationship IDs:** S012
- **Primary category:** Statistical reporting inconsistency
- **Compared document roles and provisional relationship:** REPORT versus REPORT within main article (provisional S_W).
- **Exact compared locations:** [Main p4 Fisherexact/two-sidedmethods](../../../jama_rathinam_2019_oi_190092.pdf#page=4), [p6 dose-reductionnarrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6). Both REPORT.
- **Printed evidence:** 21patients(19.6%)ofMTX107and15(13.8%)ofMMF109reducedstudymedication,P=.27; methodsspecifyFisherexacttest andtwo-sidedstatisticalsignificance;Rversion3.51listed.
- **Reproducible rule and direct observation:** Using displayedcounts/denominators, standardprobability-ordering two-sidedFisher on[[21,86],[15,94]] givesP=.276681552. Nearesthundredth is.28rather than.27. This is a conditional exact-result/precisionmismatch, not a claimP=.27changes significance.
- **Derived calculation or diagnostic:** R4.5.2 fisher.test reproduces.2766816; auxiliaryJSlogcombinations independently gives.276681552. IfMMFexposure108instead109,exactP=.2784668,alsonearest.28. Doubleminimumone-sided conventiongives.3302382,not.27. Display precision/truncation andoriginalRcallare unprovided.
- **Source-grounded alternatives / missing definitions:** Pmay have been truncated rather thanrounded;anotherconditionaltailconvention oranalysisinclusionmay be used. The source doesnotexplicitlypromise nearesthundredthrounding orlistanalysisnfor thiscomparison beyond displayedproportions.
- **Exact unresolved human question:** What exact2x2table,Fisher-taildefinition andprinting/roundingrule producedP=.27from21vs15dose reductions?
- **Bounded evidence-reuse implication:** A smallPprecisiondifference could propagate intostudyextraction; no significance/conclusion change asserted.
- **Adjudication:** Pending Human Adjudication.

## Non-candidate checks and limits

All displayedreportOR/RD95%CIs are ordered andcontain theirpointestimates; effectdirections agree withreference/narrative. Significant/nonsignificant interpretations are coherent atstated.05exceptthe separately registered summary/label/test-referenceobservations. Figure2/abstract/table/narrative repeatsagree afterrounding. Supplementinteractions.15/.20/.45are notsimpleeffecttestsandnotinventedduplicatesbecauseprimaryPcoincidentallyequals.20.

The provided seven rescuepowerrowvalues are allcovered. Formularesults87.4165,80.2453,82.8952,94.0835,95.5020,80.0441,82.3322percentarepreservedwithall35cellsineachversion. Lastcoarselyapproximate80%rowisnotregistered solelyforits2.3pointapproximation. Primarypowertarget216versusnormalapprox218after10%lossislikewisecompatibleapproximateplanning,notanindependentcandidate. Alpha-spendingfunctionyieldsexact.0010000003/.0075178357consistentprinted.001/.0075.

Missinginferentialdefinitions: adherenceactualn/testvariable/SD-versus-SE; conditionalFisher-tail/printingpolicy; mixedsitevariance/CIinversion/permutationstatistic; interactioncoefficients/SE/df; eyeclustercovariance/df; MIreplicateestimates/poolingdf; powercriticalvalue/correctionandmedianversusmeanmapping. No sidedness,df,covariance,varianceestimator,multiplicity,denominator,modelorcontrastwasinventedfromconvention. These limits do notomitanyassignedrelationshipandarenotstandalonecandidates. Unobservedprospectiveoutcomeoutputs cannotbeinferred.

Allsuppliedsource/reusedderivativespreserved. No GPU,network,externaldataoroldconclusionused. TemporaryPythonenvironmentnotneededbyrecordedprobe.

