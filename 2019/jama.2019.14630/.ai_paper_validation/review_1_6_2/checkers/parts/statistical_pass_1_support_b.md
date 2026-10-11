# Statistical pass 1: support shard B

Runtime agent: `/root/stat1_support_b`; model `gpt-6.1-sol`; effort `high`; start mode FRESH_SPAWN. Exact scope: S420, S421, S422 and each S534 through S640, inclusive (110 grouped relationships: 107 table rows plus 3 figure groups). eTable9 rows each include both MI and completers. Source role: REPORT. Findings: 2; excluded observations: 1. All 110 relationships have PASS_1_COMPLETE below and in `statistics/parts/support_b.md`; no Pass 2 review is claimed.

I read `QUALITY_CONTROL_SCOPE.md` and `workflow_1_6_2/review_contract.md` completely. Evidence: source-identical native layout `.ai_paper_validation/document_outputs/DOC-004/supp3_layout.txt` (full pp.14–24 and statistical footnotes), the new support evidence map's assigned locators, and source-linked retained figure renders at pp.25–27. No prior scientific conclusion, candidate set or report was used.

## Source confirmation and derivative provenance

All rendering uses CPU. Existing figure images: `.ai_paper_validation/review_1_5_1/preprocessing/DOC-004_visual-25.png`, `DOC-004_visual-26.png`, `DOC-004_visual-27.png`; retained Poppler render, historical version unspecified. For exact-source confirmation I newly rendered and visually opened DOC-004 pp.15,22,26 using direct Poppler `pdftoppm` version 26.01.0, 120 dpi, PNG. Commands and resulting package-relative artifacts:

| Source unit | Engine and device | Command | Derivative |
|---|---|---|---|
| DOC-004 p.15 | Poppler pdftoppm 26.01.0, CPU | pdftoppm -f 15 -l 15 -r 120 -singlefile -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-support-b-p15 | preprocessing/stat1-support-b-p15.png |
| DOC-004 p.22 | Poppler pdftoppm 26.01.0, CPU | pdftoppm -f 22 -l 22 -r 120 -singlefile -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-support-b-p22 | preprocessing/stat1-support-b-p22.png |
| DOC-004 p.26 | Poppler pdftoppm 26.01.0, CPU | pdftoppm -f 26 -l 26 -r 120 -singlefile -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-support-b-p26 | preprocessing/stat1-support-b-p26.png |

## Findings

### F-ST1-201

**Title:** Repeated 6-month alcohol confidence-interval versus P-value conflict in sensitivity analyses.

**Relationships:** S542 and S620. **Locations and roles:** REPORT [DOC-004 PDF p.15](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=15), eTable5, Total alcohol (%E), 6-month change, between-group columns; REPORT [DOC-004 PDF p.22](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=22), eTable8, same outcome/time, between-group columns. These are within the same results supplement: proposed primary relationship S_W, all relationships S_W. **Focus area:** B. **Proposed review domain:** statistical_results.

**Printed values:** Completers: intervention -0.3 (-0.4 to -0.2), control -0.1 (-0.2 to 0), contrast -0.2 (-0.4 to 0), P=.02. Baseline replacement: intervention -0.3 (-0.4 to -0.2), control -0.1 (-0.2 to 0), contrast -0.2 (-0.3 to 0), P=.02. Each table defines the changes as means with 95% CI from mixed models accounting for site and couples as random factors. Population keys differ and are retained: completers 2862/2883 at M6 versus replacement 3272/3311.

**Rule and calculation:** Null for the mean-change contrast is zero. In both rows, lower limit <0 and upper limit =0, so the printed 95% interval includes zero; .02<.05 indicates significance. The same printed row therefore gives incompatible null-exclusion and P classifications. Point estimates remain inside their intervals and endpoint order is coherent; the finding is specifically the printed interval-versus-P relationship. Display-precision intervals and relative-discrepancy calculations are not applied: category 1 explicitly has no rounding exemption. Even if an unrounded upper limit were negative and displayed as zero, this remains a category-1 candidate under the supplied scope.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The 6-month intervention-minus-control alcohol energy-percentage contrast and its uncertainty/significance in both sensitivity analyses. A reader extracting -0.2 with either printed CI would include the null, while one extracting the P value would classify it as significant at .05.

**Why context does not resolve it:** This is the always-register interval-versus-P category. The source provides 95% confidence labels and a P value in the same contrast row, without a distinct analysis attribution that reconciles the printed readings.

**Alternatives and missing definitions:** The upper endpoint could be a rounded negative bound, or the P and CI could use different inferential constructions. These are alternatives rather than supplied explanations. Exact test implementation, denominator degrees of freedom, variance estimator and unrounded endpoint are not printed. The source does not establish that the P value belongs to an independently defined alternative contrast.

**Exact human question:** For each of the two 6-month alcohol contrasts, what are the unrounded 95% CI limits, and do the printed CI and P=.02 derive from the same mixed-model contrast and inferential construction?

### F-ST1-202

**Title:** Compliance percentages printed inside eFigure2 conflict with their colored bars and plotted intervals.

**Relationship:** S421. **Locations and roles:** REPORT [DOC-004 PDF p.26](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=26), eFigure2, all seven paired bars, percentage labels, 95% CI whiskers, y axis and intervention/control legend. Proposed primary relationship S_W; all relationships S_W. **Focus area:** B. **Proposed review domain:** statistical_results.

The title identifies participant percentages complying with intended dietary changes after 12 months. The legend assigns purple to intervention and gray to control; the y axis identifies percentages with 95% CI. The caption attributes P values to between-group comparisons of proportions. The exact printed percentages below are separated from approximate graph readings; no digitization or exact graphical endpoints are claimed.

| Paired bars | Printed I / C percentages | P | Approximate plotted I / C percentages from axis | Direct directional/interval observation |
|---|---|---|---|---|
| Decreased fat | 34 / 32 | .14 | 32 / 34 | Printed I>C, drawn I<C |
| Increased MUFA | 72 / 77 | <.001 | 77 / 72 | Printed I<C, drawn I>C; I label 72 is below its drawn 95% interval (visually about 75–79), C label 77 above its interval (about 70–74) |
| Increased MUFA:SFA | 79 / 86 | <.001 | 86 / 79 | Printed I<C, drawn I>C; I label 79 is below its drawn interval (about 84–88), C label 86 above its interval (about 77–81) |
| Increased fruit | 58 / 63 | <.001 | 63 / 58 | Printed I<C, drawn I>C; I label 58 is below its drawn interval (about 61–65), C label 63 above its interval (about 56–60) |
| Increased vegetables | 56 / 64 | <.001 | 64 / 56 | Printed I<C, drawn I>C; I label 56 is below its drawn interval (about 62–66), C label 64 above its interval (about 54–58) |
| Decreased meat | 60 / 62 | .08 | 62 / 60 | Printed I<C, drawn I>C |
| Decreased sugary dessert | 59 / 58 | <.001 | 68 / 60 | I label 59 is below its drawn 95% interval (about 66–70); the gray bar is also visibly near 60 rather than 58 |

**Rule and calculation:** A percentage labeling a group's bar should identify that bar's percentage and lie inside the group's displayed 95% interval. Multiple labels in this one display fail containment directly, especially MUFA, MUFA:SFA, fruit, vegetables and sugary dessert. The first six printed group contrasts also reverse the drawn order. For example MUFA labels yield I-C=72-77=-5 percentage points, whereas the purple bar is visibly above the gray bar by about +5; vegetables labels give 56-64=-8 while the bars show about +8. Half-unit ranges for those printed contrasts are [-6,-4] and [-9,-7], respectively, and cannot reverse sign. The drawn order is a direct graphical observation rather than an inferred model result.

As an additional conservative magnitude check for the dessert intervention label, enclose its visible bar/whisker region within the deliberately broad graphical range [65,71] percentage points. The printed 59% has half-unit range [58.5,59.5]. Their minimum gap is 65-59.5=5.5 percentage points; relative discrepancy 5.5/59=0.0932>0.05. This bound does not estimate the exact bar value. The point-versus-interval contradiction itself belongs to category 1 and therefore has no display-precision exemption. The P<.001 printed over the dessert pair further identifies why choosing between the tiny labeled contrast and the substantially separated bars matters; no exact P recomputation is claimed without the denominator/test definition.

**Qualifying route:** Route A, category 1 (printed point percentages outside their plotted 95% intervals); the reversals and dessert magnitude also meet the printed-value/direction category 2. Consolidated as one repeated label-to-bar association issue with every affected location retained.

**Affected result or extracted value:** Arm-specific percentages of participants achieving seven favorable dietary changes after 12 months, their intervention-minus-control direction, and the sugary-dessert contrast. Extracting the in-bar labels yields the opposite group direction for the first six categories; the dessert intervention percentage is 59% by label and approximately 68% by graphic.

**Why context does not resolve it:** The issue meets the always-register point-estimate/interval category. The same figure supplies a single arm legend and single time point, yet the percentages, bars and intervals cannot all identify the same group result. Reconstructing likely intended labels would not determine which supplied representation a data extractor should take.

**Alternatives and missing definitions:** Labels may have been associated with the other arm for the first six pairs, or a graphic/legend component may represent a different assignment. Neither a simple global reversal nor label exchange alone reconciles the dessert 59/58 labels with the drawn approximately 68/60 pair. Exact arm denominators, numeric plotted percentages and numeric CI endpoints are not printed. A label/bar population or time-point difference is not disclosed by the caption, and remains only an alternative.

**Exact human question:** Which arm-specific percentages and 95% confidence limits are intended for each of the seven 12-month compliance categories, and how should the printed labels, colored bars and arm legend be reconciled, including the sugary-dessert pair?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p.27, eFigure3 (S422), all M6/M12 nutrient box-and-whisker panels | The figure does not define the whisker rule or print numeric endpoints; these graphical distributions do not supply a contradictory numerical interval, P value or inferential conclusion. Missing that detail alone does not reproduce an in-scope inconsistency. | CONDITIONAL_OR_UNREPORTED |

## Complete pass-1 relationship records

These rows reproduce the shard inventory record mechanically; the source-reading and scientific checks are documented above and in the inventory's scope/check definitions. `RECONCILES` does not assert recovery of unreported degrees of freedom, covariance or exact test implementation. It records ordered/containing intervals, compatible printed null/significance classifications, and no reproduced method or direction conflict for the stated analysis key.

| S ID | Exact source location; quantity | Printed contrast (95% CI); P, or graphical relationship | Pass 1 result | Pass 1 status |
|---|---|---|---|---|
| S420 | DOC-004 p.25 eFigure1, four scores at baseline/M6/M12 | Baseline P .13/.42/.98/.76; all M6/M12 P<.001; colored means and 95% CI | RECONCILES: higher scores favor intervention at follow-up; individual-arm intervals are not contrast intervals | PASS_1_COMPLETE |
| S421 | DOC-004 p.26 eFigure2, seven favorable dietary changes M12 | In-bar I/C percentages 34/32,72/77,79/86,58/63,56/64,60/62,59/58; P .14,<.001,<.001,<.001,<.001,.08,<.001 | F-ST1-202: labels conflict with colored-bar direction and plotted 95% intervals | PASS_1_COMPLETE |
| S422 | DOC-004 p.27 eFigure3, 12 nutrients M6/M12 | Common baseline-SD units, I/C box-and-whisker displays; no printed numerical endpoints or tests | Directions reconcile; whisker rule not specified, no contradictory inferential claim | PASS_1_COMPLETE |
| S534 | DOC-004 p.14 eTable5 SFA M6 | -0.4 (-0.6,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S535 | DOC-004 p.14 eTable5 SFA M12 | -0.4 (-0.5,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S536 | DOC-004 p.14 eTable5 MUFA M6 | 1.2 (0.9,1.4); <.001 | RECONCILES | PASS_1_COMPLETE |
| S537 | DOC-004 p.14 eTable5 MUFA M12 | 0.9 (0.6,1.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S538 | DOC-004 p.15 eTable5 MUFA:SFA M6 | 0.3 (0.2,0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S539 | DOC-004 p.15 eTable5 MUFA:SFA M12 | 0.2 (0.2,0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S540 | DOC-004 p.15 eTable5 PUFA M6 | 0.5 (0.4,0.6); <.001 | RECONCILES | PASS_1_COMPLETE |
| S541 | DOC-004 p.15 eTable5 PUFA M12 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S542 | DOC-004 p.15 eTable5 alcohol %E M6 | -0.2 (-0.4,0); .02 | F-ST1-201: printed CI includes null, P<.05 | PASS_1_COMPLETE |
| S543 | DOC-004 p.15 eTable5 alcohol %E M12 | -0.3 (-0.4,-0.1); .01 | RECONCILES | PASS_1_COMPLETE |
| S544 | DOC-004 p.15 eTable5 fiber M6 | 24 (20,27); <.001 | RECONCILES | PASS_1_COMPLETE |
| S545 | DOC-004 p.15 eTable5 fiber M12 | 19 (16,22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S546 | DOC-004 p.15 eTable5 omega-3 M6 | 0.7 (0.5,0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S547 | DOC-004 p.15 eTable5 omega-3 M12 | 0.7 (0.5,0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S548 | DOC-004 p.15 eTable5 cholesterol M6 | -53 (-93,-13); .009 | RECONCILES | PASS_1_COMPLETE |
| S549 | DOC-004 p.15 eTable5 cholesterol M12 | -12 (-52,29); .58 | RECONCILES | PASS_1_COMPLETE |
| S550 | DOC-004 p.15 eTable5 sodium M6 | -1.2 (-1.5,-0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S551 | DOC-004 p.15 eTable5 sodium M12 | -1.3 (-1.7,-1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S552 | DOC-004 p.16 eTable6 er-MedDiet M6 | 2.1 (2,2.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S553 | DOC-004 p.16 eTable6 er-MedDiet M12 | 2.0 (1.9,2.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S554 | DOC-004 p.16 eTable6 MDS M6 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S555 | DOC-004 p.16 eTable6 MDS M12 | 0.4 (0.4,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S556 | DOC-004 p.16 eTable6 MEDAS M6 | 1.0 (0.9,1.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S557 | DOC-004 p.16 eTable6 MEDAS M12 | 0.9 (0.8,1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S558 | DOC-004 p.16 eTable6 PDQS M6 | 2.1 (1.9,2.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S559 | DOC-004 p.16 eTable6 PDQS M12 | 1.9 (1.7,2.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S560 | DOC-004 p.17 eTable7 olive oil M6 | -3 (-9,3); .27 | RECONCILES | PASS_1_COMPLETE |
| S561 | DOC-004 p.17 eTable7 olive oil M12 | -7 (-13,-2); .01 | RECONCILES | PASS_1_COMPLETE |
| S562 | DOC-004 p.17 eTable7 refined olive oil M6 | -1 (-5,4); .72 | RECONCILES | PASS_1_COMPLETE |
| S563 | DOC-004 p.17 eTable7 refined olive oil M12 | 3 (-2,7); .26 | RECONCILES | PASS_1_COMPLETE |
| S564 | DOC-004 p.17 eTable7 EVOO M6 | -3 (-9,4); .47 | RECONCILES | PASS_1_COMPLETE |
| S565 | DOC-004 p.17 eTable7 EVOO M12 | -10 (-17,-3); .004 | RECONCILES | PASS_1_COMPLETE |
| S566 | DOC-004 p.17 eTable7 nuts M6 | 43 (36,51); <.001 | RECONCILES | PASS_1_COMPLETE |
| S567 | DOC-004 p.17 eTable7 nuts M12 | 28 (20,35); <.001 | RECONCILES | PASS_1_COMPLETE |
| S568 | DOC-004 p.17 eTable7 fruits M6 | 162 (92,233); <.001 | RECONCILES | PASS_1_COMPLETE |
| S569 | DOC-004 p.17 eTable7 fruits M12 | 154 (83,224); <.001 | RECONCILES | PASS_1_COMPLETE |
| S570 | DOC-004 p.17 eTable7 vegetables M6 | 171 (124,218); <.001 | RECONCILES | PASS_1_COMPLETE |
| S571 | DOC-004 p.17 eTable7 vegetables M12 | 169 (121,216); <.001 | RECONCILES | PASS_1_COMPLETE |
| S572 | DOC-004 p.17 eTable7 cereals M6 | -82 (-108,-55); <.001 | RECONCILES | PASS_1_COMPLETE |
| S573 | DOC-004 p.17 eTable7 cereals M12 | -96 (-123,-70); <.001 | RECONCILES | PASS_1_COMPLETE |
| S574 | DOC-004 p.18 eTable7 whole grains M6 | 184 (160,208); <.001 | RECONCILES | PASS_1_COMPLETE |
| S575 | DOC-004 p.18 eTable7 whole grains M12 | 141 (117,165); <.001 | RECONCILES | PASS_1_COMPLETE |
| S576 | DOC-004 p.18 eTable7 refined grains M6 | -303 (-332,-273); <.001 | RECONCILES | PASS_1_COMPLETE |
| S577 | DOC-004 p.18 eTable7 refined grains M12 | -264 (-294,-235); <.001 | RECONCILES | PASS_1_COMPLETE |
| S578 | DOC-004 p.18 eTable7 legumes M6 | 19 (15,23); <.001 | RECONCILES | PASS_1_COMPLETE |
| S579 | DOC-004 p.18 eTable7 legumes M12 | 17 (13,22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S580 | DOC-004 p.18 eTable7 fish M6 | 55 (40,71); <.001 | RECONCILES | PASS_1_COMPLETE |
| S581 | DOC-004 p.18 eTable7 fish M12 | 63 (47,79); <.001 | RECONCILES | PASS_1_COMPLETE |
| S582 | DOC-004 p.18 eTable7 meat M6 | -25 (-42,-8); .01 | RECONCILES | PASS_1_COMPLETE |
| S583 | DOC-004 p.18 eTable7 meat M12 | -9 (-26,8); .31 | RECONCILES | PASS_1_COMPLETE |
| S584 | DOC-004 p.18 eTable7 red meat M6 | -40 (-51,-30); <.001 | RECONCILES | PASS_1_COMPLETE |
| S585 | DOC-004 p.18 eTable7 red meat M12 | -33 (-43,-22); <.001 | RECONCILES | PASS_1_COMPLETE |
| S586 | DOC-004 p.18 eTable7 processed meat M6 | -17 (-24,-10); <.001 | RECONCILES | PASS_1_COMPLETE |
| S587 | DOC-004 p.18 eTable7 processed meat M12 | -9 (-16,-1); .02 | RECONCILES | PASS_1_COMPLETE |
| S588 | DOC-004 p.18 eTable7 pastries M6 | -52 (-61,-43); <.001 | RECONCILES | PASS_1_COMPLETE |
| S589 | DOC-004 p.18 eTable7 pastries M12 | -39 (-48,-30); <.001 | RECONCILES | PASS_1_COMPLETE |
| S590 | DOC-004 p.19 eTable7 dairy M6 | 144 (83,205); <.001 | RECONCILES | PASS_1_COMPLETE |
| S591 | DOC-004 p.19 eTable7 dairy M12 | 137 (76,198); <.001 | RECONCILES | PASS_1_COMPLETE |
| S592 | DOC-004 p.19 eTable7 yogurt M6 | 95 (69,122); <.001 | RECONCILES | PASS_1_COMPLETE |
| S593 | DOC-004 p.19 eTable7 yogurt M12 | 81 (54,107); <.001 | RECONCILES | PASS_1_COMPLETE |
| S594 | DOC-004 p.19 eTable7 fermented dairy M6 | 89 (61,117); <.001 | RECONCILES | PASS_1_COMPLETE |
| S595 | DOC-004 p.19 eTable7 fermented dairy M12 | 76 (49,104); <.001 | RECONCILES | PASS_1_COMPLETE |
| S596 | DOC-004 p.19 eTable7 low-fat dairy M6 | 228 (170,285); <.001 | RECONCILES | PASS_1_COMPLETE |
| S597 | DOC-004 p.19 eTable7 low-fat dairy M12 | 234 (177,292); <.001 | RECONCILES | PASS_1_COMPLETE |
| S598 | DOC-004 p.19 eTable7 whole-fat dairy M6 | -49 (-78,-20); .001 | RECONCILES | PASS_1_COMPLETE |
| S599 | DOC-004 p.19 eTable7 whole-fat dairy M12 | -44 (-72,-15); .003 | RECONCILES | PASS_1_COMPLETE |
| S600 | DOC-004 p.19 eTable7 alcohol g/week M6 | -6 (-10,-3); .001 | RECONCILES | PASS_1_COMPLETE |
| S601 | DOC-004 p.19 eTable7 alcohol g/week M12 | -7 (-10,-3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S602 | DOC-004 p.19 eTable7 red wine M6 | -1 (-3,1); .36 | RECONCILES | PASS_1_COMPLETE |
| S603 | DOC-004 p.19 eTable7 red wine M12 | -1 (-3,1); .36 | RECONCILES | PASS_1_COMPLETE |
| S604 | DOC-004 p.21 eTable8 energy M6 | -85 (-108,-61); <.001 | RECONCILES | PASS_1_COMPLETE |
| S605 | DOC-004 p.21 eTable8 energy M12 | -88 (-111,-64); <.001 | RECONCILES | PASS_1_COMPLETE |
| S606 | DOC-004 p.21 eTable8 protein M6 | 0.9 (0.8,1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S607 | DOC-004 p.21 eTable8 protein M12 | 0.9 (0.8,1.1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S608 | DOC-004 p.21 eTable8 carbohydrate M6 | -1.3 (-1.6,-1); <.001 | RECONCILES | PASS_1_COMPLETE |
| S609 | DOC-004 p.21 eTable8 carbohydrate M12 | -1.2 (-1.5,-0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S610 | DOC-004 p.21 eTable8 fat M6 | 0.6 (0.3,0.9); <.001 | RECONCILES | PASS_1_COMPLETE |
| S611 | DOC-004 p.21 eTable8 fat M12 | 0.4 (0.1,0.8); .006 | RECONCILES | PASS_1_COMPLETE |
| S612 | DOC-004 p.21 eTable8 SFA M6 | -0.4 (-0.5,-0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S613 | DOC-004 p.21 eTable8 SFA M12 | -0.3 (-0.4,-0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S614 | DOC-004 p.21 eTable8 MUFA M6 | 1.0 (0.8,1.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S615 | DOC-004 p.21 eTable8 MUFA M12 | 0.7 (0.5,1.0); <.001 | RECONCILES | PASS_1_COMPLETE |
| S616 | DOC-004 p.22 eTable8 MUFA:SFA M6 | 0.2 (0.2,0.3); <.001 | RECONCILES | PASS_1_COMPLETE |
| S617 | DOC-004 p.22 eTable8 MUFA:SFA M12 | 0.2 (0.1,0.2); <.001 | RECONCILES | PASS_1_COMPLETE |
| S618 | DOC-004 p.22 eTable8 PUFA M6 | 0.5 (0.4,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S619 | DOC-004 p.22 eTable8 PUFA M12 | 0.4 (0.3,0.5); <.001 | RECONCILES | PASS_1_COMPLETE |
| S620 | DOC-004 p.22 eTable8 alcohol %E M6 | -0.2 (-0.3,0); .02 | F-ST1-201: printed CI includes null, P<.05 | PASS_1_COMPLETE |
| S621 | DOC-004 p.22 eTable8 alcohol %E M12 | -0.2 (-0.3,-0.1); .01 | RECONCILES | PASS_1_COMPLETE |
| S622 | DOC-004 p.22 eTable8 fiber M6 | 21 (18,24); <.001 | RECONCILES | PASS_1_COMPLETE |
| S623 | DOC-004 p.22 eTable8 fiber M12 | 16 (13,19); <.001 | RECONCILES | PASS_1_COMPLETE |
| S624 | DOC-004 p.22 eTable8 omega-3 M6 | 0.6 (0.4,0.7); <.001 | RECONCILES | PASS_1_COMPLETE |
| S625 | DOC-004 p.22 eTable8 omega-3 M12 | 0.6 (0.4,0.7); <.001 | RECONCILES | PASS_1_COMPLETE |
| S626 | DOC-004 p.22 eTable8 cholesterol M6 | -44 (-79,-8); .02 | RECONCILES | PASS_1_COMPLETE |
| S627 | DOC-004 p.22 eTable8 cholesterol M12 | -6 (-41,30); .75 | RECONCILES | PASS_1_COMPLETE |
| S628 | DOC-004 p.22 eTable8 sodium M6 | -1.1 (-1.4,-0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S629 | DOC-004 p.22 eTable8 sodium M12 | -1.1 (-1.4,-0.8); <.001 | RECONCILES | PASS_1_COMPLETE |
| S630 | DOC-004 p.23 eTable9 weight M12, MI / completers | -2.9 (-3.2,-2.6),<.001 / -3.1 (-3.4,-2.7),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S631 | DOC-004 p.23 eTable9 waist M12, MI / completers | -3.3 (-3.6,-2.9),<.001 / -3.3 (-3.7,-3.0),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S632 | DOC-004 p.23 eTable9 BMI M12, MI / completers | -1.1 (-1.2,-1.0),<.001 / -1.1 (-1.3,-1.0),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S633 | DOC-004 p.23 eTable9 cholesterol M12, MI / completers | -1.1 (-2.9,0.7),.23 / -1.1 (-2.8,0.7),.24 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S634 | DOC-004 p.23 eTable9 LDL M12, MI / completers | -0.6 (-2.2,1.0),.48 / -0.6 (-2.2,1.0),.45 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S635 | DOC-004 p.23 eTable9 HDL M12, MI / completers | 1.1 (0.7,1.6),<.001 / 1.3 (0.8,1.7),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S636 | DOC-004 p.24 eTable9 nonHDL M12, MI / completers | -1.9 (-3.6,-0.3),.02 / -2.5 (-4.2,-0.8),.004 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S637 | DOC-004 p.24 eTable9 cholesterol:HDL M12, MI / completers | -0.1 (-0.2,-0.1),<.001 / -0.1 (-0.2,-0.1),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S638 | DOC-004 p.24 eTable9 triglycerides M12, MI / completers | -9.9 (-13.6,-6.3),<.001 / -10.4 (-14,-6.9),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S639 | DOC-004 p.24 eTable9 SBP M12, MI / completers | -1.9 (-2.7,-1.1),<.001 / -1.7 (-2.6,-0.9),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
| S640 | DOC-004 p.24 eTable9 DBP M12, MI / completers | -1 (-1.4,-0.5),<.001 / -1.0 (-1.5,-0.6),<.001 | RECONCILES in both analyses | PASS_1_COMPLETE |
