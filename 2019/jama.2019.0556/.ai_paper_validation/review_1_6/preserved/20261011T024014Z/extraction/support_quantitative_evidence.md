# Workflow 1.6 Support Quantitative Evidence Map

## Scope, tooling, and completeness

Owner/runtime agent: /root/support_mapper; fresh qc16_support_quantitative_mapper, gpt-6.1-sol/medium. Scope: DOC-002 joi190007supp1_prod.pdf physical pages 1–60; DOC-003 joi190007supp2_prod.pdf pages 1–5; DOC-004 joi190007supp3_prod.pdf pages 1–25; DOC-005 joi190007supp4_prod.pdf page 1. These are 91 disjoint PDF_PAGE units, all newly read and mapped. Reusable-backed units: DOC-004 pages 1–2 and 16–23 (10). Fresh-required units: the other 81; all have both new native and layout extraction. No workbook, CSV, DOC/DOCX, formulas or cached workbook values are supplied. No scientific coverage gap remains.

Read normative QUALITY_CONTROL_SCOPE.md, workflow_1_6/review_contract.md, settings.toml, source_inventory.md, evidence_asset_inventory.md, source_coverage.md, coverage_manifest.md and tooling_record.md. The evidence inventories were read as asset locators only. No previous conclusions/candidates were read. Role assignment is by content: DOC-002 and DOC-003 PLAN; DOC-004 and DOC-005 REPORT. Historical/background quantities within PLAN remain PLAN.

Derivative engine: direct Poppler pdftotext 26.01.0. For each explicit fresh-required page P in supplement S, commands were `pdftotext -f P -l P "joi190007suppS_prod.pdf" ".ai_paper_validation/review_1_6/preprocessing/support-sS-pP-native.txt"` and `pdftotext -layout -f P -l P "joi190007suppS_prod.pdf" ".ai_paper_validation/review_1_6/preprocessing/support-sS-pP-layout.txt"`. Expanded scope: S=1 P=1–60; S=2 P=1–5; S=3 P=3–15,24–25; S=4 P=1. Exactly 162 text derivatives; native and layout source pages agree in content. Text/layout is transcription aid, direct source remains authority.

Targeted direct render engine: Poppler pdftoppm 26.01.0, CPU, command `pdftoppm -r 110 -f P -l P -singlefile -png joi190007supp1_prod.pdf ".ai_paper_validation/review_1_6/preprocessing/support-s1-pP"`, P=12,25,31,32,38 (five PNG derivatives). These five visuals were inspected; p38 truly blank, p32 has only the final 24-month box, p31 contains the image flowchart omitted from native text, p12 is conceptual only. Existing PyMuPDF 180-dpi DOC-004 rendered_pages/page_016.png through page_023.png were visually inspected as a batch of eight; every table row and the plotted figure were mapped. No new OCR necessary; no fallback environment or GPU used. Thirteen support visuals inspected; below 32-image batch bound.

Limitations: plotted distributions on DOC-004 p17 have no printed exact means/medians/sample sizes; record legend, axes and direction without inventing values. Protocol p32 Figure 3 as supplied is mostly blank with only final 24-month follow-up box; direct rendering confirms this is source presentation, not extraction omission. Referenced C1.2 manufacturing document and raw participant data are not supplied. These are derivative/precision limitations, not skipped units. Text source contains non-English operational names on PLAN p37; mapping below translates their meanings in English while preserving numeric amounts.

Local U keys below are mapping keys only; coordinator assigns stable N/S IDs. Each keyed row is a relationship family, with distinct printed inferential rows separately identified by subkey so none can be lost during registration. This map does not diagnose candidates or assign dispositions.

## Every-page coverage ledger

All page numbers here are physical PDF pages; DOC-004 printed page is physical minus one from p3 onward. Status MAPPED means content opened and quantitative scope reconstructed; NO_APPLICABLE means opened with no result-relevant quantitative relationship beyond identifiers, bibliographic dates or administration. No source page is omitted.

| Source | Page | Role | Status | Content and quantitative mapping |
|---|---:|---|---|---|
| DOC-002 | 1 | PLAN | NO_APPLICABLE | Cover/version 7, July 11 2017; approval July 8 2015; identities only. |
| DOC-002 | 2 | PLAN | NO_APPLICABLE | Title/sponsor/version/date/address; administrative quantities only. |
| DOC-002 | 3 | PLAN | NO_APPLICABLE | Signature sheet only. |
| DOC-002 | 4 | PLAN | NO_APPLICABLE | Contents first part; page locators only. |
| DOC-002 | 5 | PLAN | NO_APPLICABLE | Contents second part; page locators only. |
| DOC-002 | 6 | PLAN | NO_APPLICABLE | Contents final part; page locators only. |
| DOC-002 | 7 | PLAN | NO_APPLICABLE | Abbreviations/administrative definitions; no estimates. |
| DOC-002 | 8 | PLAN | MAPPED | U001 design, age, nutrient doses, FBC session/time counts, MDD DSM-IV/MINI endpoint. |
| DOC-002 | 9 | PLAN | MAPPED | U002 IDS and assessment schedule, blood draw amounts, sessions/daily pills. |
| DOC-002 | 10 | PLAN | MAPPED | U003 background depression prevalence 10–25% women, 5–12% men, about 6% current population. |
| DOC-002 | 11 | PLAN | NO_APPLICABLE | Mechanistic rationale and cited qualitative effects; reference numbers are not estimates. |
| DOC-002 | 12 | PLAN | MAPPED | U004 visually inspected conceptual diagram; B12/B6 are nutrient labels, arrows 1–5 denote pathways not numeric effects. |
| DOC-002 | 13 | PLAN | MAPPED | U005 BMI more than 25 enrollment statement. |
| DOC-002 | 14 | PLAN | MAPPED | U006 primary one-year prevention; secondary IDS and other outcomes, 24-month effects. |
| DOC-002 | 15 | PLAN | MAPPED | U007 factorial four cells each250, about63 NL each, four countries each250, pooled1000; follow-up3/6/12/24. |
| DOC-002 | 16 | PLAN | MAPPED | U008 eligibility; U009 sample-size, incidence, alpha/power/dropout. |
| DOC-002 | 17 | PLAN | MAPPED | U010 IDS-30 power and80% pure-group comparison if synergistic. |
| DOC-002 | 18 | PLAN | MAPPED | U011 nutrient doses; two daily pills; distribution baseline3/6/9; 2-week call. |
| DOC-002 | 19 | PLAN | MAPPED | U012 adherence every3months;21 sessions=15x30min+6x60min. |
| DOC-002 | 20 | PLAN | MAPPED | U013 product composition minimum65%EPA/10%DHA, sunflower40%, acceptable90–125% deviation. |
| DOC-002 | 21 | PLAN | MAPPED | U014 historical endogenous vitamin D80–90%; qualitative prior studies. |
| DOC-002 | 22 | PLAN | MAPPED | U015 daily-year supplement definition; qualitative historical clinical evidence. |
| DOC-002 | 23 | PLAN | MAPPED | U016 planned EPA+DHA1.0g/day; safety comparators3g/5g; vitamin20μg=800IU; folate doses. |
| DOC-002 | 24 | PLAN | MAPPED | U017 dose/safety ranges, age-specific calcium, selenium, historical omega-dose range. |
| DOC-002 | 25 | PLAN | MAPPED | U018 folate/calcium/selenium daily doses; visually confirmed no additional label figure. |
| DOC-002 | 26 | PLAN | MAPPED | U01913-week supply baseline3/6/9; jar weight adherence. |
| DOC-002 | 27 | PLAN | NO_APPLICABLE | Non-investigational product explicitly not applicable. |
| DOC-002 | 28 | PLAN | MAPPED | U020 primary endpoints DSM-5/MINI V5.0 followed by superscript citation1 and IDS; secondary instrument identities. |
| DOC-002 | 29 | PLAN | MAPPED | U021 confounders24months; block-randomization by MDDhistory/center; screening age18–65/BMI>25/PHQ≥5. |
| DOC-002 | 30 | PLAN | MAPPED | U022 four-month initial pill package,12questionnaires, screening gap≥1week,2week call,3/6/12/24 assessment. |
| DOC-002 | 31 | PLAN | MAPPED | U023 visual recruitment diagram; five routes, PHQ9, past6month medication, telephone±15min, MINI MDD. |
| DOC-002 | 32 | PLAN | MAPPED | U024 visual Figure3 shows only online24month questionnaire box. |
| DOC-002 | 33 | PLAN | MAPPED | U025 screening instrument table,6month drug/therapy/history windows, MINI V5 DSM-IV. |
| DOC-002 | 34 | PLAN | MAPPED | U026 interview schedule baseline3/6/9/12; current MINI DSM-IV at3/6/12; lifetime baseline. |
| DOC-002 | 35 | PLAN | MAPPED | U027 all questionnaire item counts/times; optional9month physical measurements. |
| DOC-002 | 36 | PLAN | MAPPED | U028 remaining questionnaire counts/times and five blood specimen rows. |
| DOC-002 | 37 | PLAN | MAPPED | U029 five tube volumes totaling37ml at baseline6/12; schedule footnotes. |
| DOC-002 | 38 | PLAN | NO_APPLICABLE | Direct visual confirms blank page except header/footer. |
| DOC-002 | 39 | PLAN | MAPPED | U030 follow-up after treatment withdrawal retained for ITT/per-protocol. |
| DOC-002 | 40 | PLAN | MAPPED | U031 AE/SAE definitions and extra1month assessment for mild depression. |
| DOC-002 | 41 | PLAN | NO_APPLICABLE | Safety reporting deadlines15/7/8days; administrative, no results. |
| DOC-002 | 42 | PLAN | NO_APPLICABLE | Safety deadlines and half-year lists; DSMB/annualreport not applicable; no results. |
| DOC-002 | 43 | PLAN | MAPPED | U032 all planned primary/secondary/mixed/survival/mediation methods. |
| DOC-002 | 44 | PLAN | MAPPED | U033 nutrient subgroup linear regression and modifier interactions country/sex/education/income/BMI/age. |
| DOC-002 | 45 | PLAN | MAPPED | U034 half randomized totherapy; blood draw optional, general safety. |
| DOC-002 | 46 | PLAN | MAPPED | U035 IDS≥39 threshold; endpoint cases maycontinue; pill+capsule/day,≥4visits,21therapyvisits. |
| DOC-002 | 47 | PLAN | MAPPED | U036 IDS≥39 and>13 thresholds,10euro at4waves; insurance numbers administrative only. |
| DOC-002 | 48 | PLAN | NO_APPLICABLE | Data handling15years/six-digit IDs and amendment procedures; no result quantities. |
| DOC-002 | 49 | PLAN | NO_APPLICABLE | Annual/finalreport deadlines90/15days/1year/60days; administrative only. |
| DOC-002 | 50 | PLAN | NO_APPLICABLE | Structured risk analysis; four countries and product restrictions restate prior plan. |
| DOC-002 | 51 | PLAN | NO_APPLICABLE | Bibliography refs1–7, no additional reported estimates. |
| DOC-002 | 52 | PLAN | MAPPED | U037 reference11 title contains6362events/146538participants/54studies; bibliographic background only. |
| DOC-002 | 53 | PLAN | NO_APPLICABLE | Bibliography refs17–25, no additional numeric findings. |
| DOC-002 | 54 | PLAN | NO_APPLICABLE | Bibliography refs26–34, numeric genetic/metabolite identifiers only. |
| DOC-002 | 55 | PLAN | NO_APPLICABLE | Bibliography refs35–41;6month trial title is historical study duration. |
| DOC-002 | 56 | PLAN | MAPPED | U038 reference44 title250normalwomen; reference49 historical2yearstudy; no outcome estimates. |
| DOC-002 | 57 | PLAN | NO_APPLICABLE | Bibliography refs51–59; no additional numeric findings. |
| DOC-002 | 58 | PLAN | NO_APPLICABLE | Bibliography refs60–69; numeric nutrient identifiers only. |
| DOC-002 | 59 | PLAN | NO_APPLICABLE | Bibliography refs70–80; citations only. |
| DOC-002 | 60 | PLAN | NO_APPLICABLE | Bibliography refs81–89; identifiers and dates only. |
| DOC-003 | 1 | PLAN | MAPPED | U039 wavesT0/T3/T6/T9/T12; historical17% lifetimeprevalence. |
| DOC-003 | 2 | PLAN | MAPPED | U040 binary cumulativeMDD definition, secondary symptoms/utility and strata covariates. |
| DOC-003 | 3 | PLAN | MAPPED | U041 descriptive/adherence/inferential plans, effectcoding, OR/CI/P, GEE/mixed/standardized differences,2-sided.05. |
| DOC-003 | 4 | PLAN | MAPPED | U042 ITT/CACE,≥70%supplements,≥8/21sessions, RERI/linearOR model, Cox secondary, modification. |
| DOC-003 | 5 | PLAN | MAPPED | U043 interactionP<.05; MI100datasets/MAR/Rubin; sensitivity/outliers/transformation. |
| DOC-004 | 1 | REPORT | NO_APPLICABLE | Supplementcover/contents; concealmentn759 locator not separate result. |
| DOC-004 | 2 | REPORT | NO_APPLICABLE | Appendixcontents page locators only. |
| DOC-004 | 3 | REPORT | MAPPED | U044 eligibility age18–75/BMI25–40/PHQ≥5; DSM-IV/MINI5.0;6monthexclusions. |
| DOC-004 | 4 | REPORT | MAPPED | U045 doses1412mg EPA+DHA3:1; other micronutrients and placebopercentages. |
| DOC-004 | 5 | REPORT | MAPPED | U046 independent producttesting6active/5placebo in duplicate;means/SD/unit. |
| DOC-004 | 6 | REPORT | MAPPED | U047 foodtargets/tenfoodgroups;21sessions/15individual/6group/10people. |
| DOC-004 | 7 | REPORT | MAPPED | U048 MCID andscale cutoffs forPHQ/IDS/GAD/EQ5D5L. |
| DOC-004 | 8 | REPORT | MAPPED | U049 adherence8/21rationale;prior4–8/2–8/6sessioneffect,COBRA8/20,NICE12. |
| DOC-004 | 9 | REPORT | MAPPED | U05015+6session sequencing,8/21 means≥halfindividualsessions;EC50 analogy. |
| DOC-004 | 10 | REPORT | NO_APPLICABLE | Bibliography9references; no additional observed trialresults. |
| DOC-004 | 11 | REPORT | NO_APPLICABLE | Finalrationale citation only. |
| DOC-004 | 12 | REPORT | MAPPED | U051 adherence definitions,kappa.73/.70,FFQ250items/11foodgroups/0–77score,bloodn211–331/22–32%. |
| DOC-004 | 13 | REPORT | MAPPED | U052 hospitalization/death ascertainment and12monthconcealmentquestion. |
| DOC-004 | 14 | REPORT | MAPPED | U053 CACE definitions/latentclasses/assignment/compliance probabilities. |
| DOC-004 | 15 | REPORT | MAPPED | U054 CACE estimate ratio andstructuralequationmodel explanation. |
| DOC-004 | 16 | REPORT | MAPPED | U055 all18observed adherence/adverseevent/change rows andfootnotes. |
| DOC-004 | 17 | REPORT | MAPPED | U056 all4outcomeboxplotpanels,4groups,time0/3/6/12,axis9without observations;caption. |
| DOC-004 | 18 | REPORT | MAPPED | U057 narrative moderation and9inferentialrows plusreference tableA. |
| DOC-004 | 19 | REPORT | MAPPED | U0589inferentialrows plusreference tableB. |
| DOC-004 | 20 | REPORT | MAPPED | U05913inferentialrows tableC1; U0604UKrows; U0614NLrows. |
| DOC-004 | 21 | REPORT | MAPPED | U06224inferentialresults in12rows,nonimputed GEEoverall/robustT12,footnotes. |
| DOC-004 | 22 | REPORT | MAPPED | U0638CACEinferentialresults,MIadjustments/coding/compliancethresholds/stars. |
| DOC-004 | 23 | REPORT | MAPPED | U06412concealmentcells,4column denominators,total759,P<.001. |
| DOC-004 | 24 | REPORT | NO_APPLICABLE | Bibliography refs1–14; noadditionalresults. |
| DOC-004 | 25 | REPORT | NO_APPLICABLE | Bibliography refs15–26; noadditionalresults. |
| DOC-005 | 1 | REPORT | NO_APPLICABLE | Complete data-sharing statement; no participantresults; publishedMarch5,2019 and conditional access. |

Coverage counts: DOC-00260/60; DOC-0035/5; DOC-00425/25; DOC-0051/1. Status counts:61 MAPPED plus30 NO_APPLICABLE=91 complete. This status count is informational; every row is mapped for source-coverage purposes.

## PLAN quantitative and statistical relationships U001–U043

Each key points to the same physical page as the coverage ledger; embedded transcriptions below retain every printed value, label and paragraph. Expected main-paper matching keys are semantic identities, not claims of agreement or disagreement.

- U001 [DOC-002 p8](../../../joi190007supp1_prod.pdf#page=8): one-year2x2four-country prevention; population18–75overweight/mildsymptoms. Capsule1000mg EPA:DHA3:1 withEPA>700mg/DHA>100mg; calcium100–200mg,selenium25–55μg,B11folate400–600μg,vitaminD20μg. FBC21=15individual30min+6group60min. Mainendpoint12month cumulativeMDD DSM-IV MINI measuredbaseline3/6/12. Matching: design,dose,therapy,primaryoutcome.
- U002 p9: IDSbaseline3/6/12; assessmentsbaseline3/6/9/12 with4sitevisits+optional9monthvisit;24monthonline;12questionnairetopics; bloodbaseline6/12:3x6ml+2x8.5ml; dailyyearpill;15individual30min+6group60min. Matching: IDSoutcomerole,visitandblooddefinitions.
- U003 p10: background lifetimeprevalencewomen10–25%,men5–12%,currentMDDabout6%;burdenrank3projected1by2030. PLANbackground,notobservedtrialdata.
- U004 p12: conceptualFigure1 connectsfoodintake/behavior,depression,obesity,socialenvironment; arrows1–5arepathwaylabels,notestimates. Nofigurecounts,effectsorintervals.
- U005 p13: BMI>25 enrollmentdefinition. Compare precisely toinclusionrange,withoutassumingstrictboundary changesactualdenominators.
- U006 p14: primaryone-yearprevention;secondarysustainability,foodbehavior/intake/costs,weight,activity/sedentary,IDS,bodyimage/foodperception,qualityoflife;mediators/moderators;24monthlongterm.
- U007 p15: eachoffourfactorialcells250(about63NL);eachfourcountries250,pool1000;Dutcharm36monthtotal,inclusion1year,followup3/6/12/24. ExpectedmatchingrandomizedN/groupNandfactorialcontrasts.
- U008 p16: age18–75,BMI25–40,PHQ9≥5;currentMDDpast6months DSM-IV MINI excluded;antidepressant/psychologicalinterventionpast6months;anxiety/alcohol/substancedependenceprevious6months;psychosis/schizophrenia/bipolar/eatinghistory;otherlistedphysical/nutrient/pregnancy exclusions retained in transcription. RecruitmentJuly2015–June2016.
- U009 p16: printedpowered25%differenceincumulativeincidenceacross1year;control30%versusintervention15%;additiveinteraction180/group;two-sidedalpha.05,power.90,dropout20%;250/armcalledsufficient. Preserve eachquantityseparately:percentageofwhatdifferenceisnotdefinedhere. Matchsample-sizeparagraph;do notreconstruct an unreported powerformula.
- U010 p17: IDS-30continuousoutcomepowerlarger;synergisticpuregroupscomparisonmainoutcomepower80%. Matchfactorialinteractionmodelandpowerframing.
- U011 p18:2dailyunits(capsule+pill),one-year;repeat1000mg/EPA:DHA3:1/>700/>100;Ca100–200mg/Se25–55μg/B11400–600μg/D20μg;baseline3/6/9distribution;two-weekblindedcall;jarsweighed.
- U012 p19:adherenceevery3months;21sessions15x30min+6x1h. Match≥8sessioncompliancerationale.
- U013 p20:min65%EPA/min10%DHAcomposition;omega-placebo sunfloweroil78(40%)asprinted;acceptabledeviation90–125%;externalC1.2documentnot supplied.
- U014 p21:vitaminD80–90%endogenoussynthesis;backgroundnottrialresult. Omegaqualitativesupplementeffectsnoestimates.
- U015 p22:dailyplacebo/supplementfor1year;historicalcalcium/seleniumresultsqualitativewithoutnumeric effectestimates.
- U016 p23:EPA+DHA=1.0g/day; citedsafeFDA3g/day,EFSA5g/day;D20μg=800IU,4000IU/dayupperlimitand100μg/dayEFSA;toxicity>25000IU/day/noharm10000IU/day(asPLANbackground);folate400–600μgvsrecommended200–400μg.
- U017 p24:folateupperlimit1000μg/day;Ca2500mg/dayage19–50,2000mgage51–70/>70;Se25–55μg/dayvsadequate70/upper300μg;EPA>700mg/DHA>100mg/day;citedefficacious0.6–4.4gEPA+0.2–2.2gDHA;D20μg=800IU/day.
- U018 p25:folate400–600μg/day;Ca100–200mg/day;Se25–55μg/day;calciumevidenceage50+;externalmanufacturerpagesarelocatorsnotoutcomes.
- U019 p26:13weeksupplyatbaseline3/6/9;unusedjarsweighedtocalculatenotconsumed. Matchsupplementadherence calculation.
- U020 p28:main12monthMDDcumulativeincidence DSM-5 MINI V5.0 followed by superscript citation1,baseline3/6/12;IDSalsomainendpoint. SecondaryFFQ-GA2LEN,TFEQ18,SQUASH,SBQ,GAD7,EQ5D5L,SRBAI,BADS,evaluationandLIDAS24months. Matchmain/secondary outcome definitions andscales.
- U021 p29:otherBMI/waist/hip/BP/sociodemographic/medical/DNA/nutrientmeasures;24monthallsecondaryexcept evaluation. BlockrandomizationstratifiedMDDhistoryandcenter;mailages18–65,BMI>25/PHQ≥5. Matchstrataandeligibilitydenominatoronlywhere concrete.
- U022 p30:12self-reportquestionnaires,initial4monthpillpackage,fourarms;screening-to-baseline≥1week;therapyandpillcall≤2weeks;followup3/6/12/24. Matchdistribution/adherence support.
- U023 p31 visual:five recruitmentroutes(municipal,GP,cohorts,internet/socialmedia,printed/audio);screeningage/sex/weight/height,antidepressantpast6months,postcode/PHQ9;telephoneapprox15minutes;MINIdiagnosisrulesoutcurrentdepression;no printed participantflowcounts.
- U024 p32 visual:onlyonline24monthfollowupquestionnairebox;no additional quantitative node visible in suppliedPDF.
- U025 p33:screenonline/paperthenphone;MINIV5presentDSM-IV;antidepressantandtherapy6monthwindow;pregnancy/bariatricnextyear;otherexclusionsastranscribed.
- U026 p34:MINIV5currentDSM-IV3/6/12;lifetimedepressionbaseline;smokingbaseline6/12;AUDITbaseline12;chronicillnessfollowup3/6/12past3/6months;medicationlastmonthbaseline,last6months6/12;positive/negativeeffects6/12;otherinterventions12.
- U027 p35:BP/anthropometrybaseline3/6/optional9/12. Questionnaireitemcounts:PHQ9=9,IDS=30,GAD=7,EuroQol=5,TFEQ18printed21,foodbehavior47,FFQ264,Stunkard2,SQUASH20. Allbaseline3/6/12/24exceptFFQbaseline6/12/24;no9monthquestionnairemarksfor theserows. Matchinstrumentlength/labelsandassessmenttimes.
- U028 p36:SBQ18,SRBAI36,BADS25 eachbaseline3/6/12/24;adherence3items3/6/9/12;evaluationsupplements7/lifestyle25at12;LIDAS26,weight8,supplementuse9at24. Bloodbaseline6/12:serum2x8.5ml,traceelement6ml,hematologyEDTA2ml,plasmaEDTA6ml,DNAEDTA6ml**. FootnoteDNAconditionalfunding.
- U029 p37:tablebaseline6/12each17+6+2+6+6=printed37ml; q=selfreport/i=interview;9monthBP/anthropometryonlyifvisiting,notpostalexchange;DNAiffundingallows. Matchp9bloodamounts withspecificsite/timeconditioning.
- U030 p39:withdrawalfrominterventionencouragedtocontinuemeasurementsforITT/per-protocol;sample-size incorporates dropout.
- U031 p40:AEanyundesirableexperienceirrespectiveofrelatedness;SAEdeath/lifethreat/hospitalization/disability/congenital/otherimportantmedicalevent;extramilddepressionfollowup1month. Matchreportedseriousadverseeventdenominatorandlabel.
- U032 p43:pooledallfourcenters;mainITT,supplementaryperprotocol;baselinechi-square/t/ANCOVA. PrimaryMDDtimeeventKaplanMeier/logrank/Cox;two-wayand4-wayseparate/combinedeffects;adjustcountry/history;mixedregressionbaseline3/6/12forMDD/IDSmain/interactions;repeatedparticipantsandcountryclustering. Secondarymixedmodelsfood/BMI/weight/activity/sedentary/PHQ/anxiety/bodyimage/eating/utility. Four-stepmediationregressionwithbootstrapindirecteffects. No model coefficients printed here.
- U033 p44:linearregressioninbloodsubsetnutrientchangevsMDDonset/symptomchangeadjustintervention;CoxMDD/mixedsymptominteractionmodifierscountry,sex,education,income,BMI,age. Matchmodifierlist without treating omittedfutureoutcomesascandidates.
- U034 p45:halfreceivebehavioraltherapy;bloodoptional. Relevanttostrata/adherencedenominators,not standalone designissue.
- U035 p46:MINIMDDplusIDS≥39and/orsuicidalitytriggersGPcontact;MDDendpointparticipantsmaycontinue;daily pill+capsuleforoneyear,≥4sitevisits,21therapysessions.
- U036 p47:sameseverethresholdIDS≥39;IDS>13maycontinueunlesshospitalization;10euroeachfourwaves;insurance650000/5000000/7500000eurosand4yearcoverageadministrativeoutofquantitativeresultscope.
- U037 p52:historicalreference11title6362events/146538participants/54observationalstudies;noresult effectestimate;not a trial denominatorkey.
- U038 p56:historicalreference44title250normalwomen;ref49duration2years. No matchedMooDFOOD cohort implied.
- U039 DOC-003p1:wavesT0/T3/T6/T9/T12;backgroundMDDlifetimeprevalence17%,burdenrank2forYLD;not same metricastotalburdenp10protocol.
- U040 DOC-003p2:primarycumulativeMDDsinceT0yes/noMINI5.0plusMDDsection;yes1ifMDDpositiveT3orT6orT12;no0ifnegativeallthree. SecondaryPHQ9/IDS30SRatT3/T6/T12;otherGAD7/EQ5D5L. CovariatesallanalysesMDDhistoryT0yes/no+AMS/LEI/EXE/MALsite.
- U041 DOC-003p3:flowcountsandfourbaselinecolumns;adherenceMoroskyscale/%pills/reasons/sessions;bloodT6/T12D/Se/folate/EPA/DHAadjustT0;behaviorT3/T6/T12,FFQT6/T12adjustT0. PrimarylogisticOR95%CI/P,interventions effectcoded main/interactions;secondarymixed/GEE B95%CI/Padjuststrata+T0outcomes;T12standardizedmeandifferences95%CI/P;AEandconcealmentdescriptive;SASorR;alltests2-sidedP.05.
- U042 DOC-003p4:ITTprimary/CACEsecondary;goodcompliance≥70%supplements/yearjarweightselsemeanT3/T6/T9/T12selfreport;≥8/21sessions. LogisticA*Bstatisticalinteractionmultiplicative;biologicaladditiveriskinteractionRERI>0via linearORmodel,likelihood95%CI,lowestjoint-riskreferenceafterrecoding. CoxMDDtime-to-onsetsecondaryHR95%CI/P. SecondarymodificationMDDhistory/center;othersseparatepaper.
- U043 DOC-003p5:effectmodification logisticA*history/B*historyplusA,B,history,center;P<.05criterion;tabledstratifiedortext. Missingfrequency/nature,FIMLorMIappropriate;MI100datasetsprimaryoutcomeMAR,Rubinpooledestimates,sensitivityforunverifiablemissingness. Correctimpossibleoutliers,sensitivitywith/withoutotheroutliers,logtransformifmodeldistributionviolation.

## REPORT relationships U044–U064

U044 [DOC-004 p3](../../../joi190007supp3_prod.pdf#page=3), recruitment and eligibility: age 18–75 years, BMI 25–40 kg/m², PHQ-9 ≥5; MDD past 6 months according to DSM-IV MINI5.0 excluded; antidepressants/psychological intervention past6months excluded. Current eating disorder and history of psychosis/bipolar/substance dependence/severe psychiatric disorder are distinct exclusion labels. Match to main Methods population and protocol p16; do not presume history/current differences affect a reported count without a numeric link.

U045 [DOC-004 p4](../../../joi190007supp3_prod.pdf#page=4), delivered dose: 2 pills daily for one year; 1412mg EPA+DHA ratio3:1; selenium30μg, folic acid400μg, D3 20μg, calcium100mg. Placebo sunflower oil57% linoleic and30% oleic. Historical therapeutic ranges0.6–4.4gEPA +0.2–2.2gDHA. Match main intervention quantities and PLAN dose ranges; product composition itself is observed REPORT content.

U046 [DOC-004 p5](../../../joi190007supp3_prod.pdf#page=5), laboratory product verification: duplicate testing of6active and5placebo supplements; selenium mean30μg SD0.4; EPA67.9g/100gFAME SD0.85; DHA14.6g/100gFAME SD1.55. Placebo selenium0.03μg/kg SD0.03; EPA/DHA<0.1gram. Preserve FAME compositional basis distinctly from declared daily EPA/DHA mass; no unprovided total fat mass assumed.

U047 [DOC-004 p6](../../../joi190007supp3_prod.pdf#page=6), F-BA dietary advice and delivered schedule: ten different food groups claimed; vegetables300–400g/day, fruit2–3pieces/day, fish3times/week, meat300g/week, pulses3times/week, whole grains, dairy3servings/day, olive oil main cooking source, limit processed food and soft drinks, alcohol moderation. Up to21sessions;15individual30min (single or double1h) weekly then fortnightly;6group1h up to10people monthly then bimonthly. Match diet-score group labels and main intervention session counts.

U048 [DOC-004 p7](../../../joi190007supp3_prod.pdf#page=7), scale/clinical interpretation: PHQ-9 MCID2–3points (1SEM) or4–6 (2SEM), severity cutoffs5/10/15/20 mild/moderate/moderate-severe/severe. IDS no reportedMCID; cutoffs14/26/39/49 mild/moderate/severe/very severe. GAD-7 MCID2–3(1SEM) or4–6(2SEM), cutoffs5/10/15 mild/moderate/severe. EQ5D5L health utilityMCID.074. These are treatment-setting reference thresholds, not trial effect sizes.

U049 [DOC-004 p8](../../../joi190007supp3_prod.pdf#page=8): pre-specified adherence8/21 sessions. Rationale cites prior effects4–8sessions and changes first2–8; average6sessions; COBRA≥8of20 and recommended CBT12. Historical treatment quantities explicitly distinguished from observed MooDFOOD attendance.

U050 [DOC-004 p9](../../../joi190007supp3_prod.pdf#page=9): up to15 individual followed by6group sessions in12months, maintenance over remaining6months;8/21 expected≥half15individual;EC50 used as dose-response analogy. No pharmacological EC50 estimated.

U051 [DOC-004 p12](../../../joi190007supp3_prod.pdf#page=12), adherence and change measures: ≥8/21 F-BA and≥70%supplements/year defined a priori; jars count taken/received; self-report3/6/9/12; kappa.73 supplement1 and.70 supplement2, 4-itemMorisky. Change12month minus baseline weightkg absolute/relative, diet quality, serum nutrients. FFQ250items, eleven diet quality food groups, total range0–77. Baseline/12month blood subset n211–331 (22–32%), stored−80°C, selenium/folate/25OHvitaminD. Match sample-size/percentage definitions to p16; timing and biomarker-specific denominator remain keys, not assumed identical.

U052 [DOC-004 p13](../../../joi190007supp3_prod.pdf#page=13): hospitalization from follow-up questions or dropout reason; deaths from dropout reason; supplement allocation guess at12months. Match p16 adverse event counts and p23 concealment N.

U053–U054 [DOC-004 p14](../../../joi190007supp3_prod.pdf#page=14) and [p15](../../../joi190007supp3_prod.pdf#page=15): CACE defined for people receiving adequate assigned dose; two latent classes; equal allocation probability and similar compliance proportion; exclusion restriction; randomization instrumental variable in structural equation model retaining full sample. Printed effect estimate formula: original intervention estimate divided by proportion of compliers in treated arm. This defines a scale-sensitive matching key; do not apply formula to OR itself unless source establishes transformation.

### U055: Every row of adherence, adverse events and changes

[DOC-004 p16](../../../joi190007supp3_prod.pdf#page=16), printed p15, eAppendix8. Column order A=placebo/noF-BA; B=placebo/F-BA; C=supplements/noF-BA; D=supplements/F-BA. N is available analytic total, not number adherent; percentages are per-arm among available observations for each row. Full native transcription below is retained; visually checked all cells.

| Local row key | Outcome and scale | N | A | B | C | D |
|---|---|---:|---|---|---|---|
| U055.a | Multinutrient adherence≥70% by weight, n(%) | 666 | 135(76.7%) | 134(78.8%) | 126(75.0%) | 120(78.9%) |
| U055.b | Multinutrient adherence≥70% self-report, n(%) | 855 | 164(77.7%) | 165(74.3%) | 155(73.8%) | 151(71.2%) |
| U055.c | Omega adherence≥70% by weight, n(%) | 652 | 133(76.9%) | 133(81.1%) | 126(76.8%) | 120(79.5%) |
| U055.d | Omega adherence≥70% self-report, n(%) | 855 | 163(77.3%) | 164(73.9%) | 156(74.3%) | 152(71.7%) |
| U055.e | Average Morisky, median(IQR) | 856 | 1(0.50–1.50) | 1(0.50–1.75) | 1(0.50–1.50) | 1(0.50–1.75) |
| U055.f | F-BA attendance≥8, percent | 512 | NA | 71.9% | NA | 70.7% |
| U055.g | All F-BA sessions, median(IQR) | 512 | NA | 15(6–18) | NA | 15(6–19) |
| U055.h | Individual sessions, median(IQR) | 512 | NA | 14(6–15) | NA | 14(6–15) |
| U055.i | Group sessions, median(IQR) | 512 | NA | 0(0–3.3) | NA | 0(0–4) |
| U055.j | Deaths, count | NA | 0 | 0 | 0 | 1 |
| U055.k | Persons hospitalized, count | NA | 24 | 24 | 26 | 24 |
| U055.l | Diet score change T12−T0 | 719 | 0.8(5.3) | 3.6(5.9) | 1.8(5.2) | 3.4(6.4) |
| U055.m | Weight change kg T12−T0 | 766 | −0.3(4.9) | −0.8(4.9) | −0.3(5.0) | −0.4(5.1) |
| U055.n | Weight percentage change from baseline | 766 | −0.1(5.4) | −0.8(5.6) | −0.3(5.6) | −0.5(5.6) |
| U055.o | Selenium change mcg/L, median(IQR) | 335 | 1(−6.3,7) | −1(−5,5) | 5(−5,13) | 5(−3,12) |
| U055.p | Folic acid change ng/mL, median(IQR) | 335 | −0.1(−1,1.3) | 0.4(−1.2,1.7) | 6.2(0.6,10.6) | 5.9(2.8,10) |
| U055.q | Vitamin D change ng/mL, median(IQR) | 335 | 0(−2.3,3.0) | 1(−2,5) | 7(3,13) | 6(1,11) |
| U055.r | EPA change mcmol/L, median(IQR) | 334 | 2.5(−11,20) | 3(−19,13) | 32(5,81) | 30.5(6.8,89.5) |

Footnotes printed: IQR=interquartile range, T0baseline/T12 12months. Single asterisk says averageMorisky over fourfollowups, calculated when≥1available follow-up, despite starred adherence labels. Double asterisk says kappa weight/self-report multinutrient.73/omega.70. Retain exact footnote associations for label checking. Unlabeled parentheses in diet/weight rows are presented as printed; narrative is compatible with summary dispersion but does not itself label SD at this table. Matching main: adherence rates, F-BA total count, hospitalization/death, weight/diet change, biomarker availability. No P values are supplied on this page.

### U056: Every panel and graphical definition

[DOC-004 p17](../../../joi190007supp3_prod.pdf#page=17), printedp16, Appendix9. Four panels PHQ, IDS, GAD, Utility; four colored conditions: red placebo/noBA, green placebo/BA, cyan supplements/noBA, purple supplements/BA. Xaxis labeled time with ticks0,3,6,9,12; distributions shown0,3,6,12, none at9. PHQaxis0/5/10/15/20/25; IDS0/10/20/30/40/50/60; GAD0/5/10/15/20; Utility0.0to1.0 at.1 increments. No exact printed means/medians/N values in graph. Caption defines innerline median, box25th–75thpercentiles, whiskers1.5IQR past quartiles, points otherobservations, diamondmeans connected bycondition, availabledata. Graphical trend: symptoms lower atfollowup acrossconditions; utility roughly stable/slightlyhigher. No exact inferredvalues replace table results.

### U057: Table A and moderation narrative

[DOC-004 p18](../../../joi190007supp3_prod.pdf#page=18), eAppendix10: no moderation of primary/secondaryoutcomes byMDDhistory; F-BA×baselinePHQ favorslargerdepressionreduction at higherbaseline; supplements×baselineGAD favorshigherfollowupanxiety at higherbaseline; F-BA×siteutilityeffectlargerUKvsNL. TableA outcomePHQ9at12months, B unstandardized bytablelabel,95%CI,P; NL reference. Every nonreference row:

| Local row key | Predictor | B | 95% CI lower | 95% CI upper | P |
|---|---|---:|---:|---:|---|
| U057.a | Supplements | 0.046 | −0.399 | 0.490 | .841 |
| U057.b | F-BA | 0.288 | −0.155 | 0.731 | .203 |
| U057.c | Spain | −0.480 | −1.161 | 0.202 | .168 |
| U057.d | UK | 0.275 | −0.373 | 0.923 | .405 |
| U057.e | Germany | 0.233 | −0.396 | 0.862 | .468 |
| U057.f | MDD history | −0.536 | −1.036 | −0.036 | .036 |
| U057.g | Baseline PHQ9 | 0.322 | 0.265 | 0.379 | <.001 |
| U057.h | F-BA×baselinePHQ9 | −0.064 | −0.118 | −0.01 | .020 |
| U057.i | Supplements×baselinePHQ9 | 0.032 | −0.023 | 0.086 | .259 |

Matching main moderationnarrative and primarysecondaryanalysisadjustments. Per-row CI/estimate/P relationship must retain outcome/time/modelcaveat; inferentialmethod not labeled directly inthis table.

### U058: Table B overall anxiety follow-up

[DOC-004 p19](../../../joi190007supp3_prod.pdf#page=19). B,95%CI,P; Netherlandsreference. Caption says overallanxietyseverityfollow-up, distinguish from12month-onlyA. Allrows visuallyconfirmed including displayzero:

| Local row key | Predictor | B | Lower | Upper | P |
|---|---|---:|---:|---:|---|
| U058.a | Supplements | −0.107 | −0.384 | 0.17 | .45 |
| U058.b | F-BA | −0.054 | −0.329 | 0.221 | .703 |
| U058.c | Spain | 0.107 | −0.424 | 0.520 | .694 |
| U058.d | UK | 0.117 | −0.371 | 0.638 | .637 |
| U058.e | Germany | 0.058 | −0.401 | 0.606 | .804 |
| U058.f | MDD history | −0.317 | −0.698 | 0.063 | .102 |
| U058.g | Baseline GAD7 | 0.464 | 0.409 | 0.52 | 0 |
| U058.h | F-BA×baselineGAD7 | −0.016 | −0.068 | 0.036 | .554 |
| U058.i | Supplements×baselineGAD7 | 0.062 | 0.009 | 0.115 | .022 |

P=0 atU058.g is mapped literally; it is finiteprecisionnotation and not a candidate byitself. Match higherbaselineanxiety interactionnarrative toU058.i, preservingoverallfollow-up scope.

### U059–U061: Table C1 and both C2 subgroups

[DOC-004 p20](../../../joi190007supp3_prod.pdf#page=20), healthutilityat12months, B95%CI/P. C1 NLreference forsite andinteractionterms; NLreferencerows have no estimate. Both subgroup tables printedC2 (retain literal titles).

| Local row key | Population/model | Predictor | B | Lower | Upper | P |
|---|---|---|---:|---:|---:|---|
| U059.a | Allsites C1 | Supplements | .000 | −.012 | .012 | .952 |
| U059.b | Allsites C1 | F-BA | −.006 | −.018 | .006 | .313 |
| U059.c | Allsites C1 | Spain | .005 | −.012 | .022 | .548 |
| U059.d | Allsites C1 | UK | −.014 | −.031 | .003 | .097 |
| U059.e | Allsites C1 | Germany | .011 | −.006 | .027 | .198 |
| U059.f | Allsites C1 | MDDhistory | .009 | −.003 | .022 | .148 |
| U059.g | Allsites C1 | Baselineutility | .498 | .438 | .558 | <.001 |
| U059.h | Allsites C1 | F-BA×Spain | .016 | −.001 | .032 | .066 |
| U059.i | Allsites C1 | F-BA×UK | .017 | .001 | .033 | .041 |
| U059.j | Allsites C1 | F-BA×Germany | .006 | −.01 | .022 | .452 |
| U059.k | Allsites C1 | Supplements×Spain | −.006 | −.023 | .011 | .499 |
| U059.l | Allsites C1 | Supplements×UK | −.001 | −.018 | .016 | .907 |
| U059.m | Allsites C1 | Supplements×Germany | .002 | −.014 | .017 | .850 |
| U060.a | UK C2 | Supplements | .000 | −.012 | .011 | .944 |
| U060.b | UK C2 | F-BA | .013 | .001 | .024 | .033 |
| U060.c | UK C2 | MDDhistory | .007 | −.016 | .03 | .559 |
| U060.d | UK C2 | Baselineutility | .738 | .62 | .856 | <.001 |
| U061.a | NL C2 | Supplements | .000 | −.012 | .012 | .935 |
| U061.b | NL C2 | F-BA | −.007 | −.019 | .005 | .267 |
| U061.c | NL C2 | MDDhistory | −.005 | −.031 | .021 | .697 |
| U061.d | NL C2 | Baselineutility | .509 | .400 | .619 | <.001 |

Matching moderatorcontrastUKvsNL atU059.i, subgroup directionsU060.b/U061.b. Rounding to.000 is a coefficient precision issue distinct from Pdisplayzero; no inventedexactzero.

### U062: Nonimputed secondary analyses, all 24 inferential results

[DOC-004 p21](../../../joi190007supp3_prod.pdf#page=21), printedp20, eAppendix11. Overallfollow-up usesallfollowups GEE andB95%CI,P. T12robustlinearregression B(SE),P, coefficients explicitly unstandardized. Bothinterventions andinteraction modeled together; adjustsite,MDDhistory,correspondingbaselineoutcome; effectcoded−1,+1. Refplacebo/noF-BA. Every row contains two distinct statisticalresults:

| Local row key | Outcome | Contrast | Overall B | 95% CI | Overall P | T12 B | T12 SE | T12 P |
|---|---|---|---:|---|---|---:|---:|---|
| U062.a | PHQ | Supplements | .30 | .11,.49 | .002 | .28 | .11 | .013 |
| U062.b | PHQ | F-BA | −.14 | −.34,.05 | .14 | −.22 | .11 | .052 |
| U062.c | PHQ | F-BA×supplements | −.01 | −.20,.18 | .94 | .02 | .11 | .84 |
| U062.d | IDS | Supplements | .55 | .11,.99 | .01 | .28 | .28 | .30 |
| U062.e | IDS | F-BA | −.26 | −.70,.18 | .25 | −.36 | .28 | .20 |
| U062.f | IDS | F-BA×supplements | −.01 | −.45,.43 | .96 | .12 | .28 | .66 |
| U062.g | GAD | Supplements | .24 | .08,.40 | .004 | .17 | .09 | .07 |
| U062.h | GAD | F-BA | −.16 | −.32,.00 | .06 | −.26 | .09 | .005 |
| U062.i | GAD | F-BA×supplements | .04 | −.13,.20 | .66 | .03 | .09 | .74 |
| U062.j | Utility | Supplements | −.006 | −.011,.000 | .055 | −.001 | .003 | .66 |
| U062.k | Utility | F-BA | .002 | −.004,.007 | .51 | .004 | .003 | .23 |
| U062.l | Utility | F-BA×supplements | −.002 | −.008,.003 | .42 | .001 | .003 | .65 |

Matching main imputed table only as sensitivity variant after distinguishing imputations; T12BSE here differs from any standardizedmain-effectscale. For stableS mapping use suffixoverall/T12, i.e.U062.a.overall andU062.a.T12, etc.

### U063: All eight CACE results

[DOC-004 p22](../../../joi190007supp3_prod.pdf#page=22), printedp21, eAppendix12. MI data, adjustmentsite/MDDhistory; MDDlogisticanyfollowup; continuousPHQ/IDS/GAD ANCOVA12months adjustedbaseline. Interventions effectcoded−1,+1. F-BA≥8/21sessions; supplementcomplianceomega≥70%. Star*P<.05,**P<.01; onlysinglestarsprinted onthreecells.

| Local cell key | Outcome and measure | Intervention | Estimate | 95% CI | Printed star |
|---|---|---|---:|---|---|
| U063.a | MDD onset OR | F-BA | .78 | .64,.95 | * |
| U063.b | MDD onset OR | Supplements | .84 | .67,1.07 | none |
| U063.c | PHQ B | F-BA | −.22 | −.59,.15 | none |
| U063.d | PHQ B | Supplements | .43 | .08,.77 | * |
| U063.e | IDS B | F-BA | −.42 | −1.24,.40 | none |
| U063.f | IDS B | Supplements | .47 | −.33,1.27 | none |
| U063.g | GAD B | F-BA | −.31 | −.60,−.02 | * |
| U063.h | GAD B | Supplements | .18 | −.11,.47 | none |

Matching mainCACEparagraphs andU054 formula; OR versusB andeffectcodingmuststayexplicit.

### U064: Concealment table, all cells and inferential statement

[DOC-004 p23](../../../joi190007supp3_prod.pdf#page=23), printedp22, eAppendix13, n759. SameA/B/C/DcolumnorderasU055; valuesn(%).

| Local row key | Believed assignment | A | B | C | D |
|---|---|---|---|---|---|
| U064.a | Placebo | 95(48.7%) | 84(43.5%) | 66(35.1%) | 43(23.5%) |
| U064.b | Multinutrient | 16(8.2%) | 20(10.4%) | 48(25.5%) | 80(43.7%) |
| U064.c | Do not know | 84(43.1%) | 89(46.1%) | 74(39.4%) | 60(32.8%) |

Derived denominators fromprintedcountssum: A195,B193,C188,D183; total759. These sums arederivedmapping aids,not additional printedresults. PrintedP<.001, testunspecifiedonthistable; matchmainconcealmentparagraphprecisely ratherthanassumingPistwo-groupcomparison.

## Cross-location matching index

| Key | PLAN locations | REPORT locations | Main-paper semantic key | Required alignment |
|---|---|---|---|---|
| Eligibility | DOC-002p16/29/33 | DOC-004p3 | Methods eligibility and Figureflow | Age/BMI/PHQ, diagnosiswindow, actualpopulation |
| Dose | DOC-002p8/18/20/23–25 | DOC-004p4–5 | Intervention supplementation | DeclareddailyEPA+DHA mass vs FAMEcomposition, nutrientunits |
| Therapy | DOC-002p8/9/19 | DOC-004p6/8–9/12/16 | F-BA delivery/compliance | Sessionsvsminutes; individual/group;availabledenominator |
| Primary outcome | DOC-002p8/28/43;DOC-003p2–4 | DOC-004p3/22 | MDD primary/logistic/survival | DSMlabel, cumulativetimewindow, primaryvssecondarymodel |
| Secondary symptoms | DOC-002p9/28/35/43;DOC-003p2–3 | DOC-004p7/17–22 | PHQ/IDS/GAD/utility | Time, imputation, adjustment, standardizedvsunstandardized |
| Sample size | DOC-002p15–17 | DOC-004p16/23 | Power/randomizedN/flow | Plannedvsobserved;4factorialcellsvs2main-effectgroups |
| Missingness | DOC-003p5 | DOC-004p16/21–22 | Missing outcomes/MI |100datasets,MAR,Rubin,availablecasevsMI |
| CACE | DOC-003p4 | DOC-004p12/14–16/22 | CACE estimates andgoodadherence |≥70%,≥8/21,originalestimatescale,OR/ANCOVAeffectcoding |
| Moderation | DOC-002p44;DOC-003p4–5 | DOC-004p18–20 | Effectmodificationnarrative | History/site/severity,overallfollowupvs12month |
| Diet score | DOC-002p28/35 | DOC-004p6/12/16 | Dietquality/change | Tenrecommendedfoodgroupsvselevenscorecomponents;range0–77 |
| Blood counts | DOC-002p9/36–37 | DOC-004p12/16 | Nutrientmeasurementpopulation | Pairedbaseline/T12,analyte-specificN,center/time |
| Adverse events | DOC-002p40–42 | DOC-004p13/16 | Seriousadverseevents | Personshospitalizedvsepisodes,countnotrate |
| Concealment | DOC-003p3 | DOC-004p13/23 | Blindingsuccess | n759/4columns/3responses andtestdefinition |

The index identifies relationships to compare; it contains no candidate claims. All65PLANpages were opened including administration andbibliography. All26REPORTsupportpages were opened includingreferenceanddatasharing content.

## Complete page-delimited transcription parts

The full source transcriptions are preserved in two disjoint files below. Each transcription has a physical page heading and truthful PDF link. They preserve source values/spelling as transcription aids; direct source remains authoritative. Canonical map and source page transcriptions together contain every quantitative relationship without filtering. Every fresh native/layout derivative remains available in preprocessing.

- [PLAN transcriptions](parts/support_plan_transcriptions.md): DOC-002 physical pages1–60 and DOC-003 pages1–5, exactly65 units.
- [REPORT transcriptions](parts/support_report_transcriptions.md): DOC-004 physical pages1–25 and DOC-005 page1, exactly26 units.

No context shard exceeds200000 characters: canonical map under50000 bytes; PLAN transcription under150000 bytes; REPORT transcription under100000 bytes. The split does not omit or sample any source page. Mapped source counts remain91/91; fresh native/layout pages81/81; reusable newly mapped pages10/10.

Coordinator reconciliation after statistical pass 1: protocol physical p9's IDS bullet continues the main-endpoint list begun on p8. U002 records those values and should be read as main-endpoint context, not a secondary designation. Protocol p14 still lists depressive symptoms in secondary objectives. Exact source transcriptions are unchanged; the rechecker must confirm the hierarchy on all compared pages. This source-linked clarification came from fresh pass-1 direct inspection, not a legacy classification.

## Complete visual-content repair: U065

The fresh bounded mapper's [support PLAN p26 visual repair](parts/support_plan_p26_visual_repair.md) is incorporated in this canonical map by complete source-linked reference. U065.a–h records every quantity and operational label in the two protocol p26 product-label panels omitted by native extraction. All four support PDFs received complete raster-object inventories; protocol/SAP cover images were freshly inspected and contain logos only. No additional scientific raster gap remains. The support union is now U001–U065; original U001–U064 and the 91-page coverage ledger are preserved. Exact labels, quantities, role PLAN, source authority and direct derivative engines are in the repair part.
