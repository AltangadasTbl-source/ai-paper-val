# Support quantitative evidence mapping — DOC-002 and DOC-003

## Scope and method

Fresh mapping of every page of the two supplied support PDFs only. Evidence was read from newly prepared native/layout text under `preprocessing/` and checked against the direct PDFs/rendered pages where table or figure geometry mattered. DOC-003 p. 6 was additionally checked against its fresh CPU OCR asset because the heading glyphs in native/layout text are corrupt. This is an evidence inventory, not a candidate adjudication.

## Page coverage

| Source/page | Result-relevant quantitative content mapped | Status |
|---|---|---|
| DOC-002 pp. 1–2 | Planned allocation, intervention, follow-up, nested case-control sampling, Table 4 recruitment/retention/visit projections | MAPPED |
| DOC-002 pp. 3–4 | Population eligibility, cancer-rate/power assumptions, Tables 5–6, recruitment quantities | MAPPED |
| DOC-002 p. 5 | Cancer ascertainment, validation sampling, laboratory/measurement schedule, storage quantity | MAPPED |
| DOC-002 p. 6 | Longitudinal assessments, secondary endpoint definitions, measurement frequencies | MAPPED |
| DOC-002 p. 7 | Intervention doses, external supplement limits, randomization and drop-out/sample-size rule | MAPPED |
| DOC-002 p. 8 | Time-to-event endpoint, censoring, Cox/AFT/logistic/person-time analysis definitions | MAPPED |
| DOC-002 p. 9 | Interim alpha spending, nested case-control projected cases/matching/tests, secondary endpoint analyses | MAPPED |
| DOC-002 p. 10 | Data-entry QC sample, CI and re-entry threshold; recruitment/census quantities | MAPPED |
| DOC-002 pp. 11–12 | External-supplement numeric context, projected power restatement, dose/adherence/retention statements | MAPPED |
| DOC-003 p. 1 | Contents/index only; no result display beyond figure scope labels | NO_APPLICABLE_RESULT_UNIT |
| DOC-003 p. 2 | eFigure 1 post hoc cancer-incidence curve, exclusions, risk sets, duration, log-rank P | MAPPED |
| DOC-003 p. 3 | eFigure 2A residual/model and serum-level range | MAPPED |
| DOC-003 p. 4 | eFigure 2B coefficient, P, HR, CI, baseline/range and loess bands | MAPPED |
| DOC-003 p. 5 | eFigure 2C rescaled HR display and scale | MAPPED |
| DOC-003 p. 6 | Time-varying-covariate and age-adjusted Cox/post hoc model narrative | MAPPED |

## DOC-002: protocol/research-design quantitative evidence

### Design, recruitment, retention, intervention, and measurement

- **SN001 — DOC-002 p.1:** randomized double-blind placebo-controlled planned trial: 2,300 healthy independently living women aged 60+ years in nine counties; calcium 1,200 mg/day plus vitamin D 2,000 IU/day versus calcium/vitamin-D placebo; planned individual follow-up 4 years. Key: planned randomized contrast / all-cancer incidence / women 60+.
- **SN002 — p.1:** planned nested case-control analysis after four years uses serum 25OHD at randomization and end of year 1; for each cancer case, 2 controls matched by age and race. Key: serum 25OHD–cancer association / nested case-control.
- **SN003 — p.2 Table 4 (geometry checked in rendered PDF):** four sequential recruitment cohorts of 383, 767, 767, and 383 sum to 2,300. Projected cohort retention runs 383→333, 767→667, 767→667, and 383→333 across visits V1–V9. Totals printed: entered 2,300; finished 2,000; lost 300; lost/entered 13.0%; grand total visits 19,324. Visits by project year: 3,430; 4,443; 4,290; 4,143; 3,018. Key: planned recruitment/attrition/visits.
- **SN004 — p.3:** eligibility includes women ≥60 years, ≥4 years since last menses; reported context cancer rates: Nebraska 1.2%/year (60–69), 1.7%/year (70–79), 1.8%/year (70+); pilot control 2%/year, intervention 0.5%/year, overall 1.2%/year; pilot post hoc power ~66% for unadjusted RR 0.4. These are planning/pilot comparators, not current-trial results.
- **SN005 — pp.3–4 Table 5:** planned power at n=2,300 under base annual cancer rates 2%, 1.5%, 1.0%: RR 0.6 = 62%,50%,36%; RR 0.5 = 82%,71%,54%; RR 0.4 = 95%,87%,72%; RR 0.25 = 100%,98%,92%. Assumptions: hazard-rate ratio 1.0 for first 6 months, specified effect by third 6-month period, intermediate second period, 1.5% loss/period; SamplePower 2.0/Arcsin method. Planned two samples of 1,150 and ≥1,000/group after anticipated 13% attrition. Key: planned all-cancer power.
- **SN006 — pp.3–4 Table 6:** pilot site-specific values and planned power at 1,000/group, alpha=0.10: breast P=.062, RR=.216, CI .043–1.079, power 89%; lung P=.188, RR=.218, CI .023–2.107, power 81%; lymphoma/leukemia/myeloma P=.367, RR=.437, CI .073–2.634, power 33%. Narrative rounds breast and lung RR to 0.22; colon RR not computable after year 1 because one case. Key: pilot site-specific comparison / RR/CI/P.
- **SN007 — p.4:** recruitment context: previous pilot recruited 1,180 women; estimated 51,000 households in area; replicate increments 1,000; up to 5 attempts/number; claimed >95% listed household phone numbers; callback target within 72 hours. These are administrative/planning quantities only.
- **SN008 — p.5:** ascertainment every semiannual visit; random 10% sample of participants not reporting cancer for physician query. Annual serum 25OHD; baseline and end-year-1 values planned for nested case-control; annual calcium/creatinine. Duplicate blood samples for blinded assay QC; 30 cc blood stored/person at −70 freezer.
- **SN009 — p.6:** histories updated semiannually; height/weight and BMI baseline and annually; physical activity baseline/final; adherence visits every 6 months; falls recalled over previous 6 months. Secondary chronic-disease endpoints: hypertension, cardiovascular disease, osteoarthritis, colonic adenomas, diabetes; acute viral symptoms also assessed. FFQ approximately 110 items and 30–40 minutes; IPAQ has 7 questions, reported test-retest Spearman .88 and median criterion-validity correlation .30.
- **SN010 — p.7:** planned active regimen: calcium carbonate 600-mg caplet twice/day (=1,200 mg/day) and vitamin D3 capsule ≥2,000 IU/day; annual potency checks. Allowed nonstudy calcium 500–600 mg/day; vitamin D limits stated as ≤400 IU/day if <70 and wording “to more than 600 IU/day” if ≥70 (printed wording preserved). Planned block randomization in blocks of length 2, 2,300 assigned placebo versus vitamin-D/calcium. Power statement: need 2,000 participants for >80% power, with 13% expected drop-out yielding total n=2,300.

### Planned endpoints and statistical definitions

- **SN011 — p.8:** primary endpoint is time to first cancer diagnosis from personal entry date. No-event participants right-censored at study end or loss to follow-up (including death, moving, unable to continue). Primary planned methods: Cox regression, including time-dependent covariates; coefficient is change in log hazard ratio for a 1-unit covariate increase. AFT model proposed as cross-check; two-sided P<.05 significance; SAS 9.1 LIFEREG/LIFETEST/PHREG. Key: primary time-to-event analysis.
- **SN012 — p.8:** supplementary planned logistic event Yes/No analysis, covariate-adjusted. Person-time from entry to cancer diagnosis, death, or end follow-up, whichever first; incidence rate = incident cases/person-years; research unit person-year; exposure-category RR = category incidence rate / lowest-category rate using GENMOD. Smoking planned categories: never/former/current; current 0, 1–14, 15–34, ≥35 cigarettes/day; pack-years calculated.
- **SN013 — p.9:** interim analysis described as initially not planned but provisioned, then planned at middle/end of 2nd treatment year for all subjects; confidential DSMB/study-statistician review and no unplanned interim analyses. Alpha-spending α′(0)=0, α′(.5)=.0025, α′(1)=.05; control versus treatment comparison at t=.5 uses α′. Key: interim/type-I rule.
- **SN014 — p.9:** planned nested case-control: incident cancer cases years 2–4; expected 75 total = 25/year, about 5 (0.5%) of 1,000 effective treated and 20 (2%) of 1,000 effective controls/year; 1:2 case:control matching by age/race, age within ±1 year. Seasonally adjusted 25OHD; proposed two-sided t test on 75 case-minus-mean-of-2-control year-1 differences, null mean 0, alpha .05; alternative matched-pair model and baseline-to-year-1-change model.
- **SN015 — p.9:** planned specific-cancer secondary endpoints breast/lung/colon/lymphoma-leukemia-myeloma: Fisher exact where possible otherwise Yates-corrected chi-square; proportional-hazards where size allows; baseline and year-1 25(OH)D quintiles, upper-vs-lower comparison and trend. Similar framework for hypertension, cardiovascular disease, osteoarthritis, colonic adenomas, diabetes, upper-respiratory infections and falls; explicitly not powered for noncancer endpoints.
- **SN016 — p.10:** data-entry QC: quarterly 10% random sample of biweekly dataset; 95% CI for error proportion; whole quarterly dataset rejected/re-entered if upper CI bound >0.05%, otherwise accepted.
- **SN017 — pp.10–12:** planning/context values: prior pilot n=1,180; >26,000 women aged 60+ in sampled counties; external supplements in pilot median (IQR) calcium 375 mg/day (0–762), vitamin D 200 IU/day (0–400); baseline 25OHD 75.7 versus 62.3 nmol/L (difference 13.4) among vitamin-D users versus nonusers; treatment rise ~25 nmol/L. WHI context 29,000 in calcium/vitamin-D arm; proposed 2,300 (<10%). Stated expected power 87%–98% at 1.5%/year and RR=.25; 87% for RR=.4; previous vitamin-D adherence 86%, expected completion 87%, follow-up every 6 months. These are protocol rationale/planning and not matched current-trial outcome claims.

## DOC-003: supplementary post hoc results and statistical evidence

- **SN018 — p.2 eFigure 1 (visual check):** post hoc invasive-or-in-situ cancer-incidence Kaplan–Meier function, years 2–4. Excludes 84 active and 78 placebo participants who withdrew or had cancer before completing year 1. Median follow-up 4.0 years both groups. Log-rank P=.0469. Risk sets (Active/Placebo) at years 1,2,3,4: 1,072/1,069; 1,042/1,037; 1,016/1,008; 658/659. Curves end at approximately .032 active and .049 placebo; these are graphical coordinates, not printed exact estimates. Key: post hoc treatment comparison / invasive or in-situ cancer / years 2–4.
- **SN019 — p.3 eFigure 2A:** martingale residuals from Cox PH model with age alone versus serum 25(OH)D; loess overlay. Serum range 6–107 ng/mL; vast majority 30–55 ng/mL. Key: functional-form/model diagnostic.
- **SN020 — p.4 eFigure 2B (visual check):** age-adjusted Cox/loess statement: achieved 25(OH)D inversely associated with cancer, P=.03, coefficient −.017. Relative to 30 ng/mL baseline, estimated cancer HR for 30–55 ng/mL = .65 (CI .44–.97). Figure labels 95% confidence bands and the red reference x values 30/55. Key: post hoc serum 25(OH)D association / HR.
- **SN021 — p.5 eFigure 2C (visual check):** same curve as 2B rescaled to HR units, age-adjusted; 95% confidence bands shown. Vertical scale maps 30 ng/mL to HR 1 and supports direct interpretation; no additional printed point estimate.
- **SN022 — p.6:** 25(OH)D is time-varying across two intervals: enrollment to second measure at end of year 1, withdrawal, or cancer diagnosis (first), then second measure to end follow-up; baseline value first interval and second-measurement value second interval. Martingale residuals range 1 to −infinity, are skewed, and loess used to show structure. Age-adjusted Cox residual loess indicates apparent linearity 30–55 ng/mL; changes outside coincide with wide bands/inadequate data; 2C maps level 30 to 0, level 55 to Cox-model offset, then exponentiates. Key: post hoc model construction and figure transformation.

## Cross-document match keys and limitations

Primary match keys for canonical merge: (1) planned trial regimen / n=2,300 / 4-year follow-up; (2) planned all-cancer survival endpoint; (3) planned versus actual/secondary post hoc invasive-or-in-situ cancer years 2–4; (4) serum 25(OH)D cancer association, with explicit distinction between planned nested case-control and DOC-003 post hoc age-adjusted time-varying Cox analysis. Do not treat protocol projections/pilot figures as current-trial outcome values without matching population, time, model, and purpose.

Limitations: DOC-002 is a planning document, so its projections and pilot values are not expected to equal final trial results. DOC-003 p.6 heading glyphs are corrupt in extracted text, but the body text was legible and corroborated by rendered/OCR assets. Figure endpoints are graphical readings unless the caption prints an exact value.
