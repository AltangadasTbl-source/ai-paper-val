# PLAN quantitative mapping: protocol PDF pages 65–96

Scope: DOC-003, joi190092supp2_prod.pdf, PDF pages65–96 inclusive; Manual of Operation and Procedures, January6,2017 version4.5, printed contents pages and pp4–32. All locations are PLAN, including historical/background data. Mapping only; no candidate diagnosis. 32/32 pages mapped. There are 46 numeric/definition relationship groups (NPM001–NPM046), no inferential S relationships. Related rows may include several printed quantities belonging to one operational rule. Cross-document matching keys are locators for later checkers, not assertions of equality.

Reusable engine: hashed Poppler layout block `.ai_paper_validation/review_1_5_1/preprocessing/protocol_pp065_096_layout.txt`; p80 is the hashed existing image `.ai_paper_validation/review_1_5_1/preprocessing/evidence_recheck_protocol_p080.png`, historical render engine unrecorded, visually opened. Fresh pages74,81,84,89,90,91,94,96: direct Poppler26.01.0 native and layout extraction returned empty, direct `pdftoppm -r 100 -f N -l N -singlefile -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6/preprocessing/protocol_middle_pN` produced readable page images; every image was opened with view_image. Tesseract5.5.0 CPU `-l eng --psm 6` produced locator text. Visual source content controls transcription; empty native records do not indicate blank pages. Derivatives have suffixes `_native.txt`, `_layout.txt`, `.png`, `_ocr.txt`. All14 fresh pages across both middle shards were handled this way. No Office source/formula/cache exists. No scientific coverage gap.

## Page coverage

| PDF page | Mapping status | Content and relationship IDs |
|---|---|---|
|65|MAPPED_NO_APPLICABLE|Contents: section/page locators, no scientific values.|
|66|MAPPED_NO_APPLICABLE|Contents continued, no scientific values.|
|67|MAPPED_NO_APPLICABLE|Contents/appendix locators, no scientific values.|
|68|MAPPED_NO_APPLICABLE|Investigator/site roster; names and affiliations.|
|69|MAPPED_NO_APPLICABLE|Personnel roster continued.|
|70|MAPPED_NO_APPLICABLE|DSMC/NEI personnel; no numeric results.|
|71|MAPPED|NPM001–NPM003 background incidence/prevalence/blindness/switch success.|
|72|MAPPED|NPM004–NPM006 planned sample, phases, outcomes.|
|73|MAPPED|NPM007–NPM010 design summary/outcome definitions.|
|74|MAPPED_FRESH_VISUAL|NPM011–NPM013 secondary outcome grades and Table1 timeline.|
|75|MAPPED|NPM014 anatomical subgroup definitions.|
|76|MAPPED|NPM015–NPM018 inclusion thresholds and treatment history.|
|77|MAPPED|NPM019–NPM022 exclusion thresholds and lab windows.|
|78|MAPPED|NPM023 site-block randomization; latent tuberculosis has no fixed skin-test cutoff.|
|79|MAPPED|NPM024 masking and identifier/site rules.|
|80|MAPPED_REUSED_VISUAL|NPM025–NPM027 primary success/control/failure definitions.|
|81|MAPPED_FRESH_VISUAL|NPM028–NPM030 lab AE table and recovery rule.|
|82|MAPPED|NPM031 dropout/non-compliance/failure denominator rules.|
|83|MAPPED|NPM032 primary endpoint flowchart.|
|84|MAPPED_FRESH_VISUAL|NPM033–NPM034 Tables4/5 dosing and reduction schedules.|
|85|MAPPED|NPM035 methotrexate dose/pill equivalents.|
|86|MAPPED|NPM036 mycophenolate dose/pill equivalents.|
|87|MAPPED|NPM037–NPM038 folate, packaging/dispensing quantities.|
|88|MAPPED|NPM039–NPM040 adherence and prednisone start/hold.|
|89|MAPPED_FRESH_VISUAL|NPM041 Table6 prednisone taper.|
|90|MAPPED_FRESH_VISUAL|NPM042 Table7 optional taper and rescue criteria.|
|91|MAPPED_FRESH_VISUAL|NPM043–NPM044 supplements/topical taper/injections.|
|92|MAPPED|NPM045 baseline/visit collection order and therapy deviations.|
|93|MAPPED|NPM045 continued masked assessments and switch before6 months.|
|94|MAPPED_FRESH_VISUAL|NPM046 visit Tables9/10.|
|95|MAPPED|NPM046 PhaseII visit clock and two-week entry interval.|
|96|MAPPED_FRESH_VISUAL|NPM046 full study form completion matrix, transcribed below.|

## Relationship inventory

All source links resolve to the supplied PDF with physical page number. Matching keys refer to main-paper domains: eligibility, participant flow, six-month primary outcome, twelve-month continuation/switch, drug dose/adherence, AE and visual acuity/quality-of-life outcomes.

| ID | Source | Printed quantitative relationship, definition, label and matching key |
|---|---|---|
|NPM001|[p71](../../../joi190092supp2_prod.pdf#page=71)|Historical incidence >50 cases/100000 person-years; prevalence approximately115/100000 persons. Distinct rate/person-time vs prevalence/person denominator. Main key background uveitis burden.|
|NPM002|[p71](../../../joi190092supp2_prod.pdf#page=71)|Up to10% of US legal blindness; approximately30000 new blindness cases/year. Historical denominators, no trial data.|
|NPM003|[p71](../../../joi190092supp2_prod.pdf#page=71)|Approximately half of methotrexate failures subsequently succeed on mycophenolate; historical narrative proportion with no printed exact numerator/denominator.|
|NPM004|[p72](../../../joi190092supp2_prod.pdf#page=72)|216 patients randomized; monthly follow-up6 months; successful patients remain same drug another6 months; failures switch and follow additional6 months or second failure. Planned patient unit, main flow and follow-up key.|
|NPM005|[p72](../../../joi190092supp2_prod.pdf#page=72)|Aim1 higher proportion with corticosteroid-sparing controlled inflammation at6 months after enrollment; secondary visual acuity, thickness, time to control, anatomical subgroup efficacy, tolerability, QOL, AEs.|
|NPM006|[p72](../../../joi190092supp2_prod.pdf#page=72)|Aim2 switched patients followed6 months from failure, same primary and secondary outcomes as Aim1; switch clock differs from original enrollment.|
|NPM007|[p73](../../../joi190092supp2_prod.pdf#page=73)|216 patients,108 per arm; site block randomization; observer-masked, patient randomization. PhaseI0–6 months, successful treatment extended to12; PhaseII second therapy after PhaseI0–6-month failure.|
|NPM008|[p73](../../../joi190092supp2_prod.pdf#page=73)|Primary success at6 months: controlled inflammation with7.5mg/day oral prednisone and ≤2drops/day topical1% prednisolone acetate. Printed wording is “with7.5”, not inequality for oral dose.|
|NPM009|[p73](../../../joi190092supp2_prod.pdf#page=73)|Secondary proportions: switch success6 months; success5 months sustained≥28days to6 months; success12 months; PhaseI6–12 success completely off corticosteroid; PhaseII6-month success. Times to control and success distinguish elapsed time vs proportions.|
|NPM010|[p73](../../../joi190092supp2_prod.pdf#page=73)|Secondary change BSCVA, macular thickness, vitreous haze clinically on Miami/former Davis and photos NEI/Miami; edema presence; intermediate/posterior/panuveitis and retinal-vasculitis subgroup efficacy; discontinuation proportions for intolerability/SAE; rate of AEs; health/vision QOL. No effect estimates printed here.|
|NPM011|[p74](../../../joi190092supp2_prod.pdf#page=74)|Additional outcomes: dose reduction, VKH efficacy; AC-cell and haze proportions starting≥2+ with2-step fall:2+→0.5+,3+→1+,4+→2+; proportions starting≥1+ reaching0 AC or0 haze; proportion with0 both; injections for severe inflammation or edema. Baseline severity denominator specified separately for each endpoint.|
|NPM012|[p74](../../../joi190092supp2_prod.pdf#page=74)|Table1: Dec2011–Sep2012 preparation; Sep2012 onward first DSMC/site certification/project start; Aug2013–Apr2017 enrollment/follow-up. Footnote SanFrancisco began Aug2013, others joined later.|
|NPM013|[p74](../../../joi190092supp2_prod.pdf#page=74)|Table1: throughNov2017 finish6-month PhaseI +1-month visit window; throughMay2018 maximum12 months +1-month window; throughNov2018 lock/analyze/publish/disseminate.|
|NPM014|[p75](../../../joi190092supp2_prod.pdf#page=75)|SUN: anterior=AC; intermediate=vitreous; posterior=retina/choroid; pan=AC+vitreous+retina/choroid without predominant site. Anterior+intermediate distinct from pan; intermediate with vasculitis not posterior; macular edema/structural complications do not determine anatomical category. Main anatomic subgroup key.|
|NPM015|[p76](../../../joi190092supp2_prod.pdf#page=76)|History eligible subtype≥1eye; active within180days:≥2+AC and/or≥2+haze and/or retinal/choroidal activity; enrollment≥1+AC and/or≥1+haze and/or active lesions in≥1eye. Bullous serous detachment qualifies with choroidal thickening.|
|NPM016|[p76](../../../joi190092supp2_prod.pdf#page=76)|At least1 indication: active after4weeks1mg/kg prednisone-equivalent; prior180day flare with≥1grade AC/haze or inactive→active lesions on taper;10mg/day oral prednisone≥90days; active after long-acting injection4weeks–180days prior.|
|NPM017|[p76](../../../joi190092supp2_prod.pdf#page=76)|Named diseases can supply indication; severeVKH examples acute active≥4weeks or bullous retinal/choroidal detachment+other inflammation. Case-by-case center approval otherwise.|
|NPM018|[p76](../../../joi190092supp2_prod.pdf#page=76)|Willing prednisone1mg/kg or60mg/day, whichever less, lower tolerated start acceptable; alcohol≤2drinks/month; contraception/abstinence.|
|NPM019|[p77](../../../joi190092supp2_prod.pdf#page=77)|Exclude immunosuppressive use other than steroids in12months; prior drug failure/intolerance; prior biologics any time; age<16; chronic IOP<5mmHg>3months both eyes; bilateral unexaminable posterior segment; better-eye acuity hand-motion or worse.|
|NPM020|[p77](../../../joi190092supp2_prod.pdf#page=77)|Exclude peri/intravitreal injection past4weeks; fluocinolone implant<3years either eye; intraocular surgery<30days or planned next180days; pregnancy testing≤4weeks before enrollment for non-postmenopausal females.|
|NPM021|[p77](../../../joi190092supp2_prod.pdf#page=77)|CBC exclusion≤2500WBC and/or≤75000platelets and/or≤9hemoglobin within4weeks; ALT/AST≥2×labULN and/or creatinine≥1.5 within4weeks. Units not printed for these exclusion values on this page; do not silently supply them.|
|NPM022|[p77](../../../joi190092supp2_prod.pdf#page=77)|Infection exclusion and minimum TB/syphilis/hepatitis tests within90days; latent TB eligible by physician judgment, no specific tuberculin cutoff in continued pp77–78.|
|NPM023|[p78](../../../joi190092supp2_prod.pdf#page=78)|Block randomization intended equal patient numbers/arm at each site. Treatment assigned after consent and eligibility; coordinator knows assigned but not future assignments.|
|NPM024|[p79](../../../joi190092supp2_prod.pdf#page=79)|Patients/coordinators unmasked; eye/VA/OCT/photo/grading masked. Five-character ID=site digit+checksum letter+3sequential digits from001; site digits1Melbourne,2Proctor,3Chicago,4Casey,5Mexico,6KKESH,7Madurai,8Coimbatore,9Pondicherry. Example4J101. Administrative ID digits are not results.|
|NPM025|[p80](../../../joi190092supp2_prod.pdf#page=80)|Success controlled in both eyes with7.5mg/day prednisone, no peri/intravitreal corticosteroid injections after first90days,≤2drops/day topical1% prednisolone at6-month visit, no failure at any point from safety/tolerability/futility. Stopping drug alone does not count failure.|
|NPM026|[p80](../../../joi190092supp2_prod.pdf#page=80)|Table2 controlled inflammation: AC≤0.5+ SUN; haze≤0.5+ NEI; no active choroid/retina inflammation or retinal vasculitis posterior to equator. CME alone insufficient active inflammation.|
|NPM027|[p80](../../../joi190092supp2_prod.pdf#page=80)|Futility may be declared anytime for persistent unresponsive inflammation; early flare not inherently failure because drugs take months. At6months fail if no controlled inflammation with7.5mg/day and≤2drops1%. Intolerance dose reduction encouraged if willing.|
|NPM028|[p81](../../../joi190092supp2_prod.pdf#page=81)|Non-serious abnormality stop medication; allow28days recovery; repeat labs1–2weeks; resume if below threshold within28days at protocol/reduced dose. Persistence at/above non-serious threshold28days becomesSAE and immediate failure; infection unresolved28days SAE.|
|NPM029|[p81](../../../joi190092supp2_prod.pdf#page=81)|Table3 non-serious vs serious: leukocytes>1000 to<2500/μL vs≤1000/μL; platelets20000–75000/μL vs<20000/μL; hemoglobin≥6.5 to<9g/dL vs<6.5g/dL. Printed Table3 footnote non-serious lab persists28days→SAE/failure.|
|NPM030|[p81](../../../joi190092supp2_prod.pdf#page=81)|Table3 AST/ALT2 to<5×ULN vs≥5×ULN; creatinine≥1.5 to<2mg/dL vs≥2mg/dL. Medical Monitor determines non-lab SAE relation and switch safety; unsafe switch treated clinically but followed6months both phases.|
|NPM031|[p82](../../../joi190092supp2_prod.pdf#page=82)|Dropout=declines all further visits or deceased; drug-related death failure, unrelated death dropout perMonitor. Drug stopping for other reason/missed unresponsive visits are non-compliance, not dropout; seek6-month endpoint even off drug/early failure both phases.|
|NPM032|[p83](../../../joi190092supp2_prod.pdf#page=83)|Flowchart: monthly efficacy/tolerability/safety, steroid taper;6months control “with7.5mg” oral and≤2drops; success→PhaseI6–12,12-month threshold≤7.5mg; failure→alternate drug,6months later threshold≤7.5mg. AC/haze≤0.5+,no active retina/choroid; drops1%prednisolone-equivalent. Two reductions shown, intolerance persisting→switch.|
|NPM033|[p84](../../../joi190092supp2_prod.pdf#page=84)|Table4 weekly grid days1–7: weeks1/2 MTX7.5mgBID onday1 only;MMF500mgBID eachday;folate1mgdaily. Afterweek2 MTX12.5mgBID onday1 only;MMF1.5gBID daily;folate1mgdaily. BID MTX here refers split dose on one weekly day, not every day.|
|NPM034|[p84](../../../joi190092supp2_prod.pdf#page=84)|Table5 reductionI MTX10mgBID onday1, MMF1gBID daily;II MTX7.5mgBID onday1,MMF500mgBID daily. Reduce only for intolerability/safety; if none stay maintenance. Folate remains1mgdaily even reducedMTX.|
|NPM035|[p85](../../../joi190092supp2_prod.pdf#page=85)|MTX first2weeks15mg/week=7.5mgBID onceweek=3pills AM+3PM;start within6days enrollment;maintenance25mg/week=12.5BID=5+5pills weekly. Reductions20mg/week=10BID=4+4pills;15mg/week=7.5BID=3+3. Dose reduction optional before intolerance failure.|
|NPM036|[p86](../../../joi190092supp2_prod.pdf#page=86)|MMF empty stomach no food1hour before/after;first2weeks500mgBID=1pillAM+1PM;after2weeks1.5gBID=3+3pills. Reductions1gBID=2+2pills,500mgBID=1+1pills;failure intolerance still seek6-month data both phases.|
|NPM037|[p87](../../../joi190092supp2_prod.pdf#page=87)|Folate1mg/day allMTX, permitted MTX day. Initial14day supply MTX12pills/MMF28pills. Maintenance30day+buffer bottles MTX50pills,MMF100pills/bottle.|
|NPM038|[p87](../../../joi190092supp2_prod.pdf#page=87)|Baseline initial14days plus1maintenance bottle:MMF100 orMTX50. Monthly throughmonth5 additional30days:MTX50 orMMF200pills. PhaseII same; PhaseI6–12 success dispense120days at6-month visit. Additional supplies allowed beyond scheduling window. Distinguish bottle count vs monthly pills.|
|NPM039|[p88](../../../joi190092supp2_prod.pdf#page=88)|Adherence monthly calendars and returned-bottle pill counts; omit newly started bottle, example2week+2day visit. MissedMTX may take nextday,otherwisewaitnextweek preserving originalweeklyday;MMF regularnextdose.|
|NPM040|[p88](../../../joi190092supp2_prod.pdf#page=88)|Prednisone1mg/kg or60mgdaily lesser,2–4weeks initially; taper/hold7.5mg/day first6months, further reduction allowedafter6months. PhaseII efficacyfailure restart same regimen.|
|NPM041|[p89](../../../joi190092supp2_prod.pdf#page=89)|Table6 oral dose mg/day:60 duration2–4weeks decrement10;50 duration1 decrement10;40,35,30,25 duration1 decrement5;20,17.5,15,12.5,10 duration1 decrement2.5;7.5 hold toend6months. Medications6–8weeks full effect, flare first3months possible. Faster taper/under7.5 permitted if absolutely medically necessary. Optional6–12 taper, not mandatory0mgby12months. No improvement first4weeks consider supplemental treatment.|
|NPM042|[p90](../../../joi190092supp2_prod.pdf#page=90)|Table7 optional6–12:7.5mg1week decrement2.5; <7.5 &≥5 duration2–4weeks decrement1–2.5; <5 &≥2.5 duration2–4 decrement1.5–2.5; <2.5 &≥1 duration2–4 decrement1;then0. Hold7.5≥1week on entering6–12. Mildreactivation up to1+;severe≥2+AC/haze; severe rescue up to1mg/kg,mild up to2×flare dose. Non-responseafter4weeks1mg/kg holdadditional1week then considerfailure; seek6-month visits bothphases.|
|NPM043|[p91](../../../joi190092supp2_prod.pdf#page=91)|Calcium500mg3×daily;vitaminD400–800IUdaily. Topical≤2drops/day1%prednisolone or equivalent sufficient success;>2times/day failure. Table8 taper:1drop8–10times/day1–2weeks;6/day1week;4/day1;3/day1;2/day1;1/day1;none.|
|NPM044|[p91](../../../joi190092supp2_prod.pdf#page=91)|One periocular triamcinolone40mg orintravitreal4mg permitted persistent edema first90days ofeachphase. Any injection solelyforinflammation orany injection after90days→deviation form. Main injection eligibility/outcome key.|
|NPM045|[p92](../../../joi190092supp2_prod.pdf#page=92) [p93](../../../joi190092supp2_prod.pdf#page=93)|AdditionalIVtherapy/immunosuppressives/surgery prohibited unlessdeviation. VA/frontsegment/IOP beforedilation;postsegment/OCT/photo/labsafter. SF36all;NEIVFQ25all;INDVFQIndiaonly. Failurefirst6months switches, assignedphasevisitclock restarts; data doubleentered REDCap.|
|NPM046|[p94](../../../joi190092supp2_prod.pdf#page=94) [p95](../../../joi190092supp2_prod.pdf#page=95) [p96](../../../joi190092supp2_prod.pdf#page=96)|Tables9/10 and full forms matrix below. Success6months extendsanother6;baselineassessment≤14daysbeforeenrollment,lab4weeks/90days;≥2weeksbetweenvisits. PhaseI/II:week2±3days;months1–5±15days;month6−15to+30days. PhaseI9±15days,12−15to+30. PhaseII startswithin2weeks/14days failure,day1=BaselineII,possiblysameaslastPhaseIvisit;clockfixedtoBaselineII. PhaseII followed6months orsecondfailure; stillseek6-month data.|

## Full Table: study form completion schedule (PDF p96, printed p32)

Column order: I baseline; I week2; I months1–5,9; I failure anytime; I months6,12; II baseline; II week2; II months1–5; II failure anytime; II month6. `X` scheduled, `(x)` if applicable, dash unmarked. This preserves all rows and denominator/timepoint locators.

| Form | I-B | I-W2 | I-M1–5,9 | I-F | I-M6,12 | II-B | II-W2 | II-M1–5 | II-F | II-M6 |
|---|---|---|---|---|---|---|---|---|---|---|
|Eligibility/screening|X|-|-|-|-|-|-|-|-|-|
|Consent|X|-|-|-|-|-|-|-|-|-|
|Baseline history|X|-|-|-|-|-|-|-|-|-|
|Clinical eye exam|X|-|X|X|X|-|-|X|X|X|
|Secondary clinical eye exam|X|-|-|X|X|-|-|-|X|X|
|Visual acuity|X|-|X|(x)|X|-|-|X|(x)|X|
|OCT|X|-|X|(x)|X|-|-|X|(x)|X|
|Fundus|X|-|-|(x)|X|-|-|-|(x)|X|
|Laboratory|X|X|X|(x)|X|-|X|X|(x)|X|
|AE checklist|-|X|X|X|X|X|X|X|X|X|
|Vision QOL|X|-|-|X|X|-|-|-|X|X|
|Health QOL|X|-|-|X|X|-|-|-|X|X|
|Treatment assessment|X|X|X|X|X|X|X|X|X|X|
|Patient calendar|-|X|X|X|X|-|X|X|X|X|
|Medication log|X|X|X|X|X|X|X|X|X|X|
|Dropout|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|
|Protocol deviation|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|
|AE narrative|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|
|AE log|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|(x)|

Footnotes: failure may occur atscheduled/non-studyvisit; all(x) onlyifapplicable; BaselineII formifnot switching same day asPhaseIfailure; patientscompletecalendars andbringforreview. Blank II-baseline cells reflect the printed matrix, without inferring that same-day measurements were omitted.
