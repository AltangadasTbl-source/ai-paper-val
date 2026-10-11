# Statistical relationship inventory — pass 2 supplementary shard 03

Runtime agent: /root/statistical_pass2_extra_a. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Exact scope: S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140, S141, S142, S143, S144, S145, S146.

The following preserves all original assigned pass-1 records and printed inputs, then adds an explicit independent pass-2 check for each S ID. Complete assigned packet, current ledger, screen, exact-source recheck and all 53 exclusions were read. Every assigned source cell and footnote was visually reread in the current direct-source Poppler 26.01.0 rendering preprocessing/stat_extra_source17.png. Method source text: preprocessing/stat_extra_methods4-6-layout.txt, DOC-003 REPORT pp4–6. Compute device: CPU. No source or shared artifact was modified. Existing source-linked diagnostic arithmetic is reused; its unreported software selection/convention is not inferred.

## Preserved original source/statistical definitions and calculation provenance


The supplied source is [DOC-003](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), REPORT by content. Direct Poppler layout and freshly rendered source pages were read; the support mapper transcription is a locator. Native direct extraction covers physical pp17-21 and the supporting method definitions on pp4-6. Source authority is the rendered PDF. All count, denominator, percent, P-value and reference-group cells on the four assigned table pages were visually confirmed.

DOC-003 [p6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6) states that adverse events and study outcomes were summarized as percentages and compared using chi-squared or Fisher’s exact tests; [p5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=5) states secondary outcomes are hypothesis generating without multiple-testing adjustment. eTable5 footnote b on p20 and eTable6 footnote b on p21 repeat the chi-squared/Fisher family. eTable3 footnote a gives MED as comparison/reference and footnote b defines N as participants with observed data. No odds ratios, coefficients, CIs, standard errors, or test statistics are printed in these three tables. No regression/longitudinal adjustment is attributed to these table tests; no adjusted-versus-crude comparison is performed. Printed tests belong to through-12-year nutritional abnormalities, adverse events and procedures, respectively.

## Calculation and precision rules used for every record

For MED events a among n and comparison-group events b among m, the diagnostic non-continuity-corrected Pearson statistic is (n+m)[a(m-b)-(n-a)b]^2/[nm(a+b)(n+m-a-b)]. The reported-family diagnostic P is its chi-square(1) survival probability. Degrees of freedom 1 is a mathematical consequence of each reconstructed 2-by-2 table, not an inferred regression degree of freedom. The compatible Fisher diagnostic is the fixed-margin hypergeometric sum over tables no more probable than the observed table, with floating-point equality tolerance 1e-10 on log probabilities. Fisher sidedness and probability-ordering convention are not separately stated by the authors: this sum is a clearly labeled diagnostic permitted-family reconstruction that reproduces numerous rows, not an assertion about the authors’ exact software option. The Pearson tail was calculated in JavaScript using an erfc approximation with absolute numerical accuracy better than 1.5e-7; hypergeometric probabilities were evaluated by log-factorial sums. No continuity correction or effect model is assumed to be the actual author method. Both diagnostic P values are retained, and compatibility with at least one stated test family is sufficient to avoid an invented method conflict.

Counts represent integer participants and events: their half-unit rounding bands contain the printed integer as their only possible discrete value. Every observed percentage is recomputed as 100n/N and allowed its half-unit printed rounding band. Every numeric P value is allowed its own half-unit band; the remaining gap divided by printed P is recorded. Tiny last-digit gaps in 5 rows are below the scope’s 0.05 relative-discrepancy threshold. No interval-versus-P conflict exists because no intervals are printed here, and no effect-estimate/test conflict is inferred from such last-digit count-to-P diagnostics. Two all-zero eTable3 contrasts print NA; Pearson has a zero expected-event margin, and the absence of a numeric test is explicitly tracked.

Point-estimate containment, CI endpoint order, interval-versus-P agreement, coefficient sign, superiority, noninferiority, equivalence, multiplicity decision, interim and stopping checks are not applicable to these count/P-only tables unless a corresponding claim is supplied; none is supplied in this scope. Direction is retained as comparison-group frequency relative to MED; no printed narrative effect claim conflicts with the table. No sample-size calculation is printed in this scope. This prevents inventing absent model, covariance, estimand, sidedness or margin definitions.




## Updated assigned records

### S121

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); SURG 35/147 (23.8%); P 0.04. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, SURG 23.809523810%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, SURG 112. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 4.314395993, P 0.037791055; probability-ordering Fisher diagnostic P 0.041816556. COMPATIBLE: Pearson diagnostic 0.037791055 versus printed-P band [0.035, 0.045]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Anemia SURG 35/147 vs MED 11/87: P .04, Pearson diagnostic .037791055 lies in [.035,.045]. Higher surgical frequency and its anemia-specific observed-data denominators reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S122

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); RYGB 25/78 (32.1%); P 0.003. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, RYGB 32.051282051%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, RYGB 53. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 9.081329379, P 0.002582461; probability-ordering Fisher diagnostic P 0.004211109. COMPATIBLE: Pearson diagnostic 0.002582461 versus printed-P band [0.0025, 0.0035]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Anemia RYGB 25/78 vs MED 11/87: P .003, diagnostic .002582461 lies in [.0025,.0035]. Higher RYGB frequency and its own observed denominator reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S123

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); SG 8/36 (22.2%); P 0.18. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, SG 22.222222222%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, SG 28. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.788705850, P 0.181084051; probability-ordering Fisher diagnostic P 0.271461858. COMPATIBLE: Pearson diagnostic 0.181084051 versus printed-P band [0.175, 0.185]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Anemia SG 8/36 vs MED 11/87: P .18, diagnostic .181084051 lies in [.175,.185]. Higher SG frequency does not imply statistical significance.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S124

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); AGB 2/33 (6.1%); P 0.30. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, AGB 6.060606061%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, AGB 31. Direction: AGB observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.073357838, P 0.300188266; probability-ordering Fisher diagnostic P 0.511151944. COMPATIBLE: Pearson diagnostic 0.300188266 versus printed-P band [0.295, 0.305]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Anemia AGB 2/33 vs MED 11/87: P .30, diagnostic .300188266 lies in [.295,.305]. Lower AGB frequency; subgroup events 25+8+2=35 and N 78+36+33=147 equal SURG.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S125

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); SURG 48/151 (31.8%); P 0.01. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, SURG 31.788079470%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, SURG 103. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 6.225208994, P 0.012594432; probability-ordering Fisher diagnostic P 0.014704633. COMPATIBLE: Pearson diagnostic 0.012594432 versus printed-P band [0.005, 0.015]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Low iron SURG 48/151 vs MED 15/88: P .01, diagnostic .012594432 lies in [.005,.015]. Higher SURG frequency and observed-data denominators reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S126

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); RYGB 30/81 (37.0%); P 0.003. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, RYGB 37.037037037%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, RYGB 51. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 8.628087551, P 0.003310326; probability-ordering Fisher diagnostic P 0.005012322. COMPATIBLE: Pearson diagnostic 0.003310326 versus printed-P band [0.0025, 0.0035]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Low iron RYGB 30/81 vs MED 15/88: P .003, diagnostic .003310326 lies in [.0025,.0035]. Higher RYGB frequency; MED remains the exact reference.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S127

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); SG 10/37 (27.0%); P 0.20. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, SG 27.027027027%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, SG 27. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.622005528, P 0.202812509; probability-ordering Fisher diagnostic P 0.225724674. COMPATIBLE: Pearson diagnostic 0.202812509 versus printed-P band [0.195, 0.205]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Low iron SG 10/37 vs MED 15/88: P .20, diagnostic .202812509 lies in [.195,.205]. Higher SG frequency and nonsignificant printed P are compatible.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S128

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); AGB 8/33 (24.2%); P 0.37. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, AGB 24.242424242%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, AGB 25. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.807471902, P 0.368868681; probability-ordering Fisher diagnostic P 0.436495804. COMPATIBLE: Pearson diagnostic 0.368868681 versus printed-P band [0.365, 0.375]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Low iron AGB 8/33 vs MED 15/88: P .37, diagnostic .368868681 lies in [.365,.375]. Higher AGB frequency; 30+10+8=48 and N 81+37+33=151 reconcile to SURG.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S129

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); SURG 20/151 (13.2%); P 0.34. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, SURG 13.245033113%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, SURG 131. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.927632488, P 0.335478869; probability-ordering Fisher diagnostic P 0.407330607. COMPATIBLE: Pearson diagnostic 0.335478869 versus printed-P band [0.335, 0.345]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. B12 SURG 20/151 vs MED 8/88: P .34, diagnostic .335478869 lies in [.335,.345]. Higher SURG frequency; exact printed abnormality definition preserved.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S130

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); RYGB 15/81 (18.5%); P 0.07. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, RYGB 18.518518519%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, RYGB 66. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 3.188429861, P 0.074161112; probability-ordering Fisher diagnostic P 0.114593728. COMPATIBLE: Pearson diagnostic 0.074161112 versus printed-P band [0.065, 0.075]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. B12 RYGB 15/81 vs MED 8/88: P .07, diagnostic .074161112 lies in [.065,.075]. Higher RYGB frequency; no interval-based significance conflict is possible from absent intervals.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S131

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); SG 4/37 (10.8%); P 0.77. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, SG 10.810810811%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, SG 33. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.088785487, P 0.765727009; probability-ordering Fisher diagnostic P 0.747987710. COMPATIBLE: Pearson diagnostic 0.765727009 versus printed-P band [0.765, 0.775]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. B12 SG 4/37 vs MED 8/88: P .77, diagnostic .765727009 lies in [.765,.775]. Higher SG frequency and supplied test family reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S132

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); AGB 1/33 (3.0%); P 0.26. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, AGB 3.030303030%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, AGB 32. Direction: AGB observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.280423280, P 0.257820453; probability-ordering Fisher diagnostic P 0.441552612. COMPATIBLE: Pearson diagnostic 0.257820453 versus printed-P band [0.255, 0.265]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. B12 AGB 1/33 vs MED 8/88: P .26, diagnostic .257820453 lies in [.255,.265]. Lower AGB frequency; 15+4+1=20 events equal SURG.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S133

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); SURG 35/151 (23.2%); P 0.61. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, SURG 23.178807947%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, SURG 116. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.264616435, P 0.606966175; probability-ordering Fisher diagnostic P 0.640492177. COMPATIBLE: Pearson diagnostic 0.606966175 versus printed-P band [0.605, 0.615]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Vitamin D SURG 35/151 vs MED 23/88: P .61, diagnostic .606966175 lies in [.605,.615]. Lower SURG frequency is consistent with the display.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S134

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); RYGB 22/81 (27.2%); P 0.88. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, RYGB 27.160493827%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, RYGB 59. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.022642821, P 0.880389589; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.880389589 versus printed-P band [0.875, 0.885]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Vitamin D RYGB 22/81 vs MED 23/88: P .88, diagnostic .880389589 lies in [.875,.885]. Higher RYGB frequency can coexist with lower pooled SURG frequency.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S135

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); SG 2/37 (5.4%); P 0.008. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, SG 5.405405405%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, SG 35. Direction: SG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 6.996698403, P 0.008166102; probability-ordering Fisher diagnostic P 0.007064727. COMPATIBLE: Pearson diagnostic 0.008166102 versus printed-P band [0.0075, 0.0085]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Vitamin D SG 2/37 vs MED 23/88: P .008, diagnostic .008166102 lies in [.0075,.0085]. Lower SG frequency and significant printed test reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S136

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); AGB 11/33 (33.3%); P 0.43. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, AGB 33.333333333%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, AGB 22. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.615294681, P 0.432801079; probability-ordering Fisher diagnostic P 0.497518310. COMPATIBLE: Pearson diagnostic 0.432801079 versus printed-P band [0.425, 0.435]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Vitamin D AGB 11/33 vs MED 23/88: P .43, diagnostic .432801079 lies in [.425,.435]. Higher AGB frequency; 22+2+11=35 events equal SURG and subgroup N total is 151.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S137

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); SURG 1/151 (0.7%); P 0.44. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 0.662251656%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SURG 150. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.585230119, P 0.444269420; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.444269420 versus printed-P band [0.435, 0.445]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Hypocalcemia SURG 1/151 vs MED 0/88: P .44, diagnostic .444269420 lies in [.435,.445]. Higher SURG frequency; no preference for a sparse-data test is imposed.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S138

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); RYGB 1/81 (1.2%); P 0.30. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, RYGB 1.234567901%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, RYGB 80. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.092886537, P 0.295832583; probability-ordering Fisher diagnostic P 0.479289941. COMPATIBLE: Pearson diagnostic 0.295832583 versus printed-P band [0.295, 0.305]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Hypocalcemia RYGB 1/81 vs MED 0/88: P .30, diagnostic .295832583 lies in [.295,.305]. Higher RYGB frequency, count/percent and test reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S139

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); SG 0/37 (0%); P NA. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SG 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SG 37. Direction: SG observed frequency is equal than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square NA, P NA; probability-ordering Fisher diagnostic P 1.000000000. NO_APPLICABLE_NUMERIC_TEST: both groups have zero events; printed NA corresponds to a degenerate Pearson event margin.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Hypocalcemia SG 0/37 vs MED 0/88: printed P NA, both frequencies zero. Pearson event margin is degenerate; diagnostic Fisher P=1 does not compel a numeric reported test.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. No numeric printed P is available for a rounding-gap comparison; NA was checked explicitly. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S140

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); AGB 0/33 (0%); P NA. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, AGB 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, AGB 33. Direction: AGB observed frequency is equal than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square NA, P NA; probability-ordering Fisher diagnostic P 1.000000000. NO_APPLICABLE_NUMERIC_TEST: both groups have zero events; printed NA corresponds to a degenerate Pearson event margin.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Hypocalcemia AGB 0/33 vs MED 0/88: printed P NA, both frequencies zero. Pearson event margin is degenerate; subgroup events 1+0+0=1 equal SURG. NA is not a display-zero P.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. No numeric printed P is available for a rounding-gap comparison; NA was checked explicitly. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S141

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); SURG 66/151 (43.7%); P 0.10. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, SURG 43.708609272%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, SURG 85. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.684829071, P 0.101308072; probability-ordering Fisher diagnostic P 0.131498882. COMPATIBLE: Pearson diagnostic 0.101308072 versus printed-P band [0.095, 0.105]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. PTH SURG 66/151 vs MED 29/88: P .10, diagnostic .101308072 lies in [.095,.105]. Higher SURG frequency; printed threshold and denominators preserved.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S142

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); RYGB 41/81 (50.6%); P 0.02. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, RYGB 50.617283951%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, RYGB 40. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 5.422970465, P 0.019873476; probability-ordering Fisher diagnostic P 0.028345057. COMPATIBLE: Pearson diagnostic 0.019873476 versus printed-P band [0.015, 0.025]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. PTH RYGB 41/81 vs MED 29/88: P .02, diagnostic .019873476 lies in [.015,.025]. Higher RYGB frequency; no unreported multiplicity convention is imposed.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S143

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); SG 12/37 (32.4%); P 0.95. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, SG 32.432432432%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, SG 25. Direction: SG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.003221516, P 0.954737513; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.954737513 versus printed-P band [0.945, 0.955]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. PTH SG 12/37 vs MED 29/88: P .95, diagnostic .954737513 lies in [.945,.955]. Slightly lower SG frequency and near-one P reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S144

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); AGB 13/33 (39.4%); P 0.51. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, AGB 39.393939394%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, AGB 20. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.439132510, P 0.507541324; probability-ordering Fisher diagnostic P 0.526305175. COMPATIBLE: Pearson diagnostic 0.507541324 versus printed-P band [0.505, 0.515]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. PTH AGB 13/33 vs MED 29/88: P .51, diagnostic .507541324 lies in [.505,.515]. Higher AGB frequency; 41+12+13=66 and subgroup N total 151 reconcile to SURG.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S145

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypoalbuminemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Albumin <3.5 g/dL.
- **All printed values:** MED 9/88 (10.2%); SURG 23/151 (15.2%); P 0.27. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.227272727%, SURG 15.231788079%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 79, SURG 128. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.200773924, P 0.273167137; probability-ordering Fisher diagnostic P 0.327675833. COMPATIBLE: Pearson diagnostic 0.273167137 versus printed-P band [0.265, 0.275]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.


- **Pass 2:** PASS_2_COMPLETE. Hypoalbuminemia SURG 23/151 vs MED 9/88: P .27, diagnostic .273167137 lies in [.265,.275]. Higher SURG frequency; adjacent SG/AGB counts 5/4 corroborate 14+5+4=23 without adding owned relationships.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

### S146

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypoalbuminemia, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Albumin <3.5 g/dL.
- **All printed values:** MED 9/88 (10.2%); RYGB 14/81 (17.3%); P 0.18. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.227272727%, RYGB 17.283950617%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 79, RYGB 67. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.786381827, P 0.181367753; probability-ordering Fisher diagnostic P 0.261337315. COMPATIBLE: Pearson diagnostic 0.181367753 versus printed-P band [0.175, 0.185]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.



- **Pass 2:** PASS_2_COMPLETE. Hypoalbuminemia RYGB 14/81 vs MED 9/88: P .18, diagnostic .181367753 lies in [.175,.185]. Higher RYGB frequency and observed-data denominators reconcile.
- **Pass-2 count/precision and source implications:** Both event counts do not exceed their exact observed-data denominators; percentages reproduce within their printed half-unit intervals, gap zero. The reused Pearson diagnostic lies in the printed P half-unit band; gap zero and relative discrepancy zero. Group, time, reference and quantity identity match the source; no fitted model result is substituted for the count-test row.
- **Pass-2 estimate/test/method limitations:** No CI, fitted effect estimate, SE or test statistic is supplied, so point containment, interval order, interval-P compatibility and SE reproduction are not applicable. Exact per-row author test choice, Fisher sidedness/probability ordering and CMH strata/stratum counts are not supplied and are not inferred. No noninferiority/equivalence, multiplicity-adjusted conclusion, interim/stopping claim or sample-size calculation is printed for this row.
- **Pass-2 screening and recheck linkage:** The current screen and exact-source recheck already preserve F-XS-010/F-ST1-008 as one planned vascular/safety test-mapping issue; successful aggregate count-test diagnostics do not resolve that missing plan-to-result mapping. It is not re-emitted or removed. No new qualifying finding or new excluded apparent observation arises in this relationship.

## Shard closure

26 original PASS_1_COMPLETE records preserved; 26 explicit PASS_2_COMPLETE records; 24 numeric P comparisons reconcile and two zero-event comparisons explicitly retain NA. Zero new findings; zero new excluded observations; no assigned scientific coverage gap. Full pass-2 checker: checkers/parts/statistical_pass2_03.md. All current stable candidates remain Pending Human Adjudication.
