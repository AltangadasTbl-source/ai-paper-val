# Statistical pass 1 extra relationship inventory

Runtime agent: /root/statistical_pass1_extra. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Assigned disjoint scope: DOC-003 REPORT eTable3 (PDF p17), eTable5 (PDF pp19-20), eTable6 (PDF p21). This part has 102 relationships, S121-S222: 29 nutritional-abnormality contrasts (27 printed numeric P values and two NA), 48 adverse-event tests, and 25 procedure tests. No other scientific units are assigned here.

## Source and statistical definitions

The supplied source is [DOC-003](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), REPORT by content. Direct Poppler layout and freshly rendered source pages were read; the support mapper transcription is a locator. Native direct extraction covers physical pp17-21 and the supporting method definitions on pp4-6. Source authority is the rendered PDF. All count, denominator, percent, P-value and reference-group cells on the four assigned table pages were visually confirmed.

DOC-003 [p6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6) states that adverse events and study outcomes were summarized as percentages and compared using chi-squared or Fisher’s exact tests; [p5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=5) states secondary outcomes are hypothesis generating without multiple-testing adjustment. eTable5 footnote b on p20 and eTable6 footnote b on p21 repeat the chi-squared/Fisher family. eTable3 footnote a gives MED as comparison/reference and footnote b defines N as participants with observed data. No odds ratios, coefficients, CIs, standard errors, or test statistics are printed in these three tables. No regression/longitudinal adjustment is attributed to these table tests; no adjusted-versus-crude comparison is performed. Printed tests belong to through-12-year nutritional abnormalities, adverse events and procedures, respectively.

## Calculation and precision rules used for every record

For MED events a among n and comparison-group events b among m, the diagnostic non-continuity-corrected Pearson statistic is (n+m)[a(m-b)-(n-a)b]^2/[nm(a+b)(n+m-a-b)]. The reported-family diagnostic P is its chi-square(1) survival probability. Degrees of freedom 1 is a mathematical consequence of each reconstructed 2-by-2 table, not an inferred regression degree of freedom. The compatible Fisher diagnostic is the fixed-margin hypergeometric sum over tables no more probable than the observed table, with floating-point equality tolerance 1e-10 on log probabilities. Fisher sidedness and probability-ordering convention are not separately stated by the authors: this sum is a clearly labeled diagnostic permitted-family reconstruction that reproduces numerous rows, not an assertion about the authors’ exact software option. The Pearson tail was calculated in JavaScript using an erfc approximation with absolute numerical accuracy better than 1.5e-7; hypergeometric probabilities were evaluated by log-factorial sums. No continuity correction or effect model is assumed to be the actual author method. Both diagnostic P values are retained, and compatibility with at least one stated test family is sufficient to avoid an invented method conflict.

Counts represent integer participants and events: their half-unit rounding bands contain the printed integer as their only possible discrete value. Every observed percentage is recomputed as 100n/N and allowed its half-unit printed rounding band. Every numeric P value is allowed its own half-unit band; the remaining gap divided by printed P is recorded. Tiny last-digit gaps in 5 rows are below the scope’s 0.05 relative-discrepancy threshold. No interval-versus-P conflict exists because no intervals are printed here, and no effect-estimate/test conflict is inferred from such last-digit count-to-P diagnostics. Two all-zero eTable3 contrasts print NA; Pearson has a zero expected-event margin, and the absence of a numeric test is explicitly tracked.

Point-estimate containment, CI endpoint order, interval-versus-P agreement, coefficient sign, superiority, noninferiority, equivalence, multiplicity decision, interim and stopping checks are not applicable to these count/P-only tables unless a corresponding claim is supplied; none is supplied in this scope. Direction is retained as comparison-group frequency relative to MED; no printed narrative effect claim conflicts with the table. No sample-size calculation is printed in this scope. This prevents inventing absent model, covariance, estimand, sidedness or margin definitions.

### S121

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); SURG 35/147 (23.8%); P 0.04. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, SURG 23.809523810%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, SURG 112. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 4.314395993, P 0.037791055; probability-ordering Fisher diagnostic P 0.041816556. COMPATIBLE: Pearson diagnostic 0.037791055 versus printed-P band [0.035, 0.045]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S122

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); RYGB 25/78 (32.1%); P 0.003. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, RYGB 32.051282051%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, RYGB 53. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 9.081329379, P 0.002582461; probability-ordering Fisher diagnostic P 0.004211109. COMPATIBLE: Pearson diagnostic 0.002582461 versus printed-P band [0.0025, 0.0035]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S123

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); SG 8/36 (22.2%); P 0.18. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, SG 22.222222222%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, SG 28. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.788705850, P 0.181084051; probability-ordering Fisher diagnostic P 0.271461858. COMPATIBLE: Pearson diagnostic 0.181084051 versus printed-P band [0.175, 0.185]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S124

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Anemia, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Hemoglobin <11.5 g/dL.
- **All printed values:** MED 11/87 (12.6%); AGB 2/33 (6.1%); P 0.30. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.643678161%, AGB 6.060606061%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 76, AGB 31. Direction: AGB observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.073357838, P 0.300188266; probability-ordering Fisher diagnostic P 0.511151944. COMPATIBLE: Pearson diagnostic 0.300188266 versus printed-P band [0.295, 0.305]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S125

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); SURG 48/151 (31.8%); P 0.01. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, SURG 31.788079470%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, SURG 103. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 6.225208994, P 0.012594432; probability-ordering Fisher diagnostic P 0.014704633. COMPATIBLE: Pearson diagnostic 0.012594432 versus printed-P band [0.005, 0.015]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S126

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); RYGB 30/81 (37.0%); P 0.003. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, RYGB 37.037037037%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, RYGB 51. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 8.628087551, P 0.003310326; probability-ordering Fisher diagnostic P 0.005012322. COMPATIBLE: Pearson diagnostic 0.003310326 versus printed-P band [0.0025, 0.0035]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S127

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); SG 10/37 (27.0%); P 0.20. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, SG 27.027027027%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, SG 27. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.622005528, P 0.202812509; probability-ordering Fisher diagnostic P 0.225724674. COMPATIBLE: Pearson diagnostic 0.202812509 versus printed-P band [0.195, 0.205]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S128

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Low iron, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Iron <59 µg/dL or <6.6 µmol/L.
- **All printed values:** MED 15/88 (17.0%); AGB 8/33 (24.2%); P 0.37. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 17.045454545%, AGB 24.242424242%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 73, AGB 25. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.807471902, P 0.368868681; probability-ordering Fisher diagnostic P 0.436495804. COMPATIBLE: Pearson diagnostic 0.368868681 versus printed-P band [0.365, 0.375]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S129

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); SURG 20/151 (13.2%); P 0.34. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, SURG 13.245033113%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, SURG 131. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.927632488, P 0.335478869; probability-ordering Fisher diagnostic P 0.407330607. COMPATIBLE: Pearson diagnostic 0.335478869 versus printed-P band [0.335, 0.345]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S130

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); RYGB 15/81 (18.5%); P 0.07. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, RYGB 18.518518519%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, RYGB 66. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 3.188429861, P 0.074161112; probability-ordering Fisher diagnostic P 0.114593728. COMPATIBLE: Pearson diagnostic 0.074161112 versus printed-P band [0.065, 0.075]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S131

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); SG 4/37 (10.8%); P 0.77. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, SG 10.810810811%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, SG 33. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.088785487, P 0.765727009; probability-ordering Fisher diagnostic P 0.747987710. COMPATIBLE: Pearson diagnostic 0.765727009 versus printed-P band [0.765, 0.775]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S132

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin B12 deficiency, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Vitamin B12 <230 pg/mL.
- **All printed values:** MED 8/88 (9.1%); AGB 1/33 (3.0%); P 0.26. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.090909091%, AGB 3.030303030%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 80, AGB 32. Direction: AGB observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.280423280, P 0.257820453; probability-ordering Fisher diagnostic P 0.441552612. COMPATIBLE: Pearson diagnostic 0.257820453 versus printed-P band [0.255, 0.265]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S133

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); SURG 35/151 (23.2%); P 0.61. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, SURG 23.178807947%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, SURG 116. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.264616435, P 0.606966175; probability-ordering Fisher diagnostic P 0.640492177. COMPATIBLE: Pearson diagnostic 0.606966175 versus printed-P band [0.605, 0.615]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S134

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); RYGB 22/81 (27.2%); P 0.88. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, RYGB 27.160493827%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, RYGB 59. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.022642821, P 0.880389589; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.880389589 versus printed-P band [0.875, 0.885]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S135

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); SG 2/37 (5.4%); P 0.008. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, SG 5.405405405%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, SG 35. Direction: SG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 6.996698403, P 0.008166102; probability-ordering Fisher diagnostic P 0.007064727. COMPATIBLE: Pearson diagnostic 0.008166102 versus printed-P band [0.0075, 0.0085]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S136

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Vitamin D deficiency, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Vitamin D2 (1,25 Dihydroxy) ≤20 ng/mL.
- **All printed values:** MED 23/88 (26.1%); AGB 11/33 (33.3%); P 0.43. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 26.136363636%, AGB 33.333333333%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 65, AGB 22. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.615294681, P 0.432801079; probability-ordering Fisher diagnostic P 0.497518310. COMPATIBLE: Pearson diagnostic 0.432801079 versus printed-P band [0.425, 0.435]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S137

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); SURG 1/151 (0.7%); P 0.44. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 0.662251656%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SURG 150. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.585230119, P 0.444269420; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.444269420 versus printed-P band [0.435, 0.445]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S138

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); RYGB 1/81 (1.2%); P 0.30. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, RYGB 1.234567901%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, RYGB 80. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.092886537, P 0.295832583; probability-ordering Fisher diagnostic P 0.479289941. COMPATIBLE: Pearson diagnostic 0.295832583 versus printed-P band [0.295, 0.305]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S139

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); SG 0/37 (0%); P NA. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SG 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SG 37. Direction: SG observed frequency is equal than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square NA, P NA; probability-ordering Fisher diagnostic P 1.000000000. NO_APPLICABLE_NUMERIC_TEST: both groups have zero events; printed NA corresponds to a degenerate Pearson event margin.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S140

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypocalcemia, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Calcium <8.4 mg/dL.
- **All printed values:** MED 0/88 (0%); AGB 0/33 (0%); P NA. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, AGB 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, AGB 33. Direction: AGB observed frequency is equal than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square NA, P NA; probability-ordering Fisher diagnostic P 1.000000000. NO_APPLICABLE_NUMERIC_TEST: both groups have zero events; printed NA corresponds to a degenerate Pearson event margin.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S141

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); SURG 66/151 (43.7%); P 0.10. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, SURG 43.708609272%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, SURG 85. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.684829071, P 0.101308072; probability-ordering Fisher diagnostic P 0.131498882. COMPATIBLE: Pearson diagnostic 0.101308072 versus printed-P band [0.095, 0.105]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S142

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); RYGB 41/81 (50.6%); P 0.02. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, RYGB 50.617283951%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, RYGB 40. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 5.422970465, P 0.019873476; probability-ordering Fisher diagnostic P 0.028345057. COMPATIBLE: Pearson diagnostic 0.019873476 versus printed-P band [0.015, 0.025]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S143

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); SG 12/37 (32.4%); P 0.95. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, SG 32.432432432%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, SG 25. Direction: SG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.003221516, P 0.954737513; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.954737513 versus printed-P band [0.945, 0.955]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S144

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Elevated PTH, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: PTH (intact) >65 pg/mL.
- **All printed values:** MED 29/88 (33.0%); AGB 13/33 (39.4%); P 0.51. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 32.954545455%, AGB 39.393939394%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 59, AGB 20. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.439132510, P 0.507541324; probability-ordering Fisher diagnostic P 0.526305175. COMPATIBLE: Pearson diagnostic 0.507541324 versus printed-P band [0.505, 0.515]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S145

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypoalbuminemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Albumin <3.5 g/dL.
- **All printed values:** MED 9/88 (10.2%); SURG 23/151 (15.2%); P 0.27. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.227272727%, SURG 15.231788079%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 79, SURG 128. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.200773924, P 0.273167137; probability-ordering Fisher diagnostic P 0.327675833. COMPATIBLE: Pearson diagnostic 0.273167137 versus printed-P band [0.265, 0.275]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S146

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypoalbuminemia, RYGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; RYGB versus MED; MED reference. Abnormality definition: Albumin <3.5 g/dL.
- **All printed values:** MED 9/88 (10.2%); RYGB 14/81 (17.3%); P 0.18. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.227272727%, RYGB 17.283950617%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 79, RYGB 67. Direction: RYGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.786381827, P 0.181367753; probability-ordering Fisher diagnostic P 0.261337315. COMPATIBLE: Pearson diagnostic 0.181367753 versus printed-P band [0.175, 0.185]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S147

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypoalbuminemia, SG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SG versus MED; MED reference. Abnormality definition: Albumin <3.5 g/dL.
- **All printed values:** MED 9/88 (10.2%); SG 5/37 (13.5%); P 0.60. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.227272727%, SG 13.513513514%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 79, SG 32. Direction: SG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.282840866, P 0.594845193; probability-ordering Fisher diagnostic P 0.756643663. COMPATIBLE: Pearson diagnostic 0.594845193 versus printed-P band [0.595, 0.605]; interval gap 0.000154807, relative discrepancy 0.000258011 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; shared last-digit diagnostic observation is recorded once in the checker’s Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S148

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Hypoalbuminemia, AGB row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; AGB versus MED; MED reference. Abnormality definition: Albumin <3.5 g/dL.
- **All printed values:** MED 9/88 (10.2%); AGB 4/33 (12.1%); P 0.76. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.227272727%, AGB 12.121212121%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 79, AGB 29. Direction: AGB observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.089773267, P 0.764465734; probability-ordering Fisher diagnostic P 0.749040570. COMPATIBLE: Pearson diagnostic 0.764465734 versus printed-P band [0.755, 0.765]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S149

- **Location and document role:** DOC-003 REPORT, PDF p17, eTable3, Severe hypoalbuminemia, SURG row versus MED row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17).
- **Population/time/contrast/reference:** through 12 years; participants with observed laboratory data; SURG versus MED; MED reference. Abnormality definition: Albumin <2.8 g/dL.
- **All printed values:** MED 1/88 (1.1%); SURG 0/151 (0%); P 0.19. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.136363636%, SURG 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 87, SURG 151. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.723118793, P 0.189292216; probability-ordering Fisher diagnostic P 0.368200837. COMPATIBLE: Pearson diagnostic 0.189292216 versus printed-P band [0.185, 0.195]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S150

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Chest pain, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 10/96 (10.4%); SURG 15/166 (9.0%); P 0.71. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.416666667%, SURG 9.036144578%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 86, SURG 151. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.134300917, P 0.714013849; probability-ordering Fisher diagnostic P 0.827670301. COMPATIBLE: Pearson diagnostic 0.714013849 versus printed-P band [0.705, 0.715]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S151

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Hypertension (new or severe exacerbation), MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 6/166 (3.6%); P 0.71. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 160. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.481701412, P 0.487652519; probability-ordering Fisher diagnostic P 0.714305860. COMPATIBLE: Fisher diagnostic 0.714305860 versus printed-P band [0.705, 0.715]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S152

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Diabetes related foot ulcers, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 4/166 (2.4%); P 0.65. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 2.409638554%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 162. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.608039551, P 0.435526782; probability-ordering Fisher diagnostic P 0.655177098. COMPATIBLE: Fisher diagnostic 0.655177098 versus printed-P band [0.645, 0.655]; interval gap 0.000177098, relative discrepancy 0.000272459 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; shared last-digit diagnostic observation is recorded once in the checker’s Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S153

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Tachycardia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 3/96 (3.1%); SURG 3/166 (1.8%); P 0.49. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 3.125000000%, SURG 1.807228916%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 93, SURG 163. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.472029720, P 0.492054745; probability-ordering Fisher diagnostic P 0.671948640. COMPATIBLE: Pearson diagnostic 0.492054745 versus printed-P band [0.485, 0.495]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S154

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Hypotension, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 4/96 (4.2%); SURG 2/166 (1.2%); P 0.20. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 4.166666667%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 92, SURG 164. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.384595674, P 0.122536626; probability-ordering Fisher diagnostic P 0.195939091. COMPATIBLE: Fisher diagnostic 0.195939091 versus printed-P band [0.195, 0.205]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S155

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Sleep apnea (new or severe exacerbation), MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 2/166 (1.2%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.014303675, P 0.904801538; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S156

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Carotid vascular disease, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 1/166 (0.6%); P 0.56. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 165. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.178487438, P 0.277664218; probability-ordering Fisher diagnostic P 0.556320489. COMPATIBLE: Fisher diagnostic 0.556320489 versus printed-P band [0.555, 0.565]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S157

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Nausea/vomiting, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 15/96 (15.6%); SURG 43/166 (25.9%); P 0.054. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 15.625000000%, SURG 25.903614458%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 81, SURG 123. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 3.728134775, P 0.053502973; probability-ordering Fisher diagnostic P 0.063882422. COMPATIBLE: Pearson diagnostic 0.053502973 versus printed-P band [0.0535, 0.0545]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S158

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Abdominal pain, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 10/96 (10.4%); SURG 37/166 (22.3%); P 0.02. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.416666667%, SURG 22.289156627%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 86, SURG 129. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 5.824087841, P 0.015808156; probability-ordering Fisher diagnostic P 0.018823791. COMPATIBLE: Pearson diagnostic 0.015808156 versus printed-P band [0.015, 0.025]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S159

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Gastroesophageal reflux disease, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 10/96 (10.4%); SURG 29/166 (17.5%); P 0.12. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.416666667%, SURG 17.469879518%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 86, SURG 137. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.388279345, P 0.122248151; probability-ordering Fisher diagnostic P 0.150224049. COMPATIBLE: Pearson diagnostic 0.122248151 versus printed-P band [0.115, 0.125]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S160

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Diarrhea, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 7/96 (7.3%); SURG 20/166 (12.0%); P 0.22. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 7.291666667%, SURG 12.048192771%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 89, SURG 146. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.488773929, P 0.222406923; probability-ordering Fisher diagnostic P 0.292601143. COMPATIBLE: Pearson diagnostic 0.222406923 versus printed-P band [0.215, 0.225]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S161

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Constipation, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 10/96 (10.4%); SURG 17/166 (10.2%); P 0.96. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 10.416666667%, SURG 10.240963855%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 86, SURG 149. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.002031451, P 0.964050089; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.964050089 versus printed-P band [0.955, 0.965]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S162

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Dysphagia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 12/166 (7.2%); P 0.005. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 7.228915663%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 154. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 7.272867470, P 0.007000494; probability-ordering Fisher diagnostic P 0.004600394. COMPATIBLE: Fisher diagnostic 0.004600394 versus printed-P band [0.0045, 0.0055]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S163

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Hiatal hernia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 7/166 (4.2%); P 0.49. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 4.216867470%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 159. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.834673785, P 0.360924479; probability-ordering Fisher diagnostic P 0.493005380. COMPATIBLE: Fisher diagnostic 0.493005380 versus printed-P band [0.485, 0.495]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S164

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Dumping syndrome, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 8/166 (4.8%); P 0.03. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 4.819277108%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 158. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 4.772222749, P 0.028922360; probability-ordering Fisher diagnostic P 0.028645084. COMPATIBLE: Pearson diagnostic 0.028922360 versus printed-P band [0.025, 0.035]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S165

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Colon polyps, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 6/96 (6.2%); SURG 7/166 (4.2%); P 0.46. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 6.250000000%, SURG 4.216867470%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 90, SURG 159. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.533174403, P 0.465275185; probability-ordering Fisher diagnostic P 0.557528520. COMPATIBLE: Pearson diagnostic 0.465275185 versus printed-P band [0.455, 0.465]; interval gap 0.000275185, relative discrepancy 0.000598229 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; shared last-digit diagnostic observation is recorded once in the checker’s Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S166

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Gastrointestinal stricture, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 4/166 (2.4%); P 0.30. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 2.409638554%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 162. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.349117400, P 0.125354002; probability-ordering Fisher diagnostic P 0.299934260. COMPATIBLE: Fisher diagnostic 0.299934260 versus printed-P band [0.295, 0.305]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S167

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Hematochezia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 3/166 (1.8%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 1.807228916%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 163. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.237116587, P 0.626296480; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S168

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Colitis, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 3/166 (1.8%); P 0.30. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.807228916%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 163. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.755035586, P 0.185245071; probability-ordering Fisher diagnostic P 0.300868650. COMPATIBLE: Fisher diagnostic 0.300868650 versus printed-P band [0.295, 0.305]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S169

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Gastric prolapse, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S170

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Gastroparesis, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 4/96 (4.2%); SURG 0/166 (0.0%); P 0.02. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 4.166666667%, SURG 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 92, SURG 166. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 7.023901809, P 0.008042963; probability-ordering Fisher diagnostic P 0.017313734. COMPATIBLE: Fisher diagnostic 0.017313734 versus printed-P band [0.015, 0.025]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S171

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Vertigo/dizziness, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 9/96 (9.4%); SURG 27/166 (16.3%); P 0.12. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.375000000%, SURG 16.265060241%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 87, SURG 139. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.436215548, P 0.118561981; probability-ordering Fisher diagnostic P 0.138284749. COMPATIBLE: Pearson diagnostic 0.118561981 versus printed-P band [0.115, 0.125]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S172

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Depression, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 14/96 (14.6%); SURG 24/166 (14.5%); P 0.98. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 14.583333333%, SURG 14.457831325%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 82, SURG 142. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.000772592, P 0.977825119; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.977825119 versus printed-P band [0.975, 0.985]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S173

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Concussion/contusion/head injury, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 13/166 (7.8%); P 0.058. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 7.831325301%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 153. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 3.723271494, P 0.053659003; probability-ordering Fisher diagnostic P 0.058118926. COMPATIBLE: Fisher diagnostic 0.058118926 versus printed-P band [0.0575, 0.0585]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S174

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Neuropathy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 7/96 (7.3%); SURG 11/166 (6.6%); P 0.84. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 7.291666667%, SURG 6.626506024%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 89, SURG 155. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.042060203, P 0.837505113; probability-ordering Fisher diagnostic P 0.806074299. COMPATIBLE: Pearson diagnostic 0.837505113 versus printed-P band [0.835, 0.845]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S175

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Memory loss/cognitive dysfunction, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 3/96 (3.1%); SURG 6/166 (3.6%); P 0.83. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 3.125000000%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 93, SURG 160. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.043928679, P 0.833986425; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.833986425 versus printed-P band [0.825, 0.835]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S176

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Cataracts, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 12/96 (12.5%); SURG 20/166 (12.0%); P 0.91. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 12.500000000%, SURG 12.048192771%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 84, SURG 146. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.011580016, P 0.914304578; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.914304578 versus printed-P band [0.905, 0.915]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S177

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Blurred or double vision, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 7/96 (7.3%); SURG 11/166 (6.6%); P 0.84. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 7.291666667%, SURG 6.626506024%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 89, SURG 155. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.042060203, P 0.837505113; probability-ordering Fisher diagnostic P 0.806074299. COMPATIBLE: Pearson diagnostic 0.837505113 versus printed-P band [0.835, 0.845]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S178

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Glaucoma, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 5/96 (5.2%); SURG 4/166 (2.4%); P 0.23. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 5.208333333%, SURG 2.409638554%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 91, SURG 162. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.436245421, P 0.230748010; probability-ordering Fisher diagnostic P 0.294852634. COMPATIBLE: Pearson diagnostic 0.230748010 versus printed-P band [0.225, 0.235]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S179

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Upper respiratory infection, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 18/96 (18.8%); SURG 43/166 (25.9%); P 0.19. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 18.750000000%, SURG 25.903614458%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 78, SURG 123. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.742632384, P 0.186805764; probability-ordering Fisher diagnostic P 0.225376274. COMPATIBLE: Pearson diagnostic 0.186805764 versus printed-P band [0.185, 0.195]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S180

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Pneumonia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 3/96 (3.1%); SURG 11/166 (6.6%); P 0.23. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 3.125000000%, SURG 6.626506024%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 93, SURG 155. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.474384144, P 0.224655379; probability-ordering Fisher diagnostic P 0.267796332. COMPATIBLE: Pearson diagnostic 0.224655379 versus printed-P band [0.225, 0.235]; interval gap 0.000344621, relative discrepancy 0.001498352 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; shared last-digit diagnostic observation is recorded once in the checker’s Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S181

- **Location and document role:** DOC-003 REPORT, PDF p19, eTable5, Cellulitis, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=19).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 5/96 (5.2%); SURG 6/166 (3.6%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 5.208333333%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 91, SURG 160. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.384169601, P 0.535380032; probability-ordering Fisher diagnostic P 0.538036753. COMPATIBLE: Pearson diagnostic 0.535380032 versus printed-P band [0.525, 0.535]; interval gap 0.000380032, relative discrepancy 0.000717041 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; shared last-digit diagnostic observation is recorded once in the checker’s Excluded observations table.
- **Pass 1:** PASS_1_COMPLETE.

### S182

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Systemic infection/sepsis, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S183

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Osteomyelitis, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 1/166 (0.6%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 165. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.154922575, P 0.693874970; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S184

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, COVID-19, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 1/166 (0.6%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 165. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.154922575, P 0.693874970; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S185

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Severe hyperglycemia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 8/96 (8.3%); SURG 14/166 (8.4%); P 0.98. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 8.333333333%, SURG 8.433734940%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SURG 152. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.000797128, P 0.977475853; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.977475853 versus printed-P band [0.975, 0.985]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S186

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Hyperparathyroidism, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S187

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Dehydration, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 14/166 (8.4%); P 0.058. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 8.433734940%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 152. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 4.277873180, P 0.038611502; probability-ordering Fisher diagnostic P 0.057707361. COMPATIBLE: Fisher diagnostic 0.057707361 versus printed-P band [0.0575, 0.0585]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S188

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Hypokalemia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 8/166 (4.8%); P 0.33. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 4.819277108%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 158. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.240207656, P 0.265431133; probability-ordering Fisher diagnostic P 0.333797872. COMPATIBLE: Fisher diagnostic 0.333797872 versus printed-P band [0.325, 0.335]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S189

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Hyperkalemia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 0/166 (0.0%); P 0.37. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 166. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.735791826, P 0.187673048; probability-ordering Fisher diagnostic P 0.366412214. COMPATIBLE: Fisher diagnostic 0.366412214 versus printed-P band [0.365, 0.375]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S190

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Hypercalcemia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 1/166 (0.6%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 165. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.580529013, P 0.446104906; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S191

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Back pain, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 18/96 (18.8%); SURG 36/166 (21.7%); P 0.57. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 18.750000000%, SURG 21.686746988%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 78, SURG 130. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.320594880, P 0.571250294; probability-ordering Fisher diagnostic P 0.636067232. COMPATIBLE: Pearson diagnostic 0.571250294 versus printed-P band [0.565, 0.575]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S192

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Osteoarthritis, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 8/96 (8.3%); SURG 6/166 (3.6%); P 0.10. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 8.333333333%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SURG 160. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.677798753, P 0.101756273; probability-ordering Fisher diagnostic P 0.151471842. COMPATIBLE: Pearson diagnostic 0.101756273 versus printed-P band [0.095, 0.105]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S193

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Renal insufficiency, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 4/166 (2.4%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 2.409638554%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 162. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.028942593, P 0.864911654; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S194

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Acute renal failure, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 2/166 (1.2%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.014303675, P 0.904801538; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S195

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Allergy/intolerance to medication or supplement, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 5/96 (5.2%); SURG 9/166 (5.4%); P 0.94. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 5.208333333%, SURG 5.421686747%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 91, SURG 157. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.005473941, P 0.941021321; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.941021321 versus printed-P band [0.935, 0.945]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S196

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Alcohol abuse, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 7/166 (4.2%); P 0.49. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 4.216867470%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 159. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.834673785, P 0.360924479; probability-ordering Fisher diagnostic P 0.493005380. COMPATIBLE: Fisher diagnostic 0.493005380 versus printed-P band [0.485, 0.495]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S197

- **Location and document role:** DOC-003 REPORT, PDF p20, eTable5, Abdominal wall hernia, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=20).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 6/166 (3.6%); P 0.43. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 160. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.548286985, P 0.213388643; probability-ordering Fisher diagnostic P 0.428302162. COMPATIBLE: Fisher diagnostic 0.428302162 versus printed-P band [0.425, 0.435]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S198

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Crossovers, conversions, and revisions, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 24/96 (25.0%); SURG 15/166 (9.0%); P <.001. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 25.000000000%, SURG 9.036144578%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 72, SURG 151. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 12.234513771, P 0.000469225; probability-ordering Fisher diagnostic P 0.000959658. COMPATIBLE: both Pearson (0.000469225) and Fisher (0.000959658) are below .001.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S199

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Cholecystectomy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 7/166 (4.2%); P 0.49. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 4.216867470%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 159. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.834673785, P 0.360924479; probability-ordering Fisher diagnostic P 0.493005380. COMPATIBLE: Fisher diagnostic 0.493005380 versus printed-P band [0.485, 0.495]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S200

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Lysis of adhesions, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S201

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Hernia repair, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S202

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Exploratory laparoscopy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S203

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Exploratory laparotomy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 1/166 (0.6%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 165. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.580529013, P 0.446104906; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S204

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Appendectomy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S205

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Colon resection, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S206

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Hysterectomy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S207

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Other abdominal surgery, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 5/166 (3.0%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 3.012048193%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 161. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.201747044, P 0.653314414; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S208

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Endoscopic treatment of leak, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 1/166 (0.6%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 165. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.580529013, P 0.446104906; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S209

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Endoscopic treatment of dilated GJ stoma, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 2/166 (1.2%); P 0.53. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 1.204819277%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 164. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.165523633, P 0.280323002; probability-ordering Fisher diagnostic P 0.533912433. COMPATIBLE: Fisher diagnostic 0.533912433 versus printed-P band [0.525, 0.535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S210

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Endoscopic treatment of GI bleeding, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 0/166 (0.0%); P 0.37. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 0.000000000%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 166. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.735791826, P 0.187673048; probability-ordering Fisher diagnostic P 0.366412214. COMPATIBLE: Fisher diagnostic 0.366412214 versus printed-P band [0.365, 0.375]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S211

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Other therapeutic endoscopy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 5/166 (3.0%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 3.012048193%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 161. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.201747044, P 0.653314414; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S212

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Other endoscopy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 3/96 (3.1%); SURG 14/166 (8.4%); P 0.09. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 3.125000000%, SURG 8.433734940%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 93, SURG 152. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.825190197, P 0.092795850; probability-ordering Fisher diagnostic P 0.119907166. COMPATIBLE: Pearson diagnostic 0.092795850 versus printed-P band [0.085, 0.095]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S213

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Joint injection, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 9/96 (9.4%); SURG 6/166 (3.6%); P 0.053. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 9.375000000%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 87, SURG 160. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 3.739548071, P 0.053138680; probability-ordering Fisher diagnostic P 0.094073246. COMPATIBLE: Pearson diagnostic 0.053138680 versus printed-P band [0.0525, 0.0535]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S214

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Procedures for fractures, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 1/96 (1.0%); SURG 3/166 (1.8%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 1.041666667%, SURG 1.807228916%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 95, SURG 163. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.237116587, P 0.626296480; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S215

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Joint replacement, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 5/96 (5.2%); SURG 3/166 (1.8%); P 0.12. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 5.208333333%, SURG 1.807228916%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 91, SURG 163. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.376822991, P 0.123147800; probability-ordering Fisher diagnostic P 0.146897403. COMPATIBLE: Pearson diagnostic 0.123147800 versus printed-P band [0.115, 0.125]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S216

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Amputation, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 1/166 (0.6%); P 1.00. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 165. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.580529013, P 0.446104906; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Fisher diagnostic 1.000000000 versus printed-P band [0.995, 1.000]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S217

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Other orthopedic surgery, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 13/96 (13.5%); SURG 33/166 (19.9%); P 0.19. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 13.541666667%, SURG 19.879518072%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 83, SURG 133. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.687924959, P 0.193874867; probability-ordering Fisher diagnostic P 0.238772514. COMPATIBLE: Pearson diagnostic 0.193874867 versus printed-P band [0.185, 0.195]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S218

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Cataract surgery, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 8/96 (8.3%); SURG 13/166 (7.8%); P 0.89. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 8.333333333%, SURG 7.831325301%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 88, SURG 153. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.020790532, P 0.885351006; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.885351006 versus printed-P band [0.885, 0.895]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S219

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Other eye surgery, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 4/96 (4.2%); SURG 6/166 (3.6%); P 0.82. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 4.166666667%, SURG 3.614457831%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 92, SURG 160. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 0.050522726, P 0.822156259; probability-ordering Fisher diagnostic P 1.000000000. COMPATIBLE: Pearson diagnostic 0.822156259 versus printed-P band [0.815, 0.825]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S220

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Vitrectomy, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 1/166 (0.6%); P 0.56. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 165. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.178487438, P 0.277664218; probability-ordering Fisher diagnostic P 0.556320489. COMPATIBLE: Fisher diagnostic 0.556320489 versus printed-P band [0.555, 0.565]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S221

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Panniculectomy or abdominoplasty, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 0/96 (0.0%); SURG 5/166 (3.0%); P 0.16. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 0.000000000%, SURG 3.012048193%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 96, SURG 161. Direction: SURG observed frequency is higher than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 2.947822418, P 0.085993290; probability-ordering Fisher diagnostic P 0.161712951. COMPATIBLE: Fisher diagnostic 0.161712951 versus printed-P band [0.155, 0.165]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

### S222

- **Location and document role:** DOC-003 REPORT, PDF p21, eTable6, Other plastic surgery, MED and SURG row; [source](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=21).
- **Population/time/contrast/reference:** through 12 years; participants in original MED (N=96) and bariatric-surgery (N=166) groups; SURG versus MED; MED reference. Outcome definition is the named adverse-event/procedure row.
- **All printed values:** MED 2/96 (2.1%); SURG 1/166 (0.6%); P 0.56. Coefficient/OR/CI/SE/test statistic: none printed. No per-row model or covariate adjustment is printed; stated method family is chi-squared or Fisher’s exact test.
- **Count/denominator/percentage check:** exact percentages MED 2.083333333%, SURG 0.602409639%; each falls in its printed half-unit interval, gap 0. Events do not exceed denominators; nonevents MED 94, SURG 165. Direction: SURG observed frequency is lower than MED.
- **Estimate/test logic:** no estimate or CI is supplied for containment or interval-P comparison. Pearson diagnostic chi-square 1.178487438, P 0.277664218; probability-ordering Fisher diagnostic P 0.556320489. COMPATIBLE: Fisher diagnostic 0.556320489 versus printed-P band [0.555, 0.565]; interval gap 0.000000000, relative discrepancy 0.000000000 ≤0.05.
- **Method/conclusion checks:** the permitted-family reconstruction is internally compatible; no printed modeling step, adjustment, margin or decision rule conflicts. Exact per-row test selection, Fisher sidedness and probability ordering are not separately supplied, and are not inferred. No unreported detail alone is a finding.
- **Finding/excluded observation linkage:** No finding; check reconciles or is explicitly not applicable.
- **Pass 1:** PASS_1_COMPLETE.

## Shard completion

102/102 assigned relationships have PASS_1_COMPLETE. Numeric tests: 100; all-zero/no-applicable tests: 2 (S139, S140). Findings: 0. Excluded observations: 1 consolidated last-digit diagnostic pattern covering S147, S152, S165, S180, S181. Scientific coverage gaps: none. Method-definition limits: exact per-row test selection and Fisher sidedness/probability ordering are unreported, so permitted-family reconstructions are diagnostics rather than claims about software options.

