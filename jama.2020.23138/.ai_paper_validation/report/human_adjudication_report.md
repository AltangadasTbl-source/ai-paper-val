# Human Adjudication Report — `jama.2020.23138`

**Workflow status:** Complete for the defined audit scope; submitted for Human Adjudication.  
**Scientific findings:** 8 retained: 7 Accepted and 1 Uncertain.  
**Purpose:** Materials-only adjudication aid; not legal advice.

## Scope, Processing, and Limitations

- Audited: `JAMA2020-23138-MAIN` (`jama_kotecha_2020_oi_200126_1607962892.52158.pdf`), PDF pages 1–12.
- Audited: `JAMA2020-23138-SUPP03-RESULTS` (`joi200126supp3_prod_1607962892.5372.pdf`), PDF pages 1–20, with primary result pages 8–18.
- **Not Audited by Design:** `JAMA2020-23138-SUPP01-PROTOCOL` (69 pages), `JAMA2020-23138-SUPP02-SAP` (45 pages), and `JAMA2020-23138-SUPP04-DATA-SHARING` (1 page). Each received the mandatory rights screen only.
- Native text extraction completed for all 32 audited pages. The OCR selector reported backend `unavailable` because RapidOCR, ONNX Runtime, and Tesseract were absent. Required OCR therefore failed before initialization on seven figure/flow pages: main pages 3 and 8 and results-supplement pages 8–12. Original-page renders were visually verified where possible; no finding claims successful OCR.

## AI Training Restriction Summary

This compliance screen is separate from the scientific findings. Absence of a located restriction is not permission.

| Document ID and filename | Status | Exact evidence location | Human Compliance Review trigger |
|---|---|---|---|
| `JAMA2020-23138-MAIN` — `jama_kotecha_2020_oi_200126_1607962892.52158.pdf` | No AI Training Restriction Located in Provided Materials | PDF pages 1–12, recurring footer: “© 2020 American Medical Association. All rights reserved.” Info/XMP contained no AI-use, license, permissions, or terms field. | No |
| `JAMA2020-23138-SUPP01-PROTOCOL` — `joi200126supp1_prod_1607962892.5372.pdf` | No AI Training Restriction Located in Provided Materials | Screened PDF page 1, pages 52–60, full text, and Info/XMP. Non-AI controls at page 53 §11.5, page 58 §16, and page 59 §18 address data, confidentiality, and publications. | No |
| `JAMA2020-23138-SUPP02-SAP` — `joi200126supp2_prod_1607962892.5372.pdf` | No AI Training Restriction Located in Provided Materials | Screened PDF pages 1–2 and 44–45, full extractable text, and Info/XMP; no relevant rights or AI-use language located. | No |
| `JAMA2020-23138-SUPP03-RESULTS` — `joi200126supp3_prod_1607962892.5372.pdf` | No AI Training Restriction Located in Provided Materials | PDF pages 1–20, recurring footer: “© 2020 American Medical Association. All rights reserved.” XMP contained no AI-use, license, permissions, or terms statement. | No |
| `JAMA2020-23138-SUPP04-DATA-SHARING` — `joi200126supp4_prod_1607962892.5372.pdf` | No AI Training Restriction Located in Provided Materials | PDF page 1: “Data available: No” and “Release of data will be subject to a data use agreement….” These address underlying data, not AI training using the supplied PDF. | No |

## Final Evidence Cards

### 1. V1 — The supplement describes raw SF-36 scoring as primary while the main article describes normalized scoring as the primary outcome, leaving the intended primary scoring analysis ambiguous.

- **Category / severity / status:** Cross-document inconsistency / Major / Accepted
- **Evidence A:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 5, eMethods, “Quality of life tools and scoring”: “domain and summary scores were primarily analyzed using raw values.”
- **Evidence B:** `JAMA2020-23138-MAIN`, `jama_kotecha_2020_oi_200126_1607962892.52158.pdf`, PDF page 1, Abstract Results: “primary outcome of normalized SF-36 PCS at 6 months.”
- **Evidence C:** Main PDF page 6, Table 2 and Primary End Point: normalized PCS adjusted difference `1.4` (95% CI `−1.1 to 3.8`), `P=.28`; raw PCS adjusted difference `1.3` (95% CI `−1.2 to 3.9`), `P=.30`.
- **Evidence D:** Main PDF page 9, Discussion: upper 95% confidence limit for the primary outcome reported as `3.9`.
- **Direct comparison:** The supplement identifies raw values as primary; the main abstract identifies normalized PCS as primary; the Discussion’s `3.9` matches the raw row, not the normalized row’s `3.8`.
- **Reproducible logic:** Raw minus normalized effect is `1.3−1.4=−0.1 PCS points`; upper-CI difference is `3.9−3.8=0.1 PCS points`; P-value difference is `.30−.28=.02`. These exceed displayed precision, so rounding does not reconcile the designations.
- **Bounded impact:** Both analyses remain nonsignificant; the null conclusion is unchanged, but the intended primary estimate, CI, and P value require confirmation.
- **Human verification:**
  1. Confirm the raw-score statement on supplement page 5.
  2. Compare both main Table 2 PCS rows with the Abstract wording.
  3. Confirm that Discussion’s `3.9` uniquely matches the raw row.
  4. Check the approved analysis specification/output to establish the intended primary scoring analysis.

### 2. V2 — The adverse-event χ² cannot be reproduced from the stated 80/80 analysis-set denominators.

- **Category / severity / status:** Statistical reporting inconsistency / Minor / Accepted
- **Evidence A:** `JAMA2020-23138-MAIN`, `jama_kotecha_2020_oi_200126_1607962892.52158.pdf`, PDF page 4, Statistical Analysis/Results: the full analysis set included randomized patients receiving at least one dose; each group had `80`.
- **Evidence B:** Main PDF page 6, Adverse Events: `20 patients (25%)` versus `51 (64%)`, `χ²=24.91`, `P<.001`.
- **Evidence C:** Main PDF page 9, Table 4 headers: digoxin `n=80`, bisoprolol `n=80`.
- **Evidence D:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 17, eTable 5 and footnote a: `20 (25%)`, `51 (64%)`, total `71 (44%)`.
- **Direct comparison:** Reported `χ²=24.91`; Pearson χ² from the displayed `20/80` and `51/80` is `24.33`, a difference of `0.58`.
- **Reproducible calculation:** The events/non-events table is digoxin `20/60`, bisoprolol `51/29`:

  `χ² = 160 × (20×29 − 60×51)² / (80×80×71×89) = 24.3330`,

  which rounds to `24.33`, not `24.91`. A diagnostic calculation using `20/81` versus `51/80` gives `24.9077`, which rounds to `24.91`, but this numerical match does not prove that 81/80 was the actual denominator. No two-decimal rounding tolerance bridges `24.33` and `24.91`.
- **Bounded impact:** The denominator or test specification is not reproducible from the report; both values yield `P<.001`, so the displayed significance threshold is unchanged.
- **Human verification:**
  1. Confirm the analysis-set definition, group sizes, event counts, and statistic.
  2. Recalculate Pearson χ² from 20/80 and 51/80; expected value `24.3330`.
  3. Inspect statistical-program output for the actual denominator, inclusion rule, and χ² procedure.
  4. Correct the statistic or the analysis-set/table description as appropriate.

### 3. V6 — Figure 1 reports 161 randomized participants but its allocation branches total 160.

- **Category / severity / status:** Participant flow inconsistency / Minor / Accepted
- **Evidence A:** `JAMA2020-23138-MAIN`, `jama_kotecha_2020_oi_200126_1607962892.52158.pdf`, PDF page 3, Figure 1: `161 Randomized`; `80 Randomized to receive digoxin`; `80 Randomized to receive bisoprolol`.
- **Evidence B:** Main page 3, Figure 1 footnote b: one participant withdrew after randomization before therapy.
- **Evidence C:** Main page 4, Results: the participant did not complete baseline/start treatment and was replaced; `160` received at least one dose.
- **Direct comparison:** Randomized total `161` versus visible allocation branches `80+80=160`; one participant lacks an allocation/nonreceipt branch.
- **Reproducible logic:** `161−(80+80)=1`. Original-PDF visual inspection found no separate branch assigning or disposing of that participant.
- **Bounded impact:** The narrative explains the 160-person treated cohort, but the diagram does not fully show disposition for all randomized participants; this is not an identified analysis-count error.
- **Human verification:**
  1. Inspect original Figure 1 and sum its allocation branches.
  2. Confirm footnote b and the page-4 explanation.
  3. Check the randomization record for the withdrawn participant’s allocated group.
  4. Decide whether a missing allocation/nonreceipt branch should be added.

### 4. V4 — Table 3’s blanket higher-is-better footnote conflicts with lower-is-better outcomes.

- **Category / severity / status:** Presentation inconsistency / Minor / Accepted
- **Evidence A:** `JAMA2020-23138-MAIN`, `jama_kotecha_2020_oi_200126_1607962892.52158.pdf`, PDF page 7, Table 3 footnote b: “Higher values indicate better response with digoxin therapy.”
- **Evidence B:** Same table, NYHA row/footnote h: digoxin `1.5`, bisoprolol `2.0`, adjusted difference `−0.6` (95% CI `−0.8 to −0.4`); lower NYHA classes mean less limitation.
- **Evidence C:** Same table, NT-proBNP ratio `0.77` (95% CI `0.64–0.92`).
- **Evidence D:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 12, eFigure 5 caption: “negative values indicating superiority of digoxin.”
- **Direct comparison:** The blanket higher-is-better statement conflicts with a favorable negative NYHA difference and a favorable ratio below 1.
- **Reproducible logic:** NYHA crude difference is `1.5−2.0=−0.5`; adjusted difference is `−0.6`. For NT-proBNP, `1−0.77=0.23`, indicating a geometric mean about 23% lower for digoxin. No rounding tolerance is relevant.
- **Bounded impact:** Numerical results remain interpretable, but the footnote can reverse the treatment-direction interpretation.
- **Human verification:**
  1. Compare footnote b with the NYHA definition/difference.
  2. Confirm eFigure 5’s negative-is-superior statement.
  3. Confirm the intended interpretation of ratio `0.77`.
  4. Replace the general direction statement with outcome-specific wording.

### 5. V3 — Repeated baseline summaries differ across tables despite the same digoxin n=80 label.

- **Category / severity / status:** Statistical reporting inconsistency / Minor / Accepted
- **Evidence A:** `JAMA2020-23138-MAIN`, `jama_kotecha_2020_oi_200126_1607962892.52158.pdf`, PDF page 5, Table 1, digoxin `n=80`: NT-proBNP `1095 (715–1527) pg/mL`; ECG `100.1 (16.8)/min`; apex `98.2 (15.1)/min`; radial pulse `87.8 (12.1)/min`.
- **Evidence B:** Main PDF page 7, Table 3, baseline digoxin `n=80`: NT-proBNP `1091 (710–1522) pg/mL`; ECG `100.3 (16.8)/min`; apex `98.3 (15.1)/min`; radial pulse `87.8 (12.0)/min`.
- **Evidence C:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 14, eTable 2, baseline digoxin `n=80`: repeats the latter heart-rate values.
- **Direct comparison/calculation:** NT-proBNP median differs by `4 pg/mL` and IQR limits by `5 pg/mL` each; ECG mean by `0.2/min`; apex mean by `0.1/min`; radial SD by `0.1/min`. Each exceeds the displayed increment.
- **Rounding/assumption boundary:** The common n=80 label does not prove identical row-level records, timing, or derivation; no explanatory footnote was located.
- **Bounded impact:** Baseline descriptions require reconciliation; no outcome comparison is shown to change.
- **Human verification:**
  1. Confirm the cited cells and n=80 headings.
  2. Check footnotes for different timing, subsets, or derivations.
  3. Compare the source datasets/table-generation output.
  4. Confirm the correct values or disclose why the summaries differ.

### 6. V5 — eTable 2 is a heart-rate table, but its footnote describes quality-of-life interpretation.

- **Category / severity / status:** Presentation inconsistency / Minor / Accepted
- **Evidence:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 14, eTable 2 title/rows/footnote a. Title: “Resting and exertional heart rate”; rows use `beats/min`; footnote: “hence higher values represent better quality of life in the digoxin arm.”
- **Direct comparison/logical rule:** The table contains ECG, apex, radial, pulse-deficit, and exertional heart-rate endpoints, not a quality-of-life scale. The footnote names a different endpoint family; no numerical or rounding rule applies.
- **Bounded impact:** Explanatory wording is inapplicable; numerical results are unchanged.
- **Human verification:**
  1. Confirm the title, units, and footnote.
  2. Confirm no quality-of-life score appears in eTable 2.
  3. Replace/remove the footnote with endpoint-appropriate wording.

### 7. V7 — eFigure 4 labels the mental-health domain “SF35-MH” while its caption and eTable 3 identify SF36.

- **Category / severity / status:** Presentation inconsistency / Minor / Accepted
- **Evidence A:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 11, eFigure 4 panel A label: `SF35-MH`.
- **Evidence B:** Same-page caption: “SF36 domains are … MH = mental health.”
- **Evidence C:** Supplement page 15, eTable 3, SF36 Mental health row.
- **Direct comparison/logical rule:** Figure label `SF35-MH` versus caption/table `SF36`; one-character discrepancy (`5` versus `6`). A 300-dpi original-PDF render visibly showed `SF35-MH`; this finding does not rely on OCR.
- **Bounded impact:** One-character label error; numerical bars are not implicated.
- **Human verification:**
  1. Magnify original eFigure 4 panel A.
  2. Confirm `SF35-MH`.
  3. Compare it with the caption and eTable 3.
  4. Correct to the intended instrument name.

### 8. V8 — Uncertain: eTable 2’s pulse-deficit mean differs from that implied by its displayed component means, but row-specific denominators are unavailable.

- **Category / severity / status:** Arithmetic inconsistency / Not assigned / Uncertain
- **Missing evidence:** Row-specific denominators/available-case populations, participant-level paired values, or table-generation output.
- **Evidence:** `JAMA2020-23138-SUPP03-RESULTS`, `joi200126supp3_prod_1607962892.5372.pdf`, PDF page 14, eTable 2, baseline digoxin header `n=80`, apex/radial/pulse-deficit rows and footnote b. Apex `98.3 (SD 15.1) beats/min`; radial `87.8 (SD 12.0) beats/min`; deficit `−10.3 (SD 9.4) beats/min`; footnote defines radial minus apex.
- **Direct comparison:** `87.8−98.3=−10.5 beats/min` versus reported `−10.3 beats/min`; difference `0.2 beats/min`.
- **Calculation/tolerance:** One-decimal rounding intervals for the component-implied difference are approximately `(−10.60, −10.40)`; the displayed −10.3 interval is `[−10.35, −10.25)`, with no overlap. If identical paired observations underpin all rows, `mean(radial−apex)=mean(radial)−mean(apex)`. The shared n=80 header does not establish identical row-specific denominators.
- **Bounded impact:** One baseline mean may need correction or explanation; no effect on follow-up contrasts or conclusions is established.
- **Human verification:**
  1. Confirm the values, n=80 header, footnote, and subtraction direction.
  2. Obtain row-specific denominators and missing-data handling.
  3. Recalculate from paired participant-level data/table output.
  4. Resolve if populations differ appropriately or output supports −10.3; otherwise correct/explain the cell.

## Human Adjudication Checklist

1. Confirm every cited PDF page, table/figure, panel, row, column, footnote, excerpt, and value against the original PDFs.
2. Obtain the approved analysis specification and program output for V1 and V2.
3. Obtain table-generation inputs/outputs and row-level denominators for V3 and V8.
4. Confirm allocation/disposition for the withdrawn randomized participant in V6.
5. Decide correction, clarification, or no action for each Accepted issue.
6. Preserve V8 as **Uncertain** until its named missing evidence is supplied.
7. Record the protocol, SAP, and data-sharing statement as **Not Audited by Design**.
8. Record the seven-page OCR failure as a processing limitation.
