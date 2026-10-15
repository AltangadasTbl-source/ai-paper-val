# Fresh support extraction: DOC-002 protocol, physical PDF pages 1–32

Scope: only joi250046supp1_prod_1755300121.14087.pdf physical pages 1–32. Document role PLAN, assigned by prospective protocol content. Version 5.0, 10 November 2022. This is extraction, not candidate discovery or adjudication. Descriptive local keys PA001 onward are available for merger into the global relationship inventory. Matching main-paper keys are semantic join keys only; the main paper lies outside this shard and its mapper supplies exact main locations.

Engine/provenance: original raw OCR and images for physical pages 1–20 under .ai_paper_validation/review_1_5_1/preprocessing/doc002_ocr/ and doc002_render/; original engines not versioned. Readable original OCR pages 1–5 and15 used; images support every reused unit. Fresh OCR of original images for pages6–14 and16–20 uses supplied pdf_tools.py, pinned rapidocr-onnxruntime1.3.24 CPU (intra-op2/inter-op1). Fresh native and sorted-layout extraction for pages21–32 uses supplied helper and pinned PyMuPDF1.26.4; embedded glyph text is unusable. Fresh rendering pages22–32 uses the same helper/PyMuPDF at200dpi CPU; page21 current source render/OCR supplied by coordinator. Fresh OCR pages22–26 uses the pinned CPU engine. All fresh derivatives are in .ai_paper_validation/review_1_6_2/preprocessing/protocol_a_restart/. No source or reused asset changed. No workbook formulas/caches apply in this PDF-only scope.

Source evidence links use physical page numbering and are relative to this artifact: [protocol](../../../../joi250046supp1_prod_1755300121.14087.pdf#page=1). Printed pagination is separately recorded. No outside pages, old scientific maps, findings, candidates, screening logs, or reports were used.

## Page coverage

| Physical page | Printed page | Content opened and mapped | Applicability |
|---:|---|---|---|
|1|Unnumbered|Title, version, registration identity|Administrative identity only|
|2|I|Compliance statement|No result-relevant quantitative analysis|
|3|II|Amendment history|Outcome, stratification and window changes PA002–PA007|
|4|III|Amendment history|Eligibility and qualitative participation changes PA008|
|5|IV|Amendment history|Eligibility and intervention-description changes PA009–PA011|
|6|V|Amendment history|Enrollment-target and intervention-support changes PA012–PA013|
|7|VI|Amendment history|Target enrollment/randomization and qualitative timing PA014–PA015|
|8|VIII|Contents, sections1–9|Pointers only; no independent result/analysis specification|
|9|IX|Contents continuation|Pointers only; no independent result/analysis specification|
|10|X|Contents continuation|Pointers only; no independent result/analysis specification|
|11|XI|Abbreviations first page|Outcome/statistical definitions PA016|
|12|XII|Abbreviations second page|Outcome/statistical definitions PA017|
|13|1|Synopsis aims, design and interventions|PA018–PA023|
|14|2|Synopsis population, intervention and durations|PA024–PA027|
|15|3|Synopsis durations continuation|PA028|
|16|4|Table1 schedule and footnotes|PA029–PA033|
|17|5|Introduction background|Chronic-pain definitions expanded below; other historical context only|
|18|6|Rationale|Rationale/background only; intervention rationale contextualized in PA034|
|19|7|Specific aims, risks|PA035–PA038|
|20|8|Risks and mitigation|PA039; remaining ethics/confidentiality material not result-relevant|
|21|9|Risks and benefits|No numeric result/analysis specification; free withdrawal, unrestricted routine care contextualize population|
|22|10|Primary/secondary outcome table|PA040–PA043|
|23|11|Secondary outcome table continuation|PA044–PA049|
|24|12|Economic objectives table|PA050 onward|
|25|13|Exploratory objectives|Mapped below|
|26|14|Moderator/mediator table|Mapped below|
|27|15|Qualitative evaluation objectives|Mapped below|
|28|16|Qualitative evaluation table continuation|Mapped below|
|29|17|Study design/arms/randomization|Mapped below|
|30|18|Randomization continuation and design rationale|Mapped below|
|31|19|Intervention rationale/end of study|Mapped below|
|32|20|Study population/inclusion criteria|Mapped below|

## Relationships and semantic joins

| Key | Physical page(s) | Printed source specification | Main-paper semantic join |
|---|---|---|---|
|PA001|1|Title: Tailored Non-Pharmacotherapy Services for Chronic Pain: Testing Scalable and Pragmatic Approaches (RESOLVE Study). UH3 protocol version5.0,10November2022; NCT04523714.|Trial identity and protocol version|
|PA002|3|07/15/20 amendment: trial phase changed to phaseIII (sections1.1,4.1); added age and race/ethnicity subgroup analyses (sections3.4,15.7).|Trial design; subgroup prespecification|
|PA003|3|08/06/20 amendment: modified BPI-SF11 items; pain-intensity subscale4 items (sections3.1,3.2).|Pain composite and component definitions|
|PA004|3|08/06/20 amendment: sex stratification uses EHR sex rather than self-reported baseline-survey sex to ensure variable availability.|Randomization strata/source of sex|
|PA005|3|09/25/20 amendment:3month window80–140days(previous75–110);6month170–230(previous165–200);12month350–410(previous345–480). Maximum active-intervention duration12weeks moved to Table1 footnote.|Outcome assessment windows and treatment duration|
|PA006|3|09/25/20 amendment adds MCID assessment for pain-intensity and pain-interference subscales as secondary outcomes(section3.2,15.6).|Outcome hierarchy and binary subscale responders|
|PA007|3|09/25/20 amendment adds rural/medically underserved residence as randomization stratum and adjustment variable(sections4.3,15.5).|Strata and primary-analysis covariates|
|PA008|4|09/25/20 amendment adds KPWA-only no-OUD ICD10 inclusion criterion;11/23/20 clarifies patients not completing active interventions remain enrolled for qualitative interviews;03/22/21 coach interviews approximately12 rather than up to10.|Eligibility; treatment discontinuation versus withdrawal|
|PA009|5|03/31/21: KP-site pain encounters increased to≥2 at least30days apart; Essentia remains≥1.|Eligibility and enrolled population|
|PA010|5|03/31/21: all-site exclusion for surgery in prior60days and planned/scheduled surgery in next year.|Eligibility and population definition|
|PA011|5|02/24/22: painTRAINER described as online CBT-based pain-management program; virtual coach-led telephonic/video CBT-CP; Aim1 retains pain severity(intensity+interference) relative to usual care at3months.|Intervention contrast and primary outcome|
|PA012|6|02/24/22: target enrollment2,380 may be exceeded to attain randomized2,331 because not everyone consented/enrolled is randomized; randomized target described as invariable in amendment rationale.|Consented versus randomized population target|
|PA013|6|02/24/22: painTRAINER online browser program rather than downloadable application; active interventions described as independent/standalone; onboarding and ongoing support/outreach added for both; motivational-interviewing language in painTRAINER onboarding.|Delivered intervention and support|
|PA014|7|11/10/22 amendment updates enrolled target from2,380 to approximately2,500; total enrolled/randomized per site may vary595–625; goal randomized at least2,331 or777per arm, possibly slightly over; four sites.|Enrollment/randomization targets|
|PA015|7|11/10/22: up to2 interviews per healthcare stakeholder in years4–5 rather than years2–3.|Qualitative evaluation time frame|
|PA016|11|Abbreviations contextualize BPI-SF, CBT-CP, CI, DSMB, EHR, MCID; source definitions are expanded below.|Outcome and analysis notation|
|PA017|12|N=number(typically participants); OR=odds ratio; PEG=Pain, Engagement of Life & General Activity; PROMIS=Patient-Reported Outcomes Measurement Information System; QALY=quality-adjusted life year; SAP=statistical analysis plan; UC=usual care study arm/group.|Effect-measure and outcome definitions|
|PA018|13|Multicenter comparative effectiveness trial;3arm parallel intervention design; online self-directed program and live coach-led telephone/video sessions each compared with usual care.|Design and comparison/reference group|
|PA019|13|Participants in both active arms complete8CBT-based sessions approximately1per week; all trial participants enrolled12months; assessments baseline, notification of randomization,3,6,12months.|Dose and outcome times|
|PA020|13|Aim1 primary effectiveness: clinically meaningful pain-severity improvement(intensity+interference) relative to usual care3months.|Primary binary pain response|
|PA021|13|Aim1a secondary pain and quality-of-life outcomes: social-role functioning, physical functioning, PGIC. Exploratory outcomes: long-term opioid use; depression/anxiety/sleep disturbance; high-impact chronic pain and graded chronic pain.|Secondary/exploratory outcome status|
|PA022|13|Aim1b subgroup heterogeneity: sex,rural/medically underserved residence,multiple pain conditions,mental-health mood disorders,negative social determinants. Aim1c mediators: catastrophizing,pain-related self-efficacy,perceived support.|Subgroups and mediators|
|PA023|13|Aim2 cost and incremental cost-effectiveness of online and virtual coach-led interventions compared with each other and usual care. Qualitative interviews subset at approximately3–5 and12–14months; approximately20health-system stakeholders across4sites and approximately12virtual-session staff.|Economic/qualitative outcome status|
|PA024|14|Approximately2,500enrolled with high-impact chronic pain; randomized target approximately2,331(at least777per arm). Enrollment may exceed2,500 to ensure at least2,331randomized;120randomized participants qualitative interviews.|Flow denominators and trial target|
|PA025|14|Four systems: KPGA,KPNW,KPWA,Essentia; phaseIII trial.|Trial design/population context|
|PA026|14|Both active programs8sessions expected weekly; analogous content but independent programs; usual-care arm receives bound2020American Chronic Pain Association Resource Guide to Chronic Pain Management; any pharmacologic/nonpharmacologic treatment unrestricted.|Intervention doses and control condition|
|PA027|14|Study duration48months from enrollment start to completed analyses.|Administrative duration only|
|PA028|15|Subject duration12–14months; majority12months, qualitative subset last interviews12–14months. Estimated enrollment completion25months.|Follow-up duration|
|PA029|16|Table1 columns: screening/consent day−14to−1or0; baseline/randomization day0; notification approximatelyday1–7; intervention sessions1–8 approximatelydays8–14,15–21,22–28,29–35,36–42,43–49,50–56,57–63.|Randomization origin and dose schedule|
|PA030|16|Table1 follow-up3monthday80–140;6month170–230;12month/final350–410. Assessments baseline,notification,3,6,12months. Subset interviews3and12month columns.|Outcome assessment schedule|
|PA031|16|Eligibility and consent may occur screening or baseline; baseline assessment and randomization baseline column; notification notification column; eight interventions each session column; adverse-event review from intervention1 through12month follow-up.|Outcome collection and safety window|
|PA032|16|Footnote1: screening,consent,baseline may occur in same telephone/online encounter; otherwise consent/baseline within14days of screening. Footnote2: active sessions weekly over8weeks; maximum active-session duration12weeks; see10.2.|Timing and intervention duration|
|PA033|16|Stakeholders approximately2hour-long telephone interviews; coaches/intervention staff2approximately hour-long telephone interviews early/later implementation.|Qualitative measurement schedule|
|PA034|18|Rationale describes CBT-CP psychological/behavioral nonpharmacologic care delivered in scalable online/virtual modalities; no reported trial estimate, model, or power inputs on this page.|Intervention identity context|
|PA035|19|Aim1 clinically meaningful improvements explicitly≥30%in pain severity(intensity+pain-related interference), relative to usual care3months.|Primary responder threshold/direction|
|PA036|19|Aim1a secondary social-role functioning,physical functioning,PGIC; exploratory opioid use,depression,anxiety,sleep disturbance,high-impact/graded chronic pain.|Outcome hierarchy|
|PA037|19|Aim1b subgroups sex,rural/medically underserved residence,multiple pain conditions,mood disorders,negative social determinants;1c catastrophizing,self-efficacy,perceived-support mediation.|Heterogeneity and mediation|
|PA038|19|Aim2 incremental cost-effectiveness(active programs versus each other and usual care);Aim3 qualitative treatment response/site/residence and implementation.|Economic/qualitative status|
|PA039|20|All enrollees may receive unrestricted pharmacologic/nonpharmacologic care; may refuse session recordings and remain in study; may omit questions or terminate surveys/interviews without adverse consequences.|Population retention/missing assessment context|
|PA040|22|Primary objective: higher proportion achieving MCID pain severity(intensity+interference) relative to usual care3months. MCID defined30%decrease modified11item BPI-SF from baseline;binaryYes/No;self-report baseline/3months;timeframe baseline–3months.|Primary binary responder outcome|
|PA041|22|Secondary objective MCID composite at6and12months;same binarydefinition;self-report baseline,6,12;baseline–6and12months.|Long-term binary responder status|
|PA042|22|Secondary objectives row: MCID pain intensity30%decrease4item BPI-SF intensity subscale;binaryYes/No. Outcome-measured-by column prints self-report baseline,6,12months;timeframe prints Primary:baseline–3months,Secondary:baseline–6and12.|Pain-intensity binary responder and table time labels|
|PA043|22|Secondary objectives row: MCID pain-related interference. Brief-description cell prints “Minimal clinically important difference (MCID) in pain intensity” and30%decrease7item BPI-SF pain-interference subscale;binaryYes/No. Measurement column baseline,6,12;timeframe Primary:baseline–3,Secondary:baseline–6and12months.|Pain-interference binary responder and exact table labels|
|PA044|23|Secondary outcome continuous pain severity:11-item BPI-SF;baseline,3,6,12;timeframe Primary:baseline–3,Secondary:baseline–6/12months.|Continuous pain-severity status/time|
|PA045|23|Secondary continuous intensity:4-item BPI-SF;baseline,3,6,12;samePrimary3/Secondary6,12time labels.|Continuous pain-intensity status/time|
|PA046|23|Secondary continuous interference:7-item BPI-SF;baseline,3,6,12;samePrimary3/Secondary6,12labels.|Continuous interference status/time|
|PA047|23|Secondary social-role functioning:PROMIS Ability to Participate in Social Roles4A(4items;continuous);baseline,3,6,12;sametime labels.|Social-role outcome status/instrument|
|PA048|23|Secondary physical functioning:PROMIS Physical Functioning Short Form6b(6items;continuous);baseline,3,6,12;sametime labels.|Physical-function outcome status/instrument|
|PA049|23|Secondary PGIC:Guy/FarrarPatient Global Impression of Change(1item each for pain status and overall status);self-reported3,6,12months;timeframePrimary:baseline–3,Secondary:baseline–6/12.|PGIC outcome status/instrument/time|
|PA050|24|Economic objective baseline–12months: costs and incremental cost-effectiveness of active programs versus each other/usual care;incremental cost per additional MCID pain-severity patient(30%baseline reduction)estimated12months;QALY gained using EQ-5D-5Lutilities. EHR utilization standardized algorithms/Medicare fee schedules;intervention resource process data;EQ-5D-5Lself-report baseline,3,6,12months.|Economic outcome status/definition/time|
|PA051|25|Exploratory(tertiary)long-term opioid outcome binary continuous≥60day supply in prior90days;orders/fills,including carryover from prescriptions before lookback. EHR quarterly periods baseline survey day0:baseline−89to−0;3month1–90;6month91–180;9month181–270;12month271–360. Timeframe column baseline–3,6,12months.|Opioid outcome status/definition/windows|
|PA052|25|Exploratory depression PHQ8(8items continuous),anxiety GAD7(7items continuous),sleep PROMIS Sleep DisturbanceShort Form6a(6items continuous);self-report baseline,3,6,12;baseline–3,6,12months.|Exploratory outcome hierarchy/instruments|
|PA053|25|Exploratory High Impact Chronic Pain and Graded Chronic Pain Scale–Revised;self-reported intensity,duration,disability;baseline–3,6,12months.|Exploratory pain outcome status|
|PA054|25|Moderators explicitly relate to MCID in pain severity at 6 months: sex male versus female/other, birth sex self-reported at baseline using HEAL CDE; age <65 versus ≥65 years from EHR; race/ethnicity White/non-Hispanic, Black or African American/non-Hispanic, Hispanic, Other, self-reported at baseline.|Subgroup endpoint/time/category definitions|
|PA055|26|Residence moderator urban versus rural/medically underserved; baseline EHR geocoded census tract; rural US Census2010 RUCA codes4–10; underserved HRSA primary-care/mental-health geographic or geographic high-needs health-professional shortage area.|Residence subgroup definition|
|PA056|26|Multiple musculoskeletal conditions:1 pain cluster versus >1; >1 pain ICD10 diagnosis corresponding to >1 cluster, EHR prior360 days. Eight clusters: back; neck; limb/extremity/joint/arthritis; fibromyalgia; headache; orofacial/ear/TMJ; musculoskeletal chest; general pain within Other painful conditions.|Multiple-condition subgroup threshold/lookback|
|PA057|26|Mental-health moderator ICD10 depression and/or anxiety, EHR baseline prior360 days.|Mood-disorder subgroup definition|
|PA058|26|Negative SDH/existing need versus no need: self-report baseline endorsement of one or more domains; financial strain1 item; food insecurity2; transportation/access2; housing instability3.|Social-determinant subgroup definition|
|PA059|27|Mediators explicitly relate to MCID pain severity6 months: Pain Catastrophizing Scale short form6,6 items continuous, baseline/3months; Chronic Pain Self-Efficacy Scale Pain Management subscale5 items continuous, baseline/3months; perceived support2 UG3-developed items, notification of randomization/3months.|Mediation endpoint/assessment timing|
|PA060|27|Qualitative table header “Time Frame during the 4-year UH3 study period”; stakeholder/referring-clinician interviews years4–5; purposeful active-intervention patient sample stratified by site, arm, response and residence;3–5month interviews years1–3,12–14month interviews years2–3.|Qualitative sampling/timing|
|PA061|28|Qualitative discontinuation sample: patients not completing assigned active intervention still enrolled, interviews year1; intervention staff/coach process interviews years1and3.|Treatment discontinuation/qualitative population|
|PA062|29|PhaseIII randomized comparative-effectiveness3-arm parallel trial: online painTRAINER, virtual health-coach CBT-CP, usual care; four systems; UC mailed bound2020 resource guide; all arms allow unrestricted other treatments.|Design/intervention/control condition|
|PA063|29|After baseline collection, individuals randomized equal ratio1:1:1. Stratify EHR sex(male versus female/other), baseline BPI-SF severity<7 versus ≥7, site(KPWA,KPNW,KPGA,Essentia) and EHR census-tract rural/medically underserved residence.|Randomization unit/ratio/strata|
|PA064|29–30|Within each stratum random permuted blocks, random variable sizes3,6,9; approximately equal accrual to three arms. Scheme developed by TIN JHU/Tufts lead and study biostatisticians; TIN Utah DCC tables integrated into KP CHR EDC; randomize after baseline completion.|Allocation procedure/concealment|
|PA065|30|Enhanced UC tests incremental benefit over existing treatment access; bound2020 guide. Historical feasibility context: self-efficacy d=0.43; female completers pain d=0.33; mean age68,range38–90;35%African American;29%high school or less;93%easy use;91%completed8 sessions. These are historical rationale values, not RESOLVE outcomes or power inputs.|Comparator; historical context only|
|PA066|31|Virtual coach modality initially primarily telephone; COVID shift leads to video when available/acceptable. Historical442-patient trial global assessment6month OR5.0,95%CI2.0–12.5;9month OR5.4,95%CI2.3–12.8(background only).|Intervention modality and disclosed development|
|PA067|31|End of study: last participant12month assessment and any qualitative interviews up to14months from randomization.|Final follow-up definition|
|PA068|32|Initial EHR inclusion: active in one of4systems at query/prior360days; age≥18 from EHR birthdate; English/no interpreter;≥1Essentia or≥2KP pain encounters >60days apart within360days; specified nonmalignant musculoskeletal ICD10 pain conditions.|Eligibility/population and encounter threshold|
|PA069|32|No common musculoskeletal surgery within60days; no≥2separate cancer encounters(except nonmelanoma skin) within60days; no hospice/palliative care within360days; no cognitive impairment precluding program; KPWA-only no OUD ICD10.|Eligibility exclusions/population context|
|PA070|32|Screened inclusion: high-impact chronic pain, pain most/every day in past3months and life/work limitation most/every day in past3months; persistent pain PEG≥12; ability to participate in either intervention(internet and phone access).|High-impact/persistent pain thresholds/population|

## Scope completion and limits

32/32 assigned physical pages mapped. 70 descriptive relationship keys, including administrative/background context explicitly marked; no candidate diagnoses. All result-relevant endpoints, status labels, thresholds, windows, intervention quantities, randomization specifications, and population definitions in this shard extracted. No power calculation, primary model, priors, imputation, sensitivity algorithm, multiplicity/interim boundary or stopping threshold is specified on these assigned pages; contents point to later statistical sections assigned elsewhere. Those fields are not applicable within this shard rather than absent from the whole protocol.

No scientific coverage gap remains in pages1–32. Unusable embedded glyph text is a derivative limitation, covered by original images and fresh direct-source rendering/visual reading. Main-paper global IDs remain coordinator/main-mapper merge responsibilities because other source scopes were not assigned here.

Fresh derivative completion: native and sorted-layout files21–32 are complete(12each). Fresh page images21–32 are complete(12;21 provided by coordinator,22–32 produced here). Fresh CPU OCR completed for reused images6–14and16–20(14pages) and source renders22–26(5pages); existing current OCR21 reused. OCR27 was interrupted and not used. Pages27–32 fully mapped by direct image reading; no additional OCR needed. Reused readable OCR1–5and15 and images1–20 remain unchanged.

Source wording on physical p22 was visually confirmed: the pain-interference row's brief-description cell says “pain intensity” while naming the7-item interference subscale; measurement columns in both binary subscale rows list baseline,6,12months while time-frame columns separately print Primary baseline–3months and Secondary baseline–6/12months. These exact cells are preserved without interpretation.

Additional definitions: physical p11 CI=Confidence Interval; EDA=Exploratory Data Analysis; EQ-5D-5L=EuroQoL5Dimensions–5Levels; MCID=Minimal Clinically Important Difference; BPI-SF=Brief Pain Inventory–Short Form; DSMB=Data and Safety Monitoring Board. ITT is not listed on that page. Physical p17 background defines chronic pain as ≥3months and high-impact chronic pain as ≥3months with at least one major activity restriction; this contextualizes, but does not replace, the operational screening definition on p32. Historical one-in-ten prevalence on p17–18 and typical ≥50minute weekly in-person sessions over2–3months on p18 are background, not RESOLVE intervention dose or reported trial results.
