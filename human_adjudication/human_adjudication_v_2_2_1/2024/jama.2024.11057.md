# jama.2024.11057

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2024 |
| Paper | jama.2024.11057 |
| Candidates | 3 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2024/jama.2024.11057/)

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

- [C001](#candidate-c001) — Quit-date pre-message duration conflicts between the main article and both support documents (P_R)
- [C002](#candidate-c002) — eTable 4 labels motivation and confidence as median (IQR) but prints single parenthetical dispersion values (S_W)
- [C003](#candidate-c003) — eAppendix C prints IPWR once for a result otherwise defined and labelled as IPRW (S_W)

## Candidate C001

**Quit-date pre-message duration conflicts between the main article and both support documents**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.11057::C001 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 3; joi240078supp1\_prod\_1739900423.22574.pdf — PDF p. 2; joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 2.

### Candidate statement

> The main article prints a 6-week pre-quit message period, whereas both supplied support documents print a 1-week pre-quit period for the same named intervention and quit-date subgroup. Pending Human Adjudication.

### AI rationale

> Main describes6 pre-quit message weeks, whereas both the study protocol and distinct results supplement describe1 week for the same intervention/subgroup.

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

> D001 states “6 weeks before and 8 weeks after”; D002 states “a week before and 8 weeks afterward”; D003 states “1 week preceding” and 8 weeks afterward.

#### Evidence 1: Reported-versus-comparator

> 6 weeks before in D001 versus 1 week before in D002 and D003, with the intervention name, quit-date subgroup, temporal anchor, and week unit matched. All three print an 8-week post-quit period.

#### Evidence 2: Calculation

> 6 weeks - 1 week = 5 weeks; 6 weeks != 1 week.

#### Evidence 3: Alternative source-grounded interpretations

> The texts may describe different programme versions, the support documents may be outdated, or one printed occurrence may be a production discrepancy. The supplied documents do not establish which explanation applies or which schedule trial participants received.

### Source links

- sourceLinks 0: [jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 3](../../../2024/jama.2024.11057/jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3)
- sourceLinks 1: [joi240078supp1\_prod\_1739900423.22574.pdf — PDF p. 2](../../../2024/jama.2024.11057/joi240078supp1_prod_1739900423.22574.pdf#page=2)
- sourceLinks 2: [joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 2](../../../2024/jama.2024.11057/joi240078supp2_prod_1739900423.24574.pdf#page=2)
- evidencePaths 0: [2024/jama.2024.11057/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.11057/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.11057/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |
| relations | 1 | S\_C |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Mixed report-plan and main-results-supplement relationships; protocol context dated2021 and article2024 permit an unproven program-version change. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2024::jama.2024.11057::C001 |
| legacyRelationship |  |
| locations | jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 3; joi240078supp1\_prod\_1739900423.22574.pdf — PDF p. 2; joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 2. |
| originalCrossDocument | 1 |
| package | jama.2024.11057 |
| planMechanism | intervention\_delivery |
| primary | P\_R |
| rationale | Main describes6 pre-quit message weeks, whereas both the study protocol and distinct results supplement describe1 week for the same intervention/subgroup. |
| reportHref | ../../2024/jama.2024.11057/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.11057/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The main article prints a 6-week pre-quit message period, whereas both supplied support documents print a 1-week pre-quit period for the same named intervention and quit-date subgroup. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | intervention\_duration |
| suggestedDomain | protocol\_report |
| title | Quit-date pre-message duration conflicts between the main article and both support documents |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C002

**eTable 4 labels motivation and confidence as median (IQR) but prints single parenthetical dispersion values**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.11057::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 12, eTable 4; joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 13, scale footnote; jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 4, Table 1 comparator.

### Candidate statement

> eTable 4 labels the motivation and confidence rows median (IQR) but prints one parenthetical number in each affected cell, unlike its own endpoint-form IQR convention. Pending Human Adjudication.

### AI rationale

> Results-supplement eTable4 labels cells median(IQR) but gives single dispersion values unlike its own endpoint-pair convention. Main Table1 supports the format convention but concerns different groupings.

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

> eTable 4 prints motivation as 4.1 (0.8) in both groups and confidence as 3.2 (1.1) and 3.5 (1.1) under median (IQR). The same table prints other median-IQR rows as endpoint pairs, including 30.0 (27.0-30.0) and 4.0 (3.0-5.0).

#### Evidence 1: Reported-versus-comparator

> A median (IQR) label with one parenthetical value versus the same table's median (IQR) rows with two hyphen-separated endpoint values. D001 Table 1 also uses endpoint-form IQRs for the same measures.

#### Evidence 2: Calculation

> The comparator format has two values inside parentheses; each affected cell has one. Rounding cannot create two unprinted endpoints from one displayed value.

#### Evidence 3: Alternative source-grounded interpretations

> The cells may be means (SDs), scalar IQR widths under an unstated convention, or medians with omitted endpoints. The supplied package does not define the intended convention or provide analysis output to resolve it.

### Source links

- sourceLinks 0: [joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 12](../../../2024/jama.2024.11057/joi240078supp2_prod_1739900423.24574.pdf#page=12)
- sourceLinks 1: [joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 13](../../../2024/jama.2024.11057/joi240078supp2_prod_1739900423.24574.pdf#page=13)
- sourceLinks 2: [jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 4](../../../2024/jama.2024.11057/jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4)
- evidencePaths 0: [2024/jama.2024.11057/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.11057/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck.md](../../../2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/verification/evidence_recheck.md)

[Original Markdown report](../../../2024/jama.2024.11057/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Scalar IQR widths remain possible; main comparator is corroborative, not a matched-result numerical disagreement. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2024::jama.2024.11057::C002 |
| legacyRelationship |  |
| locations | joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 12, eTable 4; joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 13, scale footnote; jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 4, Table 1 comparator. |
| originalCrossDocument | 0 |
| package | jama.2024.11057 |
| planMechanism |  |
| primary | S\_W |
| rationale | Results-supplement eTable4 labels cells median(IQR) but gives single dispersion values unlike its own endpoint-pair convention. Main Table1 supports the format convention but concerns different groupings. |
| reportHref | ../../2024/jama.2024.11057/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.11057/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | eTable 4 labels the motivation and confidence rows median (IQR) but prints one parenthetical number in each affected cell, unlike its own endpoint-form IQR convention. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | summary\_statistic\_label |
| suggestedDomain | report\_internal\_inconsistency |
| title | eTable 4 labels motivation and confidence as median (IQR) but prints single parenthetical dispersion values |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C003

**eAppendix C prints IPWR once for a result otherwise defined and labelled as IPRW**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.11057::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 5, eAppendix C; joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 14, eTable 5; jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 4, Statistical Methods.

### Candidate statement

> eAppendix C prints IPWR once beside the repeated-PPA result even though the same source defines and otherwise uses IPRW, and the matched eTable labels the result IPRW. Pending Human Adjudication.

### AI rationale

> Within the results supplement, the defined IPRW method and matching eTable5 result are called IPWR once in eAppendixC. Main methods corroborate the standard abbreviation.

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

> D003 p. 5 defines IPRW as inverse probability of retention weighting and otherwise uses IPRW, but its repeated-PPA sentence prints IPWR with RR 2.21 (95% CI 1.67-2.93). D003 p. 14 and D001 p. 4 label the matching analysis IPRW.

#### Evidence 1: Reported-versus-comparator

> Undefined IPWR versus the defined and repeatedly printed IPRW for the same weighted repeated-PPA result; the RR and confidence interval match.

#### Evidence 2: Calculation

> IPWR != IPRW; the matched-result anchors are RR 2.21 = 2.21 and 1.67-2.93 = 1.67-2.93.

#### Evidence 3: Alternative source-grounded interpretations

> IPWR could be an unstated second abbreviation, but no supplied source defines it and the identical eTable result is labelled IPRW. A typographical transposition is plausible but is not asserted as a correction.

### Source links

- sourceLinks 0: [joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 5](../../../2024/jama.2024.11057/joi240078supp2_prod_1739900423.24574.pdf#page=5)
- sourceLinks 1: [joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 14](../../../2024/jama.2024.11057/joi240078supp2_prod_1739900423.24574.pdf#page=14)
- sourceLinks 2: [jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 4](../../../2024/jama.2024.11057/jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4)
- evidencePaths 0: [2024/jama.2024.11057/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.11057/.ai\_paper\_validation/review\_1\_5\_3/verification/evidence\_recheck\_C003.md](../../../2024/jama.2024.11057/.ai_paper_validation/review_1_5_3/verification/evidence_recheck_C003.md)

[Original Markdown report](../../../2024/jama.2024.11057/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The substantive mismatch is the undefined transposition against the same supplement's definition and repeated result. |
| broadPlanInvolved | 0 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 0 |
| id | C003 |
| key | 2024::jama.2024.11057::C003 |
| legacyRelationship |  |
| locations | joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 5, eAppendix C; joi240078supp2\_prod\_1739900423.24574.pdf — PDF p. 14, eTable 5; jama\_graham\_2024\_oi\_240078\_1739900423.19074.pdf — PDF p. 4, Statistical Methods. |
| originalCrossDocument | 0 |
| package | jama.2024.11057 |
| planMechanism |  |
| primary | S\_W |
| rationale | Within the results supplement, the defined IPRW method and matching eTable5 result are called IPWR once in eAppendixC. Main methods corroborate the standard abbreviation. |
| reportHref | ../../2024/jama.2024.11057/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.11057/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | eAppendix C prints IPWR once beside the repeated-PPA result even though the same source defines and otherwise uses IPRW, and the matched eTable labels the result IPRW. Pending Human Adjudication. |
| submissionInvolved | 1 |
| subtype | method\_abbreviation |
| suggestedDomain | report\_internal\_inconsistency |
| title | eAppendix C prints IPWR once for a result otherwise defined and labelled as IPRW |
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
