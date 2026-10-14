# DOC-004 support mapping: physical PDF pages 1–24

Fresh agent: 01a12bbc-b231-73f0-826a-30815634b6da. Role REPORT by content. Assigned scope only DOC-004 pp. 1–24; all 24 fresh-required units mapped. No prior scientific conclusions were read. Source: joi250019supp3_prod_1749674951.30054.pdf. References below use physical PDF pages.

Engine for native.txt and layout.txt: package-local PyMuPDF 1.26.4 through workflow_1_6_2/scripts/pdf_tools.py, text pp. 1–24; layout uses sorted reading order. page_01.txt through page_24.txt are unchanged page partitions of layout.txt generated with awk, not OCR. Current source figures pp. 11,12,19,22,23,24 rendered by the same helper, PyMuPDF 1.26.4, 200 dpi CPU, and read visually. GPU OCR was authorized by user, but no OCR engine was required for this shard. All derivatives are under preprocessing/results_a_fresh/. Native text does not contain graphic numbers; those numbers are transcribed explicitly below from current rendered source pages. No cached workbook values/formulas, structured files, or Office documents are supplied in this shard.

## Complete page coverage

| Physical page | Unit opened and mapped | Relationships | Status |
|---|---|---|---|
| 1 | Cover and complete supplement contents; eAppendix/eFigures/eTables list; no outcome results | None applicable | COMPLETE |
| 2 | Committees, staff and beginning Alberta clinics; provider/randomization administrative pairs in fresh text appendix | N200 | COMPLETE |
| 3 | Alberta clinic list continued; every provider/randomization pair preserved in appendix | N200 | COMPLETE |
| 4 | Alberta/British Columbia/Saskatchewan clinic lists; all administrative pairs preserved | N200 | COMPLETE |
| 5 | Manitoba/Ontario clinic lists; every administrative pair preserved | N200 | COMPLETE |
| 6 | Administrative outcome definitions: ACS/stroke/HF; all three provincial columns | S200 | COMPLETE |
| 7 | Hip fracture definitions/codes/procedures and event qualifiers, all provincial columns | S200 | COMPLETE |
| 8 | New glaucoma/dementia codes and event qualifiers, all provincial columns | S200 | COMPLETE |
| 9 | Nonvertebral fracture, nursing-home admission, last medical service and data cutoffs, all provincial columns | S200,S201 | COMPLETE |
| 10 | Adjudication committee, blinding/corroboration and disallowed-events explanation | S202 | COMPLETE |
| 11 | Fig.3-1 Death, ACS, HF, stroke: all 15 bars/numerators/denominators and printed percentages | N201–N204 | COMPLETE |
| 12 | Fig.3-1 continued: unplanned hospital/ED, hip fracture, glaucoma, nonvertebral fracture; all 13 bars | N205–N208 | COMPLETE |
| 13 | General adjudication rules, date assignment, first-event rule | S203 | COMPLETE |
| 14 | ACS/HF and stroke rules, 24-hour threshold | S204 | COMPLETE |
| 15 | Stroke continued, unplanned hospital/ED rules, hip fracture rules | S204,S205 | COMPLETE |
| 16 | Hip fracture continued, death, glaucoma, nursing-home, nonvertebral fracture | S205 | COMPLETE |
| 17 | Nonvertebral fracture continued; all diagnostic exclusion/inclusion rules | S205 | COMPLETE |
| 18 | ABPM sampling, time, reading schedule, adequacy thresholds, repeats/replacement and invitation counts | N209,S206 | COMPLETE |
| 19 | Fig.4-1 complete ABPM flow and every decline reason count | N210 | COMPLETE |
| 20 | Lost-contact definitions, primary adjustment covariates, summaries, missingness, Cox models, PH test | S207–S210 | COMPLETE |
| 21 | PH test qualification and every disclosed secondary-outcome change | S210,S211 | COMPLETE |
| 22 | eFigure1 map/practice-location numbers, all listed town/province counts | N211 | COMPLETE |
| 23 | eFigure2 baseline medication counts: ACE-I, ARB, CCB, diuretic; every labeled bar pair | N212–N215 | COMPLETE |
| 24 | eFigure2 continued: beta-blocker, other, combination medications; every labeled bar pair | N216–N218 | COMPLETE |

No page-level scientific gap. Administrative units on pp. 2–5 and 22 have been opened and retained; they are not assumed to be outcome evidence. No inferential effect, confidence interval, P value, subgroup result or sensitivity estimate is printed on pp. 1–24. Relevant statistical methods/definitions and outcome amendments are mapped instead.

## Fig.3-1: adjudication counts and percentages (pp.11–12)

N201–N208. Number-of-events stacked bars: blue Accepted, orange Rejected. Labels are rejected/total potential reports (printed percent rejected where supplied), not trial-arm event rates. Reporting sources overlap; do not sum source-specific totals into overall totals. No treatment-arm split, CI, test or model is printed. The following retains each printed numerator, denominator and percentage; accepted values are derivations total minus rejected, not separately printed labels.

| ID | Page | Outcome | Source category | Printed rejected/total | Printed rejected % | Derived accepted |
|---|---:|---|---|---|---|---:|
| N201 | 11 | Death | Administrative data | 0/165 | Not printed | 165 |
| N201 | 11 | Death | Patient-reported | 0/112 | Not printed | 112 |
| N201 | 11 | Death | Overall | 0/175 | Not printed | 175 |
| N202 | 11 | Acute coronary syndrome | Hospital diagnosis | 1/70 | 1.4 | 69 |
| N202 | 11 | Acute coronary syndrome | ED diagnosis | 21/71 | 29.6 | 50 |
| N202 | 11 | Acute coronary syndrome | Patient-reported | 7/53 | 13.2 | 46 |
| N202 | 11 | Acute coronary syndrome | Overall | 28/115 | 24.3 | 87 |
| N203 | 11 | Heart failure | Hospital diagnosis | 1/41 | 2.4 | 40 |
| N203 | 11 | Heart failure | ED diagnosis | 5/61 | 8.2 | 56 |
| N203 | 11 | Heart failure | Patient-reported | 16/42 | 38.1 | 26 |
| N203 | 11 | Heart failure | Overall | 22/95 | 23.2 | 73 |
| N204 | 11 | Stroke | Hospital diagnosis | 1/38 | 2.6 | 37 |
| N204 | 11 | Stroke | ED diagnosis | 6/42 | 14.3 | 36 |
| N204 | 11 | Stroke | Patient-reported | 6/42 | 14.3 | 36 |
| N204 | 11 | Stroke | Overall | 12/71 | 16.9 | 59 |
| N205 | 12 | All-cause unplanned hospitalizations/ED visit | Hospital diagnosis | 471/735 | 64.1 | 264 |
| N205 | 12 | All-cause unplanned hospitalizations/ED visit | ED diagnosis | 183/1950 | 9.4 | 1767 |
| N205 | 12 | All-cause unplanned hospitalizations/ED visit | Patient-reported | 354/1220 | 29.0 | 866 |
| N205 | 12 | All-cause unplanned hospitalizations/ED visit | Overall | 1008/3048 | 33.1 | 2040 |
| N206 | 12 | Hip fracture | Administrative data | 2/48 | 4.2 | 46 |
| N206 | 12 | Hip fracture | Patient-reported | 0/36 | Not printed | 36 |
| N206 | 12 | Hip fracture | Overall | 2/53 | 3.8 | 51 |
| N207 | 12 | Glaucoma | Administrative data | 67/111 | 60.4 | 44 |
| N207 | 12 | Glaucoma | Patient-reported | 32/101 | 31.7 | 69 |
| N207 | 12 | Glaucoma | Overall | 79/161 | 49.1 | 82 |
| N208 | 12 | Nonvertebral fractures | Administrative data | 10/243 | 4.1 | 233 |
| N208 | 12 | Nonvertebral fractures | Patient-reported | 62/301 | 20.6 | 239 |
| N208 | 12 | Nonvertebral fractures | Overall | 71/389 | 18.3 | 318 |

Matching main-paper keys: adjudicated death; ACS; HF; stroke; first unplanned hospital/ED use; hip fracture; glaucoma; nonvertebral fracture. The pooled overall accepted bars should only be compared after confirming first-event/population definitions. Source-category bars remain overlapping ascertainment reports.

## ABPM methods and flow (pp.18–19)

N209/S206: consecutive volunteers from six Alberta communities (Calgary, Edmonton, Camrose, Sherwood Park, Spruce Grove, Red Deer); 151 bedtime and 151 morning participants. Intended 6-month assessment; actual median 9.6 months (IQR 7.1–29.2 months). Suntech Oscar 2 M250 monitor. Typical measurements every 30 minutes daytime and 45 minutes overnight, participant-defined sleep window most often 11 PM–7 AM. Minimum five successful overnight readings and eight daytime. Research-team inadequate reports 7 bedtime and 5 morning; declined repeat 3/7 bedtime and 2/5 morning, requiring consecutively selected replacement participants. Invited 356 bedtime, 346 morning. This sample defines ABPM results, not all randomized participants; matching key main paper ABPM/eTable9.

N210: Fig.4-1 printed flow, 702 total consecutive invited; 346 morning/356 bedtime; 193/202 did not consent; 153/154 underwent ABPM; 5/7 inadequate; 3/4 repeated and repeat adequate; 2/3 declined repeat; 151/151 analyzed (all pairs morning/bedtime).

| Decline reason | Morning | Bedtime |
|---|---:|---:|
| Location too far/moved/transportation | 32 | 34 |
| Previous negative experience/disrupts daily routine | 15 | 22 |
| Too busy | 17 | 16 |
| Not interested | 11 | 17 |
| BP cuff fitting concerns | 7 | 3 |
| Current health problems | 4 | 6 |
| COVID-19 concerns | 4 | 3 |
| Reason not provided | 103 | 101 |

## Analysis definitions and outcome changes (pp.20–21)

S207: lost-to-follow-up when contact efforts exhausted; initiate alternate contacts at 10 unanswered phone/email attempts; 2 missed interviews in a row (missed = still unreachable five weeks after planned interview); or disconnected/nonfunctional phone. If alternate contacts unreachable within one week, phone clinic; exceptional mailed letter. This governs interview loss, distinguished from administrative ascertainment.

S208: primary adjusted HR covariates explicitly listed: age; sex; Tilburg physical frailty; current smoker; number non-BP medications; overall EQ-5D-5L health score; prior six-month hospitalization; HF; diabetes; CAD; stroke/TIA; CKD; dialysis; BMI >35 kg/m²; BMI <20 kg/m²; sleep apnea; exercise days; province. Outcomes have unique predefined covariate numbers/order in supplied SAP; limited group/outcome sizes use reduced models with predefined importance order. Matching keys: adjusted primary HR, SAP primary/reduced covariate lists.

S209: categorical distributions count/percent; continuous distributions mean/median and SD/IQR as appropriate. Missing at random; categorical covariates replaced by modal observation, continuous by mean; no outcome imputation. Matching key: main-paper/SAP missing-data specification.

S210: series of Cox proportional-hazards models for primary and secondary outcomes, beyond clinical/demographic factors. Allocation-group PH checked with Kolmogorov-type supremum test of sum of martingale residuals, 1000 simulated patterns, all outcomes. Report states no allocation PH violations; covariate violations considered insignificant because not primary interest and adjusted results did not appreciably differ from unadjusted. No test statistic/P value printed here.

S211: changes made while fully blinded to all primary/secondary outcomes, during draft published protocol manuscript/co-investigator review: (1) change from baseline overall health score at 12 months changed to absolute overall health score at 12 months; (2) total cost of care added to previous acute-care cost analysis; (3) nonvertebral fracture added secondary, administratively captured throughout but participant questions added midtrial, less sensitive early; (4) syncope last month, falling last month, new glaucoma, nocturia frequency, new impairment consistent with dementia added secondary safety, collected since trial beginning but not previously prespecified for analysis. These declarations must accompany comparison to original plans. No dates for each alteration, inferential estimates or tests printed here.

## Baseline medication figure counts (pp.23–24)

N212–N218. Every pair below is printed morning/bedtime count; orange morning, blue bedtime. Baseline, drug users; no denominators, percentages, inferential effects, intervals or tests printed. Do not assume classes/drugs are mutually exclusive. Combination products have their own panel. The visual drug spelling/abbreviation is retained. Matching main-paper key: baseline antihypertensive class use, expanded baseline/eTable3.

| ID | Panel/page | Drug | Morning | Bedtime |
|---|---|---|---:|---:|
| N212 | ACE-I/23 | ramipril | 314 | 271 |
| N212 | ACE-I/23 | perindopril | 205 | 207 |
| N212 | ACE-I/23 | lisinopril | 35 | 34 |
| N212 | ACE-I/23 | trandolapril | 27 | 26 |
| N212 | ACE-I/23 | enalapril | 21 | 21 |
| N212 | ACE-I/23 | fosinopril | 15 | 10 |
| N212 | ACE-I/23 | cilazapril | 8 | 3 |
| N212 | ACE-I/23 | quinapril | 6 | 13 |
| N213 | ARB/23 | candesartan | 144 | 171 |
| N213 | ARB/23 | irbesartan | 99 | 89 |
| N213 | ARB/23 | telmisartan | 79 | 97 |
| N213 | ARB/23 | valsartan | 70 | 87 |
| N213 | ARB/23 | losartan | 46 | 60 |
| N213 | ARB/23 | olmesartan | 30 | 32 |
| N213 | ARB/23 | eprosartan | 2 | 0 |
| N213 | ARB/23 | azilsartan | 1 | 0 |
| N214 | CCB/23 | amlodipine | 347 | 336 |
| N214 | CCB/23 | nifedipine XL/XR | 51 | 59 |
| N214 | CCB/23 | diltiazem | 33 | 26 |
| N214 | CCB/23 | diltiazem CD | 17 | 10 |
| N214 | CCB/23 | diltiazem XC | 17 | 17 |
| N214 | CCB/23 | felodipine | 12 | 15 |
| N214 | CCB/23 | nifedipine ER | 4 | 4 |
| N214 | CCB/23 | verapamil | 4 | 6 |
| N214 | CCB/23 | verapamil SR | 4 | 3 |
| N214 | CCB/23 | amlodipine & atorvastatin | 0 | 3 |
| N214 | CCB/23 | nifedipine | 0 | 2 |
| N215 | Diuretic/23 | HCTZ | 297 | 292 |
| N215 | Diuretic/23 | furosemide | 53 | 44 |
| N215 | Diuretic/23 | chlorthalidone | 40 | 30 |
| N215 | Diuretic/23 | indapamide | 36 | 43 |
| N215 | Diuretic/23 | spironolactone | 34 | 34 |
| N215 | Diuretic/23 | HCTZ-triamterene | 21 | 14 |
| N215 | Diuretic/23 | amiloride & HCTZ | 3 | 3 |
| N215 | Diuretic/23 | amiloride | 2 | 3 |
| N215 | Diuretic/23 | ethacrynic acid | 1 | 0 |
| N215 | Diuretic/23 | HCTZ-spironolactone | 0 | 3 |
| N216 | Beta blocker/24 | metoprolol | 111 | 111 |
| N216 | Beta blocker/24 | bisoprolol | 97 | 96 |
| N216 | Beta blocker/24 | atenolol | 29 | 41 |
| N216 | Beta blocker/24 | propranolol | 12 | 16 |
| N216 | Beta blocker/24 | carvedilol | 8 | 10 |
| N216 | Beta blocker/24 | labetalol | 5 | 1 |
| N216 | Beta blocker/24 | sotalol | 5 | 2 |
| N216 | Beta blocker/24 | acebutolol | 3 | 5 |
| N216 | Beta blocker/24 | propranolol LA | 3 | 2 |
| N216 | Beta blocker/24 | nadolol | 3 | 1 |
| N216 | Beta blocker/24 | metoprolol SR | 1 | 0 |
| N216 | Beta blocker/24 | nebivolol | 1 | 3 |
| N216 | Beta blocker/24 | pindolol | 1 | 0 |
| N217 | Other/24 | clonidine | 9 | 10 |
| N217 | Other/24 | hydralazine | 4 | 4 |
| N217 | Other/24 | terazosin | 3 | 7 |
| N217 | Other/24 | doxazosin | 2 | 3 |
| N217 | Other/24 | aliskiren | 1 | 2 |
| N217 | Other/24 | isosorbide mononitrate | 1 | 0 |
| N217 | Other/24 | prazosin | 1 | 2 |
| N218 | Combination/24 | perindopril/indapamide | 68 | 78 |
| N218 | Combination/24 | valsartan HCTZ | 53 | 47 |
| N218 | Combination/24 | telmisartan & HCTZ | 34 | 21 |
| N218 | Combination/24 | irbesartan HCTZ | 32 | 35 |
| N218 | Combination/24 | candesartan & HCTZ | 21 | 31 |
| N218 | Combination/24 | ramipril HCTZ | 20 | 30 |
| N218 | Combination/24 | losartan HCTZ | 18 | 14 |
| N218 | Combination/24 | olmesartan & HCTZ | 14 | 10 |
| N218 | Combination/24 | amlodipine & perindopril | 12 | 8 |
| N218 | Combination/24 | amlodipine & telmisartan | 10 | 14 |
| N218 | Combination/24 | lisinopril HCTZ | 8 | 9 |
| N218 | Combination/24 | valsartan HCT DS | 4 | 3 |
| N218 | Combination/24 | quinapril/HCTZ | 3 | 7 |
| N218 | Combination/24 | cilazapril/HCTZ | 2 | 3 |
| N218 | Combination/24 | enalapril/HCTZ | 1 | 1 |
| N218 | Combination/24 | atenolol & chlorthalidone | 0 | 3 |
| N218 | Combination/24 | pindolol & HCTZ | 0 | 1 |

## Practice-location figure (p.22)

N211 administrative counts: British Columbia 43, Alberta 326, Saskatchewan 22, Manitoba 29, Ontario 16. Table heading Location of Participating Practices. Counts correspond to recruiting practices/providers by locality, not outcome denominators. BC: Chilliwack12, Comox1, Courtenay1, Cranbrook1, Duncan1, Fort St.John1, Langley1, Nanaimo1, New Westminster4, Port Coquitlam12, Powell River1, Richmond3, Smithers3, Vancouver2. AB: Banff5, Beaumont7, Calgary101, Camrose1, Coaldale1, Coronation1, Drumheller1, Edmonton84, Edson1, Hinton2, Innisfail2, Lacombe3, Leduc5, Lethbridge9, Manning2, Medicine Hat1, Okotoks7, Peace River21, Ponoka1, Red Deer4, Rimbey1, Sherwood Park11, Spruce Grove12, St.Albert9, Strathmore8, Sundre5, Sylvan Lake9, Taber1, Three Hills6, Vulcan2, Wetaskiwin1, Whitecourt2. SK: Beechy1, Regina2, Rosetown1, Saskatoon18. MB: Winkler1, Winnipeg28. ON: Brantford1, Collingwood1, Guelph1, Hamilton2, North York3, Ottawa1, Richmond Hill1, Toronto5, Windsor1. Current supplied PDF has visible yellow annotations over parts of BC inset; labels above were legible through current visual inspection. No primary/key secondary outcome information in map.

## Complete fresh native/layout page transcription appendix

The following per-page transcriptions preserve every administrative count, ICD/ATC/service code, threshold, endpoint qualification, source-data cutoff, adjudication rule, method statement and footnote from pages with native text. Source rendering remains authority. Graphic values omitted from native text have already been separately mapped above. Figure pages also retain their native captions below.

### Physical PDF page 01 — fresh layout text

```text
                  Supplemental Online Content



Garrison SR, Bakal JA, Kolber MR, et al. Antihypertensive medication timing and
cardiovascular events and death: the BedMed randomized clinical trial. JAMA. Published
online May 12, 2025. doi:10.1001/jama.2025.4390


eAppendix. Supplemental administrative information and methods
eFigure 1. Location of participating medical clinics
eFigure 2. Medications in use at baseline
eFigure 3. Proportion of participants who withdrew or were lost to follow-up
eFigure 4. Adherence to allocation time at 6-months, by medication class
eTable 1. Study recruitment methods
eTable 2. Proportion of interviews completed online vs over the phone
eTable 3. Expanded baseline characteristics
eTable 4. Baseline characteristics of those completing the trial versus those
withdrawing or lost to follow-up
eTable 5. Baseline characteristics for those who did not complete follow-up and could
not be followed using administrative data, stratified by study allocation.
eTable 6. Medication use at 6-months
eTable 7. Compliance with allocation time over the duration of the trial
eTable 8. Success of once-daily medication changes at 6-months, along with reasons
for failure, by medication class
eTable 9. 24-hour ambulatory blood pressure monitoring results




This supplemental material has been provided by the authors to give readers additional
information about their work.





© 2025 American Medical Association. All rights reserved, including those for text and data mining,
AI training, and similar technologies.

```

### Physical PDF page 02 — fresh layout text

```text
eAppendix. Supplemental administrative information and methods

     SECTION 1: BedMed Committees, Co-investigators, and Staff

Steering Team: Scott Garrison (Overall Principal Investigator), Jeffrey Bakal, Michael Kolber,
Christina Korownyk, Finlay McAlister, Raj Padwal, Michael Hill, G. Michael Allan

Patient-Partner Working Group: Mariann Rich, Jerry Scoular, Grant Geldart, David
Nichiporik, Christine Nichiporik, Darryl Trueman, Helle Tees, Gerry Robinson, Bruce Perry

Event Adjudication Committee: Jessica Kirkwood, Michael Kolber, Christina Korownyk, Lee
Green, Roni Kraut, Scott Garrison

Data and Safety Monitoring Board: Jim Wright (Chair), Tom Perry, Marco Perez, Benji
Heran, Mohamed Ben-Eltriki

Study Statisticians and Programmers: Jeffrey Bakal, Jack (Man Shun) Yeung, Grace (Ting)
Wang, Erik Youngson

Research Coordinators: Farah Campbell, Janis Cole, Nicole Olivier

Research Assistants: Michael Kelmer, Armine Gayayan, Ana Vucenovic, Nathan Archibald,
Dorna Sadeghi, Jeffrey Cheng, Kaylin Bechard, Yvonne Marcoux, Aanchal Saran, Ryan Kichuk,
Ife Odeleye, Geoffrey Charm, Antonia Chua, Cynthia Dimaano

Administrative Assistant: Jessica Kinsella

Local (Provincial) Principal Investigators:
British Columbia: Kim McGrail
Alberta: Scott Garrison
Saskatchewan: Cathy MacLean
Manitoba: Alexander Singer
Ontario: Braden O’Neill

Participating Medical Clinics
(rand = number of resulting randomizations, provider = number of family physicians or nurse
practitioners recruiting at that location)

ALBERTA
Banff: Bear Street Family Physicians (5 providers, 9 rand)
Beaumont: Beaumont Medical (7 providers, 21 rand)
Calgary: Aspen Medical Clinic (1 provider, 16 rand), Associate Clinic (3 provider, 21 rand),
Britannia Medical Clinic (1 provider, 3 rand), Crowfoot Village Family Practice (1 provider, 5 rand),
Cura Family Practice (3 provider, 27 rand), Dr. Cathryn Kuzyk (1 provider, 10 rand), Dr. Margaret
Churcher Professional Corporation (1 provider, 1 rand), East Calgary Health Centre (11 providers,

© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 03 — fresh layout text

```text
23 rand), Family Health Clinic (1 provider, 10 rand), Foothills Primary Care Centre (16 providers,
62 rand), Saluté Family Medicine (5 providers, 5 rand), Sheldon M Chumir Health Centre (25
providers, 118 rand), South Health Campus (9 providers, 36 rand), Southland Sports Medicine (1
provider, 2 rand), Sunridge Family Medicine Teaching Centre (12 providers, 42 rand), Symons
Valley First Care (7 providers, 49 rand), Valley Ridge Family Physicians (2 providers, 14 rand),
Valley View Family Practice (1 provider, 2 rand)
Camrose: Smith Clinic (1 provider, 34 rand)
Coaldale: Campbell Clinic Coaldale (1 provider, 2 rand)
Coronation: Coronation Medical Clinic (1 provider, 3 rand)
Drumheller: Riverside Medical Clinic (1 provider, 5 rand)
Edmonton: Alliant Medical Clinic (1 provider, 9 rand), Bearspaw Medical Clinic (1 provider, 1 rand),
Capilano Medical Centre (1 provider, 7 rand), Ermineskin Medical Clinic (4 providers, 33 rand),
Glenora Medical Clinic (4 providers, 21 rand), Glenwood Medical Clinic (1 provider, 4 rand),
Granville Medical Clinic (1 provider, 6 rand), Grey Nuns Family Medicine Centre (7 providers, 34
rand), Heritage Medical Clinic (3 providers, 34 rand), Heritage Village Medicentre (4 providers, 3
rand), Hope Medical Clinic (2 providers, 7 rand), Horizon Family Practice (1 provider, 7 rand), Justik
Medical Clinic (2 providers, 16 rand), Kaye Edmonton Clinic (11 providers, 85 rand), Links Clinic (1
provider, 5 rand), Lynnwood Centre (1 provider, 23 rand), MacEwan University Health Centre (5
providers, 6 rand), Magrath Medical Clinic (1 provider, 33 rand), Millcreek Medical Centre (1
provider, 0 rand), Misericordia Family Medicine Clinic (4 providers, 30 rand), New Foundation
Medical Centre (1 provider, 10 rand), Northeast Community Health Centre (7 providers, 16 rand),
Nova Medical Clinic (2 providers, 14 rand), Ottewell Medical Clinic (6 providers, 41 rand), Sage
Seniors Association (2 providers, 7 rand), Shifa Medical Clinic (5 providers, 6 rand), Southwell
Medical Centre (1 provider, 3 rand), Summers Medical Clinic (1 provider, 0 rand), The Allin Clinic (3
providers, 44 rand), Town Centre Family Clinic (1 provider, 9 rand)
Edson: Edson Medical Centre (1 provider, 7 rand)
Hinton: Hillcrest Medical Associates (2 providers, 11 rand)
Innisfail: Innisfail Medical Clinic (2 providers, 13 rand)
Lacombe: Mainstreet Medical Services (3 providers, 28 rand)
Leduc: Griffiths Medical Clinic (3 providers, 21 rand), LA Medical Clinic (2 providers, 13 rand)
Lethbridge: Campbell Clinic South (3 providers, 44 rand), Haig Clinic (2 providers, 29 rand),
Legacy Medical Centre (4 providers, 23 rand)
Manning: Manning Medical Clinic (2 providers, 11 rand)
Medicine Hat: Horsman Catherine Dr Professional Corporation (1 provider, 21 rand)
Okotoks: Foothills Family Practice (7 providers, 60 rand)
Peace River: Aspen Mile Medical Inc (3 providers, 1 rand), Peace River Medical Clinic (21
providers, 52 rand),
Ponoka: Battle River Medical Clinic (1 provider, 4 rand)
Red Deer: Hevloc Family Medical Clinic (1 provider, 0 rand), Waskasoo Medical Clinic (3
providers, 31 rand)
Rimbey: Rimbey Medical Clinic (1 provider, 15 rand)
Sherwood Park: Synergy Medical Clinic (11 providers, 159 rand)
Spruce Grove: Westgrove Clinic (12 providers, 57 rand)


© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 04 — fresh layout text

```text
St. Albert: Horizon Health Medical Clinic (2 providers, 11 rand), St. Albert Medical Clinic (7
providers, 28 rand)
Strathmore: Valley Medical Clinic (8 providers, 40 rand)
Sundre: Moose and Squirrel Medical Clinic (5 providers, 14 rand)
Sylvan Lake: Sylvan Family Health Centre (9 providers, 51 rand)
Taber: Coulee Medical Clinic (1 provider, 1 rand)
Three Hills: Kneehill Medical Clinic (6 providers, 31 rand)
Vulcan: Vulcan Medical Clinic (2 providers, 18 rand)
Wetaskiwin: Wetaskiwin Family Medical Practice (1 provider, 1 rand)
Whitecourt: Life Medical Clinic (2 providers, 13 rand)


BRITISH COLUMBIA

Chilliwack: Crossroads Family Practice (5 provider, 33 rand), Gaetz Family Practice (1 provider, 7
rand), The Young Clinic (6 providers, 62 rand)
Comox: Comox Medical Clinic (1 provider, 12 rand)
Courtenay: Fifth Street Family Practice (1 provider, 8 rand)
Cranbrook: Fisher Peak Family Practice (1 provider, 4 rand)
Fort St. John: Fort St. John Medical Clinic (1 provider, 5 rand)
Langley: Stephen M. Shore Family Practice Inc (1 provider, 10 rand)
Nanaimo: Medical Arts Centre (1 provider, 7 rand)
New Westminster: Care4You (1 provider, 10 rand), New Westminster Family Practice (3 providers,
30 rand)
Port Coquitlam: Wilson Centre Family Practice (12 providers, 95 rand)
Powell River: Harvie Medical Clinic (1 provider, 5 rand)
Richmond: Dr. Cheryl Nagle (1 provider, 12 rand), Dr. Leslie Cohen (1 provider, 17 rand), Well
Health Oval A Inc Medical Clinic (1 provider, 7 rand)
Smithers: Coho Clinic (3 providers, 4 rand)
Vancouver: Forward Care Medical Clinic (2 providers, 10 rand)


SASKATCHEWAN

Beechy: Beechy Primary Care Clinic (1 provider, 2 rand)
Kyle: Kyle Primary Care Clinic (1 provider, 3 rand)
Lucky Lake: Lucky Lake Primary Care Clinic (1 provider, 5 rand)
Regina: 5th Avenue Medical (1 provider, 1 rand), Northgate Medical Centre (1 provider, 0 rand)
Rosetown: Rosetown & District Primary Care Centre (1 provider, 4 rand)
Saskatoon: West Winds Primary Health Centre (17 providers, 34 rand), Willowgrove Medical Group
(1 provider, 7 rand)



© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 05 — fresh layout text

```text
MANITOBA

Winkler: CW Wiebe Medical Centre (1 provider, 5 rand)
Winnipeg: Access Winnipeg West (9 providers, 43 rand), Atlantic Medical Centre (1 provider, 1
rand), Concordia Health Associates (1 provider, 14 rand), Family Medical Centre (6 providers, 47
rand), Kildonan Medical Centre (7 providers, 24 rand), Meadowood Medical Centre (3 providers, 69
rand), Memorial Medical Clinic Inc (1 provider, 4 rand)

ONTARIO

Brantford: Avenue Medical Centre (1 provider, 0 rand)
Collingwood: Collingwood Medical Centre (1 provider, 10 rand)
Guelph: Dawson Road Family Medical Clinic (1 provider, 10 rand)
Hamilton: Dr. C Prangley Medicine Prof Corp (1 provider, 8 rand), Robert Kerr (1 provider, 4 rand)
North York: Bathurst Family Physicians (3 providers, 5 rand)
Ottawa: Advanced Access Medical Clinics (1 provider, 6 rand)
Richmond Hill: Wise Health Medical Center (1 provider, 2 rand)
Toronto: Duncan Family Docs (2 providers, 5 rand), Platinum Medical FHO (1 provider, 3 rand),
Prince Edward Medical (1 provider, 2 rand), Scarborough Health Network (1 provider, 2 rand)
Windsor: DeMarco and Associates (1 provider, 8 rand)





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 06 — fresh layout text

```text
 SECTION 2: Administrative Health Data (ICD9/10) Outcome Definitions

Overview: The following describes the definitions used to screen for the occurrence of BedMed
outcomes in administrative health data in the 3 provinces (British Columbia, Alberta, Manitoba)
from which patient level data was available. Clinically, it is notable that the definitions for
glaucoma and dementia differ somewhat in that Manitoba (and not British Columbia / Alberta)
included dispensations of diagnosis defining medications in the outcome definition. For
glaucoma, this difference is likely immaterial as we only used administrative health claims
indications of glaucoma as a flag to seek information from the patient, and the primary care
provider, as to whether the patient had this diagnosis. For dementia, the difference is more
meaningful as (to avoid potentially upsetting participants) we accepted administrative claims
diagnoses of dementia without seeking corroboration from patients or primary care providers.
Hence a new diagnosis of dementia was more sensitively picked up in Manitoba, than in other
participating provinces. Manitoba also used ICD9 codes to detect fractures as many fractures
were believed to be managed in the community, or as outpatients.

ICD9/10 Codes used to detect outcomes in administrative health data
 Events           Definitions Used for       Definitions Used for       Definitions Used for
                  Alberta Data              British Columbia Data    Manitoba Data
 Acute          ICD10: I20%, I21%,      ICD10: I20%, I21%,      ICD10: I20%, I21%,
 Coronary       I22%, I24%              I22%, I24%              I22%, I24%
 Syndrome
 (ACS)           Note: ACS/MI            Note: ACS/MI            Note: ACS/MI
 Hospitalization    Hospitalization/ED visit:    Hospitalization/ED visit:    Hospitalization/ED visit:
 or ED visit        qualified by primary         qualified by primary         qualified by primary
                    diagnosis                   diagnosis                   diagnosis

 Stroke         ICD10: H34.1%,         ICD10: H34.1%,         ICD10: H34.1%,
 Hospitalization   I60%, I61%, I63%, I64%   I60%, I61%, I63%, I64%   I60%, I61%, I63%, I64%
 or ED visit
                  Note: Stroke              Note: Stroke              Note: Stroke
                   Hospitalization/ED visit:    Hospitalization/ED visit:    Hospitalization/ED visit:
                     qualified by primary         qualified by primary         qualified by primary
                    diagnosis                   diagnosis                   diagnosis

 Heart Failure    ICD10: I50%           ICD10: I50%           ICD10: I50%
 (HF)            Note: HF                 Note: HF                 Note: HF
 Hospitalization    Hospitalization/ED visit:    Hospitalization/ED visit:    Hospitalization/ED visit:
 or ED visit        qualified by primary         qualified by primary         qualified by primary
                    diagnosis                   diagnosis                   diagnosis





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 07 — fresh layout text

```text
 Events           Definitions Used for       Definitions Used for       Definitions Used for
                  Alberta Data              British Columbia Data    Manitoba Data
 Hip Fracture    ICD10: S72.0%, S72.1%,  ICD10: S72.0%, S72.1%,  ICD10: S72.0%, S72.1%,
                S72.2%                S72.2%                S72.2%
                                                           ICD9: 820%
                                                                         Physician Billing Codes:
                                                                                          • 0865 fractures, lower
                                                                             extremity, femur, neck,
                                                                          closed reduction, cast or
                                                                                  traction
                                                                                          • 0868 fractures, lower
                                                                             extremity, femur, neck,
                                                                 open reduction with
                                                                                  internal fixation
                                                                                          • 0870 fractures, lower
                                                                             extremity, femur, neck,
                                                                                prosthetic replacement
                                                                                          • 0872 fractures, lower
                                                                             extremity,
                                                                                  intertrochanteric, closed
                                                                           reduction
                                                                                          • 0874 fractures, lower
                                                                             extremity,
                                                                                  intertrochanteric, open
                                                                           reduction
                                                             The following must have
                                                    Dx code 820 on same
                                                                            claim:
                                                                                          • 1149 joints, arthroplasty,
                                                                                  hip, femoral head
                                                                       replacement type
                                                                                          • 1150 joints, arthroplasty,
                                                                          hip (cup or total hip
                                                                       replacement prosthesis)
                                                                                          • 1154 joints, arthroplasty,
                                                                                  hip, femoral head, where
                                                                         previous prosthesis, etc
                                                                              require removal
                                                                                          • 1415 total hip
                                                                               arthroplasty
                                                                                          • 1423 bipolar hip
                                                                               arthroplasty

                Event qualified by: 1 in-   Event qualified by: 1 in-   Event qualified by: 1 in-
                hosp/ED Dx (ANY Dx,    hosp/ED Dx (ANY Dx,    hosp/ED Dx (ANY Dx,
                   not just primary) or 1       not just primary)           not just primary) or
                  procedure service code                               medical claim for hip
                                                                                 fracture repair



© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 08 — fresh layout text

```text
 Events           Definitions Used for       Definitions Used for       Definitions Used for
                  Alberta Data              British Columbia Data    Manitoba Data
 New Glaucoma  ICD10: H40.1%,         ICD10: H40.1%,         ICD10: H40.1%,
 (No history)     H40.6%, H40.8%,        H40.6%, H40.8%,        H40.6%, H40.8%,
               H40.9%               H40.9%               H40.9%
               ICD9: 365.1%, 365.3%,   ICD9: 365.1%, 365.3%,   ICD9: 365.1%, 365.3%,
                365.9%                 365.9%                 365.9% (truncated to 3
                                                                                     digits when necessary if
                                                                                  5-digit code is missing on
                                                                          claim)

                                                             Glaucoma Surgery Tariff:
                                                               5547 IRIS AND
                                                      CILIARY BODY,
                                                  SURGICAL
                                              TRABECULECTOMY
                                             OR SIM FILTER PROC
                                                 FOR GLAUCOMA

                                               ATC codes for Drugs to
                                                                           Treat Glaucoma: S01E
                                                                             (includes all subclasses)

                Event qualified by: 1     Event qualified by: 1     Event qualified by: 1
                   claim or 1 in-              claim or 1 in-hosp/ED Dx   claim or 1 in-hosp/ED Dx
               hosp/NACRS Dx (ANY   (ANY Dx, not just       (ANY Dx, not just
                 Dx, not just primary)       primary)                   primary) or medical claim
                                                    Dx or billing code for
                                                                         surgery or 1+Rx for
                                                                      antiglaucoma preparations
                                                                 and miotics

 New Dementia   ICD10: F00%, F01%,     ICD10: F00%, F01%,     ICD10: F00%, F01%,
 (No history)     F03%, G30%            F03%, G30%            F03%, G30%
               ICD9: 290%, 331%       ICD9: 290%, 331%       ICD9: 290%, 331%
                                               ATC codes for Drugs to
                                                                           Treat Dementia:
                                                   N06D (includes all
                                                                             subclasses)
                Event qualified by: 1     Event qualified by: 1     Event qualified by: 1
                   claim or 1 in-hosp/ED Dx   claim or 1 in-hosp/ED Dx   claim or 1 in-hosp/ED Dx
             (ANY Dx, not just       (ANY Dx, not just       (ANY Dx, not just
                   primary)                   primary)                   primary) or medical claim
                                                    Dx or 1+Rx for anti-
                                                                     dementia drugs





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 09 — fresh layout text

```text
 Events           Definitions Used for       Definitions Used for       Definitions Used for
                  Alberta Data              British Columbia Data    Manitoba Data
 Non-Vertebral   ICD10:                ICD10:                ICD10:
 Fracture       S02%               S02%               S02%
                S22.2% - S22.9%         S22.2% - S22.9%         S22.2% - S22.9%
                S32.1% - S32.6%         S32.1% - S32.6%         S32.1% - S32.6%
                S42%, S52%, S62%       S42%, S52%, S62%      S42%, S52%, S62%
                 S72.0%, S72.1%, S72.2%  S72.0%, S72.1%, S72.2%  S72.0%, S72.1%, S72.2%
                S72.3% - S72.9%         S72.3% - S72.9%         S72.3% - S72.9%
                S82%, S92%, T02%,      S82%, S92%, T02%,      S82%, S92%, T02%,
               T10%, T12%            T10%, T12%            T10%, T12%
               T14.2%                T14.2%                T14.2%

               ICD9: N/A             ICD9: N/A             ICD9: 800-804, 806.6,
                                                                           806.7, 807-807.4, 808,
                                                                        810-819.1, 820-829.1
                                                                              (truncated to 3 digits
                                                          when necessary if 5-digit
                                                                   code is missing on claim)

                Event qualified by:       Event qualified by: 1 in-   Event qualified by: 1 in-
                1 in-hosp/ED Dx (ANY    hosp/ED Dx (ANY Dx,    hosp/ED Dx (ANY Dx,
                 Dx, not just primary)       not just primary)           not just primary) or
                                                                      medical claim Dx

                                                                 Note that hip fractures are
                                                                       a subset of non-vertebral
                                                                                    fractures, and the codes
                                                                             overlap.

 New Nursing    Claims Service Location   Billing Codes: 00114,     Admission to Long-term
 Home         Code = ‘NH’              13334, 00115               care using MB LTC
 Admission                          And Service Location       utilization data:
 (No history)                            Code=’C’ (Residential     http://mchp-
                                                care / assisted living       appserv.cpe.umanitoba.
                                                residence)                 ca/dataDescriptions.php
                                                                  ?ds=LTCUtilization
 Last Medical    The last date of contact    The last date of contact    The last date of contact
 Service Date     using PIN, Claims, DAD,   using PharmaNet, MSP,    using hospitalizations,
              NACRS/ED, and LAB    DAD, ED, and Chronic     medical claims, DPIN
                    data                      Disease Registry data       prescription
                                                                              dispensations, EDIS
                                                                 emergency dept visits,
                                                                        long-term care admission,
                                                                 and lab test data.
                  Note: Data coverage up to  Note: Data coverage up to  Note: Data coverage up to
              Nov 30, 2023;           Dec 31, 2023; except for   March 31, 2023
                   except for NACRS/ED,   DAD up to Sep 30, 2023;
           DAD up to Oct 31, 2023.   and Chronic Disease
                                               Registry to Mar 31, 2023.

© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 10 — fresh layout text

```text
                SECTION 3: Outcome Adjudication

Overview: The Event Adjudication Committee met periodically over the course of the trial to
review information gathered on participants and determine whether potential outcome events
should be accepted or rejected. For each meeting, the committee had three voting members
present, each a practicing family physician (comprised of the trial principal investigator and two
of five additional clinicians, depending on availability). A research assistant controlled the
presentation of data – which included both self-reported events, and administrative health data.
All committee members were fully blinded to allocation. In general, if patient self-report and
administrative health data appeared to corroborate each other, events were accepted without
further investigation. However, if events appeared questionable, or were present in only one of
these sources (e.g. an administrative health data diagnosis of myocardial infarction with no
corresponding participant report), then the participant’s family physician was contacted (by fax
or phone) for more information, and for their opinion on whether the event of interest actually
occurred. This process was followed for hospitalization/ED visit for ACS, stroke, or HF, as well
as for hip fracture, non-vertebral fracture, and new glaucoma diagnosis. We did not seek
confirmation from primary care providers for 1) death or continuing care admission (believing
both of these to be accurately reported by both family and administrative health data), 2) new
diagnosis of dementia (believing this to be a sensitive subject from the participant’s perspective
and not wanting our enquiry to cause them distress), and 3) all-cause unplanned hospitalization
(given the number of hospitalizations/ED visits was high for the trial as a whole and we felt this
could overwhelm the primary care providers). Adjudication rules were evolved as cases were
encountered and the resulting rules used to resolve discrepancies is reported below.

Proportion of Potential Outcomes Disallowed: Overall, a diagnosis provided as the reason for
hospitalization within administrative health data was highly likely to indicate an accepted event.
This was less true for emergency department diagnosis of ACS or stroke (which were often
diagnoses given early on in the clinical presentation before all investigations were completed),
and for participant reported heart failure or stroke (which was often contradicted by primary care
providers examining their records of the events). However, the largest category of disallowed
events was new diagnosis of glaucoma – given ophthalmologists and optometrists appear prone
to provide a claims diagnosis of glaucoma at the stage of elevated intra-ocular pressure, prior to
any loss of vision. In Figure S3-1 below we show the proportion of each outcome that was
rejected by the adjudication committee.





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 11 — fresh layout text

```text
Fig. 3-1
    Description: Figure shows the number of reported events accepted and rejected during the adjudication process. Sources of
    reporting included 1) patient reported (Pt-reported), 2) emergency department diagnosis (ED dx), and 3) most responsible hospital
    diagnosis (Hospital dx). Methods of reporting are not mutually exclusive (i.e. a single event might be reported by the patient, as
    well as have an emergency department diagnosis and a most responsible hospital diagnosis).





© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.

```

### Physical PDF page 12 — fresh layout text

```text
Fig. 3-1 Cont.





© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.

```

### Physical PDF page 13 — fresh layout text

```text
   Adjudication Rules Evolved and Used by the Committee

  GENERAL RULES
     -  Each outcome will be individually adjudicated and the committee will be blinded to
        allocation at all times. All available administrative health data and all available
        participant reporting of the same outcomes will be simultaneously presented to the
       adjudication committee for deliberation.
     -  When the administrative health data and participant self-reported data do not corroborate
       each other, adjudication will be deferred and the participant’s family physician will be
       contacted and requested to provide details from their medical records as to whether or not
       the event in question occurred.
     -  When the family physician is consulted and provides additional data, their response, if
        definitive, will generally be accepted over all else.
     -  When additional information from the family physician cannot be collected, and the
        participant reported that the event happened out of province, where administrative data is
       not available, the event (if credibly described) will generally be accepted unless stated
       otherwise.
     -   If family physicians do not respond to two fax requests for information and one phone
         call, their supplementary information will be considered not available.
     -  Each hospitalization will only be attributed to one type of outcome event (e.g. MI/ACS
    OR HF, but not both).
     -   Dates from administrative data will be accepted over self-reported dates, when both are
        available.
     -   If emergency room and hospitalization dates for the same event type differ substantially,
       the participant, and then the family physician (if needed) will be contacted to clarify the
        correct date, and if these are the same event.
     -  When administrative data for an ED visit, and a hospitalization, appear to indicate the
      same event, the earlier of the two dates (i.e. the ED visit) will be used.
     -   If participants do not remember the specific date of an event, but instead report a month,
       the 15th of that month will be assigned. If they instead report it is “early”, or “late” in a
        typical month then the 7th (early) or 23rd (late) of that month will be assigned as the date
       of the event.
     -  One participant was known to have died (reported by family) but the date was unknown.
       In this case the date of death was assigned to be halfway between the last successful
       follow-up and the next planned follow-up.
     -  Only the first occurrence of an accepted adjudicated event will be counted.





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 14 — fresh layout text

```text
  DIAGNOSIS SPECIFIC RULES

Acute Coronary Syndrome (ACS) and Heart Failure (HF)
     -  When a participant has both an ACS diagnosis and a heart failure (HF) diagnosis during
       the same hospital admission, only the ACS event will be counted.
     -  When a participant arrives in the ED or hospital with a most responsible diagnosis of
       angina, whether or not it was diagnosed as unstable angina, it will be considered a
        potential acute coronary syndrome event that requires adjudication.
     -  When an ED visit diagnosis was coded as HF, it will be considered a HF event even if the
        patient or family physician describe other physiologic contributors such as anemia or
       arrythmia. The exception to this is a simultaneous ACS diagnosis (in which only ACS
        will be recorded) or an ultimate alternative diagnosis that could explain the presentation
      which is not cardiac (e.g. a final diagnosis that the shortness of breath bringing the patient
        to hospital was caused by a COPD exacerbation, and not HF).
     -  When participants or family physicians are not available to corroborate hospitalizations
      where the most responsible diagnosis in administrative data is ACS or HF, it will be
       accepted.
     -  When participants or family physicians are not available to corroborate emergency
       department visits where the most responsible diagnosis is ACS or HF, and there is no
       corresponding hospitalization, it will be rejected, as many of these are early diagnoses
      made prior to all investigations being completed.
     -  When participants or family physicians are not available to elaborate on hospitalizations
       without a corresponding ED visit and the diagnosis is coronary artery bypass grafting, it
        will not be accepted, as the procedure was potentially treating stable angina.
     -  When participants or family physicians are not available to elaborate on hospitalizations
       with a corresponding ED visit and the diagnosis is coronary artery bypass grafting, it will
      be considered an acute coronary syndrome event given the presentation was to the ED.
     -  When participants dispute an administrative data diagnosis of ACS or HF, and further
       validation from a family physician is not available, the event will be rejected if it is an
     ED visit without a corresponding hospitalization. If instead the administrative data
       diagnosis is a hospitalization with a most responsible diagnosis of ACS or HF, then
       acceptance will be on a case-by-case basis depending on the other information provided
      by the participant.
     -  A diagnosis of MI which is described as being “Type II” in the discharge summary (i.e.
      demand outstripping supply, rather than an acute arterial obstruction) will be rejected as
        likely indicating a different clinical entity.

Stroke
     -   Stroke excludes TIA and requires persistence of neurological symptoms beyond 24 hours,
       or brain imaging evidence of cerebral infarction or hemorrhage.
     -  CRAO (Central and branch retinal artery occlusion) is considered a stroke event.

© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 15 — fresh layout text

```text
     -  When participants or family physicians are not available to corroborate hospitalizations
      where the most responsible diagnosis is stroke, it will be accepted.
     -  When participants or family physicians are not available to corroborate emergency
       department visits where the most responsible diagnosis is stroke, and there is no
       corresponding hospitalization, it will be rejected, as many of these are early diagnoses
      made prior to all investigations being completed.
     -  When participants dispute an admin data diagnosis of stroke, and further validation from
       a family physician is not available, the event will be rejected if it is an ED visit without a
       corresponding hospitalization. If instead the admin diagnosis is a hospitalization with a
      most responsible diagnosis of stroke, then acceptance will be on a case-by-case basis
      depending on the other information provided by the participant.

Unplanned All-cause Hospital and ED Visits
     -  Because hospitalizations/ED visits are so numerous, we will not attempt to confirm them
       with family physicians.
     -  To qualify as “unplanned” we require a diagnosis where a symptom is likely to have led
       the patient to present themselves to the hospital acutely.
     -  Where unclear if the event was unplanned, we will err on the side of excluding the event.
     -  We will disqualify admissions for surgery that are typically elective (e.g. hip or knee
       replacement for osteoarthritis, cancer surgery) and any ED procedures that are considered
        elective (e.g. a booked blood transfusion or chemotherapy or “follow-up care”).
     -  However, if participants present to the emergency department with complications from an
        elective surgery after discharge, that will be counted as an acute event (eg. Prostate
       biopsy bleed, bleeding post polypectomy). We will not accept unplanned overnight
        hospital stays when an elective day surgery was planned (i.e. when the patient did not
         initially leave the hospital and subsequently present to emergency).
     -  When cancer is listed as an ED visit diagnosis, it will be accepted. When cancer is listed
       as the reason for hospitalization but there is no corresponding ED visit, it will be rejected.
     -   If participants presented to the emergency room but left without being seen, that event
        will be rejected.
     -  We excluded one patient presenting to the ED for “medication refill”, and one for the
         start of “palliative care”.
     -   If participants describe attending an “urgent care centre” that is not attached to a hospital,
           it will not be counted as an emergency department, and the event will be excluded.

Hip Fractures
     -  Any hip fracture, whether or not surgery was involved, will be counted as a fracture
       event.
     -  Hip fracture includes fracture of the acetabulum.



© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 16 — fresh layout text

```text
     -   If neither primary care provider information, nor participant interview, are available to
       corroborate an administrative health indication of hospitalization for hip fracture it will
          still be accepted.

Death
     -   If the administrative health data, dialog with friends/family, published obituaries, or
       primary care providers indicate a death, this data will be accepted unless there is
        participant follow up data to contradict it.


New Diagnosis of Glaucoma
     -    It became clear early on that there are many outpatient administrative health diagnoses of
      glaucoma provided to patients who only have elevated intraocular pressure. The same is
        true for prescriptions of glaucoma eyedrops, which are often prescribed prior to any of
       the visual loss that would make the diagnosis of glaucoma clear. As a result, an
       administrative data diagnosis of glaucoma, or a prescription for glaucoma eye drops, on
         its own, is insufficient to indicate a new diagnosis of glaucoma.
     -   If family physicians cannot corroborate or refute an administrative data diagnosis of
      glaucoma using ophthalmology or optometry consult letters, we require participants to
      have been told by their ophthalmologist or optometrist that they have glaucoma in order
        to accept the diagnosis.
     -   If participants were told they have glaucoma by an ophthalmologist or optometrist and
       there are no family physician records to review, the diagnosis will be accepted. If the
       family physician did have an ophthalmology or optometry report to review and glaucoma
         is not mentioned, the diagnosis will be rejected.
     -  “Glaucoma suspect” in an ophthalmology or optometry report will be accepted as a
      glaucoma diagnosis.

Nursing Home admission
     -  Both administrative health data and participant/family-reports indicating nursing home
       admission will be accepted. Corroboration from family physicians is not required.
     -   Participants who began the trial in a low level of care assisted living facility where they
      had control of their own medication administration time, who subsequently move to a
       higher level of care where medications are administered by nurses or care aides, will be
       accepted as being admitted to a nursing home.

Non-vertebral fractures
     -   Includes any fracture, other than vertebral (back or neck), that is presumed to stem from
       trauma.
     -  We will include avulsion fractures as being traumatic, and we will exclude stress
        fractures.

© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 17 — fresh layout text

```text
     -   Fractures that are attributed to osteomyelitis, or malignancy, will be excluded.
     -   Participants need to receive their fracture diagnosis from a health care practitioner (i.e.
        self-diagnosis will not be accepted).
     -   Includes sacral / pelvic fractures
     -   If information describing a fracture is ultimately only available from one source (i.e.
        patient report or administrative health data) it will generally be accepted.





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 18 — fresh layout text

```text
         SECTION 4: Ambulatory Blood Pressure Monitoring

      Although we did not measure BP in all participants, a consecutive sample of 151
bedtime, and 151 morning group volunteers residing in one of six Alberta communities (Calgary,
Edmonton, Camrose, Sherwood Park, Spruce Grove, and Red Deer) underwent 24-hour
ambulatory BP monitoring (ABPM) carried out by a local cardiology diagnostics provider
(Advanced Respiratory Care Network - www.arcnetwork.ca/cardiology-diagnostics). The
intention was to carry this assessment out 6-months post-randomization, however a variety of
logistic hurdles, including the start of the COVID-19 pandemic, substantially delayed these
assessments for many individuals – instead taking place a median 9.6 months (IQR 7.1 to 29.2
months) into the trial.
    A Suntech Oscar 2 M250 ambulatory BP monitor was employed in all cases, with
settings per the local provider’s usual routine. Although the frequency of BP readings varied
somewhat by location, this typically entailed taking BP readings every 30 minutes during the day
and every 45 minutes overnight, with the anticipated sleep time window pre-defined by the
participant (most often 11:00 PM to 7:00 AM). When ABPM output was grossly inadequate, the
cardiology diagnostics provider performing the service asked participants to repeat those
assessments per their usual routine, without interacting with the research team. ABPM results
forwarded to the research team, who required a minimum of 5 successful overnight readings and
8 successful daytime readings, were additionally considered inadequate for interpretation for
seven bedtime and five morning participants, each of whom was asked to repeat the assessment.
Of these, 3/7 bedtime and 2/5 morning participants declined a repeat evaluation, which required
the same number of additional participants (consecutively selected) to be invited to undergo 24-
hour monitoring to replace them. Overall, in order to obtain 151 consecutive participants from
each arm of the trial, we needed to invite 356 bedtime group participants and 346 morning group
participants (Figure 4-1 below).





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 19 — fresh layout text

```text
Fig. 4-1 Flow diagram for 24-hour ambulatory blood pressure monitoring





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 20 — fresh layout text

```text
            SECTION 5: Definitions, Statistical Analyses,
              and Changes to Secondary Outcomes

Lost to follow-up: Participants were considered lost to follow-up when attempts to re-establish
contact were exhausted. This included, but was not limited to, initially reaching out to all
provided alternate contacts, and then contacting their primary care provider's clinic.

Three situations initiated the process of reaching out to alternate contacts:
    1. The study team attempted to contact the participant by phone or email 10 times without a
        reply.
    2. The participant missed 2 interviews in a row (“missed” being defined as having still been
       unreachable 5 weeks after the scheduled interview date).
    3. The study team phoned the participant, but the phone line was disconnected or non-
        functional.

If alternate contacts were not reached within a week, the participant’s primary care clinic was
contacted by phone to inquire about the participant’s status and contact information. On rare
occasions when the primary care office could not be contacted (i.e. the provider had retired, the
clinic had closed, or the participant had changed primary care providers without notifying us) the
study team mailed a letter to the participant's current address in an effort to re-establish contact.


Analytic Covariates: Analytic covariates were predefined and unique to each outcome. The
number of covariates used, and the order in which they were selected, was provided in the
published statistical analysis plan for every outcome examined. For the primary analysis,
baseline characteristics used as covariates to produce the adjusted hazard ratio included: Age,
sex, physical frailty score (Tilburg), current smoker, number of non-BP medications, Overall
Health Score (EQ-5D-5L), prior 6 months hospitalization, heart failure, diabetes, coronary artery
disease, stroke or TIA, chronic kidney disease, dialysis, BMI >35kg/m2, BMI <20kg/m2, sleep
apnea, number of exercise days, and province of residence.


Appropriateness of the statistical analyses used: Categorical variables were summarized by
count and percent, while distributions of recorded variables were described by appropriate
measures of center (mean, median) and spread (SD, IQR). Methods of analyses to compare
between groups were applied according to a published trial protocol and analysis plan.

Data were considered missing at random. Covariate data were replaced by the modal observation
for categorical variables and by the mean for continuous ones. No outcome data were imputed.

A series of Cox Proportional hazards models were used to assess the primary and secondary
outcomes over and above the effects of clinical and demographic factors. Where group sizes /
number of outcomes were limited, reduced models were used to avoid overfitting. Variables
were included in a predefined order of presumed importance. We confirmed no violations of the
proportional hazards assumption in the allocation group using a Kolmogorov-type supremum test
on the sum of martingale residuals on 1000 simulated patterns for all outcomes. Any evidence of

© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 21 — fresh layout text

```text
proportional hazard assumption violation among covariates was considered insignificant because
they are not of primary interest, and adjustment models did not appreciably change the results
compared to unadjusted analysis.

Changes to secondary outcomes: The following changes were made to secondary outcomes
while fully blinded to all primary and secondary outcomes. They came about at the time the draft
manuscript for the published protocol was being written and co-investigators were reviewing and
providing feedback on the current version of the protocol.
1. Change from baseline in self-reported Overall Health Score at 12-months was altered to
   Overall Health Score at 12-months. This alteration was made when it was newly
   recognized that comparing absolute change (or percentage change) from baseline between
   groups often provides less power to detect a difference than comparing on-treatment scores.
   (Vickers AJ. The use of percentage change from baseline as an outcome in a controlled trial
    is statistically inefficient: a simulation study. BMC Medical Research Methodology
    2001;1:6).
2.  Total cost of care was added as an outcome to strengthen the cost analysis –whereas
    previously only acute care costs were to be analyzed.
3.  Non-vertebral fracture was added as a secondary outcome. Although captured by
    administrative health data throughout the trial, we had not been asking participants about
    fractures other than hip fracture until mid-trial when we began to ask about any fractures.
   Hence this outcome was less sensitively captured in the early years of the trial.
4. Syncope in the last month, falling in the last month, new glaucoma diagnosis, nocturia
   frequency, and new impairment consistent with dementia were added as secondary
    safety outcomes. The information defining these outcomes had been collected from all
    participants since the beginning of the trial but had not previously been prespecified as
   outcomes we would analyze. They were all believed to meaningfully augment our other
    safety outcomes.





© 2025 American Medical Association. All rights reserved, including those for text and data
mining, AI training, and similar technologies.

```

### Physical PDF page 22 — fresh layout text

```text
   eFigure 1. Location of participating medical clinics





© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.

```

### Physical PDF page 23 — fresh layout text

```text
   eFigure 2. Medications in use at baseline





© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.

```

### Physical PDF page 24 — fresh layout text

```text
eFigure 2. Medications in use at baseline (continued)





© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar
technologies.

```
