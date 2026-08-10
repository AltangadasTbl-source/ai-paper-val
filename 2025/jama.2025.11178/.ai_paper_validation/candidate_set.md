# Deduplicated Candidate Set for Evidence Verification

Coordinator selection date: 2026-07-22

Candidate count: 10. These candidates were deduplicated and prioritized from the three checker outputs. No new issue was added.

## C01 — Follow-up-pattern counts do not reconcile

- Category: Participant flow inconsistency / Arithmetic inconsistency
- Location: DOC-005-RESULTS, PDF p. 7, eTable 1; corroborating DOC-001-MAIN PDF p. 5, Figure 1; DOC-006-XLSX sheet `eTable 3`, B2:E3.
- Evidence to verify: eTable 1 reports N=2331 and pattern counts 295, 188, 283, and 1568, which sum to 2334. Nonzero patterns sum to 2039 rather than 2036. By arm, painTRAINER sums to 777 rather than 776 and health coach to 780 rather than 778. The workbook partitions N=2331 as 295+468+1568.

## C02 — eTable 3 confidence intervals and P values conflict

- Category: Statistical reporting inconsistency
- Location: DOC-005-RESULTS, PDF p. 8, eTable 3.
- Evidence to verify: Seven coefficient rows have 95% CIs excluding 0 but displayed P>.05: pattern 2 (-0.28, -0.47 to -0.08, .150); pattern 1 (-0.20, -0.36 to -0.03, .226); pattern 2 by painTRAINER (-0.30, -0.58 to -0.02, .280); pattern 2 by health coach (-0.47, -0.74 to -0.19, .090); site 3 (0.19, 0.08 to 0.29, .069); site 4 (0.15, 0.05 to 0.24, .124); second AA-degree row (0.16, 0.07 to 0.25, .077).

## C03 — Workbook percentage is incompatible with its count and denominator

- Category: Arithmetic inconsistency
- Location: DOC-006-XLSX, sheet `eTable 3`, E82 with denominator E3 and missing count E83.
- Evidence to verify: E82 reports `711 (73.2)` for current depression in the All Observed N=1568 group; E83 reports 2 missing. `711/(1568-2)=45.4%`, not 73.2%. Counts across groups sum correctly to 1116 and the overall percentage is internally consistent.

## C04 — Main Table 3 standardized-effect block is internally invalid

- Category: Statistical reporting inconsistency / Presentation inconsistency
- Location: DOC-001-MAIN, Table 3, PDF pp. 10-11 / JAMA pp. 601-602, with footnote d.
- Evidence to verify: Multiple SMD point estimates fall outside their own printed 95% CIs (including pain severity, pain intensity, pain-related interference, and PGIC-pain at 12 months); social-role and physical-function SMD intervals repeatedly print the larger endpoint before the smaller endpoint; several SMD signs oppose the corresponding adjusted mean-difference signs even though footnote d defines SMD as the mean difference divided by a positive SD. Confirm whether these are manifestations of a column-mapping/transcription error and identify which subclaims are verified.

## C05 — Repeated 3-month pain-severity SMDs differ between text and Table 3

- Category: Statistical reporting inconsistency
- Location: DOC-001-MAIN, Results—Secondary Outcomes, PDF p. 7 / JAMA p. 598; Table 3, PDF p. 10 / JAMA p. 601.
- Evidence to verify: Text reports painTRAINER vs usual care SMD -0.26 and health coach vs usual care -0.36; Table 3 reports -0.25 and -0.34 for the same outcome, time point, and comparisons.

## C06 — eTable 4 duplicates one 3-month treatment comparison

- Category: Presentation inconsistency
- Location: DOC-005-RESULTS, PDF p. 9, eTable 4.
- Evidence to verify: `Health Coach vs. painTRAINER 3M` appears twice with identical RR 1.20, 95% CI 1.03 to 1.40, P=.019, suggesting a duplicated or displaced row.

## C07 — eTables 3 and 4 do not uniquely label education/site coefficients

- Category: Presentation inconsistency
- Location: DOC-005-RESULTS, PDF pp. 8-9, eTables 3-4.
- Evidence to verify: Each table has two distinct rows both labeled AA degree vs high school or less but with unequal estimates. eTable 4 also has three rows labeled only `Site`, whereas eTable 3 distinguishes Site 2, Site 3, and Site 4.

## C08 — eTable 8 labels impossible pre-enhancement 3-month counts

- Category: Participant flow inconsistency / Presentation inconsistency
- Location: DOC-005-RESULTS, PDF p. 14, eTable 8, first subset header.
- Evidence to verify: Header says N=454, 366 with at least one follow-up, and PT=149, HC=153, UC=152 `at 3-months`. The arm counts sum to all 454 randomized participants, which cannot be observed 3-month counts when only 366 had any follow-up.

## C09 — eTable 9 calls explicitly unadjusted RRs adjusted

- Category: Presentation inconsistency
- Location: DOC-005-RESULTS, PDF p. 15, section heading/lead-in, eTable 9 title, and footnote b.
- Evidence to verify: Section and footnote say no adjustment, weighting, or imputation and RRs calculated without adjustment; title says `adjusted relative risk`.

## C10 — eTable 11 treatment columns and summary-statistic labels conflict with its comparisons

- Category: Presentation inconsistency
- Location: DOC-005-RESULTS, PDF pp. 15 and 17, eTable 11.
- Evidence to verify: Printed raw-score header order is painTRAINER, health coach, usual care plus, but pairwise comparison directions/magnitudes across outcome blocks align with raw-score columns ordered usual care plus, painTRAINER, health coach. Page 15 calls them unadjusted means while eTable 11 labels them medians (IQRs). Verify column assignment and summary-statistic label.

## Not selected because of the 10-candidate cap

- Supplement p. 6 cross-reference says eFigure 1 rather than eFigure 2.
- eTable 8 RR header carries the omnibus-P footnote marker.
- Supplement p. 5 lists intervention levels as UC, PT, UC.

