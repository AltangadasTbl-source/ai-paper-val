# jama.2018.9128

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.9128 |
| Candidates | 13 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.9128/)

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

- [C001](#candidate-c001) — Intervention 3-month BMI-observation count differs across result displays (S_C)
- [C002](#candidate-c002) — Control 3-month BMI-observation count differs across result displays (S_C)
- [C003](#candidate-c003) — Intervention 9-month BMI-observation count differs across result displays (S_C)
- [C004](#candidate-c004) — Intervention 12-month BMI-observation count differs across result displays (S_C)
- [C005](#candidate-c005) — Control 12-month BMI-observation count differs across result displays (S_C)
- [C006](#candidate-c006) — Intervention 24-month BMI-observation count differs across result displays (S_C)
- [C007](#candidate-c007) — Control 24-month BMI-observation count differs across result displays (S_C)
- [C008](#candidate-c008) — Intervention 36-month BMI-observation count differs across result displays (S_C)
- [C009](#candidate-c009) — Final SAP says six assessment points but enumerates five (P_P)
- [C010](#candidate-c010) — Revised protocol gives six points but lists seven including 48 months (P_P)
- [C011](#candidate-c011) — Original protocol labels primary outcome as BMI percentile/BMI% while results use BMI kg/m² (P_R)
- [C012](#candidate-c012) — Control-condition session count and duration differ across protocol versions and article (P_R)
- [C013](#candidate-c013) — Control 9-month BMI-observation count differs across result displays (S_C)

## Candidate C001

**Intervention 3-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C001 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The intervention 3-month BMI count is 288 in the flow diagram and 279 in both the observed-BMI figure and eTable.

### AI rationale

> The intervention 3-month BMI count is 288 in the flow diagram and 279 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints 288 BMI measured at 3 mo for intervention and defines the retained count as children for whom BMI was collected. Figure 2 and eTable 1 each print intervention 279 at 3 months.

#### Evidence 1: Reported-versus-comparator

> 288 versus 279 for intervention, 3 months; Figure 2 and eTable 1 agree with each other.

#### Evidence 2: Calculation

> 288 - 279 = 9.

#### Evidence 3: Alternative source-grounded interpretations

> Figure 1 may count all collected measurements while Figure 2/eTable 1 may use a cleaned descriptive subset; no supplied caption or method defines that distinction.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2018::jama.2018.9128::C001 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The intervention 3-month BMI count is 288 in the flow diagram and 279 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention 3-month BMI count is 288 in the flow diagram and 279 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Intervention 3-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**Control 3-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The control 3-month BMI count is 277 in the flow diagram and 271 in both the observed-BMI figure and eTable.

### AI rationale

> The control 3-month BMI count is 277 in the flow diagram and 271 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints 277 BMI measured at 3 mo for control; Figure 2 and eTable 1 each print control 271 at 3 months.

#### Evidence 1: Reported-versus-comparator

> 277 versus 271 for control, 3 months.

#### Evidence 2: Calculation

> 277 - 271 = 6.

#### Evidence 3: Alternative source-grounded interpretations

> Figure 2/eTable 1 may be a cleaned descriptive subset, but the supplied package does not define a cleaning or inclusion rule.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2018::jama.2018.9128::C002 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The control 3-month BMI count is 277 in the flow diagram and 271 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The control 3-month BMI count is 277 in the flow diagram and 271 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Control 3-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Intervention 9-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C003 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The intervention 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable.

### AI rationale

> The intervention 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints intervention 282 BMI measured at 9 mo; Figure 2 and eTable 1 each print 280.

#### Evidence 1: Reported-versus-comparator

> 282 versus 280 for intervention, 9 months.

#### Evidence 2: Calculation

> 282 - 280 = 2.

#### Evidence 3: Alternative source-grounded interpretations

> A post-collection analytic or descriptive subset could explain the difference, but the package supplies no definition.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2018::jama.2018.9128::C003 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The intervention 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Intervention 9-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C004

**Intervention 12-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C004 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The intervention 12-month BMI count is 275 in the flow diagram and 274 in both the observed-BMI figure and eTable.

### AI rationale

> The intervention 12-month BMI count is 275 in the flow diagram and 274 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints intervention 275 BMI measured at 12 mo; Figure 2 and eTable 1 each print 274.

#### Evidence 1: Reported-versus-comparator

> 275 versus 274 for intervention, 12 months.

#### Evidence 2: Calculation

> 275 - 274 = 1.

#### Evidence 3: Alternative source-grounded interpretations

> One record may have been excluded from a descriptive subset, but no supplied rule establishes that.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2018::jama.2018.9128::C004 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The intervention 12-month BMI count is 275 in the flow diagram and 274 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention 12-month BMI count is 275 in the flow diagram and 274 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Intervention 12-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C005

**Control 12-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C005 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The control 12-month BMI count is 276 in the flow diagram and 275 in both the observed-BMI figure and eTable.

### AI rationale

> The control 12-month BMI count is 276 in the flow diagram and 275 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints control 276 BMI measured at 12 mo; Figure 2 and eTable 1 each print 275.

#### Evidence 1: Reported-versus-comparator

> 276 versus 275 for control, 12 months.

#### Evidence 2: Calculation

> 276 - 275 = 1.

#### Evidence 3: Alternative source-grounded interpretations

> A cleaned descriptive subset is possible but is not defined by the supplied materials.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C005 |
| key | 2018::jama.2018.9128::C005 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The control 12-month BMI count is 276 in the flow diagram and 275 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The control 12-month BMI count is 276 in the flow diagram and 275 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Control 12-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**Intervention 24-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C006 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The intervention 24-month BMI count is 280 in the flow diagram and 278 in both the observed-BMI figure and eTable.

### AI rationale

> The intervention 24-month BMI count is 280 in the flow diagram and 278 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints intervention 280 BMI measured at 24 mo; Figure 2 and eTable 1 each print 278.

#### Evidence 1: Reported-versus-comparator

> 280 versus 278 for intervention, 24 months.

#### Evidence 2: Calculation

> 280 - 278 = 2.

#### Evidence 3: Alternative source-grounded interpretations

> A post-collection descriptive-display subset could account for the difference, but the package does not state one.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C006 |
| key | 2018::jama.2018.9128::C006 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The intervention 24-month BMI count is 280 in the flow diagram and 278 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention 24-month BMI count is 280 in the flow diagram and 278 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Intervention 24-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Control 24-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C007 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The control 24-month BMI count is 267 in the flow diagram and 266 in both the observed-BMI figure and eTable.

### AI rationale

> The control 24-month BMI count is 267 in the flow diagram and 266 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints control 267 BMI measured at 24 mo; Figure 2 and eTable 1 each print 266.

#### Evidence 1: Reported-versus-comparator

> 267 versus 266 for control, 24 months.

#### Evidence 2: Calculation

> 267 - 266 = 1.

#### Evidence 3: Alternative source-grounded interpretations

> A cleaning or descriptive-subset distinction is possible but unreported.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2018::jama.2018.9128::C007 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The control 24-month BMI count is 267 in the flow diagram and 266 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | The control 24-month BMI count is 267 in the flow diagram and 266 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Control 24-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C008

**Intervention 36-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C008 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The intervention 36-month count is 278 retained/BMI collected in the flow diagram and 276 in both the observed-BMI figure and eTable.

### AI rationale

> The intervention 36-month count is 278 retained/BMI collected in the flow diagram and 276 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints intervention 278 Retained at 36 mo; its caption defines retained as BMI collected. Figure 2 and eTable 1 each print 276.

#### Evidence 1: Reported-versus-comparator

> 278 versus 276 for intervention, 36 months.

#### Evidence 2: Calculation

> 278 - 276 = 2.

#### Evidence 3: Alternative source-grounded interpretations

> Retained may have been used more broadly despite the caption, or a post-collection subset may have been used; neither is defined.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2018::jama.2018.9128::C008 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The intervention 36-month count is 278 retained/BMI collected in the flow diagram and 276 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The intervention 36-month count is 278 retained/BMI collected in the flow diagram and 276 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Intervention 36-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C009

**Final SAP says six assessment points but enumerates five**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C009 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 final SAP — PDF p. 110; DOC-002 protocol schedule — PDF p. 15; DOC-001 Methods — PDF p. 4; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The final SAP states six time points but its parenthetical schedule lists only baseline, 3, 9, 12, and 36 months.

### AI rationale

> The final SAP says six timepoints but enumerates only five. The protocol schedule and article/eTable corroborate 24 months as the likely missing item; the focal contradiction is the SAP total versus its own list.

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

> The SAP says 6 time points while enumerating five occasions. Other supplied schedules/results include 24 months; the SAP also describes six repeated measurements on p. 112.

#### Evidence 1: Reported-versus-comparator

> Stated total of six versus five listed occasions; matching sources show the otherwise omitted 24-month occasion.

#### Evidence 2: Calculation

> count(baseline, 3, 9, 12, 36) = 5; including 24 months yields 6.

#### Evidence 3: Alternative source-grounded interpretations

> The final-SAP prose may have an editorial omission, and the model may still have used 24-month data; the package does not provide the archived analysis input schedule.

### Source links

- sourceLinks 0: [DOC-002 final SAP — PDF p. 110](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=110)
- sourceLinks 1: [DOC-002 protocol schedule — PDF p. 15](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=15)
- sourceLinks 2: [DOC-001 Methods — PDF p. 4](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=4)
- sourceLinks 3: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | P\_P only; printed 24-month results do not establish that the primary model used that occasion. |
| broadPlanInvolved | 1 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C009 |
| key | 2018::jama.2018.9128::C009 |
| legacyRelationship |  |
| locations | DOC-002 final SAP — PDF p. 110; DOC-002 protocol schedule — PDF p. 15; DOC-001 Methods — PDF p. 4; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | P\_P |
| rationale | The final SAP says six timepoints but enumerates only five. The protocol schedule and article/eTable corroborate 24 months as the likely missing item; the focal contradiction is the SAP total versus its own list. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | The final SAP states six time points but its parenthetical schedule lists only baseline, 3, 9, 12, and 36 months. |
| submissionInvolved | 0 |
| subtype | planned\_schedule\_list\_count |
| suggestedDomain | plan\_material |
| title | Final SAP says six assessment points but enumerates five |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C010

**Revised protocol gives six points but lists seven including 48 months**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C010 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> DOC-002 revised protocol — PDF p. 64; DOC-001 Methods — PDF p. 4; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The revised protocol calls the schedule six points/T1-T6 while listing seven occasions, including 48 months.

### AI rationale

> The revised protocol says six points/T1-T6 but enumerates seven including 48 months, and elsewhere on the page says seven. The article/eTable 36-month horizon is contextual; no missing published 48-month outcome is counted as a report-versus-plan discrepancy.

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

> The revised protocol states 6-points in time (T1-T6) and lists baseline, 3, 9, 12, 24, 36, and 48 months; it also says six collection points. The article and eTable report through 36 months.

#### Evidence 1: Reported-versus-comparator

> Six claimed points versus seven listed occasions; baseline-to-36-month reported schedule has six occasions.

#### Evidence 2: Calculation

> count(baseline, 3, 9, 12, 24, 36, 48) = 7, not 6.

#### Evidence 3: Alternative source-grounded interpretations

> The 48-month visit may have been a separate approved extension outside T1-T6; amendment chronology and the intended distinction are not supplied.

### Source links

- sourceLinks 0: [DOC-002 revised protocol — PDF p. 64](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=64)
- sourceLinks 1: [DOC-001 Methods — PDF p. 4](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=4)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A separately approved 48-month extension outside the six core visits could reconcile the wording; amendment chronology is absent. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C010 |
| key | 2018::jama.2018.9128::C010 |
| legacyRelationship |  |
| locations | DOC-002 revised protocol — PDF p. 64; DOC-001 Methods — PDF p. 4; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | P\_P |
| rationale | The revised protocol says six points/T1-T6 but enumerates seven including 48 months, and elsewhere on the page says seven. The article/eTable 36-month horizon is contextual; no missing published 48-month outcome is counted as a report-versus-plan discrepancy. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | The revised protocol calls the schedule six points/T1-T6 while listing seven occasions, including 48 months. |
| submissionInvolved | 0 |
| subtype | planned\_schedule\_list\_count |
| suggestedDomain | plan\_material |
| title | Revised protocol gives six points but lists seven including 48 months |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C011

**Original protocol labels primary outcome as BMI percentile/BMI% while results use BMI kg/m²**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C011 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-002 original protocol — PDF p. 16; DOC-002 final SAP — PDF p. 110; DOC-001 Outcomes — PDF p. 3; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The original protocol labels the primary outcome BMI Percentile/BMI%, whereas the final SAP, article, and eTable report raw BMI in kg/m².

### AI rationale

> Original protocol BMI Percentile/BMI% wording differs from the final SAP and article/results raw BMI kg/m2 measure, and the original protocol itself supplies the raw-BMI formula. This is explicitly a planned-versus-reported outcome-scale comparison plus an internal/across-version plan-label inconsistency.

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

> The original protocol uses child's BMI Percentile and BMI% while displaying a weight(kg)/height(m²) formula. The final sources analyze/report raw BMI in kg/m², including values such as 17.8.

#### Evidence 1: Reported-versus-comparator

> BMI percentile/BMI% label versus raw-BMI kg/m² formula, analysis label, and reported values.

#### Evidence 2: Calculation

> No arithmetic reconstruction is applicable; this is a categorical scale comparison.

#### Evidence 3: Alternative source-grounded interpretations

> BMI% may be erroneous shorthand for raw BMI, or a protocol amendment may have changed the primary outcome scale; neither explanation is resolved in the supplied package.

### Source links

- sourceLinks 0: [DOC-002 original protocol — PDF p. 16](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=16)
- sourceLinks 1: [DOC-002 final SAP — PDF p. 110](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=110)
- sourceLinks 2: [DOC-001 Outcomes — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 3: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed plan/report and plan-internal relationships. The original label may have been shorthand/typo or the scale may have changed; the amendment summary mentions model changes but does not explain this label transition. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C011 |
| key | 2018::jama.2018.9128::C011 |
| legacyRelationship |  |
| locations | DOC-002 original protocol — PDF p. 16; DOC-002 final SAP — PDF p. 110; DOC-001 Outcomes — PDF p. 3; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2018.9128 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Original protocol BMI Percentile/BMI% wording differs from the final SAP and article/results raw BMI kg/m2 measure, and the original protocol itself supplies the raw-BMI formula. This is explicitly a planned-versus-reported outcome-scale comparison plus an internal/across-version plan-label inconsistency. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | The original protocol labels the primary outcome BMI Percentile/BMI%, whereas the final SAP, article, and eTable report raw BMI in kg/m². |
| submissionInvolved | 0 |
| subtype | planned\_vs\_reported\_outcome\_scale |
| suggestedDomain | protocol\_report |
| title | Original protocol labels primary outcome as BMI percentile/BMI% while results use BMI kg/m² |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C012

**Control-condition session count and duration differ across protocol versions and article**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C012 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-002 original protocol — PDF p. 14; DOC-002 revised protocol — PDF p. 64; DOC-001 abstract — PDF p. 1; DOC-001 Methods — PDF p. 3.

### Candidate statement

> The supplied original protocol, revised protocol, and article describe control exposure as 12×60, 7×45, and 6×30 minutes, respectively, without a supplied component mapping.

### AI rationale

> Control exposure is 12x60 minutes in the original protocol, 7x45 in the revised protocol, and 6x30 in the article. The card expressly compares both plan versions and their relation to the reported intervention, so P\_R and P\_P apply.

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

> Original protocol: 12 quarterly 60-minute control sessions. Revised protocol: seven 45-minute school-readiness/success programs. Article: six 30-minute group activities.

#### Evidence 1: Reported-versus-comparator

> 12 × 60 versus 7 × 45 versus 6 × 30 minutes for descriptions of the control school-readiness exposure.

#### Evidence 2: Calculation

> 12 × 60 = 720 minutes; 7 × 45 = 315 minutes; 6 × 30 = 180 minutes.

#### Evidence 3: Alternative source-grounded interpretations

> The versions may describe changed plans, ancillary components, or actual delivery. Session logs and a chronology/mapping of newsletters, field trips, baseline sessions, and activities are not supplied.

### Source links

- sourceLinks 0: [DOC-002 original protocol — PDF p. 14](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=14)
- sourceLinks 1: [DOC-002 revised protocol — PDF p. 64](../../../2018/jama.2018.9128/joi180075supp1_prod.pdf#page=64)
- sourceLinks 2: [DOC-001 abstract — PDF p. 1](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=1)
- sourceLinks 3: [DOC-001 Methods — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed between-plan-version and report-versus-plan relationships. Successive amendments, ancillary components, baseline/48-month visits, and actual delivery could explain the differences; no mapping or delivery logs are supplied. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C012 |
| key | 2018::jama.2018.9128::C012 |
| legacyRelationship |  |
| locations | DOC-002 original protocol — PDF p. 14; DOC-002 revised protocol — PDF p. 64; DOC-001 abstract — PDF p. 1; DOC-001 Methods — PDF p. 3. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism | intervention\_delivery |
| primary | P\_R |
| rationale | Control exposure is 12x60 minutes in the original protocol, 7x45 in the revised protocol, and 6x30 in the article. The card expressly compares both plan versions and their relation to the reported intervention, so P\_R and P\_P apply. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C012 |
| sourceStatus | Pending Human Adjudication |
| statement | The supplied original protocol, revised protocol, and article describe control exposure as 12×60, 7×45, and 6×30 minutes, respectively, without a supplied component mapping. |
| submissionInvolved | 0 |
| subtype | planned\_vs\_reported\_control\_exposure |
| suggestedDomain | protocol\_report |
| title | Control-condition session count and duration differ across protocol versions and article |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C013

**Control 9-month BMI-observation count differs across result displays**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.9128::C013 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2.

### Candidate statement

> The control 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable.

### AI rationale

> The control 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement.

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

> Figure 1 prints control 282 BMI measured at 9 mo; Figure 2 and eTable 1 each print 280.

#### Evidence 1: Reported-versus-comparator

> 282 versus 280 for control, 9 months.

#### Evidence 2: Calculation

> 282 - 280 = 2.

#### Evidence 3: Alternative source-grounded interpretations

> An unreported post-collection analytic or descriptive subset could explain the difference, but the supplied sources do not define it.

### Source links

- sourceLinks 0: [DOC-001 Figure 1 — PDF p. 3](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=3)
- sourceLinks 1: [DOC-001 Figure 2 — PDF p. 7](../../../2018/jama.2018.9128/jama_barkin_2018_oi_180075.pdf#page=7)
- sourceLinks 2: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.9128/joi180075supp2_prod.pdf#page=2)
- evidencePaths 0: [2018/jama.2018.9128/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.9128/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.9128/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-flow versus main-graph and main-flow versus results-eTable comparison; graph/eTable agree. A cleaned descriptive subset could explain the counts, but its inclusion rule is absent. Each arm/visit is a distinct repeated-result record, not an identical duplicate. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C013 |
| key | 2018::jama.2018.9128::C013 |
| legacyRelationship |  |
| locations | DOC-001 Figure 1 — PDF p. 3; DOC-001 Figure 2 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2018.9128 |
| planMechanism |  |
| primary | S\_C |
| rationale | The control 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.9128/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C013 |
| sourceStatus | Pending Human Adjudication |
| statement | The control 9-month BMI count is 282 in the flow diagram and 280 in both the observed-BMI figure and eTable. |
| submissionInvolved | 1 |
| subtype | repeated\_bmi\_observation\_count |
| suggestedDomain | report\_internal\_inconsistency |
| title | Control 9-month BMI-observation count differs across result displays |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
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
