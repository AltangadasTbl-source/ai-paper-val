# Human Adjudication Report

**Status:** Ready for Human Adjudication (submit to human review)
**Scientific issues retained:** 2 of 2 accepted findings; both `Presentation inconsistency`, `Minor`.

## Package audit scope and processing status

| Document ID | Filename | Scientific audit scope / status |
|---|---|---|
| `doc-799606a72443` | `jama_brenner_2019_oi_190039.pdf` | Main article; PDF pp. 1–7 audited. |
| `doc-b45e07a04d82` | `joi190039supp3_prod.pdf` | Results supplement; PDF pp. 4–8 audited. |
| `doc-5143f7e4da1a` | `joi190039supp1_prod.pdf` | Protocol; **Not Audited by Design**. |
| `doc-5704a644014e` | `joi190039supp2_prod.pdf` | Statistical analysis plan; **Not Audited by Design**. |
| `doc-ded78f53da7b` | `joi190039supp4_prod.pdf` | Administrative material; **Not Audited by Design**. |

**Preprocessing record:** All 12 scientifically scoped pages had adequate native text. OCR backend selection was `rapidocr-cpu`; no GPU was selected, and no OCR was required or additionally performed.

**Audit conclusion:** Two minor presentation items require confirmation. No participant-flow issue was retained; all feasible arithmetic and other statistical-consistency checks reconciled. A broad “overall” wording item was uncertain and excluded.

## Scientific issues

### 1. Women’s eTable 5 PPV-difference point estimates are displayed as dashes despite reproducible numeric values

**Category:** Presentation inconsistency  
**Severity:** Minor

**Issue statement:** In the three Women rows of eTable 5, the Difference in PPV point-estimate field displays “-” while the group PPVs, numeric 95% CIs, and matching eTable 4 TP/FP counts support numeric aspirin-minus-placebo differences, leaving the designated reported estimate absent.

**Evidence locations:**

- **Reported field:** `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women rows, **Difference in PPV** column:
  - Quantitative, cutoff 10.2 µg Hb/g.
  - Quantitative, cutoff 17.0 µg Hb/g.
  - Qualitative, cutoff 10.2 µg Hb/g.
- **Comparator inputs:** `doc-b45e07a04d82`, `joi190039supp3_prod.pdf`, PDF p. 6, eTable 4, Women rows at the matching Test and Cutoff values; Aspirin and Placebo **TP** and **FP** columns.

**Reported values (eTable 5, PDF p. 7):**

| Women row | Aspirin PPV | Placebo PPV | Reported Difference in PPV | Reported 95% CI |
|---|---:|---:|---:|---:|
| Quantitative, 10.2 µg Hb/g | 15.9% | 34.1% | “-” | [−34.7, −1.3] |
| Quantitative, 17.0 µg Hb/g | 17.1% | 42.9% | “-” | [−48.4, −0.7] |
| Qualitative, 10.2 µg Hb/g | 9.7% | 31.2% | “-” | [−38.9, −3.9] |

**Comparator values (eTable 4, PDF p. 6):**

| Women row | Aspirin TP, FP (N) | Placebo TP, FP (N) |
|---|---:|---:|
| Quantitative, 10.2 µg Hb/g | 11, 58 | 14, 27 |
| Quantitative, 17.0 µg Hb/g | 6, 29 | 9, 12 |
| Qualitative, 10.2 µg Hb/g | 6, 56 | 10, 22 |

**Direct reported-versus-comparator comparison:** The reported point estimate is “-” in each row; the directly reproducible aspirin-minus-placebo PPV differences are −18.2, −25.7, and −21.6 percentage points, respectively.

**Reproducible calculation:**

Rule:

`PPV difference = [TPaspirin / (TPaspirin + FPaspirin) − TPplacebo / (TPplacebo + FPplacebo)] × 100`

- Quantitative 10.2: `[11/(11+58) − 14/(14+27)] × 100 = −18.204%`, reported-scale result **−18.2 percentage points**.
- Quantitative 17.0: `[6/(6+29) − 9/(9+12)] × 100 = −25.714%`, reported-scale result **−25.7 percentage points**.
- Qualitative 10.2: `[6/(6+56) − 10/(10+22)] × 100 = −21.573%`, reported-scale result **−21.6 percentage points**.

Rounding tolerance: ±0.05 percentage points for one-decimal reporting. A dash is not a numeric point estimate within that tolerance.

**Bounded impact:** This affects only the displayed PPV-difference point estimates for the three Women subgroup rows. The component PPVs and 95% CIs remain printed; no reported total or primary outcome is changed.

**Human verification:**

1. Confirm visually in eTable 5 (PDF p. 7) that each identified Women Difference in PPV field is “-” while its 95% CI is populated.
2. Recalculate PPV in each arm from the cited eTable 4 TP and FP counts and subtract placebo from aspirin.
3. Confirm the calculations produce −18.2, −25.7, and −21.6 percentage points after one-decimal rounding while those digits are absent on p. 7.
4. Check the production table or correction record; a documented alternative reporting convention that explains the dashes would resolve the presentation question.

### 2. Table 3 omits the Test label in the third Men row

**Category:** Presentation inconsistency  
**Severity:** Minor

**Issue statement:** The third Men row in Table 3 has a blank Test cell although its cutoff and four predictive values exactly map to the Men—Qualitative row in Table 2, making the row’s test identity ambiguous within Table 3.

**Evidence locations:**

- **Reported blank label and values:** `doc-799606a72443`, `jama_brenner_2019_oi_190039.pdf`, PDF p. 5, Table 3, Men, third data row, **Test** column (blank), cutoff **10.2 µg Hb/g**; Aspirin and Placebo PPV/NPV columns and Difference columns. Table 3 footnote `a`: “Results of the intention-to-screen analysis.”
- **Comparator label and counts:** `doc-799606a72443`, `jama_brenner_2019_oi_190039.pdf`, PDF p. 5, Table 2, Men, **Qualitative** row, cutoff **10.2 µg Hb/g**; Aspirin and Placebo TP, FN, TN, and FP columns.

**Reported values (Table 3, PDF p. 5):**

- Test: **blank**.
- Aspirin: PPV **27.5%**; NPV **89.2%**.
- Placebo: PPV **20%**; NPV **90.3%**.
- Difference in PPV: **7.5** (95% CI, **−6.4 to 20.2**).
- Difference in NPV: **−1.1** (95% CI, **−5.3 to 3.0**).

**Comparator values (Table 2, PDF p. 5):**

- Men, **Qualitative**, 10.2 µg Hb/g:
  - Aspirin: TP **28**, FN **43**, TN **354**, FP **74**.
  - Placebo: TP **12**, FN **43**, TN **400**, FP **48**.

**Direct reported-versus-comparator comparison:** The Table 3 Test field is blank, whereas Table 2 identifies the matching row as **Qualitative**. All four Table 3 predictive values match those calculated from the Table 2 Men–Qualitative counts.

**Reproducible calculation:**

Rules:

`PPV = TP / (TP + FP) × 100`  
`NPV = TN / (TN + FN) × 100`

- Aspirin PPV: `28/(28+74) × 100 = 27.45098%` → **27.5%**.
- Aspirin NPV: `354/(354+43) × 100 = 89.16877%` → **89.2%**.
- Placebo PPV: `12/(12+48) × 100 = 20.0%` → **20%**.
- Placebo NPV: `400/(400+43) × 100 = 90.29345%` → **90.3%**.
- Displayed differences are also reproduced: `27.5 − 20.0 = 7.5` percentage points and `89.2 − 90.3 = −1.1` percentage points.

Rounding tolerance: ±0.05 percentage points for one-decimal values; all displayed values agree within tolerance.

**Bounded impact:** This affects only the Test label for one male subgroup predictive-value row. It does not alter the printed PPV/NPV values, confidence intervals, or any reported total.

**Human verification:**

1. Confirm visually that the Test cell is blank in the third Men row of Table 3 (PDF p. 5).
2. Confirm the cutoff and PPV/NPV values above and that corresponding third rows elsewhere are labeled `Qualitative`.
3. Recalculate the four predictive values from the cited Table 2 Men–Qualitative TP/FN/TN/FP counts.
4. Confirm the issue if the numbers identify the qualitative comparison while the Table 3 row label remains absent; a published correction identifying a different intended label would resolve it.

## AI Training Restriction Summary

This is a document-level compliance screen, not a scientific-issue category and not a legal opinion. All records concern supplied PDFs and embedded metadata only. Silence is not permission.

| Document ID and filename | Status | Exact evidence location and excerpt/result | Human Compliance Review |
|---|---|---|---|
| `doc-799606a72443` — `jama_brenner_2019_oi_190039.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1–7, repeated footer: “© 2019 American Medical Association. All rights reserved.” The footer does not expressly mention AI training, fine-tuning, model improvement, or a permission requirement for those uses. Embedded metadata also screened. | No |
| `doc-5143f7e4da1a` — `joi190039supp1_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 and repeated headers: “(CONFIDENTIAL)”; PDF p. 36, §9.7 Confidentiality: “For protection of these data, organizational procedures are implemented to prevent distribution of data to unauthorized persons.” PDF p. 38, §9.11 Data collection/List of participants: “The identity of the participants will not be revealed to unauthorized persons.” These are confidentiality/disclosure provisions, not AI-training restrictions. | No |
| `doc-5704a644014e` — `joi190039supp2_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, pp. 2–9, p. 10, and embedded PDF/XMP metadata: no qualifying rights, permissions, license, terms, text-and-data-mining, or AI-training language was located. | No |
| `doc-b45e07a04d82` — `joi190039supp3_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1, pp. 2–8, and embedded XMP metadata: no statement addressing AI training, fine-tuning, or model improvement was located; no verbatim qualifying restriction is available. | No |
| `doc-ded78f53da7b` — `joi190039supp4_prod.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1: “Trial protocol: Published as open access publication:”. This rights-adjacent statement concerns a separately published protocol and is not a license, AI-use permission, or AI-training restriction for this supplement. Embedded metadata screened. | No |
