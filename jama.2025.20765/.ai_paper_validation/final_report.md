# Package Manifest

| Document ID | Source PDF | Pages | Classification | Scientific audit scope | Disposition |
|---|---|---:|---|---|---|
| DOC-001 | `jama_zahid_2025_oi_250093_1768590553.08463.pdf` | 9 | Main article | Pages 1-9 | Audited after institutional approval confirmed 2026-07-21 |
| DOC-002 | `joi250093supp1_prod_1768590553.08963.pdf` | 109 | Composite non-results supplement: protocol, SAP, intervention materials | Not Audited by Design | Rights record retained; no scientific findings sought |
| DOC-003 | `joi250093supp2_prod_1768590553.09463.pdf` | 16 | Results supplement | Pages 3-16; pages 1-2 excluded | Audited after institutional approval confirmed 2026-07-21 |

# AI Training Restriction Summary

This separate compliance screen is not a legal opinion and is not part of the scientific issue list.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001 | Explicit AI Training Restriction | `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p1 footer, repeated pp2-9: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; institutional approval confirmed 2026-07-21 |
| DOC-002 | No AI Training Restriction Located in Provided Materials | `joi250093supp1_prod_1768590553.08963.pdf`: all 109 pages screened by native-text terms; visual review of pp1, 2, 41, 77-78, 101, and 109; embedded document/XMP metadata. No applicable quotation located. | Not required by this record; permission is not inferred |
| DOC-003 | Explicit AI Training Restriction | `joi250093supp2_prod_1768590553.09463.pdf`, p1 footer, visually verified and repeated pp2-16: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; institutional approval confirmed 2026-07-21 |

# Scientific Findings

Eight findings were retained: 2 Major and 6 Minor.

## F01 — Major — Cross-document inconsistency: omitted mHealth cluster

- **Location:** `joi250093supp2_prod_1768590553.09463.pdf`, p4, eTable 2 and p8, eTable 5; `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p5, Table 1.
- **Source evidence:** eTable 2 contains 17 mHealth sites totaling 680 participants and 168 prior-attempt “Yes” responses, omitting site 2012. eTable 5 identifies site 2012 as an mHealth cluster of 40 participants. Table 1 reports 178/720.
- **Basis:** `720 − 680 = 40`; `178 − 168 = 10`.
- **Verification:** Sum the mHealth rows in eTable 2, compare with Table 1, and confirm site 2012 in eTable 5.

## F02 — Major — Cross-document inconsistency: adverse-event direction reversed

- **Location:** `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p5; `joi250093supp2_prod_1768590553.09463.pdf`, p15, eTable 10.
- **Source evidence:** Main text states that dry mouth, irritability, and anxiety were more common with mHealth. eTable 10 reports irritability 283/699 versus 145/334 and anxiety 233/699 versus 123/334.
- **Basis:** Irritability is 40.5% versus 43.4%, and anxiety is 33.3% versus 36.8%; both are lower in mHealth. Only dry mouth follows the stated direction.
- **Verification:** Sum the non-None severity categories by arm and compare them with the prose statement.

## F03 — Minor — Arithmetic inconsistency: site 2008 death percentage

- **Location:** `joi250093supp2_prod_1768590553.09463.pdf`, p9, eTable 6 and p8, eTable 5.
- **Source evidence:** eTable 6 reports site 2008 as `5 (7.5)` deaths; eTable 5 gives a denominator of 40.
- **Basis:** `5/40 = 12.5%`, not 7.5%.
- **Verification:** Confirm the site denominator and recalculate the percentage.

## F04 — Minor — Arithmetic inconsistency: death-cause percentages

- **Location:** `joi250093supp2_prod_1768590553.09463.pdf`, p6, eTable 4.
- **Source evidence:** With 27 usual-care deaths, “Drug user” and “Severe pneumonia” are each printed as `1 (7.4%)`.
- **Basis:** `1/27 = 3.7%`, not 7.4%. Other conventional one-decimal discrepancies include `3/52 = 5.8%` (printed 5.7%), `8/52 = 15.4%` (printed 15.2%), and `16/27 = 59.3%` (printed 59.2%).
- **Verification:** Recalculate every percentage using column totals 52, 25, and 27.

## F05 — Minor — Statistical reporting inconsistency: adverse-event percentages

- **Location:** `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p5; `joi250093supp2_prod_1768590553.09463.pdf`, p15, eTable 10.
- **Source evidence:** Main text reports nausea 23.0% versus 22.3% and diarrhea 7.5% versus 7.5%. eTable 10 gives control nausea 71/334 and mHealth diarrhea 51/699.
- **Basis:** `71/334 = 21.3%`, not 22.3%; `51/699 = 7.3%`, not 7.5%.
- **Verification:** Sum mild, moderate, and severe counts and divide by each arm total.

## F06 — Minor — Presentation inconsistency: adverse-event population unidentified

- **Location:** `joi250093supp2_prod_1768590553.09463.pdf`, pp15-16, eTable 10.
- **Source evidence:** Complete symptom blocks total 699 mHealth and 334 control, but the table does not identify this population or its missingness.
- **Basis:** These denominators differ from randomized 720/360, complete-case 667/318, and death-excluded 695/333 populations.
- **Verification:** Sum the severity rows and compare 699/334 with the documented populations and table notes.

## F07 — Minor — Statistical reporting inconsistency: ITT label after deaths excluded

- **Location:** `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p3 and p6, Table 2; `joi250093supp2_prod_1768590553.09463.pdf`, p13, eTable 9.
- **Source evidence:** The main article distinguishes primary ITT from a post hoc death-excluded analysis; Table 2 ITT is 720/360. eTable 9 calls a 695/333 death-excluded analysis ITT.
- **Basis:** `720 − 25 = 695`; `360 − 27 = 333`.
- **Verification:** Compare the eTable 9 title and denominators with the methods, Figure 1, and Table 2.

## F08 — Minor — Presentation inconsistency: eTable 6 title/body mismatch

- **Location:** `joi250093supp2_prod_1768590553.09463.pdf`, p9, eTable 6.
- **Source evidence:** The title promises death rates and unsuccessful tuberculosis treatment outcomes; the body contains only arm, site ID, and deaths.
- **Basis:** No column, row, or note presents unsuccessful-treatment outcomes.
- **Verification:** Compare the complete title with every displayed column and note.

# Rejected and Uncertain Candidates

## Uncertain — C07 — Statistical reporting inconsistency: PP versus complete-case label

- **Location:** `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p3 and p6, Table 2.
- **Source evidence:** Methods describe complete-case analysis; Table 2 labels 667/318 rows “PP.”
- **Basis:** `720 − 53 = 667`; `360 − 42 = 318`. The package does not establish whether “PP” is erroneous or the authors’ label for the same population.
- **Verification:** Consult the analysis-population specification for separate per-protocol criteria and determine whether Table 2 should say complete case.

## Rejected — C09 — Cross-document inconsistency: subgroup scheme differs from prespecified list

- **Location:** `jama_zahid_2025_oi_250093_1768590553.08463.pdf`, p3 and p5; `joi250093supp2_prod_1768590553.09463.pdf`, p12, eTable 8.
- **Compared statements:** The main article lists age, education, employment, and smoking duration as prespecified subgroups; eTable 8 combines dependent/retired and adds Reading SMS Yes/No.
- **Basis for rejection:** The added SMS-reading subgroup is document-grounded, but the package does not state that every eTable 8 subgroup was prespecified. Classifying the unlabeled inclusion as an error would be speculative.
- **Verification:** Compare the methods subgroup list with eTable 8; retain as rejected unless evidence establishes that all displayed subgroups were required to be prespecified or labeled post hoc.

# Human Adjudication Checklist

- Confirm the separate compliance record: institutional approval was documented for DOC-001 and DOC-003; DOC-002 remained Not Audited by Design.
- Adjudicate F01-F08 against the stated locations, evidence, calculations, and verification instructions.
- Resolve C07 only after obtaining the analysis-population specification; do not treat it as a confirmed issue meanwhile.
- Keep C09 rejected unless additional package evidence removes the stated uncertainty.
- Preserve all source PDFs unchanged.
