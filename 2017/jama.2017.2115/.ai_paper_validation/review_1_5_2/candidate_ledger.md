# Candidate ledger

## Ledger status and merge method

This ledger contains every distinct proposal from the completed numeric-consistency,
statistical pass 1, and cross-source consistency lanes. It assigns stable IDs exactly
once. Every record is **Pending Human Adjudication**. No record is a severity
assignment, validity judgment, adjudication, or prescribed correction.

Only one merge was made before assigning stable IDs: `NCAND-001` and `SCAND-003`
are one candidate because they cite the same printed Table 2 placebo-calcium `N=1994`
cell, compare it to the same randomized placebo total, and apply the same
participant-count rule. Both lane provenances are retained in `C001`.

No other proposals were merged: the protocol inequality direction (`NCAND-002`),
protocol calcium unit (`NCAND-003`), death-CI diagnostic (`SCAND-001`),
outside-vitamin-D CI/P conflict (`SCAND-002`), and discontinuation-count mismatch
(`XCAND-001`) concern different printed values, comparators, or consistency rules.
No other checker proposals exist. The stable ID set is therefore `C001`–`C006`.

| Stable ID | Workflow category | Merged lane proposal(s) | Canonical relationship ID(s) | Status |
|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | NCAND-001; SCAND-003 | N028; S012 | Pending Human Adjudication |
| C002 | Measure, label, or scale inconsistency | NCAND-002 | N057 | Pending Human Adjudication |
| C003 | Measure, label, or scale inconsistency | NCAND-003 | N057 | Pending Human Adjudication |
| C004 | Statistical reporting inconsistency | SCAND-001 | S007 | Pending Human Adjudication |
| C005 | Statistical reporting inconsistency | SCAND-002 | N028; S012 | Pending Human Adjudication |
| C006 | Cross-document numeric inconsistency | XCAND-001 | N019; N039; S020 | Pending Human Adjudication |

## C001 — Table 2 placebo calcium `N=1994` exceeds the randomized placebo cohort

- **Workflow category:** Denominator, proportion, or total inconsistency.
- **Status:** Pending Human Adjudication.
- **Canonical relationships:** `N028`; `S012`.
- **Lane provenance:** Numeric consistency `NCAND-001`; statistical pass 1 `SCAND-003` (merged as the same printed cell and rule). Cross-source lane did not propose a distinct candidate for this cell.
- **Exact direct-PDF locations and printed evidence:** DOC-001, [p.5](../../jama_lappe_2017_oi_170019.pdf#page=5), Table 2, “Outside of Study Supplement Intake (Visit 2 to Visit 9),” calcium row, prints treatment `N=1099`, mean 500 (95% CI 475 to 525), and placebo `N=1994`, mean 512 (489 to 536), with difference −12.0 (−46.0 to 22.0). DOC-001 [p.1](../../jama_lappe_2017_oi_170019.pdf#page=1) and Figure 1 [p.4](../../jama_lappe_2017_oi_170019.pdf#page=4) each print placebo randomization `N=1147`. The adjacent placebo outside-study vitamin-D row on p.5 prints `N=1094`.
- **Comparator and reproducible rule:** A cell headed “No. of Participants” for a placebo-group participant-level mean cannot exceed the total 1147 people randomized to placebo, absent a supplied statement that it counts a different unit. `1994 > 1147` by 847; it also differs from the adjacent placebo vitamin-D `N=1094` by 900. The displayed means independently reconcile: `500 − 512 = −12.0` mg/d.
- **Direct observation:** The table prints `N=1994`, while the paper prints 1147 randomized placebo participants.
- **Diagnostic inference:** Under the table’s participant-count label, the two values cannot refer to the same unique placebo-participant population. This is exact integer logic, not a rounding issue.
- **Source-grounded alternatives:** The cell may be a transposition/typographical error, plausibly `1094` because that is the adjacent placebo outside-supplement N; alternatively, the cell could intentionally count another unit despite the printed participant header. The supplied PDFs do not establish either alternative.
- **Missing definition:** Whether the calcium-row cell is intended to count unique participants or a different unit, and the production/source-data value.
- **Human verification question:** What is the correct placebo participant count for the Table 2 outside-study calcium-intake row, and was the cell intended to be participant-level rather than observation-level?

## C002 — Protocol’s ≥70-year vitamin-D “limit” has the opposite inequality direction

- **Workflow category:** Measure, label, or scale inconsistency.
- **Status:** Pending Human Adjudication.
- **Canonical relationships:** `N057`.
- **Lane provenance:** Numeric consistency `NCAND-002`. Statistical and cross-source lanes made no distinct proposal.
- **Exact direct-PDF location and printed evidence:** DOC-002, [p.7](../../joi170019supp1_prod.pdf#page=7), section “5. Intervention,” states that participants will be asked “to limit that to no more than 400 IU/day if they are < 70 years of age and to more than 600 IU/day if they are ≥ 70.”
- **Comparator and reproducible rule:** The same instruction calls both conditions a “limit.” “No more than 400 IU/day” is an upper bound, whereas “more than 600 IU/day” is a lower-bound inequality. A limiting instruction cannot have that opposite direction without an explicit different purpose.
- **Direct observation:** The <70 clause contains `≤400 IU/day` wording; the ≥70 clause contains `>600 IU/day` wording.
- **Diagnostic inference:** The ≥70 wording is directionally incompatible with the sentence’s limiting instruction. This is a categorical inequality/label check, not a numerical recalculation.
- **Source-grounded alternatives:** “No more than 600 IU/day” may have been intended, or the ≥70 clause may have another explicitly intended maximum not represented by the printed wording. The supplied PDFs do not resolve it.
- **Missing definition:** The intended upper allowable vitamin-D quantity for participants aged ≥70 years.
- **Human verification question:** Was the ≥70-year instruction intended to say “no more than 600 IU/day,” or another explicit maximum?

## C003 — Protocol changes the calcium target unit from 1200 mg/day to 1200 g/day

- **Workflow category:** Measure, label, or scale inconsistency.
- **Status:** Pending Human Adjudication.
- **Canonical relationships:** `N057`.
- **Lane provenance:** Numeric consistency `NCAND-003`. Statistical and cross-source lanes made no distinct proposal.
- **Exact direct-PDF location and printed evidence:** DOC-002, [p.7](../../joi170019supp1_prod.pdf#page=7), section “5. Intervention,” specifies calcium `(1200 mg/d)` and calcium-carbonate `600 mg` caplets twice daily, then states that recommended intake was set as “1,200 g/day ... the level of supplementation that we are including.”
- **Comparator and reproducible rule:** `600 mg × 2/day = 1200 mg/day = 1.2 g/day`. Printed `1200 g/day` is 1000-fold larger than 1.2 g/day and conflicts with the statement that it is the same included supplementation level. The conversion is exact (`1000 mg = 1 g`).
- **Direct observation:** The same paragraph prints 1200 mg/day regimen wording and 1200 g/day as its purported matching level.
- **Diagnostic inference:** The unit labels conflict; no rounding tolerance bridges a factor of 1000.
- **Source-grounded alternatives:** The latter phrase may have intended `1,200 mg/day` or `1.2 g/day`; the supplied PDFs provide no explicit correction.
- **Missing definition:** The intended unit in the recommended-intake sentence and the protocol production source.
- **Human verification question:** Should the protocol sentence say 1,200 mg/day (1.2 g/day) rather than 1,200 g/day?

## C004 — Death-difference confidence interval is discordant with the printed flow counts under a labelled diagnostic calculation

- **Workflow category:** Statistical reporting inconsistency.
- **Status:** Pending Human Adjudication.
- **Canonical relationships:** `S007`.
- **Lane provenance:** Statistical pass 1 `SCAND-001`. Numeric lane checked the same flow counts without a separate proposal; cross-source lane made no distinct proposal.
- **Exact direct-PDF locations and printed evidence:** DOC-001 Figure 1/narrative, [p.4](../../jama_lappe_2017_oi_170019.pdf#page=4), prints 7 treatment and 9 placebo deaths among 1156 and 1147 randomized participants, and a death difference `.002` (95% CI `−.006 to .037`).
- **Comparator and reproducible rule:** The printed counts give placebo minus treatment `9/1147 − 7/1156 = .001791`, compatible with `.002`. As a diagnostic only—not a reported analysis—the ordinary unpooled-binomial Wald SE is `sqrt[(7/1156)(1−7/1156)/1156 + (9/1147)(1−9/1147)/1147] = .003463`; its nominal 95% interval is about `−.0050 to .0086`. The printed `.037` upper endpoint is far beyond this count-scale diagnostic while the lower endpoint is close to it.
- **Direct observation:** The PDF prints the counts, point difference, and CI above.
- **Diagnostic inference:** The upper CI endpoint appears quantitatively discordant with the displayed death-count contrast under the labelled standard diagnostic. The article does not identify the CI construction for this flow result, so the calculation does not establish a correction.
- **Source-grounded alternatives:** `.037` may be a transcription/typesetting endpoint issue, or a nonstandard CI method may have been used. No source in the package distinguishes these explanations.
- **Missing definition:** The death-difference CI method and contrast orientation used for the reported interval.
- **Human verification question:** Recompute the death-proportion CI from the analysis dataset using the reported method, then verify the printed upper endpoint and contrast label.

## C005 — Outside-study vitamin-D difference CI includes zero while printed P=.002

- **Workflow category:** Statistical reporting inconsistency.
- **Status:** Pending Human Adjudication.
- **Canonical relationships:** `N028`; `S012`.
- **Lane provenance:** Statistical pass 1 `SCAND-002`. Numeric lane mapped/checks N028 but made no separate proposal; cross-source lane made no distinct proposal.
- **Exact direct-PDF location and printed evidence:** DOC-001, [p.5](../../jama_lappe_2017_oi_170019.pdf#page=5), Table 2, outside-study vitamin D3 intake (visits 2–9), prints treatment `N=1099`, 740 (691 to 789) IU/d, versus placebo `N=1094`, 869 (803 to 934) IU/d; the between-group difference is `−128.1` (95% CI `−209.5 to 46.6`), `P=.002`.
- **Comparator and reproducible rule:** The printed means support a negative treatment-minus-placebo difference (`740−869=−129`, compatible with −128.1). The printed interval is ordered and contains −128.1 but includes the null zero. For a corresponding same-contrast two-sided 95% interval and two-sided null test, an interval including zero is incompatible with `P=.002`.
- **Direct observation:** The same contrast row prints the interval `−209.5 to 46.6` and two-sided `P=.002`.
- **Diagnostic inference:** Changing only the upper printed endpoint to `−46.6` makes an approximately symmetric interval around −128.1 (`−128.1 ± 81.5`); the implied `SE≈41.6`, `|z|≈3.08`, and two-sided normal-tail P is approximately `.002`. This is an explanatory diagnostic only and does not prescribe that correction. The Table 2 CI/test method is not supplied.
- **Source-grounded alternatives:** A missing minus sign before `46.6` would reconcile the printed difference, CI direction, and P; alternatively, the table may use an unreported non-corresponding CI/test pairing. The supplied evidence does not choose between them.
- **Missing definition:** Table 2 variance/CI method and exact test used for the P value.
- **Human verification question:** Verify the upper CI endpoint against the analysis output or production source and confirm whether it was `−46.6` or `46.6`.

## C006 — Figure 1 discontinuation counts conflict with p.7 vitamin-D/placebo discontinuation total and percentages

- **Workflow category:** Cross-document numeric inconsistency.
- **Status:** Pending Human Adjudication.
- **Canonical relationships:** `N019`; `N039`; `S020`.
- **Lane provenance:** Cross-source consistency `XCAND-001`. Numeric consistency covered `N017`–`N020` and `N039`–`N041` without a separate proposal; statistical pass 1 covered `S020` without a separate proposal.
- **Exact direct-PDF locations and printed evidence:** DOC-001 Figure 1, [p.4](../../jama_lappe_2017_oi_170019.pdf#page=4), prints `238 Discontinued intervention` in the vitamin-D-plus-calcium arm (components 11+93+134) and `246 Discontinued intervention` in placebo (16+76+154). DOC-001 narrative, [p.7](../../jama_lappe_2017_oi_170019.pdf#page=7), prints: “During follow-up, 304 participants (13.2%; 12.4% of the vitamin D3 + calcium group and 14.0% of the placebo group) stopped taking the vitamin D or placebo supplement.”
- **Comparator and reproducible rule:** Both locations concern the completed randomized trial, follow-up, and assigned vitamin-D-containing study supplement/placebo contrast. Figure 1 counts sum to `238+246=484`; the narrative total is 304. Narrative group percentages imply about `143/1156` and `161/1147`, summing to 304 at displayed-percent precision. Rounding cannot reconcile 484 with 304.
- **Direct observation:** The paper prints the Figure 1 238/246 counts and the p.7 304/12.4%/14.0% discontinuation statement.
- **Diagnostic inference:** Under the ordinary reading that Figure 1 “Discontinued intervention” means stopping the vitamin-D-containing assigned intervention, the counts are conflicting reports of the same follow-up construct. Figure 1 does not define whether it instead represents a broader composite (for example, stopping either component or another protocol-status category), which could explain the difference.
- **Source-grounded alternatives:** (1) Figure 1 correctly uses a broader discontinuation construct than the narrative’s vitamin-D/placebo stopping endpoint; (2) the p.7 total/percentages are correct but the figure label or counts are wrong; (3) both are valid but use an unstated different time window or event rule. The supplied PDFs do not distinguish them.
- **Missing definition:** The exact Figure 1 discontinuation event definition, component(s), time window, and participant-level counting rule, and its relation to the p.7 statement.
- **Human verification question:** What exact rule produced the Figure 1 238/246 counts, and does it differ from the p.7 304 participants stopping vitamin D or placebo? If it does not differ, which printed counts and percentages should be corrected?

## Completeness statement

The ledger preserves all six assigned IDs without suppression or renumbering. The source package supports the six records above and no additional proposal was emitted by the three completed checker artifacts at the time of merge.
