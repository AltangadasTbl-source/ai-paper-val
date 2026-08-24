# Numeric Consistency Review

## Scope and evidence boundary

Complete assigned scope: all 88 numeric/reporting relationships `N001` through `N088` in `relationships/numeric_relationship_inventory.md`. Evidence was limited to the direct PDFs and their fresh native/layout text and rendered-page assets, plus the current-run mapper records at `extraction/parts/main_mapping_doc001.md`, `extraction/parts/support_mapping_doc002.md`, and `extraction/parts/support_mapping_doc003_doc004.md`. No legacy audit derivative, web source, or external literature was used.

The review applied every applicable arithmetic, total/subgroup, numerator/denominator/percentage, rounding, missingness/population, unit/scale/label, rate-versus-count, repeated-value, and concrete analysis-unit check. Model-adjusted values were not treated as crude arithmetic identities unless the printed method explicitly supplied such a rule. A displayed threshold P value (including `<.0001`) was not treated as a display-zero candidate.

## Completion inventory

`PASS` means all applicable checks completed without a distinct qualifying discrepancy. `CANDIDATE` points to a record below; it is not a disposition or stable candidate ID.

| N IDs | Local handles / source | Completed applicable checks | Result |
|---|---|---|---|
| N001-N007 | M01-M07, DOC-001 pp. 1-4, 8 | Cluster/analysis population, randomisation, period, outcome-definition, score-scale, rate-denominator, model-label, planning-versus-observed separation | PASS |
| N008 | M08, DOC-001 p. 3 Figure 1 | Flow arithmetic: `34-11=23`; `12+11=23` | PASS |
| N009-N012 | M09-M12, DOC-001 p. 3 Figure 1 | Hospital, discharge, patient-day and calendar-year subgroup sums; rounded means; run-in/time labels | PASS |
| N013-N017 | M13-M17, DOC-001 p. 5 and Figure 1 | Hospital-category totals and percentages; baseline/intervention total reconciliation; population distinction for two nonimplementing sites | PASS |
| N018 | M18, DOC-001 p. 6 Table 2 | Sampling total/missingness: `21*5*(26+52)=8,190`; `8,190-8,109=81`; `8,109/8,190=99.0%` | PASS |
| N019-N023 | M19-M23, DOC-001 p. 6 Table 2/narrative | Percent denominators, CI endpoint ordering, sign/label agreement, narrative-to-table repeats; adjusted difference distinguished from crude change | PASS |
| N024 | M24, DOC-001 pp. 6-7 Table 3 | Death-rate arithmetic: `97/50,173*1,000=1.933`; `147/94,366*1,000=1.558`; total denominator/label match | PASS |
| N025 | M25, DOC-001 pp. 6-7 | Death and DNR totals: `97+147=244`; `155/244=63.5%`; no-DNR numerator does not exceed mortality | PASS |
| N026 | M26, DOC-001 pp. 6-7 | SCDE totals/rates/proportions: `127+259=386`; `127/251,859*1,000=.504`; `259/307,584*1,000=.842`; urgent-ICU denominators identified | PASS |
| N027-N032 | M27-M32, DOC-001 p. 7 Table 3 | Separate ICU/hospital/patient-day rate scales; event totals, preventable-arrest subset, rounding, CI ordering, model/adjustment and post-hoc labels | PASS |
| N033-N037 | M33-M37, DOC-001 pp. 8-9 | Individual patient versus admission denominator, figure scale/coordinates, percentage arithmetic, repeated narrative/table values, run-in/site labels | PASS |
| N038-N043 | D2-N01-N06, DOC-002 pp. 1, 7-16, 24 | Protocol cluster/population/period/outcome/unit/denominator definitions; no incompatible numerical identity asserted | PASS |
| N044 | D2-N07, DOC-002 pp. 1, 14, 29 | Mortality planning rate, RRR, ARR unit/size arithmetic and repeated description | CANDIDATE NC-01 |
| N045-N049 | D2-N08-N12, DOC-002 pp. 10-12, 24 | Ordered-scale categories, treatment thresholds, hours and mL/kg units, composite/urgent-transfer definitions | PASS |
| N050 | D2-N13, DOC-002 pp. 11, 28 | Preventability scale, operative threshold, event population/rate label and repeated definition | CANDIDATE NC-03 |
| N051-N054 | D2-N14-N17, DOC-002 pp. 12-17 | 48-hour/readmission operationalization, 28-day VFD, patient-day area definition, sample-size/time and measurement labels | PASS |
| N055-N059 | D2-N18-N22, DOC-002 pp. 1-6, 21 | Score ranges and threshold labels, performance measures, contextual population/time/scale separation, reference-search counts | PASS |
| N060-N067 | D2-N23-N30, DOC-002 p. 19 Table 1 | Score/trigger ranges, threshold direction, sensitivity/specificity/AUC labels, distinct instrument rows | PASS |
| N068 | D2-N31, DOC-002 pp. 22-23 | Implementation durations, group/participant units, sequential phase labels | PASS |
| N069 | D2-N32, DOC-002 pp. 25-27 | Abstraction-window units, duplicated printed code noted, cardiac-arrest scale comparator | CANDIDATE NC-02 |
| N070-N071 | D2-N33-N34, DOC-002 pp. 26, 28 | Vital-sign/medication units and preventability-scale ordering/threshold description | PASS |
| N072-N073 | D2-N35-N36, DOC-002 p. 29 | Average/rate arithmetic: listed mortality rates average `5.107... -> 5.11`; `2,202/678,365*1,000=3.246 -> 3.2` | PASS |
| N074 | D2-N37, DOC-002 pp. 14, 30 | Planning patient-day identity `99,389*4=397,556`; SCDE reference time/denominator provenance | CANDIDATE NC-04 |
| N075 | D2-N38, DOC-002 p. 30 | Reference-table percentage/rate arithmetic, conventional rounding, printed numerator/denominator labels and period label | CANDIDATE NC-05 / stable C007 |
| N076-N080 | N-D3-01-N-D3-05, DOC-003 pp. 1-7 | Hospital/patient/admission analysis-unit distinctions; count/rate and discharge/patient-day/ICU-discharge denominators; 0.5 transformation and `N/1000` scale labels | PASS |
| N081 | N-D4-01, DOC-004 pp. 2-3 | Figure rate unit and circle/period identity; matched `0.01/1,000` caption value | PASS |
| N082-N084 | N-D4-02-N-D4-04, DOC-004 pp. 4-8 | Sample total `2,588+2,832=5,420`; 0-7 observation scale; composite, 28-day, PIM/PELOD units and bounds | PASS |
| N085 | N-D4-05, DOC-004 pp. 9-10 eTable 2 | Every hospital total equals baseline+post; arm sums, mortality rates, no-DNR subset and cross-table group labels | PASS |
| N086 | N-D4-06, DOC-004 p. 11 eTable 3 | Hospital patient-day sums, event-rate arithmetic, preventable-arrest subset and cross-table linkage | PASS |
| N087 | N-D4-07, DOC-004 pp. 12-13 eTable 4 | Urgent-ICU patient denominators, shown percentage checks, CI order/containment, unit and model-label agreement | PASS |
| N088 | N-D4-08, DOC-004 p. 14 eTable 5 | Anticipated/actual count-rate arithmetic and exact cross-table totals | PASS |

## Qualifying numeric-consistency candidate records

### NC-01 — Mortality absolute-risk-reduction unit conflict in the protocol

- **Relationships and exact locations:** N044 / D2-N07: `joi180015supp1_prod.pdf#page=1`, protocol summary: “risk reduction of **0.9 deaths/1000 hospital admissions** equal to a relative risk reduction of **18%**”; `#page=14`, section 2.11: baseline **5.1 per thousand** and 18% RRR, “Absolute Risk Reduction **0.09%**”; `#page=29`, Appendix 1: 18% mortality RRR “corresponds to an absolute risk reduction of **0.9%**,” and printed RRR **0.178** at baseline **5.1/1,000**.
- **Printed comparator and rule:** `5.1*.178=.9078 per 1,000`, equivalent to `.09078%`, not `.9%`. The p.1 and p.14 expressions agree with `.9078/1,000` after rounding; p.29 is tenfold larger.
- **Tolerance:** None: factor-ten difference exceeds any rounding tolerance.
- **Direct observation:** Same planning context, printed ARR descriptions `0.9/1,000`, `0.09%`, and `0.9%`.
- **Inference and alternatives:** The p.29 `%` sign may be a typographic unit error; source does not identify the intended correction.
- **Quality-control relevance:** A factor-ten ARR unit conflict can misstate planning effect size when the protocol is abstracted.
- **Exact human question:** Does Appendix 1’s “0.9%” mean `0.9 per 1,000` / `0.09%`, or an unstated alternative denominator/calculation?

### NC-02 — Cardiac-arrest resuscitation-scale category conflict

- **Relationships and exact locations:** N045 / D2-N08 and N069 / D2-N32: `joi180015supp1_prod.pdf#page=24`, Table 5 places **CPR at category 6** and **death at category 7**; `#page=11` calls cardiac arrest without DNR “**6 or 7**”; `#page=27`, Table 6 legend says cardiac-arrest events are “scale rating **4 or 5**.”
- **Printed comparator and rule:** All name the Children’s Resuscitation Intensity Scale; Table 5’s definition assigns a cardiac arrest/CPR event category 6 (or death category 7), not 4 or 5.
- **Tolerance:** Not applicable: discrete ordinal labels.
- **Direct observation:** p.27 conflicts with the definition table and p.11 definition.
- **Inference and alternatives:** p.27 may refer to an unstated scale or be a transcription/labeling error; source does not resolve it.
- **Quality-control relevance:** The disagreement can change which events are abstracted as cardiac-arrest deterioration events.
- **Exact human question:** Does p.27 intentionally refer to another scale, or should it read `6 or 7`?

### NC-03 — Incompatible printed preventability threshold

- **Relationships and exact locations:** N050 / D2-N13: `joi180015supp1_prod.pdf#page=11` says consensus rating “**at >4**” is potentially preventable, then includes ratings **4, 5, and 6**; `#page=28`, Table 7 says “**4 or more**” is a high degree of preventability.
- **Printed comparator and rule:** `>4` selects 5-6, while the next sentence and Table 7 include 4. The rules select different event sets.
- **Tolerance:** Not applicable: discrete threshold membership.
- **Direct observation:** Mutually incompatible threshold notation and explicit inclusion examples occur in the same protocol.
- **Inference and alternatives:** “At >4” may mean >=4; Table 7 may conceivably be descriptive rather than the operative endpoint. Source does not resolve which classification governed results.
- **Quality-control relevance:** The threshold determines the numerator/rate of potentially preventable cardiac arrests.
- **Exact human question:** Was the operative threshold >=4 or >4?

### NC-04 — SCDE reference-count period conflict affecting the rate denominator

- **Relationships and exact locations:** N074 / D2-N37: `joi180015supp1_prod.pdf#page=14` calls **1,052 urgent ICU admissions/year** from four hospitals and pairs it with a 40% SCDE estimate and **2 per 1,000 patient-days**; N075 / D2-N38: `#page=30` calls the table **two years** of data and says that in the two years following 31 January 2007 there were **55,963 discharges**, **1,052 urgent PICU admissions**, and **150 code-blue events**.
- **Printed comparator and rule:** A planning rate must align count, time period, and denominator. The same `1,052` is annual on p.14 but two-year on p.30; no annualized count or period-specific patient-day denominator reconciles them.
- **Tolerance:** Not applicable: incompatible period labels, not rounding.
- **Direct observation:** Two periods attach to the same printed reference admission count.
- **Inference and alternatives:** “/year” may be shorthand/error, or p.30 may use a different inclusion period; source lacks time-stratified counts to determine the rate.
- **Quality-control relevance:** Period/denominator ambiguity can distort planned SCDE baseline-rate and power interpretation.
- **Exact human question:** Which period and patient-day denominator support the 1,052-admission reference and 2/1,000 SCDE rate?

### NC-05 — p.30 urgent-PICU and hospital-discharge rates do not round to the printed values (stable C007)

- **Relationship and exact location:** N075 / D2-N38: `joi180015supp1_prod.pdf#page=30`, Appendix 2 table. Printed inputs are **1,052** unplanned PICU admissions and **7,300** PICU discharges with printed **14.5%**; the same table prints **1,052** unplanned PICU admissions and **55,963** hospital discharges with printed **18 per 1,000 hospital discharges**.
- **Printed comparator and reproducible rule:** `1,052/7,300*100 = 14.41096%`, which conventionally rounds to **14.4%** at one decimal, not 14.5%. `1,052/55,963*1,000 = 18.79778`, which conventionally rounds to **19 per 1,000** at whole-number precision, not 18 per 1,000.
- **Tolerance:** Conventional nearest rounding at the printed precision is used. Both discrepancies exceed the half-unit rounding interval: 14.5% implies an unrounded value in `[14.45,14.55)`, and 18/1,000 implies `[17.5,18.5)`.
- **Direct observation:** The printed counts, denominators, and derived displays occur in the same p.30 table; no alternative denominator is printed for either display.
- **Inference and alternatives:** The displays could have been derived using unshown counts/denominators, a nonstandard rounding convention, or one or more transcription errors. The supplied source does not disclose such an alternative.
- **Quality-control relevance:** These are denominator-linked rate/percentage displays used as reference data in protocol planning; unresolved inconsistency can alter abstraction of event burden.
- **Exact human question:** What exact numerator/denominator and rounding convention generated the printed 14.5% and 18/1,000 values, given the p.30 table’s displayed counts?

## Summary and limitations

- **Relationships completed:** 88/88 (`N001-N088`).
- **Distinct qualifying numeric candidates:** 5 (`NC-01` through `NC-05`), all from DOC-002 protocol text. NC-05 is the numeric-lane record for already appended stable candidate `C007`.
- **No qualifying numeric candidate:** DOC-001 main paper, DOC-003 SAP, and DOC-004 supplementary results after the checks listed above.
- **Limitation:** Several values are GEE/model-adjusted estimates. Raw analysis data, variance inputs, and fitted-model outputs are not supplied, so crude calculations were not substituted for model-adjusted results. This does not affect the four direct printed contradictions.
