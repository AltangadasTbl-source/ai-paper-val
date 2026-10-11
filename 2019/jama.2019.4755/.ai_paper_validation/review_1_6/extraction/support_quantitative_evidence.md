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
# Support evidence mapping — shard B

Scope: DOC-002 physical PDF pp.33–62 (PLAN); DOC-004 pp.1–8 (REPORT); DOC-005 p.1 (REPORT). COMPLETE: 39/39 physical pages mapped, including 17 fresh-required protocol units. No candidate diagnosis, global relationship ID, or historical conclusion is used. Local keys B001–B071 are mapping keys only. Sources and reused derivatives were not modified. No Office/CSV source exists; workbook formulas and cached values are not applicable.

## Engines, commands, and evidence precedence

Direct tools available under tooling_record.md were used: Poppler pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 CPU, English, psm 6. Source-linked reusable assets: review_1_5_1/preprocessing/support/DOC-002_pp1-62_layout.txt, DOC-004_pp1-3_layout.txt, DOC-005_p1_layout.txt; document_outputs/doc-b45e07a04d82/normalized_pages/page-4.txt through page-8.txt and ocr_pages/page-5.png through page-8.png. These paths are under .ai_paper_validation/. Every listed fresh unit was opened visually using its new full-page PNG. Supplement pp.5–8 were visually opened; p7 was additionally freshly rendered to resolve placement.

Fresh derivatives all reside in .ai_paper_validation/review_1_6/preprocessing/. For each N in 34,35,37,38,40,41,44,49,51,52,53,54,56,57,58,61,62, the exact command pattern was:

```bash
pdftotext -layout -f "$N" -l "$N" joi190039supp1_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N-layout.txt"
pdftoppm -r 110 -f "$N" -l "$N" -singlefile -png joi190039supp1_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N"
tesseract ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N.png" ".ai_paper_validation/review_1_6/preprocessing/support-b-protocol-$N-ocr" -l eng --psm 6
```

Output triplet: support-b-protocol-N-layout.txt, support-b-protocol-N.png, support-b-protocol-N-ocr.txt. OCR is a locator only; English semantic mapping below is based on readable source image where font encoding or German OCR is imperfect. Additional direct locators: `pdftotext -layout -f 33 -l 62 joi190039supp1_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-b-protocol-33-62-layout.txt`; `pdftoppm -r 180 -f 7 -l 7 -singlefile -png joi190039supp3_prod.pdf .ai_paper_validation/review_1_6/preprocessing/support-b-results-7`; same render for protocol p61 with prefix support-b-protocol-61-detail. No fallback environment needed.

## Pagewise coverage

PDF links are relative to this extraction artifact. Physical PDF pages are authoritative; protocol physical pp.49 and 50 both print page49, and pp.51–62 print pages50–61.

| Source/page | Basis | Mapped content | Status |
|---|---|---|---|
| DOC-002 33 | Reusable | SUSAR deadlines, follow-up windows, unblinding and sampling burden; B001 | COMPLETE |
| DOC-002 34 | Fresh layout/render/OCR + visual | Three-month colonoscopy window and reinclusion, optional biomarkers; B002 | COMPLETE |
| DOC-002 35 | Fresh layout/render/OCR + visual | Administrative deadlines; B003; no study result | COMPLETE |
| DOC-002 36 | Reusable | Ten-year retention; B004; no study result | COMPLETE |
| DOC-002 37 | Fresh layout/render/OCR + visual | eCRF medication history two weeks, dropout three weeks; B005 | COMPLETE |
| DOC-002 38 | Fresh layout/render/OCR + visual | Diary dates, ten-year participant-list retention; B006 | COMPLETE |
| DOC-002 39 | Reusable | Funding points to Appendix4; no applicable result or displayed quantity | COMPLETE |
| DOC-002 40 | Fresh layout/render/OCR + visual | Double entry, four monitoring visits/year and first after ~20 patients; B007 | COMPLETE |
| DOC-002 41 | Fresh layout/render/OCR + visual | Monitoring/steering/publication policy; no applicable inferential result; contextual one meeting before start | COMPLETE |
| DOC-002 42 | Reusable | 300mg, day1 administration, storage, platelet/PK quantities; B008 | COMPLETE |
| DOC-002 43 | Reusable | PK half-lives and packaging; B009 | COMPLETE |
| DOC-002 44 | Fresh layout/render/OCR + visual | Storage below25°C and accountability; B010 | COMPLETE |
| DOC-002 45 | Reusable | References1–16 only; no applicable extracted results | COMPLETE |
| DOC-002 46 | Reusable | References17–34 only; no applicable extracted results | COMPLETE |
| DOC-002 47 | Reusable | References35–51 only; numeric study-title context1657 cases,10-year study, aspirin300/75/300mg; no supplied result | COMPLETE |
| DOC-002 48 | Reusable | Reference52 only; no applicable result | COMPLETE |
| DOC-002 49 | Fresh render/OCR + visual | Scanned signed approval page, not blank; dates only; no applicable result | COMPLETE |
| DOC-002 50 | Reusable | Unsigned duplicate signature form; no applicable quantitative result | COMPLETE |
| DOC-002 51 | Fresh layout/render/OCR + visual | AE/SAE/expectedness definitions; B011 | COMPLETE |
| DOC-002 52 | Fresh layout/render/OCR + visual | SUSAR, intensity and causality definitions; B012 | COMPLETE |
| DOC-002 53 | Fresh layout/render/OCR + visual | Reporting24h,3 working days/72h,7+8days,15days; B013 | COMPLETE |
| DOC-002 54 | Fresh layout/render/OCR + visual | AE outcome/action categories and fatal-event counting rule; B014 | COMPLETE |
| DOC-002 55 | Reusable | Appendix1 references3–4 only; no applicable result | COMPLETE |
| DOC-002 56 | Fresh layout/render/OCR + visual | Optional blood volumes/timing/storage; B015 | COMPLETE |
| DOC-002 57 | Fresh layout/render/OCR + visual | Laboratory contacts only; no applicable result | COMPLETE |
| DOC-002 58 | Fresh layout/render/OCR + visual | Investigator signature form only; no applicable result | COMPLETE |
| DOC-002 59 | Reusable | Financial table rows1–4; B016 | COMPLETE |
| DOC-002 60 | Reusable | Financial table rows5–12; B017 | COMPLETE |
| DOC-002 61 | Fresh layout/render/OCR + visual | Financial rows13–16,total and footnotes1–12; B018 | COMPLETE |
| DOC-002 62 | Fresh layout/render/OCR + visual | Financial footnotes13–18; B019 | COMPLETE |
| DOC-004 1 | Reusable | Contents eTables1–6; no independent result | COMPLETE |
| DOC-004 2 | Reusable | Eligibility and thresholds; B020 | COMPLETE |
| DOC-004 3 | Reusable | Eligibility continuation; B021 | COMPLETE |
| DOC-004 4 | Reusable | eTable2:20 rows,all counts/footnotes; B022–B041 | COMPLETE |
| DOC-004 5 | Reusable + visual | eTable3:9 rows,all counts/percentages/CIs; B042–B050 | COMPLETE |
| DOC-004 6 | Reusable + visual | eTable4:9 rows,all counts/percentages/CIs; B051–B059 | COMPLETE |
| DOC-004 7 | Reusable + fresh render/visual | eTable5:9 rows,all values/CIs and header placement; B060–B068 | COMPLETE |
| DOC-004 8 | Reusable + visual | eTable6:9 rows,18SD/P pairs; B069 | COMPLETE |
| DOC-005 1 | Reusable | Protocol/code/data availability; B070 | COMPLETE |

## PLAN relationships: operational, historical and contextual content

B001 [protocol p33](../../../joi190039supp1_prod.pdf#page=33): SUSAR reporting within15days,7days if deadly/life-threatening; DSUR once/year or request. Participant missing colonoscopy contacted within3weeks after medication; new appointment within3months of randomization. Unblinding envelopes: one set each at study centers,KKS,DKFZ. Stool collection device one/day. These are planned windows/counts, not observed outcomes.

B002 [protocol p34](../../../joi190039supp1_prod.pdf#page=34): colonoscopy gold standard; FIT results usually not returned. If colonoscopy absent within3months after randomization, agreed positive stool result sent to gastroenterologist; patients undergoing colonoscopy after more than3months can be reincluded. Biomarkers optional and research-only; no specified analysis time or result.

B003 [protocol p35](../../../joi190039supp1_prod.pdf#page=35): planned study end notified within90days; premature end within15days; clinical report within1year. Framework versions2008/2006/2004 are administrative context. B004 [p36](../../../joi190039supp1_prod.pdf#page=36): participant identification lists and all documentation retained at least10years. B005 [p37](../../../joi190039supp1_prod.pdf#page=37): eCRF includes medication within2weeks before start and date/reason of dropout within3weeks. B006 [p38](../../../joi190039supp1_prod.pdf#page=38): diary records whether/when medication/stool collection occurred; participant list includes randomized number only available after randomization, screening failures logged; list retained10years after study. Drug accountability records kept for years without precise duration here.

B007 [p40](../../../joi190039supp1_prod.pdf#page=40): diary/histology/colonoscopy entered by two independent blinded reviewers; planned monitoring4visits/center/year excluding initiation/close-out, two KKS and two DKFZ; first KKS after around20patients/center, variable with quality. B008 [p42](../../../joi190039supp1_prod.pdf#page=42): oral aspirin300mg/tablet, study day1 one glass water; storage not above25°C protected from humidity; placebo not above25°C. Background platelet replacement10–15%/day, aggregatory normalization4–6days because50%functioning platelets suffice. Tmax0.5–2hours; volume distribution0.16L/kg; plasma binding>90%. B009 [p43](../../../joi190039supp1_prod.pdf#page=43): unmetabolized ASA urine1%total intake; half-life ASA15–20min, salicylic acid2–3hours. RITA software version1.24; primary blister1tablet/unit. B010 [p44](../../../joi190039supp1_prod.pdf#page=44): medication below25°C protected from humidity. No trial efficacy statistics on these pages.

B011 [p51](../../../joi190039supp1_prod.pdf#page=51): AE is temporally associated untoward medical occurrence without necessary causality; pre-existing condition counts only if worsened; surgery itself not AE, underlying condition may be; planned surgery and pre-existing indication excluded. SAE criteria death,life-threatening,hospitalization/prolongation,persistent/significant disability/incapacity,congenital anomaly. Unexpected nature/severity inconsistent with product information or new specificity/severity/frequency information. B012 [p52](../../../joi190039supp1_prod.pdf#page=52): SUSAR requires suspected drug relationship plus unexpectedness plus seriousness. Intensity mild/moderate/severe based on everyday-activity interference; causality certain,probable,possible,unlikely,not assessable,not related. These classify safety counts, not statistical estimates.

B013 [p53](../../../joi190039supp1_prod.pdf#page=53): SAE report within24hours or next working day; independent second assessor within next3working days(72hours as printed). Fatal/life-threatening SUSAR notice within7calendar days,follow-up additional8calendar days; other SUSAR/safety within15calendar days. B014 [p54](../../../joi190039supp1_prod.pdf#page=54): each SUSAR single case; outcome categories recovered,resolving,unresolved,recovered with sequel,fatal,unknown. If multiple AEs only event leading to death(possibly related) classified fatal. IMP actions unknown,not applicable,none,drug treatment,other.

B015 [p56](../../../joi190039supp1_prod.pdf#page=56): first appointmentday0 optional blood4extra tubes9–10mL each(2EDTA,2serum). Specified serum8.5–9mL: Sarstedt9mL type02.1388 or Vacutainer8.5mL type367953. EDTA9–10mL: Sarstedt9mL type06.1664.001(K3) or Vacutainer10mL type367525(K2). Serum room-temperature30min,max60min; centrifuge10min2500–3500RPM. EDTA invert8–10times. Store4–8°C,pickup2–3days; laboratory centrifugation2500–3500RPM/aliquot same day; aliquots−20°C. No biomarker outcomes supplied.

### Financial plan table and formulas (all EUR)

B016 [p59](../../../joi190039supp1_prod.pdf#page=59): printed rows and component values, translated into English.

| Row | Total | Components in displayed order |
|---|---:|---|
|1 KKS project management|13,383|Protocol4,424; patient information1,580; insurance632; ethics application3,476; authority application2,528; local authority395; closure348|
|2 Internal project management|153,000|No itemized cells on this page|
|3 Clinical pharmacology management|30,950|Protocol8,000; information2,000; ethics/authority400; site/physician qualification650; SAE/SUSAR assessment10,000; amendments800; monitoring reports/DSUR3,200; steering300; final report5,600|
|4 Monitoring quality control|24,790|Investigator folder1,776; manual1,184; training1,184; initiation2,131; regular monitoring14,208; close-out1,421; site support2,886 continues p60|

B017 [p60](../../../joi190039supp1_prod.pdf#page=60):

|Row|Total|Components|
|---|---:|---|
|5 Monitoring travel|3,000|No itemized amount|
|6 Pharmacovigilance|28,922|Safety protocol884; manual2,272; SAE/SUSAR capture/report15,600; safety reports8,616; SAE listings1.704(as printed); structures1,548|
|7 Data management including eCRF|40,642|Plan504; database7,288; adverse-event coding nz; status189; queries15,309; database closure1,008; transfer1,008; MACRO license10,800; support4,536|
|8 General KKS project costs|12,731|Meetings2,592; central folder5,573; coordination4,566; audits nz|
|9 Practice compensation|60,000|Footnote6|
|10 Medication/blistering|3,400|No itemized amount|
|11 Investigator/GCP training|2,430|Footnote7|
|12 Laboratory|24,881|Courier1,440; supplies2,388; materials6,107; shipping546; measurements14,400(last3 p61)|

B018 [p61](../../../joi190039supp1_prod.pdf#page=61): row13 other meetings500; row14 ethics/BfArM fees6,800; row15 insurance67,116; row16 general costs35,060(itemized printing3,000; shipping31,080; meeting/hotel980). Study budget505,570. Overhead,tax,total including overhead/tax,contract funds,own funds,total available funds blank. Double-asterisk means total cost of subsequent items. Budget content is PLAN administrative numeric evidence, not reported clinical results.

Footnotes1–12, visually read and translated preserving printed operations: (1) ethics registration2,528 plus other ethics948; (2) TV-L E13 salary50% for3years30,000×3 plus E9 salary50% for3years21,000×3; (3) monitoring per ICH E6/SOP; (4) KKS2visits/year×3years, train80 plus53/hour plus possible hotel80, printed1,596; Benscheid/Zaineddin2visits/year×3years,80/person train, printed480; minimum total2,076; (5) assumes1/20participants SAE,100×150, and1/1000 SUSAR,2×300; (6)30/completed case,printed30×2000; (7)3physicians training650×3=1,950,hotel80×3=240,train80×3=240,total2,430; (8)blood pickup0.3/sample×2samples×2400=1,440; (9)2plasma+2serum tubes/person,100plasma tubes27.7,100serum tubes26.6 **as visually printed** (reusable text says26.9, source wins); (10)8protective tubes/person,2400participants,500tubes133,plus1,000stool collection aids; (11)3.5/delivery to DKFZ weekly52weeks×3years=546; (12)1.5/FOBGold TubeScreen measurement×4samples/person×2400=14,400.

B019 [p62](../../../joi190039supp1_prod.pdf#page=62): (13) travel/food no number; (14)BfArM study registration1,700,annual report1,000,amendment700,assume3amendments; (15)23.50/person×2400; (16)5000flyers350–500,3000questionnairesaverage1,045beforetax,all study document printing3,500,additional color costs possible; (17)postage1.45×2400=3,480,stool shipping2.25×4×2400=21,600,practice document shipping2400×2.50=6,000,total31,080; (18)1study meeting/year,4meetings total,hotel80,travelUlm/Heidelberg80 for3persons=480,additional possible500.

## REPORT definitions and matching keys

B020 [results p2](../../../joi190039supp3_prod.pdf#page=2): eligibility age40–80both sexes; postmenopause no bleeding≥12months or surgical sterilization; premenopause negative pregnancy test; planned screening/diagnostic colonoscopy. Excluded anticoagulants/antiplatelets within2weeks,ASA within1week,NSAIDs/COX2 within3days; severe kidney/liver disease GFR<30mL/min. B021 [p3](../../../joi190039supp3_prod.pdf#page=3): cardiac exclusions MI past6months; planned methotrexate≥15mg/week; other clinical/administrative exclusions without numeric result.

Matching main-paper keys: eTable2 connects returned/valid tests and planned versus actual sampling day to main participant flow/analysis populations. eTable3 connects multi-sample detection sensitivity/specificity to main secondary outcomes. eTables4–5 connect day2 per-protocol detection/predictive values to main day2 intention-to-screen Tables2–3 after explicit population matching. eTable6 connects site random-effects sensitivity analysis to main Results and statistical definitions. These are matching keys, not equality claims across differing populations.

### eTable2 complete cells

[DOC-004 p4](../../../joi190039supp3_prod.pdf#page=4). Intervention N1075; control N1059. Columns below: scheduled day; returned; valid; actual-day bins Missing,<0,0,1,2,3,4,>4. All cells N(count), never percentages. Scheduled day relative tablet intake. Valid requires valid result and sample before colonoscopy(or information unavailable). Actual day2 samples used per-protocol. “Any” aggregates sample records across scheduled occasions, not necessarily unique persons.

|Key|Group/test|Scheduled|Returned|Valid|Missing|<0|0|1|2|3|4|>4|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|B022|Intervention quantitative|≤0|1044|1026|82|152|781|9|1|0|0|1|
|B023|Intervention quantitative|2|1045|1030|77|2|11|126|758|48|5|3|
|B024|Intervention quantitative|3|989|975|77|1|0|9|105|700|65|18|
|B025|Intervention quantitative|4|955|944|64|1|0|0|7|93|677|102|
|B026|Intervention quantitative|Any|4033|3975|300|156|792|144|871|841|747|124|
|B027|Intervention qualitative|≤0|1037|970|78|149|733|8|1|0|0|1|
|B028|Intervention qualitative|2|1040|974|75|2|9|121|719|42|4|2|
|B029|Intervention qualitative|3|979|922|71|1|0|9|97|663|65|16|
|B030|Intervention qualitative|4|955|887|60|1|0|0|7|88|638|93|
|B031|Intervention qualitative|Any|4011|3753|284|153|742|138|824|793|707|112|
|B032|Control quantitative|≤0|1016|1000|80|159|753|5|2|0|0|1|
|B033|Control quantitative|2|1024|1012|78|2|4|136|747|38|4|3|
|B034|Control quantitative|3|987|979|75|1|1|5|114|706|58|19|
|B035|Control quantitative|4|959|947|72|1|0|1|1|104|656|112|
|B036|Control quantitative|Any|3986|3938|305|163|758|147|864|848|718|135|
|B037|Control qualitative|≤0|1026|968|76|149|735|5|2|0|0|1|
|B038|Control qualitative|2|1024|969|72|2|4|126|720|39|3|3|
|B039|Control qualitative|3|979|934|73|1|1|5|108|677|51|18|
|B040|Control qualitative|4|956|905|66|1|0|1|1|103|627|106|
|B041|Control qualitative|Any|3985|3776|287|153|740|137|831|819|681|128|

### eTable3 complete cells

[DOC-004 p5](../../../joi190039supp3_prod.pdf#page=5). Advanced neoplasms=CRC or advanced adenoma; one300mg aspirin/placebo; at least one positive among up to3samples scheduled days2,3,4. Cutoff µgHb/g. A=aspirin,P=placebo tuples each ordered TP,FN,TN,FP,Se%,Sp%; differences percentage points A−P with95%CI. TP/FN disease-positive; TN/FP disease-negative. Sensitivity=TP/(TP+FN),specificity=TN/(TN+FP) are reconstruction identities; interval method not stated on this page. No P values.

|Key|Sex/test/cutoff|A tuple|P tuple|Se difference [CI]|Sp difference [CI]|
|---|---|---|---|---|---|
|B042|All quantitative10.2|63,50,685,261,55.8,72.4|49,58,774,161,45.8,82.8|10.0[-3.3,22.8]|-10.4[-14.1,-6.6]|
|B043|All quantitative17.0|44,69,816,130,38.9,86.3|35,72,852,83,32.7,91.1|6.2[-6.4,18.7]|-4.9[-7.7,-2.0]|
|B044|All qualitative10.2|53,58,714,222,47.7,76.3|35,73,779,146,32.4,84.2|15.3[2.3,27.8]|-7.9[-11.5,-4.3]|
|B045|Men quantitative10.2|46,31,311,148,59.7,67.8|28,30,362,102,48.3,78.0|11.5[-5.5,27.8]|-10.3[-15.9,-4.5]|
|B046|Men quantitative17.0|34,43,384,75,44.2,83.7|22,36,408,56,37.9,87.9|6.2[-10.5,22.4]|-4.3[-8.8,0.3]|
|B047|Men qualitative10.2|41,34,343,111,54.7,75.6|19,40,372,89,32.2,80.7|22.5[5.6,38.0]|-5.1[-10.5,0.2]|
|B048|Women quantitative10.2|17,19,374,113,47.2,76.8|21,28,412,59,42.9,87.5|4.4[-16.7,25.1]|-10.7[-15.4,-5.8]|
|B049|Women quantitative17.0|10,26,432,55,27.8,88.7|13,36,444,27,26.5,94.3|1.2[-17.4,20.4]|-5.6[-9.1,-2.0]|
|B050|Women qualitative10.2|12,24,371,111,33.3,77.0|16,33,407,57,32.7,87.7|0.7[-19.0,20.7]|-10.7[-15.5,-5.9]|

### eTable4 complete cells

[DOC-004 p6](../../../joi190039supp3_prod.pdf#page=6). Same definitions/order as eTable3; day2 per-protocol rather than combined samples. All arm count cells and Se/Sp percentages preserved, all differences95%CI.

|Key|Sex/test/cutoff|A tuple|P tuple|Se difference [CI]|Sp difference [CI]|
|---|---|---|---|---|---|
|B051|All quantitative10.2|42,56,635,136,42.9,82.4|25,61,691,85,29.1,89.0|13.8[-0.1,27.1]|-6.7[-10.1,-3.2]|
|B052|All quantitative17.0|29,69,704,67,29.6,91.3|18,68,735,41,20.9,94.7|8.7[-4.0,20.8]|-3.4[-5.9,-0.8]|
|B053|All qualitative10.2|30,56,617,119,34.9,83.8|19,65,683,62,22.6,91.7|12.3[-1.4,25.4]|-7.8[-11.2,-4.5]|
|B054|Men quantitative10.2|31,34,310,78,47.7,79.9|11,34,344,58,24.4,85.6|23.2[5.0,39.5]|-5.7[-10.9,-0.4]|
|B055|Men quantitative17.0|23,42,350,38,35.4,90.2|9,36,373,29,20.0,92.8|15.4[-1.8,30.9]|-2.6[-6.5,1.4]|
|B056|Men qualitative10.2|24,33,311,63,42.1,83.2|9,37,353,40,19.6,89.8|22.5[4.5,38.6]|-6.7[-11.5,-1.8]|
|B057|Women quantitative10.2|11,22,325,58,33.3,84.9|14,27,347,27,34.1,92.8|-0.8[-21.8,20.6]|-7.9[-12.3,-3.4]|
|B058|Women quantitative17.0|6,27,354,29,18.2,92.4|9,32,362,12,22.0,96.8|-3.8[-21.6,15.0]|-4.4[-7.6,-1.1]|
|B059|Women qualitative10.2|6,23,306,56,20.7,84.5|10,28,330,22,26.3,93.8|-5.6[-25.1,15.3]|-9.2[-13.7,-4.6]|

### eTable5 complete cells and source/extraction placement facts

[DOC-004 p7](../../../joi190039supp3_prod.pdf#page=7). Caption day2,one300mg aspirin/placebo,advanced neoplasms,per-protocol. PPV/NPV in%; tuples A/P=(PPV,NPV),differences percentage points95%CI. Reconstruction identities PPV=TP/(TP+FP),NPV=TN/(TN+FN); counts from matched eTable4 rows, but equality is not assumed without checking. Printed cutoff header visibly reads `[µg` without visible `Hb/g]`, while native extraction supplies `[µg Hb/g]` in displaced order. Preserve display and text separately. Women difference cells visibly show a minus glyph alone in fresh Poppler180dpi render; extracted number fragments18.2,25.7,21.6 are displaced across lines. Mapping below records minus-only display and corresponding native-text fragments; no correction is assigned.

|Key|Sex/test/cutoff|A PPV,NPV|P PPV,NPV|PPV difference [CI]|NPV difference [CI]|
|---|---|---|---|---|---|
|B060|All quantitative10.2|23.6,91.9|22.7,91.9|0.9[-9.3,10.7]|0.0[-2.8,2.8]|
|B061|All quantitative17.0|30.2,91.1|30.5,91.5|-0.3[-15.3,14.2]|-0.5[-3.3,2.3]|
|B062|All qualitative10.2|20.1,91.7|23.5,91.3|-3.3[-14.8,7.7]|0.4[-2.6,3.3]|
|B063|Men quantitative10.2|28.4,90.1|15.9,91.0|12.5[-0.2,24.1]|-0.9[-5.2,3.4]|
|B064|Men quantitative17.0|37.7,89.3|23.7,91.2|14.0[-4.9,31.1]|-1.9[-6.1,2.2]|
|B065|Men qualitative10.2|27.6,90.4|18.4,90.5|9.2[-5.9,22.8]|-0.1[-4.4,4.2]|
|B066|Women quantitative10.2|15.9,93.7|34.1,92.8|minus-only display; native18.2[-34.7,-1.3]|0.9[-2.9,4.6]|
|B067|Women quantitative17.0|17.1,92.9|42.9,91.9|minus-only display; native25.7[-48.4,-0.7]|1.0[-2.7,4.8]|
|B068|Women qualitative10.2|9.7,93.0|31.2,92.2|minus-only display; native21.6[-38.9,-3.9]|0.8[-3.2,4.8]|

Abbreviations: CI confidence interval,FIT fecal immunochemical test,g gram,Hb hemoglobin,NPV negative predictive value,PPV positive predictive value. No P values supplied. Source display placement versus extracted hidden/misaligned text is a derivative limitation, fully mapped for review.

### eTable6 complete cells

B069 [DOC-004 p8](../../../joi190039supp3_prod.pdf#page=8): site-effect sensitivity analysis. GLMM random-intercept standard deviations with corresponding likelihood-ratio P values. Null SD=0,alternativeSD>0. Successful outcome is agreement between test and colonoscopy for advanced neoplasms at day2 after single300mg aspirin/placebo; intention-to-screen. Cutoff µgHb/g. No arm-specific SDs,counts,confidence intervals or LRT statistics supplied.

|Sex/test/cutoff|Sensitivity SD|Sensitivity P|Specificity SD|Specificity P|
|---|---:|---:|---:|---:|
|All quantitative10.2|0.00E+00|0.50|5.49E-03|0.38|
|All quantitative17.0|1.97E-01|0.16|0.00E+00|0.50|
|All qualitative10.2|0.00E+00|0.50|9.23E-03|0.30|
|Men quantitative10.2|0.00E+00|0.50|1.00E-14|0.50|
|Men quantitative17.0|0.00E+00|0.50|1.47E-02|0.40|
|Men qualitative10.2|0.00E+00|0.50|1.13E-02|0.35|
|Women quantitative10.2|0.00E+00|0.50|1.79E-12|0.50|
|Women quantitative17.0|1.67E-01|0.40|0.00E+00|0.50|
|Women qualitative10.2|4.35E-16|0.50|0.00E+00|0.50|

B070 [DOC-005 p1](../../../joi190039supp4_prod.pdf#page=1): retrospective availability statement says protocol published2018;18(1):914; statistical code available from Silvia Calderazzo; dataset not available. No supplied data/code contents or quantitative trial result. REPORT role by content, not a prospective PLAN.

B071 cross-table definition inventory: eTables3–4 counts N,Se/Sp%,eTable5 predictive values%,effect differences percentage points with95%CI; comparator aspirin minus placebo inferred from displayed signed arm contrasts and requires same sex,test,cutoff,time,population. eTable2 sample-level totals require valid/before-colonoscopy rule and actual-day bins. eTable6 SDs are model parameters, not diagnostic percentages or standard errors. Neither effect OR/RR/HR nor person-time rates occur in this scope.

## Completion and limitations

39unique pages complete;17fresh-required protocol pages rendered,OCR-located and visually inspected;22reusable-backed pages covered. eTables2–6 contain56 individually reconstructed rows:20sample-count,9combined-detection,9per-protocol detection,9predictive-value,9site-effect. All18site SD/P pairs and54difference/CI pairs in eTables3–5 retained. Pages45–48,50,55,57,58 and results cover/availability were explicitly opened from reusable content; no applicable trial results recorded. Protocol p49 signed approval scan was visually confirmed as nonblank. No scientific coverage gap remains. Derivative font corruption, low-quality German OCR and eTable5 hidden/displaced numeric text remain recorded transcription/display limitations; final recheck must use supplied PDFs. No source/reused asset changed; no web,GPU,arbitrary Python or old scientific disposition used.
