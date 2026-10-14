# Statistical pass 1 — support-results shard

- Runtime agent: agent:/root/statistics_one_support; fresh spawn; gpt-6.1-sol; high reasoning effort.
- Exact assigned scope: S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255, S256, S257, S258, S259, S260, S261, S262, S263, S264, S265, S266, S267, S268, S269, S270, S271.
- Relationships reviewed:41/41; findings:0; excluded apparent observations:4.
- Scope: REPORT DOC-004 results supplement pp.2–6, every six sensitivity result, all42 site rows/21 outcome families, and all14 side-effect families, including all counts, blank inferential cells, printed dashes, models,95%CI, Ps and footnotes.
- Every ID has PASS_1_COMPLETE in [complete relationship inventory](../../statistics/parts/support_relationship_inventory.md). Main, PLAN and unpopulated shells are checked in the distinct assigned shard; their supplied method definitions were consulted as context here.
- Sources were freshly read through PDF-native/sorted-layout text and rendered source pages. Exact PDF links below are authoritative. Fresh derivative engine: package-local pdf_tools.py with PyMuPDF1.26.4, CPU; rendering200dpi. No fresh OCR or GPU use was required.

## Completed checks

Every printed point estimate lies within its ordered95%CI. The null1/significance.05 check agrees for all41 printed RR/CI results (six sensitivity,35 site), with no interval-versus-P conflict. Mater respiratory support RR.30(.11–.80),P.016 and Other-site hemorrhage RR1.63(1.19–2.24),P.002 exclude1 and are significant. Other-site spontaneous vaginal birth RR.91(.82–1.00),P.050 reaches1 and is nonsignificant under the source's strict P<.05 rule. All other printed RR CIs include1 with nonsignificant Ps. These reconciliations are inventory checks, not excluded observations.

All displayed count-denominator-percent triplets and Yes/No/NotDone/Missing sums within the assigned tables reconcile. eTable1 headers1634/1641 are randomized infants; outcome-specific denominators and Missing categories remain distinct. eTable3 denominators1552/1557 refer to actual treatment received, not randomized allocation;1552+1557+148=3257, consistent with the supplied main report. The two empty adjusted-model count cells, all unestimable zero-event RR dashes/blanks and all empty Ps remain explicit.

A binomial log-risk diagnostic, R=(a/n)/(b/m), s²=1/a−1/n+1/b−1/m, CI=exp(logR±1.959964s), P=2Φ(−abs(logR/s)), reproduces all35 populated site RR/CI/P rows. A likelihood-ratio interaction diagnostic with separate site baselines and a common RR under the no-interaction model reproduces all16 populated interaction Ps at printed precision. For example respiratory support is.015088 and meconium aspiration.213883, matching printed.015 and.214. These diagnostics do not assert an unprinted variance estimator, degrees of freedom, covariance, test statistic or estimator implementation. No inferential comparison uses a subgroup P as though it were an interaction P.

Fisher probability-ordering diagnostics use the hypergeometric mass Pr(X=x)=C(1552,x)C(1557,K−x)/C(3109,K), summed over masses at most the observed mass. Headache P.342964, dizziness P.062301, and reflux/dyspepsia P.624277 reproduce printed.343,.062,.624. The near-unit Ps are covered in the excluded table. No RR/CI is supplied for this safety table, so no interval-versus-P conclusion is manufactured.

The six sensitivity labels and footnotes identify GEE with twin clustering, unclustered GLM, nine versus ten components, imputation, and testing-status indicator adjustment. Planned definitions [PLAN SAP pp.12–14](../../../../joi250034supp2_prod_1750956984.11521.pdf#page=12) and [REPORT main p.4](../../../../jama_kumar_2025_oi_250034_1750956984.08518.pdf#page=4) provide the relevant analysis populations, confidence/significance and missing-pH context. No missing model detail alone yielded a finding. No superiority, noninferiority, equivalence, interim or stopping decision is asserted in these supplement result tables. Formal prospective-versus-reported comparisons and package-wide multiplicity/interim analyses belong to the separate main/PLAN shard.

## Findings

None in this assigned scope after complete pass1 self-screening. No finding ID was allocated.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [DOC-004 p.2](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=2), S231–S233, GEE sensitivity results | Apparent differences between displayed model RRs and crude count ratios, including imputed composite85/1625 versus87/1625 with GEE RR1.01, and imputed pH14/1629 versus8/1637 with GEE RR1.62. GEE with twin clustering is explicitly identified. The comparisons cannot substitute crude ratios for modeled estimates; no source says these RRs are crude. | MODEL_VERSUS_CRUDE |
| REPORT [DOC-004 p.6](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=6), S259,S265,S269, diarrhoea/vomiting/hypo-paraesthesia | Printed Fisher P.999 versus probability-ordered diagnostic P1. For exact counts the recomputed P interval is[1,1], the displayed.999 interval is[.9985,.9995], gap.0005, relative gap.0005/.999≈.0005005≤.05. No CI or significance conflict exists. Consolidated near-unit display pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4), S245,S247 interaction Ps | A Wald interaction diagnostic gives respiratory.022350 versus printed.015, and meconium.230797 versus printed.214. The footnote does not identify the test. A likelihood-ratio diagnostic gives.015088 and.213883, respectively, and reproduces the other populated interaction rows. The apparent comparison imposed the Wald test on a P column whose printed results support the alternative likelihood-ratio calculation. | NOT_REPRODUCED |
| REPORT [DOC-004 p.4](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=4), S248 cesarean-or-IVB fetal-distress heading, and [DOC-004 p.5](../../../../joi250034supp3_prod_1750956984.12018.pdf#page=5) dagger footnote | Dagger appears on the cesarean-or-IVB heading although its immediate legend describes the pH NotDone assumption. This marker does not alter a number, endpoint or model interpretation; the pH meaning is explicit in the legend and pH heading. | NOTATION_OR_TYPOGRAPHY |

## Named limitations

Exact GEE refits require individual twin outcomes and fitted covariance/variance inputs, absent from the aggregate supplement. Exact imputed-event reproduction requires twin/non-twin pooled tested event rates, fractions with no other component, and arm-specific eligible NotDone counts. Exact testing-indicator adjusted GLM reproduction requires outcome×testing-status×treatment cross-tabulations. These are named reconstruction limits, without a conflicting printed value or method statement. The ordered/contained CI, null/P, population, component-label, and within-display count checks remain complete.

Durable artifacts: statistics/parts/support_relationship_inventory.md and checkers/parts/statistical_support_pass_1.md; derivatives under preprocessing/statistics_one_support/. This runtime agent performed pass1 only and may not serve as pass2.

