# Support Quantitative Evidence Map — DOC-004-RESULTS-SUPP

## Scope and evidence status

- **Direct source:** `joi250033supp4_prod_1750956987.77981.pdf`, PDF pages 1-15.
- **Stable evidence locations:** `joi250033supp4_prod_1750956987.77981.pdf#page=N` below use printed PDF page numbers, not internal supplement labels.
- **Authority and method:** all printed values were transcribed from the direct PDF; the existing native text and rendered page image were used only to locate material. The forest plot on page 9 was visually confirmed against the direct rendered PDF page because its table values are not present in the layout-text stream.
- **Coverage:** 15 of 15 assigned pages mapped. No workbook, CSV, DOC/DOCX, formula, or cached-workbook-value source belongs to this scope.
- **Boundary:** provisional relationship identifiers only. This map does not diagnose or register candidates.

## Page-by-page map

### Page 1 — contents / no result value

The contents enumerate eMethods, eReferences, eFigures 1-2, and eTables 1-4. It identifies the associated article and DOI. It contains no standalone result-relevant quantitative relationship beyond the table/figure titles subsequently mapped on pages 8-15.

### Page 2 — trial-design definitions

**RS-N001 — protocol/version chronology.** The trial registration is `NCT04372147`. Ethics approval for protocol version 1 was dated January 10, 2020 (reference `3754-I`); subsequent versions through version 5.0 dated June 7, 2022 were approved by the same committee. This is an administrative/protocol chronology, not an efficacy result.

**RS-N002 — endpoint adjudication and interim-analysis governance.** Possible recurrence cases were adjudicated by an independent blinded committee for the primary endpoint; an independent Data Safety Monitoring Board monitored safety and interpreted the planned interim analysis. No interim numerical result is printed.

### Page 3 — eligibility and intervention timing definitions

**RS-N003 — surgery-size classification used in eligibility.** Skull opening diameter up to 5 mm is classified as twist-drill craniostomy; up to 30 mm as burr-hole craniostomy; larger openings as craniotomy. Patients whose CSDH evacuation used craniotomy or twist-drill rather than burr-hole were ineligible.

**RS-N004 — intervention timing and protocol amendment.** Intervention-group patients underwent CTA followed by middle meningeal artery (MMA) embolization within 7 days of surgery. The third protocol amendment took effect April 30, 2021 and made CTA nonmandatory when a sufficiently good supra-aortic CTA from the prior year was available.

### Page 4 — embolization procedural quantities and population-side rule

**RS-N005 — device/caliber and particle-size definition.** The external carotid artery was catheterized with a 5F or 6F guiding catheter. MMA embolization used free-flow injection of 300-500 µm EmboSphere triascryl gelatin microspheric particles. The stated safety rationale says meningeal anastomotic arteries have been reported as 50 to 300 µm in diameter.

**RS-N006 — procedural target and laterality rules.** Embolization aimed to occlude both anterior and posterior MMA branches. Unilateral CSDH received homolateral embolization; bilateral CSDH generally received bilateral embolization; bilateral CSDH with unilateral surgery received embolization on the operated side. The special bilateral-recurrence scenario continues on page 5.

### Page 5 — primary-analysis definitions

**RS-N007 — special bilateral-recurrence treatment rule.** For a participant with bilateral prior surgery, a later unilateral recurrence and unilateral recurrence surgery, and study inclusion, embolization was performed bilaterally.

**RS-S001 — descriptive-statistics convention.** Baseline quantitative variables are described as median (interquartile range); qualitative variables as number (percentage), each by randomized group.

**RS-S002 — primary endpoint missing-data rule.** For the primary endpoint, patients not evaluable for the endpoint received multiple imputation, except those who died from a neurological or unknown cause, who were considered to have CSDH recurrence. The listed imputation variables are recurrence at 6 months; age; sex; unilateral/bilateral CSDH; anticoagulant/antiplatelet use; initial episode/recurrence; recent head trauma; Glasgow Coma Scale, American Society of Anesthesiologists, focal neurological deficit, hemiparesis, phasic disorder, gait disorder, headache, maximum CSDH thickness, Park classification, surgery type (burr hole/trephine craniostomy), and perioperative complications (infection, subdural empyema, epileptic seizure).

### Page 6 — imputation implementation

**RS-S003 — imputation method, number of data sets, and pooling.** The analysis used R and Multiple Imputation by Chained Equations (MICE). Ten data sets were generated, then pooled with Rubin’s rules to obtain overall estimates and standard errors. This is the definition applicable to the primary-analysis label in eFigure 2 and the EMPROTECT eTable 4 row.

### Page 7 — references / no applicable result relationship

The page contains eReferences 1-9. Citation dates, journal volumes, pages, and DOIs are bibliographic metadata, not study-result quantitative relationships; no applicable support result was mapped.

### Page 8 — eFigure 1, screening and randomization flow

**RS-N008 — screened, excluded, and randomized totals.** Adults who had surgery for CSDH and were at risk of recurrence: `n=659`; excluded: `n=317`; randomized: `n=342`.

**RS-N009 — exclusion categories.** Excluded patients: refusal `n=101`; other prespecified non-inclusion criteria `n=164`; other reasons `n=18`; unknown reasons `n=34`.

**RS-N010 — prespecified non-inclusion subcategories.** Within the printed `n=164`: follow-up not feasible `n=38`; life expectancy `<6 months`, `n=35`; renal failure `n=29`; legal guardianship/trusteeship `n=19`; functionally dependent with modified Rankin Scale score `≥4` before CSDH `n=19`; craniotomy or twist-drill craniostomy `n=11`; beyond 7 days after index surgery `n=8`; iodinated-contrast allergy `n=5`.

**RS-N011 — other-reason subcategories.** Within the printed `n=18`: dementia/patient confusion `n=8`; embolization outside trial `n=3`; patient transfer `n=2`; intracranial hypotension `n=1`; another trial `n=1`; failure to contact relatives `n=1`; antiphospholipid syndrome `n=1`; medical team unavailable `n=1`.

### Page 9 — eFigure 2, primary endpoint and sensitivity analyses

**RS-S004 — model, endpoint, covariates, and direction scale.** The forest plot reports 6-month CSDH recurrence adjudicated by the committee. The primary analysis is a logistic-regression model adjusted for randomization stratification factors: anticoagulant/antiplatelet use (yes vs no) and CSDH localization (bilateral vs unilateral). Effect measure is OR with 95% CI; on the printed forest scale, values below 1 favor embolization and values above 1 favor standard care.

**RS-S005 — primary analysis.** Population: full analysis set, multiple imputation. Embolization `24/162`; standard care `33/157`; OR `0.64` (95% CI, `0.36 to 1.14`); `P=.13`.

**RS-S006 — sensitivity analysis: adjudicated complete cases.** Embolization `24/162`; standard care `33/157`; OR `0.64` (95% CI, `0.35 to 1.14`); `P=.13`.

**RS-S007 — sensitivity analysis: on-site assessment.** Population: full analysis set, multiple imputation. Embolization `27/162`; standard care `38/156`; OR `0.61` (95% CI, `0.35 to 1.06`); `P=.08`.

**RS-S008 — sensitivity analysis: adjudicated cases without multiple imputation.** Embolization `24/171`; standard care `33/171`; OR `0.66` (95% CI, `0.37 to 1.19`); `P=.17`. Footnote: loss to follow-up and deaths from non-neurological cause were considered no event.

**RS-S009 — sensitivity analysis: adjudicated cases excluding nonembolized MMA patients.** Population: exclusion of nonembolized MMA patients, multiple imputation. Embolization `22/138`; standard care `33/157`; OR `0.71` (95% CI, `0.39 to 1.30`); `P=.27`. The caption states that the last sensitivity analysis excluded experimental-group patients who did not receive embolization.

### Page 10 — eTable 1, randomized participants by center

**RS-N012 — randomized-group totals.** The eTable header gives embolization `N=171`, standard care alone `N=171`, and overall `N=342`.

**RS-N013 — center distribution, rows 001 through 012.** Site 001, Paris-APHP Pitié Salpêtrière: `88/171 (51.5%)`, `89/171 (52.0%)`, `177/342 (51.8%)` (embolization, standard care, overall). Site 008, Limoges-CHU Dupuytren: `21/171 (12.3%)`, `19/171 (11.1%)`, `40/342 (11.7%)`. Site 011, Lille-CHRU de Lille–Roger Salengro: `19/171 (11.1%)`, `19/171 (11.1%)`, `38/342 (11.1%)`. Site 012, Tours-CHRU de Tours–Bretonneau: `10/171 (5.8%)`, `10/171 (5.8%)`, `20/342 (5.8%)`.

**RS-N014 — center distribution, rows 002 through 009.** Site 002, Paris-CH Sainte Anne: `7/171 (4.1%)`, `10/171 (5.8%)`, `17/342 (5.0%)`. Site 004, Clichy-APHP Beaujon: `7/171 (4.1%)`, `7/171 (4.1%)`, `14/342 (4.1%)`. Site 010, Marseille-APHM Nord: `6/171 (3.5%)`, `5/171 (2.9%)`, `11/342 (3.2%)`. Site 009, Marseille-APHM Timone Adultes: `4/171 (2.3%)`, `5/171 (2.9%)`, `9/342 (2.6%)`.

**RS-N015 — center distribution, rows 003 through 006.** Site 003, Paris-APHP Lariboisière: `3/171 (1.8%)`, `2/171 (1.2%)`, `5/342 (1.5%)`. Site 005, Créteil-APHP Henri Mondor: `2/171 (1.2%)`, `2/171 (1.2%)`, `4/342 (1.2%)`. Site 007, Clamart-HIA Percy: `2/171 (1.2%)`, `2/171 (1.2%)`, `4/342 (1.2%)`. Site 006, Paris-Fondation Ophtalmologique A. de Rothschild: `2/171 (1.2%)`, `1/171 (0.6%)`, `3/342 (0.9%)`.

### Page 11 — eTable 2, recurrence criteria among events at 6 months

**RS-N016 — table population and overlap rule.** The columns are embolization `N=24`, standard care alone `N=33`, overall `N=57`. The footnote states one patient could experience one or more criteria; row values are consequently criterion-specific event counts/rates, not mutually exclusive components.

**RS-N017 — criterion 1 and components.** Reappearance of homolateral CSDH with midline shift `≥5 mm` or symptomatic homolateral recurrence including death: embolization `16/24 (66.7%)`, standard care `28/33 (84.8%)`, overall `44/57 (77.2%)`. Subcomponent a, midline shift `≥5 mm`: `11/24 (45.8%)`, `17/33 (51.5%)`, `28/57 (49.1%)`. Subcomponent b, symptomatic recurrence including death: `15/24 (62.5%)`, `26/33 (78.8%)`, `41/57 (71.9%)`.

**RS-N018 — criterion 2.** Homolateral CSDH `>10 mm` maximal thickness on 6-month control head CT: `8/24 (33.3%)`, `4/33 (12.1%)`, `12/57 (21.1%)`.

**RS-N019 — criterion 3.** Repeat surgery for homolateral CSDH recurrence during the study period: `7/24 (29.2%)`, `13/33 (39.4%)`, `20/57 (35.1%)`.

**RS-N020 — criterion 4.** New hospital admission related to homolateral CSDH recurrence during the study period: `12/24 (50.0%)`, `15/33 (45.5%)`, `27/57 (47.4%)`.

**RS-N021 — recurrence classification for deaths and symptom definition.** Death from neurological or undetermined cause considered CSDH recurrence: `2/24 (8.3%)`, `1/33 (3.0%)`, `3/57 (5.3%)`. The symptomatic-recurrence footnote defines symptoms as focal neurological deficit, hemiparesis, speech disorder, gait disorder, headache, or intermittent dizziness.

### Pages 12-13 — eTable 3, prespecified procedure-related complications

**RS-N022 — major-complication total.** In embolization `N=171`, total major complications are `1 (0.6%)`.

**RS-N023 — major-complication components.** Mechanical thrombectomy after intracranial MCA occlusion during carotid catheterization: `1 (0.6%)`. The following each print `0 (0.0%)`: superficial hematoma with deglobulization (loss of 2 Hb points on CBC) and/or requiring transfusion; retroperitoneal hematoma with or without deglobulization; pseudoarterial aneurysm at puncture site requiring surgery; femoral-artery occlusion and/or acute limb ischemia; abscess at puncture site; anaphylactic shock; Quincke edema; bronchospasm with desaturation; extensive rash; persistent renal-function deterioration with creatinine-clearance decrease `>10 points`; and neurological accident with permanent sequelae.

**RS-N024 — minor-complication total and page-12 component.** In embolization `N=171`, total minor complications are `3 (1.8%)`. Superficial hematoma at the puncture site is `0 (0.0%)`.

**RS-N025 — page-13 minor-complication components.** Transient renal-function deterioration: `0 (0.0%)`; transient neurological accident: `2 (1.2%)`; asymptomatic arterial dissection: `0 (0)` as printed; mild headaches: `1 (0.6%)`. Abbreviations: MCA, middle cerebral artery; Hb, hemoglobin; CBC, complete blood count.

### Pages 14-15 — eTable 4, summarized MMA randomized trials

**RS-S010 — EMBOLISE primary outcome.** Trial `EMBOLISE (NCT04402632)`: 400 patients in 39 US centers; symptomatic subacute/CSDH with indication for surgical evacuation. Intervention was ipsilateral or bilateral MMA embolization with nonadhesive liquid embolic agent (Onyx); control was standard surgical and postsurgical care. Primary endpoint: hematoma recurrence/progression leading to repeat surgery within 90 days after index treatment. Primary outcome: `8 patients (4.1%)` in intervention versus `23 patients (11.3%)` control; RR `0.36`, 95% CI `0.11 to 0.80`; `P=.008`.

**RS-S011 — STEM primary outcome.** Trial `STEM (NCT04410146)`: 310 patients in 32 US/European sites; symptomatic CSDH, with surgical/nonsurgical standard treatment selected before randomization. Intervention was ipsilateral MMA embolization with Squid; control standard surgical/postsurgical care or medical management by subgroup. Composite endpoint at 180 days: recurrent/residual CSDH `>10 mm`, reoperation/surgical rescue, or major disabling stroke, myocardial infarction, or neurologic-cause death. Outcome: `19 of 120 (16%)` intervention versus `47 of 129 (36%)` control; OR `0.36`, 95% CI `0.20 to 0.66`; `P=.001`.

**RS-S012 — MAGIC-MT primary outcome.** Trial `MAGIC-MT (NCT04700345)`: 727 (722 in intent-to-treat analysis) patients in 31 China centers. Endpoint: recurrence (maximum hematoma thickness `>10 mm` or reoperation after prior burr-hole drainage within 90 days) or progression (maximum thickness increase `>3 mm` from baseline or surgical rescue in usual-care patients within 90 days). Outcome: `24 patients (6.7%)` intervention; the printed control comparator is `(9.9%)` with no control count shown; between-group difference `−3.3 percentage points`, 95% CI `−7.4 to 0.8`; `P=.10`.

**RS-S013 — EMPROTECT endpoint definition.** Trial `EMPROTECT (NCT04372147)`: 342 patients in 12 French centers, undergoing surgery for recurrent CSDH or first-episode CSDH at high recurrence risk. Intervention was ipsilateral MMA embolization with 300-500 µm calibrated TAG microspheres (Embosphere); control standard surgical/postsurgical care. The primary endpoint is CSDH recurrence rate at 6 months: reappearance of homolateral CSDH with midline shift `≥5 mm` or symptomatic homolateral CSDH including death; presence of homolateral CSDH `>10 mm` maximal thickness on 6-month control CT; repeat surgery for homolateral recurrence; or a new hospital admission related to homolateral recurrence.

**RS-S014 — EMPROTECT primary outcome.** `24/162 (14.8%)` intervention patients versus `33/157 (21.0%)` control patients reached the primary outcome. The table labels the analysis ITT with imputation and reports OR `0.64`, 95% CI `0.36 to 1.14`; `p=0.13`. This is the same population, effect measure, interval, and P value printed for the eFigure 2 primary analysis (RS-S005).

## Cross-location keys retained for later matching

- The randomized group totals `171`, `171`, and `342` (RS-N012) define the overall randomized population used in the no-imputation sensitivity analysis (RS-S008); they differ from endpoint-evaluable/imputed analysis denominators as printed in RS-S005 through RS-S009.
- The EMPROTECT primary endpoint definition in RS-S013 corresponds to the criteria tabulated among 57 recurrence events in RS-N016 through RS-N021 and to the adjudicated 6-month endpoint in RS-S004 through RS-S009.
- The primary-analysis result RS-S005 is repeated in the EMPROTECT cross-trial summary as RS-S014 with precision/formatting differences only (`P=.13` vs `p=0.13`; `0.36 to 1.14` in both).
- eTable 2’s denominators (`24`, `33`, `57`) are recurrence-event populations and its overlap footnote applies; they are not labeled as randomized-group denominators.

## Mapping completion and limitations

All assigned source pages 1-15 were inspected and mapped, including method/definition pages and pages 1 and 7 with no applicable result relationship. Direct PDF text did not expose the forest-plot cells on page 9; visual inspection of the direct PDF rendering supplied those values. This map deliberately makes no candidate determination, arithmetic conclusion, or comparison to unassigned sources.
