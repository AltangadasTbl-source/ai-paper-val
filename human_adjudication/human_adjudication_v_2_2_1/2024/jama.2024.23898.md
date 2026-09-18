# jama.2024.23898

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2024 |
| Paper | jama.2024.23898 |
| Candidates | 7 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2024/jama.2024.23898/)

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

- [C001](#candidate-c001) — Primary-outcome 72-hour clock origin is not stated consistently (P_R)
- [C002](#candidate-c002) — Postoperative opioid-consumption window is 24 hours versus 72 hours (P_R)
- [C003](#candidate-c003) — Unplanned-readmission window is 90 days versus 30 days (P_R)
- [C004](#candidate-c004) — ERAS subgroup cut points differ from the protocol bands (P_R)
- [C005](#candidate-c005) — The eFigure assigns both 99% and 95% labels to the same intervals (S_W)
- [C006](#candidate-c006) — Day-5 EQ-5D inference conflicts with blanket no-difference prose (S_W)
- [C007](#candidate-c007) — ERAS subgroup is labeled as two levels versus three levels (P_R)

## Candidate C001

**Primary-outcome 72-hour clock origin is not stated consistently**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C001 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 1; main article — PDF p. 5; main article — PDF p. 6; SAP — PDF p. 9.

### Candidate statement

> The matched primary GI-3 result is described as 72 hours “after surgery/operation” in the article but as 72 hours “after the start of operation” in the SAP; the printed clock origin is not explicitly aligned.

### AI rationale

> Main primaryGI-3 labels72hours after surgery/operation, whereas SAP explicitly says72hours after start of operation.

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

> The article reports the same 160/279 versus 164/278 GI-3 result as “72 hours after surgery,” “at 72 hours after operation,” and “by 72 h after operation.”

#### Evidence 1: Reported-versus-comparator

> The SAP defines the same GI-3 composite “at 72 hours after the start of operation.”

#### Evidence 2: Calculation

> No numerical recalculation is claimed. The matched counts and effects agree; the reproducible comparison is the presence versus absence of “start of operation.”

#### Evidence 3: Alternative source-grounded interpretations

> “After surgery/operation” may be shorthand for the SAP origin, or the final derivation may have used completion of surgery, anaesthesia start, or another timestamp not supplied.

### Source links

- sourceLinks 0: [main article — PDF p. 1](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1)
- sourceLinks 1: [main article — PDF p. 5](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5)
- sourceLinks 2: [main article — PDF p. 6](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6)
- sourceLinks 3: [SAP — PDF p. 9](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=9)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/cross\_source\_consistency.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md)
- evidencePaths 2: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | This is ambiguity of timezero, not proven differing derivation; article wording may be shorthand. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C001 |
| key | 2024::jama.2024.23898::C001 |
| legacyRelationship |  |
| locations | main article — PDF p. 1; main article — PDF p. 5; main article — PDF p. 6; SAP — PDF p. 9. |
| originalCrossDocument | 1 |
| package | jama.2024.23898 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Main primaryGI-3 labels72hours after surgery/operation, whereas SAP explicitly says72hours after start of operation. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | The matched primary GI-3 result is described as 72 hours “after surgery/operation” in the article but as 72 hours “after the start of operation” in the SAP; the printed clock origin is not explicitly aligned. |
| submissionInvolved | 0 |
| subtype | outcome\_time\_origin |
| suggestedDomain | protocol\_report |
| title | Primary-outcome 72-hour clock origin is not stated consistently |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C002

**Postoperative opioid-consumption window is 24 hours versus 72 hours**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C002 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 4; main article — PDF p. 6; protocol — PDF p. 17; SAP — PDF p. 11.

### Candidate statement

> The article defines and reports postoperative morphine-equivalent consumption through 24 hours, while the protocol and SAP define the matched endpoint through 72 hours.

### AI rationale

> Main reports cumulative opioid consumption through24hours; protocol and SAP define the matched outcome through72hours.

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

> The article names postoperative opioid consumption “up to 24 hours” and reports OME medians 70.6 mg versus 45.0 mg, each n=210.

#### Evidence 1: Reported-versus-comparator

> The protocol specifies cumulative morphine-equivalent consumption until 72 hours after operation start; the SAP specifies total in-hospital opioid consumption up to 72 hours.

#### Evidence 2: Calculation

> 72 hours − 24 hours = 48 hours. Aggregate 24-hour medians cannot reconstruct 72-hour medians.

#### Evidence 3: Alternative source-grounded interpretations

> The final analysis may intentionally report a distinct 24-hour measure, or the planned 72-hour endpoint may have changed before final analysis.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4)
- sourceLinks 1: [main article — PDF p. 6](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6)
- sourceLinks 2: [protocol — PDF p. 17](../../../2024/jama.2024.23898/joi240139supp1_prod_1741633738.16362.pdf#page=17)
- sourceLinks 3: [SAP — PDF p. 11](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=11)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/cross\_source\_consistency.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md)
- evidencePaths 2: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | A distinct final endpoint or amendment remains possible but no supplied final record resolves it. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C002 |
| key | 2024::jama.2024.23898::C002 |
| legacyRelationship |  |
| locations | main article — PDF p. 4; main article — PDF p. 6; protocol — PDF p. 17; SAP — PDF p. 11. |
| originalCrossDocument | 1 |
| package | jama.2024.23898 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Main reports cumulative opioid consumption through24hours; protocol and SAP define the matched outcome through72hours. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The article defines and reports postoperative morphine-equivalent consumption through 24 hours, while the protocol and SAP define the matched endpoint through 72 hours. |
| submissionInvolved | 0 |
| subtype | outcome\_window |
| suggestedDomain | protocol\_report |
| title | Postoperative opioid-consumption window is 24 hours versus 72 hours |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C003

**Unplanned-readmission window is 90 days versus 30 days**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C003 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 4; main article — PDF p. 8; protocol — PDF p. 18; SAP — PDF p. 10; SAP — PDF p. 27.

### Candidate statement

> Table 3 labels 31 versus 34 unplanned readmissions within 90 days, while article Methods, protocol, and SAP define the endpoint within 30 days.

### AI rationale

> Main Table3 reports readmissions within90days, whereas main Methods and protocol/SAP definitions including dummy-table heading specify30days.

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

> Article Methods says within 30 days; Table 3 says within 90 days and prints 31/279 (11.1%) versus 34/278 (12.2%).

#### Evidence 1: Reported-versus-comparator

> The protocol and SAP (including the SAP dummy-table heading) specify unplanned readmission within 30 days.

#### Evidence 2: Calculation

> 90 days − 30 days = 60 days; 31 / 279 × 100 = 11.11% and 34 / 278 × 100 = 12.23%, reproducing the printed percentages at one decimal place but not the window.

#### Evidence 3: Alternative source-grounded interpretations

> Table 3 may contain 30-day counts under a 90-day label, or the final endpoint may have changed to 90 days while other text remained unrevised.

### Source links

- sourceLinks 0: [main article — PDF p. 4](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4)
- sourceLinks 1: [main article — PDF p. 8](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8)
- sourceLinks 2: [protocol — PDF p. 18](../../../2024/jama.2024.23898/joi240139supp1_prod_1741633738.16362.pdf#page=18)
- sourceLinks 3: [SAP — PDF p. 10](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=10)
- sourceLinks 4: [SAP — PDF p. 27](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=27)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/cross\_source\_consistency.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md)
- evidencePaths 2: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |
| relations | 1 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Mixed report-plan and internal-article discrepancy; actual31/34 counts may be30-day counts under a90-day label or reflect a changed window. |
| broadPlanInvolved | 1 |
| category | Cross-document numeric inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2024::jama.2024.23898::C003 |
| legacyRelationship |  |
| locations | main article — PDF p. 4; main article — PDF p. 8; protocol — PDF p. 18; SAP — PDF p. 10; SAP — PDF p. 27. |
| originalCrossDocument | 1 |
| package | jama.2024.23898 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | Main Table3 reports readmissions within90days, whereas main Methods and protocol/SAP definitions including dummy-table heading specify30days. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 3 labels 31 versus 34 unplanned readmissions within 90 days, while article Methods, protocol, and SAP define the endpoint within 30 days. |
| submissionInvolved | 1 |
| subtype | outcome\_window |
| suggestedDomain | protocol\_report |
| title | Unplanned-readmission window is 90 days versus 30 days |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C004

**ERAS subgroup cut points differ from the protocol bands**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> protocol — PDF p. 17; protocol — PDF p. 18; SAP — PDF p. 15; results supplement — PDF p. 2.

### Candidate statement

> The protocol gives example ERAS compliance bands of 0–30%, 30–60%, and greater than 60%, whereas the eFigure defines low as fewer than 5 and high as at least 7 of 10 criteria; the printed definitions are not directly reconciled.

### AI rationale

> Reported eFigure lowERAS\<5/10 places40% in low, unlike the protocol's example30%-60% middle band.

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

> The eFigure displays high n=191, moderate n=274, low n=92; it defines high as ≥7/10 and low as \<5/10, and says the definitions were not predefined.

#### Evidence 1: Reported-versus-comparator

> The protocol calls its bands “e.g.” 0–30%, 30–60%, and \>60%; the SAP names high/moderate/low without cut points.

#### Evidence 2: Calculation

> 4 / 10 × 100 = 40%. The eFigure classifies 4/10 as low, while 40% is in the protocol’s printed 30–60% example band. 191 + 274 + 92 = 557.

#### Evidence 3: Alternative source-grounded interpretations

> The “e.g.” bands may be illustrative and a final 0–4/5–6/7–10 rule may have superseded them; alternatively, the scales may not have been aligned. The eFigure does not expressly define moderate.

### Source links

- sourceLinks 0: [protocol — PDF p. 17](../../../2024/jama.2024.23898/joi240139supp1_prod_1741633738.16362.pdf#page=17)
- sourceLinks 1: [protocol — PDF p. 18](../../../2024/jama.2024.23898/joi240139supp1_prod_1741633738.16362.pdf#page=18)
- sourceLinks 2: [SAP — PDF p. 15](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=15)
- sourceLinks 3: [results supplement — PDF p. 2](../../../2024/jama.2024.23898/joi240139supp3_prod_1741633738.18862.pdf#page=2)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/cross\_source\_consistency.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/cross_source_consistency.md)
- evidencePaths 2: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Protocol explicitly says e.g.; eFigure says definitions were not predefined. This is a candidate plan/report difference with disclosed exploratory categorization, not proof of protocol violation. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2024::jama.2024.23898::C004 |
| legacyRelationship |  |
| locations | protocol — PDF p. 17; protocol — PDF p. 18; SAP — PDF p. 15; results supplement — PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2024.23898 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Reported eFigure lowERAS\<5/10 places40% in low, unlike the protocol's example30%-60% middle band. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol gives example ERAS compliance bands of 0–30%, 30–60%, and greater than 60%, whereas the eFigure defines low as fewer than 5 and high as at least 7 of 10 criteria; the printed definitions are not directly reconciled. |
| submissionInvolved | 0 |
| subtype | subgroup\_cutpoints |
| suggestedDomain | protocol\_report |
| title | ERAS subgroup cut points differ from the protocol bands |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C005

**The eFigure assigns both 99% and 95% labels to the same intervals**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C005 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> results supplement — PDF p. 2; SAP — PDF p. 15.

### Candidate statement

> The eFigure legend labels horizontal subgroup intervals as 99% CIs, while its caption calls the displayed within-subgroup intervals 95% CIs.

### AI rationale

> One results eFigure labels subgroup intervals99% in its legend and95% in its caption; SAP99% convention supports the legend only.

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

> The eFigure legend says “99% CI”; its caption states that right-hand within-subgroup relative risks have “95% confidence interval.”

#### Evidence 1: Reported-versus-comparator

> The SAP specifies two-sided 1% subgroup tests and corresponding 99% CIs, supporting the legend’s planned convention but not proving the plotted calculation.

#### Evidence 2: Calculation

> 99% − 95% = 4 percentage points; the explicit labels have no rounding tolerance.

#### Evidence 3: Alternative source-grounded interpretations

> The caption may use generic 95% wording, the legend may be incorrect, or different interval types may have been intended but not distinguished.

### Source links

- sourceLinks 0: [results supplement — PDF p. 2](../../../2024/jama.2024.23898/joi240139supp3_prod_1741633738.18862.pdf#page=2)
- sourceLinks 1: [SAP — PDF p. 15](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=15)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Do not count plan involvement merely because SAP corroborates one side of the internal figure-label mismatch. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C005 |
| key | 2024::jama.2024.23898::C005 |
| legacyRelationship |  |
| locations | results supplement — PDF p. 2; SAP — PDF p. 15. |
| originalCrossDocument | 0 |
| package | jama.2024.23898 |
| planMechanism |  |
| primary | S\_W |
| rationale | One results eFigure labels subgroup intervals99% in its legend and95% in its caption; SAP99% convention supports the legend only. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C005 |
| sourceStatus | Pending Human Adjudication |
| statement | The eFigure legend labels horizontal subgroup intervals as 99% CIs, while its caption calls the displayed within-subgroup intervals 95% CIs. |
| submissionInvolved | 1 |
| subtype | confidence\_level\_label |
| suggestedDomain | statistical\_results |
| title | The eFigure assigns both 99% and 95% labels to the same intervals |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C006

**Day-5 EQ-5D inference conflicts with blanket no-difference prose**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C006 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 5; main article — PDF p. 6; SAP — PDF p. 13; SAP — PDF p. 14.

### Candidate statement

> Table 2 reports a day-5 EQ-5D-5L contrast with a 95% CI excluding zero and P=.04, whereas Results says there was no statistically significant EQ-5D-5L difference between groups.

### AI rationale

> Main day5EQ-5D row givesP=.04 and95%CI excluding0 while its Results says no statistically significantEQ-5D difference. SAP confirms the nominal framework.

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

> Day 5 is −0.057 (95% CI, −0.111 to −0.003), P=.04; Results uses blanket “no significant difference” prose for EQ-5D-5L.

#### Evidence 1: Reported-versus-comparator

> The SAP uses 95% CIs apart from subgroups, no secondary-outcome multiplicity adjustment, and time-by-treatment contrasts at each EQ-5D time point.

#### Evidence 2: Calculation

> −0.111 \< −0.057 \< −0.003; zero is outside the interval; .04 \< .05.

#### Evidence 3: Alternative source-grounded interpretations

> The prose may summarize an overall repeated-measures pattern, use an unstated endpoint-level decision rule, or omit mention of a nominal time-point result.

### Source links

- sourceLinks 0: [main article — PDF p. 5](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5)
- sourceLinks 1: [main article — PDF p. 6](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6)
- sourceLinks 2: [SAP — PDF p. 13](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=13)
- sourceLinks 3: [SAP — PDF p. 14](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=14)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | SAP is framework support, not a separately targeted plan/report deviation; overall versus timepoint narrative rule is absent. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C006 |
| key | 2024::jama.2024.23898::C006 |
| legacyRelationship |  |
| locations | main article — PDF p. 5; main article — PDF p. 6; SAP — PDF p. 13; SAP — PDF p. 14. |
| originalCrossDocument | 0 |
| package | jama.2024.23898 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main day5EQ-5D row givesP=.04 and95%CI excluding0 while its Results says no statistically significantEQ-5D difference. SAP confirms the nominal framework. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C006 |
| sourceStatus | Pending Human Adjudication |
| statement | Table 2 reports a day-5 EQ-5D-5L contrast with a 95% CI excluding zero and P=.04, whereas Results says there was no statistically significant EQ-5D-5L difference between groups. |
| submissionInvolved | 1 |
| subtype | narrative\_inference |
| suggestedDomain | statistical\_results |
| title | Day-5 EQ-5D inference conflicts with blanket no-difference prose |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C007

**ERAS subgroup is labeled as two levels versus three levels**

| Reference | Value |
| --- | --- |
| Candidate key | 2024::jama.2024.23898::C007 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> main article — PDF p. 5; SAP — PDF p. 15; results supplement — PDF p. 2.

### Candidate statement

> Article Methods calls the ERAS subgroup “high vs low,” while the SAP and eFigure name high, moderate, and low strata for the displayed interaction.

### AI rationale

> Main Methods callsERAS high versus low, but SAP and reported eFigure identify high/moderate/low for the displayed interaction.

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

> The eFigure prints high n=191, moderate n=274, and low n=92, with one interaction P=.966; the SAP names the same three levels.

#### Evidence 1: Reported-versus-comparator

> The article phrase names only high and low and does not identify it as shorthand or a separate extreme-level contrast.

#### Evidence 2: Calculation

> 191 + 274 + 92 = 557. One interaction P appears beside the three-row factor, supporting a three-level display without reconstructing its coding.

#### Evidence 3: Alternative source-grounded interpretations

> “High vs low” may be shorthand for the three-level factor, or it may describe an extreme-level contrast while the eFigure displays a separate three-level interaction.

### Source links

- sourceLinks 0: [main article — PDF p. 5](../../../2024/jama.2024.23898/jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5)
- sourceLinks 1: [SAP — PDF p. 15](../../../2024/jama.2024.23898/joi240139supp2_prod_1741633738.17362.pdf#page=15)
- sourceLinks 2: [results supplement — PDF p. 2](../../../2024/jama.2024.23898/joi240139supp3_prod_1741633738.18862.pdf#page=2)
- evidencePaths 0: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/source\_inventory.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/source_inventory.md)
- evidencePaths 1: [2024/jama.2024.23898/.ai\_paper\_validation/review\_1\_5\_3/checkers/statistical\_pass\_2.md](../../../2024/jama.2024.23898/.ai_paper_validation/review_1_5_3/checkers/statistical_pass_2.md)

[Original Markdown report](../../../2024/jama.2024.23898/.ai_paper_validation/final_report_1_5_3.md)

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
| ambiguity | Mixed report-plan and main-results-supplement labels; article could use shorthand or describe an extreme-level contrast. Distinct from C004's numerical cutpoints. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C007 |
| key | 2024::jama.2024.23898::C007 |
| legacyRelationship |  |
| locations | main article — PDF p. 5; SAP — PDF p. 15; results supplement — PDF p. 2. |
| originalCrossDocument | 0 |
| package | jama.2024.23898 |
| planMechanism | analysis\_specification |
| primary | P\_R |
| rationale | Main Methods callsERAS high versus low, but SAP and reported eFigure identify high/moderate/low for the displayed interaction. |
| reportHref | ../../2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.html |
| reportPath | 2024/jama.2024.23898/.ai\_paper\_validation/final\_report\_1\_5\_3.md |
| sourceId | C007 |
| sourceStatus | Pending Human Adjudication |
| statement | Article Methods calls the ERAS subgroup “high vs low,” while the SAP and eFigure name high, moderate, and low strata for the displayed interaction. |
| submissionInvolved | 1 |
| subtype | subgroup\_levels |
| suggestedDomain | protocol\_report |
| title | ERAS subgroup is labeled as two levels versus three levels |
| year | 2024 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
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
