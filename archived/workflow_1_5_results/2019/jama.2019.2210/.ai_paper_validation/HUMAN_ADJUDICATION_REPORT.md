# Human Adjudication Report

## Scope and method

Four supplied PDFs were inventoried. The scientific audit covered the main article, PDF pages 1–8 (page 9 was administrative/rights only), and the results supplement, pages 1–41. The protocol/SAP and data-sharing supplement were **Not Audited by Design** except for the mandatory document-level rights screen.

Native PDF text was adequate on every selected page. The required OCR selector recorded `unavailable`, but no page required OCR. The workflow retained five critic-accepted issues. No additional participant-flow, arithmetic, or CI–P reporting inconsistency was retained within the supplied documents and reviewed scope.

## Scientific issues

### 1. Table 2 HR-direction footnote reverses the stated treatment interpretation

- **Category / severity:** Statistical reporting inconsistency / **Major**
- **Issue statement:** Table 2 states that an HR greater than 1 for vitamin D indicates a decreased outcome probability, reversing the direction shown by the article's own narrative and event results.
- **Reported item:** `DOC-JAMA-2019-2210-MAIN`, `jama_urashima_2019_oi_190023.pdf`, PDF page 7, journal page 1367, Table 2, footnote a: “Hazard ratio (HR) values greater than 1 indicate that vitamin D supplementation was associated with a decreased probability of the outcome.”
- **Comparator items:**
  - Same document, PDF page 6, Results, competing-risk paragraph: relapse incidence was “significantly lower in the vitamin D group” with subdistribution HR `0.44` (95% CI, `0.21–0.89`).
  - Same document, PDF page 4, Effects of Vitamin D Supplementation: relapse occurred in `41/251` vitamin D participants and `36/166` placebo participants; Table 2 reports a subdistribution HR of `0.75`.
- **Reproducible check:** `41/251 = 16.3%`; `36/166 = 21.7%`. The lower vitamin D event proportion accompanies an HR below 1. The article also explicitly pairs `0.44 < 1` with lower incidence. No rounding tolerance can change whether an HR is above or below 1.
- **Bounded impact:** The footnote can invert a reader's interpretation of every HR and subdistribution HR in Table 2; the numerical estimates and confidence intervals themselves are unchanged.
- **Human verification:**
  1. Confirm the treatment/reference order in the Table 2 analysis output or statistical code.
  2. Confirm the page-6 narrative associates HR `0.44` with lower vitamin D incidence.
  3. If the contrast is vitamin D versus placebo, confirm that the footnote should assign decreased outcome probability to HR **less than 1**.

### 2. Table 1 does not disclose the locus-specific denominators used for SNP percentages

- **Category / severity:** Presentation inconsistency / **Minor**
- **Issue statement:** SNP percentages are displayed under treatment-arm totals of `n=251` and `n=166`, but are calculated from smaller locus-specific denominators that are not stated or explained.
- **Reported item:** `DOC-JAMA-2019-2210-MAIN`, `jama_urashima_2019_oi_190023.pdf`, PDF page 5, journal page 1365, Table 1, SNP rows, column headings, and footnote a. The headings state Vitamin D `(n = 251)` and Placebo `(n = 166)`. BsmI values are vitamin D `14 (6)`, `42 (18)`, `175 (76)` and placebo `8 (5)`, `23 (15)`, `119 (79)`. Footnote a only says percentages may not sum to 100% because of rounding.
- **Reproducible check:**
  - Vitamin D locus denominator: `14+42+175=231`, not 251. With 231, the percentages are `6.1%`, `18.2%`, and `75.8%`, reproducing `6%`, `18%`, and `76%`. With 251, they would round to `6%`, `17%`, and `70%`.
  - Placebo locus denominator: `8+23+119=150`, not 166. With 150, the percentages are `5.3%`, `15.3%`, and `79.3%`, reproducing `5%`, `15%`, and `79%`.
  - Nearest-whole-percent tolerance is ±0.5 percentage point. The issue is the undisclosed denominator, not rounding.
- **Bounded impact:** The genotype counts remain recoverable, but readers cannot identify the percentage denominator or locus-specific missingness without reconstructing each locus.
- **Human verification:**
  1. Confirm the Table 1 arm headings, BsmI counts, and percentages.
  2. Sum the three BsmI genotype counts within each arm.
  3. Recalculate percentages using both the locus sums and the arm totals.
  4. Confirm whether the table should state locus-specific denominators or add a missing-genotype footnote.

### 3. eFigure 5B incorrectly calls the greater-than-65 subgroup “older than median”

- **Category / severity:** Cross-document inconsistency / **Minor**
- **Issue statement:** eFigure 5B equates age greater than 65 years with “older than median,” although the main article reports a median age of 66 years.
- **Reported item:** `DOC-JAMA-2019-2210-SUPP-RESULTS`, `joi190023supp2_prod.pdf`, PDF page 31, eFigure 5B caption: “Post hoc subgroup analysis of older than median (> 65 years of age).”
- **Comparator items:** `DOC-JAMA-2019-2210-MAIN`, `jama_urashima_2019_oi_190023.pdf`, PDF page 4, journal page 1364, Study Population: “The median age was 66 years”; PDF page 5, Table 1 age categories.
- **Reproducible check:** Vitamin D counts through age 65 are `51+55=106`, and placebo counts are `50+41=91`, exactly matching eFigure 5A. Complements are `251-106=145` and `166-91=75`, exactly matching eFigure 5B and confirming that its boundary is greater than 65. Participants aged 66 equal, rather than exceed, a reported median of 66. No rounding tolerance applies to the stated integer-year threshold.
- **Bounded impact:** The analyzed boundary and numerical results remain identifiable; only the caption's median-relative description is wrong.
- **Human verification:**
  1. Confirm the reported overall median age of 66 years.
  2. Reconcile the Table 1 age-category counts with the time-zero counts in eFigure 5A–B.
  3. Confirm whether the intended split was greater than 65 by design; if so, relabel it without equating it to “older than median,” or document the intended convention.

### 4. eFigure 3G–I label the main article's Cdx2 strata as CDK2

- **Category / severity:** Cross-document inconsistency / **Minor**
- **Issue statement:** The supplement identifies three SNP subgroup panels as CDK2, while the main article identifies the same count-defined strata as CDX2/Cdx2.
- **Reported items:** `DOC-JAMA-2019-2210-SUPP-RESULTS`, `joi190023supp2_prod.pdf`: PDF page 13, eFigure 3G, “CDK2 GG,” time-zero placebo/vitamin D counts `49/89`; PDF page 14, eFigure 3H, “CDK2 GA,” counts `77/103`; PDF page 15, eFigure 3I, “CDK2 AA,” counts `24/38`.
- **Comparator items:** `DOC-JAMA-2019-2210-MAIN`, `jama_urashima_2019_oi_190023.pdf`, PDF page 3, SNP Analyses: “CDX2 (rs11568820)”; PDF page 5, Table 1, Cdx2 GG/GA/AA rows: vitamin D `89/103/38`, placebo `49/77/24`.
- **Reproducible check:** GG matches `49=49` and `89=89`; GA matches `77=77` and `103=103`; AA matches `24=24` and `38=38`. All `6/6` arm-by-genotype starting counts match exactly; the labels differ as CDK2 versus CDX2/Cdx2. Integer tolerance is zero.
- **Bounded impact:** The inconsistency affects the SNP identity attached to three panels; it does not establish an error in the plotted HRs, confidence intervals, or counts.
- **Human verification:**
  1. Confirm the Methods SNP identifier and Table 1 Cdx2 counts.
  2. Confirm the eFigure 3G–I labels and time-zero counts.
  3. Check the analysis dataset or figure-generation source to determine whether the three supplement labels should read CDX2/Cdx2.

### 5. Figure 3 says panel C risk numbers are absent although they are printed

- **Category / severity:** Presentation inconsistency / **Minor**
- **Issue statement:** Figure 3's caption says panel C numbers at risk are not given, but panel C visibly provides complete placebo and vitamin D risk rows.
- **Reported item:** `DOC-JAMA-2019-2210-MAIN`, `jama_urashima_2019_oi_190023.pdf`, PDF page 7, journal page 1367, Figure 3 caption: “Numbers at risk for panel C are not given because of weighting.”
- **Comparator item:** Same page and figure, panel C prints placebo `90, 88, 70, 51, 34, 22, 11` and vitamin D `142, 139, 115, 88, 61, 41, 20`.
- **Reproducible check:** Two treatment rows × seven time points = `14` visible numeric risk entries, directly contradicting “not given.” No rounding tolerance applies.
- **Bounded impact:** The contradiction does not change the graph or estimates, but creates uncertainty about whether the printed counts should be used.
- **Human verification:**
  1. Read the Figure 3 caption sentence and inspect panel C directly below it.
  2. Determine from the production figure source whether the rows are intended numbers at risk.
  3. Correct either the caption or the displayed rows to resolve the contradiction.

## Rejected candidate audit trail

The candidate that eFigure 7A–C captions omit “post hoc” was rejected by the critic. The supplement contents explicitly title eFigure 7 as post hoc, the main article places cancer-site analyses in the post-hoc sequence, and the individual captions do not make a conflicting prespecified claim.

## AI Training Restriction Summary

This separate compliance screen is not a scientific issue category, is not legal advice, and is outside the scientific-issue limits. The supplied language consists of general copyright, intellectual-property, or data-access terms rather than terms addressing AI training, fine-tuning, or model improvement. Silence is not permission.

| Document | Status | Exact supplied-file evidence | Human Compliance Review |
|---|---|---|---|
| `DOC-JAMA-2019-2210-MAIN` / `jama_urashima_2019_oi_190023.pdf` | No AI Training Restriction Located in Provided Materials | PDF pages 1–9, footer: “© 2019 American Medical Association. All rights reserved.” | No |
| `DOC-JAMA-2019-2210-SUPP-PROTOCOL-SAP` / `joi190023supp1_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF page 16, “Attribution of intellectual property rights”: “If intellectual property rights such as patent rights become relevant, such rights will be attributable to the investigator.” Parallel wording on PDF page 33 attributes such rights to “the investigators.” | No |
| `DOC-JAMA-2019-2210-SUPP-RESULTS` / `joi190023supp2_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF page 1 footer, repeated on pages 1–41: “© 2019 American Medical Association. All rights reserved.” | No |
| `DOC-JAMA-2019-2210-SUPP-DATA-SHARING` / `joi190023supp3_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF page 1: “Who can access the data: researchers whose proposed use of the data”; “Types of analyses: for a specified purpose”; “Mechanisms of data availability: after approval of a proposal”; “Any additional restrictions: not particular for now.” | No |

No explicit or conditional AI-training restriction was located in the four supplied PDFs, so the project-defined Human Compliance Review trigger was not activated. This finding does not infer permission from the absence of AI-specific language.

## Submission status

**Submitted for Human Adjudication.** A human reviewer should perform the numbered checks above and record a confirm, resolve, or reject decision for each issue.
