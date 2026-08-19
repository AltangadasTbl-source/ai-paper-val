# Numeric Consistency Review

## Scope and method

This mandatory fresh numeric review covers the complete mapped scope: DOC-001 `jama_dupuis_2024_oi_240111_1733431204.38761.pdf` pp. 1-11; DOC-002 `joi240111supp1_prod_1733431204.57929.pdf` pp. 1-46; and DOC-003 `joi240111supp2_prod_1733431204.76024.pdf` pp. 1-23. The stable relationship inventory is `relationships/numeric_relationship_inventory.md`.

I checked applicable arithmetic, row and column totals, subgroup sums, numerator/denominator/percentage relationships, missingness and population identities, rounded displays, scales, units, reference groups, rate-versus-count distinctions, person-time labels, repeated values, and measure labels. Direct PDFs are authoritative. The two canonical extraction maps were used as complete locators; targeted direct-PDF extraction confirmed both raw candidates. This document does not assign a C ID, severity, validity, disposition, or correction.

## Raw candidate records

### NC-01 — Post-registration source-layout repair of the usual-care exclusion hierarchy

**Primary category:** Numeric or arithmetic inconsistency.

**Exact source location:** DOC-001 `jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5`, Figure 1, usual-care arm, under “323 Patients screened for inclusion.”

**Printed inputs:** The figure prints “58 Patients excluded.” Visual indentation makes 13 physician preference a parent of the more deeply indented 7 disease status or progression, 4 perceived psychosocial issues, and 2 reason not provided. The other top-level values are 15 treatment outside of trial network, 14 cognitive disability, 7 language, 4 visual impairment, 3 no parent available, and 2 cancer not disclosed.

**Reproducible rule and calculation:** Children reconcile to their immediate parent: `7 + 4 + 2 = 13`. The top-level reasons reconcile exactly: `13 + 15 + 14 + 7 + 4 + 3 + 2 = 58`. The earlier flat sum of 71 double-counted the 13 parent and its children. The parallel screening branch confirms the visual convention because `32 + 4 + 2 + 4 = 42` under its 42 physician-preference parent. The downstream flow also reconciles: `323 - 58 = 265` and `265 - 41 = 224`.

**Tolerance:** Exact counts; tolerance 0. This is not a rounding comparison.

**Direct observation:** Figure 1 directly displays the counts and the two indentation levels.

**Inference:** The parent-child reading follows visual indentation and is corroborated by the parallel arm; it does not require an overlap assumption.

**Source-grounded alternatives:** A production-layout error could theoretically make the indentation misleading, but the identical hierarchy in the parallel branch supports the parent-child reading.

**Quality-control relevance:** Data extractors should preserve the hierarchy and should not propagate the superseded flat sum of 71.

**Exact human question:** Does the production source confirm that the indentation denotes the 13-parent hierarchy? The stable C001 record remains pending human adjudication and is not a 71-versus-58 claim.

### NC-02 — The main-text percentage of rejected care-pathway statements conflicts with the supplement’s displayed counts

**Primary category:** Denominator, proportion, or total inconsistency.

**Exact source locations:**

- DOC-001 `jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2`, Site Preparation and Patient Enrollment: “Overall, 40.8% of template care pathway statements were adopted, 48.7% were adapted, and 6.4% were rejected across all intervention sites.”
- DOC-003 `joi240111supp2_prod_1733431204.76024.pdf#page=6`, eTable 3, “Distribution of Care Pathway Adaptation Decisions by Site.”

**Printed inputs:** eTable 3 states `n=135` for each of 10 sites. Its “Reject” row prints counts 15, 23, 5, 25, 9, 25, 12, 11, 11, and 6; its site-specific reject percentages are 11.1%, 17.1%, 3.7%, 18.5%, 6.7%, 18.5%, 8.9%, 8.2%, 8.2%, and 4.4%. The same table prints Keep as is and Adapt counts for every site. The main text prints 6.4% rejected and a 3.7%-18.5% site range.

**Reproducible rule and calculation:** Because the table supplies a common denominator of 135 at each of 10 sites, the cross-site rejection percentage implied by the displayed table is total rejected statements divided by total statements.

`total statements = 10 x 135 = 1,350`

`total rejected = 15 + 23 + 5 + 25 + 9 + 25 + 12 + 11 + 11 + 6 = 142`

`142 / 1,350 x 100 = 10.5185...%`, which rounds to **10.5%** at one decimal place.

The corresponding printed keep and adapt counts are 551 and 657, giving `551/1,350 = 40.8%` and `657/1,350 = 48.7%`; these agree with the main text. The eTable’s reject-row range, 3.7%-18.5%, also agrees with the main-text range. Only the main-text rejected percentage, 6.4%, fails to reconcile with the displayed rejection counts.

**Tolerance:** One-decimal percentage displays; inclusive rounding tolerance +/-0.05 percentage points. The 4.1-point difference between 6.4% and 10.5% exceeds this tolerance.

**Direct observation:** DOC-001 directly prints 40.8%, 48.7%, and 6.4%. DOC-003 directly prints ten equal denominators (135), all ten reject counts, the keep/adapt counts, and the rejection range.

**Inference:** The 10.5% aggregate is derived directly from the printed eTable counts and denominators. The matching keep/adapt aggregates and matching range support the same aggregation rule; they do not prove the cause of the rejected-percentage conflict.

**Source-grounded alternatives:** The 6.4% might refer to a different, unprinted denominator or a narrower definition of “rejected,” but the main text says “template care pathway statements ... across all intervention sites,” and eTable 3 is explicitly the stated site-decision source. No separate denominator or narrower rejection definition is printed at either cited location. A transcription error in the narrative percentage is another unresolved possibility.

**Quality-control relevance:** This is a direct total/proportion discrepancy in intervention-implementation reporting. It may affect numeric extraction of pathway adaptation and interpretation of the stated implementation distribution; it does not by itself establish an effect on the trial’s clinical outcome conclusions.

**Exact human question:** What denominator and definition produce the printed 6.4% rejected statement, and should the main text instead report the 142/1,350 = 10.5% aggregate shown by eTable 3 or identify a distinct rejected-statement population?

## Checks completed without a raw candidate

The remaining 78 inventory relationships were checked without a distinct candidate. This includes all Table 1 demographic denominators and percentages; Table 2 score, symptom, fatigue, and PedsQL values; Figure 2 labels and denominators; Table 3 encounter distributions, crude rates, adjusted rate ratios, and rate labels; protocol/SAP plan-versus-result labels; supplementary completion/missingness values; all eTable 10 printed numerator/denominator/percentage cells with changing cohorts; eTable 11 percentages; eTable 12 rate-ratio/credible-region labels; and matched forest-plot values. Apparent crude-versus-adjusted differences were retained as distinct measures when source footnotes identify different models, rather than treated as arithmetic errors.

## Display-zero handling

No raw candidate was generated solely from `P < .001`, `P = 0`, `p = 0.000`, or another finite-precision display convention. The reviewed materials use threshold displays such as `P < .001`; no independent supplied-source contradiction was identified for those displays.

## Counts and limitations

- Stable N relationships reviewed: **80**.
- Raw candidates emitted before stable-ID registration: **2** (NC-01 and NC-02). The later evidence-quality audit corrected NC-01's source hierarchy; its already assigned C001 remains preserved for human adjudication.
- Direct source coverage reviewed: DOC-001 pp. 1-11, DOC-002 pp. 1-46, DOC-003 pp. 1-23.

Limitations are limited to source presentation: DOC-001 Figure 2 has no printed bar-segment values; DOC-002 planned table shells are intentionally unpopulated; and detailed statistical compatibility requiring unreported modeling choices remains for the separate statistical passes. These limitations do not prevent the two arithmetic/denominator observations above.
