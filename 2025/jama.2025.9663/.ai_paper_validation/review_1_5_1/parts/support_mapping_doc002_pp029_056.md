# DOC-002 Support Quantitative Mapping — PDF pp. 29-56

## Scope and method

- **Direct source:** `joi250042supp1_prod_1753377747.92525.pdf`, PDF pp. 29-56 (28 pages).
- **Document components:** original UK-ROX Trial Protocol v1.1 dated 14 December 2020, printed pp. 28-40 (PDF pp. 29-41); then UK-ROX Trial Protocol v1.8 dated 14 October 2024, printed pp. 1-15 (PDF pp. 42-56).
- **Fresh inspection:** the source PDF was rendered locally on CPU and visually inspected where quantitative/statistical content occurs. Native/layout extraction was retained only as a page locator because its font-to-Unicode mapping is corrupted. No reused DOC-002 scientific extraction exists.
- **Scope result:** no trial results table, outcome count, final effect estimate, or candidate observation is printed in this shard. This is protocol/SAP planning and administrative material. All relationships below are protocol definitions or planned analyses and are retained for later cross-document matching.

## Page-level coverage

| PDF pages | Printed document pages / section | Direct-source mapping outcome |
|---|---|---|
| 29-31 | v1.1 pp. 28-30; outcomes, sample size, clinical/economic analysis | Result-relevant planned endpoints, sample-size assumptions, models, interim analysis, and economic methods mapped below. |
| 32-34 | v1.1 pp. 31-33; economic-analysis continuation, trial management/ethics | No additional printed trial result; only continuation of planned economic methods and administrative identifiers. |
| 35-40 | v1.1 pp. 34-39; data handling, oversight, dissemination and appendices | No result-relevant quantitative relationship beyond protocol administration. |
| 41 | v1.1 p. 40; Appendix 3 expected adverse events | No quantitative result; list of expected SAEs only. |
| 42-44 | v1.8 pp. 1-3; cover, reference numbers, signatures | Final protocol identity/version and administrative reference numbers; no trial result. |
| 45-56 | v1.8 pp. 4-15; contacts and early protocol material | No final trial result observed in this assigned early-protocol portion; preserve as final-protocol context for matching subsequent DOC-002 shards. |

## Numeric/reporting relationships

### D2B-N001 — Primary and secondary endpoint definitions (original protocol)

- **Location:** DOC-002 PDF p. 29 (printed p. 28), v1.1.
- **Direct printed evidence:** primary clinical outcome is 90-day all-cause mortality. Primary economic outcome is incremental costs, QALYs, and net monetary benefit at 90 days. Clinical secondary outcomes include ICU/hospital mortality censored at 90 days, mortality at 60 days and 1 year, ICU/acute-hospital duration censored at 90 days, and EuroQol EQ-5D-5L HrQoL at 90 days. Economic secondary outcomes are HrQoL and resource use/costs at 90 days and estimated lifetime incremental cost-effectiveness.
- **Matching definition:** outcomes use 90 days unless a different stated censoring/time point applies; mortality time points are 60 days, 90 days, and 1 year.

### D2B-N002 — Original-protocol sample-size assumptions and recruitment target

- **Location:** DOC-002 PDF p. 29 (printed p. 28), v1.1 §4.1.
- **Direct printed evidence:** potentially eligible CMP population `N=96,028` (April 2017-March 2019); Risk II dataset `N=82,075` (April 2014-March 2016); anticipated 90-day mortality `37%`; absolute risk reduction `2.5%`, described as relative risk reduction `6.8%`; target change `37%` to `34.5%`; `90%` power requires `15,444` patients. Allowing `6%` refusal/withdrawal/loss to follow-up gives recruitment target `16,500` patients.
- **Recruitment assumption:** 8 patients per unit per month; 100 ICUs; full sample within two years, with staggered opening over six months.
- **Relationship rule:** `15,444 / (1 - 0.06) = 16,429.8`, which rounds up to the printed 16,500 planned recruitment target; this is coherent planning arithmetic, not a candidate observation.

### D2B-N003 — Planned interim information sizes and stopping threshold

- **Location:** DOC-002 PDF p. 30 (printed p. 29), v1.1 §4.2.2.
- **Direct printed evidence:** two interim analyses after recruitment and 90-day follow-up of `4,500` and `10,000` patients. The Peto-Haybittle stopping rule is `P<0.001` to recommend early termination for effectiveness or harm; additional interim analyses may occur at DMEC request.
- **Matching definition:** this is a planned stopping rule, not a reported P value or interim result.

### D2B-N004 — Economic-evaluation time horizon, sampling, QALY and monetary threshold

- **Location:** DOC-002 PDF pp. 30-31 (printed pp. 29-30), v1.1 §4.2.3.
- **Direct printed evidence:** cost-effectiveness is reported at 90 days; detailed in-patient resource data are collected from `15%` of participants selected for intervention/adherence monitoring; HrQoL is assessed at 90 days; 90-day survivors use EQ-5D score at 90 days with an assumption of zero at randomisation and linear interpolation; decedents between randomisation and day 90 are assigned zero QALYs. Net monetary benefits value QALY gains at `£20,000 per QALY` minus incremental costs.
- **Matching definition:** reported economic estimates should be mean incremental cost, QALYs and net monetary benefit at 90 days with `95% confidence intervals`; planned regression includes patient clustering within site, patient- and site-level covariate adjustment, and sensitivity/subgroup analysis.

### D2B-N005 — Original-protocol adverse-event appendix is nonquantitative

- **Location:** DOC-002 PDF p. 41 (printed p. 40), v1.1 Appendix 3.
- **Direct printed evidence:** expected SAEs list sinus tachycardia, supraventricular tachycardia, atrial fibrillation, myocardial ischaemia/infarction, and mesenteric ischaemia.
- **Mapping result:** no count, rate, proportion, or comparative safety result is printed.

### D2B-N006 — Final-protocol version identifiers retained for cross-version matching

- **Location:** DOC-002 PDF pp. 42-43 (printed pp. 1-2), v1.8.
- **Direct printed evidence:** Protocol version `1.8`, dated `14 October 2024`; IRAS number `288506`; REC number `20/SC/0423`; NIHR Portfolio CPMS ID `46926`; ISRCTN `ISRCTN13384956`; NIHR HTA project `NIHR130508`.
- **Matching definition:** these identify the final protocol section and must not be conflated with v1.1 values above.

## Statistical relationships

### D2B-S001 — Planned primary-outcome model and effect measures (original protocol)

- **Location:** DOC-002 PDF p. 30 (printed p. 29), v1.1 §4.2.2.
- **Direct printed evidence:** primary 90-day all-cause mortality analysis is adjusted for site, hypoxic-ischaemic encephalopathy, acute brain pathologies excluding hypoxic-ischaemic encephalopathy, and sepsis (stratification variables), plus prespecified baseline covariates. Regression models incorporate site random effects; reported measures are absolute risk reduction and relative risk.
- **Matching definition:** a final-paper mortality estimate should only be compared to this protocol after matching population, site/random-effect model, adjustment set, and effect measure/scale.

### D2B-S002 — Planned secondary-outcome models and survival analysis (original protocol)

- **Location:** DOC-002 PDF p. 30 (printed p. 29), v1.1 §4.2.2.
- **Direct printed evidence:** binary outcomes use binomial/Poisson-family regression; continuous outcomes use normal-family models; ICU/acute-hospital duration uses Wilcoxon rank-sum tests stratified by survival status; survival is shown in Kaplan-Meier plots and analysed using Cox proportional hazards models with shared frailty at site level.
- **Matching definition:** distinguish risk-based binary estimates from hazard-ratio survival estimates and from rank-based duration tests.

### D2B-S003 — Planned subgroup interaction tests (original protocol)

- **Location:** DOC-002 PDF p. 30 (printed p. 29), v1.1 §4.2.2.
- **Direct printed evidence:** adjusted primary-outcome regressions test treatment-by-subgroup interactions for a limited a-priori subgroup set: suspected hypoxic-ischaemic encephalopathy; acute brain injury excluding hypoxic-ischaemic encephalopathy; and sepsis.
- **Matching definition:** later subgroup P values/interaction effects must be treated as interaction analyses, not within-subgroup treatment-effect tests unless explicitly labeled otherwise.

### D2B-S004 — Planned economic-effect reporting (original protocol)

- **Location:** DOC-002 PDF p. 31 (printed p. 30), v1.1 §4.2.3.
- **Direct printed evidence:** CEA follows intention-to-treat; reports mean (95% CI) incremental cost, QALYs and net monetary benefit at 90 days; uses multilevel linear models for site clustering; robustness assessed through extensive sensitivity analysis and clinical-outcome subgroup analysis.
- **Matching definition:** a subsequent economic result should be matched by the 90-day horizon, ITT population, mean incremental measure, CI, and model/adjustment context before comparison.

## Candidate observations

No provisional candidate observation (`D2B-C...`) was identified in PDF pp. 29-56. The displayed `P<0.001` is a planned Peto-Haybittle criterion, not an observed display-zero P value or inconsistency.

## Limitations

The PDF's native/layout extraction has corrupted glyph-to-Unicode mapping. Visual direct-source inspection was therefore required for the mapped planning relationships. This shard contains protocol planning and administrative material, not a reported trial-results table; it supplies definitions and original-versus-final protocol identity for cross-document matching rather than an internal result comparison.
