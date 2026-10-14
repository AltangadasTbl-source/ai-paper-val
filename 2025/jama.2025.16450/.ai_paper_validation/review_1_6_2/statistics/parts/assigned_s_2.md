# Disjoint S review shard 2

Exact scope: S273, S274, S275, S276, S277, S278, S279, S401, S402, S403, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419, S420, S421, S422, S423, S424, S425, S426, S427, S428, S429, S430, S431, S432, S433, S434, S435, S601, S602, S603, S604, S605, S606, S607, S608, S609, S610, S611, S612, S613, S701, S801, S802, S803, S804, S805, S806, S807, S808, S809, S810, S811, S812, S813, S814, S815, S816, S817, S818, S819, S820, S821, S822, S823, S824, S825, S826, S827, S828, S829, S830, S831, S832, S833.

## S273 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S273 | DOC-005 p8method/quantitydefinitions |Headerp7RRrelative risk,footnotep8RR=riskdifference;binaryparagraphrelative risks;continuousleast-squaresMD,GA/centeradjustment;nonmissingdenominators/timewindows |Printed definitions retained exactly without diagnosis |Method/labels |

## S274 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S274 | DOC-002 p10 | PriorRCTBPD/deathRR/CI/NNT,followupNDIandmeta-analysis3effects/intervals;fullprintedtriplesinextractionN235 |

## S275 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S275 | DOC-002 p11Table1 | All14demographicdescriptiverowswithP,294vs173historicalcohorts;fullrowsN236 |

## S276 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S276 | DOC-002 p12Table2 | All22respiratory/definition/timepointrowtests;chi-square/t/Mann-Whitneyfootnotes;fullrowsN237 |

## S277 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S277 | DOC-002 p13Tables3–4 | All16morbidity+16discharge/growthrowtestsandfootnotes;fullrowsN238 |

## S278 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S278 | DOC-002 p14 | PriorSIP13%vs4%P.02anddose-rangingdescriptives;fullN239 |

## S279 — mapped relationship

Source mapping artifact: statistics/parts/protocol_results.md

| S279 | DOC-002 p24 | SevenhistoricalRR/CI/Presults:death/BPD,BPD,death,PDAclosure,reintubation,NDI,long-termdeath;fullN240 |

## S401 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S401 | [p 17](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=17) | Block urn randomization with maximum tolerable imbalance lambda per stratum. Intervention assignment probability P_i A=[lambda+min(N_(i−1,A),N_(i−1,C))−N_(i−1,A)]/[2 lambda+2 min(N_(i−1,A),N_(i−1,C))−(i−1)]. N_i A and N_i C count allocations among i infants. Lambda is not numerically disclosed. Matching key: randomization algorithm and infant-level assignment. N404/N438. |

## S402 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S402 | [p 22](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=22), [p 31](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=31) | ITT is the formal primary efficacy population: all randomized, analyzed by assigned arm, except the explicitly unconsented infant excluded from every population. Efficacy defaults to ITT unless specified. SAF, mITT and PP definitions are in N435. Matching key: primary population and analysis denominator. |

## S403 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S403 | [p 23](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=23) | Sample size based entirely on composite physiologic BPD/death at 36 weeks. Two-sided RR null 1; control 58%, intervention 48%, 90%power, overallalpha.05/final.044 after 3 interims. Large-sample proportion calculation 539/arm versus robust Poisson simulation 550/arm;1160 target includes≈5%attrition. Matching key: reported power inputs and sample size; N436/N437. |

## S404 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S404 | [p 24](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=24) | Power sensitivity accounts for total 1100 and arms 550±33 lambda under 33 site×2 GA strata;90%power stated preserved. Actual lambda, simulation code and detailed inputs are not printed. Matching key: imbalance/power statement; N438. |

## S405 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S405 | [p 24](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=24), [p 25](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=25) | General methods: two-sided tests unless specified; account for site and GA strata where possible; check continuous normality and allow transformations/nonparametric methods; SAS9.4 orhigher. Primary site/GA are fixed effects. Substantial baseline differences can motivate a secondary covariate model. Matching key: model adjustment and test sidedness. |

## S406 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S406 | [p 25](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=25) | Primary available-case model excludes missing primary outcome; expected<5%perarm. Text says sensitivity for departure MCAR→MAR will be performed, referencing 9.4.3. Secondary/safety use available observations without imputation unless specified. Matching key: missing-data assumptions/denominator; N442. |

## S407 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S407 | [p 25](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=25) | Partial NDI data at 22–26 months may be adjudicated by treatment-masked Bi B and follow-up investigators. Matching key: long-term outcome classification and missing data; N411/N412. |

## S408 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S408 | [p 25](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=25), [p 26](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=26) | Formal interim safety assesses SAE OR death in SAF, actual treatment, using robust Poisson fixed site/GA, at 40(~3%),25%,50%,75% endpoint/discharge/transfer milestone. Only DSMC/DCC statisticians access interim results; DSMC recommendation to NICHD Director. Matching key: interim safety estimand/model/population. |

## S409 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S409 | [p 26](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=26) | Interim safety model alternatives for small samples/fit/convergence: pool sites, GLMM random site, GEE site clusters with unstructured/exchangeable working correlation; if inadequate sample or persistent issues, common OR with 95%CI via Mantel–Haenszel or Fisher exact. Thus planned fallback measure is OR, distinct from RR. Matching key: safety effect-measure identity and sparse analyses. |

## S410 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S410 | [p 26](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=26) | Safety Lan–De Mets Pocock-type alpha spending, overalltwo-sided.05; thresholds.0033/.0196/.0212/.0214 at 3/25/50/75%. Exact threshold depends statistical information and prior looks; belowboundary may support disproportionate harm. Formal SAE monitoring uses listed AEs meeting SAE definition. Matching key: safety multiplicity/stopping; N439. |

## S411 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S411 | [p 26](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=26), [p 27](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=27) | Efficacy interimITT composite robust Poisson fixed GA/site, same pooling/GLMM/GEE options. Looks 25/50/75%; Lan–De Mets O'Brien–Fleming overall.05; thresholds.000015/.0030/.0183, plannedfinal.0440. Matching key: efficacy interim comparison and multiplicity; N440. |

## S412 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S412 | [p 3](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=3), [p 26](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=26), [p 37](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=37) | Exact final efficacy alpha depends whether/when prior analyses occurred; spending for omitted interims may be recovered after early stopping. Section 9.3 separately states final.044 at 100%enrollment. Matching key: actual finalalpha and confidence level under early termination, preserving both contexts. |

## S413 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S413 | [p 27](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=27) | Conditional-power interval formula: `(CP_L,CP_U)=Phi{sqrt[f/(1−f)]Z1 + sqrt[(1−f)/f](Z1±Z_gamma) − Z_alpha/sqrt(1−f)}`. Phi standardnormal CDF; f informationfraction; Z1 interim effectestimate/SE; Z_alpha=.022=2.01 and Z_gamma=.10=1.28. Interval two-sided 80%. Matching key: futility calculation; N441. |

## S414 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S414 | [p 27](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=27), [p 28](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=28) | Futility evaluated at 50%/75%; DSMC may recommend halt ifupper 80%conditional-powerlimit<.50/<.30 respectively; both correspond roughly CP.10. Complete illustrative Z1=.5…2.0 table in N441. These are optionalrecommendation rules, not automatic stops. Matching key: reported futility threshold. |

## S415 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S415 | [p 24](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=24), [p 28](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=28), [p 29](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=29), [p 37](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=37) | Pool site with<10 infants in either GAstratum into nextsmallest same-center site; mayalso pool for convergence. Center with<10 per GA pooled geographicallynearest center. Adjustment may use GLMM random site or clustered GEE if fixedsite infeasible. Matching key: reported site pooling and convergence choices; N447. |

## S416 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S416 | [p 23](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=23), [p 29](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=29), [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Only singular primary outcome undergoes formal efficacy testing, repeated 3 interim+1 final. Other analyses descriptive/exploratory, generally P and 95%CI for descriptive purposes. Modelbuilding typically P<.05 but mayuse.10/.20 for covariate selection. Matching key: outcome hierarchy, multiplicity and interpretation of secondary CIs. |

## S417 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S417 | [p 29](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=29) | Prespecified heterogeneity ofprimary treatment effect by site/center, randomization GAgroup, race, sex through interactions inrobust Poisson. Ifsiteoverparameterization/convergence, group byenrollment/geography/drugqueue-versuspharmacyprocedures. P<.1 interaction maylead tosubgroupanalyses; significantqualitative interaction requires subgroupresults. Matching key: prespecified subgroup factors and interaction tests. |

## S418 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S418 | [p 29](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=29), [p 30](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=30) | Compare counts collected outsideprimaryassessmentwindow byarm; ifdifferent, include/exclude outside-window assessmentsensitivity.36 weeks maycollectthrough 37; FU22–26 months caninclude 18–30. Matching key: endpoint timing sensitivity; N443. |

## S419 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S419 | [p 31](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=31) | Baseline random imbalance: unadjusted Student t for normalcontinuous, Wilcoxon rank sum for nonnormalcontinuous, chi-square forcategorical. P used fordiscussion and secondary covariate selection; not efficacy testing. Matching key: baseline table summaries and additional covariate rationale. |

## S420 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S420 | [p 36](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=36), [p 37](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=37) | Primary model log(mu)=Xbeta, binaryy 0 survivalwithout BPD/y 1 BPDordead. Natural loglink, Poisson working distribution, robustsandwich variance via GEE. Fixed GA<26 versus≥26, fixed site 1…k−1 versusk; beta 1 intervention versuscontrol; exp(beta 1)=covariate-adjusted RR. Matching key: primary estimator, variance and effect measure. |

## S421 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S421 | [p 37](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=37) | H0:beta 1=0 versus HA:beta 1≠0; robust treatment variance; P belowstage-specific alpha rejectsnull. EXP ESTIMATE producesadjusted RR and(1−alpha)CI with ALPHA=SIG; finalalpha.044 corresponds 95.6%CI atfullplannedlooks, sourcealsoallowsrecovery under S412. Matching key: primary P/CI confidence level and test. |

## S422 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S422 | [p 37](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=37) | Sample SAS GENMOD: WHEREITT=1; CLASSRNDARM(ref 0),RANDSTRAT(ref 2),SITE,SUBJID/PARAM=REF; MODEL BPD_DEATH=RNDARM SITE RANDSTRAT/DIST=POISSON LINK=LOG; REPEATEDSUBJECT=SUBJID/TYPE=IND; ESTIMATERNDARM1/EXP EALPHA=SIG. Subject isindividualinfant, independentworkingcorrelation. Code reproduced legibly below. Matching key: planned implementation and clustering unit. |

## S423 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S423 | [p 38](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=38) | Prespecified secondary analysis ofprimary: replicate primary model in mITT, PP and SAF; respectively excludesuntreated, excludesmajorviolations, andas-treated contrast. Additionalad hoc analyses allowed. Matching key: planned primary-population sensitivity analyses; N435. |

## S424 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S424 | [p 24](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=24), [p 25](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=25), [p 38](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=38) | Prespecified secondary primary-outcome robust Poisson additionallyincludes known BPD factors(BW,sex,race/ethnicity) andpotentialimbalancedbaselinecovariates; site/GA remainfixed. Stepwise/backward iftoo many; finaladjusted RR95%CI. Otherexamples antenatal steroids,SGA,maternaleducation/insurance. Matching key: planned covariate sensitivity and adjusted estimate. |

## S425 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S425 | [p 25](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=25), [p 38](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=38), [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Missingprimary MI sensitivity specifiedif>5%missing: primary modelcovariates plusancillarymissingness/outcome predictors, M=max(10,100×missingfraction), separateprimarymodel eachdataset, Rubinpoolingestimate/SE. MAR imputation comparesagainst MCAR available-case assumption. No further sensitivityplanned dueexpectedminimalmissing. Matching key: imputation conditions/model/pooling. |

## S426 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S426 | [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Secondary binary efficacy(primarycomponents andotherbinarysecondary) ITT robust Poisson, fixed site/GA; descriptive. Matching key: component and secondary risk ratios/populations. |

## S427 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S427 | [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Continuoussecondary outcomes ITT linearregression fixed site/GA. Matching key: adjustedcontinuous contrast/dispersion. |

## S428 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S428 | [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Ordinalsecondary(e.g.,BPDgrade) proportionalodds fixed site/GA; ifassumptionfails, partialproportionalodds or Mantel–Haenszel meanscore usingstandardizedmidranks(modifiedridits). Matching key: ordinal BPDseverity model/test/effect measure. |

## S429 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S429 | [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Nominal>2 unordered categories generalizedlogit; iffit/convergenceissues, MHgeneralassociation withdf=numbercategories−1. Matching key: nominaloutcome model/test. |

## S430 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S430 | [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39) | Countsecondary Poisson fixed site/GA, person-timeoffsetwhenappropriateforvaryingexposure. Over/underdispersion permits NB orscaling; excesszeros permits ZIP/ZINB; largeapproximatelynormalcounts permitslinearregression. Additionaladhocsecondary andposthocexploratory permitted. Matching key: ventilationdaycount/rate model and exposure. |

## S431 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S431 | [p 39](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=39), [p 40](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=40) | Safety SAFactualtreatment descriptive,no specialmissinghandlingunlessspecified; optional PPas-treated repeatifexcludedviolationsaffectsafety. Binaryrobust Poisson fixed site/GA, RR95%CI. Matching key: safetyanalysis population, imputation and adjusted effect. |

## S432 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S432 | [p 40](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=40) | Safetymodelconvergence: consider NRNsite random effect; persistentissues→common OR95%CI MHsite×GA strata withadequatecells or Fisherexact. Matching key: safetyfallback effectmeasure and sparse-cell method. |

## S433 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S433 | [p 40](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=40), [p 42](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=42) | Safety summariescountindividuals n/% with AE overall/byseverity/byrelationship, alsoeventnumberpersubject. SAE, related SAE, fatal SAE onlyifenough events; non SAEdeathsseparate. Unknownonsetcountsonstudy. Matching key: event versusparticipant numerator and SAE denominator. |

## S434 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S434 | [p 43](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=43), [p 44](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=44) | Clinicalsafety KMtime-to-inhospitaldeath byarm, censor GDBstatus; deathtimemedian/range; morbidity counts, optionalhistoricalmatched GArates. Growth safetybinarylow 10 thpercentile/deathcomposites andcontinuous Zscores at 36 weeksbasedcommonpretermgrowthcharts. Matching key: survival estimand/censoring and growth outcome status. |

## S435 — mapped relationship

Source mapping artifact: extraction/parts/sap.md

| S435 | [p 45](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=45), [p 48](../../../../joi250072supp3_prod_1761000786.6988.pdf#page=48) | Plan statesnoanalysischangesfromprotocol; potentialdisplayformatsmaychangeifnotcontradict SAP. Formalprimaryanalyses/sensitivities arise fromtext, notconditionalpotentialdisplaylist alone. Matching key: prespecified outcome/analysis provenance. |

## S601 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S601 | [p7](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=7), [p11](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=11), [p22](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=22) | Randomized, masked, active-controlled multicenter design; 1:1 allocation, site and <26/≥26-week gestation stratification; independent allocation of multiples; planned total 1160. Keys: randomization, sample size, strata, multiple-birth dependence. Numeric N602/N603. |

## S602 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S602 | [p12](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=12), [p25](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=25), [p28](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=28) | Randomized/enrolled means kit opened, regardless of administration; unopened kit excluded. All randomized, treated or untreated, receive data forms. Keys: randomized denominator, ITT, flow diagram. N606/N636. |

## S603 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S603 | [p14](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=14), [p52](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=52) | Primary physiological BPD OR death at 36 weeks PMA, assessed for all randomized; physiological assessment under GDB §5.1.2, with separate Jensen assessment required. This scope points to physiological testing instructions outside pages 1–54 and does not itself provide an oxygen-reduction algorithm. Keys: primary composite, endpoint ascertainment. N610/N637. |

## S604 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S604 | [p8](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=8), [p14](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=14) | Secondary outcomes for all randomized: component death/physiological BPD at 36 weeks, Jensen grades and grade 3, postnatal BPD steroids, severe NDI, death and their composite at 22–26 months corrected age. No ordering or multiplicity rule specified here. Keys: secondary outcome family, hierarchy. N610–N614. |

## S605 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S605 | [p14](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=14), [p16](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=16) | Severe NDI uses alternative cognitive/motor/hearing/vision criteria, with definition agreed at first follow-up; table separately describes normal/mild/moderate/severe components. Preserve table and composite rather than infer a combining algorithm absent from these pages. Keys: NDI status, long-term composite. N613/N614. |

## S606 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S606 | [p14](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=14), [p15](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=15) | Exploratory NICHD severity, ventilation duration to day 28/36 weeks, intubation after 50 hours to day 28/36 weeks, repeat surfactant after 50 hours within 7 days of final dose, respiratory follow-up at 22–26 months. No subgroup/sensitivity estimator or test specified. Keys: exploratory outcome labels/time windows. N615–N617. |

## S607 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S607 | [p15](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=15), [p35](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=35), [p38](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=38) | Safety forms require randomized AND received study drug; AE ascertainment initiates with drug and extends 168 hours after final dose, SIP/PVL 30 days; moderate or greater and unexpected mild AE. Keys: safety population, risk windows, denominator. N618/N625. |

## S608 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S608 | [p38](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=38), [p39](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=39), [p40](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=40) | Safety event-specific severity thresholds include conjunctions, repeated-measure criteria and strict/inclusive inequalities. Exact event definitions in N626–N633 and page rows; preserve quantities and units when matching safety table labels. Keys: hypoxemia/bradycardia, hypertension, hyperglycemia, hypotension, air leak, ICH, sepsis, SIP/PVL. |

## S609 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S609 | [p41](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=41), [p42](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=42), [p44](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=44) | AE severity and seriousness are distinct; grades 4/5 always serious, grade 3 alone insufficient. A continuous event contributes one record at highest grade, resolved recurrence a separate event, chronic duplicates consolidated. Relatedness possible/probable/definite distinguished from unrelated/unlikely. Keys: AE event counts, participants/events, relatedness. N634/N635. |

## S610 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S610 | [p30](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=30), [p31](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=31), [p32](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=32) | Repeated data collection every 12 hours ±1 hour in first 168 hours of life; blood-gas/glucose ±4 hours; modality-specific required settings; expected but unavailable measure recorded permanently missing, measures not expected left blank or available. This is collection logic, without an imputation or missing-outcome analysis rule. Keys: repeated physiology, measurement selection, missing fields. N620–N622. |

## S611 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S611 | [p53](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=53), [p54](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=54) | Withdrawal not replaced; discontinuing drug can retain clinical data or all study assessment; stopping further collection retains existing data. BB07 follow-up to earliest 36 weeks/death/discharge/transfer. No statistical handling of missing primary outcome is specified in this scope. Keys: withdrawal, outcome availability, randomized analysis population. N638/N639. |

## S612 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S612 | [p16](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=16) | Monthly data/accrual and periodic DSMC review for futility/efficacy; no number/timing of formal interim looks, alpha spending, conditional power or stopping threshold supplied in these pages. Keys: interim monitoring, planned decision rules. |

## S613 — mapped relationship

Source mapping artifact: extraction/parts/manual_001_054.md

| S613 | [p7](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=7), [p12](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=12), [p13](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=13), [p50](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=50), [p51](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=51) | Planned comparison is surfactant plus 0.25 mg/kg budesonide versus surfactant alone, up to two doses within 50 hours; birth-weight dosing, later surfactant usual care, early steroids/indomethacin restrictions and exceptions retained. Deviation codes do not establish a per-protocol exclusion rule. Keys: intervention definition, exposure duration, concomitant treatment, deviations. N604/N605/N608/N609/N637. |

## S701 — mapped relationship

Source mapping artifact: extraction/parts/manual_055_081.md

|S701|[DOC-003 p62](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=62)|Primary outcome physiologic BPD OR death by 36 weeks postmenstrual age, in all randomized extremely preterm infants. Recorded by study staff using existing GDB criteria, section 5.1.2 B physiologic evaluation on NG07 respiratory support form. Endpoint status, composite components, timepoint and population are explicit; no effect estimate/test/model printed on this page.|Primary BPD/death endpoint; intention-to-treat population|

## S801 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S801 — Cranial imaging lesions and timing

PLAN pp109–111, I4–8. Match keys: cPVL, brain injury, 36-week assessment. Within 28 days, cPVL means diagnosed cPVL or cysts/echolucencies in white matter around ventricle; right/left/both recorded. PVL without specified cysts/echolucencies requires PI/designee scan review. Porencephalic cyst includes non-cPVL cystic disease, a single cerebral hemisphere cyst possibly communicating with ventricle, congenital or evolving from parenchymal blood/echodensity; includes posthemorrhagic cysts/multicystic encephalomalacia, excludes subependymal/choroid plexus cysts. After day 28 use sonogram and MRI nearest 36 weeks PMA; normal study skips lesion details. Enlarged ventricles, cPVL and porencephalic cyst recorded by side. MRI explicitly excludes noncystic PVL. MRI date prompt says PCA; surrounding heading says PMA.


## S802 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S802 — Enteral feeding attainment

PLAN p111, J2. Match key: full enteral feeding time. Attainment is feeds reaching 120 ml/kg/day using current weight, with first attainment date. Nutrition and feed definitions in N801.


## S803 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S803 — Early milk, fortification and probiotic exposure

PLAN pp111–112, J2d–f. Match key: early feeding/cointerventions. Milk, fortification and probiotic exposure windows are first 28 days. Probiotic Y if received; masked/unmasked study or subsequent posttrial clinical medication refers to 3.2.1. No prescribed treatment amount or effect result.


## S804 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S804 — Proven NEC status and first date

PLAN pp112–113, J3. Match keys: NEC, surgical NEC, renal safety. Code 0 absent/suspect (no NEC or Bell IA/IB); 2 proven without surgery (IIA/IIB/IIIA); 3 proven with surgery (IIIB); 4 proven at autopsy. First diagnosis date, or death date if first found at autopsy. Feeding restart and date recorded. Creatinine measured if at least one within 10 days of diagnosis; highest mg/dL and date. Surgery includes laparotomy/drain/other procedures, Appendix E. Bell table S824.


## S805 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S805 — Spontaneous perforation and short gut

PLAN p113, J4–6. Match keys: spontaneous intestinal perforation and GI safety. Spontaneous GI perforation excludes NEC; first date collected. First enema for meconium ileus/obstruction separately. Short gut follows GI surgery, with malabsorption, severe diarrhea, gastric hypersecretion, secondary bacterial overgrowth and failure to thrive; procedure recorded in Q.


## S806 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S806 — Hearing before status

PLAN pp113–114, K. Match key: hearing morbidity. Hearing screen before status; OAE and automated ABR performed/failed separately Y/N. Diagnostic ABR before status and documented hearing loss separately. Laterality 1 unilateral, 2 bilateral for each applicable failure/loss.


## S807 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S807 — ROP classification, severity and treatment

PLAN pp114–116, L. Match keys: ROP, severe ROP, treatment. Exams usually start 4–6 weeks and continue until retinal maturation. Any stage in either eye before status qualifies. Record stage ≥3, plus disease on worst examination in either eye, stage 1/2 in Zone 1. Plus means posterior vein enlargement and arteriole tortuosity, e.g. stage 2+. Therapy: laser/cryotherapy, scleral buckle/vitrectomy, Avastin/other anti-VEGF; study treatment refers to 3.2.1. Status 1 favorable in BOTH eyes: each mature fully vascularized, or immature Zone III for two consecutive exams, or acute stage 1/2 Zone III for two consecutive exams, or clearly regressing Zone II/III. Status 2 severe in EITHER eye: surgery, detachment, or Avastin/anti-VEGF. Status 3 undetermined in either eye and neither severe: reasons 1 immature Zone I/II, 2 immature Zone III only one exam, 3 stage 1/2 Zone III only one exam, 4 stage 3 Zone III, 5 ROP Zone I/II, 6 plus disease (p116).


## S808 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S808 — AKI and hypertension measurements

PLAN p117, N. Match keys: AKI and hypertension. Clinical AKI/renal failure any time in NICU, diagnosis date and nephrology consult/referral. Hypertension diagnosis and treatment Y/N; treatments amlodipine, captopril, enalapril, enalaprilat, hydralazine, isradipine, labetalol, lisinopril, nicardipine, propranolol. BP/creatinine windows N803. No numeric AKI threshold here; death-related stage 3 rule S822.


## S809 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S809 — Early and late sepsis definitions, treatment and episodes

PLAN pp118–119, O1–4. Match keys: early/late sepsis and bloodstream infection. Early positive blood culture drawn ≤72 hours. Antibiotics ≥5 days starting within first 72 hours, including intended course truncated by death; reasons 1 sepsis, 2 meningitis, 3 UTI, 4 pneumonia, 5 other. Late culture-negative clinical infection: episode count >72 hours to status, antibiotics ≥5 days including intended course truncated by death. Late culture-positive septicemia/bacteremia: compatible clinical signs, positive blood culture after 72 hours, antibiotics ≥5 days including intended course truncated by death. New organism at any time adds episode; same bacteria after 10 days appropriate antibiotics is new episode. Six form entries, DMS accepts 10. Each episode start/stop, up to three most important organisms, CLABSI Y/N; stop is last antibiotic day. CLABSI means laboratory-confirmed BSI with central line within 48 hours before BSI, unrelated to infection elsewhere. Highest creatinine/date if measured within 10 days after initial late-sepsis diagnosis.


## S810 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S810 — UTI, meningitis and lumbar puncture

PLAN pp119–120, O5–8. Match keys: UTI/meningitis. UTI diagnosis requires antibiotics ≥5 days; date and up to three organisms. Meningitis requires positive CSF culture and antibiotics/antifungals treatment OR intent to treat ≥7 days; date, up to three organisms and PCR confirmation. LP performed/attempted for septic workup excludes ventricular tap for hydrocephalus; five form fields, DMS accepts 10; record up to five successful LP dates with CSF sent. Other infection dictionary N804.


## S811 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S811 — Generic early-death population and cause completeness

PLAN pp121–123, NG03E. Match keys: early death and flow. Infant death ≤12 hours, including delivery room. Record therapies initiated any time after birth. Autopsy Y/N; cause coding waits for autopsy results but form/EDC submission does not: TM temporarily missing then final cause. Care-limit discussion before status, intubation/ventilation or nutrition/hydration withheld/limited/withdrawn, palliative/ethics consult, comfort care only Y/N. No enrolled analysis size or mortality result.


## S812 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S812 — BiB budesonide exposure coding

PLAN p122, early-death surfactant field 2. Match key: budesonide exposure. Y if surfactant mixed with budesonide, N otherwise, T if BiB trial; T refers to 3.2.1. Generic masked-trial coding, no intervention dose or randomization rule in this field.


## S813 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S813 — Contributory cause of death and single category

PLAN pp123,127. Match keys: all-cause/cause-specific death. Contributory cause is the underlying proximate disease initiating events, etiologically specific and antecedent in time/pathology. Clinical/autopsy evidence, clinical alone if no autopsy. Only one option after PI/alternate PI consultation. Appendix C. Specify 10 congenital malformation or 90 other on early form; late form also 31 sepsis/organism; COVID-19 uses 90 other specified.


## S814 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S814 — Late-form population, status and transfers

PLAN pp123–124,126–127, NG05. Match keys: hospitalization, status, follow-up completeness. For hospitalized >120 days reaching death, discharge, transfer or one year postnatal age; diagnoses/treatments AFTER day 120. Status 1 home, 3 transferred without return in seven days, 5 death, 6 still hospitalized after one year. Transfer final outcome 1 died in hospital, 2 home, 3 still hospitalized at one year. Status/transfer/discharge/death dates. Hospitalization >120-day causes all Y/N: pulmonary, cardiac, neurologic, GI, multiple malformations, social, ophthalmologic, sepsis/infection, renal, apnea, feeding, other. Anthropometry N807.


## S815 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S815 — Late ROP/hearing and care limitation

PLAN pp124–126. Match keys: later ROP/hearing. ROP therapy after 120 days in either eye: 1 laser, 2 cryotherapy, 3 buckle, 4 vitrectomy, 5 Avastin/anti-VEGF, 6 other; study medication refers to 3.2.1. Hearing screen after 120 days; OAE/AABR performed/failed, laterality 1 unilateral/2 bilateral. Diagnostic ABR before discharge; loss Y/N/Unk when report unavailable. Care-limit discussion and intubation/ventilation or nutrition/hydration limitation after 120 days; palliative/ethics consult Y/N.


## S816 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S816 — Late discharge oxygen and medications

PLAN pp126–127, E. Match keys: home oxygen and discharge treatment. Continuous oxygen Y/N. Medication Y/N and Trial for masked placebo-controlled trial in 3a–g: diuretics, bronchodilators, anticonvulsants, antireflux, antihypertensives, methylxanthines, inhaled steroids. Systemic steroids and other medications separate; exclude vitamins/iron. Inhaled examples budesonide/fluticasone; systemic hydrocortisone/dexamethasone/prednisone/prednisolone. No amounts/durations.


## S817 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S817 — NG07 population and BPD definition routing

PLAN p128, chapter 5 revised May 1, 2025. Match keys: BPD population/definition. NG07 all GDB infants surviving >12 hours reaching status (death/discharge/transfer/120 days). Death <24 hours after surviving >12 hours: Status column only. Status before timepoint: later columns blank; Status always complete. Support includes 40 weeks PMA. Jensen Appendix M standardizes GDB and protocols with primary/secondary BPD, except trials specifically using physiologic definition. Those trials evaluate oxygen-challenge eligibility/results.


## S818 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S818 — Respiratory support collection and hierarchy

PLAN pp128–129. Match keys: respiratory duration/36-week BPD. FiO2/mode at 24 hours (snapshot), days 3,7,14,28, 36/40 weeks PMA and Status; no poststatus points. Highest-mode hierarchy HFV > CV > nasal ventilation > CPAP > nasal cannula > hood. Codes 1 HFV,2 CV,3 nasal ventilation,4 CPAP,5 NC,6 hood,7 no support,8 temporarily out of unit. HFV oscillator/jet; CV IMV/SIMV/assist-control via ETT; nasal ventilation prongs/cannula; CPAP prongs/cannula/mask. Mask/prong flow alone codes CPAP; flow plus intermittent breaths nasal ventilation. Highest FiO2 anytime during day except 24-hour snapshot; ignore temporary increases resolving to baseline <2 hours and oxygen only with feeds. NC flow paired with highest FiO2. Last HFV/CV/nasal ventilation/CPAP/any support dates through 40 0/7 weeks.


## S819 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S819 — Challenge selection and recorded absence reasons

PLAN pp130–131, revised May 1, 2025. Match key: physiologic BPD ascertainment. Only physiology trials with highest mode 5 NC (with/without oxygen) or 6 hood (including incubator oxygen) on day 36 weeks evaluated; others not evaluated/form complete. At-rest oxygen excludes <2-hour transient increases/feed-only oxygen. NC effective FiO2 uses weight/flow/concentration lookup; hood actual FiO2. Eligible: <27% oxygen and majority saturations ≥90%; 27–30% and majority ≥96%; or room air by NC. Record weight grams, date, performed/pass. Not performed: 1 increased FiO2,2 increased support CPAP/ventilator,3 instability including surgery/sepsis,4 parent/physician refusal,5 room air on/before evaluation and no oxygen/support,9 other explained.


## S820 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S820 — Prior-day saturation majority in chapter5

PLAN p130, end of section B. Match key: oxygen-challenge eligibility. Prior-24-hour chart review; printed majority means >90% of saturation readings in that period. Preserve this separately from Appendix J footnote S828.


## S821 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S821 — Cause-specific death definitions

PLAN pp137–139, Appendix C. Match key: cause-specific death. 10 major congenital malformation incompatible with life or without drastic measures, including when RDS/hemorrhage present but malformation motivates allowing death. Pulmonary: 20 severe RDS first 28 days;21 same with grade III–IV hemorrhage;22 same with fulminant pulmonary/other infection;23 same with massive pulmonary hemorrhage. 25 BPD with NC/CPAP/noninvasive or invasive positive pressure at 36 weeks PMA;26 same plus severe infection;27 same with extubation before death due to severe CNS insult;28 PPHN clinical/echo;29 BPD plus PPHN. 30 suspected infection without positive life/autopsy culture;31 proven blood/organ culture. 40 proven NEC Bell IIA or higher;41 same plus blood/peritoneal culture;42 spontaneous perforation without NEC radiology/surgery/autopsy/pathology;43 short bowel resection with malabsorption/diarrhea/failure to thrive;44 documented liver failure. 50 grade III–IV hemorrhage with CNS decompensation without severe RDS/high ventilator settings;51 heading severe hemorrhage with proven/suspected infection, body grade III/IV ventricular blood/echodensity with ventriculomegaly and/or parenchymal involvement. 70 renal S822. 60 immaturity/comfort care without active treatment, including no further care after unsuccessful birth resuscitation;90 other, excluding cardiorespiratory arrest;99 unknown only after investigation.


## S822 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S822 — Stage3 renal failure cause-of-death table

PLAN p139, death code 70. Match key: stage 3 AKI. Renal failure charted as cause of death. Serum-creatinine column: rise ≥3 × reference SCr* OR SCr ≥2.5 mg/dL** OR dialysis. Urine-output column: <0.3 ml/kg/hour for >24 hours OR anuria >12 hours. Printed * and ** have no footnote text on this page. Between-column AND/OR not printed; retain separate columns without adding logic.


## S823 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S823 — ROP diagram labels

PLAN p140, Appendix D. Match key: ROP severity. Diagram labels zones I–III; stages 1–3 at growing-vessel edge, detachment 4/5, extent clockhours, plus disease yes/no. Regression/progression/detachment and laser/cryo ablation illustrated; no participant data.


## S824 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S824 — Modified Bell staging table, all rows

PLAN p144, Appendix G. Match key: proven NEC stage ≥IIA and surgical NEC. Columns are stage, systemic, intestinal and radiologic signs.

| Stage | Systemic signs | Intestinal signs | Radiologic signs |
|---|---|---|---|
| IA, suspected | Temperature instability, apnea, bradycardia, lethargy | Elevated pre-gavage residuals, mild abdominal distension, emesis, guaiac-positive stool | Normal or intestinal dilation, mild ileus |
| IB, suspected | Same as IA | Bright red blood from rectum | Same as IA |
| IIA, definite, moderately ill | Same as above | Same as above plus absent bowel sounds, ± abdominal tenderness | Intestinal dilation, ileus, pneumatosis intestinalis |
| IIB, definite | Same as above plus mild metabolic acidosis, mild thrombocytopenia | Same as above plus absent bowel sounds, definite abdominal tenderness, ± abdominal cellulitis or right-lower-quadrant mass | Same as IIA plus portal-vein gas, ± ascites |
| IIIA, advanced, severely ill, bowel intact | Same as IIB plus hypotension, bradycardia, severe apnea, combined respiratory/metabolic acidosis, disseminated intravascular coagulation, neutropenia | Same as above plus generalized peritonitis, marked tenderness and abdominal distention | Same as IIB plus definite ascites |
| IIIB, advanced, severely ill, bowel perforated | Same as IIIA | Same as IIIA | Same as IIB plus pneumoperitoneum |

Printed citation footnote refers to Walsh/Kliegman, Clinics of North America, February 1986. Supplied citation only; no external source read.


## S825 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S825 — Major malformation coding exclusions

PLAN p145, Appendix H. Match keys: malformations and eligibility descriptors. Code families CNS 100, cardiac 200, GI 300, GU 400, chromosomal 500 (501 trisomy13,502 trisomy18,503 trisomy21), other 600 (605 inborn metabolism including G6PD), pulmonary 700. NOT major malformation: extreme prematurity, IUGR, SGA, fetal alcohol syndrome, hypothyroidism, intrauterine infection, cleft lip without palate, club feet, congenital hip dislocation, limb abnormalities, syndactyly, hypospadias, PDA, pulmonary hypoplasia (401 for bilateral renal agenesis). Generic classification, no analysis-exclusion decision here.


## S826 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S826 — Infection/NEC table, all rows

PLAN p146, Appendix I. Match key: late-onset sepsis and NEC components. All rows specify antibiotics ≥5 days.

| Blood culture | NEC | Antibiotics | Findings |
|---|---|---|---|
| Positive | Absent/suspect | ≥5 days | Late-onset sepsis |
| Positive | Proven | ≥5 days | NEC and late-onset sepsis |
| Negative | Absent/suspect | ≥5 days | No LOS, no NEC |
| Negative | Proven | ≥5 days | NEC, no LOS |


## S827 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S827 — Histologic chorioamnionitis

PLAN p147, Appendix IA. Match key: histologic chorioamnionitis covariate. Yes if report names chorioamnionitis or listed pathology. Acute I: subchorionitis/early chorionitis, patchy-diffuse neutrophils in subchorionic fibrin/membranous trophoblast; scattered neutrophils permitted in lower half of chorionic plate/connective tissue. II: >10 PMNs/high-power field in plate/connective tissue/amnion. III: numerous PMNs without amnion necrosis. IV: necrotizing changes, degenerating neutrophils, thickened eosinophilic basement membrane, at least focal epithelial degeneration/sloughing. Subacute: more than occasional mononuclear cells; neutrophils rare/absent but coexistent acute process in at least one section. Chronic: mononuclear infiltrate without acute evidence; funisitis cord inflammation; vasculitis vessel inflammation.


## S828 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S828 — BiB physiologic BPD assessment window and eligibility

PLAN p148, Appendix J revised November 12, 2020, expressly PDA and BiB trials. Match key: physiologic BPD. Objective prints 36+1 weeks corrected age; screen exactly 36 weeks, challenge as close as possible to 36 but no later than 37 weeks PMA. Include GDB infants alive at 36+1 weeks corrected age and enrolled PDA/BiB. At-rest hood actual or NC effective oxygen <27% with majority saturations ≥90% prior 24 hours, or 27–30% with majority ≥96%; room air NC at ANY lpm flow. Exclude mechanical ventilation/CPAP, hood >30%, NC effective >30%. Footnote majority is ≥90% of readings in 24 hours. Effective oxygen applies only NC via conversion tables. Ignore transient increases resolving <2 hours and oxygen only with feeds. Preserve 36+1 as printed without assigning plus-one-day or plus/minus-one-week interpretation.


## S829 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S829 — Oxygen reduction procedure and continuation/failure rule

PLAN p149. Match key: physiologic BPD challenge procedure. Supine; feeds/medications 30 minutes before; no bolus feeds during evaluation, continuous feeds permitted. Rest 5 minutes before baseline. Hood FiO2 decreases 2% every 5 minutes. NC oxygen ≥22%: decrease flow 0.5 lpm every 5 minutes to 0.5, then 0.1 lpm every 5 minutes to 0.1. Method A at 0.1 lpm decreases blender FiO2 20% every 5 minutes to room air. Method B low flow/100% oxygen: 0.06 then 0.03 lpm at 5-minute steps. Turn off/remove NC. Room-air NC >2 lpm: reduce by 2 lpm every 5 minutes to 2, then 0.5-lpm steps to 0.5 and stop. Flow 0.001–0.49 lpm: stop/remove. Continue if saturation ≥90% during 5-minute phase; stop <90% for 5 continuous minutes OR <80% for 15 seconds with good signal. Each step start records time/saturation/FiO2/NC flow; each minute time/saturation; continue until room air.


## S830 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S830 — Room-air phase pass, rapid pass and failure

PLAN p150. Match key: challenge classification. Room air 30 minutes; pass if saturations remain ≥90%, then return baseline oxygen. Rapid pass if ALL saturations ≥96% for 15 consecutive minutes in room air. Not pass if <90% for 5 continuous minutes OR <80% for 15 seconds; immediately return baseline oxygen. Date/result on NG07 B.3. Criteria only, no participant results.


## S831 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S831 — Printed effective oxygen lookup and rounding rule

PLAN pp152,154–155. Match key: effective FiO2. Table 1 factor from current lpm and weight kg; missing exact values round to nearest table value, exact midpoint UP. Table 2 factor/current concentration percent gives effective FiO2 ×100 with same rounding. N812/N813 contain every printed cell, N814 example. No algebraic formula printed; do not replace lookup cells with inferred formula values.


## S832 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S832 — Worksheet measurement grid and repeated rules

PLAN pp156–158. Match key: challenge worksheet. First page baseline plus four reduction-step blocks; second five blocks, copy as needed. Each 0–5 minutes with time/saturation each minute, FiO2/NC flow at zero only. Footers repeat continuation ≥90%, failure <90% for 5 continuous minutes OR <80% for 15 seconds; hood 2%/5min; NC ≥22% flow 0.5 then 0.1 lpm steps; Method A 20% FiO2 at 0.1 lpm, Method B 100% oxygen at 0.06 then 0.03; room-air flow 2 then 0.5-lpm steps; remove NC; monitor room air 30 minutes. Room-air grid 0–30 minutes inclusive, time/saturation; failure repeated and rapid pass ≥96% for 15 consecutive minutes. Blank forms, no patient observations.


## S833 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### S833 — Jensen BPD grade definition

PLAN p162, Appendix M. Match key: Jensen BPD severity at 36 weeks PMA. Grade 0 room air/no support; grade 1 NC flow ≤2 lpm regardless of FiO2; grade 2 NC flow >2 lpm, CPAP or noninvasive ventilation regardless of FiO2; grade 3 invasive/intubated support regardless of FiO2, including tracheostomy. Supplied Jensen 2019 citation only; no external source read. Routing S817 separates Jensen from explicit physiologic trials.


