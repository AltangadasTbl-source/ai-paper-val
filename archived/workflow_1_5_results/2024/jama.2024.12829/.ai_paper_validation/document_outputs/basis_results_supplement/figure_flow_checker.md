# Figure/flow/table visual audit — `basis_results_supplement`

- **Source PDF:** `joi240088supp1_prod_1746815064.21247.pdf`
- **Audited scope:** PDF pp. 10–25 only. PDF pp. 3–9 were not opened or audited.
- **Comparison sources:** designated main-article pp. 1–11, `main_text_extraction.md`, and `results_supplement_evidence_map.md`.
- **Source modified:** No.

## Supported local candidates

### S1 — Presentation inconsistency: three sequential CEC reviews are all labelled “2nd meeting”

- **Location:** PDF p. 10, Figure S1, four dated CEC meeting boxes.
- **Visible/source values:** The boxes are dated 2021-05-30, 2021-11-20, 2022-09-07, and 2023-04-10. The first is labelled “1st meeting,” while each of the other three is labelled “2nd meeting.”
- **Logical basis:** Four chronologically distinct review meetings cannot all have the displayed ordinal sequence 1st, 2nd, 2nd, 2nd. The associated case dispositions do reconcile within each box (19=10+6+3; 27=24+1+2; 26=23+2+1; 15=13+1+1), so the candidate is limited to the ordinal labels.
- **Verification instruction:** Inspect the headings of all four Figure S1 meeting boxes on PDF p. 10; verify whether the 2022 and 2023 boxes should read “3rd” and “4th.”
- **Status:** Supported candidate.

### S2 — Cross-document inconsistency: Figure S5 one-year mRS counts conflict with its denominator and Table S11

- **Location:** PDF p. 13, Figure S5 (1-year mRS); PDF p. 24, Table S11, “Disabling stroke” row and footnote b.
- **Visible/source values:** Figure S5 labels BA N=249 and displays mRS 0–6 counts 195, 46, 4, 2, 1, 0, 1 (sum 249). It labels AMM N=252 but displays 169, 58, 13, 3, 3, 2, 1 (sum **249**); its percentages sum 100.0% and the leading 67.9% and 23.3% equal 169/249 and 58/249, not divisions by 252. Figure S5 therefore shows mRS>2 counts of **4 BA and 9 AMM**. Table S11 defines disabling stroke as “modified Rankin Scale >2 at 1 year” but reports **6 BA and 18 AMM**.
- **Logical basis:** The AMM bar is internally inconsistent with its displayed N=252. Independently, the plotted mRS>2 category counts do not equal the Table S11 counts under Table S11’s explicit definition; even assigning all 3 AMM patients omitted from the plotted 249 to mRS>2 would yield 12, not 18. This is not an explained ITT/PPS/ATS difference because both items display the ITT arm labels and Table S11 uses n=249/n=252.
- **Verification instruction:** Read each Figure S5 category callout by legend color, sum the AMM counts and sum scores 3–6 in both arms; compare with the Figure S5 arm labels and Table S11 footnote b/counts.
- **Status:** Supported candidate.

### S3 — Arithmetic inconsistency: Table S1 balloon-arm non-border-zone percentage is incompatible with its count

- **Location:** PDF p. 14, Table S1, ischemic-stroke subrows “Border zone infarct” and “Non-zone infarct.”
- **Visible/source values:** Balloon arm: ischemic stroke n=215; border-zone infarct 84 (39.1%); non-zone infarct 131 (**61.9%**). The counts reconcile, 84+131=215.
- **Logical basis:** 131/215=60.9%, not 61.9%; the displayed percentages total 101.0%. The AMM companion values, 85/208=40.9% and 123/208=59.1%, reconcile.
- **Verification instruction:** Inspect the BA non-zone-infarct cell on PDF p. 14 and divide 131 by the displayed ischemic-stroke denominator 215.
- **Status:** Supported candidate.

### S4 — Presentation inconsistency: Table S2 contains an orphan “No. Patients evaluated” row

- **Location:** PDF p. 15, Table S2, immediately after “Current smoking, n (%)” and before the next “No. Patients evaluated” row for activity level.
- **Visible/source values:** A standalone row displays BA 249/249/NA and AMM 252/252/NA but has no characteristic/result row associated with it. The following separate denominator row (248/243/247 vs 249/251/246) is directly followed by “Activity level per week.”
- **Logical basis:** The first denominator row has no visible measure to which its six denominators apply, leaving an unlabeled/missing table entry. No scientific value is inferred from the blank.
- **Verification instruction:** Inspect the consecutive rows between current smoking and activity level on PDF p. 15 and confirm whether a characteristic/result row was omitted.
- **Status:** Supported candidate.

### S5 — Cross-document inconsistency: arterial-perforation frequency is 0 in Table S4 but 0.4% in the main text

- **Location:** Supplement PDF p. 17, Table S4, procedural-complications rows; main article PDF p. 7 / print p. 1065, paragraph immediately above Discussion.
- **Visible/source values:** Table S4 reports arterial perforation **0 (0.0%)**. The main article states “arterial perforation, **0.4%**” for the balloon-angioplasty group. Table S4’s other nearby complication values align with the narrative (vasospasm 1.2%, dissection 14.5%, pseudoaneurysm 0.0%, occlusion 0.4%, rupture 0.0%, hemorrhage 0.4%, thrombosis 1.7%).
- **Logical basis:** The two supplied documents report different frequencies for the same named balloon-arm procedural complication. The 241-procedure denominator footnote does not reconcile zero with 0.4%.
- **Verification instruction:** Compare the arterial-perforation row on supplement PDF p. 17 with the complication list on main-article PDF p. 7 and check the underlying intended count (0 versus 1).
- **Status:** Supported candidate.

### S6 — Cross-document inconsistency: Table S6 mixes an ITT header with a per-protocol balloon count/rate

- **Location:** PDF p. 19, Table S6, only outcome row; main article PDF pp. 7–8, Figure 2 overall row and Table 2 primary outcome; supplement PDF p. 21, Table S8.
- **Visible/source values:** Table S6 labels BA n=249 and AMM n=252 but reports primary outcome **9 (3.9%)** vs 34 (13.5%). In the main ITT result the values are **11/249 (4.4%)** vs 34/252 (13.5%). Table S8’s PPS result is 9/233=3.9%.
- **Logical basis:** Internally, 9/249=3.6%, not 3.9%. The BA count/rate exactly matches the PPS values while the Table S6 header and AMM count/rate match ITT. Center adjustment can alter the adjusted HR but does not explain displaying a raw count/rate that conflicts with its stated denominator.
- **Verification instruction:** Recalculate 9/249; compare Table S6’s displayed raw values with main Table 2/Figure 2 and supplement Table S8; confirm the intended Table S6 analysis population and BA event count.
- **Status:** Supported candidate.

### S7 — Presentation inconsistency: Table S7 header shows PPS arm sizes for ITT site rows

- **Location:** PDF p. 20, Table S7, arm headers and both site rows; PDF p. 23, Table S10 population denominators.
- **Visible/source values:** Table S7 headers say BA N=233 and AMM N=238. The site totals are 256+245=501, and event counts sum to BA 4+7=11 and AMM 19+15=34. The row percentages imply site-by-arm denominators about 138/118 at Beijing Tiantan and 111/134 at other centers, summing to **249 BA and 252 AMM**. Table S10 explicitly labels 249/252 as ITT and 233/238 as PPS.
- **Logical basis:** The row data are the ITT primary-result counts and ITT site population, not PPS. Thus the displayed 233/238 headers are not an explained analysis-population difference; they are incompatible with the table body.
- **Verification instruction:** Sum the two site event counts by arm, reconstruct the site-by-arm denominators from n(%), and compare the resulting 249/252 with Table S10 and Figure 1.
- **Status:** Supported candidate.

### S8 — Presentation inconsistency: Table S8 PPS title/body conflict with ITT arm headers

- **Location:** PDF p. 21, Table S8 title, arm headers, and outcome rows; PDF p. 23, Table S10 PPS denominators.
- **Visible/source values:** Table title says per-protocol population, but the headers say BA n=249 and AMM n=252. Every displayed rate is based on **233 and 238**, including 9/233=3.9%, 33/238=13.9%, 6/233=2.6%, and 20/238=8.4%. Table S10 explicitly gives PPS N=233/N=238.
- **Logical basis:** The table body and title consistently identify PPS; only the headers show ITT sizes. This is a mislabeled population header, not a conflict caused by using a legitimate alternative analysis.
- **Verification instruction:** Recalculate several Table S8 percentages under both header denominators and compare with Table S10’s PPS row.
- **Status:** Supported candidate.

### S9 — Presentation inconsistency: Table S9 ATS title/body conflict with ITT arm headers

- **Location:** PDF p. 22, Table S9 title, arm headers, and outcome rows; PDF p. 23, Table S10 ATS denominators.
- **Visible/source values:** Table title says as-treated population, but the headers say BA n=249 and AMM n=252. The primary outcome values **11 (4.5%)** and **34 (13.4%)** correspond to 11/247 and 34/254. Other body rates likewise fit ATS denominators (eg, 19/254=7.5%, 21/254=8.3%). Table S10 explicitly gives ATS N=247/N=254.
- **Logical basis:** The body and title use ATS, while the headers show ITT sizes. The within-30-day BA display 8 (3.3%) also warrants checking because 8/247 rounds to 3.2%, but the header mismatch is independently document-verifiable.
- **Verification instruction:** Recalculate the Table S9 rates using 247/254 and 249/252, then compare with Table S10’s ATS denominators; separately verify the intended rounding/denominator for 8 (3.3%).
- **Status:** Supported candidate.

## Explicit exclusions / non-candidates

- Supplement Figure S2 ends at 512 enrolled, matching the 512 randomized in main Figure 1; this is recruitment, not the 501-person primary-analysis population.
- Figure S3 center counts sum to 512. Table S7’s 501 site total is the ITT analysis population after 11 post-randomization exclusions, so the difference itself is explained.
- Table S4 uses 241 procedure recipients for procedural percentages and states this in footnote a; its n=249 arm label alone was not treated as a contradiction.
- Protocol/SAP/administrative pages and supplement pp. 3–9 were not inspected.

