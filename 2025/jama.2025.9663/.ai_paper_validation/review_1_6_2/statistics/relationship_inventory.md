# DOC-001 Inferential Statistical Relationship Inventory

Scope REPORT main article, physical PDF pp1-11. Every estimate is C versus U. RD units percentage points; RR/OR/POR/HR/sHR ratio units, null1; RD/difference null0. All printed CIs95%, tests2-sided alpha.05 unless interim. Rows explicitly retain both available-case and imputed estimates. No checker assessments or candidate judgments are made. For every result row, assessment hooks are point containment, ordered limits, null/printed-P compatibility where a P is supplied, direction against labels and narrative, and matching population/time/model. P values belong to the displayed outcome row, not automatically to each alternate effect measure. No printed standard errors or test statistics are present. Diagnostic Wald calculations must not replace the reported multilevel/imputed analyses.

| ID | Exact location | Required inputs / reported relationship | Assessment hooks and named missing definitions |
|---|---|---|---|
| S001 | p2 randomization; p3 analysis; p8 Table2 footnotea; p9 Figure3 footnotes | Individual1:1 stratified site/diagnostic subgroup variable blocks; unblinded; analysis by randomized group. Models account site clustering; diagnostic stratum, COVID, age, SpO2, PaO2:FiO2, date; Table2 specifies restricted cubic splines for age/SpO2/ratio/date; Figure3 calls adjusted multilevel logistic | Check design/analysis specification consistency and supplied PLAN comparison; main does not print spline knots or site variance specification. |
| S002 | p3 Sample Size Calculations | Usual risk .37, C.345; ARR.025; loss .06; n16500; 90% power; P<.05; allocation 1:1; two-sided convention | Reproduce independent two-proportion sample-size inputs with source methods; no printed sample-size formula / continuity correction. |
| S003 | p3 Sample Size Calculations | Interim after4500 and10000 participants; Haybittle-Peto P<.001 effectiveness / harm | Match stopping threshold/timing to PLAN; no interim statistic printed in article. |
| S004 | p3 analysis | Tests2-sided P<.05; effects95%CI; no multiple testing adjustment | Outcome status and multiplicity rules against supplied plan; do not infer multiplicity-adjusted CIs. |
| S005 | p3 outcome measures/analysis; p8 Table2 | Binary mortality logistic; RD/RR marginal standardization; durations among survivors Fine-Gray with death competing risk; organ-support days ordered logistic | Effect-measure identity; do not equate adjusted model outputs to crude count contrast. |
| S006 | p3 analysis; p6 outcomes; p8 Table2 footnoteb | MICE missing data with≥primary outcome auxiliary for secondary; baselinePaO2:FiO2 singly imputed fromSpO2:FiO2; other adjustment variables complete; duration missing discharge censored1h afterrandomization rather than imputed | Map outcome-imputation and covariate-imputation distinct processes; details/count imputations not printed in main, supplied eMethods/PLAN comparison needed. |
| S007 | p3 outcome measures; p8 Table2 footnotec | Primary all-cause90d mortality; secondaryICU/hospital duration and discharge mortality censored90d; organ support30d; 60d/1y mortality; death≤30d score−1 | Match status/time/composite components toPLAN; health-economics separately reported. |
| S008 | p3 analysis; p9 Figure3 | Prespecifieddiagnosis/COVID/ethnic subgroups; repeat adjusted primary model plus treatment×subgroup; multinomial joint interaction onOR scale | Reported interaction P values correspond omnibus group effects, not within-row treatment tests. |
| S009 | p3 analysis; p6 subgroup discussion; p8 discussion | Posthocseverity tertiles predicted death/APACHEII, PaO2:FiO2 categories, collection subset; prespecifiedmachine-learning heterogeneity separatelyreported; no significant severity interactions; weakharm first10/site, no difference randomenhanced versusstandard | Status/link map to eFigure7 and suppliedPLAN; no quantitative posthoc subgroup estimates printed in main. |
| S010 | p1 abstract; p6 outcome/discussion; p8 Table2 90d RD | Available case RD .7(−.6,2.1); imputed RD .7(−.7,2.0); P.28; observed countsN005; crudeunadjusted narrativeRD.5(−1.0,2.0) | Compare imputed abstract/narrative/Table2; RDpositive described increase; CI from.7pp decrease to2.0pp increase; do not compare adjustedRDdirectly withcrude. |
| S011 | p8 Table2 90d RR | Available case RR1.02(.98,1.06); imputed RR 1.02(.98,1.06); outcome P .28 | Marginal standardization logistic; alternate effect measure same primary outcome. |
| S012 | p8 Table2 90d OR | Available case OR1.04(.97,1.11); imputed OR 1.04(.97,1.11); outcome P .28 | Logistic odds ratio; rounded alternate measure vsRD/RR. |
| S013 | p6 oxygen exposure; p7 Figure2C | Exposuredifference−8.4h(−10.8,−6.0); C20.3/U28.7; 29.3%reduction | CI excludes0; no associated printed P ; supplementeTable5 required model/CI definition; different result frommortality. |
| S014 | p8 Table2 ICU survivor duration | Available case sHR 1.00(.96,1.04); imputed sHR 1.00(.96,1.04); P.97; mediansN066 | Deathcompetingrisk; missingdurationcensor1h; survivor descriptives not direct inferential model inputs. |
| S015 | p6 outcomes; p8 Table2 hospital survivor duration | Available case sHR .98(.94,1.02); imputed sHR .98(.94,1.02); P.27; narrativecallsHR.98(.94,1.02) | Fine-Gray label Table 2 and generic narrative hazard ratio; survivormediansN067. |
| S016 | p6 outcomes; p8 Table2 organ-support-free days | Available case POR1.00(.95,1.06); imputed POR 1.01(.96,1.07); P.64 | Ordinal death −1/positive days composite; ranked day1-30; mediansN068/30ddeathsN069. |
| S017 | p8 Table2 ICU discharge mortality | Available case RD .2(−1.2,1.6); imputed RD −.1(−1.3,1.1); P.94; countsN070 | Same adjustment as primary; imputation vsobserved populations; RD sign differs betweenmodels but both retained. |
| S018 | p8 Table2 acutehospitaldischarge mortality | Available case RD .9(−.6,2.3); imputed RD .5(−.8,1.9); P.46; countsN071 | 90dcensor; imputed model. |
| S019 | p8 Table2 60dmortality | Available case RD 1.1(−.2,2.5); imputed RD .8(−.6,2.2); P.25; countsN072 | Secondary linkage population; count/percentage and null compatibility. |
| S020 | p8 Table2 1ymortality | Available case RD 1.0(−.7,2.6); imputed RD 3.3(−.7,7.3); P.34; countsN073 | Distinguish completecase and imputation; one-year availability limited by administrative timing N016; exact imputed SE not printed. |
| S021 | p3 analysis; p6 time-to-death | Cox adjusted HR 1.01(.96,1.05); censor earliest withdrawal,365d, trial end; no P printed | Crossreference eFigure4 asprinted; source outcome/model must match actual supplement figure; site cluster / covariates S001. |
| S022 | p1 abstract; p2 KeyPoints; p6 discussion; p9 conclusion | Conservativeoxygen did not significantly reduce 90dmortality; no significant secondary differences; 95%CI−.7to2.0 excludes hypothesized −2.5 pp | Match statedclinicalconclusion to RD/interval/superiority criterion; no NI / equivalence margin stated. |
| S023 | p9 Figure3 HIE | RD−1.3(−6.2,3.6); OR.94(.76,1.17); countsN074 | Adjustedprimary subgroup model; negative RD favors C; OR <1 favors C. |
| S024 | p9 Figure3 sepsis | RD.9(−1.6,3.3); OR1.04(.93,1.17); countsN075 | Direction / null / containment; not individual-row P. |
| S025 | p9 Figure3 acute brain injury exceptHIE | RD−3.2(−12.8,6.5); OR.86(.56,1.34); countsN076 | Direction / null / containment. |
| S026 | p9 Figure3 none | RD1.0(−.8,2.8); OR1.05(.96,1.16); countsN077 | Direction / null / containment. |
| S027 | p9 Figure3 diagnosis interaction | P.67 forfour-category diagnostic group; figureORaxis.4,.7,1,1.4,2.5; leftfavorsC, rightU | Joint OR-scale interaction  null vsheterogeneity; no printed statistic / df. |
| S028 | p9 Figure3 COVID no | RD1.0(−.4,2.4); OR1.05(.98,1.13); countsN078 | Direction / null / containment. |
| S029 | p9 Figure3 COVID yes | RD−3.7(−9.3,2.0); OR.85(.66,1.09); countsN079 | Direction / null / containment. |
| S030 | p9 Figure3 COVID interaction | P.11 | Treatment×binaryCOVID interaction; no statisticprinted; no assumptionrowCI correspondsinteractionP. |
| S031 | p9 Figure3 ethnic Asian | RD1.9(−6.1,9.9); OR1.10(.74,1.63); countsN080 | Adjusted, not crude; direction/null/containment. |
| S032 | p9 Figure3 ethnic Black | RD−6.1(−15.7,3.4); OR.71(.41,1.22); countsN081 | Direction / null / containment. |
| S033 | p9 Figure3 ethnic White | RD1.3(−.3,2.9); OR1.07(.99,1.15); countsN082 | Direction / null / containment. |
| S034 | p9 Figure3 ethnic Mixed | RD−0(−15.0,14.9); OR1.00(.39,2.52); countsN083 | Retain printed −0; wide CI  arrows beyond plot range; no inferred rounded unprinted effect. |
| S035 | p9 Figure3 ethnic Other/not stated | RD−.3(−4.6,4.1); OR.99(.79,1.23); countsN084 | Direction / null / containment. |
| S036 | p9 Figure3 ethnic interaction | P.64 | Joint OR-scale interaction  fivegroups; no statistic / df printed. |
| S037 | p6 exposure narratives; p7 Figure2; p8 discussion; p9 limitations | LoweroxygenC maintainedovercalendartime/sequence/enhancedsubgroups; smallerseparationthanothertrials; noevidencecontamination | Source links eFigures2/3/4, eTables5/6/10; no claimthat achievedmeanSpO2equalsnominal90%target. |
| S038 | p6 adverseevents | C58(.7%), U29(.4%) seriousadverseevents; no significance test printed | No inferred P  or comparison claim; populationN061; eTable9link. |
| S039 | p2 consent; p4 analysispopulation; p8 imputationfootnote | All-data removal 66 excluded; unlinked primary 40 retained / imputed; secondary requires linkage consent | Analysispopulationdefinitions vsrandomizedN013-016; do not count missing as removed. |
| S040 | p4 software | Stata/MP 18.0 | Reproduction provenance; not an independentmethodconflict. |
# Statistical relationship inventory — support

Scope DOC-003 REPORT pp1–29; DOC-002 PLAN pp1–28.37 relationships. Full printed data are incorporated by reference to the complete page-level transcriptions and image-clarified table in extraction/support_quantitative_evidence.md. No statistical check outcome or candidate is assigned at mapping. Nulls mean/RD0,OR/HR1; intervals95% unless source states otherwise. Two independent later statistical passes must cover every ID. All matching keys compare same outcome/population/window/adjustment only.

| ID | Source role and exact location | Mapped statistical relationship | Inputs, matching key and named limits |
|---|---|---|---|
| S1001 | REPORT DOC-003p2,eMethods | Patientmedian exposure summarized by meanSD,medianIQR; C−U differences95%CI; absolute/percentage totaldose difference | All13rows eTable5,all26group-specificrows eTable6; mainoxygenexposure; no specific CI estimator stated here |
| S1002 | REPORT DOC-003p2,eMethods | First10dayadherence:oxygen>.21,SpO2>92%,failureFiO2reduction≥3consecutivehours;TMGreview/sitejustification;usualarmnotassessed | Target88–92%; prospective treatment finalversion matching required |
| S1003 | REPORT DOC-003pp3–5 | Deferredconsent, retaineddata and primary-only data population; lacklinkagepreventssecondaryoutcomes | NumericN1003; distinguishes primaryITT/secondarymissingness; removesall-datawithdrawals |
| S1004 | REPORT DOC-003p6 | Primary90dayallcausedeath; competingdatasourcesvalidatewithsiteparamount; otherwise anylinkeddeath and civilregistrationdate | Mainprimaryendpoint90day |
| S1005 | REPORT DOC-003p6 | SecondaryICU/hospitaldeathcensored90day;60day/1yeardeath;one-yearbinaryexcludesnoreachedyear | Compare binary1year population to time-to-event eFigure5 with censoredshortfollowup,not assume equal |
| S1006 | REPORT DOC-003pp6,7 | ICUstaylinearhours plus subsequentICUadmissionssameacutestay;hospitalcalendar-daydurationfromrandomization;death/discharge endpoints | Mainstaymodel,timeunits; no observedmean equals survivalestimate assumption |
| S1007 | REPORT DOC-003p7 | Organfreeordinaldeath≤30day=−1;survivorfreecalendardays1–30;anyresp/cardio/renal;outsideICUfree;CMP3.1assumessupportatstart,totalmaxsupporttotals≤30 | MainordinalOR and eFigure6/eTable8; no summing organ-specificdays |
| S1008 | REPORT DOC-003p10,eFigure3 | Meanexposuretrajectoriesfirst10days overallandoxygenconditional; allcontributorsN1006 | PrintedN2489 and pertimecounts different quantities; graphpoints not exact numeric |
| S1009 | REPORT DOC-003p11,eFigure4 | Runninglinesmoother mean(patientmediansfirst10days),95%CI,calendardate/sequencewithin-site | ConditionaloxygenSpO2,FiO2; mainseparation; bandwidth/modelunstated |
| S1010 | REPORT DOC-003p12,eFigure5 | HR1.01(.96–1.05),P=.82;allrandomizedminus66;KMplotonlylinkageconsent;right/interval/leftcensoring | N1008completevectors;342(2.1%)deathsunknownexacttime intervalwithdrawal→90day orleft90day;reverseKM365(277–365)/365(292–365); interval includes1; printedroundedtestinputs not exactvariance |
| S1011 | REPORT DOC-003p13,eFigure6 | CDFordinalorganfree C7327/U7444;greaterCDFlessfavorable;death−1first;stackedblueworse/yellowbetter | N1009andS1007; no independent printedOR/P |
| S1012 | REPORT DOC-003p14,eFigure7 | Posthocrisktertiles all3rows adjustedRD/OR95%CI;interactionP.18 | N1010complete rows; notcrudeOR;covariatessite,diagnostic,age,SpO2,PaO2/FiO2,COVID,date |
| S1013 | REPORT DOC-003p14,eFigure7 | PosthocAPACHEtertiles all3rows adjustedRD/OR95%CI;interactionP.98 | N1010;Cmiddle794/2140(37.1),not1794fromOCR |
| S1014 | REPORT DOC-003p14,eFigure7 | PosthocPaO2/FiO2≤100,>100–≤200,>200–≤300,>300 all4rows adjustedRD/OR95%CI;interactionP.36 | N1010; imputedratio comparison may alter rowdenominators; adjustmentformula matchescaption |
| S1015 | REPORT DOC-003p14,eFigure7 | StandardRD+.6(−.8,+2.1),OR1.03(.96–1.11);randomRD−2.6(−7.1,+2.0),OR.88(.70–1.10);interactionP.18 | N1010;standardreferenceforinteraction;allcountspercentpresent |
| S1016 | REPORT DOC-003p14,eFigure7 | First10RD+7.3(+1.5,+13.1),OR1.43(1.08–1.90);interactionP.03 versusstandard | N1010;200/486(41.2)vs159/465(34.2);Pinteraction distinct from contrastCI |
| S1017 | REPORT DOC-003p20,eTable4footnotes | DiagnosticstratificationhierarchicalHIE→sepsis→brainexceptHIE;atmostone;ICNARC2023risk/APACHEphysiologyfirst24h exceptPaO2/FiO2lastrandomization | Preserve displayeddiagnosticrowsN1014;APACHE0–71higherworse;covariatesandlabelsmatching |
| S1018 | REPORT DOC-003p21,eTable5 first8rows | FiO2overall−.04(−.05,−.03),oxygen−.02(−.03,−.01);SpO2overall−1.8(−2.0,−1.6),oxygen−2.0(−2.2,−1.8);SaO2−1.4(−1.6,−1.2),oxygen−1.6(−1.8,−1.4);PaO2−8.0(−9.3,−6.7),oxygen−7.6(−9.3,−5.9) | N1015fullmeanSD/medianIQR/No;C−U;meanofpatientmedians,notpooledhourmeans;95%CI methodnot specifiedhere |
| S1019 | REPORT DOC-003p21,eTable5 durationrows | Roomairabove92%+13.6(9.6,17.6)h;oxygenabove92%−54.0(−58.8,−49.2);target88–92%+35.5(31.4,39.6);below88%+.9(.4,1.4) | N1015C/UmeansSD/ns;allNo1234/1216;windowsfirst10daysorstop |
| S1020 | REPORT DOC-003p21,eTable5dose | Dose20.3(27.4)[1234]vs28.7(31.9)[1216];C−U−8.4(−10.8,−6.0),percent−29.3(−37.6,−20.9),Ureference | DoseequivalenceS1001; percentdenominatorUmean;median8(2–28)/16(6–40) |
| S1021 | REPORT DOC-003p22,eTable6 | First10andrandom9exposure rows,allmeanSD/medianIQR/n/differences95%CI fullytranscribed;C/Uheaders486/466,766/771 | SpO2,FiO2,SaO2,PaO2overall/oxygenconditional androomairtime;N1016; first10FiO2conditional printed−.02(−.04,−.00) preservesdisplayzero |
| S1022 | REPORT DOC-003p23,eTable6continuation | Remainingoxygenabove92%,target,belo88%,doseabsolute/percentrows allvalues;first10dose−9.2(−13.4,−5.0),−29.5(−42.9,−16.0)%;random−7.9(−10.7,−5.1),−29.0(−39.3,−18.8)% | N1016;fullrowsn480/456and754/760;weighted aggregationusesdifferentavailableN,notheaderN |
| S1023 | REPORT DOC-003p24,eTable7 | Missingprimary40(.2)logitauxhospitalduration;ICUdeath1647(10)logitaux90day;hospitaldeath1641(10)logitaux90day+hospitalduration;60day1412(8.6)logitaux90day+1year;1year1661(12.7)of13052logitnoaux;organfree1639(10)orderedlogitaux90day+ICUdeath | Allimputationmodelsincludeassignedarm,age,diagnosticstratum,COVID,SpO2,PaO2/FiO2,date;N1017; MIreplication/countsfrommain/SAPoutsideassignedsource |
| S1024 | REPORT DOC-003p24,eTable7footnote,reference9p28 | PaO2/FiO2missing1176(7.2)singlyimputedfromSpO2/FiO2usingBrown2016formula;ethnic1630(9.9)notimputed,completeethnic-onlysubgroupanalysis | Formulaidentifiedbyreferencebutnotalgebraicallyprinted;noexternalreading/inferredcoefficients |
| S1025 | REPORT DOC-003p24,eTable7footnote | MissingICUstay1653(10.1)includedandcensoredat1hour;missinghospitalstay1677(10.2)includedandcensoredat1day | Distinguishmissingness-censoringfromeventdeath andplannedcompetingriskanalysis |
| S1026 | REPORT DOC-003p25,eTable8 | Allcontinuoussecondarydescriptives groupedoverall/survivors/nonsurvivors;ICU7333=5211+2122/U7448=5290+2158;hospital7323=4791+2532/U7434=4906+2528;organfreeN7327/7444survivors4933/5054;deathscore−1 | N1018retainsallmeanSD/medianIQR;meanordinalscorevsmodelfittedORnotdirectequivalence |
| S1027 | REPORT DOC-003p26,eTable9 | SafetytimefromrandomizationtoICUdischarge/90daywhicheverfirst;C8230/U8204;anyuniqueSAE58(.7)/29(.4),eventsandpatientsseparatecolumns | AllN1019rows;patientsoverlapacrossSAEs;notaddrowpatientsasuniquetotal |
| S1028 | PLAN DOC-002pp7,16 | Eligibilityadult≥18,MVunplanned/startICU,FiO2>.21,within12hours;excludepriorrandomization90days/ECMO/clinicalarmcontraindication | Maineligibilityandpopulationdefinitions;originalv1.1 |
| S1029 | PLAN DOC-002pp8,14,15 | Originalclinicalprimary90dayall-cause;secondaryICU/hospitaldeath90day,60day,1year,ICU/hospitalstay90day,HrQoL90day;economiccost/QALY/NMB90dayprimary | Comparefinalprotocol/SAPamendmentsbeforeclassifying;organfreedaysnotlistedintheseoriginalsummary/objectivepages |
| S1030 | PLAN DOC-002p14 |16500,90%powerforARR2.5%90daymortality;clinicalsuperiorityquestion | Detailedsampleinputsnotinpp1–28;laterplanmapperprovidesalpha/baseline/loss;nofreshsamplecalculationfromincompleteinputs |
| S1031 | PLAN DOC-002p17 | Individual1:1centraltelephone/web;randompermutedvariableblocks;stratifiedsite,HIE,sepsis,acutebrainpathologiesexceptHIE | Matchingmainrandomizationandadjustmentstrata;diagnostichierarchylaterREPORTfootnote |
| S1032 | PLAN DOC-002pp18–20 | Deferredconsent;dataretainedbeforewithdrawalunlessremovalrequested;continuedrecordfollowuppermissionasked | ComparisonREPORTprimary-onlyfollowup/noremoval;noassumedsamealloutcomeN |
| S1033 | PLAN DOC-002pp20,21 | OriginalconservativeSpO290–93%,lowestoxygenat/justabove90%,alarms89/94%;usualdailyclinicaltargetnoupperalarm;continuespostextubation/90dayorICUdischarge,restartreadmission;exceptionsspecified | FullN1031,N1032;sourceversionexplicit,final/amendmentcomparisonneeded |
| S1034 | PLAN DOC-002pp22–25 | ECMO/HBOTterminatesintervention;SAEdefinition+expectedallpatient90day/ICUwindow;unexpectedoxygenrelatedonly;deathseparateoutcome | N1033–35; mainseriousadverseevent ascertainment |
| S1035 | PLAN DOC-002pp26,27 |14000basic/2500enhanced(15%patients),85%routinefields;first10/siteprospectiveenhancedthenrandomretrospectiveacrosssites/arms/time;enhancedsurvivorsHrQoL/resource90day | N1036,N1037;samplingmethodversus eTable4/6 headers;formulascachedvaluesnotapplicable |
| S1036 | PLAN DOC-002p28 | Internalpilotmonths7–12 includedfinalanalysis;trafficlightsite/recruitmentdecisionrule | Green>50sites/≥75%recruit;amber20–50/40–75%;red<20/<40%;notstatisticalinterimstoppingrule |
| S1037 | PLAN DOC-002p28 | PilotseparationSpO2≥3%,1.5–3%,<1.5% ORFiO2≥.1,.05–.09,<.05;adherence≥75%,50–75%,<50%;perprotocoladjustments | N1039;progressioncriteriaexactlyretained;boundaryconventionnotinvented |

Missing definitions are locators for later checkers, not standalone observations. Numeric and statistical record scopes cover each complete table rather than limiting the number of findings.
# Inferential-statistical relationships: plan-b

Scope: DOC-002 PLAN physical PDF pages 29–56. Seventeen S relationships mapped. These are design inputs for both independent statistical passes, without checker conclusions. Every paragraph was visually read from the source-linked hashed image. Complete page mapping and full transcription appear in extraction/parts/plan-b.md. Links refer to the exact supplied source, not printed footer numbering.

| ID | Exact PLAN location | Source-grounded statistical relationship | Inputs and matching key |
|---|---|---|---|
| S2001 | [PDF29](../../../joi250042supp1_prod_1753377747.92525.pdf#page=29), v1.1 §4.1 | Reduction from 37% to 34.5% 90-day mortality, 2.5% absolute and 6.8% relative reduction, 90% power requires 15,444 total; 6% allowance leads to 16,500 recruitment | Sample size and power; N2002. Test family, significance level and allocation ratio not specified in this paragraph. |
| S2002 | [PDF29](../../../joi250042supp1_prod_1753377747.92525.pdf#page=29), §4.2.1 | Pilot months 7–12 analyzed month 14; all green progresses unchanged, any amber amends, any red stops; NIHR HTA decision after TSC recommendation | Progression decision logic; threshold definitions elsewhere must be joined by coordinator. |
| S2003 | [PDF29](../../../joi250042supp1_prod_1753377747.92525.pdf#page=29) and [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), §4.2.2 | A priori SAP before investigators unblinded to study outcomes; all analyses intention to treat; baseline balance comparisons without statistical testing | Prospective status and analysis population. |
| S2004 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), primary outcome paragraph | Stratification-only and additional baseline-adjusted analyses; primary includes stratification variables and other prespecified risk factors; regression with site random effects; absolute risk reduction and relative risk reported | Stratification: site, hypoxic-ischaemic encephalopathy, acute brain pathologies excluding that encephalopathy, sepsis. Primary 90-day mortality model and measures. |
| S2005 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), covariates | Additional covariates selected a priori based on established outcome relationship, not imbalance, univariable significance or stepwise selection | Selection rule; no additional covariate names here. |
| S2006 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), secondary outcomes | Binomial/Poisson family for binary and normal family for continuous outcomes; lengths of stay by Wilcoxon rank-sum stratified by survival; Kaplan–Meier and Cox with shared site frailty | Secondary mortality, duration and survival analysis models. |
| S2007 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), subgroup paragraph | Treatment-by-subgroup interaction in adjusted primary regression; a priori key subgroups: suspected hypoxic-ischaemic encephalopathy, acute brain injury excluding that encephalopathy, sepsis | Primary 90-day mortality subgroup status and models. |
| S2008 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), interim paragraph; [PDF32](../../../joi250042supp1_prod_1753377747.92525.pdf#page=32), §6.1.1 | Two analyses after recruitment and 90-day follow-up of 4,500 and 10,000; Peto–Haybittle P<0.001 for effectiveness or harm; further analyses if DMEC requests. Closure section repeats thresholds and rule, referring to follow-up. | Interim and stopping correspondence. Sidedness and final multiplicity adjustment not stated here. |
| S2009 | [PDF30](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30), §4.2.3 | ITT economic conservative-vs-usual comparison; validated regression predicts resource use for all from 15% detailed monitoring and questionnaires; health/personal-health-services perspective, CMP/HES linkage, 90-day horizon | Economic population, sampling and prediction; N2004. |
| S2010 | [PDF31](../../../joi250042supp1_prod_1753377747.92525.pdf#page=31), QALY/NMB | EQ-5D-5L at 90 days measured in 15%, predicted for all; survivors' baseline utility zero, linear interpolation to day 90; decedents before day 90 zero QALYs; NMB values QALY gains at £20,000 per QALY minus incremental cost | Economic derived-measure identity and survival handling; N2005. |
| S2011 | [PDF31](../../../joi250042supp1_prod_1753377747.92525.pdf#page=31), CEA model | ITT mean 90-day incremental costs, QALYs, NMB with 95% CI; multilevel linear regression accounts for site clustering and patient/site baseline covariates; extensive sensitivity analyses and all clinical subgroups | Economic model, confidence level and sensitivity/subgroup status. Specific sensitivity definitions absent from paragraph. |
| S2012 | [PDF31](../../../joi250042supp1_prod_1753377747.92525.pdf#page=31), lifetime projection | Initial hospital survivors and same-unit readmissions to 90 days; excess mortality/utility relative to age/gender-matched population; later use population values; day-90 morbidity costs projected through excess-mortality period; lifetime increments | Lifetime economic extrapolation definition and population. |
| S2013 | [PDF48](../../../joi250042supp1_prod_1753377747.92525.pdf#page=48), v1.8 summary; [PDF54](../../../joi250042supp1_prod_1753377747.92525.pdf#page=54) and [PDF55](../../../joi250042supp1_prod_1753377747.92525.pdf#page=55), objectives | Primary 90-day all-cause mortality; secondary 30-day days alive/free organ support, ordinal with death worst, respiratory/cardiovascular/renal CCMDS support; other clinical secondary outcomes and economic primary outcomes listed fully in N2011 | Updated endpoint status, horizon, composite definition and ordinal ordering. Original version N2001 mapped separately. |
| S2014 | [PDF53](../../../joi250042supp1_prod_1753377747.92525.pdf#page=53), rationale | CMP 96,028 MV of 337,312 admissions, 34% hospital mortality, anticipated 37% at 90 days; historical pooled RR 0.91 (95% CI 0.75–1.09) with uncertainty stated | Planning-risk provenance; historical interval distinct from current trial result; N2014. |
| S2015 | [PDF54](../../../joi250042supp1_prod_1753377747.92525.pdf#page=54), §1.4 | Standalone 16,500 UK-ROX powered 90% for 2.5% absolute 90-day mortality reduction; planned individual-patient meta-analysis with Mega-ROX; UK-ROX secondary hospital mortality harmonizes with Mega-ROX primary | Standalone power versus prospective pooled analysis; endpoint correspondence; N2010. |
| S2016 | [PDF54](../../../joi250042supp1_prod_1753377747.92525.pdf#page=54), §2.1 | Explicit question whether conservative oxygen is superior to usual oxygen for 90-day all-cause mortality in non-elective adults with MV and supplemental oxygen | Superiority direction and current contrast; no noninferiority margin stated. |
| S2017 | [PDF47](../../../joi250042supp1_prod_1753377747.92525.pdf#page=47), summary; [PDF55](../../../joi250042supp1_prod_1753377747.92525.pdf#page=55) and [PDF56](../../../joi250042supp1_prod_1753377747.92525.pdf#page=56), design/population | Individual randomization; adults ≥18, invasive MV after unplanned admission OR intubated in ICU, FiO2>0.21, enrolment within 12 hours; excludes prior randomization within 90 days, ECMO and clinician indication/contraindication | Analysis unit and eligibility; N2009. Full 12-hour window is body detail. |

IDs: S2001, S2002, S2003, S2004, S2005, S2006, S2007, S2008, S2009, S2010, S2011, S2012, S2013, S2014, S2015, S2016, S2017.

No additional missing-data imputation, final multiplicity correction, precise primary link function or subgroup names beyond the three on PDF30 appear in this assigned scope. This bounds extraction without drawing conclusions about protocol/SAP portions assigned elsewhere. Historical estimates remain context records. Both statistical passes must cover every listed relationship after coordinator merge.
# Statistical relationships: plan-c

Disjoint scope DOC-002 PLAN physical PDF pages57–88. Complete evidence locators and source links in extraction/parts/plan-c.md. These23 relationships require both statistical passes after merge. No test, discrepancy, finding or candidate disposition is assigned here.

| Relationship ID | Exact PLAN locations | Statistical definition and full inputs | Matching report/plan comparison key |
|---|---|---|---|
| S3001 | p57§3.4.1 | Individualpatients1:1;centralvariablepermutedblocks;strata site,HIE,sepsis,acutebrainpathologyexcludingHIE | Randomisation/stratification/analysis adjustments |
| S3002 | p60§3.4.4;p76§8.5.1–2 | Accrueddata retained unless removal requested;refusalwithoutremoval minimum90daysurvivalonly;NDOO withoutconsent noidentifiablelinkage butminimum primarysurvival collected;deaths/dischargewithoutcapacity CAG inclusion pathway | Analysispopulation,primarymissingness and consent exclusions |
| S3003 | pp66–68 | Enhanced2,500(15%) of16,500;first10/site thenrandomsample acrosssite/arm/time;survivorHrQoLsame sample;routineCMP and mortalitylinkageall | Adherence/HrQoLpopulation and sampling |
| S3004 | p68§3.9.1 | AncillarySWAT1:1card/nocard;questionnairecompletionproportion,responsetime,completeness;excludeinpatients | Ancillaryoutcomes,distinct from clinical trial |
| S3005 | pp68–70§3.10.1,Table2,§4.2.1 | Pilotparticipantsincludedmain;trafficlight allGreencontinue,anyAmberamend,anyRedstop;NIHRfinaldecision;exact thresholds N3016–19 | Pilot decision/population |
| S3006 | p69§3.10.2 | ClinicalPRIMARY allcause90daymortality;EconomicPRIMARY incremental90daycost,QALY,NMB | Primary outcome/time/status |
| S3007 | p69§3.10.2 | ClinicalSECONDARY ICU/hospitalmortality censor90days;60day/1yearmortality;stay censor90days;ordinal30dayaliveandorgan-supportfree with deathworst;respiratory/cardiovascular/renal CriticalCareMinimumDataset;EQ5D90days | Secondary outcomes/status/component definitions |
| S3008 | p69§3.10.2 | EconomicSECONDARY EQ5D90days,resourceuse/cost90days,lifetimeincrementalcosteffectiveness | Economic outcomes/status |
| S3009 | p70§4.1 | Binary90daymortality37→34.5%,ARR2.5points,RRR6.8%;90%power;15,444;6%attrition,target16,500;alpha/sidedness/test not stated here | Power reproduction,match precise SAP assumptions elsewhere |
| S3010 | p70§4.2.2 | A priori SAP before investigatorunblinding;allITT;baselinebalance observations not significance tested | ITT/analysis timing and baseline method |
| S3011 | p70§4.2.2 | Primary90daymortality regression site random effects;PRIMARYadjustment strata(site,HIE,acutebrainexcludingHIE,sepsis)+prespecifiedriskfactors;also strata-onlymodel;report absolute riskreduction and relativerisk | Primary model/covariates/effect measure |
| S3012 | p70§4.2.2 | Additionalbaselinecovariateschosenapriori establishedoutcomeassociation;not imbalance,univariatesignificance or stepwise | Covariate selection rule |
| S3013 | p70§4.2.2 | Secondarysimilarregressions:binomial/Poisson binary;normal continuous | Secondary model families |
| S3014 | pp70–71§4.2.2 | ICU/acutehospitalstay Wilcoxonrank-sum stratifiedbysurvivalstatus | Stay distribution analysis |
| S3015 | p71§4.2.2 | SurvivalKaplan-Meierplots,Coxproportionalhazards shared sitefrailty | Survival model/clustering |
| S3016 | p71§4.2.2 | Treatment×subgroupinteraction in adjustedprimaryregression;apriorilimitedsubgroups;key suspectedHIE,acutebraininjuryexcludingHIE,sepsis | Prespecified primary subgroups |
| S3017 | p71§4.2.2;p73§6.1.1 | Interims afterrecruitmentand90dayfollowup4,500/10,000;Peto-HaybittleP<0.001;recommendterminationeither effectivenessorharm;more atDMECrequest | Interim/stopping rule;no additional multiplicity detail here |
| S3018 | p71§4.2.3 | ITTCEAhealth/personalhealthservicesperspective;15%detailedresource/HrQoLsample;validatedregressionpredictall;CMP/HES linkage and NHS/PSSRUcostunits | Economic sample extrapolation/estimand |
| S3019 | p71§4.2.3 | EQ5D5Lappropriatevalueset unnamedhere;survivorutilityzeroatrandomisationthenlinearinterpolationto90dayutility;area-under-curveQALYs;decedentsbefore90dayszeroQALYs | QALY computation and survival weighting |
| S3020 | p71§4.2.3 | NMB£20,000×incrementalQALYs−incrementalcost;mean95%CIs costs/QALYs/NMB;multilevellinearregression siteclustering andpatient/sitecovariates | Economic effect/uncertainty/model |
| S3021 | p72§4.2.3 | Extensive90dayCEAsensitivity;report acrossallclinicalsubgroups;no specificnamed sensitivity parameterhere | Prespecified economic sensitivity/subgroups |
| S3022 | p72§4.2.3 | Lifetime projection excessmortalityvsage/gendermatchedpopulation;thenpopulation survival/HrQoL;90day morbiditycostextrapolation excessmortalityperiod; combine survival/quality forincrementalcost,QALY,NMB | Lifetime model/horizon |
| S3023 | pp81,82,87,88 | Disclosedversions:oxygen targetamendedv1.2;ordinal30dayorgan-supportfree ADDED as clinicalSECONDARYv1.8 14Oct2024;SAPv1.0 coverreferencesprotocolv1.5 12Apr2022 | Endpoint/intervention amendment disclosure and prespecification chronology |

Protocol pp57–88 supplies no clinical missing-data imputation, specific clinical sensitivity analysis or final alpha/multiplicity statement beyond the interim rule. This is an explicit source-map fact, not a finding; supplied SAP body lies in other assigned shards. No plan-versus-report comparison has been decided from unassigned source units.
# Statistical relationships: DOC-002 PLAN pages 89–120

31 independent statistical relationships, all available for both statistical passes. Exact locations refer to physical pages of joi250042supp1_prod_1753377747.92525.pdf. Each location is PLAN. Every statement was read visually against the page image; coordinator GPU OCR is a transcription aid. No findings or candidate selection. Original SAP v1.0 ends page110; final v1.1 begins111. Detailed final methods after 120 belong to plan-e. Numeric IDs cross-reference relationships/parts/plan-d.md. Source links from this directory use ../../../joi250042supp1_prod_1753377747.92525.pdf#page=N.

| ID | Exact location | Statistical relationship and full specification | Comparison key |
|---|---|---|---|
| S4001 | pp93–94 §1.3; pp116–117 | Primary clinical outcome:90-day all-cause mortality. Primary economic outcome:90-day NMB. Other objectives:ICU/hospital mortality censored 90 days, 60-day/one-year mortality, ICU/hospital stay censored 90 days, 90-day HrQoL, lifetime NMB. Final objectives add30-day organ-support-free days. | N4002, N4032; endpoint status/time |
| S4002 | p94 §§2.1–2.2; p117 | Individual allocation1:1 conservative SpO2 target90±2% versus usual oxygen. Variable permuted blocks, stratified by site and four mutually exclusive diagnostic categories. Hierarchy if overlap:HIE, sepsis, acute brain injury excludingHIE, otherwise none. COVID measured but not a randomization stratum. | N4003; allocation/intervention |
| S4003 | p94 §2.3; p117 | Required total15, 444 for mortality37%→34.5%, absolute reduction2.5percentage points, relative reduction6.8%, power90%, alpha5%. Recruit16, 500 allowing6% refusal/withdrawal/loss. Calculation method not named. Historical supporting cohortsCMP N96, 028/RiskII N82, 075 are planning inputs. | N4004; sample-size reproduction |
| S4004 | p94 §2.4; p117 | All outcomes tested for superiority; no noninferiority/equivalence margin in this assigned material. | N4005; hypothesis direction |
| S4005 | pp95–96 §2.5; pp118–119 | Pilot:all green criteria mean unchanged progression; any amber means amendment; any red means stop. NIHRHTA decides afterTSC recommendation. Complete numeric thresholds N4006–N4009. Pilot participants enter main analysis. Table adherence footnote retained exactly, alongside the patient-level no-deviation definition in§3.2.2. | N4006–N4009, N4014; decision/adherence |
| S4006 | p96 §§2.6–2.7; p119 | Two interim analyses after 4, 500/10, 000 patients complete90-day follow-up/linked outcome. Primary method§5.3.1, Peto–HaybittleP<0.001 for effectiveness or harm. No conditional-power analysis or futility stopping. Extra analyses ifDMEC requests. Final analysis after all 90-day follow-up, with follow-up beyond90 censored at linked-data update/database lock. | N4010; interim/stopping |
| S4007 | p96 §2.8; p119 | Enhanced sample 2, 500(15%):first10/site≈1, 000 plus random subsequent≈1, 500; subsequent probability10%, block10 for eachsite/treatment. Hourly respiratory exposures day0/1–10 whileICU; 90-day questionnaires among surviving, consenting enhanced sample. | N4011; sampling/population/time |
| S4008 | p97 §3.1; p120 | All tests two-sided, P<0.05 unless otherwise specified; effect95%CIs; no multiplicity adjustment. Subgroups interpreted using credibility criteria. Interim exception separatelyS4006. | N4012; levels/multiplicity |
| S4009 | p97 §3.2; p120 | Exposure summaries across patient medians/durations, 95%CI differences, day1–10 distributions with contributor counts; pathways without formal tests. Conservative deviation:failure to reduceFiO2to21% for≥3 hours withSpO2>92%; 22/23% treated21% for deviations only. Usual group cannot deviate; site justification/TMG adjudication can exclude transient events. Finalp120 adds dose/pathway groups; originalp97 includes respiratory-support duration. | N4013, N4033, N4034; exposure/adherence |
| S4010 | p98 §§3.2.2–3.3 | ITT by initial assignment regardless of target/adherence; all known primary outcomes included. Repeat randomization permitted≥90 days after previous; patients can appear multiple times. Adherence=no patient-level deviation; report conservative patients with≥1deviation and adjudicated events deemed nondeviations. | N4014; analysis population/unit |
| S4011 | p99 §4.4 | Mortality/stay analyses include available outcomes despite consent unavailable/refused unless complete withdrawal; postal nonresponse remains included unless notification to withdraw. | N4016; consent population |
| S4012 | p100 §§4.4–4.5 | Patient-reported outcomes in enhanced subset included with multiple imputation as required; complete withdrawals excluded except count summaries. Questionnaire loss denominator=enhanced90-day survivors; includes consented unavailable, withdrawal and questionnaire consent never given. Compare completers to enhanced noncompleting survivors and all 90-day survivors. | N4017; PRO missingness/population |
| S4013 | pp100–101 §4.6 | Baselines descriptive, without statistical tests. ICNARC/APACHE use first24 h and can contain postrandomization observations; PaO2/FiO2 at randomization replace first24 h values; indirect intervention effects on other physiology may remain. Complete categories N4018. | N4018; severity/covariates |
| S4014 | p101 §5.1 | Primary death due to any cause by 90 days after randomization. Interim only:90-day-censored acute-hospital mortality may replace if death linkage substantially delayed. Date from site/CMP/death registration; priority continuesp102. | N4019; primary/interim proxy |
| S4015 | p102 §§5.1–5.2.2 | Site validation paramount; unvalidated linked discordance:death identified by either source accepted, date prioritizes death registrations. ICU death before discharge belowLevel2; hospital death before acute-hospital exit including transfers; both censored 90 days.60-day/one-year death; one-year analysis excludes patients not reaching one year before trial end. | N4020; death definition/time |
| S4016 | p102 §5.2.3 | ICU duration=sum linear time from randomization to first discharge/death plus subsequentICU admissions in same acute-hospital stay. Hospital duration=calendar days from randomization to discharge/death. Objective list states90-day censoring. | N4021; stay calculation/window |
| S4017 | p102 §5.2.4 | SecondaryHrQoL EQ-5D-5L at90 days; sent only to enhanced-data90-day survivors, initial sample 2, 500(15%). Economic methods§6.3 supply analysis. | N4022; HrQoL population/time |
| S4018 | p103 §5.3.1 | Primary adjustment:site, diagnostic stratum, age, randomizationSpO2, randomizationPaO2/FiO2(each restricted cubic spline3 knots), confirmed/highly suspectedCOVID. Estimand:enrolled patients not completely withdrawn, 90-day death, adjustedRD, treatment-policy strategy for loss to follow-up intercurrent event§7. | N4023; primary covariates/estimand |
| S4019 | p103 §5.3.1 | AdjustedRD from difference of marginal probabilities predicted by conditional logistic models, normal random site effects, fixed baseline covariates. Predict full cohort twice, once all conservative, once all usual.95%CI2.5th/97.5th percentiles of 2000 bootstrap samples. Supplementary conditionalOR direct model output; RR estimated similarly toRD. | N4023; effect/model/CI |
| S4020 | p103 §5.3.1 | Prespecified primary subgroups:four diagnostic groups, anticipated more benefitHIE/none, lesssepsis/brain injury; COVID vs not, more benefitCOVID. Ethnicity continues next page. | N4023; subgroup prespecification |
| S4021 | p104 §5.3.1 | Ethnicity subgroup, direction unclear. Repeat primary model adding treatment×subgroup interactions, one per dummy for multinomial subgroup. Report stratifiedOR/RD/CIs and interactionP; joint test if>2categories. | N4023; subgroup interaction/effects |
| S4022 | p104 §5.3.2 | Secondary mortalityICU/hospital/60 days/oneyear n/% by treatment; models similar to primary with adjusted comparisons. Continuous stay/HrQoL meanSD, medianIQR, overall and stratified by survival at discharge, with histograms. Stay among survivors analyzed by proportional hazards withFine–Gray for competing death. | N4020–N4022; secondary models |
| S4023 | p104 §5.3.2 | Survival Kaplan–Meier plots; adjustedCox proportional hazards with same baseline covariates as primary and shared site frailty. | Survival curves/hazard model |
| S4024 | p104 §§6.1–6.3 | Primaryeconomic 90-dayNMB; secondaryHrQoL/resources/cost90 days, lifetimecost/QALY/NMB. CEA byITT, conservativevsusual, using trial/CMP/HES/questionnaires. | N4024; economic status/population |
| S4025 | p105 §6.3 | Health/personal-health-services perspective. Enhanced-sample resource/utility prediction for all participants; train/test validation out of sample. DSU5L→3L mapping.90-dayQALYAUC:survivor baseline utility0, linearly interpolate to90 day utility; pre90-day deaths zeroQALYs. NMB=£20, 000perQALYgain minus incremental cost. Mean95%CIs for incremental outcomes. | N4025–N4026; economic definitions |
| S4026 | p105 §6.3 | BivariateSUR for correlated costs/QALYs. SiteICC>10% implies multilevelSUR, otherwise single-levelSUR. Adjust same baseline variables as primary; all clinical subgroups; acceptability curves and sensitivities. | N4027; economic model/decision |
| S4027 | p106 §6.3.1 | Economic sensitivities:alternativevanHout crosswalk; alternativeQALY/cost distributions(e.g.Gamma); CMP-only readmission costs instead ofCMPplus questionnaire for possible double counting; HES readmission costs instead of questionnaire. | Economic sensitivities |
| S4028 | p106 §§6.3.2–6.3.3 | Lifetime projections of initial acute-hospital survivors andICU readmissions through 90 days. FitWeibull/exponential/lognormal/loglogistic/Gompertz, choose by fit/plausibility versus age/sex-matched population. Apply90-day utility with age decrement and morbidity costs during excess mortality; thereafter population death rates/HrQoL.90-dayCEA all clinical subgroups. | N4028; lifetime/subgroups |
| S4029 | p107 §7 | Primary missing-outcome sensitivity:all missing conservative survive/all missing usual die, then reverse. Baseline missingness if neededMICE with all adjustment variables and outcomes; subgroups complete cases. Enhanced costs/HrQoLMICE; 20 datasets, fit each, pool byRubin. | N4029; missingness/sensitivity |
| S4030 | p107 §8 | ExpectedSAEs:sinus/supraventricular tachycardia, atrial fibrillation, myocardial ischaemia/infarction, mesenteric ischaemia, other possibly relatedSAEs. All randomized whileICU from randomization to90 days including readmissions. Patients≥1SAE compared byFisher exact; event totals and patientn/% overall/bytype/byallocated group. | N4029; safety/test |
| S4031 | p107 §9 | Stata/MP16.1 or update; other packages, e.g.R, for specific analyses. Software statement does not supply unprinted test details. | N4029; software |

Signature, contents and reference pages contain no additional trial inferential relationships. Matching final statements within this shard reuse existing relationship IDs. Final amendment historyp113 records timing and five disclosed changes, N4031; detailed final methods beyond120 are outside this scope. Missing inputs named without diagnosis:sample-size computation method and bootstrap resampling details. Scientific coverage gaps:None.
# Statistical relationship inventory — plan-e

Scope exactly DOC-002 PLAN pp121–136; 47 relationships, S5001–S5047. All source statements read on complete legible page images. Evidence method/provenance/page completeness in `extraction/parts/plan-e.md`. Planned specifications only. Matching keys refer to main-report methods, outcome results or supplemental analyses without importing unassigned report evidence. Numeric inputs cross-reference N records. No findings, candidate IDs or checker disposition are assigned. Each relationship requires both downstream statistical passes.

| ID | Exact PLAN source location | Statistical relationship and printed specification | Matching report key / numeric companion |
|---|---|---|---|
| S5001 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121), deviation continuation | FiO2 22/23 → 21% applies only to identifying deviations, explicitly not other oxygen comparisons; management review may remove apparent deviations, number reported | Protocol adherence/exposure; N5001 |
| S5002 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121), §3.3 | ITT by original assignment despite target maintenance/adherence; all known-primary-outcome included; repeat randomization after ≥90 days allowed, possible multiple contributions per patient | ITT/population/analysis unit; N5002 |
| S5003 | [p121](../../../joi250042supp1_prod_1753377747.92525.pdf#page=121)–[p122](../../../joi250042supp1_prod_1753377747.92525.pdf#page=122), §§4.1–4.3 | CONSORT counts and nested eligibility denominators; adult/invasive MV/supplemental oxygen enrollment within 12 h; excludes prior 90-day randomization, current ECMO, clinician arm indication/contraindication | Flow/randomization population; N5003–N5004 |
| S5004 | [p122](../../../joi250042supp1_prod_1753377747.92525.pdf#page=122)–[p123](../../../joi250042supp1_prod_1753377747.92525.pdf#page=123), §4.4 | Available mortality and ICU/hospital duration outcomes included absent explicit consent or refusal of ongoing participation unless complete withdrawal; enhanced patient-reported outcomes also included with imputation as needed; complete withdrawals excluded | Analysis population/withdrawal; N5005 |
| S5005 | [p123](../../../joi250042supp1_prod_1753377747.92525.pdf#page=123), §4.5 | Mortality loss counts/% by group; questionnaire loss % denominator enhanced day 90 survivors includes unavailable outcomes, withdrawals, never-consented; responder baseline comparisons versus living enhanced nonresponders and all living | Missingness/reporting denominator; N5006 |
| S5006 | [p123](../../../joi250042supp1_prod_1753377747.92525.pdf#page=123)–[p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124), §4.6 | Baseline group summaries without statistical testing; demographic, history, diagnostic/COVID, physiology, severity variables using n(%), mean(SD), median(IQR), specified categories | Baseline methods; N5007–N5009 |
| S5007 | [p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124), §4.6 | ICNARC latest calibration and APACHE II first 24 h data may include postrandomization; replace PaO2 and FiO2 with randomization readings, other indirect physiology effects may remain | Baseline severity/covariate definition; N5009 |
| S5008 | [p124](../../../joi250042supp1_prod_1753377747.92525.pdf#page=124), §5.1 | Primary all-cause 90-day mortality; interim-only acute-hospital mortality 90-day censoring may substitute if linkage delay substantial | Primary endpoint/interim definition; N5010 |
| S5009 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §5.1 continuation | Site-validated death data paramount; if no site validation, death from either linkage source counts and registration date paramount for date conflict | Primary outcome ascertainment |
| S5010 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §5.2.1 | Secondary ICU death before discharge below Level 2; acute-hospital death follows transfers until departure from acute hospital; censor both 90 days | Secondary endpoint/window; N5010 |
| S5011 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §5.2.2 | Secondary 60-day/one-year all-cause death; derive as primary; exclude patients not reaching one-year before trial closes when final patient day 90 | Secondary endpoint/analysis subset; N5011 |
| S5012 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125), §5.2.3 | ICU stay linear time plus readmissions same acute-hospital stay; hospital stay calendar days, randomization to discharge/death | Secondary duration/unit; N5012 |
| S5013 | [p125](../../../joi250042supp1_prod_1753377747.92525.pdf#page=125)–[p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.2.4 | Secondary ordinal composite death ≤30 days worst score −1, surviving free days ranked; support respiratory/cardiovascular/renal each calendar day 1–30; outside ICU free | Organ-support endpoint/status/composite; N5013 |
| S5014 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.2.4 continuation | CMP v3.1 aggregate-only supports assumed at start; total days=maximum respiratory/cardiovascular/renal totals capped 30 | Organ-support derivation; N5013 |
| S5015 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.2.5 | Secondary 90-day HRQoL EQ-5D-5L; questionnaires only enhanced-subset survivors (2500 / 15% enhanced target) | HRQoL endpoint/subset; N5014 |
| S5016 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.3.1 | Primary covariates site, diagnostic strata, age/SpO2/PaO2:FiO2 splines 3 knots, COVID, date 2-week periods spline 7 knots; date×COVID explored | Primary adjustment/missing covariates; N5015 |
| S5017 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126), §5.3.1 | Estimand all enrolled not complete withdrawal; 90-day mortality; adjusted RD; treatment-policy strategy for loss to follow-up | Primary estimand/population; S5004 |
| S5018 | [p126](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126)–[p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.1 | Conditional logistic normally distributed random site effects, fixed baseline; RD difference whole-cohort marginal risks under each assignment; 95% percentile CI, 2000 bootstraps | Primary model/effect/CI; N5016 |
| S5019 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.1 continuation | Supplementary conditional OR direct regression output and marginal RR estimated similarly to RD | Effect-measure identity; S5018 |
| S5020 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.2 | Confirmatory diagnostic strata: HIE greater conservative benefit, sepsis/acute-brain-injury-excluding-HIE less benefit, none greater benefit | Confirmatory subgroup direction; N5017 |
| S5021 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.2 | Confirmatory COVID yes/no anticipated greater conservative benefit in COVID; ethnicity interaction possible, direction unclear | Confirmatory subgroup definition; N5017 |
| S5022 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127), §5.3.2 | Repeat primary with treatment × subgroup, dummy variable interaction per multinomial category; subgroup OR/RD/CI plus interaction P, joint test if >2 categories | Interaction test/subgroup effect; N5017 |
| S5023 | [p127](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127)–[p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.3 | Exploratory causal forest R grf; phase 1 confirmatory variables, phase 2 prioritized baseline/eCRF/CMP; 50,000 initial trees, retain importance >0.2 × mean, retrain; implicit missing incorporated in attributes | HTE/exploratory analysis; N5018 |
| S5024 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.3 | Honest subgroup discovery using random forest half data / representative tree; effects/SE estimated from remaining data | HTE split-sample estimation; N5018 |
| S5025 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.3 | Individual CATE/SE from forest; subgroup conditional ATE augmented inverse propensity weighting using average_treatment_effect; absolute RD versus parametric primary-style logistic estimates | HTE effect measure/uncertainty |
| S5026 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.4 | Secondary mortality outcomes use similar primary regression with same covariates, adjusted contrasts; counts/%; continuous means/SD/medians/IQR overall and by survival, plus histograms | Secondary mortality/continuous presentation; N5019 |
| S5027 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.4 | Stay among survivors proportional hazards Fine–Gray competing death; organ-support-free ordered logistic adjusted proportional OR, same primary covariates | Secondary analysis/model identity; N5013,N5019 |
| S5028 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128), §5.3.4 | Survival Kaplan–Meier; adjusted Cox same primary covariates with shared site frailty | Survival model/adjustment |
| S5029 | [p128](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128)–[p129](../../../joi250042supp1_prod_1753377747.92525.pdf#page=129), §§6.1–6.2 | Primary economic NMB 90 days; secondary HRQoL/resource cost 90 days and lifetime cost/QALY/NMB | Economic outcome/status; N5020 |
| S5030 | [p129](../../../joi250042supp1_prod_1753377747.92525.pdf#page=129), §6.3 | Health/personal health services perspective conservative versus usual 90 days; CRF/CMP/HES data plus questionnaires random 15%; costs from unit cost × use; multiply impute non-enhanced costs with MAR justification from random selection | Economic population/cost missingness; N5021 |
| S5031 | [p129](../../../joi250042supp1_prod_1753377747.92525.pdf#page=129), §6.3 | EQ-5D-5L map to 3L DSU function; non-enhanced HRQoL imputed like costs | HRQoL mapping/missingness |
| S5032 | [p129](../../../joi250042supp1_prod_1753377747.92525.pdf#page=129), §6.3 | QALYs area utility curve; survivors zero at baseline, linear to day 90 utility; deaths through day 90 zero QALY | QALY definition; N5021 |
| S5033 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3 | NMB £20,000 × incremental QALY − incremental cost; ITT means 95% CIs of incremental cost, QALY, NMB at 90 days | Economic effect/CI; N5022 |
| S5034 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3 | Bivariate SUR correlation cost/QALY; ICC >10% multilevel site cluster, ICC ≤10% single level; primary clinical covariates | Economic model/cluster rule; N5023 |
| S5035 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3 | CEA clinical subgroups, uncertainty plane/acceptability curves | Economic uncertainty/subgroups |
| S5036 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3.1(a–c) | Sensitivity restricts random enhanced subset; complete cost/QALY cases; Hout alternative EQ mapping; alternate QALY distribution, e.g. gamma | Economic sensitivity/missingness |
| S5037 | [p130](../../../joi250042supp1_prod_1753377747.92525.pdf#page=130), §6.3.1(d) | Alternative cost distribution, e.g. gamma; CMP only ICU readmissions sensitivity avoids combined questionnaire duplication; HES instead questionnaire hospital readmission cost | Economic sensitivity/data sources |
| S5038 | [p131](../../../joi250042supp1_prod_1753377747.92525.pdf#page=131), §6.3.2 | Lifetime survival Weibull/exponential/lognormal/log logistic/Gompertz chosen fit/plausibility versus age/sex population; excess mortality then population rates; day 90 utility with age decrement and cost applied excess period; lifetime sums | Lifetime economic extrapolation |
| S5039 | [p131](../../../joi250042supp1_prod_1753377747.92525.pdf#page=131), §6.3.3 | Day 90 CEA across all clinical subgroups | Economic subgroup/status |
| S5040 | [p131](../../../joi250042supp1_prod_1753377747.92525.pdf#page=131), §7 | Hourly mode LOCF through last record; FiO2 logical 0.21 when no support; remaining interval missing FiO2/SpO2/SaO2/PaO2 LOCF; outcome analysis baseline only, unaffected | Exposure missingness; N5024 |
| S5041 | [p131](../../../joi250042supp1_prod_1753377747.92525.pdf#page=131)–[p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §7 | Primary missing minimal via registration/sites; secondary missing expected with refusal/withdrawal; MICE includes all adjusted baseline covariates/all outcomes | Outcome missingness/MI model |
| S5042 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §7 | Primary analysis multiply imputed, complete cases alongside; 20 datasets, models in each, Rubin combination | Primary/secondary missing data analysis; N5025 |
| S5043 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §7 | If MI × bootstrap computationally prevented: 5 datasets + 1000 bootstrap replicates OR complete-case RD/OR and imputed OR only | Permitted computational alternative; N5025 |
| S5044 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §8 | All randomized while ICU through 90 days/readmissions; expected SAE types listed; Fisher exact patient ≥1 SAE to discharge/day 90; event counts distinct patient counts/% overall/type by assignment | Safety model/population/counts; N5026 |
| S5045 | [p132](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132), §9 | Stata/MP 17.0 or later; other packages, e.g. R for specific analyses | Software; N5027 |
| S5046 | [p136](../../../joi250042supp1_prod_1753377747.92525.pdf#page=136), changes | v1.0 before first interim lock; v1.1 before recruitment completion; addition of secondary organ-support-free 30 days and HTE section, expanded missingness | Explicit amendment/endpoint status; N5028 |
| S5047 | [p136](../../../joi250042supp1_prod_1753377747.92525.pdf#page=136), changes | v1.1 adds total O2 dose intervention exposure and calendar time adjustment to mitigate COVID pandemic | Explicit amendment/exposure/primary adjustment; N5028 |

All 47 records await PASS_1_COMPLETE and PASS_2_COMPLETE in the coordinator's pass artifacts. Pages133–135 reference-only; no independent statistical relationship. Power, general significance/multiplicity or stopping boundary specifications are not on these assigned pages; neighboring assigned shard covers any such statements elsewhere. No assumption of absence from the full plan. No unresolved visual transcription ambiguity and no scientific coverage gap.

## Mandatory statistical pass completion registry

Every stable relationship is independently reviewed by the two distinct fresh high-effort statistical agents. Pass2 remains pending until its artifact handoff.

| ID | Pass 1 | Pass 2 |
|---|---|---|
| S001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S030 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S033 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S035 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S036 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S037 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S038 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S039 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S040 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1018 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1019 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1021 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1022 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1023 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1024 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1025 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1026 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1027 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1028 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1029 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1030 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1031 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1032 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1033 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1034 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1035 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1036 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S1037 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S2017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3018 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3019 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3021 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3022 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S3023 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4018 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4019 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4021 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4022 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4023 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4024 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4025 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4026 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4027 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4028 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4029 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4030 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S4031 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5017 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5018 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5019 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5021 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5022 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5023 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5024 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5025 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5026 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5027 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5028 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5029 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5030 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5031 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5032 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5033 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5034 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5035 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5036 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5037 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5038 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5039 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5040 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5041 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5042 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5043 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5044 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5045 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5046 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S5047 | PASS_1_COMPLETE | PASS_2_COMPLETE |
