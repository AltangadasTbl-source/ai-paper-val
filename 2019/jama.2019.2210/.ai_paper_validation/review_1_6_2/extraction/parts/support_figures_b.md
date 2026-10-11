# Support figure mapping shard B

Runtime task ID: /root/support_figures_b. Role: fresh support quantitative mapper, gpt-6.1-sol/medium. Exact scope: DOC003, joi190023supp2_prod.pdf, PDF pages 22–41 inclusive, REPORT. All 20 pages were opened using view_image on the reusable 150 dpi rendered pages. Native/layout text served as a locator and was checked visually. No historical scientific map, finding, candidate, or report was read. No source or reusable artifact was changed. No new rendering or OCR was required; compute device CPU per tooling_record.md.

Reusable assets for each page N: `.ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-NNN.txt` and `rendered_pages/page-NN.png`, all USABLE in the asset inventory. Engine: legacy layout/native text with current Poppler corroboration, and legacy 150 dpi rasterization. Fresh-required assigned units: 0. Fresh scientific mapping: 20/20.

## Common figure definitions and scope

Every page contains one figure panel, one hazard ratio with a printed 95% confidence interval, one printed P value, one printed P interaction value, two cumulative hazard curves, and an eight-value number-at-risk table. All captions explicitly define the curves as cumulative hazard of **relapse or death** in the named subgroup. The horizontal axis is **Years since Randomization**, with labeled values **0, 2, 4, 6**, which align with all risk-table columns. The green line is labeled **Placebo** and the orange/red line **Vitamin D**. The vertical axis has numeric ticks but no separate printed axis title; its cumulative-hazard interpretation comes from the caption. These are cumulative hazards, not percentages or event counts. Curve endpoints are not numerically tabulated; no interpolated endpoint was substituted for a printed value.

The figure annotations say **Hazard ratio** and **95%CI**, **P**, and **P interaction**. They do not give a model name, covariates, CI construction, test name, sidedness, interaction contrast, or a separately printed reference-group formula within the assigned pages. Matching keys below mean relapse-or-death hazard ratio for the named subgroup and Vitamin D versus placebo; this contrast follows the two-group figure context and must be matched with the other assigned evidence maps before a cross-location comparison. No event numerators or event percentages are printed. The year-zero risk counts identify displayed starting subgroup populations; later risk counts are surviving contributors to the risk sets, not endpoint event totals. No formulas, cached workbook values, sensitivity analyses, administrative material, or plan content occurs in these 20 pages. The only non-result footer is the 2019 American Medical Association copyright.

Local keys FB001–FB020 each describe a complete panel relationship: subgroup definition/status, HR/CI/P/interaction, time alignment, both risk rows, and curve/axis labels. There are **20 panels, 20 HR–CI–P relationships, 20 interaction-P relationships, 20 paired risk-table relationships (160 counts)**. Thus 40 inferential relationships if the two printed tests per panel are tracked independently. No stable N/S identifiers or candidate judgments are assigned here.

## Complete panel map

Risk counts are ordered at years **0 / 2 / 4 / 6**. Final ordering records visual curve labels near the end of each display, not an inference of a proportional-hazards model or whole-period direction.

| Local key | PDF page / figure | Subgroup and caption analysis label | HR | Printed 95% CI | P | P interaction | Placebo risk counts | Vitamin D risk counts | Final visual ordering | Matching main-paper key |
|---|---|---|---:|---|---:|---:|---|---|---|---|
| FB001 | 22 / eFigure 3P | DBP1 TT; Prespecified subgroup analysis | 0.71 | 0.42 to 1.22 | 0.22 | 0.63 | 82 / 54 / 27 / 7 | 134 / 92 / 53 / 23 | Placebo above Vitamin D | relapse/death; DBP1 TT polymorphism |
| FB002 | 23 / eFigure 3Q | DBP1 TG; Prespecified subgroup analysis | 1.00 | 0.44 to 2.24 | 0.99 | 0.49 | 59 / 43 / 21 / 6 | 87 / 63 / 37 / 9 | Placebo slightly above Vitamin D; curves cross | relapse/death; DBP1 TG polymorphism |
| FB003 | 24 / eFigure 3R | DBP1 GG; Prespecified subgroup analysis | 0.65 | 0.14 to 2.92 | 0.57 | 0.91 | 9 / 7 / 3 / 1 | 10 / 7 / 2 / 2 | Placebo above Vitamin D; early crossing | relapse/death; DBP1 GG polymorphism |
| FB004 | 25 / eFigure 3S | DBP2 CC; Prespecified subgroup analysis | 0.60 | 0.34 to 1.05 | 0.07 | 0.16 | 81 / 52 / 18 / 6 | 115 / 78 / 49 / 15 | Placebo above Vitamin D | relapse/death; DBP2 CC polymorphism |
| FB005 | 26 / eFigure 3T | DBP2 CA; Prespecified subgroup analysis | 1.19 | 0.55 to 2.60 | 0.66 | 0.16 | 58 / 46 / 29 / 7 | 91 / 64 / 33 / 14 | Vitamin D slightly above Placebo | relapse/death; DBP2 CA polymorphism |
| FB006 | 27 / eFigure 3U | DBP2 AA; Prespecified subgroup analysis | 0.80 | 0.20 to 3.20 | 0.75 | 1.00 | 11 / 6 / 4 / 1 | 25 / 20 / 10 / 5 | Vitamin D slightly above Placebo; crossing | relapse/death; DBP2 AA polymorphism |
| FB007 | 28 / eFigure 4A | Men; Post hoc subgroup analysis | 0.59 | 0.37 to 0.97 | 0.04 | 0.13 | 103 / 64 / 28 / 9 | 173 / 120 / 65 / 30 | Placebo above Vitamin D | relapse/death; men |
| FB008 | 29 / eFigure 4B | Women; Post hoc subgroup analysis | 1.18 | 0.56 to 2.51 | 0.66 | 0.13 | 63 / 49 / 26 / 7 | 78 / 56 / 28 / 5 | Vitamin D slightly above Placebo | relapse/death; women |
| FB009 | 30 / eFigure 5A | Age 65 and younger; Post hoc subgroup analysis of younger than median (≤65 years of age) | 0.86 | 0.44 to 1.68 | 0.65 | 0.48 | 91 / 68 / 33 / 11 | 106 / 76 / 45 / 18 | Placebo above Vitamin D; early crossing | relapse/death; age ≤65 years |
| FB010 | 31 / eFigure 5B | Age older than 65 years; Post hoc subgroup analysis of older than median (>65 years of age) | 0.63 | 0.37 to 1.05 | 0.07 | 0.48 | 75 / 45 / 21 / 5 | 145 / 100 / 48 / 17 | Placebo above Vitamin D | relapse/death; age >65 years |
| FB011 | 32 / eFigure 6A | BMI <25 kg/m²; Post hoc subgroup analysis | 0.75 | 0.49 to 1.16 | 0.20 | 0.87 | 144 / 99 / 47 / 14 | 208 / 141 / 68 / 28 | Placebo above Vitamin D; early crossing | relapse/death; BMI <25 kg/m² |
| FB012 | 33 / eFigure 6B | BMI ≥25 kg/m²; Post hoc subgroup analysis | 0.88 | 0.22 to 3.55 | 0.86 | 0.87 | 21 / 13 / 6 / 2 | 41 / 33 / 24 / 7 | Vitamin D slightly above Placebo; crossing | relapse/death; BMI ≥25 kg/m² |
| FB013 | 34 / eFigure 7A | Esophageal cancer; Subgroup analysis (no prespecified/post hoc modifier in caption) | 1.01 | 0.42 to 2.44 | 0.99 | 0.65 | 18 / 7 / 3 / 2 | 22 / 11 / 4 / 2 | Placebo above Vitamin D; crossing | relapse/death; esophageal cancer |
| FB014 | 35 / eFigure 7B | Gastric cancer; Subgroup analysis (no prespecified/post hoc modifier in caption) | 0.84 | 0.40 to 1.76 | 0.64 | 0.88 | 68 / 53 / 26 / 8 | 106 / 84 / 50 / 17 | Placebo above Vitamin D; crossing | relapse/death; gastric cancer |
| FB015 | 36 / eFigure 7C | Colorectal cancer; Subgroup analysis (no prespecified/post hoc modifier in caption) | 0.69 | 0.39 to 1.24 | 0.22 | 0.66 | 79 / 52 / 25 / 6 | 122 / 80 / 38 / 15 | Placebo above Vitamin D | relapse/death; colorectal cancer |
| FB016 | 37 / eFigure 8A | Stage I; Post hoc subgroup analysis | 0.39 | 0.14 to 1.13 | 0.08 | 0.14 | 67 / 53 / 29 / 7 | 115 / 100 / 61 / 22 | Placebo above Vitamin D | relapse/death; stage I |
| FB017 | 38 / eFigure 8B | Stage II; Post hoc subgroup analysis | 1.20 | 0.51 to 2.80 | 0.68 | 0.23 | 48 / 34 / 14 / 6 | 63 / 42 / 18 / 7 | Placebo above Vitamin D at end; crossing | relapse/death; stage II |
| FB018 | 39 / eFigure 8C | Stage III; Post hoc subgroup analysis | 0.86 | 0.51 to 1.46 | 0.58 | 0.62 | 51 / 26 / 11 / 3 | 73 / 34 / 14 / 6 | Placebo above Vitamin D; early crossing | relapse/death; stage III |
| FB019 | 40 / eFigure 9A | Adenocarcinoma; Post hoc subgroup analysis | 0.70 | 0.43 to 1.13 | 0.14 | 0.47 | 147 / 104 / 50 / 14 | 226 / 164 / 89 / 33 | Placebo above Vitamin D | relapse/death; adenocarcinoma |
| FB020 | 41 / eFigure 9B | Non-adenocarcinoma; Post hoc subgroup analysis | 1.18 | 0.54 to 2.60 | 0.68 | 0.47 | 19 / 9 / 4 / 2 | 25 / 12 / 4 / 2 | Placebo above Vitamin D at end; crossing | relapse/death; non-adenocarcinoma |

## Axis and population details

| Keys / PDF pages | All printed vertical ticks, in ascending order | Population definition in caption |
|---|---|---|
| FB001–002 / 22–23 | 0.00, 0.20, 0.40, 0.60 | Patients with polymorphism of DBP1 TT or TG respectively |
| FB003 / 24 | 0.00, 0.20, 0.40, 0.60, 0.80 | Patients with polymorphism of DBP1 GG |
| FB004–006 / 25–27 | 0.00, 0.20, 0.40, 0.60 | Patients with polymorphism of DBP2 CC, CA, or AA respectively |
| FB007–008 / 28–29 | 0.00, 0.20, 0.40, 0.60 | Men or women respectively |
| FB009–010 / 30–31 | 0.00, 0.20, 0.40, 0.60, 0.80 | Participants age 65 and younger, or older than 65 respectively |
| FB011–012 / 32–33 | 0.00, 0.20, 0.40, 0.60 | Participants with BMI <25 kg/m², or ≥25 kg/m² respectively; plot title uses kg/m2 and ASCII >= on p. 33 |
| FB013 / 34 | 0.00, 0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60 | Patients with esophageal cancer |
| FB014–015 / 35–36 | 0.00, 0.20, 0.40, 0.60 | Patients with gastric or colorectal cancer respectively |
| FB016–018 / 37–39 | 0.00, 0.20, 0.40, 0.60, 0.80, 1.00 | Patients with stage I, II, or III respectively |
| FB019 / 40 | 0.00, 0.20, 0.40 | Patients with adenocarcinoma |
| FB020 / 41 | 0.00, 0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60, 1.80, 2.00 | Patients with non-adenocarcinoma |

All horizontal axes and risk-table timepoints are 0, 2, 4, and 6 years. The curves extend beyond the last labeled 6-year tick, but no separate final time or cumulative-hazard value is printed. HR units are dimensionless; P and interaction P are unitless. Age units are years and BMI units kg/m². No event denominator beyond the risk-table entries is printed in this shard. Caption analysis-status wording is reproduced without assigning an unprinted status to eFigures 7A–C. DBP1 and DBP2 are figure labels; no rs identifier is printed on these pages, so the merge must use the corresponding provided definition instead of assuming an rs identifier.

## Per-page complete coverage

Every row has exactly one assigned artifact path, relative to review_1_6_2.

| Source / page | Inspection | Applicable content | Local key | Artifact | Status |
|---|---|---|---|---|---|
| DOC003 p. 22 | Native text + full reusable image | eFigure 3P | FB001 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 23 | Native text + full reusable image | eFigure 3Q | FB002 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 24 | Native text + full reusable image | eFigure 3R | FB003 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 25 | Native text + full reusable image | eFigure 3S | FB004 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 26 | Native text + full reusable image | eFigure 3T | FB005 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 27 | Native text + full reusable image | eFigure 3U | FB006 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 28 | Native text + full reusable image | eFigure 4A | FB007 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 29 | Native text + full reusable image | eFigure 4B | FB008 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 30 | Native text + full reusable image | eFigure 5A | FB009 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 31 | Native text + full reusable image | eFigure 5B | FB010 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 32 | Native text + full reusable image | eFigure 6A | FB011 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 33 | Native text + full reusable image | eFigure 6B | FB012 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 34 | Native text + full reusable image | eFigure 7A | FB013 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 35 | Native text + full reusable image | eFigure 7B | FB014 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 36 | Native text + full reusable image | eFigure 7C | FB015 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 37 | Native text + full reusable image | eFigure 8A | FB016 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 38 | Native text + full reusable image | eFigure 8B | FB017 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 39 | Native text + full reusable image | eFigure 8C | FB018 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 40 | Native text + full reusable image | eFigure 9A | FB019 | extraction/parts/support_figures_b.md | COMPLETE |
| DOC003 p. 41 | Native text + full reusable image | eFigure 9B | FB020 | extraction/parts/support_figures_b.md | COMPLETE |

## Exact source locations

All links are relative from this artifact to the package root.
- [DOC003 PDF page 22](../../../../joi190023supp2_prod.pdf#page=22)
- [DOC003 PDF page 23](../../../../joi190023supp2_prod.pdf#page=23)
- [DOC003 PDF page 24](../../../../joi190023supp2_prod.pdf#page=24)
- [DOC003 PDF page 25](../../../../joi190023supp2_prod.pdf#page=25)
- [DOC003 PDF page 26](../../../../joi190023supp2_prod.pdf#page=26)
- [DOC003 PDF page 27](../../../../joi190023supp2_prod.pdf#page=27)
- [DOC003 PDF page 28](../../../../joi190023supp2_prod.pdf#page=28)
- [DOC003 PDF page 29](../../../../joi190023supp2_prod.pdf#page=29)
- [DOC003 PDF page 30](../../../../joi190023supp2_prod.pdf#page=30)
- [DOC003 PDF page 31](../../../../joi190023supp2_prod.pdf#page=31)
- [DOC003 PDF page 32](../../../../joi190023supp2_prod.pdf#page=32)
- [DOC003 PDF page 33](../../../../joi190023supp2_prod.pdf#page=33)
- [DOC003 PDF page 34](../../../../joi190023supp2_prod.pdf#page=34)
- [DOC003 PDF page 35](../../../../joi190023supp2_prod.pdf#page=35)
- [DOC003 PDF page 36](../../../../joi190023supp2_prod.pdf#page=36)
- [DOC003 PDF page 37](../../../../joi190023supp2_prod.pdf#page=37)
- [DOC003 PDF page 38](../../../../joi190023supp2_prod.pdf#page=38)
- [DOC003 PDF page 39](../../../../joi190023supp2_prod.pdf#page=39)
- [DOC003 PDF page 40](../../../../joi190023supp2_prod.pdf#page=40)
- [DOC003 PDF page 41](../../../../joi190023supp2_prod.pdf#page=41)

## Completion and limits

Assigned coverage complete: 20/20 pages. No page was sampled or omitted. No transcription remains uncertain, and the source-visible numeric fields reconcile with the reused text transcription. Limitations of this extraction scope are the figure-local absence of model/test construction and explicit interaction contrasts, and the absence of numerical curve endpoint tabulation. These are extraction facts, not diagnosed findings. Matching main-paper locations are to be supplied by the disjoint main-paper map; this shard supplies outcome/population/status/contrast matching keys only and does not inspect outside its assigned source pages. There are no scientific-coverage gaps and no derivative gaps in the assigned scope.
