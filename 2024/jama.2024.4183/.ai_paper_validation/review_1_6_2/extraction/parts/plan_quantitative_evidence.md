# DOC-002 PLAN quantitative evidence map

Status: COMPLETE. Scope: joi240036supp1_prod_1716416466.00349.pdf, physical PDF pages 1-45, all pages. Document content: Protocol 2014-0213, August 23, 2023. All locations have role PLAN. The printed protocol page equals physical PDF page. Local PLAN-N and PLAN-S keys identify evidence records for later global relationship assignment; they are not candidate IDs. No checker finding, inclusion decision, or adjudication is made here. Matching main-paper keys are semantic keys for the separate DOC-001 mapper to join; this shard did not read DOC-001 or DOC-003.

## Provenance and engines

All 45 source units have USABLE source-matched legacy layout text: `.ai_paper_validation/review_1_5_3/preprocessing/support_doc002/layout_pN.txt`, with N replaced by the physical page. The aggregate `.ai_paper_validation/review_1_5_3/preprocessing/support_doc002/layout_all_pages.txt` is overlapping provenance. The curator independently matched these against current direct PDF text; no legacy scientific outputs were read. Fresh-required pages: 0. Every page's text was read, including cover, contents, administrative and reference material.

Direct visual confirmations used Poppler pdftoppm 26.01.0 on CPU, 105 dpi, for physical pages 8,10,16,17,22,28,29,30,31,32,33,34. Exact command template executed separately for each listed N:

`pdftoppm -f N -l N -r 105 -singlefile -png joi240036supp1_prod_1716416466.00349.pdf .ai_paper_validation/review_1_6_2/preprocessing/plan_mapper/page-N`

Outputs: `.ai_paper_validation/review_1_6_2/preprocessing/plan_mapper/page-8.png`, `.ai_paper_validation/review_1_6_2/preprocessing/plan_mapper/page-10.png`, `page-16.png`, `page-17.png`, `page-22.png`, `page-28.png`, `page-29.png`, `page-30.png`, `page-31.png`, `page-32.png`, `page-33.png`, `page-34.png` in that same directory. Each was visually opened. This resolves flow-arrow allocation, timeline column alignment, safety-table shading, Greek symbols, signs/subscripts and power-table rows. No OCR, fallback environment, Office extractor, formula execution or workbook operation was needed. There are no supplied workbook formulas/cached values or CSV/DOC/DOCX units in this assigned scope.

## Complete physical-page coverage

Each row was inspected from its exact layout_pN.txt; visual source confirmation is additionally indicated. COMPLETE_NA means that the page was opened and assessed but contributes no prospective result-relevant relationship.

| Page | Status | Content basis and mapped record(s) |
|---:|---|---|
| 1 | COMPLETE_NA | Protocol cover, title, PI and version/date; identity only. |
| 2 | COMPLETE_NA | Contents with section pointers; no analysis values or rules. |
| 3 | COMPLETE | Historical smoking burden, treatment rationale; planned 500-person SMART; PLAN-N001,N020. |
| 4 | COMPLETE | Initial/rescue doses, response decision, baseline heterogeneity and main 12-week criterion; PLAN-N002,N003; S001,S002. |
| 5 | COMPLETE | Historical augmentation efficacy and AE counts, treatment rationale and equal-benefit cost/side-effect consideration; PLAN-N020; S002. |
| 6 | COMPLETE | Double-blinding, Aims 1-5 and hypotheses/models; PLAN-S003 through S007. |
| 7 | COMPLETE | End of Aim 5; exploratory Aims 6-7; planned recruitment/sample and minimization; PLAN-N001,N004; S007-S009. |
| 8 | COMPLETE | Direct source image confirms CO parenthesis ≤5 rather than reusable text <5; inclusion and exclusion criteria item by item; PLAN-N004,N005. |
| 9 | COMPLETE | Remaining exclusion criteria, tobacco definition and recruitment section; PLAN-N005. |
| 10 | COMPLETE | Figure 1 all eight paths, recruitment and population context; PLAN-N003,N020; source image inspected. |
| 11 | COMPLETE | Consent, baseline eligibility/testing, cotinine/NicAlert rule; PLAN-N006. |
| 12 | COMPLETE | Re-screening time windows, labs/NMR, final medical clearance; PLAN-N006. |
| 13 | COMPLETE | Delayed randomization checks and visit/follow-up/support-call windows; PLAN-N007. |
| 14 | COMPLETE | Medication start, adherence measurement, V5/V7 drug levels, early termination follow-up; PLAN-N008; S010. |
| 15 | COMPLETE | Withdrawal definition and returned-medication handling; PLAN-N008. |
| 16 | COMPLETE | Table 1 full timeline and assessment cells; PLAN-N009,N010; source image inspected. |
| 17 | COMPLETE | Table 1 continuation and every footnote; questionnaires, MINI, FTND, WSWS; PLAN-N010,N011; source image inspected. |
| 18 | COMPLETE | PANAS/CES-D/PHQ/TSAMS/motivation/CERQ/sleep/SETC/SLIPS scales; PLAN-N011. |
| 19 | COMPLETE | SLIPS/SUPPS-P/RPI, exploratory impulsivity, e-cigarettes, EMA algorithm; PLAN-N011,N012; S011. |
| 20 | COMPLETE | EMA applicability, primary/secondary abstinence definition, biomarkers and missing TLFB; PLAN-N013; S008,S012. |
| 21 | COMPLETE | CTCAE, AE dosing/monitoring and start of safety table; PLAN-N014. |
| 22 | COMPLETE | Table 6 AE recording shading, serious-event definition and collection period; PLAN-N014; source image inspected. |
| 23 | COMPLETE | SAE sponsor reporting period, missing-visit management and blinded assessment; PLAN-N014,N015. |
| 24 | COMPLETE | Assessment completion policy, historical efficacy and Phase I dose/timing; PLAN-N002,N015,N020. |
| 25 | COMPLETE | Phase II dose/timing, BP modifications and minimization implementation; PLAN-N002,N016; S001. |
| 26 | COMPLETE | Unblinding rules, counseling duration/frequency, compensation; PLAN-N017,N018. |
| 27 | COMPLETE | Open-label pilot, general strategy, endpoint and responder/nonresponder aims; PLAN-N001; S002,S003-S007,S012. |
| 28 | COMPLETE | Covariate, ITT/missingness, models, priors, weighting, coding, master equation and first cell; PLAN-S013-S017; source image inspected. |
| 29 | COMPLETE | Seven remaining cells, Aim 1 and all Aim 2 contrasts, Aim 3 rationale; PLAN-S017-S020; source image inspected. |
| 30 | COMPLETE | Aim 3-5 contrasts, Aim 6/7 methods, power assumptions; PLAN-S020-S024; source image inspected. |
| 31 | COMPLETE | Advancement rule, simulation model, priors and 95% credible intervals; PLAN-S024,S025; source image inspected. |
| 32 | COMPLETE | Figure 2 all ten response/input distributions and Monte Carlo count; PLAN-S026,S027; source image inspected. |
| 33 | COMPLETE | Table 2 all eight cells, predictive-power definition/N, clinical comparator; PLAN-S027,S028; source image inspected. |
| 34 | COMPLETE | Table 3 all eight effects and four power thresholds per effect; PLAN-S029; source image inspected. |
| 35 | COMPLETE | Protection section: historical varenicline AE frequencies; PLAN-N020. |
| 36 | COMPLETE | Historical depression trial efficacy/safety; PLAN-N020. |
| 37 | COMPLETE | Prospective tolerability eligibility for VAR augmentation; historical trial counts; PLAN-N019,N020. |
| 38 | COMPLETE | Prospective tolerability eligibility for NRT augmentation and historical safety; PLAN-N019,N020. |
| 39 | COMPLETE | Prospective AE duration, data integrity, start of references; PLAN-N014,N021. |
| 40 | COMPLETE_NA | References 4-21 only; bibliographic dates/pages are not trial outcome values. |
| 41 | COMPLETE_NA | References 22-39 only; no additional prospective analysis rules. |
| 42 | COMPLETE_NA | References 40-57 only; scale/method sources already identified on substantive pages. |
| 43 | COMPLETE_NA | References 58-76 only; no additional result-relevant values. |
| 44 | COMPLETE_NA | References 77-97 only, including cited Bayesian/missingness methods; no new plan specification. |
| 45 | COMPLETE_NA | References 98-103 only; no additional outcome/model rule. |

## Planned numeric, treatment, endpoint and operational records

Source link prefix for this artifact depth is `../../../../joi240036supp1_prod_1716416466.00349.pdf#page=N`. Each link below points to a physical page. The legacy text for each cited page is the exact layout_pN.txt path given above.

### PLAN-N001 — Trial sample, pilot and accrual quantities

Locations: [p3](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=3), [p7](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=7), [p27](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=27), [p33](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=33). Planned SMART recruits 500 smokers. Participants section: double-blind two-group parallel initial treatment; up to 510 smokers = up to 10 pilot + 500 study participants. Only 510 eligible enrollment planned; prior experience says at least three times the needed number must be screened/registered in CORe; text separately estimates at least 1000 screened to attain needed eligible data-analytic sample. Power evaluated for N=500. Pilot: up to 10, same procedures except placebo if unavailable; open-label VAR or commercial NRT, separate open-label consent. Purpose procedural testing; if placebos available pilot receives placebo per protocol. No separate explicit pilot analytic-inclusion rule printed. Main matching keys: planned N, SMART randomized population, pilot exclusion/inclusion and sample-size basis.

### PLAN-N002 — Randomized pharmacotherapy dose, phase and duration

Locations: [p4](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=4), [p7](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=7), [p24](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=24), [p25](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=25). Initial NPL = one 21-mg nicotine patch plus ad lib/as-needed 2-mg nicotine lozenge to manage/prevent craving; VAR = 2-mg total daily. All receive both medication forms, one active and one matched placebo, including lozenges. Start day after randomization, 7 days before target quit date; VAR titration 0.5 mg/day days1-3, 0.5 mg twice daily days4-7, 1 mg twice daily thereafter. Initial patch + lozenge active from treatment initiation; corresponding placebo VAR. VAR recipients get placebo patch/lozenge. Abstinent week6/V5 remain initial treatment to week12/V8. Nonabstinent week6 have second randomization and six more medication weeks. Switch-to-VAR uses Phase I titration. VAR+ adds 1 mg with PM dose (3 mg total daily); NPL+ adds another 21-mg patch in AM (42 mg total daily) while retaining 2-mg ad lib lozenge. Other groups receive inactive placebos. No printed maximum daily lozenge count in assigned plan. Main keys: initial/rescue medication, 2→3-mg VAR, 21→42-mg patch, lozenge dose, 6+6-week phases, double blind/double dummy and titration.

### PLAN-N003 — Figure 1 decision paths

Location: [p10](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=10), visually confirmed. NPL→Quit→NPL; NPL→No Quit→VAR, NPL, or high-dose patch+lozenge NPL+. VAR2mg→Quit→VAR; VAR2mg→No Quit→VAR, NPL, or VAR3mg VAR+. Two response paths and six nonresponse paths. No percentages or randomization probabilities printed in figure. Main keys: SMART response decision, eight treatment pathways, rescue analysis strata. See S001 for stated minimization and probability limits.

### PLAN-N004 — All inclusion criteria

Locations: [p7](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=7), [p8](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=8). Age18-75; average smoking ≥5 cigarettes/little cigars/cigarillos per day in preceding2 months; expired CO ≥6ppm (printed parenthesis: if ≤5, positive cotinine test); interested in treatment that might change smoking behavior; able to follow English verbal/written instructions and complete all aspects; informed consent and agreement to all assessments/procedures; reachable address/telephone; only participant in household. This parenthesis is transcribed as printed, not silently reconciled with p11 NicAlert or CO rules. Smokers ready, unsure, or not yet ready to quit can enter if willing to receive treatment (p4). Main keys: smoking/CO/age eligibility, motivation population, household unit.

### PLAN-N005 — All exclusion criteria

Locations: [p8](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=8), [p9](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=9). Other tobacco ≥3 days/week in prior month if unwilling to refrain; current/planned other cessation program within next12 months; planned other nicotine substitutes or cessation treatments next12 months; uncontrolled SBP>180 or DBP>110; severe kidney disease with creatinine clearance<30 and/or severe liver disease with tests>4×upper normal level; potentially clinically significant abnormal kidney/liver labs per investigator; serious/unstable disease past3 months; abnormal rhythms/cardiovascular disease (stroke/angina/heart attack) past3 months case-by-case physician determination. Current medications: cessation drugs in last7 days (Wellbutrin/Bupropion/Zyban/NRT/Chantix); MAOI/Elavil depression drugs last14 days; precautionary list including nitroglycerin case-by-case; daily opioids≥30 days exclusionary, PRN allowed as printed '3:7 days per week or less' or more frequent use lasting<1 month. MINI exclusions: current manic/hypomanic episode (C); alcohol abuse past6 months/current dependence (I/addendum); substance abuse past6 months/current dependence (J/addendum); current/lifetime psychosis or mood disorder with psychotic features (K); other psychiatric conditions if clinically unstable/unsuitable per PI/physician. Suicidality MINI B moderate9-16 or high≥17; psychiatric hospitalization within1 year; positive screening pregnancy test (not tested if2-year postmenopausal, tubal ligation, partial/full hysterectomy); pregnancy, breastfeeding or unprotected childbearing potential. Accepted contraception: approved hormone, barrier+spermicide, IUD; emergency-only products not routine contraception. Hypersensitivity VAR/NRT/components; any condition or concomitant medication compromising safety/treatment; unsuitable investigational-drug candidate or unable to complete follow-up. Positive toxicology cocaine, opiates, methadone, benzodiazepines, barbiturates, amphetamines, methamphetamines, PCP, THC; valid prescriptions for opiates/benzodiazepines/barbiturates/amphetamines/methadone exempt; one repeat screen allowed, second positive prevents return; physician may clear plausible cross-reactive false positive. Cigarettes include little cigars/cigarillos for eligibility and ongoing smoking status. Main keys: inclusion/exclusion population and abstinence tobacco scope.

### PLAN-N006 — Screening criteria, biomarkers and eligibility timing

Locations: [p11](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=11), [p12](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=12), [p13](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=13). V0 within30 days telephone screen; one second phone screen gives additional30 days; failure then ineligible with90-day wait to re-enroll. V1 usually within30 days V0. Prior other-study MINI/labs/BP valid30-60 days. Psychiatric/medical stability judged over last3 months; lab results/final clearance before randomization. V1 delays beyond30 days allowed with renewed pregnancy/BP/medication/mental/medical/smoking review; significant change triggers repeat baseline as deemed appropriate. Urine drug failure allows one repeat. Cotinine at screening if CO<11ppm; CO6-10 cotinine is not an inclusion/exclusion test. Same standard V1. NicAlert value>2 or equivalent positive cotinine required when applicable. Baseline bilirubin, creatinine, GGT, AST, ALT; second sample NMR, processed/bankable. Two consents: screening V0 (required pre-randomization tests), treatment V1. Main keys: analyzed/randomized eligibility, NMR baseline covariate and low-CO confirmation.

### PLAN-N007 — Visit and follow-up windows

Location: [p13](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=13). V2 +3days; V6 +6; V5 -3/+10; V7 -3/+6; V8 +25, starting only after≥24h off study medication. Closed-clinic next-business-day exception except V2(+3),V5(+10),V8(+25); physician may extend V5 beyond+10 in special circumstances. 3-month follow-up -3days/+1month; 6-month follow-up -1month to final abstinence data collection or trial end, earlier of those. Missing follow-up: call, collect at least TLFB/CO/saliva cotinine; abstinent unable to attend can mail questionnaire/cotinine packet. Support calls1day prequit,3days postquit,3days and14days post-rerandomization; latter two omitted when abstinent/off medication. Separate sentence says '+2 day window for Visit 2' when discussing V2/T2 overlap. Same-day V2 cancels T2; V6 within2days T4 cancels T4; zero-day call window with≥2 attempts. Missing visits/calls recorded, not deviations. Prior-trial expected75% visits, not prospective sample denominator. Main keys: outcome assessment windows, timing, follow-up data and nonresponse reassignment time.

### PLAN-N008 — Medication measurement and follow-up continuity

Locations: [p14](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=14), [p15](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=15). Smoking diary is memory aid; only TLFB validates smoking behavior. Physical pill count determines compliance if diary/verbal/count conflict. Overall compliance ideally V8/week12 or when medication returned. Lost follow-up: compliance assumed through first missed visit after last contact, aided by verbal/prior counts. Unreturned/unaccounted medication/missed doses not deviations. Prior-trial about75% take≥80% dose; plan will account for exposure in analyses. Permanent early drug cessation before V8 triggers attempted ET8/end-treatment evaluations; encourage follow-up/counseling through study even off drug. No V8 draw/end-medication reassessment if already done at ET8 except physician-requested redraw. Withdrawal = active consent withdrawal before protocol completion or investigator safety withdrawal; seek medicines/evaluations. Main keys: adherence, ITT, drug exposure and cessation follow-up.

### PLAN-N009 — Table 1 exact time alignment

Location: [p16](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=16), visual authority. Screening/Treatment/Follow-up heading: follow-up '30 Day Post EOT & 6 mos Post-Quit'. Study Day and Days from Quit have one extra unlabeled pre-screen column before visit-1. Empty entries below mean blank printed cells; hyphens preceding numeric days are signs.

| Column | Study day | Days from quit | Days on medication | Days on medication Phase II |
|---|---:|---:|---:|---:|
| Unlabeled prescreen | -28 | -42 | blank | blank |
| Visit -1 | -14 | -28 | blank | blank |
| Visit 0 | 1 (f) | -14 | blank | blank |
| Visit 1 (a) | 8 | -7 | 0 | blank |
| T1 | 15 | -1 | 7 | blank |
| TQD | 16 | 0 | 8 | blank |
| Visit2 (m) | 17 | 1 | 9 | blank |
| T2 (m) | 19 | 3 | 11 | blank |
| Visit3 | 24 | 8 | 16 | blank |
| Visit4 | 38 | 20 | 28 | blank |
| Visit5 | 50 | 34 | 42 | blank |
| T3 | 53 | 39 | 45 | 3 |
| Visit6 (n) | 59 | 43 | 49 | 7 |
| T4 (n) | 64 | 50 | 56 | 14 |
| Visit7 | 73 | 57 | 63 | 21 |
| Visit8 (b,c) | 94 | 78 | 84 | 42 |
| Visit9 (d) | 124 | 108 | -30 | -30 |
| Visit10 (e) | 197 | 181 | -104 | -104 |

Main keys: week6/12 versus postquit time, V5 rerandomization and V8 endpoint, 3/6-month follow-up. Printed table entries retained without subtraction-based normalization.

### PLAN-N010 — Table 1 all assessment schedules and notes

Locations: [p16](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=16), [p17](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=17), both visually inspected. X cells:

| Assessment | Printed scheduled contacts |
|---|---|
| Phone Screen | Unlabeled prescreen |
| Orientation | Visit-1 |
| Consent | V0,V1 |
| FTND, CERQ, Smoking Health, Medical History | V0 |
| PHQ | V1,V2,V3,V4,V5,V6,V7,V8,V9 |
| Blood chemistry | V0,V8 |
| NMR | V0 |
| Varenicline level | V5,V7 |
| TSAMS | V0,V5 |
| Motivation stratification question | V1,V5 |
| Pregnancy | V0,V1,V5,V7,V8 |
| Drug screen | V0 |
| Cotinine test if applicable | V0,V1 |
| Height | V0 |
| Weight, BP/heart rate | V0,V1,V5,V7,V8,V9,V10 |
| ROS/physical | V0,V1 |
| MINI | V0 |
| Abstinence questionnaire/TLFB | V0,V1,T1,V2,T2,V3,V4,V5,T3,V6,T4,V7,V8,V9,V10 |
| E-cigarettes | V0 |
| SLIPS | V1,V5,V7,V8,V9,V10 |
| RPI | V1 |
| WSWS,PANAS,CES-D | V1,V2,V3,V4,V5,V6,V7,V8,V9,V10 |
| SECT (printed table label), SUPPS-P | V1,V5,V7,V8,V9,V10 |
| Sleep | V0 |
| EMA assessments | V1,T1,V2,T2,V3,V5,T3,V6,T4 |
| EMA daily diary | V1,T1,V2,T2,V3,V4,V5,T3,V6,T4,V7,V8 |
| End medication assessment | V5,V8 |
| Smoking diary | V1,V5,V7,V8 |
| Urine cotinine | V1,V5,V7,V8,V9,V10 |
| Expired CO | V0,V1,V5,V7,V8,V9,V10 |
| Medication count | V5,V7,V8 |
| Adverse events | V1,V2,V3,V4,V5,V6,V7,V8,V9 |
| Concomitant medication | Visit-1,V0,V1,V2,V3,V4,V5,V6,V7,V8,V9 |
| Support | T1,T2,T3,T4 |
| Counseling | V1,V2,V3,V4,V5,V6,V7,V8 |
| Dispense medication | V1,V5 (p17 continuation) |

Footnotes: bold visits in person; a randomization/start next day; b,c V8 EOT; d V9 3months postquit; e V10 6months postquit; f V0 within30days phone assessment, second30days on re-screen; g ask e-cigarettes V0 and first later report of use; h V9/V10 urine if clinic, mailed saliva if unavailable, saliva substitute for inability to produce timely urine at applicable visits; i diary daily84days from day after randomization, EMA assessments daily2weeks in Phase I and2weeks in Phase II from day after V5; * screening V1 before consent; ** bulk V1/V5 dispensing, exceptional schedule changes and physician continuation decision if cannot attend V5; j ROS/physical V0 orV1; k screening consent V0/treatment V1; l no VAR draw if no tablets in preceding3days or if V5 abstainer at V7; m T2 cancellation if same day V2; n T4 cancellation if within2days V6; o questionnaires may arrive up to5days before clinic. Main keys: assessment schedule, secondary outcome status, measurement timing and biomarker subset.

### PLAN-N011 — Scales, moderators and measured domains

Locations: [p17](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=17), [p18](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=18), [p19](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=19). MINI6.0 DSM-IV Axis1 and graded suicidality; FTND6 items (time-to-first-cigarette≤30minutes cited explanatory characteristic); WSWS anger, anxiety, concentration, sadness, craving plus Minnesota items, historical alphas0.75-0.93. PANAS two10-item PA/NA scales, rating1-5, historical alpha PA.86-.90, NA.84-.87. CES-D20 items/four factors (depressed affect/enervation/lack positive affect/interpersonal); PHQ9 items previous2weeks for safety; TSAMS10 items motivation; separate stages-of-change question high/low motivation for stratification. CERQ-short18 items/nine subscales self-blame, acceptance, rumination, positive refocus, planning refocus, positive reappraisal, perspective, catastrophizing, other-blame. Sleep4 items baseline. SETC confidence and temptation in20situations, four5-item subscales, five-point not-at-all→extremely; described cue domains negative affect, social/positive, physical concerns, withdrawal/urges. SLIPS23items rating0-3 relative change in pleasure/interest. SUPPS-P20items/four scales premeditation(lack), urgency, sensation seeking, perseverance(lack). RPI20items/two factors reward probability and environmental suppressors; expected IRS- lower reward/higher suppressor versus IRS+. E-cigarettes baseline and later use-reports. Main keys: secondary affect/withdrawal/craving/reinforcement, baseline moderators and symptom instruments.

### PLAN-N012 — EMA sampling and applicability

Locations: [p19](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=19), [p20](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=20), p17 notes. One diary/day throughout84-day treatment,30min after waking about previous day: CPD, alcohol, affect, sleep, motivation, compliance. Random assessments3/day, day divided3blocks, one random prompt/block, covering affect/craving/expectancies/motivation/availability/self-efficacy/stressors; separation algorithm prevents close prompts; optional delay≤20minutes. Random assessments only2weeks Phase I and2weeks Phase II. Historical burden17-30min/day, compliance>75%,>90% completed without delays; explicitly historical, not trial sample counts. EMA initiated only for subjects randomized after application complete/ready; those randomized before readiness do not participate, no deviation. Main keys: EMA analytic subset and randomized-outcome measurements.

### PLAN-N013 — Outcome definition, biochemical verification and time windows

Location: [p20](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=20); also p4,p6,p7,p27,p30. Primary = EOT seven-day point-prevalence abstinence/no smoking past7days (EOT12weeks). TLFB all contacts for cigarettes/other tobacco and nicotine including cigars/e-cigarettes; SRNT conformity stated. Secondary = continuous and prolonged abstinence at3and6months follow-up. Prolonged grace period starts2weeks following EOT; relapse≥5cigarettes from grace end to future point, examples printed EOT,3and6months postquit. Additional continuous abstinence over4weeks after EOT ('EOT-plus30days'). All data at EOT,3months,6months postquit. In-person abstinence verified expired CO<6ppm and/or salivary cotinine<15ng/ml at follow-up. Missing TLFB = nonabstinent. Cotinine half-life≈20h/exposure previous24-36h, baseline descriptive; subsequent<15ng/ml crosscheck for self-reported abstinent unable to attend clinic; urine nicotine/anabasine distinguish tobacco versus NRT; saliva if cannot give urine. No other composite primary components printed beyond p27 primary 'seven-day point prevalence and expired CO value'. Main keys: primary, continuous/prolonged secondary status, 7day/4week/grace/3month/6month windows, CO/cotinine threshold, all-smoking missingness and composite criteria.

### PLAN-N014 — Prospective safety collection/recording rules

Locations: [p20](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=20), [p21](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=21), [p22](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=22), [p23](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=23), [p39](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=39). CTCAE4.03 terminology/grades; response immediately→48h by rating. Baseline/EOT liver/renal labs, first attended follow-up substitute if V8 missed. Physician may adjust drug for AE/safety concern. AE monitoring until30days after drug completion; related probable/possible/definite followed to resolution/study end. Table6 PhaseIII shaded recording: unrelated/unlikely grades4-5; possible/probable/definitive grades2-5. PhaseI appears all cells; PhaseII unrelated/unlikely grades3-5 and related grades1-5. The trial adopts PhaseIII shaded areas. Serious criteria: death, immediately life-threatening event, hospitalization/prolongation, significant functional incapacity, congenital anomaly, or important medical event needing intervention/prevention. SAE captured first protocol-specific intervention→30days last dose unless consent withdrawn; later treatment-related SAE still reported. Follow to recovery/labs baseline/stabilization/acceptable resolution. General IND report≤5workingdays; unexpected related life-threatening/fatal≤24h(nextworkingday); Pfizer≤24h and reporting after first dose→28days discontinuation. These are administrative SAE channels, preserved separately from analytic AE collection. Main keys: safety outcome/denominator window, AE grades and intervention changes.

### PLAN-N015 — Missing assessment policy and blinding

Locations: [p23](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=23), [p24](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=24). Abstinence/self-report collected by counseling or other staff blinded to medication. Computer/phone assessment; reminders/reschedule within window. Telephone fallback can collect AE, concomitant drugs, abstinence questionnaire, PHQ, counseling. Entire clinic assessment≤45min. All visits need not be completed to participate; missing visits/associated missing assessments not logged as deviations. Main keys: analysis-set retention, outcome missingness and assessor blinding.

### PLAN-N016 — Blood-pressure-triggered dose changes

Location: [p25](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=25). Manual systolic or diastolic increase≥15%over baseline AND BP>160/100: stop ad lib lozenge, monitor; if≥15%increase persists at next contact after stopping, physician changes patch hours/discontinues. If any subsequent BP>180/110, discontinue lozenge and patch. VAR dose not adjusted by this BP rule. Main keys: randomized intervention exposure and safety modifications.

### PLAN-N017 — Counseling and unblinding

Location: [p26](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=26). All smokers brief manual-driven individual counseling:4in-person+4phone visits and up to4support calls,10-15min each over12weeks; text also compares10 versus12 treatment sessions to prior studies. Content quit preparation/high-risk coping/direct support/motivation to reset quit date/withdrawal/compliance. PhaseII safety calls omitted for abstinent/off-drug. Blinding break only individual safety need, prior IND notification and recorded reason; DSMB approval required for study-wide unblinded data release after all follow-up complete. No planned efficacy interim or arm-dropping decision for this trial is specified here; p6 describes dropping ineffective arms only as a possibility in a future adaptive trial. Main keys: behavioral cointervention, intervention duration and masking.

### PLAN-N018 — Compensation and assessment completion incentives

Locations p13,p17,p26. Up to$594 plus parking/metro for all visits/assessments, includes up to$84 EMA+$30phone-return. $10bonus for electronic questionnaire≤5days before clinic after version12 approval applies newly consented only; prior consent retains prior scheme; phone-visit questionnaires no advance-completion bonus. Mail abstinence packet$20 or comparable gift card. These are administrative/contextual values, not efficacy values. Main key: missingness/measurement implementation only.

### PLAN-N019 — Eligibility for augmentation

Locations: [p37](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=37), [p38](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=38). VAR3mg augmentation only for individuals who tolerate starting2mg well but continue smoking; double-patch+lozenge augmentation only for individuals tolerating starting NRT well but continuing smoking. Main keys: rerandomized rescue eligibility and analysis population, alongside p4/p7/p24 nonresponse descriptions.

### PLAN-N020 — Historical/background quantitative context (not trial outcomes or decision rules)

Pages3-5,10,24,35-38. These numbers were read and retained as context rather than as prospective result statements. p3 smoking worldwide≈5million premature deaths/year, US443000, Americans19%(43.8million),>40%annual quit attempt,<3%successful annual quit. p5/p37 prior VAR augmentation:73smokers after8weeks2mg,4weeks3mg→40%abstinence; AE22(30%),2stop nausea; nausea22/dreams17/vomiting13/insomnia12/headache7; naturalistic cancer88=44at2mg+44increase3mg(2AM+1PM) betweenweeks6-8; EOT4/44(9%)versus11/44(25%), chi-square3.94,P=.05,OR3.33,95%CI1.12-11.45. p5/p24/p38 NRT historical long-term benefit50-70%. p10 recruitment population3,596,086;59%Caucasian(42%non-Hispanic),19%African-American,5%Asian,.4%Native-American,33%Hispanic(any race). p24 historical VAR:threefold placebo; versus patch OR1.51(1.22-1.87),gum1.72(1.38-2.13),otherNRT1.42(1.12-1.79),combination1.06(.75-1.48); other meta-analysis>15000participants. p35 historical AE abdominal pain5-7%,constipation5-8%,flatulence6-9%,nausea16-40%,vomiting1-5%,dreams9-13%,headache15-19%,insomnia18-19%; nausea resolves10-12days,<3%withdrawal. p36 historical stable-depression trial525smokers,72%antidepressants stable2months, prior treatment2years;>one-third lifetime suicidal history; OR3.35(2.16-5.21),comparison historical3.85(2.69-5.50),suicidal ideation6.0-7.5%. p37 separate safety trial planned8000. p38 lozenge insomnia<5%; safety review35trials>9000participants; hospital observational187; high-dose42mg nausea/vomiting28%and24%. p39 prior clinical program>1800VARpatients since2006. Historical NMR/biomarker/scales reliability/time values remain in N011/N013. These data do not create a supplied separate REPORT document and are not prospective study endpoints. Main key: historical rationale only.

### PLAN-N021 — Data integrity administrative definitions

Location: [p39](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=39). Central departmental databases backed daily; selected-subset audits, password/physical security; two-stage survey editing (initial review then separate deviation review); statistician/PI/data managers regular review; continuous ranges/categorical valid-values/date-time/logical checks; data reports weekly or after new entry; initial quality review shortly after collection begins. No efficacy stopping, missing-data imputation, additional endpoint or statistical contrast specified here. Main key: data management only.

## Planned statistical relationship records

### PLAN-S001 — Allocation, randomization unit and stratification

Locations p4,p7,p25. Individual participants randomized to initial VAR/NPL, nonresponders rerandomized to continuation/augmentation/switch. Adaptive randomization/minimization stratifies motivation, gender and race. Program embedded in database, can randomize only once eligibility met/recorded; coordinator transmits assignment to pharmacy; kit/master key maintained with pharmacy; blinded stratum-distribution reports crosscheck. No exact initial allocation ratio, second-stage allocation ratio or minimization random component probability is stated anywhere in the assigned45pages. Figure1/2 branch counts cannot substitute for unstated probabilities. Main keys: individual SMART design, minimization factors, assignment probabilities and IPW.

### PLAN-S002 — Global prospective targets and success concept

Locations p4-5,p27-28. Primary criterion end-of-treatment12week abstinence, also multivariate withdrawal/craving/negative-affect outcome to distinguish effects when abstinence comparable; side-effect probabilities/cost considered when benefit relatively equal by subgroup. Five effects: Aim1 among6week responders VARvsNPL at6and12weeks; Aim4/5 among6week nonresponders differential augmentation/switch by initial treatment; Aim3 initialVAR nonresponders rescuevscontinuation; Aim2 initialNPL nonresponders rescuevscontinuation. p27 primary endpoint seven-day point prevalence AND expired CO, primary Bayesian approach probability interaction exists. Subsequent expansion might use posterior distributions as informative priors; future enrichment proportional to estimated benefit is proposed, not the current assignment rule. Main keys: primary statistical estimands, treatment sequence, subgroup interaction and Bayesian benefit.

### PLAN-S003 — Aim1

Locations p6,p27,p29. Estimate effects of6and12weeks2mgVARvsNPL on abstinence. Hypothesis week6no difference; week12VARsuperior. Logistic regression point prevalence of smoking Week12 among participants remaining initialVAR/NPL full12weeks. Analysis strategy p27 and contrast p29 explicitly identify6week responders. Printed contrast (beta0+beta1)-(beta0-beta1) for VARresponders minus NPLresponders. Main keys: initial-phase abstinence, responder continuation comparison and outcome coding.

### PLAN-S004 — Aim2

Locations p6,p27,p29. InitialNPL6week nonresponders, Week12 point prevalence via logistic regression continuation/NPL+,switchVAR. Hypotheses switch>augmentation>continuation. Three printed pairwise contrasts in S019. Main keys: CNRT/NPL initial rescue strata and all three contrasts.

### PLAN-S005 — Aim3

Locations p6,p27,p29-30. InitialVAR6week nonresponders, Week12 logistic regression continuationVAR2mg,augmentationVAR3mg,switchNPL. Hypothesis augmentation superior to both switch/continuation. Two printed contrasts in S020. Main keys: initialVAR rescue strata, augmentationvscontinue/switch.

### PLAN-S006 — Exploratory Aim4

Locations p6,p27,p30. Week12 effect of augmentation moderated by baseline treatment; nonresponse conditional; VAR-origin augmentation superior to NPL-origin augmentation. Logistic model PhaseI,PhaseII and their interaction. Printed contrast S021. Main keys: prespecified exploratory augmentation interaction/status.

### PLAN-S007 — Exploratory Aim5

Locations p6-7,p27,p30. Week12 effect of switching moderated by baseline treatment; NPL-origin switch superior to VAR-origin switch. Logistic PhaseI/PhaseII/interaction; printed contrast S022. Main keys: prespecified exploratory switching interaction/status.

### PLAN-S008 — Exploratory Aim6

Locations p7,p30. Week6 abstinence among initially randomizedVAR/NPL moderated separately by baseline motivation, dependence, NMR(normalvsslow). Each logistic model includes specified covariate,treatment,covariate×treatment. Vague neutral priors first, sensitivity with skeptical informative interaction priors per cited Dixon/Simon. NMR cutoff for normal/slow not numerically specified in assigned plan. Main keys: baseline motivation/dependence/NMR subgroup, moderator status and model.

### PLAN-S009 — Exploratory Aim7 and stated secondary outcomes

Locations p7,p30,p20. Continuous/prolonged abstinence3and6months explicitly secondary under exploratory Aim7. Affect/withdrawal/craving/nicotine reinforcement PANAS,CES-D,WSWS,mCEQ via GLM atWeeks6and12. AE differences in probability by treatment via Beta-Binomial. Distinguish these named outcomes from p20 additional4weeks-postEOT continuous abstinence. Main keys: secondary hierarchy, outcome status, safety and symptom models.

### PLAN-S010 — Exposure and drug-level relationships

Location p14. Analyze medication exposure; VAR levels V5/V7 to assess correlation with abstinence. No sample when no VAR/placebo past3days; V5abstainers omit V7since dose constant. This is a selected drug-level-measurement subset, not stated ITT exclusion. Main keys: adherence/biomarker subset and sensitivity covariate.

### PLAN-S011 — Additional exploratory symptom relationships

Locations p19. Impulsivity exploratory moderation of treatment effect on cessation and treatment effect on impulsive symptoms. RPI expected IRS- lower reward/higher environmental suppressor; no numerical IRS definition or contrast model in assigned text. Main keys: exploratory moderators/affective outcomes.

### PLAN-S012 — Endpoint/analysis-set/missingness definitions

Locations p20,p27-28. Primary EOT7daypointprevalence/expiredCO; six-week nonresponse determines rerandomization and week12stratum; no TLFB=nonabstinent. Primary ITT principles and all missing observations imputed smoking, without printed per-protocol alternative. Offdrug participants encouraged continued follow-up, missing visits not required for participation. Main keys: ITT/nonresponse rescue set, primary outcome and nonabstinent missing-data rule.

### PLAN-S013 — Covariate adjustment

Location p28. Preliminary inspect baseline group differences/compliance correlations with specified outcomes. Variables having both baseline group differences and outcome correlation treated potential confounders. Two analyses with/without relevant covariate assess confounding. No fixed demographic/cigarettes/medication-adherence covariate vector is specified beyond this rule and Aim6 moderators. Main keys: adjustment model/covariates and covariate sensitivity.

### PLAN-S014 — Generic model/data-type mapping

Location p28. Continuous→linear; dichotomous→logistic; time-to-event→proportional-hazards (SAS9.3 ProcGENMOD/PHREG). Longitudinal→generalized linear mixed models (ProcMCMC,SAS9.3). Bayesian analyses across these procedures. Main keys: Bayesian logistic abstinence, Cox/time-event and repeated-measure GLMM.

### PLAN-S015 — Missing-data models/sensitivities

Location p28. Primary ITT with missing=smoking. Secondary joint observed-outcome/missing-data modeling described robust to ignorable missingness. Sensitivities assess missing-data robustness; nonignorable patterns via pattern-mixture models. No fixed imputation draw count, tipping-point range or operational dropout-pattern grouping printed. Main keys: missingness/imputation planned versus reported, joint/pattern-mixture sensitivities.

### PLAN-S016 — Priors and weights

Location p28; p30-31. Proportion comparison priors Beta(a=1,b=1). Linear/logistic/Cox coefficient priors Normal(mean0,variance1×10^6), respectively linear/log-odds/log scales. Level1 standard residual variances Inverse-Gamma(shape.001,scale.001); level2variances Uniform(0,1000). Sensitivity optimistic,pessimistic/skeptical priors; interaction skeptical informative priors for Aim6. Inverse-probability weight stated to permit unbiased effect-size estimates with rerandomization, but exact probability values/weight formula not supplied. Simulation uses same logistic coding and neutral Normal0,variance1×10^6 log-form coefficients (p31). Main keys: beta-binomial vs regression primary approach, priors, IPW and sensitivity.

### PLAN-S017 — Coding, master logistic model and eight printed cell equations

Locations: [p28](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=28), [p29](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=29), source visually inspected. Symbols below use ASCII beta names to avoid native-PDF glyph corruption. Directly printed equation transcription, without algebraic repair:

`logit(y) = beta0 + beta1*a1 + beta2*anr21 + beta3*anr22 + beta4*anr23 + beta5*a1*anr21 + beta6*a1*anr22 + beta7*a1*anr23`.

Initial a1:VAR=1,NPL=-1. Nonresponder continuation anr21=1,others0; augmentation anr22=1,others0; switching anr23=-1,others0. Responders have zero rerandomization indicator vectors. Printed outcome cells:

| Cell | Printed linear expression | Page |
|---|---|---:|
| NRT+Loz responders | beta0-beta1 | 28 |
| VAR2mg responders | beta0+beta1 | 29 |
| NRT+Loz nonresponders→NRT+Loz | beta0-beta1+beta2-beta5 | 29 |
| NRT+Loz nonresponders→2*NRT+Loz | beta0-beta1+beta3-beta6 | 29 |
| NRT+Loz nonresponders→VAR2mg | beta0-beta1-beta4+beta7 | 29 |
| VAR2mg nonresponders→VAR2mg | beta0+beta1+beta2+beta5 | 29 |
| VAR2mg nonresponders→VAR3mg | beta0+beta1+beta3+beta6 | 29 |
| VAR2mg nonresponders→NRT+Loz | beta0+beta1-beta3+beta7 | 29 |

The last beta3 is what the source prints; it has not been replaced by another coefficient based on inferred coding. No fitted empirical coefficient estimates are printed in this plan. Main keys: primary model structure, saturated pathway estimates, labels/contrast identity and IPW.

### PLAN-S018 — Aim1 printed contrast

Location p29. VAR responders minus NRT+Loz responders = `(beta0+beta1)-(beta0-beta1)`. Main key: week12initial-responder comparison.

### PLAN-S019 — Aim2 all printed contrasts

Location p29. InitialNPL nonresponders: switchVAR minus continueNPL = `(beta0-beta1-beta4+beta7)-(beta0-beta1+beta2-beta5)`; augmentNPL minus continueNPL = `(beta0-beta1+beta3-beta6)-(beta0-beta1+beta2-beta5)`; switchVAR minus augmentNPL = `(beta0-beta1-beta4+beta7)-(beta0-beta1+beta3-beta6)`. Labels/direction retained. Main key: each Week12NPL-rescue pairwise contrast.

### PLAN-S020 — Aim3 all printed contrasts

Location p30. InitialVAR nonresponders: augmentVAR3mg minus continueVAR2mg = `(beta0+beta1+beta3+beta6)-(beta0+beta1+beta2+beta5)`; augmentVAR3mg minus switchNPL = `(beta0+beta1+beta3+beta6)-(beta0+beta1-beta3+beta7)`. Source beta3 retained in switchedNPLcell. Main key: Week12VAR-rescue comparison.

### PLAN-S021 — Aim4 printed contrast

Location p30. VAR-origin augmentVAR3mg minus NPL-origin augment2*NRT+Loz = `(beta0+beta1+beta3+beta6)-(beta0-beta1+beta3-beta6)`. Main key: cross-origin augmentation exploratory contrast.

### PLAN-S022 — Aim5 printed contrast

Location p30. NPL-origin switchVAR2mg minus VAR-origin switchNRT+Loz = `(beta0-beta1-beta4+beta7)-(beta0+beta1-beta3+beta7)`. Main key: cross-origin switching exploratory contrast.

### PLAN-S023 — Hypothesis hierarchy and decision rules

Locations p6-7,p29-31,p34. Aims1-3specified; Aims4-7explicitly exploratory. No quantitative multiplicity adjustment, familywise alpha, alpha spending, noninferiority/equivalence margin or efficacy interim boundary is specified within the45pages. The general benefit criterion for advancement to confirmatory study is separately S025; power table examines multiple posterior thresholds. Planned future arm dropping p6 is future-trial context, not current stopping rule. Main keys: outcome/analysis status, Bayesian superiority, multiplicity/interim specification.

### PLAN-S024 — Sample-size/power assumptions and simulation rationale

Locations p30-33. Power targets Aims1-5,7daypointprevalence and treatment/strategy. Week6VAR/NPLresponse derived meta-analysis; Week12conditional response from clinical consensus considering marginal rates in meta-analysis. Input estimates based on more conservative continuous abstinence; uncertain effects modeled distributions rather than fixed points. Bayesian Monte Carlo samples specified Beta distributions and fits planned logistic model with neutral coefficient priors. N=500; K=1000simulations. Table3claims all superiority hypotheses>80%chance detecting.90probabilitybenefit atN500. Historical clinical benchmark absolute-risk-reduction VARvsbupropion.089, described smaller than every Table3lower95%crediblelimit. Main keys: sample/power inputs, assumed rates, model reproducibility and predictive power.

### PLAN-S025 — Advancement criterion

Location: [p31](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=31), visual source. Narrative: posterior probability of >0.90 that postulated effect exists warrants further evaluation/confirmatory phase. Parenthetical printed nested expression transcribed: `Pr (Pr theta > 0 | data) > 0.90` (source has repeated Pr). Interpretation remains stated in prose: probability effect exists. Main keys: posterior benefit threshold and decision.

### PLAN-S026 — Figure2 every simulation prior/input

Location: [p32](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=32), visual source. Labels: Randomization PhaseI→Week6→rerandomization/continuation PhaseII→Week12. Displayed point/95%credible interval and Beta parameters retained exactly; no recomputation/normalization.

| Input/state | Printed probability | Printed 95% interval | Beta a | Beta b |
|---|---:|---|---:|---:|
| InitialNRT+Loz Week6response | .48 | .38-.58 | 193 | 210 |
| NRT+Loz responder continued Week12 | .50 | .40-.60 | 47.3 | 47.3 |
| NRT+Loz nonresponse continued Week12 | .02 | .0007-.0978 | 1.02 | 35.48 |
| NRT+Loz nonresponse augment2*NRT+Loz Week12 | .20 | .10-.34 | 8.90 | 34.6 |
| NRT+Loz nonresponse switchVAR2mg Week12 | .40 | .25-.57 | 14.4 | 21.5 |
| InitialVAR2mg Week6response | .50 | .40-.60 | 785 | 869 |
| VAR2mg responder continued Week12 | .75 | .65-.83 | 62.2 | 21.0 |
| VAR2mg nonresponse continued Week12 | .15 | .05-.30 | 4.35 | 23.1 |
| VAR2mg nonresponse switchNRT+Loz Week12 | .20 | .15-.26 | 42.8 | 170.0 |
| VAR2mg nonresponse augmentVAR3mg Week12 | .40 | .26-.55 | 17.3 | 25.7 |

Nonresponse nodes themselves have no numerical response-rate label. Main keys: sample-size assumed rates/distributions and SMART response fractions.

### PLAN-S027 — Table2 all simulated study cells

Location: [p33](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=33), visual source. Averaged point estimates/95%credible intervals from logistic fits acrossK1000, not empirical trial results.

| Simulated Week12 cell | Average point | Average 95% interval |
|---|---:|---|
| RespondersNRT+Loz | .504 | .441-.566 |
| RespondersVAR2mg | .749 | .692-.801 |
| NonrespondersNRT+Loz→NRT+Loz | .029 | .017-.047 |
| NonrespondersNRT+Loz→2*NRT+Loz | .204 | .160-.255 |
| NonrespondersNRT+Loz→VAR2mg | .399 | .343-.458 |
| NonrespondersVAR2mg→VAR2mg | .159 | .120-.203 |
| NonrespondersVAR2mg→VAR3mg | .404 | .347-.463 |
| NonrespondersVAR2mg→NRT+Loz | .201 | .157-.251 |

Main keys: power-model precision and pathway mapping; no main empirical result should be matched to these as observed rates.

### PLAN-S028 — Predictive power/precision definition

Location p33. Table3power to detect any benefit HA:theta>0; posterior-probability targets.80,.85,.90,.95. Average point/95%credibleinterval of effects from proposed logistic models acrossK1000; average intervals index design precision. Clinical benchmark.089 as S024. Main keys: power and Bayesian decision criterion.

### PLAN-S029 — Table3 every effect and threshold row

Location: [p34](../../../../joi240036supp1_prod_1716416466.00349.pdf#page=34), visually confirmed. Columns printed Effect; PosteriorProbabilityPr(theta>0); PowertoDetectPr(theta>0); AveragePointEstimate; AverageInterval(95%C.I.)Estimate. All power vectors below align to posterior thresholds[.80,.85,.90,.95], in that order. Empty repeated point/interval cells inherit the single printed effect-row value for map presentation.

| Printed effect label/group | Power at .80 | Power at .85 | Power at .90 | Power at .95 | Average point | Average 95% interval |
|---|---:|---:|---:|---:|---:|---|
| PhaseIresponders/Aim1 | .948 | .980 | .974 | .963 | .240 | .160-.327 |
| InitialNPLnonresponse/Aim2:VARvsNPL(first occurrence) | .999 | .999 | .999 | .998 | .370 | .309-.431 |
| InitialNPLnonresponse/Aim2:NPL+vsNPL | .964 | .957 | .951 | .939 | .175 | .125-.228 |
| InitialNPLnonresponse/Aim2:VARvsNPL(second printed occurrence) | .878 | .863 | .842 | .819 | .195 | .119-.269 |
| InitialVARnonresponse/Aim3:VAR+vsVAR | .930 | .922 | .915 | .895 | .245 | .172-.316 |
| InitialVARnonresponse/Aim3:VAR+vsNPL | .917 | .905 | .890 | .859 | .202 | .127-.288 |
| PhaseI*Augmentation/exploratoryAim4 | .885 | .875 | .862 | .837 | .199 | .123-.274 |
| TreatmentI*Switching/exploratoryAim5 | .899 | .885 | .872 | .846 | .198 | .123-.272 |

Both Aim2'VARvsNPL' labels are preserved as printed, with occurrence indexing solely to keep rows distinct. The planned comparisons for Aim2 remain all three in S019. Main keys: planned effect contrasts, Bayesian power and sample-size justification; no empirical trial results here.

## Join guide and bounded gaps

Planned/report joins require matching population, endpoint, timing and contrast: primary EOT7daypointprevalence at12treatmentweeks; initial6week response; initialVARorNPLnonresponse rescue; continuation/switch/augmentation; full treatment dose/duration; secondary continuous/prolonged3and6months plus4weekspostEOT; affect/withdrawal/craving/reinforcement; AE probability; motivation/dependence/NMRinteraction; generic linear/logistic/Cox/GLMM; ITTmissing=smoking and joint/pattern-mixture/prior/covariate sensitivities; IPW; posteriorbenefitthreshold>.90; N500simulationassumptions. Planned simulated tables are never observed-trial estimates.

Coverage gaps: none,45/45mapped. Derivative limitations: native formula extraction corrupts glyphs; p28-34source visual transcription above supplies printed symbols, indices/signs and labels. No OCR gap remains. Missing specifications are source facts rather than scientific-coverage gaps: exact randomization ratios/probabilities/IPWformula, normal/slowNMRcutoff, explicit pilot analytic inclusion, maximum lozenge count, fixed confounder list, numerical multiplicity/interim rule, operational joint/pattern-mixture settings. Referenced appendices (e.g. safety plan, counseling manuals, EMA algorithm) are pointers within these45pages; no separate appendix source unit exists in this assigned PDF. No conclusion about absence from the other supplied documents is made.

Counts:45pagecoverage rows;21numeric/contextualrecords PLAN-N001-N021;29statisticalrecords PLAN-S001-S029;2figures;4numberedtables (Table1,Table6,Table2,Table3) fully opened/mapped;12 direct CPU rendered pages;0fresh-requiredpages;0OCRpages;0Office/workbook/CSVunits;0unmappedpages. Quantitative historical context is retained separately in N020, not treated as prospective outcomes. COMPLETE_NA pages:1,2,40,41,42,43,44,45 (8); other37pages mapped with content.

Direct-source transcription note: p8 rendered source reads expired CO ≥6 ppm with parenthetical 'if ≤5, then positive cotinine test'. The reusable layout text loses the equality bar and gives '<5'; N004 and the coverage row use the source's ≤5. This is a derivative/source disagreement documented for transcription, without candidate diagnosis. Current direct-source SHA-256 was rechecked with sha256sum after mapping and remains eb73035cb7b875a25b3c955e6f730eb7f6ef88b711b3d18f0296ee3a857ed004.
