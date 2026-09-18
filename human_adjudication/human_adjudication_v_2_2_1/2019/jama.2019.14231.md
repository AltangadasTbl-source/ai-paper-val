# jama.2019.14231

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.14231 |
| Candidates | 11 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.14231/)

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

- [C001](#candidate-c001) — Protocol matching direction conflicts with the final matched cohort (P_R)
- [C002](#candidate-c002) — Heart-failure ARD does not reconcile with displayed 8-year incidences (S_W)
- [C003](#candidate-c003) — Coronary-disease ARD does not reconcile with displayed 8-year incidences (S_W)
- [C004](#candidate-c004) — Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences (S_W)
- [C005](#candidate-c005) — Nephropathy ARD does not reconcile with displayed 8-year incidences (S_W)
- [C006](#candidate-c006) — Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences (S_W)
- [C007](#candidate-c007) — Supplement tables use different nonsurgical medication denominators at baseline (S_W)
- [C008](#candidate-c008) — Medication comparison is labeled as two different named tests (S_C)
- [C009](#candidate-c009) — Time-varying-HR narrative cites eTable 4 while the displayed table is eTable 7 (S_W)
- [C010](#candidate-c010) — Biguanide count and percentage do not reconcile in eTable 3 (S_W)
- [C011](#candidate-c011) — Standardized-difference footnote says absolute value while columns contain negative values (S_W)

## Candidate C001

**Protocol matching direction conflicts with the final matched cohort**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C001 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 1, PDF p. 3, PDF p. 4; protocol — PDF p. 3.

### Candidate statement

> The protocol’s sentence-level matching direction conflicts with the final article’s realized cohort counts and direction.

### AI rationale

> Protocol says one nonsurgical patient matched to five surgical patients; main report says the opposite, with2287 surgical and11435 nonsurgical patients confirming five controls per surgical patient.

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

> The article reports 2,287 surgical patients and 11,435 matched nonsurgical controls, stating five nonsurgical patients per surgical patient. The protocol says each nonsurgical patient will be matched to five surgical patients.

#### Evidence 1: Reported-versus-comparator

> Final direction and counts: one surgical patient to five nonsurgical controls; protocol wording: one nonsurgical patient to five surgical patients.

#### Evidence 2: Calculation

> 2,287 × 5 = 11,435 nonsurgical controls.

#### Evidence 3: Alternative source-grounded interpretations

> The protocol may contain a planned-method wording inversion or use an unstated ratio convention.

### Source links

- sourceLinks 0: [Main article — PDF p. 1](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=1)
- sourceLinks 1: [PDF p. 3](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=3)
- sourceLinks 2: [PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 3: [protocol — PDF p. 3](../../../2019/jama.2019.14231/joi190103supp2_prod.pdf#page=3)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Protocol grammar may be inverted; implementation code and version history are absent. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2019::jama.2019.14231::C001 |
| legacyRelationship |  |
| locations | Main article — PDF p. 1, PDF p. 3, PDF p. 4; protocol — PDF p. 3. |
| originalCrossDocument | 1 |
| package | jama.2019.14231 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Protocol says one nonsurgical patient matched to five surgical patients; main report says the opposite, with2287 surgical and11435 nonsurgical patients confirming five controls per surgical patient. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol’s sentence-level matching direction conflicts with the final article’s realized cohort counts and direction. |
| submissionInvolved | 0 |
| subtype | matching\_direction |
| suggestedDomain | protocol\_report |
| title | Protocol matching direction conflicts with the final matched cohort |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C002

**Heart-failure ARD does not reconcile with displayed 8-year incidences**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7.

### Candidate statement

> The displayed control-minus-surgery heart-failure ARD does not reconcile with the displayed 8-year cumulative incidences.

### AI rationale

> Main Table2 itself prints heart failure incidences 18.9% and 6.8% together with ARD12.9%, although direct subtraction yields12.1 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy.

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

> Heart-failure incidence is 6.8% for surgery and 18.9% for controls; Table 2 reports ARD 12.9% (95% CI 10.4%-15.1%).

#### Evidence 1: Reported-versus-comparator

> Reported ARD 12.9% versus displayed-incidence subtraction 12.1%.

#### Evidence 2: Calculation

> 18.9% − 6.8% = 12.1%; discrepancy 0.8 percentage point. The two one-decimal display ranges do not overlap a displayed 12.9%.

#### Evidence 3: Alternative source-grounded interpretations

> The ARD point estimate may be separately estimated; the source expressly describes bootstrap CI generation but not a separate ARD point-estimation rule.

### Source links

- sourceLinks 0: [Main article — PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 1: [PDF p. 7](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=7)
- sourceLinks 2: [Supplement 1 — PDF p. 7](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A separate ARD point estimator may explain the discrepancy. Cross-source checker treats matching source displays as concordant; final recheck retains the internal point-estimator question, distinguishing bootstrapped CI from point estimation. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2019::jama.2019.14231::C002 |
| legacyRelationship |  |
| locations | Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 itself prints heart failure incidences 18.9% and 6.8% together with ARD12.9%, although direct subtraction yields12.1 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed control-minus-surgery heart-failure ARD does not reconcile with the displayed 8-year cumulative incidences. |
| submissionInvolved | 1 |
| subtype | effect\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Heart-failure ARD does not reconcile with displayed 8-year incidences |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Coronary-disease ARD does not reconcile with displayed 8-year incidences**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7.

### Candidate statement

> The displayed control-minus-surgery coronary-disease ARD does not reconcile with the displayed 8-year cumulative incidences.

### AI rationale

> Main Table2 itself prints coronary disease incidences 11.6% and 7.9% together with ARD4.2%, although direct subtraction yields3.7 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy.

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

> Coronary-disease incidence is 7.9% for surgery and 11.6% for controls; ARD is 4.2% (1.9%-6.8%).

#### Evidence 1: Reported-versus-comparator

> Reported ARD 4.2% versus displayed-incidence subtraction 3.7%.

#### Evidence 2: Calculation

> 11.6% − 7.9% = 3.7%; discrepancy 0.5 percentage point, beyond ordinary displayed rounding.

#### Evidence 3: Alternative source-grounded interpretations

> A separately bootstrapped or otherwise distinct ARD point estimator may have been used, but is not defined.

### Source links

- sourceLinks 0: [Main article — PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 1: [PDF p. 7](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=7)
- sourceLinks 2: [Supplement 1 — PDF p. 7](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A separate ARD point estimator may explain the discrepancy. Cross-source checker treats matching source displays as concordant; final recheck retains the internal point-estimator question, distinguishing bootstrapped CI from point estimation. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2019::jama.2019.14231::C003 |
| legacyRelationship |  |
| locations | Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 itself prints coronary disease incidences 11.6% and 7.9% together with ARD4.2%, although direct subtraction yields3.7 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed control-minus-surgery coronary-disease ARD does not reconcile with the displayed 8-year cumulative incidences. |
| submissionInvolved | 1 |
| subtype | effect\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Coronary-disease ARD does not reconcile with displayed 8-year incidences |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C004 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7.

### Candidate statement

> The displayed control-minus-surgery cerebrovascular-disease ARD does not reconcile with the displayed 8-year cumulative incidences.

### AI rationale

> Main Table2 itself prints cerebrovascular disease incidences 5.6% and 4.1% together with ARD1.8%, although direct subtraction yields1.5 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy.

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

> Cerebrovascular-disease incidence is 4.1% for surgery and 5.6% for controls; ARD is 1.8% (95% CI -0.03% to 3.4%).

#### Evidence 1: Reported-versus-comparator

> Reported ARD 1.8% versus displayed-incidence subtraction 1.5%.

#### Evidence 2: Calculation

> 5.6% − 4.1% = 1.5%; discrepancy 0.3 percentage point, beyond the approximate 0.10-point rounding bound.

#### Evidence 3: Alternative source-grounded interpretations

> The ARD may use a distinct point estimator not stated in the supplied package.

### Source links

- sourceLinks 0: [Main article — PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 1: [PDF p. 7](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=7)
- sourceLinks 2: [Supplement 1 — PDF p. 7](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A separate ARD point estimator may explain the discrepancy. Cross-source checker treats matching source displays as concordant; final recheck retains the internal point-estimator question, distinguishing bootstrapped CI from point estimation. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C004 |
| key | 2019::jama.2019.14231::C004 |
| legacyRelationship |  |
| locations | Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 itself prints cerebrovascular disease incidences 5.6% and 4.1% together with ARD1.8%, although direct subtraction yields1.5 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed control-minus-surgery cerebrovascular-disease ARD does not reconcile with the displayed 8-year cumulative incidences. |
| submissionInvolved | 1 |
| subtype | effect\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**Nephropathy ARD does not reconcile with displayed 8-year incidences**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7.

### Candidate statement

> The displayed control-minus-surgery nephropathy ARD does not reconcile with the displayed 8-year cumulative incidences.

### AI rationale

> Main Table2 itself prints nephropathy incidences 16.3% and 6.1% together with ARD11.1%, although direct subtraction yields10.2 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy.

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

> Nephropathy incidence is 6.1% for surgery and 16.3% for controls; ARD is 11.1% (8.8%-13.6%).

#### Evidence 1: Reported-versus-comparator

> Reported ARD 11.1% versus displayed-incidence subtraction 10.2%.

#### Evidence 2: Calculation

> 16.3% − 6.1% = 10.2%; discrepancy 0.9 percentage point.

#### Evidence 3: Alternative source-grounded interpretations

> The ARD may be separately estimated, but the table states only bootstrap CI generation and no separate point-estimate rule.

### Source links

- sourceLinks 0: [Main article — PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 1: [PDF p. 7](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=7)
- sourceLinks 2: [Supplement 1 — PDF p. 7](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A separate ARD point estimator may explain the discrepancy. Cross-source checker treats matching source displays as concordant; final recheck retains the internal point-estimator question, distinguishing bootstrapped CI from point estimation. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2019::jama.2019.14231::C005 |
| legacyRelationship |  |
| locations | Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 itself prints nephropathy incidences 16.3% and 6.1% together with ARD11.1%, although direct subtraction yields10.2 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed control-minus-surgery nephropathy ARD does not reconcile with the displayed 8-year cumulative incidences. |
| submissionInvolved | 1 |
| subtype | effect\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Nephropathy ARD does not reconcile with displayed 8-year incidences |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7.

### Candidate statement

> The displayed control-minus-surgery atrial-fibrillation ARD does not reconcile with the displayed 8-year cumulative incidences.

### AI rationale

> Main Table2 itself prints atrial fibrillation incidences 13.6% and 7.9% together with ARD6.5%, although direct subtraction yields5.7 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy.

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

> Atrial-fibrillation incidence is 7.9% for surgery and 13.6% for controls; ARD is 6.5% (4.4%-8.7%).

#### Evidence 1: Reported-versus-comparator

> Reported ARD 6.5% versus displayed-incidence subtraction 5.7%.

#### Evidence 2: Calculation

> 13.6% − 7.9% = 5.7%; discrepancy 0.8 percentage point, beyond ordinary displayed rounding.

#### Evidence 3: Alternative source-grounded interpretations

> The ARD may be separately estimated; the package does not define that point-estimation procedure.

### Source links

- sourceLinks 0: [Main article — PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 1: [PDF p. 7](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=7)
- sourceLinks 2: [Supplement 1 — PDF p. 7](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=7)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A separate ARD point estimator may explain the discrepancy. Cross-source checker treats matching source displays as concordant; final recheck retains the internal point-estimator question, distinguishing bootstrapped CI from point estimation. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2019::jama.2019.14231::C006 |
| legacyRelationship |  |
| locations | Main article — PDF p. 4, PDF p. 7; Supplement 1 — PDF p. 7. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table2 itself prints atrial fibrillation incidences 13.6% and 7.9% together with ARD6.5%, although direct subtraction yields5.7 points. Results supplement repeats agreeing incidences and therefore corroborates the internal main-table arithmetic rather than introducing a cross-file discrepancy. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | The displayed control-minus-surgery atrial-fibrillation ARD does not reconcile with the displayed 8-year cumulative incidences. |
| submissionInvolved | 1 |
| subtype | effect\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C007

**Supplement tables use different nonsurgical medication denominators at baseline**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 5, PDF p. 14.

### Candidate statement

> Two Supplement 1 baseline medication displays use nonsurgical denominators differing by two without a printed reconciliation rule.

### AI rationale

> eTable3 baseline nonsurgical medication N11435 differs from eTable10 year0 N11433; both tables are in the same results supplement.

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

> eTable 3 labels matched nonsurgical baseline medication data N=11,435; eTable 10 labels its nonsurgical year-0 medication-proportion sample 11,433. Both surgery values are 2,287.

#### Evidence 1: Reported-versus-comparator

> eTable 3 nonsurgical N=11,435 versus eTable 10 year-0 nonsurgical N=11,433.

#### Evidence 2: Calculation

> 11,435 − 11,433 = 2 participants.

#### Evidence 3: Alternative source-grounded interpretations

> eTable 10 may be a complete-case or availability subset, while eTable 3 may classify all matched controls.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 5](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=5)
- sourceLinks 1: [PDF p. 14](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=14)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Different medication availability/time-window subsets could account for two participants; the final recheck finds no explicit reconciliation rule. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C007 |
| key | 2019::jama.2019.14231::C007 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 5, PDF p. 14. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | eTable3 baseline nonsurgical medication N11435 differs from eTable10 year0 N11433; both tables are in the same results supplement. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Two Supplement 1 baseline medication displays use nonsurgical denominators differing by two without a printed reconciliation rule. |
| submissionInvolved | 1 |
| subtype | denominator\_definition |
| suggestedDomain | statistical\_results |
| title | Supplement tables use different nonsurgical medication denominators at baseline |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Medication comparison is labeled as two different named tests**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C008 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 4, PDF p. 10; Supplement 1 — PDF p. 12.

### Candidate statement

> Matched medication comparisons are associated with both a two-sample proportions-test label and a Fisher-exact-test label.

### AI rationale

> Main Figure5 calls the matched year8 medication P values Fisher exact tests; main Methods and results-supplement eTable8 call them two-sample proportions tests. The card explicitly targets main/supplement test-label identity, with an internal main-text mismatch too.

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

> Methods and eTable 8 name a two-sample proportions test. Figure 5 labels matched 8-year P values as Fisher exact tests. The same six result-family P values appear, including insulin P=.008 and five P\<.001 values.

#### Evidence 1: Reported-versus-comparator

> Two-sample proportions-test label versus Fisher-exact-test label for the matched year-8 medication result family.

#### Evidence 2: Calculation

> Five matched categories show P\<.001 and insulin shows P=.008 in the Figure 5/eTable 8 family; no test calculation is possible from the supplied aggregate displays.

#### Evidence 3: Alternative source-grounded interpretations

> “Two-sample proportions test” may be a generic family description, or Fisher exact testing may have been used specifically at year 8.

### Source links

- sourceLinks 0: [Main article — PDF p. 4](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=4)
- sourceLinks 1: [PDF p. 10](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=10)
- sourceLinks 2: [Supplement 1 — PDF p. 12](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=12)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)
- evidencePaths 2: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

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
| ambiguity | Two-sample proportions test may be generic or year8 may use a specific method; exact test settings are unavailable. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C008 |
| key | 2019::jama.2019.14231::C008 |
| legacyRelationship |  |
| locations | Main article — PDF p. 4, PDF p. 10; Supplement 1 — PDF p. 12. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main Figure5 calls the matched year8 medication P values Fisher exact tests; main Methods and results-supplement eTable8 call them two-sample proportions tests. The card explicitly targets main/supplement test-label identity, with an internal main-text mismatch too. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched medication comparisons are associated with both a two-sample proportions-test label and a Fisher-exact-test label. |
| submissionInvolved | 1 |
| subtype | statistical\_method\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | Medication comparison is labeled as two different named tests |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C009

**Time-varying-HR narrative cites eTable 4 while the displayed table is eTable 7**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C009 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 6, PDF p. 10, PDF p. 19.

### Candidate statement

> The time-varying-HR narrative cites eTable 4, while the adjacent and repeated display is labeled eTable 7; actual eTable 4 reports a different measure.

### AI rationale

> A narrative in the results supplement cites eTable4 for time-varying HRs, while its adjacent/repeated table is eTable7 and actual eTable4 gives rates. All locations are within the same supplement.

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

> Page 19 says eTable 4 displays adjusted HRs/CIs at 2, 5, and 8 years, whereas the adjacent and repeated table is headed eTable 7. Actual eTable 4 reports cause-specific event rates.

#### Evidence 1: Reported-versus-comparator

> Narrative reference eTable 4 versus matching HR display eTable 7; eTable 4’s displayed content is rates rather than time-varying HRs.

#### Evidence 2: Calculation

> This is a label-and-content identity comparison, not an arithmetic calculation.

#### Evidence 3: Alternative source-grounded interpretations

> The narrative may preserve numbering from an earlier supplement version; the supplied package does not establish the intended wording.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 6](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=6)
- sourceLinks 1: [PDF p. 10](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=10)
- sourceLinks 2: [PDF p. 19](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=19)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C009 |
| key | 2019::jama.2019.14231::C009 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 6, PDF p. 10, PDF p. 19. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | A narrative in the results supplement cites eTable4 for time-varying HRs, while its adjacent/repeated table is eTable7 and actual eTable4 gives rates. All locations are within the same supplement. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C009 |
| sourceStatus | Pending Human Adjudication |
| statement | The time-varying-HR narrative cites eTable 4, while the adjacent and repeated display is labeled eTable 7; actual eTable 4 reports a different measure. |
| submissionInvolved | 1 |
| subtype | cross\_reference |
| suggestedDomain | report\_internal\_inconsistency |
| title | Time-varying-HR narrative cites eTable 4 while the displayed table is eTable 7 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C010

**Biguanide count and percentage do not reconcile in eTable 3**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C010 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Supplement 1 — PDF p. 5.

### Candidate statement

> The surgery-group biguanide count, printed denominator, and printed percentage do not reconcile.

### AI rationale

> Results-supplement eTable3 gives biguanides1530(67.9%) under surgeryN2287, but that fraction rounds66.9%; no cross-file comparator is required.

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

> eTable 3 labels the metabolic-surgery group N=2,287 and prints biguanides as 1,530 (67.9%).

#### Evidence 1: Reported-versus-comparator

> Printed 67.9% versus 66.9% obtained from the printed count and denominator.

#### Evidence 2: Calculation

> 1,530 / 2,287 × 100 = 66.8999…%, which rounds to 66.9%; conversely, 67.9% of 2,287 is approximately 1,552.6.

#### Evidence 3: Alternative source-grounded interpretations

> The count or percentage may be transcribed incorrectly, or a different unprinted denominator may have been used.

### Source links

- sourceLinks 0: [Supplement 1 — PDF p. 5](../../../2019/jama.2019.14231/joi190103supp1_prod.pdf#page=5)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2019::jama.2019.14231::C010 |
| legacyRelationship |  |
| locations | Supplement 1 — PDF p. 5. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable3 gives biguanides1530(67.9%) under surgeryN2287, but that fraction rounds66.9%; no cross-file comparator is required. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C010 |
| sourceStatus | Pending Human Adjudication |
| statement | The surgery-group biguanide count, printed denominator, and printed percentage do not reconcile. |
| submissionInvolved | 1 |
| subtype | count\_percentage |
| suggestedDomain | statistical\_results |
| title | Biguanide count and percentage do not reconcile in eTable 3 |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C011

**Standardized-difference footnote says absolute value while columns contain negative values**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.14231::C011 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 5, PDF p. 6.

### Candidate statement

> Table 1’s footnote defines standardized differences as an absolute value, while the displayed columns include negative values.

### AI rationale

> Main Table1 footnote defines absolute standardized differences but the main table prints negative values. This is an internal definition-versus-display contradiction.

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

> Footnote b defines standardized differences as the “absolute value” of group difference divided by pooled SD. The columns contain negative values including index date -42.6/-15.9, men -28.0/-2.9, and age -75.3/-19.9.

#### Evidence 1: Reported-versus-comparator

> Absolute-value definition versus negative standardized-difference entries.

#### Evidence 2: Calculation

> For any real value x, \|x\| ≥ 0; negative printed values cannot simultaneously be absolute values under the footnote. The signs follow checkable surgery-minus-control examples (for example, men 34.5% versus 48.2% and -28.0).

#### Evidence 3: Alternative source-grounded interpretations

> The columns may intentionally show signed standardized differences in surgery-minus-control direction, with “absolute value” retained in the footnote.

### Source links

- sourceLinks 0: [Main article — PDF p. 5](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=5)
- sourceLinks 1: [PDF p. 6](../../../2019/jama.2019.14231/jama_aminian_2019_oi_190103.pdf#page=6)
- evidencePaths 0: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.14231/.ai\_paper\_validation/review\_1\_5\_1/checkers/cross\_source\_consistency.md](../../../2019/jama.2019.14231/.ai_paper_validation/review_1_5_1/checkers/cross_source_consistency.md)

[Original Markdown report](../../../2019/jama.2019.14231/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2019::jama.2019.14231::C011 |
| legacyRelationship |  |
| locations | Main article — PDF p. 5, PDF p. 6. |
| originalCrossDocument | 0 |
| package | jama.2019.14231 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Table1 footnote defines absolute standardized differences but the main table prints negative values. This is an internal definition-versus-display contradiction. |
| reportHref | ../../2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.14231/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C011 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 1’s footnote defines standardized differences as an absolute value, while the displayed columns include negative values. |
| submissionInvolved | 1 |
| subtype | signed\_measure\_definition |
| suggestedDomain | report\_internal\_inconsistency |
| title | Standardized-difference footnote says absolute value while columns contain negative values |
| year | 2019 |
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
