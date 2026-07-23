# Statistical Consistency Check

**Checker:** `statistical_consistency_checker`  
**Documents audited:** DOC-001 main article and DOC-004 results supplement only  
**Evidence used:** main-text evidence map, result-relevant supplementary evidence map, normalized native text, and rendered/OCR-assisted in-scope pages  
**Protocol/SAP:** Not inspected by design  
**External sources:** None  
**Source PDFs modified:** No

## Candidate issues

### SC-01 — Primary/neonatal outcome denominators are mislabeled as women

- **Category:** Presentation inconsistency
- **Status:** Candidate for evidence verification
- **Source file:** `jama_kumar_2025_oi_250034_1750956984.08518.pdf` (DOC-001)
- **Exact locations and source statements/values:**
  - **PDF p. 1, Abstract, Results:** “The primary outcome occurred in **83 of 1625 women (5.1%)** in the sildenafil citrate group and **84 of 1625 (5.2%)** in the placebo group.”
  - **PDF p. 4, Figure 1:** the terminal boxes report **1625 infants with primary outcome** in each group.
  - **PDF p. 4, Results—Participants and Adherence:** “The primary end point was available for **3250 infants**.”
  - **PDF p. 6, Results—Primary and Secondary Outcomes:** repeats that the primary outcome occurred in **83 of 1625 women** vs **84 of 1625 women**.
  - **PDF p. 6, same section:** cord-artery pH testing is reported for **1223 of 1629 women** vs **1159 of 1637 women**.
  - **PDF p. 6, Table 2:** identifies **1634 and 1641 neonates**, with infant-level nonmissing denominators of **1629 and 1637**.
  - **PDF p. 7, Table 3:** the primary outcome uses **83/1625** vs **84/1625**, and umbilical cord artery pH <7.0 uses **12/1629** vs **5/1637**; the GEE footnote states adjustment for multiple births.
- **Logical basis:** The article’s flow diagram and Results section explicitly identify the primary-outcome analysis set as 3250 infants (1625 per group). The denominators 1629 and 1637 are likewise neonatal/infant denominators in Table 2 and Table 3. Calling these denominators “women” changes the reported analysis unit and is internally inconsistent with the labeled infant-level analysis.
- **Concise verification instruction:** On DOC-001 PDF pp. 1, 4, 6, and 7, confirm that the same denominators (1625 per group for the primary outcome; 1629/1637 for cord-pH assessment) are labeled as infants/neonates in Figure 1 and the tables but as women in the prose.

## Checked items that passed

1. **Primary estimate, CI, P value, and repeats (DOC-001 pp. 1, 6-7):** RR **1.02** lies within **0.75-1.37**; the CI includes the null value 1 and **P=.91** is nonsignificant. Counts, percentages, RR, and CI repeat consistently in the Abstract, Results, Table 3, and Figure 2.

2. **Table 3 effect direction and CI/P decisions (DOC-001 p. 7):** For all reportable rows, the RR direction agrees with the displayed event rates; every RR lies within its CI; and each CI includes 1 with a corresponding **P>.05**. This includes Apgar <4 (**1.67; 0.40-7.00; P=.48**), cord pH <7 (**2.28; 0.81-6.47; P=.12**), encephalopathy (**0.94; 0.06-14.94; P=.96**), seizures (**1.87; 0.17-20.62; P=.61**), neonatal-unit admission (**0.85; 0.59-1.23; P=.39**), respiratory support (**0.81; 0.53-1.25; P=.35**), pulmonary hypertension (**0.33; 0.03-3.22; P=.34**), meconium aspiration (**1.81; 0.61-5.39; P=.29**), and emergency operative birth for fetal distress (**1.12; 0.98-1.29; P=.10**).

3. **Sensitivity analyses and main/supplement repeats (DOC-001 p. 6; DOC-004 p. 2, eTable 1):** The main-article imputed RR **1.01 (0.75-1.36)** and adjusted RR **0.98 (0.73-1.31)** exactly match eTable 1. All six displayed eTable 1 RRs lie inside their CIs, every CI includes 1, and every P value is nonsignificant (**.943, .276, .796, .937, .882, .844**).

4. **Site-specific primary outcome (DOC-001 pp. 7 and 9; DOC-004 p. 3, eTable 2):** Mater Mother’s Hospital values **16/883 vs 24/887; RR 0.67 (0.36-1.25), P=.209** and other-site values **67/742 vs 60/738; RR 1.11 (0.80-1.55), P=.537** repeat consistently. The main article’s interaction **P=.16** is the correctly rounded presentation of supplement **P=.158**. The discussion’s “33% lower” and “11% higher” descriptions agree with RRs 0.67 and 1.11.

5. **All site-stratified estimates and interaction labels (DOC-004 pp. 3-5, eTable 2):** Displayed point estimates fall within their CIs; directions agree with the two displayed rates; and CI/null decisions agree with the corresponding P values. The two within-site effects with CIs excluding 1—Mater respiratory support **0.30 (0.11-0.80), P=.016** and other-site postpartum hemorrhage **1.63 (1.19-2.24), P=.002**—also have significant interaction P values (**.015** and **.036**, respectively). Outcome and site labels remain consistent across the three-page table.

6. **Borderline rounded result (DOC-004 p. 5, eTable 2):** Other-site spontaneous vaginal birth is **RR 0.91 (0.82-1.00), P=.050**. At printed precision this is not a verifiable contradiction: the article defines significance as two-tailed **P<.05**, and the rounded CI endpoint/P value do not disclose the underlying unrounded values. It was not promoted as a candidate.

7. **Site strata aggregate to overall repeated counts (DOC-001 pp. 7-8, Tables 3-4; DOC-004 pp. 3-5, eTable 2):** Primary outcome **16+67=83** and **24+60=84**; respiratory support **5+32=37** and **17+30=47**; emergency operative birth for fetal distress **169+174=343** and **157+150=307**; spontaneous vaginal birth **494+370=864** and **521+410=931**; postpartum hemorrhage **73+91=164** and **72+56=128**.

8. **Prespecified subgroup reporting (DOC-001 pp. 7-8, Figure 2):** All subgroup RRs lie within their printed CIs, count/rate direction agrees with the RR, and every CI includes 1. The caption’s statement that all treatment-by-subgroup interaction tests were **P>.05** is consistent with the article’s “no evidence of heterogeneity” claim. Subgroup names and yes/no labels match the accompanying Results text.

9. **Tertiary outcomes highlighted in the article (DOC-001 pp. 7-8, Table 4):** Postpartum hemorrhage **164/1621 vs 128/1627**, difference **2.2% (0.2 to 4.3)**, RR **1.29 (1.03-1.60)** has a consistently positive/harm direction and both intervals exclude their respective nulls. Spontaneous vaginal birth **864/1629 vs 931/1637**, difference **-3.8% (-7.3 to -0.4)**, RR **0.93 (0.88-0.99)** is likewise directionally and internally consistent.

10. **Prespecified sildenafil-related side effects (DOC-001 p. 7; DOC-004 p. 6, eTable 3):** The main article’s statement of no significant between-group differences is consistent with all printed Fisher exact P values, whose minimum is **P=.062** for dizziness (0/1552 vs 5/1557). The safety denominators **1552 vs 1557** also reconcile with Figure 1: 1555 placebo-assigned recipients plus 2 sildenafil-assigned participants who received placebo by mistake.

## Methodological caution applied

No candidate was generated from apparent CI symmetry or from reconstructing exact P values from rounded intervals. The reported GEE/log-binomial models and rounding make such properties model-dependent; checks were limited to document-grounded containment, null/significance decisions, directions, repeats, labels, and exact count aggregation.

## Disposition

- **Local candidates returned:** 1
- **Passed check groups:** 10
- **Unsupported or uncertain candidates:** Not promoted
