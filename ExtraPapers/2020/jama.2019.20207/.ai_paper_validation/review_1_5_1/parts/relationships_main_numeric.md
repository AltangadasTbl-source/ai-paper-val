# Provisional Main Numeric Relationship Inventory — DOC-001

Scope: DOC-001 PDF pages 1-9. These are extraction-stage provisional numeric relationship IDs (`M-N`), not canonical IDs and not candidate IDs.

| Provisional ID | Relationship | Exact direct-source location(s) | Key population, unit, time, contrast, or matching occurrence |
|---|---|---|---|
| M-N001 | Trial population and allocation | PDF pp. 1, 4 | 478 randomized at 91 sites; intervention 237, control 241; 443 eligible primary set; enrollment 2011-2015 and 24-month follow-up 2013-2017. |
| M-N002 | Baseline abstract descriptives | PDF p. 1 | Age 64 (7) years; PSA 4.9 (2.1) ng/mL among 478 randomized. |
| M-N003 | Composite progression event counts | PDF pp. 1, 5 | 245 total events: 124 intervention and 121 control; TTP population 443. |
| M-N004 | 24-month progression-free percentages | PDF pp. 1, 5, Fig. 2A p. 6 | Kaplan-Meier percentage, intervention versus control: 43.5% versus 41.4%; difference 2.1 percentage points. |
| M-N005 | Randomization strata | PDF p. 2 | Age, race/ethnicity, and diagnostic-biopsy timing definitions. |
| M-N006 | Eligibility thresholds | PDF p. 2 | Age, stage, pathology, PSA, biopsy-volume, and dietary-intake thresholds. |
| M-N007 | No applicable result unit | PDF p. 2 | Background and setup only. |
| M-N008 | Intervention dose and assessment schedule | PDF p. 3 | Seven servings/d target; phase call counts/timing; dietary/plasma assessment time points. |
| M-N009 | Progression definition and censoring | PDF p. 3 | PSA, PSADT, and pathology thresholds; time from random assignment. |
| M-N010 | Design sample-size quantities | PDF p. 3 | α, planned N, power, progression risks, required events, HR design value, dropout and target enrollment. |
| M-N011 | Analysis-set definition | PDF p. 3 | Primary set excludes later ineligible participants; all-randomized ITT supportive set; censoring. |
| M-N012 | Figure 1 patient flow | PDF p. 4, Fig. 1 | 602 assessed; 124 excluded; 478 randomized; arm receipt, analyzed, and exclusion counts. |
| M-N013 | Figure 1 detailed eligibility exclusions | PDF p. 4, Fig. 1 footnotes | Exact reasons and counts by arm. |
| M-N014 | Per-protocol population | PDF pp. 4-5 | 183/226 (81.7%) versus 171/217 (79.5%). |
| M-N015 | Table 1 age/race/region | PDF p. 5, Table 1 | Arm-specific counts, denominators, percentages, means, medians, SD/IQR. |
| M-N016 | Table 1 BMI/biopsy/stage/PSA | PDF p. 5, Table 1 | Variable-specific denominators and baseline descriptors. |
| M-N017 | Completion, biopsy, and descriptive narrative | PDF p. 5 | Noncompletion counts/percentages, mean values, African American and grade-group totals, PSA count, 24-month biopsy proportion. |
| M-N018 | Primary and biopsy-only progression outcome | PDF p. 5 | Composite and upgrading-only event totals, survival percentages, differences, and censoring counts. |
| M-N019 | Active-treatment outcome | PDF p. 5 | Counts/percentages, 24-month horizon, and treatment-type missingness statement. |
| M-N020 | Narrative diet results | PDF p. 5 | 12- and 24-month analyte changes, analysis counts, units, and arm contrast. |
| M-N021 | Figure 2 risk sets and follow-up | PDF p. 6, Fig. 2 | At-risk counts at 0/6/12/18/24 months; panel-specific follow-up medians and IQRs. |
| M-N022 | Plasma-carotenoid biomarker | PDF p. 6 | Baseline and 12-month log-μmol/L means/CIs and sample sizes. |
| M-N023 | Main conclusion quantitative claim | PDF p. 6 | Narrative non-significant clinical-progression conclusion tied to primary result. |
| M-N024 | Table 2 energy | PDF p. 7, Table 2 | Baseline mean (SD), 12/24-month arm changes/CIs/P values, and between-arm difference. |
| M-N025 | Table 2 vegetable serving rows | PDF p. 7, Table 2 | Dark green, deep yellow, tomatoes, legumes, and other vegetables. |
| M-N026 | Table 2 cruciferous and total vegetables | PDF p. 7, Table 2 | Separate g/d and servings/d cruciferous rows; total vegetables servings/d. |
| M-N027 | Table 2 meat and fat rows | PDF p. 7, Table 2 | Red meat, total fat, saturated fat. |
| M-N028 | Table 2 carotenoid rows | PDF p. 7, Table 2 | Lycopene and total dietary carotenoids. |
| M-N029 | Conclusion match | PDF pp. 1, 6, 8 | Non-significant primary conclusion repeated in abstract, discussion, and conclusion. |
| M-N030 | No additional applicable result unit | PDF p. 8 | Article information and references only after conclusion. |
| M-N031 | No applicable result unit | PDF p. 9 | References only. |

## Potential consistency observations for downstream checking

These observations preserve exact comparators without making an adjudication or assigning a candidate identifier.

1. **M-N012 flow arithmetic:** Figure 1 has internal numeric identities to reproduce: 602−124=478; 237+241=478; 237−11=226; 241−24=217; 226+217=443; 11+24=35; and 478−35=443. Arm-specific exclusion subcategories also sum to displayed arm exclusions (9+2=11; 19+5=24; and the detailed retrospective counts sum to 2 and 5).
2. **M-N003/M-N018 event arithmetic:** 124+121=245. Deaths 1+3=4 and elective-treatment withdrawals 3+2=5 match printed totals. These are distinct censoring categories from progression events.
3. **M-N015/M-N016 denominators:** Table 1 explicitly changes denominators by variable: race/ethnicity 226/216, BMI 55/53, stage 225/217, and PSA 224/217. The downstream checker should retain these stated denominators rather than assume 226/217 across every table row.
4. **M-N016 visible PSA-category total:** The direct Table 1 display has a PSA denominator of 224 intervention and 217 control, but the two visible PSA categories, 0-2.5 and >2.5-5 ng/mL, sum to 124 and 128, respectively. The downstream checker should inspect whether omitted higher PSA categories are intentionally outside the printed table or whether the displayed categorical rows are expected to exhaust the stated denominators; no resolution is made here.
5. **M-N020/M-N026 unit wording:** The p. 5 correlative narrative says “cruciferous servings” while printing the 12-month change `43.10 g/d` and control change `6.44 g/d`; Table 2 p. 7 labels the matched row “Cruciferous, g/d.” The printed numerical values and unit agree with the g/d Table 2 row; the wording-to-unit pairing merits an exact-label check across narrative and table.
6. **M-N020/M-N026/M-N028 matched diet values:** The p. 5-6 narrative values match Table 2 for total vegetables, cruciferous g/d, cruciferous servings/d, and total carotenoids at both time points under the table’s mixed-model definition. Compare using the table’s rounded display precision and distinct unit rows.
7. **M-N004/M-N018/M-N021 survival versus event count:** The 24-month Kaplan-Meier progression-free percentages are time-to-event estimates, while 245 is the total observed composite event count; they must not be checked as simple complements using the 443 analysis denominator because of varying follow-up/censoring.
