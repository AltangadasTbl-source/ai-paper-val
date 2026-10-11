# Support Quantitative Evidence Map — DOC-003 pp. 82-162

## Scope and method

- **Source:** `joi250072supp2_prod_1761000786.6938.pdf`, direct PDF pages 82-162 (81 pages).
- **Fresh extraction:** `pdftotext -layout` was run for the complete range. Its text is character-encoded and unusable for trustworthy transcription. Every page was therefore directly rendered to PNG under `preprocessing/manual_082_162/`; visual page inspection was used for the result-relevant definitions/tables below. Targeted CPU OCR was attempted but did not yield usable text within the runtime limit; it is not relied on here.
- **Nature of source:** GDB Manual of Operations content. It contains data-collection definitions, coding rules, operational algorithms and worksheets. It contains no paper-level participant results, effect estimates, confidence intervals, hypothesis tests, P values, or model outputs in this shard.
- **Cross-source matching:** Match only after registry/form identity, population, time point, and definition agree. The manual's GDB population and forms must not be presumed identical to the paper population.

## Result-relevant quantitative relationships and definitions

| Provisional ID | Exact PDF page(s) | Direct source observation | Population / unit / time / measure | Cross-source match key |
|---|---:|---|---|---|
| MAN2-N001 | 84 | GDB eligibility is inborn infants at gestational age 21 0/7 through 27 6/7 weeks inclusive (<28 weeks). Death before NICU admission does not prevent posthumous enrollment when the stated inborn/liveborn criteria are met. | Infant; gestational age in completed weeks/days; enrollment. | `GDB eligibility; 21+0–27+6 weeks; <28 weeks` |
| MAN2-N002 | 84 | If an infant dies in 12 hours or less, replace NG03 with NG03E and do not enter NG07. | Infant; time from birth in hours; form-completion rule. | `NG03E; death <=12 h; NG07` |
| MAN2-N003 | 85 | Date format is mm/dd/yyyy; time is 24-hour clock beginning at 00:00. Birth weight is recorded in grams; gestational age is recorded in weeks and days. If menstrual-period dating disagrees with neonatologist estimate by more than 2 weeks, use the neonatologist estimate. | Maternal/infant record; date/time; grams; weeks/days. | `birth weight g; GA weeks/days; discrepancy >2 weeks` |
| MAN2-N004 | 86-87 | Network ID is 6 digits: a 5-digit family ID plus 1-digit birth order; birth order begins 1 for singleton/first born, then 2, 3, etc. The worked example 688751 = family ID 68875 + birth order 1 is a formatting example, not a clinical result. | Identifier; digits; multiple birth. | `Network ID 6 digits; family ID 5 digits; birth order` |
| MAN2-N005 | 88 | Parity is pregnancies reaching 20 weeks and 0 days or beyond, rather than number of fetuses/outcomes. Example: first twins each have parity 1; a subsequent delivery gives parity 2. | Pregnancy; gestational-age threshold; parity definition. | `parity >=20+0 weeks` |
| MAN2-N006 | 99-101 | NG03 status coding specifies: home discharge=1; still hospitalized at 120 days=2; transfer without return within 7 days=3; death=5. Weight, length and head circumference use the status day where possible, or within 7 days. Discussion to limit/withdraw/not escalate care is coded based on documentation prior to 120 days. | Infant clinical outcome; 120-day outcome; 7-day window; g/cm. | `NG03; status at 120 days; transfer 7 days; death` |
| MAN2-N007 | 102-105 | Outcome-form definitions distinguish chronic lung disease/respiratory support and specify completion of outcome data at 120 days or disposition; oxygen/respiratory modality and related time/date fields are collection variables, not observed trial results. | Infant; respiratory support; 120 days/disposition. | `NG03 respiratory outcome; 120 days` |
| MAN2-N008 | 106-112 | Cranial imaging rules include MRI after day 28 and selection of the imaging study closest to 36 weeks postmenstrual age; recorded abnormalities use specified diagnostic definitions and laterality. | Infant imaging; day 28; 36 weeks PMA; right/left/both. | `MRI after day 28; imaging closest 36 weeks PMA` |
| MAN2-N009 | 113-121 | The manual continues outcome-form definitions and coding for neonatal morbidities, procedures, infections, surgery, and discharge-related measures. These pages define collection categories and time anchors; no aggregated counts, rates, or inferential results are printed. | Infant clinical record; event/date/category. | `NG03 outcome definitions; event/date` |
| MAN2-N010 | 122-130 | Follow-up and outcome documentation pages define age/time windows, source-record rules, and form fields. They provide no cohort denominators, summary outcomes, effect estimates, or P values. | Infant follow-up; form-specific age/time windows. | `GDB follow-up form/time window` |
| MAN2-N011 | 131-148 | Appendices/form instructions contain diagnosis/coding definitions and operational documentation requirements. They are potential definition locators only; no paper-result relationship is printed. | Registry coding; diagnosis/date/category. | `GDB coding appendix` |
| MAN2-N012 | 149 | Oxygen reduction challenge: feeds/medications 30 minutes before evaluation; rest 5 minutes before baseline. Hood oxygen reduces FiO2 by 2% every 5 minutes. For nasal cannula at >=22%, flow decreases 0.5 L/min every 5 minutes to 0.5 L/min, then 0.1 L/min every 5 minutes to 0.1 L/min; specified room-air cannula rules use 2.0 and 0.5 L/min increments. Continue reduction if saturation >=90% during 5 minutes; stop if <90% for 5 continuous minutes or <80% for 15 seconds. | Infant oxygen challenge; FiO2 %, flow L/min, saturation %, minutes/seconds. | `oxygen reduction challenge; saturation 90%; 5 min; 80%; 15 sec` |
| MAN2-N013 | 150 | Room-air phase monitors 30 minutes. Passing requires saturation >=90%; RAPID PASS requires all saturations >=96% in room air for 15 consecutive minutes. Failure triggers are saturation <90% for 5 continuous minutes or <80% for 15 seconds. Result/date are recorded on NG07 B.3. | Infant oxygen challenge; saturation %, room air, 30/15/5 minutes, 15 seconds. | `NG07 B.3; rapid pass >=96% for 15 min` |
| MAN2-N014 | 151 | Checklist operationalizes the oxygen challenge, including 33 weeks' gestation and oxygen/flow/saturation eligibility items. It is a checklist, not a count or tested result. | Infant; challenge eligibility; weeks, FiO2/flow/saturation. | `oxygen challenge checklist; 33 weeks` |
| MAN2-N015 | 152-154 | Effective FiO2 conversion tables map nasal-cannula flow and infant weight to a factor, then factor plus current oxygen concentration to effective FiO2. Exact absent values round to nearest; exact halfway values round up. Table 1 covers flows 0.01-6.0 L/min and weights 0.7-4 kg. | Infant; weight kg; flow L/min; factor; effective FiO2 %. | `effective FiO2 table; nasal cannula; flow/weight` |
| MAN2-N016 | 155 | Worked conversion: weight 2.0 kg and flow 0.15 L/min gives factor 8; factor 8 with 100% oxygen gives effective FiO2 27%; 27% is <30%, so the infant is eligible for physiologic evaluation. | Infant; 2.0 kg; 0.15 L/min; FiO2 27% vs 30% threshold. | `effective FiO2 27%; physiologic evaluation <30%` |
| MAN2-N017 | 156-158 | Oxygen-reduction worksheets are blank data-collection tables with flow, saturation, minute, and timepoint fields. They do not report observed data or totals. | Infant worksheet; minute/time; flow/saturation. | `oxygen challenge worksheet` |
| MAN2-N018 | 159-161 | Reference/coding pages list protocol-related terms, medication/complication categories, and data-coordinator contact instructions. They contain no result-relevant numerical relationship beyond labels/codes. | Registry administration; labels/codes. | `GDB reference/coding` |
| MAN2-N019 | 162 | Resource/support page directs staff to companion GDB manuals and does not contain quantitative result content. | Administrative support. | `GDB companion manuals` |

## Inferential-statistical inventory

No inferential statistical relationship is present on pp. 82-162. Consequently no `MAN2-S` record is applicable. Numeric thresholds and conversion rules are retained as `MAN2-N` records above; they are operational definitions, not statistical analyses.

## Page-by-page coverage

| PDF page | Coverage determination |
|---:|---|
| 82 | Administrative/regulatory manual text; no result-relevant quantitative relationship. |
| 83 | Administrative/regulatory manual text; no result-relevant quantitative relationship. |
| 84 | Mapped: eligibility, <28-week criterion, <=12-hour form rule (MAN2-N001-N002). |
| 85 | Mapped: date/time, weight/GA units and >2-week hierarchy (MAN2-N003). |
| 86 | Mapped: identifier digit construction (MAN2-N004). |
| 87 | Mapped: identifier example and masked-trial data rules (MAN2-N004). |
| 88 | Mapped: parity >=20+0-week definition (MAN2-N005). |
| 89 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 90 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 91 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 92 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 93 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 94 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 95 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 96 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 97 | Baseline-form coding continuation; no distinct result relationship beyond data-definition scope. |
| 98 | Outcome-form transition; no distinct result relationship beyond data-definition scope. |
| 99 | Mapped: outcome form timing/definitions (MAN2-N006). |
| 100 | Mapped: 120-day status and 7-day measurement rules (MAN2-N006). |
| 101 | Mapped: outcome-form timing/definitions (MAN2-N006). |
| 102 | Mapped: respiratory outcome collection definition (MAN2-N007). |
| 103 | Mapped: respiratory outcome collection definition (MAN2-N007). |
| 104 | Mapped: respiratory outcome collection definition (MAN2-N007). |
| 105 | Mapped: respiratory outcome collection definition (MAN2-N007). |
| 106 | Mapped: imaging/outcome definition (MAN2-N008). |
| 107 | Mapped: imaging/outcome definition (MAN2-N008). |
| 108 | Mapped: imaging/outcome definition (MAN2-N008). |
| 109 | Mapped: imaging/outcome definition (MAN2-N008). |
| 110 | Mapped: MRI after day 28/closest to 36-week PMA rule (MAN2-N008). |
| 111 | Mapped: imaging/outcome definition (MAN2-N008). |
| 112 | Mapped: imaging/outcome definition (MAN2-N008). |
| 113 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 114 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 115 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 116 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 117 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 118 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 119 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 120 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 121 | Mapped: morbidity/procedure outcome definitions (MAN2-N009). |
| 122 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 123 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 124 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 125 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 126 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 127 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 128 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 129 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 130 | Mapped: follow-up form/time-window definitions (MAN2-N010). |
| 131 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 132 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 133 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 134 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 135 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 136 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 137 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 138 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 139 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 140 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 141 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 142 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 143 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 144 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 145 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 146 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 147 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 148 | Mapped: coding appendix; no paper-result relationship (MAN2-N011). |
| 149 | Mapped: oxygen-reduction algorithm (MAN2-N012). |
| 150 | Mapped: room-air pass/fail and RAPID PASS thresholds (MAN2-N013). |
| 151 | Mapped: oxygen challenge checklist (MAN2-N014). |
| 152 | Mapped: effective FiO2 Table 1 and rounding rule (MAN2-N015). |
| 153 | Mapped: effective FiO2 Table 2; continuation of MAN2-N015. |
| 154 | Mapped: conversion-table continuation/example; continuation of MAN2-N015. |
| 155 | Mapped: 2.0-kg/0.15-L/min worked conversion (MAN2-N016). |
| 156 | Mapped: blank oxygen-reduction worksheet (MAN2-N017). |
| 157 | Mapped: blank oxygen-reduction worksheet (MAN2-N017). |
| 158 | Mapped: blank oxygen-reduction worksheet (MAN2-N017). |
| 159 | Mapped: reference/coding labels; no result relationship (MAN2-N018). |
| 160 | Mapped: reference/coding labels; no result relationship (MAN2-N018). |
| 161 | Mapped: reference/coding labels; no result relationship (MAN2-N018). |
| 162 | Mapped: administrative companion-resource page (MAN2-N019). |

## Limitations

Native text is character-encoded; rendered direct-PDF pages, rather than the corrupt extraction, are authoritative for the values transcribed above. The attempted local OCR was unusable and was not substituted for visual source confirmation. This shard maps supplied support evidence only and does not diagnose a candidate or make a cross-source identity claim.
