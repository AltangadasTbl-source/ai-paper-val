# DOC-006-RESULTS-SUPP — Result-Relevant Evidence Map

## Scope and provenance

- **Source:** `joi240006supp5_prod_1708623115.01733.pdf` (DOC-006-RESULTS-SUPP), PDF pp. 1-53.
- **Audit boundary:** Results supplement only. This map includes the eMethod that supports reported models, eFigures 1-20, and eTables 1-13; no protocol, SAP, administrative, author-list, or data-sharing document was opened.
- **Derived-artifact provenance:** native page text is in `.ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/native_text/page-###.txt`; rendered page evidence is in `.ai_paper_validation/preprocessing/DOC-006-RESULTS-SUPP/page_images/page-###.png`; page-level quality/status is in `preprocessing/DOC-006-RESULTS-SUPP/page_manifest.csv`.
- **Visual review:** rendered pages were reviewed for all sparse/OCR-unavailable result pages (PDF pp. 7-8 and 13-25), plus partial continuation pages 37, 48, and 50. No OCR-derived values are asserted.

## Supporting supplementary method

| Location | Extracted evidence |
|---|---|
| PDF p. 4, eMethods, “Analysis comparing explanatory capabilities…” | Models compared CT-perfusion rCBF <30% core, manually delineated non-contrast-CT hypodensity, and their composite core (larger estimate), with age, presentation NIHSS, last-known-well-to-randomization time, and one imaging parameter. Lower AIC/BIC and higher AUC were defined as better; BIC-difference convention: 0-2 weak, 2-6 positive, 6-10 strong, >10 very strong evidence of model superiority. |

## Figures and flow evidence

| Location | Result-relevant content / reported values |
|---|---|
| PDF p. 5, eFigure 1 | Illustrative perfusion case: rCBF <30% 94 mL; Tmax >6 s 131 mL; mismatch ratio 1.4; mismatch volume 37 mL. |
| PDF pp. 6-7, eFigure 2 | Illustrative baseline non-contrast CT / CTP and follow-up DWI case; p. 7 is image-only continuation, visually confirmed. |
| PDF p. 8, eFigure 3 (flow diagram) | **Visually confirmed.** Assessed 958; excluded 606 (listed reasons total 606); SELECT2 trial 352; missing 90-day outcomes 4 → available 348; imaging exclusions 12 (noncontrast CT 6, perfusion imaging 5, follow-up imaging 1) → study cohort 336. As-randomized: EVT 168, MM 168. As-treated: received EVT 170 (including 2 crossover from MM), received MM 166. |
| PDF p. 9, eFigure 4 | CT hypodensity > CTP/MRI core rises from 19% at 0-3 h to 86% at 21-24 h; converse values at those points 81% and 14%, respectively. Intermediate time strata are plotted. |
| PDF pp. 10-12, eFigures 5-6 | Mismatch distributions by time and baseline CTP/MRI-core strata. eFigure 5 reports trend p values: CTP/MRI ratio ≥1.2 & volume ≥10 mL, 0.71; CTP/MRI ratio ≥1.8 & volume ≥15 mL, <0.001; corresponding composite-core definitions, 0.27 and 0.18. eFigure 6 reports p for trend <0.001 for both CTP/MRI-core mismatch definitions across 0-49, 50-99, 100-149, and ≥150 mL strata. |
| PDF p. 13, eFigure 7 | **Visually confirmed forest plot.** Functional independence (mRS 0-2) at 90 d by ASPECTS, core-volume, and mismatch strata; columns report EVT/MM counts (%), RR (95% CI), and interaction p values. Interaction p values: 0.9055, 0.9543, 0.4097, 0.7338, 0.8079 (in displayed strata order). Example: core <70 mL RR 2.36 (1.20-4.61); ≥70 mL RR 4.19 (1.27-13.89). |
| PDF p. 14, eFigure 8 | **Visually confirmed forest plot.** Independent ambulation (mRS 0-3) at 90 d across the same strata. Interaction p values: 0.6788, 0.8927, 0.2093, 0.5740, 0.4588, 0.5921. Example: core <70 mL RR 1.79 (1.26-2.54); ≥70 mL RR 3.10 (1.49-6.43). |
| PDF p. 15, eFigure 9 | **Visually confirmed forest plot.** Complete dependence/death (mRS 5-6) at 90 d across the same strata. Interaction p values: 0.8204, 0.7244, 0.9344, 0.2291, 0.2056, 0.6255, 0.9485. Example: core <70 mL RR 0.75 (0.52-1.08); ≥70 mL RR 0.74 (0.61-0.91). |
| PDF p. 16, eFigure 10 | **Visually confirmed forest plot.** 90-day ordinal mRS (GenOR) by noncontrast-CT hypodensity (“NCCT”) and largest/composite core strata. The displayed interaction p values are 0.2684, 0.9413, **0.0164**, 0.0707, 0.8886, 0.7243, 0.6791, and 0.6165. The 100-mL NCCT strata show GenOR 2.25 (1.65-3.06) for <100 mL and 1.25 (0.89-1.74) for ≥100 mL. |
| PDF pp. 17-19, eFigures 11-13 | **Visually confirmed forest plots.** Same outcomes as eFigures 7-9, using CT hypodensity and largest/composite-core strata; full cells are page-visible. eFigure 11 functional independence: interaction p values 0.4696, 0.9978, 0.1717, 0.2581, 0.3360, 0.5126, 0.3817, 0.5351. eFigure 12 independent ambulation: 0.5583, 0.4539, 0.0762, 0.1516, 0.6936, 0.9146, 0.7419, 0.5951. eFigure 13 dependence/death: 0.4646, 0.7845, 0.0664, 0.2512, 0.3272, 0.9984, 0.7851, 0.7981. |
| PDF pp. 20-23, eFigures 14-17 | **Visually confirmed continuous-model plots.** A-C plot estimated probabilities of mRS 0-2, 0-3, and 5-6; D plots estimated odds of ≥1-point mRS improvement, each with 95% CI. Covariates: CT ASPECTS (Figure 14, adjusted for composite core), CT hypodensity volume (15), composite-core volume (16), and mismatch volume (17). |
| PDF p. 24, eFigure 18 | **Visually confirmed.** Modelled independent ambulation (mRS 0-3) in EVT patients by age and CTP-acquisition-to-reperfusion/end time, at composite core 70, 100, and 150 mL. Color scale is probability bands 0.0-0.1 through 0.8-0.9. |
| PDF p. 25, eFigure 19 | **Visually confirmed.** Corresponding model by age and last-known-well-to-reperfusion/end time, at composite core 70, 100, and 150 mL (same 0.0-0.9 probability-band scale). |
| PDF pp. 26-34, eFigure 20 | Distribution of mRS 0-6 by treatment across CT-hypodensity, CTP/MRI-core, composite-core, ASPECTS, and mismatch strata. Denominators are shown in each panel (e.g., p. 26: CT hypodensity <70 mL, EVT 68/MM 64; ≥70 mL, EVT 100/MM 104). Detailed panel values are available in native-text artifacts and rendered pages. |

## Tables and sensitivity-analysis evidence

| Location | Extracted evidence |
|---|---|
| PDF pp. 35-37, eTable 1 | As-treated baseline table: EVT N=170, MM N=166. Key medians: age 66.0 (59.0-75.0) vs 67.0 (58.0-75.0); CT ASPECTS 4 (3-5) vs 4 (4-5); composite core 103 (69-140) vs 100 (74-136) mL; CTP/MRI core 70 (39-110) vs 77 (48-104) mL; CT hypodensity 84 (45-114) vs 87 (49-113) mL. PDF p. 37 defines composite core as the larger of CTP/MRI-core and CT-hypodensity estimates. |
| PDF p. 38, eTable 2 | Intention-to-treat outcomes, EVT+MM N=168 vs MM N=168: mRS median (IQR) 4 (3-6) vs 5 (4-6); mRS 0-2 34/168 (20.2%) vs 12/168 (7.1%); mRS 0-3 65/168 (38.7%) vs 31/168 (18.5%); mRS 5-6 76/168 (45.2%) vs 102/168 (60.7%); mortality 62/168 (36.9%) vs 70/168 (41.7%). Also gives hemorrhage, neurological-change, early-improvement, follow-up infarct volume, and three infarct-growth measures. |
| PDF p. 39, eTable 3 | Sensitivity results using site-investigator-adjudicated ASPECTS 3-5, 6-10, and individual 3/4/5: ordinal mRS aGenORs, and aRRs (95% CIs) for mRS 0-2, 0-3, 5-6. Example ASPECTS 3-5: aGenOR 1.70 (1.33-2.17); mRS 0-2 aRR 2.97 (1.60-5.49); mRS 0-3 aRR 2.23 (1.56-3.16); mRS 5-6 aRR 0.74 (0.61-0.91). |
| PDF p. 40, eTable 4 | CTP-only sensitivity analysis. For CTP core <70 mL: aGenOR 1.73 (1.20-2.48), mRS 0-2 aRR 2.26 (1.15-4.43), mRS 0-3 aRR 1.76 (1.24-2.50), mRS 5-6 aRR 0.77 (0.53-1.11). ≥70 mL: 1.61 (1.21-2.15), 4.12 (1.25-13.63), 2.89 (1.39-6.02), 0.75 (0.61-0.92), respectively. Further 100/150-mL strata reported; ≥150 mL has N/A for mRS 0-2 and 0-3. |
| PDF p. 41, eTable 5 | Associations per 10-mL increase in CT-hypodensity or composite-core volume within EVT and MM, with interaction p values. Examples: ordinal mRS, composite aGenOR EVT 0.92 (0.88-0.95), MM 0.95 (0.92-0.98), interaction 0.13; mRS 0-3 composite aRR EVT 0.91 (0.85-0.98), MM 0.91 (0.85-0.98), interaction 0.82. |
| PDF p. 42, eTable 6 | Model-fit comparison. Composite core is identified as preferred for all three outcomes. BIC/AUC: ordinal mRS BIC 429.3182 (no AUC); mRS 0-2 BIC 255.6287, AUC 0.7783 (0.7103-0.8463); mRS 0-3 BIC 343.3374, AUC 0.7977 (0.7472-0.8482). The table also gives ASPECTS, CT-hypodensity, and CTP/MRI-core comparator values. |
| PDF pp. 43-44, eTable 7 | As-treated mismatch-profile analysis based on composite core, for ratio ≥1.2/volume ≥10 mL and ratio ≥1.8/volume ≥15 mL. Provides EVT and MM counts, aGenOR/aRR/aRD uncertainty estimates, with adjustment for age, NIHSS, last-known-well-to-randomization time, and CTP/MRI core. |
| PDF pp. 45-46, eTable 8 | Within-arm association of concordant/discordant ASPECTS and CTP/MRI-core profiles. Provides medians, mRS 0-2/0-3/5-6 counts and effect estimates for EVT N=163 and MM N=156, plus interactions. The mRS 5-6 interaction values include 0.14 for discordant profile 1 and 0.02 for discordant profile 2. |
| PDF pp. 47-48, eTable 9 | Treatment-effect estimates by concordant/discordant profiles using CTP/MRI core. Example mRS 5-6: concordant 60/83 MM vs 41/74 EVT, aRR 0.76 (0.61-0.95); discordant profile 1, 28/63 vs 25/76, aRR 0.72 (0.49-1.05), interaction 0.83; profile 2, 10/11 vs 8/12, aRR 0.59 (0.37-0.96), interaction 0.40. |
| PDF pp. 49-50, eTable 10 | Corresponding treatment-effect estimates using composite core. Example mRS 5-6: concordant 74/118 MM vs 53/112 EVT, aRR 0.75 (0.60-0.92); discordant profile 1, 14/28 vs 13/38, aRR 0.90 (0.52-1.56), interaction 0.92; profile 2, 11/12 vs 9/14, aRR 0.59 (0.39-0.88), interaction 0.38. |
| PDF p. 51, eTable 11 | MR-DWI follow-up infarct-growth medians (IQR): MM N=101, mTICI 0-2a N=24, mTICI 2b-3 N=79. CTP/MRI growth 95 (56-135), 125 (76-179), 68 (37-142) mL; composite growth 63 (22-102), 91 (71-142), 45 (16-90) mL; CT-hypodensity growth 69 (31-122), 107 (87-152), 60 (24-110) mL. |
| PDF p. 52, eTable 12 | Infarct growth by functional outcome. Dependent (mRS 3-6) N=290 vs independent (0-2) N=46: CTP/MRI 102 (61-167) vs 45 (32-88) mL; composite 77 (31-127) vs 23.5 (11-48) mL; both p<0.001. No independent ambulation N=240 vs independent ambulation N=96: CTP/MRI 110.5 (65.5-174.5) vs 65.5 (32.5-100.5) mL; composite 85.5 (36-144) vs 31.5 (10-67) mL; both p<0.001. |
| PDF p. 53, eTable 13 | Three patients with ≥10-mL core overestimation vs follow-up infarct volume. Rows: ID 1, core 162 mL/hypodensity 33 mL/follow-up 143 mL/LKW-to-CTP 642 min/CTP-to-procedure end 77 min; ID 2, 140/0/90/289 min/N/A; ID 3, 93/5/11/51 min/125 min. |

## Handoff notes

- This is an extraction/provenance map, not an error assessment.
- The most direct arithmetic/consistency inputs are the flow values (PDF p. 8), ITT outcome numerators/denominators (p. 38), as-treated denominators (pp. 35-36), the mRS distributions (pp. 26-34), and the sensitivity tables (pp. 39-50).
- Forest-plot values on PDF pp. 13-19 were verified from rendered images because native extraction was sparse/OCR-unavailable; use the page images for any cell-level comparison.
