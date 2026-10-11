# DOC-003 quantitative and design map: physical pages 65–96

- Scope: every physical page 65–96 of `joi190092supp2_prod.pdf`, 32 unique pages.
- Document role: PLAN throughout; prospective Manual of Operation and Procedures (MOP), January 6, 2017, version 4.5. Printed MOP pages equal physical page minus 64.
- Runtime agent: `01a12954-dbd4-7d10-a3f7-3d4599c0b038`; fresh support mapping shard, medium effort.
- Inputs: normative scope and 1.6.2 review contract; current source coverage, source inventory, evidence-asset inventory and tooling record; reusable `review_1_5_1/preprocessing/protocol_pp065_096_layout.txt`; `review_1_6_1/preprocessing/protocol_b/page-N-ocr.txt` and `page-N.png` for N=74,80,81,84,89,90,91,94,96.
- All nine OCR-dependent PNG pages were opened and inspected visually. Native layout source supplies the remaining 23 pages. No fresh-required source units; no new OCR or rendering. Native reusable extraction engine: Poppler pdftotext layout, legacy version not established. OCR/raster legacy engine versions unrecorded. Compute device CPU.
- No workbook, cached values or cell formulas in this scope. No reported treatment-result estimates, intervals, P values, sample-size formula/power assumptions, interim or multiplicity rule in these pages. Planned sample size and outcome definitions are mapped below; absent items are not inferred from other sources.
- Relationship identifiers below are shard-local, for coordinator normalization; semantic main-paper keys indicate matching subjects, without inferring findings. No candidate decisions made.

## Complete page coverage

| Physical PDF page | Printed MOP page | Content mapped | Evidence route | Status |
|---:|---:|---|---|---|
| 65 | unnumbered contents | Contents primary endpoint, treatment plan, visits; no applicable numeric outcome or inferential relationship | reusable layout | COMPLETE |
| 66 | unnumbered contents | Contents examinations, AE, data management; no applicable result relationship | reusable layout | COMPLETE |
| 67 | unnumbered contents | Contents organization and appendices; no applicable result relationship | reusable layout | COMPLETE |
| 68 | 4 | Investigator/site roster; administrative, no applicable quantitative relationship | reusable layout | COMPLETE |
| 69 | 5 | Personnel roster; administrative, no applicable quantitative relationship | reusable layout | COMPLETE |
| 70 | 6 | DSMC and NEI personnel; administrative, no applicable quantitative relationship | reusable layout | COMPLETE |
| 71 | 7 | Historical incidence/prevalence/blindness numbers; background only, not trial inputs or results | reusable layout | COMPLETE |
| 72 | 8 | 216 patients; 6-month primary; switch and follow-up; aims and secondary measures | reusable layout | COMPLETE |
| 73 | 9 | Design, 108/arm; primary endpoint and all initial secondary endpoints | reusable layout | COMPLETE |
| 74 | 10 | Remaining secondary endpoints and timeline Table 1 | OCR plus visually inspected PNG | COMPLETE |
| 75 | 11 | SUN anatomical population definitions/table | reusable layout | COMPLETE |
| 76 | 12 | All inclusion thresholds and qualifying treatment/history windows | reusable layout | COMPLETE |
| 77 | 13 | All exclusion thresholds, laboratory/infectious screening windows, TB eligibility | reusable layout | COMPLETE |
| 78 | 14 | Site-block randomization and allocation concealment | reusable layout | COMPLETE |
| 79 | 15 | Observer masking; patient/coordinator unmasking; IDs | reusable layout | COMPLETE |
| 80 | 16 | Primary success, Table 2 inflammation, efficacy and intolerability failure | OCR plus visually inspected PNG | COMPLETE |
| 81 | 17 | Safety failure rules and Table 3 thresholds | OCR plus visually inspected PNG | COMPLETE |
| 82 | 18 | Dropout/death/noncompliance and continued outcome follow-up | reusable layout | COMPLETE |
| 83 | 19 | Full primary endpoint flowchart and footnotes | reusable layout | COMPLETE |
| 84 | 20 | Weekly dose Table 4, reduction Table 5 and footnotes | OCR plus visually inspected PNG | COMPLETE |
| 85 | 21 | MTX introductory/maintenance and reduction schedules | reusable layout | COMPLETE |
| 86 | 22 | MMF introductory/maintenance/reduction; 6-month follow-up | reusable layout | COMPLETE |
| 87 | 23 | Folic acid, PPI allowance, packaging/exposure quantities | reusable layout | COMPLETE |
| 88 | 24 | Adherence/missed doses; prednisone start and endpoint target | reusable layout | COMPLETE |
| 89 | 25 | Prednisone initial/Phase II/taper rules and Table 6 | OCR plus visually inspected PNG | COMPLETE |
| 90 | 26 | Optional taper Table 7; rescue/nonresponse/failure/follow-up | OCR plus visually inspected PNG | COMPLETE |
| 91 | 27 | Supplements, topical endpoint/Table 8; injections and windows | OCR plus visually inspected PNG | COMPLETE |
| 92 | 28 | Adjunctive therapy restrictions and baseline/study procedure order | reusable layout | COMPLETE |
| 93 | 29 | Outcome instruments, double entry and initial follow-up/switch rules | reusable layout | COMPLETE |
| 94 | 30 | Phase I/II duration and visit-window Tables 9–10 | OCR plus visually inspected PNG | COMPLETE |
| 95 | 31 | Phase II baseline/entry timing and non-study failure visits | reusable layout | COMPLETE |
| 96 | 32 | Complete study form completion matrix and footnotes | OCR plus visually inspected PNG | COMPLETE |

## Quantitative and statistical-design relationships

### S-P065-001 — trial size, randomization and duration

Locations: [p.72](../../../../joi190092supp2_prod.pdf#page=72), [p.73](../../../../joi190092supp2_prod.pdf#page=73), [p.78](../../../../joi190092supp2_prod.pdf#page=78), [p.79](../../../../joi190092supp2_prod.pdf#page=79). PLAN. Target 216 patients, 108 per arm (108+108=216), oral methotrexate versus oral mycophenolate mofetil. Randomized comparative-effectiveness, observer-masked, block randomization by site; lists generated by biostatistician, REDCap randomization after consent and eligibility. Coordinators cannot see future assignment. Patients and coordinators unmasked after enrollment; ophthalmologists, visual acuity examiners/refractionists, OCT operators, fundus photographers and graders masked. After any staff unmasking a protocol-deviation form is required and patient continues in trial (p.80). Initial Phase I monthly follow-up 6 months or failure. Six-month successes continue same treatment to 12 months; initial failures switch to alternative and receive another 6 months or until second failure. Matching keys: randomized population, allocation ratio, stratification/site, observer masking, first-line and crossover duration. No power inputs or calculation here.

### S-P065-002 — primary outcome status and definition

Locations: [p.72](../../../../joi190092supp2_prod.pdf#page=72), [p.73](../../../../joi190092supp2_prod.pdf#page=73), [p.80](../../../../joi190092supp2_prod.pdf#page=80), [p.83](../../../../joi190092supp2_prod.pdf#page=83). PLAN. Specific Aim 1 primary: proportion achieving corticosteroid-sparing control/treatment success at 6 months after enrollment. P.80 definition requires controlled ocular inflammation in BOTH eyes, prednisone 7.5 mg/day, topical 1% prednisolone acetate ≤2 drops/day at the 6-month visit, no periocular/intravitreal corticosteroid injections after first 90 days, and no prior treatment failure due to safety, tolerability or futility. Stopping medication at any time does not itself count as failure. Table 2: anterior chamber cells ≤0.5+ (SUN); vitreous haze ≤0.5+ (NEI); choroid/retina no active inflammation or retinal vasculitis posterior to equator. Cystoid macular edema is insufficient by itself to constitute active inflammation. P.83 flowchart: 6-month Phase I prednisone 7.5 mg; 12-month Phase I and 6-month Phase II prednisone ≤7.5 mg; ≤2 drops/day in all three outcome assessments. Flowchart controlled inflammation footnote: chamber cells and haze ≤0.5+, no active choroid/retina lesions; drops refer to prednisolone acetate 1% or equivalent. Matching keys: treatment-success composite components, both-eye unit, 6-month assessment, prednisone/drop thresholds and injection window.

### S-P065-003 — complete secondary outcome status inventory

Locations: [p.72](../../../../joi190092supp2_prod.pdf#page=72), [p.73](../../../../joi190092supp2_prod.pdf#page=73), [p.74](../../../../joi190092supp2_prod.pdf#page=74). PLAN. Aim 2 evaluates switching after initial failure using same primary/secondary outcomes six months from failure. Under explicit Secondary outcomes heading: corticosteroid-sparing success at 6 months after switching (Aim 2); time to inflammation control; time to treatment success; success at 5 months sustained at least 28 days to 6 months; Phase I success at 12 months; Phase I 6–12-month success with complete corticosteroid discontinuation; Phase II success at 6 months; change BSCVA; presence of macular edema; change macular thickness; change clinical vitreous haze Miami/formerly Davis; change photographic haze NEI and Miami/formerly Davis; efficacy intermediate/posterior/panuveitis subgroups; efficacy retinal vasculitis; proportion discontinuing due to intolerability; rate adverse events; proportion discontinuing due to SAEs; health-related and vision-related quality of life. Continued p.74: dose reduction; efficacy VKH; proportions initially ≥2+ chamber cells or haze achieving 2-step decrease (2+ to 0.5+, 3+ to 1+, 4+ to 2+); proportions initially ≥1+ chamber cells or haze reaching 0; proportion controlled with 0 haze AND 0 chamber cells; proportion requiring injections for severe inflammation; proportion requiring injections for macular edema. Matching keys: all reported secondary outcomes, subgroup prespecification and endpoint statuses. No hierarchy or multiplicity adjustment stated on these pages.

### N-P065-001 — plan timeline/background, contextual quantities

Locations: [p.71](../../../../joi190092supp2_prod.pdf#page=71), [p.74](../../../../joi190092supp2_prod.pdf#page=74). PLAN. Background incidence >50/100,000 person-years, prevalence approximately 115/100,000 persons, up to 10% legal blindness or approximately 30,000 new blindness cases/year; approximately half failing MTX subsequently successful with MMF. These are cited historical background, not reported trial outcomes or sample-size inputs. Table 1 calendar: pre-study Dec 2011–Sep 2012; DSMC/certification Sep 2012 onward; enrollment/follow-up Aug 2013–Apr 2017; Phase I 6-month+1-month window finish Nov 2017; maximum 12-month+1-month window finish May 2018; database lock/analyze/publish Nov 2018. Footnote San Francisco began Aug 2013, other sites afterward. Matching keys: follow-up duration/windows; administrative calendar preserved without upgrading its scientific relevance.

### S-P065-004 — anatomical eligibility and inflammation history

Locations: [p.75](../../../../joi190092supp2_prod.pdf#page=75), [p.76](../../../../joi190092supp2_prod.pdf#page=76). PLAN. At any time since diagnosis, intermediate, anterior-and-intermediate, posterior or panuveitis SUN criteria required. Anatomic table: anterior=anterior chamber (iritis, iridocyclitis, anterior cyclitis); intermediate=vitreous (pars planitis, posterior cyclitis, hyalitis); posterior=retina/choroid (focal/multifocal/diffuse choroiditis, chorioretinitis, retinochoroiditis, retinitis, neuroretinitis); panuveitis=chamber+vitreous+retina/choroid without predominant site. Intermediate retinal vasculitis remains intermediate with vasculitis. Inclusion: noninfectious eligible location in ≥1 eye; active in last 180 days with ≥2+ chamber cells and/or ≥2+ NEI haze and/or active retinal/choroidal inflammation; at enrollment ≥1+ cells and/or ≥1+ haze and/or active retinal/choroidal inflammation (bullous serous retinal detachment qualifies with choroidal thickening). Matching keys: analysis population, anatomical subgroups and baseline activity thresholds.

### S-P065-005 — qualifying indication and other inclusion criteria

Location: [p.76](../../../../joi190092supp2_prod.pdf#page=76). PLAN. At least one: active after 4 weeks 1 mg/kg prednisone-equivalent; recurrence after taper within prior 180 days (≥1-grade rise cells/haze or inactive→active retina/choroid); oral prednisone 10 mg/day or equivalent ≥90 days before enrollment; active after long-acting injection 4–180 days earlier; specified indication (Behcet posterior, multifocal choroiditis+panuveitis, serpiginous, birdshot, diffuse retinal vasculitis, severe VKH including active ≥4 weeks or bullous detachments plus ocular activity, sympathetic ophthalmia); or case-by-case coordinating-center approval. Willingness prednisone 1 mg/kg or 60 mg/day whichever less, lower start permitted for known intolerance; alcohol ≤2 drinks/month; contraception or abstinence. Matching keys: eligible corticosteroid-sparing population and randomized co-intervention.

### S-P065-006 — exclusion thresholds and screening windows

Location: [p.77](../../../../joi190092supp2_prod.pdf#page=77) and TB continuation [p.78](../../../../joi190092supp2_prod.pdf#page=78). PLAN. Any one excludes: infectious uveitis; noncorticosteroid immunosuppression past 12 months; previous MTX/MMF intolerance/safety issues or failure to control ocular/other inflammation; any previous biologic; age <16 years; inability to examine posterior segment in both eyes; bilateral IOP <5 mm Hg for >3 months; periocular/intravitreal steroid past 4 weeks; fluocinolone implant either eye <3 years; intraocular surgery <30 days or planned next 180 days; better-eye BSCVA hand motion or worse; pregnancy/breastfeeding/planning conception, pregnancy testing within 4 weeks except postmenopause; cancer except inactive nonmelanoma skin cancer; autoimmune/other ocular condition anticipated to dictate treatment. CBC within 4 weeks: WBC ≤2500, platelets ≤75000, hemoglobin ≤9. ALT/AST ≥2× laboratory ULN and/or creatinine ≥1.5 within 4 weeks. Active TB/HIV/syphilis/hepatitis B/C; required infection tests within 90 days; latent TB eligible, no particular tuberculin cut-off. Matching keys: trial population exclusions and safety screening.

### S-P065-007 — efficacy/futility and intolerance failure

Locations: [p.80](../../../../joi190092supp2_prod.pdf#page=80), [p.81](../../../../joi190092supp2_prod.pdf#page=81), [p.83](../../../../joi190092supp2_prod.pdf#page=83). PLAN. Futility may be declared anytime for persistent uncontrolled inflammation deemed nonresponsive and completely unlikely to control with continued study drug. Early increase does not automatically imply failure; corticosteroids may increase. At 6 months lack of controlled inflammation with prednisone 7.5 mg/day and ≤2 prednisolone acetate 1% drops/day declares failure and Phase II. Intolerability: severe attributed symptoms, patient unable and unwilling to continue; reduction strongly encouraged but NOT required. Flowchart supplies separate SAE, futility and intolerability pathways; optional reduction levels I/II, persistent intolerance→alternate drug Phase II. Matching keys: failure composite/reasons, withdrawal versus failure, crossover eligibility.

### S-P065-008 — safety failure and full laboratory threshold table

Location: [p.81](../../../../joi190092supp2_prod.pdf#page=81), continuation [p.82](../../../../joi190092supp2_prod.pdf#page=82). PLAN. At nonserious lab threshold stop drug immediately; allow 28 days to regain eligibility, recommend retest after 1–2 weeks; if below threshold within 28 days resume same/reduced protocol dose at investigator discretion. At/above nonserious threshold for 28 days becomes SAE and immediate treatment failure; no Phase II switch for this persistent abnormality, collect 6-month data/imaging if before endpoint. Other nonserious events can pause drug; unresolved infection after 28 days becomes SAE. Table 3: leukocytes nonserious >1000 to <2500/µL, serious ≤1000/µL; platelets nonserious 20000–75000/µL, serious <20000/µL; hemoglobin nonserious ≥6.5 to <9 g/dL, serious <6.5 g/dL; AST/ALT nonserious 2 to <5×ULN, serious ≥5×ULN; creatinine nonserious ≥1.5 to <2 mg/dL, serious ≥2 mg/dL. Footnote any nonserious lab abnormality unresolved 28 days becomes SAE and safety failure. For nonlaboratory SAE, Medical Monitor must judge relatedness before failure declaration and whether safe to switch to Phase II; unsafe→best judgment and 6-month follow-up. Investigator may stop medication immediately and collect failure assessments pending monitor decision, but official assessment form/failure waits. Matching keys: AE/SAE definition, laboratory thresholds, safety-failure population.

### S-P065-009 — dropout, noncompliance and missing outcome collection

Location: [p.82](../../../../joi190092supp2_prod.pdf#page=82). PLAN. Dropout only declared no interest/unwilling to attend any more visits, or deceased; no additional data for unwilling attendees. Drug-related death counts failure; unrelated death dropout, Medical Monitor discretion. Stopping treatment for other reasons (e.g. fear), missed visits/no response, nonserious AE or medication discontinuation do not themselves mean dropout if follow-up remains possible. Encourage subsequent visits especially Phase I/II 6-month outcome, regardless of medication. Every effort for 6-month follow-up after early treatment failure, including crossover patients. Matching keys: excluded/withdrawn/noncompliant denominators, missing outcome ascertainment and failure count. No imputation algorithm here.

### S-P065-010 — randomized dose tables and intervention exposure

Locations: [p.84](../../../../joi190092supp2_prod.pdf#page=84), [p.85](../../../../joi190092supp2_prod.pdf#page=85), [p.86](../../../../joi190092supp2_prod.pdf#page=86), [p.87](../../../../joi190092supp2_prod.pdf#page=87). PLAN. Table 4 initial weeks 1–2: MTX 7.5 mg BID on day 1 ONLY=15 mg/week; MMF 500 mg BID days 1–7=1 g/day; folic acid MTX only 1 mg daily. After week 2: MTX 12.5 mg BID day 1 ONLY=25 mg/week; MMF 1.5 g BID every day=3 g/day; folic acid unchanged. Table 5 reduction I MTX 10 mg BID one day/week=20 mg/week, MMF 1 g BID daily=2 g/day; reduction II MTX 7.5 mg BID one day/week=15 mg/week, MMF 500 mg BID daily=1 g/day. Footnote reduce for intolerable effects/safety only, otherwise maintenance throughout; MTX folic acid remains 1 mg daily despite reduction. MTX with food, begin convenient weekday within 6 days of enrollment; introductory 3 pills morning+3 evening once weekly, maintenance 5+5, reductions 4+4 then 3+3 (2.5 mg/pill implied by stated dose/pill correspondence). MMF empty stomach no food 1 hour before/after each dose, intro 1+1 pills/day, maintenance 3+3, reductions 2+2 then 1+1 (500 mg/pill). Cannot escalate at 2 weeks and unwilling to continue→intolerance failure, possible Phase II. Reduction optional, resume maintenance when resolved at investigator discretion. All failures followed to sixth-month assessment. PPI allowed though H2 preferred. Matching keys: randomized drug dose/duration, titration, reductions, ancillary folate.

### N-P065-002 — packaging and adherence measurements

Locations: [p.87](../../../../joi190092supp2_prod.pdf#page=87), [p.88](../../../../joi190092supp2_prod.pdf#page=88). PLAN. Initial 14-day lower-dose supply: MTX 12 pills, MMF 28 pills. Maintenance bottles MTX 50, MMF 100 pills. At baseline initial bottle plus one maintenance bottle; monthly thereafter through 5 months MTX 50 pills or MMF 200 pills, described 30-day supply plus visit buffer. After 6-month Phase I success dispense 120-day supply. Diaries/calendars and pill counting record adherence; do not count recently opened maintenance bottle at 2-week visit. Missing calendar→patient estimate missed doses. Missed MTX can be taken following day, otherwise wait next week and retain original weekday; MMF resume regular schedule. Matching keys: treatment adherence and exposure; bottle quantities administrative and distinct from prescribed daily dose.

### S-P065-011 — oral steroid co-intervention and endpoint target

Locations: [p.88](../../../../joi190092supp2_prod.pdf#page=88), [p.89](../../../../joi190092supp2_prod.pdf#page=89). PLAN. Prednisone preferred, equivalent substitute only contraindication. Start 1 mg/kg or 60 mg/day whichever lower, continue 2–4 weeks then taper, HOLD at 7.5 mg/day until first 6 months; success depends taper to 7.5. Phase I >6 months may reduce further. Phase II after efficacy failure reset 1 mg/kg/max60, lower physician-chosen dose medically indicated possible; after intolerance failure start discretionary. Medication full effect expected 6–8 weeks; inflammation during taper first 3 months does not itself mean failure. Faster taper possible severe side effects; medically necessary below7.5 first6 months allowed but strongly discouraged. Phase I6–12 taper optional, reaching0 mg by12 not mandatory.

### N-P065-003 — complete prednisone taper tables

Locations: [p.89](../../../../joi190092supp2_prod.pdf#page=89), [p.90](../../../../joi190092supp2_prod.pdf#page=90). PLAN. Table 6 dose mg/day : duration weeks : decrement mg/day = 60:2–4:10; 50:1:10; 40:1:5; 35:1:5; 30:1:5; 25:1:5; 20:1:2.5; 17.5:1:2.5; 15:1:2.5; 12.5:1:2.5; 10:1:2.5; 7.5:hold:no decrement. Note initial min(1mg/kg,60), hold7.5 through6 months; Phase II restart table for Phase I efficacy failure. If no improvement first4 weeks use best judgment for supplemental therapy, including pulse treatment/injections/additional immunosuppression. Table7 optional Phase I6–12 taper:7.5:1 week:2.5; <7.5 & ≥5:2–4 weeks:1–2.5; <5 & ≥2.5:2–4:1.5–2.5; <2.5 & ≥1:2–4:1; 0 endpoint. Footnote hold7.5 at least1 week on entering Phase I6–12. Matching keys: steroid co-intervention and endpoint success threshold.

### S-P065-012 — rescue taper and nonresponse definition

Location: [p.90](../../../../joi190092supp2_prod.pdf#page=90). PLAN. Mild reactivation up to1+ cells/haze; severe2+ or higher, retinal/choroidal severity physician discretion. Severe raise prednisone to1 mg/kg; mild up to double dose at flare until control then re-taper. Nonresponse means no increased inflammation but no improvement after first4 weeks1mg/kg prednisone; hold current dose another week; persistent nonresponse permits futility failure and Phase II, alternatively additional therapy recorded deviation. Early Phase I futility failure refusing switch still invited6-month visit. Phase II failure best judgment and attempt sixth-month data. Matching keys: failure adjudication and rescue intervention.

### S-P065-013 — topical steroid and injection component

Location: [p.91](../../../../joi190092supp2_prod.pdf#page=91). PLAN. Prednisolone acetate1% or equivalent≤2 drops/day sufficient for success, >2/day→failure; equivalent concentration/dose determined when other topical used; aim stop if possible. Table8 one drop8–10 times/day1–2 weeks;6/day1 week;4/day1;3/day1;2/day1;1/day1;none. One periocular triamcinolone40 mg or intravitreal triamcinolone4 mg injection for persistent macular edema permitted first90 days in each Phase I and Phase II. Any injection solely inflammation requires protocol deviation; any reason after90 days requires deviation. Calcium500 mg three times/day; vitamin D400–800 IU/day recommended for all. P.92 other topical adjuncts permitted; intravenous therapy, added immunosuppressives or surgery not allowed during study period; necessary exceptions recorded deviation. Matching keys: success topical threshold, injection window and rescue/co-intervention.

### S-P065-014 — outcome measurement and data capture

Locations: [p.92](../../../../joi190092supp2_prod.pdf#page=92), [p.93](../../../../joi190092supp2_prod.pdf#page=93), [p.96](../../../../joi190092supp2_prod.pdf#page=96). PLAN. SF-36 all patients when applicable; NEI-VFQ-25 all; IND-VFQ Indian patients only. VA, slitlamp and IOP before dilation; posterior examination/OCT/fundus/labs afterward; fluorescein angiogram not a study assessment but recorded when done. PDF forms double-entered into REDCap by Madurai staff. Matching keys: visual acuity, macular thickness/edema, visual/health QOL, assessment time points.

### S-P065-015 — complete assessment timing/visit windows

Locations: [p.93](../../../../joi190092supp2_prod.pdf#page=93), [p.94](../../../../joi190092supp2_prod.pdf#page=94), [p.95](../../../../joi190092supp2_prod.pdf#page=95). PLAN. Phase I randomized drug until efficacy/intolerance/safety failure; initial≤6-month efficacy/intolerance failure switches alternate. SAE switch depends monitor, collect6-month outcome even no switch if willing. Success6-month continues6 months, Phase I visit schedule while same randomized drug. Baseline-I Day1 first treatment; follow-ups anchored randomization; baseline eye exam up to14 days before enrollment; labs4 weeks or90 days depending test; minimum2 weeks between visits. Table9 Phase I0–6 or Phase II: baseline; week2±3 days; months1,2,3,4,5±15 days; month6 −15 to+30 days. Monthly visits calculated from Phase I baseline average days/month; late patients brought ASAP. Table10 Phase I6–12: month9±15 days;month12−15 to+30 days anchored Phase I baseline/treatment. Phase II baseline must start within2 weeks of Phase I failure unless exceptional coordinating-center permission; new Day1 is first rescue dose, same day as last Phase I visit or separate within2 weeks. Phase II follow-up anchored Baseline-II not changed, minimum2 weeks between visits. Nonstudy failure visit collects prescribed forms; Phase I failure→Baseline II immediately or≤14 days; Phase II failure→continue follow-up and collect6-month data. Matching keys: primary/secondary endpoint windows and switching treatment duration.

## N-P065-004 — complete form-completion matrix, p.96

Location: [p.96](../../../../joi190092supp2_prod.pdf#page=96), PLAN, MOP4.2. Visually transcribed because OCR table structure is unreliable. Columns I-B=Phase I baseline; I-W2=week2; I-F=months1–5,9; I-T=treatment failure anytime; I-E=months6,12; II-B=Phase II baseline; II-W2=week2; II-F=months1–5; II-T=treatment failure anytime; II-E=month6. `X` required, `(x)` if applicable, dash blank.

| Form | I-B | I-W2 | I-F | I-T | I-E | II-B | II-W2 | II-F | II-T | II-E |
|---|---|---|---|---|---|---|---|---|---|---|
| Eligibility/screening | X | — | — | — | — | — | — | — | — | — |
| Consent | X | — | — | — | — | — | — | — | — | — |
| Baseline history | X | — | — | — | — | — | — | — | — | — |
| Clinical eye exam | X | — | X | X | X | — | — | X | X | X |
| Secondary clinical eye exam | X | — | — | X | X | — | — | — | X | X |
| Visual acuity | X | — | X | (x) | X | — | — | X | (x) | X |
| OCT | X | — | X | (x) | X | — | — | X | (x) | X |
| Fundus | X | — | — | (x) | X | — | — | — | (x) | X |
| Laboratory report | X | X | X | (x) | X | — | X | X | (x) | X |
| AE checklist | — | X | X | X | X | X | X | X | X | X |
| Vision-related QOL | X | — | — | X | X | — | — | — | X | X |
| Health-related QOL | X | — | — | X | X | — | — | — | X | X |
| Treatment assessment | X | X | X | X | X | X | X | X | X | X |
| Patient calendar | — | X | X | X | X | — | X | X | X | X |
| Medication log | X | X | X | X | X | X | X | X | X | X |
| Patient dropout | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) |
| Protocol deviation | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) |
| AE narrative | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) |
| AE log | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) | (x) |

Footnotes: failure may be declared scheduled or non-study; all `(x)` only if applicable; Phase II baseline schedule applicable if not switching same day as Phase I failure; patient calendar completed by patient and brought to coordinator. Matching keys: observed secondary outcomes and ascertainment time points.

## Mapping limitations and completion

Mapped32/32 physical pages, 23 native-layout and9 OCR/image pages; no scientific-coverage gaps. Nine images inspected individually. Legacy OCR may omit glyphs or table alignments; above tables and thresholds use visual readings, in particular p.96 complete matrix rather than OCR rows. Shard has15 statistical/design relationships and4 contextual/numeric relationship groups. Reusable page text remains available in the hashed evidence assets as a locator; the structured map retains all result-relevant numbers and definitions. Administrative contents and rosters are recorded compactly in coverage. Visual transcription above and the exact physical PDF page prevail. No old candidate/audit conclusions read or reused.

