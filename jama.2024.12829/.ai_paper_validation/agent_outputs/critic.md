# Critic Stage — Final Scientific Issues

Retained: 9. Rejected: 1. Uncertain: 0. No new issues were sought.

## 1. Major — Statistical reporting inconsistency: estimate outside its confidence interval

- Location: `jama_sun_2024_oi_240088_1746815064.14747.pdf`, PDF p. 8 / printed p. 1066, Table 2, “Any stroke outside the territory…within 1 y.”
- Evidence: 3/249 (1.2%) vs 4/252 (1.6%); incidence difference −0.4 percentage points; 95% CI −2.4 to −1.7.
- Basis: `100 × (3/249 − 4/252) = −0.382`; −0.4 is outside [−2.4, −1.7]. The interval also conflicts with HR 0.76 (95% CI 0.17–3.40) and P=.72.
- Verify: check the upper CI endpoint and its sign against the analysis output.

## 2. Major — Cross-document inconsistency: 1-year mRS distribution and disabling-stroke counts

- Location: `joi240088supp1_prod_1746815064.21247.pdf`, p. 13, Figure S5; p. 24, Table S11 and footnote b.
- Evidence: Figure S5 labels AMM N=252, but its categories total `169+58+13+3+3+2+1=249` and its percentages use 249. Scores >2 total 4 BA and 9 AMM. Table S11 defines disabling stroke as mRS >2 at 1 year but reports 6 BA and 18 AMM.
- Basis: the figure distribution is inconsistent with its displayed denominator and the identically defined Table S11 outcome. Three omitted AMM patients cannot reconcile 9 with 18.
- Verify: sum scores 0–6 and scores 3–6 in each Figure S5 arm, then compare with the arm labels and Table S11.

## 3. Major — Cross-document inconsistency: Table S6 mixes analysis populations

- Location: supplement p. 19, Table S6; main article p. 8, Table 2; supplement p. 21, Table S8.
- Evidence: Table S6 headers are 249/252 but show 9 (3.9%) vs 34 (13.5%). Main ITT Table 2 shows 11/249 (4.4%) vs 34/252 (13.5%); PPS Table S8 shows 9/233 (3.9%).
- Basis: `9/249=3.6%`, not 3.9%; the BA value matches PPS while the header and AMM value match ITT. Center adjustment cannot itself alter a displayed raw count’s denominator.
- Verify: identify Table S6’s intended population and confirm the raw counts and denominators used for its adjusted HR.

## 4. Minor — Presentation inconsistency: Table S7 headers conflict with ITT site data

- Location: supplement p. 20, Table S7; p. 23, Table S10.
- Evidence: headers show 233/238, but site totals are 256+245=501 and events total 11 BA vs 34 AMM. The site percentages reconstruct denominators 138/118 and 111/134, totaling 249/252.
- Basis: Table S10 identifies 249/252 as ITT and 233/238 as PPS; Table S7’s body represents ITT data under PPS-sized headers.
- Verify: reconstruct each arm-by-site denominator and correct the Table S7 headers or body.

## 5. Minor — Presentation inconsistency: Table S8 PPS body has ITT headers

- Location: supplement p. 21, Table S8; p. 23, Table S10; main article p. 5, Figure 1.
- Evidence: the title identifies PPS, headers show 249/252, while values including 9 (3.9%), 33 (13.9%), 6 (2.6%), and 20 (8.4%) use 233/238.
- Basis: Table S10 and Figure 1 identify 233/238 as the PPS denominators.
- Verify: recalculate representative rates under both denominator pairs and confirm the intended PPS headers.

## 6. Minor — Presentation inconsistency: Table S9 ATS body has ITT headers

- Location: supplement p. 22, Table S9; p. 23, Table S10.
- Evidence: Table S9 is titled ATS but headers show 249/252. Values such as 11 (4.5%) and 34 (13.4%) use the Table S10 ATS denominators 247/254. The cell 8 (3.3%) also fails under both 247 and 249: each rounds to 3.2%.
- Basis: the title and body conflict with the displayed headers; one percentage remains unreconciled under either displayed or ATS arm size.
- Verify: confirm ATS arm sizes, correct the headers, and identify the denominator used for 8 (3.3%).

## 7. Minor — Cross-document inconsistency: lead-center numerator

- Location: main article p. 4 / printed p. 1062, Patient Population; supplement p. 20, Table S7; supplement p. 12, Figure S3.
- Evidence: main text reports 258/501 from the lead center; Table S7 assigns 256 of the same 501 to Beijing Tiantan and 245 elsewhere. Figure S3 reports 258 among the pre-exclusion enrollment population of 512.
- Basis: `256+245=501`; the narrative’s 258 appears to use the pre-exclusion center count with the post-exclusion denominator.
- Verify: trace the 11 exclusions by center and confirm whether the analyzed lead-center numerator is 256 or 258.

## 8. Minor — Cross-document inconsistency: arterial perforation frequency

- Location: main article p. 7 / printed p. 1065, procedural-complications paragraph; supplement p. 17, Table S4.
- Evidence: main text reports arterial perforation 0.4% and cites Table S4; Table S4 reports 0 (0.0%).
- Basis: the same named complication is reported as approximately one event versus zero.
- Verify: compare the event record supporting the narrative with the Table S4 row and correct the count or percentage.

## 9. Minor — Statistical reporting inconsistency: Table S11 test markers

- Location: supplement p. 24, Table S11, rows marked footnote c and footnotes c/d.
- Evidence: rows marked “Chi-square test” report P=.84 for 12/249 vs 14/252, P=.35 for 7/249 vs 12/252, and P=.02 for 6/249 vs 18/252. Two-sided Fisher exact calculations give .840916, .350060, and .019621; ordinary Pearson chi-square gives .710285, .253089, and .013126. Footnote d separately identifies Fisher testing.
- Basis: the displayed P values reproduce Fisher exact results rather than the stated chi-square method.
- Verify: reproduce both tests and confirm whether the three row markers or P values were entered incorrectly.

## Rejected verified candidate

- C9 was rejected from the final issue list. Its five count/percentage discrepancies are document-grounded but independent cells across multiple locations bundled into one candidate. Retaining the bundle would be overly broad, and its individual components are lower priority than the nine retained issues.

No verified candidate was classified as Uncertain.
