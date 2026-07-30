# Figure, Flow, and Visible-Table Check

## Scope

- Main article: `doc-799606a72443`, `jama_brenner_2019_oi_190039.pdf`, PDF pages 1–7.
- Results supplement: `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF pages 4–8.
- Inspected source-derived renderings: main-article Figure on PDF page 4 and supplement eTables 2–6 on PDF pages 4–8.
- Protocol, SAP, and administrative documents were not opened.

## Candidate 1

**Issue statement:** In all three Women rows of per-protocol eTable 5, the visible `Difference in PPV [95% CI]` point-estimate cell contains only a minus sign; the omitted magnitudes are reproducibly −18.2, −25.7, and −21.6 percentage points.

- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Confidence:** High

### Exact locations and visible evidence

1. `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF page 7, eTable 5, Women / Quantitative / cutoff 10.2 µg Hb/g row:
   - Aspirin PPV: `15.9`
   - Placebo PPV: `34.1`
   - Visible Difference in PPV point estimate: `-`
   - Visible 95% CI: `[-34.7, -1.3]`
2. Same document/page/table, Women / Quantitative / cutoff 17.0 µg Hb/g row:
   - Aspirin PPV: `17.1`
   - Placebo PPV: `42.9`
   - Visible Difference in PPV point estimate: `-`
   - Visible 95% CI: `[-48.4, -0.7]`
3. Same document/page/table, Women / Qualitative / cutoff 10.2 µg Hb/g row:
   - Aspirin PPV: `9.7`
   - Placebo PPV: `31.2`
   - Visible Difference in PPV point estimate: `-`
   - Visible 95% CI: `[-38.9, -3.9]`
4. Comparator counts are in `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF page 6, eTable 4, the corresponding Women rows:
   - Quantitative 10.2: aspirin `TP 11`, `FP 58`; placebo `TP 14`, `FP 27`.
   - Quantitative 17.0: aspirin `TP 6`, `FP 29`; placebo `TP 9`, `FP 12`.
   - Qualitative 10.2: aspirin `TP 6`, `FP 56`; placebo `TP 10`, `FP 22`.

### Reproducible comparison

Rule: `PPV = TP / (TP + FP) × 100`; reported difference is aspirin PPV minus placebo PPV.

1. Quantitative 10.2:
   - Aspirin: `11 / (11 + 58) × 100 = 15.942%`.
   - Placebo: `14 / (14 + 27) × 100 = 34.146%`.
   - Difference: `15.942 − 34.146 = −18.204` percentage points, which rounds to **−18.2**.
2. Quantitative 17.0:
   - Aspirin: `6 / (6 + 29) × 100 = 17.143%`.
   - Placebo: `9 / (9 + 12) × 100 = 42.857%`.
   - Difference: `17.143 − 42.857 = −25.714` percentage points, which rounds to **−25.7**.
3. Qualitative 10.2:
   - Aspirin: `6 / (6 + 56) × 100 = 9.677%`.
   - Placebo: `10 / (10 + 22) × 100 = 31.250%`.
   - Difference: `9.677 − 31.250 = −21.573` percentage points, which rounds to **−21.6**.

**Rounding tolerance:** ±0.05 percentage point for values reported to 1 decimal place. The calculations use the integer counts in eTable 4, avoiding subtraction artifacts from independently rounded PPVs in eTable 5.

### Bounded impact

The defect omits the magnitudes of all three women-specific per-protocol PPV differences from the visible point-estimate column. It does not alter the displayed group PPVs or 95% CIs, and it does not affect participant totals or the primary sensitivity outcome.

### Human verification steps

1. Open supplement PDF page 7 and inspect eTable 5, Women rows, `Difference in PPV [95% CI]`.
2. Confirm that each point-estimate cell visibly shows only `-`, followed by a complete negative 95% CI.
3. Open supplement PDF page 6, eTable 4, and verify the corresponding TP and FP counts listed above.
4. Apply `TP / (TP + FP) × 100` to both groups and subtract placebo from aspirin.
5. The issue is confirmed if the recovered one-decimal differences are −18.2, −25.7, and −21.6 while those magnitudes are absent from the visible eTable 5 cells. It is resolved only if another authoritative rendering of the supplied PDF visibly contains those magnitudes in the proper cells.

## Recruitment-flow reconciliation (no candidate issue)

`doc-799606a72443`, `jama_brenner_2019_oi_190039.pdf`, PDF page 4, Figure:

- `1208 + 1214 = 2422` randomized.
- Aspirin: `1131 + 77 = 1208`; placebo: `1153 + 61 = 1214`.
- Aspirin colonoscopy flow: `1075 + 56 = 1131`; placebo: `1059 + 94 = 1153`.
- Aspirin primary-analysis exclusion reasons: `32 + 2 + 20 + 2 = 56`.
- Placebo primary-analysis exclusion reasons: `56 + 30 + 5 + 3 = 94`.
- Analyzed total: `1075 + 1059 = 2134`.
- Total not analyzed: `77 + 61 + 56 + 94 = 288`; `2422 − 2134 = 288`, matching the Results text on PDF page 3: “From 2422 recruited participants, 288 dropped out or were excluded … leaving 2134 participants for the analysis.”

No other material, high-confidence figure/flow/visible-table candidate was identified in the assigned pages.
