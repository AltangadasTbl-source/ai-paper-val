# DOC-003 support quantitative evidence: PDF pages 33-64

## Scope and extraction record

- **Source ID:** DOC-003.
- **Direct source:** `joi240088supp2_prod_1746815064.36071.pdf`.
- **Exact assigned units:** fresh-required PDF pages 33-64, inclusive (32 of 32 mapped).
- **Method:** fresh direct-source `pdftotext` native and layout extraction for every assigned page. Targeted CPU render inspection was additionally performed for PDF pages 45, 47, and 58 because device-diagram and visual-scale labels were not completely represented by the text layer.
- **Fresh derivatives:** `preprocessing/support_doc003_pp033-064/pages-033-064.native.txt`; `preprocessing/support_doc003_pp033-064/pages-033-064.layout.txt`; one native and one layout text file per assigned page in the same directory; targeted rendered pages `page-045.png`, `page-047.png`, and `page-058.png`.
- **Source type:** protocol/SAP and appendices, not an outcome-results supplement. The protocol text contains prespecified analysis, sample-size, sensitivity, subgroup, outcome-scale, timing, population, and device-parameter relationships that are retained below. No candidate diagnosis or adjudication was performed.
- **Matching main-paper key:** `BASIS randomized clinical trial | balloon angioplasty plus aggressive medical management (AMM) versus AMM | symptomatic intracranial artery stenosis | prespecified 1-year primary composite time-to-event outcome`. Where a relationship is only a protocol definition or measurement scale, its matching key is stated with the entry.

## Result-relevant numeric and reporting relationships

### DOC003-33-64-N01 — Follow-up schedule and measurements

- **Locations:** DOC-003 PDF pp. 33-35.
- **Direct observation:** Visit 3 is discharge. Visit 4 is **30 +/- 7 days** after enrollment; it includes mRS and research-drug distribution. Visit 5 is **90 +/- 7 days** after enrollment and includes mRS and NIHSS. Visit 6 is **6 months +/- 14 days** after enrollment, by telephone, and includes mRS. Visit 7 is **1 year +/- 30 days** after enrollment and includes mRS, NIHSS, MoCA, EQ-5D, MRI/HRMRI or CT when MRI is unavailable, CTP, DSA, and optional/recommended qualifiers as printed. Thereafter, follow-up is every **6 months +/- 30 days** after the 1-year enrollment point; telephone visits include smoking/weight/exercise, aspirin follow-up, and AE/SAE/endpoint observation, while face-to-face visits also include mRS, MoCA, EQ-5D, aspirin/atorvastatin orders, and AE/SAE/endpoint observation.
- **Printed label/detail:** p. 35 lists “visit 8, visit 9, visit 10, visit 11, visit 9, and visit 11” as the recurring visits. This exact repeated numbering is retained as source text; no inference about an intended visit sequence is made.
- **Matching main-paper key:** follow-up time point; outcome-assessment schedule; 1-year primary-outcome horizon.

### DOC003-33-64-N02 — Restenosis threshold and revascularization-management rule

- **Locations:** DOC-003 PDF p. 36.
- **Direct observation:** In the experimental group, transient ischemia or ischemic stroke accompanied by DSA-diagnosed restenosis **>=70%** triggers expert advice on revascularization or medical management alone; revascularization is not recommended for restenosis **<70%**.
- **Matching main-paper key:** post-procedure clinical-event management; stenosis threshold.

### DOC003-33-64-N03 — Primary-endpoint event and adjudication timings

- **Locations:** DOC-003 PDF p. 36.
- **Direct observation:** Endpoint events are target-vessel hemorrhagic stroke, ischemic stroke, death, and target-vessel revascularization. A potential primary endpoint must be reported within **48 hours**; the event arbitration committee is to complete arbitration within **7 days**. The committee has **3 members**: two conduct initial back-to-back arbitration and a third casts the decisive vote if opinions differ.
- **Matching main-paper key:** primary composite outcome definition and adjudication process.

### DOC003-33-64-N04 — Adverse-event collection and reporting timing

- **Locations:** DOC-003 PDF pp. 36-37.
- **Direct observation:** AE/SAE collection starts with informed-consent signing and continues through study end; SAEs for people discontinuing treatment early are recorded. A SAE is to be reported in writing within **24 hours** to the institution, ethics committee, and sponsor.
- **Matching main-paper key:** safety-outcome collection window and reporting process.

### DOC003-33-64-N05 — Procedure-risk timing

- **Locations:** DOC-003 PDF p. 38.
- **Direct observation:** Acute vessel occlusion is described as usually occurring within **30 minutes** after balloon angioplasty.
- **Matching main-paper key:** peri-procedural safety-event timing.

### DOC003-33-64-N06 — Core-laboratory blinding and experience label

- **Locations:** DOC-003 PDF p. 39.
- **Direct observation:** Imaging is blinded to clinical features and treatment options and is reviewed by MRI and DSA experts with **over 10 years’** working experience.
- **Matching main-paper key:** blinded imaging assessment.

### DOC003-33-64-S01 — Prespecified primary and secondary analysis framework

- **Locations:** DOC-003 PDF p. 40.
- **Direct observation:** Primary-outcome composite event rates and corresponding **95% CIs** in the two treatment groups are estimated by Kaplan-Meier survival analysis and compared using a log-rank test. A between-group hazard ratio and **95% CI** are calculated with a Cox proportional-hazards regression model. Secondary time-to-event endpoints use Kaplan-Meier and Cox regression; common odds ratios of mRS use ordinal logistic regression. Secondary-outcome interval widths are **not adjusted for multiplicity**.
- **Population/model labels:** main analysis is intention-to-treat; per-protocol and as-treated analyses are sensitivity analyses; SAS version **9.4** is named. Detailed missing-data imputation and subgroup methods are said to be in the SAP.
- **Matching main-paper key:** primary time-to-event effect measure (hazard ratio), primary 95% CI/log-rank P value, ordinal mRS analysis, and analysis-population labels.

### DOC003-33-64-S02 — Sample-size basis and inflation steps

- **Locations:** DOC-003 PDF pp. 40-41.
- **Direct observation:** The protocol bases its calculation on a SAMMPRIS-derived **12.2%** 12-month target-vessel stroke-or-death incidence in the experimental group. It specifies **686 cases**, **80% power**, two-sided **alpha = 0.05**, and a planned **50% relative reduction** to **6.1%** after balloon angioplasty. The O’Brien-Fleming spending function is assumed to cause **6%** expansion of total type-I error; mid-term-analysis calculation increases the required size to **728 cases**; allowing **10%** loss to follow-up yields a final sample size of **802 cases**.
- **Arithmetic/relationship notes:** 12.2% multiplied by one minus 50% equals 6.1%. The sequence 686 -> 728 -> 802 is printed as the design calculation; its unprinted rounding/calculation inputs are not inferred here.
- **Matching main-paper key:** randomized sample size, primary-outcome event-rate assumption, effect-size assumption, and follow-up-loss allowance.

### DOC003-33-64-S03 — Interim-analysis definition and alpha labels

- **Locations:** DOC-003 PDF p. 41.
- **Direct observation:** Interim analysis occurs when **half** of patients have finished the **12-month** visit. The mid-term alpha is printed as **alpha1 = 0.0015** and final-analysis alpha as **alpha2 = 0.024**.
- **Matching main-paper key:** interim-analysis plan and alpha thresholds.

### DOC003-33-64-S04 — Prespecified subgroup strata

- **Locations:** DOC-003 PDF p. 41.
- **Direct observation:** Primary-outcome subgroups are age **<65 versus >=65 years**, sex, hypertension, diabetes, smoking, baseline renal function **eGFR <60 versus >=60 mL/min/1.73 m2**, target-vessel stenosis **<80% versus >=80%**, BMI **<25, 25-30, versus >=30 kg/m2**, hypoperfusion, lesion location, and mechanism (ischemic stroke versus TIA).
- **Matching main-paper key:** subgroup forest-plot/table categories and units.

### DOC003-33-64-N07 — Monitoring and study-governance frequencies

- **Locations:** DOC-003 PDF p. 42.
- **Direct observation:** The DSMB is scheduled to meet **annually**. The steering committee meets **twice a year**. The leading-center clinical research team and project team review trial progress/data monitoring online **each week**.
- **Matching main-paper key:** governance only; no directly matched main-paper efficacy result is expected.

### DOC003-33-64-N08 — Drug-supply duration

- **Locations:** DOC-003 PDF p. 44.
- **Direct observation:** Clopidogrel is free during a screening period of **3-5 days** and for the **90-day** enrollment period; atorvastatin is free for **1 year**. Continued use after those time points is based on patient condition.
- **Matching main-paper key:** AMM medication regimen and exposure duration.

### DOC003-33-64-N09 — Neuro RX device dimensions and visual labels

- **Locations:** DOC-003 PDF p. 45, including direct visual inspection of the device diagram.
- **Direct observation:** The Neuro RX catheter has a printed working length of **145 cm**, guide wire **<0.014 inch**, catheter inner diameter **>=5F (0.056 inch)**, and guide-wire exit **24 cm** from the far tip. The diagram labels a **2F proximal shaft** and **3F distal shaft**, plus the device components/markers.
- **Matching main-paper key:** intervention-device specification; no main-paper efficacy-result match is expected.

### DOC003-33-64-N10 — Neuro LPS device registration date

- **Locations:** DOC-003 PDF p. 46.
- **Direct observation:** The Neuro LPS catheter registration is printed as NMPA 20203030576 with approval date **2020-06-19**.
- **Matching main-paper key:** intervention-device provenance only; no outcome-result match is expected.

### DOC003-33-64-N11 — Neuro LPS diagram dimensions and material proportions

- **Locations:** DOC-003 PDF p. 47, including direct visual inspection of the device diagram.
- **Direct observation:** The device schematic labels overall L as **1550 +/- 100 mm**. Text defines D1 as expanded-balloon diameter and L2 as effective balloon length, and identifies two markers with **90% platinum** and **10% iridium alloy** composition. It describes the sheath as two layers.
- **Relationship note:** The p. 45 printed 145-cm working length is the lower bound of the p. 47 diagram’s 1550 +/- 100-mm overall-L range (1450-1650 mm), but the source uses different labels (“working length” versus diagram L/effective catheter length). This is retained as a label-matching question for later cross-source review, not a conclusion.
- **Matching main-paper key:** intervention-device specification; no direct efficacy-result match expected.

### DOC003-33-64-N12 — mRS scale definition

- **Locations:** DOC-003 PDF p. 52.
- **Direct observation:** The modified Rankin Scale is an ordinal hierarchical scale with scores **0-5**, higher scores indicating more severe disability, and score **6** added for death. The table defines every category from 0 (no symptoms) to 6 (death).
- **Matching main-paper key:** mRS ordinal outcome and direction; common-odds-ratio analysis in DOC-003 p. 40.

### DOC003-33-64-N13 — NIHSS scale range and item definitions

- **Locations:** DOC-003 PDF pp. 53-56.
- **Direct observation:** NIHSS is an ordinal hierarchical stroke-severity scale ranging from **0 to 42**, with higher scores indicating more severe deficit. These pages give assessment and score definitions for items 1a, 1b, 1c, 2-11; included timing/scoring thresholds are 10 seconds for motor arm at 90/45 degrees and 5 seconds for motor leg at 30 degrees. “UN” is restricted as specified for amputation/joint fusion or a physical barrier in particular items.
- **Matching main-paper key:** NIHSS follow-up outcome and direction.

### DOC003-33-64-N14 — EQ-5D-5L and visual-analogue-scale definitions

- **Locations:** DOC-003 PDF pp. 57-58; p. 58 visually confirmed.
- **Direct observation:** Appendix Table 4 is EQ-5D-5L, covering five domains (mobility, self-care, usual activities, pain/discomfort, anxiety/depression), each with five ordered response levels. The visual analogue scale is numbered **0-100**: **100** is best imaginable health and **0** worst imaginable health. The rendered ruler displays 5-point major labels from 0 through 100.
- **Matching main-paper key:** EQ-5D follow-up outcome and scale direction.

### DOC003-33-64-N15 — mTICI grade definitions

- **Locations:** DOC-003 PDF p. 59.
- **Direct observation:** Appendix Table 5 defines mTICI grades **0, 1, 2a, 2b, and 3**, from no perfusion through complete antegrade reperfusion; 2a is less than half and 2b more than half of the previously occluded target-artery ischemic territory.
- **Matching main-paper key:** angiographic/intervention technical endpoint or baseline imaging descriptor; no direct main-paper efficacy-result match expected unless mTICI is reported.

### DOC003-33-64-N16 — Protocol-version and synopsis population/treatment labels

- **Locations:** DOC-003 PDF pp. 60 and 64.
- **Direct observation:** The later protocol section identifies **Protocol Version 2.3**, dated **March 28, 2022**. Its synopsis describes a multicenter, prospective, randomized, open-label, blinded-endpoint (PROBE) trial. Eligible people are **35-80 years** old with recent TIA **<90 days** or ischemic stroke **14-90 days** before enrollment, attributed to **70-99%** atherosclerotic stenosis in named major intracranial arteries. Groups are balloon angioplasty plus AMM versus AMM alone. AMM is aspirin **100 mg daily** throughout follow-up plus clopidogrel **75 mg daily** for the first **90 days** after enrollment; the text says clopidogrel may be replaced by ticagrelor or cilostazol for resistance. The sentence continues beyond the assigned page range.
- **Matching main-paper key:** trial design, eligibility population, randomized comparison, medication regimen, and treatment-window labels.

## Tables, figures, and definitions mapped

| Source location | Object | Result-relevant content |
|---|---|---|
| pp. 42-44 | Table 1, Collaboration team of trial and Study Committee | Administrative study-organization table; p. 42 gives annual, twice-yearly, and weekly governance frequencies. No outcome numeric result appears in the table rows. |
| p. 45 | Neuro RX device diagram | Visual labels 2F proximal shaft and 3F distal shaft; text holds the remaining dimension values. |
| p. 47 | Neuro LPS device diagram | Diagram adds L = 1550 +/- 100 mm; D1 and L2 labels are defined in adjacent text. |
| p. 51 | Appendix Table 1, ASITN/SIR collateral circulation scale | Grades 0-4 and their perfusion/collateral definitions. |
| p. 52 | Appendix Table 2, modified Rankin Scale | Ordered mRS categories 0-6 and direction. |
| pp. 53-56 | Appendix Table 3, NIHSS | Total range 0-42 and detailed component scoring rules. |
| pp. 57-58 | Appendix Table 4, EuroQoL 5D-5L | Five domains, five response levels, and a 0-100 visual analogue scale with anchor direction. |
| p. 59 | Appendix Table 5, mTICI grade | Grades 0, 1, 2a, 2b, and 3; perfusion thresholds and definitions. |

## Explicit no-applicable-unit record

| PDF page(s) | Direct-source finding |
|---|---|
| 43 | Continuation of Table 1 listing teams, institutions, and investigators. It contains no result-relevant number, statistical definition, endpoint result, or effect measure beyond administrative names. |
| 48 | Device accountability/responsibilities narrative. It mentions record fields (date, quantity, serial number, shelf life, unique code) but supplies no study result or defined numerical relationship. |
| 49 | IRB/ethics administrative narrative. A yearly progress-report frequency is recorded in N07; no additional result-relevant quantitative relationship is present. |
| 50 | Reference list only. Citation publication years, volume/pages, and DOI strings are bibliographic rather than results for this supplied trial and were not treated as quantitative study evidence. |
| 60 | Cover page for a later protocol version; version/date are captured in N16, with no outcome result. |
| 61-62 | Contents pages for the later protocol. Printed internal-page references are navigational only; no trial result, table result, or inferential definition is asserted on these pages. |
| 63 | Protocol signature page only; no result-relevant quantitative content. |

## Scope-completion count

- **Assigned PDF pages directly extracted and mapped:** 32/32 (pp. 33-64).
- **Mapped local numeric/reporting relationships:** 16 (N01-N16, including scale, timing, population, medication, and device-unit definitions).
- **Mapped local inferential/statistical relationships:** 4 (S01-S04).
- **Tables/figures/appendix measurement objects mapped:** 9.
- **Candidate diagnoses registered:** 0. This mapping artifact intentionally does not diagnose or assign candidates.
- **Limitation:** The p. 64 synopsis medication sentence continues on PDF p. 65, outside this disjoint assignment; it is not reconstructed here. The protocol’s referenced detailed SAP methods, missing-data imputation, and subgroup methods are not on these pages and therefore are not inferred.
