# Cross-Source Consistency Review

## Scope and method

- **Scope reviewed:** DOC-001 main article (abstract, narrative, Figure 1, Tables 1-2, Figure 3, captions, and footnotes), DOC-002 results supplement (Figures S1-S5 and Tables S1-S12), and DOC-003 protocol/SAP compilation (protocol versions, amendment history, and SAP versions).
- **Evidence rule:** Values were compared only after matching the trial population or analysis set, outcome definition, time origin/window, treatment contrast and reference group, model/adjustment, measure and scale, unit, and displayed precision. Direct PDFs were the authority; the current quantitative maps were used as relationship locators.
- **Relationship coverage:** 68 matched relationship clusters: 45 main-to-results-supplement clusters (population/flow, baseline quantities, efficacy, safety, sensitivity, subgroup, and follow-up results) and 23 main-to-protocol/SAP definition or planning clusters (eligibility, endpoint, time window, analysis set, model, scale, sample-size revision, and follow-up definitions).
- **Protocol/SAP handling:** The 802-to-512 sample-size change, interim-analysis removal, and eligibility-window changes are recorded as dated amendments in DOC-003 and were not treated as conflicts with the final reported trial. Likewise, the final-SAP one-sided alpha of 2.5% is the same nominal threshold as the main article's two-sided type-I error of .05 for sample-size planning.
- **Excluded display convention:** Coherent `P < .001` or similar finite-precision displays were checked but are not proposals merely because an exact tail probability is not printed.

## Matched relationships with no cross-source discrepancy identified

- The primary endpoint, primary-analysis arm counts (249 and 252), main HR 0.32 (95% CI, 0.16 to 0.63), and log-rank P < .001 align among the DOC-001 abstract/narrative/Table 2/Figure 3 after distinguishing the centre-adjusted, per-protocol, and as-treated supplement analyses.
- Secondary endpoint labels, 90-day and 1-year mRS scale/direction, EQ-5D 0-100 scale, revascularization definition, restenosis threshold, and time windows align with the final protocol/SAP where the version and endpoint are matched.
- The later-protocol and final-SAP sample-size assumptions (15% versus 7%; 512 total; no interim efficacy analysis) explain their difference from the superseded original protocol/SAP design assumptions (12.2% versus 6.1%; 802 total; interim analysis).
- Rates in DOC-002 Tables S2-S5 and S11-S12 were not compared to the primary outcome without their displayed evaluated denominators or measure definitions. No rate was treated as a count, and no count was treated as a person-time rate.

## Qualifying proposals for human verification

### Proposal 1 — Female percentage in Table 1 does not reconcile with its displayed count and denominator

- **Locations:** DOC-001 [PDF p. 6](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=6>), Table 1, `Sex, No. (%)`, balloon angioplasty group (`n = 249`).
- **Printed values:** Male is `172 (69.1)` and female is `77 (30.1)`.
- **Comparison logic:** The same mutually exclusive two-category sex row identifies a balloon-angioplasty denominator of 249. `77 / 249 × 100 = 30.92%`, which rounds to 30.9% at one decimal place; `172 + 77 = 249`, and 69.1% plus a correctly rounded female complement would be 100.0%.
- **Supported alternatives:** The female count may be correct and the percentage may have been transcribed or rounded incorrectly. Alternatively, an undisclosed denominator or category convention may have been used, although the adjacent male entry and printed group denominator do not show one.
- **Human verification steps:** Inspect the Table 1 production data or author table source; confirm the intended denominator for the female row; recompute the printed one-decimal percentage; then check whether any downstream table or abstract uses the intended percentage.

### Proposal 2 — Narrative attribution of all 11 pre-analysis exclusions to consent withdrawal conflicts with Figure 1

- **Locations:** DOC-001 [PDF p. 4](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=4>), `Patient Population`; DOC-001 [PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), Figure 1.
- **Printed values:** The narrative says, `Eleven patients were excluded due to consent withdrawal`, leading to 501 primary-analysis participants (252 AMM; 249 BA). Figure 1 shows BA: `7 Withdrew consent`; AMM: `3 Withdrew consent` and `1 Not successfully recruited but assigned a randomization number in error`, then the same 249 and 252 primary-analysis counts.
- **Comparison logic:** Both locations describe the 11 removals from 512 randomized participants before the same 501-person primary analysis. Figure 1 attributes 10 removals to consent withdrawal and 1 to erroneous assignment of a randomization number, rather than 11 consent withdrawals.
- **Supported alternatives:** The narrative may use an umbrella shorthand for the 11 pre-analysis removals; or the Figure 1 administrative classification may require correction. The supplied documents do not state that the erroneous-randomization case also withdrew consent.
- **Human verification steps:** Reconcile the participant disposition dataset and case-report documentation for the one AMM participant; verify the intended exclusion reason; revise the narrative or Figure 1 only if the source disposition record supports it.

### Proposal 3 — Centre-adjusted supplement primary-outcome row conflicts with the matched main primary result and its own displayed denominator

- **Locations:** DOC-001 [PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), primary-outcome narrative; DOC-001 [PDF p. 8](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>), Table 2 primary outcome; DOC-002 [PDF p. 19](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=19>), Table S6.
- **Printed values:** DOC-001 reports the primary composite as BA `11 (4.4%)` of 249 versus AMM `34 (13.5%)` of 252. DOC-002 Table S6, labelled `Post hoc analysis of center-effect adjustment`, prints the same primary endpoint and headers `n=249` and `n=252`, but reports BA `9 (3.9)` and AMM `34 (13.5)`, with adjusted HR `0.32 (0.16 to 0.62), P=.001`.
- **Comparison logic:** Centre adjustment can change the HR, CI, and P value, but it does not by itself change the observed event count for an otherwise identical endpoint and displayed analysis-set denominators. In addition, `9 / 249 = 3.6%` to one decimal place, not 3.9%; 3.9% corresponds to 9/233 at displayed precision.
- **Supported alternatives:** Table S6 may have used a different unlabelled eligible or per-protocol set; its BA count/percentage may be wrong; or its group header may be wrong. The supplied table does not identify an alternative population for this row.
- **Human verification steps:** Obtain the centre-adjusted analysis dataset and model output; confirm the analysis-set membership and event flags; establish whether the BA numerator is 9 or 11; and make the numerator, percentage, denominators, and analysis-population label consistent with the verified output.

### Proposal 4 — Table S7 headers state per-protocol-sized group totals while displayed site results use the primary-analysis population

- **Locations:** DOC-001 [PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), Figure 1; DOC-002 [PDF p. 20](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=20>), Table S7.
- **Printed values:** Figure 1 gives primary-analysis BA/AMM counts `249/252` and per-protocol counts `233/238`. Table S7 headers print BA `N=233` and AMM `N=238`, but its site rows give total patients `256` and `245` (501 total) and event percentages: Beijing Tiantan BA `4 (2.9)` and AMM `19 (16.1)`; other centers BA `7 (6.3)` and AMM `15 (11.2)`.
- **Comparison logic:** The Table S7 site event counts sum to BA 11 and AMM 34, the DOC-001 primary-analysis primary-outcome counts. At printed precision, the four percentages correspond to denominators 138 and 111 for BA (249 total) and 118 and 134 for AMM (252 total), not to the stated 233 and 238. The Table S7 `No. of patients` column also sums to 501, not 471.
- **Supported alternatives:** The Table S7 group-header denominators may be copied from the per-protocol analysis; the site rows may intentionally use another analysis set but lack correct labels; or one of the site-total or percentage displays may be erroneous.
- **Human verification steps:** Reproduce the site-by-treatment table from the analysis dataset; verify each site denominator and analysis set; confirm the interaction-model population; and correct either the headers or the displayed counts/percentages so all use the same specified set.

### Proposal 5 — Table S8 per-protocol header conflicts with its own percentages and Figure 1 per-protocol denominators

- **Locations:** DOC-001 [PDF p. 5](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=5>), Figure 1; DOC-002 [PDF p. 21](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=21>), Table S8; DOC-002 [PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>), Table S10 per-protocol header.
- **Printed values:** Figure 1 identifies per-protocol BA/AMM counts `233/238`. Table S8 is titled `Study outcomes in the per-protocol population (PPS)` but its column headers print BA `n=249` and AMM `n=252`; its primary-outcome row is BA `9 (3.9)` and AMM `33 (13.9)`. Table S10 independently labels its per-protocol stratum `N=233` and `N=238`.
- **Comparison logic:** `9 / 233 = 3.9%` and `33 / 238 = 13.9%` at the displayed precision. Those values do not round to 3.9% and 13.9% with the Table S8 header denominators (9/249 = 3.6%; 33/252 = 13.1%). Thus the Table S8 values and the independently displayed per-protocol population agree on 233/238 while its headers state the primary-analysis counts.
- **Supported alternatives:** The headers may be a copy-forward error; the percentages may have been calculated on 233/238 while counts were presented under an intended different population; or Figure 1/Table S10 may not represent the exact PPS used by Table S8. No distinction is printed in Table S8.
- **Human verification steps:** Confirm the formal PPS definition and membership list; rerun the Table S8 tabulation; and align its title, headers, counts, percentages, and HR analysis population with the verified PPS.

### Proposal 6 — Table S9 as-treated header conflicts with its own percentages and the as-treated denominators displayed in Table S10

- **Locations:** DOC-002 [PDF p. 22](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=22>), Table S9; DOC-002 [PDF p. 23](<../../../joi240088supp1_prod_1746815064.21247.pdf#page=23>), Table S10 as-treated header.
- **Printed values:** Table S9 is titled `Study outcomes in the as-treated population (ATS)` and prints column headers BA `n=249` and AMM `n=252`, with primary-outcome values BA `11 (4.5)` and AMM `34 (13.4)`. Table S10 prints its as-treated stratum as BA `N=247` and AMM `N=254`.
- **Comparison logic:** `11 / 247 = 4.5%` and `34 / 254 = 13.4%` at one decimal place, whereas 11/249 rounds to 4.4% and 34/252 rounds to 13.5%. The Table S9 percentages therefore match the as-treated denominators printed in Table S10, not Table S9's headers.
- **Supported alternatives:** The Table S9 headers may be copied from the primary-analysis table; the Table S10 as-treated membership may differ by outcome but not be explained; or the Table S9 percentages may be based on a different unlabelled denominator.
- **Human verification steps:** Verify as-treated assignment rules, participant crossovers, and endpoint-specific eligibility; inspect the ATS analysis output; and state the correct denominators consistently in Tables S9 and S10 or document any intentional outcome-specific difference.

### Proposal 7 — One-year non-qualifying-territory stroke incidence difference lies outside its printed confidence interval

- **Locations:** DOC-001 [PDF p. 8](<../../../jama_sun_2024_oi_240088_1746815064.14747.pdf#page=8>), Table 2, `Any stroke outside the territory of the qualifying artery within 1 y after enrollment`.
- **Printed values:** BA `3 (1.2%)`; AMM `4 (1.6%)`; incidence difference `−0.4% (95% CI, −2.4 to −1.7)`; HR `0.76 (0.17 to 3.40)`; `P=.72`.
- **Comparison logic:** A point estimate must lie within its own displayed confidence interval under the label `incidence difference (95% CI)`. Here `−0.4` is greater than the stated upper endpoint `−1.7`, so it does not lie in `[-2.4, −1.7]`. The count-derived crude difference, 3/249 minus 4/252, is approximately −0.38 percentage points and rounds to −0.4%, consistent with the point estimate but not with the printed interval.
- **Supported alternatives:** One or both confidence-interval endpoints may be a transcription error; the point estimate could refer to a differently adjusted quantity not identified in the table; or the interval may have been copied from another comparison. The table gives no alternative calculation convention for this row.
- **Human verification steps:** Recreate the incidence-difference calculation using the stated analysis population and missing-case convention in Table 2; verify the source CI method and unrounded endpoints; and correct the point estimate, interval, or label to identify the same estimand.

## Limitations

- DOC-003 contains multiple protocol and SAP versions. Comparisons were limited to the final version or were explicitly version-matched; superseded planning values were not treated as observed-result conflicts.
- The PDFs provide displayed tabulations but not analytic datasets or code. Where a table has internally incompatible analysis-set labels, the exact intended population cannot be resolved from supplied evidence alone.
- This artifact records proposals for later registration and recheck only. It assigns no candidate IDs and makes no adjudication, severity, validity, or correction decision.

## Compact completion record

- **Matched relationship clusters:** 68.
- **Qualifying proposals:** 7.
- **Display-zero-only proposals:** 0.
- **Artifact:** `.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md`.
