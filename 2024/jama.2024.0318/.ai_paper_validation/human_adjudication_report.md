# Human Adjudication Report

**Package status:** Completed; submitted for Human Adjudication.  
**Scope:** Five accepted critic findings. This report reproduces only supplied evidence and calculations; it makes no finding beyond that evidence.

## Scientific Issues

### 1. Twelve-year HbA1c P value differs between the main article and results supplement

**Issue statement:** The same 12-year HbA1c estimate and confidence interval are reported with `P = .002` in the main article but `P < .001` in the results supplement, which requires confirmation of the intended model output even though both statements meet a conventional .05 significance threshold.  
**Category:** Cross-document inconsistency  
**Severity:** Minor  
**Evidence status:** Supported document-level discrepancy.

**Evidence A — main article.** **Location:** DOC-001, `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF page 1 (abstract result) and PDF page 3 (results paragraph). **Reported value:** “12-year HbA1c −1.1% (CI, −1.7 to −0.5); P = .002.”  
**Evidence B — results supplement.** **Location:** DOC-003, `joi240004supp2_prod_1721756962.82552.pdf`, PDF page 15, eTable 2, 12-year HbA1c entry. **Reported value:** “−1.1 (−1.7, −0.5); P < .001.”

**Direct comparison:** The reported estimate is `−1.1%` in both sources and the reported CI is `−1.7 to −0.5` in both; the P-value presentation differs: exact `0.002` versus a claim that the value is `<0.001`. The exact value is `0.001` greater than the stated upper bound.  
**Reproducible check:** Inputs: `P = 0.002`; supplement rule: `P < 0.001`. Calculation: `0.002 − 0.001 = +0.001`; therefore `0.002 < 0.001` is false. No rounding tolerance is stated; an exact displayed P value is compared with the displayed strict threshold.  
**Bounded impact:** The 12-year HbA1c P-value statement in one of these locations needs correction or confirmation; the supplied evidence does not change the displayed estimate or CI, and both displayed P statements are below `.05`.  
**Verification instruction:** 1. Check the 12-year HbA1c model output used for the abstract/results text and eTable 2. A P value of `.002` resolves the supplement threshold as incorrect; a value below `.001` resolves the main-text P value as incorrect; a defined different-analysis basis would explain the discrepancy.

### 2. eTable 2 timepoint labels and footnotes are internally misaligned

**Issue statement:** eTable 2 is labelled as 12-year data while its footnotes define comparisons at baseline/year 7 and at year 7, creating ambiguity about the timepoint represented by the reported results.  
**Category:** Presentation inconsistency  
**Severity:** Minor  
**Evidence status:** Supported document-level presentation discrepancy.

**Evidence A — table title and headers.** **Location:** DOC-003, `joi240004supp2_prod_1721756962.82552.pdf`, PDF page 15, eTable 2 title and column headers. **Reported wording:** title identifies “Year 12”; headers identify “Year 12.”  
**Evidence B — footnotes.** **Location:** DOC-003, same file, PDF page 15, eTable 2 footnotes `a` and `b`; PDF page 16, eTable 2 footnote `c`. **Reported wording:** footnote `a` identifies “baseline/year-7”; footnote `b` defines ratio “year 7/base” and odds ratios “7-year”; footnote `c` defines surgery as “7-year minus med 7-year” and the odds ratio “at year 7.”

**Direct comparison:** The title/headers designate year 12, whereas the cited footnotes designate year 7 (and baseline/year 7); the discrepancy is a 5-year timepoint mismatch in the labels.  
**Reproducible check:** Inputs: table label `Year 12`; footnote comparison timepoint `Year 7`. Calculation: `12 − 7 = 5 years`. No rounding applies.  
**Bounded impact:** The table’s comparison definitions, labels, or both require confirmation; the supplied evidence does not establish which values, if any, are numerically incorrect.  
**Verification instruction:** 1. Check the analysis/output table underlying eTable 2 and the intended footnote template. Confirmation that the output is year-12 data resolves the issue by revising the year-7 footnotes; confirmation that it is year-7 data resolves it by revising the title/headers.

### 3. BMI category boundary at exactly 35 is described differently across sources

**Issue statement:** The main article uses BMI categories `27 to <35` and `≥35`, whereas the supplement figure uses `<35` and `>35`, leaving BMI exactly 35 unassigned in the figure wording and requiring confirmation of the subgroup coding.  
**Category:** Cross-document inconsistency  
**Severity:** Minor  
**Evidence status:** Uncertain — the subgroup coding/model output is not supplied.

**Evidence A — main article.** **Location:** DOC-001, `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF page 7, BMI subgroup labels. **Reported values:** `27 to <35` and `≥35`.  
**Evidence B — results supplement.** **Location:** DOC-003, `joi240004supp2_prod_1721756962.82552.pdf`, PDF page 13, eFigure 6 title/legend, BMI subgroup labels. **Reported values:** `<35` and `>35`.

**Direct comparison:** At BMI `35`, DOC-001 assigns the value to `≥35`; DOC-003’s displayed `<35` and `>35` labels assign it to neither displayed group.  
**Reproducible logical check:** Inputs: `35 ≥ 35` is true; `35 < 35` is false; `35 > 35` is false. Rule: a pair of complementary displayed categories should account for the boundary value. Result: `35` is included by the DOC-001 labels and omitted by the DOC-003 labels. No rounding tolerance applies to the displayed inequalities.  
**Bounded impact:** The BMI subgroup definition or figure labelling requires correction or confirmation; without subgroup coding/model output, the supplied evidence cannot determine whether any participant or effect estimate was misclassified.  
**Verification instruction:** 1. Check the BMI subgroup variable/coding and the plotting specification for eFigure 6. Coding that assigns BMI `35` to the high-BMI group resolves the figure by changing `>35` to `≥35`; coding that excludes or handles 35 differently requires a documented explanation and matching labels.

### 4. Baseline-to-year-7 HbA1c direction is presented differently in text and Table 2

**Issue statement:** The main-text baseline and year-7 values yield a change of `−0.2`, matching Table 2, while the main text describes a “difference 0.2,” so the direction/definition of the textual difference needs confirmation.  
**Category:** Statistical reporting inconsistency  
**Severity:** Minor  
**Evidence status:** Uncertain — the definition and model output for the textual “difference” are not supplied.

**Evidence A — main text.** **Location:** DOC-001, `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF page 3, results paragraph. **Reported values:** baseline `8.2`; year 7 `8.0`; “difference 0.2 (CI, −0.5 to 0.2).”  
**Evidence B — table.** **Location:** DOC-001, same file, PDF page 6, Table 2, HbA1c change entry. **Reported value:** `−0.2` with CI `−0.5 to 0.2`.

**Direct comparison:** `8.0 − 8.2 = −0.2`, which has the same signed direction as Table 2’s `−0.2`; the textual “difference 0.2” is unsigned/positive as displayed. The magnitude is identical (`0.2`), while the displayed direction differs by `0.4` percentage points when represented as `+0.2` versus `−0.2`.  
**Reproducible calculation:** Inputs: year-7 HbA1c `8.0`, baseline HbA1c `8.2`. Formula: `year 7 − baseline = 8.0 − 8.2 = −0.2` percentage points. Comparator: Table 2 `−0.2` (CI `−0.5 to 0.2`). No rounding tolerance is needed because the calculation matches the table at one decimal place.  
**Bounded impact:** The wording/sign convention of the main-text difference needs confirmation; the supplied evidence does not establish that the table’s estimate or CI is incorrect.  
**Verification instruction:** 1. Check the source analysis/model contrast and its defined direction for the page-3 sentence. If the contrast is year 7 minus baseline, confirmation of `−0.2` resolves the text by adding the negative sign or using “decrease”; if it is baseline minus year 7, the contrast definition should be stated so it can be reconciled with Table 2.

### 5. eTable 1 race counts and percentages do not reconcile to the stated total

**Issue statement:** eTable 1 reports race categories whose counts total 261 rather than `N = 262`, and its reported `Other` percentage is `1.9%` although `4/262` is `1.5%` to one decimal place, which requires tabulation confirmation.  
**Category:** Arithmetic inconsistency  
**Severity:** Minor  
**Evidence status:** Supported arithmetic discrepancy.

**Evidence A — results supplement.** **Location:** DOC-003, `joi240004supp2_prod_1721756962.82552.pdf`, PDF page 14, eTable 1, race rows and total. **Reported values:** `N = 262`; Black `81 (30.9%)`; White `176 (67.2%)`; Other `4 (1.9%)`.  
**Evidence B — main article comparator.** **Location:** DOC-001, `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF page 4, Table 1, race rows. **Reported values:** Black `35 + 46`; White `59 + 118`; Other `2 + 2`; combined total `262`.

**Direct comparison:** eTable 1’s listed counts total `81 + 176 + 4 = 261`, one fewer than `N = 262`; the main-article race counts sum to `(35 + 46) + (59 + 118) + (2 + 2) = 262`. eTable 1’s `Other` count of `4` agrees with the main article, but `4/262 × 100 = 1.5267…%`, not the displayed `1.9%`.  
**Reproducible calculation:** Count inputs: `81`, `176`, `4`; formula `81 + 176 + 4 = 261`; discrepancy `261 − 262 = −1 participant`. Percentage inputs: `4`, `262`; formula `(4 ÷ 262) × 100 = 1.5267…%`; rounded to one decimal place = `1.5%`; reported = `1.9%`; discrepancy = `+0.4 percentage points`. Rounding tolerance considered: conventional rounding to one decimal place.  
**Bounded impact:** The eTable 1 race total and/or race percentages require correction or confirmation; the supplied evidence does not identify the missing category/count or determine whether the main-article Table 1 is the intended source tabulation.  
**Verification instruction:** 1. Re-run or inspect the eTable 1 race-frequency tabulation for all `N = 262` participants, including any missing/unknown category. A category total of 262 and percentages calculated from the stated denominator would resolve the issue; otherwise revise the displayed denominator, counts, or percentages with a documented denominator.

## AI Training Restriction Summary

This separate screen reports supplied-file language only; it is not a legal opinion and is not part of the scientific issue list.

| Document ID | Filename | Status | Exact evidence location and retained wording/context | Human Compliance Review |
|---|---|---|---|---|
| DOC-001 | `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf` | No AI Training Restriction Located in Provided Materials | PDF pages 1–11, footer: “© 2024 American Medical Association. All rights reserved.” Embedded metadata screen: no AI-use/right/license condition located. | No |
| DOC-002 | `joi240004supp1_prod_1721756962.80052.pdf` | Conditional / Permission Required | PDF page 1, “Confidential Information”: “must not be disclosed without written permission …”; PDF page 40, §11.3; PDF page 42, §14.0, data/documents confidentiality and consent language. No express AI-training term located. | Yes — permissions subsequently confirmed by the user; scientific document remains Not Audited by Design (protocol). |
| DOC-003 | `joi240004supp2_prod_1721756962.82552.pdf` | No AI Training Restriction Located in Provided Materials | PDF pages 1–22, footer: “© 2024 American Medical Association. All rights reserved.” Embedded XMP metadata: `pdfx:MSIP_Label_5e4b1be8-281e-475d-98b0-21c3457e5a46_Name = Public`; no AI-use/right/license condition located. | No |
| DOC-004 | `joi240004supp3_prod_1721756962.84052.pdf` | No AI Training Restriction Located in Provided Materials | PDF page 1, Data Sharing Statement: deidentified-data access is subject to proposal approval and a data-use agreement; no AI-training condition located. | No — scientific document remains Not Audited by Design (administrative/data-sharing material). |

## Document-Level Processing Status

| Document ID | Classification | Scientific processing status | Document-level output |
|---|---|---|---|
| DOC-001 | Main article | Completed: pages 1–11 processed; result-relevant pages rendered; no OCR required. | `document_outputs/DOC-001/` |
| DOC-002 | Protocol | Not Audited by Design; rights screen completed. | `document_outputs/DOC-002/` |
| DOC-003 | Results supplement | Completed for result-relevant pages 8–22; native text retained and pages rendered; OCR limitation recorded for sparse figure text. | `document_outputs/DOC-003/` |
| DOC-004 | Administrative/data-sharing material | Not Audited by Design; rights screen completed. | `document_outputs/DOC-004/` |
