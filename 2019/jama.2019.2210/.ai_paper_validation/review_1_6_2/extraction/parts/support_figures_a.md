# Support figure mapping A

Runtime task ID: `/root/support_figures_a`. Role: fresh support quantitative mapper, gpt-6.1-sol / medium. Exact scope: DOC003, `joi190023supp2_prod.pdf`, PDF pages 2–21 inclusive, 20 REPORT pages. This artifact maps evidence and makes no candidate decisions.

Read controls: QUALITY_CONTROL_SCOPE.md, workflow_1_6_2/review_contract.md, workflow_1_6_2/settings.toml, current source inventory, source coverage, evidence asset inventory and tooling record. Every assigned page has usable reusable extraction. All 20 page images were individually opened with view_image and visually inspected, including plot annotations, risk tables, table columns, captions, and footnotes. Reusable native text is a locator/transcription aid only. No old scientific conclusions were read.

Engines: reusable layout/native text (legacy extraction, curator corroborated with current Poppler); reusable rendered pages (legacy rasterization, 150 dpi). No new preprocessing, OCR, or rendering needed. Compute device CPU. Inputs remain unchanged. Canonical assets: `.ai_paper_validation/document_outputs/DOC-JAMA-2019-2210-SUPP-RESULTS/native_text/page-NNN.txt` and `rendered_pages/page-NN.png`, with NNN/NN equal to the PDF page below.

## Per-page coverage

| Source | PDF page | Content | Local relationships | Direct visual inspection | Status |
|---|---:|---|---|---|---|
| DOC003 | 2 | eFigure 1A, post hoc mean 25(OH)D and relapse/death | FA001 | Complete | COMPLETE |
| DOC003 | 3 | eFigure 1B, post hoc mean 25(OH)D and all-cause death | FA002 | Complete | COMPLETE |
| DOC003 | 4 | eTable 1 counts and Cox models | FA003–FA019 | Complete | COMPLETE |
| DOC003 | 5 | eFigure 2 longitudinal 25(OH)D box plots | FA020 | Complete | COMPLETE |
| DOC003 | 6 | eTable 2 multiple imputation Cox subgroup models | FA021–FA025 | Complete | COMPLETE |
| DOC003 | 7 | eFigure 3A, FokI CC | FA026 | Complete | COMPLETE |
| DOC003 | 8 | eFigure 3B, FokI CT | FA027 | Complete | COMPLETE |
| DOC003 | 9 | eFigure 3C, FokI TT | FA028 | Complete | COMPLETE |
| DOC003 | 10 | eFigure 3D, BsmI AA | FA029 | Complete | COMPLETE |
| DOC003 | 11 | eFigure 3E, BsmI AG | FA030 | Complete | COMPLETE |
| DOC003 | 12 | eFigure 3F, BsmI GG | FA031 | Complete | COMPLETE |
| DOC003 | 13 | eFigure 3G, CDK2 GG | FA032 | Complete | COMPLETE |
| DOC003 | 14 | eFigure 3H, CDK2 GA | FA033 | Complete | COMPLETE |
| DOC003 | 15 | eFigure 3I, CDK2 AA | FA034 | Complete | COMPLETE |
| DOC003 | 16 | eFigure 3J, ApaI GG | FA035 | Complete | COMPLETE |
| DOC003 | 17 | eFigure 3K, ApaI GT | FA036 | Complete | COMPLETE |
| DOC003 | 18 | eFigure 3L, ApaI TT | FA037 | Complete | COMPLETE |
| DOC003 | 19 | eFigure 3M, TaqI TT | FA038 | Complete | COMPLETE |
| DOC003 | 20 | eFigure 3N, TaqI TC | FA039 | Complete | COMPLETE |
| DOC003 | 21 | eFigure 3O, TaqI CC | FA040 | Complete | COMPLETE |

All 20 pages contain result-relevant content; none is no-applicable. No PLAN/administrative page occurs in this assigned shard. No Office/CSV source or workbook formula/cached value is present.

## Post hoc mean 25(OH)D relationships

Grouping is patient-average serum 25(OH)D over the course of the trial, rather than baseline serum concentration. Units ng/mL. Caption bins and colors: low <20 green; intermediate 20 to <30 orange; high 30 to <40 blue; very high 40 to <50 brown; extremely high ≥50 light blue. Both plots label their rows with shorthand `~20ng/mL`, `20ng/mL~`, `30ng/mL~`, `40ng/mL~`, `50ng/mL~`. These are recorded alongside the explicit caption boundaries.

### FA001 — eFigure 1A, relapse or death

[DOC003 PDF p. 2](../../../../joi190023supp2_prod.pdf#page=2), REPORT. Title in plot: `mean 25(OH)D ~20ng.mL vs. 40~50ng/mL`. Annotation: HR 0.29 (95% CI 0.11 to 0.74), P=0.01. Caption identifies post hoc analysis. Match key: relapse/death; achieved patient-mean 40–<50 vs <20 ng/mL; unadjusted HR counterpart eTable 1 FA012; not the randomized vitamin D versus placebo primary comparison. HR reference is established by eTable 1 (<20 reference).

Y axis cumulative hazard rate for relapse or death, printed ticks 0.00, 0.20, 0.40. X axis years since randomization, ticks 0, 2, 4, 6. Risk counts below are exact printed values; no event-count labels are supplied. Step coordinates themselves have no numeric data labels and are not treated as exact event data. At the plotted end, <20 is highest; then 20–<30, 30–<40, ≥50, and 40–<50 lowest.

| Mean 25(OH)D | At risk year 0 | Year 2 | Year 4 | Year 6 |
|---|---:|---:|---:|---:|
| <20 | 114 | 64 | 29 | 10 |
| 20–<30 | 123 | 78 | 32 | 9 |
| 30–<40 | 94 | 70 | 39 | 17 |
| 40–<50 | 39 | 38 | 21 | 8 |
| ≥50 | 43 | 37 | 25 | 7 |

### FA002 — eFigure 1B, all-cause death

[DOC003 PDF p. 3](../../../../joi190023supp2_prod.pdf#page=3), REPORT. Plot title: `mean 25(OH)D ~20ng.mL vs. 30~40ng/mL`. Annotation HR 0.39 (95% CI 0.18 to 0.84), P=0.02. Caption post hoc analysis. Match key: all-cause death; patient-mean 30–<40 vs <20 ng/mL; unadjusted eTable 1 FA010. Y cumulative hazard rate for death, ticks 0.00, 0.20, 0.40. X years since randomization, ticks 0,2,4,6. Final plotted order: <20 highest, then 20–<30, ≥50, 30–<40, 40–<50 lowest. Exact step coordinates/event counts are unlabeled.

| Mean 25(OH)D | At risk year 0 | Year 2 | Year 4 | Year 6 |
|---|---:|---:|---:|---:|
| <20 | 114 | 78 | 36 | 13 |
| 20–<30 | 123 | 87 | 37 | 12 |
| 30–<40 | 94 | 76 | 43 | 17 |
| 40–<50 | 39 | 39 | 21 | 8 |
| ≥50 | 43 | 42 | 28 | 7 |

### FA003 — eTable 1 population counts and percentages

[DOC003 PDF p. 4](../../../../joi190023supp2_prod.pdf#page=4), REPORT. Title: Cox proportional hazard model by patient's mean 25(OH)D level over the course of the trial. Column labels `Active n (%)` and `Placebo n (%)`. All printed counts and percentages follow. Within-arm bin percentages are displayed next to bin counts; total-row percentages use the pooled total. Reference category in both outcome columns is <20. The pooled bin totals below are derived sums, explicitly separated from source values, and match the year-0 figure counts.

| Mean 25(OH)D, ng/mL | Active n (%) printed | Placebo n (%) printed | Pooled n, derived |
|---|---|---|---:|
| <20 | 40 (16) | 74 (45) | 114 |
| 20 to <30 | 56 (23) | 67 (41) | 123 |
| 30 to <40 | 71 (29) | 23 (14) | 94 |
| 40 to <50 | 39 (16) | 0 (0) | 39 |
| ≥50 | 42 (17) | 1 (0.6) | 43 |
| Total | 248 (60) | 165 (40) | 413 |

### FA004–FA019 — all eTable 1 inferential rows

Same [DOC003 PDF p. 4](../../../../joi190023supp2_prod.pdf#page=4), REPORT. Two result lines per bin/outcome, first HR (95%CI) P, second AHR*, 95%CI, P. Footnote exactly defines AHR as hazard ratio adjusted with vitamin D supplementation. All contrasts use <20 ng/mL mean as reference. Null HR 1; event hazard, not survival probability. The table specifies Cox proportional hazard model but no further covariates beyond the AHR footnote, no sidedness, and no interaction P in this display.

| Local key | Outcome | Mean ng/mL vs <20 | Measure | Estimate | 95% CI lower | Upper | P |
|---|---|---|---|---:|---:|---:|---:|
| FA004 | Relapse or death | 20–<30 | HR | 0.62 | 0.37 | 1.02 | 0.06 |
| FA005 | Relapse or death | 20–<30 | AHR | 0.61 | 0.37 | 1.01 | 0.05 |
| FA006 | All-cause death | 20–<30 | HR | 0.66 | 0.35 | 1.24 | 0.20 |
| FA007 | All-cause death | 20–<30 | AHR | 0.64 | 0.34 | 1.20 | 0.16 |
| FA008 | Relapse or death | 30–<40 | HR | 0.47 | 0.27 | 0.84 | 0.01 |
| FA009 | Relapse or death | 30–<40 | AHR | 0.44 | 0.24 | 0.82 | 0.009 |
| FA010 | All-cause death | 30–<40 | HR | 0.39 | 0.18 | 0.84 | 0.02 |
| FA011 | All-cause death | 30–<40 | AHR | 0.33 | 0.15 | 0.74 | 0.007 |
| FA012 | Relapse or death | 40–<50 | HR | 0.29 | 0.11 | 0.74 | 0.01 |
| FA013 | Relapse or death | 40–<50 | AHR | 0.26 | 0.10 | 0.71 | 0.008 |
| FA014 | All-cause death | 40–<50 | HR | 0.44 | 0.17 | 1.16 | 0.10 |
| FA015 | All-cause death | 40–<50 | AHR | 0.34 | 0.12 | 0.96 | 0.04 |
| FA016 | Relapse or death | ≥50 | HR | 0.44 | 0.21 | 0.96 | 0.04 |
| FA017 | Relapse or death | ≥50 | AHR | 0.40 | 0.18 | 0.92 | 0.03 |
| FA018 | All-cause death | ≥50 | HR | 0.55 | 0.24 | 1.29 | 0.17 |
| FA019 | All-cause death | ≥50 | AHR | 0.43 | 0.17 | 1.08 | 0.07 |

Matching main-paper key is the post hoc achieved-average serum grouping analysis, distinct from baseline serum subgroups and randomized comparison. Statistical checker should retain both HR and AHR lines rather than substitute one for the other.

## FA020 — eFigure 2 longitudinal serum 25(OH)D

[DOC003 PDF p. 5](../../../../joi190023supp2_prod.pdf#page=5), REPORT. Serum level of 25(OH)D in ng/mL, y ticks 0,20,40,60,80,100. X groups Placebo left and Vitamin D right. Within each group five boxes: `pre 25OHD` blue; `post 25OHD 1 yr after` red; `post 25OHD 2 yrs after` green; `post 25OHD 3 yrs after` orange; `post 25OHD 4 yrs after` gray-green. Caption: measured before (pre), and every year within the same calendar month 1,2,3,4 years after starting supplements. No sample counts, numeric median/IQR/whisker labels, numeric outlier labels, P values, confidence limits, or box/whisker convention definition is printed.

Graphical values are available only by approximate reading against the scale; the following visual coordinates in ng/mL are approximate locators, not printed extraction-ready values. No exact values are invented. All boxes/whiskers/outlier marks are included to document complete visual coverage.

| Group | Measurement | Approx median | Approx box lower–upper | Approx whisker lower–upper | Approx visible outlier marks |
|---|---|---:|---|---|---|
| Placebo | Pre | 21 | 15–27 | 7–37 | 52 |
| Placebo | Year 1 | 20 | 15–27 | 4–41 | 53,73 |
| Placebo | Year 2 | 22 | 16–30 | 7–41 | 53,73 |
| Placebo | Year 3 | 21 | 7–30 | 7–47 | 53,62 |
| Placebo | Year 4 | 22 | 20–26 | 15–29 | 36,39 |
| Vitamin D | Pre | 21 | 16–27 | 6–43 | 57 |
| Vitamin D | Year 1 | 41 | 34–55 | 9–87 | 99 |
| Vitamin D | Year 2 | 50 | 37–62 | 9–99 | 101 |
| Vitamin D | Year 3 | 52 | 37–64 | 12–84 | None visible |
| Vitamin D | Year 4 | 54 | 39–74 | 32–82 | None visible |

Visual direction: placebo medians near 20 across measurements; vitamin D post-treatment boxes higher than its pretreatment box. Match key: longitudinal serum-level response, same-calendar-month annual observations; no treatment-effect hazard ratio in this panel. Limitation: source provides no exact numeric summary data, so plotted-coordinate approximations cannot support exact arithmetic checks.

## Multiple-imputation sensitivity analysis

### FA021 — eTable 2 missingness/method definition

[DOC003 PDF p. 6](../../../../joi190023supp2_prod.pdf#page=6), REPORT. Title Cox proportional hazard model by subgroup of 25(OH)D level with multiple imputation. Footnote: baseline serum 25(OH)D missing in 3 (1%) vitamin D and 4 (2%) placebo patients; multiple imputation used for these missing data. The table does not print arm denominators, subgroup counts after imputation, number of imputations, imputation model, or pooling formula. Those inputs must be matched from supplied sources if needed; they are not inferred here. Baseline subgroup boundaries are printed `0 to <20 ng/mL` and `20 to 40 ng/mL`, not achieved-average serum bins. Match main key: baseline 25(OH)D stratification with missing-baseline sensitivity analysis.

### FA022–FA025 — every eTable 2 outcome/subgroup result

Same [DOC003 PDF p. 6](../../../../joi190023supp2_prod.pdf#page=6), REPORT. Columns HR (95%CI) P. Contrast is randomized vitamin D versus placebo as the contextual subgroup treatment comparison; the table itself does not restate reference arm or further adjustment.

| Local key | Outcome | Baseline serum 25(OH)D | HR | 95% CI lower | Upper | P |
|---|---|---|---:|---:|---:|---:|
| FA022 | Relapse or death | 0 to <20 ng/mL | 1.15 | 0.65 | 2.05 | 0.63 |
| FA023 | Relapse or death | 20 to 40 ng/mL | 0.46 | 0.24 | 0.86 | 0.02 |
| FA024 | All-cause death | 0 to <20 ng/mL | 1.36 | 0.66 | 2.81 | 0.41 |
| FA025 | All-cause death | 20 to 40 ng/mL | 0.60 | 0.28 | 1.30 | 0.20 |

## Prespecified genotype subgroup panels

FA026–FA040 map eFigures 3A–3O, one panel per page. Every caption says `Prespecified subgroup analysis of [genotype]` and `Cumulative hazard curves of relapse or death were drawn in subgroup of patients with polymorphism of [genotype]`. Outcome is relapse or death, not all-cause death. Each panel labels Placebo green and Vitamin D orange/red; x axis Years since Randomization, ticks 0,2,4,6; y ticks 0.00,0.20,0.40,0.60. Each panel prints HR, 95%CI, within-subgroup P, and `P interaction`. P interaction refers to effect modification rather than the within-subgroup treatment test; reference comparator for interaction is not explicitly defined in these pages. No event counts, covariate adjustment, test sidedness, or exact step coordinates are printed.

The intended HR match key is vitamin D versus placebo for relapse/death within the named genotype; actual plot labels/directions are separately recorded, without reconciling or diagnosing. Parent/main mapper can match each genotype with the article prespecified genetic subgroup description; no main-paper extraction was independently inspected outside this disjoint shard. All risk counts are exact printed counts, ordered at years 0,2,4,6.

| Local key | Source page/panel | Printed genotype | HR | 95% CI | P | P interaction | Placebo at risk 0,2,4,6 | Vitamin D at risk 0,2,4,6 |
|---|---|---|---:|---|---:|---|---|---|
| FA026 | [p. 7, 3A](../../../../joi190023supp2_prod.pdf#page=7) | FokI CC | 0.65 | 0.34 to 1.26 | 0.20 | 0.65 | 57,37,19,8 | 92,64,35,9 |
| FA027 | [p. 8, 3B](../../../../joi190023supp2_prod.pdf#page=8) | FokI CT | 0.77 | 0.42 to 1.43 | 0.41 | 0.90 | 75,53,24,5 | 117,89,48,23 |
| FA028 | [p. 9, 3C](../../../../joi190023supp2_prod.pdf#page=9) | FokI TT | 0.97 | 0.32 to 2.88 | 0.95 | 0.67 | 25,18,10,3 | 36,21,10,3 |
| FA029 | [p. 10, 3D](../../../../joi190023supp2_prod.pdf#page=10) | BsmI AA | 0.44 | 0.03 to 7.16 | 0.56 | 0.66 | 8,3,1,0 | 14,11,5,2 |
| FA030 | [p. 11, 3E](../../../../joi190023supp2_prod.pdf#page=11) | BsmI AG | 0.60 | 0.24 to 1.48 | 0.27 | 0.50 | 23,13,7,1 | 42,26,15,3 |
| FA031 | [p. 12, 3F](../../../../joi190023supp2_prod.pdf#page=12) | BsmI GG | 0.86 | 0.52 to 1.41 | 0.55 | 0.38 | 119,88,43,13 | 175,125,72,29 |
| FA032 | [p. 13, 3G](../../../../joi190023supp2_prod.pdf#page=13) | CDK2 GG | 0.69 | 0.34 to 1.38 | 0.29 | 0.64 | 49,32,18,5 | 89,62,34,7 |
| FA033 | [p. 14, 3H](../../../../joi190023supp2_prod.pdf#page=14) | CDK2 GA | 0.72 | 0.39 to 1.32 | 0.28 | 0.63 | 77,54,25,7 | 103,72,46,20 |
| FA034 | [p. 15, 3I](../../../../joi190023supp2_prod.pdf#page=15) | CDK2 AA | 1.82 | 0.48 to 6.88 | 0.38 | 0.19 | 24,18,8,2 | 38,28,12,7 |
| FA035 | [p. 16, 3J](../../../../joi190023supp2_prod.pdf#page=16) | ApaI GG | 1.00 | 0.49 to 2.05 | 0.99 | 0.35 | 69,53,30,9 | 96,73,39,15 |
| FA036 | [p. 17, 3K](../../../../joi190023supp2_prod.pdf#page=17) | ApaI GT | 0.70 | 0.38 to 1.27 | 0.24 | 0.63 | 61,42,18,5 | 104,65,40,14 |
| FA037 | [p. 18, 3L](../../../../joi190023supp2_prod.pdf#page=18) | ApaI TT | 0.53 | 0.15 to 1.84 | 0.32 | 0.49 | 20,9,3,0 | 31,24,13,5 |
| FA038 | [p. 19, 3M](../../../../joi190023supp2_prod.pdf#page=19) | TaqI TT | 0.87 | 0.52 to 1.46 | 0.60 | 0.35 | 115,86,42,13 | 172,122,70,29 |
| FA039 | [p. 20, 3N](../../../../joi190023supp2_prod.pdf#page=20) | TaqI TC | 0.49 | 0.22 to 1.10 | 0.08 | 0.20 | 31,16,8,1 | 54,37,19,4 |
| FA040 | [p. 21, 3O](../../../../joi190023supp2_prod.pdf#page=21) | TaqI CC | — | — to — | 1.00 | — | 4,2,1,0 | 5,3,3,1 |

### Visual directions for each genotype

These are graphical observations, not exact numeric hazard estimates. Crossing curves are retained as observed and no aggregate HR is inferred from their final positions.

| Local key | Curve direction/shape observed |
|---|---|
| FA026 | Placebo finishes higher than vitamin D; early steps overlap/cross. |
| FA027 | Placebo finishes higher; curves nearly meet around year 3.5. |
| FA028 | Vitamin D higher early; placebo later rises above vitamin D and finishes higher. |
| FA029 | Placebo has one low horizontal step from near zero time; vitamin D is initially at zero, rises around year 3, and finishes above placebo. |
| FA030 | Placebo rises higher by around year 2 and finishes above vitamin D. |
| FA031 | Curves overlap/cross in first years; placebo finishes above vitamin D. |
| FA032 | Placebo mostly above vitamin D, ending higher. |
| FA033 | Curves cross early; placebo is higher later and finishes higher. |
| FA034 | Vitamin D above placebo after early follow-up, finishes higher. |
| FA035 | Curves overlap/cross and finish nearly coincident; vitamin D label lies above placebo label. |
| FA036 | Vitamin D rises above placebo early, placebo rises above later and finishes higher. |
| FA037 | Placebo initially higher; curves briefly meet/cross around year 3; placebo finishes higher. |
| FA038 | Curves cross/overlap early; placebo finishes higher. |
| FA039 | Curves cross early; placebo rises well above vitamin D and finishes higher. |
| FA040 | Placebo is at zero throughout the visible line; vitamin D rises once near year 1.8 to a horizontal level around 0.25. HR, CI, interaction shown with dashes; within-subgroup P is explicitly 1.00. |

### Derived genotype baseline-count matching keys

For matching with main-paper genotype availability, sum the three disjoint genotype baseline risk rows within each locus. These are derived counts, not newly printed source totals: FokI placebo 57+75+25=157, vitamin D 92+117+36=245; BsmI placebo 8+23+119=150, vitamin D 14+42+175=231; CDK2 placebo 49+77+24=150, vitamin D 89+103+38=230; ApaI placebo 69+61+20=150, vitamin D 96+104+31=231; TaqI placebo 115+31+4=150, vitamin D 172+54+5=231. Do not identify these with all-randomized denominators without supplied-source context.

## Completeness and limits

20/20 assigned pages mapped and visually inspected; 40 local relationship records FA001–FA040. Inferential inventory: 37 displayed outcome/contrast records (2 graph annotations, 16 eTable 1 estimate rows, 4 eTable 2 rows, 15 genotype panels including one dash-only estimate). The two graph annotations repeat eTable 1 values, leaving 35 distinct outcome/contrast/model entries (34 numeric HR/CI entries and the TaqI CC dash entry). Additional genotype interaction entries: 15 displays, 14 numerical P values and one dash. Numeric count coverage includes 40 mean-serum risk counts, all 12 eTable 1 count/percentage cells, 2 missing-baseline count/percentage pairs, and 120 genotype risk counts. eFigure 2 has 10 boxes and all visible whiskers/outlier marks mapped qualitatively and approximately; exact numerical summaries are absent from the source.

No uncertain transcription remains in printed tables, annotation numbers, risk tables, or captions. Precision limitations are source-driven: unlabelled step coordinates and box-plot values, genotype interaction comparator definition absent within this shard, and HR/CI/interaction dashes at TaqI CC. Scientific page coverage has no gaps. Sources and reused assets were not modified.
