# Numeric and reporting relationship inventory: protocol/results

Extraction inventory only. Scope DOC-002 PLAN pp1–35 and DOC-005 REPORT pp1–16. N201–N240: 40 numeric/reporting relationships, each a coherent group whose full rows/values/units are retained in extraction/parts/protocol_results.md. Statistical row identities reside in statistics/parts/protocol_results.md. Keys below are matching fields for the main-paper mapper's evidence, not claims that a mismatch exists. Source locators use PDF page numbering. No workbook formulas or cached values apply.

| ID | Source role/location | Quantitative group and denominator/unit identity | Main-paper matching key |
|---|---|---|---|
| N201 | DOC-002 PLAN pp4,7,20 | Primary physiologic BPD or death by36w PMA; all randomized; intervention lower incidence hypothesis | Primary endpoint/composite/36w PMA/ITT |
| N202 | DOC-002 PLAN pp4,16 | Eligible22 0/7–28 6/7w OR401–1000g, surfactant clinical decision, detailed exclusions | Eligibility/randomized population |
| N203 | DOC-002 PLAN pp4,16–17 | Randomization≤48h, first dose≤50h(+2hgrace); maternal indomethacin24h and infant prohibition7days after last dose | Enrollment/treatment window |
| N204 | DOC-002 PLAN pp4,17–18 | 1:1 individual/multiple birth allocation; NICU×GA<26/≥26w; block urn; randomized upon kit opening;2kits/4respules perID | Randomization/strata/unit/flow |
| N205 | DOC-002 PLAN pp5,7,20–21 | Eight secondary outcomes and timepoints:36w mortality,BPD,severity,grade3,steroids;22–26moNDI,mortality,composite | Secondary endpoint hierarchy |
| N206 | DOC-002 PLAN pp7,21 | Jensen severity noBPD/grade1≤2L/min/grade2>2L/min or noninvasive pressure/grade3 invasive; provisional NDI cognitive<70/GMFCS3–5/hearing/vision | BPDseverity ordinal/category labels |
| N207 | DOC-002 PLAN pp5,21–23 | Exploratory NIH severity36w; invasive ventilation days28/36w;intubation after50h to28d/36w;repeat surfactant after50h to7daysPLD;wheeze/cough22–26mo | Exploratory endpoint status/time |
| N208 | DOC-002 PLAN pp5,22–23 | SafetyAE7d/168h,SIP/PVL30d/720h;ICH3d ultrasound grace;growth36w;moderate+ orunexpected mild | Safety windows/AE vs GDB |
| N209 | DOC-002 PLAN pp4,18–19 | Curosurf2.5mL/kgdose1,1.25dose2;each budesonide .25mg/kg=1mL/kg;1–2doses;last≤50h | Randomized dose/duration |
| N210 | DOC-002 PLAN p19 | Suggested initialFiO2>.25,SpO2>90%,PaCO2>65torr;repeatMAP>6cmH2O,FiO2>.30,<48h | Exposure/clinical dose criteria |
| N211 | DOC-002 PLAN p20 | Steroids<7days discouraged;fluid20mL/kg/<2h;dopamine≥10mcg/kg/min;indomethacin prohibited7dPLD | Steroid outcome/violations |
| N212 | DOC-002 PLAN p23 | Follow-up22–26mo;potential5–6y;no mandated samples or posthospital procedures | Deferred follow-up status |
| N213 | DOC-002 PLAN p25 | Primary robust Poisson sandwich, fixedNICU/GA, allowed NICUpooling samecenter | Primary model/covariates |
| N214 | DOC-002 PLAN pp7,25 | Primary/secondaryITT; safetyasreceived; prespecifiedasreceivedsecondary | Analysis population/sensitivity |
| N215 | DOC-002 PLAN p25 | Continuouslinear,binaryrobustPoisson,countPoisson,ordinalproportionalodds,nominalgeneralizedlogits;fixedstrata | Outcome model families |
| N216 | DOC-002 PLAN p25 | Missingness/lossapproach delegatedtoSAPbeforeunmaskedreview;secondarycomparisonsdescriptive | Missing data/multiplicity |
| N217 | DOC-002 PLAN pp25–26 | Baseline .58 to .48,10percentagepoint reduction;24%death+45%survivorBPD;secondary descriptive;90%power/.05overall/.044final | Sample-size inputs |
| N218 | DOC-002 PLAN p26Table5 | Perarm406/539/664 at80/90/95%power(.05overall,.044final);593/753/900(.01,.009);539×2=1078;simulation550×2=1100;5%attritiontarget1160 | Sample-size target/simulation |
| N219 | DOC-002 PLAN p26 | 2000/year×.90×.70=1260eligible;33%consent415/year;1160/415=2.8y;1+2.8+2=5–6y | Recruitment background; no primary result join |
| N220 | DOC-002 PLAN pp27–28 | AE/SAEdefinitions;expectedtransientmildexcluded,baselineworsened/recurredincluded;24h/72hsite reports/7calendar-dayFDA | Safety recording definition |
| N221 | DOC-002 PLAN pp28–29 | Safetyfirst40/~3%,then25/50/75%;Pocockspendingcutoffs .0033/.0196/.0212/.0214;actualinformationdependent | DSMC safety decision |
| N222 | DOC-002 PLAN p29 | Safety robustPoissonfixedsite/GA;maypoolor site-randomGLMM early15centers | Interim safety model |
| N223 | DOC-002 PLAN p29 | Efficacy25/50/75%;O'Brien-Flemingspending .000015/.0030/.0183;final.0440;overall.05 | Interim efficacy/multiplicity |
| N224 | DOC-002 PLAN p29 | Futilityupper80%conditionalpowerCI≤.50 at50% or≤.30 at75%;pooraccrual discretion | Conditional-power stopping rule |
| N225 | DOC-005 REPORT p2eTable1 | ITT641/treated635/SAF635/PP617;randomized323/318,treatedrandomized320/315,SAF322/313,PP309/308;allstatuscounts/percentages in appendix | Figure1/populations/withdrawals |
| N226 | DOC-005 REPORT pp3–4eTable2 | SAF322/313,one220/195,two102/118;doseageh/allmeanSDmedianquartileminmax;compliance%relativeexpectedvolume;90–110%compliant;componentdoses | Doseexposure/safety/asreceived |
| N227 | DOC-005 REPORT pp5–6eTable3 | SAF322/313,participantAE/SAEcountspercent,everyRR/CI/testrow;missingnonuniformdenominators not silently fixed to headers | Safetyexperience/mainAEsummary |
| N228 | DOC-005 REPORT pp7–8eTable4 | ClinicalGDB≤120dPNA,n/Nnonmissing;growth36w;allclinical/compositecounts/effects andzmeans;clinicaldeath120d,growthdeath36w | Safetyclinical/growth/tableoutcomes |
| N229 | DOC-005 REPORT pp9–10eTable5 | ITT323/318;any69/51,major11/7;allviolationcategorycounts%;nonexclusive;majorPPexclusion;consent/ineligiblefootnotes | Flow/PPanalysis/consentwithdrawals |
| N230 | DOC-005 REPORT pp11–12eTable6 | AEevents500/403;interest468/366,unexpected83/65;allcategory/severity/relationship/action/resolutioncounts;headersparticipant322/313 | Eventburden vs participant counts |
| N231 | DOC-005 REPORT pp13–14eTable7 | SAEevents90/80;interest70/59,unexpected27/24;allcategory/severity/relationship/action/outcomes;participantheaders322/313 | SAEburden vs participant counts |
| N232 | DOC-005 REPORT pp15–16eTable8 | Deathby120d50/321vs44/313,by36w48/321vs41/313,7dPLD18/321vs21/313;fatalSAE22/321vs25/313;allages/causecounts | Allcausehospitalmortality/window |
| N233 | DOC-002 PLAN pp7–8 | Historical epidemiology/NRN/preclinical numeric rationale retained fully | No BiB result join; contextual background |
| N234 | DOC-002 PLAN p9 | Prior PK/lamb/cytokine numeric relationships andunits retained | No BiB result join; contextual background |
| N235 | DOC-002 PLAN p10 | Prior pilot/largerRCT/meta-analysis n,counts,RR/OR/CI,NNT/NDI retained | No BiB result join; contextual background |
| N236 | DOC-002 PLAN p11Table1 | Historical cohort294/173demographics/full14descriptiverows withPvalues | No BiB result join; contextual background |
| N237 | DOC-002 PLAN p12Table2 | Historicalday7/36wrespiratory/full22outcomerowswithPvalues | No BiB result join; contextual background |
| N238 | DOC-002 PLAN p13Tables3–4 | Historical16morbidity+16discharge/growthrowswithPvalues | No BiB result join; contextual background |
| N239 | DOC-002 PLAN p14 | Prior dosefinding/systemicsteroid/safety numeric rationale | No BiB result join; contextual background |
| N240 | DOC-002 PLAN p24 | Priorinhaledbudesonide7RR/CI/Ptriples,doseanddurationformula | No BiB result join; contextual background |

Truthful direct source filenames: DOC-002 joi250072supp1_prod_1761000786.68881.pdf; DOC-005 joi250072supp4_prod_1761000786.6988.pdf. The extraction artifact links each results page and key protocol pages with #page=N; numeric locations above name exact PDF page and table. Multiple tables on protocol p13 distinguish Table3 from Table4. No quantitative group is registered as a finding.
