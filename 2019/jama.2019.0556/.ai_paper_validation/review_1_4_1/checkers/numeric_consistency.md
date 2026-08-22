# Numeric Consistency Review

## Scope and method

Checked the complete unified inventory N001-N095 from DOC-001 pp. 1-11, DOC-002 pp. 1-60, DOC-003 pp. 1-5, DOC-004 pp. 1-25, and DOC-005 p. 1. Checks applied: displayed sums/differences; numerator/denominator/percentage agreement with ordinary rounding to the printed precision; mutually exclusive total/population identity; missingness definitions; rate/person-time labels; scale/unit/reference labels; repeated values; and matching main/supplement/protocol occurrences. Direct-source page locations, rather than OCR, are cited as evidence.

## Completed checks without a candidate

- **Flow and allocations (N007-N012):** 5965-3730=2235; 2235-462=1773; 1773-523=1250; 1250-225=1025. Both displayed exclusion-component lists sum to their headings. Allocation 256+256+256+257=1025. Month-3/6/12 assessment sums are 831/771/779, yielding 194/254/246 nonparticipants. Loss reasons sum to 65/62/58/61. The 246 month-12 nonmeasurements and 239 Table 2 follow-up dropouts use explicitly different definitions and are not compared as the same population.
- **Baseline table (N015-N027):** Sex, site, and education group components reconcile to denominators 257/256/256/256, with percentages compatible with ordinary one-decimal rounding. MDD-history and >=2-episode rows are nested, not mutually exclusive categories. No scale/direction or unit conflict was observed.
- **MDD counts/rates (N028-N031):** Four cells sum to 105 events and 1025 randomized; factorial partitions yield 51+54=105, 57+48=105, 513+512=1025, and dropouts 113+126=122+117=239. Percentages and rates are compatible with their stated denominators/person-months. The abstract, Key Points, narrative, and Table 2 agree when comparison definition is matched.
- **Secondary/figure values (N033-N035):** Figure counts are correctly labelled available data; no assertion that each outcome shares a common denominator is made. Narrative unadjusted means are distinguished from adjusted effects and have no incompatible unit/scale label.
- **Supplement adherence/biomarker/change table (N037-N055):** Each printed percentage is compatible with an integer group denominator and the stated total N (allowing printed one-decimal rounding); the four implied denominators sum to 666, 855, 652, and 855 respectively. F-BA NA cells align with no-F-BA groups. Deaths/hospitalizations agree with DOC-001. T0/T12, delta, units, medians/IQRs, and kappa labels have no internal arithmetic conflict; “%kg from baseline weight” is an unusual but intelligible percentage-weight label, so no mismatch is asserted.
- **Figures and concealment (N056-N065):** eAppendix 9 supplies no per-cell numerical result to total. eAppendix 13 rows total to 195/193/188/183 (759 overall); row percentages match those denominators to one decimal; unknown responses total 307/759=40.4% and supplement-belief percentages/P value match DOC-001.
- **New protocol/SAP/remaining-appendix coverage (N068-N070, N072, N074-N095):** Prespecified schedules, doses, scale cutoffs, adherence rules, product-assay units, and safety/ascertainment definitions have been retained as rules rather than compared to observed results unless a matched quantity is printed. The new source units contain no additional observed result table or count beyond the already reconciled DOC-004 eAppendix 8/13 displays. Main/SAP/eAppendix supplement-adherence definitions consistently use >=70%; this strengthens, but does not alter, NC-02. DOC-005 contains no numerical relationship applicable to a consistency check.

## Candidate consistency issues for later registration (no stable C IDs)

### NC-01 — Duplicated treatment-group label in Table 2 supplements footnote

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 Table 2, PDF p. 6](<../../../jama_bot_2019_oi_190007.pdf#page=6>); comparator allocation and event cells: [DOC-001 Figure 1, PDF p. 3](<../../../jama_bot_2019_oi_190007.pdf#page=3>) and [DOC-001 Results, PDF p. 7](<../../../jama_bot_2019_oi_190007.pdf#page=7>).
- **Direct observation:** Footnote d prints: “32 of 256 participants (12.5%) in the supplements without therapy group and 22 of 256 (8.6%) in the supplements without therapy group.” Figure 1 and Results print 32/256 (12.5%) for supplements without therapy and 22/256 (8.6%) for supplements with therapy.
- **Rule and calculation:** The supplements main-effect numerator is 32+22=54 and denominator 256+256=512, matching the Table 2 supplements row. In the mutually exclusive 2x2 allocation, the two component labels must identify the two different therapy strata. Repeating “without therapy” assigns both components to one 256-person stratum and leaves the other component unlabeled.
- **Observation versus inference:** The duplicate phrase is directly printed. Inferring that the second phrase was intended to read “with therapy” follows the printed Figure 1/Results mapping; it is not a correction applied to the source.
- **Alternative source-grounded interpretation:** The numerical event counts, percentages, total 54/512, OR, CI, and P value are mutually compatible; the defect may be confined to the footnote label.
- **Human question:** Does the published Table 2 footnote d require a correction of its second treatment-group label to “supplements with therapy,” and did any downstream representation reproduce the duplicated label?

### NC-02 — Supplement-adherence boundary is stated inconsistently across locations

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 Other Measures, PDF p. 4](<../../../jama_bot_2019_oi_190007.pdf#page=4>); [DOC-001 Adherence to Interventions, PDF p. 6](<../../../jama_bot_2019_oi_190007.pdf#page=6>); [DOC-004 eAppendix 8, PDF p. 16](<../../../joi190007supp3_prod.pdf#page=16>).
- **Direct observation:** DOC-001 p. 4 defines good adherence as taking **>=70%** of supplements during 12 months. DOC-004 p. 16 labels pill-weight and self-report multinutrient/omega adherence **>=70%**. DOC-001 p. 6 says 77% had adherence of **more than 70%** to supplements or placebo.
- **Rule and calculation:** “>=70%” includes exactly 70%; “more than 70%” excludes exactly 70%. These are non-identical threshold definitions. The 77% is a rounded summary and the printed sources do not give the number with exactly 70% adherence, so its numerical impact cannot be calculated from supplied evidence.
- **Observation versus inference:** The threshold wordings are directly printed. Any claim that the same participants were or were not counted at the boundary would be an inference unsupported by the displayed data.
- **Alternative source-grounded interpretation:** “More than 70%” may be informal prose for the predefined/table criterion >=70%, and no displayed count or conclusion is demonstrably altered.
- **Human question:** Which boundary rule generated the 77% summary, and were participants with exactly 70% adherence included in its numerator?

### NC-03 — Main-article sample-size total conflicts with its stated four per-cell counts

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-001 Sample Size, PDF p. 4](<../../../jama_bot_2019_oi_190007.pdf#page=4>).
- **Direct observation:** The direct PDF prints: “392 participants (196 in each of the 4 possible intervention combinations) were needed.” It then states that, allowing 22% attrition, 250 participants per intervention combination were needed.
- **Rule and calculation:** Four combinations with 196 participants each require 4 x 196 = 784 participants, not 392. In contrast, four x 250 = 1000, which is internally consistent with the later per-combination statement.
- **Observation versus inference:** The total 392 and parenthetical four cells of 196 are directly printed. The incompatibility is arithmetic. Inferring which of the total or per-cell number was intended is not supported by this page alone.
- **Alternative source-grounded interpretation:** The 392 may refer to a two-level main-effect comparison (196 per level), whereas 196 per *combination* would describe four cells. The sentence does not state that distinction.
- **Human question:** Was 392 intended as the sample size for each factorial main-effect contrast, or is either “392” or “196 in each of the 4” a publication error?

### NC-04 — Protocol sample-size text labels a 30% versus 15% contrast as a 25% difference

- **Primary category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-002 Sample size calculation, PDF p. 16](<../../../joi190007supp1_prod.pdf#page=16>).
- **Direct observation:** The direct PDF states it is powered to detect a “difference of 25%” in 12-month cumulative incidence, then gives expected incidence of 30% in control and 15% in intervention.
- **Rule and calculation:** 30% - 15% = 15 percentage points. Relative to 30%, the reduction is 15/30 = 50%. Neither usual calculation equals 25%.
- **Observation versus inference:** The sentence and two incidences are printed. The arithmetic discrepancy follows directly. The intended meaning of “25%” is not supplied.
- **Alternative source-grounded interpretation:** “25%” may be a typographical carryover or may refer to an unstated parameter other than the displayed two incidences; the page does not identify one.
- **Human question:** What quantity did the protocol intend “difference of 25%” to denote, and what inputs underlay the documented sample-size calculation?

### NC-05 — Main article and protocol report different sample-size event-rate and attrition inputs

- **Primary category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001 Sample Size, PDF p. 4](<../../../jama_bot_2019_oi_190007.pdf#page=4>); [DOC-002 Sample size calculation, PDF p. 16](<../../../joi190007supp1_prod.pdf#page=16>).
- **Direct observation:** DOC-001 gives 30% control versus 20% active onset, 33% reduction, 196 in each stated combination, and 22% attrition. DOC-002 gives 30% control versus 15% intervention incidence, 180 per group, and 20% dropout, inflated to 250 per arm.
- **Rule and comparison:** These are matched sample-size inputs for the same one-year factorial prevention trial, but the stated active incidence, per-cell figure, and attrition assumption differ. The documents do not state on the compared pages whether a formal amendment reconciles the changes.
- **Observation versus inference:** The different printed inputs are direct observations. Treating them as an unresolved reporting inconsistency rather than a documented amendment is an inference limited by the supplied pages.
- **Alternative source-grounded interpretation:** DOC-002 is version 7 dated July 2017 and might represent a protocol amendment or a different planning stage; DOC-001 says “at the time the trial was designed.” The package does not provide a revision explanation at these locations.
- **Human question:** Which sample-size assumptions were operative for the final trial, and is there a dated amendment or analysis record that explains the differences?

### NC-06 — Protocol gives two different DSM editions for the primary MDD endpoint

- **Primary category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 Main study parameters/endpoints, PDF p. 8](<../../../joi190007supp1_prod.pdf#page=8>); [DOC-002 Methods 8.1.1, PDF p. 28](<../../../joi190007supp1_prod.pdf#page=28>).
- **Direct observation:** On p. 8 the 12-month MDD endpoint is defined according to DSM-IV criteria using MINI. On p. 28 the same 12-month endpoint is defined according to DSM-5 criteria using MINI V5.01; both specify baseline and 3/6/12-month assessment.
- **Rule and comparison:** The same endpoint/time schedule should identify one diagnostic standard unless a version transition or distinct operational definition is explained. DSM-IV and DSM-5 are not the same label.
- **Observation versus inference:** The edition labels are directly printed. The possibility of a protocol revision or instrument-specific explanation is not resolved by these pages.
- **Alternative source-grounded interpretation:** The p. 8 summary may be an unrevised section while p. 28 records the operative method, or the inconsistent labels may not have changed the applied MINI assessment.
- **Human question:** Which diagnostic edition governed the primary-outcome MINI assessment, and was the other label intentionally retained from an earlier protocol version?

## Completion

All 95 assigned N relationships were checked. Six distinct candidate consistency issues are emitted above; none has a stable candidate ID or an adjudication judgment.
