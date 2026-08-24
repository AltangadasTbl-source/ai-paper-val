# DOC-002 relationship inventory: `joi200066supp1_prod.pdf`, PDF pages 1-31

## Scope and evidence status

Complete fresh mapping of the direct 31-page protocol PDF. All relationships are protocol/SAP definitions, planned analyses, power assumptions, or cited validation context. They are not observed VITAL-DEP results. Exact direct-PDF authority locations are given below; PDF pp. 18, 19, 21, 23, and 24 were visually inspected for the table/figure and statistical layout. No workbook is present, so there are no formulas or cached/displayed workbook values.

## Numeric/reporting relationships

| ID | Direct source location | Printed relationship and reconciliation | Matching main-paper key / status |
|---|---|---|---|
| N100 | PDF pp. 1, 3, 15 | 2×2 factorial; planned N=20,000; men ≥60, women ≥65; 5 years; D3 2,000 IU/d; EPA 500 mg/d + DHA 500 mg/d. | Trial design/doses/follow-up; PLANNED. |
| N101 | PDF pp. 3, 9 | Up to 20,000 enrolled; 18,200 anticipated additionally eligible for VITAL-DEP analyses. | Eligibility/analysis denominator; EXPECTED, not achieved. |
| N102 | PDF p. 8 | 10,000 men + 10,000 women = 20,000. Ethnicity 1,400 Hispanic + 18,600 non-Hispanic = 20,000. Race 5,000 + 500 + 400 + 80 + 14,020 = 20,000; categories may overlap ethnicity. | Baseline demographics and subgroup definition; EXPECTED. Arithmetic reconciles. |
| N103 | PDF pp. 5, 19 | 500 cases + 1,000 controls = 1,500; stated 1:2 matching, with controls matched on age group, gender, follow-up time, and season. | Biomarker/nested case-control sample; PLANNED. Arithmetic reconciles. |
| N104 | PDF pp. 14, 16 | CTSC random subset n=1,000, four centers, baseline and 2-year in-person assessments. | CTSC analyses; PLANNED. |
| N105 | PDF pp. 3, 5, 16 | Composite depression includes MDD, dysthymia, adjustment disorder including depressed mood, and depressive disorder NOS; questionnaires at years 0, 1, 3, 5. | Endpoint definition/assessment schedule; DEFINITION. |
| N106 | PDF pp. 5, 17, 20 | PHQ-8 range 0-24; ≥15 moderate-high and ≥20 high severity; ≥10 and ≥15 are separate letter-contact thresholds. | PHQ-8 scale/threshold analyses; DEFINITION. Must not equate letter threshold to primary endpoint algorithm. |
| N107 | PDF p. 18 Table 1 | Claims code lists: depressive disorders 296.2, 296.20-296.26, 296.3, 296.30-296.36, 300.4, 309.0-309.1, 309.28, 311; cited κ=0.67, sensitivity 56.6, specificity 99.4, PPV 92.8, NPV 94.4. | Claims ascertainment; cited external validation, not trial performance. |
| N121 | PDF p. 18 | The immediately preceding sentence references depression codes “(Table 3),” but the directly adjacent displayed caption is “Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders.” | Within-protocol table-reference label; possible candidate for later direct recheck. |
| N108 | PDF pp. 18-19, Figure 1 | Incident case sources: PHQ-8 algorithm, clinician diagnosis, DIS MDD/dysthymia, qualifying ICD-9 encounter, or antidepressant registration. Earliest questionnaire/CMS/dispensing date applies with a hierarchy favouring specificity. Person-time is randomization to event/censoring and stops at incident depression. | Analysis population/event date/risk time; DEFINITION. |
| N109 | PDF p. 20 | 25(OH)D assay and fatty-acid assays each report CV<10%; 25(OH)D2/D3 SRM 972. | Assay reliability/method footnote; PLANNED. |
| N110 | PDF p. 21 | ITT survival analysis: treatment versus corresponding placebo; follow to event, death, loss, or trial end; adjustment includes other intervention, age, gender. | Main time-to-event method; PLANNED. |
| N111 | PDF p. 21 | Compliance sensitivity censors when medication use is <2/3 over prior year; misclassification and CTSC-loss-to-follow-up sensitivity analyses proposed. | Sensitivity analyses; PLANNED. |
| N112 | PDF p. 21 | Mixed model has years 0/1/3/5, treatment/time/treatment×time; mean difference and 95% CI; antidepressant-initiation secondary analysis. | Longitudinal PHQ result; PLANNED. |
| N113 | PDF p. 21 | CTSC has two PHQ-8 measurements, baseline-to-2-year change, site/treatment/time/treatment×time, 95% CIs and P values. | CTSC outcome/model; PLANNED. |
| N114 | PDF pp. 21-22 | 25(OH)D deficiency <50 nmol/L or 20 ng/mL; anticipated prevalence about 35-40%; planned contrasts deficient/sufficient and EPA+DHA above/below median. | Biomarker unit/threshold and interaction reference groups; PLANNED. |
| N115 | PDF pp. 11, 25 | Annual DSMB; Haybittle-Peto interim z=3, p=0.0027, multiple looks; nominal-like final significance. | Interim monitoring; DEFINITION, not primary alpha. |
| N116 | PDF p. 23 Table 2 | Incident power-table denominators: total 15,470=7,244 women+8,226 men=10,071 non-Hispanic White+5,399 minority. African-American n=3,868 is a subgroup, not an additive partition. | Planned incidence power. All displayed values checked; no arithmetic contradiction. |
| N117 | PDF p. 23 Table 3 | Recurrent power-table denominators: total 2,730=1,856 women+874 men=1,777 non-Hispanic White+953 minority. African-American n=683 is a subgroup. | Planned recurrence power. Arithmetic reconciles. |
| N118 | PDF p. 23 | CTSC: 855 eligible; about 60%, n=513 high risk (513/855=60%); about 23%, n=196 subsyndromal (rounded planning value). | Planned CTSC subgroups/power; no candidate—percentages/n are approximate. |
| N119 | PDF pp. 23-24 | Expected cases about 900, about 500 with blood samples; 2:1 matching and control prevalence 35%/40%; power ≥80% for RR=1.4 and >90% for RR=1.5. | Planned biomarker power; not an observed effect. |
| N120 | PDF p. 24 | Interaction inputs: alpha .05, single-agent RR .90-.75, interaction RR 1.00-.60, ≥80% power for ≥30% added reduction. Continuous outcome: 25% meaningful difference; >99% primary/African-American D3; high-risk 30% >99%, subsyndromal 30% 90%. | Planned interaction/continuous-outcome power; not observed. |

## Inferential-statistical relationships

| ID | Direct source location | Statistical definition, relationship, and required matching conditions | Review status |
|---|---|---|---|
| S100 | PDF p. 21 | Baseline balance: 2-sample t or Wilcoxon rank-sum for continuous variables; chi-square for categorical variables. Match only to any reported baseline-comparison test with the same variable type. | MAPPED; protocol plan only. |
| S101 | PDF p. 21 | ITT Kaplan-Meier cumulative incidence/recurrence; log-rank agent-versus-corresponding-placebo comparison. Cox PH model produces HR and CI adjusted for other intervention, age, gender. Match outcome cohort, contrast, estimand (HR, not RR), adjustment, and censoring before comparison. | MAPPED; no observed statistic. |
| S102 | PDF p. 21 | Proportional-hazards assumption will be tested analytically and graphically. A reported PH test needs its own stated test/diagnostic; none is supplied here. | MAPPED; named definition absent beyond plan. |
| S103 | PDF p. 21 | Two-sided alpha=.05 applies to stated primary survival analysis. It must not be conflated with interim Haybittle-Peto p=.0027. | MAPPED; no P value. |
| S104 | PDF p. 21 | Compliance analysis censors at <2/3 medication use in preceding year; CTSC information supports misclassification sensitivity corrections to full-cohort treatment estimates/CIs. Any result needs population, censoring and correction method to match. | MAPPED; sensitivity plan only. |
| S105 | PDF p. 21 | Full-cohort PHQ mixed-effects model: four measures, treatment/time/treatment×time, correlation accounted for, mean difference and 95% CI. A numerical comparison needs exact time contrast and coefficient/contrast definition. | MAPPED; no effect estimate. |
| S106 | PDF p. 21 | CTSC continuous model: site/treatment/time/treatment×time, two repeated PHQ observations, 95% CIs and P values for two intervention main effects on baseline-to-2-year change. | MAPPED; no effect estimate. |
| S107 | PDF pp. 21-22 | Effect modification uses multiplicative interaction terms; biomarker contrasts are deficiency/sufficiency and above/below median. Parameters estimated with SAS Proc Mixed, two-sided alpha=.05. Any interaction P must match the modification variable/reference/model. | MAPPED; no P value. |
| S108 | PDF pp. 11, 25 | Haybittle-Peto repeated-look rule: interim z=3 SD / p=.0027, multiple-look adjustment; final interpretation close to nominal. This is a monitoring threshold, not a conventional reportable outcome P. | MAPPED; no displayed zero P issue. |
| S109 | PDF p. 23 Table 2 | Power is displayed by assumed RR values .90 to .60 over 5 years for incident depression and demographic subgroups. Expected RR footnote defines the row variable; percentages are power, not event risks or treatment effects. | MAPPED; planned-power table. |
| S110 | PDF p. 23 Table 3 | Same interpretation for recurrence: percentages are power by assumed RR and subgroup, not results. | MAPPED; planned-power table. |
| S111 | PDF pp. 23-24 | CTSC/nested case-control power statements specify assumed risks/RRs/control prevalence and thresholds. Compare only like planned quantities; do not treat a power percentage as an observed probability. | MAPPED; planned-power calculations. |
| S112 | PDF p. 24 | Additive interaction is labelled RR=1.00; interaction RR down to .60 and ≥30% additional risk reduction are assumed power scenarios. | MAPPED; effect-scale/interaction definition. |
| S113 | PDF p. 24 | Continuous-outcome power uses an SD of change and percentage difference relative to baseline mean of non-depressed persons. It does not provide an absolute PHQ mean difference, SE, or CI and cannot be reconciled to one without omitted inputs. | MAPPED; missing inputs explicitly named. |

## Full power-table transcription

### Table 2, incident depression over 5 years (PDF p. 23)

| Expected RR | Total | Women | Men | Non-Hispanic White | Minority | African-American |
|---:|---:|---:|---:|---:|---:|---:|
| Expected eligible participants | 15,470 | 7,244 | 8,226 | 10,071 | 5,399 | 3,868 |
| 0.90 | 52.6% | 33.5% | 24.9% | 37.3% | 22.3% | 17.2% |
| 0.85 | 86.7% | 64.3% | 49.5% | 69.9% | 44.3% | 33.6% |
| 0.80 | 98.6% | 88.1% | 74.8% | 91.8% | 68.9% | 54.6% |
| 0.75 | >99.9% | 97.8% | 91.5% | 98.9% | 87.4% | 74.8% |
| 0.70 | >99.9% | 99.8% | 98.1% | >99.9% | 96.5% | 89.1% |
| 0.65 | >99.9% | >99.9% | 99.8% | >99.9% | 99.4% | 96.5% |
| 0.60 | >99.9% | >99.9% | >99.9% | >99.9% | >99.9% | 99.2% |

Footnotes: † Expected RR; ‡ Expected total number of eligible participants.

### Table 3, recurrent depression over 5 years (PDF p. 23)

| Expected RR | Total | Women | Men | Non-Hispanic White | Minority | African-American |
|---:|---:|---:|---:|---:|---:|---:|
| Expected eligible participants | 2,730 | 1,856 | 874 | 1,777 | 953 | 683 |
| 0.90 | 38.2% | 30.8% | 12.7% | 26.7% | 16.4% | 12.9% |
| 0.85 | 70.9% | 59.6% | 23.5% | 52.6% | 31.6% | 24.0% |
| 0.80 | 92.1% | 84.1% | 38.5% | 77.7% | 51.3% | 39.2% |
| 0.75 | 98.9% | 96.1% | 55.7% | 92.9% | 70.9% | 56.5% |
| 0.70 | >99.9% | 99.5% | 72.2% | 98.6% | 85.9% | 72.9% |
| 0.65 | >99.9% | >99.9% | 85.2% | 99.8% | 94.7% | 85.6% |
| 0.60 | >99.9% | >99.9% | 93.4% | >99.9% | 98.5% | 93.6% |

Footnotes: † Expected RR; ‡ Expected total number of eligible participants.

## Candidate-screening note

One possible source-grounded label-consistency issue is flagged, without a C ID: on PDF p. 18, prose directs the reader to “Table 3” for ICD-9 depression codes, but the adjacent displayed caption is “Table 1.” It requires later exact-source recheck and ledger handling. The displayed totals and planned-table partitions otherwise reconcile; approximate language is explicit where it appears. There is no `P = 0` or equivalent display-zero relationship. Potential main-paper comparisons are listed in the paired extraction part and require population/time/contrast/model matching before any inconsistency can be considered.
