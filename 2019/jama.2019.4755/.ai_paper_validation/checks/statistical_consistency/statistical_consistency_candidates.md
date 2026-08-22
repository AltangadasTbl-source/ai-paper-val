# Statistical consistency check

## Scope and disposition

- Main article: `doc-799606a72443`, `jama_brenner_2019_oi_190039.pdf`, PDF pages 1-7, using `main_article_evidence_inventory.json` and its page-linked text/rendered tables.
- Results supplement: `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, result-relevant PDF pages 4-8, using `results_supplement_evidence_map.json` and its page-linked text/rendered tables.
- Protocol, SAP, administrative material, and external sources were not used.
- Two local candidates were retained. Both are visible table-presentation defects. No contradictory point estimate/CI/P-value relationship was found in the reported primary-outcome results.

## Candidate 1 — Three women's PPV difference point estimates are absent although their CIs are printed

**Priority:** 1  
**Category:** Presentation inconsistency  
**Severity:** Minor  
**Status:** Candidate for evidence verification

**One-sentence issue statement:** In the per-protocol supplement table, all three Women rows omit the numerical PPV difference and show only a minus sign, even though the component PPVs and corresponding 95% CIs are reported and support differences of approximately −18.2, −25.7, and −21.6 percentage points.

### Exact evidence

1. **Reported item:** `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women rows, “Difference in PPV [95% CI]” column.
   - Quantitative, cutoff 10.2 µg Hb/g: aspirin PPV `15.9`, placebo PPV `34.1`, displayed point estimate `-` (minus sign only), 95% CI `[-34.7, -1.3]`.
   - Quantitative, cutoff 17.0 µg Hb/g: aspirin PPV `17.1`, placebo PPV `42.9`, displayed point estimate `-` (minus sign only), 95% CI `[-48.4, -0.7]`.
   - Qualitative, cutoff 10.2 µg Hb/g: aspirin PPV `9.7`, placebo PPV `31.2`, displayed point estimate `-` (minus sign only), 95% CI `[-38.9, -3.9]`.
2. **Comparator counts:** `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF p. 6, eTable 4, corresponding per-protocol Women rows:
   - Quantitative 10.2: aspirin TP/FP `11/58`; placebo TP/FP `14/27`.
   - Quantitative 17.0: aspirin TP/FP `6/29`; placebo TP/FP `9/12`.
   - Qualitative 10.2: aspirin TP/FP `6/56`; placebo TP/FP `10/22`.

### Reproducible comparison

Rule: `PPV = TP / (TP + FP) × 100`; table difference is aspirin minus placebo, in percentage points.

1. Quantitative 10.2:
   - Aspirin: `11/(11+58)×100 = 15.942%`.
   - Placebo: `14/(14+27)×100 = 34.146%`.
   - Difference: `15.942 − 34.146 = −18.204` percentage points, expected display `−18.2`.
2. Quantitative 17.0:
   - Aspirin: `6/(6+29)×100 = 17.143%`.
   - Placebo: `9/(9+12)×100 = 42.857%`.
   - Difference: `17.143 − 42.857 = −25.714` percentage points, expected display `−25.7`.
3. Qualitative 10.2:
   - Aspirin: `6/(6+56)×100 = 9.677%`.
   - Placebo: `10/(10+22)×100 = 31.250%`.
   - Difference: `9.677 − 31.250 = −21.573` percentage points, expected display `−21.6`.

**Tolerance:** ±0.1 percentage point for the table's one-decimal rounding. The missing digits cannot be explained by rounding. Each derived point estimate lies within its printed CI and has the same negative direction, so the issue is omission of the point estimate rather than a CI-direction contradiction.

**Bounded impact:** The defect affects the displayed point estimates for three exploratory Women-subgroup PPV comparisons in the per-protocol analysis. It does not alter the printed component PPVs or CIs and does not affect the prespecified primary outcomes.

### Human verification steps

1. Open supplement PDF p. 7 and inspect the three Women cells under “Difference in PPV”; confirm that only a minus sign is visible and no digits appear.
2. Open supplement PDF p. 6, eTable 4, and verify the corresponding TP and FP counts listed above.
3. Recalculate each PPV and aspirin-minus-placebo difference using the stated formula.
4. **Confirm** the issue if the source PDF visibly lacks `18.2`, `25.7`, and `21.6` after the minus signs. **Resolve** it if higher-fidelity rendering shows those digits in the cells.

## Candidate 2 — The Men qualitative PPV/NPV row lacks its test label

**Priority:** 2  
**Category:** Presentation inconsistency  
**Severity:** Minor  
**Status:** Candidate for evidence verification

**One-sentence issue statement:** In main-article Table 3, the third Men row reports the qualitative-test PPV/NPV results but its Test cell is blank, leaving the subgroup row unlabeled.

### Exact evidence

1. **Reported item:** `doc-799606a72443`, `jama_brenner_2019_oi_190039.pdf`, PDF p. 5, Table 3, Men subgroup, third row.
   - Test cell: blank.
   - Cutoff: `10.2 µg Hb/g`.
   - Aspirin: PPV `27.5`, NPV `89.2`.
   - Placebo: PPV `20`, NPV `90.3`.
   - PPV difference `7.5 (95% CI, −6.4 to 20.2)`.
   - NPV difference `−1.1 (95% CI, −5.3 to 3.0)`.
2. **Label comparator:** same document and table:
   - All-participants third row is explicitly labeled `Qualitative`, cutoff `10.2`.
   - Women third row is explicitly labeled `Qualitative`, cutoff `10.2`.
3. **Count comparator:** `doc-799606a72443`, same PDF p. 5, Table 2, Men—Qualitative, cutoff 10.2 row:
   - Aspirin TP/FN/TN/FP `28/43/354/74`.
   - Placebo TP/FN/TN/FP `12/43/400/48`.

### Reproducible comparison

Rules: `PPV = TP/(TP+FP)×100`; `NPV = TN/(TN+FN)×100`.

- Aspirin PPV: `28/(28+74)×100 = 27.451% → 27.5%`.
- Aspirin NPV: `354/(354+43)×100 = 89.169% → 89.2%`.
- Placebo PPV: `12/(12+48)×100 = 20.000% → 20.0%`.
- Placebo NPV: `400/(400+43)×100 = 90.293% → 90.3%`.

These four recalculations uniquely reproduce the unlabeled Table 3 row from the Table 2 Men—Qualitative counts.

**Tolerance:** ±0.1 percentage point for one-decimal rounding. All values match within tolerance; the inconsistency is the missing subgroup row label, not the numerical values.

**Bounded impact:** Readers can infer the row from table order and arithmetic, but the test identity is not explicitly reported for one exploratory Men-subgroup row. No primary-outcome value is affected.

### Human verification steps

1. Open main-article PDF p. 5, Table 3, Men third row and confirm the Test cell is blank.
2. Compare the corresponding third rows for All participants and Women, both labeled `Qualitative`.
3. Use the Men—Qualitative counts in Table 2 to reproduce the four Table 3 predictive values.
4. **Confirm** the issue if the source PDF has no `Qualitative` label in that cell. **Resolve** it if a higher-fidelity source shows a label obscured in the supplied rendering.

## Checks completed without a retained candidate

- All main Table 2 and supplement eTables 3-4 sensitivities and specificities were checked against `TP/(TP+FN)` and `TN/(TN+FP)`; reported percentages and aspirin-minus-placebo directions were compatible with one-decimal rounding.
- The main primary estimates and CIs agree across Abstract, Results, and Table 2: `9.8 (−3.1 to 22.2), P=.14` at 10.2 µg Hb/g and `6.0 (−5.7 to 17.5), P=.32` at 17.0 µg Hb/g. Both CIs include the null and both P values exceed .05.
- The qualitative secondary sensitivity result `12.7 (0.1 to 24.7), P=.048` has a CI excluding zero and P below .05; the specificity results likewise have compatible CI/null/P-value directions.
- Main-text claims about increased sensitivity/lower specificity with up to three samples match supplement eTable 3 directions. The per-protocol Men sensitivity differences quoted in the main text (`23.2 [5.0 to 39.5]` and `22.5 [4.5 to 38.6]`) exactly match eTable 4.
- The reported site-effect P-value range `.16 to .50` matches eTable 6. Repeated `.50` values were not treated as errors because the supplied table reports boundary estimates and no document-grounded rule establishes that repetition as invalid.
- CI symmetry was not used as a diagnostic because the article reports Agresti-Coull/Agresti-Caffo methods.
- The statement “Overall, no significant differences were seen” for PPV/NPV was not retained as contradictory: the All-participants PPV/NPV CIs in main Table 3 and supplement eTable 5 all include zero; subgroup intervals do not establish a contradiction with an overall-population claim.
