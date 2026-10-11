# Mechanical Evidence Recheck

Scope: stable candidates C001, C002, C003, C004, C005, C006, and C007. Every comparison below was re-read against the supplied PDF at the stated PDF page. Fresh native/layout text and rendered pages were used only to locate and inspect the source; the supplied PDFs are the authority. All candidates remain **Pending Human Adjudication**.

## C001 — Figure 2 omega-3 eGFR contributor counts conflict with Table 2

- **Cited location found:** Yes. [DOC-001 Figure 2 panel B, PDF p. 7](<../../../jama_de_boer_2019_oi_190122.pdf#page=7>) and [DOC-001 Table 2, PDF p. 8](<../../../jama_de_boer_2019_oi_190122.pdf#page=8>) are present at the cited pages.
- **Source printed value/text matched:** Figure 2 panel B prints omega-3 placebo counts `607`, `459`, and `438`, and omega-3-fatty-acid counts `701`, `531`, and `496`, at baseline, year 2, and year 5. The caption states that the numbers shown are participants contributing data at each time point.
- **Comparator matched:** Table 2 prints omega-3 placebo `651`, `491`, and `462`, and active intervention `657`, `499`, and `472`, at the same three time points. Figure 2 panel A separately prints the exact `607/459/438` placebo and `701/531/496` vitamin-D sequences that recur in panel B.
- **Consistency rule applicable:** Yes. For the same eGFR outcome, omega-3 assignment, and time points, arm-specific observed contributor counts should retain the same arm membership unless a figure-specific population is stated.
- **Calculation or logical comparison reproduced:** At baseline/year 2/year 5, Figure 2 minus Table 2 equals `-44/-32/-24` for omega-3 placebo and `+44/+32/+24` for omega-3 active. The arm totals nevertheless agree at each time (`1308`, `990`, and `934`). Thus the disagreement is an arm split, not a total-count disagreement, and panel B exactly repeats panel A's arm split.
- **Necessary inputs available:** The outcome, factorial contrast, arm labels, time points, contributor counts, table counts, and figure caption are available.
- **Exact missing inputs or definitions:** The package does not provide figure-production data, a separate panel-B inclusion rule, or a statement that panel B uses a population different from Table 2.
- **Source-grounded alternative interpretation:** Panel B could use an unstated arm-specific plotting subset whose combined total happens to equal Table 2 at every time point. The exact repetition of panel A's sequences also permits a copied count-annotation explanation, but the source does not establish production mechanism.
- **Direct observation:** The two arm-specific sequences disagree at all six matched cells, while their time-specific totals agree and panel B's sequences equal panel A's sequences.
- **Inferred explanation:** An unstated subset or copied annotations are possible explanations only; neither is directly stated in the supplied source.
- **Exact remaining human question:** Which omega-3 arm-specific contributor counts and population definition were intended for Figure 2 panel B at baseline, year 2, and year 5?

## C002 — Figure 2 omega-3 urine-ACR contributor counts conflict with eTable 6

- **Cited location found:** Yes. [DOC-001 Figure 2 panel D, PDF p. 7](<../../../jama_de_boer_2019_oi_190122.pdf#page=7>) and [DOC-003 eTable 6, PDF p. 11](<../../../joi190122supp2_prod.pdf#page=11>) are present at the cited pages.
- **Source printed value/text matched:** Figure 2 panel D prints omega-3 placebo counts `609`, `463`, and `440`, and omega-3-fatty-acid counts `702`, `529`, and `505`, at baseline, year 2, and year 5. The Figure 2 caption identifies these as contributors at each time point.
- **Comparator matched:** eTable 6 prints omega-3 placebo `653`, `490`, and `467`, and active intervention `658`, `502`, and `478`, at the same times. Figure 2 panel C prints the exact `609/463/440` placebo and `702/529/505` vitamin-D sequences that recur in panel D; eTable 6 prints those same panel-C sequences for vitamin D.
- **Consistency rule applicable:** Yes. For the same urine-ACR outcome, omega-3 assignment, and time points, the arm-specific contributor counts should agree unless a different population is defined.
- **Calculation or logical comparison reproduced:** Figure 2 minus eTable 6 equals `-44/-27/-27` for omega-3 placebo and `+44/+27/+27` for omega-3 active. The two arms sum to the same totals in both locations at each time (`1311`, `992`, and `945`). Panel D therefore changes the arm split without changing the totals and exactly repeats panel C's split.
- **Necessary inputs available:** The outcome, contrast, time points, arm labels, figure contributor counts, and eTable 6 counts are available.
- **Exact missing inputs or definitions:** The package does not supply panel-D production data, a figure-specific arm-selection rule, or a stated population difference between Figure 2 and eTable 6.
- **Source-grounded alternative interpretation:** An unstated plotting subset with identical overall totals is possible. Exact reuse of the vitamin-D panel's annotations is another possible explanation, but it is inferred rather than documented.
- **Direct observation:** All six arm-specific matched counts differ; time-specific totals agree; panel D's sequences equal panel C's sequences.
- **Inferred explanation:** A copied-annotation mechanism or distinct subset is not directly established by the supplied source.
- **Exact remaining human question:** Which omega-3 urine-ACR contributor counts and population definition were intended for Figure 2 panel D at baseline, year 2, and year 5?

## C003 — Figure 3 assigns vitamin-D arm sizes to the opposite column labels

- **Cited location found:** Yes. [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>) and [DOC-001 Table 2 and Figure 3, PDF p. 8](<../../../jama_de_boer_2019_oi_190122.pdf#page=8>) are present.
- **Source printed value/text matched:** Figure 3 places overall `N=703` under `Placebo` and `N=609` under `Vitamin D`. In its omega-3-randomization rows, the first count column contains `333` and `370`, while the second contains `320` and `289`.
- **Comparator matched:** The abstract prints factorial-cell allocations of `370` for vitamin D plus omega-3, `333` for vitamin D plus omega-3 placebo, `289` for vitamin-D placebo plus omega-3, and `320` for two placebos. Table 2 labels vitamin D as the active intervention and prints observed baseline counts `701` active and `607` placebo.
- **Consistency rule applicable:** Yes. Randomized arm totals and nested factorial-cell counts must retain intervention identity when placed under treatment headings.
- **Calculation or logical comparison reproduced:** Vitamin-D active totals `370 + 333 = 703`; vitamin-D placebo totals `289 + 320 = 609`. Figure 3 places `703` under `Placebo` and `609` under `Vitamin D`. Its first-column nested counts also sum `333 + 370 = 703` and both cells received active vitamin D; its second-column counts sum `320 + 289 = 609` and both cells received vitamin-D placebo.
- **Necessary inputs available:** Factorial treatment definitions, randomized cell sizes, figure headings, overall N values, and nested factorial N values are available.
- **Exact missing inputs or definitions:** The source lacks figure-production metadata specifying whether the N columns alone, the headings, or additional elements were transposed. No independent subgroup table supplies every subgroup mean and plotted estimate for a cell-by-cell remapping.
- **Source-grounded alternative interpretation:** The participant-count columns may be transposed while the headings and mean-change values remain treatment-aligned. At the overall level, Figure 3's printed mean changes (`-13.1` under placebo and `-12.3` under vitamin D) agree in treatment direction and rounded value with Table 2, so the available evidence does not require the mean-change columns to be exchanged.
- **Direct observation:** The overall and nested participant counts beneath the two Figure 3 headings map to the opposite randomized vitamin-D assignments.
- **Inferred explanation:** A participant-count-column transposition is a plausible production explanation; whether any other figure elements were affected is not directly shown.
- **Exact remaining human question:** Are only the Figure 3 participant-count columns transposed, and what N should appear under each treatment heading for every subgroup row while preserving the intended mean changes and plotted estimates?

## C004 — Figure 4 assigns omega-3 arm sizes to the opposite column labels

- **Cited location found:** Yes. [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>), [DOC-001 Table 2, PDF p. 8](<../../../jama_de_boer_2019_oi_190122.pdf#page=8>), and [DOC-001 Figure 4, PDF p. 9](<../../../jama_de_boer_2019_oi_190122.pdf#page=9>) are present.
- **Source printed value/text matched:** Figure 4 places overall `N=659` under `Placebo` and `N=653` under `Omega-3 Fatty Acids`. In its vitamin-D-randomization rows, the first count column contains `289` and `370`, while the second contains `320` and `333`.
- **Comparator matched:** The abstract's factorial cells are `370` vitamin D plus omega-3, `333` vitamin D plus omega-3 placebo, `289` vitamin-D placebo plus omega-3, and `320` two placebos. Table 2 labels omega-3 fatty acids as active and prints observed baseline counts `657` active and `651` placebo.
- **Consistency rule applicable:** Yes. Overall randomized arm totals and their nested factorial cells must retain omega-3 treatment identity beneath the figure headings.
- **Calculation or logical comparison reproduced:** Omega-3 active totals `370 + 289 = 659`; omega-3 placebo totals `333 + 320 = 653`. Figure 4 places `659` under `Placebo` and `653` under `Omega-3 Fatty Acids`. The first-column nested counts sum `289 + 370 = 659` and both cells received active omega-3; the second-column counts sum `320 + 333 = 653` and both cells received omega-3 placebo.
- **Necessary inputs available:** Factorial assignments, randomized cell sizes, figure headings, overall N values, nested N values, and Table 2 treatment labels are available.
- **Exact missing inputs or definitions:** The package lacks figure-production metadata and an independent cell-level comparator for every subgroup mean and plotted estimate.
- **Source-grounded alternative interpretation:** The N columns may be transposed while headings and mean-change values remain treatment-aligned. At the overall level, Figure 4 prints `-13.1` under placebo and `-12.2` under omega-3, matching the corresponding rounded Table 2 changes, so the evidence does not require exchanging the mean-change columns.
- **Direct observation:** Figure 4's overall and nested participant counts map to the opposite omega-3 randomized assignments from their headings.
- **Inferred explanation:** A participant-count-column transposition is plausible; involvement of other figure elements is not directly demonstrated.
- **Exact remaining human question:** Are only the Figure 4 participant-count columns transposed, and what N should appear under each treatment heading for every subgroup row while preserving the intended mean changes and plotted estimates?

## C005 — eFigure 2 places vitamin-D participant counts under the opposite headings

- **Cited location found:** Yes. [DOC-003 eTable 6, PDF p. 11](<../../../joi190122supp2_prod.pdf#page=11>) and [DOC-003 eFigure 2, PDF p. 18](<../../../joi190122supp2_prod.pdf#page=18>) are present.
- **Source printed value/text matched:** eFigure 2 places overall `N=703` and geometric-mean change `3.02` under `Placebo`, and `N=609` and change `2.97` under `Active intervention`. Its omega-3-randomization rows place `333` and `370` in the first N column and `320` and `289` in the second.
- **Comparator matched:** eTable 6 identifies vitamin-D active baseline `N=702` and year-5 change ratio `2.97`, and placebo baseline `N=609` and ratio `3.02`. [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>) prints factorial allocations that produce `703` randomized to active vitamin D and `609` to vitamin-D placebo; the one-person `703` versus `702` difference is consistent with randomized total versus measured baseline availability.
- **Consistency rule applicable:** Yes. A displayed N must preserve the treatment identity of the arm it counts. The printed arm-specific change ratios can be checked separately from the N mapping.
- **Calculation or logical comparison reproduced:** Active vitamin D is `370 + 333 = 703`; vitamin-D placebo is `289 + 320 = 609`. eFigure 2 places those N values under the opposite headings. Its first nested N column is `333 + 370 = 703`, both active-vitamin-D cells; its second is `320 + 289 = 609`, both vitamin-D-placebo cells. In contrast, the printed `3.02` placebo and `2.97` active changes match eTable 6 under their stated treatment headings.
- **Necessary inputs available:** Figure headings, overall and nested N values, arm-specific change values, eTable 6 arm labels and values, and factorial allocations are available.
- **Exact missing inputs or definitions:** The package lacks figure-production metadata and an independent table for every subgroup change and forest estimate. It does not state whether only participant counts were transposed.
- **Source-grounded alternative interpretation:** The participant-count columns may be transposed while the arm headings, change values, and forest direction remain as printed. The available overall comparator supports this narrower interpretation because `3.02` is the table's placebo change and `2.97` is its active change.
- **Direct observation:** eFigure 2's overall and nested N values map to the opposite vitamin-D assignments, while its overall change values map to the printed headings and eTable 6.
- **Inferred explanation:** A count-column transposition is plausible; a reversal of all values or the forest direction is not established by the overall source comparison.
- **Exact remaining human question:** Should only the eFigure 2 N columns be exchanged, or do any subgroup changes or plotted estimates also require remapping; what is the intended treatment identity of each displayed element?

## C006 — eFigure 3 places omega-3 participant counts under the opposite headings

- **Cited location found:** Yes. [DOC-003 eTable 6, PDF p. 11](<../../../joi190122supp2_prod.pdf#page=11>) and [DOC-003 eFigure 3, PDF p. 19](<../../../joi190122supp2_prod.pdf#page=19>) are present.
- **Source printed value/text matched:** eFigure 3 places overall `N=659` and geometric-mean change `3.05` under `Placebo`, and `N=653` and change `2.94` under `Active intervention`. Its vitamin-D-randomization rows put `289` and `370` in the first N column and `320` and `333` in the second.
- **Comparator matched:** eTable 6 identifies omega-3 active baseline `N=658` and year-5 change ratio `2.94`, and omega-3 placebo baseline `N=653` and ratio `3.05`. [DOC-001 abstract, PDF p. 1](<../../../jama_de_boer_2019_oi_190122.pdf#page=1>) prints factorial allocations that produce `659` randomized to active omega-3 and `653` to omega-3 placebo; the one-person `659` versus `658` difference is consistent with randomized total versus measured baseline availability.
- **Consistency rule applicable:** Yes. Participant counts must retain the randomized treatment identity represented by their heading; arm-specific change values are checked as a separate mapping.
- **Calculation or logical comparison reproduced:** Omega-3 active is `370 + 289 = 659`; omega-3 placebo is `333 + 320 = 653`. eFigure 3 places those Ns under the opposite headings. Its first nested N column is `289 + 370 = 659`, both active-omega-3 cells; its second is `320 + 333 = 653`, both omega-3-placebo cells. Conversely, `3.05` under placebo and `2.94` under active match eTable 6's treatment-specific changes.
- **Necessary inputs available:** Figure headings, overall and nested N values, table arm labels and changes, and factorial allocation sizes are available.
- **Exact missing inputs or definitions:** The source lacks figure-production metadata and a separate source mapping every subgroup change and forest estimate. It does not state whether only N columns were transposed.
- **Source-grounded alternative interpretation:** The N columns may be transposed while headings, change values, and forest direction remain as printed. The overall `3.05` placebo and `2.94` active changes support that narrower source-grounded interpretation.
- **Direct observation:** The eFigure 3 N values map to the opposite omega-3 assignments, but its overall change values map to their stated headings and eTable 6.
- **Inferred explanation:** A participant-count-column transposition is plausible; the supplied comparison does not directly show that all values or the forest direction are reversed.
- **Exact remaining human question:** Should only the eFigure 3 N columns be exchanged, or do any subgroup changes or plotted estimates also require remapping; what is the intended treatment identity of each displayed element?

## C007 — Imputation count differs between the analytic-plan addendum and article methods

- **Cited location found:** Yes. [DOC-001 Methods, PDF p. 3](<../../../jama_de_boer_2019_oi_190122.pdf#page=3>) contains the article statement, and [DOC-002 Section 15c, PDF p. 32](<../../../joi190122supp1_prod.pdf#page=32>) contains the plan statement cited in the corrected ledger.
- **Source printed value/text matched:** On DOC-002 PDF p. 32, Section 15c states that results from `10 imputation datasets` will be combined using Rubin's rules. On DOC-001 PDF p. 3, Data Analysis states that multiple imputation `(M = 20)` was used for missing data and estimates were combined across imputations using Rubin rules.
- **Comparator matched:** Yes, after using DOC-002 PDF p. 32 as the exact plan location. Both passages concern multiple imputation for missing follow-up outcome information and Rubin-rule combination, but the article describes the implemented analysis more broadly than the plan passage.
- **Consistency rule applicable:** Yes as a plan-versus-implemented-method comparison: the two supplied records give different exact imputation counts for related missing-outcome analyses. A final implementation may intentionally differ from an earlier plan, so the numeric difference does not by itself establish whether documentation was required.
- **Calculation or logical comparison reproduced:** The direct numeric comparison is `20 - 10 = 10`; the article reports twice the number of imputed datasets stated in the plan. Both passages explicitly name Rubin-rule combination.
- **Necessary inputs available:** The planned count, implemented count, missing-data context, and combination rule are available.
- **Exact missing inputs or definitions:** The package lacks a dated change record, rationale, or other statement explaining the move from 10 to 20. It also does not establish whether the article's broader imputation scope was governed by this exact plan version without a later amendment.
- **Source-grounded alternative interpretation:** The implemented analysis may intentionally have increased the number of imputations and broadened the full analytic population after the plan text was written. A plan and final method may differ, and the article may accurately report the final procedure.
- **Direct observation:** The supplied plan prints `10` and the article prints `M = 20`; the corrected ledger cites the exact plan location on DOC-002 PDF p. 32.
- **Inferred explanation:** An intentional analytic update is plausible but is not documented in the supplied package passages reviewed here.
- **Exact remaining human question:** Was the change from 10 planned imputation datasets to 20 implemented imputations intentional and documented in a later governing record, and should the supplied plan-versus-method record state the change?
