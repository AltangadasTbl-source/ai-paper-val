# jama.2018.0156

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.0156 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.0156/)

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

- [C001](#candidate-c001) — Noninferiority narrative reverses the displayed bound direction (S_W)
- [C002](#candidate-c002) — Centre-5 pause contrast mixes a count outcome with seconds (S_W)
- [C003](#candidate-c003) — PP day-28 survival point difference does not round from the printed inputs (S_W)
- [C004](#candidate-c004) — PP day-28 survival confidence interval has an unresolved scale/precision inconsistency (S_W)
- [C005](#candidate-c005) — PP ROSC ETI percentage conflicts with its count, denominator, and signed difference (S_W)
- [C006](#candidate-c006) — Main article and eTable report different contributing-centre counts (S_C)
- [C007](#candidate-c007) — Published primary-endpoint description omits the amended baseline-disability qualification (P_R)
- [C008](#candidate-c008) — Protocol composite technique-failure definition cannot reconcile with the article’s smaller ETI failure count if they are the same endpoint (P_R)

## Candidate C001

**Noninferiority narrative reverses the displayed bound direction**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3 (rule); jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 4 (result/narrative).

### Candidate statement

> The narrative calls a lower CI limit greater than the threshold although the displayed lower limit is below it; the printed conclusion remains compatible with the displayed values.

### AI rationale

> The narrative calls a lower CI limit greater than the threshold although the displayed lower limit is below it; the printed conclusion remains compatible with the displayed values. The focal mismatch is within the main article.

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

> Noninferiority requires a BMV-minus-ETI lower endpoint greater than -1.00%; the result prints -1.64% and says it was “greater than the threshold,” then says noninferiority was not demonstrated.

#### Evidence 1: Reported-versus-comparator

> Reported “greater”; comparator -1.64% versus -1.00% under the stated strict rule.

#### Evidence 2: Calculation

> -1.64% \< -1.00%; difference -0.64 percentage points.

#### Evidence 3: Alternative source-grounded interpretations

> A direction word may be reversed or omitted; intended replacement wording is not supplied, while the conclusion is source-consistent.

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=3)
- sourceLinks 1: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 4](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2018::jama.2018.0156::C001 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3 (rule); jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 4 (result/narrative). |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism |  |
| primary | S\_W |
| rationale | The narrative calls a lower CI limit greater than the threshold although the displayed lower limit is below it; the printed conclusion remains compatible with the displayed values. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The narrative calls a lower CI limit greater than the threshold although the displayed lower limit is below it; the printed conclusion remains compatible with the displayed values. |
| submissionInvolved | 1 |
| subtype | noninferiority\_direction\_word |
| suggestedDomain | statistical\_results |
| title | Noninferiority narrative reverses the displayed bound direction |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Centre-5 pause contrast mixes a count outcome with seconds**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3 (definition); jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 4 (contrast).

### Candidate statement

> A contrast for the number of qualifying pauses is labelled in seconds.

### AI rationale

> A contrast for the number of qualifying pauses is labelled in seconds. The focal mismatch is within the main article.

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

> The outcome is the “number of pauses” lasting more than 2 seconds; BMV is 27, ETI 16, and the difference is printed as 11 seconds (95% CI 7 to 15).

#### Evidence 1: Reported-versus-comparator

> Reported 11 seconds; comparator is a difference in the stated number of qualifying pauses.

#### Evidence 2: Calculation

> 27 - 16 = 11 qualifying pauses under the printed wording.

#### Evidence 3: Alternative source-grounded interpretations

> The source does not say whether values are totals, means, medians, or another summary; a time interpretation conflicts with “number of pauses.”

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=3)
- sourceLinks 1: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 4](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.0156::C002 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3 (definition); jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 4 (contrast). |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism |  |
| primary | S\_W |
| rationale | A contrast for the number of qualifying pauses is labelled in seconds. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | A contrast for the number of qualifying pauses is labelled in seconds. |
| submissionInvolved | 1 |
| subtype | count\_vs\_duration\_unit |
| suggestedDomain | report\_internal\_inconsistency |
| title | Centre-5 pause contrast mixes a count outcome with seconds |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**PP day-28 survival point difference does not round from the printed inputs**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 6 (Table 2); joi180004supp1\_prod.pdf — PDF p. 123 (rounding rule).

### Candidate statement

> The PP survival difference 0.1 percentage points does not ordinarily round from the displayed counts and denominators.

### AI rationale

> The main Table 2 PP-survival difference 0.1 does not round from its displayed 54/995 and 51/943 inputs, which yield 0.0189 percentage points. The SAP rounding sentence is a supporting convention, not a separate reported-versus-plan discrepancy.

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

> BMV is 54/995 (5.4%), ETI 51/943 (5.4%), and BMV-minus-ETI is 0.1 percentage points.

#### Evidence 1: Reported-versus-comparator

> Reported 0.1; comparator from printed inputs is 0.0189 percentage points, ordinarily 0.0 to one decimal.

#### Evidence 2: Calculation

> 100 × (54/995 - 51/943) = 0.0189 percentage points, rounding to 0.0.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated retained estimator, denominator, adjustment, weighting, or rounding procedure could explain the display; no correction is adjudicated.

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 6](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=6)
- sourceLinks 1: [joi180004supp1\_prod.pdf — PDF p. 123](../../../2018/jama.2018.0156/joi180004supp1_prod.pdf#page=123)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The SAP explicitly rounds categorical percentages, not separately differences; an unreported estimator/denominator may explain the displayed 0.1. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2018::jama.2018.0156::C003 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 6 (Table 2); joi180004supp1\_prod.pdf — PDF p. 123 (rounding rule). |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism |  |
| primary | S\_W |
| rationale | The main Table 2 PP-survival difference 0.1 does not round from its displayed 54/995 and 51/943 inputs, which yield 0.0189 percentage points. The SAP rounding sentence is a supporting convention, not a separate reported-versus-plan discrepancy. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The PP survival difference 0.1 percentage points does not ordinarily round from the displayed counts and denominators. |
| submissionInvolved | 1 |
| subtype | risk\_difference\_arithmetic |
| suggestedDomain | statistical\_results |
| title | PP day-28 survival point difference does not round from the printed inputs |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**PP day-28 survival confidence interval has an unresolved scale/precision inconsistency**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3 (rule); PDF p. 6 (Table 2); joi180004supp1\_prod.pdf — PDF p. 124 (CI rule).

### Candidate statement

> The PP survival interval in a percentage-point column has a scale/precision appearance unresolved by supplied row-level methods or inputs.

### AI rationale

> The main Table 2 interval -10 to 9.7 has unresolved scale/precision relative to the same row counts, effect scale, and P=.99. SAP CI wording corroborates the general method and does not itself conflict with reported analysis.

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

> The column prints difference 0.1, 95% CI -10 to 9.7, and P=.99 for 54/995 versus 51/943.

#### Evidence 1: Reported-versus-comparator

> Reported interval -10 to 9.7 percentage points; diagnostic ordinary unpooled-binomial comparator is about -2.00 to 2.04 points.

#### Evidence 2: Calculation

> Diagnostic SE 1.028756 points; with difference 0.018864, Wald 95% interval -1.997498 to 2.035226 points.

#### Evidence 3: Alternative source-grounded interpretations

> Nonstandard method, retained data, adjustment, correction, or decimal production issue may explain the display; exact construction is absent.

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=3)
- sourceLinks 1: [PDF p. 6](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=6)
- sourceLinks 2: [joi180004supp1\_prod.pdf — PDF p. 124](../../../2018/jama.2018.0156/joi180004supp1_prod.pdf#page=124)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The diagnostic Wald interval is not an authoritative replacement; exact source CI construction is absent. Distinct from C003 point-estimate arithmetic although the same row is involved. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2018::jama.2018.0156::C004 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 3 (rule); PDF p. 6 (Table 2); joi180004supp1\_prod.pdf — PDF p. 124 (CI rule). |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism |  |
| primary | S\_W |
| rationale | The main Table 2 interval -10 to 9.7 has unresolved scale/precision relative to the same row counts, effect scale, and P=.99. SAP CI wording corroborates the general method and does not itself conflict with reported analysis. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The PP survival interval in a percentage-point column has a scale/precision appearance unresolved by supplied row-level methods or inputs. |
| submissionInvolved | 1 |
| subtype | ci\_scale\_precision |
| suggestedDomain | statistical\_results |
| title | PP day-28 survival confidence interval has an unresolved scale/precision inconsistency |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**PP ROSC ETI percentage conflicts with its count, denominator, and signed difference**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 6 (Table 2 PP ROSC row).

### Candidate statement

> The ETI PP ROSC percentage conflicts with its numerator/denominator and signed BMV-minus-ETI contrast.

### AI rationale

> The ETI PP ROSC percentage conflicts with its numerator/denominator and signed BMV-minus-ETI contrast. The focal mismatch is within the main article.

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

> BMV 342/995 (34.4%), ETI 377/943 (30.0%), and BMV-minus-ETI -5.6 points are printed.

#### Evidence 1: Reported-versus-comparator

> Reported ETI 30.0%; 377/943 = 39.979% (rounds 40.0%), and count-derived contrast is negative while displayed percentages imply positive.

#### Evidence 2: Calculation

> 100 × 377/943 = 39.979%; 100 × (342/995 - 377/943) = -5.607 points, matching -5.6; printed percentages give +4.4 points.

#### Evidence 3: Alternative source-grounded interpretations

> The source does not establish which printed value or retained estimator was intended; no correction is adjudicated.

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 6](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=6)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2018::jama.2018.0156::C005 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 6 (Table 2 PP ROSC row). |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism |  |
| primary | S\_W |
| rationale | The ETI PP ROSC percentage conflicts with its numerator/denominator and signed BMV-minus-ETI contrast. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The ETI PP ROSC percentage conflicts with its numerator/denominator and signed BMV-minus-ETI contrast. |
| submissionInvolved | 1 |
| subtype | proportion\_and\_contrast\_direction |
| suggestedDomain | statistical\_results |
| title | PP ROSC ETI percentage conflicts with its count, denominator, and signed difference |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**Main article and eTable report different contributing-centre counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 2; joi180004supp2\_prod.pdf — PDF p. 2 (eTable 1).

### Candidate statement

> The article reports 20 EMS centres whereas eTable 1 shows 21 contributing investigator-centre rows.

### AI rationale

> The article reports 20 EMS centres whereas eTable 1 shows 21 contributing investigator-centre rows. The focal comparison is the main article versus a non-plan results supplement.

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

> Methods state 20 EMS centres (15 France, 5 Belgium); eTable 1 has 21 nonempty investigator-centre rows, whose arm totals reconcile to 1018 and 1022.

#### Evidence 1: Reported-versus-comparator

> Reported count 20; comparator 21 displayed rows.

#### Evidence 2: Calculation

> 15 + 5 = 20; eTable rows = 21.

#### Evidence 3: Alternative source-grounded interpretations

> One EMS centre may map to multiple investigator-centre records; no crosswalk is supplied.

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 2](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=2)
- sourceLinks 1: [joi180004supp2\_prod.pdf — PDF p. 2](../../../2018/jama.2018.0156/joi180004supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Twenty EMS centres versus 21 investigator-centre rows may reflect different counting units; no centre-to-investigator crosswalk is supplied. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2018::jama.2018.0156::C006 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 2; joi180004supp2\_prod.pdf — PDF p. 2 (eTable 1). |
| originalCrossDocument | 1 |
| package | jama.2018.0156 |
| planMechanism |  |
| primary | S\_C |
| rationale | The article reports 20 EMS centres whereas eTable 1 shows 21 contributing investigator-centre rows. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The article reports 20 EMS centres whereas eTable 1 shows 21 contributing investigator-centre rows. |
| submissionInvolved | 1 |
| subtype | centre\_count\_unit |
| suggestedDomain | report\_internal\_inconsistency |
| title | Main article and eTable report different contributing-centre counts |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Published primary-endpoint description omits the amended baseline-disability qualification**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C007 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 1 and PDF p. 3; joi180004supp1\_prod.pdf — PDF p. 110.

### Candidate statement

> The article’s CPC-1-or-2 endpoint description omits the amendment’s qualification for survivors with baseline neurologic disability.

### AI rationale

> The main article defines favorable outcome as CPC 1 or 2, while a supplied amended protocol also qualifies baseline-disabled survivors whose disability is unchanged. The potential outcome-definition difference is directly report versus amended plan.

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

> Article: favourable outcome CPC 1 or 2. Amendment: a baseline-disabled survivor is favourable if survival retains the same disability degree.

#### Evidence 1: Reported-versus-comparator

> Reported CPC-1-or-2 description; comparator is the additional amendment qualification.

#### Evidence 2: Calculation

> No aggregate calculation: a survivor can satisfy the amendment qualification without a literal CPC-1-or-2-only classification.

#### Evidence 3: Alternative source-grounded interpretations

> Article wording may be abbreviated or no participant may require the qualification; final coding and affected count are absent.

### Source links

- sourceLinks 0: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 1](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=1)
- sourceLinks 1: [PDF p. 3](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=3)
- sourceLinks 2: [joi180004supp1\_prod.pdf — PDF p. 110](../../../2018/jama.2018.0156/joi180004supp1_prod.pdf#page=110)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | An abbreviated article definition or no affected participants could reconcile the result; aggregate counts cannot establish actual coding or count changes. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2018::jama.2018.0156::C007 |
| legacyRelationship |  |
| locations | jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 1 and PDF p. 3; joi180004supp1\_prod.pdf — PDF p. 110. |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | The main article defines favorable outcome as CPC 1 or 2, while a supplied amended protocol also qualifies baseline-disabled survivors whose disability is unchanged. The potential outcome-definition difference is directly report versus amended plan. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | The article’s CPC-1-or-2 endpoint description omits the amendment’s qualification for survivors with baseline neurologic disability. |
| submissionInvolved | 0 |
| subtype | outcome\_definition\_amendment |
| suggestedDomain | protocol\_report |
| title | Published primary-endpoint description omits the amended baseline-disability qualification |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C008

**Protocol composite technique-failure definition cannot reconcile with the article’s smaller ETI failure count if they are the same endpoint**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.0156::C008 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | discuss |

### Source location

> joi180004supp1\_prod.pdf — PDF p. 110; jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 1, PDF p. 4, and PDF p. 6.

### Candidate statement

> If the protocol composite and article Table 3 row denote the same endpoint and aligned population, aggregate displays cannot reconcile.

### AI rationale

> A supplied amended protocol defines technique failure as a composite including mortality/regurgitation/procedural failure, while the main Table 3 ETI failure row reports 21/996 without that composite definition. This is a conditional report-versus-plan endpoint/population mismatch.

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

> Amended protocol technique failure includes 28-day mortality, regurgitation, or failure to ventilate/intubate. Article prints ETI failure 21/996 (2.1%) and ITT ETI deaths 54/1022.

#### Evidence 1: Reported-versus-comparator

> Reported 21/996; conditional conservative comparator is at least 27 before other composite components.

#### Evidence 2: Calculation

> 54 - 24 - 3 = 27, and 27 \> 21.

#### Evidence 3: Alternative source-grounded interpretations

> Article row may be narrower, use another final definition, or use actual-treatment population; aggregate displays do not establish participant alignment.

### Source links

- sourceLinks 0: [joi180004supp1\_prod.pdf — PDF p. 110](../../../2018/jama.2018.0156/joi180004supp1_prod.pdf#page=110)
- sourceLinks 1: [jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 1](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=1)
- sourceLinks 2: [PDF p. 4](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=4)
- sourceLinks 3: [PDF p. 6](../../../2018/jama.2018.0156/jama_jabre_2018_oi_180004.pdf#page=6)
- evidencePaths 0: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)
- evidencePaths 2: [2018/jama.2018.0156/.ai\_paper\_validation/review\_1\_5\_2/preprocessing/native\_text/jama\_jabre\_2018\_oi\_180004.txt](../../../2018/jama.2018.0156/.ai_paper_validation/review_1_5_2/preprocessing/native_text/jama_jabre_2018_oi_180004.txt)

[Original Markdown report](../../../2018/jama.2018.0156/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 1 |
| ambiguity | The failure row may intentionally be procedural-only and uses actual-treatment safety data. The 27-versus-21 aggregate bound assumes participant-set alignment; recheck expressly says that assumption is not mechanically established. Additional source-derivative check: the final card and recheck call 54/1022 ETI deaths, but main native text explicitly labels 54/1022 day-28 survival. Thus the recorded 27-versus-21 mortality bound uses a mislabeled input and is not source-confirmed; the document-role endpoint-definition comparison is retained. Exact main-abstract derivative wording: global survival at day 28 (55/1018 \[5.4%\] in the BMV group vs 54/1022 \[5.3%\] in the ETI group). |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2018::jama.2018.0156::C008 |
| legacyRelationship |  |
| locations | joi180004supp1\_prod.pdf — PDF p. 110; jama\_jabre\_2018\_oi\_180004.pdf — PDF p. 1, PDF p. 4, and PDF p. 6. |
| originalCrossDocument | 0 |
| package | jama.2018.0156 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | A supplied amended protocol defines technique failure as a composite including mortality/regurgitation/procedural failure, while the main Table 3 ETI failure row reports 21/996 without that composite definition. This is a conditional report-versus-plan endpoint/population mismatch. |
| reportHref | ../../2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.0156/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | If the protocol composite and article Table 3 row denote the same endpoint and aligned population, aggregate displays cannot reconcile. |
| submissionInvolved | 0 |
| subtype | composite\_vs\_reported\_endpoint |
| suggestedDomain | protocol\_report |
| title | Protocol composite technique-failure definition cannot reconcile with the article’s smaller ETI failure count if they are the same endpoint |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | discuss |

## Completion checklist

- [ ] Primary reviewer ID is recorded and every primary assessment is complete.
- [ ] Primary answers were preserved at handoff, with a backup or revision reference recorded.
- [ ] Checker is a different person, with a distinct reviewer ID.
- [ ] Every final assessment uses valid applicable codes and Complete is checker_done.
- [ ] Agreement matches Primary; all other checker results have comments.
- [ ] Required discussions are resolved and participants and conclusions are recorded.
- [ ] No final disposition remains discuss, and every Final outcome follows the codebook.
- [ ] Final counts reconcile to the candidate total and Paper status is final_ready.
