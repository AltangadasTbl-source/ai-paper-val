# Figure and flow checker record

- **Document:** DOC-001-MAIN, `jama_shotar_2025_oi_250033_1750956987.75881.pdf`
- **Audited scope:** PDF pp. 1-9; visual priority pp. 4-7.
- **Comparison source:** DOC-004-RESULTS-SUPP PDF pp. 8-15 only.
- **Status:** Complete. Two local candidates retained; neither is adjudicated.

## Retained candidates

### FF-01 - Exclusion-flow title and cross-reference use an inclusion label for excluded patients

- **Category:** Presentation inconsistency
- **Exact locations:** DOC-001-MAIN PDF p. 4, Figure 1 footnote a; DOC-004-RESULTS-SUPP PDF p. 8, eFigure 1 title and exclusion box; DOC-001-MAIN PDF p. 2, Methods, Patients.
- **Visible/source statements:** Figure 1 footnote a and the eFigure 1 title both say “reasons for excluding patients with an inclusion criterion.” The eFigure 1 box instead itemizes `Patient refusal (n=101)`, `Other pre-specified non-inclusion criteria (n=164)`, `Other reasons (n=18)`, and `Unknown reasons (n=34)`. The Methods distinguishes conditions making patients “eligible for enrollment” from conditions under which patients “were not eligible for inclusion.”
- **Logic:** The displayed title/cross-reference describes excluded people as having “an inclusion criterion,” while the visual and Methods describe refusal, non-inclusion criteria, and other/unknown exclusion reasons. The label does not identify the intended exclusion category and reverses or omits the eligibility qualifier.
- **Verification instruction:** Read the exact p. 2 eligibility wording, then inspect Figure 1 footnote a on p. 4 and the eFigure 1 title and four top-level exclusion categories on supplement p. 8. Confirm the source has no omitted word such as “not meeting” before “an inclusion criterion.”

### FF-02 - Full-analysis-set/imputation labels are paired with observed evaluable-case denominators

- **Category:** Presentation inconsistency
- **Exact locations:** DOC-001-MAIN PDF p. 4, Figure 1 primary-analysis boxes; DOC-001-MAIN PDF p. 6, Table 2 primary-end-point row and footnotes a-c; DOC-004-RESULTS-SUPP PDF p. 9, eFigure 2 primary row; DOC-004-RESULTS-SUPP PDF p. 15, eTable 4 EMPROTECT primary-outcome cell.
- **Visible/source values:** Figure 1 says `171` per arm were included in the primary analysis, with `9` and `14` nonevaluable cases multiply imputed; evaluable cases were `162` and `157`. The eFigure 2 primary row is labeled `Full analysis set, multiple imputation` but displays `24/162` and `33/157`. eTable 4 similarly displays `24/162` and `33/157` followed by `ITT with imputation`. Table 2 footnote a clarifies elsewhere that case counts and percentages are observed values before imputation, while footnotes b-c say the effect analysis used the full analysis set after imputation.
- **Logic:** The visible fractions use observed evaluable-case denominators (`162` and `157`), not the stated full/ITT analysis population (`171` and `171`). The main table explains this mixed presentation, but eFigure 2 and eTable 4 do not identify their fractions as pre-imputation observed values, so their population labels and displayed denominators are internally discordant.
- **Verification instruction:** Confirm from Figure 1 that the imputed full analysis includes 171 per arm; then inspect whether eFigure 2 or eTable 4 contains a legend defining `24/162` and `33/157` as observed pre-imputation counts. If no such definition is present, retain as a presentation issue rather than treating the fractions as the imputed analysis denominators.

## Rejected checks

- **Figure 1 participant arithmetic:** `659 - 317 = 342`; `171 + 171 = 342`; nonintervention reasons sum to `13+5+4+2+1+1=26`; evaluable plus nonevaluable counts are `162+9=171` and `157+14=171`. Rejected: no count inconsistency.
- **Figure 1 discontinuation versus evaluability:** The apparent `171-15` / `171-19` mismatch is resolved by the diagram's explicit death subcategories: endpoint-known neurological/undetermined deaths remain evaluable, while the nonevaluable boxes contain other-cause deaths, losses, and withdrawals. Rejected as an ambiguous sequential-flow reading.
- **Figure 2 subgroup totals:** Unilateral plus bilateral rows reproduce all-patient events and denominators (`12+12=24`, `118+44=162`; `22+11=33`, `117+40=157`); medication-use rows do likewise. Rejected.
- **Figure 2 axes and annotations:** OR direction labels, null line at 1, confidence intervals, and interaction P values `.32` and `.18` are visibly aligned with their subgroup blocks and match the nearby Results claim. Rejected.
- **Tables 1-3 visible counts:** No figure/flow conflict was located in baseline localization counts, primary-event components, or adverse-event annotations on pp. 5-7.
