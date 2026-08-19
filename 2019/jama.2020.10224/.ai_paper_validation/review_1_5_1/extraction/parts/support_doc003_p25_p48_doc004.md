# Support quantitative evidence extraction — DOC-003 pp. 25-48 and DOC-004 pp. 1-2

## Scope and method

Direct-source scope: 26 PDF pages: `joi200066supp2_prod.pdf` PDF pp. 25-48 (DOC-003) and `joi200066supp3_prod.pdf` PDF pp. 1-2 (DOC-004). Fresh `pdftotext -layout` was used as a transcription locator for every assigned page. Tables and the eFigure were checked against rendered exact PDF pages; the direct PDFs remain authoritative. No OCR was necessary. Page references below are PDF pages.

## DOC-003 — `joi200066supp2_prod.pdf`

### PDF p. 25 — sensitivity-analysis narrative

Result-relevant narrative: additional censoring at parent-trial cardiovascular-disease (CVD) endpoints gave total-depression HR 0.99 (95% CI 0.88-1.10). CVD development was associated with total depression HR 2.96 (2.05-4.27), incident depression HR 2.72 (1.76-4.21), and recurrent depression HR 2.85 (1.46-5.55). Including CVD as a time-updated covariate gave the vitamin-D3 effect HR 0.97 (0.87-1.09). Cancer development was not statistically significantly associated with total depression HR 1.21 (0.89-1.65), incident depression HR 1.28 (0.91-1.81), or recurrent depression HR 0.97 (0.48-1.97). The text states that censoring/adjusting for time-updated parent-trial cancer endpoints did not change results. Model details beyond those stated are not supplied on this page.

### PDF p. 26 — eTable 8, Fine-Gray competing-risk sensitivity analysis

| Outcome | Participants | Adjusted subdistribution HR (95% CI) | P value |
|---|---:|---|---:|
| Total depression | 18,353 | 0.97 (0.87-1.09) | 0.60 |
| Incident depression | 16,657 | 0.99 (0.87-1.13) | 0.87 |
| Recurrent depression | 1,696 | 0.95 (0.76-1.18) | 0.62 |

Definition: adjusted HRs are from Fine and Gray subdistribution-hazard models; death from any cause is a competing event rather than a censoring event. Total depression is the composite of reported clinician diagnosis, treatment, and/or PHQ-8 >=10, and combines incident and recurrent depression. Incident cases occur among people with no past depression; recurrent cases occur among those with past depression but no treatment or activity in the previous 2 years. The two secondary-risk-set counts reconcile exactly to the total risk set: 16,657 + 1,696 = 18,353.

### PDF p. 27 — eTable 9, PHQ-8 change rate-ratio analysis

Repeated-measures negative-binomial models, with follow-up time as an indicator and adjustment for age, sex, and n-3 fatty-acid randomization group. The displayed rate ratios (RRs) and 95% CIs represent percent differences in change in PHQ-8 severity for vitamin D3 versus placebo.

| Time contrast | Vitamin D3 N | Placebo N | RR (95% CI) | P value |
|---|---:|---:|---|---:|
| Year 1 vs baseline | 8,534 | 8,486 | 1.00 (0.95-1.05) | 0.92 |
| Year 2 vs baseline | 8,381 | 8,344 | 1.03 (0.98-1.08) | 0.22 |
| Year 3 vs baseline | 8,176 | 8,112 | 1.02 (0.96-1.07) | 0.57 |
| Year 4 vs baseline | 7,763 | 7,603 | 1.00 (0.95-1.05) | 0.87 |
| Year 5 vs baseline | 5,316 | 5,231 | 1.03 (0.97-1.09) | 0.30 |
| Average years 1-5 vs baseline | 9,181 | 9,172 | 1.01 (0.97-1.05) | 0.51 |

### PDF pp. 28-29 — eTable 10, PHQ-8 sensitivity analysis censoring after a mood-safety letter

General linear response-profile models estimate means, with time indicator variables and adjustment for age, sex, and n-3 fatty-acid randomization group. Within-group values are adjusted means (95% CIs) at baseline and adjusted mean changes thereafter. Mean difference means vitamin-D3 minus placebo change. The p-interaction is a 5-degree-of-freedom treatment-by-time test.

| Time contrast | Vitamin D3 N; adjusted mean/change (95% CI) | Placebo N; adjusted mean/change (95% CI) | Mean difference (95% CI); P value |
|---|---|---|---|
| Baseline | 9,181; 1.08 (1.05, 1.11) | 9,172; 1.13 (1.09, 1.16) | --; -- |
| Year 1 vs baseline | 8,534; 0.03 (-0.01, 0.07) | 8,486; 0.03 (-0.00, 0.07) | -0.00 (-0.06, 0.05); 0.86 |
| Year 2 vs baseline | 8,349; 0.07 (0.04, 0.11) | 8,311; 0.05 (0.01, 0.09) | 0.02 (-0.03, 0.08); 0.42 |
| Year 3 vs baseline | 8,115; 0.11 (0.07, 0.15) | 8,054; 0.08 (0.04, 0.12) | 0.02 (-0.04, 0.08); 0.43 |
| Year 4 vs baseline | 7,671; 0.08 (0.04, 0.13) | 7,517; 0.10 (0.05, 0.14) | -0.01 (-0.07, 0.05); 0.69 |
| Year 5 vs baseline | 5,239; 0.24 (0.19, 0.29) | 5,159; 0.21 (0.16, 0.26) | 0.03 (-0.04, 0.10); 0.39 |
| Average years 1-5 vs baseline | 9,181; not displayed | 9,172; not displayed | 0.01 (-0.04, 0.05); 0.71 |

Displayed p-interaction: 0.63. The final-row difference is explicitly the average change difference over years 1-5.

### PDF p. 30 — sensitivity-analysis narrative for eTable 10

Administrative/procedural explanation with quantitative thresholds relevant to the sensitivity analysis: letters were sent for PHQ-8 >=10 when neither recent diagnosis nor treatment was self-reported; all participants with PHQ-8 >=15 received letters regardless of self-report. PHQ-8 observations after the letter send date were censored. The narrative says these estimates were similar to primary-analysis estimates. No additional result values are printed.

### PDF pp. 31-32 — eTable 11, PHQ-8 analysis omitting year 5

General linear response-profile models with time indicators and adjustment for age, sex, and n-3 randomization. Adjusted mean/change values, vitamin-D3-minus-placebo differences, and tests are:

| Time contrast | Vitamin D3 N; adjusted mean/change (95% CI) | Placebo N; adjusted mean/change (95% CI) | Mean difference (95% CI); P value |
|---|---|---|---|
| Baseline | 9,181; 1.08 (1.05, 1.11) | 9,172; 1.13 (1.09, 1.16) | --; -- |
| Year 1 vs baseline | 8,534; 0.03 (-0.01, 0.07) | 8,486; 0.03 (-0.01, 0.07) | -0.01 (-0.06, 0.05); 0.84 |
| Year 2 vs baseline | 8,381; 0.07 (0.03, 0.11) | 8,344; 0.04 (0.00, 0.08) | 0.03 (-0.03, 0.08); 0.36 |
| Year 3 vs baseline | 8,176; 0.09 (0.05, 0.13) | 8,112; 0.07 (0.03, 0.11) | 0.01 (-0.05, 0.07); 0.65 |
| Year 4 vs baseline | 7,763; 0.06 (0.02, 0.10) | 7,603; 0.07 (0.03, 0.11) | -0.01 (-0.07, 0.05); 0.72 |
| Average years 1-4 vs baseline | 9,181; not displayed | 9,172; not displayed | 0.00 (-0.04, 0.05); 0.83 |

Displayed p-interaction: 0.73. The footnote defines the final row as average vitamin-D3-versus-placebo PHQ-8 change over years 1-4.

### PDF pp. 33-34 — eTable 12, sex-specific depression rates

Rate unit is cases per 1,000 person-years (p-y); person-time denominators are not printed. Total depression is the composite and equals incident plus recurrent counts in each sex.

| Sex and outcome | Participants | Cases | Rate per 1,000 p-y |
|---|---:|---:|---:|
| Men: total | 9,330 | 548 | 11.36 |
| Men: incident | 8,642 | 426 | 9.49 |
| Men: recurrent | 688 | 122 | 36.27 |
| Women: total | 9,023 | 686 | 14.97 |
| Women: incident | 8,015 | 494 | 12.04 |
| Women: recurrent | 1,008 | 192 | 40.01 |

Risk-set and event-count identities: men 8,642 + 688 = 9,330 and 426 + 122 = 548; women 8,015 + 1,008 = 9,023 and 494 + 192 = 686.

### PDF p. 35 — eTable 12 result narrative

Narrative rounds the eTable 12 rates to one decimal: total 11.4/1,000 p-y in males and 15.0/1,000 p-y in females; incidence overall 10.7/1,000 p-y, 9.5 male and 12.0 female; recurrence overall 38.5/1,000 p-y, 36.3 male and 40.0 female. It reports women versus men total-depression HR 1.34 (95% CI 1.19-1.50) from the primary results model. The overall rates are new printed results, but their person-time denominators are not printed here.

### PDF pp. 36-37 — eTable 13, treatment-specific depression rates

Rate unit is cases per 1,000 person-years; person-time denominators are not printed. Counts and risk sets exactly partition total depression by incident and recurrent status.

| Group and outcome | Participants | Cases | Rate per 1,000 p-y |
|---|---:|---:|---:|
| Vitamin D3: total | 9,181 | 609 | 12.95 |
| Vitamin D3: incident | 8,350 | 459 | 10.66 |
| Vitamin D3: recurrent | 831 | 150 | 37.58 |
| Placebo: total | 9,172 | 625 | 13.29 |
| Placebo: incident | 8,307 | 461 | 10.76 |
| Placebo: recurrent | 865 | 164 | 39.32 |

Identities: vitamin D3 risk sets 8,350 + 831 = 9,181 and cases 459 + 150 = 609; placebo risk sets 8,307 + 865 = 9,172 and cases 461 + 164 = 625.

### PDF pp. 38-39 — eTable 14, baseline 25(OH)D analyses

Sample N is 11,417 with 25(OH)D data. Low vitamin D is <20 ng/mL. Cox models for total-depression HRs adjust for age, sex, vitamin-D3 randomization, and n-3 randomization. General linear response-profile models, with the same listed covariates, estimate mean differences in PHQ-8 change.

| Analysis / exposure | N | Result (95% CI) | P value |
|---|---:|---|---:|
| Total-depression HR: sufficient vitamin D | 10,089 | 1.00 (reference) | N/A |
| Total-depression HR: low vitamin D | 1,328 | 1.08 (0.87-1.35) | 0.48 |
| Total-depression HR: per 10 ng/mL 25(OH)D increase | 11,417 | 1.00 (0.93-1.08) | 0.94 |
| Overall PHQ-8 change mean difference: low vitamin D | 11,417 | -0.04 (-0.13, 0.06) | 0.45 |
| Overall PHQ-8 change mean difference: per 10 ng/mL increase | 11,417 | 0.02 (-0.01, 0.05) | 0.14 |

Categorical exposure counts reconcile: 10,089 + 1,328 = 11,417.

### PDF p. 40 — eTable 14 narrative

Narrative restates total-depression HR 1.00 (0.93-1.08) per 10-ng/mL increase and HR 1.08 (0.87-1.35) for low vitamin D. It says no significant overall PHQ-8-change differences (eTable 14c), while stating that baseline 25(OH)D was associated with initial symptom level and at individual follow-up time points; values for those time-point results are not printed on this page.

### PDF p. 41 — eTable 15, unadjusted PHQ-8 means (SDs)

| Time | Vitamin D3 mean (SD) | Placebo mean (SD) |
|---|---|---|
| Baseline | 1.08 (1.60) | 1.12 (1.63) |
| Year 1 | 1.10 (1.89) | 1.14 (1.95) |
| Year 2 | 1.12 (1.98) | 1.14 (1.97) |
| Year 3 | 1.12 (1.97) | 1.16 (2.02) |
| Year 4 | 1.09 (1.91) | 1.14 (2.01) |
| Year 5 | 1.23 (2.06) | 1.23 (2.10) |

### PDF p. 42 — eFigure, item-level symptom likelihood ratios

Direct rendered-page inspection recovered the graphic values. Repeated-measures logistic regression has follow-up time as an indicator and adjustment for age, sex, and n-3 randomization. Likelihood ratios compare vitamin D3 with placebo in change in likelihood of burden, averaged across all follow-up times since baseline.

| PHQ-8 item-level symptom | Likelihood ratio (95% CI) | P value |
|---|---|---:|
| Anhedonia | 1.21 (0.88-1.67) | 0.24 |
| Feeling of sadness | 1.03 (0.60-1.77) | 0.92 |
| Sleep problems | 1.00 (0.89-1.12) | 0.99 |
| Energy problems | 1.03 (0.88-1.21) | 0.72 |
| Appetite problems | 0.91 (0.73-1.14) | 0.40 |
| Feeling of guilt | 0.61 (0.34-1.09) | 0.10 |
| Concentration problems | 0.87 (0.56-1.37) | 0.56 |
| Motor problems | 0.74 (0.39-1.40) | 0.36 |

### PDF pp. 43-47 — eMethods / protocol and administrative content

Administrative/protocol content was inspected throughout. Quantitative statements potentially relevant to population definitions or interpretation are: planned VITAL N 20,000 in 2008, 25% / N 5,000 Black-participant goal, revised target N 26,000, final N 25,871; original lower ages 60 men/65 women, revised to 50/55; CMS linkage available in approximately 70%; PHQ-8 measured six times (baseline/year 0 and years 1-5), versus original SAP years 0, 1, 3, and 5; a separate unreported CTSC subgroup of approximately 1,000; safety thresholds PHQ-8 >=10 and >=15; CTSC component N 1,054; PHQ-8/PHQ-9 intraclass correlation 0.63 (95% CI 0.59-0.67) among N 1,053 completing both forms; 86% agreement for incidence/recurrence eligibility versus MINI classification; most baseline assessments were within one month and most within two weeks. These are protocol/administrative or concordance-context facts, not new primary-treatment-effect results. No page reports a new table, figure, or treatment contrast beyond those identified.

### PDF p. 48 — eReferences

No applicable result-relevant quantitative relationship. The page is a reference list only; numeric strings are bibliographic years, volume/issue, and page ranges.

## DOC-004 — `joi200066supp3_prod.pdf`

### PDF pp. 1-2 — Data Sharing Statement

No applicable result-relevant quantitative relationship. Both pages are administrative data-access content. The only date, 05-01-2021, is the stated availability beginning date; it is not an outcome, denominator, effect estimate, statistical definition, table, or figure. The statement says data are available to affiliated investigators through secure databases and identifiable data require specific IRB approval.

## Extraction coverage conclusion

All 26 assigned pages were directly extracted and inspected. Result-relevant tables/figure/narratives were mapped on DOC-003 pp. 25-42; protocol/administrative content was opened on DOC-003 pp. 43-48 and DOC-004 pp. 1-2. No workbook formulas or cached workbook values occur in this PDF-only scope. No possible quantitative consistency candidate was identified during mapping; this is not an adjudication.
