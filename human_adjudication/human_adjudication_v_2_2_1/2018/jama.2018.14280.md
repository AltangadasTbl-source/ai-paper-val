# jama.2018.14280

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.14280 |
| Candidates | 23 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.14280/)

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

- [C001](#candidate-c001) — Reversed endpoint in the eTable 2 PEEP interquartile range (S_W)
- [C002](#candidate-c002) — At-risk-for-ARDS percentages use undisclosed denominators (S_W)
- [C003](#candidate-c003) — Septic-shock percentages use undisclosed denominators (S_W)
- [C004](#candidate-c004) — Tobacco-use categories use undisclosed denominators (S_W)
- [C005](#candidate-c005) — Alcohol-use categories use undisclosed denominators (S_W)
- [C006](#candidate-c006) — ICU-admission categories use undisclosed denominators (S_W)
- [C007](#candidate-c007) — Sedative-infusion percentages omit effective denominators (S_W)
- [C008](#candidate-c008) — Analgesic-infusion percentages omit effective denominators (S_W)
- [C009](#candidate-c009) — Neuromuscular-blockade percentages omit effective denominators (S_W)
- [C010](#candidate-c010) — Vasopressor-use percentages omit effective denominators (S_W)
- [C011](#candidate-c011) — Mortality effect-measure wording conflicts with Table 2 and the SAP (S_W)
- [C012](#candidate-c012) — ICU-mortality RR does not reproduce from printed risks (S_W)
- [C013](#candidate-c013) — Hospital-mortality RR does not reproduce from printed risks (S_W)
- [C014](#candidate-c014) — ARDS RR does not reproduce from printed risks (S_W)
- [C015](#candidate-c015) — Pneumonia RR does not reproduce from printed risks (S_W)
- [C016](#candidate-c016) — Pneumothorax RR does not reproduce from printed risks (S_W)
- [C017](#candidate-c017) — Atelectasis RR does not reproduce from printed risks (S_W)
- [C018](#candidate-c018) — Extrapulmonary-infection RR does not reproduce from printed risks (S_W)
- [C019](#candidate-c019) — Extrapulmonary-sepsis RR does not reproduce from printed risks (S_W)
- [C020](#candidate-c020) — Delirium RR does not reproduce from printed risks (S_W)
- [C021](#candidate-c021) — Tracheostomy RR does not reproduce from printed risks (S_W)
- [C022](#candidate-c022) — The same subgroup intervals are labelled IQR and 95% CI (S_C)
- [C023](#candidate-c023) — Enrollment completion dates differ by two days (P_R)

## Candidate C001

**Reversed endpoint in the eTable 2 PEEP interquartile range**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3, eTable 2, Other Mode of Ventilation, after titration on randomization day, intermediate arm, PEEP.

### Candidate statement

> The intermediate-arm PEEP value 8 (5-1) is incompatible with the table's median (IQR) definition.

### AI rationale

> The intermediate-arm PEEP value 8 (5-1) is incompatible with the table's median (IQR) definition. The focal mismatch is within one non-plan results supplement.

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

> Supplement 3 — PDF p. 6 prints 8 (5-1) cm H2O; the note defines median (interquartile range).

#### Evidence 1: Reported-versus-comparator

> Reported median/IQR 8 (5-1) versus the ordering required for lower quartile, median, upper quartile.

#### Evidence 2: Calculation

> 5 \<= 8 is true; 8 \<= 1 is false.

#### Evidence 3: Alternative source-grounded interpretations

> The final endpoint may be truncated or mistyped; no supplied source gives a replacement.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2018::jama.2018.14280::C001 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3, eTable 2, Other Mode of Ventilation, after titration on randomization day, intermediate arm, PEEP. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | The intermediate-arm PEEP value 8 (5-1) is incompatible with the table's median (IQR) definition. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The intermediate-arm PEEP value 8 (5-1) is incompatible with the table's median (IQR) definition. |
| submissionInvolved | 1 |
| subtype | iqr\_order |
| suggestedDomain | statistical\_results |
| title | Reversed endpoint in the eTable 2 PEEP interquartile range |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**At-risk-for-ARDS percentages use undisclosed denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 1, Patients at risk for ARDS, low and intermediate arms.

### Candidate statement

> Printed percentages do not reproduce from Table 1 arm headers, while smaller denominators reproduce them.

### AI rationale

> Printed percentages do not reproduce from Table 1 arm headers, while smaller denominators reproduce them. The focal mismatch is within the main article.

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

> Main article — PDF p. 5 prints 292 (61.6) and 290 (60.3) under n=477 and n=484.

#### Evidence 1: Reported-versus-comparator

> 61.6%/60.3% versus percentages calculated from displayed arm totals.

#### Evidence 2: Calculation

> 292/477=61.2%, 290/484=59.9%; 292/474=61.6%, 290/481=60.3%.

#### Evidence 3: Alternative source-grounded interpretations

> Available-case denominators 474 and 481 may have been used but are not printed.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14280::C002 |
| legacyRelationship |  |
| locations | DOC-001, Table 1, Patients at risk for ARDS, low and intermediate arms. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed percentages do not reproduce from Table 1 arm headers, while smaller denominators reproduce them. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed percentages do not reproduce from Table 1 arm headers, while smaller denominators reproduce them. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | At-risk-for-ARDS percentages use undisclosed denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Septic-shock percentages use undisclosed denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 1, Septic shock, low and intermediate arms.

### Candidate statement

> The displayed septic-shock percentages do not reproduce from the Table 1 arm headers.

### AI rationale

> The displayed septic-shock percentages do not reproduce from the Table 1 arm headers. The focal mismatch is within the main article.

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

> Main article — PDF p. 5 prints 82 (17.6) and 74 (15.5) under n=477 and n=484.

#### Evidence 1: Reported-versus-comparator

> 17.6%/15.5% versus header-total calculations.

#### Evidence 2: Calculation

> 82/477=17.2%; 74/484=15.3%, not the displayed values.

#### Evidence 3: Alternative source-grounded interpretations

> Smaller available-case denominators may have been used; exact denominators are not supplied.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14280::C003 |
| legacyRelationship |  |
| locations | DOC-001, Table 1, Septic shock, low and intermediate arms. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | The displayed septic-shock percentages do not reproduce from the Table 1 arm headers. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed septic-shock percentages do not reproduce from the Table 1 arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Septic-shock percentages use undisclosed denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**Tobacco-use categories use undisclosed denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 1, Patient tobacco use, both arms.

### Candidate statement

> Tobacco-use counts and percentages reconcile to 475/482 rather than the 477/484 arm headers.

### AI rationale

> Tobacco-use counts and percentages reconcile to 475/482 rather than the 477/484 arm headers. The focal mismatch is within the main article.

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

> Main article — PDF p. 5 lists never/current/previous/unknown tobacco categories.

#### Evidence 1: Reported-versus-comparator

> Four category counts versus Table 1 arm headers.

#### Evidence 2: Calculation

> Low 106+97+75+197=475; intermediate 111+97+80+194=482; 106/475=22.3%, 111/482=23.0%.

#### Evidence 3: Alternative source-grounded interpretations

> 475/482 available records may be intended despite an Unknown category.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14280::C004 |
| legacyRelationship |  |
| locations | DOC-001, Table 1, Patient tobacco use, both arms. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Tobacco-use counts and percentages reconcile to 475/482 rather than the 477/484 arm headers. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Tobacco-use counts and percentages reconcile to 475/482 rather than the 477/484 arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Tobacco-use categories use undisclosed denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Alcohol-use categories use undisclosed denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 1, Patient alcohol use, both arms.

### Candidate statement

> Alcohol-use counts and percentages reconcile to 475/482 rather than Table 1 arm headers.

### AI rationale

> Alcohol-use counts and percentages reconcile to 475/482 rather than Table 1 arm headers. The focal mismatch is within the main article.

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

> Main article — PDF p. 5 prints the five alcohol-use categories.

#### Evidence 1: Reported-versus-comparator

> Category totals and percentage bases versus n=477/n=484 headers.

#### Evidence 2: Calculation

> Low 121+47+26+59+222=475; intermediate 92+61+30+56+243=482; 121/475=25.5%, 92/482=19.1%.

#### Evidence 3: Alternative source-grounded interpretations

> Variable-specific available-case bases may have been intended.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.14280::C005 |
| legacyRelationship |  |
| locations | DOC-001, Table 1, Patient alcohol use, both arms. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Alcohol-use counts and percentages reconcile to 475/482 rather than Table 1 arm headers. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Alcohol-use counts and percentages reconcile to 475/482 rather than Table 1 arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Alcohol-use categories use undisclosed denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**ICU-admission categories use undisclosed denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 1, Reason for ICU admission, both arms.

### Candidate statement

> Surgical/medical ICU-admission counts and percentages reconcile to 475/482 rather than arm headers.

### AI rationale

> Surgical/medical ICU-admission counts and percentages reconcile to 475/482 rather than arm headers. The focal mismatch is within the main article.

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

> Main article — PDF p. 5 prints surgical 82 (17.3), medical 393 (82.7), and intermediate 79 (16.4), 403 (83.6).

#### Evidence 1: Reported-versus-comparator

> Binary-category totals versus Table 1 arm headers.

#### Evidence 2: Calculation

> 82+393=475, 79+403=482; 82/475=17.3%, 79/482=16.4%.

#### Evidence 3: Alternative source-grounded interpretations

> Surgical/medical status may exist only for 475/482 patients.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C006 |
| key | 2018::jama.2018.14280::C006 |
| legacyRelationship |  |
| locations | DOC-001, Table 1, Reason for ICU admission, both arms. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Surgical/medical ICU-admission counts and percentages reconcile to 475/482 rather than arm headers. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Surgical/medical ICU-admission counts and percentages reconcile to 475/482 rather than arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | ICU-admission categories use undisclosed denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C007

**Sedative-infusion percentages omit effective denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3, eTable 4, Sedative infusion.

### Candidate statement

> Sedative-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers.

### AI rationale

> Sedative-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers. The focal mismatch is within one non-plan results supplement.

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

> Supplement 3 — PDF p. 8 prints 320 (70.6) and 333 (72.1) under headers 477/484.

#### Evidence 1: Reported-versus-comparator

> Printed percentages versus arm-header and recovered available-case denominators.

#### Evidence 2: Calculation

> 320/477=67.1%, 333/484=68.8%; 320/453=70.6%, 333/462=72.1%.

#### Evidence 3: Alternative source-grounded interpretations

> A complete-case subset may apply; eTable 4 uses reduced denominators elsewhere.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C007 |
| key | 2018::jama.2018.14280::C007 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3, eTable 4, Sedative infusion. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Sedative-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Sedative-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Sedative-infusion percentages omit effective denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Analgesic-infusion percentages omit effective denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3, eTable 4, Analgesic infusion.

### Candidate statement

> Analgesic-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers.

### AI rationale

> Analgesic-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers. The focal mismatch is within one non-plan results supplement.

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

> Supplement 3 — PDF p. 8 prints 277 (61.1) and 273 (59.1).

#### Evidence 1: Reported-versus-comparator

> Printed percentages versus header and recovered denominator calculations.

#### Evidence 2: Calculation

> 277/477=58.1%, 273/484=56.4%; 277/453=61.1%, 273/462=59.1%.

#### Evidence 3: Alternative source-grounded interpretations

> A 453/462 complete-case population may be intended.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C008 |
| key | 2018::jama.2018.14280::C008 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3, eTable 4, Analgesic infusion. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Analgesic-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | Analgesic-infusion percentages reproduce from unprinted 453/462 denominators, not arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Analgesic-infusion percentages omit effective denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C009

**Neuromuscular-blockade percentages omit effective denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3, eTable 4, Neuromuscular blockade.

### Candidate statement

> Neuromuscular-blockade percentages reproduce from unprinted 453/462 denominators, not arm headers.

### AI rationale

> Neuromuscular-blockade percentages reproduce from unprinted 453/462 denominators, not arm headers. The focal mismatch is within one non-plan results supplement.

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

> Supplement 3 — PDF p. 8 prints 53 (11.7) and 60 (13.0).

#### Evidence 1: Reported-versus-comparator

> Printed percentages versus arm-header and recovered denominator calculations.

#### Evidence 2: Calculation

> 53/477=11.1%, 60/484=12.4%; 53/453=11.7%, 60/462=13.0%.

#### Evidence 3: Alternative source-grounded interpretations

> A 453/462 available-case subset may be used.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C009 |
| key | 2018::jama.2018.14280::C009 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3, eTable 4, Neuromuscular blockade. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Neuromuscular-blockade percentages reproduce from unprinted 453/462 denominators, not arm headers. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | Neuromuscular-blockade percentages reproduce from unprinted 453/462 denominators, not arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Neuromuscular-blockade percentages omit effective denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C010

**Vasopressor-use percentages omit effective denominators**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C010 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3, eTable 4, Use of vasopressors.

### Candidate statement

> Vasopressor-use percentages reproduce from 454/462, not displayed arm headers.

### AI rationale

> Vasopressor-use percentages reproduce from 454/462, not displayed arm headers. The focal mismatch is within one non-plan results supplement.

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

> Supplement 3 — PDF p. 8 prints 363 (80.0) and 353 (76.4).

#### Evidence 1: Reported-versus-comparator

> Printed percentages versus header and recoverable denominator calculations.

#### Evidence 2: Calculation

> 363/477=76.1%, 353/484=72.9%; 363/454=80.0%, 353/462=76.4%.

#### Evidence 3: Alternative source-grounded interpretations

> Different available-case subsets may have been used; the source does not state whether nearby subsets are shared.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C010 |
| key | 2018::jama.2018.14280::C010 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3, eTable 4, Use of vasopressors. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Vasopressor-use percentages reproduce from 454/462, not displayed arm headers. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | Vasopressor-use percentages reproduce from 454/462, not displayed arm headers. |
| submissionInvolved | 1 |
| subtype | undisclosed\_denominator |
| suggestedDomain | statistical\_results |
| title | Vasopressor-use percentages omit effective denominators |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C011

**Mortality effect-measure wording conflicts with Table 2 and the SAP**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Statistical Analysis and Table 2/footnotes; DOC-003 SAP secondary outcomes.

### Candidate statement

> The main Methods wording can assign Cox HRs to ICU/hospital mortality, while Table 2 and the SAP assign RRs.

### AI rationale

> Main Methods broadly assigns mortality Cox HRs while main Table 2 labels ICU/hospital mortality RR. The SAP agrees with Table 2 and is corroboration of a Methods-versus-results wording discrepancy inside the main article.

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

> Main article Methods — PDF p. 4, Table 2 — PDF p. 6, and SAP — PDF p. 13.

#### Evidence 1: Reported-versus-comparator

> Methods says mortality rates were compared with Kaplan-Meier/Cox HRs; Table 2/SAP specify RR for ICU/hospital mortality and HR for 28/90-day mortality.

#### Evidence 2: Calculation

> Semantic comparison: Methods -\> HR/Cox if read broadly; Table 2 and SAP -\> RR/Wald for ICU/hospital mortality.

#### Evidence 3: Alternative source-grounded interpretations

> The Methods sentence may be overbroad and intended Cox only for time-indexed mortality.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The Methods sentence may intend only time-indexed 28/90-day mortality. No independent report-versus-plan departure is counted merely because SAP wording supports the table. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C011 |
| key | 2018::jama.2018.14280::C011 |
| legacyRelationship |  |
| locations | DOC-001 Statistical Analysis and Table 2/footnotes; DOC-003 SAP secondary outcomes. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Methods broadly assigns mortality Cox HRs while main Table 2 labels ICU/hospital mortality RR. The SAP agrees with Table 2 and is corroboration of a Methods-versus-results wording discrepancy inside the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | The main Methods wording can assign Cox HRs to ICU/hospital mortality, while Table 2 and the SAP assign RRs. |
| submissionInvolved | 1 |
| subtype | effect\_measure\_methods\_vs\_table |
| suggestedDomain | report\_internal\_inconsistency |
| title | Mortality effect-measure wording conflicts with Table 2 and the SAP |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C012

**ICU-mortality RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, ICU mortality and footnote c.

### Candidate statement

> Printed ICU-mortality RR 1.11 does not reproduce as the crude low/intermediate ratio from displayed risks.

### AI rationale

> Printed ICU-mortality RR 1.11 does not reproduce as the crude low/intermediate ratio from displayed risks. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints low 132/450 (29.3), intermediate 115/458 (25.1), and RR, 1.11 (0.96-1.27).

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.11 versus crude ratio of printed risks.

#### Evidence 2: Calculation

> (132/450)/(115/458)=1.168231884, rounding to 1.17, not 1.11.

#### Evidence 3: Alternative source-grounded interpretations

> A non-crude estimator, different population, weighting, or strata may underlie 1.11.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C012 |
| key | 2018::jama.2018.14280::C012 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, ICU mortality and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed ICU-mortality RR 1.11 does not reproduce as the crude low/intermediate ratio from displayed risks. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed ICU-mortality RR 1.11 does not reproduce as the crude low/intermediate ratio from displayed risks. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | ICU-mortality RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C013

**Hospital-mortality RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C013 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, hospital mortality and footnote c.

### Candidate statement

> Printed hospital-mortality RR 1.06 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed hospital-mortality RR 1.06 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints low 151/477 (31.7), intermediate 140/484 (28.9), and RR 1.06.

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.06 versus displayed-risk ratio.

#### Evidence 2: Calculation

> (151/477)/(140/484)=1.094399521, rounding to 1.09, not 1.06.

#### Evidence 3: Alternative source-grounded interpretations

> A differently defined estimator or analysis population may underlie the printed RR.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C013 |
| key | 2018::jama.2018.14280::C013 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, hospital mortality and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed hospital-mortality RR 1.06 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed hospital-mortality RR 1.06 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Hospital-mortality RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C014

**ARDS RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C014 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Development of ARDS and footnote c.

### Candidate statement

> Printed ARDS RR 0.86 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed ARDS RR 0.86 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 17/448 (3.8), 23/462 (5.0), and RR 0.86.

#### Evidence 1: Reported-versus-comparator

> Reported RR 0.86 versus printed-risk ratio.

#### Evidence 2: Calculation

> (17/448)/(23/462)=0.762228261, rounding to 0.76, not 0.86.

#### Evidence 3: Alternative source-grounded interpretations

> A model- or test-derived RR beyond displayed margins may have been used but is not described.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C014 |
| key | 2018::jama.2018.14280::C014 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Development of ARDS and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed ARDS RR 0.86 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C014 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed ARDS RR 0.86 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | ARDS RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C015

**Pneumonia RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C015 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Development of pneumonia and footnote c.

### Candidate statement

> Printed pneumonia RR 1.07 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed pneumonia RR 1.07 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 19/450 (4.2), 17/462 (3.7), and RR 1.07.

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.07 versus printed-risk ratio.

#### Evidence 2: Calculation

> (19/450)/(17/462)=1.147450980, rounding to 1.15, not 1.07.

#### Evidence 3: Alternative source-grounded interpretations

> A procedure using information beyond displayed margins is possible but not described.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C015 |
| key | 2018::jama.2018.14280::C015 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Development of pneumonia and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed pneumonia RR 1.07 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C015 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed pneumonia RR 1.07 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Pneumonia RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C016

**Pneumothorax RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C016 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Pneumothorax and footnote c.

### Candidate statement

> Printed pneumothorax RR 1.16 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed pneumothorax RR 1.16 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 8/448 (1.8), 6/462 (1.3), and RR 1.16.

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.16 versus printed-risk ratio.

#### Evidence 2: Calculation

> (8/448)/(6/462)=1.375, rounding to 1.38, not 1.16.

#### Evidence 3: Alternative source-grounded interpretations

> A model or test using unprinted information may produce a different effect.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C016 |
| key | 2018::jama.2018.14280::C016 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Pneumothorax and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed pneumothorax RR 1.16 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C016 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed pneumothorax RR 1.16 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Pneumothorax RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C017

**Atelectasis RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C017 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Atelectasis and footnote c.

### Candidate statement

> Printed atelectasis RR 1.00 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed atelectasis RR 1.00 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 51/449 (11.4), 52/464 (11.2), and RR 1.00.

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.00 versus printed-risk ratio.

#### Evidence 2: Calculation

> (51/449)/(52/464)=1.013534350, rounding to 1.01, not 1.00.

#### Evidence 3: Alternative source-grounded interpretations

> A separately estimated or more heavily rounded effect could print as 1.00, but the source does not disclose the computation.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C017 |
| key | 2018::jama.2018.14280::C017 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Atelectasis and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed atelectasis RR 1.00 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C017 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed atelectasis RR 1.00 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Atelectasis RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C018

**Extrapulmonary-infection RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C018 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Extrapulmonary infection and footnote c.

### Candidate statement

> Printed extrapulmonary-infection RR 0.84 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed extrapulmonary-infection RR 0.84 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 20/448 (4.5), 28/463 (6.0), and RR 0.84.

#### Evidence 1: Reported-versus-comparator

> Reported RR 0.84 versus printed-risk ratio.

#### Evidence 2: Calculation

> (20/448)/(28/463)=0.738201531, rounding to 0.74, not 0.84.

#### Evidence 3: Alternative source-grounded interpretations

> An unspecified procedure beyond the margins could yield the printed RR.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C018 |
| key | 2018::jama.2018.14280::C018 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Extrapulmonary infection and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed extrapulmonary-infection RR 0.84 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C018 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed extrapulmonary-infection RR 0.84 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Extrapulmonary-infection RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C019

**Extrapulmonary-sepsis RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C019 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Extrapulmonary sepsis and footnote c.

### Candidate statement

> Printed extrapulmonary-sepsis RR 0.87 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed extrapulmonary-sepsis RR 0.87 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 12/448 (2.7), 16/463 (3.5), and RR 0.87.

#### Evidence 1: Reported-versus-comparator

> Reported RR 0.87 versus printed-risk ratio.

#### Evidence 2: Calculation

> (12/448)/(16/463)=0.775111607, rounding to 0.78, not 0.87.

#### Evidence 3: Alternative source-grounded interpretations

> A non-crude RR may differ from table margins, but no implementation is identified.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C019 |
| key | 2018::jama.2018.14280::C019 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Extrapulmonary sepsis and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed extrapulmonary-sepsis RR 0.87 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C019 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed extrapulmonary-sepsis RR 0.87 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Extrapulmonary-sepsis RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C020

**Delirium RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C020 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Delirium and footnote c.

### Candidate statement

> Printed delirium RR 1.15 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed delirium RR 1.15 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 149/343 (43.4), 132/361 (36.6), and RR 1.15.

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.15 versus printed-risk ratio.

#### Evidence 2: Calculation

> (149/343)/(132/361)=1.188024560, rounding to 1.19, not 1.15.

#### Evidence 3: Alternative source-grounded interpretations

> A non-crude analysis or population not fully represented by margins may yield another RR.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C020 |
| key | 2018::jama.2018.14280::C020 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Delirium and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed delirium RR 1.15 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C020 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed delirium RR 1.15 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Delirium RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C021

**Tracheostomy RR does not reproduce from printed risks**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C021 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, Table 2, Need for tracheostomy and footnote c.

### Candidate statement

> Printed tracheostomy RR 1.03 does not reproduce from displayed risks under the crude comparator.

### AI rationale

> Printed tracheostomy RR 1.03 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article.

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

> Main article — PDF p. 6 prints 54/477 (11.3), 52/484 (10.7), and RR 1.03.

#### Evidence 1: Reported-versus-comparator

> Reported RR 1.03 versus printed-risk ratio.

#### Evidence 2: Calculation

> (54/477)/(52/484)=1.053701016, rounding to 1.05, not 1.03.

#### Evidence 3: Alternative source-grounded interpretations

> A procedure not reducible to displayed margins may have been used, but it is not specified.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Diagnostic comparison assumes the printed RR is crude; the exact estimator, weighting, or analysis population is not supplied. These are separate outcome rows, not proven instances of a single underlying coding error. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C021 |
| key | 2018::jama.2018.14280::C021 |
| legacyRelationship |  |
| locations | DOC-001, Table 2, Need for tracheostomy and footnote c. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_W |
| rationale | Printed tracheostomy RR 1.03 does not reproduce from displayed risks under the crude comparator. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C021 |
| sourceStatus | Pending Human Adjudication |
| statement | Printed tracheostomy RR 1.03 does not reproduce from displayed risks under the crude comparator. |
| submissionInvolved | 1 |
| subtype | rr\_vs\_displayed\_risks |
| suggestedDomain | statistical\_results |
| title | Tracheostomy RR does not reproduce from printed risks |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C022

**The same subgroup intervals are labelled IQR and 95% CI**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C022 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, Subgroups and Exploratory Analyses; DOC-004, Supplement 3 eTable 5.

### Candidate statement

> Identical subgroup intervals are labelled IQR in the main text and 95% CI in eTable 5.

### AI rationale

> Identical subgroup intervals are labelled IQR in the main text and 95% CI in eTable 5. The focal comparison is the main article versus a non-plan results supplement.

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

> Main article — PDF p. 6 prints inside-ICU -2.50 \[IQR, -4.63 to -0.36\] and outside-ICU 1.45 \[IQR, -0.52 to 3.43\]; Supplement 3 — PDF p. 9 labels the identical values Mean Difference (95% CI).

#### Evidence 1: Reported-versus-comparator

> Main-text IQR labels versus eTable 5 95% CI labels for identical point estimates and endpoints.

#### Evidence 2: Calculation

> Both sources show -2.50 (-4.63 to -0.36) and 1.45 (-0.52 to 3.43); only IQR versus 95% CI differs.

#### Evidence 3: Alternative source-grounded interpretations

> The narrative label may be a transcription error; the supplied sources do not establish intended wording.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C022 |
| key | 2018::jama.2018.14280::C022 |
| legacyRelationship |  |
| locations | DOC-001, Subgroups and Exploratory Analyses; DOC-004, Supplement 3 eTable 5. |
| originalCrossDocument | 0 |
| package | jama.2018.14280 |
| planMechanism |  |
| primary | S\_C |
| rationale | Identical subgroup intervals are labelled IQR in the main text and 95% CI in eTable 5. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C022 |
| sourceStatus | Pending Human Adjudication |
| statement | Identical subgroup intervals are labelled IQR in the main text and 95% CI in eTable 5. |
| submissionInvolved | 1 |
| subtype | iqr\_vs\_ci\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | The same subgroup intervals are labelled IQR and 95% CI |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C023

**Enrollment completion dates differ by two days**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.14280::C023 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-001 abstract and Results/Patients; DOC-003 SAP abstract and introduction.

### Candidate statement

> The main article reports enrollment through August 20, 2017, while the SAP reports enrollment complete on August 22, 2017.

### AI rationale

> The main article gives August 20, 2017 as enrollment end, whereas the supplied SAP/update gives August 22, 2017. This is a main-report versus SAP factual date discrepancy, rather than an ordinary results-supplement discrepancy.

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

> Main article abstract — PDF p. 1 and Results/Patients — PDF p. 5 print August 20, 2017. SAP abstract — PDF p. 3 and SAP introduction — PDF p. 5 print August 22, 2017.

#### Evidence 1: Reported-versus-comparator

> Main-article enrollment end date August 20, 2017 versus SAP enrollment-completion date August 22, 2017.

#### Evidence 2: Calculation

> August 22, 2017 is two calendar days after August 20, 2017.

#### Evidence 3: Alternative source-grounded interpretations

> August 20 may be the last screened/enrolled/randomized patient and August 22 administrative completion; the supplied sources do not define distinct events.

### Source links

- evidencePaths 0: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.14280/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.14280/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.14280/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The SAP is an update after enrollment; clinical last-patient date versus administrative completion could explain the two days. P\_R denotes document roles, not a proven prospective-plan violation. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C023 |
| key | 2018::jama.2018.14280::C023 |
| legacyRelationship |  |
| locations | DOC-001 abstract and Results/Patients; DOC-003 SAP abstract and introduction. |
| originalCrossDocument | 1 |
| package | jama.2018.14280 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | The main article gives August 20, 2017 as enrollment end, whereas the supplied SAP/update gives August 22, 2017. This is a main-report versus SAP factual date discrepancy, rather than an ordinary results-supplement discrepancy. |
| reportHref | ../../2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.14280/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C023 |
| sourceStatus | Pending Human Adjudication |
| statement | The main article reports enrollment through August 20, 2017, while the SAP reports enrollment complete on August 22, 2017. |
| submissionInvolved | 0 |
| subtype | enrollment\_end\_date |
| suggestedDomain | protocol\_report |
| title | Enrollment completion dates differ by two days |
| year | 2018 |
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
