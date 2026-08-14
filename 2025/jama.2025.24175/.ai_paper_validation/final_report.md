# Human Adjudication Report — ImmunoSep

**Status:** Pending Human Adjudication. This is a source-verification report, not a legal opinion. It uses only the five supplied PDFs. The locked workflow record contains five critic-retained **Verified** findings (items 1, 2, 4, 5, and 6), one **Uncertain** candidate (item 3), and two **Rejected** interpretations (A and B). No intended corrected value is inferred where the underlying analysis or figure-production output is absent.

## Package Manifest

| Source file | Inventory classification and scientific-audit status | SHA-256 |
|---|---|---|
| [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1) | Main article, 12 PDF pages; audited, PDF pp. 1-12 (journal pp. 775-786). | `197405b4717695cdc5f5b4a1b3823ff9cb47944041e808c8bbb1aa2546a43997` |
| [joi250116supp1_prod_1771885794.26255.pdf](../joi250116supp1_prod_1771885794.26255.pdf#page=1) | Protocol/SAP, 72 PDF pages; **Not Audited by Design** for scientific findings. | `46cc7ea5932e0a2aaa165425b30a737b98dc777822bd807dc2ffc2306012856e` |
| [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=1) | Results supplement, 54 PDF pages; recorded approved scope PDF p. 1, p. 6, and pp. 14-53. | `7a5058b20633e3361eb1911ee788d2c0949ffcd8dbc79cf68fce742761378154` |
| [joi250116supp3_prod_1771885794.28255.pdf](../joi250116supp3_prod_1771885794.28255.pdf#page=1) | Administrative nonauthor-collaborator list, 28 PDF pages; **Not Audited by Design**. | `cb722d19135061073dd3211ffb94c9d138507c4a2752c3d0764dd4d31657921a` |
| [joi250116supp4_prod_1771885794.28755.pdf](../joi250116supp4_prod_1771885794.28755.pdf#page=1) | Administrative data-sharing statement, 1 PDF page; **Not Audited by Design**. | `634710264d9263b5124f6e76eb861a22eb4da136546bf24a36f73ad57d09bab3` |

The listed hashes were recomputed and match the recorded package hashes. Source PDFs were not modified.

## AI Training Restriction Summary

This separate screen concerns only supplied-file language and is not a legal opinion.

| Document | Status | Exact evidence location and quotation/value | Human Compliance Review |
|---|---|---|---|
| [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1) | Explicit AI Training Restriction | PDF p. 1 footer, repeated pp. 2-12: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| [joi250116supp1_prod_1771885794.26255.pdf](../joi250116supp1_prod_1771885794.26255.pdf#page=1) | No AI Training Restriction Located in Provided Materials | PDF pp. 1, 60-63, and 72 and embedded document-information metadata screened; no applicable AI-training, fine-tuning, model-improvement, rights, or license wording located. Silence is not permission. | No |
| [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=1) | Explicit AI Training Restriction | PDF p. 1 footer (also recorded on the final numbered content page, PDF p. 53): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes |
| [joi250116supp3_prod_1771885794.28255.pdf](../joi250116supp3_prod_1771885794.28255.pdf#page=1) | No AI Training Restriction Located in Provided Materials | PDF p. 1; pp. 27-28; embedded XMP metadata screened. No document-use statement on AI training, fine-tuning, or model improvement was located. | No |
| [joi250116supp4_prod_1771885794.28755.pdf](../joi250116supp4_prod_1771885794.28755.pdf#page=1) | No AI Training Restriction Located in Provided Materials | PDF p. 1, “Additional Information”: “Data will be available to researchers on request subject to Sponsor restrictions.” The complete page and metadata were screened; the data-access statement does not address AI training. | No |

## Audit Method and Revision Status

The report preserves the completed verifier and critic decisions. It rechecked the cited table cells, narrative paragraphs, figure panels, footnotes, and arithmetic against retained native text and page images. Observations are labelled **direct source evidence**; recomputations are **diagnostic calculations**, not replacement model estimates. Rounding is assessed to the precision printed in the sources.

**OCR completion record.** The later GPU OCR record reports **47/47 in-scope rendered pages** completed with rapidocr-cuda on an NVIDIA GeForce RTX 5070 Laptop GPU (8151 MiB; driver 610.88). Detector, classifier, and recognizer used `CUDAExecutionProvider` as primary provider, with `CPUExecutionProvider` listed second. Retained source images control any ambiguous OCR reading.

**Report-record exceptions requiring Human Adjudication.**

1. Standalone historical `package_manifest`, `candidate_set`, checker-output, verifier-output, critic-output, and prior `final_report` files were absent. This draft therefore relies on the surviving [Human_Adjudication_Report.md](Human_Adjudication_Report.md), document records, retained preprocessing artifacts, and the completed handoffs supplied to the reporting task.
2. The compact surviving wording says “six findings … survived”; item 3 is specifically labelled **Uncertain**. This draft preserves the specific disposition and reports five Verified findings plus one Uncertain candidate.
3. The preprocessing page manifest includes results-supplement PDF pp. 7-13, whereas the recorded approved scope is p. 1, p. 6, and pp. 14-53. This is a record-scope discrepancy only; it is disclosed without changing the manifest or audit scope.
4. Items A and B are described as rejected interpretations, but no formal candidate identifiers, categories, or severities survive. None are invented here.

## Candidate Disposition Summary

| Candidate | Disposition | Category | Severity |
|---|---|---|---|
| 1. Day-15 SOFA narrative/table numerator mismatch | Verified; critic retained | Presentation inconsistency | Minor |
| 2. eTable 10 unadjusted OR does not reproduce from printed counts | Verified; critic retained | Statistical reporting inconsistency | Minor |
| 3. eFigure 9 OR outside printed confidence interval | Uncertain | Statistical reporting inconsistency | Potential severity not separately assigned in surviving record |
| 4. eFigure 8B duplicates eFigure 7B statistics despite different outcome | Verified; critic retained | Statistical reporting inconsistency | Major |
| 5. Table 2 reverses the displayed direction of the 28-day mortality difference | Verified; critic retained | Presentation inconsistency | Minor |
| 6. Abstract attaches patient-incidence percentage to event count | Verified; critic retained | Presentation inconsistency | Minor |
| A. Localized terminology slip in eFigure 6 | Rejected | Not retained in surviving record | Not retained in surviving record |
| B. Two recoverable malformed eTable 14 cells | Rejected | Not retained in surviving record | Not retained in surviving record |

## Verified Scientific Findings

### 1 — Day-15 SOFA responder numerator differs between narrative and tables

**Issue statement.** The day-15 SOFA narrative prints 51/131 with 39.7%, whereas the main table and subgroup counts support 52/131 (39.7%); this matters because the narrative numerator and its displayed percentage do not reconcile.

**Category / severity / evidence status.** Presentation inconsistency / Minor / Verified; critic retained.

**Direct source evidence.**

- **Narrative:** [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7), PDF p. 7, journal p. 781, Results—“Secondary End Points,” fourth endpoint: “(39.7%; **51 of 131**)” for precision immunotherapy; placebo: “(23.4%; 34 of 145; P = .004).”
- **Table comparator:** [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), PDF p. 6, journal p. 780, Table 2, “Main secondary outcomes,” row “≥1.4-Point decrease of mean SOFA score d 2 to 15,” Precision immunotherapy column: **52/131 (39.7)**; Placebo column: 34/145 (23.4); Difference column: 16.3 (5.3 to 26.8); OR column: 2.15 (1.28 to 3.61); P value: .004.
- **Subgroup comparator:** [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=22), PDF p. 22 (printed page 22), eTable 10, day-15 SOFA row: macrophage activation-like syndrome 12/25 and sepsis-induced immunoparalysis 40/106 in the precision-immunotherapy column.

**Direct comparison and diagnostic calculation.** Reported narrative numerator = 51; table comparator = 52; discrepancy = **narrative is lower by 1 patient**. eTable 10: 12 + 40 = **52**; denominators 25 + 106 = **131**. `52 ÷ 131 × 100 = 39.6947%`, which rounds to **39.7%** at one decimal. `51 ÷ 131 × 100 = 38.9313%`, which rounds to **38.9%**, not 39.7%. A ±0.05 percentage-point tolerance for one-decimal rounding does not bridge 38.93% to 39.7%.

**Existing supported conclusion.** The locked finding is a one-patient narrative/table presentation mismatch; the reported 39.7% agrees with 52/131.

**Bounded impact and limitation.** Confirmation is needed for the narrative responder numerator. This card does not alter the tabled effect estimate, CI, OR, or P value, and does not identify a corrected narrative version beyond the displayed reconciliation.

**Verification instruction.**

1. Read the cited Table 2 row and the cited Results paragraph. Confirmation requires observing 52/131 (39.7) in Table 2 and 51/131 (39.7%) in the narrative.
2. Add the two precision-immunotherapy eTable 10 day-15 counts. A sum of 52 with denominator 131 confirms the reported comparator; a source-data record supporting 51 would resolve the discrepancy differently.

### 2 — eTable 10 unadjusted OR does not reproduce from printed counts

**Issue statement.** In the day-15 sepsis-induced-immunoparalysis row, eTable 10 prints an unadjusted OR of 1.194, but the four printed counts yield a cross-product OR of about 1.94; this matters because the point estimate cannot be reproduced by ordinary rounding.

**Category / severity / evidence status.** Statistical reporting inconsistency / Minor / Verified; critic retained.

**Direct source evidence.** [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=22), PDF p. 22 (printed page 22), eTable 10, row “Sepsis-induced immunoparalysis” under “≥1.4-point decrease of mean SOFA of days 2 to 15”: Precision immunotherapy **40/106 (37.7)**; placebo **29/122 (23.8)**; Difference **13.9 (1.9 to 25.6)**; `ORunadjusted (95% CI)` **1.194 (1.09 to 3.45)**; P value **.030**.

**Direct comparison and diagnostic calculation.** Nonresponders are `106 − 40 = 66` and `122 − 29 = 93`. For the table’s labelled **unadjusted** odds ratio, the count-derived cross-product is `(40/66) ÷ (29/93) = (40 × 93) ÷ (66 × 29) = 3720 ÷ 1914 = 1.9436`, or **1.94** to two decimals. Reported value = **1.194**; comparator = **1.94**; discrepancy = **−0.7496** (reported lower), approximately 38.6% below the diagnostic count-derived OR. A conventional log-OR interval from the same four counts is approximately 1.10 to 3.45, compatible with the printed CI after displayed precision; ordinary rounding of 1.9436 cannot produce 1.194.

**Existing supported conclusion.** The locked finding concerns the printed unadjusted point estimate, not the direction or a replacement model result.

**Bounded impact and limitation.** The point estimate needs confirmation against the table-production or statistical-analysis output. The CI, P value, and inferential procedure are not independently replaced here; the report does not assume a different model, sidedness, or variance method.

**Verification instruction.**

1. Verify the four counts and printed OR/CI in the stated eTable 10 row. The issue is confirmed if they are 40, 66, 29, 93 and 1.194 (1.09-3.45).
2. Recompute `(40×93)/(66×29)`. A result near 1.94 confirms the diagnostic mismatch; a retained model/table-generation output explaining 1.194 would resolve the printed-value question.

### 4 — eFigure 8B repeats eFigure 7B statistics despite a different outcome

**Issue statement.** eFigure 8B, labelled as 28-day-mortality interactions, repeats all six OR/CI/P triplets printed for eFigure 7B, which is labelled as primary-endpoint interactions; this matters because the displayed mortality subgroup/interaction statistics are not reliable as shown.

**Category / severity / evidence status.** Statistical reporting inconsistency / Major / Verified; critic retained.

**Direct source evidence.**

- [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=51), PDF p. 51 (printed page 51), eFigure 7B, caption “Attainment of the Primary Endpoint According to Baseline Severity,” panel B “Interaction tests … for the primary endpoint”: **0.47 (0.30-1.62), P=.70; 1.85 (0.66-5.19), P=.24; 0.22 (0.09-0.53), P=.001; 5.79 (2.34-15.05), P<.0001; 0.56 (0.27-1.19), P=.13; 3.08 (1.37-6.96), P=.007**, respectively for APACHE II ≥25; APACHE II ≥25 × Precision Immunotherapy; CCI ≥5; CCI ≥5 × Precision Immunotherapy; SOFA ≥10; SOFA ≥10 × Precision Immunotherapy.
- [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=52), PDF p. 52 (printed page 52), eFigure 8, caption “28-Day Mortality According to Baseline Severity,” panel B: the same six displayed triplets at the same labels: **0.47 (0.30-1.62), .70; 1.85 (0.66-5.19), .24; 0.22 (0.09-0.53), .001; 5.79 (2.34-15.05), <.0001; 0.56 (0.27-1.19), .13; 3.08 (1.37-6.96), .007.**
- [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8), PDF p. 8, journal p. 782, Results—“Post Hoc and Subgroup Analyses”: identifies eFigure 7 as primary-endpoint interaction testing and eFigure 8 as 28-day-mortality interaction testing.

**Direct comparison and diagnostic calculation.** The six displayed eFigure 8B triplets equal the corresponding eFigure 7B triplets exactly at every shown digit and P-value expression (six of six matches). Reported comparator outcome labels differ: primary endpoint (eFigure 7) versus 28-day mortality (eFigure 8). As a diagnostic only, the eFigure 8A high-stratum mortality counts yield simple precision-versus-placebo ORs: APACHE II ≥25 `(22×13)/(16×27)=0.662`; CCI ≥5 `(24×26)/(30×50)=0.416`; SOFA ≥10 `(35×20)/(32×48)=0.456`. These are not interaction-model estimates and do not replace eFigure 8B; they only document that panel A's mortality comparisons are distinct from the identically repeated panel-B statistics.

**Existing supported conclusion.** The locked finding is exact duplication of the printed interaction statistics across differently labelled outcomes.

**Bounded impact and limitation.** eFigure 8B’s displayed subgroup/interaction results require confirmation against the original 28-day mortality model and figure source. No correct mortality-model OR, CI, P value, or production-error mechanism is recoverable from this package.

**Verification instruction.**

1. Compare the six panel-B lines on PDF pp. 51 and 52, including labels, ORs, CIs, and P values. Six exact matches alongside different captions confirms the duplication.
2. Inspect the original 28-day-mortality interaction-model output and figure-production source. A distinct supported set of eFigure 8B statistics resolves the displayed duplication.

### 5 — Table 2 reverses the displayed direction of the 28-day mortality difference

**Issue statement.** Table 2 lists precision immunotherapy before placebo but prints a positive 6.1% 28-day mortality difference even though precision minus placebo is −6.1 percentage points; this matters because the difference column’s sign is opposite the displayed group ordering.

**Category / severity / evidence status.** Presentation inconsistency / Minor / Verified; critic retained.

**Direct source evidence.** [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6), PDF p. 6, journal p. 780, Table 2, “Main secondary outcomes,” row “28-d Mortality”: Precision immunotherapy **57/131 (43.5)**; Placebo **72/145 (49.7)**; Difference **6.1 (−5.6 to 17.6)**; OR unadjusted **0.78 (0.49 to 1.26)**; P value **.34**. The adjacent “90-d Mortality” row prints precision 68.7 and placebo 67.6 with difference 1.1, consistent with precision minus placebo.

**Direct comparison and diagnostic calculation.** The displayed ordering is Precision immunotherapy minus Placebo. `100×(57/131 − 72/145) = 100×(0.4351145 − 0.4965517) = −6.1437` percentage points, rounding to **−6.1%**. Reported difference = **+6.1%**; expected under table ordering = **−6.1%**: the sign is reversed. One-decimal rounding tolerance (±0.05 percentage points) does not change the sign. If the interval were also displayed under precision minus placebo, the corresponding endpoint direction would be approximately −17.6 to 5.6; this is diagnostic only, not a substituted CI.

**Existing supported conclusion.** The locked finding is a directional presentation inconsistency in the difference column.

**Bounded impact and limitation.** The observed risk-difference direction needs confirmation. The report does not change the printed OR, CI, or P value and does not assert a corrected interval because the table footnotes do not establish an alternative contrast or interval-production rule for this row.

**Verification instruction.**

1. Verify the two Table 2 fractions and column order, then calculate precision minus placebo. A result of approximately −6.1 percentage points confirms the sign mismatch.
2. Check Table 2 footnotes and original tabulation output for an explicitly defined alternative contrast. Such a definition would resolve why +6.1% was printed.

### 6 — Abstract attaches patient-incidence percentage to an event count

**Issue statement.** The abstract grammatically attaches 88.8% to 1069 serious adverse events, whereas the body and eTable 13 attach that percentage to 245 of 276 patients; this matters because event count and patient incidence are different quantities.

**Category / severity / evidence status.** Presentation inconsistency / Minor / Verified; critic retained.

**Direct source evidence.**

- [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1), PDF p. 1, journal p. 775, Abstract—Results: “A total of **1069 serious treatment-emergent adverse events (88.8%)** were reported.”
- [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8), PDF p. 8, journal p. 782, Results—“Adverse Events”: “A total of **1069 serious treatment-emergent adverse events were reported in 245 patients (88.8%)**.”
- [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=27), PDF p. 27 (printed page 27), eTable 13, row “Any SAE, n (%)”, Total column **245 (88.8)** and header `Total (N=276)`.

**Direct comparison and diagnostic calculation.** Reported abstract event count = **1069** with parenthetical **88.8%**. Comparator patient incidence = `245 ÷ 276 × 100 = 88.7681%`, which rounds to **88.8%** to one decimal (±0.05 percentage points). No denominator is stated in these supplied locations for which 1069 events equals 88.8%. The body explicitly assigns 88.8% to 245 patients.

**Existing supported conclusion.** The locked finding is a presentation conflation of an event count and patient-incidence percentage in the abstract.

**Bounded impact and limitation.** The abstract’s percentage attachment needs correction or confirmation; the body and supplement support the intended patient-incidence denominator. No event-level denominator or alternative abstract wording is inferred.

**Verification instruction.**

1. Compare the abstract sentence with the body’s Adverse Events sentence. Confirmation requires observing the abstract parenthesis immediately after 1069 and the body phrase “in 245 patients (88.8%).”
2. Check eTable 13 Total column and calculate 245/276. A result rounding to 88.8% confirms the patient-incidence comparator.

## Uncertain Candidates

### 3 — eFigure 9 reports an OR outside its reported confidence interval

**Issue statement.** eFigure 9B prints an OR of 0.11 with a 95% CI of 0.36-3.42 for the APACHE II ≥25 interaction, placing the stated OR below its stated lower bound; this matters because the matched interaction magnitude cannot be interpreted reliably as printed.

**Category / potential severity / evidence status.** Statistical reporting inconsistency / not separately assigned in the surviving authority record / Uncertain. This specific locked disposition is preserved.

**Direct source evidence.** [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=53), PDF p. 53 (printed page 53), eFigure 9B, row “APACHE II ≥25 × Precision Immunotherapy,” OR column **0.11**, 95% CIs column **0.36-3.42**, P-value column **.86**. Caption: “90-Day Mortality According to Baseline Severity”; panel B: “Interaction tests of subgroups with the studied intervention for 90-day mortality.”

**Direct comparison and logical check.** Reported OR = **0.11**. Comparator rule for a conventional matched confidence interval = point estimate must be within its stated interval. Lower bound = **0.36**; `0.11 < 0.36` by **0.25**. At two-decimal displayed precision, 0.11 can represent 0.105-0.114999… and 0.36 can represent 0.355-0.364999…; those rounding intervals do not overlap. The discrepancy therefore cannot be reconciled by ordinary two-decimal rounding.

**Existing supported conclusion.** The candidate remains Uncertain because the package does not establish whether the OR, CI, or row pairing is the item in error.

**Bounded impact and limitation.** Confirmation is required before interpreting this printed interaction magnitude. The displayed CI and P value are not treated as a replacement matched result; no correct OR/CI pair is available in the supplied materials.

**Verification instruction.**

1. Inspect the specified eFigure 9B row and verify all three printed fields. Observing 0.11, 0.36-3.42, and .86 confirms the display that triggered the candidate.
2. Inspect the underlying 90-day-mortality interaction regression and original figure output. A matched OR and CI resolves the candidate; without that output, the candidate remains Uncertain.

## Rejected and Excluded Interpretations

### A — Localized terminology slip in eFigure 6

**Issue statement.** The closing sentence of the eFigure 6 caption substitutes “organ dysfunction” for the “immune dysfunction” named by the title, axis, and preceding caption, but the isolated word change does not alter the plotted result.

**Evidence status / category / severity.** Rejected. The surviving decision record did not preserve a formal candidate identifier, category, or severity for this interpretation; none is invented here.

**Direct source evidence.**

- [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=50), PDF p. 50 (printed page 50), eFigure 6 title: “Time to Reversal of Sepsis-Induced **Immune Dysfunction**”; y-axis: “% of patients with reversal of sepsis-induced **immune dysfunction**”; opening caption: “The reversal of **immune dysfunction** was studied…”.
- Same page, eFigure 6 caption, final sentence: patients without sufficient serial blood draws “were considered not to attain reversal of sepsis-induced **organ dysfunction**.”
- Same page, plotted numerical output: HR **2.38**, 95% CI **1.50 to 3.77**, `P<.001`; at-risk rows are placebo **66, 51, 44, 44, 38, 38, 37, 34** and precision immunotherapy **59, 18, 16, 16, 14, 14, 14, 13**.
- [jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf](../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=8), PDF p. 8, journal p. 782, Results—“Post Hoc and Subgroup Analyses,” identifies eFigure 6 as the time to reversal of sepsis-induced immune dysfunction.

**Reasoning procedure.**

1. The title, axis, opening caption, biomarker definition, and main-article cross-reference all identify the outcome as reversal of immune dysfunction.
2. “Organ dysfunction” occurs only in the closing caption sentence.
3. The terminology substitution does not change the HR, CI, P value, curves, or at-risk counts.
4. The completed workflow therefore treated the interpretation as a locally recoverable, non-material wording defect and rejected it as a retained scientific finding.

**Existing supported conclusion.** Preserve the Rejected disposition; no scientific issue is retained from this localized terminology slip.

**Limit on interpretation.** This report does not infer editorial intent, amend the source, or claim that the displayed time-to-event analysis is otherwise validated.

**Verification instruction.**

1. Compare the title, y-axis, opening caption, closing sentence, and main-article cross-reference. The rejected interpretation is confirmed if “organ” is isolated to the closing sentence while the outcome is otherwise consistently “immune dysfunction.”
2. Confirm that the HR, CI, P value, and risk table are unchanged by the terminology substitution.

### B — Two readily recoverable malformed eTable 14 cells

**Issue statement.** eTable 14 contains one duplicated zero and one missing opening parenthesis, but each affected count and percentage is recoverable from its row, column, denominator, and totals without changing a scientific value.

**Evidence status / category / severity.** Rejected. The surviving decision record did not preserve a formal candidate identifier, category, or severity for this interpretation; none is invented here.

**Direct source evidence.** [joi250116supp2_prod_1771885794.27755.pdf](../joi250116supp2_prod_1771885794.27755.pdf#page=30), PDF p. 30 (printed page 30), eTable 14:

- Row “Probably related,” column “Standard care + Anakinra (N=25)” prints **`0 0 (0.0)`**. Other cells in the same row are placebo 1 (4.3), rhIFNγ 3 (2.8), placebo 1 (0.8), and total 5 (1.8).
- Row “Severe,” column “Standard care + rhIFNγ (N=106)” prints **`45 42.5)`**. The same column prints Mild 19 (17.9), Moderate 40 (37.7), and Any AE by maximum severity 104 (98.1). The severe row prints 12, 14, 45, and 45 across the four treatment columns and total 116 (42.0).

**Reasoning procedure and diagnostic arithmetic.**

1. First cell, denominator check: `0/25 × 100 = 0.0%`.
2. First cell, relationship-category column check: `0 + 2 + 13 + 5 = 20`, equal to that column's Any-AE count; row check: `0 + 1 + 3 + 1 = 5`, equal to the printed row total.
3. Second cell, denominator check: `45/106 × 100 = 42.4528%`, which rounds to **42.5%** at one decimal.
4. Second cell, column check: `19 + 40 + 45 = 104`, equal to that column's Any-AE maximum-severity count.
5. Second cell, row check: `12 + 14 + 45 + 45 = 116`; `116/276 × 100 = 42.0290%`, which rounds to the printed total **42.0%**.
6. These internal checks explain why the completed workflow treated the strings as recoverable display defects and rejected them as scientific findings. They are diagnostic checks, not externally sourced corrections or an inferred production mechanism.

**Existing supported conclusion.** Preserve the Rejected disposition; the affected numerical values remain recoverable within the printed table.

**Limit on interpretation.** The report does not modify the source, infer how the defects arose, or generalize from these two cells to the rest of eTable 14.

**Verification instruction.**

1. Read both malformed strings visually on PDF p. 30 and confirm their row and column headings.
2. Recompute the two percentages and reconcile the stated row and column totals. The rejected interpretation is confirmed if the printed numerical values remain uniquely recoverable without changing any total.

## Human Adjudication Checklist

1. Confirm each source-file hash in the Package Manifest before relying on the quoted locations.
2. Confirm the two express AI-training notices and apply Human Compliance Review where flagged; treat this as a separate compliance screen, not a scientific finding.
3. For findings 1, 2, 4, 5, and 6, perform the numbered source checks in the relevant evidence card and record whether the printed values remain as quoted.
4. For item 3, obtain the original eFigure 9 regression/figure-production output; do not infer a corrected OR or CI from the package.
5. For rejection B, verify the two PDF p. 30 strings and their row/column arithmetic; preserve the missing historical category and severity rather than inventing them.
6. Resolve the report-record exceptions: distinguish the historical preprocessing-manifest page entries from the recorded approved audit scope, and preserve item 3 as Uncertain notwithstanding the historical phrase “six findings.”
