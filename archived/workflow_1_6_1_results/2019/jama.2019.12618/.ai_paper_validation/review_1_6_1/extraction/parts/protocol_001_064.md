# DOC-003 support evidence map: PDF pages 1–64

Role: PLAN. Scope is exactly joi190092supp2_prod.pdf PDF pages 1–64, comprising the original protocol/MOP (September 4, 2012 headers; September 11, 2012 DSMC cover) and the final protocol title page (January 06, 2017, version 4.5) at p64. All 64 units mapped: 60 reusable-backed and 4 fresh-required (p15, p18, p19 and p47). No uncovered scientific units. No findings or candidate judgments are made here. Stable global N/S identifiers are assigned by the canonical-map coordinator.

Evidence engines: reusable source-matched Poppler layout text in review_1_5_1/preprocessing/protocol_pp001_032_layout.txt and protocol_pp033_064_layout.txt. Fresh Poppler pdftoppm 26.01.0 rendered pp15,19 at 110 dpi; p18 at120 dpi because diagram labels are absent from native layout text despite a nonempty record. Images were visually opened. Tesseract5.5.0 CPU, English --psm6 generated pp15,19 locator OCR. Exact commands:

```bash
pdftoppm -f 15 -l 15 -r 110 -singlefile -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-015
pdftoppm -f 19 -l 19 -r 110 -singlefile -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-019
pdftoppm -f 18 -l 18 -r 120 -singlefile -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-018
tesseract .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-015.png .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/ocr-015 -l eng --psm 6
tesseract .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-019.png .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/ocr-019 -l eng --psm 6
```

Exact page references below are PDF page numbers; original printed page is generally PDF page minus1. Local authoritative evidence links are ../../../.. /joi190092supp2_prod.pdf when resolved from this part directory (four parent traversals, written without the separating space in links below). Native text appendix preserves all source-matched extracted content for every reusable unit, including tables, numerical procedural definitions, background numbers, administrative entries and bibliographic matter.

## Per-page coverage

| PDF page | Content opened and mapped | Quantitative/design applicability |
|---|---|---|
|1|Bundle title|Original/final protocol and change summary identifier; no result values.|
|2|Original MOP DSMC cover|September11,2012; administrative identity.|
|3|Contents first page|Primary endpoint, trial design, treatment and visits locators; no additional analysis specification.|
|4|Contents second page|Ophthalmic grading, OCT, safety and data-analysis locators.|
|5|Contents third page|Staff, committees and appendices; no outcome values.|
|6|Investigators/personnel/sites|Four named clinical-site locations; administrative, no analysis population count.|
|7|DSMC roster|Administrative; no statistical decision boundary.|
|8|Background|Historical incidence >50/100000 person-years, prevalence≈115/100000, up to10% blindness,≈30000 new blindness/year; historical treatment switching about half successful. Not trial results.|
|9|Introduction and aims|216 randomized patients, monthly6months, successful patients continue6more; unsuccessful switch and followed6more. Primary6month corticosteroid-sparing success; Aim2 switching efficacy.|
|10|Design summary/outcomes|Observer-masked randomized comparison, site-block randomization,216=108/arm; full primary/secondary inventory below.|
|11|Timeline and anatomical definitions|Site enrollment goals100,71,15,30; SUN anatomical classes. Administrative planned dates preserved in appendix.|
|12|Inclusion|Active within90days;≥2+ AC cells/haze or active lesions; eligibility options and baseline≥1+; steroid start1mg/kg or60mg whichever less.|
|13|Exclusion/randomization|Age<16 excluded; hypotony<5mmHg>3months both eyes; lab/infection thresholds; blocks4,6,8 equal probability bysite.|
|14|Masking/randomization distribution|Patients/coordinators unmasked; outcome examiners masked; allocation-holder separation.|
|15|Masking and success/failure, Table2|Fresh visual/OCR: BOTH eyes, AC≤0.5+, haze≤0.5+, no lesions, prednisone≤7.5mg/day, topical≤2/day at6months, no safety/tolerability discontinuation.|
|16|Failure and Table3 laboratory thresholds|Failure efficacy/tolerability/safety definitions and exact nonserious/serious cutoffs below.|
|17|Dropout/death definition|Missed visit or temporary stoppage is not dropout; drug-related death=failure, unrelated death=dropout, monitor discretion.|
|18|Primary endpoint flowchart|Fresh image supplements reusable text: seriousAE=failure, futility/intolerability→switch, six/twelve-month success and rescue logic below.|
|19|Treatment Tables4/5|Fresh visual/OCR: introductory/maintenance/dose reduction weekly/daily schedules below.|
|20|MTX/MMF narrative dosing|MTX15→25mg/week after2weeks, reductions20/15; MMF500mgBID→1.5gBID, reductions1g/500mgBID; inability to escalate declares intolerability failure.|
|21|Folicacid, packaging, adherence|Folicacid1mg/day forMTX;14day introductory and30day maintenance packages;120days at6month extension; diary/pillcounts.|
|22|Prednisone|Start min(1mg/kg,60mg/day),2–4weeks, taper/hold7.5through6months; full drug effect6–8weeks; first3months flare not necessarily failure.|
|23|Tables6/7 taper/rescue|All doses/durations/decrements below; flare mild1+, severe≥2+; severe rescue up to1mg/kg, mild up to doubled flare dose.|
|24|Topical taper Table8, supplements/adjuncts|Topical8,6,4,3,2,1,0/day; endpoint≤2/day; calcium500mgTID, vitaminD400–800IU/day; prohibited adjuncts tracked as deviations.|
|25|Visit operational sequence|Consent→ID→assignment; questionnairesSF36,NEIVFQ25US/INDVFQIndia; masked ocular assessments.|
|26|PhaseI visit windows, Table9|Baseline,week2,months1–6;months1–5 ±15days;month6−15/+30days; minimum2weeks between visits.|
|27|Table10 extension, rescue and nonstudy visits|Months6,9±15days and12−15/+30;rescue baselineII and6months/untilfailure; baselineII within7days after nonstudy failure.|
|28|Forms schedule matrix|BaselineI/II,months1–5,9,6/12/failure; OCT/VA/clinicalexam each followup; photography/QOL atbaseline/failure/endpoints.|
|29|Baseline collection/randomization|Labswithin14days before/on randomization, clinical data atbaseline; sequential ID assignment.|
|30|Baseline/followup procedures|CBC/chemistry/pregnancy and QOL collection, endpoint/failure QOL timing.|
|31|PhaseII eligibility and visits|Efficacy/tolerabilityfailure→rescue;SAE excludes rescue; nonstudy events/failure tracked.|
|32|QOL and extended-followup collection|SF36all,NEIVFQ25US,INDVFQIndia; baseline/6month-or-failure;12months ifsuccess; extendedphaseI recordedmonths9/12 orfailure.|
|33|Refraction|30min contactlens removal wait;4m standard,<20/200→1m; criterionmissing≥2 letters largestline; refraction numerical ranges appendix.|
|34|Lens table/refraction|Three VA bands20/10–20/80,20/100–20/200,<20/200; numerical trial-lens settings preserved.|
|35|Axis/cylinder/refinement|Axis steps10°,5°,3°,2°,1° bycylinder bins;0.5D cylinder↔opposite0.25D sphere compensation.|
|36|Refraction20/100–20/200|±1.00D sphere/cylinder procedure;plus cylinderaxis90°,180°,45°,135°.|
|37|Refraction axis/power|Same axisstep table andspherical-equivalent compensation.|
|38|Refinement/low acuity|±0.50D refinement;at1m+0.75D accommodation;poorVA±2.00D sphere.|
|39|Low acuity cylinder|±1D cylinder,full axisstep table repeated.|
|40|LowVA refinement/VA charts|±1D sphere, cylinder-sphere compensation;14line modifiedBaileyLovie charts.|
|41|VA apparatus/scale|Geometricletter/arithmeticlogMAR progression; thirdrow0.8logMAR=45letters=20/125Snellen;4m/1m lanes. No trial result.|
|42|VA testing|Each eyeeachvisitafterrefraction;stop at≤3 correctletters inrow≥3; <10letters4m→1m.|
|43|Lowvision/scoring|First6rows1m; <10letters1m→lowvision;countfingers3/5at1m,handmotion4/5at0.5m; scoring statement preservedbelow.|
|44|VA score andcertification|4m score letters+30;1m conditional score;lowvision→logMAR table;maxscore100;Snellen≥4/5letters;certification18±2months.|
|45|Inflammation scales|SUNAC cells0,<1;0.5+,1–5;1+,6–15;2+,16–25;3+,26–50;4+,>50. Flare/vitreouscells notprimarycontrolcriterion.|
|46|NEI vitreoushaze|Grades0,0.5+,1+,2+,3+,4+, descriptions;NEIallprimary/secondary, Davisexploratory correlation.|
|47|Davis9point image/interobserver/OCT|Two studyphysicians at6/12monthsorfailure;primarystudyophthalmologistusedforprimaryanalysis;fixedscannerbysite.|
|48|Heidelberg OCT|20°×20°,49sections,16ARTframes;baseline reference scan and7linepreset.|
|49|Heidelberg retinalthickness|7line30°×5°,7sections,25ARTframes;quality≥20;centralsubfieldthickness recorded.|
|50|Zeiss OCT|Macularcube and5lineraster; displayed scan preset512×218;identification/exportprocedure.|
|51|Zeiss thickness/fundusphotography|Signalstrength≥5;centralsubfieldthickness;fundusphotosbaseline6/12monthsorfailure;maskedNEI/Davisgrading.|
|52|Labs/nonseriousAE|Baselinewithin14days;followupwindow;temporarynonseriouslaboratoryhold≤1month;IOP>24mmHg;AST/ALT>2but<5×ULN example.|
|53|SAE/death/reporting|AST/ALT≥5×ULN listed;death/non-electivehospitalization,etc;24hourSAE/deathnotice.|
|54|Data forms/review/doubleentry|Administrative quality assurance; no inferential model.|
|55|Data coding/cleaning|Missing data explicitNA;continuous unitsincludinglogMARdefinedincodebook;singleheader,rowobservation/columnvariable.|
|56|Dataanalysis/security|Unmaskedrandomization merge and R statisticalanalysis; no test/model/CI formula specified.|
|57|Compliance/quality/staff|Dosemisses+pillcounts; weeklyscreening/enrollment/followupreports; administrative, no inferentialrule.|
|58|Staffresponsibilities|Statisticianconductanalysis/prepareallocationlist; no model choice.|
|59|Clinicalmeasurementduties/committees|Both eyesatallVA/OCTvisits;fundusbaseline6/12monthsorfailure; administrative.|
|60|DAC/interim/DSMC|Prespecifiedinterimwhen1/3patientcomplete;DSMCevaluatestoppingguidelines; no boundary value.|
|61|Stopping/organization|Conservativeearlystoppingauthorized; no numerical rule.|
|62|Bibliography|Historicalreferences;no trial quantitativeanalysis specification.|
|63|Bibliographycontinuation|Historicalreferences;no new trial relationship.|
|64|Final MOP title|January06,2017 version4.5; substantive finalprotocol beginsoutsideassignedscope.|

## Result-relevant relationships and matching keys

### A: Design, populations, primary endpoint and secondary hierarchy

[DOC-003 p9](../../../../joi190092supp2_prod.pdf#page=9), [p10](../../../../joi190092supp2_prod.pdf#page=10): patient is randomization unit; two arms oralMTX/oralMMF;216patients,108/arm; site-block observer-masked comparison. Primary Aim1 rate overall corticosteroid-sparing treatment success6months. Aim2 success6months afterswitch among first6month failures. Definition p15 requires BOTHeyes controlled; systemicprednisone≤7.5mg/day andtopicalprednisoloneacetate1%≤2drops/day at6monthvisit with no tolerability/safetyissueswarrantingdiscontinuation. ControlledinflammationTable2:ACcells≤0.5+SUN, vitreoushaze≤0.5+NEI, noactivechoroidal/retinallesions independentofmacularedema.

Secondary inventory p10 (all listed, no imposed key designation): timetocontrol, timetosuccess, success5months sustained≥28daysto6months, success12monthsPhaseI, success6–12monthswithcompletecorticosteroiddiscontinuation, success6monthsPhaseII andPhaseIIwithoutcorticosteroids, BSCVAchange, macularedemapresence, macularthicknesschange, clinicalDavisvitreoushazechange, photographicNEI/Davischange, anatomic intermediate/posterior/panuveitisefficacy, intolerabilitydiscontinuationproportion, adverseeventrate, SAEdiscontinuationproportion, health/visionQOL, occurrenceofdose reduction, VKHefficacy.

Matching main-paper keys: randomized/analyzed participantcounts; sixmonth treatment-success numerator/denominator andriskcomparison; prednisone/topicalthresholds; anatomic-location subgroupinteraction; sixmonth visualacuity/logMAR and centralmacularthickness;12monthmaintenance andrescueswitching; tolerateddose andsafetyevents. This map establishes keys only and does not compare reported results.

Eligibility pp12–13: historicalnoninfectious intermediate,anterior+intermediate,posterior,panuveitis≥1eye;activewithin90days≥2+ACcells/haze oractivelesions; baseline≥1+AC/haze oractivelesions. Additionalrequirement one ofactiveafter4weekshighdose1mg/kg, steroidtaperflarewithin14days, orchronicconditionnecessitatingsparing. Age≥16;previousnonprednisoneimmunosuppressionexcluded. ExclusionlabsCBCWBC≤2500,platelets≤75000,Hb≤10;AST/ALT≥2×ULN,creatinine≥1.5; within14days. Infectiontestswithin60days. Blocks4,6,8equiprobable/site. Population is not limited to one studyeye: success requiresboth, secondaryocularmeasurementsareboth-eyemeasurements.

### B: Failure, rescue, discontinuation, dropout and endpoint flow

[p16](../../../../joi190092supp2_prod.pdf#page=16), [p17](../../../../joi190092supp2_prod.pdf#page=17), [p18](../../../../joi190092supp2_prod.pdf#page=18): Failure may be declaredanytimeforefficacy,futility,intolerabilityorsafety; inefficacy includesfailuretotaper≤7.5mgprednisone/≤2topicalby6months. Tolerability permits two reducedoses; inability toescalatefromintroductorydoseafter2weeks isfailure (p20). SafetySAEexitimmediatelywithoutAim2; abnormalnonseriouslabsstopmedicationandallowonemonthtoregaineligibility,otherwiseexitfailure. Temporary interruption still permits efficacyfailureifcontrolorsteroidthresholdnotmetat6months. Missedvisitnotdropout; temporarydiscontinuationnotdropout; explicitwithdrawal/deathisdropoutexceptdrug-relateddeathcountedasfailure. Medicalmonitorassignsdeathrelation.

p18 diagram visually mapped: randomization→monthlyefficacy/tolerability/safety/taperassessment; anySAE→failure; clinicianfutility→alternativePhaseII; intolerablesideeffects→reductionI→ifpersistreductionII→ifpersistswitchPhaseII, ifresolvecontinue. Sixmonthcontrolled+≤7.5mg+≤2drops→successandcontinueoriginalPhaseImonths6–12, reassesssamecriteriaat12months. Sixmonthnotmeetingcriteria→alternativePhaseII→6monthlatercriteria→successorfailure. Footnotes spell AC≤0.5+,haze≤0.5+,noactivechoroid/retinal lesions; topical1%prednisoloneacetateorequivalent.

### C: Randomized treatment, dose reductions and steroid regimens

[p19](../../../../joi190092supp2_prod.pdf#page=19), [p20](../../../../joi190092supp2_prod.pdf#page=20): Table4weeks1–2MTX15mgonceweekly(day1),MMF500mgBIDeachday1–7,MTXfolicacid1mgeachday. MaintenanceMTX25mgonceweekly(day1);MMF1.5gBIDeachday;folicacid1mg/day. Table5reductionIMTX20mgweekly/MMF1gBID;reductionIIMTX15mgweekly/MMF500mgBID;folicacidcontinues1mg/day. Footnoteonlyreduceforintolerablesideeffects/safetyconcerns,otherwisehighestmaintenancethroughfollowup. NarrativeweeklyMTXdividedmorning/eveningonsameday;MMFBIDempty stomach. Studyphasesrepeatdoseintroductionforrescue.

[p22](../../../../joi190092supp2_prod.pdf#page=22), [p23](../../../../joi190092supp2_prod.pdf#page=23): Initialprednisone min(1mg/kg,60mg/day)2–4weeks; successdependentontaper≤7.5mg/day; hold7.5until6months. Table6dosemg/day:dwellweeks:decrementmg/day =60:2–4:10;50:1:10;40:1:5;35:1:5;30:1:5;25:1:5;20:1:2.5;17.5:1:2.5;15:1:2.5;12.5:1:2.5;10:1:2.5;7.5:hold. Table7extensionoptional:7.5:≥1week:2.5;[5,7.5):2–4weeks:1–2.5;[2.5,5):2–4weeks:1.5–2.5;[1,2.5):2–4weeks:1;0. Mildflare≤1+,severe≥2+AC/haze;severerescueup to1mg/kg,milddoubleflaredose;nonresponseafter4weeks→holdadditionalweekthenpossiblefailure. Table8p24topicaldailyfrequency8(1–2weeks),6(1week),4(1),3(1),2(1),1(1),none. Corticosteroidinjections,IVtherapy,additionalimmunosuppressionandsurgerynotallowedwithoutdeviationform.

### D: Visit windows, timing and measurements

[p26](../../../../joi190092supp2_prod.pdf#page=26), [p27](../../../../joi190092supp2_prod.pdf#page=27): baselineI/IIday1firsttreatment;firstsixmonthsmonthlyplusweek2;minimum2weeksbetweenvisits;months1–5±15days,month6−15/+30days. Extensionmonths6and9±15days,month12−15/+30days;studydatacollectedmonths9/12andfailure. RescuefollowupsixmonthsafterbaselineII/untilfailure; baselineIIcancoincidewithfailure. Table9p28explicitformmatrix preservedinnativeappendix. Labsbaselinewithin14daysbefore/onrandomization,followuplabswithinvisitwindow. QOLbaseline,6monthsorfailurefirst,12monthsifinitialsuccess;SF36all,NEIVFQ25US,INDVFQIndia;selfcompletionpreferredandverbatiminterviewifneeded.

### E: Visual acuity and ocular grading statistical definitions

[p43](../../../../joi190092supp2_prod.pdf#page=43), [p44](../../../../joi190092supp2_prod.pdf#page=44): exact source scoring statement p43 says “If 10 or more letters of the first line are read correctly at 4 meters” then continuesp44withscore=4metercorrectletters+30; source p44 additionally “If 3 or fewer letters of the largest line are read correctly at 4 meters” score=1metercorrectletters;≤3at1meter→lowvisionandlogMARconversionaccordingtoVisualAcuityCalculationTable. Preserved as printed, without harmonizing conditions. Max4meter score100. Snellenratio correspondingtolastline≥4/5correct. Testing p42 threshold<10letters4m→1m; p43<10letters1m→lowvision. First6rowstested1m. Lowvisioncountfingers≥3/5presentations1m;handmotion≥4/5at0.5m;lightperceptionfourpresentations0.5m. Visualacuitysecondaryoutcomeeach eyeeachvisitpostrefraction;lowvisionscoreconversiontableisreferencedbutnotpresentinthisassignedscope.

[p45](../../../../joi190092supp2_prod.pdf#page=45): ACcellgrade0:<1cell;0.5+:1–5;1+:6–15;2+:16–25;3+:26–50;4+:>50in1mm×1mmbeam. ACflare0none/1+faint/2+moderatecleardetails/3+markedhazydetails/4+intensefibrin,notprimarycontrolcriterion. Vitreouscells0none/0.5+0–5/1+6–10/2+11–20/3+21–50/4+>50in1mm×0.5mmbeam,notprimarycontrolcriterion. p46NEIvitreoushaze0clear,0.5+slightopticdiscmarginblurandlossnormalnervefiberstriations/reflex,1+opacitieswithoutretinaldetailobscuration,2+mildopticnerve/vesselblur,3+significantbutvisibleblur,4+denseopacityobscuringopticnervehead. NEIusedallprimary/secondarymeasures;Davis9pointadditionallyassessedandexploratorycorrelationplanned. p47two studyphysicians assessACcells/flare,vitreouscells/hazeat6/12monthsorfailurefirst; primaryophthalmologistmeasurementsusedforprimaryanalysis.

OCTpp47–51: eachsiteselectsoneSpectralisorCirrusandretainsthroughtrial. Both eyescentralmacularsubfieldthickness; Heidelberg20°×20°volume49sections16ARTframesand7line30°×5°7sections25ARTframes,quality≥20; Cirrusmacularcubepresetprinted512×218and5lineraster,signal≥5. Thicknessmapusedimmediatelyformacularedemadetermination; no explicitmacularedemathicknesscutoffinthesepages. PhotographicNEI/Davisgrader masked; baseline/6/12monthsorfailure.

### F: Laboratory safety thresholds

[p16](../../../../joi190092supp2_prod.pdf#page=16) Table3:

|Measure|Non-serious|Serious|
|---|---|---|
|Leukocytes|>1000and<2500/µL<1month|<2500>1monthor≤999/µL|
|Platelets|20000–75000/µL<1month|≤20000/µLor<75000/µL>1month|
|Hemoglobin|>6.4to<10g/dL|≤6.4g/dL|
|AST/ALT|2–5×referenceULN|>5×referenceULN|
|Creatinine|≥1.5to<2mg/dL|≥2mg/dL|

p52AEexamplesIOP>24mmHg,AST/ALT>2but<5×ULN; p53SAEdefinitionlistAST/ALT≥5×ULN,death,non-electivesurgery/hospitalization,MI/stroke,life-threateningreaction,significantpersistentdisability. Drugtemporaryhold/resumptionandfailurelinkmappedabove. No harmonization acrossthresholdoccurrencesisassumed.

### G: Sample size, primary analysis, missingness and interim decision-rule coverage

[p10](../../../../joi190092supp2_prod.pdf#page=10):216total108/arm. This original-MOPsharddoesnotstatepower,expectedsuccessrates,alpha,sample-sizeformula,noninferioritymargin,model,covariates,missingoutcomeimputation,orCI/testcalculation. Theseareabsentfromthisscope,notfromthepackageasawhole; otherprotocol/SAPshardsmustsupplytheircontent. p55definesdata-managementmissingvaluecodingNA,notinferentialmissing-datahandling. p56DACmergesunmaskeddatawithallocationandusesR;notaspecificprimarymodel. p60DACprespecifiedinterimwhen1/3patientscomplete,provideDSMCdatatoevaluatestoppingguidelines. p61DSMCauthorizedconservativeearlystopping;nonumericboundaryhere. Administrativeperiodicmonitoringreporttimingisnotaninterimefficacydecisionrule.

## Native layout appendix: complete reusable-backed page content

The following source-linked transcription aid preserves every available page segment. Fresh-required p15/p19 were visually transcribed above; the p18 native diagram gap is closed by the visual map above. Bibliographic and administrative numbers are preserved for completeness, with no external lookup. No workbook, CSV, DOC/DOCX, formula/cached value, or realized support result occurs in this shard.


### DOC-003 PDF page 1

```text
                          Supplementary Online Content 1

FAST Uveitis Trial original protocol, final protocol, and summary of changes

```

### DOC-003 PDF page 2

```text
                 NEI U10 EY021125-01



First-line Antimetabolites as Steroid-sparing
        Treatment (FAST) Uveitis Trial



  Data Safety and Monitoring Committee (DSMC) Meeting
                     September 11, 2012




                Manual of Operations (MOP)




                 Elizabeth Proctor Library, Room S-318
        F.I. Proctor Foundation for Research in Ophthalmology
                        513 Parnassus Avenue
                 University of California, San Francisco

```

### DOC-003 PDF page 3

```text
  First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                                     September 4, 2012
  Manual of Operation and Procedures


                                                     TABLE OF CONTENTS

INVESTIGATORS, PERSONNEL AND STUDY SITES .................................................. 5
DATA SAFETY AND MONITORING COMMITTEE (DSMC) MEMBERS........................ 6
BACKGROUND ..............................................................................................................7
1. INTRODUCTION TO TRIAL .......................................................................................8
  1.1 RESEARCH QUESTION ..............................................................................................8
  1.2. Specific Aims .........................................................................................................8
2. TRIAL DESIGN ...........................................................................................................9
  2.1 DESIGN SUMMARY ...................................................................................................9
  2.2 STUDY TIMELINE .................................................................................................... 10
  2.3 ELIGIBILITY ............................................................................................................ 10
    2.3.1 Anatomical Location of Inflammation.............................................................. 10
    2.3.2 Inclusion Criteria ............................................................................................ 11
    2.3.3 Exclusion Criteria ........................................................................................... 12
  2.4 RANDOMIZATION AND MASKING............................................................................... 12
  2.5 DEFINITIONS FOR PRIMARY ENDPOINT ..................................................................... 14
    2.5.1 Treatment Success ........................................................................................ 14
    2.5.2 Treatment Failure........................................................................................... 14
    2.5.3 Primary Endpoint Flowchart ........................................................................... 17
3. TREATMENT PLAN ................................................................................................. 18
  3.1 STUDY DRUGS ....................................................................................................... 18
    3.1.1 Methotrexate .................................................................................................. 19
    3.1.2 Mycophenolate mofetil ................................................................................... 19
    3.1.3 Folic acid........................................................................................................ 20
    3.1.4 Packaging and distribution of study medications ............................................ 20
    3.1.5 Adherence to the treatment plan .................................................................... 20
  3.2 CORTICOSTEROID THERAPY ................................................................................... 21
    3.2.1 Oral prednisone ............................................................................................. 21
    3.2.2 Supplements .................................................................................................. 23
    3.2.3 Topical corticosteroid ..................................................................................... 23
    3.2.4 Other adjunctive treatments ........................................................................... 23
  3.3 STUDY PROCEDURES ............................................................................................. 24
4. STUDY VISITS .......................................................................................................... 25
  4.1 VISIT SCHEDULES .................................................................................................. 25
    4.1.1 Phase I: First-line Treatment .......................................................................... 25
    4.1.2 Phase II: Rescue Treatment........................................................................... 26
    4.1.3 Non-study visits.............................................................................................. 26
  4.2 STUDY FORMS COMPLETION SCHEDULE ................................................................. 27
  4.3 ENROLLMENT AND BASELINE-I VISIT ........................................................................ 28
    4.3.1 Consent and eligibility evaluation .................................................................. 28
    4.3.2 Randomization ............................................................................................... 28
    4.3.3 Procedures for data collection ........................................................................ 28
    4.3.4 Specimens .................................................................................................... 29
    4.3.5 Forms for data collection ................................................................................ 29
  4.4 FOLLOW -UP VISITS ................................................................................................. 29
    4.4.1 Procedures for data collection ....................................................................... 29
    4.4.2 Specimens ..................................................................................................... 29
                                                                                                                                       2

```

### DOC-003 PDF page 4

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                                      September 4, 2012
 Manual of Operation and Procedures


    4.4.3 Forms for data collection ................................................................................ 30
  4.5 BASELINE-II ........................................................................................................... 30
    4.5.1 Eligibility ......................................................................................................... 30
  4.6 NON-STUDY VISITS ................................................................................................. 30
    4.6.1 Procedures for data collection ....................................................................... 30
    4.6.2 Specimens ..................................................................................................... 31
    4.6.3 Forms for data collection ................................................................................ 31
5. STUDY EXAMINATIONS AND PROCEDURES ....................................................... 31
  5.1 QUALITY OF LIFE QUESTIONNAIRE ADMINISTRATION ................................................. 31
  5.2 REFRACTION AND VISUAL ACUITY ........................................................................... 32
    5.2.1 Refraction Procedure .................................................................................... 32
    5.2.2 Visual acuity procedure .................................................................................. 39
    5.2.3 Visual acuity training and certification ............................................................ 43
  5.3 OPHTHALMIC PROCEDURES .................................................................................... 43
    5.3.1 Grading inflammation .................................................................................... 43
    5.3.2 Inter-observer variation of ocular inflammation ............................................... 46
  5.4 OPTICAL COHERENCE TOMOGRAPHY ...................................................................... 46
    5.4.1 Required patient assessments – Heidelberg Spectralis.................................. 46
    5.4.2 Scan procedures – Heidelberg Spectralis ...................................................... 47
    5.4.3 Obtaining retinal thickness data – Heidelberg Spectralis ................................ 48
    5.4.4 Saving/Exporting data – Heidelberg Spectralis .............................................. 48
    5.4.5 Required patient assessments – Zeiss Cirrus ................................................ 49
    5.4.6 Scan procedures – Zeiss Cirrus ..................................................................... 49
    5.4.7 Obtaining retinal thickness data –Zeiss Cirrus ............................................... 50
    5.4.8 Saving/Exporting data – Zeiss Cirrus ............................................................ 50
    5.4.9 OCT operator qualifications............................................................................ 50
  5.5 FUNDUS PHOTOGRAPHY ......................................................................................... 50
  5.6 LABORATORY MEASUREMENTS ............................................................................... 51
6. ADVERSE EVENTS .................................................................................................. 51
  6.1 NON-SERIOUS ADVERSE EVENT (AE) ...................................................................... 51
  6.2 SERIOUS ADVERSE EVENT (SAE) ........................................................................... 52
  6.3 ADVERSE EVENT REPORTING ................................................................................. 52
  6.4 PATIENT DEATH ..................................................................................................... 52
7. DATA COLLECTION AND MANAGEMENT ............................................................. 52
  7.1 DATA COLLECTION FORMS ..................................................................................... 53
  7.2 DATA REVIEW ....................................................................................................... 53
  7.3 DATA ENTRY .......................................................................................................... 53
    7.3.1 Data Entry Errors ........................................................................................... 53
    7.3.2 Data Consistency and Validity........................................................................ 54
    7.3.3 Data Preparation and Cleaning ...................................................................... 54
    7.3.4 Monitoring ...................................................................................................... 54
  7.4 DATA ANALYSIS ..................................................................................................... 55
  7.5 DATA STORAGE AND SECURITY............................................................................... 55
8. QUALITY CONTROL ................................................................................................ 55
  8.1 MEDICATION STORAGE AND EXPIRY ........................................................................ 56
  8.2 PERIODIC REPORTS .............................................................................................. 56
  8.3 DATA MANAGEMENT, SECURITY, AND QUALITY ASSURANCE ..................................... 56
  8.4 MONITORING COMPLIANCE ..................................................................................... 56

                                                                                                                                       3

```

### DOC-003 PDF page 5

```text
  First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                                 September 4, 2012
  Manual of Operation and Procedures


  8.5 CERTIFICATION ...................................................................................................... 56
  8.6 DATA AUDITS ........................................................................................................ 56
9. DUTIES AND RESPONSIBILITIES OF STAFF ........................................................ 56
  9.1 OPHTHALMOLOGIST ............................................................................................... 56
  9.2 CLINICAL TRIAL MANAGER ...................................................................................... 57
  9.3 STUDY COORDINATOR ............................................................................................ 57
  9.4 DATA ANALYST ...................................................................................................... 57
  9.5 DATA ENTRY OPERATOR ........................................................................................ 57
  9.6 BIOSTATISTICIAN .................................................................................................... 57
  9.7 OPHTHALMIC ASSISTANTS ...................................................................................... 58
  9.8 REFRACTIONISTS ................................................................................................... 58
  9.9 OCT OPERATORS .................................................................................................. 58
  9.10 FUNDUS PHOTOGRAPHERS ................................................................................... 58
  9.11 FUNDUS GRADERS ............................................................................................... 58
10. STUDY ORGANIZATION........................................................................................ 58
  10.1 EXECUTIVE COMMITTEE ....................................................................................... 58
  10.2 CLINICAL COORDINATING CENTER (CCC) .............................................................. 58
  10.3 DATA COORDINATING CENTER (DCC) ................................................................... 59
  10.4 DATA ANALYSIS CENTER (DAC) ............................................................................ 59
  10.5 DATA SAFETY AND MONITORING COMMITTEE (DSMC) ........................................... 59
  10.6 EDITORIAL COMMITTEE......................................................................................... 60
  10.7 STUDY SITES ....................................................................................................... 60
  10.8 PHARMACY .......................................................................................................... 60
  10.9 STUDY COMMUNICATIONS .................................................................................... 60
11. BIBLIOGRAPHY ..................................................................................................... 61
APPENDIX A: STUDY FORMS .................................................................................... 63
APPENDIX B: CERTIFICATION FORMS ................................................................... 118
APPENDIX C: UPRC MANUAL .................................................................................. 121




                                                                                                                                   4

```

### DOC-003 PDF page 6

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial             September 4, 2012
 Manual of Operation and Procedures



              First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial


                                Investigators, Personnel and Study Sites

Nisha Acharya, MD, MS1                                    Principal Investigator
                                                          Site Director San Francisco
                                                          Study Ophthalmologist San Francisco

SR Rathinam, MD, PhD2                                     Site Director Aravind Eye Hospitals
                                                          Study Ophthalmologist Madurai

N Radhika, MD2                                            Study Ophthalmologist Madurai

VK Anuradha, MD3                                          Study Ophthalmologist Coimbatore

Eric Suhler, MD, MPH4                                     Site Director Casey Eye Institute
                                                          Study Ophthalmologist Oregon

Todd Margolis, MD, PhD1                                   Medical Monitor

Thomas Lietman, MD1                                       Data Coordinating Center

Dr. Travis Porco, MPH, PhD1                               Data Coordinating Center, Principal statistician

Dr. Wayne Enanoria, PhD1                                  Data Coordinating Center, Research epidemiologist

Salena Lee, OD1                                           Refraction Certification Manager

Natalie Nardone, PhD1                                     Study Coordinator San Francisco

Gobinath Kanagaraj2                                       Study Coordinator Madurai

Mr. Meenakshi Sundaram3                                   Study Coordinator Coimbatore

Ms. Tracy Giles4                                          Study Coordinator Oregon



Francis I. Proctor Foundation, University of California San Francisco1; Aravind Eye Hospital,
Madurai, India2; Aravind Eye Hospital, Coimbatore, India3; Casey Eye Institute, Oregon Health and
Science University4




                                                                                                              5

```

### DOC-003 PDF page 7

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                  September 4, 2012
 Manual of Operation and Procedures



              First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial


                      Data Safety and Monitoring Committee (DSMC) Members


Maureen Maguire, PhD                                           Chair of DSMC, biostatistics
                                                               Carolyn F. Jones Professor of Ophthalmology
                                                               University of Pennsylvania

William Barlow, PhD                                            Biostatistics
                                                               Research Professor, Biostatistics
                                                               University of Washington

Jackie Glover, PhD                                             Ethics
                                                               Professor of Pediatrics
                                                               University of Colorado

Debra Goldstein, MD                                            Uveitis
                                                               Professor of Ophthalmology
                                                               Northwestern University

Steven Yeh, MD                                                 Uveitis
                                                               Assistant Professor of Ophthalmology
                                                               Emory University

Narsing Rao, MD                                                Uveitis
                                                               Professor of Ophthalmology and Pathology
                                                               Doheny Eye Institute

Donald Everett, MA                                             Program officer
                                                               National Eye Institute
                                                               National Institutes of Health




                                                                                                                   6

```

### DOC-003 PDF page 8

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
 Manual of Operation and Procedures


Background

     In the First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial, we
     propose to establish which immunosuppressive therapy, methotrexate or mycophenolate
     mofetil, is more effective as a first-line, corticosteroid-sparing agent for the treatment of non-
     infectious uveitis. Uveitis, a set of conditions defined by intraocular inflammation, is a
     significant cause of vision loss and morbidity in the United States and the world.1, 2 The
     incidence was recently estimated to be more than 50 cases per 100,000 person-years, with
     a prevalence of approximately 115 per 100,000 persons.3 Additionally, uveitis is believed to
     be the cause of up to 10% of cases of legal blindness in the United States, or approximately
     30,000 new cases of blindness per year.1, 3, 4 In contrast to common age-related eye
     disorders, uveitis may have a stronger socio-economic impact because it disproportionately
     affects younger working-age patients.5 Although the etiology of uveitis is varied, most cases
     are presumed to be immune-mediated and lack a known infectious cause.6-9 Even in
     developing countries such as India that have a larger burden of infection, the vast majority of
     cases are non-infectious.10, 11

     The current mainstay of treatment for non-infectious uveitis is corticosteroids (topical,
     systemic, locally injected, or corticosteroid-eluting implants). Due to the well documented
     local and systemic side effects associated with corticosteroid therapy, other
     immunosuppressive therapies are frequently used as corticosteroid-sparing agents in
     patients who need long-term therapy. These include antimetabolites, calcineurin inhibitors,
     alkylating agents, and biologic drugs.12 Cost and morbidity associated with uncontrolled
     inflammation make the selection of an effective initial steroid-sparing agent extremely
     important.

     When corticosteroid-sparing therapy is required, the two most commonly used first-line
     immunosuppressive agents are methotrexate and mycophenolate mofetil.13 Because of cost
     and potentially dangerous long-term side effects, other classes of drugs such as biologics
     are typically reserved for refractory cases in which other treatments have failed.12 It is
     common practice for patients requiring a steroid-sparing agent to be treated first with the
     less expensive methotrexate and then switched to mycophenolate mofetil in the event of
     treatment failure. However, results from non-comparative retrospective case series indicate
     that uveitis patients may be much more likely to achieve controlled inflammation and tolerate
     treatment with mycophenolate mofetil. 13-28 Furthermore, approximately half of the patients
     who fail treatment with methotrexate go on to successful treatment with mycophenolate
     mofetil.29 Unlike in rheumatology, where clinical trials have demonstrated differential efficacy
     of antimetabolites for systemic inflammatory diseases, there have been no prospective
     randomized, controlled trials in uveitis to systematically determine which antimetabolite is
     more clinically efficacious as initial corticosteroid-sparing therapy. This makes it difficult for
     clinicians to make informed, evidence-based decisions about first-line immunosuppressive
     treatment. In addition, if patients fail one antimetabolite, there is no evidence basis for
     deciding whether to switch to another antimetabolite, or to move on to another class of
     immunosuppressives, including biologics.




                                                                                                       7

```

### DOC-003 PDF page 9

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


1. Introduction to trial

    The proposed study is a randomized comparative effectiveness trial to determine which
    treatment, methotrexate or mycophenolate mofetil, is more effective as first-line
    corticosteroid-sparing treatment for patients with non-infectious intermediate, posterior and
    panuveitis requiring corticosteroid-sparing therapy.

    Two hundred sixteen patients with non-infectious uveitis in need of corticosteroid-sparing
    therapy will be randomized to receive either oral methotrexate or oral mycophenolate
    mofetil at Aravind Eye Hospitals (Madurai and Coimbatore, South India), Casey Eye
    Institute (Oregon Health and Science University, Portland) and the F.I Proctor Foundation
    (University of California, San Francisco). They will be followed monthly for 6 months after
    enrollment or until treatment failure. Patients who achieve success at 6 months will continue
    for another 6 months on the same medication. Patients who fail at 6 months will switch
    treatments and be followed for an additional 6 months or until failure of the second
    treatment.

    1.1 Research question

    Which treatment–methotrexate or mycophenolate mofetil–is more effective as a first-line
    immunosuppressive treatment for patients with non-infectious intermediate, posterior and
    panuveitis requiring corticosteroid-sparing therapy?

    1.2. Specific aims

    Aim 1: Establish which immunosuppressive treatment, methotrexate or
    mycophenolate mofetil, results in a higher rate of corticosteroid-sparing treatment
    success. As a primary outcome, rates of successful corticosteroid-sparing control of
    inflammation will be compared at 6 months after enrollment. We will also evaluate
    differences in secondary outcomes, such as visual acuity, macular thickness, time to control
    of inflammation, efficacy within various anatomic locations of uveitis, tolerability, quality of
    life, and adverse events.

    Aim 2: Evaluate the clinical efficacy of switching agents after initial treatment failure.
    Patients who are recorded as a treatment failure on the initial randomized drug will be
    switched to the other treatment. These patients will be followed an additional 6 months from
    the date of treatment failure, following the same protocol with the same primary and
    secondary outcomes as in Aim 1.




                                                                                                       8

```

### DOC-003 PDF page 10

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   September 4, 2012
 Manual of Operation and Procedures


2. Trial design
     2.1. Design summary
Study type
    • Randomized, observer-masked comparative effectiveness trial
    • Block randomization by site: Aravind Eye Hospitals, Casey Eye Institute, F.I Proctor
        Foundation
    • Sample size: 216 patients, 108 patients per arm (Table 1)

Treatment arms
    • Oral methotrexate
    • Oral mycophenolate mofetil
Treatment timeline
    • Phase I
            • Initial treatment from 0-6 months. If treatment success (i.e. achieving
              corticosteroid-sparing control of inflammation at 6 months), treatment extended to
              12 months.
    • Phase II
            • Second therapy initiated after failure to achieve corticosteroid-sparing control of
                 inflammation in Phase I (0-6 months).
Outcomes
    • Primary outcome (Specific Aim 1):
           • Rate of overall treatment success at 6 months, where treatment success is
              defined as controlled ocular inflammation (Table 2) with ≤ 7.5 mg/day of oral
              prednisone and ≤ 2 drops/day of topical 1% prednisolone acetate
    • Secondary outcomes
            • Specific Aim 2: Rate of corticosteroid-sparing treatment success at 6 months after
              switching treatments in patients who are a treatment failure in the first 6 months
              where treatment success is defined as in Aim 1
            • Time to control of inflammation
            • Time to treatment success
            • Proportion achieving treatment success at 5 months and sustaining, for at least 28
              days, to 6 months
            • Proportion achieving treatment success at 12 months in Phase I
            • Phase I treatment success (6-12 months) with complete discontinuation of
              corticosteroid
            • Proportion achieving treatment success at 6 months in Phase II
            • Phase II treatment success with complete discontinuation of corticosteroids
            • Change in best spectacle-corrected visual acuity (BSCVA)
            • Presence of macular edema
            • Change in macular thickness
            • Change in vitreous haze as assessed clinically by the Davis scale.
            • Change in vitreous haze as assessed by fundus photography grading by NEI and
              Davis scales
            • Efficacy for intermediate, posterior and panuveitis subgroups
            • Proportion discontinuing due to intolerability
            • Rate of adverse events
            • Proportion discontinuing due to serious adverse events
            • Quality of life (Health related and vision related)
            • Tabulate the occurrence of dose reduction used in immunosuppressive treatment
            • Efficacy of treatment in patients with Vogt-Koyanagi-Harada (VKH) disease
                                                                                                    9

```

### DOC-003 PDF page 11

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                   September 4, 2012
Manual of Operation and Procedures


    2.2. Study timeline
                                      Table 1: Timeline for study completion

            Date                                               Planned Activity
December 2011 through            Pre-study activities: refine/finalize MOP, IRB, IND, Indian Council of
September 2012                   Medical Research approval

September 2012 through           1st meeting of DSMC, conduct final certification of sites and study
November 2012                    personnel, earliest project start date
                                                              Enrollment goals by site
November 2012 through
May 2015                             Madurai             Coimbatore            San Francisco          Oregon
(2.5 years)                            100                    71                   15                   30
Through December 2015            Finish 6 month follow-up (Phase I) + 1 month visit window
Through July 2015                Finish follow-up (Maximum of 12 months + 1 month visit window period)
Through April 2016               Lock database, analyze, publish, and disseminate results

    2.3. Eligibility

         2.3.1. Anatomical location of inflammation

       All patients must have met the criteria for intermediate, anterior and intermediate, posterior
       or panuveitis, as defined by the Standardization of Uveitis Nomenclature (SUN) Working
       Group, at any time since their diagnosis of uveitis.

         The Standardization of Uveitis Nomenclature
         ______________________________________________________________
         Type          Primary Site of Inflammation Includes
         ______________________________________________________________
         Anterior Uveitis     Anterior Chamber      Iritis
                                                    Iridocyclitis
                                                    Anterior cyclitis
         Intermediate Uveitis Vitreous              Pars planitis
                                                    Posterior cyclitis
                                                    Hyalitis
         Posterior Uveitis    Retina or Choroid     Focal, multifocal, or
                                                    Diffuse choroiditis
                                                    Chorioretinitis
                                                    Retinochoroiditis
                                                    Retinitis
                                                    Neuroretinitis
         Panuveitis           Anterior Chamber
                              Vitreous
                              Retina or Choroid
         ______________________________________________________________
         *Adapted from the SUN Working Group Anatomic Classification of Uveitis




                                                                                                                   10

```

### DOC-003 PDF page 12

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures


         According to SUN criteria:
         “There was consensus that the term intermediate uveitis should be used for that subset of
         uveitis where the vitreous is the major site of inflammation, and that the presence of
         peripheral vascular sheathing and macular edema should not change the classification.
         The diagnostic term pars planitis should be used only for that subset of intermediate
         uveitis where there is snowbank or snowball formation occurring in the absence of an
         associated infection or systemic disease (that is “idiopathic”). The term panuveitis should
         be reserved for those situations in which there is no predominant site of inflammation, but
         inflammation is observed in the anterior chamber, vitreous, and retina and/or choroid (this
         is, retinitis, choroiditis, or retinal vasculitis). For the definition of panuveitis, structural
         complications such as macular edema or neovascularization should not be considered in
         classifying the anatomic location of uveitis. Inflammation in the anterior chamber and
         vitreous (this is, more vitritis than in an iridocyclitis and more anterior chamber
         inflammation than in intermediate uveitis) should be referred to as anterior and
         intermediate uveitis and not panuveitis.” 30

         2.3.2. Inclusion Criteria

         All the following criteria must be met at enrollment:
              • Historical non-infectious intermediate, anterior and intermediate, posterior or
                  panuveitis in at least one eye
              • Active inflammation within the last 90 days, defined by the presence of any of the
                  following (in at least one eye) according to SUN criteria:
                        ≥ 2+ anterior chamber cells
                        ≥ 2+ vitreous haze
                        active retinal or choroidal lesions

       At least one of the following criteria must be met before or at enrollment:
                   1.) Active inflammation after 4 weeks of high-dose (1mg/kg prednisone
                   equivalent) corticosteroid treatment

                      2.) Treatment with oral corticosteroids resulting in a reduction of inflammation,
                      followed by an increase in inflammation when corticosteroid is tapered, in the
                      14 days prior to enrollment

                       3.) Known chronic condition* necessitating corticosteroid-sparing
                      immunosuppressive treatment**

             •    At least 1+ anterior chamber cells and/or 1+ vitreous haze and/or active
                  retinal/choroidal lesions (bullous serous retinal detachment qualifies) in at least
                  one eye at enrollment

             •    Willingness to start corticosteroid treatment at 1mg/kg or 60mg a day of
                  prednisone, whichever is less

       *According to SUN guidelines, the following uveitic syndromes are thought to require chronic
       immunosuppressive therapy: Behcet’s disease with posterior segment involvement, multifocal
       choroiditis and panuveitis, serpiginous choroidopathy and birdshot retinochoroidopathy.

       **One of the chronic conditions to be considered is late phase Vogt–Koyanagi–Harada
       syndrome (VKH). VKH with posterior synechiae, bullous serous retinal detachments, and/or
       choroidal detachments may be considered in this category.
                                                                                                        11

```

### DOC-003 PDF page 13

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial    September 4, 2012
Manual of Operation and Procedures


         2.3.3. Exclusion criteria

         Any one excludes patient:
            • Any infectious cause of uveitis
            • Media opacity (such as cataract and/or corneal scar) and/or extensive posterior
               synechiae such that examination of the posterior segment is not possible in both
               eyes
            • Chronic hypotony (IOP < 5 mm Hg for > 3 months) in both eyes
            • Prior use of any immunosuppressive drug other than prednisone
            • Periocular or intravitreal corticosteroid injection in the past 2 months
            • Fluocinolone acetonide implant in either eye in < 3 years
            • Intraocular surgery in < 30 days
            • VA of hand motions or worse in better eye
            • < 16 years of age at enrollment
            • Planning to conceive during the study period, pregnant or breast-feeding (blood
               or urine pregnancy test for all females, excluding those who are post-menopausal
               is mandatory)*
            • Unwillingness to abstain from alcohol (2 drinks per month is okay)
            • Cancer
            • Systemic autoimmune disease anticipated to dictate treatment course
            • Abnormal CBC (≤ 2,500 white blood cells and/or ≤ 75,000 platelets and/or ≤10
                hemoglobin) within 14 days prior to randomization*
            • Abnormal alanine aminotransferase (ALT) and/or aspartate aminotransferase
               (AST) ≥ 2 times the upper limit of normal for the lab and/or creatinine ≥ 1.5
               within 14 days prior to randomization*
            • Evidence of active tuberculosis, HIV infection, syphilis, or hepatitis B or C
               (patients must have a tuberculin skin test, or interferon-gamma release assay, a
               chest radiograph, RPR/VDRL, FTA-ABS, Hepatitis B surface antigen and
               Hepatitis C antibody tests within 60 days prior to randomization)**

             *Testing required within 14 days prior to enrollment; **Testing required within 60 days
                prior to enrollment.

    Beyond the tests listed above, the remainder of the work-up is at the discretion of the
    investigator and should be tailored to the clinical situation. Distinguishing between infectious
    and non-infectious uveitis is part of standard of care and should be dictated by the patient’s
    clinical exam, but at minimum, all patients must have testing for tuberculosis, syphilis and
    hepatitis within 60 days prior to enrollment. Given that treatment with antimetabolites is not
    thought to increase the risk of tuberculosis, patients with latent (but not active) tuberculosis
    will be eligible for this study.


    2.4. Randomization and masking

    Block randomization of the patients will ensure that an equal number of patients are
    randomized to each study arm at each site. The exact block size will vary (4, 6, or 8 with
    equal probability) and will only be known to the biostatistician. Randomization lists will be
    created by the biostatistician (Travis Porco) and distributed to the following persons:

    Emergency Contact Personnel
      • Dr. Lalitha Prajna *, Chief Microbiologist, Aravind Eye Hospital
                                                                                                    12

```

### DOC-003 PDF page 14

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial           September 4, 2012
Manual of Operation and Procedures


         •   Dr. Christine Flaxel*, Retina specialist, Casey Eye Institute, Oregon
         •   Dr. Steven McLeod*, Chairman Department of Ophthalmology, University of California
             San Francisco
         *Emergency contact persons who will consult the list only in case of an emergency in which
         unmasking is necessary for patient safety and Dr. Thomas Lietman of the DCC cannot be
         reached.

    Data Coordinating Center (DCC) Personnel
       • Dr. Thomas Lietman, Professor of Ophthalmology and Epidemiology, University of
          California San Francisco, Proctor Foundation
       • Dr. Travis Porco, Principal statistician, Proctor Foundation
       • Dr. Wayne Enanoria*, Research epidemiologist, statistical programmer/analyst, Proctor
          Foundation
         *To be determined if Dr. Enanoria will be masked.

    The study coordinators (listed below) will be aware of patient treatment assignment; however,
    they will not have access to the randomization lists at their site. After consenting patients for
    enrollment, study coordinators will contact the designated person at their site holding
    randomization lists to request treatment assignment by patient ID. Study coordinators will then
    assign patients to that treatment.

    The following study coordinators will not have access to the randomization lists on site:
       • Dr. Natalie Nardone*, Study Coordinator, Proctor Foundation, University of California,
            San Francisco
       • Mr. Meenakshi Sundaram, Study Coordinator, Aravind Eye Hospital Coimbatore, India
       • Mr. Gobinath Kanagaraj, Study Coordinator, Aravind Eye Hospital Madurai, India
       • Ms. Tracy Giles, Study Coordinator, Casey Eye Institute, Oregon

    The following personnel will hold the randomization lists and inform study coordinators of the
    patient assignment:
        • Ms. Sally Tsang, Clinic Manager Proctor Foundation, University of California, San
            Francisco
        • Mrs. A. Maglin Brinda Mary, Aravind Eye Hospital Coimbatore, India
        • Mrs. T.S Chandravati, Aravind Eye Hospital Madurai, India
        • Dr. Jennifer Petrolatti, Pharmacist Casey Eye Institute, Oregon

    *Dr. Nardone will act as a study coordinator to Proctor Foundation patients, as well as a clinical trial
    manager for sites in India and Oregon. At these sites, she will have access to the randomization lists in
    India and Oregon, in order to check patient treatment assignment as a quality assessment.

    All patients and study coordinators will be unmasked to treatment assignment after
    enrollment, as the two study drugs are different in appearance and must be administered on
    different weekly schedules. Study ophthalmologists performing the clinical eye exams, as
    well as visual acuity examiners, OCT operators, fundus photographers and fundus graders
    will be masked to treatment assignment to prevent bias in study outcomes. Leiter's
    Pharmacy will purchase and supply mycophenolate mofetil and methotrexate from
    Amerisource Bergen.

    Leiter’s pharmacy will be responsible for preparing and distributing bottles of the
    medications labeled with randomization codes and dosing instructions to Proctor
    Foundation, and to Casey Eye Institute’s pharmacy where they will distribute the

                                                                                                           13

```

### DOC-003 PDF page 15

```text

```

### DOC-003 PDF page 16

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                 September 4, 2012
Manual of Operation and Procedures


             •    Discontinuation due to efficacy: Patients can discontinue the study
                  medication due to lack of efficacy and be declared a treatment failure and
                  enter Phase II at any time during follow-up if any of the following occur:
                            1. The patient does not reach a prednisone dose of 7.5
                                 mg/day or less and less than or equal to 2 prednisolone
                                 acetate 1% drops per day by 6 months.
                            2. The treating physician determines that it is futile to
                                 continue the current study medication due to persistent,
                                 uncontrolled inflammation that appears to be non-
                                 responsive to treatment.
             •    Discontinuation due to intolerability: Patients who must discontinue the
                  drug as a result of side effects (i.e. severe gastrointestinal upset) will be
                  recorded as a treatment failure. In patients experiencing intolerable side
                  effects, a dose reduction can be used at physician’s discretion. Please refer
                  to Table 5 for dose reduction guidelines.
             •    Discontinuation due to safety: Patients who experience any serious
                  adverse event will exit the study immediately. Patients who experience
                  abnormal lab results meeting the designated threshold of a non-
                  serious adverse event (i.e. AST or ALT increasing to twice the upper
                  limit of normal) will immediately stop taking their medication. As these
                  abnormalities are often reversible, patients whose abnormalities are
                  classified as non-serious adverse events (see Table 3) will be allowed
                  one month to regain eligibility. If the lab results return to normal within
                  one month, patients may be re-administered the study drug per
                  protocol. Otherwise, treatment failure will be declared, at which point
                  patients will exit the study and be treated according to the best medical
                  judgment of their clinician. For other non-serious adverse events (such
                  as an opportunistic infection) the study drug may be stopped
                  temporarily as per the discretion of the investigator.

    Note that if discontinuation of study medication causes a patient to have uncontrolled
    inflammation or >7.5mg/day prednisone at the 6-month visit, treatment failure due to efficacy
    may still be declared. Patients with abnormalities which meet the designated threshold of a
    serious adverse event (SAE) will exit the study immediately and be treated according the
    best medical judgment of their physician.


           Table 3: Thresholds for classifying non-serious and serious lab abnormalities
                                   Non-Serious Adverse Event               Serious Adverse Event
      Leukocytes                   >1,000 and <2,500/μL lasting            <2,500 lasting more than 1
                                   less than 1 month                       month or ≤ 999/μL
      Platelets                    20,000 to 75,000/μL lasting less        ≤ 20,000/μL or <75,000/μL
                                   than 1 month                            lasting greater than one month
      Hemoglobin                   > 6.4 to < 10 g/dL                      ≤ 6.4 g/dL
      SGOT (AST) or                2 to 5 times the upper limit of         > 5 times the upper limit of
      SGPT (ALT)                   normal of the reference range           normal of the reference range
      Creatinine                   ≥ 1.5 to < 2 mg/dL                      ≥ 2 mg/dL

             • Dropout from study: Subjects will be considered to have dropped out

                                                                                                                 15

```

### DOC-003 PDF page 17

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures


                  from study only if they declare they are no longer interested in further
                  participation or are deceased. It should be noted that missing a visit
                  does not mean that a patient has dropped out of the study, for
                  example, if they missing the 1 month visit every attempt will be made
                  to bring them back as soon as possible and to continue with
                  subsequent visits. Also, a non-serious adverse event or
                  discontinuation of study medication does not mean a patient has
                  dropped out of the study, and they should continue to be followed
                  according to the protocol, as they may be able to resume treatment.
                  We anticipate that a few patients may drop out due to relocation,
                  unwillingness to continue or death. In case of patient dropout, the
                  patient dropout form should be filled out.

                  If death is considered to be related to the study drug, the patient will
                  be counted as a treatment failure. If death is not related to the study
                  drug the patient will be counted as a dropout. This would be at the
                  discretion of the medical monitor.




                                                                                                        16

```

### DOC-003 PDF page 18

```text
          First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial            September 4, 2012
          Manual of Operation and Procedures



2.5.3. Primary Endpoint Flowchart




                                                                                                                      17
*Criteria for controlled inflammation: Anterior chamber cells ≤0.5 +; Vitreous haze ≤ 0.5 +; No
active choroid and retina lesions
** 2 drops/day refers to topical 1% prednisolone acetate or equivalent

```

### DOC-003 PDF page 19

```text

```

### DOC-003 PDF page 20

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial     September 4, 2012
Manual of Operation and Procedures


         3.1.1. Methotrexate

    All methotrexate doses will be taken once per week in a divided dose, one dose taken in the
    morning and one in the evening. For the first two weeks, an introductory dose of 15 mg/week
    orally will be administered to assess tolerability. After two weeks, the dose will be increased
    to 25 mg/week until the end of follow-up or until treatment failure due to intolerability, adverse
    events, or of lack of efficacy.

    If there are tolerability issues in the first two weeks such that the patient is not able to
    increase the dose, treatment failure due to intolerability should be declared. The patient
    would then be eligible to switch treatment in Phase II. If this occurs in Phase II, treatment
    failure would be declared and the patient would exit the study. If the dose is increased per
    protocol at two weeks, the study ophthalmologist can decide to reduce the maintenance
    dose if the patient experiences severe side effects. For the first dose reduction, methotrexate
    will be reduced to 20 mg per week. If side effects persist and the study ophthalmologist
    wishes to reduce the dose a second time, the dose will be reduced to 15 mg per week. After
    the second dose reduction, treatment can be stopped if intolerability persists and the patient
    can switch to Phase II. Treatment can be stopped early due to lack of efficacy or adverse
    events.

    To maintain masking, study coordinators will review patient side effects with the patient at
    each visit, prior to meeting with the physician. At this time, the study coordinator will remind
    the patient not to speak to their study doctor regarding the name of the medication or dosing
    instructions. If the patient is experiencing intolerable side effects, and the study coordinator
    believes a dose reduction should be considered, this will be brought up with the study
    physician. The study coordinator and patient will talk to the physician without revealing the
    name of the medication or the dosing instructions. The study doctor will then decide if the
    dose reduction should be done. The study coordinator will then provide the patient with new
    dosing instructions, away from the vicinity of the study physician (see Table 5).

         3.1.2. Mycophenolate mofetil

    Mycophenolate mofetil will be taken twice daily. Patients will be advised by the study
    coordinator to take this medication on an empty stomach. For the first two weeks, an
    introductory dose of 500 mg BID orally will be administered to assess tolerability. After two
    weeks, the dose will be increased to 1.5 g BID until the end of follow-up or until treatment
    failure due to intolerability, adverse events, or lack of efficacy.

    If there are tolerability issues in the first two weeks such that the patient is not able to
    increase the dose, treatment failure due to intolerability should be declared. The patient
    would then be eligible to switch treatment in Phase II. If this occurs in Phase II, treatment
    failure would be declared and the patient would exit the study. If the dose is increased per
    protocol at two weeks, the study ophthalmologist can decide to reduce the study treatment
    dose, if the patient experiences severe side effects. For the first dose reduction,
    mycophenolate will be reduced to 1g BID. If side effects persist and the study
    ophthalmologist wishes to reduce the dose a second time, the dose will be reduced to 500
    mg BID. After the second dose reduction, treatment can be stopped if intolerability persists
    and the patient can switch to Phase II. Treatment can be stopped early due to lack of
    efficacy or adverse events.

    To maintain masking, study coordinators will review patient side effects with the patient at
    each visit, prior to meeting with the physician. At this time, the study coordinator will remind
                                                                                                     19

```

### DOC-003 PDF page 21

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


    the patient not to speak to their study doctor regarding the name of the medication or dosing
    instructions. If the patient is experiencing intolerable side effects, and the study coordinator
    believes a dose reduction should be considered, this will be brought up with the study
    physician. The study coordinator and patient will talk to the physician without revealing the
    name of the medication or the dosing instructions. The study doctor will then decide if the
    dose reduction should be done. The study coordinator will then provide the patient with new
    dosing instructions, away from the study physician (see Table 5).

         3.1.3. Folic acid

    It is standard of care to prescribe folic acid supplements to reduce the severity of side effects
    in patients treated with methotrexate. All patients randomized to methotrexate will be
    prescribed 1 mg per day of folic acid.

         3.1.4. Packaging and distribution of study medications

    Patient medications will be packaged and distributed by Leiter’s Pharmacy, to the two U.S.
    sites, Proctor Foundation and Casey Eye Institute. Medication will be distributed to Aurolab
    in India, and they will package and distribute it to the sites in Madurai and Coimbatore, South
    India.

    Introductory bottles will contain 14 days of medication at the lower doses (15 mg for
    methotrexate and 500 mg for mycophenolate mofetil). Bottles with the maintenance dose will
    contain 30 days’ worth of medication. At the patient’s first visit (i.e. Baseline for Phase I) they
    will be given the 14 day introductory dose and the 30 day maintenance dose). At every
    monthly visit following, patients will be given an additional 30 days’ worth of medication, until
    5 months. If patients enter Phase II after treatment failure in Phase I, patients’ medication will
    be dispensed following the same schedule as in Phase I. If patients enter Phase I (6-12
    months) after treatment success in Phase I (0-6 months), they will be given 120 days’ worth
    of medication at their 6 month visit. Lost bottles will be replaced.

    Study medications, labeled with the appropriate dosing instructions, will be distributed to the
    study coordinator prior to each study visit. After randomization, before the drug is dispensed,
    the study coordinator will place the Study ID label on the bottles. If a dose reduction is used,
    the study coordinator will put a label on the bottle with the new instructions.

         3.1.5. Adherence to the treatment plan

    Patients will be given a treatment diary in the form of a checklist in which they can record
    missed doses. They will be asked to bring the diary with them to each visit. Adherence will
    be monitored by the study coordinator through review of the treatment diaries, and will be
    recorded on the Medication Adherence Log in each patient file. Pill counting will also be done
    for a more objective measure of adherence.

    The following instructions will be given to the patients if they miss scheduled doses of their
    medication:
        Methotrexate: If a patient misses their scheduled dose, they may take it the next day. If it
        is not taken the next day, they should wait until the following week.
        Mycophenolate Mofetil: If the patient misses a dose, they should continue with the
        regular dosing schedule.


                                                                                                      20

```

### DOC-003 PDF page 22

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial     September 4, 2012
Manual of Operation and Procedures


    3.2. Corticosteroid therapy

         3.2.1. Oral prednisone

    Prednisone vs. alternative oral corticosteroid

    Unless contraindicated, oral prednisone should be used. An equivalent dose of an alternative
    oral corticosteroid may be used only if a specific contraindication to oral prednisone is
    present. All references to oral corticosteroid and specific dosing schedules presented in this
    Manual of Procedures are given for oral prednisone.

    Initial dose

    All patients enrolled in the study will be initially taking concomitant oral corticosteroids at 1
    mg/kg or 60 mg daily, whichever is less. Treatment success is dependent upon successfully
    tapering concomitant prednisone to ≤ 7.5 mg/day. Initial corticosteroid dose will be continued
    for 2 to 4 weeks at which point prednisone will be gradually tapered1. Prednisone will be
    tapered to and held at 7.5 mg/day for the first 6 months of the study (i.e. until the end of
    Phase I). Further reduction of corticosteroids will be allowed in Phase II, if patients continue
    on the same medication as Phase I. If patients switch treatments and enter Phase II, they will
    follow the same protocol as the initial Phase I corticosteroid treatment. At any point,
    investigators have the option of reducing the prednisone dose if the patient is experiencing
    severe side effects, but it is strongly encouraged to follow the corticosteroid tapering
    guidelines.

    Tapering schedule

    For all patients, oral prednisone will be tapered gradually to ≤ 7.5 mg/day if possible
    according to Standardization of Uveitis Nomenclature (SUN) guidelines (see Table 6). As it
    takes 6-8 weeks for the study medications to take full effect, it is expected that inflammation
    may become uncontrolled with a corticosteroid taper in some patients during the first 3
    months of the study. This does not necessarily mean that the randomized treatment has
    failed, since more time may be needed to ensure the drug has reached its full effect.
    However, some patients who have uncontrolled inflammation are not responding to the
    medication; if the study ophthalmologist believes that continued treatment is futile prior to the
    primary endpoint, treatment failure may be declared and the patient treated according to the
    best medical judgment. At any point in this tapering schedule, investigators have the option
    to reduce the corticosteroid dose if the patient is experiencing severe side effects.




                                                                                                     21

```

### DOC-003 PDF page 23

```text
    First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial              September 4, 2012
    Manual of Operation and Procedures


        Table 6: Tapering schedule for oral prednisone: Phase I or if starting new medication in Phase II

     Dose (mg/day)                             Duration
                                                    1
                                                        (weeks)                    Decrement (mg/day)
     60                                        2–4                                 10
     50                                        1                                   10
     40                                        1                                   5
     35                                        1                                   5
     30                                        1                                   5
     25                                        1                                   5
     20                                        1                                   2.5
     17.5                                      1                                   2.5
     15                                        1                                   2.5
     12.5                                      1                                   2.5
     10                                        1                                   2.5
     7.5                                       hold*


NOTE: Begin patients at 1mg/kg or 60 mg/day, whichever is less. For Phase I hold patients at 7.5 mg/day,
up to the end of 6 months.
1
  If uveitis does not improve at the end of the first 4 weeks, use best medical judgment regarding
supplemental treatment (e.g. pulse dose treatment, corticosteroid injections, additional
immunosuppressives).


                             Table 7: Optional tapering schedule Phase I (6-12 months)

     Dose (mg/day)                             Duration (weeks)                    Decrement (mg/day)
     7.5                               1*                               2.5
     < 7.5 & ≥ 5                       2-4                              1 - 2.5
     < 5 & ≥ 2.5                       2-4                              1.5 - 2.5
     < 2.5 & ≥ 1                       2-4                              1
     0
    NOTE: When beginning Phase I (6-12 months), hold patient at 7.5 mg/day, for at least one week.

              Directions for Rescue Taper

        Reactivations can be mild or severe. Mild reactivations are considered an increase in
        inflammation up to the 1+ level in anterior chamber cell or vitreous haze. Severe
        reactivations are considered an increase in inflammation up to the 2+ level or higher in
        anterior chamber cell or vitreous haze. Retinal/choroidal lesions may be considered mild or
        severe at the discretion of the study physician.

                  If uveitis reactivates:

                       • Increase oral prednisone up to a dose of 1 mg/kg for severe reactivations, or
                       for mild reactivations, up to double the dose at which the flare occurred, until
                       uveitis is controlled. Then re-taper according to the guidelines.

        Uveitis is considered non-responsive if inflammation does not increase but does not further
        improve after the first 4 weeks of treatment.

                  If uveitis is non-responsive:

                        • Hold the current dose of prednisone for an additional week. If still no
                        improvement, treatment failure due to efficacy may be declared, and patients
                                                                                                                  22

```

### DOC-003 PDF page 24

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial     September 4, 2012
Manual of Operation and Procedures


                    may proceed to Phase II.

       After suppression of uveitis is once again achieved (either in the case of reactivation or non-
       response) follow the taper guidelines for Phase I. Patients who have failed the treatment to
       which they are randomized will then switch treatments, begin Phase II, and follow the same
       taper guidelines as Phase I (0-6 months). If patients flare during Phase II, they can follow
       directions for the rescue taper listed above. Patients who fail the second treatment will exit
       the study and be treated as per the investigators discretion.

         3.2.2. Supplements

         All patients will be given recommendations for supplemental treatment. This treatment is
         important for patients receiving oral corticosteroids, in order to minimize the incidence of
         osteoporosis. Recommendations will include:
             • Calcium supplement, 500 mg 3 times daily (unless contraindicated)
             • Vitamin D, 400-800 IU daily.

         3.2.3. Topical corticosteroid

       In addition to oral prednisone, patients may enter the study on varying doses of topical
       corticosteroid drops. Topical corticosteroids should be tapered according to the suggested
       guidelines (Table 8). The goal will be to completely taper off topical corticosteroids, but a
       dose of ≤ 2 times a day prednisolone acetate 1% or equivalent corticosteroid will be
       considered medically acceptable. The chronic use of two times a day prednisolone acetate
       was also considered to be medically acceptable in the survey we conducted of the
       American Uveitis Society members.

                 Table 8: Suggested tapering schedule for topical corticosteroid drops

                    Dose                                Duration (weeks)
                    8 times a day                              1-2
                    6 times a day                              1
                    4 times a day                              1
                    3 times a day                              1
                    2 times a day                              1
                    1 time a day                               1
                    None


    3.2.4. Other adjunctive treatments/procedures

       The protocol dictates use of oral prednisone, corticosteroid drops and study medication
       (methotrexate or mycophenolate). The investigator may use other topical adjunctive
       medications such as IOP lowering medications and cycloplegic agents. These should be
       recorded on the Treatment Assessment form at each visit. The protocol does not allow for
       corticosteroid injections, intravenous therapy, additional immunosuppressives or surgery
       during the study period. If it is felt to be necessary to do one of these, the Protocol
       Deviation form should be completed and sent to the Medical Monitor and Principal
       Investigator.


                                                                                                     23

```

### DOC-003 PDF page 25

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                 September 4, 2012
 Manual of Operation and Procedures


      3.3. Study procedures

 Enrollment visit

Study coordinators should adhere to the following protocol for study procedures taking place at the
enrollment visit.

        •    The patient’s eligibility for participating in the study will be determined between
             the study coordinator and the study physician.
        •    If eligible, the patient will review the consent form with the study coordinator and
             the study physician, and give their consent.
        •    After consent, the study coordinator will assign the patient a unique Patient ID
             (derived from the list provided to the study coordinator from the principal
             statistician).
        •    The study coordinator will then contact the designated person on site, holding
             the randomization list, to obtain the patient’s drug assignment. This will be done
             away from sight of the study physician.
        •    The study coordinator will then label the medication with the assigned Patient
             ID.

 Study visits

Study coordinators should adhere to the following protocol for study procedures taking place, after
the patient is consented, enrolled and randomized. All study procedures should follow the schedule
listed below:

        •    The patient comes for a study visit and meets with the study coordinator before
             their study doctor.
        •    The patient’s medication bottle is immediately placed in a secure, opaque bag
             and left at the study coordinators desk for the remainder of the visit.
        •    The study coordinator will check-in with the patient and complete the following
             in any order:
                 o Review of patient medication diaries
                 o Review of adverse events since last visit*
                 o Dispense new mediation bottles (if applicable)
                 o Completion of SF-36 questionnaire (All patients) (if applicable)
                 o Completion of NEI-VFQ-25 (U.S. patients only) or IND-VFQ (Indian
                     patients only) (if applicable)
                 o Review with the patient that they are not to speak with their study doctor
                     about their dosing schedule, or the name of the medication that they are
                     currently taking.
*If the patient is experiencing intolerable side effects, and the study coordinator believes a dose reduction should
be considered, this will be brought up with the study physician. The study coordinator and patient will talk to the
physician without revealing the name of the medication or the dosing instructions. The study doctor will then
decide if the dose reduction should be done. The study coordinator will then provide the patient with new dosing
instructions, away from sight of study physician.

        •    The patient will then complete the following assessments, in the following order:
                o Visual Acuity Assessment
                o Slit lamp front of the eye exam and intra-ocular pressure
        •    The patient’s eyes will then be dilated and the following assessments will be
             completed, in any order**:
                                                                                                                   24

```

### DOC-003 PDF page 26

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                       September 4, 2012
 Manual of Operation and Procedures


                   o Posterior segment exam
                   o OCT measurements
                   o Fundus photography
                   o Laboratory measurements
         •     After completion of the study visit, the patient will meet with the coordinator,
               review scheduling for the next study visit, and retrieve their medication.
**It is essential that vision, front of the eye exams and intra-ocular pressure are completed before dilation of
the eyes.

4. Study visits
      4.1. Visit schedules

             4.1.1. Phase I: First-line treatment

After eligibility has been evaluated and informed consent given for participation in the trial,
patients will be randomized to receive either methotrexate or mycophenolate mofetil. Patients will
continue with this course of treatment unless treatment failure occurs due to safety, intolerability
or lack of efficacy (if a failure is recorded within the first 6 months, the treatment assignment will
be switched to the drug not initially randomized to, and the patient will follow a new visit
schedule). Patients who are deemed treatment failures in Aim 1 due to safety (serious adverse
event) will exit the study and not proceed to Aim 2. Treatment success, according to the primary
endpoint, will be assessed at 6 months. If treatment has been deemed successful for a patient
at 6 months, they will be provided study medication for an additional 6 months and return for
additional study visits as shown below. As long as the patient stays on the first randomized
medication, Visit Schedule I will be followed.

         Guidelines for Visit Schedule I
         •     Day 1 corresponds to the Baseline-I visit, which is also the first day the patient
               receives treatment.
         •     Visit windows are determined based on the date of randomization.
         •     Baseline data must be at the Baseline-I visit, with the exception of
               laboratory measurements which may be collected within 14 days prior to or on
               the date of randomization.
         •     There should be a minimum of 2 weeks between each study visit.
         •     Data for the baseline and follow-up visits may be collected anytime within
               the visit window.

                               Table 9: Visit Schedule Phase I (0-6 months) or Phase II

                                 Visit                   Code           Window (weeks)
                                 Baseline*               BL-1 (II)
                                 Week 2                  Wk2 (II)
                                 Month 1*                M1-I (II)      ±15 days
                                 Month 2                 M2-I (II)      ±15 days
                                 Month 3                 M3-I (II)      ±15 days
                                 Month 4                 M4-I (II)      ±15 days
                                 Month 5                 M5-I (II)      ±15 days
                                 Month 6                 M6-I (II)      -15 to +30 days

*Every visit scheduled will be from the baseline visit date (Phase 1). **Every monthly visit will be calculated from the
baseline visit, using the average amount of days per month.

                                                                                                                           25

```

### DOC-003 PDF page 27

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
 Manual of Operation and Procedures


                            Table 10: Visit Schedule Phase I (6-12 months)

                       Visit                   Code          Window (weeks)
                       Month 6*                M6-I          ±15 days
                       Month 9*                M9-I          ±15 days
                       Month 12*               M12-I         -15 to +30 days
                          * since baseline/treatment administration (Phase 1)

            4.1.2. Phase II: Rescue treatment

In case of the first randomized treatment failure due to intolerability or lack of efficacy within the
first six months of treatment, the treatment assignment will be switched to the alternate treatment.
At this point, the patient will receive the antimetabolite not originally randomized to and will be
followed an additional 6 months or until failure of the second treatment.

        Guidelines for Visit Schedule II
        •     Day 1 corresponds to the Baseline-II visit, which is also the first day the patient
              receives rescue treatment with the medication not initially received.
        •     Visit dates are determined based on the date of the Baseline-II visit (which may
              also be the same date as the Phase I treatment failure date), and may not be
              changed.
        •     The Baseline-II visit form should be completed to gather information on any
              changes in health status or medications.
        •     There should be a minimum of 2 weeks between each study visit.
        •     Data for the follow-up visits may be collected anytime within the visit window.

            4.1.3. Non-study visits

Despite the regular follow-up outlined in the visit schedules above, it is anticipated that some
patients will have inflammation that is difficult to control or be intolerant to the drug. These patients
may require additional visits that do not fall within the study visit window. It is possible that the
circumstances leading to such visits may result in changes to oral or topical corticosteroid dose, or
a declaration of treatment failure and a need for rescue treatment.

        Guidelines for non-study visits

        •     Any changes to oral or topical corticosteroid dose will be noted on the appropriate form
              during the next scheduled study visit.
        •     If a treatment failure is declared at a non-study visit during follow-up while being treated
              with…
                     • Phase I (initial randomized treatment): Record a treatment failure using
                        Treatment Assessment Form. Perform BL-II visit at this time or within 7 days.
                        Phase II rescue treatment will be administered as soon as BL-II data has
                        been recorded.
                     • Phase II: Record a treatment failure using the Treatment Assessment Form.
                        Patient exits study.
                     • If treatment failure is declared at a non-study visit, an attempt should be made
                        to collect as much information as possible, including the forms listed in Table 9.



                                                                                                         26

```

### DOC-003 PDF page 28

```text
    First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                   September 4, 2012
    Manual of Operation and Procedures


    4.2. Study forms completion schedule
                           Table 9: Forms to be completed throughout patient follow-up


                                       PHASE I                                               PHASE II
                                Follow-up                    Follow-up                 Follow-up                 Follow-up
                   Baseline:      study       Treatment        study       Baseline:     study       Treatment     study
                    Phase I    months 1-5,     Failure*       months       Phase II     months        Failure*    month 6
                                    9                        6 and 12                     1-5


   Patient
   Consent
                    X
    Forms

   Eligibility
 Criteria Form
                    X
   Baseline         X                                                        X
 History Form

  Clinical Eye
  Exam Form
                    X             X             X             X              X          X             X            X
 Visual Acuity      X             X             X             X              X          X             X            X
    Forms

  OCT Form          X             X             X             X              X          X             X            X
  Fundus
  Photos
                    X                           X             X              X                        X            X
  Laboratory
  Report Form       X             X                           X              X          X                          X
   Adverse
    Event                        (X) (X) (X) (X) (X) (X) (X)
    Forms

 Quality of Life    X                           X             X             X                         X            X
 Questionnaires

  Treatment                       X             X             X              X          X             X            X
 Assessment
    Form

Patient Dropout
      Form
                                 (X) (X) (X) (X) (X) (X) (X)
 (if applicable)


    Protocol       (X) (X) (X) (X) (X) (X) (X) (X)
deviation form
(if applicable)

         *Note that treatment failure may be declared at a scheduled study visit or at a non-study visit.
                                                                                                                             27

```

### DOC-003 PDF page 29

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


    4.3. Enrollment and Baseline-I visit

    All baseline data must be collected at the Baseline-I visit, with the exception of
    laboratory measurements which may be collected within 14 days prior to or on the date of
    randomization.

         4.3.1. Consent and eligibility evaluation

         Procedures for obtaining consent include explaining the patient’s disease,
         prognosis, and treatment options, discussing the risks and benefits of participation, and
         addressing the patient’s questions and concerns. After explaining the nature of the study
         and the rights and responsibilities of the patient, the ophthalmologist and/or the study
         coordinator will obtain written consent from the subject, or written minor assent and
         parental consent if applicable. The subject is assured that participation in this study is
         voluntary and he/she can withdraw at any time if he/she feels uncomfortable.

         The eligibility evaluation will be performed using the Eligibility Form, which is to be filled
         out at the Baseline-I visit. For detailed inclusion/exclusion criteria please see Section 2.3.

         There is not a mandated separate visit for eligibility screening. If the patient fulfills all
         eligibility and exclusion criteria on a visit, he/she may sign the consent form and be
         randomized at the beginning of the official Baseline-I visit. Note that this requires that
         the patient have laboratory results that are current according to inclusion criteria
         guidelines.

         In some cases, partial eligibility will be confirmed on a screening visit but more
         information may be needed (such as laboratory confirmation of acceptable values of
         the CBC, AST, ALT and creatinine). If and when the laboratory results meet eligibility
         criteria, the patient will then be asked to complete a consent form, followed by
         randomization and the official Baseline-I visit.

         4.3.2. Randomization
         Assignment of a randomization number takes place during the Baseline-I visit after
         eligibility has been determined and the consent forms have been signed by the patient.
         After obtaining the written consent, the patient is assigned the next identification number
         from the randomization list. The study coordinator then informs the on-site person who
         carries the treatment assignment list to find out the treatment assignment that
         corresponds to the particular study ID.

         4.3.3. Procedures for data collection
       Required study procedures include the following:

             •    Medical and treatment history
             •    Clinical eye exam
             •    Visual acuity exam
             •    Optical Coherence Tomography (OCT)
             •    Fundus photography
             •    Laboratory measurements




                                                                                                      28

```

### DOC-003 PDF page 30

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial       September 4, 2012
Manual of Operation and Procedures



             •    Health-related quality of life questionnaire
             •    Vision-related quality of life questionnaire

         4.3.4.    Specimens

         The following specimens will be collected for laboratory measurements:
            • Blood for complete blood count (CBC with differential, limited to percentages of
            neutrophils and lymphocytes)
            • Blood for serum chemistry panel (AST, ALT, creatinine)
            • Blood or urine pregnancy test (all female patients, excluding those that
                 are post- menopausal)

         4.3.5. Forms for data collection

         The following forms will be filled out as part of the Baseline-I visit:
            • Patient Consent Forms
            • Eligibility Form
            • Baseline History Form
            • Clinical Eye Exam Form
            • Right Eye Visual Acuity Form
            • Left Eye Visual Acuity Form
            • OCT Form
            • Fundus Photography Form
            • Laboratory Report Form
            • Quality of Life Questionnaire Forms

    4.4. Follow-up visits

    All follow-up visit data must be collected within the study visit window.

         4.4.1.    Procedures for data collection

         Required study procedures include the following:
             • Clinical eye exam
             • Visual acuity exam
             • Optical Coherence Tomography
             • Fundus Photography
             • Laboratory measurements
             • Health-related quality of life questionnaire (if applicable*)
             • Vision-related quality of life questionnaire (if applicable*)
         *Phase 1: treatment failure or 6 month visit (whichever is first), 12 month visit; Phase 2:
         treatment failure or 6 month visit.

         4.4.2. Specimens

         The following specimens will be collected for laboratory measurements:
            • Blood for complete blood count (CBC with differential, limited to percentages of
            neutrophils and lymphocytes)
            • Blood for serum chemistry panel (AST, ALT, creatinine)
                                                                                                       29

```

### DOC-003 PDF page 31

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial         September 4, 2012
Manual of Operation and Procedures


             •    Blood or urine pregnancy test (all female patients, excluding those that
                  are post- menopausal)

         4.4.3. Forms for data collection
         The following forms will be filled out as part of the follow-up visits:
            • Baseline History Form Phase II (as needed*)
            • Clinical Eye Exam Form
            • Right Eye Visual Acuity Form
            • Left Eye Visual Acuity Form
            • OCT Form
            • Fundus Photography Form
            • Laboratory Report Form
            • Adverse Event Checklist
            • Medication Adherence Form
            • Treatment Assessment Form
            • Adverse Event Log (update if necessary)
            • Quality of Life Questionnaire Forms (if applicable**)
            • Serious Adverse Event Narrative Form (if applicable)
            • Patient Dropout Form (if applicable)
            • Protocol Deviation Form (if applicable)
         *This will only be needed if patients switch to Phase II.
         *Phase 1: baseline, treatment failure or 6 month visit (whichever is first), 12 month visit;
         Phase 2: treatment failure or 6 month visit

    4.5. Baseline-II

    Note that some Baseline-II visit data may correspond to data collected for the visit at which
    treatment failure was declared for Phase I.

         4.5.1. Eligibility

    In Phase I, if failure is due to efficacy or tolerability, the patient will be considered as eligible
    for Phase II of the study. If there is a serious adverse event in Phase I, the patient will exit
    the study and not enter Phase II.

    The Baseline History Form-II will be completed to obtain updated health related information.

    As in Phase I, there is no mandated separate visit for eligibility screening. If the patient fulfills
    all eligibility criteria at the time of treatment failure, he/she may immediately proceed to the
    Baseline-II visit.

    4.6. Non-study visits

    Despite frequent study visits, some patients may need additional visits with their clinician
    according to standard of care that do not fall within study visit windows. Required data
    collection during these non-study visits is limited to adverse event reporting and declaration
    of treatment failure.

         4.6.1. Procedures for data collection

         Required study procedures include the following:
                                                                                                            30

```

### DOC-003 PDF page 32

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial         September 4, 2012
 Manual of Operation and Procedures


              •    Clinical eye exam (if treatment failure is declared)

          4.6.2. Specimens

          No specimens are required during non-study visits.

          4.6.3. Forms for data collection

          The following forms will be filled out at non-study visits only if treatment failure is declared.
             • Clinical Eye Exam Form
             • Treatment Assessment Form

         The following forms will be filled out at non-study visits only if a serious or non-serious
        adverse event has occurred:

              •    Adverse Event Checklist
              •    Adverse Event Log (update)

     All Phase II procedures and protocol are the same as Phase I. For Phase I patients who
     are continuing on the same medication, physicians can see the patients as often as they
     would like. However, for purposes of this study we will only be recording information at
     Month 9 and Month 12, or a non-study visit that leads to treatment failure.

5. Study examinations and procedures

     5.1. Quality of life questionnaire administration

     All patients will be asked to complete standard quality of life questionnaires related to
     overall health and visual function at baseline visits as well as at 6 months or treatment
     failure (whichever is first) in order to measure quality of life outcomes. Patients who
     experience treatment success with Phase I treatment through the maximum follow-up of 12
     months will also complete questionnaires at the 12- month visit. The following
     questionnaires will be administered:

     Health-related quality of life

     • SF-36 questionnaire (all patients)

     Vision-related quality of life

     • NEI-VFQ-25 (U.S. patients only)

     • IND-VFQ (Indian patients only)

     Given data suggesting that SF-36 scores vary by method of administration such that
     patients overstate quality of life in clinic interviews, questionnaires will be self-administered
     whenever possible at clinic appointments It is anticipated that some patients will not have
     adequate visual function to complete the questionnaire on their own, and some patients
     may also be illiterate. In such cases, the coordinator will read the questions aloud to the
     patient and record the patient’s answers on the appropriate questionnaire forms (Section
     A.14). It is very important that the questions are answered in their original form, so

                                                                                                          31

```

### DOC-003 PDF page 33

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                 September 4, 2012
 Manual of Operation and Procedures


     coordinators should never rephrase or interpret questions for the patient.

     5.2. Refraction and visual acuity

          5.2.1. Refraction procedure
        Beginning Approximate Refraction

     The beginning approximate refraction should be obtained by performing retinoscopy or
     auto- refraction. One of these measurements is used as the beginning approximate
     refraction at each visit.

     Subjects who arrive for examination wearing contact lenses are asked to remove the
     lenses prior to refraction. The subject must wait for 30 minutes after removing the contact
     lenses before refraction can be performed.

     Refraction may be initially performed at distances different than four meters (i.e.
     using a phoropter in a common refraction lane). However, if this is done, the spherical
     power refinement step must be repeated with lenses in place after the subject has been
     positioned at four meters for visual acuity testing.

     The examiner will use Chart R (Precision Vision Chart Version 2305b) for manifest
     refraction. Each eye is refracted at four meters unless the visual acuity measured at this
     distance on chart R is worse than 20/200 (defined as missing 2 or more letters on the top
     line, the 20/200 or 6/60 line). This subject must then be moved to a distance of one meter
     from the study visual acuity chart, and refraction must be performed and recorded at this
     distance. Use of Visual Acuity Form R is optional but may be helpful in keeping track of
     patient’s acuity level.

        Manifest Refraction

     In general, instructions are to ‘push plus’ and to add minus diopter corrections only if there
     is a demonstrated increase in visual acuity, i.e., the patient is able to read more letters.
     The steps are as follows:
            • Seat the subject 4 meters in front of the refraction chart;
            • Place and adjust the trial frame on the subject’s face so that the lens cells are
                parallel to the anterior plane of the orbit;
            • Adjust the pupillary distance of the trial frame to make sure that the lenses
                position in front of the centers of the pupils;
            • Adjust the lens cells for the proper distance from the cornea;
            • Occlude the eye not being refracted;
            • Insert spherical lens correction into the compartment closest to the eye;
            • Place cylindrical lens correction in the compartment in the front of the frame;
            • Set cylindrical lens to appropriate axis setting

     Please refer to the table below to ensure that proper lenses are used for the appropriate
     visual acuity level:

Vision with                                                     Cylinder
                               Sphere                                                       Sphere Refinement
Best Correction                                         Use correct JCC as below
                        Power        Increment         Axis       Power         Increment   Power     Increment

                                                                                                                  32

```

### DOC-003 PDF page 34

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial            September 4, 2012
 Manual of Operation and Procedures


6/3-6/24                +0.50           +0.50          0.50        0.25         +0.25   +0.37      +0.25
20/10-20/80             -0.37           -0.25                                   -0.25   -0.37      -0.25
(4 meters)              +0.50           +0.50                                           +0.37      +0.25
6/30-6/60               +1.00           +1.00          1.00        1.00         +1.00   +0.50      +0.50
20/100-20/200           -1.00           -1.00                                   -1.00   -0.50      -0.50
(4 meters)              +1.00           +1.00                                           +0.50      +0.50
<6/60                   +2.00           +2.00          1.00        1.00         +1.00   +1.00      +1.00
<20/200                 -2.00           -2.00                                   -1.00   -1.00      -1.00
(1 meter)               +2.00           +2.00                                           +1.00      +1.00

        Examples for each visual acuity level are detailed below.

For Patients with Visual Acuity of 6/3-6/24 (20/10-20/80):

          Determine Sphere Power
              •    Ask patient to identify the orientation of the tumbling “E”s on the smallest
                   possible line that he/she can see on the Chart R;
              •    With the subject looking at the smallest line legible on the visual acuity chart,
                   place a +0.50 spherical lens in front of the eye being tested. Ask the subject, “Is
                   vision better, worse, or the same?”
              •    If the subject responds that vision is made better or if there is no change,
                   replace the spherical lens with one that is +0.50 more plus;
              •    Continue to check with the +0.50 lens to see if the subject will accept more
                   plus by repeating the step above;
              •    When an additional +0.50 lens makes the subject’s vision worse, remove the +0.50
                   lens
              •    Then hold a -0.37 spherical lens over the eye;
              •    If this -0.37 lens improves the subject’s vision, even by one letter, replace the
                   spherical lens in the trial frame by one that is -0.25 more minus;
              •    If the -0.37 spherical lens does not allow the patient to read more letters or if it
                   makes the vision worse, move on to cylindrical testing;• Remember,          if   the
                   patient reports that the -0.37 lens makes the vision better but if s/he is unable to
                   read more letters, do not change spherical lens by -0.25.

          Determine and refine cylinder axis
        The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
        refraction.

              •    Ask the subject to look at a letter on a line of Chart R which is one line larger
                   than the smallest line he/she could read (one above threshold);
              •    If no cylinder is present in the beginning approximate refraction, place the
                   +/- 0.50 diopter cross-cylinder with the positive axis first at 90º and then at 180º,
                   asking if either position makes the letters clearer;
              •    If the patient prefers either one of these positions, place a +0.50 cylindrical lens
                   in the trial frame aligned with the preferred axis;
              •    If the patient did not prefer cylinder at axis 90° or 180°, position the cross
                   cylinder with the positive axis first at 45° then 135°;
              •    Ask if the patient prefers either of these positions;
              •    If so, place a +0.50 cylinder lens in the trial frame aligned with the preferred axis;
              •    If the subject prefers none of the four positions, no further cylinder testing is
                                                                                                          33

```

### DOC-003 PDF page 35

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures


                  required;
             •    If cylinder is present in the beginning approximate refraction or if you have
                  added +0.50 cylinder power in the above step, position the +/- 0.50 diopter
                  cross-cylinder first with the positive axis 45º to the right of the cylinder axis
                  (position one), and secondly with the positive axis at 45º to the left of the cylinder
                  axis (position two). Ask the subject which position improves vision (position one or
                  position two?);
             •    If the subject responds that neither position is better and if this was the first test
                  of axis position, move the axis of the cylinder in the trial frame 15º to the right or
                  left and repeat;
             •    If the subject prefers one position to the other, rotate the cylinder toward the
                  preferred positive axis of the cross-cylinder in the step sizes recommended (see
                  Table below) and repeat. (If the subject states that one position of the cross-
                  cylinder is no better than the other position, proceed to refining cylinder power).
                               Table: Axis step sizes for refinement of cylinder.

                                    Cylinder Power           Axis Step Sizes
                                    < 1.00 D                         10°
                                    1.00 to < 2.00 D                 5°
                                    2.00 to < 3.00 D                 3°
                                    3.00 to < 5.00 D                 2°
                                    5.00 to < 8.00 D                 1°

         Refine cylinder power
             •  Ask the subject to look at the lowest line on the visual acuity chart which can be
                read;
             • Switch to +/- 0.25 diopter cross-cylinder;
             • Align the ± 0.25 diopter cross-cylinder first with the positive axis and then
                with the negative axis coincident with the cylinder axis. Ask the subject which is
                better;
             • If the subject prefers the negative axis coincident with the cylinder axis,
                decrease the power of the cylinder in the trial frame by +0.25 diopter;
              • If a subject indicates a change that would introduce negative cylinder power,
                remove all cylinder power and continue testing for positive cylinder power at an
                axis 90º away from the previous axis;
             • If the subject prefers the positive axis coincident with the cylinder axis,
                increase the power of the trial frame by +0.25 diopter and retest;
             • Beginning with cylinder powers of 1.00 diopter or more, for each 0.5 diopter
                change in cylinder power, adjust the sphere power by 0.25 diopter of the
                opposite sign; this is done to maintain the spherical equivalent.

         Spherical refinement
         End the refraction by performing the spherical refinement step.
            • With the subject looking at the smallest line legible on the visual acuity chart,
               place a +0.37 spherical lens in front of the eye being tested. Ask the subject, “Is
               vision better, worse, or the same?”
            • If the subject responds that vision is made better or if there is no change,
               replace the spherical lens with one that is +0.25 more plus;
            • Continue to check with the +0.37 lens to see if the subject will accept more
                                                                                                34

```

### DOC-003 PDF page 36

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


                  plus by repeating the step above;
             •    When an additional +0.37 lens makes the subject’s vision worse, remove the +0.37
                  lens;
             •    Then hold a -0.37 spherical lens over the eye;
             •    If this -0.37 lens improves the subject’s vision, even by one letter, replace the
                  spherical lens in the trial frame by one that is -0.25 more minus;
             •    Continue presenting the -0.37 lens to see if there is any further improvement in
                  vision;
             •    When an additional -0.37 lens does not improve vision;
             •    Present the +0.37 lens, again asking “if vision is better, worse or the same?”
             •    If patient responds that vision is better or the same, repeat spherical refinement
                  testing as detailed above;
             •    If patient responds that vision is worse, testing is complete.
             •    Remember to always to end the refraction by checking with plus lenses.
         For Patients with Visual Acuity of 6/30-6/60 (20/100-20/200):

         Determine Sphere Power
             •    Ask patient to identify the orientation of the tumbling “E”s on the smallest
                  possible line that he/she can see on the Chart R;
             •    With the subject looking at the smallest line legible on the visual acuity chart,
                  place a +1.00 spherical lens in front of the right eye. Ask the subject, “Is vision
                  better, worse, or no change?”
             •    If the subject responds that vision is made better or is the same, replace the
                  spherical lens with one that is +1.00 more plus;
             •    Continue to check with the +1.00 lens to see if the subject will accept more
                  plus by repeating the step above;
             •    When an additional +1.00 lens makes the subject’s vision worse, remove the +1.00
                  lens
             •    Then hold a -1.00 spherical lens over the eye;
             •    If this -1.00 lens improves the subject’s vision, even by one letter, replace the
                  spherical lens in the trial frame by one that is -1.00 more minus;
             •    If the -1.00 spherical lens does not allow the patient to read more letters or if it
                  makes the vision worse, move on to cylindrical testing;
             •    Remember, if the patient reports that the -1.00 lens makes the vision better but if
                  s/he is unable to read more letters, do not change spherical lens by -1.00.
             •    NOTE: if visual acuity improves significantly during manifest refraction, the
                  examiner may need to change to trial lenses that are specified for the new level
                  of acuity for the remainder of the refraction. Please refer to the Trial Lens Guide
                  above.

         Determine and refine cylinder axis
         The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
         refraction.
             • Ask the subject to look at a letter on a line of Chart R which is one line larger
                 than the smallest line he/she could read (one above threshold);
             • If no cylinder is present in the beginning approximate refraction, place the
                 +/- 1.00 diopter cross-cylinder with the positive axis first at 90º and then at 180º,
                 asking if either position makes the letters clearer;
             • If the patient prefers either of these positions, place a +1.00 cylindrical lens in
                                                                                                    35

```

### DOC-003 PDF page 37

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures


                the trial frame at the preferred axis;
             •  If the patient did not prefer cylinder at axis 90° or 180°, position the cross
                cylinder with the positive axis first at 45° then 135°;
             • Ask if the patient prefers either of these positions;
             • If so, place a +1.00 cylinder lens in the trial frame at the preferred axis;
             • If the subject prefers none of the four positions, no further cylinder testing is
             required;
             • If cylinder is present in the beginning approximate refraction or if you have
                added +1.00 cylinder power in the above step, position the +/- 1.00 diopter
                cross-cylinder first with the positive axis 45º to the right of the cylinder axis
                (position one), and secondly with the positive axis at 45º to the left of the cylinder
                axis (position two). Ask the subject which position improves the vision (position one
                or position two?);
             • If the subject responds that neither position is better and if this was the first test
                of axis position, move the axis of the cylinder in the trial frame 15º to the right or
                left and repeat;
             • If the subject prefers one position to the other, rotate the cylinder toward the
                preferred positive axis of the cross-cylinder in the step sizes recommended (see
                Table below) and repeat. (If the subject states that one position of the cross-
                cylinder is no better than the other position, proceed to refining cylinder power).

                                Table: Axis step sizes for refinement of cylinder

                                    Cylinder Power           Axis Step Sizes
                                    < 1.00 D                         10°
                                    1.00 to < 2.00 D                 5°
                                    2.00 to < 3.00 D                 3°
                                    3.00 to < 5.00 D                 2°
                                    5.00 to < 8.00 D                 1°

         Refine cylinder power
             •    Ask the subject to look at the lowest line on the visual acuity chart which can be
                  read;
             •    Align the ± 1.00 diopter cross-cylinder first with the positive axis and then
                  with the negative axis coincident with the cylinder axis. Ask the subject which is
                  better;
             •    If the subject prefers the negative axis coincident with the cylinder axis,
                  decrease the power of the cylinder in the trial frame by +1.00 diopter;
             •    If a subject indicates a change that would introduce negative cylinder power,
                  remove all cylinder power and continue testing for positive cylinder power at an
                  axis 90º away from the previous axis;
             •    If the subject prefers the positive axis coincident with the cylinder axis,
                  increase the power of the trial frame by +1.00 diopter and retest;
             •    Beginning with cylinders of 1.00 diopter or more, for each 0.5 diopter change in
                  cylinder power, adjust the sphere by 0.25 diopter of the opposite sign; this is
                  done to maintain the spherical equivalent.

         Spherical refinement
         End the refraction by performing the spherical refinement step.
                                                                                                        36

```

### DOC-003 PDF page 38

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial       September 4, 2012
Manual of Operation and Procedures


              • With the subject looking at the smallest line legible on the visual acuity chart,
                place a +0.50 spherical lens in front of the eye being tested. Ask the subject, “Is
                vision better, worse, or the same?”
             • If the subject responds that vision is made better or if there is no change,
                replace the spherical lens with one that is +0.50 more plus;
             • Continue to check with the +0.50 lens to see if the subject will accept more
                plus by repeating the step above;
             • When an additional +0.50 lens makes the subject’s vision worse, remove the +0.50
                lens
             • Then hold a -0.50 spherical lens over the eye;
             • If this -0.50 lens improves the subject’s vision, even by one letter, replace the
                spherical lens in the trial frame by one that is -0.50 more minus;
             • Continue presenting the -0.50 lens to see if there is further improvement in vision;
             • When an additional -0.50 lens does not improve vision;
             • Show the patient the +0.50 lens, again asking “if vision is better, worse or the
                same?”
             • If patient responds that vision is better or the same, repeat spherical refinement
                testing as detailed above;
             • If patient responds that vision is worse, refraction testing is complete.
             • Remember to always to end the refraction by checking with plus power.

         For Patients with Visual Acuity < 6/60 (<20/200):

         Determine Sphere Power
         NOTE: If refraction cannot be performed at 4 meters, defined as missing 2 or more
         letters on the largest line, then the subject should be moved to 1 meter and the above
         refraction sequence followed. At 1 meter, a + 0.75 spherical lens is added to the
         beginning approximate refraction to adjust for the accommodative difference between 4
         and 1 meter.
              • Ask patient to identify the orientation of the tumbling “E”s on the smallest
                 possible line that he/she can see on the Chart R;
              • With the subject looking at the smallest line legible on the visual acuity chart,
                 place a +2.00 spherical lens in front of the right eye. Ask the subject, “Is it better,
                 worse, or no change?”
              • If the subject responds that vision is made better or is the same, replace the
                 spherical lens with one that is +2.00 more plus;
              • Continue to check with the +2.00 lens to see if the subject will accept more
                 plus by repeating the step above;
              • When an additional +2.00 lens makes the subject’s vision worse, remove the +2.00
                 lens
              • Then hold a -2.00 spherical lens over the eye;
              • If this -2.00 lens improves the subject’s vision, even by one letter, replace the
                 spherical lens in the trial frame by one that is -2.00 more minus;
              • If the -2.00 spherical lens does not allow the patient to read more letters or if it
                 makes the vision worse, move on to cylindrical testing;
              • Remember, if the patient reports that the -2.00 lens makes the vision better but if
                 s/he is unable to read more letters, do not change spherical lens by -2.00.
              • NOTE: if visual acuity improves significantly during manifest refraction, the
                 examiner may need to change to trial lenses that are specified for the new level
                 of acuity for the remainder of the refraction. Please refer to the Trial Lens Guide
                                                                                                       37

```

### DOC-003 PDF page 39

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures


                  above.

         Determine and refine cylinder axis
         The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
         refraction.
             • Ask the subject to look at a letter on a line of Chart R which is one line larger
                 than the smallest line he/she could read (one above threshold);
             • If no cylinder is present in the beginning approximate refraction, place the
                 +/- 1.00 diopter cross-cylinder with the positive axis first at 90º and then at 180º,
                 asking if either position makes the letters clearer;
             • If the patient prefers either of these positions, place a +1.00 cylindrical lens in
                 the trial frame at the preferred axis;
             • If the patient did not prefer cylinder at axis 90° or 180°, position the cross
                 cylinder with the positive axis first at 45° then 135°;
             • Ask if the patient prefers either of these positions;
             • If so, place a +1.00 cylinder lens in the trial frame at the preferred axis;
             • If the subject prefers none of the four positions, no further cylinder testing is
                 required.
             • If cylinder is present in the beginning approximate refraction or if you have
                 added +1.00 cylinder power in the above step, position the +/- 1.00 diopter
                 cross-cylinder first with the positive axis 45º to the right of the cylinder axis
                 (position one), and secondly with the positive axis at 45º to the left of the cylinder
                 axis (position two). Ask the subject which position improves the vision (position one
                 or position two?);
             • If the subject responds that neither position is better and if this was the first test
                 of axis position, move the axis of the cylinder in the trial frame 15º to the right or
                 left and repeat;
             • If the subject prefers one position to the other, rotate the cylinder toward the
                 preferred positive axis of the cross-cylinder in the step sizes recommended (see
                 table below) and repeat. (If the subject states that one position of the cross-
                 cylinder is no better than the other position, proceed to refining cylinder power).

                                Table: Axis step sizes for refinement of cylinder

                                    Cylinder Power           Axis Step Sizes
                                    < 1.00 D                         10°
                                    1.00 to < 2.00 D                 5°
                                    2.00 to < 3.00 D                 3°
                                    3.00 to < 5.00 D                 2°
                                    5.00 to < 8.00 D                 1°

         Refine cylinder power
             • Ask the subject to look at the lowest line on the visual acuity chart which can be
             read;
             • Align the ± 1.00 diopter cross-cylinder first with the positive axis and then
                with the negative axis coincident with the cylinder axis. Ask the subject which is
                better;
             • If the subject prefers the negative axis coincident with the cylinder axis,
                decrease the power of the cylinder in the trial frame by 1.00 diopter;

                                                                                                        38

```

### DOC-003 PDF page 40

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   September 4, 2012
Manual of Operation and Procedures


             •    If a subject indicates a change that would introduce negative cylinder power,
                  remove all cylinder power and continue testing for positive cylinder power at an
                  axis 90º away from the previous axis;
             •    If the subject prefers the positive axis coincident with the cylinder axis,
                  increase the power of the trial frame by +1.00 diopter and retest;
             •    Beginning with cylinders of 1.00 diopter or more, for each 0.5 diopter change in
                  cylinder power, adjust the sphere by 0.25 diopter of the opposite sign, this is
                  done to maintain the spherical equivalent.

         Spherical refinement
         End the refraction by performing the spherical refinement
         step.
             • With the subject looking at the smallest line legible on the visual acuity chart,
               place a +1.00 spherical lens in front of the eye being tested. Ask the subject, “Is
               vision better, worse, or the same?”
             • If the subject responds that vision is made better or if there is no change,
               replace the spherical lens with one that is +1.00 more plus;
             • Continue to check with the +1.00 lens to see if the subject will accept more
               plus by repeating the step above;
             • When an additional +1.00 lens makes the subject’s vision worse, remove the +1.00
               lens
             • Then hold a -1.00 spherical lens over the eye;
             • If this -1.00 lens improves the subject’s vision, even by one letter, replace the
               spherical lens in the trial frame by one that is -1.00 more minus;
             • Continue presenting the -1.00 lens to see if there is further improvement in vision;
             • When an additional -1.00 lens does not improve vision;
             • Present the +1.00 lens, again asking “if vision is better, worse or the same?”
             • If patient responds that vision is better or the same, repeat spherical refinement
               testing as detailed above;
             • If patient responds that vision is worse, testing is complete.
             • Remember to always to end the refraction by checking with plus power.

         Record the lens correction obtained during manifest refraction for the right eye on the
         appropriate examination forms in the section for visual acuity measurements (Section
         A.5). Then proceed to refraction of the left eye, following steps as outlined above.

    5.2.2. Visual acuity procedure

         Visual acuity measurement is necessary for the secondary outcome in this trial.
         Therefore, we have created a standardized method that aims to minimize any bias from
         either the refractionist or the patient. This has been adapted from the Visual Acuity
         protocols from the Age Related Eye Disease Study (AREDS 1999)32, and the Aravind
         Eye Hospital’s Practical Guide to Refraction33 and is similar to the method we are
         currently using at Aravind Eye Hospital and Proctor/UCSF for the NEI funded Steroids
         for Corneal Ulcers Trial and the Mycotic Ulcer Treatment Trial.

         Visual Acuity Charts
         The following equipment is used: a set of three charts, which are modified Bailey-Lovie
         charts, Charts 1, 2 and R (Precision Vision Chart 2305, 2305a and 2305b,
         respectively). Each chart consists of 14 lines of high-contrast “tumbling E’s”. There is

                                                                                                   39

```

### DOC-003 PDF page 41

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial     September 4, 2012
Manual of Operation and Procedures


         a geometric progression of letter size (and, thus, an arithmetic progression of the
         logarithm of minimum angle of resolution) from line to line.

         Chart 1 is for measuring aided visual acuity of the right eye and Chart 2 is to be used for
         measuring aided visual acuity of the left eye at all visits. Chart R will be used for
         obtaining all manifest subjective refractions.

         Visual Acuity Boxes
         The dimensions of the light box are 24 and 3/4 inches (62.9 cm) by 25 and 3/4 inches
         (65.4 cm) by 7 inches (17.8 cm). The box can be mounted on a wall or on a cylindrical
         stand. The stand is mounted on a five-pronged wheelbase, with each prong about 14
         inches (35.6 cm) long; two of the five wheels are lockable. When the box is mounted
         on the stand, its height can be varied. The light box should be mounted at a height
         such that the top of the third row of letters (0.8 logMAR, 45 letters, 20/125 Snellen) is
         49 +/- 2 inches (124.5 +/-5.1 cm) from the floor. The rear of the box provides storage
         space for the two charts not being used.

         Illumination
         The overhead room lights should be turned off during the visual acuity test. The
         box itself provides sufficient illumination for the examiner to record the test results.
         Additional light can have an adverse effect such as glare. With the box light off, not
         more than 15 foot-candles of light should fall on the center of the chart. The visual
         acuity light box is equipped with two 20- watt fluorescent tubes. Because the
         illumination of fluorescent tubes diminishes by 5 percent during the first 100 hours and
         by another 5 percent during the next 2,000 hours, new tubes should be kept "on" for
         about 4 days (approximately 96 hours, does not have to be continuous) before use. All
         tubes should be replaced once a year.

         Each tube is partially covered by a 14-inch (35.6 cm) fenestrated sleeve, open in the
         back, which serves as a baffle to reduce illumination. Each sleeve should be centered
         on the tube such that an equal length of tube (about 4 and 3/16 inches or 10.6 cm) is left
         uncovered to the right and left of the sleeve.

         4- and 1-Meter Visual Acuity Lanes
         A distance of 4 meters (13 feet and 1.5 inches, or 157.5 inches) is required between the
         subject's eyes and the visual acuity chart for the 4-meter test, and a distance of 1 meter
         (39 and 3/8 inches) is required for the 1-meter test. The room for visual acuity testing
         must have, in addition to the 4- meter lane, space for the visual acuity box (and possibly a
         stand) and space for the subject.
             • Wall-mounted box: In addition to the 4-meter lane, 7 inches (17.8 cm) must be
                allowed for the depth of the box plus space for the subject to sit or stand.
             • Stand-mounted box: In addition to the 4-meter lane, 13 inches (33 cm) must be
                 allowed for two of the stand's casters to touch the rear wall (or a line marked on
                 the floor when there is no wall) plus space for the subject to sit or stand.

         Marking the Distance

         4 Meters
              •   If the chair and visual acuity box are permanently affixed, distance
                                                                                                     40

```

### DOC-003 PDF page 42

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial         September 4, 2012
Manual of Operation and Procedures


                  measurements need to be made only once and no floor marks are needed to
                  ensure the correct distance.
              •   If the box is mounted on the wall but the subject's chair is not permanently affixed,
                  the 4- meter distance of the subject's eye from the chart must be marked clearly
                  and permanently.
              •   If the box is mounted on a movable stand, the 4-meter distance must be
                  marked clearly and permanently. The location and orientation of the box must be
                  rechecked each time a new chart is put in place or the box is touched. When the
                  stand touches the rear wall of the room, two of the five casters should touch the
                  wall.

         1 Meter
             •    The 1-meter distance is measured from the eye of the subject, who is seated
                  comfortably in a chair with his or her back firmly placed against the chair's back,
                  to the center of the second (for testing the left eye) or fourth letter (for testing the
                  right eye) of the third line of the chart. A stick, one meter long, should be used
                  to confirm the distance for each subject.

         Visual Acuity Procedure
             •    Visual acuity will be measured at each study visit.
             •    Visual acuity should be measured for each eye AFTER refraction. Visual acuity
                  should NOT be recorded during the refraction procedure.
             •    It is very important that the examiner is not aware of the patient’s clinical
                  records, in order to minimize bias. Therefore, the visual acuity examiner will not
                  have access to the patient’s previous clinical examination or treatment results.
             •    Visual acuity is tested separately for each eye (one eye at a time). The patient’s
                  untested eye will be completely covered with a patch, to block out all light from
                  entering this eye. The examiner must constantly ensure that this eye remains
                  occluded at all times.
             •    The patient is instructed to read each letter on the chart starting with the largest
                  line, at the 4-meter distance.
             •    The patient will show the orientation of the tumbling “E” with the hand that they
                  are not using to occlude the untested eye. If the patient cannot identify the
                  orientation of a letter, they are encouraged to guess. Only one response is
                  allowed per letter.
             •    The examiner must ensure that the patient does not squint (creating a pin-hole
                  effect) or lean forward (reducing the distance to the chart).
             •    Once a patient has given a response for a letter and has moved on to provide a
                  response for the next letter, any corrections of previous response will not be
                  accepted.
             •    However, if the patient has given a response for a letter and has not yet
                  moved on to provide a response for the next letter, a correction of the previous
                  response is accepted.
             •    If the subject gives two possible responses for a letter, tell the patient to commit
                  to one answer. The examiner CANNOT, at anytime, give the patient any
                  indication as to whether a response is correct or incorrect.
             •    If 3 or fewer letters are identified correctly on any row from Row 3 or below,
                  STOP testing on that row.
             •    In the case that the patient reads less than 10 letters at 4 meters, move the
                  patient or the chart so that there is a distance between the two of 1 meter.
                                                                                                    41

```

### DOC-003 PDF page 43

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


             •    Visual acuity will then be retested at this 1 meter distance.
             •    Only the first 6 rows of letters need to be read at 1 meter.
             •    If less than 10 letters are read at 1 meter, then the examiner must proceed to
                  Low Vision Testing, starting with Count Fingers testing. If the patient does not
                  adequately Count Fingers (see below), proceed to Hand Motion. If the patient
                  does not adequately recognize Hand Motion (see below), then proceed to Light
                  Perception.

         Testing of Count Fingers Vision
         In testing for count fingers vision, the examiner’s hand presenting 1, 2, or 5 fingers is held
         steady at a distance of 1 meter directly in front of the eye being examined. The fellow
         eye is completely occluded with a patch. Refractive correction should not be used.
         A light should be shown directly on the hand from behind the subject and room
         lights should be turned on. The examiner’s fingers should be presented in random
         order and repeated 5 times. Eccentric viewing should be encouraged. If the subject
         correctly identifies three of the five presentations, then count fingers visions is noted. If
         not, then the subject must be tested for hand motion vision.

         Testing of Hand Motion Vision
         The examiner’s hand with all fingers spread out should be extended ½ meter directly in
         front of the eye being examined. The fellow eye should be occluded with a patch.
         Refractive correction should not be used. A light should be shone directly on the hand
         from behind the subject and room lights should be turned on. The examiner’s hand
         should be moved in an up-and-down direction (vertically) or in a side-to-side direction
         (horizontally) at a constant speed of approximately one back and forth presentation per
         second. The subject is instructed that the examiner’s hand will be presented and
         they will have to respond to the question: “What am I doing with my hand?” This
         should be repeated five times. Four out of five correct responses indicate that hand
         motions visions is present. If the subject does not correctly identify four out of five, then
         you must test for light perception.

         Testing for Light Perception
         The indirect ophthalmoscope is used as the light source for testing light perception.
         Room lights should be off.       The opposite eye must be completely patched. No
         correction should be used. From a distance of ½ meter with the light source turned up
         to maximum intensity, the light from the indirect ophthalmoscope is directed into the
         subject’s eye four times. The subject is asked to respond when the light is “on”. Light
         Perception is recorded if the examiner is convinced the subject sees the light.
         Otherwise, the vision should be recorded as “No Light Perception”.

         Scoring Best Corrected Visual Acuity
         On the Visual Acuity Forms, the examiner will circle all letters read correctly. Letters
         read incorrectly or not read at all will be left unmarked. At the end of each row of
         letters, the examiner will write down the total number of letters read correctly on the line
         provided. If visual acuity was not tested at 1 meter, the examiner will indicate this on the
         form.
         After each measurement of visual acuity, the biostatistician will calculate the score for
         the visit. The visual acuity score is defined as follows:
             • If 10 or more letters of the first line are read correctly at 4 meters, the 4 meter
                                                                                                 42

```

### DOC-003 PDF page 44

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial       September 4, 2012
Manual of Operation and Procedures


                  visual acuity score is equal to the number of letters read correctly at 4 meters plus
                  30.
             •    If 3 or fewer letters of the largest line are read correctly at 4 meters, the visual
                  acuity score is equal to the number of letters read correctly at 1 meter.
             •    If 3 or fewer letters are read at 1 meter, then low vision testing must be
                  performed. (This result, count fingers, hand motion, light perception, or no light
                  perception, will be used for the analysis by converting into a logMAR score
                  according to Visual Acuity Calculation Table).

         The highest attainable 4-meter visual acuity score is 100.


         The Snellen equivalent, defined as the Snellen ratio corresponding to the most difficult
         line for which the subject read at least 4 of 5 letters correctly, will also be entered by the
         examiner on the 4-meter Visual Acuity Form (Section A.5).
         The data entry staff will enter the number correct on each row at 4 meters, and if
         applicable, 1 meter and low vision testing results (They will not enter which letters the
         examiner circled, i.e., which letters the patient identified correctly.). The biostatistician
         will calculate the visual acuity score and double check the data entered by the examiner
         and data entry staff by reviewing the original forms.

         5.2.3.    Visual acuity training and certification

         The goal of the certification process is to standardize methodology for refraction and
         visual acuity measurement. All visual function examinations must be performed by
         study-certified technicians. The principal investigator at each site is responsible for
         ensuring that the appropriate personnel are identified, trained and certified. A qualified
         visual function examiner (SL) from the Clinical Coordinating Center (Proctor Foundation)
         will certify the rooms and technicians at each site.

         Technicians are expected to perform the refraction and visual acuity tests on at least
         one and possibly more non-study subjects according to protocol requirements. The
         examiner will determine whether or not the candidate executes the study protocol
         accurately for each procedure. A checklist (Visual Acuity/Refraction Certification Form,
         Section B.1) containing required procedures will be used to facilitate this process.

         Room certification will be performed and recorded (Room Certification Form, section
         B.2) to ensure that all study rooms meet illumination, equipment, and distance
         requirements. Logs should be kept to document dates of light box bulb replacement.

         Certification is valid for a period 18 months (± 2 months) from the date of
         certification. The process should begin as soon as possible, as technicians must be
         certified before the first study subject is seen. A minimum of two certified technicians
         are required at each site.

         The visual acuity measuring schedule may be found on the Study Forms Completion
         Schedule.

    5.3. Ophthalmic procedures

         5.3.1. Grading inflammation
                                                                                                       43

```

### DOC-003 PDF page 45

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                 September 4, 2012
Manual of Operation and Procedures



    The study ophthalmologist at each site will be required to perform an eye examination at
    each study visit. This examination should be similar to that performed in the routine care of
    uveitis patients. Several components will be assessed in detail per study protocol. The
    grading schemes to be used for these assessments are adapted from the Standardization of
    Uveitis Nomenclature (SUN) Working Group.2
    Anterior Chamber Cells
    SUN Working Group Grading Scheme for Anterior Chamber Cells
                   Grade                              Cells in Field*
                      0                                     <1
                    0.5+                                    1-5
                     1+                                    6-15
                     2+                                   16-25
                     3+                                   26-50
                     4+                                    >50
  *Field size is a 1mm by 1mm slit lamp beam. Grading should be conducted in a completely dark room.

    Anterior Chamber Flare
    Anterior Chamber Flare will be assessed by slit lamp exam but will not be part of our study
    criteria for controlled inflammation.

    SUN Working Group Grading Scheme for Anterior Chamber Flare
                   Grade                                   Description
                     0                                        None
                    1+                                        Faint
                    2+                        Moderate (iris and lens details clear)
                    3+                         Marked (iris and lens details hazy)
                    4+                          Intense (fibrin or plastic aqueous)
   *Adapted from: Hogan MJ, Kimura SJ, Thygeson P. Signs and symptoms of uveitis: I. Anterior
    Uveitis. AM J Ophthal 1964;47:155-170; Grading should be conducted in a completely dark room

    Vitreous Cells
    There is currently no accepted standard for grading vitreous cells, which will not be part of
    our study criteria for controlled inflammation. However, we will collect this information using
    the grading scheme below, which is adapted from the MUST trial:

                        Grade                                              Cells in Field*
                           0                                                 No cells
                         0.5+                                               0 to 5 cells
                          1+                                                6-10 cells
                          2+                                                11-20 cells
                          3+                                                21-50 cells
                          4+                                                    >50
  *Field size is a 1mm by 0.5mm beam; Grading should be conducted in a completely dark room; These
  cells are graded by slit lamp exam after dilation.

    Vitreous Haze
    Vitreous haze will be assessed using an indirect ophthalmoscope set at mid-power and a
    20D lens. Fundus examination will be done with the last view being the area around the
                                                                                                                 44

```

### DOC-003 PDF page 46

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                September 4, 2012
Manual of Operation and Procedures


    optic disc. The examiner should then compare this view to the photograph (Figure 1) and
    determine the level of vitreous haze. The National Eye Institute System for grading
    vitreous haze will be used for all primary and secondary outcome measures. Additionally,
    vitreous haze will be assessed on the 9-point grading scale recently published by Davis et
    al. An exploratory analysis will correlate measurements from the NEI and Davis scales.
    Clinical measurements of vitreous haze will also be compared to objective assessments
    done by grading of fundus photos.
                        Figure 1: National Eye Institute system for grading vitreous haze

                           Grade                                                Description
                              0                                                    Clear
                            0.5+                                   Slight blurring of optic disc margin
                                                               Normal striations and reflex of nerve fiber
                                                                       layer cannot be visualized
                             1+                              Opacities without obscuration of retinal details
                             2+                                Few opacities resulting in mild blurring of
                                                               details of optic nerve and retinal vessels
                             3+                                  Optic nerve head and retinal vessels
                                                                 significantly blurred but still visible
                             4+                               Dense opacity obscuring optic nerve head
   *Grading should be conducted in a completely dark room.




    From Nussenblatt RB, Palestine AG, Chan CC, Roberge F. Standardization of vitreal inflammatory activity in
    intermediate and poseterior uveitis. Ophthalmology 1985; 92: 467-471.




                                                                                                                 45

```

### DOC-003 PDF page 47

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                  September 4, 2012
Manual of Operation and Procedures




                        Figure 2: Davis et al 9-point system for grading vitreous haze




    From Davis JL, Madow B, Cornett J, et al. Scale for photographic grading of vitreous haze in uveitis. Am J
    Ophthalmol;150:637-641 e1.

    Slit lamp examination and dilated funduscopic exam are important parts of our study:
    assessments of anterior chamber cells and vitreous haze will determine the patient’s course
    of treatment. All of our study physicians are fellowship-trained uveitis specialists who have
    participated in prior uveitis studies.

         5.3.2. Inter-observer variation of ocular inflammation

    At the 6th month study visit, the 12th month study visit, or at treatment failure (whichever is
    earlier), inter-observer agreement on slit lamp observations and funduscopic exam will be
    assessed. Coordinators will arrange for two certified study physicians to measure anterior
    chamber cells, anterior chamber flare, vitreous cells, and vitreous haze at the Month 6 and
    12 visit or at declaration of treatment failure. The inter- observer variation will be reported.
    The primary study ophthalmologist’s measurements will be used for primary analysis

    5.4. Optical coherence tomography

    We will be using spectral-domain optical coherence tomography (SD-OCT) in this study to
    monitor the effects of treatment by measuring macular thickness and changes in macular
    thickness. We will be utilizing the Heidelberg Spectralis SD-OCT unit and the Zeiss Cirrus
    SD-OCT unit for all study assessments. Each site must choose either Heidelberg Spectralis
    or Zeiss Cirrus at the time of study initiation and continue to use that same scanner for all
    patients the duration of the study.

         5.4.1. Required patient assessments—Heidelberg Spectralis

         For our study, one of each of the following scans is required for each eye:

              •   20° x 20° High Speed Volume scan centered on the macula

                                                                                                                  46

```

### DOC-003 PDF page 48

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures


              •   7 Line Preset scan centered on the macula


         5.4.2. Scan procedures—Heidelberg Spectralis
         Creating Patient Files
         For Baseline Scans:
         To ensure patient confidentiality, patient ID only will be used. Patient name and other
         identifying information will not be used on the scans. Therefore, when setting up the
         patient file, please follow the instructions below:
             • Click on the red forward facing icon in the toolbar
             • In the Last Name field, enter study name: FAST
             • In the First Name field, enter patient’s unique study ID number
             • For Date of Birth, always use 1/1/2000
             • Click proper field in gender section
             • In Patient ID field enter patient’s unique study ID number, example: “1-APR-211”
                 For Follow-up Scans:
             • Click on the side facing icon in the toolbar
             • Ensure that a scan from the baseline visit has been set as a reference scan:
                  •      Identify the scan from the baseline visit that you would like to set as reference

                  •      Right click on the scan
                  •      Select “Progression”
                  •      Select “Set Reference”
                  •      This setting will be confirmed by a red icon appearing on the bottom left
                         corner of the selected scan

         Procedures for Obtaining Scans
         General Guidelines
            • Scans may be obtained if the patient’s pupils are not dilated. However, pupil
               dilation prior to obtaining scans is encouraged
            • Clean chin rest and forehead rests
            • Adjust table and chin rest height to ensure patient comfort
            • Make sure that patient is aligned straight; slight face turns to the left or
               right may decrease scan quality

             Click on the Preset “Dense” scan icon on the screen to obtain the 20° x 20° volume
             scan. Please make sure that the scan will have the following parameters:
                     o 20° x 20°
                     o 49 sections
                     o 16 frames (ART)

             •    Pull the camera all the way back
             •    Move the instrument toward the patient slowly, taking care not to alarm patient
                  and to not touch the patient’s eyes or eyelashes with the instrument
             •    Ask patient to fixate on the blue light on the inside of the machine
             •    Remind patient not to follow the movement of the red scan lines
             •    If patient is having trouble focusing on fixation light, you may need to help the
                  patient direct his/her gaze by using external fixation targets
             •    Focus in on the circular black and white retinal reflex
             •    Move the camera forward so that the fundus image comes into view and fills the
                                                                                                        47

```

### DOC-003 PDF page 49

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial     September 4, 2012
Manual of Operation and Procedures


                  screen
             •    Use the focusing knob to obtain maximum brightness and clarity of the image
             •    Ensure that the image is maintained in the upper third of the screen
             •    Click “Acquire”
             •    Repeat for next eye

             Click on the “7 Line” Preset Scan icon
             This scan will have the following parameters:
                     o 30° x 5°
                     o 7 sections
                     o 25 frames (ART)

             •    Focus image as described above
             •    Click “Acquire”
             •    Repeat for next eye
             •    Please review scans for completeness and quality. A good quality scan
                  should have a score of at least 20. Please repeat any scans that are not
                  complete or of poor quality.

         5.4.3. Obtaining retinal thickness data—Heidelberg Spectralis

             •    After closing the acquisition window, double click on the volume scan.
             •    Select “Thickness Map” tab
             •    Record central subfield thickness on data sheet
             •    Print out copy of scan for patient file

         Be sure to complete analysis of data and record information on data collection form as
         soon as possible. This will ensure that the treating physician will be able to use the
         SD-OCT results in real time to determine if macular edema is present or not.


         5.4.4. Saving/Exporting data—Heidelberg Spectralis
       Saving Data

             •    All scans should be saved and archived at each study site on the Heidleberg SD-
                  OCTunit.
             •    After obtaining scans, right click on each scan icon and choose “Export as E2E”
             •    Save the “E2E” data onto a removable hard drive separate from the main unit: this
                  raw data may be requested from each site at a later date.

       Exporting Data
           • One image of the central macula from each 20º x 20º scan should be emailed to the
               Proctor Foundation for review.
           • With volume scan displayed, and with the central macular scan highlighted, click
               on “Image” tab on toolbar
           • Select “Export as Picture”
           • Export and save image on a desktop folder or onto a USB drive
           • Save images as “jpg” files
           • Also create a PDF file of the “Thickness Map” described above in section 5.4.3
           • Place these images of both eyes in a file
                                                                                                     48

```

### DOC-003 PDF page 50

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial    September 4, 2012
Manual of Operation and Procedures


             •    Label the file with patient’s unique study ID, visit number, and date of visit,
                  example: “1-APR-211-BL-10AUG2012”
             •    Email images for each patient to Proctor Foundation:
             •    Repeat above steps for scan number 4 of the 7 Line Preset Scan
             •    If images cannot be obtained or are of poor quality, please provide comments in
                  email

         5.4.5. Required patient assessments—Zeiss Cirrus
               For our study, one of each of the following scans is required for each eye:
                 • Macular Cube Scan
                 • 5 Line Raster scan centered on the macula

         5.4.6. Scan procedures—Zeiss Cirrus
         Creating Patient Files
         To ensure patient confidentiality, patient ID only will be used. Patient name and other
         identifying information will not be used on the scans. Therefore, when setting up the
         patient file, please follow the instructions below:
             • In the Last Name field, enter study name: FAST
             • In the First Name field, enter patient’s unique study number
             • For Date of Birth, always use 1/1/2000
             • Click proper field in gender section
             • In Patient ID field enter patient’s unique study ID number, example: “1-APR-211”

         Procedures for Obtaining Scans
         General Guidelines
            • Scans may be obtained if the patient’s pupils are not dilated. However, pupil
               dilation prior to obtaining scans is encouraged
            • Clean chin rest and forehead rests
            • Adjust table and chin rest height to ensure patient comfort
            • Make sure that patient is aligned straight; slight face turns to the left or
               right may decrease scan quality
            • Ensure that the camera is pulled all the way back
            • Move the instrument toward the patient slowly, taking care not to alarm patient
               and to not touch the patient’s eyes or eyelashes with the instrument

             Select “Scan Macular Cube 512x218” default in the upper panel of the Acquire
             screen
             • In the Iris Viewport, center the scan beam through the pupil by clicking on the pupil
                 center or using the X-Y controls
             • Focus the iris image using the chinrest arrows
             • Center the fundus image in the Fundus Viewport
             • Click on “Auto Focus”
             • Use small arrows to focus manually
             • Click “Optimize”
             • Ask patient to blink right before image capture
             • Click “Capture”
             • Review scan; if acceptable, click “Save”
             • If not acceptable, click “Try Again”

             Repeat above steps to acquire “5 Line Raster” default Scan
                                                                                                    49

```

### DOC-003 PDF page 51

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        September 4, 2012
Manual of Operation and Procedures



             •    If patient is having trouble focusing on fixation light, you may need to help the
                  patient direct his/her gaze by using external fixation targets
             •    Ensure that the scan image is maintained in the upper half of the screen
             •    Please review scans for completeness and quality. Signal strength should be
                  at least 5 or higher. Please repeat any scans that are not complete or of poor
                  quality.

         5.4.7. Obtaining retinal thickness data—Zeiss Cirrus

             •    Obtain Macular Thickness analysis
             •    Obtain 5 Line Raster analysis
             •    Record central subfield thickness on data sheet

         Be sure to complete analysis of data and record information on data collection form as
         soon as possible. This will ensure that the treating physician will be able to use the
         SD-OCT results in real time to determine if macular edema is present or not.


         5.4.8. Saving/Exporting data—Zeiss Cirrus

             •    All scans should be saved and archived at each study site on the Zeiss Cirrus SD-
                  OCT unit. This raw data should also be saved onto a separate removable hard
                  drive so that it is available for export and review at a later date.
             •    The following images should be emailed to the Proctor Foundation for review.
                      One image/screen shot of macular cube printout for each eye
                      One image/screen shot of 5 line raster printout for each eye
                      Images can be sent as “jpg”, “tiff” or “pdf” files
                      Images should be sent to:
                      If images cannot be obtained or are of poor quality, please provide
                        comments in email

         5.4.9. OCT operator qualifications

    Prior to the study start date, at least 2 personnel who will be responsible for obtaining SD-
    OCT scans at each site should be identified. These individuals should have prior
    experience with operation of either the Heidelberg SD-OCT or Zeiss Cirrus SD-OCT
    instrument for routine clinic purposes. Dr. Salena Lee will go to each site before that start of
    the trial to meet with these technicians to review all required OCT procedures specified in
    our protocol. OCT operators must be able to demonstrate ability to obtain scans as well as
    knowledge of the study protocol.

    5.5 Fundus Photography

    Color fundus photography will be performed at baseline, 6 months, 12 months or treatment
    failure. Photos will include fundus reflex images and non-stereoscopic fundus images.
    Vitreous haze will be graded according to the NEI and Davis scales by masked graders.
    Photographers will need to be certified by the Uveitis Photograph Reading Center prior to
    obtaining photos four our study. Please see UPRC manual (Appendix C) for instructions on
    certification and obtaining study photos.


                                                                                                        50

```

### DOC-003 PDF page 52

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial       September 4, 2012
Manual of Operation and Procedures



     5.6. Laboratory measurements

     Hematology and serum chemistry will be monitored in all patients prior to enrollment and
     throughout participation in the study. Each of the participating sites has an accredited onsite
     laboratory where all blood draws and laboratory measurements will be performed. The
     following will be measured and recorded on the Laboratory Report Form (Section A.7) for
     each:

     Hematology

     • Hemoglobin and/or hematocrit
     • Platelet count
     • White blood cell count (WBC)
       • % neutrophils; % lymphocytes
     Serum Chemistry

     •    SGOT (AST)
     •    SGPT (ALT)
     •    Creatinine
     •    Serum or urine for pregnancy test

     Laboratory measurements used for baseline visits should be collected within 1 4 days of
     the official visit date. Those used for follow-up visits may be collected at any time within the
     study visit window.

     All abnormal values will be reported on the Adverse Event Checklist (Section A.9) and
     monitored for resolution on the Adverse Event Log. Abnormalities which result in a non-
     serious adverse event (i.e. AST or ALT increasing to twice the upper limit of normal) will
     result in immediate stopping of study medications. As these abnormalities are often
     reversible, patients will be allowed one month to regain eligibility. If the lab results have
     returned to normal within one month, patients may be re- administered the study drug
     according to protocol. Labs can be checked prior to one month, and if normal, treatment
     can resume. Otherwise, treatment failure will be declared and patients will exit the study and
     be treated according to the best medical judgment of their physician. Note that treatment
     failure may be declared due to lack of efficacy if a patient’s inflammation becomes
     uncontrolled during this one month period if it occurs at the 6 month visit.

     Abnormalities which meet the designated threshold of a severe adverse event (SAE) will
     result in immediate stopping of study medications, and should be reported on the Serious
     Adverse Event Narrative form (Section A.11). Patients will then exit the study and be treated
     according to the best medical judgment of their physician.

6.       Adverse events
     6.1. Non-serious adverse event (AE)

     Non-serious adverse events may include any unfavorable medical occurrences in patients
     who have ever received study medication, regardless of any causal relationship with
     treatment. Examples* may include:
         • Increased intraocular pressure (>24 mm Hg)
         • Abnormal lab findings (> 2 times but < 5 times the upper limit of normal AST or
                                                                                                        51

```

### DOC-003 PDF page 53

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial       September 4, 2012
 Manual of Operation and Procedures


              ALT, rise in creatinine to ≥ 1.5 to < 2 mg/dL, reduction of white blood cell count to
              below 2.5)
          •   Concurrent accident or illness
          •   Increase in the frequency and severity of symptoms of a pre-existing condition
          •   Side effects such as gastrointestinal upset, nausea, vomiting, fatigue

     *For additional details, please see the adverse event checklist
     (Section A.9)

     6.2. Serious adverse event (SAE)

     Serious adverse events include any medical occurrence that results in the following
     outcomes, or any other adverse event classified as severe*:
        • ≥ 5 times the upper limit of normal AST or ALT
        • Death
        • Non-elective surgery or hospitalization for any reason
        • Myocardial infarction or stroke
        • Life-threatening adverse drug experience
        • Persistent or significant disability or incapacity

     *For additional details, please see the adverse event checklist
     (Section A.9)

     6.3. Adverse event reporting

     Non-serious and serious adverse events will be recorded at each study visit on the
     appropriate form (Adverse Event Checklist and Log, Sections A.9-A.10). An adverse event
     log will be maintained for each patient to record the onset and resolution of any adverse
     events.

     In case of a Serious Adverse Event (SAE), the Serious Adverse Event Narrative Form
     (Section A.11) will be completed by the Investigator and submitted to the Medical Monitor,
     Dr. Todd Margolis (                           ) within 24 hours of the SAE. Information
     recorded on this form will include the nature of the event, date of onset, date of resolution,
     date of notification to Medical Monitor, and action taken. The form will be reviewed, signed
     and forwarded to the DSMC by the Medical Monitor. Any significant study drug-related
     adverse events will be reported by the coordinating center to the FDA and CHR office as
     appropriate.


     6.4. Patient death

     Any patient death that occurs during the study will be reported by the study center's
     Study Coordinator to the Medical Monitor within 24 hours. The study arm of any deceased
     patient will be made available to the DSMC by the DCC if appropriate.

7.   Data collection and management

 This section discusses how the data will be collected from the different Study Centers, entered
 into the computer database and stored, and transferred to the Data Analysis Committee under
 the supervision of the Data Coordinating Center (DCC). The data management plan described
                                                                                                        52

```

### DOC-003 PDF page 54

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial    September 4, 2012
Manual of Operation and Procedures


below is similar to what we are already using for our NEI-funded SCUT and MUTT clinical trials,
which enroll patients at Proctor/UCSF, Dartmouth, and at Aravind Eye Hospital in India.
Proctor/UCSF is the clinical and data coordinating center for these trials.

    7.1. Data collection forms

    The data collection forms are derived from the Steroids for Corneal Ulcers Trial, the Mycotic
    Ulcer Treatment Trial pilot and main trial, and the FAST pilot trial initiated as a precursor to
    this proposed study. These forms have been extensively field-tested by UCSF and Aravind
    investigators.

    Study personnel at each site will be given specific training for each form for which they
    will be responsible. Paper forms for each patient will be completed by study personnel
    (study physicians, refractionists, etc.) within 48 hours following the study visit at each study
    site. Questions which arise during the use of the forms will be communicated with the Data
    Coordinating Center at Proctor, and the results and answers will be communicated to all
    sites. Teleconferences and site visits will be held periodically for all users of the forms to
    review procedures and address questions.

    7.2. Data review

    Before data entry, the forms will be reviewed and cross-checked for consistency and
    completeness by the study coordinator within 24 hours of completing the form. If the forms
    are not filled out completely, the study coordinator will contact the person responsible for
    completing the form to provide the missing data, or clarify any inconsistent data. The study
    coordinator or investigators who filled out the form are the only people who are authorized to
    add missing data or make any changes to the study forms. All changes should be made
    with a red ink pen, and then signed and dated. The computer data entry forms contain
    two fields at the end, in which the data entry personnel will indicate whether or not
    there was any “red ink” (corrections to the paper form), and which fields contained
    corrections; this will be used in quality assurance monitoring. Further investigation may be
    conducted if certain fields or personnel are associated with a higher rate of paper form errors.
    7.3. Data entry

    Once the completed study forms have been reviewed and approved by the study
    coordinator, the study coordinator will enter the first round of data entry, before giving the
    forms to the data entry operators at each site, for them to complete the second entry. All
    data will be entered into the official electronic research data capture service at UCSF;
    REDCap.

    Our goal is for both data entries to occur within two working days of form review and
    approval by the study coordinator (and within 3 working days of form completion) in order
    to prevent the accumulation of un-entered forms. The database program contains an entry
    module for each form, prompting the user to enter the data in the same order as the
    form and clearly indicating each question. All data will be double-entered at each site, by the
    study coordinators and independent data entry operators to ensure accuracy.

         7.3.1. Data entry errors

    At each site, a data analyst will compare double-entered study data using the automated

                                                                                                    53

```

### DOC-003 PDF page 55

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


    feature in REDCap (with a goal of completing within 2 days of data entry completion).
    Wherever there is a mismatch, an error file will be generated with relevant data such as the
    form, field name, visit name, and data for which discrepancy is found. The data analyst will
    then contact the data entry operators to verify the forms and re-enter the data. Discrepancies
    and missing values will be assessed by the data analyst, and resolved by queries sent to the
    study coordinator and appropriate observers (clinician, refractionist, etc). A logfile will
    preserve the date and time of any changes, together with who entered the changes.

         7.3.2. Data consistency and validity

    A database data quality assessment program will be created in R programming software to
    help prevent inconsistencies or invalid data. The database program will check for the
    following errors: (1) improper entry of the patient ID based on the checksum, (2) data fields
    that are out of range, (3) inconsistent or illogical entries, (4) incompleteness, and (5)
    numerical values that are far outside the range of those previously entered. The software will
    create an error file with relevant data such as the form identification, field names and the
    data. Automated checks will be made to ensure consistency and that each variable in the
    analysis set has in-range values (protecting against negative ages, spelling errors in
    categorical factors, and similar errors). The DCC will conduct regular checks of the data at
    each site and will contact the study coordinator about any errors in order to resolve the
    inconsistencies and have the data entry operators enter the correct data.

         7.3.3. Data preparation and cleaning

    Data sets for analysis will be produced in Microsoft Excel® worksheets (downloaded from
    the REDCap system) containing a single header line whose variable names match the
    REDCap database. Each analysis set will be in the form of a rectangular table in which each
    column corresponds to a single variable and each row to an observation. All missing values
    will be coded explicitly using the string “NA” (as used in the R software). Codes for
    categorical variables (such as 1 for male, and 2 for female) will be avoided in favor of self-
    documenting character strings (such as Male, Female) whenever possible.

    A detailed codebook will be prepared, containing for each variable, (a) the form from which
    the variable derived, (b) the text of the question, (c) all possible values for the variable, and
    (d) summary statistics for the variable. Note that all codes and character strings that
    represent categorical factors will be clearly defined in the codebook. Units for each
    continuous variable (e.g. logMAR) will be unambiguously indicated for each variable. Each
    release of the analysis set will be accompanied by the corresponding version of the
    codebook. Version numbering with dates will be strictly observed.

         7.3.4. Monitoring

    We will maintain a record of (1) changes to the initial entries on database forms, and (2)
    changes made to all entered data. Database errors include (a) missing information, (b)
    erroneous information that was initially entered, and (c) errors arising from difficulties with the
    forms themselves. Weekly quality assurance reports will summarize the number of each of
    these. Most importantly, we will closely monitor the waiting time between the collection of the
    initial form and the entry of the data to ensure that this time is less than 48 hours. If entry
    times exceed 48 hours, then this will trigger a response, which may include investigation,
    retraining, and even reassignment.


                                                                                                      54

```

### DOC-003 PDF page 56

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial     September 4, 2012
Manual of Operation and Procedures


    7.4. Data analysis

    Following data checks by the data analyst, the Data Analysis Committee will be responsible
    for analyzing the data. It will merge the unmasked data with the randomization list, perform
    statistical analyses and prepare reports.


    Standard report-generation software included with the R statistical and data analysis
    package will be used to ensure consistency of the codebook and analysis set at all times.

    Data monitoring reports will be prepared based on analysis data sets. These will be
    prepared using report-generation software. Monitoring reports will include (a) recruitment
    reports for each center, (b) compliance reports, (c) retention reports, and (d) data quality
    reports. These will be reviewed by the DCC on a monthly basis, and communicated to the
    study sites on a monthly basis.

    7.5. Data storage and security

    Paper forms will be maintained in locked file cabinets in locked rooms only accessible to
    research staff at each study site.

    All electronic storage, both at the Aravind sites and at Proctor and Casey, will be subject to
    standard security procedures in compliance with established enterprise information security
    standards. Each computer will be hardware-firewalled and will not be accessible outside
    the Local Area Network. Hard-disk encryption will be used for each machine, and the
    machine will not be accessible without a network account and password. Only one
    individual at each site will have password access to the machine; new accounts may be
    provided by the local network administrator only with the approval of the DCC. Accounts will
    be immediately deactivated for data entry or other personnel who leave the study. The
    computer used for data entry and storage will be kept in a physically locked room, and
    only authorized study personnel will be able to access this machine. All individuals who
    access the server room will be logged as to time and date. At each center, the complete
    database (including all data tables as well as change logs) will be backed up weekly on the
    server and weekly on a CD/DVD, which will be kept at a safe, locked cabinet. Temperature
    logs will be maintained for the server room and reported.

    The database at the DCC will be stored on a SQL server located at 95 Kirkham Street, San
    Francisco, CA and three sets of backup copies on CD/DVD will be kept. The server is
    hardware-firewalled and also uses hard-disk encryption; it is inaccessible outside the Proctor
    network and cannot be physically accessed by anyone other than the network administrator.
    Other visitors must be accompanied by an information security professional and the visit will
    be logged. All data will be protected with passwords and the computer/server on which the
    data is stored and the backup copies on CD/DVD will be located in a lock-secured facility.
    Each back-up file will be archived offsite. In the event of disruption due to unforeseen
    circumstances, all materials needed to continue will be available from the offsite archive.

 8. Quality control

    With the help of the Data Coordinating Center and the Data Analysis Committee, the
    Clinical Coordinating Center will evaluate the quality of study activities (clinical examination,
    treatment compliance, refraction, etc.).

                                                                                                     55

```

### DOC-003 PDF page 57

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
 Manual of Operation and Procedures


     8.1. Medication storage and expiry

     Study medications will be stored at room temperature. The expiration dates of the treatment
     kits will be regularly monitored and all expired study medicine will be discarded appropriately.

     8.2. Periodic reports

     The Study Coordinators will send weekly reports on the number of eligible patients
     screened, the number of patients enrolled, reasons for ineligibility, and the number of
     patients who have come back for follow-up visits to the Clinical Coordinating Center. This
     will be used to monitor the enrollment/follow-up progress and any protocol violation in
     enrollment. The CCC will send bi- weekly reports to all investigators with a summary
     of overall enrollment and breakdown of enrollment at each site.

     When a site visit or training/certification is conducted at a study site, a report will be
     prepared and sent to the Executive Committee.

     The minutes of the DSMC meeting will be circulated electronically among the investigators
     and the members of the DSMC after each meeting.
     8.3. Data management, security and quality assurance

     See Section 7.

     8.4. Monitoring compliance

     Patients will be asked to record missed doses in individual treatment diaries and to bring
     them with their medication to each follow-up visit. The study coordinator will collect details of
     the number of doses missed by the patient and recorded these in the medication adherence
     log. In addition study coordinators will conduct pill counts at each visit.

     8.5. Certification

     For training and certification process, see Sections 5.2.3.

     8.6. Data audits

     Samples of data forms will be audited at each site to ensure consistency between
     the source documents and data entry. Patient charts will also be reviewed two times a year
     to confirm adherence to the protocol.

9. Duties and responsibilities of staff

     9.1. Ophthalmologist

              •    Responsible for enrolling study subjects
              •    Provide information for completing the clinical examination forms
              •    Obtain written consent from the subjects with the help of study coordinator
              •    Initiate study medication as per the randomization
              •    Responsible for the care of the patient throughout the course of the study
              •    Manage adverse events

                                                                                                       56

```

### DOC-003 PDF page 58

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      September 4, 2012
Manual of Operation and Procedures


    9.2. Clinical Trial Manager

             •    Ensure the execution of the study as per the protocol
             •    Arrange training of the ophthalmic assistants, and refractionists
             •    Coordinate with the collaborating centers
             •    Prepare weekly reports regarding recruitment and follow-up progress
             •    Handle correspondence between centers
             •    Maintain IRB approval and renewals
             •    Communicate with central pharmacy regarding drug orders and distribution to sites

    9.3. Study Coordinator

             •    Make sure that appropriate patients are screened and enrolled in to the study
                  (including obtaining appropriate assent/consent)
             •    Prepare weekly reports regarding recruitment and follow-up progress
             •    Send reminders to study subjects for follow-up visits
             •    Meeting with the patient at each study visit, prior to the study ophthalmologist to
                  help maintain masking
             •    Assist ophthalmologist, ophthalmic assistants, and refractionists for conformity to
                  study procedures
             •    Verify data forms for completion and collect missing information
             •    Transfer study forms for prompt data entry
             •    Maintain stock of and dispense study medications

    9.4. Data Analyst

             •    Develop data entry programs specific to the study forms under the supervision of
                  DCC
             •    Monitor the flow of forms from the coordinator
             •    Supervise data entry operators for any errors or omissions
             •    Develop consistency checks
             •    Communicate with study coordinators and data entry operators to correct any
                  mistakes in study forms and data entry
             •    Transfer data as and when requested by the DCC
             •    Back up all data appropriately

    9.5. Data Entry Operator
             •    Enter all data from study forms when submitted by the study coordinator
             •    Verify inconsistencies in the forms and send them for correction to the study
                  coordinator
             •    Perform double entry to ensure accurate recording

     9.6. Biostatistician (Proctor)
             •    Review data for quality control purposes
             •    Prepare reports for DSMC
             •    Lock database at completion of study after database is cleaned
             •    Conduct analyses at the conclusion of the study
             •    Prepare randomization list and distribute the list to a pharmacist and non-
                  masked, senior physicians at the study sites in case of emergency.




                                                                                                      57

```

### DOC-003 PDF page 59

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial       September 4, 2012
 Manual of Operation and Procedures


     9.7. Ophthalmic Assistants

              •    Obtain patient information
              •    Measure preliminary vision
              •    Assist ophthalmologist in the clinical examination/enrollment of the subject
              •    Counsel and motivate patients to return for scheduled follow-up visits


     9.8. Refractionists

              •    Perform manifest refraction as specified by protocol of both eyes at each visit
              •    Measure and record best spectacle-corrected visual acuity at each visit
              •    Enter visual acuity (number of letters read and Snellen equivalent) on the study
                   form

     9.9. OCT Operators

              •    Perform OCT photography as specified by protocol of both eyes at all visits

     9.10. Fundus Photographers

              •    Perform fundus photography as specified by protocol of both eyes at the baseline,
                   6 months, 12 months or treatment failure visits.

     9.11. Fundus Graders

              •    Complete grading of vitreous haze from images of fundus photography.

10. Study Organization

     10.1. Executive Committee

     The Executive Committee will be chaired by Dr. Acharya at the Proctor Foundation and will
     include Dr. Lietman and Dr. Porco. This committee will act as the administrative and
     executive arm of the clinical trial and will meet once a month to provide overall oversight for
     the study and make decisions on day-to-day operational issues. The role of the Executive
     Committee includes but is not limited to monitoring study progress and data collection
     process, supervising the Clinical Coordinating Center (CCC) and Data Coordinating Center
     (DCC) for overall quality control, evaluating and adopting changes in study procedures as
     necessary, communicating with and implementing recommendations from the Data and
     Safety Monitoring Committee, making executive decisions on the allocation of resources,
     establishing policies on publications and authorship, and approving and overseeing ancillary
     studies.

     10.2 Clinical Coordinating Center (CCC)

     Dr. Acharya will also be responsible for directing the CCC, located at the Proctor
     Foundation/UCSF. The responsibility of the CCC includes oversight and coordination of the
     clinical implementation of the trial at Aravind, Oregon Health Sciences and at Proctor/UCSF.
     Specifically, this includes roles such as maintaining an up-to-date manual of operations,
     obtaining human research approvals from Institutional Review Boards, conducting training
     and certification of all personnel including physicians and refractionists, supervising

                                                                                                        58

```

### DOC-003 PDF page 60

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial    September 4, 2012
Manual of Operation and Procedures


    preparation and dispensing of study medication, ensuring proper masking, and monitoring
    protocol adherence and recruitment. The CCC will monitor the recruitment progress with
    weekly reports from each of the study sites. It will also organize twice yearly site visits to
    conduct chart reviews, training and certification of study personnel and monthly phone calls
    with study investigators to review enrollment, retention and any other study-related issues.
    Under the direction of the CCC, Dr. Salena Lee, the senior optometrist at the Proctor
    Foundation, will be responsible for training/certifying study refractionists and managing the
    refraction protocol. She will also be responsible for monitoring overall quality of the OCT
    imaging. Dr. Todd Margolis, co-investigator, will serve as medical monitor of the trial. He will
    receive all reports of serious adverse events from all study sites, ascertain whether further
    information is needed, and convey that information to the DSMC. As with our current NEI-
    funded studies, the study coordinator at Proctor/UCSF (Natalie Nardone) will assist with
    many of the clinical coordination activities listed above and also check in weekly by email
    with the study coordinators at each site to discuss any study-related issues.

    10.3 Data Coordinating Center (DCC)

    The DCC including, Dr. Lietman, Dr. Porco and Dr. Enanoria, is responsible for supervising
    data collection, data management, data quality control, data analysis, event adjudication,
    and training and certification of study site staff in the data management systems. The DCC
    will also be responsible for coordinating and supporting the activities of the Data Safety
    Monitoring Committee, including preparing interim and final data reports and organizing
    meetings with the Data Analysis Committee. The DCC will also be responsible for the
    dissemination of datasets for use by the Data Analysis Committee and other investigators.
    The DCC will meet weekly to monitor the progress and quality of data entry/management
    and address any issues. The DCC will be in close contact with the data analysts and data
    entry operators to ensure quality assurance of data entry. See MOP for further information
    on data management (Section 7).

    10.4 Data Analysis Center (DAC)

    Dr. Porco will direct the Data Analysis Committee with assistance from Dr. Enanoria. The
    primary functions of the DAC include designing a statistical analysis plan, preparing and
    distributing randomization lists, performing data analysis, and coordinating publications and
    presentations. The Committee is responsible for obtaining data from the Data Coordinating
    Center, performing unmasked data analyses and for preparing reports for the Data and
    Safety Monitoring Committee, and at the conclusion of the study, for the Principal
    Investigator. The DAC will also be responsible for conducting the prespecified interim
    analysis (when 1/3 of patients complete the study) and also for providing data to the DSMC
    to evaluate the stopping guidelines.

    10.5 Data Safety and Monitoring Committee (DSMC)

    The Data Safety and Monitoring Committee (DSMC) will be independent and NEI-appointed,
    with experts from diverse fields including ethics, biostatistics, epidemiology, ophthalmology,
    and international health care, and include at least one member of the NEI staff as an ex
    officio member. The committee will meet for the first time before the study begins. Only
    after the DSMC reviews and approves the protocol will patients be enrolled. We anticipate
    the group will meet regularly throughout the study and review information on data quality,
    enrollment, patient retention, and study outcomes, etc. Committee members will be
    instructed to be vigilant for any trend in severe or unexpected adverse events that may
    threaten the safety of the patients. They will be authorized to implement a conservative,

                                                                                                    59

```

### DOC-003 PDF page 61

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial    September 4, 2012
Manual of Operation and Procedures


    early stopping rule.

    10.6 Editorial Committee

    The Editorial Committee is composed of the principal investigator Dr. Acharya and co-
    investigators Dr. Rathinam and Dr. Suhler. This committee has the responsibility to assist in
    the preparation of the primary study results and to review secondary manuscripts produced
    by the study investigators. They have the responsibility to ensure the completion of the
    primary manuscript (Specific Aim 1) in a timely manner and direct its submission for
    publication.

    10.7 Study Sites

    Under the supervision of the CCC, Dr. Rathinam will direct the Aravind clinical centers, Dr.
    Suhler will direct the Casey Eye Institute clinical center, and Dr. Acharya will be in charge of
    the Proctor Foundation clinical center.

    10.8 Pharmacy

    Leiter’s Pharmacy (San Jose, CA) is one of the country’s largest ophthalmic compounding
    pharmacies and is well known among ophthalmologists for their quality and reproducibility.
    They have participated in a number of clinical trials with experience in preparing and
    masking medications identified only by study ID, including the SCUT, MUTT and FAST pilot
    trials. We have worked with Chuck Leiter to discuss drug preparation for this study and cost
    estimates, and have experience with the medication distribution process from our pilot trial.
    Leiter’s Pharmacy will prepare all of the study medications for the trial.

    10.9 Study Communications

    The study coordinator at the Proctor Foundation (Natalie Nardone) will be responsible for
    ensuring that communication between all facilities and committees is conducted seamlessly.
    Communication between study personnel at the Proctor Foundation and investigators at
    other sites will be performed by extensive use of secure email. Much of the communication
    will be through email, but we have found that regular, international, conference calls are
    valuable, and that regular, face-to-face meetings are mandatory. Members of the CCC and
    the DCC at the Proctor Foundation will visit Oregon and Aravind every 4-6 months through
    the duration of the study to discuss details of the study and monitor quality control.




                                                                                                    60

```

### DOC-003 PDF page 62

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   September 4, 2012
 Manual of Operation and Procedures


11. Bibliography

 1. Nussenblatt RB. The natural history of uveitis. Int Ophthalmol 1990;14:303-8.
 2. Rothova A, Suttorp-van Schulten MS, Frits Treffers W, Kijlstra A. Causes and frequency of
 blindness in patients with intraocular inflammatory disease. Br J Ophthalmol 1996;80:332-6.
 3. Gritz DC, Wong IG. Incidence and prevalence of uveitis in Northern California; the Northern
 California Epidemiology of Uveitis Study. Ophthalmology 2004;111:491-500; discussion 500.
 4. Suttorp-Schulten MS, Rothova A. The possible impact of uveitis in blindness: a literature
 survey. Br J Ophthalmol 1996;80:844-8.
 5. Durrani OM, Meads CA, Murray PI. Uveitis: a potentially blinding disease. Ophthalmologica
 2004;218:223-36.
 6. Rothova A, Buitenhuis HJ, Meenken C, et al. Uveitis and systemic disease. Br J Ophthalmol
 1992;76:137-41.
 7. Smit RL, Baarsma GS, de Vries J. Classification of 750 consecutive uveitis patients in the
 Rotterdam Eye Hospital. Int Ophthalmol 1993;17:71-6.
 8. McCannel CA, Holland GN, Helm CJ, Cornell PJ, Winston JV, Rimmer TG. Causes of uveitis in
 the general practice of ophthalmology. UCLA Community-Based Uveitis Study Group. Am J
 Ophthalmol 1996;121:35-46.
 9. Mercanti A, Parolini B, Bonora A, Lequaglie Q, Tomazzoli L. Epidemiology of endogenous
 uveitis in north-eastern Italy. Analysis of 655 new cases. Acta Ophthalmol Scand 2001;79:64-8.
 10. Das D, Bhattacharjee H, Bhattacharyya PK, et al. Pattern of uveitis in North East India: a
 tertiary eye care center study. Indian J Ophthalmol 2009;57:144-6.
 11. Rathinam SR, Namperumalsamy P. Global variation and pattern changes in epidemiology of
 uveitis. Indian J Ophthalmol 2007;55:173-83.
 12. Jabs DA, Rosenbaum JT, Foster CS, et al. Guidelines for the use of immunosuppressive
 drugs in patients with ocular inflammatory disorders: recommendations of an expert panel. Am J
 Ophthalmol 2000;130:492-513.
 13. Galor A, Jabs DA, Leder HA, et al. Comparison of antimetabolite drugs as corticosteroid-
 sparing therapy for noninfectious ocular inflammation. Ophthalmology 2008;115:1826-32.
 14. Siepmann K, Huber M, Stubiger N, Deuter C, Zierhut M. Mycophenolate mofetil is a highly
 effective and safe immunosuppressive agent for the treatment of uveitis : a retrospective analysis
 of 106 patients. Graefes Arch Clin Exp Ophthalmol 2006;244:788-94.
 15. Teoh SC, Hogan AC, Dick AD, Lee RW. Mycophenolate mofetil for the treatment of uveitis.
 Am J Ophthalmol 2008;146:752-60, 760 e1-3.
 16. Thorne JE, Jabs DA, Qazi FA, Nguyen QD, Kempen JH, Dunn JP. Mycophenolate mofetil
 therapy for inflammatory eye disease. Ophthalmology 2005;112:1472-7.
 17. Larkin G, Lightman S. Mycophenolate mofetil. A useful immunosuppressive in inflammatory
 eye disease. Ophthalmology 1999;106:370-4.
 18. Kilmartin DJ, Forrester JV, Dick AD. Rescue therapy with mycophenolate mofetil in refractory
 uveitis. Lancet 1998;352:35-6.
 19. Baltatzis S, Tufail F, Yu EN, Vredeveld CM, Foster CS. Mycophenolate mofetil as an
 immunomodulatory agent in the treatment of chronic ocular inflammatory disorders.
 Ophthalmology 2003;110:1061-5.
 20. Choudhary A, Harding SP, Bucknall RC, Pearce IA. Mycophenolate mofetil as an
 immunosuppressive agent in refractory inflammatory eye disease. J Ocul Pharmacol Ther
 2006;22:168-75.
 21. Bom S, Zamiri P, Lightman S. Use of methotrexate in the management of sight-threatening
 uveitis. Ocul Immunol Inflamm 2001;9:35-40.
 22. Dev S, McCallum RM, Jaffe GJ. Methotrexate treatment for sarcoid-associated panuveitis.
 Ophthalmology 1999;106:111-8.
 23. Foeldvari I, Wierk A. Methotrexate is an effective treatment for chronic uveitis associated with
 juvenile idiopathic arthritis. J Rheumatol 2005;32:362-5.
                                                                                                    61

```

### DOC-003 PDF page 63

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   September 4, 2012
Manual of Operation and Procedures


24. Gangaputra S, Newcomb CW, Liesegang TL, et al. Methotrexate for Ocular Inflammatory
Diseases. Ophthalmology 2009.
25. Holz FG, Krastel H, Breitbart A, Schwarz-Eywill M, Pezzutto A, Volcker HE. Low-dose
methotrexate treatment in noninfectious uveitis resistant to corticosteroids. Ger J Ophthalmol
1992;1:142-4.
26. Shah SS, Lowder CY, Schmitt MA, Wilke WS, Kosmorsky GS, Meisler DM. Low-dose
methotrexate therapy for ocular inflammatory disease. Ophthalmology 1992;99:1419-23.
27. Taylor SR, Habot-Wilner Z, Pacheco P, Lightman SL. Intraocular methotrexate in the
treatment of uveitis and uveitic cystoid macular edema. Ophthalmology 2009;116:797-801.
28. Daniel E, Thorne JE, Newcomb CW, et al. Mycophenolate Mofetil for Ocular Inflammation.
Am J Ophthalmol 2009.
29. Sobrin L, Christen W, Foster CS. Mycophenolate mofetil after methotrexate failure or
intolerance in the treatment of scleritis and uveitis. Ophthalmology 2008;115:1416-21, 1421 e1.
30. Jabs DA, Nussenblatt RB, Rosenbaum JT. Standardization of uveitis nomenclature for
reporting clinical data. Results of the First International Workshop. Am J Ophthalmol 2005; 140:
509-16.
31. Nussenblatt RB, Palestine AG, Chan CC, Roberge F. Standardization of vitreal inflammatory
activity in intermediate and posterior uveitis. Ophthalmology 1985;92:467-71.
32. Manual of Operations: Age Related Eye Disease Study, 2000.
33. Sherring AK. A Practical Guide on Refraction, 1999.




                                                                                                   62

```

### DOC-003 PDF page 64

```text
            NEI U10 EY021125-01



First-line Antimetabolites as Steroid-sparing
        Treatment (FAST) Uveitis Trial




       Manual of Operations & Procedures
                     (MOP)



                    January 06, 2017
                      Version 4.5

```

## Additional visual closure and finalized derivative record

[p47](../../../../joi190092supp2_prod.pdf#page=47), Figure 2, was rendered and opened because native text omitted the image labels. The Davis vitreous-haze photographic scale contains nine panels labeled 0, 1, 2 / 3, 4, 5 / 6, 7, 8, representing progressively more obscured fundus photographs. No patient data, estimate, interval, P value, or numerical score conversion is printed in the image. The label inventory is now complete. This is a fourth fresh-required unit in this shard; p18 is the third. Every other assigned page has source-matched reusable content sufficient for quantitative mapping. No gap remains.

Additional commands (Poppler 26.01.0):

```bash
pdftoppm -f 47 -l 47 -r 120 -singlefile -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/page-047
pdftotext -layout -f 15 -l 15 joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/layout-015.txt
pdftotext -layout -f 19 -l 19 joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/layout-019.txt
pdftotext -layout -f 18 -l 18 joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/layout-018.txt
pdftotext -layout -f 47 -l 47 joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_a/layout-047.txt
```

All derivatives are newly created; all source and reused assets remain unchanged. The fresh layout files confirm absence of p15/p19 text and partial p18/p47 image transcription. Final exact partition: total 64, reusable 60, fresh-required 4, mapped 64. No Office or workbook sources occur in the assigned scope. Coverage status COMPLETE.
