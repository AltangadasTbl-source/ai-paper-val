# Evidence Verification Report

## Scope and verification limit

This is the single required verification stage for the 10 candidates selected by the
Coordinator. Verification was restricted to:

- DOC-001-MAIN, `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`
- DOC-006-RESULTS-SUPP, `joi240006supp5_prod_1708623115.01733.pdf`
- page-linked text and page renderings derived from those PDFs

No new issues were searched for. No external sources were used. Each candidate used no more than
two verification rounds.

## Classification summary

| Candidate | Classification | Verification rounds | Disposition |
|---|---|---:|---|
| TA-001 | **Verified** | 1 | Retain |
| TA-002 | **Verified** | 1 | Retain |
| Statistical candidate 1 | **Verified** | 1 | Retain |
| Statistical candidate 2 | **Verified** | 1 | Retain |
| Statistical candidate 3 | **Verified** | 1 | Retain |
| Statistical candidate 6 | **Uncertain** | 2 | Do not retain as a confirmed finding |
| FF-01 | **Verified** | 2 | Retain |
| FF-02 | **Verified** | 2 | Retain |
| FF-03 | **Verified** | 2 | Retain |
| FF-04 | **Rejected** | 1 | Do not retain |

Result: **8 Verified, 1 Uncertain, 1 Rejected.**

---

## Verified evidence cards

### V-01 — Main Table 1 general-anesthesia percentage does not reproduce from the displayed count and column total

- **Classification:** Verified
- **Category / severity:** Arithmetic inconsistency / Minor
- **Issue statement:** Main Table 1 reports 100 EVT patients as 59.9%, but the displayed EVT
  column total of 168 gives 59.5% to one decimal.
- **Reported source:** DOC-001-MAIN,
  `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 5, Table 1,
  column `Endovascular thrombectomy (n = 168)`, section `Additional characteristics, No. (%)`,
  row `General anesthesia used`: **`100 (59.9)`**.
- **Comparator:** The same table's EVT column header states **`n = 168`**. No footnote attached
  to this row gives a different denominator or a missing-value rule.
- **Reproducible calculation:** `100 / 168 × 100 = 59.5238%`, which rounds to **59.5%**, not
  59.9%. The displayed value is high by **0.4 percentage points**. A value of 59.9% would be
  consistent with an unstated denominator of 167 because `100 / 167 × 100 = 59.8802%`.
- **Bounded impact:** The inconsistency affects the percentage for one baseline characteristic;
  it does not show that the count of 100 or any outcome estimate is wrong. The package cannot
  distinguish a percentage error from an omitted available-case denominator.
- **Human verification steps:**
  1. Open DOC-001-MAIN PDF p. 5 and confirm the EVT header is `n = 168`.
  2. Confirm the `General anesthesia used` EVT cell is `100 (59.9)`.
  3. Recalculate `100/168 × 100` and round to one decimal.
  4. Confirm the finding if no row-specific denominator of 167 is documented; a documented
     denominator of 167 would resolve it as a denominator-presentation omission.

### V-02 — Supplement eTable 1 general-anesthesia percentage does not reproduce from the displayed as-treated total

- **Classification:** Verified
- **Category / severity:** Arithmetic inconsistency / Minor
- **Issue statement:** Supplement eTable 1 reports 100 as-treated EVT patients as 59.5%, but the
  displayed as-treated EVT total of 170 gives 58.8% to one decimal.
- **Reported source:** DOC-006-RESULTS-SUPP,
  `joi240006supp5_prod_1708623115.01733.pdf`, PDF pp. 35-36, eTable 1,
  `Endovascular thrombectomy N=170` column, `Additional characteristics` section,
  row `General Anesthesia Used`: **`100 (59.5%)`**.
- **Comparator:** eTable 1 identifies the as-treated EVT column as **`N=170`** on PDF p. 35.
  Its footnotes on pp. 36-37 do not state another denominator or a missing-value rule for general
  anesthesia.
- **Reproducible calculation:** `100 / 170 × 100 = 58.8235%`, which rounds to **58.8%**, not
  59.5%. The displayed value is high by **0.7 percentage points**. The printed 59.5% is
  reproduced by an unstated denominator of 168: `100 / 168 × 100 = 59.5238%`.
- **Bounded impact:** The inconsistency is confined to one baseline percentage. It does not
  establish whether the count, percentage, or undocumented nonmissing denominator is the item
  requiring correction.
- **Human verification steps:**
  1. Open DOC-006-RESULTS-SUPP PDF p. 35 and confirm the EVT header is `N=170`.
  2. On PDF p. 36, confirm `General Anesthesia Used` is `100 (59.5%)`.
  3. Recalculate `100/170 × 100` and round to one decimal.
  4. Confirm the finding if no row-specific denominator of 168 is documented; such documentation
     would resolve it as a denominator-presentation omission.

### V-03 — The sentence labelled “follow-up imaging” reproduces baseline core-imaging counts

- **Classification:** Verified
- **Category / severity:** Presentation inconsistency / Moderate
- **Issue statement:** The Results section labels 8 MRI and 328 CT examinations as follow-up
  imaging, although those exact counts are the modalities used to determine core at randomization
  and a separate 204-patient MR-DWI follow-up cohort is reported.
- **Reported source:** DOC-001-MAIN,
  `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 4, Results, second paragraph:
  **“Follow-up imaging modality was MRI in 8 of 336 patients (2%) and CT in 328 of 336
  patients (98%).”**
- **Comparators:**
  - DOC-001-MAIN PDF p. 5, Table 1, row group `Imaging modality used to determine ischemic core
    volume at randomization`: CT perfusion **165 EVT + 163 medical care**; MR DWI
    **3 EVT + 5 medical care**.
  - DOC-001-MAIN PDF p. 9, section `Association of Follow-Up Infarct Volume and Infarct Growth
    With EVT Outcomes`: **“In patients with MR diffusion follow-up (n = 204 [61%])”**.
  - DOC-006-RESULTS-SUPP PDF p. 51, eTable 11, title `patients with MR DWI follow-up`,
    columns **MM N=101**, **mTICI 0-2a N=24**, and **mTICI 2b-3 N=79**.
- **Reproducible calculation / logical basis:**
  - Baseline CT core-imaging total: `165 + 163 = 328`.
  - Baseline MR-DWI core-imaging total: `3 + 5 = 8`.
  - MR-DWI follow-up total: `101 + 24 + 79 = 204`.
  - `8/336 × 100 = 2.38%` (reported as 2%); `204/336 × 100 = 60.71%`
    (reported as 61%).
  The p. 4 values exactly reproduce the explicitly labelled randomization modalities and cannot
  simultaneously describe the reported 204-person MR-DWI follow-up cohort.
- **Bounded impact:** The error misidentifies the imaging time point and can make the MRI
  follow-up analysis population appear to contain 8 rather than 204 patients. It does not change
  the displayed infarct-growth estimates.
- **Human verification steps:**
  1. Confirm the quoted `Follow-up imaging modality` sentence on DOC-001-MAIN PDF p. 4.
  2. Add the two Table 1 treatment-column counts on PDF p. 5 to reproduce 328 CT and 8 MR DWI
     at randomization.
  3. Confirm `n=204` on DOC-001-MAIN PDF p. 9 and `101 + 24 + 79` in DOC-006-RESULTS-SUPP
     eTable 11 on PDF p. 51.
  4. Confirm the finding if the p. 4 sentence remains labelled follow-up; correction to
     baseline/randomization imaging would resolve it.

### V-04 — The medical-management infarct-growth upper quartile is 125 mL in the main article and 135 mL in eTable 11

- **Classification:** Verified
- **Category / severity:** Cross-document inconsistency / Minor
- **Issue statement:** For the same medical-management MR-DWI follow-up group and infarct-growth
  measure, the main article reports an upper quartile of 125 mL while the cited supplement reports
  135 mL.
- **Reported source:** DOC-001-MAIN,
  `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 9,
  `Association of Follow-Up Infarct Volume and Infarct Growth With EVT Outcomes`:
  medical management **`median, 95 [IQR, 56-125] mL`**, followed by the citation to eTable 11.
- **Comparator:** DOC-006-RESULTS-SUPP,
  `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 51, eTable 11,
  MM `N=101`, row `Infarct growth from CTP/MRI core (ml), median (IQR)`:
  **`95 (56, 135)`** mL.
- **Reproducible calculation / logical basis:** The outcome, group, median, and lower quartile
  match, and the main text explicitly cites eTable 11. Upper-quartile difference:
  `135 mL − 125 mL = 10 mL`.
- **Bounded impact:** Only the upper quartile of this one descriptive distribution is affected;
  the median, lower quartile, and other reperfusion-group summaries shown alongside it agree.
- **Human verification steps:**
  1. Confirm `95 [IQR, 56-125] mL` on DOC-001-MAIN PDF p. 9.
  2. Confirm `95 (56, 135)` in the MM column of DOC-006-RESULTS-SUPP eTable 11, PDF p. 51.
  3. Confirm both labels specify infarct growth from baseline CTP/MRI core in the MR-DWI
     follow-up analysis.
  4. The retained 10-mL difference confirms the finding; correction of either upper quartile to
     the source analysis value would resolve it.

### V-05 — `aRR` is incorrectly expanded as “absolute risk reduction” for a ratio measure

- **Classification:** Verified
- **Category / severity:** Presentation inconsistency / Minor
- **Issue statement:** The article defines `aRR` as “absolute risk reduction,” but its estimation
  method, ratio-scale values, footnotes, and separate `aRD` measure identify `aRR` as an adjusted
  risk/rate ratio.
- **Reported sources:**
  - DOC-001-MAIN,
    `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 6,
    `Association of ASPECTS and CT Perfusion/MRI Core Volume With Clinical Outcomes in
    EVT-Treated Patients`: **“Functional independence (absolute risk reduction [aRR],
    0.89 [95% CI, 0.84-0.95] per 10-mL increase)”**.
  - DOC-001-MAIN PDF p. 7, Table 2 abbreviations: **`aRR, absolute risk reduction`**.
  - DOC-001-MAIN PDF p. 9, Table 3 abbreviations: **`aRR, absolute risk reduction`**.
- **Comparators:**
  - DOC-001-MAIN PDF p. 4, Statistical Analysis: secondary outcomes used **“modified Poisson
    regression models with robust standard errors.”**
  - DOC-001-MAIN PDF p. 7, Table 2 footnote, and p. 9, Table 3 footnote:
    **“aRR greater than 1 indicates higher rate ratio”** for the listed binary mRS outcomes.
  - DOC-001-MAIN PDF p. 9, Table 3 abbreviations separately define **`aRD, absolute risk
    difference`** and display aRD estimates such as `−0.001`.
- **Reproducible logical basis:** A risk/rate ratio is multiplicative and has null value 1;
  an absolute risk reduction/difference is additive and has null value 0. The displayed `0.89`
  with a ratio-type CI, modified-Poisson method, the explicit phrase `higher rate ratio`, and the
  separately reported `aRD` are mutually consistent with an adjusted risk/rate ratio, not an
  absolute reduction.
- **Bounded impact:** The numeric estimates need not be wrong, but the expansion can cause a
  multiplicative ratio such as 0.89 to be read as an absolute 0.89-unit risk reduction.
- **Human verification steps:**
  1. Confirm the modified-Poisson method on DOC-001-MAIN PDF p. 4.
  2. Confirm the `absolute risk reduction` expansion on pp. 6, 7, and 9.
  3. Confirm the same tables call the measure a `rate ratio` and that Table 3 separately reports
     `aRD`.
  4. The co-occurrence of these incompatible definitions confirms the finding; defining `aRR`
     as the intended adjusted ratio term would resolve it.

### V-06 — Main text says EVT outcome probabilities rise with mismatch volume, while eFigure 17 shows them falling

- **Classification:** Verified
- **Category / severity:** Statistical reporting inconsistency / Moderate
- **Issue statement:** The main article says functional-independence and independent-ambulation
  probabilities increase with mismatch volume in EVT recipients, but both EVT curves in the
  explicitly cited eFigure 17 slope downward as mismatch volume increases.
- **Reported source:** DOC-001-MAIN,
  `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 8,
  `Association of Mismatch With EVT Treatment Effect and Functional Outcomes`:
  **“as mismatch volume increased, the marginal probability of functional independence and
  independent ambulation increased for patients receiving EVT but decreased in patients
  receiving medical management only (eFigure 17 in Supplement 5).”**
- **Comparator:** DOC-006-RESULTS-SUPP,
  `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 23, eFigure 17:
  panel A is labelled estimated probability of mRS 0-2 and panel B mRS 0-3; the legend identifies
  the teal curve as EVT and red curve as MM. Across an x-axis increasing from about −100 to
  400 mL, both teal EVT curves fall from left to right. Both red MM curves also fall.
- **Reproducible logical basis:** An increase in probability as x increases requires a positive
  plotted slope. The displayed EVT slope is negative in both cited favorable-outcome panels
  (visually, approximately 0.27 to 0.05 in panel A and 0.62 to 0.07 in panel B over the shown
  range). Thus the plot shows the opposite EVT direction from the text. The conclusion does not
  depend on color assignment because neither arm curve rises.
- **Bounded impact:** The direction of the modelled mismatch-volume association within EVT is
  reported inconsistently. This does not by itself invalidate the separate categorical mismatch
  treatment-effect results.
- **Human verification steps:**
  1. Read the quoted sentence on DOC-001-MAIN PDF p. 8.
  2. On DOC-006-RESULTS-SUPP PDF p. 23, follow the EVT curves in eFigure 17 panels A and B from
     low to high mismatch volume.
  3. Confirm both curves decline as the x-axis increases.
  4. Opposite text and plot directions confirm the finding; correction of either the narrative
     direction or the plotted model output to the source analysis would resolve it.

### V-07 — eFigure 13 reverses the favor-direction labels for the adverse mRS 5-6 outcome

- **Classification:** Verified
- **Category / severity:** Presentation inconsistency / Moderate
- **Issue statement:** eFigure 13 labels relative risks below 1 as favoring medical management
  for complete dependence or death, although lower risk of that adverse outcome favors
  thrombectomy and the same-outcome eFigure 9 labels the direction correctly.
- **Reported source:** DOC-006-RESULTS-SUPP,
  `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 19, eFigure 13,
  captioned `complete dependence or death (mRS 5-6)`: the forest-plot axis labels the side below
  1 **`Favours Medical Management`** and the side above 1 **`Favours Thrombectomy`**.
- **Source values:** In eFigure 13, NCCT core `<70mL (n=132)` reports thrombectomy
  **`27 (39.71%)`**, medical management **`39 (60.94%)`**, and RR
  **`0.68 (0.49-0.95)`**, plotted left of 1.
- **Comparator:** DOC-006-RESULTS-SUPP PDF p. 15, eFigure 9, the same outcome
  `complete dependence or death (mRS 5-6)`, labels the below-1 side
  **`Favours Thrombectomy`** and above-1 side **`Favours Medical Management`**.
- **Reproducible logical basis:** The plotted risk is thrombectomy relative to medical
  management. For an adverse outcome, RR `<1` indicates less complete dependence/death in the
  thrombectomy numerator group. The example percentages also satisfy `39.71% < 60.94%`.
  Therefore the below-1 direction favors thrombectomy, not medical management.
- **Bounded impact:** Point estimates and CIs remain readable, but the annotations can invert
  the visual interpretation of every row in eFigure 13.
- **Human verification steps:**
  1. Confirm the eFigure 13 outcome and favor labels on DOC-006-RESULTS-SUPP PDF p. 19.
  2. Confirm the `<70mL (ncct)` percentages and RR 0.68.
  3. Compare the same-outcome labels in eFigure 9 on PDF p. 15.
  4. Opposite favor labels for the same adverse outcome confirm the finding; swapping the
     eFigure 13 annotations would resolve it.

### V-08 — eFigures 18-19 and the main text conflict over whether the prediction covariate is CTP/MRI or composite core

- **Classification:** Verified
- **Category / severity:** Cross-document inconsistency / Moderate
- **Issue statement:** The prediction-figure labels alternately identify the fixed core-volume
  covariate as CTP/MRI core and composite core, while the panels themselves say only `Core
  Volume`, so the reported model input is not consistently identified.
- **Reported and comparison sources:**
  - DOC-006-RESULTS-SUPP,
    `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 24, eFigure 18 title:
    **“with CTP/MRI core volume set at a) 70ml, b) 100ml and c) 150ml.”**
  - On the same page, eFigure 18 explanatory text instead says the relationship is consistent
    across **“composite core volume estimates”** and decreases as **“composite core volume
    estimate increases.”**
  - DOC-006-RESULTS-SUPP PDF p. 25, eFigure 19 title and body specify **“composite core volume”**
    at 70, 100, and 150 mL.
  - DOC-001-MAIN,
    `jama_sarraj_2024_oi_240006_1708623114.96234.pdf`, PDF p. 10,
    `Association of Age and Time With Functional Outcome After EVT`, after separately citing
    eFigures 18 and 19: **“The relationship was consistent across estimated CT perfusion/MRI
    core volumes set at 70 mL, 100 mL, and 150 mL.”**
  - The visible panel strips on DOC-006 pp. 24-25 say only **`Core Volume 70`**,
    **`Core Volume 100`**, and **`Core Volume 150`**.
- **Logical basis:** DOC-006-RESULTS-SUPP PDF p. 37, eTable 1 footnote, defines composite core as
  **“the larger of CTP/MRI core volume and CT hypodensity volume estimates.”** Composite and
  CTP/MRI core are therefore distinct variables and their labels are not interchangeable. The
  quoted sources assign different variables to the same family of prediction panels.
- **Bounded impact:** The inconsistency prevents a reader from determining from the figures and
  article text which core estimate was held fixed, especially for eFigure 19. It does not show
  that the displayed predicted probabilities themselves are numerically wrong.
- **Human verification steps:**
  1. Compare the eFigure 18 title with its explanatory text on DOC-006-RESULTS-SUPP PDF p. 24.
  2. Compare eFigure 19 on PDF p. 25 with the collective main-text statement on DOC-001-MAIN
     PDF p. 10.
  3. Confirm on DOC-006-RESULTS-SUPP PDF p. 37 that composite core is defined as a distinct
     larger-of-two estimate.
  4. The conflicting labels confirm the reporting finding. Model code/output is needed only to
     decide which label should replace the others.

---

## Uncertain candidate

### U-01 — “No effect modification” narrative versus eFigure 10 interaction P=.0164

- **Classification:** Uncertain
- **Category / severity:** Cross-document inconsistency / Minor if confirmed
- **Candidate statement:** DOC-001-MAIN PDF p. 11, Discussion, says:
  **“While no evidence of EVT treatment effect modification was observed based on either imaging
  modality…”**
- **Comparator:** DOC-006-RESULTS-SUPP PDF p. 16, eFigure 10, NCCT hypodensity-volume
  100-mL split, reports:
  - `<100mL (ncct), n=207`: GenOR **2.25 (95% CI, 1.65-3.06)**
  - `>=100mL (ncct), n=129`: GenOR **1.25 (95% CI, 0.89-1.74)**
  - interaction **P=.0164**
- **Calculation:** The article's rule on DOC-001-MAIN PDF p. 4 is `P<.05`; `.0164 < .05`.
  Thus eFigure 10 reports statistical evidence of interaction for this post hoc NCCT threshold.
- **Why not Verified:** The necessary scope link is missing. In context, `either imaging
  modality` may be intended to summarize the primary/prespecified ASPECTS and CTP/MRI-core
  analyses rather than every post hoc NCCT-hypodensity threshold analysis. The PDFs do not define
  the scope of that phrase. A broad reading conflicts with eFigure 10; a restricted reading does
  not.
- **Bounded impact:** Any exception is limited to the post hoc NCCT hypodensity `<100` versus
  `>=100` mL ordinal-mRS analysis; it does not imply interaction for other measures or thresholds.
- **Human resolution steps:**
  1. Confirm the Discussion wording on DOC-001-MAIN PDF p. 11.
  2. Confirm the NCCT rows and interaction P=.0164 on DOC-006-RESULTS-SUPP PDF p. 16.
  3. Ask whether `either imaging modality` was intended to cover post hoc NCCT-hypodensity
     sensitivity analyses.
  4. Classify as confirmed only if the sentence was intended as a summary of all reported imaging
     analyses; otherwise resolve by limiting the narrative explicitly to the intended analyses.

---

## Rejected candidate

### R-01 — FF-04 alleged displaced labels in eFigure 6A

- **Classification:** Rejected
- **Reason:** The original-page rendering contradicts the candidate. DOC-006-RESULTS-SUPP,
  `joi240006supp5_prod_1708623115.01733.pdf`, PDF p. 12, eFigure 6A visibly shows four paired bar
  groups, and the labels `0-49 ml`, `50-99 ml`, `100-149 ml`, and `150 ml or larger` are each
  centered beneath their respective group. Panel B uses the same correctly aligned four-label
  layout.
- **Source values checked:** Panel A bar pairs are 2%/98%, 6%/94%, 13%/87%, and 28%/73%;
  each is visibly associated with one centered stratum label.
- **Logical basis:** Four visible groups have a one-to-one, spatially centered mapping to four
  labels. The alleged displacement is not present in the source page and appears to have arisen
  from a prior rendering or visual-reading error.
- **Human check:** Open DOC-006-RESULTS-SUPP PDF p. 12 at full-page width and compare each label
  midpoint with its paired bars. The centered positions reject the candidate.
