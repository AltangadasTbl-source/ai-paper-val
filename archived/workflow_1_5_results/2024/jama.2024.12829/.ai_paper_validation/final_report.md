# Human Adjudication Report

## Package Manifest

| Document ID | File | Classification | Scientific Audit Scope |
|---|---|---|---|
| basis_main_article | `jama_sun_2024_oi_240088_1746815064.14747.pdf` | Main article; 11 PDF pages | All pages audited |
| basis_results_supplement | `joi240088supp1_prod_1746815064.21247.pdf` | Results supplement; 25 PDF pages | PDF pp10–25 audited; pp3–9 Not Audited by Design; pp1–2 retained as scope evidence |
| basis_protocol_sap | `joi240088supp2_prod_1746815064.36071.pdf` | Protocol/SAP; 167 PDF pages | pp1–167 Not Audited by Design |

Native text extraction was usable for audited main-article pages and supplement tables. Result-figure text on supplement pp10–13 was sparse and selectively rendered for visual inspection; no local OCR engine was available. These limitations do not alter the locations or values below.

## AI Training Restriction Summary

This is a supplied-materials compliance screen, separate from the scientific findings, and is not legal advice.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| basis_main_article | Explicit AI Training Restriction | `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF pp10–11, footer/end matter: “© 2024 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required. The user instructed this workflow to assume permissions and continue. |
| basis_results_supplement | No AI Training Restriction Located in Provided Materials | `joi240088supp1_prod_1746815064.21247.pdf`, PDF p1: “This supplemental material has been provided by the authors to give readers additional information about their work.” Focused rights pages, text-layer keyword screen, and embedded metadata contained no AI-training, fine-tuning, or model-improvement restriction. | No |
| basis_protocol_sap | No AI Training Restriction Located in Provided Materials | `joi240088supp2_prod_1746815064.36071.pdf`, PDF p1, lines 3–4: “This trial protocol has been provided by the authors to give readers additional information about their work.” Entire supplied PDF and embedded metadata screened; no relevant restriction located. | No |

## Scientific Findings

1. **Category:** Statistical reporting inconsistency  
   **Priority:** Major  
   **Location:** `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p8 / printed p1066, Table 2, “Any stroke outside the territory…within 1 y.”  
   **Compared values:** 3/249 (1.2%) vs 4/252 (1.6%); incidence difference −0.4 percentage points; 95% CI −2.4 to −1.7.  
   **Basis:** `100 × (3/249 − 4/252) = −0.382`; −0.4 is outside [−2.4, −1.7]. The interval also conflicts with HR 0.76 (95% CI 0.17–3.40) and P=.72.  
   **Verification:** Check the upper CI endpoint and its sign against the analysis output.

2. **Category:** Cross-document inconsistency  
   **Priority:** Major  
   **Location:** `joi240088supp1_prod_1746815064.21247.pdf`, PDF p13, Figure S5; PDF p24, Table S11 and footnote b.  
   **Compared values:** Figure S5 labels AMM N=252, but categories total `169+58+13+3+3+2+1=249` and percentages use 249. Scores >2 total 4 BA and 9 AMM; Table S11 defines disabling stroke as mRS >2 at 1 year and reports 6 BA and 18 AMM.  
   **Basis:** The figure distribution conflicts with its displayed denominator and with the identically defined Table S11 outcome; three omitted AMM patients cannot reconcile 9 with 18.  
   **Verification:** Sum scores 0–6 and scores 3–6 in each Figure S5 arm, then compare with arm labels and Table S11.

3. **Category:** Cross-document inconsistency  
   **Priority:** Major  
   **Location:** Supplement PDF p19, Table S6; main article PDF p8, Table 2; supplement PDF p21, Table S8.  
   **Compared values:** Table S6 headers are 249/252 but show 9 (3.9%) vs 34 (13.5%). Main ITT Table 2 shows 11/249 (4.4%) vs 34/252 (13.5%); PPS Table S8 shows 9/233 (3.9%).  
   **Basis:** `9/249=3.6%`, not 3.9%; the BA value matches PPS while the header and AMM value match ITT.  
   **Verification:** Identify Table S6’s intended population and confirm raw counts and denominators used for its adjusted HR.

4. **Category:** Presentation inconsistency  
   **Priority:** Minor  
   **Location:** Supplement PDF p20, Table S7; PDF p23, Table S10.  
   **Compared values:** Headers show 233/238, but site totals are 256+245=501 and events total 11 BA vs 34 AMM. Site percentages reconstruct denominators 138/118 and 111/134, totaling 249/252.  
   **Basis:** Table S10 identifies 249/252 as ITT and 233/238 as PPS; Table S7’s body represents ITT data under PPS-sized headers.  
   **Verification:** Reconstruct each arm-by-site denominator and correct the Table S7 headers or body.

5. **Category:** Presentation inconsistency  
   **Priority:** Minor  
   **Location:** Supplement PDF p21, Table S8; PDF p23, Table S10; main article PDF p5, Figure 1.  
   **Compared values:** The PPS table headers show 249/252; values including 9 (3.9%), 33 (13.9%), 6 (2.6%), and 20 (8.4%) use 233/238.  
   **Basis:** Table S10 and Figure 1 identify 233/238 as PPS denominators.  
   **Verification:** Recalculate representative rates under both denominator pairs and confirm intended PPS headers.

6. **Category:** Presentation inconsistency  
   **Priority:** Minor  
   **Location:** Supplement PDF p22, Table S9; PDF p23, Table S10.  
   **Compared values:** Table S9 is titled ATS but headers show 249/252. Values including 11 (4.5%) and 34 (13.4%) use ATS denominators 247/254. The cell 8 (3.3%) fails under both 247 and 249, each rounding to 3.2%.  
   **Basis:** Title and body conflict with displayed headers; one percentage remains unreconciled.  
   **Verification:** Confirm ATS arm sizes, correct headers, and identify the denominator used for 8 (3.3%).

7. **Category:** Cross-document inconsistency  
   **Priority:** Minor  
   **Location:** Main article PDF p4 / printed p1062, Patient Population; supplement PDF p20, Table S7; supplement PDF p12, Figure S3.  
   **Compared values:** Main text reports 258/501 from the lead center; Table S7 assigns 256 of 501 to Beijing Tiantan and 245 elsewhere. Figure S3 reports 258 among the pre-exclusion enrollment population of 512.  
   **Basis:** `256+245=501`; the narrative pairs the pre-exclusion center count with the post-exclusion denominator.  
   **Verification:** Trace the 11 exclusions by center and confirm whether the analyzed lead-center numerator is 256 or 258.

8. **Category:** Cross-document inconsistency  
   **Priority:** Minor  
   **Location:** Main article PDF p7 / printed p1065, procedural-complications paragraph; supplement PDF p17, Table S4.  
   **Compared values:** Main text reports arterial perforation 0.4% and cites Table S4; Table S4 reports 0 (0.0%).  
   **Basis:** The same named complication is reported as approximately one event versus zero.  
   **Verification:** Compare the event record supporting the narrative with the Table S4 row and correct the count or percentage.

9. **Category:** Statistical reporting inconsistency  
   **Priority:** Minor  
   **Location:** Supplement PDF p24, Table S11, rows marked footnote c and footnotes c/d.  
   **Compared values:** Rows marked “Chi-square test” report P=.84 for 12/249 vs 14/252, P=.35 for 7/249 vs 12/252, and P=.02 for 6/249 vs 18/252. Two-sided Fisher exact results are .840916, .350060, and .019621; ordinary Pearson chi-square results are .710285, .253089, and .013126.  
   **Basis:** Displayed P values reproduce Fisher exact results rather than the stated chi-square method; footnote d separately identifies Fisher testing.  
   **Verification:** Reproduce both tests and confirm whether the three row markers or P values were entered incorrectly.

## Rejected and Uncertain Candidates

- **Rejected — C9, Arithmetic inconsistency:** Five independently located count/percentage discrepancies were verified but bundled into one candidate. The critic rejected the bundle as overly broad; its components were lower priority than the nine retained findings.
- **Uncertain candidates:** None.

## Human Adjudication Checklist

- Confirm each source value and location in the original PDFs.
- For Finding 1, verify the Table 2 CI sign and endpoint against analysis output.
- For Findings 2–8, determine the intended population, denominator, count, or table/figure label.
- For Finding 9, reproduce the stated and displayed statistical tests and resolve method markers or P values.
- Record adjudication outcome for each finding: confirmed, corrected, or not confirmed.
- Complete the required Human Compliance Review for the main article’s AI-training restriction; this report provides no legal conclusion.
