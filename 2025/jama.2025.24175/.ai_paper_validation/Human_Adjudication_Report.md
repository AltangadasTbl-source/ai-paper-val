# Human Adjudication Report — ImmunoSep

## Scope and status

This package-level review used only the supplied PDFs. Scientific auditing covered DOC-001 (main article, PDF pages 1-12) and DOC-003 (results supplement, PDF pages 1, 6, and 14-53). DOC-002 (protocol/SAP), DOC-004 (collaborators), and DOC-005 (data sharing) were **Not Audited by Design**. The six findings below survived independent source verification and critic review. They require human adjudication; they do not establish the intended corrected values where underlying outputs are unavailable.

## Findings for human adjudication

### 1. Day-15 SOFA responder count differs between narrative and tables

- **Category / severity:** Presentation inconsistency / Minor.
- **Locations and evidence:** DOC-001, `jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf`, PDF p7, Secondary End Points: “39.7%; 51 of 131.” DOC-001 PDF p6, Table 2, “≥1.4-Point decrease of mean SOFA score d 2 to 15”: “52/131 (39.7).” DOC-003, `joi250116supp2_prod_1771885794.27755.pdf`, PDF p22, eTable 10: MALS 12/25 and SII 40/106.
- **Comparison and calculation:** 12 + 40 = 52 and 25 + 106 = 131; 52/131 = 39.69%, which rounds to 39.7%. In contrast, 51/131 = 38.93%, or 38.9%.
- **Bounded impact:** The narrative understates the responder numerator by one and pairs 51 with the percentage for 52; the tabulated effect estimate and inference are not otherwise challenged.
- **Human verification:** Compare DOC-001 pp6-7, then sum the two DOC-003 p22 subgroup counts. Confirm whether the source data support 52/131.

### 2. eTable 10 unadjusted odds ratio does not reproduce from its counts

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Location and evidence:** DOC-003 PDF p22, eTable 10, day-15 SOFA response, sepsis-induced immunoparalysis: precision immunotherapy 40/106 (37.7%), placebo 29/122 (23.8%), printed unadjusted OR 1.194 (95% CI, 1.09-3.45), P=.030.
- **Calculation:** non-events are 66 and 93; OR = (40/66) / (29/93) = (40 × 93) / (66 × 29) = 1.944, or 1.94. A conventional log-OR CI is approximately 1.10-3.45, compatible with the displayed CI after rounding; ordinary rounding cannot yield 1.194.
- **Bounded impact:** The point estimate understates the count-derived OR, though its direction, CI exclusion of 1, and stated significance are unchanged.
- **Human verification:** Recompute the cross-product OR from the four counts and inspect the table’s analysis specification/model output.

### 3. eFigure 9 reports an OR outside its reported confidence interval

- **Category / severity:** Statistical reporting inconsistency / Uncertain.
- **Location and evidence:** DOC-003 PDF p53, eFigure 9B, “APACHE II ≥25 × Precision Immunotherapy”: OR 0.11; 95% CI 0.36-3.42; P=.86.
- **Logical check:** 0.11 is below the lower CI bound 0.36. At the shown precision, rounding cannot reconcile this. The package cannot determine whether the OR, CI, or pairing is incorrect.
- **Bounded impact:** This interaction magnitude cannot be interpreted reliably as printed; the CI and P value indicate no clear interaction, but the correct estimate is unavailable.
- **Human verification:** Read the printed row, then consult the underlying regression/figure output to confirm a matched OR and CI.

### 4. eFigure 8B duplicates eFigure 7B statistics despite a different outcome

- **Category / severity:** Statistical reporting inconsistency / Major.
- **Locations and evidence:** DOC-003 PDF p51, eFigure 7B (primary endpoint), and PDF p52, eFigure 8B (28-day mortality), print the same six OR/CI/P triplets: 0.47 (0.30-1.62), P=.70; 1.85 (0.66-5.19), P=.24; 0.22 (0.09-0.53), P=.001; 5.79 (2.34-15.05), P<.0001; 0.56 (0.27-1.19), P=.13; and 3.08 (1.37-6.96), P=.007.
- **Comparator calculation:** From eFigure 8A high-stratum mortality counts, simple precision-versus-placebo ORs are APACHE II ≥25: (22 × 13)/(16 × 27) = 0.66; CCI ≥5: (24 × 26)/(30 × 50) = 0.42; and SOFA ≥10: (35 × 20)/(32 × 48) = 0.46. These do not replace model interaction terms, but they show that the copied values do not describe the displayed mortality comparisons.
- **Bounded impact:** eFigure 8B subgroup/interaction results are unreliable as displayed; the correct mortality-model output cannot be recovered from the package.
- **Human verification:** Compare every p51/p52 triplet, recalculate the three eFigure 8A simple ORs, and check the original 28-day mortality model output and figure source.

### 5. Table 2 reverses the difference direction for 28-day mortality

- **Category / severity:** Presentation inconsistency / Minor.
- **Location and evidence:** DOC-001 PDF p6, Table 2, 28-day mortality: precision immunotherapy 57/131 (43.5%), placebo 72/145 (49.7%), difference +6.1% (95% CI, −5.6 to 17.6), OR 0.78. The adjacent 90-day row follows the displayed precision-minus-placebo ordering.
- **Calculation:** 100 × (57/131 − 72/145) = −6.1437%, or −6.1%. The printed +6.1% is placebo minus precision; its CI direction would correspondingly be approximately −17.6% to 5.6% under precision-minus-placebo.
- **Bounded impact:** The sign reverses the observed risk-difference direction, although the CI includes zero and OR/P=.34 still indicate no statistically significant difference.
- **Human verification:** Recalculate both displayed mortality percentages, apply the table’s column order, and check whether a footnote defines an alternative contrast for this row.

### 6. The abstract attaches the patient-incidence percentage to an event count

- **Category / severity:** Presentation inconsistency / Minor.
- **Locations and evidence:** DOC-001 PDF p1, Abstract Results: “A total of 1069 serious treatment-emergent adverse events (88.8%) were reported.” DOC-001 PDF p8, Adverse Events: “1069 … events were reported in 245 patients (88.8%).” DOC-003 PDF p27, eTable 13, Any SAE total: 245 (88.8), total N=276.
- **Calculation:** 245/276 = 88.77%, rounding to 88.8%. No supplied denominator makes 1069 events equal 88.8%.
- **Bounded impact:** The abstract conflates event count with patient incidence. The body and supplement make the intended patient-incidence denominator recoverable.
- **Human verification:** Compare the abstract with DOC-001 p8 and eTable 13; confirm that 88.8% refers to 245/276 patients.

## AI Training Restriction Summary

This document-rights screen is separate from the scientific issues and is not legal advice. The user authorized this investigation; an explicit restriction is still recorded as a Human Compliance Review flag.

| Document | Status | Exact location and evidence | Human Compliance Review |
|---|---|---|---|
| DOC-001 — main article | Explicit AI Training Restriction | PDF pp1-12 footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| DOC-002 — protocol/SAP | No AI Training Restriction Located in Provided Materials | Screened PDF pp1, 60-63, 72 and embedded metadata; no AI-training, fine-tuning, model-improvement, rights, or license language located. | No |
| DOC-003 — results supplement | Explicit AI Training Restriction | PDF p1 (repeated through p54) footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| DOC-004 — collaborators | No AI Training Restriction Located in Provided Materials | Screened PDF pp1, 27-28 and embedded metadata; no relevant rights language located. | No |
| DOC-005 — data sharing | No AI Training Restriction Located in Provided Materials | PDF p1: “Data will be available to researchers on request subject to Sponsor restrictions.” This governs data access and does not mention AI training. | No |

## Human adjudication disposition

**Pending Human Adjudication.** The review rejected two visually apparent but non-material formatting candidates (a localized terminology slip in eFigure 6 and two readily recoverable malformed eTable 14 cells). No finding asserts misconduct, raw-data validity, or an unprovided correction.
