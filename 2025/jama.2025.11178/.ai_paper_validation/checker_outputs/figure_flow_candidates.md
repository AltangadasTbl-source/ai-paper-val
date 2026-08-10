# Figure, Flow, and Presentation Check: Local Candidates

- Package: `jama.2025.11178`
- Audited sources: DOC-001-MAIN (main article pp. 1-14), DOC-005-RESULTS (results supplement pp. 3-18; p. 2 context only), and directly relevant DOC-006-XLSX cells.
- Excluded by design: protocol, SAP, TIDieR/intervention-description, and administrative content.
- Method: inspected retained page images for main Figures 1-2 and Tables 1-3; supplement eFigures 1-2 and eTables 1-11; compared visible labels/counts with nearby text, the evidence maps, and directly relevant workbook cells.
- Result: 6 document-verifiable local candidates. No candidate issue was found in main Figure 1, main Figure 2, supplement eFigure 1, or the plotted patterns in supplement eFigure 2.

## Candidate 1 - Follow-up-pattern categories overcount the randomized population by 3

- **Category:** Participant flow inconsistency / Cross-document inconsistency
- **Location:** DOC-005-RESULTS, `joi250046supp4_prod_1755300121.15587.pdf`, PDF p. 7, eTable 1 ("Primary outcome follow-up rates and patterns overall and by arm"); corroborating locations: DOC-001-MAIN, Figure 1, PDF p. 5 / JAMA p. 596; DOC-006-XLSX, `joi250046supp5_prod_1755300121.16087.xlsx`, sheet `eTable 3`, cells B2:E3.
- **Visible/source evidence:**
  - eTable 1 reports randomized N=2331 and mutually exclusive pattern rows of no follow-up=295, one observed follow-up=188, two observed follow-ups=283, and three observed follow-ups=1568.
  - These pattern rows total 2334, not 2331: `295 + 188 + 283 + 1568 = 2334`.
  - The "at least 1 follow-up" component rows also total 2039 rather than the reported 2036: `188 + 283 + 1568 = 2039`.
  - By arm, usual care reconciles (`74 + 64 + 99 + 540 = 777`), but painTRAINER totals 777 against randomized N=776 and health coach totals 780 against randomized N=778.
  - Main Figure 1 reports the internally reconciling any-follow-up counts of 643/776 for painTRAINER, 690/778 for health coach, and 703/777 for usual care.
  - The workbook independently reports overall N=2331, missing all 3 follow-ups N=295, missing 1 or 2 follow-ups N=468, and all observed N=1568. Thus its incomplete-but-not-all-missing group is 468, whereas eTable 1's one/two rows total 471 (`188 + 283`).
- **Reasoning:** The follow-up-pattern rows are presented as exhaustive categories. They exceed both the randomized denominator and the separately reported at-least-one-follow-up total by 3; the overcount is localized to painTRAINER (+1) and health coach (+2). The workbook preserves the expected overall partition (`295 + 468 + 1568 = 2331`).
- **Verification instruction:** Reconcile participant-level follow-up-pattern coding by arm. Check whether one or more of the eTable 1 values 77, 103, 464 (painTRAINER) and 47, 81, 564 (health coach) were transcribed incorrectly, then confirm the corrected rows sum to 643 and 690 and the full table sums to 2331.

## Candidate 2 - eTable 8's pre-enhancement header labels all 454 randomized participants as 3-month observations despite only 366 having any follow-up

- **Category:** Participant flow inconsistency / Presentation inconsistency
- **Location:** DOC-005-RESULTS, `joi250046supp4_prod_1755300121.15587.pdf`, PDF p. 14, eTable 8, first subset header ("Randomized prior to 8/9/2021").
- **Visible evidence:** The header states: "N=454; 366 with at least 1 follow-up; PT=149, HC=153, UC=152 at 3-months." The three stated 3-month arm counts sum to all 454 randomized participants: `149 + 153 + 152 = 454`.
- **Reasoning:** A 3-month observed count of 454 cannot coexist with only 366 participants having at least one of the 3-, 6-, or 12-month follow-ups. The arm values may instead be randomized arm sizes, in which case the phrase "at 3-months" is attached to the wrong counts; as printed, the header is internally impossible.
- **Verification instruction:** Check the subset's actual 3-month observed denominators. Either replace 149/153/152 with the correct 3-month counts or relabel them explicitly as randomized arm sizes.

## Candidate 3 - The missing-data text points to the wrong supplementary figure

- **Category:** Presentation inconsistency
- **Location:** DOC-005-RESULTS, `joi250046supp4_prod_1755300121.15587.pdf`, PDF p. 6, final sentence; comparison locations: PDF p. 3, eFigure 1, and PDF p. 10, eFigure 2.
- **Visible evidence:** Page 6 says, "eTable 6 and eFigure 1 provide summaries of the predicted probabilities and corresponding weights." However:
  - eFigure 1 on p. 3 is the histogram of completed intervention sessions for painTRAINER and virtual health coach.
  - eFigure 2 on p. 10 is titled "Histogram of estimated probabilities and weights."
- **Reasoning:** The cited subject matter matches eFigure 2, not eFigure 1. The cross-reference sends readers to an unrelated adherence figure.
- **Verification instruction:** Change "eFigure 1" to "eFigure 2" in the final sentence on supplement p. 6.

## Candidate 4 - eTable 9's title calls the relative risks adjusted although the section and footnote say they are unadjusted

- **Category:** Presentation inconsistency
- **Location:** DOC-005-RESULTS, `joi250046supp4_prod_1755300121.15587.pdf`, PDF p. 15, "ADDITIONAL UNADJUSTED DATA AND ANALYSES," eTable 9 title and footnote b.
- **Visible evidence:**
  - The lead-in says these are "unadjusted analyses with no adjustment, weighting or imputation."
  - The eTable 9 title says "unadjusted percentage ... and **adjusted relative risk** between group comparisons."
  - Footnote b says the RRs were calculated "without adjustment."
- **Reasoning:** The title's "adjusted relative risk" directly contradicts both the section description and the table's own methodological footnote.
- **Verification instruction:** Confirm the model specification and change the title to "unadjusted relative risk" if footnote b and the section lead-in are correct.

## Candidate 5 - eTable 11's printed treatment-group columns are incompatible with its pairwise comparisons and nearby description

- **Category:** Presentation inconsistency
- **Location:** DOC-005-RESULTS, `joi250046supp4_prod_1755300121.15587.pdf`, PDF p. 17, eTable 11 header and rows; nearby description on PDF p. 15.
- **Visible evidence:**
  - Page 15 says eTable 11 provides "unadjusted mean secondary outcomes."
  - eTable 11 instead labels its three group columns "Raw Score Median (25%-tile, 75%tile)" in the order painTRAINER, health coach, usual care plus.
  - Pain severity at 3 months is printed as PT 5.1, HC 4.6, UC 4.6, while the adjacent comparisons are PT vs UC -0.5, HC vs UC -0.5, and HC vs PT 0.0. The printed group order would suggest the opposite direction for PT vs UC, whereas the comparisons align if the three group columns are read as UC, PT, HC.
  - Social-role functioning at 3 months is printed as PT 43.4, HC 44.6, UC 44.8, while comparisons are PT vs UC +1.2, HC vs UC +1.4, and HC vs PT +0.2. Again, those comparisons align with a UC, PT, HC column order, not the printed PT, HC, UC order.
  - The same directional pattern recurs across pain intensity, interference, physical functioning, and both PGIC outcomes.
- **Reasoning:** The discrepancy is systematic across all outcome blocks, not an isolated rounding effect. The nearby prose also calls the group summaries means, while the table calls them medians/IQRs. At minimum, the group-order and summary-statistic labels cannot all be correct as printed.
- **Verification instruction:** Compare eTable 11 against the source analysis output. Verify whether the three raw-score columns should be labeled usual care plus, painTRAINER, health coach and whether their parenthetical limits are 95% CIs rather than IQRs; correct the header and group labels accordingly.

## Candidate 6 - eTable 8 attaches the omnibus-P footnote marker to the relative-risk header

- **Category:** Presentation inconsistency
- **Location:** DOC-005-RESULTS, `joi250046supp4_prod_1755300121.15587.pdf`, PDF p. 14, eTable 8 column headers and footnotes b-c.
- **Visible evidence:** The header reads "Adjusted Relative Risk" with superscript c, followed by "(95% CI)" with superscript b. Footnote b describes the adjusted percentages and adjusted RRs; footnote c defines the omnibus P value and its multiple-comparison rule. The P-value column also carries superscript c, where that marker is appropriate.
- **Reasoning:** Superscript c on "Adjusted Relative Risk" directs readers to a footnote about the omnibus P value rather than RR estimation. Footnote b is the RR-method footnote.
- **Verification instruction:** Remove the superscript c from "Adjusted Relative Risk" (or replace it with b if a marker is intended) while retaining c on the P-value column.

