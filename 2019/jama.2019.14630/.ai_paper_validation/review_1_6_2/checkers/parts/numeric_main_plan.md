# Numeric consistency checker — main and protocol shard

Assigned scope: DOC-001 REPORT, N001–N056; DOC-002 PLAN, N801–N820. All 76 grouped numeric/design relationships were checked; full check record: relationships/parts/numeric_main_plan.md. Main Table 2 and Table 3 numeric mean/change/contrast identities were checked through their associated S records; mixed-model contrasts are preserved as model estimates. Figure 4 proportions supply no participant counts or denominators, so no numerator/denominator is fabricated. Exact source pages were confirmed with available direct Poppler pdftotext -layout for main pp.1–4 and protocol pp.53–54; other locations were checked against the new source-linked complete maps. Existing text is a transcription aid, not a replacement source for final mechanical recheck. Compute device: CPU. No sources or reused assets were changed.

## Findings

### F-NUM-001

**Title:** Abstract completion count is the main analysis count, while the flow gives a smaller 12-month nutritional-completer population.

**Relationships:** N001, N007, N008; main analysis definition S002 and sensitivity definition S004.  
**Compared document roles:** REPORT vs REPORT within the same main article.  
**Proposed relationship type:** S_W.  
**Focus area:** A, counts and denominators / analysis-population attribution.  
**Proposed review domain:** statistical_results.

**Exact source locations and printed inputs:**

- REPORT [main PDF p.1, abstract Results](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=1): “6583 (96%) completed the 12-month follow-up and were included in the main analysis,” among 6874 randomized participants.
- REPORT [main PDF p.3, Figure 1](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=3): main analyses I3272/C3311; missing nutritional information at12months I439/C368; post hoc sensitivity analyses at12months I2833/C2943.
- REPORT [main PDF p.4, Statistical Analysis and Results](../../../../jama_saynorea_2019_oi_190106_1635377898.43062.pdf#page=4): principal analyses include randomized participants with baseline nutritional data “regardless of whether they had incomplete information at follow-up visits,” using multiple imputation; completer-only sensitivity further excludes people without nutritional information at follow-up. A total6583 were analyzed.

**Rule and calculation:** Match the completion claim to the printed completion-sensitive population before comparing exact counts. Main analysis total3272+3311=6583. Missing12-month nutritional information439+368=807. Nutritional completer total2833+2943=5776=6583−807. Exact-count recomputed interval is [5776,5776], compared with exact printed [6583,6583]; gap807, relative discrepancy807/6583=0.122589 (>0.05). Relative to randomized6874, nutritional completer fraction100×5776/6874=84.0268%, compared with printed96% interval[95.5,96.5]; gap11.4732 percentage points, relative discrepancy11.4732/96=0.119512 (>0.05). In contrast6583/6874=95.7667% does reconcile arithmetically with96% when it denotes the baseline-eligible imputed analysis population.

**Qualifying route:** Route B.

**Affected result or extracted value:** Number and proportion completing12-month follow-up for the primary dietary adherence analysis, and whether the primary result comes from observed completers or an imputed population.

**Why context does not resolve it:** The abstract attaches the completion and main-analysis descriptions to one count. The body distinguishes a6583-person imputed population from the5776-person complete-nutritional-information population, without giving a separate count of people who attended a12-month visit but supplied incomplete nutrition data. A data extractor cannot tell which definition underlies “completed” in the abstract.

**Alternatives:** Completion might mean attendance at a12-month follow-up visit, rather than availability of the nutritional information required for completer analyses; under that interpretation the807 missing nutritional records could coexist with completed visits. Alternatively, “completed” could denote inclusion in the imputed analysis. The printed package passages cited here do not state the attendance denominator or identify such a broader definition. The finding does not assume that every missing nutritional record means absence from follow-up.

**Exact human question:** What definition and observed count of12-month follow-up completion underlie the abstract's6583 (96%), and how does that count relate to the5776 nutritional completers and807 missing12-month nutritional records in Figure1?

## Excluded observations

Only apparent issues decided against emission appear below. Reconciled checks remain in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.1 abstract Results; p.4 Table1 | Abstract3406 [52%] men among6874 implies49.5490%;52% half-unit interval[51.5,52.5] yields gap1.9510 points/52=.03752≤.05. The3406 count separately equals analyzed1702+1704 men. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.4 Table1 education; p.4 Results missingness | Education703/3240=21.6975% vs21%, and902/3285=27.4581% vs28%; after printed percentage intervals the relative residuals are.00941/.00150. Nutritional missing807/6583=12.2588% vs12.2%, interval gap.00889/12.2=.000729. Consolidated pattern of small percentage discrepancies. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.5 Table2; pp.7–8 Table3 | PDQS12month crude change contrast6.9−4.4=2.5 vs model2.4; SFA12month−.9−(−.6)=−.3 vs model−.4; PUFA12month1.3−.8=.5 vs model.4; fiber6month40−16=24 vs model23; other small row contrasts similarly retained as explicit mixed-effects estimates. No crude estimator is claimed. | MODEL_VERSUS_CRUDE |
| PLAN protocol pp.44–45 nutrient targets | Printed≈2.4g sodium from100mmol sodium chloride versus chemical equivalent≈2.299g; input100 interval[99.5,100.5] gives[2.2875,2.3105]g; printed2.4 interval[2.35,2.45] gives gap.0395/2.4=.0165≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol p.54 weight-change size | Fixed-input conventional normal diagnostic≈251.2/group versus337/group is not a reproduced discrepancy under the mandatory half-unit displayed-input intervals: SD[7.5,8.5], difference[1,3] permit≈[98.1,1134.2]/group including337. Statistical reviewer separately covers method specification S807. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol pp.4,14–15,20,74–75 | Recruitment calendars,20original centers vs later3added, and original support7 vs laterA8 differ across plan versions; amendments explain center additions, and calendar comparisons do not change a planned decision rule or analysis population. | PERIPHERAL_COMPARISON |

## Coverage and limitations

76/76 assigned N relationships checked, one finding, six excluded-observation patterns. There is no quantitative-scope gap in this shard. No source-exact histogram heights, boxplot quantiles or power coordinates are printed; the complete map supplies panels, axes, direction and definitions, without invented values. The attendance-versus-nutrition-completeness alternative in F-NUM-001 remains for exact recheck and human adjudication. No C IDs or adjudication dispositions assigned.

