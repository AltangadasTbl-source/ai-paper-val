# jama.2025.24175

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.24175 |
| Candidates | 14 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.24175/)

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

- [C001](#candidate-c001) — Day-15 SOFA responder numerator differs between Table 2 and narrative (S_W)
- [C002](#candidate-c002) — Protocol and report IFN-gamma dose comparison (P_R)
- [C003](#candidate-c003) — Primary responder cutoff comparison (P_R)
- [C004](#candidate-c004) — Immunoparalysis entry-classification threshold comparison (P_R)
- [C005](#candidate-c005) — Protocol sample-size, dropout, and total-target arithmetic (P_P)
- [C006](#candidate-c006) — Historical-trial narrative and flow diagram death counts (P_P)
- [C007](#candidate-c007) — APACHE II Table 2 P value versus displayed t-test inputs (P_P)
- [C008](#candidate-c008) — Figure 1 septic-shock classification children exceed their parent total (P_P)
- [C009](#candidate-c009) — ImmunoSep study-site totals across report, protocol, and SAP (P_R)
- [C010](#candidate-c010) — Figure 2C relative-risk label versus displayed association (P_P)
- [C011](#candidate-c011) — eTable 10 SII day-15 OR versus counts, CI, and P value (S_W)
- [C012](#candidate-c012) — eFigure 8B repeats eFigure 7B interaction results under a different outcome caption (S_W)
- [C013](#candidate-c013) — eFigure 9B APACHE interaction point estimate outside its CI (S_W)
- [C014](#candidate-c014) — Historical mortality-pair registration (P_P)

## Candidate C001

**Day-15 SOFA responder numerator differs between Table 2 and narrative**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 2, PDF p. 6; DOC-001 Results narrative, PDF p. 7.

### Candidate statement

> Pending Human Adjudication. The matched day-15 responder occurrence prints 52/131 in Table 2 and 51/131 in the narrative.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. 52/131 versus 51/131, with the same displayed 39.7% and placebo comparator.

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

> Table 2 prints precision immunotherapy 52/131 (39.7%) versus placebo 34/145 (23.4%); the narrative prints 51 of 131 (39.7%) versus 34 of 145 (23.4%) for the same endpoint.

#### Evidence 1: Reported-versus-comparator

> 52/131 versus 51/131, with the same displayed 39.7% and placebo comparator.

#### Evidence 2: Calculation

> 52/131 = 39.6947% (39.7% rounded); 51/131 = 38.9313% (38.9% rounded). Table-2 counts yield crude OR (52x111)/(79x34) = 2.15.

#### Evidence 3: Alternative source-grounded interpretations

> A table or narrative transcription error is possible; an undocumented analysis-set distinction is possible but both locations print denominator 131.

### Source links

- sourceLinks 0: [DOC-001 Table 2, PDF p. 6](../../../2025/jama.2025.24175/jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6)
- sourceLinks 1: [DOC-001 Results narrative, PDF p. 7](../../../2025/jama.2025.24175/jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C001 |
| key | 2025::jama.2025.24175::C001 |
| legacyRelationship |  |
| locations | DOC-001 Table 2, PDF p. 6; DOC-001 Results narrative, PDF p. 7. |
| originalCrossDocument | 1 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. 52/131 versus 51/131, with the same displayed 39.7% and placebo comparator. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. The matched day-15 responder occurrence prints 52/131 in Table 2 and 51/131 in the narrative. |
| submissionInvolved | 1 |
| subtype | Day-15 SOFA responder numerator differs between Table 2 and narrative |
| suggestedDomain | report\_internal\_inconsistency |
| title | Day-15 SOFA responder numerator differs between Table 2 and narrative |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**Protocol and report IFN-gamma dose comparison**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C002 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | exclude |

### Source location

> DOC-002 protocol, PDF p. 6; DOC-001 regimen, PDF p. 2.

### Candidate statement

> Pending Human Adjudication. Retained ID with a direct-source repair: the alleged 20-microgram protocol comparator was not reproduced.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Directly printed 100 micrograms versus 100 micrograms, not the prior 100-versus-20 comparison.

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

> Direct protocol rendering prints sc rhIFNgamma 100 micrograms once every other day; the report prints 100 micrograms every 48 hours for 15 days.

#### Evidence 1: Reported-versus-comparator

> Directly printed 100 micrograms versus 100 micrograms, not the prior 100-versus-20 comparison.

#### Evidence 2: Calculation

> 100/100 = 1.

#### Evidence 3: Alternative source-grounded interpretations

> The 20-microgram locator transcription may reflect font encoding; an unsupplied approved protocol version remains unavailable.

### Source links

- sourceLinks 0: [DOC-002 protocol, PDF p. 6](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=6)
- sourceLinks 1: [DOC-001 regimen, PDF p. 2](../../../2025/jama.2025.24175/jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2025::jama.2025.24175::C002 |
| legacyRelationship |  |
| locations | DOC-002 protocol, PDF p. 6; DOC-001 regimen, PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism | intervention\_delivery |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Directly printed 100 micrograms versus 100 micrograms, not the prior 100-versus-20 comparison. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Retained ID with a direct-source repair: the alleged 20-microgram protocol comparator was not reproduced. |
| submissionInvolved | 0 |
| subtype | Protocol and report IFN-gamma dose comparison |
| suggestedDomain | protocol\_report |
| title | Protocol and report IFN-gamma dose comparison |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | exclude |

## Candidate C003

**Primary responder cutoff comparison**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C003 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | exclude |

### Source location

> DOC-002 protocol, PDF p. 7; DOC-001 report, PDF p. 1; DOC-002 SAP, PDF p. 66.

### Candidate statement

> Pending Human Adjudication. Retained ID with a direct-source repair: the alleged 1.5-point binary cutoff was not reproduced.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. 1.4 versus 1.4 in matched supplied sources, not 1.5 versus 1.4.

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

> Direct protocol, report, and SAP occurrences print a 1.4-point responder cutoff; SAP defines \>1.4 as achievement.

#### Evidence 1: Reported-versus-comparator

> 1.4 versus 1.4 in matched supplied sources, not 1.5 versus 1.4.

#### Evidence 2: Calculation

> 1.4 - 1.4 = 0.

#### Evidence 3: Alternative source-grounded interpretations

> The 1.5 value may be derivative-text recognition error; an unsupplied protocol version may differ.

### Source links

- sourceLinks 0: [DOC-002 protocol, PDF p. 7](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=7)
- sourceLinks 1: [DOC-001 report, PDF p. 1](../../../2025/jama.2025.24175/jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1)
- sourceLinks 2: [DOC-002 SAP, PDF p. 66](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=66)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2025::jama.2025.24175::C003 |
| legacyRelationship |  |
| locations | DOC-002 protocol, PDF p. 7; DOC-001 report, PDF p. 1; DOC-002 SAP, PDF p. 66. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. 1.4 versus 1.4 in matched supplied sources, not 1.5 versus 1.4. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Retained ID with a direct-source repair: the alleged 1.5-point binary cutoff was not reproduced. |
| submissionInvolved | 0 |
| subtype | Primary responder cutoff comparison |
| suggestedDomain | protocol\_report |
| title | Primary responder cutoff comparison |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | exclude |

## Candidate C004

**Immunoparalysis entry-classification threshold comparison**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | exclude |

### Source location

> DOC-002 protocol, PDF p. 9; DOC-003 eMethods, PDF p. 13; DOC-002 SAP reversal definition, PDF p. 69.

### Candidate statement

> Pending Human Adjudication. Retained ID with a direct-source repair: entry sources agree at 5000, while 8000 belongs to a separately named reversal endpoint.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Entry threshold 5000 versus separately defined reversal threshold 8000.

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

> Entry classification is ferritin at or below 4420 ng/mL plus HLA-DR below 5000 molecules/monocyte. SAP p. 69 prints restoration above 8000 for day-15 reversal.

#### Evidence 1: Reported-versus-comparator

> Entry threshold 5000 versus separately defined reversal threshold 8000.

#### Evidence 2: Calculation

> Matched entry sources agree at 5000; no 8000-versus-5000 entry comparison is present.

#### Evidence 3: Alternative source-grounded interpretations

> The prior record may have transferred the reversal value into entry classification; an unsupplied entry definition is unavailable.

### Source links

- sourceLinks 0: [DOC-002 protocol, PDF p. 9](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=9)
- sourceLinks 1: [DOC-003 eMethods, PDF p. 13](../../../2025/jama.2025.24175/joi250116supp2_prod_1771885794.27755.pdf#page=13)
- sourceLinks 2: [DOC-002 SAP reversal definition, PDF p. 69](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=69)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2025::jama.2025.24175::C004 |
| legacyRelationship |  |
| locations | DOC-002 protocol, PDF p. 9; DOC-003 eMethods, PDF p. 13; DOC-002 SAP reversal definition, PDF p. 69. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Entry threshold 5000 versus separately defined reversal threshold 8000. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Retained ID with a direct-source repair: entry sources agree at 5000, while 8000 belongs to a separately named reversal endpoint. |
| submissionInvolved | 0 |
| subtype | Immunoparalysis entry-classification threshold comparison |
| suggestedDomain | protocol\_report |
| title | Immunoparalysis entry-classification threshold comparison |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | exclude |

## Candidate C005

**Protocol sample-size, dropout, and total-target arithmetic**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C005 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 protocol, PDF p. 25 and PDF p. 26.

### Candidate statement

> Pending Human Adjudication. Retained ID with repaired direct inputs: protocol prints 117 per arm, about 15% dropout, and total randomization 280.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Required analyzable total 234 versus planned randomization 280 under an approximate attrition statement.

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

> The source does not print the prior 112-per-arm premise; it prints 117 patients per arm, about 15% dropout, and N=280.

#### Evidence 1: Reported-versus-comparator

> Required analyzable total 234 versus planned randomization 280 under an approximate attrition statement.

#### Evidence 2: Calculation

> 2x117 = 234; 234/(1-.15) = 275.29 (conventionally at least 276); 1-234/280 = 16.43%.

#### Evidence 3: Alternative source-grounded interpretations

> Conservative rounding to 280, approximately 16.4% attrition, or unstated block/operational inflation could explain the residual.

### Source links

- sourceLinks 0: [DOC-002 protocol, PDF p. 25](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=25)
- sourceLinks 1: [PDF p. 26](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=26)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Original 112 input not reproduced, repaired 117 input leaves only approximate attrition/rounding question. Retained as repaired\_residual, not fully negated. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2025::jama.2025.24175::C005 |
| legacyRelationship |  |
| locations | DOC-002 protocol, PDF p. 25 and PDF p. 26. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Required analyzable total 234 versus planned randomization 280 under an approximate attrition statement. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Retained ID with repaired direct inputs: protocol prints 117 per arm, about 15% dropout, and total randomization 280. |
| submissionInvolved | 0 |
| subtype | Protocol sample-size, dropout, and total-target arithmetic |
| suggestedDomain | plan\_material |
| title | Protocol sample-size, dropout, and total-target arithmetic |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C006

**Historical-trial narrative and flow diagram death counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C006 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 narrative, PDF p. 41; DOC-002 Figure 1, PDF p. 50.

### Candidate statement

> Pending Human Adjudication. The personalized-immunotherapy death count is 14 in the narrative and 11 in the flow figure, conditional on a matched time window.

### AI rationale

> Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Personalized arm 14 versus 11; placebo count 18 agrees.

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

> Narrative reports 18/21 (85.7%) placebo and 14/15 (93.3%) personalized-immunotherapy deaths at 28 days; Figure 1 reports early termination because of death n=18 and n=11.

#### Evidence 1: Reported-versus-comparator

> Personalized arm 14 versus 11; placebo count 18 agrees.

#### Evidence 2: Calculation

> 14/15 = 93.3%; 11/15 = 73.3%; difference = 3 people.

#### Evidence 3: Alternative source-grounded interpretations

> Figure 1 may represent a shorter intervention-termination window; its time window is not stated.

### Source links

- sourceLinks 0: [DOC-002 narrative, PDF p. 41](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=41)
- sourceLinks 1: [DOC-002 Figure 1, PDF p. 50](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=50)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 1: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/extraction/support\_quantitative\_evidence.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/extraction/support_quantitative_evidence.md)
- evidencePaths 2: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/parts/mapping/doc002\_pp033\_064.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/parts/mapping/doc002_pp033_064.md)
- evidencePaths 3: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/DOC-002/pp033\_064/low-36.png](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/low-36.png)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  Historical PROVIDE study results presented in protocol background; not current ImmunoSep observed results. Protocol footer and introduction directly inspected in stored page render. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2025::jama.2025.24175::C006 |
| legacyRelationship | P\_B |
| locations | DOC-002 narrative, PDF p. 41; DOC-002 Figure 1, PDF p. 50. |
| originalCrossDocument | 1 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Personalized arm 14 versus 11; placebo count 18 agrees. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. The personalized-immunotherapy death count is 14 in the narrative and 11 in the flow figure, conditional on a matched time window. |
| submissionInvolved | 0 |
| subtype | Historical-trial narrative and flow diagram death counts |
| suggestedDomain | plan\_material |
| title | Historical-trial narrative and flow diagram death counts |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C007

**APACHE II Table 2 P value versus displayed t-test inputs**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C007 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Table 2, PDF p. 48.

### Candidate statement

> Pending Human Adjudication. The printed P=.376 is not compatible with conventional two-group calculations from the displayed Student t-test inputs.

### AI rationale

> Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Printed P=.376 versus diagnostics from the displayed group summaries and named test.

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

> Placebo n=21, 18.2 +/- 8.7; personalized immunotherapy n=15, 30.5 +/- 9.4; P=.376; footnote identifies Student t test.

#### Evidence 1: Reported-versus-comparator

> Printed P=.376 versus diagnostics from the displayed group summaries and named test.

#### Evidence 2: Calculation

> Pooled SD about 9.00, SE about 3.04, t about 4.05 (34 df; two-sided P about .0003); Welch t about 3.99 (about 29 df; P about .0004).

#### Evidence 3: Alternative source-grounded interpretations

> P may be transposed, an input may be inaccurate, or an unreported transformed/different dataset analysis may have been used.

### Source links

- sourceLinks 0: [DOC-002 Table 2, PDF p. 48](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=48)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 1: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/extraction/support\_quantitative\_evidence.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/extraction/support_quantitative_evidence.md)
- evidencePaths 2: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/parts/mapping/doc002\_pp033\_064.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/parts/mapping/doc002_pp033_064.md)
- evidencePaths 3: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/DOC-002/pp033\_064/low-36.png](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/low-36.png)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  Historical PROVIDE study results presented in protocol background; not current ImmunoSep observed results. Protocol footer and introduction directly inspected in stored page render. |
| broadPlanInvolved | 1 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2025::jama.2025.24175::C007 |
| legacyRelationship | P\_B |
| locations | DOC-002 Table 2, PDF p. 48. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Printed P=.376 versus diagnostics from the displayed group summaries and named test. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. The printed P=.376 is not compatible with conventional two-group calculations from the displayed Student t-test inputs. |
| submissionInvolved | 0 |
| subtype | APACHE II Table 2 P value versus displayed t-test inputs |
| suggestedDomain | plan\_material |
| title | APACHE II Table 2 P value versus displayed t-test inputs |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C008

**Figure 1 septic-shock classification children exceed their parent total**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C008 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Figure 1, PDF p. 50.

### Candidate statement

> Pending Human Adjudication. Displayed child classifications sum to 178 under a parent total of 177.

### AI rationale

> Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Parent 177 versus displayed child total 178.

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

> Parent septic shock =177; children MALS 44 (24.8%), immunoparalysis 2 (1.1%), intermediate 132 (74.0%).

#### Evidence 1: Reported-versus-comparator

> Parent 177 versus displayed child total 178.

#### Evidence 2: Calculation

> 44+2+132 = 178; percentages total 99.9% from rounding, but integer children exceed parent by one.

#### Evidence 3: Alternative source-grounded interpretations

> One count or parent total may be typographic, or an unstated overlap/unclassified case may exist.

### Source links

- sourceLinks 0: [DOC-002 Figure 1, PDF p. 50](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=50)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 1: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/extraction/support\_quantitative\_evidence.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/extraction/support_quantitative_evidence.md)
- evidencePaths 2: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/parts/mapping/doc002\_pp033\_064.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/parts/mapping/doc002_pp033_064.md)
- evidencePaths 3: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/DOC-002/pp033\_064/low-36.png](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/low-36.png)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  Historical PROVIDE study results presented in protocol background; not current ImmunoSep observed results. Protocol footer and introduction directly inspected in stored page render. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C008 |
| key | 2025::jama.2025.24175::C008 |
| legacyRelationship | P\_B |
| locations | DOC-002 Figure 1, PDF p. 50. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Parent 177 versus displayed child total 178. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Displayed child classifications sum to 178 under a parent total of 177. |
| submissionInvolved | 0 |
| subtype | Figure 1 septic-shock classification children exceed their parent total |
| suggestedDomain | plan\_material |
| title | Figure 1 septic-shock classification children exceed their parent total |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C009

**ImmunoSep study-site totals across report, protocol, and SAP**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C009 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-001 report, PDF p. 2; DOC-002 protocol, PDF p. 10; DOC-002 SAP, PDF p. 65; PDF p. 67.

### Candidate statement

> Pending Human Adjudication. Retained ID with repaired direct-source values: 24, 31, and 33 sites require milestone definitions.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. Repaired direct values 24, 31, and 33; prior 28 and report p.1 citation were not reproduced.

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

> Protocol and SAP design print 24 sites, SAP model text says 31 participated, and the report prints 33 sites.

#### Evidence 1: Reported-versus-comparator

> Repaired direct values 24, 31, and 33; prior 28 and report p.1 citation were not reproduced.

#### Evidence 2: Calculation

> The three integers cannot be reconciled by rounding; protocol and SAP design share 24.

#### Evidence 3: Alternative source-grounded interpretations

> They may describe different operational milestones, but chronology and definitions are absent.

### Source links

- sourceLinks 0: [DOC-001 report, PDF p. 2](../../../2025/jama.2025.24175/jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2)
- sourceLinks 1: [DOC-002 protocol, PDF p. 10](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=10)
- sourceLinks 2: [DOC-002 SAP, PDF p. 65](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=65)
- sourceLinks 3: [PDF p. 67](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=67)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |
| relations | 1 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Original 28 corrected to24, but repaired 24/31/33 mismatch remains. Both plan internal and final-vs-plan contexts; milestone definitions missing. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C009 |
| key | 2025::jama.2025.24175::C009 |
| legacyRelationship |  |
| locations | DOC-001 report, PDF p. 2; DOC-002 protocol, PDF p. 10; DOC-002 SAP, PDF p. 65; PDF p. 67. |
| originalCrossDocument | 1 |
| package | jama.2025.24175 |
| planMechanism | population\_recruitment\_sites |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. Repaired direct values 24, 31, and 33; prior 28 and report p.1 citation were not reproduced. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Retained ID with repaired direct-source values: 24, 31, and 33 sites require milestone definitions. |
| submissionInvolved | 0 |
| subtype | ImmunoSep study-site totals across report, protocol, and SAP |
| suggestedDomain | protocol\_report |
| title | ImmunoSep study-site totals across report, protocol, and SAP |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C010

**Figure 2C relative-risk label versus displayed association**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C010 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 Figure 2C, PDF p. 51; DOC-002 Figure 3, PDF p. 52.

### Candidate statement

> Pending Human Adjudication. Figure 2C labels 2.82 (1.58-5.14) as RR although displayed counts give a crude RR of 1.61 and the same value/CI appears as an HR in Figure 3.

### AI rationale

> Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. RR label/value 2.82 versus crude RR 1.61 and identical nearby HR 2.82.

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

> Figure 2C shows 69/103 deaths versus 37/89 and labels RR\_death 2.82 (1.58-5.14), P\<.0001; Figure 3 prints HR 2.82 (1.58-5.14).

#### Evidence 1: Reported-versus-comparator

> RR label/value 2.82 versus crude RR 1.61 and identical nearby HR 2.82.

#### Evidence 2: Calculation

> (69/103)/(37/89) = 1.61; (69x52)/(34x37) = 2.85, compatible with 2.82.

#### Evidence 3: Alternative source-grounded interpretations

> The value may be HR, OR, another model output, or paired with count rows from a different analysis; source does not resolve it. P\<.0001 is threshold notation and not this card's basis.

### Source links

- sourceLinks 0: [DOC-002 Figure 2C, PDF p. 51](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=51)
- sourceLinks 1: [DOC-002 Figure 3, PDF p. 52](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=52)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 1: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/extraction/support\_quantitative\_evidence.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/extraction/support_quantitative_evidence.md)
- evidencePaths 2: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/parts/mapping/doc002\_pp033\_064.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/parts/mapping/doc002_pp033_064.md)
- evidencePaths 3: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/DOC-002/pp033\_064/low-36.png](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/low-36.png)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity |  Historical PROVIDE study results presented in protocol background; not current ImmunoSep observed results. Protocol footer and introduction directly inspected in stored page render. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C010 |
| key | 2025::jama.2025.24175::C010 |
| legacyRelationship | P\_B |
| locations | DOC-002 Figure 2C, PDF p. 51; DOC-002 Figure 3, PDF p. 52. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. RR label/value 2.82 versus crude RR 1.61 and identical nearby HR 2.82. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Figure 2C labels 2.82 (1.58-5.14) as RR although displayed counts give a crude RR of 1.61 and the same value/CI appears as an HR in Figure 3. |
| submissionInvolved | 0 |
| subtype | Figure 2C relative-risk label versus displayed association |
| suggestedDomain | plan\_material |
| title | Figure 2C relative-risk label versus displayed association |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C011

**eTable 10 SII day-15 OR versus counts, CI, and P value**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-003 eTable 10, PDF p. 22.

### Candidate statement

> Pending Human Adjudication. Printed OR 1.194 does not reconcile with the count-derived crude OR and interval midpoint.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Printed 1.194 versus count-derived OR about 1.94 and CI log midpoint about 1.94.

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

> SII day-15 row prints 40/106 versus 29/122, OR 1.194 (1.09-3.45), P=.030.

#### Evidence 1: Reported-versus-comparator

> Printed 1.194 versus count-derived OR about 1.94 and CI log midpoint about 1.94.

#### Evidence 2: Calculation

> (40x93)/(66x29) = 1.94; sqrt(1.09x3.45) about 1.94.

#### Evidence 3: Alternative source-grounded interpretations

> Decimal/transcription error or a differently defined analysis pairing may explain the row.

### Source links

- sourceLinks 0: [DOC-003 eTable 10, PDF p. 22](../../../2025/jama.2025.24175/joi250116supp2_prod_1771885794.27755.pdf#page=22)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C011 |
| key | 2025::jama.2025.24175::C011 |
| legacyRelationship |  |
| locations | DOC-003 eTable 10, PDF p. 22. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Printed 1.194 versus count-derived OR about 1.94 and CI log midpoint about 1.94. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Printed OR 1.194 does not reconcile with the count-derived crude OR and interval midpoint. |
| submissionInvolved | 1 |
| subtype | eTable 10 SII day-15 OR versus counts, CI, and P value |
| suggestedDomain | statistical\_results |
| title | eTable 10 SII day-15 OR versus counts, CI, and P value |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C012

**eFigure 8B repeats eFigure 7B interaction results under a different outcome caption**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C012 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-003 eFigure 7B, PDF p. 51; DOC-003 eFigure 8B, PDF p. 52.

### Candidate statement

> Pending Human Adjudication. Six OR/CI/P rows repeat exactly under primary-endpoint and 28-day-mortality captions.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Complete six-row primary-endpoint output versus identical six-row 28-day-mortality output.

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

> eFigure 7B prints APACHE 0.47 and interaction 1.85; CCI 0.22 and interaction 5.79; SOFA 0.56 and interaction 3.08, with their CIs/P values. eFigure 8B repeats all six rows exactly under a 28-day mortality caption; A panels have different event/total data.

#### Evidence 1: Reported-versus-comparator

> Complete six-row primary-endpoint output versus identical six-row 28-day-mortality output.

#### Evidence 2: Calculation

> Six point estimates, intervals, and P values are identical across the two panels.

#### Evidence 3: Alternative source-grounded interpretations

> A copied panel or incorrect caption is possible; source-production files are unavailable and no specific mechanism is established.

### Source links

- sourceLinks 0: [DOC-003 eFigure 7B, PDF p. 51](../../../2025/jama.2025.24175/joi250116supp2_prod_1771885794.27755.pdf#page=51)
- sourceLinks 1: [DOC-003 eFigure 8B, PDF p. 52](../../../2025/jama.2025.24175/joi250116supp2_prod_1771885794.27755.pdf#page=52)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C012 |
| key | 2025::jama.2025.24175::C012 |
| legacyRelationship |  |
| locations | DOC-003 eFigure 7B, PDF p. 51; DOC-003 eFigure 8B, PDF p. 52. |
| originalCrossDocument | 1 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Complete six-row primary-endpoint output versus identical six-row 28-day-mortality output. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Six OR/CI/P rows repeat exactly under primary-endpoint and 28-day-mortality captions. |
| submissionInvolved | 1 |
| subtype | eFigure 8B repeats eFigure 7B interaction results under a different outcome caption |
| suggestedDomain | report\_internal\_inconsistency |
| title | eFigure 8B repeats eFigure 7B interaction results under a different outcome caption |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C013

**eFigure 9B APACHE interaction point estimate outside its CI**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C013 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-003 eFigure 9B, PDF p. 53.

### Candidate statement

> Pending Human Adjudication. The printed OR 0.11 lies below its printed 95% CI lower endpoint 0.36.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Point estimate 0.11 versus interval lower endpoint 0.36.

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

> APACHE II \>=25 interaction row prints OR 0.11, 95% CI 0.36-3.42, P=.86.

#### Evidence 1: Reported-versus-comparator

> Point estimate 0.11 versus interval lower endpoint 0.36.

#### Evidence 2: Calculation

> 0.11 \< 0.36; rounding cannot span the difference.

#### Evidence 3: Alternative source-grounded interpretations

> A point estimate, endpoint, or row alignment may be wrong; source does not identify which component.

### Source links

- sourceLinks 0: [DOC-003 eFigure 9B, PDF p. 53](../../../2025/jama.2025.24175/joi250116supp2_prod_1771885794.27755.pdf#page=53)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C013 |
| key | 2025::jama.2025.24175::C013 |
| legacyRelationship |  |
| locations | DOC-003 eFigure 9B, PDF p. 53. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Point estimate 0.11 versus interval lower endpoint 0.36. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. The printed OR 0.11 lies below its printed 95% CI lower endpoint 0.36. |
| submissionInvolved | 1 |
| subtype | eFigure 9B APACHE interaction point estimate outside its CI |
| suggestedDomain | statistical\_results |
| title | eFigure 9B APACHE interaction point estimate outside its CI |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C014

**Historical mortality-pair registration**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.24175::C014 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | exclude |

### Source location

> DOC-002 actual mortality sentence, PDF p. 41; Discussion, PDF p. 42; Table 2, PDF p. 48; Figure 1, PDF p. 50.

### Candidate statement

> Pending Human Adjudication. Retained ID with direct-source repair: no supplied source prints the registered mortality count/percentage pairs.

### AI rationale

> Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Unsupported assembled alleged pairs versus directly printed coherent p.41 mortality pairs.

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

> Actual p.41 pairs are 18/21 (85.7%) and 14/15 (93.3%) and reconcile. The alleged p.42 pairs are absent; p.48 values 10 (47.6%) and 12 (80.0%) are unrelated rows.

#### Evidence 1: Reported-versus-comparator

> Unsupported assembled alleged pairs versus directly printed coherent p.41 mortality pairs.

#### Evidence 2: Calculation

> 18/21 = 85.7%; 14/15 = 93.3%.

#### Evidence 3: Alternative source-grounded interpretations

> The prior record may have combined a Figure 1 count with unrelated Table 2 values and a shifted page citation; an outside source is unavailable.

### Source links

- sourceLinks 0: [DOC-002 actual mortality sentence, PDF p. 41](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=41)
- sourceLinks 1: [Discussion, PDF p. 42](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=42)
- sourceLinks 2: [Table 2, PDF p. 48](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=48)
- sourceLinks 3: [Figure 1, PDF p. 50](../../../2025/jama.2025.24175/joi250116supp1_prod_1771885794.26255.pdf#page=50)
- evidencePaths 0: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 1: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/extraction/support\_quantitative\_evidence.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/extraction/support_quantitative_evidence.md)
- evidencePaths 2: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/parts/mapping/doc002\_pp033\_064.md](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/parts/mapping/doc002_pp033_064.md)
- evidencePaths 3: [2025/jama.2025.24175/.ai\_paper\_validation/review\_1\_5\_1/preprocessing/DOC-002/pp033\_064/low-36.png](../../../2025/jama.2025.24175/.ai_paper_validation/review_1_5_1/preprocessing/DOC-002/pp033_064/low-36.png)

[Original Markdown report](../../../2025/jama.2025.24175/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |
| legacyRelations | 0 | P\_B |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Final direct-source recheck explicitly does not reproduce registered mismatch; relationship denotes original registration only.  Historical PROVIDE study results presented in protocol background; not current ImmunoSep observed results. Protocol footer and introduction directly inspected in stored page render. |
| broadPlanInvolved | 1 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C014 |
| key | 2025::jama.2025.24175::C014 |
| legacyRelationship | P\_B |
| locations | DOC-002 actual mortality sentence, PDF p. 41; Discussion, PDF p. 42; Table 2, PDF p. 48; Figure 1, PDF p. 50. |
| originalCrossDocument | 0 |
| package | jama.2025.24175 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target concerns historical/background results inside the protocol, not the current trial plan or submitted main/results supplement. Unsupported assembled alleged pairs versus directly printed coherent p.41 mortality pairs. |
| reportHref | ../../2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.24175/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C014 |
| sourceStatus | Pending Human Adjudication |
| statement | Pending Human Adjudication. Retained ID with direct-source repair: no supplied source prints the registered mortality count/percentage pairs. |
| submissionInvolved | 0 |
| subtype | Historical mortality-pair registration |
| suggestedDomain | plan\_material |
| title | Historical mortality-pair registration |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | exclude |

## Completion checklist

- [ ] Primary reviewer ID is recorded and every primary assessment is complete.
- [ ] Primary answers were preserved at handoff, with a backup or revision reference recorded.
- [ ] Checker is a different person, with a distinct reviewer ID.
- [ ] Every final assessment uses valid applicable codes and Complete is checker_done.
- [ ] Agreement matches Primary; all other checker results have comments.
- [ ] Required discussions are resolved and participants and conclusions are recorded.
- [ ] No final disposition remains discuss, and every Final outcome follows the codebook.
- [ ] Final counts reconcile to the candidate total and Paper status is final_ready.
