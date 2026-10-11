# Supplement Numeric Candidate Cards

Runtime: 01a1288b-7ea4-7e11-a311-a35c8ef28abd. Fresh numeric shard; no stable candidate IDs, adjudications, or dispositions assigned. Each observation awaits human adjudication. Exact source pages are authority. Mapper transcription and reusable renders are locating aids.

## SUPPORT-NUM-001: Two eTable 2 columns carry the same intervention label

Compared locations: REPORT DOC004 eTable2 PDF p3 arm headings and REPORT DOC004 eTable2 continuation PDF p5 headings. Links: [p3](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=3), [p5](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=5).
Printed inputs: p3 Intervention group N=3,272; Intervention group N=3,311; between-group difference. P5 Intervention group N=3,272; Control group N=3,311.
Rule/calculation: the repeated table must preserve randomized arm identities. The 3,311 column changes its printed identity from Intervention to Control while its population and contrast position persist. Identity comparison has zero rounding tolerance. Direct observation is the contradictory heading; interpreting the second column as control is an inference supported by continuation headings. An alternative is an intentionally different population, but no such change is announced. Relevance: arm misassignment can reverse extraction of contrasts. Human question: Which arm should the N=3,311 column in the first eTable2 panel identify?

## SUPPORT-NUM-002: Red-wine median exceeds its upper quartile

Compared locations: REPORT DOC004 eTable2 p7 red-wine intervention baseline cell and its median(IQR) row/footnote definition. [Source p7](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=7).
Printed inputs: red wine g/week, intervention baseline median(IQR) 33 (0,29), control 4 (0,29).
Rule/calculation: Q1 <= median <= Q3; 33-29=4 g/week. Even allowing independent nearest-integer rounding ±0.5, minimum excess is 3 g/week. Direct observation: the central value is outside its reported quartile interval. No distribution/model inference is needed. Alternatives: central statistic may be mislabeled, a digit may be transcribed, or a quartile may be wrong; the package does not identify which. Relevance: impossible median summary may propagate into distribution extraction. Human question: Which value or summary label is intended for intervention red-wine baseline 33 (0,29)?

## SUPPORT-NUM-003: Olive-oil baseline label conflicts with its summary format and table footnote

Compared locations: REPORT DOC004 eTable4 p10 Total olive oil baseline row and REPORT DOC004 eTable4 p11 footnote. [p10](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=10), [p11](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=11).
Printed inputs: Baseline, mean(SD), both groups 350 (175,350); footnote Baseline data are median(IQR).
Rule: one SD accompanies a mean, whereas the printed parentheses supply two endpoints and the footnote specifies quartiles. The row and footnote conflict exactly; rounding is irrelevant. Direct observation: incompatible statistic labels and three-number formatting. Inferring that median(IQR) was intended is supported by neighboring rows but is not a correction. Alternative: row may intentionally differ, in which case its two parenthetical numbers need definition. Relevance: extracting an SD from two quartiles yields incompatible evidence. Human question: Does olive-oil baseline report mean(SD), median(IQR), or another explicitly defined summary?

## SUPPORT-NUM-004: The contents list inserts 245 into an all-randomized participant label

Compared locations: REPORT DOC004 p1 eTable9 contents entry and REPORT DOC004 eTable9 p23 MI column population. [p1](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=1), [p23](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=23).
Printed inputs: p1 'all randomized 245 participants'; p23 all randomized participants, intervention n=3,272 and control n=3,311.
Rule/calculation: matched population counts total 3,272+3,311=6,583, which differs from the inserted 245 by 6,338. Count tolerance zero. Direct current-source Poppler render numeric_support_doc004_p001.png confirms245 visibly printed inline, rather than an extraction-only artifact. Direct observation: 245 occurs inside the participant phrase; interpreting it as a cohort count is conditional. Strong alternative: a stray manuscript line number rather than an intended sample size. The observation is a quantitative label ambiguity, not a claim that 245 is the analytic denominator. Relevance: contents labels may enter automated extraction. Human question: Is 245 an unintended line-number insertion, and what participant count or label should this contents entry convey?

## SUPPORT-NUM-005: Waist-to-height ratio scaling is unmarked

Compared locations: PLAN DOC003 p14 Table2 waist-to-height ratio row versus the same table's waist(cm) row and p17 dimensional-trait definition. [p14](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=14), [p17](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=17).
Printed inputs: waist-to-height ratio 66.2(6.5),66.4(5.5); mean waist109.9cm,110.4cm; ratio row has no percent or x100 label.
Rule/calculation: waist/height with matching length units is dimensionless; a percent-scaled ratio requires x100 labeling. A diagnostic division109.9/66.2=1.6601cm versus109.9/.662=166.01cm illustrates the100-fold scale ambiguity, but ratio of means is not the mean of individual ratios and is not treated as an exact height estimate. No rounding explains the scale factor100. Direct observation: the printed values and missing scaling label. The inference is that percent scaling was intended; underlying heights and ratio convention are absent. Alternative: mixed length units or an intended percent convention. Relevance: extracted ratios differ100-fold without the missing convention. Human question: Are the printed ratios66.2/66.4 percentages (100 times waist/height), or which explicit scale defines them?

## SUPPORT-NUM-006: Diabetes upper-bound statement versus displayed screening percentage

Compared locations: PLAN DOC003 p15 lines356-357 and PLAN DOC003 p14 randomized self-reported diabetes row. [p14](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=14), [p15](../../../../joi190106supp2_prod_1635377898.49605.pdf#page=15).
Printed inputs: randomized diabetes27.2%; 'diabetic participants do not exceed27% of the total cohort'.
Rule/calculation: if27% is a strict upper bound for the same randomized cohort,27.2>27 by0.2 percentage points; the one-decimal input interval[27.15,27.25) remains above27. Direct observation: strict-looking upper-bound wording alongside a larger displayed percentage. Alternative: the narrative rounds the cohort prevalence to a whole percent, in which case27.2 rounds to27 and there is no numerical conflict, or diabetes definitions/cohorts differ. Do not infer a recruitment violation. Relevance: distinguishing a reported prevalence from an eligibility cap affects denominator interpretation. Human question: Is27% a rounded descriptive prevalence or an exact cohort limit, and does it refer to the Table2 self-reported-diabetes population?

## SUPPORT-NUM-007: Same baseline red-wine summaries differ under missing-follow-up replacement

Compared locations: REPORT DOC004 eTable2 p7 MI baseline and REPORT DOC004 eTable7 p19 baseline-replacement baseline. [p7](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=7), [p19](../../../../joi190106supp3_prod_1635377898.49725.pdf#page=19).
Printed inputs: both population headers I3,272/C3,311; eTable2 redwine baseline I33(0,29),C4(0,29); eTable7 baseline I0(0,29),C0(0,29). ETable7 title replaces missing values with baseline value.
Rule/calculation: changing how missing follow-up values are supplied should leave an identically defined, observed baseline unchanged. Printed differences33 and4g/week exceed integer-rounding tolerance1g/week. Direct observation: same endpoint/unit/arm/header/baseline displays different central summaries. Alignment is conditional because baseline missingness, imputation of baseline, and exact baseline denominator are not supplied. Alternative: baseline imputation or different baseline availability could change the central summaries despite identical allocation headers. This differs from SUPPORT-NUM-002's within-cell ordering rule. Relevance: baseline comparisons can be copied as differing analytic cohorts. Human question: Were baseline values or baseline populations also changed/imputed, and which explains redwine baseline33/4 versus0/0?
