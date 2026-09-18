# jama.2025.9110

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.9110 |
| Candidates | 6 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.9110/)

## Review setup

Edit the Markdown source. Empty cells mean unanswered. AI suggestions are reference only. All statuses and counts below are maintained manually.

| Field | Value |
| --- | --- |
| Stage | primary |
| Primary reviewer ID |  |
| Primary reviewer name |  |
| Checker ID |  |
| Checker name |  |
| Primary completed on |  |
| Primary backup or revision reference |  |
| Checker completed on |  |
| Paper status | not\_started |

Use `primary` or `checker` for Stage. Use `not_started`, `in_progress`, `primary_ready`, or `final_ready` for Paper status. Follow the [handoff instructions](../USAGE.md#handoff) before starting checking.

## Paper results

Leave final counts blank until every candidate is final. Zero means reviewed and none found. These are candidate counts, not independently deduplicated issue counts.

| Outcome | Final candidate count |
| --- | --- |
| primary\_temporal |  |
| secondary\_temporal |  |
| protocol\_descriptive |  |
| plan\_descriptive |  |
| not\_eligible |  |
| total\_final |  |

## Candidate index

- [C001](#candidate-c001) — Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints (S_W)
- [C002](#candidate-c002) — eTable 10 uses a comma in one one-decimal survival percentage (S_W)
- [C003](#candidate-c003) — Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays (S_W)
- [C004](#candidate-c004) — Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR) (S_W)
- [C005](#candidate-c005) — eTable 10 tracheostomy row switches percent-sign notation across period cells (S_W)
- [C006](#candidate-c006) — eTable 10 new-KRT row switches percent-sign notation across period cells (S_W)

## Candidate C001

**Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.9110::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 7, Table 2, Duration of invasive ventilation, mean (SD), h; main article — PDF p. 1; Results Supplement — PDF p. 18, eTable 10.

### Candidate statement

> The invasive-ventilation Table 2 row is labeled mean (SD) but each group display contains two endpoints.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The printed \`mean (SD)\` label is compared with the two-endpoint parenthetical displays and the supplementary median (IQR) presentation convention.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> Table 2 prints augmented protein 84.0 (35.0 to 178.9) and usual protein 78.0 (33.2 to 161.0), while the row label says mean (SD). It separately prints Mean difference, 6.8 (−3.0 to 16.5) hours. eTable 10 describes comparable central-value/two-bound summaries as median (IQR).

#### Evidence 1: Reported-versus-comparator

> The printed mean (SD) label is compared with the two-endpoint parenthetical displays and the supplementary median (IQR) presentation convention.

#### Evidence 2: Calculation

> 35.0 \< 178.9 and 33.2 \< 161.0; each parenthesis has two ordered endpoints, not one SD. No rounding rule applies.

#### Evidence 3: Alternative source-grounded interpretations

> to or an endpoint may be a production error in an intended mean/SD display; alternatively the label may be wrong and the values may be a median-plus-interval summary. The supplied package does not define the endpoints.

### Source links

- sourceLinks 0: [Main article — PDF p. 7](../../../2025/jama.2025.9110/jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7)
- sourceLinks 1: [main article — PDF p. 1](../../../2025/jama.2025.9110/jama_summers_2025_oi_250040_1753124024.36498.pdf#page=1)
- sourceLinks 2: [Results Supplement — PDF p. 18](../../../2025/jama.2025.9110/joi250040supp3_prod_1753124024.38098.pdf#page=18)

[Original Markdown report](../../../2025/jama.2025.9110/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Main label versus own two-endpoint displays; supplement is comparable convention, not identically matched discrepancy. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2025::jama.2025.9110::C001 |
| legacyRelationship |  |
| locations | Main article — PDF p. 7, Table 2, Duration of invasive ventilation, mean (SD), h; main article — PDF p. 1; Results Supplement — PDF p. 18, eTable 10. |
| originalCrossDocument | 0 |
| package | jama.2025.9110 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The printed \`mean (SD)\` label is compared with the two-endpoint parenthetical displays and the supplementary median (IQR) presentation convention. |
| reportHref | ../../2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The invasive-ventilation Table 2 row is labeled mean (SD) but each group display contains two endpoints. |
| submissionInvolved | 1 |
| subtype | Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints |
| suggestedDomain | report\_internal\_inconsistency |
| title | Invasive-ventilation descriptive summary is labeled mean (SD) but displays two endpoints |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**eTable 10 uses a comma in one one-decimal survival percentage**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.9110::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Results Supplement — PDF p. 18, eTable 10, Alive at day 90 \[n (%)\], Period 2 usual protein (4 units, n = 530).

### Candidate statement

> One eTable 10 day-90 survival percentage uses a comma-and-space where matched cells use a decimal point.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. \`72, 3%\` is compared with the row's point-decimal convention and its printed count/denominator.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The cell prints 383 (72, 3%); neighboring matched cells include 323 (67.3%), 258 (77.0%), 229 (76.8%), and 408 (74.0%).

#### Evidence 1: Reported-versus-comparator

> 72, 3% is compared with the row's point-decimal convention and its printed count/denominator.

#### Evidence 2: Calculation

> 383 / 530 × 100 = 72.2641509…%, which rounds to 72.3% at one decimal (rounding interval 72.25% to \<72.35%). The question is punctuation, not a numerator/denominator mismatch.

#### Evidence 3: Alternative source-grounded interpretations

> A comma can be a decimal separator in some locales and preserve the intended numeric value, but its isolated use in this point-decimal table remains a rendering inconsistency.

### Source links

- sourceLinks 0: [Results Supplement — PDF p. 18](../../../2025/jama.2025.9110/joi250040supp3_prod_1753124024.38098.pdf#page=18)

[Original Markdown report](../../../2025/jama.2025.9110/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2025::jama.2025.9110::C002 |
| legacyRelationship |  |
| locations | Results Supplement — PDF p. 18, eTable 10, Alive at day 90 \[n (%)\], Period 2 usual protein (4 units, n = 530). |
| originalCrossDocument | 0 |
| package | jama.2025.9110 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. \`72, 3%\` is compared with the row's point-decimal convention and its printed count/denominator. |
| reportHref | ../../2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | One eTable 10 day-90 survival percentage uses a comma-and-space where matched cells use a decimal point. |
| submissionInvolved | 1 |
| subtype | eTable 10 uses a comma in one one-decimal survival percentage |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 10 uses a comma in one one-decimal survival percentage |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.9110::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 7, Table 2; Results Supplement — PDF p. 5, secondary analyses; Results Supplement — PDF p. 27, eFigure 6.

### Candidate statement

> The Bayesian quantile Table 2 row is labeled mean (SD) despite a median-difference estimand and two-endpoint group displays.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The Table 2 \`mean (SD)\` group-summary label is compared with its own median-difference effect label, the final Bayesian method description, and the two-bound group displays.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The row prints 62.0 (0 to 77) versus 64.0 (0 to 77) under mean (SD) and reports Median difference, −1.50 (−3.86 to 0.90). The supplement defines the Bayesian quantile coefficient as a difference in medians and repeats the median difference with a 95% credible interval.

#### Evidence 1: Reported-versus-comparator

> The Table 2 mean (SD) group-summary label is compared with its own median-difference effect label, the final Bayesian method description, and the two-bound group displays.

#### Evidence 2: Calculation

> 0 \< 77 in each group parenthesis, so each contains two bounds rather than one SD. The printed estimand is Median difference; no supplied text explains an intentional separate mean/SD convention.

#### Evidence 3: Alternative source-grounded interpretations

> The label may have carried over from the preceding linear-model row. Separately calculated means/SDs might have been intended alongside a median estimand, but the source neither defines that convention nor explains the two endpoints.

### Source links

- sourceLinks 0: [Main article — PDF p. 7](../../../2025/jama.2025.9110/jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7)
- sourceLinks 1: [Results Supplement — PDF p. 5](../../../2025/jama.2025.9110/joi250040supp3_prod_1753124024.38098.pdf#page=5)
- sourceLinks 2: [Results Supplement — PDF p. 27](../../../2025/jama.2025.9110/joi250040supp3_prod_1753124024.38098.pdf#page=27)

[Original Markdown report](../../../2025/jama.2025.9110/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Main label versus own two endpoints and median-difference effect. Final supplementary methods corroborate median estimand. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2025::jama.2025.9110::C003 |
| legacyRelationship |  |
| locations | Main article — PDF p. 7, Table 2; Results Supplement — PDF p. 5, secondary analyses; Results Supplement — PDF p. 27, eFigure 6. |
| originalCrossDocument | 0 |
| package | jama.2025.9110 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The Table 2 \`mean (SD)\` group-summary label is compared with its own median-difference effect label, the final Bayesian method description, and the two-bound group displays. |
| reportHref | ../../2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The Bayesian quantile Table 2 row is labeled mean (SD) despite a median-difference estimand and two-endpoint group displays. |
| submissionInvolved | 1 |
| subtype | Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays |
| suggestedDomain | report\_internal\_inconsistency |
| title | Bayesian quantile row is labeled mean (SD) despite its associated median estimand and two-endpoint group displays |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR)**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.9110::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article Results — PDF p. 5, Biochemical Outcomes; main article Discussion — PDF p. 8.

### Candidate statement

> The Discussion calls the matched day-10 blood-urea summaries means while Results reports medians (IQR).

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The Discussion's \`mean\` label is compared with the Results' matched analyte, day, groups, direction, unit, and \`median (IQR)\` description.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> Results calls day-10 blood-urea values median (IQR): augmented protein 13.0 (8.2–18.8) versus usual protein 10.6 (7.1–15.4) mmol/L. Discussion says that mean urea concentrations at day 10 were higher in the augmented protein group.

#### Evidence 1: Reported-versus-comparator

> The Discussion's mean label is compared with the Results' matched analyte, day, groups, direction, unit, and median (IQR) description.

#### Evidence 2: Calculation

> No calculation is appropriate: mean and median are distinct summary-statistic labels, and no matched day-10 mean values are supplied.

#### Evidence 3: Alternative source-grounded interpretations

> Mean may be nontechnical prose, a copy-editing substitution, or a reference to unprinted group means. The supplied package does not report a distinct matched mean analysis.

### Source links

- sourceLinks 0: [Main article Results — PDF p. 5](../../../2025/jama.2025.9110/jama_summers_2025_oi_250040_1753124024.36498.pdf#page=5)
- sourceLinks 1: [main article Discussion — PDF p. 8](../../../2025/jama.2025.9110/jama_summers_2025_oi_250040_1753124024.36498.pdf#page=8)

[Original Markdown report](../../../2025/jama.2025.9110/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2025::jama.2025.9110::C004 |
| legacyRelationship |  |
| locations | Main article Results — PDF p. 5, Biochemical Outcomes; main article Discussion — PDF p. 8. |
| originalCrossDocument | 1 |
| package | jama.2025.9110 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The Discussion's \`mean\` label is compared with the Results' matched analyte, day, groups, direction, unit, and \`median (IQR)\` description. |
| reportHref | ../../2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The Discussion calls the matched day-10 blood-urea summaries means while Results reports medians (IQR). |
| submissionInvolved | 1 |
| subtype | Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR) |
| suggestedDomain | report\_internal\_inconsistency |
| title | Discussion describes the matched day-10 urea summaries as means while Results reports medians (IQR) |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C005

**eTable 10 tracheostomy row switches percent-sign notation across period cells**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.9110::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Results Supplement — PDF p. 18, eTable 10, Tracheostomy in ICU \[n (%)\].

### Candidate statement

> The eTable 10 tracheostomy row changes percent-sign notation halfway across matched period cells.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. All eight are percentage displays in one \`\[n (%)\]\` row, but the first four omit \`%\` and the last four include it.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The first four cells print 27 (5.6), 36 (10.7), 29 (9.7), and 24 (4.5) without %; the last four print 35 (6.4%), 38 (10.3%), 43 (12.2%), and 23 (4.8%) with %.

#### Evidence 1: Reported-versus-comparator

> All eight are percentage displays in one \[n (%)\] row, but the first four omit % and the last four include it.

#### Evidence 2: Calculation

> 27/480×100=5.625%→5.6%; 36/335×100=10.746…%→10.7%; 29/298×100=9.732…%→9.7%; 24/530×100=4.528…%→4.5%. These reconcile at one decimal (0.05 percentage-point rounding tolerance); the issue is notation, not arithmetic.

#### Evidence 3: Alternative source-grounded interpretations

> The \[n (%)\] header makes the unsigned entries understandable, but it does not explain the within-row switch to explicit signs. Intended typography is not stated.

### Source links

- sourceLinks 0: [Results Supplement — PDF p. 18](../../../2025/jama.2025.9110/joi250040supp3_prod_1753124024.38098.pdf#page=18)

[Original Markdown report](../../../2025/jama.2025.9110/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2025::jama.2025.9110::C005 |
| legacyRelationship |  |
| locations | Results Supplement — PDF p. 18, eTable 10, Tracheostomy in ICU \[n (%)\]. |
| originalCrossDocument | 0 |
| package | jama.2025.9110 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. All eight are percentage displays in one \`\[n (%)\]\` row, but the first four omit \`%\` and the last four include it. |
| reportHref | ../../2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable 10 tracheostomy row changes percent-sign notation halfway across matched period cells. |
| submissionInvolved | 1 |
| subtype | eTable 10 tracheostomy row switches percent-sign notation across period cells |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 10 tracheostomy row switches percent-sign notation across period cells |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**eTable 10 new-KRT row switches percent-sign notation across period cells**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.9110::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Results Supplement — PDF p. 18, eTable 10, New kidney replacement therapy commenced during index ICU admission after commencing trial enteral nutrition \[n (%)\].

### Candidate statement

> The eTable 10 new-kidney-replacement-therapy row changes percent-sign notation halfway across matched period cells.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. All eight are percentage displays within one \`\[n (%)\]\` row, but \`%\` is absent from the first four and present in the final four.

### Human assessment

Fill Primary during initial review. At handoff, preserve Primary and copy its eight answers into Checker / final. Edit only Checker / final during checking. A blank final answer does not inherit a primary answer.

| Field | Primary | Checker / final |
| --- | --- | --- |
| Disposition |  |  |
| Review domain |  |  |
| Statistcal\_or\_numerical issue |  |  |
| Substantiveness |  |  |
| Downstream impact |  |  |
| Report-internal or planning-material inconsistency |  |  |
| Protocol interpretation |  |  |
| Notes (optional) |  |  |
| Complete | no | no |

| Checker record | Value |
| --- | --- |
| Checker result |  |
| Checker comment |  |
| Discussion resolution |  |
| Resolution note |  |
| Final outcome |  |

For `agree`, all eight effective final answers must equal Primary. Other checker results require a comment. `disagree`, `unable`, or a primary `discuss` require resolved discussion and a note naming participants and the conclusion. Leave Final outcome blank until final readiness.

### Evidence

#### Evidence 0: Source evidence

> The first four cells print 33 (6.9), 26 (7.8), 22 (7.4), and 35 (6.6) without %; the last four print 38 (6.9%), 33 (9.0%), 29 (8.2%), and 33 (6.8%) with %.

#### Evidence 1: Reported-versus-comparator

> All eight are percentage displays within one \[n (%)\] row, but % is absent from the first four and present in the final four.

#### Evidence 2: Calculation

> 33/480×100=6.875%→6.9%; 26/335×100=7.761…%→7.8%; 22/298×100=7.383…%→7.4%; 35/530×100=6.604…%→6.6%. All reconcile at one decimal (0.05 percentage-point rounding tolerance); the issue is notation, not a rate/count discrepancy.

#### Evidence 3: Alternative source-grounded interpretations

> The row header makes unsigned values interpretable as percentages, but the source gives no reason why only the final four cells carry % or which convention was intended.

### Source links

- sourceLinks 0: [Results Supplement — PDF p. 18](../../../2025/jama.2025.9110/joi250040supp3_prod_1753124024.38098.pdf#page=18)

[Original Markdown report](../../../2025/jama.2025.9110/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2025::jama.2025.9110::C006 |
| legacyRelationship |  |
| locations | Results Supplement — PDF p. 18, eTable 10, New kidney replacement therapy commenced during index ICU admission after commencing trial enteral nutrition \[n (%)\]. |
| originalCrossDocument | 0 |
| package | jama.2025.9110 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. All eight are percentage displays within one \`\[n (%)\]\` row, but \`%\` is absent from the first four and present in the final four. |
| reportHref | ../../2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.9110/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The eTable 10 new-kidney-replacement-therapy row changes percent-sign notation halfway across matched period cells. |
| submissionInvolved | 1 |
| subtype | eTable 10 new-KRT row switches percent-sign notation across period cells |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 10 new-KRT row switches percent-sign notation across period cells |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Completion checklist

- [ ] Primary reviewer ID is recorded and every primary assessment is complete.
- [ ] Primary answers were preserved at handoff, with a backup or revision reference recorded.
- [ ] Checker is a different person, with a distinct reviewer ID.
- [ ] Every final assessment uses valid applicable codes and Complete is checker_done.
- [ ] Agreement matches Primary; all other checker results have comments.
- [ ] Required discussions are resolved and participants and conclusions are recorded.
- [ ] No final disposition remains discuss, and every Final outcome follows the codebook.
- [ ] Final counts reconcile to the candidate total and Paper status is final_ready.
