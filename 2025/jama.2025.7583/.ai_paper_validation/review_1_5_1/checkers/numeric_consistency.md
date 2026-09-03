# Numeric Consistency Review

## Scope, method, and status

This independent numeric-review pass covered every canonical numeric/reporting relationship, **N001 through N089**, without sampling. I used the canonical relationship inventory and fresh quantitative evidence maps as locators, then checked the relevant printed values against the supplied direct PDFs. I did not consult legacy candidate, checker, verifier, quality, or final-report artifacts. Statistical inventory material was consulted only where an analysis-definition label was necessary to distinguish a numeric relationship.

Checks applied where applicable were: integer and subgroup totals; numerator/denominator/percentage reconciliation; mutually exclusive versus explicitly overlapping categories; analysis-population identity; displayed differences and rounding; cross-document identity after matching population/time/definition; measure, threshold, unit, and rate/count labels; and repeated-value consistency. A percentage rounded to one decimal was accepted when its exact fraction rounds to the printed value (tolerance: 0.05 percentage point); rounded whole-percentage narrative language was accepted within 0.5 percentage point. A planning quantity marked as approximate or “on average” was not required to reproduce an integer target exactly.

**Result:** 89/89 relationships explicitly checked. Three distinct provisional quality-control candidates are documented below. All candidates are **Pending Human Adjudication**; no stable candidate ID, severity, validity judgment, or disposition is assigned here.

## Provisional candidates

### NC-01 — Primary-endpoint midline-shift boundary differs between the SAP and the protocol/publication

- **Primary category:** Measure, label, or scale inconsistency.
- **Relationships/provenance:** N009 (main endpoint definition), N033 (protocol endpoint definition), with the linked SAP endpoint definition needed as the comparator; corroborated by results supplement eTable 4.
- **Exact direct-source locations:**
  - `jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3`, End Points: “midline shift of **5 mm or greater**”.
  - `joi250033supp1_prod_1750956987.76581.pdf#page=7`, primary-endpoint definition: “midline shift **≥ 5mm**”; the protocol contains further matching ≥5-mm wording.
  - `joi250033supp4_prod_1750956987.77981.pdf#page=15`, EMPROTECT row: “midline shift **≥ 5 mm**”.
  - `joi250033supp5_prod_1750956987.78281.pdf#page=3`, SAP primary outcome: “midline shift **> 5mm**”.
- **Printed inputs and direct observation:** The main article, protocol, and results supplement each include a shift exactly equal to 5 mm in the endpoint (`≥5` / “5 mm or greater”). The SAP excludes an exact 5-mm shift (`>5`).
- **Reproducible rule/calculation:** Compare the set of qualifying shift values. `x ≥ 5 mm` includes `x = 5 mm`; `x > 5 mm` does not. The two definitions therefore differ at the boundary by the exact value 5 mm; this is not a rounding comparison and requires no numerical tolerance.
- **Inference and alternatives:** It is an inference that the SAP wording was an editorial/translation or version-specific drafting difference rather than the definition used for the adjudicated result. A protocol amendment or a source-specific convention could explain the difference, but the supplied materials do not identify a version change that reconciles this exact threshold. No participant-level shifts are supplied, so the effect on event counts cannot be quantified.
- **Quality-control relevance:** A data extractor using the SAP alone could apply a different component definition from the one reported in the article and results supplement. This is a bounded endpoint-definition consistency issue; it does not establish an error in the trial result.
- **Exact human question:** Which midline-shift boundary governed final endpoint adjudication—`≥5 mm` or `>5 mm`—and should the SAP be corrected or annotated to match that final definition?
- **Checker provenance:** Numeric consistency review; direct-PDF confirmation completed.

### NC-02 — Stated 20% loss-to-follow-up allowance does not arithmetically reconcile with the printed 142-per-group and 342-total sample-size figures

- **Primary category:** Numeric or arithmetic inconsistency.
- **Relationships/provenance:** N011 (main planning summary), N036/N040 (protocol planning and loss allowance), N056 (protocol detailed sample arithmetic); linked SAP sample-size definition used for cross-document confirmation.
- **Exact direct-source locations:**
  - `joi250033supp1_prod_1750956987.76581.pdf#page=50`, section 12.2: “142 patients per group are required” and “Assuming a lost-to-follow-up rate of 20%, a total of 342 patients (171 per group) is required.”
  - `joi250033supp5_prod_1750956987.78281.pdf#page=5`, section 3.2: the same `142` per group, `20%` loss-to-follow-up, and `342` total (`171` per group) statements.
  - `jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3`, Sample Size Calculation: `20%` lost to follow-up and a needed total of `342` patients, described as calculated with two sequential tests.
- **Printed inputs and direct observation:** Both detailed planning documents print a required analysable size of `142 × 2 = 284`, a loss-to-follow-up rate of `20%`, and an enrolled total of `342` (`171 × 2`).
- **Reproducible rule/calculation:** If “20% lost to follow-up” means 20% of enrolled participants are unavailable, required enrollment is `284 / (1 − 0.20) = 355`; with equal groups this is 177.5 per group before an explicit rounding rule. The printed total gives `342 × 0.80 = 273.6` expected retained participants, `10.4` fewer than 284. Equivalently, `342 / 284 − 1 = 20.42%` is an inflation over the required analysable sample, which is distinct from retaining 80% of enrollment.
- **Tolerance:** Integer rounding cannot reconcile 342 with 355: even rounding 177.5 per group down/up gives totals 354 or 356. The discrepancy is 13 participants from the direct 20%-of-enrollment calculation.
- **Inference and alternatives:** The documents may use the common but differently defined convention of adding 20% to the analysable sample (`284 × 1.20 = 340.8`) and then rounding/design-adjusting to 342. The sequential-design computation may also have supplied an unstated adjustment. Those alternatives could make 342 intentional, but neither source explains that the reported “20% loss” is an inflation convention rather than a 20% loss fraction.
- **Quality-control relevance:** This is a planning-reporting arithmetic/definition issue that can mislead readers reconstructing target enrollment or expected analyzable sample. It does not claim that the observed randomized total or reported efficacy result is invalid.
- **Exact human question:** Does the stated 20% allowance mean 20% added to the 284 required analysable participants, rather than 20% of enrolled participants lost; if so, should the sample-size text state that convention or provide the full sequential-design calculation?
- **Checker provenance:** Numeric consistency review; direct-PDF confirmation completed.

### NC-03 — Standard-care burr-hole and trephine surgery counts exceed their shared printed denominator

- **Primary category:** Denominator, proportion, or total inconsistency.
- **Relationship/provenance:** N021, baseline treatment/surgery values in Table 1.
- **Exact direct-source location:** `jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5`, Table 1, Treatment: standard-care column prints `146/163 (89.6)` for “Trepanation burr hole craniostomy” and `18/163 (11.0)` for “Trephine craniostomy.” Footnote e identifies both as craniostomy procedures with openings up to 30 mm.
- **Printed inputs and direct observation:** The two displayed procedure rows use the same stated standard-care denominator, 163, and describe the two named craniostomy procedures in the same treatment section.
- **Reproducible rule/calculation:** `146 + 18 = 164`, which exceeds the shared printed denominator `163` by one patient. Independently, `146/163 × 100 = 89.57%` (89.6% rounded) and `18/163 × 100 = 11.04%` (11.0% rounded); their displayed percentages sum to `100.6%`. Integer-count reconciliation has zero tolerance; percentage rounding cannot resolve the one-patient excess.
- **Inference and alternatives:** The two rows may not be intended to be mutually exclusive, or one row’s numerator/denominator may be a typographical error. However, the supplied table gives neither an overlap explanation nor a separate denominator for either row, while footnote e describes them as the two methods of craniostomy. The checker does not infer which printed value, if any, should change.
- **Quality-control relevance:** A reader extracting baseline surgery type could record an impossible procedure distribution for the displayed standard-care denominator; this can propagate a denominator error into tabular data reuse. It does not establish a problem with the trial’s primary outcome.
- **Exact human question:** Were any standard-care patients counted in both burr-hole and trephine procedure rows; if not, which printed count or denominator should be corrected, and should Table 1 state the relevant overlap/missing-data rule?
- **Checker provenance:** Numeric consistency review; direct-PDF confirmation completed.

## Complete relationship-by-relationship record

| ID | Checked relationship and applied checks | Result |
|---|---|---|
| N001 | Randomized total and arm sum: `171 + 171 = 342`; repeated in flow/abstract. | PASS — exact. |
| N002 | Recruitment dates, 12 centers, and follow-up date; repeated-location labels. | PASS — no incompatible matched value. |
| N003 | `274/342 = 80.12%`, printed 80.1%; completion `308/342 = 90.06%`, printed 90.1%. | PASS — one-decimal rounding. |
| N004 | `24/162 = 14.81%`, `33/157 = 21.02%`; components `22+2=24`, `32+1=33`. | PASS — exact/rounded. |
| N005 | Matched primary analysis values, OR/CI/difference labels, population and imputation label. | PASS — no numeric or label mismatch. |
| N006 | `7/162 = 4.32%`, `13/157 = 8.28%`; observed difference −3.96 percentage points. | PASS — rounding to 4.3%, 8.3%, and −4.0%. |
| N007 | `3/171 = 1.75%`, `1/171 = 0.58%`; minor components `2+1=3`. | PASS — rounded percentages and totals. |
| N008 | Eligibility thresholds, units, and intervention timing. | PASS — no incompatible threshold/label in matched records. |
| N009 | Primary composite threshold/definition across main/protocol/SAP/supplement. | CANDIDATE NC-01. |
| N010 | Secondary endpoint labels, units, and 1-/6-month time points. | PASS — matched framework. |
| N011 | Planned sample size, attrition, interim parameters and arithmetic. | CANDIDATE NC-02. |
| N012 | `164+101+34+18=317`; `659−317=342`. | PASS — exact flow arithmetic. |
| N013 | `13+5+4+2+1+1=26`; `145+26=171`; control `171`. | PASS — exact flow arithmetic. |
| N014 | Arm discontinuations: intervention `9+5+1=15`; control `13+5+1=19`; death subtotals `6+3=9`, `5+8=13`. | PASS — exact. |
| N015 | Intervention `162+9=171`, control `157+14=171`; nonevaluable subgroups sum to 9 and 14. | PASS — exact. |
| N016 | Sex totals each arm 171; percentages reconcile. | PASS — exact/rounded. |
| N017 | Medical-history numerators/denominators and ASA scale label. | PASS — percentages reconcile; no scale mismatch. |
| N018 | Risk-factor fractions, available-case denominators, and percentages. | PASS — all reconcile within rounding. |
| N019 | Symptom available-case denominators and percentages; GCS scale direction. | PASS — all reconcile within rounding. |
| N020 | Baseline imaging totals (`127+44=171`, `130+41=171`), units and available-case labels. | PASS — no inconsistency. |
| N021 | Surgery-type counts/denominators: intervention `150/167 + 17/167 = 167`; standard care `146/163 + 18/163 = 164`. | CANDIDATE NC-03 — shared printed denominator exceeded by one. |
| N022 | Surgery-complication percentages and nonexclusive “other” label/footnote. | PASS — fractions reconcile; no false subgroup-sum rule applied. |
| N023 | mRS rates, risk differences, time points, CI/order, and percentage labels. | PASS — printed differences match rounded rates; model label retained. |
| N024 | Mortality fractions/percentages and differences at 1 and 6 months. | PASS — exact/rounded. |
| N025 | Hospital-stay medians, unit days, difference and matched narrative. | PASS — exact repetition. |
| N026 | Localization subgroup numerators sum to all-patient counts (`12+12=24`, `22+11=33`); OR labels. | PASS — exact. |
| N027 | Medication subgroup numerators sum to all-patient counts (`5+19=24`, `13+20=33`); OR labels. | PASS — exact. |
| N028 | On-site sensitivity OR/CI/P and endpoint-assessor label. | PASS — no conflicting matched value. |
| N029 | `36/171=21.05%`, `32/171=18.71%`, `91/171=53.22%`, `89/171=52.05%`; patient versus event-count labels. | PASS — rounding and labels consistent. |
| N030 | Adverse-event row percentages, denominators, and count-versus-patient frequency labels. | PASS — all fractions reconcile. |
| N031 | Functional-status values and transient-deficit duration label. | PASS — no incompatible occurrence. |
| N032 | Expected 10% versus observed rounded 6% narrative, with primary-result match. | PASS — observed unadjusted difference is 6.2 points and coherently rounded to 6%. |
| N033 | Protocol primary composite, particularly shift boundary versus final sources. | CANDIDATE NC-01. |
| N034 | Secondary definitions/time points/rate versus duration labels. | PASS — no incompatible matched definition. |
| N035 | Patient-level 1:1 randomization, ITT and technical-nontreatment labels. | PASS — consistent with 171/171 flow. |
| N036 | Planned N, centers, duration and approximate recruitment-rate statements. | PASS — `1.2 on average` and rounded per-center planning values are not exact-total claims. |
| N037 | Recruitment-feasibility estimates and units. | PASS — prospective approximate context, no reported-total contradiction. |
| N038 | Eligibility/risk thresholds and units. | PASS — matched labels. |
| N039 | T1/T2 timing windows and endpoint time labels. | PASS — no incompatible timepoint. |
| N040 | Planned 20% loss allowance and sample-size identity. | CANDIDATE NC-02. |
| N041 | Intervention particle size, timing and laterality definitions. | PASS — units/labels consistent. |
| N042 | Comparator and cointervention definition. | PASS — no quantitative mismatch. |
| N043 | Background rates/counts explicitly contextual rather than trial results. | PASS — no matched-result comparison applicable. |
| N044 | Renal-decline threshold and SAE rule. | PASS — no inconsistent threshold occurrence. |
| N045 | Adjudication committee size/cadence and trigger labels. | PASS — no numeric conflict. |
| N046 | Five SAE criteria. | PASS — count/definition internally coherent. |
| N047 | Fatal SAE/fatal recurrence monitoring labels. | PASS — no outcome rate asserted. |
| N048 | SAE recurrence thresholds and components. | PASS — no incompatible stated rule in its prospective context. |
| N049 | Safety-period timing. | PASS — no incompatible duration/value. |
| N050 | Hb and creatinine-clearance thresholds. | PASS — units and thresholds consistent. |
| N051 | Immediate/15-day/8-day timing rules. | PASS — distinct administrative intervals, no arithmetic relation claimed. |
| N052 | New-fact and annual-report deadlines. | PASS — no conflict. |
| N053 | T0/T1/T2 collection labels. | PASS — no conflict. |
| N054 | `129/342=37.72%`; printed 37.5% information fraction is a planned information, not participant-proportion, label. | PASS — no erroneous denominator inference. |
| N055 | Planned recurrence, ITT, death and sensitivity definitions. | PASS — version/stage qualifiers retained. |
| N056 | `142` per group, 20% loss, 342 total arithmetic. | CANDIDATE NC-02. |
| N057 | Interim 129, stopping threshold, ITT and imputation labels. | PASS — no incompatible printed value. |
| N058 | Screening/reflection/consent timing. | PASS — no mismatch. |
| N059 | Final-summary timing. | PASS — no mismatch. |
| N060 | PHRC funding label. | PASS — no numeric relationship requiring reconciliation. |
| N061 | Park CT-density thresholds and imputation-covariate label. | PASS — no outcome/count claim or threshold conflict. |
| N062 | Recurrence/admission adjudication process. | PASS — no numeric mismatch. |
| N063 | Major-complication renal threshold. | PASS — consistent definition label. |
| N064 | Named imputation covariates. | PASS — no numerical output asserted. |
| N065 | Trial registration and approval chronology. | PASS — no incompatible source date/value. |
| N066 | Committee/DSMB governance. | PASS — no numeric result asserted. |
| N067 | Surgery-size thresholds and eligibility labels. | PASS — no unit/threshold inconsistency. |
| N068 | CTA/embolization within-7-day timing and amendment. | PASS — matched timing. |
| N069 | 5F/6F catheter and 300–500-µm particle/anastomosis units. | PASS — units/labels consistent. |
| N070 | Unilateral/bilateral treatment rules. | PASS — no incompatible count/label. |
| N071 | Bilateral-prior-surgery special rule. | PASS — no mismatch. |
| N072 | `659−317=342` screened/excluded/randomized flow. | PASS — exact. |
| N073 | `101+164+18+34=317` exclusions. | PASS — exact. |
| N074 | `38+35+29+19+19+11+8+5=164`. | PASS — exact. |
| N075 | `8+3+2+1+1+1+1+1=18`. | PASS — exact. |
| N076 | Randomized group totals `171+171=342`. | PASS — exact. |
| N077 | eTable 1 center rows 001/008/011/012: arm and overall sums/percentages. | PASS — each row and displayed rounding reconcile. |
| N078 | eTable 1 center rows 002/004/010/009: arm and overall sums/percentages. | PASS — each row and displayed rounding reconcile. |
| N079 | eTable 1 center rows 003/005/007/006; all 12 center rows total 171/171/342. | PASS — exact totals; percentages reconcile. |
| N080 | Event denominators 24/33/57 and explicitly overlapping-criteria footnote. | PASS — `24+33=57`; no invalid component sum applied. |
| N081 | Criterion-1/component arm and overall counts/percentages. | PASS — overall counts equal arm sums; overlap rule prevents component summation. |
| N082 | Thickness criterion `8+4=12`; fractions/percentages. | PASS — exact/rounded. |
| N083 | Repeat surgery `7+13=20`; fractions/percentages. | PASS — exact/rounded. |
| N084 | Admission `12+15=27`; fractions/percentages. | PASS — exact/rounded. |
| N085 | Neurologic/unknown death `2+1=3`; fractions/percentages and definition. | PASS — exact/rounded. |
| N086 | Major complication `1/171=0.58%`, printed 0.6%. | PASS — rounded. |
| N087 | Major components total one event; all remaining components zero. | PASS — exact/rounded. |
| N088 | Minor total `3/171=1.75%`, printed 1.8%; component label. | PASS — rounded. |
| N089 | Minor components `2+1=3`; `2/171=1.17%`, `1/171=0.58%`; zero values. | PASS — exact/rounded. |

## Explicit exclusions and limitations

- No display-zero P value was registered as a candidate. The numeric relationships in this pass contain no independent source-grounded contradiction that would make a display-zero convention relevant.
- For N021, the source prints different available-case denominators for different surgery entries. The table does not state that all rows share one denominator, so no missingness-total candidate was inferred.
- For N054, the `37.5%` is expressly an information fraction in a sequential design, not necessarily `129/342` rounded; it was not treated as a denominator mismatch.
- Protocol/SAP planning statements were not treated as conflicting with observed results merely because the final study recruitment period, endpoint version, or analysis implementation differs from a prospectively stated plan. The two candidates above are limited to a directly printed boundary difference and a directly reproducible stated arithmetic relationship.
