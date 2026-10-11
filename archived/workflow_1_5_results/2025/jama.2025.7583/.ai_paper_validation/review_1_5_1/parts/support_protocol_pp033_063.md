# DOC-002-PROTOCOL Support Quantitative Evidence Map: PDF Pages 33–63

## Scope and extraction record

- Direct source: `joi250033supp1_prod_1750956987.76581.pdf` (EMPROTECT protocol version 1.1, dated 06/01/2020).
- Assigned source units: PDF pages 33–63 inclusive (31 pages); no reusable per-page extraction was available.
- Fresh extraction: `pdftotext` native and `pdftotext -layout`, one output of each kind for every assigned page, at `preprocessing/DOC-002-PROTOCOL/pp033_063/page-033-{native,layout}.txt` through `page-063-{native,layout}.txt`.
- Direct-source authority: printed PDF page numbers below. Native/layout text agreed sufficiently for the mapped content; no OCR was required.
- Map convention: `P2-N` records numeric, denominator, threshold, time, or definition relationships; `P2-S` records inferential/statistical-analysis relationships. These are relationship inventory records, not candidate determinations.

## Page-completeness register

| PDF page | Section/content inspected | Mapping result |
|---:|---|---|
| 33 | Safety definitions | No result-relevant quantitative relationship; administrative safety definitions only. |
| 34 | New-fact definition and investigator role | No result-relevant quantitative relationship. |
| 35 | WHO-UMC causality table | No result-relevant quantitative relationship; ordinal causal categories only. |
| 36 | SAE definition and immediate notification | P2-N001: five qualifying SAE criteria; P2-N002: special-monitoring definition. |
| 37 | Safety reporting specifics | P2-N003: non-immediate cSDH recurrence definition begins. |
| 38 | Safety reporting specifics | P2-N003 continued; P2-N004: notification period definition. |
| 39 | SAE notification procedure | No result-relevant quantitative relationship. |
| 40 | SAE follow-up and sponsor role | No result-relevant quantitative relationship. |
| 41 | Expected device-related events | P2-N005: safety thresholds (Hb and creatinine clearance) begin. |
| 42 | Expected device/procedure-related events | P2-N005 continued. |
| 43 | Regulatory safety reporting deadlines | P2-N006: 15-day and 8-day timing rules. |
| 44 | New-fact/annual safety report/DSMB | P2-N007: 15-day new-fact follow-up and 60-day annual-report timing; no study efficacy result. |
| 45 | Data collection plan | P2-N008: collection time points T0, T1, T2. |
| 46 | Source documents/confidentiality | No result-relevant quantitative relationship. |
| 47 | Data processing | No result-relevant quantitative relationship. |
| 48 | Statistical aspects, primary endpoint plan | P2-N009, P2-S001, P2-S002, P2-S003. |
| 49 | Primary analysis continuation and secondary endpoint plan | P2-N010, P2-S002, P2-S004, P2-S005. |
| 50 | Secondary analysis and sample-size assumptions | P2-N011, P2-S006, P2-S007, P2-S008. |
| 51 | Stopping, missing data, ITT definition | P2-N012, P2-S009. |
| 52 | Monitoring/quality-control plan | No result-relevant quantitative relationship. |
| 53 | eCRF and quality procedures | No result-relevant quantitative relationship. |
| 54 | Audit/consent procedure | P2-N013: inclusion/consent timing. |
| 55 | Consent procedure | P2-N013 continued: 24-hour reflection period. |
| 56 | Compensation/legal obligations | No result-relevant quantitative relationship. |
| 57 | Legal obligations/final-report timing | P2-N014: final-report summary timing. |
| 58 | Archiving/financing/insurance | No result-relevant quantitative relationship. |
| 59 | Publication rules | P2-N015: funder acknowledgement specifies PHRC 2018; not an outcome result. |
| 60 | Bibliography references 1–9 | No result-relevant protocol relationship. |
| 61 | Bibliography references 10–19 | No result-relevant protocol relationship. |
| 62 | Bibliography references 20–24 | No result-relevant protocol relationship. |
| 63 | Addenda list | No result-relevant quantitative relationship; appendices themselves are not printed in this source. |

All 31 assigned PDF pages were inspected and explicitly recorded. Pages described as no-applicable contain no result-relevant reported value, analysis definition, or quantitative comparator within the assigned printed content.

## Numeric, threshold, timing, and definitional relationships

### P2-N001 — Serious-adverse-event qualifying criteria

- Source: DOC-002-PROTOCOL PDF p.36, section 10.2.1.
- Printed evidence: an SAE meets one of five enumerated criteria: death; life-threatening event; hospitalization/prolongation; significant/lasting disability or handicap; congenital anomaly or malformation.
- Relationship/use: definition for classifying safety counts and interpreting any reported SAE total. No SAE count is reported on this page.
- Main-paper matching key: safety/serious-adverse-event outcomes; match only after population, follow-up, and SAE definition align.

### P2-N002 — Special SAE monitoring includes fatal cSDH recurrence

- Source: DOC-002-PROTOCOL PDF p.36.
- Printed evidence: special monitoring includes “any serious adverse event with a fatal outcome” and “fatal cSDH recurrences.”
- Relationship/use: fatal recurrence is a safety-monitoring subclass, distinct from a generic recurrence endpoint unless a report specifies otherwise.
- Main-paper matching key: fatal adverse events and recurrence outcomes.

### P2-N003 — cSDH recurrence definition for non-immediate SAE reporting

- Source: DOC-002-PROTOCOL PDF pp.37–38, section 10.2.2.1.
- Printed evidence: recurrence is “greater than 10 mm or symptomatic during the study period,” or need for neurosurgical re-intervention during the study period, or re-hospitalization related to homolateral cSDH recurrence during the study period.
- Relationship/use: the three alternatives are joined by “or”; this safety-reporting definition may not be assumed identical to the primary endpoint definition without direct matching evidence.
- Main-paper matching key: cSDH recurrence at 6 months / re-intervention / hospital readmission.

### P2-N004 — SAE immediate-notification time window

- Source: DOC-002-PROTOCOL PDF pp.38–39, section 10.2.3.
- Printed evidence: notification begins on the date of the first research-specific act/procedure/examination; continues for participant follow-up; has no time limit when SAE is likely due to device or research-specific procedures.
- Relationship/use: temporal definition for safety-reporting counts, not a reported outcome period.

### P2-N005 — Expected safety-event numerical thresholds

- Source: DOC-002-PROTOCOL PDF p.41 (device procedure) and p.42 (CT angiography procedure).
- Printed evidence: puncture-site complication includes superficial hematoma with “loss of 2 Hb points” and/or transfusion; renal deterioration is persistent creatinine-clearance decrease of “more than 10 points.” The >10-point renal threshold is repeated for CT angiography.
- Relationship/use: exact thresholds for expected-event classification; source does not state a denominator, count, or observed value.
- Main-paper matching key: procedural complications, renal events, and adverse-event definitions.

### P2-N006 — Regulatory reporting deadlines for serious events

- Source: DOC-002-PROTOCOL PDF p.43.
- Printed evidence: initial report without delay for death/life-threatening qualifying events and within 15 days for other qualifying events; additional information for death/life-threatening events within eight days; in other cases within a further 15 days.
- Relationship/use: administrative timing rules only; no clinical event result.

### P2-N007 — Safety-report timing definitions

- Source: DOC-002-PROTOCOL PDF p.44.
- Printed evidence: new-fact additional information is due within a maximum of 15 days from availability; annual safety report is sent within 60 days of the anniversary date corresponding to first-patient inclusion.
- Relationship/use: administrative time measures, not clinical endpoints.

### P2-N008 — Scheduled electronic data-collection times

- Source: DOC-002-PROTOCOL PDF p.45, section 11.1.
- Printed evidence: “Data at T0, T1 and T2 will be collected electronically.”
- Relationship/use: establishes three scheduled eCRF time labels but does not define their calendar equivalents on this page. It cannot alone establish which reported result is at 1 or 6 months.
- Main-paper matching key: baseline and follow-up result time points; requires definition alignment.

### P2-N009 — Interim-analysis information size and timing

- Source: DOC-002-PROTOCOL PDF p.48, section 12.1.
- Printed evidence: interim analysis at 6-month follow-up of 129 included patients (37.5%), approximately 15 months after start (9 months inclusion + 6 months follow-up); the primary endpoint is analyzed in two stages.
- Relationship/use: planned interim sample/information fraction and calendar schedule, not a realized enrollment/result count.
- Main-paper matching key: trial enrollment, interim analysis, primary recurrence endpoint at 6 months.

### P2-N010 — Primary-analysis endpoint and outcome handling

- Source: DOC-002-PROTOCOL PDF pp.48–49.
- Printed evidence: primary endpoint is cSDH recurrence rate; interim population includes randomized patients with recoverable 6-month recurrence status in initially allocated group; patients dying without recurrence are considered failures. Final primary analysis uses ITT population; same death-without-recurrence handling. Sensitivity analysis excludes experimental-arm patients not receiving embolization after CT angiography; two subgroups are uni/bilateral cSDH and anticoagulant/antiplatelet use.
- Relationship/use: defines endpoint time/status and planned sensitivity/subgroup contrast. It is a protocol plan, not an observed recurrence rate.
- Main-paper matching key: primary recurrence outcome, ITT set, death handling, sensitivity and subgroup analyses.

### P2-N011 — Sample-size arithmetic and assumptions

- Source: DOC-002-PROTOCOL PDF p.50, section 12.2.
- Printed evidence: planned control recurrence 15%; embolized-group recurrence 5%; 80% power; two-sided overall alpha 5%; 142 patients per group required; assumed 20% lost to follow-up; total 342 (171 per group) required.
- Direct arithmetic diagnostic: 142 × 2 = 284 analyzed patients. With 20% attrition, 284 / (1 − 0.20) = 355, not 342; 342 × 0.80 = 273.6. This record preserves the printed protocol values and the reproducible relationship for later checking; it does not adjudicate the discrepancy because sequential-design conventions and the exact calculation inputs may affect the stated number.
- Main-paper matching key: planned sample size, recruitment target, primary recurrence assumptions.

### P2-N012 — Planned stopping and missing-data rules

- Source: DOC-002-PROTOCOL PDF pp.50–51, sections 12.4–12.5.
- Printed evidence: interim after 129 included/followed patients; inclusion may stop for a between-group difference at 0.001 or low conditional power. Main analysis is ITT; all randomized participants remain in originally assigned arm; multiple imputation is planned for unevaluable primary-endpoint patients.
- Relationship/use: planned discontinuation/missing-data definitions; distinguish from realized analysis and denominators.
- Main-paper matching key: interim stopping, ITT analysis population, primary-endpoint missing-data handling.

### P2-N013 — Inclusion/consent timing

- Source: DOC-002-PROTOCOL PDF pp.54–55, section 14.1.
- Printed evidence: screening occurs within 7 days of cSDH evacuation surgery during same hospitalization; a 24-hour reflection period is allowed from information to consent signature; consent is before inclusion during same hospitalization.
- Relationship/use: eligibility/inclusion timing definition; no enrollment count.
- Main-paper matching key: timing of treatment/randomization/inclusion.

### P2-N014 — Final-report submission timing

- Source: DOC-002-PROTOCOL PDF pp.57–58, section 15.6.
- Printed evidence: final report summary sent within one year of end of research, defined as end of last participant’s participation.
- Relationship/use: administrative timing only.

### P2-N015 — Funder-year label

- Source: DOC-002-PROTOCOL PDF p.59, section 17.3.
- Printed evidence: protocol’s requested acknowledgement says study funded by PHRC 2018 (Ministry of Health).
- Relationship/use: funder/year metadata; not a quantitative outcome. Can be matched to manuscript funding text only as an identity label.

## Inferential/statistical relationships

### P2-S001 — Planned descriptive-statistics convention

- Source: DOC-002-PROTOCOL PDF p.48.
- Printed evidence: qualitative variables: number, percentage, and missing data by response modality; quantitative variables: number, mean, SD; non-normal quantitative variables: median and IQR (first to third quartile), by group and evaluation date.
- Main-paper matching key: descriptive table statistics and missing-data display; match group, time point, and distribution convention.

### P2-S002 — Primary recurrence model and fallback

- Source: DOC-002-PROTOCOL PDF pp.48–49.
- Printed evidence: recurrence by group analyzed with mixed logistic model adjusted for stratification factors; fixed effects are randomization group, anticoagulant/antiplatelet use, and uni/bilateral cSDH; center is random effect. If nonconvergence, use Mantel-Haenszel adjusted for center and, if possible, other stratification factors.
- Main-paper matching key: adjusted primary effect estimate/model, covariates, and analysis population. Model/estimand must match before comparing numerical effects.

### P2-S003 — Sequential alpha-spending plan

- Source: DOC-002-PROTOCOL PDF pp.48–49.
- Printed evidence: two-stage Lan & DeMets approach using O’Brien & Fleming alpha-spending function; interim nominal alpha = 0.001; final conventional alpha = 0.05 because the low interim level yields “virtual absence” of alpha inflation.
- Main-paper matching key: primary-endpoint P value, confidence level, and interim/final analysis designation.

### P2-S004 — Secondary dependency outcome model

- Source: DOC-002-PROTOCOL PDF pp.49–50.
- Printed evidence: dependent proportion (Rankin score ≥4) at 1 and 6 months compared using GEE logistic model with patient cluster effect; parameters are arm, visit as class, and visit-by-arm interaction; interactions evaluate between-arm difference at each month.
- Main-paper matching key: modified Rankin/dependency results at 1 and 6 months, effect model, threshold ≥4.

### P2-S005 — Other secondary-endpoint tests

- Source: DOC-002-PROTOCOL PDF p.50.
- Printed evidence: mortality at 1 and 6 months, cumulative hospital stay at 6 months, 6-month re-intervention rate, and complication rate compared by group; quantitative endpoints use Student t test or Wilcoxon if non-normal; qualitative criteria use chi-square or Fisher exact as appropriate. Adverse events at 1 and 6 months described globally/by group as number, frequency, percentage; SAEs separately.
- Main-paper matching key: corresponding secondary outcomes/tests and AE display.

### P2-S006 — Power and planned effect calculation

- Source: DOC-002-PROTOCOL PDF p.50.
- Printed evidence: planned 15% versus 5% recurrence comparison, 80% power, overall two-sided alpha 5%, sequential Lan–DeMets/O’Brien–Fleming scheme.
- Relationship/use: prospective power/sample-size assumption, not a test of realized study results. Cross-source comparison requires recognizing protocol versus published estimand and any amendment.

### P2-S007 — Expected significance thresholds

- Source: DOC-002-PROTOCOL PDF p.50, section 12.3.
- Printed evidence: all analyses at 5% two-sided alpha except interim at nominal 0.001 from 129 patients.
- Main-paper matching key: reported P-value interpretation and confidence interval convention.

### P2-S008 — Futility/stopping decision rule

- Source: DOC-002-PROTOCOL PDF pp.49–51.
- Printed evidence: conditional power estimated at interim; project may discontinue for too-low conditional power after DSMB consultation; efficacy stopping may occur at 0.001 threshold.
- Main-paper matching key: any early termination statement or analysis cohort; requires evidence of realized DSMB decision.

### P2-S009 — ITT and multiple-imputation analysis plan

- Source: DOC-002-PROTOCOL PDF p.51.
- Printed evidence: ITT includes all randomized patients in their initially assigned arm and is the main analysis; multiple imputation planned for participants not evaluable for primary endpoint.
- Main-paper matching key: published analysis-set label, missing primary outcome handling, randomized denominators.

## Mapping limitations

- This assigned source segment is a protocol/safety/administrative section. It reports planned methods, definitions, assumptions, and regulatory timing rather than observed trial results.
- Addenda listed on p.63 are not printed as pages in the supplied 63-page PDF; no unprinted appendix content was inferred.
- No candidate diagnosis or legacy audit material was consulted. The arithmetic diagnostic in P2-N011 is retained solely as a source-grounded relationship for the designated checking stages.
