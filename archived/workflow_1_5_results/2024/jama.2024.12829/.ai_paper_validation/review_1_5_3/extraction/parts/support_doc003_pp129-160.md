# Support Quantitative Evidence Mapping — DOC-003, PDF pages 129–160

## Scope, source authority, and extraction method

- **Direct source:** `joi240088supp2_prod_1746815064.36071.pdf` (DOC-003), PDF pages 129–160 inclusive (32 fresh-required PDF-page units).
- **Source type:** protocol/SAP compilation. These pages contain the closing pages of one undated SAP, a blank separator, and Version 2.0 of the SAP dated September 9, 2022. They contain planned definitions and analysis specifications, not trial result tables.
- **Fresh extraction:** `pdftotext` native and layout output was generated independently from the direct PDF for every assigned page at `preprocessing/support_doc003_pp129-160/page-129` through `page-160` (`.native.txt` and `.layout.txt`). PDF page 144 was additionally rendered and visually confirmed to contain only the document header, line numbers 2431–2432, and its page number; it has no result-relevant quantitative content.
- **Mapping status:** COMPLETE for 32/32 assigned pages. This artifact maps evidence only; it does not make a candidate finding or adjudication.

## Main-paper matching keys

The following source-grounded keys permit later matching to the main article (`jama_sun_2024_oi_240088_1746815064.14747.pdf`), without asserting that differently dated SAP plans are results.

| Key | Support-source definition/location | Matched main-paper result or design identity |
|---|---|---|
| MPK-01 | BASIS: balloon angioplasty plus aggressive medical management (AMM) versus AMM alone; 1:1 allocation (PDF pp. 132–133 and 151). | Main article title/design and intervention comparison: balloon angioplasty plus AMM versus AMM alone.
| MPK-02 | Composite primary endpoint: stroke/death within 30 days after enrollment or angioplasty, or ischemic stroke/revascularization in the qualifying artery after day 30 through 12 months (PDF pp. 130, 136, 148, 155). | Main article primary outcome uses the same 30-day plus day-31-to-12-month composite structure.
| MPK-03 | Time-to-event primary analysis: Kaplan-Meier event rates with 95% CIs, log-rank comparison, and Cox-model HR with 95% CI (PDF pp. 139 and 159). | Main article reports the primary outcome as 4.4% versus 13.5%, HR 0.32 (95% CI, 0.16–0.63), P < .001.
| MPK-04 | Version 2.0 sample-size plan: anticipated 15% medical-group versus 7% angioplasty-group primary outcome (8 percentage-point absolute difference), 512 total/256 per group, 80% power, one-sided alpha 2.5%, and 10% dropout (PDF p. 153). | Main article reports 512 randomized and 501 confirmed eligible/completing the trial. The plan is a prespecified design value, not a result numerator or denominator.
| MPK-05 | Secondary endpoint family: 30-day, 90-day, 12-month, 24-month, and 36-month stroke/death, mRS, restenosis, revascularization, combined vascular events, and EQ-5D (PDF pp. 149–150). | Main article states it reports 1-year results and describes the corresponding 30-day/1-year and longer-term secondary-outcome family; 24- and 36-month outcomes are not reported in the article.
| MPK-06 | Prespecified treatment-effect subgroup modelling: Cox-model interaction tests and forest plot; age, sex, hypertension, diabetes, smoking, renal function, stenosis, BMI, hypoperfusion/collateral status, circulation, and qualifying mechanism (PDF pp. 140 and 160). | Main article reports subgroup/interactions in its results displays; this SAP supplies the planned model/contrast key.
| MPK-07 | Centre-adjusted Cox HR is a sensitivity analysis (PDF pp. 136, 156). | Main article reports a post hoc centre-effect-adjusted analysis as similar to the main analysis; the plan provides the sensitivity-analysis label.

## Quantitative and statistical evidence

### Earlier SAP section (PDF pages 130–142; continuation listed on p. 129)

**Endpoint definitions and time windows.**

- **Primary endpoint (PDF pp. 130 and 136):** ischemic/hemorrhagic stroke or all-cause death within 30 days after enrollment or after qualifying-lesion balloon angioplasty during follow-up, **or** ischemic stroke or revascularization from/of the qualifying artery beyond 30 days through 12 months after enrollment.
- **Secondary endpoints (PDF pp. 130–131):** target-territory stroke (ischemic or hemorrhagic) or all-cause death at 90 days and 12 months; non-target-territory stroke at 90 days and 12 months; mRS at 90 days and 12 months; qualifying-artery revascularization within 1 year; restenosis within 12 months; combined stroke/myocardial infarction/vascular death within 12 months; EQ-5D within 12 months.
- **Restenosis definition (PDF p. 131):** target-artery stenosis **>70%** or increased by **30%**, on follow-up neurovascular imaging.
- **Safety window (PDF p. 131):** all patients evaluated from enrollment through 1 year. Listed measurements include vital signs, laboratory measures, adverse events (AEs), and serious AEs.

**Hypothesis, design, treatments, and sample size.**

- **Hypothesis (PDF p. 132):** balloon angioplasty plus AMM could decrease primary-endpoint risk by **50%** versus AMM alone during more than 12 months of follow-up.
- **Eligibility/design labels (PDF p. 132):** prospective multicentre randomized open-label blinded-endpoint (PROBE) trial; sICAS defined as recent TIA **<90 days** or ischemic stroke **21–90 days** attributed to **70%–99%** atherosclerotic stenosis; random allocation **1:1**.
- **AMM regimen and targets (PDF p. 133):** aspirin **100 mg daily** for the whole follow-up; clopidogrel **75 mg daily** for the first **90 days**; atorvastatin **20–80 mg/day** for 1 year; LDL target **<1.8 mmol/L** or **<70 mg/dL**; blood-pressure target **130–140/90–100 mm Hg**. The first **100** participants completing peri-operative (**30-day**) observation were to inform interim feasibility discussion.
- **Interim-analysis specification (PDF p. 134):** analysis when half of patients completed the 12-month visit; interim alpha **0.0015**, final alpha **0.024**.
- **Sample-size specification (PDF p. 134):** assumed 12-month target-vessel stroke/death rate **12.2%**; **80%** power; two-sided alpha **0.05**; **50% relative reduction** to **6.1%**; O'Brien-Fleming spending function assumed to expand total type-I error by **6%**; calculated n **686**, increased to **728** for interim analysis, and **802** final after allowing **10%** loss to follow-up.

**Analysis populations and comparison.**

- **ITT (PDF p. 134):** randomized patients receiving the study intervention; analysed according to randomized intervention; primary efficacy population.
- **PPS (PDF p. 135):** subset of FAS (mITT); patients completing treatment or without serious protocol violation; secondary endpoint-evaluation set. Partial violators contribute through the time of violation.
- **ATS (PDF p. 135):** randomized patients with more than one use of study products; analysed according to intervention received; secondary endpoint-evaluation set.
- **Safety set (PDF p. 135):** patients receiving at least one use of study products with safety assessment available.
- **Comparison (PDF p. 136):** balloon angioplasty plus AMM versus AMM alone for the stated composite primary endpoint in high-risk sICAS.

**Statistical definitions and sensitivity/subgroup plans.**

- **General inference (PDF p. 136):** SAS 9.4; statistics two-sided; **P < 0.05** regarded as significant.
- **Centre sensitivity analysis (PDF p. 136):** main analyses do not adjust for centre effects; centres with small sample sizes may be pooled; centre-adjusted sensitivity analysis uses a Cox proportional-hazards model to calculate the treatment-effect HR.
- **Subgroups (PDF p. 136):** primary-outcome rate at each covariate level; treatment-effect heterogeneity assessed by interaction tests. Covariate values are not enumerated in this earlier SAP section.
- **Multiplicity (PDF p. 137):** one primary efficacy variable and one treatment comparison; no multiplicity adjustment for multiple comparisons or endpoints.
- **Missing-data/withdrawal convention (PDF p. 137):** withdrawal visit assigned to the next scheduled visit for summaries/clinic-visit analysis; participants with at least one post-baseline measure included for that endpoint; participants with no post-randomization visits excluded from all endpoint analyses.
- **Event-rate formula (PDF p. 137):** treatment-group event rate = **sum of the number of events for all patients / sum of treatment periods for all patients**. The plan explicitly distinguishes people/person-time and event rate.
- **Time-to-event convention (PDF pp. 137–138):** Kaplan-Meier approach for risk of stroke or combined vascular event; first event is modelled when multiple events of the same type occur; censor at study termination or death if no event occurs.
- **Disposition/deviation conventions (PDF p. 138):** report counts in each analysis population, exclusions from PPS, clinic-visit attendance, randomization/completion/premature withdrawal by group, reasons for withdrawal, and protocol-deviation listings. Protocol violators remain in FAS (mITT) but are excluded from PPS; partial violators have only relevant post-violation data excluded.
- **Baseline summaries (PDF p. 139):** continuous variables as median (interquartile range), compared by Wilcoxon rank-sum; categorical variables as n (%), compared by chi-squared or Fisher exact test.
- **Primary efficacy analysis (PDF p. 139):** composite event rates and **95% CIs** estimated by Kaplan-Meier; log-rank comparison; Cox proportional-hazards HR with **95% CI**. ITT is main analysis; PPS and ATS are sensitivity analyses, with detailed analysis required if their results are inconsistent with ITT.
- **Defined subgroup levels and model (PDF p. 140):** separate Cox model for each treatment-by-subgroup interaction, displayed in a forest plot. Levels: age <65 versus >=65 years; sex; hypertension; diabetes; smoking; eGFR <60 versus >=60 mL/min/1.73 m2; target-vessel stenosis <80% versus >=80%; BMI <25, 25–30, or >=30 kg/m2; hypoperfusion/CTP/ASITN-SIR collateral scale; anterior versus posterior circulation; ischemic stroke versus TIA mechanism.
- **Secondary efficacy analysis (PDF p. 141):** target- and non-target-territory stroke/death outcomes at 90 days/12 months and combined vascular events: Cox model with HR and **95% CI**; mRS at 90 days/12 months: ordinal logistic regression yielding common OR; restenosis: logistic regression yielding OR and **95% CI**; EQ-5D: Student t test or Wilcoxon rank-sum as appropriate.
- **Safety/concomitant medication (PDF p. 142):** AE count and percentage summarized by system-organ class and preferred term; Fisher exact test for between-group AE-event counts and deaths; vital signs described/compared by time point; concomitant medication group counts compared by chi-squared or Fisher exact test. MedDRA version **26 or later** is the AE coding dictionary.

### SAP Version 2.0 (cover PDF p. 145; contents pp. 146–147; substantive section pp. 148–160)

**Version identity.** PDF p. 145 identifies the document as the BASIS Statistical Analysis Plan, **Version 2.0, September 9, 2022**. The contents on pp. 146–147 confirm that the substantive SAP begins at PDF p. 148 and continues beyond the assigned p. 160 boundary.

**Endpoint definitions and time windows.**

- **Primary endpoint (PDF p. 148):** stroke/death within 30 days after enrollment or qualifying-lesion balloon angioplasty, or ischemic stroke/revascularization of the qualifying artery beyond 30 days through 12 months after enrollment.
- **Secondary endpoints (PDF pp. 148–150):** any stroke/all-cause death within 30 days; target-territory stroke/all-cause death at 90 days, 12 months, 24 months, and 36 months; non-target-territory stroke at the same windows; mRS at 90 days, 12 months, and 24 months; neurological improvement by mRS at 36 months; target-artery revascularization within 12 months; restenosis within 12 months; combined stroke/MI/vascular death within 12, 24, and 36 months; EQ-5D within 12 months.
- **Restenosis definition (PDF p. 149):** stenosis **>70%** or increased by **30%** on follow-up neurovascular imaging.
- **Safety (PDF p. 150):** assessment from enrollment to 1 year, including vital signs, listed blood/laboratory testing, AEs, and serious AEs.

**Hypothesis, design, treatments, and sample size.**

- **Hypothesis (PDF p. 151):** **50%** primary-endpoint risk reduction with angioplasty plus AMM during more than 12-month follow-up.
- **Design/eligibility (PDF p. 151):** prospective multicentre PROBE trial, sICAS attributed to **70%–99%** atherosclerotic stenosis of specified ICA C4–C7, MCA M1, VA V4, or BA lesions; randomization **1:1**. Site consistency process specifies **3–5** angioplasty-case videos per centre before continued enrollment.
- **AMM regimen and targets (PDF pp. 151–152):** aspirin **100 mg daily** throughout follow-up; clopidogrel **75 mg daily** for **90 days**; atorvastatin **20–80 mg/day** for 1 year; LDL **<1.8 mmol/L** or **<70 mg/dL**; blood pressure **130–140/90–100 mm Hg**. The first **100** participants were to complete a **30-day** peri-operative observation for AE-focused discussion.
- **Interim/DSMB plan (PDF p. 153):** no interim efficacy analysis; DSMB receives regular summary data and may recommend trial modification or early stopping for safety.
- **Sample size (PDF p. 153):** anticipated primary-outcome rate **15%** in medical group and **7%** in angioplasty group, an **8 percentage-point absolute difference**; n **512 total (256/group)** for **80%** power, one-sided alpha **2.5%**, and **10%** dropout.

**Population definitions, inference, and sensitivity/subgroup plans.**

- **ITT/PPS/ATS/safety populations (PDF pp. 153–154):** same core definitions as the earlier SAP: ITT randomized/treated analysed by randomization and primary efficacy population; PPS subset of FAS (mITT), secondary; ATS analysed by treatment received, secondary; safety set received at least one study product plus safety assessment.
- **General inference (PDF p. 155):** SAS 9.4; two-sided statistics; **P < 0.05** significant.
- **Centre sensitivity (PDF pp. 155–156):** no centre adjustment in main analysis; pooled small centres as necessary; centre-effect analysis is sensitivity analysis using Cox model for treatment-effect HR.
- **Subgroup/multiplicity (PDF p. 156):** primary-outcome rate by covariate level and interaction tests; one primary efficacy variable/one treatment comparison and no multiplicity adjustment.
- **Missing data/event-rate/time-to-event (PDF p. 157):** same withdrawal and inclusion conventions as earlier SAP; event-rate formula is **sum of events / sum of treatment periods**; use Kaplan-Meier time-to-event methods and first event; censor at termination/death if no event.
- **Disposition/deviation conventions (PDF p. 158):** report analysis-population counts, PPS exclusions, visit attendance, randomized/completed/withdrawn counts by group and withdrawal reasons; FAS (mITT) includes protocol violators while PPS excludes them, with partial-violation data restricted to pre-violation information.
- **Baseline and primary analysis (PDF p. 159):** median (IQR)/Wilcoxon rank-sum for continuous variables and n (%)/chi-squared or Fisher exact test for categorical variables; primary Kaplan-Meier composite event rates with **95% CIs**, log-rank comparison, and Cox HR with **95% CI**. ITT main analysis, PPS/ATS sensitivity analyses.
- **Subgroup levels and model (PDF p. 160):** separate Cox interaction model/forest plot; same listed levels as earlier SAP: age <65 versus >=65, sex, hypertension, diabetes, smoking, eGFR <60 versus >=60 mL/min/1.73 m2, stenosis <80% versus >=80%, BMI <25/25–30/>=30 kg/m2, hypoperfusion/CTP/ASITN-SIR, circulation, and ischemic stroke versus TIA mechanism. PDF p. 160 starts the secondary-efficacy section, which continues outside this shard.

## Page-by-page complete coverage

| PDF page | Unit coverage and result relevance |
|---:|---|
| 129 | Contents for the earlier SAP; maps sections 12.1–12.5 and reference to pp. 139–142. No standalone result relationship. |
| 130 | Earlier SAP introduction, primary endpoint, beginning secondary endpoint list; mapped above. |
| 131 | Earlier SAP secondary endpoints, restenosis threshold, safety scope; mapped above. |
| 132 | Earlier SAP hypothesis/design/eligibility/allocation; mapped above. |
| 133 | Earlier SAP treatments, doses/targets, first-100/30-day discussion, planned-analysis conditions; mapped above. |
| 134 | Earlier SAP interim alpha plan, sample-size values, ITT beginning; mapped above. |
| 135 | Earlier SAP PPS/ATS/safety definitions; mapped above. |
| 136 | Earlier SAP comparison, P threshold, centre sensitivity, subgroup interaction concept; mapped above. |
| 137 | Earlier SAP multiplicity, missingness, event-rate formula, time-to-event beginning; mapped above. |
| 138 | Earlier SAP time-to-event censoring and disposition/deviation conventions; mapped above. |
| 139 | Earlier SAP baseline and primary-endpoint analysis definitions; mapped above. |
| 140 | Earlier SAP subgroup levels/models and secondary-analysis heading; mapped above. |
| 141 | Earlier SAP secondary analysis models/effect measures and safety-analysis beginning; mapped above. |
| 142 | Earlier SAP AE/death/vital-sign/concomitant-medication analyses; mapped above. |
| 143 | Reference list only; no trial result-relevant quantitative relationship. |
| 144 | Visually confirmed separator page with header/line numbers/page number only; no applicable quantitative content. |
| 145 | SAP Version 2.0 cover/date; administrative identity only. |
| 146 | Version 2.0 contents (sections through 11.2); administrative navigation only. |
| 147 | Version 2.0 contents (sections 12–13); administrative navigation only. |
| 148 | Version 2.0 introduction, objective, primary endpoint, secondary-list beginning; mapped above. |
| 149 | Version 2.0 secondary endpoints and restenosis threshold; mapped above. |
| 150 | Version 2.0 extended secondary endpoints and safety scope; mapped above. |
| 151 | Version 2.0 hypothesis/design/eligibility/randomization/treatment beginning; mapped above. |
| 152 | Version 2.0 treatment doses/targets, first-100/30-day discussion, planned-analysis conditions; mapped above. |
| 153 | Version 2.0 DSMB/no-interim statement, sample size, ITT beginning; mapped above. |
| 154 | Version 2.0 population definitions; mapped above. |
| 155 | Version 2.0 treatment comparison, P threshold, centre-effect analysis beginning; mapped above. |
| 156 | Version 2.0 centre sensitivity, subgroup/multiplicity rules, missing-data heading; mapped above. |
| 157 | Version 2.0 withdrawal, event-rate formula, time-to-event conventions; mapped above. |
| 158 | Version 2.0 disposition and protocol-deviation conventions; mapped above. |
| 159 | Version 2.0 baseline/primary analysis model definitions; mapped above. |
| 160 | Version 2.0 subgroup levels/model and start of secondary endpoint section; mapped above; the secondary section continues on unassigned p. 161. |

## Tables, figures, formulas, workbook/structured values, and limitations

- **Tables/figures:** No result table or figure occurs on PDF pp. 129–160.
- **Formulas:** One explicit event-rate formula is present in each SAP version: total events divided by total treatment periods (PDF pp. 137 and 157). No workbook, CSV, XLS/XLSX formula, cached value, or displayed workbook cell occurs in this PDF scope.
- **Protocol/SAP versus result status:** All numerical values in this shard are protocol/SAP definitions, thresholds, dosing targets, planning assumptions, sample-size parameters, or intended analyses. They are retained for cross-document matching but are not treated as observed trial results.
- **Boundary limitation:** Version 2.0 secondary-efficacy analysis begins at PDF p. 160 and continues at p. 161, which is outside this assigned shard and must be covered by the owner of the next page range. No source unit in pp. 129–160 remains unmapped.
