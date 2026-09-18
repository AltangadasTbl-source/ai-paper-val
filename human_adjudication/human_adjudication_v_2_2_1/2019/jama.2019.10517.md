# jama.2019.10517

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2019 |
| Paper | jama.2019.10517 |
| Candidates | 3 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2019/jama.2019.10517/)

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

- [C001](#candidate-c001) — Table 5 absolute difference does not reproduce from the displayed counts (S_W)
- [C002](#candidate-c002) — HbA1c interaction is labelled with a concentration unit while matched displays use percent (S_C)
- [C003](#candidate-c003) — Protocol recruitment target conflicts between 82 and 98 participants per site (P_P)

## Candidate C001

**Table 5 absolute difference does not reproduce from the displayed counts**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.10517::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> jama\_flint\_2019\_oi\_190079.pdf — PDF p. 9, Table 5, total-cholesterol and LDL rows.

### Candidate statement

> Table 5 prints an absolute unadjusted difference of 4.3% for two rows whose displayed counts and percentages yield approximately 4.4 percentage points under the ordinary raw-proportion calculation and nearest one-decimal rounding. Pending Human Adjudication.

### AI rationale

> Within main Table 5, 9/64 versus 6/62 yields 4.4 percentage points by ordinary one-decimal rounding, while two rows show 4.3. No plan comparator is involved.

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

> Each cited row prints 9/64 (14.1%) for sertraline plus olanzapine and 6/62 (9.7%) for sertraline plus placebo. Each prints 4.3 (-8 to 17.2) in the “Absolute Unadjusted Difference Between Groups, % (95% CI)” column.

#### Evidence 1: Reported-versus-comparator

> Reported point value: 4.3%. Comparator: the first displayed raw proportion minus the second, (9/64 − 6/62) × 100, and independently 14.1 − 9.7 percentage points.

#### Evidence 2: Calculation

> 9/64 = 14.0625% and 6/62 = 9.677419%; (9/64 − 6/62) × 100 = 4.38508065 percentage points, which is 4.4 to one decimal under nearest rounding. The displayed rounded percentages also give 14.1 − 9.7 = 4.4. The gap from the printed 4.3 is about 0.085 percentage point, exceeding a half-unit one-decimal rounding interval of 0.05.

#### Evidence 3: Alternative source-grounded interpretations

> The source may have used truncation, undocumented row-specific denominators, a different estimator, or unprinted analysis-population inputs. The cited table does not identify any such basis. The repeated value could also be an intentional reuse of one result, but that does not establish how 4.3 was obtained.

### Source links

- sourceLinks 0: [jama\_flint\_2019\_oi\_190079.pdf — PDF p. 9](../../../2019/jama.2019.10517/jama_flint_2019_oi_190079.pdf#page=9)
- evidencePaths 0: [2019/jama.2019.10517/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/source_inventory.md)

[Original Markdown report](../../../2019/jama.2019.10517/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Truncation, unprinted denominators, or a distinct estimator could explain the small difference. |
| broadPlanInvolved | 0 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2019::jama.2019.10517::C001 |
| legacyRelationship |  |
| locations | jama\_flint\_2019\_oi\_190079.pdf — PDF p. 9, Table 5, total-cholesterol and LDL rows. |
| originalCrossDocument | 0 |
| package | jama.2019.10517 |
| planMechanism |  |
| primary | S\_W |
| rationale | Within main Table 5, 9/64 versus 6/62 yields 4.4 percentage points by ordinary one-decimal rounding, while two rows show 4.3. No plan comparator is involved. |
| reportHref | ../../2019/jama.2019.10517/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.10517/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 5 prints an absolute unadjusted difference of 4.3% for two rows whose displayed counts and percentages yield approximately 4.4 percentage points under the ordinary raw-proportion calculation and nearest one-decimal rounding. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | effect\_arithmetic |
| suggestedDomain | statistical\_results |
| title | Table 5 absolute difference does not reproduce from the displayed counts |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**HbA1c interaction is labelled with a concentration unit while matched displays use percent**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.10517::C002 |
| Frozen relationship | S\_C |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> jama\_flint\_2019\_oi\_190079.pdf — PDF p. 1, abstract Results; jama\_flint\_2019\_oi\_190079.pdf — PDF p. 7, Secondary Outcomes; jama\_flint\_2019\_oi\_190079.pdf — PDF p. 8, Table 4; and joi190079supp2\_prod.pdf — PDF p. 9, eFigure 8.

### Candidate statement

> The same HbA1c daily treatment-by-time estimate is labelled mg/dL in two main-article locations, whereas matched table and longitudinal figure displays label HbA1c as percent. Pending Human Adjudication.

### AI rationale

> Main abstract/Results label the HbA1c interaction mg/dL while main Table 4 and the matched longitudinal figure in the results supplement label HbA1c percent. The card explicitly compares both report components, with an additional within-main unit mismatch.

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

> Main-article pages 1 and 7 print the HbA1c daily treatment-by-linear-time result as −0.0002 mg/dL (95% CI, −0.0021 to 0.0016); page 7 reports adjusted P = .99. Table 4 labels the outcome HbA1c, %, and eFigure 8 labels its axis HbA1c (%) for the matched mixed-model display.

#### Evidence 1: Reported-versus-comparator

> Reported label: mg/dL for the repeated interaction coefficient and interval. Comparator labels: % in Table 4 and HbA1c (%) in eFigure 8 for the same named outcome.

#### Evidence 2: Calculation

> This is a label comparison, not a numeric conversion. The coefficient and interval match exactly across pages 1 and 7. No conversion between mg/dL and %, or definition of a distinct transformed HbA1c variable, is supplied.

#### Evidence 3: Alternative source-grounded interpretations

> The repeated mg/dL label could be a production carryover from surrounding metabolic measures. Alternatively, the model may have used a transformed outcome whose unit was not defined. The supplied sources do not distinguish these possibilities or establish an intended replacement label.

### Source links

- sourceLinks 0: [jama\_flint\_2019\_oi\_190079.pdf — PDF p. 1](../../../2019/jama.2019.10517/jama_flint_2019_oi_190079.pdf#page=1)
- sourceLinks 1: [jama\_flint\_2019\_oi\_190079.pdf — PDF p. 7](../../../2019/jama.2019.10517/jama_flint_2019_oi_190079.pdf#page=7)
- sourceLinks 2: [jama\_flint\_2019\_oi\_190079.pdf — PDF p. 8](../../../2019/jama.2019.10517/jama_flint_2019_oi_190079.pdf#page=8)
- sourceLinks 3: [joi190079supp2\_prod.pdf — PDF p. 9](../../../2019/jama.2019.10517/joi190079supp2_prod.pdf#page=9)
- evidencePaths 0: [2019/jama.2019.10517/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.10517/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.10517/.ai_paper_validation/final_report_1_5_1.md)

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
| ambiguity | Mixed cross-file and within-main unit comparisons; an undefined outcome transformation remains an alternative. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2019::jama.2019.10517::C002 |
| legacyRelationship |  |
| locations | jama\_flint\_2019\_oi\_190079.pdf — PDF p. 1, abstract Results; jama\_flint\_2019\_oi\_190079.pdf — PDF p. 7, Secondary Outcomes; jama\_flint\_2019\_oi\_190079.pdf — PDF p. 8, Table 4; and joi190079supp2\_prod.pdf — PDF p. 9, eFigure 8. |
| originalCrossDocument | 0 |
| package | jama.2019.10517 |
| planMechanism |  |
| primary | S\_C |
| rationale | Main abstract/Results label the HbA1c interaction mg/dL while main Table 4 and the matched longitudinal figure in the results supplement label HbA1c percent. The card explicitly compares both report components, with an additional within-main unit mismatch. |
| reportHref | ../../2019/jama.2019.10517/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.10517/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The same HbA1c daily treatment-by-time estimate is labelled mg/dL in two main-article locations, whereas matched table and longitudinal figure displays label HbA1c as percent. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | unit\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | HbA1c interaction is labelled with a concentration unit while matched displays use percent |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_C |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**Protocol recruitment target conflicts between 82 and 98 participants per site**

| Reference | Value |
| --- | --- |
| Candidate key | 2019::jama.2019.10517::C003 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> joi190079supp1\_prod.pdf — PDF p. 7, Figure 1 and Section 3.9.1; joi190079supp1\_prod.pdf — PDF p. 17, Table 4; and joi190079supp1\_prod.pdf — PDF p. 21, Section 4.2.1.

### Candidate statement

> Within the protocol/SAP, four sites recruiting 98 acute participants each reconcile with an acute total of 392, while another statement says each of four sites will recruit 82 patients without a stated population, phase, or version distinction. Pending Human Adjudication.

### AI rationale

> The same protocol/data-analytic-plan PDF specifies 98 acute recruits per site and 392 overall at four sites, but elsewhere says 82 per site (328). This is entirely inside the plan document.

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

> Page 7 prints Acute Phase (N=392) and enrollment across four sites. Page 17 states that each site will recruit 98 acutely ill participants and randomize 44 remitted participants. Page 21 states that four research sites will each recruit 82 patients with the stated psychotic-depression population.

#### Evidence 1: Reported-versus-comparator

> Reported statement: 82 patients per site. Comparator: 98 acutely ill participants per site and total acute N=392, all within the same supplied protocol/SAP.

#### Evidence 2: Calculation

> 98 × 4 = 392, reproducing the acute total. 82 × 4 = 328, 64 below 392. The per-site values differ by 98 − 82 = 16. The separate randomized target, 44 × 4 = 176, agrees with the planned discontinuation RCT total and does not resolve the acute-recruitment mismatch.

#### Evidence 3: Alternative source-grounded interpretations

> The 82/site statement may describe an earlier or amended target, a human-subjects subset, or another denominator; 98/site may represent all acutely ill participants. None of the cited passages labels a distinct version, subset, phase, or time basis that resolves the difference.

### Source links

- sourceLinks 0: [joi190079supp1\_prod.pdf — PDF p. 7](../../../2019/jama.2019.10517/joi190079supp1_prod.pdf#page=7)
- sourceLinks 1: [joi190079supp1\_prod.pdf — PDF p. 17](../../../2019/jama.2019.10517/joi190079supp1_prod.pdf#page=17)
- sourceLinks 2: [joi190079supp1\_prod.pdf — PDF p. 21](../../../2019/jama.2019.10517/joi190079supp1_prod.pdf#page=21)
- evidencePaths 0: [2019/jama.2019.10517/.ai\_paper\_validation/review\_1\_5\_1/source\_inventory.md](../../../2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/source_inventory.md)
- evidencePaths 1: [2019/jama.2019.10517/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2019/jama.2019.10517/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2019/jama.2019.10517/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Earlier target, phase, or human-subjects subset is possible but not labelled in the compared passages. |
| broadPlanInvolved | 1 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2019::jama.2019.10517::C003 |
| legacyRelationship |  |
| locations | joi190079supp1\_prod.pdf — PDF p. 7, Figure 1 and Section 3.9.1; joi190079supp1\_prod.pdf — PDF p. 17, Table 4; and joi190079supp1\_prod.pdf — PDF p. 21, Section 4.2.1. |
| originalCrossDocument | 0 |
| package | jama.2019.10517 |
| planMechanism |  |
| primary | P\_P |
| rationale | The same protocol/data-analytic-plan PDF specifies 98 acute recruits per site and 392 overall at four sites, but elsewhere says 82 per site (328). This is entirely inside the plan document. |
| reportHref | ../../2019/jama.2019.10517/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2019/jama.2019.10517/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Within the protocol/SAP, four sites recruiting 98 acute participants each reconcile with an acute total of 392, while another statement says each of four sites will recruit 82 patients without a stated population, phase, or version distinction. Pending Human Adjudication. |
| submissionInvolved | 0 |
| subtype | recruitment\_denominator |
| suggestedDomain | plan\_material |
| title | Protocol recruitment target conflicts between 82 and 98 participants per site |
| year | 2019 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
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
