# Support Statistical Relationship Inventory — Temporary Keys

Temporary `US` keys are source-mapping records only. All P values, intervals, and models remain pending independent statistical checking.

| Temporary key | Source locations | Statistical definition/result relationship | Status for later passes |
|---|---|---|---|
| US001 | DOC-003 p. 6; DOC-002 p. 6 | Protocol calls for cause-specific event rates per 100 patient-years; eTable 4 reports eight-year rates and nonsurgical-minus-surgery differences with 95% bootstrap CIs (1,000 samples). | Model/interval source-grounded; compare label, direction, and arithmetic. |
| US002 | DOC-003 p. 6; DOC-002 p. 7 | Protocol calls for cumulative-incidence estimates; eTable 5 prints eight endpoints, years 2/5/8, treatment groups, percentages and 95% CIs. | Check endpoint/time/contrast and CI order. |
| US003 | DOC-003 p. 6; DOC-002 p. 9 | Fully adjusted Cox-PH HRs, 95% CIs and outcome P values: eight overall results listed in eTable 6. | Check HR-CI direction/containment; display values include <.001, not display-zero P. |
| US004 | DOC-003 p. 6; DOC-002 p. 9 | PH assumptions planned by weighted residuals; eTable 6’s final column is PH-assumption P. Values .89/.76/.63/.65/.24/.10/.46/.04 by endpoint order. | Check labels distinctly from outcome P values. |
| US005 | DOC-002 p. 8 | Primary-composite subgroup Cox models replace a continuous covariate with dichotomous subgroup plus treatment interaction; eight interaction P values .35/.93/.90/.80/.94/.53/.72/.98. | Check subgroup labels, HR/CI containment, and interaction-column identity. |
| US006 | DOC-003 p. 6; DOC-002 pp. 10,19 | Time-varying fully adjusted HRs at years 2/5/8 use a restricted cubic spline of observed follow-up interacted with treatment; eTable 7 is duplicated verbatim. | Check duplicate equality, time labels, and HR/CI containment. |
| US007 | DOC-002 p. 12 | eTable 8 uses treatment-interacted four-knot spline for metabolic/nutritional changes and two-sample proportions test for medication at each time point; intervals are 98.8% Bonferroni corrected. | Check unit, sign, CI and P label alignment. |
| US008 | DOC-002 p. 12 | Metabolic/nutritional contrasts use estimates and 98.8% CIs at four timepoints; medication contrasts use percentage-point estimates and P values. | Do not equate these P values with Cox P values. |
| US009 | DOC-002 p. 15 | Intervention cumulative incidences and 95% CIs are Kaplan-Meier estimates, surgery only. | Check CI order and surgery-only label; no nonsurgery contrast. |
| US010 | DOC-002 p. 17 | Sensitivity report: 15 datasets; five endpoint HR families stated consistently significant, and cerebrovascular/coronary/AF significant in 13/12/11. | Requires connection to Fig. 4 only; individual displayed values are not tabulated. |
| US011 | DOC-002 pp. 19-20; DOC-003 p. 7 | E-value method on risk-ratio scale for HR and closest-to-null CI limit. E-values: primary 2.15/1.92; secondary 2.62/2.11; mortality 2.81/2.13; HF 4.69/3.52; CAD 2.27/1.55; cerebrovascular 2.35/1.31; nephropathy 4.46/3.29; AF 1.90/1.21. eTable 12 comparator HRs are separate outcome-specific associations for smoking, hypertension, dyslipidemia, insulin. | Check E-value/HR/CI matched endpoint and stated scale; not a direct HR equality rule. |
| US012 | DOC-002 p. 19 | Narrative says eTable 4 displays time-varying adjusted HRs, while the immediate table is headed eTable 7 and same table occurs p. 10. | Statistical-label/cross-reference relationship; preserve exact printed comparator. |
| US013 | DOC-003 p. 6 | Five multiply imputed datasets; predictive mean matching/logistic/polytomous logistic by variable type; Rubin formula for SEs/contrasts; alpha .05 and 95% CIs; secondary analyses exploratory without multiplicity adjustment. | Protocol definition only; do not assume it verifies a particular printed analysis. |

**DISPLAY_ZERO_NOT_CANDIDATE:** No `P = 0`, `p = 0.000`, or equivalent displayed-zero P value appears in this assigned support scope. Values printed as `<.001` are threshold displays and are not a displayed-zero relationship.

**No applicable workbook-formula/cached-value relationship:** no XLS/XLSX/CSV/Office workbook is within this scope.
