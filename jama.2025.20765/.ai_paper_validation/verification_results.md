# Evidence Verification Results

Verification stage: one round against original DOC-001 and DOC-003 PDFs. Outcome: 9 Verified, 1 Uncertain, 0 Rejected.

## C01 — Verified — Missing mHealth cluster in prior-attempt table

- DOC-003 p4 eTable 2 has 17 mHealth sites (680 participants), omits site 2012, and its “Yes” counts total 168.
- DOC-001 p5 Table 1 reports 178/720; DOC-003 p8 eTable 5 identifies site 2012 as an mHealth cluster of 40.
- Calculation: 178 − 168 = 10 prior attempts; 720 − 680 = 40 participants.
- Human verification: Sum the 17 eTable 2 rows, compare with Table 1, and confirm site 2012 in eTable 5.

## C02 — Verified — Site 2008 death percentage

- DOC-003 p9 eTable 6 reports site 2008 as `5 (7.5)`; DOC-003 p8 eTable 5 gives its denominator as 40.
- Calculation: 5/40 = 12.5%, not 7.5%.
- Human verification: Locate site 2008 on both pages and divide 5 by 40.

## C03 — Verified — Death-cause percentages

- DOC-003 p6 eTable 4 has 27 usual-care deaths but reports Drug user 1 (7.4%) and Severe pneumonia 1 (7.4%).
- Calculation: 1/27 = 3.7%, not 7.4%. Additional discrepancies: 3/52 = 5.8%, printed 5.7%; 8/52 = 15.4%, printed 15.2%; 16/27 = 59.3%, printed 59.2%.
- Human verification: Recalculate each table percentage from column totals 52, 25, and 27.

## C04 — Verified — Adverse-event percentages

- DOC-001 p5 reports nausea 23.0% vs 22.3% and diarrhea 7.5% vs 7.5%.
- DOC-003 p15 eTable 10 gives control nausea 71/334 = 21.3%, not 22.3%, and mHealth diarrhea 51/699 = 7.3%, not 7.5%.
- Human verification: Sum mild, moderate, and severe counts and divide by each arm total.

## C05 — Verified — Adverse-event direction reversed

- DOC-001 p5 states dry mouth, irritability, and anxiety were more common in mHealth.
- DOC-003 p15 eTable 10 gives irritability 283/699 = 40.5% vs 145/334 = 43.4%, and anxiety 233/699 = 33.3% vs 123/334 = 36.8%.
- Basis: Irritability and anxiety are lower, not higher, in mHealth; dry mouth alone has the stated direction.
- Human verification: Compare summed non-None categories with the prose sentence.

## C06 — Verified — Unidentified adverse-event analysis population

- DOC-003 pp15-16 eTable 10 totals 699 mHealth and 334 control for each complete symptom block without identifying the population or missingness.
- These differ from randomized 720/360, complete-case 667/318, and death-excluded 695/333.
- Human verification: Add four severity rows and compare 699/334 with the documented populations and table notes.

## C07 — Uncertain — “PP” versus complete-case label

- DOC-001 p3 describes complete-case analysis; p6 Table 2 labels rows PP with 667/318.
- 720 − 53 = 667 and 360 − 42 = 318, so PP equals the described complete-case population.
- Uncertainty: The package does not prove PP is erroneous rather than the authors’ label for that same population; no separate PP eligibility criteria are reported.
- Human verification: Obtain the analysis-population specification and determine whether Table 2 should say complete case.

## C08 — Verified — ITT label after excluding deaths

- DOC-001 p3 distinguishes primary ITT from a post hoc analysis excluding deaths; Table 2 ITT is 720/360.
- DOC-003 p13 eTable 9 is titled post-hoc sensitivity analysis (intention to treat) after excluding deaths and uses 695/333.
- 720 − 25 = 695; 360 − 27 = 333.
- Human verification: Compare eTable title/denominators with methods, Figure 1, and Table 2.

## C09 — Verified — Subgroup scheme differs from stated prespecified list

- DOC-001 p3 prespecifies age, education, employment (active, dependent, retired), and smoking duration.
- DOC-003 p12 eTable 8 combines dependent/retired and adds Reading SMS Yes/No; DOC-001 p5 summarizes SMS-reading without identifying it as post hoc.
- Human verification: Compare every methods subgroup and category with eTable 8 and the p5 summary.

## C10 — Verified — eTable 6 title/body mismatch

- DOC-003 p9 eTable 6 title names death rates and unsuccessful TB treatment outcomes.
- Body contains only arm, site ID, and deaths n(%); no unsuccessful-treatment outcome appears.
- Human verification: Compare the complete table title with all displayed columns and notes.

