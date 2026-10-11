# Statistical pass 2 bounded input packet 6

Exact disjoint assigned relationships: S198, S199, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222.

Read this complete packet AND statistics/pass2_shared_context.md, which preserves the complete current candidate ledger, initial screening log, exact-source recheck facts, and all 53 original checker exclusions. Only assigned S records below are owned here; source-part headers describe original global provenance and do not expand this assignment. Every assigned relationship needs an explicit PASS_2_COMPLETE record without discarding its PASS_1_COMPLETE facts. All candidates remain Pending Human Adjudication. Original source-linked calculations are reused rather than repeated unnecessarily.

## Original source-part shared methods and provenance

# Statistical pass 1 extra relationship inventory

Runtime agent: /root/statistical_pass1_extra. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Assigned disjoint scope: DOC-003 REPORT eTable3 (PDF p17), eTable5 (PDF pp19-20), eTable6 (PDF p21). This part has 102 relationships, S121-S222: 29 nutritional-abnormality contrasts (27 printed numeric P values and two NA), 48 adverse-event tests, and 25 procedure tests. No other scientific units are assigned here.

## Source and statistical definitions

The supplied source is [DOC-003](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), REPORT by content. Direct Poppler layout and freshly rendered source pages were read; the support mapper transcription is a locator. Native direct extraction covers physical pp17-21 and the supporting method definitions on pp4-6. Source authority is the rendered PDF. All count, denominator, percent, P-value and reference-group cells on the four assigned table pages were visually confirmed.

DOC-003 [p6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6) states that adverse events and study outcomes were summarized as percentages and compared using chi-squared or Fisher’s exact tests; [p5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=5) states secondary outcomes are hypothesis generating without multiple-testing adjustment. eTable5 footnote b on p20 and eTable6 footnote b on p21 repeat the chi-squared/Fisher family. eTable3 footnote a gives MED as comparison/reference and footnote b defines N as participants with observed data. No odds ratios, coefficients, CIs, standard errors, or test statistics are printed in these three tables. No regression/longitudinal adjustment is attributed to these table tests; no adjusted-versus-crude comparison is performed. Printed tests belong to through-12-year nutritional abnormalities, adverse events and procedures, respectively.

## Calculation and precision rules used for every record

For MED events a among n and comparison-group events b among m, the diagnostic non-continuity-corrected Pearson statistic is (n+m)[a(m-b)-(n-a)b]^2/[nm(a+b)(n+m-a-b)]. The reported-family diagnostic P is its chi-square(1) survival probability. Degrees of freedom 1 is a mathematical consequence of each reconstructed 2-by-2 table, not an inferred regression degree of freedom. The compatible Fisher diagnostic is the fixed-margin hypergeometric sum over tables no more probable than the observed table, with floating-point equality tolerance 1e-10 on log probabilities. Fisher sidedness and probability-ordering convention are not separately stated by the authors: this sum is a clearly labeled diagnostic permitted-family reconstruction that reproduces numerous rows, not an assertion about the authors’ exact software option. The Pearson tail was calculated in JavaScript using an erfc approximation with absolute numerical accuracy better than 1.5e-7; hypergeometric probabilities were evaluated by log-factorial sums. No continuity correction or effect model is assumed to be the actual author method. Both diagnostic P values are retained, and compatibility with at least one stated test family is sufficient to avoid an invented method conflict.

Counts represent integer participants and events: their half-unit rounding bands contain the printed integer as their only possible discrete value. Every observed percentage is recomputed as 100n/N and allowed its half-unit printed rounding band. Every numeric P value is allowed its own half-unit band; the remaining gap divided by printed P is recorded. Tiny last-digit gaps in 5 rows are below the scope’s 0.05 relative-discrepancy threshold. No interval-versus-P conflict exists because no intervals are printed here, and no effect-estimate/test conflict is inferred from such last-digit count-to-P diagnostics. Two all-zero eTable3 contrasts print NA; Pearson has a zero expected-event margin, and the absence of a numeric test is explicitly tracked.

Point-estimate containment, CI endpoint order, interval-versus-P agreement, coefficient sign, superiority, noninferiority, equivalence, multiplicity decision, interim and stopping checks are not applicable to these count/P-only tables unless a corresponding claim is supplied; none is supplied in this scope. Direction is retained as comparison-group frequency relative to MED; no printed narrative effect claim conflicts with the table. No sample-size calculation is printed in this scope. This prevents inventing absent model, covariance, estimand, sidedness or margin definitions.



## Assigned original records

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
