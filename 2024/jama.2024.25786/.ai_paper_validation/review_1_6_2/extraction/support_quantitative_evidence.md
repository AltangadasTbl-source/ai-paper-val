# Support quantitative evidence map — current protocol/SAP and report supplements

Status: COMPLETE. Runtime agent: /root/support_mapper; named role qc162_support_quantitative_mapper; run model gpt-6.1-sol; reasoning medium. Exact disjoint assigned scope: DOC-002 PDF pp.62–103 (42 pages), DOC-003 pp.1–26 (26 pages), DOC-004 pp.1–3 (3 pages), DOC-005 p.1 (1 page): 72 pages. DOC-002 pp.1–61 are owned by another mapper and are not extracted here. This map records evidence and relationships without diagnosing findings. Mapper-local SUP IDs identify complete groups; reviewers assign authoritative N/S inventories. There are 40 relationship groups below, including every source display and its underlying rows/cells preserved in the complete page transcription appendix.

Read completely: QUALITY_CONTROL_SCOPE.md; workflow_1_6_2/review_contract.md; workflow_1_6_2/settings.toml; source_inventory.md; source_coverage.md; evidence_asset_inventory.md; tooling_record.md. Source roles: DOC-002 PLAN (including prospective DMSC charter); DOC-003 REPORT; DOC-004 REPORT administrative; DOC-005 REPORT administrative. No supplied Office or workbook source exists; formulas/cached workbook values are not applicable. No old scientific conclusions were read.

## Provenance and fresh-required units

Reusable native text is .ai_paper_validation/preprocessed/DOC-002.txt (assigned pp.62–103 only), DOC-003.txt, DOC-004.txt and DOC-005.txt; legacy pypdf engine, version unrecorded. Table and eFigure spatial readings were checked visually against all thirteen inventoried full-page renders DOC-003-page-13.png through DOC-003-page-25.png. Historical render engine unrecorded. All source values, including unusual printed denominators and percentages, are retained without normalization. Native and image values agreed at these locations.

Fresh-required DOC-002 pp.75 and103: direct Poppler pdftotext 26.01.0 layout extraction plus pdftoppm 26.01.0 CPU render, 140 dpi, followed by direct visual inspection. Commands: `pdftotext -layout -f 75 -l 75 joi240147supp1_prod_1738701765.28701.pdf .ai_paper_validation/review_1_6_2/preprocessing/support-current/DOC-002-p075-layout.txt`; identical command with page103 and p103 output. Render commands: `pdftoppm -f 75 -l 75 -r 140 -singlefile -png joi240147supp1_prod_1738701765.28701.pdf .ai_paper_validation/review_1_6_2/preprocessing/support-current/DOC-002-p075`; identical command for103. PNG files have matching prefixes. Native/layout text omits both figures; the complete fresh visual transcriptions below close both gaps. No OCR needed; images legible. Compute device CPU; no fallback. Source and reused assets unchanged.

## Every-page applicability ledger

| Source | Page | Applicability / mapped content |
|---|---:|---|
| DOC-002 | 62 | Statistical design, power, missing data, analysis model, covariates, subgroups, population |
| DOC-002 | 63 | Major protocol violations and oxygen thresholds; drug accounting administrative remainder |
| DOC-002 | 64 | Safety definitions, monitoring window and first-event recording |
| DOC-002 | 65 | Safety reporting and follow-up completion; ethics administrative remainder |
| DOC-002 | 66 | Oxygen dose range and monitoring; historical pilot/background and publication timeline distinguished from trial results |
| DOC-002 | 67 | DMSC timing and statistical interim review; publication administrative remainder |
| DOC-002 | 68 | Charter v1.1, date24-Aug-2022; administrative cover opened, no result values |
| DOC-002 | 69 | Prospective interim assessments, sample fractions, timing and data structure |
| DOC-002 | 70 | Data coding, 2-by-2 summaries, stopping guidance and no-futility rule |
| DOC-002 | 71 | DMSC membership; opened, no applicable quantitative result |
| DOC-002 | 72 | Charter signatures/dates; opened, no applicable quantitative result |
| DOC-002 | 73 | Charter amendment, variable names and missing/pending codes |
| DOC-002 | 74 | Archiving/funding/change authorization; opened, no applicable statistical result |
| DOC-002 | 75 | Fresh visual extraction of participant and study-progress timelines |
| DOC-002 | 76 | References; opened, no applicable trial quantitative result |
| DOC-002 | 77 | References; opened, no applicable trial quantitative result |
| DOC-002 | 78 | Protocol change log and revised violation threshold |
| DOC-002 | 79 | Protocol change log and safety/DMSC amendments |
| DOC-002 | 80 | SAP1.0 date11-Jan-2023; no revisions; title/registration metadata |
| DOC-002 | 81 | Protocol1.8 link and signatures; opened, no applicable result values |
| DOC-002 | 82 | SAP abstract design, outcomes, model, sample size and interim timing |
| DOC-002 | 83 | Intervention dose/duration and composite objective |
| DOC-002 | 84 | Design, randomization, blinding and prospective approval |
| DOC-002 | 85 | Power inputs, superiority, stopping, final-analysis timing |
| DOC-002 | 86 | Two-sided inference/multiplicity, adherence and analysis populations |
| DOC-002 | 87 | Baseline summaries, no baseline tests, withdrawal/follow-up |
| DOC-002 | 88 | Primary/key secondary definitions and primary model, GEE/IPW |
| DOC-002 | 89 | Secondary/exploratory models, every subgroup, missingness and harms |
| DOC-002 | 90 | SAS9.4 |
| DOC-002 | 91 | Model/attrition rationale and FDR control |
| DOC-002 | 92 | Planned publication split of 30-day and long-term outcomes |
| DOC-002 | 93 | Recruitment status913 by11-Feb-2023; administrative status, no outcome results |
| DOC-002 | 94 | References; opened, no applicable trial quantitative result |
| DOC-002 | 95 | References; opened, no applicable trial quantitative result |
| DOC-002 | 96 | References; opened, no applicable trial quantitative result |
| DOC-002 | 97 | Baseline Table1 definitions and units |
| DOC-002 | 98 | Baseline Table1 continuation, AIS/ISS, intubation and vital-sign footnotes |
| DOC-002 | 99 | Intervention Table2 windows/units and violation definitions |
| DOC-002 | 100 | Primary/key secondary Table3 statuses, components and assessment |
| DOC-002 | 101 | Exploratory Table4 every row, window and exclusions |
| DOC-002 | 102 | Safety supplemental Table1 every row, classification and first-event rule |
| DOC-002 | 103 | Fresh visual extraction of planned CONSORT flow, placeholders and criteria |
| DOC-003 | 1 | Contents; opened, display inventory and status labels |
| DOC-003 | 2 | Contents; opened, no independent quantitative result |
| DOC-003 | 3 | Contents; opened, no independent quantitative result |
| DOC-003 | 4 | Personnel/assessors; opened, no applicable quantitative result |
| DOC-003 | 5 | DMSC/personnel and participating bases; administrative units opened |
| DOC-003 | 6 | Participating centers and minimum approximately400 activations/year; administrative |
| DOC-003 | 7 | Intervention measurement and primary/key secondary outcome definitions |
| DOC-003 | 8 | Pneumonia/VAP item-by-item criteria |
| DOC-003 | 9 | ARDS formula/thresholds and exploratory definitions |
| DOC-003 | 10 | Exploratory calculations, follow-up and harms definitions |
| DOC-003 | 11 | Harms monitoring, per-protocol criteria, deviations and missingness |
| DOC-003 | 12 | IPW predictors and primary missingness rule |
| DOC-003 | 13 | eFigure panelsA/B/C: visually mapped all trajectories, units, captions |
| DOC-003 | 14 | eTable1 all25 enrollment/receiving-center rows |
| DOC-003 | 15 | eTable2 all characteristic rows |
| DOC-003 | 16 | eTable3 all11 characteristic rows and classification footnotes |
| DOC-003 | 17 | eTable4 all3 outcome rows and all3 inferential model columns |
| DOC-003 | 18 | eTable5 all9 outcome rows and all3 inferential model columns |
| DOC-003 | 19 | eTable6 all6 outcome rows and all3 inferential model columns |
| DOC-003 | 20 | eTable7 all11 subgroup/all-patient rows with2 model columns |
| DOC-003 | 21 | eTable7 remaining2 rows and footnotes |
| DOC-003 | 22 | eTable8 all3 per-protocol outcome rows and all3 model columns |
| DOC-003 | 23 | eTable9 all7 safety rows and denominator explanation |
| DOC-003 | 24 | eTable10 both exclusion rows and missing-allocation footnote |
| DOC-003 | 25 | eTable11 all6 sensitivity rows, estimates, CIs andP |
| DOC-003 | 26 | References; opened, no applicable trial quantitative result |
| DOC-004 | 1 | Collaborators; opened, no applicable quantitative/statistical support |
| DOC-004 | 2 | Collaborators; opened, no applicable quantitative/statistical support |
| DOC-004 | 3 | Collaborators; opened, no applicable quantitative/statistical support |
| DOC-005 | 1 | Sharing statement; opened, six/12-month publication dependency and03-Jan-2026 availability; no trial quantitative/statistical result |

## Relationship register

Every group points to the exact supplied source via the page ledger and the appendix SOURCE PAGE headings. Main-paper matching keys are semantic identifiers, not invented values. Inferential estimates have restrictive versus liberal contrast; table columns retain source labels rather than being renamed crude/unadjusted. All printed95% CI andP columns remain distinct from multiplicity decisions.

| ID | Exact source location | Complete relationship / main-paper matching key |
|---|---|---|
| SUP001 | DOC-002 p62 | Protocol power and target: 710 per arm, 1420 evaluable, maximum 1600; 33% reduction, 80% power, 5% alpha, 15% liberal incidence. Historical pilot values separated below. Main sample-size methods. |
| SUP002 | DOC-002 pp62–63 | Protocol modified ITT excludes ISS=0; PP excludes at least one major violation; missingness below 5% uses complete cases, above 5% and not MCAR uses IPW; sensitivity assessment. Main analysis population. |
| SUP003 | DOC-002 p62 | Protocol logistic primary OR/95% CI adjusted for age, sex, center, intubation at randomization and admission pneumonia. Secondary categorical Fisher/chi-square and continuous competing-risk survival; 5% significance. Main statistical methods. |
| SUP004 | DOC-002 p62 | Protocol subgroups: intubation within one hour, ICU, TBI, COPD, hypoxemia, prehospital/in-hospital; ISS-adjusted analysis. Main Figure4 and subgroup methods. |
| SUP005 | DOC-002 pp63,86,99 | All four major-violation criteria: restrictive flow at least 3 L/min with SpO2 at least 98%, or FiO2 above .4 with same saturation; liberal flow below 3 or FiO2 below .4. Each requires two consecutive hourly records. Main PP/adherence. |
| SUP006 | DOC-002 pp64–65,102 | All safety categories, first-event recording, maximum 30 days; monitoring at first 24 hours then every third day; SAE/SAR/SUSAR distinctions. Main safety/eTable9. |
| SUP007 | DOC-002 pp67,69 | DMSC looks at 355 and 710 completed 30-day follow-ups, approximately 25% and 50%; notifications at 20% and 45%, data five days before meeting; first mortality, second mortality plus respiratory complications. Main interim methods. |
| SUP008 | DOC-002 pp69–70,73 | DMSC data: one row per patient; externally renamed allocation; mortality, pneumonia, ARDS coded 0/1/999/blank, with blank pending; allocation-stratified 2-by-2 tables; no other variables. Main monitoring and missingness. |
| SUP009 | DOC-002 p70 | No strict stopping criterion; suggested RR lower 95% CI above 2 for either numerator arm; no futility before 1420 complete follow-ups; steering committee decision. Main stopping methods. |
| SUP010 | DOC-002 p75 | Fresh participant timeline: intervention T0 to T8; 30-day mortality/pneumonia/ARDS; six-month EQ-5D-5L and GOSE; 12-month mortality, EQ-5D-5L, GOSE. Main intervention/outcome timing. |
| SUP011 | DOC-002 pp66,75 | Fresh study-progress timeline: spring2021 approvals, fall2021 first inclusion, spring2023 1420 with 30-day follow-up, fall2023 drafting, winter2024 submission. Administrative prospective calendar, retained separately. |
| SUP012 | DOC-002 pp78–81 | Complete version changes: v1.6 violations revised, v1.7 intubated restrictive threshold changes from at least .4 to above .4, v1.8 safety details and DMSC1.1. SAP1.0 Jan11,2023 has no revisions and links protocol1.8. |
| SUP013 | DOC-002 pp82–84 | SAP superiority design; 1:1 blocks4/6/8, including-center/base and intubation strata; eight-hour restrictive oxygen above21% to SpO2 94%, liberal12–15 L/min or FiO2 .6–1.0. Main design/intervention. |
| SUP014 | DOC-002 p85 | SAP power: 710 per arm including3.5% dropout, total1420; 15% versus10%, five percentage points, 33% relative reduction, 80% power, 5% alpha. Main sample-size methods. |
| SUP015 | DOC-002 pp85–86 | SAP interim and stopping guidance; final analysis30 days after final inclusion; two-sided5% tests and95% CI; exploratory BH lower significance level and FDR5%, with P and CI assessment. Main inference/multiplicity. |
| SUP016 | DOC-002 pp86–87 | SAP modified ITT excludes expected discharge below24 hours after secondary survey; PP only primary/key secondary; follow-up until withdrawal; baseline counts/percentages and medians/IQR, no baseline tests. Main population and summaries. |
| SUP017 | DOC-002 pp88,100 | Primary composite and two key secondary outcomes, all30 days; two blinded specialists; three contact attempts on different days; unreachable home-discharge patients considered alive; transfer without records has missing vital status. Main definitions. |
| SUP018 | DOC-002 pp88–89 | SAP primary logistic OR, strata adjustment; additional age/sex/ISS/first GCS; GEE including-base clustering; logistic observation-probability IPW from baseline and allocation; weighted GEE variance. Key secondary same; exploratory logistic/linear and BH. Main models. |
| SUP019 | DOC-002 p89 | Seven SAP primary subgroups: initially intubated within one hour, ICU, TBI AIS at least3, lung disease, hypoxemia below90%, inclusion location, ISS above15. Main Figure4/eTable7. |
| SUP020 | DOC-002 pp89–92 | Withdrawal observed event retained, absent event before withdrawal missing; IPW; SAS9.4; six/12-month follow-up separate SAP/publications; all30-day outcome statuses. Main missingness/status. |
| SUP021 | DOC-002 pp97–98 | Complete baseline Table1 dictionary: all variables, categories, units and footnotes, including GCS3–15, oxygen thresholds85%/90%, supraglottic airway as intubation, AIS/ISS. Main Patient Characteristics Table/eTables1–2. |
| SUP022 | DOC-002 p99 | Complete intervention Table2 dictionary: eight hourly medians, locations, oxygen delivery/units; ABG1 hour±30 minutes and6 hours±2 hours; PaO2, hemoglobin, lactate units; violations/deviations. Main oxygen/eTable3. |
| SUP023 | DOC-002 p101 | Complete exploratory Table4 dictionary: every surgery, ICU, neurologic, hypoxemic, ventilation, LOS, infection and intubation variable and window; every exclusion and footnote. Main Figure2/eTables5–6. |
| SUP024 | DOC-002 p103 | Fresh prospective CONSORT template: all placeholder counts, eligibility/exclusion criteria, secondary exclusion, allocation, withdrawal/lost follow-up, primary analysis. Main Figure1. |
| SUP025 | DOC-003 p7 | Report hourly intervention measures; missing sheet values approximated from records; high-flow cannula recorded as mask; ABG closest to prescribed1-hour and6-hour windows. Main oxygen methods. |
| SUP026 | DOC-003 pp7–9 | Report primary/key secondary definitions and ascertainment; complete CDC pneumonia/VAP criteria and Berlin ARDS thresholds/formula below. Main endpoints. |
| SUP027 | DOC-003 pp9–10 | Complete exploratory definitions: ventilation inclusion/exclusions, commenced-hour/day calculations and examples, transfer/discharge rules, postdischarge pneumonia ascertainment. Main Figure2/eTables5–6. |
| SUP028 | DOC-003 pp10–11 | Report safety first-event window/monitoring, all PP oxygen thresholds, documented clinical deviations. Main safety/adherence/eTables3,8,9. |
| SUP029 | DOC-003 pp11–12 | Report IPW and predictors: allocation, injury type, oxygen-supply type, psychiatric comorbidity, Danish personal/temporary ID; GEE variance; primary missingness after withdrawal without respiratory complication. Main methods. |
| SUP030 | DOC-003 p13 | Three-panel eFigure: all hour trajectories/IQR, units and caption; aggregate liberal/restrictive SpO2 100(99–100)/97(96–99), flow12(12–15)/0(0–1), FiO2 .60(.60–.80)/.28(.21–.36). Main oxygen narrative. |
| SUP031 | DOC-003 p14 | Complete eTable1: 20 enrollment and five receiving-center rows; N750/758, total1508; all counts, denominators, percentages below. Main Patient Characteristics Table. |
| SUP032 | DOC-003 p15 | Complete eTable2: every BMI, injury mechanism, transport, previous oxygen, saturation, temperature and surgery row; every printed denominator and percentage retained. Main baseline table. |
| SUP033 | DOC-003 p16 | Complete eTable3: 11 rows and all denominators, medians/IQR, percentages; eight-record category priority and ties, ABG windows, all footnotes. Main oxygen/adherence. |
| SUP034 | DOC-003 p17 | Complete eTable4: three outcomes, three model columns, nine OR/CI/P sets; all event counts/denominators/percentages; active-smoking definition. Main Figure2. |
| SUP035 | DOC-003 p18 | Complete eTable5: nine outcomes, 24 OR/CI/P sets plus MI dash cells; all counts/percentages/footnotes; multiplicity conclusion. Main Figure2 exploratory outcomes. |
| SUP036 | DOC-003 p19 | Complete eTable6: six outcomes, 18 mean-difference/CI/P sets; group medians/IQR/n, units and multiplicity conclusion. Main Figure2 exploratory outcomes. |
| SUP037 | DOC-003 pp20–21 | Complete eTable7: all-patient and12 subgroup rows,26 OR/CI sets; all count/percentage pairs; head-only AIS and ISS footnotes. Main Figure4. |
| SUP038 | DOC-003 p22 | Complete eTable8: three outcomes, nine OR/CI/P sets; PP N700/656, outcome denominators683/627 or685/629; every footnote. Main PP sensitivity. |
| SUP039 | DOC-003 pp23–24 | Complete eTables9–10: seven safety rows with full denominator explanation and no SAR/SUSAR; two exclusion rows, allocation counts/percentages, N130/341 and two missing allocations. Main Figure1/safety. |
| SUP040 | DOC-003 p25 | Complete eTable11: six missing-not-counted/missing-counted sensitivity rows, six OR/CI/P sets; every count/percentage, including printed135//750. Main sensitivity analysis. |

## Fresh visual extraction: DOC-002 p75

Figure1 Participant timeline: trauma → enrollment process → T0(hour0), intervention initiated → intervention → T8, intervention completed → follow-up. At30days: mortality, pneumonia andARDS. At6months: EQ-5D-5L andGOSE. At12months: mortality,EQ-5D-5L andGOSE. Figure2 Study progress: writingprotocol → spring2021 approvalapplications → approvalsreceived → fall2021firstpatient → inclusion → spring2023 1420patientswith30-dayfollow-upincluded → datamanagement → fall2023manuscriptdrafting → manuscriptdraftready → winter2024submissionprimarypaper. Timeline spacing is illustrative; exact quantitative dates/windows are labels above.

## Fresh visual extraction: DOC-002 p103

All n values are prospective placeholders, not observed participant totals. Assessment for eligibility following trauma-team activation(n=XXXX). Exclusion(n=XXXX): age<18years(n=XXX);secondarytransfer(n=XXX);suspicionCOintoxication(i=XXX);cardiacarrestbeforeoronadmission(n=XXX);expectedhospitalstay<24hours(n=XXX);otherdominatinginjurytype thanbluntorpenetrating(n=XXX);prolongedtimeintraumacentrebeforeinclusion>90min(n=XXX);traumateamactivationcancelled(n=XXX);missed(n=XXX);other(n=XXX). Totalrandomised(n=XXXX). Exclusionafterrandomisation(n=XXX):age<18,secondarytransfer,COsuspicion,cardiacarrest,previouslyincluded,other(e.g. unintended envelope opening; neutral paraphrase),eachn=XXX(exceptCOi=XXX). Secondaryexclusion(n=XXX):secondarysurveyrevealsno/minorinjuriesandexpecteddischarge<24hours(n=XXX). Totalincluded(n=XXXX). Allocation restrictive(n=XXX)/liberal(n=XXX). Eacharm excludedat30-dayfollow-up(n=XX),withdrawnorunobtainableconsent(n=XX),lost30-dayfollow-up(n=XX);eacharm includedprimaryanalysis(n=XXX). Text is transcribed as source flow content, with no numerical participant result implied.

## eFigure quantitative visual transcription: DOC-003 p13

PanelA SpO2(%): x=Pre,1,2,3,4,5,6,7,8hours; yaxis break to0,then93–100 in1-unit ticks. Restrictive median Pre97,H1 97,H2 98,H3–H8 97;IQR approximately Pre93–99,H1 95–100,H2 96–100,H3 96–99,H4 96–99,H5 96–99,H6 96–99,H7 95–99,H8 96–99. Liberal Pre97,H1–H8 100;IQR approximately Pre93–99,H1 100–100,H2 100–100,H3 99.75–100,H4 100–100,H5 99.5–100,H6–H8 99–100. Noninteger endpoints are graphical approximations, not printed numeric labels.

PanelB oxygenflow(L/min),H1–H8;axis0,3,6,9,12,15. Restrictivemedian0allhours,IQRH1 0–2,H2–H8 0–1. Liberalmedian15,13,12,12,12,12,12,12;IQRgraphapproximatelyH1 15–15,H2 12–15,H3–H4 10–15,H5–H6 10–13.25,H7–H8 5–12. Printedaggregate medians/IQR are liberal12(12–15),restrictive0(0–1).

PanelC FiO2,H1–H8;axis.21,.30,.40,.50,.60,.70,.80,.90,1.00. Restrictivemedianapproximately.32,.30,.29,.27,.25,.25,.25,.25;IQRapproximately.25–.45,.24–.40,.22–.39,.21–.36,.21–.35,.21–.35,.21–.35,.21–.34. Liberalmedianapproximately.98,.65,.60,.60,.60,.60,.60,.60;IQRapproximately.63–1.00,.60–.99,.60–.80,.60–.70,.60–.65,.60–.65,.60–.62,.60–.60. Printedaggregates liberal.60(.60–.80),restrictive.28(.21–.36). Caption definitions and numeric aggregate annotations are source printed; graphical endpoint approximations are clearly distinguished and do not pretend exact data recovery.

## Complete structured result tables for bounded checker reads

The following direct layout transcriptions preserve every row and column of eTables1–11, including all counts, denominators, percentages, medians/IQR/n, estimates, confidence intervals, P values, labels and footnotes. Source pages appear in order14,15,16,17,18,19,20,21,22,23,24,25; each printed page number is the exact PDF page. Restrictive precedes liberal. Inferential columns appear in source order: odds ratio or mean difference, P; adjusted measure, P; adjusted plus smoking, P. eTable7 has two OR/CI columns and no P column; eTable11 has one OR/CI/P column. These columns are labels in the supplied display; no inference that the first model is crude is introduced. The values were visually checked against all12 reusable full-page renders and freshly extracted using direct Poppler pdftotext26.01.0 CPU `-layout -f 14 -l 25`, output preprocessing/support-current/DOC-003-tables14-25-layout.txt. This section is the authoritative compact row/column map for SUP031–SUP040. Read this section together with SUP025–SUP030 and the plan register; the complete native appendix is retained for provenance and exhaustive page coverage.

```text
                                                                                                                  14


4.2 eTables

 eTable 1. Additional Characteristics of Patient Enrollment Location and
 Receiving Trauma Center
                                                                                 Restrictive        Liberal
 Characteristics                                                                oxygen group     oxygen group
                                                                                   (N=750)          (N=758)
 Enrollment location – no./total no. (%)
  Prehospital
    Physician staffed Critical Care Unit 1 and 2 – City:
                                                                                 62/750 (8.3)     68/758 (9.0)
    Copenhagen, Denmark
    Physician staffed Critical Care Unit 3 – South:
                                                                                 25/750 (3.3)     21/758 (2.8)
    Hvidovre, Denmark
    Physician staffed Critical Care Unit 4 – North:
                                                                                 25/750 (3.3)     26/758 (3.4)
    Hilleroed, Denmark
    Physician staffed Critical Care Unit 5 – Center: Herlev,
                                                                                 34/750 (4.5)     36/758 (4.7)
    Denmark
    Danish Air Ambulance Ringsted, Denmark                                       40/750 (5.3)     37/758 (4.9)
    Danish Air Ambulance Billund, Denmark                                        21/750 (2.8)     23/758 (3.0)
    Danish Air Ambulance Skive, Denmark                                          17/750 (2.3)     18/758 (2.4)
    Danish Air Ambulance Saltum, Denmark                                          2/750 (0.3)      2/758 (0.3)
    Physician staffed Critical Care Unit: Odense, Denmark                        38/750 (5.1)     39/758 (5.1)
    Physician staffed Critical Care Unit: Aarhus, Denmark                        13/750 (1.7)     13/758 (1.7)
    Physician staffed Critical Care Unit: Randers, Denmark                        1/750 (0.1)      0/758 (0.0)
    Lifeliner 2 Helicopter Emergency Medical Services
    (including a physician-staffed ambulance vehicle),                           5/750 (0.7)      3/758 (0.4)
    Rotterdam, The Netherlands
    REGA 3, Swiss-Air Ambulance, Bern, Switzerland                               19/750 (2.5)     16/758 (2.1)
    REGA 10, Swiss-Air Ambulance, Wilderswil,
                                                                                 3/750 (0.4)      3/758 (0.4)
    Switzerland
    REGA 14, Swiss-Air Ambulance, Zweisimmen,
                                                                                 3/750 (0.4)      2/758 (0.3)
    Switzerland
  In-hospital
    Rigshospitalet, Copenhagen University Hospital,
                                                                                150/750 (20.0)   160/758 (21.1)
    Denmark
    Odense University Hospital, Odense, Denmark                                 118/750 (15.7)   117/758 (15.4)
    Aarhus University Hospital, Aarhus, Denmark                                  62/750 (8.3)     58/758 (7.7)
    Erasmus MC, University Medical Center Rotterdam,
                                                                                87/750 (11.6)    90/758 (11.9)
    Rotterdam, The Netherlands
    University Hospital Bern, Switzerland                                        25/750 (3.3)     26/758 (3.4)
 Receiving trauma center – no./total no. (%) (N=1508)
  Rigshospitalet, Copenhagen University Hospital,
                                                                                335/750 (44.4)   348/758 (45.7)
  Denmark
  Odense University Hospital, Odense, Denmark                                   173/750 (22.9)   177/758 (23.2)
  Aarhus University Hospital, Aarhus, Denmark                                   100/750 (13.3)    93/758 (12.2)
  Erasmus MC, University Medical Center Rotterdam,
                                                                                92/750 (12.2)    93/758 (12.2)
  Rotterdam, The Netherlands
  University Hospital Bern, Switzerland                                          50/750 (7.2)     47/758 (6.7)

Trauma patients allocated to either a restrictive or liberal oxygen strategy.




© 2024 American Medical Association. All rights reserved.
                                                                                                                              15



 eTable 2. Additional Characteristics of Patients
                                                                                  Restrictive                  Liberal
 Characteristics                                                                oxygen group              oxygen group
                                                                                    (N=750)                   (N=758)
                                                                                25.0 (22.5-28.1)          25.0 (22.8-27.8)
 Body Mass Index – kg/m2
                                                                                    [n=628]                   [n=615]
 Mechanism of injury – no./total no. (%)
   Traffic: Motor vehicle accident                                               147/742 (19.8)            151/756 (20.0)
   Traffic: Motorcycle accident                                                   74/742 (10.0)             70/756 (9.3)
   Traffic: Bicycle accident                                                     109/742 (14.7)            108/756 (14.3)
   Traffic: Pedestrian                                                            53/742 (7.1)              50/756 (6.6)
   Traffic: Other (eg, ship, airplane, or railway train)                          14/742 (1.9)              19/756 (2.5)
   Shot by handgun, shotgun, rifle or other firearm of any
                                                                                   8/724 (1.1)               6/756 (0.8)
   caliber
   Stabbed by knife, sword, dagger, other pointed or sharp
                                                                                   69/742 (9.3)              68/756 (9.0)
   object
   Struck or hit by blunt object                                                  51/742 (6.9)               58/756 (7.7)
   Fall: 0-2 meters                                                               82/742 (11.1)              69/756 (9.1)
   Fall: 2-4 meters                                                               66/742 (8.9)               68/756 (9.0)
   Fall: >4 meters                                                                58/742 (7.8)               57/756 (7.5)
   Blast/explosion                                                                 3/742 (0.4)               4/756 (0.5)
   Other                                                                           8/742 (1.1)               28/756 (3.7)
 Type of transport to the trauma center – no./total no. (%)
   Ground ambulance                                                              583/747 (78.0)            585/743 (78.7)
   Helicopter ambulance                                                          140/747 (18.7)            141/743 (19.0)
   A combination of ground ambulance and helicopter
                                                                                   14/747 (1.9)              9/743 (1.2)
   ambulance
   Private vehicle                                                                 1/747 (0.1)               3/743 (0.4)
   Walk-in                                                                         9/747 (1.2)               4/743 (5.3)
   Other                                                                           0/747 (0.0)               1/743 (0.1)
 Use of prehospital or in-hospital supplemental oxygen
                                                                                 333/713 (46.7)            351/718 (48.9)
 prior to randomization – no./total no. (%)
                                                                                 100 (97-100)               99 (97-100)
    Highest SpO2 measured prior to randomization – %
                                                                                    [n=265]                   [n=285]
                                                                                36.5 (35.9-37.0)          36.5 (35.9-36.9)
 Body temperature measured on admission – o C
                                                                                    [n=479]                   [n=484]
 Surgery performed in the trauma resuscitation room
  Neurosurgery – no./total no. (%)                                                  3/744 (0.4)              1/747 (0.1)
  Cardiothoracic surgery – no./total no. (%)                                       10/744 (1.3)              9/747 (1.2)
  Abdominal surgery – no./total no. (%)                                             0/744 (0.0)              4/747 (0.5)
  Orthopedic surgery – no./total no. (%)                                            2/744 (0.3)              1/747 (0.1)
  Vascular surgery – no./total no. (%)                                              1/744 (0.1)              0/747 (1.1)
  Other(s) – no./total no. (%)                                                      1/744 (0.1)              1/747 (0.1)

Trauma patients allocated to either a restrictive or liberal oxygen strategy. Continuous variables are presented as median with
interquartile range.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                16



 eTable 3. Oxygen Intervention Characteristics
                                                                                   Restrictive                  Liberal
 Characteristic                                                                   oxygen group               oxygen group
                                                                                      (N=750)                   (N=758)
                                                                                    54 (35-79)                 52 (33-78)
 Time from trauma to randomization – min (N=1268)
                                                                                     [n = 633]                  [n=635]
 Type of supplemental oxygen* – no./total no. (%)
   No supplemental oxygen                                                          200/739 (27.1)             13/735 (1.8)
   Nasal cannula                                                                   171/739 (23.1)             45/735 (6.1)
   Non-rebreather mask                                                              18/739 (2.4)             340/735 (46.2)
   Intubated (at any point during the intervention period)                         350/739 (47.4)            337/735 (45.9)
                                                                                  12.9 (11.4-14.0)          12.7 (11.3-14.0)
 Hemoglobin hour 1 ± 30 min § – g/dL
                                                                                      [n=602]                   [n=603]
                                                                                  12.5 (10.8-13.7)          12.4 (10.6-13.9)
 Hemoglobin hour 6 ± 2 hours § – g/dL
                                                                                      [n=482]                   [n=487]
                                                                                    1.5 (0.9-2.5)             1.4 (0.9-2.4)
 Lactate hour 1 ± 30 min § – mmol/L
                                                                                      [n=585]                   [n=590]
                                                                                    1.4 (0.9-2.2)             1.4 (0.9-2.1)
 Lactate hour 6 ± 2 hours § – mmol/L
                                                                                      [n=472]                   [n=479]
 Major protocol violation ¶ – no./total no. (%)                                     50/742 (6.7)             102/744 (13.7)
 Protocol deviation † – no./total no. (%)                                           40/741 (5.4)              17/738 (2.3)

Trauma patients allocated to either a restrictive or liberal oxygen strategy. The time from trauma to randomization is presen ted
with a median and interquartile range.
* The data collection sheet consisted of eight hourly data points (H1-H8). The sum of no supplemental oxygen, nasal cannula,
non-rebreather mask or intubated is 100%. Patients are in the no supplemental oxygen category if none of the eight data points
were nasal cannula, non-rebreather mask or intubated. If just one of the eight data points was intubated, the patient was
categorized as intubated. Patients could receive both supplemental oxygen via a nasal cannula and non -rebreather mask
during the 8-hour intervention period at different time points and were registered in the appropriate category based on the
majority of the data points from the sheet. In case they were evenly distributed, the patient was registered in the non -rebreather
mask category.
§ The 1st and 2nd arterial blood gases during the oxygen intervention were obtained at hour 1 ± 30 min after randomization and
hour 6 ± 2 hours after randomization, respectively.
¶ See page 10 for definitions of major protocol violations.
† See page 10 for definition of protocol deviations.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                      17



 eTable 4. Primary and Key Secondary Outcomes

                                         Restrictive            Liberal                                                                                           Adjusted odds
                                                                                     Odds ratio                           Adjusted odds
                                          oxygen                oxygen                                     P value                                 P value       ratio + smoking          P value
                                                                                      (95% CI)                            ratio (95% CI)
                                           group                group                                                                                                (95% CI)
 Primary outcome
 Death and/or major
                                           118/733             121/724                  1.01                                   0.98                                    1.05
 respiratory complications –                                                                                 0.94                                    0.92                                   0.80
                                            (16.1)              (16.7)              (0.75 to 1.37)                         (0.68 to 1.41)                          (0.73 to 1.49)
 no./total no. (%)
 Key secondary outcomes
                                                                                        1.28                                   1.37                                    1.37
 Death – no./total no. (%)              63/733 (8.6)         53/724 (7.3)                                    0.23                                    0.25                                   0.26
                                                                                    (0.85 to 1.92)                         (0.80 to 2.38)                          (0.80 to 2.33)
 Major respiratory
                                                                                        0.84                                   0.84                                    0.90
 complications – no./total              65/733 (8.9)        78/724 (10.8)                                    0.33                                    0.38                                   0.58
                                                                                    (0.59 to 1.19)                         (0.57 to 1.23)                          (0.61 to 1.32)
 no. (%)

Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. Death and major respiratory complications were both evaluated within 30 days. The smoking variable
reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                          18



 eTable 5. Categorical Exploratory Outcomes

                                          Restrictive            Liberal                                                                                              Adjusted odds
                                                                                       Odds ratio                            Adjusted odds
                                           oxygen                oxygen                                       P value                                  P value       ratio + smoking           P value
                                                                                        (95% CI)                             ratio (95% CI)
                                            group                group                                                                                                   (95% CI)
 Presence of any
                                                                                          1.67                                     1.72                                    1.69
 hypoxemic episodes (SpO2                44/737 (6.0)         28/737 (3.8)                                      0.04                                     0.03                                    0.04
                                                                                      (1.02 to 2.70)                           (1.04 to 2.78)                          (1.04 to 2.78)
 <90%) * – no./total no. (%)
 ICU re-admission(s) –                                                                    0.59                                     0.60                                    0.57
                                         17/368 (4.6)         18/352 (5.1)                                      0.22                                     0.25                                    0.19
 no./total no. (%) †                                                                  (0.26 to 1.37)                           (0.25 to 1.43)                          (0.25 to 1.32)
 Sepsis during hospital
                                                                                          0.55                                     0.53                                    0.52
 admission – no./total no.               19/736 (2.6)         31/727 (4.3)                                      0.06                                     0.05                                    0.05
                                                                                      (0.30 to 1.02)                           (0.29 to 1.00)                          (0.27 to 1.00)
 (%)
 Surgical site infection(s)
                                                                                          0.50                                     0.49                                    0.51
 within 30 days – no./total              23/736 (3.1)         32/724 (4.4)                                      0.05                                     0.03                                    0.04
                                                                                      (0.25 to 0.99)                           (0.26 to 0.93)                          (0.27 to 0.96)
 no. (%)
 Pneumonia post-discharge
 within 30 days after                                                                     1.06                                     1.04                                    1.03
                                         27/640 (4.2)         24/620 (3.9)                                      0.86                                     0.89                                    0.93
 enrollment ¶ – no./total no.                                                         (0.60 to 1.85)                           (0.59 to 1.85)                          (0.57 to 1.85)
 (%)
 Brain injury within 7 days of
                                            290/738              275/732                  1.11                                     1.05                                    1.04
 admission – no./total no.                                                                                      0.35                                     0.68                                    0.74
                                             (39.3)               (37.6)              (0.88 to 1.41)                           (0.82 to 1.35)                          (0.81 to 1.33)
 (%)
 Myocardial infarction within
                                          0/738 (0.0)          1/730 (0.1)                    -                    -                   -                    -                   -                   -
 7 days – no./total no. (%)
 Cerebral ischemia within 7                                                               1.56                                     1.45                                    1.47
                                         16/738 (2.2)         10/730 (1.4)                                      0.30                                     0.38                                    0.36
 days – no./total no. (%)                                                             (0.68 to 3.57)                           (0.63 to 3.45)                          (0.64 to 3.45)
 ICU admission – no./total                  374/738              359/736                  1.16                                     1.01                                    1.01
                                                                                                                0.24                                     0.95                                    0.95
 no. (%)                                     (50.7)               (48.8)              (0.90 to 1.49)                           (0.76 to 1.33)                          (0.76 to 1.33)

Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. No exploratory outcomes were statistically significant between the groups after adjusting for multiple
testing. The smoking variable reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients.
* Defined as any hypoxemic episodes (SpO2 <90%) during the eight-hour intervention from the hourly collected SpO2 values.
† ICU: Intensive care unit.
¶ Only patients discharged within 30 days were eligible for evaluation of pneumonia post-discharge.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                       19



 eTable 6. Continuous Exploratory Outcomes
                                                                                                                                                                   Adjusted mean
                                         Restrictive            Liberal                                                    Adjusted mean
                                                                                  Mean difference                                                                   difference +
                                          oxygen                oxygen                                      P value          difference              P value                                P value
                                                                                     (95% CI)                                                                         smoking
                                           group                group                                                         (95% CI)
                                                                                                                                                                      (95% CI)
 Initial surgery duration after
                                        114 (64-166)         113 (68-149)                 10.3                                    12.6                                    15.4
 trauma resuscitation room                                                                                     0.29                                    0.22                                   0.13
                                          [n=165]              [n=161]               (-8.8 to 29.3)                          (-7.4 to 32.6)                          (-4.3 to 35.0)
 treatment – min
 Time on mechanical                        0 (0-14)             0 (0-12)                  4.8                                     3.3                                     3.7
                                                                                                               0.45                                    0.59                                   0.54
 ventilation – hours                       [n=735]              [n=725]              (-7.6 to 17.2)                          (-8.7 to 15.2)                          (-8.1 to 15.6)
 Days alive without
                                          30 (29-30)           30 (29-30)                 -0.6                                    -0.4                                    -0.5
 mechanical ventilation –                                                                                      0.16                                    0.27                                   0.20
                                           [n=735]              [n=723]               (-1.4 to 0.2)                           (-1.1 to 0.3)                           (-1.2 to 0.2)
 days
 Intensive Care Unit Length                  2 (1-9)             2 (1-7)                   1.1                                     1.0                                     1.0
                                                                                                               0.10                                    0.17                                   0.16
 of Stay – days                             [n=368]             [n=357]               (-0.2 to 2.5)                           (-0.4 to 2.3)                           (-0.4 to 2.5)
 Days alive outside the
                                          29 (26-30)           30 (27-30)                 -0.8                                    -0.5                                    -0.6
 Intensive Care Unit within                                                                                    0.09                                    0.17                                   0.12
                                           [n=736]              [n=724]               (-1.7 to 0.1)                           (-1.3 to 0.2)                           (-1.3 to 0.2)
 30 days – days
 Hospital Length of Stay –                 7 (3-15)             7 (3-15)                  -0.7                                    -1.0                                    -1.0
                                                                                                               0.41                                    0.23                                   0.23
 days                                      [n=736]              [n=728]               (-2.3 to 0.9)                           (-2.3 to 0.6)                           (-2.5 to 0.6)

Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. All continuous variables are presented as medians with interquartile ranges in the group allocation
columns. No exploratory outcomes were statistically significant between the groups after adjusting for multiple testing. The smoking variable reflects only active smokers, identified from medical
records and, in some cases, confirmed directly with patients.
* Patients still admitted at day 30 were not eligible for evaluation of pneumonia post-discharge.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                   20



 eTable 7. Adjusted Subgroup Analyses
                                                   Restrictive                  Liberal
                                                                                              Odds ratio (95% CI)   Adjusted odds ratio (95% CI)
                                                  oxygen group              oxygen group
                                                    no. of events/total no. of patients (%)
                                                                                                     1.01                      0.98
 All patients                                     118/733 (16.1)           121/724 (16.7)
                                                                                                 (0.75 to 1.37)            (0.68 to 1.39)
 Intubated at randomization
                                                                                                     1.12                      1.16
   No                                             56/558 (10.0)              50/543 (9.2)
                                                                                                 (0.75 to 1.67)            (0.73 to 1.85)
                                                                                                     0.90                      0.76
   Yes                                            62/175 (35.4)             71/181 (39.2)
                                                                                                 (0.57 to 1.41)            (0.45 to 1.30)
 ICU admission
                                                                                                     0.98                      0.89
   No                                              42/458 (9.2)             50/481 (10.4)
                                                                                                 (0.64 to 1.49)            (0.56 to 1.43)
                                                                                                     0.96                      0.98
   Yes                                            74/271 (27.3)             68/238 (28.6)
                                                                                                 (0.63 to 1.49)            (0.58 to 1.67)
 Moderate or severe traumatic brain
 injury *
                                                                                                     1.06                      1.11
   AIS < 3                                         45/500 (9.0)              48/473 (9.2)
                                                                                                 (0.68 to 1.64)            (0.68 to 1.85)
                                                                                                     0.81                      0.83
   AIS ≥ 3                                        73/233 (31.3)             73/202 (36.1)
                                                                                                 (0.53 to 1.25)            (0.51 to 1.37)
 Known lung disease
                                                                                                     0.88                      0.95
   No                                             97/667 (14.5)            105/643 (16.3)
                                                                                                 (0.65 to 1.22)            (0.65 to 1.39)
                                                                                                     1.85                      1.06
   Yes                                             19/59 (32.2)              14/69 (20.2)
                                                                                                 (0.73 to 4.55)            (0.40 to 2.86)
 Site of inclusion
                                                                                                     0.81                      0.95
   Prehospital                                    48/303 (15.8)             54/296 (18.2)
                                                                                                 (0.51 to 1.28)            (0.55 to 1.64)
                                                                                                     1.19                      0.98
   In-hospital                                    70/430 (16.3)             67/428 (15.7)
                                                                                                 (0.81 to 1.79)            (0.63 to 1.52)
 Injury severity score †




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                         21


                                                           Restrictive                  Liberal
                                                                                                                        Odds ratio (95% CI)               Adjusted odds ratio (95% CI)
                                                          oxygen group              oxygen group
                                                            no. of events/total no. of patients (%)
                                                                                                                                 1.33                                   1.14
   ISS ≤ 15                                                 22/380 (5.8)                  19/389 (4.9)
                                                                                                                             (0.69 to 2.56)                         (0.56 to 2.33)
                                                                                                                                 0.86                                   0.93
   ISS > 15                                                95/352 (27.0)                 100/329 (30.4)
                                                                                                                             (0.60 to 1.23)                         (0.62 to 1.40)

Adjusted subgroup analyses for trauma patients allocated to either a restrictive or liberal oxygen strategy.
* Moderate or severe traumatic brain injury was evaluated by a score of 3 or higher on the AIS (Abbreviated Injury Scale) from the head/neck codes, but only head codes were selected.
† Injury Severity Score: ISS.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                                                                                    22



 eTable 8. Per-Protocol Analyses of Primary and Key Secondary Outcomes ¶
                                        Restrictive            Liberal
                                                                                                                                                                  Adjusted odds
                                         oxygen                oxygen                Odds ratio                           Adjusted odds                                                       P
                                                                                                           P value                                 P value       ratio + smoking
                                          group                 group                 (95% CI)                            ratio (95% CI)                                                    value
                                                                                                                                                                     (95% CI)
                                         (N=700)               (N=656)
 Primary outcome
 Death and/or major
                                           104/683             105/627                 0.98                                    0.97                                    1.04
 respiratory complications –                                                                                 0.91                                    0.87                                   0.83
                                            (15.2)              (16.7)             (0.71 to 1.35)                          (0.67 to 1.41)                          (0.71 to 1.52)
 no./total no. (%)
 Key secondary outcomes
                                                                                       1.27                                    1.25                                    1.22
 Death – no./total no. (%)              54/683 (7.9)        44/627 (7.0)                                     0.29                                    0.45                                   0.49
                                                                                   (0.82 to 2.00)                          (0.70 to 2.22)                          (0.69 to 2.17)
 Major respiratory
                                                                                       0.78                                    0.82                                    0.89
 complications – no./total              58/685 (8.5)        69/629 (11.0)                                    0.20                                    0.34                                   0.58
                                                                                   (0.54 to 1.14)                          (0.54 to 1.23)                          (0.59 to 1.33)
 no. (%)

Per-protocol analyses of trauma patients allocated to either a restrictive or liberal oxygen strategy. Death and major respiratory complications were both evaluated within 30 days. The smoking
variable reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients.
¶ See page 10 for definitions of major protocol violations.




© 2024 American Medical Association. All rights reserved.
                                                                                                                                 23



 eTable 9. Adverse Events (AE) and Serious Adverse Events (SAE) ¶
                                                                                   Restrictive                 Liberal
                                                                                  oxygen group             oxygen group
                                                                                     (N=750)                  (N=758)
 Adverse event (AE) – no./total no. (%)
  Atelectasis                                                                     207/750 (27.6)           263/758 (34.7)
  Irritability of airway mucosa                                                    16/750 (2.1)             20/758 (2.6)
 Serious adverse event (SAE) – no./total no. (%)
  Death                                                                             63/750 (8.4)             53/758 (7.0)
  Was life-threatening                                                              8/750 (1.1)              13/758 (1.7)
  Involved or prolonged hospital length of stay                                     29/750 (3.9)             37/758 (4.9)
  Involved persistence of significant disability or incapacity                      0/750 (0.0)              0/758 (0.0)
  Resulted in a congenital anomaly or birth defect                                  0/750 (0.0)              1/758 (0.1)

¶ See page 9 for the definitions of AE and SAE registration. There is a difference in the denominator of the patients for both
groups compared to the outcome tables because patients were observed for AEs and SAEs up until a potential consent
withdrawal. In case consent was withdrawn and no event was registered, the patient was registered as having no events and
included in this table. No Serious Adverse Reactions (SAR) or Suspected Unexpected Serious Adverse Reactions (SUSAR)
were registered.




© 2024 American Medical Association. All rights reserved.
                                                                                                                         24



 eTable 10. Distribution of Oxygen Interventions Among the Post-
 Randomization Excluded Patients ¶
                                                                                Restrictive                Liberal
                                                                               oxygen group            oxygen group
                                                                                  (N=750)                 (N=758)
 Exclusion after randomization – no./total no. (%) (N=130)                       55/750 (45)             67/758 (55)
 Secondary exclusion – no./total no. (%) (N=341) *                              174/750 (51)            165/758 (49)

¶ Detailed numbers on the post-randomization excluded patients from Figure 1 in the main manuscript.
* Two patients had missing data on the randomized oxygen intervention, which is the reason for the discrepancy between
N=341 and the numbers in the table.




© 2024 American Medical Association. All rights reserved.
                                                                                               25



 eTable 11. Best/Worst Case Scenario: Primary and Key Secondary Outcomes
                                   Restrictive          Liberal        Odds ratio
                                                                                       P value
                                  oxygen group       oxygen group       (95% CI)
 Primary outcome
 Missing not counted as
 event: Death and/or major                                                0.99
                                  118/750 (15.7)     121/758 (16.0)                     0.96
 respiratory complications –                                          (0.74 to 1.33)
 no./total no. (%)
 Missing counted as event:
 Death and/or major                                                       0.85
                                  135//750 (18.0)    155/758 (20.4)                     0.24
 respiratory complications –                                          (0.65 to 1.11)
 no./total no. (%)
 Key secondary outcomes
 Missing not counted as
                                                                          1.28
 event: Death – no./total no.      63/750 (8.4)        53/758 (7.0)                     0.22
                                                                      (0.86 to 1.92)
 (%)
 Missing counted as event:                                                0.93
                                   80/750 (10.7)      87/758 (11.4)                     0.70
 Death – no./total no. (%)                                            (0.68 to 1.30)
 Missing not counted as
 event: Major respiratory                                                 0.82
                                   65/750 (8.7)       78/758 (10.3)                     0.26
 complications – no./total                                            (0.57 to 1.16)
 no. (%)
 Missing counted as event:
 Major respiratory                                                        0.70
                                   82/750 (10.9)     112/758 (14.8)                     0.02
 complications – no./total                                            (0.52 to 0.95)
 no. (%)




© 2024 American Medical Association. All rights reserved.
```


## Exact main-paper matching locations supplied by the main mapper

These are cross-reference keys supplied by the disjoint main mapper, not an independent extraction of an unassigned source. Main source is jama_arleth_2024_oi_240147_1738701765.27201.pdf. Patient Characteristics Table is on source p.4, including its continued PaO2 panel. Primary, key secondary and exploratory outcomes are in Figure2 on source p.6. Oxygen exposure narrative is on pp.5–6. Kaplan–Meier Figure3 is on p.7. Primary-outcome subgroups are in Figure4 on p.8. Statistical Analysis is on p.5; outcome definitions on pp.4–5; intervention methods on pp.2–4. The register's semantic 'Main Table2' outcome keys refer to Figure2; its semantic baseline Table1 key refers to the Patient Characteristics Table. These exact source locations govern downstream matching.

Evidence links: [protocol/SAP power](../../../joi240147supp1_prod_1738701765.28701.pdf#page=85), [SAP inference and populations](../../../joi240147supp1_prod_1738701765.28701.pdf#page=86), [SAP primary analysis](../../../joi240147supp1_prod_1738701765.28701.pdf#page=88), [SAP subgroup and missingness](../../../joi240147supp1_prod_1738701765.28701.pdf#page=89), [DMSC stopping guidance](../../../joi240147supp1_prod_1738701765.28701.pdf#page=70), [fresh timeline](../../../joi240147supp1_prod_1738701765.28701.pdf#page=75), [fresh prospective flow](../../../joi240147supp1_prod_1738701765.28701.pdf#page=103), [report missing-data method](../../../joi240147supp2_prod_1738701765.29201.pdf#page=12), [eFigure](../../../joi240147supp2_prod_1738701765.29201.pdf#page=13), [eTable1](../../../joi240147supp2_prod_1738701765.29201.pdf#page=14), [eTable2](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15), [eTable3](../../../joi240147supp2_prod_1738701765.29201.pdf#page=16), [eTable4](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17), [eTable5](../../../joi240147supp2_prod_1738701765.29201.pdf#page=18), [eTable6](../../../joi240147supp2_prod_1738701765.29201.pdf#page=19), [eTable7 first page](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), [eTable7 continuation](../../../joi240147supp2_prod_1738701765.29201.pdf#page=21), [eTable8](../../../joi240147supp2_prod_1738701765.29201.pdf#page=22), [eTable9](../../../joi240147supp2_prod_1738701765.29201.pdf#page=23), [eTable10](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24), [eTable11](../../../joi240147supp2_prod_1738701765.29201.pdf#page=25).

Count basis: 72 unique assigned pages; 40 complete mapper-local relationship groups; 11 result tables occupying12 pages; one three-panel result figure; two fresh plan pages containing three figures. Inferential result sets: eTable4=9; eTable5=24 printed sets plus three dash-only myocardial-infarction model cells; eTable6=18; eTable7=26; eTable8=9; eTable11=6; total92 printed estimate/interval sets,66 also with printed P values. No scientific coverage gaps.

## Complete assigned native transcription appendix

The following is the complete page-delimited assigned-source transcription, not selected excerpts. Every table cell, footnote, statistical definition, outcome status, numeric administrative item and reference is retained for exhaustive downstream checking. Image-only content is supplemented above. Page markers refer to the original PDFs; use package-relative source paths ending #page=N. DOC-002: joi240147supp1_prod_1738701765.28701.pdf; DOC-003: joi240147supp2_prod_1738701765.29201.pdf; DOC-004: joi240147supp3_prod_1738701765.30201.pdf; DOC-005: joi240147supp4_prod_1738701765.30701.pdf. Formatting is native transcription; column associations were visually checked for all results displays.

### DOC-002 PLAN pp62–103

```text
===== SOURCE PAGE 62 =====
 
62 
 
 
3.8 Statistical analysis 
In TRAUMOX1, the primary combined endpoint occurred in 20% in the restrictive group and 33% in the 
liberal group. In larger studies, mortality from trauma has been estimated to be around 6-12%24, and the 
incidence for ventilator associated pneumonia post trauma to be almost 30%13. With 710 trial participants in 
each arm, we will be able to detect a 33% risk reduction with a restrictive supplemental oxygen strategy 
(with 80% power at the 5% significance level) if the incidence of our primary outcome is 15% in the liberal 
group. Our primary analysis will be a modified intention-to-treat analysis, but a per-protocol analysis will 
also be carried out. A detailed statistical analysis plan, including the pre-specified subgroup analyses, will be 
made. In the primary analysis, we will exclude trial participants where no injuries are found defined as ISS = 
0. 
 
If less than 5% of data required for any specific analysis on primary or secondary outcomes are missing, a 
complete case analysis will be performed. If more than 5% are missing, and it is concluded that data are not 
‘missing completely at random’ (MCAR criterion),
25 inverse probability weighting will be used to correct 
this bias. A sensitivity analysis on the assumptions used for missing data will be done to verify robustness.  
 
Inclusion of trial participants will end when the goal of 1420 evaluable trial participants has been reached 
including the 30-day follow up period. This means that the maximum number of trial participants will be 
1600 as inclusion will continue during evaluation of the 30-day follow-up. EQ-5D-5L score and GOSE score 
at 6 months and 12 months will be obtained. Mortality at 30 days and 12 months will also be obtained. The 
primary composite outcome will be compared between the two groups using logistic regression reported as 
Odds Ratio (OR) with 95% CI. The primary analysis will be adjusted for age, sex, centre, intubated at 
randomisation (yes/no), and known pneumonia on admission (under treatment). Secondary outcomes will 
also be compared between the two groups using Fisher’s exact test/Chi2 test for categorical data and 
competing risk survival analyses for continuous data. We will use a 5% significance level. Any changes or 
additional analyses will be reported.  
 
In the per-protocol analysis, all trial participants with ≥1 major protocol violation will be removed. Please 
see section 3.8.1 for definitions of major protocol violations.  
 
Pre-specified subgroup analyses will be made on trial participants initially intubated (within one hour of the 
accident) (yes/no), trial participants with ICU admission (yes/no), trial participants with moderate and severe 
traumatic brain injuries (yes/no), trial participants with chronic obstructive pulmonary disease (yes/no), 
episodes with hypoxaemia as well as an analysis on trial participants enrolled prehospital versus in-hospital. 
An analysis adjusted for Injury Severity Score will also be conducted. 
 
The statistical analysis will be performed by a biostatistician.  
 
3.8.1 Major protocol violations 
A major protocol violation will be defined as: 
 
x Restrictive O2 group: during the intervention period 
 
===== SOURCE PAGE 63 =====
 
63 
 
- For non-intubated trial participants: Supplemental oxygen ≥3 L O2/min and having an SpO2 ≥98% 
recorded in two consecutive hourly values in the data collection sheet: “Randomisation, data 
collection sheet and REDCap inclusion” 
 
- For intubated trial participants: FiO2 >0.4 and having an SpO2 ≥98% recorded in two consecutive 
hourly values in the data collection sheet: “Randomisation, data collection sheet and REDCap 
inclusion” 
 
x Liberal O2 group: during the intervention period 
 
- For non-intubated trial participants: Supplemental oxygen <3 L O2/min in two consecutive hourly 
values in the data collection sheet: “Randomisation, data collection sheet and REDCap inclusion” 
 
- For intubated trial participants: FiO2 <0.4 in two consecutive hourly values in the data collection 
sheet: “Randomisation, data collection sheet and REDCap inclusion” 
 
 
4. Drug management and accounting 
4.1 Drug management 
The investigated drug will be handled by the usual providers: Air Liquide A/S, Strandmøllen A/S and Linde 
Gas A/S. 
 
4.2 Drug accounting 
As the consumption of the trial medicine, oxygen, is continuous in all prehospital and intrahospital units, the 
providers (Strandmøllen A/S, Linde Gas A/S and Air Liquide A/S) will register batch numbers and 
expiration dates as usual. Detailed accounting and registration of the drugs will not be possible, as oxygen 
runs through central pipelines and thus cannot be tracked on an individual trial participant level. However, 
we foresee no possible complications or risks beyond the existing, which will be entirely unrelated to this 
study. Any potential problems with the delivery will not affect the enrolled trial participants any further than 
it would were they not enrolled in the study. No other methods to study oxygen at our institution are 
possible. Therefore, appendix 12 (“Produktresuméer for oxygen ved Air Liquide, Strandmøllen og Linde 
Gas, kryogen og komprimeret”) will be the most detailed available source of drug accounting and thus serve 
as the primary source. 
 
 
5. Safety management 
5.1 Definitions 
The following definitions will be used26: 
 
x Adverse Event (AE): Any untoward medical occurrence in a subject to whom a medicinal product is 
adminsitered and which does not necessarily have a causal relationship with this treatment. 
 
===== SOURCE PAGE 64 =====
 
64 
 
x Serious Adverse Event (SAE): Any untoward medical occurrence that at any dose requires inpatient 
hospitalisation or prolongation of existing hospitalisation, results in persistent or significant 
disability or incapacity, results in a congenital anomaly or birth defect, is life-threatening, or results 
in death. 
 
x Suspected Unexpected Serious Adverse Reaction (SUSAR): A suspected, serious adverse reaction, 
the nature, severity or outcome of which is not consistent with the reference safety information.  
 
5.2 Tracking of events 
The local investigators at each centre is responsible for recording the different types of AEs and SAEs in the 
trial participant’s Case Report Form in REDCap. The specific investigator will assess the correlation 
between an event and trial medicine using the following AE/SAE event policy: 
x 1: Unrelated – No temporal context; other etiologies are more likely to be the cause 
x 2: Possible related – Less clear connection; other etiologies are also possible 
x 3: Probably related – Clear temporal correlation with medication discontinuation, and not reasonably 
explained by the known clinical condition of the subject 
x 4: Related – Clear temporal relationship with rehabilitation test or clinical assessment 
 
To monitor AEs and SAEs, a TRAUMOX2 investigator will assess the trial participant’s medical record: 
x Once within the first 24 hours 
x Every third day until discharge (maximum of 30 days) 
 
5.3 Adverse Events and Serious Adverse Events 
This group of trial participants are expected to have a lot of complications. It is the established practice in 
trials on critically ill patients that adverse events are part of the natural trajectory of the primary disease 
process or expected complications of the critical illness.27  
 
Therefore, we have chosen to record only the following AEs:  
x Atelectasis (only atelectases assessed by a radiologist are recorded) 
x Irritability of airway mucosa (recorded only if registered by the health care staff in the medical 
record) 
 
Only the first AE of either atelectasis or irritability of airway mucosa will be recorded during admission (not 
a subsequent). 
 
We will register all SAEs. The registration will be done in REDCap and once a SAE registration is complete, 
the sponsor and coordinating investigator will receive an e-mail notification within 24 hours via the REDCap 
notification e-mail system. Thus, the law on immediate notifying (within 24 hours after it has come to an 
investigator’s knowledge) the sponsor about SAEs is being followed. 
 
5.4 Suspected Unexpected Serious Adverse Reactions 
All potential SUSARs will be reported to the sponsor within 24 hours of discovery. If the sponsor believes 
that a trial participant has a SUSAR which results in death or is in a life-threatening condition, it will be 
reported as soon as possible to the Danish Medicines Agency and The Committee on Health Research Ethics 
and no later than 7 days after it has come to sponsor’s knowledge. No later than 8 days after the report (15 
===== SOURCE PAGE 65 =====
 
65 
 
days in total), sponsor must inform the mentioned authorities about all relevant information on the follow-up 
of the SUSAR. All other trial participants that have a SUSAR that do not result in death or in life-threatening 
conditions must be reported no later than 15 days after sponsor has been made aware of these. 
 
5.5 Reporting 
Once a year, a report with all SUSARs will be sent to The Danish Medicines Agency and The Committee on 
Health Research Ethics.   
 
After the last trial participant, last visit (1420 trial participants with a complete 30-day, 6- and 12-month 
follow-up), the end of the trial will be reported within 90 days to the relevant authorities or according to 
national law. All events, reactions and results of the study will be reported to the EudraCT database results 
within a year after termination of the study. 
 
 
6. Study administration 
6.1 Ethics and dissemination 
Trial participant insurances will be in place at all trial centres either through the national health insurance or 
through specifically supplied local trial insurances as required according to the specific trial centres and 
national regulations. 
 
This RCT will be conducted in compliance with the published trial protocol, the Helsinki Declaration in its 
latest version,
28 the Good Clinical Practice (GCP) guidelines29 and national laws in the participating 
countries. The protocol will be sent to the Danish Committee on Health Research Ethics for the Capital 
Region of Denmark and The Danish Medicines Agency. It will be monitored by the regional Good Clinical 
Practice Unit. Data management must be approved according to national legislation. We have written the 
protocol in accordance with the SPIRIT 2013 Statement19 and will register the trial in the 
www.clinicaltrials.gov and European Union Drug Regulating Authorities Clinical Trials (EudraCT) 
registries before the enrolment of the first trial participant. No substantial deviation from the protocol will be 
implemented without prior review and approval of the regulatory authorities except where it may be 
necessary to eliminate an immediate hazard to the trial participants. In such case, the deviation will be 
reported to the authorities as soon as possible. 
 
As stated in section 3.4.2 regarding consent procedures in Denmark, the trial participants in this study are 
considered temporarily incompetent because of the acute and severe condition related to their traumatic 
injuries. Symptoms will include severe pain, impaired consciousness, and early complications are circulatory 
and respiratory failure requiring emergency intubation. Some of these trial participants are expected to die. 
Current practice is that supplemental oxygen is administered as soon as possible after trauma often 
prehospitally. Thus, the intervention tested in this trial is pivotal to be given immediately in the early phase 
after trauma. Furthermore, it is stated above that a liberal supplemental oxygen strategy may be detrimental 
and should be avoided as soon as possible. Therefore, we cannot delay enrolment and need to use the consent 
procedures for emergency research. To make clinical trials with the goal of improving the treatment of 
traumatic injuries it is necessary to include unconscious and incompetent patients as no clinically relevant 
animal model exists. In other countries, national law will be followed in terms of including patients 
considered temporarily incompetent. 
 
===== SOURCE PAGE 66 =====
 
66 
 
Oxygen is a well-known drug given in a dosage of FiO2 0.21-1.0 and can be administered by paramedics, 
nurses, and doctors. The side-effects of normobaric oxygen-strategies include slightly decreased heart rate as 
well as increased risk of atelectasis, pleuritis and respiratory distress syndrome. The greater the FiO2, the 
greater the risk. As the standard treatment of care currently includes high levels of FiO2, it seems plausible 
that the intervention group will have a decreased risk for developing these side-effects. On the other side, 
hypoxia is documented to be deleterious. To avoid the risk of hypoxia, all trial participants will be monitored 
with continuous pulse oximetry and arterial blood gases to avoid desaturation. If the saturation is 
unmeasurable due to e.g. hypovolemia or hypothermia the treating physician will decide and document the 
treatment of choice. When measurable again, the allocated intervention will resume. In the TRAUMOX1 
trial, we observed only seven episodes of desaturation (SpO2 below 90%) in the restrictive group (median 
87% [87-89]). Of note, five of the seven cases of SpO2 below 89% occurred in two trial participants; one trial 
participant who had just been extubated and another trial participant who went into cardiac arrest for another 
reason than hypoxemia.  
 
The trial participants receiving the standard treatment and what is recommended in current guidelines (liberal 
oxygen) will not be put at any additional risk compared to trial participants not enrolled in the study. 
However, we suspect this standard treatment is not always beneficial. As outlined in the background section, 
we hypothesise that a liberal supplemental oxygen strategy may be detrimental and should be avoided as 
soon as possible. Thus, the restrictive supplemental oxygen (intervention group) may be associated with 
fewer side effects, with no additional risk, as seen in other trial participant populations. Therefore, we 
believe that this study may be beneficial for the single trial participant. 
Finally, there will be no risk of delaying treatment due to enrolment, as the treating physician will be treating 
the trial participant as usual, until the randomisation results are available, and the allocation has begun. 
Therefore, we think that the study will add no risk for the included trial participants. 
 
6.2 Timeline of study progress 
Approvals will be applied for spring 2021 initially in Denmark. First inclusion is expected autumn 2021, 
enrolment completed spring 2023 and data analysis and manuscript drafting autumn 2023. The submission of 
primary paper is expected at the beginning of year 2024. See figure 2. 
 
6.3 Publication policy 
The study results will be published in an appropriate international peer-reviewed scientific journals. When 
study results are published, it will be announced on the study website https://www.traumox2.org/. The study 
will be registered, and study results will be disclosed by the coordinating principal investigator in one or 
more public clinical study registry(ies), according to national/international use, including both positive, 
negative and inconclusive results. The registration will include a list of the investigational centres. The 
steering committee and the primary centre investigator (active) will be listed as co-authors in the 
publications. If the centre involves prehospital inclusion the prehospital centre investigator (active) will be 
co-author. Top-enrolling centres will be able to designate one additional co-author for every completely 
documented 100 trial participants. All authors must fulfil the criteria for authorship according to the ICMJE 
group. Each contributing centre can designate a reasonable number of active collaborators that participates in 
the study administration. These collaborators will be mentioned in the TRAUMOX2-study group and will be 
trackable via PubMed. In line with the principles of data preservation and sharing, the steering committee 
will, after publication of the overall dataset, consider all reasonable requests to make the dataset available in 
whole or part for secondary analyses and scientific publication. The steering committee will consider 
===== SOURCE PAGE 67 =====
 
67 
 
proposals for secondary analyses on the basis of the scientific quality of the proposal. Proposals will need to 
be revised and approved by the steering committee prior to submission. 
 
6.4 Data monitoring and safety committee (DMSC) 
An independent data monitoring- and safety committee (DMSC) will be set up. The committee will include a 
statistician. The committee will meet when 30-day follow-up of 355 (approximately 25% of the sample size 
estimation) and 710 (approximately 50% of the sample size estimation) trial participants has been obtained. 
Prior to the meeting, a biostatistician will perform an interim analysis with blinded data provided by the 
sponsor and principal investigator. Criteria for premature termination will be decided by steering committee. 
Furthermore, the sponsor has the responsibility to report the overall number of serious adverse events (SAEs) 
yearly to the DMSC. The DMSC charter has been approved by DMSC members and the Danish Medicines 
Agency. The content of the charter is: 
  
===== SOURCE PAGE 68 =====
 
68 
 
Charter for the Data Monitoring and Safety 
Committee (DMSC) for TRAUMOX2 
 
Version 1.1 
 
Date: 24-08-2022 
 
Comparing Restrictive versus Liberal Oxygen Strategies for Trauma 
Patients: The TRAUMOX2 Trial 
 
 
 
 
  
 
 EudraCT number: 2021-000556-19 
Danish Research Ethics Committee number: H-21018062 
ClinicalTrials.gov number: NCT05146700 
 
 
 
Chief investigator and sponsor: Professor Jacob Steinmetz, M.D., Ph.D. 
  

===== SOURCE PAGE 69 =====
 
69 
 
Introduction 
This charter will define the responsibilities of the independent DMSC, the members, the purpose of 
the DMSC and the timing of the meetings. The DMSC is answerable for the safety of trial 
participants, assessing the safety and efficacy of the interventions during the trial, and for 
monitoring the overall conduct of the clinical trial. The DMSC is obliged to follow the EU Clinical 
Trials Directive 2001/20/EC while assessing the study and to keep all patient-level data 
confidential. The DMSC consists of three clinicians with expertise in critical emergency care 
research and an independent biostatistician. The DMSC members have been chosen in order to 
avoid any financial or intellectual conflicts of interest. The members have agreed to this task for the 
entire duration of the clinical trial. However, should any members leave the DMSC during the trial, 
the steering committee will appoint the replacement(s). The DMSC is independent from the sponsor 
and the trial investigators. The DMSC will be notified of all changes to the protocol or changes in 
trial conduct. The clinicians of the DMSC will be unpaid. The biostatistician will be paid for the 
hours spent on data analysis prior to the DMSC meetings. 
 
Timing of the meetings 
Two interim analysis meetings will be held to review data relating to treatment efficacy, patient 
safety, and quality of trial conduct (e.g. enrollment progression). The four members of the DMSC 
will meet either physically or online when 30-day follow-up data (primary outcome) of 355 
(approximately 25 % of sample size estimation) and 710 (approximately 50 % of sample size 
estimation) patients have been obtained. The trial will continue while the DMSC review the data. 
The DMSC will be specifically notified by e-mail by the sponsor or coordinating investigator when 
approximately 20 % and 45 % of the patients are included due to scheduling and arranging the first 
and second meeting. Furthermore, it is optional for the DMSC members to receive the newsletters 
from the trial. The DMSC will be responsible for scheduling and arranging the meetings. Data will 
be provided to the DMSC at least 5 days prior to their meetings. 
 
Interim data review  
The DMSC will review non-identifiable person data for 30-day mortality at the two predetermined 
time points. In addition, at the second interim analysis, the DMSC will also consider available data 
on major lung complications defined as pneumonia and acute respiratory distress syndrome within 
30 days after trauma. The DMSC can at any time request extra reviews if necessary. The data will 
be provided to the biostatistician in Excel. One row will represent one trial participant and each 
column will be a data variable. The data variables included in the raw data output are: 
1: record_id (a number that uniquely identifies the patient) 
===== SOURCE PAGE 70 =====
 
70 
 
2: scr_incl_randomisation (the randomisation code: group A or B) 
3: outc_prim_30d_mort (occurrence of death within 30 days: 0 = no, 1 = yes, 999 = missing data, 
blank field = data not entered, still pending) 
4: outc_prim_30d_pneu (occurrence of pneumonia within 30 days: 0 = no, 1 = yes, 999 = missing 
data, blank field = data not entered, still pending) 
5: outc_prim_30d_ards (occurrence of acute respiratory distress syndrome within 30 days: 0 = no, 1 
= yes, 999 = missing data, blank field = data not entered, still pending) 
The DMSC statistician will provide aggregate data analysis for variable 3, 4 and 5 in two-by-two 
tables stratified on variable 2 (renamed randomisation code blinded by an external person). The data 
provided is only to evaluate on treatment efficacy and patient safety. Thus, no other data variables 
will be provided.  
The DMSC may recommend stopping the trial at each of the two interim analyses if a major 
difference in 30-day mortality is found. There are no strict stopping criteria, but it is suggested that 
the recommendation should be based on only a considerable difference, such as a relative risk 
where the lower limit of the 95 % CI is >2 (regardless of which group is nominator). The same 
applies to both the first and second interim analysis. There should be no premature ending of the 
trial for futility before completion of the preplanned inclusion of 1420 patients with a complete 30-
day follow-up.  
 
Content of the DMSC reports 
After each of the two reviews, the DMSC will produce a short report to the steering committee with 
recommendations for continuation, modifications, or premature termination of the trial. The DMSC 
will be advisory to the steering committee. Therefore, the final decision regarding potential 
modifications or termination will rest with the steering committee. 
 
Members of the DMSC 
Bodil Steen Rasmussen, MD, Ph.D. 
Chairman of the Data Monitoring and Safety Committee 
Professor 
Department of Anesthesia and Intensive Care 
Aalborg University Hospital 
Lars Wiuff Andersen, MD, M.P.H., Ph.D., D.M.Sc. 
Member of the Data Monitoring and Safety Committee 
===== SOURCE PAGE 71 =====
 
71 
 
Associate professor 
Department of Anesthesiology and Intensive Care Medicine 
Aarhus University Hospital 
Research Center for Emergency Medicine 
Aarhus University Hospital and Aarhus University 
Prehospital Emergency Medical Services 
Central Denmark Region 
Marius Rehn, MD, Ph.D. 
Member of the Data Monitoring and Safety Committee 
Associate professor 
Consultant Anaesthesiologist and pre-hospital critical care doctor 
Department of Research and Development 
Norwegian Air Ambulance Foundation 
Oslo, Norway Air Ambulance Department 
Division of Prehospital Services 
Oslo University Hospital 
Norway Faculty of Health Sciences, University of Stavanger 
Stavanger, Norway 
Brice Ozenne, biostatistician 
Member of the Data Monitoring and Safety Committee 
Assistant professor 
Department of Public Health, Section of Biostatistics  
University of Copenhagen 
Denmark 
Neurobiology Research Unit and BrainDrugs 
Copenhagen University Hospital  
Rigshospitalet 
Denmark 
  
===== SOURCE PAGE 72 =====
 
72 
 
Read and agreed by 
Bodil Steen Rasmussen 
Date: 20-12-2021 
Signature:  
 
Lars Wiuff Andersen 
Date:  
Signature: 
 
Marius Rehn 
Date:  
Signature:  
 
Brice Ozenne 
Date: 19-12-2021 
Signature:  
 
 
 
  

===== SOURCE PAGE 73 =====
 
73 
 
Change log 
24-08-2022: Renamed the variable names in this charter for variable 3, 4 and 5 due to changes in 
the database. For all 3 variables, a description of the values “999 = missing data” and “blank field = 
data not entered, still pending” was added. 
All members have read and agreed to the updated DMSC charter version 1.1.  
===== SOURCE PAGE 74 =====
 
74 
 
6.5 Archiving of documents 
The investigator will keep the subject’s files and original data according to the local methods and facilities. 
The investigator should maintain the trial documents as specified in the ICH-GCP-Guideline for 10 years. 
The investigator/institution should take measures to prevent accidental or premature destruction of these 
documents. 
 
6.6 Funding 
TRAUMOX2 is initiated by a research group of medical doctors in “Afdeling for Bedøvelse, Operation og 
TraumeCenter 6011, HovedOrtoCentret, Rigshospitalet, Copenhagen, Denmark”. It is funded by the Novo 
Nordisk Foundation which is a non-profit organisation. The duration of the funding is 4 years and the 
amount granted is 6.326.084 DKK. It covers the sponsor’s and coordinating investigator’s salary, the 
overhead and completion costs, including that each participating centre will receive 150 euro per trial 
participant included with completely documented trial participants (after 30 days). Each centre will distribute 
the amount as agreed upon within the local organization. The Novo Nordisk Foundation is not involved in 
the management of the study itself, or the decision to submit the manuscript for publication, but will be 
mentioned in all public communication, and any publication resulting from the project will be mentioned as 
”The work presented in this article is supported by Novo Nordisk Foundation grant NNF20OC0063985”. 
The funding will be paid to a bank account within the department in the sponsor’s name. The sponsor and 
coordinating investigator have no conflicts of interests in relation to the Novo Nordisk Foundation. In 
addition, the study is also partly funded by The Lundbeck Foundation as a personal grant of 350.000 DKK to 
study coordinator Josefine Baekgaard. Some of this grant will be spent on salary to Baekgaard as well as 
unexpected expenses to the trial. Drug expenses will be covererd by the participating centres’ departmental 
budget. Drug expenses beyond the normal department budget will also be covered by the participating 
centres. 
 
6.7 Protocol changes 
Can only be decided by the steering committee of the study. 
  
===== SOURCE PAGE 75 =====
 
75 
 
Figure 1 – Participant timeline 
 
 
 
Figure 2 – Timeline of study progress 
 
 
 
  

===== SOURCE PAGE 76 =====
 
76 
 
7. References 
1.  American College of Surgeons: The Committee on Trauma. ATLS: Advanced Trauma Life Support 
(Student Course Manual), 10th Edition.; 2018. doi:10.1111/j.1365-2044.1993.tb07026.x 
2.  Mosby, American College of Surgeons, National Association o f Emergency. PHTLS: Basic and 
Advanced Prehospital Trauma Life Support, 5th Edition.; 2003. 
3.  Hale KE, Gavin C, O’Driscoll BR. Audit of oxygen use in emergency ambulances and in a hospital 
emergency department. Emerg Med J. 2008;25(11):773-776. doi:10.1136/emj.2008.059287 
4.  McMullan J, Rodriquez CmsD, Ward KW, et al. Prevalence of P rehospital Hypoxemia and Oxygen 
Use in Trauma Patients. Mil Med. 2013;178(10):1121-1125. doi:10.7205/MILMED-D-13-00126 
5.  Boyle M, Wong J. Prescribing oxygen therapy. An audit of ox ygen prescribing practices on medical 
wards at North Shore Hospital, Auckland, New Zealand. N Z Med J. 2006;119(1238):31-35. 
6.  Eskesen TG, Baekgaard JS, Steinmetz J, Rasmussen LS. Initia l use of supplementary oxygen for 
trauma patients: A systematic review. BMJ Open. 2018;8(7):1-7. doi:10.1136/bmjopen-2017-020880 
7.  Chu DK, Kim LHY, Young PJ, et al. Mortality and morbidity i n acutely ill adults treated with liberal 
versus conservative oxygen therapy (IOTA): a systematic review and meta-analysis. Lancet. 
2018;391(10131):1693-1705. doi:10.1016/S0140-6736(18)30479-3 
8.  Taher A, Pilehvari Z, Poorolajal J, Aghajanloo M. Effects o f Normobaric Hyperoxia in Traumatic 
Brain Injury: A Randomized Controlled Clinical Trial. Trauma Mon. 2016;21(1):1-5. 
doi:10.5812/traumamon.26772 
9.  Suzuki S, Eastwood GM, Peck L, Glassford NJ, Bellomo R. Cur rent oxygen management in 
mechanically ventilated patients: A prospective observational cohort study. J Crit Care. 
2013;28(5):647-654. doi:10.1016/j.jcrc.2013.03.010 
10.  Helmerhorst HJF, Schultz MJ, Van Der Voort PHJ, et al. Eff ectiveness and Clinical Outcomes of a 
Two-Step Implementation of Conservative Oxygenation Targets in Critically Ill Patients: A Before 
and After Trial. Crit Care Med. 2016;44(3):554-563. doi:10.1097/CCM.0000000000001461 
11.  Eskesen TG, Baekgaard JS, Christensen RE, et al. Supplemen tal oxygen and hyperoxemia in trauma 
patients: A prospective, observational study. Acta Anaesthesiol Scand. 2019;63(4):531-536. 
doi:10.1111/aas.13301 
12.  Staehr-Rye AK, Meyhoff CS, Scheffenbichler FT, et al. High  intraoperative inspiratory oxygen 
fraction and risk of major respiratory complications. Br J Anaesth. 2017;119(1):140-149. 
doi:10.1093/bja/aex128 
13.  Six S, Jaffal K, Ledoux G, Jaillette E, Wallet F, Nseir S.  Hyperoxemia as a risk factor for ventilator-
associated pneumonia. Crit Care. 2016;20(195):1-8. doi:10.1186/s13054-016-1368-4 
14.  Allegranzi B, Zayed B, Bischof f P, et al. New WHO recommendations on intraoperative and 
postoperative measures for surgical site infection prevention: an evidence-based global perspective. 
Lancet Infect Dis. 2016;16(12):e288-e303. doi:10.1016/S1473-3099(16)30402-9 
15.  Eastwood G, Bellomo R, Baile y M, et al. Arterial oxygen tension and mortality in mechanically 
ventilated patients. Intensive Care Med. 2012;38(1):91-98. doi:10.1007/s00134-011-2419-6 
===== SOURCE PAGE 77 =====
 
77 
 
16.  Helmerhorst HJF, Arts DL, Schultz MJ, et al. Metrics of Ar terial Hyperoxia and Associated 
Outcomes in Critical Care*. Crit Care Med. 2017;45(2):187-195. 
doi:10.1097/CCM.0000000000002084 
17.  Schjørring OL, Klitgaard TL, Perner A, et al. Lower or Hig her Oxygenation Targets for Acute 
Hypoxemic Respiratory Failure. N Engl J Med. Published online 2021:1-11. 
doi:10.1056/nejmoa2032510 
18.  Baekgaard JS, Isbye D, Ottosen CI, et al. Restrictive vs l iberal oxygen for trauma patients-the 
TRAUMOX1 pilot randomised clinical trial. Acta Anaesthesiol Scand. 2019;63(7):947-955. 
doi:10.1111/aas.13362 
19.  Chan A- W, Tetzlaff JM, Altman DG, et al. SPIRIT 2013 Statement : Defining Standard Protocol 
Items for Clinical Trials. Ann Intern Med. 2013;158(3):200-207. doi:10.7326/0003-4819-158-3-
201302050-00583.Requests 
20.  Harris PA, Taylor R, Thiel ke R, Payne J, Gonzalez N, Conde JG. Research electronic data capture 
(REDCap)-A metadata-driven methodology and workflow process for providing translational 
research informatics support. J Biomed Inform. 2009;42(2):377-381. doi:10.1016/j.jbi.2008.08.010 
21.  CDC: National Healthcare Safety Network. Pneumonia (Ventilator-Associated [VAP] and Non-
Ventilator-Associated Pneumonia [PNEU]) Event.; 2021. 
https://www.cdc.gov/nhsn/pdfs/pscmanual/6pscvapcurrent.pdf 
22.  Ranieri VM, Rubenfeld GD, Thompson BT, et al. Acute respir atory distress syndrome: The Berlin 
definition. JAMA. 2012;307(23):2526-2533. doi:10.1001/jama.2012.5669 
23.  Savitsky B, Givon A, Rozenfeld M, Radomislensky I, Peleg K . Traumatic brain injury: It is all about 
definition. Brain Inj. 2016;30(10):1194-1200. doi:10.1080/02699052.2016.1187290 
24.  Demetriades D, Murray J, Charalambides K, et al. Trauma Fa talities: Time and Location of Hospital 
Deaths. J Am Coll Surg. 2004;198(1):20-26. doi:10.1016/j.jamcollsurg.2003.09.003 
25.  Mallinckrodt CH, Lin Q, Molenberghs M. A structured framew ork for assessing sensitivity to missing 
data assumptions in longitudinal clinical trials. Pharm Stat. 2013;12(1):1-6. doi:10.1002/pst.1547 
26.  The European Parliament and the Council of the European Un ion. REGULATION (EU) No 536/2014 
OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 16 April 2014 on Clinical Trials 
on Medicinal Products for Human Use, and Repealing Directive 2001/20/EC.; 2014. 
doi:10.1093/med/9780199609147.003.0017 
27.  Cook D, Lauzier F, Rocha MG, Sayles MJ, Finfer S. Serious adverse events in academic critical care 
research. CMAJ. 2008;178(9):1181-1184. doi:10.1503/cmaj.071366 
28.  World Medical Association. WMA Declaration of Helsinki - Ethical Principles for Medical Research 
Involving Human Subjects.; 2013. https://www.wma.net/policies-post/wma-declaration-of-helsinki-
ethical-principles-for-medical-research-involving-human-subjects/ 
29.  European Medicines Agency. Guideline for Good Clinical Practice - E6 (R2).; 2016. 
===== SOURCE PAGE 78 =====
 
78 
 
TRAUMOX2 protocol log changes 
 
Version 1.4 
30/09/2021 
 
Version 1.5 
08/12/2021 
Front page 
x Added new version number, date, research ethics committee number 
journal number and clinicaltrials.gov number 
General information 
x Changed date and protocol version 
x Added name and affiliation of our biostatistician for the DMSC 
6.4 Data monitoring and safety committee (DMSC) 
x Added name and affiliation of our biostatistician for the DMSC 
x Added that the DMSC charter will be added as an appendix to the 
protocol when it’s ready. It will be ready before the comite begins its 
work. 
Typography 
x Corrected minor typographical words a few places in the protocol 
Version 1.6 
23/02/2022 
General information 
x Added foreign investigators 
Protocol synopsis 
x Added EudraCT, clinicaltrials.gov and VEK number 
x Changed Videnscenter for Dataanmeldelser to the English name 
3.4 Recruitment, consent and assignment of interventions 
x Trauma bay: Changed that the trauma leader must be the including 
physician, e.g. the including physician may be the trauma leader or 
the attending anaesthesiologist 
3.8.1 Major protocol violations 
x Added the new, revised major protocol violations 
6.4 Data monitoring and safety committee (DMSC) 
x Added the DMSC charter 
Version 1.7 
03/08/2022 
Appendices 
x Added appendix 14: Protocol amendment TRAUMOX2 - 
Biomarkers of oxidative stress in patients receiving a liberal or 
restrictive oxygen strategy; it will only take place at Rigshospitalet, 
Copenhagen 
x Added appendix 15: Specific trial participant information on 
biomarker study 
x Added appendix 16: Specific trial participant consent form on 
biomarker study 
x Added appendix 17: Specific next of kin information on biomarker 
study 
x Added appendix 18: Specific next of kin consent form on biomarker 
study 
3.8.1 Major protocol violations 
x Changed the restrictive violation for intubated trial participants from 
“FiO2 ≥0.4 and having an SpO2 ≥98% (…)” to “FiO2 >0.4 and 
having an SpO2 ≥98% (…)” 
Version 1.7.1 
25/08/2022 
General information 
x Added Bern investigators and Bern as study site 
Appendices 
x Stated that the appendices are applicable in Denmark 
===== SOURCE PAGE 79 =====
 
79 
 
3.1 Study design and setting 
x Specified that all trauma centres must be within the continental 
Europe and not as part of the European Union 
Version 1.7.2 
22/10/2022 
General information 
x Added Antwerp investigator and Antwerp as study site 
Version 1.8 
21/11/2022 
5.3 Adverse Events and Serious Adverse Events 
x Specified in detail how to register the two adverse events in the 
study 
DMSC charter 
x Updated it to version 1.1 
 
===== SOURCE PAGE 80 =====
 
80 
 
Comparing Restrictive vs. Liberal Oxygen Strategies 
for Trauma Patients: The TRAUMOX2 Trial – 
Statistical Analysis Plan 
 
Tobias Arleth, MD1, Josefine Baekgaard, MD, Ph.D.1, Volkert Siersma, Ph.D.2, Markus Klimek, 
MD, Ph.D.3, Jochen Hinkelbein, MD, Dr. Med. DESA, EDIC, FAsMA4, Lars Simon Rasmussen, 
MD, Ph.D., DMSc1, Jacob Steinmetz, MD, Ph.D.1,5 for the TRAUMOX2 study group 
 
1Department of Anaesthesia, Centre of Head and Orthopaedics, University of Copenhagen, 
Rigshospitalet, Denmark 
2The Research Unit for General Practice and Section of General Practice, Department of Public 
Health, University of Copenhagen, Copenhagen, Denmark 
3Department of Anaesthesiology, Erasmus MC, University Medical Centre Rotterdam, Rotterdam, 
The Netherlands 
4Department of Anaesthesiology, Intensive Care Medicine and Emergency Medicine, Johannes 
Wesling Klinikum Minden, University Hospital of Ruhr University Bochum, Minden, Germany 
5Danish Air Ambulance, Denmark 
 
ORCID numbers: 
Tobias Arleth: 0000-0002-7484-6207 
Josefine Widding Baekgaard: 0000-0002-5420-723X 
Volkert Siersma: 0000-0003-1941-2681 
Markus Klimek: 0000-0002-0122-9929 
Jochen Hinkelbein: 0000-0003-3585-9459  
Lars Simon Rasmussen:
 0000-0002-7480-3004 
Jacob Steinmetz: 0000-0001-9620-8911 
 
Trial registration: EudraCT number: 2021-000556-19; ClinicalTrials.gov identifier: 
NCT05146700 (date of registration: December 7th, 2021) 
 
SAP version: 1.0 
 
SAP date: 11-01-2023 
 
SAP revisions: None 
 
===== SOURCE PAGE 81 =====
 
81 
 
Protocol version: 1.8 
 
Signatures of 1
st author, senior statistician, and chief investigator:  
 
 
Tobias Arleth Volkert Siersma Jacob Steinmetz 
1st author Senior statistician Chief investigator and sponsor 
   
   
 
 
 
 
 
 
 
 
 
 
 
Corresponding author: 
Tobias Arleth, MD 
Department of Anaesthesia 
Centre of Head and Orthopaedics 
Rigshospitalet, Copenhagen 
Denmark 
E-mail: tobias.arleth@regionh.dk 
Phone: +45 35 45 95 02 
  

===== SOURCE PAGE 82 =====
 
82 
 
Abstract 
Background: The international ATLS (Advanced Trauma Life Support) guidelines recommend that all 
severely injured trauma patients receive supplemental oxygen based on very limited evidence. The 
TRAUMOX2 trial randomises adult trauma patients to a restrictive or liberal oxygen strategy for eight hours. 
The primary composite outcome consists of 30-day mortality and/or development of major respiratory 
complications (pneumonia and/or acute respiratory distress syndrome; ARDS). This manuscript presents the 
statistical analysis plan for TRAUMOX2. 
 
Methods: Patients are randomised 1:1 in variable block sizes of four, six and eight, stratified by including 
centre (prehospital base or trauma centre) and tracheal intubation at inclusion. The trial will include 1420 
patients to be able to detect a 33% relative risk reduction with the restrictive oxygen strategy of the 
composite primary outcome with 80% power at the 5% significance level. We will conduct modified 
intention-to-treat analyses on all randomised patients and per-protocol analyses for the primary composite 
outcome and key secondary outcomes. The primary composite outcome and two key secondary outcomes 
will be compared between the two allocated groups using logistic regression reported as odds ratios (ORs) 
with 95% confidence intervals (CI) adjusted for the stratification variables as in the primary analysis. A P-
value below 5% will be considered statistically significant. A Data Monitoring and Safety Committee 
(DMSC) has been established to conduct interim analyses after inclusion of 25% and 50% of the patients.  
 
Conclusions: This statistical analysis plan of the TRAUMOX2 trial will minimise bias and add transparency 
to the statistics applied in the analysis of the trial. The results will add evidence on restrictive and liberal 
supplemental oxygen strategies for trauma patients.  
 
Registration: ClinicalTrials.gov identifier: NCT05146700 (date of registration: December 7
th, 2021). 
European Union Drug Regulation Authorities Clinical Trials Database, EudraCT number: 2021-000556-19. 
  
===== SOURCE PAGE 83 =====
 
83 
 
INTRODUCTION 
The international ATLS (Advanced Trauma Life Support) guidelines recommend that all severely injured 
trauma patients receive supplemental oxygen1 based on very limited evidence.2,3 Thus, supplemental oxygen 
is commonly used in trauma patients4–12, although it may lead to hyperoxaemia which has been associated 
with pulmonary complications and increased mortality.13,14 The TRAUMOX2 trial15 randomises adult 
patients with suspected major trauma to eight hours of a restrictive or liberal oxygen strategy. The restrictive 
group receives the lowest dosage of oxygen (>21%) that ensures an SpO2 of 94%. The liberal group receives 
12-15 L O2/min or FiO2 = 0.6-1.0. The primary objective of TRAUMOX2 is to compare the effect of these 
two oxygen strategies on 30-day mortality and/or development of major respiratory complications 
(pneumonia and/or acute respiratory distress syndrome; ARDS) (primary composite outcome). This 
manuscript presents the statistical analysis plan for TRAUMOX2.  
===== SOURCE PAGE 84 =====
 
84 
 
METHODS 
This statistical analysis plan of the TRAUMOX2 trial has been written according to the Guidelines for the 
Content of Statistical Analysis Plans in Clinical Trials.16 It aims to give an overview and justification of the 
chosen variables and statistical methods used in TRAUMOX2. The database system used for this trial is 
REDCap.17 The plan is prepared while the trial is still including patients and thus before the database is 
exported for analysis by the trial statistician. All analyses of the primary and secondary outcomes will be 
conducted according to this publication. The steering committee of the trial approved this statistical analysis 
plan on the 11th of January 2023. 
 
The TRAUMOX2 trial has been approved by the Danish Research Ethics Committee (H-21018062), the 
Danish Medicines Agency (EudraCT 2021-000556-19), the Knowledge Centre on Data Protection 
Compliance, Health Science and Innovation in the Capital Region of Denmark, and by all authorities as 
required at participating centres.  
 
Trial design 
TRAUMOX2 is an investigator-initiated, international, multicentre, parallel-grouped, superiority, primary 
outcome assessor- and analyst-blinded, randomised, controlled, clinical trial. 
 
Randomisation and blinding 
Patients are randomised 1:1 in variable block sizes of four, six and eight, stratified by including centre 
(prehospital base or trauma centre) and tracheal intubation (yes/no) at inclusion. The randomisation table was 
generated outside of REDCap by a statistician otherwise not affiliated with the study. The allocation 
sequence list and specific block size are only known by this statistician and will remain concealed from the 
investigators. Prior to randomisation, consent must be obtained either by proxy (from another physician) or 
according to national legislation. Immediately afterwards, randomisation is done by opening a concealed 
envelope with information on allocation. Each concealed envelope contains a study ID that matches a study 
ID on the randomisation list generated by the statistician. Subsequently, informed consent is confirmed from 
the patient or a relative in case the patient cannot give consent. National law on consent is followed if neither 
the patient nor the relative can provide consent. A more detailed description of the consent procedure is 
presented in the protocol and on the study website.15,18 
 
The treating staff will be aware of the patients’ randomisation group, and due to the nature of oxygen 
treatment, patients and relatives will often be aware of the allocated oxygen strategy as well. While the trial 
is including patients for the study, members of the research team will also be aware of the patients’ oxygen 
allocation strategy. At least two allocation-blinded primary outcome assessors (specialists in anaesthesia, 
intensive care, emergency medicine or similar) will be appointed at each centre to assess in-hospital lung 
complications (pneumonia and/or ARDS). Blinding will be ensured by concealing all information indicative 
of the allocation prior to assessment. The trial statistician is blinded to the allocation of treatment, and 
manuscript writers will become blinded to the allocation of treatment once the trial ends and data is exported 
for analysis. In the exported dataset, the randomisation groups will be renamed A and B by an unblinded 
research assistant otherwise not affiliated with the study. Afterwards, the renamed dataset will be forwarded 
to the trial statistician for data analysis. While data is analysed, the blinded authors will write two versions of 
the manuscript: one where treatment A is the liberal oxygen strategy, and another version where treatment A 
is the restrictive oxygen strategy. These two manuscripts will exclude data on oxygenation during the 
===== SOURCE PAGE 85 =====
 
85 
 
intervention period, as this would reveal the allocation group. All authors must agree on both versions before 
unblinding. 
 
Sample size calculation 
In TRAUMOX119, the pilot study for TRAUMOX2, the primary composite outcome occurred in 20% in the 
restrictive group and 33% in the liberal group. In larger studies, mortality from major trauma has been 
estimated to be 6-12%20, and the incidence of ventilator associated pneumonia post trauma was almost 30% 
in one study.14 In TRAUMOX2, we estimate that with 710 trial participants in each trial arm, including a 
drop-out rate of 3.5%, yielding a total of 1420 patients, we will be able to detect a 33% relative risk 
reduction in the incidence of the composite primary outcome (30-day mortality and/or major respiratory 
complications) with a restrictive supplemental oxygen strategy with 80% power at the 5% significance level 
if the incidence of our primary outcome is 15% in the liberal group and 10% in the restrictive group. This 
corresponds to an absolute between-group difference of 5 percentage points. 
 
Framework 
The primary analysis will be conducted as a superiority trial to test whether the restrictive group is superior 
to the liberal group.  
 
Statistical interim analysis and stopping guidance 
An independent data monitoring- and safety committee (DMSC) has been set up. The committee includes a 
statistician. The committee met when information on 30-day mortality had been collected in 355 patients 
(approximately 25% of the envisioned sample size) and recommended the trial to continue. The DMSC will 
meet again when 30-day mortality has been collected in 710 patients (approximately 50% of the sample size 
estimation). In addition, at the second interim analysis, the DMSC will also consider available data on major 
respiratory complications. Prior to the meetings, the DMSC statistician performs an interim analysis with 
data blinded towards the allocation. There are no strict stopping criteria, but in the DMSC charter, it is 
suggested that a recommendation should be based on only a considerable difference, such as a relative risk 
where the lower limit of the 95% confidence interval is >2 (regardless of which group is nominator). This 
applies to both the first and second interim analysis. There will be no premature ending of the trial for futility 
before the preplanned inclusion of 1420 patients. In addition, the sponsor has the responsibility to report the 
overall number of annual SAEs to the committee. The DMSC will have an advisory role to the steering 
committee and therefore the final decision regarding potential modifications or termination will rest with the 
steering committee. Detailed information on the DMSC is available on the study website 
(www.traumox2.org). 
 
Timing of outcome assessments and final analysis 
The registered variables at baseline, during intervention and during admission (in-hospital) are presented in 
Tables 1, 2 and 4. In addition to the variables collected during the intervention (Table 2), a figure displaying 
the median hourly SpO2 with interquartile range for both groups will be made. The primary composite 
outcome and key secondary outcomes are presented in Table 3. The exploratory secondary outcomes at day 
30 are available in Table 4. A long-term follow-up is assessed at six- and 12 months on morbidity and 
quality-of-life outside the scope of the primary analysis. A 12-month mortality will also be assessed. The 
primary analysis can begin 30 days after the last patient has been included. 
  
===== SOURCE PAGE 86 =====
 
86 
 
STATISTICAL PRINCIPALS 
Confidence intervals and P values 
We will use a significance level of 5% and thus 95% confidence intervals (CI) on our estimates. Significance 
tests will be two sided. The exploratory secondary outcomes will be adjusted for multiple testing by having 
their P-values, and thus 95% CIs, assessed using a significance level lower than 5% according to the 
Benjamini-Hochberg method.21 Hence, for the P-values of the exploratory secondary outcomes it will be 
indicated whether they are significant while controlling the false discovery rate at 5%. 
 
Adherence and protocol deviations 
For all TRAUMOX2 trial participants, it is possible to deviate from the protocol if clinically justified by the 
treating physician. These reasons should always be documented in REDCap. 
 
A major protocol violation will be defined as: 
 
• Restrictive O
2 group, during the intervention period 
 
For non-intubated trial participants: Supplemental oxygen ≥3 L O2/min AND an SpO2 ≥98% recorded at two 
consecutive hourly time points on the data collection sheet.  
For intubated trial participants: FiO
2 >0.4 AND an SpO2 ≥98% recorded at two consecutive hourly time 
points on the data collection sheet. 
 
• Liberal O2 group, during the intervention period 
 
For non-intubated trial participants: Supplemental oxygen <3 L O
2/min at two consecutive hourly time points 
on the data collection sheet. 
For intubated trial participants: FiO2 <0.4 at two consecutive hourly time points on the data collection sheet. 
 
For the main paper, data on protocol deviations and major protocol violations will be presented in Table 2.  
 
Analysis populations 
We will conduct modified intention-to-treat analyses on all randomised patients.22 The modification is based 
on the exclusion criterion stating that trauma patients are secondarily excluded after randomisation and 
trauma centre diagnostics (e.g. secondary survey after CT scan), if the latter has resulted in expected 
discharge within 24 hours (due to few or no injuries). If consent is withdrawn for a patient, no data after the 
day will be collected. Please see Figure 1. Per-protocol analyses will also be carried out, but only for the 
primary composite outcome and key secondary outcomes. The per-protocol population is the same as the 
modified intention-to-treat population with exclusion of those having one or more major protocol violations. 
===== SOURCE PAGE 87 =====
 
87 
 
TRIAL POPULATION 
Screening, eligibility and recruitment  
Screening, eligibility, and recruitment is conducted as stated in the trial protocol.15 A CONSORT23 flow 
diagram is presented in Figure 1.  
 
Baseline patient characteristics 
Baseline variables for all analysed patients are presented in Table 1. Data will be summarised with numbers 
and percentages for categorical variables and medians with interquartile ranges (IQRs) for continuous 
variables. According to the CONSORT 2010 statement23, differences in baseline variables between the 
restrictive oxygen group and liberal oxygen group will not explored.  
 
Withdrawal and follow-up 
Since this is an acute medical study, patients are always included upon the discretion of an including 
physician. Patient or next-of-kin consent is sought after inclusion in all cases. After inclusion, patients are at 
any time allowed to refrain from giving consent or withdraw consent they have given previously. If consent 
is withdrawn, patients are followed up until this time point. However, the participating centres’ individual 
approach will always be according to national law. 
===== SOURCE PAGE 88 =====
 
88 
 
ANALYSIS 
Outcome definitions 
 
Primary outcome and key secondary outcomes  
The primary outcome is a composite outcome consisting of 30-day mortality and/or major respiratory 
complications (pneumonia and/or ARDS) within 30 days. The 30-day mortality is assessed using in-hospital 
or national/local registries. Whenever this is not possible, for instance if the patient is a foreigner, 30-day 
mortality will be sought by contacting the patient or relatives by phone or e-mail on day 30 after inclusion or 
later. At least three attempts on three different days should be carried out. If no contact is obtained, and the 
patient was discharged to home from either the TRAUMOX2 including hospital or a subsequent receiving 
hospital, the patient is considered to be alive on day 30. However, if the patient was transferred to another 
hospital without medical record access for TRAUMOX2 investigators, 30-day vital status is considered 
unknown and 30-day mortality is then considered as missing data. The definition of major respiratory 
complications, pneumonia and ARDS, is in accordance with the criteria described by the CDC24 and the 
Berlin definition25, respectively. It is evaluated through the available medical record system via a blinded 
assessment by at least two specialists in anaesthesia, intensive care medicine, emergency medicine or similar 
appointed at each centre. If the patient is transferred to another hospital, and the medical record from that 
hospital until day 30 is not available, the assessment will be based on the available medical record from the 
TRAUMOX2 participating centre only. However, an attempt of obtaining the medical record of the receiving 
facility will be carried out and will be included in the primary outcome assessment if possible. 
 
The two key secondary outcomes are 30-day mortality and major respiratory complications (pneumonia 
and/or ARDS) within 30 days, respectively.  
 
The details of all primary and key secondary outcomes are presented in Table 3. 
 
In-hospital registrations and exploratory secondary outcomes 
Additional outcomes are presented in Table 4.  
 
Analysis methods 
 
Primary composite outcome 
The primary composite outcome will be compared between the two groups using logistic regression and 
reported as odds ratio (OR) with 95% CI, adjusted for the stratification variables. An additional analysis for 
the primary composite outcome using logistic regression will be made with adjustment for the stratification 
variables, age, sex, ISS, and the first available GCS score after trauma. Excess association within the 
stratification is adjusted for through the method of generalized estimating equations (GEE) the including 
base as a clustering variable. Potential differential dropout from the study – through late withdrawal of 
consent or unreachable for follow-up – is adjusted for through weighting of the available data by the inverse 
of the probability of being observed26; the latter are estimated in a logistic regression model on baseline 
characteristics and the allocation. Adjustment of the variance matrix to reflect the weighting is included in 
the GEE method. Evaluation of significance will be based on the P-value.  
 
===== SOURCE PAGE 89 =====
 
89 
 
Key secondary outcomes 
The key secondary outcomes will be analysed similarly to the primary composite outcome and adjusted for 
the same covariates.  
 
Exploratory secondary outcomes 
Exploratory secondary outcomes will be analysed similarly to the primary composite outcome and adjusted 
for the same covariates while the type of regression is according to the type of the outcome (e.g., logistic 
regression for binary outcomes and linear regression for continuous outcomes). Evaluation of significance 
will be adjusted according to the Benjamini-Hochberg method.
21 
 
Subgroup analyses 
The following subgroup analyses related to the primary outcome will be performed: 
x Initially intubated within one hour after trauma  
x Intensive Care Unit admission 
x Moderate or severe traumatic brain injury (Abbreviated Injury Score ≥3) 
x Known lung disease 
x Episode(s) of hypoxaemia during the intervention (SpO
2 <90%) 
x Included pre-hospital vs. in-hospital 
x Injury Severity Score >15 
 
Missing data 
If patients withdraw their consent once they regain consciousness, data up until that day is collected and 
stored. However, the participating centres’ individual approach will always be according to national law. If 
data is available for time-dependent outcomes (e.g., outcomes that are specified to be assessed 7 or 30 days 
after inclusion), the assessments will be done dependent on the timing of withdrawal of consent. In case a 
time-dependent outcome occurs within the period of available data for patients who withdraw consent, the 
outcome will be registered. If an outcome does not occur within the period of available data for a time-
dependent outcome, the outcome is registered as missing data. Missing outcome data, which primarily covers 
the patients who withdraw consent, is adjusted for using the inverse probability weighting method described 
above under primary composite outcome. 
 
Additional analyses 
A statistical analysis plan for the long-term follow-up at six- and 12 months will become available on the 
study website (www.traumox2.org).  
 
Harms 
 
Adverse Events and Serious Adverse Events 
We have chosen to register only atelectases assessed by a radiologist and irritability of airway mucosa only if 
registered by the health care staff in the medical record as adverse events in accordance with established 
practice in trials on critically ill patients who experience many events as part of the natural trajectory of the 
primary disease process or expected as a result of the critical illness.27 For the main paper, the numbers and 
frequencies will be presented as shown in the supplementary Table 1. 
 
===== SOURCE PAGE 90 =====
 
90 
 
Statistical software 
SAS (version 9.4) will be used for all analyses.  
===== SOURCE PAGE 91 =====
 
91 
 
Discussion 
The trauma population is particularly exposed to high concentrations of oxygen5,7–9, although the supporting 
evidence is extremely sparse.2,3 The TRAUMOX2 trial will add important scientific information to this area. 
The aim of this statistical plan is to provide transparency of the statistics that will be used to evaluate the 
data. The plan has been prepared according to current recommendations16 and presented before the last 
patient has been randomised. 
 
Randomisation is carried out with sealed envelopes stratified by intubation at inclusion and the including 
centre or pre-hospital base. This simple solution was chosen to avoid randomisation challenges in the acute 
setting where no internet connection may be available, for example on the road or in the air, and to make 
randomisation quicker and more pragmatic. However, there is a risk, through reshuffling of the envelopes or 
dispersion over multiple vehicles related to a prehospital base, that the generated allocation sequence is not 
strictly followed. This would reduce the efficiency of the block-randomisation slightly as allocation may thus 
be less balanced, but randomisation is not invalidated as any reshuffling is independent of the actual 
allocation.  
 
The rationale for choosing our primary composite outcome, 30-day mortality and/or development of major 
respiratory complications (pneumonia and/or ARDS), falls into two categories. First, both outcomes are 
patient-centred and important for the trauma patient; trauma is the leading cause of death globally for people 
up till 49 years of age
28 and the incidence of pneumonia is high amongst critically ill patients and lung 
complications are associated with longer hospital stays and increased morbidity and mortality.29–31 Second, a 
primary composite outcome can increase the statistical precision and thus the efficiency of the trial.32 
Furthermore, the primary outcome is assessor-blinded to compensate for the open label intervention. Finally, 
the numbers from the literature on mortality and pneumonia in trauma patients that were chosen for the 
sample size calculation were based on the best available evidence including a pilot trial when the trial was 
designed. 
 
We have chosen logistic regression for our primary outcome because it is the natural choice of statistical 
model in which to analyze binary outcomes. The effect estimates obtained are odds ratios that are not 
dependent on the marginal distribution of the outcome and, as such, may be directly compared to odds ratio 
effect estimates from similar studies but on patients with higher or lower risk. Also, we will assess the 
significance of our exploratory secondary outcomes controlling for the false discovery rate at 5% with the 
Benjamini-Hochberg method, which yields a lower Type I-error in our study.
21 
 
The primary challenge in the statistical analyses is the adjustment for possible differential attrition. Several 
outcomes cannot, or only partly, be evaluated because of loss to follow-up, withdrawal of consent, or death. 
For example, a person who dies three days after trauma has automatically a lower chance of developing 
pneumonia and only a maximum of three days Intensive Care Unit stay. As the intervention is hypothesized 
to have an effect on, among other things, mortality, this probable differential attrition is to be taken seriously. 
We adjust for differential attrition by inverse probability weighting.26 
 
  
===== SOURCE PAGE 92 =====
 
92 
 
Dissemination 
The data on the primary composite outcome, key secondary outcomes and exploratory secondary outcomes 
will be analysed when 30-day follow-up is complete. The data presented in this manuscript will constitute 
the basis for the primary publication of the study which will be submitted to a peer-reviewed clinical journal. 
The data on the long-term follow-up at six- and 12 months will be presented in separate publications 
submitted later to peer-reviewed clinical journals when the long-term follow-up is complete. All results will 
be sought published, including both positive, negative, or inconclusive results.  
===== SOURCE PAGE 93 =====
 
93 
 
Status 
The TRAUMOX2 trial began recruiting the 7th of December, 2021. As of 11th of February 2023, 913 patients 
have been included. We expect that the last patient is included in the beginning of year 2024.  
===== SOURCE PAGE 94 =====
 
94 
 
References 
1.  American College of Surgeons: The Committee on Trauma. ATLS: Advanced Trauma Life Support 
(Student Course Manual), 10th Edition.; 2018. doi:10.1111/j.1365-2044.1993.tb07026.x 
2.  Eskesen TG, Baekgaard JS, Steinmetz J, Rasmussen LS. Initia l use of supplementary oxygen for 
trauma patients: A systematic review. BMJ Open. 2018;8(7):1-7. doi:10.1136/bmjopen-2017-020880 
3.  Hansen TE, Christensen RE, Baekgaard J, Steinmetz J, Rasmus sen LS. Supplemental Oxygen for 
Traumatic Brain Injury: A Systematic Review. Acta Anaesthesiol Scand. Published online 2021:1-10. 
doi:10.1111/aas.14019 
4.  McMullan J, Rodriquez CmsD, Ward KW, et al. Prevalence of P rehospital Hypoxemia and Oxygen 
Use in Trauma Patients. Mil Med. 2013;178(10):1121-1125. doi:10.7205/MILMED-D-13-00126 
5.  Leitch P, Hudson AL, Griggs JE, Stolmeijer R, Lyon RM, ter Avest E. Incidence of hyperoxia in 
trauma patients receiving pre-hospital emergency anaesthesia: results of a 5-year retrospective 
analysis. Scand J Trauma Resusc Emerg Med. 2021;29(1):4-11. doi:10.1186/s13049-021-00951-w 
6.  Boyle M, Wong J. Prescribing oxygen therapy. An audit of ox ygen prescribing practices on medical 
wards at North Shore Hospital, Auckland, New Zealand. N Z Med J. 2006;119(1238):31-35. 
7.  Eskesen TG, Baekgaard JS, Christensen RE, et al. Supplement al oxygen and hyperoxemia in trauma 
patients: A prospective, observational study. Acta Anaesthesiol Scand. 2019;63(4):531-536. 
doi:10.1111/aas.13301 
8.  Baekgaard JS, Abback PS, Boubaya M, et al. Early hyperoxemi a is associated with lower adjusted 
mortality after severe trauma: Results from a French registry. Crit Care. 2020;24(1):1-11. 
doi:10.1186/s13054-020-03274-x 
9.  Baekgaard J, Siersma V, Christensen RE, et al. A high fract ion of inspired oxygen may increase 
mortality in intubated trauma patients – A retrospective cohort study. Injury. Published online 2021. 
doi:10.1016/j.injury.2021.09.015 
10.  Kondo Y, Gibo K, Abe T, Fukuda T, Kukita I. Association of  prehospital oxygen administration and 
mortality in severe trauma patients (PROMIS): A nationwide cohort study. Medicine (Baltimore). 
2019;98(27):e16307. doi:10.1097/MD.0000000000016307 
11.  Christensen MA, Steinmetz J, Velmahos G, Rasmussen LS. Sup plemental oxygen therapy in trauma 
patients: an exploratory registry‐based study. Acta Anaesthesiol Scand. 2021;(July 2020):1-12. 
doi:10.1111/aas.13829 
12.  Hale KE, Gavin C, O’Driscoll BR. Audit of oxygen use in emergency ambulances and in a hospital 
emergency department. Emerg Med J. 2008;25(11):773-776. doi:10.1136/emj.2008.059287 
13.  Staehr-Rye AK, Meyhoff CS, Scheffenbichler FT, et al. High  intraoperative inspiratory oxygen 
fraction and risk of major respiratory complications. Br J Anaesth. 2017;119(1):140-149. 
doi:10.1093/bja/aex128 
14.  Six S, Jaffal K, Ledoux G, Jaillette E, Wallet F, Nseir S.  Hyperoxemia as a risk factor for ventilator-
associated pneumonia. Crit Care. 2016;20(195):1-8. doi:10.1186/s13054-016-1368-4 
15.  Baekgaard J, Arleth T, Siersma V, et al. Comparing restric tive versus liberal oxygen strategies for 
===== SOURCE PAGE 95 =====
 
95 
 
trauma patients — the TRAUMOX2 trial: protocol for a randomised clinical trial. BMJ Open. 
2022;12:e064047. doi:10.1136/bmjopen-2022-064047 
16.  Gamble C, Krishan A, Stocken D, et al. Guidelines for the Content of Statistical Analysis Plans in 
Clinical Trials. JAMA. 2017;318(23):2337-2343. doi:10.1001/jama.2017.18556 
17.  Harris PA, Taylor R, Thiel ke R, Payne J, Gonzalez N, Conde JG. Research electronic data capture 
(REDCap)-A metadata-driven methodology and workflow process for providing translational 
research informatics support. J Biomed Inform. 2009;42(2):377-381. doi:10.1016/j.jbi.2008.08.010 
18.  The TRAUMOX2 Trial website. www.traumox2.org 
19.  Baekgaard JS, Isbye D, Ottosen CI, et al. Restrictive vs l iberal oxygen for trauma patients-the 
TRAUMOX1 pilot randomised clinical trial. Acta Anaesthesiol Scand. 2019;63(7):947-955. 
doi:10.1111/aas.13362 
20.  Demetriades D, Murray J, Charalambides K, et al. Trauma Fa talities: Time and Location of Hospital 
Deaths. J Am Coll Surg. 2004;198(1):20-26. doi:10.1016/j.jamcollsurg.2003.09.003 
21.  Benjamini Y, Hochberg Y. Controlling the False Discovery R ate: a Practical and Powerful Approach 
to Multiple Testing. J R Stat Soc. 1995;57(1):289-300. doi:10.1111/j.2517-6161.1995.tb02031.x 
22.  Demets DL, Cook T. Challenges of Non-Intention-to-Treat An alyses. JAMA. 2019;321(2):145-146. 
doi:10.1001/jama.2018.19192 
23.  Schulz KF, Altman DG, Moher D, The CONSORT Group. CONSORT 2010 Statement: updated 
guidelines for reporting parallel group randomised trials. Lancet. 2010;375(9721):1136. 
doi:10.1016/S0140-6736(10)60456-4 
24.  CDC: National Healthcare Safety Network. Pneumonia (Ventilator-Associated [VAP] and Non-
Ventilator-Associated Pneumonia [PNEU]) Event.; 2021. 
https://www.cdc.gov/nhsn/pdfs/pscmanual/6pscvapcurrent.pdf 
25.  Ranieri VM, Rubenfeld GD, Thompson BT, et al. Acute respir atory distress syndrome: The Berlin 
definition. JAMA. 2012;307(23):2526-2533. doi:10.1001/jama.2012.5669 
26.  Dufouil C, Brayne C, Clayton D. Analysis of longitudinal s tudies with death and drop-out: A case 
study. Stat Med. 2004;23(14):2215-2226. doi:10.1002/sim.1821 
27.  Cook D, Lauzier F, Rocha MG, Sayles MJ, Finfer S. Serious adverse events in academic critical care 
research. CMAJ. 2008;178(9):1181-1184. doi:10.1503/cmaj.071366 
28.  WHO. Injuries and Violence: The Facts.; 2014. 
http://www.who.int/violence_injury_prevention/media/news/2015/Injury_violence_facts_2014/en/ 
29.  Lipovy B, Rihová H, Gregorova N, et al. Epidemiology of ve ntilator-associated tracheobronchitis and 
ventilator-associated pneumonia in patients with inhalation injury at the burn centre in Brno (Czech 
Republic). Ann Burns Fire Disasters. 2011;24(3):120-125. 
30.  Kollef MH, Hamilton CW, Ernst FR. Economic Impact of Venti lator-Associated Pneumonia in a 
Large Matched Cohort. Infect Control Hosp Epidemiol. 2012;33(3):250-256. doi:10.1086/664049 
31.  Melsen WG, Rovers MM, Groenwold RHH, et al. Attributable m ortality of ventilator-associated 
===== SOURCE PAGE 96 =====
 
96 
 
pneumonia: A meta-analysis of individual patient data from randomised prevention studies. Lancet 
Infect Dis. 2013;13(8):665-671. doi:10.1016/S1473-3099(13)70081-1 
32.  Freemantle N, Calvert M, Wood J, Eastaugh J, Griffin C. Co mposite Outcomes in Randomized 
Trials: Greater Precision But With Greater Uncertainty? JAMA. 2003;289(19):2554-2559. 
doi:10.1001/jama.289.19.2554 
33.  Ringdal K, Coats T, Lefering R, et al. The Utstein Trauma Template for Uniform Reporting of Data 
Following Major Trauma: Data Dictionary. Version 1.1.1.; 2008. 
  
===== SOURCE PAGE 97 =====
 
97 
 
TABLE 1 - BASELINE REGISTRATIONS 
 
Variable Definition 
Age Calculated from birth year  
Sex Genotypic 
Height Measured in cm 
Weight Measured in kg 
Active smoker (y/n) 
 
Comorbidities prior to trauma (y/n) 
 
Lung disease Chronic obstructive pulmonary disease 
(COPD), asthma, lung fibrosis, or positive 
COVID
-19 test on the day of admission, 
other 
Cardiovascular disease Hypertension, angina, atrial fibrillation, 
heart failure, coronary artery disease, other 
Other 
 
Mechanism of injury* Traffic (motor vehicle accident, motorcycle 
accident, bicycle accident, 
 
pedestrian, other), shot, stab, struck,  
fall (0-2 metres, 2-4 metres, >4 metres), 
blast/explosion, other, unknown 
Dominating type of injury Blunt or penetrating 
Site of inclusion Pre-hospital or in-hospital 
Airway at inclusion** Non-intubated or intubated 
Use of pre-hospital or in-hospital supplemental oxygen 
prior to randomisation (y/n) 
 
Highest SpO2 measured prior to randomisation number 
Time with supplemental oxygen treatment before 
randomisation 
minutes 
Indication for supplemental oxygen treatment 
before randomisation 
Lifesaving (SpO2 <85%), avoiding 
hypoxaemia (SpO2< 90%),  
routine treatment independent of SpO2 
Supplemental oxygen administration form before 
randomisation 
Nasal cannula, non-rebreather mask, 
intubated 
Initial oxygen flow or initial FiO2 number 
Receiving trauma centre Rigshospitalet, Copenhagen, Denmark, 
Odense Universitetshospital, 
 
Odense, Denmark, Aarhus 
Universitetshospital, Aarhus, Denmark,  
Erasmus Medical Centre, Rotterdam, The 
Netherlands, University Hospital Bern, 
Switzerland 
Active treatment of pneumonia on admission (y/n) Evaluated through patient medical charts 
Intubation (y/n) Pre-hospital, Trauma Centre  
Death Pre-hospital, Trauma Centre 
Pre-hospital information 
First vital signs*** 
Systolic blood pressure mmHg 
===== SOURCE PAGE 98 =====
 
98 
 
Diastolic blood pressure mmHg 
Pulse bpm 
Respiratory rate  number / min 
SpO2 number 
Body temperature Celsius 
Glasgow Coma Scale score number 3-15 
Trauma centre information 
Type of transport to the trauma centre Ground ambulance, helicopter, combination 
of ground ambulance and helicopter, private 
vehicle, walk-in, police, other 
Time from trauma to trauma centre arrival minutes 
Surgery performed in the trauma centre (y/n) 
 
If yes, type of surgery Neurosurgery, Cardiothoracic surgery, 
Abdominal surgery,  
Orthopaedic surgery, Urological surgery, 
Vascular surgery, Gynaecological surgery, 
other 
First vital signs** 
Systolic blood pressure mmHg 
Diastolic blood pressure mmHg 
Pulse bpm 
Respiratory rate number / minute 
SpO2 % 
Body temperature Celsius 
Glasgow Coma Scale score number 3-15 
Destination after trauma centre resuscitation  Operating Room, Intensive Care Unit, Ward 
Injury details 
 
Injured body region(s) Head, Neck, Face, Spine, Thorax, 
Abdomen, Pelvis, Extremity, Other(s) 
Abbreviated Injury Score (AIS) codes numbers 
Injury Severity Score (ISS) number 
*Following the Utstein template for reporting33  
mechanism of injury 
**A supraglottic airway is also considered intubation and can be noted in the CRF separately 
***Including time and date of vital sign measurement 
 
 
  
===== SOURCE PAGE 99 =====
 
99 
 
TABLE 2 - DATA COLLECTED SPECIFICALLY DURING INTERVENTION PERIOD 
Variable Definition 
Time from trauma to randomisation minutes 
For every hour during the 8-hour intervention: 
Patient location Pre-hospital, Trauma Centre, Operating Room, Examination 
Room, Post
-Anaesthesia Care Unit, Intensive Care Unit, 
Ward 
SpO2 median 
Type of supplemental oxygen None, nasal cannula, non-rebreather mask, intubated* 
Oxygen flow (L/min) median 
FiO2  median  
1st ABG** (at hour 1 ± 30 minutes after randomisation) 
PaO2 kPa or mmHg 
Haemoglobin mmol/L 
Lactate mmol/L 
2nd ABG*** (at hour 6 ± 2 hours after randomisation) 
PaO2 kPa or mmHg 
Haemoglobin mmol/L 
Lactate mmol/L 
Major protocol violation** (y/n) 
 
Protocol deviation (y/n) 
 
*A supraglottic airway is also considered intubation and can be noted in the CRF separately 
**Arterial blood gas 
***A major protocol violation will be defined as: 
 
• Restrictive O
2 group, during the intervention period 
 
For non-intubated trial participants: Supplemental oxygen ≥3 L O2/min AND an SpO2 ≥98% recorded at two 
consecutive hourly time points on the data collection sheet.  
For intubated trial participants: FiO
2 >0.4 AND an SpO2 ≥98% recorded at two consecutive hourly time 
points on the data collection sheet. 
 
• Liberal O2 group, during the intervention period 
 
For non-intubated trial participants: Supplemental oxygen <3 L O
2/min at two consecutive hourly time points 
on the data collection sheet. 
For intubated trial participants: FiO2 <0.4 at two consecutive hourly time points on the data collection sheet. 
  
===== SOURCE PAGE 100 =====
 
100 
 
TABLE 3 - PRIMARY OUTCOME AND KEY SECONDARY 
OUTCOMES
 
 
Primary outcome Definition 
30-day mortality and/or development of major respiratory 
complications (pneumonia* and/or Acute Respiratory Distress 
Syndrome (ARDS)**) (y/n) 
Assessed by two specialists in 
anaesthesia, intensive care 
medicine, emergency medicine 
or similar using blinded medical 
records, laboratory and 
microbiology results, and 
radiological assessments 
Key secondary outcomes 
 
30-day mortality (y/n) 
 
Major respiratory complications (pneumonia and/or ARDS) within 30 
days (y/n) 
 
All key outcomes are accompanied by specific times and dates 
*Pneumonia is categorised as non-ventilator-associated pneumonia (PNEU) or  
ventilator-associated pneumonia (VAP), defined by the CDC criteria24 
**ARDS is categorised as mild, moderate, or severe, defined by the Berlin definition25  
  
===== SOURCE PAGE 101 =====
 
101 
 
TABLE 4 - EXPLORATORY SECONDARY OUTCOMES (IN-HOSPITAL) 
Variable Definition 
Initial surgery duration after trauma centre treatment minutes 
Referring ward after initial surgery after trauma centre 
treatment 
Intensive Care Unit, Ward 
Intensive Care Unit admission (y/n) 
 
Brain injury within 7 days of admission (y/n) Including description based on the patient's 
medical record 
Myocardial infarction within 7 days (y/n) 
 
Cerebral ischaemia within 7 days (y/n) 
 
Episodes of hypoxaemia (y/n) Number of times with SpO2 <90% in the 
data collection sheet 
Intubation post randomisation (y/n) During and after intervention 
If yes, location, time and date of intubation Pre-hospital, Trauma Centre, Intensive Care 
Unit 
 
 
Mechanical ventilation initiated as part of 
general anaesthesia on spontaneously 
breathing patients to facilitate surgery is not 
included  
Extubation (y/n) 
 
Re-intubation (y/n) 
 
Total number of intubations within 30 days number 
Time on mechanical ventilation (hours)* Number of ventilator hours within 30 days 
after enrolment
 
  
Days alive without mechanical ventilation (days) Number of ventilator-free days within 30 
days after enrolment 
Days alive outside the Intensive Care Unit within 30 days number 
Intensive Care Unit Length of Stay days 
Intensive Care Unit re-admission(s) (y/n) 
 
Hospital Length of Stay** days 
 
 
Sepsis during hospital admission (y/n) Clearly stated in the patient's medical record 
by a physician or assigned as a diagnosis 
Pneumonia post-discharge within 30 days after enrolment 
(y/n/patient still admitted after 30 days)
 
Evaluated through drugs prescribed after 
hospital discharge in countries where this 
information is available 
Surgical site infection(s) within 30 days (y/n) At least one of the following: purulent 
drainage, positive microbiologic testing from 
surgical site/wound and sign(s) of infection, 
diagnosis of surgical site infection by a 
surgeon 
*Mechanical ventilation initiated on spontaneously breathing patients to facilitate surgery is not included  
**Only the primary admission will be considered (no re-admissions) 
If a patient is transferred from the hospital to a psychiatry department or a rehabilitation centre for further 
treatment, then the day of transfer is considered the date of hospital discharge 
===== SOURCE PAGE 102 =====
 
102 
 
SUPPLEMENTAL TABLE 1 – ADVERSE EVENTS 
AND SERIOUS ADVERSE EVENTS 
Variable 
 
Adverse Event (AE)* 
Atelectasis (y/n)** 
 
Irritability of airway mucosa (y/n)*** 
 
Serious Adverse event (SAE)**** 
Death (y/n) 
 
Was life-threatening (y/n) 
 
Involved or prolonged hospital length of stay 
(y/n) 
 
Involved persistence of significant disability 
or incapacity (y/n) 
 
Resulted in a congenital anomaly or birth 
defect (y/n) 
 
*Any untoward medical occurrence as registered by clinicians in a subject to whom a medicinal product is 
administered, and which does not necessarily have a causal relationship with this treatment; only the first AE 
of either atelectasis or irritability of airway mucosa will be recorded during admission (maximum of 30 days) 
**Only atelectases assessed by a radiologist are recorded 
***Recorded only if registered by the health care staff in the medical record 
****Any untoward medical occurrence that at any dose requires inpatient hospitalisation or prolongation of 
existing hospitalisation (including all re-admissions), results in persistent or significant disability or 
incapacity, results in a congenital anomaly or birth defect, is life-threatening, or results in death. Must be 
classified as either A) SUSAR (SAE is both related and unexpected) B) SAR (SAE is related but not 
unexpected) or C) SAE (SAE is not related and not unexpected)  
===== SOURCE PAGE 103 =====
 
103 
 
Figure 1 
CONSORT flow diagram of screening, randomisation and follow-up 
 
 
 
 
 
```

### DOC-003 REPORT pp1–26

```text

===== SOURCE PAGE 1 =====
Supplemental Online Content 
Arleth T, Baekgaard J, Siersma V, et al; TRAUMOX2 Trial Group. Early restrictive 
vs liberal oxygen for trauma patients: the TRAUMOX2 randomized clinical trial. 
JAMA. Published online December 10, 2024. doi:10.1001/jama.2024.25786 
 
eMethods 
eFigure. Oxygen Intervention Characteristics 
eTable 1. Additional Characteristics of Patient Enrollment Location and Receiving 
Trauma Center 
eTable 2. Additional Characteristics of Patients 
eTable 3. Oxygen Intervention Characteristics 
eTable 4. Primary and Key Secondary Outcomes 
eTable 5. Categorical Exploratory Outcomes 
eTable 6. Continuous Exploratory Outcomes 
eTable 7. Adjusted Subgroup Analyses 
eTable 8. Per-Protocol Analyses of Primary and Key Secondary Outcomes 
eTable 9. Adverse Events (AE) and Serious Adverse Events (SAE) 
eTable 10. Distribution of Oxygen Interventions Among the Post-Randomization 
Excluded Patients 
eTable 11. Best/Worst Case Scenario: Primary and Key Secondary Outcomes 
This supplemental material has been provided by the authors to give readers additional 
information about their work. 
  
===== SOURCE PAGE 2 =====
2 
 
© 2024 American Medical Association. All rights reserved. 
TABLE OF CONTENTS 
 
1. The TRAUMOX2 Trial Group ......................................................................................................................... 4 
1.1 Steering committee ........................................................................................................................................ 4 
1.2 Trial statistician.............................................................................................................................................. 4 
1.3 Investigators ................................................................................................................................................... 4 
1.4 Primary outcome assessors ............................................................................................................................ 4 
1.5 Data Monitoring and Safety Committee (DMSC) ......................................................................................... 5 
2. Participating Prehospital Bases and Trauma Centers ................................................................................... 5 
2.1 Prehospital bases ............................................................................................................................................ 5 
2.1.1 Denmark ................................................................................................................................................. 5 
2.1.2 The Netherlands ..................................................................................................................................... 6 
2.1.3 Switzerland ............................................................................................................................................. 6 
2.2 Trauma centers............................................................................................................................................... 6 
2.2.1 Denmark ................................................................................................................................................. 6 
2.2.2 The Netherlands ..................................................................................................................................... 6 
2.2.3 Switzerland ............................................................................................................................................. 7 
3. Supplementary Methods.................................................................................................................................... 7 
3.1 Research ethics committee/IRB approvals .................................................................................................... 7 
3.2 Details on intervention data ........................................................................................................................... 7 
3.3 Details on outcomes ....................................................................................................................................... 7 
3.3.1 Primary outcome and key secondary outcomes ..................................................................................... 7 
3.3.2 Exploratory outcomes............................................................................................................................. 9 
3.4 Adverse Events (AEs), Serious Adverse Events (SAEs) and Suspected Unexpected Serious Adverse 
Reactions (SUSARs).......................................................................................................................................... 10 
3.5 Major protocol violations of oxygenation ................................................................................................... 11 
3.6 Protocol deviations ...................................................................................................................................... 11 
3.7 Details on statistical analyses ...................................................................................................................... 11 
3.7.1 Blinding while analyzing...................................................................................................................... 11 
3.7.2 Handling of missing outcome data ....................................................................................................... 11 
4. Supplementary Results .................................................................................................................................... 13 
4.1 eFigure ......................................................................................................................................................... 13 
eFigure. Oxygen Intervention Characteristics ............................................................................................... 13 
4.2 eTables ......................................................................................................................................................... 14 
eTable 1. Additional Characteristics of Patient Enrollment Location and Receiving Trauma Center ......... 14 
eTable 2. Additional Characteristics of Patients ........................................................................................... 15 
eTable 3. Oxygen Intervention Characteristics ............................................................................................. 16 
eTable 4. Primary and Key Secondary Outcomes......................................................................................... 17 
eTable 5. Categorical Exploratory Outcomes ............................................................................................... 18 
eTable 6. Continuous Exploratory Outcomes ............................................................................................... 19 
eTable 7. Adjusted Subgroup Analyses ........................................................................................................ 20 
===== SOURCE PAGE 3 =====
3 
 
© 2024 American Medical Association. All rights reserved. 
eTable 8. Per-Protocol Analyses of Primary and Key Secondary Outcomes ............................................... 22 
eTable 9. Adverse Events (AE) and Serious Adverse Events (SAE) ¶ ......................................................... 23 
eTable 10. Distribution of Oxygen Interventions Among the Post-Randomization Excluded Patients ....... 24 
eTable 11. Best/Worst Case Scenario: Primary and Key Secondary Outcomes ........................................... 25 
References ............................................................................................................................................................. 26 
 
 
 
  
===== SOURCE PAGE 4 =====
4 
 
© 2024 American Medical Association. All rights reserved. 
1. The TRAUMOX2 Trial Group 
 
1.1 Steering committee 
 
Jacob Steinmetz (chief investigator and sponsor), Tobias Arleth (coordinating investigator), Josefine Baekgaard, 
Markus Klimek, Jochen Hinkelbein, and Lars Simon Rasmussen. 
 
1.2 Trial statistician  
 
Volkert Siersma. 
 
1.3 Investigators 
 
Listed by country and hospital. 
 
Denmark 
 
Hospital Names 
Rigshospitalet, Copenhagen 
University Hospital 
Jacob Steinmetz (chief investigator and sponsor), Tobias Arleth 
(coordinating investigator), Josefine Baekgaard, Felicia Dinesen, Lars 
Simon Rasmussen, Andreas Creutzburg, Oscar Rosenkrantz, Johan 
Heiberg, Dan Isbye 
Odense University Hospital Søren Mikkelsen (primary investigator), Stine Thorhauge Zwisler, Louise 
Breum Petersen, Peter Martin Hansen, Søren Darling, Maria Charlotte 
Reiersøl Mørkeberg 
Aarhus University Hospital Mikkel Andersen (primary investigator), Christian Fenger-Eriksen, Peter 
Trappaud Bach 
 
The Netherlands 
 
Hospital Names 
Erasmus MC, University 
Medical Center Rotterdam 
Mark G. Van Vledder (primary investigator), Esther M.M. Van Lieshout, 
Dennis Den Hartog, Markus Klimek, Niki A. Ottenhof, Iscander M. 
Maissan 
 
Switzerland 
 
Hospital Names 
Inselspital Bern Wolf E. Hautz (primary investigator), Dominik A. Jacob, Roland Albrecht, 
Matthias Haenggi, Manuela Iten 
 
1.4 Primary outcome assessors 
 
Listed by country. 
 
Denmark 
 
Peter Martin Hansen, Johan Heiberg, Lars Simon Rasmussen, Dan Isbye. 
 
The Netherlands 
 
Iscander M. Maissan, Niki A. Ottenhof. 
===== SOURCE PAGE 5 =====
5 
 
© 2024 American Medical Association. All rights reserved. 
Switzerland 
 
Matthias Haenggi, Manuela Iten. 
 
1.5 Data Monitoring and Safety Committee (DMSC) 
 
Bodil Steen Rasmussen (chair of the DMSC), M.D., Ph.D. 
Professor 
Department of Anesthesia and Intensive Care, Aalborg University Hospital 
 
Lars Wiuff Andersen, M.D., Ph.D., M.P.H, D.M.Sc. 
Professor 
Department of Anesthesiology and Intensive Care Medicine, Aarhus University Hospital,  
Research Center for Emergency Medicine, Aarhus University Hospital and Aarhus University, Prehospital 
Emergency Medical Services, Central Denmark Region 
 
Marius Rehn, M.D., Ph.D. 
Professor, Consultant Anaesthesiologist and pre-hospital critical care doctor 
Department of Research and Development, Norwegian Air Ambulance Foundation Oslo, Norway  
Air Ambulance Department, Division of Prehospital Services, Oslo University Hospital, Norway Faculty of 
Health Sciences, University of Stavanger, Stavanger, Norway 
 
Brice Ozenne, Biostatistician, Ph.D. 
Associate professor 
Department of Public Health, Section of Biostatistics, University of Copenhagen, Denmark  
Neurobiology Research Unit and BrainDrugs, Copenhagen University Hospital, Rigshospitalet Denmark 
 
2. Participating Prehospital Bases and Trauma Centers 
 
2.1 Prehospital bases 
 
2.1.1 Denmark 
 
Physician staffed Critical Care Units (physician-staffed ambulance vehicles) 
 
All physician staffed Critical Care Units have one referring trauma center. 
 
Referring trauma center Critical Care Unit 
Rigshospitalet, Copenhagen 
University Hospital 
Physician staffed Critical Care Unit 1 and 2 – City: Copenhagen (2 
vehicles) 
Physician staffed Critical Care Unit 3 – South: Hvidovre (1 vehicle) 
Physician staffed Critical Care Unit 4 – North: Hilleroed (1 vehicle) 
Physician staffed Critical Care Unit 5 – Center: Herlev (1 vehicle) 
Odense University Hospital Physician staffed Critical Care Unit: Odense (1 vehicle) 
Aarhus University Hospital Physician staffed Critical Care Unit: Aarhus (1 vehicle) 
Physician staffed Critical Care Unit: Randers (1 vehicle) 
 
Helicopter Emergency Medical Services (HEMS) 
 
City Air Ambulance 
Ringsted Danish Air Ambulance Ringsted 
Billund Danish Air Ambulance Billund 
===== SOURCE PAGE 6 =====
6 
 
© 2024 American Medical Association. All rights reserved. 
Skive Danish Air Ambulance Skive 
Saltum Danish Air Ambulance Saltum 
 
2.1.2 The Netherlands 
 
City Air Ambulance 
Rotterdam Lifeliner 2 Helicopter Emergency Medical Services (including a physician-
staffed ambulance vehicle) 
 
2.1.3 Switzerland 
 
Helicopter Emergency Medical Services (HEMS) 
 
City Air Ambulance 
Bern REGA 3 
Wilderswil REGA 10 
Zweisimmen REGA 14 
 
2.2 Trauma centers 
 
Participating trauma centers should be able to provide definitive treatment of trauma patients (i.e., no transfer to 
more specialized institution needed), possess a trauma registry, and have a minimum average of approximately 
400 trauma team activations per year. 
 
2.2.1 Denmark 
 
City Trauma department 
Copenhagen Department of Anesthesia 
Center of Head and Orthopedics 
Rigshospitalet, University of Copenhagen 
Inge Lehmanns Vej 6, DK-2100 Copenhagen 
Odense Department of Anesthesiology and Intensive Care 
Odense University Hospital 
J. B. Winsløws Vej 4, DK-5000 Odense 
Aarhus Department of Anesthesiology 
Aarhus University Hospital 
Palle Juul-Jensens Boulevard 99, DK-8200 Aarhus 
 
2.2.2 The Netherlands 
 
City Trauma department 
Rotterdam Emergency Department 
Erasmus MC, University Medical Center Rotterdam 
P.O. Box 2040, 3000 CA Rotterdam 
 
 
===== SOURCE PAGE 7 =====
7 
 
© 2024 American Medical Association. All rights reserved. 
2.2.3 Switzerland 
 
City Trauma department 
Bern Department of Emergency Medicine 
Inselspital University Hospital Bern 
Rosenbühlgasse 27, 3010 Bern 
 
3. Supplementary Methods 
 
3.1 Research ethics committee/IRB approvals 
 
Country Ethics approval 
Denmark The Regional Scientific Ethical Committee, approval no. H-21018062 
First approved October 20, 2021 
The approval was given to all participating sites in Copenhagen, Odense, and Aarhus 
with the coordinating site in Copenhagen as the applicant 
The Netherlands Medical Research Ethics Committee Erasmus MC, approval no. MEC-2021 
First approved February 24, 2022 
Switzerland Ethics Committee of the Canton Bern, approval no. 2022-01335 
First approved November 1, 2022 
 
3.2 Details on intervention data 
 
The arterial oxyhemoglobin saturation measured by pulse oximetry (SpO2),the  type of oxygen delivery, flow 
(liters of oxygen per minute), and fraction of inspired oxygen (FiO2) values were collected and registered hourly. 
In case of missing values on the data collection sheet, an approximated hourly median value of SpO2, flow and 
FiO2 were used from the medical record. The use of high-flow nasal cannula was noted on the data collection 
sheet as a non-rebreather mask. In case more arterial blood gasses (ABGs) were obtained in the intervention 
period besides the protocolized two ABGs at 1 hour ± 30 minutes and 6 hours ± 2 hours after randomization, the 
results from the ABG closest to the designated time points were used. 
 
3.3 Details on outcomes 
 
3.3.1 Primary outcome and key secondary outcomes 
 
The primary outcome was a composite of death and/or major respiratory complications within 30 days. Major 
respiratory complications were defined as pneumonia based on the Centers for Disease Control and Prevention 
(CDC) criteria1 and/or acute respiratory distress syndrome (ARDS) based on the Berlin definition.2 Assessment 
of the primary outcome was blinded for the assessors. All primary outcome assessors were asked to guess the 
treatment allocation in their assessments. The key secondary outcomes were death and major respiratory 
complications within 30 days individually. 
 
Death 
 
Investigators registered death within 30 days using the medical record or national/local registries. If that was not 
possible, for instance if the patient was a foreigner, death within 30 days was assessed by contacting the patient 
or relatives by phone or e-mail at day 30 or after from the day of inclusion. At least three attempts on three 
different days were carried out. If no contact was obtained, and the patient was discharged to home from either 
the TRAUMOX2 participating site or subsequent receiving hospital, the patient was considered to be alive on 
day 30. However, if the patient was transferred to another hospital without medical record access for 
investigators, 30-day vital status was considered as missing data.  
 
 
 
===== SOURCE PAGE 8 =====
8 
 
© 2024 American Medical Association. All rights reserved. 
Major respiratory complications 
 
The blinded assessment of pneumonia and/or ARDS within 30 days from inclusion was based on the available 
medical record system. If the patient was transferred to another hospital, and the local medical record until day 
30 was not available, the assessment was based on the available medical record from the TRAUMOX2 
participating site only. However, an attempt of obtaining the medical record of the receiving facility was carried 
out and included in the primary outcome assessment if possible. Pneumonia and ARDS diagnoses were 
accompanied by dates of event. Pneumonia was categorized as non-ventilator associated pneumonia (PNEU) or 
ventilator-associated pneumonia (VAP); please see the criteria below. ARDS was categorized as mild, 
moderate, or severe; please see the criteria below. 
 
A shortened version of the pneumonia CDC criteria is shown below. Please see the reference for full details. 
 
Pneumonia CDC criteria1 
Pneumonia (PNEU) is identified by using a combination of imaging, clinical and laboratory criteria. 
 
Date of event: For a PNEU/VAP the date of event is the date when the first element used to meet the PNEU 
infection criterion occurred for the first time within the 7-day Infection Window Period. 
 
Ventilator-associated pneumonia (VAP): A pneumonia where the patient is on mechanical ventilation for >2 
calendar days on the date of event, with day of ventilator placement being Day 1,*  
AND 
the ventilator was in place on the date of event or the day before. 
*If the ventilator was in place prior to inpatient admission, the ventilator day count begins with the admission 
date to the first inpatient location. 
Imaging Test Evidence Signs/Symptoms 
Two or more serial chest imaging test results with at 
least one of the following: 
 
New and persistent  
or 
Progressive and persistent 
• Infiltrate 
• Consolidation  
• Cavitation 
 
Note: In patients without underlying pulmonary or 
cardiac disease (for example: respiratory distress 
syndrome, bronchopulmonary dysplasia, pulmonary 
edema, or chronic obstructive pulmonary disease), 
one definitive imaging test result is acceptable. 
For ANY PATIENT, at least one of the following: 
 
• Fever (>38.0°C or >100.4°F)  
• Leukopenia (≤4000 WBC/mm3) or leukocytosis 
(≥12,000 WBC/mm3)  
• For adults ≥70 years old, altered mental status with 
no other recognized cause 
 
And at least two of the following: 
 
• New onset of purulent sputum or change in 
character of sputum, or increased respiratory 
secretions, or increased suctioning requirements 
• New onset or worsening cough, or dyspnea, or 
tachypnea  
• Rales or bronchial breath sounds 
• Worsening gas exchange (for example: O2 
desaturations (for example: PaO2/FiO2 ≤240 mmHg), 
increased oxygen requirements, or increased 
ventilator demand) 
 
 
 
 
 
 
 
 
 
===== SOURCE PAGE 9 =====
9 
 
© 2024 American Medical Association. All rights reserved. 
Table 3 from the ARDS reference is shown below. Please see the reference for full details. 
 
The Berlin Definition of Acute Respiratory Distress Syndrome2 
Timing Within 1 week of a known clinical insult or new or worsening respiratory 
symptoms 
Chest imaginga Bilateral opacities—not fully explained by effusions, lobar/lung collapse, or 
nodules 
Origin of edema Respiratory failure not fully explained by cardiac failure or fluid overload  
Need objective assessment (eg, echocardiography) to exclude hydrostatic edema if 
no risk factor present 
Oxygenationb Mild: 200 mmHg < PaO2/FIO2 ≤ 300 mmHg with PEEP or CPAP ≥5cmH2Oc 
Moderate: 100 mmHg < PaO2/FIO2 ≤ 200 mmHg with PEEP ≥5cmH2O 
Severe: PaO2/FIO2 ≤ 100 mmHg with PEEP ≥5cmH2O 
Abbreviations: CPAP, continuous positive airway pressure; FIO2, fraction of inspired oxygen; PaO2, partial 
pressure of arterial oxygen; PEEP, positive end-expiratory pressure. 
aChest radiograph or computed tomography scan. 
bIf altitude is higher than 1000 m, the correction factor should be calculated as follows: [PaO2/FIO2 x 
(barometric pressure/760)]. 
cThis may be delivered noninvasively in the mild acute respiratory distress syndrome group. 
 
3.3.2 Exploratory outcomes  
 
Only exploratory outcomes that required further elaboration than what was stated in the statistical analysis plan 
is mentioned in the table below. 
 
Outcome Definition 
Episode(s) of 
hypoxemia during the 
eight-hour intervention 
Number of times the hourly collected SpO2 value from the data collection sheet 
was <90% 
Surgical site 
infection(s) within 30 
days 
At least one of the following stated in the medical record (based on the CDC 
criteria for a surgical site event3): 
• Purulent drainage 
• Positive microbiologic testing from surgical site/wound 
• Deliberately opened by a surgeon AND sign(s) of infection 
• Diagnosis of surgical site infection by a surgeon 
Ventilator hours within 
30 days 
Ventilator hours was defined as: 
Positive pressure ventilation at any time, including Bilevel Positive Airway 
Pressure (BiPAP)  
 
The following treatments were not considered as mechanical ventilation: 
Non-invasive ventilation (NIV), high flow nasal cannula or Continuous Positive 
Airway Pressure (CPAP) 
 
Endotracheal intubation and mechanical ventilation during surgery were not 
included in the above definitions if the patient was breathing spontaneously 
without an endotracheal tube before surgery. 
===== SOURCE PAGE 10 =====
10 
 
© 2024 American Medical Association. All rights reserved. 
 
Only mechanical ventilation started pre-hospital, in the trauma center or in the 
ICU was considered. Hour(s) were calculated as commenced hour(s) with no 
decimals (eg, 1 hour and 15 minutes on mechanical ventilation = 2 hours on 
mechanical ventilation) 
Ventilator-free days 
within 30 days 
The definition for being ventilated in the above was also applied here for 
calculating ventilator-free days. Days were calculated as commenced day(s) with 
no decimals (eg, 1 hour on mechanical ventilation = 1 day = 29 days ventilator-
free days) 
Days alive outside the 
ICU within 30 days 
Day(s) were calculated as commenced day(s) with no decimals (eg, 1 hour of ICU 
admission = 1 ICU day = 29 days alive outside the ICU) 
ICU length of stay (ICU 
LOS) 
Calculated as commenced day(s) with no decimals (eg, 25 hours of ICU admission 
= 2 ICU days) 
Hospital length of stay 
(HOS LOS) 
Calculated as commenced day(s) with no decimals (eg, 25 hours of admission = 2 
admission days) 
 
Only the primary admission was considered (no re-admissions).  
If a patient was transferred from one hospital to another hospital for further 
treatment related to the trauma, it was not considered a hospital discharge. 
If a patient was transferred from the hospital to a psychiatry department or a 
rehabilitation center for further treatment, then the day of transfer was considered 
the date of hospital discharge 
Sepsis during hospital 
admission 
Clearly stated in the patient's medical record by a physician or assigned as a 
diagnosis 
Pneumonia post-
discharge within 30 
days 
Depending on the site: Evaluated through drugs prescribed after hospital discharge 
in countries where this information was available or by calling the patients at the 
6-month follow-up  
 
We are still collecting long-term follow-up data at 6 and 12 months on functional outcome (GOSE) and quality 
of life (EQ-5D-5L). This will be presented later in the follow-up study. A statistical analysis plan for handling 
these data will become available on our trial website www.traumox2.org beforehand. 
  
3.4 Adverse Events (AEs), Serious Adverse Events (SAEs) and Suspected Unexpected Serious Adverse 
Reactions (SUSARs) 
 
We defined Adverse Events (AEs) as any untoward medical occurrence in a subject to whom a medicinal 
product is administered, and does not necessarily have a causal relationship with this treatment. This group of 
trial patients were expected to have a lot of complications due to trauma. It is the established practice in trials on 
critically ill patients that adverse events are part of the natural trajectory of the primary disease process or 
expected complications of the critical illness.4 Therefore, we chose to record only the following until discharge 
(but a maximum of 30 days) as AEs: 
 
• Atelectasis (only atelectases assessed by a radiologist were recorded) 
• Irritability of airway mucosa (recorded only if registered by the health care staff in the medical record) 
 
Only the first AE of either atelectasis or irritability of airway mucosa was recorded during admission (not a 
subsequent).  
 
We defined Serious Adverse Events (SAEs) as any untoward medical occurrence that resulted in death, was life-
threatening, involved or prolonged hospital length of stay (eg, re-admission), involved persistence of significant 
disability or incapacity or resulted in a congenital anomaly or birth defect. 
 
===== SOURCE PAGE 11 =====
11 
 
© 2024 American Medical Association. All rights reserved. 
To monitor AEs and SAEs, a TRAUMOX2 investigator would assess the trial participant’s medical record:  
 
• Once within the first 24 hours  
• Every third day until discharge (maximum of 30 days) 
 
Suspected Unexpected Serious Adverse Reactions (SUSARs) were not expected in this trial given the long-
standing history for the use of supplemental oxygen in medicine for over a century with its safety profile being 
well-investigated with no major safety concerns. 
 
3.5 Major protocol violations of oxygenation 
 
All patients with ≥1 major protocol violation of oxygenation were removed in the per-protocol analyses. The 
per-protocol population was the same as the modified intention-to-treat population with exclusion of the patients 
having one or more major protocol violations. 
 
A major protocol violation of oxygenation during the eight-hour intervention was defined as:  
 
Restrictive oxygen group 
Non-intubated patients Intubated patients 
Supplemental oxygen ≥3 liters of oxygen per minute 
AND SpO2 ≥98% recorded at two consecutive hourly 
time points on the data collection sheet 
FiO2 >0.4 AND SpO2 ≥98% recorded at two 
consecutive hourly time points on the data collection 
sheet 
 
Liberal oxygen group 
Non-intubated patients Intubated patients 
Supplemental oxygen <3 liters of oxygen per minute 
at two consecutive hourly time points on the data 
collection sheet 
FiO2 <0.4 at two consecutive hourly time points on 
the data collection sheet 
 
3.6 Protocol deviations 
 
For all TRAUMOX2 patients, it was possible to deviate from the protocol if clinically justified by the treating 
physician. Such deviations were always documented including the clinical justification in our database. 
 
3.7 Details on statistical analyses 
 
3.7.1 Blinding while analyzing 
 
The trial statistician was blinded to the treatment allocation, and the manuscript authors became blinded to the 
treatment allocation once the trial concluded and the data were exported for analysis. In the exported dataset, the 
randomization groups were renamed to eg, “GR12” and “GR17”, by an unblinded research assistant who was 
not otherwise involved in the trial. Subsequently, the renamed dataset was provided to the trial statistician for 
data analysis. 
 
3.7.2 Handling of missing outcome data 
 
If patients withdrew their consent once they regained consciousness, data up until that day were collected and 
stored. However, the participating sites’ individual approach were always according to national law. If data were 
available for time-dependent outcomes (eg, outcomes that were specified to be assessed 7 or 30 days after 
inclusion), the assessments were done dependent on the timing of withdrawal of consent. In case a time-
dependent outcome occurred within the period of available data for patients who withdrew consent, the outcome 
event was registered. If an outcome did not occur within the period of available data for a time-dependent 
outcome, the outcome was registered as missing data.  
===== SOURCE PAGE 12 =====
12 
 
© 2024 American Medical Association. All rights reserved. 
Missing outcome data, which covered patients who withdrew consent or were unavailable for follow-up, was 
adjusted for using inverse probability weighting.5 In this method, patients with available outcome data were 
weighted by the inverse of the probability of being observed. Specifically for the primary outcome, if major 
respiratory complications were not present before the consent was withdrawn, we considered both death and 
major respiratory complications within 30 days to be missing. The weights were calculated in a logistic 
regression model based on the allocation, the dominating injury type, the type of oxygen supply, psychiatric 
comorbidity and (for Danish patients) whether a personal identification number was registered, or the use of a 
temporary personal identification number. Adjustment of the variance matrix to reflect the weighting was 
included in the generalized estimating equations method. 
 
  
===== SOURCE PAGE 13 =====
13 
 
© 2024 American Medical Association. All rights reserved. 
4. Supplementary Results 
 
4.1 eFigure 
 
eFigure. Oxygen Intervention Characteristics 
 
 
Trauma patients allocated to either a restrictive or liberal oxygen strategy. The “Pre” term in panel A refers to the first SpO2 
measurement from the prehospital setting. SpO2: Arterial oxygen saturation measured by pulse oximetry. L/min: Liters per 
minute. FiO2: Fraction of inspired oxygen.  

===== SOURCE PAGE 14 =====
14 
 
© 2024 American Medical Association. All rights reserved. 
4.2 eTables 
 
eTable 1. Additional Characteristics of Patient Enrollment Location and 
Receiving Trauma Center 
Characteristics 
Restrictive  
oxygen group 
(N=750) 
Liberal  
oxygen group  
(N=758) 
Enrollment location – no./total no. (%)   
Prehospital   
Physician staffed Critical Care Unit 1 and 2 – City: 
Copenhagen, Denmark 62/750 (8.3) 68/758 (9.0) 
Physician staffed Critical Care Unit 3 – South: 
Hvidovre, Denmark 25/750 (3.3) 21/758 (2.8) 
Physician staffed Critical Care Unit 4 – North: 
Hilleroed, Denmark 25/750 (3.3) 26/758 (3.4) 
Physician staffed Critical Care Unit 5 – Center: Herlev, 
Denmark 34/750 (4.5) 36/758 (4.7) 
Danish Air Ambulance Ringsted, Denmark 40/750 (5.3) 37/758 (4.9) 
Danish Air Ambulance Billund, Denmark 21/750 (2.8) 23/758 (3.0) 
Danish Air Ambulance Skive, Denmark 17/750 (2.3) 18/758 (2.4) 
Danish Air Ambulance Saltum, Denmark 2/750 (0.3) 2/758 (0.3) 
Physician staffed Critical Care Unit: Odense, Denmark 38/750 (5.1) 39/758 (5.1) 
Physician staffed Critical Care Unit: Aarhus, Denmark 13/750 (1.7) 13/758 (1.7) 
Physician staffed Critical Care Unit: Randers, Denmark 1/750 (0.1) 0/758 (0.0) 
Lifeliner 2 Helicopter Emergency Medical Services 
(including a physician-staffed ambulance vehicle), 
Rotterdam, The Netherlands 
5/750 (0.7) 3/758 (0.4) 
REGA 3, Swiss-Air Ambulance, Bern, Switzerland 19/750 (2.5) 16/758 (2.1) 
REGA 10, Swiss-Air Ambulance, Wilderswil, 
Switzerland 3/750 (0.4) 3/758 (0.4) 
REGA 14, Swiss-Air Ambulance, Zweisimmen, 
Switzerland 3/750 (0.4) 2/758 (0.3) 
In-hospital   
Rigshospitalet, Copenhagen University Hospital, 
Denmark 150/750 (20.0) 160/758 (21.1) 
Odense University Hospital, Odense, Denmark 118/750 (15.7) 117/758 (15.4) 
Aarhus University Hospital, Aarhus, Denmark 62/750 (8.3) 58/758 (7.7) 
Erasmus MC, University Medical Center Rotterdam, 
Rotterdam, The Netherlands 87/750 (11.6) 90/758 (11.9) 
University Hospital Bern, Switzerland 25/750 (3.3) 26/758 (3.4) 
Receiving trauma center – no./total no. (%) (N=1508)   
Rigshospitalet, Copenhagen University Hospital, 
Denmark 335/750 (44.4) 348/758 (45.7) 
Odense University Hospital, Odense, Denmark 173/750 (22.9) 177/758 (23.2) 
Aarhus University Hospital, Aarhus, Denmark 100/750 (13.3) 93/758 (12.2) 
Erasmus MC, University Medical Center Rotterdam, 
Rotterdam, The Netherlands 92/750 (12.2) 93/758 (12.2) 
University Hospital Bern, Switzerland 50/750 (7.2) 47/758 (6.7) 
 
Trauma patients allocated to either a restrictive or liberal oxygen strategy. 
  
===== SOURCE PAGE 15 =====
15 
 
© 2024 American Medical Association. All rights reserved. 
eTable 2. Additional Characteristics of Patients 
Characteristics 
Restrictive  
oxygen group 
(N=750) 
Liberal  
oxygen group  
(N=758) 
Body Mass Index – kg/m2 25.0 (22.5-28.1) 
[n=628] 
25.0 (22.8-27.8) 
[n=615] 
Mechanism of injury – no./total no. (%)   
Traffic: Motor vehicle accident 147/742 (19.8) 151/756 (20.0) 
Traffic: Motorcycle accident 74/742 (10.0) 70/756 (9.3) 
Traffic: Bicycle accident 109/742 (14.7) 108/756 (14.3) 
Traffic: Pedestrian 53/742 (7.1) 50/756 (6.6) 
Traffic: Other (eg, ship, airplane, or railway train) 14/742 (1.9) 19/756 (2.5) 
Shot by handgun, shotgun, rifle or other firearm of any 
caliber 8/724 (1.1) 6/756 (0.8) 
Stabbed by knife, sword, dagger, other pointed or sharp 
object 69/742 (9.3) 68/756 (9.0) 
Struck or hit by blunt object 51/742 (6.9) 58/756 (7.7) 
Fall: 0-2 meters 82/742 (11.1) 69/756 (9.1) 
Fall: 2-4 meters 66/742 (8.9) 68/756 (9.0) 
Fall: >4 meters 58/742 (7.8) 57/756 (7.5) 
Blast/explosion 3/742 (0.4) 4/756 (0.5) 
Other 8/742 (1.1) 28/756 (3.7) 
Type of transport to the trauma center – no./total no. (%)   
Ground ambulance 583/747 (78.0) 585/743 (78.7) 
Helicopter ambulance 140/747 (18.7) 141/743 (19.0) 
A combination of ground ambulance and helicopter 
ambulance 14/747 (1.9) 9/743 (1.2) 
Private vehicle 1/747 (0.1) 3/743 (0.4) 
Walk-in 9/747 (1.2) 4/743 (5.3) 
Other 0/747 (0.0) 1/743 (0.1) 
Use of prehospital or in-hospital supplemental oxygen 
prior to randomization – no./total no. (%) 333/713 (46.7) 351/718 (48.9) 
Highest SpO2 measured prior to randomization – % 100 (97-100) 
[n=265] 
99 (97-100) 
[n=285] 
Body temperature measured on admission – oC 36.5 (35.9-37.0) 
[n=479] 
36.5 (35.9-36.9) 
[n=484] 
Surgery performed in the trauma resuscitation room   
   Neurosurgery – no./total no. (%) 3/744 (0.4) 1/747 (0.1) 
   Cardiothoracic surgery – no./total no. (%) 10/744 (1.3) 9/747 (1.2) 
   Abdominal surgery – no./total no. (%) 0/744 (0.0) 4/747 (0.5) 
   Orthopedic surgery – no./total no. (%) 2/744 (0.3) 1/747 (0.1) 
   Vascular surgery – no./total no. (%) 1/744 (0.1) 0/747 (1.1) 
   Other(s) – no./total no. (%) 1/744 (0.1) 1/747 (0.1) 
 
Trauma patients allocated to either a restrictive or liberal oxygen strategy. Continuous variables are presented as median with 
interquartile range. 
  
===== SOURCE PAGE 16 =====
16 
 
© 2024 American Medical Association. All rights reserved. 
eTable 3. Oxygen Intervention Characteristics 
Characteristic 
Restrictive  
oxygen group 
(N=750) 
Liberal  
oxygen group  
(N=758) 
Time from trauma to randomization – min (N=1268) 54 (35-79) 
[n = 633] 
52 (33-78) 
[n=635] 
Type of supplemental oxygen* – no./total no. (%)    
No supplemental oxygen 200/739 (27.1) 13/735 (1.8) 
Nasal cannula 171/739 (23.1) 45/735 (6.1) 
Non-rebreather mask 18/739 (2.4) 340/735 (46.2) 
Intubated (at any point during the intervention period) 350/739 (47.4) 337/735 (45.9) 
Hemoglobin hour 1 ± 30 min § – g/dL 12.9 (11.4-14.0) 
[n=602] 
12.7 (11.3-14.0) 
[n=603] 
Hemoglobin hour 6 ± 2 hours § – g/dL 12.5 (10.8-13.7) 
[n=482] 
12.4 (10.6-13.9) 
[n=487] 
Lactate hour 1 ± 30 min § – mmol/L 1.5 (0.9-2.5) 
[n=585] 
1.4 (0.9-2.4) 
[n=590] 
Lactate hour 6 ± 2 hours § – mmol/L 1.4 (0.9-2.2) 
[n=472] 
1.4 (0.9-2.1) 
[n=479] 
Major protocol violation ¶ – no./total no. (%)  50/742 (6.7) 102/744 (13.7) 
Protocol deviation † – no./total no. (%) 40/741 (5.4) 17/738 (2.3) 
 
Trauma patients allocated to either a restrictive or liberal oxygen strategy. The time from trauma to randomization is presented 
with a median and interquartile range.  
* The data collection sheet consisted of eight hourly data points (H1-H8). The sum of no supplemental oxygen, nasal cannula, 
non-rebreather mask or intubated is 100%. Patients are in the no supplemental oxygen category if none of the eight data points 
were nasal cannula, non-rebreather mask or intubated. If just one of the eight data points was intubated, the patient was 
categorized as intubated. Patients could receive both supplemental oxygen via a nasal cannula and non-rebreather mask 
during the 8-hour intervention period at different time points and were registered in the appropriate category based on the 
majority of the data points from the sheet. In case they were evenly distributed, the patient was registered in the non-rebreather 
mask category. 
§ The 1st and 2nd arterial blood gases during the oxygen intervention were obtained at hour 1 ± 30 min after randomization and 
hour 6 ± 2 hours after randomization, respectively.  
¶ See page 10 for definitions of major protocol violations.  
† See page 10 for definition of protocol deviations.
===== SOURCE PAGE 17 =====
17 
 
© 2024 American Medical Association. All rights reserved. 
eTable 4. Primary and Key Secondary Outcomes 
 
Restrictive 
oxygen 
group 
Liberal  
oxygen 
group 
Odds ratio  
(95% CI) P value Adjusted odds 
ratio (95% CI) P value 
Adjusted odds 
ratio + smoking 
(95% CI) 
P value 
Primary outcome         
Death and/or major 
respiratory complications – 
no./total no. (%)  
118/733 
(16.1) 
121/724 
(16.7) 
1.01 
(0.75 to 1.37) 0.94 0.98 
(0.68 to 1.41) 0.92 1.05 
(0.73 to 1.49) 0.80 
Key secondary outcomes         
Death – no./total no. (%) 63/733 (8.6) 53/724 (7.3) 1.28 
(0.85 to 1.92) 0.23 1.37 
(0.80 to 2.38) 0.25 1.37 
(0.80 to 2.33) 0.26 
Major respiratory 
complications – no./total 
no. (%) 
65/733 (8.9) 78/724 (10.8) 0.84 
(0.59 to 1.19) 0.33 0.84 
(0.57 to 1.23) 0.38 0.90 
(0.61 to 1.32) 0.58 
 
Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. Death and major respiratory complications were both evaluated within 30 days. The smoking variable 
reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients. 
 
  
===== SOURCE PAGE 18 =====
18 
 
© 2024 American Medical Association. All rights reserved. 
eTable 5. Categorical Exploratory Outcomes 
 
Restrictive 
oxygen 
group 
Liberal  
oxygen 
group 
Odds ratio  
(95% CI) P value Adjusted odds 
ratio (95% CI) P value 
Adjusted odds 
ratio + smoking 
(95% CI) 
P value 
Presence of any 
hypoxemic episodes (SpO2 
<90%) * – no./total no. (%) 
44/737 (6.0) 28/737 (3.8) 1.67 
(1.02 to 2.70) 0.04 1.72 
(1.04 to 2.78) 0.03 1.69 
(1.04 to 2.78) 0.04 
ICU re-admission(s) – 
no./total no. (%) † 17/368 (4.6) 18/352 (5.1) 0.59 
(0.26 to 1.37) 0.22 0.60 
(0.25 to 1.43) 0.25 0.57 
(0.25 to 1.32) 0.19 
Sepsis during hospital 
admission – no./total no. 
(%) 
19/736 (2.6) 31/727 (4.3) 0.55 
(0.30 to 1.02) 0.06 0.53 
(0.29 to 1.00) 0.05 0.52 
(0.27 to 1.00) 0.05 
Surgical site infection(s) 
within 30 days – no./total 
no. (%) 
23/736 (3.1) 32/724 (4.4) 0.50 
(0.25 to 0.99) 0.05 0.49 
(0.26 to 0.93) 0.03 0.51 
(0.27 to 0.96) 0.04 
Pneumonia post-discharge 
within 30 days after 
enrollment ¶ – no./total no. 
(%) 
27/640 (4.2) 24/620 (3.9) 1.06 
(0.60 to 1.85) 0.86 1.04 
(0.59 to 1.85) 0.89 1.03 
(0.57 to 1.85) 0.93 
Brain injury within 7 days of 
admission – no./total no. 
(%) 
290/738 
(39.3) 
275/732 
(37.6) 
1.11 
(0.88 to 1.41) 0.35 1.05 
(0.82 to 1.35) 0.68 1.04 
(0.81 to 1.33) 0.74 
Myocardial infarction within 
7 days – no./total no. (%) 0/738 (0.0) 1/730 (0.1) - - - - - - 
Cerebral ischemia within 7 
days – no./total no. (%) 16/738 (2.2) 10/730 (1.4) 1.56 
(0.68 to 3.57) 0.30 1.45 
(0.63 to 3.45) 0.38 1.47 
(0.64 to 3.45) 0.36 
ICU admission – no./total 
no. (%) 
374/738 
(50.7) 
359/736 
(48.8) 
1.16 
(0.90 to 1.49) 0.24 1.01 
(0.76 to 1.33) 0.95 1.01 
(0.76 to 1.33) 0.95 
 
Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. No exploratory outcomes were statistically significant between the groups after adjusting for multiple 
testing. The smoking variable reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients. 
* Defined as any hypoxemic episodes (SpO2 <90%) during the eight-hour intervention from the hourly collected SpO2 values.  
† ICU: Intensive care unit.  
¶ Only patients discharged within 30 days were eligible for evaluation of pneumonia post-discharge. 
 
 
===== SOURCE PAGE 19 =====
19 
 
© 2024 American Medical Association. All rights reserved. 
eTable 6. Continuous Exploratory Outcomes 
 
Restrictive 
oxygen 
group 
Liberal  
oxygen 
group 
Mean difference  
(95% CI) P value 
Adjusted mean 
difference  
(95% CI) 
P value 
Adjusted mean 
difference + 
smoking  
(95% CI) 
P value 
Initial surgery duration after 
trauma resuscitation room 
treatment – min 
114 (64-166) 
[n=165] 
113 (68-149) 
[n=161] 
10.3 
(-8.8 to 29.3) 0.29 12.6 
(-7.4 to 32.6) 0.22 15.4 
(-4.3 to 35.0) 0.13 
Time on mechanical 
ventilation – hours 
0 (0-14) 
[n=735] 
0 (0-12) 
[n=725] 
4.8 
(-7.6 to 17.2) 0.45 3.3 
(-8.7 to 15.2) 0.59 3.7 
(-8.1 to 15.6) 0.54 
Days alive without 
mechanical ventilation – 
days 
30 (29-30) 
[n=735] 
30 (29-30) 
[n=723] 
-0.6 
(-1.4 to 0.2) 0.16 -0.4 
(-1.1 to 0.3) 0.27 -0.5 
(-1.2 to 0.2) 0.20 
Intensive Care Unit Length 
of Stay – days 
2 (1-9) 
[n=368] 
2 (1-7) 
[n=357] 
1.1 
(-0.2 to 2.5) 0.10 1.0 
(-0.4 to 2.3) 0.17 1.0 
(-0.4 to 2.5) 0.16 
Days alive outside the 
Intensive Care Unit within 
30 days – days 
29 (26-30) 
[n=736] 
30 (27-30) 
[n=724] 
-0.8 
(-1.7 to 0.1) 0.09 -0.5 
(-1.3 to 0.2) 0.17 -0.6 
(-1.3 to 0.2) 0.12 
Hospital Length of Stay – 
days 
7 (3-15) 
[n=736] 
7 (3-15) 
[n=728] 
-0.7 
(-2.3 to 0.9) 0.41 -1.0 
(-2.3 to 0.6) 0.23 -1.0 
(-2.5 to 0.6) 0.23 
 
Trial outcomes for trauma patients allocated to either a restrictive or liberal oxygen strategy. All continuous variables are presented as medians with interquartile ranges in the group allocation 
columns. No exploratory outcomes were statistically significant between the groups after adjusting for multiple testing. The smoking variable reflects only active smokers, identified from medical 
records and, in some cases, confirmed directly with patients. 
* Patients still admitted at day 30 were not eligible for evaluation of pneumonia post-discharge. 
 
  
===== SOURCE PAGE 20 =====
20 
 
© 2024 American Medical Association. All rights reserved. 
eTable 7. Adjusted Subgroup Analyses 
 Restrictive  
oxygen group 
Liberal  
oxygen group Odds ratio (95% CI) Adjusted odds ratio (95% CI) 
 no. of events/total no. of patients (%)   
All patients 118/733 (16.1) 121/724 (16.7) 1.01  
(0.75 to 1.37) 
0.98 
(0.68 to 1.39) 
Intubated at randomization     
No 56/558 (10.0) 50/543 (9.2) 1.12 
(0.75 to 1.67) 
1.16 
(0.73 to 1.85) 
Yes 62/175 (35.4) 71/181 (39.2) 0.90 
(0.57 to 1.41) 
0.76 
(0.45 to 1.30) 
ICU admission     
No 42/458 (9.2) 50/481 (10.4) 0.98 
(0.64 to 1.49) 
0.89 
(0.56 to 1.43) 
Yes 74/271 (27.3) 68/238 (28.6) 0.96 
(0.63 to 1.49) 
0.98 
(0.58 to 1.67) 
Moderate or severe traumatic brain 
injury *     
AIS < 3 45/500 (9.0) 48/473 (9.2) 1.06 
(0.68 to 1.64) 
1.11 
(0.68 to 1.85) 
AIS ≥ 3  73/233 (31.3) 73/202 (36.1) 0.81 
(0.53 to 1.25) 
0.83 
(0.51 to 1.37) 
Known lung disease     
No  97/667 (14.5) 105/643 (16.3) 0.88 
(0.65 to 1.22) 
0.95 
(0.65 to 1.39) 
Yes  19/59 (32.2) 14/69 (20.2) 1.85 
(0.73 to 4.55) 
1.06 
(0.40 to 2.86) 
Site of inclusion     
Prehospital  48/303 (15.8) 54/296 (18.2) 0.81 
(0.51 to 1.28) 
0.95 
(0.55 to 1.64) 
In-hospital 70/430 (16.3) 67/428 (15.7) 1.19 
(0.81 to 1.79) 
0.98 
(0.63 to 1.52) 
Injury severity score †     
===== SOURCE PAGE 21 =====
21 
 
© 2024 American Medical Association. All rights reserved. 
 Restrictive  
oxygen group 
Liberal  
oxygen group Odds ratio (95% CI) Adjusted odds ratio (95% CI) 
 no. of events/total no. of patients (%)   
ISS ≤ 15 22/380 (5.8) 19/389 (4.9) 1.33 
(0.69 to 2.56) 
1.14 
(0.56 to 2.33) 
ISS > 15 95/352 (27.0) 100/329 (30.4) 0.86 
(0.60 to 1.23) 
0.93 
(0.62 to 1.40) 
 
Adjusted subgroup analyses for trauma patients allocated to either a restrictive or liberal oxygen strategy.  
* Moderate or severe traumatic brain injury was evaluated by a score of 3 or higher on the AIS (Abbreviated Injury Scale) from the head/neck codes, but only head codes were selected.  
† Injury Severity Score: ISS. 
 
  
===== SOURCE PAGE 22 =====
22 
 
© 2024 American Medical Association. All rights reserved. 
eTable 8. Per-Protocol Analyses of Primary and Key Secondary Outcomes ¶ 
 
Restrictive 
oxygen 
group 
(N=700) 
Liberal  
oxygen 
group 
(N=656) 
Odds ratio  
(95% CI) P value Adjusted odds 
ratio (95% CI) P value 
Adjusted odds 
ratio + smoking 
(95% CI) 
P 
value 
Primary outcome         
Death and/or major 
respiratory complications – 
no./total no. (%)  
104/683 
(15.2) 
105/627 
(16.7) 
0.98 
(0.71 to 1.35) 0.91 0.97 
(0.67 to 1.41) 0.87 1.04 
(0.71 to 1.52) 0.83 
Key secondary outcomes         
Death – no./total no. (%) 54/683 (7.9) 44/627 (7.0) 1.27 
(0.82 to 2.00) 0.29 1.25 
(0.70 to 2.22) 0.45 1.22 
(0.69 to 2.17) 0.49 
Major respiratory 
complications – no./total 
no. (%) 
58/685 (8.5) 69/629 (11.0) 0.78 
(0.54 to 1.14) 0.20 0.82 
(0.54 to 1.23) 0.34 0.89 
(0.59 to 1.33) 0.58 
 
Per-protocol analyses of trauma patients allocated to either a restrictive or liberal oxygen strategy. Death and major respiratory complications were both evaluated within 30 days. The smoking 
variable reflects only active smokers, identified from medical records and, in some cases, confirmed directly with patients. 
¶ See page 10 for definitions of major protocol violations.
===== SOURCE PAGE 23 =====
23 
 
© 2024 American Medical Association. All rights reserved. 
eTable 9. Adverse Events (AE) and Serious Adverse Events (SAE) ¶ 
 
Restrictive  
oxygen group 
(N=750) 
Liberal  
oxygen group 
(N=758) 
Adverse event (AE) – no./total no. (%)   
   Atelectasis 207/750 (27.6) 263/758 (34.7) 
   Irritability of airway mucosa 16/750 (2.1) 20/758 (2.6) 
Serious adverse event (SAE) – no./total no. (%)   
   Death 63/750 (8.4) 53/758 (7.0) 
   Was life-threatening 8/750 (1.1) 13/758 (1.7) 
   Involved or prolonged hospital length of stay 29/750 (3.9) 37/758 (4.9) 
   Involved persistence of significant disability or incapacity 0/750 (0.0) 0/758 (0.0) 
   Resulted in a congenital anomaly or birth defect 0/750 (0.0) 1/758 (0.1) 
 
¶ See page 9 for the definitions of AE and SAE registration. There is a difference in the denominator of the patients for both 
groups compared to the outcome tables because patients were observed for AEs and SAEs up until a potential consent 
withdrawal. In case consent was withdrawn and no event was registered, the patient was registered as having no events and 
included in this table. No Serious Adverse Reactions (SAR) or Suspected Unexpected Serious Adverse Reactions (SUSAR) 
were registered. 
  
===== SOURCE PAGE 24 =====
24 
 
© 2024 American Medical Association. All rights reserved. 
eTable 10. Distribution of Oxygen Interventions Among the Post-
Randomization Excluded Patients ¶ 
 
Restrictive  
oxygen group 
(N=750) 
Liberal  
oxygen group 
(N=758) 
Exclusion after randomization – no./total no. (%) (N=130) 55/750 (45) 67/758 (55) 
Secondary exclusion – no./total no. (%) (N=341) * 174/750 (51) 165/758 (49) 
 
¶ Detailed numbers on the post-randomization excluded patients from Figure 1 in the main manuscript. 
* Two patients had missing data on the randomized oxygen intervention, which is the reason for the discrepancy between 
N=341 and the numbers in the table. 
  
===== SOURCE PAGE 25 =====
25 
 
© 2024 American Medical Association. All rights reserved. 
eTable 11. Best/Worst Case Scenario: Primary and Key Secondary Outcomes 
 Restrictive 
oxygen group 
Liberal  
oxygen group 
Odds ratio  
(95% CI) P value 
Primary outcome     
Missing not counted as 
event: Death and/or major 
respiratory complications – 
no./total no. (%)  
118/750 (15.7) 121/758 (16.0) 0.99 
(0.74 to 1.33) 0.96 
Missing counted as event: 
Death and/or major 
respiratory complications – 
no./total no. (%) 
135//750 (18.0) 155/758 (20.4) 0.85 
(0.65 to 1.11) 0.24 
Key secondary outcomes     
Missing not counted as 
event: Death – no./total no. 
(%) 
63/750 (8.4) 53/758 (7.0) 1.28 
(0.86 to 1.92) 0.22 
Missing counted as event: 
Death – no./total no. (%) 80/750 (10.7) 87/758 (11.4) 0.93 
(0.68 to 1.30) 0.70 
Missing not counted as 
event: Major respiratory 
complications – no./total 
no. (%) 
65/750 (8.7) 78/758 (10.3) 0.82 
(0.57 to 1.16) 0.26 
Missing counted as event: 
Major respiratory 
complications – no./total 
no. (%) 
82/750 (10.9) 112/758 (14.8) 0.70 
(0.52 to 0.95) 0.02 
===== SOURCE PAGE 26 =====
 
26 
 
References 
 
1. CDC: National Healthcare Safety Network. Pneumonia (Ventilator-Associated [VAP] and Non-Ventilator-
Associated Pneumonia [PNEU]) Event.; 2021. 
2. Ranieri VM, Rubenfeld GD, Thompson BT, et al. Acute respiratory distress syndrome: The Berlin definition. 
JAMA. 2012;307(23):2526-2533. doi:10.1001/jama.2012.5669 
3. CDC: National Healthcare Safety Network. Surgical Site Infection Event (SSI).; 2021. 
4. Cook D, Lauzier F, Rocha MG, Sayles MJ, Finfer S. Serious adverse events in academic critical care research. 
CMAJ. 2008;178(9):1181-1184. doi:10.1503/cmaj.071366 
5. Dufouil C, Brayne C, Clayton D. Analysis of longitudinal studies with death and drop-out: A case study. Stat 
Med. 2004;23(14):2215-2226. doi:10.1002/sim.1821 
  
 
 ```

### Administrative support: explicit not-applicable records

DOC-004 pages1,2,3 were each opened completely: collaborator names, institutions, qualifications, contributions and form-version/page-count metadata; no result-relevant quantitative or inferential support. DOC-005 page1 was opened completely: deidentified participant data/data dictionary on reasonable request, after six/12-month studies, beginning03-Jan-2026, no enddate, allpost-hoc analyses, no supportingdocuments; no trial quantitative/inferential result. No coverage gaps. Derivative limitations: unknown historical engine versions; native text omits plan figures, closed by fresh visual extraction; plotted values without printed labels are approximate readings explicitly identified above.
