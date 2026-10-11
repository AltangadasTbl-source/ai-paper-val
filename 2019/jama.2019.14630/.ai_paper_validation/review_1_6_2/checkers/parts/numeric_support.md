# Numeric consistency checker — support shard

Status: COMPLETE. Scope: DOC-003 SAP numerical screening and recruitment group N400; DOC-004 results groups N401, N402, N403 and every baseline locator N430–N540; DOC-005 ancillary REPORT p.1 (no numerical result). The assigned inventory has 115 groups. New locator N541 extends the inventory to the numerical representations in DOC-004 p.26 eFigure2, cross-referenced to S421. Total reviewed inventory: 116 groups. Main article and protocol numerical relationships and inferential checks are assigned elsewhere. No old scientific conclusions or web evidence were consulted.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Read the current support summary and baseline locator rows, complete source-identical SAP and results layout texts, and data-sharing text. Independently inspected retained source renders of SAP p.15 and results pp.25–27. Confirmed the red-wine entry against a fresh direct PDF p.7 render. Rendering command: `pdftoppm -f 7 -l 7 -singlefile -scale-to 2000 -png joi190106supp3_prod_1635377898.49725.pdf .ai_paper_validation/review_1_6_2/preprocessing/numeric_support/results-p7`; engine Poppler pdftoppm 26.01.0, CPU. Derivative: preprocessing/numeric_support/results-p7.png. Retained figures: `.ai_paper_validation/review_1_6_1/preprocessing/sap-results-sap-p15.png`, `.ai_paper_validation/review_1_5_1/preprocessing/DOC-004_visual-25.png`, `DOC-004_visual-26.png`, `DOC-004_visual-27.png`; retained rendering version is unspecified where not recorded by the asset curator.

## Findings

### F-NUM-101

**Title:** Red-wine baseline median exceeds its displayed upper quartile.

**Relationship:** N451. **Compared location and role:** REPORT DOC-004 PDF p.7, eTable2 continuation, Red wine (g/week), Intervention group N=3272, Baseline median (IQR). [Exact source page](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=7).

**Printed inputs:** intervention baseline `33 (0, 29)`; the row is explicitly labeled median (IQR), and the footnote repeats that baseline data are median (IQR). Control is `4 (0,29)` but is not required for the within-row contradiction.

**Rule and calculation:** For one distribution, Q1 <= median <= Q3. The displayed intervention median is 33 and Q3 is 29. Half-unit input intervals are median [32.5,33.5] and Q3 [28.5,29.5]; Q1 is [−0.5,0.5], restricted to nonnegative intake if needed. The largest possible Q3 is 29.5, below the smallest possible median 32.5. The minimum gap is 3 g/week and the relative discrepancy is 3/33 = 0.09091 > 0.05. The compatible-median interval implied by the printed quartiles is at most [−0.5,29.5] (or [0,29.5] with nonnegative intake); it cannot overlap the printed median interval. This is not a comparison of differing sensitivity sets or a test inference.

**Focus area:** A (displayed descriptive quantities) and B (numerical ordering). **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The intervention group's baseline red-wine median in g/week and its interquartile limits, any of which a data extractor may retain from this table.

**Why context does not resolve it:** Both the row and the footnote identify median and interquartile limits; neither identifies which of 33 or 29 should be used if the two do not reconcile. A reader cannot choose the intended median or upper quartile from the same display. It changes a printed numerical quantity rather than a resolvable symbol or wording.

**Alternatives and missing definition:** The median or upper quartile may be a substituted number, or the three values may have been taken from different descriptive calculations. Neither explanation is established by the supplied display; no alternative statistic is specified. Other baseline copies are not used to propose a replacement.

**Exact human question:** Which intervention-group baseline median and quartiles for red-wine intake correspond to this analysis, and how should the printed `33 (0,29)` be understood?

### F-NUM-102

**Title:** eFigure2 percentage labels do not reconcile with the corresponding plotted bars.

**Relationship:** N541, cross-reference S421. **Compared locations and roles:** REPORT DOC-004 PDF p.26 eFigure2, percentage labels inside each purple Intervention and gray Control bar versus those bars' top heights against the percentage axis. [Exact source page](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=26). One repeated pattern is emitted, with every affected category preserved.

**Printed inputs and graphical representations:**

| Intended change | Printed Intervention / Control (%) | Visually read bar heights Intervention / Control (%) |
|---|---:|---:|
| Decreased fat | 34 / 32 | approximately 32 / 34–35 |
| Increased MUFA | 72 / 77 | approximately 77 / 72 |
| Increased MUFA:SFA | 79 / 86 | approximately 86 / 79 |
| Increased fruit | 58 / 63 | approximately 63 / 58 |
| Increased vegetables | 56 / 64 | approximately 64 / 56 |
| Decreased meat | 60 / 62 | approximately 62 / 60 |
| Decreased sugary dessert | 59 / 58 | approximately 68 / 60 |

Graphical values are axis-based visual approximations, not newly asserted exact estimates. The legend identifies the purple bars as Intervention and gray as Control; the vertical axis gives percentages and 95% CI. For MUFA, MUFA:SFA, fruit, vegetables, fat and meat, the printed label ordering reverses the corresponding bar-height ordering. The sugary-dessert intervention label is substantially below its own bar height, without a group-order reversal. Thus a simple global legend swap does not resolve the complete display.

**Rule and calculation:** The numerical annotation inside a bar and the height of that bar must refer to the same percentage unless the display names another meaning. None is named here. Printed integer percentages receive ±0.5 percentage-point intervals. Conservative visual intervals of ±1 percentage point around the approximate top are used below; these incorporate reading imprecision rather than pretending the plot prints exact top values.

| Robust example | Printed half-unit interval (%) | Conservative graphical interval (%) | Minimum gap | Relative discrepancy |
|---|---:|---:|---:|---:|
| MUFA:SFA, Intervention label 79 | [78.5,79.5] | [85,87] | 5.5 | 5.5/79 = 0.06962 |
| MUFA:SFA, Control label 86 | [85.5,86.5] | [78,80] | 5.5 | 5.5/86 = 0.06395 |
| Fruit, Intervention label 58 | [57.5,58.5] | [62,64] | 3.5 | 3.5/58 = 0.06034 |
| Fruit, Control label 63 | [62.5,63.5] | [57,59] | 3.5 | 3.5/63 = 0.05556 |
| Vegetables, Intervention label 56 | [55.5,56.5] | [63,65] | 6.5 | 6.5/56 = 0.11607 |
| Vegetables, Control label 64 | [63.5,64.5] | [55,57] | 6.5 | 6.5/64 = 0.10156 |
| Sugary dessert, Intervention label 59 | [58.5,59.5] | [67,69] | 7.5 | 7.5/59 = 0.12712 |

Each robust example remains above 0.05 after display and visual precision allowances. The smaller fat, meat and MUFA differences are retained as locations of the repeated label/bar pattern; they are not separate numerical findings. The result does not depend on reconstructing an unspecified denominator, event count, or statistical test. Statistical P-value compatibility is covered by the statistical lane.

**Focus area:** A (percentages) and B (direction across numerical and graphical representations). **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Arm-specific proportions complying with each intended dietary change at 12 months, especially MUFA:SFA, fruit, vegetables and sugary dessert. The plotted intervention advantage for several changes conflicts with the printed labels suggesting a control advantage; the sugary-dessert percentage also changes materially in magnitude.

**Why context does not resolve it:** The single legend, category captions and percentage axis give no distinct definition for the internal percentage labels. They do not identify whether the labels or the heights are the intended proportions; sugary dessert also prevents resolution by a single legend swap. A reader or data extractor may retain the printed labels or the plotted proportions with different numerical and directional readings.

**Alternatives and missing definition:** Some labels might refer to another population, time point, or denominator, or some may have been transposed across arms. The figure names only one 12-month comparison and gives no such alternative mapping. A global legend swap would not reconcile the dessert labels. No preferred representation or replacement values are proposed.

**Exact human question:** Which arm-specific 12-month percentages do the eFigure2 bar heights and internal labels represent, and what mapping reconciles their numerical and directional readings across all seven intended changes?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-004 p.3 eTable2 first column header pair | The second N=3311 column repeats Intervention; the continuation headers consistently identify it as Control, so the intended group is identifiable without changing a printed number. | TERMINOLOGY_OR_WORDING |
| DOC-004 p.10 eTable4 total olive-oil baseline | Row says mean (SD) but contains `350 (175,350)`; its table footnote explicitly identifies baseline median (IQR), and the three-number form resolves the statistic label in place. | TERMINOLOGY_OR_WORDING |
| DOC-004 pp.7,13,19 red-wine baseline copies | Baseline copies in distinct MI, completer and baseline-replacement tables show intervention medians 33,4,0 and control medians 4,4,0. The cross-location baseline-copy difference is peripheral. The independently reproduced p.7 within-row quantile issue is separately emitted as F-NUM-101. | PERIPHERAL_COMPARISON |

## Completed checks and limitations

Recruitment totals reconcile exactly: 9677−1195=8482; 706+489=1195; 8482−1232=7250; 7250−376=6874; 333+43=376; 1195+1232+376=2803; 6066+808=6874; 3052+416=3468; 3014+392=3406; 3468+3406=6874; 3052+3014=6066; 416+392=808. Couple allocation is a participant count, not 808 households.

Population/time-point sets remain distinct. MI and baseline replacement: 3272+3311=6583. Food/nutrient completers: M6 2862+2883=5745 and M12 2833+2943=5776. er-MedDiet's marked footnote instead gives M6 3030+3090=6120 and M12 2971+3095=6066. Risk completers: 2840+2946=5786. All are within the parent analysis set. Source-main N008 separately documents the 291 baseline exclusions (53 absent FFQ and238 out-of-range energy) from6874 to6583; this is corroboration only and belongs to the main numeric shard.

Reviewed all111 baseline locator groups against their complete source row values and statistic labels, including wrapped upper quartiles, SDs and all four eTable9 columns. Only N451 fails the within-row numerical ordering rule. Means of component quantities are not assumed to reproduce means of participant ratios; the MUFA:SFA and cholesterol:HDL labels are ratio quantities and do not show an effect-measure substitution. Median food groups are not summed as though they were means or disjoint quantities. Modeled changes, not crude before/after arithmetic, are explicitly identified by the source. Half-unit subtraction checks on the displayed arm change means do not yield another reproduced numerical discrepancy in the support tables; one-unit integer and0.1 decimal differences admit rounding combinations.

N401 score ranges reconcile with component counts: er-MedDiet17 one-point criteria; MDS9 one-point components; MEDAS14 one-point criteria; PDQS21 components ×2 maximum points=42. Historical MCID derivation log(.75)=−.2877 and exp(−.2877/2)=.866, printed .87 and13% reduction, reconciles within display precision. SAP body-weight/BMI/waist examples of5% give4.325kg,1.625kg/m²,5.4cm and reconcile with4.3,1.6,5.4. These reconciled checks are not excluded observations.

DOC-005 contains no quantitative result or statistical-design calculation. Figures1 and3 were checked visually for quantity labels, units, directions and graphical scope; their unprinted numerical endpoints are not invented. Limitations: exact figure top values and participant numerators/denominators are not printed in eFigure2. Its finding uses conservative visual bands and is robust in the documented categories; it does not infer exact estimates or P-value calculations. No assigned source coverage or tool gap remains.

Counts: 116 numerical relationship groups (115 assigned plus N541 extension); 2 findings; 3 excluded observations. Complete inventory: relationships/parts/numeric_support.md.
