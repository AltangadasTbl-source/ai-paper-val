# Figure and Participant-Flow Check

- **Checker:** figure_flow_checker
- **Scope:** DOC-001 main article, PDF pp. 3, 6, 9-10 (Figures 1-4), and DOC-004 results supplement, PDF pp. 25-27 (eFigures 1-3). Protocol, SAP, and administrative pages were not inspected.
- **Visual method:** direct inspection of source-PDF renders plus the retained page-level text. The available OCR backend is `rapidocr-cpu`; no GPU/CUDA OCR was used or claimed.
- **Result:** 2 presentation candidates; 0 participant-flow candidates. These are candidates for verification, not determinations that either referenced display is erroneous.

## Candidate FFC-01 — Main-text statement conflicts with eFigure 2’s labelled group percentages

- **Category / severity:** Presentation inconsistency / Moderate.
- **Issue statement:** The main text says that the intervention group had a *significantly higher* proportion achieving favourable dietary changes for “most comparisons,” but the explicitly referenced eFigure 2 labels the control percentage as higher for five of seven dietary changes, including four comparisons marked `p<0.001`.
- **Reported main-text item:** DOC-001, `jama_saynorea_2019_oi_190106_1635377898.43062.pdf`, PDF p. 8 (journal p. 1493), *Energy Intake and Nutrients*: “**The proportion of participants achieving any favorable dietary changes was significantly higher in the intervention than in the control group for most comparisons (eFigure 2 in Supplement 3).**”
- **Definition supplied by the main article:** DOC-001, PDF p. 4 (journal p. 1489), *Outcomes*: “any favorable dietary changes (ie, **any change in the desirable direction**).”
- **Comparator visual item:** DOC-004, `joi190106supp3_prod_1635377898.49725.pdf`, PDF p. 26, Supplemental eFigure 2, visible bar labels and legend. Purple is labelled **Intervention** and gray **Control**. The caption states that displayed p values compare the group proportions.

  | eFigure 2 change | Intervention | Control | Displayed P | Which visible percentage is higher |
  |---|---:|---:|---:|---|
  | ↓ Fat | 34% | 32% | .14 | Intervention |
  | ↑ MUFA | 72% | 77% | <.001 | Control |
  | ↑ MUFA:SFA | 79% | 86% | <.001 | Control |
  | ↑ Fruit | 58% | 63% | <.001 | Control |
  | ↑ Vegetables | 56% | 64% | <.001 | Control |
  | ↓ Meat | 60% | 62% | .08 | Control |
  | ↓ Sugary dessert | 59% | 58% | <.001 | Intervention |

- **Reproducible comparison:** From the seven visible group pairs, intervention is numerically higher in `2/7` pairs (fat and sugary dessert), not a majority. It is higher with a displayed significant p value in `1/7` pairs (sugary dessert), whereas control is higher with `p<0.001` in `4/7` pairs (MUFA, MUFA:SFA, fruit, vegetables). Thus the figure’s labelled values do not support the cited statement that intervention proportions were significantly higher for “most comparisons.”
- **Bounded impact:** The discrepancy affects the qualitative description of the direction and frequency of the eFigure 2 proportion comparisons. It does not, by itself, establish that the continuous nutrient-change estimates or the intervention effect are incorrect.
- **Human verification steps:**
  1. Confirm the purple/gray legend and the seven printed percentages on DOC-004 PDF p. 26; the issue is confirmed if they remain intervention/control as transcribed above.
  2. Confirm the quoted DOC-001 PDF-p. 8 sentence and the DOC-001 PDF-p. 4 definition of “any favorable” change.
  3. Check the figure-generation data or author source to determine whether the bar labels/legend or the narrative sentence should be corrected. A corrected group assignment or a different specified denominator/rule that changes these labelled comparisons would resolve the issue.

## Candidate FFC-02 — eFigure 3 does not explain its box-and-whisker marks

- **Category / severity:** Presentation inconsistency / Low.
- **Issue statement:** Supplemental eFigure 3 presents box-and-whisker-shaped marks for nutritional changes but supplies no caption/legend explanation of the middle line, box, or whiskers, leaving the plotted summaries undefined within that figure.
- **Affected visual:** DOC-004, `joi190106supp3_prod_1635377898.49725.pdf`, PDF p. 27, Supplemental eFigure 3. The visible plot contains, for each group and time point, a rectangle with a central vertical line and horizontal whiskers; the page text/caption only expands abbreviations (CHO, SFA, MUFA, PUFA, w-3).
- **Direct comparator:** DOC-001, `jama_saynorea_2019_oi_190106_1635377898.43062.pdf`, PDF p. 9 (journal p. 1494), Figure 3. It uses the same horizontal box-and-whisker visual construction and explicitly states: middle line = within-group median change; box = IQR; whiskers = most extreme observed values within 1.5 × IQR of the nearer quartile.
- **Reproducible comparison:** Read the entirety of DOC-004 PDF-p. 27 title/caption/footnote: it identifies standardized units and abbreviations but contains no statement corresponding to any of the three mark definitions supplied at DOC-001 PDF p. 9. Therefore an eFigure 3 reader cannot determine from the eFigure itself whether its marks are medians/IQR/whiskers, means/CI, or another summary.
- **Bounded impact:** This limits interpretation of the eFigure 3 distributions only; it does not change the numerical results in eTables 5 and 8.
- **Human verification steps:**
  1. Inspect the full PDF-p. 27 caption and figure for a mark-definition key; confirmation requires that none is present.
  2. Compare the visual elements against DOC-001 PDF-p. 9 Figure 3 and its explicit legend.
  3. Check author figure-generation materials; a caption specifying the plotted statistic, spread, and whisker rule resolves the issue.

## No participant-flow candidate located

DOC-001 Figure 1, PDF p. 3, reconciles arithmetically at every displayed branch: `9677 − 2803 = 6874`; `3406 − 134 = 3272` and `3468 − 157 = 3311`; individual-plus-couple randomization totals are `2892 + 380 = 3272` and `2909 + 402 = 3311`; and the displayed completer counts equal main-analysis counts minus unavailable nutritional information at the stated follow-up (`3272 − 410 = 2862`, `3311 − 428 = 2883`, `3272 − 439 = 2833`, `3311 − 368 = 2943`). No flow contradiction is reported.
