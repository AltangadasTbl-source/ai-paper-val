# Support Quantitative Evidence Map — DOC-003 PDF Pages 161–167

## Scope and method

- **Direct source:** `joi240088supp2_prod_1746815064.36071.pdf` (DOC-003), PDF pages 161–167 inclusive.
- **Coverage:** 7 of 7 assigned fresh-required PDF pages mapped. No reusable scientific extraction was used.
- **Fresh direct-source extraction:** `pdftotext` native and layout-preserved text were created for each page in `preprocessing/support_doc003_pp161-167/`. Every page was rendered from the direct PDF. Pages 165–166 were visually inspected to retain the two-column alignment of the SAP-version revision table; this table continues across those two PDF pages.
- **Scope boundary:** These pages are protocol/SAP and administrative/reference material, not observed trial-result output. The map records all result-relevant definitions, planned comparisons, historical SAP values, labels, time windows, and formula-like relationships visible in this shard. It assigns no candidate ID, makes no diagnosis, and does not use legacy conclusions.

## Result-relevant quantitative and statistical evidence

### R1 — Prespecified time-to-event secondary-outcome analyses

- **Source:** DOC-003 [PDF p. 161](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=161>), SAP §12.3 continuation.
- **Statistical definition and labels:** The visible continuation states that a qualifying-lesion event after enrollment or balloon angioplasty during follow-up is analyzed with a Cox proportional-hazards model and reported as a hazard ratio (HR) with **95% CI**; the full outcome label begins outside this assigned shard. The following fully visible planned analyses use Cox proportional-hazards models and report HRs with **95% CIs**:
  - any ischemic or hemorrhagic stroke inside the target-artery territory or all-cause death at **90 days, 12 months, 24 months, and 36 months** after enrollment;
  - any ischemic or hemorrhagic stroke outside the target-artery territory at **90 days, 12 months, 24 months, and 36 months** after enrollment;
  - combined stroke, myocardial infarction, and vascular death at **12 months, 24 months, and 36 months** after enrollment.
- **Matching main-paper key:** secondary time-to-event endpoint; target-territory stroke; non-target-territory stroke; all-cause death; composite vascular event; HR; 95% CI; follow-up horizon.

### R2 — Ordinal disability, restenosis, and quality-of-life analysis definitions

- **Source:** DOC-003 [PDF p. 161](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=161>)–[PDF p. 162](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=162>), SAP §12.3 continuation.
- **Statistical definition and labels:**
  - Common odds ratios for modified Rankin Scale (**mRS**) at **90 days, 12 months, 24 months, and 36 months** are estimated with ordinal logistic regression.
  - Target-artery restenosis rate within **12 months** is compared between treatment groups with logistic regression and reported as an odds ratio with **95% CI**. Restenosis is defined as imaging stenosis **>70%** or an increase of **30%** on follow-up neurovascular imaging.
  - EuroQol-5-Dimensions Scale (**EQ-5D**) quality of life within **12 months** after enrollment is tested with Student *t* test or Wilcoxon rank-sum test, as appropriate.
- **Matching main-paper key:** mRS common OR; ordinal disability endpoint; restenosis rate/threshold; OR and 95% CI; EQ-5D outcome; 12-month quality-of-life comparison; test label.

### R3 — Safety-analysis population summaries and comparison rules

- **Source:** DOC-003 [PDF p. 162](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=162>), SAP §12.4.
- **Statistical definition and labels:** Adverse events are coded using MedDRA version **26** or later and grouped by system organ class and preferred term. Within each treatment group, the number and percentage of subjects experiencing an AE are summarized by those groups; Fisher exact test is specified to compare the number of each grouped AE event between treatment groups. Deaths over the treatment period are summarized and compared using Fisher exact test. Vital-sign results at different time points are to be statistically described and compared, with no further test, time points, scale, or summary statistic supplied on these pages.
- **Matching main-paper key:** safety population; adverse-event count and percentage; MedDRA system organ class/preferred term; serious adverse events; death count; Fisher exact test; vital-sign time point.
- **Definition limitation to retain:** The same paragraph uses subject-level number/percentage for AE summaries and “number of each grouped AE event” for the Fisher comparison; this page does not state whether the latter comparison is person-level or event-level.

### R4 — Concomitant-medication comparison plan

- **Source:** DOC-003 [PDF p. 162](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=162>)–[PDF p. 163](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=163>), SAP §12.5.
- **Statistical definition and labels:** Medication listings include antiplatelets (aspirin, clopidogrel, ticagrelor, cilostazol), anticoagulants, lipid-lowering statins, and antihypertensives (diuretic, ACE inhibitor, angiotensin receptor blocker, beta-blocker, calcium-channel antagonist, central alpha agonist, vasodilator). Chi-squared or Fisher exact tests are specified to compare the number between treatment groups.
- **Matching main-paper key:** concomitant medication; antiplatelet/anticoagulant/statin/antihypertensive exposure; treatment-group count; chi-squared test; Fisher exact test.

### R5 — SAP-version 1.0 interim-analysis values versus SAP-version 2.0 rule

- **Source:** DOC-003 [PDF p. 165](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=165>), two-column table “Revisions to previous SAP version,” §5.3.
- **Table/relationship:** The left column, SAP version **1.0**, states that interim analysis occurs when half of patients complete the **12-month** visit, with mid-term analysis **alpha 1 = 0.0015** and final analysis **alpha 2 = 0.024**. The right column, Changes in SAP version **2.0**, states that interim analyses **will not be performed**. It instead describes DSMB review of enrollment, subject status, baseline characteristics, and safety data, including coded SAE summary tables, at regular intervals; an independent statistician prepares those statistics.
- **Matching main-paper key:** interim analysis; alpha-spending/interim threshold; final-analysis alpha; DSMB; trial monitoring; SAP version.

### R6 — Historical and revised sample-size assumptions and totals

- **Source:** DOC-003 [PDF p. 165](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=165>)–[PDF p. 166](<../../../../joi240088supp2_prod_1746815064.36071.pdf#page=166>), two-column table “Revisions to previous SAP version,” §6.
- **Table, formula-like relationships, and labels:**
  - **SAP version 1.0 (left column):** Based on a **12.2%** 12-month target-vessel stroke-or-death incidence in the stated experimental group, a sample size of **686** cases at **80%** power and two-sided **alpha = 0.05** was intended to detect a **50% relative reduction**, written as **6.1%** after balloon angioplasty. The O'Brien-Fleming spending function was assumed to produce **6%** expansion of the total type-I error. SAS calculation for the interim analysis increased the required sample to **728**; allowing **10%** lost to follow-up produced a final sample size of **802** cases.
  - **SAP version 2.0 (right column):** The anticipated composite primary-outcome event rate is **15%** in the medical group and **7%** in the balloon-angioplasty group, an **8-percentage-point absolute difference**. Planned enrollment is **512** patients (**256 per group**), with **80%** statistical power, one-sided **alpha = 2.5%**, and **10%** dropout.
- **Matching main-paper key:** planned/revised randomized total; per-group allocation; primary-composite event risk; absolute risk difference; relative reduction; power; sidedness; alpha; dropout/lost-to-follow-up allowance; interim-analysis plan; SAP-version provenance.
- **Scope note:** These are historical and revised design assumptions in a version-change table, not observed outcome values.

## Explicit no-applicable or context-only units

| PDF page(s) | Direct-source content | Result-relevance disposition |
|---|---|---|
| 161 | SAP §12.3 continuation | Mapped in R1–R2. No observed result table, figure, or trial effect estimate is reported. The opening Cox-model sentence has an outcome label that begins before this shard, so no missing text is inferred. |
| 162 | Completion of EQ-5D test statement; SAP §§12.4–12.5 | Mapped in R2–R4. Safety and medication analysis definitions only; no observed safety or medication results. |
| 163 | Completion of medication section and Reference §13 | Medication test plan mapped in R4. The reference-list entries are no-applicable to result mapping. |
| 164 | Completion of Reference §13 and otherwise blank numbered lines | No result-relevant quantitative relationship beyond bibliographic page/DOI information; no-applicable. |
| 165–166 | Two-column “Revisions to previous SAP version” table | Mapped in R5–R6 after visual alignment confirmation. It contains historical/revised methods and assumptions, not observed trial results. |
| 167 | Blank final PDF page with line numbers only | No-applicable; no result-relevant text, table, figure, formula, or administrative decision is present. |

## Extraction counts and limitations

- **Units mapped:** 7 PDF pages, all fresh-required and directly extracted.
- **Fresh derivatives:** 7 native-text files, 7 layout-text files, and 7 direct-source rendered PNG pages in `preprocessing/support_doc003_pp161-167/`.
- **Result-relevant relationships/definitions mapped:** 6 (R1–R6): 4 planned-analysis relationships, 1 SAP-version interim-analysis relationship, and 1 versioned sample-size-assumption relationship.
- **Tables/figures with observed trial results:** 0. The single table is an SAP revision table; it reports prospective/historical assumptions and decisions, not trial outcomes.
- **Limitations:** Page 161 starts mid-sentence; the unshown outcome name is not reconstructed. The safety and medication paragraphs specify comparison tests but do not give observed counts, denominators, effect estimates, P values, or detailed test-selection rules. Cross-document matching requires a later review against aligned main-paper outcomes, population, time point, contrast, and SAP version.
