# Numeric relationship inventory — Workflow 1.6.1

Runtime agent: /root/numeric_checker. Scope: all four supplied documents, 83 mapped physical PDF pages (DOC-001 REPORT 10; DOC-002 PLAN 55; DOC-003 REPORT 17; DOC-004 REPORT 1). All 39 numeric families N001–N028 and N101–N111 are retained. Subordinate row keys remain part of their parent family; they are not independently renumbered or sampled. Statistical evidence is cross-referenced by the mapper S IDs below. There is no numeric relationship on DOC-004 p1. Controls read completely: QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md. Current source/tooling inventories and both complete canonical maps were read. No earlier scientific conclusions were read.

Counts are exact integers. Each noninteger displayed input retains its half-unit rounding interval: two decimals ±0.005; one decimal ±0.05; whole percentages ±0.5 percentage points, clipped to allowable probability bounds. Arithmetic checks require interval intersection, rather than equality of rounded midpoints. A model-based estimate is not replaced by crude arithmetic; absent paired contributor definitions do not justify assuming identical samples.

## Complete family check register

| ID | Numeric rule or matching relationship checked | Statistical cross-reference | Numeric review record |
|---|---|---|---|
| N001 | 38−8=30; 1+7=8; randomized and treated 30 across abstract/flow/text | S001 | Complete; reconciles. |
| N002 | 30−3=27; 2+1=3; final analysis and completer totals | S001 | Complete; reconciles. |
| N003 | Age range/mean/SD; 22+8=30; abstract sex notation | S011–S012 | Complete; obvious percent-symbol observation excluded. |
| N004 | Completer 16+11=27; enrolled genotype counts against complete roster | S007, S056–S057, S111 | Complete; analysis counts reconcile; enrolled baseline difference peripheral. |
| N005 | Recruitment, last visit and follow-up dates/windows | None | Complete; administrative comparisons peripheral. |
| N006 | 200×3=600 mg/day; 4+1+4+2=11 weeks/set; 1–4 sets and 4–16 visits | S001–S002 | Complete; reconciles. |
| N007 | 14-day baseline/last-two-week windows; IVR bounds/direction; all zero scores | S015–S018, S055–S060, S107–S109 | Complete; absence-of-symptom zero resolves wording. |
| N008 | Four-week periods versus 11-week sets; visits and other measurement timing | S004–S005 | Complete; period/set wording resolves immediately. |
| N009 | 24+3=27; 24/27=88.889%; 3/27=11.111%; follow-up responders | S002, S107 | Complete; percentages reconcile; patient 11 exception disclosed. |
| N010 | Probability thresholds and 1–4 sets, with 80%-displayed responders | S002, S106–S107 | Complete; boundary display precision and advisory decisions resolve. |
| N011 | 23+4=27; 23+2×4=31; two-set IDs1/2/4/5 | S025–S051, S107 | Complete; reconciles. |
| N012 | 773/868=89.055%; 2676/2728=98.094%; 31×28=868 | S004–S006 | Complete; reconciles, no reconstruction of unprinted measurement allocations. |
| N013 | Bayesian arm score scales/ordering; 5.56−2.50=3.06; baseline and model populations | S007 | Complete; reconciles. |
| N014 | Table1 n16/11; baseline definitions; every row retained below | S011–S024 | Complete; percentages and ranges checked. S0145/11 versus46% is outside nearest-whole precision but its explicit baseline count/denominator resolve extraction; CONTEXT_RESOLVES. |
| N015 | Consecutive-patient count, analysis-series x-axis and primary probability claim | S054 | Complete; graphical probabilities not exact arithmetic inputs. |
| N016 | INQoL 0–100 versus all printed baseline summaries and treatment units | S022, S063 | Complete; F-NUM-001. |
| N017 | SF-36 0–100; every component distribution/change sign and unit | S023–S024, S061–S062 | Complete; bounds reconcile; paired effect not inferred from marginal means. |
| N018 | Five attempts; seconds; first/fifth/mean clinical tests and 3-meter walking | S019–S021, S064–S074 | Complete; no ratio/effect-unit identity conflict survives context. |
| N019 | Force0–600 N; paresis0–100%; five 3-second attempts; duration units | S075–S087 | Complete; bounds checked; paired samples and interaction model distinguished. |
| N020 | EMG grade0–3, ten insertions×30seconds; no baseline | S088 | Complete; reported means/SD feasible. |
| N021 | .75/3.85=19.481%; .75/1.75=.4286; 2/3.85=51.948%; 2/1.75=1.1429 | S053 | Complete; clinical approximate 20% translation excluded. |
| N022 | 21/30=70%; 1/30=3.333%; matching main/supplement counts | None | Complete; reconciles. |
| N023 | No observed cardiac abnormality claim versus safety stopping rule | S104 | Complete; unprinted numeric percentage not invented. |
| N024 | Serum mean/SD and reference range in μg/mL; dose reference in mg/day | None | Complete; different units explicitly defined. |
| N025 | Two subtherapeutic patients4/13; .11/.27 below .5; undetectable washout | None | Complete; reconciles. |
| N026 | 94% adherence and two patients below75%; percentage contributor definition | None | Complete; missing denominator prevents mechanical reconstruction. |
| N027 | 26/31=83.871% treatment-set preferences; later patient wording | None | Complete; immediate source supplies set denominator. |
| N028 | 24 responders through18–31months; matching follow-up and response totals | S007, S010 | Complete; reconciles. |
| N101 | Adult eligibility≥18; QT500/QRS150; medication washouts5/3/2days | None | Complete; no observed denominator inconsistency. |
| N102 | Prospective titration200/400/600 mg/day, 11–44weeks, 1–4sets | S101 | Complete; arithmetic reconciles. |
| N103 | Primary weeks3/4/8/9 repeated at11-week offsets; symptom scales | S101–S102 | Complete; windows reconcile. |
| N104 | All schedule period starts/ends, evaluation and washout cells, 4–16visits | None | Complete; no omitted schedule group. |
| N105 | Three/five contractions; seconds, N, %, bounded grading | None | Complete; definitions retained, design comparisons cross-source lane. |
| N106 | Seven+eight=15days reporting; DSMB three; 10% of30=3 | S103–S104 | Complete; decision count arithmetic reconciles. |
| N107 | Planned30=20+10; chloride15/sodium15; center/cohort allocations | S102 | Complete; center/cohort administrative differences peripheral. |
| N108 | Every patient1–30: age, sex, gene, four baseline IVR values, family membership | S011–S018 | Complete; 22men/8women;18CLCN1/12SCN4A; remove3/6/7→16CLCN1/11SCN4A. |
| N109 | Every analyzed patient tuple, interim and post-trial decisions; roster27, continued24, stopped3 | S107, S025–S051 | Complete; all27 row keys retained, total31sets, exception11 disclosed. |
| N110 | Every12reaction/category rows in both arms; count/percentage bounds, overlaps and serious-event identity | None | Complete; count6%-display observation excluded; union reconstruction conditional. |
| N111 | Both6-column×8-summary-row simulations; valid1000/missing0; both decision frequency tables | S003, S102 | Complete; 315+685=1000;685/1000=68.5%;1.29−1.75=−.46;4.65−4.58=.07;4.67−3.38=1.29. |

## Printed main numeric inputs


All observations here belong to REPORT DOC-001. Page numbers in this table identify physical PDF pages and the named paragraph, figure or table.

| ID | Exact location | Printed quantities, population, timing and matching occurrence |
|---|---|---|
| N001 | p1 abstract Design/Results; p4 Figure 1 and Recruitment | 38 screened/assessed/contacted and recruited; 8 excluded: 1 did not meet inclusion criteria (ongoing cardiac and psychiatric disease), 7 declined (pregnancy or visit schedule examples). 30 enrolled/randomized and received study medication. |
| N002 | p1 abstract Results; p4 Figure 1 and Recruitment/Numbers Analyzed | 3 did not complete: 2 lost to follow-up/nonadherent/did not complete visits, 1 discontinued for serious adverse event. 27 completed as planned and 27 N-of-1 trials included in analysis. |
| N003 | p1 abstract Results; p4 Baseline Data | Enrolled n=30: age mean 43.4, SD 15.24 years (p4 range 19–65); abstract prints “22% men”; p4 prints “Twenty-two men and 8 women.” Exact source representations preserved. |
| N004 | p1 abstract Results; p4 Baseline Data; p5 Table 1; p8 Table 2 footnote a | Enrolled: 19 CLCN1 and 11 SCN4A. Table 1/completer and Table 2 analysis: n=16 CLCN1, n=11 SCN4A, total 27. CLCN1 is skeletal muscle chloride channel gene; SCN4A skeletal muscle sodium channel gene. p4 primary results prints subgroup gene as “CLNC1” alongside n=16. |
| N005 | p1 Design; p4 Recruitment; p8 Follow-up | Abstract enrollment February 2014–June 2015, follow-up completed September 2016. Detailed recruitment January 6, 2014–February 2, 2015; first enrollment February 21, 2014; last study visit June 10, 2015. Follow-up completed September 10, 2016, range 18–31 months. |
| N006 | p1 Interventions; p2 Clinical Trial Design/Randomization/Procedures | Double-blind randomized placebo-controlled single-center adult genetically confirmed NDM N-of-1 trials. Mexiletine hydrochloride 200 mg capsules three times daily (=printed 600 mg daily p1) versus placebo. Each participant has 1–4 treatment sets, each 11 weeks: 4-week mexiletine + 4-week placebo, block randomized, 1-week washout between, 2 weeks interim analysis at end. Antimyotonic treatment recipients have 2-week washout before baseline. 4–16 study visits depending on required sets. |
| N007 | p2 Outcomes; p3 Outcomes; p1 Main Outcomes; p5 Table 1 footnote b; p8 Table 2 footnote e | IVR automated telephone diary asks symptoms during previous 24 hours and ordinal severity 1–9, 9 worst ever; primary mean daily stiffness, secondary daily pain/weakness/tiredness. Higher scores indicate greater impairment. Table 1 baseline is 2 weeks pretrial; Table 2 baseline daily calls over 14 days; frequentist treatment-period means use last 2 weeks of each treatment period. |
| N008 | p3 Outcomes | Non-IVR secondary outcomes assessed beginning and end of each “4-week treatment set” as printed; myotonic discharge grading assessed only end. Preference for one of two periods recorded after each set. Random serum mexiletine levels analyzed at end of trial. |
| N009 | p1 Results; p4 Primary Outcome | 24/27 (89%) completers had predefined clinically meaningful individual effect and stopped trial to continue regular mexiletine; 3/27 (11%) had predefined clinical ineffectiveness, stopped trial and discontinued mexiletine. All three nonresponders SCN4A. |
| N010 | p2 Procedures; p3 Bayesian Analysis | Stopping based on posterior probability that clinical difference exceeds 0.75: >0.80 (>80%) discontinue trial/start treatment; <20% discontinue trial/no regular treatment; otherwise continue N-of-1 trial. Maximum 1–4 sets noted p2. |
| N011 | p4 Figure 1/Numbers Analyzed; p5 Figure 2 caption | 23 participants completed one set; four completed two sets; 31 sets from 27 patients analyzed. Figure 2 identifies two-set patients 1,2,4,5 and dropout patients 3,6,7. |
| N012 | p4 Numbers Analyzed | Primary telephone calls 773/868 completed (89%); secondary in-person possible outcome measures 2676/2728 collected (98%). Missing data described as relatively small and assumed missing at random; multiple imputation not performed. |
| N013 | p1 Results; p4 Primary Outcome | Overall baseline muscle stiffness median 6.08, IQR 4.71–6.80; during mexiletine 2.50, 95% CrI 1.77–3.24; placebo 5.56, 95% CrI 4.73–6.39. Abstract grammatical presentation follows baseline “median”; p4 repeats exact quantities. Contrast and Bayesian effect in S007. |
| N014 | p5 Table 1 header and footnotes; p8 Table 2 footnotes a–b | Baseline subgroup n=16 and 11. Table 1 bedside/Timed Up&Go rows represent median/IQR across patients, each patient contributing median on five trials. Table 2 baseline for non-IVR measures is visit 1, start of first treatment period; no EMG baseline available. |
| N015 | p4 Primary Outcome; p6 Figure 3C caption; p9 Discussion | Meaningful reduction claim with >95% probability after first 11 consecutive patients (p4); Figure 3 caption says 95% or greater, patients 1–11 as labeled elsewhere; x-axis Figure 3 does not match Figure 2 ordering. Discussion repeats first 11 consecutive patients. |
| N016 | p3 Outcomes; p5 Table 1 footnote f; p8 Table 2 footnote g | INQoL composite 0–100, higher worse. All its baseline quartiles, means and treatment changes preserved in S022 and S063, including values outside this stated scale. No normalization performed. |
| N017 | p3 Outcomes; p5 Table 1 footnote g; p8 Table 2 footnote f | SF-36 Dutch physical and mental components each 0–100, lower worse. Both distribution and treatment change rows preserved in S023–S024 and S061–S062. |
| N018 | p3 Outcomes; p5 Table 1 footnotes c–e; p8 Table 2 footnotes h–i | Handgrip/eyelid action myotonia relaxation after forceful contraction for 5 seconds; first, fifth, mean of five attempts; seconds, higher worse. Timed Up&Go: rise, walk 3 meters, turn, return, sit at self-selected speed; seconds, higher worse. |
| N019 | p3 Outcomes; p8 Table 2 footnotes j–l | Handgrip dynamometry MVIC: five trials of 3-second maximum voluntary isometric contractions. Relaxation duration from 90% to 5%, seconds, higher worse; peak force 0–600 N, lower worse; transient paresis maximal percentage decline from peak during 3-second MVIC, 0–100%, higher worse. |
| N020 | p3 Outcomes; p8 Table 2 EMG row and footnote m | Myotonic discharge concentric needle EMG left rectus femoris at rest: ten insertions, 30 seconds evaluation each; grading 0–3, 0 no discharges, 3 discharges at every insertion, higher worse. No baseline row value. |
| N021 | p3 Bayesian Analysis; p6 Figure 3 caption | Expert consensus (three clinical experts) meaningful difference 0.75 for all four IVR outcomes; corresponds to 20% change and standardized effect 0.43 using historical untreated mean 3.85, SD 1.75. Figure 3B additionally defines 2.0-point threshold =52% change/effect size 1.14. These baseline reference numbers are historical inputs, not current trial baseline. |
| N022 | p1 Results; p8 Adverse Events; p9 Discussion | Gastrointestinal discomfort mexiletine 21 patients (70%); p8 explicitly 21/30. Abstract placebo 1 (3%). One serious allergic skin reaction/reversible urticaria-like rash mexiletine (3%), excluded from trial. p9 repeats GI frequency 70%. |
| N023 | p8 Adverse Events | No clinically relevant ECG rhythm abnormalities or cardiac conduction interval changes observed during trial. Exact numeric event count not printed; do not substitute a derived percentage. |
| N024 | p8 Drug Levels | End-mexiletine serum level mean 1.06, SD 0.51 μg/mL. Antiarrhythmic therapeutic reference dose 600–1200 mg/day, serum reference 0.5–2.0 μg/mL. |
| N025 | p8 Drug Levels | Two patients, IDs 4 and 13, subtherapeutic serum levels 0.11 and 0.27 μg/mL respectively. Levels undetectable at start of periods and end of placebo periods, described as adequate washout. |
| N026 | p8 Adherence | Mean drug adherence 94%; only two patients (IDs 1 and 23) below 75%. Denominator of adherence percentage not separately specified in this paragraph. |
| N027 | p8 Adherence and Blinding; p9 Limitations | Mexiletine preferred over placebo in 26/31 treatment sets (84%). p9 calls this high percentage of patients preferring mexiletine (84%); exact phrasing preserved. |
| N028 | p8 Follow-up; p9 Discussion/Conclusions | All 24 responders continued mexiletine through follow-up, no adverse events occasioning discontinuation; 18–31 months through September 10, 2016. Discussion states stiffness/weakness/tiredness reduced, most objective/QOL effects medium-to-large, pain meaningful-effect probability below 50%; conclusion stiffness reduction consistent with previous RCT and efficacy/feasibility supported. |

## Main table subordinate row keys and inputs

Every Table 1 row S011–S024 and every Table 2 outcome row S055–S088 is checked as numeric evidence for the parent definitions above. Interaction rows S089–S092 retain their statistical cross-reference. The complete cells below preserve the mapper's source transcription, not a new finding selection.

## Table 1 — all baseline rows

Exact source: p5 Table 1, header CLCN1 N=16 versus SCN4A N=11. P values footnote a: nonparametric Mann–Whitney U genotype comparison. All rows retain printed measurement summaries, including age mean/range and count/percentage rows. Footnotes b–g in N007, N014 and N016–N018.

| ID | Characteristic/unit/summary | CLCN1 | SCN4A | P |
|---|---|---|---|---|
| S011 | Age years, mean (range) | 50 (24–65) | 38 (19–64) | .09 |
| S012 | Men count (%) | 13 (81) | 7 (64) | .39 |
| S013 | Pretrial mexiletine count (%) | 2 (13) | 0 | .50 |
| S014 | Pretrial other antimyotonic count (%) | 7 (44) | 5 (46) | .62 |
| S015 | IVR stiffness median (IQR) | 6.7 (6.0–7.0) | 4.7 (3.3–5.1) | .002 |
| S016 | IVR pain median (IQR) | 0 (0–1.1) | 3.4 (2.3–5.5) | .002 |
| S017 | IVR weakness median (IQR) | 3.8 (1.1–5.0) | .5 (0–6.1) | .06 |
| S018 | IVR tiredness median (IQR) | 3.4 (1.4–6.0) | 5.1 (3.9–6.1) | .16 |
| S019 | Handgrip action myotonia seconds, median (IQR) | 1.1 (.9–2.0) | 1.5 (1.0–6.4) | .40 |
| S020 | Eyelid closure action myotonia seconds, median (IQR) | 1.2 (.6–2.9) | 4.0 (1.3–11.2) | .01 |
| S021 | Timed Up&Go seconds, median (IQR) | 9.7 (8.8–11.0) | 9.5 (8.3–10.3) | .49 |
| S022 | INQoL composite median (IQR) | 84.0 (74.5–110.3) | 98.0 (56.0–120.0) | .82 |
| S023 | SF-36 physical median (IQR) | 40.8 (37.7–46.6) | 38.7 (33.6–40.0) | .11 |
| S024 | SF-36 mental median (IQR) | 52.1 (44.7–57.1) | 55.0 (37.2–59.1) | .88 |

p4 Baseline Data matching narrative: stiffness higher CLCN1, pain higher SCN4A, eyelid closure action myotonia higher SCN4A, differences at baseline.

## Table 2 — all outcome rows, effects, intervals and P values

Exact source p7 Table 2, continued p8. Heading: total NDM disease group N=27, frequentist (non-Bayesian) statistics. For genotype rows, n16/n11 from footnote a. Each cell is reproduced in source order; parenthetical baseline/period values in first block are SD; treatment parentheses are 95% CI. In second block baseline parentheses are SD and placebo/mexiletine change parentheses are 95% CI. Second-block heading literally states “Treatment Effect (Placebo-Mexiletine), Mean (95% CI)”. These printed signs and labels are preserved. Footnote d says all statistically significant findings favored mexiletine. Model/test definitions S004–S006; each subgroup row shown following a significant interaction per footnote c. No crude substitution for model-based results.

| ID | IVR outcome/group | Baseline mean (SD) | Placebo mean (SD) | Mexiletine mean (SD) | Treatment mean (95% CI) | P |
|---|---|---|---|---|---|---|
| S055 | Stiffness overall, primary | 5.65 (1.78) | 5.55 (2.09) | 2.42 (1.81) | 3.12 (2.46 to 3.78) | <.001 |
| S056 | Stiffness CLCN1 | 6.45 (1.71) | 6.46 (1.71) | 2.60 (1.50) | 3.82 (3.10 to 4.54) | <.001 |
| S057 | Stiffness SCN4A | 4.34 (2.02) | 4.22 (1.93) | 2.16 (2.24) | 1.89 (1.01 to 2.76) | .002 |
| S058 | Pain | 1.95 (2.09) | 2.08 (2.10) | 1.37 (2.13) | .70 (.18 to 1.23) | .01 |
| S059 | Weakness | 2.84 (2.54) | 2.96 (2.75) | 1.49 (1.66) | 1.56 (1.05 to 2.06) | <.001 |
| S060 | Tiredness | 4.28 (2.28) | 3.65 (2.51) | 2.41 (2.53) | 1.27 (.58 to 1.95) | .001 |

| ID | Secondary outcome/group, unit | Baseline mean (SD) | Change placebo mean (95% CI) | Change mexiletine mean (95% CI) | Treatment effect mean (95% CI), printed heading placebo–mexiletine | P |
|---|---|---|---|---|---|---|
| S061 | SF-36 physical, points | 38.26 (7.81) | 1.04 (−.60 to 2.96) | 8.66 (5.94 to 11.38) | 7.81 (4.72 to 10.88) | <.001 |
| S062 | SF-36 mental, points | 50.29 (9.67) | −1.85 (−4.81 to 1.11) | 4.77 (.67 to 8.48) | 6.78 (1.64 to 11.92) | .001 |
| S063 | INQoL composite, points | 96.89 (38.49) | −7.22 (−14.5 to −.29) | −21.44 (−30.90 to −11.95) | −14.22 (−24.71 to −3.74) | .01 |
| S064 | Handgrip action, first, seconds | 3.33 (5.00) | .46 (−.30 to −1.23) | −2.39 (−4.22 to −.55) | −2.85 (−5.28 to −.42) | .02 |
| S065 | Handgrip action, fifth, seconds | 1.36 (1.25) | .28 (−.43 to .99) | −.69 (−1.18 to −.19) | −.97 (−2.03 to .09) | .07 |
| S066 | Handgrip action fifth CLCN1, seconds | .93 (.41) | −.01 (−.21 to .18) | −.30 (−.42 to −.18) | .04 (−1.11 to 1.19) | .95 |
| S067 | Handgrip action fifth SCN4A, seconds | 2.59 (3.00) | .71 (−1.17 to 2.60) | −1.24 (−2.48 to −.02) | −1.96 (−3.41 to .51) | .009 |
| S068 | Handgrip action mean, seconds | 2.02 (2.33) | .29 (−.17 to .76) | −1.14 (−1.95 to −.34) | −1.44 (−2.66 to −.22) | .02 |
| S069 | Eyelid action first, seconds | 6.70 (7.38) | −.74 (−2.49 to 1.01) | −4.99 (−8.25 to −1.73) | −4.25 (−8.45 to −.05) | .05 |
| S070 | Eyelid action fifth, seconds | 2.24 (3.23) | −.44 (−1.24 to .36) | −1.39 (−2.57 to −.21) | −.95 (−2.25 to .35) | .14 |
| S071 | Eyelid action mean, seconds | 3.50 (4.15) | −.43 (−1.24 to .37) | −2.54 (−4.15 to −.93) | −2.11 (−3.94 to −.28) | .03 |
| S072 | Timed Up&Go first, seconds | 10.10 (2.38) | −.15 (−.99 to .68) | −1.41 (−1.96 to −.85) | −1.25 (−2.23 to −.28) | .01 |
| S073 | Timed Up&Go fifth, seconds | 8.91 (1.52) | .29 (−.45 to 1.03) | −.70 (−1.13 to −.27) | −1.00 (−2.01 to .03) | .06 |
| S074 | Timed Up&Go mean, seconds | 9.51 (1.77) | .07 (−.67 to .01) | −1.05 (−1.48 to −.62) | −1.12 (−2.07 to −.18) | .02 |
| S075 | Dynamometry relaxation first, seconds | .84 (1.81) | −.10 (−.87 to .67) | −.10 (−.22 to .01) | −.02 (−.86 to .82) | .96 |
| S076 | Dynamometry relaxation fifth, seconds | .31 (.23) | .00 (−.12 to .13) | −.02 (−.07 to .03) | −.01 (−.16 to .14) | .87 |
| S077 | Dynamometry relaxation mean, seconds | .48 (.70) | −.07 (−.33 to .19) | −.05 (−.10 to .00) | −.02 (−.28 to .25) | .91 |
| S078 | Dynamometry peak force first, N | 344.07 (173.56) | −7.81 (−39.39 to 23.77) | 18.92 (−6.53 to 44.37) | 32.92 (−5.10 to 70.94) | .09 |
| S079 | Dynamometry peak force fifth, N | 321.41 (150.51) | 6.15 (−14.99 to 27.30) | 27.96 (5.27 to 50.65) | 24.08 (−5.22 to 53.39) | .10 |
| S080 | Dynamometry peak force mean, N | 336.85 (157.85) | −3.85 (−25.84 to 18.14) | 29.90 (5.74 to 54.05) | 37.23 (10.19 to 64.28) | .009 |
| S081 | Transient paresis first, % | 29.19 (27.65) | .69 (−7.68 to 9.07) | −2.4 (−11.55 to 6.75) | −3.7 (−15.10 to 7.68) | .51 |
| S082 | Transient paresis fifth, % | 20.30 (18.75) | .73 (−3.63 to 5.09) | −8.56 (−17.26 to .14) | −12.25 (−22.04 to −2.47) | .02 |
| S083 | Transient paresis fifth CLCN1, % | 24.35 (23.11) | 4.31 (−1.32 to 9.94) | −18.75 (−28.59 to −8.91) | −23.85 (−32.45 to −15.24) | <.001 |
| S084 | Transient paresis fifth SCN4A, % | 9.12 (10.33) | −5.00 (−11.32 to 1.32) | 9.56 (1.24 to 17.87) | 13.71 (−1.96 to 25.47) | .02 |
| S085 | Transient paresis mean, % | 24.11 (20.13) | −.08 (−4.84 to 4.68) | −6.38 (−10.81 to −1.95) | −7.34 (−13.45 to −1.24) | .02 |
| S086 | Transient paresis mean CLCN1, % | 32.56 (22.35) | 1.53 (−5.70 to 8.75) | −11.26 (−16.83 to −5.69) | −12.37 (−18.35 to −6.38) | <.001 |
| S087 | Transient paresis mean SCN4A, % | 8.10 (7.40) | −2.64 (−8.50 to 3.22) | 2.31 (.10 to 4.52) | 4.46 (−3.85 to 12.76) | .28 |

The p8 continuation returns to period means/SD, rather than changes/CI:

| ID | Outcome/unit | Baseline | Placebo mean (SD) | Mexiletine mean (SD) | Treatment mean (95% CI) | P |
|---|---|---|---|---|---|---|
| S088 | Myotonic discharges needle EMG, grade | dash, unavailable | 2.52 (.89) | 1.85 (1.13) | .67 (.23 to 1.11) | <.001 |

| ID | Table 2 interaction row, p7 | Printed P | Matching narrative |
|---|---|---|---|
| S089 | IVR stiffness genotype×treatment | .004 | Subgroup primary reductions appear S056–S057; discussion p8 favors CLCN1 degree of response. |
| S090 | Fifth handgrip action myotonia genotype×treatment | .04 | p8 narrative favors SCN4A and repeats CLCN1 .04 (−1.11–1.19), SCN4A −1.96 (−3.41–.51), P=.04. |
| S091 | Fifth transient paresis genotype×treatment | <.001 | p6 narrative favors CLCN1; repeats −23.85 (−32.45–−15.24) versus 13.71 (−1.96–25.47), P<.001. |
| S092 | Mean-of-five transient paresis genotype×treatment | .002 | p6–8 narrative favors CLCN1; repeats −12.37 (−18.35–−6.38) versus 4.46 (−3.85–12.76), P=.002. |

p6 secondary narrative identifies total-group statistically significant objective/QOL results: SF-36 physical and mental, INQoL, mean handgrip/eyelid closure bedside tests, walking speed, handgrip peak force, and EMG discharge grade. p9 repeats most secondary measurements (including objective electrophysiological) showed significant effects aligned with primary and medium-to-large effects. Those claims match the named outcome rows for checking without selecting only significant results; all displayed nonsignificant rows are also fully retained above.

## Complete support numeric inputs and row keys

The following locators retain every planned numeric family and every baseline, individual-outcome, adverse-reaction and simulation row. S evidence included inside these sections is cross-referenced, not independently assigned numeric IDs.

## PLAN numeric and analysis relationships

### N101 — Population and eligibility

Source: [protocol p.18](../../../joi180136supp1_prod.pdf#page=18), continuation p.19; summary p.7. Adults at least 18 years, genetically confirmed nondystrophic myotonia; participation in the previous genetic-variability study or new genetically confirmed patient. Chloride channelopathies include Becker/Thomsen phenotypes; sodium channelopathies include PMC and SCM. Exclude consent inability/unwillingness; other neurologic conditions affecting measurements; genetically confirmed DM1 with CTG >50 repeats or DM2; malignant arrhythmia/conduction disturbances, second-/third-degree AV block, QT >500 ms or QRS >150 ms; listed cardiac antiarrhythmic medication; pregnancy/lactation; myotonia medication within washout windows; renal/hepatic disease, heart failure, myocardial infarction history or seizure disorders. Washout: phenytoin/flecainide at least 5 days; carbamazepine/mexiletine at least 3 days; propafenone/procainamide/disopyramide/quinidine/encainide at least 2 days (p.13; p.22 repeats as required 5/3/2 days).

REPORT counterpart [eTable 1 p.2](../../../joi180136supp2_prod.pdf#page=2), visually opened: inclusion only age ≥18 and genetically confirmed NDM; same eight exclusion categories. Printed DM1 parenthesis is “CTG > repeats” without a numeric threshold. Its caption expands CTG as cysteine-threonine-glycine (amino acids); reproduced from the published protocol, a citation only, not externally consulted. Printed first exclusion contains “inability or willingness” in the source; extraction records consent exclusion without interpreting that phrasing. QT/QRS thresholds 500/150 ms and medication windows 5/3/2 days retained. Main key: eligibility, age, genetic diagnosis, analysis-population selection.

### N102 — Intervention, washout and pharmacokinetics

Sources protocol pp.7,12–14,22,30. Each patient minimum 1, maximum 4 treatment sets, each set active/placebo 4 weeks each, randomized order, 1-week interperiod washout. Oral mexiletine day 1 200 mg once, day 2 200 mg twice, day 3 onward 200 mg three times daily; matching placebo titration. Steady dose 600 mg/day. Minimum/maximum participation 11/44 weeks, including evaluation periods. Follow-up 3 months after individual trial. Identical capsules prepared by pharmacy, storage 15–25 °C; compliance pill counting p.31. Half-life approximately 10–12 hours, sufficient serum concentration anticipated within 5 doses, maximum/stable serum by day 3. Co-medications affecting sodium channels prohibited during trial. Main key: randomized mexiletine regimen and duration, crossover design, adherence.

### N103 — Primary and secondary endpoint definitions

Sources protocol pp.7–8,13–14,31. Primary mean daily participant-assessed IVR stiffness, ordinal 1–9, using last two weeks of each treatment period: weeks 3,4,8,9,14,15,19,20,25,26,30,31,36,37,41,42. First two weeks weekly IVR, final two weeks daily; calls encouraged immediately after first morning dose. Daily symptom frequency in hours also collected for stiffness, pain, weakness, fatigue. Secondary: IVR pain, weakness, fatigue; clinical myotonia; quantitative handgrip myotonia; INQoL; adult SF-36; mexiletine plasma levels; biceps force; needle EMG; IVR measurements from remaining weeks and washouts. No “other” parameters. Main key: primary IVR stiffness score/time window, secondary symptom/QoL/physiology outcomes.

### N104 — Assessment schedule and study diagram

Protocol p.14 visual Figure 1: M weeks 1–4, washout 5, P 6–9, evaluation 10–11; P 12–15, washout 16, M 17–20, evaluation 21–22; M 23–26, washout 27, P 28–31, evaluation 32–33; P 34–37, washout 38, M 39–42, evaluation 43–44. Order is illustrative, not a replacement for randomized order. Table 1 pp.15–17: lab/pregnancy/consent/history at screening; ECG/needle EMG screening and end of every period (weeks 4,9,15,20,26,31,37,42). INQoL/SF-36, clinical myotonia, quantitative grip, biceps, plasma measurements at starts and ends of periods (weeks 1,4,6,9,12,15,17,20,23,26,28,31,34,37,39,42); drug dispensed at start, bottles collected at end. IVR weekly in first two weeks and daily in last two weeks, X* explicitly daily. Table contains empty evaluation/washout cells. Screening text p.13 says 1–4 weeks before start and assessment paragraph 1–2 weeks before baseline; ECG comparisons to week 0. Visits 4–16, approximately 2 hours each. Main key: primary observation window, crossover period length, number of visits.

### N105 — Physiologic measurement definitions

Protocol pp.32–34. Eye closure and hand closure held 3 seconds, relaxation timed in seconds, repeated 5 times. Percussion thenar/EDC, EDC site about 3 cm distal to lateral epicondyle and 1 cm medial. Grip MVIC 3 seconds then relax to baseline; warm-up series 5 contractions each 3 seconds with 10 seconds rest; initial versus fifth relaxation compared. Relaxation intervals 90%→10%, 90%→50%, 90%→75% MVIC; 3 sets separated by 10 minutes. Figure 2 p.33 photograph contains no additional numerical result. Biceps MVC measured 3 times, peak used; 60% MVC contractions at least 30 seconds, 10-minute rests; left arm horizontal, elbow 90° abduction, isometric force feedback. Rectus femoris needle EMG: discharges ≥500 ms in 3 areas outside endplate; grades 1+ minimal criteria, 2+ more than half locations, 3+ every needle movement in all areas. Main key: reported clinical/grip/EMG endpoint units and definitions.

### N106 — Safety, withdrawal and administrative rules

Protocol pp.35–39,47–50. Withdrawal anytime, urgent medical withdrawal, intercurrent event precluding visits/evaluation; exit interview within 7 days, adverse events followed until resolved/stable. SAE definitions: death/life-threatening/hospitalization/prolongation/disability/congenital anomaly/new safety event. Fatal/life-threatening preliminary SAE report ≤7 days plus 8 days completion; SUSAR ≤15 days, fatal ≤7 plus 8; line list half-yearly, safety annual. DSMB 3 independent members, review ECG/plasma/AE after each treatment set, cardiac event notification within 24 hours, meeting documentation within 5 days. Safety thresholds are S104. Pregnancy exclusion and immediate investigator notification; contraception if no sterilization or menopause ≥1 year. CRF retained 15 years; all substantial amendments notified, no actual amendment/version update supplied. Annual progress, end notification within 8 weeks of last patient's last visit, final report within 1 year. These administrative units were opened; administrative dates/contact details/insurance are not efficacy results. Main key: adverse-event denominator, early termination rules, intention-to-treat (S103).

### N107 — Planned recruitment and calendar counts

Protocol p.12: two ten-person cohorts followed in parallel, trials within 88 weeks. Protocol pp.44–45: estimated ≤15% ineligible; initial stratified contacts 15 chloride,10 PMC,10 SCM. Planned Nijmegen 20 =10 chloride +10 sodium (5 PMC +5 SCM); Maastricht 10 =5 chloride +2 PMC +3 SCM; total 30. Nijmegen first two parallel groups of 10 (5 chloride/5 sodium each), consecutively; Maastricht group 10 after Nijmegen completion, text. Figure 5 p.45: Nijmegen database 111, Maastricht 20; Nijmegen sampling figure lists 15 chloride,10 PMC,10 MC; inclusion branches 10 chloride,5 PCM,5 SCM; Maastricht 5 chloride,2 PCM,3 SCM. Preserve figure abbreviations as printed; clinical terms are not independently adjudicated. Figure 6 p.46: inclusion Jan/Feb 2011; first Nijmegen N=10 March 2011–Jan 2012; second Nijmegen N=10 and Maastricht N=10 Sept 2011–July 2012; analysis/publication Aug–Dec 2012. Main key: target sample 30, genotype strata, centers and enrollment (calendar values primarily administrative).

### S101 — Prospective objectives/design

Protocol pp.11–12,31: primary objective refine N-of-1 methodology and assess aggregated Bayesian evidence for rare-disease coverage decisions; clinical improvement in myotonia secondary objective. Double-blind randomized placebo-controlled individual crossover trials aggregated using Bayesian hierarchical modeling. Randomization generated by HTA programmer, allocation sent to pharmacy; code broken after all individual trials completed, exceptional individual unblinding for SAE as needed. Compare noninformative/informative-prior results for robustness and compare worldwide CINCH trial results. Main key: statistical design and primary clinical outcome reporting.

### S102 — Prospective sample-size simulation and its REPORT counterpart

Protocol pp.19–21: stiffness 9-point scale, historical placebo mean 4.62, clinically relevant difference 0.75 corresponding to effect size 0.34. Expected 10 daily measures per arm from last 2 weeks. 1000 repetitions: draw mean effect from elicited design prior; simulate 30 individual trials with 2×10×2 or 2×10×3 observations; random intercept/slope plus common within-person residual; analyze in R/R2WinBUGS using elicited N(1.75,0.89) analysis prior or vague N(1.75,10), retaining elicited design prior; calculate Ppost(β0>0.75), then mean over replicates. N notation is mean/SD per p.41. Simulation inputs placebo mean 4.62, intercept SD 2.19, slope SD 1.77, residual SD 0.827. Observations <1/>9 truncated to 1/9. Fixed subgroup/center effects ignored in simulation, explicitly distinguished from analysis model. 2/3 completed pairs anticipate missing data within flexible 1–4-pair design. Table heading “Expected Posterior Probability >0.75”: clinical prior 2/3 printed “treatment periods” 0.817/0.821; noninformative prior 0.782/0.784. Text calls them treatment pairs. Sufficient-evidence interim cutoff 0.8. No formula-based sample-size equation printed.

REPORT eMethods 4 pp.15–17 gives a separate operating-characteristic simulation with 14 observations per arm per pair, fixed true effect 0 or 1.75, variable baseline and variability per patient/treatment; individual continuation probability <20%, >80%, or 20–80% after each pair. Repeat to final patient stopping, then 30 trials aggregated; 1000 repeated groups. SAS 9.4; WinBUGS 1.4 run from R 3.1.3. Printed step 2 refers individual analysis to eMethods 2 and step 4 refers group meta-analysis to eMethods 3; retained as pointers only. Null type I error printed 0.00 and mean bias 0.07; alternative power 68.5%, mean effect 1.29, bias −0.46 =1.29−1.75. Complete simulation table values under N111. Main key: sample size/power/type I error/operating characteristics, priors, 30 participants, 0.75 threshold.

### S103 — Prospective analysis population/missingness

Protocol p.35: intent-to-treat; all data acquired before termination included in primary analysis unless consent withdrawn. Final visit attempted, clinical follow-up until AE resolution. No replacement/imputation formula is printed despite section heading replacement. Main key: primary analysis population and handling dropout/missing IVR.

### S104 — Safety stopping decisions

Protocol p.38: accumulated study-related serious AEs ≥10% (3 patients) or ≥2 same cardiac AEs/SAEs trigger DSMB convening and review for continue/stop. Figure 3 p.39: conduction abnormality second/third AV block, QT >500 ms, QRS >150 ms or other serious ECG abnormality → stop individual trial; serum mexiletine >2 µg/mL or noncompliance range 0–0.25 µg/mL → stop individual; any cardiac AE/SAE → stop individual. Figure group rule printed “cardiac events ... in more than 10% (three patients)” or ≥2 same cardiac events → convene/review, decide continue/stop. Text and figure definitions preserved separately without diagnosis. Main key: safety decision rules, early stopping.

### S105 — Prospective primary/secondary model and priors

Protocol pp.40–41: IVR stiffness dependent variable; hierarchical levels patient, chloride/sodium subgroups (type 1/2), center. Patient random intercept and random slope; center/subgroup fixed effects; common within-person residual variance. Marginal posterior mean population effect, between-patient variation, individual effects with shrinkage. Investigate treatment×pair and treatment×order interactions. Secondary endpoints analyzed same way. Clinical priors for each individual's treatment effect and population mean effect, other parameters almost noninformative. Mean priors normal with large SD, example placebo mean=5 SD=10; variance priors inverse gamma shape=scale=0.001. Elicited population treatment-effect prior normal mean 1.75 SD 0.89; individual priors elicited from treating physician by 2.5th/97.5th percentiles. Robustness substitution with noninformative priors. Posterior after first pair used as prior for second pair, etc.; stated motivation conjugacy. Main key: primary Bayesian model/random effects/covariates, subgroup analysis, sensitivity to priors, treatment-order interaction.

### S106 — Prospective individual interim rules

Protocol pp.41–43: after pairs 1,2,3, blinded statistician calculates marginal individual posterior; substantial effect >0.75. If P(effect>0.75) ≥80% or ≤20%, advise discontinue; otherwise advise continue; patient and physician discuss effects and choose. Interim uses only noninformative priors to avoid strong elicited prior effect with sparse data. Interim is advisory, no efficacy interim for the aggregated trial. Figure 4 p.43 caption “Likelihood Ratio (LR) calculation during trial”: LR0→LR1→LR2→(LR3), dashed “+ informative priors” annotations, discontinue branches sufficient effectiveness/ineffectiveness versus continue, careful consideration physician/patient, subsequent treatment/no treatment, meta-analysis of combined trials. Figure has no formula/numeric LR threshold. Main key: responder definition, individual stopping, Bayesian prior sensitivity.

## REPORT tables, figures and model relationships

### N108 — Complete eTable 2 baseline rows

Source [eTable 2 p.3](../../../joi180136supp2_prod.pdf#page=3) patients 1–19 and [p.4](../../../joi180136supp2_prod.pdf#page=4) patients 20–30. All IVR values are baseline means; age in years. S/P/W/T = stiffness/pain/weakness/tiredness. A dash means source dash. Family symbols * patients 8/9/19, ** 14/15/16, *** 24/25/26/27; each symbol denotes same family. IVR interactive voice response, CLCN1 skeletal-muscle chloride channel, SCN4A skeletal-muscle sodium channel. Genotype strings retained as source labels. Main key: Table 1 baseline age/sex/genotype, baseline IVR summaries, family structure.

| Patient | Age | Sex | Gene | Mutation(s), allele 1/2 | Previous treatment | Comorbidity | S | P | W | T |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 24 | Male | CLCN1 | Gly233Ser/Gly233Ser | mexiletine, acetazolamide | — | 7.87 | 1.20 | 9.00 | 8.80 |
| 2 | 33 | Male | CLCN1 | Gly285Glu/Arg894X | phenytoin | asthma | 6.93 | 0.00 | 6.00 | 2.93 |
| 3 | 27 | Male | CLCN1 | c.302-1G>A | — | — | 2.85 | 2.31 | 0.00 | 0.00 |
| 4 | 25 | Female | SCN4A | Gly1306Ala | — | — | 4.93 | 2.93 | 2.36 | 2.57 |
| 5 | 25 | Male | CLCN1 | Arg894X/Arg894X | phenytoin | — | 7.07 | 0.00 | 0.00 | 2.36 |
| 6 | 26 | Male | CLCN1 | Gly233Ser/Gly233Ser | acetazolamide, carbamazepine | cluster headache | 7.78 | 6.11 | 7.89 | 7.44 |
| 7 | 39 | Female | SCN4A | Gly305Glu/Ser264fsX6 | — | depression | 5.20 | 0.00 | 0.00 | 4.47 |
| 8* | 21 | Female | SCN4A | Gly1306Val | acetazolamide | — | 5.14 | 3.68 | 0.00 | 5.41 |
| 9* | 51 | Male | SCN4A | Gly1306Val | acetazolamide, gabapentin | — | 5.09 | 5.55 | 0.00 | 6.14 |
| 10 | 32 | Male | SCN4A | Gly1306Ala | — | panic disorder | 4.71 | 2.29 | 0.00 | 7.29 |
| 11 | 53 | Male | SCN4A | Gly1306Val | amitriptyline | stable angina pectoris | 0.00 | 5.12 | 0.00 | 4.47 |
| 12 | 53 | Female | SCN4A | Val1485Phe | — | migraine, arthrosis, asthma | 3.56 | 3.37 | 3.75 | 4.88 |
| 13 | 51 | Male | SCN4A | Arg1148Cys | — | lumbago | 4.23 | 5.46 | 4.38 | 5.46 |
| 14** | 54 | Female | CLCN1 | c.302-2 A>C | — | — | 5.50 | 0.00 | 3.00 | 5.08 |
| 15** | 58 | Male | CLCN1 | c.302-2 A>C | — | hypertension | 7.07 | 0.47 | 3.67 | 2.60 |
| 16** | 60 | Male | CLCN1 | c.302-2 A>C/Met646Ile | quinidine | — | 6.62 | 0.00 | 4.00 | 6.31 |
| 17 | 55 | Male | CLCN1 | Gly285Glu/Met646Ile | — | lumbosacral hernia | 5.87 | 3.67 | 5.13 | 1.07 |
| 18 | 48 | Female | ClCN1 | c.302-2 A>C/Met646Ile | tocainide | — | 5.71 | 0.59 | 4.18 | 0.88 |
| 19* | 21 | Male | SCN4A | Gly1306Val | — | — | 3.31 | 2.00 | 0.23 | 3.85 |
| 20 | 32 | Female | SCN4A | Gly1306Val | — | — | 6.08 | 5.85 | 0.46 | 5.08 |
| 21 | 64 | Male | SCN4A | Gly1306Val | acetazolamide | COPD | 2.77 | 3.00 | 2.62 | 2.62 |
| 22 | 19 | Male | SCN4A | Leu703Pro | acetazolamide | — | 8.00 | 0.00 | 5.00 | 7.00 |
| 23 | 50 | Male | CLCN1 | Gly285Glu/Met646Ile | acetazolamide | — | 7.71 | 0.00 | 7.71 | 0.00 |
| 24*** | 53 | Male | CLCN1 | Phe413Cys | — | — | 6.80 | 3.73 | 4.60 | 7.47 |
| 25*** | 58 | Male | CLCN1 | Phe413Cys | — | hypothyroidism | 6.57 | 0.00 | 2.79 | 3.07 |
| 26*** | 62 | Male | CLCN1 | Phe413Cys | — | — | 6.80 | 0.00 | 3.93 | 3.67 |
| 27*** | 60 | Male | CLCN1 | Phe413Cys | — | cerebral infarction | 6.22 | 0.00 | 0.00 | 6.89 |
| 28 | 65 | Male | CLCN1 | Lys195fsX | quinidine | subdural hematoma | 6.71 | 0.00 | 3.37 | 0.79 |
| 29 | 44 | Female | CLCN1 | Phe413Cys | — | — | 6.71 | 0.00 | 0.57 | 4.86 |
| 30 | 49 | Male | CLCN1 | Gly285Glu | — | panic disorder | 4.62 | 3.69 | 0.00 | 4.00 |

### N109 / S107 — Complete individual primary outcome tuples

Source [eTable 3 p.5](../../../joi180136supp2_prod.pdf#page=5), visual confirmation. Mean treatment effect IVR stiffness = placebo minus mexiletine, 95% credible interval, posterior probability of effect >0.75, final interim number, post-trial treatment. N=27 completed analyzed trials; patients 3/6/7 dropped out. Responders pre-defined >0.80, nonresponders <0.20; nonresponders 11/13/22 bold. Patient 11 exception footnote: probability influenced by wide noninformative prior because observed distribution 0 (95% CI 0;0), no stiffness on either treatment; trial stopped after 1 set and mexiletine discontinued. Printed interval/probability retained separately from footnote's observed-data tuple. Main key: primary individual treatment effects/main figure, responder counts, continuation rules, genotype effects.

| Patient row key | Gene | Interim | Mean effect | 95% CrI | Posterior | Post-trial |
|---|---|---:|---:|---|---:|---|
| 1 | CLCN1 | 2 | 4.4 | 4.03;4.85 | 100% | Continued |
| 2 | CLCN1 | 2 | 3.1 | 2.63;3.49 | 100% | Continued |
| 4 | SCN4A | 2 | 1.1 | 0.27;1.90 | 81% | Continued |
| 5 | CLCN1 | 2 | 4.7 | 4.50;4.87 | 100% | Continued |
| 8 | SCN4A | 1 | 1.2 | −0.03;2.41 | 80% | Continued |
| 9 | SCN4A | 1 | 3.2 | 2.78;3.56 | 100% | Continued |
| 10 | SCN4A | 1 | 3.7 | 2.28;5.04 | 100% | Continued |
| 11 | SCN4A | 1 | 0.00 | −12.24;12.16 | 38%* | Stopped |
| 12 | SCN4A | 1 | 2.66 | 1.76;3.56 | 100% | Continued |
| 13 | SCN4A | 1 | −0.05 | −0.56;0.45 | 2% | Stopped |
| 14 | CLCN1 | 1 | 3.5 | 2.81;4.19 | 100% | Continued |
| 15 | CLCN1 | 1 | 2.7 | 2.16;3.24 | 100% | Continued |
| 16 | CLCN1 | 1 | 4.49 | 3.96;5.03 | 100% | Continued |
| 17 | CLCN1 | 1 | 3.22 | 2.94;3.50 | 100% | Continued |
| 18 | CLCN1 | 1 | 2.55 | 1.77;3.32 | 100% | Continued |
| 19 | SCN4A | 1 | 2.63 | 1.18;4.01 | 99% | Continued |
| 20 | SCN4A | 1 | 1.13 | 0.14;2.13 | 80% | Continued |
| 21 | SCN4A | 1 | 4.41 | 3.80;5.0 | 100% | Continued |
| 22 | SCN4A | 1 | 0.01 | −0.56;0.57 | 1% | Stopped |
| 23 | CLCN1 | 1 | 5.49 | 4.98;6.04 | 100% | Continued |
| 24 | CLCN1 | 1 | 2.64 | 2.16;3.12 | 100% | Continued |
| 25 | CLCN1 | 1 | 1.65 | 1.27;2.03 | 100% | Continued |
| 26 | CLCN1 | 1 | 4.65 | 4.07;5.21 | 100% | Continued |
| 27 | CLCN1 | 1 | 3.14 | 2.46;3.83 | 100% | Continued |
| 28 | CLCN1 | 1 | 4.50 | 4.0;4.99 | 100% | Continued |
| 29 | CLCN1 | 1 | 6.99 | 6.59;7.41 | 100% | Continued |
| 30 | CLCN1 | 1 | 3.57 | 2.91;4.23 | 100% | Continued |

[eFigure 1 p.7](../../../joi180136supp2_prod.pdf#page=7) visual: 11-week set, 4-week treatment period, minimum 11/maximum 44 weeks, four possible sets/8 periods. Visits numbered 1–16, 4 per set; interim 1/2/3 with enough evidence branches yes stop/no continue; interim 4 stop. Illustrative treatment orders M/P, P/M, M/P, P/M with interperiod washout. Actual 4 patients (1,2,4,5) needed 2 sets; other 23 needed 1 set. These are all 27 completed participants. No additional numeric results in graphical boxes.

### N110 — Complete eTable 4 and serious-event figure

Source [p.6](../../../joi180136supp2_prod.pdf#page=6), reported numbers and percentages; denominator not separately labeled in this table, participant roster N=30 supplies matching main key but is not a new denominator claim. Columns mexiletine/placebo. Main key: adverse events, gastrointestinal discomfort, study withdrawals, dose reduction, safety population.

| Reaction/category | Mexiletine No. (%) | Placebo No. (%) |
|---|---|---|
| Gastrointestinal discomfort: reflux, dyspepsia, nausea, diarrhea, flatulence | 21 (70%) | 1 (3%) |
| Tremor | 2 (7%) | 0 (0%) |
| Palpitations | 2 (7%) | 0 (0%) |
| Headache | 1 (3%) | 1 (3%) |
| Insomnia | 1 (3%) | 0 (0%) |
| Any | 27 (90%) | 2 (6%) |
| >1 adverse reactions | 2 (7%) | 0 (0%) |
| >2 adverse reactions | 0 (0%) | 0 (0%) |
| Causing study withdrawal | 1 (3%) | 0 (0%) |
| Leading to dosage reduction | 3 (10%) | 0 (0%) |
| Leading to additional therapy | 2 (7%) | 0 (0%) |
| Serious: allergic skin reaction (toxicodermia) | 1 (3%) | 0 (0%) |

[eFigure 3 p.9](../../../joi180136supp2_prod.pdf#page=9): patient 7, generalized papules after 11 days mexiletine; panel A clinical photograph; B skin biopsy superficial dermatitis/eosinophils/leucostasis, hematoxylin-eosin 40×. No plotted outcome estimate. Histology scale is photographic, not participant quantity.

### S108 — Complete group posterior probability display

Source [eFigure 2 p.8](../../../joi180136supp2_prod.pdf#page=8), NDM group N=27. Horizontal axis mean effect (IVR placebo−IVR mexiletine), ticks −1,0,1,2,3,4,5; vertical probability density function ticks 0.0,0.2,0.4,0.6,0.8. Vertical dotted meaningful threshold 0.75; probabilities area right of threshold: stiffness solid black 100%, pain red dashed 45%, weakness blue dotted 87%, tiredness green dash-dot 74%. Curves centered around corresponding group mean effects; no numeric mean/CrI printed in the plot itself. Main key: group Bayesian primary/secondary IVR effects and posterior probabilities. These probabilities are not frequentist P values.

### S109 — Individual Bayesian model, complete formulas/definitions

Source [eMethods 1 p.10](../../../joi180136supp2_prod.pdf#page=10). For i=1:30 Stiffness_plac[i] ~ dnorm(mu_plac,tau_plac); j=1:30 Stiffness_mex[j] ~ dnorm(mu_mex,tau_mex). Means separately dnorm(0,0.001). sigma_plac and sigma_mex separately dunif(0.01,10), tau_arm=1/(sigma_arm×sigma_arm). diff=mu_plac−mu_mex; p1=step(diff), p2=step(diff−0.75), p3=step(diff−2). Max 30 measurements per period stated. Data scores during respective placebo/mexiletine periods; mu means over days, sigma within-arm SD; probabilities difference >0, >0.75, >2. In WinBUGS code second dnorm argument is precision; retain source precision rather than relabel as variance. Main key: individual mean effect, 95% CrI, noninformative prior/stopping probability.

### S110 — Group hierarchical model, complete formulas/definitions

Source [eMethods 2 p.11](../../../joi180136supp2_prod.pdf#page=11)–p.12. For i=1:n, mu_mex[i] ~ dnorm(mu.mex,tau.mex), mu_plac[i] ~ dnorm(mu.plac,tau.plac), diff_patient[i]=mu_plac[i]−mu_mex[i]. Each t=1:N_plac[i] Stiff_Plac[i,t] ~ dnorm(mu_plac[i],tau.within); each t=1:N_mex[i] Stiff_Mex[i,t] ~ dnorm(mu_mex[i],tau.within). p1=step(mu.plac−mu.mex), p2=step(mu.plac−mu.mex−0.75), p3=step(mu.plac−mu.mex−2). sigma.within, sigma.mex, sigma.plac each dunif(0.01,10); corresponding tau=1/sigma². mu.mex and mu.plac each dnorm(4,0.001). diff=mu.plac−mu.mex.

n patients; N_arm[i] observed counts; population mu mean of individual means, population arm SD between individual means; common within-person SD assumed same for placebo/mexiletine. Printed glossary p.11 calls mu_mex[i] mean during placebo and mu_plac[i] mean during mexiletine; code/data names above retained separately. Printed sigma.mex description continues p.12 as SD “during placebo treatment”; glossary diff definition explicitly placebo minus mexiletine population means. These label transcriptions are recorded without interpretation. Main key: aggregated Bayesian IVR mean effects, 95% CrI, probability >0.75, model hierarchy/common variance/prior.

### S111 — Genotype hierarchical model, complete formulas/definitions

Source [eMethods 3 p.13](../../../joi180136supp2_prod.pdf#page=13)–p.14. Gen_Pat[i]=1 CLCN1,0 SCN4A. mu_gen.mex[i]=a+b×Gen_Pat[i]; mu_gen.plac[i]=c+d×Gen_Pat[i]; mu_mex[i] ~ dnorm(mu_gen.mex[i],tau.mex); mu_plac[i] ~ dnorm(mu_gen.plac[i],tau.plac); diff_patient=mu_plac−mu_mex. Observation likelihoods same arm-specific means and common tau.within as S110. a,b,c,d each dnorm(0,0.01); three sigma priors each dunif(0.01,10), tau=1/sigma². mu.mex_SCN4A=a, mu.mex_CLCN1=a+b, mu.plac_SCN4A=c, mu.plac_CLCN1=c+d. diff_SCN4A=mu.plac_SCN4A−mu.mex_SCN4A; diff_CLCN1=mu.plac_CLCN1−mu.mex_CLCN1. p2_genotype=step(diff_genotype−0.75), p3_genotype=step(diff_genotype−2). Between-person arm SD same for both genotypes; within-person SD same both arms and both genotypes.

Printed glossary p.14 mu_mex[i]/mu_plac[i] names are paired with placebo/mexiletine respectively, as on p.11; sigma.mex description says placebo; diff_CLCN1 glossary line says “mu.plac–mu.mex for SCN4A patients,” while code uses CLCN1. Population probabilities explicitly labeled genotype-specific >0.75 and >2. These source labels are preserved without diagnosis. Main key: genotype Bayesian group stiffness effects/probabilities, subgroup contrast and priors. No subgroup numeric estimate printed in these model pages.

### N111 — Complete simulation summary Tables 1–4

Source [eMethods 4 p.16](../../../joi180136supp2_prod.pdf#page=16) and [p.17](../../../joi180136supp2_prod.pdf#page=17). All six columns each valid N=1000 and missing=0 in both simulations. mean_sets mean pairs per patient; diff.mean.tot=mu.plac.tot−mu.mex.tot; mu arm scores; p1 posterior probability effect>0; p2 posterior probability effect>0.75. Table entries are simulated summary outputs, not formulas or observed patient outcomes. Main key: sample-size operating characteristics, power/type I error and bias.

| Null true effect 0 statistic | mean_sets | diff.mean.tot | mu.mex.tot | mu.plac.tot | p1.mean.tot | p2.mean.tot |
|---|---:|---:|---:|---:|---:|---:|
| Mean | 3.41 | .07 | 4.58 | 4.65 | .55 | .12 |
| Median | 3.43 | .06 | 4.57 | 4.66 | .55 | .09 |
| SD | .21 | .27 | .38 | .31 | .19 | .10 |
| Minimum | 2.73 | −.85 | 3.46 | 3.74 | .04 | .00 |
| Maximum | 3.97 | .95 | 5.82 | 5.57 | .97 | .66 |
| 25th percentile | 3.27 | −.12 | 4.32 | 4.43 | .41 | .04 |
| 50th percentile | 3.43 | .06 | 4.57 | 4.66 | .55 | .09 |
| 75th percentile | 3.57 | .25 | 4.83 | 4.86 | .69 | .17 |

Null Table 2 category .00 frequency1000, percent100, valid percent100,cumulative100; category1.00 frequency .00, percent .00,valid .00,cumulative100; total1000,percent100,valid100,cumulative100. Type I error definition number of times p2.mean.tot>80%, p2_effect=1; narrative 0.00.

| Alternative true effect 1.75 statistic | mean_sets | diff.mean.tot | mu.mex.tot | mu.plac.tot | p1.mean.tot | p2.mean.tot |
|---|---:|---:|---:|---:|---:|---:|
| Mean | 2.59 | 1.29 | 3.38 | 4.67 | .99 | .83 |
| Median | 2.60 | 1.29 | 3.37 | 4.67 | 1.00 | .86 |
| SD | .25 | .26 | .35 | .31 | .02 | .12 |
| Minimum | 1.73 | .43 | 2.44 | 3.79 | .81 | .26 |
| Maximum | 3.47 | 2.13 | 4.60 | 5.59 | 1.00 | 1.00 |
| 25th percentile | 2.43 | 1.12 | 3.13 | 4.46 | .99 | .77 |
| 50th percentile | 2.60 | 1.29 | 3.37 | 4.67 | 1.00 | .86 |
| 75th percentile | 2.73 | 1.46 | 3.62 | 4.88 | 1.00 | .93 |

Alternative Table 4 category .00 frequency315, percent31.5 (source decimal comma in Percent),valid31.5,cumulative31.5; category1.00 frequency685,percent68.5,valid68.5,cumulative100.0; total1000,percent100.0,valid100.0, cumulative cell blank. Power positive conclusion P(effect>0.75)>80%, 685/1000=68.5%; mean bias printed −0.46 [1.29−1.75].

## Coverage and limitations

39/39 numeric families complete. Subordinate support rows:30 baseline patients;27 individual outcomes;12 adverse-reaction/category rows;16 simulation summary rows containing96cells, plus2 complete frequency tables and12 valid/missing column pairs. Main numeric table cross-references:14 Table1 rows and34 Table2 outcome rows. Every row's scale, sign, displayed dispersion/interval and relevant denominator was inspected; inferential compatibility is separately tracked in the canonical statistical inventory. No sampling was applied. No source or reused asset was modified. No new derivative file was needed: direct Poppler25.03.0 layout extracts were read to standard output for DOC-001 pp5–8, DOC-002 pp38–39 and DOC-003 pp3–6/15–17. Exact source pages confirmed the finding inputs. Reused DOC-001 p5 image was visually inspected; no OCR disagreement found. No scientific coverage gap; unreported paired contributor sets, adverse-category completeness and adherence denominators limit mechanical reconstruction and are explicitly excluded below in the checker. Graphical approximate coordinates are not exact count or estimate inputs.
