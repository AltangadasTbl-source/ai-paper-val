# Cross-Source Consistency Check

## Scope and method

This check covered all result-relevant matched relationships in DOC-001, DOC-002, and DOC-003 using the two canonical extraction maps and direct confirmation in the supplied PDFs. A difference was called only after matching the study population, time point, contrast, model, measure, scale, unit, reference group, analysis set, and printed precision. DOC-002 is a protocol/SAP source and its planned table shells contain no observed results; it was used for definitions and planned-model comparisons, not as an alternative observed-result table.

Direct sources checked:

- [DOC-001 main article](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2), PDF pp. 1-11.
- [DOC-002 protocol/SAP](../../../joi240111supp1_prod_1733431204.57929.pdf#page=1), PDF pp. 1-46.
- [DOC-003 results supplement](../../../joi240111supp2_prod_1733431204.76024.pdf#page=1), PDF pp. 1-23.

## Matched scope and count

Forty-six matched result or definition families were checked: enrollment/analysis populations and completion; care-pathway adaptation decisions; the week-8 primary model; the baseline model; six primary sensitivity/missing-data analyses; 15 individual SSPedi proportional-odds results; severe-symptom risk-difference results; week-4 outcomes; PROMIS fatigue; eight PedsQL domains; documentation, any-intervention, and symptom-specific-intervention outcome sets; pathway-consistent intervention counts; four encounter models; and planned outcome/model definitions in the protocol/SAP.

The repeated primary, individual-symptom, fatigue/PedsQL, documentation/intervention, participant-flow, and encounter values matched after their distinct populations, estimands, models, and displayed precision were preserved. The following is the one distinct qualifying candidate found.

## Candidate: overall care-pathway rejection percentage conflicts with the site-level table

**Primary category:** Cross-document numeric inconsistency

**Matched result identity:** Care-pathway adaptation decisions across all 10 intervention sites. The common denominator is 135 template statements at each site, or 1,350 site-statement decisions in total. This is an implementation result, not a patient-level outcome; no participant population, time-point, treatment contrast, statistical model, reference group, or transformed scale differs between the locations.

**Exact linked locations and printed values:**

- The main article states: “Overall, 40.8% of template care pathway statements were adopted, 48.7% were adapted, and **6.4% were rejected across all intervention sites**.” [DOC-001, p. 2](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2)
- DOC-003 eTable 3 prints `n = 135` for each of 10 sites and gives the `Reject` counts as 15, 23, 5, 25, 9, 25, 12, 11, 11, and 6. [DOC-003 eTable 3, p. 6](../../../joi240111supp2_prod_1733431204.76024.pdf#page=6)
- The same eTable prints `Keep as is` counts totaling 551 and `Adapt` counts totaling 657, which reproduce the main article’s 40.8% and 48.7%, respectively, at one-decimal displayed precision. [DOC-003 eTable 3, p. 6](../../../joi240111supp2_prod_1733431204.76024.pdf#page=6)

**Comparison logic:**

The printed eTable 3 rejection counts total 142. With the displayed denominator of 10 × 135 = 1,350 decisions, the directly pooled rejection proportion is 142/1,350 = 10.5185%, which displays as 10.5% to one decimal place. It does not equal the main article’s printed 6.4%, and normal rounding cannot bridge the 4.1-percentage-point difference. The table’s individual-site rejection percentages (3.7% through 18.5%) and the main article’s stated site-level range are mutually compatible, but that range does not resolve the overall total.

**Supported alternatives that do not remove the observed mismatch:**

- A different denominator or exclusion rule may have been used for the main article’s 6.4%, but neither the main-article sentence nor eTable 3 identifies one. The eTable labels all three rows as adaptation choices and prints the same 135-statement denominator at every site.
- An unweighted mean of the ten printed site percentages is also about 10.5% because all sites have equal denominators; it does not yield 6.4%.
- The 6.4% may refer to an unprinted rejection subset rather than the eTable’s `Reject` row. The supplied sources do not label the main-text number as a subset, so this remains a human verification question rather than an asserted correction.

**Human verification steps:**

1. Inspect the cited main-article sentence and eTable 3 `n` and `Reject` rows in the supplied PDFs.
2. Re-add the ten printed rejection counts: 15 + 23 + 5 + 25 + 9 + 25 + 12 + 11 + 11 + 6 = 142.
3. Divide 142 by 1,350 and compare the one-decimal result (10.5%) with the printed 6.4%.
4. Consult the analysis/implementation source used to prepare the main-text aggregate, if available, to determine whether 6.4% denotes a defined subset or is a transcription/aggregation difference.

## Limitations

DOC-002 provides planned definitions and blank reporting shells rather than a second display of observed trial results. DOC-003 eFigure 2 and eFigure 3 estimates were available as visual displays and were compared through their direct-source-confirmed transcription in the canonical map; no unsupported bar or plot measurements were created. This check does not adjudicate the cause of the recorded mismatch or prescribe a correction.

**Raw qualifying candidate count:** 1
