# DOC-003 Statistical Relationship Inventory

Scope: SAP PDF pp. 1-45. These are pre-specified inferential definitions and unfilled reporting templates. No result-specific test statistic, CI, estimate, or P value was printed. Every relationship below is ready for later matched-result comparison and is not a candidate disposition.

| ID | Exact location | Statistical definition | Population/time/contrast/model/measure/scale/direction | Check status and candidate potential |
|---|---|---|---|---|
| S2001 | PDF p. 8 | Sample-size power assumption: 85% power, effect size 0.5 SD, two-sided alpha 0.05, 144 randomised; 160 with assumed 10% attrition. | Planning only; QoL continuous outcome. | No observed result to test. |
| S2002 | PDF pp. 8-9 | Superiority framework; null=no PCS difference. Interim Haybittle-Peto probability threshold <0.001. | Digoxin vs beta-blocker. | No interim result. |
| S2003 | PDF p. 9 | Group differences use two-sided 95% CIs and two-sided tests; no multiplicity adjustment. | All estimates unless stated otherwise. | Match confidence level/sidedness if results are found. |
| S2004 | PDF pp. 10-12 | ITT primary/secondary/safety analyses; standard adjusted covariates and Bisoprolol reference. Binary relative-risk route: log-binomial; if convergence fails Poisson robust SE; then unadjusted log-binomial if needed. | All planned outcomes as applicable. | No model result or convergence outcome printed. |
| S2005 | PDF pp. 18,33 | Primary 6-month PCS linear regression: outcome=6-month PCS; predictors baseline PCS, treatment, minimisation variables, age, baseline LVEF; adjusted mean difference, 95% CI, P. | ITT; Digoxin-Bisoprolol; positive favours Digoxin. | Template blank; match estimate/CI/P/model footnote later. |
| S2006 | PDF p. 19 | PCS mixed repeated-measures model: treatment, minimisation variables, age, baseline LVEF, time in days; initially constant treatment effect, test treatment*time; use time-specific estimates if interaction P<0.05; unstructured covariance. | Repeated PCS; adjusted mean difference/95% CI. | No interaction/result printed. |
| S2007 | PDF pp. 18-19,34-35 | Each listed SF-36 global/domain outcome at 6/12 months uses primary linear-regression method. | PCS/MCS/PF/RP/RE/SF/MH/EV/Pain/GHP; 0-100, higher better; Bisoprolol reference. | Blank templates. |
| S2008 | PDF pp. 19,36 | EQ-5D index and VAS at 6/12 months use primary linear model. | Index -0.285 to 1; VAS 0-100; higher better; adjusted mean difference. | Blank template. |
| S2009 | PDF pp. 19,36 | AFEQT overall at 6/12 months uses primary linear model. | 0 complete disability to 100 no disability; positive difference favours Digoxin. | Template footnote label says visual analogue score; potential measure-label check. |
| S2010 | PDF pp. 19-20,37 | LVEF at 12 months uses linear regression plus baseline MI, PCI/stent and CABG/CAPG covariates. | Continuous % LVEF; higher better; adjusted mean difference/95% CI/P. | Blank template. |
| S2011 | PDF pp. 20,37 | E/e' uses primary linear model; composite diastolic indices uses logistic regression with baseline binary category and standard covariates. | E/e' lower better; composite adjusted OR/95% CI. | p.37 blanket positive-difference/higher-is-better note conflicts with p.20 E/e' direction; potential label-direction check. |
| S2012 | PDF pp. 20,38 | Heart-rate measures use primary linear model separately at 6/12 months; 24-hour ambulatory rate has no baseline adjustment because measured once. | bpm, Digoxin vs Bisoprolol. | No estimates; p.38 placement under Baseline needs timing confirmation. |
| S2013 | PDF pp. 20,39 | Walk distance is the main six-minute-walk endpoint and uses primary linear model separately at 6/12 months. | metres; positive difference favours Digoxin. | Blank template. |
| S2014 | PDF pp. 21,40 | EHRA ordinal logistic regression: class 1 reference, baseline EHRA/treatment/sex/age/LVEF; lower OR favours Digoxin. Binary 2-class improvement logistic regression: yes outcome/reference, treatment/sex/age/LVEF; OR>1 favours Digoxin. | Separate 6/12 month analyses. | Blank template; coding/direction clear. |
| S2015 | PDF pp. 21,40 | Naturally log-transformed NT-pro-BNP uses primary linear model; exponentiated effect is geometric mean ratio. | Baseline/6/12 months, <1 favours Digoxin. | Heading/time and pg/mL versus ng/L labels require cross-template check; no result. |
| S2016 | PDF pp. 22,41-44 | Feasibility outcomes: no formal model-based analysis. Safety template specifies chi-square test for difference in patients with >=1 AE and a P-value placeholder. | Arm comparison; patients versus event counts distinct. | No P value/result. No DISPLAY_ZERO_NOT_CANDIDATE entry required. |
| S2017 | PDF pp. 22-23,45 | Primary PCS subgroup effects tested by treatment-by-subgroup interaction: sex, modified EHRA, prior beta-blocker, age, LVEF. | Forest plot reports adjusted mean difference (95% CI) and interaction P. | Blank template. |
| S2018 | PDF p. 23 | Primary PCS sensitivities: per-protocol; add baseline apical HR; exclude questionnaire outside +/-4-week window; missing outcome MI using chained equations, 50 imputations, Stata MI/regress, pooled with `mi estimate`. | 6-month PCS. | No imputed or sensitivity result. |

## Statistical-definition limitations

- The SAP specifies models and direction but not observed estimates, standard errors, test statistics, degrees of freedom, or a completed P-value display. Compatibility calculations are therefore not applicable at this source alone.
- No coherent `P = 0`, `p = 0.000`, or equivalent display-zero result occurs in this source. No display-zero candidate is created.
