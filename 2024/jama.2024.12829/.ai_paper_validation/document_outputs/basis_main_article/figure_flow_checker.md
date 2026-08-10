# Figure/flow/table visual audit — `basis_main_article`

- **Source PDF:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`
- **Audited scope:** PDF pp. 1–11; retained page renders and nearby native/extracted text only.
- **Source modified:** No.

## Supported local candidate

### M1 — Statistical reporting inconsistency: point estimate lies outside the displayed confidence interval

- **Location:** PDF p. 8 / print p. 1066, Table 2, secondary outcome “Any stroke outside the territory of the qualifying artery within 1 y after enrollment.”
- **Visible/source values:** Balloon angioplasty 3/249 (1.2%) versus aggressive medical management 4/252 (1.6%); incidence difference **−0.4 percentage points** with displayed 95% CI **−2.4 to −1.7**.
- **Logical basis:** The point estimate −0.4 is outside the displayed interval [−2.4, −1.7]. A direct unadjusted difference calculation gives approximately −0.38 percentage points, and the approximate normal interval is −2.43 to +1.67 percentage points, suggesting the upper-bound sign may have been dropped. The inconsistency is verifiable without choosing a preferred CI method because any valid displayed CI must contain its reported point estimate.
- **Verification instruction:** Inspect the Table 2 row on PDF p. 8 and confirm that the upper bound is printed as “−1.7”; recompute the difference and CI from 3/249 and 4/252 or check the article’s production value.
- **Status:** Supported candidate.

## Checked without a supported inconsistency

- **Figure 1, PDF p. 5:** 326+238+89+73+46+43+35+24+23=897 screening exclusions; 1409−897=512 randomized; arm withdrawals reconcile 256→249 and 256→252; adjudication exclusions reconcile 249−16=233 and 252−14=238.
- **Figure 2, PDF p. 7:** Most subgroup strata reconcile to the primary-analysis denominators. Hypoperfusion uses only the CT-perfusion-assessed subset (122 vs 127); the figure explicitly identifies CT perfusion and does not state that this subgroup covers all randomized participants, so no contradiction was inferred.
- **Figure 3, PDF p. 9:** Overall and landmark hazard-ratio annotations match the nearby result claims. The at-risk table starts at 249 and 252. No unambiguous visual/count contradiction was located.

