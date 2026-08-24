# Cross-Source Consistency Check

## Completed scope and method

This check covered all 53 numeric/reporting relationships in `relationships/numeric_relationship_inventory.md` and all 35 inferential relationships in `statistics/relationship_inventory.md` (88 mapped relationships total), across DOC-001 main article, DOC-002 protocol, DOC-003 supplement, and DOC-004 data-sharing statement. Canonical maps and native/layout text were used as locators. Each proposition below was confirmed against the printed supplied PDF page; direct PDFs, rather than a derivative, are the authority.

For a cross-location comparison, the population, time basis, contrast, model or analysis condition, measure/scale/unit, reference group, and displayed precision were matched first. Planned protocol quantities, sensitivity analyses, descriptive unadjusted values, and competing-risk estimates were not treated as alternative prints of the main intention-to-treat result.

## Candidate propositions requiring human adjudication

### Vitamin-D concentration unit in the main-results narrative

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 main article — PDF p. 6](<../../../jama_okereke_2020_oi_200066.pdf#page=6>), Results, “Baseline Characteristics”; [DOC-001 main article — PDF p. 4](<../../../jama_okereke_2020_oi_200066.pdf#page=4>), Table 1 footnote; [DOC-001 main article — PDF p. 8](<../../../jama_okereke_2020_oi_200066.pdf#page=8>), Figure 4; [DOC-003 Supplement 2 — PDF pp. 38-40](<../../../joi200066supp2_prod.pdf#page=38>), eTable 14 and narrative.
- **Printed comparators:** DOC-001 p. 6 states: “The mean 25-hydroxyvitamin D level was 31.1 ng/mL and 11.6% of participants had levels lower than 20 mg/mL.” Table 1 labels the same analyte as “25-hydroxyvitamin D” with categories “<20” and “≥20 ng/mL,” and says to multiply ng/mL by 2.5 for nmol/L. Figure 4 labels the baseline subgroup in ng/mL. DOC-003 eTable 14 also defines low vitamin D as “<20 ng/mL.”
- **Comparison logic:** This is the same analyte and threshold, in the randomized baseline cohort, not a conversion or a different analysis set. The direct comparison rule is identity of the unit attached to the 20-threshold: the repeated table, figure, and supplement definitions use ng/mL, whereas the narrative occurrence prints mg/mL. The printed 31.1 value immediately preceding the threshold is also in ng/mL.
- **Supported alternatives:** The isolated `mg/mL` could be a unit-label transcription error. A different laboratory unit is not supported by the supplied source because no conversion or alternative threshold is stated, and all matched threshold definitions use ng/mL.
- **Human verification steps:** Open the four cited PDF locations; verify the letters in the p. 6 unit and the threshold unit in Table 1/Figure 4/eTable 14; check the production source or author query record, if available, for the intended unit. Preserve the reported percentage unless its denominator or source definition is independently changed.

### Incorrect protocol table locator for ICD-9 depression codes

- **Category:** Measure, label, or scale inconsistency (cross-location reference-label inconsistency).
- **Exact source locations:** [DOC-002 protocol — PDF p. 18](<../../../joi200066supp1_prod.pdf#page=18>), ICD-9-code paragraph and immediately following table; [DOC-002 protocol — PDF p. 23](<../../../joi200066supp1_prod.pdf#page=23>), displayed Table 3.
- **Printed comparators:** On DOC-002 p. 18, the paragraph says, “ICD-9 codes will be used to identify depression (Table 3)”; the immediately following displayed caption is “Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders.” DOC-002 p. 23 contains the separately numbered “Table 3,” a recurrent-depression power table.
- **Comparison logic:** The referring sentence and immediately adjacent table concern the same ICD-9-code list. The cited number must identify that list. Table 3 is a different quantitative object (power by expected risk ratio) and does not display ICD-9 codes.
- **Supported alternatives:** The internal locator may be a numbering carryover from an earlier protocol draft, or the adjacent caption could have been renumbered without updating prose. The supplied PDF does not establish which text was intended to change.
- **Human verification steps:** Inspect p. 18 and p. 23 in the supplied protocol; verify whether there is any intervening or appendixed ICD-9 table numbered Table 3 in the authoritative protocol version; compare the version-control or typesetting source, if available, before selecting a correction.

### Supplementary narrative names the wrong main-article figure for depression-risk subgroup results

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-003 Supplement 2 — PDF p. 13](<../../../joi200066supp2_prod.pdf#page=13>), “Description of Results from Sub-Group Analyses in Figure 3 and eTable 2”; [DOC-001 main article — PDF p. 8](<../../../jama_okereke_2020_oi_200066.pdf#page=8>), Figure 4; [DOC-001 main article — PDF p. 7](<../../../jama_okereke_2020_oi_200066.pdf#page=7>), Figure 3.
- **Printed comparators:** DOC-003 p. 13 says that no treatment-by-subgroup interactions occurred “(main Figure 3)” and reports depression-risk subgroup values including women `p-interaction=0.10`, normal versus higher BMI `p-interaction=0.06`, baseline vitamin-D use `HR=0.87 (95% CI: 0.73-1.04)`, and 25(OH)D `≥20 ng/ml HR=0.89 (95% CI: 0.77-1.04)`. DOC-001 Figure 4 prints those depression-risk subgroup values. DOC-001 Figure 3 displays crude PHQ-8 score distributions and does not print those hazard ratios or interaction P values.
- **Comparison logic:** The treatment contrast, outcome (depression risk), subgroup definitions, effect measure (hazard ratio), and displayed precision of the four quoted values match Figure 4 exactly. They do not match the PHQ-8 distribution graphic in Figure 3. Therefore, the numerical narrative has an internally mismatched main-figure locator.
- **Supported alternatives:** “Figure 3” may be a supplement-to-main cross-reference error; the supplement heading may have retained a prior main-figure number. The supplied evidence does not show an alternative main-article figure containing the quoted depression-risk results.
- **Human verification steps:** Open DOC-003 p. 13 and DOC-001 pp. 7-8; verify the quoted values and figure captions; inspect the accepted-manuscript or production cross-reference fields, if available, to determine whether the narrative parenthetical, heading, or figure numbering was intended to differ.

## Checked matched-result families with no qualifying difference

The following comparisons were checked and reconciled at printed precision after the required identity matching. “No qualifying difference” does not mean that unlike analyses were forced to agree.

| Matched family | Compared direct locations | Matching and reconciliation |
|---|---|---|
| Randomized population, allocation, and follow-up | DOC-001 pp. 1, 3, 6, 9; DOC-003 pp. 3-8, 36-37 | Same randomized VITAL-DEP cohort: total 18,353; vitamin D3/placebo 9,181/9,172; median follow-up 5.3 years. Supplement eTable 13 retains the group denominators. |
| Primary total-depression counts, rates, HR, and P | DOC-001 pp. 1, 6, 8; DOC-003 pp. 25-26, 36-37 | Same intention-to-treat total-depression outcome and vitamin-D3-versus-placebo contrast: 609/9,181 and 625/9,172; 12.9 and 13.3 per 1,000 person-years in the main article; HR 0.97 (0.87-1.09), P=.62. eTable 13 gives 12.95 and 13.29, which are compatible with one-decimal display rounding; it does not relabel cases as rates or supply a competing effect estimate. Fine-Gray P=.60 is a different competing-risk model, not a comparator for the primary Cox P=.62. |
| Incident and recurrent counts, denominators, rates, HRs, and Ps | DOC-001 pp. 5, 6, 8; DOC-003 pp. 26, 36-37 | Same risk sets and endpoint partitions: 8,350+831=9,181, 8,307+865=9,172; 459+150=609 and 461+164=625. Main rounded rates 10.7/10.8 and 37.6/39.3 agree with supplement 10.66/10.76 and 37.58/39.32. Main Cox HRs/Ps are 0.99 (0.87-1.13), .88 and 0.95 (0.76-1.19), .67. |
| Main Figure 4 subgroup depression-risk results and supplement narrative | DOC-001 p. 8; DOC-003 p. 13 | Values for women, BMI, baseline vitamin-D use, and baseline 25(OH)D agree exactly; the figure-reference discrepancy is recorded separately above. Other Figure 4 subgroup values have no separate matched external numerical print. |
| Baseline Table 1 values and Supplement 2 eTable 1 | DOC-001 p. 4; DOC-003 pp. 3-8 | Same randomized groups and available-data denominators. Shared age, sex, race, BMI, Charlson, supplemental-vitamin-D, physical-activity, geographic-region, factorial-allocation, and 25(OH)D entries agree at shown precision. Available-data denominators and rounding footnotes explain why categories are not all divided by the randomized N. |
| Overall and annual adjusted PHQ-8 changes | DOC-001 pp. 1, 6; DOC-003 pp. 27-32 | The main primary response-profile result, overall vitamin-D3-minus-placebo difference 0.01 (-0.04 to 0.05), is matched only to the same primary all-responses analysis. Supplement eTable 9 uses negative-binomial rate ratios, and eTables 10-11 apply censoring or omit year 5; their different estimates are not conflicts. |
| Raw PHQ-8 distributions versus adjusted estimates | DOC-001 pp. 6-7; DOC-003 p. 41 | Supplement eTable 15 prints unadjusted means (SD), while main Table 2 prints adjusted response-profile means/changes with CIs. Different summary/model and time contrast preclude direct equality; no mislabeled scale was found. |
| PHQ-8 subgroup results | DOC-001 pp. 6-8; DOC-003 pp. 9-13 | Main Figure 4 is depression risk; supplement eTable 2 is adjusted PHQ-8 mean-change. They concern different outcomes and effects; the supplement correctly labels its mean-difference scale and interaction tests. |
| Adherence statement | DOC-001 p. 6; DOC-003 p. 16 | Main “90% or greater ... at all assessments” matches questionnaire-respondent proportions of 90.6-100.0% (vitamin D3) and 89.8-100.0% (placebo) only as a rounded narrative generalization. Because placebo year 5 is printed 89.8%, the statement cannot be treated as an exact equality claim without knowing its unrounded percentage. No candidate is proposed on this basis. |
| Sensitivity-analysis depression effects | DOC-001 p. 6; DOC-003 pp. 14-25, 28-32 | Main states sensitivities were consistent. Supplement results differ by explicitly stated censoring, covariate, competing-risk, or time restriction. They are not printed as the main primary Cox or primary PHQ-8 estimate, so no cross-result conflict was called. |
| Baseline vitamin-D threshold definition | DOC-001 pp. 4, 8-9; DOC-002 pp. 21-22; DOC-003 pp. 3-8, 38-40 | `<20 ng/mL` agrees with `<50 nmol/L` under the explicitly printed ×2.5 conversion. The one `mg/mL` occurrence is the separate candidate proposition. Different means (31.1 narrative, 31.2/31.1 by group, and 30.8 limitation) have different aggregation/available-sample descriptions and were not equated. |
| Protocol treatment dose, factorial design, and endpoint/method definitions | DOC-002 pp. 1-24; DOC-001 pp. 2-5; DOC-003 pp. 17-26, 43-47 | Vitamin D3 2,000 IU/day and factorial structure agree. The protocol's planned N=20,000, anticipated eligibility N=18,200, 5-year schedule, planned assessments, alpha/power, and planned RR tables are prospective assumptions, not achieved result comparators. Later revised trial targets and six annual PHQ assessments are documented context rather than cross-document numeric conflicts. |
| CTSC/concordance quantities | DOC-001 p. 3; DOC-002 pp. 14, 16, 21-24; DOC-003 pp. 46-47 | Planned CTSC N=1,000, main CTSC validation subset N=1,054, and concordance N=1,053 apply to distinct planning, enrolled, and paired-assessment sets. No source represents them as one identical analysis denominator. |
| Rate/count terminology | DOC-001 pp. 1, 5-6, 8; DOC-003 pp. 33-37 | Counts, participant denominators, and case rates per 1,000 person-years are separately headed/defined. Rates were not recomputed as proportions because person-time denominators are not printed. |
| Supplement-only tables, eFigure, and data-sharing statement | DOC-003 pp. 14-48; DOC-004 pp. 1-2 | Censoring tables, CVD/cancer variants, PHQ-8 rate-ratio and item-level likelihood-ratio results, biomarker associations, CTSC agreement, eMethods quantities, references, and data-sharing date lack a second same-result print outside their stated analysis. No cross-document candidate can be inferred from absence of a comparator. |

## Limitations

No raw data, person-time denominators, production files, amendment history, or author query record was supplied. The review therefore verifies printed agreement and labels, not the underlying calculations. Protocol and supplement content with a different planned population, sensitivity condition, model, outcome, or time basis was documented as non-comparable rather than treated as a discrepancy. The supplied package contains no structured dataset or workbook.

## Compact completion record

- **Mapped relationships reviewed:** 88 (53 numeric/reporting and 35 inferential-statistical).
- **Matched cross-location result or definition families checked:** 15.
- **Qualifying candidate propositions:** 3.
- **Non-candidate reconciliations recorded:** 15 families.
- **Display-zero P-only propositions:** 0.
- **Artifact path:** `.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md`.
