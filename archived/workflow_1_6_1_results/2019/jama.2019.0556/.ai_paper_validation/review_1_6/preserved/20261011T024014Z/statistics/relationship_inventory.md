# Workflow 1.6 Statistical Relationship Inventory

Runtime agent: /root/statistics_pass1; newly spawned qc16_statistical_consistency_reviewer; model gpt-6.1-sol; reasoning effort high; current inherited provider retained; FRESH_SPAWN. PASS1 was performed by this fresh runtime. PASS2 was independently completed by fresh runtime /root/statistics_pass2, gpt-6.1-sol/high, FRESH_SPAWN, with current inherited provider retained. The two runtime IDs are distinct. Stable statistical set: S001–S140,140 relationships. Identical repeated results share one S ID; distinct outcomes,times,contrasts,models and measures have separate records. Two disjoint relationship record parts contain117 and23 relationships,each below120. All140 rows explicitly record both PASS_1_COMPLETE and PASS_2_COMPLETE. The 117/23 parts are disjoint by relationship IDs, while source documents can recur across shards.

## Source, role and coverage definitions

main = DOC-001 jama_bot_2019_oi_190007.pdf,REPORT,11pages. supplement1 = DOC-002 joi190007supp1_prod.pdf,PLAN,60pages. supplement2 = DOC-003 joi190007supp2_prod.pdf,PLAN,5pages. supplement3 = DOC-004 joi190007supp3_prod.pdf,REPORT,25pages. supplement4 = DOC-005 joi190007supp4_prod.pdf,REPORT,1page. Physical PDF pagination is used throughout. Stable relative source links from this file: [main](../../../jama_bot_2019_oi_190007.pdf#page=1),[protocol](../../../joi190007supp1_prod.pdf#page=1),[SAP](../../../joi190007supp2_prod.pdf#page=1),[results supplement](../../../joi190007supp3_prod.pdf#page=1),[data-sharing statement](../../../joi190007supp4_prod.pdf#page=1).

Main M001–M120 and support U001–U064 maps were read completely. Complete source text was inspected in page-delimited bounded scopes,including all65PLANpages,all26REPORTsupportpages and main11pages. Main graphics/table image locators supplied by mapping were used; fresh targeted source renders for mainp4,protocolp16,and resultssupplementp22 were visually inspected. Source values remain authoritative; native/layout transcriptions are aids. No web,legacy checker,legacy candidate or legacy report read. All direct tools available; no fallback environment or OCR used by this pass. Direct derivatives produced with Poppler26.01.0 `pdftoppm -r 110 -f N -l N -singlefile -png SOURCE PREFIX`,for mainN4,protocolN16,resultssupplementN22; prefixes review_1_6/preprocessing/stats1-main-p4,stats1-s1-p16,stats1-s3-p22. Images each below32-page shard bound. Local source transcriptions were read in disjoint line chunks; no input part over200000characters.

## Model and inferential definition profiles

Each row references the profile below. An absent definition remains absent; naming a conventional model does not supply its degrees of freedom,variance estimator,CI construction or covariance. Exact P/CI reconstruction was performed only where a source-defined identity exists,such as Table3 doubling. Qualitative null/P agreement and interval containment are checks,not an inferred test inversion. No normal approximation establishes a candidate.

| Profile | Supplied model,population,time,scale,coding and definitions | Missing compatible-inference definitions |
|---|---|---|
| POWER-R | REPORT mainp4 primary cumulativeMDD,factorial main effects;two-sidedalpha.05,power.90,active20/control30;attrition22% | Sample-size formula,interaction configuration,n definition aligning392 with4×196 |
| POWER-P | PLAN protocolp16–17 cumulativeMDD,additive interaction;two-sidedalpha.05,power.90,control30/active15;dropout20%;synergistic contrast80% | Power formula,precise25%contrast definition,synergistic effect assumed,IDS variance |
| PH-TEST | REPORT mainp4 scaled Schoenfeld residual proportionality test,post-hoc Cox | Test statistic,df,per-term/global output,variance/model tie handling |
| MISSING | REPORT mainp6 missing cumulativeMDD atT3,T6,T12,all4randomized arms;two-sidedthreshold.05 mainp6 | Test name/statistic,df,multiplicity,observed versus imputed test population |
| LOGIT-MI | REPORT mainpp1,4,6,7 cumulative12monthMDD logistic;all1025randomized,100MI MAR Rubin;joint interventions andinteraction,site/history adjusted;−1control,+1active;OR95%CI;two-sided.05 | Exact contrast represented by displayed OR beyond one-unit coded coefficient,pooleddf,covariance/variance estimator,CI/test engine,multiplicity adjustment NR |
| COX-MI | REPORT mainpp4,6,7 time-to-firstMDD;3/6/12 event/censor times orlastmeasure;MI/site/history/joint interventions&interaction;−1,+1;HR95%CI;two-sided.05 | Hazard tie handling,pooleddf,covariance/variance estimator,CI/test engine,full treatmentcontrast mapping,multiplicity NR |
| GEE-MI | REPORT mainpp4,6,8 Table3 overallfollowupT3/T6/T12 longitudinalANCOVA GEE,exchangeablecorrelation;100MI MAR Rubin;site/history/correspondingbaseline,bothinterventions,interactionomitted;−1,+1;unstandardizedB95%CI,two-sided.05;MD=2B includingCI | Pooleddf,sandwich/finite-samplecovariance,interval/test engine,multiplicityadjustment NR;exploratory interpretation explicitly given |
| ROBUST-MI | REPORT mainp8 Table3 T12 robustlinearregression;100MI MAR Rubin;sameadjustment/−1,+1/interactionomitted;B95%CI,MD=2B;two-sided.05 | Pooleddf,meaningofrobust variance/fit,interval/test engine,multiplicityadjustment NR |
| COHEN | REPORT mainpp4,8 CohenDfrombaseline/T12means andpooledSD,MI;separatefromadjustedB | Exact means/SDs,baseline/T12covariance,small-samplecorrection,precisechangeformula,CI/PforD NR |
| INTERACTION-MI | REPORT mainp7 foursecondaryoutcomes,interventioninteractionP.41–.98;methodsMI/jointmodel;removedfromfinalTable3 | Row-specificP,coefficientCI,overallversusT12identity,df/covariance NR |
| HISTORY-MOD | REPORT results supplementp18 nohistorymoderation primary/secondary;mainp4 interactionmethod andSAPp5 historyinteractionexamples | Allrow-specificcoefficients/CI/P,secondarytime/model,specificvariance/MIstatus NR |
| CONCEAL | REPORT mainp8/results supplementp23,12monthbelievedallocation,759available,4arms/3categories,P<.001;two-sidedglobalthresholdmainp6 | Exact test/statistic,grouping/df,multiplicity andanalysisdefinition NR |
| KAPPA | REPORT results supplementpp12,16 pillweight/selfreportagreement;omega/multinutrientidentifiedp4 | Weighted/unweighteddefinition,analysisdenominator,CI/SE,paireddata NR |
| MOD-A | REPORT results supplementp18 TableA PHQT12;B95%CI/P,supplements,F-BA,siteNLreference,history,baselinePHQ,interactionswithbaselinePHQ;globaltwo-sided.05mainp6 | Table-specificmodel/MI,variance,interval/testengine,df,multiplicity NR;mainT12robustframework is locator,not a proof of table's engine |
| MOD-B | REPORT results supplementp19 TableB overallGADfollowup;B95%CI/P,samepredictorswithbaselineGAD | Table-specificGEE/MI/variance/df/interval/testengine,multiplicity NR;noforcedsymmetry |
| MOD-C | REPORT results supplementp20 C1utilityT12andseparateUK/NLC2;B95%CI/P,baselineutility/history,site/interactionNLreferencesC1 | Table-specificMI/variance/df/interval/testengine,multiplicity NR;subgroupmodelnotassumedequaltoallsiteconditionalmodel |
| GEE-OBS | REPORT results supplementp21 nonimputedallfollowupsGEE;B95%CI,bothinterventionsandinteraction,site/history/baselineadjusted;−1,+1;globaltwo-sided.05 | Availableindividualdenominator,workingcorrelation,sandwich/variance,CI/testengine,df,multiplicity NR |
| ROBUST-OBS | REPORT results supplementp21 nonimputedT12robustlinearregression;B(SE),sameadjustment/interactions/coding;two-sided.05 | AvailableN,robustfit/variance,df,testengine,multiplicity NR;noCIsupplied |
| CACE-MDD | REPORT results supplementpp14–15 instrument/structuralequationmethod,p22 logisticMDDanyfollowup,MIsite/history,−1,+1,OR95%CI;F-BA8/21,omega≥70%;starP<.05 | Exactoriginaleffectscale/model,compliancefraction/denominator,latentclassmapping,nonlinearCACElink,variance/df/CI/testengine NR |
| CACE-CONT | REPORT results supplementp22 T12ANCOVA PHQ/IDS/GAD,MIsite/history/baseline,−1,+1,unstandardizedB95%CI;samecomplianceandstars | Exactoriginalestimateandcompliancefraction/denominator,variance/df/CI/testengine NR |

## Complete inferential mapping-key coverage

| M/U keys | Registered S relationships |
|---|---|
| M010,U009,U010 | S001,S002,S003 |
| M012 assumption test;M071 | S004,S005,S006,S007 |
| M074–M085 | S008,S009,S010,S011,S012,S013;referenceOR/HR1rows lackinferentialuncertainty,keptasreferenceinprofiles |
| M092–M103 | S014–S037,eachtimecontrastB andeachDseparate;footnoteidentitiescarriedinprofiles |
| M104–M110 | RepetitionsS014,S015,S018,S022,S025;unadjustedmeansandavailablegraphsnotadditionalinferentialtests |
| M091 | S038,S039,S040,S041 |
| M111,U057–U061 narrative | S042–S051(history),S062,S072,S081(directionrepetitions),S134(definitions) |
| M112,U063 | S118,S119,S120,S121,S122,S123,S124,S125 |
| M116,U064 | S052 |
| U051,U055footnotes | S053,S054 |
| U057.a–i | S055,S056,S057,S058,S059,S060,S061,S062,S063 |
| U058.a–i | S064,S065,S066,S067,S068,S069,S070,S071,S072 |
| U059.a–m | S073,S074,S075,S076,S077,S078,S079,S080,S081,S082,S083,S084,S085 |
| U060.a–d | S086,S087,S088,S089 |
| U061.a–d | S090,S091,S092,S093 |
| U062.a–l,overallandT12 | S094,S095,S096,S097,S098,S099,S100,S101,S102,S103,S104,S105,S106,S107,S108,S109,S110,S111,S112,S113,S114,S115,S116,S117 |
| U053,U054 CACEformula | S126,S127 |
| U002,U006,U020,U032,U033,U040–U043 | S128,S129,S130,S131,S132,S133,S134,S135 |
| M071 secondary questionnaire missingness,M086–M089 | S136,S137,S138,S139; each qualitative outcome statement covers the printed baseline/3/6/12 assessment vector without inventing time-specific tests |
| U010 IDS continuous power expectation | S140; separate from synergistic MDD comparison S003 |

AllotherM/Ukeysreviewedforinferentialeligibility:descriptivecounts,medians,IQRs,SDs,doses,schedules,instrumentcutoffs,backgroundprevalence,referencebibliographicidentifiers,administration,no-applicablepages andunlabelledgraphpositionshave no additional trial estimateCI/P/test/SErelationship. MCID/SEM reference ranges onREPORTsupplementp7are treatment-setting reference thresholds,not computedtrialSEs. No unprintedtestsorconfidenceintervalscreated. Statisticalcoverage is complete; missinginferentialdefinitions are bounded limitations.

## Canonical record parts

The following two pass1 parts were merged below; canonical pass2 status fields have now been updated, while the original pass1 parts remain unchanged. Every S record remains visible in this canonical inventory. Part1: statistics/parts/stats1-relationships-001.md (S001–S117,117). Part2: statistics/parts/stats1-relationships-002.md (S118–S140,23). Source evidence is preserved; pass2 has completed every canonical row. Its full row-specific reasoning and retained values are in statistics/parts/stats2-relationships-001.md and statistics/parts/stats2-relationships-002.md.
# Statistical relationship inventory part 1

Scope: S001–S117, 117 distinct inferential or definition relationships; runtime /root/statistics_pass1, gpt-6.1-sol/high, FRESH_SPAWN. Every row is PASS_1_COMPLETE. Source roles and physical PDF pages are explicit. NR means not reported, not zero. The model-definition profiles in the canonical inventory apply to every row naming that profile. Check K means ordered endpoints, estimate containment, direction, scale and labels checked; matched repetitions checked where present; no independent inconsistency found. Check Q means no numeric estimate/interval available; all supplied inferential statements, scope, label and repetitions checked. Exact CI/P/test compatibility is not asserted when the profile lacks a supplied compatible rule. Every canonical row now records the completion of the distinct pass2 agent; the pass1 observations below remain historical evidence of pass1.

## Power, assumptions and missingness

| S ID | Mapping key | Exact source and role | Printed inferential relationship | Definition profile | Pass-1 checks and observations | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S001 | M010 | REPORT jama_bot_2019_oi_190007.pdf p4 Sample Size | Active20%, control30%; relative33%, absolute10%; N392,196 in each4 combinations; two-sided alpha.05,power.90,attrition22%,250/combination; prior25–50% | POWER-R | Counts/scale checked; SC01 internal total wording; SC03 comparison with PLAN assumptions | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | U009 | PLAN joi190007supp1_prod.pdf p16 section4.4,p17 continuation | Difference25%; control30%,active15%; additive-interaction180/group,two-sided alpha.05,power.90,dropout20%,250/arm | POWER-P | SC02 percentage meaning; SC03 planning-assumption match to S001; no invented power formula | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | U010 | PLAN joi190007supp1_prod.pdf p17 section4.4 | Synergistic pure-treatment-group comparison power80%; IDS continuous power statement separately tracked S140 | POWER-P | Q; contrast differs from additive calculation; unreported effect/variance prevent reconstruction | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | M012 | REPORT jama_bot_2019_oi_190007.pdf p4 Statistical Methods | Scaled Schoenfeld proportionality test P>.05; hazard assumption met | PH-TEST | Q; direction agrees with stated test; statistic/df/per-term/global identity NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T3 P=.47;194/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T6 P=.62;254/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T12 P=.91;246/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Main primary and post hoc outcomes

| S ID | Mapping key | Exact source and role | Estimate, 95% CI, P | Profile | Checks and repetitions | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S008 | M075,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | Supplements OR1.06,[.87,1.29],P.57;N512/513,54/51 events | LOGIT-MI | K; p1,p6,p7 estimates/CI identical;p6/p7 P identical; unit-change/contrast definition limitation only | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | M077,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | F-BA OR.93,[.76,1.13],P.47;N512/513,48/57 events | LOGIT-MI | K; all repeats agree; shared effectcode contrast definition limitation only | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | M078,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | Supplements×F-BA OR.93,[.76,1.14],P.48 | LOGIT-MI | K; repeats identical; p1 says combination and explicitly P for interaction; interpretation limited to interaction | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | M080,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | Supplements HR1.05,[.86,1.27],P.65;4488/4656 person-months | COX-MI | K; repetitions match; effectcode contrast definition limitation only; SC06 planned-secondary/post-hoc label | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | M082,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | F-BA HR.91,[.75,1.10],P.32;4641/4503 person-months | COX-MI | K; repetitions match; shared effectcode definition limitation only; SC06 shared analysis label | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | M083,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | Supplements×F-BA HR.91,[.75,1.11],P.36 | COX-MI | K; repetitions match; interaction kept distinct from joint intervention effect | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Main secondary effects: each outcome/time/contrast separately

Narrative comparisons below use the explicit Table3 footnote d factor2. Rounding compatibility is assessed by allowing each rounded coefficient/endpoint its printed last-digit half-unit. Thus .33 may represent .325 and .12 may represent .124; their doubled displays .65 and .25 are compatible. No hidden exact values are assumed.

| S ID | Mapping key | REPORT exact location: jama_bot_2019_oi_190007.pdf | Coefficient,95% CI,P and matched adjusted mean difference | Profile | Checks | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S014 | M092.overall,M105 | p8 Table3 PHQ supplements overall;p8 text | B.33,[.12,.53],P.002; text MD.65,[.25,1.06],P.002 | GEE-MI | K; factor2 matches after independent display rounding | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | M092.T12,M108 | p8 Table3 PHQ supplements T12;p8 text | B.28,[.05,.50],P.02; text MD.56,[.11,1.01],P.02 | ROBUST-MI | K; factor2 matches after independent display rounding | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | M093.overall | p8 Table3 PHQ F-BA overall | B−.13,[−.33,.07],P.19 | GEE-MI | K; negative symptom coefficient compatible with nonsignificance | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | M093.T12 | p8 Table3 PHQ F-BA T12 | B−.17,[−.39,.06],P.14 | ROBUST-MI | K; narrative no other significant therapy effect agrees | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | M094.overall,M106 | p8 Table3 IDS supplements overall;p8 text | B.60,[.15,1.05],P.01; text MD1.20,[.29,2.10],P.01 | GEE-MI | K; factor2 compatible with rounding; symptom increase direction | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | M094.T12 | p8 Table3 IDS supplements T12 | B.36,[−.19,.90],P.20 | ROBUST-MI | K; overall significance does not imply T12 significance | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | M095.overall | p8 Table3 IDS F-BA overall | B−.23,[−.67,.22],P.32 | GEE-MI | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | M095.T12 | p8 Table3 IDS F-BA T12 | B−.28,[−.83,.27],P.31 | ROBUST-MI | K; Cohen D S033 belongs separate unadjusted baseline/T12 definition | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | M096.overall,M107 | p8 Table3 GAD supplements overall;p8 text | B.25,[.08,.42],P.004; text MD.50,[.16,.84],P.004 | GEE-MI | K; exact displayed factor2 agreement | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | M096.T12 | p8 Table3 GAD supplements T12 | B.14,[−.04,.33],P.13 | ROBUST-MI | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | M097.overall | p8 Table3 GAD F-BA overall | B−.16,[−.32,.01],P.06 | GEE-MI | K; near-null nonsignificance retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | M097.T12,M104 | p8 Table3 GAD F-BA T12;p8 text;p9 discussion | B−.24,[−.42,−.06],P.01; text MD−.48,[−.84,−.12],P.01 | ROBUST-MI | K; exact factor2 agreement, lower anxiety narrative and figure direction coherent | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | M098.overall | p8 Table3 utility supplements overall | B−.006,[−.012,.000],P.052 | GEE-MI | K; rounded upper.000 may be slightly positive; no forced exact-zero boundary contradiction | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | M098.T12 | p8 Table3 utility supplements T12 | B−.002,[−.008,.005],P.61 | ROBUST-MI | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | M099.overall | p8 Table3 utility F-BA overall | B.002,[−.003,.008],P.44 | GEE-MI | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | M099.T12 | p8 Table3 utility F-BA T12 | B.004,[−.002,.009],P.23 | ROBUST-MI | K | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Standardized descriptors and qualitative inference

| S ID | Mapping key | Exact location and role | Printed value or inferential statement | Profile | Checks | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S030 | M092.D,M103 | REPORT main p8 Table3 PHQ supplements | Cohen D.10, no CI/P for D | COHEN | Positive sign agrees with poorer supplement PHQ change; no exact imputed group summaries supplied | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | M093.D,M103 | REPORT main p8 Table3 PHQ F-BA | Cohen D−.02, no CI/P for D | COHEN | Direction coherent; adjusted B and baseline/T12 descriptor are different estimands | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | M094.D,M103 | REPORT main p8 Table3 IDS supplements | Cohen D.05, no CI/P for D | COHEN | Positive sign agrees; exact imputed inputs NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S033 | M095.D,M103 | REPORT main p8 Table3 IDS F-BA | Cohen D.006, no CI/P for D | COHEN | Small positive D versus negative adjusted B is not a contradiction: unadjusted change and adjusted ANCOVA differ; inputs NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | M096.D,M103 | REPORT main p8 Table3 GAD supplements | Cohen D.10, no CI/P for D | COHEN | Direction coherent; inputs NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S035 | M097.D,M103 | REPORT main p8 Table3 GAD F-BA | Cohen D−.07, no CI/P for D | COHEN | Direction coherent; inputs NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S036 | M098.D,M103 | REPORT main p8 Table3 utility supplements | Cohen D−.07, no CI/P for D | COHEN | Direction coherent; higher utility is better, unlike symptom scales | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S037 | M099.D,M103 | REPORT main p8 Table3 utility F-BA | Cohen D.08, no CI/P for D | COHEN | Direction coherent; no equality with adjusted B asserted | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S038 | M091 | REPORT main p7 secondary interaction prose,p8 Table3 footnote a | PHQ supplements×F-BA no significant interaction; P belongs aggregate range.41–.98, row-specific P NR | INTERACTION-MI | Q; main interactions omitted; nonimputed interactions S098/S099 are distinct variant | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S039 | M091 | REPORT main p7,p8 Table3 footnote a | IDS supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q; no inferred row-specific P | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S040 | M091 | REPORT main p7,p8 Table3 footnote a | GAD supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S041 | M091 | REPORT main p7,p8 Table3 footnote a | Utility supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S042 | U057.narrative | REPORT joi190007supp3_prod.pdf p18 moderation opening | MDD history×supplements: primary outcome not moderated; coefficient/CI/P NR | HISTORY-MOD | Q; statement not confused with main history covariate coefficient | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S043 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: primary outcome not moderated; coefficient/CI/P NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S044 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: PHQ secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S045 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: PHQ secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S046 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: IDS secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S047 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: IDS secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S048 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: GAD secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S049 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: GAD secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S050 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: utility secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S051 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: utility secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q; no result assumed for unprinted separate time-to-onset moderation | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S052 | M116,U064 | REPORT main p8 concealment;REPORT joi190007supp3_prod.pdf p23 eAppendix13 | P<.001; n759; believed supplements percentages8.2,10.4,25.5,43.7 across four arms,three answers | CONCEAL | Q; matched P/percentages agree; exact test and tested grouping NR; no assumed chi-square df | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S053 | U051,U055 footnote | REPORT joi190007supp3_prod.pdf p12 compliance,p16 footnote | Kappa.73: p12 supplement1,p16 multinutrient | KAPPA | Definition-label comparison SC07; estimate in admissible range; no CI/SE | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S054 | U051,U055 footnote | REPORT joi190007supp3_prod.pdf p12 compliance,p16 footnote | Kappa.70: p12 supplement2,p16 omega | KAPPA | Definition-label comparison SC07; estimate in admissible range; no CI/SE | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Moderation Table A: PHQ at 12 months

All following locations are REPORT joi190007supp3_prod.pdf p18 Table A, B unstandardized, 95% CI/P, MOD-A profile. Netherlands reference has no inferential estimate and is retained in the profile, not an invented S row.

| S ID | Map | Predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S055 | U057.a | Supplements | .046 | [−.399,.490] | .841 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S056 | U057.b | F-BA | .288 | [−.155,.731] | .203 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S057 | U057.c | Spain | −.480 | [−1.161,.202] | .168 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S058 | U057.d | UK | .275 | [−.373,.923] | .405 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S059 | U057.e | Germany | .233 | [−.396,.862] | .468 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S060 | U057.f | MDD history | −.536 | [−1.036,−.036] | .036 | K; main history covariate is not intervention×history | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S061 | U057.g | Baseline PHQ | .322 | [.265,.379] | <.001 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S062 | U057.h,M111 | F-BA×baseline PHQ | −.064 | [−.118,−.01] | .020 | K; p18 and main p8/p9 larger reduction at higher PHQ direction match | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S063 | U057.i | Supplements×baseline PHQ | .032 | [−.023,.086] | .259 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Moderation Table B: overall follow-up anxiety

All locations REPORT joi190007supp3_prod.pdf p19 Table B; MOD-B profile, B unstandardized, 95% CI/P; Netherlands reference. Intervals for site terms need not be forced symmetric without an explicit interval engine.

| S ID | Map | Predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S064 | U058.a | Supplements | −.107 | [−.384,.17] | .45 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S065 | U058.b | F-BA | −.054 | [−.329,.221] | .703 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S066 | U058.c | Spain | .107 | [−.424,.520] | .694 | K; asymmetric about B, method NR; no symmetry-only candidate | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S067 | U058.d | UK | .117 | [−.371,.638] | .637 | K; asymmetric about B, method NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S068 | U058.e | Germany | .058 | [−.401,.606] | .804 | K; asymmetric about B, method NR | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S069 | U058.f | MDD history | −.317 | [−.698,.063] | .102 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S070 | U058.g | Baseline GAD | .464 | [.409,.52] | 0 | K; DISPLAY_ZERO_NOT_CANDIDATE; independent contradiction absent | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S071 | U058.h | F-BA×baseline GAD | −.016 | [−.068,.036] | .554 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S072 | U058.i,M111 | Supplements×baseline GAD | .062 | [.009,.115] | .022 | K; p18 and main p8 higher anxiety at higher baseline direction agree | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Utility moderation: all-site C1 and separate UK/NL C2 tables

All locations REPORT joi190007supp3_prod.pdf p20, B unstandardized,95% CI/P. MOD-C profile; C1 Netherlands reference for site/interactions. Both subgroup headings printed C2; numbering does not alter quantitative identities. Rounded B.000 does not establish an exact zero coefficient.

| S ID | Map | Table/population and predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S073 | U059.a | C1 supplements | .000 | [−.012,.012] | .952 | K; rounding compatible | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S074 | U059.b | C1 F-BA | −.006 | [−.018,.006] | .313 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S075 | U059.c | C1 Spain | .005 | [−.012,.022] | .548 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S076 | U059.d | C1 UK | −.014 | [−.031,.003] | .097 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S077 | U059.e | C1 Germany | .011 | [−.006,.027] | .198 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S078 | U059.f | C1 MDD history | .009 | [−.003,.022] | .148 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S079 | U059.g | C1 baseline utility | .498 | [.438,.558] | <.001 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S080 | U059.h | C1 F-BA×Spain | .016 | [−.001,.032] | .066 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S081 | U059.i,M111 | C1 F-BA×UK | .017 | [.001,.033] | .041 | K; UK>NL narrative p18/main p8 matches | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S082 | U059.j | C1 F-BA×Germany | .006 | [−.01,.022] | .452 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S083 | U059.k | C1 supplements×Spain | −.006 | [−.023,.011] | .499 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S084 | U059.l | C1 supplements×UK | −.001 | [−.018,.016] | .907 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S085 | U059.m | C1 supplements×Germany | .002 | [−.014,.017] | .850 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S086 | U060.a | C2 UK supplements | .000 | [−.012,.011] | .944 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S087 | U060.b | C2 UK F-BA | .013 | [.001,.024] | .033 | K; UK benefit direction agrees with C1 comparison | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S088 | U060.c | C2 UK MDD history | .007 | [−.016,.03] | .559 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S089 | U060.d | C2 UK baseline utility | .738 | [.62,.856] | <.001 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S090 | U061.a | C2 NL supplements | .000 | [−.012,.012] | .935 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S091 | U061.b | C2 NL F-BA | −.007 | [−.019,.005] | .267 | K; distinct subgroup model, not exact C1 conditional coefficient identity | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S092 | U061.c | C2 NL MDD history | −.005 | [−.031,.021] | .697 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S093 | U061.d | C2 NL baseline utility | .509 | [.400,.619] | <.001 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Nonimputed sensitivity: every overall and T12 result

All locations REPORT joi190007supp3_prod.pdf p21 eAppendix11. Profile GEE-OBS overall, ROBUST-OBS T12. Effectcoded−1,+1; intervention and interaction included together; site/history/baseline adjusted. Main Table3 excludes interaction and imputes; numeric equality is not expected. Overall shows B95%CI; T12 shows B(SE), not a CI. No guessed variance or degrees of freedom.

| S ID | Map | Outcome/contrast/time | B | CI or SE exactly as labeled | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S094 | U062.a.overall | PHQ supplements overall | .30 | CI[.11,.49] | .002 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S095 | U062.a.T12 | PHQ supplements T12 | .28 | SE.11 | .013 | SE positive; no CI supplied; rounded ratio compatible diagnostically, no exact rule supplied | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S096 | U062.b.overall | PHQ F-BA overall | −.14 | CI[−.34,.05] | .14 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S097 | U062.b.T12 | PHQ F-BA T12 | −.22 | SE.11 | .052 | SE positive; near-threshold result not forced to P<.05 from rounded2.0 ratio | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S098 | U062.c.overall | PHQ interaction overall | −.01 | CI[−.20,.18] | .94 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S099 | U062.c.T12 | PHQ interaction T12 | .02 | SE.11 | .84 | SE positive; low ratio coherent qualitatively | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S100 | U062.d.overall | IDS supplements overall | .55 | CI[.11,.99] | .01 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S101 | U062.d.T12 | IDS supplements T12 | .28 | SE.28 | .30 | SE positive; .275–.285 rounding of numerator/denominator admits ratio1.036 and diagnostic Pabout.30 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S102 | U062.e.overall | IDS F-BA overall | −.26 | CI[−.70,.18] | .25 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S103 | U062.e.T12 | IDS F-BA T12 | −.36 | SE.28 | .20 | SE positive; no exact inferential rule | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S104 | U062.f.overall | IDS interaction overall | −.01 | CI[−.45,.43] | .96 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S105 | U062.f.T12 | IDS interaction T12 | .12 | SE.28 | .66 | SE positive; no exact inferential rule | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S106 | U062.g.overall | GAD supplements overall | .24 | CI[.08,.40] | .004 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S107 | U062.g.T12 | GAD supplements T12 | .17 | SE.09 | .07 | SE positive; no exact inferential rule | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S108 | U062.h.overall | GAD F-BA overall | −.16 | CI[−.32,.00] | .06 | K; rounded upper.00 can be positive; no boundary-only candidate | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S109 | U062.h.T12 | GAD F-BA T12 | −.26 | SE.09 | .005 | SE positive; lower anxiety direction matches main sensitivity interpretation | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S110 | U062.i.overall | GAD interaction overall | .04 | CI[−.13,.20] | .66 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S111 | U062.i.T12 | GAD interaction T12 | .03 | SE.09 | .74 | SE positive; no exact inferential rule | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S112 | U062.j.overall | Utility supplements overall | −.006 | CI[−.011,.000] | .055 | K; precision permits null within unrounded interval | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S113 | U062.j.T12 | Utility supplements T12 | −.001 | SE.003 | .66 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S114 | U062.k.overall | Utility F-BA overall | .002 | CI[−.004,.007] | .51 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S115 | U062.k.T12 | Utility F-BA T12 | .004 | SE.003 | .23 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S116 | U062.l.overall | Utility interaction overall | −.002 | CI[−.008,.003] | .42 | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S117 | U062.l.T12 | Utility interaction T12 | .001 | SE.003 | .65 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | PASS_2_COMPLETE |
# Statistical relationship inventory part 2

Scope: S118–S140,23 relationships; same fresh pass-1 owner /root/statistics_pass1. All rows PASS_1_COMPLETE; definition profiles and K/Q check meanings are in canonical inventory/part1.

## CACE: every effect row separately

Every location below is REPORT joi190007supp3_prod.pdf p22 eAppendix12. CACE-MDD profile for MDD, CACE-CONT for symptoms. CI95%; single*=P<.05; **=P<.01 definition printed but no double-star cell. No exact P or SE supplied. Effectcoding−1,+1; omega adherence≥70%,F-BA8/21. The observed ITT and CACE populations/estimands are different; equality of their coefficients is not imposed.

| S ID | Map | Outcome/intervention | Estimate | 95% CI | Printed inference | Checks/repetitions | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S118 | U063.a,M112 | MDD F-BA | OR.78 | [.64,.95] | * P<.05 | K; main p8 OR/CI and significant narrative identical;p9 lower MDD coherent | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S119 | U063.b,M112 | MDD supplements | OR.84 | [.67,1.07] | no star,exact P NR | K; main p8 no primary effect compatible; direction differs from ITT S008 but CACE original-scale mapping unknown; see S127 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S120 | U063.c | PHQ F-BA | B−.22 | [−.59,.15] | no star | K; direction matches ITT, inference nonsignificant | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S121 | U063.d | PHQ supplements | B.43 | [.08,.77] | * P<.05 | K; poorer symptoms direction matches main narrative | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S122 | U063.e | IDS F-BA | B−.42 | [−1.24,.40] | no star | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S123 | U063.f | IDS supplements | B.47 | [−.33,1.27] | no star | K | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S124 | U063.g | GAD F-BA | B−.31 | [−.60,−.02] | * P<.05 | K; lower anxiety direction matches primary ITT symptom analysis | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S125 | U063.h | GAD supplements | B.18 | [−.11,.47] | no star | K | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Definition-linked inferential comparisons and planned quantitative analyses

| S ID | Mapping key | Exact sources and document roles | Printed relationship and check | Definition/missing inputs | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|
| S126 | U053,U054,U063.a/c/e/g,M014,M112 | REPORT joi190007supp3_prod.pdf pp14–15 CACE explanation,p22 F-BA column;REPORT main pp4,6,8 | CACE difference described as original intervention effect/proportion compliers; randomization instrument in structural equation model. Full-sample CACE coefficient matches main only for stated OR. No forced direct division of an OR. | CACE profile; original coefficient scale, exact original-model inputs, paired compliance denominator, nonlinear-to-linear estimand mapping NR. Cannot reproduce numerical rescaling from displayed ITT OR or B. Definition deficit is a limitation, not a manufactured candidate. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S127 | U053,U054,U063.b/d/f/h,M014,M112 | REPORT joi190007supp3_prod.pdf pp14–15,p22 supplements column;REPORT main pp4,6,8 | Same formula statement for supplements; OR.84 versus ITT1.06 is a direction difference across distinct analyses; CACE direction is not asserted equal to ITT absent original input/model mapping. | Original effect scale/model and compliance fraction NR; no unsupported OR-ratio or log-OR scaling identity assumed. All printed CACE intervals contain estimate; stars coherent. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S128 | U032,U040,U041,U042,M007,M012,M075 | PLAN joi190007supp1_prod.pdf pp28,43;PLAN joi190007supp2_prod.pdf pp2–4;REPORT main pp4,6 | Protocol primary survival and mixed analysis; SAP primary cumulative-MDD logistic OR95%CI/P, secondary Cox HR95%CI/P; report primary logistic/post-hoc Cox. Logistic definition matches SAP; protocol/SAP differ by version scope; SC06 report post-hoc Cox label versus SAP secondary plan. | PLAN models retain their prospective roles; no numerical results in plans. Version chronology/amendment mapping NR. No clinical/design adjudication. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S129 | U002,U006,U020,U032,U040,M008,M094,M095 | PLAN joi190007supp1_prod.pdf pp9,14,28,43;PLAN joi190007supp2_prod.pdf p2;REPORT main pp4,8 | IDS in protocol p28 main study endpoints/p43 primary parameter severity; protocol p9 continues its main-endpoint list, while SAP p2 calls IDS secondary; main Table3 secondary IDS estimates S018–S021. SC05 concrete endpoint/inferential label discrepancy. | Endpoint hierarchy differs inside PLAN and between PLAN/REPORT; exact amendment history not supplied. Comparisons keep outcome,12month and scale identity. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S130 | U041,M092–M103 | PLAN joi190007supp2_prod.pdf p3 fourth-analysis paragraph;REPORT main p8 Table3 | SAP T12 standardized mean differences95%CI/P; report T12 unstandardized coefficient95%CI/P plus separate Cohen D without CI/P. effect-measure/precision-output definition limitation only. | Unstandardized B and standardized D are explicitly distinct. No denominator or SD borrowed from available-data plots; missing imputed SD and D uncertainty. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S131 | U009,U042,M078 | PLAN joi190007supp1_prod.pdf p16 power;PLAN joi190007supp2_prod.pdf p4 interaction plan;REPORT main p6 Table2 interaction | SAP multiplicative interaction A×B in logistic; planned additive RERI from linear-OR model with likelihood95%CI, lowest-risk joint reference recoding, RERI>0 departure criterion. Report shows multiplicative interaction only. | RERI estimate/CI not supplied; no numerical identity with OR.93 imposed; omission of separately planned analysis alone not a numeric candidate. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S132 | U033,U041,U055.o–r | PLAN joi190007supp1_prod.pdf pp43–44;PLAN joi190007supp2_prod.pdf p3 third-analysis paragraph;REPORT supplement3 p16 | Planned nutrient-status regression in blood subset adjusted intervention; planned longitudinal T6/T12 blood concentrations adjustedT0 as compliance check. Report descriptive changes N335/334,medianIQR only. | No observed inferential test/CI/coefficient supplied; no conversion of IQR toSE or CI. Data availability/nutrient change identities covered; method omissions not candidates alone. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S133 | U032,U041,U055.l/m/n | PLAN joi190007supp1_prod.pdf p43 secondary;PLAN joi190007supp2_prod.pdf p3 third-analysis paragraph;REPORT supplement3 p16 | Planned longitudinal behavior T3/T6/T12 and dietary intake T6/T12 adjustedT0; protocol secondary mixed models. Report diet/weight descriptive T12−T0,not inferential. | No estimateCI/P for these contrasts; SD-like parentheses are not inferential SE; missing supplied result prevents compatibility reconstruction. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S134 | U033,U042,U043,M013,M111,U057–U061 | PLAN joi190007supp1_prod.pdf p44;PLAN joi190007supp2_prod.pdf pp4–5;REPORT main pp4,8;REPORT supplement3 pp18–20 | Protocol modifiers country/sex/education/income/BMI/age in Cox/Mixed; SAP history/center,interactionP<.05; report site/history plus post-hoc baseline severity; all printed modifier estimates tracked S055–S093. | Planned/unreported subgroup coefficient identities not invented; baseline severity explicitly post-hoc; table exact interval/variance engines and MI status NR. Matched PHQ/GAD/utility directions agree. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S135 | U043,M011,M015,U062,U063 | PLAN joi190007supp2_prod.pdf p5 missingness;REPORT main pp4,6,p8 tables;REPORT supplement3 pp21–22 | SAP100datasets,MAR,Rubin rules,FIML/MI where appropriate;report100datasets,MAR,Rubin,MI main/CACE and nonimputed sensitivity. Two-sided.05 reportp6/SAPp3. | Poolingdf,finite-sample adjustment,exact model covariance,variance estimator,CI engine and multiplicity correction NR. Exchangeable GEE correlation supplied. No external defaults used to derive exact P from CI/SE. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S136 | M071,M086 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition,p7 Figure2 PHQ N | PHQ questionnaire missing rates did not differ across intervention groups. Available N baseline996,T3 819,T6 750,T12 757; corresponding missing29,206,275,268 among1025 are arithmetic locators, not new inferential estimates. | Overall no-difference statement covers these assessment times; no individual-time P/test/CI/statistic is supplied, and no time-specific inference is invented. Two-sided threshold mainp6; test model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S137 | M071,M087 | REPORT mainp6 Follow-up Attrition,p7 Figure2 IDS N | IDS questionnaire missing rates did not differ across intervention groups. Available N baseline994,T3 817,T6 747,T12 757; missing31,208,278,268 derived among1025. | Same broad missingness inference; no separate printed time-specific test. Test/model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S138 | M071,M088 | REPORT mainp6 Follow-up Attrition,p7 Figure2 GAD N | GAD questionnaire missing rates did not differ across intervention groups. Available N baseline993,T3 815,T6 747,T12 757; missing32,210,278,268 derived among1025. | Same broad missingness inference; no separate printed time-specific test. Test/model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S139 | M071,M089 | REPORT mainp6 Follow-up Attrition,p7 Figure2 utility N | Utility questionnaire missing rates did not differ across intervention groups. Available N baseline993,T3 814,T6 747,T12 757; missing32,211,278,268 derived among1025. | Same broad missingness inference; no separate printed time-specific test. Test/model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S140 | U010 | PLAN joi190007supp1_prod.pdf p17 section4.4 | IDS-30 continuous outcome power will be much larger; prior prevention trial smaller samples gave significant differences; no numeric power/effect/variance/P supplied. | Separate from synergistic MDD contrast S003. Alpha/two-sided/power assumptions on p16 describe primary calculation; no IDS variance or specific IDS power model supplied. Qualitative expectation only; Q. | PASS_1_COMPLETE | PASS_2_COMPLETE |

## Pass 2 completion and source-recheck reconciliation

Fresh runtime /root/statistics_pass2, qc16_statistical_consistency_reviewer, gpt-6.1-sol/high, FRESH_SPAWN, inherited current provider. All S001–S140,140 relationships, revisited against the full cross-lane C001–C020 ledger and20 direct-source rechecks. One new descriptive measure-association candidate P2-01 was discovered in N175/U055, then registered by the coordinator as C021 and checked by a different fresh high-effort agent /root/recheck_append_001. The complete final C001–C021 ledger and all21 rechecks were incorporated before pass2 completion. C021 is recorded_candidate, REPORT/REPORT, S_W, Measure, label, or scale inconsistency category, report_internal_inconsistency, with mechanically suggested retain; no new inferential S ID is required. All21 candidates remain Pending Human Adjudication.

Relationship-disjoint output parts: statistics/parts/stats2-relationships-001.md has S001–S117,117 explicit rows; statistics/parts/stats2-relationships-002.md has S118–S140,23 explicit rows. Each retains exact input values plus source location or a truthful declared source band and records individual pass2 reasoning, PASS_1_COMPLETE and PASS_2_COMPLETE. The canonical140 original rows above also contain both complete statuses. The pass1 part artifacts are preserved unchanged. Complete pass2 checker summary: checkers/statistical_pass_2.md. New-candidate full evidence: checkers/statistical_pass_2_new_candidates.md.

Source-authority refinements incorporated: C009 lacks matched numerator/denominator and endpoint pairing, so record_input_error remains and no full-trial denominator is imposed. C018 expressly compares interaction versus main-effect power, so record_input_error remains and no same-calculation identity is imposed. C016 protocol p28 says MINI V5.0 followed by citation1; no V5.01 version discrepancy is propagated, while DSM-5/DSM-IV remains. C017 protocolp9 corroborates the main/primary side; actual IDS example values are MAINp8 Table3. C006 protocolp26 explicitly supplies1412mg fish oil with minimum65%EPA/minimum10%DHA as a mass-basis alternative, without establishing exact active EPA+DHA mass. C021 confirms four single-asterisk pill-weight/self-report rows, an unstarred separate Morisky row, and a single-asterisk footnote defining average Morisky; no equality of scores/percentages/N is assumed.

All point/interval ordering and containment checks remain coherent. Matched effect repetitions and explicit factor2 relationships reconcile under printed precision. Coherent display-zero S070 remains DISPLAY_ZERO_NOT_CANDIDATE. Exact OR expB/exp2B transformation, binary/continuous CACE original input and compliance mapping, symmetric moderator CI engine, precise pooled/robust inference definitions and standardized-D imputed inputs remain absent; no identities are manufactured. The genuine conditional candidates retain their specifically named missing definitions. No severity, acceptance, validity or final correction is assigned.

## Final descriptive mapping extension and statistical-scope closure

The later support visual repair mapped U065.a–h on protocol physical p26 and checked the entire family as N185. Both product labels contain descriptive dose, composition, package-unit and storage quantities plus administrative identifiers, with no clinical outcome estimate, uncertainty interval, P value, test, SE or statistical model. The fresh numeric repair specialist and final high-effort quality auditor confirm that no additional inferential S relationship is introduced. C022 is a PLAN product-unit label observation; C021 is a REPORT marker/measure association. The full registered statistical set remains S001–S140, covered explicitly by both distinct fresh high-effort statistical passes; the final22-ID cross-lane context is covered by the source rechecks and quality audit.
