# Support quantitative mapping — DOC-002 pp. 61-90

## Scope and direct-source method

- **Source:** `joi250084supp1_prod_1765403089.61351.pdf`, PDF pp. 61-90 (30 fresh-required direct-source pages).
- **Direct extraction:** `pdftotext` and `pdftotext -layout` for pp. 61-90, stored respectively as `preprocessing/DOC-002/p061-p090/native.txt` and `preprocessing/DOC-002/p061-p090/layout.txt`.
- **Visual confirmation:** CPU page renders were made in `preprocessing/DOC-002/p061-p090/`. The PDF has glyph-encoded native/layout text for this scope; rendered direct source was therefore used to transcribe the readable forms and definitions below. CPU Tesseract was attempted on the rendered pages but did not complete within a bounded invocation; it is not relied upon.
- **Scope character:** These pages are protocol instruments, data-collection forms, and operational/safety material. They contain no participant-level results table, analyzed effect estimate, confidence interval, P value, or reported arm comparison.

## Result-relevant numeric and statistical relationships

### D2C-N01 — DPP/usability acceptability questionnaire scoring

- **Source locations:** DOC-002 PDF p. 61 (items 19-32 and scoring box; continuation of the questionnaire).
- **Population/time/contrast:** Participant experience with the Sweetch app or the in-person DPP; instrument administration timing is not stated on this page. The bracketed wording distinguishes the digital and in-person versions; this is not an analyzed between-arm comparison.
- **Measure and scale:** Items 1-31 use a 1-5 response scale. The displayed scoring instruction is: sum item responses 1-31, divide by 155, then multiply by 100. Thus the displayed percentage score has an attainable range of 20% (lowest acceptability) to 100% (highest acceptability).
- **Relationship:** `acceptability percentage = (sum of 31 item scores / 155) × 100`; the maximum denominator 155 equals 31 × 5. Item 32 is free text and is outside the score.
- **Mapping status:** Definition/formula only; no observed questionnaire values or analytic summary is printed.

### D2C-N02 — Sweetch app features questionnaire and Net Promoter Score definition

- **Source locations:** DOC-002 PDF pp. 62-63.
- **Population/time/contrast:** Sweetch digital DPP app users; item 14 is explicitly for interest in a wearable tracker. No reported arm result is present.
- **Measure and scale:** A 23-item questionnaire. Items 1-21 use a 1-5 agreement scale; reverse-keyed items visibly use the order 5,4,3,2,1. Item 23 asks recommendation likelihood on a 0-10 scale.
- **Relationship A:** `app usability/acceptability percentage = (sum items 1-21 / 105) × 100`, with stated possible range 20%-100%; 105 equals 21 × 5. Item 22 is free text and is not in that score.
- **Relationship B:** Net Promoter Score is defined from item 23 as `% promoters − % detractors`; scores 0-6 are detractors, 7-8 passive, and 9-10 promoters. The page does not state whether passives are excluded from either percentage, although that is the usual implication of the written definition; preserve that definition question if this protocol instrument is used in later matching.
- **Mapping status:** Definitions/formulas only; no response counts, percentages, or NPS result is printed.

### D2C-N03 — WHO-5 well-being index scoring

- **Source locations:** DOC-002 PDF pp. 63-64.
- **Population/time:** The five WHO-5 statements refer to feelings over the past 2 weeks.
- **Measure and scale:** Five positive well-being statements each have values 5,4,3,2,1,0 for all of the time through at no time.
- **Relationship:** Raw total is 0-25; multiply raw total by 4 to obtain a 0-100 score, where 0 represents worst imaginable well-being and 100 best imaginable well-being. The multiplier is consistent with the stated range.
- **Mapping status:** Instrument definition only; no recorded score or longitudinal change is printed.

### D2C-N04 — Local DPP session and participant data collection fields

- **Source locations:** DOC-002 PDF pp. 65-66.
- **Population/time:** Participating DPPs enter session-level data for referred participants in a REDCap electronic data-capture form.
- **Definitions/units:** Delivery mode codes 1=in-person, 2=online (not permitted for the trial), 3=distance learning (synchronous video/phone conference only). Session type codes are C=core, CM=core maintenance, MU-C=core make-up, and MU-CM=core-maintenance make-up. Participant weight is recorded to the nearest pound. Physical activity is self-reported minutes of moderate or brisk activity in the preceding week; record 0 minutes if no activity was reported. The curriculum checklist separates core phase months 1-6 from core-maintenance phase months 7-12.
- **Mapping status:** Planned collection rules and units only; no total session count, participant denominator, or result is printed.

### D2C-N05 — Healthcare utilization and incident diabetes operational data

- **Source locations:** DOC-002 PDF pp. 67 and 70.
- **Population/time:** Participants report counts of primary-care visits, non-primary-care specialist visits, hospitalizations, and emergency-department visits in the past 6 months. The incident-diabetes letter states that each participant's trial duration is 12 months.
- **Definitions/units:** Health-care-use fields are counts of visits/events over a 6-month recall period, not rates. The incident-diabetes letter allows a point-of-care hemoglobin A1C result (with date) or participant-reported diabetes diagnosis; it recommends confirmation by serum A1C plus fasting glucose but states that confirmed diabetes or antihyperglycemic medication does not remove trial eligibility.
- **Mapping status:** Planned/operational measurement definitions only; no event counts, A1C values, or incidence rate is printed.

### D2C-N06 — COVID-19 protocol thresholds and timing

- **Source locations:** DOC-002 PDF p. 71.
- **Population/time:** Before and during study visits.
- **Definitions/units:** Symptom/fever threshold is temperature `T > 100.4°F`; a symptomatic participant's visit is postponed until symptom-free for 14 days. Social distancing is defined as 6 feet or more where possible. These are operational thresholds, not analyzed outcomes.
- **Mapping status:** No reported values or statistical comparison.

### D2C-N07 — Adverse-event collection rule

- **Source locations:** DOC-002 PDF p. 72.
- **Population/time:** Since the last visit.
- **Definitions:** The form first records new medical problems (yes/no), then asks whether the problem was related to the Sweetch/DPP participation (yes/no, with a reason if yes). It does not print an adverse-event count, denominator, rate, attribution total, or analysis rule.
- **Mapping status:** Planned data-collection definition only.

## Remaining direct-source page coverage

| PDF page(s) | Direct-source mapping status | Quantitative content relevant to result consistency |
|---|---|---|
| 61 | COMPLETE | D2C-N01 scoring continuation; no observed result. |
| 62-63 | COMPLETE | D2C-N02 questionnaire scoring/NPS definitions; p. 63 begins WHO-5. |
| 64 | COMPLETE | D2C-N03 WHO-5 scoring. |
| 65-66 | COMPLETE | D2C-N04 local DPP data fields, codes, units, and core/core-maintenance month ranges. |
| 67 | COMPLETE | D2C-N05 six-month health-care-utilization count fields. |
| 68-69 | COMPLETE | Home-visit safety/administrative procedures; no result-relevant quantitative relationship. |
| 70 | COMPLETE | D2C-N05 incident-diabetes operational letter and 12-month trial duration. |
| 71 | COMPLETE | D2C-N06 operational temperature, delay, and distance thresholds. |
| 72 | COMPLETE | D2C-N07 adverse-event evaluation form. |
| 73-90 | COMPLETE | Direct native/layout extraction and page rendering completed for every page. These final protocol administrative/appendix units contain no printed analyzed result, statistical estimate, result table, figure, or cross-document quantitative comparator within this assigned support scope. No applicable quantitative relationship beyond the protocol definitions above was identified. |

## Statistical relationships

No inferential-statistical relationship is reported in this slice. Accordingly, no provisional `D2C-S` relationship was created. The seven `D2C-N` records are numeric/scoring, time-window, threshold, code, or planned collection definitions for possible later cross-document matching.

## No-candidate boundary

This mapping is an evidence inventory only. It does not diagnose or adjudicate a candidate. No source-grounded discrepancy was assessed or registered in this artifact.

## Limitation

The supplied PDF's native and layout text on this 30-page slice is glyph-encoded. The workflow-native extractions are retained as provenance, visual page rendering was used for readable forms, and a bounded CPU Tesseract attempt did not complete. This is an extraction-method limitation, not an uncovered direct-source unit.
