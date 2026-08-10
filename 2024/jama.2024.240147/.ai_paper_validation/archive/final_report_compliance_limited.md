# Report Status: Human Adjudication Required

## 1. Package Manifest

| Document | Source file | Role | Pages | Audit status |
|---|---|---|---:|---|
| DOC-001 | jama_arleth_2024_oi_240147_1738701765.27201.pdf | Main article | 11 | Withheld pending Human Compliance Review |
| DOC-002 | joi240147supp1_prod_1738701765.28701.pdf | Trial protocol and statistical analysis plan | 103 | Not Audited by Design: no triggered protocol-to-report comparison |
| DOC-003 | joi240147supp2_prod_1738701765.29201.pdf | Results supplement with eMethods, eFigure, and eTables 1-11 | 26 | Audited |
| DOC-004 | joi240147supp3_prod_1738701765.30201.pdf | Nonauthor collaborator list | 3 | Not Audited by Design: administrative content without result tables, figures, or claims |
| DOC-005 | joi240147supp4_prod_1738701765.30701.pdf | Data-sharing statement | 1 | Not Audited by Design: administrative content without result tables, figures, or claims |

DOC-001 was withheld pending Human Compliance Review because source pages 1-11 expressly reserve rights for text and data mining, AI training, and similar technologies. Accordingly, this scientific audit is limited to DOC-003, and cross-document/main-article validation is incomplete.

## 2. AI Training Restriction Summary

- DOC-001: Explicit AI Training Restriction; scientific processing withheld pending human clearance.
- DOC-002, DOC-003, DOC-004, and DOC-005: No explicit AI-training statement located. Permission is not inferred.
- DOC-003 was selected for result-relevant audit. DOC-002, DOC-004, and DOC-005 remain Not Audited by Design for the reasons stated above.

## 3. Scientific Findings

| ID | Category | Severity | Exact location | Compared values or statements | Calculation or logical basis | Verification instruction |
|---|---|---|---|---|---|---|
| C1 | Arithmetic inconsistency | Minor | DOC-003, p. 14, eTable 1, receiving trauma center | Restrictive: 335/750 shown 44.4% vs 44.7%; 173/750 22.9% vs 23.1%; 92/750 12.2% vs 12.3%; 50/750 7.2% vs 6.7%. Liberal: 348/758 45.7% vs 45.9%; 177/758 23.2% vs 23.4%; two 93/758 cells 12.2% vs 12.3%; 47/758 6.7% vs 6.2%. | Printed percentages do not equal the displayed fractions; 100/750 = 13.3% is correct. | Recalculate each cited cell using the printed denominators and verify source values. |
| C2 | Presentation inconsistency | Minor | DOC-003, p. 15, eTable 2, injury mechanism - firearm, restrictive group | Firearm is 8/724 (1.1%); all other restrictive mechanism rows use denominator 742, and the 13 mechanism numerators sum to 742. | The firearm denominator differs from the other mechanism denominators; no correction is established. | Check the source table and denominator definition before changing the cell. |
| C3 | Arithmetic inconsistency | Minor | DOC-003, p. 15, eTable 2, arrival mode - Walk-in, liberal group | 4/743 is shown as 5.3%. | 4/743 = 0.5% when rounded to one decimal place. | Verify the numerator, denominator, and displayed percentage. |
| C4 | Arithmetic inconsistency | Minor | DOC-003, p. 15, eTable 2, surgical specialty - vascular surgery, liberal group | 0/747 is shown as 1.1%. | 0/747 = 0.0%. | Verify the numerator, denominator, and displayed percentage. |
| C5 | Presentation inconsistency | Minor | DOC-003, p. 19, eTable 6 footnotes; compare p. 18, eTable 5 | An asterisk footnote addresses postdischarge pneumonia, but eTable 6 has no corresponding row or asterisk marker. The topic appears in eTable 5 with a paragraph-mark footnote. | The eTable 6 asterisk footnote is unlinked within that table. | Confirm intended footnote placement and marker in the source layout. |
| C6 | Arithmetic inconsistency | Minor | DOC-003, p. 20, eTable 7, AIS <3, liberal group | 48/473 is shown as 9.2%. | 48/473 = 10.1% when rounded to one decimal place. | Verify the numerator, denominator, and displayed percentage. |
| C7 | Presentation inconsistency | Minor | DOC-003, p. 24, eTable 10 header and cited cells | Header states "No./total No. (%)"; values include 55/750 (45), 67/758 (55), 174/750 (51), and 165/758 (49). | Using printed denominators yields 7.3%, 8.8%, 23.2%, and 21.8%; displayed percentages instead use row totals 122 and 339. | Confirm denominator conventions and revise the header, denominators, or percentages as applicable. |
| C8 | Participant flow inconsistency | Major | DOC-003, p. 24, eTable 10, postrandomization exclusions | The table states N = 130 exclusions after randomization; group counts are 55 and 67. | 55 + 67 = 122, leaving 8 participants unexplained; no applicable footnote is provided. | Reconcile the eight participants and document the correct flow counts or explanatory note. |
| C9 | Presentation inconsistency | Minor | DOC-003, p. 25, eTable 11, primary outcome - missing counted as event, restrictive group | The cell is printed as 135//750 (18.0%). | 135/750 = 18.0%; the duplicated slash is a formatting defect. | Confirm and correct the cell typography. |

## 4. Rejected and Uncertain Candidates

No verifier-rejected candidates were reported.

| ID | Category | Status | Exact location | Compared values or statements | Logical basis | Verification instruction |
|---|---|---|---|---|---|---|
| C10 | Statistical reporting inconsistency | Uncertain | DOC-003, p. 17, eTable 4 and p. 20, eTable 7, All patients | The same counts and unadjusted OR are reported; adjusted OR is 0.98 with CI 0.68 to 1.41 in eTable 4 and 0.98 with CI 0.68 to 1.39 in eTable 7. | Identical adjusted models are not established from the available material. | Confirm model specifications, precision, and source calculations before treating the CI difference as an error. |

## 5. Human Adjudication Checklist

- Obtain a human compliance disposition for DOC-001 before any main-article audit.
- If DOC-001 is cleared, re-audit it and perform cross-document comparisons.
- Adjudicate each candidate C1-C10.
- Reconcile the eight participants identified in C8.
- Confirm eTable 10 denominator conventions.
- Document final accept/reject status and any corrections.
