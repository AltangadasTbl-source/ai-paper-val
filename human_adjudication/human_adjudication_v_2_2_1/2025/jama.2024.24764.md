# jama.2024.24764

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2024.24764 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2024.24764/)

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

- [C001](#candidate-c001) — Smoking percentages use a different denominator from the printed smoking totals (S_W)
- [C002](#candidate-c002) — Operating-surgeon level totals exceed participant denominators without a multi-response qualifier (S_W)
- [C003](#candidate-c003) — Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier (S_W)
- [C004](#candidate-c004) — Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier (S_W)
- [C005](#candidate-c005) — Control-arm mortality differs between participant flow and 30-day safety reporting (S_W)
- [C006](#candidate-c006) — Longitudinal quality-of-life covariance specification differs between SAP and final article (P_R)
- [C007](#candidate-c007) — Length-of-stay effect measure and model differ between SAP/protocol and final article (P_R)
- [C008](#candidate-c008) — Australia-inclusive length-of-stay result differs from the stated UK-only analysis population (P_R)

## Candidate C001

**Smoking percentages use a different denominator from the printed smoking totals**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 5, Table 1

### Candidate statement

> The smoking rows print variable-specific totals of 405 and 402, while all six percentages reproduce the group-header denominators 411 and 410 without an explanatory convention.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Reported percentages are 53.5/23.1/21.9 and 54.4/17.1/26.6; comparator denominators are printed smoking totals 405/402 versus group headers 411/410.

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

> Smoking counts are 220/95/90 and 223/70/109; they sum to printed Total No. values 405 and 402. Group headers are 411 and 410.

#### Evidence 1: Reported-versus-comparator

> Reported percentages are 53.5/23.1/21.9 and 54.4/17.1/26.6; comparator denominators are printed smoking totals 405/402 versus group headers 411/410.

#### Evidence 2: Calculation

> 220+95+90=405; 223+70+109=402. 220/411=53.53% and the other five printed percentages likewise reproduce 411/410, not 405/402.

#### Evidence 3: Alternative source-grounded interpretations

> Total No. may denote nonmissing smoking records while percentages intentionally use all randomized participants; the page does not state that convention or identify the six and eight unclassified records.

### Source links

- sourceLinks 0: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 5, Table 1](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=5)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

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
| id | C001 |
| key | 2025::jama.2024.24764::C001 |
| legacyRelationship |  |
| locations | jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 5, Table 1 |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Reported percentages are 53.5/23.1/21.9 and 54.4/17.1/26.6; comparator denominators are printed smoking totals 405/402 versus group headers 411/410. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The smoking rows print variable-specific totals of 405 and 402, while all six percentages reproduce the group-header denominators 411 and 410 without an explanatory convention. |
| submissionInvolved | 1 |
| subtype | Smoking percentages use a different denominator from the printed smoking totals |
| suggestedDomain | statistical\_results |
| title | Smoking percentages use a different denominator from the printed smoking totals |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Operating-surgeon level totals exceed participant denominators without a multi-response qualifier**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2

### Candidate statement

> Operating-surgeon category totals exceed the printed participant denominators without a statement that the rows permit multiple responses.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Category totals 446 and 429 are compared with participant denominators 411 and 410; percentage totals are 108.5% and 104.6%.

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

> Under No. of participants (%), consultant/registrar/senior-house-officer values are 319/123/4 and 318/110/1, with group denominators 411 and 410.

#### Evidence 1: Reported-versus-comparator

> Category totals 446 and 429 are compared with participant denominators 411 and 410; percentage totals are 108.5% and 104.6%.

#### Evidence 2: Calculation

> 319+123+4=446 (35 above 411); 318+110+1=429 (19 above 410).

#### Evidence 3: Alternative source-grounded interpretations

> More than one surgeon level may have operated on a participant, making the rows multi-response; no qualifier appears on the page.

### Source links

- sourceLinks 0: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

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
| id | C002 |
| key | 2025::jama.2024.24764::C002 |
| legacyRelationship |  |
| locations | jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Category totals 446 and 429 are compared with participant denominators 411 and 410; percentage totals are 108.5% and 104.6%. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Operating-surgeon category totals exceed the printed participant denominators without a statement that the rows permit multiple responses. |
| submissionInvolved | 1 |
| subtype | Operating-surgeon level totals exceed participant denominators without a multi-response qualifier |
| suggestedDomain | statistical\_results |
| title | Operating-surgeon level totals exceed participant denominators without a multi-response qualifier |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 continuation

### Candidate statement

> Fascia-closing surgeon-level totals exceed participant denominators without a stated multi-response rule.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Totals 445 and 433 are compared with 411 and 410; percentage totals are 108.2% and 105.7%.

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

> Consultant/registrar/senior-house-officer fascia-closing counts are 201/218/26 and 193/225/15 under group denominators 411 and 410.

#### Evidence 1: Reported-versus-comparator

> Totals 445 and 433 are compared with 411 and 410; percentage totals are 108.2% and 105.7%.

#### Evidence 2: Calculation

> 201+218+26=445 (34 above 411); 193+225+15=433 (23 above 410).

#### Evidence 3: Alternative source-grounded interpretations

> Co-closure by more than one surgeon level may make the rows intentionally multi-response; the table gives no response-unit definition.

### Source links

- sourceLinks 0: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 continuation](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

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
| id | C003 |
| key | 2025::jama.2024.24764::C003 |
| legacyRelationship |  |
| locations | jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 continuation |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Totals 445 and 433 are compared with 411 and 410; percentage totals are 108.2% and 105.7%. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Fascia-closing surgeon-level totals exceed participant denominators without a stated multi-response rule. |
| submissionInvolved | 1 |
| subtype | Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier |
| suggestedDomain | statistical\_results |
| title | Fascia-closing surgeon level totals exceed participant denominators without a multi-response qualifier |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 continuation

### Candidate statement

> Skin-closing surgeon-level totals exceed participant denominators without a stated multi-response rule.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Totals 425 and 416 are compared with 411 and 410; percentage totals are 103.5% and 101.5%.

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

> Consultant/registrar/senior-house-officer skin-closing counts are 115/214/96 and 102/241/73 under denominators 411 and 410.

#### Evidence 1: Reported-versus-comparator

> Totals 425 and 416 are compared with 411 and 410; percentage totals are 103.5% and 101.5%.

#### Evidence 2: Calculation

> 115+214+96=425 (14 above 411); 102+241+73=416 (6 above 410).

#### Evidence 3: Alternative source-grounded interpretations

> The rows may be intended multi-response entries, but the source does not state this.

### Source links

- sourceLinks 0: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 continuation](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=7)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

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
| id | C004 |
| key | 2025::jama.2024.24764::C004 |
| legacyRelationship |  |
| locations | jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 7, Table 2 continuation |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Totals 425 and 416 are compared with 411 and 410; percentage totals are 103.5% and 101.5%. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Skin-closing surgeon-level totals exceed participant denominators without a stated multi-response rule. |
| submissionInvolved | 1 |
| subtype | Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier |
| suggestedDomain | statistical\_results |
| title | Skin-closing surgeon level totals exceed participant denominators without a multi-response qualifier |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Control-arm mortality differs between participant flow and 30-day safety reporting**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 3, Figure 1; PDF p. 6, safety narrative; PDF p. 8, Table 3

### Candidate statement

> Participant flow reports 25 deaths (10 intervention, 15 control), whereas Table 3 and the safety narrative report 24 deaths within 30 days (10 intervention, 14 control).

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Figure 1 total 25 and control count 15 are compared with the explicitly 30-day total 24 and control count 14.

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

> Figure 1 reports 10 and 15 deaths. The narrative and Table 3 report mortality within 30 days as 10/411 and 14/410.

#### Evidence 1: Reported-versus-comparator

> Figure 1 total 25 and control count 15 are compared with the explicitly 30-day total 24 and control count 14.

#### Evidence 2: Calculation

> 10+15=25; 10+14=24; intervention counts agree and control counts differ by one.

#### Evidence 3: Alternative source-grounded interpretations

> Figure 1 may include one control-arm death outside the 30-day window; Figure 1 does not name its mortality window.

### Source links

- sourceLinks 0: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 3, Figure 1](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=3)
- sourceLinks 1: [PDF p. 6, safety narrative](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6)
- sourceLinks 2: [PDF p. 8, Table 3](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8)
- evidencePaths 0: [2025/jama.2024.24764/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2025/jama.2024.24764/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Figure mortality window is unspecified; count discrepancy may be a time-window difference. All locations are in the main article despite original cross-document category. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2025::jama.2024.24764::C005 |
| legacyRelationship |  |
| locations | jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 3, Figure 1; PDF p. 6, safety narrative; PDF p. 8, Table 3 |
| originalCrossDocument | 1 |
| package | jama.2024.24764 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Figure 1 total 25 and control count 15 are compared with the explicitly 30-day total 24 and control count 14. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Participant flow reports 25 deaths (10 intervention, 15 control), whereas Table 3 and the safety narrative report 24 deaths within 30 days (10 intervention, 14 control). |
| submissionInvolved | 1 |
| subtype | Control-arm mortality differs between participant flow and 30-day safety reporting |
| suggestedDomain | report\_internal\_inconsistency |
| title | Control-arm mortality differs between participant flow and 30-day safety reporting |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**Longitudinal quality-of-life covariance specification differs between SAP and final article**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C006 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 26, SAP; jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 4, Statistical Analysis

### Candidate statement

> The SAP specifies unstructured covariance with robust sandwich standard errors for the QoL model family, while the final article specifies independent covariance.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Final-article independent covariance is compared with SAP unstructured covariance and robust sandwich variance estimation.

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

> The SAP prints unstructured covariance and robust sandwich standard errors for SF-12/EQ-5D repeated measures; the final article prints independent covariance for that outcome-model family.

#### Evidence 1: Reported-versus-comparator

> Final-article independent covariance is compared with SAP unstructured covariance and robust sandwich variance estimation.

#### Evidence 2: Calculation

> Not applicable; unstructured and independent are distinct named covariance specifications.

#### Evidence 3: Alternative source-grounded interpretations

> An amendment, diagnostic, convergence consideration, or concise article description may explain the difference; no such record is supplied.

### Source links

- sourceLinks 0: [joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 26, SAP](../../../2025/jama.2024.24764/joi240145supp1_prod_1741627844.87412.pdf#page=26)
- sourceLinks 1: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 4, Statistical Analysis](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4)
- evidencePaths 0: [2025/jama.2024.24764/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2025/jama.2024.24764/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Covariance specifications differ; article silence about sandwich SE does not prove it was absent. Amendment/output unavailable. |
| broadPlanInvolved | 1 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2025::jama.2024.24764::C006 |
| legacyRelationship |  |
| locations | joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 26, SAP; jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 4, Statistical Analysis |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Final-article independent covariance is compared with SAP unstructured covariance and robust sandwich variance estimation. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The SAP specifies unstructured covariance with robust sandwich standard errors for the QoL model family, while the final article specifies independent covariance. |
| submissionInvolved | 0 |
| subtype | Longitudinal quality-of-life covariance specification differs between SAP and final article |
| suggestedDomain | protocol\_report |
| title | Longitudinal quality-of-life covariance specification differs between SAP and final article |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C007

**Length-of-stay effect measure and model differ between SAP/protocol and final article**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C007 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 25, SAP; joi240145supp4\_prod\_1741627844.90412.pdf — PDF p. 39, protocol; jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 4; PDF p. 8, Table 3

### Candidate statement

> SAP/protocol describe adjusted mean difference, or skewed-data unadjusted median difference, whereas the final article reports log-transformed adjusted ratios of geometric means for length of stay.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Multiplicative, dimensionless ratios of geometric means are compared with additive differences in days for the same endpoint.

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

> The final article reports adjusted ratios of geometric means 0.91 and 0.96 after log transformation; SAP/protocol plan additive mean-difference or median-difference reporting.

#### Evidence 1: Reported-versus-comparator

> Multiplicative, dimensionless ratios of geometric means are compared with additive differences in days for the same endpoint.

#### Evidence 2: Calculation

> Not reproducible from aggregate printed data: medians/IQRs cannot reconstruct geometric means, fitted log-scale coefficients, or adjusted ratios.

#### Evidence 3: Alternative source-grounded interpretations

> Nonnormality noted in the article may have motivated the final approach, but the supplied skewness branch specifies a median difference and no amendment or decision rule is supplied.

### Source links

- sourceLinks 0: [joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 25, SAP](../../../2025/jama.2024.24764/joi240145supp1_prod_1741627844.87412.pdf#page=25)
- sourceLinks 1: [joi240145supp4\_prod\_1741627844.90412.pdf — PDF p. 39, protocol](../../../2025/jama.2024.24764/joi240145supp4_prod_1741627844.90412.pdf#page=39)
- sourceLinks 2: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 4](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4)
- sourceLinks 3: [PDF p. 8, Table 3](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8)
- evidencePaths 0: [2025/jama.2024.24764/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2025/jama.2024.24764/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | UK-only comparison isolates effect measure from C008 population issue; skewness anticipated but planned median difference differs from geometric-mean ratio. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2025::jama.2024.24764::C007 |
| legacyRelationship |  |
| locations | joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 25, SAP; joi240145supp4\_prod\_1741627844.90412.pdf — PDF p. 39, protocol; jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 4; PDF p. 8, Table 3 |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Multiplicative, dimensionless ratios of geometric means are compared with additive differences in days for the same endpoint. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | SAP/protocol describe adjusted mean difference, or skewed-data unadjusted median difference, whereas the final article reports log-transformed adjusted ratios of geometric means for length of stay. |
| submissionInvolved | 0 |
| subtype | Length-of-stay effect measure and model differ between SAP/protocol and final article |
| suggestedDomain | protocol\_report |
| title | Length-of-stay effect measure and model differ between SAP/protocol and final article |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C008

**Australia-inclusive length-of-stay result differs from the stated UK-only analysis population**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2024.24764::C008 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 18, SAP endpoint; PDF p. 25, SAP population; joi240145supp4\_prod\_1741627844.90412.pdf — PDF p. 24, protocol; jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 1, abstract; PDF p. 8, Table 3

### Candidate statement

> SAP and protocol specify UK-only length-of-stay reporting, while the final article additionally reports a UK-and-Australia result.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. A UK-and-Australia analysis population is compared with the planned UK-only endpoint population.

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

> SAP/protocol state that LOS is UK-only and exclude Australian-randomized participants. The final article reports UK-only ratio 0.91 (95% CI 0.82-1.02), P=.12 and UK-and-Australia ratio 0.96 (0.88-1.06), P=.21.

#### Evidence 1: Reported-versus-comparator

> A UK-and-Australia analysis population is compared with the planned UK-only endpoint population.

#### Evidence 2: Calculation

> No arithmetic reconstruction is required: UK patients only and UK and Australian patients are different populations.

#### Evidence 3: Alternative source-grounded interpretations

> The all-country result may be an additional intended analysis while the UK-only result remains the designated endpoint; the supplied package does not label its status.

### Source links

- sourceLinks 0: [joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 18, SAP endpoint](../../../2025/jama.2024.24764/joi240145supp1_prod_1741627844.87412.pdf#page=18)
- sourceLinks 1: [PDF p. 25, SAP population](../../../2025/jama.2024.24764/joi240145supp1_prod_1741627844.87412.pdf#page=25)
- sourceLinks 2: [joi240145supp4\_prod\_1741627844.90412.pdf — PDF p. 24, protocol](../../../2025/jama.2024.24764/joi240145supp4_prod_1741627844.90412.pdf#page=24)
- sourceLinks 3: [jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 1, abstract](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1)
- sourceLinks 4: [PDF p. 8, Table 3](../../../2025/jama.2024.24764/jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8)
- evidencePaths 0: [2025/jama.2024.24764/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2025/jama.2024.24764/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2024.24764/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | UK-only result remains reported; all-country result is additional and status is unclear, not proven substitution. |
| broadPlanInvolved | 1 |
| category | Analysis-unit or population inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2025::jama.2024.24764::C008 |
| legacyRelationship |  |
| locations | joi240145supp1\_prod\_1741627844.87412.pdf — PDF p. 18, SAP endpoint; PDF p. 25, SAP population; joi240145supp4\_prod\_1741627844.90412.pdf — PDF p. 24, protocol; jama\_atherton\_2025\_oi\_240145\_1741627844.85412.pdf — PDF p. 1, abstract; PDF p. 8, Table 3 |
| originalCrossDocument | 0 |
| package | jama.2024.24764 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. A UK-and-Australia analysis population is compared with the planned UK-only endpoint population. |
| reportHref | ../../2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2025/jama.2024.24764/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | SAP and protocol specify UK-only length-of-stay reporting, while the final article additionally reports a UK-and-Australia result. |
| submissionInvolved | 0 |
| subtype | Australia-inclusive length-of-stay result differs from the stated UK-only analysis population |
| suggestedDomain | protocol\_report |
| title | Australia-inclusive length-of-stay result differs from the stated UK-only analysis population |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
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
