# Support Statistical Relationship Inventory (Provisional IDs)

Provisional IDs `US001` onward are statistical/inferential relationships; coordinator assigns canonical S IDs. This maps rather than adjudicates compatibility. P values printed as `<0.001` are finite-precision displays, not candidates solely for display format.

| ID | Direct evidence | Statistical definition / results assigned | Reproducible check boundary |
|---|---|---|---|
| US001 | DOC-002 p.19; DOC-003 p.11 | Original protocol sample-size basis: 397/arm, VFD means 23/24, common SD 5, 80% power, two-sided α=.05; 20% inflation to 476/arm. | Compare sample size only under the named t-test/SD/effect assumptions. |
| US002 | DOC-002 p.33 | Protocol primary planned Cox regression, p=.05, 95% confidence levels, ITT and per-protocol. | Planned analysis, not a reported result. |
| US003 | DOC-002 pp.33-35 | Protocol secondary t/Mann-Whitney, chi-square/Fisher, proportional hazards; ICER ratio and nonparametric-bootstrap CI; PSA 10,000 Monte Carlo; cost missingness >10% imputation. | Requires matching endpoint/analysis population/model. |
| US004 | DOC-003 pp.11-13 | SAP: normality visual + D’Agostino-Pearson; two-sided α=.05, no multiplicity adjustment; VFD Student t test/mean difference; Kaplan-Meier/log-rank liberation. | Test/estimate checks only for named paired result. |
| US005 | DOC-003 p.13 | Mortality: 28/90d unadjusted Cox HR/95% CI; ICU/hospital RR/95% CI/Wald likelihood-ratio approximation and chi-square; LOS selected GLM. | Do not interchange HR/RR or models. |
| US006 | DOC-003 pp.13-15 | Per-protocol exclusions; nine subgroup interaction GLMs; exploratory zero-inflated GLM/GLMM, mediation derivations. | Subgroups require interaction P, not within-subgroup P alone. |
| US007 | DOC-003 pp.21-22 | Amendment comparison: primary Cox changed to t/mean difference; outcome and subgroup-plan additions/changes, including Gaussian rather than zero-inflated subgroup model due to CLT. | Cross-document planned-versus-paper identity only; not a result contradiction by itself. |
| US008 | DOC-004 p.5/eTable1 | 13 rows × 4 between-arm P comparisons: continuous medians(IQR) or stated count/total(%); P cells include <.001, .99, .45, .14, etc. | P has no named exact table-test; check only direct compatible count/percentage, interval/order, and matched results. |
| US009 | DOC-004 p.6/eTable2 | 3 ventilation-mode strata × 7 rows × 4 timepoints, each printed P; exact values in fresh layout evidence PDF p.6. | Mode/time/measure must match before comparison. |
| US010 | DOC-004 p.7/eTable3 | 3 mode strata × 6 rows × 4 timepoints, each printed P or `---` for two equal-zero event comparisons; exact values in fresh layout evidence PDF p.7. | `---` is missing/not-applicable P display; not P=0. |
| US011 | DOC-004 p.8/eTable4 | 30 co-intervention comparisons, including exact P=1.00, NA for double-zero HFOV/ECCO2R; categorical/continuous formats defined. | `P=1.00` is ordinary rounded display; NA is not a test. |
| US012 | DOC-004 p.9/eTable5 | Nine subgroup interaction relationships: group means±SD, low-minus-intermediate mean difference 95% CI, one interaction P per modifier. | Check CI contains point estimate, endpoint order, sign against group means (rounding aware), and interaction label. |
| US013 | DOC-004 p.10/eFigure1 | Cumulative VFD proportion curves; no P/test printed. | Graphical only; match arm/axis/time scale. |
| US014 | DOC-004 pp.11-13/eFigures2-4 | Distribution figures; no estimate, CI, test, or P printed. | No numerical statistical calculation available. |
| US015 | DOC-005 p.1 | No applicable statistical relationship. | Documented no-applicable scope. |
