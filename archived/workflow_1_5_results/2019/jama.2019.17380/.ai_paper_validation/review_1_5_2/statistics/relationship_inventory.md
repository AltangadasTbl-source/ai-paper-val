# Canonical Statistical Relationship Inventory

Canonical IDs were assigned after complete disjoint fresh mapping. Each relationship must receive both PASS_1_COMPLETE and PASS_2_COMPLETE status before completion.

## Pass completion state

- **PASS_1_COMPLETE:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039
- **PASS_2_COMPLETE:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039

## Main article — DOC-001

Provisional IDs are local to this mapper. All results require the downstream two-pass statistical review. Locations are `jama_de_boer_2019_oi_190122.pdf#page=N`.

| ID | Result, population/model/contrast, and exact printed values | Status |
|---|---|---|
| S001 | Primary D3 vs placebo, full randomized population, age/sex/baseline ACR-adjusted mixed model with imputation: y5 difference in eGFR change +0.9 mL/min/1.73m2 (95%CI -0.7 to2.5), P=.25; positive=slower decline with active (p8 Table2; p1,p4 repetitions). | MAPPED. |
| S002 | Primary omega vs placebo, same model: y5 difference +0.9 (-0.7 to2.6), P=.27 (p8; p1,p4 repetitions). | MAPPED. |
| S003 | D3 vs placebo biomarker at y2: mean25OHD41.4(SD11.0) vs29.8(SD11.1) ng/mL, P<.001 (p4). | MAPPED. |
| S004 | Omega vs placebo biomarker at y2: omega index3.6%(SD1.0%) vs2.3%(SD0.8%), P<.001 (p4). | MAPPED. |
| S005 | Treatment-by-treatment interaction for primary eGFR outcome P=.42, reported not significant (p4). | MAPPED. |
| S006 | D3 composite >=40% decline/kidney failure/death: HR0.92 (0.68-1.25), P=.61; events85 vs79; rates2.5 vs2.7 per100PY (p9). | MAPPED. |
| S007 | D3 >=40% decline: HR0.97 (0.63-1.51), P=.90;42 vs38 events, rates1.6 vs1.7 (p9). | MAPPED. |
| S008 | D3 ACR doubling with final>=30mg/g: HR1.34 (1.00-1.80), P=.05;111 vs74 events, rates4.4 vs3.3 (p9). | MAPPED. |
| S009 | Omega composite: HR1.11 (0.81-1.50),P=.52;86 vs78, rates2.7 vs2.5 (p9). | MAPPED. |
| S010 | Omega >=40% decline: HR0.99 (0.64-1.54),P=.97;40 vs40, rates1.6 vs1.6 (p9). | MAPPED. |
| S011 | Omega ACR doubling: HR1.08 (0.81-1.44),P=.60;96 vs89, rates4.0 vs3.7 (p9). | MAPPED. |
| S012 | Table3 model label: Cox regression HR; P tests null HR=1; eGFR outcomes exclude4 baseline-eGFR missing, ACR outcome excludes1 baseline-ACR missing (p9). | MAPPED. |
| S013 | Fig3 D3 subgroup interaction tests: race .58; baseline ACR .36;25OHD .15;baseline eGFR .18;BMI .79;omega randomized group .42 (p8). Each displayed effect is adjusted active-placebo change in eGFR baseline-y5. | MAPPED. |
| S014 | Fig4 omega subgroup interaction tests: EPA/DHA .72;baseline ACR .70;hsCRP .73;fish intake .51;D3 randomized group .42 (p9). Same adjusted change-in-eGFR contrast. | MAPPED. |
| S015 | Sample-size relation: N1320,80% power, two-sided alpha=.05, detectable difference2.3 mL/min/1.73m2 under stated assumptions (p3). | MAPPED. |
| S016 | Model rule: treatment-by-time(y5) P used for treatment effects; two-tailed P<.05 significant; mixed model has random intercept, time categories, treatment*time, age/sex and time interactions, eGFR baseline ACR adjustment; M=20 imputation/Rubin rules (p3). | MAPPED. |
| S017 | Composite narrative repeats HRs .92(.68-1.25) and1.11(.81-1.50) as nonsignificant (p4); matches Table3 (p9). | MAPPED. |
| S018 | No statistically significant proportional-hazards violations reported for any secondary outcome (p4). | MAPPED. |
| S019 | Narrative says no significant subgroup heterogeneity and no significant correlation of biomarker change with eGFR change; no coefficients/P values printed for correlation (p4). | MAPPED; values unavailable in DOC-001 main paper. |
| S020 | The results characterize secondary endpoint analyses as exploratory because potential type-I error from multiple comparisons (p3); no multiplicity-adjusted P values reported. | MAPPED; interpretation label. |

## Mapper-only observations for later checking

- Table 2 primary CIs contain their printed point estimates and cross the null for both active-placebo y5 contrasts.
- All Table 3 hazard-ratio CIs contain their printed HRs; CIs for all displayed HRs include 1 (the D3 urine-ACR lower limit prints 1.00). These are mapping observations, not adjudications.
- No literal `P = 0`/`p = 0.000` display occurs in the mapped main-paper results. P<.001 values require ordinary compatibility checking but are not display-zero records.
## Support sources — DOC-002, DOC-003

Fresh support scope only. Provisional IDs. All inferential values below are printed source facts; planned protocol equations are definitions, not retrospective tests.

| ID | Location | Statistical relationship | Status / candidate note |
|---|---|---|---|
| S021 | DOC-002 pp.17-18 | Original protocol: multiplicative interaction ANCOVA beta4 P<.05; ACR `log(ACR4)` model and eGFR ANCOVA; no multiplicity correction. | Planned definition. |
| S022 | DOC-002 pp.19-20 | Planned power as N1500 with 20% loss and specified effect/power pairs; composite RR power .69-.76 (80%) and .65-.73 (90%). | Planned calculation. |
| S023 | DOC-002 pp.32-33 | Addendum linear mixed models, beta6 interaction P<.05; 10 imputation sets/Rubin rules; two-sided alpha .05; simulation 2,000. | Planned definition. |
| S039 | DOC-002 p.23 | Parent-trial Haybittle-Peto interim rule z=3 / P=.0027, adjusted for multiple looks. | Planned monitoring definition; no result. |
| S024 | DOC-003 pp.2-4 | Calibration multiplier 5.49/5.961, regression .006801+1.037603 pre-shift, QC correlation r=.999. | QC statistical relation; no candidate. |
| S025 | DOC-003 p.9 | eGFR complete cases D3 difference .87, 95%CI(-.83,2.58), P=.32. | CI contains null; coherent. |
| S026 | DOC-003 p.9 | eGFR complete cases omega difference .09, 95%CI(-1.61,1.80), P=.92. | CI contains null; coherent. |
| S027 | DOC-003 p.10 | Adherent eGFR D3 .89(-.74,2.52), P=.28. | CI contains null; coherent. |
| S028 | DOC-003 p.10 | Adherent eGFR omega .42(-1.22,2.06), P=.61. | CI contains null; coherent. |
| S029 | DOC-003 p.11 | Full ACR D3 ratio .99(.84,1.17), P=.90. | Ratio CI contains 1; coherent. |
| S030 | DOC-003 p.11 | Full ACR omega ratio .96(.81,1.14), P=.64. | Ratio CI contains 1; coherent. |
| S031 | DOC-003 p.12 | Available-case ACR D3 1.03(.86,1.22), P=.77; omega .93(.78,1.11),P=.44. | Both ratio CIs contain 1. |
| S032 | DOC-003 p.13 | Adherent ACR D3 1.02(.85,1.22),P=.87; omega .99(.83,1.19),P=.94. | Both ratio CIs contain 1. |
| S033 | DOC-003 p.14 | UTI-excluded ACR D3 .99(.84,1.17),P=.90; omega .98(.83,1.16),P=.80. | Both ratio CIs contain 1. |
| S034 | DOC-003 p.15 | D3 post-hoc HRs 1.03(.68,1.58),.82(.64,1.05),.82(.61,1.09),.79(.59,1.06); P .88,.12,.17,.12. | Each CI contains HR=1; coherent. |
| S035 | DOC-003 p.15 | Omega post-hoc HRs 1.07(.70,1.63),.96(.75,1.23),.89(.66,1.19),.86(.64,1.15); P .77,.77,.44,.31. | Each CI contains HR=1; coherent. |
| S036 | DOC-003 p.17 | Correlations: r=-.05 and r=-.02; no P value, N, or regression definition printed. | No mechanical inference beyond printed r. |
| S037 | DOC-003 p.18 | Vitamin-D eFigure subgroup interaction P values .89,.30,.99,.77,.69,.21,.53; effect shown as active/placebo ratio with 95%CI graphical. | All printed P>.05; participant-count-column observation separately recorded as SUPPORT-OBS-001. |
| S038 | DOC-003 p.19 | Omega eFigure subgroup interaction P values .64,.50,.79,.31,.68,.53; effect ratio/95%CI graphical. | All printed P>.05; participant-count-column observation SUPPORT-OBS-002. |

## Statistical definition notes

- eGFR table differences are from linear mixed models adjusted for age, sex, baseline urine ACR, with missing data handled by multiple imputation; positive means higher year-5 eGFR/less loss for active treatment.
- ACR table ratios are from linear mixed models adjusted for age and sex with multiple imputation. P values test differential baseline-to-year-5 change.
- eTable 10 HRs are Cox-regression post-hoc analyses; P tests HR=1. Incidence-rate differences use per-100-person-years scale and are not counts.
- No display-zero P value appears in assigned support sources, so no `DISPLAY_ZERO_NOT_CANDIDATE` record is required.
