# Statistical relationship inventory — pass 1 report/regimen shard

Runtime agent: /root/statistical_pass_1; model gpt-6.1-sol; effort high; fresh mandatory pass 1. Exact scope: all REPORT evidence DOC-001 pp1–12, DOC-004 pp1–26, DOC-005 pp1–6, DOC-006 p1, and PLAN DOC-003 pp66–130, including their report comparisons. Complementary PLAN-only shard S201 onward is owned by a distinct fresh specialist and merged by the coordinator. No old scientific outputs or external evidence were used. Original supplied PDFs are final authority; current mapper records retain every occurrence.

This shard contains S001–S112 (112 distinct relationships). A relationship bundles its estimate, bounds, standard error, test and repeated occurrences; different endpoint/dose/population rows remain distinct. The 35 forest rows include all three printed estimates and all 105 printed intervals. Block P values are interaction tests, never reassigned to a single within-subgroup contrast. Definitions and versions reused by several outcomes are cross-referenced rather than silently duplicated. The canonical source occurrence index consists of main M001–M100; support SP5-N001–N012/SP5-S001–S057; support SP6-N001–N033/SP6-S001–S019, with exact page-specific transcriptions in the current extraction files.

## Pass 1 checking conventions

Every result row below was checked for point containment, ordered limits, direction, null versus printed test, applicable population/window/model and matched occurrences. Every model row was checked for necessary steps, coherent design/data structure, planned versus reported specification and conclusions under the stated rule. Bayesian credible intervals and posterior probabilities are not frequentist P values. Primary success requires posterior Pr(DRR<1) at least .979, and futility is Pr(DRR<.9)<.05; .645/.65 does not establish either success or futility. No trial interim posterior is printed, so the statement that no futility cutoff was met is not numerically reproducible from final posterior alone. No raw-data, covariance, degrees-of-freedom, multiplicity or sidedness convention is invented. Profile-likelihood survival intervals need not be log symmetric around the Cox estimate.

For Wald displays, estimate ±1.96×SE and z=estimate/SE are explicitly diagnostic approximations; they do not replace finite-df mixed-model inference. Display-half-unit intervals are used for numeric reproduction, with relative gaps at most .05 screened out. Interval/test conflicts under route A category 1 are exempt from that precision screen. Checks with no source contradiction are retained as completed records, not excluded observations. Each row has an explicit pass-1 recheck fact; pass 2 remains the responsibility of a different fresh agent.

## Stable relationships

Source shorthand: D1 = REPORT main article; D3 = PLAN SAP bundle; D4 = REPORT results supplement. Page numbers are physical supplied-PDF pages. Citations and exact values are in the mapper occurrence index above, supplemented by direct current-run source extraction/visual evidence in preprocessing/statistics-1/. All statuses below apply individually.

| S ID | Exact relationship and occurrences | Pass-1 check/recheck fact | Pass 1 status |
|---|---|---|---|
| S001 | D1 pp1,2,4,9; D4 p15 common DRR .97 CrI .783–1.175; median .96; SD .099; Pr<1 .6450/.65; Pr<.9 .2505 | Estimate contained; null inside; posterior below .979 and above futility .05; no primary benefit claim reconciles. | PASS_1_COMPLETE |
| S002 | D1 p4 regimen-only DRR .96 CrI .709–1.357 | Contained, ordered, null inside; separate ERO population retained. | PASS_1_COMPLETE |
| S003 | D1 p4; D4 p15 placebo ALSFRS Bayesian slope −1.03, SD .073, CrI −1.181–−.894; main −1.176–−.892 | Contained, decline direction; between-location tiny endpoints within .05 relative precision. | PASS_1_COMPLETE |
| S004 | D1 p4; D4 p15 active Bayesian slope −1.00, SD .075, CrI −1.143–−.847; main −1.153–−.858 | Contained, decline direction; between-location endpoint differences within .05 relative precision. | PASS_1_COMPLETE |
| S005 | D1 p4 placebo monthly exponential mortality .007; D4 p15 .010 SD .0026 CrI .0054–.0154 | Interval contains supplement estimate; matched source copies disagree beyond precision; numeric/cross-source lane tracks count/rate extraction implications. | PASS_1_COMPLETE |
| S006 | D1 p4 active monthly exponential mortality .006; D4 p15 .009 SD .0025 CrI .0052–.0150 | Interval contains supplement estimate; matched source copies disagree beyond precision; same rate discrepancy pattern as S005. | PASS_1_COMPLETE |
| S007 | D4 p15 onset covariate median/mean1.03 SD .046 CrI .938–1.120 | Ordered, contained; not a treatment contrast or frequentist test. | PASS_1_COMPLETE |
| S008 | D4 p15 prebaseline slope median1.39 mean1.40 SD .079 CrI1.255–1.565 | Ordered, contained; no mismatched P assigned. | PASS_1_COMPLETE |
| S009 | D4 p15 edaravone covariate1.13 SD .101 CrI .949–1.344 | Ordered, contained; null inside. | PASS_1_COMPLETE |
| S010 | D4 p15 riluzole covariate1.03 SD .093 CrI .854–1.220 | Ordered, contained; null inside. | PASS_1_COMPLETE |
| S011 | D1 pp3–4 CAFS pooled/shared ranks140.5/143.9, Wilcoxon P.51; D4 p9 supportive CAFS | Direction agrees with no benefit; ranks are adjusted-model-independent summaries, not DRR estimates. Planned adjusted inference tracked S085. | PASS_1_COMPLETE |
| S012 | D1 p4 baseline-NfL CAFS sensitivity P.88 | No interval supplied; nonsignificant interpretation consistent; base-method identity linked S085. | PASS_1_COMPLETE |
| S013 | D1 p4 SVC NfL sensitivity active slope −1.73 CrI/CI −2.18–−1.29 PPN/month | Containment/order and decline agree; distinct slope model from 24-week repeated-measures result. | PASS_1_COMPLETE |
| S014 | D1 p4 SVC NfL sensitivity placebo slope −1.55 CI −1.94–−1.17 PPN/month | Containment/order and decline agree; covariance of treatment contrast absent, not inferred. | PASS_1_COMPLETE |
| S015 | D1 pp4,6,7 Table2 pooled/shared PAV-free HR .46 CI .12–1.49 P.22, 5/120 vs9/162 | Contained; null inside and P>.05 agree; adjusted profile-likelihood CI not replaced by crude risks. | PASS_1_COMPLETE |
| S016 | D1 pp6–7 Table2 30mg/shared HR .06 CI .002–.56 P.04,1/59 vs9/162 | Contained; CI excludes1 and P<.05 agree; nominal exploratory claim retained. | PASS_1_COMPLETE |
| S017 | D1 pp6–7 Table2 60mg/shared HR .96 CI .25–3.08 P.95,4/61 vs9/162 | Contained; null inside and P>.05 agree. | PASS_1_COMPLETE |
| S018 | D1 pp6–7 Table2 pooled/regimen HR .25 CI .05–1.09 P.06,5/120 vs4/41 | Contained; null inside and P>.05 agree. | PASS_1_COMPLETE |
| S019 | D1 pp6–7 Table2 30mg/regimen HR .03 CI .0004–.36 P.03,1/59 vs4/41 | Contained; CI excludes1 and P<.05 agree; profile likelihood explains asymmetry. | PASS_1_COMPLETE |
| S020 | D1 pp6–7 Table2 60mg/regimen HR .47 CI .10–2.16 P.32,4/61 vs4/41 | Contained; null inside and P>.05 agree. | PASS_1_COMPLETE |
| S021 | D1 p4 survival NfL sensitivity HR .45 CI .11–1.50 | Contained, ordered, null inside; no source P to invent. | PASS_1_COMPLETE |
| S022 | D1 p7 assisted ventilation16(18%)/9(31%), HR .40 CI .17–1.01 | Contained; null inside; no printed P; prevalent exclusions mean unspecified risk sets are not120/41 by assumption. | PASS_1_COMPLETE |
| S023 | D1 p7 gastrostomy14(12%)/7(17%), HR .37 CI .14–1.04 | Contained; null inside; no printed P; direction of nominal point estimate favorable. | PASS_1_COMPLETE |
| S024 | D1 p7 ALS-related SAE admission5(4%)/3(7%), HR .23 CI .04–1.33 | Contained; null inside; no printed P. | PASS_1_COMPLETE |
| S025 | D1 p7 SAE admission14(12%)/7(18%), HR .48 CI .18–1.33 | Contained; null inside; no printed P; baseline exclusion and time-to-event model retained. | PASS_1_COMPLETE |
| S026 | D4 p16 FAS pooled ALSFRS −5.47(.43)/−5.51(.36), difference0.0(.55), CI −1.03–1.11 P.94 | Difference .04 within printed0.0 half-unit; containment/null/P agree; diagnostic Wald halfwidth1.078 agrees. | PASS_1_COMPLETE |
| S027 | D4 p16 FAS pooled SVC −9.32(1.36)/−8.53(1.15), difference−.78(1.77), CI−4.25–2.68 P.66; D1 p4 | Contrast arithmetic accommodates half units; Wald halfwidth3.4692; null/P agree; unit copy tracked S087. | PASS_1_COMPLETE |
| S028 | D4 p16 FAS30 ALSFRS −5.70(.59)/−5.51(.36),−.19(.69),CI−1.53–1.16 P.79 | Contained/null/P agree; diagnostic z−.275; precision handles modest finite-df/rounding differences. | PASS_1_COMPLETE |
| S029 | D4 p16 FAS30 SVC −7.84(1.84)/−8.53(1.15), .69(2.19),CI−3.55–4.92 P.75; D1 p4 | Contained/null/P agree; diagnostic z.315; adjusted contrast equals printed group difference. | PASS_1_COMPLETE |
| S030 | D4 p16 FAS60 ALSFRS −5.24(.59)/−5.51(.36), .27(.68),CI−1.07–1.60 P.69 | Contained/null/P agree; diagnostic z.397. | PASS_1_COMPLETE |
| S031 | D4 p16 FAS60 SVC −10.79(1.99)/−8.53(1.15),−2.26(2.29),CI−6.75–2.24 P.33; D1 p4 | Contained/null/P agree; diagnostic z−.987. | PASS_1_COMPLETE |
| S032 | D4 p17 ERO pooled ALSFRS −5.45(.44)/−5.39(.71),−.07(.83),CI−1.71–1.57 P.94 | Printed group subtraction−.06 and contrast−.07 intervals overlap; null/P agree. | PASS_1_COMPLETE |
| S033 | D4 p17 ERO pooled SVC −9.57(1.38)/−6.74(2.29),−2.83(2.67),CI−8.10–2.44 P.29 | Contained/null/P agree; diagnostic z−1.060. | PASS_1_COMPLETE |
| S034 | D4 p17 ERO pooled plasma changes−2.3/+7.9;−9.5 CI−18.0–0 P.04; D1 p8 Fig3A−9.5 CI−17.8–−.5/text−.4 P.04 | Printed p17 interval contains0 with P<.05; F-ST1-001. GMR calculation reproduces plasma row; S088. | PASS_1_COMPLETE |
| S035 | D4 p17 ERO pooled serum+.4/+26.8;−26.4 CI−50.3–−2.6 P.03; D1 p8 Fig3B−23.2 CI−39.5–−2.5 P.03 | Estimate contained/null/P agree; serum scale/calculation does not reproduce paired plasma method, F-ST1-006. | PASS_1_COMPLETE |
| S036 | D4 p17 ERO30 ALSFRS −5.56(.60)/−5.39(.71),−.17(.93),CI−2.00–1.66 P.85 | Contained/null/P agree; diagnostic z−.183. | PASS_1_COMPLETE |
| S037 | D4 p17 ERO30 SVC −7.61(1.86)/−6.74(2.29),−.87(2.94),CI−6.69–4.95 P.77 | Contained/null/P agree; diagnostic z−.296. | PASS_1_COMPLETE |
| S038 | D4 p17 ERO30 plasma−1.3/+7.9;−8.5 CI−18–2 P.10 | Contained/null/P agree; GMR method reproduces−8.5 under half-unit precision. | PASS_1_COMPLETE |
| S039 | D4 p17 ERO30 serum+1.4/+26.8;−25.5 CI−52.2–1.3 P.06 | Contained/null/P agree; serum contrast scale pattern F-ST1-006. | PASS_1_COMPLETE |
| S040 | D4 p17 ERO60 ALSFRS −5.35(.61)/−5.39(.71), .04(.93),CI−1.79–1.87 P.97 | Contained/null/P agree; diagnostic z.043. | PASS_1_COMPLETE |
| S041 | D4 p17 ERO60 SVC −11.53(1.98)/−6.74(2.29),−4.79(3.03),CI−10.76–1.19 P.12 | Contained/null/P agree; diagnostic z−1.581. | PASS_1_COMPLETE |
| S042 | D4 p17 ERO60 plasma−3.4/+7.9;−10.5 CI−20–0 P.04 | Printed interval contains0 with P<.05; repeated F-ST1-001. GMR method reproduces−10.5. | PASS_1_COMPLETE |
| S043 | D4 p17 ERO60 serum−.5/+26.8;−27.4 CI−45.1–−.7 P.05 | CI excludes0 while printed P=.05 is not<.05; repeated F-ST1-001; scale pattern F-ST1-006. | PASS_1_COMPLETE |
| S044 | D4 p18 all participants slopes−.98 CI−1.13–−.82 /−1.01 CI−1.13–−.88;diff .03 CI−.16–.23 | All three contained/ordered; difference crosses0; no benefit claim agrees. | PASS_1_COMPLETE |
| S045 | D4 p18 riluzole N slopes−1.07 CI−1.39–−.75 /−.88 CI−1.15–−.61;diff−.19 CI−.60–.22;block P.22 | All contained/ordered; difference crosses0; P is interaction, not this row contrast. | PASS_1_COMPLETE |
| S046 | D4 p18 riluzole Y slopes−.95 CI−1.12–−.78 /−1.05 CI−1.19–−.90;diff .10 CI−.12–.32 | Contained/ordered; difference crosses0; same block P.22. | PASS_1_COMPLETE |
| S047 | D4 p18 edaravone N slopes−1.00 CI−1.17–−.83 /−.96 CI−1.10–−.81;diff−.04 CI−.27–.18;block P.19 | Contained/ordered; difference crosses0; interaction distinct. | PASS_1_COMPLETE |
| S048 | D4 p18 edaravone Y slopes−.91 CI−1.22–−.60 /−1.17 CI−1.43–−.90;diff .26 CI−.14–.66 | Contained/ordered; difference crosses0. | PASS_1_COMPLETE |
| S049 | D4 p18 neither drug slopes−1.15 CI−1.49–−.81 /−.82 CI−1.10–−.54;diff−.33 CI−.77–.10 | Contained/ordered; difference crosses0. | PASS_1_COMPLETE |
| S050 | D4 p18 riluzole only slopes−.94 CI−1.14–−.75 /−1.01 CI−1.18–−.83;diff .06 CI−.20–.32 | Group difference rounding accommodates .06; contained/ordered/null inside. | PASS_1_COMPLETE |
| S051 | D4 p18 edaravone only slopes−.49 CI−1.45–.47 /−1.38 CI−2.27–−.49;diff .89 CI−.42–2.20 | Contained/ordered; difference crosses0 despite individual placebo slope excluding0. | PASS_1_COMPLETE |
| S052 | D4 p18 both drugs slopes−.96 CI−1.28–−.64 /−1.15 CI−1.43–−.88;diff .19 CI−.23–.61 | Contained/ordered; difference crosses0. | PASS_1_COMPLETE |
| S053 | D4 p18 age<65 slopes−.97 CI−1.15–−.80 /−1.03 CI−1.18–−.88;diff .05 CI−.18–.28;block P.81 | Subtraction precision accommodates .05; contained/ordered/null inside; P interaction. | PASS_1_COMPLETE |
| S054 | D4 p18 age≥65 slopes−.95 CI−1.23–−.68 /−.95 CI−1.19–−.71;diff0 CI−.36–.36 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S055 | D4 p19 female slopes−.98 CI−1.22–−.74 /−1.10 CI−1.33–−.87;diff .12 CI−.21–.45;block P.50 | Contained/ordered/null inside; interaction not within-row test. | PASS_1_COMPLETE |
| S056 | D4 p19 male slopes−.99 CI−1.18–−.80 /−.97 CI−1.12–−.81;diff−.02 CI−.27–.22 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S057 | D4 p19 White slopes−.95 CI−1.10–−.80 /−1.01 CI−1.14–−.88;diff .06 CI−.14–.25 | Contained/ordered/null inside; no race interaction P printed. | PASS_1_COMPLETE |
| S058 | D4 p19 notHispanic/Latino slopes−.97 CI−1.13–−.82 /−1.01 CI−1.14–−.88;diff .04 CI−.16–.24 | Contained/ordered/null inside; no ethnicity interaction P printed. | PASS_1_COMPLETE |
| S059 | D4 p19 weight<56 slopes−1.39 CI−2.02–−.76 /−1.14 CI−1.73–−.55;diff−.25 CI−1.11–.60 | Contained/ordered/null inside; no block P printed. | PASS_1_COMPLETE |
| S060 | D4 p19 weight56–<77 slopes−.93 CI−1.18–−.68 /−1.04 CI−1.25–−.83;diff .11 CI−.21–.43 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S061 | D4 p19 weight77–<150 slopes−.95 CI−1.14–−.75 /−.97 CI−1.14–−.80;diff .03 CI−.23–.28 | Subtraction precision accommodates .03; contained/ordered/null inside. | PASS_1_COMPLETE |
| S062 | D4 p19 BMI<18.5 slopes−.43 CI−1.50–.63 /−1.40 CI−2.30–−.49;diff .96 CI−.43–2.35 | Subtraction precision accommodates .96; contained/ordered/null inside. | PASS_1_COMPLETE |
| S063 | D4 p19 BMI18.5–<25 slopes−1.03 CI−1.29–−.78 /−1.07 CI−1.28–−.85;diff .03 CI−.30–.36 | Subtraction precision accommodates .03; contained/ordered/null inside. | PASS_1_COMPLETE |
| S064 | D4 p19 BMI25–<30 slopes−.95 CI−1.18–−.72 /−.93 CI−1.13–−.73;diff−.02 CI−.33–.28 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S065 | D4 p19 BMI30–<40 slopes−1.00 CI−1.32–−.68 /−1.09 CI−1.36–−.82;diff .09 CI−.33–.50 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S066 | D4 p19 BMI≥40 slopes−.35 CI−1.26–.56 /−.15 CI−1.05–.76;diff−.21 CI−1.49–1.07 | Subtraction precision accommodates−.21; contained/ordered/null inside. | PASS_1_COMPLETE |
| S067 | D4 p19 CKD1 slopes−.99 CI−1.16–−.81 /−1.04 CI−1.20–−.88;diff .05 CI−.18–.29 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S068 | D4 p19 CKD2 slopes−.92 CI−1.22–−.63 /−.92 CI−1.15–−.69;diff0 CI−.38–.37 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S069 | D4 p19 onset<18months slopes−.99 CI−1.28–−.69 /−.95 CI−1.22–−.68;diff−.04 CI−.37–.30;block P.59 | Contained/ordered/null inside; block interaction P. | PASS_1_COMPLETE |
| S070 | D4 p19 onset≥18months slopes−.96 CI−1.18–−.75 /−1.04 CI−1.23–−.85;diff .08 CI−.16–.32 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S071 | D4 p20 definite/onset<18 slopes−1.05 CI−1.40–−.71 /−1.25 CI−1.65–−.86;diff .20 CI−.29–.69;block P.53 | Contained/ordered/null inside; complementary row label identity reviewed separately. | PASS_1_COMPLETE |
| S072 | D4 p20 notdefinite/onset<18 printed slopes−.95 CI−1.12–−.77 /−.97 CI−1.11–−.84;diff .03 CI−.19–.24 | Arithmetic precision accommodates .03; contained/null inside; source-label versus complement is a separate extraction relationship. | PASS_1_COMPLETE |
| S073 | D4 p20 allALSFRSitems≥2 slopes−.99 CI−1.31–−.67 /−.88 CI−1.11–−.65;diff−.11 CI−.50–.27;block P.38 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S074 | D4 p20 anyitem<2 slopes−.99 CI−1.17–−.81 /−1.08 CI−1.25–−.91;diff .09 CI−.13–.32 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S075 | D4 p20 NfL<median slopes−.85 CI−1.07–−.64 /−.95 CI−1.12–−.78;diff .10 CI−.17–.36;block P.74 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S076 | D4 p20 NfL≥median slopes−1.04 CI−1.25–−.83 /−1.07 CI−1.26–−.88;diff .03 CI−.25–.31 | Contained/ordered/null inside. | PASS_1_COMPLETE |
| S077 | D4 p20 dFRS<median slopes−.84 CI−1.07–−.62 /−.91 CI−1.09–−.72;diff .06 CI−.21–.34;block P.70 | Subtraction precision accommodates .06; contained/null inside. | PASS_1_COMPLETE |
| S078 | D4 p20 dFRS≥median slopes−1.16 CI−1.41–−.90 /−1.14 CI−1.36–−.93;diff−.01 CI−.29–.27 | Subtraction precision accommodates−.01; contained/null inside. | PASS_1_COMPLETE |
| S079 | D1 p8 serum outlier sensitivity−9.7 CI−18.5–.1 P.05; D4 p25 reverse contrast+9.7 CI−.1–18.5 P.051; active+.8/PBO11.6 | Containment and reverse-direction signs reconcile; rounded .05 vs .051 precision and inclusive null support no nominal benefit; missing exact model-df acknowledged. | PASS_1_COMPLETE |
| S080 | D1 p8 serious TEAE9%/10%/16%/17%, P.31; D4 p21 counts15/163,6/59,10/61,7/41 | No CI; nested placebo groups not four independent arms by assumption; test identity absent, no numerical contradiction demonstrated. | PASS_1_COMPLETE |
| S081 | D1 pp2–4; D4 pp7–9; D3 pp83,116–117 Bayesian joint repeated function/exponential mortality, DRR effect, hierarchy borrowing | Coherent model links common slowing; no requirement to equal crude ratio; unreported MCMC draws are limited by disclosed diagnostics. | PASS_1_COMPLETE |
| S082 | D1 pp3–4,9; D4 p9; D3 pp83,117–118 posterior threshold/futility/noearlysuccess/secondary closed sequence | Final primary fails .979; no lower confirmatory claim; dose30 survival/NfL explicitly nominal/exploratory; reported failure to stop needs interim posterior not supplied. | PASS_1_COMPLETE |
| S083 | D1 pp3,5; D4 pp6–7; D3 pp82,115–117 FAS/ERO/ECM/EPP/STF/STN/SRO; concurrent A/B/D shared controls | Randomized284 efficacy versus283 safety distinguishable; report FAS and ERO primary results, additional planned sets tracked S094. | PASS_1_COMPLETE |
| S084 | D3 pp71,94,96–98,104 governing hierarchy and plan versions | RegimenSAP3 governs focal design; later MasterSAP3 applies later regimens, not automatically this2020–2022 regimen. Disclosed v1→v3 modifications retained. | PASS_1_COMPLETE |
| S085 | D3 pp84–85,118–119 CAFS adjusted primary, unadjusted sensitivity; D1 pp3–4 Wilcoxon primary P.51 | Direct source planned regression/onset,dFRS,drugs versus reported Wilcoxon differs; F-ST1-002. | PASS_1_COMPLETE |
| S086 | D3 p118 hierarchical two-tailedP<.05 vs CAFS code one-sided upper test | Stated sidedness differs inside plan for same primary key secondary analysis; F-ST1-007; code-variable symbol slip separately excluded. | PASS_1_COMPLETE |
| S087 | D1 p4 mean change over24wk −9.32,−7.84,−10.79,−8.53 and−.78 labeled PPN/month; D4 p16 24-week change | Quantity-changing repeated main label for SVC; F-ST1-004, with genuine monthly sensitivity model S013–014 distinguished. | PASS_1_COMPLETE |
| S088 | D1 p8 Fig3; D4 p17 NfL log/exponentiated/GMR contrast and serum/plasma groups | Same GMR method reproduces all three plasma rows but not serum rows; F-ST1-006; do not apply crude arithmetic to an otherwise coherent adjusted effect. | PASS_1_COMPLETE |
| S089 | D3 pp78,89,111,126 delta-FRS formula permonth vs subgroup thresholds labeled points/year | Label discrepancy apparent; monthly definition and report median split supply immediate reading; excluded notation/unit observation. | PASS_1_COMPLETE |
| S090 | D1 p3 plasma prespecified regimen-only; D4 p6 plasma posthoc; D3 pp77,110,112,127 serum/CSF NfL scope/separatePD plans | Prespecification attribution differs for same plasma result; F-ST1-005; absent separate plans are alternative, not reconstructed evidence. | PASS_1_COMPLETE |
| S091 | D1 p3 planned serumFAS replaced by posthoc regimen-only rerun; D3 pp77,110,115–119 | Exploratory analysis population substitution is expressly disclosed with plate-rerun explanation; no primary/key-secondary omission or outcome-status change established; excluded context. | PASS_1_COMPLETE |
| S092 | D3 pp96–98,119–121 repeated measures treatment main/revised contrast versus estimand paragraph shared-baseline | Source amendment/code supplies intended nonshared baseline; residual phrase does not alter printed result by itself, excluded context. | PASS_1_COMPLETE |
| S093 | D3 pp85,119–121 repeated measures code and printed contrast `post*trtrnd*visit` versus model `trtrnd|visit` | Template `post` absent from supplied model; intended baseline/week24 subtraction identified by coefficients/prose; excluded notation, not a preferred model critique. | PASS_1_COMPLETE |
| S094 | D3 pp116–117,119,125 BayesianECM/EPP and planned CAFS/SVC MI/deathalone/supportive analyses; report full results | Named planned primary/key secondary analysis results absent; F-ST1-003. Generic performed-sensitivity statement supplies no result estimates/tests. | PASS_1_COMPLETE |
| S095 | D3 pp72–75,105–108; D4 pp3–5 3:3:2 randomized regimen strata/24week dose volumes | Allocation and formulation arithmetic coherent; each dose60mL×2 at250/500μg/mL yields30/60mg. | PASS_1_COMPLETE |
| S096 | D3 pp76,109 general transformation/MAR/baseline conventions; D1 p3, D4 pp10–12 | Source versions delegate master conventions; MAR mixed models explicitly coherent, no alternative preferred. | PASS_1_COMPLETE |
| S097 | D3 pp77–79,110–113 ALSFRS0–48,delta-FRS,SVC GLI,homeFVC,HHD loss-of-strength definitions | Score directions and numeric bounds coherent; method/count definitions mapped; no raw scoring audit. | PASS_1_COMPLETE |
| S098 | D3 pp79,85–87,113,121–123 survivalcomposite/deathalone,windows,censoring/logrank/Cox | Age covariate stated; mainTable2 also sex versus method list, exact model attribution not automatically inferred; profile-likelihood intervals accepted as supplied. | PASS_1_COMPLETE |
| S099 | D3 pp80,87,114,123 clinical event/death composites and King's interval censoring; D4 pp6,12; D1 p7 | Prevalent-event exclusions source-defined; composite clinical events include death/PAV, risk sets not invented from group n. | PASS_1_COMPLETE |
| S100 | D3 pp87,124 standardized slope composite ALSFRS/SVC/ALSAQ, unadjusted then adjustedANOVA | Distinct analyses/models disclosed by revisions; no printed observed composite result, exploratory omission peripheral. | PASS_1_COMPLETE |
| S101 | D3 pp78,87,112,124 HHD0/02 interval-censored Cox/functional support | Death/death-equivalent component source-defined; no observed HR/CI supplied; exploratory outcome not mistaken for missing key secondary. | PASS_1_COMPLETE |
| S102 | D3 pp87–88,112,124 voice cubicB-splineknots8/16,random effects/AR1/fallbacks | Methods match repeated voice structure; convergence sequence prespecified and internally coherent; no printed voice estimate to challenge. | PASS_1_COMPLETE |
| S103 | D3 pp88,119,125 reference-basedMI50imputations/FCS/regression/death support | Inherited50-imputation sensitivity and bounds explicit; v3 change disclosed; required result omissions in S094, not method preference. | PASS_1_COMPLETE |
| S104 | D3 pp88–89,125–126; D4 p13 subgroup interactions/cutoffs/convergence | Prespecified site/earlydisease/urate and other subgroups not present in ALSFRSforest35rows; declared allprespecified subgroup statement alone lacks estimates; cross-source completeness and keyanalysis route tracked F-ST1-003 only where primary/key. | PASS_1_COMPLETE |
| S105 | D3 pp89,126 shared-control heterogeneitydiagnostic, regimen effects/NfLsupport | Model choice coherent; report generic borrowing description not quantitative diagnostic output; report basis not reconstructed. | PASS_1_COMPLETE |
| S106 | D3 pp89–90,112–114,127 PK/PD separateplans/BLQ/geomean/geoCV/lognormalCI | Separate plans absent; PK/PD details alone not a contradiction; serum/CSFNfL remit distinct from otherPD. | PASS_1_COMPLETE |
| S107 | D3 pp90–91,127–128 safetyPoisson exposureoffset/ratedifference95%deltaCI; D4 pp21–24 | Supplement prints incidenceproportions/eventcounts, no rate estimates orCI; no ratio label attributed to absent rates. | PASS_1_COMPLETE |
| S108 | D3 pp77,81,90–91,110,115,127–128 lab/DILI/CTCAE/CSSRS safetydefinitions | Explicit thresholds and time windows coherent; broad clinical assessment excluded. | PASS_1_COMPLETE |
| S109 | D3 pp91–93,128–130 flow/exposure/blindingFisher/guessdifferenceCI/history/deviations | No inferential blinding results printed; auxiliarymethod not primary/key, no false missing-result finding. | PASS_1_COMPLETE |
| S110 | D1 pp3,7; D4 pp10,13; D3 pp86–89,122–126 randomslopes fixedtreatment/month, covariate×month,regimen/participantUN | v3 equation/code treatmentmain matches; monthlytime conversion12/365.25 coherent; not same model as24weekMMRM. | PASS_1_COMPLETE |
| S111 | D4 pp10–12 serum rerun/outlier thresholds <4pg/mL or<2%max,1baselineomitted;D1 pp3,8 | Rerun/outlier sensitivity disclosed; primary noexclusions and sensitivity1exclusion are different analyses, not contradiction. | PASS_1_COMPLETE |
| S112 | D5 pp1–6 collaboratorroster; D6 p1 softwarescope; D1 pp10–12/D4pp1–2,26 administration/rights | All units inspected/mapped, no additional inferential relationship; softwareSAS/R/JAGS versionbounds compatible, unavailablecode not quantitative finding. | PASS_1_COMPLETE |

## Direct-source evidence and limitations

All current mapping inputs were read anew. Direct confirmation derivatives from supplied PDFs: main pp3–4 sorted layout; SAP pp109–115 and116–123 sorted layouts; results-supplement p6 sorted layout; results-supplement p17 rendered image, visually inspected. Engine for each: bundled pdf_tools.py with /home/juliz/venvs/stt/bin/python, PyMuPDF1.28.0. Rendering CPU200dpi; no OCR run. Source-matched legacy images/transcriptions locate remaining rows and exact source recheck remains mandatory for registered candidates. No inferred unprinted graph coordinates or model degrees of freedom. Simulation assumptions and primary Bayesian prior computations are exclusively in disjoint PLAN shard S201 onward. No scientific-coverage gap; model diagnostic reproduction limited by absent posterior draws, interim posteriors, mixed-model covariance/df, complete Cox likelihood and unavailable separate PK/PD plans. These limitations are named, not converted into findings.
