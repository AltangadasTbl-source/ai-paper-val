# Support Quantitative Evidence Map — DOC-002 to DOC-004

## Scope, method, and page completion

- **DOC-002:** `joi250068supp1_prod_1760999665.28862.pdf`, PDF pp. 1-26. All pages were freshly directly inspected. Its native text layer was garbled; pages were rendered at 200 dpi for visual inspection. CPU Tesseract was attempted but produced empty output, so visual direct-source reading was retained as the authority. No result values are reported in this protocol; it supplies planned definitions and sample-size assumptions.
- **DOC-003:** `joi250068supp2_prod_1760999665.29862.pdf`, PDF pp. 1-24. All pages freshly directly extracted with `pdftotext -layout`; native text was usable.
- **DOC-004:** `joi250068supp3_prod_1760999665.30362.pdf`, PDF pp. 1 and 4-11 mapped using the listed usable source-linked native page text; pp. 2-3 freshly directly extracted. Direct PDF was used for exact reading where a definition or display mattered.

All 61 assigned pages were mapped. “No result display” below means the page was reviewed and contains administrative/method/reference content rather than a result-relevant quantitative display; it does not mean it was skipped.

| Source | Mapped pages with no result display / role |
|---|---|
| DOC-002 | pp. 1-2 cover/contents; pp. 3-19 protocol design, eligibility, procedures, administration, and outcome definitions; pp. 23-26 data-management/ethics/references. Quantitative planning tables on pp. 20-22 are mapped below. |
| DOC-003 | pp. 1-4 cover, contents, roles; pp. 5-6 background/eligibility; pp. 10-12 data schedule/reporting; pp. 23-24 software/references/scoring appendix. Definitions and all quantitative/statistical plans on pp. 7-9 and 13-22 are mapped below. |
| DOC-004 | p. 1 contents; p. 3 eMethods references. p. 2 supplies the patch/AF definition and reporting rules. pp. 4-11 are mapped below. |

## Protocol planning quantities (DOC-002)

| Provisional ID | Exact location | Direct-source observation and relationship |
|---|---|---|
| UN001 | DOC-002 p.20, Table 1 | Placebo/control yearly AF diagnosis rate is 0.70% in years 1-5; cumulative diagnosis is 0.70%, 1.40%, 2.10%, 2.80%, 3.50%. Active-arm additional patch-found AF is 0.49%, 0.42%, 0.35%, 0.28%, 0.21% by years 1-5, based respectively on 70%, 60%, 50%, 40%, 30% of cases otherwise found in that year; cumulative active-arm AF diagnosis is 3.96%, 4.24%, 4.59%, 5.01%, 5.50%. |
| UN002 | DOC-002 p.20, Table 2 | Initial whole-trial sample-size table: at 2.5 years, control 1.75%, active 4.41%, alpha 0.05, 90% continuity-corrected total n=1914; rows for comparison times 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 give control/active expected proportions 0.70/3.96, 1.05/4.10, 1.40/4.24, 1.75/4.41, 2.10/4.59, 2.45/4.80, 2.80/5.01, 3.15/5.25, 3.50/5.50 and total n 1019, 1261, 1565, 1914, 2348, 2825, 3406, 4004, 4711. |
| UN003 | DOC-002 p.21, Table 3 | Updated whole-trial assumptions: patch detection 3.75% or interim 4.09%; at 2.5 years total active AF 4.41% (ratio 2.5; implied control 1.77%) or 4.82% (ratio 2.5; implied control 1.93%), and alternatives at ratio 2 or rate 4.41/4.82%. Required total n for 90% power ranges 1773-2939 at 2p<0.05 and 2454-4088 at 2p<0.01; associated calculated powers for total n=2500/4000/5000 are printed. |
| UN004 | DOC-002 p.22, Table 4 | Subgroup power planning: age <80 (64%; patch AF 2.78%; total active 3.27%; ratio 2.5; implied control 1.31%; n 2642/3658 for 90% power at 2p<.05/<.01); age >=80 (36%; 6.28%; 7.39%; 2.5; 2.95%; n 1135/1571); age <75 (25%; 2.52%; 2.96%; 2.5; 1.18%; n 2924/4048); age >=75 (75%; 4.62%; 5.44%; 2.5; 2.18%; n 1563/2164); males (54%; 4.94%; 5.82%; 2.5; 2.33%; n 1458/2018); females (46%; 3.09%; 3.64%; 2.5; 1.46%; n 2367/3276). |

## SAP definitions, planned estimands, and planning quantities (DOC-003)

| Provisional ID | Exact location | Direct-source observation and relationship |
|---|---|---|
| UN005 | DOC-003 pp.7-9 | Primary outcome: ITT presence of primary-care AF record from randomization through 2.5 years. Secondary: the same outcome by age (<80, >=80) and sex; and mean time with known AF within 5 years, from first post-randomization AF record to 5 years, death, or withdrawal, with no-AF participants contributing zero. |
| UN006 | DOC-003 p.9 | 1:1 allocation to a single 2-week Zio XT patch versus usual care, minimised by age (<75/>=75), sex, and residual CHA2DS2-VASc score (0-1, 2, 3-6). |
| UN007 | DOC-003 pp.12-14 | Primary-care follow-up ends at earliest death, withdrawal, GP-practice loss, or day 913/1826 (randomization day 0); national data end at earliest death, withdrawal, or day 913/1826. Pre-randomization AF does not count unless a later post-randomization record occurs. No censoring applies to the 2.5-year primary outcome; 5-year time-with-AF is right-censored at earliest death, withdrawal, or day 1826. |
| UN008 | DOC-003 pp.14-17 | Planned descriptive quantities: follow-up to day 913 and 1826; active-arm patch adherence (number/proportion, median wear time, analyzable-data proportion, activation delay); patch AF number/proportion, burden, longest duration (hours), maximum/minimum AF heart rate, first episode (days), other arrhythmias, and patch-report-to-primary-care-AF time. p.16 shell denominators are overall 5,040, patch 2,520, control 2,520. |
| UN009 | DOC-003 pp.19-20 | Exploratory anticoagulation exposure: post-randomization record count/proportion and median first-record months, and distinct calendar-month exposure mean, assessed to 30 and 60 months (or death/withdrawal). Excludes rivaroxaban 2.5 mg twice daily. Nonrandomized groups are: patch AF plus post-randomization primary-care AF; primary-care AF only; patch AF without primary-care AF. |
| UN010 | DOC-003 pp.21-22 | Power assumptions: initial n=2,500, later n=5,000; usual-care AF 0.7%/year, expected 1.75% over 2.5 years; screening AF 3.75% plus usual care, total active-arm 4.4%; expected ratio about 2.5. n=2,500 (1,250/arm) was planned for >90% power at two-sided p<.05. Expansion to 5,000 aimed for >90% power at 2p<.01 for 2.5-fold and 2-fold differences, and about 90% subgroup power at 2p<.05. |

## Results supplement: exact displayed results (DOC-004)

| Provisional ID | Exact location | Direct-source observation and relationship |
|---|---|---|
| UN011 | DOC-004 p.2 | Patch records up to 14 days. AF is >=30 seconds continuous AF-compatible tracing. Immediate GP alerts: AF, flutter, sustained VT/VF, pauses >6 s, complete/Mobitz II/high-grade AV block. Results letters report AF presence/absence, duration, rate, and burden. |
| UN012 | DOC-004 p.4 eTable 1 | Patch allocation n=2,520; wore/returned 2,126 (84.4%); activation median 10 days (IQR 6-18); wear median 13.9 d (13.2-14.0); analyzable median 13.5 d (12.6-13.9); suitable data 98.8% (95.8-99.6); wore >=10.5 d 1,960 (77.8%); wore <10.5 d 166 (6.6%); unworn returned 188 (7.5%); not returned 206 (8.2%). |
| UN013 | DOC-004 p.4 eTable 1 | Of 166 wearing <10.5 days: attachment 43 (25.9%), skin reaction 18 (10.8%), other 8 (4.8%), unknown 97 (58.4%); stated denominator is 166. |
| UN014 | DOC-004 pp.5-6 eTable 2 | Patch group n=2,520; ECG data 2,126 (84.4%), no ECG 394 (15.6%). Age groups: <75 683/577 (84.5%)/106 (15.5%); 75-<80 1032/876 (84.9%)/156 (15.1%); >=80 805/673 (83.6%)/132 (16.4%); mean (SD) 77.7 (5.9), 77.6 (5.9), 77.8 (6.1). Sex: male 1340/1137 (84.9%)/203 (15.1%); female 1180/989 (83.8%)/191 (16.2%). |
| UN015 | DOC-004 pp.5-6 eTable 2 | Race/ethnicity: Asian 27/20 (74.1%)/7 (25.9%); Black 2/2 (100.0%)/0; White 2045/1738 (85.0%)/307 (15.0%); Other 21/17 (81.0%)/4 (19.0%); missing 425/349 (82.1%)/76 (17.9%). BMI: <25 488/422 (86.5%)/66; 25-<30 751/639 (85.1%)/112; >=30 571/466 (81.6%)/105; missing 710/599 (84.4%)/111; mean (SD) 28.2 (5.2), 28.0 (5.0), 29.3 (6.1). |
| UN016 | DOC-004 p.5 eTable 2 | CHA2DS2-VASc: <3 33/31 (93.9%)/2; 3 685/596 (87.0%)/89; 4 983/846 (86.1%)/137; >=5 819/653 (79.7%)/166; median (IQR) 4 (3-5), 4 (3-5), 4 (4-5). Prior diagnoses (overall/ECG/no ECG): hypertension 2255/1908/347; diabetes 713/582/131; stroke/TIA 485/395/90; CKD >=3 438/366/72; thromboembolism 271/216/55; MI 269/226/43; heart failure 244/191/53; PAD 214/170/44. |
| UN017 | DOC-004 pp.5-6 eTable 2 | Medications (overall/ECG/no ECG): statin 1739/1462/277; RAAS inhibitor 1599/1341/258; PPI/H2 antagonist 1265/1065/200; calcium-channel blocker 1200/996/204; diuretic 713/593/120; aspirin/dipyridamole 705/585/120; beta-blocker 619/529/90; P2Y12 363/300/63; oral anticoagulation 174/137/37; DOAC 128/101/27; VKA 59/47/12. |
| UN018 | DOC-004 p.7 eTable 3 | Patch-detected AF 89: 3.53% of all 2,520 and 4.19% of 2,126 wearers; AF without flutter 74 (2.94%, 3.48%); AF with flutter 15 (0.60%, 0.71%). Urgent other findings: flutter without AF 13 (0.52%,0.61%); complete AV block 5 (0.20%,0.24%); high-grade AV block 10 (0.40%,0.47%); Mobitz II 8 (0.32%,0.38%); 2:1 second-degree AV block 1 (0.04%,0.05%); pauses >6 s 6 (0.24%,0.28%); sustained VT >30 s 2 (0.08%,0.09%). |
| UN019 | DOC-004 p.7 eTable 3 | Nonurgent findings: nonsustained VT <=30 s 676 (26.83%,31.80%); sustained SVT >30 s 134 (5.32%,6.30%); nonsustained SVT <=30 s 1772 (70.32%,83.35%). Denominators printed are randomized-to-patch n=2,520 and wore/returned n=2,126. |
| UN020 | DOC-004 p.8 eFigure 1 | Sensitivity result using primary- or secondary-care AF to 2.5 y: overall patch 251/2520 (9.96%) vs usual care 207/2520 (8.21%), absolute difference 1.75% (95% CI 0.16%-3.33%), ratio 1.21 (1.02-1.45), p=.03. Age <80: 142/1715 (8.28%) vs 110/1744 (6.31%), difference 1.97% (0.24%-3.71%), ratio 1.31 (1.03-1.67); age >=80: 109/805 (13.54%) vs 97/776 (12.50%), 1.04% (-2.28%-4.36%), 1.08 (0.84-1.40), heterogeneity p=.28. |
| UN021 | DOC-004 p.8 eFigure 1 | Sex sensitivity result: females patch 105/1180 (8.90%) vs 70/1180 (5.93%), difference 2.97% (0.86%-5.08%), ratio 1.50 (1.12-2.01); males 146/1340 (10.90%) vs 137/1340 (10.22%), 0.67% (-1.66%-3.00%), 1.07 (0.85-1.33), heterogeneity p=.07. Figure says 95% CIs are not adjusted for multiplicity. |
| UN022 | DOC-004 p.9 eFigure 2 | Distribution display limited to patch-detected AF: first episode day 1-14; burden 0-100%; longest episode 0-336 h; grouped longest episode proportions: [30 sec,6 min) 9%, [6 min,6 h) 29%, [6 h,24 h) 20%, >=24 h 42%; rate axes max 75-225 and min 0-150 beats/min. |
| UN023 | DOC-004 p.10 eFigure 3 | Kaplan-Meier restricted to patch-detected AF: risk set at months 0-6 is 89,34,18,10,8,7,6. Seven participants whose primary-care AF record predates urgent patch report are in risk set at day 0 and counted as immediate events. |
| UN024 | DOC-004 p.11 eFigure 4 | AF/AFL distribution: first episode day 1-14; burden 0-100%; longest duration 0-336 h; grouped duration [30 sec,6 min) 10%, [6 min,6 h) 26%, [6 h,24 h) 18%, >=24 h 46%; max-rate axis 75-225, min-rate axis 0-150 beats/min. |

## Direct-source mapping limitations

Protocol native text was unreliable and the local CPU OCR invocation yielded empty files; rendered protocol pages were inspected directly, with quantitative planning tables visually confirmed. Exact OCR transcription is therefore unavailable for narrative protocol pages, but there is no remaining unmapped source unit. Figure histogram bin counts beyond the explicitly printed percentages and axes are not printed and cannot truthfully be recovered from the raster display.
