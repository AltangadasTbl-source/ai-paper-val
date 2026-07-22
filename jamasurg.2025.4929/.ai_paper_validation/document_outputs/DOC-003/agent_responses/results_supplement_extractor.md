# Results-Supplement Evidence Map - DOC-003

## Document disposition

- **Document:** DOC-003 - `soi250075supp2_prod_1767031598.05318.pdf` (3 PDF pages)
- **Inventory class:** Results supplement.
- **Audit range:** all three pages. Page 3 was visually checked using `preprocessing/images/page-003-results-table-180dpi.png`; the page-3 OCR was not used as canonical evidence.
- **Result:** **Audited - result-relevant supplementary evidence extracted.** No protocol, SAP, administrative, author-list, or data-sharing material was audited.

## Source-page map

| PDF page | Section | Extracted evidence / use |
|---:|---|---|
| 1 | Supplemental Online Content | Identifies the parent trial (Dat TQ et al., UMC-UPPERGI-01), the DOI `10.1001/jamasurg.2025.4929`, and the two supplied tables: eTable 1 and eTable 2. |
| 2 | **eTable 1. Inclusion and Exclusion Criteria** | Contextual eligibility evidence supporting the reported analysis population; not an outcome table. |
| 3 | **eTable 2. Univariate and Multivariate Analysis for Predicting Postoperative Morbidity** | Result-relevant regression table. Native text was checked against the rendered page for cell placement, `>=` signs, and CI bounds. |

## eTable 1 - eligibility context (PDF p. 2)

**Inclusion criteria:** age 18-80 years; histologically confirmed gastric adenocarcinoma in the lower or middle third of the stomach; clinical T4aN0-3M0 on preoperative imaging; ECOG performance status 0-1; ASA-PS I-III.

**Exclusion criteria:** pregnancy/breastfeeding; bulky lymph nodes; duodenal invasion; previous gastric surgery; severe tumor-related bleeding or perforation requiring emergency surgery; previous chemotherapy or radiotherapy; neoadjuvant chemotherapy; other malignancy within 5 years; severe conditions contraindicating laparoscopy.

**Cross-document anchor (for later comparison, not an audit conclusion):** DOC-001, PDF p. 2, describes the same eligibility framework and cites eTable 1 in Supplement 2.


## eTable 2 - postoperative morbidity analysis (PDF p. 3)

Column order verified from the rendered page: **Variable; Morbidity n/N (%); Univariate OR (95% CI), P value; Multivariate OR (95% CI), P value.** Statistic is n (%). CI = confidence interval; OR = odds ratio; LDG = laparoscopic distal gastrectomy; ODG = open distal gastrectomy; GOO = gastric outlet obstruction.

| Variable (reference) | Morbidity n/N (%) | Nonreference result: univariate OR (95% CI), P | Multivariate OR (95% CI), P |
|---|---|---|---|
| Age (<60) | 13/88 (14.8) | >=60: 2.28 (1.12-4.64), 0.040 | >=60: 1.70 (0.79-3.65), 0.173 |
| Age (>=60) | 32/120 (27.7) |  |  |
| Sex (male) | 34/154 (22.1) | Female: 0.97 (0.46-2.04), 0.939 | Not displayed |
| Sex (female) | 11/54 (20.4) |  |  |
| Approach (LDG) | 23/104 (22.1) | ODG: 0.85 (0.44-1.63), 0.619 | Not displayed |
| Approach (ODG) | 22/104 (21.2) |  |  |
| BMI <25 kg/m2 | 35/145 (24.1) | >=25: 0.64 (0.30-1.36), 0.183 | Not displayed |
| BMI >=25 kg/m2 | 10/63 (15.9) |  |  |
| Comorbidity (no) | 12/95 (12.6) | Yes: 3.10 (1.50-6.41), 0.004 | Yes: 2.42 (1.11-5.30), 0.026 |
| Comorbidity (yes) | 33/113 (29.2) |  |  |
| ASA 1 | 1/9 (11.1) | ASA 2: 1.97 (0.23-16.8), 0.535; ASA 3: 2.76 (0.33-23.03), 0.348 | Not displayed |
| ASA 2 | 17/86 (19.8) |  |  |
| ASA 3 | 27/113 (23.9) |  |  |
| Tumor size <5 cm | 16/96 (16.7) | >=5 cm: 1.75 (0.88-3.46), 0.110 | >=5 cm: 1.46 (0.71-2.98), 0.300 |
| Tumor size >=5 cm | 29/112 (25.9) |  |  |
| Albumin <35 | 6/25 (24.0) | >=35: 0.86 (0.32-2.29), 0.760 | Not displayed |
| Albumin >=35 | 39/183 (21.3) |  |  |
| Anemia (no) | 27/146 (18.5) | Yes: 1.80 (0.90-3.56), 0.094 | Not displayed |
| Anemia (yes) | 18/62 (29.0) |  |  |
| GOO (no) | 35/148 (23.7) | Yes: 0.65 (0.30-1.41), 0.270 | Yes: 0.69 (0.31-1.54), 0.363 |
| GOO (yes) | 10/60 (16.7) |  |  |
| pT (pT1-pT3) | 12/64 (18.8) | pT4a: 1.29 (0.62-2.70), 0.501 | Not displayed |
| pT (pT4a) | 33/144 (22.9) |  |  |
| pN (N0) | 10/51 (19.6) | N1-2: 0.98 (0.41-2.36), 0.963; N3: 0.431 (0.60-3.37), 0.431 | Not displayed |
| pN (N1-2) | 16/83 (19.3) |  |  |
| pN (N3) | 29/74 (25.7) |  |  |
| Type of anastomosis (Billroth II) | 33/163 (20.2) | Rouxx-En-Y: 1.43 (0.67-3.07), 0.356 | Not displayed |
| Type of anastomosis (Rouxx-En-Y) | 12/45 (26.7) |  |  |

## Table-level anchors for later verification

- Every displayed categorical denominator totals **208** within its variable (including 104 LDG + 104 ODG); every displayed morbidity numerator totals **45** within its variable.
- The treatment-arm morbidity cells are **LDG 23/104 (22.1%)** and **ODG 22/104 (21.2%)**.
- The only visibly populated multivariate rows are age >=60, comorbidity yes, tumor size >=5 cm, and GOO yes. A dash is visually printed in the multivariate area for albumin <35, anemia yes, GOO no, and pN N0; other omitted multivariate cells are blank.
- **Cross-document anchors (not audit conclusions):** DOC-001 PDF p. 1 reports 208 participants (104 per group), 22.1% vs 21.2% any postoperative complication, and comorbidity OR 2.42 (95% CI, 1.11-5.30; P = .03). DOC-001 PDF p. 6 reports comorbidity OR 2.42 (95% CI, 1.11-5.30; P = .03) and approach OR 0.85 (95% CI, 0.44-1.63; P = .62), citing eTable 2 in Supplement 2.

## Extraction limitations

- PDF p. 3 native-text reading order is degraded; its displayed values above were transcribed from the rendered page where a table cell, comparison sign, or confidence-interval bound mattered.
- The OCR derivative (`preprocessing/page-003-ocr.txt`) is noncanonical and was not used to establish evidence.
- This is an evidence extraction only: no inconsistency, diagnosis, or candidate issue is asserted.
