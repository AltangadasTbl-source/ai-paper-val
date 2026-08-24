# Support inferential-statistical relationship inventory (provisional US IDs)

All IDs are provisional support-lane statistical maps, not candidate findings. Reported P values, CIs, effect measures, model labels, populations, time points, and contrasts are retained exactly enough for later full-pass checking.

## Protocol/SAP definitions

| ID | Source and reported definition | Statistical relationship / match key |
|---|---|---|
| US001 | DOC-002 p. 17 sample-size plan: baseline composite 80%, 5% improvement, 80% power, 5% significance level, ICC .02, 40 clusters, approximately 4,800 patients. | Design inference parameters; no supplied formula, sidedness, variance, or resulting test statistic. `sample-size-80-5-80power-ICC002` |
| US002 | DOC-002 p. 18: χ2 for categorical comparisons; Student t or Mann-Whitney U for continuous comparisons. | Univariate testing rule; selection depends on distribution. `SAP-univariate-tests` |
| US003 | DOC-002 pp. 18-19: GEE accounting for within-hospital correlation; qualitative variables population-average OR and quantitative variables mean difference, each 95% CI; composite opportunity-level binary outcome. | Planned clustered-analysis framework and effect-measure labels. `SAP-GEE-OR-MD-95CI` |
| US004 | DOC-002 p. 19: Kaplan-Meier curves and proportional-hazards Cox models for clinical vascular events and mortality at discharge and 3/6/12 months; sensitivity analysis includes contraindicated patients in overall-population denominator. | Planned survival model/timepoints and sensitivity population. `SAP-Cox-3-6-12m` |

## Baseline-survey and loss-to-mRS comparisons

| ID | Source location, population/contrast, printed statistic | Relationship / match key |
|---|---|---|
| US005 | DOC-003 p. 2 eAppendix: intervention vs control baseline composite 80.2% vs 79.5%; narrative: no statistically significant differences for composite. | No exact P, CI, test, or model is supplied. `baseline-survey-composite-and-nine-PM` |
| US006 | DOC-003 p. 5 eTable 2: observed one-year mRS vs loss, age median (IQR) 65 (56-74) vs 64 (56-74), P=.81. | Test/model unspecified. `eTable2-age` |
| US007 | Same table: male 63.2% vs 64.2%, P=.61. | Test/model unspecified. `eTable2-male` |
| US008 | Same: ischemic stroke 28.8% vs 29.5%, P=.68. | Test/model unspecified. `eTable2-ischemic-stroke-history` |
| US009 | Same: diabetes 22.5% vs 23.0%, P=.75. | Test/model unspecified. `eTable2-diabetes` |
| US010 | Same: hypertension 64.6% vs 63.2%, P=.44. | Test/model unspecified. `eTable2-hypertension` |
| US011 | Same: dyslipidemia 7.2% vs 7.3%, P=.94. | Test/model unspecified. `eTable2-dyslipidemia` |
| US012 | Same: CAD/previous MI 13.0% vs 11.4%, P=.21. | Test/model unspecified. `eTable2-CAD-MI` |
| US013 | Same: atrial fibrillation 5.1% vs 5.3%, P=.79. | Test/model unspecified. `eTable2-AF` |
| US014 | Same: ever smoking 44.0% vs 44.7%, P=.71. | Test/model unspecified. `eTable2-smoking` |
| US015 | Same: admission NIHSS median (IQR) 3 (2-6) vs 3 (2-6), P=.99; NIHSS scale footnote range 0-42. | Test/model unspecified. `eTable2-NIHSS` |

## eTable 3: individual new vascular events

The contrast is intervention vs control. Columns separately report adjusted absolute percentage-point difference (95% CI) and its P value, then adjusted HR (95% CI) and its P value. Adjustment: patient age, gender, ischemic-stroke history, hypertension, diabetes, hyperlipidemia, AF, CAD/previous MI, smoking, NIHSS; hospital grade, region, stroke unit, teaching status, neurological-ward beds (DOC-003 p. 7 footnote). No model/test pairing for the absolute-difference P column is stated in this table.

| ID | Printed result | Statistical relationship / match key |
|---|---|---|
| US016 | DOC-003 p. 6, 3m ischemic stroke: difference -.57% (95% CI -1.91 to .76), P=.40; HR .89 (95% CI .59-1.36), P=.59. | Two adjusted inferential displays, same time/event contrast. `eTable3-3m-ischemic-stroke` |
| US017 | 3m hemorrhagic stroke: -.35% (-.92 to .22), P=.23; HR .85 (.40-1.83), P=.68. | `eTable3-3m-hemorrhagic-stroke` |
| US018 | 3m myocardial infarction: -.10% (-.36 to .17), P=.48; HR .58 (.13-2.67), P=.48. | `eTable3-3m-MI` |
| US019 | 3m vascular death: -1.43% (-2.33 to -.54), P=.001; HR .62 (.42-.92), P=.02. | `eTable3-3m-vascular-death` |
| US020 | 6m ischemic stroke: -1.40% (-2.82 to .02), P=.05; HR .72 (.53-.99), P=.04. | `eTable3-6m-ischemic-stroke` |
| US021 | 6m hemorrhagic stroke: -.25% (-.80 to .30), P=.38; HR .92 (.46-1.82), P=.80. | `eTable3-6m-hemorrhagic-stroke` |
| US022 | 6m myocardial infarction: -.03% (-.35 to .29), P=.86; HR .78 (.27-2.24), P=.64. | `eTable3-6m-MI` |
| US023 | 6m vascular death: -1.06% (-2.08 to -.04), P=.04; HR .78 (.56-1.10), P=.16. | `eTable3-6m-vascular-death` |
| US024 | 12m ischemic stroke: -1.84% (-3.45 to -.23), P=.03; HR .73 (.57-.93), P=.01. | `eTable3-12m-ischemic-stroke` |
| US025 | 12m hemorrhagic stroke: -.08% (-.71 to .55), P=.80; HR 1.02 (.55-1.88), P=.96. | `eTable3-12m-hemorrhagic-stroke` |
| US026 | 12m myocardial infarction: -.13% (-.46 to .21), P=.45; HR .71 (.30-1.67), P=.43. | `eTable3-12m-MI` |
| US027 | 12m vascular death: -1.94% (-3.26 to -.62), P=.004; HR .71 (.54-.94), P=.02. | `eTable3-12m-vascular-death` |

## eTable 4: overall-population sensitivity analysis

The contrast is intervention vs control. For every row, eTable 4 prints absolute difference in percentage points (95% CI) and P, then adjusted ORPA (population-average odds ratio; 95% CI) and P. The footnote specifies adjustment for age, gender, ischemic-stroke history, hypertension, diabetes, hyperlipidemia, AF, CAD/previous MI, smoking, admission NIHSS, hospital grade, region, stroke unit, teaching status, and neurological-ward beds.

| ID | Printed result | Statistical relationship / match key |
|---|---|---|
| US028 | DOC-003 p. 8 composite mean (SD): 85.3 (15.2) vs 80.9 (17.1); difference 4.20% (1.77-6.63), P<.001; ORPA 1.36 (1.11-1.67), P=.003. | Cluster-level composite and adjusted population-average OR. `eTable4-overall-composite` |
| US029 | IV rt-PA: difference 5.81% (-4.57-16.19), P=.27; ORPA 2.60 (.76-8.87), P=.13. | `eTable4-IV-rtPA` |
| US030 | Early antithrombotics: 2.68% (.48-4.87), P=.02; ORPA 1.73 (1.05-2.87), P=.03. | `eTable4-early-antithrombotics` |
| US031 | Dysphagia screening: 1.72% (-1.95-5.40), P=.36; ORPA 2.37 (.69-8.18), P=.17. | `eTable4-dysphagia` |
| US032 | DVT prophylaxis: 14.79% (3.16-26.42), P=.01; ORPA 2.09 (.95-4.62), P=.07. | `eTable4-DVT` |
| US033 | Discharge antithrombotics: 5.32% (.44-10.20), P=.03; ORPA 1.89 (.99-3.64), P=.05. | `eTable4-discharge-antithrombotics` |
| US034 | AF anticoagulation: 12.90% (-3.51-29.3), P=.12; ORPA 1.78 (.61-5.14), P=.29. | `eTable4-AF-anticoagulation` |
| US035 | Lipid lowering: 2.46% (-2.03-6.95), P=.28; ORPA 1.17 (.61-2.24), P=.63. | `eTable4-lipid-lowering` |
| US036 | Antihypertensive medication: 6.32% (-.58-13.21), P=.07; ORPA 1.47 (.97-2.23), P=.07. | `eTable4-antihypertensive` |
| US037 | Antidiabetic medication: 6.16% (1.70-10.62), P=.007; ORPA 1.59 (1.11-2.23), P=.01. | `eTable4-antidiabetic` |

## Scope note

No display-zero P value occurs in the assigned support sources. All listed P values are retained regardless of nominal threshold; no statistical candidate diagnosis has been performed in this artifact.
