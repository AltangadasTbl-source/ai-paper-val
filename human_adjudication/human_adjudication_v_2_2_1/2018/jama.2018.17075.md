# jama.2018.17075

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.17075 |
| Candidates | 8 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.17075/)

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

- [C001](#candidate-c001) — Normothermia Injury Severity Score median is below its printed IQR lower endpoint (S_W)
- [C002](#candidate-c002) — Primary risk difference has opposite signs in matched main-article locations (S_W)
- [C003](#candidate-c003) — Intracranial-bleeding effect and P-value reporting conflicts with matched evidence (S_C)
- [C004](#candidate-c004) — Extracranial-bleeding effect and P-value reporting conflicts with matched evidence (S_C)
- [C005](#candidate-c005) — As-treated evacuated-mass-lesion cell reverses count and percentage order (S_W)
- [C006](#candidate-c006) — As-treated non-evacuated-mass-lesion cell reverses count and percentage order (S_W)
- [C007](#candidate-c007) — Adjusted odds-ratio confidence-interval string is malformed (S_W)
- [C008](#candidate-c008) — Abstract male count conflicts with its percentage and Table 1 total (S_W)

## Candidate C001

**Normothermia Injury Severity Score median is below its printed IQR lower endpoint**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 5, Table 1, normothermia Injury Severity Score.

### Candidate statement

> The normothermia Injury Severity Score median is lower than the lower endpoint of its printed IQR.

### AI rationale

> The normothermia Injury Severity Score median is lower than the lower endpoint of its printed IQR. The focal mismatch is within the main article.

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

> The median (IQR) cell prints 20.0 (20.5-35.0) for normothermia.

#### Evidence 1: Reported-versus-comparator

> Reported median 20.0; comparator IQR lower endpoint 20.5 under the same explicit median (IQR) label.

#### Evidence 2: Calculation

> 20.5 - 20.0 = 0.5 Injury Severity Score points; the labelled lower endpoint exceeds the labelled median.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated convention could theoretically alter the reading, but the cell label, parentheses, and parallel hypothermia median/IQR layout support the ordinary interpretation. No alternative definition is printed.

### Source links

- sourceLinks 0: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 5, Table 1, normothermia Injury Severity Score](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=5)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.17075::C001 |
| legacyRelationship |  |
| locations | jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 5, Table 1, normothermia Injury Severity Score. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_W |
| rationale | The normothermia Injury Severity Score median is lower than the lower endpoint of its printed IQR. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The normothermia Injury Severity Score median is lower than the lower endpoint of its printed IQR. |
| submissionInvolved | 1 |
| subtype | median\_iqr\_order |
| suggestedDomain | statistical\_results |
| title | Normothermia Injury Severity Score median is below its printed IQR lower endpoint |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Primary risk difference has opposite signs in matched main-article locations**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 1, abstract Results; PDF p. 5, Primary Outcome Results; PDF p. 7, Table 2 favorable outcome.

### Candidate statement

> The abstract prints a positive primary risk difference while matched Results and Table 2 locations print a negative risk difference with the same displayed counts and CI.

### AI rationale

> The abstract prints a positive primary risk difference while matched Results and Table 2 locations print a negative risk difference with the same displayed counts and CI. The focal mismatch is within the main article.

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

> All locations report hypothermia 117/240 (48.8%), normothermia 111/226 (49.1%), and CI -9.4 to 8.7. The abstract prints risk difference 0.4%; Results and Table 2 print -0.4 percentage points.

#### Evidence 1: Reported-versus-comparator

> Reported abstract point estimate +0.4%; matched comparator Results/Table 2 point estimate -0.4, with the same group order and CI.

#### Evidence 2: Calculation

> (117/240 - 111/226) x 100 = -0.3650 percentage points, rounding to -0.4.

#### Evidence 3: Alternative source-grounded interpretations

> A reversed abstract contrast could produce approximately +0.4, but a correspondingly reversed CI would ordinarily be -8.7 to 9.4; the unchanged printed abstract CI does not fully reconcile that reading.

### Source links

- sourceLinks 0: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 1, abstract Results](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=1)
- sourceLinks 1: [PDF p. 5, Primary Outcome Results](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=5)
- sourceLinks 2: [PDF p. 7, Table 2 favorable outcome](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=7)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C002 |
| key | 2018::jama.2018.17075::C002 |
| legacyRelationship |  |
| locations | jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 1, abstract Results; PDF p. 5, Primary Outcome Results; PDF p. 7, Table 2 favorable outcome. |
| originalCrossDocument | 1 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_W |
| rationale | The abstract prints a positive primary risk difference while matched Results and Table 2 locations print a negative risk difference with the same displayed counts and CI. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The abstract prints a positive primary risk difference while matched Results and Table 2 locations print a negative risk difference with the same displayed counts and CI. |
| submissionInvolved | 1 |
| subtype | repeated\_effect\_sign |
| suggestedDomain | report\_internal\_inconsistency |
| title | Primary risk difference has opposite signs in matched main-article locations |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Intracranial-bleeding effect and P-value reporting conflicts with matched evidence**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C003 |
| Frozen relationship | S\_C |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 7, Table 2, new or increased intracranial bleeding; joi180132supp2\_prod.pdf — PDF p. 10, eTable 6, same outcome; jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 3, Statistical Analysis.

### Candidate statement

> The intracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value.

### AI rationale

> The intracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value. The focal comparison is the main article versus a non-plan results supplement.

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

> Both result locations print 47/260 (18.1%) versus 37/240 (15.4%). Table 2 prints RR 1.23 (0.43-3.5), P=.70; eTable 6 prints P=.43.

#### Evidence 1: Reported-versus-comparator

> Reported Table 2 RR 1.23 and P=.70; comparator printed-proportion RR is approximately 1.17, and the matched eTable P is .43.

#### Evidence 2: Calculation

> (47/260)/(37/240) = 1.1726, rounding to 1.17, not 1.23. A diagnostic log-scale CI is approximately 0.79-1.74 and an uncorrected two-proportion comparison approximately P=.43; these diagnostics do not replace the reported analysis.

#### Evidence 3: Alternative source-grounded interpretations

> A differently modelled effect is conceivable, but Table 2 is labelled Relative Risk and no row-specific adjusted analysis is identified. The neighboring row is a possible source-grounded token-assignment hypothesis only.

### Source links

- sourceLinks 0: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 7, Table 2, new or increased intracranial bleeding](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=7)
- sourceLinks 1: [joi180132supp2\_prod.pdf — PDF p. 10, eTable 6, same outcome](../../../2018/jama.2018.17075/joi180132supp2_prod.pdf#page=10)
- sourceLinks 2: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 3, Statistical Analysis](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=3)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-versus-results-supplement P-value mismatch and within-main RR/count incompatibility. Adjacent intra-/extracranial bleeding rows may have swapped effect tokens, but they are distinct outcomes and are not merged as duplicate IDs. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2018::jama.2018.17075::C003 |
| legacyRelationship |  |
| locations | jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 7, Table 2, new or increased intracranial bleeding; joi180132supp2\_prod.pdf — PDF p. 10, eTable 6, same outcome; jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 3, Statistical Analysis. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_C |
| rationale | The intracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The intracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value. |
| submissionInvolved | 1 |
| subtype | bleeding\_effect\_and\_p\_attachment |
| suggestedDomain | statistical\_results |
| title | Intracranial-bleeding effect and P-value reporting conflicts with matched evidence |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C004

**Extracranial-bleeding effect and P-value reporting conflicts with matched evidence**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C004 |
| Frozen relationship | S\_C |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 7, Table 2, new significant extracranial bleeding; joi180132supp2\_prod.pdf — PDF p. 10, eTable 6, same outcome; jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 3, Statistical Analysis.

### Candidate statement

> The extracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value.

### AI rationale

> The extracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value. The focal comparison is the main article versus a non-plan results supplement.

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

> Both result locations print 8/260 (3.1%) versus 6/240 (2.5%). Table 2 prints RR 1.17 (0.79-1.74), P=.43; eTable 6 prints P=.70.

#### Evidence 1: Reported-versus-comparator

> Reported Table 2 RR 1.17 and P=.43; comparator printed-proportion RR is approximately 1.23, and the matched eTable P is .70.

#### Evidence 2: Calculation

> (8/260)/(6/240) = 1.2308, rounding to 1.23, not 1.17. A diagnostic log-scale CI is approximately 0.43-3.50 and an uncorrected two-proportion comparison approximately P=.70; these diagnostics do not reconstruct the reported analysis.

#### Evidence 3: Alternative source-grounded interpretations

> A differently modelled effect is possible in theory, but no row-specific adjusted analysis is supplied. The adjacent intracranial row mathematically aligns with the printed 1.17 (0.79-1.74), P=.43, which is a hypothesis about token assignment, not an established explanation.

### Source links

- sourceLinks 0: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 7, Table 2, new significant extracranial bleeding](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=7)
- sourceLinks 1: [joi180132supp2\_prod.pdf — PDF p. 10, eTable 6, same outcome](../../../2018/jama.2018.17075/joi180132supp2_prod.pdf#page=10)
- sourceLinks 2: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 3, Statistical Analysis](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=3)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| ambiguity | Mixed main-versus-results-supplement P-value mismatch and within-main RR/count incompatibility. Adjacent intra-/extracranial bleeding rows may have swapped effect tokens, but they are distinct outcomes and are not merged as duplicate IDs. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2018::jama.2018.17075::C004 |
| legacyRelationship |  |
| locations | jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 7, Table 2, new significant extracranial bleeding; joi180132supp2\_prod.pdf — PDF p. 10, eTable 6, same outcome; jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 3, Statistical Analysis. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_C |
| rationale | The extracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value. The focal comparison is the main article versus a non-plan results supplement. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The extracranial-bleeding Table 2 RR/CI/P display conflicts with its printed counts and with the matched supplement P value. |
| submissionInvolved | 1 |
| subtype | bleeding\_effect\_and\_p\_attachment |
| suggestedDomain | statistical\_results |
| title | Extracranial-bleeding effect and P-value reporting conflicts with matched evidence |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C005

**As-treated evacuated-mass-lesion cell reverses count and percentage order**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi180132supp2\_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, evacuated mass lesion V, normothermia.

### Candidate statement

> An as-treated normothermia CT cell is inconsistent with its No. (%) header and displayed denominator.

### AI rationale

> An as-treated normothermia CT cell is inconsistent with its No. (%) header and displayed denominator. The focal mismatch is within one non-plan results supplement.

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

> Under No. (%), normothermia (n=196) prints 34.7 (68); surrounding cells use count followed by percentage.

#### Evidence 1: Reported-versus-comparator

> Reported token order 34.7 (68) versus the count-first header and denominator relationship represented by 68/196.

#### Evidence 2: Calculation

> 68/196 x 100 = 34.6939%, rounding to 34.7%; 34.7 is noninteger in the count position. With the adjacent reconciled category reading, the five CT counts can close at 3 + 108 + 15 + 68 + 2 = 196.

#### Evidence 3: Alternative source-grounded interpretations

> A percentage-first convention would reconcile this one cell, but conflicts with No. (%) and surrounding count-first cells; no row-specific exception is printed.

### Source links

- sourceLinks 0: [joi180132supp2\_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, evacuated mass lesion V, normothermia](../../../2018/jama.2018.17075/joi180132supp2_prod.pdf#page=18)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.17075::C005 |
| legacyRelationship |  |
| locations | joi180132supp2\_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, evacuated mass lesion V, normothermia. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_W |
| rationale | An as-treated normothermia CT cell is inconsistent with its No. (%) header and displayed denominator. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | An as-treated normothermia CT cell is inconsistent with its No. (%) header and displayed denominator. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_order |
| suggestedDomain | report\_internal\_inconsistency |
| title | As-treated evacuated-mass-lesion cell reverses count and percentage order |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C006

**As-treated non-evacuated-mass-lesion cell reverses count and percentage order**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi180132supp2\_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, non-evacuated mass lesion VI, normothermia.

### Candidate statement

> An as-treated normothermia CT cell does not reconcile with its No. (%) header, printed denominator, or displayed category total.

### AI rationale

> An as-treated normothermia CT cell does not reconcile with its No. (%) header, printed denominator, or displayed category total. The focal mismatch is within one non-plan results supplement.

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

> Under No. (%), normothermia (n=196) prints 1 (2); other CT rows print 3 (1.5), 108 (55.1), 15 (7.7), and the adjacent cell 34.7 (68).

#### Evidence 1: Reported-versus-comparator

> Reported literal count/percentage 1 (2) versus 1/196 and the count-total relationship across the five displayed categories.

#### Evidence 2: Calculation

> 1/196 x 100 = 0.5102%, not 2%. Reading count 2 and percentage 1 gives 2/196 x 100 = 1.0204%, and 3 + 108 + 15 + 68 + 2 = 196; literal count 1 produces 195.

#### Evidence 3: Alternative source-grounded interpretations

> A row-specific denominator of 50 could make 1 (2) arithmetically possible, but the table prints n=196, no row-specific denominator/missingness note, and five exhaustive categories.

### Source links

- sourceLinks 0: [joi180132supp2\_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, non-evacuated mass lesion VI, normothermia](../../../2018/jama.2018.17075/joi180132supp2_prod.pdf#page=18)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.17075::C006 |
| legacyRelationship |  |
| locations | joi180132supp2\_prod.pdf — PDF p. 18, eTable 10, CT Marshall classification, non-evacuated mass lesion VI, normothermia. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_W |
| rationale | An as-treated normothermia CT cell does not reconcile with its No. (%) header, printed denominator, or displayed category total. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | An as-treated normothermia CT cell does not reconcile with its No. (%) header, printed denominator, or displayed category total. |
| submissionInvolved | 1 |
| subtype | count\_percentage\_order |
| suggestedDomain | report\_internal\_inconsistency |
| title | As-treated non-evacuated-mass-lesion cell reverses count and percentage order |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C007

**Adjusted odds-ratio confidence-interval string is malformed**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C007 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> joi180132supp2\_prod.pdf — PDF p. 22, post-hoc adequate-cooling Results, final sentence.

### Candidate statement

> The printed adjusted odds-ratio confidence-interval string does not provide two unambiguous endpoints.

### AI rationale

> The printed adjusted odds-ratio confidence-interval string does not provide two unambiguous endpoints. The focal mismatch is within one non-plan results supplement.

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

> The source prints adjusted odds ratio hypothermia vs normothermia; 0.95 (0.55-275 1.64) P = .84.

#### Evidence 1: Reported-versus-comparator

> Reported parenthesized sequence 0.55-275 1.64 versus the same page's explicit odds-ratio (95% CI) convention requiring two identifiable endpoints; the unadjusted example is 0.91 (0.59-1.41) P=.68.

#### Evidence 2: Calculation

> The ordered sequence is 0.55, 275, 1.64. Although point estimate 0.95 lies between 0.55 and 1.64, no source-based calculation identifies the role of 275 or licenses removal of it.

#### Evidence 3: Alternative source-grounded interpretations

> The same-page syntax supports a possible 0.55-1.64 interval with an extraneous token, but the PDF does not define 275; punctuation or digits may instead be missing.

### Source links

- sourceLinks 0: [joi180132supp2\_prod.pdf — PDF p. 22, post-hoc adequate-cooling Results, final sentence](../../../2018/jama.2018.17075/joi180132supp2_prod.pdf#page=22)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| id | C007 |
| key | 2018::jama.2018.17075::C007 |
| legacyRelationship |  |
| locations | joi180132supp2\_prod.pdf — PDF p. 22, post-hoc adequate-cooling Results, final sentence. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_W |
| rationale | The printed adjusted odds-ratio confidence-interval string does not provide two unambiguous endpoints. The focal mismatch is within one non-plan results supplement. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed adjusted odds-ratio confidence-interval string does not provide two unambiguous endpoints. |
| submissionInvolved | 1 |
| subtype | malformed\_ci\_string |
| suggestedDomain | statistical\_results |
| title | Adjusted odds-ratio confidence-interval string is malformed |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C008

**Abstract male count conflicts with its percentage and Table 1 total**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.17075::C008 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 1, abstract Results; PDF p. 5, Table 1, Men and Women rows.

### Candidate statement

> The abstract's male count conflicts with both its stated percentage and the Table 1 arm total.

### AI rationale

> The abstract's male count conflicts with both its stated percentage and the Table 1 arm total. The focal mismatch is within the main article.

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

> The abstract states 500 provided ongoing consent and 402 men \[80.2%\]. Table 1 gives hypothermia 207 (79.6) and normothermia 194 (80.8) men, and women 53 (20.4) and 46 (19.2).

#### Evidence 1: Reported-versus-comparator

> Reported abstract 402/500 (80.2%) versus the arithmetic percentage 80.4% and Table 1 male subtotal 207+194=401, which is 80.2% of 500.

#### Evidence 2: Calculation

> 402/500 x 100 = 80.4%. 207 + 194 = 401; 401/500 x 100 = 80.2%; sex-category totals close as 401 + 53 + 46 = 500.

#### Evidence 3: Alternative source-grounded interpretations

> A denominator near 501 could approximate 402 at 80.2%, but the abstract anchors the text to 500 and Table 1 reports all 500 without a missingness note.

### Source links

- sourceLinks 0: [jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 1, abstract Results](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=1)
- sourceLinks 1: [PDF p. 5, Table 1, Men and Women rows](../../../2018/jama.2018.17075/jama_cooper_2018_oi_180132.pdf#page=5)
- evidencePaths 0: [2018/jama.2018.17075/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.17075/.ai_paper_validation/review_1_5_2/source_inventory.md)

[Original Markdown report](../../../2018/jama.2018.17075/.ai_paper_validation/final_report_1_5_2.md)

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
| key | 2018::jama.2018.17075::C008 |
| legacyRelationship |  |
| locations | jama\_cooper\_2018\_oi\_180132.pdf — PDF p. 1, abstract Results; PDF p. 5, Table 1, Men and Women rows. |
| originalCrossDocument | 0 |
| package | jama.2018.17075 |
| planMechanism |  |
| primary | S\_W |
| rationale | The abstract's male count conflicts with both its stated percentage and the Table 1 arm total. The focal mismatch is within the main article. |
| reportHref | ../../2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.17075/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C008 |
| sourceStatus | Pending Human Adjudication |
| statement | The abstract's male count conflicts with both its stated percentage and the Table 1 arm total. |
| submissionInvolved | 1 |
| subtype | sex\_count\_and\_percentage |
| suggestedDomain | statistical\_results |
| title | Abstract male count conflicts with its percentage and Table 1 total |
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
