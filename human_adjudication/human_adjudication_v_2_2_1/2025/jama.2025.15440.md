# jama.2025.15440

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2025 |
| Paper | jama.2025.15440 |
| Candidates | 2 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2025/jama.2025.15440/)

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

- [C001](#candidate-c001) — Conflicting confidence intervals for the matched any-stroke rate ratio (S_W)
- [C002](#candidate-c002) — Stroke subtype counts do not partition the displayed any-stroke count in the patch group (S_W)

## Candidate C001

**Conflicting confidence intervals for the matched any-stroke rate ratio**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15440::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | report\_internal\_inconsistency |
| AI suggested disposition | retain |

### Source location

> DOC-001: jama\_wijesurendra\_2025\_oi\_250068\_1760999665.28362.pdf — PDF p. 1 (abstract); PDF p. 5 (results narrative); and PDF p. 7 (Figure 4B).

### Candidate statement

> The abstract and detailed results/Figure 4B report the same any-stroke arm counts and rate-ratio point estimate but different 95% confidence-interval endpoints.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Abstract CI 0.76-1.53 versus detailed-results/Figure 4B CI 0.77-1.51 for the same displayed counts, follow-up context, and point estimate.

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

> Page 1 prints patch 69 (2.7%) versus usual care 64 (2.5%), rate ratio 1.08 (95% CI 0.76-1.53). Pages 5 and 7 print the same 69 versus 64 and rate ratio 1.08 but 95% CI 0.77-1.51 for the 2.5-year any-stroke comparison.

#### Evidence 1: Reported-versus-comparator

> Abstract CI 0.76-1.53 versus detailed-results/Figure 4B CI 0.77-1.51 for the same displayed counts, follow-up context, and point estimate.

#### Evidence 2: Calculation

> Lower endpoints differ by 0.77 - 0.76 = 0.01; upper endpoints differ by 1.53 - 1.51 = 0.02. This direct printed-value comparison does not select either interval as correct.

#### Evidence 3: Alternative source-grounded interpretations

> One location may contain a transcription or production-rounding difference; separate interval calculations may have been used but not labeled; or one display may not have received the same update. Event times, O-E, V, unrounded endpoints, and the exact CI procedure are not supplied.

### Source links

- sourceLinks 0: [jama\_wijesurendra\_2025\_oi\_250068\_1760999665.28362.pdf — PDF p. 1](../../../2025/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1)
- sourceLinks 1: [PDF p. 5](../../../2025/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5)
- sourceLinks 2: [PDF p. 7](../../../2025/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7)

[Original Markdown report](../../../2025/jama.2025.15440/.ai_paper_validation/final_report_1_5_1.md)

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
| key | 2025::jama.2025.15440::C001 |
| legacyRelationship |  |
| locations | DOC-001: jama\_wijesurendra\_2025\_oi\_250068\_1760999665.28362.pdf — PDF p. 1 (abstract); PDF p. 5 (results narrative); and PDF p. 7 (Figure 4B). |
| originalCrossDocument | 1 |
| package | jama.2025.15440 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. Abstract CI 0.76-1.53 versus detailed-results/Figure 4B CI 0.77-1.51 for the same displayed counts, follow-up context, and point estimate. |
| reportHref | ../../2025/jama.2025.15440/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15440/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The abstract and detailed results/Figure 4B report the same any-stroke arm counts and rate-ratio point estimate but different 95% confidence-interval endpoints. |
| submissionInvolved | 1 |
| subtype | Conflicting confidence intervals for the matched any-stroke rate ratio |
| suggestedDomain | report\_internal\_inconsistency |
| title | Conflicting confidence intervals for the matched any-stroke rate ratio |
| year | 2025 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | report\_internal\_inconsistency |
| ai\_disposition | retain |

## Candidate C002

**Stroke subtype counts do not partition the displayed any-stroke count in the patch group**

| Reference | Value |
| --- | --- |
| Candidate key | 2025::jama.2025.15440::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001: jama\_wijesurendra\_2025\_oi\_250068\_1760999665.28362.pdf — PDF p. 7, Figure 4B rows Presumed ischemic stroke, Hemorrhagic stroke, and Any stroke, including its caption/footnote. The matching any-stroke total also appears on PDF p. 5 and PDF p. 1.

### Candidate statement

> Figure 4B prints patch-group presumed ischemic and hemorrhagic stroke counts whose sum exceeds the patch-group Any stroke count, while the usual-care counts reconcile.

### AI rationale

> Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. If subtype rows are mutually exclusive participant-level components counted under the same rule, patch subtypes total 72 versus \`Any stroke\` 69, while usual-care subtypes total 64 versus \`Any stroke\` 64.

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

> Figure 4B prints patch/usual care respectively: presumed ischemic stroke 60 (2.4%)/58 (2.3%); hemorrhagic stroke 12 (0.5%)/6 (0.2%); and any stroke 69 (2.7%)/64 (2.5%). The figure labels the columns No. of events (%), describes events from randomization through 2.5 years, and defines presumed ischemic stroke as including unspecified stroke.

#### Evidence 1: Reported-versus-comparator

> If subtype rows are mutually exclusive participant-level components counted under the same rule, patch subtypes total 72 versus Any stroke 69, while usual-care subtypes total 64 versus Any stroke 64.

#### Evidence 2: Calculation

> Patch: 60 + 12 = 72, three above 69. Usual care: 58 + 6 = 64, equal to 64. Displayed patch percentages give 2.4% + 0.5% = 2.9% versus 2.7%, but integer counts establish the observation. The individual percentages reproduce from n = 2520, so percentage rounding does not explain the integer-count relationship.

#### Evidence 3: Alternative source-grounded interpretations

> Stroke types may overlap; one participant may contribute multiple stroke records/types; Any stroke may count unique participants while subtype rows count events; or record-source/classification rules may create overlap. The supplied figure does not specify the necessary counting convention. The usual-care equality does not establish exclusivity.

### Source links

- sourceLinks 0: [jama\_wijesurendra\_2025\_oi\_250068\_1760999665.28362.pdf — PDF p. 7](../../../2025/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=7)
- sourceLinks 1: [PDF p. 5](../../../2025/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=5)
- sourceLinks 2: [PDF p. 1](../../../2025/jama.2025.15440/jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf#page=1)

[Original Markdown report](../../../2025/jama.2025.15440/.ai_paper_validation/final_report_1_5_1.md)

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
| id | C002 |
| key | 2025::jama.2025.15440::C002 |
| legacyRelationship |  |
| locations | DOC-001: jama\_wijesurendra\_2025\_oi\_250068\_1760999665.28362.pdf — PDF p. 7, Figure 4B rows Presumed ischemic stroke, Hemorrhagic stroke, and Any stroke, including its caption/footnote. The matching any-stroke total also appears on PDF p. 5 and PDF p. 1. |
| originalCrossDocument | 0 |
| package | jama.2025.15440 |
| planMechanism |  |
| primary | S\_W |
| rationale | Target is within one main article or one non-plan results supplement/workbook; no substantive plan comparison. If subtype rows are mutually exclusive participant-level components counted under the same rule, patch subtypes total 72 versus \`Any stroke\` 69, while usual-care subtypes total 64 versus \`Any stroke\` 64. |
| reportHref | ../../2025/jama.2025.15440/.ai\_paper\_validation/final\_report\_1\_5\_1.html |
| reportPath | 2025/jama.2025.15440/.ai\_paper\_validation/final\_report\_1\_5\_1.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | Figure 4B prints patch-group presumed ischemic and hemorrhagic stroke counts whose sum exceeds the patch-group Any stroke count, while the usual-care counts reconcile. |
| submissionInvolved | 1 |
| subtype | Stroke subtype counts do not partition the displayed any-stroke count in the patch group |
| suggestedDomain | statistical\_results |
| title | Stroke subtype counts do not partition the displayed any-stroke count in the patch group |
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
