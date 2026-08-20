# Figure, table, and flow screen — candidate findings

**Scope:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF pp. 1-9. Rendered pages used for Figure 1 (p. 3), Table 1 (pp. 5-6), Figure 2 (p. 7), and Table 2/Figure 3 (p. 8), with nearby native text checked. This is a candidate screen, not a final adjudication.

## FFC-001 — Secondary-outcome absolute difference differs between nearby text and table

- **Category / severity:** Arithmetic inconsistency; minor.
- **Reported item:** Postextubation respiratory failure at day 7.
- **Exact locations and visible evidence:**
  - **Text:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF p. 6 / printed p. 1470, **Secondary Outcomes**: “21% vs 29%; difference, −8.7% [95% CI, −15.2% to −1.8%]; P = .01.”
  - **Table comparator:** same document, PDF p. 8 / printed p. 1472, **Table 2**, secondary-outcomes row *Postextubation respiratory failure at day 7*: HFNO alone **88 (29)**; HFNO with NIV **70 (21)**; absolute difference **−8.5 (−15.2 to −1.8)**; **P=.01**.
  - The same counts are visibly repeated in DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF p. 2, **eTable 1**, first row.
- **Reproducible comparison:** The table denominators are 302 (HFNO alone) and 339 (HFNO with NIV). Using the displayed counts, `(70 / 339 × 100) − (88 / 302 × 100) = 20.64897 − 29.13907 = −8.49010` percentage points, which rounds to **−8.5 percentage points** at one decimal, not −8.7. The narrative and table otherwise show the same confidence interval and P value.
- **Bounded impact:** The discrepancy is 0.2 percentage point in the stated secondary-outcome contrast; it does not alter the displayed event counts, direction, confidence interval, or stated significance.
- **Verification steps:**
  1. Confirm the visual Table 2 row and the PDF p. 6 Secondary Outcomes sentence both refer to postextubation respiratory failure at day 7 and the same randomized groups.
  2. Recalculate the displayed proportion difference from 70/339 and 88/302. A result of −8.5 percentage points confirms the table/count-consistent value; source analysis output showing an alternative estimand would resolve the discrepancy.

## Screened with no additional local candidate

- **Figure 1 flow, PDF p. 3:** every displayed exclusion and allocation reconciliation holds: `3121−1460=1661`; `1661−692=969`; `969−321=648`; `306+342=648`; and `302+339=641` analyzed.
- **Figures 2-3, PDF pp. 7-8:** displayed day-7 curve endpoints and baseline at-risk totals agree with Table 2 and the hypercapnic/nonhypercapnic subgroup counts.
- **Table 1, PDF pp. 5-6:** reviewed mutually exclusive category totals and subgroup counts reconcile to the shown denominators where such summation is applicable.
