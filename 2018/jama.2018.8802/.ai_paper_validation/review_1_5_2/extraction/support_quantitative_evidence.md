# Support quantitative evidence extraction

## Scope and method

Fresh support-only mapping of `DOC-002` (`joi180070supp1_prod.pdf`, PDF pp. 1-25) and `DOC-003` (`joi180070supp2_prod.pdf`, PDF pp. 1-9). Evidence used: the new native-text and coordinate-layout TSV assets named in the coverage plan. No legacy audit derivative or external source was used. `UN` and `US` are provisional mapper keys, not candidate IDs.

## Page-level completion

| Source/page(s) | Result-relevant content and completion |
|---|---|
| DOC-002 pp. 1-2 | Cover and investigator/cluster list; no trial-result display. COMPLETE, not applicable. |
| DOC-002 pp. 3-4 | Background and design: annual stroke-care cost US$5.76 billion; 40 hospitals; two-arm cluster trial. COMPLETE. |
| DOC-002 p. 5 | Flow-diagram caption only; diagram’s internal visual labels/numbers are not recoverable from native/layout text. COMPLETE with visual-only limitation. |
| DOC-002 pp. 6-8 | Eligibility, 563-network hospitals, 27 provinces plus 4 municipalities, approximately 20 hospitals per province/municipality, age >18 years, within 7 days, 40 clusters, 1:1 allocation. COMPLETE. |
| DOC-002 pp. 9-10 | Intervention descriptions: first 7 acute-admission days plus discharge; rtPA arrival <2 hours and treatment <3 hours; two-day workshop; 4 written protocols. COMPLETE. Figure 2 internal visual content not recoverable. |
| DOC-002 pp. 11-12 | Monitoring recommendation once weekly; cycle every 30 consecutive patients per cluster. COMPLETE. Figure 3 internal visual content not recoverable. |
| DOC-002 pp. 13-16 | Primary performance measures, eligibility exclusions, composite/all-or-none definitions, secondary-outcome/time definitions. COMPLETE. Figure 4 internal visual content not recoverable. |
| DOC-002 pp. 17-19 | Sample-size assumptions and analysis plan. COMPLETE. |
| DOC-002 p. 20 | Follow-up time points 3, 6, 12 months; administrative content otherwise. COMPLETE. |
| DOC-002 pp. 21-25 | References only; no study-result display. COMPLETE, not applicable. |
| DOC-003 p. 1 | Supplement contents list only. COMPLETE, not applicable. |
| DOC-003 p. 2 | Baseline-survey results and definitions. COMPLETE. |
| DOC-003 pp. 3-4 | eTable 1 performance-measure definitions and exclusions. COMPLETE. |
| DOC-003 p. 5 | eTable 2 baseline characteristics by one-year mRS availability. COMPLETE. |
| DOC-003 pp. 6-7 | eTable 3 individual vascular events at 3, 6, 12 months and adjustment/event footnotes. COMPLETE. |
| DOC-003 pp. 8-9 | eTable 4 sensitivity analysis, definitions, adjustment covariates. COMPLETE. |

## Extracted quantitative definitions and displays

### DOC-002 protocol (pp. 3-20)

- **UN001** — PDF p. 3: China annual stroke-care cost stated as about **US$5.76 billion**.
- **UN002** — PDF p. 4: **40 hospitals** participate in the two-arm, parallel, cluster-randomized trial.
- **UN003** — PDF p. 6: network includes **563 hospitals**, from **27 provinces** and **4 municipalities**, with about **20 hospitals** per province/municipality; hospital exclusion includes fewer than **10 suspected AIS patients/month**.
- **UN004** — PDF pp. 6-7: patient eligibility is age **>18 years**, ischemic stroke within **7 days** of index event, and CT/MRI confirmation within **7 days** after symptom onset.
- **UN005** — PDF p. 7: **40 eligible clusters** stratified by province, hospital grade, and baseline stroke-care quality; randomized **1:1** to intervention/control.
- **UN006** — PDF p. 8: **2** QCI providers per intervention cluster attend a **2-day** workshop.
- **UN007** — PDF p. 9: clinical pathway covers each of the first **7 days** of acute admission and discharge.
- **UN008** — PDF p. 10: rtPA protocol eligibility is arrival within **2 hours** of last-seen-normal and treatment within **3 hours**; medication protocol specifies antithrombotics by end of **day 2**.
- **UN009** — PDF p. 11: implementation performance may be viewed at any time, recommended **once per week**.
- **UN010** — PDF p. 12: feedback cycle follows **30 consecutive patients** per hospital/cluster and is repeated every **30 consecutive patients**.
- **UN011** — PDF pp. 13-15: nine primary performance measures: rtPA arrival <2 h/treatment <3 h; antithrombotic medication within **48 h**; DVT prophylaxis within **48 h**; dysphagia screen before oral intake; discharge antithrombotic; AF anticoagulation; statin if LDL **>=100 mg/dL**; antihypertensive if hypertension; hypoglycemic if diabetes.
- **UN012** — PDF pp. 15-16: shared exclusions include discharge to hospice/another short-term general hospital or leaving against advice before end of **hospital day 2**; non-rtPA acute measures exclude death before end of day 2; rtPA excludes erroneous/missing times, outside-hospital rtPA, and initiation after **180 minutes**; discharge measures exclude in-hospital death.
- **UN013** — PDF p. 16: composite adherence = interventions performed among eligible patients / possible interventions among eligible patients; all-or-none = proportion of eligible patients receiving all applicable measures.
- **UN014** — PDF p. 16: secondary outcomes include in-hospital death; ischemic stroke, hemorrhagic stroke, myocardial infarction, vascular death; disability mRS **3-5**; and all-cause mortality at **3, 6, 12 months**.
- **UN015** — PDF p. 17: sample-size assumptions: baseline mean composite score **80%**, target improvement **5%**, **80%** power, **5%** significance level, ICC **0.02**, **40 clusters**, approximately **4800 patients**, median **120** AIS patients/cluster.
- **UN016** — PDF p. 17: planned **3** monitoring/feedback/improvement cycles, **30 patients/cycle/cluster** (30 x 3 x 40 = 3600 stated enrollment implication; this is a planned-cycle quantity separate from the approximate 4800 sample-size quantity).
- **UN017** — PDF pp. 18-19: categorical variables as proportions; normally distributed continuous variables mean (SD), skewed variables median (IQR); composite care opportunity coded 1=met, 0=not met. Example: eligible for **5 of 7** measures, receives **3**, thus five observations: **3** with outcome 1 and **2** with outcome 0.
- **UN018** — PDF pp. 19-20: clinical vascular events/mortality evaluated at discharge and **3, 6, 12 months**; sensitivity analysis includes contraindication patients in the overall-population denominator.

### DOC-003 eAppendix/eTables (pp. 2-9)

- **UN019** — PDF p. 2: pre-randomization baseline survey prospectively included **20 patients per cluster**; same endpoint definition as randomized phase.
- **UN020** — PDF p. 2: composite adherence: intervention **80.2%** versus control **79.5%**. Individual intervention versus control adherence: IV rtPA <2 h **22.6% vs 13.0%**; early antithrombotics **95.4% vs 88.4%**; dysphagia screening **79.6% vs 88.1%**; DVT prophylaxis **14.4% vs 7.8%**; discharge antithrombotics **91.6% vs 91.6%**; AF/flutter anticoagulation **14.8% vs 28.2%**; lipid lowering **66.9% vs 64.6%**; antihypertension **69.4% vs 71.2%**; hypoglycemic therapy **83.2% vs 78.2%**.
- **UN021** — PDF pp. 3-4: eTable 1 defines all nine performance measures, including IV rtPA arrival within **2 h** and treatment within **3 h**, early antithrombotics within **2 days**, DVT prophylaxis by hospital day **2**, and LDL threshold **>=100 mg/dL**; exclusions mirror UN012, including rtPA after **180 minutes**.
- **UN022** — PDF p. 5 eTable 2: one-year mRS data group n=**3949**, loss-to-one-year-mRS group n=**851**; total represented **4800**. Age median (IQR) **65 (56-74)** vs **64 (56-74)**; NIHSS **3 (2-6)** vs **3 (2-6)**; NIHSS range **0-42**.
- **UN023** — PDF p. 5: one-year mRS versus loss counts/percentages: male **2497/3949 (63.2%)** vs **546/851 (64.2%)**; ischemic stroke **1137/3949 (28.8%)** vs **251/851 (29.5%)**; diabetes **890/3949 (22.5%)** vs **196/851 (23.0%)**; hypertension **2552/3949 (64.6%)** vs **538/851 (63.2%)**; dyslipidemia **285/3949 (7.2%)** vs **62/851 (7.3%)**; CAD/previous MI **512/3949 (13.0%)** vs **97/851 (11.4%)**; AF **200/3949 (5.1%)** vs **45/851 (5.3%)**; ever smoking **1736/3949 (44.0%)** vs **380/851 (44.7%)**.
- **UN024** — PDF p. 6 eTable 3, 3 months, intervention/control event counts: ischemic stroke **44/2400 (1.8%)** vs **55/2400 (2.3%)**; hemorrhagic stroke **14/2400 (0.6%)** vs **20/2400 (0.8%)**; MI **3/2400 (0.1%)** vs **5/2400 (0.2%)**; vascular death **46/2400 (1.9%)** vs **67/2400 (2.8%)**.
- **UN025** — PDF p. 6 eTable 3, 6 months: ischemic stroke **74/2400 (3.1%)** vs **102/2400 (4.3%)**; hemorrhagic stroke **17/2400 (0.7%)** vs **21/2400 (0.9%)**; MI **8/2400 (0.3%)** vs **8/2400 (0.3%)**; vascular death **70/2400 (2.9%)** vs **82/2400 (3.4%)**.
- **UN026** — PDF p. 6 eTable 3, 12 months: ischemic stroke **117/2400 (4.9%)** vs **160/2400 (6.7%)**; hemorrhagic stroke **23/2400 (1.0%)** vs **24/2400 (1.0%)**; MI **11/2400 (0.5%)** vs **14/2400 (0.6%)**; vascular death **91/2400 (3.8%)** vs **125/2400 (5.2%)**.
- **UN027** — PDF p. 7: a patient may have different new vascular events; sums of event types can exceed number of patients with new vascular events.
- **UN028** — PDF p. 8 eTable 4 sensitivity analysis: composite measure mean (SD) **85.3 (15.2)** intervention vs **80.9 (17.1)** control.
- **UN029** — PDF p. 8: IV rtPA <2 h **46/254 (18.11%)** vs **23/238 (9.66%)**; early antithrombotics **2307/2400 (96.1%)** vs **2253/2400 (93.9%)**; dysphagia screen **2255/2328 (96.9%)** vs **2040/2139 (95.4%)**; DVT prophylaxis **178/672 (26.5%)** vs **66/606 (10.9%)**.
- **UN030** — PDF p. 8: discharge antithrombotics **2272/2400 (94.7%)** vs **2141/2400 (89.3%)**; AF anticoagulation **63/182 (34.6%)** vs **39/174 (22.5%)**; lipid lowering **1415/1517 (93.3%)** vs **1439/1586 (90.8%)**; antihypertensive **1510/1870 (80.7%)** vs **1372/1803 (76.1%)**; antidiabetic **653/743 (87.9%)** vs **557/688 (81.1%)**.
- **UN031** — PDF pp. 7, 9: adjusted analyses include patient age, sex, ischemic stroke, hypertension, diabetes, hyperlipidemia, AF, CAD/previous MI, smoking, NIHSS and hospital grade, region, stroke unit, teaching status, neurological-ward beds. ORPA means population-average odds ratio; eTable 4 uses overall-population sensitivity denominators.

## Evidence limitations

Native text duplicates characters and splits several decimal digits. Values were resolved with coordinate layout and exact-source full-page rasters where needed; DOC-003 p. 8 visibly prints eTable 4 rtPA percentages of 18.11% and 9.66%. The raw visual-only contents of DOC-002 Figures 1-4 were unavailable in the initial text/layout assets, but their captions and associated non-result definitions were mapped. No inference or candidate diagnosis is made here.
