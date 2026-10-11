# Cross-source consistency review — consolidated checker

## Scope, method, and durable coverage

This canonical checker consolidates the four disjoint completed cross-source shards without changing their source-linked relationship records.  It covers all **383/383** assigned cross-lane relationships: numeric/reporting `N001`–`N282` (282) and inferential-statistical `S001`–`S101` (101).  Comparisons matched population, phase/time point, contrast, analysis set, outcome/measure, scale/unit, reference group, model where applicable, and displayed precision before a difference was retained.  Direct PDFs were the authority; mapped extracts were locators.  No web source or legacy candidate conclusion was used.

| Shard | Complete assigned coverage | Durable relationship record | Result |
|---|---|---|---|
| cross-001 | `N001`–`N094`; `S001`–`S025` (119) | `parts/cross_source_N001_N094_S001_S025.md` | 2 drafts retained |
| cross-002 | `N095`–`N188`; `S026`–`S051` (120) | `parts/cross_source_N095_N188_S026_S051.md` | no draft |
| cross-003 | `N189`–`N248`; `S052`–`S080` (89) | `parts/cross_source_N189_N248_S052_S080.md` | no draft |
| cross-004 | `N249`–`N282`; `S081`–`S101` (55) | `parts/cross_source_N249_N282_S081_S101.md` | 3 drafts retained |

The four listed artifacts retain every individual relationship record, exact source location, matching logic, no-candidate determination, and shard limitation.  Their scopes are mutually disjoint and total 383.  The candidate registrations below merge only exact duplicates: C007 and C008 each combine the matching numeric-check and cross-source records; no other candidate is merged.

## Registered cross-lane candidate provenance

### C001 — protocol timeline end date

- **Status:** Pending Human Adjudication.
- **Primary checker provenance:** numeric consistency `N044`, `parts/numeric_checks_N001_N094.md`.
- **Exact source location and printed values:** [Protocol PDF p. 11](../../../joi190092supp2_prod.pdf#page=11), Table 1: enrollment “November 2012 through May 2015”; six-month follow-up completion “Through December 2015”; maximum 12-month follow-up plus one-month window “Through July 2015.”
- **Comparison logic:** May 2015 plus 13 months ends no earlier than June 2016; July 2015 also precedes the printed December 2015 six-month completion. Calendar dates have no rounding tolerance.
- **Supported alternative and human verification:** A year may be typographical or the maximum schedule may apply to an earlier cohort. Verify the final amendment and the intended year/cohort for the July entry.

### C002 — eligible failure total vs switching denominators

- **Status:** Pending Human Adjudication.
- **Primary checker provenance:** numeric consistency `N010`, with supporting source relationship `N009` and Table 2/Figure 1, `parts/numeric_checks_N001_N094.md`.
- **Exact source locations and printed values:** [Main PDF p. 7](../../../jama_rathinam_2019_oi_190092.pdf#page=7) states 49 of 68 eligible failures switched, then gives 20/32 and 29/42; [main PDF p. 6, Table 2](../../../jama_rathinam_2019_oi_190092.pdf#page=6) reports 32 and 42 failures; [main PDF p. 3, Figure 1](../../../jama_rathinam_2019_oi_190092.pdf#page=3) reports 20 and 29 switches.
- **Comparison logic:** 20+29=49, and 32+42=74; 74 exceeds the stated eligible total 68 by 6, although both printed percentages are arithmetically correct.
- **Supported alternative and human verification:** 32 and 42 may intentionally mean all failures rather than eligible failures. Verify the denominator definitions and original-arm allocation of the six ineligible failures.

### C003 — allocation block sizes

- **Status:** Pending Human Adjudication.
- **Checker provenance:** cross-source `N002` and `S014`, `parts/cross_source_N001_N094_S001_S025.md`; SAP allocation records `N196` and `N237` supply version-specific alternative evidence. `S001` is unrelated and excluded.
- **Exact source locations and printed values:** [Main PDF p. 2](../../../jama_rathinam_2019_oi_190092.pdf#page=2) says “permutated blocks of size 4 and 6”; [Protocol PDF p. 13](../../../joi190092supp2_prod.pdf#page=13) §2.4 says blocks “4, 6, or 8 with equal probability.”
- **Comparison logic:** For the matched trial/site-block allocation description, the stated sets differ: `{4,6}` versus `{4,6,8}`.
- **Supported alternative and human verification:** The protocol is planned and the article may state blocks actually used after an amendment. The supplied SAP on physical pp. 9 and 49–50 specifies only 4 and 6 with probabilities 2/3 and 1/3, matching the article. Verify the final protocol, amendment history, and randomization list.

### C004 — six-month success injection-after-90-days criterion

- **Status:** Pending Human Adjudication.
- **Checker provenance:** cross-source `N004`, `N026`, `N112`, `N263`, and `S024`, `parts/cross_source_N001_N094_S001_S025.md`; `S001` is unrelated and excluded.
- **Exact source locations and printed values:** [Main PDF p. 3](../../../jama_rathinam_2019_oi_190092.pdf#page=3) lists success components and calls other injections protocol deviations; [Protocol manual PDF p. 80](../../../joi190092supp2_prod.pdf#page=80) §2.5.1 requires no periocular/intravitreal corticosteroid injection after the first 90 days.
- **Comparison logic:** The otherwise matched patient-level six-month definitions differ because the manual has an explicit post-day-90 injection exclusion and the article’s enumerated success definition does not.
- **Supported alternative and human verification:** The article may have abbreviated an operational failure rule or the endpoint changed by version. The SAP sensitivity section on physical p. 70 uses inflammation status at an injection 90 days after enrollment but does not establish the primary rule. Verify version-in-force, assessment forms, and classifications for the eight reported cases.

### C005 — missed-dose Welch P=.87 compatibility

- **Status:** Pending Human Adjudication.
- **Checker provenance:** statistical pass 1 `S006`, `checkers/statistical_pass_1.md`.
- **Exact source locations and printed values:** [Main PDF p. 6, Table 2](../../../jama_rathinam_2019_oi_190092.pdf#page=6) prints MTX 4.6 (SD 1.0)% (`n=96`) and MMF 4.3 (SD 0.5)% (`n=98`), `P=.87`; [main PDF p. 4](../../../jama_rathinam_2019_oi_190092.pdf#page=4) specifies a Welch t test.
- **Comparison logic:** Diagnostic SE `sqrt(1.0²/96 + 0.5²/98) ≈ 0.114`; diagnostic t `0.3/0.114 ≈ 2.63`, giving two-sided P about `.01`, not `.87`, beyond display rounding. This is a diagnostic, not a replacement analysis.
- **Supported alternative and human verification:** An unprinted analytic N, unrounded scale, distinct summary, or another comparison’s P value could explain it. Verify row-level analysis data and the exact Welch-test output.

### C006 — main Table 3 MMF n=109 header vs supplement N=108/percentages

- **Status:** Pending Human Adjudication.
- **Checker provenance:** main-table records `N029`, `N030`, and `N034`; supplement records `N276`–`N278`, `parts/cross_source_N249_N282_S081_S101.md`.
- **Exact source locations and printed values:** [Main PDF p. 8, Table 3](../../../jama_rathinam_2019_oi_190092.pdf#page=8) labels MMF `n=109`, including decreased/defective vision `19 (17.6)` and fatigue `59 (54.6)`; [Supplement PDF pp. 10–12, eTables 4–6](../../../joi190092supp1_prod.pdf#page=10) label treated MMF `N=108`. Only eTable 4 repeats the matched vision cell `19 (17.6)`; fatigue is an internal main-table denominator check. The main footnote says one MMF-assigned patient never received study drug.
- **Comparison logic:** 19/108=17.592…% →17.6 and 59/108=54.630…% →54.6; under 109 these are 17.4% and 54.1%. The printed percentages thus use 108 although the main header says 109.
- **Supported alternative and human verification:** The header may intentionally give randomized assignment while percentages use recipients, with the footnote intended to signal this. Verify the table shell/output and apply the approved convention to every MMF percentage.

### C007 — eTable 9 MMF serious diarrhea 1 (3.4) vs N=20

- **Status:** Pending Human Adjudication.
- **Checker provenance:** numeric consistency `N281`, `parts/numeric_checks_N189_N282.md`; cross-source `N280`/`N281`, `parts/cross_source_N249_N282_S081_S101.md`. These are merged because they compare the same cell, denominator, and calculation.
- **Exact source location and printed values:** [Supplement PDF p. 15, eTable 9](../../../joi190092supp1_prod.pdf#page=15) labels MMF `N=20`; its Serious Systemic diarrhea cell is `1 (3.4)` and the table defines entries as patients with at least one event (%).
- **Comparison logic:** 1/20×100=5.0% to one decimal, not 3.4%. The N=20 column elsewhere shows `1 (5.0)` and the N=29 MTX column shows `1 (3.4)`.
- **Supported alternative and human verification:** An unprinted event-specific denominator near 29, header error, copied percentage, or typesetting error could explain it. Verify the AE tabulation, numerator, percentage, and any omitted subset.

### C008 — eTable 8 serious-ocular hypertension label vs eTable 1 surgery-required definition

- **Status:** Pending Human Adjudication.
- **Checker provenance:** numeric consistency `N282`, `parts/numeric_checks_N189_N282.md`; cross-source `N279`/`N282`, `parts/cross_source_N249_N282_S081_S101.md`. These are merged because both compare the same seriousness label and eTable 1 criterion.
- **Exact source locations and printed values:** [Supplement PDF p. 5, eTable 1](../../../joi190092supp1_prod.pdf#page=5) defines non-serious ocular hypertension `≥24 mm Hg` and serious ocular hypertension as `Surgery required (laser or incisional)`; [Supplement PDF p. 14, eTable 8](../../../joi190092supp1_prod.pdf#page=14) places `Ocular hypertension >24mm Hg` under Serious Ocular and reports MTX `1 (1.6)`, MMF `0 (0.0)`. Its footnote points to “eFigure 2,” not eTable 1; eTable 1 is a separate comparator and eTable 9 labels the serious row as surgery required.
- **Comparison logic:** The serious-row label repeats the non-serious pressure criterion rather than the referenced surgery-required seriousness criterion; displayed percentages are not the conflict.
- **Supported alternative and human verification:** The row may abbreviate a surgery-required event, carry a copied non-serious label, or use an unprinted cohort rule. Verify the event-level case, intended seriousness criterion, and matching eTable 9 serious row.

## Limitations

Most protocol/SAP material is prospective planning or version history rather than a matched observed result, so a plan-versus-result difference alone was not called a candidate.  The supplied package lacks amendment history, randomization lists, participant-level classifications, row-level analysis data, and model output needed to distinguish a reporting inconsistency from an undocumented implementation detail.  No workbook, CSV, web material, external literature, or legacy candidate conclusion was used.
