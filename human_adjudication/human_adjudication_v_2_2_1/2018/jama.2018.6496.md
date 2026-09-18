# jama.2018.6496

[All years](../README.md) · [Usage](../USAGE.md) · [Codebook](../CODEBOOK.md)

| Paper information | Value |
| --- | --- |
| Version | v.2.2.1 |
| Year | 2018 |
| Paper | jama.2018.6496 |
| Candidates | 4 |
| Based on | v.2.1.5.3 |

[Original paper package](../../../2018/jama.2018.6496/)

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

- [C001](#candidate-c001) — Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration (S_W)
- [C002](#candidate-c002) — Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes (S_W)
- [C003](#candidate-c003) — Protocol and published hypoxemia observation windows use different endpoint events (P_R)
- [C004](#candidate-c004) — Protocol and published first-attempt-duration measures use different endpoint events (P_R)

## Candidate C001

**Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.6496::C001 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 3 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2; DOC-003 eTable 1 note — PDF p. 3; DOC-001 statistical-analysis methods — PDF p. 4.

### Candidate statement

> DOC-001 Table 3 prints the all-patient first-attempt-duration confidence limits in descending order (4 to -1); the intended unclustered limits remain unresolved.

### AI rationale

> The main Table 3 CI is printed 4 to -1, a reversed order inside one table. The supplement explicitly recalculates inference for physician clustering and therefore is distinct-model context, not a same-analysis cross-file mismatch.

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

> Table 3 prints all-patient medians of 38 (29 to 51) and 36 (25 to 54) seconds, difference 1 (4 to -1), and P=.24. The main methods name Hodges-Lehmann median between-group differences with associated 95% confidence intervals. The clustered eTable prints 1 s (-1 s to 4 s), P=.95 and states that inferential columns were recalculated for physician clustering.

#### Evidence 1: Reported-versus-comparator

> The reported main-table interval is 4 to -1; the applicable lower-to-upper display convention requires a lower endpoint not greater than the upper endpoint. The clustered interval is contextual distinct-model evidence, not an unclustered replacement.

#### Evidence 2: Calculation

> 4 \> -1; the displayed sequence is decreasing. Reordering to -1 to 4 is only a diagnostic possibility, not an assigned correction.

#### Evidence 3: Alternative source-grounded interpretations

> An unstated reverse-order convention or source-specific transcription could explain the display. The clustered result supports the possibility of a reversed display, but its stated recalculation for physician clustering means it does not establish the intended unclustered values.

### Source links

- sourceLinks 0: [DOC-001 Table 3 — PDF p. 7](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=7)
- sourceLinks 1: [DOC-003 eTable 1 — PDF p. 2](../../../2018/jama.2018.6496/joi180054supp2_prod.pdf#page=2)
- sourceLinks 2: [DOC-003 eTable 1 note — PDF p. 3](../../../2018/jama.2018.6496/joi180054supp2_prod.pdf#page=3)
- sourceLinks 3: [DOC-001 statistical-analysis methods — PDF p. 4](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=4)
- evidencePaths 0: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.6496/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The clustered -1 to 4 interval cannot establish the intended unclustered endpoints. |
| broadPlanInvolved | 0 |
| category | Statistical reporting inconsistency |
| currentReportCrossDocument | 0 |
| id | C001 |
| key | 2018::jama.2018.6496::C001 |
| legacyRelationship |  |
| locations | DOC-001 Table 3 — PDF p. 7; DOC-003 eTable 1 — PDF p. 2; DOC-003 eTable 1 note — PDF p. 3; DOC-001 statistical-analysis methods — PDF p. 4. |
| originalCrossDocument | 0 |
| package | jama.2018.6496 |
| planMechanism |  |
| primary | S\_W |
| rationale | The main Table 3 CI is printed 4 to -1, a reversed order inside one table. The supplement explicitly recalculates inference for physician clustering and therefore is distinct-model context, not a same-analysis cross-file mismatch. |
| reportHref | ../../2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C001 |
| sourceStatus | Pending Human Adjudication |
| statement | DOC-001 Table 3 prints the all-patient first-attempt-duration confidence limits in descending order (4 to -1); the intended unclustered limits remain unresolved. |
| submissionInvolved | 1 |
| subtype | ci\_endpoint\_order |
| suggestedDomain | statistical\_results |
| title | Reverse-ordered confidence-interval endpoints for all-patient first-attempt duration |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C002

**Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.6496::C002 |
| Frozen relationship | S\_W |
| AI suggested domain | statistical\_results |
| AI suggested disposition | retain |

### Source location

> DOC-001 Table 3 — PDF p. 7; DOC-001 Table 5 — PDF p. 9; DOC-002 protocol secondary outcomes — PDF p. 9; DOC-002 analytic issues — PDF p. 21.

### Candidate statement

> The ETT+stylet denominators differ by two across linked waveform-dependent outcomes (366 versus 364), and the supplied aggregate sources do not establish whether the difference is intentional under an outcome-specific denominator rule.

### AI rationale

> Main Tables 3 and 5 use ETT+stylet denominators 366 and 364 for linked composite/hypoxemia outcomes. Protocol definitions explain the relationship and even support outcome-specific missingness; there is no independent inconsistency with the protocol.

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

> Table 3 reports ETT+stylet first-attempt success without hypoxemia as 282/366 (77%). Table 5 reports ETT+stylet hypoxemia as 50/364 (14%). Both footnotes invoke matching hypoxemia threshold/window language and unavailable valid waveform; the Bougie denominators are 371 in both linked rows. The protocol defines success without hypoxemia as first-attempt success plus no hypoxemia.

#### Evidence 1: Reported-versus-comparator

> The ETT+stylet denominators are 366 for the composite and 364 for hypoxemia alone. Denominator identity is expected only if both rows require an observed hypoxemia classification for every denominator member; the printed sources do not state the implemented denominator-construction rule.

#### Evidence 2: Calculation

> 366 - 364 = 2. Relative to the randomized ETT+stylet total, 376 - 366 = 10 and 376 - 364 = 12. Aggregate counts cannot identify the two patients.

#### Evidence 3: Alternative source-grounded interpretations

> A patient known to have failed the first attempt may be deterministically classifiable as not achieving the composite without a usable waveform, while lacking a hypoxemia-only classification. Outcome-specific missing-data handling could therefore make the composite denominator larger. The aggregate sources do not show whether either explanation accounts for these two patients.

### Source links

- sourceLinks 0: [DOC-001 Table 3 — PDF p. 7](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=7)
- sourceLinks 1: [DOC-001 Table 5 — PDF p. 9](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=9)
- sourceLinks 2: [DOC-002 protocol secondary outcomes — PDF p. 9](../../../2018/jama.2018.6496/joi180054supp1_prod.pdf#page=9)
- sourceLinks 3: [DOC-002 analytic issues — PDF p. 21](../../../2018/jama.2018.6496/joi180054supp1_prod.pdf#page=21)
- evidencePaths 0: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.6496/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | S\_W |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | Known first-attempt failures may be classifiable as composite failures without a valid hypoxemia waveform, allowing different denominators. The discrepancy remains conditional and within the main article. |
| broadPlanInvolved | 0 |
| category | Denominator, proportion, or total inconsistency |
| currentReportCrossDocument | 0 |
| id | C002 |
| key | 2018::jama.2018.6496::C002 |
| legacyRelationship |  |
| locations | DOC-001 Table 3 — PDF p. 7; DOC-001 Table 5 — PDF p. 9; DOC-002 protocol secondary outcomes — PDF p. 9; DOC-002 analytic issues — PDF p. 21. |
| originalCrossDocument | 0 |
| package | jama.2018.6496 |
| planMechanism |  |
| primary | S\_W |
| rationale | Main Tables 3 and 5 use ETT+stylet denominators 366 and 364 for linked composite/hypoxemia outcomes. Protocol definitions explain the relationship and even support outcome-specific missingness; there is no independent inconsistency with the protocol. |
| reportHref | ../../2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C002 |
| sourceStatus | Pending Human Adjudication |
| statement | The ETT+stylet denominators differ by two across linked waveform-dependent outcomes (366 versus 364), and the supplied aggregate sources do not establish whether the difference is intentional under an outcome-specific denominator rule. |
| submissionInvolved | 1 |
| subtype | linked\_outcome\_denominators |
| suggestedDomain | statistical\_results |
| title | Two-patient ETT+stylet denominator difference across linked hypoxemia outcomes |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | S\_W |
| ai\_domain | statistical\_results |
| ai\_disposition | retain |

## Candidate C003

**Protocol and published hypoxemia observation windows use different endpoint events**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.6496::C003 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-002 protocol secondary outcomes — PDF p. 9; DOC-002 protocol measurement procedure — PDF p. 10; DOC-001 Table 3 — PDF p. 7; DOC-001 Table 5 — PDF p. 9; DOC-003 eTable 1 note — PDF p. 3; DOC-003 postintubation form — PDF p. 10.

### Candidate statement

> The protocol ends hypoxemia surveillance one minute after ETT-cuff inflation, while the published materials end it one minute after intubation-attempt completion; the supplied package does not document whether those events were treated as equivalent or whether the definition changed.

### AI rationale

> The protocol ends hypoxemia surveillance one minute after ETT-cuff inflation, while the published materials end it one minute after intubation-attempt completion; the supplied package does not document whether those events were treated as equivalent or whether the definition changed. The reported article/results definition is compared substantively with the supplied protocol or SAP.

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

> DOC-002 states that hypoxemia observation begins at first-attempt start and ends one minute after ETT-cuff inflation; page 10 repeats the cuff-inflation endpoint and 20-second recording schedule. DOC-001 Tables 3 and 5 and DOC-003 eTable 1 describe hypoxemia during or within one minute after completion of the intubation attempt. DOC-003 defines attempt 1 end as blade removal.

#### Evidence 1: Reported-versus-comparator

> The threshold and starting event agree. The planned endpoint is one minute after cuff inflation; the published endpoint is one minute after attempt completion/blade removal. These are nonidentical named procedural events.

#### Evidence 2: Calculation

> No numeric recalculation is applicable. The reproducible comparison is one minute after ETT-cuff inflation versus one minute after attempt completion/blade removal.

#### Evidence 3: Alternative source-grounded interpretations

> “Attempt completion” could be shorthand for cuff inflation, or the events could have occurred close together in practice. The data form explicitly defines attempt end as blade removal, so operational equivalence is not established by the supplied package.

### Source links

- sourceLinks 0: [DOC-002 protocol secondary outcomes — PDF p. 9](../../../2018/jama.2018.6496/joi180054supp1_prod.pdf#page=9)
- sourceLinks 1: [DOC-002 protocol measurement procedure — PDF p. 10](../../../2018/jama.2018.6496/joi180054supp1_prod.pdf#page=10)
- sourceLinks 2: [DOC-001 Table 3 — PDF p. 7](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=7)
- sourceLinks 3: [DOC-001 Table 5 — PDF p. 9](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=9)
- sourceLinks 4: [DOC-003 eTable 1 note — PDF p. 3](../../../2018/jama.2018.6496/joi180054supp2_prod.pdf#page=3)
- sourceLinks 5: [DOC-003 postintubation form — PDF p. 10](../../../2018/jama.2018.6496/joi180054supp2_prod.pdf#page=10)
- evidencePaths 0: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.6496/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The planned cuff-inflation and reported blade-removal events may have been harmonized or intentionally changed, but no amendment/equivalence rule is supplied. The data form corroborates the reported operational event; it is not a separately counted protocol-versus-manual discrepancy. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C003 |
| key | 2018::jama.2018.6496::C003 |
| legacyRelationship |  |
| locations | DOC-002 protocol secondary outcomes — PDF p. 9; DOC-002 protocol measurement procedure — PDF p. 10; DOC-001 Table 3 — PDF p. 7; DOC-001 Table 5 — PDF p. 9; DOC-003 eTable 1 note — PDF p. 3; DOC-003 postintubation form — PDF p. 10. |
| originalCrossDocument | 0 |
| package | jama.2018.6496 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | The protocol ends hypoxemia surveillance one minute after ETT-cuff inflation, while the published materials end it one minute after intubation-attempt completion; the supplied package does not document whether those events were treated as equivalent or whether the definition changed. The reported article/results definition is compared substantively with the supplied protocol or SAP. |
| reportHref | ../../2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C003 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol ends hypoxemia surveillance one minute after ETT-cuff inflation, while the published materials end it one minute after intubation-attempt completion; the supplied package does not document whether those events were treated as equivalent or whether the definition changed. |
| submissionInvolved | 0 |
| subtype | outcome\_surveillance\_window |
| suggestedDomain | protocol\_report |
| title | Protocol and published hypoxemia observation windows use different endpoint events |
| year | 2018 |
| ai\_source | meta\_report/consistency\_reclassification\_2026-09-04/reclassified\_candidates.json |
| ai\_relationship | P\_R |
| ai\_domain | protocol\_report |
| ai\_disposition | retain |

## Candidate C004

**Protocol and published first-attempt-duration measures use different endpoint events**

| Reference | Value |
| --- | --- |
| Candidate key | 2018::jama.2018.6496::C004 |
| Frozen relationship | P\_R |
| AI suggested domain | protocol\_report |
| AI suggested disposition | retain |

### Source location

> DOC-002 protocol — PDF p. 9; DOC-001 outcome methods — PDF p. 3; DOC-001 Table 3 — PDF p. 7; DOC-003 eTable 1 note — PDF p. 3; DOC-003 data form — PDF p. 10.

### Candidate statement

> The protocol defines first-attempt time to intubation through ETT-cuff inflation, whereas the published analyses use blade removal; the supplied package does not document how or why the measurement endpoint changed.

### AI rationale

> The protocol defines first-attempt time to intubation through ETT-cuff inflation, whereas the published analyses use blade removal; the supplied package does not document how or why the measurement endpoint changed. The reported article/results definition is compared substantively with the supplied protocol or SAP.

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

> The protocol defines first-attempt time to intubation from attempt start through ETT-cuff inflation with the tube in the trachea. The article and eTable define duration from laryngoscope-blade insertion through blade removal and report all-patient medians of 38 versus 36 seconds. The data form also identifies blade removal as attempt end.

#### Evidence 1: Reported-versus-comparator

> The start event is compatible. The planned endpoint is cuff inflation; the published endpoint is blade removal. The latter can define a different time scale and a duration for failed attempts.

#### Evidence 2: Calculation

> No numeric recalculation is applicable. The patient-level difference would be time(blade removal) - time(cuff inflation), but neither paired timestamps nor a defined equivalence are supplied.

#### Evidence 3: Alternative source-grounded interpretations

> The final analysis may deliberately use blade removal so failed attempts receive a duration, or the labels may refer to a harmonized timing procedure not described in the sources. Repetition in article, supplement, and form supports use of the published operational measure but does not document its relation to the protocol endpoint.

### Source links

- sourceLinks 0: [DOC-002 protocol — PDF p. 9](../../../2018/jama.2018.6496/joi180054supp1_prod.pdf#page=9)
- sourceLinks 1: [DOC-001 outcome methods — PDF p. 3](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=3)
- sourceLinks 2: [DOC-001 Table 3 — PDF p. 7](../../../2018/jama.2018.6496/jama_driver_2018_oi_180054.pdf#page=7)
- sourceLinks 3: [DOC-003 eTable 1 note — PDF p. 3](../../../2018/jama.2018.6496/joi180054supp2_prod.pdf#page=3)
- sourceLinks 4: [DOC-003 data form — PDF p. 10](../../../2018/jama.2018.6496/joi180054supp2_prod.pdf#page=10)
- evidencePaths 0: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/source\_inventory.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/source_inventory.md)
- evidencePaths 1: [2018/jama.2018.6496/.ai\_paper\_validation/review\_1\_5\_2/verification/evidence\_recheck.md](../../../2018/jama.2018.6496/.ai_paper_validation/review_1_5_2/verification/evidence_recheck.md)

[Original Markdown report](../../../2018/jama.2018.6496/.ai_paper_validation/final_report_1_5_2.md)

### Relationship records

| kind | order | relationship |
| --- | --- | --- |
| relations | 0 | P\_R |

### Source metadata

All catalog fields are preserved below. Historical paths are provenance strings; use the clickable links above to open files.

| Catalog field | Original value |
| --- | --- |
| additionalSensitivityExclude | 0 |
| ambiguity | The planned cuff-inflation and reported blade-removal events may have been harmonized or intentionally changed, but no amendment/equivalence rule is supplied. The data form corroborates the reported operational event; it is not a separately counted protocol-versus-manual discrepancy. |
| broadPlanInvolved | 1 |
| category | Measure, label, or scale inconsistency |
| currentReportCrossDocument | 1 |
| id | C004 |
| key | 2018::jama.2018.6496::C004 |
| legacyRelationship |  |
| locations | DOC-002 protocol — PDF p. 9; DOC-001 outcome methods — PDF p. 3; DOC-001 Table 3 — PDF p. 7; DOC-003 eTable 1 note — PDF p. 3; DOC-003 data form — PDF p. 10. |
| originalCrossDocument | 0 |
| package | jama.2018.6496 |
| planMechanism | endpoint\_definition\_window\_hierarchy |
| primary | P\_R |
| rationale | The protocol defines first-attempt time to intubation through ETT-cuff inflation, whereas the published analyses use blade removal; the supplied package does not document how or why the measurement endpoint changed. The reported article/results definition is compared substantively with the supplied protocol or SAP. |
| reportHref | ../../2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.html |
| reportPath | 2018/jama.2018.6496/.ai\_paper\_validation/final\_report\_1\_5\_2.md |
| sourceId | C004 |
| sourceStatus | Pending Human Adjudication |
| statement | The protocol defines first-attempt time to intubation through ETT-cuff inflation, whereas the published analyses use blade removal; the supplied package does not document how or why the measurement endpoint changed. |
| submissionInvolved | 0 |
| subtype | duration\_endpoint\_definition |
| suggestedDomain | protocol\_report |
| title | Protocol and published first-attempt-duration measures use different endpoint events |
| year | 2018 |
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
