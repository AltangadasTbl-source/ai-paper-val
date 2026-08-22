# Evidence-verification stage

**Scope.** Verification was limited to the four parent-supplied candidates. TC-01, STAT-01, and FFC-002 were deduplicated as a single candidate. No new issues were sought. The cited original PDFs and their source-linked rendered page images were reopened. No candidate received more than two verification rounds.

**Result:** 4 **Verified**, 0 **Uncertain**, 0 **Rejected**.

## VF-01 — Verified

- **Candidate:** RF absolute-difference conflict (STAT-02 / FFC-001).
- **Category / severity:** Arithmetic inconsistency; minor.
- **One-sentence issue statement:** For postextubation respiratory failure at day 7, the main narrative reports an absolute difference of **−8.7 percentage points**, while Table 2 reports **−8.5 percentage points** for the same outcome and the displayed counts reproduce −8.5 percentage points.
- **Source evidence:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF p. 6 / printed p. 1470, **Results—Secondary Outcomes**, first paragraph: “21% vs 29%; difference, **−8.7% [95% CI, −15.2% to −1.8%]; P = .01**.”
- **Comparison evidence:** DOC-001-main-article, same filename, PDF p. 8 / printed p. 1472, **Table 2**, Secondary Outcomes row “Postextubation respiratory failure at day 7”: high-flow nasal oxygen alone, **88 (29)** with `n=302`; high-flow nasal oxygen with NIV, **70 (21)** with `n=339`; absolute difference, **−8.5% (95% CI, −15.2% to −1.8%)**; **P=.01**.
- **Calculation / logical basis:** The table's contrast is the NIV arm minus the oxygen-alone arm. `(70/339 − 88/302) × 100 = 20.64897 − 29.13907 = −8.49010` percentage points, which rounds to **−8.5 percentage points** to the displayed one decimal place. It does not round to −8.7. The narrative and table have the same endpoint, time point, CI, and P value; neither labels a different estimand. The displayed estimates differ by **0.2 percentage point**.
- **Bounded impact:** The inconsistency changes only the displayed point estimate by 0.2 percentage point. It does not change the event counts, direction, confidence interval, P value, or nominal-significance interpretation.
- **Verification rounds:** Round 1 reopened and compared the native PDF text on pp. 6 and 8 and visually confirmed both rendered pages. Round 2 recomputed the risk difference from the displayed counts and denominators.
- **Human verification steps:**
  1. On DOC-001 PDF p. 6, confirm the quoted Secondary Outcomes sentence reports −8.7%.
  2. On DOC-001 PDF p. 8, confirm the Table 2 row reports 88/302, 70/339, and −8.5%.
  3. Recalculate `(70/339 − 88/302) × 100`; a result of approximately −8.4901 percentage points confirms the count-consistent −8.5% display.
  4. Check the source analysis output for an explicitly different estimand; absent one, the narrative and table should be standardized.

## VF-02 — Verified

- **Candidate:** Same RF comparison P-value conflict (deduplicated TC-01 / STAT-01 / FFC-002).
- **Category / severity:** Cross-document inconsistency; minor.
- **One-sentence issue statement:** The identical displayed day-7 postextubation-respiratory-failure comparison reports **P=.01** in the main article and **P=.02** in the results supplement without labelling different tests.
- **Source evidence:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF p. 8 / printed p. 1472, **Table 2**, Secondary Outcomes row “Postextubation respiratory failure at day 7”: **88 (29)** of 302 versus **70 (21)** of 339, absolute difference **−8.5% (95% CI, −15.2% to −1.8%)**, **P=.01**. The nearby narrative on PDF p. 6 also reports **P=.01**.
- **Comparison evidence:** DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF p. 2, **eTable 1**, first row “Post-extubation respiratory failure at day 7, No. (%)”: **88 (29)** of 302 versus **70 (21)** of 339, **P=.02**.
- **Calculation / logical basis:** The outcome, day-7 time point, arm labels, arm denominators, event counts, and rounded percentages are identical. The displayed P values differ by `.02 − .01 = .01`. DOC-001 PDF p. 4 / printed p. 1468, **Statistical Analysis**, states that day-7 postextubation respiratory-failure rates were compared by a **χ² test**, but neither cited result labels a different χ² implementation. As a sensitivity check from the displayed 2×2 table, the uncorrected Pearson χ² P value is approximately `.012786` (rounds to `.01`) and the continuity-corrected value is approximately `.016490` (rounds to `.02`). This supplies a plausible explanation but does not resolve the unlabelled conflict or establish which implementation was intended.
- **Bounded impact:** Both values are below .05, so the discrepancy does not change the nominal-significance conclusion; it leaves the exact reported P value and intended χ² implementation indeterminate from the supplied documents.
- **Verification rounds:** Round 1 reopened and visually confirmed DOC-001 pp. 6 and 8 and DOC-003 p. 2. Round 2 reopened the stated method on DOC-001 p. 4 and reproduced the two common χ² implementations from the displayed counts.
- **Human verification steps:**
  1. Confirm the identical endpoint, denominators, and counts in DOC-001 Table 2 and DOC-003 eTable 1.
  2. Confirm that the two displayed P values are .01 and .02.
  3. Inspect the prespecified analysis settings or production output for continuity correction and the exact P value.
  4. A documented, separately labelled test for each table would resolve the apparent inconsistency; otherwise standardize the P value to the prespecified analysis.

## VF-03 — Verified

- **Candidate:** Nonhypercapnic P-value formatting conflict (STAT-03).
- **Category / severity:** Statistical reporting inconsistency; minor.
- **One-sentence issue statement:** For day-7 reintubation in the nonhypercapnic subgroup, the main narrative reports **P=.10**, whereas eTable 4 reports **P=.1057** for the same displayed comparison, which rounds to .11 rather than .10 at the narrative's two-decimal precision.
- **Source evidence:** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF p. 7 / printed p. 1471, **Results—Subgroup Analysis and Additional Analyses**, first paragraph: among **530** patients with PaCO2 ≤45 mm Hg, reintubation at day 7 was “13% with noninvasive ventilation vs 18% with high-flow nasal oxygen alone; difference, **−5.0% [95% CI, −11.2% to 1.1%]; P=.10**.”
- **Comparison evidence:** DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF p. 7, **eTable 4**, Primary outcome row “Reintubation at day 7, No. (%)”: oxygen alone **45 (18)** of 254; oxygen with NIV **35 (13)** of 276; difference **−5.0% (95% CI, −11.2% to 1.1%)**; **P=.1057**. The subgroup totals reconcile: `254 + 276 = 530`.
- **Calculation / logical basis:** The subgroup definition, endpoint, time point, totals, rounded percentages, difference, and CI match. Ordinary nearest-hundredth rounding gives `.1057 → .11`, not `.10`. Using the displayed 2×2 counts, the uncorrected Pearson χ² test gives `P≈.1057337`, which reproduces eTable 4's .1057 and likewise rounds to .11. No different test is labelled in the narrative.
- **Bounded impact:** Both P values exceed .05 and the CI crosses zero, so the discrepancy does not change the reported nonsignificant conclusion; it affects numerical precision and reproducibility only.
- **Verification rounds:** Round 1 reopened and visually confirmed DOC-001 p. 7 and DOC-003 p. 7. Round 2 checked subgroup-total identity, ordinary rounding, and the count-based χ² value.
- **Human verification steps:**
  1. Confirm the narrative's subgroup, outcome, effect, CI, and P=.10 on DOC-001 p. 7.
  2. Confirm the same subgroup comparison and P=.1057 in DOC-003 eTable 4 on p. 7.
  3. Verify the statistical output and the intended formatting rule. An exact P near .1057 confirms that a two-decimal nearest-rounding display should be .11; a separately specified analysis yielding .10 would resolve the discrepancy.

## VF-04 — Verified

- **Candidate:** eFigure timing-label mismatch (FFC-003).
- **Category / severity:** Presentation inconsistency; minor.
- **One-sentence issue statement:** The supplementary eFigure describes survival **from extubation** in its caption but labels the plotted time scale as **days since intubation**, giving incompatible time origins on the same figure.
- **Source evidence and comparison:** DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF p. 9, **eFigure**. Caption: “Kaplan-Meier Curves of the Cumulative Probability of Survival **From Extubation to Day 90**.” Plot x-axis: “**Days Since Intubation**.”
- **Logical basis:** Extubation and intubation are distinct clinical events and therefore distinct possible time origins. A single 0-to-90-day Kaplan-Meier scale cannot be simultaneously “from extubation” and “since intubation” without an explicit transformation or definition; none appears in the caption or visible annotations. The contradiction is directly visible within one figure and requires no arithmetic.
- **Bounded impact:** The figure's time origin is ambiguous. The curves, at-risk counts, and displayed log-rank P value remain visible, but readers cannot determine from the figure whether day 0 is intubation or extubation.
- **Verification rounds:** One round reopened the original supplement PDF p. 9, checked the page image at original detail, and compared the caption with the graphical x-axis label.
- **Human verification steps:**
  1. On DOC-003 PDF p. 9, confirm the caption says “From Extubation to Day 90.”
  2. On the same page, confirm the x-axis says “Days Since Intubation.”
  3. Inspect the programmed survival-time variable or figure source. If day 0 is extubation, correct the x-axis; if day 0 is intubation, correct the caption and related wording.

