# jama.2018.8802

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.8802 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.8802/)

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

- [C001](#candidate-c001) — Table 1 CAD/previous-myocardial-infarction percentage does not reproduce (S_W)
- [C002](#candidate-c002) — LDL eligibility boundary differs between result labels and supplied measure definition (P_R)
- [C003](#candidate-c003) — eTable 4 discharge-antithrombotics control percentage does not reproduce (S_W)
- [C004](#candidate-c004) — eTable 4 AF-anticoagulation control percentage does not reproduce (S_W)
- [C005](#candidate-c005) — eTable 4 lipid-lowering control percentage does not reproduce (S_W)
- [C006](#candidate-c006) — eTable 4 antidiabetic-medication control percentage does not reproduce (S_W)
- [C007](#candidate-c007) — baseline-survey patient total does not reconcile with stated per-cluster inclusion (S_C)
- [C008](#candidate-c008) — in-hospital death absolute-difference CI and P value do not reconcile (S_W)

## Candidate C001

**Table 1 CAD/previous-myocardial-infarction percentage does not reproduce**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_wang\_2018\_oi\_180070.pdf — PDF p. 6, Table 1, CAD/previous myocardial infarction, intervention column and Patients, No. header.

### Candidate statement

> The intervention cell prints 311 (13.05) under a 2,400-patient column, but the displayed fraction does not yield 13.05%.

### AI rationale

> The intervention cell prints 311 (13.05) under a 2,400-patient column, but the displayed fraction does not yield 13.05%. The focal mismatch is within the main article.

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

> The direct PDF prints intervention Patients, No. = 2400 and the row cell 311 (13.05).

#### Evidence 1: Reported-versus-comparator

> Reported 13.05% versus 311/2400.

#### Evidence 2: Calculation

> 311 / 2400 × 100 = 12.9583%, which rounds to 13.0% at one decimal or 12.96% at two decimals, not 13.05%.

#### Evidence 3: Alternative source-grounded interpretations

> A row-specific denominator or nonstandard calculation may have been used, but neither is supplied.

### Source links

- sourceLinks 0: [jama\_wang\_2018\_oi\_180070.pdf — PDF p. 6](../../../2018/jama.2018.8802/jama_wang_2018_oi_180070.pdf#page=6)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.8802::C001 |
| legacyRelationship |  |
| locations | jama\_wang\_2018\_oi\_180070.pdf — PDF p. 6, Table 1, CAD/previous myocardial infarction, intervention column and Patients, No. header. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_W |
| rationale | The intervention cell prints 311 (13.05) under a 2,400-patient column, but the displayed fraction does not yield 13.05%. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention cell prints 311 (13.05) under a 2,400-patient column, but the displayed fraction does not yield 13.05%. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Table 1 CAD/previous-myocardial-infarction percentage does not reproduce |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**LDL eligibility boundary differs between result labels and supplied measure definition**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C002 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> jama\_wang\_2018\_oi\_180070.pdf — PDF p. 7, Table 2 lipid-lowering row; joi180070supp1\_prod.pdf — PDF p. 15, definition; joi180070supp2\_prod.pdf — PDF p. 3, eTable 1 definition; and joi180070supp2\_prod.pdf — PDF p. 8, eTable 4 label.

### Candidate statement

> The main and sensitivity result rows use LDL \>100 mg/dL, while supplied formal measure definitions use LDL ≥100 mg/dL.

### AI rationale

> Main Table 2 and the sensitivity-results eTable use LDL \>100; the protocol formal definition and results-supplement eTable 1 use \>=100. The target is eligibility as formally defined versus attached to reported results, giving P\_R; the main-versus-results-definition and within-supplement definition/label differences also substantively occur.

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

> The result labels print \>100 mg/dL; both supplied definitions print ≥100 mg/dL with additional eligibility conditions.

#### Evidence 1: Reported-versus-comparator

> A strict threshold excludes LDL exactly 100 mg/dL; an inclusive threshold includes it.

#### Evidence 2: Calculation

> \>100 ≠ ≥100; no rounding tolerance applies.

#### Evidence 3: Alternative source-grounded interpretations

> The result-row wording may be abbreviated while the formal inclusive definition governed eligibility; the supplied package does not state this.

### Source links

- sourceLinks 0: [jama\_wang\_2018\_oi\_180070.pdf — PDF p. 7](../../../2018/jama.2018.8802/jama_wang_2018_oi_180070.pdf#page=7)
- sourceLinks 1: [joi180070supp1\_prod.pdf — PDF p. 15](../../../2018/jama.2018.8802/joi180070supp1_prod.pdf#page=15)
- sourceLinks 2: [joi180070supp2\_prod.pdf — PDF p. 3](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=3)
- sourceLinks 3: [joi180070supp2\_prod.pdf — PDF p. 8](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |
| relations | 1 | S\_C |
| relations | 2 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Mixed planned/reported and submission-internal definition relationships. Labels may be abbreviations while the inclusive definition governed the denominators; participant-level LDL-at-100 data are absent. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2018::jama.2018.8802::C002 |
| legacyRelationship |  |
| locations | jama\_wang\_2018\_oi\_180070.pdf — PDF p. 7, Table 2 lipid-lowering row; joi180070supp1\_prod.pdf — PDF p. 15, definition; joi180070supp2\_prod.pdf — PDF p. 3, eTable 1 definition; and joi180070supp2\_prod.pdf — PDF p. 8, eTable 4 label. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | Main Table 2 and the sensitivity-results eTable use LDL \>100; the protocol formal definition and results-supplement eTable 1 use \>=100. The target is eligibility as formally defined versus attached to reported results, giving P\_R; the main-versus-results-definition and within-supplement definition/label differences also substantively occur. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The main and sensitivity result rows use LDL \>100 mg/dL, while supplied formal measure definitions use LDL ≥100 mg/dL. |
| submissionInvolved | 1 |
| subtype | eligibility\_threshold |
| suggestedDomain | protocol\_report |
| title | LDL eligibility boundary differs between result labels and supplied measure definition |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C003

**eTable 4 discharge-antithrombotics control percentage does not reproduce**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Antithrombotics, control cell.

### Candidate statement

> The control cell prints 2141/2400 (89.3), but the fraction rounds to 89.2% at one decimal.

### AI rationale

> The control cell prints 2141/2400 (89.3), but the fraction rounds to 89.2% at one decimal. The focal mismatch is within one non-plan results supplement.

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

> The cell under No. / Total (%) prints 2141/2400 (89.3).

#### Evidence 1: Reported-versus-comparator

> Reported 89.3% versus fraction-derived 89.2083%.

#### Evidence 2: Calculation

> 2141 / 2400 × 100 = 89.2083%, which rounds to 89.2%; the nearest-tenth interval for 89.3% begins at 89.25%.

#### Evidence 3: Alternative source-grounded interpretations

> No alternative denominator or rounding convention is supplied; the header defines the displayed fraction.

### Source links

- sourceLinks 0: [joi180070supp2\_prod.pdf — PDF p. 8](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.8802::C003 |
| legacyRelationship |  |
| locations | joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Antithrombotics, control cell. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_W |
| rationale | The control cell prints 2141/2400 (89.3), but the fraction rounds to 89.2% at one decimal. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The control cell prints 2141/2400 (89.3), but the fraction rounds to 89.2% at one decimal. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable 4 discharge-antithrombotics control percentage does not reproduce |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**eTable 4 AF-anticoagulation control percentage does not reproduce**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Anticoagulation for Atrial Fibrillation, control cell.

### Candidate statement

> The control cell prints 39/174 (22.5), but the fraction rounds to 22.4% at one decimal.

### AI rationale

> The control cell prints 39/174 (22.5), but the fraction rounds to 22.4% at one decimal. The focal mismatch is within one non-plan results supplement.

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

> The direct PDF prints 39/174 (22.5) beneath No. / Total (%).

#### Evidence 1: Reported-versus-comparator

> Reported 22.5% versus fraction-derived 22.4138%.

#### Evidence 2: Calculation

> 39 / 174 × 100 = 22.4138%, which rounds to 22.4%, below the 22.45% lower boundary for 22.5%.

#### Evidence 3: Alternative source-grounded interpretations

> No alternative denominator or rounding convention is supplied.

### Source links

- sourceLinks 0: [joi180070supp2\_prod.pdf — PDF p. 8](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.8802::C004 |
| legacyRelationship |  |
| locations | joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Anticoagulation for Atrial Fibrillation, control cell. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_W |
| rationale | The control cell prints 39/174 (22.5), but the fraction rounds to 22.4% at one decimal. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The control cell prints 39/174 (22.5), but the fraction rounds to 22.4% at one decimal. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable 4 AF-anticoagulation control percentage does not reproduce |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**eTable 4 lipid-lowering control percentage does not reproduce**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Lipid-lowering for LDL \>100 mg/dL, control cell.

### Candidate statement

> The control cell prints 1439/1586 (90.8), but the fraction rounds to 90.7% at one decimal.

### AI rationale

> The control cell prints 1439/1586 (90.8), but the fraction rounds to 90.7% at one decimal. The focal mismatch is within one non-plan results supplement.

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

> The direct PDF prints 1439/1586 (90.8) beneath No. / Total (%).

#### Evidence 1: Reported-versus-comparator

> Reported 90.8% versus fraction-derived 90.7314%.

#### Evidence 2: Calculation

> 1439 / 1586 × 100 = 90.7314%, which rounds to 90.7%, below the 90.75% lower boundary for 90.8%.

#### Evidence 3: Alternative source-grounded interpretations

> No alternative denominator or rounding convention is supplied; C002 is a separate label/definition comparator.

### Source links

- sourceLinks 0: [joi180070supp2\_prod.pdf — PDF p. 8](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.8802::C005 |
| legacyRelationship |  |
| locations | joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Lipid-lowering for LDL \>100 mg/dL, control cell. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_W |
| rationale | The control cell prints 1439/1586 (90.8), but the fraction rounds to 90.7% at one decimal. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The control cell prints 1439/1586 (90.8), but the fraction rounds to 90.7% at one decimal. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable 4 lipid-lowering control percentage does not reproduce |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**eTable 4 antidiabetic-medication control percentage does not reproduce**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Antidiabetic Medication, control cell.

### Candidate statement

> The control cell prints 557/688 (81.1), but the fraction rounds to 81.0% at one decimal.

### AI rationale

> The control cell prints 557/688 (81.1), but the fraction rounds to 81.0% at one decimal. The focal mismatch is within one non-plan results supplement.

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

> The direct PDF prints 557/688 (81.1) beneath No. / Total (%).

#### Evidence 1: Reported-versus-comparator

> Reported 81.1% versus fraction-derived 80.9593%.

#### Evidence 2: Calculation

> 557 / 688 × 100 = 80.9593%, which rounds to 81.0%, below the 81.05% lower boundary for 81.1%.

#### Evidence 3: Alternative source-grounded interpretations

> No alternative denominator or rounding convention is supplied.

### Source links

- sourceLinks 0: [joi180070supp2\_prod.pdf — PDF p. 8](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=8)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.8802::C006 |
| legacyRelationship |  |
| locations | joi180070supp2\_prod.pdf — PDF p. 8, eTable 4, Antidiabetic Medication, control cell. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_W |
| rationale | The control cell prints 557/688 (81.1), but the fraction rounds to 81.0% at one decimal. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The control cell prints 557/688 (81.1), but the fraction rounds to 81.0% at one decimal. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_rounding |
| suggestedDomain | statistical\_results |
| title | eTable 4 antidiabetic-medication control percentage does not reproduce |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C007

**baseline-survey patient total does not reconcile with stated per-cluster inclusion**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C007 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_wang\_2018\_oi\_180070.pdf — PDF p. 6, Table 1 baseline-survey Hospitals, No. = 40 and Patients, No. = 801; joi180070supp2\_prod.pdf — PDF p. 2, eAppendix baseline-survey statement; jama\_wang\_2018\_oi\_180070.pdf — PDF p. 5, Figure 1; joi180070supp1\_prod.pdf — PDF p. 4 and PDF p. 7, 40-cluster statements.

### Candidate statement

> Table 1 reports 801 baseline-survey patients and 40 survey hospitals, while the supplement states that 20 patients per cluster were prospectively included, implying 800 under an exact fixed-count reading.

### AI rationale

> Main Table 1 reports 801 baseline-survey patients in 40 hospitals, while the ordinary results-supplement eAppendix says 20 patients per cluster were included, implying 800. Protocol 40-cluster statements corroborate the cluster count; the discrepant total versus per-cluster inclusion claim is main versus non-plan supplement.

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

> Table 1 prints 40 hospitals and 801 patients in the baseline-survey column; the eAppendix prints 20 patients per cluster were prospectively included.

#### Evidence 1: Reported-versus-comparator

> Reported total 801 versus 20 × 40 = 800 under the stated same-survey, exact-count interpretation.

#### Evidence 2: Calculation

> 20 × 40 = 800; the difference from the Table 1 total is one patient.

#### Evidence 3: Alternative source-grounded interpretations

> Twenty may be an operational target rather than exact realized count, or one cluster may have contributed 21 patients; neither qualification is supplied.

### Source links

- sourceLinks 0: [jama\_wang\_2018\_oi\_180070.pdf — PDF p. 6](../../../2018/jama.2018.8802/jama_wang_2018_oi_180070.pdf#page=6)
- sourceLinks 1: [joi180070supp2\_prod.pdf — PDF p. 2](../../../2018/jama.2018.8802/joi180070supp2_prod.pdf#page=2)
- sourceLinks 2: [jama\_wang\_2018\_oi\_180070.pdf — PDF p. 5](../../../2018/jama.2018.8802/jama_wang_2018_oi_180070.pdf#page=5)
- sourceLinks 3: [joi180070supp1\_prod.pdf — PDF p. 4](../../../2018/jama.2018.8802/joi180070supp1_prod.pdf#page=4)
- sourceLinks 4: [PDF p. 7](../../../2018/jama.2018.8802/joi180070supp1_prod.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Twenty may be a target, with one cluster enrolling 21; the printed retrospective inclusion claim lacks that qualification. No additional plan discrepancy is counted. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2018::jama.2018.8802::C007 |
| legacyRelationship |  |
| locations | jama\_wang\_2018\_oi\_180070.pdf — PDF p. 6, Table 1 baseline-survey Hospitals, No. = 40 and Patients, No. = 801; joi180070supp2\_prod.pdf — PDF p. 2, eAppendix baseline-survey statement; jama\_wang\_2018\_oi\_180070.pdf — PDF p. 5, Figure 1; joi180070supp1\_prod.pdf — PDF p. 4 and PDF p. 7, 40-cluster statements. |
| originalCrossDocument | 1 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Table 1 reports 801 baseline-survey patients in 40 hospitals, while the ordinary results-supplement eAppendix says 20 patients per cluster were included, implying 800. Protocol 40-cluster statements corroborate the cluster count; the discrepant total versus per-cluster inclusion claim is main versus non-plan supplement. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1 reports 801 baseline-survey patients and 40 survey hospitals, while the supplement states that 20 patients per cluster were prospectively included, implying 800 under an exact fixed-count reading. |
| submissionInvolved | 1 |
| subtype | sampling\_count\_vs\_total |
| suggestedDomain | report\_internal\_inconsistency |
| title | baseline-survey patient total does not reconcile with stated per-cluster inclusion |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C008

**in-hospital death absolute-difference CI and P value do not reconcile**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.8802::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_wang\_2018\_oi\_180070.pdf — PDF p. 8, Table 3 Death / In hospital row, absolute-difference and adjacent P-value columns; jama\_wang\_2018\_oi\_180070.pdf — PDF p. 4, data-analysis statements.

### Candidate statement

> The in-hospital-death adjusted absolute-difference 95% CI contains zero, while the adjacent absolute-difference P-value cell is .009 under the article's two-sided testing statement.

### AI rationale

> The in-hospital-death adjusted absolute-difference 95% CI contains zero, while the adjacent absolute-difference P-value cell is .009 under the article's two-sided testing statement. The focal mismatch is within the main article.

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

> Table 3 prints adjusted absolute difference −0.7% with 95% CI −1.1% to 0.2% and adjacent .009; page 4 describes adjusted absolute differences, 95% CIs, and two-sided tests.

#### Evidence 1: Reported-versus-comparator

> The CI includes zero, while .009 \< .05 for the corresponding adjacent absolute-difference pairing.

#### Evidence 2: Calculation

> −1.1 \< 0 \< 0.2, so zero is inside the printed CI; .009 \< .05.

#### Evidence 3: Alternative source-grounded interpretations

> The P value may use a different estimand, model, or inferential construction, but the table places it adjacent to the absolute-difference column and supplies no distinction.

### Source links

- sourceLinks 0: [jama\_wang\_2018\_oi\_180070.pdf — PDF p. 8](../../../2018/jama.2018.8802/jama_wang_2018_oi_180070.pdf#page=8)
- sourceLinks 1: [jama\_wang\_2018\_oi\_180070.pdf — PDF p. 4](../../../2018/jama.2018.8802/jama_wang_2018_oi_180070.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.8802/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.8802/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.8802/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C008 |
| key | 2018::jama.2018.8802::C008 |
| legacyRelationship |  |
| locations | jama\_wang\_2018\_oi\_180070.pdf — PDF p. 8, Table 3 Death / In hospital row, absolute-difference and adjacent P-value columns; jama\_wang\_2018\_oi\_180070.pdf — PDF p. 4, data-analysis statements. |
| originalCrossDocument | 0 |
| package | jama.2018.8802 |
| planMechanism |  |
| primary | S\_W |
| rationale | The in-hospital-death adjusted absolute-difference 95% CI contains zero, while the adjacent absolute-difference P-value cell is .009 under the article's two-sided testing statement. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.8802/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The in-hospital-death adjusted absolute-difference 95% CI contains zero, while the adjacent absolute-difference P-value cell is .009 under the article's two-sided testing statement. |
| submissionInvolved | 1 |
| subtype | ci\_p\_compatibility |
| suggestedDomain | statistical\_results |
| title | in-hospital death absolute-difference CI and P value do not reconcile |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
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
