# DOC-001 statistical relationship inventory (temporary MS keys)

All HRs are adjusted Cox-model estimates for surgery versus matched nonsurgical patients; all Table 2 CI/P values use the table's stated fully adjusted model. `DISPLAY_ZERO_NOT_CANDIDATE` is included only for actual coherent display zeroes; none was printed in DOC-001.

| Key | Printed statistical relationship | Context, model, and source | Mapping status |
|---|---|---|---|
| MS001 | Primary MACE HR 0.61 (95% CI 0.55-0.69), P<.001. | Fully adjusted Cox; 8-y primary extended MACE; PDF p. 1 abstract, p. 4 Results, p. 7 Table 2/Figure 2A. | Mapped. |
| MS002 | Secondary 3-component MACE HR 0.62 (0.53-0.72), P<.001. | Fully adjusted Cox; 8-y secondary composite; PDF p. 4 Results, p. 7 Table 2/Figure 2B. | Mapped. |
| MS003 | All-cause mortality HR 0.59 (0.48-0.72), P<.001. | Fully adjusted Cox; 8-y; PDF p. 1 abstract, p. 4 Results, p. 7 Table 2, p. 8 Figure 3A. | Mapped. |
| MS004 | Heart failure HR 0.38 (0.30-0.49), P<.001. | Fully adjusted Cox; baseline heart-failure cases excluded from that outcome risk set; PDF p. 7 Table 2, p. 8 Figure 3B. | Mapped. |
| MS005 | Coronary artery disease HR 0.69 (0.54-0.87), P=.002. | Fully adjusted Cox; outcome-specific baseline exclusions; PDF p. 7 Table 2, p. 8 Figure 3C. | Mapped. |
| MS006 | Cerebrovascular disease HR 0.67 (0.48-0.94), P=.02. | Fully adjusted Cox; outcome-specific baseline exclusions; PDF p. 7 Table 2, p. 8 Figure 3D. | Mapped. |
| MS007 | Nephropathy HR 0.40 (0.31-0.52), P<.001. | Fully adjusted Cox; outcome-specific baseline exclusions; PDF p. 7 Table 2, p. 8 Figure 3E. | Mapped. |
| MS008 | Atrial fibrillation HR 0.78 (0.62-0.97), P=.03. | Fully adjusted Cox; outcome-specific baseline exclusions; PDF p. 7 Table 2, p. 8 Figure 3F. | Mapped; proportional-hazards assumption exception is reported on p. 6, with time-varying HRs deferred to Supplement 1. |
| MS009 | Primary 8-y ARD 16.9% (13.1-20.4); secondary 10.6% (7.5-13.6); mortality 7.8% (5.1-10.2). | 95% bootstrap CI, 1,000 samples; control minus surgery; PDF p. 7 Table 2 footnote. | Mapped. |
| MS010 | Individual-endpoint ARDs: HF 12.9% (10.4-15.1), CAD 4.2% (1.9-6.8), CVD 1.8% (-0.03 to 3.4), nephropathy 11.1% (8.8-13.6), AF 6.5% (4.4-8.7). | 95% bootstrap CI, 1,000 samples; PDF p. 7 Table 2. | Mapped. |
| MS011 | Mean weight-reduction difference 20.3 kg (20.1-20.6); Figure 4 percent-weight-loss difference 14.7% (14.5-14.9), P<.001. | Flexible regression with treatment-interacted 4-knot spline; 8 years; PDF pp. 4, 7, 9. | Mapped. |
| MS012 | HbA1c change difference 1.1 percentage points (1.0-1.2), P<.001. | Same longitudinal spline context; PDF p. 7 Results and p. 9 Figure 4B. | Mapped. |
| MS013 | Figure 5: P<.001 for noninsulin diabetes medication, renin-angiotensin inhibitor, other antihypertensive, lipid-lowering medication, and aspirin; P=.008 for insulin. | Figure caption says Fisher exact test comparing 8-y proportions; the article's Methods calls the longitudinal medication comparison a two-sample proportions test. Exact proportions and n are deferred to Supplement 1. PDF p. 10. | Mapped; cross-source contextual handoff required. |
| MS014 | No primary-outcome interaction heterogeneity reported for sex, age, BMI, HbA1c, eGFR, insulin, sulfonylurea, or lipid-lowering medication. | Interaction term separately added to fully adjusted Cox model; values cited to Supplement 1 eFigure 1. PDF p. 4. | Mapped; no direct main-paper interaction estimates. |
| MS015 | Proportional-hazards assumption reported satisfied for primary/secondary composites and individual outcomes except atrial fibrillation. | Weighted-residual test described on pp. 3-4; detailed P values in Supplement 1 eTable 6 and time-varying AF HRs in eTable 7. PDF p. 6. | Mapped; no direct main-paper test values. |
| MS016 | Sensitivity analysis: five random control-index assignments x 1:1, 1:5, 1:10 matching = 15 data sets; HR/95% CI generated for all outcomes, with narrative conclusion that differences were negligible. | Fully adjusted Cox; PDF pp. 4, 8-9; detailed estimates in Supplement 1 eFigure 4. | Mapped; no direct numerical HR panel. |
| MS017 | Baseline imputation: five imputed data sets; predictive mean matching numeric, logistic binary, polytomous logistic categorical; Rubin-formula SEs. | Methods, PDF p. 4. | Mapped model/statistic context. |
| MS018 | Significance threshold .05, two-sided; Table 2 secondary-endpoint findings stated exploratory because of multiple comparisons. | Methods, PDF p. 4. | Mapped inferential context. |

No P-value display is printed as `P = 0`, `p = 0.000`, or equivalent in this main article; therefore no `DISPLAY_ZERO_NOT_CANDIDATE` record applies.
