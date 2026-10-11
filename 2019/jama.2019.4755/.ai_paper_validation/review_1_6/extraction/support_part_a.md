# Support quantitative evidence — shard A

Status: COMPLETE. Runtime agent ID: 01a12865-691c-7d70-8421-94a8a420e881. Exact disjoint source scope: DOC-002, joi190039supp1_prod.pdf physical pp.1–32; DOC-003, joi190039supp2_prod.pdf physical pp.1–10. Both documents are PLAN by their content, including historical results and risk figures. Local keys A001–A052 are evidence mapping keys, not candidate IDs or global relationship IDs. No candidate diagnosis or old scientific conclusion was used. Assigned source units: 42; mapped: 42; reusable-backed: 24; fresh-required and visually inspected: 18; uncovered: 0. No supplied workbook or CSV occurs in this scope, hence no formulas/cached values are applicable.

## Engines and evidence provenance

Read QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md, source_inventory.md, source_coverage.md, evidence_asset_inventory.md, tooling_record.md and coverage_manifest.md. Direct engines: Poppler pdftotext/pdftoppm 26.01.0 and CPU Tesseract 5.5.0 (Leptonica 1.86.0), as recorded by tooling probe. Reused immutable source-backed layout assets: `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt` (only assigned pp.1–32 inspected; corrupted fresh-required units used only as locators) and `.ai_paper_validation/review_1_5_1/preprocessing/support/DOC-003_pp1-10_layout.txt` (all ten pages). No old candidate/checker/quality/final report was read.

For EACH N in 1,6,7,8,12,13,16,18,19,20,21,22,23,24,26,30,31,32, commands were:

```text
pdftotext -layout -f N -l N joi190039supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-a/support-a-DOC-002-pN-layout.txt
pdftoppm -r 90 -f N -l N -singlefile -png joi190039supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-a/support-a-DOC-002-pN
view_image: support-a-DOC-002-pN.png, direct visual page inspection
tesseract .ai_paper_validation/review_1_6/preprocessing/support-a/support-a-DOC-002-pN.png .ai_paper_validation/review_1_6/preprocessing/support-a/support-a-DOC-002-pN-ocr -l eng --psm 6
```

Each native layout `.txt` is Poppler; each `.png` is Poppler rasterization; each `-ocr.txt` is targeted CPU Tesseract evidence support. All 18 page images were opened and visually inspected. OCR/native text is locator aid only. Visually confirmed corrections to corrupted font text include methotrexate ≥15 mg/week (pp.13,23), figure cutpoints 8,4,2,1 μg/g (p.16), complete flowchart timeline (p.20), payment 75 euros (p.26), and platelet lifespan 10±1 days (p.30). No fallback environment or GPU was used.

## Individual page coverage

Every row is COMPLETE. Physical PDF pages, rather than internal printed footer totals, define locations.

| Source | Physical page | Evidence mode | Content mapped / explicit applicability |
|---|---:|---|---|
| DOC-002 | 1 | Fresh layout/render/visual/CPU OCR | Protocol version 1.5 dated 24 July 2015; title and administration. No outcome number. A001. |
| DOC-002 | 2 | Reused layout | Sponsor/coordinator contacts; no applicable scientific quantitative relationship. |
| DOC-002 | 3 | Reused layout | Development personnel and contacts; no applicable scientific quantitative relationship. |
| DOC-002 | 4 | Reused layout | Centers/labs/manufacturer contacts; no applicable scientific quantitative relationship. |
| DOC-002 | 5 | Reused layout | Statistician, management/monitoring and safety contacts; no applicable result number. |
| DOC-002 | 6 | Fresh layout/render/visual/CPU OCR | Contents index; endpoint and power sections located; no independent result. |
| DOC-002 | 7 | Fresh layout/render/visual/CPU OCR | Contents continued; administrative and appendix sections located; no independent result. |
| DOC-002 | 8 | Fresh layout/render/visual/CPU OCR | Abbreviations: AUC=area under curve; ITT=intention to treat; iFOBT=immunochemical fecal occult blood test. |
| DOC-002 | 9 | Reused layout | Abbreviations continued: ROC, SAE, LSI/LSO; no independent result. |
| DOC-002 | 10 | Reused layout | Background estimates, historical sensitivity/AUC/P, planned dose/population/timing. A002–A005. |
| DOC-002 | 11 | Reused layout | Objectives/intervention/duration/endpoints. A006–A008. |
| DOC-002 | 12 | Fresh layout/render/visual/CPU OCR | Study population/criteria and medication washouts. A009. |
| DOC-002 | 13 | Fresh layout/render/visual/CPU OCR | Criteria thresholds and analysis population definition. A010–A011. |
| DOC-002 | 14 | Reused layout | Analysis timing, safety set, planned counts/duration/calendar. A011–A013. |
| DOC-002 | 15 | Reused layout | Historical disease burden, prevention, diagnostic sensitivity/specificity and AUC. A014–A017. |
| DOC-002 | 16 | Fresh layout/render/visual/CPU OCR | Historical ROC Figure 1, dose context, historical sensitivity. A018–A020. |
| DOC-002 | 17 | Reused layout | Historical aspirin subgroup ≈10%; sex availability, multi-day context. A020. |
| DOC-002 | 18 | Fresh layout/render/visual/CPU OCR | Recruitment, blood tubes/test kits, sample and treatment timing. A021–A022. |
| DOC-002 | 19 | Fresh layout/render/visual/CPU OCR | Colonoscopy timing, >3-month sensitivity analysis, no-colonoscopy dropouts. A023. |
| DOC-002 | 20 | Fresh layout/render/visual/CPU OCR | Full Figure 2 study timeline: day0/1/3/4/5, colonoscopy day6 onward. A024. |
| DOC-002 | 21 | Fresh layout/render/visual/CPU OCR | Full Table 1 schedule and all six footnotes. A025. |
| DOC-002 | 22 | Fresh layout/render/visual/CPU OCR | Repeated endpoints and eligibility/washout criteria. A008–A009. |
| DOC-002 | 23 | Fresh layout/render/visual/CPU OCR | Repeated safety thresholds/full exclusions. A010. |
| DOC-002 | 24 | Fresh layout/render/visual/CPU OCR | Comparator/dose/randomization numbers/two reviewers. A026–A027. |
| DOC-002 | 25 | Reused layout | Laboratory assignments and single-dose compliance; optional blood/sample storage. A028. |
| DOC-002 | 26 | Fresh layout/render/visual/CPU OCR | Recruitment counts/time, operational payment and withdrawal reporting. A029–A030. |
| DOC-002 | 27 | Reused layout | Withdrawal timing, >3-month violations, stopping threshold/dropout windows. A030–A031. |
| DOC-002 | 28 | Reused layout | Complete analytic methods and power inputs. A032–A034. |
| DOC-002 | 29 | Reused layout | Specificity expected interval. A035. |
| DOC-002 | 30 | Fresh layout/render/visual/CPU OCR | Safety historical rate/count/risk and pharmacokinetic/lifespan values. A036–A037. |
| DOC-002 | 31 | Fresh layout/render/visual/CPU OCR | Historical platelet/bleeding results and washout relationship. A038–A039. |
| DOC-002 | 32 | Fresh layout/render/visual/CPU OCR | Dose rationale and safety observation/reporting windows. A040–A041. |
| DOC-003 | 1 | Reused layout | SAP title, EudraCT identity and study code; no result number. A001. |
| DOC-003 | 2 | Reused layout | Planned objectives, sample size, eligibility, dose/kits and initial sampling. A042. |
| DOC-003 | 3 | Reused layout | Timing, delayed colonoscopy sensitivity, dropout and datasets. A042–A043. |
| DOC-003 | 4 | Reused layout | Analysis sets, eligibility and explicit day-renumbering footnote. A044–A045. |
| DOC-003 | 5 | Reused layout | Full exclusions and thresholds. A009–A010. |
| DOC-003 | 6 | Reused layout | Variables, unit/threshold definitions, eight pathology levels and secondary metrics. A046–A047. |
| DOC-003 | 7 | Reused layout | Auxiliary day intervals, missing/invalid rules, disposition/baseline tests/compliance. A048–A049. |
| DOC-003 | 8 | Reused layout | Primary/secondary definitions, adjusted intervals, tests, ROC and mixed model. A050–A051. |
| DOC-003 | 9 | Reused layout | Time changes, subgroups/software and section7 explicit amendments. A051–A052. |
| DOC-003 | 10 | Reused layout | References, including interval, ROC and software method citations; no extra independently reported result. A050–A051 context. |

## Complete quantitative and statistical map

Source citations below are package-root filenames plus physical page anchors. All entries have role PLAN. Matching keys identify main-paper topics for later comparison; they do not assert identical populations/results or any discrepancy.

| Key | Exact source locations | Printed inputs, definitions, relationships and matching main-paper key |
|---|---|---|
| A001 | joi190039supp1_prod.pdf#page=1; joi190039supp2_prod.pdf#page=1 | Protocol version1.5 dated24-July-2015; EudraCT2011-005603-32, internal codeK357. SAP same study. Identity key: trial registration/protocol version; identifiers are administrative, not sample counts. |
| A002 | joi190039supp1_prod.pdf#page=10 | Background CRC third most common cancer/fourth cancer death cause; >1.2million new cases and >600000 deaths/year worldwide. Historical contextual quantities, not trial outcomes. |
| A003 | joi190039supp1_prod.pdf#page=10 | Prior observational iFOBT advanced-neoplasm sensitivity ASA70.8% vs nonuser35.9%, P=.001; specificity differences described small. Main matching key: introductory historical aspirin diagnostic study, distinct from randomized trial. |
| A004 | joi190039supp1_prod.pdf#page=10 | Prior study AUC among men0.87 ASA vs0.68 nonuser, P=.003. AUC scale0–1; diagnostic discrimination, not sensitivity percentage. |
| A005 | joi190039supp1_prod.pdf#page=10 | Planned300mg single dose vs placebo, N2400 age40–80, administered≥5days before colonoscopy with≥4full drug-free intervening days. One baseline plus three postdose stool days; two tests. Main keys: dose, sample size, age and day schedule. |
| A006 | joi190039supp1_prod.pdf#page=11 | Main objective six measures for two iFOBTs: sensitivity/specificity/PPV/NPV/LR/AUC for advanced neoplasms. Secondary: sex-specific accuracy, multi-day sampling, single-dose safety, optional biomarkers. |
| A007 | joi190039supp1_prod.pdf#page=11 | Single oral300mg ASA tablet without enteric coating vs single placebo; participant study duration5days, protocol day1=dose day. Colonoscopy outside study. |
| A008 | joi190039supp1_prod.pdf#page=11; joi190039supp1_prod.pdf#page=22 | Primary endpoint sensitivity at predefined positivity cutpoints of FOBGold Tube Screen for advanced neoplasms. Secondary PPV,NPV,specificity,AUC,LR,sex-specific performance,multi-day gain,SAEs. No numerical threshold supplied at these locations. |
| A009 | joi190039supp1_prod.pdf#page=12; joi190039supp1_prod.pdf#page=22; joi190039supp2_prod.pdf#page=4; joi190039supp2_prod.pdf#page=5 | Age40–80; postmenopausal definition≥12months without menstrual bleeding or surgical sterilization. Exclude anticoagulants/antiplatelets within2weeks, ASA within1week, NSAIDs/COX2 inhibitors within3days. Screening or diagnostic colonoscopy allowed, prior CRC/positive-FOBT colonoscopy excluded. Main key: eligibility/analysis population. |
| A010 | joi190039supp1_prod.pdf#page=13; joi190039supp1_prod.pdf#page=23; joi190039supp2_prod.pdf#page=5 | Exclusion thresholds GFR<30ml/min; myocardial infarction in past6months; intended methotrexate≥15mg/week. Other stated exclusions (bleeding, asthma unless ASA tolerated, hypersensitivity, gout, oxaluria, G6PD/glutathione peroxidase deficiency, epilepsy, uncontrolled cardiac conditions, interacting drugs, pregnancy, alcohol/illicit drugs, surgery/noncompliance/other trial) define population, not results. |
| A011 | joi190039supp1_prod.pdf#page=13; joi190039supp1_prod.pdf#page=14 | Diagnostic analyses for population with primary-endpoint test day3 data and available colonoscopy; sex strata. Baseline and three additional days at least2days after dose; combine samples on2or3days. Safety all randomized participants, ITT. |
| A012 | joi190039supp1_prod.pdf#page=14 | N2400 to randomize; N2000 primary endpoint analyzed. Printed anticipated difference400; corresponding retained fraction2000/2400 is a derivable identity, not a printed dropout proportion. |
| A013 | joi190039supp1_prod.pdf#page=14 | Total duration60months; clinical phase48months; preparationQ1/Jan2012; first subjectQ2/June2013; last in/outQ2/June2017; database lockQ3/Sept2017; analysesQ4/Dec2017; reportQ1/March2018. Prospective calendar, not actual recruitment outcome. |
| A014 | joi190039supp1_prod.pdf#page=15 | World >1.2million cases/>600000 deaths/year; Germany>70000 cases/almost30000 deaths/year. CRC prevention60–90% by endoscopic adenoma removal; Germany primary colonoscopy offered sinceOctober2002; FOBT screening reductions20–30% incidence/CRC mortality. Historical/contextual PLAN. |
| A015 | joi190039supp1_prod.pdf#page=15 | Advanced-neoplasm iFOBT sensitivity<50% at cutpoints giving90–95% specificity. Threshold tradeoff context, not trial sensitivity/precision estimate. |
| A016 | joi190039supp1_prod.pdf#page=15 | Prior prospective screening cohortN1979; ASA sensitivity70.8% vs35.9%, P=.001; specificity85.7% vs89.2–91.1% nonusers. Denominators for those historical percentages not supplied here; do not substitute trial denominators. |
| A017 | joi190039supp1_prod.pdf#page=15 | Historical male AUC0.87vs0.68,P=.003; repeated in summary A004. |
| A018 | joi190039supp1_prod.pdf#page=16 | Figure1 male historical RIDASCREEN Hb ROC: bold line=ASA users, thin=nonusers; markers thresholds8,4,2,1μg/g stool. Vertical sensitivity%0–100; lower horizontal100−specificity%0–100; upper specificity axis100–0. No exact coordinate table; curves retained as graphical evidence without invented numeric coordinates. |
| A019 | joi190039supp1_prod.pdf#page=16 | Drug marketed>100years/since1899; study300mg vs normal pain adult500mg; secondary-prevention range75–325mg. Dose contexts differ, not paired trial arms. |
| A020 | joi190039supp1_prod.pdf#page=16; joi190039supp1_prod.pdf#page=17 | Other observational aspirin/NSAID sensitivity51.2%→66.7% without specificity loss; no significant difference/no numerical P. Prior ASA users≈10% and mostly men, insufficient women data. Distinct historical cohorts/mixed drug groups; no trial inference. |
| A021 | joi190039supp1_prod.pdf#page=18 | N2400 age40–80; optional four blood tubes=2EDTA+2serum; four kits for EACH of two tests=eight kits. Randomized single300mg vs placebo. Visitday0, baseline sampleday0or1 before dose; doseday1. |
| A022 | joi190039supp1_prod.pdf#page=18 | Postdose samples protocol days3/4/5 preferably consecutive; delayed collection allowed. Minimum allowed two samples before dose and day3. One kit of each test per collection time; samples before bowel preparation. Sampling day matters for denominator/time key. |
| A023 | joi190039supp1_prod.pdf#page=19 | ≥4ASA-free intervening days before colonoscopy; study-to-colonoscopy maximum3months; >3months triggers sensitivity analyses; absent colonoscopy=dropout. Tests/readouts blinded to treatment and colonoscopy. |
| A024 | joi190039supp1_prod.pdf#page=20 | Figure2 full schedule: day0 appointment/consent/eligibility/questionnaire/optionalblood/randomization/kits/diary/medication supply; day1 both test samples then single medication; day3both; day4both; day5both; trial endsday5; screening/diagnostic colonoscopy fromday6 onward. Matches day1-to-day6 difference5calendar days/four full intervening days. |
| A025 | joi190039supp1_prod.pdf#page=21 | Table1 columns0,day1,day3,day4,day5,colonoscopyfromday6. Consent/eligibility/randomization/exam/parameters/blood/questionnaire/kits at0; dose1; each stool test1,3,4,5; concomitant medication/(S)AE at1,3,4,5andcolonoscopy. Footnotes: parameters age/sex/weight/height/BP; questionnaire family/lifestyle; eightkits; collection may postpone/minimumday1and3; blood2EDTA+2serum; safety interviewbeforecolonoscopy or phonewithin3weeks when colonoscopy>3weeksafterdose. |
| A026 | joi190039supp1_prod.pdf#page=24 | Comparator diagnostic performance in placebo recipients; singleoral300mg ASA orplacebo. Random medication identifiers1–4000; centers receive blocks and use next ascending participant number. Identifier upper bound4000 is not a planned N4000. No block size/allocation ratio stated here. |
| A027 | joi190039supp1_prod.pdf#page=24 | Data extraction/entry by two independent blinded reviewers, discrepancies reconciled; participant level medication/randomization, not cluster allocation. Three envelope sets at center,KKS,DKFZ. Context only unless concretely affects quantitative comparison. |
| A028 | joi190039supp1_prod.pdf#page=25 | Single-dose compliance diary/emptypackage/accountability; FOBGold analyses atLimbach, FDHb/Hp atDKFZ; future biomarkers optional and untimed long-term storage, no additional test result. |
| A029 | joi190039supp1_prod.pdf#page=26 | Operational75euros/recruitedpatient paid after colonoscopy or completed trial if nocolonoscopywithin3months. Prior BliTz4150participants sinceJan2006. Planned2400in48months; add centers if lowrecruitment. Values are feasibility/context, not trial observations. |
| A030 | joi190039supp1_prod.pdf#page=26; joi190039supp1_prod.pdf#page=27 | Withdrawal within3weeks recorded; data retained≥10years. Doseday-to-colonoscopy difference≤4days triggers withdrawal or postpone to achieve4drug-free days; >3months documented violation and sensitivity analysis. Dropout reasons explored/documentedwithin3weeks; no reenrollment/reusedIDs. |
| A031 | joi190039supp1_prod.pdf#page=27 | Study stopping if only25%orless target participants after halfplannedrecruitmenttime and furthercenters unpromising; authoritieswithin15days if prematuretermination. Target2400 and48months elsewhere yield contextual600participants/24months; these are derived thresholds, not separately printed. |
| A032 | joi190039supp1_prod.pdf#page=28 | Diagnostic sensitivity/specificity/LR/PPV/NPV with95%CIs at cutpoints yielding specificity>90%, colonoscopygoldstandard, ASA vsplacebo ITT; primaryFOBGoldday3; whole-rangeROC/AUC; total/sexstrata/advancedadenoma-vs-carcinoma; baseline/postdose/multi-day2or3; bothtests; safetyallrandomized irrespective samples/colonoscopy. Primaryconfirmatory, others exploratory. |
| A033 | joi190039supp1_prod.pdf#page=28 | Power paragraph describes day3 sensitivity/specificity/AUC of two tests, patientsfirstsampleday4dueconstipation excluded. Expectedadvancedneoplasmprevalence10%;100advancedneoplasmsineachoftwogroups. LinkN2000 A012: implied1000participants/group if equalgroups,100diseased/group,900nondiseased/group. Allocation equality is implied by counts, not separately printed ratio here. |
| A034 | joi190039supp1_prod.pdf#page=28 | Baselineplacebosensitivity36%; two-sidedalpha.05withcontinuitycorrection;90%powertodetectASA60%entirepopulation;90%powertodetectASA70%sex-specific; historical71%. Derivable sensitivity increments24/34percentagepoints; sex-specificnumberofdiseasedsubjectsnotexplicitlystated; do not silentlyassumeequalmalefemalesize. |
| A035 | joi190039supp1_prod.pdf#page=29 | Expectedspecificity90%withCI88–92%inbothgroups; intervalconfidencelevel95%specifiedA032. Count/nondiseased denominatorforprecisionnotrepeatedhere; onlyimplied900/grouponA033assumptions. |
| A036 | joi190039supp1_prod.pdf#page=30 | Backgroundlong-termASAabsoluteincreaseupperGIevents.12%peryear; excessmortalityattributableto1-weekuse185per100million, also.000185%overall and.000417%age>60. Countdenominatorandsameprintedpercentareavailablefordirectarithmeticrelationship; age-specificnumeratorabsent. ThesearePLANbackground, nottrialSAEs. |
| A037 | joi190039supp1_prod.pdf#page=30 | Drugdose300mgvs500mgpain/75–325mgprevention, >100yearssince1899; salicylatehalflife2–3hours/nearlyeliminated1day; plateletlifespan10±1days, assumedaggregationnormalization10days, laboratorymarkerwithin2weeks. Differentbiologicalquantities/scales. |
| A038 | joi190039supp1_prod.pdf#page=31 | In-vitroASA-freeplatelets10–40%normalizeaggregation; addition40%→TxB2production40%butaggregation80%; fourvolunteersfunctionalrecovery5–6.8daysvsmeasuredsurvival10.4days; estimated50%functioningplateletsnormalizesaggregation, average5days/7dayslowturnover; PFA100normalizes4–6days, bleedingtime2–4days, mucosalbleeding3days. Historicaldenominators/assaysdiffer. |
| A039 | joi190039supp1_prod.pdf#page=31 | Historicalcolonoscopybleedingincidence.16%withoutpolypectomy/.4–3.4%with; ASA≥onedosewithin1weekbeforeorafterpolypectomy; historicalcohort1174polypectomy patients. Higher-riskproceduresstopASA5days; study≥4fullASA-freedays; <4fullinterveningdayswithdraworpostpone. |
| A040 | joi190039supp1_prod.pdf#page=32 | PriorASAdaily100mg/maxsuppression≈5days; routine loading500mg;300mgsimilarlyeffective; enteric-coated300mgsubmaximalandnotused. Matchesmainstudydose/formulation; otherdosevalueshistoricalcontext. |
| A041 | joi190039supp1_prod.pdf#page=32 | AEobservationprotocol days1–5; ifcolonoscopy>3weeksafterdose phonewithin3weeks; SAEsfollowuntilrecovery/stabilization, reportedwithin24hoursornextworkingday. AEnumerator/timewindowmatchingkey. |
| A042 | joi190039supp2_prod.pdf#page=2; joi190039supp2_prod.pdf#page=3 | SAPcopiesprotocol N2400,age40–80, twoimmunochemicaltests,single300mgvsplacebo,fourkits/test/eighttotal,2EDTA+2serum; consentday0,doseday1,baselineday0or1beforemedication, laterdays3/4/5,optionalminimum2samples. ≥4drugfreedays;maximum3months/delayedsensitivity/nocolonoscopydropout. These day numbers are explicitly renumbered later, A045. |
| A043 | joi190039supp2_prod.pdf#page=3 | Mainanalysisdataset sampledates/diary/colonoscopy/test/questionnaire/demography/randomization/auxiliaries; eCRFeligibility,timing,demography/randomization,vitals,endstudy,AEs. No individual patient values supplied. |
| A044 | joi190039supp2_prod.pdf#page=4 | Fullanalysisset all recruited satisfyingprotocolcriteria, useddemography/compliance. PP≥1validsampleexactexpectedday; baselineanytimebeforeoronsamedayasdose(explicitminorprotocoldeviation), laterday2/3/4; eligibilityandcolonoscopyaftersampleapply. ITS≥1validsamplecollectedbeforecolonoscopyorinformationunavailable. Analysis denominators varybytest/day and subsequentsection7amendment. |
| A045 | joi190039supp2_prod.pdf#page=4 | Footnote1 explicitly redefinesdoseasday0; originaldays3/4/5nowdays2/3/4. Protocolbaseline−1or0undernewnumbering; SAPPPpermitsanypre-doseday. Mainmatchingkey:day2endpoint vsprotocolday3 representssamepostdoseelapsedtime. |
| A046 | joi190039supp2_prod.pdf#page=6 | Demographysexmale/female; consent/birthyears; colonoscopyindicationscreening/diagnostic; weightkg,heightcm,current smoker/nonsmoker. PrimarysensitivityadvancedneoplasmsdefinedCRC oradvancedadenoma; quantitativeFOBGoldunitngHb/mlbuffer; qualitativepositive/negative/invalid. Positivity17μgHb/gfecesandlower10.2Hb/gfeces (sourceomitsμginthe secondprintedunit); do not silently correct unit omission. |
| A047 | joi190039supp2_prod.pdf#page=6 | EightmostadvancedcolonoscopyfindingsCRC,advancedadenoma,SSP≥1cm,SSP<1cm,nonadvancedadenoma,hyperplasticpolyp,undefinedpolyp,nofinding. FDHb/Hpoutcomepositive/weaklypositive/negative/invalid. SecondaryFDsensitivity/FOBGoldAUC/bothtestsspecificity/LR/PPV/NPV/testsneeded/colonoscopiesneeded. Mainmatchingkey:pathologydefinition/advancedneoplasm/comparator thresholds. |
| A048 | joi190039supp2_prod.pdf#page=7 | Twoauxiliaryintervalsindays:sampledate−dosedate;colonoscopydate−sampledate. Originalmissingtest/sampledayexcluded;invalidtesttreatedmissing; multipletestsamedayfirstvalidinsequenceused. Latersection7changemissingdayrulesA052 must be retained. |
| A049 | joi190039supp2_prod.pdf#page=7 | CONSORTrecruited/fullset/excludedreasons; age=consentyear−birthyear,5-yearclasses; absolutefrequency/%overallandarm; chisquareorFisherexactarmtests. Compliancecountsstratifiedexpectedcollectionday/test/arm,missing/invalid. |
| A050 | joi190039supp2_prod.pdf#page=8 | Primarysensitivitypositivetestamongdiseased. Threshold17μgHb/gmanufacturerand10.2μgHb/gcalledFDHb/HpComplexquicktestthresholdintheprimaryanalysisparagraph; preservewordingforlaterlabelmatching. NullnoASA-vsplacebosensitivitychange; originalPPday2. WaldadjustedCI:Agresti–Coullforproportions,Agresti–Caffoforarmdifferences; two-sidedP<.05. SAPdoesnotstateexplicitP-valuetestformulaorcontinuitycorrectionhere; namedCIformulaalonecannotbeassumedthePformula. |
| A051 | joi190039supp2_prod.pdf#page=8; joi190039supp2_prod.pdf#page=9 | Complete secondary definitions/methods, temporal and subgroup relationships detailed below. |
| A052 | joi190039supp2_prod.pdf#page=9 | Section7Changes: primarynowITSday2; missingcollectiondayincludedconsistentwithITS; test independenceofprimaryFOBGoldday2ITSmissingoutcomefromarmusingFisherexact, evaluateproportionmissing, decidehandlingfromboth. Mainmatchingkey: primaryanalysisset/missingoutcomes/test. Disclosedchangecontext, not automaticallycontradiction. |

## A051 — individual secondary inferential relationships

All locations are joi190039supp2_prod.pdf#page=8 unless stated otherwise. Definitions use participant counts, not person-time rates. No results estimates are supplied by the SAP.

1. FD Hb/Hp positivity = positive OR weakly positive; sensitivity = positive among diseased.
2. Specificity = negative among healthy; PPV = diseased among positive; NPV = healthy among negative. With TP/FP/TN/FN these definitions imply denominators TP+FN, TN+FP, TP+FP, TN+FN respectively. This is a source-grounded algebraic translation, not a printed 2×2 table.
3. Likelihood ratio of given test result = probability of that result among diseased divided by probability among healthy; consequently positive/negative LR use different numerator/denominator test outcomes.
4. ROC plots positive proportion among healthy against sensitivity for increasing thresholds; total AUC and partial AUC truncated at specificity .8; significance level .05; DeLong OR bootstrap through pROC. Source explicitly permits two methods, so later comparisons require matched method rather than assuming one.
5. Number of iFOBTs needed per detected advanced neoplasm = total performed iFOBTs / positive tests among diseased; colonoscopies needed = total positive iFOBTs / positive tests among diseased. Test counts versus persons and multiple-day combinations must remain distinct in denominator checking.
6. Null no ASA-placebo change in FD sensitivity, and in both-test specificity/PPV/NPV; adjusted Wald Agresti–Coull intervals for values and Agresti–Caffo intervals for differences; two-sided P<.05. CI for tests/colonoscopies-needed also says Wald Agresti–Coull; source does not print transform formula.
7. Generalized mixed effects binomial logit model responses sensitivity or specificity; predictors arm, sex, test, stool day; random intercept for repeated measurements on same participant. Do not compare adjusted model estimates directly to unadjusted count differences without matching.
8. Secondary analyses PP and ITS day2; PP sensitivity/specificity day0 before medication and days2/3/4, differences eachpostdoseday minus day0; graphical changes and combined multiple days. Old day-number mapping A045 applies.
9. Serious adverse events evaluated/listed (p.9).
10. Sex, age<60 vs≥60, current smoking, BMI<25 vs≥25kg/m² stratify sensitivity/specificity (p.9). BMI=weightkg/(heightmeters squared). Pathology sensitivity additionally stratified SSP≥1cm and advancedadenoma. Colonoscopy category/endpoint matching needs A046–A047; no unsupplied redefinition is made here.
11. Binomial logit generalized linear model assesses stratification interaction coefficient at .05 (p.9). This is interaction testing, distinct from comparing significance within two strata.
12. R for all analyses; PropCIs for sensitivity/specificity CI and pROC for ROC/AUC/significance (p.9). Method citations on p.10 provide named sources only; no external article was accessed.

## Limits and handoff

No scientific coverage gap. Fresh native extraction retained embedded-font corruption; direct page images and visual transcription resolved all assigned content. Targeted OCR supports navigation and is not source authority. Historical ROC exact coordinates are not tabulated; only labels, directions, thresholds and visual curves are supplied. Several prospective statistics lack exact formulas/denominators, so their unspecified inputs are explicitly named rather than invented. All matching main keys are topic locators: result-level numerical identity must be established by downstream reviewers. Scope outside DOC-002 pp.1–32 and DOC-003 pp.1–10 is owned by separate agents and not asserted covered here.

Fresh derivatives completion: all 18 native layout files, all 18 full-page PNG files, and all 18 OCR text files exist under the unique `preprocessing/support-a/` path (54 derivatives total). Local verification counted exactly 42 source coverage rows. Scientific mapping emitted 52 local evidence keys, with A051 expanded into 12 individually specified definition/statistical-method relationships. No direct source or reused asset was edited.
