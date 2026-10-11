# Canonical Inferential-Statistical Relationship Inventory

## Convention

Each record has a distinct `S` ID. Source status is explicit: `OBSERVED` is a reported result and `PROSPECTIVE` is protocol/SAP planning. Checks enabled: IC=interval containment/order; P=test/CI compatibility where the source provides a compatible rule; DIR=sign/direction/measure; XDOC=matched cross-source; POP=population/denominator/model; LAB=measure/model/scale/label. No record is an adjudication.

| Stable ID | Source; population/time/contrast/model | Printed estimate, CI, P/test, or prospective definition | Checks | Mapper provenance | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|
| S001 | DOC-001 pp.2-3; trial-wide; prospective | Two-sided P<.05, 95% CI, no multiplicity adjustment; site clustering; adjusted covariates stated | LAB,POP | MAIN-S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S002 | DOC-001 pp.2-3; trial-wide methods | Logistic binary; Fine-Gray duration; ordered-logistic DAWOS; Cox death; RD/RR marginal standardisation; chained imputation | LAB,POP | MAIN-S004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S003 | DOC-001 p.3; subgroup plan | Diagnostic/COVID/ethnicity interactions on OR scale; post-hoc severity/data collection | LAB,POP | MAIN-S005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S004 | DOC-001 pp.1,6,8; known 90-d outcome; conservative-usual | Adjusted multiply-imputed RD .7 pp (95% CI -.7,2.0), P=.28; Table 2 RR1.02(.98,1.06), OR1.04(.97,1.11) | IC,P,DIR,XDOC,POP,LAB | MAIN-S002,S008 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S005 | DOC-001 p.8; ICU survivor duration | Fine-Gray sHR1.00(.96,1.04), P=.97, available/imputed | IC,P,DIR,POP,LAB | MAIN-S009 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S006 | DOC-001 p.8; hospital survivor duration | Fine-Gray sHR .98(.94,1.02), P=.27 | IC,P,DIR,POP,LAB | MAIN-S010 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S007 | DOC-001 p.8; DAWOS 30 d | proportional OR available 1.00(.95,1.06), imputed1.01(.96,1.07), P=.64 | IC,P,DIR,XDOC,POP,LAB | MAIN-S011 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S008 | DOC-001 p.8; ICU-discharge mortality | adjusted RD .2(-1.2,1.6) available; -.1(-1.3,1.1) imputed; P=.94 | IC,P,DIR,POP,LAB | MAIN-S012 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S009 | DOC-001 p.8; hospital-discharge mortality | adjusted RD .9(-.6,2.3) available; .5(-.8,1.9) imputed; P=.46 | IC,P,DIR,POP,LAB | MAIN-S013 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S010 | DOC-001 p.8; 60-d mortality | adjusted RD1.1(-.2,2.5) available; .8(-.6,2.2) imputed; P=.25 | IC,P,DIR,POP,LAB | MAIN-S014 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S011 | DOC-001 p.8; one-year mortality, available linkage subset | adjusted RD1.0(-.7,2.6) available;3.3(-.7,7.3) imputed; P=.34 | IC,P,DIR,POP,LAB | MAIN-S015 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S012 | DOC-001 p.8; model footnote | site/stratum/COVID/splines/date adjustment; imputation and censoring rule | POP,LAB,XDOC | MAIN-S016 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S013 | DOC-001 p.9; diagnosis subgroups, 90-d mortality | HIE/sepsis/brain/none RDs and ORs; diagnosis interaction P=.67; adjusted OR-scale interaction | IC,P,DIR,POP,LAB | MAIN-S017,S020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S014 | DOC-001 p.9; COVID subgroup, 90-d mortality | COVID no/yes RDs and ORs; interaction P=.11 | IC,P,DIR,POP,LAB | MAIN-S018,S020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S015 | DOC-001 p.9; ethnicity outcome-available subset | five ethnicity RDs/ORs; interaction P=.64; outcome-specific denominators | IC,P,DIR,POP,LAB | MAIN-S019,S020 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S016 | DOC-003 p.12; one-year time-to-death, linkage-consenting population | adjusted HR1.01(.96,1.05), P=.82; 342 undated deaths interval/left censored; reverse-KM follow-up | IC,P,DIR,XDOC,POP,LAB | D3-S001; MAIN-S006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S017 | DOC-003 p.14; predicted-risk tertiles | adjusted OR 1.19(.98,1.45),1.00(.88,1.13),1.09(.96,1.23); interaction P=.18 | IC,P,DIR,POP,LAB | D3-S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S018 | DOC-003 p.14; APACHE-II tertiles | adjusted OR1.04(.91,1.20),1.06(.93,1.21),1.06(.94,1.20); interaction P=.98 | IC,P,DIR,POP,LAB | D3-S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S019 | DOC-003 p.14; PaO2/FIO2 subgroups | adjusted OR1.15(.95,1.38),1.00(.89,1.12),.98(.85,1.12),1.11(.96,1.28); interaction P=.36 | IC,P,DIR,POP,LAB | D3-S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S020 | DOC-003 p.14; data-collection subgroups | standard OR1.03(.96,1.11); enhanced random .88(.70,1.10); first-10 1.43(1.08,1.90); interaction P=.18, displayed first-10 P=.03 | IC,P,DIR,POP,LAB | D3-S002; MAIN-S007 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S021 | DOC-003 p.24; missing data / imputation | single PaO2/FIO2 imputation; logit/ordered-logit secondary imputation; stated censoring rules | POP,LAB,XDOC | D3-S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S022 | DOC-002 p.26; v1.1 prospective sample size | 34% to31.5%, 2.5 pp, two-sided alpha .05, 90% power, n16,500, 5% unavailable | POP,LAB | D2A-S001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S023 | DOC-002 pp.12-13; cited historical evidence | RR .91(.75,1.09); hyperoxia RR1.21(1.03,1.43), OR1.22(1.12,1.33); external context | IC,DIR,LAB | D2A-S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S024 | DOC-002 p.30/70-71; prospective primary mortality plan | ITT; site/strata/baseline adjustment; random effects; absolute/relative risks; later plan 37% to34.5% and N15,444/16,500 | POP,LAB,XDOC | D2B-S001; D2C-S001,S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S025 | DOC-002 pp.30,70-71; prospective secondary models | binomial/Poisson, normal, stratified Wilcoxon, KM/Cox shared frailty | POP,LAB | D2B-S002; D2C-S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S026 | DOC-002 pp.30,71; prospective subgroup/interim | prespecified interactions; Peto-Haybittle P<.001 at 4,500/10,000 | POP,LAB | D2B-S003; D2C-S004 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S027 | DOC-002 pp.31,71-72; prospective health economics | ITT mean incremental cost/QALY/NMB at 90 d, 95% CI, multilevel models, sensitivity/lifetime analyses | POP,LAB | D2B-S004; D2C-S006 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S028 | DOC-002 pp.68-70; prospective pilot rule | traffic-light green/amber/red progression rule; not an effect estimate | LAB | D2C-S005 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S029 | DOC-002 pp.88-112; SHEAP opening material | prospective clinical/economic plan only; no observed inferential result | POP,LAB | D2D-S001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S030 | DOC-002 p.87-88; version/outcome constraint | 30-d ordinal DAWOS added in protocol v1.8 while SHEAP title links v1.5 | XDOC,LAB | D2D-S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S031 | DOC-002 p.120; SAP global convention | two-sided P<.05, 95% CI, no multiplicity adjustment; interim P<.001 separately | LAB,XDOC | D2E-S001 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S032 | DOC-002 pp.119,124,126; SAP primary estimand | 90-d all-cause death; ITT; adjusted site/Mega-ROX/calendar-time; 95% CI/P; no futility rule | POP,LAB,XDOC | D2E-S002 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S033 | DOC-002 p.121; SAP analysis population | initial assignment, known-primary-outcome inclusion despite adherence; re-randomisation >=90 d | POP,LAB | D2E-S003 | PASS_1_COMPLETE | PASS_2_COMPLETE |
| S034 | DOC-002 pp.127-131; SAP subgroup/economic plans | planned heterogeneity and sensitivity/lifetime analysis, no observed estimates | POP,LAB | D2E-S004 | PASS_1_COMPLETE | PASS_2_COMPLETE |

All entries are currently `Pass 1: PASS_1_COMPLETE` and `Pass 2: PASS_2_COMPLETE`. No candidate ID, validity finding, severity, or disposition is made here.
