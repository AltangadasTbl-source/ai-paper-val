# Numeric relationship inventory: DOC-004 / DOC-005

All relationship IDs below are newly assigned within this shard. Values are direct-source transcriptions; `Potential` is only a check-routing note, not an adjudication or candidate ID. No workbook exists, hence no formula/cached-value distinction applies.

| ID | Source location | Population/time/contrast; measure and units | Printed values / rule | Main-paper key | Potential |
|---|---|---|---|---|---|
| N3001 | DOC-004 p.2-4 | Trial schedule/intervention | 24-h pre-randomization pause; visits baseline, 6m,12m; resting HR target <=100 bpm; combination therapy if persistent HR >100 bpm | ASSESSMENT_SCHEDULE; HR_TARGET | None |
| N3002 | p.4 | Treatment dose / titration | Digoxin 62.5-250 mcg/day, default 125; day-1 loading twice dose. Bisoprolol 1.25-15 mg/day, default 2.5. Visits: 1.4 (SD .6; 1-3) vs 1.5 (.9; 1-6) | TREATMENT_DOSE | None |
| N3003 | p.5 | QoL definitions | SF36/PCS/MCS 0-100, higher better; normalized mean 50 UK; MCID .5 SD / 4.1-9.2. EQ-5D VAS 0-100; index 0-1; MCID .18. AFEQT 0-100; 5-point important change | QOL_SCALE_DEFINITIONS | Label/scale cross-check |
| N3004 | p.6 | Echo definitions | 3 index beats averaged; RR difference <60 ms; diastolic rule E/e′ >=15, or if <15, >=2 of IVRT <=65 ms, E decel <=120 ms, E/e′ >=11, PV decel <=220 ms | ECHO_DEFINITION | None |
| N3005 | p.8 | Eligibility | age >=60; NYHA >=II; exclude HR <60 bpm, MI <6m, decomp HF <14d, major surgery <3m | ELIGIBILITY | None |
| N3006 | p.9 | End uptitration; digoxin vs beta-blocker | 24-h HR 79 +/-11 vs 74 +/-11 beats/min | HR_24H_UPTITRATION | Cross-source / statistic check |
| N3007 | p.12 | NYHA denominators | Digoxin n=80/76/73 and beta-blocker n=80/74/72 at baseline/6m/12m; no baseline class I | NYHA_COUNTS | Denominator check |
| N3008 | p.13 | Digoxin medication, 6m/12m | attended 76/73; digoxin 73 (96.1%)/70 (95.9%); dose 160.5 (55.4)/158 (57) mcg; range 62.5-250 both; level .78 (.31)/.72 (.27) mcg/L; diltiazem 3 (3.9%)/5 (6.8%) | MEDICATION_DIGOXIN | Percentage check |
| N3009 | p.13 | Beta-blocker medication, 6m/12m | attended 74/72; bisoprolol 59 (79.7%)/58 (80.6%); dose 3.2 (1.8)/3.3 (2.1) mg; range 1-10 both; any beta blocker 66 (89.2%)/65 (90.3%); nebivolol 7 (9.5%)/7 (9.7%); diltiazem 1 (1.4%)/1 (1.4%) | MEDICATION_BETABLOCKER | Percentage/subset check |
| N3010 | p.14 | Resting 12-lead HR | baseline 100.3 (16.8),99.2 (19.2) n=80,80; 6m 76.9 (12.1),74.8 (11.6) n=76,74; 12m 75.4 (9.9),74.3 (11.2) n=73,72 | HR_12LEAD | Cross-source check |
| N3011 | p.14 | Resting apex HR | baseline 98.3 (15.1),99.0 (16.8); 6m 78.4 (10.5),76.2 (11.1); 12m 78.3 (9.2),76.2 (10.6) | HR_APEX | None |
| N3012 | p.14 | Resting radial HR | baseline 87.8 (12.0),86.9 (10.3); 6m 76.2 (9.7),73.9 (10.8); 12m 76.0 (9.0),73.8 (10.0) | HR_RADIAL | None |
| N3013 | p.14 | Peripheral pulse deficit | baseline -10.3 (9.4),-12.1 (12.0); 6m -2.3 (3.9),-2.3 (4.2); 12m -2.3 (5.1),-2.3 (3.2) | HR_PULSE_DEFICIT | Direction / definition |
| N3014 | p.14 | Post-walk radial HR | baseline 99.9 (19.6),103.7 (20.2), n=80,79; 6m 90.5 (19.1),89.8 (18.2), n=74,73; 12m 90.1 (15.9),87.3 (15.2), n=71,69 | HR_POSTWALK | Denominator / cross-source |
| N3015 | p.14 | Post-walk minus resting radial HR | baseline 12.1 (17.8),16.8 (20.7); 6m 14.3 (19.6),15.8 (16.4); 12m 13.9 (13.8),13.7 (15.4) | HR_EXERTION_DELTA | Arithmetic / definition |
| N3016 | p.15 | SF36 PCS normalized (mean 50) | baseline 28.9 (11.6),27.2 (10.2); 6m 31.9 (11.7),29.7 (11.4); 12m 32.5 (13.0),29.4 (12.4) | SF36_PCS | Cross-source |
| N3017 | p.15 | SF36 MCS | baseline 50.4 (10.2),49.5 (10.0); 6m 51.1 (10.6),50.0 (10.4); 12m 53.6 (8.9),51.3 (10.1) | SF36_MCS | None |
| N3018 | p.15 | SF36 physical functioning | 26.8 (12.6),25.9 (12.2); 29.2 (13.7),27.7 (13.6); 31.5 (14.1),27.5 (13.0) | SF36_PF | Cross-source |
| N3019 | p.15 | SF36 role physical | 31.8 (12.6),29.6 (12.1); 34.2 (12.0),31.3 (12.8); 37.0 (12.6),32.0 (12.4) | SF36_RP | Cross-source |
| N3020 | p.15 | SF36 bodily pain | 39.1 (12.2),37.5 (10.9); 42.0 (12.1),41.0 (11.6); 40.5 (12.7),41.9 (12.5) | SF36_BP | None |
| N3021 | p.15 | SF36 global health | 40.5 (9.4),39.0 (9.4); 41.6 (9.6),40.0 (9.8); 42.8 (9.9),39.6 (10.0) | SF36_GH | Cross-source |
| N3022 | p.15 | SF36 vitality | 43.4 (9.6),40.3 (10.0); 44.9 (10.4),43.0 (10.0); 47.1 (9.9),42.0 (10.0) | SF36_VT | Cross-source |
| N3023 | p.15 | SF36 social function | 42.8 (12.3),41.3 (12.0); 46.1 (11.5),43.5 (12.5); 45.6 (12.3),43.3 (11.6) | SF36_SF | None |
| N3024 | p.15 | SF36 role emotional | 40.2 (14.3),39.8 (15.0); 42.0 (13.3),38.7 (14.9); 45.2 (12.9),40.7 (15.5) | SF36_RE | None |
| N3025 | p.15 | SF36 mental health | 48.0 (11.6),48.2 (9.5); 48.2 (10.7),49.4 (11.2); 51.3 (9.3),51.8 (9.5) | SF36_MH | None |
| N3026 | p.15 | EQ-5D index | .67 (.19),.63 (.22); .66 (.27),.65 (.23); .66 (.27),.62 (.29) | EQ5D_INDEX | Scale check |
| N3027 | p.15 | EQ-5D VAS | 64.0 (16.6),61.6 (20.3); 71.8 (16.3),68.5 (17.1); 72.2 (17.0),66.2 (17.9) | EQ5D_VAS | Cross-source |
| N3028 | p.16 | AFEQT overall | 62.2 (16.7),57.2 (17.6); 72.1 (17.9),65.6 (16.8); 75.6 (17.1),68.1 (16.1) | AFEQT_OVERALL | Cross-source |
| N3029 | p.16 | AFEQT symptoms, post-hoc | 82.3 (18.3),76.0 (23.7); 87.2 (14.1),83.2 (16.4); 89.8 (15.5),86.2 (16.2) | AFEQT_SYMPTOMS | Post-hoc label |
| N3030 | p.16 | AFEQT daily activities, post-hoc | 44.2 (22.4),39.3 (22.4); 58.9 (26.0),47.9 (24.0); 62.0 (25.1),48.2 (24.4) | AFEQT_DAILY | Post-hoc label |
| N3031 | p.16 | AFEQT treatment concern, post-hoc | 72.8 (21.3),68.4 (21.4); 79.6 (19.4),77.4 (16.3); 84.3 (17.2),82.5 (14.8) | AFEQT_CONCERN | Post-hoc label |
| N3032 | p.16 | AFEQT treatment satisfaction, post-hoc | 55.1 (20.2),55.3 (21.2); 79.8 (15.0),73.3 (19.0); 84.1 (14.0),75.2 (18.8) | AFEQT_SATISFACTION | Post-hoc label |
| N3033 | p.17 | Adverse event event counts | Events digoxin/beta/total: 29/142/171; each row’s exact patient/event counts are in extraction artifact | ADVERSE_EVENT_TOTAL | Sum check |
| N3034 | p.17 | >=1 adverse event | 20/80 (25%), 51/80 (64%), total 71/160 (44%) | ADVERSE_EVENT_ANY | Percentage / total check |
| N3035 | p.18 | Historical SF36 studies | N 716,665,200,155,102,30; contextual changes 4.8,4,8.9,3.8,12 | CONTEXT_SF36_LITERATURE | Not trial outcome |

### Numeric relation checks performed

- eTable 1 percentages reconcile to the printed attendance denominators to one decimal percent (including 73/76=96.1%, 70/73=95.9%, 59/74=79.7%, 58/72=80.6%, 66/74=89.2%, 65/72=90.3%).
- eTable 5 category totals reconcile as patient totals within rows (e.g., dizziness 4+24=28; total events 29+142=171; any event 20+51=71). Its percentages use randomized-arm denominators of 80, not attendance counts; they round as printed. A patient can have multiple events, so event count need not equal patient count.
- DOC-005 p.1 is explicitly no-applicable for quantitative result mapping.

