# Deduplicated Candidate Shortlist

Coordinator selection for one evidence-verification stage. Candidate count: 10. All locations use PDF page numbers unless a printed page is also stated. No protocol/SAP evidence is used.

## C1 — Statistical reporting inconsistency: incidence-difference estimate outside its CI

- Source: `jama_sun_2024_oi_240088_1746815064.14747.pdf`, p. 8 (printed p. 1066), Table 2, “Any stroke outside the territory of the qualifying artery within 1 y after enrollment.”
- Displayed evidence: 3/249 (1.2%) vs 4/252 (1.6%); incidence difference −0.4 percentage points; 95% CI −2.4 to −1.7.
- Basis: −0.4 is not contained in [−2.4, −1.7]. The displayed counts yield approximately −0.38 percentage points.
- Verify: inspect the original table and determine whether the upper CI endpoint/sign is incorrect.

## C2 — Presentation and cross-document inconsistency: Figure S5 AMM denominator and disabling-stroke counts

- Sources: `joi240088supp1_prod_1746815064.21247.pdf`, p. 13, Figure S5; p. 24, Table S11 and footnote b.
- Displayed evidence: Figure S5 labels AMM N=252 but its mRS 0–6 counts sum to 249 and its percentages use 249. Figure S5 mRS scores >2 sum to 4 BA and 9 AMM, whereas Table S11 defines disabling stroke as mRS >2 at 1 year and reports 6 BA and 18 AMM.
- Basis: the figure denominator is internally inconsistent, and the plotted category totals do not reconcile with the table’s identically defined outcome.
- Verify: read and sum every Figure S5 category in both arms, verify displayed percentages, and compare mRS >2 totals with Table S11’s definition and counts.

## C3 — Cross-document inconsistency: Table S6 mixes ITT labels with a PPS-like balloon result

- Sources: supplement p. 19, Table S6; main article p. 8, Table 2; supplement p. 21, Table S8.
- Displayed evidence: Table S6 headers are 249/252 but the primary outcome is 9 (3.9%) vs 34 (13.5%). Main ITT Table 2 gives 11/249 (4.4%) vs 34/252 (13.5%); PPS Table S8 gives 9/233 (3.9%).
- Basis: 9/249=3.6%, while 9/233=3.9%; the balloon count/rate appears PPS-like despite an ITT-sized header and an ITT medical arm.
- Verify: determine the intended Table S6 analysis population and raw outcome values; distinguish the displayed raw count/rate from the center-adjusted HR.

## C4 — Presentation inconsistency: Table S7 PPS headers on ITT site data

- Sources: supplement p. 20, Table S7; p. 23, Table S10.
- Displayed evidence: headers state BA N=233 and AMM N=238, but site totals are 256+245=501 and events sum to 11 vs 34. The four site-by-arm percentages imply arm totals of 249 and 252. Table S10 labels 249/252 as ITT and 233/238 as PPS.
- Basis: the table body represents the 501-person ITT analysis while its arm headers display PPS denominators.
- Verify: reconstruct site-by-arm denominators from the counts/percentages and determine the correct headers.

## C5 — Presentation inconsistency: Table S8 PPS body with ITT headers

- Sources: supplement p. 21, Table S8; p. 23, Table S10; main article p. 5, Figure 1.
- Displayed evidence: the title says PPS, headers say 249/252, but rates such as 9 (3.9%), 33 (13.9%), 6 (2.6%), and 20 (8.4%) use 233/238. Table S10 and Figure 1 give PPS denominators 233/238.
- Basis: the title and body are PPS while the headers are ITT.
- Verify: recalculate representative rates under both denominator pairs and confirm the intended headers.

## C6 — Presentation/arithmetic inconsistency: Table S9 ATS body with ITT headers

- Sources: supplement p. 22, Table S9; p. 23, Table S10.
- Displayed evidence: the title says ATS, headers say 249/252, but 11 (4.5%) and 34 (13.4%) use 247/254, which Table S10 labels ATS. The BA 30-day cell is 8 (3.3%), although 8/247 and 8/249 both round to 3.2%.
- Basis: the body is ATS while the headers are ITT; one percentage remains unreconciled even under the apparent ATS denominator.
- Verify: confirm ATS denominators, recalculate all rates, and separately check the 8 (3.3%) cell.

## C7 — Cross-document inconsistency: lead-center count in the 501-patient analysis

- Sources: main article p. 4 (printed p. 1062), Results—Patient Population; supplement p. 20, Table S7; supplement p. 12, Figure S3.
- Displayed evidence: the main Results state 258/501 primary-analysis patients came from the lead center. Table S7 partitions the same 501 as 256 at Beijing Tiantan and 245 elsewhere. Figure S3 shows 258 enrolled at Beijing Tiantan among the pre-exclusion total of 512.
- Basis: the narrative appears to pair the 512-person recruitment-site count with the 501-person analysis denominator, whereas Table S7 reports 256/501.
- Verify: trace the displayed analysis populations and determine whether the 501-person lead-center numerator is 256 or 258.

## C8 — Cross-document inconsistency: arterial perforation frequency

- Sources: main article p. 7 (printed p. 1065), procedural-complications paragraph; supplement p. 17, Table S4.
- Displayed evidence: the narrative reports arterial perforation 0.4% in the balloon group and cites Table S4; Table S4 reports 0 (0.0%).
- Basis: the same named procedural complication is reported as one-event-equivalent vs zero.
- Verify: compare the original locations and determine the intended count/percentage.

## C9 — Arithmetic inconsistency: multiple displayed count/percentage pairs

- Sources and displayed evidence:
  - Main p. 4, Patient Population: 343 (69.1%) male among 501; 343/501=68.5%.
  - Main p. 6, Table 1: BA female 77 (30.1%) with n=249; 77/249=30.9%.
  - Main p. 6, Table 1: AMM NIHSS 2–4, 51 (20.5%) with n=252; 51/252=20.2%.
  - Main p. 6, Table 1: BA stenosis 90%–99%, 25 (10.4%) with n=249; 25/249=10.0%.
  - Supplement p. 14, Table S1: BA non-zone infarct 131 (61.9%) among 215; 131/215=60.9%, and 84+131=215.
- Basis: direct integer arithmetic does not reproduce the displayed percentages at one-decimal precision.
- Verify: confirm each original cell/statement and applicable denominator, then recalculate with ordinary one-decimal rounding.

## C10 — Statistical reporting inconsistency: Table S11 P values and stated test markers

- Source: supplement p. 24, Table S11, rows marked footnote c and footnotes c/d.
- Displayed evidence: footnote c states chi-square testing. Overall serious adverse events 12/249 vs 14/252 gives P=.84; nervous-system disorders 7/249 vs 12/252 gives P=.35; disabling stroke 6/249 vs 18/252 gives P=.02. Footnote d separately identifies Fisher exact testing.
- Basis: ordinary Pearson chi-square gives approximately .710, .253, and .013; two-sided Fisher exact gives approximately .841, .350, and .020, matching the displayed values.
- Verify: recompute the three 2×2 tests using standard Pearson chi-square and two-sided Fisher exact methods, inspect the original c/d markers, and determine whether the P values or method labels are inconsistent.

## Retained but not selected for verification

- Figure S1 repeats the ordinal label “2nd meeting” on three later meeting boxes; lower priority presentation issue.
- Table S2 contains an orphan “No. Patients evaluated” row; lower priority and the missing association cannot be resolved locally.
- Separate arithmetic checker formulations that duplicate C3–C6 or C9.
