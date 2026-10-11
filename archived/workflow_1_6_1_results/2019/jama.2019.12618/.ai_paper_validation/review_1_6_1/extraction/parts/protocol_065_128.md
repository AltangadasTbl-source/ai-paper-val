# DOC-003 support mapping: PDF pages 65–128

Document role: PLAN, by content: FAST Manual of Operation and Procedures, January 6, 2017 version 4.5. Exact source: `joi190092supp2_prod.pdf`; printed manual page = PDF page minus 64. Scope: all 64 PDF pages; 49 reusable-backed and 15 fresh-required. Mapping is extraction only; no candidate diagnosis. No workbook, CSV, formula cache, or reported trial result table exists in this shard. All content including administrative and measurement procedures was opened. Complete page transcriptions below retain every numeric entry, table, label, footnote and operational example; the interpretive map identifies matching main-paper keys without making comparisons.

## Tool provenance and fresh visual confirmation

Reusable assets: `.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp065_096_layout.txt` and `protocol_pp097_128_layout.txt`, source-matched Poppler layout, split at form feeds with AWK. Direct engines: Poppler pdftotext/pdftoppm 26.01.0; Tesseract 5.5.0 CPU OCR. No fallback environment. For each N = 74, 80, 81, 84, 89, 90, 91, 94, 96, 105, 107, 109, 116, 118, 120, commands executed:

```bash
pdftotext -layout -f N -l N joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_b/page-N-layout.txt
pdftoppm -r 120 -f N -l N -singlefile -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_1/preprocessing/protocol_b/page-N
tesseract .ai_paper_validation/review_1_6_1/preprocessing/protocol_b/page-N.png .ai_paper_validation/review_1_6_1/preprocessing/protocol_b/page-N-ocr -l eng --psm 6
```

Every fresh page was visually viewed from its new PNG. Native/layout text on these pages is empty; OCR is a locator/transcription aid, with visual readings recorded in the map. None is blank. Page 96 table columns and X/(x) cells require the PNG for exact table positioning; below its schedule is described directly from the rendered source. Existing reusable assets and sources are unchanged.

## Page-level coverage and quantitative map

Every row status is COMPLETE. R = reusable layout read; F = fresh layout, render, visual reading and CPU OCR. Links are relative to this shard artifact.

| PDF page | Basis | Content / quantitative relationships and matching result key | Status |
|---:|---|---|---|
| 65 | R | Contents: design, primary endpoint, treatment, visits; navigation only, no applicable estimate/test. | COMPLETE |
| 66 | R | Contents: refraction, inflammation, OCT, adverse events, data analysis; navigation only. | COMPLETE |
| 67 | R | Contents: organization and appendices; no applicable quantitative result. | COMPLETE |
| 68 | R | Personnel and study sites; no applicable statistical relationship. | COMPLETE |
| 69 | R | Personnel continued; no applicable statistical relationship. | COMPLETE |
| 70 | R | DSMC and NEI personnel; no applicable statistical relationship. | COMPLETE |
| 71 | R | Background incidence >50/100000 person-years; prevalence approximately 115/100000; up to 10% legal blindness;30000 new blindness/year; approximately half switch successes. Historical context, no trial estimates. | COMPLETE |
| 72 | R | Planned 216 randomized patients; monthly follow-up 6 months; success continues another 6 months, failures switch and follow another 6 months. Primary proportion success at 6 months; secondary VA, macular thickness, time to inflammation control, anatomic subgroup efficacy, tolerability, QoL, AE. | COMPLETE |
| 73 | R | Observer masked, site block randomization,216 total/108 per arm. Primary overall success 6 months with controlled inflammation,7.5 mg/day prednisone and≤2 drops/day 1% prednisolone. Secondary success after switching 6 months; time to control/success;5 month success sustained≥28 days to 6 months;12 month success; corticosteroid discontinuation 6–12 months; BSCVA, macular edema/thickness, vitreous haze NEI/Miami, anatomic/vasculitis subgroup, intolerance, AE rate, SAE discontinuation,QoL. | COMPLETE |
| 74 | F | Visual: secondary dose reduction,VKH efficacy;2 step reduction from≥2+ cells/haze (2+→0.5+,3+→1+,4+→2+); from≥1+ to 0; stricter controlled inflammation 0 cells/0 haze; injection proportions for severe inflammation/mac edema. Table 1 administrative timeline 2011–2018,6 month and 12 month follow-up plus 1 month windows. | COMPLETE |
| 75 | R | SUN anatomical classification: intermediate vitreous; posterior retina/choroid; panuveitis no predominant site; anterior+intermediate distinct from panuveitis; macular edema does not change category; intermediate vasculitis remains intermediate. Main key: anatomic subgroup population. | COMPLETE |
| 76 | R | Inclusion:≥2+ cells/haze or retinal/choroidal inflammation within 180 days;≥1+ at enrollment; corticosteroid-sparing need criteria 4 weeks 1 mg/kg,≥1 grade rebound 180 days,10 mg/day≥90 days,injection 4–180 days, specified diagnoses; prednisone min(1 mg/kg,60 mg). | COMPLETE |
| 77 | R | Exclusion: prior immunosuppression 12 months,age<16, bilateral IOP<5 mmHg>3 months,injection<4 weeks,implant<3 years,surgery<30 days/planned 180 days; labs WBC≤2500,platelets≤75000,Hb≤9,ALT/AST≥2 ULN,creatinine≥1.5 within 4 weeks; screening 90 days. Main key: enrolled population and safety definitions. | COMPLETE |
| 78 | R | Equal-arm block randomization by site, biostatistician-generated lists, concealed future allocation in REDCap. | COMPLETE |
| 79 | R | Patients/coordinators unmasked; ophthalmologists,VA,OCT,photographers,graders masked; site ID digits 1–9,5 character identifier; administrative IDs not analysis denominators. | COMPLETE |
| 80 | F | Visual primary endpoint: both eyes controlled at 6 month,7.5 mg/day prednisone,≤2 drops/day 1%prednisolone,no periocular/intravitreal injections after 90 days,and no failure at any point due safety,tolerability,futility. Table 2 cells≤0.5+,NEI haze≤0.5+,no active choroid/retina inflammation or retinal vasculitis posterior to equator; cystoid macular edema alone insufficient. Stopping drug alone not failure. Futility may be declared any time; increasing early inflammation alone not failure. | COMPLETE |
| 81 | F | Visual: intolerance failure without mandatory dose reduction. Safety: nonserious lab abnormalities allowed 28 days to resolve,repeat labs 1–2 weeks; persisting 28 days→SAE/failure. Table 3 WBC nonserious>1000 to<2500/µL,SAE≤1000;platelets 20000–75000/µL,SAE<20000;Hb≥6.5 to<9 g/dL,SAE<6.5;AST/ALT 2 to<5 ULN,SAE≥5 ULN;creatinine≥1.5 to<2 mg/dL,SAE≥2. Nonlaboratory SAE relatedness decided by Medical Monitor;6 month follow-up still collected. | COMPLETE |
| 82 | R | Dropout only unwilling further visits or death; related death=failure,unrelated death=dropout. Drug discontinuation/missed visits alone noncompliant,not dropout;encourage 6 month follow-up after failure in both phases. | COMPLETE |
| 83 | R | Primary endpoint flowchart:monthly efficacy/tolerability/safety;6 month success→PhaseI 6–12,otherwise switch→PhaseII 6 months;intolerance two dose reductions;controlled cells/haze≤0.5+,noactive choroid/retina lesions;at 12 month/PhaseII 6 month≤7.5 mg prednisone,≤2 drops/day. | COMPLETE |
| 84 | F | Visual Tables 4–5: MTX introductory 7.5 mgBID one day/week=15 mg/week;maintenance 12.5 mgBID one day/week=25 mg/week. MMF 500 mgBID daily weeks 1–2,1.5 gBID daily afterwards. MTX reductions 10 mgBID weekly=20 mg/week then 7.5 mgBID weekly=15 mg/week;MMF 1 gBID then 500 mgBID. Folic acid 1 mg/day even reduced MTX. | COMPLETE |
| 85 | R | MTX 15 mg/week first 2 weeks,25 mg/week after;split morning/evening once weekly;start within 6 days. Reductions 20 then 15 mg/week optional;failure for unwilling/unable tolerability, safety or efficacy. | COMPLETE |
| 86 | R | MMF 500 mgBID 2 weeks→1.5 gBID;empty stomach±1 hour;reductions 1 gBID then 500 mgBID;follow 6 months even intolerance failure;maintenance re-escalation discretionary. | COMPLETE |
| 87 | R | Folic acid 1 mg/day;14 day intro MTX 12 pills,MMF 28 pills;maintenance bottles 50/100 pills;monthly supply MTX 50/MMF 200 pills;120 day supply at 6 month;packaging context. | COMPLETE |
| 88 | R | Adherence diaries,pill counts,self-estimated missed doses;MTX make-up next day otherwise nextweek;MMF regular schedule. Prednisone min(1 mg/kg,60 mg),2–4 weeks then taper/hold 7.5 mg/day first 6 months. | COMPLETE |
| 89 | F | Visual Table 6: prednisone 60 mg 2–4 weeks then 50,40,35,30,25,20,17.5,15,12.5,10 each 1 week then 7.5 hold;decrements 10,10,5,5,5,5,2.5,2.5,2.5,2.5,2.5 mg/day. MTX/MMF effect 6–8 weeks;faster taper/less 7.5 allowed medically necessary;6–12 month optional steroid cessation. | COMPLETE |
| 90 | F | Visual Table 7 optional 6–12 month prednisone:7.5 mg 1 week decrement 2.5;<7.5≥5 mg 2–4 weeks decrement 1–2.5;<5≥2.5 mg 2–4 weeks decrement 1.5–2.5;<2.5≥1 mg 2–4 weeks decrement 1;0. Mild reactivation≤1+,severe≥2+;rescue severe 1 mg/kg,mild up to double dose;nonresponsive after 4 weeks 1 mg/kg,hold 1 moreweek then futility possible;retain 6 month assessment. | COMPLETE |
| 91 | F | Visual calcium 500 mg 3 times/day,vitD 400–800 IU/day. Table 8 topical 1 drop 8–10/day 1–2 weeks,then 6,4,3,2,1/day each 1 week thennone. Success≤2/day 1%prednisolone-equivalent. One mac edema injection first 90 days per phase,perioculartriamcinolone 40 mg/intravitreal 4 mg;other injections protocol deviation. | COMPLETE |
| 92 | R | Adjunctive IOP/cycloplegic allowed;IV/extra immunosuppression/surgery deviation. Enrollment and study assessment sequence;SF 36 all participants. | COMPLETE |
| 93 | R | NEIVFQ 25 all,INDVFQ Indian;masked study procedures;VA/slitlamp/IOP before dilation;REDCap double entry. PhaseI failure<6 months switches to PhaseII. | COMPLETE |
| 94 | F | Visual Table 9:week 2±3 days,months 1–5±15 days,month 6−15 to+30 days;Table 10 month 9±15 days,month 12−15 to+30 days. Baseline eye exam≤14 days pre-randomization,lab 4 weeks/90 days;minimum 2 weeks betweenvisits. PhaseII alternate treatment followed 6 months/untilfailure;SAE may preclude switch but 6 month data retained. | COMPLETE |
| 95 | R | PhaseII startwithin 2 weeks of failure;day 1=BaselineII;minimum 2 weeks betweenvisits;non-study failure collectforms andstillfollow 6 months. | COMPLETE |
| 96 | F | Visual matrix:PhaseI baseline,week 2,months 1–5/9,failureanytime,months 6/12;PhaseII baselineII,week 2,months 1–5,failureanytime,month 6. Eligibility/consent/history baselineI;clinicaleye atbaselineI,followups/failure/endpoints;secondaryeye atbaselineI,failure/endpoints;VA/OCT atbaselineI,followups/endpoints andconditionalfailure;fundusbaselineI,endpoint,conditionalfailure;labsbaselineI/week 2/followups/endpoints,baselineII/week 2;AEchecklist week 2/followups/failure/endpoints inbothphases. QoLbaselineI,failure,endpoints;TreatmentAssessment andMedicationLog allvisits;calendar exceptbaselines. Dropout/deviation/AEnarrative/logconditionalallvisits. Footnotes(x)=ifapplicable;failurecanoccuratnonstudyvisit;BaselineIIpacketifnot samedayasPhaseIfailure. | COMPLETE |
| 97 | R | Baseline eye exam≤14 days beforeenrollment;inflammationeligibilitycanusethe 14 dayperiod despite improvementbeforeenrollment. Screening labs 4 weeks/90 days. Randomize onlyaftereligibilityverified. | COMPLETE |
| 98 | R | Consentthenrandomization;required medicalhistory,eyeexam,VA,OCT,fundus,labs,QoL;CBC/chemistry/pregnancy within 4 weeks,infectiousscreening 90 days. | COMPLETE |
| 99 | R | Followupdataregardlessofwindow;PhaseI 6–12 month studyrecordmonth 9/12 or failure;monthlylabs. Secondaryeye/fundus/QoL atfailure/6 month/12 month;CD 4 atbaseline 3,6,12 months selectedsites. | COMPLETE |
| 100 | R | Formsregardlessofadherence;PhaseIIstart≤2 weeks;relatedSAEmedicalmonitordecision forsafeswitch otherwise 6 monthfollowup. | COMPLETE |
| 101 | R | Nonstudyvisits minimumclinicalexam iffailing,no mandatoryspecimens;attemptallprocedures andQoL,medication,AEforms. | COMPLETE |
| 102 | R | QoLSF 36,NEIVFQ 25 all;INDVFQIndian;baseline,6 months/failurewhicheverfirst,and 12 monthscontinuers;failurebefore 6 monthsalsocollect 6 month. Letterchartrefraction 4 m;contactlenswait 30 minutes. | COMPLETE |
| 103 | R | LetterChartR 2110;VA<20/200 (miss≥2 largestline)refraction 1 m. Lens table:20/10–20/80 sphere+0.50/−0.37 increments+0.50/−0.25,cylinderaxis 0.50/power 0.25/refinement±0.37 increments±0.25;20/100–20/200 sphere±1,cylinder 1,refinement±0.50;below 20/200 sphere±2,cylinder 1,refinement±1. | COMPLETE |
| 104 | R | Letterrefractiongoodacuity:sphere+0.50/−0.37 steps−0.25;cylinder±0.50,90°/180°,45°/135°,axis±45°,initialrotate 15°. | COMPLETE |
| 105 | F | Visualaxisstep table<1 D 10°,1–<2 D 5°,2–<3 D 3°,3–<5 D 2°,5–<8 D 1°. Cylinder±0.25 D;from 1 D,each 0.5 D cylinderchange sphere 0.25 Doppositesign preserves spherical equivalent;refinement±0.37,steps±0.25. | COMPLETE |
| 106 | R | LetterVA 20/100–20/200 sphere±1,cylinder±1;90/180 and 45/135 degrees;useacuityappropriatelenses. | COMPLETE |
| 107 | F | Visual repeated axis step table as 105;cylinder±1;0.5 D/0.25 Dsphericalequivalent;refinement±0.50 D. | COMPLETE |
| 108 | R | LetterVA<20/200 move 4→1 m;add+0.75 D sphere for distance;±2 D sphere,±1 D cylinder. | COMPLETE |
| 109 | F | Visual repeated axis step table as 105;±1 Dcylinder;0.5 D/0.25 Dsphericalequivalent;refinementstart+1 D. | COMPLETE |
| 110 | R | Letterrefinement±1 D;separate eyes;3 charts 14 lines;logMAR progression;chartlabels 2110/2111/2112;0.8 logMAR=45 letters=20/125 Snellen. | COMPLETE |
| 111 | R | Letterboxlighting≤15 footcandles,2×20 W,tubeloss 5%100 h+5%2000 h,preburn 96 h;testlanes 4 mand 1 m;operationalmeasurementsretainedbelow. | COMPLETE |
| 112 | R | LetterVAeachvisitafterrefraction;testseparateeyes;oneanswerperletter;<20 lettersat 4 m→1 mfirst 6 rows;0 letters 1 m→lowvision;countfingers 1/2/5,5 trials,3/5 at 1 m. | COMPLETE |
| 113 | R | Handmotion 0.5 m,1 cycle/sec,4/5;lightperception 0.5 m 4 presentations. Snellenequivalentmostdifficultline≥4/5;biostatisticiancalculatesscore. | COMPLETE |
| 114 | R | Certification 18±2 months,≥2 technicians/site. TumblingEChartR 2305 b;4 m/1 msame 20/200 largestlinethreshold;contactlens 30 min. | COMPLETE |
| 115 | R | TumblingElensguide sameacuityband/increments aslettertable 103,±0.50/−0.37 forgoodacuity;90°/180°axistesting. | COMPLETE |
| 116 | F | Visual±0.50 cylinder,45°/135°,±45°flips,15°initialrotation;axissteptableas 105;±0.25 power;0.5 D/0.25 Dsphericalequivalent. | COMPLETE |
| 117 | R | TumblingEgoodacuitysphericalrefinement±0.37 steps±0.25;20/100–20/200±1 sphere;trial-lensadjustforimprovedVA. | COMPLETE |
| 118 | F | Visual±1 cylinder 90°/180°,45°/135°,±45°flips,15°initialrotation;axissteptableas 105;±1 power;0.5 D/0.25 Dsphericalequivalent. | COMPLETE |
| 119 | R | TumblingErefinement±0.50;VA<20/200 move 1 m/add+0.75 sphere,±2 Dsphere. | COMPLETE |
| 120 | F | Visual±1 cylinder 90°/180°,45°/135°,±45°flips,15°initialrotation;axissteptableas 105;±1 power. | COMPLETE |
| 121 | R | TumblingEcylinder 0.5 D→sphere 0.25 Doppositesign;refinement±1 D;3 charts 14 lines 2305/2305 a/2305 b;rightchart 1/leftchart 2. | COMPLETE |
| 122 | R | TumblingEbox/lighting/4 m 1 mlanes sameoperationalunitsas 110–111;0.8 logMAR=45 letters=20/125. | COMPLETE |
| 123 | R | TumblingEeachvisitafterrefraction;separate eyes;stoprowif≤3 responsesfromrow 3 below;<10 letters 4 m→1 mfirst 6 rows;<10 letters 1 m→lowvision. | COMPLETE |
| 124 | R | Countfingers 3/5 at 1 m,handmotion 4/5 at 0.5 m,lightperception 4 presentations. Printed scoring:if≥10 letters of firstline at 4 m,score=4 mcount+30;if≤3 largestline 4 m,score=1 mcount;if≤3 letters 1 m,lowvision. Literal text retained;no interpretation imposed. | COMPLETE |
| 125 | R | Highest 4 mscore 100;lowvisionconvertedlogMARusingcalculationtable;Snellen≥4/5 mostdifficultline;certification 18±2 months,2 technicians;AREDSopacity 1 presence/2 significance/3 severe,halfgrades. | COMPLETE |
| 126 | R | Cataractcategories<1,1,1.5,2,2.5,>3. Primarycellscale 0<1 cell,0.5+1–5,1+6–15,2+16–25,3+26–50,4+>50;field 1×1 mm highest magnification and illumination before dilation. | COMPLETE |
| 127 | R | Flare 0 none,1 faint,2 moderate,3 marked,4 intense excludedfromcontrolledinflammation. Vitreouscell 0 none,0.5+0–5,1+6–10,2+11–20,3+21–50,4+>50,field 1×0.5 mm,alsoexcluded. NEIhaze allprimary/secondary;Miami 9 pointexploratorycorrelation/photograding. | COMPLETE |
| 128 | R | Figure 1 NEIhaze 0 clear,0.5+slightdiscblur,1 opacitieswithoutretinalobscuration,2 milddetailblur,3 disc/vesselsblurredstillvisible,4 denseopacityobscuresdisc. Mainkey: inflammationcontrolendpoint. | COMPLETE |

## Source-grounded relationships for matching

- Planned population and design: pages 72–79 patient-level 216/108, site block randomization, masking; match main Methods study design, inclusion and analysis population.
- Primary success definition: pages 73,80–83; controlled bilateral inflammation at 6 months, steroid doses, injection 90 daycondition, safety/tolerability/futility; match main primary endpoint and treatment failure subtypes.
- Randomized intervention: pages 84–91 doses, reductions, prednisone/topicaltaper and injectionpolicy; match main randomized doses, adherence and dose reductions.
- Follow-up windows and missing observation distinctions: pages 82,94–101; dropout/noncompliance distinction, failure follow-up, windows; match main follow-up and analysis population.
- Secondary outcomes and subgroup definitions: pages 72–75,102–128; anatomic/VKH/vasculitis efficacy, macular edema/thickness, vision scales,NEI/Miami,QoL; match main secondary outcomes and anatomic treatment interactions.
- No sample-size power formula, hypothesis test, confidence level, multiplicity/stopping significance boundary, or fitted statistical analysis specification is stated in these assigned pages. Sample count/design definitions are extracted rather than inferred. Prospective measurement and operational definitions are PLAN material, not reported outcomes.

## Complete per-page locator/transcription evidence

The following blocks retain the full assigned reusable layout or fresh OCR, paired with exact PDF page links. Fresh OCR can contain character substitutions; visually read map above and the source PNG take precedence, especially tables and inequality signs. No OCR normalization has been silently applied.

### DOC-003 PDF page 65

[Direct source](../../../../joi190092supp2_prod.pdf#page=65)

```text
  First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                                           January 6, 2017 - Version 4.5
  Manual of Operation and Procedures


                                                              TABLE OF CONTENTS


INVESTIGATORS, PERSONNEL AND STUDY SITES ....................................................................................4
DATA SAFETY AND MONITORING COMMITTEE (DSMC) MEMBERS .........................................................6
NATIONAL EYE INSTITUTE (NEI) PROGRAM OFFICER ...............................................................................6
BACKGROUND .................................................................................................................................................7
1. INTRODUCTION TO TRIAL ..........................................................................................................................8
   1.1. RESEARCH QUESTION .................................................................................................................................8
   1.2. SPECIFIC AIMS ............................................................................................................................................8
2. TRIAL DESIGN ..............................................................................................................................................9
   2.1. DESIGN SUMMARY ......................................................................................................................................9
   2.2. STUDY TIMELINE .......................................................................................................................................10
   2.3. ELIGIBILITY ...............................................................................................................................................11
     2.3.1. Anatomical location of inflammation ................................................................................................11
     2.3.2. Inclusion Criteria ..............................................................................................................................12
     2.3.3. Exclusion criteria .............................................................................................................................13
     2.3.3.a. Screening for Active Tuberculosis ................................................................................................13
   2.4. RANDOMIZATION AND MASKING..................................................................................................................14
   2.5. DEFINITIONS FOR PRIMARY ENDPOINT ........................................................................................................16
     2.5.1. Determination of Treatment Success/Failure ..................................................................................16
     2.5.2. Treatment failure .............................................................................................................................16
     2.5.3. Dropouts, Non-Compliant Patients and Follow-up ..........................................................................18
     2.5.4 Primary Endpoint Flowchart .............................................................................................................19
3. TREATMENT PLAN .....................................................................................................................................20
   3.1. STUDY DRUGS ..........................................................................................................................................20
     3.1.1. Methotrexate ...................................................................................................................................21
     3.1.2. Mycophenolate Mofetil ....................................................................................................................22
     3.1.3. Folic acid .........................................................................................................................................23
     3.1.4. Packaging and distribution of study medications ............................................................................23
     3.1.5. Adherence to the treatment plan .....................................................................................................24
   3.2. CORTICOSTEROID THERAPY ......................................................................................................................24
     3.2.1. Oral prednisone ...............................................................................................................................24
     3.2.2. Supplements ...................................................................................................................................27
     3.2.3. Topical corticosteroid ......................................................................................................................27
     3.2.4. Periocular and Intravitreal Injections ...............................................................................................27
     3.2.5 Other adjunctive treatments/procedures ..........................................................................................28
   3.3. STUDY PROCEDURES ................................................................................................................................28
4. STUDY VISITS .............................................................................................................................................29
   4.1. VISIT SCHEDULES .....................................................................................................................................29
     4.1.1. Phase I: First-line treatment ............................................................................................................29
     4.1.2. Phase II: Rescue treatment .............................................................................................................30
     4.1.3. Non-study visits ...............................................................................................................................31
   4.2. STUDY FORMS COMPLETION SCHEDULE ......................................................................................................32
   4.3. PHASE I ENROLLMENT/BASELINE VISIT.......................................................................................................33
     4.3.1. Consent and eligibility evaluation ....................................................................................................33
     4.3.2. Randomization ................................................................................................................................34
     4.3.3. Procedures for data collection .........................................................................................................34
     4.3.4. Specimens .......................................................................................................................................34
     4.3.5. Forms for data collection .................................................................................................................35
   4.4. FOLLOW-UP VISITS....................................................................................................................................35
     4.4.1. Procedures for data collection .........................................................................................................35
     4.4.2. Specimens .......................................................................................................................................35


```

### DOC-003 PDF page 66

[Direct source](../../../../joi190092supp2_prod.pdf#page=66)

```text
  First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                                           January 6, 2017 - Version 4.5
  Manual of Operation and Procedures


     4.4.3. Forms for data collection .................................................................................................................36
   4.5. BASELINE PHASE II ...................................................................................................................................36
     4.5.1. Eligibility...........................................................................................................................................36
   4.6. NON-STUDY VISITS....................................................................................................................................37
     4.6.1. Study Procedures ............................................................................................................................37
     4.6.2. Specimens .......................................................................................................................................37
     4.6.3. Forms for data collection .................................................................................................................37
5. STUDY EXAMINATIONS AND PROCEDURES..........................................................................................38
   5.1. QUALITY OF LIFE QUESTIONNAIRE ADMINISTRATION ....................................................................................38
   5.2.A REFRACTION AND VISUAL ACUITY (PROTOCOL – FOR LETTER VISION CHARTS) .............................38
     5.2.1.A Refraction procedure ....................................................................................................................38
     5.2.2.A Visual acuity procedure.................................................................................................................46
     5.2.3.A Visual acuity training and certification ...........................................................................................49
   5.2.B REFRACTION AND VISUAL ACUITY (PROTOCOL – FOR TUMBLING E CHART) .....................................50
     5.2.1.B Refraction procedure ....................................................................................................................50
     5.2.2.B Visual acuity procedure.................................................................................................................57
     5.2.3.B Visual acuity training and certification ...........................................................................................61
   5.3. OPHTHALMIC PROCEDURES .......................................................................................................................61
     5.3.1. Grading Cataracts ...........................................................................................................................61
     5.3.2. Grading inflammation ......................................................................................................................62
     5.3.3. Inter-observer variation of ocular inflammation ...............................................................................65
     5.3.4. Training and certification of ophthalmologists and study coordinators ...........................................65
   5.4. OPTICAL COHERENCE TOMOGRAPHY .........................................................................................................66
     5.4.1. Required patient assessments—Heidelberg Spectralis ..................................................................66
     5.4.2. Scan procedures—Heidelberg Spectralis .......................................................................................66
     5.4.3. Obtaining retinal thickness data—Heidelberg Spectralis ................................................................67
     5.4.4. Saving/Exporting data—Heidelberg Spectralis ...............................................................................67
     5.4.5. Required patient assessments—Zeiss Cirrus .................................................................................69
     5.4.6. Scan procedures—Zeiss Cirrus ......................................................................................................69
     5.4.7. Obtaining retinal thickness data—Zeiss Cirrus ...............................................................................70
     5.4.8. Saving/Exporting data—Zeiss Cirrus ..............................................................................................70
     5.4.9. OCT operator qualifications.............................................................................................................70
   5.5. FUNDUS PHOTOGRAPHY ...........................................................................................................................71
   5.6. LABORATORY MEASUREMENTS ..................................................................................................................71
6. ADVERSE EVENTS ....................................................................................................................................72
  6.1. NON-SERIOUS ADVERSE EVENT (AE) .........................................................................................................72
  6.2. SERIOUS ADVERSE EVENT (SAE) ..............................................................................................................72
  6.3. ADVERSE EVENT REPORTING.....................................................................................................................72
  6.4. PATIENT DEATH ........................................................................................................................................73
7. DATA COLLECTION AND MANAGEMENT ..............................................................................................73
  7.1. DATA COLLECTION FORMS ........................................................................................................................73
  7.2. DATA REVIEW...........................................................................................................................................74
  7.3. DATA ENTRY.............................................................................................................................................74
    7.3.1. Data entry errors ...........................................................................................................................74
    7.3.2. Data consistency and validity ........................................................................................................74
    7.3.3. Data preparation and cleaning ......................................................................................................75
    7.3.4. Monitoring ......................................................................................................................................75
  7.4. DATA ANALYSIS ........................................................................................................................................75
  7.5. DATA STORAGE AND SECURITY ..................................................................................................................75
8. QUALITY CONTROL ...................................................................................................................................76
   8.1. MEDICATION STORAGE AND EXPIRY ...........................................................................................................76
   8.2. PERIODIC REPORTS ..................................................................................................................................76
   8.3. DATA MANAGEMENT, SECURITY AND QUALITY ASSURANCE ..........................................................................77
   8.4. MONITORING COMPLIANCE ........................................................................................................................77
   8.5. CERTIFICATION ........................................................................................................................................77


```

### DOC-003 PDF page 67

[Direct source](../../../../joi190092supp2_prod.pdf#page=67)

```text
  First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                                         January 6, 2017 - Version 4.5
  Manual of Operation and Procedures


   8.6. DATA AUDITS ............................................................................................................................................77
9. DUTIES AND RESPONSIBILITIES OF STAFF ...........................................................................................77
   9.1. OPHTHALMOLOGIST ..................................................................................................................................77
   9.2. CLINICAL TRIAL MANAGER ........................................................................................................................77
   9.3. STUDY COORDINATOR ..............................................................................................................................77
   9.4. DATA ANALYST .........................................................................................................................................78
   9.5. DATA ENTRY OPERATOR ..........................................................................................................................78
   9.6. BIOSTATISTICIAN (PROCTOR) ....................................................................................................................78
   9.7. OPHTHALMIC ASSISTANTS.........................................................................................................................78
   9.8. REFRACTIONISTS ......................................................................................................................................78
   9.9. OCT OPERATORS ....................................................................................................................................78
   9.10. FUNDUS PHOTOGRAPHERS .....................................................................................................................79
   9.11. THE READING CENTER ...........................................................................................................................79
10. STUDY ORGANIZATION ...........................................................................................................................79
  10.1. EXECUTIVE COMMITTEE ..........................................................................................................................79
  10.2. CLINICAL COORDINATING CENTER (CCC) ................................................................................................79
  10.3. UVEITIS PHOTOGRAPH READING CENTER (UPRC) ..................................................................................79
  10.4. DATA COORDINATING CENTER (DCC) .....................................................................................................80
  10.5. DATA ANALYSIS CENTER (DAC) ..............................................................................................................80
  10.6. DATA SAFETY AND MONITORING COMMITTEE (DSMC) .............................................................................80
  10.7. EDITORIAL COMMITTEE ...........................................................................................................................80
  10.8. STUDY SITES..........................................................................................................................................81
  10.9. PHARMACY.............................................................................................................................................81
  10.10 STUDY COMMUNICATIONS ......................................................................................................................81
11. BIBLIOGRAPHY .......................................................................................................................................82


APPENDIX A: STUDY FORMS
APPENDIX B: CERTIFICATION FORMS
APPENDIX C: QUALITY OF LIFE QUESTIONNAIRES
APPENDIX D: PATIENT CALENDARS
APPENDIX E: UPRC MANUAL
APPENDIX F: TABLE FOR ASSESSING UVEITIS ACTIVITY


```

### DOC-003 PDF page 68

[Direct source](../../../../joi190092supp2_prod.pdf#page=68)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


                                 Investigators, Personnel and Study Sites

Nisha Acharya, MD, MS                                     Principal Investigator
                                                          Site Director San Francisco
                                                          Study Ophthalmologist San Francisco


John Gonzales, MD                                         Study Ophthalmologist San Francisco

Thuy Doan, MD                                             Study Ophthalmologist, San Francisco

SR Rathinam, MD, PhD                                      Site Director Aravind Eye Hospital Madurai
                                                          Study Ophthalmologist Madurai

T Radhika, MD                                             Study Ophthalmologist Madurai

Vedhanayaki, MD                                           Study Ophthalmologist Madurai

VK Anuradha, MD                                           Site Director Aravind Eye Hospital Coimbatore
                                                          Study Ophthalmologist Coimbatore

VR Saravanan, DO, DNB, FRCS                               Study Ophthalmologist Coimbatore

Upendra Babu, MD                                          Study Ophthalmologist Coimbatore

S. Bala Murugan, MD                                       Site Director Aravind Eye Hospital Pondicherry
                                                          Study Ophthalmologist Pondicherry

Prabu Baskaran, MD                                        Study Ophthalmologist Pondicherry

Lourdes Arellanes-Garcia, MD                              Site Director Mexico City
                                                          Study Ophthalmologist Mexico City

Luz Elena Concha del Rio, MD                              Co-investigator Mexico City
                                                          Study Ophthalmologist Mexico City

Hassan Al Dhibi, MD                                       Site Director Riyadh
                                                          Study Ophthalmologist Riyadh

Donald Stone, MD                                          Study Ophthalmologist Riyadh

Mohammed Al Shamrani, MD                                  Study Ophthalmologist Riyadh

Abdulelah Al Abdullah, MD                                 Study Ophthalmologist Riyadh

Lyndell Lim, MD                                           Site Director Melbourne
                                                          Study Ophthalmologist Melbourne

Debra Goldstein, MD                                       Site Director Chicago
                                                          Study Ophthalmologist Chicago

Eric Suhler, MD, MPH                                      Site Director Portland
                                                          Study Ophthalmologist Portland
                                                                                                                   4


```

### DOC-003 PDF page 69

[Direct source](../../../../joi190092supp2_prod.pdf#page=69)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        January 6, 2017 - Version 4.5
 Manual of Operation and Procedures



                         Investigators, Personnel and Study Sites, continued.


Jeremy Keenan, MD, MPH                                    Medical Monitor


Thomas Lietman, MD                                        Data Coordinating Center


Travis Porco, MPH, PhD                                    Data Coordinating Center, Principal statistician


Maya Rao, MPH                                             Coordinating Center Manager
                                                          Study Coordinator San Francisco


Erica Browne, MS                                          Data Manager/ Study Coordinator San Francisco



Mr. AL. Sivaram                                           Study Coordinator Madurai

Mrs. G. Jeyakohila                                        Study Coordinator Madurai

Ms. V. Gracy Evangelin                                    Study Coordinator Madurai

Ms. R. Srija                                              Study Coordinator Coimbatore

Ms. R. Thilagavathi                                       Study Coordinator Pondicherry

Tracy Giles                                               Study Coordinator Oregon

Yoko Burgoa                                               Study Coordinator Mexico City

Hilda Hernández                                           Study Coordinator Mexico City

Julie Morrison                                            Study Coordinator Melbourne

Tanya Pejnovic                                            Study Coordinator Melbourne

Julie A. Johnson                                          Study Coordinator Chicago

Sara Al Nuwaysir                                          Study Coordinator Riyadh

Abdulrahman Al Hommadi                                    Study Coordinator Riyadh




                                                                                                                     5


```

### DOC-003 PDF page 70

[Direct source](../../../../joi190092supp2_prod.pdf#page=70)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        January 6, 2017 - Version 4.5
 Manual of Operation and Procedures



                      Data Safety and Monitoring Committee (DSMC) Members


Maureen Maguire, PhD                                           Chair of DSMC
                                                               Biostatistics
                                                               Carolyn F. Jones Professor of Ophthalmology
                                                               University of Pennsylvania



William Barlow, PhD                                            Biostatistics
                                                               Research Professor, Biostatistics
                                                               University of Washington


Jackie Glover, PhD                                             Ethics
                                                               Professor of Pediatrics
                                                               University of Colorado



Steven Yeh, MD                                                 Uveitis
                                                               Associate Professor of Ophthalmology
                                                               Emory University


Narsing Rao, MD                                                Uveitis
                                                               Professor of Ophthalmology and Pathology
                                                               Doheny Eye Institute



Albert Vitale, MD                                              Uveitis
                                                               Professor of Ophthalmology & Visual Sciences
                                                               University of Utah School of Medicine




                               National Eye Institute (NEI) Program Officer


Donald Everett, MA                                             Program Officer
                                                               National Eye Institute
                                                               National Institutes of Health




                                                                                                                     6


```

### DOC-003 PDF page 71

[Direct source](../../../../joi190092supp2_prod.pdf#page=71)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
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

### DOC-003 PDF page 72

[Direct source](../../../../joi190092supp2_prod.pdf#page=72)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


1. Introduction to trial

    The proposed study is a randomized comparative effectiveness trial to determine which
    treatment, methotrexate or mycophenolate mofetil, is more effective as first-line
    corticosteroid-sparing treatment for patients with non-infectious intermediate, posterior and
    panuveitis requiring corticosteroid-sparing therapy.

    Two hundred sixteen patients with non-infectious uveitis in need of corticosteroid-sparing
    therapy will be randomized to receive either oral methotrexate or oral mycophenolate
    mofetil at Aravind Eye Hospitals (Madurai, Coimbatore, and Pondicherry, South India),
    Casey Eye Institute (Oregon Health and Science University, Portland), "Dr. Luis Sánchez
    Bulnes" Hospital, Asociación Para Evitar la Ceguera (Mexico City), Center for Eye Research
    Australia at the Royal Victorian Eye & Ear Hospital (University of Melbourne), Northwestern
    University Feinberg School of Medicine (Chicago, IL), King Khaled Eye Specialist Hospital
    (Riyadh, Saudi Arabia), and the F.I Proctor Foundation (University of California, San
    Francisco). They will be followed monthly for 6 months after enrollment or until treatment
    failure. Patients who achieve success at 6 months will continue for another 6 months on the
    same medication. Patients who fail at 6 months will switch treatments and be followed for
    an additional 6 months or until failure of the second treatment.

    1.1. Research question

    Which treatment–methotrexate or mycophenolate mofetil–is more effective as a first-line
    immunosuppressive treatment for patients with non-infectious intermediate, posterior and
    panuveitis requiring corticosteroid-sparing therapy?

   1.2. Specific aims

    Aim 1: Establish which immunosuppressive treatment, methotrexate or
    mycophenolate mofetil, results in a higher proportion of patients achieving
    corticosteroid-sparing control of inflammation. As a primary outcome, proportion of
    successful corticosteroid-sparing control of inflammation will be compared at 6 months after
    enrollment. We will also evaluate differences in secondary outcomes, such as visual acuity,
    macular thickness, time to control of inflammation, efficacy within various anatomic locations
    of uveitis, tolerability, quality of life, and adverse events.

    Aim 2: Evaluate the clinical efficacy of switching agents after initial treatment failure.
    Patients who are recorded as a treatment failure on the initial randomized drug will be
    switched to the other treatment. These patients will be followed an additional 6 months from
    the date of treatment failure, following the same protocol with the same primary and
    secondary outcomes as in Aim 1.




                                                                                                               8


```

### DOC-003 PDF page 73

[Direct source](../../../../joi190092supp2_prod.pdf#page=73)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


2. Trial design
        2.1. Design summary
Study type
    • Randomized, observer-masked comparative effectiveness trial
    • Block randomization by site: Aravind Eye Hospitals, Casey Eye Institute, Asociación Para
        Evitar la Ceguera, Center for Eye Research Australia at the Royal Victorian Eye & Ear
        Hospital, Northwestern University Feinberg School of Medicine, King Khaled Eye
        Specialist Hospital, and F.I. Proctor Foundation
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
           • Proportion of overall treatment success at 6 months, where treatment success is
              defined as controlled ocular inflammation (Table 2) with 7.5 mg/day of oral
              prednisone and ≤ 2 drops/day of topical 1% prednisolone acetate
    • Secondary outcomes
            • Proportion of corticosteroid-sparing treatment success at 6 months after switching
              treatments in patients who are a treatment failure in the first 6 months where
              treatment success is defined as in Aim 1 (Specific Aim 2)
            • Time to control of inflammation
            • Time to treatment success
            • Proportion achieving treatment success at 5 months and sustaining, for at least 28
              days, to 6 months
            • Proportion achieving treatment success at 12 months in Phase I
            • Phase I treatment success (6-12 months) with complete discontinuation of
              corticosteroid
            • Proportion achieving treatment success at 6 months in Phase II
            • Change in best spectacle-corrected visual acuity (BSCVA)
            • Presence of macular edema
            • Change in macular thickness
            • Change in vitreous haze as assessed clinically by the Miami (formerly Davis) scale
            • Change in vitreous haze as assessed by fundus photography grading by NEI and
              Miami (formerly Davis) scales
            • Efficacy for intermediate, posterior and panuveitis subgroups
            • Efficacy for retinal vasculitis
            • Proportion discontinuing due to intolerability
            • Rate of adverse events
            • Proportion discontinuing due to serious adverse events
            • Quality of life (Health related and vision related)
                                                                                                                9


```

### DOC-003 PDF page 74

[Direct source](../../../../joi190092supp2_prod.pdf#page=74)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
« Dose reduction
«Efficacy of treatment in patients with Vogt-Koyanagi-Harada (VKH) disease
e Proportion of patients beginning with at least 2+ inflammation in anterior chamber
cells who experience a 2-step reduction (i.e. decreasing from 2+ to 0.5+; 3+ to 1+;
4+ to 2+).
e Proportion of patients beginning with at least 2+ inflammation in vitreous haze who
experience a 2-step reduction (i.e. decreasing from 2+ to 0.5+; 3+ to 1+; 4+ to 2+).
« Proportion of patients who started with at least 1+ inflammation levels in anterior
chamber cells who achieve a decrease to 0 level of inflammation in anterior
chamber cells.
e Proportion of patients who started with at least 1+ inflammation levels in vitreous
haze who achieve a decrease to 0 level of inflammation in vitreous haze.
e Proportion of patients achieving controlled inflammation defined by 0 level of
inflammation in vitreous haze and 0 level of inflammation in anterior chamber cells
e Proportion of patients requiring injections for severe inflammation during the trial
e Proportion of patients requiring injections for macular edema during the trial
2.2. Study timeline
Table 1: Timeline for study completion
ember 2011 through} Pre-study activities: refine/finalize MOP, IRB, IND, Indian Council of
September 2012 Medical Research approval
September 2012 1st meeting of DSMC, conduct final certification of sites and study
through personnel, earliest project start date
August 2013* through
‘April 2017 Enrollment and follow-up
Through November Finish 6 month follow-up (Phase |) + 1 month visit window
2017
Through May 2018 Finish follow-up (Maximum of 12 months + 1 month visit window period)
Through November Lock database, analyze, publish, and disseminate results
2018
* San Francisco started enrollment in August 2013. Other sites on boarded at differing times after
Aug 2013.
10

```

### DOC-003 PDF page 75

[Direct source](../../../../joi190092supp2_prod.pdf#page=75)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


2.3. Eligibility
.
        2.3.1. Anatomical location of inflammation

        All patients must have met the criteria for intermediate, anterior and intermediate, posterior
        or panuveitis, as defined by the Standardization of Uveitis Nomenclature (SUN) Working
        Group, at any time since their diagnosis of uveitis.

        The Standardization of Uveitis Nomenclature
         ______________________________________________________________
         Type              Primary Site of Inflammation Includes
         ______________________________________________________________
         Anterior Uveitis       Anterior Chamber         Iritis
                                                         Iridocyclitis
                                                         Anterior cyclitis
         Intermediate Uveitis Vitreous                   Pars planitis
                                                         Posterior cyclitis
                                                         Hyalitis
         Posterior Uveitis      Retina or Choroid        Focal, multifocal, or
                                                         Diffuse choroiditis
                                                         Chorioretinitis
                                                         Retinochoroiditis
                                                         Retinitis
                                                         Neuroretinitis
         Panuveitis             Anterior Chamber
                                Vitreous
                                Retina or Choroid
         ______________________________________________________________
         *Adapted from the SUN Working Group Anatomic Classification of Uveitis

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
          intermediate uveitis and not panuveitis.” 30 If vasculitis is present in the setting of
          intermediate uveitis, it should be called intermediate uveitis with vasculiltis, not posterior
          uveitis.




                                                                                                            11


```

### DOC-003 PDF page 76

[Direct source](../../../../joi190092supp2_prod.pdf#page=76)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


       2.3.2. Inclusion Criteria

         All the following criteria must be met at enrollment:
              • History of non-infectious intermediate, anterior and intermediate, posterior or
                  panuveitis in at least one eye
              • Active inflammation within the last 180 days, defined by the presence of any of
                  the following (in at least one eye) according to SUN criteria and the NEI vitreous
                  haze grading scale:
                          ≥ 2+ anterior chamber cells and/or
                          ≥ 2+ vitreous haze and/or
                          active retinal or choroidal inflammation
              • Active inflammation in at least one eye at enrollment, defined by any of the
                  following:
                          ≥ 1+ anterior chamber cells and/or
                          ≥ 1+ vitreous haze and/or
                          active retinal/choroidal inflammation (bullous serous retinal
                          detachment qualifies if choroidal thickening)
              • At least one of the following criteria must be met before or at enrollment:
                       1.) Active inflammation after 4 weeks of high-dose (1mg/kg prednisone
                       equivalent) oral corticosteroid treatment
                       2.) Treatment with oral corticosteroids resulting in a reduction of inflammation,
                       followed by an increase in inflammation (of at least 1 grade in anterior chamber
                       cells or vitreous haze or a change of non-active to active retinal/choroidal
                       lesions) when corticosteroid is tapered, in the 180 days prior to enrollment
                       3.) Treatment with 10mg/day oral prednisone or equivalent over at least the
                       past 90 days prior to enrollment
                       4.) Active inflammation after long-acting corticosteroid injection 4 weeks to 180
                       days prior to enrollment
                       5.) One of the following uveitic conditions necessitating corticosteroid-sparing
                       immunosuppressive treatment12:
                                  Behcet’s disease with posterior segment involvement
                                  Multifocal choroiditis with panuveitis
                                  Serpiginous choroidopathy
                                  Birdshot retinochoroidopathy
                                  Diffuse retinal vasculitis
                                  Severe Vogt-Koyanagi-Harada syndrome (VKH) (for example: acute
                                    VKH that has been active for at least 4 weeks, or VKH with bullous
                                    serous retinal detachments and/or choroidal detachments with other
                                    signs of ocular inflammation)
                                  Sympathetic ophthalmia
                        6.) If the patient does not fit any of these categories, but the physician believes
                        corticosteroid-sparing immunosuppressive therapy is indicated, eligibility may
                        be assessed on a case-by-case basis after discussion with the coordinating
                        center. Please contact Dr. Acharya at 415-624-7710 or by email.
              • Willingness to start corticosteroid treatment at 1mg/kg or 60mg a day of
                  prednisone, whichever is less (starting at a lower dose is acceptable if patient has
                  known tolerability issues)
              • Willingness to limit alcohol consumption (American College of Rheumatology
                  recommendation is 2 drinks per month or less)
              • Willingness to use an acceptable method of contraception during the study period
                  (i.e. pharmacologics, devices, barrier methods) or abstinence.

                                                                                                           12


```

### DOC-003 PDF page 77

[Direct source](../../../../joi190092supp2_prod.pdf#page=77)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


       2.3.3. Exclusion criteria

         Any one excludes patient:
            • Any infectious cause of uveitis
            • Prior immunosuppressive therapy other than corticosteroids in the past 12 months
            • Prior intolerability or safety issues with methotrexate or mycophenolate mofetil
            • Prior failure to control ocular or other inflammation using methotrexate or
               mycophenolate mofetil
            • Prior biologic therapy at any time
            • < 16 years of age at enrollment
            • Media opacity (such as cataract and/or corneal scar) and/or extensive posterior
               synechiae such that examination of the posterior segment is not possible in both
               eyes
            • Chronic hypotony (IOP < 5 mm Hg for > 3 months) in both eyes
            • Periocular or intravitreal corticosteroid injection in the past 4 weeks
            • Fluocinolone acetonide implant in either eye in < 3 years
            • Intraocular surgery in < 30 days, or planned surgery within the next 180 days
            • Best spectacle-corrected visual acuity of hand motion or worse in better eye
            • Planning to conceive during the study period, pregnant or breast-feeding (blood
               or urine pregnancy test for all females, excluding those who are post-menopausal
               is mandatory within 4 weeks prior to enrollment)
            • History of cancer (If a patient has a history of non-melanoma skin cancer they can
               still be considered for inclusion in this study, provided it is not currently active).
            • Systemic autoimmune disease or ocular condition (besides uveitis) anticipated to
               dictate treatment course
            • Abnormal CBC (≤ 2,500 white blood cells and/or ≤ 75,000 platelets and/or ≤9
                hemoglobin) within 4 weeks prior to enrollment*
            • Abnormal alanine aminotransferase (ALT) and/or aspartate aminotransferase
               (AST) ≥ 2 times the upper limit of normal for the lab and/or creatinine ≥ 1.5
               within 4 weeks prior to enrollment
            • Evidence of active tuberculosis, HIV infection, syphilis, or hepatitis B or C
               (patients must have a tuberculin skin test, or interferon-gamma release assay, a
               chest radiograph, RPR/VDRL, FTA-ABS, or other treponemal tests, Hepatitis B
               surface antigen and Hepatitis C antibody tests within 90 days prior to enrollment)

    Beyond the tests listed above, the remainder of the work-up is at the discretion of the
    investigator and should be tailored to the clinical situation. Distinguishing between infectious
    and non-infectious uveitis is part of standard of care and should be dictated by the patient’s
    clinical exam, but at minimum, all patients must have testing for tuberculosis, syphilis and
    hepatitis within 90 days prior to enrollment. If there is any clinical suspicion of infection, other
    tests should be considered at the investigator’s discretion (i.e. leptospirosis in India). Testing
    is available for this at Aravind Eye Hospitals if indicated.

       2.3.3.a. Screening for Active Tuberculosis
    Given that treatment with antimetabolites is not thought to increase the risk of tuberculosis,
    patients with latent (but not active) tuberculosis will be eligible for this study. It is at the study
    doctor’s discretion to determine if the patient has active or latent tuberculosis, based on the
    testing required. There is no specific cut off for the tuberculin skin test for inclusion in the
    trial. Treatment for latent TB should be handled according to the standard of care in the
                                                                                                           13


```

### DOC-003 PDF page 78

[Direct source](../../../../joi190092supp2_prod.pdf#page=78)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial      January 6, 2017 - Version 4.5
Manual of Operation and Procedures


    country in which the patient is enrolled. For example, patients with latent TB may be treated
    with INH in the U.S. However, this is not standard practice in India. Particular consideration
    to TB as an etiology should be given to patients with serpiginous chorioretinopathy, and an
    evaluation by an internist should be done if needed.

    2.4. Randomization and masking

    Block randomization of the patients will ensure that an equal number of patients are
    randomized to each study arm at each site. Randomization lists will be created by the
    biostatistician (Travis Porco) and accessed online via REDCap database. The following
    people will be able to access to the list of patients who have been randomized through the
    REDCap database:

    Emergency Contact Personnel*
      • Dr. Lalitha Prajna, Chief Microbiologist, Aravind Eye Hospital Madurai
      • Dr. R. Revathi, Chief, Cornea Services, Aravind Eye Hospital Coimbatore
      • Dr. R. Venkatesh, Chief Medical Officer, Aravind Eye Hospital Pondicherry
      • Dr. Maggie Ryan, Research Pharmacist, Casey Eye Institute, Oregon
      • Dr. Stephen McLeod, Chairman Department of Ophthalmology, University of California
          San Francisco
      • Dr. Ma. del Carmen Preciado, Ophthalmologist, APEC, Mexico
      • Dr. Sukhpal Sandhu, Retinal ophthalmologist, CERA, Melbourne
      • Dr. Andrea Birnbaum, Ophthalmologist, Northwestern University, Chicago
      • Dr. Marco Mura, Chief of Vitreoretinal Services, KKESH, Riyadh

         *Emergency contacts will log into REDCap to consult the list of randomized patients in case of an
         emergency in which unmasking is necessary for patient safety and Dr. Thomas Lietman of the DCC cannot
         be reached.

       Data Coordinating Center (DCC) Personnel
        • Dr. Thomas Lietman, Professor of Ophthalmology and Epidemiology, University of
            California San Francisco, Proctor Foundation
        • Dr. Travis Porco, Principal statistician, Proctor Foundation
        • Ms. Erica Browne, Research analyst, Data Manager, Proctor Foundation
        • Ms. Maya Rao, Study Coordinator, Coordinating Center Manager, Proctor Foundation

    The study coordinators (listed below) will be aware of patient treatment assignment and will
    have a copy of the patient ID list for their site; however, they will not know future treatment
    assignments prior to randomizing patients. After consenting patients for enrollment and
    confirming all eligibility requirements have been met, study coordinators will log into REDCap
    and perform the randomization. Study coordinators will then give patients their assigned
    treatment.

    The following study coordinators will have access to REDCap to perform randomizations but
    will not know the treatment assignments prior to randomizing patients:
         • Ms. Maya Rao*, Study Coordinator, University of California, San Francisco
         • Ms. Erica Browne, Study Coordinator, University of California, San Francisco
         • Mr. Sivaram, Study Coordinator, Aravind Eye Hospital Madurai, India
         • Ms. V. Gracy Evangelin, Study Coordinator, Aravind Eye Hospital Madurai, India
         • Ms. R. Srija, Study Coordinator, Aravind Eye Hospital Coimbatore, India
         • Ms. R. Thilagavathi, Study Coordinator, Aravind Eye Hospital Pondicherry, India
         • Ms. Tracy Giles, Study Coordinator, Casey Eye Institute, Oregon
         • Ms. Yoko Burgoa, Study Coordinator, APEC, Mexico
                                                                                                                 14


```

### DOC-003 PDF page 79

[Direct source](../../../../joi190092supp2_prod.pdf#page=79)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial              January 6, 2017 - Version 4.5
Manual of Operation and Procedures


         •   Ms. Hilda Hernández, Study Coordinator, APEC, Mexico
         •   Ms. Julie Morrison, Study Coordinator, CERA, Melbourne
         •   Ms. Tanya Pejnovic, Study Coordinator, CERA, Melbourne
         •   Ms. Julie A. Johnson, Study Coordinator, Northwestern University, Chicago
         •   Ms. Sara Al Nuwaysir, Study Coordinator, KKESH, Riyadh
         •   Mr. Abdulrahman Al Hommadi, Study Coordinator, KKESH, Riyadh

    *Ms. Rao will act as study coordinator to Proctor Foundation patients, as well as Coordinating Center Manager
    overseeing all other sites. She will have access to the randomization lists for other sites, in order to check patient
    treatment assignment as a quality assessment and manage distribution of medications to all sites.

    All patients and study coordinators will be unmasked to treatment assignment after
    enrollment, as the two study drugs are different in appearance and must be administered on
    different weekly schedules. Study ophthalmologists performing the clinical eye exams, as
    well as visual acuity examiners, OCT operators, fundus photographers and fundus graders
    will be masked to treatment assignment to prevent bias in study outcomes. The UCSF
    Pharmacy’s investigational drugs department will purchase and supply mycophenolate
    mofetil and methotrexate.

    The UCSF pharmacy will be responsible for purchasing and distributing bottles of the
    medications labeled with NDC/lot number and expiration dates to Proctor Foundation, who
    will add dosing instructions and distribute medication to the Mexico City, India, and Chicago
    sites, and to Casey Eye Institute’s and CERA’s pharmacies where they will distribute the
    medication.

    Dose reduction instructions and study ID labels will be provided to each site on separate
    label sheets. Each site will place the study ID label on the bottle after randomization, before
    dispensing the drug to the patient. The format of the study ID numbers are as follows: the
    first character will be a number: “1” for Melbourne, “2” for Proctor Foundation, “3” for
    Chicago, “4” for Casey Eye Institute, “5” for Mexico City, “6” for KKESH, “7” for Madurai,“8”
    for Coimbatore, and “9” for Pondicherry. The next character is a checksum character, which
    will be a single letter. The last three characters will be sequential digits beginning at 001. An
    example identifier is 4J101; all identifiers have exactly five characters, and no other study at
    the sites uses this format.

    After enrollment and randomization, the patient ID labels will be placed on the medication
    bottles by the study coordinator or pharmacist, depending on site-specific requirements. If a
    dose reduction is used, the study coordinator will place the reduction labels on the
    medication bottles. At no time will the study doctor handle labeling or distribution of the
    study medication. Study coordinators will record the study ID, drug, date dispensed, bottle
    number, lot number, and expiration date of each bottle dispensed during the trial in the drug
    accountability log.

    To maintain masking throughout the trial, steps will be taken to avoid the study doctors
    discovering patient assignment. Not only will the study doctors have no part in handling the
    medication bottles, all patients will be given dark bags to place and keep their bottles in
    throughout the trial. They will be instructed to bring their medication to their visits enclosed
    in the bags, and an extra bag will be kept at the front desk of the clinics in case they forget.
    This will minimize the chances of the study doctor seeing the medications. Additionally,
    patients will meet with the study coordinator first, before seeing their study doctor. The study
    coordinator will review the patients’ medication calendars with them and keep the calendars
    and study bottles in his/her office for the entire patient visit. Before bringing patients to the
    study doctor, the study coordinator will remind them to not discuss their dosing and
                                                                                                                        15


```

### DOC-003 PDF page 80

[Direct source](../../../../joi190092supp2_prod.pdf#page=80)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
medication name with their study doctor.
Clinical examiners, refractionists, OCT operators, fundus photographers and fundus graders
will not be given any information on medication assignment. If personnel are unmasked at
any time, a protocol deviation form must be completed, scanned and emailed to both the
Medical Monitor , Principal Investigator
‘and Coordinating Center — Note
at these patients should still continue in the trial.
2.5. Definitions for primary endpoint
2.5.1. Determination of Treatment Success/Failure
Treatment success is defined as controlled ocular inflammation (see Table 2) in both eyes
with 7.5 mg/day of prednisone, no periocular or intravitreal corticosteroid injections after the
first 90 days of follow up, and < 2 drops/day of topical 1% prednisolone acetate at the 6
month visit without treatment failure any point due to safety, tolerability or futility. Patients
can stop medication at any time, but that in and of itself does not count as a treatment
failure.
Table 2: Criteria for controlled inflammation
Parameter Definition of control
: vasculitis posterior to the equator
*SUN criteria®; ** NEI vitreous haze grading scale™ *** Cystoid macular edema is not
sufficient to be called active inflammation
2.5.2. Treatment failure
+ Failure due to efficacy: Patients can be declared a treatment failure due to
futility and be declared a treatment failure and enter Phase || at any time
during follow-up if the following occurs: The treating physician
determines that it is futile to continue the current study medication due to
persistent, uncontrolled inflammation that appears to be non-responsive to
treatment. This option of declaring futility should only be declared if
treatment with study medication seems completely unlikely to be able to
control inflammation. Since the medications take up to a few months to
fully take effect, increase in inflammation early on in the trial is not an
indication of treatment failure. Corticosteroids may be increased in the
case of increased inflammation.
Efficacy will be judged at the primary endpoint of 6 months. Specifically,
at 6 months, if there is a lack of efficacy, patients will be declared a
treatment failure and enter Phase II if the following occurs: The patient
does not have controlled inflammation (see Table 2) with a prednisone dose
of 7.5 mg/day and less than or equal to 2 prednisolone acetate 1% drops
per day by 6 months.
+ Failure due to intolerability: Patients who experience severe symptoms
thought to be related to the drug should try a dose reduction if they are
willing. If this is not successful and the patient is unable to continue their
16

```

### DOC-003 PDF page 81

[Direct source](../../../../joi190092supp2_prod.pdf#page=81)

```text
Firstine Antimetabolites as Sterold-sparing Treatment (FAST) Uveltis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
medication due to symptoms and is also not willing to continue, treatment
failure can be declared. Please refer to Table 5 for dose reduction
guidelines. Trial of a dose reduction is strongly encouraged, however it is_
not required for a patient to be determined a treatment failure due to
intolerability.
+ Failure due to safety: Patients who experience abnormal lab results
meeting the designated threshold of a non-serious adverse event (e.g.
AST or ALT increasing to twice the upper limit of normal) will
immediately stop taking their medication. As these abnormalities are
often reversible, patients whose abnormalities are classified as non-
serious adverse events (see Table 3) will be allowed 28 days to regain
eligibility. It is recommended that these patients repeat lab tests within
1-2 weeks of the initial abnormal result to see if the results return
below the designated threshold (e.g. AST or ALT less than twice the
upper limit of normal). If the lab results return below the designated
threshold of a non-serious adverse event within 28 days, patients may
be re-administered the study drug per protocol or at one of the
designated dose reduction levels, at the investigator's discretion.
If lab results remain at or above the threshold of a non-serious
adverse event for 28 days, this is classified as a serious adverse
event and treatment failure will immediately be declared. At this point,
patients will be treated according to the best medical judgment of their
clinician and not switch to Phase II (if currently in Phase I). However,
month 6 visit data and imaging should still be collected (Phase | and
Phase Il), if the serious adverse event occurs before the six month
visit. For other non-serious adverse events (Such as an opportunistic
infection) the study drug may be stopped temporarily as per the
discretion of the investigator. If an infection does not resolve within 28
days, it is considered a serious adverse event.
Table 3: Thresholds for classifying non-serious and serious lab abnormalities
Non-Serious Adverse Event* Serious Adverse Event
SGPT (AL normal of the reference range | normal of the reference range
"NOTE: If any non-serious lab abnormality does not resolve within 28 days, then it must be classified as a
serious adverse event, and treatment failure due to safety will be declared.
For all non-laboratory SAEs, treatment failure cannot be declared until the Medical
Monitor judges that the SAE is related to the study drug. This will require the
investigator notifying the Medical Monitor about the event, and the Medical Monitor
contacting the investigator regarding his determination. The Medical Monitor will
determine two things: 1, whether this is a true treatment failure because the SAE
is likely to be related to the study drug, and 2, whether it is safe to switch the
patient to Phase II. If it is not safe to switch, the patient will be treated according to
best medical judgment, and still be followed up at their 6 month visit (Phase | and
Phase Il).
7

```

### DOC-003 PDF page 82

[Direct source](../../../../joi190092supp2_prod.pdf#page=82)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures



                 If the investigator thinks the SAE is related to the study drug, he/she can stop the
                 study medication anytime (including prior to determination of treatment failure by
                 the Medical Monitor). If the investigator thinks treatment failure is likely (prior to
                 hearing from the Medical Monitor) they should obtain all study assessments which
                 would be collected at a treatment failure visit. However, the investigator will wait to
                 complete the Treatment Assessment Form and officially declare treatment failure
                 until they are instructed to do so by the Medical Monitor.

       2.5.3. Dropouts, Non-Compliant Patients and Follow-up

             •    Dropout from study: Patients will be considered to have dropped out from
                  the study only if they declare they are no longer interested in further
                  participation and not willing to return for any study visits, or are
                  deceased. If patients are not willing to return for any study visits, no further
                  information will be collected on those patients. We anticipate that a few
                  patients may drop out due to unwillingness to continue or death. In case of
                  patient dropout, the patient dropout form should be filled out.

                  If death is considered to be related to the study drug, the patient will be
                  counted as a treatment failure. If death is not related to the study drug, the
                  patient will be counted as a dropout. This would be at the discretion of the
                  Medical Monitor.

             •    Non-compliant Patients: Patients who stop the study treatment for
                  reasons other than efficacy, tolerability and/or safety (i.e. fear of potential
                  side effects) but are willing to return for study visits, are not considered
                  dropouts. Also, if patients miss study visits, and do not respond to contact,
                  they are not considered dropouts. These patients will be considered non-
                  compliant patients, and will be encouraged to return for subsequent study
                  visits regardless of whether or not they are taking study medication,
                  especially the 6 month visit (Phase I and Phase II).

                  It should be noted that missing a visit does not mean that a patient has
                  dropped out of the study. These patients are considered to be non-
                  compliant. For example, if they missed the 1 month visit, every attempt will
                  be made to bring them back as soon as possible and to continue with
                  subsequent visits. Also, a non-serious adverse event or discontinuation of
                  study medication does not mean that the patient has dropped out and they
                  should continue to be followed according to the protocol, as they may be
                  able to resume treatment. Even if the patient is not willing to resume
                  treatment, but is willing to return for study visits they are not considered
                  dropouts.

             •    Following Patients who fail prior to Phase I & Phase II (6 months): If
                  patients are declared a treatment failure prior to Phase I or Phase II 6
                  Months, every effort should be made to bring the patient back for the 6
                  month visit. Note, that patients who are declared treatment failure, and are
                  switching from Phase I to Phase II will already be followed.




                                                                                                           18


```

### DOC-003 PDF page 83

[Direct source](../../../../joi190092supp2_prod.pdf#page=83)

```text
          First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial                     January 6, 2017 - Version 4.5
          Manual of Operation and Procedures
   2.5.4 Primary Endpoint Flowchart                                                      Randomization to
                                                                                           MTX or MMF
                             Monthly: evaluation of efficacy,                                                                           At six months: controlled
                           tolerability, and safety; steroid taper                                                                     inflammation* with 7.5 mg
                                      with adjustments                                                                              prednisone and ≤2 drops/day**?
       At any time:             At any time:                                  At any time:                                Yes, treatment            No: switch to alternate
     serious adverse          clinician deems                               intolerable side                                 success                 medication, Phase II
          event               treatment futile                                   effects
                                                                                                                     Continue treatment in         6 months later: controlled
                                                                                                                     Phase I, months 6-12         inflammation* with ≤7.5 mg
                      Treatment             Switch to alternate             Dose reduction                                                             prednisone and ≤2
                        failure             medication, Phase II                   I                                                                     drops/day**?
                                                                                                                    At 12 months: controlled
                                                               Intolerable side            Side effects           inflammation* with ≤7.5 mg
                                                                                                                       prednisone and ≤2                             Yes: treatment
                                                                effects persist              resolve                                                                    success
                                                                                                                          drops/day**?
                                                               Dose reduction                         Continue treatment                                             No: treatment
                                                                     II                                  per protocol                   Yes: treatment
                                                                                                                                                                         failure
                                                                                                                                           success
                                                Intolerable side                 Side effects
                                                 effects persist                   resolve                                              No: treatment
                                                                                                                                            failure
                                                             Switch to alternate            Continue treatment
                                                             medication, Phase II              per protocol
*Criteria for controlled inflammation: Anterior chamber cells ≤0.5 +; Vitreous haze ≤ 0.5 +; No active choroid and retina lesions
** 2 drops/day refers to topical 1% prednisolone acetate or equivalent                                                                                                        19


```

### DOC-003 PDF page 84

[Direct source](../../../../joi190092supp2_prod.pdf#page=84)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
3. Treatment plan
3.1. Study drugs
Patients will be randomized to receive either methotrexate or mycophenolate mofetil. In
addition, folic acid supplements will be given to all patients who have been randomized to
methotrexate. All_study ophthalmologists, refractionists, OCT operators, fundus
photographers and fundus graders will be masked to _treatment_assignment. For
dosing schedules, see Tables 4 and 5.
To maintain masking, study coordinators will review patient side effects with the patient at
each visit, prior to meeting with the physician. At this time, the study coordinator will remind
the patient not to speak to their study doctor regarding the name of the medication or
dosing instructions. If the patient is experiencing intolerable side effects, the study
coordinator and patient will speak with the study doctor about the possibility of a dose
reduction, without revealing the name of the medication or the dosing instructions. The study
doctor will then decide if the dose reduction should be tried and communicate this with the
patient and study coordinator. The study coordinator will then provide the patient with new
dosing instructions, away from the vicinity of the study physician (see Table 5).
Table 4: Weekly Dosing Schedule
Drug Day
1 2 3 4 5 6 7
Methotrexate 7.5 mg BID
Introductory Dose
Mycophenolate 500 500 500 500 500 500 500
Weeks 182 Mofetil mgBID mgBID mgBID mgBID mgB8ID mgBID mgBID
Folic Acid 11mg 41mg img img img 1mg img
(methotrexate only) daily daily — daily daily ~— daily daily _— daily
Methotrexate 12.5 mg BID
Maintenance Dose
Mycophenolate 16 16 16 15 15 15 16
Mofetil gBID gBID gBID gBID gBID gBID gBID
Post week 2
Folic Acid 1mg img img img img img img
(methotrexate only) daily daily — daily daily ~— daily daily _—_ daily
Table 5: Dose Reduction Guidelines*
Drug Day
4 2 3 4 5 6 7
Methotrexate 10mg BID
Reduction
Level!
™ ate
Mycopnenola 4g BID 14gBID 1gBID 1gBID 1gBID 1gBID 1gBID
Reduction Methotrexate 7.6m BID.
Level Il
Mycophenolate 500mg 500mg 500mg 500mg 500mg 500mg 500mg
mofetil BID BID BID BID BID BID BID
“Doses should only be reduced in response to intolerable side effects and safety concerns. If there are no
tolerability/safety issues, the patient should stay on the maintenance dose for the duration of follow-up. Note: 29
Even if a dose reduction is used for methotrexate, folic acid should remain at 1 mg daily.

```

### DOC-003 PDF page 85

[Direct source](../../../../joi190092supp2_prod.pdf#page=85)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures



All individuals handling methotrexate and mycophenolate, including study participants and/or
family members/others caring for and assisting study participants with their medications outside of
the hospital/clinic, will be educated on the Safe Handling of Hazardous Medications guidelines
outlined in the National Institute for Occupational Safety and Health manual, Preventing
Occupational Exposures to Antineoplastic and Other Hazardous Drugs in Health Care Settings.

The National Institute for Occupational Safety and Health manual can be found at:
http://www.cdc.gov/niosh/docs/2004-165/pdfs/2004-165.pdf

     3.1.1. Methotrexate

     All methotrexate doses will be taken once per week in a divided dose, one dose taken in
     the morning and one in the evening. Patients on methotrexate will be instructed to take their
     medication with food. For the first two weeks, an introductory dose of 15 mg/week (7.5mg
     BID once a week) orally will be administered to assess tolerability. This means taking 3 pills
     in the morning and 3 pills in the evening once a week. Patients should be instructed at the
     Enrollment/Baseline visit to begin methotrexate on a day that is convenient for them, within 6
     days of enrollment. After two weeks, the dose will be increased to 25 mg/week (12.5mg BID)
     This means taking 5 pills in the morning and 5 pills in the evening once a week, until the end
     of follow-up or until treatment failure due to intolerability, adverse events, or of lack of
     efficacy.

     If there are tolerability issues in the first two weeks such that the patient is not able to
     increase the dose, and unwilling to continue the current dose, treatment failure due to
     intolerability should be declared. The patient would then be eligible to switch treatment in
     Phase II. If this occurs in Phase II, treatment failure would be declared and patient will be
     treated according to best medical judgment. If the dose is increased per protocol at two
     weeks, the study ophthalmologist can decide to reduce the maintenance dose if the patient
     experiences severe side effects.

                 3.1.1.a. Dose Reduction MTX

                 If the patient is experiencing intolerable side effects, the study coordinator and
                 patient will speak to the doctor about the possibility of a dose reduction, without
                 revealing the name of the medication or the dosing instructions. The study doctor
                 will then decide if the dose reduction should be done and inform the study
                 coordinator and patient. The study coordinator will then provide the patient with
                 new dosing instructions, away from sight of study physician. A dose reduction is
                 not mandatory but is encouraged in the setting of intolerability.

                 For the first dose reduction, methotrexate will be reduced to 20 mg/week (10mg
                 BID, once a week). This means taking 4 pills in the morning and 4 pills in the
                 evening once a week. If side effects persist and the study ophthalmologist wishes
                 to reduce the dose a second time, the dose will be reduced to 15mg/week (7.5mg
                 BID, once a week). This means taking 3 pills in the morning and 3 pills in the
                 evening, once a week. After the second dose reduction, treatment can be stopped
                 if intolerability persists and the patient can switch to Phase II.

                 Although dose reductions are strongly encouraged, they are not mandatory to
                 attempt before determining treatment failure. Treatment failure due to
                 intolerability can be declared without trial of a dose reduction.
                                                                                                            21


```

### DOC-003 PDF page 86

[Direct source](../../../../joi190092supp2_prod.pdf#page=86)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures



                If a dose reduction has been utilized, and the investigator feels that the
                tolerability/safety issues have been resolved, it is at their discretion to return the
                patient to the maintenance dose level of the medication.

    3.1.2. Mycophenolate Mofetil

    Mycophenolate mofetil will be taken twice daily. Patients on mycophenolate mofetil will be
    instructed to take their medication on an empty stomach with no food one hour before or
    after taking each dose. For the first two weeks, an introductory dose of 500 mg BID orally will
    be administered to assess tolerability. This means taking one pill in the morning and one pill
    in the evening. After two weeks, the dose will be increased to 1.5 g BID. This means taking 3
    pills in the morning and 3 pills in the evening until the end of follow-up or until treatment
    failure due to intolerability, adverse events, or lack of efficacy.

    If there are tolerability issues in the first two weeks such that the patient is not able to
    increase the dose, and also is unwilling to continue, treatment failure due to intolerability
    should be declared. The patient would then be eligible to switch treatment in Phase II. If this
    occurs in Phase II, treatment failure would be declared. If the dose is increased per protocol
    at two weeks, the study ophthalmologist can decide to reduce the maintenance dose if the
    patient experiences severe side effects.

    At any point if treatment failure is declared due to tolerability, the patient should be treated
    according to best medical judgment and still be followed up to their 6th month assessment
    (Phase I and Phase II).

                3.1.2.a. Dose Reduction Mycophenolate Mofetil

                If the patient is experiencing intolerable side effects, the study coordinator and
                patient will speak to the doctor about the possibility of a dose reduction, without
                revealing the name of the medication or the dosing instructions. The study doctor
                will then decide if the dose reduction should be done and inform the study
                coordinator and patient. The study coordinator will then provide the patient with
                new dosing instructions, away from sight of study physician. A dose reduction is
                not mandatory but is encouraged in the setting of intolerability.

                For the first dose reduction, mycophenolate will be reduced to 1g BID. This means
                taking 2 pills in the morning and 2 pills in the evening. If side effects persist and
                the study ophthalmologist wishes to reduce the dose a second time, the dose will
                be reduced to 500 mg BID. This means taking 1 pill in the morning and 1 pill in the
                evening. After the second dose reduction, treatment can be stopped if intolerability
                persists and the patient can switch to Phase II.

                Although dose reductions are strongly encouraged, they are not mandatory to
                attempt before determining treatment failure. Treatment failure due to
                intolerability can be declared without trial of a dose reduction.

                If a dose reduction has been utilized, and the investigator feels that the
                tolerability/safety issues have been resolved, it is at their discretion to return the
                patient to the maintenance dose level of the medication.



                                                                                                           22


```

### DOC-003 PDF page 87

[Direct source](../../../../joi190092supp2_prod.pdf#page=87)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


                 3.1.2.b. Proton Pump Inhibitors and Mycophenolate Mofetil

                 Upon entering the trial some patients may be taking proton pump inhibitors (e.g.
                 omeprazole). Due to a potential interaction with mycophenolate mofetil, H2
                 blockers are preferred over proton pump inhibitors. However, proton pump
                 inhibitors are acceptable if the physician and/or patient does not want to change.
                 This should be noted on the Baseline History Form under current systemic
                 medications.

     3.1.3. Folic acid

It is standard of care to prescribe folic acid supplements to reduce the severity of side effects in
patients treated with methotrexate. All patients randomized to methotrexate will be prescribed
1mg per day of folic acid. It is fine to take folic acid the day methotrexate is taken.

     3.1.4. Packaging and distribution of study medications

Patient medications will be purchased and packaged by UCSF’s pharmacy, printed with the
medication name, lot number, and expiration date. Proctor Foundation will be responsible for
distributing medications and labels with dosage instructions to all other sites.

Initial dose bottles will contain 14 days of medication at the lower initial dose. The initial two-week
supply of methotrexate is 12 pills, and the initial two-week supply for mycophenolate mofetil is 28
pills. Maintenance dose bottles will contain 30 days’ worth of medication, plus additional pills as a
buffer for visit scheduling. Methotrexate maintenance dose bottles will contain 50 pills each.
Mycophenolate mofetil maintenance doses will be provided in bottles of 100 pills each.

At the patient’s first visit (i.e. Baseline for Phase I) they will be given the 14 day introductory dose
and either one maintenance dose bottle of mycophenolate (100 pills) or one maintenance dose
bottle of methotrexate (50 pills). At every monthly visit following, patients will be given an
additional 30 days’ worth of medication (50 pills of methotrexate, or 200 pills of mycophenolate)
until 5 months. If a patient needs to schedule their appointment beyond the visit window allowed
by the medication supply, additional bottles may be dispensed to ensure sufficient supply of
medicine, although this scheduling should be discouraged.

If patients enter Phase II after treatment failure in Phase I, patients’ medication will be dispensed
following the same schedule as in Phase I. If patients enter Phase I (6-12 months) after treatment
success in Phase I (0-6 months), they will be given 120 days’ worth of medication at their 6 month
visit. Lost bottles will be replaced.

Study medications, labeled with the appropriate dosing instructions, will be distributed to the study
coordinator prior to each study visit. After randomization, before the drug is dispensed, the study
coordinator will place the Study ID label on the bottles. If a dose reduction is used, the study
coordinator will put a label on the bottle with the new instructions.

Study coordinators will also place number labels, provided by the coordinating center, on all
bottles in order to track which individual bottles were dispensed to patients. Study coordinators will
indicate on the Medication Log, what type of bottle they have dispensed (i.e. initial or
maintenance), how many bottles, what type of bottle has been returned, and the numbers of the
bottles.



                                                                                                            23


```

### DOC-003 PDF page 88

[Direct source](../../../../joi190092supp2_prod.pdf#page=88)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


If at any time the patient fails to bring in their used maintenance bottles, the study coordinator
should refer to the clinic staff member responsible for maintaining the randomization list to verify
patient assignment. This will ensure that the patient is given the correct maintenance bottle
corresponding to their assignment.

     3.1.5. Adherence to the treatment plan

Patients will be given a treatment diary in the form of a monthly calendar on which they will be
asked to record the medications they are taking as well as reasons for missed doses. They will be
asked to bring the calendars with them to each visit. Adherence will be monitored by the study
coordinator through review of the calendars, and will be recorded on the Medication Log in each
patient file. Pill counting of pills in bottles remaining from the previous study period will also be
done for a more objective measure of adherence. If a patient has just started on a new bottle
shortly before the visit, do not count these pills. For instance, if a patient returns for their two week
visit two weeks plus two days after the baseline visit, the study coordinator will not count the pills
remaining in the maintenance dose bottle they have just started on. If the patient fails to bring in
their calendar, the study coordinator should ask the patient to estimate the number of doses they
have missed.

                    3.1.5.a. Missed Doses

                    The following instructions will be given to the patients if they miss scheduled
                    doses of their medication:

                    Methotrexate: If a patient misses their scheduled dose, they may take it the next
                    day. If it is not taken the next day, they should wait until the following week. If
                    patients make-up their dose on the next day, they should continue their
                    medication weekly from the original day.

                    Mycophenolate Mofetil: If the patient misses a dose, they should continue with
                    the regular dosing schedule.

3.2. Corticosteroid therapy

     3.2.1. Oral prednisone

Prednisone vs. alternative oral corticosteroid

Unless contraindicated, oral prednisone should be used. An equivalent dose of an alternative oral
corticosteroid may be used only if a specific contraindication to oral prednisone is present. All
references to oral corticosteroid and specific dosing schedules presented in this Manual of
Procedures are given for oral prednisone.

Initial dose

All patients enrolled in the study will be initially taking concomitant oral corticosteroids at 1 mg/kg
or 60 mg daily, whichever is less. Treatment success is dependent upon successfully tapering
concomitant prednisone to 7.5 mg/day. Initial corticosteroid dose will be continued for 2 to 4
weeks at which point prednisone will be gradually tapered.1 Prednisone will be tapered to and held
at 7.5 mg/day for the first 6 months of the study. Further reduction of corticosteroids will be
allowed in Phase I after six months. If patients switch treatments and enter Phase II due to a
failure of efficacy in Phase I, they will follow the same protocol as the initial Phase I corticosteroid
                                                                                                            24


```

### DOC-003 PDF page 89

[Direct source](../../../../joi190092supp2_prod.pdf#page=89)

```text
Firstine Antimetabolites as Sterold-sparing Treatment (FAST) Uveltis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
treatment and begin at 1 mg/kg or 60 mg, whichever is less. In patients failing for efficacy,
investigators may start at a lower prednisone dose if they feel it is medically indicated. However,
following the corticosteroid tapering guidelines is strongly encouraged. If patients switch
treatments and enter Phase || due to a failure of intolerability in Phase I, then it is at the study
doctor's discretion at what dose of corticosteroid to start the patient.
Tapering schedule
For all patients, oral prednisone will be tapered gradually according to Standardization of
Uveitis Nomenclature (SUN) guidelines (see Table 6). As it takes 6-8 weeks for the study
medications to take full effect, it is expected that inflammation may become uncontrolled with
a corticosteroid taper in some patients during the first 3 months of the study. This does not
necessarily mean that the randomized treatment has failed, since more time may be needed
to ensure the drug has reached its full effect. If the study ophthalmologist believes that
continued treatment is futile prior to the primary endpoint, treatment failure may be declared
and the patient should enter Phase II. If this occurs in Phase Il, treatment failure will be
declared and the patient should be treated according to best medical judgment. However, all
patients should be followed up to their 6" month assessment in Phase II.
At_any point in Phase | or Phase Il, investigators have the option of reducing the
prednisone dose, and following a faster taper, if the patient is experiencing severe side
effects. However, it is strongly encouraged that investigators follow the corticosteroid
tapering guidelines. If absolutely medically necessary, the investigator may digress from
the protocol and reduce steroids below 7.5 mg/day in the first six months, but this is strongly
discouraged.
The corticosteroid tapering schedule for Phase | (6-12 months) is optional, and physicians
may taper patients as they deem medically acceptable. It is not mandatory for patients to
reduce down to Omg of prednisone by 12 months. In general, a rapid taper in Phase | months
6-12 is not recommended due to issues of adrenal insufficiency.
Table 6: Tapering schedule for oral prednisone: Phase | or if starting new medication in Phase II*
Dose (mq/da‘ Duration (weeks) Decrement (mq/day
60 2-4 10
50 1 10
40 1 5
35 1 5
30 1 5
25 1 5
20 1 25
17.5 1 25
15 1 25
12.5 1 25
10 1 25
75 hold*
NOTE: Begin patients at 1mg/kg or 60 mg/day, whichever is less. For Phase | hold patients at 7.5 mg/day, up to the end
of 6 months.
“if starting Phase II and failed Phase | due to efficacy.
If uveitis does not improve at the end of the first 4 weeks, use best medical judgment regarding supplemental treatment
(eg. pulse dose treatment, corticosteroid injections, additional immunosuppressives).
25

```

### DOC-003 PDF page 90

[Direct source](../../../../joi190092supp2_prod.pdf#page=90)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
Table 7: Optional tapering schedule Phase | (6-12 months)
Dose (mg/day) Duration (weeks) Decrement (mg/day)
75 " 25
<75825 2-4 1-25
<5 &225 2-4 15-25
<25821 2-4 1
i}
NOTE: When beginning Phase | (6-12 months), hold patient at 7.5 mg/day, for at least one week.
Directions for Rescue Taper
Reactivations can be mild or severe. Mild reactivations are considered an increase in
inflammation up to the 1+ level in anterior chamber cell or vitreous haze. Severe
reactivations are considered an increase in inflammation up to the 2+ level or higher in
anterior chamber cell or vitreous haze. Retinal/choroidal lesions may be considered mild or
severe at the discretion of the study physician.
If uveitis reactivates:
+ Increase oral prednisone up to a dose of 1 mg/kg for severe reactivations, or
for mild reactivations, up to double the dose at which the flare occurred, until
uveitis is controlled. Then re-taper according to the guidelines.
Uveitis is considered non-responsive if inflammation does not increase but does not further
improve after the first 4 weeks of treatment on 1mg/kg oral prednisone.
If uveitis is non-responsive:

+ Hold the current dose of prednisone for an additional week. If still no
improvement, treatment failure due to futility may be declared, and patients may
proceed to Phase ||. Alternatively, other therapies may be added, but these should
be noted as a protocol deviation.

+ If treatment failure is declared due to futility in Phase |, before the primary
endpoint of 6 months, patients may switch to Phase II. Patients who refuse to
switch to Phase II should be encouraged to return for a 6-month visit. Patients
who switch to Phase II will already be followed.

* If treatment failure is declared due to futility in Phase II, before the primary
endpoint of 6 months, patients will be treated according to best medical judgment.
If treatment failure is declared prior to 6 months, Phase | and Phase Il, every
attempt must be made to bring patients back for their 6 month assessment.

After suppression of uveitis is once again achieved (either in the case of reactivation or non-
response) follow the taper guidelines for Phase |. Patients who have failed the treatment to
which they are randomized will then switch treatments, begin Phase II, and follow the same
taper guidelines as Phase | (0-6 months). If patients flare during Phase Il, they can follow
directions for the rescue taper listed above. Patients who fail the second treatment at the 6
month endpoint will be treated as per the investigators discretion.

26

```

### DOC-003 PDF page 91

[Direct source](../../../../joi190092supp2_prod.pdf#page=91)

```text
Firstine Antimetabolites as Sterold-sparing Treatment (FAST) Uveltis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
3.2.2. Supplements
All patients will be given recommendations for supplemental treatment. This treatment is
important for patients receiving oral corticosteroids, in order to minimize the incidence of
osteoporosis. Recommendations will include:
« Calcium supplement, 500 mg 3 times daily (unless contraindicated)
« Vitamin D, 400-800 IU daily.
3.2.3. Topical corticosteroid
In addition to oral prednisone, patients may enter the study on varying doses of topical
corticosteroid drops. Topical corticosteroids should be tapered according to the suggested
guidelines (Table 8). Various types of topical corticosteroids are acceptable. The chronic
use of two times a day prednisolone acetate 1% was considered to be medically acceptable
in a survey we conducted of the American Uveitis Society members. Thus, a dose of s 2
drops a day prednisolone acetate 1% or equivalent corticosteroid will be considered
sufficient in order to declare treatment success. If possible, the goal will be to completely
taper off topical corticosteroids. In order to determine treatment success or failure, the
equivalent amount of prednisolone acetate 1% would have to be determined, and if greater
than 2 times a day treatment failure will be declared.
Table 8: Suggested tapering schedule for topical corticosteroid drops
1 drop, 6 times a day 1
1 drop, 4 times a day 1
1 drop, 3 times a day 1
1 drop, 2 times a day 1
1 drop, 1 time a day 1
None
3.2.4. Periocular and Intravitreal Injections
The use of periocular and intravitreal injections during the trial is strongly discouraged, as it
hinders the ability to assess the study drugs’ effectiveness for controlling inflammation. One
injection, either periocular triamcinolone 40mg or intravitreal triamcinolone 4mg, may be
administered to treat persistent macular edema during the first 90 days of follow-up if the
investigator thinks this is medically necessary. One injection for persistent macular edema
is permitted in the first 90 days of follow-up of Phase |, and similarly, one injection treating
persistent macular edema is permitted in the first 90 days of follow-up of Phase Il. If an
injection is given at any time solely for the purpose of treating inflammation, a Protocol
Deviation Form should be completed and sent to the Medical Monitor
HE. P'incipal Investigator jand
Coordinating Center Manager |. If an injection is given for any reason
after the first 90 days of follow-up of either Phase I or Phase II, a Protocol Deviation Form
should be completed and sent to the Medical Monitor, Principal Investigator, and
27

```

### DOC-003 PDF page 92

[Direct source](../../../../joi190092supp2_prod.pdf#page=92)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


        Coordinating Center Manager.


        3.2.5 Other adjunctive treatments/procedures

        The protocol dictates use of oral prednisone, corticosteroid drops and study medication
        (methotrexate or mycophenolate). The investigator may use other topical adjunctive
        medications such as IOP lowering medications and cycloplegic agents. These should be
        recorded on the Treatment Assessment form at each visit. The protocol does not allow for
        intravenous therapy, additional immunosuppressives or surgery during the study period. If
        such therapies are deemed necessary, the Protocol Deviation form should be completed
        and sent to the Medical Monitor, Principal Investigator, and Coordinating Center Manager.

3.3. Study procedures

 Enrollment/Baseline visit

Study coordinators should adhere to the following protocol for study procedures taking place at the
enrollment visit.

        •    The patient’s eligibility for participating in the study will be determined by the
             study ophthalmologist, aided by the study coordinator.
        •    If eligible, the patient will review the consent form with the study coordinator and
             the study physician, and give their consent.
        •    After consent, the study coordinator will assign the patient a unique Patient ID
             (derived from the list provided to study coordinator by the principal statistician).
        •    The study coordinator will then contact the designated person on site, holding
             the randomization list, to obtain the patient’s drug assignment. This will be done
             away from sight of the study physician.
        •    The study coordinator will then label the medication with the assigned Patient
             ID. They should also place the appropriate number for the bottles (i.e. if it is the
             first bottle dispensed, it should have the #1 on the bottle).

Study visits

Study coordinators should adhere to the following protocol for study procedures taking place, after
the patient is consented, enrolled and randomized. All study procedures should follow the schedule
listed below:

        •    The patient comes for a study visit and meets with the study coordinator before
             their study doctor.
        •    The patient’s medication bottle and folic acid bottle (if applicable) is immediately
             placed in a secure, opaque bag and left at the study coordinators desk for the
             remainder of the visit. Patient medication calendars should also be placed in the
             opaque bag.
        •    The study coordinator will check-in with the patient and complete the following
             in any order:
                 o Review of patient medication diaries
                 o Review of adverse events since last visit*
                 o Dispense new medication bottle (if applicable)
                 o Completion of SF-36 questionnaire (All patients) (if applicable)
                                                                                                            28


```

### DOC-003 PDF page 93

[Direct source](../../../../joi190092supp2_prod.pdf#page=93)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


                 o    Completion of NEI-VFQ-25 (all patients) and IND-VFQ (Indian patients
                      only)
                 o    Remind the patient that they should not speak to their study doctor about
                      their dosing schedule, or the name of the medication that they are
                      currently taking.

*If the patient is experiencing intolerable side effects, the study coordinator and patient will speak
to the doctor about the possibility of a dose reduction, without revealing the name of the medication
or the dosing instructions. The study doctor will then decide if the dose reduction should be done
and inform the study coordinator and patient. The study coordinator will then provide the patient
with new dosing instructions, away from sight of study physician. A dose reduction is not
mandatory but is encouraged in the setting of intolerability.

        •    The patient will then complete the study assessments, in the following order:
                 o Visual Acuity Assessment
                 o Slit lamp front of the eye exam and intra-ocular pressure
        •    The patient’s eyes will then be dilated and the following assessments will be
             completed, in any order**:
                 o Posterior segment exam
                 o OCT imaging
                 o Fundus photography
                 o Fluorescein angiogram (not a study assessment, but if performed results
                    should be recorded)
                 o Laboratory measurements
        •    After completion of the study visit, the patient will meet with the coordinator,
             review scheduling for the next study visit, and retrieve their medication.

**It is essential that visual acuity measurements, front of the eye exams and intra-ocular pressure
are completed before dilation of the eyes.

Data handling and data entry
After completion of each study visit, study coordinators at all sites will scan data collection forms
and send them electronically in PDF format to the study email address                               Hard
copies of the forms should be kept in a secure location at each site. Study staff at Madurai will
perform double data entry of the PDF forms into a web-based REDCap database from which data
can be electronically extracted for analysis. See section 7 for further details on the data entry
process.


4. Study visits
        4.1. Visit schedules
                4.1.1. Phase I: First-line treatment

After eligibility has been evaluated and informed consent given for participation in the trial,
patients will be randomized to receive oral methotrexate or mycophenolate mofetil. Patients will
continue with this course of treatment unless treatment failure occurs due to safety, intolerability
or lack of efficacy. If a failure is recorded within the first 6 months, the treatment assignment will
be switched to the drug not initially randomized to, and the patient will follow a new visit
schedule.

Patients who are treatment failures in Phase I due to safety (i.e. a serious adverse event
deemed to be related to the study drug by the Medical Monitor) may or may not proceed to
                                                                                                            29


```

### DOC-003 PDF page 94

[Direct source](../../../../joi190092supp2_prod.pdf#page=94)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
Phase II depending on the Medical Monitor's determination. In most cases of an SAE, the
patient will likely not be allowed to switch to Phase II, but in some cases, such as an SAE due
to intolerability, it may be deemed safe to switch to Phase II. Even if the patient does not switch
to Phase ||, outcome data at 6 months should be collected if the patient is willing.
Treatment success, according to the primary endpoint, will be assessed at 6 months. If treatment
has been deemed successful for a patient at 6 months, they will be provided study medication
for an additional 6 months and return for additional study visits as shown below. As long as the
patient stays on the first randomized medication, Visit Schedule | will be followed.
Guidelines for Visit Schedule |
« Day 1 corresponds to the Baseline-| visit, which is also the first day the patient
receives treatment.
¢ Visit windows are determined based on the date of randomization.
« The baseline eye exam and other baseline assessments may be collected at a
separate visit up to 14 days before the patient is enrolled and randomized.
Laboratory measurements may be collected within either 4 weeks or 90 days
prior to the date of randomization, depending on the laboratory test.
« There should be a minimum of 2 weeks between each study visit.
« Data for the baseline and follow-up visits may be collected anytime within
the visit window.
Table 9: Visit Schedule Phase | (0-6 months) or Phase II
Visit Window
Days/Weeks
Baseline*
Week 2 +3 days
Month 1* +15 days
Month 2 +15 days
Month 3 £15 days
Month 4 £15 days
Month 5 £15 days
Month 6 -15 to +30
*Every monthly visit scheduled will be calculated from the baseline visit date (Phase 1), using the
average amount of days per month. If a patient does not come in within the visit window, every
attempt should be made to get them in for a clinic visit as soon as possible.
Table 10: Visit Schedule Phase I (6-12 months)
Visit Window
(Weeks)
Month 12* -15 to +30
* Since baseline/treatment administration (Phase 1)
4.1.2. Phase Il: Rescue treatment
In case of the first randomized treatment failure due to intolerability or lack of efficacy within the
first six months of treatment, the treatment assignment will be switched to the alternate treatment.
At this point, the patient will receive the antimetabolite not originally randomized to and will be
followed an additional 6 months or until failure of the second treatment.
30

```

### DOC-003 PDF page 95

[Direct source](../../../../joi190092supp2_prod.pdf#page=95)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial           January 6, 2017 - Version 4.5
 Manual of Operation and Procedures



Patients will be given 2 weeks to enter into Phase II after treatment failure in Phase I. If patients
do not enter within the 2-week window, they should be treated according to best medical judgment
of their physician. If the physician believes a patient would benefit from treatment in Phase II, but
there is an exceptional circumstance preventing the patient from entering Phase II within the 2-
week window, contact the Coordinating Center for assistance.

        Guidelines for Visit Schedule II
        •     Day 1 corresponds to the Baseline-II visit, which is also the first day the patient
              receives rescue treatment with the medication not initially received. Day 1 may
              be its own visit date (i.e. if within 2 weeks of the end of Phase I). Alternatively
              Day 1 may be the same day as the last day of Phase I. All study forms should
              indicate what visit it is for Phase I and what visit it is for Phase II, if applicable.
              See the following example below.

     Phase       ☒1              ☒2

      Visit    ☒ Baseline    ☐ Two weeks            ☐ Non-study visit (treatment failure only)

               Month:        ☐ 1        ☐     2     ☐ 3       ☐    4     ☐      5   ☒   6        ☐ 9      ☐ 12


        •     Visit dates are determined based on the date of the Baseline-II visit (which may
              be the same date as Phase I treatment failure), and may not be changed.
        •     The Baseline-II visit form should be completed to gather information on any
              changes in health status or medications.
        •     There should be a minimum of 2 weeks between each study visit.
        •     Data for the follow-up visits may be collected anytime within the visit window.

        4.1.3. Non-study visits

Despite the regular follow-up outlined in the visit schedules above, it is anticipated that some
patients will have inflammation that is difficult to control or be intolerant to the drug, leading to
additional visits. These additional visits may not fall within the study visit window. It is possible that
the circumstances leading to such visits may result in changes to oral or topical corticosteroid
dose, or a declaration of treatment failure and a need for rescue treatment. If treatment failure is
declared at a non-study visit, all of the forms required at the time treatment failure is declared
should be completed.

        Guidelines for non-study visits

        •     Any changes to oral or topical corticosteroid dose will be noted on the appropriate form
              during the next scheduled study visit.
        •     If a treatment failure is declared at a non-study visit during follow-up while being treated
              during…
                   • Phase I (initial randomized treatment): Record a treatment failure using
                       Treatment Assessment Form. Perform Baseline II visit at this time or within 14
                       days. Phase II rescue treatment can start immediately.
                   • Phase II: Record a treatment failure using the Treatment Assessment Form.
                       Patient should continue to be followed until 6 months and 6th month data collected.
                   • If treatment failure is declared at a non-study visit, an attempt should be made to
                       collect as much information as possible, including the forms listed in Section 4.2.
                                                                                                                    31


```

### DOC-003 PDF page 96

[Direct source](../../../../joi190092supp2_prod.pdf#page=96)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
4.2. Study form completion schedule
ee
Baseline | Week | Followup | Treatme | Follow up | Baseline: | Week | Followup | Treatment | Follow up
:Phasel | 2 months nt months Phase 2 months | Failure month
15,9 Failure 6 &12 re 15 anytime” 6
anytime"
Eligibility” x
‘Screening Form
Baseline History x
Form
Clinical Eye x x x x x x x
Exam Form
Secondary
Clinical Eye x x x x x
Exam Form
em |e} Pete te] | Pee
Form
portm Pep Pepe pe ee
[frasrom Poe PT fT Pe pe Pt ey
Laboratory x x x [co x x x () x
Report Form
Adverse Event x x x x x x x x x
Checklist
Vision Related x x x x x
Quality of Life
Health Related x x x x x
Quality of Life
Treatment
‘Assessment x x x x x x x x x x
Form
Patient x x x x x x x x
Calendar"
Protocol (x) x) x) (x) (x) (x) x x (x) (x)
Adverse Event ®) ®) c) co) ®) ®) ®) ®) ®) ®)
Narrative
og
*Note that treatment failure may be declared at a scheduled study visit or at a non-study visit;
All (x) are only to be filled out if applicable.
“If not switching on the same day as Phase | treatment failure
“*Patients will complete this form and bring to the study coordinator for review
32

```

### DOC-003 PDF page 97

[Direct source](../../../../joi190092supp2_prod.pdf#page=97)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


4.3. Phase I Enrollment/Baseline visit

    The Phase I Enrollment/Baseline visit should occur after the patient has been screened and
    determined to be eligible for the study. Screening is a process that should occur before or on
    the date of the patient’s Enrollment/Baseline visit. The baseline eye exam and other baseline
    assessments may be collected at a separate visit up to 14 days before the patient is enrolled
    and randomized, with the exception of laboratory measurements which may be collected
    within 4 weeks or 90 days prior to or on the date of randomization (depending on the test).

    Many patients will still have active enough inflammation at the time of enrollment to meet
    criteria (≥1+ AC cells, ≥1+ vitreous haze by NEI scale, or active retinal/choroidal
    inflammation). However, some patients may have had active inflammation when screened
    (within 14 days prior to enrollment) but at the time of enrollment, the inflammation is
    improved because of steroid treatment. As long as the inflammation met inclusion criteria
    within this 14 day period, those values can be used for the baseline exam (enrollment exam).
    If there is a patient whom you think is very likely to be enrolled in the next 14 days but you
    are still waiting for some screening labs, it is fine to go ahead and consent and obtain the
    baseline study assessments (eye exam with secondary grader using both NEI and Miami
    scales for vitreous haze, fundus photos, OCT, questionnaires, etc.), as long as you do not
    randomize. Randomization can only occur once all eligibility criteria have been verified. The
    inflammation recorded on the baseline Clinical Eye Exam form needs to meet inflammation
    eligibility criteria.

       4.3.1. Consent and eligibility evaluation

         Procedures for obtaining consent include explaining the patient’s disease, prognosis, and
         treatment options, discussing the risks and benefits of participation, and addressing the
         patient’s questions and concerns. After explaining the nature of the study and the rights
         and responsibilities of the patient, the ophthalmologist and/or the study coordinator will
         obtain written consent from the subject, or written minor assent and parental consent if
         applicable. The subject is assured that participation in this study is voluntary and he/she
         can withdraw at any time if he/she feels uncomfortable.

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
         randomization and the official Baseline-I visit. All other criteria must be met at the time the
         consent form is signed and randomization occurs (except the active inflammation criteria
         which must be met within 14 days prior to randomization).




                                                                                                           33


```

### DOC-003 PDF page 98

[Direct source](../../../../joi190092supp2_prod.pdf#page=98)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures



       4.3.2. Randomization
         Randomization treatment assignment takes place during the Baseline-I visit after
         eligibility has been determined and the consent forms have been signed by the patient.
         In some cases randomization can occur on the same day that patient is screened for
         enrollment, if the patient signs the consent form on that day. If the patient wishes to
         come back at a later time to sign the consent forms, randomization will occur on the
         date they return. If a patient returns to sign the consent and enroll on a different date
         to his or her screening visit, he or she must have had the relevant laboratory tests
         within 4 weeks prior to enrollment for trial eligibility.

         After obtaining the written consent, the study coordinator will assign the next
         identification number from the patient ID list. The coordinator will then log into the
         REDCap database to perform the randomization for the corresponding patient ID. The
         coordinator will take note of the treatment assigned by REDCap, dispense the assigned
         treatment to the patient, and review dosing instructions with the patient.


         4.3.3. Procedures for data collection
       Required study procedures include the following:

             •    Medical and Treatment History
             •    Clinical eye exam
             •    Visual acuity exam
             •    Optical Coherence Tomography (OCT)
             •    Fundus photography
             •    Laboratory measurements
             •    Health-related quality of life questionnaire
             •    Vision-related quality of life questionnaire(s)

         4.3.4. Specimens

         The following specimens will be collected for laboratory measurements within 4 weeks
         prior to enrollment:
             • Blood for complete blood count (CBC with differential, limited to percentages of
                  neutrophils and lymphocytes)
             • Blood for CD4 at AEH, KKESH, and UCSF sites only
             • Blood for serum chemistry panel (AST, ALT, creatinine)
             • Blood or urine pregnancy test (all female patients, excluding those that
                  are post-menopausal)

         The following specimens will be collected for laboratory measurements within 90 days prior
         to enrollment:

             •    Hepatitis B surface antigen (HBsAg)
             •    Hepatitis C antibody
             •    Tuberculin skin test
             •    Interferon gamma release assay
             •    Chest radiograph
             •    Syphilis (RPR/VDRL/other non-specific)
             •    Syphilis (FTA-ABS/MHATP/other specific)
                                                                                                           34


```

### DOC-003 PDF page 99

[Direct source](../../../../joi190092supp2_prod.pdf#page=99)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures



          4.3.5. Forms for data collection

          The following forms will be filled out as part of the Baseline-I visit:
             • Patient Consent Forms
             • Eligibility/Screening Form
             • Baseline History Form
             • Clinical Eye Exam Form
             • Secondary Clinical Eye Exam Form
             • Right Eye Visual Acuity Form
             • Left Eye Visual Acuity Form
             • OCT Form
             • Fundus Photography Form
             • Laboratory Report Form
             • Quality of Life Questionnaire Forms
             • Treatment Assessment Form
             • Protocol Deviation Form (if applicable)
4.4. Follow-up visits

     It is strongly encouraged for all follow up data to be collected within the study visit window, but
     should be collected regardless.

     All Phase II procedures and protocol are the same as Phase I. For Phase I patients who
     are continuing on the same medication, physicians can see the patients as often as they
     would like. However, for purposes of this study we will only be recording information at
     Month 9 and Month 12, or a non-study visit that leads to treatment failure.

     Laboratory test results will be collected monthly.

        4.4.1. Procedures for data collection

          Required study procedures include the following:
              • Clinical eye exam
              • Secondary Clinical eye exam*
              • Visual acuity exam
              • Optical Coherence Tomography
              • Fundus Photography*
              • Laboratory measurements
              • Quality of Life Questionnaire Forms*
          *Phase 1: treatment failure and 6 month visit (whichever is first), 12 month visit; Phase 2:
          treatment failure and 6 month visit.

        4.4.2. Specimens

          The following specimens will be collected for laboratory measurements:
             • Blood for complete blood count (CBC with differential, limited to percentages of
                  neutrophils and lymphocytes)
             • Blood for CD4 at AEH, KKESH, and UCSF sites only at Baseline, Month 3, 6, &12
             • Blood for serum chemistry panel (AST, ALT, creatinine)
             • Blood or urine pregnancy test (all female patients, excluding those that
                  are post- menopausal)
                                                                                                            35


```

### DOC-003 PDF page 100

[Direct source](../../../../joi190092supp2_prod.pdf#page=100)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures




        4.4.3. Forms for data collection
          The following forms will be filled out as part of the follow-up visits:
             • Clinical Eye Exam Form
             • Secondary Clinical Eye Exam Form*
             • Right Eye Visual Acuity Form
             • Left Eye Visual Acuity Form
             • OCT Form
             • Fundus Photography Form*
             • Laboratory Report Form
             • Adverse Event Checklist
             • Medication Log
             • Patient Medication Calendar (to be completed by the patient)
             • Treatment Assessment Form
             • Adverse Event Log (update if necessary)
             • Quality of Life Questionnaire Forms *
             • Serious Adverse Event Narrative Form (if applicable)
             • Patient Dropout Form (if applicable)
             • Protocol Deviation Form (if applicable)

          *Phase 1: baseline, treatment failure and 6 month visit, 12 month visit; Phase 2: treatment
          failure and 6 month visit; Treatment failure anytime (study or non-study visit)
          For follow-up visits, all the above procedures and forms should be completed for all
          patients, regardless of if they are taking the medication or compliant with study visits.

4.5. Baseline Phase II

     This visit may occur on the same day as treatment failure in Phase I, if the patient proceeds
     directly to Phase II. If both visits occur on the same day, study coordinators will mark the
     Phase I visit and Phase II visit at the same time on the case report forms. However, patients
     have up to two weeks to come back to clinic and begin Phase II after treatment failure in Phase
     I. In this case, complete the Baseline Phase II form packet on the date Baseline II starts.

     4.5.1. Eligibility

     In Phase I, if failure is due to efficacy or tolerability or for selected cases for safety (if deemed
     safe by the Medical Monitor), the patient will be considered as eligible for Phase II of the
     study. If there is a serious adverse event in Phase I, deemed to be related to the study drug
     by the Medical Monitor, the patient will be declared a treatment failure. The Medical Monitor
     will determine if it is safe for the patient to enter Phase II. If not, the patient should still be
     followed for 6 months.

     As in Phase I, there is no mandated separate visit for eligibility screening in Phase II. If the
     patient is declared a treatment failure in Phase I for any reason other than an SAE deemed
     to be related to the study drug (by the Medical Monitor), he/she may immediately proceed to
     Phase II. Any reason for eligibility failure for Phase II will be captured in the adverse event
     log of the last Phase I visit, thus there is no need to have a separate eligibility screening
     form.



                                                                                                            36


```

### DOC-003 PDF page 101

[Direct source](../../../../joi190092supp2_prod.pdf#page=101)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


4.6. Non-study visits

     Despite frequent study visits, some patients may need additional visits with their
     ophthalmologist according to standard of care that do not fall within study visit windows.
     Required data collection during these non-study visits is limited to adverse event reporting
     and declaration of treatment failure if it occurs. It is preferable that treatment failure is
     declared at a regularly scheduled study visit rather than a non-study visit, however if it is
     necessary the physician can decide to do so.

        4.6.1. Study Procedures

          Every attempt should be made to obtain all study procedures at a non-study visit if
          treatment failure is being declared. However, if this is not possible the required study
          procedures include the following:
              • Clinical eye exam (if treatment failure is declared)

        4.6.2. Specimens

          No specimens are required during non-study visits.


        4.6.3. Forms for data collection

          The following forms will be filled out at non-study visits only if treatment failure is declared.
          Every attempt should be made to acquire information for all other forms. However, if this is not
          possible, at the minimum the following must be completed:

              •    Clinical Eye Exam Form
              •    Treatment Assessment Form
              •    Quality of Life
              •    Medication Log
              •    Adverse Event Checklist
              •    Adverse Event Log (update if necessary)
              •    Serious Adverse Event Narrative Form (if applicable)




                                                                                                            37


```

### DOC-003 PDF page 102

[Direct source](../../../../joi190092supp2_prod.pdf#page=102)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


5. Study examinations and procedures

     5.1. Quality of life questionnaire administration

     All patients will be asked to complete standard quality of life questionnaires related to
     overall health and visual function at baseline visits as well as at 6 months or treatment
     failure (whichever is first) in order to measure quality of life outcomes. Patients who
     experience treatment success with Phase I treatment and continue into Phase I (6-12
     months) also complete questionnaires at the 12-month visit, or earlier if treatment failure is
     declared. The following questionnaires will be administered:

     If treatment failure occurs prior to 6 months (Phase I and Phase II) questionnaires should also
     be collected at the time of treatment failure as well as 6 months.

     Health-related quality of life

     • SF-36 questionnaire (all patients)

     Vision-related quality of life

     • NEI-VFQ-25 (all patients)
     • IND-VFQ (Indian patients only)

     Given data suggesting that SF-36 scores vary by method of administration such that
     patients overstate their quality of life in clinic interviews, questionnaires will be self-
     administered whenever possible at clinic appointments. Additionally the NEI-VFQ should
     be self-administered whenever possible. It is anticipated that some patients will not have
     adequate visual function to complete the questionnaires on their own, and some patients
     may also be illiterate. In such cases, the coordinator will read the questions aloud to the
     patient and record the patient’s answers on the appropriate questionnaire forms (Section
     A.13). It is very important that the questions are answered in their original form, so
     coordinators should never rephrase or interpret questions for the patient.


     5.2.A Refraction and visual acuity (PRIMARY – FOR LETTER VISION CHARTS)

        5.2.1.A Refraction procedure

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

                                                                                                            38


```

### DOC-003 PDF page 103

[Direct source](../../../../joi190092supp2_prod.pdf#page=103)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial           January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


     The examiner will use Chart R (Precision Vision Chart Version 2110) for manifest
     refraction. Each eye is refracted at four meters unless the visual acuity measured at this
     distance on chart R is worse than 20/200 (defined as missing 2 or more letters on the top
     line, the 20/200 or 6/60 line). This subject must then be moved to a distance of one meter
     from the study visual acuity chart, and refraction must be performed and recorded at this
     distance.

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

Vision with                                                    Cylinder
Best                           Sphere                Use correct Jackson Cross             Sphere Refinement
Correction                                                Cylinder as below
                        Power        Increment        Axis     Power Increment              Power       Increment
20/10-20/80             +0.50          +0.50         0.50       0.25      +0.25             +0.37          +0.25
6/3-6/24                - 0.37         - 0.25                             -0.25              -0.37         -0.25
 (4 meters)             +0.50          +0.50                                                +0.37          +0.25
20/100-20/200           +1.00           +1.00         1.00         1.00         +1.00       +0.50         +0.50
6/30-6/60               -1.00           -1.00                                   -1.00       -0.50         -0.50
 (4 meters)             +1.00           +1.00                                               +0.50         +0.50
<20/200                 +2.00           +2.00         1.00         1.00         +1.00       +1.00         +1.00
<6/60                   -2.00           -2.00                                   -1.00       -1.00         -1.00
 (1 meter)              +2.00           +2.00                                               +1.00         +1.00

Examples for each visual acuity level are detailed below.


For Patients with Visual Acuity of 20/10-20/80 (6/3-6/24):

          Determine Sphere Power
              •    Ask patient to identify the smallest possible line that he/she can see on the Chart
                   R;
              •    With the subject looking at the smallest line legible on the visual acuity chart,
                   place a +0.50 spherical lens in front of the eye being tested. Ask the subject, “Is
                                                                                                                    39


```

### DOC-003 PDF page 104

[Direct source](../../../../joi190092supp2_prod.pdf#page=104)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


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
             •    Remember, if the patient reports that the -0.37 lens makes the vision better but if
                  s/he is unable to read more letters, do not change spherical lens by -0.25.
             •    If the -0.37 spherical lens does not allow the patient to read more letters or if it
                  makes the vision worse, recheck using the +0.50 lens
             •    If the +0.50 lens makes vision better or the same, repeat above sequence
             •    If the +0.50 lens makes vision worse, move on to cylindrical testing

         Determine and refine cylinder axis
       The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
       refraction.

             •    Ask the subject to look at a letter on a line of Chart R which is one line larger
                  than the smallest line he/she could read (one above threshold);
             •    If no cylinder is present in the beginning approximate refraction, place the
                  +/- 0.50 diopter cross-cylinder with the positive axis first at 90º and then at 180º,
                  asking if either position makes the letter clearer;
             •    If the patient prefers either one of these positions, place a +0.50 cylindrical lens
                  in the trial frame aligned with the preferred axis;
             •    If the patient did not prefer cylinder at axis 90° or 180°, position the cross
                  cylinder with the positive axis first at 45° then 135°;
             •    Ask if the patient prefers either of these positions;
             •    If so, place a +0.50 cylinder lens in the trial frame aligned with the preferred axis;
             •    If the subject prefers none of the four positions, no further cylinder testing is
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




                                                                                                           40


```

### DOC-003 PDF page 105

[Direct source](../../../../joi190092supp2_prod.pdf#page=105)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
Table: Axis step sizes for refinement of cylinder.
Cylinder Power | Axis Step Sizes
<1.00D
Tooto<2000 |__|
2.00t0<3.00D [|
3,00t0<5.000 | 2 _|
5.00t0<600D |__|
Refine cylinder power

+ Ask the subject to look at the lowest line on the visual acuity chart which can be
read;

= Switch to +/- 0.25 diopter cross-cylinder;

+ Align the + 0.25 diopter cross-cylinder first with the positive axis and then
with the negative axis coincident with the cylinder axis. Ask the subject which is
better;

+ If the subject prefers the negative axis coincident with the cylinder axis,
decrease the power of the cylinder in the trial frame by +0.25 diopter;

+ If a subject indicates a change that would introduce negative cylinder power,
remove all cylinder power and continue testing for positive cylinder power at an
axis 90° away from the previous axis;

+ If the subject prefers the positive axis coincident with the cylinder axis,
increase the power of the trial frame by +0.25 diopter and retest;

+ Beginning with cylinder powers of 1.00 diopter or more, for each 0.5 diopter
change in cylinder power, adjust the sphere power by 0.25 diopter of the
opposite sign; this is done to maintain the spherical equivalent.

Spherical refinement
End the refraction by performing the spherical refinement step.

+ With the subject looking at the smallest line legible on the visual acuity chart,
place a +0.37 spherical lens in front of the eye being tested. Ask the subject, “Is
vision better, worse, or the same?”

+ If the subject responds that vision is made better or if there is no change,
replace the spherical lens with one that is +0.25 more plus;

+ Continue to check with the +0.37 lens to see if the subject will accept more
plus by repeating the step above;

+ When an additional +0.37 lens makes the subject’s vision worse, remove the +0.37
lens;

+ Then hold a -0.37 spherical lens over the eye;

+ If this -0.37 lens improves the subject's vision, even by one letter, replace the
spherical lens in the trial frame by one that is -0.25 more minus;

+ Continue presenting the -0.37 lens to see if there is any further improvement in
vision;

+ When an additional -0.37 lens does not improve vision;

+ Present the +0.37 lens, again asking “if vision is better, worse or the same?”

+ If patient responds that vision is better or the same, repeat spherical refinement
testing as detailed above;

+ If patient responds that vision is worse, testing is complete.

+ Remember to always end the refraction by checking with plus lenses.

4

```

### DOC-003 PDF page 106

[Direct source](../../../../joi190092supp2_prod.pdf#page=106)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


         For Patients with Visual Acuity of 20/100-20/200 (6/30-6/60):

         Determine Sphere Power
             •    Ask patient to identify the smallest possible line that he/she can see on the Chart
                  R;
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
             •    Remember, if the patient reports that the -1.00 lens makes the vision better but if
                  s/he is unable to read more letters, do not change spherical lens by -1.00.
             •    If the -1.00 spherical lens does not allow the patient to read more letters or if it
                  makes the vision worse, recheck using the +1.00 lens; recheck using +1.00 lens
             •    If the +1.00 lens makes vision better or the same, repeat above sequence
             •    If the +1.00 lens makes vision worse, move on to cylindrical testing;
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
                 asking if either position makes the letter clearer;
             • If the patient prefers either of these positions, place a +1.00 cylindrical lens in
                 the trial frame at the preferred axis;
             • If the patient did not prefer cylinder at axis 90° or 180°, position the cross
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
                                                                                                           42


```

### DOC-003 PDF page 107

[Direct source](../../../../joi190092supp2_prod.pdf#page=107)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures

+ If the subject responds that neither position is better and if this was the first test
of axis position, move the axis of the cylinder in the trial frame 15° to the right or
left and repeat;

+ If the subject prefers one position to the other, rotate the cylinder toward the
preferred positive axis of the cross-cylinder in the step sizes recommended (see
Table below) and repeat. (If the subject states that one position of the cross-
cylinder is no better than the other position, proceed to refining cylinder power).

Table: Axis step sizes for refinement of cylinder
[<to0D | to”
[S.00to<a0oD [1 |
Refine cylinder power

+ Ask the subject to look at the lowest line on the visual acuity chart which can be
read;

+ Align the + 1.00 diopter cross-cylinder first with the positive axis and then
with the negative axis coincident with the cylinder axis. Ask the subject which is
better;

+ If the subject prefers the negative axis coincident with the cylinder axis,
decrease the power of the cylinder in the trial frame by +1.00 diopter;

+ If a subject indicates a change that would introduce negative cylinder power,
remove all cylinder power and continue testing for positive cylinder power at an
axis 90° away from the previous axis;

+ If the subject prefers the positive axis coincident with the cylinder axis,
increase the power of the trial frame by +1.00 diopter and retest;

= Beginning with cylinders of 1.00 diopter or more, for each 0.5 diopter change in
cylinder power, adjust the sphere by 0.25 diopter of the opposite sign; this is
done to maintain the spherical equivalent.

Spherical refinement
End the refraction by performing the spherical refinement step.

+ With the subject looking at the smallest line legible on the visual acuity chart,
place a +0.50 spherical lens in front of the eye being tested. Ask the subject, “Is
vision better, worse, or the same?”

+ If the subject responds that vision is made better or if there is no change,
replace the spherical lens with one that is +0.50 more plus;

+ Continue to check with the +0.50 lens to see if the subject will accept more
plus by repeating the step above;

+ When an additional +0.50 lens makes the subject’s vision worse, remove the +0.50
lens

+ Then hold a -0.50 spherical lens over the eye;

+ If this -0.50 lens improves the subject's vision, even by one letter, replace the
spherical lens in the trial frame by one that is -0.50 more minus;

+ Continue presenting the -0.50 lens to see if there is further improvement in vision;

+ When an additional -0.50 lens does not improve vision;

+ Show the patient the +0.50 lens, again asking “if vision is better, worse or the

43

```

### DOC-003 PDF page 108

[Direct source](../../../../joi190092supp2_prod.pdf#page=108)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


                  same?”
             •    If patient responds that vision is better or the same, repeat spherical refinement
                  testing as detailed above;
             •    If patient responds that vision is worse, refraction testing is complete.
             •    Remember to always to end the refraction by checking with plus power.

         For Patients with Visual Acuity <20/200 (<6/60):

         Determine Sphere Power
         NOTE: If refraction cannot be performed at 4 meters, defined as missing 2 or more
         letters on the largest line, then the subject should be moved to 1 meter and the above
         refraction sequence followed. At 1 meter, a + 0.75 spherical lens is added to the
         beginning approximate refraction to adjust for the accommodative difference between 4
         and 1 meter.
              • Ask patient to identify the smallest possible line that he/she can see on the Chart
                 R;
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
              • Remember, if the patient reports that the -2.00 lens makes the vision better but if
                 s/he is unable to read more letters, do not change spherical lens by -2.00.
              • If the -2.00 spherical lens does not allow the patient to read more letters or if it
                 makes the vision worse, retest using +2.00 lens;If the +2.00 lens makes vision
                 better or the same, repeat above sequence;
              • If the +2.00 lens makes vision worse, move onto cylindrical testing;
              • NOTE: if visual acuity improves significantly during manifest refraction, the
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
                 the trial frame at the preferred axis;
             • If the patient did not prefer cylinder at axis 90° or 180°, position the cross
                                                                                                           44


```

### DOC-003 PDF page 109

[Direct source](../../../../joi190092supp2_prod.pdf#page=109)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
cylinder with the positive axis first at 45° then 135°;

+ Ask if the patient prefers either of these positions;

= If so, place a +1.00 cylinder lens in the trial frame at the preferred axis;

+ If the subject prefers none of the four positions, no further cylinder testing is
required.

+ If cylinder is present in the beginning approximate refraction or if you have
added +1.00 cylinder power in the above step, position the +/- 1.00 diopter
cross-cylinder first with the positive axis 45° to the right of the cylinder axis
(position one), and secondly with the positive axis at 45° to the left of the cylinder
axis (position two). Ask the subject which position improves the vision (position one
or position two?);

+ If the subject responds that neither position is better and if this was the first test
of axis position, move the axis of the cylinder in the trial frame 15° to the right or
left and repeat;

+ If the subject prefers one position to the other, rotate the cylinder toward the
preferred positive axis of the cross-cylinder in the step sizes recommended (see
table below) and repeat. (If the subject states that one position of the cross-
cylinder is no better than the other position, proceed to refining cylinder power).

Table: Axis step sizes for refinement of cylinder
[<t00D Tt
[4.00to<200D | 5°
[5.00to<8.00D [1 |
Refine cylinder power

+ Ask the subject to look at the lowest line on the visual acuity chart which can be
read;

+ Align the + 1.00 diopter cross-cylinder first with the positive axis and then
with the negative axis coincident with the cylinder axis. Ask the subject which is
better;

+ If the subject prefers the negative axis coincident with the cylinder axis,
decrease the power of the cylinder in the trial frame by 1.00 diopter;

+ If a subject indicates a change that would introduce negative cylinder power,
remove all cylinder power and continue testing for positive cylinder power at an
axis 90° away from the previous axis;

+ If the subject prefers the positive axis coincident with the cylinder axis,
increase the power of the trial frame by +1.00 diopter and retest;

+ Beginning with cylinders of 1.00 diopter or more, for each 0.5 diopter change in
cylinder power, adjust the sphere by 0.25 diopter of the opposite sign, this is
done to maintain the spherical equivalent.

Spherical refinement
End the refraction by performing the spherical refinement
step.

+ With the subject looking at the smallest line legible on the visual acuity chart,
place a+1.00 spherical lens in front of the eye being tested. Ask the subject, “Is

45

```

### DOC-003 PDF page 110

[Direct source](../../../../joi190092supp2_prod.pdf#page=110)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


                  vision better, worse, or the same?”
             •    If the subject responds that vision is made better or if there is no change,
                  replace the spherical lens with one that is +1.00 more plus;
             •    Continue to check with the +1.00 lens to see if the subject will accept more
                  plus by repeating the step above;
             •    When an additional +1.00 lens makes the subject’s vision worse, remove the +1.00
                  lens
             •    Then hold a -1.00 spherical lens over the eye;
             •    If this -1.00 lens improves the subject’s vision, even by one letter, replace the
                  spherical lens in the trial frame by one that is -1.00 more minus;
             •    Continue presenting the -1.00 lens to see if there is further improvement in vision;
             •    When an additional -1.00 lens does not improve vision;
             •    Present the +1.00 lens, again asking “if vision is better, worse or the same?”
             •    If patient responds that vision is better or the same, repeat spherical refinement
                  testing as detailed above;
             •    If patient responds that vision is worse, testing is complete.
             •    Remember to always to end the refraction by checking with plus power.

         Record the lens correction obtained during manifest refraction for the right eye on the
         appropriate examination forms in the section for visual acuity measurements (Section
         A.5). Then proceed to refraction of the left eye, following steps as outlined above.

       5.2.2.A Visual acuity procedure
        Visual acuity measurement is necessary for a secondary outcome in this trial.
        Therefore, we have created a standardized method that aims to minimize any bias from
        either the examiner or the patient. This has been adapted from the Visual Acuity
        protocols from the Age Related Eye Disease Study (AREDS 1999)32, and the Aravind
        Eye Hospital’s Practical Guide to Refraction33 and is similar to the method we are
        currently using at Aravind Eye Hospital and Proctor/UCSF for the NEI funded Steroids
        for Corneal Ulcers Trial and the Mycotic Ulcer Treatment Trials.

         Visual Acuity Charts
         The following equipment is used: a set of three charts, which are modified Bailey-Lovie
         charts, Charts 1, 2 and R (Precision Vision Chart 2110, 2111 and 2112, respectively).
         Each chart consists of 14 lines of high-contrast letters. There is a geometric
         progression of letter size (and, thus, an arithmetic progression of the logarithm of
         minimum angle of resolution) from line to line.

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
                                                                                                           46


```

### DOC-003 PDF page 111

[Direct source](../../../../joi190092supp2_prod.pdf#page=111)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures




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
                                                                                                           47


```

### DOC-003 PDF page 112

[Direct source](../../../../joi190092supp2_prod.pdf#page=112)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures




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
                  line, at the 4-meter distance, and is encouraged to read as many letters as
                  possible.
             •    If the patient cannot identify a letter, they are encouraged to guess. Only one
                  response is allowed per letter.
             •    The examiner must ensure that the patient does not squint (creating a pin-hole
                  effect) or lean forward (reducing the distance to the chart).
             •    Once a patient has given a response for a letter and has moved on to provide a
                  response for the next letter, any corrections of previous response will not be
                  accepted.
             •    However, if the patient has given a response for a letter and has not yet
                  moved on to provide a response for the next letter, a correction of the previous
                  response is accepted.
             •    If the subject gives two possible responses for a letter, tell the patient to commit
                  to one answer. The examiner CANNOT, at any time, give the patient any
                  indication as to whether a response is correct or incorrect.
             •    In the case that the patient reads less than 20 letters at 4 meters, move the
                  patient or the chart so that there is a distance between the two of 1 meter.
             •    Visual acuity will then be retested at this 1 meter distance.
             •    Only the first 6 rows of letters need to be read at 1 meter.
             •    If no letters are read at 1 meter, then the examiner must proceed to Low Vision
                  Testing (see below), starting with Count Fingers testing. If the patient does not
                  adequately Count Fingers, proceed to Hand Motion. If the patient does not
                  adequately recognize Hand Motion, then proceed to Light Perception.

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
                                                                                                           48


```

### DOC-003 PDF page 113

[Direct source](../../../../joi190092supp2_prod.pdf#page=113)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


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
         the visit.

         The Snellen equivalent, defined as the Snellen ratio corresponding to the most difficult
         line for which the subject read at least 4 of 5 letters correctly, will also be entered by the
         examiner on the 4-meter Visual Acuity Form (Section A.5).
         The data entry staff will enter the number correct on each row at 4 meters, and if
         applicable, 1 meter and low vision testing results (They will not enter which letters the
         examiner circled, i.e., which letters the patient identified correctly.). Coordinating center
         personnel will double check the data entered by the examiner and data entry staff.

       5.2.3.A     Visual acuity training and certification
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

                                                                                                           49


```

### DOC-003 PDF page 114

[Direct source](../../../../joi190092supp2_prod.pdf#page=114)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


          Room certification will be performed and recorded (Room Certification Form, section
          B.2) to ensure that all study rooms meet illumination, equipment, and distance
          requirements. Logs should be kept to document dates of light box bulb replacement.

          Certification is valid for a period 18 months (± 2 months) from the date of
          certification. The process should begin as soon as possible, as technicians must be
          certified before the first study subject is seen. A minimum of two certified technicians
          are required at each site. The visual acuity measurement schedule may be found on
          the Study Forms Completion Schedule.


5.2.B Refraction and visual acuity (PROTOCOL FOR TUMBLING E CHART)

        5.2.1.B Refraction procedure

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

                                                                                                            50


```

### DOC-003 PDF page 115

[Direct source](../../../../joi190092supp2_prod.pdf#page=115)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


       Please refer to the table below to ensure that proper lenses are used for the appropriate
       visual acuity level:
Vision with                                            Cylinder
Best                        Sphere          Use correct Jackson Cross Sphere Refinement
Correction                                       Cylinder as below
                     Power      Increment    Axis      Power Increment       Power     Increment
6/3-6/24              +0.50       +0.50      0.50       0.25      +0.25       +0.37      +0.25
20/10-20/80           -0.37        -0.25                          -0.25       -0.37       -0.25
(4 meters)            +0.50       +0.50                                       +0.37      +0.25
6/30-6/60             +1.00       +1.00      1.00       1.00      +1.00       +0.50      +0.50
20/100-20/200         -1.00        -1.00                          -1.00       -0.50       -0.50
(4 meters)            +1.00       +1.00                                       +0.50      +0.50
<6/60                 +2.00       +2.00      1.00       1.00      +1.00       +1.00      +1.00
<20/200               -2.00        -2.00                          -1.00       -1.00       -1.00
(1 meter)             +2.00       +2.00                                       +1.00      +1.00

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
              •    Remember, if the patient reports that the -0.37 lens makes the vision better but if
                   s/he is unable to read more letters, do not change spherical lens by -0.25.
              •    If the -0.37 spherical lens does not allow the patient to read more letters or if it
                   makes the vision worse, retest using the +0.50 lens;
              •    If the +0.50 lens makes vision better or the same, repeat above sequence
              •    If the +0.50 lens makes vision worse, move on to cylindrical testing

          Determine and refine cylinder axis
        The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
        refraction.

              •    Ask the subject to look at a letter on a line of Chart R which is one line larger
                   than the smallest line he/she could read (one above threshold);
              •    If no cylinder is present in the beginning approximate refraction, place the
                   +/- 0.50 diopter cross-cylinder with the positive axis first at 90º and then at 180º,
                                                                                                            51


```

### DOC-003 PDF page 116

[Direct source](../../../../joi190092supp2_prod.pdf#page=116)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
asking if either position makes the letters clearer;

+ If the patient prefers either one of these positions, place a +0.50 cylindrical lens
in the trial frame aligned with the preferred axis;

+ If the patient did not prefer cylinder at axis 90° or 180°, position the cross
cylinder with the positive axis first at 45° then 135°;

+ Ask if the patient prefers either of these positions;

+ If So, place a +0.50 cylinder lens in the trial frame aligned with the preferred axis;

= If the subject prefers none of the four positions, no further cylinder testing is
required;

+ If cylinder is present in the beginning approximate refraction or if you have
added +0.50 cylinder power in the above step, position the +/- 0.50 diopter
cross-cylinder first with the positive axis 45° to the right of the cylinder axis
(position one), and secondly with the positive axis at 45° to the left of the cylinder
axis (position two). Ask the subject which position improves vision (position one or
position two?);

+ If the subject responds that neither position is better and if this was the first test
of axis position, move the axis of the cylinder in the trial frame 15° to the right or
left and repeat;

+ If the subject prefers one position to the other, rotate the cylinder toward the
preferred positive axis of the cross-cylinder in the step sizes recommended (see
Table below) and repeat. (If the subject states that one position of the cross-
cylinder is no better than the other position, proceed to refining cylinder power).

Table: Axis step sizes for refinement of cylinder.
[<to0D | te
[3.00to<500D | 2? |
[5.00% <8.00D [1 |

Refine cylinder power

+ Ask the subject to look at the lowest line on the visual acuity chart which can be
read;

+ Switch to +/- 0.25 diopter cross-cylinder;

+ Align the + 0.25 diopter cross-cylinder first with the positive axis and then
with the negative axis coincident with the cylinder axis. Ask the subject which is
better;

+ If the subject prefers the negative axis coincident with the cylinder axis,
decrease the power of the cylinder in the trial frame by +0.25 diopter;

+ If a subject indicates a change that would introduce negative cylinder power,
remove all cylinder power and continue testing for positive cylinder power at an
axis 90° away from the previous axis;

- If the subject prefers the positive axis coincident with the cylinder axis,
increase the power of the trial frame by +0.25 diopter and retest;

+ Beginning with cylinder powers of 1.00 diopter or more, for each 0.5 diopter
change in cylinder power, adjust the sphere power by 0.25 diopter of the
opposite sign; this is done to maintain the spherical equivalent.

Spherical refinement
End the refraction by performing the spherical refinement step.
52

```

### DOC-003 PDF page 117

[Direct source](../../../../joi190092supp2_prod.pdf#page=117)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


             •    With the subject looking at the smallest line legible on the visual acuity chart,
                  place a +0.37 spherical lens in front of the eye being tested. Ask the subject, “Is
                  vision better, worse, or the same?”
             •    If the subject responds that vision is made better or if there is no change,
                  replace the spherical lens with one that is +0.25 more plus;
             •    Continue to check with the +0.37 lens to see if the subject will accept more
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
             •    If an additional +1.00 lens makes the subject’s vision worse, remove the +1.00 lens
             •    Then hold a -1.00 spherical lens over the eye;
             •    If this -1.00 lens improves the subject’s vision, even by one letter, replace the
                  spherical lens in the trial frame by one that is -1.00 more minus;
             •    Remember, if the patient reports that the -1.00 lens makes the vision better but if
                  s/he is unable to read more letters, do not change spherical lens by -1.00.
             •    If the -1.00 spherical lens does not allow the patient to read more letters or if it
                  makes the vision worse, retest using the +0.50 lens;
             •    If the +1.00 lens makes vision better or the same, repeat above sequence;
             •    If the +1.00 lens makes vision worse, move on to cylindrical testing;
             •    NOTE: if visual acuity improves significantly during manifest refraction, the
                  examiner may need to change to trial lenses that are specified for the new level
                  of acuity for the remainder of the refraction. Please refer to the Trial Lens Guide
                  above.

         Determine and refine cylinder axis
         The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
         refraction.
             • Ask the subject to look at a letter on a line of Chart R which is one line larger
                                                                                                           53


```

### DOC-003 PDF page 118

[Direct source](../../../../joi190092supp2_prod.pdf#page=118)

```text
Firstine Antimetabolites as Sterold-sparing Treatment (FAST) Uveltis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures
than the smallest line he/she could read (one above threshold);

+ If no cylinder is present in the beginning approximate refraction, place the
+/- 1.00 diopter cross-cylinder with the positive axis first at 90° and then at 180°,
asking if either position makes the letters clearer;

+ If the patient prefers either of these positions, place a +1.00 cylindrical lens in
the trial frame at the preferred axis;

+ If the patient did not prefer cylinder at axis 90° or 180°, position the cross
cylinder with the positive axis first at 45° then 135°;

+ Ask if the patient prefers either of these positions;

+ If so, place a +1.00 cylinder lens in the trial frame at the preferred axis;

+ If the subject prefers none of the four positions, no further cylinder testing is
required;

+ If cylinder is present in the beginning approximate refraction or if you have
added +1.00 cylinder power in the above step, position the +/- 1.00 diopter
cross-cylinder first with the positive axis 45° to the right of the cylinder axis
(position one), and secondly with the positive axis at 45° to the left of the cylinder
axis (position two). Ask the subject which position improves the vision (position one
or position two?);

+ If the subject responds that neither position is better and if this was the first test
of axis position, move the axis of the cylinder in the trial frame 15° to the right or
left and repeat;

+ If the subject prefers one position to the other, rotate the cylinder toward the
preferred positive axis of the cross-cylinder in the step sizes recommended (see
Table below) and repeat. (If the subject states that one position of the cross-
cylinder is no better than the other position, proceed to refining cylinder power).

Table: Axis step sizes for refinement of cylinder
[<4.00p ft
[100to<200D [ 5°
[5.00t0<8.00D [1
Refine cylinder power

+ Ask the subject to look at the lowest line on the visual acuity chart which can be
read;

+ Align the + 1.00 diopter cross-cylinder first with the positive axis and then
with the negative axis coincident with the cylinder axis. Ask the subject which is
better;

+ If the subject prefers the negative axis coincident with the cylinder axis,
decrease the power of the cylinder in the trial frame by +1.00 diopter;

+ If a subject indicates a change that would introduce negative cylinder power,
remove all cylinder power and continue testing for positive cylinder power at an
axis 90° away from the previous axis;

+ If the subject prefers the positive axis coincident with the cylinder axis,
increase the power of the trial frame by +1.00 diopter and retest;

+ Beginning with cylinders of 1.00 diopter or more, for each 0.5 diopter change in
cylinder power, adjust the sphere by 0.25 diopter of the opposite sign; this is
done to maintain the spherical equivalent.

54

```

### DOC-003 PDF page 119

[Direct source](../../../../joi190092supp2_prod.pdf#page=119)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures



         Spherical refinement
         End the refraction by performing the spherical refinement step.
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
              • If an additional +2.00 lens makes the subject’s vision worse, remove the +2.00 lens
              • Then hold a -2.00 spherical lens over the eye;
              • If this -2.00 lens improves the subject’s vision, even by one letter, replace the
                 spherical lens in the trial frame by one that is -2.00 more minus;
              • Remember, if the patient reports that the -2.00 lens makes the vision better but if
                 s/he is unable to read more letters, do not change spherical lens by -2.00.
              • If the -2.00 spherical lens does not allow the patient to read more letters or if it
                 makes the vision worse, retest using the +2.00 lens;
              • If the +2.00 lens makes vision better or the same, repeat above sequence;
              • If the +2.00 lens makes vision worse, move on to cylindrical testing;
                                                                                                           55


```

### DOC-003 PDF page 120

[Direct source](../../../../joi190092supp2_prod.pdf#page=120)

```text
FirstJine Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial January 6, 2017 - Version 4.5
Manual of Operation and Procedures

+ NOTE: if visual acuity improves significantly during manifest refraction, the
examiner may need to change to trial lenses that are specified for the new level
of acuity for the remainder of the refraction. Please refer to the Trial Lens Guide
above.

Determine and refine cylinder axis
The following descriptions are for plus cylinders. Adjust accordingly for minus cylinder
refraction.

+ Ask the subject to look at a letter on a line of Chart R which is one line larger
than the smallest line he/she could read (one above threshold);

+ If no cylinder is present in the beginning approximate refraction, place the
+/- 1.00 diopter cross-cylinder with the positive axis first at 90° and then at 180°,
asking if either position makes the letters clearer;

+ If the patient prefers either of these positions, place a +1.00 cylindrical lens in
the trial frame at the preferred axis;

+ If the patient did not prefer cylinder at axis 90° or 180°, position the cross
cylinder with the positive axis first at 45° then 135°;

- Ask if the patient prefers either of these positions;

* If so, place a +1.00 cylinder lens in the trial frame at the preferred axis;

+ If the subject prefers none of the four positions, no further cylinder testing is required.

+ If cylinder is present in the beginning approximate refraction or if you have
added +1.00 cylinder power in the above step, position the +/- 1.00 diopter
cross-cylinder first with the positive axis 45° to the right of the cylinder axis
(position one), and secondly with the positive axis at 45° to the left of the cylinder
axis (position two). Ask the subject which position improves the vision (position one
or position two?);

+ If the subject responds that neither position is better and if this was the first test
of axis position, move the axis of the cylinder in the trial frame 15° to the right or
left and repeat;

+ If the subject prefers one position to the other, rotate the cylinder toward the
preferred positive axis of the cross-cylinder in the step sizes recommended (see
table below) and repeat. (If the subject states that one position of the cross-
cylinder is no better than the other position, proceed to refining cylinder power).

Table: Axis step sizes for refinement of cylinder
[<t00D Tt
[100% <2000 |_|
[.00te<800D | 1 |
Refine cylinder power

+ Ask the subject to look at the lowest line on the visual acuity chart which can be
read;

+ Align the + 1.00 diopter cross-cylinder first with the positive axis and then
with the negative axis coincident with the cylinder axis. Ask the subject which is
better;

+ If the subject prefers the negative axis coincident with the cylinder axis,
decrease the power of the cylinder in the trial frame by 1.00 diopter;

+ If a subject indicates a change that would introduce negative cylinder power,

56

```

### DOC-003 PDF page 121

[Direct source](../../../../joi190092supp2_prod.pdf#page=121)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


                  remove all cylinder power and continue testing for positive cylinder power at an
                  axis 90º away from the previous axis;
             •    If the subject prefers the positive axis coincident with the cylinder axis,
                  increase the power of the trial frame by +1.00 diopter and retest;
             •    Beginning with cylinders of 1.00 diopter or more, for each 0.5 diopter change in
                  cylinder power, adjust the sphere by 0.25 diopter of the opposite sign, this is
                  done to maintain the spherical equivalent.

         Spherical refinement
         End the refraction by performing the spherical refinement step.
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

       5.2.2.B Visual acuity procedure
        Visual acuity measurement is necessary for a secondary outcome in this trial.
        Therefore, we have created a standardized method that aims to minimize any bias from
        either the refractionist or the patient. This has been adapted from the Visual Acuity
        protocols from the Age Related Eye Disease Study (AREDS 1999)32, and the Aravind
        Eye Hospital’s Practical Guide to Refraction33 and is similar to the method we are
        currently using at Aravind Eye Hospital and Proctor/UCSF for the NEI funded Steroids
        for Corneal Ulcers Trial and the Mycotic Ulcer Treatment Trials.

         Visual Acuity Charts
         The following equipment is used: a set of three charts, which are modified Bailey-Lovie
         charts, Charts 1, 2 and R (Precision Vision Chart 2305, 2305a and 2305b,
         respectively). Each chart consists of 14 lines of high-contrast “tumbling E’s”. There is
         a geometric progression of letter size (and, thus, an arithmetic progression of the
         logarithm of minimum angle of resolution) from line to line.

         Chart 1 is for measuring aided visual acuity of the right eye and Chart 2 is to be used for
                                                                                                           57


```

### DOC-003 PDF page 122

[Direct source](../../../../joi190092supp2_prod.pdf#page=122)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


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
                  measurements need to be made only once and no floor marks are needed to
                  ensure the correct distance.
              •   If the box is mounted on the wall but the subject's chair is not permanently affixed,
                  the 4- meter distance of the subject's eye from the chart must be marked clearly
                  and permanently.
                                                                                                           58


```

### DOC-003 PDF page 123

[Direct source](../../../../joi190092supp2_prod.pdf#page=123)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


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
                  to one answer. The examiner CANNOT, at any time, give the patient any
                  indication as to whether a response is correct or incorrect.
             •    If 3 or fewer letters are identified correctly on any row from Row 3 or below,
                  STOP testing on that row.
             •    In the case that the patient reads less than 10 letters at 4 meters, move the
                  patient or the chart so that there is a distance between the two of 1 meter.
             •    Visual acuity will then be retested at this 1 meter distance.
             •    Only the first 6 rows of letters need to be read at 1 meter.
             •    If less than 10 letters are read at 1 meter, then the examiner must proceed to
                  Low Vision Testing, starting with Count Fingers testing. If the patient does not
                  adequately Count Fingers (see below), proceed to Hand Motion. If the patient
                  does not adequately recognize Hand Motion (see below), then proceed to Light
                                                                                                           59


```

### DOC-003 PDF page 124

[Direct source](../../../../joi190092supp2_prod.pdf#page=124)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
Manual of Operation and Procedures


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
                 visual acuity score is equal to the number of letters read correctly at 4 meters plus
                 30.
             • If 3 or fewer letters of the largest line are read correctly at 4 meters, the visual
                 acuity score is equal to the number of letters read correctly at 1 meter.
             • If 3 or fewer letters are read at 1 meter, then low vision testing must be
                                                                                                           60


```

### DOC-003 PDF page 125

[Direct source](../../../../joi190092supp2_prod.pdf#page=125)

```text
 First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial   January 6, 2017 - Version 4.5
 Manual of Operation and Procedures


                   performed. (This result, count fingers, hand motion, light perception, or no light
                   perception, will be used for the analysis by converting into a logMAR score
                   according to Visual Acuity Calculation Table).

          The highest attainable 4-meter visual acuity score is 100.

          The Snellen equivalent, defined as the Snellen ratio corresponding to the most difficult
          line for which the subject read at least 4 of 5 letters correctly, will also be entered by the
          examiner on the 4-meter Visual Acuity Form (Section A.5).
          The data entry staff will enter the number correct on each row at 4 meters, and if
          applicable, 1 meter and low vision testing results (They will not enter which letters the
          examiner circled, i.e., which letters the patient identified correctly.). Coordinating center
          personnel will double check the data entered by the examiner and data entry staff.

        5.2.3.B     Visual acuity training and certification

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
          are required at each site. The visual acuity measurement schedule may be found on
          the Study Forms Completion Schedule.

5.3. Ophthalmic procedures

     5.3.1. Grading Cataracts
     The study ophthalmologist will grade cataracts at every clinical exam based on the Age-
     Related Eye Disease Study (AREDS) clinical lens grading system (Chew et al., 2010).
     Pupils must be dilated maximally and lenses should be examined at the slit lamp for the
     presence and severity of three types of opacity: nuclear, cortical and posterior
     subcapsular. For each type of opacity, the examiner should compare the lens being
     examined with the AREDS 2008 Clinical lens opacity standard photographs, of increasing
     severity. In each series, “1” indicates clinical presence, “2” indicates clinical significance,
     and “3” indicates severe occurrence. Half grades may be given, for example if a nuclear
     opacity was thought to be half way between the first and second standard photographs, a
     decimalized grade of “1.5” could be assigned.
                                                                                                            61


```

### DOC-003 PDF page 126

[Direct source](../../../../joi190092supp2_prod.pdf#page=126)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial        January 6, 2017 - Version 4.5
Manual of Operation and Procedures



    The study ophthalmologists will refer to laminated photos of the scale in real time when
    making the clinical assessment. If no cataract is present, he/she will indicate this on the
    clinical exam form.

    The following categories of severity are present for all types of opacity (nuclear, cortical
    and posterior subcapsular): <1, 1, 1.5, 2, 2.5, >3.




    *Clinical grading adapted from: Chew EY, KIM J, Sperduto RD et al. Evaluation of the Age-Related Eye Disease
    Study Clinical Lens Grading System AREDS Report No. 31. Ophthalmology 2010: 11; 2112-2119.

    5.3.2. Grading inflammation
    Slit lamp examination and dilated funduscopic exam are important parts of our study:
    assessments of anterior chamber cells and vitreous haze will determine the patient’s course
    of treatment. All of our study physicians are fellowship-trained uveitis specialists who have
    participated in prior uveitis studies.

    The study ophthalmologist at each site will be required to perform an eye examination at
    each study visit. This examination should be similar to that performed in the routine care of
    uveitis patients. Several components will be assessed in detail per study protocol. The
    grading schemes to be used for these assessments are adapted from the Standardization of
    Uveitis Nomenclature (SUN) Working Group.2

    Anterior Chamber Cells
    SUN Working Group Grading Scheme for Anterior Chamber Cells
                          Grade                                            Cells in Field*
                              0                                                   <1
                            0.5+                                                  1-5
                             1+                                                  6-15
                             2+                                                 16-25
                             3+                                                 26-50
                             4+                                                  >50
    *Field size is a 1mm by 1mm slit lamp beam. Grading should be done with the highest magnification and
    illumination and conducted in a completely dark room, prior to dilation.

                                                                                                                62


```

### DOC-003 PDF page 127

[Direct source](../../../../joi190092supp2_prod.pdf#page=127)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial           January 6, 2017 - Version 4.5
Manual of Operation and Procedures



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
 *Field size is a 1mm by 0.5mm beam; Grading should be conducted in a completely dark room; These cells are
 graded by slit lamp exam after dilation.

    Vitreous Haze
    Vitreous haze will be assessed using an indirect ophthalmoscope set at mid-power and a
    20D lens. Fundus examination will be done with the last view being the area around the
    optic disc. The examiner should then compare this view to the photograph (Figure 1) and
    determine the level of vitreous haze. The National Eye Institute System for grading
    vitreous haze will be used for all primary and secondary outcome measures. Additionally,
    vitreous haze will be assessed separately on the 9-point grading scale recently published
    by Davis et al., known as the Miami scale. The examiner should compare the vitreous
    haze view with the Miami photograph. An exploratory analysis will correlate
    measurements from the NEI and Miami scales. Clinical measurements of vitreous haze
    will also be compared to objective assessments done by grading of fundus photos by the
    reading center.

    If the physician thinks that the grading of vitreous haze is affected by a significant media
    opacity (i.e. a dense/mature cataract) they should indicate on the Clinical Exam Form that
    they cannot make a reliable judgment of vitreous haze due to the opacity.




                                                                                                                   63


```

### DOC-003 PDF page 128

[Direct source](../../../../joi190092supp2_prod.pdf#page=128)

```text
First-line Antimetabolites as Steroid-sparing Treatment (FAST) Uveitis Trial          January 6, 2017 - Version 4.5
Manual of Operation and Procedures


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
    *Grading should be conducted in a completely dark room; From Nussenblatt et al.Standardization of vitreal
    inflammatory activity in intermediate and posterior uveitis.Ophthalmology1985;92:467-471.




                                                                                                                  64


```

## Explicit current mapping transcription correction

The bounded direct-source confirmation in protocol_065_096_bounded_confirmation.md supplies the authoritative complete p.96 form/visit matrix. In the compressed p.96 summary, the Phase II Laboratory Report baseline entry must be read as blank, rather than scheduled. The source matrix has week 2, months 1–5 and month 6 scheduled, and failure marked (x). This correction concerns the current derivative summary; the supplied source and retained rendering did not change. No new inferential or statistical-design relationship is identified. Full p.96 source evidence and the exact matrix remain in the bounded confirmation artifact.
