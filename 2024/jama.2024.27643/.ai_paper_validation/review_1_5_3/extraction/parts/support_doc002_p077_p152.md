# Support quantitative evidence map — support-002

## Scope and direct-source method

- **Source ID:** DOC-002, `joi240158supp1_prod_1742927563.7611.pdf` (229-page supplied PDF; source authority).
- **Exact assigned units:** PDF pp. 77–152 inclusive (76 physical PDF pages), all fresh-required.
- **Fresh extraction:** `pdftotext` native and `pdftotext -layout` were run directly for pp. 77–152. Outputs are `preprocessing/support-002/doc002_p077_p152_native.txt` and `preprocessing/support-002/doc002_p077_p152_layout.txt`.
- **Targeted direct renders:** PDF pp. 101, 103, and 105–111 were rendered for table/figure structure. CPU Tesseract was used only where the native text was absent or materially incomplete: pp. 106–111 and pp. 139–148. The PDF, not OCR, remains the authority.
- **Document identity within these pages:** pp. 77–83 are the tail of the Master Protocol v5.0; pp. 84–152 are Regimen-Specific Appendix C (CNM-Au8), v3.0 dated 2020-06-03. Its printed internal page numbering runs 1–71 across PDF pp. 84–154.
- **Relationship IDs:** local IDs below are durable mapper locators only. They are not candidate IDs or adjudications.

## Page-complete applicability map

| PDF page(s) | Direct-source content and applicability |
|---|---|
| 77–81 | C-SSRS lifetime/since-last-visit assessment form: result-relevant measurement definitions and ordinal labels mapped below. |
| 82–83 | Reference-list continuation only; **no applicable result-relevant quantitative content**. |
| 84 | Regimen appendix title page; **no applicable result-relevant quantitative content**. |
| 85–87 | Table of contents only; it contains navigational internal-page numbers, but no result definition or reported result. **No applicable result-relevant quantitative content.** |
| 88 | Signature/attestation page; **no applicable result-relevant quantitative content**. |
| 89–90 | Abbreviation list; labels (including ALSAQ-40, ALSFRS-R, AUC, CNS-BFS, PD, PK, SVC) provide terminology but no numerical result. |
| 91–97 | Regimen summary and schedules of activities: planned sample allocation, timing, intervention, measurement schedule, and footnotes mapped below. |
| 98–100 | Background/rationale narrative. Quantitative context and product concentration/dosing are mapped below. |
| 101–111 | Product-characteristic table and preclinical figures/results, including printed statistics, units, samples, tests, and figure labels, mapped below. |
| 112–137 | Objectives/endpoints, design, intervention tables, safety margins, visit timing, outcomes, PK/PD definitions, and regimen statistical considerations mapped below. |
| 138 | ALSAQ-40 appendix title only; scale content begins at p. 139. |
| 139–146 | ALSAQ-40 form. Native text layer is blank except page furniture; direct render plus CPU OCR confirms its 40-item, two-week recall response form. Result-relevant scale definitions mapped below; individual questionnaire prose is not reported trial-result data. |
| 147–148 | CNS-BFS form. Three-domain 21-item scoring form and labels mapped below. |
| 149–152 | Reference-list continuation only; **no applicable result-relevant quantitative content**. |

## Protocol and regimen definitions, populations, intervention, and timing

### N-D002-001 — Regimen design, population, allocation, and follow-up

- **Locations:** [DOC-002 — PDF p. 91](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=91>), [PDF p. 92](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=92>), [PDF p. 114](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=114>), and [PDF p. 115](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=115>).
- **Definition/contrast:** multi-center randomized, placebo-controlled, double-blind regimen of oral CNM-Au8 30 mg or 60 mg versus colour-matched placebo. Active:placebo allocation is 3:1; active participants are allocated equally between 30 mg and 60 mg.
- **Planned numbers:** 160 randomized: 120 active and 40 placebo; active is 60 at 30 mg/day and 60 at 60 mg/day. Approximately 60 US centres. Enrollment stops when pre-defined futility criteria are met or the target randomized number is reached.
- **Timing:** maximum placebo-controlled treatment 24 weeks. Participants either have a 28-day follow-up phone call or may enter an OLE planned for at least 52 weeks. The summary gives up to 34 weeks for non-OLE participation (6-week screening + 24-week treatment + 4-week safety follow-up) and approximately 86 weeks with the 52-week OLE; about 10 visits in each stated phase. Section 4.3 describes approximately 24 weeks double-blind plus an additional 52 weeks open label.
- **Population rule:** participant must meet Master Protocol eligibility and the regimen exclusion is history of allergy to gold/gold salts/colloidal gold.

### N-D002-002 — Placebo-controlled and OLE assessment schedule

- **Locations:** [PDF pp. 93–97](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=93>), [PDF pp. 125–133](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=125>).
- **Placebo-controlled visits:** baseline Day 0; Week 2 Day 14 ±3; Week 4 Day 28 ±7; Week 8 Day 56 ±7; Week 12 Day 84 ±3; Week 16 Day 112 ±7; Week 20 Day 140 ±3; Week 24/early termination Day 168 ±7; safety call 28 days after last dose ±3 days. Screening windows are Master Protocol −42 to −1 days and regimen-specific −41 to 0 days. The maximum interval between placebo-controlled visits is 64 days.
- **OLE visits:** Weeks 2, 4, 8, 12, 16, 20, 24, 28, 40, and 52 after the placebo-controlled Week 24 visit; stated day targets/windows include 14 ±3, 28 ±10, 56 ±7, 84 ±3, 112 ±7, 140 ±3, 168 ±3, 196 ±14, 280 ±14, and 364 ±14. OLE maximum visit windows are 64 days for Weeks 8/16 and 96 days for Weeks 28/40/52.
- **Repeated measures:** ALSFRS-R is scheduled throughout both periods; SVC, CNS-BFS, ALSAQ-40, voice, PK/PD samples, C-SSRS, laboratory tests, adverse-event review, drug accountability and vital status have the schedule marks and footnotes on pp. 93–97. The exact calendar rules and special remote-visit omissions are stated in N-D002-012.

### N-D002-003 — Intervention composition, dose, route, and compliance definition

- **Locations:** [PDF pp. 98, 116–119](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=116>), [PDF p. 122](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=122>).
- **Product/dose:** a 60-mL bottle contains CNM-Au8 at 250 μg/mL (15 mg) or 500 μg/mL (30 mg); two bottles each morning give 120 mL/day and 30 mg/day or 60 mg/day. The matched placebo also has two 60-mL bottles/day and 120 mL/day. Administration is oral once daily at about the same time (±1 hour), at least 30 minutes before food; it may be by mouth or gastric tube.
- **Table 2 / Table 3 labels:** each active/placebo dose is two bottles daily, 60 mL/bottle. Per bottle NaHCO3 is 32.8 mg in all three products; Au is 15 mg (30-mg regimen), 30 mg (60-mg regimen), and not applicable for placebo; USP purified water is 60 mL each. Storage: 15–25°C (59–77°F), mean kinetic temperature not over 25°C; 15–30°C (59–86°F) excursions allowed.
- **Dose modification:** no anticipated adjustment during placebo-controlled treatment. With Medical Monitor approval, tolerance-related down-titration is one bottle daily, followed by possible re-challenge to two bottles; no drug holidays. In OLE, blinded dose is maintained and prior placebo recipients are re-randomized to 30 or 60 mg.
- **Compliance analysis-set definition:** bottle counts/logs; per-protocol intake should be 80%–120% of planned dose. A missed same-day dose must not be doubled.

## Endpoints and measurement definitions

### S-D002-001 — Primary analysis endpoint and model

- **Location:** [PDF p. 112](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=112>).
- **Primary efficacy objective/endpoint:** efficacy of CNM-Au8 versus placebo on ALS disease progression, measured as change in ALSFRS-R using a **Bayesian repeated-measures model that accounts for loss to follow-up due to mortality**.
- **Analysis label:** the page provides no effect estimate, interval, posterior criterion, or numerical result; this is a statistical definition requiring matching to the Master Protocol/SAP when cross-source mapping.

### N-D002-004 — Secondary, safety, and exploratory endpoint labels

- **Location:** [PDF pp. 112–113](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=112>).
- **Secondary efficacy:** change in SVC; change in muscle strength measured by hand-held dynamometry and grip strength; survival.
- **Safety:** treatment-emergent adverse/serious adverse events; laboratory and ECG changes/clinically significant abnormalities; treatment-emergent suicidal ideation and behaviour.
- **Exploratory:** quantitative voice changes; active versus placebo difference in the proportion with **≥6-point ALSFRS-R decline from baseline to Week 24**; biofluid-neurodegeneration biomarkers; patient-reported-outcome changes.

### N-D002-005 — ALSAQ-40 and CNS-BFS measurement scales

- **Locations:** [PDF pp. 135, 138–148](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=135>).
- **ALSAQ-40:** patient self-report health-status outcome of subjective well-being in ALS/motor-neuron disease; 40 questions. The direct form uses a two-week recall period. Items 1–30 use a five-category frequency/ability response frame including Never, Rarely, Sometimes, Often, and Always/cannot perform or walk at all when applicable; items 31–40 use Never, Rarely, Sometimes, Often, Always. The eight form pages (PDF pp. 139–146) are image-only in the native layer and were directly rendered/OCR-confirmed. No trial score/value is printed.
- **CNS-BFS:** patient self-report endpoint/clinical measure with 21 questions in three domains: salivation (7), speech (7), swallowing (7). Salivation/swallowing use Does Not Apply=1, Rarely=2, Occasionally=3, Frequently=4, Most of the Time=5. Speech adds Unable to Communicate by Speaking=6. The form supplies domain-total fields and an overall-score field but no computation rule or observed score. On PDF pp. 147–148 it shows the domain item counts and response labels.

### N-D002-006 — C-SSRS safety assessment definitions and coding

- **Locations:** [PDF pp. 77–81](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=77>).
- **Ideation screen:** five ordered ideation types: wish to be dead; non-specific active thoughts; active ideation with any method but no intent; active ideation with some intent but no specific plan; active ideation with specific plan and intent. If questions 1 and 2 are both negative, proceed to suicidal behaviour; if question 2 is positive, ask 3–5; any positive 1/2 triggers intensity section. The most severe ideation type is numbered 1–5.
- **Intensity labels:** frequency 1=less than once/week, 2=once/week, 3=2–5 times/week, 4=daily/almost daily, 5=many times/day. Duration 1=few seconds/minutes, 2=<1 hour/some time, 3=1–4 hours/a lot of time, 4=4–8 hours/most of day, 5=>8 hours/persistent/continuous. Controllability 1=easily controlled through 5=unable to control, with 0=does not attempt; deterrents and reasons-for-ideation also have ordered 1–5 plus 0=does not apply.
- **Behaviour/count fields:** actual, interrupted, and aborted attempts have yes/no and blank total-number fields; preparatory acts and suicidal behaviour are yes/no. Actual lethality/medical damage is coded 0–5 (no/very minor damage through death). Potential lethality is completed only where actual lethality=0 and is coded 0–2 (not likely injury; injury but not death; likely death despite care). The forms are measurement definitions only; no participant values appear.

### N-D002-007 — Voice, PK, PD, and biomarker definitions

- **Locations:** [PDF pp. 134–137](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=134>).
- **Voice:** in addition to clinic recordings, two recordings weekly via Android/iOS app. Tasks: five fixed plus five randomly selected sentences, consonant-vowel sequence, sustained phonation, and one-breath counting. App/AI identifies vocal attributes; trained personnel QC individual recordings.
- **PK:** whole-blood Au and plasma riluzole concentrations are pre-dose. The first 40 riluzole-taking Regimen-C participants to reach Week 8 are to be assessed by DSMB/unblinded designee for population-PK changes for CNM-Au8 versus placebo at Weeks 4 and 8; no result is printed.
- **PD:** pre-dose plasma, whole blood, urine. Potential metabolomic markers: NAD+, NADH, NADP+, NADPH, ATP, ADP, AMP, GSSG, GSH; disease-progression markers may include urinary p75ECD and serum neurofilament light chain.

### S-D002-002 — Regimen statistical considerations

- **Location:** [PDF p. 137](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=137>).
- **Definition:** default Master Protocol statistical design applies with one stated deviation: **no interim analyses for early success**. Clinical-trial simulation is used for operating characteristics (details in regimen SAP). The primary analysis shares all controls from other regimens, justified by minor eligibility differences and no expected systematic primary-endpoint difference across control groups.

## Tables, formulas, quantitative preclinical evidence, and statistical labels

### N-D002-008 — Table 1: CNM-Au8 particle characteristics

- **Location:** [PDF p. 101](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=101>), visually confirmed from a direct render.
- **Columns/assumptions:** CNM-Au8 500 μg/mL, 60-mL dose; disc-like minimum (aspect 0.2) versus spherical maximum (aspect 1.0).
- **Rows:** median diameter 13 nm; volume 2.3×10^2 versus 1.2×10^3 nm³; surface area 3.2×10^2 versus 5.3×10^2 nm²; Au atoms/nanocrystal 1.4×10^4 versus 6.8×10^4; molecular weight 2.7×10^3 versus 1.3×10^4 kDa; total surface area/mL 3.6×10^2 versus 1.2×10^2 cm²; nanocrystals/mL 1.1×10^14 versus 2.3×10^13; nanocrystals/60-mL dose 3.4×10^15 versus 6.8×10^14.

### S-D002-003 — Figure 1 and Figure 2 preclinical NADH/NAD statistics

- **Location:** [PDF p. 103](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=103>), direct render.
- **Figure 1A:** NADH absorbance at 339 nm (cm⁻¹) over time in minutes, for 26 μM NADH in 5.7 mM NaHCO3 with 3.4 μg/mL Au; comparator labels are CNM-Au8, NIST 10-nm, NIST 30-nm, and NADH control/no GNPs.
- **Figure 1B:** relative NADH oxidation rate (a.u.) versus GNPs at [Au] about 3.4 μg/mL. Caption/footnote: *P<0.05 versus control, one-way ANOVA followed by Dunnett's test.
- **Figure 2:** effects of CNM-Au8 on NAD+ and NADH levels in primary rodent mesencephalic cultures; bar panels use quantity of NAD+ (μM) and ratio of NAD+/NADH, respectively. Dose labels include control, CNM-Au8 10/100/500/1,000 ng/mL, and BDNF 50 ng/mL; the same P<0.05 versus control one-way ANOVA/Dunnett label applies. Values are plotted graphically without a supplied numeric table.

### S-D002-004 — Figures 4–9 preclinical effects and printed tests

- **Locations:** [PDF pp. 105–111](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=105>), direct renders and targeted OCR.
- **Figure 4:** SOD/ROS generation. Panel A is Abs 450 nm, cm⁻¹ (t=20 minutes), a.u. (SEM) for CNM-Au8 1000/750/500/250 and vehicle. Panel B is mean intensity (a.u.) over time (seconds) for control, buffer, and 0.3/1/3 μg/mL; marked comparisons ** and **** are drawn. Panel C is mean intensity (a.u.) over time (seconds) with rotenone for buffer, 0.3, 1, and 3 μg/mL; an asterisk is drawn. Graphic values are not tabulated.
- **Figure 5:** CNM-Au8 effects on OPC differentiation (O4+ cells) and glycolytic ATP in MO3.13 oligodendrocytes at 72 hours, plotted as mean ± SEM. Stated analysis: one-way ANOVA, P<0.05.
- **Figure 6:** rat motor-neuron glutamate-excitotoxicity experiments. Cultures were pre-treated on day 11; riluzole was pre-treatment for 1 hour; day-13 glutamate was 20 minutes then treatment for 48 hours. Outcomes/labels include MAP-2 motor-neuron survival, neurite-network area, and cytoplasmic TDP-43. Figure panels state *P<0.05 versus glutamate, one-way ANOVA followed by PLSD Fisher's test; illustrated glutamate concentration is 20 μM.
- **Figure 7:** iPSC-derived normal human motor neurons exposed to SOD1A4V ALS-participant astrocytes for 14 days. Panels quantify Tuj1, Isl1/2, and ChAT by CNM-Au8 dose (ng/mL); exact bar heights are graphical, not tabulated.
- **Murine study narrative:** rapidly progressive model: N=15/group, clinical-onset P=0.13 (Mantel-Cox), lack of brainstem atrophy P<0.05 (unpaired t test); other functional measures not significant. Slower model: N=20 female mice, 10/group, balanced for weight; stated life spans approximately 157 versus 129 days for the two strain contexts.
- **Figure 8:** slower SOD1G93A model, locomotor efficacy: A neurological score P=0.0074 (two-way ANOVA); B weights-hold P<0.01 (two-way ANOVA); C horizontal-bar P<0.05 (two-way ANOVA); D/E home-wheel velocity including periods Days 71–100, 101–130, 131–160 and P<0.0001 (two-tailed t test). Axes are age (weeks/days), score, test units, or wheel-running velocity as plotted.
- **Figure 9:** survival proportions Kaplan–Meier plot, Breslow–Wilcoxon P=0.0302 and hazard ratio 0.3730, CNM-Au8 versus vehicle; x-axis days alive (120–180) and y-axis survival proportions (%) (0–100).

### N-D002-009 — Animal/human safety-margin tables and exposure relationship

- **Locations:** [PDF pp. 119–122](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=119>).
- **Table 4, 21-day HED body-surface-area dose ratios for 60-kg human:** rat NOAEL 40 mg/kg/day=240 mg/m²; safety margins at human 15/30/60/90 mg (9.3/18.5/37.0/55.5 mg/m²) are 25.9/13.0/6.5/4.3. Canine NOAEL 90 mg/kg/day=1800 mg/m²; corresponding margins 194.6/97.3/48.6/32.4.
- **Table 5, 21-day AUC(0–24) animal:human ratio:** human AUCs at 15/30/60/90 mg are 32.3/41.4/50.3/66.0 ng·hr/mL. Rat NOAEL 40 mg/kg/day, animal AUC 106 ng·hr/mL, margins 3.3/2.6/2.1/1.6. Canine NOAEL 90 mg/kg/day, animal AUC 596, margins 18.5/14.4/11.8/9.0. Footnote: animal AUC is male/female average at end of study.
- **Table 6, chronic AUC ratio:** rat 6-month NOAEL 40 mg/kg/day, AUC 209, margins 6.5/5.0/4.2/3.2; canine 9-month NOAEL 10 mg/kg/day, AUC 440, margins 13.6/10.6/8.7/6.7, in the same human-dose order. The text states 30.6 hr·ng/mL mean AUC for rodent neuroprotection and 50.3 hr·ng/mL at human 60 mg, supporting 15–30 mg minimum human-equivalent exposure; selected ALS doses are 30 and 60 mg/day.

### N-D002-010 — Safety thresholds and follow-up rules

- **Locations:** [PDF pp. 123–124](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=123>).
- **Human prior exposure:** Phase-1 doses 15, 30, 60, 90 mg; stated well tolerated up to 90 mg/day over 21 consecutive days. No human ALS trials at the time of document.
- **Laboratory alert table:** ALT/AST >3× ULN; creatinine >1.5× baseline; platelet count <75,000/mm³. These prompt further investigation but do not mandate reduction/discontinuation.

### N-D002-011 — Schedule-specific assessment rules and administrative timing

- **Locations:** [PDF pp. 93–97](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=93>) and [PDF pp. 125–133](<../../../../joi240158supp1_prod_1742927563.7611.pdf#page=125>).
- **Footnoted definitions:** vital signs are weight, systolic/diastolic pressure, respiratory rate, heart rate, temperature; height is Master Screening only. Clinical safety labs: CBC/differential, chemistry, thyroid function, urinalysis; OLE table also labels liver tests. Pregnancy tests are as applicable. AEs after consent are recorded.
- **Collection rules:** whole blood/plasma pre-dose at baseline and Week 24; plasma pre-dose Week 4/8. Vital status is death/death-equivalent date or last-known-alive date, determined for each randomized participant at end of placebo-controlled follow-up and again at last-patient-last-visit if alive.
- **Visit-specific timing:** Week 2/12/20 placebo telephone visits at 14±3/84±3/140±3 days; Week 4/8 at 28±7/56±7; Week 16 112±7; Week 24 168±7; safety call 28±3 after last dose. Early termination during placebo/OLE calls for Week-24/OLE-Week-52 assessments respectively and the stated 28±3 safety-call rule.
- **Remote visits:** during pandemic remote schedules, blood/urine PK/PD samples are not collected by home health agency and must be recorded as such; this is an administrative collection rule, not an observed missing-data result.

## Non-applicable / limitations record

- **No reported human efficacy, safety, participant-flow, laboratory, PK, PD, or trial-result values occur in pp. 77–152.** This shard contains protocol/regimen definitions, planned quantities, forms, and preclinical rationale; its values must not be represented as observed results.
- **Image-only form content:** ALSAQ-40 pages 139–146 required direct render plus CPU OCR because native/layout text did not contain form questions. The form-level counts, two-week recall, and response labels were confirmed; no scores were printed.
- **Graph-only preclinical values:** Figures 1, 2, 4–9 provide plotted points/bars/curves but no source data table. Axis units, treatment labels, sample sizes where printed, and test/P-value/HR labels are mapped; unprinted precise graphical readings are not fabricated.
- **No workbook, CSV, DOC/DOCX, formula cells, or cached workbook values are in this assigned source unit.**

## Completion counts

- **Assigned/mapped physical source units:** 76/76 PDF pages (pp. 77–152).
- **Pages with result-relevant quantitative/measurement/statistical content:** 64 pages (77–81, 89–137, and 139–148).
- **Explicit no-applicable pages:** 12 pages (82–88, 138, and 149–152); pp. 85–87 are navigational contents only.
- **Mapped local quantitative/definition relationships:** 11 `N-D002` records.
- **Mapped local inferential/statistical relationships:** 4 `S-D002` records.
- **Coverage gap:** none for the assigned direct PDF pages. Figure data are only graphically displayed where noted; that is a source limitation, not a page-coverage gap.
