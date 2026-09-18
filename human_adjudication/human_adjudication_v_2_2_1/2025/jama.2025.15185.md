# jama.2025.15185

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.15185 |
| Candidates | 12 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.15185/)

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

- [C001](#candidate-c001) — Baseline index-stroke type counts differ across baseline tables (S_C)
- [C002](#candidate-c002) — Baseline NIHSS statistic and label do not reconcile across tables (S_C)
- [C003](#candidate-c003) — Time from stroke onset to randomization differs across baseline tables (S_C)
- [C004](#candidate-c004) — Estimand 4 confidence-interval upper endpoint differs within eTable 2 (S_W)
- [C005](#candidate-c005) — Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4 (S_C)
- [C006](#candidate-c006) — PROMIS-10 descriptive means differ between main text and eTable 4 (S_C)
- [C007](#candidate-c007) — Placebo five-week FMA standard deviation differs from eTable 4 (S_C)
- [C008](#candidate-c008) — Placebo PRAI no-improvement numerator differs between main text and eTable 4 (S_C)
- [C009](#candidate-c009) — eTable 6 overall adverse-event total is one below arms and category sums (S_W)
- [C010](#candidate-c010) — eFigure 4 switches locally from FMA to FMMA without qualification (S_W)
- [C011](#candidate-c011) — Estimand 4 win ratio appears under an FMA mean-difference column heading (S_W)
- [C012](#candidate-c012) — Estimand 4 is called an odds ratio in prose and a win ratio in the table (S_W)

## Candidate C001

**Baseline index-stroke type counts differ across baseline tables**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C001 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 4, Table 1; DOC-004, Supplement 3 — PDF p. 10 and PDF p. 11, eTable 1.

### Candidate statement

> The same randomized levodopa arm has different ischemic/hemorrhagic index-stroke counts in two baseline tables. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Main \`260/47\` versus supplement \`263/44\` for the same named arm and categories.

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

> Main Table 1 prints levodopa n=307: ischemic 260 (84.7%), hemorrhagic 47 (15.3%). eTable 1 prints levodopa n=307: ischemic 263 (85.7%), hemorrhagic 44 (14.3%); placebo values match.

#### Evidence 1: Reported-versus-comparator

> Main 260/47 versus supplement 263/44 for the same named arm and categories.

#### Evidence 2: Calculation

> 260 + 47 = 307; 263 + 44 = 307; the category changes are +3/-3 at an unchanged arm total.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated recoding or data cut could explain the difference; neither table identifies one.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4)
- sourceLinks 1: [Supplement 3 — PDF p. 10](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=10)
- sourceLinks 2: [PDF p. 11](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=11)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2025::jama.2025.15185::C001 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 4, Table 1; DOC-004, Supplement 3 — PDF p. 10 and PDF p. 11, eTable 1. |
| originalCrossDocument | 1 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Main \`260/47\` versus supplement \`263/44\` for the same named arm and categories. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The same randomized levodopa arm has different ischemic/hemorrhagic index-stroke counts in two baseline tables. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Baseline index-stroke type counts differ across baseline tables |
| suggestedDomain | report\_internal\_inconsistency |
| title | Baseline index-stroke type counts differ across baseline tables |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**Baseline NIHSS statistic and label do not reconcile across tables**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 4, Table 1, and PDF p. 5, Results; DOC-004, Supplement 3 — PDF p. 11, eTable 1.

### Candidate statement

> eTable 1 labels its NIHSS row as median \[IQR\] but prints a decimal-plus-one-parenthesized-value form that does not identify the same summary as the main table. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. A labelled median/IQR row with two-endpoint main summaries versus one decimal and one parenthesized value in the supplement.

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

> Main values are median (IQR) 7 (5-11) levodopa, 8 (5-10) placebo, and overall 7 (5-10). eTable 1 labels Median NIHSS at randomization \[IQR\] yet prints 8.2 (3.9), 8.3 (3.8), and 8.2 (3.9).

#### Evidence 1: Reported-versus-comparator

> A labelled median/IQR row with two-endpoint main summaries versus one decimal and one parenthesized value in the supplement.

#### Evidence 2: Calculation

> Main summaries contain a central value and two IQR endpoints; each supplement summary has one central decimal and one parenthesized number, so mapping requires a missing definition.

#### Evidence 3: Alternative source-grounded interpretations

> The supplement values may be means (SDs) under a stale label, or may use an unstated one-number convention; neither interpretation is stated there.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4)
- sourceLinks 1: [PDF p. 5](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5)
- sourceLinks 2: [Supplement 3 — PDF p. 11](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=11)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |
| relations | 1 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Internal median/IQR label-form issue and explicit matched main/supp summary comparison. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2025::jama.2025.15185::C002 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 4, Table 1, and PDF p. 5, Results; DOC-004, Supplement 3 — PDF p. 11, eTable 1. |
| originalCrossDocument | 0 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. A labelled median/IQR row with two-endpoint main summaries versus one decimal and one parenthesized value in the supplement. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 1 labels its NIHSS row as median \[IQR\] but prints a decimal-plus-one-parenthesized-value form that does not identify the same summary as the main table. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Baseline NIHSS statistic and label do not reconcile across tables |
| suggestedDomain | report\_internal\_inconsistency |
| title | Baseline NIHSS statistic and label do not reconcile across tables |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Time from stroke onset to randomization differs across baseline tables**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C003 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 4, Table 1; DOC-004, Supplement 3 — PDF p. 11, eTable 1.

### Candidate statement

> Same-named time-to-randomization summaries differ across tables; the supplement omits the unit needed to make the cross-source comparison unconditional. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Main arm medians \`3.0/3.0\` versus supplement \`8/7\` for the same named variable.

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

> Main prints Time from stroke onset to randomization, median (IQR), d: 3.0 (2.0-5.0) for both arms. eTable 1 prints 7 \[5,10\] overall, 8 \[5,10\] placebo, and 7 \[5-11\] levodopa without a visible unit.

#### Evidence 1: Reported-versus-comparator

> Main arm medians 3.0/3.0 versus supplement 8/7 for the same named variable.

#### Evidence 2: Calculation

> If the supplement values are days, levodopa differs by 7-3=4 days and placebo by 8-3=5 days; these are not rounding differences.

#### Evidence 3: Alternative source-grounded interpretations

> A different unstated unit, time origin, derivation, population, or data version may be used.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4)
- sourceLinks 1: [Supplement 3 — PDF p. 11](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=11)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Results-supp unit omitted; day comparison is conditional. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2025::jama.2025.15185::C003 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 4, Table 1; DOC-004, Supplement 3 — PDF p. 11, eTable 1. |
| originalCrossDocument | 1 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Main arm medians \`3.0/3.0\` versus supplement \`8/7\` for the same named variable. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Same-named time-to-randomization summaries differ across tables; the supplement omits the unit needed to make the cross-source comparison unconditional. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Time from stroke onset to randomization differs across baseline tables |
| suggestedDomain | report\_internal\_inconsistency |
| title | Time from stroke onset to randomization differs across baseline tables |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**Estimand 4 confidence-interval upper endpoint differs within eTable 2**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3 — PDF p. 12, eTable 2 narrative; PDF p. 13, Estimand 4 row.

### Candidate statement

> Two matched Estimand 4 displays in eTable 2 have different upper 95% CI endpoints. Pending Human Adjudication.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Identical point estimate/lower endpoint with upper endpoint \`1.25\` versus \`1.26\`.

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

> Narrative: 1.06 (95% CI, 0.86 to 1.25). Matched full-analysis-set composite row: 1.06 \[0.86-1.26\].

#### Evidence 1: Reported-versus-comparator

> Identical point estimate/lower endpoint with upper endpoint 1.25 versus 1.26.

#### Evidence 2: Calculation

> 1.06=1.06, 0.86=0.86, and 1.26-1.25=0.01.

#### Evidence 3: Alternative source-grounded interpretations

> A rounding-boundary or one-hundredth transcription difference is possible; no unrounded output or separate calculation is supplied.

### Source links

- sourceLinks 0: [Supplement 3 — PDF p. 12](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=12)
- sourceLinks 1: [PDF p. 13](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=13)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C004 |
| key | 2025::jama.2025.15185::C004 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3 — PDF p. 12, eTable 2 narrative; PDF p. 13, Estimand 4 row. |
| originalCrossDocument | 0 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Identical point estimate/lower endpoint with upper endpoint \`1.25\` versus \`1.26\`. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Two matched Estimand 4 displays in eTable 2 have different upper 95% CI endpoints. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Estimand 4 confidence-interval upper endpoint differs within eTable 2 |
| suggestedDomain | statistical\_results |
| title | Estimand 4 confidence-interval upper endpoint differs within eTable 2 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C005 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4.

### Candidate statement

> The main-text levodopa PROMIS-29 mean does not follow ordinary whole-number rounding of the matched eTable 4 mean. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Main levodopa \`66 (14)\` versus detailed \`64.74 (14.33)\`.

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

> Main: levodopa 66 (14), placebo 65 (14). eTable: levodopa 64.74 (14.33), placebo 65.11 (13.79), effect -0.37.

#### Evidence 1: Reported-versus-comparator

> Main levodopa 66 (14) versus detailed 64.74 (14.33).

#### Evidence 2: Calculation

> 64.74 rounds to 65, not 66; 64.74-65.11=-0.37, matching the eTable effect.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated scoring transformation, analysis set, or descriptive-versus-model summary could differ.

### Source links

- sourceLinks 0: [main article — PDF p. 6](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)
- sourceLinks 1: [Supplement 3 — PDF p. 15](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=15)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C005 |
| key | 2025::jama.2025.15185::C005 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4. |
| originalCrossDocument | 1 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Main levodopa \`66 (14)\` versus detailed \`64.74 (14.33)\`. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The main-text levodopa PROMIS-29 mean does not follow ordinary whole-number rounding of the matched eTable 4 mean. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4 |
| suggestedDomain | report\_internal\_inconsistency |
| title | Levodopa PROMIS-29 descriptive mean differs between main text and eTable 4 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**PROMIS-10 descriptive means differ between main text and eTable 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4.

### Candidate statement

> Both detailed PROMIS-10 means are near 30, whereas the main text prints 28 for both arms. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Main \`28 (6)\`/\`28 (6)\` versus eTable \`29.87 (5.74)\`/\`30.04 (5.73)\`.

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

> Main prints 28 (6) in both arms. eTable prints placebo 29.87 (5.74) and levodopa 30.04 (5.73), with adjusted effect 0.18.

#### Evidence 1: Reported-versus-comparator

> Main 28 (6)/28 (6) versus eTable 29.87 (5.74)/30.04 (5.73).

#### Evidence 2: Calculation

> 29.87 and 30.04 each round to 30, not 28; 30.04-29.87=0.17, while the labelled adjusted effect is 0.18.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated PROMIS-10 scoring version or analysis population may differ.

### Source links

- sourceLinks 0: [main article — PDF p. 6](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)
- sourceLinks 1: [Supplement 3 — PDF p. 15](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=15)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2025::jama.2025.15185::C006 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4. |
| originalCrossDocument | 1 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Main \`28 (6)\`/\`28 (6)\` versus eTable \`29.87 (5.74)\`/\`30.04 (5.73)\`. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Both detailed PROMIS-10 means are near 30, whereas the main text prints 28 for both arms. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | PROMIS-10 descriptive means differ between main text and eTable 4 |
| suggestedDomain | report\_internal\_inconsistency |
| title | PROMIS-10 descriptive means differ between main text and eTable 4 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Placebo five-week FMA standard deviation differs from eTable 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C007 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4.

### Candidate statement

> The main placebo five-week FMA SD does not follow ordinary whole-number rounding of eTable 4. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Placebo SD \`26\` versus detailed \`25.20\`.

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

> Main placebo mean (SD) is 56 (26); eTable placebo is 56.27 (25.20). Levodopa 57 (27) aligns with 57.37 (26.70).

#### Evidence 1: Reported-versus-comparator

> Placebo SD 26 versus detailed 25.20.

#### Evidence 2: Calculation

> 56.27 rounds to 56; 25.20 rounds to 25, not 26; levodopa 57.37 (26.70) rounds to 57 (27).

#### Evidence 3: Alternative source-grounded interpretations

> An unstated population, imputation summary, or SD convention could differ.

### Source links

- sourceLinks 0: [main article — PDF p. 6](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)
- sourceLinks 1: [Supplement 3 — PDF p. 15](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=15)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2025::jama.2025.15185::C007 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4. |
| originalCrossDocument | 1 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Placebo SD \`26\` versus detailed \`25.20\`. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | The main placebo five-week FMA SD does not follow ordinary whole-number rounding of eTable 4. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Placebo five-week FMA standard deviation differs from eTable 4 |
| suggestedDomain | report\_internal\_inconsistency |
| title | Placebo five-week FMA standard deviation differs from eTable 4 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C008

**Placebo PRAI no-improvement numerator differs between main text and eTable 4**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C008 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4.

### Candidate statement

> The placebo PRAI no-improvement numerator differs by one at the same printed denominator. Pending Human Adjudication.

### AI rationale

> Target explicitly compares current main article and non-plan results supplement/workbook. Same placebo denominator \`270\` with numerator \`52\` versus \`51\`.

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

> Main placebo is 52/270 (19%); eTable placebo is 51 (18.89%) (n=270). Levodopa is 51/276 in both.

#### Evidence 1: Reported-versus-comparator

> Same placebo denominator 270 with numerator 52 versus 51.

#### Evidence 2: Calculation

> 51/270=18.888...%, matching 18.89%; 52/270=19.259...%, compatible with 19%. The printed numerator differs by one.

#### Evidence 3: Alternative source-grounded interpretations

> Different handling of no improvement and no relevant improvement could affect one record, but no distinct rule is supplied.

### Source links

- sourceLinks 0: [main article — PDF p. 6](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)
- sourceLinks 1: [Supplement 3 — PDF p. 15](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=15)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2025::jama.2025.15185::C008 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 6, Secondary Outcomes; DOC-004, Supplement 3 — PDF p. 15, eTable 4. |
| originalCrossDocument | 1 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_C |
| rationale | Target explicitly compares current main article and non-plan results supplement/workbook. Same placebo denominator \`270\` with numerator \`52\` versus \`51\`. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The placebo PRAI no-improvement numerator differs by one at the same printed denominator. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Placebo PRAI no-improvement numerator differs between main text and eTable 4 |
| suggestedDomain | report\_internal\_inconsistency |
| title | Placebo PRAI no-improvement numerator differs between main text and eTable 4 |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C009

**eTable 6 overall adverse-event total is one below arms and category sums**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001, main article — PDF p. 6, Table 2 and narrative, and PDF p. 7; DOC-004, Supplement 3 — PDF p. 17, eTable 6.

### Candidate statement

> eTable 6 prints an overall adverse-event total of 145 although arm and exhaustive category totals are 146. Pending Human Adjudication.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Header \`145\` versus arms and category sums \`146\`.

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

> Main reports 146 events: 79 levodopa and 67 placebo. eTable header gives overall n=145, placebo 67, levodopa 79; its intensity, outcome, and relation rows also provide complete classifications.

#### Evidence 1: Reported-versus-comparator

> Header 145 versus arms and category sums 146.

#### Evidence 2: Calculation

> 67+79=146; intensity 58+86+2=146; outcome 1+29+116=146; relation 2+66+23+2+39+14=146.

#### Evidence 3: Alternative source-grounded interpretations

> One event might be subject to an unstated exclusion or duplicate-event rule, but no footnote supports a different overall set.

### Source links

- sourceLinks 0: [main article — PDF p. 6](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)
- sourceLinks 1: [PDF p. 7](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7)
- sourceLinks 2: [Supplement 3 — PDF p. 17](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=17)
- evidencePaths 0: [2025/jama.2025.15185/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.15185/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Internal eTable total versus its own arm/category sums is target; main 146 merely corroborates arithmetic. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C009 |
| key | 2025::jama.2025.15185::C009 |
| legacyRelationship |  |
| locations | DOC-001, main article — PDF p. 6, Table 2 and narrative, and PDF p. 7; DOC-004, Supplement 3 — PDF p. 17, eTable 6. |
| originalCrossDocument | 0 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Header \`145\` versus arms and category sums \`146\`. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 6 prints an overall adverse-event total of 145 although arm and exhaustive category totals are 146. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | eTable 6 overall adverse-event total is one below arms and category sums |
| suggestedDomain | statistical\_results |
| title | eTable 6 overall adverse-event total is one below arms and category sums |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C010

**eFigure 4 switches locally from FMA to FMMA without qualification**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C010 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3 — PDF p. 23, eFigure 4; DOC-003, Supplement 2 — PDF p. 2, SAP objective; DOC-001, main article — PDF p. 1, PDF p. 3, and PDF p. 6.

### Candidate statement

> eFigure 4 uses FMA in its title/legend and FMMA on its axis without a local qualification. Pending Human Adjudication.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Within the same figure, \`FMA\` versus \`FMMA\` for the stated assessment.

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

> eFigure 4 title/legend use FMA; its axis reads Adjusted Mean Difference (FMMA points). The SAP defines Fugl-Meyer Motor Assessment as FMMA.

#### Evidence 1: Reported-versus-comparator

> Within the same figure, FMA versus FMMA for the stated assessment.

#### Evidence 2: Calculation

> No numeric calculation applies; the reproduced comparison is the local unqualified abbreviation switch.

#### Evidence 3: Alternative source-grounded interpretations

> The SAP's explicit FMMA definition supports that FMMA may be an intentional synonym for the FMA used in the article; it is not evidence of a numeric error.

### Source links

- sourceLinks 0: [Supplement 3 — PDF p. 23](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=23)
- sourceLinks 1: [Supplement 2 — PDF p. 2](../../../2025/jama.2025.15185/joi250066supp2_prod_1761597796.4701.pdf#page=2)
- sourceLinks 2: [main article — PDF p. 1](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1)
- sourceLinks 3: [PDF p. 3](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3)
- sourceLinks 4: [PDF p. 6](../../../2025/jama.2025.15185/jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6)
- evidencePaths 0: [2025/jama.2025.15185/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.15185/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | SAP defines FMMA, supporting synonym interpretation. It is a local figure abbreviation switch, not report-versus-SAP discrepancy. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C010 |
| key | 2025::jama.2025.15185::C010 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3 — PDF p. 23, eFigure 4; DOC-003, Supplement 2 — PDF p. 2, SAP objective; DOC-001, main article — PDF p. 1, PDF p. 3, and PDF p. 6. |
| originalCrossDocument | 0 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Within the same figure, \`FMA\` versus \`FMMA\` for the stated assessment. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | eFigure 4 uses FMA in its title/legend and FMMA on its axis without a local qualification. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | eFigure 4 switches locally from FMA to FMMA without qualification |
| suggestedDomain | report\_internal\_inconsistency |
| title | eFigure 4 switches locally from FMA to FMMA without qualification |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C011

**Estimand 4 win ratio appears under an FMA mean-difference column heading**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3 — PDF p. 13, eTable 2 column heading and Estimand 4 row.

### Candidate statement

> Estimand 4's win ratio is displayed under a column headed as an FMA mean difference. Pending Human Adjudication.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. A dimensionless win ratio row versus an FMA-point mean-difference heading.

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

> The heading reads Estimated Effect of Levodopa: Mean Difference on FMA, \[CI\]. Estimand 4 identifies a death-and-3-month-FMA composite summary as win ratio \[95% CI\] and prints 1.06 \[0.86-1.26\].

#### Evidence 1: Reported-versus-comparator

> A dimensionless win ratio row versus an FMA-point mean-difference heading.

#### Evidence 2: Calculation

> No arithmetic is required: a win ratio and an FMA-point mean difference are different measures/scales under the supplied labels.

#### Evidence 3: Alternative source-grounded interpretations

> The heading may be intended for all rows except Estimand 4, but no exception or qualifying footnote is shown.

### Source links

- sourceLinks 0: [Supplement 3 — PDF p. 13](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=13)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C011 |
| key | 2025::jama.2025.15185::C011 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3 — PDF p. 13, eTable 2 column heading and Estimand 4 row. |
| originalCrossDocument | 0 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. A dimensionless win ratio row versus an FMA-point mean-difference heading. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | Estimand 4's win ratio is displayed under a column headed as an FMA mean difference. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Estimand 4 win ratio appears under an FMA mean-difference column heading |
| suggestedDomain | report\_internal\_inconsistency |
| title | Estimand 4 win ratio appears under an FMA mean-difference column heading |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C012

**Estimand 4 is called an odds ratio in prose and a win ratio in the table**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15185::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-004, Supplement 3 — PDF p. 12, eTable 2 narrative; PDF p. 13, Estimand 4 row.

### Candidate statement

> Matched Estimand 4 displays label the same 1.06 effect as an odds ratio in prose and a win ratio in the table. Pending Human Adjudication.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. \`Odds ratio\` in prose versus \`win ratio\` in the matched table row.

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

> Narrative calls 1.06 (95% CI, 0.86 to 1.25) an odds ratio; the matched full-analysis-set composite row calls 1.06 \[0.86-1.26\] a win ratio \[95% CI\].

#### Evidence 1: Reported-versus-comparator

> Odds ratio in prose versus win ratio in the matched table row.

#### Evidence 2: Calculation

> No arithmetic is required: odds ratio and win ratio are not interchangeable labels under the supplied definitions.

#### Evidence 3: Alternative source-grounded interpretations

> A modelling relationship may exist, but the supplied package does not define the terms as synonyms.

### Source links

- sourceLinks 0: [Supplement 3 — PDF p. 12](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=12)
- sourceLinks 1: [PDF p. 13](../../../2025/jama.2025.15185/joi250066supp3_prod_1761597796.4701.pdf#page=13)

[Original Markdown report](../../../2025/jama.2025.15185/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C012 |
| key | 2025::jama.2025.15185::C012 |
| legacyRelationship |  |
| locations | DOC-004, Supplement 3 — PDF p. 12, eTable 2 narrative; PDF p. 13, Estimand 4 row. |
| originalCrossDocument | 0 |
| package | jama.2025.15185 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. \`Odds ratio\` in prose versus \`win ratio\` in the matched table row. |
| reportHref | ../../2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15185/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched Estimand 4 displays label the same 1.06 effect as an odds ratio in prose and a win ratio in the table. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | Estimand 4 is called an odds ratio in prose and a win ratio in the table |
| suggestedDomain | report\_internal\_inconsistency |
| title | Estimand 4 is called an odds ratio in prose and a win ratio in the table |
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
