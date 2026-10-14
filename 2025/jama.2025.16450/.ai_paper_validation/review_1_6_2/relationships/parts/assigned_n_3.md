# Disjoint N review shard 3

Exact scope: N726, N727, N728, N729, N730, N731, N732, N733, N734, N735, N736, N737, N738, N739, N740, N741, N742, N743, N744, N745, N746, N747, N748, N749, N750, N751, N752, N753, N754, N755, N756, N757, N758, N801, N802, N803, N804, N805, N806, N807, N808, N809, N810, N811, N812, N813, N814.

## N726 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N726|[DOC-003 p86](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=86)|Web EDC network ID six digits: five-digit family ID links siblings plus one-digit birth order; first digit 1–9, examples 100221/310002. Birth-order need not follow strict delivery order but consistent per infant; only eligible infants numbered from 1. Outside usual GDB criteria requires NRN-study Y; usual-criteria infants do not require it. PAIR enrollment separate checkbox. Administrative identifiers do not provide counts.|Sibling/pregnancy linkage; registry inclusion|

## N727 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N727|[DOC-003 p87](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=87)|Masked trial medications coded T for unknown active/placebo, Y if later known clinical medication. First-dose date initially trial dose then replaced by known clinical medication date with comment retaining trial exposure. Course count left blank for T, replaced by number of known clinical courses if later treated; medication type Other/comment under T then actual known type if later treated. Training ID T0001 and illustrative network ID 688751=68875+1 are examples, not data.|Concomitant medication ascertainment and trial masking|

## N728 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N728|[DOC-003 p88](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=88)|Unmasked trials: Y for received active treatment; date first dose, total completed courses, actual type recorded. Mother biological at delivery, surrogate if applicable. Age completed years. Gravidity all confirmed pregnancies including current. Parity pregnancies reaching ≥20 weeks 0 days including delivery, irrespective fetal count/outcome; each twin same parity; example first twin pregnancy parity1, next pregnancy parity2.|Baseline maternal age/parity and concomitant treatment|

## N729 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N729|[DOC-003 p88](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=88)|Marital status code1 married (including separated/common law); 2 single/divorced/widowed; 6 unknown. Highest education biological or surrogate mother at delivery, record reliable source.|Baseline categorical ascertainment|

## N730 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N730|[DOC-003 p89](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=89)|Education codes:1 ≤8th grade;2 grades9–12/no diploma;3 diploma/GED and <one full college year;4 trade/technical;5 ≥one college year or associate degree/no BA/BS;6 BA/BS/no higher degree;7 graduate;8 unknown. All insurance types at admission:10 public,3 private,5 self-pay/uninsured,6 unknown,9 other. Ethnicity:1 Hispanic/Latino regardless race;2 not Hispanic/Latino;3 unknown/not reported. Codes identify categories, not ordinal outcomes/counts.|Baseline maternal demographic categories|

## N731 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N731|[DOC-003 p90](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=90)|Race:1 Black;2 White;3 American Indian/Alaskan Native;4 Asian (includes Philippine origins; historically grouped Pacific Islander);5 Native Hawaiian/other Pacific Islander;6 >one race;7 unknown/not reported. Maternal height inches/cm, pre-pregnancy or earliest first-trimester weight pounds/kg, delivery weight pounds/kg; unknown PM permanently missing.|Baseline race and maternal anthropometric units|

## N732 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N732|[DOC-003 p90](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=90)|Multiple gestation: exclude early fetal reductions <14 weeks; number fetuses includes live/stillborn. Pregnancy complications 4a/5a yes/no/unknown; chart-listed problem Y otherwise Unk/N.|Multiple-birth definition|

## N733 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N733|[DOC-003 p91](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=91)|Prenatal care1 no visits;2 limited (<3 visits OR started third trimester);3 adequate (≥3 visits AND started before third trimester). First ultrasound GA weeks/days; unknown days PM or * rather than0; if GA unavailable first-trimester ultrasound indicator uses <14 weeks.|Baseline care and ultrasound measurement definitions|

## N734 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N734|[DOC-003 p91](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=91)|Pregestational diabetes prior diagnosis Y; type1 code1, type2 code2, type unknown3. Highest treatment level:1 insulin,2 oral hypoglycemic,3 diet only,5 none,6 unknown.|Baseline maternal diabetes/treatment|

## N735 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N735|[DOC-003 p92](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=92)|Gestational diabetes diagnosed during pregnancy; same highest-treatment hierarchy as N734. Maternal hypertension BP >140 systolic OR >90 diastolic on ≥2 occasions prior/during pregnancy; chronic/prior flag. Antepartum bleeding after20 weeks excludes bloody show. Clinical chorioamnionitis chart-documented; histologic chorioamnionitis after placental pathology refers Appendix Ia; acute funisitis documented Y otherwiseN.|Maternal hypertension/diabetes/chorioamnionitis baseline definitions|

## N736 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N736|[DOC-003 p93](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=93)|Admission date/time reliable source; absent time first maternal vitals; midnight00:00. ROM before delivery Y; simultaneous delivery N; cesarean undocumented date/time assume delivery N; undocumented ROM Unk. Unknown exact date/time asks estimated ROM >18h.|Rupture-of-membranes baseline threshold|

## N737 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N737|[DOC-003 p93](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=93)|Antenatal steroid exposure during pregnancy Y/N/Unk; types1 betamethasone,2 dexamethasone,3 both,4 unknown; trial T if active/placebo unknown. Complete course:2 betamethasone doses OR4 dexamethasone doses in one course for fetal maturation AND ≥24h first dose to delivery; shorter elapsed interval incomplete; only predelivery doses count. More than one course Y if any dose beyond one complete course, N if ≤one course, Unk if unknown.|Antenatal steroid subgroup/baseline exposure and completion|

## N738 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N738|[DOC-003 p94](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=94)|Maternal antibiotics within72h predelivery exclude prophylactic intraoperative antibiotics. Magnesium sulfate this admission predelivery Y/N/unknown. Electronic fetal-heart monitoring within12h predelivery excludes stethoscope/sonogram. Delivery modes1 vaginal vertex,2 breech,3 cesarean,5 unknown.|Baseline antenatal treatments and delivery|

## N739 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N739|[DOC-003 p94](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=94)|Calendar day00:00–23:59; birth date Day of life1 even if partial24h, next calendar day Day2. Outborn means outside designated network-hospital walls; includes outside-born trial participants. Birth/date/time and outborn admission date recorded.|Days-of-life/timepoint definition and birthplace|

## N740 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N740|[DOC-003 p95](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=95)|Prenatal diagnosis other than prematurity/immaturity leading to care limits recorded all applicable; Other codes199/299/399/499/599/699/799 are system identifiers. Death ≤12h includes delivery room, NG03E. Sex1 male,2 female,3 ambiguous requires genetics consult/pathology confirmation. GA methods1 obstetric,2 neonatal; LMP-based OB discrepancy >2weeks neonatal prevails, as N725.|Early mortality, sex and GA baseline/population|

## N741 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N741|[DOC-003 p96](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=96)|Official Apgar at1,5,10minutes. Delivery support Y for each: oxygen FiO2>.21 by mask/hood/CPAP/ET; PPV mask/prongs bag/Neopuff; CPAP; intubation even transient for breathing, excludes suction/surfactant-only tube immediately removed; chest compressions; epinephrine IV/intratracheal.|Delivery respiratory support and baseline Apgar|

## N742 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N742|[DOC-003 p96](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=96)|Documented cord clamping/milking Y otherwiseN. Clamping delay codes1 <30s;2 30–60s;3 >1–3min;4 >3min before pulsation stops;5 until stop;6 other. Birthweight grams with source hierarchy continued p97.|Baseline cord management and birthweight|

## N743 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N743|[DOC-003 p97](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=97)|Birthweight preferred delivery record, nursery admission, admission examination, pathology on death; centers may choose more reliable order. Length/HC centimeters within72h birth; HC preferred admission examination, nursery admission, pathology. Thermal wrap documentation Y, absentN, standard care with missing documentation Unknown; wraps/PE bags/exothermic mattress included, NICU bed covers/tents excluded. First temperature after nursery/holding/stabilization admission Celsius or Fahrenheit; date/time, source1 rectal,2 axillary,3 skin.|Baseline anthropometry/temperature and ascertainment|

## N744 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N744|[DOC-003 p98](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=98)|NG03 from birth through day120/discharge/transfer/death, whichever first; death ≤12h NG03E instead NG03/NG07. NG05 only hospitalized >120d, completed after death/discharge/transfer. Pending autopsy cause TM then update; do not delay form. First discharge home ends data collection, no further data on readmission. Within-center transfers tracked to final departure. Outside transfers seek final death/discharge; return within7d without home discharge continuous admission; NRN-to-NRN is not transfer status.|Mortality and morbidity observation boundary; missing causes; disposition|

## N745 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N745|[DOC-003 p99](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=99)|Transfers ≤120d: previous attained events Y, others blank until receiving center disposition/120d; time-limited questions (first24h,<72h,first28d,36weeks) completed only if reached; ongoing/updatable events supplied; counts of days/courses through transfer with end date for continued counting. NG07 highest support each attained timepoint; unachieved blank/dates since last point. >120d NG07 already completed; NG05 starts sectionB, attained problemsY, othersblank. NG02 origin hospital, NG03E generally not transfer.|Outcome counts/timepoints and cross-center completeness|

## N746 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N746|[DOC-003 p100](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=100)|NG03 status1 home,2 hospitalized at120d,3 outside transfer/no return network within7d,5 dead; date recorded. Weight grams, length/HC centimeters on status date or within7d. Care-limit discussions priorNG03status/prior120d Y; intubation/ventilation and nutrition/hydration withheld/limited/withdrawn flagged; palliative/ethics consults recorded. Transfer section applies no7dreturn.|Disposition/mortality and growth outcome timepoint|

## N747 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N747|[DOC-003 p101](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=101)|Transferred final outcome1 died hospital,2 home,3 hospitalized at1year. At home discharge: continuous oxygenY/N; medications Y/N/T masked trial: diuretics, bronchodilators, anticonvulsants, antireflux, antihypertensives, methylxanthines, inhaled steroids, systemic steroids, other; exclude vitamins/iron. Human milk Y/N with type continuation p102.|Discharge oxygen and respiratory medication outcomes|

## N748 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N748|[DOC-003 p102](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=102)|Milk type1 maternal,2 donor,3 both,4unknown. Death section if status5 or transferred final outcome died hospital; include subsequently available evidence. Date death; autopsy if done wait for results for cause. Contributory cause is single underlying proximate etiologically specific antecedent cause, clinical/autopsy evidence, chosen with PI; detail codes10 congenital,31sepsis,90other. Codes not realized counts.|Mortality/date/cause ascertainment|

## N749 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N749|[DOC-003 p102](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=102)|36-week status all infants:1home,2hospital at36weeks,3transfer/no7dreturn,5dead. If hospital record actual measurement date; growth measurements within36weeks±7d, dates need not same, use weight date if different. N750 continuation units.|36-week status and growth timepoint; distinguish from physiologic BPD test window|

## N750 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N750|[DOC-003 p103](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=103)|At36weeks±7d: weight grams, length/HC centimeters; printed label gestational age. No growth score formula or computed result.|36-week anthropometric outcome units/window|

## N751 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N751|[DOC-003 p103](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=103)|Surfactant any preparation/location; first date and delivery-room indicator. Products1 beractant/Survanta,2 poractant alfa/Curosurf,3 calfactant/Infasurf,9other. Mixed with budesonide Y/N; T for BiB enrolled, section3.2.1 masked instructions. Administration1ETT (includes INSURE),2 LISA/MIST catheter below vocal cords,3aerosol mask/prongs,4LMA,9other. No additional randomized dose stated.|Intervention receipt/masking, surfactant product/route|

## N752 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N752|[DOC-003 p104](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=104)|Pneumothorax documented pleural air/displaced lung, excludes thoracotomy-associated. PIE documented radiographic/pathologic air from alveoli/small airways into perivascular tissues, includes clinical notes. Pulmonary hemorrhage bright red ET blood with clinical deterioration. All Y/N.|Pulmonary air leak and hemorrhage secondary outcomes|

## N753 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N753|[DOC-003 p104](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=104)|Systemic steroids any dose/course preventing/treating BPD/CLD, excludes inhaled and extubation/stridor doses. First-dose date, >one courseY/N, total exposure >14daysY/N; drug codes2dexamethasone,6hydrocortisone,7prednisolone. Masked/unmasked treatment and later care use N727/N728 rules. Inhaled nitric oxide receipt/first exposure Y/T/date; vitaminA continuation p105.|Postnatal steroid and rescue respiratory-treatment outcomes|

## N754 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N754|[DOC-003 p105](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=105)|VitaminA receivedY and trial coding rules. PDA clinical left-to-right shunt evidence (murmur/hyperdynamic precordium/bounding pulses/wide pulse pressure/heart failure/increased pulmonary vasculature/cardiomegaly/O2) OR ECHO left-to-right shunt. Treatments indomethacin/ibuprofen/acetaminophenY/N/trial; catheter closure includes failed closure, date and successY/N.|PDA and treatment secondary outcomes|

## N755 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N755|[DOC-003 p106](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=106)|New vasoactive drugs within24h after catheter PDA closure or surgeryY/N. Surgical ligation and other treatments (coils)Y/N; exclude fluid restriction. Hypotension treatment first24h: volume bolus, vasopressor initiation, systemic steroid initiation flags. ECHO to monitor pulmonary hypertension first week, date/treatment; late/chronic ECHO date continuation p107.|PDA treatment and early hypotension/pulmonary hypertension outcomes|

## N756 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N756|[DOC-003 p107](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=107)|Late/chronic pulmonary hypertension ECHO date/treatment. Indomethacin first24hY/N/trial rules; EEG-confirmed seizuresY/N.|Neurologic and pulmonary vascular outcomes|

## N757 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N757|[DOC-003 p107](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=107)|Cranial ultrasound within28d; if none skipI6; if all no ICH/PVL/ventriculomegaly skipI6. ICH any brain bleed including germinal matrix. Most severe scan first28d; earliest if ties. Rank germinal/subependymal <ventricular blood <dilatation <parenchymal blood. Discrete echodensity/increased echogenicity equivalent. Only definite findings, consultPI if unclear; separate3c–3g independent findings not grade; multiple findings allowed.|ICH/brain injury outcome definition, imaging window and aggregation|

## N758 — mapped relationship

Source mapping artifact: extraction/parts/manual_082_108.md

|N758|[DOC-003 p108](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=108)|Findings:3c germinal/subependymal blood (if ventricular-only codeN);3d ventricular blood regardless size;3e enlarged ventricles with concurrent/prior blood on any scan;3f enlargement without blood on any scan;3g parenchymal blood (may lack ventricular blood, differs diffuse echogenicity). Laterality right/left/both; midline shiftY/N. Grade-only report maps I→3c,II→3d,III→3d+3e,IV→3g; isolated dilation/no blood→3f. Basal ganglia/thalamus and cerebellar hemorrhage separate flags. If reported grade and description differ, description prioritized, confirmPI.|ICH grade III/IV mapping and imaging outcome ascertainment|

## N801 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N801 — Nutrition measurement units and threshold

PLAN pp111–112, J1–2. Match keys: nutrition duration, full enteral feeds, feeding descriptors. Parenteral days count any day amino acids or lipid solution was received, even for part of the day; zero if never. Enteral feeds include breast milk, formula and colostrum priming reaching the stomach; exclude sterile water. First feed codes: 1 maternal, 2 donor, 3 formula; mixed first feeds use the majority type. Record first feed date and first date feeds reach 120 ml/kg/day, using current weight. First-28-day human milk codes printed: 1 maternal only, 2 donor only, 4 none; printed instruction is: "None if the infant did not receive maternal milk, donor milk or was not in a feeding trial in the first 28 days." Fortification: 1 bovine, 2 human milk, 3 both, 4 neither.


## N802 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N802 — Hematology measurements

PLAN p116, M. Blood type: 1 A, 2 B, 3 AB, 4 O, 5 unknown; Rh: 1 positive, 2 negative, 3 unknown. pRBC at any time before status: first date, lowest hemoglobin (g/dL) OR hematocrit (%) before first transfusion, and total transfusion count. Enter only one laboratory measure, using the center's usual clinical measure. Platelets: first date and lowest pretransfusion count; no platelet unit printed here. Erythropoiesis agents Y/N, study medication refers to 3.2.1. Highest total bilirubin in first 14 days, mg/dL. Match keys: laboratory safety and cointerventions.


## N803 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N803 — Renal measurements

PLAN pp117–118, N. BP systolic/diastolic in mmHg within ±1 week of status. Multiple readings discussed with PI; example normal repeat within 24 hours after crying may be recorded, whereas similar consistently elevated readings retain elevated value. Serum creatinine first 6 weeks: row 1 days 1–4, row 2 days 5–7, then weeks 2–6. Maximum/minimum mg/dL and respective dates for each period. Match keys: renal safety and measurement windows.


## N804 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N804 — Other infection classification dictionary

PLAN p120. Other proven infections: 4 syphilis, 5 toxoplasmosis, 6 HIV, 7 SARS-CoV-2, 8 HSV, 9 CMV, 10 influenza, 11 RSV, 12 other specified. Diagnosis number, date, code and treated Y/N recorded. Malformation codes refer to Appendix H. Match keys: infection and malformation outcomes.


## N805 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N805 — Procedure-record capacity

PLAN p121. All surgery/catheterization before status, including ROP and fetal surgery: date, all procedure codes and surgical site infection Y/N/Unk. Six paper entries; DMS accepts 10. Include failed catheter closures. Other surgery codes end in 99 and require specification. No observed procedure count printed. Match key: surgical morbidity.


## N806 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N806 — Early-death surfactant and route dictionary

PLAN p122. Surfactant codes: 1 beractant/Survanta, 2 poractant alfa/Curosurf, 3 calfactant/Infasurf, 9 other. Mixed budesonide Y/N, or T if BiB enrolled, referring to 3.2.1. Routes: 1 ETT including INSURE via ETT, 2 LISA/MIST catheter below vocal cords, 3 aerosol by nebulizer mask/prongs, 4 LMA, 9 other. Pressors include dopamine, dobutamine, epinephrine, isuprel. Volume support includes albumin 5% or 20%, blood, FFP, plasmanate, Ringer's lactate. Intubation/ventilation and IV fluids Y/N. No randomized dose printed. Match key: surfactant/budesonide exposure.


## N807 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N807 — Late-status anthropometry and milk codes

PLAN pp124,127. Weight grams, length and head circumference centimeters at status preferably, or within 7 days. Human milk at discharge: yes, no or unknown; type 1 maternal, 2 donor, 3 both, 4 unknown. Match keys: growth and discharge descriptors.


## N808 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N808 — Respiratory day-count and paired FiO2/flow example

PLAN p129. Birth calendar day is day 1 despite less than 24 hours; next calendar day is day 2. Total support days cannot exceed day of life. Example day 7: 4 CV + 2 nasal ventilation + 1 CPAP = 7 days. Highest FiO2 and mode recorded at each point; nasal flow paired with highest FiO2. Example FiO2 1.00 at 0.03 lpm and .27 at 0.5 lpm on same day: record 1.00 and 0.03 lpm. Match keys: respiratory duration and oxygen assessment.


## N809 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N809 — Weight collection windows

PLAN p130, A4. Weight windows: day 3 uses days 2–4; day 7 uses 6–8; day 14 uses 12–16; day 28 uses 26–30; 36 weeks uses 36-0/7 to 37-0/7 weeks; 40 weeks uses 40-0/7 to 41-0/7 weeks. Weight grams enters effective oxygen calculation. Match key: BPD assessment window.


## N810 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N810 — Outcome-related surgical code labels

PLAN pp141–142. Outcome-related procedure codes: 201 laparotomy; 202 bowel resection/anastomosis or perforation repair; 203 jejunostomy/ileostomy/colostomy primary/revision; 204 ostomy takedown; 205 peritoneal drain for any reason including NEC/IP; 206 gastrostomy; 301 tracheostomy. CNS: 601 posthemorrhagic hydrocephalus shunt, 602 other hydrocephalus shunt, 603 ventricular reservoir, 604 exteriorization/revision, 605 removal. ROP: 902 laser ablation, 903 scleral buckle, 904 vitrectomy; 906 other ophthalmology explicitly excludes ROP. Remaining procedure codes describe operations without numerical results or decision thresholds. Match keys: surgical NEC/IP, hydrocephalus, ROP therapy, respiratory support.


## N811 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N811 — Certification example values, not participant results

PLAN p151. Hypothetical certification eligibility examples, not participant results: mechanical ventilation; 33 weeks gestation; room air; 2.0 kg/2 lpm/100% oxygen/saturation 90–96%; 1.8 kg/1 lpm/60%/90–96%; 1.9 kg/0.25 lpm/70%/>96%; 2.1 kg/0.1 lpm/30%/>96%; 1.7 kg/0.5 lpm/40%/>96%. Y/N answers blank. BPD/no BPD examples: all saturations ≥96% for 15 minutes in room air; <90% for 6 minutes; ≥90% for 30 minutes; mostly ≥90% with 1 minute at 85% spontaneously returning >90%. Classification answers blank. Apnea question contrasts observation with usual institutional routines including increasing support after brief observation. Match key: illustrative challenge rules only.


## N812 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N812 — Printed Table1: factor as a function of flow and weight

PLAN [p152](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=152), Appendix J Table 1. Flow LPM; weight kg. Every printed lookup value follows. Blank alternate-flow cells use —. Printed lookup values, not workbook formulas or caches.

| Flow LPM | Alternate LPM | 0.7kg | 1.0kg | 1.25kg | 1.5kg | 2kg | 2.5kg | 3kg | 3.5kg | 4kg |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0.01|—|1|1|1|1|1|0|0|0|0|
|0.03|1/32|4|3|2|2|2|1|1|1|1|
|0.06|1/16|9|6|5|4|3|2|2|2|2|
|0.125|1/8|18|12|10|8|6|4|4|4|4|
|0.15|—|21|15|12|10|8|6|5|4|4|
|0.25|1/4|36|25|20|17|13|10|8|7|6|
|0.5|1/2|71|50|40|33|25|20|17|14|13|
|0.75|3/4|100|75|60|50|38|30|25|21|19|
|1.0|1.0|100|100|80|67|50|40|33|29|25|
|1.25|—|100|100|100|83|63|50|42|36|31|
|1.5|—|100|100|100|100|75|60|50|43|38|
|2.0|—|100|100|100|100|100|80|67|57|50|
|3.0|—|100|100|100|100|100|100|100|86|75|
|4.0|—|100|100|100|100|100|100|100|100|100|
|5.0|—|100|100|100|100|100|100|100|100|100|
|6.0|—|100|100|100|100|100|100|100|100|100|


## N813 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N813 — Printed Table2: effective FiO2 (×100) by factor and concentration

PLAN [p154](../../../../joi250072supp2_prod_1761000786.6938.pdf#page=154), Appendix J Table 2. Columns: factor and concentration percent. Every printed lookup cell follows, preserving the printed factor sequence. Dark shading begins at 27% effective oxygen, with no separate legend. Printed lookup values, not formula results.

| Factor | 21% | 22% | 25% | 30% | 40% | 50% | 100% |
|---:|---:|---:|---:|---:|---:|---:|---:|
|0|21|21|21|21|21|21|21|
|1|21|21|21|21|21|21|22|
|2|21|21|21|21|21|22|23|
|3|21|21|21|21|22|22|23|
|4|21|21|21|21|22|22|24|
|5|21|21|21|21|22|22|25|
|6|21|21|21|22|22|23|26|
|7|21|21|21|22|22|23|27|
|8|21|21|21|22|23|23|27|
|9|21|21|21|22|23|24|28|
|10|21|21|21|22|23|24|29|
|11|21|21|21|22|23|24|30|
|12|21|21|21|22|23|24|30|
|13|21|21|22|22|23|25|31|
|14|21|21|22|22|24|25|32|
|15|21|21|22|22|23|25|33|
|17|21|21|22|23|24|26|34|
|18|21|21|22|23|24|26|35|
|19|21|21|22|23|25|27|36|
|20|21|21|22|23|25|27|37|
|21|21|21|22|23|25|27|38|
|22|21|21|22|23|25|27|38|
|23|21|21|22|23|25|28|39|
|25|21|21|22|23|25|28|41|
|27|21|21|22|23|25|29|42|
|28|21|21|22|24|26|29|43|
|29|21|21|22|24|27|29|44|
|30|21|21|22|24|27|30|45|
|31|21|21|22|24|27|31|47|
|33|21|21|22|24|27|31|47|
|36|21|21|22|24|28|31|49|
|38|21|21|23|24|28|32|51|
|40|21|21|23|25|29|33|53|
|42|21|21|23|25|29|33|54|
|43|21|21|23|25|29|33|55|
|44|21|21|23|25|29|34|56|
|50|21|21|23|25|30|35|60|
|55|21|22|23|26|31|37|64|
|57|21|22|23|26|32|38|66|
|60|21|22|23|26|32|38|68|
|63|21|22|24|27|33|39|71|
|67|21|22|24|27|34|40|74|
|71|21|22|24|27|34|42|77|
|75|21|22|24|28|35|43|80|
|80|21|22|24|28|36|44|84|
|83|21|22|24|28|37|45|87|
|86|21|22|24|29|37|46|89|
|100|21|22|25|30|40|50|100|


## N814 — mapped relationship

Source mapping artifact: extraction/parts/manual_109_162.md

### N814 — Conversion example

PLAN pp154–155. Example asks effective FiO2 for a 2.0 kg infant on 100% oxygen at 0.15 lpm. Answer: Table 1 factor 8; Table 2 factor 8/100% gives 27%; states less than 30% and eligible for physiologic evaluation. No saturation value supplied in the example answer. Instructional example, not an observed result.


