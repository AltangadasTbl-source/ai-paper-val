# C012 focused independent recheck

Scope: C012 only. Existing CPU-rendered images of supplied Supplement 4 PDF pages 4, 5, 7, and 10 were inspected visually. Supplied Supplement 5 workbook XML was read directly using `unzip -p`; existing extraction was used only to locate cells. Sources and earlier artifacts were preserved.

## Exact evidence

- [Supplement 4, PDF page 4, Adjustment](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4): additional weight-model variables were selected using a similar process to the outcome-model selection, with eTable 2 identifying the selected variables.
- [Supplement 4, PDF page 5, Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5): the primary weighted analysis used a logistic regression for having at least one observed follow-up. Additional predictors were to be related at the 0.10 level to both the 3-month MCID outcome and any observed follow-up, conditional on study arm and the base adjustment variables. Predictions p_i produce weights w_i=1/p_i, subsequently rescaled and used in GEE.
- [Supplement 4, PDF page 7, eTable 2, FINAL VARIABLES SELECTED, last row](../../../joi250046supp4_prod_1755300121.15587.pdf#page=7): “Additional variables selected for inclusion in non-response weight model” lists PEG score, Depression (PHQ-8 score), Anxiety (GAD-7 score), presence of any negative social determinant of health, and education (any college vs. HS degree or less).
- [Supplement 4, PDF page 10, eTable 5](../../../joi250046supp4_prod_1755300121.15587.pdf#page=10): the displayed logistic weighting-model coefficients include “Not employed”, OR 1.49, 95% CI 1.11–2.00, P=0.008. No education coefficient is displayed. The other four additional predictors from eTable 2 are displayed: PEG score, PHQ-8, GAD-7, and “No Negative Social Determinant of Health”. The last variable uses reversed coding but still represents the listed construct. The local note states “Health care site information has been excluded”; it does not state that education coefficients were omitted.
- [Supplement 5 workbook](../../../joi250046supp5_prod_1755300121.16087.xlsx), worksheet `eTable 3`, A18 and H18:J18: A18 identifies “Not employed”; H18 is <0.001 for the primary MCID outcome, I18 is 0.0228 for overall non-response, and J18 is 0.0591 for missingness at the 3-month time point. H2:J2 supply those column definitions. H18 and I18 are compatible with the stated P<0.10 weight-selection criterion; J18 pertains to a different missingness outcome.

## Mechanical recheck fields

| Required field | C012 fact |
|---|---|
| Location found | All registered Supplement 4 locations found; corroborating workbook locations found. |
| Source value/text matched | The final weight-model list names education; the displayed fitted model names employment and has no education row. |
| Comparator matched | Both locations concern the non-response logistic weight model supporting the primary analysis, not the outcome estimation model. |
| Consistency rule applicable | A stated final predictor membership list and a fitted-model coefficient summary should identify a compatible model, or explain omitted terms, coding, or subsequent selection. |
| Calculation/logical comparison | Five additional predictors listed; four matched by construct in the fitted-model display; education not displayed; employment displayed despite not being in that final weight-model list. |
| Display-precision interval check | Not applicable to categorical predictor membership. There is no recomputed numeric discrepancy or relative discrepancy. The coefficient is transcribed for identification, not used as evidence of an estimate/interval/P conflict. |
| Necessary inputs available | Sufficient to reproduce the printed membership discrepancy. Insufficient to reconstruct actual fitted probabilities, weights, or outcome effects. |
| Exact missing inputs/definitions | Actual final weight-model design matrix/formula including education coding, explanation of omitted coefficient rows, individual covariates and outcomes, coefficients/intercept, rescaling details and analysis code needed for exact replication, and matched analyses assessing alternative memberships. |
| Source-grounded alternatives | Employment plausibly satisfied the reported selection rule, as corroborated by workbook H18/I18. The final list could be outdated, education could be omitted only from the coefficient display, a row label could refer to a different term than printed, or the fitted model could have changed. These possibilities are not established by the supplied tables. |
| Direct observation versus inferred explanation | Direct: the two printed memberships differ. Inferred and unproven: actual removal of education, substitution by employment, or a change in fitted participant weights. |
| Exact remaining human question | Which additional covariates actually entered the final non-response weight model, including education and employment, and which final formula and coefficient summary reproduce the primary weighted analysis? |

## Classification and evidence state

Both compared locations are REPORT content describing implemented analysis and fitted results within one results supplement. Primary relationship: S_W. All relationships: S_W. Review domain: statistical_results, because the discrepancy concerns statistical model specification. No PLAN comparison is necessary; the workbook corroboration does not create an additional relationship. Existing classification is retained.

Evidence state: reproduced. Determining fact: the final non-response predictor list includes education whereas the fitted weight-model summary includes employment and displays no education term. This state records the reproducible printed discrepancy, not a determination of the actual software model or a human disposition. Status: Pending Human Adjudication.

## Bounded downstream implication

The issue directly affects model identification and replication. Because predicted follow-up probabilities are inverted and rescaled before weighted GEE, a difference in the actual predictor set could change participant weights and hence RR, standard errors, confidence intervals, and derived quantities. No supplied matched analysis quantifies that change, and the displayed weight summary cannot isolate education or employment contributions. It is therefore unsupported to claim a change in statistical significance or the trial conclusion.

The OR of 1.49 describes conditional odds of having any observed follow-up for the employment term. It is neither a treatment effect nor a 49% change in analysis weight. No replacement code or numeric replacement is supplied by this recheck.
