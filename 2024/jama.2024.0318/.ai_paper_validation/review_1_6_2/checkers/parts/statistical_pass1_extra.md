# Statistical pass 1 extra checker

Runtime agent: /root/statistical_pass1_extra. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN.

Exact assigned disjoint scope: DOC-003 REPORT eTable3 physical p17, eTable5 physical pp19-20, eTable6 physical p21. Complete relationship inventory: statistics/parts/pass1_extra_inventory.md, S121-S222 (102 relationships). This shard covers 29 eTable3 contrasts, 48 eTable5 adverse-event tests, 25 eTable6 procedure tests. It covers no main-article, PLAN, other supplement table, figure or longitudinal-model relationship. No supplied source or reused asset was altered; no prior checker/report/candidate output, external source, browser or custom Python helper was used.

## Complete checks and self-screening

All 102 records explicitly have PASS_1_COMPLETE. All 100 printed numeric P values reconcile within the scope’s display-precision threshold with at least one stated test-family reconstruction; S139 and S140 print NA for all-zero event tables. Every count, denominator and printed percentage was retained and checked. No printed estimates, CIs, SEs, regression adjustments or margins are supplied in these three tables, so containment, endpoint order and estimate/CI/P compatibility checks cannot create a conflict here. No superiority, noninferiority, equivalence, interim, stopping, or multiplicity decision is attributed to these table rows.

Source-grounded method family: DOC-003 p6 statistical appendix and p20/p21 table footnotes state chi-squared or Fisher’s exact testing. MED is the eTable3 reference per p17 footnote a; p17 footnote b defines denominator N as observed laboratory data. Secondary outcomes are described as hypothesis generating and unadjusted for multiple testing on p5. No effect estimate was compared with a crude risk/odds ratio. The missing per-row choice, Fisher sidedness and probability-ordering convention are recorded precisely as limits; a missing convention without a conflicting printed result is not a finding. Pearson 2-by-2 and Fisher hypergeometric reconstructions are diagnostic checks supported by the stated family and repeated-row reproducibility, not imputed claims about the authors’ exact options.

Route A categories were checked before self-screening: no point estimate/interval-P conflict is possible from these count/P-only displays; no printed sign/digit slip changes a reading; all within-display percentages reconcile; no printed result fails a method reproducing the rest of its display beyond the 0.05 threshold; no planned-versus-reported outcome/analysis comparison is assigned to this shard. Repeated rows were all reviewed, including rare/zero-event rows, rather than sampled. No clinical or broad method preference is proposed.

## Findings

No findings meet the inclusion threshold in this scope. No finding ID was assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-003 REPORT p17 eTable3 hypoalbuminemia SG; p19 eTable5 diabetes-related foot ulcers, colon polyps, pneumonia and cellulitis; S147, S152, S165, S180, S181 | Consolidated apparent last-digit count-to-test diagnostic discrepancy: S147 Hypoalbuminemia SG: printed 0.60, Pearson diagnostic 0.594845193, half-unit-band gap 0.000154807, relative 0.000258011; S152 Diabetes related foot ulcers: printed 0.65, Fisher diagnostic 0.655177098, half-unit-band gap 0.000177098, relative 0.000272459; S165 Colon polyps: printed 0.46, Pearson diagnostic 0.465275185, half-unit-band gap 0.000275185, relative 0.000598229; S180 Pneumonia: printed 0.23, Pearson diagnostic 0.224655379, half-unit-band gap 0.000344621, relative 0.001498352; S181 Cellulitis: printed 0.53, Pearson diagnostic 0.535380032, half-unit-band gap 0.000380032, relative 0.000717041. All gaps are far below 0.05 after the printed P half-unit interval, and none involves a confidence interval or a contradictory stated test conclusion. | ROUNDING_OR_DISPLAY_PRECISION |

Only this apparent issue is listed; reconciled checks and absent method details without a conflict are not excluded observations. The five tiny last-digit gaps do not reverse significance at .05; no route A interval/test conflict is excluded.

## Direct-source confirmation and derivative provenance

Fresh direct Poppler 26.01.0 derivatives (CPU) are under review_1_6_2/preprocessing/: stat_extra_pages17-21-layout.txt, stat_extra_methods4-6-layout.txt, stat_extra_source17.png, stat_extra_source19.png, stat_extra_source20.png, stat_extra_source21.png. The four rendered table images were visually read fully and confirmed all source cells. The method-location extraction was read in full for the supporting table-test definitions. These derivatives are additional locators and direct-page views, not modifications of reused assets.

Commands used:

```text
pdftotext -layout -f 17 -l 21 joi240004supp2_prod_1721756962.82552.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat_extra_pages17-21-layout.txt
pdftotext -layout -f 4 -l 6 joi240004supp2_prod_1721756962.82552.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat_extra_methods4-6-layout.txt
pdftoppm -f 17 -l 17 -singlefile -scale-to 1800 -png joi240004supp2_prod_1721756962.82552.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat_extra_source17
pdftoppm -f 19 -l 19 -singlefile -scale-to 1800 -png joi240004supp2_prod_1721756962.82552.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat_extra_source19
pdftoppm -f 20 -l 20 -singlefile -scale-to 1800 -png joi240004supp2_prod_1721756962.82552.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat_extra_source20
pdftoppm -f 21 -l 21 -singlefile -scale-to 1800 -png joi240004supp2_prod_1721756962.82552.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat_extra_source21
```

## Completion and limitations

Assigned coverage 102/102 relationships; 100 numeric P checks and two explicitly no-applicable all-zero tests. Findings 0; excluded observations 1 consolidated pattern. Scientific coverage gaps: none. Missing exact per-row test choice and Fisher sidedness/probability ordering limit claims about exact software options; the source’s permitted family nonetheless reconciles every printed test under the inclusion threshold. Full numerical calculations, source locations, reference groups, counts/percentages and status are retained in the relationship inventory.

