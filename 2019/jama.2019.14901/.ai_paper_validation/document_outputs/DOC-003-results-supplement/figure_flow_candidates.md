# Figure and table screen — candidate findings

**Scope:** DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF pp. 1-9. Rendered pages inspected for eTables 1-5 and the eFigure. This is a candidate screen, not a final adjudication.

## FFC-002 — P value for the same displayed secondary outcome differs between eTable 1 and the main article

- **Category / severity:** Statistical reporting inconsistency; minor.
- **Reported item:** Postextubation respiratory failure at day 7.
- **Exact locations and visible evidence:**
  - **Supplement:** DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF p. 2, **eTable 1**, first row: HFNO alone **88 (29)**, HFNO with NIV **70 (21)**, **P=.02**.
  - **Main-article comparator:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF p. 8 / printed p. 1472, **Table 2**, same row: **88 (29)** and **70 (21)**, **P=.01**. The nearby article narrative at PDF p. 6 / printed p. 1470 also states **P=.01**.
- **Reproducible logical comparison:** Both locations label the outcome “postextubation respiratory failure at day 7,” use the same two group denominators (302 and 339), and display identical group counts and rounded percentages. Their displayed P values nevertheless differ: `.02 − .01 = .01`.
- **Bounded impact:** Both printed P values are below .05, so the discrepancy does not change the displayed conventional significance classification; it leaves the exact reported P value indeterminate from the documents.
- **Verification steps:**
  1. Confirm whether eTable 1 and Table 2 were intended to report the same analysis/test for this identically labelled outcome and counts.
  2. Check the statistical output or author correction record. An output P that rounds to .01 supports Table 2; one that rounds to .02 supports eTable 1; distinct, predeclared tests would resolve the apparent inconsistency.

## FFC-003 — Supplementary survival eFigure has incompatible time-origin labels

- **Category / severity:** Presentation inconsistency; minor.
- **Exact location and visible evidence:** DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF p. 9, **eFigure**. The caption reads: “Kaplan-Meier Curves of the Cumulative Probability of Survival **From Extubation to Day 90**.” The plot x-axis label reads **“Days Since Intubation.”**
- **Explicit within-package comparator:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF p. 7, **Figure 2**, and PDF p. 8, **Figure 3**, each label the x-axis **“Time Since Extubation, d.”**
- **Reproducible logical comparison:** A single Kaplan-Meier time scale cannot simultaneously have the stated origin *from extubation* and be labelled *days since intubation* without further definition; no reconciliation is provided in the caption or visible annotations.
- **Bounded impact:** The visual time origin for the day-90 survival trajectory is ambiguous. The plotted labels, at-risk counts, and log-rank P=.37 remain visible, but a reader cannot determine from the figure alone whether the 0-to-90 scale is anchored to intubation or extubation.
- **Verification steps:**
  1. Confirm the eFigure caption and x-axis wording on PDF p. 9.
  2. Compare the programmed Kaplan-Meier time variable or figure source. If measured from extubation, correcting the x-axis resolves the issue; if measured from intubation, correcting the caption and any linked day-90 wording resolves it.

## Screened with no additional local candidate

- **eTables 2-4, PDF pp. 3-7:** subgroup group sizes and event counts reconcile to the main article totals (for example, day-7 reintubations `10+45=55` vs HFNO alone and `5+35=40` vs HFNO with NIV).
- **eTable 5, PDF p. 8:** center-level denominators and reintubation numerators reconcile to the displayed Total row: 641 overall, 302 HFNO alone, 339 HFNO with NIV, and 95/55/40 day-7 reintubations.
- **eFigure, PDF p. 9:** day-90 number-at-risk totals are not treated as event totals; no unsupported arithmetic contradiction was inferred from their expected censoring/death losses.
