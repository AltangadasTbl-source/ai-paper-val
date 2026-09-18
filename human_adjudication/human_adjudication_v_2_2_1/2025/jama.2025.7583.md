# jama.2025.7583

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.7583 |
| Candidates | 3 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.7583/)

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

- [C001](#candidate-c001) — Primary-endpoint midline-shift boundary differs across matched supplied sources (P_R)
- [C002](#candidate-c002) — Printed sample-size attrition allowance does not reconcile with the printed target (P_P)
- [C003](#candidate-c003) — Standard-care surgery-type counts exceed their shared printed denominator (S_W)

## Candidate C001

**Primary-endpoint midline-shift boundary differs across matched supplied sources**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7583::C001 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 3; protocol — PDF p. 7; protocol — PDF p. 16; results supplement — PDF p. 15; SAP — PDF p. 3.

### Candidate statement

> Matched supplied sources define the same six-month primary-endpoint imaging component with different inclusion operators: inclusive \>=5 mm versus strict \>5 mm.

### AI rationale

> Target compares reported current-study content with supplied protocol/SAP specification. The inclusive \`\>=5 mm\` wording in the main article, protocol, and results supplement is compared with the SAP’s strict \`\>5 mm\` wording.

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

> The main article prints “5 mm or greater”; protocol pp. 7 and 16 and the results supplement print \>=5 mm; the SAP prints \>5 mm. Each occurrence is the same six-month homolateral-CSDH primary-endpoint imaging component, alongside the same symptomatic-CSDH alternative.

#### Evidence 1: Reported-versus-comparator

> The inclusive \>=5 mm wording in the main article, protocol, and results supplement is compared with the SAP’s strict \>5 mm wording.

#### Evidence 2: Calculation

> For shift x, x \>= 5 includes x = 5; x \> 5 excludes x = 5. The set difference is the boundary value alone. Rounding cannot reconcile the two operators.

#### Evidence 3: Alternative source-grounded interpretations

> The SAP expression may be typographic or version-specific, or it may state the operational rule while the repeated inclusive expression states a different version. The supplied package does not identify the programmed adjudication rule or report whether any case had exactly 5-mm shift.

### Source links

- sourceLinks 0: [Main article — PDF p. 3](../../../2025/jama.2025.7583/jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3)
- sourceLinks 1: [protocol — PDF p. 7](../../../2025/jama.2025.7583/joi250033supp1_prod_1750956987.76581.pdf#page=7)
- sourceLinks 2: [protocol — PDF p. 16](../../../2025/jama.2025.7583/joi250033supp1_prod_1750956987.76581.pdf#page=16)
- sourceLinks 3: [results supplement — PDF p. 15](../../../2025/jama.2025.7583/joi250033supp4_prod_1750956987.77981.pdf#page=15)
- sourceLinks 4: [SAP — PDF p. 3](../../../2025/jama.2025.7583/joi250033supp5_prod_1750956987.78281.pdf#page=3)
- evidencePaths 0: [2025/jama.2025.7583/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.7583/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.7583/.ai_paper_validation/final_report_1_5_1.md)

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
| ambiguity | Both protocol-versus-SAP and report-versus-SAP endpoint operator explicitly targeted. No case at exactly5 mm identified. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2025::jama.2025.7583::C001 |
| legacyRelationship |  |
| locations | Main article — PDF p. 3; protocol — PDF p. 7; protocol — PDF p. 16; results supplement — PDF p. 15; SAP — PDF p. 3. |
| originalCrossDocument | 0 |
| package | jama.2025.7583 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Target compares reported current-study content with supplied protocol/SAP specification. The inclusive \`\>=5 mm\` wording in the main article, protocol, and results supplement is compared with the SAP’s strict \`\>5 mm\` wording. |
| reportHref | ../../2025/jama.2025.7583/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7583/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | Matched supplied sources define the same six-month primary-endpoint imaging component with different inclusion operators: inclusive \>=5 mm versus strict \>5 mm. |
| submissionInvolved | 0 |
| subtype | Primary-endpoint midline-shift boundary differs across matched supplied sources |
| suggestedDomain | protocol\_report |
| title | Primary-endpoint midline-shift boundary differs across matched supplied sources |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C002

**Printed sample-size attrition allowance does not reconcile with the printed target**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7583::C002 |
| Frozen relationship | P\_P |
| AI suggested domain | plan\_material |
| AI suggested disposition | retain |

### Source location

> Protocol — PDF p. 50; SAP — PDF p. 4; SAP — PDF p. 5; main article — PDF p. 3.

### Candidate statement

> The printed 142-per-group requirement, stated 20% loss-to-follow-up allowance, and 171-per-group/342-total target do not reconcile under a true loss-fraction convention.

### AI rationale

> Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed enrollment is 171 per group/342 total. The comparator is the enrollment required to retain 142 per group after a stated 20% loss fraction.

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

> Protocol and SAP print 142 required participants per group, a 20% loss-to-follow-up assumption, and 342 total participants (171 per group); the main article repeats the 20% allowance and total 342. The protocol and SAP state that 142 per group accounts for the planned sequential tests.

#### Evidence 1: Reported-versus-comparator

> Printed enrollment is 171 per group/342 total. The comparator is the enrollment required to retain 142 per group after a stated 20% loss fraction.

#### Evidence 2: Calculation

> 142 \* 2 = 284. Under a 20%-of-enrollment loss fraction, 284 / 0.80 = 355 aggregate participants. With 1:1 whole-person allocation, 142 / 0.80 = 177.5, requiring 178 per arm and 356 total. The printed target gives 171 \* 0.80 = 136.8 expected retained participants per arm. By contrast, adding 20% to the required count gives 142 \* 1.20 = 170.4, which can round upward to 171 per arm.

#### Evidence 3: Alternative source-grounded interpretations

> The authors may have treated “20% loss” as an addition to the required count, or an unstated sequential-design adjustment or unrounded software output may explain 342. The supplied sources do not state the attrition denominator, calculation convention, separate adjustment, or calculation trace.

### Source links

- sourceLinks 0: [Protocol — PDF p. 50](../../../2025/jama.2025.7583/joi250033supp1_prod_1750956987.76581.pdf#page=50)
- sourceLinks 1: [SAP — PDF p. 4](../../../2025/jama.2025.7583/joi250033supp5_prod_1750956987.78281.pdf#page=4)
- sourceLinks 2: [SAP — PDF p. 5](../../../2025/jama.2025.7583/joi250033supp5_prod_1750956987.78281.pdf#page=5)
- sourceLinks 3: [main article — PDF p. 3](../../../2025/jama.2025.7583/jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3)
- evidencePaths 0: [2025/jama.2025.7583/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.7583/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.7583/.ai_paper_validation/final_report_1_5_1.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_P |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Plan and article AGREE at342 and20%; arithmetic incompatibility is within protocol/SAP full input sequence. Article does not print142. Not report-versus-plan. |
| broadPlanInvolved | 1 |
| category | Numeric or arithmetic inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2025::jama.2025.7583::C002 |
| legacyRelationship |  |
| locations | Protocol — PDF p. 50; SAP — PDF p. 4; SAP — PDF p. 5; main article — PDF p. 3. |
| originalCrossDocument | 0 |
| package | jama.2025.7583 |
| planMechanism |  |
| primary | P\_P |
| rationale | Target is internal to protocol/SAP definitions, calculations, or plan versions; final results are not the conflicting comparator. Printed enrollment is 171 per group/342 total. The comparator is the enrollment required to retain 142 per group after a stated 20% loss fraction. |
| reportHref | ../../2025/jama.2025.7583/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7583/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The printed 142-per-group requirement, stated 20% loss-to-follow-up allowance, and 171-per-group/342-total target do not reconcile under a true loss-fraction convention. |
| submissionInvolved | 0 |
| subtype | Printed sample-size attrition allowance does not reconcile with the printed target |
| suggestedDomain | plan\_material |
| title | Printed sample-size attrition allowance does not reconcile with the printed target |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_P |
| ai\_domain | plan\_material |
| ai\_disposition | retain |

## Candidate C003

**Standard-care surgery-type counts exceed their shared printed denominator**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.7583::C003 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> Main article — PDF p. 5, Table 1, Treatment rows.

### Candidate statement

> In Table 1’s standard-care column, two surgery-type numerators total 164 against their shared printed denominator of 163; clarification is required because the table does not state the participant-versus-procedure overlap rule.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The two printed numerators, 146 and 18, are compared with their repeated denominator, 163, under the table’s participant-framed \`No./total No. (%)\` presentation.

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

> The standard-care column prints 146/163 (89.6%) for trepanation burr-hole craniostomy and 18/163 (11.0%) for trephine craniostomy. The header defines entries as No./total No. (%); footnote e describes procedures performed either with a cranial drill or a skull trephine cylindrical saw.

#### Evidence 1: Reported-versus-comparator

> The two printed numerators, 146 and 18, are compared with their repeated denominator, 163, under the table’s participant-framed No./total No. (%) presentation.

#### Evidence 2: Calculation

> 146 + 18 = 164, one above 163. 146 / 163 \* 100 = 89.570...% rounds to 89.6%, and 18 / 163 \* 100 = 11.042...% rounds to 11.0%; the printed percentages sum to 100.6%. Rounding cannot remove the one-membership integer excess.

#### Evidence 3: Alternative source-grounded interpretations

> A participant with bilateral surgery could have received different techniques and been counted in both rows, allowing 164 row memberships among 163 participants. Alternatively, a printed numerator or denominator may need correction. The package does not establish either explanation.

### Source links

- sourceLinks 0: [Main article — PDF p. 5](../../../2025/jama.2025.7583/jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5)
- evidencePaths 0: [2025/jama.2025.7583/.ai\_paper\_validation/review\_1\_5\_1/verification/evidence\_recheck.md](../../../2025/jama.2025.7583/.ai_paper_validation/review_1_5_1/verification/evidence_recheck.md)

[Original Markdown report](../../../2025/jama.2025.7583/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2025::jama.2025.7583::C003 |
| legacyRelationship |  |
| locations | Main article — PDF p. 5, Table 1, Treatment rows. |
| originalCrossDocument | 0 |
| package | jama.2025.7583 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. The two printed numerators, 146 and 18, are compared with their repeated denominator, 163, under the table’s participant-framed \`No./total No. (%)\` presentation. |
| reportHref | ../../2025/jama.2025.7583/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.7583/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | In Table 1’s standard-care column, two surgery-type numerators total 164 against their shared printed denominator of 163; clarification is required because the table does not state the participant-versus-procedure overlap rule. |
| submissionInvolved | 1 |
| subtype | Standard-care surgery-type counts exceed their shared printed denominator |
| suggestedDomain | statistical\_results |
| title | Standard-care surgery-type counts exceed their shared printed denominator |
| year | 2025 |
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
