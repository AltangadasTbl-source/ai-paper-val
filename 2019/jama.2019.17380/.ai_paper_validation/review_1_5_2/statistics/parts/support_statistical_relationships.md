# Support Statistical Relationship Inventory

Fresh support scope only. Provisional IDs. All inferential values below are printed source facts; planned protocol equations are definitions, not retrospective tests.

| ID | Location | Statistical relationship | Status / candidate note |
|---|---|---|---|
| SUPPORT-S001 | DOC-002 pp.17-18 | Original protocol: multiplicative interaction ANCOVA beta4 P<.05; ACR `log(ACR4)` model and eGFR ANCOVA; no multiplicity correction. | Planned definition. |
| SUPPORT-S002 | DOC-002 pp.19-20 | Planned power as N1500 with 20% loss and specified effect/power pairs; composite RR power .69-.76 (80%) and .65-.73 (90%). | Planned calculation. |
| SUPPORT-S003 | DOC-002 pp.32-33 | Addendum linear mixed models, beta6 interaction P<.05; 10 imputation sets/Rubin rules; two-sided alpha .05; simulation 2,000. | Planned definition. |
| SUPPORT-S019 | DOC-002 p.23 | Parent-trial Haybittle-Peto interim rule z=3 / P=.0027, adjusted for multiple looks. | Planned monitoring definition; no result. |
| SUPPORT-S004 | DOC-003 pp.2-4 | Calibration multiplier 5.49/5.961, regression .006801+1.037603 pre-shift, QC correlation r=.999. | QC statistical relation; no candidate. |
| SUPPORT-S005 | DOC-003 p.9 | eGFR complete cases D3 difference .87, 95%CI(-.83,2.58), P=.32. | CI contains null; coherent. |
| SUPPORT-S006 | DOC-003 p.9 | eGFR complete cases omega difference .09, 95%CI(-1.61,1.80), P=.92. | CI contains null; coherent. |
| SUPPORT-S007 | DOC-003 p.10 | Adherent eGFR D3 .89(-.74,2.52), P=.28. | CI contains null; coherent. |
| SUPPORT-S008 | DOC-003 p.10 | Adherent eGFR omega .42(-1.22,2.06), P=.61. | CI contains null; coherent. |
| SUPPORT-S009 | DOC-003 p.11 | Full ACR D3 ratio .99(.84,1.17), P=.90. | Ratio CI contains 1; coherent. |
| SUPPORT-S010 | DOC-003 p.11 | Full ACR omega ratio .96(.81,1.14), P=.64. | Ratio CI contains 1; coherent. |
| SUPPORT-S011 | DOC-003 p.12 | Available-case ACR D3 1.03(.86,1.22), P=.77; omega .93(.78,1.11),P=.44. | Both ratio CIs contain 1. |
| SUPPORT-S012 | DOC-003 p.13 | Adherent ACR D3 1.02(.85,1.22),P=.87; omega .99(.83,1.19),P=.94. | Both ratio CIs contain 1. |
| SUPPORT-S013 | DOC-003 p.14 | UTI-excluded ACR D3 .99(.84,1.17),P=.90; omega .98(.83,1.16),P=.80. | Both ratio CIs contain 1. |
| SUPPORT-S014 | DOC-003 p.15 | D3 post-hoc HRs 1.03(.68,1.58),.82(.64,1.05),.82(.61,1.09),.79(.59,1.06); P .88,.12,.17,.12. | Each CI contains HR=1; coherent. |
| SUPPORT-S015 | DOC-003 p.15 | Omega post-hoc HRs 1.07(.70,1.63),.96(.75,1.23),.89(.66,1.19),.86(.64,1.15); P .77,.77,.44,.31. | Each CI contains HR=1; coherent. |
| SUPPORT-S016 | DOC-003 p.17 | Correlations: r=-.05 and r=-.02; no P value, N, or regression definition printed. | No mechanical inference beyond printed r. |
| SUPPORT-S017 | DOC-003 p.18 | Vitamin-D eFigure subgroup interaction P values .89,.30,.99,.77,.69,.21,.53; effect shown as active/placebo ratio with 95%CI graphical. | All printed P>.05; participant-count-column observation separately recorded as SUPPORT-OBS-001. |
| SUPPORT-S018 | DOC-003 p.19 | Omega eFigure subgroup interaction P values .64,.50,.79,.31,.68,.53; effect ratio/95%CI graphical. | All printed P>.05; participant-count-column observation SUPPORT-OBS-002. |

## Statistical definition notes

- eGFR table differences are from linear mixed models adjusted for age, sex, baseline urine ACR, with missing data handled by multiple imputation; positive means higher year-5 eGFR/less loss for active treatment.
- ACR table ratios are from linear mixed models adjusted for age and sex with multiple imputation. P values test differential baseline-to-year-5 change.
- eTable 10 HRs are Cox-regression post-hoc analyses; P tests HR=1. Incidence-rate differences use per-100-person-years scale and are not counts.
- No display-zero P value appears in assigned support sources, so no `DISPLAY_ZERO_NOT_CANDIDATE` record is required.
