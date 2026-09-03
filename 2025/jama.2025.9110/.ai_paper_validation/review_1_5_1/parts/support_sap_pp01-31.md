# D03 SAP fresh direct-source quantitative evidence map

Source: `joi250040supp2_prod_1753124024.37799.pdf`, PDF pp. 1-31. Fresh page renders were made in `preprocessing/sap-001/`; native PDF text is font-encoded/garbled and was not used as authority. Printed-page evidence is authoritative. This SAP is a prospective analysis specification, not a results source; no observed trial-result table is present.

## Page-by-page coverage

| PDF page | Coverage and extracted content |
|---:|---|
| 1 | Title/authors; no result-relevant quantitative relationship. |
| 2 | Abstract: eight ICUs; 1:1 formula allocation; 3-month periods, 12-month duration; primary days free of index hospital and alive at day 90; secondary outcome list; planned 95% CIs; 3,412 enrolled. |
| 3 | Background and trial rationale; no trial result. |
| 4 | Background and SAP supersedes protocol/registry; external-study contextual values only. |
| 5 | External-study contextual protein doses and sample sizes; no TARGET result. |
| 6 | Background continuation; no TARGET result. |
| 7 | External trial context: PRECISE n=935; high dose 2-2.4 g/kg/day versus usual 0.8-1.2 g/kg/day; no TARGET result. |
| 8 | Design: 8 ICU clusters; 4 allocated to each sequence; four 3-month periods/12 months; patient exposure until day 90, ICU discharge, or death. |
| 9 | Eligibility: age >=16; EN at index/subsequent ICU admission; exclude contraindication, >12 h non-trial formula, prior participation; planned CONSORT counts. |
| 10 | Formula contents: augmented 100 g protein/1000 mL, 1260 kcal/1000 mL; usual 63 g/1000 mL, 1250 kcal/1000 mL. Primary outcome formula: 90 minus in-hospital/readmission days within 90; midnight rule; death through day 90 assigned 0. |
| 11 | Primary examples: discharge day 30 -> 60; discharge day 92 censored day 90 -> 0; death by day 90 -> 0. Secondary: survivor-only primary analogue, alive day 90, invasive ventilation hours. |
| 12 | Secondary definitions: ventilation, ICU/hospital length of stay, tracheostomy, renal replacement therapy, discharge destination. |
| 13 | Analysis populations, descriptive baseline/flow reporting, treatment delivery; no observed results. |
| 14 | General analysis: intention-to-treat; cluster/crossover and period adjustment; 95% CI and two-sided significance convention. |
| 15 | Primary-model specification: mixed-effects regression for days-free outcome with treatment, period and cluster structure; model estimates adjusted mean difference and 95% CI. |
| 16 | Primary-model diagnostics/alternative model provisions; no results. |
| 17 | Alive-at-day-90 analysis: mixed-effects logistic model; odds ratio, 95% CI, treatment/period/cluster terms. |
| 18 | Survivor-only days-free analysis: same mixed-model framework; population restricted to day-90 survivors. |
| 19 | Ventilation and length-of-stay analyses: mixed-effects models; skew/distribution handling specified. |
| 20 | Binary secondary outcomes (tracheostomy/RRT/discharge destination): mixed-effects logistic models, OR and 95% CI. |
| 21 | Prespecified subgroup/effect-modification analyses; interaction terms and 95% CI; multiplicity interpretive caution. |
| 22 | Sensitivity analyses including alternative adjustment/period and missing-data handling; no results. |
| 23 | Missing-data specifications and linkage-based outcome ascertainment; no results. |
| 24 | Safety/adverse-event and protocol-deviation descriptive reporting plan; no results. |
| 25 | Planned presentation tables/figures and CONSORT flow; no observed values. |
| 26 | Statistical software, reproducibility, and reporting conventions; no results. |
| 27 | Administrative declarations; no applicable quantitative result. |
| 28 | References only; no applicable quantitative result. |
| 29 | References only; no applicable quantitative result. |
| 30 | References only; no applicable quantitative result. |
| 31 | References only; no applicable quantitative result. |

## Relationship inventory

- **SAP-N001** (pp. 2, 8): eight clusters, 1:1 sequence allocation, 3-month periods, four periods/12 months; cluster is randomization unit and patient is analysed once.
- **SAP-N002** (p. 2): enrolment statement is 3,412 patients; this is a planned-SAP administrative count requiring matched main-paper comparison only after population/time match.
- **SAP-N003** (p. 10): formula composition contrast is 100 vs 63 g protein/1000 mL and 1260 vs 1250 kcal/1000 mL.
- **SAP-N004** (pp. 10-11): primary scale is 0-90 days; value = 90 minus qualifying index-hospital/readmission days, with death by day 90 = 0; worked examples confirm day-30 discharge=60 and day-92 discharge=0.
- **SAP-N005** (pp. 11-12): secondary outcome definitions distinguish survivor-only days free, day-90 alive proportion, ventilation duration (hours), ICU/hospital LOS, tracheostomy, RRT and discharge destination.
- **SAP-S001** (pp. 14-16): primary planned estimand is adjusted treatment mean difference with 95% CI under a mixed-effects model accounting for cluster, period and crossover structure.
- **SAP-S002** (p. 17): day-90 survival planned effect measure is OR with 95% CI from mixed-effects logistic regression.
- **SAP-S003** (pp. 18-20): survivor-only, duration and binary-secondary models retain population/outcome-specific mixed-model definitions; binary outcomes use OR/95% CI.
- **SAP-S004** (pp. 21-23): subgroup interaction and sensitivity/missing-data analyses are planned; no result/P value is reported here.

## Candidate seeds and display-zero check

No SAP-only candidate seed registered. This support document supplies plans/definitions, not observed effect estimates or result tables. No `P = 0`/equivalent display-zero relationship observed; `DISPLAY_ZERO_NOT_CANDIDATE` not applicable.

## Limitations

Direct pages were visually inspected from fresh CPU-rendered derivatives; initial native extraction is character-encoded. No OCR transcription is relied on for a candidate. Pages 27-31 are administrative/reference-only and explicitly mapped as no-applicable.
