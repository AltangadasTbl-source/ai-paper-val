# jama.2024.19585

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2024 |
| Paper | jama.2024.19585 |
| Candidates | 3 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2024/jama.2024.19585/)

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

- [C001](#candidate-c001) — Usual-care exclusion hierarchy requires source-layout confirmation (S_W)
- [C002](#candidate-c002) — Main-text rejected-statement percentage conflicts with the supplement counts (S_C)
- [C003](#candidate-c003) — eTable 10 labels logistic-regression odds ratios as differences (S_W)

## Candidate C001

**Usual-care exclusion hierarchy requires source-layout confirmation**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.19585::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | exclude |

### Source location

> jama\_dupuis\_2024\_oi\_240111\_1733431204.38761.pdf — Figure 1, PDF p. 5, usual-care branch.

### Candidate statement

> Stable C001 is retained for human confirmation of Figure 1's visual parent-child hierarchy. The direct source supports reconciliation, not a 71-versus-58 mismatch: the nested reasons sum to their parent and the top-level reasons sum to 58.

### AI rationale

> The retained candidate concerns nested counts within main Figure1; recheck explicitly finds7+4+2=13 and top-level sum58, reconciling the displayed total.

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

> The source prints 58 Patients excluded. Visual indentation places 13 Physician preference at the top level and 7 Disease status or progression, 4 Perceived psychosocial issues, and 2 Reason not provided beneath it. The other top-level counts are 15, 14, 7, 4, 3, and 2. The parallel branch presents a matching parent-child convention: 32 + 4 + 2 + 4 = 42.

#### Evidence 1: Reported-versus-comparator

> The printed exclusion total is 58; the source-layout comparator is the top-level hierarchy, not a flat list of all displayed counts.

#### Evidence 2: Calculation

> 7 + 4 + 2 = 13. Then 13 + 15 + 14 + 7 + 4 + 3 + 2 = 58. The surrounding flow also reconciles: 323 - 58 = 265 and 265 - 41 = 224.

#### Evidence 3: Alternative source-grounded interpretations

> A production-layout error could make the indentation misleading, although the parallel branch supports the hierarchy interpretation. No flat 71-versus-58 comparison is carried forward.

### Source links

- sourceLinks 0: [jama\_dupuis\_2024\_oi\_240111\_1733431204.38761.pdf — Figure 1, PDF p. 5](../../../2024/jama.2024.19585/jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5)
- evidencePaths 0: [2024/jama.2024.19585/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.19585/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.19585/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.19585/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.19585/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | NOT REPRODUCED: prior71-versus58 sum double-counted the13 parent; stable ID retained only for production-layout confirmation. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2024::jama.2024.19585::C001 |
| legacyRelationship |  |
| locations | jama\_dupuis\_2024\_oi\_240111\_1733431204.38761.pdf — Figure 1, PDF p. 5, usual-care branch. |
| originalCrossDocument | 0 |
| package | jama.2024.19585 |
| planMechanism |  |
| primary | S\_W |
| rationale | The retained candidate concerns nested counts within main Figure1; recheck explicitly finds7+4+2=13 and top-level sum58, reconciling the displayed total. |
| reportHref | ../../2024/jama.2024.19585/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.19585/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Stable C001 is retained for human confirmation of Figure 1's visual parent-child hierarchy. The direct source supports reconciliation, not a 71-versus-58 mismatch: the nested reasons sum to their parent and the top-level reasons sum to 58. |
| submissionInvolved | 1 |
| subtype | flow\_hierarchy |
| suggestedDomain | statistical\_results |
| title | Usual-care exclusion hierarchy requires source-layout confirmation |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | exclude |

## Candidate C002

**Main-text rejected-statement percentage conflicts with the supplement counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.19585::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_dupuis\_2024\_oi\_240111\_1733431204.38761.pdf — narrative, PDF p. 2 and joi240111supp2\_prod\_1733431204.76024.pdf — eTable 3, PDF p. 6.

### Candidate statement

> The main text reports 6.4% rejected across intervention sites, whereas the displayed eTable 3 reject counts and equal denominators imply 142/1,350 = 10.5%.

### AI rationale

> Main rejected-statement percentage6.4% conflicts with142/1350=10.5% from the supplied non-plan eTable3 site counts.

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

> The main text prints 40.8% adopted, 48.7% adapted, and 6.4% rejected across intervention sites. eTable 3 prints n=135 at each of 10 sites and reject counts of 15, 23, 5, 25, 9, 25, 12, 11, 11, and 6.

#### Evidence 1: Reported-versus-comparator

> Reported: 6.4% rejected. Comparator from the displayed eTable 3 rejection counts and denominators: 10.5% to one decimal place.

#### Evidence 2: Calculation

> Rejects = 15 + 23 + 5 + 25 + 9 + 25 + 12 + 11 + 11 + 6 = 142; total decisions = 10 x 135 = 1,350; 142 / 1,350 x 100 = 10.5185...%, or 10.5%. Keep and adapt totals are 551 and 657, reproducing 40.8% and 48.7%, respectively.

#### Evidence 3: Alternative source-grounded interpretations

> The narrative could use an unprinted unique-statement population or narrower rejection definition rather than site-statement decisions. The supplied locations do not provide the numerator, denominator, exclusions, weighting, or aggregation rule necessary to reproduce 6.4%; equal site denominators make ordinary weighting insufficient as an explanation.

### Source links

- sourceLinks 0: [jama\_dupuis\_2024\_oi\_240111\_1733431204.38761.pdf — narrative, PDF p. 2](../../../2024/jama.2024.19585/jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=2)
- sourceLinks 1: [joi240111supp2\_prod\_1733431204.76024.pdf — eTable 3, PDF p. 6](../../../2024/jama.2024.19585/joi240111supp2_prod_1733431204.76024.pdf#page=6)
- evidencePaths 0: [2024/jama.2024.19585/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.19585/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.19585/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A different unreported rejection population/definition remains possible. |
| broadPlanInvolved | 0 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2024::jama.2024.19585::C002 |
| legacyRelationship |  |
| locations | jama\_dupuis\_2024\_oi\_240111\_1733431204.38761.pdf — narrative, PDF p. 2 and joi240111supp2\_prod\_1733431204.76024.pdf — eTable 3, PDF p. 6. |
| originalCrossDocument | 1 |
| package | jama.2024.19585 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main rejected-statement percentage6.4% conflicts with142/1350=10.5% from the supplied non-plan eTable3 site counts. |
| reportHref | ../../2024/jama.2024.19585/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.19585/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The main text reports 6.4% rejected across intervention sites, whereas the displayed eTable 3 reject counts and equal denominators imply 142/1,350 = 10.5%. |
| submissionInvolved | 1 |
| subtype | aggregate\_percentage |
| suggestedDomain | report\_internal\_inconsistency |
| title | Main-text rejected-statement percentage conflicts with the supplement counts |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**eTable 10 labels logistic-regression odds ratios as differences**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.19585::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 start, PDF p. 13; joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 continued values, PDF p. 14; joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 footnote, PDF p. 15; and joi240111supp2\_prod\_1733431204.76024.pdf — eMethods, PDF p. 22.

### Candidate statement

> eTable 10 labels its modeled-effect columns Difference (95% CI), while eMethods states that the documentation, any-intervention, and symptom-specific-intervention analyses estimate odds ratios using logistic regression.

### AI rationale

> Within one results supplement, eTable10 labels modeled effects Difference while eMethods expressly defines the relevant analyses as logistic odds ratios.

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

> On p. 13, eTable 10 prints Difference (95% CI) under each cohort group. Examples include 0.53 (0.28, 1.01) on p. 13 and 5.30 (2.50, 11.24) and 17.96 (1.03, 313.1) on p. 14; p. 15 identifies mixed- or fixed-effects logistic regression for P values. On p. 22, eMethods states that the relevant logistic-regression analyses estimate the odds ratio.

#### Evidence 1: Reported-versus-comparator

> Reported table label: Difference (95% CI). Methods comparator: odds ratio, a multiplicative effect measure with null value 1.

#### Evidence 2: Calculation

> No arithmetic reconstruction is needed. The representative estimates and intervals are organized around the multiplicative null of 1, consistent with the named odds-ratio estimand.

#### Evidence 3: Alternative source-grounded interpretations

> Difference may have been intended as a generic umbrella label for the modeled comparison while every cell remains an odds ratio. The package does not define that usage or identify any block as an additive difference.

### Source links

- sourceLinks 0: [joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 start, PDF p. 13](../../../2024/jama.2024.19585/joi240111supp2_prod_1733431204.76024.pdf#page=13)
- sourceLinks 1: [joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 continued values, PDF p. 14](../../../2024/jama.2024.19585/joi240111supp2_prod_1733431204.76024.pdf#page=14)
- sourceLinks 2: [joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 footnote, PDF p. 15](../../../2024/jama.2024.19585/joi240111supp2_prod_1733431204.76024.pdf#page=15)
- sourceLinks 3: [joi240111supp2\_prod\_1733431204.76024.pdf — eMethods, PDF p. 22](../../../2024/jama.2024.19585/joi240111supp2_prod_1733431204.76024.pdf#page=22)
- evidencePaths 0: [2024/jama.2024.19585/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.19585/.ai_paper_validation/review_1_5_3/source_inventory.md)

[Original Markdown report](../../../2024/jama.2024.19585/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Difference might be an undefined generic heading; numerical odds-ratio error is not established. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2024::jama.2024.19585::C003 |
| legacyRelationship |  |
| locations | joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 start, PDF p. 13; joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 continued values, PDF p. 14; joi240111supp2\_prod\_1733431204.76024.pdf — eTable 10 footnote, PDF p. 15; and joi240111supp2\_prod\_1733431204.76024.pdf — eMethods, PDF p. 22. |
| originalCrossDocument | 0 |
| package | jama.2024.19585 |
| planMechanism |  |
| primary | S\_W |
| rationale | Within one results supplement, eTable10 labels modeled effects Difference while eMethods expressly defines the relevant analyses as logistic odds ratios. |
| reportHref | ../../2024/jama.2024.19585/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.19585/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 10 labels its modeled-effect columns Difference (95% CI), while eMethods states that the documentation, any-intervention, and symptom-specific-intervention analyses estimate odds ratios using logistic regression. |
| submissionInvolved | 1 |
| subtype | effect\_measure\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 10 labels logistic-regression odds ratios as differences |
| year | 2024 |
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
