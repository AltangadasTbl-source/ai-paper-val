# Statistical Pass 1

## Completed scope

Fresh statistical pass 1 covered all source-backed inferential relationships across the complete supplied package:

| Direct source | Pages | Covered inferential scope |
|---|---:|---|
| DOC-001 `jama_dupuis_2024_oi_240111_1733431204.38761.pdf` | 1-11 | Main trial model definitions, all Table 2 and Table 3 estimates, intervals and P values, abstract/key-point/narrative repetitions, and Figure 2 scope. |
| DOC-002 `joi240111supp1_prod_1733431204.57929.pdf` | 1-46 | Final/original protocol and final SAP inference definitions, planned power simulations, and the printed external/background inferential statements. Blank planned result shells were checked as unpopulated shells, not observed results. |
| DOC-003 `joi240111supp2_prod_1733431204.76024.pdf` | 1-23 | eTables 6-12, eFigures 1-3, eText, including all 135 eTable 10 OR/CI/P cells and their three distinct denominator cohorts. |

The stable statistical inventory is [relationship_inventory.md](../statistics/relationship_inventory.md). It contains **57 S IDs (S001-S057)**, each marked `PASS_1_COMPLETE`.

**Explicit pass-1 relationship record:** S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057. Every enumerated ID is documented in the linked inventory and completed in this pass.

## Checks performed

For every applicable relationship, pass 1 checked:

* point-estimate containment and interval endpoint ordering;
* sign/direction against outcome scale, contrast, labels, narrative, and repeated locations;
* effect-measure and scale labels (MD, OR, RR, absolute risk difference, CI versus credible interval/region);
* exact cross-location repetitions after matching outcome, time point, population, contrast, model, and precision; and
* interval/P/test/statistic/SE compatibility only when supplied-source definitions made that comparison applicable.

No test statistic or SE was printed for the principal reported models. The sources also omit degrees of freedom, CI construction, variance estimators, covariance, multiplicity treatment, and (for eTable 10) the model fallback selected for each cell. These definitions were not inferred from convention. Where the same result used another model, transformed scale, Bayesian credible region, imputed data, or explicitly different population, it was not treated as an identity comparison.

## Raw pass-1 candidate output

**Count: 1.**

**Effect-measure label in DOC-003 eTable 10.** On DOC-003 pp. 13-15, eTable 10 labels its shared modeled-effect column `Difference (95% CI)` across documentation, any intervention, and symptom-specific intervention. On DOC-003 p. 22, eMethods says these analyses fit logistic regression to estimate an **odds ratio**. The table prints multiplicative effect values, for example 0.53 (0.28, 1.01), 17.96 (1.03, 313.1), and 5.30 (2.50, 11.24). Under the supplied-source model definition, the effect-column label conflicts with the stated effect measure. This raw candidate concerns the label/measure contradiction, not P-value precision or a reconstructed test. The coordinator should assign the stable C ID after duplicate merging.

All other completed comparisons found no independent supplied-source contradiction in a matched inferential result, endpoint order, containment, effect/scale label, direction, or repeated location.

This is discovery output only. It does not assign severity, validity, acceptance, rejection, or a correction.

## Display-zero rule

**DISPLAY_ZERO_NOT_CANDIDATE records: 0.** No printed P value equals display zero in the supplied sources. The `0.000` text on DOC-002 pp. 10, 24, and 34 is an ICC value in planned power tables, not a P value. P values printed as `<.001` were retained as bounded values; no positive tail probability was derived from them.

## Diagnostics and limitations

* No diagnostic approximation was used as a candidate rule.
* eTable 10 includes sparse cells with extreme ORs and rounded intervals. Although some interval/P combinations can look unusual under a simple Wald reconstruction, the supplied text permits mixed or fixed logistic regression depending on event counts and does not identify the per-cell fit, CI method, test statistic, SE, or variance estimator. They therefore remain documented missing definitions, not candidates.
* The supplied source identifies the primary model, contrasts, confidence level, and two-sided convention, but not enough technical detail to reproduce P values from interval widths. Bayesian credible intervals/regions and posterior probabilities were kept distinct from frequentist CIs and P values.
* Protocol/SAP inference statements and external/background evidence are included for coverage and label consistency; they are not assumed to be observed trial results.

## Pass-2 requirement

The distinct pass-2 runtime must revisit S001-S057 after receipt of the full candidate ledger and mechanical recheck facts. It must record `PASS_2_COMPLETE` for every S ID and may append any newly supported raw candidate without altering this pass-1 record.
